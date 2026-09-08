# Fifth-wave lane Z: positive corridor optimum via involution-bundle augmentation

Date: 2026-07-25

Method: pure mathematics only.  No web search, finite search, computation,
random experiment, or signed/fractional endpoint is used.

## 0. Verdict

The Z3 free-quota corridor admits a concrete positive-fibre augmentation
theorem which is strictly more informative than generic
\(M\)-convexity or comparison with an unknown better factor.

Let

\[
n=2m+1,\qquad
W=\binom nm,\qquad
B=\frac Wn=\operatorname{Cat}_m,\qquad
H=\lceil A\sqrt m\rceil ,
\]

where \(A>0\) is fixed and \(m\) is sufficiently large that
\(H\le m-2\).  For an exact factor \(F\), compare \(F\) with
\(\sigma F\), where \(\sigma\) is a fixed-point involution of cycle type
\(1\,2^m\).  Cancel common wreaths, form the genuine ownership components,
and bundle every orbit of components under \(\sigma\).  Every common
signing of these bundles is one binary positive exact factor.

For every moved target pair \(p=\{S,\sigma S\}\) at depth \(q\), let
\(M_p\) be its fixed total load and let
\(D_p(\varepsilon)\) be its signed load difference under a bundle signing.
The exact pair corridor is

\[
\boxed{
h_{c_q,M_p}(D)
=
\max\{b_{c_q}(M_p),\,|D|-1\},
}
\tag{0.1}
\]

where

\[
b_c(M)=(2c-M)_+ +(M-2c-2)_+.
\tag{0.2}
\]

This gives the exact positive-cell decomposition

\[
\boxed{
\min_{\varepsilon}
\mathcal C_H(F^\sigma_\varepsilon)
=
\mathcal M_\sigma(F)
+\operatorname{Lock}_\sigma(F)
+\operatorname{Sync}_\sigma(F).
}
\tag{0.3}
\]

Here \(\mathcal M_\sigma\) is the real midpoint corridor,
\(\operatorname{Lock}_\sigma\) is the loss from indivisible component-row
coefficients, and \(\operatorname{Sync}_\sigma\) is the exact additional
loss from requiring one common bundle signing for all targets and depths.
Consequently the steepest legal gain in this concrete cell is exactly

\[
\boxed{
\Gamma_\sigma(F)
=
I_\sigma(F)
-\operatorname{Lock}_\sigma(F)
-\operatorname{Sync}_\sigma(F)\ge0,
}
\tag{0.4}
\]

where

\[
I_\sigma(F)=\mathcal C_H(F)-\mathcal M_\sigma(F)
\]

is the ideal Jensen-smoothing gain.

Every positive corridor has a strict ideal direction:

\[
\boxed{
\mathcal C_H(F)>0
\quad\Longrightarrow\quad
\max_{\sigma\in\mathcal I_m} I_\sigma(F)>0.
}
\tag{0.5}
\]

Indeed, any two equal-rank targets can be exchanged by some
\(\sigma\in\mathcal I_m\), and one can choose a low/high or
floor/high target pair whose midpoint balancing gains at least one
unweighted unit.  Thus a positive exact-factor optimum can survive only by
restituting every strict Jensen direction through genuine ownership locking
or common-sign synchronization.

Both residues have explicit upper bounds.  If \(z_{pK}\) is the action of
bundle \(K\) on target pair \(p\), put

\[
\operatorname{Frag}_\sigma
=
\sum_p\frac{
(\max_K|z_{pK}|-1-b_{c_q}(M_p))_+
}{c_q}.
\tag{0.6}
\]

Then

\[
\operatorname{Lock}_\sigma\le\operatorname{Frag}_\sigma.
\]

For the preferred-sign target--bundle incidence graph, let
\(\delta_\sigma\) be its vector synchronization defect and let

\[
S_\sigma
=
\sum_{p,K}\frac{2|z_{pK}|}{c_q}.
\]

Hyperplane rounding gives

\[
\operatorname{Sync}_\sigma
\le\sqrt{S_\sigma\delta_\sigma},
\qquad
S_\sigma
\le2W\sum_{q\le H}\frac1{c_q}
\le2HW.
\tag{0.7}
\]

Therefore

\[
\boxed{
\Gamma_\sigma(F)
\ge
I_\sigma(F)
-\operatorname{Frag}_\sigma(F)
-\sqrt{S_\sigma(F)\delta_\sigma(F)}.
}
\tag{0.8}
\]

The fixed-point-involution spectrum yields a completely explicit
level-set lower bound \(\operatorname{Mix}(F)\) for the average ideal gain.
It follows that

\[
\boxed{
\max_{\sigma,\varepsilon}
\bigl[
\mathcal C_H(F)-\mathcal C_H(F^\sigma_\varepsilon)
\bigr]
\ge
\left[
\operatorname{Mix}(F)
-\mathbb E_\sigma\operatorname{Frag}_\sigma(F)
-\mathbb E_\sigma\sqrt{S_\sigma(F)\delta_\sigma(F)}
\right]_+.
}
\tag{0.9}
\]

Every comparison in (0.9) has at most \(\lfloor B/2\rfloor\) underlying
ownership components.  If its right side is \(g>0\), Z3 atomic splitting
produces a genuine support-feasible corridor-atomic packet improving by at
least

\[
\boxed{
\frac g{\lfloor B/2\rfloor}\ge\frac{2g}{B}.
}
\tag{0.10}
\]

This is the requested steepest-descent/augmentation theorem under a
concrete legal trade family.

It does not yet bound the positive optimum.  The missing theorem is a
genuine ownership estimate showing that fragmentation and signed-cycle
synchronization cannot consume the involution mixing gain above the
\(HB=o(W)\) scale.  A precise such estimate would give
\(\mathcal C_H=O_A(HB)=o(W)\) after \(O_A(\log n)\) exact macrosteps.

There is also a genuine packet-local MSW example for which both the
corridor and mobile overload have the certified lower bound

\[
\left(\frac3{1024}+O(m^{-1})\right)B.
\]

The certificate is \(\Theta(B)=\Theta(W/m)=o(W)\).  No matching
\(O(B)\) upper bound on the local minimum is proved, and no
\(\Omega(W)\) weighted-overload lower bound is certified.

## 1. Exact-factor corridor setup

Throughout, \(q\le H\) in a sum means \(1\le q\le H\).  At such a depth,
put

\[
r_q=m-q,\qquad
N_q=\binom n{r_q},\qquad
W=c_qN_q+\rho_q,
\tag{1.1}
\]

where

\[
c_q=\left\lfloor\frac W{N_q}\right\rfloor\ge1,
\qquad
0\le\rho_q<N_q.
\]

For an exact factor \(F\), let

\[
\mu_q^F(S)
\]

be the number of selected wreaths which own the \(r_q\)-set \(S\) as a
cyclic interval.  Every rank load has total

\[
\sum_S\mu_q^F(S)=W.
\tag{1.2}
\]

Every exact factor has exactly \(B\) wreaths.  Indeed, each wreath owns
exactly \(n\) middle \(m\)-sets, while the exact-factor equations cover
all \(W\) middle sets once, so

\[
n|F|=W,\qquad |F|=B.
\tag{1.2a}
\]

For later comparison with the original balanced-overload objective, put

\[
D_q^-(F)=\sum_S(c_q-\mu_q^F(S))_+,
\qquad
D_q^+(F)=\sum_S(\mu_q^F(S)-c_q-1)_+,
\qquad
O_q(F)=\max\{D_q^-(F),D_q^+(F)\}.
\tag{1.2b}
\]

Define

\[
\chi_c(t)=\operatorname{dist}(t,\{c,c+1\})
=(c-t)_+ +(t-c-1)_+
\tag{1.3}
\]

for integral \(t\), and

\[
\boxed{
\mathcal C_H(F)
=
\sum_{q\le H}\frac1{c_q}
\sum_{S\in\binom{[n]}{r_q}}
\chi_{c_q}(\mu_q^F(S)).
}
\tag{1.4}
\]

Z3 proves, factorwise,

\[
\sum_{q\le H}\frac{O_q(F)}{c_q}
\le
\mathcal C_H(F)
\le
2\sum_{q\le H}\frac{O_q(F)}{c_q}.
\tag{1.5}
\]

Thus \(\min_F\mathcal C_H(F)=o(W)\) for every fixed \(A\) is equivalent,
up to the universal factor two, to fixed-window unlabelled overload and
hence to MWB by the frozen diagonalization theorem.

Put

\[
s_H=\sum_{q\le H}\frac1{c_q},
\qquad
L_H=\operatorname{lcm}(c_1,\ldots,c_H).
\tag{1.6}
\]

Every corridor value lies in \(L_H^{-1}\mathbb Z_{\ge0}\).  Also

\[
\boxed{
\mathcal C_H(F)\le2Ws_H\le2HW.
}
\tag{1.7}
\]

Indeed, at one depth the total deficit below \(c_q\) is at most
\(c_qN_q\le W\), and the total surplus above \(c_q+1\) is at most \(W\).

All objects below remain in the finite positive exact-factor fibre

\[
\mathcal X_m
=
\{x\in\{0,1\}^{\mathscr W_m}:A_mx=\mathbf1\}.
\tag{1.8}
\]

No rank is optimized independently of another.

## 2. Fixed-point involution bundle cells

Let \(\mathcal I_m\) be the conjugacy class of coordinate involutions of
cycle type \(1\,2^m\).  Fix \(F\in\mathcal X_m\) and
\(\sigma\in\mathcal I_m\).

Cancel the common wreaths of \(F\) and \(\sigma F\), and form the
middle-ownership overlay.  Let \(\mathscr K^0_\sigma(F)\) be its connected
components.  Switching either complete side of any collection of these
components preserves every middle-set equation and therefore gives an exact
factor.


The map \(\sigma\) swaps the two overlay sides and preserves middle-set
incidence, so it permutes \(\mathscr K^0_\sigma(F)\) in orbits of size one
or two.  Bundle the components in each orbit of this action.  If \(K\) is
such a bundle, let
\(K^+\) be the union of its \(F\)-sides and put

\[
K^-=\sigma K^+.
\tag{2.1}
\]

For every bundle signing

\[
\varepsilon\in\{\pm1\}^{\mathscr K_\sigma(F)},
\]

choose \(K^{\varepsilon_K}\) in each bundle and retain the common frozen
part.  Denote the resulting factor by

\[
F^\sigma_\varepsilon.
\tag{2.2}
\]

If there are no noncommon bundles, the signing set contains its unique
empty signing and every empty signed sum below is zero.  In the
fragmentation formula we also use the convention \(\max\varnothing=0\).

### Lemma Z5.1 -- positive legality and component count

Every \(F^\sigma_\varepsilon\) is a binary integral exact factor.
Moreover, the number \(k_\sigma(F)\) of underlying noncommon ownership
components satisfies

\[
\boxed{
k_\sigma(F)\le
\left\lfloor\frac{|F\setminus\sigma F|}{2}\right\rfloor
\le\left\lfloor\frac B2\right\rfloor.
}
\tag{2.3}
\]

#### Proof

Each bundle signing switches a union of complete ownership components, so
all middle-set equations remain exactly one and no wreath is used twice.
This proves positive exact-factor legality.

The two sides of each noncommon ownership component have equal cardinality.
Before cancellation every wreath vertex has degree \(n\) in the
middle-ownership graph.  A middle set owned by a common wreath on one side
has that same wreath as its unique owner on the other side, so canceling a
common wreath removes its whole matched block and leaves every noncommon
vertex of degree \(n\).  Counting component edges from the two sides gives
equality.

If a component had one wreath on each side, their two middle-incidence
columns would be equal.  To see that this forces the same unoriented
wreath, let \(d_C(u,v)\in\{1,\ldots,m\}\) be cyclic distance in a wreath
\(C\).  The number of owned middle intervals containing both \(u\) and
\(v\) is

\[
m-d_C(u,v).
\]

Thus the middle column determines all cyclic distances, in particular its
distance-one pairs, which are exactly the edges of the unoriented cycle.
Distinct unoriented wreaths therefore have distinct columns.  Since common
wreaths were already canceled, each noncommon component side has at least
two wreaths.  The old sides of distinct components partition
\(F\setminus\sigma F\), and \(|F|=B\), proving (2.3).  \(\square\)

This factor-two improvement over the generic \(B\)-component bound is the
reason for using noncommon component structure explicitly.

Fix a depth \(q\).  A target is fixed if \(\sigma S=S\); its load is
unchanged throughout the bundle cell.  For a moved target orbit

\[
p=(q,\{S,\sigma S\}),
\]

orient the pair as \(S,\sigma S\), and define

\[
z_{pK}
=
\#\{E\in K^+:E\text{ owns }S\}
-
\#\{E\in K^+:E\text{ owns }\sigma S\}.
\tag{2.4}
\]

Let

\[
M_p
=
\mu_q^F(S)+\mu_q^F(\sigma S).
\tag{2.5}
\]

Every child has this same pair total.  Put

\[
D_p(\varepsilon)=\sum_K\varepsilon_Kz_{pK}.
\tag{2.6}
\]

The frozen \(\sigma\)-invariant part contributes equally to the two
oriented targets, and \(K^-=\sigma K^+\) reverses the signed difference.
Therefore the two child loads are exactly

\[
\boxed{
\frac{M_p+D_p(\varepsilon)}2,
\qquad
\frac{M_p-D_p(\varepsilon)}2.
}
\tag{2.7}
\]

In particular, both quantities are integral for every allowed signing.

## 3. Exact pair normal form and restitution identity

Extend the scalar corridor to real arguments by

\[
\overline\chi_c(x)=\operatorname{dist}(x,[c,c+1]).
\tag{3.1}
\]

It agrees with \(\chi_c\) at every integer.

### Lemma Z5.2 -- exact two-target corridor

Let \(M,D\in\mathbb Z\) have the same parity, so that
\((M\pm D)/2\) are integral.  Then

\[
\boxed{
\begin{aligned}
h_{c,M}(D)
&:=
\chi_c\!\left(\frac{M+D}{2}\right)
+\chi_c\!\left(\frac{M-D}{2}\right)\\
&=
\max\{b_c(M),\,|D|-1\},
\end{aligned}
}
\tag{3.2}
\]

where

\[
\boxed{
b_c(M)
=(2c-M)_+ +(M-2c-2)_+
=2\overline\chi_c(M/2).
}
\tag{3.3}
\]

Consequently \(h_{c,M}\) is even as a function of \(D\), nondecreasing
in \(|D|\), and \(1\)-Lipschitz as a function of \(D\).

#### Proof

By symmetry assume \(D\ge0\), and put

\[
x=\frac{M+D}{2},
\qquad
y=\frac{M-D}{2},
\qquad x\ge y.
\]

If \(x\le c\), both loads are on or below the corridor and
\(h=2c-M\).  If \(y\ge c+1\), both are on or above the corridor and
\(h=M-2c-2\).  In every remaining crossing case, direct substitution gives
\(h=x-y-1=D-1\), except that a load already in the corridor contributes
zero and the same maximum formula remains valid.  These three cases are
exactly (3.2).

Alternatively, for integral \(t\),

\[
\chi_c(t)=\left|t-c-\frac12\right|-\frac12.
\]

Thus

\[
h_{c,M}(D)
=
\frac{
|M-(2c+1)+D|+|M-(2c+1)-D|
}{2}-1,
\]

and the identity

\[
\frac{|a+b|+|a-b|}{2}=\max\{|a|,|b|\}
\]

gives the same result.  Feasible parity guarantees that the displayed
quantity is nonnegative.  Formula (3.3) is the distance of the pair total
from the interval \([2c,2c+2]\).  The monotonicity and Lipschitz assertions
are immediate from (3.2).  \(\square\)

For each moved target pair, define its minimum signed discrepancy

\[
r_p
=
\min_{\eta\in\{\pm1\}^{\mathscr K_\sigma(F)}}
\left|\sum_K\eta_Kz_{pK}\right|.
\tag{3.4}
\]

Its exact targetwise minimum corridor is

\[
\min_\eta h_{c_q,M_p}(D_p(\eta))
=
\max\{b_{c_q}(M_p),r_p-1\}.
\tag{3.5}
\]

The signs attaining (3.4) come in antipodal pairs.

Define the real midpoint corridor

\[
\boxed{
\mathcal M_\sigma(F)
=
\sum_{q\le H}\frac1{c_q}
\sum_{S\in\binom{[n]}{r_q}}
\overline\chi_{c_q}\!\left(
\frac{\mu_q^F(S)+\mu_q^F(\sigma S)}2
\right).
}
\tag{3.6}
\]

This real midpoint is only the exact scalar lower floor for each conserved
pair total; it is never used as a fractional factor or as an endpoint.

At a fixed target this is its original corridor cost.  At a moved pair its
two equal midpoint terms sum to \(b_{c_q}(M_p)\).  Convexity gives the
nonnegative ideal Jensen gain

\[
\boxed{
I_\sigma(F)
=
\mathcal C_H(F)-\mathcal M_\sigma(F)\ge0.
}
\tag{3.7}
\]

Define the row-locking residue

\[
\boxed{
\operatorname{Lock}_\sigma(F)
=
\sum_p
\frac{
(r_p-1-b_{c_q}(M_p))_+
}{c_q}.
}
\tag{3.8}
\]

It is the exact loss between the real pair-total floor and the minimum
attainable by pair-dependent component signs.

Finally define the common-sign synchronization residue

\[
\boxed{
\operatorname{Sync}_\sigma(F)
=
\min_\varepsilon
\sum_p\frac{
h_{c_q,M_p}(D_p(\varepsilon))
-h_{c_q,M_p}(r_p)
}{c_q}.
}
\tag{3.9}
\]

Every summand is nonnegative by (3.4)--(3.5).

### Theorem Z5.3 -- exact positive-cell optimum

For every exact factor \(F\) and every
\(\sigma\in\mathcal I_m\),

\[
\boxed{
\min_{\varepsilon}
\mathcal C_H(F^\sigma_\varepsilon)
=
\mathcal M_\sigma(F)
+\operatorname{Lock}_\sigma(F)
+\operatorname{Sync}_\sigma(F).
}
\tag{3.10}
\]

Hence the exact steepest bundle-cell gain is

\[
\boxed{
\begin{aligned}
\Gamma_\sigma(F)
&:=
\mathcal C_H(F)
-\min_\varepsilon\mathcal C_H(F^\sigma_\varepsilon)\\
&=
I_\sigma(F)
-\operatorname{Lock}_\sigma(F)
-\operatorname{Sync}_\sigma(F)
\ge0.
\end{aligned}
}
\tag{3.11}
\]

If \(F\) is locally minimal in this entire bundle cell, then

\[
\boxed{
I_\sigma(F)
=
\operatorname{Lock}_\sigma(F)
+\operatorname{Sync}_\sigma(F).
}
\tag{3.12}
\]

In particular, every global corridor minimizer obeys (3.12) for every
\(\sigma\in\mathcal I_m\).

#### Proof

The fixed-target contribution is \(\mathcal M_\sigma\)'s fixed part.
For a moved pair, (3.3) contributes \(b_{c_q}(M_p)/c_q\) to
\(\mathcal M_\sigma\), (3.8) raises it to the pair-dependent-sign minimum
\(h_{c_q,M_p}(r_p)/c_q\), and (3.9) is by definition the remaining exact
loss under one common signing.  Summation proves (3.10).

The original factor \(F\) is a vertex of its bundle cell, so the minimum in
(3.10) is at most \(\mathcal C_H(F)\).  This proves (3.11), including
nonnegativity.  Cell locality makes the minimum equal to the original
value, which proves (3.12).  \(\square\)

The identity (3.12) is the corridor analogue of a restitution theorem:
there is no generic convexity remainder.  Every unit of ideal smoothing is
restored exactly by row indivisibility or by incompatibility of common
component signs.

## 4. Every positive corridor has an ideal involution direction

### Lemma Z5.4 -- any two equal-rank targets can be paired

For any \(S,T\in\binom{[n]}r\), there is
\(\sigma\in\mathcal I_m\) with \(\sigma S=T\).

#### Proof

Pair the equally sized sets \(S\setminus T\) and \(T\setminus S\)
bijectively.  On the remaining points, pair internally inside
\(S\cap T\) and inside \([n]\setminus(S\cup T)\).  The sum of the sizes of
these last two sets is

\[
n-2|S\setminus T|,
\]

which is odd.  Exactly one of them is odd; leave one point fixed there and
pair every other point internally.  The resulting permutation has one
fixed point and \(m\) transpositions, and maps \(S\) to \(T\).  \(\square\)

### Theorem Z5.5 -- strict ideal gain from every defect

If \(\mathcal C_H(F)>0\), then at some defective depth \(q\) there exists
\(\sigma\in\mathcal I_m\) such that

\[
\boxed{
I_\sigma(F)\ge\frac1{c_q}>0.
}
\tag{4.1}
\]

#### Proof

Fix a depth with nonzero corridor.  If some target has load

\[
x\le c_q-1,
\]

then conservation
\(\sum_S\mu_q(S)=c_qN_q+\rho_q\ge c_qN_q\) forces another target with
load

\[
y\ge c_q+1.
\]

Pairing these two loads has ideal corridor gain at least one: their current
cost is

\[
(c_q-x)+(y-c_q-1)_+,
\]

whereas (3.3) is the minimum cost at the same pair total, and direct
subtraction is at least one.

If no load is below \(c_q\), nonzero corridor means that some load has
\(y\ge c_q+2\).  Since
\(\rho_q<N_q\), not every load can be at least \(c_q+1\); hence some
target has load \(x=c_q\).  Pairing \(x\) and \(y\) again gains exactly at
least one relative to the mass floor.

By Lemma Z5.4, choose one fixed-point involution exchanging the selected
targets.  Every other target orbit has nonnegative Jensen gain, so the
weighted total ideal gain is at least \(1/c_q\).  \(\square\)

Theorem Z5.5 does not assert a legal descent: (3.12) shows exactly how a
positive optimum can block it.  It proves that locking and synchronization,
not lack of an ideal balancing direction, are the only remaining
positive-fibre obstructions for this trade family.

## 5. Quantitative ideal mixing over fixed-point involutions

The existence proof above can be averaged.  The needed spectrum is exact.

For one rank \(r\), define the conjugacy-class averaging operator

\[
(P_rf)(S)
=
\mathbb E_{\sigma\in\mathcal I_m}f(\sigma S)
\qquad
\left(S\in\binom{[n]}r\right).
\tag{5.1}
\]

### Lemma Z5.6 -- fixed-point-involution spectrum

On every Johnson degree \(j\) occurring on the controlled rank-\(r\) slice
(where \(r\le m-1\)), \(P_r\) acts by

\[
\boxed{
\rho_0=1,\qquad
\rho_{2a+1}=0,\qquad
\rho_{2a}
=
\frac{\binom ma}{\binom{2m+1}{2a}}.
}
\tag{5.2}
\]

For every nonconstant degree occurring on the rank-\(r\) slice,

\[
0\le\rho_j\le\frac1n.
\tag{5.3}
\]

Consequently, for all target families
\(X,Y\subseteq\binom{[n]}r\),

\[
\boxed{
\left\langle\mathbf1_X,P_r\mathbf1_Y\right\rangle
\ge
\frac{|X||Y|}{N}
-\frac{\sqrt{|X||Y|}}n,
}
\tag{5.4}
\]

where \(N=\binom nr\) and the inner product is unnormalized counting
measure.

#### Proof

A \(\sigma\)-fixed subset is a union of two-cycles, with the unique fixed
point optionally included.  Hence the permutation characters on
\(j\)-subsets satisfy

\[
\operatorname{Fix}_{2a}(\sigma)=\binom ma,
\qquad
\operatorname{Fix}_{2a+1}(\sigma)=\binom ma.
\]

The permutation module on \(j\)-sets decomposes multiplicity-freely into
the two-row Johnson modules of degrees \(0,\ldots,j\).  Thus the degree
\(j\) character is the fixed-\(j\)-set character minus the
fixed-\((j-1)\)-set character.  For odd \(j=2a+1\) this difference is
zero.  For even \(j=2a\ge2\), its ratio to the module dimension is

\[
\frac{\binom ma-\binom m{a-1}}
{\binom n{2a}-\binom n{2a-1}}
=
\frac{\binom ma}{\binom n{2a}},
\]

because both numerator and denominator, divided by their first binomial
term, equal \((m-2a+1)/(m-a+1)\) when \(n=2m+1\).  This proves (5.2).
Moreover,

\[
\frac{\rho_{2a+2}}{\rho_{2a}}
=
\frac{2a+1}{2(m-a)+1}\le1
\]

through the occurring Johnson degrees.  Hence the even ratios decrease
with \(a\), and their first nonconstant value is

\[
\rho_2
=
\frac{m}{\binom{2m+1}{2}}
=
\frac1{2m+1}
=
\frac1n.
\]

This proves (5.3).

Write

\[
\mathbf1_X=\frac{|X|}{N}\mathbf1+f_X,
\qquad
\mathbf1_Y=\frac{|Y|}{N}\mathbf1+f_Y,
\]

with \(f_X,f_Y\) mean zero.  Self-adjointness and (5.3) give

\[
\langle f_X,P_rf_Y\rangle
\ge-\frac1n\|f_X\|_2\|f_Y\|_2
\ge-\frac{\sqrt{|X||Y|}}n.
\]

Adding the constant term proves (5.4).  \(\square\)

For one rank load \(\mu=\mu_q^F\), define the four level sets

\[
\begin{aligned}
L_q&=\{S:\mu(S)\le c_q-1\},&
R_q^+&=\{S:\mu(S)\ge c_q+1\},\\
Z_q^0&=\{S:\mu(S)=c_q\},&
U_q&=\{S:\mu(S)\ge c_q+2\}.
\end{aligned}
\tag{5.5}
\]

An unordered target pair of type \(L_q\)--\(R_q^+\) has ideal gain at
least one.  So does a pair of type \(Z_q^0\)--\(U_q\).  These two pair
types are disjoint.

Define

\[
\boxed{
\begin{aligned}
\operatorname{Mix}(F)
=
\sum_{q\le H}\frac1{c_q}
\bigg(&
\left[
\frac{|L_q||R_q^+|}{N_q}
-\frac{\sqrt{|L_q||R_q^+|}}n
\right]_+\\
&+
\left[
\frac{|Z_q^0||U_q|}{N_q}
-\frac{\sqrt{|Z_q^0||U_q|}}n
\right]_+
\bigg).
\end{aligned}
}
\tag{5.6}
\]

### Theorem Z5.7 -- averaged ideal gain

\[
\boxed{
\mathbb E_{\sigma\in\mathcal I_m}I_\sigma(F)
\ge
\operatorname{Mix}(F).
}
\tag{5.7}
\]

In particular, some single involution simultaneously realizes at least the
right side across all controlled depths.

#### Proof

Fix \(q\), abbreviate \(\mu=\mu_q^F\), and put

\[
\kappa_q(x,y)
=
\chi_{c_q}(x)+\chi_{c_q}(y)
-2\overline\chi_{c_q}\!\left(\frac{x+y}{2}\right).
\]

If \(I_{\sigma,q}\) is the depth-\(q\) summand of \(I_\sigma\), then
permutation invariance gives the exact identity

\[
I_{\sigma,q}
=
\frac1{2c_q}\sum_S
\kappa_q\bigl(\mu(S),\mu(\sigma S)\bigr).
\]

There is no hidden factor two in the cross-count.  For disjoint target
families \(X,Y\), involutivity gives

\[
\frac12\sum_S\left[
\mathbf1_X(S)\mathbf1_Y(\sigma S)
+\mathbf1_Y(S)\mathbf1_X(\sigma S)
\right]
=
\sum_S\mathbf1_X(S)\mathbf1_Y(\sigma S).
\]

After averaging, the right side is
\(\langle\mathbf1_X,P_{r_q}\mathbf1_Y\rangle\) and counts each unordered
cross-orbit once.  For \(X=L_q,Y=R_q^+\), every such orbit has
\(\kappa_q\ge1\).  The same holds for
\(X=Z_q^0,Y=U_q\), and the two orbit types are disjoint.  Each expected
cross-count is nonnegative and, by (5.4), at least its displayed spectral
lower bound, hence at least the positive part of that bound.  Multiply by
\(1/c_q\), sum in \(q\), and use linearity of expectation.  \(\square\)

Sparse level sets can make (5.6) vanish even when the corridor is positive.
Thus Theorem Z5.7 is a quantitative anti-concentration criterion, not a
universal coercive lower bound in terms of \(\mathcal C_H(F)\).

## 6. Explicit ownership residues

### Lemma Z5.8 -- greedy row fragmentation

For every target pair,

\[
\boxed{
r_p\le\max_K|z_{pK}|.
}
\tag{6.1}
\]

Consequently,

\[
\boxed{
\operatorname{Lock}_\sigma(F)
\le
\operatorname{Frag}_\sigma(F)
:=
\sum_p
\frac{
(\max_K|z_{pK}|-1-b_{c_q}(M_p))_+
}{c_q}.
}
\tag{6.2}
\]

#### Proof

Replace the coefficients by their absolute values and assign signs
sequentially.  At each step choose the new sign opposite to the current
partial sum.  If the current absolute sum is \(s\) and the new coefficient
is \(a\), the next absolute sum is \(|s-a|\le\max\{s,a\}\).  Induction
leaves a final discrepancy at most the largest coefficient, proving (6.1).
The positive-part function is monotone, so (3.8) gives (6.2).
\(\square\)

To bound synchronization, let

\[
\Sigma_p^{\mathrm{opt}}
=
\left\{
\xi\in\{\pm1\}^{\mathscr K_\sigma(F)}:
h_{c_q,M_p}(D_p(\xi))=h_{c_q,M_p}(r_p)
\right\}
\tag{6.3a}
\]

be the complete set of pair-corridor-minimizing signings.  It contains
every signing attaining \(r_p\) and is antipodally symmetric.  This larger
set matters when (3.2) has a flat interval.

Put

\[
a_{pK}=\frac{2|z_{pK}|}{c_q},
\qquad
S_\sigma=\sum_{p,K}a_{pK}.
\tag{6.3}
\]

Define the exact signed bipartite frustration

\[
\boxed{
\operatorname{Fr}_\sigma
=
\min_{\substack{
\xi^p\in\Sigma_p^{\mathrm{opt}}\\
\varepsilon_K,t_p\in\{\pm1\}
}}
\sum_{p,K}
a_{pK}
\mathbf1_{\{\varepsilon_K\ne t_p\xi_K^p\}}.
}
\tag{6.4}
\]

The target phase \(t_p\) chooses either preferred antipode, while
\(\varepsilon_K\) must be one common legal bundle signing.

### Lemma Z5.9 -- exact-sign synchronization bound

\[
\boxed{
\operatorname{Sync}_\sigma
\le
\operatorname{Fr}_\sigma.
}
\tag{6.5}
\]

The frustration is zero exactly when, for some joint choice of pair-optimal
signings, the signed target--bundle incidence graph is balanced.  This is
also equivalent to \(\operatorname{Sync}_\sigma=0\).  In particular, zero
frustration holds when the active incidence graph is a forest.

#### Proof

Compare a common signing \(\varepsilon\) with the preferred antipode
\(t_p\xi^p\) for one pair \(p\).  Flipping a mismatched bundle \(K\)
changes \(D_p\) by \(2|z_{pK}|\).  Lemma Z5.2 is \(1\)-Lipschitz in \(D\),
so after weighting by \(1/c_q\) the pair-cost loss is at most
\(a_{pK}\).  Flip all mismatches and sum over pairs; minimizing proves
(6.5).

Zero frustration is exactly satisfiability of
\(\varepsilon_K=t_p\xi_K^p\) on every active edge.  This is equivalent to
positive sign product around every signed bipartite cycle.  It makes every
pair simultaneously optimal and hence gives zero synchronization loss.
Conversely, a common signing with zero synchronization is pair-optimal for
every \(p\); choosing it as the corresponding preferred signing gives zero
frustration.  A forest has no cycle obstruction.  \(\square\)

Define the vector synchronization defect

\[
\boxed{
\delta_\sigma
=
\min_{\substack{
\xi^p\in\Sigma_p^{\mathrm{opt}}\\
\|u_K\|=\|v_p\|=1
}}
\sum_{p,K}a_{pK}
\frac{1-\xi_K^p\langle u_K,v_p\rangle}{2},
}
\tag{6.6}
\]

The vectors may be taken in a real Euclidean space of dimension at most
the number of target and bundle vertices.  Thus the feasible Gram-matrix
set is compact and the displayed minimum is attained.

### Lemma Z5.10 -- vector rounding and support mass

\[
\boxed{
\operatorname{Fr}_\sigma
\le
\sqrt{S_\sigma\delta_\sigma},
\qquad
S_\sigma
\le
2Ws_H
\le2HW.
}
\tag{6.7}
\]

#### Proof

For fixed vectors, choose a standard Gaussian vector \(g\) and set

\[
\varepsilon_K=\operatorname{sgn}\langle g,u_K\rangle,
\qquad
t_p=\operatorname{sgn}\langle g,v_p\rangle.
\]

The probability of violating one signed incidence is

\[
\frac{\arccos(\xi_K^p\langle u_K,v_p\rangle)}{\pi}.
\]

For \(-1\le x\le1\),

\[
\frac{\arccos x}{\pi}
\le\sqrt{\frac{1-x}{2}}.
\]

Indeed, writing \(x=\cos\theta\) reduces this to
\(2u/\pi\le\sin u\) for
\(u=\theta/2\in[0,\pi/2]\), which is the chord bound from concavity of
sine on that interval.

Weighted Cauchy--Schwarz therefore bounds the expected mismatch by
\(\sqrt{S_\sigma\delta_\sigma}\), and one deterministic signing attains no
more.

For the support bound, at a fixed depth,

\[
\sum_{p,K}|z_{pK}|
\le
\sum_{p,K}
\bigl(
\#(K^+\text{ owners of }S)
+\#(K^+\text{ owners of }\sigma S)
\bigr).
\]

The right side counts active-side occurrences on moved targets and is at
most

\[
n\sum_K|K^+|\le nB=W,
\]

because every wreath owns exactly \(n\) rank-\(r_q\) cyclic intervals.
Multiply by \(2/c_q\) and sum in \(q\).  \(\square\)

Combining (3.11), (6.2), (6.5), and (6.7) gives the explicit
support-feasible augmentation inequality

\[
\boxed{
\Gamma_\sigma(F)
\ge
I_\sigma(F)
-\operatorname{Frag}_\sigma(F)
-\sqrt{S_\sigma(F)\delta_\sigma(F)}.
}
\tag{6.8}
\]

If every active coefficient satisfies

\[
|z_{pK}|\le b_{c_q}(M_p)+1
\tag{6.9}
\]

and the preferred-sign incidence graph is balanced, then

\[
\operatorname{Lock}_\sigma
=\operatorname{Sync}_\sigma=0,
\qquad
\Gamma_\sigma=I_\sigma.
\tag{6.10}
\]

Thus fragmentation and signed cycles are not heuristic obstructions: they
are the two exact features which must be controlled.

## 7. The concrete steepest-augmentation theorem

Define the best involution-bundle gain

\[
\operatorname{Aug}(F)
=
\max_{\sigma\in\mathcal I_m}
\max_\varepsilon
\bigl[
\mathcal C_H(F)-\mathcal C_H(F^\sigma_\varepsilon)
\bigr]
=
\max_{\sigma\in\mathcal I_m}\Gamma_\sigma(F).
\tag{7.1}
\]

### Theorem Z5.11 -- involution-bundle steepest descent

For every positive exact factor,

\[
\boxed{
\operatorname{Aug}(F)
\ge
\left[
\operatorname{Mix}(F)
-\mathbb E_{\sigma\in\mathcal I_m}\operatorname{Frag}_\sigma(F)
-\mathbb E_{\sigma\in\mathcal I_m}
\sqrt{S_\sigma(F)\delta_\sigma(F)}
\right]_+.
}
\tag{7.2}
\]

If the right side is \(g>0\), there is also one legal
\(\mathcal C_H\)-atomic packet of underlying ownership components whose
switch improves \(F\) by at least

\[
\boxed{
\frac g{k_\sigma(F)}
\ge
\frac g{\lfloor B/2\rfloor}
\ge
\frac{2g}{B}.
}
\tag{7.3}
\]

The atomic packet is a feasible augmented-Graver element of

\[
\widehat A_H
=
\begin{pmatrix}
A_m&0\\
B_H&-I
\end{pmatrix}.
\tag{7.4}
\]

Here \(B_H\) is the vertical stack of the depth-\(q\) load maps \(B_q\),
\(1\le q\le H\).

#### Proof

Average (6.8) over \(\sigma\), and apply Theorem Z5.7:

\[
\mathbb E_\sigma\Gamma_\sigma(F)
\ge
\operatorname{Mix}(F)
-\mathbb E_\sigma\operatorname{Frag}_\sigma(F)
-\mathbb E_\sigma\sqrt{S_\sigma(F)\delta_\sigma(F)}.
\]

Since every \(\Gamma_\sigma\ge0\), its maximum is at least the positive
part of this average lower bound.  This proves (7.2), and every maximizing
child is an exact factor by Lemma Z5.1.

Let \(G=F^\sigma_\varepsilon\) be a child with actual gain \(g'\ge g\).
Its \(F/G\) overlay consists of at most \(k_\sigma(F)\) underlying ownership
components.  Apply the Z3 atomic splitting theorem to the corridor changes
inside this overlay: recursively split every packet having a nonnegative
interaction cut.  The terminal leaves are corridor-atomic, their changes
sum to at most the full change, and one leaf gains at least
\(g'/k_\sigma(F)\ge g/k_\sigma(F)\).  Lemma Z5.1 gives the remaining
bounds in (7.3).
Z3 also proves that every corridor-atomic packet is primitive for the
ordinary load lift (7.4).  \(\square\)

Theorem Z5.11 is unconditional.  Its right side may be zero; proving it is
large above the \(HB\) scale is the remaining positive-fibre problem.

### Proposition Z5.11a -- support size required for one large gain

Let a legal exact-factor trade replace \(s\) old wreaths by \(s\) new
wreaths.  Then

\[
\boxed{
\left|
\mathcal C_H(F')-\mathcal C_H(F)
\right|
\le
2ns\sum_{q\le H}\frac1{c_q}
=2ns\,s_H
\le2nsH.
}
\tag{7.5}
\]

Consequently, a one-shot improvement of at least \(\epsilon W\) requires

\[
\boxed{
s\ge
\frac{\epsilon B}{2s_H}
\ge
\frac{\epsilon B}{2H}.
}
\tag{7.6}
\]

For a fixed Gaussian window, this is
\(\Omega_{A,\epsilon}(B/\sqrt m)\) replaced wreaths.

#### Proof

The corridor is \(1\)-Lipschitz in every load coordinate.  At one depth,
the old and new sides contain \(ns\) target occurrences each, so the
\(\ell^1\) load change is at most \(2ns\).  Multiply by \(1/c_q\), sum in
\(q\), and use \(W=nB\).  \(\square\)

This is a one-step packet-size lower bound, not an obstruction to a long
sequence of smaller improvements.

## 8. Direct attack on the positive optimum

Let

\[
C_H^*
=
\min_{F\in\mathcal X_m}\mathcal C_H(F).
\tag{8.1}
\]

### Corollary Z5.12 -- one-cell positive optimum certificate

For every exact \(F\) and every \(\sigma\in\mathcal I_m\),

\[
\boxed{
\begin{aligned}
C_H^*
&\le
\mathcal M_\sigma(F)
+\operatorname{Lock}_\sigma(F)
+\operatorname{Sync}_\sigma(F)\\
&\le
\mathcal M_\sigma(F)
+\operatorname{Frag}_\sigma(F)
+\sqrt{S_\sigma(F)\delta_\sigma(F)}.
\end{aligned}
}
\tag{8.2}
\]

Thus, for every fixed \(A\), the following concrete condition is sufficient
for fixed-window unlabelled overload:

\[
\boxed{
\mathcal M_\sigma(F)+\operatorname{Frag}_\sigma(F)=o(W),
\qquad
\delta_\sigma(F)=o\!\left(\frac W{s_H}\right)
}
\tag{8.3}
\]

for some positive exact \(F=F_{m,A}\) and
\(\sigma=\sigma_{m,A}\).  Since \(s_H\le H=O_A(\sqrt m)\), it is enough to
have

\[
\delta_\sigma(F)=o_A(W/\sqrt m).
\tag{8.4}
\]

#### Proof

The first line of (8.2) is Theorem Z5.3 evaluated at its exact minimizing
child.  The second uses (6.2), (6.5), and (6.7).  Under (8.3),

\[
\sqrt{S_\sigma\delta_\sigma}
\le
\sqrt{2Ws_H\,\delta_\sigma}
=o(W).
\]

Hence \(C_H^*=o(W)\) for this fixed \(A\).  If (8.3) is supplied for every
fixed \(A>0\), then (1.5) and the frozen diagonalization theorem give
MWB.  \(\square\)

Unlike Z3 comparison descent, (8.2) compares the positive optimum to
explicit data in one exact ownership cell; it does not assume a better
exact comparator.  Condition (8.3) remains unproved.

### Theorem Z5.13 -- conditional logarithmic macro-descent

Fix \(A>0\).  Suppose there are constants

\[
0<\eta_A\le1,
\qquad
K_A>0,
\tag{8.5}
\]

and an integer \(m_0(A)\), such that for every \(m\ge m_0(A)\) and every
exact factor \(F\), with \(H=\lceil A\sqrt m\rceil\), there is an
involution satisfying

\[
\boxed{
I_\sigma(F)
-\operatorname{Frag}_\sigma(F)
-\sqrt{S_\sigma(F)\delta_\sigma(F)}
\ge
\eta_A\mathcal C_H(F)-K_AHB.
}
\tag{8.6}
\]

Then steepest involution-bundle descent reaches an exact factor with

\[
\boxed{
\mathcal C_H(F)
\le
R_A(m):=\frac{2K_A}{\eta_A}HB=o(W)
}
\tag{8.7}
\]

after at most

\[
\boxed{
1+
\left\lceil
\frac2{\eta_A}
\log^+\!\left(
\frac{\mathcal C_H(F_0)}{R_A(m)}
\right)
\right\rceil
=O_A(\log n)
}
\tag{8.8}
\]

macrosteps from any initial exact factor \(F_0\), where
\(\log^+x=\max\{0,\log x\}\).  Therefore (8.6) implies overload on this
fixed \(A\)-window.  If its hypothesis holds for every fixed \(A>0\)
with \(A\)-dependent constants, the frozen diagonalization theorem then
implies MWB.

If one insists that every step itself be corridor-atomic, the same
conclusion follows in

\[
O_A(B\log n)
\tag{8.9}
\]

atomic packet steps.

#### Proof

If \(\mathcal C_H(F)>R_A(m)\), then (8.6) and (6.8) give a legal child gain
at least

\[
\eta_A\mathcal C_H(F)-K_AHB
>
\frac{\eta_A}{2}\mathcal C_H(F).
\]

Thus one macrostep multiplies the corridor by at most
\(1-\eta_A/2\).  Iteration and
\(-\log(1-\eta_A/2)\ge\eta_A/2\) prove (8.8).  The universal initial bound
(1.7) makes the logarithm \(O_A(\log n)\).

Since

\[
\frac{HB}{W}=\frac Hn=O_A(m^{-1/2}),
\]

(8.7) is \(o(W)\).  For atomic steps, Theorem Z5.11 retains at least
\(2/B\) of each available macro-gain.  Above \(R_A(m)\), the macro-gain
is greater than \(\eta_A\mathcal C_H(F)/2\), so one atomic step gains more
than \(\eta_A\mathcal C_H(F)/B\) and contracts by a factor at most
\(1-\eta_A/B\).  Hence at most
\(O((B/\eta_A)\log^+(\mathcal C_H(F_0)/R_A(m)))=O_A(B\log n)\) atomic
steps reach the same threshold.  \(\square\)

Hypothesis (8.6) is the precise unproved route-closing lemma.  It asks for
control of genuine bundle coefficients and signed target cycles; no
quadratic component-variance proxy occurs.

## 9. Necessary structure of a positive local minimum

Call \(F\) **involution-bundle-local** if no vertex of any cell
\(\{F^\sigma_\varepsilon\}\), \(\sigma\in\mathcal I_m\), has smaller
corridor.

### Theorem Z5.14 -- exact local restitution and averaged obstruction

An involution-bundle-local factor satisfies, for every
\(\sigma\in\mathcal I_m\),

\[
\boxed{
I_\sigma(F)
=
\operatorname{Lock}_\sigma(F)
+\operatorname{Sync}_\sigma(F).
}
\tag{9.1}
\]

Consequently,

\[
\boxed{
\operatorname{Mix}(F)
\le
\mathbb E_\sigma\operatorname{Frag}_\sigma(F)
+\mathbb E_\sigma\sqrt{S_\sigma(F)\delta_\sigma(F)}.
}
\tag{9.2}
\]

More pointwise, if for some \(\sigma\)

\[
I_\sigma(F)-\operatorname{Lock}_\sigma(F)\ge\gamma W
\tag{9.3}
\]

with \(\gamma>0\), then

\[
\boxed{
\delta_\sigma(F)
\ge
\frac{\gamma^2W}{2s_H}
\ge
\frac{\gamma^2W}{2H}.
}
\tag{9.4}
\]

On a fixed Gaussian window this is
\(\Omega_{A,\gamma}(W/\sqrt m)\).

#### Proof

Locality makes \(\Gamma_\sigma(F)=0\), so (9.1) is (3.11).  Average it,
use Theorem Z5.7, and apply
\(\operatorname{Lock}\le\operatorname{Frag}\) and
\(\operatorname{Sync}\le\sqrt{S\delta}\) to get (9.2).

Under (9.3), (9.1) and Lemma Z5.10 give

\[
\gamma W
\le\operatorname{Sync}_\sigma
\le\sqrt{2Ws_H\,\delta_\sigma}.
\]

Squaring proves (9.4).  \(\square\)

Theorem Z5.14 classifies what an \(\Omega(W)\)-corridor local minimum would
have to realize: either the ideal level-set mixing is already small because
the defects are highly concentrated, or row fragmentation and signed-cycle
frustration are macroscopically large.  It does not construct such a
factor.

## 10. A genuine packet-local obstruction with a Catalan-scale certificate

The following exact example shows that a natural sparse family of
support-feasible MSW trades can have a positive packet-local minimum carrying
a certified \(\Theta(B)=o(W)\) lower bound.  The proof gives no
\(O(B)\) upper bound on that minimum and therefore determines the scale of
the certificate, not the full objective value.

Let

\[
C_j=\operatorname{Cat}_j,
\qquad
F^0=F_m^{\mathrm{MSW}},
\qquad
\tau=(2\ 3),
\]

and assume \(m\ge6\).  For each Dyck word
\(U\in\mathcal D_{m-5}\), put

\[
R_U=110010U\in\mathcal D_{m-2}.
\tag{10.1}
\]

Let \(z_U\) be the new-minus-old switch of the genuine \(p=0\),
two-for-two MSW ownership component in the \(F^0/\tau F^0\) overlay indexed
by \(R_U\).  Here genuineness and the fixed-\(p\) component
classification are the established theorems of
`MSW_COMPONENT_HIERARCHY_REDUCTION.md`, with the corresponding shadow
formulas in `MSW_MULTIRANK_LOCAL_TRADES.md`.  Its two old roots are

\[
X_U=1100R_U=1100110010U,
\qquad
Y_U=1010R_U=1010110010U.
\tag{10.2}
\]

The fixed-\(p\) MSW component theorem proves that these components have
disjoint old and new supports and switch independently.  Hence

\[
\boxed{
F_\varepsilon
=
F^0+\sum_{U\in\mathcal D_{m-5}}\varepsilon_Uz_U,
\qquad
\varepsilon\in\{0,1\}^{\mathcal D_{m-5}},
}
\tag{10.3}
\]

is always a binary positive exact factor.  From every cube vertex, toggling
any nonempty coordinate packet is a support-feasible union of complete
ownership components.

The canonical depth-one collision family proved in
`FRACTIONAL_PACKET_CANONICAL_MSW_OBSTRUCTION_20260725.md` and independently
checked in its audit has one distinct target \(S_V\) for every
\(V\in\mathcal D_{m-4}\), with three pairwise row-disjoint owners

\[
E(w^{(1)}V),\qquad
E(w^{(2)}V),\qquad
E(w^{(3)}V),
\tag{10.4}
\]

where the seed prefixes are

\[
w^{(1)}=11110000,\qquad
w^{(2)}=11101000,\qquad
w^{(3)}=11001100.
\tag{10.5}
\]

### Lemma Z5.15 -- retained collision targets

Every cube vertex \(F_\varepsilon\) retains all three owners in (10.4)
whenever \(V\) is not of the form \(10U\),
\(U\in\mathcal D_{m-5}\).  Therefore it has at least

\[
\boxed{
L_m=C_{m-4}-C_{m-5}
}
\tag{10.6}
\]

distinct depth-one targets of load at least three.

#### Proof

Among the deleted roots of \(z_U\), the root \(X_U\) is exactly
\(w^{(3)}10U\).  The other root \(Y_U\) begins with
\(10101100\), different from all three prefixes in (10.5).  Thus a selected
trade deletes from the collision triples only the row
\(E(w^{(3)}10U)\).  Different suffixes and different fixed-\(p\)
components have disjoint supports.  New sides cannot delete old owners.
Hence every triple with suffix outside the subfamily
\(\{10U\}\) remains intact.  Their number is (10.6).  \(\square\)

At depth one,

\[
\frac W{N_1}=\frac{m+2}{m},
\qquad
c_1=1.
\tag{10.7}
\]

Every balanced mobile quota is one or two.  A target of load at least three
has corridor cost at least one and exceeds every allowed quota by at least
one.

### Theorem Z5.16 -- positive packet-local cube minimum

For every fixed \(A>0\), all sufficiently large \(m\), and
\(H=\lceil A\sqrt m\rceil\), every cube vertex satisfies

\[
\boxed{
\mathcal C_H(F_\varepsilon)\ge L_m,
\qquad
\sum_{q\le H}\frac{O_q(F_\varepsilon)}{c_q}\ge L_m.
}
\tag{10.8}
\]

Choose a minimizer \(F^\star\) of \(\mathcal C_H\) on the finite cube
(10.3).  Then no nonempty packet of the catalogued components improves
\(F^\star\), while (10.8) holds.  Thus \(F^\star\) is a genuine
positive-fibre packet-local minimum for this concrete trade family.

The constants satisfy

\[
\boxed{
L_m\ge\frac12C_{m-4}>\frac1{512}C_m,
}
\tag{10.9}
\]

and more precisely

\[
\boxed{
\frac{L_m}{C_m}
=
\frac3{1024}+O(m^{-1}),
\qquad
|\mathcal D_{m-5}|
=
\left(\frac1{1024}+O(m^{-1})\right)C_m.
}
\tag{10.10}
\]

#### Proof

Lemma Z5.15 and \(c_1=1\) give one unit of corridor and mobile-quota
surplus at every retained target.  This proves (10.8) directly; using the
factor-two comparison (1.5) would unnecessarily lose a constant.

A minimum exists on the finite cube.  Every packet toggle leads to another
cube vertex, so no such packet improves it.

For \(k=m-4\),

\[
\frac{C_{k-1}}{C_k}=\frac{k+1}{4k-2},
\]

and hence

\[
\frac{C_k-C_{k-1}}{C_k}
=
\frac{3(k-1)}{4k-2}\ge\frac12.
\]

Also

\[
\frac{C_{m-4}}{C_m}
=
\prod_{j=m-3}^{m}\frac{j+1}{4j-2}
>4^{-4}=\frac1{256}.
\]

This proves (10.9).  Taking the fixed-shift Catalan asymptotics gives
(10.10).  \(\square\)

The locality in Theorem Z5.16 is only with respect to the explicit subcube
(10.3).  It is not proved local under all involution bundles, all
cancellation-connected packets, or all augmented-Graver moves.  Nor is it
proved nonglobal in the whole exact-factor fibre.

Most importantly,

\[
L_m=\Theta(B)=\Theta(W/m)=o(W).
\tag{10.11}
\]

Thus the proved collision certificate is not an \(\Omega(W)\) lower bound.
The actual objective at the cube minimizer is not proved to be
\(O(B)\), so the theorem neither certifies nor excludes a larger value.  A
macroscopic certified obstruction requires a \(W\)-sized exact target
certificate or another lower-bound mechanism; neither is known.

## 11. Logical scope and remaining theorem

### Unconditional conclusions

This report proves:

1. the exact pair corridor formula (3.2);
2. positive legality of every fixed-point-involution bundle signing;
3. the exact midpoint--lock--synchronization decomposition (3.10);
4. a strict ideal involution direction for every positive corridor;
5. the fixed-point-involution level-set mixing bound (5.7);
6. the row-fragmentation and signed-incidence bounds (6.2), (6.5), and
   (6.7);
7. the concrete steepest bundle and atomic-packet augmentation bounds
   (7.2)--(7.3);
8. the one-cell upper bound on the positive optimum (8.2);
9. the exact restitution identities forced at an involution-bundle local
   or global minimum; and
10. the MSW packet-local example with a Catalan-scale certified lower
    bound.

### Unproved statements

None of the following is proved:

1. the route-closing ownership inequality (8.6);
2. \(\mathcal C_H^*=o(W)\);
3. a uniform anti-concentration theorem forcing
   \(\operatorname{Mix}(F)\gtrsim\mathcal C_H(F)\);
4. an upper bound placing the averaged fragmentation and synchronization
   residues below the mixing gain;
5. an \(\Omega(W)\)-corridor positive local minimum;
6. labelled common-owner synchronization; or
7. a literal contiguous-OR word.

The precise remaining Z5 lemma is:

> **Involution restitution gap -- UNPROVED.**  For every fixed \(A>0\),
> prove constants \(\eta_A>0\), \(K_A<\infty\), and \(m_0(A)<\infty\)
> such that, for all \(m\ge m_0(A)\), every positive exact factor has a
> fixed-point involution satisfying (8.6), or prove the averaged sufficient
> inequality obtained by replacing its left side with the right side of
> (7.2).

This lemma is sufficient, not asserted necessary for MWB.  A counterexample
to it would refute only this involution-bundle descent architecture.

## 12. Independent audit of the decisive constants

The proof was independently audited at the pair, ownership, spectral, and
scale levels.

1. **Pair normalization.**  The two loads move by half of \(D\), but a
   component mismatch changes \(D\) by \(2z_{pK}\).  Since (3.2) is
   \(1\)-Lipschitz, the synchronization edge weight is exactly
   \(2|z_{pK}|/c_q\).  There is no missing factor two.

2. **Midpoint baseline.**  Two identical real midpoint terms equal
   \(b_c(M)\), not \(2b_c(M)\).  Thus (3.6), (3.8), and (3.10) have
   compatible normalizations.

3. **Equivariant bundling.**  An individual complete ownership component
   is already a legal exact-factor switch.  Bundling its \(\sigma\)-orbit
   is needed instead for the symmetric pair-total normal form
   \(K^-=\sigma K^+\).  Every bundle signing remains legal because it
   still switches only complete underlying components.

4. **Component divisor.**  A noncommon ownership component cannot be
   one-for-one because distinct unoriented wreath columns are distinct.
   Hence it uses at least two old wreaths and
   \(k_\sigma\le\lfloor B/2\rfloor\).  This justifies the constant
   \(2/B\) in (7.3).

5. **Spectrum.**  Odd Johnson degrees have eigenvalue zero; nonconstant even
   degrees have nonnegative eigenvalue at most \(1/n\).  The mixing error
   in (5.4) is therefore
   \(n^{-1}\sqrt{|X||Y|}\) with unnormalized counting measure.

6. **Support mass.**  At one depth, the absolute bundle coefficients are
   charged to active old-side target occurrences.  Each old wreath has
   exactly \(n\) such occurrences, giving
   \(\sum_{p,K}|z_{pK}|\le W\) and the exact factor two in (6.7).

7. **Descent scale.**  \(HB/W=H/n=O_A(m^{-1/2})\), whereas the certified
   MSW lower bound has only \(L_m/W=\Theta(1/m)\).  No upper bound on the
   cube-minimum objective is inferred from this certificate.

8. **Implication scope.**  Every constructed child is one exact factor
   shared across all depths.  Any conclusion obtained from the sufficient
   conditions (8.3) or (8.6) is unlabelled histogram balancing only; no
   labelled synchronization or literal word is inferred.

## 13. Final theorem-level conclusion

The free-quota corridor does have a rigorous positive-fibre steepest
augmentation theory.  Fixed-point involutions expose an ideal balancing
direction at every state of nonzero corridor, and genuine ownership-bundle signings
convert that direction into an exact child with losses measured by two
explicit residues.  The best proved gain is (7.2), and a positive gain
contains a corridor-atomic support-feasible packet with the improved
universal comparison divisor \(\lfloor B/2\rfloor\).

The positive optimum remains open because exact factors may, in principle,
restore all involution smoothing through row locking and signed-cycle
synchronization.  The concrete MSW packet-local example has only a
\(\Theta(W/m)\) certified lower bound; no \(\Omega(W)\) lower bound and no
matching \(O(W/m)\) objective upper bound is proved.  The route is therefore
advanced to a precise ownership-restitution inequality, not closed.
