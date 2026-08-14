# Hostile audit of the Catalan `T0V` `q3` relay, `G2` seam, and phase gate

**Date:** 2026-08-14
**Audited source:**
`MATH_REDUCTION_CATALAN_T0V_Q3_C12_C8_RELAY_HAS_A_G2_SEAM_AND_THREE_STATE_GATE_20260814.md`
**Verdict:** **PASS**, with the source's explicit limits.  The 17-owner
packet is a literal base `q3` repair and an all-suffix typed-safe tensor
through `q2`; it is not an all-suffix `q3` repair.  The native-cycle
minimality is finite/menu-specific, and neither a resident reset collar
nor contracted thirteen-port descent is claimed.

## 1. Literal packet and base typed replay

I reconstructed the canonical semilength-six incidence factor and toggled
the four printed alternating supports.  Their owner sets have sizes
`4,3,6,4` and are pairwise disjoint.  Their combined support has

```text
17 owners, 16 colours, 34 incidences.
```

The apparent colour deficit of one is intentional: the frozen `C8+C6`
shares its audited relay colour.  The added `C12` and closing `C8` introduce
no further shared colour.  At every changed owner and colour the toggle
preserves degree two, and the result remains a path factor.

The old, frozen-mixed, relay, and final loads are exactly

```text
old W3       1       frozen-mixed W3       0
C12 W3       2       C12 H3                0
final W3     2       final H3               1.
```

The final complete typed-deck current profile is

```text
deck        positive values   negative values   support casualties
owner              0                 0                  0
upper q1           0                 0                  0
lower q2           0                 0                  0
lower q1           8                 9                  0
upper q2           6                 6                  0
upper q3          12                 8                  0.
```

The replay retains coefficients rather than booleanizing the deck, so the
source correctly warns that these are distinct-value counts.  In
particular the nonunit lower-`q1` and upper-`q3` coefficients are not lost.

## 2. Provider and finite-atlas scope

The canonical `W3=110111001111` deck has one base provider.  Its root,
owners, colours, and positions agree verbatim with the source.  The frozen
mixed packet deletes that occurrence.  Complete replays through suffix
semilength four give old/new load `1/0` for every `W3[V]` and place the
provider on root `110110011000V`; the source correctly labels this as a
finite trace rather than an all-width uniqueness theorem.

The independent cycle enumerators give:

```text
cycle    owner-disjoint tested    raw W3 creators    typed-q2-safe creators
C6                  804                   7                    0
C8                 2208                  31                    0
C10                1757                 235                    0
C12               11789                1578                    1
C14               86876               12103                    0.
```

The `C6` and `C8` atlases are complete.  The longer-cycle DFS starts from
every endpoint-replacement arc that can occur in a four-owner `W3` path,
deduplicates literal cycle supports, and then replays the complete factor.
A single new `W3` provider must contain at least one changed endpoint arc,
so the target-relevant restriction is complete for the stated
single-cycle question.

The sole typed-`q2`-safe `C12` creator is the printed relay and has exactly
one `q3` casualty, `H3`.  With that relay fixed, the complete
owner-disjoint helper searches find zero `C6` closers among 792 and one
`C8` closer among 2,165.  Its data match the printed circuit.

I checked the source's negative auxiliary wording carefully.  The
two-`C6`, `C8+C6`, and CP-SAT no-gos all require at least one member that
creates `W3` individually.  They do not exclude a jointly creating bank
with no individually creating member.  The source states exactly that
limitation and makes no absolute minimum-bank claim.

## 3. Boundary-current identity

Let `Delta3^0` be the final base current.  I independently compared the
literal full-factor current with the proposed decomposition at every
`m=6,...,10`.  In each run the remainder is identically zero on every
typed deck.  At `q3` the exact strata are:

* base body rows marked by the suffix owner `V`;
* five one-suffix-colour rows marked by the injective `c0(V)=g(V)`; and
* for `s>=2`, the two-row seam marked by
  `G2(V)=c0(V) union c1(V)`.

The fixed prefix weights separate these three strata.  The locality proof
in the source is sufficient for all suffixes: a three-colour window can
cross a fixed prefix/suffix boundary in zero, one, or two suffix colours,
and a window using three suffix colours is untouched.  Direct inspection
of the finite changed boundary darts gives exactly the five signs in
`S1` and the two signs in `S2`.

On every deck through `q2`, the same comparison gives only the base body
current and the already-audited first-colour seam.  The old base providers
tensor, and the frozen theorem's two uniform providers back its negative
seam row.  Therefore the source's all-suffix typed-support-safe `q<=2`
statement is justified independently of the later `q3` failure.

## 4. `G2` collision and literal casualties

The semilength-three quotient table is exact.  In particular

```text
G2=111101 has two suffix preimages and current -2, final load 6;
G2=111110 has two suffix preimages and current -2, final load 3;
G2=110111 has the singleton V=110100, current -1, final load 0.
```

The sole provider of the singleton prefixed target is root
`111100101000110100` at position eight.  At suffix semilength four the
complete replay gives exactly the two casualties printed in the source
and no casualty on a typed deck through `q2`.

The logical distinction in Section 4 is important and correct.
Noninjectivity of `G2` prevents the old injective-seam proof, but does not
itself imply a support hole: both repeated fibres survive.  The literal
old/new loads prove the actual failures.  Marking by `c0(V)` is sufficient
to separate physical repair resources because `g^{-1}=h'`; it does not by
itself create a `q3` provider.  The source does not conflate these claims.

## 5. Topology, colouring, and directed voltage

The fixed-complementary projected component counts on both rank shores are

```text
m              6      7       8       9        10
components   125    422    1416    4827     16698,
```

equal to `Cat_m-7 Cat_(m-6)` in every replay.  The source correctly leaves
no numerical extrapolation hidden here.  The base merged 104-cycle meets
exactly the eight printed old Dyck roots.  Concatenation of canonical
insertion/deletion orders with `V` copies the same endpoint splice to
`R_iV`; distinct suffixes have disjoint root sets.  This proves the stated
all-`m` histogram with one length-`8(2m+1)` cycle per suffix and all other
cycles native of length `2m+1`.

The displayed z-free owner triangle is literal: its edge colours occur in
the claimed old/new states.  A deterministic DSATUR certificate colours
the entire z-free union graph with three colours, while the triangle rules
out two.  Hence the local undirected chromatic number is exactly three.

That certificate does **not** imply a `p=3` cyclic clock.  Reconstructing
the physical complementary closures gives

```text
old  {13:132},            new  {13:124,104:1}.
```

A unit directed `Z3` potential on a component of length `L` would sum to
`L=0 mod 3`; it fails on both 13 and 104.  Whole-component reversal does
not change this condition.  More generally, if `b` directed edges use
increment `-1`, closure gives `L-2b=0 mod3`.  Therefore the separate-state
lower bounds are `264` non-unit edges in the complete old closure and `249`
in the complete new closure; the affected subsystem alone needs at least
`16` and `1`.  These arithmetic bounds match the source and show why a single
global reset is not a valid repair.

The source also gets the all-`m` residue scope right.  With native length
`L=2m+1` and merged length `8L`, the same congruence gives a positive
per-packet reset lower bound, hence `Omega(Cat_(m-6))` resets, when
`L` is nonzero modulo three.  It is silent when `L=0 mod3`; no all-residue
lower bound is inferred from the `m=6` histogram.

Thus the remaining residence gate is accurately formulated as a
suffix-local phase-reset/cut-open collar, not as an application of the
existing closed `p`-tag theorem.

## 6. Thirteen-port and implication boundary

Nothing in the relay replay proves descent of the native thirteen-port
theorem through the six-root contraction.  The source explicitly carries
forward the five hypotheses of the frozen `q<=2` theorem: physical signed
role, intact source block, common-history consistency, separated starts,
and quotient connectivity.  The `G2` mark and three-colour certificate do
not discharge any of them.

The scope distinction is also correct: the `C12+C8` addition changes the
local action from six roots to eight and loses the binary relative phase.
It therefore cannot inherit the six-root port statement verbatim.  Either
a later backup must suppress topology-neutrally to the old interface, or
an eight-root/reset-state port theorem must be proved.

The exact remaining package must therefore combine three independent
features:

1. positive current into the collapsed `G2` target;
2. `c0(V)`-injective physical resources; and
3. a literal reset collar satisfying residence and component suppression.

This is a reduction, not a hidden existence claim.

## 7. Reproducibility

All substantive enumeration, replay, colouring, component work, and
hashing were performed on H100.  The compact hostile replay is

```text
scratch/audit_msw_t0v_mixed_q3_relay_gate_compact_20260814.py
scratch/audit_msw_t0v_mixed_q3_relay_gate_compact_20260814.h100.out.
```

It independently asserts the literal packet loads, typed current profile,
body/`S1`/`S2` identity, finite singleton-provider trace, exact casualties,
component counts, z-free three-colouring, closure histograms, directed
voltage no-go, and reset lower bounds.  Separate exhaustive outputs bind
the finite native-cycle census and helper uniqueness.

The frozen H100 SHA-256 digests are:

| artifact | SHA-256 |
|---|---|
| reduction source | `add07801007e4dcb0b93aaa68f3280035ebd55cc5d2a106256efac634439c2e4` |
| compact hostile verifier | `bd5c2559d80d8775f62cb81324f9d6e05976bf1d005df7c6fdd4375261640a4a` |
| compact hostile output | `0448818d18a49eb1836b94db77db897e547af384e482bdea92daaf23fdbc29c1` |
| provider tracer | `ebb4f9105a293bebf55941a19704e3e421a10749b8f42a6953da117395a7c8ea` |
| provider output | `79c6782392066d8cf86094b3a75d67adba0a242864aa3ae48464141d259b3274` |
| `C6`/two-`C6` search | `230cfbc2677453a83463cd6cffecd28b1416b81c02cbe19c0375b03629e67a93` |
| two-`C6` output | `5222cae16b40c1a8e82f8f3529444c25b7cb0a8697aad88c2426b1d2e3b5a49b` |
| `C8`/`C8+C6` search | `27d79c32953890a35f7262b7550b88ef554efc7759e3205b431c2c84bdb9d1ab` |
| `C8+C6` output | `6e436ce991920f213379e116b335ff210836d2f7c7434beabd13cb66da945ffa` |
| shared-colour `C6` bank solver | `b6faf184c164832b85003f1e9ad1283d72499b288a6d1a202427c2e2c8c1ef01` |
| shared-colour solver output | `ec3fd22a6432ed7d5e053bca84691ab4d569fb495808411c4695961cbf6d6294` |
| target-relevant long-cycle search | `58039fedd08fee692629ac3fadef3a452a561b397361fbca7a70d40f13519cb4` |
| `C10` output | `2b562e9e1759976ae452a65f30713c95112ddcf50aba6bf57b58c72eddfe6de3` |
| `C12` output | `45ed417d00c0f364f00d687e80681385299ae37d5bcadc2478e1e83b6d1a169c` |
| `C14` output | `bb105f0fa28d15fc716b97443493b630060299cfc5563d0e8091c6f60d889a21` |
| relay-closer search | `e781e2fdfd34eb6a3179dfe204ca967127ed17017ea34c88fbfee721e1387187` |
| relay-closer output | `e304433cc1e69c6b0297ba64d65e835e497a2e683d857fbc29517bcdb1bd9764` |
| full tensor replay library | `8f1f090294b6710b9aedeaec810df067d4c6cba6c49b56dc86903e1ec8e2ec01` |

The audit file's own digest is reported externally to avoid a
self-referential hash.
