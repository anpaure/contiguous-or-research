# Adjacent-swap carrier cycles are exact wreath trades

Date: 2026-07-27

## 1. Two-window adjacent move

Let \(n=2m+1\) and let \(\pi=(x_0,\ldots,x_{n-1})\) be a cyclic order.
Swap the adjacent positions \(p,p+1\), obtaining \(\pi'\).  Exactly two
length-\(m\) cyclic intervals change: the windows starting at

\[
 p+1\quad\text{and}\quad p+m+2\pmod n.              \tag{1.1}
\]

Write

\[
 R(\pi,p)=\mathcal M(\pi)\setminus\mathcal M(\pi'),
 \qquad
 A(\pi,p)=\mathcal M(\pi')\setminus\mathcal M(\pi).
\]

Thus \(|R|=|A|=2\), and the old and new wreaths share \(n-2\) middle
owners.

For an exact factor \(F\), there are \(n\) moves per row and \(C_m\) rows,
so the entire adjacent-move catalogue has exactly

\[
 nC_m=W                                                   \tag{1.2}
\]

members.

## 2. Directed carrier graph

Use pairs of middle owners as vertices and put one directed arc

\[
 R(\pi,p)\longrightarrow A(\pi,p)                       \tag{2.1}
\]

for every adjacent move.  The arc remembers its factor row and its literal
new wreath; this is the decoration missing from an uncoloured carrier graph.

### Theorem 2 (carrier-cycle trade)

Suppose

\[
 R_1\to R_2\to\cdots\to R_k\to R_1                  \tag{2.2}
\]

is a directed cycle whose arcs come from distinct rows of \(F\).  Replacing
each of those rows by its adjacent-swapped row is an exact support-matched
\(k\)-trade.

### Proof

On arc \(i\), the new row deletes the owner pair \(R_i\) and adds
\(R_{i+1}\).  Summed around (2.2), every pair is deleted and added once.
Because the original rows have disjoint supports and occur at most once, no
owner can be deleted twice.  The zero signed incidence therefore also
prevents any owner from being added twice.  The new rows are disjoint and
their union equals the old union. \(\square\)

Equivalently, among the edges of the odd-graph factor, each adjacent move
maps one factor edge to a new odd-graph edge.  Carrier cycles are precisely
the directed cycles that land back on factor edges with distinct row owners.

## 3. The discovered \(m=5\) carrier

The complete five-block search found a trade whose old/new owner-incidence
matrix, after ordering its five rows cyclically, has two nonzero entries in
each row and column:

\[
\begin{pmatrix}
0&0&0&9&2\\
0&0&2&0&9\\
9&2&0&0&0\\
2&0&9&0&0\\
0&9&0&2&0
\end{pmatrix}.                                         \tag{3.1}
\]

The entries \(9=n-2\) are the unchanged parts of adjacent-swapped wreaths;
the entries 2 are the transferred carrier pairs.  Hence (3.1) is literally a
decorated directed 5-cycle from Theorem 2.

At the source factor there are exactly three adjacent carrier cycles (all of
length five).  Their complete MWB search selects one with

\[
 G_H=85/8,qquad D_H=71/8,qquad
 \Delta\Phi_H=-7/4.                                    \tag{3.2}
\]

It produces the verified exact factor

```
scratch/m5_adjacent_carrier_next.txt
```

with

\[
\begin{array}{c|r}
\text{PBBS retention}&155\\
\text{weighted MWB}&185/4\\
\text{weighted CPCR}&649/8\\
\text{CPCR pairs}&215\\
\text{balanced }L^1&103\\
\text{zero cells}&17\\
\text{PCap at every depth}&0.
\end{array}
\]

The move certificate is
`scratch/m5_adjacent_carrier_next_certificate.json`.  At the terminal factor
the same linear catalogue again has exactly three carrier cycles, all
non-improving; this is certified by
`scratch/m5_adjacent_carrier_round2_report.json`.

## 4. Exact search calibration

`scratch/wreath_adjacent_carrier_cycles.py` constructs the \(W\) decorated
arcs and enumerates directed cycles.  The main search exposes the same family
through

```
--adjacent-move-catalogue
```

Around the source factor, the structural catalogue has 462 rows and the
support-closure search visits 407 states.  It finds exactly the same three
length-five trades as direct directed-cycle enumeration.  Its best trade is
identical to the best trade found by the complete 172,909-wreath five-block
census.  Thus the factorial search has been replaced, for this improvement,
by an exact linear-size construction.

## 5. Relation to separated double swaps

A separated double swap changes three windows and gives signed
3-in/3-out atoms.  Those atoms reproduce all 2-trades at \(m=3,4,5\), but at
the audited \(m=5\) factor they have no higher zero-sum circulation through
size five.  The successful five-trade instead comes from a directed cycle of
the simpler 2-in/2-out adjacent atoms.

This distinction is useful:

* inverse signed triples explain the complete 2-trade geometry;
* adjacent-pair cycles explain the first scalable higher trade; and
* general bounded trades can combine both kinds, but need not reduce to
  either one alone.

## 6. Remaining asymptotic gate

The carrier theorem removes middle-layer integrality and decoration at once.
The remaining assertion is quantitative:

> When weighted CPCR is \(\Omega(W)\), construct enough directed carrier
> cycles, or one suitable cycle, for which coherent lower-rank gain exceeds
> Dirichlet noise.

Uniform averaging is not adequate: the finite factor has only three carrier
cycles and just one is favorable.  A proof must relate the orientation of a
cycle to the current signed shadow imbalance.  This is now a precise
decorated-cycle inequality rather than an abundance-without-compatibility
problem.

## 7. Canonical MSW supply audit

The complete partial-functional graph can be decomposed in linear time, so
long cycles cannot hide beyond a search cutoff.  For the canonical MSW
factor, the exact finite values for \(3\le m\le10\) are

\[
\begin{array}{c|rrrrrrrr}
m&3&4&5&6&7&8&9&10\\ \hline
\#\text{ cycles}&6&8&10&12&14&16&18&20\\
\text{cycle length}&3&4&5&6&7&8&9&10.
\end{array}
\]

Thus the observed identity is exactly \(2m\) cycles, all of length \(m\).
No other cycle of any length occurs in these instances.  This pattern is not
yet proved for general \(m\).

It is also asymptotically too sparse by itself.  For \(m\ge5\), the audited
cycles touch

\[
 2m^2-2m-9
\]

distinct factor rows, only a polynomial number compared with
\(C_m\).  Approximately three quarters of all carrier arcs land on another
factor edge, but those internal arcs form branching in-trees feeding exits
or the \(2m\) short cycles.  They are not disjoint paths: the maximum audited
indegree is \(m-1\).

Therefore canonical MSW plus its existing carrier cycles cannot pay a linear
shadow defect.  A successful asymptotic use needs one of:

1. a new exact factor with \(\Omega(C_m)\) favorable carrier-cycle mass;
2. a path-closing/rewiring theorem that converts the abundant internal
   carrier arcs into cycles; or
3. a richer move atlas that closes the branching carrier forest.

The exhaustive audit is `scratch/audit_msw_adjacent_carriers.py`.

## 8. Exact closure deficiency and the finite carrier component

Let (f) be the partial carrier map on the (W) factor edges: an edge is
sent to the added pair of the corresponding adjacent swap when that pair is
again a factor edge, and otherwise it exits. If (T) is the set of distinct
internal targets, then the minimum number of arcs which **arbitrary**
retargeting would have to change to make (f) a permutation is exactly

\[
 W-|T|
 =\#\{\text{exiting arcs}\}
  +\sum_{t\in T}(d^-(t)-1).
\tag{8.1}
\]

Indeed, at most one existing arc into each (t\in T) can be preserved, and
preserving one for every (t) leaves exactly (W-|T|) missing targets and
the same number of arcs to replace. Equation (8.1) is only a closure
diagnostic: the replacement arcs need not be realizable by wreath moves.

The new profile is emitted by
`enumerate_all_adjacent_carrier_cycles`. For canonical MSW at (m=3,ldots,8)
the permutation deficiencies are

\[
8,38,153,593,2276,8722,
\]

while the cycle-vertex counts remain (2m^2). Thus the branching/exiting
forest, not a hidden long cycle, carries essentially all of the available
adjacent-swap mass.

`scratch/search_wreath_carrier_closure.py` explores the exact state graph
generated by the legal cycles, allowing closure to improve while MWB worsens.
From the current (m=5) factor the whole connected component has eight
states. Its best closure state has deficiency (197), down from (211), and
two of its three cycles have positive (G-D). Nevertheless its weighted MWB
is (373/8), whereas the starting state has (185/4); following a favorable
cycle returns toward the original basin. The certificate
`scratch/m5_carrier_beam_best_certificate.json` replays the two exact trades.

This finite trap sharpens the asymptotic target: carrier-cycle abundance and
positive compensation can be manufactured locally, but pure carrier cycles
do not enlarge the reachable component enough. A successful move atlas must
also close or reroute noncyclic carrier paths.

**Postscript.**  The first such rerouting primitive is now explicit: two
separated-double-swap triple atoms close an adjacent-carrier path by returning
one owner directly and sending the remaining pair through the path. See
`MATH_LEMMA_COUPLED_LOCAL_MOVE_CIRCULATIONS_20260727.md`. Thus the last
sentence is no longer only a target; it has a finite-verified construction,
although its asymptotic supply remains open.
