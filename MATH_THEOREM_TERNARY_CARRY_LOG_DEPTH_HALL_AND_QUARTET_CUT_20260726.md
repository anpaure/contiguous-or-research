# The logarithmic-depth Hall and quartet cut for the ternary-carry macrocells

Date: 2026-07-26

Method: pure mathematics only. No computation, search, solver, or web input
is used.

## 0. Verdict

The present phase-dense ternary-carry construction cannot be inserted into
the physical candidate-degree lower-tail theorem: it fails that theorem's
shadow-injectivity hypothesis.  Its correct actual-menu support analogue has
a linear Hall deficit at one logarithmic depth, long before the Gaussian
depths.

Let

\[
 W=\binom{2m}{m},\qquad
 N_q=\binom{2m}{m-q},
\tag{0.1}
\]

and let \(t\) be a power of two, \(h=2t=o(m)\).  Assume

\[
 H\le t<2H,
 \qquad H\longrightarrow\infty,
\tag{0.2}
\]

as in the phase-dense construction.  All but \(u\) middle owners lie in
canonical first-\(t\)-eligible-block
macrocells of size \(24^t\), where, for some absolute \(c>0\),

\[
                         u\le e^{-cm}W.
\tag{0.3}
\]

For the present ternary-carry successor and every proved legal
whole-macrocell block-permutation/affine conjugate which preserves the
six-fibre port structure--and, more generally, every literal cellwise
affine menu option having a common-order Hamming reference and the same
sparse carry-tail ledger--put

\[
 q_*:=\left\lceil2\log_2h\right\rceil.
\tag{0.4}
\]

Then, for both signs,

\[
 \boxed{
 M_{q_*}^-=W-o(W),\qquad M_{q_*}^+=W-o(W).}
\tag{0.5}
\]

The same support conclusion holds for every convex combination or
correlated distribution of the binary target-support vectors of one legal
conjugate per macrocell.  In particular, the aggregate unit-demand support
lower tail at this depth is

\[
 \boxed{
 \sum_T(1-\lambda_{q_*}^\epsilon(T))_+
 =W-o(W),}
\tag{0.6}
\]

where \(\lambda\) is the fractional physical target-support load.

This is not a failure of the geometric face census.  The formula

\[
                         \lambda(T)={2^q\over\binom hq}d_q(T)
\tag{0.7}
\]

from the affine candidate-degree theorem assumes a depth-\(q\)
shadow-injective factor in every \(Q_h\)-cell.  The carry is instead a
sparse perturbation of parallel common-order Hamming factors and is very
far from shadow-injective at \(q_*\).  Thus (0.7) cannot be specialized to
the carry.  The correct macrocell support function has total mass only
\(o(W)\), which gives (0.6) directly.

The antipodal quartet issue does not rescue the construction.  The current
carry theorem does not prove that the recursive-factor antipodal quartets
survive its base-three switches.  Even if one grants the most favorable
possible quotient of all lower and upper targets into atoms of size at most
four, the quotient still has \(\Omega(W)\) uncovered atoms at \(q_*\).

Consequently the present carry factor, its proved legal whole-macrocell
affine orbit, and every orthogonal array formed from that orbit fail the
weighted-balanced completion gate and cannot by themselves prove
coefficient one.
The obstruction does not rule out a new ternary fusion built directly on a
trace-rainbow recursive factor.  Such a construction requires a new common
port-coordinate theorem after independent affine refreshing.

## 1. Source facts from the ternary-carry construction

One canonical macrocell is

\[
                         \mathcal M\cong\mathcal V^t,
 \qquad |\mathcal V|=24,
\tag{1.1}
\]

and therefore

\[
                         |\mathcal M|=24^t=6^t2^h.
\tag{1.2}
\]

The static all-new shore partitions \(\mathcal M\) into \(6^t\)
physical \(Q_h\)-cells.  In every cell the factor is the parallel Hamming
factor with common cyclic direction order

\[
 (\alpha_1,\ldots,\alpha_t,
  \beta_1,\ldots,\beta_t)
\tag{1.3}
\]

repeated twice.

The adjacent-port holonomy consists of two three-cycles.  The conditional
port choices implement addition by one on \(\mathbb Z/3^t\mathbb Z\),
giving fused cycles of length \(2h3^t\).  Relative to the static all-new
successor \(F_0\), the carry successor \(F_{\rm car}\) changes exactly

\[
 \boxed{
 e_{\mathcal M}
 ={3(1-3^{-t})\over4h}|\mathcal M|}
\tag{1.4}
\]

outgoing edges.

Every proved legal whole-macrocell block permutation or affine phase
conjugacy which preserves the six-fibre ports sends
\((F_{\rm car},F_0)\) to a pair with the same edge-change count and the
same common-order reference structure.  More generally, all results below
apply to any legal menu alternative \(F\) for which there is such a
reference \(F_0(F)\) and the difference set has size at most (1.4).

The word "whole-macrocell" is essential.  Independent affine recursive
factors in the \(6^t\) constituent cells do give local shadow injectivity,
but the present carry theorem supplies no common phase/syndrome fibres for
those independent factors.  They are not legal alternatives in the proved
carry construction.

## 2. Two support lemmas

For a successor permutation \(F\) on a middle-owner set, define its signed
depth-\(q\) targets by

\[
 \tau_{q,F}^-(x)=\bigcap_{j=0}^qF^j(x),
 \qquad
 \tau_{q,F}^+(x)=\bigcup_{j=0}^qF^j(x).
\tag{2.1}
\]

### Lemma 2.1 (common-order support bound)

Suppose \(P\) is partitioned into \(L\) physical \(Q_h\)-cells and, within
each cell, all components of \(F_0\) share a single cyclic order of the
\(h\) directions.  The common order may depend on the cell.  Then, for
either sign and \(1\le q<h\),

\[
 \boxed{
 |\operatorname {im}\tau_{q,F_0}^\epsilon|
 \le Lh2^{h-q}.}
\tag{2.2}
\]

#### Proof

One common cyclic order exposes at most \(h\) direction sets for a
length-\(q\) window.  Once its direction set is fixed, an affine
\(q\)-face has \(2^{h-q}\) possible outside orientations.  Both the lower
intersection and the upper union are determined by that affine face.
Thus one cell supplies at most \(h2^{h-q}\) distinct targets.  Sum over
the cells; physical coincidences between cells only reduce the image.
\(\square\)

### Lemma 2.2 (stability under changed outgoing edges)

Let \(F,F_0:P\to P\) be permutations and put

\[
                         D=\{x:F(x)\ne F_0(x)\},
 \qquad e=|D|.
\tag{2.3}
\]

Then, for every \(q\ge1\) and either sign,

\[
 \boxed{
 |\operatorname {im}\tau_{q,F}^\epsilon|
 \le |\operatorname {im}\tau_{q,F_0}^\epsilon|+qe.}
\tag{2.4}
\]

#### Proof

Let \(A_q\) be the starts whose first \(q\) outgoing \(F\)-edges contain
a tail in \(D\).  For prescribed \(y\in D\) and lag
\(j\in\{0,\ldots,q-1\}\), the unique possible start is \(F^{-j}(y)\).
Hence

\[
                              |A_q|\le qe.
\tag{2.5}
\]

If \(x\notin A_q\), induction gives
\(F^j(x)=F_0^j(x)\) for \(0\le j\le q\), so its target already occurs in
the \(F_0\)-image.  Each member of \(A_q\) creates at most one additional
distinct target.  This proves (2.4).  \(\square\)

## 3. Exact macrocell support bound

Apply Lemma 2.1 to the \(6^t\) static \(Q_h\)-cells and Lemma 2.2 with
(1.4).  For every legal menu alternative \(F\), every
\(1\le q<h\), and either sign,

\[
\begin{aligned}
 |\operatorname {im}\tau_{q,F}^\epsilon|
 &\le6^th2^{h-q}+qe_{\mathcal M}\\
 &=|\mathcal M|
   \left(
      {h\over2^q}
      +{3q(1-3^{-t})\over4h}
   \right).
\end{aligned}
\tag{3.1}
\]

Put

\[
 \eta_{h,q}
 ={h\over2^q}+{3q(1-3^{-t})\over4h}.
\tag{3.2}
\]

Thus

\[
 \boxed{
 \max_{F\in\mathfrak G_{\mathcal M}}
 |\operatorname {im}\tau_{q,F}^\epsilon|
 \le |\mathcal M|\eta_{h,q}.}
\tag{3.3}
\]

This is a count of distinct physical targets.  It is not merely a
direction-support or type-profile estimate.

The estimate also survives auxiliary cycle splicing.  If
\(\widetilde F\) differs from a legal carry option \(F\) on \(a_{\mathcal
M}\) further outgoing tails, then the difference set between
\(\widetilde F\) and the common-order reference has size at most
\(e_{\mathcal M}+a_{\mathcal M}\).  The same proof gives

\[
 \boxed{
 |\operatorname {im}\tau_{q,\widetilde F}^\epsilon|
 \le |\mathcal M|\eta_{h,q}+qa_{\mathcal M}.}
\tag{3.4}
\]

## 4. The all-target weighted cut

Let the good-owner mass be

\[
                         G=W-u,
\tag{4.1}
\]

partitioned into the canonical macrocells.  At a fixed signed depth, choose
one menu alternative in every macrocell.  We shall also use the convex
relaxation of the resulting **binary target-support vectors**.  The
remaining \(u\) owners are completed disjointly.  If a completion instead
splices through good-owner edges, its changed good tails are governed by
(3.4).

For a fractional choice \(x_{\mathcal M,F}\), define its physical support
load by

\[
 \lambda_q^\epsilon(T)
 =\sum_{\mathcal M}\sum_{F\in\mathfrak G_{\mathcal M}}
 x_{\mathcal M,F}
 \mathbf1_{\{T\in\operatorname {im}\tau_{q,F}^\epsilon\}},
 \qquad
 \sum_Fx_{\mathcal M,F}=1.
\tag{4.2}
\]

Equation (3.3) gives

\[
\begin{aligned}
 \sum_T\lambda_q^\epsilon(T)
 &=\sum_{\mathcal M,F}x_{\mathcal M,F}
       |\operatorname {im}\tau_{q,F}^\epsilon|\\
 &\le G\eta_{h,q}.
\end{aligned}
\tag{4.3}
\]

Allow the \(u\) bad owners to hit distinct additional targets.  Since
\((1-z)_+\ge1-z\) for \(z\ge0\),

\[
 \boxed{
 \sum_{T\in\mathcal T_q^\epsilon}
       (1-\lambda_q^\epsilon(T))_+
 \ge N_q-G\eta_{h,q}-u.}
\tag{4.4}
\]

Equivalently, in the weighted Hall dual take weight one on every target of
this signed rank.  The demand side is \(N_q\); the support function of all
macrocell menus, plus the arbitrary bad-owner completion, is at most
\(G\eta_{h,q}+u\).  Therefore (4.4) is valid for arbitrary correlations
among the choices and is already an obstruction to the fractional
binary-support cover relaxation.

For an integral choice, the number of distinct hit targets is at most the
same right-hand support, and hence

\[
 M_q^\epsilon
 \ge N_q-G\eta_{h,q}-u.
\tag{4.5}
\]

There is an important distinction here.  The looser fractional
**occurrence** LP has columns

\[
 n_{\mathcal M,F}(T)
 =|\{x\in\mathcal M:\tau_{q,F}^\epsilon(x)=T\}|,
 \qquad
 \sum_T n_{\mathcal M,F}(T)=|\mathcal M|.
\tag{4.6}
\]

The all-one target weight therefore evaluates every occurrence column at
\(|\mathcal M|\), so it does not separate that LP: multiplicity on an
already hit target supplies its full column mass.  No fractional
occurrence-LP obstruction is claimed.  This does not weaken the integral
conclusion, because an integral balanced realization must physically hit
every target whose floor quota is one; repeated occurrences cannot repair
an absent target.

## 5. Evaluation at the logarithmic depth

For \(q_*\) from (0.4),

\[
 {h\over2^{q_*}}\le{1\over h},
 \qquad
 {3q_*(1-3^{-t})\over4h}
 =O\left({\log h\over h}\right),
\tag{5.1}
\]

so

\[
                         \eta_{h,q_*}=o(1).
\tag{5.2}
\]

By (0.2), \(2H\le h<4H\), and hence \(q_*\le H\) for all sufficiently
large \(H\).  Also \(q_*=O(\log h)=o(\sqrt m)\).  The exact adjacent-rank
product is

\[
 {N_q\over W}
 =\prod_{j=0}^{q-1}{m-j\over m+j+1}.
\tag{5.3}
\]

Uniformly for \(q=o(\sqrt m)\), taking logarithms gives

\[
 \log{N_q\over W}
 =-{q^2\over m}+O\left({q\over m}+{q^3\over m^2}\right).
\tag{5.4}
\]

Thus

\[
                         N_{q_*}=W-o(W).
\tag{5.5}
\]

Substitution of (0.3), (5.2), and (5.5) in (4.4)--(4.5) proves
(0.5)--(0.6).  Since \(W/N_{q_*}=1+o(1)\) and
\(W-N_{q_*}\gg u\), the balanced floor demand at this depth is indeed one
per target.

More explicitly, let \(n_T\) be the signed depth-\(q_*\) occurrence
histogram after a globally depth-\(q_*\)-geodesic integral completion, as
every admissible literal construction must be.  Then \(\sum_Tn_T=W\); a
nongeodesic completion already fails the required signed-rank condition.
Let
\(S=|\{T:n_T>0\}|\).  Write \(a\) for the number of outgoing tails of
good macrocell factors rewired by that completion; thus \(a=0\) for a
disjoint completion.  Equations (3.4) and (0.3) give

\[
                         S\le G\eta_{h,q_*}+u+q_*a.
\tag{5.6}
\]

Consequently, if \(q_*a=o(W)\), then \(S=o(W)\).  For any exact balanced
baseline \(b_T\in\{1,2\}\) with \(\sum_Tb_T=W\),

\[
 \sum_T(b_T-n_T)_+
 \ge |\{T:n_T=0\}|
 =N_{q_*}-S
 =W-o(W).
\tag{5.7}
\]

The two histograms have equal total mass, hence

\[
 \boxed{
 \sum_T(n_T-b_T)_+
 =\sum_T(b_T-n_T)_+
 =W-o(W).}
\tag{5.8}
\]

Thus the actual integral balanced overload is linear, not merely the
number of missing physical targets.  In particular, this applies after any
auxiliary splicing with
\(\sum_{\mathcal M}a_{\mathcal M}=o(W/q_*)=o(W/\log h)\).

## 6. Why the affine candidate-degree theorem does not apply

Fix the static all-new shore decomposition of every good macrocell, and let
\(\mathscr C\) be the resulting physical \(Q_h\)-cell atlas.  Its size is

\[
                         |\mathscr C|={G\over2^h}.
\tag{6.1}
\]

For an actual physical target \(T\), the geometric degree used in the
affine candidate theorem is exactly

\[
 d_q^\epsilon(T)
 =\#\{c\in\mathscr C:
       T\text{ is the }\epsilon\text{-trace of an affine }q
       \text{-face of }c\}.
\tag{6.2}
\]

Equivalently, write a cell as

\[
 c=\left\{C_c\cup\{e_i^{x_i}:1\le i\le h\}:
              x\in\mathbb F_2^h\right\},
 \qquad E_i=\{e_i^0,e_i^1\}.
\]

Its contribution to \(d_q^-(T)\) is one exactly when there are
\(D\in\binom{[h]}q\) and
\(y\in\mathbb F_2^{[h]\setminus D}\) such that

\[
 T=C_c\cup\{e_i^{y_i}:i\notin D\};
\tag{6.2a-}
\]

its contribution to \(d_q^+(T)\) is one exactly when

\[
 T=C_c\cup\bigcup_{i\in D}E_i
       \cup\{e_i^{y_i}:i\notin D\}.
\tag{6.2a+}
\]

Thus (6.2a\(\pm\)) is a pointwise physical formula; its only unresolved
input is how many different canonical macrocells realize that displayed
core-and-pair pattern for the same \(T\).

Local six-cell face separation implies that one fixed macrocell contributes
at most one to (6.2).  Different canonical macrocells can contribute to the
same target, so their incidences add.  Counting all affine faces gives the
exact aggregate

\[
 \boxed{
 \sum_Td_q^\epsilon(T)
 ={G\over2^h}\binom hq2^{h-q}
 =G{\binom hq\over2^q}.}
\tag{6.3}
\]

This is the complete unconditional candidate-degree computation available
from the first-eligible-block macrocell theorem.  A pointwise formula would
require the cross-macrocell exterior-incidence census, but the cut below
does not need it.

For one shadow-injective recursive factor in a physical \(Q_h\)-cell, the
full labeled affine menu has incidence fraction

\[
                         p_{h,q}={2^q\over\binom hq}
\tag{6.4}
\]

on each geometric candidate face.  This uses the fact that the factor
selects \(2^h\) distinct affine \(q\)-faces, one at each start.  It leads
to the exact full-menu degree

\[
 \deg_{\Gamma_h}(q,\epsilon,T)
 =|\Gamma_h|{2^q\over\binom hq}d_q^\epsilon(T),
 \qquad \Gamma_h=\mathbb F_2^h\rtimes S_h,
\tag{6.4a}
\]

and hence to the barycentric physical load

\[
                         \lambda(T)=p_{h,q}d_q(T).
\tag{6.5}
\]

Equations (6.3)--(6.5) give \(\sum_T\lambda(T)=G\), exactly the required
total occurrence mass.  But this calculation is legal only because a
recursive factor selects \(2^h\) distinct affine \(q\)-faces, one at each
start.

The static Hamming factor in one carry cell has \(2^h\) starts but at most
\(h2^{h-q}\) distinct faces.  At \(q_*\), this is only an \(O(1/h)\)
fraction of its starts.  The carry changes only the fraction

\[
                         {e_{\mathcal M}\over|\mathcal M|}
 =O(1/h)
\tag{6.6}
\]

of outgoing edges, and (3.1) shows that its physical image remains
\(O((\log h)/h)|\mathcal M|\).

Consequently the geometric degree \(d_q(T)\) is not the actual carry-menu
support incidence.  A geometric face can be available in the underlying
cubes while no carry alternative selects it at the required consecutive
phase.  For chosen fractional weights, the correct target-specific support
load is

\[
 r_{\mathcal M,q}^\epsilon(T)
 =\sum_{F\in\mathfrak G_{\mathcal M}}
    x_{\mathcal M,F}
    \mathbf1_{\{T\in\operatorname {im}\tau_{q,F}^\epsilon\}},
\tag{6.7}
\]

and (4.3) computes its complete aggregate bound:

\[
 \boxed{
 \sum_T\sum_{\mathcal M}r_{\mathcal M,q_*}^\epsilon(T)
 \le O\left({\log h\over h}\right)W=o(W).}
\tag{6.8}
\]

Thus the geometric lower tail \(\sum_T(1-p_{h,q}d_q(T))_+\) has not been
computed and is not claimed large.  Rather, the actual carry-menu support
lower tail is \(W-o(W)\).  Passing from block-permutation balance to the
proved legal whole-macrocell affine orbit only relabels each small trace
image and cannot change this all-target support cut.

## 7. Inseparable lower/upper-antipodal quartets

For the recursive \(Q_h\)-factor, the two traces of one face and its
antipodal translate form the local incidence atom

\[
 L(R),\quad U(R),\quad L(R+\mathbf1),\quad U(R+\mathbf1).
\tag{7.1}
\]

The present ternary-carry theorem proves only the odometer identity after a
full \(2h\)-phase lap.  It does not prove a commuting physical antipode or
the half-period identity needed to retain (7.1).  Hence importing the
quartet quotient from the recursive factor would itself be an unjustified
step.

There is an occurrence-level remnant.  For one carry option \(F\), let
\(F_0\) be its static reference, let \(A_0=F_0^h\) be the static cube
antipode, and let \(B_q\) be the starts whose \(F\)-window meets a changed
tail.  Lemma 2.2 gives

\[
                         |B_q|\le qe_{\mathcal M}.
\tag{7.1a}
\]

The set

\[
 P_{\rm stab}
 =\mathcal M\setminus(B_q\cup A_0B_q)
\tag{7.1b}
\]

is \(A_0\)-invariant and has size at least
\(|\mathcal M|-2qe_{\mathcal M}\).  For every \(x\in P_{\rm stab}\),
the windows from \(x\) and \(A_0x\) agree with their static windows and
therefore form the usual lower/upper-antipodal quartet.  This pairs almost
all occurrences when \(q=q_*\), but it does not create global
incidence-twin target classes: different macrocells and different menu
options may attach different partners to the same physical target.

There is nevertheless a quotient-robust obstruction.  Let

\[
 \mathcal T_q=\mathcal T_q^-\mathbin{\dot\cup}\mathcal T_q^+,
 \qquad |\mathcal T_q|=2N_q,
\tag{7.2}
\]

and grant an arbitrary surjective quotient map

\[
                         \pi:\mathcal T_q\to\mathcal A
\tag{7.3}
\]

whose fibres have size at most four.  Declare an atom hit whenever any one
of its members is hit.  This convention is more favorable than genuine
quartet incidence.  It gives

\[
                         |\mathcal A|\ge{N_q\over2}.
\tag{7.4}
\]

For one integral macrocell choice, the number of hit atoms is at most the
number of hit tagged targets.  Equations (3.3) for the two signs therefore
bound it by

\[
                         2|\mathcal M|\eta_{h,q}.
\tag{7.5}
\]

For a fractional choice, define the atom-support load

\[
 \lambda_A
 =\sum_{\mathcal M,F}x_{\mathcal M,F}
   \mathbf1_{\{A\cap(\operatorname {im}\tau_{q,F}^-
                    \cup\operatorname {im}\tau_{q,F}^+)\ne\varnothing\}},
\tag{7.6}
\]

and include the bad-owner completion in the same load.  Summing (7.5)
over the fractional choices gives

\[
                         \sum_{A\in\mathcal A}\lambda_A
 \le2G\eta_{h,q}+2u.
\tag{7.7}
\]

Therefore

\[
 \boxed{
 \sum_{A\in\mathcal A}(1-\lambda_A)_+
 \ge {N_q\over2}-2G\eta_{h,q}-2u.}
\tag{7.8}
\]

At \(q=q_*\), the right side is \(W/2-o(W)\).  For an integral choice,
the left side of (7.8) is exactly the number of uncovered quotient atoms.
Thus (7.8) applies to integral choices, correlated distributions, and the
fractional binary-support relaxation.

If an integral literalization additionally rewires \(a\) good outgoing
tails, the right side of (7.8) decreases by at most \(2qa\).  Hence the
same quartet cut survives whenever \(qa=o(W)\).

Thus lower/upper-antipodal inseparability cannot absorb the deficit; even
an arbitrary favorable four-to-one quotient leaves a linear cut.

## 8. Exact boundary and required replacement

The proved obstruction covers:

1. the current ternary-carry successor;
2. arbitrary proved legal block permutations and affine phase conjugacies
   applied to the whole macrocell construction while preserving its
   six-fibre ports;
3. every legal menu alternative which remains an
   \(e_{\mathcal M}\)-edge perturbation of a parallel common-order
   reference;
4. integral choices, randomized or globally correlated distributions, and
   fractional convex combinations of their binary support vectors (but
   not the looser occurrence-multiplicity LP); and
5. every quotient into lower/upper-antipodal atoms of size at most four.

It does not cover independently refreshed recursive factors in the
constituent \(Q_h\)-cells, because the base-three carry has not been proved
compatible with those factors.  This is the smallest surviving replacement
statement:

> **Affine-rainbow carry compatibility — UNPROVED.**  Construct a
> whole-owner-fibre ternary fusion on the recursive trace-rainbow factors
> such that independent or candidate-fibre-balanced affine conjugacies
> retain a common six-point port coordinate, produce \(o(24^t/H)\)
> components, and preserve simultaneous two-sided shadow injectivity or
> weighted physical Hall expansion through \(q\le H\).

Any repair which remains a perturbation of a common-order reference must
also change many more edges.  At \(q_*\), Lemma 2.2 shows that a macrocell
required to create \(\Theta(|\mathcal M|)\) distinct targets needs

\[
                         e=\Omega(|\mathcal M|/q_*)
 =\Omega(24^t/\log h)
\tag{8.1}
\]

changed outgoing edges per macrocell.  The current carry changes only
\(\Theta(24^t/h)\).

Without a homogeneity assumption, the unconditional global form is

\[
 \sum_{\mathcal M}e_{\mathcal M}
 =\Omega(W/q_*)=\Omega(W/\log h).
\tag{8.2}
\]

Indeed, summing Lemmas 2.1--2.2 at \(q_*\) gives total signed support at
most \(G/h+q_*\sum_{\mathcal M}e_{\mathcal M}\); covering
\(\Theta(W)\) distinct targets forces (8.2).  Thus the average required
edit count is \(\Omega(24^t/\log h)\), although edits may be distributed
unevenly.  The current carry has total edit count \(\Theta(W/h)\), which
is asymptotically too small.  No claim of MWB or coefficient one is made.

## 9. Adversarial audit

The proof has been checked against the following potential escapes.

1. **Different orders in different components.**  Lemma 2.1 would be
   false if components inside one \(Q_h\)-cell could use unrelated cyclic
   direction orders.  The audited static shore has one shared order in
   every cell.  A recursive trace-rainbow replacement falls outside the
   lemma and is precisely the surviving hypothesis in Section 8.

2. **Fractional multiplicity.**  The all-target support weight does not
   separate the occurrence-multiplicity LP; (4.6) records this explicitly.
   The theorem's no-go is integral (and, separately, valid for the stronger
   binary-support convexification).

3. **Hidden completion switches.**  A completion that changes good tails
   is not charged to the exceptional owner set.  Equations (3.4) and (5.6)
   charge every such tail and show that \(\Omega(W/\log h)\) of them are
   necessary to evade the cut.

4. **Geometric affine availability.**  Equations (6.2a\(\pm\))--(6.4a)
   compute the genuine geometric menu incidence.  They do not imply carry
   incidence because the carry is not shadow-injective; no lower-tail claim
   about \(p_{h,q}d_q(T)\) is used.

5. **Antipodal identification.**  No global quartet relation is assumed.
   Section 7 first isolates the only proved stable occurrence pairs and
   then grants an arbitrary, maximally favorable four-to-one target
   quotient.  The remaining \(W/2-o(W)\) cut is therefore insensitive to
   the unresolved physical quartet matching.

These checks leave the logarithmic-depth cut intact, but only for the
common-order sparse-carry class stated above.
