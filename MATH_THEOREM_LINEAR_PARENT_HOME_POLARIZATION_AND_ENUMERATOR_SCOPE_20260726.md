# Linear parent rainbows: home polarization and the limit of the block enumerator

Date: 2026-07-26

Method: pure mathematics only.

## 0. Outcome

Fix one lower Gaussian depth

\[
                         q=A\sqrt m+O(1)\le H,\qquad A\ge0
\]

and assume \(q\ge1\).  Use the patched linear-scale atlas with

\[
 {m\over128}<R\le {m\over64},\qquad
 d=4\left\lceil {5\over2}\log _2m\right\rceil ,
\]

and discard its \(e^{-\Omega(m)}W\) bad owners.  Every retained parent
cell is a literal rainbow: at depth \(q\), each legal joint packet state
emits a set of targets of cardinality equal to the number of owners in
the cell.  Complementation fuses the upper problem to the lower one.

This note gives three exact conclusions.

1. The adaptive rank-twisted block enumerator extends to an exact
   multiblock, middle-conditioned generating function.  It controls every
   joint moment of the cell dimensions.
2. That enumerator is invariant under every change of compiler
   conjugates.  Consequently it contains no information about the
   higher intersections of literal compiler images which determine
   target holes.  No negative-dependence or Latin-resolution theorem
   follows from it alone.
3. Product-hole \(o(N_q)\) forces asymptotic **home polarization**:
   almost every target must have one fused packet group whose option
   distribution contains it with probability \(1-o(1)\).  Diffuse laws, including the
   uniform affine atlas and every bounded-density tilt of it, leave
   \[
                    (e^{-G/N_q}-o(1))N_q=\Theta(W)
   \]
   holes.  Moreover, moments of every fixed order are insufficient to
   decide the all-zero probability.

Thus the hoped-for gradual upgrade from pair codegrees to finitely many
higher moments is impossible.  A positive construction must produce a
full-order home-packet resolution: targets assigned to one fused group
must lie, almost entirely, in one actual fused compiler state.  The exact
remaining condition is the packet-configuration Hall inequality in
Section 6.

This note does **not** prove product-hole \(o(W)\), and it does not exhibit
a literal physical Hall cut against the unrestricted correlated atlas.
It proves that the aggregate enumerator and every finite-order
negative-dependence calculation are insufficient to decide that
alternative.

## 1. Exact aggregate block enumerator

Let

\[
 B_j=A_j\mathbin{\dot\cup}C_j,\qquad |A_j|=|C_j|=d,
 \qquad 1\le j\le J,
\]

be the complete macroblocks, and let \(\rho=2m-2dJ<2d\) be the residual
coordinate count.  For an unconditioned subset \(X\), put

\[
 K_j=|X\cap B_j|,\qquad
 Y_j=\#\{\text{singleton edges of }M_{j,K_j}\text{ in }X\}.
\]

For indeterminates \(u_1,\ldots,u_J,z\), one has exactly

\[
\boxed{
 \sum_{X\subseteq[2m]}z^{|X|}\prod_{j=1}^Ju_j^{Y_j(X)}
 =(1+z)^\rho\prod_{j=1}^J(1+2u_jz+z^2)^d.}           \tag{1.1}
\]

### Proof

For one fixed perfect matching of a \(2d\)-coordinate block, one edge
contributes \(1\), \(2uz\), or \(z^2\), according as it is empty,
singleton, or full.  Hence its block enumerator is
\((1+2uz+z^2)^d\).

The coefficient of \(z^k u^s\) depends only on \(d,k,s\), not on the
particular perfect matching.  In the rank-\(k\) coefficient we may
therefore replace the fixed matching by the prescribed \(M_{j,k}\).
Summing over \(k\) leaves the same polynomial.  Different blocks and the
residual coordinates multiply, proving (1.1). \(\square\)

Conditioning on the middle layer gives the exact joint probability
generating function

\[
\boxed{
 \mathbb E\left[\prod_{j\in L}u_j^{Y_j}\,\middle|\,|X|=m\right]
 =
 {\left[z^m\right](1+z)^{2d(J-|L|)+\rho}
       \prod_{j\in L}(1+2u_jz+z^2)^d
  \over \binom{2m}{m}}}                              \tag{1.2}
\]

for every \(L\subseteq[J]\).  Thus all dimension moments, not merely
pair moments, are known exactly.

## 2. Why the enumerator has no literal-overlap content

The variables in (1.1) record only:

* local ranks;
* the number of singleton edges in each adaptive frame; and
* the total rank.

They do not record which singleton edges are selected as packet
directions, their abstract compiler labels, a cycle order, or a literal
target.

### Proposition 2.1 (compiler-blindness)

Fix the complete rank-twisted status-cell partition and its packet
tiling.  Replacing the compiler state in any collection of packets
changes none of (1.1)--(1.2), while it can change every literal image
set

\[
                         I_{P,q}^{\omega}.
\]

In particular the enumerator does not determine a weighted literal score

\[
                         |A\cap I_{P,q}^{\omega}|,              \tag{2.1}
\]

and therefore cannot determine the higher cross-packet intersections
which enter the hole functional.

### Proof

The left side of (1.1) is determined before a packet factor is installed:
\(Y_j(X)\) depends only on \(X\), its local rank, and the matching
\(M_{j,K_j}\).  A compiler conjugate changes only the successor
permutation inside the already fixed packet.  Hence it leaves every
monomial of (1.1) unchanged.

On the other hand, a nontrivial affine coordinate conjugate moves the
compiler's selected literal \(q\)-faces.  Indeed the affine cube group is
transitive on the physical \(q\)-face universe, while one compiler image
has density

\[
                    {2^q\over\binom Rq}\in(0,1).
\]

If its orbit were a singleton, the image would be a nonempty invariant
proper subset of a transitive set, which is impossible.  Choose two
distinct orbit images \(I^\omega,I^{\omega'}\) and put \(A=I^\omega\).
Then (2.1) equals \(2^R\) for \(\omega\) and is strictly smaller for
\(\omega'\), while (1.1) is unchanged.  Thus even the one-image weighted
score is not encoded; higher intersections require still more literal
data. \(\square\)

The dispersed-frame property controls where candidate directions can
occur.  It does not repair Proposition 2.1: after the directions are
fixed, the compiler image can still be conjugated without changing any
block variable.

## 3. Exact product-hole functional

Let \(\mathfrak G\) be the atomic fused choice groups.  In the
complement-equivariant construction, one group consists of a packet
\(P\), its complementary packet \(P^c\), and their common compiler
label.  Write

\[
 J_{g,q}^{\omega}
   =I_{P,q}^{-,\omega}\cup I_{P^c,q}^{-,\omega}
\]

for the lower target set covered by group state \(\omega\).  Give group
\(g\) an arbitrary probability distribution \(x_g\) on its legal states
and choose distinct groups independently.  Put

\[
 p_g(T)=\Pr_{x_g}(T\in J_{g,q}^{\omega}),\qquad
 \lambda_T=\sum_gp_g(T).
\]

Packet injectivity gives

\[
 \sum_Tp_g(T)\le2^{R+1},\qquad
 \sum_T\lambda_T\le G.                               \tag{3.1}
\]

Independence gives the exact expected missing mass

\[
\boxed{
 \widetilde{\mathcal H}_q^-
 =\sum_{T\in\binom{[2m]}{m-q}}
       \prod_{g\in\mathfrak G}(1-p_g(T)).}            \tag{3.2}
\]

This is a full-order expression.  Expanding one summand uses every
intersection order among the provider events.

## 4. Diffuse product laws have a linear hole count

### Theorem 4.1 (diffuse product obstruction)

Suppose

\[
                         \eta_m:=\max_{g,T}p_g(T)=o(1).
\]

Then

\[
\boxed{
 \widetilde{\mathcal H}_q^-
 \ge N_q\exp\left\{-{G/N_q\over1-\eta_m}\right\}
 =(e^{-G/N_q}-o(1))N_q.}                            \tag{4.1}
\]

### Proof

For \(0\le p\le\eta_m\),

\[
                         \log(1-p)\ge-{p\over1-\eta_m}.
\]

Hence the hole probability of \(T\) is at least

\[
 \exp\left\{-{\lambda_T\over1-\eta_m}\right\}.
\]

The exponential is convex.  Jensen's inequality and (3.1) give

\[
 {1\over N_q}\widetilde{\mathcal H}_q^-
 \ge
 \exp\left\{-{1\over N_q(1-\eta_m)}
                 \sum_T\lambda_T\right\},
\]

which is (4.1). \(\square\)

For the uniform affine atlas, a compatible packet face has inclusion
probability \(\theta_{R,q}\), so a fused group has point probability at
most \(2\theta_{R,q}\), where

\[
                         \theta_{R,q}={2^q\over\binom Rq}=o(1).
\]

Theorem 4.1 therefore applies.  It also applies to every nonuniform tilt
whose point probabilities are at most \(K_m\theta_{R,q}\) with
\(K_m\theta_{R,q}=o(1)\).  Thus a bounded or subcritical likelihood tilt
cannot produce \(o(W)\) product holes.

## 5. Product success forces home polarization

The converse structural statement is stronger than a covariance bound.

### Theorem 5.1 (home-packet polarization)

Assume \(G/N_q=O(1)\) and

\[
                         \widetilde{\mathcal H}_q^-=o(N_q).
                                                               \tag{5.1}
\]

For each target choose a fused group \(h(T)\) maximizing \(p_g(T)\).  Then

\[
\boxed{
 {1\over N_q}
 \sum_T\bigl(1-p_{h(T)}(T)\bigr)\longrightarrow0.}    \tag{5.2}
\]

Thus almost every target has one asymptotically certain home fused group.

### Proof

Fix \(\varepsilon>0\) and \(\Lambda>0\).  Consider targets satisfying

\[
 \lambda_T\le\Lambda,\qquad
 \max_gp_g(T)\le1-\varepsilon.                       \tag{5.3}
\]

Among vectors in \([0,1-\varepsilon]^{\mathfrak G}\) of sum at most
\(\Lambda\), the product \(\prod_g(1-p_g)\) is minimized by putting as
many coordinates as possible at \(1-\varepsilon\), at most one at an
intermediate value, and the rest at zero.  Hence every target in (5.3)
has hole probability at least

\[
 c_{\varepsilon,\Lambda}
 :=\varepsilon^{\,\lceil\Lambda/(1-\varepsilon)\rceil+1}>0.    \tag{5.4}
\]

By (5.1), the number of targets in (5.3) is \(o(N_q)\).  Markov's
inequality and (3.1) give

\[
 |\{T:\lambda_T>\Lambda\}|
 \le {G\over\Lambda}=O(N_q/\Lambda).                  \tag{5.5}
\]

First let \(m\to\infty\), then let \(\Lambda\to\infty\).  We obtain, for
every fixed \(\varepsilon>0\),

\[
 {1\over N_q}
 |\{T:1-\max_gp_g(T)\ge\varepsilon\}|\longrightarrow0.          \tag{5.6}
\]

Since the deficits lie in \([0,1]\), integrating their tail
distributions proves (5.2). \(\square\)

If one now samples one option in every fused group, the expected number of
targets missed by their designated home groups is the left side of
(5.2).  Hence some integral option choice realizes all but \(o(N_q)\)
of these homes.  The difficulty is not rounding a polarized law; it is
constructing one.

## 6. Exact home-bundle and Hall condition

For a target \(T\) and fused group \(g\), define

\[
 {\cal G}_g(T)=
 \{\omega:T\in J_{g,q}^{\omega}\}.                  \tag{6.1}
\]

A bundle \(B_g\) assigned to \(g\) can be made certain by one fused
state if and only if

\[
\boxed{
                         \bigcap_{T\in B_g}{\cal G}_g(T)
                         \ne\varnothing.}             \tag{6.2}
\]

This is the full-order Latin condition.  Separate nonemptiness of the
sets \({\cal G}_g(T)\), target-to-packet Hall, and all pair codegrees do
not imply (6.2).

Equivalently, a fractional cover outside a reserve of \(E\) targets
exists if and only if, for every \(y_T\ge0\),

\[
\boxed{
 \sum_g\max_\omega\sum_Ty_T{\bf1}_{J_{g,q}^{\omega}}(T)
 +\rho_E(y)
 \ge\sum_Ty_T,}                                      \tag{6.3}
\]

where \(\rho_E(y)\) is the sum of the \(E\) largest target weights.
For the all-depth problem, the same option \(\omega\) occurs inside the
maximum for every depth; complementation supplies the upper sign.

The block enumerator (1.1) proves neither side of (6.2) and supplies no
estimate for the maximum in (6.3).

## 7. Fixed-order moments cannot determine holes

### Theorem 7.1 (exact moment-indeterminacy)

For every fixed \(k\ge1\) and every \(n\ge k+1\), there are two
exchangeable laws on provider indicators

\[
                         (\xi_1,\ldots,\xi_n)\in\{0,1\}^n
\]

such that

\[
 \mathbb E\prod_{i\in A}\xi_i
\]

is identical under the two laws for every \(|A|\le k\), but

\[
 \Pr(\xi_1=\cdots=\xi_n=0)
\]

equals \(2^{-k}\) under one law and zero under the other.

### Proof

Under the first law, choose an even integer
\(Z\in\{0,\ldots,k+1\}\) with

\[
 \Pr(Z=j)=2^{-k}\binom{k+1}j\qquad(j\ \text{even}),
\]

and then choose a uniformly random \(Z\)-subset of \([n]\).  Under the
second law use the identical formula on odd \(j\).  Both displayed
probability laws have total mass one.

For \(r\le k\), the joint moment on any \(r\) distinct coordinates is

\[
                         {\mathbb E(Z)_r\over(n)_r}.             \tag{7.1}
\]

The difference of the two numerators is

\[
 2^{-k}\sum_{j=0}^{k+1}(-1)^j\binom{k+1}j(j)_r=0,               \tag{7.2}
\]

because the \((k+1)\)-st finite difference annihilates every polynomial
of degree at most \(k\).  Thus all moments through order \(k\) agree.
The all-zero event is \(Z=0\), which has probability \(2^{-k}\) in the
even law and zero in the odd law. \(\square\)

Consequently no theorem based on pair codegrees, any fixed collection of
higher codegrees, or any fixed-order truncation of inclusion--exclusion
can prove (3.2) is \(o(W)\).  The needed structure is a full Latin
resolution or an equivalent all-order union theorem.

## 8. Verdict

The linear choice of \(R\), logarithmic rank-twisted blocks, exact
parent-cell rainbows, and fused signs reduce the one-sided residual to a
clean dichotomy.

* Diffuse or mildly tilted product laws have \(\Theta(W)\) holes.
* A successful product law must polarize to almost deterministic
  home packets.
* The exact block enumerator controls all owner-profile moments but is
  compiler-blind.
* Every fixed order of literal codegrees is insufficient.

What remains is precisely (6.2)--(6.3): construct packet bundles lying
in actual compiler images across distinct parent cells, or find a
literal weight \(y\) violating (6.3) by \(\Omega(W)\).  No such physical
violation is produced here, so the unrestricted coefficient-one gate
remains open.
