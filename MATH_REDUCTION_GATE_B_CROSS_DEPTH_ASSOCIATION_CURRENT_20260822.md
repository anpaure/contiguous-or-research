# Gate B: the cross-depth association current

**Date:** 2026-08-22  
**Status:** unconditional pathwise reduction and exact information
obstruction.  The all-depth second-moment hypothesis is equivalent, after
the first-moment normalization, to an `Omega(1/xi)` association factor for
two independently hole-Palm sampled targets.  This factor has an exact
joint first-blocker telescope.  It is not a consequence of the marginal
relative-protection telescope.  Moreover, independent row scrambling at
the different depths preserves every fixed-depth incidence statistic while
reducing the all-depth second moment to at most `mu+mu^2`.  Consequently a
genuinely joint cross-depth theorem is necessary.  The note does not prove
that theorem for the stopped punctured catalogue.  Section 6 identifies
the weakest aggregate four-root version: an ordered cross-depth
coincidence sum.  It is equivalent, up to constants in the live range, to
the missing scalar second moment.

## 1. Terminal catalogue and the three scalar hypotheses

Put

\[
 b=2r+1,\qquad A={b\choose r},\qquad B=A/b,
 \qquad Q=\left\lceil\sqrt{b\log b}\right\rceil .       \tag{1.1}
\]

Assume `b` is sufficiently large that `Q<=r-1`.

Fix one realized good stopped trajectory and its nonempty terminal labelled
survivor catalogue `C`, of size `Z`.  Let

\[
 \mathcal H=\bigsqcup_{q=1}^Q
       (\mathcal H_q^-\sqcup\mathcal H_q^+),
 \qquad |\mathcal H|=\xi A Q.                            \tag{1.2}
\]

The family may be any one of the residual hole families produced by a
subsequent deterministic peeling rule.  All assertions below are therefore
deterministic after the stopped trajectory and the peeling stage have been
fixed.

For a tagged target `T`, let

\[
 I_T(F)={\bf1}_{\{T\text{ is a full-row window of }F\}},
 \qquad p_T={1\over Z}\sum_{F\in\mathcal C}I_T(F),       \tag{1.3}
\]

and for two tagged targets put

\[
 p_{TU}={1\over Z}\sum_{F\in\mathcal C}I_T(F)I_U(F).
                                                                    \tag{1.4}
\]

For a uniform terminal survivor `F`, define

\[
 z_q(F)={1\over2b}\sum_{T\in\mathcal H_q^-\sqcup
                                      \mathcal H_q^+}I_T(F),
 \qquad \Phi(F)=\sum_{q=1}^Qz_q(F).                    \tag{1.5}
\]

Thus `0<=z_q<=1` and `0<=Phi<=Q`.  Write

\[
 \mu=\mathbb E\Phi,
 \qquad J=\mathbb E\Phi^2,
 \qquad \bar p={1\over|\mathcal H|}\sum_{T\in\mathcal H}p_T.
                                                                    \tag{1.6}
\]

Reversing finite sums gives the exact normalizations

\[
 \boxed{\mu={1\over2b}\sum_Tp_T,
 \qquad J={1\over4b^2}\sum_{T,U}p_{TU},
 \qquad \bar p={2b\mu\over\xi A Q}.}                  \tag{1.7}
\]

Suppose the proposed scalar hypotheses hold with fixed positive constants:

\[
 \max_Tp_T\le R\bar p,\qquad
 \mu\le C_1\xi Q,\qquad J\ge c_2\xi Q^2.             \tag{1.8}
\]

Since `Phi^2<=Q Phi`, (1.8) also forces

\[
 \boxed{c_2\xi Q\le\mu\le C_1\xi Q,
 \qquad {2c_2b\over A}\le\bar p\le{2C_1b\over A},
 \qquad p_T\le {2RC_1b\over A}.}                       \tag{1.9}
\]

In particular the first and third scalars put the average terminal hole
degree at the complete-catalogue scale and cap every terminal hole degree
by a fixed multiple of that scale.  They do not supply the second moment.

## 2. The missing scalar is exactly pair association

Assume `mu>0` and define the terminal hole-Palm law

\[
 \omega(T)={p_T\over2b\mu}.                              \tag{2.1}
\]

For `p_Tp_U>0`, put

\[
 \mathcal R(T,U)={p_{TU}\over p_Tp_U},                  \tag{2.2}
\]

and put (mathcal R(T,U)=0) when `p_Tp_U=0`.  Values on zero
`omega tensor omega` mass are immaterial.

### Theorem 2.1 (exact association identity)

For independent `T,U` with law `omega`,

\[
 \boxed{
 \mathbb E_{\omega\otimes\omega}\mathcal R(T,U)
 ={J\over\mu^2}.}                                      \tag{2.3}
\]

Consequently (1.8) implies

\[
 \boxed{
 \mathbb E_{\omega\otimes\omega}\mathcal R(T,U)
 \ge {c_2\over C_1^2\xi}.}                            \tag{2.4}
\]

#### Proof

Substitution of (2.1)--(2.2), followed by (1.7), gives

\[
 \sum_{T,U}{p_Tp_U\over(2b\mu)^2}{p_{TU}\over p_Tp_U}
 ={\sum_{T,U}p_{TU}\over4b^2\mu^2}={J\over\mu^2}.
\]

Now use the last two inequalities in (1.8). `square`

Thus the second-moment target is not another marginal degree estimate.  It
asks two independently target-Palm sampled holes to occur in one survivor
row with a likelihood ratio of order `1/xi` on average.

There is also a strictly cross-depth form.  Put `m_q=E z_q`.  Since
`z_q^2<=z_q`, (1.8) gives

\[
\begin{aligned}
 \sum_{q\ne d}\operatorname {Cov}(z_q,z_d)
 &=J-\sum_q\mathbb Ez_q^2
       -\left(\mu^2-\sum_qm_q^2\right)\\
 &\ge c_2\xi Q^2-C_1\xi Q-C_1^2\xi^2Q^2.             \tag{2.5}
\end{aligned}
\]

Hence, whenever

\[
 Q\ge {4C_1\over c_2},\qquad
 \xi\le {c_2\over4C_1^2},                             \tag{2.6}
\]

one necessarily has

\[
 \boxed{
 \sum_{q\ne d}\operatorname {Cov}(z_q,z_d)
 \ge {c_2\over2}\xi Q^2.}                            \tag{2.7}
\]

The diagonal depth terms are only `O(xi Q)` and the product of the means is
only `O(xi^2 Q^2)`.  Neither can produce (1.8) in the live regime
`xi=o(1)`, `Q->infinity`.

## 3. Exact joint first-blocker telescope

Let

\[
 \mathcal C_0\supseteq\mathcal C_1\supseteq\cdots
 \supseteq\mathcal C_\tau=\mathcal C                 \tag{3.1}
\]

be the actual nested stopped catalogues, with the first one the complete
restored labelled catalogue, and put `Z_j=|C_j|`.  For a target
and a target pair define

\[
 X_j(T)=\sum_{F\in\mathcal C_j}I_T(F),\qquad
 X_j(T,U)=\sum_{F\in\mathcal C_j}I_T(F)I_U(F),       \tag{3.2}
\]

\[
 p_j(T)={X_j(T)\over Z_j},\qquad
 p_j(T,U)={X_j(T,U)\over Z_j}.                       \tag{3.3}
\]

Write `D_j=C_j-C_(j+1)` and, whenever the relevant denominator is
positive, put

\[
 d_j={|\mathcal D_j|\over Z_j},\qquad
 d_j(T)={|\mathcal D_j\cap\mathcal S_j(T)|\over X_j(T)},
                                                                    \tag{3.4}
\]

\[
 d_j(T,U)=
 {|\mathcal D_j\cap\mathcal S_j(T)\cap\mathcal S_j(U)|
       \over X_j(T,U)}.                                  \tag{3.5}
\]

If a terminal joint star is nonempty, every denominator for that pair and
its marginals is positive at every preceding time.

### Theorem 3.1 (joint protection and association current)

For every pair with `p_tau(T,U)>0`, define

\[
 \mathscr P_\tau(T)=
 \sum_{j<\tau}\log{1-d_j(T)\over1-d_j},              \tag{3.6}
\]

\[
 \mathscr P_\tau^{(2)}(T,U)=
 \sum_{j<\tau}\log{1-d_j(T,U)\over1-d_j},            \tag{3.7}
\]

and the joint association current

\[
 \mathscr A_\tau(T,U)=
 \sum_{j<\tau}\log
 {\{1-d_j(T,U)\}\{1-d_j\}
       \over\{1-d_j(T)\}\{1-d_j(U)\}}.              \tag{3.8}
\]

Then, pathwise,

\[
 \boxed{p_\tau(T)=p_0(T)e^{\mathscr P_\tau(T)},
 \qquad
 p_\tau(T,U)=p_0(T,U)e^{\mathscr P_\tau^{(2)}(T,U)},} \tag{3.9}
\]

\[
 \boxed{
 {p_\tau(T,U)\over p_\tau(T)p_\tau(U)}
 ={p_0(T,U)\over p_0(T)p_0(U)}
       e^{\mathscr A_\tau(T,U)},
 \qquad
 \mathscr A_\tau=\mathscr P_\tau^{(2)}
                  -\mathscr P_\tau(T)-\mathscr P_\tau(U).} \tag{3.10}
\]

#### Proof

Directly from (3.2)--(3.5),

\[
 {p_{j+1}(T)\over p_j(T)}={1-d_j(T)\over1-d_j},
 \qquad
 {p_{j+1}(T,U)\over p_j(T,U)}={1-d_j(T,U)\over1-d_j}.  \tag{3.11}
\]

Multiplication over `j` proves (3.9).  Divide the pair identity by the two
marginal identities; the one-step factor is exactly the summand in (3.8).
This proves (3.10). `square`

The first-blocker cells from C.13 make every term explicit.  If accepted
rows in bite `j` are deterministically ordered and `B_j(G)` denotes the
corresponding first-blocker cell, then

\[
 Z_jd_j=\sum_G|\mathcal B_j(G)|,                    \tag{3.12}
\]

\[
 X_j(T)d_j(T)=\sum_G|\mathcal B_j(G)\cap\mathcal S_j(T)|,
                                                                    \tag{3.13}
\]

\[
 \boxed{
 X_j(T,U)d_j(T,U)=
 \sum_G|\mathcal B_j(G)\cap\mathcal S_j(T)
                         \cap\mathcal S_j(U)|.}     \tag{3.14}
\]

Equations (2.3) and (3.10) identify the precise stopped statistic needed by
the second-moment route.  For every pair with
\(p_\tau(T)p_\tau(U)>0\), define the extended terminal likelihood ratio

\[
 \Lambda_\tau(T,U)={p_\tau(T,U)\over
                         p_\tau(T)p_\tau(U)},            \tag{3.15a}
\]

so it is zero when the two terminal marginal stars are nonempty but their
joint star is empty.  On the positive-joint support, (3.10) gives its
association-current representation.  Therefore

\[
 \boxed{
 \mathbb E_{T,U\sim\omega}\Lambda_\tau(T,U)
 =
 \mathbb E_{T,U\sim\omega}\left[
 {p_0(T,U)\over p_0(T)p_0(U)}
 e^{\mathscr A_\tau(T,U)}
 \right]
 ={J\over\mu^2}.}                                  \tag{3.15}
\]

In the middle expression the whole bracket is, by convention, zero on an
empty terminal joint star; the logarithm \(\mathscr A_\tau\) is not
separately asserted there.

Thus the open pair-degree lower bound is exactly the lower bound
`Omega(1/xi)` for the left side of (3.15), at every residual peeling stage.
It can come from pre-existing physical vertical compatibility
`p_0(T,U)/(p_0(T)p_0(U))`, from positive stopped association current, or
from both.  Marginal protection alone does not distinguish them.

In the complete restored catalogue, a depth-`q` target has

\[
 p_0(T)={b\over B_q},\qquad B_q={b\choose r-q}.       \tag{3.16}
\]

Under (1.8)--(1.9), every nonempty terminal hole therefore has the uniform
upper marginal-protection bound

\[
 \boxed{
 \mathscr P_\tau(T)=\log{p_T\over p_0(T)}
 \le\log(2RC_1),}                                   \tag{3.17}
\]

because `B_q<=A`.  Hence the factor `1/xi` demanded by (2.4) is not hidden
in an unbounded positive marginal-protection tail when the three scalar
hypotheses hold; it is a pair-compatibility/association phenomenon.

### Proposition 3.2 (marginal protection does not determine association)

There are two one-step deletion systems with identical initial catalogue,
identical deleted fraction, and identical marginal protection increments
for `T` and `U`, but with different joint association increments.

Indeed, take sixteen labelled records, four in each incidence cell

\[
 (I_T,I_U)\in\{(0,0),(1,0),(0,1),(1,1)\}.             \tag{3.18}
\]

In system `+`, retain respectively `3,1,1,3` records in those four cells;
in system `-`, retain `1,3,3,1`.  Both systems retain eight records and,
for each of `T,U`, retain four of the eight incident records.  Thus

\[
 d=d(T)=d(U)={1\over2},                              \tag{3.19}
\]

so both marginal protection increments are zero.  The initial joint star
has four records.  System `+` retains three of them and system `-` retains
one, so

\[
 d_+(T,U)={1\over4},\qquad d_-(T,U)={3\over4},       \tag{3.20}
\]

and the association multipliers from (3.8) are respectively

\[
 {3\over2}\qquad\hbox{and}\qquad {1\over2}.         \tag{3.21}
\]

Taking the retained cells `2,0,0,2` versus `0,2,2,0` gives the still
sharper finite alternative: the same zero marginal increments coexist with
a doubled joint association or with an empty terminal joint star.  These
are abstract incidence catalogues, not claimed punctured residuals.  They
prove that the marginal C.13 telescope has no algebraic implication for
(3.8); punctured cross-depth geometry must be added.

## 4. Fixed-depth information cannot force the pair lower bound

The following finite theorem formalizes the all-depth information gap.

### Theorem 4.1 (independent depth scrambling)

Let `C` be any finite set of `Z` labelled records and let
`z_1,...,z_Q:C->[0,1]`.  For each `q`, choose independently a uniform
permutation `sigma_q` of `C` and set

\[
 \widetilde z_q(F)=z_q(\sigma_qF),\qquad
 \widetilde\Phi(F)=\sum_q\widetilde z_q(F).          \tag{4.1}
\]

Writing `mu=sum_q E z_q`, one has

\[
 \boxed{
 \mathbb E_{\sigma_1,\ldots,\sigma_Q}
 \mathbb E_F\widetilde\Phi(F)^2
 =\sum_q\mathbb Ez_q^2+
   \sum_{q\ne d}(\mathbb Ez_q)(\mathbb Ez_d)
 \le\mu+\mu^2.}                                    \tag{4.2}
\]

Consequently there is a deterministic choice of the depth permutations
for which

\[
 \boxed{\mathbb E_F\widetilde\Phi(F)^2\le\mu+\mu^2.} \tag{4.3}
\]

#### Proof

For each `q`, row permutation preserves `E z_q^2`.  For `q ne d`,
independence of the two permutations makes

\[
 \mathbb E_{\sigma_q,\sigma_d,F}
 \widetilde z_q(F)\widetilde z_d(F)
 =(\mathbb Ez_q)(\mathbb Ez_d).
\]

Expansion of the square proves the equality in (4.2).  Since
`0<=z_q<=1`, one has `E z_q^2<=E z_q`; also the off-diagonal product sum is
at most `mu^2`.  This proves the inequality.  Some realization is no
larger than its average, proving (4.3). `square`

The scrambling applies to the whole incidence matrix at a fixed depth, not
to individual target columns.  It therefore preserves, separately at each
depth:

* every target degree `p_T` and every marginal protection value;
* the complete multiset of row scores `z_q(F)`;
* every within-depth target codegree and every statistic invariant under a
  common permutation of the row labels at that depth.

It changes only the coupling of the row records at different depths.  If
`mu<=C_1 xi Q`, (4.3) gives

\[
 {\mathbb E\widetilde\Phi^2\over\xi Q^2}
 \le {C_1\over Q}+C_1^2\xi.                       \tag{4.4}
\]

This tends to zero for `Q->infinity` and `xi->0`.  Therefore no collection
of conclusions which sees each depth only up to an independent row
relabeling can imply `E Phi^2>=c_2 xi Q^2`.

The construction in Theorem 4.1 is an information obstruction, not a
physical punctured counterexample: independent depth scrambling generally
does not come from one cyclic word.  Its force is precisely that a proof
must use that missing physical coupling.  C.13's one-target protection
identity is marginal.  H.11, H.15, and H.16 concern a fixed boundary event
and its fixed-depth harmonic/blocker profile.  Applied separately, they
are invariant under the scrambling above.  They can contribute only after
being upgraded to a two-event, cross-depth statement controlling (3.14) or
(3.8).

The deterministic scrambling furnished by (4.3) is for the one fixed hole
family used to define the functions (z_q).  If a peeling rule produces
several future-selected families, (4.3) does not assert that one
scrambling simultaneously minimizes all of their second moments.  No such
simultaneous assertion is needed for the information obstruction: at each
stage, data invariant under independent depth relabelling still fail to
determine that stage's cross-depth coupling.

## 5. Quantifier audit and narrowed positive target

The terminal hole family and every residual peeling family are selected
after the stopped trajectory is known.  Equations (1.7), (2.3), and
(3.9)--(3.15) are pathwise finite identities and are valid for such
future-selected families.  By contrast, the martingales C.13.6--C.13.11
are fixed-target statements.  One may not condition them on `T,U` being
terminal holes, or average a fixed-target tail estimate under the
future-dependent law `omega`, without a separate stopped uniform-transfer
theorem.

Likewise, a complete-state or regenerated-reference estimate for the
one-step expectation of (3.8) cannot be iterated through adaptive
residuals.  The exact required statement is pathwise/probabilistic on the
actual stopped catalogue and must survive the later geometric peeling.

The three-scalar frontier is therefore narrowed as follows.

1. The first moment and maximum degree are marginal questions.  Together
   with the second moment they imply the sharp baseline bounds (1.9) and
   the bounded marginal protection (3.17).
2. The second moment is equivalent to (2.4), and asymptotically forces the
   cross-depth covariance (2.7).
3. Its exact stopped source is the joint first-blocker association current
   (3.8), with cell numerator (3.14), combined with initial cyclic
   compatibility as in (3.15).
4. The smallest new geometric theorem capable of closing this route is a
   uniform lower bound of order `1/xi` in (3.15), or equivalently the
   pair-degree lower bound itself, for every residual family generated by
   a specified balanced peeling rule.  It must be a joint cross-depth
   theorem; the existing marginal/fixed-depth lemmas cannot supply it by
   separate application.

This leaves the positive Gate-B scalar open, but removes the ambiguity
about which part of first-blocker protection must be controlled and rules
out any proof assembled only from the presently certified one-depth
profiles.

## 6. The minimal aggregate four-root gate

Write

\[
 \mathcal H_q=\mathcal H_q^-\sqcup\mathcal H_q^+
\]

and retain all shore and depth tags.  Define the ordered cross-depth
coincidence mass

\[
 \boxed{
 J_\times(\mathcal H)=
 {1\over4b^2}
 \sum_{\substack{1\le q,d\le Q\\q\ne d}}
 \ \sum_{\substack{T\in\mathcal H_q\\U\in\mathcal H_d}}
 p_{TU}.}                                               \tag{6.1}
\]

Each summand asks one survivor row to contain two windows at different
depths.  Equivalently, it is a four-boundary-root incidence, with
coincident endpoints allowed when the physical windows force them.

### Theorem 6.1 (weakest aggregate cross-depth reduction)

At every nonterminal geometric peeling stage, suppose the one-sided
degree cap and first-moment upper bound in (1.8) hold with fixed
constants.  If, for one fixed \(c_\times>0\),

\[
 \boxed{J_\times(\mathcal H_i)\ge
             c_\times\xi_iQ^2}                          \tag{6.2}
\]

for the actual current family, then the scalar second-moment hypothesis
of Corollary 5.4 in the protection--vertical-tilt theorem holds with
\(c_2=c_\times\).  Hence its geometric peeling and rounding conclusions
close Gate B, subject to the other interfaces stated there.

Equivalently, because \(p_{TU}=X_\tau(T,U)/Z_\tau\), the concrete
four-root count required at stage \(i\) is

\[
 \boxed{
 \sum_{q\ne d}\sum_{\substack{T\in\mathcal H_{i,q}\\
                              U\in\mathcal H_{i,d}}}
 X_\tau(T,U)
 \ge4b^2c_\times\xi_iQ^2Z_\tau.}                       \tag{6.2a}
\]

Conversely, suppose

\[
 \mu_i\le C_1\xi_iQ,\qquad
 J_i\ge c_2\xi_iQ^2.
\]

If \(Q\ge2C_1/c_2\), then necessarily

\[
 \boxed{J_\times(\mathcal H_i)\ge
             {c_2\over2}\xi_iQ^2.}                     \tag{6.3}
\]

Thus (6.2) is equivalent up to an absolute constant to the missing scalar
moment in the live range.  Among assumptions expressed only as an
aggregate of cross-depth pair incidences, it discards exactly the
nonnegative same-depth part and no more.

#### Proof

Expanding the score by depths gives

\[
 J_i=\mathbb E\Phi_i^2
 =\sum_{q=1}^Q\mathbb Ez_q^2+J_\times(\mathcal H_i).
                                                               \tag{6.4}
\]

The first term is nonnegative, so (6.2) implies the required lower bound
on \(J_i\).  This invokes Corollary 5.4 with the already assumed marginal
hypotheses.

In the reverse direction, \(0\le z_q\le1\) gives

\[
 \sum_q\mathbb Ez_q^2\le\sum_q\mathbb Ez_q=\mu_i.
\]

Subtract this from (6.4) and use the two displayed scalar bounds:

\[
 J_\times\ge c_2\xi_iQ^2-C_1\xi_iQ
 \ge {c_2\over2}\xi_iQ^2.
\]

This proves (6.3).  \(\square\)

The association-current form of (6.1) is also exact.  When
\(p_Tp_U>0\), set

\[
 \Lambda_\tau(T,U)={p_\tau(T,U)\over p_\tau(T)p_\tau(U)},
                                                               \tag{6.5}
\]

including the value zero when the terminal joint star is empty.  Values
on zero \(p_Tp_U\)-mass are immaterial.  For a positive terminal joint
star, (3.10) gives

\[
 \Lambda_\tau(T,U)=
 {p_0(T,U)\over p_0(T)p_0(U)}
 e^{\mathscr A_\tau(T,U)}.                             \tag{6.6}
\]

Consequently

\[
 \boxed{
 J_\times={1\over4b^2}
 \sum_{q\ne d}\sum_{\substack{T\in\mathcal H_q\\U\in\mathcal H_d}}
 p_Tp_U\Lambda_\tau(T,U).}                             \tag{6.7}
\]

Put

\[
 M_\times={1\over4b^2}
 \sum_{q\ne d}\sum_{\substack{T\in\mathcal H_q\\U\in\mathcal H_d}}
 p_Tp_U\le\mu^2.                                       \tag{6.8}
\]

If \(M_\times>0\), normalize its summands to a cross-depth product-Palm
law.  Under the first-moment bound, (6.2) is the four-root likelihood
estimate

\[
 \mathbb E_{\rm cross\ Palm}\Lambda_\tau
 ={J_\times\over M_\times}
 \ge {c_\times\over C_1^2\xi}.                         \tag{6.9}
\]

If \(M_\times=0\), then \(J_\times=0\), so (6.2) cannot hold.  Formula
(6.9) shows why a factor of order \(1/\xi\) is unavoidable when the
product-Palm mass is at its largest permitted scale.  If that mass is
smaller, the required average association is correspondingly larger.

For comparison, the centered four-root current is

\[
 \Gamma_\times
 =J_\times-M_\times
 =\sum_{q\ne d}\operatorname {Cov}(z_q,z_d).           \tag{6.10}
\]

Since \(M_\times\le C_1^2\xi^2Q^2\), (6.2) and a positive lower bound of
order \(\xi Q^2\) on (6.10) are asymptotically equivalent when
\(\xi=o(1)\).  The raw form (6.2) is the weaker exact sufficient
statement; it does not demand that the negligible independent baseline
be subtracted.

The quantifier in Theorem 6.1 is pathwise.  The family
\(\mathcal H_i\) is allowed to be selected by the prescribed peeling rule
after the stopped trajectory and all terminal incidences are known.
Accordingly, a probabilistic proof of (6.2) must hold simultaneously for
the actual future-selected stages, or be a conditional theorem uniform
over every family the rule can output.  A fixed-family estimate cannot be
conditioned on later selection.

### Proposition 6.2 (fixed-depth data do not imply (6.2))

There are abstract labelled catalogues with identical complete
fixed-depth incidence data but with cross-depth masses differing by a
factor \(1/\eta\), where \(\eta\) is their common one-depth incidence
density.

Let \(M\) be prime, \(Q\le M\), and take the labelled record set
\(\mathbb F_M^2\).  At each depth replicate one binary column \(2b\)
times, so its normalized depth score is the column itself and all
within-depth degrees and codegrees are determined by that column.  In the
aligned system put

\[
 z_q(a,c)=\mathbf1_{\{a=0\}}\qquad(1\le q\le Q),
\]

whereas in the scrambled system choose distinct field elements
\(\lambda_q\) and put

\[
 \widetilde z_q(a,c)
 =\mathbf1_{\{a+\lambda_qc=0\}}.
\]

Every fixed-depth column in either system has exactly \(M\) ones and the
two incidence matrices at that depth differ only by a row permutation.
Thus all fixed-depth target degrees, codegrees, row-score multisets, and
marginal protection values agree.  With \(\eta=1/M\),

\[
\begin{array}{c|c|c}
 &\mathbb E\Phi^2&J_\times\\ \hline
\text{aligned}
 &\eta Q^2&\eta Q(Q-1),\\
\text{scrambled}
 &\eta Q+\eta^2Q(Q-1)&\eta^2Q(Q-1).
\end{array}                                             \tag{6.11}
\]

Indeed, two distinct affine equations have one common solution, whereas
all aligned depth events are the same event.  Hence the aligned system
satisfies the scalar lower bound with a constant, while

\[
 {\mathbb E\widetilde\Phi^2\over\eta Q^2}
 ={1\over Q}+\eta\left(1-{1\over Q}\right)\longrightarrow0
                                                               \tag{6.12}
\]

as \(Q,M\to\infty\).  This is an information counterexample, not a
punctured physical residual.  It proves that (6.2), or an equivalent
cross-depth physical coupling theorem, cannot be replaced by any
collection of independently row-relabeling-invariant fixed-depth facts.

## 7. Finite audit

The checker

    scratch/verify_gate_b_cross_depth_association_current_20260822.py

uses exact rational arithmetic.  It verifies (1.7), (2.3),
(2.5)--(2.7), the labelled joint telescope (3.9)--(3.10), the
first-blocker sums, (3.17), the fixed-depth scrambling invariants and
average (4.2), the future-selected-family scope, and the
four-root reduction and counterexample in Section 6.
