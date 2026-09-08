# A one-block coatom-order perturbation breaks the quadratic reflection fibre

Date: 2026-08-01  
Status: unconditional all-`d` local packet theorem inside the current
endpoint-planted ECO construction.  It supplies a second upper-transparent
resident move beyond the common-order reflected-pair fibre.  Global physical
slot availability and bounded terminal compiler deletion remain open.

## 0. Result

Use the first authoritative endpoint-plantable schedule, with upper screens
at zero-based transitions

\[
                         \{0,2,4,6,8,10\}.                       \tag{0.1}
\]

Write the fillers as `(f_0,...,f_d,p)`, where `p=f_(d+1)`.  The planted first
`Iab` block uses the authoritative omission order

\[
                         p,f_1,\ldots,f_d,f_0,
\]

and every other active block normally lists the coatom omissions in the
order

\[
                    f_0,f_1,f_2,f_3,\ldots,f_{d+1}.
\]

Change only the **label-attached** `Ica` block, in both ECO phases, to

\[
                    f_0,f_2,f_1,f_3,\ldots,f_{d+1}.              \tag{0.2}
\]

For every `d>=2` and `r>=d+4`, the resulting two tensor phases still have:

1. the same distinct rank-`r` owner set and the same endpoints;
2. simple Johnson-path topology;
3. equal immediate lower and upper palette multisets;
4. equal pointwise prefix/suffix OR signatures;
5. equal complete internal interval-OR support;
6. identical clipped residence boundary state; and
7. no internal positive coordinate run shorter than `d+1`.

For every `d>=3`, however, this packet does **not** preserve the reflected
pair current between depths `2` and `d`.  It therefore escapes the quadratic
fibre preserved by every common-order mixed-screen packet.

The same perturbation works with the second planted schedule
`{0,2,3,4,6,8,10}`.  The first schedule is fixed here for the cleanest
formula.  This is the first authenticated reflection-breaking packet in the
additive-constant programme.

## 1. Fixed-endpoint coatom reorder lemma

Let `B(V,pi)` be the block consisting of all coatoms of a filler set `F`,
with fixed active label `V`, listed in order `pi`.  Suppose two orders `pi`
and `pi'` have the same first and last omissions.

### Lemma 1.1

Replacing `B(V,pi)` by `B(V,pi')` preserves:

* the block owner set and endpoints;
* simple Johnson adjacency inside the block and at both exterior screens;
* the pointwise block prefix/suffix OR signatures; and
* the complete distinct interval-OR support in every fixed exterior context.

#### Proof

All coatoms remain present once, so the owner set is unchanged.  Two
different coatoms differ in exactly two filler coordinates, hence every
consecutive pair in either ordering is a Johnson edge.  Fixed first/last
coatoms preserve both screen attachments.

A singleton interval in the block is one coatom, so the singleton support is
the same set.  The union of any two distinct filler coatoms is the full
filler set `F`; consequently every interval of length at least two wholly
inside the block has value `V union F`.  Likewise, a block prefix or suffix
has its endpoint coatom at length one and `V union F` thereafter.  The
prefix/suffix/internal deck replacement theorem now gives equality in every
exterior context. \(\square\)

Order (0.2) fixes `f_0` and `p=f_(d+1)`, so Lemma 1.1 applies separately to
the two already endpoint-planted ECO phases.  Both modified phases therefore
have the same OR support because the two untwisted planted phases did.

The screen owners themselves are literally unchanged.  Lower screens use
all of `F`; every planted upper screen has filler part `F-{p,f_0}`.  The
modified `Ica` block
occurs once in each phase, so its changed internal q1-intersection multiset
is added equally to both phases.  This proves rows 1--5 above.

## 2. Residence remains exact

Every internal filler coordinate is present at every screen.  If its zero
occurs at position `p_L` in one coatom block and position `p_R` in the next,
the positive run between those zeros has length

\[
                         (d+2)-p_L+p_R.                         \tag{2.1}
\]

The adjacent swap in (0.2) changes `p` by at most one.  Hence the two
affected incoming/outgoing runs have length at least

\[
                              (d+2)-1=d+1.                       \tag{2.2}
\]

All other runs are canonical.  The modified block is internal and its first
and last coatoms are fixed, so the clipped global boundary state is also
unchanged.  This proves rows 6--7.

## 3. Exact reflection defect

Let `Delta_q^0` be the signed old-to-new depth-`q` intersection-occurrence
change for the canonical packet and `Delta_q^*` that of (0.2).  Put

\[
                              R_q=\Delta_q^*-\Delta_q^0.
\]

Only intersection windows which contain exactly one of the two swapped
coatoms can change.  Internal-block windows occur identically in the two ECO
phases and cancel.  Directly substituting the old left/right contexts of the
`Ica` block and the new ones leaves, at the two extreme depths,

\[
\begin{aligned}
 R_2={}&[G_2\cup\{a,f_1\}]+[G_2\cup\{p,f_2\}]\\
      &-[G_2\cup\{a,f_2\}]-[G_2\cup\{p,f_1\}],               \tag{3.1}\\
 G_2={}&K\cup\{\mathord\infty,c,f_3,\ldots,f_d\},\\[1mm]
 R_d={}&[G_d\cup\{a,f_1\}]+[G_d\cup\{f_0,f_2\}]\\
      &-[G_d\cup\{a,f_2\}]-[G_d\cup\{f_0,f_1\}],             \tag{3.2}\\
 G_d={}&K\cup\{\mathord\infty,c\}.
\end{aligned}
\]

Both are unit Johnson rectangles, but on different active/filler label
pairs.  The canonical currents obey

\[
                 \deg^{(2)}(\Delta_2^0)=\deg^{(2)}(\Delta_d^0).
\]

Subtracting the pair currents of (3.1)--(3.2), the modified reflected defect
is

\[
              [f_0f_1]-[f_0f_2]-[pf_1]+[pf_2].                 \tag{3.3}
\]

The four coordinate pairs in (3.3) are distinct for `d>=3`, so the vector
is nonzero.  Therefore

\[
 \deg^{(2)}(\Delta_2^*)\ne\deg^{(2)}(\Delta_d^*),               \tag{3.4}
\]

and the packet breaks the reflected-pair invariant.

## 4. Why this matters

The schedule-classification theorem shows that all sixteen common-order
mixed-screen choices preserve reflection.  The obstruction came from using
one identical filler flag in every active block, not from coatom thickening
itself.

Packet (0.2) retains the full upper/residence safety interface while adding
a genuinely new quadratic current.  The next algebraic question is now
concrete:

> characterize the combined all-depth occurrence lattice generated by the
> canonical maximal-chain packets and the one-block-order breakers.

If the combined lattice is the product of the per-depth fixed-point-degree
kernels, the quadratic serial obstruction disappears completely.  Physical
planting and compiler augmenting linkage would then be the only remaining
local-to-global gates.

## 5. Audit

The dependency-free replay verifies every row above for `2<=d<=32`, with
literal occurrence multiplicities and the exact four-pair vector (3.3):

```text
scratch/audit_coatom_single_block_order_reflection_breaker_20260801.py
scratch/coatom_single_block_order_reflection_breaker_20260801.audit.json
```

It reports

```text
PASS_COATOM_SINGLE_BLOCK_ORDER_REFLECTION_BREAKER
```

with canonical payload SHA-256

```text
d549ae255a20bf81b89f9ae7dd62875b173096e8069302f873ceef5439501025
```
