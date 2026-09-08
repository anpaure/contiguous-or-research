# K17 `h=1`: augmented-incidence lollipop reduction

**Date:** 2026-08-02  
**Status:** exact central-layer reduction.  The later theorem
`MATH_THEOREM_ODD_MIDDLE_LEVELS_FIXED_BOUNDARY_LOLLIPOP_EXISTENCE_20260802.md`
proves unconditionally that this degree/connectivity core is feasible for
every fixed adjacent boundary pair.  Neither note supplies residence, the
upper deck, or the lower compiler, and neither claims a length-24313 word.

## 0. Result

Put

\[
 r=9,\qquad \mathcal Q={{[17]}\choose 8},\qquad
 \mathcal T={{[17]}\choose 9},\qquad W=24310.
\]

The physical-edge formulation of the `h=1` face uses one variable for each
Johnson edge `(Q;a,b)`, hence

\[
 W{9\choose2}=875160                                  \tag{0.1}
\]

carrier variables, plus equally many opening variables and the missing/
duplicated-colour interface.

The same central object is equivalent to a connected degree-constrained
subgraph of the Middle Levels incidence graph using only

\[
                       9W=218790                       \tag{0.2}
\]

binary incidence variables.  The selected graph is a forced lollipop: one
alternating tail entering one alternating cycle.  Its Euler trail is exactly
the augmented coatom chronology needed by the exceptional boundary port.

Moreover, the missing colour, duplicated colour, and initial owner may all
be fixed by symmetry.

## 1. The boundary port forces a Johnson pair

Let `M` be the unique missing rank-eight colour and `D` the unique duplicated
rank-eight colour.  Open one of the two physical `D`-edges, and suppose its
initial owner `B` contains `M`, as required by the occurrence-port identity.

### Lemma 1.1 (forced boundary triangle)

Necessarily

\[
 |M\cap D|=7,\qquad B=M\cup D.                       \tag{1.1}
\]

Conversely, if distinct rank-eight sets `M,D` satisfy `|M cap D|=7`, then
their union is the unique rank-nine owner containing both.

#### Proof

The opened edge has colour `D`, so both endpoints contain `D`.  The port
condition gives `M contained-in B`.  Thus the rank-nine set `B` contains
`M union D`.  Since `M` and `D` are distinct rank-eight sets,

\[
 9\ge |M\cup D|=16-|M\cap D|\ge9.
\]

All inequalities are equalities.  The converse is immediate. \(\square\)

The symmetric group on `[17]` is transitive on ordered Johnson-adjacent
rank-eight pairs.  Every `h=1` solution is therefore isomorphic to one with

\[
 D=\{0,1,\ldots,7\},\qquad
 M=\{0,1,\ldots,6,8\},\qquad
 B=\{0,1,\ldots,8\}.                                \tag{1.2}
\]

There is only one orbit to search, not eight intersection types.

## 2. Replace the opening by the missing boundary incidence

Given a physical `h=1` Hamilton cycle, remove its opened incidence `DB` and
insert the incidence `MB`.  Keep every other selected containment incidence.
Call the resulting simple bipartite graph `G^+`.

The degrees in `G^+` are

\[
\begin{aligned}
 \deg(T)&=2 &&(T\in\mathcal T),\\
 \deg(M)&=1,\\
 \deg(D)&=3,\\
 \deg(Q)&=2 &&(Q\in\mathcal Q\setminus\{M,D\}).     \tag{2.1}
\end{aligned}
\]

The unique edge at `M` is `MB`.  The graph is connected because the physical
owner cycle was connected and the replacement changes only the label of its
opened boundary half-edge.

Conversely, start with binary incidence variables

\[
 y_{Q,T}=1\quad\Longleftrightarrow\quad Q\subset T
 \text{ is selected},                               \tag{2.2}
\]

and impose (2.1), connectedness, `y_(M,B)=1`, and
`y_(M,T)=0` for `T not equal B`.

### Theorem 2.1 (lollipop theorem)

Every connected graph satisfying (2.1) is the union of:

1. one alternating simple path from `M` to `D`; and
2. one alternating simple cycle through `D`, otherwise disjoint from the
   path.

Consequently it has an Euler trail from `M` to `D` which uses every selected
incidence once.  Along that trail every owner occurs once, every coatom other
than `D` occurs once, and `D` occurs twice.

#### Proof

There are `2W` active vertices and, by summing owner degrees, `2W` edges.
Thus a connected `G^+` is unicyclic.  All vertices have degree two except
the leaf `M` and the degree-three vertex `D`.

The unique cycle must contain `D`: otherwise the component joining `M` to
that cycle would create either another leaf or a second vertex of degree
three.  Removing the cycle edges at `D` leaves one path whose endpoints are
`M` and `D`.  No branch can leave either object because there are no further
non-degree-two vertices.  This proves the asserted decomposition.

Traverse the tail from `M` to `D`, then traverse the cycle once and return
to `D`.  Every edge is used once.  Every owner has degree two and hence is
visited once; the same holds for ordinary coatoms.  The shared vertex `D`
is encountered at the tail/cycle junction and at the final endpoint.
\(\square\)

### Corollary 2.2 (exact augmented coatom chronology)

Write the coatom occurrences on the Euler trail as

\[
                         Q_0,Q_1,\ldots,Q_W.          \tag{2.3}
\]

Then

\[
 Q_0=M,\qquad Q_W=D,                                 \tag{2.4}
\]

the multiset in (2.3) contains every member of `mathcal Q` once and one
additional occurrence of `D`, and

\[
                         Q_i\cup Q_{i+1}=T_i          \tag{2.5}
\]

lists every owner `T_i in mathcal T` exactly once.

#### Proof

The occurrence statement is Theorem 2.1.  Consecutive coatoms on the trail
are distinct rank-eight subsets of their intervening rank-nine owner, so
their union is that owner.  Every owner occurs once. \(\square\)

## 3. Recover the physical `h=1` cycle

The first owner on the trail is `B`, because `MB` is the unique incidence at
`M`.  Let `A` be the final owner before the endpoint occurrence `Q_W=D`.

Delete `MB` and add `DB`.  In the ordered interpretation, pair this new
`DB` half-edge with the terminal `DA` half-edge to form the opened physical
`D`-edge `BA`.  At the internal occurrence of `D`, pair its two trail
incidences.  Every ordinary coatom already pairs its two trail incidences.

This produces a physical Hamilton cycle on all owners.  Its q1 colour
multiset has load zero at `M`, load two at `D`, and load one everywhere else.
Opening `BA` recovers the Euler chronology (2.3).

The construction also covers the case in which the two physical `D`-edges
share `B`: this occurs exactly when `DB` was already one of the three
selected incidences at `D`.  The augmented graph itself remains simple.

Conversely, Section 2 transforms every physical `h=1` solution satisfying
the boundary-port condition into such a connected `G^+`.  Therefore the two
representations are equivalent, including the shared-owner case.

## 4. Exact smaller master

The base model has the `218790` variables (2.2) and the rows

\[
\begin{aligned}
 \sum_{Q\subset T}y_{Q,T}&=2 &&(T\in\mathcal T),\\
 \sum_{T\supset Q}y_{Q,T}&=2
                    &&(Q\in\mathcal Q\setminus\{M,D\}),\\
 \sum_{T\supset M}y_{M,T}&=1,\\
 \sum_{T\supset D}y_{D,T}&=3,\\
 y_{M,B}&=1.                                         \tag{4.1}
\end{aligned}
\]

The fixed last row and the degree-one row force every other `M` incidence
to zero.  No physical-edge variables, opening variables, port variables, or
missing/duplicated selector variables are required.

The remaining gates are added fail-closed.

1. **Connectivity.**  A decoded component not containing `M` yields the
   exact cut

   \[
      \sum_{Q\in S,T\notin S}y_{Q,T}
      +\sum_{Q\notin S,T\in S}y_{Q,T}\ge
      \begin{cases}
        1,&D\in S,\\
        2,&D\notin S.
      \end{cases}                                    \tag{4.2}
   \]

   The first case separates the two odd vertices and hence has odd cut
   parity.  The second contains neither odd vertex and hence has even cut
   parity.  Both inequalities are necessary for, and together exclude,
   every non-root component.
2. **Orientation.**  Once connected, the tail is fixed.  The unique cycle
   has two orientations, giving at most two augmented owner chronologies.
3. **Rank-ten coverage.**  Decode the physical cycle from Section 3.  Every
   missing rank-ten target gives the exact lazy disjunction of the incidence
   pairs that would realize it on a non-opened physical edge.  For an
   ordinary coatom the two selected incidences determine that edge.  At `D`,
   two selected incidences alone do **not** identify the retained physical
   pair: one `D` incidence is on the tail and the other two are the cycle
   incidences.  A `D`-provider term must therefore include a certified
   cycle-membership/topology witness.  Until such a witness is channelled,
   a failed `D`-dependent row may use only the complete decoded-assignment
   no-good.
4. **Residence and deeper upper rows.**  Replay the two possible Euler
   chronologies with the existing literal first-arrival and linear age-run
   oracles.  Add only a certified dependency cut or, failing that, the exact
   incidence no-good.
5. **Lower compiler.**  On an accepted augmented coatom chronology, solve
   the age/refresh two-row compiler and finally replay all `131071` nonzero
   targets in the emitted length-24313 word.

The reduction changes only the representation of the central selector.  It
does not weaken any acceptance gate.

## 5. Scope-safe consequence

The first theorem-guided non-equivariant fallback now has a `218790`-variable
bipartite degree core rather than `2017730` variables before lazy rows.  A
connected base assignment has only two possible physical chronological
decodings.  The boundary colours and owner are fixed outright by (1.2).

The central degree/connectivity system is now known to be satisfiable by the
fixed-boundary lollipop existence theorem cited at the top.  A selected
incidence factor must still pass literal residence, every upper target, the
named lower compiler, and the exhaustive word verifier.  Thus central
existence is no longer a search risk, but none of the downstream acceptance
gates is discharged by that existence theorem.
