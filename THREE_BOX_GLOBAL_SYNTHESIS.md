# Three-box programme: global synthesis after the local-architecture audit

## 1. Why this is the right scale of attack

Let

\[
  \nu(k)=\min |A|,
  \qquad
  W(k)=\binom{k}{\lfloor k/2\rfloor},
\]

where every nonzero `k`-bit mask must be the OR of a nonempty contiguous
subarray of `A`.  The exact finite cases are useful evidence, but repairing
one more value of `k` does not address the main mathematical gap

\[
                 W(k)\leq \nu(k)\leq(\sqrt2+o(1))W(k).
\]

The productive all-dimensional target is

\[
                         \nu(k)=(1+o(1))W(k).             \tag{1.1}
\]

The product-box reduction turns (1.1) into one uniform theorem about a
three-dimensional polynomial-sized poset.  This pass has now separated what
is genuinely promising in that reduction from two attractive but impossible
local architectures.

## 2. Proved global reduction

Split `[k]` into three balanced coordinate blocks and take a symmetric-chain
decomposition in each block.  Tuples of component chains partition the
Boolean lattice into boxes

\[
                P=[0,p]\times[0,q]\times[0,r].
\]

If `w(P)` denotes the width of a box, then the exact coefficient identity is

\[
                         \sum_P w(P)=W(k).              \tag{2.1}
\]

Words constructed independently inside the boxes may be concatenated.  Thus
the following local theorem would immediately imply (1.1).

> **Three-box OR lemma.**  Uniformly in `p,q,r`, the nonzero points of
> `[0,p] x [0,q] x [0,r]` admit a contiguous coordinatewise-maximum word of
> length
> \[
>          w(P)+O(p+q+r+1).                              \tag{2.2}
> \]

The normalization to coordinatewise maxima is exact: closing every entry
downward in each of the three component chains preserves every box-valued
interval OR.  For balanced blocks, typical side lengths are `Theta(sqrt k)`
and typical box widths are `Theta(k)`.  The local errors in (2.2) aggregate to

\[
                         O(W(k)/\sqrt k),                \tag{2.3}
\]

so (2.2) gives the stronger quantitative conclusion

\[
                \nu(k)\leq W(k)+O(W(k)/\sqrt k).
\]

The box rank-slack theorem shows that an additive term proportional to the
side length is necessary in cubic boxes.  Hence (2.2) asks for the correct
local order of error, not an unrealistically sharp statement.

## 3. Positive local theorems obtained

For the cubic box `[0,m]^3`, two explicit hook-based chain partitions
`L,R'` were constructed and audited.  They satisfy

\[
                 |L|=W_m,
                 \qquad |R'|=W_m+m,
                 \qquad |L\cap R'|\leq1.               \tag{3.1}
\]

Thus the bare chain-count and orthogonality requirements can be met with
exactly the permitted `O(m)` loss.  The construction is fully explicit: cut
the triangular double-intersection family in the two standard hook SCDs and
recombine `P_(i,j)` with `S_(i+1,j)`.  This is a real theorem, not a search
observation.

Independently, the concentric hexagonal walk through the middle layer of
`[0,2a]^3` has complete consecutive-minimum and consecutive-maximum shadows
at every depth.  This proves that all-depth two-sided shadow enumeration
itself is not the missing ingredient.  The separate band audit shows that
this particular order cannot be realized by a width-plus-perimeter monotone
interval band.

Together these results locate the difficulty after ordinary shadow coverage
and abstract orthogonality: it is the simultaneous endpoint order, interval
capacity, and pin-survival geometry.

## 4. Architectures now ruled out

### 4.1 Two balanced coordinate blocks

The natural two-block chain-product architecture cannot have constant one.
Already in a square two-chain box, refining one standard product SCD so that
it has an orthogonal partner requires a positive fraction of the grid width
in extra chains.  Summed over typical boxes, that loss is `Omega(W(k))`.
Three blocks are the first dimension in which width dominates side length.

### 4.2 Concentric rings with an `O(a)` monotone band

For the ring-by-ring middle ordering in `[0,2a]^3`, every factorable monotone
central band of total offset `D=O(a)` leaves at most

\[
                         3a^3+O(a^2)                    \tag{4.1}
\]

physical intervals that avoid all selected middle witnesses.  But the number
of nonzero targets below the middle layer is

\[
                         4a^3+O(a^2).                   \tag{4.2}
\]

Therefore no sparse labeling of such a band can be universal.  This kills
every complete-ring ordering with only `O(a)` repeats, not merely one choice
of ring phase.  Any future middle-layer skeleton must interleave radii or use
a genuinely different geometry.

### 4.3 The near-orthogonal hook pair

The pair in (3.1) has the correct number of chains but its endpoint
precedence is globally cyclic.  The precise obstruction is recorded in
`THREE_BOX_NEAR_ORTHOGONAL_PRECEDENCE_OBSTRUCTION.md`: one endpoint
precedence relation contains a family of

\[
                         \binom{m+1}{2}                 \tag{4.3}
\]

explicit alternating cycles.  Their full cut supports have multiplicity at
most two.  Fractional cycle packing therefore forces at least

\[
                         {m(m+1)\over4}                 \tag{4.4}
\]

chain-gap cuts, even when cuts may be placed in either endpoint family.
This is `Theta(W_m)`, not `O(m)`.

The cycles are local two-chain reversals, not the initially tempting nested
perimeter cycles.  For every `a+j<m`, the diagonal prefix
`D_j=P_(m-j,j)` and the chain `C_(a,j)` containing `S_(a,j)` occur in
opposite orders along `L_(a,j)` and `L_(a+1,j)`.  Their four witnessing
points are

\[
 (j,a,m-j),\quad(m-a,m-j,m-j),\quad
 (j,a+1,a),\quad(j,a+1,m-j).
\]

The diagonal-prefix supports are distinct consecutive gaps, the suffix
chains are distinct, and a left chain occurs in at most two certificates.
This gives the claimed congestion-two packing rigorously.

There is also an endpoint-count consequence in the pure-refinement model,
preceding triangular bandwidth.  If `x,y` cuts are assigned to the two sides
and the resulting pieces are not globally re-merged across old chains, then

\[
 n\geq\max(W_m+x,W_m+m+y)
    \geq W_m+{m^2+5m\over8}
    =(7/6-o(1))W_m.                                      \tag{4.5}
\]

Thus no choice of triangular ordering can recover near-width length from
this seed within that refinement model; it can only add further padding.
The quadratic cut obstruction survives arbitrary one-prefix/one-suffix
rematching, but the displayed chain-count consequence need not survive a
more general compensating rechain.

Thus the inner-label shift solves orthogonality but cannot be repaired into
an ordered endpoint pair at lower-order cost.  The lesson is structural:
endpoint precedence must be nearly acyclic **by design**.  It cannot be
treated as a final cleanup after constructing an unordered orthogonal pair.

## 5. Exact remaining mathematical lemma

The global programme is now concentrated in one local statement:

> **Ordered three-box lemma.**  For every `[0,p] x [0,q] x [0,r]`, construct
> two chain partitions with at most
> \[
>              w(P)+C(p+q+r+1)
> \]
> nonempty pieces per side such that:
>
> 1. their incidence is orthogonal;
> 2. both within-chain precedence digraphs are acyclic;
> 3. topological orders can be chosen with all occupied cells in the physical
>    triangle `left <= right`, using only the same `O(p+q+r)` slack; and
> 4. the resulting intervals satisfy coordinatewise pin survival.

By the endpoint-decomposition and pin-survival theorems, this lemma gives the
three-box OR lemma and hence (1.1).

The new precedence obstruction sharpens the design brief.  It is not enough
to seek another pair with almost minimum chain counts.  The pair must come
with an explicit acyclic orientation certificate, or at least an alternating
cycle transversal of size `O(p+q+r)`, from the moment it is defined.

A direct range-maximum construction proving (2.2) would be equally good and
may be cleaner; the ordered-chain formulation is a diagnostic normal form,
not a requirement that the proof use SCD surgery.

## 6. Current conclusion

No new exact value of `nu(k)` is claimed here.  The progress is global:

* the constant-one asymptotic conjecture is reduced to a uniform three-box
  lemma;
* the exact width and error aggregation are proved;
* all-depth hexagonal shadows and near-minimum orthogonality are separately
  achievable;
* the ring-band route is killed by a cubic interval-capacity deficit; and
* the hook-pair route is killed by a quadratic precedence-cycle packing.

The next useful theorem must therefore build a locally ordered object from
the outset.  Further isolated finite-`k` repair is not the active mathematical
strategy.
