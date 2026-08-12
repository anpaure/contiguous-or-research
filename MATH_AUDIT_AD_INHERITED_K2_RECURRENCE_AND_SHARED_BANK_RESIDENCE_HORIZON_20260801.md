# Audit of the inherited `K2` recurrence and its sharp shared-bank residence horizon

Date: 2026-08-01  
Lane: AD, same-parity split-core recurrence  
Status: exact local algebra verified; indefinite signed-residence closure
refuted and replaced by a sharp lifetime theorem.

## 1. Scope and verdict

This note audits the inherited-site transition in

- `MATH_THEOREM_AD_SPLIT_CORE_ONE_SIDED_PASCAL_STATE_RECURRENCE_20260801.md`,
  and
- Section 6 of
  `MATH_THEOREM_A_K2_PIVOT_ONE_ENDED_PREFIX_EXTENSION_AND_RELATIVE_EROSION_20260801.md`.

For a repaired depth-`h` split packet with menu pair

\[
                         1\le j<h,\qquad2\le s\le h,
\]

the following statements are exact.

1. A plateau retains `(j,s)`.
2. A deadline jump retains the same logical enriched labels at child
   indices `(j+1,s)`.
3. All four source blocks satisfy literal prefix/suffix identities; hence
   the owner row, pre-row, both native `q1` palettes, and all pivot rays have
   their asserted Pascal values.
4. The fresh jump coordinates each have two singleton source occurrences.
5. The terminal socket sends `(O,a)` to `(O+beta,a+beta)` on a plateau and
   to `(O+alpha,O)` on a jump.

Thus no packet algebra, Pascal-sector tag, native-`q1` equation, or local
owner envelope forces a fresh repair-site reset.  A mixed compiler cap can
still reject inherited physical addresses, and alternate hosts for a barred
base pair remain exterior hypotheses.

The stronger assertion that the shared-bank packet remains signed-resident
through arbitrarily many deadline jumps is false.

## 2. Literal inherited block identities

At a jump put `H=h+1` and

\[
 \Lambda'=(\alpha,\Lambda),\quad P'=(P,\gamma),\quad
 D'^-=(\gamma,D^-),\quad D'^+=(D^+,\alpha).
\]

For the inherited menu pair `(j+1,s)`, direct substitution gives

\[
\begin{aligned}
 E_H^-&=(\gamma)E_h^-,&
 A_H^-(j+1)&=(\alpha)A_h^-(j),\\
 A_H^+(s)&=A_h^+(s)(\gamma),&
 E_H^+&=E_h^+(\alpha).
\end{aligned}                                           \tag{2.1}
\]

In particular, no inherited enriched full-core source value is withdrawn.
The menu inequalities are invariant:

\[
 j<h\Longrightarrow j+1<H,qquad2\le s\le h<H.       \tag{2.2}
\]

The fresh `alpha` occurs as the first letter of `A_H^-` and the last letter
of `E_H^+`; the fresh `gamma` occurs as the first letter of `E_H^-` and the
last letter of `A_H^+`.  These are four physical singleton occurrences.
If the active repair labels themselves were born at an earlier jump, their
opposite-bank singleton backups also persist.  No such internal backup is
created for an arbitrary barred base label.

The identities (2.1) prove owner/native-palette persistence.  They do not
by themselves prove signed residence or transport arbitrary mixed compiler
rows.

## 3. Sharp residence obstruction

### Theorem 3.1

Start from a pairwise-disjoint packet at depth `h_0`.  After `t` deadline
jumps let `h=h_0+t`.  For every `i` with `1<=i<=t`, the coordinate
`alpha_i` occurs once in `Lambda` and once in `D^+`; `gamma_i` occurs once
in `D^-` and once in `P`.  The two source occurrences of either coordinate
have separation

\[
                         \Delta_i=3h_0+t+2i.           \tag{3.1}
\]

Their positive owner-support intervals have length `h+1`, so the internal
zero-gap between them has length

\[
                         g_i=2h_0+2i-1.                \tag{3.2}
\]

The coordinate satisfies signed depth-`h` residence if and only if

\[
                t\le h_0+2i-2.                        \tag{3.3}
\]

Consequently all shared jump labels are resident if and only if
`t<=h_0`.  At jump `h_0+1`, precisely the oldest pair is already defective,
with gap `2h_0+1<h+1=2h_0+2`.

The complete local owner traces are

\[
 \operatorname{tr}(\alpha_i)
 =0^{t-i}1^{h+1}0^{g_i}1^{t-i+1},\qquad
 \operatorname{tr}(\gamma_i)
 =1^{t-i+1}0^{g_i}1^{h+1}0^{t-i}.                    \tag{3.4}
\]

#### Proof

At time `t`, `alpha_i` has index `t-i+1` in `Lambda` and index
`h_0-1+i` in `D^+`.  Reading absolute positions in the four-block source
gives (3.1).  The indices of `gamma_i` are `t-i+1` in `D^-` and `h_0+i`
in `P`, giving the same separation.  One occurrence belongs to exactly
`h+1` consecutive depth-`h` owner windows.  The number of owner windows
strictly between the two support intervals is therefore

\[
 \Delta_i-(h+1)=3h_0+t+2i-(h_0+t)-1=2h_0+2i-1.
\]

This zero-run is internal.  Requiring it to have length at least `h+1`
gives (3.3).  The strongest inequality is `i=1`.  Plateaux alter neither
the two positions nor the membership trace.  \(\square\)

For the smallest example, take `h_0=2`.  After three jumps the current
depth is `5`, and the complete packet traces are

\[
 \operatorname{tr}(\alpha_1)=0^2 1^6 0^5 1^3,
 \qquad
 \operatorname{tr}(\gamma_1)=1^3 0^5 1^6 0^2.
\]

The central `0^5` is internal and residence requires `6`.  This is a local
packet trace, but it remains an obstruction in every full chronology which
keeps the packet contiguous: exterior prefixes and suffixes can alter only
the clipped first/last runs.  A noncontiguous global rethread can evade it,
but then it is no longer the inherited packet construction being audited.

## 4. Consequences for the recurrence

The inherited index rule is the proof-safe **algebraic** default.  It also
preserves all local signed runs through the finite horizon `t<=h_0`.
However, it is not an unbounded residence recurrence.

A fresh choice `(1,H)` for the two enrichment sites does not change the two
source occurrences in (3.1), so it does not repair Theorem 3.1.  Beyond the
horizon one needs at least one of:

1. a shared-bank rebase which removes or relocates one occurrence of every
   expiring coordinate;
2. a nonlocal rethread which lengthens each internal zero-gap; or
3. an explicitly nonflat compiler in which the affected residence row is
   discharged elsewhere.

There is an exact conditional cadence statement.  If a genuine literal
rebase at depth `b` restores pairwise-disjoint banks without changing the
exported interface, then exactly `b` further deadline jumps are safe and the
next jump is not.  The latest-reset schedule is therefore

\[
                          2b,4b,8b,\ldots.
\]

Only one integer countdown `c=b-t` (or oldest-birth slack
`2H_min-2-h`) is needed, so the **state-field** cost is constant.  No such
bounded-support literal rebase is proved.  In particular this does not give
constant source-length cost or a `B+O(1)` induction.

For a hypothetical rolling pair refresh, the first-generation pair `i`
expires at jump `t_i=b+2i-1`.  Hence service starts before jump `b+1` and
then one old pair reaches its deadline every two jumps.  This is an exact
necessary calendar, not a construction of a compatible bounded packet.

Within the horizon, and assuming the two displaced singleton targets have
post-transition-admissible, cell-distinct hosts, the remaining rows are the
exterior rows: upper-exact rooted owner-path completion, literal suffix and
terminal acceptance, and one background/common-cap occurrence ledger.
For an unbounded same-parity induction, shared-bank residence regeneration
is an additional essential gate.

## 5. Terminal socket

Let the last `h+2` source letters be `z_0,...,z_(h+1)` and put

\[
 O=\bigcup_{i=0}^{h}z_i,qquad
 a=\bigcup_{i=1}^{h+1}z_i,qquad a\subset O.
\]

Tagging every `z_i` by the plateau coordinate `beta` gives the two cells
`O+beta,a+beta`.  On a jump, prepending the singleton `{alpha}` gives
the two order-`h+1` cells `O+alpha,O`.  This is an exact two-cell
transducer.  It says nothing about the preceding windows crossing into this
terminal block; their cap and target transport remain exterior hypotheses.

## 6. Replay and precise scope

The dependency-free replay

```text
scratch/audit_ad_split_core_one_sided_pascal_state_20260801.py
```

checks all `(h-1)^2` repair pairs for `2<=h<=12`, both pre/post rows,
native palettes, plateau/jump block maps, physical fresh-singleton addresses,
an accumulated shared-bank plateau, integrated-rank terminal formulas, and
78 exact slack-ledger cases.  It also checks signed runs and the exact residence
horizon for every `2<=h_0<=12`.  The JSON status is

```text
PASS_WITH_SHARP_SHARED_BANK_RESIDENCE_HORIZON
```

with canonical payload SHA-256
`537b47a8da56535b0d4ae3574b611eaf836846a96cd6f311aef4880710ec6543`.

Frozen file SHA-256 values are:

```text
69a7f6f11df18ee3c011c972e394765433b99ec21061620375199bff9357e408  MATH_THEOREM_AD_SPLIT_CORE_ONE_SIDED_PASCAL_STATE_RECURRENCE_20260801.md
53a15b0acad3e5273587392aa33d242ff22048eb3328f8a10c2cad1d7fb1ca64  scratch/audit_ad_split_core_one_sided_pascal_state_20260801.py
b6d5cf1591d8974995d503c324f9c432a169310994d1e00419656e47bbcbb6f3  scratch/ad_split_core_one_sided_pascal_state_20260801.audit.json
```

The replay is a symbolic formula audit, not a proof of physical support,
the exterior Hamilton path, alternate exterior hosts, global caps, a
residence rebase, or common compiler existence.  Theorem 3.1 is symbolic
for every `h_0>=2`; the finite replay is independent corroboration.
