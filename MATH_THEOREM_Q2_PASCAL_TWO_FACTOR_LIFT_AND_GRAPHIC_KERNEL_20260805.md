# The q2 Pascal lift from a spanning two-factor and its exact graphic kernel

**Date:** 2026-08-05  
**Method:** pure mathematics; componentwise cyclic surgery and an exact
occurrence-CSP reduction; no computation or search  
**Status:** unconditional implication.  The Hamilton-cycle Pascal
turn-section lift extends to an arbitrary spanning middle-levels two-factor
provided the complement of the section meets every factor cycle.  Endpoint
completion remains canonical, including factor cycles on which the section
is empty.  The combined section-plus-cycle-hit condition is an exact
`O(Cat_r)` occurrence-labelled CSP.  Applied to the canonical PBBS
two-factor, q2 section compatibility is already solved; only the cycle-hit
clauses remain.

## 1. A spanning middle-levels two-factor

Let `Gamma` have order `2r-1`, let `z` be new, and put

\[
 \Omega=\Gamma\dot\cup\{z\},\qquad
 P={2r-1\choose r-1},\qquad
 Q={2r-1\choose r-2},\qquad
 \kappa=P-Q=\operatorname {Cat}_r.                 \tag{1.1}
\]

Let `H` be a spanning two-factor of the middle-levels incidence graph on
`Gamma`.  Write each component cyclically as

\[
 X_{a,0},U_{a,0},X_{a,1},U_{a,1},\ldots,
 X_{a,p_a-1},U_{a,p_a-1},                           \tag{1.2}
\]

where

\[
 X_{a,i}\in{\Gamma\choose r-1},\qquad
 U_{a,i}=X_{a,i}\cup X_{a,i+1}\in{\Gamma\choose r}. \tag{1.3}
\]

All `X`-states and all `U`-states occur exactly once globally, and
`sum_a p_a=P`.  Define the turn occurrences

\[
 Y_{a,i}=X_{a,i-1}\cap X_{a,i}\in{\Gamma\choose r-2}. \tag{1.4}
\]

Choose a set `S` of turn positions satisfying:

1. exactly one occurrence of every member of `binom(Gamma,r-2)` belongs to
   `S`;
2. every `D in binom(Gamma,r-3)` occurs as
   `Y_(a,i) cap Y_(a,i+1)` for two adjacent positions in `S`; and
3. on every factor component, at least one turn position is outside `S`.

The first two rows say that `S` is a q2-complete section.  The third is the
**graphic** or **cycle-hit** condition.  Since `|S|=Q`, its complement has
exactly `kappa` positions.

## 2. The z-sector forest

For every selected adjacency `i,i+1 in S` on component `a`, put

\[
 (z+Y_{a,i})(z+Y_{a,i+1}).                           \tag{2.1}
\]

Let `s` be the total number of nonempty selected runs over all factor
components.  Because every component has an omitted position, the graph
`F_Z` in (2.1) is a spanning `s`-component linear forest on

\[
 z+{\Gamma\choose r-2}.                              \tag{2.2}
\]

It has `Q-s` edges.  Its union colours are the distinct values

\[
 z+X_{a,i}\qquad(i,i+1\in S),                        \tag{2.3}
\]

and its intersections cover every member of
`z+binom(Gamma,r-3)`.

The proof is componentwise: selected runs are paths; two adjacent distinct
rank-`(r-2)` facets of `X_(a,i)` have union `X_(a,i)`; and row 2 of the
section hypothesis is exactly the lower-intersection coverage.

## 3. Componentwise A-sector surgery

On a factor cycle which has both selected and omitted positions, perform
the run-boundary surgery of the Hamilton-cycle theorem independently on
each omitted run.  Namely, if

\[
 p\in S,\quad d_1,\ldots,d_\ell\notin S,\quad
 a=d_\ell+1\in S,                                    \tag{3.1}
\]

delete the A-sector edges indexed by every omitted occurrence except the
last, and delete at the last position the edge following it:

\[
 e_{d_1-1},e_{d_2-1},\ldots,e_{d_{\ell-1}-1},e_{d_\ell}. \tag{3.2}
\]

Add the cross edge

\[
 X_{d_\ell}--(z+Y_a).                                \tag{3.3}
\]

Here and below the factor-component index is suppressed.

If an entire factor cycle is omitted, delete **all** of its A-sector
edges and add no cross edge on that component.

Exactly one A-edge is deleted per omitted turn occurrence.  As every
factor cycle is hit, deleting `d_a>=1` edges from its projected A-cycle
leaves exactly `d_a` path components.  Summing gives

\[
 \#\operatorname{comp}(F_A)=\sum_a d_a=\kappa,
 \qquad |E(F_A)|=P-\kappa=Q.                        \tag{3.4}
\]

There is one cross edge for every nonempty selected run, hence `s` in all.
Each joins one Z-path endpoint to an A-path endpoint.  Distinct cross edges
use distinct Z-components and distinct endpoint roles, so they create
neither a cycle nor degree three.  Therefore the combined graph `F` has

\[
 (\kappa+s)-s=\kappa                                  \tag{3.5}
\]

components and

\[
 |E(F)|=Q+(Q-s)+s=2Q.                                \tag{3.6}
\]

## 4. Palette proof

All A-edge unions are distinct because they are members of the globally
bijective bank `(U_(a,i))`.  The z-containing unions are

* `z+X_(a,i)` at selected-selected adjacencies; and
* `z+X_(a,d_ell)` at omitted-to-selected run boundaries.

These cyclic adjacency types are disjoint, and every `X` occurs globally
once.  Thus all edge unions of `F` are distinct.

For intersections avoiding `z`, first delete the A-edge occurrence at
every omitted turn position.  The retained occurrences are exactly the
chosen one-per-colour section.  On each proper omitted run, surgery instead
retains its last omitted occurrence and deletes the following selected
occurrence; the cross edge (3.3) restores the latter intersection.  A wholly
omitted component contains no selected occurrence and needs no restoration.
Hence every member of `binom(Gamma,r-2)` remains covered.  Section row 2
and (2.1) cover every z-containing rank-`(r-2)` target.

We have proved:

### Theorem 4.1 (two-factor Pascal lift)

Under the three hypotheses in Section 1, `F` is a spanning
`Cat_r`-component linear forest on `binom(Omega,r-1)`.  It covers every
rank-`(r-2)` set as an edge intersection, and all of its rank-`r` edge
unions are pairwise distinct.

## 5. Canonical endpoint completion

For every proper omitted run, use the endpoint assignment from the
Hamilton-cycle lift:

1. assign the terminal Z-endpoint `z+Y_p` to `z+X_p`;
2. for `j=d_1,...,d_(ell-1)`, assign one endpoint role at `X_j` to
   `z+X_j`;
3. assign the opposite endpoint role created by deleting
   `X_(j-1)X_j` to `U_(j-1)`; and
4. assign the endpoint `X_a` created by deleting
   `X_(d_ell)X_a` to `U_(d_ell)`.

These are literal containments and use exactly the `2 ell` union colours
left unused by that run.

There is one new case.  If a factor component is wholly omitted, every
`X_(a,i)` is isolated in `F_A` and has two endpoint roles.  Assign them to

\[
 z+X_{a,i}\qquad\hbox{and}\qquad U_{a,i-1}.          \tag{5.1}
\]

Both contain `X_(a,i)`.  As `i` varies, (5.1) exhausts exactly the unused
z-bank and A-bank colours of that component.

The component-indexed banks are disjoint globally.  Hence these assignments
biject all `2 kappa` endpoint roles to all unused rank-`r` owners, with each
endpoint contained in its assigned owner.  Inserting the edge union at each
internal transition and the assigned owners at the endpoints lifts every
path of `F` to an owner-once rank-`r` path.

### Theorem 5.1 (two-factor endpoint completion)

The endpoint completion theorem remains valid componentwise for every
spanning two-factor satisfying the cycle-hit condition, including factor
cycles on which the chosen section is empty.  No additional endpoint Hall
problem remains.

## 6. Exact combined section-plus-graphic kernel

Assume the turn word is q1- and q2-surjective.  For each repeated q1 label
`Y`, let `O(Y)` be its occurrence set, let `a_Y in O(Y)` be its selected
occurrence, and put

\[
 \mathcal R=\{Y:|O(Y)|\ge2\},\qquad
 H=\bigcup_{Y\in\mathcal R}O(Y).                    \tag{6.1}
\]

The sparse-kernel theorem gives the exact positive q2 constraints

\[
 \forall D\text{ exceptional},\qquad
 \bigvee_{i\in E_D}
 \bigwedge_{Y\in\{Y_i,Y_{i+1}\}\cap\mathcal R}
 [a_Y=\text{the endpoint occurrence in }i].         \tag{6.2}
\]

For a factor cycle `C`, every position whose q1 label is globally unique is
selected in every section.  A repeated-label position `p` is omitted
exactly when

\[
 a_{Y_p}\ne p.                                      \tag{6.3}
\]

Therefore the cycle-hit condition is exactly the negative clause

\[
 \boxed{
 \bigvee_{p\in C\cap H}[a_{Y_p}\ne p]
 }
\qquad\text{for every factor cycle }C.              \tag{6.4}
\]

An empty disjunction means that `C` contains only globally unique q1
labels; then no one-occurrence section can hit it.

### Theorem 6.1 (exact combined kernel)

A q2-complete section whose complement meets every factor cycle exists if
and only if the positive constraints (6.2) and the graphic clauses (6.4)
have a common assignment.

Moreover, with `kappa=Cat_r`, this instance has at most

* `kappa` variables and `2 kappa` total domain values;
* `4 kappa` exceptional q2 constraints/witness terms;
* `2 kappa` nontrivial factor-cycle clauses; and
* `2 kappa` total literal occurrences across all factor-cycle clauses.

#### Proof

The positive equivalence is the sparse exceptional-kernel theorem.  Formula
(6.3) proves (6.4) exactly.  Conversely, a common assignment selects one
occurrence of every repeated label and the unique occurrence of every other
label; (6.2) gives q2 coverage and (6.4) punctures every factor cycle.

There are at most `2 kappa` repeated occurrence positions.  Distinct factor
cycles partition them, so both the number of nonempty graphic clauses and
their total length are at most `2 kappa`.  The remaining bounds are the
sparse-kernel bounds. `square`

Thus the extra graphic requirement does not destroy kernelization: the
whole two-factor lift is governed by a Catalan-scale signed occurrence CSP.

## 7. Application to the PBBS two-factor

Set `m=r-1`, so the canonical PBBS step-two factor lives on the rank-`m`
layer of a `(2m+1)`-set.  The theorem

`MATH_THEOREM_PBBS_MAX_HEIGHT_Q1_SECTION_IS_Q2_COMPLETE_20260805.md`

constructs one explicit assignment satisfying every positive q2 constraint
(6.2).  Therefore only (6.4) remains.

The exact PBBS graphic gate is:

\[
 \boxed{
 \text{every }f^2\text{-cycle contains a q1 occurrence which is not the
 globally selected max-height occurrence of its colour}.}
                                                               \tag{7.1}
\]

Two useful sufficient conditions are immediate.

1. If every `f^2`-cycle contains two occurrences of the same q1 colour,
   then at most one of those occurrences is selected, so (7.1) holds.
2. More generally, if one can choose the maximum-height ties in the q1 rule
   so that every `f^2`-cycle loses one occurrence, the complete two-factor
   Pascal lift follows.  The q2 proof is unaffected by these tie choices,
   because the two q1 blocks induced by every canonical q2 witness are
   uniquely tallest.

The PBBS action--angle theorem proves scalar feasibility: every PBBS period
is odd, so `f^2` has the same components as `f`; their number is at most
`Cat_m`, while the q1 section omits

\[
 {2m+1\choose m}-{2m+1\choose m-1}
 =\operatorname {Cat}_{m+1}                         \tag{7.2}
\]

occurrences.  Since `Cat_(m+1)>Cat_m`, there are more than enough omissions
in total.  This does not prove their componentwise distribution.

No existing MSW, Middle Levels, or PBBS theorem cited here states either
sufficient condition 1 or (7.1).  The remaining q2 ordered-diamond gate is
therefore no longer section compatibility; it is the signed cycle-hit
system (6.4) inside an already feasible positive kernel.

## 8. Scope

Proved:

1. the Pascal section lift and endpoint completion for arbitrary spanning
   middle-levels two-factors under exact cycle-hit;
2. the exact combined positive-q2/negative-graphic occurrence CSP and its
   `O(Cat_r)` size;
3. on the PBBS factor, unconditional feasibility of the positive half and
   exact isolation of the remaining graphic clauses.

Not proved:

1. the PBBS cycle-hit clauses for every `m`;
2. Hamiltonization of the odd-ground factor;
3. q3 or higher intersection rows, residence, or the literal compiler; or
4. `nu(k)=B(k)+O(1)`.

