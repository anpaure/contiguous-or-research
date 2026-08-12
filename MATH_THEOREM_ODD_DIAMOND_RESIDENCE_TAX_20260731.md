# Odd diamond lifts pay exactly one unit of residence

Date: 2026-07-31  
Status: dimension-uniform theorem plus exact `K15 -> K17` specialization;
no all-(k) construction is claimed

## 1. The run-loss identity

Let

\[
  T_0,T_1,\ldots,T_{s-1},T_0
\]

be a cyclic Johnson component of rank-\(r\) sets, and put

\[
                         C_i=T_i\cap T_{i+1}.       \tag{1.1}
\]

Fix a coordinate \(x\) whose cyclic indicator is nonconstant. A positive cyclic run of \(x\) in the
\(T\)-sequence of length \(\ell\ge2\) has boundary Johnson steps which
delete and insert \(x\), while every internal step retains it.
Consequently (1.1) turns this run into a positive run of length exactly
\(\ell-1\) in the \(C\)-sequence.  A singleton \(T\)-run contributes no
positive \(C\)-run.  Conversely every positive run in \(C\) arises from a
unique \(T\)-run of length at least two. Hence

\[
 \boxed{\quad \operatorname{runs}_x(C)
       =\{\ell-1:\ell\in\operatorname{runs}_x(T),\ \ell\ge2\}.\quad} \tag{1.2}
\]

If \(x\) is absent from the whole component it stays absent; if it is
present on the whole component it stays present and does not shorten.
Neither constant case occurs when the component family enumerates a
complete uniform layer.

In the lower-`q1`-bijective factors used below, singleton runs are impossible:
the two incident edge intersections would both equal \(T_i\setminus\{x\}\).
Thus no run is discarded in the intended parent class.

In the two-new-coordinate odd diamond lift, the `A`-shore owners are

\[
                            A_i=C_i\cup\{u,v\}.     \tag{1.3}
\]

Thus every old-coordinate run loses exactly one unit of residence before
any macro cutting or nonflat rank exchange is applied.

## 2. The regenerative residence criterion

Suppose the child is to be compiled at depth \(d\), so every internal
positive owner run must have length at least \(d+1\). By (1.2), an
unbroken parent run of length \(d+1\) becomes a forbidden `A`-shore run of
length \(d\). Such a run has the trace pattern

\[
                0\,1^d\,0                              \tag{2.1}
\]

and is internal to a residual macro exactly when all \(d+1\) physical
trace edges spanning (2.1) are retained.

Write the colour of trace edge \(i\) as

\[
                         Z_i=C_i\cap C_{i+1}.       \tag{2.2}
\]

The parent-induced macro rule retains exactly one physical occurrence of
every required \(Z\)-colour. Therefore:

> **Theorem 2.1 (one-unit residence tax).** A parent with minimum
> coordinate-run length at least \(d+2\) makes every `A`-shore macro
> automatically depth-\(d\) resident. More generally, a parent run of
> length exactly \(d+1\) is harmless iff at least one of its \(d+1\)
> spanning trace edges can be left unretained. If all those edge colours
> have unique physical occurrences, the child contains a forced short run
> under every occurrence transversal and every port completion.

The theorem is local and exact. It identifies two legitimate recursive
states:

1. **margin state:** export residence \(d+2\), one unit stronger than the
   child compiler needs; or
2. **compensated state:** carry a cut/facet/nonflat actuator hitting every
   minimum parent run whose ordinary trace edge cannot be discarded.

Ordinary depth-\(d\) residence alone is not regenerative.

## 3. Exact `K15 -> K17` specialization

For the authenticated `6390+45` parent, \(d=3\). Exact lower-rainbow
counting gives `429` runs per coordinate in \(T\), and its construction is
resident, so all parent runs have length at least four. The literal census
finds exactly

\[
              95\text{ length-four runs per coordinate},
              \qquad 1425\text{ in total}.          \tag{3.1}
\]

These become precisely the `A`-shore patterns \(0,111,0\). Of them,
`165` have four unique rank-six edge colours: exactly eleven per old
coordinate. Theorem 2.1 therefore proves that no occurrence transversal,
macro permutation, macro reversal, or integral port flow based on this
parent can produce a flat depth-three-resident child.

The exact coupled optimum over all occurrence transversals is `180`, proved
by a retained bound-179 CNF/DRAT certificate and attained by an independently
replayed choice. Interestingly, each coordinate can separately attain its
solver-free floor eleven, but the fifteen choices cannot do so
simultaneously; the additional fifteen-run debt is an integral correlation
effect, not a scalar count.

This explains why the optimized port-flow carrier can improve upper and
deeper palettes substantially while its residence gate cannot close. It
also explains what a successful nonflat construction must do: exchange or
otherwise compensate at least one physical slot in every forced
minimum-run packet.

## 4. Consequence for the general construction

The dimension-uniform parent-induced macro-flow theorem closes ownership,
connectivity, and the immediate lower palette under its exact flow
hypotheses. The state exported to the next odd dimension must nevertheless
contain more than those central invariants. At minimum it must include

\[
  (\text{lower-rainbow factor},\ 
   \text{trace-colour occurrence transversal},\ 
   \text{residence margin or compensation set}).    \tag{4.1}
\]

Upper palettes and the common lower compiler remain additional correlated
coordinates. Any induction that exports only a resident middle factor
silently loses one residence unit at its next diamond step and is
insufficient.

## 5. Audit sources

The exact `K17` counts and the occurrence-choice CNF are independently
replayable in

```text
scratch/audit_k17_fixed_macro_residence_obstruction_20260731.py
scratch/build_k17_macro_residence_cnf_20260731.py
scratch/build_k17_macro_residence_cnf_relax_forced_20260731.py
scratch/k17_macro_residence_20260731.cnf
scratch/k17_macro_residence_20260731.map.json
```

The CNF has `1425` run clauses, including `165` empty clauses coming from
the unique-colour packets. No SAT-solver conclusion is used.
