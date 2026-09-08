# Six-slot `h=4`: redundant endpoints and a two-gate scalar/KKT reduction

**Date:** 2026-08-04
**Status:** unconditional pure-mathematical reduction.  It replaces the
three inert endpoint faces and their four correlated Apéry corrections by
two one-parameter endpoint-train gates.  Every inner minimization is
one-dimensional and its possible interior minimizers satisfy explicit
first-derivative equations.  The two final scalar gates are not signed
here, so complete six-slot positivity is not claimed.

Put

\[
 A={\sqrt\pi\over2},
\]

and let

\[
 K(w)=
 \begin{cases}
  1-e^{-(A-w)^2}-e^{-(A+w)^2},&0\le w\le A,\\
  -e^{-(A+w)^2},&w>A
 \end{cases}
\tag{0.1}
\]

be the Rayleigh signed-tail kernel.  For `tau>0`, write

\[
 F_\tau(w)=\sum_{q\ge0}K(q\tau+w),
 \qquad C(\tau)=F_\tau(0).
\tag{0.2}
\]

Consider the canonical six-slot size-four-efficient table

\[
 (c_0,\ldots,c_6)=(0,x,y,z,P,P+u,P+v).
\tag{0.3}
\]

The authoritative seven-correction theorem supplies

\[
 {2A\over3}\le P<A,
 \qquad 0\le u<A-P\le v,
\tag{0.4}
\]

\[
 x\le u,
 \qquad y\le {P\over2},
 \qquad z\le {3P\over4},
 \qquad v\le {P\over2},
\tag{0.5}
\]

and the saturated endpoint equation

\[
 v=\max\{A-P,x+u,y,2z-P\}.
\tag{0.6}
\]

The threshold face `v=A-P` is already strictly positive.  We work on the
three inert faces, where `v>A-P`.

## 1. The endpoint generator is literally redundant

### Lemma 1.1

On each inert face, the size-six generator is equal to a configuration
using only the first five generators:

\[
\begin{array}{c|c}
\mathrm X&c_6=c_1+c_5,\\
\mathrm Y&c_6=c_2+c_4,\\
\mathrm Z&c_6=2c_3.
\end{array}
\tag{1.1}
\]

Consequently the exact six-slot Bellman clock is unchanged if the size-six
generator is deleted.

#### Proof

The three equalities are respectively `v=x+u`, `v=y`, and
`v=2z-P`.  Replace every occurrence of a size-six generator by the
displayed lower configuration.  Capacity and value are preserved exactly.
Thus every configuration using size six has a first-five realization with
the same value, while the reverse inclusion of configuration families is
trivial.  The Bellman maxima agree at every capacity. \(\square\)

This does **not** invoke the complete five-slot theorem: the retained
endpoint `P+u` is strictly below `A`.  The obstruction is a delayed first
crossing in a five-generator clock.

## 2. Exact endpoint-period lower comparison

Set

\[
 p=A-P,
 \qquad a=p-u,
 \qquad \delta=v-p,
 \qquad \tau=P+v=A+\delta.
\tag{2.1}
\]

Then

\[
 0<p\le {A\over3},
 \qquad 0<a\le p,
 \qquad 0<\delta<{A\over2}.
\tag{2.2}
\]

Indeed `P>=2A/3` gives the bound on `p`, `P+u<A` gives `a>0`, and
maximum efficiency gives

\[
 \tau=P+v\le {3P\over2}<{3A\over2}.
\]

Equation (0.6) becomes the exact three-displacement identity

\[
 \boxed{
 \delta=\max\{x-a,y-p,2z-A\}.}
\tag{2.3}
\]

In particular,

\[
 x\le a+\delta,
 \qquad y\le p+\delta,
 \qquad z\le{\tau\over2},
\tag{2.4}
\]

and at least one inequality is an equality.  Also

\[
 0\le x<{A\over2},
 \qquad0\le y<{A\over2}.
\tag{2.5}
\]

### Lemma 2.1 (literal endpoint train)

The exact Bellman functional satisfies

\[
\boxed{
\begin{aligned}
 \Phi\ge\mathscr E:={}&C(\tau)
 +F_\tau(x)+F_\tau(A-a)\\
 &+F_\tau(y)+F_\tau(A-p)+F_\tau(z).
\end{aligned}}
\tag{2.6}
\]

#### Proof

At capacity `6q+r`, use `q` copies of the endpoint configuration and the
size-`r` generator.  Its value is `q tau+c_r`.  For `q=0`, internal
superadditivity gives the exact value `V_r=c_r`.  For `q>=1`, both the
candidate and the Bellman optimum lie in `[A,infinity)`, where `K` is
increasing.  Hence

\[
 K(V_{6q+r})\ge K(q\tau+c_r).
\]

Summing the six residue classes gives (2.6).  The redundancy lemma shows
that the endpoint configuration is available even after deleting the
literal size-six generator. \(\square\)

Thus the five nonzero endpoint residues have become two reflected pairs

\[
 (x,A-a),
 \qquad(y,A-p),
\tag{2.7}
\]

and one singleton `z`.

## 3. A period-uniform no-interior-minimum lemma

### Lemma 3.1

For every `tau>=A`, every interior critical point of `F_tau` on
`[0,A/2]` is a strict local maximum.  Consequently, for

\[
 0\le L\le U\le {A\over2},
\]

one has

\[
 \boxed{
 \min_{L\le w\le U}F_\tau(w)
 =\min\{F_\tau(L),F_\tau(U)\}.}
\tag{3.1}
\]

#### Proof

For `0<=w<=A/2`, all positive-period terms are on the Gaussian tail, so

\[
 F_\tau(w)
 =1-e^{-(A-w)^2}
  -\sum_{q\ge0}e^{-(A+w+q\tau)^2}.
\tag{3.2}
\]

Put

\[
 \phi(t)=te^{-t^2},
 \qquad \lambda(t)={\phi'(t)\over\phi(t)}={1\over t}-2t.
\tag{3.3}
\]

The logarithmic derivative `lambda` is strictly decreasing.  At an
interior critical point, differentiation of (3.2) gives

\[
 \sum_{q\ge0}\phi(A+w+q\tau)=\phi(A-w).
\tag{3.4}
\]

Differentiating once more and using the decrease of `lambda`,

\[
\begin{aligned}
 {1\over2}F_\tau''(w)
 &=\sum_{q\ge0}\phi'(A+w+q\tau)+\phi'(A-w)\\
 &\le
 2A\left({1\over A^2-w^2}-2\right)\phi(A-w)<0.
\end{aligned}
\tag{3.5}
\]

The last inequality follows from

\[
 A^2-w^2\ge{3A^2\over4}={3\pi\over16}>{1\over2}.
\]

Thus every interior critical point is a strict maximum.  A global minimum
on a closed interval cannot occur at such a point, proving (3.1).
\(\square\)

## 4. Three one-dimensional envelopes

Fix

\[
 0\le\delta\le {A\over2},
 \qquad \tau=A+\delta,
\]

and put

\[
 m_\delta(b)=\min\left\{{A\over2},b+\delta\right\}.
\tag{4.1}
\]

### 4.1 An inactive reflected pair

Define

\[
\boxed{
 \mathcal I(\delta)
 =\min_{0\le b\le A/3}
 \left[
 F_\tau(A-b)
 +\min\{C(\tau),F_\tau(m_\delta(b))\}
 \right].}
\tag{4.2}
\]

If `0<=r<=A/2` and `r<=b+delta`, then Lemma 3.1 gives

\[
 F_\tau(r)+F_\tau(A-b)\ge\mathcal I(\delta).
\tag{4.3}
\]

Thus `mathcal I` is a common lower envelope for either nonactive pair in
(2.7).

### 4.2 The active reflected pair together with the ceiling

On face `X`, the active low shift is

\[
 x=a+\delta,
\]

while on face `Y` it is

\[
 y=p+\delta.
\]

In both cases the active low shift `ell` obeys

\[
                         3\ell\le\tau.
\tag{4.4}
\]

For `X`, this follows already from `x<=P/4`; for `Y`, it is equivalent
to `2y<=P`.  Hence the corresponding base `b` lies in

\[
 0\le b\le B_\delta:={A-2\delta\over3}.
\tag{4.5}
\]

Define

\[
\boxed{
 \mathcal H(\delta)
 =\min_{0\le b\le B_\delta}
 \left[
 C(\tau)+F_\tau(b+\delta)+F_\tau(A-b)
 \right].}
\tag{4.6}
\]

This retains the entire active complementary pair and the unique ceiling;
no reflection error or period gain is discarded.

### 4.3 The singleton

Define

\[
\boxed{
 \mathcal S(\delta)
 =\min_{0\le w\le\tau/2}F_\tau(w).}
\tag{4.7}
\]

The endpoint inequality `2z<=tau` gives

\[
                         F_\tau(z)\ge\mathcal S(\delta).
\tag{4.8}
\]

## 5. The two scalar gates

### Theorem 5.1

Every table on face `X` or `Y` satisfies

\[
 \boxed{
 \Phi\ge
 \mathfrak G_{XY}(\delta)
 :=\mathcal H(\delta)+\mathcal I(\delta)+\mathcal S(\delta).}
\tag{5.1}
\]

Every table on face `Z` satisfies

\[
 \boxed{
 \Phi\ge
 \mathfrak G_Z(\delta)
 :=C(\tau/2)+2\mathcal I(\delta).}
\tag{5.2}
\]

#### Proof

On `X` or `Y`, one pair in (2.7) is active.  Allocate it together with
the ceiling to (4.6), allocate the other pair to (4.2), and use (4.8) for
the singleton.  Equation (2.6) gives (5.1).

On `Z`, both reflected pairs are inactive and `z=tau/2`.  The elementary
interlacing identity

\[
 C(\tau)+F_\tau(\tau/2)
 =\sum_{n\ge0}K(n\tau/2)
 =C(\tau/2)
\tag{5.3}
\]

then gives (5.2). \(\square\)

### Corollary 5.2 (complete scalar reduction)

The complete six-slot `h=4` branch is positive if

\[
 \boxed{
 \mathfrak G_{XY}(\delta)>0,
 \qquad
 \mathfrak G_Z(\delta)>0
 \quad(0<\delta<A/2).}
\tag{5.4}
\]

Conversely, any nonpositive canonical `h=4` table forces the corresponding
gate in (5.4) to be nonpositive at its own `delta`.  The threshold value
`delta=0` is already strictly positive by the authenticated endpoint
theorem.

Thus the three inert faces and four correlated late corrections have been
replaced by two scalar functions of one outer variable.  Each constituent
envelope contains only one inner scalar minimization.

## 6. Exact KKT list for the remaining scalar gates

For fixed `tau`, abbreviate

\[
 T_\tau(w)=F_\tau'(w)
 =\sum_{q\ge0}K'(q\tau+w),
\tag{6.1}
\]

and

\[
 R_\tau(w)={\partial\over\partial\tau}F_\tau(w)
 =\sum_{q\ge1}qK'(q\tau+w).
\tag{6.2}
\]

Absolute Gaussian convergence justifies all differentiations below.

### Proposition 6.1 (inner minimizers)

Every minimizer defining `mathcal H(delta)` is either an endpoint
`b in {0,B_delta}` or satisfies

\[
 \boxed{T_\tau(b+\delta)=T_\tau(A-b).}
\tag{6.3}
\]

Every minimizer defining `mathcal I(delta)` lies at `b=0`, `b=A/3`, a
switching point

\[
 b+\delta={A\over2}
 \quad\hbox{or}\quad
 F_\tau(m_\delta(b))=C(\tau),
\tag{6.4}
\]

or satisfies one of the two smooth equations

\[
 \boxed{T_\tau(A-b)=0}
\tag{6.5}
\]

and

\[
 \boxed{T_\tau(b+\delta)=T_\tau(A-b).}
\tag{6.6}
\]

Equation (6.5) applies when the selected low endpoint is constant (`0` or
`A/2`); equation (6.6) applies on the moving endpoint branch.

Every minimizer defining `mathcal S(delta)` is `0`, `tau/2`, or a point
`w` satisfying

\[
 \boxed{T_\tau(w)=0,
 \qquad A/2\le w\le\tau/2.}
\tag{6.7}
\]

#### Proof

Differentiate the one-dimensional objectives on each smooth branch.  The
only nonsmooth locations are exactly (6.4).  Lemma 3.1 excludes an
interior minimizing critical point of `F_tau` below `A/2`, which sharpens
the range in (6.7). \(\square\)

### Proposition 6.2 (outer derivative ledger)

At a smooth point where the displayed inner minimizers are unique, the
envelope derivatives are obtained without differentiating those minimizers.
For an interior minimizer `b` of `mathcal H`,

\[
\boxed{
 \mathcal H'(\delta)
 =R_\tau(0)
  +R_\tau(b+\delta)+T_\tau(b+\delta)
  +R_\tau(A-b).}
\tag{6.8}
\]

At the fixed endpoint `b=0`, the same displayed formula holds with
`b=0`.  At the moving endpoint

\[
 b=B_\delta,
 \qquad b+\delta={\tau\over3},
 \qquad A-b={2\tau\over3},
\]

one instead has

\[
\boxed{
 \mathcal H'(\delta)
 =R_\tau(0)
  +R_\tau(\tau/3)+{1\over3}T_\tau(\tau/3)
  +R_\tau(2\tau/3)+{2\over3}T_\tau(2\tau/3).}
\tag{6.8a}
\]

For `mathcal I`, the three smooth low-endpoint branches have derivatives

\[
\begin{array}{c|c}
\text{selected low endpoint}&\mathcal I'(\delta)\\ \hline
0&R_\tau(A-b)+R_\tau(0),\\
A/2&R_\tau(A-b)+R_\tau(A/2),\\
b+\delta&R_\tau(A-b)+R_\tau(b+\delta)+T_\tau(b+\delta).
\end{array}
\tag{6.9}
\]

For `mathcal S`, an interior critical minimizer contributes

\[
                         \mathcal S'(\delta)=R_\tau(w),
\tag{6.10}
\]

The fixed endpoint `w=0` contributes

\[
                         \mathcal S'(\delta)=R_\tau(0),
\tag{6.10a}
\]

while the moving endpoint `w=tau/2` contributes

\[
 \mathcal S'(\delta)
 =R_\tau(\tau/2)+{1\over2}T_\tau(\tau/2).
\tag{6.11}
\]

Finally,

\[
 {d\over d\delta}C(\tau/2)
 ={1\over2}\sum_{q\ge1}qK'(q\tau/2).
\tag{6.12}
\]

#### Proof

Use the envelope theorem on each smooth branch and
`d tau/d delta=1`.  The explicit moving low shift contributes the
additional `T_tau` term in (6.8)--(6.9); the moving half-period endpoint
contributes half of `T_tau` in (6.11).  At `b=B_delta`, the two shifts are
`tau/3` and `2tau/3`, with velocities `1/3` and `2/3`, giving (6.8a).
Equation (6.12) is direct termwise differentiation. \(\square\)

Equations (6.3)--(6.12) are the exact finite KKT system left by this
reduction.  In particular, the Chamber-II strategy of subtracting shift
stationarity from a period residual can now be attempted on a finite list
of complementary-pair branches; there is no remaining high-dimensional
Apéry maximum or availability-head case split.

## 7. What is and is not proved

The theorem proves:

1. all three inert endpoints are redundant lower composites;
2. their endpoint comparison has the exact two-pair-plus-singleton form;
3. all physical variables collapse to the two outer gates (5.1)--(5.2);
4. every smooth inner or outer stationary obstruction obeys the explicit
   one-dimensional KKT ledger in Section 6, while all nonsmooth and domain
   boundary candidates are listed separately.

It does **not** prove that `mathfrak G_XY` or `mathfrak G_Z` is positive.
Accordingly it does not close `h=4`, complete six-slot positivity, the
all-grid Bellman inequality, or any OR-word construction.

## 8. Frozen dependencies

| role | file | SHA-256 |
|---|---|---|
| canonical six-slot normalization | `MATH_THEOREM_SIX_SLOT_CANONICAL_MAXIMUM_EFFICIENCY_APERY_NORMAL_FORMS_20260804.md` | `3b537980a6f18aae936979335cc6756079ff10b92a80019acf3a97df8be9bede` |
| authoritative `h=4` seven-correction reduction | `MATH_THEOREM_SIX_SLOT_FOUR_EFFICIENT_SEVEN_CORRECTION_REDUCTION_20260804.md` | `fa362d05e586749467f9d5acb5f20883825d82505da71fba97fec678b4c213f9` |
| independent audit of that reduction | `MATH_AUDIT_SIX_SLOT_FOUR_EFFICIENT_SEVEN_CORRECTION_REDUCTION_INDEPENDENT_20260804.md` | `0f8baa74dc167940c8923d8f5beee6f7016e8e7c6ba6b24a53a5861b7a99965f` |
| threshold endpoint closure and endpoint-period comparison | `MATH_THEOREM_SIX_SLOT_ENDPOINT_EFFICIENT_SUBCOMPLEMENTARY_PAIR_CLOSURE_20260804.md` | `4929d9e074816be68ece5a97203c5ea1696fd2f79f8445da9cc746ad205209e0` |
