# A decorable `ML(7)` cycle and the exact hexagon-transfer invariant

Date: 2026-07-31  
Status: explicit positive `m=4` theorem; exact local preservation criterion;
complete finite census around the displayed `m=2,3,4` fixtures; scoped
warning against freezing an arbitrary alternating SDR through a Middle
Levels gluing recursion

## 0. Verdict

The first counterexample in
`MATH_THEOREM_CATALAN_ALTERNATING_TURN_SDR_HALL_AND_M4_COUNTEREXAMPLE_20260731.md`
does **not** indicate nonexistence at `m=4`.  One ordinary Boolean-incidence
hexagon toggle changes that counterexample into a Hamilton cycle of
`ML(7)` admitting a Catalan decoration.  The resulting diamond lift is a
spanning `Cat_4=14`-path forest.

The same calculation identifies the right recursive state.  A gluing
hexagon preserves a *fixed* decoration if and only if two finite conditions
hold:

1. the selected turn-colour palettes on the six hexagon vertices are
   unchanged, separately on the two shores; and
2. the three path fragments created by deleting the old hexagon matching
   have alternating marked boundary types after the new matching reconnects
   them.

This is an exact six-port transfer rule.  It is stronger than preserving the
two turn surjections and weaker than recomputing the full gap--Hall problem.

The finite `m=4` census also gives a genuine qualification.  Of the sixteen
hexagon toggles which carry the displayed Hamilton cycle to another Hamilton
cycle, only six admit a decoration common to both cycles.  Four further
outputs are decorable only after changing the representatives, and six are
not decorable.  Thus a recursive proof may carry a **feasible-decoration
relation** or a tree of transparent hexagons, but it may not freeze an
arbitrary SDR and assume that the standard Middle Levels gluing operation
preserves it.

## 1. Turn colours and decorations

Fix (m\ge2), put \(\Omega=[2m-1]\), and write a Hamilton cycle of the
middle-levels graph as

\[
 C=A_0,B_0,A_1,B_1,\ldots,A_{Q-1},B_{Q-1},A_0,
 \qquad A_i\subset B_i\supset A_{i+1},
 \tag{1.1}
\]

where

\[
 Q=\binom{2m-1}{m-1}.
\]

It is useful to define the turn colour at a vertex without choosing an
index.  If (v\in\binom\Omega{m-1}) has its two neighbours (x,y) in
(C), put

\[
                    \tau_C(v)=x\cup y\in\binom\Omega{m+1}.
\tag{1.2}
\]

If (v\in\binom\Omega m), put

\[
                    \tau_C(v)=x\cap y\in\binom\Omega{m-2}.
\tag{1.3}
\]

A decoration is equivalently a pair of selected vertex sets

\[
 D_A\subseteq\binom\Omega{m-1},\qquad
 D_B\subseteq\binom\Omega m                         \tag{1.4}
\]

such that:

* the colours \(\tau_C(D_A)\) are the rank-((m+1)) sets, each once;
* the colours \(\tau_C(D_B)\) are the rank-((m-2)) sets, each once; and
* after unselected vertices are deleted from the cyclic word (C), the
  selected vertices alternate between (D_A) and (D_B).

This is the vertex form of the two turn transversals plus the alternating
occurrence SDR in the companion trace theorem.

## 2. The exact transparent-hexagon lemma

Let (H\in\binom\Omega{m-2}), and choose distinct (a,b,c\notin H).  Put

\[
 L_a=H+a,\quad L_b=H+b,\quad L_c=H+c,
\tag{2.1}
\]

\[
 U_{ab}=H+a+b,\quad U_{bc}=H+b+c,\quad U_{ca}=H+c+a.
\tag{2.2}
\]

These six vertices span the standard Boolean-incidence hexagon (Z).  Its
two alternating matchings are

\[
 M_0=\{L_aU_{ab},L_bU_{bc},L_cU_{ca}\},              \tag{2.3}
\]

\[
 M_1=\{L_aU_{ca},L_bU_{ab},L_cU_{bc}\}.              \tag{2.4}
\]

Assume (C\cap Z=M_0), and assume

\[
                         C'=C\mathbin\triangle Z       \tag{2.5}
\]

is again a Hamilton cycle.  Deleting (M_0) from (C) leaves three paths.
The matching (M_1) reconnects the same six path ports in the other cyclic
order.

The same definitions apply componentwise to a two-factor: selected turn
colours are required to be globally bijective, while selected shore types
alternate on every factor cycle.  A hexagon toggle may then merge or split
components.  Deleting its old matching still leaves at most three relevant
path fragments, and the boundary test below is imposed on every new cyclic
component.  The proof is identical.  The Hamilton-to-Hamilton formulation is
used first because it is the exact finite fibre audited in Sections 3--4.

### Theorem 2.1 (transparent-hexagon criterion)

Let (D=(D_A,D_B)) be a decoration of (C).  The same selected vertex sets
form a decoration of (C') if and only if both of the following hold.  In
the componentwise two-factor version, replace "a decoration" by the
componentwise condition in the preceding paragraph.

**Palette condition.**  Separately on the two shores,

\[
 \{\!\{\tau_C(v):v\in D_A\cap V(Z)\}\!\}
 =
 \{\!\{\tau_{C'}(v):v\in D_A\cap V(Z)\}\!\},       \tag{2.6}
\]

\[
 \{\!\{\tau_C(v):v\in D_B\cap V(Z)\}\!\}
 =
 \{\!\{\tau_{C'}(v):v\in D_B\cap V(Z)\}\!\}.     \tag{2.7}
\]

**Boundary-alternation condition.**  Orient the three retained paths as they
are traversed in (C').  On each nonempty selected subsequence record only
the shore type of its first and last selected vertices.  Delete fragments
whose selected subsequence is empty.  In the resulting cyclic list of
nonempty fragment subsequences, the last recorded type of each fragment and
the first recorded type of the next are opposite.

#### Proof

Only the neighbour pairs at the six vertices of (Z) change under (2.5).
Every selected turn colour outside (Z) is therefore unchanged.  Because
the old selected colours are a bijection onto the whole alphabet, the new
selected colours are again a bijection exactly when the missing local
multiset is restored.  This proves (2.6)--(2.7).

Inside a retained path, reversal changes the order of the selected shore
types but preserves their alternation.  Thus the only possible new failures
of cyclic alternation occur at the three new seams.  They are absent exactly
under the displayed boundary test.  This proves necessity and sufficiency.
\(\square\)

The theorem is genuinely local: it stores two turn-colour multisets and at
most two boundary bits per retained fragment.  Two useful extreme cases are:

* if (D\cap V(Z)=\varnothing), the palette condition is automatic;
* if (V(Z)\subseteq D), it is just equality of the three local turn
  colours on each shore.

The boundary condition remains necessary in both cases.  In particular,
being disjoint from the selected marks is not by itself a gluing theorem.

### Corollary 2.2 (protected linearity; Hamilton-to-Hamilton form)

If the common mark trace has, on a retained portion disjoint from the six
ports, either an unmarked run of length at least four or an even marked run,
then the physical lift is a linear forest on both sides of a
Hamilton-to-Hamilton toggle.  For a componentwise toggle which may split a
factor cycle, the same conclusion requires such a protected breaker on every
output component (or the exact trace-face test separately on every output
component).

This is the binary-trace criterion: the protected run prevents the unique
cycle face

\[
 \text{all positive zero-runs have length }2,
 \qquad\text{all one-runs are odd}.                  \tag{2.8}
\]

For an induction one may store the weaker exact post-toggle bit “outside the
cycle face” instead of a protected literal run.

### Theorem 2.3 (exact leaf-peelable transfer test)

Assume the decoration of (C) is leaf-peelable, with gap--colour forest
(\Gamma), and that Theorem 2.1 preserves the decoration on (C').  Let

\[
 D=E(\Gamma)\setminus E(\Gamma'),\qquad
 S=E(\Gamma')\setminus E(\Gamma),                    \tag{2.9}
\]

where a gap vertex is an occurrence-labelled oriented cyclic gap between
selected (A)-vertices.  Its unordered endpoint pair is only shorthand and
need not identify it uniquely: two opposite gaps may have the same pair.
Delete (D), contract every component of
(\Gamma-D), and retain every new gap vertex appearing in (S).  Then the
decoration of (C') is leaf-peelable if and only if the attachment
multigraph induced by (S) on these contracted vertices is loopless and
acyclic.

Only the three old and three new seam-crossing gaps and the three lower-turn
values at the upper-shore hexagon vertices can change.  All internal gaps of
the three retained fragments are literal copies.  Thus (2.9) is another
finite boundary transfer test.  Here ``finite'' refers to the number of
changed gap objects.  A seam-crossing gap may still carry a
dimension-growing number of colour occurrences, so this statement alone is
not a dimension-independent bounded-state theorem.

#### Proof

The edge identity

\[
                    \Gamma'=(\Gamma-D)+S             \tag{2.10}
\]

is tautological.  Since (\Gamma-D) is a forest, adding (S) creates no
cycle exactly when each new edge joins two distinct current components and
the component-level attachment graph has no cycle.  This is precisely the
stated loopless-forest condition.  The preserved decoration already gives a
perfect matching of (\Gamma'); when (\Gamma') is a forest that perfect
matching is unique and is recovered by leaf peeling. \(\square\)

Theorem 2.3 is necessary: palette transparency by itself does not preserve
gap acyclicity.  Section 4 gives the smallest possible failure, one new
four-cycle.

## 3. One hexagon repairs the explicit `m=4` counterexample

Use bitmasks on ([7]=\{0,\ldots,6\}).  Start with the Hamilton cycle

```text
7 23 19 51 49 57 56 60 52 53 21 29 13 15 11 43 35 99
97 113 112 120 104 108 44 45 41 105 73 75 67 71 69 77
76 92 28 30 14 46 42 106 98 114 50 58 26 27 25 89 88 90
74 78 70 102 38 54 22 86 82 83 81 85 84 116 100 101 37 39
```

from the gap--Hall counterexample.  Take

\[
 H=33=\{0,5\},\qquad (a,b,c)=(3,4,6).                \tag{3.1}
\]

The six hexagon vertices are

\[
              41,49,97\quad\hbox{and}\quad57,113,105. \tag{3.2}
\]

The toggle replaces

\[
        (41,105),(49,57),(97,113)                    \tag{3.3}
\]

by

\[
        (41,57),(49,113),(97,105).                   \tag{3.4}
\]

The resulting Hamilton cycle is

```text
7 23 19 51 49 113 112 120 104 108 44 45 41 57 56 60 52 53
21 29 13 15 11 43 35 99 97 105 73 75 67 71 69 77 76 92
28 30 14 46 42 106 98 114 50 58 26 27 25 89 88 90 74 78
70 102 38 54 22 86 82 83 81 85 84 116 100 101 37 39
```

Starting with the first rank-three vertex, choose

\[
\begin{split}
 I={}&\{1,2,3,4,5,9,10,11,13,15,17,19,20,21,23,24,26,28,30,32,34\},\\
 J={}&\{0,1,2,3,4,8,9,10,12,13,16,17,19,20,22,23,25,26,28,30,33\}.
\end{split}                                           \tag{3.5}
\]

Direct substitution proves that (I) selects every rank-five turn colour
once, (J) selects every rank-two turn colour once, and their 42 marked
positions alternate by shore.  The mark trace has one zero-run of length
six, so its physical diamond lift is a spanning fourteen-path forest.

This is an explicit positive `m=4` result, not merely a solver status.

## 4. What the small cases say

The exact statistics of the displayed fixtures are:

| (m) | (Q) | (P) | lower turn multiplicities | upper turn multiplicities | gap lengths | gap degrees | colour degrees |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 2 | 3 | 1 | (3^1) | (3^1) | (3^1) | (1^1) | (1^1) |
| 3 | 10 | 5 | (2^5) | (2^5) | (1^1 2^3 3^1) | (1^1 2^4) | (1^1 2^4) |
| 4 | 35 | 21 | (1^9 2^{10}3^2) | (1^{10}2^9 3^1 4^1) | (1^9 2^{11}4^1) | (1^{12}2^8 3^1) | (1^{11}2^{10}) |

Thus the positive `m=4` gap--Hall graph is extremely sparse: every colour
meets at most two gaps, and all but one gap sees at most two colours.  Its
perfect matching is not a consequence of regularity; it is a nearly forced
one-dimensional matching.

There is a sharper common pattern.  In all three displayed positive cases
the gap--colour graph is a forest and its perfect matching is unique.  The
component profiles `(gaps,colours,edges)` are

\[
\begin{array}{c|c}
m&\text{component profiles}\\ \hline
2&(1,1,1),\\
3&(5,5,9),\\
4&6(1,1,1)+(2,2,3)+3(3,3,5)+(4,4,7).
\end{array}                                           \tag{4.1}
\]

Every one of the 1,728 decoration vertex sets of the repaired `m=4` cycle
has this forest/unique-matching property, not only the displayed choice.
Call such a decoration **leaf-peelable**.  For a leaf-peelable decoration,
the lower occurrence SDR is recovered deterministically by deleting leaves;
the full exponential Hall family has disappeared from the certificate.

At `m=3`, the displayed positive cycle has five alternating hexagons, but
every toggle splits it into two components.  Read in reverse, each is a
valid standard gluing operation which merges a two-cycle factor to the
decorated Hamilton cycle.  At `m=4`, the positive cycle has 31 alternating
hexagons:

\[
16\text{ produce one cycle},\qquad
11\text{ produce two},\qquad
 4\text{ produce three}.                             \tag{4.2}
\]

Ten of the sixteen Hamilton outputs are decorable.  Exhausting all 6,144
upper transversals of the displayed cycle gives exactly 1,728 distinct
decoration vertex-set pairs.  Exactly six Hamilton toggles admit a
decoration common to both sides.  Their common-decoration counts are

\[
                      576,576,144,144,432,540.        \tag{4.3}
\]

All common decorations give linear forests on both sides.  On four of the
six transparent toggles every hexagon vertex is marked; on the other two no
hexagon vertex is marked.  The exact transparent hexagons are:

\[
\begin{array}{c|c|c|c}
H&(a,b,c)&\#\text{ common decorations}&|D\cap V(Z)|\\ \hline
10 &(0,2,4)&576&6\\
34 &(2,3,4)&576&6\\
66 &(0,3,4)&144&6\\
20 &(1,3,5)&144&0\\
20 &(3,5,6)&432&0\\
96 &(0,1,4)&540&6
\end{array}                                           \tag{4.4}
\]

The leaf-peelable invariant is also robust in this neighbourhood.  In five
of the six transparent rows, every common decoration is leaf-peelable on
both sides.  In the remaining row `H=66,(a,b,c)=(0,3,4)`, exactly 72 of its
144 common decorations are leaf-peelable on both sides.  Thus each of the
six transparent Hamilton rethreadings has at least one common
leaf-peelable/linear decoration.

It is **not automatic**.  For the transparent toggle

\[
 H=66=\{1,6\},\qquad(a,b,c)=(0,3,4),                 \tag{4.5}
\]

72 common decorations remain leaf-peelable and 72 do not.  In the first
audited failure, the new boundary gap with endpoints \(\{67,100\}\) sees
both lower colours 65 and 68.  The unchanged gap with endpoints
\(\{67,76\}\) already sees both colours.  Consequently the new gap graph
contains the literal four-cycle

\[
 \{67,100\}-65-\{67,76\}-68-\{67,100\}.              \tag{4.6}
\]

Its unique cyclic component has profile `(7,7,14)`, and the whole gap graph
has two perfect matchings instead of one.  Both turn palettes, occurrence
alternation and physical linearity nevertheless survive.  This is an exact
counterexample to “transparent hexagon implies leaf-peelable.”  Theorem 2.3
is the missing local clause.

Of the remaining ten Hamilton toggles, four become decorable only after a
different representative choice and six fail the decoration gate entirely.

## 5. The recursive invariant suggested by the calculation

The correct sufficient recursive object is a **decorated gluing state**:

1. a middle-levels factor together with selected occurrences realizing the
   two turn palettes exactly once;
2. for each retained path fragment, the first and last marked shore types;
3. a protected binary-trace breaker, or equivalently the exact cycle-face
   bit of the trace; and
4. a dynamically valid spanning family of gluing hexagons satisfying the
   palette and boundary tests of Theorem 2.1 at the moment they are used.

The small-case evidence supports adding a fifth, stronger state bit:

5. the gap--colour graph is a balanced forest with its leaf-peeling perfect
   matching.

This extra condition is not needed for Proposition 5.1, but it converts the
alternating occurrence SDR from a Hall problem into a deterministic
recursion.  It is propagated exactly by Theorem 2.3.  The `m=4` census proves
that transparent Hamilton rethreadings compatible with this stronger state
exist; it does not by itself exhibit a component-merging transparent edge or
prove that a spanning transparent gluing tree always exists.  A separate
standard-factor fixture in
`MATH_THEOREM_CATALAN_LEAF_PEELABLE_TRANSPARENT_GLUING_STATE_20260731.md`
supplies a genuine transparent component merge at `m=4`.  These are two
different certificates and must not be silently identified.

### Proposition 5.1 (transparent gluing-tree implication)

Suppose a standard recursive Middle Levels factor in dimension (2m-1)
admits a sequence of compatible hexagon toggles which:

* merges all of its components into one Hamilton cycle;
* starts with a componentwise Catalan decoration: globally bijective selected
  lower and upper turn palettes, alternating selected shore types on every
  factor component, and the corresponding selected-occurrence matching;
* is transparent in the sense of Theorem 2.1 at every step; and
* retains a protected trace breaker.

Then the final Hamilton cycle has a Catalan decoration whose physical lift
is a spanning \(\operatorname {Cat}_m\)-path forest with exact lower and
upper diamond palettes.

#### Proof

Induct over the toggles.  Theorem 2.1 preserves the selected palettes and
alternation, while the protected breaker and the binary-trace theorem
preserve linearity.  The component-merging hypothesis gives the final
Hamilton cycle.  The decorated-cycle/perfect-diamond equivalence then gives
the claimed forest and palettes. \(\square\)

### Corollary 5.2 (leaf-peelable transparent gluing tree)

Under the hypotheses of Proposition 5.1, suppose additionally that the
initial componentwise gap--colour graph is a forest with its displayed
perfect matching and every toggle passes Theorem 2.3.  Then the final
Hamilton cycle has a leaf-peelable Catalan decoration.

This is immediate by induction from the exact edge exchange
\(\Gamma'=(\Gamma-D)+S\).  It is the strongest recursive invariant proved
here: both turn palettes, alternating representatives, physical linearity,
and uniqueness of the gap matching propagate by finite local transfer
tests.

This proposition is a precise target, not yet an all-(m) construction.
The finite census proves both sides of the strategic diagnosis:

* fixed-decoration transparent rethreadings really exist and already repair
  the first `m=4` obstruction, while the separate standard-factor fixture
  cited above supplies the component-merging base;
* transparency is not automatic, even among Hamilton-preserving toggles.

Therefore the promising induction **within the stronger transparent lane**
is recursive joint alternating-SDR plus a transparent gluing tree, not two
separate rainbows, and not “freeze one arbitrary SDR before applying the
published gluing tree.”  An exact dynamic program may carry the finite
endpoint/palette transfer relation of Theorem 2.1 over the plane-tree
gluing recursion.  What remains unproved is that this relation always has an
accepting root.

At the **globally prepared-palette** level, the remaining gluing statement
in this lane is:

> **Leaf-peelable transparent gluing-tree theorem.**  For every (m\ge2),
> one standard recursive middle-levels factor admits global exact lower and
> upper turn representatives, a componentwise gap forest, a protected trace
> breaker, and a dynamically compatible component-spanning family of
> incidence hexagons satisfying Theorems 2.1 and 2.3.

That theorem would imply the Catalan linear-forest object for every (m).
It would not by itself discharge the later endpoint-connector/primitive-
voltage gate or the final low-layer compiler, so it is a precise construction
theorem rather than a claim that the whole \(\nu(k)=B(k)\) conjecture has
already been proved.

It is not the minimal central existential target.  The corrected
Decorated Middle Levels 2-Factor Theorem only asks for one spanning factor
with globally exact turn palettes and componentwise alternating marks, with
no wholly marked component and no partially marked component on the mixed
cycle face.  It permits representative reoptimization and unmarked factor
components, and requires no Hamiltonization or gluing tree.  Thus the exact
hierarchy is

\[
 \text{transparent joint-SDR gluing tree}
 \Longrightarrow \text{decorated Hamilton cycle}
 \Longrightarrow \text{accepting decorated 2-factor}
 \Longrightarrow \text{Catalan linear matching}.
\]

The m=5 calculation shows that this is only the gluing half of a uniform
recursion.  A standard factor may first require one atomic correlated repair
packet whose intermediate states are not decorated.  The current all-m
target **in this repair-first recursive lane** is therefore the uniform
repaired transparent macro lemma:
repair to an accepting joint decoration at a macro boundary, then apply a
transparent leaf-preserving component-spanning gluing tree.

## 6. Audit

Run

```text
python3 scratch/audit_decorable_ml7_gluing_20260731.py
```

The dependency-free audit:

* verifies the one-hexagon identity (3.3)--(3.4);
* verifies the displayed `ML(7)` Hamilton cycle and decoration literally;
* reconstructs the gap graph and physical forest flag;
* checks the `m=2` and `m=3` comparison fixtures;
* enumerates every literal incidence hexagon at the three fixtures;
* enumerates all 6,144 upper SDRs and all 1,728 decoration vertex-set pairs
  at `m=4`; and
* checks every common-decoration count in (4.3)--(4.4), including linearity
  and the leaf-peelable gap-forest invariant on both sides.

The independent producer

```text
python3 scratch/search_decorable_ml7_20260731.py
```

uses an unrelated exact six-state-per-vertex 2-factor CNF with lazy subtour
cuts and found another decorable `ML(7)` cycle after six models.  It is
corroboration only; the theorem above is proved by the displayed finite
certificate and the audit.
