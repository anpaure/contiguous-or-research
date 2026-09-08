# Random trace spread and low-expansion localization of the remaining Ore cuts

**Date:** 2026-08-04  
**Status:** unconditional asymptotic pure-mathematical theorem.  It chooses
the private common-core witness paths so that every lower star has
**constant** protected internal-owner load and private endpoint
exposure.  The `2m` endpoints of the deterministic top bank are priced
separately.  The resident high-trace greedy packing preserves these
bounds.  Consequently
every protected Ore cut with ordinary weighted expansion larger than an
absolute constant per lower vertex is automatically safe.  This does not close
the residual low-expansion cut family.

## 0. Setup

Use the full-size common-core ring and hybrid clipped-resident reservoir.
Thus

\[
 K\sqcup E=[2m-1],\qquad |K|=m-1,\quad |E|=m,
\]

and every private low target is `K union T`, where `T subset E` is
noninterval and

\[
                         3\le q=|T|\le m-d-1.
\tag{0.1}

Put

\[
                         h=m-q\ge d+1,\qquad n=m-1.
\]

For each such `T`, independently choose a uniformly random cyclic order of
`K` together with a cut, and take the `q` consecutive `h`-windows

\[
 W_{T,0},W_{T,1},\ldots,W_{T,q-1}
\]

whose linear span is all of `K`.  The owners

\[
                         T\cup W_{T,j}
\tag{0.2}

form the low path of the hybrid reservoir.  Every owner, immediate-lower
colour, and immediate-upper colour has exact external trace `T`, so paths
for different `T` remain resource-disjoint for every choice of the orders.

This random choice **replaces** the common-`G_2` alignment used in the
earlier deterministic singleton construction.  The two choices cannot be
imposed simultaneously: a common internal deletion window for every
triple would create linear load at the corresponding lower star.  The
spread theorem below supplies the singleton inequalities directly, since
`R_0=10<m-2` for all sufficiently large `m`.

For a lower vertex `x`, define

* `l_P(x)=lambda_P({x})`, its singleton protected loss; and
* `e_P^{\rm priv}(x)` to be the number of protected path endpoints outside
  the deterministic top bank which contain `x` and whose unique protected
  lower neighbour is not `x`.

The second quantity overcounts the endpoint terms from the private and
high banks.  The top bank has exactly `2m` endpoints, so its entire
contribution to any cut is at most `2m`.  This separation is necessary:
the common core `K`, for example, lies below all `m` starting endpoints of
the top paths.

## 1. Uniform fixed-trace marginals

### Lemma 1.1

For fixed `T`, every rank-`h` subset of `K` occurs as a path owner with
probability

\[
                         {q\over {n\choose h}}.
\tag{1.1}

Every fixed owner candidate occurs as one of the two path endpoints with
probability

\[
                         {2\over {n\choose h}}.
\tag{1.2}

#### Proof

The random order is invariant under `Sym(K)`, so each of the `q` owner
positions has the uniform rank-`h` marginal.  The windows in one path are
distinct; summing their disjoint position events gives (1.1).  The same
argument at the two distinct endpoints gives (1.2). \(\square\)

The low paths are monotone at the level of their moving `K` windows: any
two nonconsecutive owners differ in at least two exchanges.  Hence a fixed
lower vertex can be contained in at most two consecutive owners of one
path.  If two occur, their intersection is that lower vertex, so neither
creates singleton loss.  Therefore one private path contributes at most
one unit to `l_P(x)` and at most one unit to `e_P^{\rm priv}(x)`.

## 2. Constant mean at every lower star

Fix a lower vertex `x`, and write

\[
 S=x\cap E,\qquad D=K\setminus x,\qquad |S|=|D|=s.
\tag{2.1}

An owner over `x` has external trace either `S` or `S union {z}` for one
`z in E-S`.  The trace-`S` path contributes at most one singleton or
endpoint unit deterministically.  For `T=S union {z}`, one has `q=s+1` and
the required `K`-part is the fixed set `K-D` of size `m-s-1`.  Lemma 1.1
gives the upper bounds

\[
 \mu_l(s)\le
 (m-s){s+1\over {m-1\choose s}},
\tag{2.2}

and

\[
 \mu_e(s)\le
 (m-s){2\over {m-1\choose s}}.
\tag{2.3}

For the random low bank one has `2<=s<=m-3`.  The function

\[
 { (m-s)(s+1)\over {m-1\choose s}}
\]

decreases and then increases on this range, so its maximum is attained at
an endpoint and is `6/(m-1)`.  The endpoint mean is smaller.  The fixed
top cyclic-interval bank contributes only an absolute constant to
`l_P(x)`, by the cyclic deletion/addition lemma, and the possible
own-trace private path adds at most one to either load.  Thus `l_P(x)` and
`e_P^{\rm priv}(x)` are an absolute deterministic contribution plus a sum
of independent Bernoulli variables of mean at most `6/(m-1)`.

### Theorem 2.1 (simultaneous star spread)

For all sufficiently large `m`, the low path orders can be chosen so that

\[
 \boxed{
  \max_x l_P(x)\le R_0,\qquad
  \max_x e_P^{\rm priv}(x)\le R_0,\qquad
  R_0=10.}
\tag{2.4}

#### Proof

Put `B_s={m-1\choose s}`.  The number of lower vertices with external
size `s` is

\[
 N_s={m\choose s}{m-1\choose s}={m\over m-s}B_s^2.
\tag{2.5}

For either random load, the standard exponential-moment bound gives

\[
 \Pr(X\ge6)\le
 \left({e(m-s)(s+1)\over6B_s}\right)^6.
\tag{2.6}
\]

Consequently the sum of all bad-event probabilities is at most

\[
 \sum_{s=2}^{m-3}
 {m(m-s)^5\bigl(e(s+1)/6\bigr)^6\over B_s^4}=o(1).
\tag{2.7}
\]

Indeed, the two endpoint terms `s=2,m-3` are `O(m^{-1})`; the next two are
smaller; and for `4<=s<=m-5`, one has
`B_s>={m-1\choose4}`, making each summand `O(m^{-4})`.
Thus one choice makes every random contribution at most five.

For the top bank, the cyclic deletion lemma gives at most two harmful
`K`-additions and the cyclic addition lemma at most two harmful
`E`-additions.  The own-trace private path contributes at most one.
Therefore `l_P(x)<=5+4+1=10`, while
`e_P^{\rm priv}(x)<=5+1<=10`. \(\square\)

No resource collision is introduced by this random choice: exact external
trace separates different private paths, and every single path is already
simple and clipped resident.

## 3. The high resident tail preserves the spread

The high traces are packed by the symmetric monotone-geodesic greedy theorem
in the hybrid reservoir.  We strengthen its forbidden set adaptively.

### Lemma 3.1

One monotone Johnson geodesic increases each of `l_P(x)` and
`e_P^{\rm priv}(x)` by at most one for every fixed lower vertex `x`.

#### Proof

If two path owners contain `x`, monotonicity forces them to be consecutive;
their intersection is `x`, so they create no singleton loss.  Thus at most
one internal owner is harmful.  The two endpoints of a geodesic of length
at least two cannot both be rank-`m` supersets of the same rank-`m-1` set,
so endpoint exposure also rises by at most one.  The bounded exceptional
two-owner case satisfies the same conclusion directly. \(\square\)

### Theorem 3.2 (spread-preserving high packing)

The high monotone geodesics can be selected, still pairwise disjoint in all
three resource ranks, so that after their addition

\[
                         l_P(x),e_P^{\rm priv}(x)\le R_0
                         \qquad(x\in\mathcal L).
\tag{3.1}

#### Proof

At each greedy step, call `x` critical for one of the two loads if that load
equals `R_0`.  The total load summed over all `x` is at most `m` times the
number of resources already selected.  Hence the number of critical lower
vertices is at most a polynomial factor times `2^m+H_d`, where

\[
                         H_d=\sum_{j\le d}{m\choose j}=2^{o(m)}.
\]

Forbid every owner containing any critical lower vertex.  This enlarges the
hybrid theorem's forbidden owner bank by only

\[
                         O(m^2(2^m+H_d))
\tag{3.2}

resources.  Its random high geodesic has central-binomial resource supply
`2^(2m-o(m))`, so the same union bound is now

\[
 {O(m^4(2^m+H_d))\over2^{2m-o(m)}}
 =2^{-m+o(m)}<1.
\]

A legal geodesic therefore remains at every step.  It avoids every critical
star, while Lemma 3.1 raises every noncritical load by at most one.
Induction proves (3.1). \(\square\)

## 4. Every moderately expanding Ore cut is safe

For a lower cut `A`, the exact path-forest identity is

\[
 \lambda_P(A)=
 \sum_{x\in A}l_P(x)
 -\sum_{U:d_P(U)=2}(a_U-2)_+
 +E_1(A),
\tag{4.1}

where `a_U=|N(U)\cap A|` and `E_1(A)` counts endpoint owners with at least
two facets in `A` whose protected edge goes outside `A`.

Every private or high endpoint counted by `E_1(A)` contains at least two
members of `A`, and is consequently counted in `e_P^{\rm priv}(x)` for at
least two such `x`.  There are only `2m` top endpoints.  Therefore

\[
 E_1(A)\le {1\over2}\sum_{x\in A}e_P^{\rm priv}(x)+2m.
\tag{4.2}

Discarding the favourable middle term in (4.1) and applying (2.4),(3.1)
gives

\[
 \boxed{
                         \lambda_P(A)\le {3R_0\over2}|A|+2m
                         =15|A|+2m.}
\tag{4.3}

### Theorem 4.1 (low-expansion localization)

Every cut satisfying

\[
                         \sigma(A)\ge 15|A|+2m
\tag{4.4}

is safe.  Hence every failed cut obeys both

\[
 \boxed{
  \sigma(A)<15|A|+2m,}
\tag{4.5}

and

\[
 \boxed{
  \sum_U(a_U-2)_+
  >(m-17)|A|-2m.}
\tag{4.6}

Its upper-shadow surplus also satisfies

\[
 \boxed{
  |N(A)|-|A|
  <{m-1\over m-2}
    \left(15|A|+2m\right).}
\tag{4.7}

#### Proof

Equation (4.3) and the protected Ore criterion prove (4.4)--(4.5).
Regularity gives the exact identity

\[
 \sigma(A)=(m-2)|A|-\sum_U(a_U-2)_+,
\]

which proves (4.6).  Finally the frozen shadow inequality

\[
 \sigma(A)\ge {m-2\over m-1}(|N(A)|-|A|)
\]

gives (4.7). \(\square\)

Combining this theorem with the frozen near-shadow localization, a failed
cut must now be simultaneously:

1. small or co-small of size `O(m^2 2^m)`;
2. outside the automatically safe complement range `<=m-2`;
3. of weighted expansion only `O(1)` per selected lower vertex (up to the
   additive `2m` top-endpoint bank); and
4. almost maximally clique-overlapped in the exact sense (4.6).

## 5. Every zero-clique-defect cut is safe

The frozen equality classification says that `b(A)=0` exactly when

\[
 A=\mathop{\dot\bigcup}_i{S_i\choose m-1},
 \qquad |S_i\cap S_j|\le m-3.
\tag{5.1}

The spread theorem closes this entire family.

Fix one support `S`, put

\[
 t=|S|,\qquad u=(2m-1)-t,
 \qquad A_S={S\choose m-1}.
\tag{5.2}

An upper owner meeting `A_S` has either all `m` facets in `A_S` (when it
lies inside `S`) or exactly one such facet (when it contains one point
outside `S`).  Define `theta_P(S)` to be the number of latter boundary
owners whose protected degree is two and neither protected lower incidence
is their unique `S`-facet.

### Lemma 5.1 (exact one-support cut)

For every `S` of size at least `m-1`,

\[
 \boxed{
  \lambda_P(A_S)=\theta_P(S),
  \qquad
  \sigma(A_S)={u(m-2)\over m}{t\choose m-1}.}
\tag{5.3}

Moreover,

\[
                         \theta_P(S)\le
                         \sum_{x\in A_S}l_P(x).
\tag{5.4}

#### Proof

An internal owner contained in `S` has `a_U=m` and no protected edge to the
complement, so contributes zero.  A boundary owner has `a_U=1`; its local
loss is one exactly in the definition of `theta_P(S)`.  This proves the
first identity.  Every such occurrence is also a harmful internal owner in
the singleton cut of its unique `S`-facet, proving (5.4).

The upper shadow consists of the internal owners and the boundary owners.
Equivalently, substitute

\[
 {t\choose m}={t\choose m-1}{t-m+1\over m},
 \qquad 2m-2-t=u-1
\]

in the exact equality-cut slack formula.  It gives

\[
 {m-2\over m-1}
 \left[{t\choose m}+(2m-2-t){t\choose m-1}\right]
 ={u(m-2)\over m}{t\choose m-1}.
\]

\(\square\)

### Theorem 5.2 (all `b=0` cuts pass)

For the spread reservoir and all sufficiently large `m`, every cut with
`b(A)=0` satisfies the protected Ore inequality.

#### Proof

First consider one support.  By (2.4) and (5.4),

\[
                         \theta_P(S)\le
                         R_0{t\choose m-1}.
\]

This is at most the right side of (5.3) whenever

\[
                         {u(m-2)\over m}\ge R_0.
\tag{5.5}

If `u=0`, then `A_S=mathcal L` and the cut is trivially safe.  It remains
to treat

\[
                         1\le u<{mR_0\over m-2}=O(1).
\tag{5.6}

The complete protected reservoir has only

\[
                         M_P=O(m2^m+mH_d)=2^{m+o(m)}
\tag{5.7}

internal owners.  Hence `theta_P(S)<=M_P`.  On the other hand, uniformly
under (5.6),

\[
 {t\choose m-1}
 ={2m-1-u\choose m-1}=2^{2m-o(m)}.
\tag{5.8}

Thus the slack in (5.3) exceeds `M_P` for every `u>=1` and all sufficiently
large `m`.  This closes every one-support cut.

For (5.1), no upper owner can meet two different component families: two
distinct facets of one owner intersect in `m-2` points, contradicting the
support-intersection bound.  Therefore both `lambda` and `sigma` split
additively over the supports `S_i`.  Every summand is safe, so their union
is safe. \(\square\)

Consequently every failed cut left by Theorem 4.1 has **positive**
clique-closure defect `b(A)>0`; all exact equality cases of the
shadow-slack inequality have disappeared.

## 6. Every principal up-star is safe

The other canonical small-shadow family is a principal up-star.  Fix
`C\subseteq[2m-1]`, put `c=|C|`, `r=m-c`, and define

\[
 \mathcal A_C={x\in\mathcal L:C\subseteq x\}.
\tag{6.1}
\]

### Lemma 6.1 (star loss is a path-crossing count)

Assume `2\le r\le m-1`.  Then

\[
 \boxed{\lambda_P(\mathcal A_C)=
 \#\{\text{protected path edges crossing }
       \{U\in\mathcal U:C\subseteq U\}\}.}
\tag{6.2}
\]

Every protected path contributes at most two crossings.

#### Proof

An upper owner containing `C` has exactly `r` lower facets in
`\mathcal A_C`; every other owner has none.  Since `r\ge2`, its contribution
to protected loss is the number of its protected incidences whose lower
facet does not contain `C`.  Along a Johnson edge this happens exactly
when one endpoint owner contains `C` and the other does not, proving
(6.2).

Every coordinate has one occurrence interval along each top, sliding, or
monotone-geodesic path.  The owners containing every coordinate of `C`
therefore form the intersection of intervals, hence an interval.  Such an
interval has at most two boundary edges. \(\square\)

Write

\[
 a=|C\cap K|,\qquad |C\cap E|=c-a.
\tag{6.3}
\]

A low fixed-trace path can meet the star only if its external trace
contains `C\cap E` and has size at most `m-a`.  Hence the number of such
paths is at most

\[
 \sum_{j=0}^{r}{r+a\choose j}
 \le H_r(m):=\sum_{j=0}^{r}{m\choose j}.
\tag{6.4}
\]

The top bank contributes only `m` paths, and the high bank at most
`H_d=2^{o(m)}` paths.  Lemma 6.1 gives

\[
 \lambda_P(\mathcal A_C)\le
 2\bigl(H_r(m)+m+H_d\bigr).
\tag{6.5}
\]

### Theorem 6.2 (principal-star closure)

For all sufficiently large `m`, every principal up-star
`\mathcal A_C` satisfies the protected Ore inequality.

#### Proof

The cases `c=0` and `r=1` are respectively the full cut and a singleton;
the latter is safe because `\lambda_P\le R_0<m-2`.

Now let `2\le r\le m-1`.  Direct counting gives

\[
 |\mathcal A_C|={m+r-1\choose r-1},
\qquad
 \boxed{\sigma(\mathcal A_C)=
 {2c\over m}{m+r-1\choose r}
 ={2c\over r}|\mathcal A_C|.}
\tag{6.6}
\]

If `r\le m/10`, then `2c/r\ge18`.  Since
`|\mathcal A_C|\ge m+1` for `r\ge2`, the general bound (4.3) gives

\[
 \lambda_P(\mathcal A_C)\le15|\mathcal A_C|+2m
 <18|\mathcal A_C|\le\sigma(\mathcal A_C).
\]

Suppose `m/10\le r\le m/2`.  Then

\[
 H_r(m)\le(r+1){m\choose r},
\]

while

\[
 {{m+r-1\choose r}\over {m\choose r}}
 =\prod_{j=1}^{r}{m-1+j\over m-r+j}
 \ge\left(1+{r-1\over m}\right)^r
 =\exp(\Omega(m)).
\tag{6.7}
\]

Here `2c/m\ge1`, so (6.6)--(6.7) dominate (6.5), including the
subexponential `H_d` term.

Finally suppose `m/2\le r\le m-1`.  Then `H_r(m)\le2^m`, whereas

\[
 {m+r-1\choose r}
 \ge {\lfloor3m/2\rfloor-1\choose\lfloor m/2\rfloor}
 =2^{(\frac32 H_2(1/3)+o(1))m}.
\tag{6.8}
\]

Since `\frac32H_2(1/3)>1` and `2c/m\ge2/m`, (6.6) again dominates
(6.5).  Thus every star is safe. \(\square\)

Principal up-stars are the complements of the exact colex families which
attain the Lovasz--Kruskal--Katona lower-shadow bound.  The protected bank
therefore passes both canonical extremal geometries: the zero-defect
down-clique unions of Section 5 and every principal up-star.  What remains
is a stability problem for partial/colex-perturbed extremizers.

## 7. Exact frontier

The randomization used here is only an existence proof over finite cyclic
orders; no computation or sampled assertion occurs.  It preserves the
explicit target witnesses, q1 simplicity, common-core ring covariance, and
clipped residence.

The residual extension theorem is now sharply concentrated on small or
co-small, low-expansion, **positive-defect** nearly clique-closed lower
families.  Proving that such a family cannot violate the residual
path-forest Hall inequality—or constructing an additional deterministic
anti-clique balancing rule—is the remaining factor row.  Component
distribution, endpoint collar closure, and the common cap remain separate.
