# Independent audit: the complete fixed-root entrance bank cannot be retained

Date: 2026-09-09. **PASS, pure proof. No execution or search.**

Independently derived the argument below, then read the complete
[induction-agent proof](Q3_ALL_ROOT_ENTRANCE_BANK_FORCES_ONE_STEP_RUNS_20260909.md).
The local obstruction, all possible arrivals (including either new coordinate),
the boundary case r=1, and the quantitative matching-injectivity strengthening
all check. Root supplied the obstruction family and the stronger global count.

## 1. Exact hypotheses

There are `2r+1` old positions, followed by two new positions a,b; r>=1.
Write u,x,y for the first three old positions. Child lower states have rank
r+1 and child upper states rankr+2. The outgoing matching is canonical Phi:
add the zero at the first global minimum of the ones-minus-zeros prefix walk.

A complete factor has one predecessor and one successor at every child
lower state, using each outgoing Phi upper once. A successor is a different
facet of that upper: the return along the outgoing matching edge to its own
lower state is excluded. Every closed positive coordinate run is required
to have length at least2. Hamiltonicity is unnecessary; the argument applies
to any such complete strict cycle cover.

For each Dyck word D' of semilengthr, the prescribed root entrance is

\[
(0D')+a\longrightarrow 1D'\quad\text{in sector }00.
\]

Its upper is `(1D')+a`, and it occupies the incoming socket of `1D'00`.
The head family H consists exactly of old words of rankr+1 whose every
nonempty prefix is strictly positive. It has sizeCat_r.

## 2. First-minimum/last-minimum inverse, with endpoint conventions

For an upper word of total height+1, let j be the position immediately after
the **last** global minimum, allowing the empty prefix. This position exists
because the final height+1 is above the minimum, and its step is upward.
Deleting that bit lowers all later heights by2. Before j the heights are at
least the old minimum; at j the new height is one less than that minimum;
afterward they are at least this new value. Thus j is the first new global
minimum, and canonical Phi restores the deleted bit.

Conversely, flipping a lower word's first-minimum zero raises the entire
suffix by2. The upper's last minimum is immediately before the flipped
position. This proves uniqueness and handles the case where the last
minimum is the empty prefix.

## 3. A critical lower state and all its possible successors

Fix any Dyck word D of semilengthr−1 and append the new bits00 to

\[
Z=111D,\qquad U=011D,\qquad V=101D.
\]

The outgoing upper of U00 is Z00: U first attains its minimum−1 at u.
All upper facets are obtained by deleting one of Z's old ones:

* Delete u: the forbidden self-successor U00.
* Delete x: V00, whose old prefix heights begin1,0,1, so it is not in H.
* Delete y: `110D00`, whose nonempty old heights are all at least1, so it is
  in H.
* Delete a one in D: before deletion the old heights are positive; afterward
  they are `1 +` the corresponding Dyck prefix height, again at least1.
  These heads are also in H.

There are no new-coordinate facets because Z00 contains neither a nor b.
The last two cases give exactlyr distinct heads

\[
H_Z=\{Z-t:t\in Z\setminus\{u,x\}\}\subset H.
\]

If every prescribed root entrance is retained, all heads in H_Z already
have their incoming edge. The only nonself successor available to U is
therefore V, which insertsu and deletesx.

## 4. Complete arrival classification forces x to have age1

Every upper capable of entering U00 is `(U00)+z` with z absent from U00.
The possibilities are u, a zero coordinate of D, a, and b; this list is
exhaustive.

For z=u, the upper is Z00. All its nonempty prefixes are positive (old
prefixes start1,2,3 and remain at least3; the new zeros finish at2,1).
Its last minimum is the empty prefix, so its Phi preimage is U00. This is
the excluded self-return.

For every other z, the upper's minimum−1 is attained **only at old position
u**. The first old heights are−1,0,1. Adding an old zero in D raises a later
suffix and leaves all following old heights at least1; its final new-zero
heights are2,1. Adding a gives final heights2,1; adding b gives0,1. None of
these cases returns to−1 after u.

The inverse matching therefore removes x, the up-step immediately after u.
The incoming lower source is exactly `(U00+z)−x`, which omitsx. Every nonself
arrival at U thus insertsx freshly. Consequently the successor U→V would
give a lower-coordinate pattern `0,1,0`, a positive run of length1. This
violates residence at least2.

The calculation includes r=1, where D is empty and the old-zero cases simply
disappear. No assumption about the selected Hall facets, parent history,
unused sectors, or eventual topology enters the contradiction.

## 5. Matching injectivity gives the stronger global count

The preceding arrival statement holds even when some prescribed root
entrances have been removed. In **every** complete strict residence-at-least2
canonical-Phi factor, U cannot use either its self facet or V. It must use
a head in H_Z.

As D ranges over all Cat_(r−1) Dyck words, the critical lower states U and
uppers Z are distinct. Their chosen successor heads must also be distinct,
because the incoming matching has degree one. Each chosen head excludes
its prescribed root entrance. Hence at least

\[
\boxed{\mathrm{Cat}_{r-1}}
\]

of the Cat_r prescribed first-entrance incidences must be omitted, replaced,
or reopened. The exact proportion is

\[
\frac{\mathrm{Cat}_{r-1}}{\mathrm{Cat}_r}
=\frac{r+1}{2(2r-1)}\longrightarrow\frac14.
\]

This is a matching constraint, stronger than merely requiring one unreserved
head in each individual H_Z. For the old19-to-child21 instance it requires
at leastCat_8=1430 ofCat_9=4862 root incidences to change, a proportion5/17.
These are exact symbolic Catalan values, not a new finite census.

The direct injection `D↦110D` supplies distinct permissible heads for this
particular family. Freeing these heads resolves its distinct-head condition;
it does not prove residence-three continuation or completion of the rest
of the factor.

## 6. Consequence and exact scope

The previous q3 excursions remain valid as disjoint, locally legal partial
paths. The [explicit whole01-strip extension](COMPLETE_CANONICAL_PHI_SECTOR_LAW_AND_EXPLICIT_01_STRIP_EXTENSION_20260909.md)
also remains a valid partial incidence construction. But both retain all
the forbidden root entrance bank, so they cannot be completed into a spanning
strict canonical-Phi factor of residence at least2 without reopening some
of those entrances. Merely assigning more unused states or changing later
Hall facets cannot fix this obstruction while the first incidences remain.

This does **not** disprove canonical-Phi factors generally, noncanonical
factors, alternate root-port selections, finite linear words whose endpoints
escape a cyclic condition, optimal21 words, or all-dimensional equality.
It establishes a necessary change to this specific induction architecture.
