# The untouched Catalan rail is an independent filler, not an inherited copy

Date: 2026-07-31  
Status: exact all-parameter substitution theorem; independently replayed on
the chained strict constructions at child parameters `n=3,4,5,6`; no guarded
filler-existence theorem is claimed

## 0. Result

In the direct edgewise two-coordinate recursion, let `F` be the child
Catalan linear forest used to define the puncture set `Q`, the two strict
side occurrence systems, the `z`-rail, and the two seam families.  Previous
accounts also put a literal copy of `F` on the disjoint `c`-rail.

That last identification is unnecessary.

> **Independent `c`-rail filler theorem.**  Let `G` be any other Catalan
> linear forest at the same parameter on the same old ground set.  Replace
> the translated child rail
>
> \[
>                         c+F
> \]
>
> by `c+G`, leaving `Q`, both side representative systems, the punctured
> `z`-rail, and both seam families unchanged.  Then every lower and upper
> palette remains exact.  Moreover, the complete physical support is a
> linear forest if and only if `G` and the remaining three-sector support
> are linear forests.  Its number of components is unchanged.

Thus the strict construction is intrinsically a **two-parent recursion**:
`F` supplies the direct-incidence and puncture geometry, while an
independently chosen `G` supplies the isolated `c`-rail chronology.

This removes a false coupling from the residence interface.  Internal
residence defects on the `c`-rail are inherited from `G`, not necessarily
from the structural parent `F`.  It does not by itself construct a
next-depth-safe `G`, and therefore does not finish guarded induction.

## 1. Setup

Let the old ground set be `Omega`, `|Omega|=2n`.  A Catalan linear forest
has middle vertices `binom(Omega,n)`, exactly one physical edge of every
lower colour in `binom(Omega,n-1)`, and exactly one physical edge of every
upper colour in `binom(Omega,n+1)`.

Adjoin two coordinates `c,z`.  The four middle-vertex sectors are

\[
\begin{array}{c|c}
0&\binom\Omega{n+1}\\
c&c+\binom\Omega n\\
z&z+\binom\Omega n\\
cz&c+z+\binom\Omega{n-1}.
\end{array}                                           \tag{1.1}
\]

The strict direct-edgewise construction based on `F` uses:

1. the pure upper side in sector `0`;
2. a translated Catalan rail in sector `c`;
3. the punctured copy `z+(F-Q)` in sector `z`;
4. the pure lower side in sector `cz`; and
5. seams only of types `0-z` and `z-cz`.

In particular, no seam and no side edge is incident with a vertex of the
form `c+T` with `T in binom(Omega,n)`.

## 2. Exact substitution theorem

### Theorem 2.1 (independent filler)

Suppose the choices based on `F` satisfy the four exact strict palettes of
the direct-edgewise normal form.  Let `G` be any Catalan linear forest at
parameter `n`.  Form `H(F,G)` by using `c+G` in the `c`-sector and retaining
all other atoms from the construction based on `F`.

Then:

1. every ambient rank-`n` lower colour occurs exactly once;
2. every ambient rank-`n+2` upper colour occurs exactly once;
3. the `c`-sector is a union of connected components disjoint from every
   other sector;
4. `H(F,G)` is a linear forest exactly when `G` and the complementary
   three-sector support are linear forests; and
5. if `G` has `K=Cat_n` components and the three-sector support has
   `Cat_{n+1}-K` components, then `H(F,G)` has `Cat_{n+1}` components.

#### Proof

An edge `T--T'` of `G` has lower and upper colours

\[
                       L=T\cap T',\qquad U=T\cup T'.
\]

After adjoining `c`, its colours are `c+L` and `c+U`.  Since `G` uses every
old lower and upper colour exactly once, `c+G` uses exactly the two palette
banks

\[
 c+\binom\Omega{n-1},\qquad c+\binom\Omega{n+1}.      \tag{2.1}
\]

These are precisely the banks used by `c+F`; all other ambient colour
banks are disjoint from (2.1).  Replacing `c+F` by `c+G` therefore changes
neither the multiplicity nor the support of any ambient palette.

By (1.1), `c+G` lies on the vertex set `c+binom(Omega,n)`.  The list of
allowed seams shows that no edge outside this rail meets that vertex set.
Consequently `c+G` is a union of entire connected components.  Degrees,
cycles, and component counts are therefore direct sums of those of `G`
and of the remaining three-sector support.  This proves (3)--(5), and
(1)--(2) were proved by the palette partition.  `square`

### Corollary 2.2 (residence decoupling)

For every old coordinate `x`, its binary trace on a `c`-sector component
is exactly its trace on the corresponding component of `G`.  The new
coordinates are constant there: `c=1` and `z=0`.

Hence every body-residence predicate on that rail may be imposed on `G`
independently of the common basis and side representatives chosen from
`F`.

This corollary only decouples the quantifiers.  A guarded induction still
needs a supply theorem producing a filler `G` safe at the output guard,
plus motif-safe `z` and side sectors and legal seam records.

## 3. Corrected recursive target

The direct guarded gate can now be stated without the artificial equation
`G=F`:

> Given a structural Catalan forest `F` and a guarded filler Catalan forest
> `G` at the same parameter, choose `Q` and both direct side SDRs from `F`
> so that the three-sector support is a guarded linear forest.  Then
> `H(F,G)` is the next Catalan forest, with the `c`-rail guard inherited
> solely from `G`.

There are still two genuine existence questions:

* whether the strict common-basis/graphic/motif choice exists for the
  structural parent; and
* whether a right-total bank of guarded fillers exists as the required
  residence depth grows.

The theorem proves that those questions need not be solved by one and the
same child object.  In particular, the copied-`c` obstruction in the
one-parent chained witness is evidence against that one-parent choice, not
against the direct collar itself.

## 4. Independent finite replay

The standard-library audit

```text
scratch/audit_catalan_independent_c_rail_filler_20260731.py
```

loads the authenticated chained witness

```text
scratch/catalan_direct_edgewise_side_lift_recursive_n3_n6_20260731.witness.json
```

at child parameters `n=3,4,5,6`.  In each case it replaces the `c`-rail by
the coordinate-rotation image of the supplied child forest.  This is a
genuinely different physical edge set in every audited case.  It then
reconstructs the full ambient support and checks, without trusting the
witness claims:

* all ambient lower and upper colours occur exactly once;
* maximum physical degree is two;
* the support is acyclic; and
* the component count is respectively `14,42,132,429`.

The audit writes

```text
scratch/catalan_independent_c_rail_filler_20260731.audit.json
```

No search or external solver is used.

## 5. Guarded sequel

The exact residence factorization, the finite-bank sealed-ancestry
obstruction, the guard-jump promotion reduction, and the antipodal-geodesic
universal-filler target are proved separately in

```text
MATH_THEOREM_CATALAN_INDEPENDENT_FILLER_GUARD_FACTORIZATION_20260731.md
```

That sequel also replays the known residence-clean parameter-five forest as
an independent filler and removes exactly the `44` inherited `c`-rail
minimum-three clauses.  It does not promote the present substitution theorem
to an all-parameter guarded construction.
