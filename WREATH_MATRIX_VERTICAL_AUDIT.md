# The wreath matrix as a vertical-control device

This note audits the two papers of Jan Petr and Pavel Turek,
*The wreath matrix* (arXiv:2501.07269) and *Intervals in Dyck paths and the
wreath conjecture* (arXiv:2501.07277), against the vertical-shadow problem.

The conclusion has one genuinely positive part and one sharp limitation.

* The positive part is stronger than the spectrum stated in the paper.  A
  four-wreath kernel vector from Petr--Turek is a **rank selector**: after all
  cyclic orders are identified on one common column space, it changes the
  interval multiplicities at exactly one complementary pair of ranks and no
  other rank.  The translates of these vectors span every real discrepancy
  with zero point marginals.  Consequently the complete simultaneous
  vertical problem has a perfect signed/fractional solution, rank by rank,
  inside the kernel of the middle incidence matrix.
* This does not round to a wreath factor.  A kernel vector need not be a
  support-feasible switch between two `0/1` factors, and an unpointed wreath
  matrix forgets the nesting of starts required by a symmetric-chain
  resolution.  The natural attempt to restore that nesting with the
  Petr--Turek Dyck heights already fails for `m=2`, for every possible wreath
  decomposition of the middle layer.

Thus the algebra finds the correct continuous tangent directions.  The exact
missing theorem is integral: combine the rank-selecting trades into
alternating circuits whose positive and negative wreaths are separately
disjoint.  A single four-wreath trade can never itself be support-feasible.

Throughout,

\[
        n=2m+1,\qquad
        \Omega=\{\text{unoriented cyclic orders of }[n]\},\qquad
        W=\binom nm,
\]

and a cyclic order is taken modulo rotation and reversal.  For `m>=2`, its
family of cyclic `m`-intervals determines the order, so `Omega` is also the
column set of the Petr--Turek `(n,m)` wreath matrix.

## 1. The full tower of interval-incidence matrices

For `1<=r<=n-1`, define

\[
 B_r:\mathbb R^\Omega\longrightarrow
       \mathbb R^{\binom{[n]}r},
 \qquad
 (B_rx)_S=
   \sum_{C\in\Omega}x_C\,{f1}\{S\text{ is a cyclic }r\text{-interval of }C\}.
 \tag{1.1}
\]

The Petr--Turek wreath matrix at the middle rank is exactly the Gram matrix

\[
                         M=B_m^{\mathsf T}B_m.          \tag{1.2}
\]

An exact middle wreath factor is a vector

\[
              x\in\{0,1\}^{\Omega},\qquad B_mx={\bf1}. \tag{1.3}
\]

It uses

\[
                         b=W/n=\operatorname {Cat}_m   \tag{1.4}
\]

orders.  At rank `r`, its full vertical multiplicity vector is

\[
                         c_r=B_rx.                     \tag{1.5}
\]

Every selected order supplies `n` intervals, so the mean multiplicity is

\[
                 \mu_r=\frac{W}{\binom nr}.            \tag{1.6}
\]

The exact quadratic duplicate energy is

\[
 \mathcal E_r(x)=\|B_rx-\mu_r{\bf1}\|_2^2.             \tag{1.7}
\]

Since `B_r^T 1=n 1` and every feasible `x` has `1^T x=b`, minimizing (1.7)
is equivalent to minimizing

\[
                    x^{\mathsf T}K_rx,
       \qquad      K_r=B_r^{\mathsf T}B_r.             \tag{1.8}
\]

Thus a multi-depth collision energy is encoded exactly by the **extended
Gram family**

\[
                         \sum_r w_rK_r,                \tag{1.9}
\]

not by `M=K_m` alone.

Indeed, on (1.3),

\[
                         x^{\mathsf T}Mx=W              \tag{1.10}
\]

is constant, and the difference of any two exact factors lies in `ker M`.
The positive eigenvalues computed by Petr--Turek therefore cannot distinguish
two middle factors by their vertical quality.  All useful freedom lies in the
zero eigenspace.

## 2. Representation-theoretic form of the missing data

The maps `B_r` are `S_n`-equivariant.  For `r<=m`, the target permutation
module is multiplicity-free:

\[
 \mathbb C^{\binom{[n]}r}
   \cong \bigoplus_{j=0}^{r} S^{(n-j,j)}.              \tag{2.1}
\]

Consequently, on the `S^{(n-j,j)}` isotypic component of
`C^Omega`, the positive semidefinite operator `K_r` has rank at most one in
the multiplicity space.  In suitable notation it has the form

\[
 K_r\big|_j
   =\lambda_{r,j}
      \bigl|u_{r,j}\bigr\rangle
      \bigl\langle u_{r,j}\bigr|\otimes I_{S^{(n-j,j)}}. \tag{2.2}
\]

Petr--Turek compute the norms/eigenvalues in (2.2) for the single row
`r=m`.  A simultaneous spectral treatment would additionally need the
angles

\[
                         \langle u_{r,j},u_{s,j}\rangle,          \tag{2.3}
\]

equivalently the singular scalars of the rectangular cross-incidence
operators `B_r B_s^T`.  Those scalars are in principle computable: an entry
of `B_rB_s^T` is the number of cyclic orders in which two prescribed sets are
intervals, and by symmetry depends only on their sizes and intersection.
The usual Johnson-scheme/Eberlein transform then diagonalizes it.

But even complete knowledge of (2.2)--(2.3) is a continuous statement.  It
does not ensure that a vector in the affine space `B_mx=1` is nonnegative,
`0/1`, or admits nested pointed starts.  The next theorem makes this
limitation exact rather than philosophical.

## 3. Petr--Turek's four-wreath vector is a rank selector

Fix the cyclic order

\[
                         C=(1,2,\ldots,n).              \tag{3.1}
\]

For `2<=a<=m`, put

\[
 \tau=(1\ 2),\qquad \sigma=(a+1\ a+2)
\]

and form the signed four-order vector

\[
 z_a=e_C-e_{\tau C}-e_{\sigma C}+e_{\tau\sigma C}.    \tag{3.2}
\]

This is the vector called `x_a` in Lemma 5.1 of *The wreath matrix*.

### Theorem 1 (rank-selector trade)

For every `1<=r<=m`,

\[
                         B_rz_a=0\qquad(r\ne a).        \tag{3.3}
\]

At the exceptional rank, with `K={3,4,...,a}` (empty when `a=2`),

\[
\begin{aligned}
 B_az_a={}&e_{K\cup\{2,a+1\}}
           -e_{K\cup\{1,a+1\}}\\
          &-e_{K\cup\{2,a+2\}}
           +e_{K\cup\{1,a+2\}}.                     \tag{3.4}
\end{aligned}
\]

By complementation, `B_(n-a)z_a` is the complementary copy of (3.4), and
all other upper ranks are unchanged.  In particular, for `a<m`,

\[
                         z_a\in\ker B_m=\ker M.         \tag{3.5}
\]

#### Proof

Let `P={1,2}` and `Q={a+1,a+2}`.  If an `r`-set `S` contains zero or two
members of `P`, the two terms related by `tau` cancel in (3.2).  The same is
true for `Q` and `sigma`.  A nonzero coefficient is therefore possible only
when `S` contains exactly one member of each of `P,Q`.

If such an `S` is a cyclic interval in one of the four orders, the two ends
of that interval must cut the two adjacent pairs `P,Q`.  The two arcs between
the cuts have lengths `a` and `n-a`.  Since `r<=m<n-a`, necessarily `r=a`.
This proves (3.3).  At rank `a`, the four choices of one endpoint from each
pair give exactly the four sets and signs displayed in (3.4).  The statement
for upper ranks follows because the complement of a cyclic `a`-interval is a
cyclic `(n-a)`-interval.  QED.

This direct proof uses all cyclic starts and therefore remains valid when
`gcd(n,a)>1`; it is slightly cleaner for the present application than
identifying the smaller `(n,a)`-wreaths used in the general Petr--Turek
definition.

## 4. The rank selectors span every real vertical discrepancy

Let `A_a` be the point-versus-`a`-set incidence matrix:

\[
 (A_af)_i=\sum_{S\ni i}f_S.                            \tag{4.1}
\]

Every vector in (3.4) lies in `ker A_a`.  Conversely, all its relabelings
span this kernel.

### Lemma 2 (elementary interval squares span the margin kernel)

For `2<=a<=n-2`, the vectors

\[
 e_{K\cup\{x,y\}}-e_{K\cup\{x',y\}}
 -e_{K\cup\{x,y'\}}+e_{K\cup\{x',y'\}},              \tag{4.2}
\]

where `|K|=a-2` and `x,x',y,y'` are distinct and outside `K`, span
`ker A_a` over `R`.

#### Proof

They plainly lie in the kernel.  For the reverse inclusion, let `f` be
orthogonal to every vector (4.2).  If `R,R'` are adjacent `(a-1)`-sets
avoiding `x,y`, the four-term relation shows that

\[
 f(R\cup\{x\})-f(R\cup\{y\})
 =f(R'\cup\{x\})-f(R'\cup\{y\}).                      \tag{4.3}
\]

The Johnson graph on the `(a-1)`-sets avoiding `x,y` is connected, so the
difference in (4.3) depends only on `x,y`.  These differences satisfy the
cocycle identity, hence equal `c_x-c_y` for suitable numbers `c_i`.
It follows along every edge of the Johnson graph `J(n,a)` that

\[
                         f(S)-\sum_{i\in S}c_i
\]

is constant.  Thus `f` is in the row space of `A_a`.  The orthogonal
complement of the span of (4.2) is therefore `row(A_a)`, proving the claim.
QED.

Now let `x` be any weighted collection of `b` cyclic orders.  Every point is
contained in exactly `a` of the cyclic `a`-intervals of one order, so

\[
                         A_aB_ax=ab\,{\bf1}.            \tag{4.4}
\]

The constant vector `mu_a 1` has the same point marginals, because

\[
 \mu_a\binom{n-1}{a-1}
   =\frac{W}{\binom na}\frac an\binom na
   =\frac{aW}{n}=ab.                                   \tag{4.5}
\]

Therefore

\[
                         B_ax-\mu_a{\bf1}\in\ker A_a.  \tag{4.6}
\]

Combining Theorem 1 and Lemma 2 gives the main positive conclusion.

### Theorem 3 (simultaneous signed vertical balancing)

Let `x` be any exact middle wreath factor.  There is a real vector

\[
                         z\in\ker B_m                 \tag{4.7}
\]

which is a linear combination of relabelings of the four-order trades
`z_2,...,z_(m-1)` and for which

\[
             B_a(x+z)=\mu_a{\bf1}\qquad(1\le a<m).    \tag{4.8}
\]

Consequently all complementary upper ranks are balanced as well, while

\[
                         B_m(x+z)={\bf1}.               \tag{4.9}
\]

#### Proof

Rank `a=1` is already constant for every collection of cyclic orders.  For
each `2<=a<m`, (4.6) and Lemma 2 express
`mu_a 1-B_ax` as `B_a z^(a)`, where `z^(a)` is a linear combination of
relabelings of `z_a`.  Theorem 1 says that `z^(a)` changes no rank other than
`a,n-a`; in particular it lies in `ker B_m`.  Hence

\[
                         z=\sum_{a=2}^{m-1}z^{(a)}
\]

does all corrections simultaneously.  QED.

Equivalently, the linear map

\[
 \ker B_m\longrightarrow\bigoplus_{a=2}^{m-1}\ker A_a,
 \qquad z\longmapsto(B_2z,\ldots,B_{m-1}z),             \tag{4.10}
\]

is surjective.  It even has an explicit rank-by-rank right inverse built
from four-wreath trades.

Theorem 3 is the exact extent of the spectral gain.  It says there is **no
real-linear or representation-theoretic obstruction at all** to simultaneous
perfect vertical balancing.  But the corrected vector `x+z` may have
negative, fractional, or larger-than-one coordinates.  Indeed the means
`mu_a` are usually nonintegral.  The uniform fractional weighting of all
cyclic orders is another immediate perfectly balanced point.  What remains
is precisely the `0/1` geometry of the exact-cover polytope.

## 5. The integral switch problem exposed by the theorem

A particularly important obstruction is hidden by the signed notation: a
single vector (3.2) is **never** a legal two-for-two switch of exact factors.

### Lemma 4 (no elementary trade is support-feasible)

For `2<=a<m`, each of the two diagonal pairs

\[
                 \{C,\tau\sigma C\},\qquad
                 \{\tau C,\sigma C\}                  \tag{5.1}
\]

contains two wreaths with a common middle set.  Hence neither pair can be a
subset of an exact middle factor.

#### Proof

Swapping two adjacent coordinates changes only those cyclic `m`-intervals
which contain exactly one member of the swapped pair.  There are exactly two
such intervals.  The relative permutation between either pair in (5.1) is
the product of two disjoint adjacent swaps, so at most four middle intervals
change.  The two wreaths therefore share at least `n-4>0` middle sets
(`n>=7` here).  Two wreaths in an exact factor are disjoint.  QED.

Thus the four-order vectors are tangent directions but not edges of the
`0/1` exact-cover polytope.  A concrete global theorem sufficient for
near-rainbow marginals must instead say:

> For each `a=m-q` in the required central band, combine many relabeled
> rank-`a` four-order vectors into an integral circuit whose positive-support
> wreaths are pairwise disjoint and whose negative-support wreaths are
> pairwise disjoint, and whose rank-`a` action reduces the duplicate energy
> to `o(binomial(n,a))`.

The ranks would still decouple at the level of full interval marginals by
(3.3).  What the wreath matrix does **not** prove is the existence of even
one such disjoint-support circuit through a given exact factor, let alone
connectivity or expansion of the factor space.  A signed kernel relation is
not automatically a move in the `0/1` fibre; in the smallest explicit
relations, overlap makes this failure absolute.

There is a second limitation.  The vectors `B_ax` count all starts of a
selected order.  A symmetric-chain resolution must select nested subsets of
starts at successive depths.  Unpointed matrices `K_r` forget that coupling.
Even perfect marginal coverage at every rank does not by itself supply the
nested perfect matchings of `MSW_ATOM_FLOW.md`.

## 6. The strengthened Dyck conjectures do not supply the nesting

Petr--Turek Conjectures 2.2 and 2.4 ask for a wreath factor indexed by Dyck
paths, with the low coordinate labels under rises and the high labels under
falls; Conjecture 2.4 adds a reflection symmetry.  Their interval identity

\[
                         \iota_m(m,l)=\binom ml^2       \tag{6.1}
\]

is exactly the necessary type count for the middle layer.  Independently,
the pointed-Dyck height identity gives exactly the global symmetric-chain
radius ledger.  It is tempting to assign to the cyclic start associated with
a pointed cut the radius equal to its height.

This implication is false even in the first nontrivial case, independently
of how the conjectured labels are chosen.

### Theorem 4 (the pointed-height Petr--Turek route fails at `m=2`)

No decomposition of `binom([5],2)` into two wreaths can be vertically
resolved if the two wreaths are required to receive the pointed-height
multisets of the two Dyck paths of semilength two.

#### Proof

The two Dyck paths are

\[
                         UUDD,\qquad UDUD,
\]

and their five vertex heights are

\[
                         (0,1,2,1,0),qquad(0,1,0,1,0). \tag{6.2}
\]

At depth one they therefore demand respectively three and two active starts.

A `(5,2)` wreath is a Hamilton cycle in `K_5`.  Two wreaths partitioning all
two-sets are complementary Hamilton cycles.  Normalize the first cyclic
order to

\[
                         (0,1,2,3,4).
\]

The other is, up to orientation,

\[
                         (0,2,4,1,3).
\]

At an active start with current coordinate `t`, the lower depth-one member
is the singleton `{t}`, while the upper member is the four-set complementary
to the predecessor of `t`.  Hence the active starts must form a perfect
matching from current coordinates to predecessor coordinates.

Each wreath supplies one such permutation matching.  The relative
permutation of the two predecessor maps is a five-cycle (step `-1` versus
step `-2`, up to reversing the second cycle).  Their union is therefore one
alternating ten-cycle.  It has exactly two perfect matchings: all five edges
from the first wreath, or all five edges from the second.  No perfect matching
uses `3+2` edges.  This contradicts (6.2).  QED.

The actual `m=2` example printed by Petr--Turek is precisely the two orders
above.  The theorem is stronger: changing to any other compatible wreath
decomposition cannot help.

This does not refute their conjectures, which concern only the middle layer.
It proves that the conjectures plus the correct Dyck radius histogram do not
imply the vertical theorem.  Radius mass must be transferred between Dyck
paths/wreaths, or selected by a separate global matching.

## 7. Final assessment

The wreath-matrix program gives a useful new global direction, but not by
using the already-computed eigenvalues as a black box.

1. Replace the one matrix `M` by the tower `B_r` and the pointed versions
   needed for nested starts.
2. Use the four-wreath vectors as rank-local **signed** trades.  Theorem 3
   proves that they span every continuous vertical correction independently
   at every rank; Lemma 4 proves that none is individually an exact-factor
   switch.
3. Prove a disjoint-support alternating-circuit theorem inside the `0/1`
   fibre `B_mx=1`.  This is the first genuinely integral gate.
4. After marginal defects are small, solve the nested-start tower by the
   bipartite matching formulation in `MSW_ATOM_FLOW.md`.

So the representation theory does encode the multi-depth duplicate energy
once the extended Gram family is introduced, and its kernel contains exactly
the right continuous correction directions.  It does not currently select a
near-rainbow factor: the missing content is nonnegative integral rounding and
pointed nesting, not another eigenvalue calculation for `M`.
