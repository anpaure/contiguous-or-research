# Fixed-decoration monotonicity: exact theorem and normalization obstruction

Date: 2026-07-25

Method: pure mathematics only. No computation or search is used.

## 0. Verdict

The proposed binary expansion is correct: after all deterministic floor,
cap, and deadline parameters have been fixed, the live priority catalogue
is a literal submultihypergraph of the initial fixed-decoration catalogue.
Thus every pair-codegree numerator only decreases.

There is, however, a decisive normalization error in the proposed
application.  In the existing hereditary recurrence,

\[
 z_t=\prod_{s<t}q_s
 \tag{0.1}
\]

is the remaining **resource density**, whereas a one-root decorated degree
has ideal retention

\[
 a_t:=\frac{d_t(v)}{d_0(v)}\simeq z_t^{\,g-1}.
 \tag{0.2}
\]

Deletion together with the stopped lower bound

\[
 d_t(v)\ge(1-\eta)z_t^{\,g-1}d_0(v)
 \tag{0.3}
\]

therefore gives only

\[
 S_{t,h}(x)\le
 (1-\eta)^{-2}z_t^{-2(g-1)}S_{0,h}(x)
 \tag{0.4}
\]

and an off-diagonal triangle factor

\[
 (1-\eta)^{-3}z_t^{-3(g-1)}.
 \tag{0.5}
\]

At the required stopping density \(z_t=1/\log m\), these factors are

\[
 (\log m)^{2(g-1)}\quad\hbox{and}\quad
 (\log m)^{3(g-1)},
 \tag{0.6}
\]

which are superpolynomial because \(g=m^{1/2+o(1)}\).  They do not close
the quadratic-variation ledger.

If one separately assumes the much stronger lower bound

\[
 d_t(v)\ge(1-\eta)z_td_0(v),
 \tag{0.7}
\]

then the proposed \(z_t^{-2}\) and \(z_t^{-3}\) conclusions are valid.
But (0.7) is not the stopped degree theorem currently available when
\(z_t\) has the meaning (0.1); it is incompatible with the ideal scale
(0.2) for \(z_t<1\) and \(g>2\).  Redefining \(z_t\) to mean degree
retention makes the deterministic statement true but makes the terminal
degree retention equal \((\log m)^{-(g-1)}\), not \(1/\log m\), so the
asymptotic obstruction remains.  Nor can one obtain (0.7) by calling
\(d_t(v)/z_t^{g-2}\) a compensated degree.  That quotient is not the
degree of \(\widehat{\mathcal H}_t\), while the normalized kernel and its
monotone numerator use the actual integer degree \(d_t(v)\).  Renaming a
compensated quantity does not change the factor in Theorem 2.1.

In particular, equation (6.3) of
MATH_ATTACK_GLOBAL_STOPPED_PRIORITY_MARTINGALE_20260725.md may be read as
a conditional stopping barrier, but not as a consequence of the current
compensator.  Corollary 3.2 of
MATH_ATTACK_DYNAMIC_QUARANTINE_CONDITIONED_PAIR_SQUARE_RECURRENCE_20260725.md
uses the actual one-root factor \(q_t^{g-1}\), whose product is (0.2).

Conversely, stopping when the degree-retention factor itself first equals
\(1/\log m\) means stopping at resource density

\[
 z_t=(1/\log m)^{1/(g-1)}
 =1-\frac{\log\log m}{g-1}
  +O\!\left(\frac{(\log\log m)^2}{g^2}\right).
 \tag{0.7a}
\]

Only \(O(\log\log m/g)=o(1)\) of the resources have then been consumed,
so this reinterpretation stops far too early for the coefficient-one
ledger.

Thus fixed-decoration monotonicity does not close hereditary pair-square
variance in the present process.  The missing gain is exactly the
two-root contraction

\[
 d_t(x,y)\lesssim z_t^{\,g-2}d_0(x,y),
 \tag{0.8}
\]

which, divided by the two one-root scales \(z_t^{g-1}\), yields one
factor \(z_t^{-1}\) per normalized codegree.  This is the conditioned
mean pair-link gate, not a consequence of binary deletion.

No coefficient-one conclusion follows from the proposed simplification.

## 1. Audit of the fixed-decoration expansion

A fixed decoration consists of

* one base grid and its tag;
* its fixed middle-owner set;
* one fixed total order of its phases; and
* the protected targets claimed by that order under the final
  deterministic floor/cap/deadline vector.

For a base grid \(P\), let \(\Sigma(P)\) be its fixed set of priority
orders.  For \(\sigma\in\Sigma(P)\), its owner set and claimed-target set
are fixed.  Let

\[
 \chi_t(P,\sigma)\in\{0,1\}
 \tag{1.1}
\]

indicate that the decoration is still feasible after history \(t\).
Tag retirement, owner consumption, target consumption, permanent
quarantine, and voluntary wasteful restriction can only change
\(\chi_t\) from one to zero.

For the deadline condition, let \(B_{t,q}(P)\) be the number of phases
whose first unavailable target has depth at most \(q\).  A fixed order is
feasible precisely when its bad phases occupy positions allowed by the
fixed inequalities

\[
 B_{t,q}(P)\le d_q\qquad(1\le q\le Q).
 \tag{1.2}
\]

The used-target set grows, so every \(B_{t,q}(P)\) is nondecreasing.
Consequently a fixed order can die but cannot be resurrected.  The
factorial formula \(\Pi_t(P)\) merely counts the surviving fixed orders:

\[
 a_t(P)=\Pi_t(P)
 =\sum_{\sigma\in\Sigma(P)}\chi_t(P,\sigma).
 \tag{1.3}
\]

Choosing a different feasible order at a later time means choosing a
different edge that was already present initially; it does not mutate an
edge.

The audited deadline enlargement is chosen once before the process and
must be absorbed into the definition of the initial decoration set.  An
adaptive relaxation \(d_q(t+1)>d_q(t)\) could add decorations and would
invalidate the argument, but no such relaxation occurs in the stated
scheme.  A rejected tentative edge creates no state change; under the
auxiliary wasteful process its neighbours are permanently deleted, which
again preserves monotonicity.

Therefore

\[
 \boxed{
 \widehat{\mathcal H}_t\subseteq\widehat{\mathcal H}_0}
 \tag{1.4}
\]

as a literal submultihypergraph, and

\[
 d_t(x,y)\le d_0(x,y)
 \tag{1.5}
\]

for every fixed pair of resource vertices.  This part of the proposal is
fully valid.

Sampling a base grid with probability proportional to \(a_t(P)\), then
sampling uniformly among its surviving priorities, is exactly uniform
sampling of one surviving fixed decorated edge within the chosen tag.
Thus there is no hidden factorial weight once the expansion is made.

## 2. Exact deterministic theorem

The theorem must be stated in terms of actual degree retention, not
resource density.

### Theorem 2.1 (deletion divided by retained degrees)

Let \(\mathcal H_t\subseteq\mathcal H_0\) be finite
multihypergraphs.  Write

\[
 d_t(x)=\#\{e\in\mathcal H_t:x\in e\},
 \qquad
 d_t(x,y)=\#\{e\in\mathcal H_t:x,y\in e\},
 \tag{2.1}
\]

and suppose that for every live vertex \(v\),

\[
 d_t(v)\ge a_vd_0(v)>0.
 \tag{2.2}
\]

For distinct live vertices put

\[
 K_t(x,y)=\frac{d_t(x,y)}{\sqrt{d_t(x)d_t(y)}}.
 \tag{2.3}
\]

Then

\[
 \boxed{
 K_t(x,y)\le(a_xa_y)^{-1/2}K_0(x,y).}
 \tag{2.4}
\]

For any set \(Y\) of live vertices,

\[
 \boxed{
 \sum_{y\in Y}K_t(x,y)^2
 \le a_x^{-1}\sum_{y\in Y}a_y^{-1}K_0(x,y)^2.}
 \tag{2.5}
\]

For the off-diagonal nonnegative triangle,

\[
 \boxed{
 \sum_{\substack{y,z\in Y\\y\ne z}}
 K_t(x,y)K_t(y,z)K_t(z,x)
 \le
 \sum_{\substack{y,z\in Y\\y\ne z}}
 \frac{K_0(x,y)K_0(y,z)K_0(z,x)}{a_xa_ya_z}.}
 \tag{2.6}
\]

If \(a_v\ge a\) for every relevant vertex, (2.5)--(2.6) have factors
\(a^{-2}\) and \(a^{-3}\).  If the full triangle permits \(y=z\), its
diagonal part is the pair-square and has the sharper factor \(a^{-2}\):

\[
 \mathfrak T_t(x)
 \le a^{-2}S_0(x)+a^{-3}\mathfrak B_0(x).
 \tag{2.7}
\]

#### Proof

Subhypergraph containment gives
\(d_t(x,y)\le d_0(x,y)\).  Dividing by the two lower degree bounds in
(2.2) proves (2.4).  Squaring and summing proves (2.5).  Multiplying
(2.4) for \((x,y),(y,z),(z,x)\) cancels the square roots and gives the
factor \((a_xa_ya_z)^{-1}\), proving (2.6).  All summands are
nonnegative.  Equation (2.7) follows because \(K_t(y,y)=1\) on the
diagonal. \(\square\)

The proof applies verbatim to exposed/claimed mixed kernels after making
a separate vertex copy for every occurrence type and using its actual
occurrence degree.  A stopped lower bound is required for every type
appearing in the cyclic product.

### 2.1 The exponents are sharp

Under only deletion and (2.2), neither exponent can be improved.  Fix
rational \(0<a<1\), and choose integers \(D,c\) such that \(aD\) is an
integer and \(2c\le aD\).  Form a multigraph with live vertices
\(x,y,z\), with \(c\) parallel copies of each of \(xy,yz,zx\).  Pad each
of \(x,y,z\) to degree \(D\) using \(D-2c\) edges to private degree-one
vertices.  In the residual graph retain all \(3c\) core edges and exactly
\(aD-2c\) private edges at each live vertex.
Then

\[
 d_0(x)=d_0(y)=d_0(z)=D,\qquad
 d_t(x)=d_t(y)=d_t(z)=aD,
 \tag{2.8}
\]

while

\[
 d_t(x,y)=d_0(x,y)=c
 \tag{2.9}
\]

and similarly for the other two pairs.  Hence every normalized core
entry is multiplied by exactly \(a^{-1}\), every core pair-square by
\(a^{-2}\), and the core triangle by \(a^{-3}\).  Deleted private
vertices are simply omitted from the live set.  Arbitrary real \(a\)
follows by rational approximation.

This also proves a structural no-go: no argument using only
\(\mathcal H_t\subseteq\mathcal H_0\) and one-root degree lower bounds
can recover an additional numerator contraction.

## 3. Applying the theorem with the current PBBS variables

For one bite, the established ideal one-root and two-root contractions
are

\[
 \rho_{1,s}=q_s^{\,g-1},
 \qquad
 \rho_{2,s}=q_s^{\,g-2}.
 \tag{3.1}
\]

After \(t\) bites, put

\[
 z_t=\prod_{s<t}q_s.
 \tag{3.2}
\]

The stopped one-root lower bound therefore has reference

\[
 \prod_{s<t}\rho_{1,s}=z_t^{\,g-1},
 \tag{3.3}
\]

up to the accumulated scalar error.  Inserting

\[
 a=(1-\eta)z_t^{\,g-1}
 \tag{3.4}
\]

into Theorem 2.1 gives exactly (0.4)--(0.5), not the desired powers.

Using the raw estimates

\[
 S_{0,0}(x)=O(m^{-2}),
 \qquad
 \sum_hS_{0,h}(x)=O(m^{-1}),
 \qquad
 \mathfrak T_0(x)=m^{-1+o(1)},
 \tag{3.5}
\]

monotonicity alone yields at terminal density \(z=1/\log m\)

\[
 \sum_hS_{t,h}(x)
 \le
 m^{-1+o(1)}(\log m)^{2(g-1)},
 \tag{3.6}
\]

and, even using the crude full-triangle form,

\[
 \mathfrak T_t(x)
 \le
 m^{-1+o(1)}(\log m)^{3(g-1)}.
 \tag{3.7}
\]

These are valid upper bounds but are asymptotically useless.  Indeed

\[
 (\log m)^{c(g-1)}
 =\exp\bigl((c+o(1))g\log\log m\bigr)
 =m^{m^{1/2+o(1)}}
 \tag{3.8}
\]

for either fixed \(c=2\) or \(c=3\).  More precisely, the exponent of
\(m\) in the middle expression is
\((c+o(1))g\log\log m/\log m=m^{1/2+o(1)}\).

Accordingly the prospective all-stratum monotonicity bound for the
quadratic-variation coefficient is

\[
 Qm^{-1+o(1)}(\log m)^{3(g-1)}\log\log m,
 \tag{3.9}
\]

which has logarithm

\[
 (3+o(1))g\log\log m
 \tag{3.10}
\]

and in particular does not tend to zero.  The global stopped-Doob theorem
cannot be fed this bound.

Using the time profile instead of its terminal supremum does not repair
the estimate.  With effective time \(u=-\log z\), its triangle part is
bounded only by

\[
 m^{-1+o(1)}
 \int_0^{\log\log m}e^{3(g-1)u}\,du
 =
 \frac{m^{-1+o(1)}}{3(g-1)}
 \left((\log m)^{3(g-1)}-1\right).
 \tag{3.11}
\]

Multiplication by \(Q=m^{1/2+o(1)}\) changes only a polynomial prefactor;
the terminal exponential in \(g\log\log m\) remains.

## 4. Why the desired \(z^{-2}\) appears only with a two-root theorem

Suppose in addition to the one-root scale one proves

\[
 d_t(x,y)\le(1+o(1))z_t^{\,g-2}d_0(x,y)
 \tag{4.1}
\]

in the pointwise or weighted form needed by the block.  Combining (4.1)
with

\[
 d_t(x),d_t(y)\ge(1-o(1))z_t^{\,g-1}d_0(x),
                    (1-o(1))z_t^{\,g-1}d_0(y)
 \tag{4.2}
\]

gives

\[
 K_t(x,y)\le(1+o(1))z_t^{-1}K_0(x,y),
 \tag{4.3}
\]

and hence the desired \(z_t^{-2}\) pair-square inflation.  Three such
factors give \(z_t^{-3}\) for the off-diagonal triangle.

The exponent is the exact quotient

\[
 \frac{z_t^{\,g-2}}{z_t^{\,g-1}}=z_t^{-1}.
 \tag{4.4}
\]

Deleting fixed decorations supplies only the numerator bound
\(d_t(x,y)\le d_0(x,y)\), replacing \(z_t^{g-2}\) in (4.4) by one and
losing \(z_t^{-(g-2)}\).  Thus (4.1), or its weighted conditioned
mean-link version, is exactly the information missing from monotonicity.

## 5. Conditional version of the proposed closure

If a new process really supplies the stronger barrier

\[
 d_t(v)\ge(1-\eta)z_td_0(v)
 \tag{5.1}
\]

with the same \(z_t\ge1/\log m\), then Theorem 2.1 does prove

\[
 S_{t,h}(x)\le(1-\eta)^{-2}z_t^{-2}S_{0,h}(x)
 \tag{5.2}
\]

and

\[
 \mathfrak T_t(x)
 \le(1-\eta)^{-2}z_t^{-2}S_0(x)
 +(1-\eta)^{-3}z_t^{-3}\mathfrak B_0(x).
 \tag{5.3}
\]

For \(z_t\ge1/\log m\), \(g=m^{1/2+o(1)}\), and the raw triangle
\(m^{-1+o(1)}\), this is still \(m^{-1+o(1)}\).  Summing through
\(Q=m^{1/2+o(1)}\) strata and \(O(\log\log m)\) effective time gives

\[
 B_m=m^{-1/2+o(1)}.
 \tag{5.4}
\]

The weighted stopped-Doob theorem with
\(\eta=B_m^{1/4}=m^{-1/8+o(1)}\) would then charge martingale exits by

\[
 O(B_m/\eta^2)W=O(B_m^{1/2}W)=o(W),
 \tag{5.5}
\]

leaving predictable mean-spread as the scalar gate.

This is a correct conditional theorem.  It is not an application to the
current recurrence because (5.1) differs from (3.3) by the factor

\[
 z_t^{-(g-2)}.
 \tag{5.6}
\]

At \(z_t=1/\log m\), (5.6) is
\((\log m)^{g-2}\), so the difference cannot be absorbed into the stopped
error \(1\pm\eta\).

## 6. Priority losses, quarantine, and what remains

For ordinary resource conflicts, if \(e,e'\) are independent surviving
decorations in a fibre and \(E\) is the sampled decorated edge, then

\[
 \Pr(e\sim E\mid E)^2
 =\Pr(e\sim E,\ e'\sim E\mid E).
 \tag{6.1}
\]

Averaging (6.1) is exactly the current common-link count.  Hence the
conditional theorem in Section 5 really would close the scalar degree
quadratic variation; factorial priority weights introduce no further
obstruction.

Dynamic bad-grid quarantine remains deletion-only, so it preserves
Theorem 2.1.  Its trigger is not an ordinary shared-resource relation and
must be charged separately in quadratic variation.  The existing
\(m^{-4+o(1)}\) total-loss ledger makes that term negligible outside
weighted \(o(W)\) fibres.  Direct root consumption must likewise be
excluded by freezing immediately before the consuming jump or by using
the exact root-survival conditional law.

For the actual resource-density normalization, the surviving statements
are therefore:

1. scalar predictable mean-spread, needed to establish the one-root scale
   \(z_t^{g-1}\);
2. conditioned two-root mean contraction (4.1), or a weighted substitute
   strong enough to recover (4.3); and
3. the corresponding common-link/four-walk control if (4.1) is available
   only in expectation rather than pathwise.

The fixed-decoration observation proves binary deletion but does not
remove the second item.  The exact residual no-go is that deletion plus
one-root degree stopping has sharp inflation in the actual retained-degree
factor \(a_t\), and \(a_t=z_t^{g-1}\) in the current chronology.
