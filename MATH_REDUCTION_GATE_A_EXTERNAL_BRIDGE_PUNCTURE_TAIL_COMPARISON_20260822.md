# Gate A: external-bridge Gram form and tail-robust puncture comparison

**Date:** 2026-08-22  
**Status:** exact dominant-cell reduction and tail-mass-free puncture
comparisons.  Sparse puncture boundary sets are negligible in mass, the
dominant pairs coming from nonclean full-factor blocks have negligible
global mass, and the duplicate bridge has negligible oscillation inside
each clean block.  The between-block and bulk activity-bridge regressions
remain open.

## 0. Result

Fix a root target (v) in the complete directed-punctured catalogue.  On
the dominant cell

\[
                    (F\cap H)-\{v\}=\varnothing,
\]

the already-proved root-containing star theorem removes the part of
(K_2^\circ(F,H)) coming from further rows (G\ni v), at a uniform
(o(z/q_0)) cost.  The remaining external-row kernel has the exact form

\[
 \boxed{
 K_{\rm ext}(F,H)=
 \sum_{G\not\ni v}\{h_G(F)h_G(H)-b_G(F)b_G(H)\},}       \tag{0.1}
\]

where

\[
 h_G(F)=w(G\cap F)-1,\qquad
 b_G(F)=\mathbf1_{\{G\cap F\ne\varnothing\}}.           \tag{0.2}
\]

Thus the live dominant-cell problem is a signed difference of two Gram
kernels: the positive activity bridge and the unweighted duplicate bridge.
Neither Gram term may be discarded separately.

There is nevertheless a tail-relative comparison which costs no lower
bound on the tail mass.  Let (X) be the product target state, let
(d=d_v(X)), and for an increasing function (g\ge0) put

\[
 W_g(A)=\mathbb E[\mathbf1_{\{A\subseteq X\}}g(d)].       \tag{0.3}
\]

If every target has retention probability at least (x), then for any
two forced target sets (A,B),

\[
 \boxed{
 {W_g(A)\over W_g(B)}\le x^{-|B-A|},\qquad
 {W_g(B)\over W_g(A)}\le x^{-|A-B|},}                    \tag{0.4}
\]

whenever the denominators are positive.  This applies to both literal
pair weights (extended by zero for (d<2))

\[
 g_{12}(d)=(d-2)_{10},\qquad
 g_c(d)={(d-c)_+^{12}\over(d)_2},\quad c\ge11.           \tag{0.5}
\]

Now fix two distinct directed cyclic factors whose full target sets both
contain (v).  Each has (b-1=2r) punctures which retain (v).
Changing both punctures adds at most four new forced targets.  Hence,
within this block, either pair law induced by (0.5) has
maximum-to-minimum weight ratio at most (x^{-4}).  Consequently every
set (mathcal B) of puncture pairs satisfies

\[
 \boxed{
 \Pi_g(\mathcal B\mid\hbox{the fixed full-factor pair})
 \le x^{-4}{|\mathcal B|\over(b-1)^2}.}                  \tag{0.6}
\]

In particular, if (|\mathcal B|=O(b)), then, uniformly for
(x\ge r^{-\alpha}),

\[
 \Pi_{12}(\mathcal B\mid\text{block})+
 \Pi_c(\mathcal B\mid\text{block})
 =O(r^{-1+4\alpha})=o(1)                                \tag{0.7}
\]

through the live range (alpha\le1/(256K)), (K\ge1).  This remains
true for the live deterministic cutoffs

\[
 (1+\delta)z\le c\le Kz                                \tag{0.8}
\]

(with integer rounding), provided the corresponding pair weight is
nonzero.  No probability of the upper-degree tail appears in (0.6).

If the two full factors have an additional common target (u\ne v), an
off-root-disjoint puncture pair must delete (u) on at least one side.
There is at most one puncture doing so on each factor.  Therefore at most
(2(b-1)) of the ((b-1)^2) root-retaining pairs in a nonclean block can
lie in the dominant cell.  Since (0.6) holds for nonclean as well as clean
blocks, mixing over the full-factor blocks gives, for either global pair
law (when it is defined),

\[
 \boxed{\Pi_g(\text{dominant and nonclean})
 \le {2x^{-4}\over b-1}=O(x^{-4}/r).}                   \tag{0.9}
\]

This is (O(r^{-1+4\alpha})=o(1)) in the live range and contains no
lower bound on the cutoff-tail mass.

The event in (0.9) is **dominant and nonclean**, not the exceptional
overlap event of G.19.  Thus (0.9) does not prove
\(\Pi_c(\tau\ne(0,0))=o(1)\).  Nor can it be divided by the mass of the
dominant cell to control the conditional law \(\Pi_c^0\) without a lower
bound on that cell mass.  Its unconditional mass conclusion is the exact
tail-mass-free scope.

There is also a pointwise gain for the duplicate bridge.  If (D_M) is
the middle-target catalogue degree and (C,D) form a clean full-factor
pair, then

\[
 \boxed{\operatorname {osc}_{h,k}
 B^0(E_h(C),E_k(D))=O(D_M/r).}                          \tag{0.10}
\]

Thus (q_0\operatorname {osc}B^0=O(z_v/r)), where
(z_v=D_vq_0/p_v) is the conditional product-law root degree.  This
removes the duplicate bridge from the **within-block puncture
comparison**, under an arbitrary tail tilt.  It does not compare the
block baselines of (B^0), so a between-full-factor duplicate regression
remains open.

Accordingly, at the mass level a boundary-cell proof may delete every
external-bridge exception supported on (O(r)) puncture pairs per clean
full-factor pair.  Turning this into deletion of a kernel-weighted term
still requires a pointwise envelope or uniform integrability.
What is still required is a bulk theorem after those exceptions are
removed: for the activity bridge, either the remaining value of (0.1) is
puncture-independent up to (o(z/q_0)), or its signed likelihood
covariance is favorable or (o(z/q_0)).  One must also control the
between-block baseline of the duplicate bridge.  Boundary codegrees and
factorial off-root disjointness alone do not prove these bulk statements.

The exact (r=2) adverse-sign example does not contradict this reduction:
its dominant cell is empty.  Every punctured row at (r=2) contains four
of the five lower-shore singleton targets, so two root rows have at least
three common lower targets.

## 1. External bridge identity

Let (F,H\ni v) and assume (F\cap H=\{v\}).  For a further external row
(G\not\ni v), put

\[
                         A=G\cap F,\qquad B=G\cap H.
\]

The sets (A,B) are disjoint.  If either is empty, the two-star
coefficient is zero.  Otherwise multiplicativity of
(w(S)=\prod_{u\in S}p_u^{-1}) gives

\[
\begin{aligned}
 w(A\cup B)-w(A)-w(B)
 &=w(A)w(B)-w(A)-w(B)\\
 &=(w(A)-1)(w(B)-1)-1.                                  \tag{1.1}
\end{aligned}
\]

The right side of (1.1) is also zero after multiplication by
(b_G(F)b_G(H)) when one intersection is empty.  Summing over external
rows proves (0.1).

For orientation, if (mathcal A) is any family of root rows, extend the
right side of (0.1) to all ordered pairs, whether or not they are
off-root disjoint.  Then its ordered-distinct average has the exact Gram
form

\[
\begin{aligned}
 {1\over(|\mathcal A|)_2}\sum_{F\ne H\in\mathcal A}
 \widetilde K_{\rm ext}(F,H)
 ={1\over(|\mathcal A|)_2}\sum_{G\not\ni v}\bigg[&
   \left(\sum_{F\in\mathcal A}h_G(F)\right)^2
       -\sum_{F\in\mathcal A}h_G(F)^2\\
 &-\left(\sum_{F\in\mathcal A}b_G(F)\right)^2
       +\sum_{F\in\mathcal A}b_G(F)^2\bigg].           \tag{1.2}
\end{aligned}
\]

This is obtained by expanding the two squares.  On the dominant cell the
extended kernel equals the genuine kernel.  Formula (1.2) explains why an
absolute bridge-row count is not the correct target: the activity and
duplicate energies occur with opposite signs.

## 2. A monotone forcing comparison

### Lemma 2.1

Let ((X_u)_{u\in\mathcal V}) be independent Bernoulli variables with
(p_u\ge x>0).  Let (Y(X)\ge0) be increasing.  For a target set (A),
write

\[
                         W(A)=\mathbb E[\mathbf1_{\{A\subseteq X\}}Y(X)].
\]

Then (0.4) holds with (W_g) replaced by (W).

#### Proof

Put (C=A\cap B), (A'=A-C), and (B'=B-C).  Condition on every
coordinate of (C) being one.  The remaining coordinates retain their
product law.  Since (Y\ge0),

\[
 W(A)\le \Pr(C\subseteq X)\,
              \mathbb E[Y\mid C\subseteq X].             \tag{2.1}
\]

Both (Y) and (mathbf1_{\{B'\subseteq X\}}) are increasing.  Harris's
inequality in the conditional product law gives

\[
 W(B)\ge \Pr(C\subseteq X)\Pr(B'\subseteq X)
              \mathbb E[Y\mid C\subseteq X].             \tag{2.2}
\]

Divide (2.1) by (2.2) and use
(Pr(B'\subseteq X)\ge x^{|B'|}).  This proves the first inequality;
interchanging (A,B) proves the second.  \(\square\)

### Lemma 2.2

The functions in (0.5), extended by zero for (d<2), are nondecreasing
on the nonnegative integers.

#### Proof

For (d\ge2), the assertion for (g_{12}) is immediate; its zero
extension causes no jump at (d=2).  The second function vanishes
through (d\le c).  On the positive real branch its logarithmic
derivative is

\[
 {12\over d-c}-{1\over d}-{1\over d-1}.
\]

After multiplication by the positive denominator, its numerator is

\[
 12d(d-1)-(2d-1)(d-c)
 =10d^2+(2c-11)d-c>0                                   \tag{2.3}
\]

for (d>c\ge11).  Hence the integer sequence is nondecreasing.  \(\square\)

Since (d_v(X)) is increasing in the retained-target state, Lemmas
2.1--2.2 prove (0.4) for both weights in (0.5).

## 3. Puncture blocks

For a directed cyclic word (C=(w_0,\ldots,w_{b-1})), let

\[
 \widehat E(C)=
 \{(M,I_r^C(s)):s\in\mathbb Z_b\}
 \mathbin{\dot\cup}
 \{(L,I_{r-1}^C(s)):s\in\mathbb Z_b\}.                 \tag{3.1}
\]

Its puncture at (h) is

\[
 E_h(C)=\widehat E(C)-
       \{(M,I_r^C(h)),(L,I_{r-1}^C(h))\}.                \tag{3.2}
\]

This is the usual catalogue row after rotating the word so that (h=0).
If (v\in\widehat E(C)), exactly one puncture deletes (v), so precisely
(b-1) punctures retain it.

Regard cyclic words which differ by rotation as one directed full factor.
The deck-reconstruction theorem of Appendix C.8 says that every catalogue
row determines its word, and hence its underlying full factor, uniquely.
Thus the ordered root-row pairs are partitioned by ordered full-factor
pairs.

Fix two distinct directed full factors (C,D) whose full decks both
contain (v).  There are ((b-1)^2) ordered root-retaining puncture
pairs.  If in addition

\[
                         \widehat E(C)\cap\widehat E(D)=\{v\}, \tag{3.3}
\]

then every root-retaining pair
(P_{h,k}=(E_h(C),E_k(D))) is off-root disjoint.  The forcing comparison
below does not require (3.3).  Let (S_{h,k}) be the union of the two carrier rows.
If ((h,k)) and ((h',k')) are root-retaining, then changing
the first puncture can add at most the two targets deleted at (h), and
changing the second can add at most the two targets deleted at (k).
Therefore

\[
 |S_{h',k'}-S_{h,k}|\le4,qquad
 |S_{h,k}-S_{h',k'}|\le4.                               \tag{3.4}
\]

For (g\in\{g_{12},g_c\}), the unnormalized pair weight is exactly

\[
 \mathcal W_g(h,k)
 =\mathbb E[\mathbf1_{\{S_{h,k}\subseteq X\}}g(d_v(X))]. \tag{3.5}
\]

Apply Lemma 2.1 and (3.4), on every block of positive pair weight:

\[
                         x^4\le
 {\mathcal W_g(h,k)\over\mathcal W_g(h',k')}
 \le x^{-4}.                                            \tag{3.6}
\]

Let (M=(b-1)^2), (m=|\mathcal B|), and normalize the weights within
the block.  Equation (3.6) gives

\[
 \Pi_g(\mathcal B\mid C,D)
 \le {m\max\mathcal W_g\over M\min\mathcal W_g}
 \le x^{-4}{m\over M},                                  \tag{3.7}
\]

which is (0.6).  If (m=O(b)), then (m/M=O(1/r)).  Substituting
(x\ge r^{-\alpha}) proves (0.7).

Now suppose that the block is nonclean, and choose

\[
 u\in\bigl(\widehat E(C)\cap\widehat E(D)\bigr)-\{v\}.
\]

The target (u) has a unique start in each full deck.  If
(E_h(C)\cap E_k(D)=\{v\}), at least one of the two punctures must be
the unique puncture which deletes (u).  In the ((b-1)\)-by-((b-1))
root-retaining grid, these possibilities lie on at most one row and one
column.  Consequently

\[
 \#\{(h,k):E_h(C)\cap E_k(D)=\{v\}\}\le2(b-1).          \tag{3.8}
\]

(If both deletion indices are root-retaining, the sharper count is
(2(b-1)-1).)  For (C=D), two distinct punctures leave at least
(2b-4>1) common targets, so the identical-factor block contributes no
dominant pair.  Combining (3.7)--(3.8) in every nonclean block and then
mixing the block-conditional laws proves

\[
 \Pi_g(\text{dominant and nonclean})
 \le {2x^{-4}\over b-1}.                               \tag{3.9}
\]

This proves (0.9).  Notice that the mixing step introduces no smallest
block mass and no cutoff-tail probability.

The same argument also shows that the likelihood ratio

\[
 {\mathcal W_{g_c}(h,k)\over\mathcal W_{g_{12}}(h,k)}
\]

has maximum-to-minimum ratio at most (x^{-8}) inside any block where
both pair laws are defined.
The separate pair-law bound (0.6) is sharper for deleting a set of
puncture pairs.

### Duplicate-bridge oscillation inside a clean block

For a clean block define

\[
 B^0(F,H)=\sum_{G\not\ni v}
 \mathbf1_{\{G\cap F\ne\varnothing\}}
 \mathbf1_{\{G\cap H\ne\varnothing\}}.                \tag{3.10}
\]

Changing one puncture changes at most four targets in symmetric
difference.  If the indicator in (3.10) changes when (F) is replaced by
(F') while (H\subseteq\widehat E(D)) is fixed, the affected row (G)
contains some (u\in F\mathbin\triangle F') and some
(t\in\widehat E(D)).  Cleanliness gives
(u\notin\widehat E(D)).

Appendix C.8 proves that every off-skeleton target pair has codegree
(O(D_M/r^2)).  Its only two skeleton types are a middle--lower
containment pair and a disjoint middle--middle pair, each of codegree
(O(D_M/r)).  For (r\ge3), a target outside one cyclic full deck has at most one
containment neighbor in that deck: two such cyclic intervals would have
union or intersection equal to the target and would put the target in the
deck.  A middle target outside the deck likewise has at most one disjoint
middle neighbor: two cyclic (r)-intervals inside its ((r+1))-point
complement would be consecutive, making the target their complementary
cyclic (r)-interval.  Hence

\[
 \sum_{t\in\widehat E(D)}d(u,t)
 \le 2\,O(D_M/r)+2b\,O(D_M/r^2)=O(D_M/r).              \tag{3.11}
\]

The finitely many smaller values of (r) are absorbed in the absolute
constant in (3.11).

A union bound over the at most four changed targets, followed by the
same argument on the other factor, gives

\[
 \operatorname {osc}_{h,k}B^0(E_h(C),E_k(D))=O(D_M/r). \tag{3.12}
\]

Since (D_v\ge D_M), (p_v\le1), and
(z_v=D_vq_0/p_v), multiplication by (q_0) makes (3.12)
(O(z_v/r)).  Therefore the (B^0) expectation difference between any
two probability laws supported inside this fixed clean block is
tail-mass-free and (O(z_v/(rq_0))) before multiplication by (q_0).
This controls puncture oscillation only.  The block baseline of (B^0)
can still depend on ((C,D)), and the two global pair laws can assign
different masses to different blocks.

## 4. Exact residual theorem

Let (Pi_{12}^0,Pi_c^0) denote the two pair laws restricted to the
dominant cell, and write

\[
 B^+(F,H)=\sum_{G\not\ni v}h_G(F)h_G(H),\qquad
 B^0(F,H)=\sum_{G\not\ni v}b_G(F)b_G(H).                 \tag{4.1}
\]

After the proved root-star suppression, the conditional kernel contrast
inside the dominant cell is

\[
 \boxed{
 q_0\left[
  \{\mathbb E_{\Pi_{12}^0}B^+
       -\mathbb E_{\Pi_c^0}B^+\}
 -\{\mathbb E_{\Pi_{12}^0}B^0
       -\mathbb E_{\Pi_c^0}B^0\}
 \right]_+.}                                            \tag{4.2}
\]

The full difference also contains the two cell masses and the between-cell
term of the law-of-total-covariance formula.  Thus (4.2) is not asserted to
equal the complete (Delta_{2,c}).  A uniform (o(z/q_0)) bound on the
inner contrast in (4.2), equivalently an (o(z)) bound on (4.2) itself,
is a sufficient dominant-cell input; retaining cancellation with the
between-cell term may be weaker.

The unique underlying full factors partition the pair catalogue into the
blocks of Section 3.  Equation (0.9) gives tail-mass-free negligible
global mass to dominant pairs arising in nonclean blocks; it does not by
itself give negligible mass after conditioning on the dominant cell.  In
each clean block remove (O(b)) exceptional puncture pairs.
Equations (0.6)--(0.7) prove tail-relative negligible **mass** of those
exceptions.  To turn mass deletion into (4.2), one still needs either a
kernel-weighted uniform-integrability estimate on the deleted pairs or a
pointwise (o(z/q_0)) boundary envelope.  Equation (3.12) separately
removes the within-clean-block puncture response of (B^0) at
(O(z/r)=o(z)) cost after multiplication by (q_0).  It does not remove
the between-block response of the (B^0) baselines.  On the remaining
bulk, one still needs

\[
 q_0\left[
  \Delta_{12,c} B^+-\Delta_{12,c}B^0
 \right]_+=o(z),                                        \tag{4.3}
\]

where (Delta_{12,c}Y=mathbb E_{\Pi_{12}^0}Y-
\mathbb E_{\Pi_c^0}Y).  Formula (4.3), not a cellwise favorable sign,
is the precise external bridge theorem still absent.

For the exact within-block formulation, fix a clean block
\(Q=(C,D)\), let \(\mu_{12,Q},\mu_{c,Q}\) be the two pair laws
conditioned on that block, and put

\[
 \Delta_QY=\mathbb E_{\mu_{12,Q}}Y-\mathbb E_{\mu_{c,Q}}Y.
\]

Equation (3.12) gives
\(q_0|\Delta_QB^0|=O(z_v/r)=o(z_v)\).
Consequently the exact unresolved **within-clean-block** statement is

\[
 \boxed{\sup_{Q\ {m clean}}q_0[\Delta_QB^+]_+=o(z_v),} \tag{4.4}
\]

with the same statement on any retained bulk once its deleted set has a
kernel-weighted envelope.  This is the precise sense in which only the
activity bridge remains inside a clean block.  Equation (4.4) does not
control the different global masses assigned to the blocks; those leave
an activity block-weight term and the (B^0) block-baseline regression.

The forcing lemma shows exactly what a puncture-boundary decomposition can
buy without a tail lower bound: a factor (x^{-4}) in mass, or (x^{-8})
for an unnormalized likelihood-ratio oscillation.  The boundary-codegree
argument also gives the (O(D_M/r)) duplicate oscillation within a clean
block.  Neither argument compares different underlying full cyclic
factors.  Such a comparison, or a bulk signed activity-bridge estimate
within them, is genuinely additional information.
