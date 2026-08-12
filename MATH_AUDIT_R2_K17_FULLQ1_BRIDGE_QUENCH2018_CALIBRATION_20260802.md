# R2 audit: full-q1 neutral bridge and strict ordered quench to residence 2018

**Date:** 2026-08-02  
**Mode:** read-only remote hash/report/catalogue inspection.  No search or
solver was launched by this audit.

## Result inspected

Starting from the `fullq1_strict17` factor of literal opened residence 2025,
the promoted seed-2 lane applies:

1. one connected q1-neutral C6 bridge, row `2508`; then
2. the ordered three-C8 continuation `2446,12688,2243`, generated at the
   bridged state.

The terminal literal replay reports

```text
orientation 0: (1277,741), residence 2018, holes r10..13=(0,1518,278,4)
orientation 1: (1276,742), residence 2018, holes r10..13=(0,1518,278,4)
connected augmented lollipop: PASS
opened q1 holes in both frames: [0,0]
```

The auxiliary ordinary-component score is 2016 and is not substituted for
the opened score.

## Literal selected rows

```text
bridge C6 row 2508
  roots 15672,15768,16152
  old   25943,26169,26860
  new   26167,26862,25944

quench C8 row 2446
  roots 15129,16152,15130,47896
  old   24702,26858,24713,87553
  new   26857,24711,87554,24704

quench C8 row 12688
  roots 104210,112386,104226,120578
  old   186038,199229,186075,210811
  new   199228,186074,210812,186039

quench C8 row 2243
  roots 13625,13626,15672,79160
  old   21223,25940,142666,21222
  new   21214,21228,25947,142660
```

The three quench root sets are pairwise disjoint.  The full packet repeats
bridge roots 16152 and 15672.  Catalogue rows 12688 and 2243 have
`connected=0` when applied singly to the immediate post-bridge state; their
individual base-state opened score is therefore deliberately not used.  In
the promoted order `2446 -> 12688 -> 2243`, an independent complete replay
checks guards, positive ordinary q1 load, both opened q1 frames, the protected
boundary and connectivity at every prefix.  The packet therefore satisfies
strict-prefix semantics, not merely terminal-batch semantics.

There are 15 distinct removed and 15 distinct inserted incidences on 13
distinct roots.  Each circuit is degree-balanced, so the aggregate signed
root and owner currents are zero even at the two repeated roots.

## Hash manifest

The factor/search artifacts are below

```text
/home/amodo/or15/work/root_k17_q1zero_residence_oracle_20260802/
```

```text
748bc5cfe639028fd6642f044249740f333e5849556c9684af551e4f7356ef64  escape_s2_bridge.best.model
77cbcd9cff041446208984d0b6a8b5e6b6e9c281f62ed81cfc2e4b1bc152e28e  escape_s2_bridge.audit.json
50f2375697cc07e66b9cae4277b4b446e8396b863e388336f30e3c7d5935d63b  escape_s2_bridge.catalogue.tsv
c8f961413aeea43cbad5036e801c08f854f84889eaef11c281aa83bea46c057d  escape_s2_quench.best.model
956f147f3ec77b118cfd99e699fdb73f2d3d49604fb7966cd81e2deb40e89ab2  escape_s2_quench.extended.model
8976bfd4854338672de88dfe0036cdddf46c46095c164d836056e1be1890d280  escape_s2_quench.audit.json
ea24de7b229b572ad2f25a3a03f96230b29266daf56c2daf5ce92435b2f331ec  escape_s2_quench.passive.audit.json
53267516d1af6fa7f029af3e8aa4153035b06edb076a8e795a928c77a2b1ad92  escape_s2_quench.catalogue.tsv
```

The independent strict-prefix replay is below

```text
/home/amodo/or15/work/audit_k17_fullq1_floor_compounds_20260802/
```

```text
4d0cac9a426125da2cbb5a3134b9b4b64f64cccbdd01f4907e7829c2575d3063  promoted_chain.audit.json
46e0ddaa3ccca27bc853d8ab27d9094614f900c81cf071cd09c0953978d8a22e  audit_k17_strict_promoted_compounds_20260802.cpp
8ae21b56cec03e04386b3c2f8aad441ec1421e5c9f3387d3da744a4aaf9d2488  promoted_moves.tsv
```

The local terminal checkpoint and exact pair-cross-term companion are

```text
885f62c5b7689ada00970688a9771a5bcaa543657e3fae3d065aed3d1f41cb9d  checkpoint_fullq1_escape_res2018__independent.audit.json
5f4b8bd99fc1e173513eba52c16013f8c3d4b0d159acc04b492c8ee75aaf1cdc  MATH_AUDIT_R2_K17_FULLQ1_NEUTRAL_BRIDGE_PAIR_CROSS_TERM_AND_REGENERATION_20260802.md
```

## Scope

This audit authenticates byte hashes and cross-checks the selected catalogue
rows and promoted reports.  The separate promoted-chain audit independently
reconstructs the complete current-state catalogues and replays every displayed
prefix.  This note does not prove minimal support or establish a regenerative
theorem.  Its exact finite claim is the displayed strict ordered packet.
