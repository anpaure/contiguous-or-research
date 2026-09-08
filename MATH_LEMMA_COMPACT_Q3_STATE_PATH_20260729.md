# Compact exact lower/upper `q=2,3` state-path encoding

Date: 2026-07-29

## Setting

Let `k` be odd, let `r=(k+1)/2`, and let a selected directed quotient
Hamilton circuit lift to the equivariant physical carrier

\[
T_0,T_1,\ldots,T_{W-1}\in\binom{[k]}r.
\]

For a rank-`r-3` target `S`, lower-`q=3` coverage asks for an index `i`
such that

\[
T_i\cap T_{i+1}\cap T_{i+2}\cap T_{i+3}=S.
\]

In the graded one-core compiler this is not an extra frozen derivative-row
hypothesis.  It is nevertheless necessary: the top low target and its
maximal erosion envelope both have rank `r-3`, so positive Hall degree is
equivalent to the target occurring as such a four-window intersection.

## Lemma (state-path equivalence)

Define

\[
V_S=\{U\in\tbinom{[k]}r:S\subseteq U\}.
\]

There is a lower-`q=3` witness for `S` if and only if there are states
`U_0,U_1,U_2,U_3 in V_S` satisfying:

1. each directed Johnson step `U_j -> U_{j+1}` is the physical lift of a
   selected directed quotient arc; and
2. for every coordinate `x notin S`, at least one of the four states omits
   `x`.

Proof.  A physical witness supplies the four states, its three consecutive
selected arcs, and condition 2 because their intersection equals `S`.
Conversely, selected quotient arcs lift to a directed 2-factor.  Since every
physical vertex has one selected outgoing arc, the three selected steps
compose into four consecutive carrier states.  Every state contains `S`,
while condition 2 excludes every coordinate outside `S` from their common
intersection.  Their intersection is therefore exactly `S`.  Equivariance
then covers every translate in the orbit of `S`.  This remains valid for
short off-central orbits.  QED.

The same proof works verbatim at every depth `q`: use `q+1` states and `q`
selected transitions.  Its upper dual takes all central subsets of a
rank-`r+q` target `U` and requires every coordinate of `U` to occur in at
least one state.  Thus intersection and union shadows have one common exact
state-path representation.

There is a sharper common description.  Write each lower state as `S union
X_j`, and each upper state as `U minus X_j`, where every `X_j` is a `q`-set.
In both cases exact shadow coverage is

\[
                     \bigcap_{j=0}^{q}X_j=\varnothing.                 \tag{1}
\]

A Johnson step deletes one defect coordinate and inserts one.  There are
exactly `q` steps and `X_0` has exactly `q` coordinates.  Therefore (1) is
equivalent to the following finite certificate:

> the `q` deleted defect coordinates are pairwise distinct and all belong to
> the initial defect set `X_0`.

For an intersection witness, a defect deletion is the carrier coordinate
deleted by the step.  For a union witness, it is the carrier coordinate
inserted by the step, because that coordinate leaves the omitted set.

## CP-SAT encoding

For each missing lower or upper target orbit representative:

- enumerate the central supersets of a lower target, or the central subsets
  of an upper target;
- create `q+1` integer state variables in this domain;
- enumerate table rows `(u,v,a)` where `u,v` are adjacent states and `a` is
  the unique directed quotient arc whose lift is `u -> v`;
- put the same transition table on each of the `q` consecutive steps;
- use `AddElement(a, arc_vars, 1)` to require the selected quotient arc;
- record the defect coordinate deleted by each transition;
- require the `q` deleted coordinates to be all different;
- use a two-column table to require each deleted coordinate to belong to the
  defect set of the initial state.

At `k=15`, every rank-5 target uses only 120 states, at most 2520 transition
rows, and 10 explicit auxiliary variables (four states, three arcs, and three
deleted coordinates).  The earlier exact DNF had about
122,000 three-choice motif flags **per target**.  Thus this formulation is
exact rather than a relaxation, while reducing the auxiliary-variable count
by more than three orders of magnitude.

The corresponding `k=15` state/transition counts are:

| shadow | states | directed rows before self-loop omission |
|---|---:|---:|
| lower `q=2` | 36 | 504 |
| lower `q=3` | 120 | 2520 |
| upper `q=2` | 45 | 720 |
| upper `q=3` | 165 | 3960 |

## Validation

The implementation is in
`scratch/graded_quotient_pipeline.py` as
`QuotientCatalogue.shadow_state_template` and lazy constraint kind
`shadow-state-path`.  The older DNF builders remain only as independent
small-case regression oracles.

For every one of the 15 rank-3 target orbits at `k=11`, exhaustive composition
of all three-step state paths gives exactly the same set of selected-choice
triples as the independent diagnostic DNF `cover_lower_q3`.  The known
`k=11` strict carrier also supplies witnesses.  The repository regression
suite passes locally and with OR-Tools on the remote CPU host.

An actual OR-Tools solve with the known `k=11` selector fixed at Hamming
radius zero and simultaneous lower- and upper-`q=3` state-path constraints
returns `OPTIMAL`, independently checking the table/`AddElement` linkage.
