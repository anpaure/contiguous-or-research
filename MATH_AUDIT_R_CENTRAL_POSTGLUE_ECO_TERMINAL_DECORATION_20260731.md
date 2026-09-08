# Audit: raw ECO Hamiltonization and terminal decoration are separate gates

Date: 2026-07-31  
Status: exact conditional central-CLMT theorem; exact correction to the first
post-glue draft; exact `m=2`, `m=4`, and project-`m=5` calibrations; no
all-dimension existence theorem

## 0. Verdict

The proposed quantifier simplification is valid for the **central Catalan
Linear Matching** object, with one necessary correction.

The proof-safe factorization is

\[
 \boxed{
 \begin{array}{c}
 \text{(A) a collision-free strict ECO incidence hypertree}\cr
 \Downarrow\cr
 \text{one undecorated Hamilton cycle}\cr
 \Downarrow\cr
 \text{(B) an unrestricted alternating-circuit packet}\cr
 \Downarrow\cr
 \text{one terminal forest-decorated Hamilton cycle.}
 \end{array}}
 \tag{0.1}
\]

No decoration, forced owner, residual gap matching, or occurrence router is
needed during (A).  However, “joint alternating SDR” in the last line is not
quite sufficient: the **same occurrence-level SDR** must lie off the unique
binary-trace cycle face.  Without that clause one gets a perfect diamond
matching and maximum physical degree two, but possibly one cyclic component.

The weakest exact missing statement in this middle-levels-supported route is
therefore not a transparent-gluing theorem.  It is:

> For every `m>=2`, some Hamilton cycle of `ML(2m-1)` has a perfect
> turn-augmentation matching whose induced binary trace is a forest trace.

The all-`m` Stage-(A) ECO hypertree is an independent constructive target;
because any two 2-factors differ by alternating circuits, it does not reduce
the content of this terminal theorem.  Neither target supplies residence,
deep shadows, socket/voltage state, RSB survival, or the common compiler.

## 1. Stage (A): the exact undecorated topology theorem

Let `F` be a spanning two-factor, with initial component set `V`.  For each
selected ECO incidence atom `t`, let `S_t subset V` be the set of initial
components containing its three old factor edges and put

\[
                         w_t=|S_t|-1.                 \tag{1.1}
\]

Assume:

1. different atoms have disjoint physical port sets;
2. every atom is a strict physical hypermerge: whenever the current blocks
   containing `S_t` are distinct, the toggle merges exactly those blocks and
   splits none; and
3. the component--atom incidence graph on `V disjoint-union T`, with
   `v--t` iff `v in S_t`, is a tree.

### Theorem 1.1 (decoration-free incidence-hypertree execution)

Toggling all atoms gives one Hamilton cycle.  No decoration data enter the
proof.

#### Proof

Port disjointness makes the symmetric differences commute and preserves
degree two.  Before a pending atom `t` is toggled, two members of `S_t`
cannot already lie in the same current component: an earlier incidence path
between them together with their two edges through `t` would make a cycle in
the incidence graph.  Strictness therefore decreases the component count by
exactly `w_t`.

The tree edge count is

\[
 \sum_t |S_t|=|V|+|T|-1,
 \qquad\text{hence}\qquad
 \sum_t w_t=|V|-1.                                  \tag{1.2}
\]

Starting from `|V|` components, the final degree-two factor has one
component and is Hamiltonian.  \(\square\)

The exact hypergraphic sparsity rows are

\[
 \sum_{t:S_t\subseteq X}w_t\le |X|-1
       \quad(\varnothing\ne X\subsetneq V),
 \qquad
 \sum_t w_t=|V|-1,                                  \tag{1.3}
\]

together with literal port compatibility and the physical strictness test.
The last test is real: a ternary atom meeting three distinct cycles is
automatically clean, whereas a two-touch atom has a doubled-cycle pairing
phase which may merge or may leave a `4+2` factor.

Current all-`m` ECO supply proves connectedness of the unfiltered component
two-section and gives an explicit collision path forest.  It does **not**
prove a port-disjoint strict incidence tree.  Connected two-section is
insufficient already for supports `{1,2,3}` and `{1,2,4}`, whose incidence
graph contains `1-t_1-2-t_2-1`.  Thus (A) remains an honest selection gate.

An ordinary component-path bank is a useful stronger subface, not without
loss of generality.  The clean binary star with supports
`{0,1},{0,2},{0,3}` is a valid Hamiltonizing incidence tree but cannot tile
one component path.  Hence path-DAG integrality does not itself prove (A).

## 2. Stage (B): circuit realization is not an existential gate

### Theorem 2.1 (two-factor difference decomposition)

Let `F,F'` be two spanning 2-factors of the same graph.  Then
`F symmetric-difference F'` decomposes into edge-disjoint closed alternating
circuits.  Toggling those circuits successively preserves degree two and
ends at `F'`.

#### Proof

Colour `F-F'` red and `F'-F` blue.  At every vertex the red and blue degrees
are equal, since both factors have degree two.  Pair red and blue half-edges
at each vertex and follow the pairings; this partitions the symmetric
difference into closed alternating trails, which may be split at repeated
transition states.  On each circuit the numbers of deleted and inserted
incident edges agree at every vertex, so toggling preserves degree two.
Edge-disjoint unprocessed circuits retain their red/blue status.  After all
toggles precisely `F-F'` has been deleted and `F'-F` inserted.  \(\square\)

Consequently, from **any** Stage-(A) Hamilton cycle `C_0`, a post-glue packet
to a terminal Hamilton cycle `C_*` exists if and only if such a terminal
cycle exists.  Intermediate packet states need only be 2-factors; requiring
every prefix to remain Hamiltonian is a stronger optional routing normal
form.

## 3. The exact terminal matching and trace criterion

Fix a Hamilton cycle

\[
 C=A_0,B_0,A_1,B_1,\ldots,A_{Q-1},B_{Q-1},A_0
 \quad\text{of }ML(2m-1),                            \tag{3.1}
\]

and put

\[
 Q=\binom{2m-1}{m-1},\qquad
 P=\binom{2m-1}{m-2},\qquad
 K=Q-P=\operatorname{Cat}_m.                         \tag{3.2}
\]

The turn-augmentation graph has shores

\[
 \{A_i\}\sqcup\binom{[2m-1]}{m-2}
 \quad\text{and}\quad
 \{B_j\}\sqcup\binom{[2m-1]}{m+1}.                 \tag{3.3}
\]

It contains the literal cycle edges `A_i B_{i-1}, A_i B_i`, the upper-turn
occurrence edge `A_i u_i`, and the lower-turn occurrence edge
`ell_j B_j`.  A perfect matching is exactly one joint alternating upper and
lower occurrence SDR.

Equivalently, choose an upper SDR `I`; between consecutive chosen upper
occurrences form the cyclic gaps.  The lower side is the
**occurrence-refined** gap graph: an edge `(G,L;j)` records that position
`j in G` has lower colour `L`.  Ordinary gap Hall guarantees a colour
matching, but the realizing occurrence `j` must still be retained because
it determines the trace.

Write the trace of one perfect turn-augmentation matching as

\[
                    1^{a_1}0^{b_1}\cdots1^{a_s}0^{b_s}.
                                                               \tag{3.4}
\]

Alternation makes every `b_i` positive and even.

### Theorem 3.1 (fixed-cycle central criterion)

The supported physical lift is a Catalan linear forest if and only if the
turn-augmentation graph has a perfect matching for which

\[
      (\exists i\ b_i\ge4)
      \quad\text{or}\quad
      (\exists i\ a_i\text{ even}).                 \tag{3.5}
\]

It then has exactly `K=Cat_m` path components.

#### Proof

The perfect matching gives a perfect Boolean-diamond matching.  Its physical
lift spans `2Q` middle vertices, has

\[
                         P+Q=mK                       \tag{3.6}
\]

edges, and has maximum degree two.  The binary-trace theorem says it has a
cycle exactly on the complementary face

\[
                     b_i=2\ \forall i,
               \qquad a_i\text{ odd}\ \forall i.    \tag{3.7}
\]

Off that face it is a forest.  Euler's identity and
`2Q-(P+Q)=Q-P=K` give the component count.  \(\square\)

The trace row is automatic when `K` is odd.  Indeed, on (3.7) there would be
exactly `K` zero-runs and therefore `K` one-runs.  The total number of marked
positions is `2P`, even, but it would be a sum of `K` odd integers; hence
`K` must be even.

The trace row is otherwise independent.  At `m=2`, select the unique upper
and lower turn colours on opposite rail positions of `ML(3)=C_6`.  The
trace is `100100`.  Gap Hall is `K_{1,1}` and the selected shores alternate,
but the physical lift is one `C_4` plus two isolated vertices.  This is the
smallest literal refutation of “joint alternating SDR implies CLMT.”

### Corollary 3.2 (the exact two-stage implication)

Stage (A), followed by any terminal Hamilton cycle and one perfect
turn-augmentation matching satisfying (3.5), proves the central Catalan
Linear Matching statement in that dimension.

This is an exact sufficient theorem for the middle-levels-resolvable class.
It is not a necessary representation theorem for arbitrary Catalan linear
diamond matchings.

## 4. Comparison with repair-first transparent collars

The two proof routes have different quantifiers.

### Post-glue existential route

* Stage (A) stores only literal physical compatibility, strict component
  gain, and incidence-tree topology.
* The decoration is chosen globally and only at `C_*`.
* No all-six colour coherence, fixed `(I,J)`, forced-owner residual Hall,
  leaf-owner alignment, or local-`Q` occurrence router is imposed on the
  ECO glues.
* The exact missing theorem is one forest-decorable Hamilton cycle for every
  `m`, not a transparent path from a prescribed decoration.

### Repair-first transparent route

For a fixed decoration, one incidence-hex toggle preserves it exactly when

1. its selected local turn-colour multisets agree separately on the two
   shores; and
2. after reconnection, the retained-fragment boundary mark types alternate.

If a leaf-peelable decoration is required, its changed gap attachments must
also remain acyclic after contracting the retained gap forest.  A protected
trace breaker (or the terminal trace bit) is still needed.  These conditions
give a prefix-stable recursive interface, owner matching, and possible
private-routing state.  They are strictly stronger than terminal existence.

The exact `ML(7)` census quantifies this separation.  There are `31`
alternating incidence hexagons, `16` Hamilton outputs, `10` decorable
outputs after representatives may change, and only `6` outputs with a
common forest decoration.  The same authoritative theorem gives one
explicit incidence-hex repair of the gap-Hall counterexample.  Thus
terminal repair is genuinely weaker, while transparent preservation is a
nonempty and useful recursive face.

Neither central route, by itself, supplies residence, deeper shadows,
prefix/cut survival, socket or primitive voltage, Pascal reachability,
RSB state, or common-`Q` compiler compatibility.  Those rows remain
downstream and must not be inferred from a terminal decoration.

## 5. Exact project-`m=5` post-glue calibration

The canonical project-`m=5` factor has component orders `36,72,144`.  The
two standard ECO atoms `g0,g1` have disjoint ports and component supports
`{36,144}` and `{72,144}`.  Individually they give profiles `72+180` and
`36+216`; together they give one `252`-vertex Hamilton cycle.  This is a
strict raw binary incidence tree.

That raw Hamilton cycle has the period-three turn deficit.  The synchronized
three pairwise-disjoint `C10` packet is then applied **after** the glues.
Every prefix is Hamiltonian, its augmented matching ranks are

\[
                         207,208,209,210,              \tag{5.1}
\]

and the terminal matching has a gap forest and a zero-run of length four.
Its physical lift is exactly a `42=Cat_5` path forest.  The `C10` supports
avoid the twelve ECO ports, so the same endpoint also admits the stronger
repair-first presentation.  This proves both orders at `m=5`, not an
all-dimension induction.

## 6. Sharp remaining boundary

The two unresolved uniform statements are:

* **(A)** choose, in every dimension, a pairwise-port-disjoint strict ECO
  incidence hypertree (optional as a central existence proof, but useful as
  a canonical-factor construction); and
* **(B)** prove the Decorated Middle Levels theorem of Section 0.

Because of Theorem 2.1, (B) is the weaker and logically decisive central
gate.  Proving (A) does not force (B); proving (B), together with ordinary
Middle Levels Hamiltonicity, already proves the middle-levels-supported
central CLMT architecture.  A repair-first private collar proves a stronger
recursive interface but is not necessary for this existential conclusion.

The exact finite audit is
`scratch/audit_catalan_postglue_eco_hypertree_terminal_sdr_20260731.py`.
It independently replays the raw `m=5` incidence tree, the post-glue
three-`C10` chronology, augmented ranks and trace, the commuting
repair-first order, the `m=2` obstruction, and the `ML(7)` `31/16/10/6`
census.  No finite computation is used in the all-dimension implications.
