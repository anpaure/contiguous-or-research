# Alternating port hexagons preserve the exact K17 carrier and halve its downstream defects

Date: 2026-07-31  
Status: exact exchange theorem and independently replayed finite descent; no K17
word or improved numerical upper bound is claimed

## 0. Result

Start from the literal Hamilton/lower-rainbow K17 owner cycle in
`MATH_THEOREM_K17_PARENT_INDUCED_MACRO_PORT_HAMILTON_CYCLE_20260731.md`.
Keeping all `1430` physical residual macros fixed, a sequence of `1445`
connected alternating-hex exchanges changes only the two selected facets of
the pure `U` owners.  Every exchange preserves:

1. all `24310` rank-nine owners;
2. every rank-eight lower-q1 colour exactly once;
3. degree two at every port colour; and
4. one Hamilton owner cycle.

The lexicographic defect vector

\[
 (\text{upper-q1 holes},\ \text{positive runs of length }2\text{ or }3,
   \ \text{lower-q2 holes})
\]

improves from

\[
                  (1891,2892,1623)
             \quad\hbox{to}\quad
                  (812,1963,1345).                  \tag{0.1}
\]

The optimized literal cycle is

```text
scratch/k17_parent_induced_macro_port_hexopt_20260731.cycle
SHA-256 37a36e4b335ef3efaa2667e558b8477cfae46f4beff3cafe5c98c232a1f6c45a
```

This is a strict carrier improvement, not an optimal word.  The fixed-macro
residence obstruction remains: at least `605` length-three runs are wholly
internal to the macros and cannot be changed by any port-flow exchange.

## 1. The exact hex exchange

Let \(W\) be a rank-ten subset of `[15]` and choose three distinct rank-nine
facets \(U_0,U_1,U_2\subset W\).  Put

\[
 T_{01}=U_0\cap U_1,qquad
 T_{12}=U_1\cap U_2,qquad
 T_{20}=U_2\cap U_0.                                \tag{1.1}
\]

These are three distinct rank-eight sets.  The containment incidences

\[
 U_0-T_{01}-U_1-T_{12}-U_2-T_{20}-U_0              \tag{1.2}
\]

form a six-cycle.  If selected and unselected incidences alternate around
(1.2), toggle all six.

### Theorem 1.1 (alternating-hex invariance)

An alternating-hex toggle preserves degree two at every `U` owner and
preserves every residual demand \(d_T\) at every port colour.  After the
fixed macro incidences are reinserted, it therefore preserves the complete
rank-eight colour palette.  If the resulting two-factor is connected, it
preserves the literal Hamilton owner cycle as well.

#### Proof

Every \(U_i\) loses one selected incidence and gains the other incident
edge of (1.2).  Every \(T_{ij}\) likewise loses one selected incidence and
gains the other.  All other incidences are untouched.  Thus all degrees are
unchanged.  The macro incidences and physical macro interiors never move,
so the resulting graph is another exact solution of the port `b`-flow.
Suppressing its port-colour vertices gives the owner graph.  When it is
connected, degree two makes it one Hamilton cycle. \(\square\)

This is the smallest exchange because two distinct rank-nine owners share
at most one rank-eight facet, so the containment graph has no four-cycle.

## 2. Exhaustive move catalogue and descent

There are

\[
 {15\choose10}{10\choose3}=360360                 \tag{2.1}
\]

labelled hex templates.  At the initial flow, `7225` are alternating and
`3625` also preserve the single port cycle.  The C++ descent scans the whole
catalogue, accepts only connected toggles, and optimizes the defect vector
lexicographically.  It performs `1000` improving exchanges, exports an exact
checkpoint, resumes from that port state, and performs another `445` before
reaching its one-hex local optimum.

No SAT/CP optimizer is used.  Connectivity and all three objective terms are
replayed on the literal owner graph after every accepted move.

## 3. Independent downstream census

### Upper interval holes

\[
\begin{array}{c|rrrrrrrr}
\text{rank}&10&11&12&13&14&15&16&17\\ \hline
\text{missing}&812&754&116&3&0&0&0&0
\end{array}                                           \tag{3.1}
\]

The immediate upper holes split by new-coordinate signature as

\[
   \text{pure}=16,qquad X=418,qquad Y=378,qquad XY=0.  \tag{3.2}
\]

For comparison, before the exchange descent these numbers were
`618,650,623,0`.  Thus the port flow removes all but sixteen pure holes and
more than half of the total upper-q1 defect.

### Lower decks

\[
\begin{array}{c|c|c}
q&\text{distinct target-rank colours}&\text{missing}\\ \hline
2&18103/19448&1345\\
3&11567/12376&809
\end{array}                                           \tag{3.3}
\]

At depth three, `620` windows retain rank seven rather than dropping to rank
six.

### Residence

The short-run profile is

\[
            620\text{ runs of length }2,qquad
            1343\text{ runs of length }3.            \tag{3.4}
\]

The best possible one-edge opening neutralizes only three, leaving `1960`
short internal runs.  Moreover the separately audited fixed-macro theorem
identifies `605` length-three runs whose support and flanks are all internal
to a macro.  Consequently no further `U`-port exchange, object permutation,
or macro reversal can make this fixed macro family depth-three resident.

There is also a parent-universal strengthening.  The authenticated parent
has `1425` A-shore `0-111-0` patterns; `165` of them (exactly eleven per old
coordinate) have four unique rank-six edge colours.  Every lower-colour
occurrence transversal must retain all four edges, so these patterns remain
internal under **every** parent-induced forest choice.  Hence changing only
the retained occurrence transversal cannot repair residence either.  For
this parent, the obstruction survives all macro-port flows and all occurrence
choices in the present construction template.

## 4. Meaning for the general construction

The result separates two issues that were previously conflated.

* The unrestricted integral port flow is highly flexible: local exact
  exchanges can preserve the central theorem while repairing most upper
  service.
* Residence is not a port-flow problem, and for this parent it cannot be
  repaired by changing the retained rank-six occurrence transversal.  It
  requires a different parent/macro-interior construction or a nonflat
  compiler.

The all-dimensional target should therefore impose residence before the
parent is frozen, and only then use the port-flow/hex catalogue for
connectivity and upper service.

## 5. Artifacts

Search engine:

```text
scratch/search_k17_macro_port_hex_optimizer_20260731.cpp
```

Optimized port assignment and literal cycle:

```text
scratch/k17_parent_induced_macro_port_hexopt_20260731.uports.txt
scratch/k17_parent_induced_macro_port_hexopt_20260731.cycle
```

Independent full census:

```text
scratch/audit_k17_macro_port_hexopt_cycle_20260731.py
scratch/k17_parent_induced_macro_port_hexopt_20260731.audit.json
```
