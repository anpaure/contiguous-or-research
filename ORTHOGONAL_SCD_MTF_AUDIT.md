# Auxiliary SCD adjacencies versus exact move-to-front transitions

This note audits a natural global proposal for the universal contiguous-OR
problem.  Fix one symmetric chain decomposition `D`, regard its chains as
vertices, and use the edges of a second edge-disjoint or orthogonal SCD `E`
to join the corresponding `D`-chains.  The hope is that the resulting chain
graph can be threaded by genuine one-step arbitrary-mask move-to-front (MTF)
updates.

The conclusion has two parts.

1. Edge-disjointness and orthogonality do **not** imply MTF compatibility.
   There is a simple exact local obstruction at every cross edge.
2. The published Gregor--Micka--Mutze cycle ordering of the
   Greene--Kleitman chains also does not evade the obstruction.  Its recursive
   four-chain blocks contain at most one generically usable internal MTF
   adjacency, so the ordering has a linear number of breaks.

The positive information is that the local obstruction is cheap to test and
applies to *any* number of auxiliary SCDs.  It identifies exactly what a new
global braid must preserve in addition to cube adjacency.

The exact state-fiber and quotient-chain theorems used below are proved in
`MTF_TRANSVERSAL.md`.  The two published SCD constructions being audited are
[Gregor--Jager--Mutze--Sawada--Wille, *Gray codes and symmetric
chains*](https://arxiv.org/abs/1802.06021) and
[Gregor--Micka--Mutze, *On the central levels
problem*](https://arxiv.org/abs/1912.01566).

## 1. The projected auxiliary-SCD graph

Let `D` and `E` be two SCDs of `B_k`.  For a set `S`, write `C_D(S)` for its
chain in `D`.  Every edge

\[
                  u\subset v=u\cup\{x\}
\tag{1.1}
\]

of `E` projects to an edge between the vertices `C_D(u)` and `C_D(v)`.
If the two SCDs are edge-disjoint, these two chains are distinct.  If they
are orthogonal, the vertices seen while walking along one `E`-chain are also
distinct, so that one `E`-chain projects to a simple path in the quotient.

Neither property says anything about ordered-partition recency states.  The
following theorem gives the missing test.

Write a saturated chain as

\[
 C=(B; e_1,\ldots,e_h)
  =\bigl(B,B+e_1,\ldots,B+e_1+\cdots+e_h\bigr),
\tag{1.2}
\]

and write `b(C)=B` and `t(C)=B+e_1+...+e_h`.

### Theorem 1 (cross-edge anchor obstruction)

Let (1.1) join two distinct chains `C=C_D(u)` and `F=C_D(v)` of the same
saturated chain decomposition.

1. If `b(F)` is nonempty and there is a one-step MTF transition from some
   state exposing `C` to some state exposing `F`, then

   \[
                         x\in b(F).                  \tag{1.3}
   \]

2. If `b(C)` is nonempty and there is a one-step MTF transition from some
   state exposing `F` to some state exposing `C`, then

   \[
                         u=t(C).                     \tag{1.4}
   \]

The only unhandled target in either statement is the unique chain whose
minimum is empty.

#### Proof

For the first direction, write

\[
 F=(A;f_1,\ldots,f_g),\qquad
 F_j=\{f_1,\ldots,f_j\},\qquad v=A\cup F_j.
\]

The quotient-chain theorem says that `C-A` and `F-A` must be cross-nested.
Suppose that `x` is not in `A`.  Then `x` is one of the first `j` target
increments and

\[
                 u-A=F_j-\{x\}.                     \tag{1.5}
\]

A `(j-1)`-subset of `F_j` is comparable with every prefix
`emptyset,F_1,...,F_j` only when it is `F_(j-1)`.  Hence `x=f_j` and

\[
                 u=A\cup F_{j-1}.                   \tag{1.6}
\]

But (1.6) is the preceding member of the chain `F`, contradicting that `u`
lies in the distinct chain `C`.  This proves (1.3).

For the reverse direction write `C=(B;e_1,...,e_h)` and
`u=B+E_i`, where `E_i={e_1,...,e_i}`.  Cross-nesting now forces

\[
                       v-B=E_i\cup\{x\}              \tag{1.7}
\]

to be comparable with every target prefix `E_0,...,E_h`.  A set comparable
with all these prefixes is either one of the prefixes or contains `E_h`.
In the first case, (1.7) forces `x=e_(i+1)`, making `v` the next member of
`C`, again a contradiction.  In the second case, a prefix plus one new
coordinate can contain `E_h` only if either `i=h`, or `i=h-1` and
`x=e_h`.  The latter is the same forbidden next-member case.  Thus `i=h`
and `u=t(C)`, proving (1.4).  QED.

### Consequence

For an upward auxiliary edge, a forward MTF arc can only add a coordinate
which is already frozen into the minimum of the target chain.  A reverse MTF
arc can only leave the top of its target chain.  Ordinary cube adjacency,
even when supplied by an orthogonal SCD, has neither property built into its
definition.

The conditions are necessary, not sufficient.  The remaining members of
the two quotient chains must still pass the complete prefix-fence test.

### Small exact counterexample

In `B_4`, take the standard Greene--Kleitman SCD `D_0` and its complementary
edge-disjoint SCD.  The latter contains the edge

\[
                         \{3\}\subset\{2,3\}.        \tag{1.8}
\]

In `D_0`, the lower endpoint lies in the chain with template `*01*`, while
the upper endpoint lies in the chain `01**`.  The added coordinate `2` does
belong to the target minimum, so (1.3) passes.  Nevertheless, after
quotienting by the target minimum `{2}`, the two chains contain respectively

\[
 \{3\}\subset\{1,3\}\subset\{1,3,4\},
 \qquad
 \varnothing\subset\{3\}\subset\{3,4\}.             \tag{1.9}
\]

The sets `{1,3}` and `{3,4}` cross.  Thus (1.8) is not an MTF transition in
that direction, and the reverse direction fails (1.4).  This is an explicit
edge of a standard auxiliary SCD which gives no directed edge at all in the
MTF chain-fiber graph.

## 2. First-pair versus last-pair connectors

For a Greene--Kleitman template `C` with at least two stars, let

* `f(C)` replace the first two stars by `0,1`;
* `ell(C)` replace the last two stars by `0,1`.

If

\[
                  C=(B;e_1,\ldots,e_h),              \tag{2.1}
\]

then

\[
\begin{aligned}
 f(C)&=(B+e_2;e_3,\ldots,e_h),\\
 \ell(C)&=(B+e_h;e_1,\ldots,e_{h-2}).                 \tag{2.2}
\end{aligned}
\]

The last-pair direction is the genuine MTF move already proved in
`GLOBAL_MTF_SCD_HANDOFF.md`:

\[
                         C\longrightarrow\ell(C).     \tag{2.3}
\]

The superficially symmetric first-pair direction is not genuine.

### Lemma 2 (first-pair fence)

If `h>=3`, there is no MTF transition `C -> f(C)`.  If `B` is nonempty,
there is no transition `f(C) -> C` for any `h>=2`.

#### Proof

For `C -> f(C)`, quotient by the target minimum `B+e_2`.  The source
quotient contains the singleton `{e_1}`, while the first nonempty target
quotient member is `{e_3}`.  They are incomparable when `h>=3`.

For `f(C) -> C`, quotient by `B`.  The source quotient begins with
`{e_2}`, while the target quotient begins with `{e_1}`.  Again they are
incomparable.  QED.

The reverse last-pair direction is equally rigid.  If `B` is nonempty, then
`ell(C)-B` begins with `{e_h}`, whereas `C-B` begins with `{e_1}`; hence
`ell(C) -> C` fails.  If `B` is empty, apply the special target anchor
`{e_1}`.  For `h>=3` the residual source begins with `{e_h}` while the
residual target begins with `{e_2}`, so it still fails.  The sole exception
is the two-star longest chain.

There are only boundary exceptions:

* if `h=2`, then `f(C)` is a singleton chain and `C -> f(C)` is allowed;
* if `B` is empty, the target is the unique longest chain and the separate
  empty-minimum anchor rule applies.

Both exception families are negligible in the asymptotic chain count.

The asymmetry between `f` and `ell` is not a cosmetic convention.  Prefix
unions impose a direction on the star word, and move-to-front preserves that
direction after deletion.

## 3. Audit of the Gregor--Micka--Mutze cycle ordering

Gregor--Micka--Mutze construct a Hamilton cycle containing every
Greene--Kleitman chain.  Their recursive cycle ordering `Lambda_n` replaces
almost every parent chain `C` by four descendants.  In even dimension the
unreversed descendant block is

\[
 *C*,\quad f(*C*),\quad f(\ell(*C*)),\quad \ell(*C*), \tag{3.1}
\]

and in odd dimension it is

\[
 *C*,\quad \ell(*C*),\quad \ell(f(*C*)),\quad f(*C*).\tag{3.2}
\]

Some blocks are reversed.  Parents of the shortest possible length have a
two- or three-descendant exceptional rule.

The cube Hamilton cycle joins consecutive chains at alternating top and
bottom endpoints.  Those endpoint edges are exactly what is needed to join
the *full cube paths*.  They are not automatically MTF transitions between
the compressed chain fibers.

### Theorem 3 (linear-break obstruction for `Lambda_n`)

Among the three internal directed adjacencies of any ordinary four-chain
descendant block, at most one is a one-step MTF transition.  Consequently,
even if every connector between two consecutive descendant blocks is
declared usable, the cyclic order `Lambda_n` has at most

\[
                         (1/2+o(1))W(n+2)             \tag{3.3}
\]

usable directed adjacencies.  Any MTF path cover constrained to this order
therefore has at least

\[
                         (1/2-o(1))W(n+2)             \tag{3.4}
\]

components.

#### Proof

In (3.1), the only generic forward last-pair relation is

\[
             f(*C*)\longrightarrow
             \ell(f(*C*))=f(\ell(*C*)).              \tag{3.5}

The first adjacency is a forbidden first-pair move, and the third is the
reverse of a first-pair move.  Reversing the four-chain block cannot create
more than one last-pair direction.

In (3.2), the first adjacency is the last-pair move
`*C* -> ell(*C*)`; the second is a first-pair move, and the third reverses a
last-pair move.  After reversing the block, at most one last-pair direction
again remains.  Lemma 2 and the quotient-prefix test exclude the other
generic directions.

There is at most one internal usable edge per parent block, and at most one
inter-block connector per parent block.  Thus there are at most twice as
many usable directed edges as parent chains, apart from the shortest-chain
exceptions.  The number of shortest Greene--Kleitman chains is `o(W(n))`,
while

\[
                         W(n+2)=(4-o(1))W(n).          \tag{3.6}

\]

This proves (3.3).  A directed path cover using `E` edges on `W(n+2)`
vertices has at least `W(n+2)-E` components, proving (3.4).  QED.

Already in dimension four the order is

```text
****, 01**, 0101, **01, 0011, *01*
```

up to cyclic rotation and reversal.  The transition `**** -> 01**` fails:
after quotienting by the target minimum `{2}`, the source contributes
`{1}` before the target requires `{3}`.  Thus the failure is present at the
first nontrivial recursive step, not only asymptotically.

## 4. The central-diamond graph is unchanged by the cycle ordering

There is a second graph which should not be confused with the endpoint
connector graph.  Every SCD of `B_(2m)` pairs an `(m-1)`-set `S` with the
`(m+1)`-set `U` two steps above it.  The two intermediate middle sets define
a Johnson edge with intersection `S` and union `U`.  For the
Greene--Kleitman SCD these edges form the two-sided rainbow forest from
`GK_TWO_SIDED_RAINBOW_FOREST.md`.

The Gregor--Micka--Mutze theorem orders the same Greene--Kleitman chains; it
does not change this central-diamond map.  The exact indegree law from
`GK_PROJECTION_COUNTS.md` is

\[
 \#\{X:\deg^-(X)=j\}=\binom{2m-j-1}{m-j},             \tag{4.1}
\]

so the limiting indegree distribution is

\[
                         P(J=j)=2^{-(j+1)}.            \tag{4.2}

\]

In particular, asymptotically one quarter of all middle vertices branch.
The former assertion that any linear subforest retains at most `W/2` edges
was false and is retracted.  Exact optimization requires the rooted-tree DP
in `MATH_CORRECTION_GK_PROJECTION_LINEAR_SUBFOREST_TREE_DP_20260731.md`,
whose retained-edge values for `m=3,...,7` are
`13,44,159,588,2188`.  The original projection is still not itself a
`Cat_m`-component path factor because it branches, and merely rereading the
same edges in Hamilton-cycle order does not change that fact; no asymptotic
linearization bound is asserted here.

## 5. What remains viable

The audit rules out the direct implications

```text
edge-disjoint/orthogonal SCDs
    => projected cube adjacencies are MTF transitions

Greene--Kleitman cube Hamilton ordering
    => compressed MTF tour of Greene--Kleitman chains.
```

It does **not** rule out using several SCDs after a new state-aware selection
step.  A viable theorem would have to choose edges satisfying the full
quotient-prefix fence and simultaneously choose inherited ordered-partition
states so that consecutive witnesses compose.  The auxiliary chain graph
must therefore be decorated by at least:

1. the target minimum used as the new MTF anchor;
2. the target increment-prefix order after deleting that anchor; and
3. the residual block refinement inherited by the following edge.

Orthogonality controls only set intersections between chains and lexical
edge-disjointness controls only cube edges.  Neither controls these three
recency data.  Any future expansion argument must be run in this decorated
state graph, not in the bare quotient on chain labels.
