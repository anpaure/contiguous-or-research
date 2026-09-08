# Independent audit of the two post-glue Catalan routes

Date: 2026-07-31  
Verdict: **GO**, with one necessary binary-trace clause; exact project-`m=5`
post-glue replay; no all-`m` decorated-Hamilton, RSB, compiler or `nu=B`
claim

## 1. Exact central implication

The authoritative post-glue reduction is correct.  Let `F,F'` be spanning
two-factors of one graph.  Colour `F-F'` red and `F'-F` blue.  At each
vertex the red and blue degrees agree.  Pair red and blue half-edges at each
vertex and follow the pairings; this decomposes `F triangle F'` into
edge-disjoint closed alternating circuits.  Toggling them successively keeps
degree two and ends at `F'`.  Intermediate factors need not be connected or
decorated.

Consequently, once any raw ECO construction supplies one Middle Levels
Hamilton cycle, alternating-circuit realization adds no existential gate.
There is a post-glue repair to an accepting endpoint if and only if an
accepting decorated Hamilton endpoint exists.

For completeness, a pairwise port-disjoint, subsetwise strict ECO family
whose component--atom incidence graph is a tree does supply such a starting
Hamilton cycle.  The incidence-tree identity

\[
                    \sum_t(|S_t|-1)=|V|-1
\]

and strictness reduce the initial component count to one in every atom
order.  This is a sufficient Stage-A certificate, not the remaining central
theorem.

## 2. Necessary trace correction

A perfect terminal augmented occurrence matching gives a joint alternating
upper/lower SDR and a spanning physical graph of maximum degree two.  It is
a Catalan **linear** matching only if the induced binary trace is off the
unique cycle face

\[
  \text{every zero-run has length two and every one-run is odd}.   \tag{2.1}
\]

The clause is necessary already for `m=2`.  On the standard six-cycle of
`ML(3)`, mark `A_0` and `B_12`.  The trace is `100100`; it selects the unique
upper and lower turn colours and alternates by shore, but its physical edges
are

\[
                 12,15,24,45,
\]

which form the four-cycle `1-2-4-5-1`, with positions `0,3` isolated.
Thus “joint SDR implies CLMT” is false without the forest-side trace test.

The weakest exact central statement is therefore the **Decorated Middle
Levels theorem**:

> for every `m>=2`, `ML(2m-1)` contains one Hamilton cycle whose augmented
> occurrence graph has a perfect matching whose induced binary trace is on
> the linear-forest side.

A leaf-peelable gap forest is a stronger useful target, not a necessary
central condition.

## 3. Reconciliation with the recursive transparent route

The two architectures have different interfaces.

* The minimal existential route chooses the decoration only at the terminal
  Hamilton cycle.  No forced owner, residual gap matching, occurrence
  router, or prefix decoration is required during raw gluing.
* The recursive transparent route carries one fixed decoration through a
  gluing tree.  For each hex toggle it must jointly preserve (i) the selected
  local turn-colour multisets, separately on both shores, and (ii) the
  alternating boundary mark types of the retained fragments.  If
  leaf-peelability is carried, the changed gap attachment must also remain
  acyclic after contraction.

Separate shore rainbows, an arbitrary frozen SDR, and an arbitrary Middle
Levels gluing tree do not imply those joint rows.  The authenticated `m=4`
census is exact:

\[
 31\text{ alternating hexes},\quad16\text{ Hamilton outputs},\quad
 10\text{ decorable outputs},\quad
 6\text{ transparent Hamilton outputs admitting a common forest decoration}.
\]

Thus transparent gluing is a stronger sufficient recursive route to the
minimal theorem, not a necessary existence interface.  Preassigned
period-three filters are stronger again: all `729` complete complement-
paired banks fail support on the known repaired `m=5` decorated Hamilton.

## 4. Independent project-`m=5` post-glue replay

The canonical factor has component orders `36,72,144`.  The two standard
ECO atoms are, edge for edge,

```text
g0 = Z(101010), touching components 0 and 2,
g1 = Z(101100), touching components 1 and 2.
```

Their ports are disjoint and their incidence graph is the path
`0-g0-2-g1-1`.  Literal component profiles are

```text
none:      36,72,144
g0:        72,180
g1:        36,216
g0+g1:     252
```

Only after this Hamiltonization, the replay applies the three frozen `C10`
circuits.  Each is alternating and Hamilton-safe at its stage.  The
augmented matching ranks are

\[
                         207\to208\to209\to210.
\]

The terminal state has complete turn palettes, `84` marked occurrences on
each shore, a forest gap graph and a forest binary trace.  Hence it is an
exact post-glue central CLMT certificate.  The `30` circuit vertices avoid
the `12` glue ports, so this finite fixture also admits the repair-first
ordering; the general post-glue theorem does not assume such commutation.

## 5. Downstream scope

Post-glue repair is one RSB regeneration node.  After the terminal
decoration, residual phase, physical lift, connectors and opening are fixed,
residence, deep-shadow witnesses, gain--Brauer/socket state and the compiler
must be recomputed.  Decoration or ECO disjointness alone transports none of
those states.  Therefore the central reduction does not prove `nu=B`.

## 6. Replay

Run

```text
python3 scratch/audit_catalan_postglue_eco_hypertree_terminal_sdr_20260731.py
```

The replay authenticates the two authoritative route theorems and their
frozen `m=4`/period-three audits, reconstructs the complete `m=5` chronology,
and builds the `m=2` trace obstruction directly.
