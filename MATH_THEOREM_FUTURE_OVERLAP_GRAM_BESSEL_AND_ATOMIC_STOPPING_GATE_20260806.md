# Future-overlap Gram factorization, marked Bessel reduction, and the atomic stopping gate

**Date:** 2026-08-06  
**Method:** exact product-residual coefficient algebra, Schur-product
positivity, finite constituent-role expansion, and Hilbert-space Bessel
inequalities; no computation or search  
**Status:** unconditional algebraic reduction. The apparent four-atomic-
macro normalization in the angular survivor term is not an irreducible
fourth moment: it factors through products of unmarked, one-mark, and
two-mark future-overlap norms. Literal stopping preserves the Gram
factorization pointwise. If the marked difference is retained, however,
deletion can create an atomic boundary term; if it is polarized into
positive marked norms, no stopping boundary remains but one still needs a
sharp aggregate marked-capacity estimate. Neither alternative is proved
at the final required scale here.

This note continues
MATH_THEOREM_STABILIZER_SHELL_DECOMPOSITION_OF_SCOV4_20260806.md and
MATH_THEOREM_JOINT_ROOT_PAIR_LYAPUNOV_AND_MARKED_CLUSTER_NORMALIZATION_20260806.md.

## 1. Exact factorization of the current pair coefficient

Fix a live pair root \(Q\), and let \(E,F\supseteq Q\) be available atomic
doublets. Put

\[
 n_E=|(E-Q)\cap(\mathcal L\mathbin{\dot\cup}\mathcal R)|,
 \qquad s_E=|E\cap([k]\times[L])|=2,
\tag{1.1}
\]

and define \(n_F,s_F\) similarly. Retain

\[
 \begin{aligned}
 m_N(E,F;Q)&=|((E\cap F)-Q)\cap
                  (\mathcal L\mathbin{\dot\cup}\mathcal R)|,\\
 m_S(E,F)&=|(E\cap F)\cap([k]\times[L])|,\\
 u_N(E,F;Q)&=|((E\cup F)-Q)\cap
                  (\mathcal L\mathbin{\dot\cup}\mathcal R)|,\\
 u_S(E,F)&=|(E\cup F)\cap([k]\times[L])|.
 \end{aligned}
\tag{1.2}
\]

Then

\[
 n_E+n_F=u_N+m_N,
 \qquad s_E+s_F=u_S+m_S.
\tag{1.3}
\]

Write

\[
 r_i={p_i\over p_*},\qquad r_{s,i}={p_{s,i}\over p_{s,*}},
 \qquad \rho_i={p_{i+1}\over p_i},\qquad
 \rho_{s,i}={p_{s,i+1}\over p_{s,i}}.
\tag{1.4}
\]

The coefficient of \((Q,E,F)\) in the hypothetical next pair potential is

\[
 \mu_i(Q,E,F)=c_i(Q,E,F)R_i(E,F;Q).
\tag{1.5}
\]

### Proposition 1.1 (exact future-overlap Gram coefficient)

Put

\[
 b_{E,i}=\xi_{E,i}\rho_i^{-n_E}\rho_{s,i}^{-s_E}.
\tag{1.6}
\]

Then

\[
 \boxed{
 \mu_i(Q,E,F)=b_{E,i}b_{F,i}
 \left({p_{i+1}\over p_*}\right)^{m_N(E,F;Q)}
 \left({p_{s,i+1}\over p_{s,*}}\right)^{m_S(E,F)}.}
\tag{1.7}
\]

This identity includes the two slot fugacities exactly.

#### Proof

By (FP2) and (FP4),

\[
 \mu_i=\xi_E\xi_F r_i^{m_N}r_{s,i}^{m_S}
        \rho_i^{-u_N}\rho_{s,i}^{-u_S}.
\]

Use (1.3) to write

\[
 \rho_i^{-u_N}=\rho_i^{-n_E}\rho_i^{-n_F}\rho_i^{m_N},
 \qquad
 \rho_{s,i}^{-u_S}=\rho_{s,i}^{-s_E}\rho_{s,i}^{-s_F}
                         \rho_{s,i}^{m_S}.
\]

Now \(r_i\rho_i=p_{i+1}/p_*\), and similarly on the slot shore.
Substitution proves (1.7). \(\square\)

The same calculation applies after one more deterministic survivor
multiplier. More precisely, within a fixed accepted-macro stratum, the
literal product \(\mu_i(A)t_A\) is the hypothetical next coefficient of
the same pair row. Repeating Proposition 1.1 with the next deterministic
density replaces \(b_{E,i}\) and the two kernel parameters by their next
values. Thus the \(t_A\) appearing in the conditioned linear-hit
coefficient does not destroy the factorization. A finite mixture of
accepted-macro strata is handled by a finite direct sum.

## 2. Positivity, including slots and stopped deletions

For \(a,b\ge1\), define

\[
 K_Q^{a,b}(E,F)=a^{m_N(E,F;Q)}b^{m_S(E,F)}.
\tag{2.1}
\]

### Proposition 2.1 (Schur-product positivity)

The matrix \(K_Q^{a,b}\), indexed by atomic edges through \(Q\), is
positive semidefinite. It has a Gram representation

\[
                         K_Q^{a,b}(E,F)
          =\langle\Phi_Q(E),\Phi_Q(F)\rangle.
\tag{2.2}
\]

Consequently, the matrix \((\mu_i(Q,E,F))_{E,F}\) is positive
semidefinite.

#### Proof

For a non-slot resource \(u\notin Q\), the two-dimensional feature

\[
                         \phi_u(E)=(1,\sqrt{a-1}\,{\bf1}_{\{u\in E\}})
\]

has inner product

\[
 \langle\phi_u(E),\phi_u(F)\rangle
       =1+(a-1){\bf1}_{\{u\in E\cap F\}}.
\]

Use the analogous feature with \(b\) for every slot, and take their tensor
product. The product of the coordinate inner products is exactly (2.1).
This proves (2.2). Equation (1.7) is a nonnegative diagonal congruence of
this Gram matrix. \(\square\)

This remains exact in a stopped state. An unavailable atomic edge has
\(b_{E,i}=0\); deleting atomic rows is therefore a principal compression
followed by a nonnegative diagonal congruence. The deterministic density
update only changes \(a,b\ge1\). Hence stopping creates no algebraic
remainder in the Gram factorization itself.

## 3. Finite mark-role expansion

For the composite row \(A=(Q,E,F)\), output and blocker incidences are
unions of the two constituent incidences. For a Boolean incidence write

\[
 {\bf1}_{\{x\in E\cup F\}}
 =e_x+f_x-e_xf_x,
 \qquad e_x={\bf1}_{\{x\in E\}},\quad
        f_x={\bf1}_{\{x\in F\}}.
\tag{3.1}
\]

The same formula applies to the blocker support, after using its correct
resource type and omitting a distinguished root when required. Thus
\(z_A(x)\chi_A(y)\) is an exact signed sum of at most nine monomials. Each
monomial assigns the mark \(x\) to \(E\), \(F\), or both, and independently
assigns \(y\) to \(E\), \(F\), or both. Root and slot incidences give the
same finite list with their own feature coordinates.

For a finite marked set \(S\), define

\[
 U_{Q,S}=\sum_{E\supseteq Q}b_{E,i}
        {\bf1}_{\{S\subseteq E\}}\Phi_Q(E).
\tag{3.2}
\]

Empty \(S\) is allowed. Every one of the nine monomials in (3.1) has the
form

\[
                         \langle U_{Q,S},U_{Q,T}\rangle,
\tag{3.3}
\]

where \(S,T\subseteq\{x,y\}\). Its total number of distinct marks is at
most two. Summing over \(Q\) is the same identity in the direct-sum
Hilbert space \(\bigoplus_Q\mathcal H_Q\). Summing the finitely many pair,
root, and accepted-macro strata is another finite direct sum.

Equation (3.3) is the exact point at which a termwise expansion into four
atomic macros is avoidable.

## 4. Bessel reduction of an angular difference

Let a stabilizer transposition \(\tau\) fix the output \(x\) and exchange
the blocker states \(y,z\). Consider first one monomial (3.3).

If the blocker mark occurs only on the left feature, then

\[
 \begin{aligned}
 &\langle U_{Q,S\cup\{y\}},U_{Q,T}\rangle
  -\langle U_{Q,S\cup\{z\}},U_{Q,T}\rangle\\
 &\qquad=\langle U_{Q,S\cup\{y\}}-U_{Q,S\cup\{z\}},
                    U_{Q,T}\rangle.
 \end{aligned}
\tag{4.1}
\]

Therefore

\[
 \boxed{
 |\Delta_{y,z}|^2\le
 \|U_{Q,S\cup\{y\}}-U_{Q,S\cup\{z\}}\|^2
 \|U_{Q,T}\|^2.}
\tag{4.2}
\]

If \(y\) occurs on both features, insert and subtract the mixed term:

\[
 \begin{aligned}
 &\langle U_{S,y},U_{T,y}\rangle
       -\langle U_{S,z},U_{T,z}\rangle\\
 &\quad=\langle U_{S,y}-U_{S,z},U_{T,y}\rangle
       +\langle U_{S,z},U_{T,y}-U_{T,z}\rangle.
 \end{aligned}
\tag{4.3}
\]

Bessel and \((a+b)^2\le2a^2+2b^2\) bound (4.3) by two products of the form
in (4.2). Applying this to the nine monomials and then using finite
Cauchy--Schwarz gives the following.

### Theorem 4.1 (atomic marked Bessel aperture)

For every literal output/blocker type and every stabilizer generator,

\[
 \boxed{
 |\lambda_{x,y}-\lambda_{x,z}|^2
 \le C\sum_{\rho\in\mathfrak R}
       \mathcal N_{\rho}(x;y,z)\,
       \mathcal D_{\rho}(x;y,z),}
\tag{4.4}
\]

where \(|\mathfrak R|=O(1)\), and every factor is one of

\[
 \begin{aligned}
 \mathcal N_\rho&=\|U_{Q,S}\|^2,\\
 \mathcal D_\rho&=
   \|U_{Q,T\cup\{y\}}-U_{Q,T\cup\{z\}}\|^2,
 \end{aligned}
\tag{4.5}
\]

in a finite direct sum over \(Q\) and macro strata. Every \(S,T\) has
size at most two. No norm in (4.5) contains four independently marked
atomic macros.

The unsigned version

\[
 \mathcal D_\rho\le
 2\|U_{Q,T\cup\{y\}}\|^2+2\|U_{Q,T\cup\{z\}}\|^2
\tag{4.6}
\]

is always available.

## 5. Identification with existing rooted moments

The norms in (4.5) are exactly the existing product-residual moments,
with no new four-edge kernel:

* \(\|U_{Q,\varnothing}\|^2\) is the unmarked pair/root future-overlap
  moment;
* \(\|U_{Q,\{x\}}\|^2\) is a one-entry rooted collision moment;
* \(\|U_{Q,\{x,y\}}\|^2\) is a finite role pattern of the marked size-two
  normalization in Proposition 6.2 of the joint root--pair note when
  \(x,y\) are marked owner occurrences;
* lower, owner-root, and slot versions are the corresponding rooted
  collision and slot ledgers already separated in (ROc)/(FE3).

In particular, the split-side rectangle

\[
 \sum_{E,F}b_Eb_FK_Q(E,F)
             {\bf1}_{\{x\in E\}}{\bf1}_{\{y\in F\}}
 =\langle U_{Q,\{x\}},U_{Q,\{y\}}\rangle
\tag{5.1}
\]

is controlled by the two diagonal one-mark norms. It does not require a
separate positive normalization of all four atomic macros obtained by
squaring (5.1). Likewise a same-side rectangle is an inner product of an
unmarked feature with a two-mark feature.

This proves the algebraic part of the proposed BIMARK4 escape.

## 6. What happens under killing

There are two different statements.

1. **Pointwise coefficient factorization.** This survives killing
   exactly, by Proposition 2.1. No boundary correction appears.
2. **A future potential for the marked difference.** The quantity

   \[
    \|U_{Q,T\cup\{y\}}-U_{Q,T\cup\{z\}}\|^2
   \tag{6.1}
   \]

   is not monotone under deletion. Removing one feature can destroy a
   negative cross term and increase (6.1). Thus retaining the conjugate
   difference moves the stopped-boundary problem to an atomic marked
   difference, but does not make it disappear.

If instead (4.6) is used, every resulting norm has nonnegative feature
coefficients and a kernel with nonnegative entries. At fixed density it
can only decrease when atomic edges are deleted. The predictable density
rescaling is already the ordinary future-overlap drift. This removes the
stopped-boundary issue at the price of discarding the conjugate
cancellation.

Hence the exact remaining fork is:

\[
 \boxed{
 \begin{array}{ll}
 \text{signed route:}&
 \text{price the atomic marked-difference birth/service;}\\[1mm]
 \text{positive route:}&
 \text{prove that the sum of the positive one-/two-mark norms in (4.6)}\\
 &\text{has the spare aggregate }d\text{-scale required by ANG4.}
 \end{array}}
\tag{6.2}
\]

The positive route is now a product of already normalized quadratic
moments, but Proposition 6.2 by itself only bounds each normalized moment.
It does not automatically prove the required weighted product sum over
all outputs, blocker-shell edges, roots, and stopping times.

## 7. Smallest remaining quantitative row

Let \(\mathfrak E_x\) denote the normalized stabilizer-shell generator
edges used in \(\operatorname {Ang}_x\). Theorem 4.1 reduces ANG4 to
finitely many sums

\[
 \boxed{
 \mathbb E\sum_{i<\tau}{d^2\over X_i}
  \sum_x{1\over c_x}
  \sum_{(y,z)\in\mathfrak E_x}
       \mathcal N_{\rho,i}(x;y,z)
       \mathcal D_{\rho,i}(x;y,z).}
\tag{ABESSEL}
\]

All factors in (ABESSEL) are degree-two atomic future moments with at
most two marks. A sufficient closure is either:

* a marked capacity bound on \(\mathcal N_\rho/c_x\), followed by an
  occupation/Dirichlet bound on \(\sum\mathcal D_\rho\); or
* the positive polarization (4.6), followed by a Carleson estimate for
  products of the marked norms.

The existing rooted collision and Proposition 6.2 estimates are exactly
the local normalizations needed in either proof. What is not checked in
the present note is the final stopped aggregate coefficient in
(ABESSEL). Therefore this note removes a bespoke four-macro marked
normalization from the frontier, but does not by itself prove ANG4 or the
additive-constant theorem.

## 8. Static marked normalization alone does not imply (ABESSEL)

There is a minimal Gram-level obstruction. Take one root \(Q\), one
available atomic completion \(E_0\), and the rank-one kernel

\[
                         K(E_0,E_0)=1.
\tag{8.1}
\]

Let \(E_0\) carry the output mark \(x\) and blocker mark \(y\), but not the
shell neighbour \(z\). Give its feature coefficient value one. Then

\[
 \lambda_{x,y}=1,\qquad \lambda_{x,z}=0,
\tag{8.2}
\]

and the Bessel factors are

\[
                         \mathcal N_x=1,\qquad
                         \mathcal D_{y,z}=1.
\tag{8.3}
\]

Every unmarked, one-mark, and two-mark Gram norm in this example is at
most one. Thus it satisfies a dimension-free statement of the form
\(\Gamma_A=O(1)\), but its angular energy has no inverse power of \(d\).
Disjoint auxiliary rows can supply the ordinary one-resource reference
loads without changing (8.2).

This does not assert that the one-row fibre has appreciable probability in
the authenticated process. It proves the logical boundary:

\[
 \boxed{\text{cluster-rooted normalization without a relative capacity
 or stopped occupation estimate does not imply (ABESSEL).}}
\tag{8.4}
\]

The example is the atomic-feature version of the stopped point-mass
obstruction in Section 5.2 of the stabilizer-shell note.

## 9. A modular capacity/occupation tradeoff

For each of the finitely many Bessel roles, suppose there are predictable
weights \(\pi_{\rho,x}\ge0\), with

\[
                         \sum_\rho\pi_{\rho,x}\le C,
\tag{9.1}
\]

and fix \(0\le\alpha\le2\). Suppose

\[
 \boxed{
 \mathcal N_{\rho,i}(x;y,z)
 \le {C\over d^\alpha}c_x\,\pi_{\rho,x}.}
\tag{MCAP-alpha}
\]

Suppose also that the marked atomic difference has the occupation bound

\[
 \boxed{
 \mathbb E\sum_{i<\tau}{1\over X_i}
 \sum_{x,\rho}\pi_{\rho,x}
 \sum_{(y,z)\in\mathfrak E_x}
       \mathcal D_{\rho,i}(x;y,z)
 \le {C\over d^{2-\alpha}}\mathsf A.}
\tag{MDIR-alpha}
\]

Then Theorem 4.1 gives

\[
 \begin{aligned}
 &\mathbb E\sum_{i<\tau}{d^2\over X_i}
 \sum_x{1\over c_x}
 \sum_{(y,z)\in\mathfrak E_x}
 |\lambda_{x,y}-\lambda_{x,z}|^2\\
 &\qquad\le
 Cd^{2-\alpha}\mathbb E\sum_{i<\tau}{1\over X_i}
 \sum_{x,\rho}\pi_{\rho,x}
 \sum_{(y,z)\in\mathfrak E_x}\mathcal D_{\rho,i}
 \le C'\mathsf A.
 \end{aligned}
\tag{9.2}
\]

Thus (MCAP-alpha)+(MDIR-alpha) proves ANG4. The shell/covariance aperture
requires a total gain \(d^{-2}\), but that gain may be divided arbitrarily
between a relative capacity cap and marked-difference occupation.

The intended interpretation is:

* (MCAP-alpha) is a **relative common-mark cap**.
* (MDIR-alpha) is a stopped occupation estimate for a one- or two-mark
  atomic load difference. It is lower-degree than the original composite
  star and is the natural marked analogue of the root-variance future
  potential.

Two allocations are especially relevant.

1. The typical residual pair scale suggests \(\alpha=2\), with an
   \(O(\mathsf A)\) occupation estimate.
2. The actual analytical pair stop only enforces a relative
   \(O(d^{-1})\) cap. It corresponds to \(\alpha=1\), and must be combined
   with the spare \(O(d^{-1})\) marked first-entry/occupation scale. This
   is the allocation aligned with the present stopped architecture.

Proposition 6.2 supplies the static normalization for the marked
difference and Proposition 7.1 supplies a \(d^{-1}\) first-two-hit gain.
They do not by themselves identify the literal occupation sum in
(MDIR-alpha). What is not yet proved is that the two estimates hold
simultaneously for every occurrence-labelled role used by the stopped
composite row, with their stated aggregate quantifiers. In particular, the
current pair stop tests selected compatible carrier relations, whereas
(MCAP-alpha) ranges over every role entering the analytic composite star.
A uniform pointwise cap over all abstract marks would be stronger than
necessary; an averaged Carleson form of (MCAP-alpha) is sufficient.

## 10. Audit against the existing pair stop and first-two-hit theorem

The authoritative analytical pair stop in (7.2) of the
rank-compensated-doublet note is

\[
 {Y_{v,w}\over\min(Y_v,Y_w)}\le{\gamma\over d}
\tag{10.1}
\]

for every **tested selected-compatible carrier pair** \(\{v,w\}\in
\mathcal P\), up to its local bad time. The authoritative marked
first-two-hit statement, Proposition 7.1 of the joint root--pair note, is

\[
 \mathcal F_{3,A}(p_*)\le {C\over d}D_A^2\Gamma_A(p_*)
\tag{10.2}
\]

for a fixed compatible marked cluster \(A\) of size two or three.

These have the two powers suggested by the \(\alpha=1\) allocation, but
their literal indices do not equal (MCAP-alpha) and (MDIR-alpha).

### 10.1 The capacity row is a kernel-tilted third incidence

For fixed \(Q,E,x\), define

\[
 \pi_{Q,E}(x)=
 {\sum_{F\supseteq Q\cup\{x\}}b_FK_Q(E,F)
  \over
  \sum_{F\supseteq Q}b_FK_Q(E,F)}.
\tag{10.3}
\]

For one constituent-role split, put

\[
 \begin{aligned}
 N_{Q,x}&=\sum_{E,F\supseteq Q}
 b_Eb_FK_Q(E,F){\bf1}_{\{x\in E\cap F\}},\\
 C_{Q,x}&=\sum_{E,F\supseteq Q}
 b_Eb_FK_Q(E,F){\bf1}_{\{x\in E\}}.
 \end{aligned}
\tag{10.4}
\]

Then \(N_{Q,x}/C_{Q,x}\) is the \(C_{Q,x}\)-weighted average of
\(\pi_{Q,E}(x)\) over \(E\supseteq Q\cup\{x\}\). Consequently,

\[
 \sup_{E\supseteq Q\cup\{x\}}\pi_{Q,E}(x)\le{\gamma\over d}
 \quad\Longrightarrow\quad
 N_{Q,x}\le{\gamma\over d}C_{Q,x}.
\tag{10.5}
\]

Equation (10.5), or its weighted average over \(Q,E,x\), is the literal
capacity statement required by the split-side Bessel term. It is a
future-overlap-kernel-tilted **third** incidence \(Q+x\). In contrast,
(10.1) is an un-tilted current two-resource rate statement for a tested
pair. It does not quantify over an arbitrary output \(x\), and it does
not condition on the first atomic completion \(E\).

### Proposition 10.1 (the pair stop does not imply the Bessel cap)

There is a positive product-overlap kernel and a weighted atomic fibre
which satisfies the scalar pair ratio (10.1) but has

\[
                         {N_{Q,x}\over
                          2C_{Q,x}-N_{Q,x}}=1-o(1).
\tag{10.6}
\]

#### Proof

Take one exceptional completion \(H\supseteq Q\cup\{x\}\) of weight
\(\epsilon=d^{-1}\), and a bank of completions through \(Q\), but not
\(x\), of total weight one. Arrange that every bank member has no
non-root overlap with \(H\). Let

\[
                         K_Q(H,H)=R,\qquad
                         K_Q(H,J)=1
\tag{10.7}
\]

for every bank member \(J\), where \(R\ge d^3\). This is a literal
product-overlap pattern: take \(a>1\), let \(H\) have \(m\) private
non-root resources, choose \(a^m=R\), and make the other completions
disjoint from those resources.

The raw marked share is at most

\[
                         {\epsilon\over1+\epsilon}\le d^{-1},
\]

so the analogue of (10.1) passes. But

\[
 N_{Q,x}=\epsilon^2R,\qquad
 C_{Q,x}=\epsilon^2R+\epsilon,
\tag{10.8}
\]

and the union-incidence coefficient is
\(2C_{Q,x}-N_{Q,x}\). Since \(\epsilon^2R\ge d\), (10.6) follows.
\(\square\)

This is a quantifier counterexample, not a claim that the complete
authenticated FIFO orbit has such an appreciable fibre. It proves that
mapping (10.1) to (MCAP-alpha) requires the rooted-overlap/first-entry
geometry or a new kernel-tilted capacity stop; the scalar selected-pair
stop alone is insufficient. The mismatch persists even if ordinary
one-resource loads are repaired by disjoint rows.

### 10.2 First-two-hit injection is not marked-difference occupation

The term in (10.2) is indexed by a selected edge \(G\) carrying two
distinct hits in \(E\cup F\). The difference norm in (MDIR-alpha) is
already present after a **one-sided first kill**:

\[
 \|U_{Q,T\cup\{y\}}-U_{Q,T\cup\{z\}}\|^2.
\tag{10.9}
\]

A transition may kill the \(y\)-feature and miss the \(z\)-feature with
only one relevant incidence. Such a transition contributes zero to the
binomial factor \(\binom{j(G;E,F)}2\) in (10.2), but it can create a
nonzero value of (10.9). If subsequent accepted edges avoid the surviving
feature for many steps, (10.9) has positive occupation although the
corresponding first-two-hit ledger remains zero.

Thus Proposition 7.1 supplies the correct scale for correlated
multi-hit **injection**, but it is not a literal map to
(MDIR-alpha). To obtain the \(d^{-1}\) occupation gain one still needs the
one-mark future-service drift, including the coefficient of one-sided
births and the stopped difference boundary. This is exactly the signed
atomic route in (6.2).

### Corollary 10.2 (proof-safe status of the \(\alpha=1\) attempt)

Neither half of the proposed identification is automatic:

1. (MCAP1) requires a kernel-tilted rooted third-incidence estimate such
   as (10.5), averaged over every analytic occurrence role; and
2. (MDIR1) requires a one-hit marked-difference birth/service theorem, not
   merely the two-hit static injection (10.2).

Accordingly the existing selected-pair stop plus Proposition 7.1 do not
yet prove ANG4. They locate its expected \(d^{-1}\times d^{-1}\) scale,
but a literal stopped occurrence-level transfer remains substantive.
