# Audit of the superpolynomial correlation scale against extensive reciprocal-\(C_8\) components

Date: 2026-07-26

Method: pure mathematics only.  No computation, finite search, solver, or
web input is used.

## 0. Verdict

Let

\[
 H=\lceil\sqrt{m\log m}\rceil,qquad M=m+H,qquad
 W=\binom{2m}{m},\qquad N_H=\binom{2m}{m-H},
\tag{0.1}
\]

and define the promotion-root-star parameters

\[
 R=\binom mH,qquad L=\binom MH,qquad
 p={M\over L},\qquad \theta=Rp={MN_H\over W}.
\tag{0.2}
\]

The block-factor hole theorem in
`MATH_THEOREM_PROMOTION_RING_BLOCK_FACTOR_HOLE_FLOOR_20260726.md`
is correct.  For the explicit height in (0.1),

\[
 \theta=1+o(1),qquad
 {1\over p}={R\over\theta}=(1+o(1))R,
\tag{0.3}
\]

and

\[
 \boxed{
 \log R=\log{1\over p}
  =\left({1\over2}+o(1)\right)
        \sqrt m\,(\log m)^{3/2}.}
\tag{0.4}
\]

There is one quantifier correction.  The weaker hypothesis

\[
 H=(1+o(1))\sqrt{m\log m}
\tag{0.5}
\]

does **not** by itself imply \(\theta=1+o(1)\).  Criticality must be
assumed separately, or one must take a height satisfying

\[
                         {H^2\over m}=\log m+o(1).
\tag{0.6}
\]

The ceiling choice (0.1), as well as the separately tuned critical
height, satisfies (0.6).

For the extensive reciprocal-\(C_8\) bank with

\[
 u=\lfloor\alpha m\rfloor,qquad0<\alpha<1/2,
\tag{0.7}
\]

a uniformly sampled Dyck root belongs, with probability \(1-o(1)\), to
an exact Boolean ownership component of size

\[
 \boxed{
 2^{|J(x)|}
 =\exp\left(\left({\alpha\log2\over8}+o(1)\right)m\right)
 =R^{\omega(1)}.}
\tag{0.8}
\]

The global mask menu has \(2^u=\exp((\alpha\log2+o(1))m)=R^{\omega(1)}\)
certified completed-factor assignments, and the full Catalan row set has

\[
 B=C_m=\exp((\log4+o(1))m)=R^{\omega(1)}.
\tag{0.9}
\]

These inequalities do **not** meet the block theorem by themselves.
They compare three different quantities:

* \(R\) is a number of distinct promotion roots which must be jointly
  dependent;
* \(2^{|J(x)|}\) is the number of Dyck-root vertices in one coordinate
  orbit; and
* \(2^u\) is the number of possible values of one global latent mask.

A correlation block is counted by the number of root variables it
couples, not by the number of states in its sample space.

There is a sharper exact comparison.  Let

\[
 \Gamma=\langle(\beta_j\ \gamma_j):1\le j\le u\rangle
\tag{0.10}
\]

be the disjoint-pair coordinate group of the fixed-slot bank.  For every
middle target \(D\) and every promotion root \(A\subset D\),

\[
 \boxed{
 |\Gamma A\cap\{A'\subset D:|A'|=m-H\}|
       =2^{t(A,D)}\le2^H,}
\tag{0.11}
\]

where \(t(A,D)\) is the number of generating pairs which are contained in
\(D\) and split by \(A\).  A complete rooted packet component has only
\(2m\) transported starts, so all of its direct depth-\(H\) traces meet
one provider star in at most

\[
                         \boxed{2m\,2^H=o(R).}
\tag{0.12}
\]

Quantitatively,

\[
 {2m\,2^H\over R}
 =\exp\left(-\left({1\over2}+o(1)\right)
                   \sqrt m(\log m)^{3/2}\right).
\tag{0.13}
\]

Thus a typical Boolean component is enormous in total cardinality but
vanishingly thin inside every promotion provider star.  This is the
correct reconciliation of (0.4) and (0.8).

Consequently, any attempted promotion-frame rounding in which

1. promotion roots are assigned to independently chosen fixed-slot
   \(C_8\) components,
2. each assigned frame is controlled through the component's direct
   transported coordinate-orbit traces, and
3. individual root frames have the uniform cyclic-frame marginal,

still has a linear expected middle-hole floor.  The targetwise block
parameter is \(o(1)\), so the block proof gives

\[
                         \mathbb EZ\ge(e^{-1}-o(1))W.
\tag{0.14}
\]

This conditional application is exact.  It is not a direct no-go for
ECAP: ECAP chooses ordinary packets, not one uniform frame for every
rank-\((m-H)\) promotion root, and one promotion root can occur in
several packet components.  If several components jointly control one
root, their dependency blocks must be merged; the transitive closure may
be global and then lies outside the block-product hypothesis.

Finally, full Catalan hierarchy cardinality is also an inadequate proxy.
A local Catalan closure on a semilength-\(t\) coordinate block already
has \(C_t\ge R\) at

\[
 t=\left({1\over4\log2}+o(1)\right)
       \sqrt m(\log m)^{3/2}=o(m),
\tag{0.15}
\]

but a closure supported on \(c=o(m)\) coordinates meets a fixed provider
star in at most

\[
 \max_{0\le j\le H}\binom cj=o(R).
\tag{0.16}
\]

To contain \((1-o(1))R\) roots of a target star, a fixed-support closure
must touch all but \(o(m/H)\) coordinates of that target.  Moreover a
large closure is physically selectable only when a completed-factor
ledger or an exact componentwise shore identity has been proved;
connectivity or state count alone gives no legal factor choice.

The sharp conclusion is therefore:

\[
 \boxed{
 \begin{gathered}
 \text{extensive \(C_8\) cubes exceed the required correlation scale in
 raw state count,}\\
 \text{but their direct fixed-pair components miss the required
 targetwise root-star alignment;}\\
 \text{only a globally dependent, root-scale, physically completed
 selection can evade the theorem.}
 \end{gathered}}
\tag{0.17}
\]

## 1. Audit of the block-factor theorem

Fix \(D\in\binom{[2m]}m\).  Its promotion roots are exactly

\[
 \mathcal R(D)=\{A\in\tbinom{D}{m-H}\},
 \qquad |\mathcal R(D)|=R=\binom mH.
\tag{1.1}
\]

For \(A\in\mathcal R(D)\), a uniform cyclic frame on
\(U_A=[2m]\setminus A\), \(|U_A|=M\), contains the prescribed
\(H\)-set \(D\setminus A\) as a cyclic window with probability

\[
                         p={M\over\binom MH}.
\tag{1.2}
\]

The exact ratio identity is

\[
 {R\over L}
 ={m!^2\over(m-H)!(m+H)!}
 ={N_H\over W},
\tag{1.3}
\]

so \(Rp=MN_H/W=\theta\).

Partition the promotion roots into independent blocks \(\mathcal B_j\),
with arbitrary dependence inside each block and uniform individual
marginals.  For fixed \(D\), put

\[
 r_{j,D}=|\mathcal B_j\cap\mathcal R(D)|,
 \qquad \mu_{j,D}=r_{j,D}p.
\tag{1.4}
\]

Markov's inequality gives

\[
 \Pr(\mathcal B_j\text{ supplies no witness for }D)
 \ge1-\mu_{j,D}.
\tag{1.5}
\]

If \(\mu_{j,D}\le\alpha<1\), block independence and
\(\sum_j\mu_{j,D}=\theta\) give

\[
\begin{aligned}
 \Pr(D\text{ is missed})
 &\ge\prod_j(1-\mu_{j,D})\\
 &\ge\exp\left(-{\theta\over1-\alpha}\right).
\end{aligned}
\tag{1.6}
\]

This proves the hole theorem.  The targetwise form follows by taking

\[
                    \alpha_D=p\max_jr_{j,D}.
\tag{1.7}
\]

If a fixed positive fraction of targets had \(\alpha_D\le1-\eta\),
(1.6) would give a positive linear expected hole count.  Hence a
block-product law supported on \(o(W)\)-hole selections must have, for
all but \(o(W)\) targets,

\[
 \max_j|\mathcal B_j\cap\mathcal R(D)|
 \ge(1-o(1)){1\over p}=(1-o(1))R.
\tag{1.8}
\]

The proof uses no independence inside a block and no second-moment-to-
\(L^1\) conversion.  Deleting phases or imposing tags can only remove
witnesses, so it cannot evade (1.6).

### 1.1 The critical-height qualification

Uniformly for \(H=O(\sqrt{m\log m})\),

\[
 \log{N_H\over W}
 =-{H^2\over m}
  +O\left({H^2\over m^2}+{H^4\over m^3}\right).
\tag{1.9}
\]

Therefore

\[
 \log\theta
 =\log(m+H)-{H^2\over m}+o(1)
 =\log m-{H^2\over m}+o(1).
\tag{1.10}
\]

Equation (0.5) allows, for example, a relative height error
\(\varepsilon_m\to0\) with \(\varepsilon_m\log m\to\infty\); then
\(\theta\) need not approach one.  Equation (0.6) is the correct
critical condition.  Under (0.1), the ceiling changes \(H^2/m\) by
\(o(1)\), so (0.3) holds.

Stirling gives

\[
 \log R
 =H\log{m\over H}+H
  +O\left({H^2\over m}+\log H\right),
\tag{1.11}
\]

which proves (0.4).  Since \(1/p=R/\theta\), the same asymptotic holds
for \(1/p\) at criticality.

## 2. Exact reciprocal-\(C_8\) component census

Choose \(u\le m/2\) disjoint four-coordinate slots in a Dyck word of
semilength \(m\).  Let \(J(x)\subseteq[u]\) be the slots at which root
\(x\) contains \(1100\) or \(1010\).  For every prescribed
\(T\subseteq[u]\), deletion of those blocks gives the exact census

\[
 \#\{x:T\subseteq J(x)\}=2^{|T|}C_{m-2|T|}.
\tag{2.1}
\]

Consequently the complete generating polynomial is

\[
 \boxed{
 Z_u(z):=\sum_{x\in D_m}z^{|J(x)|}
 =\sum_{h=0}^{u}\binom uh\bigl(2(z-1)\bigr)^hC_{m-2h}.}
\tag{2.2}
\]

The toggles commute and preserve \(J(x)\).  The full ownership component
through \(x\) is exactly

\[
 \mathcal K(x)=\{\tau_Tx:T\subseteq J(x)\},
 \qquad |\mathcal K(x)|=2^{|J(x)|}.
\tag{2.3}
\]

The number of Boolean ownership components is therefore exactly

\[
 \boxed{
 c_u=\sum_x2^{-|J(x)|}=Z_u(1/2)
     =\sum_{h=0}^{u}(-1)^h\binom uh C_{m-2h}.}
\tag{2.4}
\]

The number of independent component-mask bits in the fully
componentwise completed cube is

\[
\begin{aligned}
 s_u&=\sum_{\mathcal K}|J(\mathcal K)|
     =\sum_x|J(x)|2^{-|J(x)|}\\
 &=\frac12Z_u'(1/2)
   =\sum_{h=1}^{u}h(-1)^{h-1}\binom uh C_{m-2h}.
\end{aligned}
\tag{2.5}
\]

Thus there are exactly \(2^{s_u}\) legal component-mask assignments,
each producing a completed factor.  This statement counts certified
assignments; two assignments are not asserted to give distinct unlabelled
factors if an additional symmetry identifies them.  It is distinct from
the \(2^u\) **global-mask** assignments, in which every component uses
the restriction of the same mask \(A\subseteq[u]\).

For \(u=\lfloor\alpha m\rfloor\), the one- and two-slot censuses give

\[
 \mathbb E|J(x)|={\alpha m\over8}+O_\alpha(1),
 \qquad \operatorname {Var}|J(x)|=O_\alpha(m).
\tag{2.6}
\]

Hence, for a uniformly sampled Dyck root,

\[
                    |J(x)|=\left({\alpha\over8}+o(1)\right)m
\tag{2.7}
\]

with probability \(1-o(1)\).  Equations (0.4) and (2.7) prove (0.8).
This is a root-size-biased statement; a component sampled uniformly from
the set of components can have a different size distribution.

## 3. The exact provider-star intersection bound

Let \(\Gamma\) be generated by disjoint transpositions
\(P_j=\{\beta_j,\gamma_j\}\).  Fix

\[
 D\in\binom{[2m]}m,qquad
 A\in\binom D{m-H}.
\tag{3.1}
\]

For a generator pair, there are four cases.

1. If the pair is contained in \(D\) and split by \(A\), both shores
   remain subsets of \(D\).
2. If it meets \(D\) in one point and is split by \(A\), only the shore
   containing the \(D\)-point remains in \(D\).
3. If \(A\) contains both or neither point, the transposition fixes
   \(A\).
4. A pair disjoint from \(D\) also fixes \(A\).

The independent generators therefore prove the exact equality in
(0.11).  Every pair counted by \(t(A,D)\) contains a distinct element of
\(D\setminus A\), which has size \(H\).  Hence \(t(A,D)\le H\).

In a reciprocal-\(C_8\) Boolean ownership component, transport a marked
cyclic start through the exact occurrence bijections.  Coordinate
permutations commute with the depth-\(H\) trace, so that start supplies
one \(\Gamma\)-orbit of promotion roots.  There are \(2m\) marked starts
in a row.  Taking their union and applying (0.11) proves (0.12).

Now

\[
 \log R=H\log(m/H)+H+o(H\log(m/H)),
\tag{3.2}
\]

whereas

\[
                    \log(2m\,2^H)=H\log2+O(\log m).
\tag{3.3}
\]

Since \(\log(m/H)=(1/2+o(1))\log m\), (0.13) follows.

Suppose now that a proposed promotion-ring controller assigns every
promotion root to one independently sampled \(C_8\) ownership component,
and that the assigned root frame is a function of that component's legal
mask.  The assigned roots in one component form a subset of its direct
trace influence set, so (0.12) gives

\[
 p\max_{\mathcal K}
   |\mathcal B_{\mathcal K}\cap\mathcal R(D)|
 \le p(2m\,2^H)
 ={\theta\,2m\,2^H\over R}=o(1).
\tag{3.4}
\]

If the individual frame marginals are uniform, apply the targetwise
block proof with \(\alpha_D=o(1)\) to obtain (0.14).

The three italicized hypotheses are indispensable.  A promotion root may
be influenced by several packet components; merging all jointly
influencing components can create one large dependency block.  Also the
uniform distribution on \(C_8\) masks need not induce the uniform
distribution on all cyclic frames of a promotion root.  Without a proved
promotion-root controller map and its marginal law, (3.4) is a calibrated
conditional obstruction, not a direct application to ECAP.

## 4. Catalan hierarchy size versus aligned support

The Catalan asymptotic is

\[
 \log C_t=t\log4-{3\over2}\log t+O(1).
\tag{4.1}
\]

Equating its leading term to (0.4) gives (0.15).  Therefore a mesoscopic
Catalan closure can have more abstract states than the required root-star
scale.

Now suppose every transformation in one closure is supported on a fixed
coordinate set \(S\), \(|S|=c\), and fixes membership outside \(S\).
For \(A\subset D\), every orbit point \(A'\subset D\) has

\[
 A'\setminus S=A\setminus S,
 \qquad |A'\cap S|=|A\cap S|.
\tag{4.2}
\]

Writing \(d=|D\cap S|\) and \(j=|(D\setminus A)\cap S|\le H\), the
number of possibilities is at most

\[
                         \binom dj\le
               \max_{0\le i\le H}\binom ci,
\tag{4.3}
\]

which proves (0.16) whenever \(c=o(m)\).  More sharply, even in the best
case \(j=H\),

\[
 {\binom dH\over\binom mH}
 =\prod_{i=0}^{H-1}{d-i\over m-i}
 \le\left({d\over m}\right)^H.
\tag{4.4}
\]

If this ratio is \(1-o(1)\), then

\[
                         m-d=o(m/H).
\tag{4.5}
\]

Thus targetwise correlation requires almost full physical support, not
merely \(C_t\ge R\).  A hierarchy which genuinely recomputes moves across
all coordinates is not covered by (4.2); it may escape the support bound,
but then its global exact-factor completion and selectable shores must be
proved directly.

## 5. What is physically selectable

The following distinctions are exact.

1. **One global fixed-slot mask.**  For every \(A\subseteq[u]\), the
   factor \(F^A\) is a completed anchored exact factor.  Choosing one
   such \(A\) is physically legal.  A random global mask makes all root
   components dependent through one latent variable; it is not a
   small-block product law.

2. **One mask per full Boolean ownership component.**  The sealed
   cubical identity and the absence of ownership edges between components
   make an independent deterministic mask choice on each component a
   completed exact factor.  Randomizing those masks independently is a
   genuine component-product law, but its promotion-root interpretation
   must still satisfy the controller and marginal hypotheses in Section
   3.

3. **One certified variant per selected packet row.**  After infinity
   cutting, every row variant is an ordinary literal packet.  Different
   rows may be taken from different completed factors and concatenated.
   This is legal for rowwise ECAP, with middle and shadow collisions paid
   by the exact packet ledger.  It is not one common exact factor and is
   not a one-frame-per-promotion-root block law.

4. **Arbitrary rootwise factor rows.**  Selecting one local state at each
   anchored factor row is not a completed factor unless it is induced by
   a certified global mask, a certified componentwise mask, or another
   proved ledger-balanced switch scheme.

5. **A large Catalan closure.**  Connectivity, orbit size, or the
   presence of many exact factors as vertices does not authorize
   arbitrary internal shore choices.  A deterministic state is legal if
   it is itself a completed exact factor.  Mixing local states is legal
   only after a complete \(X/Y\)-ownership and port identity has been
   proved.

6. **A probability law.**  The law is an averaging device, not a physical
   factor.  To prove existence, every support point claimed as a candidate
   must be literal.  The block theorem additionally assumes uniform
   individual cyclic-frame marginals and independence between the stated
   blocks.

The global-mask lane and a genuinely global Catalan closure therefore
escape the block-size no-go in principle.  They do not solve ECAP: the
fixed-slot bank retains exact coordinate-orbit mass invariants, and no
theorem currently aligns one globally legal choice with the middle,
shallow, and annular profile requirements simultaneously.

## 6. Certified boundary

Proved:

1. the block-factor theorem, its targetwise strengthening, and the
   critical scale (0.4);
2. the necessary correction (0.6) to the height hypothesis;
3. the exact fixed-slot generating polynomial, component count, and
   component-mask count (2.2)--(2.5);
4. the comparison \(2^{|J(x)|}=R^{\omega(1)}\) for a typical root;
5. the exact provider-star intersection formula (0.11) and the
   \(2m2^H=o(R)\) component influence bound;
6. the conditional linear-hole application (0.14);
7. the fixed-support Catalan closure bound (4.3)--(4.5); and
8. the physical selectability classification in Section 5.

Not proved:

1. that ECAP induces a promotion-root block-product law;
2. that uniform \(C_8\) masks give uniform cyclic-frame marginals;
3. that every promotion root is controlled by only one Boolean component;
4. a globally completed non-coordinate Catalan closure satisfying all
   middle-through-\(H\) target ledgers; or
5. coefficient one.

Hence the superpolynomial theorem rules out local/product *root
correlation*, not small state spaces.  Extensive \(C_8\) supplies an
enormous exact menu, but its direct coordinate components remain
targetwise too thin; the only live use is through a globally dependent
completed selection or through an ECAP packet theorem proved without
misidentifying packet variants as promotion-root blocks.
