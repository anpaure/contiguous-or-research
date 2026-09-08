# Cross-fibre \(Q_{r+1}\) recoupling: normalized IDP and the persistent scaled congruence

Date: 2026-07-26

Method: pure mathematics only.  No computation, solver, common-order
syndrome assumption, random tiling, or web input is used.

## 0. Result

This note attacks the cross-fibre recoupling requested after the
\(M\)-convex failure of individual selector fibres.

There is a smallest exact recoupling.  A physical \(Q_{r+1}\) slab has
\(r+1\) resolutions into two parallel \(Q_r\) packets: choose one
coordinate to freeze and leave the other \(r\) active.  After normalizing
direction counts by the one-packet atom

\[
                              g_r={2^r\over r},       \tag{0.1}
\]

the resolution vectors are twice the bases of \(U_{r,r+1}\).  After
dividing by \(2g_r\), they are the unscaled hypersimplex
\(\Delta(r,r+1)\), and arbitrary bundles of slabs have an exact integer
decomposition theorem.

The normalization cannot be removed.

### Persistent congruence

Every isometric \(Q_r\)-packet factor, with arbitrary cycle-specific
direction orders and arbitrary affine compiler conjugates, contributes
exactly \(g_r\) lower-depth-one targets in each active direction and zero
in every inactive direction.  Hence every bundle of such packets has
direction counts divisible by \(g_r\).

If the packets partition a complete cube, the number active in each
physical direction has the same parity as the total number of packets.
Therefore differences between any two tilings of the same cubical
super-fibre are divisible by

\[
                              2g_r={2^{r+1}\over r}   \tag{0.2}
\]

in every direction.  Complementary active sets and diverse compiler
orders do not change this invariant.  It persists for bundles of every
size, in particular every subexponential-size bundle.

### Quantitative boundary

At the direction-marginal level, rounding one fractional
\(Q_{r+1}\)-resolution per slab costs at most \(4g_r\) in
\(\ell^1\).  Over owner mass \(W_0\), the total is at most

\[
                              {2W_0\over r}=o(W).     \tag{0.3}
\]

Thus cross-fibre recoupling removes the *coefficient-scale direction
error*.  It does not prove literal all-depth balancing: the projection
forgets target identities, and changing a slab resolution can alter a
large set of higher-depth traces.  A further target-labelled cancellation
theorem is still necessary.

## 1. The two-packet resolution trade

Let \(R\) be a set of \(r+1\) physical orientation axes and identify the
owner slab with \(Q_R\).  For \(i\in R\), define the \(i\)-resolution

\[
 \mathcal R_i
  =\bigl\{\{x_i=0\}\cong Q_{R\setminus\{i\}},
           \{x_i=1\}\cong Q_{R\setminus\{i\}}\bigr\}. \tag{1.1}
\]

The two members of (1.1) are disjoint physical \(Q_r\)'s and partition
all of \(Q_R\).  Hence, for any \(i,j\in R\),

\[
                         \mathcal R_i
                       \longleftrightarrow
                         \mathcal R_j                 \tag{1.2}
\]

is an exact two-packet-versus-two-packet owner trade.

Install any certified compiler factor independently in the two packets
on either shore.  The two packets may use different cyclic direction
orders and different affine conjugates.  Since every packet receives a
complete factor, (1.2) creates no owner, seam, collar, or interface
boundary.

This is the minimal cross-fibre move: the coordinate frozen on one shore
is active on the other, so the old selector decoder is broken inside the
slab.

## 2. Exact direction vectors

An isometric \(C_{2r}\) in \(Q_r\) contains each of its \(r\) physical
directions exactly twice.  A spanning factor contains

\[
                              {2^r\over2r}            \tag{2.1}
\]

cycles.  Therefore the number of factor edges, equivalently lower
depth-one target occurrences, in each active direction is

\[
                 2\,{2^r\over2r}={2^r\over r}=g_r.  \tag{2.2}
\]

This calculation uses neither a common direction order nor a syndrome
column.  It is true cycle by cycle.

The \(i\)-resolution has two packets, both active on
\(R\setminus\{i\}\).  Its direction-count vector is therefore

\[
                    d_i=2g_r(\mathbf1_R-e_i).        \tag{2.3}
\]

After division by \(2g_r\), the \(r+1\) choices in (2.3) are exactly

\[
        \{\mathbf1_R-e_i:i\in R\}
              =\{\mathbf1_A:A\in\tbinom Rr\},         \tag{2.4}
\]

the bases of the uniform matroid \(U_{r,r+1}\).

## 3. Integer decomposition for slab bundles

### Theorem 3.1 (normalized super-fibre IDP)

Take \(K\) disjoint \(Q_{r+1}\) slabs with the same labelled carrier
\(R\), and choose one resolution in each.  The set of normalized
aggregate direction vectors is exactly

\[
 \boxed{
 \left\{u\in\mathbb Z^{R}:
       0\le u_i\le K,\quad
       \sum_{i\in R}u_i=Kr\right\}.}                 \tag{3.1}
\]

Equivalently, it is the full integer-point set of
\(K\Delta(r,r+1)\), hence is \(M\)-convex and has the integer
decomposition property.

#### Proof

If \(c_i\) slabs use the \(i\)-resolution, then

\[
                  u_i=K-c_i,\qquad
                  c_i\ge0,\qquad \sum_i c_i=K.       \tag{3.2}
\]

Thus every resolution choice satisfies (3.1).  Conversely, given
\(u\) in (3.1), put \(c_i=K-u_i\).  These are nonnegative integers
summing to

\[
             (r+1)K-Kr=K.                           \tag{3.3}
\]

Assign exactly \(c_i\) slabs to resolution \(i\).  Their sum is \(u\).
\(\square\)

The same proof works for disjoint carrier sets by taking direct sums of
uniform-matroid base polytopes.  It also permits independent compiler
orders inside every constituent packet: those labels refine a resolution
without changing its direction vector.

## 4. Deterministic direction rounding with \(o(W)\) cost

Let a fractional solution choose resolution \(i\) in one slab with
weights

\[
                         \lambda_i\ge0,\qquad
                         \sum_i\lambda_i=1.           \tag{4.1}
\]

Its normalized direction vector is

\[
                         \mathbf1_R-\lambda.         \tag{4.2}
\]

Choose any \(i\) with maximal \(\lambda_i\), and round to
\(\mathbf1_R-e_i\).  Then

\[
 \|(\mathbf1_R-e_i)-(\mathbf1_R-\lambda)\|_1
          =\|e_i-\lambda\|_1
          =2(1-\lambda_i)\le2.                       \tag{4.3}
\]

Restoring the scale \(2g_r\), one slab incurs at most \(4g_r\)
direction-marginal error.

A disjoint slab contains \(2^{r+1}\) owners.  Thus a collection covering
\(W_0\) owners contains \(W_0/2^{r+1}\) slabs, and independent
deterministic rounding gives

\[
 {W_0\over2^{r+1}}\,4{2^r\over r}
                         ={2W_0\over r}=o(W).         \tag{4.4}
\]

There is no grouping interface cost: the slabs and their two-packet
resolutions are exact owner partitions.  Equation (4.4) is only a
direction-projection error bound.

## 5. Congruence for arbitrary packet bundles

### Theorem 5.1 (one-packet divisibility)

Let \(\mathcal P\) be any owner-disjoint family of physical \(Q_r\)
packets, each carrying an arbitrary factor into isometric
\(C_{2r}\)'s.  Let \(a_j\) be the number of packets whose active set
contains physical direction \(j\).  Then its lower-depth-one direction
count is

\[
                              D_j=g_r a_j.            \tag{5.1}
\]

In particular

\[
                              D_j\equiv0\pmod{g_r}.   \tag{5.2}
\]

The same holds for upper depth one.

#### Proof

Every packet containing \(j\) contributes (2.2), independently of its
direction orders and affine conjugate.  Packets not containing \(j\)
contribute zero.  Summation proves (5.1). \(\square\)

### Theorem 5.2 (cubical parity)

Suppose the packets partition a complete physical cube \(Q_D\), and let
\(N\) be their number.  Then

\[
                              a_j\equiv N\pmod2       \tag{5.3}
\]

for every \(j\in D\).  Hence any two \(Q_r\)-packet tilings of the same
cube have direction-count difference divisible by \(2g_r\).

#### Proof

Cut \(Q_D\) into the two \(j\)-halves.  A packet active in \(j\)
places \(2^{r-1}\) owners in each half.  A packet inactive in \(j\) lies
entirely in one half and contributes \(2^r\) owners there.  If
\(b_0,b_1\) are the numbers of inactive packets in the two halves, the
equality of the half sizes gives

\[
 a_j2^{r-1}+b_0 2^r
   =a_j2^{r-1}+b_1 2^r,
\]

so \(b_0=b_1\).  Therefore

\[
                         N-a_j=b_0+b_1
\]

is even, proving (5.3).  Apply (5.1) to two tilings and subtract.
\(\square\)

Theorem 5.2 applies regardless of how many selector fibres are grouped.
It is therefore stronger than a subexponential-bundle obstruction.

## 6. Why complementary active sets do not unscale the lattice

Complementary active sets can make the *sum* of direction counts
uniform.  They cannot change the congruence class.

For any bundle, its normalized packet-count vector
\((a_j)\) is integral.  For a cubical super-fibre it lies in the parity
coset

\[
             \{a\in\mathbb Z^D:a_j\equiv N\pmod2,\
                              \sum_j a_j=Nr\}.        \tag{6.1}
\]

Multiplication by \(g_r\) gives the literal direction counts.  Minkowski
sums of complementary resolutions remain inside (6.1); diverse-order
compiler labels only refine the fibres over one point of (6.1).

Thus no cross-fibre grouping made solely of whole isometric \(Q_r\)
packets can produce an unscaled unit hypersimplex in literal target
coordinates.  The smallest exact normalized exchange is the
\(Q_{r+1}\) trade (1.2), and its literal step is \(2g_r(e_i-e_j)\).

## 7. All-depth boundary

The normalized IDP in Theorem 3.1 closes the direction-count projection,
not the literal target problem.  At depth \(q>1\), a target records the
entire consecutive \(q\)-window, its source orientation, and its
macroblock frame.  Two slab resolutions with the same direction
marginals can have different literal target supports.

Using independent or diverse cyclic orders is necessary, but direction
divisibility gives no cancellation theorem for those higher flags.  Even
under the optimistic assumption that only windows meeting an exchanged
direction are charged, the consecutive-window census has order

\[
                         {WH^2\over r},               \tag{7.1}
\]

which is unusable in the central regime.  Without a proved alignment of
the common directions, the literal symmetric difference may be larger.
Thus (7.1) is a lower benchmark for what a successful cancellation must
beat, not an asserted exact derivative formula.

Therefore the recoupling result is exact but partial:

* owner/interface cost: zero;
* direction-marginal rounding cost: \(O(W/r)=o(W)\);
* literal all-depth cancellation: still open;
* unit-scale polymatroidality: impossible within whole isometric
  \(Q_r\) packets because of Theorems 5.1--5.2.

A coefficient-one continuation must construct target-labelled
cancellations between the diverse-order slab resolutions, rather than
seek an unscaled direction hypersimplex from complementary active sets
alone.

The higher-depth face audit is continued in
\`MATH_THEOREM_HIGHER_DEPTH_SLAB_IDP_AND_FACE_CONGRUENCE_20260726.md\`.
At depth \(q\), every literal face occurs with its antipodal mate, every
support has even multiplicity, and active-direction incidence is exactly
\(q2^r/r\); both signs and all depths are projections of one common
nested flag vector.
