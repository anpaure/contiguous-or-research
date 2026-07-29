#!/usr/bin/env python3
"""Standard-library replay of the canonical exact k=15 certificate.

This audit deliberately imports neither the factor/search implementation nor
either retained word verifier.  It hash-pins the construction artifacts,
reconstructs the advertised opened middle path from the saved physical
components, checks the depth-three OR identities, and directly enumerates all
literal interval unions of the canonical word.
"""

from __future__ import annotations

from collections import Counter
from hashlib import sha256
from itertools import combinations
import json
from math import comb
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FACTOR_DIR = ROOT / "scratch/k15_fixed_matching_pbbs_resident_20260729"
WORD = ROOT / "answers/k15.word"
WORD_COPY = FACTOR_DIR / "arbitrary_seams.s44.t12863.word"
FACTOR = FACTOR_DIR / "from3_markov_s7_merge.best.json"
FACTOR_AUDIT = FACTOR_DIR / "from3_markov_s7_merge.independent.audit.json"
COMPONENTS = FACTOR_DIR / "from3_markov_s7_merge.components.json"
COMPILER_AUDIT = FACTOR_DIR / "arbitrary_seams_compile.audit.json"

EXPECTED = {
    WORD: "f35da2f0c98ec07de3e5318554157af490558e881be5c8bbcb5e3d1c8c08b14b",
    WORD_COPY: "f35da2f0c98ec07de3e5318554157af490558e881be5c8bbcb5e3d1c8c08b14b",
    FACTOR: "0c11aefbfe3a0661c457b48f0a7a82afacc6d02d4362e23e5d710bb799135555",
    FACTOR_AUDIT: "c5f700aef824b93e257957c313a7395eb3d2512c773e6d434f08934ba93ac6f4",
    COMPONENTS: "f765d52aa68810af0e4897c6881f46ecf016b86394341a97f894dc6b53058151",
    COMPILER_AUDIT: "5eeb04a61d8a085e89b05db9ca1075cfd64e5f95a9a35bcbb80711617579d125",
}

K, R, DEPTH = 15, 8, 3
WIDTH = comb(K, R)
FULL = (1 << K) - 1


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def derivative(row: list[int]) -> list[int]:
    return [left | right for left, right in zip(row, row[1:])]


def derive(row: list[int], depth: int) -> list[int]:
    answer = row
    for _ in range(depth):
        answer = derivative(answer)
    return answer


def rank_layer(rank: int) -> set[int]:
    return {
        sum(1 << coordinate for coordinate in chosen)
        for chosen in combinations(range(K), rank)
    }


def maximal_erosion(middle: list[int]) -> list[int]:
    answer = []
    for position in range(len(middle) + DEPTH):
        value = FULL
        lo = max(0, position - DEPTH)
        hi = min(len(middle) - 1, position)
        for source in range(lo, hi + 1):
            value &= middle[source]
        answer.append(value)
    return answer


def residence_violations(middle: list[int]) -> int:
    bad = 0
    for coordinate in range(K):
        bit = 1 << coordinate
        index = 0
        while index < len(middle):
            if not middle[index] & bit:
                index += 1
                continue
            end = index + 1
            while end < len(middle) and middle[end] & bit:
                end += 1
            if index > 0 and end < len(middle) and end - index <= DEPTH:
                bad += 1
            index = end
    return bad


def fixed_shadow_holes(middle: list[int]) -> tuple[dict[str, int], dict[str, int], dict[str, list[int]]]:
    lower_holes: dict[str, int] = {}
    upper_holes: dict[str, int] = {}
    lower_missing: dict[str, list[int]] = {}
    for q in range(1, R):
        lower = set()
        upper = set()
        for start in range(len(middle) - q):
            lo, up = FULL, 0
            for value in middle[start : start + q + 1]:
                lo &= value
                up |= value
            if lo.bit_count() == R - q:
                lower.add(lo)
            if up.bit_count() == R + q:
                upper.add(up)
        wanted_lower = rank_layer(R - q)
        wanted_upper = rank_layer(R + q)
        missing = sorted(wanted_lower - lower)
        lower_missing[str(q)] = missing
        lower_holes[str(q)] = len(missing)
        upper_holes[str(q)] = len(wanted_upper - upper)
    return lower_holes, upper_holes, lower_missing


def direct_interval_cover(word: list[int]) -> tuple[int, int]:
    covered = bytearray(1 << K)
    enumerated = 0
    for start in range(len(word)):
        value = 0
        for end in range(start, len(word)):
            value |= word[end]
            enumerated += 1
            covered[value] = 1
            if value == FULL:
                break
    missing = sum(not covered[value] for value in range(1, FULL + 1))
    return enumerated, missing


def main() -> None:
    for path, expected in EXPECTED.items():
        actual = digest(path)
        if actual != expected:
            raise ValueError(f"hash mismatch for {path}: {actual}")
    if WORD.read_bytes() != WORD_COPY.read_bytes():
        raise AssertionError("canonical word and retained compiler word differ")

    factor_audit = json.loads(FACTOR_AUDIT.read_text())
    if factor_audit.get("status") != "PASS":
        raise AssertionError("frozen factor audit is not PASS")
    if factor_audit.get("candidate_sha256") != EXPECTED[FACTOR]:
        raise AssertionError("factor audit points at another candidate")

    component_payload = json.loads(COMPONENTS.read_text())
    if component_payload.get("candidate_sha256") != EXPECTED[FACTOR]:
        raise AssertionError("component file points at another candidate")
    cycles = [list(map(int, row)) for row in component_payload["middle_components"]]
    if list(map(len, cycles)) != [6390, 45]:
        raise AssertionError("physical component lengths changed")

    cut0, reverse0 = 22, 0
    cut1, reverse1 = 41, 1
    if reverse0 != 0 or reverse1 != 1:
        raise AssertionError("advertised orientations changed")
    opened0 = cycles[0][cut0 + 1 :] + cycles[0][: cut0 + 1]
    opened1 = [cycles[1][(cut1 - offset) % len(cycles[1])] for offset in range(len(cycles[1]))]
    expected_middle = opened0 + opened1

    word = [int(token) for token in WORD.read_bytes().split()]
    if len(word) != WIDTH + DEPTH:
        raise AssertionError("canonical word has the wrong length")
    if any(value <= 0 or value > FULL for value in word):
        raise AssertionError("canonical word has an empty or out-of-range letter")
    middle = derive(word, DEPTH)
    if middle != expected_middle:
        raise AssertionError("third derivative is not the certified opening")
    if len(middle) != WIDTH or set(middle) != rank_layer(R):
        raise AssertionError("third derivative is not exactly the middle layer")

    cut_colours = [
        cycles[0][cut0] & cycles[0][(cut0 + 1) % len(cycles[0])],
        cycles[1][cut1] & cycles[1][(cut1 + 1) % len(cycles[1])],
    ]
    if cut_colours != [18553, 18033]:
        raise AssertionError("cut-colour ledger changed")
    seam_at = len(opened0) - 1
    seam_left, seam_right = middle[seam_at], middle[seam_at + 1]
    seam_colour = seam_left & seam_right
    if (seam_left ^ seam_right).bit_count() != 2 or seam_colour != 17017:
        raise AssertionError("winning seam is no longer the certified Johnson seam")
    if seam_colour in cut_colours:
        raise AssertionError("winning seam unexpectedly recycles a cut colour")

    erosion = maximal_erosion(middle)
    if derive(erosion, DEPTH) != middle:
        raise AssertionError("maximal erosion does not differentiate to the middle path")
    if derivative(word) != derivative(erosion):
        raise AssertionError("compiled word violates the exact one-core equation DA=DP")
    if word[0] != cut_colours[0] or word[-1] != cut_colours[1]:
        raise AssertionError("the two cut colours are not pinned at opposite endpoints")
    if residence_violations(middle):
        raise AssertionError("middle chronology has a short internal coordinate run")

    lower_holes, upper_holes, lower_missing = fixed_shadow_holes(middle)
    expected_lower = {str(q): (2 if q == 1 else 0) for q in range(1, R)}
    if lower_holes != expected_lower:
        raise AssertionError(f"unexpected lower-shadow ledger: {lower_holes}")
    if lower_missing["1"] != [18033, 18553]:
        raise AssertionError("the two lower-q1 holes changed")
    if any(upper_holes.values()):
        raise AssertionError("middle chronology has an upper fixed-window hole")

    enumerated, missing = direct_interval_cover(word)
    if missing:
        raise AssertionError(f"canonical word misses {missing} nonempty masks")

    lower_ideal = sum(comb(K, rank) for rank in range(1, R))
    delay = 0
    while delay * WIDTH + comb(delay + 1, 2) < lower_ideal:
        delay += 1
    if (lower_ideal, delay, WIDTH + delay) != (16383, 3, 6438):
        raise AssertionError("deadline lower-bound arithmetic changed")

    compiler_audit = json.loads(COMPILER_AUDIT.read_text())
    compiled = compiler_audit.get("compiled_rows", [])
    if len(compiled) != 1:
        raise AssertionError("expected one retained successful compiler row")
    winner = compiled[0]
    compiler = winner.get("compiler", {})
    if (
        winner.get("source_state"),
        winner.get("target_state"),
        compiler.get("status"),
        compiler.get("output_sha256"),
    ) != (44, 12863, "VERIFIED_OPTIMAL", EXPECTED[WORD]):
        raise AssertionError("compiler provenance does not identify the canonical word")

    middle_payload = " ".join(map(str, middle)).encode() + b"\n"
    result = {
        "schema": "ad-k15-exact-6438-certificate-scope-audit-v1",
        "status": "PASS",
        "k": K,
        "word": str(WORD.relative_to(ROOT)),
        "word_sha256": EXPECTED[WORD],
        "word_length": len(word),
        "covered_nonempty_masks": FULL,
        "missing_masks": 0,
        "enumerated_intervals_until_full": enumerated,
        "deadline_lower_bound": {
            "rank": R,
            "width": WIDTH,
            "lower_ideal": lower_ideal,
            "depth": delay,
            "B": WIDTH + delay,
            "depth_minus_one_capacity": (delay - 1) * WIDTH + comb(delay, 2),
            "depth_capacity": delay * WIDTH + comb(delay + 1, 2),
        },
        "factor_sha256": EXPECTED[FACTOR],
        "factor_audit_sha256": EXPECTED[FACTOR_AUDIT],
        "components_sha256": EXPECTED[COMPONENTS],
        "compiler_audit_sha256": EXPECTED[COMPILER_AUDIT],
        "component_lengths": list(map(len, cycles)),
        "cuts": [cut0, cut1],
        "orientations": [reverse0, reverse1],
        "cut_colours": cut_colours,
        "seam_colour": seam_colour,
        "seam_recycles_cut_colour": False,
        "middle_sha256": sha256(middle_payload).hexdigest(),
        "middle_width": len(middle),
        "middle_layer_exact": True,
        "middle_residence_violations": 0,
        "lower_holes": lower_holes,
        "upper_holes": upper_holes,
        "DA_equals_DP": True,
        "boundary_pins": [
            {"position": 0, "target": word[0]},
            {"position": len(word) - 1, "target": word[-1]},
        ],
        "proof_scope": (
            "The equality nu(15)=6438 uses only the proved deadline lower "
            "bound and the literal word check. Factor, seam-census, and "
            "CP-SAT artifacts are independently replayed provenance, not "
            "trusted proof dependencies."
        ),
    }
    result["audit_sha256"] = sha256(
        json.dumps(result, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
