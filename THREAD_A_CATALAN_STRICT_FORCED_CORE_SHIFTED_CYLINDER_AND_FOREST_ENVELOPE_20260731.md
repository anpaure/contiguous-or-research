# Strict direct-edge common bases: forced cores, shifted cylinders, and a forest-envelope Hall theorem

Date: 2026-07-31  
Status: theorem/audit; no all-dimensional strict collar is claimed

## 1. Scope and verdict

Let \(F\) be an oriented parameter-\(n\) Catalan path forest, let

\[
 |E(F)|=N,\qquad |Q|=C,\qquad \alpha=C/N<1,
\]

and let \(\mathcal B_{\rm dir}\) be the family of common size-\(C\)
bases of the two **strict direct-edge** pulled-back dual transversal
matroids from
`MATH_THEOREM_CATALAN_DIRECT_EDGEWISE_SIDE_LIFT_RECURSION_20260731.md`.
This family is different from the common bases of the unrestricted
two-step containment matroids.

There are three conclusions.

1. The physical degree-zero law produces a canonical forced subset of
   every strict no-empty deletion bank.  Therefore an unshifted
   equal-density cylinder law can fail already at order one.
2. This failure occurs in the authenticated (n=3) strict Boolean
   instance: the strict common-base family has an eleven-edge core, so no
   probability law on that family has marginal (14/15) on every edge.
   After contracting the core, however, the residual family is exactly
   (U_{3,4}) and has the usual negative cylinder property.  Thus the
   obstruction is forced nonuniform geometry, not a failure of negative
   dependence after the correct contraction.
3. A rigorous replacement for the unshifted quasirandom hypothesis is a
   **shifted cylinder** condition: bound the deterministic local load of
   the forced core, then demand cylinder bounds only on the residual
   choice.  Explicit constants recover all five local estimates used by
   the unconditioned punctured-forest argument.  For the strict physical
   representative itself, a separate forest-envelope Hall theorem gives
   an exact integral sufficient condition.

This does not prove that the required shifted law or forest envelope
exists for every \(n\).  It rules out one proposed transfer and isolates
two checkable replacement hypotheses.

## 2. Forced edges from the physical degree law

For an upper physical vertex \(Y\in\binom{[2n]}{n+1}\), the direct-edge
degree law is

\[
 d^-_F(Y)=\sum_{x\in Y}d_F(Y-x)-2.                 \tag{2.1}
\]

If this degree is zero, the proof of the cited direct-edge theorem gives
a unique child edge \(q_Y\): it is the child edge whose upper colour is
\(Y\).  Define

\[
 Z^-(F)=\{q_Y:d^-_F(Y)=0\}.                         \tag{2.2}
\]

Define \(Z^+(F)\) by the deletion-dual lower formula, and put

\[
 Z(F)=Z^-(F)\cup Z^+(F).                            \tag{2.3}
\]

The direct degree theorem gives

\[
 |Z^-(F)|\le \operatorname {Cat}_n,qquad
 |Z^+(F)|\le \operatorname {Cat}_n.                \tag{2.4}
\]

### Lemma 2.1 (forced-star law)

If a size-\(C\) bank \(Q\) admits strict direct-edge representatives on
both shores with no anchor-free side component, then

\[
                         Z(F)\subseteq Q.            \tag{2.5}
\]

#### Proof

Suppose \(d^-_F(Y)=0\).  No strict upper side atom is incident with \(Y\).
Consequently \(Y\) cannot be an internal vertex of a nonempty strict side
component.  In a no-empty anchored realization it must be supplied as the
inherited anchor belonging to its unique upper-colour child edge \(q_Y\).
The direct-edge normal form identifies inherited anchors with selected
edges of \(Q\), so \(q_Y\in Q\).  This proves \(Z^-(F)\subseteq Q\); the
lower shore is the complement-dual argument.  ∎

The lemma uses the no-empty strict side hypothesis.  A degree-zero vertex
does not by itself force membership in an unrestricted two-step bank, and
it need not be forced if anchor-free components or a different physical
catalogue are permitted.

## 3. The forced-core obstruction to an unshifted cylinder law

For any nonempty family \(\mathcal B\) of \(C\)-subsets of an \(N\)-set
\(E\), define its core

\[
 \operatorname {core}(\mathcal B)=\bigcap_{Q\in\mathcal B}Q.       \tag{3.1}
\]

### Theorem 3.1 (order-one obstruction)

Assume \(C<N\).  If \(\operatorname {core}(\mathcal B)\ne\varnothing\),
then no probability distribution \(\mu\) supported on \(\mathcal B\)
satisfies either

\[
 \Pr_\mu(e\in Q)=C/N\quad(e\in E)                  \tag{3.2}
\]

or the unshifted cylinder inequalities

\[
 \Pr_\mu(A\subseteq Q)\le(C/N)^{|A|}
 \quad(1\le |A|\le L)                              \tag{3.3}
\]

for any \(L\ge1\).

#### Proof

For \(e\in\operatorname {core}(\mathcal B)\), every supported set contains
\(e\), so \(\Pr(e\in Q)=1>C/N\).  Taking \(A=\{e\}\) also contradicts
(3.3).  ∎

Equivalently, a balanced law exists exactly when

\[
 (C/N)\mathbf 1_E\in
 \operatorname {conv}\{\mathbf 1_Q:Q\in\mathcal B\}.              \tag{3.4}
\]

The core hyperplane \(x_e=1\) is the simplest possible separating
certificate when (3.4) fails.

### Corollary 3.2 (strict no-empty consequence)

Let \(\mathcal B_{\rm phys}\) be the strict common bases admitting both
no-empty physical shores.  If \(Z(F)\ne\varnothing\) and
\(\mathcal B_{\rm phys}\ne\varnothing), then no law on
\(\mathcal B_{\rm phys}\) satisfies the unshifted \(C/N\) cylinder bound.

#### Proof

Lemma 2.1 gives \(Z(F)\subseteq\operatorname {core}(\mathcal B_{\rm phys})\).
Apply Theorem 3.1.  ∎

This is a restriction on the **strict direct-edge/no-empty** route.  It
does not contradict the exact equal-marginal distribution on the
unrestricted common bases.

## 4. Exact \(n=3\) Boolean counterexample and its contraction

The exhaustive strict-matroid audit

```text
scratch/audit_catalan_direct_edgewise_n3_matroid_density_20260731.py
scratch/catalan_direct_edgewise_n3_matroid_density_20260731.audit.json
```

has \(N=15,C=14\).  Recording a size-\(14\) basis by its unique retained
edge, the strict common bases are exactly

\[
 E\setminus\{0\},\quad E\setminus\{1\},\quad
 E\setminus\{5\},\quad E\setminus\{11\}.            \tag{4.1}
\]

### Proposition 4.1 (authenticated strict balanced-law no-go)

For this actual Boolean instance,

\[
 \operatorname {core}(\mathcal B_{\rm dir})
 =E\setminus\{0,1,5,11\},qquad
 |\operatorname {core}(\mathcal B_{\rm dir})|=11.   \tag{4.2}
\]

Hence no law supported on the strict common bases has marginal \(14/15\)
on every child edge, and no such law obeys the proposed cylinder bound
even for singletons.

#### Proof

Equation (4.1) is the complete size-\(14\) common-basis list in the
authenticated exhaustive audit.  Intersecting those four sets gives
(4.2), and Theorem 3.1 applies.  ∎

### Proposition 4.2 (negative dependence survives the correct contraction)

Contract the eleven-edge core and put \(R=\{0,1,5,11\}\).  The residual
bases are exactly the four three-subsets of \(R\), namely the bases of
\(U_{3,4}\).  Under their uniform distribution, for every
\(A\subseteq R\), \(a=|A|\),

\[
 \Pr(A\subseteq Q)=
 \begin{cases}
 (4-a)/4,&0\le a\le3,\\
 0,&a=4,
 \end{cases}                                        \tag{4.3}
\]

and

\[
 \Pr(A\subseteq Q)\le(3/4)^a.                      \tag{4.4}
\]

#### Proof

A residual basis omits one uniformly chosen element of \(R\).  It contains
\(A\) exactly when the omitted element lies outside \(A\), proving (4.3).
For \(a=0,1,2,3,4\), inequality (4.4) is respectively equality, equality,
\(1/2\le9/16\), \(1/4\le27/64\), and \(0\le81/256\).  ∎

Thus the \(n=3\) obstruction is not evidence against all forms of negative
dependence.  It specifically disproves an **unshifted equal-density** law
on the full edge set.  Forced contraction is mathematically necessary.

## 5. A shifted-cylinder theorem with explicit constants

The unconditioned punctured-forest theorem uses five local edge families.
Put

\[
 s_n=\left\lfloor {4n\over\log n}\right\rfloor .
\]

Their uniform-\(Q\) mean bounds and integer target thresholds are

\[
 (\lambda_1,\ldots,\lambda_5)
 \le(5,3n,6,6,5n),                                  \tag{5.1}
\]

\[
 (b_1,\ldots,b_5)=(s_n,20n,s_n,s_n,30n).           \tag{5.2}
\]

There are \(O(4^n)\) such local families on both shores.

### Theorem 5.1 (forced-core shifted-cylinder criterion)

Let \(Z\subseteq E(F)\) be deterministic and let \(Q=Z\cup Q'\), where
\(Q'\subseteq E(F)\setminus Z\) is random.  Suppose that for every one of
the five local families \(L\):

1. \(z_L=|Z\cap L|\le b_j/2\), where \(j\) is the type of \(L\);
2. there are numbers \(p_e\in[0,1]\), \(e\in L\setminus Z\), with
   \(\sum_{e\in L\setminus Z}p_e\le\lambda_j\);
3. for every \(A\subseteq L\setminus Z\) with
   \(|A|\le b_j-z_L+1\),

   \[
   \Pr(A\subseteq Q')\le\prod_{e\in A}p_e.         \tag{5.3}
   \]

Then, for all sufficiently large \(n\), with positive probability every
local count obeys

\[
                         |Q\cap L|\le b_j.           \tag{5.4}
\]

Indeed the probability that any one of the \(O(4^n)\) inequalities fails
is \(o(1)\).

#### Proof

Put \(Y=|Q'\cap(L\setminus Z)|\).  Failure of (5.4) means

\[
 Y\ge t:=b_j-z_L+1\ge b_j/2.                       \tag{5.5}
\]

From (5.3),

\[
 \mathbb E (Y)_t
 \le t!\!\sum_{|A|=t}\prod_{e\in A}p_e
 \le\left(\sum_ep_e\right)^t\le\lambda_j^t.        \tag{5.6}
\]

Therefore

\[
 \Pr(Y\ge t)\le{\lambda_j^t\over t!}
 \le\left({e\lambda_j\over t}\right)^t.           \tag{5.7}
\]

For types \(1,3,4\), \(t\ge2n/\log n\) and

\[
 -\log\Pr(Y\ge t)\ge(2-o(1))n.                    \tag{5.8}
\]

For type (2),

\[
 -\log\Pr(Y\ge t)
 \ge10n\log {10\over3e}>2.03n.                    \tag{5.9}
\]

For type (5),

\[
 -\log\Pr(Y\ge t)
 \ge15n\log {3\over e}>1.47n.                     \tag{5.10}
\]

All three exponents exceed \((\log4)n\).  A union bound over \(O(4^n)\)
families proves (5.4) simultaneously with probability \(1-o(1)\).  ∎

### Consequence 5.2

For the unrestricted physical slot catalogue, Theorem 5.1 is a valid
replacement for the unshifted cylinder hypothesis in the pointwise
punctured-forest theorem: it yields the same five local bounds and hence
\(P-o(P)\) side forests.

For the strict direct-edge catalogue, Theorem 5.1 supplies only a
quasirandom strict common bank \(Q\).  It does **not** produce the strict
representatives or the rooted graphic base.  Those remain separate
integral rows.

The explicit hypotheses also expose the new obstruction.  A forced core
is harmless only if it is locally diffuse:

\[
 |Z\cap L|\le b_j/2                              \tag{5.11}
\]

for every relevant local family.  The global estimate
\(|Z|\le2\operatorname {Cat}_n\) does not imply (5.11).

## 6. A partition-plus-graphic sufficient theorem

Fix one shore on its \(N\) physical owners, its \(P\) lower palette
blocks, its \(P\) upper palette blocks, the physical capacity vector
\(b_v\in\{1,2\}\), and
\(N-P=C-K\) distinct root-star edges \(R\).  An allowed atom has one lower
colour, one upper colour, and one physical edge.

### Theorem 6.1 (forest-envelope Hall theorem)

Suppose there is a subcatalogue \(\mathcal A_0\) of allowed atoms such
that:

1. the physical projection is injective on \(\mathcal A_0\), and the
   simple graph consisting of \(R\) and every projected physical edge is a
   forest;
2. even if all atoms of \(\mathcal A_0\) are exposed, their physical
   incidences obey the capacities \(b_v\);
3. in the bipartite graph whose left and right vertices are the two
   palette banks and whose edges are the atoms of \(\mathcal A_0\), Hall's
   inequalities hold:

   \[
   |N(S)|\ge|S|\qquad(S\text{ in either palette shore}).           \tag{6.1}
   \]

Then there is an exact palette-saturating, anchor-capped, no-empty linear
side forest with \(c_0=0\).

#### Proof

By (6.1), choose a perfect matching \(J\subseteq\mathcal A_0\) between
the \(P\) lower and \(P\) upper palette blocks.  It has \(P\) atoms.  By
hypotheses 1 and 2, \(T=J\cup R\) is graphic-independent and respects all
physical capacities.  Moreover

\[
 |T|=P+(N-P)=N.                                     \tag{6.2}
\]

The rooted physical graph has \(N+1\) vertices.  A forest with \(N\) edges
on this vertex set is connected, hence is a spanning tree.  The rooted
side-tree identity now gives a no-empty side forest with \(c_0=0\).  ∎

The theorem is deliberately one-sided and stronger than necessary.  Its
value is that, on a capacity-safe forest envelope, the difficult
intersection of two partition bases, a graphic base and overlapping
degree caps collapses to ordinary bipartite Hall.  Finding such envelopes
simultaneously on both shores, with one common \(Q\), is not proved.

## 7. Exact remaining boundary

The following implications are now rigorous:

\[
\begin{array}{c}
\text{strict no-empty physical realization}\\
\Downarrow\\
Z(F)\subseteq Q
\end{array}
\qquad
\begin{array}{c}
\text{unshifted }C/N\text{ cylinder law}\\
\Downarrow\\
Z(F)=\varnothing.
\end{array}                                         \tag{7.1}
\]

Thus the unrestricted balanced-common-basis law cannot simply be reused
on the strict direct-edge family.  The minimum surviving probabilistic
hypothesis is:

* contract the forced core;
* prove residual cylinder bounds with their true, generally nonuniform
  marginals;
* prove local diffuseness of the forced core;
* then solve the strict two-partition/graphic/cap representative row, for
  example by a forest envelope as in Theorem 6.1.

No theorem in this note supplies the last three bullets for arbitrary
child forests.  In particular, it does not prove DERF, RSB, a common cap,
deep-shadow preservation, a compiler, or \(\nu(k)=B(k)\).

## 8. Adversarial audit

1. **Unrestricted/strict distinction.**  Proposition 4.1 concerns the
   strict pulled-back direct-edge matroids.  The unrestricted \(n=3\)
   deletion banks may all be common bases; there is no contradiction.
2. **Forced-star scope.**  Lemma 2.1 uses no-empty anchored strict sides.
   It is not a statement about arbitrary punctured forests.
3. **Negative dependence.**  The \(n=3\) residual law is positively good:
   it is \(U_{3,4}\).  The no-go is only for the unshifted constant
   \(C/N\) vector on all fifteen edges.
4. **Shifted-cylinder direction.**  Theorem 5.1 is sufficient, not
   necessary.  Its half-threshold local-diffuseness constants were chosen
   to beat the \(O(4^n)\) union bound; no optimality is claimed.
5. **Forest envelope.**  Theorem 6.1 assumes capacity safety for the whole
   subcatalogue, much stronger than capacity safety of one matching.  It
   is an exact positive class, not an all-\(n\) construction.
