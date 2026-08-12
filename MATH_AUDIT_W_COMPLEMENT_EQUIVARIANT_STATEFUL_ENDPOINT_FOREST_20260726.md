# Audit of complement-equivariant stateful endpoint forests

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or
web input is used.

## 0. Verdict

**Subsequent sharp update.**  For the standard BTK product-SCD, the
uniform reachable-state mixing sought below is false.  The natural queue
produced by almost every complete atom makes both endpoint orientations
exact sinks already for \(H\ge7\); see
`MATH_THEOREM_W_BTK_H_MEMORY_ENDPOINT_SINK_OBSTRUCTION_20260726.md`.
Sections 5--8 below remain valid as average/conditional statements, but
they are not a live proof route for that fixed-colour complete-atom
catalogue.

The static residence-free endpoint graph in
`MATH_THEOREM_ONE_SIDED_PRODUCT_SCD_FLAG_FUSION_AND_RESIDENCE_DICHOTOMY_20260726.md`
is not sufficient for an iterated forest. Pairwise-safe seams can create a
positive residence across an intervening short path. Theorem 7.1 of that
note must therefore be retracted in its static-graph form.

The exact repair is an `H`-memory automaton. Before every new transition it
retains the insertion and deletion labels from the preceding `H-1`
transitions. A new deletion may not equal a retained insertion, and a new
insertion may not equal a retained deletion. When an atom is appended, its
seam and all of its internal transitions must be processed sequentially.
This detects every nonadjacent seam interaction.

Complement/reversal gives an exact two-sided theorem. If a route family is
closed under

\[
 (X_0,X_1,\ldots,X_s)^\dagger
 =(X_s^c,X_{s-1}^c,\ldots,X_0^c),                  \tag{0.1}
\]

and **every whole route** is lower `H`-safe, then every route is also upper
`H`-safe and

\[
                         M_q^+=M_q^-               \tag{0.2}
\]

for the numbers of physical missing upper and lower targets. Pairing
static arcs is not enough; the paired routes must pass the automaton.

For `m\ge2`, there are no fixed path or fixed seam orbits under `\dagger`.
Self-complementary cycles have length at least `2m`, so their total number
is at most `W/(2m)=o(W/H)` when `H=o(m)`.

The proposed endpoint-degree scale has a valid average precursor. If
`\mathcal E` is the set of product-SCD path endpoints, then

\[
 {1\over|\mathcal E|}
 \sum_{X\in\mathcal E}|N_J(X)\cap\mathcal E|
 \ge\left({4\over\sqrt\pi}+o(1)\right)m^{3/2}.      \tag{0.3}
\]

If a candidate active set were a uniform `h`-set, its exact survival
against an independent forbidden `f`-set would be

\[
                         {\binom{m-f}h\over\binom mh}.           \tag{0.4}
\]

At `H=\sqrt m\,\omega`, `h=O(\sqrt m)`, this is
`\exp[-O(\omega)]`; for `\omega=\log\log m` it is only a polylogarithmic
loss. A fully rigorous averaged version remains true after restricting to
paths of length at most `\sqrt{3m\log m}` and gives average surviving
degree `m^{3/2-o(1)}` for `\omega=o(\sqrt{\log m})`.

What is not proved is the required **uniform dynamic mixing**: the actual
active sets of a fixed SCD need not be hypergeometric relative to a
reachable history queue, and (0.3) is an average degree, not a minimum or
Hall-expansion statement. Consequently no state-valid near-spanning path
cover follows from the current inputs. The exact missing lemma is stated
in Section 8.

## 1. Static pairwise safety is false

Write a transition as

\[
                         X_t=X_{t-1}-a_t+b_t.        \tag{1.1}
\]

Take five distinct coordinates `a,b,x,y,z`, with `a,b` initially present
and `x,y,z` initially absent, and use the three transitions

\[
                         -a+x,qquad -b+y,qquad -x+z.            \tag{1.2}
\]

Each transition is literal. The first two pieces are pairwise lower-safe
because the second removal is `b\ne x`; the last two are pairwise
lower-safe because the last removal is `x\ne y`. Thus a static graph which
tests only the two paths incident to each seam accepts both joins.

The full three-edge route is not lower-safe at depth three. The first edge
inserts `x` and the third removes it, so its inclusive positive residence
has length three. If the initial owner is `S`, the four-owner intersection
is

\[
                         S\setminus\{a,b\},         \tag{1.3}
\]

of size `m-2`, rather than `m-3`. The intervening path need not touch `x`.
This is exactly the nonadjacent interaction in the audit request.

The example embeds for `3\le H\le m` by inserting `H-3` transitions on
fresh coordinates between the first insertion and final removal. Hence no
static pair graph on original atoms can certify an iterated forest.

## 2. The exact `H`-memory automaton

For a transition word (1.1), define before edge `t`

\[
\begin{aligned}
 I_t&=(b_j:\max\{1,t-H+1\}\le j<t),\\
 D_t&=(a_j:\max\{1,t-H+1\}\le j<t).
\end{aligned}                                        \tag{2.1}
\]

The order records ages; membership is all that is needed for the next
edge. Accept `-a_t+b_t` exactly when

\[
                         a_t\notin I_t,qquad b_t\notin D_t.     \tag{2.2}
\]

After acceptance, delete entries older than `H-1` transitions and append
`b_t` to `I_t` and `a_t` to `D_t`.

### Theorem 2.1 (two-sided state criterion)

A Johnson path has correct lower and upper shadow ranks at every depth
`q\le H` if and only if every transition is accepted by (2.2).

#### Proof

The lower rank fails in a `q`-window exactly when a coordinate inserted on
an earlier edge is removed on a later edge in that window. Thus lower
safety is equivalent to

\[
                         b_i\ne a_j
 \quad(i<j,\ j-i+1\le H),                           \tag{2.3}
\]

which is the first condition in (2.2). Dually, the upper rank fails exactly
when a coordinate removed earlier is reinserted later, so upper safety is
equivalent to

\[
                         a_i\ne b_j
 \quad(i<j,\ j-i+1\le H),                           \tag{2.4}
\]

the second condition. `\square`

When appending a path atom, process the seam edge first and then every
internal edge of the atom. If the atom has fewer than `H` transitions, the
state leaving it still contains labels from earlier atoms. This is exactly
what the static graph discarded.

### Corollary 2.2 (stateful replacement for the static forest)

An ordered sequence of internally safe path atoms gives an `H`-safe fused
route if and only if its seams and atom transitions are accepted
sequentially by the automaton. This statement is both necessary and
sufficient and includes all nonadjacent seam interactions.

## 3. Complement/reversal transfers lower to upper exactly

For a route `R=(X_0,\ldots,X_s)`, define `R^\dagger` by (0.1). A transition
`X_{t-1}\to X_t=X_{t-1}-a_t+b_t` becomes, in `R^\dagger`, the transition

\[
                         X_t^c\longrightarrow X_{t-1}^c
 =X_t^c-a_t+b_t.                                    \tag{3.1}
\]

Thus the reversed-complement transition word is

\[
                         (a_s,b_s),(a_{s-1},b_{s-1}),\ldots,(a_1,b_1).
                                                               \tag{3.2}
\]

For every `q`-window one has the exact identities

\[
 L_q^{R^\dagger}(s-i-q)=\bigl(U_q^R(i)\bigr)^c,qquad
 U_q^{R^\dagger}(s-i-q)=\bigl(L_q^R(i)\bigr)^c.     \tag{3.3}
\]

### Theorem 3.1 (exact complement-equivariant forest lemma)

Let `\mathcal F` be an owner-disjoint family of directed routes such that:

1. `R\in\mathcal F` if and only if `R^\dagger\in\mathcal F`;
2. every route, including every dagger mate, is accepted by the **lower**
   insertion-memory half of the automaton; and
3. the underlying owner set is complement-closed.

Then:

* every route is lower and upper `H`-safe;
* the physical target sets satisfy

  \[
  \mathcal U_q(\mathcal F)
   =\{T^c:T\in\mathcal L_q(\mathcal F)\};           \tag{3.4}
  \]

* lower injectivity is equivalent to upper injectivity; and
* the missing target counts obey `M_q^+=M_q^-` exactly for every
  `q\le H`.

The same equality holds for changes relative to any complement-equivariant
baseline. Hence a zero or constant aggregate lower missing-shadow bound
automatically gives the identical upper bound.

#### Proof

The lower automaton gives lower safety. Applied to `R^\dagger`, it gives
lower safety of the mate, which is upper safety of `R` by (3.3). Thus the
two lower-memory tests on an orbit are equivalent to the two-sided test
(2.2) on one representative. Equation (3.3) proves (3.4).
Complementation is a bijection between the two target layers, so used-set
cardinalities, collisions, and holes correspond exactly. `\square`

The route-level hypothesis is indispensable. Pairing a static arc
`P\to Q` with `Q^\dagger\to P^\dagger` checks only one boundary on each
side. It neither detects (1.2) nor proves that the assembled primal and
mirror routes remain automaton-valid.

Operationally, extending a primal route on the right by an atom `Q`
extends its mirror route on the **left** by `Q^\dagger`. A paired greedy
algorithm must maintain both whole boundary states simultaneously.

## 4. Fixed and self-complementary orbits

### Proposition 4.1 (no fixed path components)

For `m\ge2`, no nonempty simple Johnson path is fixed by `\dagger`, even as
an unoriented path graph. No literal endpoint seam is fixed by the induced
arc involution.

#### Proof

If a directed path with `s` edges satisfied `R=R^\dagger`, then

\[
                         X_i=X_{s-i}^c.             \tag{4.1}
\]

If `s` is even, the middle vertex would equal its complement, impossible.
If `s` is odd, the two middle vertices would be complements. Their Johnson
distance is `m`, so they are not adjacent when `m\ge2`.

Every automorphism of an unoriented finite path is the identity or the
reversal. The identity would fix every owner under complementation; the
reversal is the preceding case. Thus no unoriented fixed path exists.

A fixed arc would join a component to its complement mate and would have
to join an endpoint `X` to `X^c`, again impossible for `m\ge2`. `\square`

Consequently all path and seam orbits have size two. A complement-equivariant
path forest has an even number of physical components and its constructions
may be performed on one representative of each orbit, with the mirror
operation forced.

### Proposition 4.2 (self-dual cycles are negligible)

Every self-complementary simple Johnson cycle has length at least `2m`.
Hence an owner-disjoint family contains at most

\[
                         {W\over2m}=o(W/H)           \tag{4.2}
\]

such cycles whenever `H=o(m)`.

#### Proof

A self-complementary cycle containing `X` also contains `X^c`. Their
Johnson distance is `m`, so either arc of the cycle between them has at
least `m` edges. `\square`

They can therefore be retained or paid as an exceptional cycle family
without affecting the target component scale.

## 5. Exact raw endpoint census and average degree

Put

\[
                         c_m=\binom m{\lfloor m/2\rfloor}.       \tag{5.1}
\]

The product-SCD cover has `P_0=c_m^2` paths. Let `\mathcal E` be its set of
distinct endpoint owners. When `m` is odd every path is nontrivial. When
`m` is even, the number of singleton paths is

\[
 S_0=c_m^2-
 \binom m{m/2-1}^{\!2}=O(c_m^2/m).                 \tag{5.2}
\]

Therefore

\[
                         |\mathcal E|=2c_m^2-S_0
 =(2+o(1))c_m^2
 =\left({4\over\sqrt\pi}+o(1)\right){W\over\sqrt m}.           \tag{5.3}
\]

The middle Johnson graph is `m^2`-regular and has least eigenvalue `-m`.
For every vertex set `S`,

\[
 2e_J(S)\ge {m(m+1)|S|^2\over W}-m|S|.             \tag{5.4}
\]

Applying (5.4) to `\mathcal E` gives

\[
 {2e_J(\mathcal E)\over|\mathcal E|}
 \ge {m(m+1)|\mathcal E|\over W}-m
 =\left({4\over\sqrt\pi}+o(1)\right)m^{3/2}.       \tag{5.5}
\]

Equation (5.5) counts adjacent endpoint owners. One neighbouring product
path contributes at most two endpoints, so the guaranteed average number
of distinct adjacent paths is at least

\[
 \left({2\over\sqrt\pi}+o(1)\right)m^{3/2},
\]

after the `O(1)` same-path exclusion.  The order \(m^{3/2}\) survives,
but the constant \(4/\sqrt\pi\) belongs to endpoint-owner incidences.
Moreover (5.5) includes same-half seams; the corresponding cross-half
endpoint statistic has an SCD-independent \(\Omega(m^{3/2})\) average,
not a minimum or history-conditioned bound.

It is an average. It gives neither a minimum degree nor expansion after
history restrictions.

## 6. Exact random-active-set survival

Let `F\subseteq[m]` have size `f`, and let `U` be a uniform `h`-subset,
independent of `F`. Then

\[
 \Pr(U\cap F=\varnothing)
 ={\binom{m-f}h\over\binom mh}
 =\prod_{j=0}^{h-1}\left(1-{f\over m-j}\right).     \tag{6.1}
\]

When `f+h=o(m)`,

\[
 \log\Pr(U\cap F=\varnothing)
 =-{fh\over m}
  +O\!\left({fh(f+h)\over m^2}\right).             \tag{6.2}
\]

In particular, if

\[
 H=\sqrt m\,\omega,qquad f\le H,qquad h\le K\sqrt m,          \tag{6.3}
\]

for fixed `K`, the probability is `\exp[-O_K(\omega)]`. With
`\omega=\log\log m`, this is `(\log m)^{-O_K(1)}`.

The same calculation remains polynomially large for the slowly growing
cutoff

\[
                         h_0=\sqrt{3m\log m},        \tag{6.4}
\]

provided `\omega=o(\sqrt{\log m})`:

\[
 \Pr(U\cap F=\varnothing)
 \ge\exp[-O(\omega\sqrt{\log m})]=m^{-o(1)}.        \tag{6.5}
\]

For two independent half-active sets and two forbidden queues, the two
factors multiply and only double the exponent.

### Proposition 6.1 (average short-path mixing calculation)

All but `m^{-3+o(1)}` of the product-SCD paths have length at most `h_0`.
The total number of raw endpoint adjacencies incident with longer paths is
`o(|\mathcal E|m^{3/2})`. If the two forbidden queues are chosen uniformly
and independently of the candidate active sets, the number of surviving
short-path endpoint incidences is at least

\[
                         |\mathcal E|m^{3/2-o(1)}.   \tag{6.6}
\]

Equivalently, the average surviving degree is at least `m^{3/2-o(1)}`.

#### Proof

The exact long-path census is

\[
 P_{\ge h_0}
 =\binom m{\lfloor(m-h_0)/2\rfloor}^{\!2}
 \le e^{-h_0^2/m+o(\log m)}c_m^2
 =m^{-3+o(1)}c_m^2.                                \tag{6.7}
\]

Even charging all `m^2` Johnson neighbours to every long endpoint gives
`O(m^{-1+o(1)}c_m^2)`, negligible beside the
`\Omega(c_m^2m^{3/2})` directed adjacency lower bound from (5.5).

For every remaining arc, each candidate active set has size at most
`h_0`. Average (6.1) over independent uniform forbidden queues and use
(6.5), once for each half. Summing over the raw short arcs proves (6.6).
`\square`

This is an exact averaged theorem. It does not apply to the queue produced
by an earlier SCD route: that queue is correlated with the candidate
endpoint and active sets.

## 7. Why the proposed degree theorem is still missing

The quantitative proposal would require a statement of the following
form. For every reachable two-sided automaton state `\sigma`, based at all
but a negligible family of endpoint paths,

\[
 \#\{Q:\text{a Johnson seam to }Q\text{ exists and }Q
       \text{ is accepted sequentially from }\sigma\}
 \ge m^{3/2-o(1)}.                                  \tag{7.1}
\]

For a Hall or nibble proof one needs more: the candidates in (7.1) must
expand every relevant family of states and have controlled state-route
codegrees.

Neither (5.5) nor Proposition 6.1 proves (7.1).

* Equation (5.5) is only an average raw degree. A dense endpoint core can
  coexist with many low-degree endpoints.
* Equation (6.1) assumes a uniform forbidden set independent of the active
  set. A reachable queue is selected from previous SCD paths and may be
  adversarially correlated with the next active-set catalogue.
* A common coordinate relabelling makes marginals symmetric but preserves
  every active-set intersection and every endpoint adjacency, so it cannot
  repair this gap.
* Pairwise codegree or static-edge estimates do not control the sequential
  state update exposed in Section 1.

Thus the claimed polynomial dynamic degree, although quantitatively
plausible for `\omega=\log\log m`, is not a theorem of the current
product-SCD or diverse-compiler inputs.

## 8. Exact stateful path-cover target

Assume in this section that a complement-closed owner partition into
nonexceptional initial paths has first been supplied, and let `\mathcal O`
be its set of `\dagger`-orbits. Proposition 4.1 makes every orbit have size
two. If this partition has the product-SCD path count, then

\[
 |\mathcal O|=(1+o(1)){c_m^2\over2}.     \tag{8.1}
\]

This complement-closed partition is an additional interface. An arbitrary
choice of SCDs is not automatically closed under pure complementation: the
complements of its chains form another SCD which may cut the same owner set
differently. Superposing the two covers would duplicate owners. Thus
(8.1), and the route-hypergraph reduction below, are conditional on an
owner-disjoint complement-equivariant path partition (or on replacing the
product-SCD atoms by an already complement-equivariant compiler).

Put

\[
                         \ell=\lceil\omega^2\rceil.             \tag{8.2}
\]

Define an `\ell`-route hyperedge to be an `\ell`-set of path orbits which
can be ordered into one two-sided automaton-valid route, while its forced
mirror order gives the complementary route. A matching of these route
hyperedges covering all but `o(|\mathcal O|/\omega)` orbits produces a
complement-equivariant path cover with

\[
 O(|\mathcal O|/\ell)+o(|\mathcal O|/\omega)
 =o(W/H)                                             \tag{8.3}
\]

physical components.

#### Proof

Each selected hyperedge gives two physical route components and consumes
`\ell` complement orbits. The uncovered orbits contribute two singleton
route components each. Since

\[
 c_m^2=\left({2\over\sqrt\pi}+o(1)\right){W\over\sqrt m},
 \qquad H=\sqrt m\,\omega,                          \tag{8.4}
\]

the selected components contribute `O(W/(\sqrt m\omega^2))` and the
uncovered ones contribute `o(W/(\sqrt m\omega))`. `\square`

This reduction is exact. The missing theorem is:

> **Stateful endpoint route-matching lemma.** The `\ell`-route hypergraph
> has a matching covering all but `o(|\mathcal O|/\omega)` vertices,
> with every route satisfying any prescribed constant-loss lower port
> condition.

A proof would need the uniform state-degree and route-codegree estimates
missing in Section 7. The average calculation (6.6) is not enough for a
greedy or Hall proof.

## 9. Missing-shadow scope

State validity proves that every crossing window has the intended rank and
that all old path-interior witnesses remain literal. It does not prove that
new crossing targets are globally unused, nor that removing a prescribed
endpoint collar leaves no target uncovered. Therefore:

* concatenating open paths has zero **increase** in missing targets if all
  old interiors are retained;
* exact replacement of a prescribed boundary tower still requires the
  prefix-set identity or a separate target reassignment;
* complement-equivariance transfers any proved lower missing-shadow
  statement to the upper side via Theorem 3.1; but
* residence safety and dynamic endpoint degree alone do not prove the
  constant-one target atlas.

This corrects the zero-loss wording of the one-sided static-forest note and
sets the precise proved/conditional boundary.
