# Stationary feedback: the endpoint-fiber obstruction

This note isolates the exact obstruction to a feedback rule that both preserves
the uniform permutation law and preferentially serves an externally fixed
family of unseen `k`-sets.  It applies to the tail-MTF state graph used in
`MASTER_HANDOFF.md`, Section 5.7.  No computation is used.

## 1. State graph and labels

Fix integers `n>=1` and `0<=sigma<=n-1`, put `f=n-sigma`, and assume
`1<=k<=f`.  Let `Omega=S_n`.  Write a state as

\[
 \pi=(\pi_1,\ldots,\pi_n),
\]

from most to least recent.  Put
`J={f,f+1,...,n}` and `d=|J|=sigma+1`.  For `j in J`, let

\[
 T_j\pi=(\pi_j,\pi_1,\ldots,\pi_{j-1},
                  \pi_{j+1},\ldots,\pi_n)
\]

be the eligible move which records `pi_j` and moves it to the front.  Let

\[
 C_k(\pi)=\{\pi_1,\ldots,\pi_k\}.
\]

The directed state graph is represented as a bipartite graph with a left and
a right copy of `Omega` and the edges

\[
 \pi_L\longrightarrow (T_j\pi)_R \qquad (j\in J).
\]

Every generator `T_j` is a bijection, so this graph is `d`-regular on both
sides.  The set observed on the edge is the new length-`k` window

\[
 \ell(\pi,j)
   =\{\pi_1,\ldots,\pi_{k-1},\pi_j\}
   =C_k(T_j\pi).                                      \tag{1}
\]

The last equality uses `j>=f>=k` and remains true when `j=k`.

## 2. Exact matching obstruction

Let `U` be any family of rank-`k` sets, interpreted as the currently unseen
family, and put

\[
 \Omega_U=\{\tau\in\Omega:C_k(\tau)\in U\},\qquad
 M={n\choose k},\qquad \rho=|U|/M.
\]

Each color fiber has size

\[
 |C_k^{-1}(S)|=k!(n-k)!,
\]

and hence `|Omega_U|=rho n!`.

**Theorem 2.1 (endpoint-fiber theorem).**  The subgraph consisting of the
edges labeled by members of `U` is exactly the set of full-graph edges whose
right endpoint lies in `Omega_U`.  Its maximum matching size is

\[
 |\Omega_U|=k!(n-k)!|U|=\rho n!.
\]

Consequently it has a perfect matching, or a fractional perfect matching,
if and only if `U` is the whole rank-`k` layer.

**Proof.**  Equation (1) says that every incoming edge of a fixed right state
`tau` has the single label `C_k(tau)`.  Thus all `d` incoming edges of `tau`
are retained when `tau in Omega_U`, and none are retained otherwise.  A
matching therefore has size at most `|Omega_U|`.  Conversely, fix any
`j_0 in J`; the edges

\[
 (T_{j_0}^{-1}\tau)_L\longrightarrow\tau_R
       \qquad(\tau\in\Omega_U)
\]

form a matching of that size.  If `U` is proper, taking all left vertices in
Hall's condition gives the deficient neighborhood `Omega_U`.  The same cut
rules out a fractional perfect matching.  If `U` is the whole layer, any one
generator `T_{j_0}` is a perfect matching.  \(\square\)

This conclusion is independent of every pseudorandomness or discrepancy
property of `U`: the obstruction is the missing right fibers themselves.
If `c_U(pi)` is the number of unseen members of the fan at `pi`, double
counting the retained edges also gives the exact identity

\[
 \frac1{n!}\sum_{\pi\in\Omega}c_U(\pi)=d\rho.           \tag{1a}
\]

Thus quasirandomness may make the fan degrees nearly constant, but it can
only redistribute this fixed amount of unseen incidence.

There is a sharper version which incorporates a necessary fact about an
actual coverage history: immediately before a new observation, the current
top-`k` color has already been observed.  Assume for this refinement that
`k<f`.  Define

\[
 D_k(\tau)=\{\tau_2,\ldots,\tau_{k+1}\}
\]

and let `b(U)` be the number of oriented Johnson edges `(A,B)` with
`A notin U`, `B in U`, and `|A cap B|=k-1`.

**Theorem 2.2 (lifted Johnson-boundary theorem).**  Retain only transitions
whose left color is covered and whose new label is unseen.  This subgraph is
the union of all incoming fibers of

\[
 \Xi_U=\{\tau:C_k(\tau)\in U,\ D_k(\tau)\notin U\}.
\]

Its maximum matching size is exactly

\[
 |\Xi_U|=b(U)(k-1)!(n-k-1)!.
\]

Every doubly stochastic eligible kernel puts the same normalized mass on
covered-to-unseen transitions, namely

\[
 \frac{|\Xi_U|}{n!}
   =\frac{b(U)}{M k(n-k)}.                             \tag{1b}
\]

**Proof.**  For every `j in J`, the predecessor of `tau` is

\[
 T_j^{-1}\tau=(\tau_2,\ldots,\tau_j,\tau_1,
                    \tau_{j+1},\ldots,\tau_n).
\]

Since `j>=f>k`, all `d` predecessors have the same old color `D_k(tau)`.
Thus either all incoming edges of `tau` are covered-to-unseen, precisely when
`tau in Xi_U`, or none are.  The fixed-generator matching used in Theorem
2.1 attains the matching bound, while the column sums of any doubly stochastic
kernel give total mass `|Xi_U|/n!`.  Finally, an oriented boundary pair `(A,B)` uniquely
specifies `tau_1=B\setminus A`, `tau_{k+1}=A\setminus B`, and the set in
positions `2,...,k`; ordering the intersection and the remaining letters
gives `(k-1)!(n-k-1)!` states.  \(\square\)

For `0<rho<1`, under a uniform left state the current color is covered with
probability `1-rho`.  Hence every doubly stochastic eligible kernel satisfies

\[
 \Pr(\text{new unseen}\mid\text{current covered})
 =\frac{b(U)}{M k(n-k)(1-\rho)}.
\]

For a cut-quasirandom family satisfying

\[
 b(U)=(1+o(1))\rho(1-\rho)M k(n-k),
\]

the mass in (1b) is
`(1+o(1))rho(1-rho)`.  Conditional on a uniform state having covered current
color, the doubly stochastic covered-to-unseen rate is consequently
`(1+o(1))rho`, the baseline density.  Pseudorandomness removes boundary
bottlenecks but does not create stationary preference.

As a structured comparison, for the star
`U={S:1 in S}` one has `rho=k/n` and

\[
 b(U)=|U|(n-k),\qquad |\Xi_U|/n!=1/n.
\]

Here the lifted boundary is exceptionally thin: entering `U` requires letter
`1` to be the newly moved front letter.

## 3. Every doubly stochastic kernel has the same unseen mass

A kernel `K` on the eligible graph is doubly stochastic when

\[
 \sum_\tau K(\pi,\tau)=1\quad\hbox{and}\quad
 \sum_\pi K(\pi,\tau)=1.
\]

**Theorem 3.1 (stationary mass identity).**  For every such `K`, its total
stationary mass on edges labeled by `U` is exactly `rho`:

\[
 \frac1{n!}\sum_{\pi\in\Omega}\sum_{\tau\in\Omega}
 K(\pi,\tau)\,1_{\{C_k(\tau)\in U\}}
 =\frac{|U|}{M}.                                      \tag{2}
\]

**Proof.**  Sum first over the right endpoint and use its column sum:

\[
 \frac1{n!}\sum_{\tau\in\Omega_U}\sum_\pi K(\pi,\tau)
 =\frac{|\Omega_U|}{n!}=\rho.\qquad\square
\]

Thus a doubly stochastic kernel cannot improve even the average one-step
unseen probability above the uncovered density.  In particular, if every
row gave unseen moves probability at least `1-eta`, then necessarily
`rho>=1-eta`.  A family of density bounded away from one cannot support an
"almost always unseen" stationary kernel, however quasirandom it is.

There is also a quantitative approximate version which needs no Markov or
kernel assumption.  If `Pi` is uniform, one eligible move produces `Pi'`
with law `q`, and

\[
 \|q-\operatorname{Unif}(\Omega)\|_{TV}\le\varepsilon,
\]

then

\[
 \Pr(C_k(\Pi')\in U)\le \rho+\varepsilon.              \tag{3}
\]

Indeed, apply the defining event bound for total variation to `Omega_U`.
So a one-step advantage `delta` over the uniform unseen rate forces at least
`delta` total-variation displacement from stationarity.

Equivalently it is enough to compare the law of `C_k(Pi')` with the uniform
law on the rank-`k` layer; passing from the state to its color can only reduce
total variation.  In particular, a rule which chooses an unseen label with
probability at least `1-eta` must displace the next-state law from uniform by
at least `1-eta-rho`.

More generally, let the input state have an arbitrary law `p` and apply a
doubly stochastic eligible kernel `K`.  Since `K` fixes the uniform law and
Markov kernels contract total variation,

\[
 \Pr_{pK}(C_k(\Pi')\in U)
 \le \rho+\|p-\operatorname{Unif}(\Omega)\|_{TV}.       \tag{3a}
\]

Thus a doubly stochastic adaptive step can exploit a correlation already
present between the state and `U`, but it cannot obtain a near-certain unseen
hit from a conditional state law close to uniform.  At uncovered density
`rho`, hit probability `1-eta` requires conditional state displacement at
least `1-eta-rho`.

This bound is sharp as a one-step statement.  Assume `0<rho<1` and fix
`h in [rho,1]`.  Among all input laws `p` and all doubly stochastic eligible
kernels whose output label lies in `U` with probability at least `h`, the
minimum possible `\|p-Unif(Omega)\|_TV` is exactly

\[
 h-\rho.                                               \tag{3b}
\]

The lower bound is (3a).  For equality, give `Omega_U` total mass `h`,
uniformly within it, give its complement mass `1-h`, uniformly within it,
and call the resulting output law `q_h`.  Then
`\|q_h-Unif(Omega)\|_TV=h-rho`.  Fixing any `j_0 in J`, use the deterministic
bijection `T_{j_0}` and take the input law to be the pullback of `q_h`.
This realizes `q_h` and preserves total variation.  In particular, forcing
an unseen move with probability one costs exactly `1-rho` of conditional
state displacement; the difficulty is to generate and transport that
correlation along one coverage trajectory.  This sharpness construction does
not impose that the input color is already covered; with that additional
history constraint, Theorem 2.2 supplies the relevant boundary capacity.

## 4. Coupon-plateau consequence

The same endpoint observation gives a process-level no-go.  Consider any
sequence of observed rank-`k` sets `S_1,S_2,...`; consecutive observations
need not be adjacent eligible moves.  Let `U_t` be the family not seen among
`S_1,...,S_t` (so `U_0` is the whole layer), let `u_t=|U_t|`, and let `F_t`
contain the observation history.
Suppose the conditional law of the next observed set satisfies

\[
 \bigl\|\mathcal L(S_{t+1}\mid F_t)
       -\operatorname{Unif}\!\left({[n]\choose k}\right)\bigr\|_{TV}
 \le\varepsilon_t.
\]

Then

\[
 \Pr(S_{t+1}\in U_t\mid F_t)
 \le \frac{u_t}{M}+\varepsilon_t
\]

and therefore, with `a=1-1/M`,

\[
 \mathbb E u_L
 \ge M a^L-\sum_{t=0}^{L-1}a^{L-1-t}\mathbb E\varepsilon_t.       \tag{4}
\]

In particular, if `L=mu M+O(1)` for fixed `mu` and

\[
 \frac1M\sum_{t<L}\mathbb E\varepsilon_t=o(1),
\]

then

\[
 \frac{\mathbb E u_L}{M}\ge e^{-\mu}-o(1).             \tag{5}
\]

For exact conditional uniformity of the next label, equality holds in the new-hit
probability and the expected coupon plateau is exactly
`M(1-1/M)^L`.

**Proof.**  Conditional on `F_t`, use (3) with `U=U_t`.  Since one new set is
removed precisely on a new hit,

\[
 \mathbb E(u_{t+1}\mid F_t)\ge a u_t-\varepsilon_t.
\]

Iteration proves (4), and (5) follows from `a^L -> e^{-mu}`.  \(\square\)

## 5. What this settles, and what it does not

The proposed static route

> for each uncovered family `U`, choose a doubly stochastic eligible kernel
> supported mostly on moves labeled by `U`

cannot beat uniform sampling.  Its optimum stationary unseen mass is exactly
`|U|/M`, and a good-only fractional matching fails for every proper `U`.
Even approximate conditional stationarity with vanishing average error leaves
the constant coupon plateau.

This does **not** rule out coefficient-one adaptive walks.  A successful walk
must create and retain a substantial correlation between its permutation
state and its coverage history.  Its unconditional permutation marginal may
even be uniform (for example after a random phase shift), but its conditional
law given the uncovered family cannot remain close to uniform.  Equivalently,
the useful flow object must live on correlated pairs `(permutation, coverage
state)`, or on a specially ordered trajectory through the equal-size color
fibers, rather than being a doubly stochastic kernel on permutations for each
externally frozen `U`.

This obstruction is compatible with the open late-access/R''-functional
program: that program seeks repeated fan access for survivors and deliberately
uses coverage-state correlation; it must not be strengthened to conditional
uniform mixing of the full permutation state.
