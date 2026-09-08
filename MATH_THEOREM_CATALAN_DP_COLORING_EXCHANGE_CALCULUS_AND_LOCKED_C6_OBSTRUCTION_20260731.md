# Conflict-free colourings do not by themselves supply a local exchange reservoir

Date: 2026-07-31  
Status: exact two-colour exchange calculus; an infinite linear-host
obstruction; and a literal locked-`C6` pair inside the fixed-`Q`, `n=3`
capacity-slot hypergraph.  These results do **not** refute the
Delcourt--Postle near-forest theorem.  They show that its whole colouring
cannot be called a local alternating-circuit reservoir without an additional
geometric or multi-colour argument.

## 1. Exact conflict graph of two colour classes

Let `G` be an `r`-uniform hypergraph and let `M,N` be two matchings in `G`.
Define the bipartite conflict multigraph

\[
 \Gamma(M,N)
\]

with vertex classes `M,N`: for every host vertex used by both matchings,
join the unique two atoms that use it, retaining the host vertex as an edge
label.  Parallel edges are allowed when the same two atoms share several
host vertices.

For `B subseteq N`, let `Gamma(B) subseteq M` be its neighbourhood.

### Theorem 1.1 (exact exchange deficiency)

The hybrid

\[
                  (M\setminus A)\cup B                         \tag{1.1}
\]

is a matching if and only if `Gamma(B) subseteq A`.  Consequently the
largest hybrid using exactly the inserted set `B` is obtained by
`A=Gamma(B)`, and its change in cardinality is

\[
                        |B|-|\Gamma(B)|.                        \tag{1.2}
\]

In particular, a count-neutral two-colour switch exists precisely at a
Hall-tight set `|Gamma(B)|=|B|`.

#### Proof

The atoms of `B` are mutually disjoint.  An atom of `M` must be removed
exactly when it shares a host vertex with one of them.  This is precisely
membership in `Gamma(B)`.  Equation (1.2) is then immediate.  `square`

For a connected component `K` of `Gamma(M,N)`, put `m_K=|K cap M|` and
`n_K=|K cap N|`.  Let `b_M(K)` be the number of host vertices used by its
`M`-atoms but not by `N`, and define `b_N(K)` dually.  Counting the `r`
resources of every atom gives the exact boundary identity

\[
                    r(m_K-n_K)=b_M(K)-b_N(K).                    \tag{1.3}
\]

Thus a whole-component switch is count-neutral exactly when its two
resource boundaries have equal size.

There is one useful aggregate identity for a full proper colouring
`M_1,...,M_t`.  For every fixed colour `c`, properness at each host vertex
gives

\[
 \boxed{\quad
 \sum_{d\ne c}|E(\Gamma(M_c,M_d))|
   =\sum_{v\in V(M_c)}(d_G(v)-1).
 \quad}                                                       \tag{1.4}
\]

Indeed, the `d_G(v)-1` other atoms through `v` all have different colours.
Thus a near-regular host coloured with `D(1+o(1))` colours forces the
*average* two-colour conflict graph to have average degree `r-o(1)`.  It
does not bound component sizes or produce a Hall-tight proper subset; the
obstructions below are regular at equality.

### Corollary 1.2 (identical support can still be globally locked)

If `M,N` cover the same host-vertex set, then `Gamma(M,N)` is `r`-regular
and every connected component is balanced.  Moreover every Hall-tight set
is a union of connected components.  Hence the smallest support-preserving
two-colour exchange has the size of the smallest component, which may be
the full size of the colour class.

#### Proof

Regularity and balance are immediate.  In a connected regular bipartite
graph, a nonempty proper set `B` on one shore satisfies
`|Gamma(B)|>|B|`: equality in the degree count would leave no edge from
`Gamma(B)` to the complementary shore and disconnect the graph.  Apply
this componentwise.  `square`

## 2. An infinite sharp obstruction under the colouring hypotheses

Let `p>=5` be prime, choose four distinct elements
`a_1,...,a_4 in F_p`, and take four vertex parts
`V_i={i} times F_p`.  Put

\[
 e_{x,c}=\{(i,x+a_i c):1\le i\le4\},\qquad x,c\in\mathbb F_p.  \tag{2.1}
\]

This is a four-partite, four-uniform hypergraph with

\[
             \Delta=p,\qquad \Delta_2\le1.                      \tag{2.2}
\]

Colour `e_(x,c)` by `c`.  Every colour class

\[
                         M_c=\{e_{x,c}:x\in\mathbb F_p\}        \tag{2.3}

\]

is a perfect matching, so this is an optimal proper `Delta`-colouring.

### Theorem 2.1 (all two-colour exchanges are global)

For every `c ne d`, the conflict graph `Gamma(M_c,M_d)` is a connected
four-regular bipartite graph.  Therefore there is no nonempty proper
count-neutral switch between any two colour classes.

#### Proof

A red atom indexed by `x` and a blue atom indexed by `y` meet in part `i`
exactly when

\[
                         y=x+a_i(c-d).                           \tag{2.4}
\]

The four values are distinct, giving a simple four-regular graph.  A
two-step walk on the red shore changes `x` by
`(a_i-a_j)(c-d)`.  At least one such difference is nonzero, and every
nonzero element generates the additive group of `F_p`.  Thus the graph is
connected.  Corollary 1.2 finishes the proof.  `square`

This family has a power-saving codegree far stronger than needed by the
colouring theorem, all colour classes are perfect, and nevertheless there
is no proper two-colour exchange at all.  It proves that *proper colouring
plus small codegree* does not force a local alternating-circuit bank.
The Johnson/slot geometry would have to supply additional content.

## 3. The outer-cycle dependency theorem for the capacity-slot host

Return to the four-uniform fixed-`Q` capacity-slot hypergraph.  Suppose
`M,N` are exact on both outer palettes (all punctured lower and all upper
colours).  Retain in `Gamma(M,N)` only the two outer-resource labels.  Every
atom then has degree two, so this outer conflict graph is a disjoint union
of alternating even cycles.

Contract those cycles.  Make a directed dependency graph `D_(M,N)` by
drawing `Z -> Z'` when a slot of a blue atom in outer cycle `Z` is also
used by a red atom in outer cycle `Z'`.

### Theorem 3.1 (phase closure)

A set `S` of outer cycles may be changed from the red phase to the blue
phase while preserving both outer palettes and every slot capacity if and
only if `S` is out-closed in `D_(M,N)`.  In particular every sink strongly
connected component gives a legal count-neutral switch, but its size is
unbounded; if `D_(M,N)` is strongly connected, the only two phases are the
two complete matchings.

#### Proof

Outer-palette preservation forces one of the two alternating phases on
each outer cycle.  Blue atoms are mutually disjoint.  The hybrid is a
slot matching precisely when every red atom sharing a selected blue slot
has also been removed.  After contraction this is exactly the absence of
an arc from `S` to its complement.  `square`

This is the correct deterministic implication of two exact colour classes.
It gives a finite closure system, not independent Boolean circuit choices.

## 4. A literal fixed-`Q` locked pair at `n=3`

On the authenticated `n=3` minus shore, the punctured lower bank is

\[
 \{19,26,28,38,41,49\},
\]

and the upper bank is `\{31,47,55,59,61,62\}`.  The audit below exhibits
two exact capacity-slot matchings `M,N`.  Their outer conflict graph has
two alternating `C6` components (three atoms on each shore per component),
but the slot-dependency quotient has both cross-arcs

\[
                            Z_0\longrightarrow Z_1,
                 \qquad    Z_1\longrightarrow Z_0.               \tag{4.1}
\]

Therefore the two individual `C6` switches are both illegal.  Of the four
phase vectors, exactly

\[
                         00\quad\hbox{and}\quad11                 \tag{4.2}

\]

are feasible.  Each displayed class is itself a physical matching and
therefore avoids every projected-cycle conflict.  Giving `M,N` two colours
and every other atom a singleton colour produces a literal proper
conflict-free colouring with `12 <= D_0=40` colours containing this locked
pair.

The fixture is independently reconstructed and replayed by

```text
scratch/audit_catalan_dp_coloring_locked_c6_n3_20260731.py
scratch/catalan_dp_coloring_locked_c6_n3_20260731.audit.json
```

This finite example is not a no-go for a different colouring or for a
multi-colour exchange.  Its exact scope is that even inside the actual
capacity-slot geometry, outer `C6` circuits need not be independently
switchable and need not be bichromatic repair atoms.

## 5. Consequence for the exact cover-down programme

The full Delcourt--Postle colouring remains useful as a distributed supply
of near-perfect, high-girth matchings.  What it deterministically supplies
is:

1. many large matchings;
2. the conflict-graph deficiency formula (1.2);
3. outer alternating cycles when two classes are outer-exact; and
4. a directed closure problem on those cycles.

It does **not** by itself supply bounded `C6/C8` absorbers, independent
cycle phases, or a serializable ear system.  A valid next theorem must use
additional Johnson geometry or at least three colours, and must prove that
the relevant dependency closure has small sink components or a controlled
ear decomposition.  Simply retaining all colour classes is not yet an
absorber theorem.
