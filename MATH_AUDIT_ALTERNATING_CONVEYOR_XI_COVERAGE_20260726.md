# Alternating incidence conveyors: exact sparse-edit moment versus coverage

Date: 2026-07-26

Method: pure mathematics only.

## 0. Verdict

Put

\[
 B=C_s=\operatorname {Cat}_s,\qquad n=2s+1,\qquad W_s=nB.
\]

For a bank of root-disjoint, nondegenerate clean alternating
`C_(2 ell)` conveyors, the initial/final full ownership overlay has one
component of size `ell` for every conveyor.  If `M` roots are changed and
`N` conveyors are used, then the primary adjacent-edit moment satisfies

\[
 \boxed{
 \Xi={1\over B}\sum_{j=1}^N \ell_jD_j
       \ge {1\over B}\sum_{j=1}^N\ell_j^2
       \ge {M^2\over BN}.}
 \tag{0.1}
\]

Here `ell_j` is the root-orbit size, `D_j` is the sum of the rooted
adjacent-transposition distances in that component, and
`M=sum_j ell_j`.  For a uniform `ell`-bank this is exactly

\[
 \boxed{\Xi=\ell {M\over B}\,\bar d,\qquad \bar d\ge1.}
 \tag{0.2}
\]

The same identity holds for the complete physical profile edit moment:

\[
 \boxed{\Xi_H=\ell {M\over B}\,\bar e_H,}
 \tag{0.3}
\]

where `bar e_H` is the weighted mean half-`L^1` row-profile change.

Consequently the audited extensive native-row demand

\[
                         M\ge(\delta_{\rm inv}-o(1))B
\tag{0.4}
\]

is compatible with `Xi=o(sqrt(s))` for a hypothetical positive-density
bank of bounded clean `C_6` or `C_8` components having bounded row edit.
There is no row-count-only no-go for such a bank.

There is, however, a sharp obstruction for a sparse bank.  Positive-density
coverage together with `Xi=o(sqrt(s))` requires

\[
                         \boxed{N=\omega(B/\sqrt s).}
\tag{0.5}
\]

The ballot-forced theorem guarantees only a selected-edge-disjoint bank of
order `B/s`.  Using only a bank of that order to change a positive density
of roots forces `Xi=Omega(s)`.  Serially repeating its cycles does not add
new root components and cannot improve (0.1).

This does **not** refute the carrier extraction target `SACE_s`.  Its
certified carrier demand is only `Theta(B/s^(3/2))`; bounded cycles can
meet that numerical count with `Xi=o(sqrt(s))` while touching only `o(B)`
roots.  Likewise the Lane-G aligned-context demand is `Theta(B)` per
local context, not `Theta(W_s)`, and is not contradicted by (0.1).

A separate, stronger obstruction applies if one demands
`Omega(W_s)` actual weighted histogram movement from the same one-shot
pair.  In that case the sparse-edit condition itself is impossible.  This
is conditional on that stronger normalization and must not be called a
Lane-G or `SACE_s` no-go.

## 1. Conveyor model and the exact ownership component

Let `F,G` be exact anchored `D_s`-port factors.  A clean conveyor on a
root set

\[
                         R=\{P_0,\ldots,P_{\ell-1}\}
\tag{1.1}
\]

uses clean coherently oriented alternating `C_(2 ell)` switches at
successive phases.  Each switch cyclically transports the suffix strands
by

\[
                         \tau=(P_0\ P_1\ \cdots\ P_{\ell-1}).
\tag{1.2}
\]

If `k` stages are used, endpoint closure requires `ell | k`.  We assume
that the final object is genuinely exact and anchored.  This is an
important hypothesis: nonidentity fixed-exterior twisted slabs are ruled
out by the geodesic counteraudit.  Thus the statement applies only to an
actual internal or boundary-moving conveyor whose complete `X/Y` ledgers
and seams have been proved.

Call the conveyor nondegenerate when the interval between its first two
successive cut phases contains a state or colour token.  In that interval
the final row rooted at `P_i` owns a token which in `F` belonged to the row
rooted at `tau(P_i)` (up to reversing the chosen cyclic orientation).

### Lemma 1.1 (one component per root orbit)

For a nondegenerate conveyor, the full state-and-colour ownership overlay
of `F,G`, restricted to `R`, is one component and has side size `ell`.
Different root-disjoint conveyors lie in different components.

#### Proof

Every switch only reassembles segments belonging to the rows in `R`.
Thus every ownership edge incident with a root in `R` has both root labels
in `R`, so no overlay component can leave `R`.

The common port token at `P_i` joins the two shore vertices bearing root
`P_i`.  Nondegeneracy supplies, for every `i`, an ownership edge from the
old row at `tau(P_i)` to the new row at `P_i`.  After contracting the
common port edges, the owner graph therefore contains the cycle generated
by `tau`.  It is connected on `R`, proving that the full bipartite overlay
has one component.  Root-disjoint conveyors share no state or colour
token, so their components are disjoint.  \(\square\)

Further serial repetitions on the same transported root label do not
enlarge this component: they change the segment owner powers
`tau,tau^2,...`, but all of them remain inside the same `tau`-orbit.

There is a useful exact formal ledger.  If one alternating switch deletes
`p` selected incidence edges and its endpoint router has order `d` on `b`
root strands, one closed serial packet uses `d` copies and deletes `pd`
selected incidences.  After `a` complete laps the formal count is `apd`,
whereas the full ownership component still has size `b`.  For the standard
routers this gives

\[
\begin{array}{c|c|c|c|c}
\text{router}&b&p&d&pd\\ \hline
\text{clean }C_6&3&3&3&9\\
\text{folded }C_6\text{ transposition}&2&3&2&6\\
\text{clean four-strand }C_8&4&4&4&16\\
\text{clean }C_{2\ell}&\ell&\ell&\ell&\ell^2
\end{array}
\tag{1.3}
\]

For an endpoint-inert two-strand octahedral `C_8`, no serial closure is
needed; when both rows genuinely change its component size is two and the
formal selected-incidence count is four.  Table (1.3) is only a formal
switch ledger until the serial object is proved literal.  Moreover the
number `pd` is not automatically the final productive seam count: later
copies can cancel an earlier edge change.  Section 5 uses only the final
old-only seam count and is therefore immune to such cancellation.

## 2. Exact `Xi` identities and the optimal coverage inequality

For component `R_j`, put

\[
 \ell_j=|R_j|,\qquad
 D_j=\sum_{P\in R_j}d(P),
\tag{2.1}
\]

where `d(P)` is the rooted adjacent-transposition distance between the
complete cyclic rows of `F,G`, with the anchor fixed (or minimized over
the audited dihedral representatives).  The definition of the sparse-edit
moment gives the identity

\[
                         \Xi={1\over B}\sum_j\ell_jD_j.
\tag{2.2}
\]

Every root in a nondegenerate component changes its row.  Hence `d(P)>=1`,
so `D_j>=ell_j`.  This proves the first inequality in (0.1).  Cauchy's
inequality gives

\[
       \sum_{j=1}^N\ell_j^2\ge {(sum_j\ell_j)^2\over N}
                              ={M^2\over N},
\tag{2.3}
\]

and proves the last inequality in (0.1).

The inequality is best possible from component sizes and changed-root
count alone: equality in (2.3) holds for equal component sizes, and the
first inequality cannot be improved without excluding a one-adjacent-swap
change at every root.

For a uniform `ell`-bank, define

\[
 \bar d={1\over M}\sum_{P\ {m changed}}d(P).
\tag{2.4}
\]

Then (2.2) becomes (0.2).  In particular, if `M=alpha B`,

\[
                         \alpha\ell\le\Xi
                         =\alpha\ell\bar d.
\tag{2.5}
\]

Thus bounded `ell` and bounded mean edit are fully compatible with
positive-density coverage and `Xi=o(sqrt(s))`.

For the sharper physical edit moment, let

\[
 e_{q,P}={1\over2}\|z^G_{q,P}-z^F_{q,P}\|_1,
 \quad
 E_H(P)={1\over\Omega_H}\sum_{q\le H}w_qe_{q,P},
 \quad
 \Omega_H=\sum_{q\le H}w_q.
\tag{2.6}
\]

The definition of `Xi_H` and Lemma 1.1 give the exact identity

\[
 \Xi_H={\ell\over B}\sum_{P\ {m changed}}E_H(P)
       =\ell {M\over B}\bar e_H,
\tag{2.7}
\]

which is (0.3).  No lower bound `bar e_H>=1` is asserted: a changed cyclic
row can be invisible at a particular collection of interval lengths.

## 3. Serial phase span gives explicit upper bounds

Suppose a closed conveyor uses `k=a ell` distinct switch phases, and its
initial and final Johnson traces agree outside transition indices
`u,...,v`.  Put

\[
                         h=v-u+1.
\tag{3.1}
\]

Necessarily `h>=k`.  The two traces have the same states immediately
before and after this band.  Since the final path is a complement geodesic,
the coordinates deleted in the band are exactly the set difference of
these endpoint states, and the inserted coordinates are the reverse set
difference.  These two sets are therefore the same for `F` and `G`.

In the anchored coordinate word, only

\[
 (a_u,\ldots,a_v),\qquad(b_u,\ldots,b_v)
\tag{3.2}
\]

can change.  Each is a permutation of a fixed `h`-set.  Sorting the two
blocks independently gives

\[
                         \boxed{d(P)\le2\binom h2=h(h-1).}
\tag{3.3}
\]

At any proper cyclic interval length, a window set can change only when
one of its two boundary cuts lies strictly inside one of the two blocks.
There are `2(h-1)` such internal cuts and two possible window boundaries,
so

\[
                         \boxed{e_{q,P}\le4(h-1).}
\tag{3.4}
\]

Consequently, for a uniform bank covering `M=alpha B` roots,

\[
 \boxed{
 \Xi\le\alpha\ell h(h-1),\qquad
 \Xi_H\le4\alpha\ell(h-1).}
\tag{3.5}
\]

If one closed repetition is packed into `h=O(ell)` phases, these become

\[
                         \Xi=O(\alpha\ell^3),\qquad
                         \Xi_H=O(\alpha\ell^2).
\tag{3.6}
\]

Thus the displayed universal bounds certify the primary condition for
`ell=o(s^(1/6))`, and the sharper physical condition for
`ell=o(s^(1/4))`, under positive-density coverage.  These are sufficient
rates, not converses.  For `a` serial laps in a compact phase band, replace
`ell` in the span by `a ell`, giving respectively

\[
 O(\alpha a^2\ell^3),\qquad O(\alpha a\ell^2).
\tag{3.7}
\]

Serial repetition therefore preserves component size but generally
increases row edit; it is not free in `Xi`.

## 4. Sparse guaranteed banks cannot also give extensive row escape

Suppose the available root-disjoint conveyor bank has at most `N` members
and one asks it to meet the native extensive-distance demand (0.4).  Then
(0.1) gives

\[
 \Xi\ge {\delta_{\rm inv}^2B\over N}+o(B/N).
\tag{4.1}
\]

Hence `Xi=o(sqrt(s))` requires (0.5).

The ballot theorem guarantees a selected-edge-disjoint family of order

\[
                         M_s^{\rm cert}=\Theta(B/s).
\tag{4.2}
\]

Selected-edge disjointness is weaker than root-disjointness, so granting
root disjointness is already optimistic.  If one uses only a subbank of
`N=O(B/s)` independently switchable components and nevertheless demands
`M>=delta B`, then

\[
                         \boxed{\Xi\ge(\delta^2+o(1))s.}
\tag{4.3}
\]

This violates `Xi=o(sqrt(s))`.  Repeating the same conveyors serially does
not change `N` or `M`, so it cannot alter (4.3).

Equation (4.3) is a no-go for obtaining **both** extensive native-row
escape and sparse rounding from only the guaranteed `Theta(B/s)` bank.
It is not a no-go for an unproved `Theta(B)` bank of bounded cycles.

## 5. Productive seam and weighted-movement obstruction

There is a second, logically separate obstruction.  Let `T` be the number
of old-only undirected wreath edges in the final pair `F,G`, restricted to
the conveyor bank.  It is the final productive seam count, not the number
of switches performed along a history.

### Lemma 5.1 (productive seams cost adjacent edits)

For a uniform `ell`-bank,

\[
                         T\le4\sum_Pd(P),\qquad
                         \boxed{\Xi\ge{\ell T\over4B}.}
\tag{5.1}
\]

#### Proof

One adjacent transposition in a cyclic coordinate word changes exactly two
length-`s` interval vertices.  The start-index cycle is fixed, so every
undirected wreath edge whose two interval vertices are unchanged remains
unchanged.  At most the four old edges incident with the two changed
vertices can disappear.  A shortest adjacent-swap sequence and the
triangle inequality give `T<=4 sum_P d(P)`.  Substitute the exact uniform
identity `Xi=(ell/B)sum_Pd(P)`.  \(\square\)

If an actual depth-`q` histogram or one-Lipschitz overload objective moves
by `D_q`, the audited packet-locality theorem gives

\[
                         T\ge {D_q\over2q}.
\tag{5.2}
\]

Therefore

\[
                         \boxed{\Xi\ge{\ell D_q\over8qB}.}
\tag{5.3}
\]

In particular, if `D_q>=delta W_s` at `q=x sqrt(s)+O(1)`, then

\[
 \Xi\ge\left({\delta\ell\over4x}+o(1)\right)\sqrt s,
\tag{5.4}
\]

which is incompatible with `Xi=o(sqrt(s))`.  At fixed depth the lower
bound is `Omega(s)`.

The same conclusion follows directly from weighted row-profile movement.
Put

\[
                         \mathcal A_H
 =\sum_{q\le H}w_q\sum_Pe_{q,P}.
\tag{5.5}
\]

For a uniform bank, (2.7) is equivalently

\[
                         \boxed{
 \mathcal A_H={B\Omega_H\over\ell}\Xi_H.}
\tag{5.6}
\]

The adjacent-edit lemma gives also

\[
                         \mathcal A_H
 \le {2B\Omega_H\over\ell}\Xi.
\tag{5.7}
\]

For the standard fixed Gaussian window,

\[
 H=\lceil A\sqrt s\rceil,\qquad
 \Omega_H=\kappa_A\sqrt s+O_A(1),
\tag{5.8}
\]

with `kappa_A>0`.  Hence an actual weighted movement
`mathcal A_H>=delta W_s` forces

\[
 \Xi\ge\left({\delta\ell\over\kappa_A}+o_A(1)\right)\sqrt s,
 \qquad
 \Xi_H\ge\left({2\delta\ell\over\kappa_A}+o_A(1)\right)\sqrt s.
\tag{5.9}
\]

This is the precise one-shot bulk-action obstruction recorded in the
critical-pair synthesis: small `Xi` is a terminal rounding condition and
cannot itself supply `Omega(W_s)` counterbias.

## 6. The normalization boundary: Lane G and `SACE_s` survive

The hypotheses in (5.4) or (5.9) are stronger than the currently stated
local carrier demands.

### 6.1 Lane G

One aligned size-`s` context has `B=C_s` rooted rows.  The exact Lane-G
plateau demand per context is `Theta(B)`; after multiplying by the number
of aligned outer contexts it becomes `Theta(W_outer/s^(3/2))`.  It is not
`Theta(W_s)=Theta(sB)` inside one local factor.

Even a demand `gamma B` at every one of `Theta(sqrt(s))` weighted local
depths gives `mathcal A_H=Theta(B Omega_H)` and, through (5.6), only the
necessary scale

\[
                         \Xi_H=Theta(\ell).
\tag{6.1}
\]

For bounded `ell`, this is compatible with `o(sqrt(s))`.  Thus the seam
no-go (5.9) must not be applied to Lane G after replacing its local
`Theta(B)` demand by the larger `Theta(W_s)` normalization.

### 6.2 Ballot carrier extraction

The audited strand-admissible extraction target asks for useful carrier
mass

\[
                         D_s^{\rm car}=Theta(B/s^{3/2}).
\tag{6.2}
\]

Only `Theta(B/s^(3/2))` constant-gain certificates are numerically needed
from the raw `Theta(B/s)` certificate bank.  A bounded-`ell` root-disjoint
selection of this size, with bounded adjacent row edit, has

\[
                         \Xi
 =O\left({\ell^2\over s^{3/2}}\right)=o(\sqrt s).
\tag{6.3}
\]

Even the much coarser bound `d(P)=O(s)` gives

\[
                         \Xi=O(\ell^2/\sqrt s),
\tag{6.4}
\]

which still passes for bounded `ell`.  Such a selection touches only
`O(B/s^(3/2))` roots, however, and therefore does not meet the independent
native extensive-distance test (0.4).

Accordingly there are two distinct gates:

1. the `SACE_s` carrier amount is numerically compatible with sparse
   `Xi`;
2. using only the guaranteed `Theta(B/s)` components to obtain
   positive-density native row escape is impossible by (4.3).

Conflating these two normalizations would produce a false no-go.

## 7. Exact constructive redirect

The alternating-cycle lane remains viable only through one of the
following sharpenings.

1. Prove a bank of `omega(B/sqrt(s))` independent full-ownership
   components, with enough bounded clean/folded cycles to cover the
   required positive-density root set and with bounded mean row edit.
2. Prove that a sparse `SACE_s` bank need not itself escape the native
   basin because it is composed with a separate extensive growing
   counterseed, while retaining its signed `Theta(B/s^(3/2))` carrier
   gain.
3. Bypass the rowwise `Xi` estimate by proving direct signed cancellation
   of the full component effects.  Unsigned cycle count or formal serial
   monodromy is insufficient.

No existing theorem supplies any of these statements.  In particular,
fixed-exterior serial repetition is unavailable, selected-edge
disjointness is not full-overlay independence, and favourable carrier sign
is not implied by cycle orientation.

No coefficient-one conclusion is claimed.
