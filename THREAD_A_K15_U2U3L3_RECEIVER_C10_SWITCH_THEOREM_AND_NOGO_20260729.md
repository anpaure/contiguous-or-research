# `k=15`: receiver-`C10` switch theorem and the support-five no-go for `u2u3l3_s801`

Date: 2026-07-29

Status: general switch theorem proved; new factor lightly replayed; exact
solver-free obstruction proved for a single component-transversal quotient
`C10` in the frozen fixed-`M0` fibre.  This note does **not** obstruct
compound circuits, a longer odd-support circuit, a change of `M0`, or the
non-equivariant eight-seam opening route.

## 1. Audited input and its true quotient topology

The candidate

```text
scratch/k15_fixed_matching_pbbs_resident_20260729/u2u3l3_s801.engine.json
```

has SHA-256

```text
886877094a3eaba8950136728d131782141a4b6f882d570ecb3791827da98f83.
```

Its two independent retained audits certify 6,435 distinct middle states,
minimum coordinate run four, no residence defects, no lower or upper holes
at any proper depth, and the nine physical cycle lengths

```text
1890, 774, 774, 774, 774, 774, 555, 75, 45.
```

The nine physical cycles descend to only five quotient cycles.  In the
canonical unoriented quotient traversal used by the factor audit, their
data are

| quotient length | voltage mod 15 | lift multiplicity | physical length(s) |
|---:|---:|---:|---:|
| 258 | 5 | 5 | `774` five times |
| 126 | 4 | 1 | `1890` |
| 37 | 1 | 1 | `555` |
| 5 | 4 | 1 | `75` |
| 3 | 11 | 1 | `45` |

Indeed a quotient cycle of length `ell` and voltage `w` lifts to
`gcd(15,w)` cycles, each of length

\[
                 \frac{15\ell}{\gcd(15,w)}.                 \tag{1.1}
\]

The signs of the displayed voltages depend on the independently chosen
orientation of each unoriented quotient component.  In the directed
fixed-matching convention `tau=M0^{-1}P`, the five directed voltages sum to
zero modulo 15.  Only that coherent directed convention is used in the
switch formula below.

## 2. Equivariant matching normal form

Let a cyclic group `G=Z_k` act freely on both shores of a bipartite
incidence graph.  Choose quotient representatives for the lower shore and
write a physical lower vertex as `(x,t)`, where `t in G`.  Let `M0` and `P`
be equivariant perfect matchings.  Write

\[
\begin{aligned}
 M_0(x,t)&=(m_0(x),t+a(x)),\\
 P(x,t)&=(p(x),t+b(x)).
\end{aligned}                                                \tag{2.1}
\]

Put

\[
 \tau=m_0^{-1}p,
 \qquad
 \delta(x)=b(x)-a(\tau x)\pmod k.                            \tag{2.2}
\]

Thus the physical first-return map on the lower shore is

\[
             T(x,t)=(\tau x,t+\delta(x)).                    \tag{2.3}
\]

For a quotient `tau`-cycle `C`, its voltage is

\[
                        \omega(C)=\sum_{x\in C}\delta(x).    \tag{2.4}
\]

Formula (1.1), with `15` replaced by `k`, follows immediately by iterating
(2.3).

## 3. The exact receiver-cycle switch theorem

Choose distinct receiver marks `y_0,...,y_(r-1)` and put

\[
 x_i=\tau^{-1}y_i,
 \qquad
 \gamma=(y_0\ y_1\ \cdots\ y_{r-1}).                        \tag{3.1}
\]

The old matching edge at source `x_i` ends in the quotient upper vertex
`m0(y_i)`.  Suppose that, for every `i`, the quotient incidence catalogue
contains a non-`M0` edge

\[
 e_i' : x_i\longrightarrow m_0(y_{i+1}),                    \tag{3.2}
\]

where subscripts are cyclic, and let its phase be `b_i'`.  Replace the old
`P` edge at `x_i` by `e_i'` and leave all other `P` edges unchanged.

### Theorem 3.1 (receiver `C_(2r)` switch)

The preceding replacement has the following exact properties.

1. It is an equivariant perfect matching `P'`, edge-disjoint from `M0`.
   Its symmetric difference with `P` is one quotient alternating
   `C_(2r)`; its physical lift changes exactly `kr` old and `kr` new
   incidence edges.
2. Its quotient monodromy is

   \[
                              \tau'=\gamma\tau.              \tag{3.3}
   \]

3. If the `r` marks lie in `r` distinct old `tau`-cycles, the switch joins
   those `r` cycles into one and leaves every other quotient cycle
   unchanged.
4. If the joined cycle is the whole quotient, its resulting voltage is

   \[
   \begin{aligned}
    \Omega'
      &=\sum_x\delta(x)
        +\sum_i\left[(b_i'-a(y_{i+1}))
                     -(b(x_i)-a(y_i))\right]\\
      &=\sum_x\delta(x)+\sum_i(b_i'-b(x_i))\pmod k.          \tag{3.4}
   \end{aligned}
   \]

   Hence the physical factor is one cycle exactly when

   \[
                              \gcd(k,\Omega')=1.              \tag{3.5}
   \]

#### Proof

The new upper endpoints in (3.2) are a cyclic permutation of the old upper
endpoints, so degree one holds on both quotient shores.  Each selected
quotient incidence orbit lifts to `k` disjoint physical incidences; hence
the lifted matching is also perfect.  The assumed catalogue membership and
non-`M0` condition give incidence legality and edge-disjointness.  The old
and new edges alternate on the ten, or generally `2r`, quotient vertices.

Since `P'(x_i)=M0(y_(i+1))`, while `P'=P` off the selected sources,
`M0^{-1}P'=gamma tau`, proving (3.3).  Cutting the old incoming edge at one
mark in each of `r` distinct cycles and reconnecting it to the next mark
traverses the `r` old residual paths successively, so they form one cycle.

The new voltage increment at `x_i` is `b_i'-a(y_(i+1))`; subtracting its
old increment gives the first line of (3.4).  Since `(y_(i+1))` is a
permutation of `(y_i)`, all `a`-terms telescope.  Formula (3.5) is the lift
formula (1.1).  ∎

### Corollary 3.2 (necessary support and parity)

If `tau` has exactly five cycles and a receiver `5`-cycle makes it one
cycle, then its five marks lie one in each old cycle.  More generally, for
an `r`-cycle multiplier,

\[
             c(\gamma\tau)-c(\tau)\equiv r-1\pmod2.          \tag{3.6}
\]

Thus a single receiver cycle taking five quotient components to one must
have odd support.  If support five is unavailable, the next possible
single-cycle primitive is support seven, an alternating `C14`; a support-six
`C12` cannot do the job by parity.

#### Proof

A switch on five marks can lower the cycle count by at most four.  Equality
requires all five touched old components to be distinct, by the same cut and
reconnection argument as in Theorem 3.1.  Finally
`sgn(gamma)=(-1)^(r-1)` and
`sgn(pi)=(-1)^(N-c(pi))`, which gives (3.6).  ∎

## 4. Exact shadow and residence ledgers

Let `T` and `T'` be the physical lower-shore monodromies before and after a
switch, and let `S` be the physical set of changed sources.  For depth `q`,
define

\[
\begin{aligned}
 \Phi_q^-(u;T)&=\bigcap_{j=0}^{q}M_0(T^ju),\\
 \Phi_q^+(u;T)&=\bigcup_{j=0}^{q}M_0(T^ju),\\
 \mu_q^\pm(T)&=\sum_u e_{\Phi_q^\pm(u;T)}.                  \tag{4.1}
\end{aligned}

Put

\[
 A_q=\{u:T^ju\in S\text{ or }T'^ju\in S
              \text{ for some }0\le j<q\}.                 \tag{4.2}
\]

Then the all-depth ledger is the identity

\[
 \boxed{
 \mu_q^\pm(T')-\mu_q^\pm(T)
 =\sum_{u\in A_q}
   \left(e_{\Phi_q^\pm(u;T')}-e_{\Phi_q^\pm(u;T)}\right).} \tag{4.3}
\]

Indeed a start outside `A_q` follows the same first `q` transitions under
both permutations.  Since both are permutations,

\[
 |A_q|\le 2q|S|,
 \qquad
 \|\mu_q^\pm(T')-\mu_q^\pm(T)\|_1\le4q|S|.                \tag{4.4}
\]

For a quotient `C10` at `k=15`, `|S|=75`, so the bounds are `150q` affected
starts and `300q` histogram `L1` change.  They are damage ceilings, not
support-preservation theorems.  Exact preservation is equivalent to

\[
             \mu_q^\pm(T)(Z)+\Delta_q^\pm(Z)\ge1            \tag{4.5}
\]

for every intended target `Z`, with `Delta` computed by (4.3).

One deck is automatic.  Both `M0(x)` and `P'(x)` are distinct rank-eight
supersets of the physical rank-seven source `x`, so

\[
                       M_0(x)\cap P'(x)=x.                   \tag{4.6}

Thus the complete squarefree lower-`q1` deck survives every legal
fixed-`M0` receiver switch.  The upper-`q1` and lower-`q2` quotient load
vectors instead obey the exact local formula

\[
 \mu_c' = \mu_c-sum_i e_{c(e_i)}+\sum_i e_{c(e_i')},        \tag{4.7}
\]

and are complete exactly when every coordinate of the right-hand side is
positive.

Residence is also exact and local, but it is not enough to inspect five
abstract seams.  In the fixed-`M0` chart, middle residence at least four is
equivalent on every physical consecutive lower arc sequence to

\[
 \operatorname{ins}(e_i)\ne\operatorname{del}(e_{i+1}),
 \qquad
 \operatorname{ins}(e_i)\ne\operatorname{del}(e_{i+2}).    \tag{4.8}
\]

Equivariant expansion gives the audited all-negative width-two/three clause
ideal.  Since the present factor satisfies it, a receiver switch is resident
if and only if the updated selected-variable set contains none of those
clauses.  This remains exact when two lifted seams are close; an
independent-collar approximation would not.

## 5. The exact support-five obstruction for `u2u3l3_s801`

Define the receiver exchange digraph `G` as follows.  Its vertices are the
429 quotient lower receivers.  For a receiver `y`, let `x=tau^{-1}y`.
There is an arc `y -> z` precisely when the frozen catalogue contains the
legal replacement edge

\[
                         x\longrightarrow M_0(z).            \tag{5.1}
\]

A receiver `C10` is exactly a directed `5`-cycle in `G`.  The reconstruction
from the frozen mapping has 2,570 alternative arcs, 1,437 between distinct
`tau`-components.  Label the components by their quotient lengths

```text
A=258, B=126, C=37, D=5, E=3.
```

The complete component-pair arc counts are

| from/to | A | B | C | D | E |
|---|---:|---:|---:|---:|---:|
| A | 910 | 463 | 145 | 21 | 7 |
| B | 478 | 206 | 60 | 5 | 6 |
| C | 127 | 75 | 16 | 3 | 1 |
| D | 19 | 8 | 1 | 0 | 2 |
| E | 12 | 3 | 0 | 1 | 1 |

Thus the component-level projection looks almost complete.  Nevertheless
the physical receiver states do not compose.

### Theorem 5.1 (no component-transversal quotient `C10`)

The receiver exchange digraph of `u2u3l3_s801` contains no directed
`5`-cycle meeting all five quotient monodromy components.  Consequently no
single support-five alternating matching exchange can turn the nine-cycle
physical factor into one physical cycle, even before imposing voltage,
upper-`q1`, lower-`q2`, residence, deeper shadows, or compiler constraints.

#### Exact finite certificate

The three receivers in `E` are

\[
                              152,315,318.                    \tag{5.2}
\]

Starting at each one, recursively follow an exchange arc only when its
destination belongs to a previously unvisited component.  After all five
components have been visited, the possible terminal receivers are

\[
\begin{array}{c|l}
152&188,366\\
315&1,6,7,25,28,83,92,95,145,163,201,202,205,418\\
318&117,188.
\end{array}                                                  \tag{5.3}
\]

The respective receiver sets having an arc back to the chosen start are

\[
\begin{array}{c|l}
152&117,152,194,264,319,335\\
315&117,188,257,267,319\\
318&114,147,171,231,331,355.
\end{array}                                                  \tag{5.4}
\]

Each row of (5.3) is disjoint from the corresponding row of (5.4).  The
numbers of full component-transversal directed paths before the failed
closure test are respectively `3,17,2`.

Every desired directed `5`-cycle contains exactly one `E` receiver by
Corollary 3.2, and has a unique cyclic rotation beginning there.  The first
four arcs are therefore one of the 22 paths certified in (5.3), while its
last arc would put its terminal in (5.4), which is impossible.  This proves
the theorem.  ∎

The statewise rarity already gives useful hand pruning.  The only `E -> D`
arc is

```text
receiver 315 -> receiver 191, variable 1068, voltage correction 1;
```

the only `D -> C` arc is

```text
receiver 216 -> receiver 218, variable 2564, voltage correction 0;
```

and the only `C -> E` arc is

```text
receiver 188 -> receiver 315, variable 2277, voltage correction 14.
```

In particular projected component arrows cannot be concatenated without
checking that the arrival receiver is also the departure mark.

The solver-free reproduction scripts are

```text
scratch/thread_audit_k15_u2u3l3_c10_structure_20260729.py
scratch/thread_a_k15_u2u3l3_c10_sparse_prefilter_20260729.py
```

They rebuild the graph from

```text
scratch/k15_fixed_matching_pbbs_resident_20260729/seed0.mapping.json
```

whose SHA-256 is

```text
2350beb3c4bed89fb56a5a698e124f094ef59da375932511b667dc7483a46bb9.
```

The search is a depth-five traversal from three starts, not a SAT solve or a
large enumeration.  It was independently replicated.  Its scope is exactly
one connected receiver `C10` in this frozen non-loop fixed-`M0` catalogue.

### Theorem 5.2 (the next primitive is a four-orbit near-merger, not an exact merger)

The corresponding sparse support-seven audit gives the following exact
census after identifying cyclic rotations:

```text
simple receiver C14s meeting all five old components       76
unit-voltage among those                                    46
making tau'=gamma tau one quotient cycle                    42
making one quotient cycle and having unit voltage           24
preserving upper q1                                           2
preserving lower q2                                           3
preserving both immediate decks                               0
resident among the 24 physical one-cycle switches             0
```

The counts `80` and `48` obtained when separately anchoring at all three
vertices of the shortest component are the corresponding pre-deduplication
path and unit-voltage counts.  Four cycles contain two possible shortest-
component anchors; rotating the directed mark/edge lists together gives the
76/46 canonical counts above.

Therefore no bare support-seven receiver cycle is an exact resident
double-shadow merger.  Since support eight is parity-forbidden by (3.6), an
exact single receiver-cycle merger preserving both immediate decks must
have support at least nine.  This is a statement about one circuit; a
compensated `C14` or a compound family is not excluded.

There is, in fact, a sharp constructive near-merger.  The receiver marks

```text
13, 19, 25, 117, 315, 52, 66
```

with source rows

```text
50, 68, 43, 216, 152, 142, 51
```

and new fixed-map variables

```text
353, 479, 306, 1517, 1065, 998, 358
```

have resulting voltage one and make a single physical cycle of length
6,435.  Exact literal replay gives only the following shadow losses:

| depth/sign | missing quotient representative | physical missing |
|---|---:|---:|
| upper `q1` | 7399 | 5 |
| lower `q2` | 1139 | 15 |
| upper `q3` | 7663 | 15 |
| upper `q4` | 15855 | 5 |

Every other lower or upper target at every proper depth survives.  The new
Hamilton cycle has minimum run three and exactly 30 physical residence bad
runs/shortfall units, represented by two violated quotient residence
clauses.  Thus the smallest concrete equivariant fusion target is now

\[
 \boxed{\text{this }C14\; +\;\text{a compensator for four shadow orbits
 and two residence clauses}.}                               \tag{5.5}
\]

These statements are reproduced by

```text
scratch/thread_a_k15_u2u3l3_c14_sparse_prefilter_20260729.py.
```

The exhaustive scope is one simple support-seven receiver cycle in the
frozen fixed-`M0` non-loop catalogue.  No all-circuit or changing-`M0`
no-go is claimed.

## 6. Why this does not replace the physical eight-seam route

Opening the nine physical cycles removes one old transition from each and
uses eight new physical seams.  It is non-equivariant, has two useful global
boundaries, and changes only a constant-size physical collar.  Its pinched
rank-seven row requires at least seven useful Johnson seams, but its raw
collar is genuinely an eight-seam object.

A quotient receiver `C10` is topologically more ambitious but physically
much larger.  Its five quotient sources expand to 75 physical sources and
therefore to 75 old and 75 new transitions.  It has no boundary cells.  Its
advantage is the automatic exact lower-`q1` identity (4.6); its cost is the
all-depth collar (4.3), whose naive support is an order of magnitude larger
than the eight-splice collar.  It must therefore be exactly shadow-neutral
or exploit substantial witness multiplicity.  Scalar compiler slack does
not imply either property.

For the present factor the issue is sharper: the support-five quotient
connector fails before those collar tests.  A bare support-seven connector
can close topology with unit voltage, but Theorem 5.2 shows that it needs a
secondary shadow/residence compensator.  The valid next connector families
are therefore:

1. two dynamically legal receiver triangles (`C6+C6`) forming a loose tree
   on the five quotient components;
2. the explicit near-merging support-seven receiver cycle (`C14`) in
   Theorem 5.2 plus a bounded compensating circuit;
3. a compound/disconnected matching circuit whose total multiplier is even;
4. a switch which changes `M0`; or
5. the already isolated non-equivariant eight-seam path construction.

Every equivariant candidate in items 1--3 must still pass (3.4), (4.5),
(4.7), and (4.8).  No connectivity claim follows from component-level arc
counts alone.
