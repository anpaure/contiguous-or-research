# Audit of the coherent-birail interchange reduction

Date: 2026-08-01  
Status: the abstract matrix theorem is verified, and the two displayed
conditional implications are correct.  Its new Hamiltonicity strength does
not address the missing physical lift.  CBC(C) is a sufficient construction
target, not a proved equivalence or an unconditional additive bound.

## 1. External theorem

Baggett and Yan prove that for every realizable pair of margins `(R,S)`, the
interchange graph on the full class `A(R,S)` of zero-one matrices is maximally
Hamiltonian: Hamilton-laceable in the bipartite case and Hamilton-connected
otherwise.

Primary source: [J. S. Baggett and H. Yan, *Interchange graphs of
(0,1)-matrices are maximally Hamiltonian*, arXiv:2607.13165
(2026)](https://arxiv.org/abs/2607.13165), Theorem 1.1.

The theorem applies to a **full fixed-margin class**.  Its invariant positions
are positions forced across that whole class; deleting them factors the class
into smaller full margin blocks.  It does not say that an arbitrary subset
cut out by structural zeros, residence, owner, chronology, upper-witness or
compiler constraints remains connected under the surviving squares.

## 2. Two correct conditional statements

### 2.1 Coherent token orbit

If every edge of a graph `G` is a physically legal transposition of two whole
multi-depth tokens, and every such edge remains legal after every preceding
legal sequence, then the physical orbit is exactly

\[
               \prod_{C\in\operatorname{Comp}(G)}\operatorname{Sym}(C).
\]

This is the elementary edge-transposition generation theorem plus the strong
closure hypothesis.  It correctly shows that one connected generating
skeleton is enough; pairwise commuting packets are unnecessary.

The content is entirely in physical closure.  A prospective packet menu, or
one packet which is legal in the initial chronology, does not establish it.

### 2.2 Matrix-fibre lift

Suppose the reachable chronology component maps onto one full matrix fibre
`A(R,S)`, every abstract interchange has a safe physical lift from every
chronology over its source matrix, and compiler defect is a function only of
the matrix.  Then the minimum physical defect equals the minimum defect on
the fibre.

This implication is correct.  But only **connectivity** of the interchange
graph is used to reach a minimizing matrix.  Ryser's classical interchange
connectivity already supplies that fact.  Baggett--Yan's Hamilton-connected
or Hamilton-laceable strengthening is not used by the displayed proof.

It would become relevant only if the construction needed a spanning listing,
specified path endpoints, or simultaneous routing through many matrix states.

## 3. Why the current OR state is not yet such a fibre

### 3.1 Diagonal multi-depth action

The same physical packet acts simultaneously at all depths.  The legal state
space is therefore a diagonal subset of the product of the separate
depth-margin fibres.  Separate depthwise connectivity says nothing about the
diagonal orbit.  The two-token/two-depth example in the proposed reduction is
a valid minimal counterexample.

### 3.2 Structural zeros and higher data

A candidate matrix entry can be forbidden by incumbent-owner collision,
residence, endpoint state, unavailable common core, last-witness service,
rooted topology, or the terminal cap.  These are not necessarily invariant
positions of the full margin class.  Deleting them can remove required
2-by-2 moves and split the physical state graph.

The exact packet audits make this visible:

* prospective coatom choices can be quadratic or larger before the host is
  fixed;
* after fixing a directed Hamilton target, an aligned full collar has at most
  one realization for a fixed oriented target;
* the canonical Mütze pull graph filtered to full two-rail coatom packets is
  disconnected from semilength five onward.

There is also an exact exterior obstruction to replacing the full chronology
by the rail's three prefix/suffix states.  A rotating-hole rail placed between
two rolling fans can preserve q1 palettes and exact rail residence while
destroying `floor(n^2/4)` distinct uniquely witnessed crossing upper targets.
For `n=h=Theta(sqrt(m))` this is `Theta(m)` child-local birth on one
`O(h)` protected path.  Thus the rail's constant **internal** interface does
not make complete external witness damage constant.

Thus full-margin square completeness is not currently proved and should not
be inferred from raw menu size.

### 3.3 Compiler defect is not known to factor through the matrix

`lambda_d(T)` depends on physical cell positions, exterior interval unions,
the maximal antecedent/cap, and integral target-to-cell competition.  Two
chronologies with the same compressed lower-profile matrix can have different
legal cells and different complete damage.  The equality

\[
                        \lambda_d(T)=\lambda(\phi(T))
\]

is therefore a substantive quotient theorem, not a definition already
validated by the coatom profile calculation.

There is now a literal rotating-hole counterfamily to an unqualified bounded
damage quotient.  One task insertion can leave the entire rank-`m` owner
cycle unchanged while forcing `h-1` strict-lower reference targets to lose
their unique cells in every final cap-feasible word.  Thus even `H=1` may
have `Omega(h)` complete matched damage on the natural rail source.  A
positive theorem must jointly select a diffuse host, cap and reference
matching that exclude this concentration; locality alone cannot do so.

## 4. What CBC(C) still assumes

CBC(C) is a useful sufficient lemma, but its hypotheses include the following
unproved global rows.

1. An upper-complete resident starting chronology exists in every dimension.
   Even its immediate unprotected central face contains the doubly-rainbow
   middle-levels Hamilton problem.
2. A closed physical generator graph exists, not merely a prospective packet
   catalogue.
3. Its diagonal orbit contains a chronology of compiler defect at most `C`.
   This is the terminal integral Hall/common-cap theorem.
4. The resulting state exports/regenerates through the next Pascal child.

An exhaustive proof-safe defect state must therefore include the targetwise
exterior last-witness casualty set, rather than only a bounded list of nested
ray endpoint states.

Consequently CBC(C) is not equivalent to `nu(k)<=B(k)+C`; it is one
architecture-specific sufficient route.

## 5. Calibration from the new exact results

The physical lift is plausible rather than empty.

* The rotating-hole collar has a shortest resident return rail, an explicit
  depth-`h` wreath antecedent and a constant internal upper interface.
* The full terminal plus collar has upper-surjective Hamilton completions in
  every tested true-depth case `(m,h)=(4,2),(5,2),(6,3),(7,3)`.
* Full-rotation central four-resource factors have exact Catalan-forest
  realizations through `m=8`; at `m=8` one endpoint-bearing ternary exchange
  removes the sole residual 32-cycle.

These are evidence for a closed structured subclass.  They do not prove that
the entire relevant profile space is a full matrix fibre.

## 6. The honest next lemma

The useful target exposed by the matrix language is:

> **Physical coherent square-completeness.**  Construct one upper-complete
> resident chronology and one compressed state class such that (i) every
> margin-preserving square required by a connected generator lifts to a
> bounded safe packet from every state in the class; (ii) those lifts preserve
> the class; and (iii) the terminal compiler neighbourhoods factor through a
> laminar/convex function of the compressed state, with deficiency at most a
> constant somewhere in the orbit.

If proved, classical interchange connectivity already supplies reachability;
Baggett--Yan then gives the optional stronger conclusion that the whole
abstract fibre admits endpoint-prescribed spanning traversals.

## 7. The `B+1` heuristic

At length `B+1` the scalar short-window capacity increases by `W+d+1`, while
a bounded number of local coatom packets has `O(d^2)=O(k)=o(W)` scalar
footprint.  This correctly rules out a scalar-capacity obstruction.

It does not prove `B+1`: incidence Hall deficiency, complete literal damage,
upper/topology compatibility and recursive regeneration can remain despite
arbitrarily large scalar slack.  `B+1` is therefore a credible sharpened
conjecture, not a consequence of the interchange theorem.

## 8. Exact correction: the smallest honest coherent fibre is cubic

The occurrence-labelled three-slot mixed-coatom state can now be computed
exactly.  Label the three active chain types `1,2,3`; the three prepared
slots have types `12,23,31`.  The whole-chain orientation table is a
`3 by 3` zero-one matrix with zero diagonal and unit row and column sums.
Its allowed support is

\[
                         K_{3,3}-\{11,22,33\}=C_6.
\]

There are exactly two feasible states, the two alternating perfect
matchings of this `C_6`.  No supported `2 by 2` square exists.  Their
difference is the indispensable cubic

\[
 x_{12}x_{23}x_{31}-x_{21}x_{32}x_{13}.                 \tag{8.1}
\]

The same cubic acts coherently at every depth: expanding by depth makes its
formal degree `3(d-1)`, while quotienting each complete provider chain to one
honest token contracts it back to degree three.  More generally, for the
prepared three-label family, supported quadrics and cubics form a Markov
basis; repeated slots of one pair type give `C_4` quadrics and one slot of
each of the three types gives the `C_6` cubic.  Thus the uniform degree bound
is three, not two.

This has two consequences for CBC.

1. Baggett--Yan's full-table square theorem is not the physical
   reachability theorem even on the smallest authenticated face.
2. The failure is bounded and constructive: the corrected target is a
   **closed coherent alternating-cycle atlas**, with prepared-family degree
   bounded by three independently of `d`.

An independent exhaustive replay enumerates all `2^6` supported tables,
finds the two states, proves the absence of a supported square, and recovers
the six-entry primitive difference.

## 9. Exact positive correction: one split letter absorbs one complete ray

The linear complete-damage example in Section 3.3 is a genuine obstruction
at fixed length and fixed compiler width, but it is not an additive-length
obstruction.  If an old source letter satisfies

\[
                              X=Z\cup T,
\]

replace it by the consecutive nonempty block `Z,T`.  Mapping every old
interval to the interval containing the complete replacement block is
injective and preserves its literal OR.  The genuinely new cells are the
two endpoint rays based at `Z` and `T`.

In the rotating-hole counterfamily, split

\[
                         X=\{\epsilon\}\cup\tau
             \quad\hbox{as}\quad \{\epsilon\},\tau .
\]

Every old target, owner and upper witness survives.  The task `tau` is a
singleton, while the displaced old cell and all `h-1` alleged casualties
are the new right ray.  Crossing owner deadlines rise from `h+1` to `h+2`;
their values and order do not change.  Hence one added position pays the
whole linear family by a nonflat one-unit deadline staircase.

The exact regenerative issue is now sharper.  One transition may be repaired
by a bounded number of source splits, but those split boundaries can
accumulate across dimensions.  If `Phi` is the minimum number of essential
marked boundaries, the proof-safe recurrence is only

\[
                             \Phi'\le\Phi+H
\]

without a contraction theorem.  A uniform reclaim fraction `theta>0` would
instead give

\[
                    \Phi'\le(1-\theta)\Phi+H,
\]

and hence a bounded invariant.  Thus the corrected additive route needs
both a closed bounded-degree coherent atlas and a regenerative split reset.

Files:

* `MATH_THEOREM_R_COHERENT_BIRAIL_MULTIDEPTH_MARKOV_BASIS_20260801.md`;
* `scratch/audit_coherent_birail_c6_markov_basis_20260801.py`;
* `MATH_THEOREM_H1_SPLIT_LETTER_RAY_ABSORPTION_AND_ONE_COLUMN_CRITERION_20260801.md`;
* `MATH_AUDIT_H2_SPLIT_LETTER_BLOCK_CONTRACTION_AND_TASK_HOSTING_20260801.md`.
