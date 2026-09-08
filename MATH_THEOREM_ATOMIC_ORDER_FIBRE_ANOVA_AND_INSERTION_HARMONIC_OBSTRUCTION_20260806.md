# Atomic order-fibre ANOVA and the shared-insertion harmonic obstruction

**Date:** 2026-08-06  
**Method:** exact product-permutohedron conditioning and a coordinate-star
test on the authenticated fresh FIFO formula; no computation or search  
**Status:** proof-safe host specialization.  The private-order generator
does not have the strong candidate-space lumpability required by the
killed Green identity.  The obstruction is an explicit shared-insertion
mode living on the whole interior of one macro side.  Adding adjacent
insertion switches removes it from the kernel, but does not remove the
range-intertwining defect: the mode is affine in insertion position and is
harmonic at every interior position.  The corrected residual is a killed
insertion-position observability row, not a finite endpoint/mark table.

This note specializes
`MATH_THEOREM_KILLED_PRIVATE_SWITCH_GREEN_IDENTITY_AND_COMPONENT_OBSTRUCTION_20260806.md`
to the fresh FIFO block in
`MATH_THEOREM_FRESH_FIFO_BLOCK_CHAIN_KERNEL_AND_PAYLOAD_ATLAS_GATE_20260805.md`
and its punctured duplicate lift.

## 1. The conditional order fibre

Fix all endpoint banks and all exterior/port data of one fresh `h`-fold
macro, where `h in {2,3}`.  Away from the separately priced terminal fan,
the literal states have the form

\[
 \begin{aligned}
 S_j&=C\cup\{a_{j+1},\ldots,a_d\}
          \cup\{b_1,\ldots,b_j\},\\
 T_j^c&=C\cup A\cup\{x_{j+1}^c,\ldots,x_d^c\}
          \cup\{b_1,\ldots,b_j\},
 \end{aligned}
 \qquad 0\le j<d.
\tag{1.1}
\]

The order variables are

\[
 \alpha=(a_1,\ldots,a_d),\qquad
 \beta=(b_1,\ldots,b_{d-1}),\qquad
 \xi_c=(x_1^c,\ldots,x_d^c).
\tag{1.2}
\]

The final inserted label is private to copy `c`; it affects only the
already isolated terminal role.  Conditional on the fixed endpoint banks,
the complete order fibre carries the product law

\[
 \mathfrak S_d(\alpha)\times
 \mathfrak S_{d-1}(\beta)\times
 \prod_{c=1}^h\mathfrak S_d(\xi_c).
\tag{1.3}
\]

Let `g=K_Tf` be one generic, collision-free macro-side score on a fixed
resource layer `T`.  Rooted/common collisions are excluded here because
they belong to the existing `(ROc)`/`(FE3)` faces.  Formula (1.1) gives

\[
 \boxed{
 g(\alpha,\beta,\xi_1,\ldots,\xi_h)
 =g_L(\alpha,\beta)
   +\sum_{c=1}^h g_c(\beta,\xi_c)+g_{\rm ext}.}
\tag{1.4}
\]

The constant exterior term includes the other macroscopically separated
half and the fixed distinguished-root convention.  On a generic face it
does not alter the order dependence in (1.4).

### Theorem 1.1 (exact order-fibre Hoeffding support)

Under the product law (1.3), the conditional Hoeffding decomposition of
`g` has support only on

\[
 \boxed{
 \varnothing,\quad
 \alpha,\quad\beta,\quad\alpha\beta,
 \quad\xi_c,\quad\beta\xi_c\ (1\le c\le h).}
\tag{1.5}
\]

In particular, there are no `xi_c xi_c'` interactions and no interaction
involving three order banks.

#### Proof

Apply the standard product conditional-expectation expansion separately
to the two-variable function `g_L(alpha,beta)` and to each two-variable
function `g_c(beta,xi_c)`.  A function of two coordinates has only its
constant, two main, and one two-coordinate interaction terms.  Summing
the expansions gives exactly (1.5).  Orthogonality is the ordinary
Hoeffding orthogonality under the product measure.  \(\square\)

This is the exact ANOVA reduction available from the complete order fibre.
It does not say that the candidate resolvent intertwines these summands.

## 2. What deletion-only private switches miss

Let

\[
 \Lambda_{\rm del}
 =\Lambda_\alpha+\sum_{c=1}^h\Lambda_{\xi_c}
\tag{2.1}
\]

be the adjacent-transposition generator used by the private deletion/tail
switch proposal.  Its invariant sigma-field contains the entire shared
insertion order `beta`.  Hence

\[
 \ker\Lambda_{\rm del}
 \supseteq\{F(\beta):F\text{ arbitrary}\}.
\tag{2.2}
\]

The inclusion is strict only because fixed endpoint and exterior data are
also invariant; the displayed insertion-order space is the relevant new
part.

There is a literal slow mode in (2.2).  On a rank-`q` resource layer put

\[
 f_z^{(q)}(S)={\bf1}_{\{z\in S\}}-{q\over k}.
\tag{2.3}
\]

This is the standard sector-one coordinate-star vector.  Choose
`z in B`, and let `ell=ell_beta(z)` be its position in the shared
insertion order.

For the `d` common lower resources `S_0,...,S_(d-1)`,

\[
 \boxed{
 \sum_{j=0}^{d-1}f_z^{(t)}(S_j)
 =(d-\ell)-{dt\over k}.}
\tag{2.4}

For the complete owner words of the `h` copies, including the terminal
owner,

\[
 \boxed{
 \sum_{c=1}^h\sum_{j=0}^{d}f_z^{(r)}(T_j^c)
 =h\left(d-\ell+1-{(d+1)r\over k}\right).}
\tag{2.5}

Both expressions are independent of every deletion/tail order and are
nonconstant affine functions of `ell`.

### Proposition 2.1 (literal shared-insertion kernel obstruction)

On either the lower side (2.4) or owner side (2.5), the deletion-only
private generator annihilates a nonzero `Theta(d)`-amplitude interior
macro-side score.  Consequently its candidate component charge is not
supported only on endpoints, marks, or terminal fans.

#### Proof

The membership of `z` in (1.1) changes from zero to one precisely when
`j` reaches `ell`.  Counting the roles after that event gives (2.4) and
(2.5).  Neither count uses `alpha` or any `xi_c`, so (2.1) annihilates it.
As `ell` ranges over the `d-1` shared insertion positions, the centered
value has range `Theta(d)`.  Removing or adjoining constantly many
distinguished endpoint roles changes it by only `O(1)` and cannot erase
the interior affine mode.  \(\square\)

Thus the candidate-fibre defect from the killed Green identity is present
in the authenticated atomic normal form.  It is not merely an abstract
possibility.

## 3. Adding the shared insertion permutohedron is still not lumpable

The natural repair is the full order generator

\[
 \Lambda_{\rm ord}
 =\Lambda_\alpha+\Lambda_\beta+
   \sum_{c=1}^h\Lambda_{\xi_c},
\tag{3.1}
\]

where every factor is the equal-weight adjacent-transposition Laplacian.
Its invariant functions on a fixed endpoint fibre are constants.  Hence
the only kernel obstruction is the endpoint/exterior conditional mean.

But strong lumpability requires more than removal of the kernel.  Recall
the condition

\[
 MK=\Lambda_{\rm ord}KR.
\tag{3.2}
\]

from the killed Green identity.  It fails on the same coordinate-star
mode.

Let

\[
 \phi(\ell)=A-B\ell,
 \qquad B\ne0,
\tag{3.3}
\]

be either affine function (2.4) or (2.5), after absorbing constants into
`A`.  If `1<ell<d-1`, exactly two adjacent insertion transpositions move
`z`, one to `ell-1` and one to `ell+1`.  Every other adjacent
transposition fixes `phi`.  Therefore

\[
 \boxed{
 (\Lambda_\beta\phi)(\ell)
 =2\phi(\ell)-\phi(\ell-1)-\phi(\ell+1)=0
 \quad(1<\ell<d-1).}
\tag{3.4}

Only the two extreme insertion positions carry its Laplacian.

The pristine resource operators are Johnson invariant.  Hence the
sector-one vector (2.3) is a common eigenvector and

\[
 Rf_z^{(q)}=\rho_{q,1}f_z^{(q)}
\tag{3.5}

for its resolvent eigenvalue `rho_(q,1)`.  On every FIFO side with nonzero
sector-one covariance this eigenvalue is positive; the coordinate-star
calculation in the joint-Lyapunov note is exactly such a side.

### Theorem 3.1 (interior harmonic obstruction to strong lumpability)

For every interior insertion position `ell` at which `phi(ell) ne 0`,

\[
 (\Lambda_{\rm ord}KRf_z)(\ell)=0,
 \qquad
 (MKf_z)(\ell)=m\phi(\ell)\ne0,
\tag{3.6}

where `m>0` is the constant candidate mass on the order fibre.  Thus

\[
 \boxed{MK\ne\Lambda_{\rm ord}KR.}
\tag{3.7}

Moreover the defect occurs on `Theta(d)` interior positions, not on a
bounded endpoint or mark set.

#### Proof

The score depends only on `beta`, so every generator factor in (3.1)
except `Lambda_beta` annihilates it.  Equations (3.4)--(3.5) give the first
identity in (3.6).  Candidate mass is constant and positive on the
complete order orbit, so the second identity follows.  An affine
nonconstant function has at most one zero, leaving `Theta(d)` nonzero
interior positions.  \(\square\)

This theorem rules out the hoped-for conclusion that complete-order ANOVA
makes the intertwining defect an endpoint/mark term.  ANOVA identifies the
order coordinates; it does not turn the local adjacent-swap generator into
the FIFO covariance operator.

The loss is quantitatively sharp.  Put `n=d-1` and center the affine
position function as

\[
 \psi(\ell)=B\left(\ell-{n+1\over2}\right),
 \qquad 1\le\ell\le n.
\tag{3.8}
\]

Under a uniform permutation, the position of `z` is uniform, and hence

\[
 \mathbb E\psi^2={B^2(n^2-1)\over12}.
\tag{3.9}
\]

For the unnormalized adjacent-transposition Laplacian

\[
 (\Delta_{\rm adj}F)(\pi)
 =\sum_{q=1}^{n-1}(F(\pi)-F(\pi\tau_q)),
\tag{3.10}
\]

only the one or two transpositions adjacent to `z` change `psi`.  Therefore

\[
 \langle\psi,\Delta_{\rm adj}\psi\rangle
 ={1\over2}\mathbb E_\pi\sum_{q=1}^{n-1}
   (\psi(\pi)-\psi(\pi\tau_q))^2
 ={n-1\over n}B^2.
\tag{3.11}
\]

Consequently

\[
 \boxed{
 {\mathbb E\psi^2
  \over\langle\psi,\Delta_{\rm adj}\psi\rangle}
 ={n(n+1)\over12}=\Theta(d^2).}
\tag{3.12}
\]

Thus a scalar Poincare repair of the insertion mode necessarily loses a
quadratic factor.  Any successful argument must recover that factor from
the killing hazard, a nonlocal flow, or an exactly matched future
potential; changing constants in the adjacent generator cannot remove it.

There is a support--gap tradeoff which shows that this is not peculiar to
adjacent transpositions.  Let `mathcal Q` be any reversible insertion-order
generator, normalized so that its total outgoing rate at every permutation
is at most one.  Suppose every allowed move changes the position of every
label by at most `s`.  For the same affine witness,

\[
 \mathcal E_{\mathcal Q}(\psi,\psi)
 ={1\over2}\mathbb E_\pi
   \sum_{\pi'}q(\pi,\pi')
       (\psi(\pi)-\psi(\pi'))^2
 \le {B^2s^2\over2}.
\tag{3.13}
\]

Combining this with (3.9) gives

\[
 \boxed{
 {\mathbb E\psi^2\over
       \mathcal E_{\mathcal Q}(\psi,\psi)}
 \ge {n^2-1\over6s^2}.}
\tag{3.14}
\]

In a prefix FIFO word, moving an insertion label by `s` positions changes
its membership in at least `s` consecutive lower states and in the
parallel owner states.  Hence a switch changing at most `m` literal word
occurrences has `s<=m`.  Every constant-support order generator therefore
has an `Omega(d^2)` insertion-position relaxation cost after bounded-rate
normalization.  A bounded-support generator cannot remove the harmonic
row by a different choice of local moves.

## 4. Physical meaning of the insertion generator

An adjacent transposition in `beta` changes exactly one lower state and
the parallel owner state in each of the `h` copies.  Hence one insertion
edge changes at most

\[
 1+h\le4
\tag{4.1}

literal resource occurrences in one macro.  This is still a constant-size
physical move, unlike a global coordinate transposition, which can change
`Theta(d)` occurrences.

The constant support is useful for first-hit enumeration, but it does not
by itself bound the bilinear edge term

\[
 (g_a-g_b)(h_a-h_b),
 \qquad h=KRf.
\tag{4.2}

Expanding (4.2) gives at most `(h+1)^2` products

\[
 \langle b_p,f\rangle\langle b_q,Rf\rangle,
\tag{4.3}

where each `b_p` is a Johnson-edge incidence of one changed occurrence.
The bounded number of occurrence labels is compatible with the rooted
size-two/size-three ledgers.  The resolvent-weighted second factor in
(4.3), however, is not one of those ledgers until a coefficient-faithful
flow or Bellman comparison is supplied.

## 5. The weakest remaining host-specific row

Let `P_0` be conditional expectation over the entire order fibre, with
endpoint/exterior data fixed, and let `P_beta` denote the centered main
effect of the shared insertion order in the Hoeffding decomposition
(1.5).  Write

\[
 P_{\rm loc}=I-P_0-P_\beta.
\tag{5.1}

The already proposed deletion/tail private switches act only on
`P_loc`.  Theorems 2.1 and 3.1 prove that neither `P_0` nor `P_beta` may be
discarded.

A strictly weaker sufficient replacement for full strong lumpability is
the following three-row statement, with the actual future-fugacity
coefficients and after the authenticated static injections have been
subtracted.

1. **Endpoint row.**  The cumulative killed Green form involving `P_0`
   is bounded by the existing pair/root future potential.
2. **Insertion-position row.**  The cumulative killed Green form in which
   at least one factor is `P_beta` is `O(M/d^4)`.
3. **Local-order row.**  The cumulative form on `P_loc` is paid by the
   private deletion/tail first-hit ledger.

More explicitly, row 2 is the insertion-position observability estimate

\[
 \boxed{
 \begin{aligned}
 \mathbb E\sum_i {\beta_i\over X_i}
 \Bigg[
 &\langle P_{U_i}P_\beta Kf_i,
          P_{U_i}\mathcal H_i f_i\rangle\\
 &+\sum_{\substack{a\in U_i,b\notin U_i\\a\sim_\beta b}}
 w_{ab}\,(P_\beta g_i)_a(h_{i,a}-h_{i,b})
 \Bigg]_+
 =O(M/d^4),
 \end{aligned}}
\tag{IPH}
\]

together with the transpose cross terms in which `P_beta` falls on the
`h` factor.  Here `a sim_beta b` means one adjacent shared-insertion
switch.  The endpoint and local-order rows are the analogous projections
of the exact killed Green identity.

There are only

\[
 2h+4\le10
\tag{5.2}

Hoeffding types in (1.5), so expanding every bilinear term by type costs
only an absolute number of rows.  Thus `(IPH)` is not an arbitrary
candidate-space operator norm.  It is a one-dimensional killed
insertion-position Hardy/observability estimate, repeated over endpoint
fibres and the finitely many resource/marked types.

The affine witness (3.3) shows the sharp scale that such a theorem must
see.  An adjacent insertion generator has zero second difference in the
interior, so any proof of `(IPH)` must use at least one of:

* the stopping/killing hazard along the insertion-position chain;
* a nonlocal insertion-order switch represented by a controlled physical
  flow of adjacent switches; or
* an additional future potential for the insertion-position first moment.

Ordinary Poincare control on the adjacent permutohedron loses its slow
one-dimensional factor and is not the desired theorem.

## 6. Self-audit and scope

1. Equations (1.1)--(1.4) are the authenticated fresh FIFO formulas.  The
   punctured terminal convention affects only `O(1)` roles and does not
   alter the affine interior calculation.
2. The ANOVA statement is conditional on fixed endpoint/exterior banks and
   on the generic collision-free face.  Root/common collisions must remain
   in `(ROc)`/`(FE3)`.
3. The coordinate-star vector is a legitimate mean-zero Johnson-layer
   vector.  The positivity of its resolvent eigenvalue is used only on
   resource sides whose sector-one FIFO covariance is nonzero.
4. Theorem 3.1 disproves strong candidate-space lumpability for the
   equal-weight adjacent order generator.  It does not disprove a
   differently supported nonlocal generator or a future-potential payment.
5. Constant physical support (4.1) does not by itself price the
   resolvent-weighted product (4.3); no such claim is made.
6. `(IPH)` is a sufficient target, not a proved estimate.  Therefore this
   note does not establish the raw Bellman value or the bottom cleanup
   theorem.

The bottom analytic gate has consequently narrowed to a recognisable
one-dimensional object:

\[
 \boxed{
 \text{a killed Hardy/observability inequality for the shared insertion
 position, coupled to the actual future relation potential.}}
\]

The previous global `FSW` and the proposed endpoint-only private-switch
closure are both stronger or incorrectly typed formulations of this row.
