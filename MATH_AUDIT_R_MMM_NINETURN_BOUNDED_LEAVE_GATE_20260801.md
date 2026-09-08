# Independent audit of the MMM nine-turn bounded-leave reduction

Date: 2026-08-01  
Audited file:
`MATH_THEOREM_R_MMM_NINETURN_DEFECT_BLOCK_RECURSION_SYNDROME_AND_BOUNDED_LEAVE_GATE_20260801.md`  
Method: independent symbolic audit plus lightweight replay of already-frozen
`n=4,5,6` artifacts; no new search.

## Verdict

**PASS WITH THE STATED OPEN GATE.**  The note proves exact recurrences,
hypergraph/lattice reductions, and sufficient bounded-state criteria.  It
does not prove a uniform bounded block leave.

## 1. Raw-defect count

The missing raw MMM turns are exactly cyclic triples of nonempty Dyck words.
Double counting a labelled word with one of its three distinguished cuts
gives

\[
 D_n={2n+1\over3}[z^{n-1}](C-1)^3
     ={2n+1\over n-1}\binom{2n-2}{n-4}.
\]

This gives `3,22,117` at `n=4,5,6`.  Consecutive division yields

\[
 {D_{n+1}\over D_n}
 ={2(2n-1)(2n+3)(n-1)\over(n-3)(n+3)(2n+1)},
\]

and subtraction of four gives exactly the numerator
`-4n^2+58n+42`.  Its ratio is `-2/n+O(n^-2)`, so the discrepancy from four
copies is unbounded in magnitude.  This refutes only the stated four-tagged-
copy plus bounded-correction recursion.

Peak insertion/deletion preserves the nonempty three-Dyck-component grammar.
It is a raw-defect morphism, not a theorem about an independently glued
Hamilton endpoint.

## 2. Block normal form and counts

Complementing the upper shore turns every block into

\[
 H+Q_0,H+Q_1,H+Q_2\quad\text{versus}\quad
 G+Q_0,G+Q_1,G+Q_2,
\]

where `H,G,Q_0,Q_1,Q_2` partition the ground with sizes
`n-4,n-4,3,3,3`.  Complementing back gives the three pairwise-union upper
holes, so the equivalence is exact.

The unrestricted edge count, degree, and codegrees follow by direct
partition counting:

\[
 |B_n^{all}|={(2n+1)!\over(n-4)!^2(3!)^3 3!},
\]

\[
 d={1\over2}\binom{n-1}{3}^2\binom{n+2}{3}.
\]

Same-shore codegree is `binom(n-1,3)` exactly at intersection `n-4`.
Cross-shore codegrees are `binom(n-1,3)^2` at intersection zero and `10` at
intersection three.  The normalized maximum is `O(n^-3)`.

These are ambient counts only.  The induced endpoint hypergraph at `n=6`
has isolated vertices, so no regular-hypergraph matching theorem follows.

## 3. Leave and recursive criteria

A block removes three targets on each shore.  Therefore

\[
                         \rho_n=D_n-3\nu(B_n)
\]

is exact.  A maximal matching has a balanced block-free leave, proving the
balanced-independence sufficient criterion.  The finite-state padding
theorem is a literal induction: lifted parent blocks and the transition
matching use complementary vertex banks and hence unite without collision.

The active-diameter lemma is scoped to one literal padded gadget.  It does
not obstruct relational gadgets or a bounded collection placed in several
independent sockets.

## 4. Syndrome and degree cuts

For one block, the left-minus-complement-right incidence vector is

\[
                         3({\mathbf 1}_H-{\mathbf 1}_G),
\]

so the `F_3` syndrome and both shore counts modulo three are invariant.
In original upper notation, a coordinate in an active triple contributes
upper-minus-lower degree one, while a coordinate in `H` contributes
`2 lower-upper=3`.  This proves both integer rows and the residual-size
lower bounds in the theorem.

Light replay of the frozen endpoints gives, up to coordinate naming:

* best `n=5`: lower degrees all `8`, upper degrees
  `(14,15,13,14,...,14)`, syndrome `e_1-e_2`;
* canonical and best one-glue `n=6`: lower degrees all `45`, upper degrees
  `(72,74,70,72,...,72)`, syndrome `2(e_1-e_2)`.

The exact `n=5` one-pair leaves carry the first syndrome.  At `n=6`, count
and syndrome allow a three-pair leave, while exact search excludes a
`38`-block packing; hence syndrome is necessary but not sufficient.

## 5. Finite census scope

The authenticated conclusions are:

\[
                         \rho_4=0,\qquad \rho_5=1,
                         \qquad \rho_6\ge6.
\]

The last inequality does not include a `37`-block witness; it is not an
equality.  Also, `38` blocks at `n=6` would leave three pairs.  Adding one
unit service would still not give complete repair, so no such interpretation
is used in the main note.

The `112` and `56` figures count labelled gluing-tree selections passing the
Hamilton audit.  The main theorem correctly avoids asserting that every
selection has a distinct physical edge set.

## 6. Relational and physical scope

Every block is a crown in the containment graph.  Berge decomposition and
Hall deficiency prove the augmenting-path formulation exactly.  The crossed
rerouter closes the audited `n=5` service bank, but its `n=5` and `n=6`
coordinate rows are not one padded orbit.

Colour-service edges are not physical packets.  One nine-turn block is three
`C_10` switches and fifteen replaced factor seams.  The physical crossed
compound at active ground eleven fails residence, while the separate full
reset passes all guards but needs a private recursively supplied socket.
Therefore no residence, deeper-shadow, common-cap, compiler, or unconditional
`B(k)+O(1)` statement has leaked into the result.

The exact unresolved alternatives are correctly stated: bounded balanced
independence, a finite-state block cover-down, bounded containment Hall
deficiency with physical augmenting packets, or a growing obstruction in one
of their dual quantities.
