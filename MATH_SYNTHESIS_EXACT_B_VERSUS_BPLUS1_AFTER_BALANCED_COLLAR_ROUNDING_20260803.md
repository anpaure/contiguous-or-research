# Exact `B` versus `B+1` after balanced collar rounding

**Date:** 2026-08-03  
**Status:** proof-safe synthesis of the new unconditional theorems and the
two surviving construction branches.  This note proves conditional
implications only.  It does not prove `nu(k)=B(k)+O(1)`.

## 0. Current status

The verified finite result remains

\[
                  \nu(k)=B(k)\qquad(0\le k\le16),
\]

and the first unresolved value remains

\[
                  24313=B(17)\le\nu(17)\le25746.
\]

For the all-dimensional problem, every scalar and anonymous lower-rank
row is now exact.  What remains is occurrence-labelled correlation.

## 1. What is now unconditional on the lower side

Let `W` be the middle-layer width and `d=d(k)` the lower-bound deadline.
The following four statements are proved.

1. The complete optimal collar/residual rank inventory decomposes exactly
   into `W` noncontiguous rank patterns of maximum size `d`, with equitable
   loads and no forbidden adjacent residual ranks.
2. Separately, every prescribed named rank target can be assigned to a
   distinct containing owner/rank port, with the same equitable owner-load
   histogram.  This is an ordinary two-matroid intersection.
3. Every named target below a `(7/8+o(1))sqrt(r)` collar has an exact
   literal nonadjacent flag factor on distinct owners.
4. For arbitrary residual matching-rank marginals and arbitrary collar
   columns, the two banks have an exact anonymous joint decomposition whose
   row loads differ by at most one.  Thus total mass at most `dW` fits at
   depth `d` with no additive scalar slack.

These are four projections of one desired object.  None identifies the
anonymous rows in item 4 with actual owners while simultaneously making
their named targets one inclusion flag.

### Exact lower gate

The remaining lower theorem is therefore:

> **Balanced named-flag theorem.**  The optimal anonymous joint rank rows
> can be assigned bijectively to the middle owners, and every occurrence
> in a row can be assigned to a distinct named target contained in that
> owner, so that the targets of the row form one inclusion flag.

Equivalently, the full pattern/owner/order/named-target configuration
hypergraph has a matching saturating every pattern and owner and using the
required number of every target rank.

The canonical fractional matching exists and its retained nonadjacent band
has normalized pair scale `O(r^-2)`.  The published fixed-uniformity
Delcourt--Postle and Joos--Mubayi--Smith black boxes do not apply directly
to the growing-rank labelled host.  A tailored cross-SCD absorber or a new
growing-uniformity laminar-flag theorem is still required.

## 2. Two lower constructions which are now rigorously excluded

The following failures are architecture-specific, not lower bounds against
the balanced named-flag theorem.

1. Any construction whose flags only split one fixed SCD omits
   `Omega(W)` targets.
2. The exact sparse parity-block residual factor cannot be attached to the
   collar while its chunks remain intact.  Its positive-density family of
   full length-`d` chunks is forced to carry
   `Omega(sqrt(r)W)` collar incidences.  Consequently every fixed additive
   slack fails on that whole-chunk face, and a remainder-preserving repair
   must migrate `Omega(sqrt(r)W)` target incidences.

The second statement does not contradict anonymous exact depth `d`:
equitable residual loading minimizes every collar Gale cut.  It proves that
the residual and collar flags must be constructed jointly, rather than by
repairing the parity-block factor afterward.

## 3. The exact-`B` branch

On the odd owner layer, fix a first perfect incidence factor.  The second
factor problem is exactly a perfect matching in the residual regular
digraph whose upper-colour multiplicities all lie in `{1,2}`.  Its displayed
LP has the canonical feasible point `x_e=1/(m-1)`.  Integrally, it is
equivalent to

\[
 \boxed{\text{one rainbow representative of every upper colour}
        +\text{a vertex-disjoint rainbow residual completion}.}
\]

The two marginal colour SDRs always exist, but occurrence correlation is
not automatic.  Prospective Boolean `C6` supply is cubic; an incumbent can
use a `C6` only when its local pointer has the corresponding directed
3-cycle.  Thus raw support count does not prove energy descent.

If an upper-surjective cyclic simple owner row is obtained, the first-exit
construction gives a deterministic pair of disjoint terminal occurrences
at every seam.  Two-coordinate capacity then reduces to one ordinary Hall
graph, and one linear opening loses exactly two bundles.

However, direct canonical terminal acceptance is impossible.  A folded-C8
cross ticket is an incomparable pair in opposite phases; a first-exit pair
is a nested Hasse pair in one phase.  Hence the literal direct acceptance
graph is empty.  The exact-`B` branch still requires a protected
value-and-phase converter, transported background, and the regenerative
same-parity overlay.

## 4. The `B+1` pivot branch bypasses the converter

The monotone-pivot construction provides a different terminal interface.
One inserted nonempty letter, at a protected sharp-aperture geodesic,

* preserves every old contiguous-OR value;
* replaces the local nonflat crossing band by the required flat owner
  geodesic;
* creates one singleton and two complete nested lower rays; and
* compiles those ray targets with zero local residual deficiency once the
  transported background matching is fixed away from them.

At owner level the correct `B+1` certificate is an upper-surjective
alternating Hamilton **path**, not a closed cap-two factor.  Relative to a
first perfect matching it is exactly

\[
 \boxed{\text{rooted upper-exact Catalan forest}
        +\text{a free-port Hamilton path through its components}.}
\]

The depth row has `W` owner cells plus one controlled boundary nonowner.
Thus this branch does not use the folded-C8 terminal tickets and does not
need a first-exit value/phase converter.

### Conditional `B+1` implication

For a fixed dimension, suppose one constructs a literal source of length
`B(k)+1` satisfying all of the following in one state.

1. Its depth-`d` row consists of every middle owner once in the protected
   upper-surjective Hamilton-path order, plus one controlled boundary
   nonowner.
2. The row contains the protected pivot geodesic and its resident collar.
3. Every strict-lower target outside the pivot singleton/rays has a
   transported literal matching, and the ray targets are assigned to the
   pivot cells.
4. Every upper target has a retained interval witness, and every internal
   coordinate run satisfies residence.
5. The boundary nonowner supplies or routes the unique missing endpoint
   `q1` obligation and passes the common cap/erosion state.

Then the monotone-insertion transport theorem, exact pivot-ray compiler,
and Hamilton-path owner certificate give a universal word of length
`B(k)+1`.  Hence

\[
                         \nu(k)\le B(k)+1.
\]

This is a conditional implication.  The protected Catalan path, nonflat
source antecedent, balanced named lower flag, all-width witnesses, and
residence must coexist; no current theorem supplies that intersection.

## 5. Shortest honest all-dimensional target

For an additive theorem, the `B+1` branch currently has the shorter list.
It needs three correlated constructions.

1. **Balanced named flags:** lift the exact anonymous collar/residual rows
   to literal ownerwise inclusion flags.
2. **Protected Catalan path:** build the upper-exact Hamilton path while
   containing the pivot collar and prescribed endpoint types.
3. **Regenerative source lift:** produce the nonflat antecedent, preserve
   arbitrary-width upper witnesses and residence, and export only bounded
   state to the next same-parity dimension.

The exact-`B` branch replaces the pivot/nonowner interface by a cap-two
Hamilton cycle and a protected first-exit type converter.  It is therefore
strictly stronger at the terminal interface, though it may remain useful
for proving exact equality.

The next proof effort for `B(k)+O(1)` should prioritize the balanced
named-flag theorem and the protected Catalan path.  More local repair of the
parity chunks or more untyped terminal sockets cannot close the audited
gates.
