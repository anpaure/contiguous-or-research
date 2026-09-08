# The K16 chronological `D^4` zipper: exact local mechanism and K17 interface

Date: 2026-07-31  
Lane: L  
Status: independent finite replay PASS; corrected conditional lift interface;
no K17 construction or new upper bound

## 0. Verdict

The 49-term partial-facet substitution in the promoted K16 word has two
different matching layers.

1. The 128-edge **value containment graph** says that every bridge facet is
   contained in several omitted parent owners.  The oriented parent factor
   supplies a canonical successor-owner SDR.
2. The 96-edge **chronological graph** remembers the literal occurrence of
   each four-cell `D^3` facet window and permits only its one-cell left or
   right extension in the same word.  This graph is

   \[
                         P_8\ \dot\cup\ P_{90}.       \tag{0.1}
   \]

   It has a unique perfect matching: four right/head extensions on the
   large-component collar and 45 left/tail extensions on the opened small
   cycle.

The uniqueness is a linear-boundary phenomenon.  The small component would
give an even alternating cycle, with two perfect matchings, if its final
right extension were allowed cyclically.  In the actual linear word that
extension begins at `12869`, outside `D^4`, so one alternating edge is
absent and the cycle becomes `P_90`.

This mechanism has a clean dimension-free local form, but only on a fixed
word and an equal-size selected facet/owner bank.  It does not lift K16 to
K17 by itself.  At K17 the adjacent Pascal banks on 16 old coordinates have
unequal sizes, differing by `Cat_8=1430`, so a residual Catalan sector is
unavoidable.  Any K17 use must embed the zipper inside a larger
residence-compatible, upper-complete rethread and one common lower compiler.

## 1. Authoritative objects

The input certificates are

```text
answers/k15.word
  f35da2f0c98ec07de3e5318554157af490558e881be5c8bbcb5e3d1c8c08b14b
answers/k16.word
  890ac346ce142f5f9ed564d487ff3e2fb99aea93ae2c104ec13765fa5d3814fe
```

The primary theorem/audit chain is:

```text
MATH_THEOREM_AD_K16_LITERAL_D4_ZIPPER_AND_PHASE_JUMP_RULE_20260731.md
MATH_AUDIT_AD_K16_LITERAL_D4_ZIPPER_AND_PHASE_JUMP_RULE_20260731.md
scratch/audit_ad_k16_literal_d4_zipper_phase_rule_20260731.py
scratch/ad_k16_literal_d4_zipper_phase_rule_20260731.audit.json
```

The earlier value-level and mixed-depth inputs are:

```text
MATH_THEOREM_K16_SHIFTED_CHUNK_FACET_SUBSTITUTION_ANATOMY_20260731.md
MATH_THEOREM_K16_FACET_OWNER_RANK_EXCHANGE_20260731.md
MATH_THEOREM_K16_NONFLAT_FACET_BRIDGE_PASCAL_NORMAL_FORM_20260731.md
MATH_AUDIT_K16_D3_TWO_SHIFT_FACET_BRIDGE_AND_CONDITIONAL_EVEN_LIFT_20260731.md
```

The independent raw-word replay is

```text
scratch/audit_independent_ad_k16_literal_zipper_20260731.py
scratch/audit_independent_ad_k16_literal_zipper_20260731.json
```

Section 8 adds a second independent leaf-peeling replay written in this
lane.

## 2. Algebraic facet/owner exchange

Let

\[
 C=(V_0,V_1,\ldots,V_{s-1})
\]

be an oriented rank-`r` Johnson cycle and put

\[
                       F_i=V_i\cap V_{i+1}.          \tag{2.1}
\]

If the `F_i` are distinct, then

\[
                  F_{i-1}\cup F_i=V_i.              \tag{2.2}
\]

Indeed, the two facets are distinct rank-`r-1` subsets of `V_i` and hence
omit different coordinates.  After adjoining `z`, (2.2) becomes

\[
            (z\cup F_{i-1})\cup(z\cup F_i)=z\cup V_i.\tag{2.3}
\]

There is also the typed boundary identity

\[
                    V_i\cup(z\cup F_i)=z\cup V_i.   \tag{2.4}
\]

Thus consecutive facet-mode derivative rows reconstruct owner-mode targets
one derivative level above.  For a rooted path, an incoming facet
`V_(i-1) intersect V_i` is contained in its head owner `V_i`; for a cycle,
the successor map is a bijection.  This supplies the 49-edge canonical
matching in the coarser containment graph without invoking Hall.

That canonical containment matching is not the chronological matching on
the small component.  The physical boundary removes its final successor
extension, so the unique chronological matching uses every tail owner
instead.

## 3. Exact occurrence graph

Put

\[
 T=D^3(\texttt{answers/k15.word}),\qquad z=2^{15}.
\]

The 49 tagged rank-eight `D^3` occurrences in the child have starts

\[
 [6386,6390)\ \dot\cup\ [12825,12870),               \tag{3.1}
\]

and their omitted rank-eight parent-owner indices are

\[
 [5109,5113)\ \dot\cup\ [6390,6435).                 \tag{3.2}
\]

For a bridge occurrence `(p,F)` and an omitted owner `V`, define the
occurrence-labelled graph `Xi` by

\[
 (p,F)\sim V
 \iff
 D^4A^{16}_{p-1}=z\cup V
 \quad\hbox{or}\quad
 D^4A^{16}_{p}=z\cup V,                              \tag{3.3}
\]

with an out-of-range start unavailable.  Equivalently, an edge is an exact
five-cell interval obtained by extending the displayed four-cell core by
one cell on the labelled side.

This definition carries four essential occurrence constraints.

1. The low row is a physical occurrence, not only its facet value.
2. The extension uses the same fixed word; containment alone is insufficient
   because the added cell may introduce a contaminating coordinate.
3. Each bridge occurrence and each omitted owner is used once in the
   one-step assignment.
4. Witness intervals may overlap.  This is upper-target coverage, so there
   is no cell-capacity conflict between two matched intervals.

The perfect-matching equivalence is exact only for this fixed-word,
occurrence-bijective, one-cell-extension subclass.  Ordinary coverage could
use a longer witness or need not use every bridge occurrence.

## 4. Why the matching is unique

### 4.1 Four-row forward zipper

Number the four long-collar bridge occurrences `b_0,...,b_3` and the four
omitted owners `u_0,...,u_3=T[5109:5113]`.  Their chronological adjacency is

\[
 N(b_0)=\{u_0\},\qquad
 N(b_i)=\{u_{i-1},u_i\}\quad(1\le i\le3).            \tag{4.1}
\]

Thus the component order is

\[
 b_0,u_0,b_1,u_1,b_2,u_2,b_3,u_3,                   \tag{4.2}
\]

which is `P_8`.  Endpoint forcing gives

\[
                         b_i\longmapsto u_i,         \tag{4.3}
\]

the four right/head extensions.  Their inclusive five-cell intervals are

\[
                         [6386+i,6390+i].            \tag{4.4}
\]

The pinned cell `A16[6389]=z` lies in exactly these four depth-three cores.

### 4.2 Opened 45-cycle backward zipper

For `0<=r<45`, put

\[
 t_r=35+r\pmod {45},\qquad
 b_r=z\cup\left(T_{6390+t_r}\cap
 T_{6390+((t_r+1)\bmod45)}\right).                  \tag{4.5}
\]

Every nonterminal occurrence offers its tail owner by a left extension and
its head owner by a right extension.  The final bridge start is `12869`,
but `D^4A16` has no start `12869`; its right/head edge is therefore absent.
The alternating 90-cycle is opened to `P_90`.

Leaf forcing then chooses every tail/left edge:

\[
 b_r\longmapsto T_{6390+t_r}.                        \tag{4.6}
\]

The inclusive intervals are

\[
                         [12824+r,12828+r].          \tag{4.7}
\]

The last is the honest linear interval `[12868,12872]`; there is no cyclic
wrap.  The first left extension is the typed unmarked-owner/facet seam
(2.4), and the remaining 44 are facet/facet unions (2.3).

### 4.3 Forest proof

The full graph has 96 edges.  Both shore-degree profiles are

\[
                         1^2 2^{47}.                 \tag{4.8}
\]

Its component ledgers are `(8,7)` and `(90,89)`, with maximum degree two and
two leaves each.  Hence (0.1) holds.  In any forest, an edge incident with a
leaf is forced in every perfect matching; recursively deleting the leaf and
its mate recovers the displayed 49 edges and proves uniqueness.

More generally, uniqueness of a proposed matching is equivalent to absence
of an alternating cycle.  A balanced forest with a perfect matching is a
particularly transparent sufficient interface for recursion.

## 5. Adjacent-row deck exchange

The exact selected first-band ledger is:

\[
\begin{array}{c|ccc}
\text{target bank}&\text{ordinary row}&\text{bridge row}&\text{boundary repeat}\\ \hline
z+\binom{[15]}7&D^2:6388&D^3:49&2,\\
z+\binom{[15]}8&D^3:6386&D^4:50&1.
\end{array}                                               \tag{5.1}
\]

For the selected partition, remove the two bridge values from the `D^2`
side.  This leaves `6386+49=6435` distinct marked rank-eight targets.  On
the upper row, the chronological matching uses the 49 omitted owners only;
they are disjoint from the 6386 high `D^3` owners.  The 50th marked `D^4`
owner is `T[5108]`, already present in `D^3`, and is a boundary repetition,
not a demand vertex of `Xi`.

The untagged sides independently satisfy

\[
 \{\text{rank-eight plain }D^3\}=\binom{[15]}8,
 \qquad
 \{\text{rank-nine plain }D^4\}=\binom{[15]}9.      \tag{5.2}
\]

The second equality is coverage by 6434 occurrences with 5005 distinct
values, not an occurrence bijection.  Together (5.1)--(5.2) are an exact
cover of the child ranks eight and nine.  They are not a deeper-shadow or
lower-compiler theorem.

## 6. Phase and shift arithmetic

The parent components are strict `Z_15` spirals of base lengths 426 and 3
and common sheet voltage `g=4`.  The observed clean displacement is `s=3`.
The phase equation

\[
                         4\tau\equiv3\pmod {15}      \tag{6.1}
\]

has the unique solution `tau=12`.  Cutting before that sheet gives chunk
lengths

\[
 (15-12)426=1278,\quad12\cdot426=5112,
\]

\[
 (15-12)3=9,\quad12\cdot3=36.                       \tag{6.2}
\]

The actual parent starts of the four plain chunks are

\[
                         5112,0,6426,6390,            \tag{6.3}
\]

whereas their affine shifts relative to the continuing output index are

\[
                         5112,5157,36,6426.           \tag{6.4}
\]

These must not be conflated.  On the high tagged large-component rail the
two affine shifts are 5113 and 5158; their difference 45 is exactly the mass
of the skipped small component.

For a general `q`-sheet spiral, the congruence

\[
                         g\tau\equiv s\pmod q         \tag{6.5}
\]

has a solution exactly when `gcd(g,q)` divides `s`, and then has
`gcd(g,q)` solutions modulo `q`.  It is unique only when `gcd(g,q)=1`.
This qualification is required in the generic phase lemma; K16 satisfies it.

The fixture identity

\[
                         49=45+(3+1)                  \tag{6.6}
\]

has two sources: the reserved component mass 45 and the four depth-three
windows through the interior singleton.  The reusable count is `S+c`, not a
theorem that every future collar has size `d+1`.

## 7. Exact hypotheses for a K17 use

### 7.1 What is dimension-free

The following local facts do lift unchanged.

1. A directed lower-rainbow Johnson path/cycle has distinct facets and the
   algebraic head/tail identities (2.2)--(2.4).
2. On a fixed word, one-cell bridge repair is exactly perfect matching in
   the occurrence graph (3.3).
3. If that graph is a balanced forest, its matching is unique and
   leaf-peelable.  A path zipper is forced forward when its first tail offer
   is outside the demand bank; a cycle zipper is forced backward when one
   final head offer is removed by a declared linear opening.
4. A common spiral phase exists under the congruence condition (6.5), with
   uniqueness only in the coprime case.

### 7.2 What does not transfer verbatim

The balanced K15-to-K16 slot exchange uses

\[
 {15\choose8}={15\choose7}=6435.                    \tag{7.1}
\]

For a one-coordinate K16-to-K17 Pascal split, the corresponding old banks
are unequal:

\[
 {16\choose8}=12870,\qquad {16\choose9}=11440,
 \qquad12870-11440=1430=\operatorname{Cat}_8.       \tag{7.2}
\]

Therefore an equal-size global facet/owner zipper cannot cover the K17
middle layer by itself.  One needs a Catalan residual sector or a
boundary-deficient rail carrying those 1430 unmatched facet slots.  This is
the same structural residue exposed by the current four-sector K15-to-K17
factor, not a numerical nuisance.

There is a second nontransfer.  The displayed K16 `D^3` row is a two-rank
diagnostic; the authenticated K16 middle chronology uses the variable
staircase, with shallow rows served one derivative level earlier.  It cannot
be treated as a flat parent carrier for K17.  A one-step K16-to-K17 lift must
export the actual scheduled row/cap relation, while the current four-sector
K17 factor instead starts directly from K15 and two new coordinates.

### 7.3 Sufficient K17 module interface

A K17 construction may use the K16 zipper mechanism as a local module if it
supplies all of the following jointly.

1. **Rank-correct parent factor.**  A selected K16 or K15-derived owner
   factor with globally distinct relevant edge facets and an explicit
   Catalan residual bank accounting for (7.2).
2. **Occurrence realization.**  One physical K17 word realizes every
   selected low core at the required derivative depth.  The associated
   left/right extension graph has a perfect matching; for deterministic
   leaf-peel transfer, require a balanced forest.  More generally, uniqueness
   relative to a chosen perfect matching is equivalent to the absence of an
   alternating cycle.
3. **Local openings.**  Every complete cyclic zipper not placed at the one
   global word endpoint has its own typed seam/opening which removes one
   alternating extension edge.  The single K16 terminal boundary cannot be
   reused simultaneously by many K17 cycles.
4. **Phase compatibility.**  All selected components solve one common phase
   equation, including the exact side/orientation of their zipper matching.
5. **First-band balance.**  The marked/unmarked Pascal decks, including the
   Catalan residual sector, cover the desired K17 adjacent ranks as literal
   occurrences.  Value containment is not enough.
6. **Residence and deeper flags.**  The resulting order passes the exact
   run/event transducer and protects every deeper upper target across all
   new cuts.
7. **Common compiler.**  The same chronology admits one integral
   maximal-common-cap lower assignment.  Marginal Hall for the zipper does
   not imply this row.
8. **Linear endpoints.**  No cyclic `D^(d+1)` witness is used, and the two
   global endpoint collars are exported explicitly.

For the currently frozen direct K15-to-K17 four-sector factor, an additional
finite obstruction is already known: its direct formulas have 60 forced
upper-q1 occurrence conflicts, so any Hamilton repair needs at least 60
external rank-ten edges and at least 61 old-edge deletions.  A zipper-based
K17 proposal must therefore be part of that global rethread (or change the
sector formulas upstream); it cannot be appended as a small preservation
patch to the unmodified factor.

These hypotheses are sufficient as an interface, not proved to exist in all
dimensions.

## 8. Independent replay

This lane's independent script is

```text
scratch/audit_l_k16_chronological_d4_zipper_independent_20260731.py
```

It derives the bridge starts and omitted owner bank from the two answer
words, reconstructs the 128-edge containment graph and 96-edge chronological
graph, proves the `P_8 + P_90` decomposition, leaf-peels the unique matching,
checks every inclusive five-cell interval, verifies the adjacent-row deck
exchange, and checks the phase congruence and chunk arithmetic.  It writes

```text
scratch/l_k16_chronological_d4_zipper_independent_20260731.audit.json
```

No search or solver is used.
