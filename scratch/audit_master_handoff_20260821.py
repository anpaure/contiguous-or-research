#!/usr/bin/env python3
"""Mechanical audit for the self-contained MASTER_HANDOFF.

The literal finite word bodies are the only allowed external mathematical
data. This checker verifies their hashes and universality, checks the
internal-proof structure, and authenticates provenance hashes. It does not
replace the hostile line-by-line proof audits.
"""

from __future__ import annotations

import hashlib
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / (sys.argv[1] if len(sys.argv) > 1 else "MASTER_HANDOFF.md")

SOURCES = {
    "MATH_THEOREM_DIRECT_PUNCTURED_CONFIGURATION_PAIR_PROFILE_AND_CLUSTER_GATE_20260821.md":
        "22044dff7084c05db25f0dfa869cb583c85811748784af0cca5eba4a07debe92",
    "MATH_THEOREM_PUNCTURED_BOUNDARY_CODEGREE_VIA_GAP_REFINEMENT_20260821.md":
        "fb45d1430df211474f2dcd652214c7b7a0ee3faf97db5bf88a52605b25c800b2",
    "MATH_REDUCTION_PUNCTURED_BOUNDARY_POLYMER_TO_ANNEALED_REGENERATION_20260821.md":
        "a8970535db0b5b1d7fb29f4bdd73e2fe4b19ca09dd399ba4620973e8b062297a",
    "MATH_THEOREM_PUNCTURED_INDEPENDENT_RESIDUAL_DEGREE_VARIANCE_20260821.md":
        "6ca0a8e9eddbe1bd6c44dcab4e9c46e57dca34b1210bea1b565fcaee6a779261",
    "MATH_AUDIT_PUNCTURED_PURGE_CLUSTER_DRIFT_AND_RENORMALIZED_GATE_20260821.md":
        "91edb1bd3daf8119a437120f7f2553a0d688ed06d8a11664f7d4bb30cef27fac",
    "MATH_THEOREM_ISOLATED_EDGE_BITE_COUNT_CONCENTRATION_20260821.md":
        "13500a5f06c4328d5e860e9d50c97f8acdd377b488fb58ae8114f4fb310b0aa0",
    "MATH_THEOREM_AVERAGE_SCALE_MAX_DEGREE_PUNCTURED_NIBBLE_SUFFICIENCY_20260821.md":
        "9fd2dba4a3094c1b89d8a027ddc3e31f1f2849f876900fc82bc6cd493b308984",
    "MATH_THEOREM_BOOLEAN_ALTERNATING_GK_INTEGRAL_RETIREMENT_20260821.md":
        "ec05b81a0748f0a25e61b2ab2c71a58f8097791d7fec9094504fff26eee25103",
    "MATH_THEOREM_CAPACITY_C_DIRTY_WREATH_PRUNING_AND_FRAGMENT_COMPILER_20260821.md":
        "719ece8441b1549d0aad37c8e649b92bc72a5e4fdd5d8d91ab7d71cfc55045c6",
    "MATH_THEOREM_Q1_REPEAT_PURGE_PRESERVES_ALL_DEPTH_WREATH_COVERAGE_20260821.md":
        "08f70645868388282f356dc4c51e1bf791eeb3b4197edd09107c27f909c280b9",
    "MATH_THEOREM_PUNCTURED_INDEPENDENT_RESIDUAL_HIGH_MOMENTS_20260822.md":
        "5679873d53a34cb030a0c69c9ffedf047cbfa9bca32ca1eb08558af262efae6b",
    "MATH_THEOREM_SATURATING_RAINBOW_FIFO_RECUT_CRITERION_20260822.md":
        "b621b107608bdd4bfbb58fa06a981d9520f8007b563360701494cfa8aa1c43cf",
    "MATH_THEOREM_GATE_B_CAPACITY_THRESHOLD_AND_WEIGHTED_FIFO_SEAM_20260822.md":
        "d97b76162aa9d05ced8fc431452af90d11afca1ad3c4d46a5a9b5713773542aa",
    "MATH_THEOREM_PUNCTURED_FIXED_SLICE_HIGH_MOMENTS_AND_STOPPED_PALM_REDUCTION_20260822.md":
        "c5b4384d4e9747c4f532177a23d1448a1ff095730793aa0c54ba9baa484ca178",
    "MATH_REDUCTION_PUNCTURED_COVERDOWN_HOLE_ENRICHMENT_FLAG_ARCS_AND_SPECTRAL_CONE_20260822.md":
        "8497067c015b8420afda536ec828d1eafff4a472a41e01c792855251bc966bd6",
    "MATH_THEOREM_ROOTED_CONFLICT_EXPOSURE_DRIFT_AND_MICROBITE_HIERARCHY_20260822.md":
        "3dd0833d55be634149c54d8922d4bfe55860a65258f34d24af7b15b8a0937081",
    "MATH_THEOREM_CONFLICT_UNION_EXPOSURE_COMPRESSION_AND_INITIAL_COLLISION_20260822.md":
        "43291b67083914bb0c4d773404e9707dee1052d9fc2038f4f26d34b53c913dd8",
    "MATH_THEOREM_EXTERNAL_WINDOW_REGULARITY_AND_SURVIVOR_CATALOGUE_NO_GO_20260822.md":
        "a154213fcfb09585e16a2119546ca2acd40e3d368a57ed15e4f4a4b360980909",
    "MATH_REDUCTION_CURRENT_SCALE_EXTERNAL_ROW_PRODUCT_AND_SLICE_20260822.md":
        "bb3094799f9516fa7a260ba48798c03b6b244dfd60cdebd732a36d747a900aaf",
    "MATH_THEOREM_STOPPED_EXTERNAL_HIT_COMPENSATOR_AND_RELATIVE_PROTECTION_GATE_20260822.md":
        "6ee3f2d76c3091bf1b6bd44199a14d5047dd714f71c2a7a867d98d1c159cca76",
    "MATH_THEOREM_POST_PURGE_CENTERED_DEFECT_STABILITY_20260822.md":
        "5621f4042df3bf046efe78c1359a3046f3acb7a2bc950257a3076f797286439f",
    "scratch/verify_post_purge_centered_defect_stability_20260822.py":
        "6b88e4f67fb8fd5eee80dbfe109dbc03748640c26f09c7974ffa3e63219682d9",
    "MATH_REDUCTION_GATE_B_PALM_COLLISION_ENTROPY_AND_LATE_PROTECTION_20260822.md":
        "43ac38a4e0ebd0281a38193fe3cb40bc578e542e0aeae90daf2d76603c7e0758",
    "scratch/verify_gate_b_palm_collision_transport_20260822.py":
        "a77b20d98b33cfc0ad336bd735b1520b1093bd25af9300cff104b37cb6d9bb33",
    "MATH_THEOREM_GATE_B_PAIR_POTENTIAL_COMMON_BLOCKER_DRIFT_20260822.md":
        "0c5cddbfc370668dc2dd6a19bb73a8fc312f54d0ff2d66db5fc6d9fd77c31366",
    "scratch/verify_gate_b_pair_potential_common_blocker_drift_20260822.py":
        "9743a582a195faa59c516a0aca2d285835ca873bd9c28c80aafbcdf2fde95003",
    "MATH_THEOREM_GATE_B_FIRST_BLOCKER_CELL_COLLISION_DICHOTOMY_20260822.md":
        "c00695f1a15a46f300e62cd94a580792991ce8bea8d51a9dc8706ce9fa520141",
    "scratch/verify_gate_b_first_blocker_cell_collision_dichotomy_20260822.py":
        "f80d77217820a5018e68b357b1c84cba99da11b1cdc4cad680dfc7c5bf32a55a",
    "MATH_THEOREM_GATE_A_CONFLICT_VARIANCE_COMPANION_DUPLICATE_REDUCTION_20260822.md":
        "f5189436390153b46fd831194f256b51c64b2b63a7bfea8ef21c9208b0a1ff5c",
    "scratch/verify_gate_a_conflict_variance_reduction_20260822.py":
        "7fc05739117e8eb619f52e894487509c13d38f7eb1dd401f2125ff8a610d15bd",
    "MATH_REDUCTION_GATE_A_HIGH_EVEN_MOMENT_CAP_ONLY_SHADOW_LEDGER_20260822.md":
        "22fc1972797642896c0bc161ed4ec68954f5fa6d4963d761f6c75d39f51e863c",
    "scratch/verify_gate_a_high_even_moment_shadow_ledger_20260822.py":
        "e496f3868c7803998f4f0c2c0edeac11754cc8d80f7ebf2b5a61841e35a3663c",
    "MATH_REDUCTION_GATE_A_ROOTED_TWELVE_CARRIER_DOOB_DUPLICATE_AND_NO_FREEDMAN_20260822.md":
        "7180e0bc5d55a81d4360f295f966acd5b50168d879feaf5673c5cb31ee1f6490",
    "scratch/verify_gate_a_rooted_twelve_carrier_doob_duplicate_20260822.py":
        "39d03e9275732429821684d574f6efcf1fa4d4239b0d64093c25214941e04556",
    "MATH_AUDIT_GATE_A_LITERAL_TERMINAL_DOOB_EXACT_SLICE_20260822.md":
        "4da560ea98940d8ebf2b2b0ccc7de26198b5af744c8759a275a958c0ce1650c0",
    "scratch/verify_gate_a_literal_terminal_doob_exact_slice_20260822.py":
        "2b03c42f77402798321170e26330063534e12804810b4597df4e77b972e37980",
    "MATH_AUDIT_GATE_A_SCALAR_PALM_ONE_STEP_RECURSION_20260822.md":
        "538bc63d55db540e3c263c37f8cc9dcd0951a60cd340ac31add9d49d811ab033",
    "scratch/verify_gate_a_scalar_palm_recursion_20260822.py":
        "e2296852ee97d26ebb332a042c95f05f0b4c398963a4803666e1c1fd97059271",
    "MATH_REDUCTION_GATE_A_ROOT_HAZARD_EXTERNAL_UNION_AND_ONE_ROOT_DEFICIT_20260822.md":
        "e1497815383ac5aa6f12880fcd4e2d8a69f4d42af1f82ccbb8a4f9252c6eeb89",
    "scratch/audit_gate_a_external_union_decomposition_20260822.py":
        "0165207eda056a893a479297dcc75b942e8af5bf4a58a5961fd96d45c682e3c6",
    "MATH_THEOREM_GATE_A_FINITE_BITE_CARRIER_SURVIVAL_REMAINDER_20260822.md":
        "ac1605bd7f96c760dd33a8bdb144e18dffb694b7f88a89804ca774e621199ab5",
    "scratch/verify_gate_a_finite_bite_carrier_remainder_20260822.py":
        "3627c32cebf1f9a6e645155510772138028d76876dbcc4b0763825d2d680b729",
    "MATH_REDUCTION_GATE_A_UNCONDITIONED_RANDOM_CLOCK_MIXTURE_REFERENCE_20260822.md":
        "d316a9f356da891c3ba0d42d4de3114bd971995b8da59f6c858b6f93f7b69d4f",
    "scratch/verify_gate_a_random_clock_mixture_reference_20260822.py":
        "9a2c6743ddd1e8e0b60d102b3ae40a5495a402baf2ff967e471670f818664d41",
    "MATH_THEOREM_GATE_A_AVOIDANCE_EXTENSION_HIERARCHY_AND_EROSION_REBINNING_20260822.md":
        "1500b46e1877cfb22959035cf8b98afffd8f85e87fca20ee9420f62e32cb7bcc",
    "scratch/verify_gate_a_avoidance_extension_hierarchy_20260822.py":
        "9747a20ca70e136d4f13ea7ae3dd26b79d9b81b444e02946769ea13578bd3a9a",
    "MATH_THEOREM_FIFO_RAINBOW_FRACTIONAL_CIRCULATION_AND_QUOTA_ROUNDING_20260822.md":
        "8b16bb1630d8314ec9057d963b008c359b38a204f3957188d1f340de9768d5a1",
    "scratch/verify_fifo_rainbow_fractional_and_atom_quota_20260822.py":
        "ade510cbc2617ec0624d6612ba13b36d32f5fa0eace4487a3388fb64a500ecbb",
    "MATH_THEOREM_GATE_C_FRAGMENT_QUOTA_COMPILER_REOPENED_SCALE_20260822.md":
        "c2826f98a76b33d7d0864a8c3c3021197ea4a16efb511d3bb3c2013c6dcc4ce8",
    "scratch/verify_gate_c_fragment_quota_compiler_20260822.py":
        "ffde211c1e4f70aa670469d688fab9f191740b7da41f0f8adf7e2b52cc3fbfee",
    "MATH_THEOREM_COMPLETE_R4_COMPENSATED_Q2_CURRENT_SURJECTIVITY_20260822.md":
        "5b1597132cb75458535ab3dcb0364b828d845c9e12c96729d2e3245c15764164",
    "MATH_THEOREM_COMPLETE_R5_COMPENSATED_Q2_CURRENT_SURJECTIVITY_20260822.md":
        "547db22bfdd31197a81bb7d30da93d360cff40be91f97b11e96c733bc5467093",
    "scratch/verify_complete_r5_compensated_q2_surjectivity_20260822.cpp":
        "71f1de2d49ee56a57723460e94d1e9bae158a027bf003ab3fc59a9d1dcf99f10",
    "MATH_REDUCTION_ALL_R_COMPENSATED_GIBBS_SPECHT_GRAM_GATE_20260822.md":
        "9978b3df3b79cb2380550cf40f7e349ec84d7f9150d0dc72bc8c2eeb8c9dc897",
    "MATH_OBSTRUCTION_STANDARD_OUTPUT_FISHER_SCALE_AND_DIMENSIONLESS_GRAM_GATE_20260822.md":
        "91faaa3f1344227aeea8c40921693a7bbe5049efaa5e084f56353bcaa52f1bc6",
    "scratch/verify_depth_two_fisher_scale_obstruction_20260822.py":
        "670a2b0e558dbc50ae35873594c51169a8c3a7f13cc86849b1a0a339e3615494",
    "MATH_REDUCTION_COMPENSATED_GRAM_TO_EXPOSURE_INTERSECTION_HISTOGRAMS_20260822.md":
        "c4c60e9e47818cac32155aa76321a06fa027b9cbd5742e097343ef3e20a61af8",
    "MATH_REDUCTION_DEPTH_TWO_ORBIT_REGIMES_AND_EXPOSURE_GRAM_STABILITY_GATE_20260822.md":
        "95d21f3c8db579d672964de59065954896365bcadbca56a32db0d8d9fd411565",
    "scratch/verify_depth_two_orbit_regimes_20260822.py":
        "f680f79b9614f4d4173fd9203d15ded0a70dc40519757fa25a0e8c3b01ff6dcc",
    "MATH_REDUCTION_SECOND_ORDER_EXPOSURE_SIGNAL_AND_VENN_COUPLING_GATE_20260822.md":
        "7f708e830134c362a2636a698a502f0dd7794258722bdc67be93826ad703453e",
    "scratch/verify_exposure_zero_avoidance_decomposition_20260822.py":
        "a06326573b3ba46e5e3dd724918d5c4917d385cbaa8e9aa7ed480a28315686ab",
    "scratch/verify_r4_dimensionless_compensated_gram_angle_20260822.py":
        "7219d4cb792d9a9682ef1925014a9c4895662f36cc68c3a3d52583ee299acfe7",
    "scratch/research_r5_compensated_gram_angles_20260822.cpp":
        "5ea7a4764bd3eda8312b3522f6397da8f0b3853e1f1e74c799c5f3113e4f94f6",
    "MATH_REDUCTION_W2_HAHN_VENN_SCALAR_AND_HARMONIC_REMAINDER_20260822.md":
        "3b27bcda16358d56c98d6dc094f4a13108c41d638dd26e77e8840fc350866518",
    "scratch/research_w2_hahn_venn_exact_20260822.py":
        "8b7916edd570e7705b9154f88e66b0922d9d0f3ac05e1c8ed874eaac695c04d4",
    "MATH_THEOREM_GATE_B_CYCLIC_CENTRAL_FACTOR_AND_REMAINDER_SCALE_20260822.md":
        "5f293097eca1eb08711ee0e795f4ff833a8b66380ac86373be1de0c7b0f3ed76",
    "scratch/verify_gate_b_cyclic_central_factor_20260822.py":
        "eeb38634a09a8f8910f1dfc17db80ec3fa244c63cb11e7cc49e23dc770b0b74f",
    "MATH_THEOREM_GATE_B_ALL_MODULE_BOUNDARY_PROFILE_IDENTITY_20260822.md":
        "b08acf59f4a611782578f6adb34cb2c8bb5e029be6e7b78a1ad75318caac20bf",
    "scratch/verify_gate_b_all_module_boundary_profile_identity_20260822.py":
        "55ce14ec9c28b85ebb018f1d3765e11ef3a966bd70fb29499e14609468992fca",
    "scratch/research_gate_b_allj_boundary_averages_20260822.py":
        "f3a1e3e1cff2d585e20448e077adcc71d8b63918441b5936c7bff2430d31c2df",
    "MATH_THEOREM_GATE_B_W2_DELOCALIZED_INVERSE_AND_EXPOSURE_THRESHOLD_20260822.md":
        "edefd7a7ba708e694979b04bd7a926d785a6c0bbec218d00f3da00fb26a3182b",
    "scratch/verify_gate_b_w2_delocalized_inverse_and_exposure_threshold_20260822.py":
        "d649fb369f65b297fb0d6dc510919b5b3f3e1089b7865199a8ff0a89d8f0a1fc",
    "MATH_REDUCTION_GATE_B_FULL_EXPOSURE_ZERO_AVOIDANCE_BOUNDARY_QUOTIENT_20260822.md":
        "5fb7c524643230812521fbfd8a731271a8f19cb3397956806a83054a787256d9",
    "scratch/verify_gate_b_full_exposure_zero_avoidance_boundary_quotient_20260822.py":
        "d9929bfc16e5dcce095f770bff175d2349e6797864fc5605bc74b62e868f1194",
    "MATH_THEOREM_GATE_B_UNIFORM_ORBIT_FACTOR_WITNESS_20260822.md":
        "406e93356218b85d31f0816e2b555710e7fd883258d92194fd79bbd9eb2f3f0e",
    "scratch/verify_gate_b_uniform_orbit_witness_20260822.py":
        "494eccc95239fda982f28018e7511a19f48630989abd56cf7fdc89965dd86e4d",
    "MATH_REDUCTION_GATE_C_OFFSET_TRACK_MATCHING_20260822.md":
        "c18c4e7fa0d45c74e175ae18ddd548056ccff86a6a0c2e2cd13dc69aafbbba67",
    "scratch/verify_gate_c_offset_track_reduction_20260822.py":
        "6c5e362fb8148f7e3602905727ff14b676f7146516d286aa1cf191de51a7e675",
    "MATH_REDUCTION_GATE_C_MULTISCALE_VARIABLE_FRAGMENT_COMPILER_20260822.md":
        "af62ce90d2736bc4465b291f5316481faa7d7a9bc1e0e2d5bcc5edb54d05119b",
    "scratch/verify_gate_c_multiscale_variable_fragment_20260822.py":
        "e1e1b058cf8ac4fe0be7952d0caeaa5b38253f63b61b4650a75194e07f2cd33f",
    "MATH_REDUCTION_GATE_C_DIRECT_HOLE_AND_TWO_JUNTA_OBSTRUCTION_20260822.md":
        "c3dfa81094fd0d9d3b425d5c0884228865ebd58eb9e18883e10ea16162829f21",
    "scratch/verify_gate_c_direct_hole_and_two_junta_obstruction_20260822.py":
        "7740a6ad4c5f5882f6f183e41f91cdddb7a2a327e3de0496ed58482c992d1162",
    "MATH_REDUCTION_GATE_C_SLOW_COVERDOWN_AND_PHASE_PACKET_NORMAL_FORM_20260822.md":
        "eb76e3606850a31d9a0ca861a04b1c0917c41cedc3f49841e52dfe0586cb0e19",
    "scratch/verify_gate_c_slow_coverdown_and_phase_packet_20260822.py":
        "1b03b01a06f5ede9192d575223189c3287798d137abb9717696d6a4110c22cfb",
    "MATH_REDUCTION_GATE_C_PHASE_PACKET_HYPERCUBE_BANK_20260822.md":
        "443d49ec66bf7aae233e5428557fd5c561a3c439a0b1b741db4a9cf01c836fca",
    "scratch/verify_gate_c_phase_packet_hypercube_bank_20260822.py":
        "29ea364ebfaef01cacafad0a2b8e0049c4a8416d1c222d059d50ae52446977a2",
    "MATH_THEOREM_GATE_A_ONE_STEP_LAG_EROSION_ABSORPTION_20260822.md":
        "d61346a3932727273c6500a621342991c0f9ccc3138bce8fad5e682ffb75ae13",
    "scratch/verify_gate_a_one_step_lag_erosion_absorption_20260822.py":
        "8ef9d3723acbfbaae5d1a615f321fd0140c376dcb1ef0de57003d6466cb862e0",
    "MATH_THEOREM_GATE_A_CARRIER_HAZARD_BOUNDARY_CONDUCTANCE_20260822.md":
        "b888b3db045d63ef023bf93f11c67d5c31b4121d1f4b7eef74cf20690a1e8395",
    "scratch/verify_gate_a_carrier_hazard_boundary_conductance_20260822.py":
        "25b58edf54375b248ed3ed9b8cb194379fea31938357a731f77af770540a2610",
    "MATH_REDUCTION_GATE_B_ZERO_AVOIDANCE_SIXTEEN_LOCAL_ATOMS_20260822.md":
        "bfe167069665a142d520387daf465942d44d48962113991e0215ccce707192fa",
    "scratch/verify_gate_b_zero_avoidance_sixteen_local_atoms_20260822.py":
        "89197fd6df0346740e40ff3b459fddbf9371cbe3eabae574d12a90c98b701777",
    "MATH_THEOREM_GATE_C_ALL_PAIRING_COHERENT_TOUR_ORBIT_20260822.md":
        "08d6ae6f5de72e7cb4b47070084a5b8e356d2d8b2bbae336ba8a0da2ac77c81d",
    "scratch/verify_gate_c_all_pairing_coherent_tour_orbit_20260822.py":
        "16a8b8fe383705b803847a584c32ae6ee6dc3408e75c635ce126b3cf22e60aec",
    "MATH_OBSTRUCTION_GATE_C_GK_SCD_COHERENT_TOUR_20260822.md":
        "63f96f74c29bbd958ae06dcba7da0b9b23bf41794eec481d40299a84653d6a5a",
    "scratch/verify_gate_c_gk_scd_coherent_tour_obstruction_20260822.py":
        "9be9ff9a81fb474c5cbc9705e65b4076a95b8ef384d16124ae9c13850116f410",
    "MATH_THEOREM_GATE_C_NON_GK_SCD_HAMILTON_FLAG_REPAIR_20260822.md":
        "1ce99d86c71358ee99bef2901e62578051116767d1264c165d03a1e4d367cbec",
    "scratch/verify_gate_c_non_gk_scd_hamilton_flag_repair_20260822.py":
        "5068e9ea0e339dcd6a962a571e906bad3434de801809a397102438f7e7aee168",
    "MATH_REDUCTION_GATE_A_CONTEMPORANEOUS_NORMALIZED_EXPOSURE_20260822.md":
        "d10e69f6045b18def197c1ddfe57230daa27b2ce79d38726f737dc75ba5d1b18",
    "scratch/verify_gate_a_contemporaneous_normalized_exposure_20260822.py":
        "64c438e95e8a3ee40a2f4042d2126ec2029d02c8301e65eae7d3192782bbe268",
    "MATH_OBSTRUCTION_GATE_C_CYCLIC_MINIMUM_AND_ONE_ASCENT_SCARCITY_20260822.md":
        "5f77152c0193ea6147d5a1ba873921486e52743850ddca6bb4ccb42641d3cba0",
    "scratch/verify_gate_c_cyclic_minimum_and_one_ascent_scarcity_20260822.py":
        "1370d13f9fb385dd75c662b20c4af6530cb7321c756671a0a51eb69cbd7dec4b",
    "MATH_OBSTRUCTION_GATE_C_PARITY_DEFECT_BANDWIDTH_20260822.md":
        "4568f53c80d12a26839dc0c9b316dbf5ae736304f542843f2c4303cbd2739f12",
    "scratch/verify_gate_c_parity_defect_bandwidth_20260822.py":
        "3f09a6e1183772fe971bf9cf0eae5ed4b97331b0c36245d129e6fb543df2ee11",
    "MATH_OBSTRUCTION_GATE_B_J2_LOCAL_SCALE_AND_FIVE_VERTEX_BANK_20260822.md":
        "636671d28385d5f45fac299ab9f7ca48dbd4c01d7685e76883cfff40b3ae6564",
    "scratch/verify_gate_b_j2_local_scale_and_five_vertex_bank_20260822.py":
        "dab28604a36c517478db1529bb7a6ddb74ef532a1e24a26816d8a7d574736eab",
    "scratch/research_gate_b_local_atoms_fast_venn_20260822.py":
        "ac53061e70687df50e88f068e8feb517291edd9b388392aa298039d1423738fa",
    "MATH_OBSTRUCTION_GATE_C_ORDERED_GK_DIAMOND_FIXED_CUT_20260822.md":
        "48a2cccb69b845748331f41480c4799f65f357c3ca7a5c090a313dc11281def9",
    "scratch/verify_gate_c_ordered_gk_diamond_fixed_cut_20260822.py":
        "fd9b6956a119fb9e53caf14f7c599b4a0a72896a306b244e0174799a44d1e244",
    "MATH_REDUCTION_GATE_C_MESOSCOPIC_PARITY_STAIRCASE_20260822.md":
        "f80794bd80c97f9ccba5761778d4fa217f7652d523b9175d0e7c261741a9f21a",
    "scratch/verify_gate_c_mesoscopic_parity_staircase_20260822.py":
        "f133bcb97982684d2df763f74365129fdd0ddbfc1850190e12d7c01c384cfff1",
    "MATH_OBSTRUCTION_GATE_C_ONE_ASCENT_FULL_SUBLINEAR_SCARCITY_20260822.md":
        "4eb28533f98df3bfb35d15b0df0e20122e9a58e20281ef48569acf6976f32949",
    "scratch/verify_gate_c_one_ascent_full_sublinear_scarcity_20260822.py":
        "1558e3a2c260727ab72a1b0cfa7826a29f4958f6e53c25e56985958d16561d3c",
    "MATH_CORRECTION_GATE_A_SIGNED_REFERENCE_TAIL_CLUSTER_20260822.md":
        "46d1ab89c02e80ca08f81490a66b575733b07e899062798357b9de342faa7bf2",
    "scratch/verify_gate_a_punctured_reference_local_cluster_20260822.py":
        "740f50428f4dec18888278a1bb457f1bb4311edf25c30baebd4948bd754e41e6",
    "MATH_THEOREM_GATE_B_J3_FULL_PROFILE_FINITE_DIFFERENCE_20260822.md":
        "178c679e2e7610de1bb9f6de485d6cae90fe814ae101ff841e8214fa0aa3ba89",
    "scratch/verify_gate_b_j3_full_profile_finite_difference_20260822.py":
        "eadd91a5a77abcd73dda8ab19934c12f971628b21bcfecf60c72c31e2123d6d7",
    "MATH_THEOREM_GATE_C_ANTIPODAL_SWAP_FACTOR_ADAPTED_TOUR_20260822.md":
        "beea2a63ec579bd0b66944f6809471b4c686b45eeb7b6fd57a3167b551c1636a",
    "scratch/verify_gate_c_antipodal_swap_factor_adapted_tour_20260822.py":
        "93c5451686f3d7fc7e6cdc5db11b4cf9ea1e06802d5babcceba872974345a12b",
    "MATH_REDUCTION_GATE_C_GENERAL_ANTIPODAL_WREATH_PREFIX_ENTROPY_20260822.md":
        "8225b8a01db657f1e3be77d845076cde2035dc0e235e3e82e1b2fc0be64d450b",
    "scratch/verify_gate_c_general_antipodal_wreath_prefix_entropy_20260822.py":
        "9aa8bd8f49576dc402c2e9093e42b52f95c0b80b1accb3f12fd243c8ed8f8338",
    "MATH_OBSTRUCTION_GATE_A_PUNCTURED_HAZARD_DEGREE_MONOTONICITY_20260822.md":
        "de5ee6ffa9c4ffb3350fc92421a6a0f4b9249d3af83e49e7c3e977a3925126df",
    "scratch/verify_gate_a_punctured_hazard_degree_monotonicity_20260822.py":
        "1476dfbc1a8dc36d7fbeee9c800847803f1828131d8e6dfbe1d67d5f7e381421",
    "MATH_THEOREM_GATE_B_UNIFORM_ALLJ_LOCAL_DEFECT_CONDITIONING_20260822.md":
        "8a6ac590457ccd7c312cd5402959c2909dd4e061378784aabaa7c26483dbdd63",
    "scratch/verify_gate_b_uniform_allj_local_defect_conditioning_20260822.py":
        "5185c23f16dace0c5cdfceb69eb924fd5e59f74685bfcdaa5189423655411311",
    "MATH_REDUCTION_GATE_C_BLOCK_SHUFFLE_ROW_RIGIDITY_20260822.md":
        "9b05cc8ae7356e0850125752403bb811d79927092320902a3e666c12069015a5",
    "scratch/verify_gate_c_block_shuffle_row_rigidity_20260822.py":
        "7d824fc4ff2eebec3e1c82148e18b0fd368676ad041ff160aaff262ad5bf5dcc",
    "MATH_THEOREM_GATE_C_LOCAL_DECK_ENTROPY_COMMON_CORE_20260822.md":
        "93a0433ea1b7899a86f1f4cfb753e55d06cbc9ad322ede2d677a42059305fdaf",
    "scratch/verify_gate_c_local_deck_entropy_common_core_20260822.py":
        "e4c96afaa868138c686329ddd18bec58aa0e6c45885339727a29fc7c0a374c45",
    "MATH_OBSTRUCTION_GATE_A_PRODUCT_PALM_M12_SIMPSON_20260822.md":
        "43e75302afa35c377cc39116869dec2f2d4433b05d1121474cc6a92015ad4eaa",
    "scratch/verify_gate_a_product_palm_m12_simpson_20260822.py":
        "b4b7670ce0b0c4184145ae4118642d5b0745f316429712586651409f7f6e4af7",
    "MATH_REDUCTION_GATE_A_PUNCTURED_PRODUCT_CONNECTED_CARRIER_CLUSTER_20260822.md":
        "59787c85ba51eddb28d79e7adf52f221953cdc3de57f656aa73a986809798f9f",
    "scratch/verify_gate_a_punctured_product_connected_carrier_cluster_20260822.py":
        "9c39bcdc0d69a312fc7626a4c9477e80158a671458bb17449f211a204d1535f8",
    "MATH_REDUCTION_GATE_A_PUNCTURED_TAIL_MOBIUS_U_STATISTIC_20260822.md":
        "3bd95565eeb7bd9dcb55979351d824db408bfb36412eb796a3b3cf559d385fc8",
    "scratch/verify_gate_a_punctured_tail_mobius_u_statistic_20260822.py":
        "687d8e20b5c5ed7d43fc2b8da01d40d948260c92ea3a9fc3c3dbdf1479db070c",
    "MATH_REDUCTION_GATE_A_TWO_STAR_DIRECTIONAL_HOEFFDING_TAIL_RESPONSE_20260822.md":
        "51252b5b151c6aec368667df716f92837118a8563118cc52fc305eac7bfe2455",
    "scratch/verify_gate_a_two_star_directional_tail_response_20260822.py":
        "47f856d52fffe2a790d690a3b3a2e05e6b42826674920e95761dfdb013b41855",
    "MATH_REDUCTION_GATE_A_TWO_STAR_POSITION_WEIGHT_SIGNED_REGRESSION_20260822.md":
        "8ee04ad40011a346e27fa35a931b88e6e9c3c5d7fc702c29898a402e6b624e8f",
    "scratch/verify_gate_a_two_star_position_weight_regression_20260822.py":
        "80aa4f9582369304be5e6867a21fe1930bc2b28d43b5ad813547f697dd64ba4a",
    "MATH_REDUCTION_GATE_C_EQUAL_BLOCK_TWO_SIDED_BALLOT_RIGIDITY_20260822.md":
        "615091495a9a73d365f5ecca13252f14dd9c0ceaa8e5fb588f60701d4c33334f",
    "scratch/verify_gate_c_equal_block_two_sided_ballot_rigidity_20260822.py":
        "7a9616f53195d3fdaa76a39a1aac6f876f94b7695d1142cd60681c21f9711caa",
    "MATH_REDUCTION_GATE_C_BLOCK_GAP_WINDING_COORDINATES_20260822.md":
        "6bae2ba8a23a31aaf6373b0ffea0047cdda707a07732998adc10ebf11ac53d2a",
    "scratch/verify_gate_c_block_gap_winding_coordinates_20260822.py":
        "93cd5e2ef7eab08247724cdcdf3b6c5fb12a92d660845f907d161ed08d91ae68",
    "MATH_REDUCTION_GATE_C_SINGLE_ROOT_BALLOT_LAW_AND_MOMENT_GATE_20260822.md":
        "1738b1d5e9553ae80da0d64c2bb9d01229425dbd6dcccf19e86c492eee4673ce",
    "scratch/verify_gate_c_single_root_ballot_law_and_moment_gate_20260822.py":
        "bdcf5f5ea755e0529b331c614cec972d9b54f553dbc55bb09f98fb3aa8433c04",
    "MATH_THEOREM_GATE_B_SHORE_DIFFERENCE_CURRENT_AND_REMOTE_CONE_20260822.md":
        "5cc09a0b026b62f2c218a20b98dc96c261f3650753a883afa5d59d476b2c1e06",
    "scratch/verify_gate_b_shore_difference_current_20260822.py":
        "50e34d90f18e124b7bacb2ed9c44cef0b0568bef2070f73eb97bf20b33495cdc",
    "MATH_REDUCTION_GATE_C_MULTIROOT_GRID_AND_TWO_ROOT_FOUR_LETTER_20260822.md":
        "814885e2ac4895950e17be131a3b75303a338b2f0f502b41a0eca968e098cf55",
    "scratch/verify_gate_c_multiroot_grid_two_root_four_letter_20260822.py":
        "fa2ac5b62fb5da32d9a38c897b3a7cb7a986448724466a0213ef8d0281672d94",
    "MATH_THEOREM_GATE_C_PIVOT_FLIP_FACTORIAL_MOMENT_20260822.md":
        "ca98c35c1e934ba6583e0793c6181a531759e1e7d1971f7e4115dbd4c88c7f2f",
    "scratch/verify_gate_c_pivot_flip_factorial_moment_20260822.py":
        "4f6557f84f128540c33dffbcbb8ecd2ae1020883730d1d341f3d7f8c17800c88",
    "MATH_COROLLARY_GATE_C_PIVOT_MISS_SET_TAIL_20260822.md":
        "de8f8fdab80db6b4c3feba354a295762960b9dcf3b38a464704708d645a5f857",
    "scratch/verify_gate_c_pivot_miss_set_tail_20260822.py":
        "21014502681a749995eb7e8a12f5a3d81d8c923fa6df6e34e206a5c95f87a171",
    "MATH_THEOREM_GATE_B_J2_SIX_VERTEX_ROOTED_CORE_DETERMINANT_20260822.md":
        "867c9585122050cd5c3336861482d6954c0cbeb8d1a94df5d1753db45411e70f",
    "scratch/verify_gate_b_j2_six_vertex_rooted_core_determinant_20260822.py":
        "63e2015bb5c7a1fee3941ea473b2b37c2c1be5c8e009e522867b01805ea3d662",
    "MATH_THEOREM_GATE_C_UNEQUAL_ODD_BLOCK_WEIGHTED_EXCURSION_20260822.md":
        "8626c932e6ef4beff8621caec31f072751070228b253b677abed455ef49ae9dd",
    "scratch/verify_gate_c_unequal_odd_block_weighted_excursion_20260822.py":
        "f6d1a681ec5cb43d3480db3278bb205c6b6a5a5ba86c3dd7e02f9bd5cd134ce9",
    "MATH_THEOREM_GATE_C_ONE_GIANT_ENTROPY_COMMON_ATLAS_20260822.md":
        "81053a13711a697da83bae48dd8a6711d7808153d2019fd70509a4bb86996cdf",
    "scratch/verify_gate_c_one_giant_entropy_common_atlas_20260822.py":
        "afa288ab10f968f8bc645a53b6018a66c16b71e9cb7866d66d5db66c265c2b3c",
    "MATH_REDUCTION_GATE_A_TWO_STAR_TWO_SHORE_OVERLAP_CELLS_20260822.md":
        "2c219c45d76633f1c5ae5c16446ae23c65cde175f3452b0cd854b958d7986655",
    "scratch/verify_gate_a_two_star_overlap_cell_decomposition_20260822.py":
        "419e389cdd7e980c77e12e941bc8a0958ab606d42e7215882e1bf3effd52cf79",
    "MATH_OBSTRUCTION_GATE_C_FIXED_PAIRING_ATLAS_CAP_20260822.md":
        "64d28f9b139622ebf241ffdfe8279df9306c2e1730e608392e0040f7b618b23f",
    "scratch/verify_gate_c_fixed_pairing_atlas_cap_20260822.py":
        "82e4bf7ea7e3b0b78e2b582bb2db58dbfe300a7c197f5a1fc88271a1f97a52e1",
    "MATH_REDUCTION_GATE_A_FACTORIAL_PAIR_PALM_OFFROOT_DISJOINTNESS_20260822.md":
        "df9d1baf182835fdd1f045b561993dc3099d6bfd17396436e69ce9025513f662",
    "MATH_THEOREM_GATE_C_PAIRING_DEFECT_INCIDENCE_AND_MENU_20260822.md":
        "ea2ba36f43bdc4e5082ccdfb9ad482f095deba3ea9527e8b9e3076b8b11659a9",
    "scratch/verify_gate_c_pairing_defect_incidence_and_menu_20260822.py":
        "552990f2429c5b9462e3873cfe966e1506347f270f1aa139ff1eeddf3f143c37",
    "MATH_THEOREM_GATE_C_FIXED_ORDER_THREE_RANK_CAYLEY_BANK_20260822.md":
        "ec326a7e2c5e57dc640f6f5de5c6cc1942163e52017d60969d0d5f7432d1e16f",
    "scratch/verify_gate_c_fixed_order_three_rank_cayley_bank_20260822.py":
        "076cbd535fb9666a57509864b9106560846ca977f0e38b0674214efc816c47a7",
    "MATH_THEOREM_GATE_C_THREE_RANK_LINEAR_COSET_RESOLUTION_20260822.md":
        "49d29d5ea0fb86452b72a7b7be96533123764d2603a9c05d701b7d729f6b8e05",
    "scratch/verify_gate_c_three_rank_linear_coset_resolution_20260822.py":
        "f59a44913edba64690f416799a96227ff4d66345c8bb3359eb21ec090ac56e93",
}

WORDS = {
    1: (1, "4355a46b19d348dc2f57c046f8ef63d4538ebb936000f3c9ee954a27460dd865"),
    2: (2, "f251ddc12234e0da8d3b778bd0f7463fb477f16f47757f5617dc8b4ff4d4f14a"),
    3: (4, "aafa934d13be209cc39a9b5cb0b140af652fc0eebd127c42c6c982422964a790"),
    4: (7, "efe145ebc697686a2e3bf53a36362b5025835f2eb0ba16a1a0e64e2abd4ec1ca"),
    5: (12, "72195450d0361b37fbf58442203014eff475b3f59222c907fab99743106eee06"),
    6: (21, "7d30e058f98e6c09d65515e3f3971ae8bd7637f711670fa06a8a1dc536852d6d"),
    7: (37, "dda4b06c2e35bda3ea8a876a90807172adee166567d84b587ef5ae68cae9bec7"),
    8: (72, "df6d76b468bd816fd014d9b6f5259ba60e5f1ea06e4c4313901fe6155c8780eb"),
    9: (128, "c7e8cbfbe1a3531ffae4c9a01bd4b3b51dad0856b38486bacc56dbcaa73e3221"),
    10: (254, "24b6fc4f4c054e46ef54553ca37eded126150542d51a61256a837d666e0c74fd"),
    11: (465, "746b469af108558b14e7f6af0e3f76f9b6f39f70b3561e0258cc976650761850"),
    12: (926, "6d598c62f5925d1d2dfce8279eea82069318bd93ff66d0b204c639cf06297851"),
    13: (1719, "8d202e793d3317d2c3db76fef51f9d20d0e4e09fa2899a9686285cc01f4577d0"),
    14: (3434, "7d94117099bbb46402e8f4edda718dae7eb10e2e5e34e9b588e08a198b43db17"),
    15: (6438, "f35da2f0c98ec07de3e5318554157af490558e881be5c8bbcb5e3d1c8c08b14b"),
    16: (12873, "890ac346ce142f5f9ed564d487ff3e2fb99aea93ae2c104ec13765fa5d3814fe"),
}

REQUIRED = (
    "The historically decisive breakthrough for each closed dimension was:",
    "# Appendix A: Elementary asymptotics",
    "# Appendix B: The sole self-containment exception",
    "# Appendix C: Complete proofs for the direct punctured route",
    "# Appendix D: Self-contained abstract alternating-GK retirement",
    "# Appendix E: Near-perfect defect-one Dyck tail-seam matching",
    "## Appendix E.4: A balanced two-seam atom",
    "## Appendix E.5: Exact internal resolution into wreath rows",
    "## Appendix C.3bis: Independent high moments and exact cap trimming",
    "## Appendix C.3ter: Fixed slices and the stopped Palm reduction",
    "## Appendix C.3quater: Rooted conflict exposure and the microbite hierarchy",
    "## Appendix E.6: Exact FIFO recutting of a rainbow Johnson path",
    "## Appendix C.9: Exact all-depth occurrence-capacity threshold",
    "## Appendix C.10: Exact positive cover-down and cheap rounding",
    "## Appendix C.11: Shallow external regularity and the survivor-catalogue no-go",
    "## Appendix C.12: Signed current-scale collision forcing",
    "## Appendix C.12a: Post-purge centered-defect stability",
    "## Appendix C.13: Stopped external hits and relative protection",
    "## Appendix C.14: Palm collision, entropy, and late protection",
    "## Appendix C.15: Pair-potential and common-blocker drift",
    "## Appendix C.16: First-blocker-cell collision dichotomy",
    "## Appendix E.7: Multiplicity-weighted FIFO seam criterion",
    "# Appendix G. Conflict variance: the exact companion/pair-square reduction",
    "### G.1 A high-even-moment cap-only alternative",
    "### G.2 Rooted twelve-carrier Palm likelihood and the no-Freedman obstruction",
    "### G.3 Literal terminal density and the exact functional gate",
    "### G.4 Exact scalar Palm recursion and survival-selection covariance",
    "### G.5 Infinitesimal root hazard and the external-exposure deficit",
    "### G.6 Finite bites, degree regression, and the random-size reference",
    "### G.7 Avoidance extensions and fixed-ancestor curvature",
    "### G.8 One-step-lag absorption of degree rebinning",
    "### G.9 Carrier hazard evolves by conflict-boundary conductance",
    "### G.10 Fixed-jump normalization and the tail-local companion gate",
    "### G.11 The signed tail residual and its first punctured cluster",
    "### G.12 Punctured Palm hazard is not monotone in the root degree",
    "### G.13 A product Palm Simpson obstruction at carrier order twelve",
    "### G.14 The exact punctured connected-carrier correction",
    "### G.15 The connected-carrier Möbius and U-statistic hierarchy",
    "### G.16 Directional decomposition of the first two-star",
    "### G.17 Exact signed position-weight regression",
    "### G.18 The two-shore overlap-cell determinant",
    "### G.19 Factorial pair-Palm mass is off-root disjoint",
    "# Appendix H. Compensated Gate-B switching and its complete-catalogue Gram gate",
    "### H.4 Exposure-intersection histogram form and exact finite angles",
    "### H.4a Exact depth-two orbit scale at the shallow bottleneck",
    "### H.4b A uniform all-module orbit-factor witness",
    "### H.5 The second-order exposure signal and the Venn-coupling obstruction",
    "### H.6 The exact \\(W_2\\) Hahn--Venn scalar and an absolute remainder bound",
    "### H.7 A uniform cyclic-variance bound for the central factor",
    "### H.8 The all-module boundary-profile identity",
    "### H.9 A delocalized complete-\\(W_2\\) inverse and the exposure threshold",
    "### H.10 Full exposure is exactly zero avoidance on the boundary events",
    "### H.11 Sixteen local atoms for zero avoidance",
    "### H.12 The exact \\(j=2\\) local scale and the five-vertex bank",
    "### H.13 A finite difference certifies the full \\(j=3\\) local profile",
    "### H.14 Uniform all-depth local defect conditioning",
    "### H.15 A shore-difference current bound and the remote cone",
    "### H.16 The exact \\(j=2\\) six-vertex rooted-core determinant",
    "# Appendix I. FIFO and fragment quota compilers",
    "### I.5 The reopened logarithmic scale and exact open statement",
    "### I.6 Nearby-window representation and abstract flag balance",
    "### I.7 Independent columns do not serialize",
    "### I.8 Extended-track compiler and exact open gate",
    "### I.9 A multiscale variable-fragment compiler",
    "### I.10 The direct band-hole gate and a balanced two-junta obstruction",
    "### I.11 Arbitrarily slow cover-down and the phase-packet normal form",
    "### I.12 Integral phase-packet banks and the ordered-queue obstruction",
    "### I.13 The all-pairing coherent-tour orbit",
    "### I.14 The ordered Greene--Kleitman factor contains no coherent tour",
    "### I.15 A non-GK central factor with Hamilton projections and two near-tours",
    "### I.16 Exact intersections and the parity-defect bandwidth",
    "### I.17 A mesoscopic parity staircase and the uniform-orbit obstruction",
    "### I.18 Exact factor-adapted antipodal-swap tours",
    "### I.19 General antipodal prefix tests and the block-entropy threshold",
    "### I.20 Deletion-deck rigidity for antipodal block shuffles",
    "### I.21 Factorial local-deck entropy has a near-total common core",
    "### I.22 Equal-block shuffles force almost-everywhere two-sided ballot cuts",
    "### I.23 Exact gap-winding coordinates for the block-order count",
    "### I.24 The exact single-root ballot law and the factorial-moment gate",
    "### I.25 The exact multiroot grid and two-root four-letter bridge",
    "### I.26 Pivot flips give every factorial moment",
    "### I.27 Direct pivot miss-set tail",
    "### I.28 Unequal odd blocks and weighted excursions",
    "### I.29 One giant block has a subexponential common atlas",
    "### I.30 The universal fixed-pairing atlas cap",
    "### I.31 Pairing incidence and near-optimal menus",
    "### I.32 A fixed-order three-rank Cayley bank",
    "### I.33 Exact linear-coset resolution into three-rank banks",
    "Gate A: quenched maximum-degree-cap preservation",
    "Gate B: physical all-depth coinstantiation",
    "Gate C: coherent atom/product serialization",
    "The objective `nu(k)=(1+o(1))W(k)` is **not yet proved**.",
)

FORBIDDEN = (
    "**[A]**",
    "**[F]**",
    "exact central MSW Catalan factor",
    "Star-forest reverse peeling",
    "finite simultaneous routing exists through",
    "tail-seam graph has near-perfect numerical matchings",
)


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for block in iter(lambda: fh.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def verify_word(k: int, expected_length: int, path: Path) -> None:
    masks = [int(x) for x in path.read_text().split()]
    assert len(masks) == expected_length, (k, len(masks), expected_length)
    assert all(0 < x < (1 << k) for x in masks), f"out-of-range mask k={k}"
    ending: set[int] = set()
    seen: set[int] = set()
    for x in masks:
        ending = {x} | {y | x for y in ending}
        seen |= ending
    assert seen == set(range(1, 1 << k)), f"coverage failure k={k}"


def main() -> None:
    assert TARGET.is_file(), f"missing target: {TARGET}"
    raw = TARGET.read_bytes()
    text = raw.decode("utf-8")
    lines = text.count("\n") + 1
    size = len(raw)
    # The rigor-preserving 2026-08-22 refresh added Appendices G--I.  These
    # guards are deliberately only corruption/runaway-growth alarms; they
    # must not reject the audited expansion merely because it is rigorous.
    assert lines < 19_000, f"handoff unexpectedly large: {lines} lines"
    assert size < 750_000, f"handoff unexpectedly large: {size} bytes"
    display_open = re.findall(r"(?m)^[ \t]*\\\[[ \t]*$", text)
    display_close = re.findall(r"(?m)^[ \t]*\\\][ \t]*$", text)
    assert len(display_open) == len(display_close), "unbalanced display math"
    inline_open = re.findall(r"(?<!\\)\\\(", text)
    inline_close = re.findall(r"(?<!\\)\\\)", text)
    assert len(inline_open) == len(inline_close), "unbalanced inline math"
    assert text.count("~~~") % 2 == 0, "unbalanced fenced block"
    assert not re.search(r"[\x00-\x08\x0b-\x1f]", text), "control byte"
    assert not re.search(r"^\+#+\s", text, re.MULTILINE), "malformed diff-prefixed heading"
    tags = re.findall(r"\\tag\{([^}]+)\}", text)
    assert len(tags) == len(set(tags)), "duplicate equation tag"

    for phrase in REQUIRED:
        assert phrase in text, f"missing required phrase: {phrase}"
    for phrase in FORBIDDEN:
        assert phrase not in text, f"forbidden external/dead claim: {phrase}"

    for rel, expected in SOURCES.items():
        path = ROOT / rel
        assert path.is_file(), f"missing provenance source: {rel}"
        assert sha256(path) == expected, f"source hash mismatch: {rel}"
        assert expected in text, f"provenance hash omitted: {rel}"

    for k, (length, expected) in WORDS.items():
        path = ROOT / f"answers/k{k:02d}.word"
        assert sha256(path) == expected, f"word hash mismatch k={k}"
        assert expected in text, f"word hash omitted k={k}"
        verify_word(k, length, path)
        assert f"| {k} | {length} |" in text, f"breakthrough row missing k={k}"

    print(
        "MASTER_HANDOFF_SELF_CONTAINED_AUDIT_PASS",
        f"lines={lines}",
        f"bytes={size}",
        f"sha256={hashlib.sha256(raw).hexdigest()}",
        f"sources={len(SOURCES)}",
        f"words={len(WORDS)}",
    )


if __name__ == "__main__":
    main()
