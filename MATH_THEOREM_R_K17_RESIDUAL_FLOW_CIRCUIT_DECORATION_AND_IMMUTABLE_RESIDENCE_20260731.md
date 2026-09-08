# Residual-flow circuits give exact upper-turn transport but cannot repair the fixed `K17` macro residence

Date: 2026-07-31  
Status: exact general switch theorem plus an independently replayed finite
`C6` census on the authenticated carrier; no `K17` word or new upper bound
is claimed

## 0. Verdict

Rebase on the literal carrier

```text
scratch/k17_parent_induced_macro_port_cycle_20260731.cycle
SHA-256 39cc3abe6a8991dc101a585123989deab863030060c00d3e0a2a60cd73252de6
```

from
`MATH_THEOREM_K17_PARENT_INDUCED_MACRO_PORT_HAMILTON_CYCLE_20260731.md`.
Middle ownership, connectivity and the complete lower-`q1` palette are now
finished.  They are not gates in this note.

There is an exact circuit calculus for changing the selected pure-`U`
incidences while retaining those three properties.  A circuit is legal
precisely when a finite boundary-pairing graph is one cycle.  At every
touched port it transports one rank-ten upper-turn occurrence, so its full
upper effect is an ordinary signed divergence vector.  This gives a finite
augmenting-path formulation for upper-`q1` repair.

On the frozen flow, the smallest circuits are Boolean incidence hexagons.
The complete exact census is:

\[
\begin{array}{c|r}
\text{applicable alternating }C_6&7225\\
\text{Hamilton-safe}&3625\\
\text{Hamilton-safe and upper-provider-safe}&1711\\
\text{strictly reduce the upper-}q1\text{ hole count}&1121\\
\text{fill three holes and lose none}&15.
\end{array}                                             \tag{0.1}
\]

Thus the upper-turn layer has genuine monotone local mobility.  It is not a
dead flow fibre.

Residence is different.  The independently audited fixed-macro theorem
finds `605` length-three positive runs whose entire collars lie inside one
of the `1430` residual macros.  Every residual-flow circuit changes only
ports.  Hence **no sequence of these circuits, of any support, can make the
frozen macro family depth-three resident**.  The strengthened occurrence
audit goes further: for this fixed parent, every rank-six occurrence
transversal has at least `165` forced internal length-three runs, and the
certified exact coupled minimum is `180`.  A successful construction must
therefore change the parent chronology or use a genuinely nonflat compiler.

## 1. The fixed incidence Hamilton cycle

Let

\[
 \mathcal T=\binom{[15]}8,
 \qquad \mathcal U=\binom{[15]}9,
 \qquad |\mathcal T|=6435,
 \qquad |\mathcal U|=5005.                            \tag{1.1}
\]

Let \(\mathcal P\) be the `1430` fixed residual `A/X/Y` macros.  Contract
each pure owner and each macro to one block, but retain a vertex for every
rank-eight port colour.  The authenticated carrier is then a bipartite
Hamilton cycle

\[
 H\subseteq
  (\mathcal U\mathbin{\dot\cup}\mathcal P)\ \square\ \mathcal T .
                                                               \tag{1.2}
\]

Every macro has its two forced port incidences.  Every \(U\in\mathcal U\)
has two selected facet incidences \(UT\), \(T\subset U\).  Every block and
every colour vertex has degree two in \(H\).  Suppressing the colour
vertices and expanding the macros gives the literal `24310`-owner cycle.

Write \(x\) for the selected \(\mathcal U\)-to-\(\mathcal T\) incidences.
All other data in this note, including every macro interior, are fixed.

## 2. Exact alternating-circuit theorem

### Definition 2.1 (conformal circuit)

A conformal alternating circuit of half-length \(t\) is a simple cycle in
the rank-nine/rank-eight containment graph, indexed as

\[
 U_0,T_0,U_1,T_1,\ldots,U_{t-1},T_{t-1},U_0,          \tag{2.1}
\]

such that

\[
 E^- =\{U_iT_i:0\le i<t\}\subseteq x,
 \qquad
 E^+ =\{U_{i+1}T_i:0\le i<t\}\cap x=\varnothing,    \tag{2.2}
\]

with indices modulo \(t\).  Its toggle is

\[
                         x'=x-E^-+E^+.               \tag{2.3}
\]

### Theorem 2.2 (degree, palette and topology)

For every conformal circuit:

1. (x') has the same degree at every (U)- and (T)-vertex as (x).
   Consequently it preserves every owner and every rank-eight lower colour
   exactly once.
2. Cut the Hamilton cycle (H) at the (t) old incidences (E^-).  Let
   (P_K) be the perfect pairing of the resulting (2t) boundary
   occurrences induced by the retained path fragments, and let (M_K) be
   the perfect matching induced by the new incidences (E^+).  Then

   \[
        H'=(H-E^-)+E^+\text{ is Hamiltonian}
        \quad\Longleftrightarrow\quad
        P_K\cup M_K\text{ is one }2t\text{-cycle}.   \tag{2.4}
   \]

3. If (x_0,x_1) are any two integral flows with the same degree rows,
   (x_0\triangle x_1) decomposes into conformal alternating circuits.
   Thus these circuits generate the whole fixed-macro degree fibre.  The
   decomposition alone does not guarantee that its prefixes satisfy (2.4).

#### Proof

At every vertex of (2.1), one selected incidence is removed and one is
added.  This proves the degree assertion.  A colour vertex remains degree
two and still occurs once, so suppression gives the same complete lower
palette.

The removed incidences are a matching in the bipartite Hamilton cycle.
Deleting them therefore leaves (t) path fragments.  Contract each
fragment to its boundary pair.  Reattaching (E^+) gives exactly the
two-matching graph (P_K\cup M_K); its cycles are in bijection with the
components of (H').  This proves (2.4).

Finally every vertex has equal degree in (x_0\setminus x_1) and
(x_1\setminus x_0).  Their red/blue symmetric difference is Eulerian and
decomposes into alternating even circuits.  Toggling one circuit preserves
all degree rows, so the decomposition can be applied sequentially.  The
Hamilton row is not a degree row, which is why (2.4) must still be checked.
\(\square\)

Theorem 2.2 is the exact replacement for an arbitrary `b`-flow argument.
Ordinary flow proves degrees.  The six-/eight-/longer-port pairing proves
the one-cycle row.

## 3. Exact upper-turn transport

Fix a conformal circuit.  At colour (T_i), let (B_i) be the unchanged
block on the other side of (T_i), and let (W_i) be its literal rank-nine
endpoint owner.  Before the switch the physical adjacency at (T_i) is

\[
                         U_i\ --\ W_i,               \tag{3.1}
\]

and afterwards it is

\[
                         U_{i+1}\ --\ W_i.           \tag{3.2}
\]

Both owners contain (T_i).  Therefore the unique changed upper-`q1`
occurrence at this port is

\[
 Q_i=U_i\cup W_i
       \quad\longrightarrow\quad
 Q'_i=U_{i+1}\cup W_i.                              \tag{3.3}
\]

The three additions outside (T_i) are distinct, so (Q_i,Q'_i) are
rank-ten sets differing by one Johnson exchange.  No internal macro turn
changes.

Let \(\mu(Q)\) be the current rank-ten occurrence load, and define

\[
 o_K(Q)=|\{i:Q_i=Q\}|,
 \qquad
 a_K(Q)=|\{i:Q'_i=Q\}|.                              \tag{3.4}
\]

### Corollary 3.1 (provider-safe augmenting circuit)

The exact post-switch load is

\[
                    \mu'(Q)=\mu(Q)-o_K(Q)+a_K(Q).    \tag{3.5}
\]

Hence a Hamilton-safe circuit loses no covered upper-`q1` target iff

\[
       o_K(Q)-a_K(Q)\le \mu(Q)-1
       \qquad\text{for every currently covered }Q.  \tag{3.6}
\]

It strictly improves coverage iff (3.6) holds and (a_K(Q)>0) for at least
one current hole (Q).  These conditions are necessary and sufficient for
one circuit; no independence assumption is used.

### Corollary 3.1A (tag-sector invariance)

Every residual-flow turn transport preserves the subset of the two new
coordinates carried by its rank-ten colour.  Indeed the old and new pure
owners in (3.3) carry neither tag, while the unchanged endpoint (W_i)
carries both, one or neither in both unions.  The four tag sectors therefore
decouple at upper `q1`.  Their current missing counts for
`none/Y/X/XY` are

\[
                         618,\quad623,\quad650,\quad0.
\]

In particular no flow switch is needed for the `XY` sector, and none can
move surplus between the other three sectors.

Orient every selected residual incidence (T\to U), and every unselected
legal incidence (U\to T), obtaining the residual digraph (D_H).

### Theorem 3.2 (provider return-path criterion)

Fix an **ordered provider corner**

\[
                 U^+\xrightarrow{e}T\xrightarrow{f}U^- ,
\]

where (e) is unselected, (f) is selected, and replacing the incidence
(TU^-) by (TU^+) creates a desired missing upper turn against the
unchanged other endpoint at (T).  Simple conformal circuits containing
this ordered corner are in bijection with simple directed paths

\[
                         T\leadsto U^+
             \quad\text{in }D_H-e                   \tag{3.7}
\]

whose first arc is (f), by adjoining (e).  Such a path is a valid
provider augment exactly when:

1. its fragment pairing satisfies (2.4); and
2. its bundled turn divergence satisfies (3.6).

It fills precisely the initially missing labels entered by the resulting
turn arcs.

#### Proof

Deleting (e) from a simple directed circuit leaves the path (3.7); its
first arc records exactly which selected incidence at (T) is evicted.
Adjoining (e) closes the circuit.  Theorem 2.2 supplies the
degree, palette and monodromy rows; Corollary 3.1 supplies the exact
provider row. \(\square\)

The selected first arc is essential when (T) currently has two pure
incidences: the unused arc (e) alone does not determine the unchanged
physical endpoint and therefore does not determine the new upper turn.

Thus ordinary reachability is only a relaxation.  A correct path search
must carry both the boundary pairing (monodromy) and the capped signed load
on every touched upper label.

### Theorem 3.3 (finite ordered augmenting-path formulation)

Let \(\mathfrak X\) have as vertices the Hamiltonian integral flows in the
fixed macro degree fibre.  Join (x) to (x\triangle K) when (K) is a
conformal circuit passing (2.4), and label the arc by the signed vector

\[
                         \Delta_K=a_K-o_K.            \tag{3.8}
\]

Starting from load vector \(\mu_0\), a sequence of fixed-macro switches
preserves upper-`q1` coverage at every prefix and finishes with all
rank-ten targets covered if and only if it is a path

\[
 x_0\to x_1\to\cdots\to x_s                         \tag{3.9}
\]

in \(\mathfrak X\) such that

\[
 \mu_0(Q)+\sum_{j< h}\Delta_{K_j}(Q)\ge1
       \quad(Q\text{ initially covered},\ 1\le h\le s),           \tag{3.10}
\]

and the final vector is at least one on every rank-ten target.

Equivalently, each circuit is a bundled transport of (t) units on the
rank-ten Johnson graph.  Any successful packet decomposes into transport
paths from surplus occurrences to holes plus circulation cycles, but that
scalar transport is sufficient only when the bundled switches admit the
Hamilton-safe ordering (3.9).  Thus ordinary target flow is a relaxation,
not the missing theorem.

#### Proof

Equation (3.5) telescopes along a path.  Conditions (3.10) are exactly the
prefix provider constraints, and membership in \(\mathfrak X\) is exactly
the one-cycle condition.  Necessity and sufficiency follow directly.  The
path/cycle decomposition is the standard decomposition of a nonnegative
integer transport after pairing deficits with surpluses.  It forgets the
bundle and topology labels, so only the forward implication survives after
that projection. \(\square\)

Since the frozen carrier has `1891` missing rank-ten targets, every complete
fixed-macro repair has total changed half-support at least `1891`: a
half-length-(t) circuit can introduce at most (t) previously missing
targets.  The current surplus occurrence count is

\[
                  24310-17557=6753,                 \tag{3.11}
\]

so scalar occurrence supply is ample.  Correlated containment and topology,
not the scalar total, are the upper-turn gate.

## 4. The minimal Boolean circuits

The rank-eight/rank-nine containment graph has no `C4`.  Indeed, if two
distinct rank-nine sets contained two distinct common rank-eight facets,
the union of those facets would be a rank-nine set equal to both owners.

Every `C6` is determined by a rank-seven kernel (K) and three distinct
outside coordinates (a,b,c):

\[
\begin{array}{lll}
 T_a=K+a,&T_b=K+b,&T_c=K+c,\\
 U_{ab}=K+a+b,&U_{bc}=K+b+c,&U_{ca}=K+c+a.
\end{array}                                          \tag{4.1}
\]

Its switch cyclically replaces

\[
 U_{ab}T_a, U_{bc}T_b, U_{ca}T_c
 \quad\text{by}\quad
 U_{ab}T_b, U_{bc}T_c, U_{ca}T_a                 \tag{4.2}
\]

or the reverse rotation.

### Theorem 4.1 (complete frozen-flow `C6` census)

For the authenticated flow artifact with SHA
`5d27dc9b0c31f7418a0393e4725cb76582fef9aa20bc0840092b814820f64d89`,
the exact counts are

\[
\begin{array}{c|rrr}
\text{components after toggle}&1&2&3\\ \hline
\text{number of alternating }C_6&3625&2703&897.
\end{array}                                          \tag{4.3}
\]

On the `3625` Hamilton-safe switches, the complete
`(new holes filled, covered targets lost)` profile is

\[
\begin{array}{c|rrrr}
 &0&1&2&3\ \hline
0&793&696&190&18\\
1&711&548&173&18\\
2&192&176&60&7\\
3&15&20&7&1
\end{array}.                                         \tag{4.4}
\]

Rows index filled and columns index lost.  In particular `1711` switches
are provider-safe, and `1121` strictly reduce the hole count.

One maximal calibration switch has kernel `5167`, outside-coordinate
indices `(4,8,14)` (zero based), and replaces the incidences

```text
(5439,  5183) -> (5439,  5423)
(21807, 5423) -> (21807, 21551)
(21567,21551) -> (21567, 5183)
```

where each pair is `(rank9 owner, rank8 colour)`.  It removes upper
occurrences `21871,22079,70975` and adds the three previously missing
targets `5503,22319,87103`; none of the removed targets becomes uncovered.
The port-pairing test is one cycle.  Thus it gives a literal

\[
                         1891\longrightarrow1888    \tag{4.5}
\]

upper-`q1` improvement while retaining the Hamilton carrier and every
lower-`q1` colour.

The complete fifteen maximal switches are in the audit JSON.  The census is
a direct enumeration of (4.1), not SAT and not a heuristic neighbourhood.

### Corollary 4.2 (exact maximum-hex option cube)

The fifteen fill-three/lose-zero hexagons use `45` distinct pure owners and
`45` distinct rank-eight colours.  Their removed upper labels are all
distinct; their additions have `44` distinct labels (only `22319` is
repeated), and no added label is removed.  Thus their degree and upper-load
effects commute.  Topology does not.

Toggling all fifteen fills `44` holes and loses none, but the port factor
splits into four cycles.  Cutting all `45` old incidences once reduces the
complete `2^15` option cube to two matchings on `90` boundary occurrences.
Its exact component profile is

\[
\begin{array}{c|rrrrrrr}
\text{components}&1&2&3&4&5&6&7\\ \hline
\text{states}&10270&12686&7596&1918&262&32&4.
\end{array}                                           \tag{4.6}
\]

Of the `10270` Hamilton states, `10128` are reachable from the original
state by an ordering whose every prefix is Hamiltonian.  The best such state
uses thirteen hexagons, indexed

```text
0,1,2,4,5,6,7,8,9,11,12,13,14
```

and fills `39` distinct upper holes without losing any.  One Hamilton-safe
application order is

```text
14,13,12,9,11,8,7,6,5,4,2,1,0.
```

Consequently the authenticated fixed-macro fibre has an explicit monotone
lower-rainbow Hamilton route

\[
                         1891\longrightarrow1852     \tag{4.7}
\]

at upper `q1`.  The failure of the all-fifteen packet is a literal
monodromy obstruction, while the thirteen-switch route proves that it is
not an obstruction to every large correlated packet.

## 5. Residence monoid and the immutable obstruction

For an oriented atomic object (B=(V_0,\ldots,V_s)) and coordinate (j),
record the binary word

\[
              (1_{j\in V_0},\ldots,1_{j\in V_s}).   \tag{5.1}
\]

For the depth-three residence test it suffices to retain its first and last
bits, leading and trailing positive-run lengths truncated at four, whether
the word is all one, and the number of internal positive runs of lengths
one, two and three.  Concatenating two oriented objects updates this record
deterministically by merging their boundary runs.  This is an associative
finite monoid, so it gives the exact run signature of every object order and
orientation.

A positive run whose entering edge, internal edges and leaving edge all lie
inside one atomic object is an invariant of every port reconnection.  Macro
reversal reverses the same `0 1^ell 0` word and does not change its length.

The authoritative literal audit
`MATH_THEOREM_K17_FIXED_MACRO_RESIDENCE_OBSTRUCTION_20260731.md` proves that
the frozen macros contain exactly

\[
                    605\text{ such runs of length }3.              \tag{5.2}
\]

### Corollary 5.1 (sharp fixed-macro no-go)

No path in the full exchange graph \(\mathfrak X\), even using circuits of
unbounded support, can satisfy depth-three residence while the `1430`
macro interiors remain fixed.

This is stronger than a local-neighbourhood floor and weaker than a `K17`
no-go.  It excludes only:

* changing the integral `U`-to-port flow;
* permuting the fixed atomic objects; and
* reversing fixed macros.

It does not exclude changing which repeated rank-six occurrences are
retained together with other architectural changes, changing the parent
chronology, rethreading inside macros outside the occurrence-transversal
construction, or using a nonflat compiler.

### Theorem 5.2 (all occurrence transversals of the fixed parent fail)

Let (C_i=T_i\cap T_{i+1}) be either authenticated parent trace cycle.
An internal `A`-shore run `0 1 1 1 0` at coordinate (j) survives exactly
when its four supporting physical rank-six-colour edges are retained.  The
parent has `1425` such patterns, `95` per old coordinate.  In exactly `165`
patterns all four supporting rank-six colours have unique occurrences.
Those four edges are forced in every occurrence transversal.  The `165`
forced patterns split as exactly eleven per coordinate.

Consequently **no choice of one occurrence of each rank-six colour**, even
followed by an arbitrary integral port flow, macro order and macro reversal,
can make this fixed parent into a flat depth-three-resident child.

#### Proof

Choosing one occurrence per rank-six colour is a one-hot system.  Avoiding
one displayed run contributes the negative clause saying that at least one
of its four support edges is not retained.  If all four support colours are
unique, every corresponding choice variable is forced true, so this clause
is empty.  One empty clause already proves infeasibility; the literal audit
finds `165`.  Port reconnection cannot alter an internal `A`-shore word.
\(\square\)

### Proposition 5.2A (certified exact finite optimum)

For the authenticated fixed parent, the minimum number of internal short
`A`-shore runs over all rank-six occurrence transversals is exactly `180`.
One materialized transversal attains twelve per old coordinate and replays
to `180` literal macro-internal runs.  The lower bound is the independently
checked DRAT proof that a transversal with at most `179` is impossible.

The solver-free unique-colour argument in Theorem 5.2 supplies `165` of the
floor; the remaining `15` are a genuine integral correlation tax across the
coordinate rows.  This finite sharpening changes no general quantifier in
Corollary 5.3.

### Corollary 5.3 (dimension-uniform one-unit residence tax)

Let \(T_0,\ldots,T_{s-1}\) be any cyclic Johnson component of rank-\(r\)
sets and put \(C_i=T_i\cap T_{i+1}\).  For every coordinate \(j\) whose
indicator is nonconstant on the component, a positive run of length
\(\ell\ge2\) in the \(T\)-cycle becomes a positive run of length exactly
\(\ell-1\) in the \(C\)-cycle; a singleton run disappears.  Every positive
\(C\)-run arises uniquely this way.  An all-zero or all-one coordinate stays
constant and does not pay the tax.  In a lower-`q1`-bijective parent,
singleton runs are impossible by the duplicate-intersection argument below,
so every nonconstant parent run participates.

Consequently a flat odd-diamond child compiled at depth \(d\) needs one of
the following exported parent states:

1. **margin:** parent minimum run at least \(d+2\); or
2. **compensation:** an explicit cut/facet/nonflat actuator hits at least one
   of the \(d+1\) trace edges spanning every parent run of length \(d+1\).

Ordinary parent residence \(d+1\) is not regenerative.

#### Proof

At the entering boundary of a \(j\)-run the Johnson step inserts \(j\), at
the leaving boundary it deletes \(j\), and every internal step retains it.
Thus \(C_i=T_i\cap T_{i+1}\) contains \(j\) on exactly one fewer consecutive
position.  The converse follows from the same boundary description.
An unbroken parent run of length \(d+1\) is therefore the forbidden child
word \(0\,1^d\,0\).  Breaking one of its spanning trace edges is necessary
and sufficient to keep that word from lying internally in one residual
macro. \(\square\)

For completeness, a length-one positive run is impossible in every
lower-`q1`-bijective Hamilton cycle.  If coordinate (j) occurred only in
owner (U) between two neighbours omitting (j), both adjacent
intersections would equal (U\setminus\{j\}), duplicating one lower colour.
Thus the residence defects in this fibre begin at lengths two and three.

## 6. What is proved and what remains

The fixed-macro problem now splits exactly.

1. **Upper `q1`: live.**  Flow circuits act by the exact transport law
   (3.5).  There are already `918` one-step provider-safe switches filling
   at least one hole (`711+192+15`), including fifteen three-hole switches.
   An all-hole ordered packet is not proved.
2. **Residence: closed negative for every occurrence transversal of this
   fixed parent.**  Equation (5.2) blocks the frozen transversal, while
   Theorem 5.2 supplies `165` forced blockers uniformly over all of them and
   Proposition 5.2A sharpens the fixed-parent minimum to `180`.
3. **Deeper shadows:** not controlled by the immediate turn vector.  A
   circuit cuts and reconnects whole owner fragments, so all interval
   witnesses must be replayed or carried in a protected boundary state.
4. **Compiler:** wholly downstream and not addressed here.

There is also a logically prior occurrence-coherence row.  If (x_e)
selects one physical edge in each rank-six colour fibre, then residence
packets impose negative hyperclauses on (x), while retained parent-upper
unique providers give linear rewards on the same variables.  For a fibre
with (u_Z) unique providers, its exact marginal deletion floor is

\[
                          \sum_Z(u_Z-1)^+.
\]

This is `505` for the present parent.  Its residence marginal optimum is
`180`.  The octahedral `r2` parent improves the two separate figures to
`405` and `150`.  These are marginal pairs, not certified common points:
the occurrence-labelled provider set, surviving run-packet set, and induced
macro-port signature must be exported together.  Only after this common
transversal is chosen does the residual circuit/flow calculus of Sections
2--4 begin.

Accordingly an occurrence/flow search on this parent is mathematically
retired for the flat compiler.  The smallest honest next construction is
either (i) a different lower-rainbow parent chronology whose occurrence
system has no forced internal run clauses, followed by connected flow and
upper transport, or (ii) a genuinely nonflat compiler that can consume the
forced short runs.  In an all-dimension induction, the regenerative state
must export the one-extra-unit margin or the explicit compensation set of
Corollary 5.3.  A port-only augmenting algorithm can improve upper service
but cannot finish the optimal-word route.

## 7. Reproducibility and independent audit

Primary bounded census:

```text
scratch/audit_r_k17_residual_flow_c6_decoration_20260731.py
SHA-256 efeade2d5df9e1d2c4b6f1bffafde927cbf9265dd08d6cac717bd9748eefa033

scratch/k17_residual_flow_c6_decoration_20260731.audit.json
SHA-256 ac201ac3cf2dee747a6a654a7de696135df093f02d7116174058f4094392523a
```

The script fails closed on both frozen source hashes, reconstructs the
colour/object Hamilton cycle, enumerates every Boolean incidence hexagon,
uses the six-boundary pairing test rather than a component proxy, and
computes exact occurrence multiplicities before declaring a provider safe.

An independent implementation reconstructed the selected incidences from
the literal owner cycle alone.  It reproduced `7225`, the component split
`3625/2703/897`, the full table (4.4), and the `1711` provider-safe count.
It also physically replayed representative gain-three, gain-two and
gain-one outputs.  The option cube uses the same exact path-pairing theorem
on one common `90`-boundary cut and asserts its full cardinality
`32768`.  Separately, the strengthened fixed-parent residence theorem and
audit are authoritative for (5.2) and Theorem 5.2.

The exact `180` occurrence optimum is authenticated by

```text
scratch/k17_macro_residence_optimal_20260731.json
SHA-256 8ecf43e13bfb7e0c204847f3c480dadc76af39dec979d245dc73bd5a5b5717b4

scratch/k17_macro_residence_optimal_20260731.verify.json
SHA-256 71ffd874fe520daf8609902cf2f12df181a55b1b38d3299633bb95c7e5e89a10

scratch/k17_macro_residence_bound179_20260731.cnf
SHA-256 4cbf25a3f4d322c54ce91b068dc08e49223e86019d3dfccc51f065a3860cf19c

scratch/k17_macro_residence_bound179_20260731.drat
SHA-256 8d55ea0215b62b43aaba7a94eda194555227ffdb0a73eb174d227afa0695c018
```

The independent DRAT check records a `5531`-clause core and `99145`
resolution steps.  The computational sharpening is finite-parent-specific;
the solver-free `165` unique-colour packets are the reusable obstruction.
