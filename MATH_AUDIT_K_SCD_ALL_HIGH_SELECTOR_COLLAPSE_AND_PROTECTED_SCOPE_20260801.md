# Audit: the SCD collapse of the all-high ordered-chain selector

**Date:** 2026-08-01  
**Status:** **PASS for the exact marked selector LP; physical correlation
rows remain open.**

## 0. Verdict

Let \(n=2m+1\), \(1\le d\le m+1\), put
\[
                         L_r=\binom{[2m+1]}r,
\]
let roots be the rank-\(m\) sets, and let a depth-\(d\) all-high local flag
at a root \(q\) be a descending path

\[
 q=T_0\supset T_1\supset\cdots\supset T_{d-1},
 \qquad |T_j|=m-j.                                      \tag{0.1}
\]

The proposed symmetric-chain-decomposition construction is sound for the
exact selector LP

\[
 \sum_{f:\operatorname{root}(f)=q}x_f=1,
 \qquad
 \sum_{f:T_j(f)=T}y_{f,j}=1,
 \qquad 0\le y_{f,j}\le x_f,                         \tag{0.2}
\]

with binary (x,y).  It chooses one local flag at every root and marks one
occurrence of every high target, simultaneously at every rank.  The
unrestricted nested-chain correlation row is therefore closed exactly.

There is no hidden LP requirement invalidating the construction.  The
important qualifier is that the arbitrary continuation below a short SCD
chain is **unmarked**.  Those suffixes still exist as physical flag data,
but (0.2) does not require every suffix occurrence to be a named provider.
Thus the theorem does not solve a stronger all-occurrence load profile, nor
does it produce legal successor turns, an Euler chronology, upper shadows,
residence, or a small common order menu.

## 1. Why every symmetric chain has exactly one root

Fix a symmetric-chain decomposition of (B_{2m+1}).  Every chain has the
form

\[
 C_a\subset C_{a+1}\subset\cdots\subset C_{2m+1-a},
 \qquad a\le m.                                      \tag{1.1}
\]

It therefore contains rank (m), and strict rank increase makes that
member unique.  Because the chains partition the lattice, sending a chain
to its rank-\(m\) member is a bijection from the SCD chains to
\(\binom{[2m+1]}m\).  Hence there is exactly one SCD chain available for
every root; no root is duplicated or omitted.

## 2. Literal flag completion and exact marks

Suppose a chain starts at rank (a), write (ell=m-a), and let

\[
 z_j=C_{m-j+1}-C_{m-j}\qquad(1\le j\le\ell).        \tag{2.1}
\]

Then

\[
 C_{m-j}=C_m-\{z_1,\ldots,z_j\}.                   \tag{2.2}
\]

If (ell<d-1), choose another (d-1-ell) distinct elements from the
minimum set (C_a).  This is always possible because

\[
 |C_a|=m-ell\ge d-1-ell
\]

is equivalent to (d-1\le m).  Put the elements from (2.1) first in the
deletion word and the arbitrary continuation after them.  This gives a
literal local order flag of the required depth.

Mark the rank-((m-j)) occurrence only for (j\leell).  A fixed target
(T) of rank (m-j) lies in one SCD chain.  That chain starts at a rank at
most (m-j), so its associated root flag follows the chain through (T)
and marks it.  No other root flag marks (T), because no other SCD chain
contains it.  This proves every target equation in (0.2) exactly once.

The arbitrary deeper continuation causes no extra marked load.  This is
legal precisely because (0.2) has independent mark variables satisfying
only (y_{f,j}\le x_f).  If a later physical model makes every suffix an
unavoidable resource row, that is an additional model and the SCD theorem
must not be cited for it.

## 3. Prepared flags: what is already closed

An arbitrary family of prescribed downward segments need not be contained
in one preselected SCD.  That does **not** leave the selector LP open.

For every nonempty family (mathcal X) of rank-((r-1)) sets,
(1\le r\le m), the Boolean upper shadow satisfies

\[
 |\partial^+\mathcal X|
 \ge |\mathcal X|+2m+1-r.                          \tag{3.1}
\]

This follows by complementing and applying the Lovasz form of
Kruskal--Katona; the real-binomial difference

\[
 \binom{x}{k-1}-\binom{x}{k},\qquad k=2m+2-r,
\]

is increasing on (x\in[k,2m+1]) and has minimum (k-1=2m+1-r).

At the top adjacency the reserve is (m+1).  Consequently, after deleting
any (h\le m+1) prepared rank-(m) roots, Hall still matches every
rank-((m-1)) target to a distinct flexible root.  At each lower adjacency,
ordinary normalized matching supplies a matching saturating the lower
shore.  The union is a chain forest covering every high target once.

Therefore any (h\le m+1) arbitrary prescribed root flags coexist with an
exact selector: retain those flags, mark none of their suffixes, and obtain
all marks from the flexible-root chain forest.  This is stronger than an
SCD-extension statement and has zero marked-target sidecar.

There are two different ways to interpret ``the segments themselves must be
marked'', and they must not be conflated.

In the actual occurrence-labelled LP, fix forced variables
\(y_{f_i,j}=1\), with \(1\le j<d\), on at most \(h\le m+1\) prescribed
root flags.  Feasibility is equivalent to the forced target values
\(T_j(f_i)\) being distinct.
Necessity is the target equality in (0.2).  For sufficiency, start with the
quarantined solution above and transfer the unique flexible mark on every
forced target to its prescribed occurrence.  Marks at different depths of
one chosen flag need not be contiguous.

For fully marked prefixes starting at distinct rank-\(m\) roots, target
injectivity is equivalent to pairwise vertex-disjointness.  Two such prefixes
cannot concatenate: their first meeting is a target collision.  Hence
vertex-disjointness is the exact protected-rooted-prefix formulation.

Only after root labels and duplicate occurrences are forgotten does the
edge-union statement apply.  For an unlabelled required edge set \(E\), its
edges \(E_r\) at every interface \(m-d+2\le r\le m\) must be a matching
and must satisfy residual Hall

\[
 |N(X)\setminus U(E_r)|\ge |X|
 \quad\bigl(X\subseteq L_{r-1}\setminus D(E_r)\bigr).          \tag{3.2}
\]

where \(N\) is neighbourhood in the rank-\((r-1,r)\) containment graph.
For a union of at most \(h\le m+1\) saturated fragments, (3.1) makes these
Hall rows automatic.  Thus the unlabelled union is extendible exactly when
it is a descending linear forest; arbitrary fragments may concatenate in
this model only.

For \(m\ge2\) and \(d\ge2\), the bound is sharp.  Let \(A\) have rank
\(m-1\), fix \(a\in A\), and for every one of the \(m+2\) elements
\(x\notin A\) prescribe

\[
 A\cup\{x\}\to(A\setminus\{a\})\cup\{x\}.
\]

The rooted edges and marked targets are pairwise disjoint, but their roots
exhaust every possible provider of \(A\).  Thus target injectivity and
vertex-disjointness need not suffice beyond \(h=m+1\).

The exact prepared-selector boundary is therefore:

* arbitrary prescribed flags: feasible when their marks are quarantined;
* occurrence-labelled forced marks: exactly target-injective for
  \(h\le m+1\);
* fully marked distinct-root prefixes: exactly pairwise vertex-disjoint in
  that range; and
* unlabelled physical fragments: exactly residual Hall, reducing to a
  descending linear forest in that range.

## 4. Relation to the random atlas and fractional law

For deletion depth \(j\), a fixed target
\(T\in\binom{[2m+1]}{m-j}\) is supported by a uniform global order with
probability

\[
 p_j={\binom{m+j+1}{j}\over\binom{2m+1}{j}}.        \tag{4.1}
\]

Indeed it is supported exactly when the first (j) global coordinates
avoid (T).  Put

\[
 \mathcal N=\sum_{j=1}^{d-1}\binom{2m+1}{m-j},
 \qquad p_* =\min_{1\le j<d}p_j.                   \tag{4.2}
\]

Then

\[
 L=\left\lceil {\log\mathcal N+c\over p_*}\right\rceil       \tag{4.3}
\]

independent orders support every target at every high rank with probability
at least (1-e^{-c}).  If (2d-3\le m), then (p_*=p_{d-1}), so

\[
 p_*^{-1}=
 {\binom{2m+1}{d-1}\over\binom{m+d}{d-1}}.          \tag{4.4}
\]

This matches the bottom-suffix covering lower bound within the logarithmic
(O(m)) factor.  It is targetwise support only.

Uniform local orders give the exact unmarked fractional marginal

\[
 \rho_j=
 {\binom{m+j+1}{j}\over\binom mj}
 ={\binom{2m+1}m\over\binom{2m+1}{m-j}}.            \tag{4.5}
\]

Fractional thinning by (1/\rho_j) yields each marked target row exactly
one.  The SCD construction is an integral realization of the marked target
rows, not a rounding theorem inside the sampled atlas.  Its local flags may
require up to one global-order extension per root.  Targetwise support in
the (L)-order atlas does not imply that the correlated SCD paths are
available there.

## 5. Two different stronger multiplicity questions

The marked selector must be separated from the unmarked load profile.

* With no pins, a layered node-capacitated Boolean flow rounds (4.5)
  integrally so that every target load is
  (lfloor\rho_j\rfloor) or (lceil\rho_j\rceil) at all depths.
* Three prepared roots (S+\{a_i\}) under one robust order may have one
  common suffix at every positive depth.  Whenever

  \[
  j(j+1)<(m-j+1)\log2,
  \]

  one has (\rho_j<2), so the balanced cap is two but the prepared load is
  three.  This produces
  (Theta(\min\{d,\sqrt m\})) violated rank rows.

Thus the SCD theorem gives zero **marked-cover** defect, including a bounded
prepared bank, but does not imply dimension-independent balanced unmarked
load error.  Fractional feasibility cannot be promoted to an (O(1))
claim on that stronger face.

## 6. The first genuine one-copy gap is physical

The unrestricted and bounded-prepared marked-chain selector rows are now
closed.  The remaining conditions are not consequences of an SCD:

1. the flags at consecutive roots must satisfy the literal survivor/age
   inequalities;
2. selected turns must balance root and owner indegree/outdegree and admit
   the required Euler topology;
3. upper shadows and residence must survive the same chronology;
4. if a small global-order atlas is required, its root-order columns must
   contain the needed chain forest.

There is also an exact quantifier warning in the robust-order interface.  An
ordered-shift portal (p\to q_\beta) uses the prepared order at both the
tail and the head.  Fixing only the (O(1)) portal tails does not retain the
linear list after the heads choose mixed orders.  If
(z_1,\ldots,z_m) is the prepared tail order, a mixed head order is legal
only when its first (d-1) deleted labels are

\[
 z_2,\ldots,z_{d-1},w,
 \qquad w\in\{z_d,\ldots,z_m\}.                    \tag{6.1}
\]

Only (m-d+1) of the ((m)_{d-1}) head prefixes work.  Independent head
orders leave expected list size at most

\[
 (m+1){m-d+1\over(m)_{d-1}},                       \tag{6.2}
\]

which is (O(1)) at (d=3) and tends to zero for fixed (d\ge4).
Accordingly, the balanced-turn portal theorem still needs either a
same-order head halo or a cross-order robust-turn theorem, followed by
residual fractional turn Hall.  None of these follows from the exact SCD
selector.

## 7. Audited boundary

The proposed collapse is valid, and in the exact marked selector LP it is
stronger than a marginal or fractional statement:

\[
 \boxed{\text{unrestricted all-high marked chain correlation is solved.}}
\]

Moreover, bounded arbitrary prepared flags are already harmless at this
selector level by quarantine plus the (m+1) upper-shadow reserve.  What
remains is a **transition-compatible protected selector**, not an SCD
existence problem.  No additive-constant word conclusion is inferred.
