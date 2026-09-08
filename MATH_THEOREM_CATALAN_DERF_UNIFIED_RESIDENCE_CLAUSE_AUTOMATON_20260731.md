# All minimum-three DERF residence constraints form one cubic selected-edge CNF

Date: 2026-07-31  
Status: exact all-parameter equivalence, including collar seams and short
trace blocks; independent replay on the strict (n=3,4,5) outputs. No
simultaneous all-parameter solution with the other construction rows is
claimed.

## 0. Result

The body clauses of the companion residence-motif theorem and the collar
boundary automaton are not separate species. At minimum-positive-run three
they are one selected-edge condition.

Let ({\cal E}) be an occurrence-labelled candidate physical edge bank and
let (lambda_e) be the Boolean literal saying that edge occurrence (e)
is present. For every candidate three-edge path

\[
              e_0e_1e_2:\quad v_0-v_1-v_2-v_3           \tag{0.1}
\]

with a nonempty set

\[
              (v_1\cap v_2)\setminus(v_0\cup v_3),       \tag{0.2}
\]

add the clause

\[
              \neg\lambda_{e_0}\vee
              \neg\lambda_{e_1}\vee
              \neg\lambda_{e_2}.                        \tag{0.3}
\]

Assume the selected support is a path forest and its edge-intersection
colours are injective. Then it has no internal positive run of length below
three if and only if it satisfies every clause (0.3).

This includes paths which cross one or two sector seams and paths whose
intermediate trace blocks have only one or two vertices. No special
short-block exception is needed.

## 1. Exact selector dictionary for the strict lift

For a strict direct-edgewise lift, use the following edge literals.

\[
\begin{array}{c|c}
\text{candidate physical edge}&\lambda_e\\ \hline
\text{untouched child edge in the }c\text{-sector}&1\\
\text{child edge }q\text{ in the punctured }z\text{-sector}&\neg q\\
\text{upper direct occurrence }o&s_o^-\\
\text{lower direct occurrence }o&s_o^+\\
\text{either collar seam belonging to }q&q.
\end{array}                                             \tag{1.1}
\]

After substituting (1.1), (0.3) is a clause of width at most three in the
common-basis and side-occurrence variables. Repeated literals may make it
shorter. In particular:

* triples wholly in (z) give the positive hitting clauses on (Q);
* triples wholly in a side give the negative side-occurrence clauses;
* triples meeting collar seams give mixed-sign clauses; and
* a bad triple wholly in (c) gives the empty clause, because all three
  of its edges are forced.

The last case is the exact algebraic form of the next-depth regeneration
obstruction.

## 2. Equivalence and streaming automaton

### Theorem 2.1 (unified selected-edge residence criterion)

Under path-forest and intersection-palette injectivity, (0.3) is necessary
and sufficient for minimum-three residence on every selected component.

#### Proof

Intersection-palette injectivity excludes an internal positive singleton
run. By the exact `0110` lemma, an internal run of length two occurs
precisely on a selected three-edge path satisfying (0.2). Such a path
violates (0.3). Conversely every violated clause selects the complete bad
path and hence creates that run. \(\square\)

### Corollary 2.2 (two-edge deterministic state)

Orient a partial selected path. For a directed Johnson edge (e), write
(a(e),b(e)) for its deletion and insertion coordinates. The exact
streaming state is the last two directed edges. Appending (g) after
(e,f) is legal exactly when

\[
                            b(e)\ne a(g).               \tag{2.1}
\]

Thus joining two body-safe protected fragments requires scanning only the
first two new edges; after that, their internally verified state takes
over. If a fragment is shorter, the same two-edge state naturally spans
several seams. This is the minimum-three protected boundary automaton.

#### Proof

The only newly completed three-edge window after appending (g) is
((e,f,g)). Apply the `0110` lemma. \(\square\)

The automaton is equally valid for a later transparent endpoint-routing
forest: connector edges are simply additional candidate occurrences with
their own selector literals. The residence part of that routing theorem
therefore remains local. Deep-shadow and compiler ownership do not follow
from this automaton.

## 3. Exact replay on the strict chain

For the three retained outputs, the bad selected windows split as follows.

\[
\begin{array}{c|r|r|r|r|r}
n&\text{total}&\text{inside one sector}&
 \text{meeting a boundary/seam}&\text{one transition}&\text{two transitions}\\ \hline
3&17&5&12&1&11\\
4&44&17&27&8&19\\
5&144&57&87&36&51.
\end{array}                                             \tag{3.1}
\]

No bad three-edge window has three sector transitions. This is a property
of the four-sector collar incidence pattern, not an assumption in Theorem
2.1.

At the first step, the five within-sector clauses are forced contradictions
on the copied (c)-rail. Even if a different (Q) or different side SDRs
removed all twelve seam clauses, the fixed child copy would still fail.
The authenticated cut intervals and their minimum three-cut stabbing set
are recorded in the companion local-clause theorem.

## 4. General guard width

For a required positive-run threshold (h), replace (0.2) by all binary
window motifs

\[
                            0\,1^r\,0,\qquad 1\le r<h.   \tag{4.1}
\]

Each motif is a selected path of (r+1) edges and gives one clause of that
width. A streaming implementation stores the last (h-1) edge changes,
or equivalently the capped coordinate suffix-run state. The
intersection-palette argument removes the (r=1) family in the Catalan
trace setting.

This is a finite-width local system for each dimension. Because the
deadline threshold grows without bound while the (c)-rail is copied
unchanged, the strict recursion cannot export a forever sealed child body.
It must regenerate or rethread the child rail at depth jumps.

## 5. Remaining quantifier

Residence itself no longer requires a separate global theorem. The open
statement is simultaneous feasibility:

> choose or regenerate the child rail at the output threshold, choose the
> strict synchronized common basis and both direct side SDRs, satisfy the
> unified motif CNF (0.3), keep the physical support acyclic and
> anchor-capped, and use the same connector choices for the private
> deep-shadow witnesses and exact compiler relation.

The unified CNF is local and low-width, but low width does not imply it is
compatible with the two matching systems or the compiler. The present
theorem closes the residence characterization, not that joint integral
quantifier.

## 6. Audit

The standard-library script

```text
scratch/audit_catalan_derf_unified_residence_automaton_20260731.py
```

authenticates the recursive witness, verifies the complete ambient lower
palette is injective, scans every four-vertex window, checks (0.2) against
the two-edge automaton and writes

```text
scratch/catalan_derf_unified_residence_automaton_20260731.audit.json
```

It independently reproduces (3.1). No solver result or all-parameter
feasibility assertion is used.
