# Wreath LP duality, unavoidable collisions, and a relaxed transfer target

## Status

This note does **not** prove the weak vertical wreath lemma.  It proves three
things about that lemma.

1.  The entire all-depth wreath covering problem is feasible with zero
    defect in the natural fractional set-partitioning relaxation.  Thus no
    LP dual involving only middle ownership and shadow-cover constraints can
    obstruct the lemma.
2.  The exact unavoidable collision mass through the required growing band
    is computed.  The desired lemma asks for additive optimality `o(W)` over
    a forced collision term of order `WH`; equivalently its permitted
    relative loss among all required shadow colours is `o(m^{-1/2})`.
3.  Exact middle ownership can be dropped altogether.  A family of almost
    `Cat_m` cyclic orders with `o(W)` aggregate missing masks in the whole
    band still gives a literal OR word of length `W+o(W)`.  This is a
    strictly more flexible integral target if exact wreath factors prove too
    rigid.

Throughout,

\[
 n=2m+1,\qquad W=\binom n m,\qquad B=W/n=\operatorname{Cat}_m.
\]

For an oriented cyclic order `pi` (taken modulo rotation), write

\[
 I_\pi(j,r)=\{\pi_j,\ldots,\pi_{j+r-1}\}.
\]

## 1. Exact fractional vertical resolution

Let `P_n` be the set of all oriented cyclic orders on `[n]`, modulo
rotation.  Thus `|P_n|=(n-1)!`.

### Theorem 1 (uniform fractional all-depth wreath factor)

Assign every `pi in P_n` the weight

\[
 x_\pi=\frac1{m!(m+1)!}.
\tag{1.1}
\]

Then:

* every middle set `A in binom([n],m)` has total interval load exactly one;
* for every `1 <= r <= m` and every `S in binom([n],r)`, the total load of
  cyclic orders in which `S` is an `r`-interval is

\[
 \lambda_r=\frac{\binom n m}{\binom n r}\ge1;
\tag{1.2}
\]

* every complementary `(n-r)`-set has the same load; and
* the total weight of the cyclic orders is exactly `B`.

In particular, the fractional set-partitioning LP

\[
 \sum_{\pi:A\text{ is an }m\text{-interval of }\pi}x_\pi=1
 \quad(A\in\tbinom{[n]}m),
\tag{1.3}
\]

\[
 \sum_{\pi:S\text{ is an }r\text{-interval of }\pi}x_\pi\ge1
 \quad(1\le r\le m,\ S\in\tbinom{[n]}r),
\tag{1.4}
\]

is feasible simultaneously at **all** depths.

#### Proof

Fix an `r`-set `S`, with `r<n`.  Make `S` one consecutive block.  Its
elements have `r!` internal orders, and the resulting block together with
the `n-r` remaining labelled elements has `(n-r)!` oriented circular
orders.  Hence exactly

\[
 r!(n-r)!
\tag{1.5}
\]

members of `P_n` contain `S` as a cyclic interval.  For `r=m`, multiplying
(1.5) by (1.1) gives one.  For general `r`, it gives

\[
 \frac{r!(n-r)!}{m!(m+1)!}
 =\frac{\binom n m}{\binom n r},
\]

which is at least one because the middle layer is largest.  The complement
of a cyclic interval is a cyclic interval, proving the upper-rank assertion.
Finally,

\[
 \sum_{\pi\in P_n}x_\pi
 =\frac{(n-1)!}{m!(m+1)!}=B.
\]

This proves every claim. `square`

### Corollary 1.1 (no linear-dual obstruction)

No Farkas/LP-dual certificate using only nonnegative wreath variables,
exact middle ownership, and arbitrary weighted lower/upper shadow-cover
constraints can prove that a vertical wreath resolution is impossible.
The uniform point (1.1) satisfies every such cover constraint, at every
depth, with the exact middle mass `B`.

This does not round the solution.  It locates the obstruction, if one
exists, in correlated integrality rather than fractional capacity.

There is an equivalent collision statement.  At depth `q`, put

\[
 r=m-q,\qquad N_q=\binom n{m-q},\qquad
 \lambda_q=W/N_q.
\]

Every target has fractional load `lambda_q`, so the fractional duplicate
mass is exactly

\[
 \sum_{S\in\binom{[n]}{m-q}}(\lambda_q-1)
 =W-N_q.
\tag{1.6}
\]

Thus the fractional solution attains the information-theoretic collision
minimum simultaneously at all depths.

The same symmetric point satisfies even the nested fractional version of
the stronger SCD target.

### Corollary 1.2 (exact fractional cyclic-interval SCD)

For `0<=q<=m`, put

\[
 R_q=\frac{\binom n{m-q}}W,
 \qquad R_{m+1}:=0,
 \qquad p_d:=R_d-R_{d+1}.
\tag{1.7}
\]

The numbers `p_d` form a probability distribution on radii
`d in {0,...,m}`.  Split every pointed cyclic order `(pi,j)` of weight
`x_pi` into a radius-`d` symmetric chain with weight `x_pi p_d`, namely

\[
 I_\pi(j,m-d)\subset\cdots\subset I_\pi(j,m)
 \subset I_\pi(j,m+1)\subset\cdots\subset I_\pi(j,m+1+d).
\tag{1.8}
\]

Then every Boolean mask, including the empty and full masks, has total
chain load exactly one.

Indeed, the fraction of a pointed chain surviving to depth `q` is

\[
 \sum_{d\ge q}p_d=R_q.
\]

A fixed rank-`m-q` target has unrestricted load `lambda_q=W/N_q` by
Theorem 1, so its active load is `lambda_q R_q=1`; complementation gives
the upper member.  The case `q=m` also works: the total pointed-chain mass
is `W` and `R_m=1/W`, giving the empty and full masks load one.

Thus even nesting, exact rank quotas, and simultaneous lower/upper balance
have no fractional obstruction.  The missing theorem is wholly the
integral coupling of those radius decisions with one exact middle factor.

There is also no hidden central-factor integrality issue in (1.1).  Fix any
one exact middle wreath factor (for example the MSW factor), orient its
`B` wreaths, and average all its coordinate relabellings by `Sym(n)`.
The group is transitive on `P_n`, so every oriented cyclic order occurs with
the same average weight.  Total weight is `B`, forcing that weight to be

\[
 B/(n-1)!=1/[m!(m+1)!].
\]

Hence the uniform point is in the convex hull of incidence vectors of
bona fide exact middle factors.  What fails to commute with this averaging
is the nonlinear hole indicator `1_{mu_q(S)=0}`; this is precisely the
integrality/correlation gap left by the theorem.

More explicitly, symmetrize any probability distribution on exact factors.
For a fixed depth-`q` target, let `Z_q` be its random multiplicity.  Then

\[
 \mathbb E Z_q=\lambda_q,
 \qquad
 \Pr(Z_q=0)
 =\mathbb E(Z_q-1)_+-(\lambda_q-1).
\tag{1.9}
\]

The identity is just `(z-1)_+=z-1_{z>=1}`.  Thus the missing probability
is exactly the Jensen gap above the fractional collision floor.  Linear
moments determine `lambda_q` but cannot control this gap.  Independent or
Poisson-like rounding has a large gap; the desired construction must force
`Z_q>0` almost always by correlated integral choices.

## 2. The exact integral collision floor

Let `F` be an exact integral middle wreath factor.  For a rank-`m-q` set
`S`, let `mu_q(S)` be its number of cyclic-interval occurrences and put

\[
 E_q=\sum_S(\mu_q(S)-1)_+,
 \qquad
 M_q=\#\{S:\mu_q(S)=0\}.
\]

There are exactly `W` slots at every depth.  Therefore

\[
 \boxed{E_q=(W-N_q)+M_q.}
\tag{2.1}
\]

This is the global collision ledger in its most direct form.  Summing to
depth `H` gives

\[
 \sum_{q=1}^H E_q=L_H+\sum_{q=1}^H M_q,
 \qquad
 L_H:=\sum_{q=1}^H(W-N_q).
\tag{2.2}
\]

Hence the weak vertical wreath condition is exactly

\[
 \sum_{q=1}^H E_q=L_H+o(W).
\tag{2.3}
\]

### Proposition 2.1 (size of the unavoidable term)

Assume

\[
 H/\sqrt m\longrightarrow\infty,
 \qquad H=o(m^{2/3}).
\]

Then

\[
 \sum_{q=1}^H\frac{N_q}{W}
 =\left(\frac{\sqrt\pi}{2}+o(1)\right)\sqrt m,
\tag{2.4}
\]

and consequently

\[
 \boxed{L_H
 =W\left(H-\left(\frac{\sqrt\pi}{2}+o(1)\right)\sqrt m\right).}
\tag{2.5}
\]

#### Proof

The exact ratio is

\[
 R_q:=\frac{N_q}{W}
 =\prod_{i=0}^{q-1}\frac{m-i}{m+2+i}.
\tag{2.6}
\]

Taylor expansion, uniformly for `q=o(m^{2/3})`, gives

\[
 \log R_q
 =-\frac{q(q+1)}m+\frac{q(q+1)}{m^2}
   +O\!\left(\frac{q^4}{m^3}\right).
\tag{2.7}
\]

On every fixed window `q <= K sqrt(m)`, (2.7) turns the sum into the
Riemann sum for `integral_0^K exp(-x^2) dx`.  The remaining terms are
bounded by a Gaussian uniformly in `m`; first let `m -> infinity` and then
`K -> infinity`.  Since `H/sqrt(m) -> infinity`, this proves (2.4).
Equation (2.5) follows from the definition of `L_H`. `square`

For the tail-compatible value

\[
 H=(1/2+\varepsilon)\sqrt{n\log n},
\]

the forced duplicate mass is `(1-o(1))WH`.  The desired theorem permits
only `o(W)` additional collisions.  Thus it requires relative accuracy
`o(1/H)` above the collision floor.

Equivalently, the total number of required lower shadow colours is

\[
 \sum_{q=1}^H N_q
 =\left(\frac{\sqrt\pi}{2}+o(1)\right)W\sqrt m,
\tag{2.8}
\]

and `sum M_q=o(W)` is relative uncovered mass `o(m^{-1/2})`.  This is why a
routine `o(1)`-relative nibble estimate is quantitatively insufficient.

The scale also distinguishes harmless finite seams from a real
obstruction.  Since `B=W/n=Theta(W/m)`, a uniform bound

\[
 M_q=O(Bq^a)
\]

would contribute

\[
 O(BH^{a+1})
 =O\!\left(Wm^{(a-1)/2}(\log m)^{(a+1)/2}\right)
\tag{2.9}
\]

at the stated depth.  Catalan-scale `O(B)` defects per depth are harmless,
whereas a genuine lower bound of order `qB` over a positive fraction of the
shallow depths would already be large enough to defeat this particular
wreath target.  No such lower bound is presently known.

## 3. A local host constraint, and why it is not an obstruction

### Proposition 3.1 (disjoint middle hosts)

For every exact middle wreath factor and every rank-`m-q` target `S`,

\[
 \boxed{(q+1)\mu_q(S)
 \le \binom{m+q+1}{q}.}
\tag{3.1}
\]

#### Proof

One occurrence of `S` as a cyclic interval is contained in exactly `q+1`
of the length-`m` cyclic intervals of that wreath: extend its left and right
ends by a total of `q` positions.  Two distinct occurrences of `S` cannot
use the same middle host.  Occurrences in different wreaths have disjoint
middle hosts because the factor partitions the middle layer, and an
`(m-q)`-set occurs at most once in one cyclic order.  Hence the `q+1` hosts
per occurrence are disjoint subsets of the complete family of middle
supersets of `S`.  That family has size

\[
 \binom{n-(m-q)}q=\binom{m+q+1}q.
\]

This proves (3.1). `square`

At `q=1`, (3.1) is the known matching cap

\[
 \mu_1(S)\le\left\lfloor\frac{m+2}{2}\right\rfloor.
\]

For growing `q`, however, the right side is enormous compared with the mean
load `W/N_q`.  It supplies no positive lower bound on `M_q`.  Together with
Theorem 1 and the verified `m=4` factor having `M_1=0`, this gives no sign of
an intrinsic capacity obstruction to `sum M_q=o(W)`.  What remains is a
very sharp integral correlation problem.

## 4. Exact middle ownership is not necessary

The following transfer theorem is a strictly weaker replacement target.

Let `P` be any multiset of `p` oriented cyclic orders; no middle
partition is assumed.  For `0<=q<=H`, let

\[
 U_q^-(P)=\bigcup_{\pi\in P}\{I_\pi(j,m-q):j\in\mathbb Z_n\},
\]

and put

\[
 M_q(P)=\binom n{m-q}-|U_q^-(P)|.
\tag{4.1}
\]

Complementation shows that the analogous upper family of rank `m+1+q`
has the same defect.

If `mu_q(S)` is the multiplicity in this arbitrary family and

\[
 D_q=\sum_S(\mu_q(S)-1)_+,
\]

then the exact missing-only ledger is

\[
 \boxed{M_q=\binom n{m-q}+D_q-pn.}
\tag{4.2a}
\]

Unlike the exact-factor formulation, there is no reason to minimize
`D_q` separately.  Only the resulting `M_q` enters the OR-word bound.

### Theorem 4 (relaxed cyclic-family transfer)

For every `1<=H<m`,

\[
 \boxed{
 \nu(n)\le
 p(n+2H+1)
 +2\sum_{q=0}^H M_q(P)
 +2\sum_{r=0}^{m-H-1}\binom nr-1.}
\tag{4.2}
\]

#### Proof

For every `pi in P`, set

\[
 E_j=I_\pi(j,m-H)
\]

and emit

\[
 E_0,E_1,\ldots,E_{n-1},E_0,E_1,\ldots,E_{2H}.
\]

For `1<=t<=2H+2`, every `t`-entry window within this block has union

\[
 I_\pi(j,m-H+t-1).
\]

Thus all masks in `U_q^-(P)` and their complementary upper families occur
as literal contiguous ORs.  The blocks have total length `p(n+2H+1)`.
Append every missing lower and upper band mask, then every nonempty mask in
the two outer tails.  This adds the second and third terms in (4.2); the
`-1` removes the empty lower-tail mask. `square`

### Corollary 4.1 (weak cyclic near-resolution suffices)

Suppose, for the tail-compatible `H`, there are cyclic families `P_m` such
that

\[
 p_m n=W+o(W),\qquad
 \sum_{q=0}^H M_q(P_m)=o(W).
\tag{4.3}
\]

Then

\[
 \nu(2m+1)=W+o(W).
\]

Indeed `p_m H=o(W)` because `H=o(n)`, and the two binomial tails are
`o(W)`.

This target permits `o(W)` missing and repeated middle masks, as well as
`o(B)` excess cyclic blocks.  The exact-factor weak vertical wreath lemma is
the special case `p=B` and `M_0=0`.  Therefore an obstruction tied to exact
middle partitioning would not by itself obstruct the OR construction.

## 5. Conclusions for the obstruction lane

The strongest rigorous conclusions are:

* the natural all-depth LP has an explicit symmetric feasible point with
  zero fractional defect;
* every integral factor must pay the collision floor (2.5), and the desired
  lemma asks for only `o(W)` excess above it;
* the local host constraints do not force holes;
* no universal positive lower bound on `sum M_q/W` follows from linear
  capacity, endpoint counts, or target multiplicity caps; and
* exact middle ownership is dispensable via Theorem 4.

Accordingly, `sum M_q=o(W)` remains mathematically plausible, but it is a
lossless integral-design statement, not a consequence of fractional
feasibility.  A genuine negative result must use a nonlinear integrality
invariant shared across depths.  If such an invariant is found only for
exact factors, the relaxed cyclic-family target (4.3) is the appropriate
replacement rather than abandonment of the constant-one programme.
