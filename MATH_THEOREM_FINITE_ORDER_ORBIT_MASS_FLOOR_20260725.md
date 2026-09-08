# Finite-order orbit-mass floor and the long-cycle countermodel

Date: 2026-07-25

Method: pure mathematics only.

## 0. Outcome

The involution orbit-mass floor extends verbatim to every finite-order
coordinate permutation.  If `sigma` acts on the depth-`q` targets and
`O` is one target orbit, then every diagonal row replacement preserves

\[
                         t_O=\sum_{S\in O}\mu_q(S).
\]

Consequently that orbit always retains at least

\[
                         (|O|-t_O)_+
\]

holes.  In the relaxation in which occurrence tokens may be moved
independently one step at a time, this lower bound is exact after repeated
steps: orbit totals are the only invariants.

When `n=2m+1` is prime and `sigma` is an `n`-cycle, every nontrivial-rank
target orbit has size `n`.  The exact aggregate floor is therefore

\[
 \mathfrak D_{\sigma,q}(\mu)
 =\sum_{O} (n-t_O)_+
 ={1\over2}\left(\sum_O|t_O-n|-(W-N_q)\right).
\]

Long-cycle class averaging and the exact depth-one point margins do not
force this quantity to be `o(W)`.  An explicit integral abstract load
vector below obeys the correct total mass, the exact point margins, and the
known wreath multiplicity cap, yet has

\[
             \mathfrak D_{\sigma,1}(\mu)
             \ge (1/90+o(1))W
\]

for **every** coordinate `n`-cycle `sigma`.  Thus any positive theorem must
use substantially more of the exact wreath geometry than class-average
Johnson spectrum, point margins, and the scalar cap.

## 1. Orbitwise conservation for an arbitrary permutation

Let `F` be an exact middle wreath factor, fix a depth `q`, and abbreviate

\[
                         \mu(S)=\mu_q^F(S).
\]

Let `sigma` be any coordinate permutation of finite order.  For a row set
`A subseteq F`, put

\[
 a_A(S)=\#\{C\in A:S\text{ is an }(m-q)\text{-interval of }C\}.
\tag{1.1}
\]

Under the diagonal replacement

\[
                         F_A=(F\setminus A)\sqcup\sigma A,
\]

an occurrence at `S` is removed when its row lies in `A`, and an occurrence
at `sigma^{-1}S` in a selected row is moved to `S`.  Hence

\[
 \boxed{
 \mu_A(S)=\mu(S)-a_A(S)+a_A(\sigma^{-1}S).}
\tag{1.2}
\]

Let `O` be an orbit of the induced action of `sigma` on the target rank.
Summing (1.2) around `O` telescopes:

\[
 \boxed{
 \sum_{S\in O}\mu_A(S)=\sum_{S\in O}\mu(S)=:t_O.}
\tag{1.3}
\]

This holds for orbits of every divisor of the order of `sigma`, including
fixed targets.

## 2. Exact finite-order orbit floor

Write `d_O=|O|`, and let `H(\nu)` denote the number of zero coordinates of
a nonnegative integer target-load vector `nu`.

### Theorem 2.1

Every diagonal replacement satisfies

\[
 \boxed{
 H(\mu_A)\ge
 \mathfrak D_\sigma(\mu)
 :=\sum_{O}(d_O-t_O)_+.}
\tag{2.1}
\]

Moreover, in the occurrence-level relaxation permitting arbitrary
individual occurrence tokens to move repeatedly from `S` to `sigma S`,
the reachable vectors are exactly the nonnegative integer vectors `nu`
satisfying

\[
                         \sum_{S\in O}\nu(S)=t_O
 \quad\text{for every orbit }O.
\tag{2.2}
\]

Consequently the minimum possible number of holes in that relaxation is
exactly `mathfrak D_sigma(mu)`.  It can be attained using at most
`d_O-1` synchronous one-step rounds on an orbit of size `d_O`.

#### Proof

On an orbit with `d` coordinates and total nonnegative integer mass `t`,
at most `t` coordinates can be positive.  It therefore has at least
`(d-t)_+` zero coordinates.  Equation (1.3) proves (2.1).

Necessity of (2.2) follows from the same conservation law.  Conversely,
label all occurrence tokens.  Given an initial vector and a desired vector
with the same orbit total, assign the tokens to the desired slots.  On the
directed cycle every token has a unique forward distance in
`{0,1,...,d-1}` to its assigned slot.  In round `j`, move exactly the tokens
whose remaining forward distance is positive.  After at most `d-1` rounds
all tokens reach their assigned slots.  This realizes every vector in
(2.2).

Choose a final vector with one token on each of `min(d,t)` slots and put
all remaining tokens anywhere.  It has exactly `(d-t)_+` holes, proving
attainability of the floor. \(\square\)

Thus the exact maximum occurrence-level improvement is

\[
 \boxed{H(\mu)-\mathfrak D_\sigma(\mu).}
\tag{2.3}
\]

The row-packet constraint can only reduce this improvement.

There is also a useful exact `L^1` form.  If the target rank has size `N`
and total load `W`, then

\[
 \boxed{
 \mathfrak D_\sigma(\mu)
 ={1\over2}\left(
   \sum_O|t_O-d_O|+N-W
  \right).}
\tag{2.4}
\]

Indeed, the sum of `d_O-t_O` over all orbits is `N-W`, and positive-part
summation gives (2.4).

## 3. Prime long cycles

Assume now that `n=2m+1` is prime, take a target rank

\[
                         1\le r=m-q\le n-1,
\]

and let `sigma` be a coordinate `n`-cycle.  If a nonempty proper target
`S` were fixed by `sigma^j` for some `0<j<n`, then `sigma^j` would itself
be an `n`-cycle and transitivity would force `S` to be empty or all of
`[n]`.  Therefore every target orbit has size exactly `n`.

Writing `N_q=\binom{n}{m-q}`, there are `N_q/n` target orbits and

\[
 \boxed{
 \mathfrak D_{\sigma,q}(\mu)
 =\sum_{O\in\binom{[n]}{m-q}/\langle\sigma\rangle}(n-t_O)_+
 ={1\over2}\left(\sum_O|t_O-n|-(W-N_q)\right).}
\tag{3.1}
\]

Equivalently, if

\[
 E_{\sigma,q}=\sum_O(t_O-n)_+,
\]

then

\[
 \boxed{
 \mathfrak D_{\sigma,q}=E_{\sigma,q}-(W-N_q).}
\tag{3.2}
\]

Thus the forced global surplus `W-N_q` is harmless; only surplus
concentrated above `n` on some target orbits creates an equal extra deficit
elsewhere.

## 4. Exact class-average second moment

Put

\[
 \lambda_q={W\over N_q},\qquad
 f_q=\mu_q-\lambda_q\mathbf1,
\]

and let

\[
 \mathsf A_\sigma={1\over n}\sum_{j=0}^{n-1}P_{\sigma^j}
\tag{4.1}
\]

be the orthogonal projection onto functions constant on the target orbits
of `sigma`.  On an orbit `O`,

\[
 (\mathsf A_\sigma f_q)(S)={t_O\over n}-\lambda_q.
\]

Therefore

\[
 \boxed{
 \sum_O(t_O-n\lambda_q)^2
 =n\|\mathsf A_\sigma f_q\|_2^2.}
\tag{4.2}
\]

For a uniform coordinate `n`-cycle and prime `n`, every nonidentity power
is again uniformly distributed over the `n`-cycle conjugacy class.  The
class average on rank-`r` targets is

\[
                         \Pi_0-{1\over n-1}\Pi_1.
\]

It follows that

\[
 \boxed{
 \mathbb E_\sigma\mathsf A_\sigma
 =\Pi_0+{1\over n}\sum_{j\ge2}\Pi_j.}
\tag{4.3}
\]

Every exact wreath load has the uniform point margins

\[
 \sum_{S\ni x}\mu_q(S)=(m-q){W\over n}
\tag{4.4}
\]

for every coordinate `x`.  Hence `f_q` has no `U_0` or `U_1` harmonic
part.  Since each `mathsf A_sigma` is an orthogonal projection, (4.2)--
(4.4) give the exact identity

\[
 \boxed{
 \mathbb E_\sigma\sum_O(t_O-n\lambda_q)^2
 =\|f_q\|_2^2.}
\tag{4.5}
\]

For example, Cauchy--Schwarz yields only

\[
 \boxed{
 \mathbb E_\sigma\mathfrak D_{\sigma,q}
 \le \sqrt{{N_q\over n}}\,\|f_q\|_2.}
\tag{4.6}
\]

At the first shadow the known cap permits
`||f_1||_2^2=Theta(mW)`, so (4.6) is merely `O(W)`.  The exact class
average second moment does not by itself imply an `o(W)` orbit floor.

## 5. A point-margin and class-average countermodel at the first shadow

We now show that this failure is genuine at the level of the available
aggregate data.

Let

\[
 r=m-1,\qquad N=\binom n{m-1},\qquad B={W\over n},
\]

and fix one coordinate `n`-cycle `tau`.  Its action partitions the
rank-`r` targets into `K=N/n` orbits of size `n`.  Each such target orbit is
a one-design: every coordinate belongs to exactly `r` of its members.

Put

\[
                         L=\left\lfloor{2n\over9}\right\rfloor.
\tag{5.1}
\]

For all sufficiently large `m`, this obeys the exact wreath first-shadow
cap

\[
                         L\le M_m=left\lfloor{m+2\over2}\right\rfloor.
\tag{5.2}
\]

Write

\[
                         B=aL+b,qquad0\le b<L.
\]

Assign load `L` to every target in each of `a` chosen `tau`-orbits, load
`b` to every target in one further orbit when `b>0`, and load zero on all
remaining targets.  Denote this integer load vector by `mu`.

Its total mass is exact:

\[
                         \sum_S\mu(S)=n(aL+b)=nB=W.
\tag{5.3}
\]

Its point margins are also exactly those of a wreath factor.  Since every
chosen `tau`-orbit contains each coordinate in exactly `r` targets,

\[
 \boxed{
 \sum_{S\ni x}\mu(S)=r(aL+b)=rB
 \quad\text{for every }x.}
\tag{5.4}
\]

Finally `0 <= mu(S) <= L <= M_m`.

We claim that its orbit floor is linear for every coordinate `n`-cycle,
not merely for `tau`.  Let `sigma` be arbitrary and let `P` be the support
of `mu`.  For each `sigma`-target orbit `O`, put
`h_O=|O intersection P|`.  Then

\[
                         t_O\le Lh_O.
\]

Because `4L<n` for large `n`, every orbit with `h_O<=4` contributes at
least `n-4L` to the floor.  Also

\[
 \#\{O:h_O\ge5\}\le {|P|\over5},
 \qquad
 |P|\le n\left({B\over L}+1\right)={W\over L}+n.
\]

Consequently

\[
 \boxed{
 \mathfrak D_{\sigma,1}(\mu)
 \ge(n-4L)\left(
 {N\over n}-{1\over5}\left({W\over L}+n\right)
 \right).}
\tag{5.5}
\]

Now

\[
 n-4L=(1/9+o(1))n,
 \]

and, using `W/N=(m+2)/m=1+o(1)`, the parenthesis in (5.5) is

\[
 {N\over n}\left(1-{nW\over5LN}+o(1)\right)
 =\left({1\over10}+o(1)\right){N\over n}.
\]

Therefore, uniformly over every coordinate `n`-cycle `sigma`,

\[
 \boxed{
 \mathfrak D_{\sigma,1}(\mu)
 \ge(1/90+o(1))N
 =(1/90+o(1))W.}
\tag{5.6}
\]

This is an abstract load countermodel, not a claim that the vector `mu`
is realized by an exact wreath factor.  Its precise force is that the
following data are insufficient, even jointly:

1. exact total target mass `W`;
2. exact depth-one point margins;
3. the exact wreath multiplicity cap;
4. the long-cycle class-average harmonic identity.

Any proof that `mathfrak D_(sigma,1)=o(W)` for some long cycle must use
additional occurrence-support or row-packet geometry of the exact factor.

## 6. Consequence for the bridge programme

Replacing a transposition by a long cycle enlarges target orbits, but it
does not remove the mass-floor obstruction.  It changes the local
two-target rule

\[
                  (0,t)\mapsto\text{at least }(2-t)_+\text{ holes}
\]

into the orbit rule

\[
                  (\mu(S):S\in O)\mapsto(|O|-t_O)_+.
\]

Repeated occurrence-level one-step transfers attain that floor exactly,
so no further invariant exists in the unconstrained token model.  The
remaining positive problem is therefore sharply identified: construct an
exact factor and a coordinate permutation for which almost every target
orbit already has total mass at least its orbit size, and then realize the
necessary redistribution with legal row-packet switches.  Neither class
averaging nor point margins alone supplies the first requirement.

## 7. Prime-cycle band smoothing and the exact row-lift gate

There is a clean sufficient energy hypothesis which *does* control the
orbit floor.  Fix `A<infinity`, put `H=ceil(A sqrt(m))`, and suppose one
exact factor satisfies

\[
 \boxed{\|f_q\|_2^2\le C_AW\qquad(1\le q\le H).}
\tag{7.1}
\]

For a prime coordinate cycle, write

\[
 \mathsf A_\sigma={1\over n}\sum_{j=0}^{n-1}P_{\sigma^j}.
\]

The exact class average gives

\[
 \mathbb E_\sigma\|\mathsf A_\sigma f_q\|_2^2
 ={1\over n}\|f_q\|_2^2.
\tag{7.2}
\]

The orbit surplus sharpens the elementary `L^1` estimate: whenever
`lambda_q>1`,

\[
 \boxed{
 \mathfrak D_{\sigma,q}
 \le {\|\mathsf A_\sigma f_q\|_2^2
       \over4(\lambda_q-1)}.}
\tag{7.3}
\]

Indeed, with `d_O=t_O-n lambda_q` and `a=n(lambda_q-1)`, the orbit
contribution is `(-d_O-a)_+`; apply
`(y-a)_+ <= y^2/(4a)` and use
`sum_O d_O^2=n||mathsf A_sigma f_q||_2^2`.

Split at `Q=ceil(m^(1/4))`.  Averaging one common cycle simultaneously for
all depths gives

\[
 \sum_{q\le Q}\|\mathsf A_\sigma f_q\|_2^2=O_A(QW/n)
\tag{7.4}
\]

and, since `lambda_q-1 >= q^2/(2m)` in the fixed Gaussian window,

\[
 \sum_{Q<q\le H}
 {\|\mathsf A_\sigma f_q\|_2^2\over\lambda_q-1}
 =O_A(W/Q).
\tag{7.5}
\]

Cauchy--Schwarz handles (7.4), while (7.3) handles (7.5).  Thus

\[
 \boxed{
 \sum_{q\le A\sqrt m}\mathfrak D_{\sigma,q}
 =O_A(Wm^{-1/4})=o(W).}
\tag{7.6}
\]

This removes the orbit-mass obstruction but does not lift independently
routed occurrence tokens to rows.  That remaining condition has the
following exact endpoint form.

For a map `e:F -> Z_n`, define

\[
 F^{(e)}=\{\sigma^{e(C)}C:C\in F\}.
\tag{7.7}
\]

Call `e` **middle-admissible** when the middle wreath packets of `F^(e)`
partition `binom([n],m)` exactly.  Its depth-`q` load is

\[
 \mu_q^{(e)}(S)
 =\sum_{C\in F}
   \mathbf1_{\{\sigma^{-e(C)}S
                \text{ is an }(m-q)\text{-interval of }C\}}.
\tag{7.8}
\]

Every middle-admissible row-power lift preserves every target-orbit mass.
The exact remaining lift statement is:

### Row-lift gate `RL_A`

For the cycle supplied by (7.6), construct one middle-admissible exponent
map `e` such that

\[
 \boxed{
 \sum_{q\le A\sqrt m}
 \left(H_q(F^{(e)})-\mathfrak D_{\sigma,q}(F)\right)=o(W).}
\tag{7.9}
\]

Equivalently, legal row packets must realize all but `o(W)` of the coverage
attainable by independent token routing.  A sequence of exact component
switches using powers of the same `sigma` is one admissible implementation;
(7.9) states only the required endpoint.

Combining (7.6) and (7.9) gives total band defect `o(W)`.  If both the
bounded-energy factor theorem (7.1) and `RL_A` hold for every fixed `A`,
diagonalization yields a `sqrt(m) omega(m)` band, and the established
literal wreath transfer and outer-tail construction give coefficient one.

The remaining mathematics therefore separates into two precise tasks:

1. construct an exact factor with the Poisson-scale energy (7.1);
2. prove `RL_A`, overcoming the coupling of all `n` occurrences in a row
   and all depths through one common row exponent.
