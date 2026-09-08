# The authenticated `6390+45` parent yields a literal lower-rainbow `K17` Hamilton cycle

Date: 2026-07-31  
Status: exact finite theorem, constructed by an integral `b`-flow and independently
replayed; no `K17` word or numerical upper-bound improvement is claimed

## 0. Result

The unrestricted macro flow of Section 7 of
`MATH_THEOREM_K17_GMM_ENDPOINT_ORIENTED_RESIDUAL_FACTOR_20260731.md`
passes for the authenticated two-cycle `K15` parent.  More strongly, one
integral completion is connected.

> **Theorem.** There is a Hamilton cycle on all
> \(\binom{[17]}9\) whose consecutive intersections enumerate
> \(\binom{[17]}8\) exactly once.

The literal cycle is

```text
scratch/k17_parent_induced_macro_port_cycle_20260731.cycle
SHA-256 39cc3abe6a8991dc101a585123989deab863030060c00d3e0a2a60cd73252de6
```

It has `24310` distinct rank-nine owners, `24310` Johnson edges, and `24310`
distinct rank-eight edge intersections.  An independent literal verifier
checks equality with the two complete Boolean layers, rather than only their
cardinalities.

This closes middle ownership, connectivity, and the complete immediate lower
palette for this `K15 -> K17` branch.  It does **not** close residence, deeper
lower shadows, upper shadows, or the common-cap compiler.

## 1. The parent supplies the lower forest directly

Let the two directed parent cycles have owner sequences \(T_i\), of lengths
`6390` and `45`, and put

\[
 C_i=T_i\cap T_{i+1}.
\]

The \(C_i\) enumerate all rank-seven subsets of `[15]`.  Consecutive
intersections

\[
 Z_i=C_i\cap C_{i+1}
\]

have rank six and the exact multiplicity profile

\[
                    1^{3630}2^{1320}3^{55}.          \tag{1.1}
\]

In particular every one of the `5005` rank-six colours occurs.  Retain the
first occurrence of every \(Z\), in the authenticated component order.  The
retained `5005` edges form a spanning linear forest on the `6435` vertices
\(C_i\).  The deleted-edge counts on the two parent cycles are

\[
                         1405+25=1430.               \tag{1.2}
\]

Thus the forest has exactly `1430 = Cat_8` naturally oriented paths and both
parent cycles receive endpoints.

For comparison, the parent upper unions have multiplicity profile

\[
                    1^{3675}2^{1230}3^{100}.         \tag{1.3}
\]

The occurrence graph which pairs \(Z_i\) with \(T_i\cup T_{i+1}\) has
maximum matching only `4425/5005`.  Hence a common parent-index transversal
does not explain the construction; the unrestricted port flow is genuinely
needed.

## 2. The literal macros form a port forest

Orient every retained \(C\)-path in the forward parent direction and use the
left `X` socket and right `Y` socket from the endpoint-coupling construction.
Constructing the full physical residual graph on all `A/X/Y` owners gives
exactly `1430` paths.  Reading each from its free `X` endpoint to its free `Y`
endpoint produces a directed port edge on rank-eight old-owner colours.

The resulting macro port graph has

\[
  \deg_{\cal P}(T):\qquad 0^{4021}1^{1968}2^{446},   \tag{2.1}
\]

and is a linear forest with exactly `5005` components.  It has no loop, no
cycle, and maximum degree two.  Only

\[
                          78/1430                   \tag{2.2}
\]

macro port edges are Johnson edges.

Equation (2.2) is an important scope check.  The coupled-tight-enumeration
subclass from Section 6 would reject this successful construction.  A macro
is an atomic physical path, so its two external colours need not themselves
be a Johnson pair.

## 3. Exact integral completion

Let \({\cal T}=\binom{[15]}8\), \({\cal U}=\binom{[15]}9\), and define

\[
 d_T=2-\deg_{\cal P}(T).
\]

Then

\[
 d_T:\qquad 0^{446}1^{1968}2^{4021},
 \qquad \sum_Td_T=10010=2|{\cal U}|.                \tag{3.1}
\]

Use the integral network

\[
 s\longrightarrow U\longrightarrow T\longrightarrow t,
\]

with source capacities two, unit containment arcs \(U\supset T\), and sink
capacity \(d_T\).  The deterministic adjacency shuffle with seed `74`,
followed by Dinic's algorithm, has flow value

\[
                         10010/10010.                \tag{3.2}
\]

The two selected facets of each \(U\) define one \(U\)-labelled Johnson
edge on \({\cal T}\).  Adding these `5005` edges to the fixed `1430` macro
edges gives a connected two-regular graph on all `6435` members of
\({\cal T}\): it is one Hamilton port cycle.

Expand every macro edge to its literal residual `A/X/Y` path and every
\(U\)-edge to its one `U` owner.  The expansion has

\[
 3\cdot6435+5005=24310
\]

owners.  The owner sectors partition \(\binom{[17]}9\), while the internal
macro colours and the port-cycle colours partition \(\binom{[17]}8\).
The independent literal replay verifies both partitions and every Johnson
adjacency.  This proves the theorem.

The chosen undirected completion traverses `751` macros from `X` to `Y` and
`679` from `Y` to `X`.  Thus it does not certify the optional globally
oriented macro-coherence strengthening.

## 4. Downstream census

The new cycle is not directly consumable by the existing depth-three erosion
compiler.

### Lower decks

\[
\begin{array}{c|c|c|c}
q&\text{target rank}&\text{distinct}&\text{missing}\\ \hline
1&8&24310&0\\
2&7&17825&1623\\
3&6&11363&1013
\end{array}                                           \tag{4.1}
\]

At width four, `1063` occurrences still have rank seven rather than rank
six.

### Upper intervals

\[
\begin{array}{c|r|r}
\text{rank}&\text{distinct}&\text{missing}\\ \hline
10&17557&1891\\
11&11466&910\\
12&6060&128\\
13&2377&3\\
14&680&0\\
15&136&0\\
16&17&0\\
17&1&0
\end{array}                                           \tag{4.2}
\]

### Residence and best opening

The cyclic positive-coordinate run census has

\[
                    1063\text{ runs of length }2,
 \qquad             1829\text{ runs of length }3.  \tag{4.3}
\]

There are no length-one runs.  Exhausting all `24310` possible opening
edges, the best cut is edge `142`, whose lost lower colour is decimal
`109378`.  It makes only three short runs into boundary runs, leaving

\[
                             2889                    \tag{4.4}
\]

short internal runs.  Therefore no current depth-three maximal-erosion
compiler can consume this cycle unchanged.  The later parent-universal
residence audit shows that `165` forced short patterns survive every retained
\(Z\)-occurrence choice for this parent.  Thus neither port-flow optimization
nor a different occurrence transversal can close residence here; one needs a
different parent/macro-interior construction or a nonflat compiler.

## 5. Dimension-uniform sufficient rule

The construction extracts one exact reusable lemma.  Let
\(|\Omega|=2r-1\), let \(F\) be a directed lower-rainbow Johnson 2-factor
on \(\binom\Omega r\), and index its lower colours by

\[
 C_i=T_i\cap T_{\operatorname{succ}(i)}.
\]

Assume the induced edges \(C_iC_{\operatorname{succ}(i)}\) collectively
cover every \(Z\in\binom\Omega{r-2}\).  Select one physical occurrence of
every \(Z\), and assume at least one unselected edge remains on every parent
cycle.  Retaining the selected edges gives a spanning linear forest on the
\(C\)-deck with

\[
 {2r-1\choose r-1}-{2r-1\choose r-2}=\operatorname{Cat}_r
\]

components.

Orient each retained path forward.  If its first and last lower-colour
indices are \(\alpha\) and \(\beta\), let \(A\) be the set of all first
indices and \(B\) the set of all last indices on the same parent component.
Under the left-`X`/right-`Y` socket convention, its literal macro ports are

\[
 \ell(\alpha,\beta)
   =T_{\operatorname{succ}(\operatorname{prev}_A(\alpha))},
 \qquad
 h(\alpha,\beta)
   =T_{\operatorname{next}_B(\beta)}.               \tag{5.1}
\]

Here `prev` and `next` are cyclic among endpoint occurrences on the same
parent component.  Formula (5.1) is obtained by following the free end of
the corresponding cut `X`-rail and `Y`-rail segment.

### Theorem 5.1 (parent-induced macro-flow lift)

Suppose additionally that:

1. the port edges (5.1) are loopless and form a linear forest on
   \(\binom\Omega r\); and
2. the integral residual flow

   \[
     \deg(U)=2,qquad
     \deg(T)=2-\deg_{\cal P}(T)                      \tag{5.2}
   \]

   has a solution whose union with the macro port forest is connected.

Then the four-sector lift on \(\Omega\cup\{x,y\}\) has a Hamilton cycle on
all rank-\((r+1)\) owners whose consecutive intersections enumerate the
complete rank-\(r\) layer exactly once.

#### Proof

The selected \(Z\)-edges and endpoint sockets give the literal disjoint
`A/X/Y` macro paths, with their three internal lower-colour classes each
bijective.  Condition (5.2) chooses two rank-\(r\) facets of every pure
rank-\((r+1)\) owner `U` and uses every residual port capacity.  Reinsert the
fixed macro incidences.  Degree two gives a port two-factor; connectedness
makes it one cycle.  Expanding its macro edges gives one owner cycle.  Its
internal macro colours and its port vertices are the four disjoint Pascal
classes of the child rank-\(r\) layer, each once. \(\square\)

Thus the exact all-\(r\) central target is no longer “couple two tight
enumerations.”  It is:

> construct a lower-rainbow parent whose induced lower-colour cycles admit
> a covering occurrence transversal for which (5.1) is a linear forest and
> the residual containment flow (5.2) has a connected solution.

This theorem concerns only ownership and immediate lower colour.  A general
construction still has to impose residence, upper service, and compiler
compatibility on the parent/macro interiors.

## 6. Reproducibility

Primary constructor and audit:

```text
scratch/audit_k17_parent_induced_macro_port_cycle_20260731.py
scratch/k17_parent_induced_macro_port_cycle_20260731.audit.json
```

Independent literal verifier:

```text
scratch/verify_k17_parent_induced_macro_port_cycle_20260731.py
scratch/k17_parent_induced_macro_port_cycle_20260731.verify.json
```

The primary audit reconstructs the parent colours, forest, literal residual
paths, macro ports, integral flow, connected port cycle, and expanded K17
cycle from the authenticated source.  The independent verifier reads only
the final cycle and checks the full owner and intersection layers.
