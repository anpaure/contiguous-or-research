# Recursive compiler higher-order types: exact \(k\)-enumerator and blind-context flats

Date: 2026-07-26

## 0. Verdict

Let the physical diverse compiler have dimension

\[
                         R=2n,\qquad n=4\cdot2^s,
 \qquad K=2^R,
\]

and let one legal option be an affine conjugate of its complete trace
image.  The option array is not an orthogonal array of growing strength.
Before antipodal fusion it is not even a covering array of strength two,
because a face and its packet antipode have identical incidence columns.
After antipodal fusion, a second and genuinely recursive obstruction
remains.

A physical \(q\)-window visits only

\[
 d_\rho(q)=\left\lfloor{\rho+q-1\over2}\right\rfloor+1
\]

bottom \(Q_4\)-leaves.  Fixing its phase variables \((x,\rho)\), every
even change of the context \(p\) on the unvisited leaves gives another
face in the same compiler image with the same direction support.  Thus
every option contains affine **blind-context flats** of size at least

\[
 2^{u_q-1},\qquad
 u_q=n-4\left(\left\lfloor q/2\right\rfloor+1\right)
      ={R\over2}-2q+O(1).                            \tag{0.1}
\]

This gives degree-scale higher atoms of every fixed order.  If \(D_q\)
is the affine degree of one face, then for every
\(t\le u_q/2\) there are \(t+1\) distinct nonantipodal faces with

\[
 \boxed{
 {d_{t+1}\over D_q}
 \ge{(u_q)_{2t}\over(R-q)_{2t}}
 =4^{-t}\exp\!\left(O\!\left({t(q+t)\over R}\right)\right).}
 \tag{0.2}
\]

For fixed \(t\), the conditional common-option probability is therefore
at least \(4^{-t}-o(1)\).  The independent affine value would be
\(\theta_{R,q}^{,t}\), where

\[
                         \theta_{R,q}={2^q\over\binom Rq}=o(1).
\]

Hence the post-antipode catalogue is not even an approximate orthogonal
array of any fixed strength at least two.  The pair atom \(1/4-o(1)\) is
the first member of an all-order hierarchy, not an isolated defect.

There is nevertheless an exact finite recursion for every higher common-
option enumerator.  Theorem 2.1 below is the \(k\)-start extension of the
existing pair transfer.  Its coefficients give the exact common-option
degree of every proposed \(k\)-target home bundle, with one affine label
shared across all selected depths and signs.  Thus higher realizability is
decidable from the recursive seed, but it is not pseudorandom.

This result refutes the route

\[
 \text{normalized conjugacy + growing-strength OA/codegrees}
 \Longrightarrow\text{rainbow near-cover}.
\]

It does not refute a structured near-cover.  The blind flats may instead
be used as large realizable home bundles, but their physical identity is
packet-dependent.  A global theorem must align these flats between
different parents or verify the exact product-hole criterion directly.

## 1. Higher column types

For \(k\ge1\), take starts

\[
 (p^{(s)},x^{(s)},\rho_s),\qquad 1\le s\le k,
\]

and window lengths \(\ell_s\).  At one physical coordinate, the stacked
column symbol is

\[
 \mathbf u=(u_1,\ldots,u_k)\in\{0,1,*\}^k.          \tag{1.1}
\]

An affine translation exchanges \(0\) and \(1\) simultaneously in every
nonstar entry of this vector; a coordinate permutation permutes the
physical columns.  Consequently the complete affine type of an ordered
\(k\)-tuple is the histogram of the symbols (1.1), modulo this common
column complementation.

This is the exact higher analogue of the pair type \((a,\delta)\).  It
also gives a direct realizability test: a proposed ordered target tuple
has a common compiler option precisely when its column histogram occurs
among the base compiler's ordered row tuples after one physical frame
identification.

## 2. Exact \(k\)-start transfer recursion

Let

\[
 \boldsymbol\kappa=(\kappa_1,\ldots,\kappa_k),
 \qquad
 \mathbf c=(c_1,\ldots,c_k)
\]

record the parities of the \(p\)- and \(x\)-variables.  Introduce an
indeterminate \(Z_{\mathbf u}\) for each stacked physical column symbol
\(\mathbf u\in\{0,1,*\}^k\).  Define

\[
\begin{aligned}
 B_n^{(k)}[\boldsymbol\ell,\boldsymbol\rho,
           \boldsymbol\kappa,\mathbf c](\mathbf Z)
 :=\sum_{\substack{|p^{(s)}|=\kappa_s\\|x^{(s)}|=c_s\ (1\le s\le k)}}
 \prod_{i=1}^{n}\prod_{\sigma\in\{a,b\}}
 Z_{\left(
   \tau^{(n)}_{\ell_s,\rho_s}(p^{(s)},x^{(s)})_{i,\sigma}
          \right)_{s=1}^k}.
                                                               \tag{2.1}
\end{aligned}
\]

Identifying \(Z_{\mathbf u}\) with the variable obtained by exchanging
all \(0/1\) entries in \(\mathbf u\) passes directly to affine column
types.

Suppose \(n=2h\).  For each start \(s\) and child \(j\in\{0,1\}\), let
\((\ell_{s,j},\rho_{s,j})\) be the child window obtained from
\((\ell_s,\rho_s,c_s)\) by the parity-alternating split in the recursive
rotor.

### Theorem 2.1 (exact higher enumerator)

\[
\boxed{
\begin{aligned}
 B_n^{(k)}[\boldsymbol\ell,\boldsymbol\rho,
           \boldsymbol\kappa,\mathbf c]
 =\sum_{\boldsymbol\alpha,\boldsymbol\beta\in\{0,1\}^k}
 &B_h^{(k)}[\boldsymbol\ell_0,\boldsymbol\rho_0,
             \boldsymbol\alpha,\boldsymbol\beta]\\
 {}cdot{}
 &B_h^{(k)}[\boldsymbol\ell_1,\boldsymbol\rho_1,
      \boldsymbol\kappa\oplus\boldsymbol\alpha,
      \mathbf c\oplus\boldsymbol\beta].
\end{aligned}}                                                   \tag{2.2}
\]

The base \(B_4^{(k)}\) is the explicit finite sum obtained from the
audited \(Q_4\) direction table.  In the protected range \(q=o(n)\),
each bottom leaf sees only physical lengths \(0,1,2\), so the five seed
traces already listed in the pair enumerator are sufficient for every
fixed \(k\).

#### Proof

For each of the \(k\) starts, parent moves alternate between the two
children.  Deleting the other child's moves leaves the stated consecutive
child interval.  Write \((\alpha_s,\beta_s)\) for the two left-child
parities.  The right parities are then

\[
                 (\kappa_s\oplus\alpha_s,
                  c_s\oplus\beta_s).
\]

The child coordinate sets are disjoint, so their column-histogram
monomials multiply.  Summing independently over all \(2k\) left parity
bits proves (2.2).  The \(Q_4\) formula follows by direct substitution in
the finite seed table. \(\square\)

At the root, sum (2.1) over \(\rho_s,c_s\) with every
\(\kappa_s=0\).  If distinct rows are required, use ordinary
inclusion--exclusion over the partition lattice of \([k]\); trace
injectivity identifies equality of faces with equality of starts.  The
coefficient of a column histogram \(\mathfrak h\) is then the exact
number

\[
                         A_k(\mathfrak h)            \tag{2.3}
\]

of ordered distinct base-image \(k\)-tuples of that affine type.

If \(M_k(\mathfrak h)\) is the number of ambient ordered \(k\)-tuples of
type \(\mathfrak h\) relative to one fixed first face, affine double
counting gives

\[
 \boxed{
 \Pr_g(f_1,\ldots,f_k\in gI_q)
 ={A_k(\mathfrak h)\over V_{R,q}M_k(\mathfrak h)},
 \qquad
 \Pr_g(f_2,\ldots,f_k\in gI_q\mid f_1\in gI_q)
 ={A_k(\mathfrak h)\over K M_k(\mathfrak h)}.}      \tag{2.4}
\]

For a common all-depth label, replace each entry of (1.1) by its vector
of symbols indexed by \((q,\epsilon)\).  The proof of (2.2) is unchanged.
Thus (2.2), rather than a product of separate-depth enumerators, computes
the exact common-label bundle degree.

## 3. Blind-context flats

Use the physical representation

\[
             (p,x,\rho),\qquad p\in E_n, x\in Q_n,
             \ \rho\in\{0,1\}.
\]

For a fixed \((x,\rho)\), a physical length-\(q\) interval visits
\(d_\rho(q)\) distinct bottom leaves.  Let \(V(x,\rho)\subset[n]\) be
the union of their four coarse context coordinates and put

\[
                         U=[n]\setminus V(x,\rho).
\]

If \(\alpha\in\mathbb F_2^U\) has even weight, then

\[
                  (p,x,\rho)\longmapsto
                  (p\oplus\alpha,x,\rho)             \tag{3.1}
\]

preserves the root parity.  The recursive schedule depends on \(x\), and
every visited leaf sees the same context as before.  Hence the complete
window direction support is unchanged.  The initial physical owners
differ only in the fixed \(b_i\)-coordinates indexed by
\(\operatorname{supp}\alpha\), all outside the support.  Therefore all

\[
 \left\{f_q(p\oplus\alpha,x,\rho):
       \alpha\in E(U)\right\}                       \tag{3.2}
\]

belong to the same compiler image and form an affine even-parity flat of
size \(2^{|U|-1}\).  Since

\[
 |U|=n-4d_\rho(q)\ge u_q,                           \tag{3.3}
\]

this proves (0.1).

The construction is simultaneous for every shorter nested window which
visits a subset of the same leaves.  Thus the flat is a common-label
object, not a separately reselected depth phenomenon.

## 4. All-order codegree atoms

Fix one base face \(f_0=f_q(p,x,\rho)\).  Choose \(t\) ordered disjoint
unordered pairs

\[
              A_s=\{i_s,j_s\}\subseteq U,
              \qquad1\le s\le t,                  \tag{4.1}
\]

and put

\[
              f_s=f_q(p\oplus e_{i_s}\oplus e_{j_s},x,\rho).
                                                               \tag{4.2}
\]

The \(t+1\) faces share one support.  Relative to \(f_0\), face \(f_s\)
differs on exactly its labelled two-set \(A_s\), and those two-sets are
pairwise disjoint.  This affine tuple type is independent of the start.

For a fixed first ambient face, the number of ordered tuples of this type
is

\[
                         M_t={(R-q)_{2t}\over2^t}.   \tag{4.3}
\]

For every base face, (3.3) supplies at least

\[
                         B_t={(u_q)_{2t}\over2^t}    \tag{4.4}
\]

base tuples.  Hence its base enumerator satisfies \(A_{t+1}\ge KB_t\).
Substitution in (2.4) proves (0.2).

For \(q=o(R)\) and \(t=o(R)\),

\[
 \log{(u_q)_{2t}\over(R-q)_{2t}}
 =-2t\log2+O\left({t(q+t)\over R}\right).          \tag{4.5}
\]

The faces in (4.2) are nonantipodal once \(R-q>4\), so the same lower
bound survives the local antipodal contraction.

For \(t=1\), (0.2) recovers the nonantipodal
\((q,2)\) atom \(1/4-o(1)\).  For every fixed \(t\), it gives a
conditional common-option probability bounded away from zero, whereas an
orthogonal option array would give \(\theta_{R,q}^{,t}=o(1)\).

## 5. Consequence for home labels

The exact one-sided packet criterion is

\[
 \min_{x\in\prod_P\Delta(\Omega_P)}
 \sum_{q,\epsilon,T}
       \prod_P\left(1-
       \sum_\omega x_{P\omega}
          {\bf1}_{\{T\in I_{P,q}^\epsilon(\omega)\}}\right)
 =o(W).                                                   \tag{5.1}
\]

The higher enumerator (2.2) decides every local common-option coefficient
which can enter a proposed home-bundle construction.  The atoms (0.2)
show that these coefficients are not controlled by first and pair
pseudorandomness, and that a growing-strength orthogonal-array or
low-codegree rainbow theorem is unavailable.

There are two logically distinct possibilities left.

1. **Use the flats.**  Build home bundles from packet-relative blind
   flats and prove that dispersed parent frames make those flats almost
   resolve the global target layer.
2. **Break the flats.**  Add genuinely nonconjugate compiler templates or
   cross-parent trades whose window schedule depends on the currently
   blind context coordinates.

The present affine option orbit cannot do the second: column complements
and permutations transport the flats but never destroy them.  The first
is a higher-order global alignment theorem and is not implied by the
recursive enumerator alone.

Thus the actual recursive compiler has a complete exact \(k\)-target
enumerator, but its option family is clustered at every order.  Near-
perfect home-packet assignment remains plausible only as a deliberately
structured resolution of these clusters, not as a consequence of
covering-array strength or generic degree/codegree expansion.

