#!/usr/bin/env python3
"""Light hostile binding replay for the frozen root5 F208 union theorem."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


EXPECTED = {
    "/dev/shm/q4z17_root5_f208_allowed_rows_leaf9196.txt": "f7966bdb17b3ac79a5d13bffc5fe3f76fc78fd3a29a30da0e01e5a4983dbd30c",
    "/dev/shm/q4z17_reflect_sample0_augmented255k_leaf9196.dat": "78b5eff17642880681e156bbecb52405a3254f985b60e8e61fdb033e1979a7c9",
    "scratch/search_q4_k17_root5_f208_complete_target_union_atlas_leaf9196_20260815.h100.json": "b87e920ca6bbb5fdcc94bae5d05a7ead5e03f6a5e3c23000d3173908e7c327f9",
    "/dev/shm/q4z17_root5_f208_atlas_leaf9196_all.tsv": "973330a5ec497a8a834b8cac8f11797592fdc5d73503cd9e95fc45b435e45a76",
    "/dev/shm/q4z17_root5_f208_atlas_leaf9196_new.tsv": "6ed4d58e0dc88ab4c394e189395f9ebae650d20ec52ed5c5b3f6fa0fc1e5145e",
    "scratch/audit_q4_k17_root5_f208_complete_target_union_atlas_leaf9196_20260815.h100.json": "7b58b3f235c82a4217b617bb7cff97bd2d737fa5835d10e50fc3bc03cdfc5369",
    "scratch/search_q4_k17_owner_targeted_reflection_pairs_20260814.cpp": "861527ebce2d0f6a3aa7edbb070dd5e57ddb832f5a9786bcd12483d904d4db14",
    "/dev/shm/search_q4_k17_owner_targeted_reflection_pairs": "2874480130e9e27a71115f82f00c3f4b234da9a8f94b4b9922d8b9a20b57560c",
    "scratch/build_q4_k17_root5_f208_complete_target_union_atlas_20260815.py": "553900a33d9cc37153f5af210d4ea1cf5349e69d18cfa54c4fc8ec673f142f1f",
    "scratch/audit_q4_k17_root5_f208_complete_target_union_atlas_20260815.py": "6dc10771c0bd56659997019978f76b6a78f8845f34e65d3119002fe4301a6f07",
    "/dev/shm/q4z17_root5_f208_atlas_leaf9196_rows/row661.h100.json": "0b9b89133ab1953f47848cf852dd2ef1d491ed80b1ed345fc8da25a5e7e73459",
    "/dev/shm/q4z17_root5_f208_atlas_leaf9196_rows/row661.h100.tsv": "dc9aab41f80c418f85aa845a6abd126bc6b4fef66394f3d877a2b1ef45ca3dd8",
    "/dev/shm/q4z17_reflect_sample0_root5_f208_fullatlas.dat": "cc97b4fb16040c965f923e6ce9c847e254a0307693d5c2eaec0b616c601c2f3a",
    "scratch/audit_q4_k17_z17_root5_f208_fullatlas_build_20260815.h100.json": "596636546cbcf88d7ed7a1208ce9a001804e0f26d5808f5fc5b27f2fe1dd5105",
    "scratch/audit_q4_k17_root5_f208_fullatlas_append_replay_20260815.py": "3f70cd5587189edfac13a9467e4773585b7df4f11318220784a862cf1ee941de",
    "scratch/audit_q4_k17_root5_f208_fullatlas_append_replay_20260815.h100.json": "2a73e42bee4e3593f40dbdaf8d1481b6e6fec7a92ddece588512e523dc251ae7",
    "scratch/audit_q4_k17_root5_f208_fullatlas_k20_manifest_20260815.json": "29c490c1cbcb3bb6ff9068e5d950a05f2c633453026a27e546900c1b42344923",
    "scratch/audit_q4_k17_root5_f208_fullatlas_row661_pivots_20260815.json": "ce5530bf6eb2271af5a3ede31f4a8eaaa283f85bb2e72f26079a6709dd0010a2",
    "/dev/shm/q4z17_root5_f208_fullatlas_pivot_satfirst30/summary.json": "4d29d90465fad2b22df6788e36f3dc512c58eb500a71fb7c5e48bca5c19a2281",
    "scratch/audit_q4_k17_root5_f208_fullatlas_pivot_satfirst30_replay_20260815.h100.json": "895e12d9dc9a406ae7fa84383dabc89418e724e1027726600234d56149eca30f",
    "scratch/audit_q4_k17_z17_root5_f208_fullatlas_patch600s8677123_20260815.h100.json": "accb7c1109d1a2daf0b97ea58435d957254199136f180f96b408b9f436aea164",
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def load(path: str) -> dict:
    with Path(path).open(encoding="ascii") as stream:
        return json.load(stream)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--theorem", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    observed = {}
    for name, expected in EXPECTED.items():
        actual = sha256(Path(name))
        assert actual == expected, (name, actual, expected)
        observed[name] = actual

    with Path(args.theorem).open(encoding="utf-8") as stream:
        theorem = stream.read()
    for digest in EXPECTED.values():
        assert digest in theorem
    assert "10,006 complete allowed masks = 7,919 frozen + 2,087 new" in theorem
    assert "The per-target record sum is 100,060" in theorem
    assert "The total is 1,014 pivots" in theorem

    atlas = load("scratch/search_q4_k17_root5_f208_complete_target_union_atlas_leaf9196_20260815.h100.json")
    assert atlas["status"] == "PASS"
    assert atlas["allowed_row_count"] == len(atlas["target_rows"]) == 208
    assert atlas["unique_pair_masks"] == 10006
    assert atlas["frozen_pair_masks"] == 7919
    assert atlas["genuinely_new_pair_masks"] == 2087
    assert atlas["per_target_record_sum"] == 100060
    assert atlas["tenfold_membership_histogram"] == {"10": 10006}
    assert len(atlas["per_target"]) == 208

    atlas_audit = load("scratch/audit_q4_k17_root5_f208_complete_target_union_atlas_leaf9196_20260815.h100.json")
    assert atlas_audit["status"] == "PASS"
    assert atlas_audit["unique_pair_masks"] == 10006
    assert atlas_audit["frozen_pair_masks"] == 7919
    assert atlas_audit["genuinely_new_pair_masks"] == 2087
    assert atlas_audit["literal_witness_replays"] == 112153
    assert atlas_audit["every_mask_seen_at_exactly_its_ten_target_rows"]

    row661 = next(entry for entry in atlas["per_target"]
                  if entry["target_row"] == 661)
    assert row661["unique_pair_masks"] == row661["frozen_pair_masks"] == 144
    assert row661["new_pair_masks"] == 0

    append = load("scratch/audit_q4_k17_root5_f208_fullatlas_append_replay_20260815.h100.json")
    assert append["status"] == "PASS"
    assert append["base_pair_masks"] == 277960
    assert append["appended_pair_masks"] == 2087
    assert append["full_pair_masks"] == 280047
    assert append["base_prefix_identical"]
    assert append["ordered_appended_suffix_equals_new_catalog"]

    branches = load("scratch/audit_q4_k17_root5_f208_fullatlas_k20_manifest_20260815.json")
    assert branches["status"] == "PASS" and len(branches["branches"]) == 10
    expected_self = [[3309, 3361], [3309, 3425], [3309, 3428],
                     [3309, 3429], [3309, 3438], [3309, 3439],
                     [3316, 3361], [3316, 3425], [3316, 3428],
                     [3316, 3439]]
    assert [branch["self_indices"] for branch in branches["branches"]] == expected_self
    assert all(branch["residual_rows"] == 200 for branch in branches["branches"])
    assert all(661 not in branch["self_rows"] for branch in branches["branches"])

    pivots = load("scratch/audit_q4_k17_root5_f208_fullatlas_row661_pivots_20260815.json")
    assert pivots["status"] == "PASS" and len(pivots["branches"]) == 10
    pivot_counts = [branch["pivot_count"] for branch in pivots["branches"]]
    assert pivot_counts == [105, 97, 101, 104, 106, 102, 104, 94, 100, 101]
    assert sum(pivot_counts) == 1014
    assert all(branch["immediate_component_cuts"] == 0
               for branch in pivots["branches"])
    assert all(branch["component_count_histogram"] == {"1": branch["pivot_count"]}
               for branch in pivots["branches"])

    campaign = load("/dev/shm/q4z17_root5_f208_fullatlas_pivot_satfirst30/summary.json")
    assert campaign["status"] == "PASS" and campaign["graphs"] == 1014
    assert len(campaign["records"]) == 1014
    assert {record["status"] for record in campaign["records"]} == {"UNKNOWN"}
    assert not campaign["sat_found"]
    campaign_replay = load("scratch/audit_q4_k17_root5_f208_fullatlas_pivot_satfirst30_replay_20260815.h100.json")
    assert campaign_replay["status"] == "PASS"
    assert campaign_replay["result_count"] == 1014
    assert not campaign_replay["sat_certificates"]

    cp = load("scratch/audit_q4_k17_z17_root5_f208_fullatlas_patch600s8677123_20260815.h100.json")
    assert cp["status"] == cp["patch_summary"]["status"] == "UNKNOWN"
    assert cp["patch_summary"]["eligible_pairs"] == 10006
    assert cp["patch_summary"]["eligible_self"] == 8
    assert cp["patch_summary"]["free_rows"] == 208

    result = {
        "status": "PASS",
        "scope": "hostile hash and semantic replay of the frozen F208 union package",
        "theorem": str(Path(args.theorem).resolve()),
        "theorem_sha256": sha256(Path(args.theorem)),
        "bound_artifacts": len(observed),
        "atlas_masks": 10006,
        "frozen_masks": 7919,
        "new_masks": 2087,
        "target_catalogues": 208,
        "per_target_records": 100060,
        "literal_witness_replays": 112153,
        "row661_masks": 144,
        "self_branches": 10,
        "row661_pivots": 1014,
        "bounded_pivot_status": "UNKNOWN",
        "monolithic_cp_status": "UNKNOWN",
        "owner_only_scope": True,
    }
    with Path(args.output).open("w", encoding="ascii") as stream:
        json.dump(result, stream, indent=2, sort_keys=True)
        stream.write("\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
