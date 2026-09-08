# Residual port circuits: exact Hamilton monodromy and upper-turn transport

Date: 2026-07-31  
Status: exact switch calculus and scoped finite reduction for the authenticated
`K17` lower-rainbow Hamilton carrier; no all-upper or residence completion is
claimed

## 0. Scope and conclusion

Fix the literal carrier

```text
scratch/k17_parent_induced_macro_port_cycle_20260731.cycle
SHA-256 39cc3abe6a8991dc101a585123989deab863030060c00d3e0a2a60cd73252de6
```

and keep all `1430` residual `A/X/Y` macros internally fixed.  The only
variables considered here are the selected containments between the `5005`
pure old rank-nine objects and the old rank-eight port colours.  Every switch
in this fibre preserves all owners and every rank-eight lower colour.

There are three exact, logically separate tests on such a switch.

1. Its incidence symmetric difference must be an alternating circulation.
2. Its reconnection transition system must have one component, not merely
   degree two.
3. Its directed rank-ten turn transport must not consume the last occurrence
   of an old colour, and must enter the desired missing colours.

Tests 1--3 give a smallest exact directed-path formulation for one residual
circuit.  They also expose two sharp limitations:

* the `1891` missing rank-ten colours force total switched half-support at
  least `1891`; bounded repair cannot finish the upper palette;
* `605` length-three positive runs lie strictly inside the frozen macros, so
  no residual port circulation, of any support, can finish depth-three
  residence; more strongly, `165` forced internal runs survive every
  rank-six occurrence transversal of this fixed parent.

Thus the present fibre has genuine upper-q1 mobility, including exact
maximum-efficiency incidence hexagons, but cannot by itself finish the
`K17` chronology.

## 1. The full port cycle and the residual exchange digraph

Let

\[
 {\cal T}=\binom{[15]}8,\qquad {\cal U}=\binom{[15]}9.
\]

Contract each fixed residual macro to one block and retain every pure
`U` owner as a singleton block.  Subdivide each adjacency by its old
rank-eight colour.  The authenticated carrier becomes a bipartite Hamilton
cycle

\[
 {\cal H}\subseteq ({\cal B},{\cal T};E),                 \tag{1.1}
\]

where \({\cal B}\) consists of the `1430` macro blocks and the `5005`
singleton `U` blocks.  A macro has its two fixed incidences.  A singleton
\(U\) may use any facet \(T\subset U\), and currently uses exactly two.

Form the directed residual exchange graph \(D_{\cal H}\) on
\({\cal U}\cup{\cal T}\) by orienting

\[
 T\longrightarrow U\quad\text{for a currently selected incidence},
 \qquad
 U\longrightarrow T\quad\text{for an unselected legal incidence}. \tag{1.2}
\]

Macro incidences do not occur in \(D_{\cal H}\), because they are frozen.

### Lemma 1.1 (circuits are exactly directed residual cycles)

A simple conformal switch of the residual integral `b`-flow is exactly a
simple directed cycle of \(D_{\cal H}\).  If its length is \(2t\), it deletes
\(t\) selected incidences and inserts \(t\) unselected incidences.  Every
singleton owner and every rank-eight colour retains its prescribed degree.

#### Proof

At every vertex of a directed cycle, one selected incidence enters the
deleted shore of the toggle and one unselected incidence enters the added
shore.  Hence the degree change is zero.  Conversely, a conformal connected
degree-zero change in a bipartite graph alternates selected and unselected
edges and therefore has the orientation (1.2).  A simple connected such
change is one directed cycle.  General integral differences decompose into
these circuits. \(\square\)

In particular, owner coverage and lower-q1 coverage are automatic.  They do
not need to be reimposed on a circuit catalogue.

## 2. Hamiltonicity is an exact fragment transition test

Let \(\Gamma\) be a directed residual cycle and let \(R\) and \(B\) be its
deleted and added incidence sets, each of size \(t\).  Delete \(R\) from the
Hamilton cycle \({\cal H}\).  The result consists of exactly \(t\) retained
path fragments, allowing a one-vertex fragment when deleted incidences are
adjacent.  Contract every retained fragment and add the incidences in \(B\).
Call the resulting multigraph \(Q_\Gamma\).

Every contracted fragment has two free half-ports, and the added incidences
use every half-port once.  Thus \(Q_\Gamma\) is two-regular.

### Theorem 2.1 (one-cycle monodromy criterion)

The toggled factor

\[
                 {\cal H}'={\cal H}\mathbin\triangle\Gamma
\]

is Hamiltonian if and only if \(Q_\Gamma\) is connected.  Equivalently,
every nonempty proper union of retained fragments is crossed by an added
incidence.

#### Proof

Expansion of a vertex of \(Q_\Gamma\) restores the corresponding retained
path and changes neither the number nor the incidence pattern of connected
components.  Since \(Q_\Gamma\) is two-regular, it is connected exactly when
it is one cycle.  The cut statement is the ordinary characterization of
connectedness. \(\square\)

### Corollary 2.2 (incidence hexagons)

For \(t=3\), the toggle is Hamilton-safe if and only if no added incidence
is a loop after contraction.

#### Proof

A loop in a two-regular graph is a component.  Conversely, a loopless
two-regular multigraph on three vertices must be the triangle: the degree
equations force one edge between every pair. \(\square\)

For \(t\ge4\), absence of loops is not enough; two or more nontrivial cycles
may remain.  This is the first precise obstruction to treating alternating
circuits as ordinary augmenting moves.

## 3. Every changed turn is one Johnson transport arc

For a port colour \(T\), each incident block has a distinguished physical
endpoint owner, a rank-nine superset of \(T\).  Suppose \(T\) lies on
\(\Gamma\).  Exactly one selected singleton incidence is replaced.  Write

\[
 U^-=T+a,\qquad U^+=T+c,
\]

for its old and new pure owners, and write

\[
 W_T=T+b
\]

for the unchanged physical endpoint on the other side of \(T\).  Legality
of the old and new factor makes \(a,b,c\) pairwise distinct.  The rank-ten
upper turn at \(T\) changes by

\[
 Y_T^-=T+\{a,b\}\quad\longrightarrow\quad
 Y_T^+=T+\{b,c\}.                                   \tag{3.1}
\]

Thus \(Y_T^-\) and \(Y_T^+\) are adjacent in \(J(17,10)\), sharing the
rank-nine set \(T+b\).

Let \(m(Y)\) be the total multiplicity of rank-ten upper colour \(Y\) in
the full physical carrier, including fixed macro interiors.  Direct every
arc (3.1) from old to new and let

\[
 o_\Gamma(Y)=\#\{T:Y_T^-=Y\},\qquad
 i_\Gamma(Y)=\#\{T:Y_T^+=Y\}.
\]

### Theorem 3.1 (literal upper-turn derivative)

For every rank-ten colour \(Y\),

\[
             m'(Y)=m(Y)-o_\Gamma(Y)+i_\Gamma(Y).    \tag{3.2}
\]

Consequently the switch loses no formerly present upper colour if and only
if

\[
       o_\Gamma(Y)-i_\Gamma(Y)\le m(Y)-1
       \quad\text{for every }Y\text{ with }m(Y)>0,  \tag{3.3}
\]

and it fills a missing colour \(Y\) if and only if \(i_\Gamma(Y)>0\).

#### Proof

Only the \(t\) touched port colours change their two physical neighbours.
At each such port (3.1) removes one occurrence and adds one occurrence.
Summing gives (3.2).  Conditions (3.3) and \(i_\Gamma(Y)>0\) are precisely
the assertions \(m'(Y)\ge1\) for an old colour and for a missing colour,
respectively. \(\square\)

The number of holes therefore changes by

\[
 \#\{Y:m(Y)>0,\ m'(Y)=0\}
 -\#\{Y:m(Y)=0,\ i_\Gamma(Y)>0\}.                  \tag{3.4}
\]

This formula correctly handles repeated sources, repeated targets, and a
colour which is both removed and re-added inside one packet.

### Corollary 3.2 (tag-sector invariance)

Every arc (3.1) preserves the subset of the two new coordinates carried by
the upper colour.  Hence residual-flow transport has four invariant tag
sectors.  In the authenticated carrier their missing counts are

\[
                    618,\quad623,\quad650,\quad0.  \tag{3.5}
\]

#### Proof

Both \(U^-\) and \(U^+\) are pure old owners.  All new-coordinate tags in
either upper union come from the unchanged endpoint \(W_T\), so the tag set
is the same before and after the switch.  The counts in (3.5) are the
independently frozen literal census in
`MATH_THEOREM_K17_FIXED_MACRO_RESIDENCE_OBSTRUCTION_20260731.md`. \(\square\)

## 4. Explicit hexagon signature

Every incidence hexagon in the rank-eight/rank-nine containment graph has a
rank-seven kernel \(K\) and distinct external coordinates \(a,b,c\).  In one
orientation its deleted-to-added incidences are

\[
\begin{array}{ccl}
 K+a+b:&K+a&\longmapsto K+b,\\
 K+b+c:&K+b&\longmapsto K+c,\\
 K+c+a:&K+c&\longmapsto K+a.
\end{array}                                         \tag{4.1}
\]

The other orientation reverses all three arrows.  If the unchanged endpoint
at \(K+x\) adds \(w_x\), its three upper arcs are obtained from

\[
 K+x+\{w_x,\text{old extra}}
 \longrightarrow
 K+x+\{w_x,\text{new extra}}.                     \tag{4.2}
\]

Equations (4.1)--(4.2), Corollary 2.2, and (3.3) are a complete constant-time
certificate for an alternating `C6`: alternation, one-cycle topology, and
lossless upper gain require no physical replay beyond the endpoint table.

The frozen exact census gives

\[
\begin{array}{c|r}
\text{alternating incidence hexagons}&7225\\
\text{Hamilton-safe}&3625\\
\text{Hamilton-safe and lossless}&1711\\
\text{fill three holes and lose none}&15.
\end{array}                                         \tag{4.3}
\]

The fifteen last rows attain the theoretical maximum of three newly filled
colours for a half-length-three switch.  By Lemma 1.1, Corollary 2.2 and
Theorem 3.1, toggling any one of them gives a literal owner-complete,
lower-q1-complete Hamilton carrier with `1888` rather than `1891` missing
rank-ten colours.  This is an exact one-step existence consequence, although
no particular output cycle is frozen in this note.  The complete literal
payload is

```text
scratch/k17_residual_flow_c6_decoration_20260731.audit.json
```

and its source is

```text
scratch/audit_r_k17_residual_flow_c6_decoration_20260731.py
```

The script reconstructs the contracted Hamilton cycle, uses the six-port
pairing test of Theorem 2.1, and computes (3.2) from the literal physical
cycle.  Its extended audit also verifies that the fifteen maximum rows have
disjoint incidence supports and enumerates their complete `2^15` transition
cube.  It finds `10270` Hamilton states, `10128` Hamilton-prefix-reachable
states, and a thirteen-row prefix-safe packet filling `39` distinct holes
without loss (terminal hole count `1852`).

There is a useful exact refinement.  The fifteen supports are in fact
pairwise vertex-disjoint: they use `45` distinct singleton owners and `45`
distinct port colours.  Thus their incidence toggles commute.  Their
aggregate upper signature loses no old colour and fills `44` distinct holes
(one new colour is repeated).  Nevertheless their all-at-once transition
system has four cycles, of object lengths

\[
                         4033,\quad1817,\quad370,\quad215.       \tag{4.4}
\]

So even a disjoint, individually Hamilton-safe, maximally efficient packet
need not be Hamilton-safe in aggregate.  This is replayed without a subset
search by

```text
scratch/audit_r_k17_maximal_c6_packet_monodromy_20260731.py
scratch/k17_maximal_c6_packet_monodromy_20260731.audit.json
```

## 5. The exact provider augmenting-path formulation

Fix an ordered provider corner

\[
       U^+\xrightarrow{e}T\xrightarrow{f}U^- .     \tag{5.1}
\]

Here \(e\) is unselected and \(f\) is selected.  Suppose replacing the
selected singleton \(U^-\) at \(T\) by \(U^+\), against the unchanged other
endpoint at \(T\), creates a desired missing upper colour.  Delete \(e\)
temporarily.

### Theorem 5.1 (provider-path theorem)

Simple residual circuits containing the ordered corner \(e,f\) are in
bijection with simple directed paths

\[
                  P:T\leadsto U^+\quad\text{in }D_{\cal H}-e,   \tag{5.2}
\]

whose first arc is \(f\), via \(\Gamma=P+e\).  Such a path gives a
lower-rainbow Hamilton switch
which loses no old upper colour exactly when

1. the fragment graph \(Q_{P+e}\) is connected; and
2. inequalities (3.3) hold for the turn arcs of \(P+e\).

It fills precisely the distinct initially missing labels entered by those
arcs.

#### Proof

Removing \(e\) from a simple directed cycle containing the corner leaves the
directed path (5.2), whose first arc records exactly which selected
incidence at \(T\) is evicted.  Adding (5.1) closes a simple directed cycle.
Lemma 1.1 gives degree and lower-colour preservation, Theorem 2.1
gives Hamiltonicity, and Theorem 3.1 gives the exact upper verdict. \(\square\)

When \(T\) has two selected pure incidences, specifying \(e\) without \(f\)
does not identify the fixed opposite endpoint and hence does not identify a
provider target.  The ordered corner is the minimal seed.

This is the smallest exact augmenting-path reduction.  Ordinary reachability
in \(D_{\cal H}\) is only the first row: the path must carry both a fragment
monodromy state and an upper-debt state.

### Proposition 5.2 (transport decomposition)

For any lossless packet, the directed multigraph of its upper arcs decomposes
into directed cycles and directed paths so that every path with positive
source divergence starts at a colour \(Y\) at most \(m(Y)-1\) times, and
every filled old hole is the endpoint of at least one path.

Conversely, those source-capacity conditions imply (3.3), provided every old
hole that is claimed filled receives an arc.

#### Proof

Decompose an arbitrary directed multigraph into cycles and paths after
pairing incoming and outgoing arcs at every vertex.  The number of paths
starting at \(Y\) is the positive part of
\(o_\Gamma(Y)-i_\Gamma(Y)\), which is at most \(m(Y)-1\) exactly by (3.3).
A missing old colour has no outgoing arc, because no old turn bears that
label.  If filled, it has positive indegree and hence terminates at least one
path.  The converse is the same balance calculation. \(\square\)

The proposition is an upper-label flow theorem, not a lifting theorem.
Paths in the rank-ten transport graph are coupled into residual incidence
circuits, and those circuits are further coupled by Theorem 2.1.

## 6. Exact finite state for a compound packet

For a packet whose total deleted support has size \(t\), cut the original
cycle at those incidences.  An exact compositional state consists of:

1. the pairing/component relation on the at most \(2t\) boundary half-ports;
2. the signed balances \(i(Y)-o(Y)\) for every touched upper label, together
   with its initial multiplicity capped at the largest possible departure;
3. for residence through depth \(d\), the prefix and suffix bit runs of every
   retained fragment, capped at \(d+1\), plus the flag that the whole fragment
   is constant in that coordinate and a flag recording an already-internal
   forbidden run.

Joining packet pieces updates these three rows deterministically.  The
accepting root states are respectively:

* one component;
* inequalities (3.3) and the requested filled labels; and
* no forbidden internal run.

This is finite for fixed \(t,d,k\).  Its connectivity row cannot be replaced
by parity or by the binary cycle-space equation.  Degree-preserving changes
are Eulerian over `GF(2)`, but connected two-factors are not a linear or
matroidal subfamily.

A minimal abstract illustration starts from the cycle

\[
                 1,2,3,4,5,6,7,8,1.
\]

The exchange

\[
 \{12,56\}\mapsto\{16,25\}
\]

splits it into two cycles, and so does

\[
 \{34,78\}\mapsto\{38,47\}.
\]

Applying both exchanges at once gives the Hamilton cycle

\[
                 1,8,3,2,5,4,7,6,1.          \tag{6.1}
\]

After subdividing the old edges by fixed colour vertices, this is a
degree- and colour-preserving two-factor example: in the first exchange keep
the `2` endpoint of the colour on `12` and the `6` endpoint of the colour on
`56`, and swap their other endpoints `1,5`; do the analogous operation on
`34,78`.  It is not asserted to be
a Boolean-containment `C4` (the Boolean incidence graph has no `C4`); its
purpose is the exact logical one: cycle-space feasibility and even two
individually tested moves do not provide a monotone Hamilton path.  In the
Boolean fibre the corresponding obstruction first has to be sought among
incidence `C6` and longer packets, with the fragment state retained.

There is one harmless parity check.  Modulo two, every turn arc changes two
upper multiplicity coordinates.  Therefore the parity vector
\(m'-m\pmod2\) has even Hamming weight.  This is necessary, but far weaker
than the monodromy and source-capacity conditions.

## 7. Residence locality and the fixed-macro obstruction

For a positive coordinate run, include its entering and leaving transitions
in its **closed edge support**.  If a rethread leaves every edge in this
closed support inside one retained fragment, the run is unchanged, even if
the fragment is reversed.  Hence every changed run of length at most \(d\)
lies in the radius-\(d\) collar of a deleted or added incidence.  This proves
the residence state in Section 6 is exact rather than heuristic.

More strongly, if a run's closed support lies strictly inside one fixed
macro, no residual-flow switch can change it at all.  The authenticated
carrier has exactly `605` such length-three runs, by

```text
MATH_THEOREM_K17_FIXED_MACRO_RESIDENCE_OBSTRUCTION_20260731.md
scratch/k17_fixed_macro_residence_obstruction_20260731.audit.json
```

Therefore no selection or sequence of the circuits in this note makes the
fixed macro family depth-three resident.  The strengthened theorem audits
all occurrence transversals of the same parent: among `1425` `A`-shore
patterns `0 1 1 1 0`, exactly `165` (eleven per old coordinate) use four
rank-six colours having unique physical occurrences.  Their support edges
are forced, so the corresponding avoidance clauses are empty.  Thus merely
changing the retained occurrences also cannot finish this fixed parent.
The independently certified coupled optimum is `180` internal short runs;
the extra `15` above the solver-free floor are an integral cross-coordinate
correlation cost.
This remains a sharp scoped obstruction, not a global one: changing the
parent chronology or changing the compiler schedule lies outside it.

## 8. Quantitative consequence for the authenticated carrier

The carrier has `24310` rank-ten turn occurrences, `17557` distinct upper
colours and `1891` missing upper colours.  Its total surplus occurrence count
is

\[
                         24310-17557=6753.           \tag{8.1}
\]

Thus scalar source capacity exceeds the number of holes.  However a
half-length-\(t\) residual circuit packet changes at most \(t\) port turns,
so it introduces at most \(t\) previously missing colours.

### Corollary 8.1 (support floor)

Any residual-flow packet which fills all `1891` current rank-ten holes has
total deleted-incidence support at least

\[
                              t\ge1891.              \tag{8.2}
\]

#### Proof

Every missing colour needs a new occurrence, and only a touched port turn can
create one.  There are at most \(t\) touched turns. \(\square\)

The fifteen `fill_3, lose_0` hexagons prove that the local efficiency bound
can be attained.  They do not prove a `631`-hexagon completion: their
supports may overlap, sources may cease to be surplus, later hexagons may
cease to alternate, and the compound fragment transition system may acquire
subtours.  An exact constructive continuation must therefore select a
large correlated circuit packet with the three states of Section 6 for upper
service.  To finish residence as well, it must change the parent chronology
or use a genuinely nonflat compiler; occurrence selection inside this parent
is now closed.

## 9. Independently checked proof boundary

The general claims above use only:

* degree conservation on a directed alternating circuit;
* contraction/expansion of paths;
* the literal two-neighbour definition of an upper turn; and
* directed multigraph balance.

The decisive implication was checked in both directions: connected
\(Q_\Gamma\) expands to one cycle, while any disconnected
\(Q_\Gamma\) expands to the same number of factor components.  In
particular, the `C6` shortcut requires all three new links to be nonloops;
checking only that one link crosses an old arc is insufficient.

The numerical `C6` census (4.3) and the `605` immutable-run count are exact
finite inputs with their own scripts and payloads.  This note did not rerun
or extend either enumeration.  It proves how those inputs compose and why
neither by itself supplies a complete `K17` decoration.
