# The first parent-induced `K17` macro family has 605 immutable short runs

Date: 2026-07-31  
Status: exact scoped theorem with literal audit; no global `K17` obstruction

## Result

Consider the authenticated Hamilton carrier

```text
scratch/k17_parent_induced_macro_port_cycle_20260731.cycle
```

constructed from `1430` residual macro paths and `5005` singleton pure-`U`
objects.  A **port edge** is an edge between two atomic objects.  Its
rank-eight intersection contains neither new coordinate.  Conversely every
edge whose intersection contains neither new coordinate is a port edge.
There are exactly

\[
                         6435=1430+5005
\]

of them, so this criterion recovers the object decomposition directly from
the literal carrier.

> **Theorem 1.** Among the carrier's `2892` positive coordinate runs of
> length below four, exactly `605` are length-three runs whose two flanking
> edges and internal edges all lie strictly inside one residual macro.
> Consequently no permutation of the fixed atomic objects, no reversal of
> any macro, and no replacement of the integral `U`-to-port completion can
> make this macro family depth-three resident.

Thus port-flow optimization alone cannot finish `K17`.  At least one of
the following must change:

1. the retained occurrence of some repeated rank-six trace colour, hence
   the internal macro paths;
2. the parent chronology itself; or
3. the flat maximal-erosion compiler, by using a genuinely nonflat schedule.

The first alternative is not sufficient for this fixed parent.

> **Theorem 2.** Allow an arbitrary choice of one physical occurrence of
> every rank-six trace colour, rather than retaining the first occurrence.
> Every resulting macro family still contains at least `165` solver-free
> forced internal length-three coordinate runs, exactly eleven for each of
> the fifteen old coordinates.  The exact simultaneous minimum is `180`, as
> sharpened in Proposition 2.1.

Consequently changing only the occurrence transversal, macro
order/orientation, and port flow can never finish this fixed retained-edge
`A/X/Y` template.  A different parent chronology, a same-parent
cut/facet/value-changing compensation, or a nonflat compiler remains open.

This is deliberately scoped.  It is not an obstruction to an alternative
parent-induced forest or to an optimal `K17` word.

## Proof

Write the cyclic owner sequence as \(V_0,\ldots,V_{W-1}\), and let

\[
                         I_i=V_i\cap V_{i+1}.
\]

Every internal edge of an `A/X/Y` macro retains at least one of the two new
coordinates in \(I_i\).  At a port, the adjacent endpoint owners are two
extensions of the same old rank-eight colour, or one such extension and a
pure `U` owner, or two pure `U` owners.  Their intersection is therefore
exactly that old colour and contains neither new coordinate.  This proves
the port-edge characterization.  The literal census gives `6435` such
edges and cuts the cycle into `5005` one-vertex objects and `1430` longer
objects, exactly the construction ledger.

A positive coordinate run of length \(\ell\) is determined by the
\(\ell+1\) edges consisting of its entering edge, its \(\ell-1\) internal
edges, and its leaving edge.  If none is a port edge, the entire binary
pattern

\[
                            0\,1^\ell\,0
\]

lies strictly inside one macro.  Permuting macros does not alter it, and
reversing the macro merely reverses the same pattern.  Changing the
`U`-to-port flow changes only port adjacencies.  Hence its length is
invariant under all three operations.

The independent scan finds

\[
  1063\text{ runs of length }2,\qquad
  1829\text{ runs of length }3,
\]

of which exactly `605` length-three runs meet no port edge.  Depth-three
residence requires every internal positive run to have length at least
four, so the fixed family cannot pass. \(\square\)

## The occurrence-transversal obstruction

Let \(C_i=T_i\cap T_{i+1}\) be either cyclic rank-seven trace. A strictly
internal short run in the `A` shore has the form

\[
  x\notin C_{i-1},\quad
  x\in C_i\cap C_{i+1}\cap C_{i+2},\quad
  x\notin C_{i+3}.                                  \tag{2.1}
\]

It survives exactly when the four physical edges
\(i-1,i,i+1,i+2\) are all retained. For each rank-six colour \(Z\), the
construction must retain exactly one physical edge having colour \(Z\).
Thus (2.1) gives one negative clause on at most four occurrence-choice
variables. This is an exact CNF characterization, not merely a necessary
condition.

The authenticated parent has `1425` patterns (2.1), exactly `95` per old
coordinate. In `165` of them all four rank-six edge colours have a unique
physical occurrence. Those edges are forced retained, so their clauses are
empty. The distribution is exactly eleven empty clauses per coordinate.
This proves Theorem 2 solver-free. \(\square\)

### Proposition 2.1 (exact occurrence-transversal optimum)

For this fixed parent, the minimum number of strictly internal short
`A`-shore runs over all rank-six occurrence transversals is exactly

\[
                              \boxed{180}.           \tag{2.2}
\]

An authenticated choice attains twelve runs per old coordinate. The
independent macro-path replay reconstructs all `1430` paths and counts the
same `180` literal runs. For the lower bound, the exact bound-query CNF
introduces one violation variable for each of the `1260` non-forced
patterns and asks whether at most `14` of them can remain, in addition to
the `165` forced patterns. Kissat returns `UNSAT`; the retained DRAT proof
is independently accepted by `drat-trim` with a `5531`-clause core and
`99145` resolution steps. Thus no unverified optimizer bound is used in
(2.2).

The coordinate-restricted minimum is `11`: the fixed packets give the lower
bound, and one attaining coordinate witness transports to all fifteen old
coordinates by cyclic coordinate rotation of the frozen parent.  These
fifteen coordinatewise witnesses are not compatible with one common
occurrence transversal.  The extra `15` in (2.2) are therefore a global
integral-correlation debt.  They are not fifteen further individually forced
packets, and `180` is not a lower bound on the number of distinct future
actuator sites because one cut/facet/rethread may hit several surviving
packets.

## A useful separation of the upper-`q1` gate

The same audit splits rank-ten upper unions by their two-new-coordinate
tag.  For tags `none`, `Y`, `X`, `XY`, the missing counts are respectively

\[
                           618,\quad623,\quad650,\quad0.
\]

The `XY` palette is already complete internally.  The one-tag palettes
have `882` and `900` colours absent from the fixed macro interiors but
`984` port opportunities each; the pure palette has `4021` port
opportunities for `3003` targets.  Thus the upper-`q1` ledger is not ruled
out by capacity.  It remains a constrained port-turn covering problem,
whereas residence already forces an upstream change of macro interiors.

## Reproducibility

```text
python3 scratch/audit_k17_fixed_macro_residence_obstruction_20260731.py
python3 scratch/build_k17_macro_residence_cnf_20260731.py \
  --cnf scratch/k17_macro_residence_20260731.cnf \
  --map scratch/k17_macro_residence_20260731.map.json
python3 -m py_compile scratch/audit_k17_fixed_macro_residence_obstruction_20260731.py
python3 -m py_compile scratch/build_k17_macro_residence_cnf_20260731.py
python3 -m py_compile scratch/build_k17_macro_residence_cnf_relax_forced_20260731.py
```

The audit reads only the frozen literal cycle, reconstructs all port edges,
checks the `5005+1430` object decomposition, and emits

```text
scratch/k17_fixed_macro_residence_obstruction_20260731.audit.json
```

The CNF audit has `2805` one-hot occurrence variables, `1425` residence
clauses, and `165` explicit empty clauses. It records every physical
pattern and its exact occurrence-choice literals.

The authenticated builder above remains byte-fixed. Its optional
empty-clause relaxation is preserved, without changing that lineage, as
`scratch/build_k17_macro_residence_cnf_relax_forced_20260731.py`.

The exact optimum package is

```text
scratch/solve_k17_macro_residence_maxsat_20260731.py
scratch/k17_macro_residence_optimal_20260731.json
scratch/verify_k17_macro_residence_optimum_20260731.py
scratch/k17_macro_residence_optimal_20260731.verify.json
scratch/build_k17_macro_residence_bound_cnf_20260731.py
scratch/build_k17_macro_residence_bound_cnf_coordinate_20260731.py
scratch/k17_macro_residence_bound179_20260731.map.json
scratch/k17_macro_residence_bound179_20260731.cnf
scratch/k17_macro_residence_bound179_20260731.drat
scratch/k17_macro_residence_bound179_20260731.dratcheck.txt
```

The legacy bound builder reproduces the frozen bound-`179` CNF and map
byte-for-byte. Its later coordinate-face option is preserved separately in
`scratch/build_k17_macro_residence_bound_cnf_coordinate_20260731.py`.
