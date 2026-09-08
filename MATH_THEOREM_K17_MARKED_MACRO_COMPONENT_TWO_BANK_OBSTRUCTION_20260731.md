# The frozen `K17` macro forest obstructs the whole-component two-bank rethread

Date: 2026-07-31  
Status: exact solver-free finite theorem; six-socket macro-forest exchange remains open

## 0. Result

The `108` forced nonflat A-shore macros do admit one compatible owner-phase
Hamilton path when they are detached from the frozen port forest.  They do
**not** admit the more restrictive whole-component two-bank realization in
that forest.

The fixed macro forest places the `108` required macros in `106` components.
Closing those components forces another `82` optional macros into the marked
bank, for

```text
marked components                         106
required macros                           108
whole-component closure macros            190
optional macros forced by closure          82
literal rank-nine owner tokens            3970
```

Every required macro is internally clean.  Nevertheless, six of the forced
components contain, wholly inside their optional macros, exactly `32` strict
internal depth-two runs of length two:

```text
coordinate x (bit 15)                      16
coordinate y (bit 16)                      16
depth-three runs below four                  0
```

Reversing a component preserves this census.  A residual `U` connector can
touch only a component endpoint, so it cannot change any of these strict
internal runs.  Therefore the exact constrained `U`-to-port model with one
marked owner interval and one complementary facet interval is infeasible
before any global flow or connectivity constraint is considered.

This is not a `K17` no-go.  In all six bad components the unique required
macro is an endpoint edge.  Hence one macro-forest split per component would
remove the bad optional tail topologically.  The next exact target is a
**six-socket occurrence/macro-edge exchange**, followed by the ordinary
two-bank `b`-flow.

## 1. The exact connector model

Let `P` be the fixed macro-edge forest on the `6435` rank-eight port colours
`T`, and put

\[
                         d(T)=2-\deg_P(T).                         \tag{1.1}
\]

For every pure rank-nine owner `U` and every pair of distinct facets
`T,T' subset U`, introduce a binary variable

\[
                            x_{U;T,T'}.                             \tag{1.2}
\]

The exact residual flow rows are

\[
 \sum_{\{T,T'\}\subset U}x_{U;T,T'}=1
 \quad(U\in\tbinom{[15]}9),                                      \tag{1.3}
\]

\[
 \sum_{U,T':\,T,T'\subset U}x_{U;T,T'}=d(T)
 \quad(T\in\tbinom{[15]}8).                                      \tag{1.4}
\]

Thus every `U` is a distinct connector, every residual port is filled, and
the union with `P` is two-regular.  Contracting the components of `P`, a
two-bank solution additionally requires:

1. the `106` components meeting required macros induce one path;
2. all complementary components induce the other path;
3. exactly two selected `U` edges cross between the banks; and
4. the two physical joins satisfy the capped coordinate-run inequalities.

Connectivity of both induced paths makes their union one cycle.  These are
the precise flow/connector rows requested by the two-bank formulation.

## 2. Why component closure is forced

An internal vertex of a nontrivial macro component has macro degree two.
Equation (1.1) gives it residual demand zero, so no variable in (1.2) may use
it.  In the expanded carrier the two incident macro paths are therefore
traversed consecutively, without an intervening `U` owner.

Consequently a single marked phase interval that contains any macro edge of
a fixed component must traverse every macro edge between its two external
ports.  For the `108` required macros this is exactly the `190`-edge closure
above.  Adding further optional components cannot remove a violation already
strictly internal to one of these components.

## 3. Literal residence replay

The audit reconstructs the rank-nine owner value of every node in every
macro path:

\[
 A_i=C_i\cup\{x,y\},\qquad
 X_i=T_i\cup\{x\},\qquad
 Y_i=T_i\cup\{y\}.                                                 \tag{3.1}
\]

It orders each macro component from one degree-one port to the other and
orients every literal macro path accordingly.  Every original required
macro separately has

\[
        \#\{\text{internal D2 runs}<3\}
      = \#\{\text{internal D3 runs}<4\}=0.                         \tag{3.2}
\]

For the whole-component closure the six failing rows are:

| component | macros | required endpoint macro | owner tokens | D2 length-two runs |
|---:|---:|---:|---:|---:|
| 8 | 13 | 842 | 68 | 12 |
| 17 | 3 | 931 | 23 | 2 |
| 18 | 3 | 648 | 23 | 2 |
| 26 | 17 | 941 | 91 | 12 |
| 31 | 3 | 736 | 23 | 2 |
| 32 | 3 | 832 | 23 | 2 |

All `32` bad runs lie entirely inside `26` optional macro paths; none lies
inside a required path.  Sixteen are on `x`, sixteen on `y`, and all have
length exactly two.  There are no strict internal D3 violations because
adjacent OR either merges neighbouring runs or moves the dilated run onto a
component boundary; every resulting strict internal D3 run has length at
least four.  D2 already fails the nonflat compiler requirement.

The component order is unique up to reversal.  Reversal preserves each run
length and whether it is strict internal.  Equations (1.3)--(1.4) attach
connectors only at the two external component ports.  Hence no assignment of
the connector variables can repair (3.2) for the six rows in the table.

This proves the stated fixed-forest two-bank obstruction.

## 4. The six-socket escape

In each bad component the only required macro occurs at one endpoint.  If
the macro forest is changed at the one adjacency separating that required
edge from its optional tail, the required edge can enter the owner bank as a
singleton component while the bad tail stays in the facet bank.

At least one forest adjacency incidence must change in each of the six
vertex-disjoint bad components, so six component-local splits are a rigorous
lower bound for this escape inside the component-splitting class (one
multi-edge exchange may service two such incidences).  It is only a
topological/residence statement: one must still find compatible alternative
occurrence ports, re-solve
(1.3)--(1.4), preserve the displaced palettes, and pass the common-cap
compiler.

Thus the unrestricted next problem is much smaller than the original
`107`-boundary debt, but it is not solved by this note.

## 5. Reproducibility and scope

Run

```text
python3 scratch/audit_k17_marked_macro_component_two_bank_obstruction_20260731.py
python3 -m py_compile scratch/audit_k17_marked_macro_component_two_bank_obstruction_20260731.py
```

Artifacts:

```text
scratch/audit_k17_marked_macro_component_two_bank_obstruction_20260731.py
SHA-256 22bc6ed6e20a0b0d9a049720bf681fbac1991c334e81d66c5442265353fd6e11

scratch/k17_marked_macro_component_two_bank_obstruction_20260731.audit.json
SHA-256 c4a7e2477186247bdbdace01967426a1cf55db8bcacc99296b679c681451e259
payload SHA-256 f5d7bcdaf7c06375d9459fe35e1c662780330c1eeda70602d8e0160aff8da519

scratch/independent_verify_k17_marked_macro_two_bank_obstruction_20260731.py
SHA-256 cf0e1d93b2a4ac41d49f176355b4fae3f676772323030b60543287dab1090032

scratch/k17_marked_macro_component_two_bank_obstruction_20260731.independent.json
SHA-256 b668fbc5e75a9ccd25c3571a9c4938f2a6167b0e66ca18d8c35c096afe90bdec
payload SHA-256 d1c0a5d75402d8e054ba3a0a426c253a1f53c99b63edd285f80e3a2ca5598694
```

Authenticated dependencies are recorded in the audit JSON.  The theorem
closes only the whole-component two-bank model in the **frozen** macro-edge
forest.  It does not exclude changing the occurrence transversal or macro
forest, splitting components by a six-socket exchange, using more than two
phase intervals, or constructing an optimal `K17` word by another compiler.
