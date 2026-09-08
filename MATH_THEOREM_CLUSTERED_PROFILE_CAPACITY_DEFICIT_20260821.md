# Clustered product schedules have only sublinear split-profile capacity deficit

**Status (2026-08-21).**  Every statement below is proved.  The theorem
removes a scalar obstruction from the clustered two-block product route: once
the requisite local tight-cycle factors are supplied and all admissible
payload ranks are pooled, their total phase capacity falls
short of the upper-band split-profile target counts by only
`O(W_b b^(-1/4))=o(W_b)`.  It does **not** choose compatible local cyclic
orders, prevent labelled collisions between different order banks, or prove
the coefficient-one construction.  The remaining issue is a genuinely
order-level multirank alignment theorem.

## 1. Setup and exact profile capacity

Let `b` tend to infinity through odd primes and put

\[
 W_b={2b\choose b},\qquad M_q={2b\choose b+q}.
\]

Let `H=H(b)` satisfy

\[
 H/\sqrt b\longrightarrow\infty,qquad H=o(b^{2/3}). \tag{1.1}
\]

For `1<=q<=H` and `q<=s<=b`, the rank-`(b+q)` split profile with `s`
letters on the first `b`-set and `b+q-s` on the second has size

\[
 P_{q,s}={b\choose s}{b\choose s-q},qquad
 \sum_sP_{q,s}=M_q.                                  \tag{1.2}
\]

Write `c_j=binom(b,j)`.  Conditionally assume, for every admissible `r`, a
tight-cycle factor of the rank-`r` subsets of `A` and one of the
rank-`(b-r)` subsets of `B` (the growing-rank Baranyai--Katona input); each
has `c_r/b` cyclic orders.  Pool these order pairs and use the clustered
schedules `tau_r=A^rB^(b-r)`.  On every central profile for which all
`r=s-z`, `0<=z<=q`, are admissible, the resulting formal phase-diagonal
occurrence capacity is

\[
 T_{q,s}={1\over b}\left[
 (b-s-q+1)c_s^2+(s-2q+1)c_{s-q}^2
 +2\sum_{z=1}^{q-1}c_{s-z}^2\right].                \tag{1.3}
\]

Indeed, for a fixed payload `r`, a cyclic `q`-phase interval in
`A^rB^(b-r)` contains zero `A` phases in `b-r-q+1` positions, all `q` in
`r-q+1` positions, and exactly `z` in two positions for every
`1<=z<=q-1`.  Solving `s=r+z`, multiplying by the number
`c_r^2/b^2` of local order pairs and by `b` points per phase diagonal, and
summing over `z` gives (1.3).

Profiles with, say, `s` outside `[b/4,3b/4]` have total mass
`e^{-Omega(b)}M_q`, uniformly for `q<=H`.  For large `b`, every `s` in that
central interval and every `0<=z<=q` gives an admissible payload
`H+2<=s-z<=b-H-2`.  It is therefore enough to bound the positive part of
`P_(q,s)-T_(q,s)` on these central profiles.  For definiteness set
`T_(q,s)=0` outside this central admissible range, so those exceptional
profiles are charged in full below.

## 2. A pointwise deficit localization

### Lemma 2.1

Uniformly for `q<=H` and central `s`, put

\[
 a=c_s,\qquad c=c_{s-q},\qquad R={a\over c}=e^u,\qquad
 x=s-{b+q\over2}.
\]

Then

\[
 {T_{q,s}\over P_{q,s}}
 \ge 1-{q\over b}+{u^2\over4}                       \tag{2.1}
\]

for all sufficiently large `b`.  Consequently, if `T_(q,s)<P_(q,s)`, then

\[
 |u|<2\sqrt{q/b},\qquad
 0<P_{q,s}-T_{q,s}\le {q\over b}P_{q,s}.             \tag{2.2}
\]

#### Proof

Log-concavity of the binomial coefficients gives, for `0<=z<=q`,

\[
 c_{s-z}\ge c_s^{1-z/q}c_{s-q}^{z/q},
\]

and hence

\[
 {c_{s-z}^2\over ac}\ge R^{1-2z/q}.
\]

The exponents in the sum over `1<=z<=q-1` occur in opposite pairs, so
`e^v+e^(-v)>=2` gives

\[
 \sum_{z=1}^{q-1}R^{1-2z/q}\ge q-1.                \tag{2.3}
\]

Put

\[
 A={b-s-q+1\over b},\qquad B={s-2q+1\over b}.
\]

Then `A+B=1-3q/b+2/b` and `A-B=-2x/b`.  Binomial symmetry and
unimodality give `sign(u)=-sign(x)`, so `(A-B)sinh(u)>=0`.  Therefore

\[
 Ae^u+Be^{-u}
 =(A+B)\cosh u+(A-B)\sinh u
 \ge(A+B)\cosh u.                                   \tag{2.4}
\]

Divide (1.3) by `ac`, use (2.3), (2.4), and
`cosh u>=1+u^2/2`.  Since `q<=H=o(b)`, eventually
`A+B>=1/2`, and

\[
 {T_{q,s}\over P_{q,s}}
 \ge 1-{q\over b}+{u^2\over4}.
\]

This is (2.1), and (2.2) follows immediately.  \(\square\)

### Lemma 2.2

If `T_(q,s)<P_(q,s)`, then

\[
 \left|s-{b+q\over2}\right|
 \le {b+1\over2\sqrt{bq}}=O(\sqrt{b/q}).            \tag{2.5}
\]

#### Proof

Let `d=(b+1)/2`.  The exact product formula for `R` is

\[
 u(x)=\sum_{j=0}^{q-1}
 \log {d-(x+j-(q-1)/2)\over d+(x+j-(q-1)/2)}.       \tag{2.6}
\]

The summands are `g(x+theta_j)`, where `g` is odd and

\[
 g'(y)=-{2d\over d^2-y^2}\le-{2\over d}=-{4\over b+1}.
\]

The offsets `theta_j` are symmetric, so `u(0)=0`; integrating the derivative
bound gives

\[
 |u(x)|\ge {4q|x|\over b+1}.                         \tag{2.7}
\]

Combine (2.7) with (2.2).  \(\square\)

## 3. Aggregate capacity theorem

### Theorem 3.1

The total split-profile capacity deficit of the clustered payload bank obeys

\[
 \sum_{q=1}^H\sum_s [P_{q,s}-T_{q,s}]_+
 =O(W_b b^{-1/4})=o(W_b),                            \tag{3.1}
\]

where profiles outside the central admissible range are charged in full.

#### Proof

The distribution `P_(q,s)/M_q` is hypergeometric: it is the number of
chosen points in one `b`-set when a uniformly random `(b+q)`-subset of a
`2b`-set is sampled.  Uniformly for `q=o(b)`, Stirling's bounds give

\[
 \max_s {P_{q,s}\over M_q}=O(b^{-1/2}).              \tag{3.2}
\]

For completeness, (3.2) follows by applying
`binom(N,k)=Theta(2^{NH(k/N)}/sqrt(Np(1-p)))` uniformly on the central
range; the entropy exponent is maximized at `s=(b+q)/2`, and the two
square-root denominators divided by the corresponding denominator for
`M_q` leave `Theta(b^{-1/2})`.  Outside a fixed central interval the same
entropy bound is exponentially smaller.

By Lemma 2.2, at rank `q` only `O(sqrt(b/q))` profiles can have positive
deficit.  Equations (2.2) and (3.2) therefore give

\[
 \sum_s[P_{q,s}-T_{q,s}]_+
 \le O\left({\sqrt q\over b}\right)M_q
      +e^{-\Omega(b)}M_q.                            \tag{3.3}
\]

Moreover

\[
 {M_q\over W_b}
 =\prod_{j=1}^q{b-j+1\over b+j}
 \le\exp\left(-{q^2\over2b}\right)                 \tag{3.4}
\]

for `q<=H=o(b)`, since
`log((b-j+1)/(b+j))<=-(2j-1)/(b+j)` and
`b+j<=2b`.  Finally,

\[
 \sum_{q\ge1}\sqrt q\,e^{-q^2/(2b)}=O(b^{3/4})     \tag{3.5}
\]

by comparison with the corresponding integral.  Summing (3.3) and using
(3.4)--(3.5) proves (3.1); the exponentially small tail-profile charge is
negligible.  \(\square\)

## 4. Exact consequence and remaining gate

The earlier rigid one-to-one bank has a `(1/2-o(1))W_b` phase-hole ledger,
but that ledger is not a split-profile **capacity** obstruction.  The
surplus multiplicities contributed by neighboring payload ranks are
numerically sufficient to absorb all but `O(W_b b^(-1/4))` of the profile
demand.

What is not proved is an integral assignment of labelled target sets to
actual local order pairs which realizes this capacity simultaneously across
all ranks, uses compatible orientations/endpoints, and serializes the chosen
atoms without cross-atom window collisions.  Formula (3.1) identifies that
remaining problem sharply: it is a coherent multirank order-bank
transport/matching theorem, not a shortage of phase or split-profile volume.
