# Reachable compound seam collars and bounded-task greedy/Haxell induction

Date: 2026-07-31  
Lane: R, bounded-defect Pascal physicalization  
Status: exact seam grouping and exact conditional regenerative theorem.
The required bounded physical-seam lift is not presently known.  No
unconditional `B(k)+O(1)` theorem is claimed.

## 0. Outcome

The exact AD seam theorem supports a stronger sparse-state formulation than
one raw repair task per damaged depth/window.  If two cyclic physical
chronologies differ in `s` old seams and `s` new seams, their residence,
fixed-depth shadow, and bounded-span compiler differences admit a bookkeeping
partition into at most `s` paired **signed collar groups**.  At depth `ell`,
one group contains at most `ell` old and `ell` new boundary windows, and its
changed owner-window support lies in two collars of radius `ell`, one in each
chronology.  Turning such a group into one physical compound task requires a
certified old/new seam-event pairing and one packet which closes both signed
collars.  Without that certificate the unconditional partition has at most
`2s` one-sided collar groups.  Changed linear cuts, reroots, and endpoint
capping are separate boundary tasks.

Consequently, if a reachable Pascal lift satisfies

\[
                         s\le a\Phi+s_0,              \tag{0.1}
\]

then a state with bounded carried defect `Phi` exposes only boundedly many
compound tasks, provided the nonseam births are also bounded.  For a fixed
bound `H` on the total task count, quadratic lists and a **per previously
selected packet/per other list** exclusion bound `O(mD)` have an elementary
greedy transversal whenever

\[
                         \alpha m^2>(H-1)\beta mD.    \tag{0.2}
\]

Here `D` is the largest physical dependency span, normally
`Theta(d(k))=Theta(sqrt(m))`.  Thus (0.2) holds eventually for fixed `H`.
This bounded-task route does not require a global full-atlas load theorem.

The missing input is not (0.1) alone.  It is the joint literal statement

\[
 |{\cal T}|\le\lambda\Phi+r_0+q s,\qquad
 s\le a\Phi+s_0,                                      \tag{0.3}
\]

where `q=1` requires owned paired compound packets and `q=2` is the
unconditional one-sided ledger, together with an exhaustive child ledger.
The seam count is occurrence-labelled and phase-resolved, with multiplicity.
Existing dimension-uniform Pascal constructions either leave the physical
cut/seam set conditional or use Catalan-many macro gaps.  Only the finite
`k=16` reroot ledger among the cited protected-state entries explicitly
records an AD changed-seam count; no current all-parameter theorem
propagates it.

## 1. The exact seam theorem

Let `T,T'` be cyclic Hamilton chronologies on the same `N` labelled owner
occurrences.  If `s=0`, the cyclic chronologies coincide and there is no
cyclic seam ledger.  Henceforth assume `s>0`.  Put

\[
 D^-=E(T)\setminus E(T'),\qquad
 D^+=E(T')\setminus E(T),\qquad |D^-|=|D^+|=s.       \tag{1.1}
\]

Deleting `D^-` decomposes the common graph into path fragments `P`.  For an
`ell`-edge owner window with `1<=ell<N` define

\[
                 b_\ell=\sum_P\min\{\ell,|V(P)|\}.   \tag{1.2}
\]

The AD theorem proves

\[
 |\mathcal B^-_\ell|=|\mathcal B^+_\ell|=b_\ell
                         \le \ell s,                 \tag{1.3}
\]

where \(\mathcal B^-_\ell,\mathcal B^+_\ell\) are the old and new windows not
wholly contained in one common fragment.  All reversal-invariant internal
window statistics transport bijectively, including across a reversed
fragment.  For linear paths the
same bound holds only when the cut and endpoint cap are fixed.  A changed
cut, reroot, prefix, suffix, or cap can alter endpoint windows even when
`s=0`; those corrections must be placed in the bounded exceptional bank.

For a compiler cell using `h` consecutive erosion letters at erosion depth
`d`, the owner dependency span is

\[
                            \ell=d+h-1.               \tag{1.4}
\]

Thus (1.3) applies simultaneously to fixed-depth shadows, residence collars,
and compiler signatures after taking a maximum declared span `D<N`, only
under the AD transported-skeleton hypotheses: controller, core, phase and
representative choices on a common fragment remain fixed.  Reoptimizing any
of them creates extra exposure.

## 2. Signed seam-ledger groups and the compound-task hypothesis

Fix arbitrary orderings

\[
             D^-=(e^-_1,\ldots,e^-_s),\qquad
             D^+=(e^+_1,\ldots,e^+_s).                \tag{2.1}
\]

For every old boundary window, choose the least-indexed old seam in its
span; for every new boundary window, choose the least-indexed new seam in
its span.  Define the signed ledger group `G_j` to contain:

1. every old boundary occurrence assigned to `e^-_j` and its signed
   deletion/protection requirement;
2. every new boundary occurrence assigned to `e^+_j` and its signed
   creation requirement;
3. the fixed-cut prefix/suffix run states at those two seams; and
4. every erosion/envelope/compiler row whose declared dependency window was
   assigned to either seam.

Empty `G_j` may be discarded.

### Theorem 2.1 (signed seam-ledger partition)

The complete changed-window ledger through span `D` is the disjoint union of
at most `s` signed groups `G_j`.  At a fixed span `ell`, each `G_j` contains
at most `ell` old and `ell` new based windows.  Its physical occurrence
support lies in the union of an old and a new radius-`ell` seam collar; over
all `ell<=D` it therefore uses at most `4D+O(1)` owner positions.

#### Proof

Every boundary window contains at least one changed seam, so the least-index
rule assigns it exactly once.  A fixed seam belongs to exactly `ell` cyclic
`ell`-edge windows; hence no task receives more than `ell` assigned windows
from either chronology.  Every such window starts at most `ell-1` edges
before its assigned seam and ends at most `ell-1` edges after it.  The union
of its owner positions is therefore contained in a radius-`ell` collar.
Taking the two chronologies and the largest span `D` gives the stated
physical bound.  Equation (1.3) proves that there are no other changed
windows.  QED.

The pairing in (2.1) is only bookkeeping: it need not pair physically local
edit events, compatible boundary types, or collars admitting any common
packet.  A **certified paired compound lift** additionally assigns each
`G_j` one nonempty packet menu whose members close its complete signed state,
including boundary, witness, topology, and cap tickets.  Without such a
certificate, use the `s` old and `s` new one-sided groups separately.  The
`4D+O(1)` bound concerns changed owner-window support only; a cap path,
compiler linkage, or topology ticket may be nonlocal and must be included in
the complete packet support/load hypothesis separately.

The number of labelled rows stored inside one group can be quadratic in `D`
when every depth is written separately.  The theorem reduces the number of
ledger groups, not by itself the number of selectable physical tasks.  A
candidate is eligible only if it closes the whole compound signature.

## 3. Reachable task count

Let `Phi` be an integer carried-defect count on an accepted regenerative
state.  Assume one Pascal lift has the following exact ledger.

* Every old defect has at most `lambda` declared child descendants.
* There are at most `r_0` fresh nonseam and changed-endpoint tasks.
* Its authenticated physical construction has a phase-resolved,
  occurrence-labelled seam-event count `s`, with multiplicity, satisfying
  (0.1).  Endpoint symmetric difference alone is not this count for a serial
  multi-phase construction.
* Every seam-induced row belongs to a certified paired compound task as
  defined after Theorem 2.1.
* The preceding three classes exhaust every fresh residence, shadow,
  compiler, witness, cap, and topology obligation in the child ledger.

### Corollary 3.1 (compound exposure bound)

The pre-repair child has at most

\[
 \widehat H(\Phi)
   \le \lambda\Phi+r_0+s
   \le (\lambda+a)\Phi+(r_0+s_0)                    \tag{3.1}
\]

compound tasks.

#### Proof

Charge inherited tasks to their parent defects, fresh nonseam/endpoint tasks
to the fixed birth bank, and all seam effects to the at most `s` certified
paired tasks.  The exhaustive-ledger hypothesis says that there is no fourth
class of fresh child birth, proving (3.1).  QED.

If only the unconditional one-sided ledger partition is available, replace
`s` by `2s` throughout (3.1), hence replace the coefficient `a` by `2a` and
the constant `s_0` by `2s_0`.  This changes no boundedness conclusion but
does not manufacture an exact whole-collar packet.

For passive two-coordinate upper-hole inheritance one may take
`lambda=4`.  This value does not control residence or compiler births; those
belong respectively to the `s` and `r_0` terms and must be proved bounded in
the same physical lift.

## 4. Greedy packet selection for a bounded reachable bank

Fix a state with at most `H` compound tasks.  For task `i`, let
\(\mathcal P_i\) be its guard-complete list of whole packets.  Assume constants
`alpha,beta>0` and a dependency span `D=D_m` such that:

1. \(|\mathcal P_i|\ge\alpha m^2\) for every task;
2. for every \(i\ne j\) and every packet \(p\in\mathcal P_i\), at most
   \(\beta mD\) packets of \(\mathcal P_j\) are incompatible with \(p\); and
3. every pairwise-compatible transversal is globally composable: its
   source-fixed resources are private, its signed collar states direct-sum,
   and its complete witness, topology, and cap tickets are mutually legal.

The second condition is a per-pair menu exclusion theorem.  It must include
all physical, colour, witness, topology, and cap conflicts; the local C6
parameter count alone proves none of those global ticket rows.

### Lemma 4.0 (token-to-pair exclusion)

Suppose every incompatibility is witnessed by a shared token, every packet
uses at most `rD+r_tok` noncore tokens, and any one such token occurs in at
most `kappa m` candidates of any fixed other task list.  Then condition 2
holds with

\[
          K_{\rm pair}\le(rD+r_{\rm tok})\kappa m.      \tag{4.0}
\]

In particular one may take the uniform constant
`beta=kappa(r+r_tok)` when `D>=1`.

#### Proof

For a fixed packet and another task list, take the union of the candidate
sets using each token of the packet.  The union bound gives at most
`(rD+r_tok)kappa m` candidates.  Multiple shared tokens only reduce the union.
QED.

Source-fixed tokens must be private before this lemma is applied.  Complete
cap paths and replacement-witness anchors count as tokens only after their
per-other-list multiplicity has been proved; local physical multiplicity
does not imply that bound.

### Theorem 4.1 (bounded-bank greedy selector)

If

\[
                  \alpha m^2>(H-1)\beta mD,           \tag{4.1}
\]

there is a compatible transversal selecting one whole packet for every
task.

#### Proof

Order the tasks arbitrarily.  After packets have been selected for `j`
earlier tasks, their union forbids at most `j beta mD` candidates in the
next list.  This is strictly less than `alpha m^2` by (4.1), so a candidate
remains.  Induction selects the transversal, and hypothesis 3 turns it into
one legal simultaneous physical repair.  QED.

### Corollary 4.1a (Haxell form)

Let `Gamma` be the complete cross-list packet-conflict graph and put

\[
 \Delta=\max_{i,p\in\mathcal P_i}
   \sum_{j\ne i}|N_\Gamma(p)\cap\mathcal P_j|.        \tag{4.2}
\]

Haxell's independent-transversal theorem applies whenever

\[
                       \min_i|\mathcal P_i|\ge2\Delta. \tag{4.2a}
\]

Under assumption 2, the crude estimate is
`Delta<=(H-1)beta mD`.  Thus for a bounded bank the direct greedy row (4.1)
is sharper by a factor two.  Haxell is useful when a dispersed extensive
bank admits a direct global `Delta` bound much smaller than this sum.

If `D=o(m)` and `H` is absolute, (4.1) holds for all sufficiently large
`m`.  At compiler depth `d(k)=Theta(sqrt(m))` with bounded extra cell span,
`D=Theta(sqrt(m))`, so the list-to-exclusion ratio is `Theta(sqrt(m))`.

### Corollary 4.2 (star-covered unary guards)

Suppose the unary rejected `(b,c)` pairs in every task menu have at most
`g_0mD` edges, and one selected packet excludes at most `g_1mD` candidates
from any other task list.  Then a compatible transversal exists whenever

\[
              m^2-g_0mD>(H-1)g_1mD,                 \tag{4.3}
\]

equivalently whenever

\[
                         m>(g_0+(H-1)g_1)D.           \tag{4.4}
\]

#### Proof

Every list retains at least `m^2-g_0mD` candidates.  Apply the proof of
Theorem 4.1 with `beta=g_1` and this exact lower bound in place of
`alpha m^2`.  QED.

The exact bad-pair star-cover theorem supplies the unary premise when the
union of all guards has an `O(D)` cover in the two free C6 coordinates.  A
mere `O(mD)` count is enough for (4.3), but neither count follows from
bounded packet support.

This agrees with Corollary 4.1a: Haxell remains the appropriate selector for
an extensive dispersed task bank, while Theorem 4.1 is the sharper exact
finite-bank selector.

## 5. Conditional reachable induction

Fix constants `E,e_0,a,s_0,lambda,r_0,alpha,beta` and spans `D_m=o(m)`.
Assume a finite authenticated base with `Phi<=E` and, for every sufficiently large `m`
and every reachable accepted state with `Phi<=E`, a Pascal lift satisfying
Sections 2--4.  Assume further that the simultaneous repair leaves an
accepted child with

\[
                              \Phi'\le e_0,             \tag{5.1}
\]

and exports the same typed state needed at the next step.  Here an exact
collar reset is the guarded-contraction `q=1` case with zero deficiency and
zero leakage.  Every unclosed collar casualty, displaced witness, or deferred
cap/topology obligation must be charged literally to `Phi'`; it cannot be
discarded merely because the local owner windows were repaired.  Put

\[
 H_E=(\lambda+a)E+r_0+s_0.                            \tag{5.2}
\]

### Theorem 5.1 (compound-collar regenerative induction)

If `E>=e_0` and

\[
                   \alpha m^2\ge2(H_E-1)\beta mD_m    \tag{5.3}
\]

for every parameter above the finite base, then an infinite compatible
regenerative spine exists with `Phi<=E`.  If every accepted state has a
terminal physicalization of length `B(k)+c_0` whose total literal completion
cost is at most `c_1 Phi+c_2`, then

\[
                    \nu(k)\le B(k)+c_0+c_1E+c_2       \tag{5.4}
\]

along that spine and its certified parity children.

#### Proof

Suppose `Phi<=E`.  Corollary 3.1 bounds the task bank by `H_E`.
Equation (5.3) and Corollary 4.1a give a simultaneous legal repair, and (5.1)
returns to `Phi'<=e_0<=E`.  Induction gives the spine.  Apply the stated
terminal theorem at each dimension; its additive charge is bounded by the
right side of (5.4) and is paid once after recompilation, not accumulated
down the spine.  QED.

This theorem is a genuine `B(k)+O(1)` implication, but every hypothesis is
uniform and literal.  In particular, a bounded seam count without a
guard-complete per-pair exclusion theorem does not imply (5.3), and a
compatible packet transversal without regenerative export does not imply
the induction.

## 6. Audit of known Pascal physical lifts

No current fully guarded all-parameter Pascal theorem proves (0.3).

1. `MATH_THEOREM_AD_RSB_DEPTH2_EROSION_DELTA_REGENERATION_GUARDS_20260731.md`
   proves `b_ell<=ell s` after the final physical chronologies are fixed,
   but explicitly states that a transparent circuit or bounded common-core
   linkage need not have bounded physical seam count.
2. The dimension-uniform component-neutral braid has
   `b=Cat_r` macro paths and `b` cyclic gaps (or `b-1` linear gaps).  It
   supplies an exact lower-palette ledger, but not a comparison with only
   `O(Phi+1)` changed physical seams.  Treating every macro join as a fresh
   seam gives a Catalan-scale, not bounded, value.
3. The protected Shadow--Braid theorem is conditional on a supplied fixed
   sealed segmentation and supplies no uniform cut-count bound.  In its
   frozen direct `K17` calibration, one
   row needs at least `61` deleted factor edges for the upper-q1 repair and
   another needs at least `49` cuts before the staircase budget can pass.
   These are finite scoped lower bounds, not an asymptotic no-go, but they
   do not furnish absolute `s_0`.
4. The `k=13,14,15` protected-state entries record construction join counts,
   not AD symmetric-difference seam counts.  Only `k=16` explicitly records
   two changed reroot seams.  None proves a recurrent all-parameter bound.
5. A coherent ECO toggle is a genuine dimension-uniform local result: it has
   exact `s=6` with a common connector, `s<=6+c` if that connector changes,
   and a prepared connector cube has \(s=6|U\triangle V|\).  It does not supply
   an all-dimensional repaired ECO bank, a bound on atom count by `Phi`, or
   uniform residence/compiler/export acceptance.
6. There is a restricted positive owner-topology lift when the parent
   already supplies one perfect Pascal trace cycle
   \(C=(C_0,\ldots,C_{N-1})\).  With marked facet cycle
   \(G_i=z+(C_{i-1}\cap C_i)\), delete the two cycle edges
   \(C_{i-1}C_i\) and \(G_iG_{i+1}\), then add the legal containment seam
   \(C_{i-1}G_i\).  The result is one spanning child path: two cycles were
   opened into paths and the cross seam joins their exposed endpoints.
   This is an absolute two-cut/one-join owner statement, not an AD
   symmetric-difference seam ledger.  It supplies neither the extra
   residence unit, protected all-depth witnesses, nor compiler reset.

For an inherited spanning linear forest with `t` components, any Hamilton
path obtained by deleting `d` forest edges and adding `a` outside edges
satisfies

\[
                              a-d=t-1.                 \tag{6.1}
\]

Hence `a>=t-1`.  The component-neutral Pascal forest with
`t=Cat_r+c_U` has a Catalan-scale construction/birth seam bank relative to
its inherited interiors.  Declaring an already joined macro cycle to be the
baseline may make a later comparison have `s=1`, but only moves the
authentication of those births into the unproved baseline/reset theorem.

Thus the sparse reachable route has two coupled missing rows: a
**defect-Lipschitz physical lift** with a phase-resolved event count
`s_ev<=a Phi+s_0`, and an **owned whole-collar compression** which supplies
one exact packet menu for every charged event (or one-sided event) and an
exhaustive child ledger.  A positive theorem may compare the child to a
preinstalled macro chronology so that Catalan-many unchanged joins cancel;
it must nevertheless authenticate the remaining occurrence-labelled seam
events and all exported guards.  Counting endpoint symmetric difference,
abstract switch edges, linkage paths, or macro components is not a substitute
for `s_ev`.

## 7. Sharp remaining statement

The bounded-task route will prove `B(k)+O(1)` once one supplies, uniformly
on a reachable regenerative spine:

\[
 \boxed{
  |{\cal T}|\le\lambda\Phi+r_0+q s_{\rm ev},\quad
  s_{\rm ev}\le a\Phi+s_0,\quad
  |\mathcal P_i|\ge\alpha m^2,\quad
  \operatorname{excl}_{j}(p)\le\beta mD_m,\quad
  D_m=o(m),}
\]

together with an exhaustive child ledger, certified paired collars with
`q=1` (or the factor-two one-sided replacement `q=2`), global composition, and bounded
terminal/export state.  The AD seam theorem unconditionally partitions the
changed owner-window ledger; the physical whole-collar menu is an additional
hypothesis.  Theorem 4.1 then supplies the selector.  No present theorem
proves the combined physical-lift/owned-collar row uniformly in `m`.
