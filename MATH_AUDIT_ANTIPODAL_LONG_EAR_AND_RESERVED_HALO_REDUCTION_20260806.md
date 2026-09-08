# Proof audit: antipodal long ears and reserved external halos

**Date:** 2026-08-06  
**Primary files:**

* `MATH_THEOREM_ANTIPODAL_FOLDED_CUBE_LONG_EAR_REDUCTION_20260806.md`,
  SHA-256
  `0361549889b944b399f16f95a279bc0a5d65f4e25d56db0f62c8d34bd4cf575e`;
* `MATH_THEOREM_ANTIPODAL_EAR_RESERVED_HALOS_AND_PORT_QUANTIFIER_GATE_20260806.md`,
  SHA-256
  `7c83f6259e4c51ff3e8098da5b3dcb7a9b1f01779e7c35f987d81442bf18fd23`.

**Method:** independent symbolic audit of trace distances, endpoint
intersections, geodesic prefix laws, residence, and palette projections;
no computation or search  
**Verdict:** GO for the folded-cube order, minimum-intersection prospective
ports, random-geodesic aperture, and the reserved external-halo theorem.
The advertised global ear packing remains conditional.  The prospective
minimum-intersection port quantifier is removed by the inherited-port
dwell recurrence; the exact first missing statement is now joint private
endpoint-halo selection.

## 1. Folded-cube trace order

Representatives avoiding coordinate `m` are exactly an `(m-1)`-cube.  In
the expanded word `R_i,bar R_i`, the internal pair distance is `m`, and

\[
 |\bar R_i\mathbin\triangle R_{i+1}|=m-1
\]

because `R_i,R_(i+1)` differ once.  Deleting the adjacent pair
`emptyset,E` creates the seam from the complement of one singleton to a
different singleton.  Its distance is `m-2`.  This verifies Theorem 1.1,
including the cyclic closing seam.

## 2. Prospective endpoint intersection

For a complement seam, the two required `K`-set sizes sum to `m` in an
`(m-1)`-set, so minimum `K`-intersection is one and external intersection
is zero.

For `bar S -> S triangle {e}`:

* if `e notin S`, external intersection is `{e}` and the two `K` sizes sum
  to `m-1`;
* if `e in S`, external intersection is empty and the two `K` sizes sum to
  `m+1`.

Thus total intersection is respectively one or two.  At the seam created
by deleting `emptyset,E`, both contributions are one.  Lemma 2.1 is exact.

Its quantifier is existential **per seam**, so by itself it does not bind
the two port requests incident with one trace to one physical witness.
The inherited-port recurrence repairs this: prescribe the incoming
`K`-window, choose a cyclic order containing it as a window, and use an
incident cyclic window as the outgoing port.  For arbitrary consecutive
ports, external intersection is at most one and `K` intersection at most
the smaller port size, which is at most `(m+1)/2`.  Thus the physical ear
distance remains at least `m/2-2`, and after the two halos it remains
`Omega(m)`.  Theorem 4.1 is exact.

## 3. Random-geodesic probabilities

At owner level `s`, a monotone geodesic independently chooses an unordered
deleted prefix and inserted prefix, both of size `s`.  The law is uniform
on `binom(q,s)^2` compatible owners.  At an edge it chooses prefix sizes
`s,s+1`, giving the product in the palette formula.  Lemma 3.1 is exact;
the displayed `square` at its end is only a typographical TeX omission.

## 4. Central external aperture

For a retained representative satisfying

\[
 2d+1\le |S|\le m-2d-1,
\]

both directional external differences at a complement seam are at least
`2d`.  At the other seam, one of the two sizes loses exactly one, which is
why the strict one-unit margin in the displayed band is necessary.  The
deleted binomial tails are `2^{o(m)}` at `d=O(sqrt(m))`.

The first and last `d` external swaps use disjoint coordinates.  They keep
the `K`-projection literally constant and leave equal residual deletion
and insertion banks of size `q-2d`.  Hence the middle segment is again an
unconditioned uniform monotone geodesic on those residual banks, proving
the exact conditioned probabilities rather than only an asymptotic bound.

## 5. Residence and local palettes

Every `K` bit is frozen for `d` owners adjacent to each port.  This is
exactly stronger than every nested split endpoint flag, whose requested
extension is at most `d`.

Every external coordinate changes at most once on the full monotone ear.
The adjacent fixed-trace block has length at least `d+1`; therefore no
positive run or zero gap meeting the seam is short.

At an external swap `S -> S-x+y`, the lower and upper palette projections
are `S-x` and `S+y`.  They are neither the old nor the new owner trace.
Because at least `d` external changes remain outside either halo, no proper
halo state reaches the opposite endpoint trace early.  Thus these roles
cannot collide with an adjacent fixed-trace witness palette.  This verifies
Theorem 2.1.

## 6. Endpoint blocking audit

For a frozen oriented port `A_i -> B_i`, the first lower colour is always
`A_i-x` for some `x in A_i-B_i`.  Forbidding those `q_i` facets blocks the
entire first-step menu, independently of the insertion.  Across
`Theta(2^m)` distance-`Theta(m)` ports this costs only `O(m2^m)` roles.

Therefore the ambient/used cardinality comparison cannot establish private
halos after ports have been frozen.  This obstruction does not refute a
joint port-and-background selection; it fixes its order of quantifiers.

## 7. Proof-safe frontier

Unconditional:

1. all central seams are almost antipodal in external trace;
2. arbitrary inherited ports are realized by one physical opened dwell;
3. the resulting owner ports retain distance at least `m/2-O(1)`;
4. residence can be paid entirely in two deterministic external halos;
5. the free middle retains distance `Omega(m)` and exact exponential
   aperture.

Still required:

1. select first palette tickets jointly with the background, defeating the
   facet blocker;
2. pack the free middle geodesics against the resulting fixed bank; and
3. retain the all-width PBBS and terminal-cap interfaces.

No statement in either audited file proves `nu(k)<=B(k)+O(1)`.

## 8. Independent audit of the inherited-port recurrence

An arbitrary `h`-subset `P` of `K` can be made a cyclic `h`-window, and
any prescribed Johnson neighbour of `P` can be made its incident window.
Thus the incoming port may be inherited from the preceding ear and the
outgoing port taken from one physical opened dwell.

At every antipodal or near-antipodal seam, the trace-size sum lies in
`{m-1,m,m+1}` and external intersection has size at most one.  Hence the
two arbitrary `K`-port sizes also sum to one of those three values, their
intersection is at most `(m+1)/2`, and total owner intersection is at most
`m/2+2`.  The resulting distance bound `m/2-2`, and its residual
`m/2-O(d)` after halo reservation, are correct.  This removes the two-port
quantifier noted in the earlier sections of this audit.

## 9. Independent audit of fork separation

In the undeleted antipodal word, the predecessor and successor of every
trace differ in exactly one external coordinate.  The `2^{o(m)}` tail
deletions create only `2^{o(m)}` exceptional splice positions, which are
explicitly excluded from the central theorem.

At a central fork, flip the distinguishing coordinate on the disagreeing
branch first and hold it forever on the agreeing branch.  Pair it with a
second coordinate of the opposite direction, and delay that second flip
to the final transition of the agreeing branch.  After the first edge the
distinguishing bit separates every owner and internal palette role.  On
the first edge itself, the two-bit patterns are `(0,0)` and `(1,1)`, while
the agreeing branch remains `(1,0)` until its last edge.  At that last edge
its other external coordinates are within one swap of a near-complement
of the central trace, so it cannot equal the exceptional first-edge role.
Lemma 8.1 is proof-safe.

## 10. Independent audit of the birthday calculation

For complementary free endpoints, the weighted number of starts reaching
one trace at a fixed deletion/insertion profile is

\[
 {\binom s\beta\binom{M-s}\alpha
  \over\binom u\alpha\binom{M-u}\beta}
 ={\binom M u\over\binom M s}.
\]

The rank-monotone type word keeps `s` between complementary endpoint
ranks, so unimodality bounds the ratio by one.  Naming at most two common
or absent coordinates, the stage, and a palette offset introduces only a
polynomial number of classes and a polynomial adjacent-binomial factor.
The external load bound is therefore polynomial.

`Sym(K)` invariance makes every conditional `K`-projection uniform.  The
three reciprocal-layer sums used in the collision estimate are exactly

\[
 \sum_{s=1}^m{\binom ms\over\binom{m-1}{s-1}}=mH_m,
\]

\[
 \sum_{s=0}^{m-1}{\binom ms\over\binom{m-1}s}=mH_m,
\]

and

\[
 \sum_{s=2}^m{\binom ms\over\binom{m-1}{s-2}}=O(m^2).
\]

All nonlocal role pairs use independent macro variables.  The only
overlapping-variable pairs are an ear with its incident dwell (already
locally fresh) and the two incident ears (fork-separated).  Hence expected
collision count is polynomial, and deleting both incident macros per bad
pair costs only polynomially many macros.

The alteration does not itself repair those macros.  The exact new gate is
the polynomial repair lemma, with ports and first facets reselected jointly
against the frozen good bank.

## 11. The internal repair lemma is superseded by LLL

Every retained central owner or palette role has a `K`-projection in a
layer of size at least

\[
 N_*=\binom{m-1}{2d-1}=m^{\Omega(d)}.
\]

Combining this with the polynomial external-load bound gives a uniform
point-load bound `m^C/N_*`.  After one object is fixed, summing collision
probabilities over all other nonlocal objects therefore costs at most
`epsilon_m=m^(C+1)/N_*=o(1)`.

The dependency graph is local in the base variables: one ear uses only the
variables of its two endpoint dwells and its private middle order.  A
collision event can depend on another only through a constant number of
neighbouring object indices.  Hence its dependency-neighbourhood
probability sum is `O(epsilon_m)`.  Taking `x_e=2Pr(B_e)` verifies the
asymmetric local-lemma inequality once that sum is below `1/2`.

The two families of potentially nonindependent local comparisons were
already removed exactly: incident ear--dwell roles are fixed-trace fresh,
and the two ears around one dwell are fork-separated.  Thus Theorem 11.2
correctly upgrades the polynomial alteration to a collision-free internal
bank.

This does not automatically include an arbitrary frozen PBBS or terminal
cap bank.  Such a bank needs its own point-load bound or must be co-selected
by the existing halo-separation mechanism.

## 12. Low-cycle relative avoidance

The low rolling-collar cycle has at most

\[
 m^{O(1)}(2em/d)^d
\]

owner and immediate-palette roles.  A central random macro hits one fixed
role with probability at most `1/N_*`, so its unary collision probability
is at most the displayed size times `m^{O(1)}/N_*`.  Since

\[
 N_*\ge((m-1)/(2d-1))^{2d-1},
\]

the logarithm of this ratio is
`-d log(m/d)+O(d)`, which tends to negative infinity.  The unary events
have the same local base-variable dependency as the pair events.  Adding
them to the asymmetric LLL is therefore valid.

## 13. Ore-halo extension

One macro has `O(m)` incidences and `O(m^2)` roles in its enlarged Ore
halo.  Every added role changes the external trace and physical rank by at
most one.  Therefore the polynomial external-load theorem survives with a
polynomially larger exponent, while every conditional `K` fibre still has
size at least

\[
                         \binom{m-1}{2d-2}.
\]

This is superpolynomial, so the extra polynomial factor in the LLL degree
is harmless.  Lemma 13.1 correctly upgrades direct role privacy to
nonlocal full-halo privacy.

## 14. Co-selection with the protected reservoir

For the deterministic top/low reservoir, one path contributes only
polynomially many halo roles to its trace and its Hamming-one neighbours.
Thus maximum obstacle load per external trace is polynomial.  The rolling
low cycle is handled by Section 12.

The high-tail paths may be selected after the central bank.  One candidate
halo has only `m^{O(1)}` roles; the fixed central halo has
`m^{O(1)}2^m` roles; and every candidate marginal denominator remains
`2^{2m-o(m)}`.  A cofacet outside the candidate target is still witnessed
by one of only polynomially many used facets, so it changes the numerator
only polynomially.  The greedy forbidden probability is therefore
`2^{-m+o(m)}`.  Lemmas 14.1--14.2 are valid.

For the local exposure audit, a fixed lower vertex lies below at most two
consecutive owners of a monotone ear or cyclic-window dwell.  Dually, a
fixed owner contains at most two consecutive protected lower colours.
Only two intended objects meet at one chronology seam.  Thus the safe
overcounts `ell_A<=4`, `e_A^priv<=2`, `z_U(A)<=4` hold.  Full nonlocal halo
separation makes the joint ledger the maximum of these and the old
`10,10,9`, not their sum.  New segment endpoints are private rather than
exceptional.  The incidence scale remains `O(m2^m)`.  Hence every input of
the existing protected-factor theorem is preserved and Theorem 14.3's
spanning two-factor conclusion is justified.

## 15. Remaining scope after the joint factor

The common-core union witness in each dwell, immediate palettes, central
residence halos, low literal tickets, and old hinge-damage witnesses are
literal subobjects and survive the coextension.  A generic residual
two-factor edge does not supply arbitrary-width upper witnesses, global
residence, bounded component count, or a common-cap compiler.  The deleted
tail traces and exceptional splices are also absent.  The five automatic
and four open rows listed in Section 15 of the theorem match the actual
quantifiers.
