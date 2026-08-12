# Audit of the endpoint-bearing path-bank absorber interface

Date: 2026-08-01  
Lane: AD / central four-resource cycle absorption  
Status: exact central theorem and exact interface audit.  No claim about a
literal contiguous-OR word is made.

## 0. Verdict

There is an exact positive replacement for the cycle-internal no-go, but it
has a sharper hypothesis than “a protected cycle plus a fixed-H q1
extension.”

One protected cycle edge and **two edges in two distinct directed path
components** support the ternary Boolean-hex exchange.  After adjoining the
shortest resident return rail, the exchange

\[
 \{AB,CD,EF\}\longrightarrow\{AF,CB,ED\}                 \tag{0.1}
\]

preserves the lower palette, upper palette, typed tail bank and typed head
bank exactly, preserves every physical indegree and outdegree, and replaces
one directed cycle plus two directed paths by two directed paths.  Thus it
is an endpoint-bearing, path-bank-regenerative cycle absorber.  Two old
path atoms are support-minimal in the ordered Boolean-diamond host.

For a residence threshold `h+1`, one collared plus phase contains `h+5`
directed owner atoms.  Its lower-owner incidence lift therefore contains
exactly

\[
                         2(h+5)                           \tag{0.2}
\]

Middle Levels incidence edges and has maximum degree two.  Hence `H`
pairwise incidence-disjoint plus collars are covered by the fixed-H
two-factor extension theorem whenever

\[
                         2H(h+5)\le m-2.                  \tag{0.3}
\]

This is the exact part that composes.

What does **not** compose automatically is equally important.  The
fixed-H theorem gives an undirected q1 two-factor on `[2m-1]`; it does not
give a directed orientation compatible with several prescribed paths, the
rank-`m+1` upper palette, the old phase and plus phase in one factor, or the
rooted component structure making the two old partner edges distinct path
tickets.  Consequently (0.3) is a q1 planting theorem, not an unconditional
four-resource cycle-absorption theorem.

## 1. Exact local resource accounting

Let `L` have rank `m-1`, let `b in L`, and take distinct exterior labels
`a,d_0,c`.  Put

\[
\begin{array}{lll}
 E=L+d_0, &F=L+a, &U=L+a+d_0,\\
 A=L-b+a+d_0, &B=L-b+a+c,\\
 C=L-b+c+d_0, &D=L+c.
\end{array}                                                \tag{1.1}
\]

The old and new packet phases are

\[
 O=\{A\to B,C\to D,E\to F\},\qquad
 N=\{A\to F,C\to B,E\to D\}.                            \tag{1.2}
\]

Their four typed resource rows are

\[
\begin{array}{c|c|c}
 &O&N\\ \hline
\text{lower}&
 \{L-b+a,L-b+c,L\}&
 \{L-b+a,L-b+c,L\}\\
\text{upper}&
 \{U-b+c,U-a+c,U\}&
 \{U,U-b+c,U-a+c\}\\
\text{tail}&\{A,C,E\}&\{A,C,E\}\\
\text{head}&\{B,D,F\}&\{F,B,D\}.
\end{array}                                                \tag{1.3}
\]

Thus (1.2) is an exact four-resource exchange.  Notice that the upper row
is an equality of the **actual paired unions**, not a consequence of lower
q1 balance.

Let

\[
                 R:F=V_1\to V_2\to\cdots\to V_{h+2}\to V_0=E
                                                               \tag{1.4}
\]

be the private shortest resident rail of
`MATH_THEOREM_BOOLEAN_HEX_SHORTEST_RESIDENT_RETURN_RAIL_AND_PHASE_DECOUPLING_20260801.md`.
Since `R` is unchanged and its two outer palettes avoid (1.3),

\[
                         G^-=O\cup R,
              \qquad     G^+=N\cup R                         \tag{1.5}
\]

are four-resource matchings with identical local typed resource sets.
Both have `h+5` atoms: `h+2` rail atoms and three packet atoms.  They use
`h+7` physical owner vertices: the `h+3` rail-cycle vertices and
`A,B,C,D`.

### Theorem 1.1 (endpoint-bearing resident cycle absorber)

Let an ordered four-resource matching have physical indegree and outdegree
at most one.  Suppose it contains `G^-` and, in the full physical graph,

1. `EF union R` is one directed-cycle component;
2. `AB` and `CD` lie in two distinct directed-path components; and
3. those three components are pairwise distinct.

Then replacing `G^-` by `G^+`:

* preserves both outer resource multisets exactly;
* preserves every physical vertex's indegree and outdegree separately;
* preserves maximum physical degree two;
* removes exactly one directed cycle; and
* returns exactly two directed path components in place of the original
  cycle and two paths.

The collar-internal residence assertions and the local upper decks proved
for `R` remain valid in the corresponding phases.

#### Proof

The first three bullets follow coordinatewise from (1.3), with the
unchanged private rail added.  Delete the three old packet atoms.  The
cycle becomes the directed path `F R E`; each of the two old paths splits
at its selected edge.  The new atoms splice the first old path prefix to
`F R E` and then to the second old path suffix, while `C->B` joins the two
remaining fragments.  The result is two paths and contains no directed
cycle.  The residence and local-deck statements are exactly the local rail
theorems; no exterior chronology statement is used.  \(\square\)

### Proposition 1.2 (the two-path hypothesis is sharp for this packet)

If `AB` and `CD` lie in the same directed path component, toggling (1.2)
does not eliminate the last cycle.

#### Proof

If `AB` precedes `CD`, the unchanged directed segment `B leadsto C`
together with the new edge `C->B` is a cycle.  If `CD` precedes `AB`, the
unchanged segment `D leadsto A`, the new edge `A->F`, the broken-cycle
path `F R E`, and the new edge `E->D` form a cycle.  \(\square\)

Moreover one exterior path atom cannot suffice in this host: that would be
a nontrivial exact `2<->2` Boolean-diamond exchange, ruled out by the exact
outer-square/star-centre theorem.  Hence the ternary old support (one cycle
atom plus two path atoms) is support-minimal.

### Corollary 1.3 (fixed disjoint bank)

For `H` pairwise physically and four-resource-private packets satisfying
Theorem 1.1 on disjoint triples of components, all toggles commute.  The
simultaneous toggle preserves the complete four typed resource multisets,
preserves cap two pointwise, removes exactly `H` cycles, and returns `2H`
path components.  Pairwise packet privacy is sufficient here because the
theorem assumes the full component triples are disjoint; without that
component hypothesis, pairwise resource disjointness alone does not rule
out a cycle traversing several packets.

## 2. Exact interface with the fixed-H q1 extension theorem

An owner atom `T->H` with lower colour `L=T intersect H` lifts to the two
incidences

\[
                         T-L-H.                          \tag{2.1}
\]

The plus phase `G^+` has `h+5` lower-coloured owner atoms, so (2.1) gives
exactly `2(h+5)` incidence edges.  Palette privacy makes all its lower
vertices distinct.  Its physical path form makes every owner incidence
degree at most two, while each used lower vertex has degree exactly two.
Thus its lift is a 2-bounded alternating-path bank.

For `H` pairwise incidence-vertex-disjoint plus collars the protected bank
`P^+` satisfies

\[
              \Delta(P^+)\le2,\qquad
              |E(P^+)|=2\sum_{i=1}^H(h_i+5).             \tag{2.2}
\]

The small protected-factor theorem consequently supplies a spanning
undirected q1 two-factor containing `P^+` under

\[
              2\sum_i(h_i+5)\le m-2.                     \tag{2.3}
\]

This proves (0.3) when all `h_i=h`.

### 2.1 Four non-compositions

The following stronger conclusions do not follow from (2.3).

1. **Directed orientation.**  A completion component has only two global
   orientations.  If it contains two protected paths whose prescribed
   directions disagree around that component, no orientation realizes both
   typed tail/head records.  Ore--Ryser completion is undirected and does
   not prevent this conflict.  For one protected path, orienting its
   component is harmless; for several paths an orientation-compatible
   completion is an additional condition.

2. **Upper palette.**  The q1 theorem controls owner degrees and the
   rank-`m-1` lower palette.  It has no paired-union row.  The explicit
   `ML_4` completion in the source theorem covers only 20 of 21
   rank-five upper colours.  Local equality (1.3) says a toggle does not
   change whatever upper multiset the old factor had; it does not create
   an upper-complete old factor.

3. **One-phase quantifier.**  The theorem embeds `P^+` or `P^-`, separately.
   Their union is generally not 2-bounded.  Separate extendability does not
   produce one old factor on which the literal exchange can be performed.

4. **Rooted topology.**  A spanning q1 two-factor may have up to `W/3`
   components and contains no path component before openings are selected.
   It does not ensure that `AB` and `CD` become two distinct path tickets,
   or that the packet cycle is the component to be opened.  Theorem 1.1
   therefore needs a rooted component/opening certificate beyond (2.3).

   This is not merely absence of a proof.  The dimension-uniform `H=4`
   fixture in
   `MATH_THEOREM_H2_FINITE_H_RECURSIVE_HOST_ROOTED_Q1_NOGO_AND_CONDITIONAL_GATE_20260801.md`
   prescribes four pairwise typed-compatible q1 rails forming a saturated
   Johnson `C4`.  Every degree-two completion retains that closed
   component, so no connected spanning completion or Hamilton opening can
   contain the bank.  The fixture does not refute disconnected two-factor
   extension; it refutes precisely the missing rooted inference.

These are independent logical gaps.  In particular the central local
absorber is proved, while its universal fixed-H host theorem is not.

### 2.2 Ground-set qualification

The shortest-rail theorem is stated in the even ordered-diamond host on
`2m` coordinates.  The q1 extension theorem is stated in `ML_m` on
`2m-1` coordinates.  A direct application needs the complete packet label
set to lie in the chosen odd ground.

The rail formula itself remains valid there.  For one fixed target and one
fixed ternary choice `(b,c)`, however, the number of exterior `y` choices
is

\[
  |[2m-1]\setminus(U\cup\{c\})|=m-3,                    \tag{2.4}
\]

so the odd-ground realization count is

\[
                         (m-3)(m-2)_h,                   \tag{2.5}
\]

not `(m-2)(m-2)_h`.  This requires `m>=4`; the ordered `x`-tuple still
requires `h<=m-2`.  Formula (2.5) is a recount, not a theorem that an
arbitrary Pascal fibre contains the selected target and every packet label.

There is also a structural arithmetic difference.  On the even host the
lower and upper outer shores have equal size, so a full four-resource
matching can be bijective on both.  On the odd host the rank-`m+1` shore is
smaller; the correct global upper condition is surjectivity with excess,
not injectivity.  “Both outer palettes” must therefore mean exact local
multiset preservation plus a separately certified global upper cover.

## 3. Central theorem versus OR-word guards

Theorem 1.1 proves only the central owner/outer-resource statement and the
internal part of the resident collar.  Its exact scope is:

| row | proved locally | not supplied globally |
|---|---|---|
| lower q1 | identical old/new palette | existence of the rooted old host |
| adjacent upper | identical old/new packet multiset | upper completeness of the bulk |
| physical cap | indegree/outdegree preserved pointwise | compatible ordering/openings of all components |
| residence | no short internal run in either collared phase | exterior join runs and bulk residence |
| wider upper shadows | explicit internal deck and three-state rail rays | last witnesses across external cuts |
| compiler/common cap | nothing beyond resource privacy | literal cells, cap assignment, bounded complete damage |

The naked phases also have different clipped boundary-run records and
different socket pairings.  Hence strong unary U3/U4 transparency is false.
Phase decoupling permits separate old-auxiliary and plus-terminal
certificates, but does not manufacture either certificate.

## 4. Smallest proof-safe positive statement

The current exact implication is therefore:

> If a single ordered four-resource factor already contains a fixed
> private bank of resident collared old phases satisfying the distinct-path
> component hypothesis of Theorem 1.1, then toggling the bank is an exact
> endpoint-bearing cycle absorber preserving both outer palettes and
> cap-two degrees.  If instead only the plus incidence paths are specified,
> (2.3) embeds them in some undirected q1 two-factor, but directed typed
> orientation, upper completion and rooted path-ticket topology remain
> additional hypotheses.

This separates the proved positive local actuator from the still-open
universal host-selection problem.  No contiguous-OR conclusion follows
until exterior residence, all-width last-witness coverage and one terminal
common-cap certificate are supplied on one literal chronology.

## 5. Sources audited

* `MATH_THEOREM_AD_FOUR_RESOURCE_CYCLE_INTERNAL_EXCHANGE_OBSTRUCTION_20260801.md`;
* `MATH_THEOREM_BOOLEAN_HEX_TERNARY_FOUR_RESOURCE_ABSORBER_20260801.md`;
* `MATH_THEOREM_BOOLEAN_HEX_SHORTEST_RESIDENT_RETURN_RAIL_AND_PHASE_DECOUPLING_20260801.md`;
* `MATH_THEOREM_FIXED_H_COLLAR_Q1_TWO_FACTOR_AND_ROOTED_HOST_GATE_20260801.md`;
* `MATH_THEOREM_BOOLEAN_HEX_COLLARED_CYCLE_REGENERATIVE_SIDECAR_20260801.md`;
* `MATH_THEOREM_H2_FINITE_H_RECURSIVE_HOST_ROOTED_Q1_NOGO_AND_CONDITIONAL_GATE_20260801.md`.

No handoff or research-index file was edited by this audit.
