# Context-phased compiler: the all-order Hall audit and a literal parent-tag cut

Date: 2026-07-26

Method: pure mathematics only. No computation, search, solver, or web
input is used.

Throughout,

\[
                         W=\binom{2m}{m}.
\]

## 0. Verdict

The logarithmic blind-spectrum estimate does not imply the all-order
configuration Hall inequality.  Complete affine batching gives exact
one-target marginals, but those marginals are weighted
compatible-source loads; their total mass is large enough while their
pointwise lower tail may still be linear.

This distinction is witnessed by a literal context-phased atlas.  There
is a legal carrier-confined rank-twisted packet atlas with

\[
                         G=W-e^{-\Omega(m)}W
\]

retained middle owners, packet dimension \(R=\Theta(m)\), and the exact
context-phased \(C_{2R}\)-factor in every packet, such that all active
directions lie in one coordinate carrier

\[
                         E\subset[2m],\qquad
                         |E|={m\over2}+O(\log m).
\]

Every local conclusion survives:

1. exact owner factorhood;
2. \(o(W/H)\) cycles when \(H=o(m)\);
3. two-sign trace injectivity through every \(q\le H\);
4. the complete logarithmic blind-spectrum bound; and
5. arbitrary affine compiler conjugation and arbitrary correlation
   between parent choices.

Nevertheless, at every fixed Gaussian depth

\[
                         q=A\sqrt m+O(1),\qquad A>0,
\]

the exterior coordinate tag \(X\cap E^c\) is invariant.  A
positive-density band \(\mathcal B_q\) of lower targets satisfies, for
every legal global option,

\[
 \boxed{
 \#\{\hbox{covered targets in }\mathcal B_q\}
 \le(e^{-A^2}+o(1))|\mathcal B_q|.}                 \tag{0.1}
\]

Moreover

\[
                         |\mathcal B_q|
                         \ge(c_A-o(1))\binom{2m}{m-q}
                         =\Theta_A(W)               \tag{0.2}
\]

for a constant \(c_A>0\).  Thus

\[
 \boxed{
 \mathfrak H_q^-
 \ge(c_A-o(1))(1-e^{-A^2})\binom{2m}{m-q}
 =\Omega_A(W).}                                    \tag{0.3}
\]

Taking the literal target weight \(y=\mathbf1_{\mathcal B_q}\) violates
the reserve-\(o(W)\) all-order configuration Hall inequality by
\(\Omega_A(W)\).  This is a cross-parent cut: every packet/spectator
fibre is locked to one exterior tag, and no correlated law can transfer
owner capacity between tags.

Therefore the requested dichotomy closes on the negative side for the
local hypotheses presently available.  The context-phased compiler and
its logarithmic blind bound do not force all-order Hall.  They can only
participate in a positive theorem after one adds a genuinely
projection-free parent/frame hypothesis.

The result is not a universal obstruction to every moving-frame atlas.
It is a sharp obstruction to deriving coefficient one from the
context-phased compiler, rank-twisted owner factorhood, and local
blind-spectrum control alone.

## 1. Exact all-order configuration Hall inequality

Let \(\mathcal G\) be the family of owner-disjoint choice groups after
every shared frame, slab, or affine variable has been placed in one
common group.  For \(g\in\mathcal G\), let \(\Omega_g\) be its legal
option set and let

\[
                         J_g^\omega\subseteq\mathcal V
                                                               \tag{1.1}
\]

be the complete typed literal target support of option \(\omega\),
simultaneously at every protected depth and both signs.

For an integer reserve \(s\), put

\[
 \rho_s(y)=\hbox{the sum of the \(s\) largest coordinates of }y.
                                                               \tag{1.2}
\]

The fractional multiple-choice cover with reserve \(s\) is

\[
\begin{aligned}
 x_{g\omega}&\ge0,&
 \sum_{\omega\in\Omega_g}x_{g\omega}&=1,\\
 0\le z_v&\le1,&
 \sum_vz_v&\le s,\\
 \sum_{g,\omega}x_{g\omega}
       \mathbf1_{\{v\in J_g^\omega\}}+z_v&\ge1
                         &&(v\in\mathcal V).          \tag{1.3}
\end{aligned}
\]

Its exact weighted Hall inequalities are

\[
 \boxed{
 \sum_g\max_{\omega\in\Omega_g}
          \sum_{v\in J_g^\omega}y_v
       +\rho_s(y)
 \ge\sum_vy_v
 \qquad(y\ge0).}                                   \tag{1.4}
\]

Necessity follows by multiplying (1.3) by \(y_v\), summing, and
maximizing separately in each group.  Sufficiency is the separating
hyperplane theorem applied to the Minkowski sum of the group
configuration polytopes, the reserve polytope

\[
 \{z\in[0,1]^{\mathcal V}:\sum_vz_v\le s\},
\]

and the downward orthant.  The downward orthant forces every separating
normal to satisfy \(y\ge0\), and the support function of the reserve
polytope is exactly \(\rho_s(y)\).
Therefore (1.4) is all-order: the maximum contains one whole legal
common-depth configuration, not a moment or a bounded target tuple.

In particular, to refute reserve \(s=o(W)\), it suffices to find one
literal weight \(y\) for which the reverse gap is \(\Omega(W)\).

There is a useful statewise specialization.

### Lemma 1.1 (parent-tag Hall cut)

Let \(\tau:\mathcal V\to\mathcal A\) be a target-tag map.  Suppose every
owner occurrence has a tag in \(\mathcal A\), every legal option preserves
that tag, and \(C_a\) is the total number of owner occurrences carrying
tag \(a\).  Put

\[
                         D_a=|\tau^{-1}(a)|.
\]

For any tag set \(B\subseteq\mathcal A\), the literal weight

\[
                         y_v=\mathbf1_{\{\tau(v)\in B\}}
\]

satisfies

\[
 \sum_g\max_{\omega\in\Omega_g}
       \sum_{v\in J_g^\omega}y_v
                         \le\sum_{a\in B}C_a.        \tag{1.5}
\]

Consequently, if

\[
                         \sum_{a\in B}(D_a-C_a)=\Omega(W),       \tag{1.6}
\]

then (1.4) fails for every \(s=o(W)\).

#### Proof

Choose in each group an option attaining the maximum in (1.5).  These
options form one legal global state because all shared variables are
already inside common groups.  Every emitted occurrence of a target
tagged \(a\) comes from an owner occurrence tagged \(a\), and each owner
emits once at the typed layer supporting \(y\).  Thus the total number of
group incidences with tags in \(B\) is at most
\(\sum_{a\in B}C_a\).  This proves (1.5).  Since
\(\sum_vy_v=\sum_{a\in B}D_a\) and \(\rho_s(y)\le s\), (1.6) violates
(1.4). \(\square\)

This lemma already permits arbitrary dependence between group options:
it is a deterministic capacity statement for every global state.

## 2. What affine batching actually proves

Fix one physical packet \(P\cong Q_R\), one sign, and one depth \(q\).
The context-phased compiler has exactly \(2^R\) distinct physical
\(q\)-faces.  The affine cube group

\[
                         \Gamma_R=Q_R\rtimes S_R
\]

is transitive on the

\[
                         \binom Rq2^{R-q}
\]

physical \(q\)-faces.  Hence every packet face \(f\) has exact affine
inclusion probability

\[
 {2^R\over\binom Rq2^{R-q}}
                         ={2^q\over\binom Rq}.       \tag{2.1}
\]

One affine label is used at all depths and both signs, so (2.1) holds
simultaneously as a family of first-marginal identities.

For a global literal target \(T\), however, one must sum (2.1) only over
parent cells in which \(T\) is a physical packet face.  The result is
the source-normalized compatible load

\[
 \Lambda_q^\epsilon(T)
 =\sum_{\substack{X\sim T\\X\ {\rm retained}}}
       {1\over\binom{S(X)}q}.                       \tag{2.2}
\]

It obeys the conservation identity

\[
                         \sum_T\Lambda_q^\epsilon(T)=G,         \tag{2.3}
\]

but (2.3) does not imply
\(\Lambda_q^\epsilon(T)\ge1\) pointwise or outside \(o(W)\) targets.
At Gaussian depth its average is

\[
 {G\over N_q}=e^{A^2+o(1)},\qquad
 N_q=\binom{2m}{m-q},                               \tag{2.4}
\]

so a positive-density low-load region can coexist with conservation by
overloading its complement.

This is the exact gap in the attempted positive argument.  The
context-phased replacement preserves (2.1), but first marginals alone
do not prove (1.4).

## 3. A legal carrier-confined context-phased atlas

Use logarithmic rank-twisted macroblocks and let \(E\) be a union of
complete macroblocks with

\[
                         e:=|E|={m\over2}+O(\log m).             \tag{3.1}
\]

Choose

\[
                         R=8\cdot2^r
\]

maximal subject to \(R\le m/256\).  Then

\[
                         {m\over512}<R\le{m\over256},            \tag{3.2}
\]

and \(R=2n\) with \(n=4\cdot2^r\), exactly the admissible scale of the
context-phased recursion.

The rank-twisted product enumerator shows that, under the unconditioned
Boolean-cube measure, the number \(S_E\) of split matching axes belonging
to \(E\) has the exact law

\[
                         S_E\sim{\rm Bin}(e/2,1/2).              \tag{3.3}
\]

Thus \(\mathbb ES_E=m/8+O(\log m)\), whereas
\(16R\le m/16\).  Chernoff's inequality gives
\(\Pr(S_E<16R)=e^{-\Omega(m)}\).  Since

\[
                         \Pr(|X|=m)=\Theta(m^{-1/2}),
\]

conditioning on the middle layer changes this bound by only a polynomial
factor:

\[
 \Pr(S_E<16R\mid |X|=m)
 \le{\Pr(S_E<16R)\over\Pr(|X|=m)}
                         =e^{-\Omega(m)}.            \tag{3.4}
\]

Consequently the middle owners lying in product cells with fewer than
\(16R\) such axes have total mass

\[
                         e^{-\Omega(m)}W.            \tag{3.5}
\]

Discard those cells.  In every retained cell select the required packet
directions only among the split axes in \(E\), freeze all other
orientations, and partition the cell into parallel physical
\(Q_R\)-packets.  Install the context-phased factor in every packet.

The packets partition the retained owners, so owner factorhood is exact.
The context-phased theorem gives \(C_{2R}\)-components and literal
two-sign trace injectivity through \(R/4-1\).  Thus every
\(H=o(m)\) is protected for all large \(m\).  The total number of cycles
is

\[
                         {G\over2R}=O(W/m)=o(W/H).               \tag{3.6}
\]

The omitted mass in (3.5) is \(o(W/H)\).

All packet moves change only coordinates of \(E\).  Consequently every
owner occurrence \(X\), every time along its compiler cycle, and every
affine conjugate allowed inside the selected packet obey

\[
                         P^i(X)\cap E^c=X\cap E^c.               \tag{3.7}
\]

Equation (3.7) is statewise.  It is therefore unaffected by dependent
or adversarial choices of compiler options across different parents.

## 4. The exterior-tag capacity calculation

Fix \(q=A\sqrt m+O(1)\), \(A>0\).  For
\(Y\subseteq E^c\), define

\[
\begin{aligned}
 \mathcal O_Y
 &=\{X\in\tbinom{[2m]}m:X\cap E^c=Y\},\\
 \mathcal T_Y
 &=\{T\in\tbinom{[2m]}{m-q}:T\cap E^c=Y\}.          \tag{4.1}
\end{aligned}
\]

Put \(t=m-q-|Y|\).  Then exactly

\[
                         |\mathcal T_Y|=\binom et,\qquad
                         |\mathcal O_Y|=\binom e{t+q}.           \tag{4.2}
\]

By (3.7), every emitted lower target in \(\mathcal T_Y\) must be emitted
by an owner in \(\mathcal O_Y\).  Every owner emits one target at this
depth.  Hence, for every simultaneous choice of all group options,

\[
 \#\{\hbox{covered targets in }\mathcal T_Y\}
                         \le|\mathcal O_Y|.           \tag{4.3}
\]

This remains true if the left side is replaced by the sum of group
incidences rather than the size of their union, because there is still
only one emitted occurrence per retained owner.

Write

\[
                         t={e\over2}-{q\over4}+x
\]

and retain the exterior tags for which

\[
                         |x|\le {q\over8}.            \tag{4.4}
\]

Uniformly in this band, the central binomial expansion gives

\[
\begin{aligned}
 \log {|\mathcal O_Y|\over|\mathcal T_Y|}
 &=
 \log{\binom e{e/2+3q/4+x}
              \over
              \binom e{e/2-q/4+x}}\\
 &=-{2\over e}
   \left[\left({3q\over4}+x\right)^2
          -\left(-{q\over4}+x\right)^2\right]+o(1)\\
 &=-{2\over e}\left({q^2\over2}+2qx\right)+o(1)\\
 &\le-{q^2\over2e}+o(1)
  =-A^2+o(1).                                      \tag{4.5}
\end{aligned}
\]

The error in (3.1) changes the last expression by \(o(1)\).

Let \(\mathcal B_q\) be the disjoint union of all
\(\mathcal T_Y\) satisfying (4.4).  For a uniform rank-\((m-q)\)
target, \(t=|T\cap E|\) is hypergeometric, with mean

\[
                         {e(m-q)\over2m}
                         ={e\over2}-{q\over4}+o(\sqrt m)
\]

and variance \(\Theta(m)\).  The local central limit theorem therefore
gives a constant \(c_A>0\) such that

\[
                         |\mathcal B_q|
 \ge(c_A-o(1))N_q.                                  \tag{4.6}
\]

Summing (4.3) and (4.5) over these disjoint exterior fibres proves
(0.1)--(0.3).

## 5. Literal violation of all-order Hall

Support the target weight on the single lower typed layer and put

\[
                         y_T=\mathbf1_{\{T\in\mathcal B_q\}}.   \tag{5.1}
\]

Because all genuinely shared variables were placed in common choice
groups, independently maximizing each group in (1.4) still produces one
legal global option.  Equations (4.3)--(4.5) therefore give

\[
 \sum_g\max_{\omega\in\Omega_g}
          \sum_{T\in J_g^\omega}y_T
 \le(e^{-A^2}+o(1))|\mathcal B_q|.                  \tag{5.2}
\]

For every reserve \(s=o(W)\),

\[
                         \rho_s(y)\le s=o(W).        \tag{5.3}
\]

Using (4.6), the right side of the Hall inequality exceeds the left side
by

\[
 (1-e^{-A^2}-o(1))|\mathcal B_q|-o(W)
                         =\Omega_A(W).               \tag{5.4}
\]

Thus (1.4) fails.  This is stronger than failure of integral rounding:
even the fractional all-order configuration cover has a linear
deficiency.

Complementation gives the corresponding upper cut.  A weight supported
on one sign and one depth is already a valid all-depth dual weight, so
stacking the other layers cannot repair the violation.

## 6. Why the logarithmic blind theorem does not see the cut

For a protected window visiting \(d=\Theta(q)\) bottom leaves, the
context-phased compiler has residual blind subgroup

\[
                         \mathcal B_A=\bigoplus_jE(C_j)
\]

and exact weight enumerator

\[
 W_A(z)=\prod_j{(1+z)^{s_j}+(1-z)^{s_j}\over2}.     \tag{6.1}
\]

For every \(t\le c\log m\),

\[
 { [z^{2t}]W_A(z)\over\binom{R-q}{2t}}
                         \le\left({Ct\over d}\right)^t.         \tag{6.2}
\]

At \(d=\Theta(\sqrt m)\), the top logarithmic strength is
\(\exp[-\Omega((\log m)^2)]\), and the sum of all normalized
nontrivial coefficients through that range is \(O(1/d)=o(1)\).

None of (6.1)--(6.2) changes (3.7).  The blind spectrum concerns context
translations inside the active packet carrier \(E\); the Hall cut is
the exact macroscopic quotient

\[
                         X\longmapsto X\cap E^c.     \tag{6.3}
\]

Thus the obstruction is not a residual blind atom of bounded or
logarithmic strength.  It is a statewise parent-tag conservation law.
No moment calculation is used in (4.2)--(5.4).

This also identifies the logical role of the logarithmic theorem:
it closes the former local higher-atom objection, thereby forcing any
remaining obstruction to live in the cross-parent projection.  The
exterior-tag cut is exactly such an obstruction.

## 7. Algebraic parent-tag resolution and its exact missing hypothesis

For a projection-free atlas, a natural correlated law is a common
translation.  Let \(Z\) be a finite abelian translation group, choose
base labels \(\gamma_g\), and set

\[
                         \omega_g(z)=\gamma_g+z,\qquad z\in Z.
                                                               \tag{7.1}
\]

For a target \(v\), define its provider set

\[
                         S_g(v)=
 \{z\in Z:v\in J_g^{\omega_g(z)}\}.                 \tag{7.2}
\]

If \(\mathfrak H(z)\) is the number of uncovered targets, then exactly

\[
 \boxed{
 {1\over|Z|}\sum_{z\in Z}\mathfrak H(z)
 =\sum_v\left(1-
       {\left|\bigcup_gS_g(v)\right|\over|Z|}\right).}          \tag{7.3}
\]

Hence a common-shift law succeeds if and only if its aggregate
provider-union deficit is \(o(W|Z|)\).  This is an all-order set-union
criterion, not an inclusion-exclusion truncation.

For the carrier atlas, (3.7) makes every \(S_g(v)\) empty unless the
spectator fibre supporting \(g\) has the same exterior tag as \(v\).
Summing the provider capacity inside the band (4.4) reproduces (5.2), so
no choice of the base offsets \(\gamma_g\) can satisfy (7.3).

A positive theorem must therefore alter parent frames so that, for every
positive-density coordinate cut, owner mass can cross its tags.  Even
that projection-free condition is only necessary: after it is proved,
one must still establish the literal provider-union inequality (7.3) or
the full configuration Hall inequalities (1.4).

## 8. Certified boundary

Proved:

1. the exact all-order fractional Hall criterion (1.4);
2. the exact correction that affine batching gives (2.2)--(2.3), not a
   pointwise lower bound;
3. a legal context-phased carrier atlas satisfying every current local
   compiler and blind-spectrum gate;
4. the literal exterior-tag capacity cut (0.1);
5. an \(\Omega_A(W)\) lower bound on missing shadows at one Gaussian
   depth;
6. an explicit positive-density violation of all-order configuration
   Hall; and
7. the exact correlated common-shift union identity (7.3).

Not proved:

1. an obstruction to every genuinely moving-frame context-phased atlas;
2. a projection-free parent-frame construction;
3. the provider-union bound (7.3) for such a construction; or
4. coefficient one.

The exact conclusion is therefore a no-go for the proposed local-to-global
implication, not for all possible frame-changing compilers.
