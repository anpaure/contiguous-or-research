# The q2 Pascal lift from a turn section has a canonical endpoint completion

**Date:** 2026-08-05  
**Method:** pure mathematics; exact cyclic-word surgery and Pascal-sector
counting; no computation, search, solver, or probabilistic input  
**Status:** unconditional implication.  A middle-levels Hamilton cycle on
`2r-1` coordinates which has a `q2`-complete one-occurrence section of its
lower-turn word lifts explicitly to a spanning `Cat_r`-path forest on the
rank-`(r-1)` layer of `2r` coordinates.  The lifted forest covers every
rank-`(r-2)` intersection target, has pairwise distinct rank-`r` edge
unions, and its `2 Cat_r` endpoint roles match canonically to all unused
rank-`r` owners.  Thus the even-ground ordered-diamond correlation is
closed conditional only on the stated odd-ground turn-section property.
The existence of such a section for all `r` is not proved here.

## 0. Parameters and the exact Pascal split

Let `r>=3`, let `Gamma` have order `2r-1`, let `z` be a new coordinate,
and put

\[
 \Omega=\Gamma\dot\cup\{z\},\qquad
 P={2r-1\choose r-1},\qquad
 Q={2r-1\choose r-2},\qquad
 C=\operatorname {Cat}_r={1\over r+1}{2r\choose r}.
\tag{0.1}
\]

Then

\[
                         P-Q=C.                    \tag{0.2}
\]

The rank-`(r-1)` layer of `Omega` has the two Pascal sectors

\[
 \mathcal A={\Gamma\choose r-1},\qquad
 \mathcal Z=z+{\Gamma\choose r-2},                 \tag{0.3}
\]

of orders `P` and `Q`.  Its rank-`(r-2)` intersection targets split as

\[
 {\Gamma\choose r-2}
 \quad\dot\cup\quad
 \left(z+{\Gamma\choose r-3}\right),              \tag{0.4}
\]

while its rank-`r` union colours split into two equal banks

\[
 {\Gamma\choose r}
 \quad\dot\cup\quad
 \left(z+{\Gamma\choose r-1}\right),              \tag{0.5}
\]

each of order `P`.

An `A-A` Johnson edge uses the first bank in both (0.4) and (0.5).  A
`Z-Z` edge uses the second bank in both.  A cross edge

\[
                 X\;--\;(z+Y),\qquad Y\subset X,  \tag{0.6}
\]

has intersection `Y` and union `z+X`.  This mixed sector is what permits
the two odd-ground constructions to be joined without repeating a union
colour.

## 1. The odd middle-level cycle and its two turn rows

Fix a Hamilton cycle of `ML(2r-1)`, written cyclically as

\[
 X_0,U_0,X_1,U_1,\ldots,X_{P-1},U_{P-1},          \tag{1.1}
\]

where

\[
 X_i\in{\Gamma\choose r-1},\qquad
 U_i=X_i\cup X_{i+1}\in{\Gamma\choose r}.         \tag{1.2}
\]

Indices are taken modulo `P`.  The `U_i` are all distinct and hence
enumerate `binom(Gamma,r)`.

Define the lower-turn occurrence word

\[
                         Y_i=X_{i-1}\cap X_i
                         \in{\Gamma\choose r-2}.   \tag{1.3}
\]

Assume first-level turn surjectivity:

\[
                    \{Y_i: i\in\mathbb Z_P\}
                    ={\Gamma\choose r-2}.          \tag{1.4}
\]

There are `P` occurrences of `Q` labels, so the exact occurrence surplus
is `C`.

### Definition 1.1 (q2-complete turn section)

A set `S subseteq mathbb Z_P` is a **q2-complete turn section** if

1. for every `Y in binom(Gamma,r-2)`, exactly one index `i in S` has
   `Y_i=Y`; and
2. every `D in binom(Gamma,r-3)` occurs on an adjacent selected pair:

   \[
    \exists i\in\mathbb Z_P:\quad
       i,i+1\in S,\qquad Y_i\cap Y_{i+1}=D.        \tag{1.5}
   \]

Thus `|S|=Q` and its complement `D_0=mathbb Z_P setminus S` has order
`C`.  Let `s` be the number of cyclic runs of `S`.  Since `D_0` is
nonempty,

\[
                            1\le s\le C.            \tag{1.6}
\]

The section condition is the only hypothesis below which is not supplied
by the ordinary Middle Levels Theorem.

## 2. The selected turn forest in the z-sector

For every `i` with `i,i+1 in S`, put the edge

\[
 (z+Y_i)(z+Y_{i+1}).                               \tag{2.1}
\]

Call the resulting graph `F_Z`.

### Lemma 2.1 (selected runs are the exact z-sector forest)

`F_Z` is a spanning linear forest on `mathcal Z` with exactly `s`
components and `Q-s` edges.  Its edge unions are distinct and equal to

\[
                    z+X_i\qquad(i,i+1\in S),       \tag{2.2}
\]

and its intersections cover every member of
`z+binom(Gamma,r-3)`.

#### Proof

The section uses one occurrence of every `Y`, so the selected occurrence
positions identify bijectively with the vertices of `mathcal Z`.  The
induced subgraph of a cycle on a proper subset of its positions is a union
of paths, one for every cyclic run of selected positions.  This gives the
component and edge counts.

At the middle owner `X_i`, the two turns `Y_i,Y_(i+1)` are distinct when
both are selected, because a section cannot select two occurrences of the
same label.  Both are rank-`(r-2)` facets of `X_i`; hence

\[
 Y_i\cup Y_{i+1}=X_i,qquad
 |Y_i\cap Y_{i+1}|=r-3.                            \tag{2.3}
\]

The `X_i` are distinct, proving union injectivity.  Condition (1.5) proves
the intersection coverage.  \(\square\)

## 3. Run-boundary surgery in the A-sector

The projected owner cycle on `mathcal A` has edges

\[
                  e_i=X_iX_{i+1},                 \tag{3.1}
\]

with

\[
                  X_i\cap X_{i+1}=Y_{i+1},qquad
                  X_i\cup X_{i+1}=U_i.             \tag{3.2}
\]

Write one cyclic omitted run as

\[
 p\in S,quad d_1,d_2,\ldots,d_\ell\notin S,quad
 a=d_\ell+1\in S,                                 \tag{3.3}
\]

where `p=d_1-1`.  For this omitted run delete from the A-cycle the
`ell` edges

\[
 e_{d_1-1},e_{d_2-1},\ldots,e_{d_{\ell-1}-1},e_{d_\ell}.
\tag{3.4}
\]

In words: delete the edges indexed by every omitted occurrence except the
last one, and replace the deletion at the last omitted occurrence by the
edge indexed by the following selected run start.  Do this independently
for every omitted run, and call the remaining graph `F_A`.

Finally add the cross edge

\[
                 X_{d_\ell}\;--\;(z+Y_a)           \tag{3.5}
\]

for every omitted run.  It is legal because `Y_a subset X_(d_ell)`.
Call the union of `F_A`, `F_Z`, and all edges (3.5) the graph `F`.

### Theorem 3.1 (Pascal turn-section lift)

`F` is a spanning linear forest on `binom(Omega,r-1)` with exactly `C`
components.  It has `2Q` edges, every member of
`binom(Omega,r-2)` occurs as an edge intersection, and all edge unions are
pairwise distinct members of `binom(Omega,r)`.

#### Proof

There are exactly `C` omitted positions.  Formula (3.4) deletes one A-edge
per omitted position, hence `C` edges altogether.  Deleting `C` edges from
one cycle gives a spanning `C`-component linear forest `F_A` with `Q`
edges.

For a run (3.3), the endpoint `X_(d_ell)` created by deleting `e_(d_ell)`
still has its other A-edge `e_(d_ell-1)`: the deletion at the last omitted
position was precisely the one displaced in (3.4).  Thus it has A-degree
one.  The vertex `z+Y_a` is the initial endpoint of the corresponding run
of `F_Z`.  The cross edges (3.5) therefore join distinct Z-components to
A-endpoint occurrences.  They are a matching on the Z-component side and
cannot create a cycle or degree three.  Starting with `C+s` components,
the `s` cross edges leave exactly `C` components.

The A-edges not deleted have distinct union colours because the complete
bank `(U_i)` was distinct.  The Z-edges use `z+X_i` only for an `SS`
adjacency in the binary word of `S`.  The cross edge at a run start uses
`z+X_(d_ell)`, the corresponding `DS` adjacency.  These indices are all
distinct, and the A bank avoids `z`, so every union in `F` is distinct.

For intersections containing `z`, Lemma 2.1 applies.  For intersections
avoiding `z`, first imagine deleting the A-edge occurrence at every index
outside `S`.  The retained A-edges then contain exactly one occurrence of
every `Y`.  On each omitted run, surgery (3.4) instead retains the last
omitted occurrence `Y_(d_ell)` and deletes the selected occurrence `Y_a`.
The cross edge (3.5) has intersection exactly `Y_a`, restoring that target.
All other selected occurrences remain.  Hence every member of
`binom(Gamma,r-2)` is still covered.

Finally

\[
 |E(F)|=Q+(Q-s)+s=2Q
       =(P+Q)-C
       ={2r\choose r-1}-C,                         \tag{3.6}
\]

which agrees with the component count.  \(\square\)

## 4. Every missing owner has a canonical endpoint role

Theorem 3.1 leaves exactly `2C` unused rank-`r` union colours.  A priori
one would expect a separate endpoint Hall problem.  For the run-boundary
surgery, that matching is explicit.

Fix one omitted run (3.3).  The unused `z`-containing colours belonging to
that run are

\[
 z+X_p,z+X_{d_1},\ldots,z+X_{d_{\ell-1}}.          \tag{4.1}
\]

The colour `z+X_(d_ell)` is used by the cross edge.  Match:

1. the unjoined terminal Z-endpoint `z+Y_p` to `z+X_p`;
2. for `j=d_1,...,d_(ell-1)`, one A-endpoint role at `X_j` to
   `z+X_j`;
3. for every left-block deleted edge `e_(j-1)=X_(j-1)X_j`,
   `j=d_1,...,d_(ell-1)`, its other endpoint role at `X_(j-1)` to
   the unused colour `U_(j-1)`; and
4. the A-endpoint `X_a` of the right deleted edge
   `e_(d_ell)=X_(d_ell)X_a` to `U_(d_ell)`.

For a string of consecutive deleted A-edges, an internal isolated owner
has two endpoint **roles**; Items 2 and 3 use its two roles separately.

### Theorem 4.1 (canonical endpoint completion)

The assignments above, over all omitted runs, biject the `2C` endpoint
roles of `F` to

\[
 {\Omega\choose r}\setminus
       \{A\cup B:AB\in E(F)\},                    \tag{4.2}
\]

and every endpoint is contained in its assigned owner.  Consequently every
path component of `F` lifts to a rank-`r` owner path, and over all
components every rank-`r` owner of `Omega` occurs exactly once.

#### Proof

An omitted run of length `ell` contributes `ell` deleted A-edges and one
cross attachment, so it leaves `2ell-1` A-endpoint roles and one Z-endpoint
role.  Its unused colours consist of `ell` A-bank colours (the unions of
the deleted A-edges) and `ell` Z-bank colours (4.1), also `2ell` in all.

Item 1 uses one Z colour on the Z-endpoint.  Items 2--4 use the remaining
`2ell-1` colours on the A-endpoint roles.  Every displayed containment is
literal:

\[
 Y_p\subset X_p,qquad X_j\subset z+X_j,qquad
 X_{j-1},X_j\subset U_{j-1},qquad X_a\subset U_{d_\ell}.
\tag{4.3}
\]

The run banks are disjoint by their cyclic indices.  Thus all assignments
are distinct and exhaust both the endpoint roles and the unused colours.

Along one component, put the assigned owner at each endpoint and put the
edge union at every internal transition.  Two consecutive owners are
distinct rank-`r` supersets of their common rank-`(r-1)` state, so their
intersection is exactly that state.  The colours in (4.2) are disjoint
from all internal unions, proving owner-once globally.  This also handles
an isolated A-state: its two oriented endpoint roles receive two distinct
unused owners.  (An isolated state inside one left-deletion block receives
one avoiding-`z` and one containing-`z` owner; a singleton selected run
can instead receive two distinct avoiding-`z` owners from its two
neighbouring omitted runs.)  \(\square\)

## 5. Exact residual gate on the odd cycle

The remaining section problem has a compact occurrence-labelled form.
Introduce binary variables `x_i` on the cyclic turn occurrences.  A
q2-complete section exists if and only if

\[
 \sum_{i:Y_i=Y}x_i=1
 \quad\left(Y\in{\Gamma\choose r-2}\right),        \tag{5.1}
\]

and

\[
 \sum_{i:Y_i\cap Y_{i+1}=D}x_ix_{i+1}\ge1
 \quad\left(D\in{\Gamma\choose r-3}\right).       \tag{5.2}
\]

Equivalently, make a conflict graph whose vertices are the adjacent turn
occurrences `(i,i+1)` with `Y_i != Y_(i+1)` (equivalently, with
`Y_i intersection Y_(i+1)` of rank `r-3`), partitioned by their
intersection colour `D`.
Two occurrence edges conflict when they force two different occurrences of
the same rank-`(r-2)` label.  Then (5.1)--(5.2) hold exactly when this
conflict graph has an independent transversal of all `D`-classes; after
choosing the transversal, choose an arbitrary occurrence for every still
unforced `Y`-class.

This is an exact gate, not merely a sufficient relaxation.  In deletion
language, one chooses `C` occurrences, all but one from each repeated
`Y`-class, so that the deleted positions are **not** a vertex cover of the
occurrence-edge graph of any `D`-colour.

The ordinary assertions

* the turn word is surjective;
* every `D` occurs somewhere among adjacent turns; and
* the aggregate edge count exceeds `|binom(Gamma,r-3)|`

do not imply (5.1)--(5.2), because the only occurrences witnessing two
different `D`-classes may demand incompatible representatives of one
repeated `Y`.  The independent-transversal formulation is therefore the
sharp correlation left on this route.

## 6. Relation to the fixed-z MSW puncture

The fixed-coordinate MSW theorem produces separately:

1. an A-sector Catalan forest with exact upper colours; and
2. a Z-sector Catalan forest with injective lower colours.

Its centered-q2 condition asks those two marginal forests to coincide in
one puncture.  The construction above uses a different quantifier order.
It first chooses one occurrence of every odd-ground lower turn, keeps the
selected runs in the Z-sector, and uses the omitted runs themselves as the
complete bank of cross seams and endpoint-owner tickets.  Thus no claim
that every puncture, or even one canonical MSW puncture, is centered-q2
exact is needed.

What remains common to both routes is occurrence-level correlation.  In
the MSW language it is the centered multiplicity condition.  In the
Pascal-turn language it is exactly the section gate (5.1)--(5.2).

## 7. Scope

The exact positive conclusion is:

> a q2-complete turn section of one odd-ground middle-levels Hamilton cycle
> gives an even-ground owner-once Catalan path factor whose rank-`(r-2)`
> intersection palette is complete.

No separate endpoint Hall theorem is needed; Theorem 4.1 closes it
canonically.

The note does **not** prove:

1. that every `r` admits a middle-levels Hamilton cycle with a q2-complete
   turn section;
2. any `q>=3` intersection/union row;
3. residence or the literal lower compiler; or
4. `nu(k)=B(k)+O(1)`.

The next narrow theorem is the odd-ground independent-transversal problem
(5.1)--(5.2).  If the currently proposed one-sided turn-surjective forest
already includes a literal one-occurrence representative for every
rank-`(r-2)` turn and covers every rank-`(r-3)` adjacent-turn colour, then
that theorem is exactly the missing hypothesis and the even-ground q2
ordered-diamond lift is complete.
