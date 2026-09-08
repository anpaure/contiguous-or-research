# The exact `k=11` word is a fully guarded middle-levels reset

Date: 2026-07-31  
Status: exact finite full-reset theorem; all central, residence, shadow and
compiler rows pass on the eleven-coordinate base; recursive installation is
open

## 0. Verdict

The first physical crossed rerouter solved topology and occurrence
correlation but failed residence.  The existing exact `k=11` certificate
contains a stronger object which had not been read as a packet:

> Its third derivative is a Hamilton factor of `ML(11)` with complete turn
> palettes, perfect augmented matching, minimum cyclic coordinate residence
> four, and complete intersection/union shadows at every depth.  The
> original length-465 word is an actual lower compiler covering all 2,047
> nonempty masks.

Relative to the canonical MMM factor, this is one finite atomic **full
reset**.  It changes 882 middle-level vertices and 621 old seams; its
symmetric difference is one connected degree-four compound.  Thus it is
not a small local switch, but its size is independent of the later ambient
dimension.

This is the first packet in this lane on which topology, both palettes,
occurrence correlation, residence, all deeper shadows and the compiler are
simultaneously positive.  It proves compatibility of the guards, not the
general construction: a recursion must still create a private
eleven-coordinate socket (or an equivalent transparent gluing state) into
which the reset can be installed without consuming other packets' resources.

## 1. From the exact word to a middle-levels factor

Let

```text
A = scratch/sigma_sat_k11_465.word
```

and let `D` be adjacent union on a linear word.  Put

\[
                         T=D^3A.                    \tag{1.1}
\]

The frozen certificate has length 465, so `T` has length 462.  Exact
evaluation gives

\[
                 \{T_i\}=\binom{[11]}6.             \tag{1.2}
\]

Read `T` cyclically and set

\[
                         X_i=T_i\cap T_{i+1}.        \tag{1.3}
\]

Then

\[
                 \{X_i\}=\binom{[11]}5.             \tag{1.4}
\]

with no repetition.  Therefore

\[
 X_0,T_1,X_1,T_2,\ldots,X_{461},T_0,X_0             \tag{1.5}
\]

is a Hamilton cycle of the middle-levels graph `ML(11)` (up to the harmless
index convention in (1.5)).

## 2. The complete guard theorem

### Theorem 2.1 (eleven-coordinate guarded reset)

The factor (1.5) and word `A` satisfy all of the following.

1. **Topology:** (1.5) is one 924-vertex Hamilton cycle.
2. **Turn palettes:** all 330 rank-four lower turns and all 330 rank-seven
   upper turns occur.
3. **Occurrence correlation:** the augmented decoration graph has a perfect
   matching of size 792.
4. **Residence:** every cyclic coordinate run in the rank-six word `T` has
   length at least four.
5. **All-depth shadows:** for every `1<=q<=5`, the intersections and unions
   of `q+1` consecutive entries of `T` contain every set of ranks `6-q` and
   `6+q`, respectively.
6. **Compiler:** every nonempty subset of `[11]` is the union of a contiguous
   interval of the linear word `A`, and `D^3A=T`.
7. **Catalan forest:** one perfect augmented matching decodes to a spanning
   132-path linear forest on the rank-six layer of the twelve-coordinate
   diamond lift.  Its formal endpoint catalogue has 1,185 legal connector
   records and every component has at least six component-neighbours.

#### Proof

The independent audit enumerates the 465-entry word and all 108,345 linear
intervals, obtaining all `2^11-1=2047` nonempty masks.  It computes the four
derivative rows literally; the third row is exactly (1.2).  It then checks
(1.3)--(1.4) and every edge of (1.5).

The two turn maps are computed from the two neighbours of each cycle
vertex.  Their supports are the complete rank-four and rank-seven layers.
The augmented graph is rebuilt from those literal turns and physical edges;
an independent augmenting-path algorithm returns rank 792, the full shore
size.

For residence the audit decomposes the cyclic membership word of every
coordinate into maximal one-runs.  The minimum is four.  For every depth
`q=1,...,5` it directly enumerates all 462 cyclic windows, computes their
intersection and union, and checks containment of the complete target
layers.

Finally decode the perfect augmented matching into selected turn vertices
and residual cross edges.  There are 330 selected vertices on each shore,
their cyclic types alternate, and their binary trace is outside the unique
cycle face.  The resulting 792 distinct diamond edges have maximum degree
two on all 924 middle vertices and form exactly 132 acyclic components.
Direct endpoint comparison gives the stated connector counts.  These
computations prove items 1--7. \(\square\)

The exact run histogram begins with 143 runs of length four and 132 of
length five; residence is achieved at the threshold rather than by making
all runs long.  This agrees with the run-boundary mechanism in the known
optimal words.

## 3. It is an atomic reset from the canonical MMM state

Let `F_0` be the canonical MMM Hamilton factor with gluing selection
`(7,8,9,11,12)`, and let `F_*` be (1.5).  The source has 22 turn holes on
each shore and augmented rank 770; the target has zero holes and rank 792.
Their exact difference ledger is

```text
common physical edges: 303
removed old seams:      621
added new seams:        621
changed vertices:       882
symmetric-difference components: one
maximum changed degree: four.
```

The signed occurrence banks are

```text
lower: 110 negative + 110 positive units, 209 changed colours;
upper:  98 negative +  98 positive units, 195 changed colours.
```

No colour loses more than one occurrence and no target support is lost.
The common augmented graph has rank only 272.  Therefore this reset is
**atomic and global on its active eleven coordinates**; it is not a private
22-path extension of the old matching and should not be decomposed into
independently selectable micro-switches.

## 4. Padding and the precise interface

For ambient `ML(2n+1)`, `n>=5`, choose disjoint coordinate sets

```text
H, active, G
```

of sizes `n-5,11,n-5`.  Add `H` to every vertex of `F_0` and `F_*` and keep
`G` absent.  Exactly as in the crossed-compound padding lemma, this preserves
all factor edges, turns, matching incidences and the active-coordinate
residence/shadow tables.  It produces a dimension-uniform boundaried reset
of constant physical size.

Two qualifications are load-bearing.

1. The padded length-465 word does **not** cover the complete larger Boolean
   cube; it is only a private compiler for the active socket and its padded
   target bank.
2. The reset can be installed only when the host exposes the complete old
   boundaried patch and reserves its external topology, provider and
   compiler interfaces.  Merely finding the same turn defects elsewhere is
   insufficient.

Under a private socket hypothesis the guard proof is immediate: replace the
whole component atomically, use Theorem 2.1's target decoration and compiler,
and leave every external provider/cell unchanged.  Because the active
component and every one of its tables have fixed size, this costs `O(1)`
state independent of `n`.

## 5. Consequence for the general construction

The earlier packet work separated three questions:

```text
service Hall -> physical factor -> downstream guards.
```

The crossed rerouter solved the first.  The 189-vertex compound solved the
second.  The full reset proves that the third is compatible with the first
two on one finite base.  The remaining theorem is no longer the existence
of a finite guarded gadget; it is its **recursive socket supply**:

> Construct the MMM/Pascal recursion so that all emitted bounded debt lies
> in disjoint copies of a finite collection of private sockets, including
> the eleven-coordinate full-reset socket, and join the resulting compiled
> forests without violating their exported boundary states.

Equivalently, a transparent gluing induction may carry the exact target
state of Theorem 2.1 rather than repair the stateless canonical factor after
the fact.  The finite theorem gives a positive state to carry.  It does not
prove that the standard recursion preserves or supplies it.

The decoded 132-path forest is particularly useful for that next step: the
reset exports a literal linear object, not merely a perfect matching.  The
minimum component-neighbour count six does not by itself give a spanning
connector tree, but it rules out isolated socket components in the base
state and supplies a concrete gluing catalogue for a transparent-tree
search.

This materially strengthens the case for a finite-state general
construction: every logical guard has now passed simultaneously on a
nontrivial base.  The open problem has moved to replication and gluing.

## 6. Reproducibility and scope

Run

```text
python3 scratch/audit_ml11_guarded_full_reset_20260731.py
```

to produce

```text
scratch/ml11_guarded_full_reset_20260731.audit.json.
```

The audit imports only the defining MMM reconstruction and generic matching
routine.  It derives the target factor from the frozen word rather than from
a solver model.  The theorem is finite and exact at active ground 11, plus
the formal padding statement.  It does not assert private-socket abundance,
disjoint packing, transparent recursive gluing, or `nu(k)=B(k)` for all
`k`.
