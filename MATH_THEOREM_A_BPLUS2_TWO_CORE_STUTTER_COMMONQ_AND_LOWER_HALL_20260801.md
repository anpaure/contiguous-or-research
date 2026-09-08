# The `B+2` two-core stutter: exact common-Q interval and residual lower Hall

Date: 2026-08-01  
Lane: A, rotated endpoint host / common-Q  
Status: exact local common-Q characterization, exact owner-cover ledger, and
exact residual lower-matching theorem.  The source placement, arbitrary-width
upper bank, topology and all-dimensional regeneration remain open.

## 0. Result

The standard `B+1` endpoint wrap is flat-impossible.  The proposed `B+2`
replacement uses

\[
 \begin{aligned}
 Q^-&=(f_{d-1},f_{d-2},\ldots,f_2,K_L,Z),\\
 P^+&=(T,K_R,f_{d-1},f_{d-2},\ldots,f_2).                \tag{0.1}
 \end{aligned}
\]

Its gained owner bank is exactly

\[
                     U,D_{d-1},D_{d-2},\ldots,D_2,U.      \tag{0.2}
\]

This owner calculation does not by itself give a common-Q word.  The exact
additional ray condition is

\[
                           K_L\subseteq A,\qquad K_R\subseteq B. \tag{0.3}
\]

Thus a forced common literal stutter `K_L=K_R=K` requires

\[
                              \varnothing\ne K\subseteq A\cap B, \tag{0.4}
\]

after intersecting with both full source caps and every mixed-row screen.
The weaker palette hypothesis `K subseteq A union B` is insufficient.

For fixed exterior letters this becomes one exact set interval

\[
                         K_{\min}\subseteq K\subseteq K_{\max}. \tag{0.5}
\]

It is nonempty precisely under the conditions of Theorem 2.2 below.  The
two singleton `K` rows must be pinned if equality of the two physical source
letters is part of the state; the unconstrained componentwise maximal word
normally enlarges the left and right letters differently.

The local lower bank has `2d+2` cells but matching rank only `2d-1`: the
left base `Z`, right base `T`, and common core `K` each occur twice.  Hence
the two stutters do not provide two independent lower credits.  After fixing
one representative of every ray target and one `K` cell, exact completion is
ordinary residual Hall in the final literal word.  Before the word is fixed,
the residual injection must be chosen first and included in the same
maximal-word test; abstract Hall alone is insufficient.

## 1. Owner-cover ledger

Let the active aperture be

\[
                         \Gamma=A\cup B,
\]

let `F={f_1,...,f_d}` be disjoint from `Gamma`, and put

\[
 U=\Gamma\cup F,qquad D_j=U-\{f_j\},qquad
 Z=A\cup\{f_1\},\qquad T=B\cup\{f_d\}.                  \tag{1.1}
\]

Assume the rank calibration

\[
                         |\Gamma|+d=m+1,                  \tag{1.1a}
\]

so `U` has rank `m+1` and every `D_j` has the middle rank `m`.

Assume only that the nonempty stutter letters in (0.1) are subsets of
`Gamma`.

### Lemma 1.1 (the stutters are owner-invisible)

The `d` length-`d+1` windows crossing `Q^-|P^+` have, in order, the values
(0.2), independently of `K_L,K_R`.

#### Proof

Every crossing window contains `Z` and `T`, whose union already contains
`Gamma`, `f_1` and `f_d`.  The first window contains all of `Q^-` and `T`,
so it is `U`.  After one shift, `f_(d-1)` has left and no new filler has
entered, giving `D_(d-1)`.  The unique missing filler walks through
`f_(d-2),...,f_2`, and the last window is again `U`.  Both stutters add only
coordinates already present through `Z union T`, so they do not alter the
list.  \(\square\)

The intersection of the crossing-owner targets through any one of the four
pivotal positions `Z,T,K_L,K_R` is

\[
 H_0=U\cap\bigcap_{j=2}^{d-1}D_j
       =\Gamma\cup\{f_1,f_d\}.                            \tag{1.2}
\]

Thus the crossing owner rows alone admit every core-only stutter.  Owner-cap
legality at the complete word level is stronger because the two stutter
positions also lie in exterior owner windows.

### Theorem 1.2 (sharp additive-two owner count)

Suppose the old row is owner-complete and its dropped middle-owner bank is

\[
                         D_d,D_{d-1},\ldots,D_1.           \tag{1.3}
\]

After replacing it by (0.2), middle-owner coverage is retained if and only
if `D_1` and `D_d` each had another retained occurrence outside (1.3).

Consequently at least two excess owner-window occurrences are necessary.
At additive slack two, the count is rigid: before the recut `D_1,D_d` each
have load two, every other middle owner has load one, and there is no old
nonmiddle window; after the recut every middle owner has load one and the two
surplus windows are the two copies of `U`.  At slack `c>2`, exactly `c-2`
further excess occurrences remain.

#### Proof

For `2<=j<=d-1`, one lost occurrence of `D_j` is replaced by one gained
occurrence.  The masks `D_1,D_d` are lost and not gained, so each needs a
retained duplicate.  Conversely those two duplicates, together with the
replaced internal coatoms, preserve every middle owner.  Two retained
duplicates consume two excess occurrences.  Equality at slack two forces
all other loads and nonmiddle counts to be minimal, giving the stated rigid
profiles.  \(\square\)

The copies of `U` have rank one above the middle layer.  Therefore (0.2) is
an owner-**cover** row with two nonowner break cells, not a flat Johnson
chronology in which every depth-`d` window is a middle owner.  Any topology
theorem must connect the middle-width genuine owner windows across those two
breaks separately.

## 2. Exact common-Q feasibility of the stutters

### Lemma 2.1 (ray transparency)

The complete left exclusive ray ending at `Z` is

\[
 Z,\quad Z\cup K_L,\quad
 A\cup K_L\cup\{f_1,f_2\},\ldots,
 A\cup K_L\cup\{f_1,\ldots,f_{d-1}\}.                    \tag{2.1}
\]

It is the canonical `A`-flag, with its base repeated once, if and only if
`K_L subseteq A`.  Dually, the right exclusive ray is the canonical
`B`-flag with its base repeated once if and only if `K_R subseteq B`.

#### Proof

The second left cell has value `Z union K_L`; equality with the required
base `Z` is equivalent to `K_L subseteq Z`.  Since `K_L subseteq Gamma` and
the fillers are disjoint from `Gamma`, this is `K_L subseteq A`.  Under that
condition every later equality in (2.1) follows.  The first equality is also
necessary, so the condition is exact.  The right side is identical.  \(\square\)

This proves (0.3)--(0.4).  For example, at `d=3`, take
`Gamma={a,b}`, `A={a}`, `B={b}`.  Every nonempty `K subseteq Gamma` gives the
correct owner palette `U,D_2,U`, but no common nonempty `K` preserves both
rays.  This is the first common-core obstruction with a nonempty internal-
coatom bank.  The same disjoint-core phenomenon already occurs at `d=2`,
where the gained owner bank is simply `U,U`.

Now freeze every source letter other than the two stutter positions.  For
each required row `R` meeting at least one stutter, let `B_R` be the OR of
all its fixed letters with both stutters omitted, and let `S_R` be its target.
At this stage the row family excludes the two variable singleton pins (2.5),
whose target `K` has not yet been chosen.  Let `Pi_L,Pi_R` be the full caps
at the two stutter positions, including all exterior owner and compiler
screens.

Define

\[
 \begin{aligned}
 K_{\min}&=\bigcup_R(S_R-B_R),\\
 K_{\max}&=A\cap B\cap\Pi_L\cap\Pi_R\cap\bigcap_R S_R.   \tag{2.2}
 \end{aligned}
\]

### Theorem 2.2 (same-core maximal-word interval)

There is a common nonempty literal source letter `K` at both stutter
positions, preserving the canonical rays and realizing every affected row,
if and only if

\[
 \boxed{
 B_R\subseteq S_R\quad(R),\qquad
 K_{\min}\subseteq K_{\max},\qquad K_{\max}\ne\varnothing.} \tag{2.3}
\]

When (2.3) holds, any nonempty `K` satisfying (0.5) works.  If
`K_min=emptyset`, choose any nonempty subset of `K_max`.  Conversely every
feasible common core lies in this interval.

#### Proof

An affected row has value `B_R union K`, whether it meets one or both copies
of the same letter.  Equality with `S_R` is equivalent to

\[
                B_R\subseteq S_R,qquad
                S_R-B_R\subseteq K\subseteq S_R.          \tag{2.4}
\]

Intersect the upper bounds over all rows and both caps, add the exact ray
upper bound `K subseteq A cap B`, and union the lower bounds.  This gives
(2.2)--(2.3).  Nonzeroness is the final displayed condition.  \(\square\)

To certify the equality of the two physical letters inside an ordinary
maximal-word system, first choose `K` from (0.5) and include singleton rows

\[
                         \{k_L\}\mapsto K,qquad
                         \{k_R\}\mapsto K.                \tag{2.5}
\]

They force both maximal letters to be exactly `K`.  Without (2.5), the
componentwise maximal word for the owner and ray rows generally enlarges
the left stutter toward `Z` and the right stutter toward `T`; existence of a
smaller common-core witness does not make equality of the two positions a
maximal-word invariant.

Owner rows alone have `K_min=emptyset` and impose only the local cap (1.2).
The nontrivial parts of (2.3) are therefore the ray intersection, the two
full exterior caps, and the protected mixed rows.

### Corollary 2.3 (asymmetric escape)

Equality of the two stutters is unnecessary for the owner palette and ray
flags.  With separate nonempty letters, the exact local conditions are only

\[
                         K_L\subseteq A,qquad K_R\subseteq B, \tag{2.6}
\]

plus their respective caps and all mixed-row reconstruction equations.
Equivalently, define the two componentwise maximal letters

\[
 \begin{aligned}
 K_L^*&=A\cap\Pi_L\cap\bigcap_{R:k_L\in R}S_R,\\
 K_R^*&=B\cap\Pi_R\cap\bigcap_{R:k_R\in R}S_R.           \tag{2.7}
 \end{aligned}
\]

The asymmetric word exists exactly when both are nonempty and

\[
 S_R=B_R\cup
      \bigl(K_L^*\text{ if }k_L\in R\bigr)\cup
      \bigl(K_R^*\text{ if }k_R\in R\bigr)               \tag{2.8}
\]

for every affected row.  Thus disjoint effective cores obstruct the
same-`K` design but not necessarily the same-length asymmetric design.

## 3. Exact lower matching ledger

Assume from now on the common-core face (0.4), and assume `K` and every left
and right flag value are strict-lower targets, mutually distinct as in the
coatom application.

### Lemma 3.1 (local rank is `2d-1`)

The full local lower bank consists of:

* `d` left-ray cells with `d-1` distinct target values, because `Z` repeats;
* `d` right-ray cells with `d-1` distinct target values, because `T` repeats;
* the two singleton stutter cells, both of value `K`.

Hence its `2d+2` physical cells have lower-matching rank exactly

\[
                                  2d-1.                    \tag{3.1}
\]

The `d` owner windows in (0.2) have strict-lower matching rank zero.

#### Proof

Lemma 2.1 gives the two ray lists and their single repetitions.  The two
singleton cells are parallel occurrences of one further target `K`.  The
assumed target distinctness makes the three contributions disjoint, proving
(3.1).  Every window in (0.2) has middle or upper-middle rank, so none is a
strict-lower target cell.  \(\square\)

Choose one cell for each of the `2d-2` ray targets and one singleton cell for
`K`.  Let `F_0` be this `2d-1`-edge partial matching and let `T_0` be its
targets.  For a convenient protected reserve, put

\[
 C_0=C(F_0)\cup\{\text{the second singleton }K\text{ cell}\}. \tag{3.1a}
\]

Thus `|C_0|=2d`; exactly one cell of `C_0` is deliberately unused, and the
extra `Z` and `T` ray cells were not reserved.

Let `mathcal L` be the full lower target bank, let `mathcal C` be all lower
cells in the final word, and let `G` be the literal realization graph.  Put

\[
 G_0=G[\mathcal L-T_0,\mathcal C-C_0].                    \tag{3.2}
\]

### Theorem 3.2 (residual lower condition)

A full lower matching extending `F_0` exists if and only if

\[
        |N_{G_0}(X)|\ge|X|\qquad(X\subseteq\mathcal L-T_0). \tag{3.3}
\]

For a fixed literal word with one demand per target mask, (3.3) reduces to

\[
   \operatorname{Occ}(S)\setminus C_0\ne\varnothing
                  \qquad(S\in\mathcal L-T_0),             \tag{3.4}
\]

because cells of different literal values cannot coincide.  With
occurrence-labelled multiplicity, replace (3.4) by the corresponding free
occurrence count; this characterizes extensions which respect the declared
reserve `C_0`.

#### Proof

Equation (3.3) is Hall's theorem on the residual graph.  For one demand per
target mask it is also equivalent to unrestricted extension of `F_0`, since
the deliberately unused reserved cell has value `K in T_0`.  In a fixed
literal word each cell has one value, so neighborhoods of distinct masks are
disjoint; Hall then reduces to their individual nonemptiness/counts.  With
multiple occurrence-labelled demands, delete only the cells used by `F_0`
if unrestricted extension rather than reserve-respecting extension is
intended.  \(\square\)

In particular, if a protected matching for `mathcal L-T_0` is already
literal in this same final word, it automatically avoids `C_0`: every cell
of `C_0` has value in `T_0`.  Adding `F_0` then causes zero further Hall
loss.  This is a coexistence statement in one final cap, not transport from
a different completed word.

Before the final word is fixed, abstract Hall is insufficient.  Propose a
common core `K` and a residual injection

\[
             \phi:\mathcal L-T_0\longrightarrow\mathcal C-C_0,
\]

add the two singleton-`K`
pins and all occurrence equalities to the owner/ray rows, and define

\[
 K_p(K,\phi)=\Pi_p\cap
   \bigcap_{R\in\mathcal R_{\rm base}(K):p\in R}S_R
   \cap\bigcap_{S:p\in\phi(S)}S.                         \tag{3.5}
\]

Here `mathcal R_base(K)` includes the two rows (2.5).

### Theorem 3.3 (pre-word common-Q order)

The `B+2` local bank and residual lower assignment are simultaneously
feasible if and only if there is a pair `(K,phi)`, where `phi` is injective,
such that:

1. after adding the rows selected by `phi`, their complete affected-row
   family has a nonempty augmented interval
   `K_min(phi) subseteq K subseteq K_max(phi)` as in (2.2)--(2.3) (or the
   asymmetric equations (2.7)--(2.8) hold);
2. the two chosen singleton rows `k_L mapsto K,k_R mapsto K` are inserted,
   and every resulting `K_p(K,phi)` is nonempty; and
3. every owner, ray, protected and assigned residual row is reconstructed by
   the union of its `K_p(K,phi)` letters and frozen exterior.

Under a private/composable residual option atlas relative to the already
fixed owner/ray/`K` baseline, condition 3 factors.  If the free slot
neighborhoods (computed after deleting `C_0`) are intervals in one order,
the existence of `phi` is then
equivalent to

\[
 \#\{S:N(S)\subseteq[i,j]\}\le j-i+1                    \tag{3.6}
\]

for every slot interval `[i,j]`; for laminar neighborhoods it suffices to
check the distinct neighborhood cuts.

#### Proof

For fixed `(K,phi)`, conditions 1--3 are exactly the componentwise
maximal-word criterion applied to the complete row family.  Quantifying over
both objects is therefore necessary and sufficient.  On the
private/composable face, if every residual option is source-disjoint from the
stutters (or has a common stutter boundary signature), the interval is
selection-invariant and ordinary Hall remains; interval Hall reduces to
(3.6), and laminar Hall to its neighborhood cuts.  \(\square\)

The fixed-exterior hypothesis of Section 2 is load-bearing in the displayed
`K_min(phi)` formula.  If other letters of an affected row are also live,
one must quantify over `(K,phi)` and apply the full maximal-word equations
directly; a frozen `B_R` must not be inferred from their caps.

For comparison with a pre-stutter reference word, let `g_L,g_R` be the two
insertion gaps.  The canonical lift of an old interval `I` has length

\[
       |I|+\mathbf1_{g_L\in\operatorname{int}(I)}
            +\mathbf1_{g_R\in\operatorname{int}(I)}.       \tag{3.7}
\]

Because `K_L subseteq Z` and `K_R subseteq T`, including the inserted
letters on a crossed gap preserves the old OR.  Such an occurrence remains
in a depth-`d` lower bank exactly when (3.7) is at most `d`.  Every selected
old occurrence failing this inequality is unusable; its target belongs in
the residual Hall problem only if no alternate retained occurrence is
chosen.  The indicators in (3.7) are gap-crossing indicators, not merely
tests that `I` contains `Z` or `T`.

## 4. Scope and smallest remaining theorem

The following points are now exact.

1. The owner palette (0.2) and additive-two count close only at the level of
   owner coverage; the two copies of `U` are nonowner breaks.
2. Palette legality `K subseteq Gamma` does not imply compiler legality.
   Same-core common-Q is exactly (2.3); asymmetric common-Q is exactly
   (2.7)--(2.8).
3. The local lower bank has rank `2d-1`, not `2d` or `2d+2`; the stutters
   buy no two-unit lower matching surplus.
4. Residual lower completion is exactly (3.3) in a final word and Theorem 3.3
   before the word is chosen.

There is also a source-count caveat.  One final `Q^-|P^+` seam uses two
stutter positions.  Placing identical stutter collars independently at both
the old and new cuts normally uses four physical stutter occurrences and is
not a `B+2` theorem.  The additive-two owner ledger must instead use the
native dropped bank (1.3) together with retained duplicates of `D_1,D_d`,
or exhibit an explicit overlap/reuse of the physical stutters.

The smallest remaining positive statement is therefore a fresh `M Q P`
source/cap theorem which simultaneously provides:

* the two nonowner `U` breaks and every middle owner once;
* two cap-legal stutters satisfying (2.3) (or the asymmetric escape);
* the residual injection of Theorem 3.3;
* the protected arbitrary-width upper rows and the connected owner topology;
  and
* an explicit two-position source ledger, not two disjoint copies of the
  collar.

No `B+2` universal word or all-dimensional regeneration follows from the
local palette and common-Q calculations alone.

Dependencies:

* `MATH_THEOREM_H1_FLAT_BPLUS1_ENDPOINT_WRAP_NOGO_AND_BPLUS2_STUTTER_PALETTE_20260801.md`;
* `MATH_THEOREM_A_ROTATED_HOST_COMMONQ_MATCHING_AND_SAFE_CUT_20260801.md`;
* `MATH_THEOREM_A_FIXED_H_TYPED_SOCKET_PASCAL_PLANTING_20260801.md`.
