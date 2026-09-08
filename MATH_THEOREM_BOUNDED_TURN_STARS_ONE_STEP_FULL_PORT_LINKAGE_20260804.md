# Any bounded bank of lower-turn stars has a one-step full-port linkage

**Date:** 2026-08-04  
**Method:** pure mathematics; no computation, search, or solver  
**Status:** unconditional Boolean-incidence theorem.  It strengthens the
separated-turn theorem by allowing arbitrary distinct lower turns, including
adjacent turns with shared owner ports.  It constructs a raw simultaneous
typed-suffix linkage for the union of all owner stars.  Physical occurrence
materialization and bounded dynamic deletion remain separate premises.

## 0. Setting

Fix `m>=3`, put `n=2m-1`, and let

\[
 \mathcal L=\binom{[n]}{m-1},\qquad
 \mathcal U=\binom{[n]}m,\qquad
 \mathcal V=\binom{[n]}{m+1}.
\]

Choose arbitrary distinct lower turns

\[
 L_1,\ldots,L_p\in\mathcal L,
 \qquad
 1\le p\le\left\lfloor{m+2\over4}\right\rfloor.
\tag{0.1}
\]

For source `i`, put

\[
 C_i=[n]\setminus L_i,
 \qquad |C_i|=m,
\]

and define its complete owner star and terminal cloud by

\[
 P_i=\{L_i+a:a\in C_i\}\subseteq\mathcal U,
\tag{0.2}
\]

\[
 \mathcal V_i
 =\{L_i\cup\{a,b\}:\{a,b\}\in\tbinom{C_i}{2}\}
 \subseteq\mathcal V.
\tag{0.3}
\]

The terminal cloud is the edge set of the complete graph `K_{C_i}`.  The
edge `{a,b}` is incident with both owner ports `L_i+a` and `L_i+b`.

## 1. Exact pairwise overlap

For `i\ne j`, write

\[
 d_{ij}=|L_i\setminus L_j|=|L_j\setminus L_i|.
\]

### Lemma 1.1

The owner-star and terminal-cloud intersections satisfy:

\[
 |P_i\cap P_j|=
 \begin{cases}
 1,&d_{ij}=1,\\
 0,&d_{ij}\ge2,
 \end{cases}
\tag{1.1}
\]

and

\[
 |\mathcal V_i\cap\mathcal V_j|=
 \begin{cases}
 m-1,&d_{ij}=1,\\
 1,&d_{ij}=2,\\
 0,&d_{ij}\ge3.
 \end{cases}
\tag{1.2}
\]

When `d_{ij}=1`, the common terminals form one vertex-star in each of the
two complete-graph representations (0.3).

#### Proof

The union `L_i\cup L_j` has rank `m-1+d_{ij}`.  A common owner has rank
`m`, so it exists exactly at `d_{ij}=1`, when the union itself is unique.

A common terminal has rank `m+1`, so none exists for `d_{ij}\ge3`.  At
`d_{ij}=2`, the union itself has rank `m+1` and is the unique common
terminal.  At `d_{ij}=1`, write

\[
 L_i=H\cup\{a\},\qquad L_j=H\cup\{b\},\qquad |H|=m-2.
\]

A common terminal is

\[
 H\cup\{a,b,c\},
 \qquad c\in[n]\setminus(H\cup\{a,b\}),
\]

and there are `m-1` choices for `c`.  In the `j`-th terminal graph these
are exactly the edges `{a,c}` incident with the fixed vertex `a`; the
description on the `i`-th graph is symmetric.  \(\square\)

### Corollary 1.2 (cycle-supported overlap)

Suppose source `j` selects any subset of the edges of one Hamilton cycle
of `K_{C_j}`.  Then its selected terminal set meets `\mathcal V_i` in at
most two values for every `i\ne j`.

#### Proof

At exchange distance one, Lemma 1.1 turns the intersection into a vertex-
star, and a Hamilton cycle has degree two at that vertex.  At distance two
there is only one candidate, and at larger distance there is none.
\(\square\)

## 2. Simultaneous linkage of the union of owner stars

### Theorem 2.1

Let

\[
 P_0=\bigcup_{i=1}^pP_i.
\tag{2.1}
\]

There is an injection

\[
 \phi:P_0\longrightarrow\mathcal V
\tag{2.2}
\]

such that

\[
 U\subset\phi(U)qquad(U\in P_0).
\tag{2.3}
\]

Consequently the Boolean incidence graph between ranks `m` and `m+1`
contains `|P_0|` pairwise vertex-disjoint one-edge paths linking **every
distinct owner port in the union of the `p` stars** to a distinct terminal.

#### Proof

Process the sources in the order `1,\ldots,p`.  Assume all owner ports in
the earlier union have already received globally distinct terminals, and
that the terminals first assigned at each earlier source form a subset of
one Hamilton cycle in its graph `K_{C_j}`.

At source `i`, mark as forbidden every edge of `K_{C_i}` whose terminal
has already been used.  By Corollary 1.2, each earlier source contributes
at most two forbidden edges.  Hence the forbidden graph has at most

\[
 2(i-1)
\tag{2.4}
\]

edges.  After deleting them, the residual graph `H_i` satisfies

\[
 \delta(H_i)\ge m-1-2(i-1)=m-2i+1.
\tag{2.5}
\]

Because `i\le p\le floor((m+2)/4)`, the right side is at least `m/2`.
Dirac's theorem gives a Hamilton cycle in `H_i`.  Orient it cyclically.

For each coordinate `a\in C_i` whose owner `L_i+a` has **not** appeared in
an earlier star, assign to that owner the terminal indexed by the outgoing
cycle edge `{a,b(a)}`:

\[
 \phi(L_i+a)=L_i\cup\{a,b(a)\}.
\tag{2.6}
\]

The outgoing edges of distinct vertices on a directed Hamilton cycle are
distinct.  Thus all newly assigned terminals are distinct within this
stage.  They avoid all old terminals because the cycle lies in `H_i`.
Ports already seen retain their old terminal and receive no second path.

The newly selected terminal set is a subset of the current Hamilton cycle,
so the induction invariant required by Corollary 1.2 is retained.  After
the final stage, every port in `P_0` has been assigned exactly once.  The
ports and terminals are both globally distinct, proving vertex-disjointness
of the displayed incidence edges.  \(\square\)

## 3. Exact raw gammoid rank and deletion transfer

Let `Gamma_0` be the strict gammoid on `P_0` whose displayed sinks and
one-edge paths are those of Theorem 2.1.  Then

\[
 \boxed{r_{\Gamma_0}(P_0)=|P_0|.}
\tag{3.1}
\]

If a physical deletion bank `F` meets `h_F` of the displayed paths, then
the surviving paths prove

\[
 \boxed{
 |P_0|-r_{\Gamma_F}(P_0)\le h_F\le|F|.
 }
\tag{3.2}
\]

No subset Hall calculation is needed: this is a literal full linkage, and
one deleted unit-capacity vertex meets at most one displayed path.

### Corollary 3.1 (bounded-source wedge activation)

Assume in one residual cap/guard/phase/occurrence state that:

1. every owner and terminal value above is materialized as the distinct
   occurrence used by its displayed path;
2. every displayed containment `U subset phi(U)` is present as a typed
   legal residual edge from that owner occurrence to that terminal
   occurrence;
3. for every incidence `L_i subset U`, the literal source-to-owner prefix
   is completion-stable, has empty or private interior, and is disjoint
   from the suffix network except at `U`; different sources and owner
   values use distinct unit capacities;
4. the displayed suffixes end at legal typed sinks and avoid the fixed
   compensation linkage; and
5. the priced deletion bank meets at most `m-p` displayed suffix paths and
   does not delete the required source/prefix resources.

Then the near-full owner-gammoid theorem applies and selects one globally
owner/q1-terminal-distinct protected wedge at each of the `p` lower turns,
with a simultaneous typed route for every claim.

For bounded `p`, both `p<=floor((m+2)/4)` and `p<=m-1` hold for all
sufficiently large `m`.  Thus the raw full-port rank row is unconditional
at the Boolean-value level for **arbitrary distinct source turns**, not only
for a separated source bank.

## 4. Scope and remaining occurrence lemma

The theorem removes two former assumptions:

* the complete owner-star union need not be postulated independent in a
  suffix gammoid; it has the explicit one-step linkage above;
* lower turns need not be pairwise nonadjacent; shared owner ports are
  deduplicated and adjacent terminal overlap costs at most two edges per
  earlier source.

It does not prove that a materialized regenerative child has all selected
rank-`m+1` terminal occurrences and containment edges available with the
required type, that its source-to-owner prefixes have the required private
occurrence lift, or that its compensation/background deletion footprint
hits only `m-p` of these paths.  Those are now the exact remaining cap-state rows.  The companion
rank-layer and linear-footprint theorems give sufficient bounded-damage
conditions for that second row.

## 5. Dependencies

The only external combinatorial input is Dirac's Hamilton-cycle theorem.
The final activation corollary uses:

* `MATH_THEOREM_NEAR_FULL_OWNER_GAMMOID_PROTECTED_WEDGE_BYPASS_20260804.md`;
* `MATH_THEOREM_CAP_AWARE_PROTECTED_WEDGE_ACTIVATION_AND_EXACT_MENU_THRESHOLD_20260804.md`.
