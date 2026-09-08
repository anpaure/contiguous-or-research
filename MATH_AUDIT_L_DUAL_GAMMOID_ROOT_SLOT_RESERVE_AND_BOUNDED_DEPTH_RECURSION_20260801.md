# Independent audit: dual-gammoid root-slot reserve and bounded-depth recursion

**Date:** 2026-08-01  
**Audited file:** MATH_THEOREM_L_DUAL_GAMMOID_ROOT_SLOT_RESERVE_AND_BOUNDED_DEPTH_RECURSION_20260801.md  
**Method:** independent symbolic replay of every rank, Hall, pruning, and
recursion row; no finite computation.  
**Verdict:** **PASS WITH THE PHYSICAL ROOT-SLOT LIFT EXPLICITLY
CONDITIONAL.**

## 1. Cell-matroid identity

Let \(M\) be the transversal matroid on compiler cells and suppose the
target side has size \(t\) and is saturated.  Then \(r_M(C)=t\).  For every
cell set \(D\), dual rank is

\[
 r_{M^*}(D)=|D|-t+r_M(C-D).
\]

Thus \(D\) has full dual rank exactly when \(r_M(C-D)=t\), which is exactly
target saturation after deletion.  This verifies Theorem 1.1, including the
direction of the alternating-linkage representation: matched cells point to
their targets and unmatched incidences point toward cells, ending at cells
unused by the reference matching.

If \(D\) is unsafe, Hall gives nonempty \(A\) with

\[
 |D\cap N(A)|\ge |N(A)|-|A|+1.
\]

Conversely deleting that many cells from a minimizing \(N(A)\) leaves at
most \(|A|-1\) neighbors.  Hence the dual girth is exactly one plus the
minimum Hall slack.  No scalar-capacity assumption enters this argument.

For one-cell sites, Rado/matroid intersection applies after passing to the
explicit task-labelled pullback of the cell matroid; candidates sharing one
physical cell are parallel.  For multi-cell packets, item 2536L's two-row
augmentation counterexample still applies; the new note does not silently
promote packets to matroid elements.

## 2. Boolean root-slot count and sharpness

For \(S\in\binom{[2m+1]}{m-j}\), the number of rank-\(m\) roots containing
\(S\) is

\[
 \binom{(2m+1)-(m-j)}{j}=\binom{m+j+1}{j}=D_j.
\]

The cited protected rankwise theorem permits deletion of any \(D_j-1\)
roots.  Since \(D_1-1=m+1\) and \(D_j\) increases with \(j\), every one of
the disjoint rank layers survives the same at-most-\(m+1\) root deletion.
Their matchings unite because their cell copies are disjoint.

At \(j=1\), a fixed \((m-1)\)-facet has exactly \(m+2\) containing roots.
Deleting precisely those roots isolates it.  This checks both the uniform
threshold and the note's careful scope: all banks through size \(m+1\) are
safe, while only some—not all—banks of size \(m+2\) fail.

## 3. Physical lift quantifiers

The proof of Theorem 3.2 uses only the following three literal facts:

1. every Boolean containment edge is present in one common cap state;
2. all non-Boolean targets have a matching disjoint from every candidate
   ray;
3. a ray can delete a slot cell only above one of its declared hazard roots.

After deleting the union of hazard fibres, Theorem 2.1 gives the Boolean
slot matching and the fixed residual matching supplies the other targets.
Therefore (3.2) is sufficient.  None of these facts follows from separate
rankwise matchability, so the theorem correctly labels the lift as a
hypothesis.

The minimal quantifier counterexample also replays.  With
\(N(x)=\{u,v\}\), \(N(y)=\{u\}\), deleting \(v\) leaves a matching in either
one-target projection but no joint matching.  Thus “for every rank there is
a matching” does not imply one common matching; abstractly private root or
owner labels do not repair the cut.

## 4. Menu pruning arithmetic

After retaining \((i-1)\ell\) candidates, maximum cross-list degree
\(\Delta\) removes at most \(\Delta(i-1)\ell\) candidates from list \(i\).
The worst row \(i=H\) is feasible when

\[
 L_0-\Delta(H-1)\ell\ge\ell,
\]

which is the first bound in (4.1).  The complete hazard union has at most
\(aH\ell\) roots, giving the second bound.  Hence the entire option bank,
not merely one eventual transversal, is compiler-coindependent.

For ordered flags, only the shared tail/head/owner **resource** conflict
degree is known to be at most \(3(H-1)\).  The final theorem now requires a
separate nonadjacent chronology planting, or another full failed-cross
degree bound, before applying Theorem 4.1.  In the static prospective
version no collar claim is made.  The number of prepared roots is at most
\(H+H\ell_{\rm stat}\), and (4.4) makes this at most \(m+1\).  The protected
complete-atlas construction assigns every named target to a flexible-root
occurrence, so deleting every prepared occurrence leaves a saturating
static matching.  For fixed \(H\) and \(d,b=o(m)\), the menu bounds are
linear in \(m\).  The note correctly calls this positive density only inside
the local \(\Theta(m)\) endpoint lists, not among the exponentially many
roots.

The static quantifier order is essential: menus and all their head flags are
frozen first, and only then are the flexible flags completed.  The result
does not place these cells in a pre-existing mixed table.

## 5. Laminar row

Given a cut-complete laminar family, residual Hall is

\[
 \sum_{p\in P}|R_p\cap J|\le
 |J|-\#\{t:N(t)\subseteq J\}.
\]

If every coefficient is zero or one and the induced site sets \(E_J\) are
themselves laminar, these are exactly laminar-matroid capacities and Rado's
rank inequalities apply.  The audit confirms that both qualifications are
needed.  A packet that meets one tight branch twice gives a coefficient-two
knapsack row for which matroidality can fail; cell laminarity alone does not
give a matroid on packets.  The note also now records that the full cell cut
has coefficient \(d\) on an uncontracted depth-\(d\) ray, so this face is
normally useful only at depth one, after packet contraction, or after a
one-cell-per-branch decomposition.

## 6. Relocation-depth counterexample

The generalized states in (7.1) have common total size \(m\).  Replacing
\(X_i\) by \(X_i^+\) changes the represented target from
\(q_i=K+\{i\}\) to \(q_{i+1}=K+\{i+1\}\).  The connector
\(Z_i\to A_i\to Z_{i+1}\) is used only for \(0\le i<N-1\), so no undefined
\(Z_N\) occurs.  With the declared reference matching, the second \(X_0\)
is the sole free root port, every intermediate \(q_i\) is matched at the
unique next bay, and \(q_N\) is the only hole.  Therefore the reachable
network of the **declared site catalogue** is a path with \(N=m+2\) sites.
The note does not claim an exhaustive classification of every other legal
stutter in the ambient chronology.

Increasing \(m\) by one adds a fixed letter to \(K\) and one terminal bay;
all old transitions remain literal and the declared unique path length
increases by one.  The site-owner endpoints are distinct and ray
occurrences are private, but the retained \(q_0\) provider repeats the
root-site owner.  The final theorem therefore does not claim privacy for
every background provider endpoint.  Within this exact scope, Boolean
owner degree, rankwise Hall, separated sites, and a same-parity recursive
embedding do not imply bounded alternating distance.

The bounded-depth state was audited with two corrections during drafting:
general length-bounded vertex-disjoint paths were **not** called ordinary
time-expanded maxflow, because shared physical capacities across time
copies make that reduction invalid without another gadget.  The final note
uses an exact path-packing predicate.  Its constant-height funnel subclass
is an ordinary acyclic strict-gammoid/maxflow face.  The zero-stretch
recursion now also quantifies over every allowed child deletion: its
inherited pullback must be an allowed parent deletion, while new direct bays
must be pairwise disjoint and survive every child deletion.  Under those
hypotheses injection preserves witness paths directly.  A compulsory
\(c\)-site extension yields only \(L_{t+1}\le L_t+c\), exactly as stated.

## 7. Final scope verdict

The note proves a sharp coindependent reserve in the abstract Boolean
root-slot compiler, a linear planted menu in the static complete atlas, and
exact matroid/laminar/funnel sufficient faces.  It does **not** prove that
the physical ordered endpoint is a same-neighbour stutter, that its ray
cells are one root fibre in a common cap state, or that a zero-stretch
occurrence funnel exists.  Consequently it makes no \(O(1)\) sidecar or
\(B(k)+O(1)\) claim.  With those qualifications, every displayed theorem
and counterexample passes.
