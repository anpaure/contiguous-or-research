# `k=17`: executable incidence-host opening layer, exact 3-trim oracle, and compact upper certificate

Date: 2026-08-01  
Lane: AD  
Status: exact implementation and independently replayed negative regression.  No
positive K-host chronology, `k=17` word, SAT claim, or UNSAT claim is made.

## 0. Verdict

K's compact unordered incidence-factor master now has a literal companion for
the complete strict-upper opening gate.

1. Rank ten remains eager.  The host already channels all `51,480` unordered
   facet-turn atoms and contains the `1,144` upper-colour-orbit ALO rows.  The
   companion forbids the eight quotient-loop turns, introduces one opening
   variable for each of the remaining `51,472` turns, chooses exactly one, and
   requires a second selected turn of the same rank-ten colour orbit.
2. A decoded primitive-voltage Hamilton factor is expanded into its exact
   `17*1430=24,310` physical owner cycle.  The oracle scans at most eight first
   future arrivals per owner start and tests all `1,430` normalized openings.
3. The opening test is the exact **source 3-trimmed** test.  On rank-nine owner
   intervals it is the ordinary edge-interior test; subtracting three again is
   an unsound double trim.
4. Ranks `11,...,16` are separated by exact phase-core clauses guarded by the
   complete selected incidence factor.  Rank seventeen is automatic.
5. A positive root is accompanied by at most `4,921` normalized witness rows
   for ranks `10,...,16`, or at most `2,633` after the eager rank-ten rows.
   A separate verifier replays every owner OR, phase mask, cut offset, and row
   bound.

The authenticated MMM unit-voltage chronology is a negative calibration.  It
is rejected at the eager gate by exactly `148` missing rank-ten quotient
colours, namely `2,516` physical colours.  It is not evidence against the K
master, whose first selected deletion-spine chronology is still unavailable.

## 1. Exact host companion

Let `x_e` be K's incidence variables.  At a facet, let

\[
                         z_{ef}=x_e x_f
\]

be the host's already-channelled unordered turn atom.  There are
`1430 binom(9,2)=51,480` such atoms.  Eight use distinct parallel incidences
between the same quotient owner and facet; a connected spanning factor cannot
use them, and the companion forbids them eagerly.

For each nonloop turn `t`, introduce `o_t`.  Let `c(t)` be its rank-ten target
orbit.  The added semantic rows are

\[
 o_t\Rightarrow z_t,
 \qquad
 o_t\Rightarrow\bigvee_{t'\ne t,\ c(t')=c(t)}z_{t'},              \tag{1.1}
\]

together with exactly one `o_t`.

### Theorem 1.1 (rank-ten exactness)

Assume the host's `1,144` rank-ten ALO rows.  The companion is satisfiable for
a fixed selected factor if and only if the factor has a selected nonloop turn
whose upper-colour orbit has multiplicity at least two.  Choosing that turn as
the opening preserves every physical rank-ten target, and every rank-ten-safe
opening has this property.

#### Proof

The first row of (1.1) makes the chosen opening an actual selected turn.  The
second supplies a distinct selected quotient occurrence of its colour orbit.
Every quotient occurrence lifts once in each of the seventeen phases, so after
deleting the normalized phase-zero occurrence, the distinct occurrence still
supplies all seventeen targets in that orbit.  All other colour orbits retain
all their selected occurrences.  Conversely, a rank-ten witness contains a
rank-ten-coloured Johnson edge; a uniquely supplied cut colour has no surviving
edge occurrence.  This proves both directions.  QED

A connected rank-ten-surjective factor necessarily has at least one such
turn, since `1,430` selected turns cover only `1,144` colour orbits.  Thus the
one-hot opening companion is an existential rooting of the unrooted factor,
not a requirement that every colour be duplicated.

There are `51,472` opening variables and `51,471` Sinz auxiliaries.  The exact
added clause count is

\[
 8+2(51,472)+(3(51,472)-3)=257,365.                              \tag{1.2}
\]

On the frozen K host used in the regression, the combined base has

```text
variables  115830 + 102943 = 218773
clauses    577148 + 257365 = 834513.
```

The current K host also contains eager native rank-seven rows; the upper layer
does not alter them.

## 2. Exact source trim and literal output offset

Write

\[
 T_i=A_i\cup A_{i+1}\cup A_{i+2}\cup A_{i+3}.                   \tag{2.1}
\]

An owner witness `[T_a,...,T_b]` comes from the source witness
`[A_a,...,A_(b+3)]`.  Its 3-trimmed source interior is exactly

\[
                 \{T_j\to T_{j+1}:a\le j<b\}.                   \tag{2.2}
\]

Therefore the implementation marks the ordinary owner-edge interval
`[a,b)`.  The preliminary implementation incorrectly used `[a,b-3)`; that
double trim was found adversarially and removed before any frozen output.

For the literal age-zero source letters `P_i`, one has

\[
 T_i=P_{i-3}\cup P_{i-2}\cup P_{i-1}\cup P_i,
 \qquad A_i=P_{i-3}.                                             \tag{2.3}
\]

Hence cutting owner dart `T_i->T_(i+1)` emits the source starting at
`P_(i-2)`.  A positive certificate records separately:

```text
root_position, physical_cut, emitted_P_start=(physical_cut-2) mod 24310.
```

This offset is not inferred from a generic untrimmed opening convention.

## 3. Helical expansion and exact phase cores

For quotient step voltages `v_i`, put

\[
 p_0=0,\qquad p_{i+1}=p_i+v_i,\qquad V=p_{1430}\pmod {17}.       \tag{3.1}
\]

After rejecting `V=0`, the physical owners are

\[
 T_{qN+i}=\rho^{qV+p_i}T_i,
 \qquad N=1430,\quad 0\le q<17.                                 \tag{3.2}
\]

For every physical owner start, the union can grow only on the first future
arrival of one of its eight missing coordinates.  Thus at most
`8W=194,480` first-growth events enumerate all undominated upper witnesses.

Fix a normalized target representative `U`, a quotient root turn `t`, and a
normalized witness `I`.  Let `P_t(I)` be the seventeen-bit mask of target
phases for which the ordinary owner interior of the rotated witness crosses
the normalized phase-zero physical cut.  Define

\[
                         L_t(U)=\bigcap_I P_t(I).                 \tag{3.3}
\]

Then root `t` preserves the entire physical orbit of `U` exactly when
`L_t(U)=empty`.

### Theorem 3.1 (guarded phase-core cut)

Let `S` be the `2N=2,860` incidence variables selected by an incumbent
connected factor, and let

\[
 G_U=\{t\text{ selected in }S:L_t(U)=\varnothing\}.
\]

The clause

\[
 \boxed{\left(\bigvee_{e\in S}\neg x_e\right)
        \vee\left(\bigvee_{t\in G_U}o_t\right)}                 \tag{3.4}
\]

is valid.  For the fixed factor `S`, the family (3.4) over all target orbits
of ranks `11,...,16` is equivalent to choosing one higher-safe root.

#### Proof

Keeping every variable in `S` fixes the entire labelled incidence cycle,
its two orientations up to reversal, all voltages, and every phase core.
Then (3.4) says precisely that the chosen one-hot root belongs to `G_U`.
Imposing this for every target orbit makes the root lie in the intersection
of all `G_U`, which is exactly the upper-safe-root condition.  If any selected
incidence changes, the guard satisfies the row, so no conclusion is projected
onto a different chronology.  QED

The oracle emits these rows only after eager rank ten passes.  If rank ten is
already incomplete, it emits the smaller whole-factor no-good.  The rows are
ordinary DIMACS clauses and may be accumulated in a proof-producing CEGAR
loop; a final UNSAT claim still requires the solver's DRAT/LRAT proof.

## 4. The `4,921`/`2,633` certificate

A rank-`s` witness contains at most `binom(s,9)` distinct owners.  Therefore
it crosses a fixed quotient edge orbit in at most

\[
 b_s=\left\lceil\frac{\binom{s}{9}-1}{1430}\right\rceil
      =(1,1,1,1,2,4,8)                                          \tag{4.1}
\]

phases for `s=10,...,16`.  Start with one witness.  For every phase in its
crossing mask, choose one additional witness omitting that phase.  At most
`b_s+1` rows then have empty mask intersection.  Since the target-orbit
counts are

```text
rank       10   11   12   13   14  15  16
orbits   1144  728  364  140   40   8   1,
```

the total is

\[
 2(1144+728+364+140)+3(40)+5(8)+9=4921.                         \tag{4.2}
\]

Removing rank ten leaves

\[
                  2(728+364+140)+3(40)+5(8)+9=2633.             \tag{4.3}
\]

The positive verifier checks all `2,425` target-orbit banks, literal owner
ORs, the recomputed phase masks, empty intersections, (4.2)--(4.3), the
rank-seventeen whole opened path, and the cut/`P` offset.  No positive
certificate is currently available, so this acceptance path is implemented
and statically audited but not claimed to have accepted an incumbent.

## 5. Executable package and regression

Frozen package:

```text
scratch/ad_k17_incidence_trim3_upper_20260801/
```

Core sources:

```text
build_ad_k17_incidence_trim3_upper_layer_20260801.cpp
  SHA e9debf667bd0d52878a16342808a8ef2ef6b230055b4979ef67ef9643eb80a04

audit_ad_k17_incidence_trim3_upper_opening_oracle_20260801.cpp
  SHA 33360fe78e64ed35886c9c0bda88987b6a75c05949289ab8d875653578ddbea9

verify_ad_k17_incidence_trim3_compact_certificate_20260801.cpp
  SHA f0893290aba7326c8efbda3806b320e39d2b3b5a487d7abb05b69a7f5eff4260

compose_ad_k17_incidence_trim3_cnf_20260801.cpp
  SHA 4891370da3f37f90adcc8410b7c5588c7190af9516e363d0d6bd2915125cd9cc

build_ad_k17_mmm_selected_incidence_regression_20260801.cpp
  SHA 17a8122e3fe1bbf8c48f39cdcfa02b8a40ed7f39af0d2d407057a60594f8dfa1

build_ad_k17_kcycle_trim3_selected_20260801.cpp
  SHA 3aa798e61cc1f6c20af9d6ae2fad5ef3797a948950fce4b73791ac113c99e080
```

The production layer/oracle/converter sources were compiled on H100 CPU with

```text
g++ -std=c++20 -O3 -DNDEBUG -Wall -Wextra -pedantic
```

The final bridge hardening was compiled both locally and on H100 with the
same warning flags.  Its lightweight fixture replay shows that malformed row
widths fail closed, shifts are range checked, and the declared voltage is
checked against the shift-derived voltage before any selected-cycle output
is accepted.

The production layer returned

```text
PASS openings=51472 maxvar=218773 clauses=257365
```

and exact composition returned

```text
PASS vars=218773 clauses=834513
```

The map-bound MMM regression returned

```text
CUT_EAGER_Q1_INCOMPLETE_SELECTED_CYCLE
voltage=1 q1holes=148 saferoots=0 best=7038 rows=0.
```

Its exact best-hole vector at ranks `10,...,16` is

\[
                     (2516,2720,1377,374,51,0,0).                \tag{5.1}
\]

The production bridge consumes the current proof-carrying K separator
columns (`orientation`, owner/facet representatives, selected incidence
variables and shifts), rebinds the selected unordered turn/opening variables,
and emits the oracle schema.  On an independently generated K-format MMM
fixture its output is byte-identical to the direct selected-cycle conversion:

```text
PASS orientation=0 rows=1430 voltage=1
cmp mmm.selected.tsv mmm.bridged.selected.tsv: identical.
declared-voltage mutation 1->2: rejected by recomputed shift voltage 1.
```

```text
scratch/ad_k17_incidence_trim3_upper_20260801/kcycle_bridge.audit.json
  SHA 419fd4e5612b140ee0110e7b10c5535dce5b66fd6e12887e429f54025aec32b4
  status PASS_K17_K_SEPARATOR_TO_TRIM3_ORACLE_BRIDGE_ROUNDTRIP.
```

The independently streamed audit additionally verifies:

```text
selected quotient turns       1430
selected incidence variables  2860
rank10 load histogram         0^148, 1^562, 2^434
lazy whole-factor literals    2860
phase-core rows               381280
by rank 11/12/13/14           229300/116107/31568/4305.
```

Independent audit:

```text
scratch/audit_ad_k17_incidence_trim3_regression_independent_20260801.py
  SHA 20b6b0d8d4538c14d01fdbb42896fa7806c53f3eff165a7c46c2595a9b31055f

scratch/ad_k17_incidence_trim3_regression_independent_20260801.audit.json
  SHA 7b0a55f6797e2c05b25b7f62a99f8e9cd37b3ceb93ad52c88e2f44e5267042da
  status PASS_INDEPENDENT_K17_INCIDENCE_TRIM3_MMM_REGRESSION_AND_KCYCLE_BRIDGE.
```

The positive verifier deliberately rejects the negative MMM certificate
because it has no accepted root.

## 6. Exact remaining boundary

The implementation closes the upper-layer semantics, not the K17 existence
problem.  Still required are:

1. a selected connected primitive-voltage incidence factor satisfying the
   deletion-spine and residual lower rows;
2. a positive upper-safe root from this oracle;
3. root/Sinz reassignment (or a chosen-root unit solve) if the oracle's safe
   root differs from the SAT incumbent's arbitrary opening assignment;
4. final literal source replay and the remaining compiler/common-cap checks.

The current status of that global search is **UNKNOWN**.  The old ordinary
untrimmed source-opening model is not used anywhere in this package.
