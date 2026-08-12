# Exact dicut representation and the one-shore Gray-prefix no-go

**Date:** 2026-08-04  
**Status:** unconditional exact-cut theorem and pair-cell obstruction.  The
note sharpens the bilateral component criterion in the all-available case
to a nested measurable-set representation.  It then proves that a connected
cyclic interval inside one pair cell cannot be assembled from several whole
cells of one other pairing.  Thus the most direct binary-expansion/Gray-prefix
construction is impossible except in the single-power residue case.  A
genuinely two-shore nested-difference construction remains open.  At the
residence scale `D>s_2(r)`, even the exceptional single-power case is too
small-dimensional to supply a valid macro block.

## 1. Exact cut representation for two available partitions

Let `P,Q` be partitions of a finite universe `V`, and suppose every block on
both shores is available.  Preselect an arbitrary owner set `U subseteq V`.
We ask whether `U` can be extended to an exact cover of `V` by adding whole
blocks from `P` and `Q`.  Here an extension means that the added blocks are
pairwise disjoint, are disjoint from `U`, and together with `U` have union
`V`.

A set is **P-measurable** when it is a union of `P`-blocks, and similarly
for `Q`.

### Theorem 1.1 (nested-difference representation)

The following are equivalent.

1. `U` extends to an exact cover by whole `P`- and `Q`-blocks.
2. There are a `P`-measurable set `A` and a `Q`-measurable set `B` such that

   \[
                              A\subseteq B,
                              \qquad U=B\setminus A.           \tag{1.1}
   \]
3. In the block-intersection multigraph `Gamma(P,Q)`, oriented canonically
   from the `P` shore to the `Q` shore, the owner edges labelled by `U` are
   exactly a directed cut: there is a vertex set `S` with

   \[
                 \delta^-(S)=\varnothing,
                 \qquad \delta^+(S)=U.                        \tag{1.2}
   \]

Here parallel owner edges retain their labels, so (1.2) is an equality of
owner-edge sets.

#### Proof

Suppose an extension is given.  Let `A` be the union of the selected
`P`-blocks, and let `Y` be the union of the selected `Q`-blocks.  Exact
coverage says

\[
                     A\cap Y=\varnothing,
                     \qquad A\mathbin{\dot\cup}Y=V\setminus U. \tag{1.3}
\]

Put `B=V-Y`.  Complements of `Q`-measurable sets are `Q`-measurable.
Equation (1.3) gives `A subseteq B` and `B-A=U`, proving (1) implies (2).

Conversely, given (1.1), select all `P`-blocks contained in `A` and all
`Q`-blocks contained in `V-B`.  These two measurable sets are disjoint and
their union is

\[
                         A\cup(V-B)=V-U.
\]

Together with the preselected set `U`, they form an exact cover.  This proves
(2) implies (1).

For the cut form, let `S` consist of

* the `P`-blocks outside `A`, and
* the `Q`-blocks outside `B`.

An edge of the canonical orientation enters `S` only if its owner lies in
`A` and outside `B`, which is impossible because `A subseteq B`.  Thus
`delta^-(S)` is empty.  An edge leaves `S` exactly when its owner lies
outside `A` and inside `B`, namely in `B-A=U`.  This gives (1.2).

Conversely, given a dicut (1.2), let `A` be the union of the `P`-blocks
outside `S` and let `B` be the union of the `Q`-blocks outside `S`.  The
absence of an entering edge says that no owner lies in `A-B`, so
`A subseteq B`.  The leaving edges are exactly the owners in `B-A`, hence
`U=B-A`.  Thus (2) and (3) are equivalent. \(\square\)

### Corollary 1.2 (zero-zero incidence form)

Equivalently, there are binary block labels `x_A` on `P` and `y_B` on `Q`
such that

\[
 \begin{array}{c|c}
 v\in U & x_{P(v)}=y_{Q(v)}=0,\\
 v\notin U & x_{P(v)}+y_{Q(v)}=1.
 \end{array}                                                  \tag{1.4}
\]

Thus `U` is the complete set of existing edges between the two zero-block
classes, and there is no edge between the two one-block classes.

#### Proof

Given an exact extension, label a block `1` exactly when it is selected.
Exact coverage gives (1.4).  Conversely, select precisely the blocks labelled
`1`.  The second row of (1.4) covers every owner outside `U` exactly once,
while the first row makes all selected blocks disjoint from `U`; the absence
of a `1,1` incidence makes the selected blocks pairwise disjoint.  Thus the
labels give an exact extension. \(\square\)

This is sharper than saying that `U` merely disconnects each of its own
edges.  An extendible puncture is a saturated one-way cut, not an arbitrary
multicut.

## 2. Cells contained in a cell of another pairing

Now let `R,Q` be perfect pairings on the same ground set, and let `C` be one
pair cell of `R`.  Its Johnson graph is a cube on the singleton pairs of its
record.

### Lemma 2.1 (nonshared singleton obstruction)

If a `Q`-cell `K` is contained in `C`, then every singleton pair in the
record of `K` is also a pair of `R`.

#### Proof

Suppose a singleton `Q`-pair `{p,q}` is not an `R`-pair.  The cell `K`
contains two owners which agree everywhere except that one selects `p` from
this singleton pair and the other selects `q`.  The coordinates `p,q` lie
in two distinct `R`-pairs.  Switching `p` to `q` changes the occupancies of
both of those `R`-pairs, so the two owners have different `R`-cell records.
They cannot both lie in `C`, contradicting `K subseteq C`. \(\square\)

### Theorem 2.2 (contained cells are cube-edge isolated)

Let `K_1,K_2` be distinct `Q`-cells, both contained in one `R`-cell `C`.
No cube edge of `C` joins a vertex of `K_1` to a vertex of `K_2`.

Consequently, every connected subset of the cube graph of `C` which is a
union of whole contained `Q`-cells is exactly one `Q`-cell.

#### Proof

An edge of the cube `C` swaps the selected member of one singleton `R`-pair
`{p,q}`.  If `{p,q}` is also a `Q`-pair, the `Q` occupancy record is unchanged,
so both edge endpoints lie in the same `Q`-cell.

Assume `{p,q}` is not a `Q`-pair.  Let `p'` and `q'` be their respective
partners in `Q`.  Swapping `p` for `q` changes the occupancies of the two
distinct `Q`-pairs `{p,p'}` and `{q,q'}` by one.  If both endpoint `Q`-cells
were contained in `C`, Lemma 2.1 would forbid either record from having a
singleton on either of these nonshared `Q`-pairs.

But two integers in `{0,1,2}` which differ by one cannot both avoid `1`.
Already on the pair `{p,p'}`, one endpoint record has occupancy `1`, or the
same is true after reversing the direction of the swap.  Hence at least one
endpoint cell is not contained in `C`.  Thus an edge whose two endpoints
belong to contained `Q`-cells cannot change the `Q`-cell.

Every contained `Q`-cell is itself a connected subcube of `C`: Lemma 2.1
makes each of its singleton directions a singleton direction of `C`.
Contained `Q`-cells are also disjoint.  The first statement therefore says
that they are exactly the connected components of their union inside the
cube graph of `C`.  A connected union contains only one of them. \(\square\)

The proof allows `R` and `Q` to share some pairs.  Those common singleton
directions give the internal cube directions of a contained `Q`-cell; every
nonshared direction leaves the family of contained cells before it can enter
another one.

## 3. The binary Gray-prefix temptation

For context, let

\[
                  g_0,g_1,\ldots,g_{2^m-1}                    \tag{3.1}
\]

be the binary reflected Gray ordering of `Q_m`.  If

\[
                  b=2^{d_1}+\cdots+2^{d_t},
                  \qquad d_1>\cdots>d_t,                      \tag{3.2}
\]

then the prefix `{g_0,...,g_(b-1)}` is a disjoint union of affine coordinate
subcubes of dimensions `d_1,...,d_t`.  This follows by recursively removing
the largest complete reflected half-cube.  The blocks occur consecutively
in the Gray traversal, so their union is connected.

This makes (3.2) look perfectly adapted to a residue
`b congruent to W_r modulo 2^M`: one might try to realize each binary summand
as one whole cell of another pairing.  Theorem 2.2 rules out exactly that
alignment.

### Corollary 3.1 (one-shore connected-union no-go)

Let `U` be a nonempty proper cyclic interval of any Hamilton cycle in an
`R`-cell `C`.  If `U` is a union of whole `Q`-cells each contained in `C`,
then `U` is one `Q`-cell and

\[
                              |U|=2^a                           \tag{3.3}
\]

for some `a>=0`.

#### Proof

The interval contains the Hamilton-path edges between consecutive vertices,
so its vertex set is connected in the cube graph of `C`.  Apply Theorem 2.2.
Every pair cell has power-of-two cardinality. \(\square\)

### Corollary 3.2 (residue consequence)

Let `M>s_2(r)`, put `Q_0=2^M`, and let `b` be a positive integer with

\[
                   b\equiv W_r\pmod {Q_0}.                    \tag{3.4}
\]

Then `nu_2(b)=s_2(r)`.  If a connected interval `U` as in Corollary 3.1 has
length `b`, necessarily

\[
                              b=2^{s_2(r)}.                    \tag{3.5}
\]

In particular, if the least positive residue

\[
                   \omega=W_r\bmod2^M                         \tag{3.6}
\]

is not `2^{s_2(r)}`, no interval of length `omega` can be assembled as a
union of contained cells from one other pairing.  More generally, no
residue-compatible length other than the exceptional value (3.5) can arise
from this one-shore construction.

#### Proof

Congruence modulo `2^M` preserves the exact valuation `s_2(r)`.  A power of
two having that valuation is uniquely `2^{s_2(r)}`.  Apply (3.3). \(\square\)

The result is independent of whether the Hamilton cycle itself is resident.
It therefore rules out the suggested one-shore Gray-prefix alignment even
before collar constraints are imposed.  Standard reflected Gray codes also
do not have the required long residence, but that separate defect is not
used here.

There is a stronger conclusion in the exceptional power case.

### Lemma 3.3 (small cubes cannot carry a long resident Hamilton path)

If `2<=a<D`, the cube `Q_a` has no `D`-resident Hamilton path, where internal
path residence means that two occurrences of one transition direction have
linear index distance at least `D`.

#### Proof

Such a path has `2^a-1` transition edges, all labelled by its `a` cube
directions.  If `2^a-1<D`, the entire transition word lies in one interval
of length less than `D`, so every direction occurs at most once.  This would
give `2^a-1<=a`, false for `a>=2`.

If `2^a-1>=D`, the first `D` transition edges must have distinct directions,
which requires `a>=D`.  This again contradicts `a<D`. \(\square\)

### Corollary 3.4 (complete one-shore no-go at the residence scale)

Let `M>s_2(r)`, and assume `D>=3` and `s_2(r)<D`.  No connected interval `U` with
`|U| congruent to W_r modulo 2^M` which is a union of contained cells from
one other pairing can simultaneously

1. be internally `D`-resident, and
2. have at least `D` vertices, as required by the sharp macro-block theorem.

#### Proof

Corollaries 3.1 and 3.2 force the interval to be one contained cell of
dimension exactly `a=s_2(r)`.  Its consecutive traversal inside the
`R`-cell uses only shared `R,Q` directions: the nonshared-direction argument
in Theorem 2.2 excludes an `R`-cube edge whose two endpoints both lie in the
contained cell.  The interval is therefore a Hamilton path of that
`a`-cube.

If `a<=1`, the interval has at most two vertices, fewer than `D`.  If
`2<=a<D`, Lemma 3.3 rules out internal residence. \(\square\)

Thus even the exceptional congruence `omega=2^{s_2(r)}` does not yield a
usable one-shore macro block once the residence deadline dominates the
binary digit sum, as it does asymptotically.

## 4. The surviving two-shore target

Theorem 1.1 shows that the correct positive object is not a union of cells
from one extra frame.  It is a proper nested difference

\[
                         U=B\setminus A,                       \tag{4.1}
\]

where `A` is `P`-measurable, `B` is `Q`-measurable, and `A subsetneq B`.
Equivalently, the owner edges of a residue-compatible resident interval in
the third frame must form a literal one-way dicut in `Gamma(P,Q)`.

Theorem 2.2 says that neither shore can be dispensed with when the required
length has more than one binary summand.  What remains is the following
aligned-cut problem.

> **Resident nested-difference problem.**  Choose perfect pairings
> `P,Q,R`, an `R`-cell `C`, and a resident Hamilton cycle of `C` so that one
> residue-compatible cyclic interval is `B-A` for nested measurable sets
> `A subseteq B` on the `P` and `Q` shores.

Even after such a dicut is found, whole selected cells must meet the good
dimension threshold, and the resulting path blocks still require macro Hall
and collar holonomy.  Those requirements are not consequences of the
nested-difference theorem.

The gain is a sharp elimination of a false construction route and an exact
replacement target:

\[
 \boxed{\text{not a binary union of one-shore cells, but a two-shore
 nested measurable difference carrying one resident interval.}}          \tag{4.2}
\]
