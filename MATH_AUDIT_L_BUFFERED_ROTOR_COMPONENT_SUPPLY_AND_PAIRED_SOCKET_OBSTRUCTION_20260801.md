# Independent audit: buffered rotor supply and paired-socket obstruction

Date: 2026-08-01  
Audited file:
`MATH_THEOREM_L_BUFFERED_ROTOR_COMPONENT_SUPPLY_AND_PAIRED_SOCKET_OBSTRUCTION_20260801.md`  
Verdict: **PASS with the explicit type-level/canonical-catalogue scopes in
the theorem**.

## 1. Package and switch rows

For `g_(a,b)`, the mobile vector is a positive composition of
`B=b-a+1` into `D+1=d-a+1` parts.  At `b=d+1`, `B=D+2`, so exactly one
part is two and rotation is transitive.  At `a=d-1`, there are two positive
parts and the rotation orbits are unordered pairs of sum `B`, giving
`floor(B/2)`.  Proposition 1.1 is exact.

For positive permanent core `K>=1`, adjacent unit transfer on positive
compositions is connected.  In the crossed baseline arcs, all shifted
mobile rows are equal, the mobile/tail row is positive, and the only fresh
inequalities compare adjacent values differing by one; `K>=1` supplies the
needed slack.  Thus Theorem 2.1 correctly proves connectedness only after
contracting raw rotation necklaces.  It does not prove distinct physical
ports or a serializable spanning tree.

## 2. Core-free and tight-word rows

For the core-free complete positive-composition bank, the original
coordinate marginals cancel in `M_0-M_d`.  Every added age occurrence
contributes at most `r`, while every untouched raw necklace needs at least
one positive-slack exit.  Hence `kappa-t<=rt` and
`t>=ceil(kappa/(r+1))` when `kappa>1`.  The one-necklace exception is
necessary and is stated.

Whenever `M_i=M_(i+1)` on a consecutive coordinate range, summing the
nonnegative successor inequalities forces termwise equality on every
selected edge.  The successor graph therefore splits by the frozen internal
word.  Inside one block the remaining graph is product dominance.  Finite
poset Strassen/Hall gives exactly the upward-set inequalities of Theorem
3.5.  This is an **unlabelled age-type occurrence** theorem; it does not
include fixed labelled owners, fixed partitions, or physical guarded arcs.

For Theorem 3.4, the pair package types are
`(d+1,2,1^(d-1))` and `(d+2,1^d)`.  They do not enter the all-two tight
fibre.  Both shores of that fibre are the same prefix downset

```text
P={(x_0,x_1)>0:x_0+x_1<=5}.
```

A bijection `y<=x` on identical finite multisets has zero summed slack and
is pointwise equality, forcing the all-two self-loop.  The smallest numeric
row `d=3,r=8,N=140`, aggregate vector
`(20,0,140,0,140,0,0,15)`, is consistent.

For Theorem 3.6, the top role cannot be supplied without a
`g_(0,r-1)` package: otherwise it consumes `(d+1)p_0T>N` low-buffer
occurrences.  Every canonical alternative package misses the all-two word,
so the same closed fibre persists.  This proves decomposition independence
only among canonical uniform-rotor occurrence packages and canonical unit
self-loops.  It is not a no-go for arbitrary physical clocks with the same
aggregate role vector.  The smallest row
`d=4,r=10,N=775,T=3`, vector `(210,775,775,168)`, checks.

## 3. Paired resources and positive face

Under the theorem's serial-safe macro semantics, the graphic equations,
two socket capacities, other unit capacities, and exact payload equation
are plainly necessary.  Conversely a serial-safe spanning tree reduces the
component count by one at each merge and satisfies the claimed fusion.
Theorem 4.1 is therefore an exact formulation, not an assertion that its
multi-resource system is integral.

The `2x2` diagonal/off-diagonal catalogue passes both projected `K_(2,2)`
Hall systems and has no joint choice.  The private signed payload example
preserves rank totals but has no nonempty cancellation.  These prove that
separate two-buffer Hall and aggregate rank rows are insufficient.

On the private, payload-zero, serial-safe face every connected component
graph has a usable spanning tree, proving Corollary 6.1.  The one-nonprivate-
shore extension is correctly scoped to the otherwise private payload-zero
face; it is ordinary graphic/partition matroid intersection, not the full
paired problem.

## 4. Final scope

The note proves:

* positive-core necklace-level switch supply;
* exact core-free occurrence-edit lower bounds;
* explicit two-buffer and canonical-decomposition tight-fibre no-gos;
* the exact paired macro system and its private min-cut face.

It does not prove a literal pair-labelled connector atlas, named NRFC
colouring, owner-simple physical fusion, residence, upper/deep witnesses,
or common-cap/compiler compatibility.  The theorem states these exclusions
correctly.

