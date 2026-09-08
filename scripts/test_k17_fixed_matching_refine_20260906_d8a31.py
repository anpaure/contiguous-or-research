#!/usr/bin/env python3
"""Quick h100 tests. K17_REFINE_SEED names the isolated seed .txt snapshot."""

import copy
from dataclasses import replace
from hashlib import sha256
import json
import os
from pathlib import Path
import socket
import tempfile
from types import SimpleNamespace
import unittest

from ortools.sat.python import cp_model
import k17_fixed_matching_refine_20260906_d8a31 as refine


@unittest.skipUnless(socket.gethostname().split(".")[0].lower() in ("h100", "arboghast"), "h100-only tests")
class FixedMatchingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.seed = Path(os.environ["K17_REFINE_SEED"]).resolve(strict=True)
        cls.body = cls.seed.read_bytes()
        cls.data = json.loads(cls.seed.with_suffix(".json").read_bytes())
        cls.rows, cls.report, cls.source = refine.load_seed(cls.seed, cls.seed.with_suffix(".json"))
        cls.cat = refine.Catalogue(cls.rows)
        cls.model, cls.x, cls.missing, cls.census = refine.build_model(cls.cat, "optimize", 102)
        print("INITIAL_MODEL_CENSUS " + json.dumps(cls.census, sort_keys=True), flush=True)

    def test_seed_matches_every_saved_metric(self):
        self.assertEqual(self.report["quotient_score"], self.data["quotient_score"])
        self.assertEqual(self.report["physical_audit"], self.data["physical_audit"])
        self.assertEqual(self.report["quotient_score"]["missing_orbits"], [0, 102, 51, 48])
        self.assertEqual(self.report["quotient_score"]["physical_cycles"], 5)
        self.assertFalse(self.report["full_gates_pass"])

    def test_free_actions_and_literal_descriptors(self):
        for rank, count in ((7, 1144), (8, 1430), (9, 1430), (10, 1144)):
            reps = refine.representatives(rank)
            self.assertEqual(len(reps), count)
            for mask in reps:
                self.assertEqual(len({refine.rotate(mask, s) for s in range(17)}), 17)
        for a in self.cat.edges:
            low, base_added, _ = self.rows[a.lower]
            next_low = refine.rotate(self.rows[a.next][0], a.shift)
            self.assertNotEqual(a.next, a.lower)
            self.assertEqual(1 << a.ins, next_low & ~low)
            self.assertEqual(1 << a.delete, low & ~next_low)
            self.assertEqual(a.lmask, low & next_low)
            self.assertEqual(a.umask, low | (1 << base_added) | (1 << a.added))
            self.assertEqual(a.lmask.bit_count(), 7)
            self.assertEqual(a.umask.bit_count(), 10)
            self.assertEqual(a.l2, refine.canonical(a.lmask))
            self.assertEqual(a.u1, refine.canonical(a.umask))

    def test_complete_hint_is_solver_feasible(self):
        solver = cp_model.CpSolver()
        solver.parameters.num_search_workers = 1
        solver.parameters.max_time_in_seconds = 15
        solver.parameters.fix_variables_to_their_hinted_value = True
        status = solver.solve(self.model)
        self.assertEqual(status, cp_model.OPTIMAL, solver.response_stats())
        self.assertEqual(solver.objective_value, 102)
        self.assertEqual(len(self.model.proto.solution_hint.vars), len(self.model.proto.variables))
        self.assertEqual(sum(solver.boolean_value(v) for v in self.x), refine.N)
        print("COMPLETE_HINT_SOLVE " + solver.response_stats(), flush=True)

    def test_missing_flags_are_exact_both_directions(self):
        hint = self.model.proto.solution_hint
        for original in (0, 1):
            clone = self.model.clone()
            pos = next(i for i, var in enumerate(hint.vars)
                       if var >= len(self.x) and hint.values[i] == original)
            clone.proto.solution_hint.values[pos] = 1 - original
            solver = cp_model.CpSolver()
            solver.parameters.num_search_workers = 1
            solver.parameters.max_time_in_seconds = 15
            solver.parameters.fix_variables_to_their_hinted_value = True
            self.assertEqual(solver.solve(clone), cp_model.INFEASIBLE)

    def test_eager_phase_nogoods_and_voltage_triangles(self):
        selected = set(self.cat.seed_selection)
        counts = {}
        for kind, edges in refine.phase_nogoods(self.cat):
            self.assertFalse(selected.issuperset(edges))
            counts[kind] = counts.get(kind, 0) + 1
            a, b = (self.cat.edges[e] for e in edges[:2])
            low1 = refine.rotate(self.rows[a.next][0], a.shift)
            low2 = refine.rotate(self.rows[b.next][0], a.shift + b.shift)
            inserted = low1 & ~self.rows[a.lower][0]
            if kind == "bad2":
                self.assertEqual(inserted, low1 & ~low2)
            elif kind == "bad3":
                c = self.cat.edges[edges[2]]
                low3 = refine.rotate(self.rows[c.next][0], a.shift + b.shift + c.shift)
                self.assertEqual(inserted, low2 & ~low3)
        self.assertEqual(counts, self.census["phase_nogoods"])
        a = refine.Descriptor(0, 0, 0, 1, 1, 0, 5, 0, 0, 0, 0)
        b = replace(a, lower=1, next=2, shift=3)
        c = replace(a, lower=2, next=0, shift=13)
        cat = SimpleNamespace(edges=[a, b, c], by_lower=[[0], [1], [2]])
        self.assertEqual([ids for kind, ids in refine.phase_nogoods(cat) if kind == "zero_voltage_triangle"], [(0, 1, 2)])
        cat.edges[2] = replace(c, shift=12)
        self.assertFalse(any(kind == "zero_voltage_triangle" for kind, _ in refine.phase_nogoods(cat)))
        self.assertEqual(list(refine.positive_runs([1, 1, 1], 0)), [3])
        self.assertEqual(list(refine.positive_runs([1, 0, 1, 1], 0)), [3])

    def test_publication_roundtrip_and_m0_fail_closed(self):
        with tempfile.TemporaryDirectory(prefix="k17_d8a31_test_", dir=self.seed.parent) as tmp:
            directory = Path(tmp)
            best = refine.publish(directory, "initial", self.rows, self.rows, self.source, 102, 102, "optimize")
            published = Path(best["paths"]["body"]).read_bytes()
            self.assertEqual(published, self.body)
            reread, report, _ = refine.load_seed(Path(best["paths"]["body"]), Path(best["paths"]["json"]))
            self.assertEqual(reread, self.rows)
            self.assertEqual(report["quotient_score"], self.report["quotient_score"])
            self.assertEqual(best["body_sha256"], sha256(published).hexdigest())
            before = set(directory.iterdir())
            swapped = [(low, b, a) for low, a, b in self.rows]
            with self.assertRaisesRegex(ValueError, "M0 columns changed"):
                refine.publish(directory, "bad", swapped, self.rows, self.source, 102, 102, "optimize")
            with self.assertRaisesRegex(ValueError, "objective mismatch"):
                refine.publish(directory, "bad", self.rows, self.rows, self.source, 102, 101, "optimize")
            self.assertEqual(set(directory.iterdir()), before)

    def test_mismatched_serialization_rejected_and_seed_untouched(self):
        data = copy.deepcopy(self.data)
        data["choices"][0][2] = data["choices"][0][1]
        with self.assertRaisesRegex(ValueError, "choices disagree"):
            refine.decode_factor(self.body, data)
        with self.assertRaisesRegex(ValueError, "header/length"):
            refine.decode_factor(self.body + b"0 0 0\n", self.data)
        self.assertEqual(self.seed.read_bytes(), self.body)
        self.assertEqual(sha256(self.seed.with_suffix(".json").read_bytes()).hexdigest(), self.source["json_sha256"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
