# Gate B: exact protection--vertical-tilt transform

**Date:** 2026-08-22  
**Status:** unconditional pathwise theorem and positive reduction.  A
fractional cover supported on one terminal survivor catalogue need not obtain
the whole factor `1/x` from the unweighted external degree of every hole.
The factor splits exactly into terminal relative protection and a rooted
multidepth change of measure.  Indicator tilts give a concrete rooted
vertical-rich-event criterion; exponential tilts give an integrated rooted
score-current criterion.  The note does not prove the required rooted
advantage for the actual stopped residual.

## 1. Catalogue, holes, and relative protection

Fix `r>=2` and put

\[
 b=2r+1,\qquad A={b\choose r},\qquad B={A\over b}.
\tag{1.1}
\]

Let `C` be a nonempty finite labelled catalogue of directed cyclic rows and
write `Z=|C|`.  The labels may distinguish several copies of the same
physical row.  Fix `1<=Q<=r-1` and a tagged depth `1<=q<=Q`, and put

\[
 k_q=r-q,\qquad B_q={b\choose{k_q}},
\tag{1.2}
\]

and identify the complementary upper shore with a second tagged copy of
the same `k_q`-set layer.  For a tagged target `T` at depth `q`, let

\[
 \mathcal S(T)=\{F\in\mathcal C:T\text{ is a full-row window of }F\},
 \qquad X(T)=|\mathcal S(T)|.
\tag{1.3}
\]

Define the catalogue relative protection by

\[
 \mathscr P(T)=
 \begin{cases}
 \displaystyle\log\!\left({X(T)/Z\over b/B_q}\right),&X(T)>0,\\[6pt]
 -\infty,&X(T)=0.
 \end{cases}
\tag{1.4}
\]

If `C` is the terminal catalogue of the stopped punctured process, (1.4)
is exactly its previously defined telescoping relative protection, because
the complete initial catalogue has target incidence probability `b/B_q`.
No probabilistic conditioning is used below: after a trajectory is fixed,
all statements are deterministic finite identities.  The identities do not
require `Q` to equal the C.9 shallow cutoff.  For the all-depth Gate-B
interface one must instead take the complete master cutoff
`Q=ceil(sqrt(b log b))` (for sufficiently large `r`).

Let

\[
 \mathcal H=\bigsqcup_{q=1}^Q
       (\mathcal H_q^-\sqcup\mathcal H_q^+)
\tag{1.5}
\]

be any fixed shore-tagged hole family.  A full row has exactly `b` windows
on each tagged layer.  Put

\[
 s_q(F)=\sum_{u\in\mathbb Z_b}
 \left({\bf1}_{I_{r-q}^F(u)\in\mathcal H_q^-}
      +{\bf1}_{I_{r+1+q}^F(u)\in\mathcal H_q^+}\right),
 \qquad z_q(F)={s_q(F)\over2b}.
\tag{1.6}
\]

Thus `0<=z_q<=1`, and the same row `F` supplies all `Q` coordinates.

## 2. Exact change-of-measure identity

Let `U` be the uniform probability law on `C`.  When `X(T)>0`, let `U^T`
be `U` conditioned on `F in S(T)`, equivalently the uniform law on the
external star `S(T)`.  For an arbitrary function

\[
                         w:\mathcal C\longrightarrow[0,\infty)
\tag{2.1}
\]

with `E_U w>0`, define one common tilted row law

\[
 \pi_w(F)={w(F)\over Z\,\mathbb E_Uw}.
\tag{2.2}
\]

In every logarithmic or rooted criterion below, a target with `X(T)=0`
has combined potential `-infinity` and fails the criterion.  Expressions
involving `U^T` are asserted only when `X(T)>0`.  This is forced rather than
cosmetic: no cover supported on `C` can cover an empty-star target.

### Theorem 2.1 (protection--tilt factorization)

For every tagged target `T`,

\[
 \boxed{
 \Pr_{\pi_w}(T\subset F)
 ={b\over B_q}\,e^{\mathscr P(T)}
   {\mathbb E_{U^T}w\over\mathbb E_Uw}.}
\tag{2.3}
\]

Here the right side is interpreted as zero when `X(T)=0`; no conditional
law `U^T` is then required.

Consequently, for fixed `K,x>0`, giving every labelled row `F` weight

\[
                         y_F=KxB\,\pi_w(F)
\tag{2.4}
\]

is a fractional cover of a subfamily `H' subseteq H` if and only if, for
every `T in H'` at depth `q`,

\[
 \boxed{
 \mathscr P(T)+
 \log{\mathbb E_{U^T}w\over\mathbb E_Uw}
 \ge \log{B_q\over KxA}.}
\tag{2.5}
\]

In particular, `H'` has a survivor-supported fractional cover of mass at
most `KxB` if and only if there is one nonnegative `w` satisfying (2.5)
simultaneously for every `T in H'`.

#### Proof

For `X(T)>0`, reverse the finite sums:

\[
\begin{aligned}
 \Pr_{\pi_w}(T\subset F)
 &=\sum_{F\in\mathcal S(T)}{w(F)\over Z\mathbb E_Uw}\\
 &={X(T)\over Z}{\mathbb E_{U^T}w\over\mathbb E_Uw}\\
 &={b\over B_q}e^{\mathscr P(T)}
       {\mathbb E_{U^T}w\over\mathbb E_Uw},
\end{aligned}
\tag{2.6}
\]

which proves (2.3).  The total mass in (2.4) is `KxB`.  Its coverage of
`T` is at least one precisely when

\[
 \Pr_{\pi_w}(T\subset F)\ge {1\over KxB}
 ={b\over KxA}.
\tag{2.7}
\]

Substitution of (2.3), cancellation of `b`, and taking logarithms gives
(2.5).

If a fractional cover `a_F` of a nonempty family has mass `t<=KxB`,
normalize it to the row law `pi(F)=a_F/t` and set `w(F)=Z pi(F)`.  Then
`E_Uw=1`; moreover every target
has `pi`-incidence at least `1/t>=1/(KxB)`, so (2.5) follows from the
already proved equivalence.  Conversely, (2.4) is the required cover.
The empty-family case is vacuous.  This proves the last assertion. `square`

Taking `w=1` recovers the unweighted survivor criterion

\[
                         \mathscr P(T)\ge
                         \log{B_q\over KxA}.
\tag{2.8}
\]

The new point is that (2.8) is sufficient but not necessary: a rooted
vertical tilt may supply part, or all, of the missing logarithm.

### Corollary 2.2 (combined protection is the exact target Palm density)

For `X(T)>0`, define

\[
 \mathscr Q_w(T)=\mathscr P(T)+
       \log{\mathbb E_{U^T}w\over\mathbb E_Uw},
\tag{2.9}
\]

and put `exp(Q_w(T))=0` when `X(T)=0`.  Sample `F` from `pi_w` and then a
uniform start on one fixed tagged depth-`q` shore.  The resulting target
Palm law is

\[
 \boxed{\nu_{q,w}(T)={1\over B_q}e^{\mathscr Q_w(T)}.}
\tag{2.10}
\]

Consequently,

\[
 \boxed{\sum_{T\text{ at tagged depth }q}
               e^{\mathscr Q_w(T)}=B_q,\qquad
 |\{T:\mathscr Q_w(T)\ge s\}|\le B_qe^{-s}.}
\tag{2.11}
\]

At the cover threshold `s=log(B_q/(KxA))`, the upper tail in (2.11) has
size at most `KxA`.  Thus changing the survivor law does not evade the
capacity alignment: it only replaces raw protection by the combined
protection--tilt potential `Q_w`.

#### Proof

A row has exactly `b` windows at the fixed tagged depth, so dividing its
target-incidence probabilities by `b` gives a probability law.  Equation
(2.3) divided by `b` is (2.10).  Summing (2.10) proves the first identity
in (2.11), and Markov's counting argument proves the second. `square`

## 3. A rooted vertical-rich-event criterion

For `0<=a<1` and `0<rho<=1`, define

\[
 R_a(F)={1\over Q}
   |\{q:s_q(F)\ge2ab\}|,
 \qquad
 E_{a,\rho}=\{F:R_a(F)\ge\rho\}.
\tag{3.1}
\]

This is the same genuinely vertical event used by the vertical
concentration theorem: one row must be hole-rich at a positive fraction of
the depths.

### Corollary 3.1 (conditioning on one common rich event)

Suppose `U(E_(a,rho))>0`.  Uniform measure on the survivor rows in
`E_(a,rho)`, assigned total mass `KxB`, fractionally covers a family `H'`
of positive-star targets if and
only if

\[
 \boxed{
 {U(E_{a,\rho}\mid T)\over U(E_{a,\rho})}
 \ge {B_q\over KxA}\,e^{-\mathscr P(T)}
 \qquad(T\in\mathcal H'_q).}
\tag{3.2}
\]

Thus a concrete positive Gate-B theorem may split into two factors:

\[
 e^{\mathscr P(T)}
 \quad\hbox{and}\quad
 {U(E_{a,\rho}\mid T)\over U(E_{a,\rho})},
\tag{3.3}
\]

whose product must be at least `B_q/(KxA)` for every nonexceptional hole.

#### Proof

Apply Theorem 2.1 with `w=1_(E_(a,rho))`. `square`

For example, uniformly over the shallow range `B_q/A=Theta(1)`, it is
enough for some `0<=lambda<=1` and constants `C_1,C_2>0` that

\[
 \mathscr P(T)\ge\lambda\log(1/x)-C_1,
 \qquad
 {U(E_{a,\rho}\mid T)\over U(E_{a,\rho})}
       \ge C_2x^{-(1-\lambda)}.
\tag{3.4}
\]

Then (3.2) holds with an absolute `K` depending only on `C_1,C_2` and the
uniform lower bound for `A/B_q`.  This interpolates continuously between
the full relative-protection route (`lambda=1`) and a purely vertical
rooted-conditioning route (`lambda=0`).

The quantifier in (3.2) is essential.  A lower bound on `U(E)` or on the
average of `U(E|T)` over holes does not give a fractional cover.  The same
event and the same conditioned row law must satisfy (3.2) target by target.

## 4. Multidepth exponential tilts and the exact current

Let `theta=(theta_1,...,theta_Q) in R^Q` and put

\[
 \Phi_\theta(F)=\sum_{q=1}^Q\theta_qz_q(F),
 \qquad w_\theta(F)=e^{\Phi_\theta(F)}.
\tag{4.1}
\]

For `0<=t<=1`, let `U_(t theta)` be the law on `C` with density
proportional to `exp(t Phi_theta)` relative to `U`, and let
`U_(t theta)^T` be the analogous tilt of the rooted law `U^T`.

### Theorem 4.1 (integrated rooted vertical current)

For every target with `X(T)>0`,

\[
 \boxed{
 \log{\mathbb E_{U^T}e^{\Phi_\theta}\over
            \mathbb E_Ue^{\Phi_\theta}}
 =\int_0^1\sum_{q=1}^Q\theta_q
 \left(\mathbb E_{U_{t\theta}^T}z_q
      -\mathbb E_{U_{t\theta}}z_q\right)dt.}
\tag{4.2}
\]

Hence the single exponential row law `pi_(w_theta)` gives a fractional
cover of mass `KxB` on `H'` whenever, simultaneously for every
`T in H'_q`,

\[
 \boxed{
 \mathscr P(T)+
 \int_0^1\sum_{d=1}^Q\theta_d
 \left(\mathbb E_{U_{t\theta}^T}z_d
      -\mathbb E_{U_{t\theta}}z_d\right)dt
 \ge\log{B_q\over KxA}.}
\tag{4.3}
\]

#### Proof

For

\[
 f_T(t)=\log\mathbb E_{U^T}e^{t\Phi_\theta}
       -\log\mathbb E_Ue^{t\Phi_\theta},
\tag{4.4}
\]

finite differentiation gives

\[
 f_T'(t)=\mathbb E_{U_{t\theta}^T}\Phi_\theta
          -\mathbb E_{U_{t\theta}}\Phi_\theta.
\tag{4.5}
\]

Since `f_T(0)=0`, integration and (4.1) give (4.2).  Substitute (4.2)
into (2.5) to obtain (4.3). `square`

Equation (4.3) is a positive multidepth transform, rather than a signed
linear response.  It requires one vector `theta` for the complete band.
Separate vectors chosen after seeing each target would not define one row
law and would not prove Gate B.

### Corollary 4.2 (subgaussian rooted-mean criterion)

Let `Phi:C->R` be one common multidepth statistic.  Suppose that for some
`V>=0` and `lambda>=0`,

\[
 \log\mathbb E_U
       e^{\lambda(\Phi-\mathbb E_U\Phi)}
 \le {\lambda^2V\over2}.
\tag{4.6}
\]

If, for every `T in H'_q`,

\[
 \boxed{
 \mathscr P(T)+\lambda
   (\mathbb E_{U^T}\Phi-\mathbb E_U\Phi)
       -{\lambda^2V\over2}
 \ge\log{B_q\over KxA},}
\tag{4.7}
\]

then the tilt `w=exp(lambda Phi)` is a fractional cover law of mass
`KxB` on `H'`.

In particular, if one common lower bound

\[
 \mathbb E_{U^T}\Phi-\mathbb E_U\Phi\ge\Delta>0
 \qquad(T\in\mathcal H')
\tag{4.8}
\]

holds and (4.6) is valid at `lambda=Delta/V` with `V>0`, then the tilt
supplies at least

\[
                         {\Delta^2\over2V}
\tag{4.9}
\]

of the missing logarithmic factor.  Thus, for the vertical score
`Phi=sum_(q<=Q) z_q`, a variance proxy `V=O(Q)` would reduce a wholly
tilt-supplied factor `log(1/x)` to the targetwise rooted-mean requirement

\[
                         \Delta=\Omega(\sqrt{Q\log(1/x)}),
\tag{4.10}
\]

not a linear-in-`Q` mean gap.

#### Proof

Jensen's inequality under the rooted law gives

\[
 \log\mathbb E_{U^T}e^{\lambda\Phi}
 \ge\lambda\mathbb E_{U^T}\Phi.
\tag{4.11}
\]

Equation (4.6) gives

\[
 \log\mathbb E_Ue^{\lambda\Phi}
 \le\lambda\mathbb E_U\Phi+{\lambda^2V\over2}.
\tag{4.12}
\]

Subtract (4.12) from (4.11), add `P(T)`, and apply (2.5); this proves
(4.7).  Substitution of `lambda=Delta/V` proves (4.9).  Finally solve
`Delta^2/(2V)>=log(1/x)-O(1)` when `V=O(Q)` to obtain (4.10). `square`

The hypotheses in (4.6) and (4.8) must hold for the actual terminal
catalogue.  Product-reference concentration or an average rooted mean over
the terminal holes cannot be substituted for these two pathwise inputs.

### Corollary 4.3 (the required tangent is a centered co-hole Gram row)

For tagged holes `T,U`, put

\[
 X(T,U)=|\mathcal S(T)\cap\mathcal S(U)|
\tag{4.13}
\]

(with the shore and depth tags retained), and take

\[
                         \Phi(F)=\sum_{q=1}^Qz_q(F).
\tag{4.14}
\]

For every `T` with `X(T)>0`, the rooted mean gap in (4.8) is exactly

\[
 \boxed{
 \Delta_{\mathcal H}(T)
 ={1\over2b}\sum_{U\in\mathcal H}
 \left({X(T,U)\over X(T)}-{X(U)\over Z}\right).}
\tag{4.15}
\]

Therefore a concrete sufficient positive theorem is:

1. the actual terminal vertical score (4.14) is subgaussian under `U` with
   proxy `V=O(Q)` at the required common tilt;
2. outside `o(A)` holes, all stars are nonempty and the centered co-hole
   Gram row (4.15), together
   with the raw protection `P(T)`, satisfies (4.7).

Conditional on the separate subgaussian input, the exponent in this
targetwise sufficient criterion can be supplied by a smaller score scale
than the order-`Q` scale appearing in a one-step unweighted row-score
criterion.  With bounded raw protection, (4.10) asks only
`Delta_H(T)=Omega(sqrt(Q log(1/x)))`, whereas a one-step unweighted
row-score criterion at the capacity scale asks for a rooted vertical score
of order `Q`.  This compares the scalar sufficient thresholds only; it does
not order the underlying hypotheses or establish the required mean gap.

#### Proof

Because all layers and shores are tagged, (1.6) gives the exact finite
identity

\[
 \Phi(F)={1\over2b}\sum_{U\in\mathcal H}
                         {\bf1}_{\{F\in\mathcal S(U)\}}.
\tag{4.16}
\]

Average (4.16) first under `U^T` and then under `U`, and subtract.  The two
incidence probabilities are respectively `X(T,U)/X(T)` and `X(U)/Z`,
which proves (4.15).  The sufficient statement is Corollary 4.2. `square`

### Corollary 4.4 (variance is the incidence-weighted mean tangent)

Let

\[
 p_T={X(T)\over Z}=\Pr_U(T\subset F).
\tag{4.17}
\]

For the identities in this corollary, set
`Delta_H(T)=0` when `p_T=0`; its value is immaterial because its incidence
weight is zero.  Rooted tilt criteria still fail on such a target, as fixed
after (2.2).

For the score `Phi` in (4.14),

\[
 \boxed{
 \sum_{T\in\mathcal H}p_T\Delta_{\mathcal H}(T)
 =2b\,\operatorname {Var}_U\Phi.}
\tag{4.18}
\]

If `E_U Phi>0`, the probability law

\[
 \omega(T)={p_T\over2b\,\mathbb E_U\Phi}
 \qquad(T\in\mathcal H)
\tag{4.19}
\]

therefore satisfies

\[
 \boxed{
 \mathbb E_{T\sim\omega}\Delta_{\mathcal H}(T)
 ={\operatorname {Var}_U\Phi\over\mathbb E_U\Phi}.}
\tag{4.20}
\]

Thus vertical score fluctuation automatically creates a positive
*incidence-weighted average* exponential-tilt tangent.  Gate B still needs
the pointwise lower tail in (4.7); (4.20) cannot replace it, because the
positive tangent may be concentrated on a small set of holes.

#### Proof

Let `I_T(F)=1_(F in S(T))`.  Equation (4.16) says

\[
                         \sum_{T\in\mathcal H}I_T=2b\Phi.
\tag{4.21}
\]

Also

\[
 p_T\Delta_{\mathcal H}(T)
 =\mathbb E_U[I_T\Phi]-p_T\mathbb E_U\Phi.
\tag{4.22}
\]

Sum (4.22) over `T` and use (4.21); the result is
`2b(E Phi^2-(E Phi)^2)`, proving (4.18).  Summing `p_T` in (4.21) gives
`2b E Phi`, so (4.19) is a probability law and division proves (4.20).
`square`

## 5. Geometric partial-cover peeling

The preceding targetwise criteria can be weakened further when they are
available repeatedly on the current residual.  This is useful because an
average co-hole tangent may identify a positive fraction of good holes
without controlling all of them in one step.

### Theorem 5.1 (constant-fraction laws suffice)

Fix `Q>=1`, one admissible physical-row universe `Omega`, and a finite
tagged hole family `H_0`.  Put

\[
                         \xi_i={|\mathcal H_i|\over AQ}.
\tag{5.1}
\]

Assume constants `c in (0,1]` and `K>0` have the following property for
every nonterminal residual `H_i`: there is one probability law `pi_i`
supported on `Omega` and a subset `G_i subseteq H_i` such that

\[
 |\mathcal G_i|\ge c|\mathcal H_i|,
 \qquad
 \Pr_{F\sim\pi_i}(T\subset F)
       \ge {1\over K\xi_iB}\quad(T\in\mathcal G_i).
\tag{5.2}
\]

Set `H_(i+1)=H_i-G_i`.  Stop at any first `m` for which
`|H_m|<=epsilon A`.  Then the union of the stagewise fractional weights

\[
                         y^{(i)}=K\xi_iB\,\pi_i
\tag{5.3}
\]

covers `H_0-H_m` and has total mass at most

\[
 \boxed{
 \sum_{i<m}\|y^{(i)}\|_1
 \le {K\over c}\,{|\mathcal H_0|\over AQ}\,B.}
\tag{5.4}
\]

Consequently, if `|H_0|=O(xAQ)` and `epsilon=o(1)`, these partial laws
already produce a fractional cover of mass `O(xB)` outside `o(A)` holes.

#### Proof

Equation (5.2) and (5.3) give coverage at least one on every member of
`G_i`.  Moreover

\[
 |\mathcal H_{i+1}|\le(1-c)|\mathcal H_i|,
 \qquad
 \xi_i\le(1-c)^i\xi_0.
\tag{5.5}
\]

Therefore the sum of the masses in (5.3) is at most

\[
 K B\sum_{i\ge0}\xi_i
 \le K B\xi_0\sum_{i\ge0}(1-c)^i
 ={K\over c}\xi_0B,
\tag{5.6}
\]

which is (5.4).  Every removed target remains covered by the sum of the
stagewise vectors, while only `H_m` is omitted. `square`

Theorem 5.1 changes the positive quantifier in a material way.  At stage
`i`, (2.5), (3.2), or (4.7) is needed only on a fixed positive fraction
`G_i` of the *current* holes, with `x` in the mass normalization replaced
by their aggregate density `xi_i`.  The laws may change between stages but
must remain on the same admissible universe `Omega`; their weighted sum is
still one valid fractional cover.  Separate laws for
individual targets would not have the geometric mass bound (5.4).

### Corollary 5.2 (variance-to-positive-fraction tilt)

Apply Corollaries 4.2--4.4 to a nonempty current family `H_i`, its score
`Phi_i`, and its uniform catalogue law `U`.  Abbreviate

\[
 \mu_i=\mathbb E_U\Phi_i,
 \qquad
 m_i={\operatorname {Var}_U\Phi_i\over\mu_i},
\tag{5.7}
\]

and assume `mu_i>0`.  Suppose every current hole has `p_T=X(T)/Z>0` and
the hole-incidence probabilities obey

\[
 {\max_{T\in\mathcal H_i}p_T
  \over\min_{T\in\mathcal H_i}p_T}\le R.
\tag{5.8}
\]

Then at least

\[
 \boxed{
 {m_i\over R(2Q-m_i)}\,|\mathcal H_i|}
\tag{5.9}
\]

holes satisfy

\[
                         \Delta_{\mathcal H_i}(T)\ge {m_i\over2}.
\tag{5.10}
\]

Here `0<=m_i<=Q`.  If, in addition, for some `V_i>0`,

\[
 \log\mathbb E_U
  \exp\!\left\{{m_i\over2V_i}(\Phi_i-\mu_i)\right\}
 \le {m_i^2\over8V_i},
\tag{5.11}
\]

and every hole counted in (5.9) obeys

\[
 \boxed{
 \mathscr P(T)+{m_i^2\over8V_i}
 \ge\log{B_{q(T)}\over K\xi_iA},}
\tag{5.12}
\]

then one exponential row law covers all those holes with fractional mass
`K xi_i B`.

Consequently, if (5.8), (5.11), and (5.12) hold at every nonterminal
stage with fixed `R,K` and

\[
                         m_i\ge c_0Q>0,
\tag{5.13}
\]

then Theorem 5.1 applies with

\[
                         c={c_0\over R(2-c_0)},
\tag{5.14}
\]

and gives the required `O(xB)` fractional cover whenever
`|H_0|=O(xAQ)`.

#### Proof

Under the incidence-weighted target law `omega_i` from (4.19), (4.20)
gives `E_omega Delta=m_i`.  Since `0<=Phi_i<=Q`,

\[
 \operatorname {Var}\Phi_i
 \le\mathbb E\Phi_i^2
 \le Q\mathbb E\Phi_i,
\tag{5.15}
\]

so `m_i<=Q`.  Also every rooted mean gap is at most `Q`.  If
`G_i={T:Delta(T)>=m_i/2}`, then

\[
 m_i\le {m_i\over2}(1-\omega_i(\mathcal G_i))
            +Q\omega_i(\mathcal G_i),
\tag{5.16}
\]

and hence

\[
                         \omega_i(\mathcal G_i)
 \ge {m_i\over2Q-m_i}.
\tag{5.17}
\]

Condition (5.8) converts incidence mass to cardinality:

\[
 \omega_i(\mathcal G_i)
 \le R{|\mathcal G_i|\over|\mathcal H_i|},
\tag{5.18}
\]

which proves (5.9).

Use Corollary 4.2 with
`lambda=m_i/(2V_i)`.  Equations (5.10)--(5.11) make the tilt contribution
at least

\[
 {m_i\over2V_i}{m_i\over2}-{m_i^2\over8V_i}
 ={m_i^2\over8V_i}.
\tag{5.19}
\]

Thus (5.12) and (4.7), with `x=xi_i`, cover `G_i` at the asserted mass.
Finally (5.13) turns (5.9) into the fixed fraction (5.14), and Theorem 5.1
finishes the iteration. `square`

### Theorem 5.3 (aggregate vertical survivor tail suffices)

There is a second route to the positive fraction in Theorem 5.1 which
does not require a pointwise rooted estimate.  Fix one current nonempty
hole family `H_i`, its score `Phi_i=sum_(q<=Q)z_q`, and an event
`E_i subseteq C` with `u_i=U(E_i)>0`, and assume
`E_U Phi_i>0`.  Put

\[
 p_T=\Pr_U(T\subset F),\qquad
 \bar p_i={1\over|\mathcal H_i|}
              \sum_{T\in\mathcal H_i}p_T,
\tag{5.20}
\]

and assume only the one-sided external-degree cap

\[
                         \max_{T\in\mathcal H_i}p_T
                         \le R\bar p_i.
\tag{5.20a}
\]

Define the fraction of all current hole incidences carried by the
event:

\[
 \beta_i={\mathbb E_U[\Phi_i\mathbf1_{E_i}]
                 \over\mathbb E_U\Phi_i}.
\tag{5.21}
\]

Suppose, for fixed constants `a>0` and `beta_0 in (0,1]`,

\[
 \mathbb E_U[\Phi_i\mid E_i]\ge aQ,
 \qquad \beta_i\ge\beta_0.                         
\tag{5.22}
\]

Then uniform measure `pi_i=U(.|E_i)` has a subset
`G_i subseteq H_i` of size at least

\[
 \boxed{
 |\mathcal G_i|\ge
 {\beta_0\over2R(2-\beta_0)}|\mathcal H_i|}
\tag{5.23}
\]

such that

\[
 \boxed{
 \Pr_{F\sim\pi_i}(T\subset F)
 \ge {a\beta_0\over2(2-\beta_0)\xi_iB}
 \qquad(T\in\mathcal G_i).}
\tag{5.24}
\]

Consequently, if (5.20a)--(5.22) hold at every nonterminal peeling stage
with the same `R,a,beta_0`, Theorem 5.1 gives a fractional cover of mass

\[
 O_{R,a,\beta_0}(xB)
\tag{5.25}
\]

outside `o(A)` holes whenever `|H_0|=O(xAQ)`.

#### Proof

For `T` with `p_T>0`, put

\[
 r_T={U(E_i\mid T)\over U(E_i)},
 \qquad
 \omega_i(T)={p_T\over2b\mathbb E_U\Phi_i}.
\tag{5.26}
\]

The denominator in `omega_i` is correct because
`sum_(T in H_i)p_T=2b E_U Phi_i`.  Reversing the finite sums gives the
event analogue of (4.20):

\[
\begin{aligned}
 \mathbb E_{T\sim\omega_i}r_T
 &= {1\over2b\mathbb E_U\Phi_i\,u_i}
       \sum_{T\in\mathcal H_i}\Pr_U(E_i,\,T\subset F)\\
 &= {\mathbb E_U[\Phi_i\mid E_i]
       \over\mathbb E_U\Phi_i}
 =:R_i.
\end{aligned}
\tag{5.27}
\]

Also `0<=r_T<=1/u_i` and

\[
                         u_iR_i=\beta_i.
\tag{5.28}
\]

Let `G_i={T:r_T>=R_i/2}`.  Exactly as in (5.16),

\[
 R_i\le {R_i\over2}(1-\omega_i(\mathcal G_i))
                +{1\over u_i}\omega_i(\mathcal G_i),
\tag{5.29}
\]

so

\[
 \omega_i(\mathcal G_i)
 \ge {u_iR_i\over2-u_iR_i}
 ={\beta_i\over2-\beta_i}
 \ge {\beta_0\over2-\beta_0}.
\tag{5.30}
\]

Write

\[
 g_0={\beta_0\over2-\beta_0},\qquad
 \mathcal L_i=\{T:p_T\ge(g_0/2)\bar p_i\}.
\tag{5.31}
\]

The complement of `L_i` has `omega_i`-mass at most `g_0/2`, while
(5.30) gives `omega_i(G_i)>=g_0` for the preliminary set
`G_i={T:r_T>=R_i/2}`.  Replace `G_i` by its intersection with `L_i`.
The new set has `omega_i`-mass at least `g_0/2`.  The upper cap (5.20a)
therefore gives

\[
 {g_0\over2}
 \le\omega_i(\mathcal G_i)
 ={\sum_{T\in\mathcal G_i}p_T
      \over|\mathcal H_i|\bar p_i}
 \le R{|\mathcal G_i|\over|\mathcal H_i|},
\tag{5.31a}
\]

which is (5.23).

It remains to check the target incidence with no suppressed constants.
The identity preceding (5.27) gives

\[
                         \bar p_i
 ={2b\mathbb E_U\Phi_i\over|\mathcal H_i|}.
\tag{5.31b}
\]

For `T` in the new `G_i`, (5.22), (5.26), and (5.31)--(5.31b) yield

\[
\begin{aligned}
 \Pr_{\pi_i}(T\subset F)
 &=p_Tr_T\\
 &\ge {g_0\over2}
       {2b\mathbb E_U\Phi_i\over|\mathcal H_i|}
       {\mathbb E_U[\Phi_i\mid E_i]
        \over2\mathbb E_U\Phi_i}\\
 &\ge {g_0abQ\over2|\mathcal H_i|}
 ={g_0a\over2\xi_iB},
\end{aligned}
\tag{5.32}
\]

using `|H_i|=xi_i A Q` and `B=A/b`.  Thus (5.2) holds with

\[
 K={2\over g_0a}={2(2-\beta_0)\over a\beta_0},\qquad
 c={g_0\over2R}={\beta_0\over2R(2-\beta_0)}.
\tag{5.33}
\]

Theorem 5.1 proves (5.25). `square`

For the explicit vertical event `E_(eta,rho)` from (3.1), every row in the
event has

\[
                         \Phi_i(F)\ge\eta\rho Q.
\tag{5.34}
\]

Hence (5.22) follows with `a=eta rho` from the single incidence-share
condition `beta_i>=beta_0`.  A more directly probabilistic sufficient
form is

\[
 U(E_{\eta,\rho})\ge c_1\xi_i,
 \qquad
 \mathbb E_U\Phi_i\le C_1\xi_iQ,                 
\tag{5.35}
\]

because (5.34)--(5.35) give

\[
                         \beta_i\ge {c_1\eta\rho\over C_1}.
\tag{5.36}
\]

Conversely, (5.34) and the mean bound in (5.35) give by Markov

\[
 U(E_{\eta,\rho})\le {C_1\over\eta\rho}\,\xi_i.
\tag{5.37}
\]

Thus the requested probability `Omega(xi_i)` is the sharp order under the
same mean hypothesis, not an unnecessarily strong constant-probability
tail.

Thus the positive survivor-tail theorem now sufficient for Gate B has an
aggregate form: at every geometric residual scale, construct one common
event of rows which is vertically rich, has survivor probability
`Omega(xi_i)`, and lies in a catalogue whose current hole score has mean
`O(xi_iQ)` and whose maximum hole degree is at most a constant times the
current hole-average degree.
No target-by-target rooted tail is required after Theorem 5.3.

### Corollary 5.4 (a vertical second moment closes the fractional gate)

The event in Theorem 5.3 follows from two scalar moments.  Suppose that at
every nonterminal residual stage, for fixed constants `R,C_1,c_2>0`,

\[
 \max_{T\in\mathcal H_i}p_T\le R\bar p_i,
\tag{5.38}
\]

\[
 \boxed{
 \mathbb E_U\Phi_i\le C_1\xi_iQ,
 \qquad
 \mathbb E_U\Phi_i^2\ge c_2\xi_iQ^2.}
\tag{5.39}
\]

Then the geometric peeling theorem produces a fractional cover of mass
`O_(R,C_1,c_2)(xB)` outside `o(A)` holes.

Equivalently, the new positive Gate-B moment target is the pair-degree
lower bound

\[
 \boxed{
 \sum_{T,U\in\mathcal H_i}X(T,U)
 \ge 4b^2c_2\xi_iQ^2Z,}
\tag{5.40}
\]

together with (5.38) and the first-moment upper bound in (5.39).

#### Proof

Since `0<=Phi_i<=Q`, the two inequalities in (5.39) imply
`c_2<=C_1`; otherwise
`E Phi_i^2<=Q E Phi_i` would contradict them.  Put

\[
                         a={c_2\over2C_1}\in(0,1/2],
 \qquad E_i=\{F:\Phi_i(F)\ge aQ\}.
\tag{5.41}
\]

On the complement of `E_i`, one has `Phi_i^2<aQ Phi_i`, while everywhere
`Phi_i^2<=Q^2`.  Therefore

\[
\begin{aligned}
 c_2\xi_iQ^2
 &\le\mathbb E_U\Phi_i^2\\
 &\le aQ\mathbb E_U\Phi_i+Q^2U(E_i)\\
 &\le {c_2\over2}\xi_iQ^2+Q^2U(E_i),
\end{aligned}
\tag{5.42}
\]

and hence

\[
                         U(E_i)\ge {c_2\over2}\xi_i.
\tag{5.43}
\]

By definition, `E[Phi_i|E_i]>=aQ`; moreover (5.39), (5.41), and (5.43)
give

\[
 \beta_i={U(E_i)\mathbb E[\Phi_i\mid E_i]
                   \over\mathbb E\Phi_i}
 \ge {c_2^2\over4C_1^2}.
\tag{5.44}
\]

Thus Theorem 5.3 applies with constants

\[
                         a={c_2\over2C_1},qquad
                         \beta_0={c_2^2\over4C_1^2}.
\tag{5.45}
\]

For (5.40), square the exact score identity (4.16) and average:

\[
 \mathbb E_U\Phi_i^2
 ={1\over4b^2Z}
   \sum_{T,U\in\mathcal H_i}X(T,U).
\tag{5.46}
\]

This makes the second inequality in (5.39) exactly (5.40). `square`

The scale in (5.39) is extremal but natural.  Since
`Phi_i^2<=Q Phi_i`, a mean of order `xi_iQ` permits at most order
`xi_iQ^2` for the second moment.  Corollary 5.4 asks for a fixed fraction
of that maximum, which is precisely the statement that current hole
incidences are vertically clustered on rows rather than dispersed like
independent holes.  The lower second moment also forces

\[
 c_2\xi_iQ\le\mathbb E_U\Phi_i\le C_1\xi_iQ,
 \qquad
 {2c_2b\over A}\le\bar p_i\le {2C_1b\over A},
\tag{5.47}
\]

using `Phi_i^2<=Q Phi_i` and
`bar p_i=2b E Phi_i/(xi_iAQ)`.  Thus (5.38)--(5.39) include the required
average external-degree floor and, through (5.38), an absolute maximum
degree bound of order `b/A`; neither is silently assumed later.

## 6. Rounding and exact scope

If (2.5), (3.2), or (4.3) holds outside `o(A)` aggregate holes, or if the
peeling theorem produces the summed cover in (5.4), the fractional cover
has mass `O(xB)`.  The independent rounding theorem of Appendix C.10,
with multiplier `3 log r`, then gives

\[
                         O(x\log r\,B)
\tag{6.1}
\]

physical rows and leaves only `o(A)` aggregate holes, provided
`x log r=o(1)`.  Labelled copies may be coalesced after sampling; coverage
is unchanged and the number of physical rows can only decrease.

To invoke the second bullet of Gate B in the master handoff, take
`Q=ceil(sqrt(b log b))`, let `Omega` be the physical coalescence of the
admissible restored rows from the one actual stopped catalogue `C`, and
apply every peeling law on that same `Omega`.  One must also prove
`|H_0|=O(xAQ)` and the stated stagewise hypotheses.  If instead `Q` is only
the C.9 shallow cutoff, the results above cover only that shallow subfamily
and do not prove Gate B.

The existing zero-avoidance statements H.11, H.15, and H.16 do not by
themselves establish either the one-shot criteria (3.2), (4.3), or the
aggregate peeling hypotheses (5.20a), (5.35):

1. H.11 is a fixed-harmonic, signed local affine identity;
2. H.15 bounds a fixed-harmonic remote shore difference, not a positive
   rooted likelihood ratio;
3. H.16 localizes a specified bounded family of Venn-gap terms, not the
   complete terminal survivor law;
4. none of them supplies a vertically rich event of survivor probability
   `Omega(xi)` through all `Q` depths, the one-sided constant-factor
   maximum-degree cap on the current holes, or the required stopped
   transfer.

They could contribute to a proof of the tangent in (4.2) or to the degree
cap in (5.20a), but transfer to the stopped catalogue and the
positive vertical-event probability remain unproved.

The most concrete scalar positive frontier isolated here is: prove the
one-sided cap (5.38) and the two estimates (5.39)
with fixed constants at every geometric residual scale.  Corollary 5.4,
Theorem 5.3, and geometric peeling then create the targetwise fractional
cover automatically.  The event form (5.20a), (5.35) and the one-shot
alternatives (3.2), (4.3) remain valid when that information is more
accessible.  In every formulation, the factor `1/x` may be shared between
dynamic relative protection and vertical survivor clustering; it need not
be charged entirely to either mechanism alone.
