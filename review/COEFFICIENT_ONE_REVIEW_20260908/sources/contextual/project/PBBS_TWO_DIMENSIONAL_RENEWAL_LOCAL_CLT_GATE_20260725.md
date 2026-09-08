# An abstract two-dimensional Fourier gate, and why the PBBS record state does not satisfy it

Date: 2026-07-25

This note concerns only the unresolved large-overlap, zero-winding part of
the coefficient-one PBBS packing theorem.  The scalar seam renewal has
critical mass \(\Theta(s)\).  Sections 1--3 prove that a genuinely diffusive
block-index coordinate would reduce that mass to \(O(\sqrt s)\), which is
already sufficient.  The subsequent exact calculation in
`PBBS_TWO_DIM_CARRIER_TRANSFER_COUNTEROBSTRUCTION_20260725.md` shows that the
natural PBBS record-minimum state is not diffusive: its transfer is upper
triangular and its eigenvalues are independent of the block marker.  Thus
the abstract theorem below remains correct, but its proposed direct PBBS
application is retracted.  The valid PBBS replacement is the explicit
source-sensitive triangular resolvent recorded in that note.

## 1. Scalar additive renewal

Let

\[
 \rho_s(y)=r_s\sum_{j\in\mathbb Z}p_s(j)y^j,
 \qquad \sum_jp_s(j)=1,
 \tag{1.1}
\]

have nonnegative coefficients, and suppose

\[
 {c_0\over s}\le1-r_s\le {C_0\over s}.
 \tag{1.2}
\]

The coefficient of displacement \(d\) in the renewal resolvent is

\[
 G_s(d):=[y^d]{1\over1-\rho_s(y)}
 =\sum_{k\ge0}r_s^k p_s^{*k}(d).
 \tag{1.3}
\]

### Lemma 1.1 (renewal local limit)

If

\[
 \sup_{d\in\mathbb Z}p_s^{*k}(d)\le {C\over\sqrt{k+1}}
 \qquad(k\ge0)
 \tag{1.4}
\]

uniformly in \(s\), then

\[
 \boxed{\sup_dG_s(d)=O(\sqrt s)=o(s).}
 \tag{1.5}
\]

#### Proof

By (1.3)--(1.4),

\[
 G_s(d)\le C\sum_{k\ge0}{r_s^k\over\sqrt{k+1}}.
\]

Equation (1.2) gives \(r_s^k\le\exp(-c_0k/s)\).  Comparison with the
integral of \(e^{-c_0x/s}x^{-1/2}\) gives \(O(\sqrt s)\).  \(\square\)

Thus the unrestricted scalar mass \((1-r_s)^{-1}=\Theta(s)\) is critical
only because it sums over every block displacement.  Prescribing one block
index gains the local-limit factor \(s^{-1/2}\).

## 2. A matrix version

The genuine carrier must also retain an unmatched-height state.  Let
\(\mathcal H_s\) be a finite-dimensional Hilbert space with a fixed weighted
norm, and let

\[
 \mathsf R_s(y)=\sum_{j\in\mathbb Z}\mathsf R_{s,j}y^j
 \tag{2.1}
\]

be a matrix Laurent polynomial with nonnegative entries.  Its power records
one more seam-renewal pair, while the exponent of \(y\) records the change in
the current dual-block index.  Put

\[
 \mathsf G_s(y)=(I-\mathsf R_s(y))^{-1}.
 \tag{2.2}
\]

### Theorem 2.1 (matrix Fourier gate)

Assume there are absolute constants \(c_0,C_0,c_1,c_2,\theta_0>0\) and
numbers \(r_s\) satisfying (1.2) such that

\[
 \|\mathsf R_s(e^{i\theta})\|
 \le r_s e^{-c_1\theta^2}
 \qquad(|\theta|\le\theta_0),
 \tag{2.3}
\]

and

\[
 \|\mathsf R_s(e^{i\theta})\|
 \le r_s(1-c_2)
 \qquad(\theta_0\le|\theta|\le\pi).
 \tag{2.4}
\]

Then, for all vectors \(u,v\in\mathcal H_s\) and all \(d\in\mathbb Z\),

\[
 \boxed{
 \left|[y^d]\langle u,\mathsf G_s(y)v\rangle\right|
 \le C\sqrt s\,\|u\|\|v\|.}
 \tag{2.5}
\]

#### Proof

Fourier inversion and the Neumann series give

\[
 [y^d]\langle u,\mathsf G_s(y)v\rangle
 ={1\over2\pi}\int_{-\pi}^{\pi}e^{-id\theta}
 \langle u,(I-\mathsf R_s(e^{i\theta}))^{-1}v\rangle\,d\theta.
 \tag{2.6}
\]

On \(|\theta|\le\theta_0\), (2.3) gives

\[
 \|(I-\mathsf R_s(e^{i\theta}))^{-1}\|
 \le {1\over1-r_se^{-c_1\theta^2}}
 \le {C\over s^{-1}+\theta^2}.
 \tag{2.7}
\]

The integral of the last function over a fixed interval is \(O(\sqrt s)\).
On the complementary interval, (2.4) makes the resolvent norm \(O(1)\).
Substitution in (2.6) proves (2.5).  \(\square\)

The same proof works on a proper lattice after integrating over one dual
period, or with a finite collection of peripheral lattice phases.  What is
essential is quadratic decay away from each permitted phase and a uniform
gap elsewhere.

## 3. Consequence for the PBBS zero-winding kernel

The audited one-crossing kernel satisfies, on every fixed Gaussian band,

\[
 \sup_n2^{-n}[x^n]K^\times_{s,t,u}(x)=O(s^{-6}),
 \tag{3.1}
\]

whereas its unrestricted scalar renewal factor has critical mass
\(\Theta(s)\).  Suppose the actual separator-spanning carrier admits a
coefficientwise synchronized transfer representation in which

* unmatched height is the internal state in \(\mathcal H_s\);
* current dual-block index is marked by \(y\);
* the required endpoint identities prescribe one displacement \(d\); and
* the one-pair transfer \(\mathsf R_s(y)\) satisfies (2.3)--(2.4), with
  source and sink vectors of uniformly bounded weighted norm.

Then Theorem 2.1 replaces the scalar \(\Theta(s)\) factor by
\(O(\sqrt s)\).  Consequently one fixed height contributes at most

\[
 O(4^m s^{-11/2}),
 \tag{3.2}
\]

and summing over \(s\asymp_A\sqrt m\) gives

\[
 O_A(4^m m^{-9/4})
 =O_A\!\left({B_m\over m^{3/4}}\right)
 =o_A\!\left({B_m\over\sqrt m}\right).
 \tag{3.3}
\]

Together with the already proved sub-Gaussian packing estimate, this would
settle the complete zero-winding sector of \((QST_A)\).

## 4. The originally proposed PBBS assertion (now refuted for the natural record state)

The mathematical burden is now narrower than a direct \(o(s)\) Green bound:

> **PBBS block-diffusion lemma.**  After conditioning on the common balanced
> endpoint word and expressing the literal carrier equation in the state
> (unmatched height, current dual-block index), the critical one-pair
> transfer has a uniformly nondegenerate additive block displacement, in
> the operator sense (2.3)--(2.4).

Equivalently, the leading scalar seam mode must acquire quadratic Fourier
curvature bounded below by an absolute constant when the block index is
marked.  A weaker curvature \(c_s\) still gives a resolvent bound
\(O(\sqrt{s/c_s})\), so any \(c_s\gg s^{-1}\) is sufficient for little-oh.

This lemma is not proved here, and for the natural exact record state it is
false.  Proposition 4.2 of
`MATH_ATTACK_QST_TWO_SEAM_TRANSFER_KERNEL_20260725.md` shows why the block
coordinate cannot be deleted.  The triangular calculation cited above
shows that retaining it gives a running-maximum process rather than an
additive local limit.  What survives from this section is only the abstract
sufficiency theorem, not the claimed PBBS route.

## 5. Record-depth weighting of the common boundary

The natural exact block state is the record depth of the common balanced
boundary word.  The following estimate is unconditional and is useful for
combining any state-dependent resolvent with the shared-boundary collision
theorem.

For a balanced binary word (e) of length (2\ell), put

\[
 h(e)=-\min_{0\le j\le2\ell}\operatorname{net}(e[1,j]).
 \tag{5.1}
\]

### Lemma 5.1 (first record moment of bridges)

\[
 \boxed{
 \sum_{e:\,|e|=2\ell,\ \operatorname{net}(e)=0}h(e)
 \le 4^\ell.}
 \tag{5.2}
\]

The same bound holds after imposing the endpoint-letter restrictions of a
genuine PBBS common boundary.

#### Proof

By the layer-cake identity,

\[
 \sum_eh(e)=\sum_{a\ge1}\#\{e:h(e)\ge a\}.
\]

Reflection at the first visit to level (-a) injects the latter bridges
into paths with (ell-a) up-steps and (ell+a) down-steps.  Hence

\[
 \#\{e:h(e)\ge a\}\le\binom{2\ell}{\ell+a}.
\]

Summing the strict upper half of the binomial row gives at most
(2^{2\ell-1}<4^\ell).  Endpoint restrictions only remove words.
(\square)

In the notation of Lemma 2.1 of
`PBBS_SHARED_BOUNDARY_COLLISION_20260725.md`, each forward and dual point
probability is at most (C4^{-\ell}).  Therefore (5.2) gives the weighted
Hadamard estimate

\[
 \boxed{
 \sum_{e\ {
m balanced}}h(e)
 \Pr(U[1,2\ell]=e)
 \Pr(V[|V|-2\ell+1,|V|]=e)
 \le C4^{-\ell}.}
 \tag{5.3}
\]

The unweighted collision is (O(4^{-\ell}/\sqrt{\ell+1})); weighting by
the exact record state therefore costs only the natural factor
(O(\sqrt{\ell+1})), not the worst-case factor (ell).
