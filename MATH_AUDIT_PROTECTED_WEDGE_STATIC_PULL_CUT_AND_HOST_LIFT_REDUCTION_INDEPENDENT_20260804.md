# Independent audit: protected wedges versus a static pull host

**Date:** 2026-08-04  
**Audited theorem:**
`MATH_THEOREM_PROTECTED_WEDGE_STATIC_PULL_CUT_AND_HOST_LIFT_REDUCTION_20260804.md`  
**Audited theorem SHA256:**
`328bf5b1a280a1f926dac07afa478fa6469071b3fa8cb71788702ba17b483791`  
**Verdict:** **GO**, with the scope stated in the theorem.  The result is an
exact characterization relative to a fixed static tree-compatible pull
host.  It is not an existence theorem for such a host and does not price
residence, arbitrary upper witnesses, or compiler resources unless those
resources are explicitly added to the protected bank.

No search, finite enumeration, or solver result is used in this audit.

## 1. Definitions and switch semantics

The theorem fixes a two-factor `F`, a protected factor-edge set
`D subseteq F`, and for every host label `e` an alternating switch with
old phase `O_e subseteq F` and new phase `N_e cap F = emptyset`.

For one switch the new factor is

\[
                         F_e=(F\setminus O_e)\cup N_e.
\]

Since `D subseteq F` and `N_e cap F = emptyset`, no protected edge deleted
from `F` can be reintroduced by `N_e`.  Therefore

\[
                         D\subseteq F_e
 \iff O_e\cap D=\varnothing.
\]

This verifies Lemma 2.1, including its “if and only if.”  If the two
factor incidences at a lower vertex survive, the switched two-factor still
has degree two there, so those same two owners remain its neighbours.  The
full wedge and their q1 union are therefore unchanged.

The check is only support-level.  It correctly makes no claim about an
unnamed physical occurrence or witness whose value happens to agree with a
surviving wedge value.

## 2. Exact fixed-host cut characterization

Let

\[
 B_D=\{e:O_e\cap D\ne\varnothing\},
 \qquad H_D=H-B_D.
\]

A pull tree preserving `D` can use only edges of `H_D`.  Hence it is a
spanning tree of `H_D`, proving necessity in Theorem 3.1.

Conversely, if `H_D` is connected, it has a labelled spanning tree.  The
tree-compatibility hypothesis says exactly that every graphic forest of
host labels is simultaneously switchable and that its component effect is
contraction of that forest.  A spanning tree therefore produces one
connected spanning two-factor, hence one Middle-Levels Hamilton cycle.
Every selected switch avoids `D` by definition of `H_D`.

Thus

\[
 \text{a transparent pull tree exists}
 \iff H_D\text{ is connected}.
\]

The cut formulation

\[
 \delta_H(X)\nsubseteq B_D
 \quad(\varnothing\ne X\subsetneq\operatorname{Comp}(F))
\]

is the standard multigraph connectivity criterion; loops, if present, do
not cross any cut and are irrelevant.

If a pull set `A` is preselected, a spanning tree containing it exists
exactly when `A` is a graphic forest of the connected graph `H_D`.
Corollary 3.2 is therefore an exact application of graphic-basis
extension.  Parallel host labels cause no issue: two parallel labels form
a graphic 2-cycle and cannot both belong to the prescribed forest.

## 3. Forbidden-host load

For each factor edge `d`, let

\[
 \lambda(d)=|\{e:d\in O_e\}|,
 \qquad \lambda=\max_d\lambda(d).
\]

Every forbidden host edge contains at least one incidence with a member of
`D`.  Double-counting these incidences gives

\[
 |B_D|
 \le \sum_{d\in D}\lambda(d)
 \le |D|\lambda
 =2p\lambda.
\]

If the edge-connectivity of `H` exceeds `2p lambda`, deletion of `B_D`
cannot disconnect it.  The strict inequality in the theorem is necessary
for this purely cardinal bound: a minimum cut may have exactly
`2p lambda` edges.

For the canonical GMN family, pairwise edge-disjoint pull circuits imply
that an old factor edge belongs to at most one pull old phase, so
`lambda=1`.  The cited canonical-host theorem identifies a unique star
bridge, hence edge-connectivity one.  If the old phase of that bridge meets
`D`, the bridge is removed and the transparent host disconnects.  This
validly shows that low pull load alone does not imply a protected pull
tree.

## 4. Composition with wedge packing

The protected wedge-packing theorem supplies a `2p`-edge protected bank
with the required owner and q1 distinctions.  Its protected-factor row
supplies some two-factor `F` containing that bank.  The new theorem adds no
hidden requirement between those two steps: once a tree-compatible host
for that same `F` satisfies the protected cut condition, Theorem 3.1
Hamiltonizes `F` while retaining every protected incidence.

Therefore the implication

\[
 \text{wedge packing}
 \to F\supseteq D
 \xrightarrow{\operatorname{PPC}(F,D,H)}
 \text{Hamilton cycle containing }D
\]

is correct.  `PPC` is necessary and sufficient only inside the specified
host.  A different pull family or a Hamilton cycle unrelated to the host
may exist even when `PPC` fails; the theorem states this limitation.

## 5. Static-host quantifier obstruction

At a lower vertex `L` of a two-factor there are exactly two incident factor
edges.  Consequently there is exactly one unordered full wedge at `L`
supported by that fixed factor.  On the `(2m-1)`-element ground set,
`|L|=m-1`, so its complement has size `m` and the complete wedge menu at
`L` has size

\[
                         \binom m2.
\]

Deleting the unique factor-supported pair leaves
`binom(m,2)-1` candidates and none is supported by the fixed factor.  This
proves Theorem 6.1 and shows that even an asymptotically full local menu
cannot be embedded into a factor chosen independently of that menu.

This is a quantifier obstruction, not a nonexistence theorem.  It leaves
open exactly the two routes stated in the theorem:

1. select wedges, factor, and host jointly; or
2. select wedges first and prove that an adaptive factor completion has
   `PPC`.

## 6. Dependency and scope audit

The proof uses only the following imported statements:

1. the protected wedge bank can be extended to some spanning two-factor;
2. a static tree-compatible pull family acts on component forests by
   graphic contraction;
3. the canonical GMN pull circuits are pairwise edge-disjoint; and
4. the standard labelled plane-tree pull host has its star bridge.

No portal-to-pull identification is assumed.  Indeed, Corollary 3.2
isolates it as an additional premise: prescribed portal labels must first
be realized as actual transparent host edges forming a graphic forest.

No full protected-state claim is made.  To protect residence rails,
upper-witness tickets, compiler cells, or common-cap resources, their
physical support and incompatibilities must be incorporated into the
forbidden-host definition.  The current theorem protects exactly the
factor incidence support `D` and the q1 turn value forced by that support.

## 7. Final verdict

All logical directions, cardinal bounds, and quantifiers check.

The exact topology frontier is therefore

\[
 \boxed{H-B_D\text{ connected}.}
\]

What remains open is an existence theorem producing this cut condition
jointly with the protected wedge bank (or a redundant noncanonical host
whose cut expansion makes it automatic).  The audited theorem neither
assumes nor claims that missing existence result.
