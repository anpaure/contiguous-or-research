# The canonical MSW first- and second-shadow collision energies are linear

Date: 2026-07-25

Method: pure symbolic counting; no finite enumeration is used.

## 0. Outcome

Put

\[
 n=2m+1,\qquad W=\binom{2m+1}{m},\qquad B=\operatorname{Cat}_m.
\]

For the canonical Mütze--Standke--Wiechert exact wreath factor, let

\[
 P_1=\sum_{|S|=m-1}\binom{\mu_1(S)}2
\]

be the number of unordered pairs of equal first-shadow occurrences.  The
two intrinsic even-core maps are

\[
 \alpha(x)=x\cap f(x),\qquad
 \Gamma(x)=g(f^{-1}x)\cup g(x).
\]

This note proves exact, nonrecursive inverse criteria for both maps and the
sharp-order estimate

\[
\boxed{P_1=\Theta(W).}
\tag{0.1}
\]

It also proves the first genuinely multistep extension:

\[
 \boxed{P_2=O(W),\qquad
 \|\mu_2-\lambda_2\mathbf1\|_2^2=O(W).}                        \tag{0.1a}
\]

The depth-two proof classifies the four feasible coupled-corridor order
types, gives a reversible renewal or finite-strip count for each, proves
an exact padding conjugacy for the upper sector, and controls all four
seam sectors by a fan injection.  Thus the entire second shadow, not just
one intrinsic sector, is included.

The upper bound includes the two exceptional endpoint colours of every
MSW column and all their cross-collisions with internal colours.  The lower
bound is the already symbolic marked-gap family; no finite enumeration is
used anywhere.

There cannot be a proof based on uniformly bounded intrinsic fibres.  For
every `k>=1`, a target in semilength `m=2k` has at least `k` preimages under
`Gamma`; see Section 4.

More precisely, the symbolic marked-gap collision family and the theorem
below give

\[
 \left(\frac1{16}+O(m^{-1})\right)W
 \le P_1\le C W
\tag{0.2}
\]

for an absolute constant `C`.  Equivalently,

\[
 \boxed{\|\mu_1-\lambda_1\mathbf1\|_2^2=O(W),
 \qquad \lambda_1={m+2\over m}.}
\tag{0.3}
\]

## 1. Path notation and the two pivot descriptions

Write an up-step as `1`, a down-step as `0`, and let `H_w(r)` be the
height of a path `w` immediately before position `r`.  For an interval
`I` of positions, write

\[
 U_h(w;I)=\#\{r\in I:w_r=1,\ H_w(r)=h\},
\quad
 D_h(w;I)=\#\{r\in I:w_r=0,\ H_w(r)=h\}.
\tag{1.1}
\]

An up-step touches the line `1` precisely when it starts at height `0` or
`1`.  A down-step touches the line `0` precisely when it starts at height
`0` or `1`.

The MSW maps have the following definitions.  On a balanced path `x`, the
map `g` flips the `(D_0(x)+1)`-st down-step touching line `0`, whereas
`g'` flips the `D_0(x)`-th such down-step.  On a path `y` ending at height
`2`, the maps `h` and `h'` flip respectively the `U_1(y)`-th and
`(U_1(y)+1)`-st up-steps touching line `1`.  Moreover,

\[
 h^{-1}=g',\qquad g^{-1}=h'.
\tag{1.2}
\]

Consequently:

* as `y` ranges over all length-`2m` paths ending at height `2`, the
  internal lower colours are obtained by flipping down the two consecutive
  touching-line-`1` up-steps of ranks `U_1(y)` and `U_1(y)+1`;
* as `x` ranges over the balanced paths in flaw classes `1,...,m-1`, the
  internal upper cores `Gamma(x)` are obtained by flipping up the two
  consecutive touching-line-`0` down-steps of ranks `D_0(x)` and
  `D_0(x)+1`.

The first statement follows because the two middle neighbours of `y` are
`h(y)` and `h'(y)=g^{-1}(y)`, whose intersection is `alpha`.  The second
follows from

\[
 \Gamma(x)=g'(x)\cup g(x).
\tag{1.3}
\]

## 2. Exact inverse criterion for `alpha`

Let `z` be a length-`2m` path ending at height `-2`; equivalently, `z` is
an `(m-1)`-subset of `[2m]`.  If `p<q` are down-step positions of `z`, let
`y=z+\{p,q\}` denote the path obtained by flipping both steps up.

### Lemma 2.1 (exact `alpha` inverse)

The equality `alpha(y)=z` holds if and only if all four conditions below
hold:

\[
\begin{array}{ll}
\text{(a)}&H_z(p)\in\{0,1\},\\
\text{(b)}&H_z(q)\in\{-2,-1\},\\
\text{(c)}&\text{there is no up-step of `z` starting at height `-2` or
`-1` strictly between `p` and `q`},\\
\text{(d)}&D_1(z;[1,p))=D_{-2}(z;(q,2m]).
\end{array}
\tag{2.1}
\]

#### Proof

In `y`, the two flipped steps must be the consecutive up-steps touching
line `1` whose ranks are `U_1(y)` and `U_1(y)+1`.  The first starts at
height `0` or `1` in both `y` and `z`, proving (a).  Between the two
flips, `z` is two height units below `y`; hence the second starts at height
`-2` or `-1` in `z`, proving (b), and consecutiveness is exactly (c).

It remains to translate the ordinal condition.  Put

\[
 A_i=U_i(z;[1,p)),\qquad R_i=U_i(z;(q,2m]).
\]

The number of touching-line-`1` up-steps of `y` before `p` is `A_0+A_1`.
The total number of up-steps of `y` starting at height `1` is

\[
 A_1+\mathbf1_{H_z(p)=1}
 +\mathbf1_{H_z(q)=-1}+R_{-3};
\]

condition (c) removes the possible middle contribution.  Thus `p` has
rank `U_1(y)` precisely when

\[
 A_0+1
 =\mathbf1_{H_z(p)=1}+\mathbf1_{H_z(q)=-1}+R_{-3}.
\tag{2.2}
\]

Crossing the horizontal line `1/2` in the prefix gives

\[
 A_0=D_1(z;[1,p))+\mathbf1_{H_z(p)=1}.
\tag{2.3}
\]

Crossing the line `-5/2` in the suffix gives

\[
 R_{-3}=D_{-2}(z;(q,2m])+\mathbf1_{H_z(q)=-2}.
\tag{2.4}
\]

Substitution into (2.2), followed by
`1_{H_z(q)=-1}+1_{H_z(q)=-2}=1`, gives exactly (d).  Every step above is
reversible, so (a)--(d) are also sufficient.  \(\square\)

Let `a(z)=|alpha^{-1}(z)|` and put

\[
 L_\alpha(z)=D_0(z)+D_1(z).
\]

### Corollary 2.2 (pointwise local-time bound)

\[
 \boxed{a(z)\le2L_\alpha(z).}
\tag{2.5}
\]

#### Proof

Fix the first position `p`.  Condition (d) fixes the number `k` of
down-steps starting at `-2` strictly after `q`.  If `q` itself starts at
`-2`, it is therefore the `(k+1)`-st such step from the right and is
unique.  There is also at most one possible `q` starting at `-1`: two such
choices `q<q'` would force an up-step from `-2` to `-1` between them, in
contradiction with condition (c) for `q'`.  There are `L_alpha(z)` possible
first positions by (a), proving (2.5).  \(\square\)

## 3. Exact inverse criterion for `Gamma`

Let `T` be a length-`2m` path ending at height `4`; equivalently, `T` is
an `(m+2)`-subset of `[2m]`.  For up-step positions `p<q`, let
`x=T-\{p,q\}` be obtained by flipping both down.

### Lemma 3.1 (exact `Gamma` inverse)

The equality `Gamma(x)=T` holds, with `x` in an internal flaw class, if
and only if

\[
\begin{array}{ll}
\text{(a)}&H_T(p)\in\{0,1\},\\
\text{(b)}&H_T(q)\in\{2,3\},\\
\text{(c)}&\text{there is no down-step of `T` starting at height `2` or
`3` strictly between `p` and `q`},\\
\text{(d)}&U_0(T;[1,p))=U_3(T;(q,2m]).
\end{array}
\tag{3.1}
\]

#### Proof

In `x`, positions `p,q` must be the consecutive down-steps touching line
`0` whose ranks are `D_0(x)` and `D_0(x)+1`.  Before `p`, `T=x`; between
the two positions, `T` is two units above `x`.  This proves (a)--(c).

Let `L_i=D_i(T;[1,p))` and `R_i=D_i(T;(q,2m])`.  Equating the number
`L_0+L_1` of touching-line-`0` down-steps before `p` with `D_0(x)-1`
gives

\[
 L_1+1
 =\mathbf1_{H_T(p)=0}+\mathbf1_{H_T(q)=2}+R_4.
\tag{3.2}
\]

Prefix crossings of the line `1/2` and suffix crossings of the line
`7/2` give respectively

\[
 L_1=U_0(T;[1,p))-\mathbf1_{H_T(p)=1},
\tag{3.3}
\]

\[
 R_4=U_3(T;(q,2m])-\mathbf1_{H_T(q)=2}.
\tag{3.4}
\]

Substitution into (3.2), using
`1_{H_T(p)=0}+1_{H_T(p)=1}=1`, yields (d).  Again the derivation is
reversible.  Conditions (a) and (d) also ensure that both touching-step
ranks exist; excluding the two endpoint flaw classes is exactly the stated
internal-domain requirement.  \(\square\)

Writing `c(T)=|Gamma^{-1}(T)|` and

\[
 L_\Gamma(T)=U_0(T)+U_1(T),
\]

the same uniqueness argument gives

\[
 \boxed{c(T)\le2L_\Gamma(T).}
\tag{3.5}
\]

Indeed, after fixing `p`, a possible `q` starting at height `3` is fixed
by the number of later `U_3` steps in (3.1d).  There is at most one `q`
starting at height `2`, since returning to height `2` after an earlier
such up-step requires a forbidden down-step starting at height `3`.

## 4. `Gamma` has unbounded fibres

For `k>=1`, put `m=2k` and define the endpoint-four path

\[
 T_k=(10)^{k-1}\,111\,(10)^{k-1}\,1.
\tag{4.1}
\]

It has length `4k=2m`, with `m+2` up-steps.  Its `k` up-steps from height
`0` to height `1` are indexed from the left by `j=0,...,k-1`.  Its `k`
up-steps from height `3` to height `4` are indexed from the right by the
same values.  Call these positions `p_j` and `q_j`.

For every `j`, one has `p_j<q_j`, there is no down-step starting at height
`2` or `3` between them, and

\[
 U_0(T_k;[1,p_j))=j=U_3(T_k;(q_j,4k]).
\]

Lemma 3.1 therefore gives `k` distinct preimages, so

\[
 \boxed{|\Gamma^{-1}(T_k)|\ge k=m/2.}
\tag{4.2}
\]

Thus the general matching cap of order `m` is sharp in order even for the
canonical intrinsic map.  A proof of linear aggregate collision energy
must use the rarity of large fibres, not a pointwise constant.

## 5. A bridge-local-time summation lemma

### Lemma 5.1

Fix integers `a,b`.  Among all length-`2m` up/down paths from height `0`
to height `b`, the total number of visits to height `a` (and hence the
total number of up-steps or down-steps starting at `a`) is `O_{a,b}(4^m)`.

#### Proof

At time `t`, the number of such pointed paths is

\[
 \binom{t}{(t+a)/2}
 \binom{2m-t}{(2m-t+b-a)/2},
\tag{5.1}
\]

with the expression interpreted as zero when parity or range fails.  The
standard central-binomial bound gives

\[
 \binom rj\le {C2^r\over\sqrt{r+1}}
\]

uniformly when `j-r/2` is bounded.  Hence (5.1) is at most

\[
 {C_{a,b}4^m\over
   \sqrt{t+1}\sqrt{2m-t+1}}.
\]

The sum of the reciprocal square-root factor over `0<=t<=2m` is bounded
by an absolute constant (compare with the beta integral).  Summing (5.1)
proves the lemma.  \(\square\)

## 6. The intrinsic `O(W sqrt(m))` pair bound

Let `Y_m` be all length-`2m` paths ending at height `2`.  For one
occurrence `y in Y_m`, put `z=alpha(y)` and let `p<q` be its two selected
positions.  Apart from these two positions, a down-step of `z` starting at
height `0` or `1` corresponds to a down-step of `y` starting

* at height `0` or `1` before `p`;
* at height `2` or `3` between `p` and `q`;
* at height `4` or `5` after `q`.

Consequently

\[
 L_\alpha(z)
 \le2+\sum_{h=0}^{5}D_h(y).
\tag{6.1}
\]

Using (2.5), counting ordered colliding partners from each occurrence,
and then applying Lemma 5.1 gives

\[
\begin{aligned}
 2P_\alpha
 &=\sum_z a(z)(a(z)-1)\\
 &=\sum_{y\in Y_m}(a(\alpha(y))-1)\\
 &\le 2\sum_{y\in Y_m}L_\alpha(\alpha(y))
 =O(4^m).
\end{aligned}
\tag{6.2}
\]

For `Gamma`, sum over the internal balanced paths `x`.  If
`T=Gamma(x)` and `p<q` are selected, then, apart from the selected
positions, an up-step of `T` starting at height `0` or `1` corresponds to
an up-step of `x` starting in

\[
 \{0,1\},\quad\{-2,-1\},\quad\{-4,-3\}
\]

in the three successive regions.  Hence

\[
 L_\Gamma(T)
 \le2+\sum_{h=-4}^{1}U_h(x),
\tag{6.3}
\]

and (3.5) plus Lemma 5.1 gives

\[
                         P_\Gamma=O(4^m).
\tag{6.4}
\]

Finally,

\[
 4^m=O\!\left(\sqrt m\binom{2m+1}{m}\right)
       =O(W\sqrt m),
\tag{6.5}
\]

so

\[
 \boxed{P_\alpha+P_\Gamma=O(W\sqrt m).}
\tag{6.6}
\]

## 7. Endpoint colours and the full first shadow

Let `e(S)` be the number of the `2B` endpoint occurrences equal to the
no-infinity target `S`, and retain `a(S)=|alpha^{-1}(S)|`.  The endpoint
and cross-endpoint contribution is exactly

\[
 P_{\rm end}
 =\sum_S\left(a(S)e(S)+\binom{e(S)}2\right).
\tag{7.1}
\]

For every first-shadow target, the occurrences form a matching on its
`m+2` middle supersets.  Thus its full load is at most

\[
 M_m=\left\lfloor{m+2\over2}\right\rfloor.
\]

Since `a(S)+e(S)<=M_m` and `sum_S e(S)=2B`,

\[
 P_{\rm end}
 \le {2M_m-1\over2}\sum_Se(S)
 =(2M_m-1)B=O(W).
\tag{7.2}
\]

Combining (6.6) and (7.2) gives the coarse full bound
`P_1=O(W sqrt(m))`.  The next sections use the clean-corridor conditions
to remove the square-root loss.

## 8. Catalan renewal kernels

Put

\[
 \mathcal C(u)=\sum_{r\ge0}\operatorname{Cat}_r u^r
 ={1-\sqrt{1-4u}\over2u},
 \qquad
 \mathcal B(u)=\sum_{r\ge0}\binom{2r}r u^r
 ={1\over\sqrt{1-4u}}.
\tag{8.1}
\]

A primitive positive or negative excursion, including its first and last
steps, has generating function

\[
 K(u):=u\mathcal C(u)={1-\sqrt{1-4u}\over2}.
\tag{8.2}
\]

Two independently chosen primitive excursions have generating function
`K(u)^2`.  A nonempty sequence of paired excursions has generating function

\[
 \Phi(u):={K(u)^2\over1-K(u)^2}.
\tag{8.3}
\]

We shall also use

\[
 J(u):={u^2\over(1-u)^2},
 \qquad
 \Psi(u):={J(u)\over1-J(u)}.
\tag{8.4}
\]

### Lemma 8.1 (critical convolution)

Suppose `A(u)=sum a_r u^r` has nonnegative coefficients and

\[
                         a_r\le\binom{2r}r.
\tag{8.5}
\]

Then

\[
 [u^m]A(u)\Phi(u)=O\!\left(\binom{2m}m\right),
 \qquad
 [u^m]A(u)\Psi(u)=O\!\left(\binom{2m}m\right).
\tag{8.6}
\]

#### Proof

Coefficientwise, `A<=mathcal B`, so it is enough to use `mathcal B`.
Write `s=sqrt(1-4u)`.  By (8.2), `K=(1-s)/2`; in particular
`K(1/4)=1/2`.  The denominator in (8.3) is nonzero at `u=1/4`, and

\[
 \Phi(u)=\phi_0+\phi_1s+O(s^2).
\]

Consequently

\[
 \mathcal B(u)\Phi(u)
 ={\phi_0\over\sqrt{1-4u}}+O(1)+O(\sqrt{1-4u}).
\tag{8.7}
\]

Its coefficients are `O(4^m/sqrt(m))`, equivalently
`O(binomial(2m,m))`.  Here is an elementary coefficient audit of the last
step.  The algebraic function `Phi` is analytic in a standard slit
Delta-domain at `1/4`, and its displayed expansion (or the binomial series
for `sqrt(1-4u)`) gives

\[
 [u^r]\Phi(u)=O\!\left({4^r\over(r+1)^{3/2}}\right).
\tag{8.8a}
\]

Using `binomial(2s,s)=O(4^s/sqrt(s+1))`, the convolution is at most

\[
 C4^m\sum_{r=0}^m
 {1\over\sqrt{m-r+1}(r+1)^{3/2}}.
\tag{8.8b}
\]

For `r<=m/2`, take out `O(m^{-1/2})` and sum `(r+1)^{-3/2}`.  For
`r>m/2`, take out `O(m^{-3/2})` and sum
`(m-r+1)^{-1/2}=O(sqrt(m))`.  Thus (8.8b) is
`O(4^m/sqrt(m))`, with no hidden polynomial loss.

For the second kernel, `J(1/4)=1/9`, and `Psi` is analytic in a disk of
radius strictly larger than `1/4` (the first positive solution of `J=1`
is `u=1/2`).  Thus `mathcal B Psi` has only the square-root pole of
`mathcal B`.  Equivalently, the coefficients of `Psi` are `O(c^r)` for
some `c<4`, and the same split convolution proves the estimate.  \(\square\)

The number of all `alpha` occurrences in semilength `r` and the number of
all `Gamma` occurrences are respectively

\[
 \binom{2r}{r+1}\le\binom{2r}r,
 \qquad
 (r-1)\operatorname{Cat}_r
 ={r-1\over r+1}\binom{2r}r\le\binom{2r}r.
\tag{8.8}
\]

Thus the generating series of every typed subfamily of base occurrences
satisfies Lemma 8.1.

## 9. Linear pair count for `Gamma`

For a `Gamma` occurrence `(T;p,q)`, define its type and crossing index by

\[
 (H_T(p),H_T(q))\in
 \{(0,2),(0,3),(1,2),(1,3)\},
 \qquad
 k=U_0(T;[1,p))=U_3(T;(q,2m]).
\tag{9.1}
\]

### Lemma 9.1 (the two singleton types)

For every `T`, each of the types `(0,2)` and `(1,3)` occurs at most once.

#### Proof

For type `(0,2)`, the index `k` makes `p` the `(k+1)`-st up-step starting
at height `0`.  For fixed `p`, there is at most one possible `q` starting
at height `2`: after one such step reaches height `3`, returning to height
`2` before a second choice requires a down-step starting at height `3`,
forbidden by Lemma 3.1(c).

If two occurrences had indices `k<l`, then `p_k<p_l`, while the suffix
count forces `q_l<q_k`.  They would be nested.  Returning from height `3`
after `q_l` to height `2` at `q_k` again forces a forbidden `D_3`.

For type `(1,3)`, `q` is uniquely determined by `k`: it is the
`(k+1)`-st `U_3`, counted from the right.  Two choices of `p` for that
`q`, or nested choices with different indices, would have to return from
height `2` after the earlier `p` to height `1` at the later one.  This
requires a forbidden `D_2`.  \(\square\)

### Lemma 9.2 (nested `(0,3)` renewal)

The total number of unordered pairs of type-`(0,3)` occurrences in
semilength `m` is `O(binomial(2m,m))`.

#### Proof

For a fixed `k`, both positions are unique: `p_k` is the `(k+1)`-st
`U_0` from the left and `q_k` the `(k+1)`-st `U_3` from the right.  If
`k<l` are both valid, then

\[
                         p_k<p_l<q_l<q_k.
\tag{9.2}
\]

The outer corridor contains no `D_2` or `D_3`.  Between successive
selected `U_0` steps, it therefore has a unique block

\[
                         D_1\,A\,U_0,
\tag{9.3}
\]

where `A` is a path from height `0` to itself staying at or below `0`.
This is a primitive negative excursion based at height `1`, counted by
`K(u)`.  From an inner selected `U_3` towards the next outer selected
`U_3`, the corresponding block is

\[
                         U_3\,B\,D_4,
\tag{9.4}
\]

where `B` stays at or above height `4`; it is counted by the same `K(u)`.

More explicitly, for each successive low index `i`, the left block begins
immediately after `p_i` and ends with `p_(i+1)`.  For each successive high
index, the right block begins with the inner `q_i` and ends immediately
before the next outer `q_(i-1)`.  Delete these `l-k` left blocks (9.3) and
`l-k` right blocks (9.4).  They are disjoint by (9.2).  The result is a
shorter endpoint-four path with the marked occurrence `(p_k,q_k)`.
Conversely, this base occurrence, the positive integer `l-k`, and the two
ordered excursion lists reconstruct the original path and both marked
occurrences uniquely.  Each inserted left block contains exactly one new
`U_0`, and each right block exactly one new `U_3`, so the indices cannot
shift ambiguously.

The collision generating function is therefore coefficientwise bounded by
`A_03(u)Phi(u)`, where `A_03` counts base occurrences.  Apply (8.8) and
Lemma 8.1.  \(\square\)

### Lemma 9.3 (adjacent `(1,2)` renewal)

The total number of unordered pairs of type-`(1,2)` occurrences in
semilength `m` is `O(binomial(2m,m))`.

#### Proof

After `p` goes from height `1` to `2`, the next step cannot be `D_2`, so
`q` is the immediately following `U_2`.  Every occurrence is an adjacent
`11` passage from height `1` to height `3`.

For two occurrences in chronological order, the prefix `U_0` count is
nondecreasing and the suffix `U_3` count nonincreasing.  Equality in (9.1)
forces a common index.  Hence there is no `U_0` or `U_3` strictly between
consecutive occurrences, and the intervening path stays in `[1,3]`.

Starting just after one occurrence and ending just after the next, its
unique word is

\[
 D_3(U_2D_3)^aD_2(U_1D_2)^bU_1U_2,
 \qquad a,b\ge0.
\tag{9.5}
\]

Indeed, at height `3` the absence of `U_3` forces `D_3`; at height `2`
there are only the loops `U_2D_3` before the descent `D_2`; and at height
`1` every `U_1` not followed by `D_2` would begin an intervening
occurrence.  The block generating function is exactly
`J(u)=u^2/(1-u)^2`.

Deleting a nonempty sequence of consecutive blocks leaves one marked base
occurrence, and insertion is unique.  The pair generating function is
bounded by `A_12(u)Psi(u)`.  Use (8.8) and Lemma 8.1.  \(\square\)

### Theorem 9.4

\[
 \boxed{P_\Gamma=O\!\left(\binom{2m}m\right)=O(W).}
\tag{9.6}
\]

#### Proof

Let `c_tau(T)` be the multiplicity of type `tau`.  Lemmas 9.1--9.3 and
(8.8) give

\[
 \sum_Tc_\tau(T)^2
 =\sum_Tc_\tau(T)+2\sum_T\binom{c_\tau(T)}2
 =O\!\left(\binom{2m}m\right)
\tag{9.7}
\]

for every type.  Since `(sum_tau c_tau)^2<=4sum_tau c_tau^2`, summing over
`T` proves the theorem, including collisions between different types.
\(\square\)

## 10. Linear pair count for `alpha`

For an `alpha` occurrence `(z;p,q)`, define its type and crossing index by

\[
 (H_z(p),H_z(q))\in
 \{(0,-2),(0,-1),(1,-2),(1,-1)\},
 \qquad
 k=D_1(z;[1,p))=D_{-2}(z;(q,2m]).
\tag{10.1}
\]

We audit the four types directly.

### Lemma 10.1 (the two singleton types)

For every `z`, each of the types `(1,-1)` and `(0,-2)` occurs at most
once.

#### Proof

For type `(1,-1)`, `p` is the `(k+1)`-st `D_1` and is fixed by `k`.
For fixed `p`, two possible `q` steps from height `-1` would require a
forbidden `U_{-2}` between them.  If two indices satisfied `k<l`, then
`p_k<p_l` and the suffix count would give `q_l<q_k`; returning from height
`-2` after `q_l` to height `-1` at `q_k` gives the same contradiction.

For type `(0,-2)`, `q` is the `(k+1)`-st `D_{-2}` from the right.  Two
choices of `p`, at equal or different indices, would require a return from
height `-1` after the earlier `p` to height `0` at the later one, using a
forbidden `U_{-1}`.  \(\square\)

### Lemma 10.2 (nested `(1,-2)` renewal)

The total number of unordered pairs of type-`(1,-2)` occurrences in
semilength `m` is `O(binomial(2m,m))`.

#### Proof

Both endpoints are fixed by the index.  If `k<l` are valid, then

\[
                         p_k<p_l<q_l<q_k.
\tag{10.2}
\]

Between successive selected `D_1` steps, the outer clean corridor forces
a primitive positive excursion

\[
                         U_0\,A\,D_1,
\tag{10.3}
\]

where `A` stays at or above height `1`.  From an inner selected `D_{-2}`
towards the next outer one, it forces a primitive negative excursion

\[
                         D_{-2}\,B\,U_{-3},
\tag{10.4}
\]

where `B` stays at or below height `-3`.  Both are counted by `K(u)`.

For each successive left index, delete the block beginning immediately
after the outer `p_i` and ending with `p_(i+1)`.  On the right, delete the
block beginning with the inner `q_i` and ending immediately before the
next outer `q_(i-1)`.  Thus deleting the `l-k` paired excursions leaves
one shorter marked type-`(1,-2)` occurrence.  The blocks are disjoint by
(10.2), the two ordered excursion lists reverse the deletion uniquely, and
the pair generating function is bounded by
`A_(1,-2)(u)Phi(u)`.  Apply (8.8) and Lemma 8.1.  \(\square\)

### Lemma 10.3 (adjacent `(0,-1)` renewal)

The total number of unordered pairs of type-`(0,-1)` occurrences in
semilength `m` is `O(binomial(2m,m))`.

#### Proof

After `p` descends from height `0` to `-1`, Lemma 2.1(c) forbids an
up-step from `-1`; hence `q` is the immediately following `D_{-1}`.
Every occurrence is an adjacent `00` passage from height `0` to `-2`.

For chronologically ordered occurrences, the prefix `D_1` count is
nondecreasing and the suffix `D_{-2}` count nonincreasing.  Equation
(10.1) forces a common index.  There is no `D_1` or `D_{-2}` between
consecutive occurrences, so the intervening path stays in `[-2,0]`.

Starting just after one occurrence and ending just after the next, its
unique word is

\[
 U_{-2}(D_{-1}U_{-2})^a
 U_{-1}(D_0U_{-1})^bD_0D_{-1},
 \qquad a,b\ge0.
\tag{10.5}
\]

It has generating function `J(u)`.  Deleting a nonempty sequence of these
blocks leaves one base occurrence, so the pair series is bounded by
`A_(0,-1)(u)Psi(u)`.  Use (8.8) and Lemma 8.1.  \(\square\)

### Theorem 10.4

\[
 \boxed{P_\alpha=O\!\left(\binom{2m}m\right)=O(W).}
\tag{10.6}
\]

#### Proof

Apply the typed square-sum argument (9.7) to Lemmas 10.1--10.3, using the
mass bound (8.8).  This also counts every cross-type pair.  \(\square\)

## 11. Full pair count and sharp order

Theorems 9.4 and 10.4, together with the exact endpoint estimate (7.2),
give

\[
 \boxed{P_1=P_\alpha+P_\Gamma+P_{\rm end}=O(W).}
\tag{11.1}
\]

For the reverse inequality, the symbolic `1100/1010` marked-gap family
gives `(2m-3)Cat_(m-2)` pairs of distinct pointed first-shadow occurrences,
with no pointed slot reused.  Hence

\[
 P_1\ge(2m-3)\operatorname{Cat}_{m-2}
 ={m(m+1)\over4(2m-1)(2m+1)}W
 =\left({1\over16}+O(m^{-1})\right)W.
\tag{11.2}
\]

This proves (0.1)--(0.2).  Large fibres such as (4.2) are compatible with
the linear aggregate because each added nested layer has critical paired
weight `K(1/4)^2=1/4`.

## 12. Euclidean energy and prime smoothing

The exact energy identity is

\[
 \|\mu_1-\lambda_1\mathbf1\|_2^2
 =2P_1-(\lambda_1-1)W,
 \qquad \lambda_1={m+2\over m}.
\tag{12.1}
\]

Equation (11.1) proves (0.3).  The coarse local-time proof lost
`sqrt(m)` because it counted visits to the relevant height bands
separately; the renewal proof pairs the forced left and right excursions.

If `n=2m+1` is prime and `sigma` is a uniform coordinate `n`-cycle, the
exact class average for the centered load `f_1` gives

\[
 \mathbb E_\sigma\|\Pi_\sigma f_1\|_2^2
 ={1\over n}\|f_1\|_2^2=O(W/m).
\tag{12.2}
\]

The orbit-floor Cauchy bound is therefore `O(W/sqrt(m))`; in particular,
some prime cycle has first-shadow orbit-mass floor `o(W)` for the canonical
MSW factor.

## 13. Exact all-depth sector formulas and the depth-two gate

The proof above is special to depth one, but its first structural reduction
extends exactly.  For one root write

\[
 A=(a_0,\ldots,a_{m-1}),\qquad
 B=(b_0,\ldots,b_{m-1}).
\]

For `0<=q<m`, all depth-`q` lower colours split into the following three
families:

\[
 \alpha_q(w,i)
 =\{a_0,\ldots,a_{i-1}\}
  \cup\{b_{i+q},\ldots,b_{m-1}\},
 \quad 0\le i\le m-q,
\tag{13.1}
\]

the `2q` endpoint colours

\[
 \{b_r,\ldots,b_{r+m-q-1}\}quad(0\le r<q),
\qquad
 \{a_r,\ldots,a_{r+m-q-1}\}quad(1\le r\le q),
\tag{13.2}
\]

and the `m-q` colours containing `infinity`, whose upper cores are

\[
 \Gamma_q(w,i)
 =\{a_0,\ldots,a_i\}
  \cup\{b_{i-q},\ldots,b_{m-1}\},
 \quad q\le i<m.
\tag{13.3}
\]

The lower colour corresponding to (13.3) is

\[
 \{\infty\}\cup([2m]\setminus\Gamma_q(w,i)).
\tag{13.4}
\]

### Lemma 13.1 (sector decomposition)

Equations (13.1)--(13.4) list every one of the `2m+1` depth-`q` slots of
the row, without repetition as pointed slots.

#### Proof

After cutting the step-two omitted-label order immediately after
`infinity`, the remaining linear order is

\[
                         b_0,b_1,\ldots,b_{m-1},
                         a_0,a_1,\ldots,a_{m-1}.
\tag{13.5}
\]

The colours avoiding `infinity` are precisely its intervals of length
`m-q`.  Starts `q,...,m` give (13.1); the `q` starts before that range and
the `q` starts after it give (13.2).  A colour containing `infinity` is the
complement, apart from `infinity`, of an interval of (13.5) of length
`m+q+1`.  Its `m-q` possible starts give (13.3)--(13.4).  The counts are

\[
                         (m-q+1)+2q+(m-q)=2m+1.
\]

\(\square\)

The intrinsic sectors themselves are exact ladders of depth-one pivots.
For (13.1), put `z=alpha_q(w,i)` and, for `0<=t<=q`, set

\[
 X_t=z\cup A_{[i,i+t)}\cup B_{[i+t,i+q)}.
\tag{13.6}
\]

Then `X_t=x_(i+t)`, so `X_(t+1)=f(X_t)`, and

\[
 X_t\cap X_{t+1}
 =z\cup A_{[i,i+t)}\cup B_{[i+t+1,i+q)}.
\tag{13.7}
\]

Thus an `alpha_q` occurrence is precisely a composable `q`-edge MSW
ladder whose common core is `z`.  Dually, if

\[
 Y_j=A_{[0,j]}\cup B_{[j,m)},
\]

then, after writing `j=i+q` in (13.3),

\[
 \Gamma_q(w,i+q)=\bigcup_{t=0}^{q}Y_{i+t}.
\tag{13.8}
\]

These identities are the exact general-`q` starting point: they retain
the order and composability data which would be lost by treating the
`2q` or `2q+2` flipped coordinates as an unordered marked set.

There is also an all-depth conjugacy between the two intrinsic sectors.
For a length-`2m` path `Y` ending at height `2`, put

\[
                         \mathcal P(Y)=1\,\overline Y\,1.       \tag{13.8a}
\]

This is a balanced path of semilength `m+1`.

### Lemma 13.1A (all-depth padding conjugacy)

For every `1<=q<m`, padding and complementation map every intrinsic
`Gamma_q` occurrence at semilength `m` to an intrinsic `alpha_q`
occurrence at semilength `m+1`.  If the upper target is `T`, the lower
target is

\[
                         \boxed{z=1\,\overline T\,1.}           \tag{13.8b}
\]

The map is a bijection onto the padded subfamily and preserves pointed
collision pairs.  Consequently

\[
 \boxed{
 \sum_T\binom{\mu_{\Gamma,q}^{(m)}(T)}2
 \le
 \sum_z\binom{\mu_{\alpha,q}^{(m+1)}(z)}2.}                   \tag{13.8c}
\]

#### Proof

Use the endpoint-`2` paths in (13.8).  An upper occurrence is the union
of the composable chain

\[
                         Y_i,Y_{i+1},\ldots,Y_{i+q}.
\]

At depth one, the inverse criteria of Lemmas 2.1 and 3.1 are conjugate
under `mathcal P`: for an old position `p`,

\[
 U_h(Y)\longmapsto D_{1-h}(\mathcal P(Y)),
 \qquad
 D_h(Y)\longmapsto U_{1-h}(\mathcal P(Y)).                    \tag{13.8d}
\]

The height bands, clean-corridor exclusions, and ordinal equality are
therefore carried exactly from one upper pivot edge to one lower pivot
edge, with orientation reversed.  Apply this independently to the `q`
adjacent edges and reverse their order.  The resulting balanced paths

\[
 \mathcal P(Y_{i+q}),\mathcal P(Y_{i+q-1}),\ldots,
 \mathcal P(Y_i)
\]

form one composable `q`-edge lower MSW ladder.  Its common intersection
is

\[
 \bigcap_{t=0}^{q}\mathcal P(Y_{i+t})
 =1\,\overline{\bigcup_{t=0}^{q}Y_{i+t}}\,1
 =1\,\overline T\,1.
\]

Unpadding, complementing, and reversing gives the inverse on this
subfamily.  Hence pointed occurrences and collision pairs are preserved,
which proves (13.8c). \(\square\)

Thus every all-depth intrinsic energy estimate only has to be proved for
`alpha_q`; the `Gamma_q` estimate follows at the adjacent semilength.

There is already a useful all-depth consequence.  In the ladder (13.6),
write its `t`-th deleted/inserted pivot pair as `(b_t,a_t)`, so
`b_t<a_t`, and let

\[
 k_t=D_1(C_t;[1,b_t))=D_{-2}(C_t;(a_t,2m]),
 \qquad C_t=X_t\cap X_{t+1}.
\tag{13.9}
\]

### Lemma 13.2 (the pivot counters form a Motzkin walk)

For every intrinsic depth-`q` occurrence,

\[
                         k_{t+1}-k_t\in\{-1,0,1\}
 \qquad(0\le t<q-1).
\tag{13.10}
\]

More precisely, the only possible relative orders of two consecutive
pivot intervals are

\[
\begin{array}{c|c}
\text{relative order}&k_{t+1}-k_t\\ \hline
b_t<a_t<b_{t+1}<a_{t+1}&0\\
b_t<b_{t+1}<a_{t+1}<a_t&+1\\
b_{t+1}<b_t<a_t<a_{t+1}&-1\\
b_{t+1}<b_t<a_{t+1}<a_t&0.
\end{array}
\tag{13.11}
\]

The opposite crossing
`b_t<b_(t+1)<a_t<a_(t+1)` and the reverse-disjoint order
`b_(t+1)<a_(t+1)<b_t<a_t` are impossible.

#### Proof

Restrict the ladder to `X_t,X_(t+1),X_(t+2)` and remove their common
rank-`(m-2)` core.  With

\[
 (c,s,r,d)=(b_t,a_t,b_{t+1},a_{t+1}),
\]

this is exactly the centered depth-two configuration of Lemma 13.4 below.
Its order table and Corollary 13.5 give (13.10)--(13.11).  \(\square\)

Thus the `q` apparently separate ordinal constraints collapse to one
nonnegative nearest-neighbour counter path.  Any uniform all-`q` renewal
must sum this Motzkin/noncrossing state exactly (for example by a
determinantal corridor encoding); treating the `q` edges as independent
renewal channels discards the decisive synchronization.

### Conditional shell-transfer criterion

The exact numerical target for such an encoding is already favorable.
Suppose a pair of equal depth-`q` ladders admits a unique iterative shell
deletion with the following properties:

1. deleting a nesting shell changes the counter state by `+1` or `-1`,
   with coefficient generating function bounded by `K(u)^2` for each
   sign;
2. deleting a flat shell has one of the two zero-step types in (13.11),
   with generating function bounded by `J(u)` for each type;
3. deletion stops at one pointed base occurrence, and insertion of the
   typed shell list reconstructs the original collision pair uniquely.

Then the total shell series is coefficientwise bounded by

\[
 {R(u)\over1-R(u)},
 \qquad R(u)=2K(u)^2+2J(u).
\]

At the Catalan singularity,

\[
 R(1/4)=2\left({1\over2}\right)^2
       +2\left({1\over9}\right)
       ={13\over18}<1.
\tag{13.11a}
\]

Consequently the critical-convolution proof of Lemma 8.1 would give
`O(binomial(2m,m))`, with an absolute constant independent of `q`: the
base-occurrence coefficient is at most `(m-q+1)Cat_m<=binomial(2m,m)`,
and `R/(1-R)` has only a square-root singularity at `1/4`.

This conclusion concerns the intrinsic ladder-collision series encoded by
the assumed deletion.  For the full depth-`q` load one must center first:

\[
 E_q=\|\mu_q-\lambda_q\mathbf1\|_2^2
 =2P_q-(\lambda_q-1)W,
 \qquad
 P_q^{\rm bal}:=P_q-{\lambda_q-1\over2}W={E_q\over2}.
\tag{13.11b}
\]

Raw `P_q=O(W)` cannot hold uniformly once `lambda_q` grows.  In the
central window `q<=A sqrt(m)`, where `lambda_q=O_A(1)`, an `O_A(W)` raw
pair estimate is equivalent in strength to `E_q=O_A(W)`; beyond that
window the shell transfer has to count the balanced excess in (13.11b).

This is a conditional criterion, not a proved shell bijection.  The
weights `K^2` and `J` in Sections 9--10 count separation between repeated
occurrences, whereas (13.11) classifies adjacent pivots inside one
occurrence.  Identifying those two structures requires a pair-of-ladders
deletion/insertion proof; the Motzkin table alone does not justify it.

The exact depth-two audit below shows that the numerical value `13/18`
cannot be used as a model for the true all-depth transfer.  The three
genuinely iterated depth-two kernels have critical weights

\[
 {1\over4},\qquad {3\over8},\qquad {3\over8},                  \tag{13.11c}
\]

for the crossing-flat, `+1`, and `-1` counter types.  Their scalar sum is
exactly one.  The other flat type splits into a chronological insertion
of weight `1/12` and one-off overlap loops; it is not another freely
iterable scalar shell.  Thus a row-sum proof of strict subcriticality is
not available.  Any all-`q` proof must use the direction/state structure
of the counter walk.

Strict subcriticality is fortunately stronger than the final application
needs.  In view of Theorem 4.2A of the prime-cycle smoothing note, it is
enough to prove a **sublinear critical Green bound**: if the genuine
pair-of-ladders deletion has shell Green kernel `mathcal G_q(u)` and

\[
 \boxed{
 [u^m]\,\mathcal B(u)\mathcal G_q(u)
 \le C_A(q+1)^\beta\binom{2m}{m}
 \quad(q\le A\sqrt m)                                         \tag{13.11d}
 }
\]

for some fixed `beta<1`, then the canonical factor has
`E_q=O_A(W(q+1)^beta)` and prime-cycle smoothing gives aggregate defect
`o(W)`.  A one-dimensional critical Motzkin Green function naturally has
square-root, rather than linear, growth.  Consequently a bound of order
`sqrt(q)` in (13.11d) would already finish the energy part of the
constant-one argument.  The remaining task is to construct the genuine
stateful deletion kernel and prove this polynomial Green estimate; the
false scalar `13/18` shortcut is no longer used.

The analytic estimate suggested by the three critical weights is already
elementary.  Let `T` be the substochastic kernel on the nonnegative
integers defined by

\[
 T(k,k)={1\over4},\qquad T(k,k+1)={3\over8},\qquad
 T(k,k-1)={3\over8}\quad(k\ge1),                               \tag{13.11e}
\]

and at `k=0` omit the transition to `-1` (it is killing mass).

### Lemma 13.2A (critical half-line Green bound)

For every `t,q>=0`,

\[
 \boxed{
 \sum_{j\ge0}T^t(0,j)\le {C\over\sqrt{t+1}},\qquad
 \sum_{t=0}^{q}\sum_{j\ge0}T^t(0,j)\le C\sqrt{q+1}.}           \tag{13.11f}
\]

The same `O(sqrt(q+1))` bound holds for
`sum_(t<=q)T^t(0,0)`.

#### Proof

Realize `T` as the walk with increments `-1,0,+1` of probabilities
`3/8,1/4,3/8`, killed on its first visit to `-1`.  Let `J` be the number
of nonzero increments in the first `t` steps.  Conditional on `J=j`, the
nonzero skeleton is an ordinary simple symmetric walk of length `j`.
The reflection principle (or the ballot identity) gives

\[
 \Pr(\min_{s\le j}S_s\ge0)\le {C\over\sqrt{j+1}}.
\]

Now `J` has law `Bin(t,3/4)`.  Splitting at `J=t/2` and using a Chernoff
bound below that point gives

\[
 \mathbb E(J+1)^{-1/2}\le C(t+1)^{-1/2}.
\]

This is the first assertion.  Summing it through `q` proves the second.
The return mass is bounded by the survival mass. \(\square\)

Thus, if the genuine shell deletion starts its directional state at the
killing boundary and is dominated by `T`, the required `O(sqrt q)` Green
amplification follows automatically.  The unresolved mathematics is the
combinatorial domination and reconstruction, not the random-walk
estimate.

### Lemma 13.2B (exact depth-three directional audit)

For one intrinsic depth-three ladder, let `delta_0,delta_1` be the two
successive counter increments.  After separating the forward-disjoint
zero type as a distinct symbol `F`, the critical alphabet is exactly
`{-,C,+}`.  Assign the three letters their depth-two critical values
`3/8,1/4,3/8`.  The nine two-letter words then have the formal product
weights

\[
\begin{array}{c|ccc}
 &-&C&+\\ \hline
-&9/64&3/32&9/64\\
C&3/32&1/16&3/32\\
+&9/64&3/32&9/64
\end{array}                                                    \tag{13.11g}
\]

and the entries sum to one.  If `r=min(k_0,k_1,k_2)` and `t_*` is the
first location of that minimum, then `h_t=k_t-r` starts at `0` at `t_*`;
read away from `t_*` in either direction, it is a killed half-line
Motzkin path.  Thus the killing-boundary state is exact for one ladder.

For two ladders, however, the raw gap is not a three-step state:

\[
 (k'_{t+1}-k_{t+1})-(k'_t-k_t)
 =\delta'_t-\delta_t\in\{-2,-1,0,1,2\}.                      \tag{13.11h}
\]

The extreme moves are locally genuine.  The `+` witness
`X=101001`, with `(c,r,d,s)=(2,3,4,6)`, and the `-` witness
`X=100101`, with `(r,c,s,d)=(1,3,4,5)`, realize increments `+1` and `-1`
symbolically.  Pairing their signatures changes the formal gap by two.
Moreover, the extreme move occurs in a genuine common-target collision.
At semilength `10`, put

\[
 S=0^6\,1^6\,00000100.
\]

One depth-three occurrence over `S` has

\[
 (b_0,b_1,b_2)=(2,3,1),\qquad (a_0,a_1,a_2)=(6,4,5),
 \qquad (k_0,k_1,k_2)=(0,1,0),                            \tag{13.11i}
\]

and a second has

\[
 (b'_0,b'_1,b'_2)=(15,13,19),\qquad
 (a'_0,a'_1,a'_2)=(16,17,20),
 \qquad (k'_0,k'_1,k'_2)=(1,0,0).                         \tag{13.11j}
\]

Thus their signed gap is `(1,-1,0)`, and its first step is genuinely
`-2`.  In this example the extreme step crosses from gap `1` to gap `-1`:
it is a boundary/orientation transition, not a translation-invariant bulk
step.  The audit does not assert that every genuine extreme step must have
this form.

#### Proof

Apply Lemma 13.2 to the windows `(X_0,X_1,X_2)` and
`(X_1,X_2,X_3)`.  This gives the four-symbol alphabet; multiplying the
assigned one-cell values gives (13.11g).  Subtracting the first global minimum proves the killed
boundary assertion.  Subtraction of the two counter recurrences gives
(13.11h), and the two hand witnesses are those in (13.19a).

For completeness, the first occurrence in (13.11i), restricted to its
first six positions, has the four states

\[
 111000,\quad101001,\quad100101,\quad000111
\]

over the zero core.  Its three edge cores have counters `(0,1,0)`.
The remaining suffix `1^6 00000100` begins at height `-2`, rises to `4`,
and returns to `-2` without a `D_{-2}`, so all three ordinal equalities
remain unchanged.  For (13.11j), restrict to the final block `00000100`.
Before shifting by `12`, its pivot data are

\[
 (b_0,b_1,b_2)=(3,1,7),\qquad(a_0,a_1,a_2)=(4,5,8),
\]

and its edge cores have up-step sets
`{1,6,7}`, `{4,6,7}`, `{4,5,6}`, with counters `(1,0,0)`.
The prefix `0^6 1^6` returns to height zero and has no `D_1`, so shifting
the block preserves all three ordinal equalities.  The corridor conditions
in both constructions lie entirely inside the displayed six- or
eight-step block.  Finally the four depth-two parent targets are

\[
 S+\{1\},\quad S+\{6\},\quad S+\{19\},\quad S+\{16\},
\]

and hence are distinct, as required for a genuine bowtie. \(\square\)

There is a second, independent obstruction to iterating the depth-two
proof.  If a depth-three occurrence has common core `S` and pivot pairs
`(b_t,a_t)`, the common targets of its first and second depth-two
subladders are

\[
                         S+\{b_2\},\qquad S+\{a_0\}.          \tag{13.11k}
\]

For a genuine depth-three bowtie, the corresponding four depth-two parent
targets of the two occurrences are distinct.  Hence neither pair of
subladders is a depth-two collision, and Lemmas 13.7--13.9 cannot simply be
multiplied along (13.11g).  A successful all-depth proof may keep the
`+/-2` moves in a larger finite Markov-additive shell state; it still must
prove translation invariance away from the boundary (the exhibited
extreme move is only a sign-changing boundary move), zero drift,
non-coboundary variance, and regenerative or strip control of `F`.  What
is invalid is projecting the pair gap directly to the three-state kernel
without that coherence theorem.

At depth two, (13.1) also has a useful exact composition description.  An
oriented depth-one `alpha` occurrence with output `S` and selected positions
`p<q` is the directed MSW edge

\[
                         S\cup\{p\}\longrightarrow S\cup\{q\}.
\tag{13.12}
\]

### Lemma 13.3 (depth-two `alpha` composition)

A rank-`(m-2)` path `z` is an `alpha_2` output precisely when there are
four distinct positions `d_0,s,r,a_1` such that the two valid oriented
depth-one occurrences

\[
 z\cup\{r,d_0\}\longrightarrow z\cup\{r,s\},
 \qquad
 z\cup\{r,s\}\longrightarrow z\cup\{s,a_1\}
\tag{13.13}
\]

have respective colours \(z\cup\{r\}\) and \(z\cup\{s\}\).  Equivalently,
the selected pairs in Lemma 2.1 are `(d_0,s)` for \(z\cup\{r\}\) and
`(r,a_1)` for \(z\cup\{s\}\).

#### Proof

For three consecutive column states, write the two deleted coordinates as
`b_i,b_(i+1)` and the two inserted coordinates as `a_i,a_(i+1)`.  Their
common intersection is `z`, and the states are

\[
 z+\{b_i,b_{i+1}\},\quad
 z+\{b_{i+1},a_i\},\quad
 z+\{a_i,a_{i+1}\}.
\]

Set `(d_0,r,s,a_1)=(b_i,b_(i+1),a_i,a_(i+1))` to obtain (13.13).
Conversely, determinism of `f` makes two composable oriented occurrences
in (13.13) one genuine two-step column segment.  \(\square\)

The same statement becomes considerably cleaner when recentered at its
middle balanced path.

### Lemma 13.4 (centered depth-two inverse criterion)

Let `X` be a balanced path in an internal flaw class, let `r,s` be
distinct up-step positions of `X`, and put `z=X-{r,s}`.  There is a
depth-two segment

\[
 z\cup\{c,r\}\longrightarrow X
 \longrightarrow z\cup\{s,d\}
\tag{13.14}
\]

with common core `z` if and only if `c,d` are distinct down-step positions
of `X`, distinct from `r,s`, and

\[
 c<s,\qquad r<d,
\tag{13.15a}
\]

\[
 H_X(c),H_X(r),H_X(d)\in\{0,1\},
 \qquad H_X(s)\in\{-2,-1\},
\tag{13.15b}
\]

\[
 \begin{array}{l}
 \text{there is no `X`-up-step starting at `-2` or `-1` in `(c,s)`,}\\
 \text{there is no `X`-up-step starting at `0` or `1` in `(r,d)`,}
 \end{array}
\tag{13.15c}
\]

and

\[
 \boxed{
 D_1(X;[1,c))=D_0(X;(s,2m]),\qquad
 D_1(X;[1,r))=D_0(X;(d,2m]).}
\tag{13.15d}
\]

#### Proof

The first edge of (13.14) has depth-one core `X-{s}=z+{r}` and selected
pair `(c,s)`.  Before `s` this core has the same heights as `X`, while
strictly after `s` it is two units below `X`.  Lemma 2.1 therefore turns
its height, corridor, and ordinal conditions into the first condition in
each line of (13.15b)--(13.15d).  The second edge has core
`X-{r}=z+{s}` and selected pair `(r,d)`.  Before `r` it agrees with `X`
and after `r` it is two units below `X`, giving the second condition in
each line.  The inequalities (13.15a) are the orientations of the two
depth-one edges.  All translations are reversible, and Lemma 13.3 then
composes the two edges.  \(\square\)

Put

\[
 k_0=D_1(X;[1,c))=D_0(X;(s,2m]),\qquad
 k_1=D_1(X;[1,r))=D_0(X;(d,2m]).
\tag{13.16}
\]

There are only six physical order types.  Monotonicity of the prefix
`D_1` count and of the suffix `D_0` count gives the following exact table.

\[
\begin{array}{c|c|c}
\text{order}&\text{counter relation}&\text{forced empty counts}\\ \hline
c<s<r<d&k_0=k_1&D_1([c,r))=D_0((s,d])=0\\
c<r<s<d&k_0=k_1&D_1([c,r))=D_0((s,d])=0\\
c<r<d<s&k_1-k_0=D_1([c,r))=D_0((d,s])\\
r<c<s<d&k_0-k_1=D_1([r,c))=D_0((s,d])\\
r<c<d<s&k_0=k_1&D_1([r,c))=D_0((d,s])=0\\
r<d<c<s&k_0=k_1&D_1([r,c))=D_0((d,s])=0
\end{array}
\tag{13.17}
\]

Here all unlabelled counts are taken in `X`.  This table is the finite
two-corridor state space for a depth-two bowtie.  In particular, four of
the six order types already have one synchronized renewal index; only the
third and fourth types carry a nonzero counter gap.

### Corollary 13.5 (one master index)

The second and sixth order types in (13.17), `c<r<s<d` and
`r<d<c<s`, are empty.  In the third type

\[
                         k_1-k_0=1,
\tag{13.18}
\]

and in the fourth type

\[
                         k_0-k_1=1.
\tag{13.19}
\]

Thus exactly four physical order types are feasible.  Every centered
depth-two occurrence has one renewal index and an order-determined offset
in `{-1,0,1}`; there are not two freely varying corridor indices.

#### Proof

In the second type, equality of the counters forces
`D_1(X;[c,r))=0`.  Hence the down-step `c` must start at height `0` and
ends at `-1`.  Reaching the up-step `r`, which starts at height `0` or
`1`, before `s` would require an up-step from `-1`; this is forbidden on
`(c,s)` by (13.15c).  The type is therefore impossible.

In the third type, reaching the high up-step `r` before `s` forces `c` to
be a `D_1`, so the common difference in the third row of (13.17) is at
least one.  After `d`, the low-corridor prohibition says that once the
path uses a `D_0` it cannot return to height `0` before `s`.  Hence there
is at most one `D_0` in `(d,s]`; equality in (13.17) proves (13.18).

In the fourth type, two `D_1` steps in `[r,c)` would require an intervening
`U_0`, forbidden by the high-corridor condition on `(r,d)`.  The common
difference in the fourth row of (13.17) is therefore at most one.  After
the up-step `s` the height is at most `0`; reaching the down-step `d`
without a forbidden `U_0` forces `d` to start at height `0`.  Thus `d`
itself contributes a `D_0` to `(s,d]`, so the common difference is at
least one.  This proves (13.19).

Finally consider the sixth type.  Equality of the counters forces
`D_1(X;[r,c))=0`.  Immediately after the up-step `r` the path is at height
`1` or `2`.  Before the down-step `d`, which starts at height `0` or `1`,
the path must therefore use a `D_1`, either at `d` or earlier.  That step
lies in `[r,c)`, a contradiction.  \(\square\)

The four surviving cases are genuinely nonempty.  Direct symbolic
witnesses, with the marked positions read from left to right, are

\[
\begin{array}{c|c}
c<s<r<d&X=0110,quad(c,s,r,d)=(1,2,3,4)\\
c<r<d<s&X=101001,quad(c,r,d,s)=(2,3,4,6)\\
r<c<s<d&X=100101,quad(r,c,s,d)=(1,3,4,5)\\
r<c<d<s&X=1001,quad(r,c,d,s)=(1,2,3,4).
\end{array}
\tag{13.19a}
\]

Substitution in (13.15)--(13.16) verifies each row without enumeration.

### Corollary 13.6 (a common-target outer index)

Every feasible occurrence in Lemma 13.4 canonically determines two marked
down-steps `P<Q` of the common endpoint-`-4` path `z` and an index `k` as
follows:

\[
\begin{array}{c|c|c}
\text{order type}&(P,Q)&k\\ \hline
c<s<r<d&(c,d)&k_0=k_1\\
c<r<d<s&(c,s)&k_0=k_1-1\\
r<c<s<d&(r,d)&k_1\\
r<c<d<s&(r,s)&k_0=k_1
\end{array}
\tag{13.20}
\]

They satisfy the single common-path relation

\[
 H_z(P)\in\{0,1\},\qquad H_z(Q)\in\{-4,-3\},
 \qquad
 \boxed{D_1(z;[1,P))=D_{-4}(z;(Q,2m])=k.}
\tag{13.21}
\]

#### Proof

Before the first of `r,s`, the paths `X` and `z` agree.  Between them
`X` is two units above `z`, and after both it is four units above `z`.
Substitute these shifts into (13.16), using the equalities and unit offsets
from Corollary 13.5.  In the four feasible orders this gives exactly the
four rows of (13.20) and (13.21).  The height assertions follow from
(13.15b), and every one of `c,d,r,s` is a down-step in `z`.  \(\square\)

Thus two depth-two occurrences over the same `z` do not carry two
independent unbounded counters.  Their possible long-range separation is
organized by the same left `D_1`/right `D_{-4}` index.  In particular, for
outer endpoint type `(1,-4)`, indices `k<l` force nested outer pairs.
To recover the familiar `K(u)^2` renewal one must still prove, using the
two clean-corridor conditions rather than (13.21) alone, that the two
separation pieces reduce to primitive excursions and that the internal
marks form a uniquely reconstructible finite-strip decoration.  This is
the remaining bowtie lemma.  Four distinct depth-one parents do not supply
four independent renewal indices, so a `K(u)^4` kernel cannot be assumed
without an additional reconstruction argument.

### Lemma 13.7 (the crossing-flat order has linear square energy)

Let `a_x(z)` count centered depth-two occurrences of order

\[
                         r<c<d<s.
\]

Then

\[
 \sum_z\binom{a_x(z)}2=O\!\left(\binom{2m}m\right).
\tag{13.22}
\]

#### Proof

For this order, the fifth row of (13.17) and the two clean corridors force

\[
                         H_X(c)=1,\qquad H_X(d)=0.
\]

Indeed, after the up-step `r`, reaching `c` without a `D_1` in `[r,c)`
forces `c` to start at height `1`; after `c`, reaching `d` without a
forbidden `U_0` forces `d` to start at height `0`.  Pass to the common
endpoint-`-4` path `z=X-{r,s}`.  Then `c` is a `D_{-1}`, `d` is a
`D_{-2}`, and the interval from `r` through `s` has the exact normal form

\[
 \begin{cases}
 D_0,&H_z(r)=0,\\
 D_1\,E_+\,D_0,&H_z(r)=1,
 \end{cases}
 \quad D_{-1}D_{-2}\quad
 \begin{cases}
 D_{-3},&H_z(s)=-3,\\
 D_{-3}\,E_-\,D_{-4},&H_z(s)=-4,
 \end{cases}
\tag{13.23}
\]

where `E_+` is an arbitrary excursion from `0` to `0` staying at or above
`0`, and `E_-` is an arbitrary excursion from `-4` to `-4` staying at or
below `-4`.  To verify (13.23), note that on `(r,d)` the common path has
no up-step from `-2` or `-1`, on `(c,s)` it has no up-step from `-4` or
`-3`, on `[r,c)` it has no `D_{-1}`, and on `(d,s]` it has no `D_{-2}`.
Consequently the first departure below `0`, the two middle down-steps, and
the last arrival at `-4` are forced; only the two displayed excursions can
vary.  Conversely, (13.23) together with the outer equality (13.21)
implies the corresponding conditions of Lemma 13.4 by direct substitution.

Split by the endpoint pair
`(H_z(r),H_z(s))`.  In subtype `(1,-4)`, the outer relation (13.21) makes
`r` the `(k+1)`-st `D_1` from the left and `s` the `(k+1)`-st `D_{-4}`
from the right.  If `k<l` both occur, their normal forms are nested and
share the rigid central descent `D_0D_{-1}D_{-2}D_{-3}`.  Between
successive selected `D_1` steps lies one primitive positive excursion;
between the corresponding selected `D_{-4}` steps lies one primitive
negative excursion.  Deleting the synchronized pairs is reversible, so
the collision series is bounded by a base-occurrence series times
`Phi(u)`, and Lemma 8.1 applies.

The mixed subtypes `(1,-3)` and `(0,-4)` occur at most once for a fixed
`z`.  In the first case the index fixes `r`, after which the first permanent
departure below `0` in (13.23) fixes the central descent and `s`; the
second case is the reversed argument starting from the index-fixed `s`.
The same nesting argument excludes two different indices.

Finally, subtype `(0,-3)` is precisely a marked consecutive passage

\[
                         D_0D_{-1}D_{-2}D_{-3}
\]

from height `0` to `-4`.  Two chronologically ordered passages have a
nondecreasing prefix `D_1` count and a nonincreasing suffix `D_{-4}`
count; (13.21) forces the common index.  The intervening path therefore
has no `D_1` and no `D_{-4}` and stays in the fixed strip `[-4,0]`.
Walks in this strip, even with two marked passages, have exponential
growth strictly below `2` per step (the path-graph spectral radius is
`2 cos(pi/6)<2`).  Their semilength generating function is consequently
analytic in a disk of radius larger than `1/4`.  Convolution with the
base-occurrence series is again `O(binomial(2m,m))`.  Summing the four
subtypes proves (13.22).  \(\square\)

### Lemma 13.8 (the two offset orders have linear square energy)

Let `a_+(z)` count centered depth-two occurrences of order

\[
                         c<r<d<s.
\]

Then

\[
 \sum_z\binom{a_+(z)}2=O\!\left(\binom{2m}m\right).
\tag{13.24}
\]

The same estimate holds for the reversed order `r<c<s<d`.

#### Proof

In the first order, (13.18) and the two clean corridors force `c` and `d`
to be respectively `D_1` and `D_1` in `X`.  In the common endpoint-`-4`
path `z`, they are therefore `D_1` and `D_(-1)`.  Starting at `c`, the
segment through `s` has the exact normal form

\[
 D_1
 \begin{cases}
   D_0D_{-1},&H_z(r)=0,\\
   U_0E_1^+D_1\,E_0^+D_0D_{-1},&H_z(r)=1,
 \end{cases}
 E_{-2}^+D_{-2}
 \begin{cases}
   D_{-3},&H_z(s)=-3,\\
   D_{-3}E_{-4}^-D_{-4},&H_z(s)=-4.
 \end{cases}
\tag{13.25}
\]

Here `E_h^+` and `E_h^-` are arbitrary excursions based at `h`, staying
respectively at or above and at or below `h`; the displayed `D_0` or
`D_1` in the first brace is `r`, the displayed `D_(-1)` is `d`, and the
last displayed step is `s`.  Indeed, there is no `D_1` in `(c,r)`.  If
`r=D_0`, it and `d` must consequently be consecutive.  If `r=D_1`, the
part from just after `c` through `r` is a primitive positive excursion,
and the first subsequent permanent descent below `0` is `D_0D_(-1)`.
After `d`, (13.18) says that there is exactly one `D_(-2)` before `s`;
the low clean corridor then gives the last brace.  The same first-return
argument proves the converse, so (13.25) is an exact, unambiguous form.

The subtype `H_z(s)=-3` occurs at most once for a fixed `z`.  For a fixed
index, `c` is fixed and (13.25) fixes all later marks.  If indices `k<l`
both occurred, then `c_k<c_l` while the suffix counts force
`s_l<s_k`.  Moreover `r_k<=c_l`: either `r_k` is the next `D_1` after
`c_k`, or it occurs before that step.  After `s_l=D_(-3)`, returning to
height `-3` at `s_k` requires a `U_(-4)`, forbidden in the clean corridor
from `r_k` to `s_k`.

It remains to treat `H_z(s)=-4`.  For two occurrences with indices
`k<l`, their outer marks are nested.  Between consecutive selected `D_1`
steps there is no `D_1`, and the outer clean corridor prevents the path
from going below `-2` and returning.  The intervening block is therefore

* an arbitrary excursion from `0` to `0` confined to `[-2,0]`, followed
  by
* a primitive positive excursion ending with the next selected `D_1`.

The first factor has generating function

\[
 L_2(u)={1-u\over1-2u},
\tag{13.26}
\]

the bounded-height Catalan fraction of height two, and the second has
generating function `K(u)`.  On the right, consecutive selected `D_(-4)`
steps enclose one primitive negative excursion, again counted by `K(u)`.
Thus one synchronized shell has series

\[
 H_+(u)=L_2(u)K(u)^2,
 \qquad H_+(1/4)={3\over8}<1.
\tag{13.27}
\]

Deleting the top blocks from just after the outer `c` through the inner
`c`, and the paired bottom blocks from the inner `s` back to the outer
`s`, leaves a shorter occurrence.  The remaining internal marks are the
inner ones; after reinsertion the outer marks are recovered by the
first-return rules in (13.25).  Hence deletion and insertion are mutually
inverse.  The pair series is bounded by a base-occurrence series times
`H_+/(1-H_+)`.  The latter has a finite square-root expansion at `1/4`,
so the coefficient argument of Lemma 8.1 proves (13.24).

For the other offset order use word reversal.  If `X^R` is `X` read from
right to left and `p^*=2m+1-p`, then

\[
 D_h\longmapsto D_{1-h},\qquad
 U_h\longmapsto U_{-1-h}.
\]

The relabelling

\[
 (c',r',d',s')=(d^*,s^*,c^*,r^*)
\]

takes `c<r<d<s` bijectively to `r'<c'<s'<d'`.  It interchanges the two
clean corridors and the two counter equalities in (13.15), with
`k'_0=k_1` and `k'_1=k_0`.  It also takes the common target `z` to its
reversal.  Thus it is a bijection on collision pairs, proving the second
assertion.  \(\square\)

### Lemma 13.9 (the disjoint-forward order has linear square energy)

Let `a_f(z)` count centered depth-two occurrences of order

\[
                         c<s<r<d.
\]

Then

\[
 \sum_z\binom{a_f(z)}2=O\!\left(\binom{2m}m\right).
\tag{13.28}
\]

#### Proof

The zero counter gap in the first row of (13.17) forces `c=D_0` and
`d=D_1` in `X`.  Hence they are `D_0` and `D_(-3)` in `z`.  Write
`E_h^+` and `E_h^-` as in Lemma 13.8.  Splitting by the heights of `s`
and `r` in `z`, the segment from `c` through `d` is exactly one of

\[
\begin{array}{c|l}
(H_z(s),H_z(r))&\text{marked normal form}\\ \hline
(-1,-2)&D_0D_{-1}D_{-2}D_{-3},\\
(-1,-1)&D_0D_{-1}\,U_{-2}E_{-1}^+D_{-1}\,
                    E_{-2}^+D_{-2}D_{-3},\\
(-2,-2)&D_0D_{-1}E_{-2}^-D_{-2}\,
                    E_{-3}^-U_{-3}D_{-2}D_{-3},\\
(-2,-1)&D_0D_{-1}E_{-2}^-D_{-2}\,
                    E_{-3}^-U_{-3}U_{-2}E_{-1}^+D_{-1}\,
                    E_{-2}^+D_{-2}D_{-3}.
\end{array}
\tag{13.29}
\]

In each row the first of the two height-labelled down-steps is `s`, the
second is `r`, and the first and last steps are `c` and `d`.

To derive (13.29), note first that `D_1(X;[c,r))=0`: after `c=D_0`,
the low clean corridor either makes `s=D_(-1)` the next step, or gives
`D_(-1)E_{-2}^-s` with `s=D_(-2)`.  On `(s,r)` there is neither a
`D_(-1)` nor a `D_(-2)`.  Thus a step `s=D_(-1)` is followed either by
`r=D_(-2)`, or by `U_(-2)E_{-1}^+r` with `r=D_(-1)`.  A step
`s=D_(-2)` is followed by `E_{-3}^-U_(-3)` and the same two alternatives.
Finally, `D_0(X;(s,d])=0` and the high clean corridor make
`r=D_(-2)` immediately followed by `d=D_(-3)`, whereas
`r=D_(-1)` is followed by `E_{-2}^+D_(-2)d`.  These implications are
reversible.

The parsing is unambiguous once the outer pair `(c,d)` is specified.
This follows from the first-return convention in the second row, the
last-return convention in the third row, and both conventions in the
fourth row.  Equivalently, the selected negative excursion is the last
one before the permanent rise through `U_(-3)`, and the selected positive
excursion ends at the first subsequent return through `D_(-1)`.

Now take two occurrences and order them so that `c_1<=c_2`.  If the
`c` marks are equal, outer-pair uniqueness orders the distinct `d` marks.
If `c_1<c_2`, inspection of (13.29) shows that every `D_0` strictly
between `c_1` and `d_1` lies in one of the displayed positive excursions.
If `c_2>=d_1`, then `d_2>c_2` makes the desired order immediate.  If
`c_2<d_1`, the path after `c_2` stays at or above `-2` until `d_1`, so no
`D_(-3)` can occur before `d_1`.  In either case,

\[
                         c_1<c_2\quad\Longrightarrow\quad d_1\le d_2.
\tag{13.30}
\]

Monotonicity in the outer equality (13.21) now forces the two occurrences
to have the same index.  Consequently there is no `D_1` in
`[c_1,c_2)` and no `D_(-4)` in `(d_1,d_2]`.

There are two strict geometric cases.  If `d_1<c_2`, the bridge from just
after `d_1` at height `-4` to `c_2` at height `0` stays in `[-4,0]`.
Indeed, crossing either boundary and returning would use one of the two
just-excluded steps.  Its semilength series is the endpoint entry of the
five-state path resolvent,

\[
 B_4(u)={u^2\over(1-u)(1-3u)},
 \qquad B_4(1/4)={1\over3}.
\tag{13.31}
\]

The continuant identity
`det(I-sqrt(u) A_(P_5))=1-4u+3u^2` proves (13.31).  The four complete
passages in (13.29) have total series

\[
 A_f(u)=u^2+2u^3\mathcal C(u)^2+u^4\mathcal C(u)^4
       =u^2\mathcal C(u)^2,
 \qquad A_f(1/4)={1\over4}.
\tag{13.32}
\]

Thus the path from after `d_1` through the second occurrence and after
`d_2` is a balanced insertion with series coefficientwise bounded by
`B_4A_f`; its critical value is `1/12`.  Deleting it leaves the first
marked occurrence, and the typed bridge and passage reconstruct the pair.

If instead `c_2<d_1`, superimposing the two normal forms makes the overlap
rigid:

\[
             c_2D_0\;D_{-1}\;D_{-2}\;d_1D_{-3}.
\tag{13.33}
\]

For completeness, occurrence 1 puts the path at or above `-2` from just
after `c_2` until `d_1`.  The reason is that the two rows of (13.29) with
`H_z(r_1)=-2` have no internal `D_0` at all.  Hence `c_2` lies in one of
the positive excursions of a row with `H_z(r_1)=-1`, after all its
negative excursions, and the rest of occurrence 1 is bounded below by
`-2`.  Dually, since `d_1<d_2`, an internal `D_(-3)` in occurrence 2 is
possible only in a row with `H_z(s_2)=-2`; it lies in that occurrence's
negative part, before the permanent rise, where the path is bounded above
by `-2`.  After the compulsory `D_(-1)` following `c_2`, their
intersection is the single level `-2`; hence no intervening step is
possible, and the terminal `D_(-2)D_(-3)` of occurrence 1 gives (13.33).

Delete the loop from `c_1` up to but not including `c_2`, and the loop
from just after `d_1` through `d_2`.  The first is a nonempty excursion
at or below `0`, and the second a nonempty excursion at or above `-4`.
Each has series

\[
                         \mathcal C(u)-1={K(u)\over1-K(u)}.
\tag{13.34}
\]

The deletions leave the rigid marked occurrence (13.33), preserve its
outer index, and are uniquely reversed.  If only one outer endpoint is
shared, exactly one of the two loops is deleted; equality of both outer
endpoints would give the same occurrence by the unambiguous parsing.

Every kernel in (13.31)--(13.34) is finite at `u=1/4` and has a finite
square-root expansion there.  The number of centered depth-two base
occurrences in semilength `r` is `(r-1)Cat_r<=binom(2r,r)`.  The coefficient
split in Lemma 8.1 therefore applies to the disjoint, overlapping, and
shared-endpoint cases and proves (13.28).  \(\square\)

### Theorem 13.10 (linear energy for the intrinsic lower depth-two sector)

If `mu_(alpha,2)(z)` counts the intrinsic occurrences (13.1) at `q=2`,
then

\[
 \sum_z\binom{\mu_{\alpha,2}(z)}2
 =O\!\left(\binom{2m}m\right)=O(W),
 \qquad
 \sum_z\mu_{\alpha,2}(z)^2=O(W).
\tag{13.35}
\]

#### Proof

Corollary 13.5 partitions the occurrences into exactly four order types.
Their within-type pair energies are bounded by Lemmas 13.7--13.9.  Their
total first moment is `(m-1)Cat_m<=binom(2m,m)`.  Apply
`(x_1+...+x_4)^2<=4 sum_i x_i^2` target by target.  \(\square\)

For the upper core one has the exact recursive pivot formula

\[
 \Gamma_2(x)
 =x\cup\{\operatorname{pos}(g,x),
          \operatorname{pos}(g',x),
          \operatorname{pos}(g',f^{-1}x)\},
\tag{13.36}
\]

valid on flaw classes `2,...,m-1`.  Formula (13.36) follows immediately
from (13.3): the three added positions are `a_i,b_(i-1),b_(i-2)`.

### Lemma 13.11 (exact `Gamma_2`--`alpha_2` padding conjugacy)

Let `Y` be a length-`2m` path ending at height `2`.  A centered upper-core
occurrence has four distinct positions, with `r,s` down-steps and `c,d`
up-steps of `Y`, and consists of the two depth-one targets

\[
                         Y+\{r\},\qquad Y+\{s\}
\]

with selected pairs `(r,c)` and `(d,s)`.  Equivalently,

\[
 r<c,\qquad d<s,
\tag{13.37a}
\]

\[
 H_Y(r),H_Y(c),H_Y(d)\in\{0,1\},
 \qquad H_Y(s)\in\{2,3\},
\tag{13.37b}
\]

there is no `Y`-down-step from `0` or `1` in `(r,c)`, no `Y`-down-step
from `2` or `3` in `(d,s)`, and

\[
 \boxed{
 U_0(Y;[1,r))=U_1(Y;(c,2m]),\qquad
 U_0(Y;[1,d))=U_1(Y;(s,2m]).}
\tag{13.37c}
\]

Put a leading and trailing up-step around the bitwise complement of `Y`,

\[
                         X=1\,\overline Y\,1.
\tag{13.38}
\]

After shifting every old position by one, relabel

\[
 (c_\alpha,r_\alpha,d_\alpha,s_\alpha)=(d,r,c,s).
\tag{13.39}
\]

Then (13.37) is exactly the centered lower criterion (13.15) for `X`.
In particular, if the common upper target is `T=Y+\{r,s\}`, the common
lower target is

\[
                         z=1\,\overline T\,1.
\tag{13.40}
\]

The path `X` starts with an up-step, so it is not in the all-negative flaw
class; it ends with an up-step and is balanced, so it visits height `-1`
immediately before its last step and is not Dyck.  Thus it lies in an
internal flaw class.  The construction is a bijection from upper-core
occurrences to the padded subfamily of lower occurrences, and it preserves
collision pairs.  Hence

\[
 \sum_T\binom{\mu_{\Gamma,2}(T)}2
 =O\!\left(\binom{2m+2}{m+1}\right)=O(W).
\tag{13.41}
\]

#### Proof

Apply Lemma 3.1 to `Y+\{r\}` with selected pair `(r,c)`, and to
`Y+\{s\}` with selected pair `(d,s)`.  Before and after the flipped
position the height changes by two, giving (13.37) directly.

For an old position `p`, complementation plus the leading up-step sends

\[
 U_h(Y)\longmapsto D_{1-h}(X),
 \qquad D_h(Y)\longmapsto U_{1-h}(X).
\tag{13.42}
\]

Thus the height bands in (13.37b) become those in (13.15b), the two
down-step exclusions become the two up-step exclusions in (13.15c), and
`U_0,U_1` become `D_1,D_0` in (13.15d).  The two inequalities become
`c_alpha<s_alpha` and `r_alpha<d_alpha`.  This proves the exact
conjugacy; (13.40) follows by complementing the two flipped positions.
Theorem 13.10 at semilength `m+1` now gives (13.41), and
`binom(2m+2,m+1)=2binom(2m+1,m)=2W`.  \(\square\)

### Lemma 13.12 (the four seam sectors have linear square mass)

Let `e_2(S)` be the number of the four endpoint occurrences in (13.2),
at `q=2`, having no-infinity target `S`.  Then

\[
 \max_S e_2(S)\le m+2,
 \qquad
 \sum_S e_2(S)^2=O(W).
\tag{13.43}
\]

#### Proof

Fix `S`.  A pointed depth-two occurrence has three middle supersets.  If
the two coordinates immediately before `S` in its cyclic interval are
`p_1,p_2` and the two immediately after it are `s_1,s_2`, those supersets
are

\[
 S+\{p_1,p_2\},\qquad S+\{p_1,s_1\},\qquad S+\{s_1,s_2\}.
\tag{13.44}
\]

Across all pointed occurrences of the fixed target, the three two-sets in
(13.44) never repeat.  Otherwise the same middle set `S+Q` would occur in
two rows of the exact middle factor.  This is the fan-simplicity argument.

Every one of the four seam intervals abuts the cut at `infinity`, so at
least one of its three fan edges has the form `{infinity,x}`.  Select one
such edge by a fixed side convention.  The selected edges for distinct
seam occurrences over `S` are distinct by fan simplicity.  Since `S`
does not contain `infinity`, there are only `m+2` possible choices of
`x` outside `S`.  This proves the pointwise bound.  Finally,

\[
 \sum_Se_2(S)=4\operatorname{Cat}_m,
 \qquad
 \sum_Se_2(S)^2
 \le(m+2)4\operatorname{Cat}_m=O(W).
\tag{13.45}
\]

\(\square\)

### Theorem 13.13 (linear full depth-two collision energy)

For the canonical exact MSW wreath factor,

\[
 \boxed{
 P_2=\sum_{|S|=m-2}\binom{\mu_2(S)}2=O(W),
 \qquad
 E_2=\|\mu_2-\lambda_2\mathbf1\|_2^2=O(W),}
\tag{13.46}
\]

where

\[
                         \lambda_2={(m+2)(m+3)\over m(m-1)}.
\tag{13.47}
\]

#### Proof

For a no-infinity target write its load as
`mu_(alpha,2)(S)+e_2(S)`.  Theorem 13.10 and Lemma 13.12 give both square
sums as `O(W)`, so Cauchy gives

\[
 \sum_S\mu_{\alpha,2}(S)e_2(S)=O(W).
\tag{13.48}
\]

Thus all intrinsic--intrinsic, seam--seam, and intrinsic--seam pairs with
no-infinity target have total `O(W)`.  Targets containing `infinity` are
in bijection, by complementation off `infinity`, with the upper cores in
Lemma 13.11, so their pair count is also `O(W)`.  These sectors exhaust
(13.1)--(13.4), proving `P_2=O(W)`.

There are `W` pointed depth-two slots in total and
`binom(2m+1,m-2)` targets.  Their ratio is (13.47), and the exact identity

\[
                         E_2=2P_2-(\lambda_2-1)W
\tag{13.49}
\]

proves the centered assertion.  \(\square\)

### Corollary 13.14 (simultaneous prime smoothing through depth two)

If `n=2m+1` is prime, one coordinate `n`-cycle `sigma` satisfies

\[
 \boxed{
 \mathfrak D_{\sigma,1}+\mathfrak D_{\sigma,2}
 =O(W/\sqrt m)=o(W).}                                         \tag{13.50}
\]

#### Proof

Theorems 11.1 and 13.13 give `E_1+E_2=O(W)`.  The exact prime-cycle
projection average is

\[
 \mathbb E_\sigma\|\Pi_\sigma f_q\|_2^2={E_q\over n},
 \qquad q=1,2.
\]

For either depth, the orbit-floor Cauchy bound is

\[
 \mathfrak D_{\sigma,q}
 \le\sqrt{N_q}\,\|\Pi_\sigma f_q\|_2.
\]

Average the sum, use Jensen, and note `N_q=Theta(W)` and `n=Theta(m)`.
Some common cycle has the asserted bound. \(\square\)

## 14. Parent-edge reduction at every depth

There is a factor-independent reduction which removes most of that next
gate.  Work in the cyclic step-two coordinate order of one wreath.  A
depth-`q` colour is an interval `I` of length `m-q`.  It has exactly two
depth-`(q-1)` parents,

\[
                         I^-:=I\cup\{\ell(I)\},
 \qquad                  I^+:=I\cup\{r(I)\},
\tag{14.1}
\]

obtained by adjoining the coordinate immediately before or immediately
after `I`.  Regard the pointed occurrence of `I` as the edge
`{I^-,I^+}`.  This construction includes the seam and infinity sectors;
no cut of the cyclic order is being made.

Let `G_q` be the resulting multigraph after all wreaths are superposed.
Its vertices are rank-`(m-q+1)` target sets and its edges are the pointed
depth-`q` occurrences.  If `d_q(T)` denotes the degree of `T` in this
multigraph, then

\[
                         \boxed{d_q(T)=2\mu_{q-1}(T).}
\tag{14.2}
\]

Indeed, every pointed occurrence of `T` has precisely its left and right
one-coordinate truncations as incident depth-`q` edges.

### Lemma 14.1 (sharp wedge/bowtie reduction)

Let `P_q=sum_S binom(mu_q(S),2)`.  The number of depth-`q` collision
pairs whose two parent edges share a depth-`(q-1)` target is at most

\[
                         \boxed{2P_{q-1}.}
\tag{14.3}
\]

Consequently, if `B_q` denotes the number of the remaining collision
pairs--those for which the two parent edges have four distinct
depth-`(q-1)` targets--then

\[
                         \boxed{P_q\le2P_{q-1}+B_q.}
\tag{14.4}
\]

#### Proof

Fix a target `T` and distinguish its `mu_(q-1)(T)` pointed occurrences.
Each such occurrence has two distinct depth-`q` children, obtained by
deleting its left or right endpoint.  Two colliding depth-`q` slots which
share the parent target `T` cannot use the same pointed occurrence of `T`:
its two children have different target sets.  For a fixed pair of distinct
pointed `T` occurrences, their two two-element child families intersect in
at most two targets.  Hence `T` supports at most
`2 binom(mu_(q-1)(T),2)` such collision pairs.  Summing over `T` proves
(14.3).  A pair sharing both parents may be charged twice, which is harmless.
Every uncharged pair has four distinct parents, proving (14.4).  \(\square\)

At depth two, Theorem 11.1 therefore gives

\[
 \#\{\hbox{depth-two collision pairs sharing a depth-one parent}\}
 \le2P_1=O(W).
\tag{14.5}
\]

The complementary depth-two species is a genuine bowtie: two edges over
the same rank-`(m-2)` core `S` whose four endpoints are

\[
                         S+a,\quad S+b,\quad S+c,\quad S+d
\tag{14.6}
\]

with `a,b,c,d` distinct.  Equivalently, its two middle owners are
`S+{a,b}` and `S+{c,d}`, and at each owner the two locally deleted
coordinates are exactly its displayed extra pair.  Lemmas 13.7--13.12
count these disjoint-extra bowties, including the seam and upper-core
sectors, while (14.5) independently pays for every wedge and parallel
parent pair.  Thus Theorem 13.13 closes both parts of the reduction.
