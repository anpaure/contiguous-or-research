# The suspended `D_3` pentagon already has a connected union of endpoint-sealed companion matchings

**Date:** 2026-08-06  
**Method:** pure mathematics; direct reading of the eight authenticated
native alignments and an exact unit-current circulation argument  
**Status:** unconditional endpoint/common-tail theorem.  It uses the
corrected positive companion graph, with the spurious edge `52` absent.  It
does **not** prove state-closed generation at changing slots, cancellation of
the native q1/all-width rail currents, or terminal common-cap feasibility.

## 0. Verdict

The capacity-one endpoint router is not needed for a connected spanning
companion skeleton in the suffix-suspended anchored `D_3` pentagon.

In the negative phase, the native edges

\[
                              M^- =\{12,54\}                  \tag{0.1}
\]

are row-disjoint and each fixes its two complementary endpoint pairs.  In
the positive phase, the same is true of

\[
                              M^+ =\{14,32\}.                 \tag{0.2}
\]

Their union is the spanning path

\[
                              5-4-1-2-3.                      \tag{0.3}
\]

Every one of these four moves therefore suspends, with a common tail, to an
individually sealed capacity-one exact support trade.  The two phase
matchings already satisfy the endpoint part of the phase-switched companion
hypothesis with no cross-cylinder coalescence.

The remaining four native edges really do leak.  Their endpoint currents
are

\[
 \begin{array}{c|c}
  23^-&[126]-[124]\\
  25^-&[234]-[124]\\
  43^+&[235]-[135]\\
  45^+&[136]-[135].
 \end{array}                                                \tag{0.4}
\]

Moreover these leaks cannot cancel by taking any nonnegative collection of
forward moves from the corrected two-phase catalogue, even after arbitrary
coordinate conjugation preserving the `D_3` port family.  All four currents
flow from one endpoint orbit into two different endpoint orbits.  Thus the
sealed spanning path (0.3) is not merely convenient: within the native
port-preserving forward catalogue, it is the entire endpoint-safe part.

## 1. A unit-current common-tail criterion

Let `J` be a base ground and let `E` be a disjoint tail ground.  Fix one
tail complement geodesic

\[
                         S_0,S_1,\ldots,S_s.                  \tag{1.1}
\]

For an oriented base endpoint `P`, its proper common-tail column is

\[
                         \mathcal C(P)
                         =\{P+S_j:1\le j\le s\}.              \tag{1.2}
\]

The columns for distinct `P` are disjoint, because projection to `J`
recovers `P`.

Suppose a finite collection of local base trades is exact on its internal
state and adjacent-colour ledgers.  Assume each trade changes only one
oriented terminal endpoint, from `P_c` to `Q_c`; write this as the unit arc

\[
                              P_c\longrightarrow Q_c.         \tag{1.3}
\]

Assume also that the selected old packets are pairwise resource-disjoint and
that no oriented old endpoint occurrence is used twice.

### Theorem 1.1 (capacity-one endpoint-cycle criterion)

After suspension by the common tail (1.1), the simultaneous replacement is
exact on every proper tail state and tail adjacent colour if and only if

\[
        \deg_H^+(P)=\deg_H^-(P)
        \qquad\hbox{for every endpoint type }P,                \tag{1.4}
\]

where `H` is the directed multigraph with arcs (1.3).  Under the
capacity-one old-endpoint hypothesis, every nontrivial component of `H` is
a directed cycle; sealed trades are loops.

In a directed cycle, the positive endpoint claim of one trade is installed
at the exact occurrence freed by the next trade.  The same cyclic matching
works simultaneously at every tail level.

#### Proof

At proper tail state `j`, the aggregate signed current is

\[
             \sum_c\bigl([Q_c+S_j]-[P_c+S_j]\bigr).            \tag{1.5}
\]

The map `[P] -> [P+S_j]` is injective.  Hence (1.5) vanishes if and only if
the coefficient of every `P` vanishes, which is exactly (1.4).

The identical argument applies to the tail adjacent colours after replacing
`S_j` by `S_j union S_(j+1)`.  Every internal base resource was assumed
exact already.

Because old endpoint occurrences have capacity one, every vertex has
outdegree at most one.  Balance gives indegree at most one as well.  A finite
balanced directed graph of maximum in/out degree one is a disjoint union of
directed cycles and isolated vertices.  Matching each incoming claim to the
unique outgoing old occurrence proves the capacity-one statement.  \(\square\)

This theorem is the weakest useful router: no Hall system remains after the
unit endpoint arcs have been selected.  The only global condition is the
Euler balance (1.4).

## 2. Literal endpoint currents of the corrected `D_3` catalogue

Write `[P]` for the **oriented** complementary endpoint token

\[
                              (P,[6]-P).                        \tag{2.1}
\]

The first entry is the anchored root and the second is the terminal
endpoint.  This oriented convention is proof-safe for suspension; reversing
a row is not silently identified with the same token.

For semilength three, an aligned native pair has the form

\[
 \begin{aligned}
 r_0&=(a,b,x,c,d,y_1,y_2),\\
 r_1&=(b,d,x,a,c,y_1,y_2),
 \end{aligned}                                                \tag{2.2}
\]

and its native substitution is

\[
 \begin{aligned}
 r'_0&=(b,a,x,d,c,y_1,y_2),\\
 r'_1&=(d,b,x,c,a,y_1,y_2).
 \end{aligned}                                                \tag{2.3}
\]

Rotate each output order so that `infinity` is last.  Its first three
coordinates are the initial endpoint of the corresponding complement path.
Applying this literal rule to the four negative and four corrected positive
alignments gives:

\[
\begin{array}{c|c|c|c}
\text{phase edge}&\text{old endpoint pairs}&\text{new endpoint pairs}
  &D_e\\ \hline
-:12&[123]+[124]&[123]+[124]&0\\
-:23&[124]+[125]&[125]+[126]&[126]-[124]\\
-:25&[124]+[134]&[134]+[234]&[234]-[124]\\
-:54&[134]+[135]&[134]+[135]&0\\ \hline
+:14&[123]+[135]&[123]+[135]&0\\
+:32&[125]+[124]&[125]+[124]&0\\
+:43&[135]+[125]&[125]+[235]&[235]-[135]\\
+:45&[135]+[134]&[134]+[136]&[136]-[135].
\end{array}                                                  \tag{2.4}
\]

### Theorem 2.1 (exact endpoint classification)

The four edges `12^-`, `54^-`, `14^+`, and `32^+` are individually
endpoint-sealed.  The other four currents are exactly (0.4).

#### Proof

Equation (2.3), followed by the rotate-after-`infinity` rule, gives the
middle two columns of (2.4).  Cancelling the common oriented endpoint tokens in
each row gives the last column.  Complementary terminal endpoints are
carried automatically by the oriented token (2.1).  \(\square\)

The deletion of the formerly reported positive edge `52` is respected:
it appears nowhere in (2.4).

## 3. Two sealed phase matchings already span all five rows

### Theorem 3.1 (sealed connected phase skeleton)

The negative edges `12,54` form a matching, the positive edges `14,32`
form a matching, and their union is connected:

\[
                  M^-\cup M^+=\{12,54,14,32\}
                  =\{5-4,4-1,1-2,2-3\}.                     \tag{3.1}
\]

After suspending the two pentagon phases by any common complement-geodesic
tail, every edge in these matchings remains an individually sealed,
reversible, capacity-one exact support trade.  Hence endpoint-halo
coalescence is not a missing premise for this connected phase skeleton.

#### Proof

Disjointness inside each phase and connectivity of (3.1) are immediate.
The native inverse-pair theorem says that every displayed move preserves
the aggregate two central palettes of its two rows.  By Theorem 2.1, the
two endpoint pairs are also unchanged for each edge in (3.1).

Under common-tail suspension, the base-part state and adjacent-colour
ledgers remain equal.  In each sealed row, the two native adjacent swaps
leave the three-label deletion set fixed; hence they occur within the two
halves of the base order, rather than across its `infinity` cut.  In the
tensor word

\[
              (D_P,D_S,I_P,I_S,\mathord\infty),                \tag{3.2}
\]

the tail blocks `D_S,I_S` therefore remain in their original positions,
and the output is exactly the common-tail suspension of the output base
path.  Every proper tail state and tail adjacent colour depends only on the
fixed terminal endpoint of its named row and on the common tail.  Reorder
the two new rows by their distinct oriented endpoint tokens; then those
resources agree row by row.  Thus the suspended old and new two-row packets
have identical complete factor-resource ledgers and can be replaced inside
the pentagon partial factor with the outside untouched.  The native move is
involutive, so the trade is reversible.  \(\square\)

The conclusion is deliberately about the endpoint and exact-factor
interface.  A native edge still has nonzero q1/deeper interval current, and
one use at one slot does not provide a state-closed copy of every positional
generator.

## 4. A sharp orbit-mass no-go for every leaking forward edge

Let

\[
       G=\operatorname{Aut}(\mathcal D_3)
        =\langle(2\ 3),(4\ 5)\rangle.                         \tag{4.1}
\]

On complementary endpoint-pair types, define the three `G`-orbits

\[
 \begin{aligned}
 \mathcal A&=G[124]=\{[124],[125],[134],[135]\},\\
 \mathcal B&=G[126]=\{[126],[136]\},\\
 \mathcal C&=G[234]=\{[234],[235]\}.
 \end{aligned}                                                \tag{4.2}
\]

Every nonzero current in (2.4) is a unit arc from `mathcal A` to
`mathcal B` or from `mathcal A` to `mathcal C`.

### Theorem 4.1 (port-preserving forward-orbit no-go)

Take any nonnegative multiset of coordinate conjugates, under `G`, of the
eight forward native moves in (2.4).  If its aggregate endpoint current is
zero, then every selected move is one of the four sealed types.  In
particular no leaking forward move can be repaired by any number of other
forward moves from the corrected port-preserving two-phase orbit.

#### Proof

For a signed endpoint current `D`, put

\[
                       \Phi(D)=\sum_{P\in\mathcal A}D(P).       \tag{4.3}
\]

Every sealed move has `Phi=0`.  Every leaking move in (2.4), and every
`G`-conjugate of it, has `Phi=-1`, because its negative endpoint lies in
`mathcal A` and its positive endpoint lies in `mathcal B union mathcal C`.
Therefore a nonnegative multiset containing `L` leaking moves has
`Phi=-L`.  Zero aggregate current forces `L=0`.  \(\square\)

This is the orbit-mass obstruction in the exact Reynolds formula: the
port-preserving group is not transitive on endpoint types, and each leak
has nonzero mass on the orbit `mathcal A`.

### Corollary 4.2 (exact escape routes)

Any endpoint-safe construction which genuinely uses one of the leaking
edges must introduce at least one of:

1. a physically plantable reverse arc from `mathcal B union mathcal C`
   back to `mathcal A`;
2. a coordinate phase outside `Aut(D_3)`, together with a reselected port
   completion;
3. an external component whose endpoint current has positive
   `mathcal A`-mass; or
4. a joint outside completion which changes the endpoint bank itself.

Accidental claim overlap or laminarity cannot evade Theorem 4.1, because
`Phi` is an additive endpoint-type invariant.

## 5. Sharpened remaining guard

The corrected `D_3` pentagon therefore closes the endpoint part of the
phase-switched companion programme more strongly than a generic common-halo
router would:

\[
 \boxed{
 \begin{array}{c}
 \text{negative sealed matching }\{12,54\}\\
 +\text{ positive sealed matching }\{14,32\}\\
 \Longrightarrow\text{ connected endpoint-safe phase skeleton.}
 \end{array}}                                                \tag{5.1}
\]

What remains is not endpoint coalescence.  It is the following guarded
dynamic statement:

> **Sealed-edge reuse and rail closure.**  Promote the four sealed displayed
> native occurrences to reusable closed phase excursions which supply the
> required positional words after every preceding excursion, while cancelling
> their q1/all-width two-rail currents and retaining the terminal common-cap
> interface.

Theorem 3.1 supplies a connected union of capacity-one endpoint-safe
matchings.  It does not turn one involutive slot on each edge into the full
diagonal `A_(2m+1)` action required by the abstract group theorem.  That
state-closure/rail problem, rather than a terminal endpoint Hall problem, is
the exact next gate.
