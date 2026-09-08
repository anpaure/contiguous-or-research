# Fifth-wave AA: target-specific signs, exact children, and sequence incompatibility

Date: 2026-07-25

Method: pure mathematics only.  No web search, finite search, random
experiment, or solver is used.

## 0. Outcome

Put

\[
n=2m+1,\qquad
W=\binom nm,\qquad
t=\frac Wn=\operatorname{Cat}_m,\qquad
H=\lceil A\sqrt m\rceil,
\]

where \(A>0\) is fixed and \(m\) is sufficiently large that
\(H\le m-2\).

This report proves a target-specific signing theorem which is genuinely
different from the global component-variance method of AA3.

Fix one exact factor \(F\), one transposition \(\tau\), and the genuine
ownership components of the overlay \(F\) versus \(\tau F\).  Choose a
balanced quota vector which is \(\tau\)-invariant.  For every moved target
orbit \(p=\{S,\tau S\}\), independently minimize the exact two-target
overload and choose one minimizing component signing \(\sigma^p\).  The
signing \(-\sigma^p\) is equally good.  This antipodal freedom produces a
signed target--component synchronization problem.

If \(z_{pK}\) is the action of genuine component \(K\) on the oriented
target pair, set

\[
S_{\mathrm{tar}}=\sum_{p,K}|z_{pK}|,
\]

and let \(\delta_{\mathrm{tar}}\) be the vector synchronization defect
defined in (3.2).  The main theorem gives one common component signing
\(\varepsilon\), hence one literal exact child factor, with

\[
\boxed{
\vartheta(F_\varepsilon,\beta)
\le \tau_{\mathrm{pkt}}(F_\varepsilon,\beta)
\le \Omega_\beta(F_\varepsilon)
\le
\Omega_{\mathrm{sep}}
+\sqrt{S_{\mathrm{tar}}\delta_{\mathrm{tar}}}.}
\tag{0.1}
\]

Here \(\vartheta\) and \(\tau_{\mathrm{pkt}}\) are the fractional and integral
survival-packet cover numbers, \(\Omega_\beta\) is total one-sided quota
overload, and \(\Omega_{\mathrm{sep}}\) is the sum of the exact
target-pair minima plus the immutable overload on \(\tau\)-fixed targets.
Every constant in (0.1) is exact.

Consequently, the following is sufficient for \(\mathrm{FSP}_A\): for
every fixed \(A\), construct \(F,\tau,\beta\) with

\[
\boxed{
\Omega_{\mathrm{sep}}
+\sqrt{S_{\mathrm{tar}}\delta_{\mathrm{tar}}}
=o_A(t/\sqrt m).}
\tag{0.2}
\]

Condition (0.2) is **UNPROVED** on the genuine factor fibre.  It is a
precise target-specific replacement for the failed global
component-variance gate.

The report also proves four incompatibility statements.

1. For any linear target weights, the exact loss between illegal
   resource-dependent signs and one common signing is a componentwise
   triangle deficit.  It vanishes exactly when all active resource effects
   on every component have one weak sign.
2. Recomputing components while repeatedly using the same transposition
   gives no extra freedom: the intrinsic switching cube is unchanged, and
   the whole sequence collapses to one common terminal signing.
3. Changing the target between stages creates an exact retargeting-debt
   term.  A two-step exact cycle can report two positive target gains and
   have zero endpoint gain.
4. Any exact-factor path from the canonical MSW factor to an
   \(\mathrm{FSP}_A\) endpoint has total row-replacement variation at least
   \[
   \left(\frac1{256}-o(1)\right)t.
   \]
   Thus no \(o(t)\)-variation target-specific schedule can cheaply bypass
   the canonical packet obstruction.

The fourth statement is a basin theorem, not a disproof of
\(\mathrm{FSP}_A\).  A witness may start at positive-density distance from
the canonical factor.  No implication to \(\mathrm{PTAD}_A\) is claimed:
an exact-factor path is not one literal MTF state chronology.

## 1. Exact target and packet setup

At depth \(q\le H\), put

\[
r_q=m-q,\qquad
N_q=\binom n{r_q},\qquad
\lambda_q=\frac W{N_q},\qquad
c_q=\lfloor\lambda_q\rfloor.
\tag{1.1}
\]

A balanced quota vector has

\[
\beta_q(S)\in\{c_q,c_q+1\},
\qquad
\sum_{S\in\binom{[n]}{r_q}}\beta_q(S)=W.
\tag{1.2}
\]

For an exact factor \(G\), let

\[
\mu_a(G)=\mu_q^G(S)
\qquad
(a=(q,S))
\tag{1.3}
\]

be the number of wreaths of \(G\) which own \(S\) as a cyclic interval of
length \(r_q\).  Define the total quota overload

\[
\Omega_\beta(G)
=
\sum_{q\le H}\sum_S
(\mu_q^G(S)-\beta_q(S))_+.
\tag{1.4}
\]

Since both the load and quota totals equal \(W\) at every depth,

\[
\Omega_\beta(G)
=\frac12\sum_{q\le H}\sum_S
|\mu_q^G(S)-\beta_q(S)|.
\tag{1.5}
\]

### Lemma 1.1 -- invariant balanced quotas

For every transposition \(\tau\), every \(q\le m-2\), and every balanced
upper-quota count, there is a balanced quota vector satisfying

\[
\beta_q(S)=\beta_q(\tau S)
\qquad(S\in\tbinom{[n]}{r_q}).
\tag{1.6}
\]

#### Proof

Let \(F_q\) be the number of \(\tau\)-fixed targets and \(P_q\) the number
of moved target pairs.  Explicitly,

\[
F_q=\binom{n-2}{r_q}+\binom{n-2}{r_q-2},
\qquad
P_q=\binom{n-2}{r_q-1},
\qquad
N_q=F_q+2P_q.
\tag{1.7}
\]

The number of targets which must receive quota \(c_q+1\) is

\[
\rho_q=W-c_qN_q\in\{0,1,\ldots,N_q-1\}.
\]

If \(\rho_q\le2P_q\), choose
\(b=\rho_q\bmod2\) fixed targets and
\((\rho_q-b)/2\) moved pairs.  If \(\rho_q>2P_q\), choose every moved
pair and \(\rho_q-2P_q\) fixed targets.  The latter number is at most
\(F_q\).  Since \(F_q\ge1\), both constructions are valid and invariant.
Assign the upper quota on the chosen invariant set.  \(\square\)

### Theorem 1.2 -- overload gives a packet cover with constant one

For every exact factor and every integral quota system,

\[
\boxed{
\vartheta(G,\beta)
\le\tau_{\mathrm{pkt}}(G,\beta)
\le\Omega_\beta(G).}
\tag{1.8}
\]

#### Proof

For every over-capacity resource \(a\), choose arbitrarily

\[
d_a=(\mu_a(G)-\beta(a))_+
\]

distinct owners of \(a\), and let \(B\) be the union of all chosen
wreaths.  For each \(a\), the set \(B\) contains at least \(d_a\) owners,
so deleting \(B\) leaves at most \(\beta(a)\) owners.  Hence \(B\) is an
integral survival-packet cover and

\[
|B|\le\sum_a d_a=\Omega_\beta(G).
\]

Fractional cover is a relaxation of integral cover.  This proves (1.8).
\(\square\)

Thus the very strong discrepancy estimate
\(\Omega_\beta(G)=o_A(t/\sqrt m)\) is already sufficient for
\(\mathrm{FSP}_A\), with no rounding loss and no completion step.

## 2. Exact target-pair floors and one common signing

Fix an exact factor \(F\), a transposition \(\tau\), and the genuine
ownership components \(K\) of the overlay between \(F\) and \(\tau F\).
Write the two sides of component \(K\) as \(K^+\) and
\(K^-=\tau K^+\).  A common signing
\(\varepsilon\in\{\pm1\}^{\mathscr K_\tau(F)}\) chooses side
\(K^{\varepsilon_K}\) for every component and produces one exact child
factor \(F_\varepsilon\).

Fix a \(\tau\)-invariant balanced quota vector.  For a moved target orbit

\[
p=(q,\{S,\tau S\}),
\]

choose the orientation \(S,\tau S\), and put

\[
z_{pK}
=
\#\{E\in K^+:E\text{ owns }S\}
-
\#\{E\in K^+:E\text{ owns }\tau S\}.
\tag{2.1}
\]

Let \(M_p\) be the total load on the pair.  It is independent of the
component signing, because replacing \(K^+\) by \(\tau K^+\) exchanges
the two target counts.  With

\[
D_p(\varepsilon)=\sum_Kz_{pK}\varepsilon_K,
\tag{2.2}
\]

the two child loads are

\[
\frac{M_p+D_p(\varepsilon)}2,
\qquad
\frac{M_p-D_p(\varepsilon)}2.
\tag{2.3}
\]

Let their common quota be \(b_p\).  The exact pair overload is

\[
\ell_p(D)
=
\left(\frac{M_p+D}{2}-b_p\right)_+
+
\left(\frac{M_p-D}{2}-b_p\right)_+.
\tag{2.4}
\]

This function is even and satisfies

\[
|\ell_p(D)-\ell_p(D')|
\le\frac12|D-D'|.
\tag{2.5}
\]

Indeed, away from its breakpoints the derivative of the sum is one of
\(-1/2,0,1/2\); continuity gives the global bound.

Put

\[
r_p=\min_{\eta\in\{\pm1\}^{\mathscr K_\tau(F)}}
|D_p(\eta)|.
\tag{2.6}
\]

Since \(\ell_p(D)\) is nondecreasing in \(|D|\), its exact local floor is

\[
\boxed{
\ell_p^*
=
\max\left\{
0,
M_p-2b_p,
\frac{M_p+r_p}{2}-b_p
\right\}.}
\tag{2.7}
\]

Choose \(\sigma^p\) attaining (2.6).  Both \(\sigma^p\) and
\(-\sigma^p\) attain \(\ell_p^*\).

A \(\tau\)-fixed target has the same count on the two sides of every
component, so its overload is immutable in this cube.  Let
\(\Omega_{\mathrm{fix}}\) be the sum of those fixed-target overloads, and
define

\[
\Omega_{\mathrm{sep}}
=\Omega_{\mathrm{fix}}+\sum_p\ell_p^*.
\tag{2.8}
\]

This is the illegal target-by-target optimum.  It need not be attained by
one common factor.

Define the exact signed target--component frustration

\[
\mathfrak f_{\mathrm{tar}}
=
\min_{\varepsilon_K,t_p\in\{\pm1\}}
\sum_{p,K}|z_{pK}|
\mathbf1_{\{\varepsilon_K\ne t_p\sigma_K^p\}},
\tag{2.9}
\]

where the minimum also ranges over the choice of a minimizing
\(\sigma^p\) when there are ties.

### Theorem 2.1 -- exact target-specific common-signing theorem

There is one common signing \(\varepsilon\), hence one exact child factor,
such that

\[
\boxed{
\Omega_\beta(F_\varepsilon)
\le
\Omega_{\mathrm{sep}}+\mathfrak f_{\mathrm{tar}}.}
\tag{2.10}
\]

Consequently

\[
\boxed{
\vartheta(F_\varepsilon,\beta)
\le\tau_{\mathrm{pkt}}(F_\varepsilon,\beta)
\le
\Omega_{\mathrm{sep}}+\mathfrak f_{\mathrm{tar}}.}
\tag{2.11}
\]

#### Proof

Fix \(\varepsilon,t\).  For orbit \(p\), compare \(\varepsilon\) with the
equally minimizing signing \(t_p\sigma^p\).  Flipping one component \(K\)
changes \(D_p\) by \(2|z_{pK}|\).  Equations (2.5) and the triangle
inequality therefore give

\[
\ell_p(D_p(\varepsilon))
\le
\ell_p^*
+
\sum_K|z_{pK}|
\mathbf1_{\{\varepsilon_K\ne t_p\sigma_K^p\}}.
\tag{2.12}
\]

Sum over moved orbits and add the immutable fixed-target overload.  Then
minimize the mismatch term.  This proves (2.10), and Theorem 1.2 gives
(2.11).  Every outcome switches only whole genuine component sides.
\(\square\)

The signed bipartite incidence graph has component vertices \(K\), target
vertices \(p\), and desired edge relation

\[
\varepsilon_K=t_p\sigma_K^p
\qquad(z_{pK}\ne0).
\tag{2.13}
\]

Thus \(\mathfrak f_{\mathrm{tar}}=0\) exactly when, for some joint choice
among all tied local minimizers, every signed cycle has positive sign
product.  In particular, a forest incidence graph is
perfectly synchronizable.  This is a literal exact-factor statement, not
an SDP relaxation.

## 3. Vector synchronization and the FSP sufficient theorem

Put

\[
a_{pK}=|z_{pK}|,
\qquad
S_{\mathrm{tar}}=\sum_{p,K}a_{pK}.
\tag{3.1}
\]

Define

\[
\delta_{\mathrm{tar}}
=
\min
\sum_{p,K}a_{pK}
\frac{1-\sigma_K^p\langle u_K,v_p\rangle}{2},
\tag{3.2}
\]

where the minimum is over all choices of local minimizers \(\sigma^p\)
and all unit vectors \(u_K,v_p\).  For fixed local minimizers this is a
semidefinite program in their joint Gram matrix.

Also define the angular value

\[
\mathfrak A_{\mathrm{tar}}
=
\inf
\sum_{p,K}a_{pK}
\frac{\arccos(\sigma_K^p\langle u_K,v_p\rangle)}{\pi}.
\tag{3.3}
\]

Here the infimum is over the same local minimizers and unit vectors as in
(3.2).

### Theorem 3.1 -- target synchronization rounding

One has

\[
\boxed{
\mathfrak f_{\mathrm{tar}}
=\mathfrak A_{\mathrm{tar}}
\le\sqrt{S_{\mathrm{tar}}\delta_{\mathrm{tar}}}.}
\tag{3.4}
\]

Hence some literal exact child satisfies

\[
\boxed{
\vartheta(F_\varepsilon,\beta)
\le\tau_{\mathrm{pkt}}(F_\varepsilon,\beta)
\le\Omega_\beta(F_\varepsilon)
\le
\Omega_{\mathrm{sep}}
+\mathfrak A_{\mathrm{tar}}
\le
\Omega_{\mathrm{sep}}
+\sqrt{S_{\mathrm{tar}}\delta_{\mathrm{tar}}}.}
\tag{3.5}
\]

#### Proof

Take a standard Gaussian vector \(g\), and hyperplane-round

\[
\varepsilon_K=\operatorname{sgn}\langle g,u_K\rangle,
\qquad
t_p=\operatorname{sgn}\langle g,v_p\rangle.
\]

The probability that incidence \(pK\) violates (2.13) is exactly

\[
\frac{\arccos(\sigma_K^p\langle u_K,v_p\rangle)}{\pi}.
\]

Therefore the expected mismatch cost is the objective in (3.3), and some
rounding attains no more than that expectation, proving
\(\mathfrak f_{\mathrm{tar}}\le\mathfrak A_{\mathrm{tar}}\).  Conversely,
given a discrete minimizer \((\varepsilon,t)\) in (2.9), take scalar unit
vectors \(u_K=\varepsilon_Ke\) and \(v_p=t_pe\).  Every satisfied edge has
angle zero and every violated edge has angle \(\pi\), so its angular cost
is exactly \(\mathfrak f_{\mathrm{tar}}\).  Hence equality holds.  Finally,

\[
\frac{\arccos x}{\pi}
\le\sqrt{\frac{1-x}{2}}
\qquad(-1\le x\le1),
\]

and weighted Cauchy--Schwarz gives the second inequality in (3.4).
Combine with Theorems 1.2 and 2.1.  \(\square\)

### Corollary 3.2 -- route-closing FSP certificate

For every fixed \(A>0\), suppose that for all sufficiently large \(m\)
there are an exact factor \(F_{m,A}\), a transposition \(\tau_{m,A}\), and
a common \(\tau_{m,A}\)-invariant balanced quota system through
\(H=\lceil A\sqrt m\rceil\), such that

\[
\Omega_{\mathrm{sep}}
+\sqrt{S_{\mathrm{tar}}\delta_{\mathrm{tar}}}
=o_A(t/\sqrt m).
\tag{3.6}
\]

Then \(\mathrm{FSP}_A\) holds.  Hence, by the audited packet-Hall route
and fixed-window diagonalization, MWB and the coefficient-one
contiguous-OR upper bound follow.

Condition (3.6) is **UNPROVED**.  The little-\(o\) is essential.  A bound
of order merely \(O_A(t/\sqrt m)\) does not prove \(\mathrm{FSP}_A\).
Equivalently, it is sufficient to prove separately

\[
\Omega_{\mathrm{sep}}=o_A(t/\sqrt m),
\qquad
S_{\mathrm{tar}}\delta_{\mathrm{tar}}=o_A(t^2/m).
\tag{3.7}
\]

The theorem avoids the global variance floor because it subtracts the
exact target-pair overload floors before synchronization.  It does not
assert that the synchronization defect is small in a genuine factor.

## 4. Exact linear target loss

Let \(p(G)=(\mu_a(G))_a\) be the full controlled multirank profile.  For
component \(K\), let \(a_K\) be the profile of \(K^+\) and put

\[
\Delta_K=a_K-\tau a_K.
\tag{4.1}
\]

Every child satisfies

\[
\boxed{
p(F_\varepsilon)
=\frac{p(F)+p(\tau F)}2
+\frac12\sum_K\varepsilon_K\Delta_K.}
\tag{4.2}
\]

For arbitrary real target weights \(y=(y_a)_a\), write

\[
L_y(G)=\langle y,p(G)\rangle,
\qquad
\Gamma_K(y)=\langle y,\Delta_K\rangle.
\tag{4.3}
\]

### Theorem 4.1 -- exact target triangle deficit

The best legal common signing is

\[
\boxed{
\min_\varepsilon L_y(F_\varepsilon)
=\frac{L_y(F)+L_y(\tau F)}2
-\frac12\sum_K|\Gamma_K(y)|.}
\tag{4.4}
\]

If one illegally chooses the component sign separately for every resource,
the value becomes

\[
\frac{L_y(F)+L_y(\tau F)}2
-\frac12\sum_{K,a}|y_a\Delta_{K,a}|.
\tag{4.5}
\]

Thus the exact common-sign incompatibility loss is

\[
\boxed{
\Lambda_y
=\frac12\sum_K
\left(
\sum_a|y_a\Delta_{K,a}|
-\left|\sum_a y_a\Delta_{K,a}\right|
\right).}
\tag{4.6}
\]

It vanishes if and only if, for every component \(K\), all nonzero
numbers \(y_a\Delta_{K,a}\) have one weak sign.

#### Proof

Substitute (4.2) into \(L_y\).  Every common sign \(\varepsilon_K\)
appears only in the term \(\varepsilon_K\Gamma_K(y)/2\), proving (4.4).
Allowing a different sign for each \((K,a)\) gives (4.5).  Their
difference is (4.6), and equality in the scalar triangle inequality gives
the last assertion.  \(\square\)

For every depth and component,

\[
\sum_{S\in\binom{[n]}{m-q}}\Delta_{K,(q,S)}=0,
\tag{4.7}
\]

because both component sides have the same number of wreaths and every
wreath owns exactly \(n\) cyclic intervals at that depth.  Consequently
every weight vector which is constant on each rank makes
\(\Gamma_K(y)=0\) for all \(K\).  Depth-dependent but target-uniform
linear weights are exactly powerless.  More generally, constant-plus-point
linear weights are factor-constant because exact factors have fixed totals
and fixed point margins.  Any useful first-order target must genuinely
break target symmetry.

No biased or correlated law on legal common signings can improve (4.4):
its expected value is a convex combination of deterministic vertex values.
Randomization proves existence; it does not enlarge the linear optimum.

## 5. Controlled sequences

### Theorem 5.1 -- same-transposition recomputation collapses

Let \(\mathscr D_\tau(F)\) be the exact switching cube generated by the
genuine components of \(F\) versus \(\tau F\).  Then

\[
\boxed{
\mathscr D_\tau(G)=\mathscr D_\tau(F)
\qquad(G\in\mathscr D_\tau(F)).}
\tag{5.1}
\]

Hence every finite sequence which repeatedly recomputes components but
uses only the same transposition \(\tau\) ends at one vertex
\(F_\varepsilon\) of the original cube.  It cannot realize incompatible
depth- or resource-specific signs.

#### Proof

The original overlay decomposes into unordered side pairs
\(\{K^+,K^-\}\), with \(K^-=\tau K^+\).  A cube vertex chooses exactly
one side from each pair.  Applying \(\tau\) chooses the opposite side.
The middle-mask ownership edges inside each pair are unchanged, up to
reversing left and right, and no ownership edge joins different original
components.  Thus the recomputed overlay has the same unordered component
pairs.  Successive switches only toggle the same component bits, so their
composition is one common terminal signing.  \(\square\)

Varying transpositions can leave this cube.  The following theorem is the
safe way to use such recomputation.

### Theorem 5.2 -- exact target-certificate iteration

Fix one balanced quota system.  Let \(F_0\) be exact.  At stage \(j\),
choose a transposition \(\tau_j\) under which this same quota system is
invariant, form the target-pair certificate of
Sections 2--3 in the current factor \(F_j\), and suppose

\[
\Omega_{\mathrm{sep},j}
+\sqrt{S_j\delta_j}
\le
(1-\rho_j)\Omega_\beta(F_j)+e_j,
\qquad 0\le\rho_j\le1.
\tag{5.2}
\]

Then one may choose a common-sign exact child \(F_{j+1}\) satisfying

\[
\Omega_\beta(F_{j+1})
\le(1-\rho_j)\Omega_\beta(F_j)+e_j.
\tag{5.3}
\]

Consequently

\[
\boxed{
\Omega_\beta(F_T)
\le
\Omega_\beta(F_0)\prod_{j<T}(1-\rho_j)
+
\sum_{j<T}e_j\prod_{j<s<T}(1-\rho_s).}
\tag{5.4}
\]

If the right side is \(o_A(t/\sqrt m)\), the final exact factor satisfies
\(\mathrm{FSP}_A\).

#### Proof

Apply Theorem 3.1 at every stage.  This gives (5.3) with one common
signing, so every intermediate object is an exact factor.  Iterating the
affine recurrence gives (5.4), and Theorem 1.2 gives the last conclusion.
\(\square\)

The hypothesis (5.2) is **UNPROVED**.  Merely reporting a different linear
target gain at each stage is not a substitute, because of the next exact
identity.  If the quota vector is changed between stages, or is not
\(\tau_j\)-invariant, its own retargeting error must be entered separately;
Theorem 5.2 does not silently absorb that change.

### Theorem 5.3 -- moving-target debt

For any exact-factor path \(F_0,\ldots,F_T\), put \(p_j=p(F_j)\).  Let
\(y_j\) be arbitrary stage targets and define the reported gains

\[
g_j=\langle y_j,p_{j-1}-p_j\rangle.
\]

For every terminal target \(y_*\),

\[
\boxed{
\langle y_*,p_0-p_T\rangle
=
\sum_{j=1}^Tg_j
+
\sum_{j=1}^T
\langle y_*-y_j,p_{j-1}-p_j\rangle.}
\tag{5.5}
\]

The second sum has no fixed sign.

#### Proof and sharpness

Insert \(y_j+(y_*-y_j)\) into each term of the telescoping sum
\(\langle y_*,p_0-p_T\rangle\).

The debt is necessary even on an exact two-cycle.  Let

\[
F_0=F,\qquad F_1=\tau F,\qquad F_2=F,
\qquad d=p(F)-p(\tau F).
\]

Take \(y_1=d\) and \(y_2=-d\).  Both reported gains equal \(\|d\|^2\),
but the endpoint gain is zero.  Adding a sufficiently large constant on
each rank makes both target vectors nonnegative without changing either
gain, because every profile difference has rankwise sum zero.

For a quadratic discrepancy from a fixed profile \(b\), writing
\(\Delta_j=p_j-p_{j-1}\) gives

\[
\|p_j-b\|^2-\|p_{j-1}-b\|^2
=
2\langle p_{j-1}-b,\Delta_j\rangle
+\|\Delta_j\|^2.
\tag{5.6}
\]

Thus a first-order target gain must beat half the squared actual move.  If
\(\tau b=b\), then

\[
\langle p-b,p-\tau p\rangle
=\frac12\|p-\tau p\|^2,
\tag{5.7}
\]

so on the full relabelling move the linear term and movement term cancel
exactly.  This is the sequential form of the AA3 variance obstruction.

## 6. Exact FSP path obstruction

For exact factors \(F,G\), put

\[
d(F,G)=|F\setminus G|=|G\setminus F|,
\tag{6.1}
\]

half their row symmetric difference.  For fixed balanced quotas \(\beta\),
write \(\vartheta_\beta(F)\) for the fractional survival-packet cover
number, and put

\[
\vartheta_*(F)
=\min_{\beta\text{ balanced through }H}\vartheta_\beta(F).
\tag{6.2}
\]

### Theorem 6.1 -- packet value is one-Lipschitz

For all exact factors,

\[
\boxed{
|\vartheta_\beta(F)-\vartheta_\beta(G)|\le d(F,G),
\qquad
|\vartheta_*(F)-\vartheta_*(G)|\le d(F,G).}
\tag{6.3}
\]

#### Proof

Start with a fractional packet cover on \(F\).  Retain its weights on
\(F\cap G\) and give weight one to every row of \(G\setminus F\).  A
packet of \(G\) either contains a new row and is hit with weight one, or is
entirely common.  In the latter case it is the identical resource-labelled
packet in \(F\), so the retained weights cover it.  Therefore

\[
\vartheta_\beta(G)\le\vartheta_\beta(F)+d(F,G).
\]

Reverse \(F,G\).  Minimizing over the same finite family of balanced quota
vectors preserves the common Lipschitz constant, proving the second
inequality.  \(\square\)

Let \(F_m^{\mathrm{MSW}}\) be the canonical exact MSW factor.  The audited
depth-one packet certificate proves, uniformly over every balanced quota
system,

\[
\vartheta_*(F_m^{\mathrm{MSW}})
\ge\operatorname{Cat}_{m-4}.
\tag{6.4}
\]

### Theorem 6.2 -- positive-density sequence incompatibility

Every exact-factor path \(F_0,\ldots,F_T\) with
\(F_0=F_m^{\mathrm{MSW}}\) satisfies

\[
\boxed{
\sum_{j=1}^Td(F_{j-1},F_j)
\ge
\operatorname{Cat}_{m-4}-\vartheta_*(F_T).}
\tag{6.5}
\]

In particular, if \(F_T\) is an \(\mathrm{FSP}_A\) endpoint, then

\[
\boxed{
\sum_{j=1}^Td(F_{j-1},F_j)
\ge
\left(\frac1{256}-o(1)\right)t.}
\tag{6.6}
\]

If every step replaces at most \(s\) rows, at least
\((1/256-o(1))t/s\) nontrivial steps are necessary.

#### Proof

The triangle inequality and Theorem 6.1 give

\[
\sum_jd(F_{j-1},F_j)
\ge d(F_0,F_T)
\ge\vartheta_*(F_0)-\vartheta_*(F_T).
\]

Use (6.4).  Since

\[
\frac{\operatorname{Cat}_{m-4}}{\operatorname{Cat}_m}
=\frac1{256}+O(m^{-1})
\]

and an \(\mathrm{FSP}_A\) endpoint has
\(\vartheta_*(F_T)=o_A(t/\sqrt m)=o(t)\), (6.6) follows.  \(\square\)

This theorem permits arbitrary transpositions, recomputation, correlated
signs, temporary uphill moves, and even arbitrary exact-factor steps.  It
therefore gives a genuine exact-factor incompatibility theorem.

There is also an endpoint compression statement.  For arbitrary exact
factors \(F,G\), cancel their common rows and form the direct middle-owner
overlay.  Switch its balanced connected components one at a time.  Every
intermediate family is an exact factor, and each noncommon row is replaced
exactly once.  Hence there is an exact path from \(F\) to \(G\) of total
variation exactly \(d(F,G)\).  Consequently, under general exact-pair
ownership moves, minimum path recourse to an endpoint property is exactly
ordinary row distance to its witness set.  Under transposition-only moves,
only the lower bound is automatic; reachability remains restricted to the
universal switch class.

The known native \((2\ 3)\)-cube switch replaces exactly
\(2\operatorname{Cat}_{m-4}\) canonical rows and destroys the displayed
canonical packet certificate.  Thus positive Catalan density is
order-sharp for escaping that certificate.  The resulting child is not
proved to satisfy \(\mathrm{FSP}_A\).

## 7. A genuine target-private MSW synchronization

The target theorem is not vacuous.  In the canonical MSW factor, let
\(\tau=(2\ 3)\), and use the audited suffix-indexed depth-one targets
\(S_V\), \(V\in\mathcal D_{m-4}\), from the canonical packet
obstruction.  The audited symbolic semilength-four owner table gives the
target core word

\[
Q=10111101
\]

has complement \(27\) and exactly the three base owners

\[
11110000,\qquad11101000,\qquad11001100.
\]

Its transposed companion

\[
Q'=(2\ 3)Q=11011101
\]

has complement \(37\) and exactly the single base owner \(11011000\).
The audited suffix-separation lemma says that every owner after appending
\(V\) is obtained by appending that same \(V\) to a base owner.  Hence the
paired canonical loads are exactly

\[
(\mu(S_V),\mu(\tau S_V))=(3,1).
\tag{7.1}
\]

Assign quota two to both targets in every such moved pair.  The available
upper-quota count satisfies

\[
2\operatorname{Cat}_{m-4}
<\rho_1=\frac{2W}{m+2}
\qquad(m\ge4).
\tag{7.2}
\]

Reserve these moved pairs first and apply the parity construction of
Lemma 1.1 to the remaining \(\rho_1-2\operatorname{Cat}_{m-4}\)
upper quotas.  If \(L=\operatorname{Cat}_{m-4}\), then

\[
L\le P_1,
\qquad
0\le\rho_1-2L\le F_1+2(P_1-L),
\]

where the first inequality follows, for example, by injecting an
\((m-4)\)-subset of \([2m-8]\) into an \((m-2)\)-subset of
\([2m-1]\) after adjoining two fixed new elements.  Thus the same parity
proof works using the remaining \(P_1-L\) pairs and all \(F_1\) fixed
targets.

For each \(V\), the private size-two genuine component
\(\mathcal C_{0,1100V}\) changes the pair load from \((3,1)\) to
\((2,2)\).  Indeed, its old rows are

\[
11001100V,\qquad10101100V.
\]

The first owns \(Q V\) but not \(Q'V\), while the second owns neither.
After transposition the new side therefore removes one \(S_V\) owner and
adds one \(\tau S_V\) owner.  Suffix separation prevents cross-effects
between distinct \(V\)'s.  These components are distinct for different
\(V\).  Therefore the local target demands on this Catalan family are
simultaneously satisfiable.  Write \(\mathcal T_{\mathrm{MSW}}\) for this
restricted family.  Then

\[
\Omega_{\mathrm{sep}}^{\mathcal T_{\mathrm{MSW}}}=0,
\qquad
\mathfrak f_{\mathrm{tar}}^{\mathcal T_{\mathrm{MSW}}}=0
\tag{7.3}
\]

Switching all private components is one exact child factor and costs
exactly \(2\operatorname{Cat}_{m-4}\) row
replacements.

This removes the known canonical packet family by a common signing even
though a global fair-variance argument does not identify the move.  It does
not prove (3.6): overloads on all other targets and depths remain
uncontrolled.

## 8. PTAD scope

For a proper marked set \(Z\), the audited trace repair functional has the
exact linearization

\[
\Phi_Z(\mathcal H)
=
\min_{U\subseteq2^Z}
\left[
\sum_{R\in U}
\bigl(\nu(2m-|Z|)+\mathbf1_{\{R\ne\varnothing\}}\bigr)
+
\#\{S\in\mathcal H:S\cap Z\notin U\}
\right].
\tag{8.1}
\]

Thus target-specific signs could help estimate the last, linear hole term
only after one actual hole family \(\mathcal H\), one proper trace set, and
one literal MTF state walk have been constructed.  An exact-factor
switching sequence does not supply the portal ordering, legal MTF bridges,
or common chronology required by \(\mathrm{PTAD}_A\).  Different factor
states cannot donate different depths to one word.  No PTAD implication is
proved in this report.

## 9. Exact status

### Proved

1. Existence of \(\tau\)-invariant balanced quotas at every controlled
   rank.
2. The constant-one implication
   \(\vartheta\le\tau_{\mathrm{pkt}}\le\Omega_\beta\).
3. The exact pair-overload floor (2.7).
4. The literal target-specific common-signing theorem (2.10).
5. The signed-incidence balance criterion and vector bound
   \(\mathfrak f_{\mathrm{tar}}\le\sqrt{S\delta}\).
6. The fixed-window sufficient condition (3.6) for \(\mathrm{FSP}_A\).
7. The exact linear triangle-deficit formula (4.6).
8. Same-transposition sequence collapse and moving-target debt.
9. Exact target-certificate iteration through recomputed factors.
10. One-Lipschitz packet value and the positive-density canonical path
    obstruction.
11. A common genuine MSW signing which synchronizes the known Catalan
    target family at exact cost \(2\operatorname{Cat}_{m-4}\).

### Unproved and not claimed

1. The route-closing genuine bound (3.6).
2. Any theorem forcing low target-incidence holonomy in an arbitrary exact
   factor.
3. \(\mathrm{FSP}_A\), MWB, or the contiguous-OR theorem.
4. \(\mathrm{PTAD}_A\) or any factor-to-MTF chronology translation.
5. That the positive-density MSW child has small packet-cover value outside
   the explicitly repaired target family.

The fifth-wave conclusion is therefore exact: the theorem in this report
beats the global variance no-go if the signed target--component incidence
has Catalan-small pair floors and synchronization defect.  One common
hyperplane rounding preserves exact-factor legality.  Repeated
same-transposition scheduling gives no extra freedom, and every adaptive
route out of the canonical basin must pay positive Catalan-density row
variation.
