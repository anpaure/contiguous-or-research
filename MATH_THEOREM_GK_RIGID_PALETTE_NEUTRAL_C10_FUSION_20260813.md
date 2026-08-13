# A palette-neutral `C10` fuses the rigid odd-GK cycle with three donor cycles

**Date:** 2026-08-13  
**Status:** unconditional immediate-palette/topology theorem for every
`m>=5`, and q2-transparent theorem for every `m>=6`.  No q3 or
deeper-shadow neutrality is claimed.

## 0. Verdict

Let `n=2m+1`, and let `F_m` be the odd Greene--Kleitman/complement
Johnson two-factor on rank-`m+1` owners.  There is an explicit alternating
`C10` through one edge of its forced single-soliton cycle such that:

1. every owner degree remains two;
2. the five rank-`m` lower colours are cyclically permuted;
3. every rank-`m+2` upper colour is preserved edge by edge; and
4. four old factor cycles are replaced by exactly two cycles.

Thus the singleton-colour cycle is not frozen in the ambient Boolean
diamond matching space.  A five-diamond surgery exports its rigid colour
and lowers the local component count by two.

The `C10` factors through two alternating `C6` switches with one cancelling
internal chord.  For `m>=6` both phases are q2-multiset neutral.  This is a
strict strengthening of the graphic-neutral rigid `C6`: the paired packet
has net support five and genuinely lowers component count.


## 1. The five old GK diamonds

Binary words below are read on coordinates `0,1,...,2m`.  Put

\[
\begin{aligned}
 L_0&=0^m1^m0,\\
 L_1&=10^{m-1}1^{m-1}00,\\
 L_2&=11\,0^{m-2}1^{m-2}000,\\
 L_3&=10^{m-1}1^{m-2}010,\\
 L_4&=0^m1^{m-2}011.
\end{aligned}                                           \tag{1.1}
\]

Each has weight `m`.  Write `g_+(L)` and `g_-(L)` for its upward
successors in the ordinary and complemented Greene--Kleitman symmetric
chain decompositions.  Direct linear parenthesis cancellation gives the
following oriented endpoints (all exponents are nonnegative for `m>=5`):

\[
\begin{array}{c|c|c}
i&A_i&B_i\\ \hline
0&0^{m-1}1^{m+1}0&0^m1^{m+1}\\
1&10^{m-2}1^m00&10^{m-1}1^m0\\
2&11\,0^{m-3}1^{m-1}000&11\,0^{m-2}1^{m-1}00\\
3&10^{m-2}1^{m-1}010&11\,0^{m-2}1^{m-2}010\\
4&0^{m-1}1^{m-1}011&10^{m-1}1^{m-2}011.
\end{array}                                             \tag{1.2}
\]

For each `i`, the unordered pair `{A_i,B_i}` is exactly
`{g_+(L_i),g_-(L_i)}`.  The labels `A_i,B_i` are chosen for the cyclic
switch identity, not to prescribe which of the two GK maps supplies the
endpoint.  Hence

\[
                         E_i=A_iB_i                     \tag{1.3}
\]

is an old edge of `F_m`, with lower colour `L_i`.

## 2. The alternating `C10`

Replace the five old edges by

\[
                         E_i'=B_iA_{i-1}
                         \qquad(i\in\mathbb Z_5).       \tag{2.1}
\]

The ten owners in `(1.2)` are pairwise distinct for `m>=5`, so `(2.1)`
is a simple alternating `C10`.  Every owner loses one old incident edge
and gains one new incident edge.  Therefore owner degree is preserved
pointwise.

The set identities in `(1.2)` give

\[
 B_i\cap A_{i-1}=L_{i-1},\qquad
 B_i\cup A_{i-1}=A_i\cup B_i.                         \tag{2.2}
\]

The first equality says that the new lower colours are

\[
                         L_4,L_0,L_1,L_2,L_3,           \tag{2.3}
\]

a cyclic permutation of the old five.  The second equality is stronger
on the upper side: the rank-`m+2` union colour of `E_i` is recreated by
`E_i'` at the same role.  Thus both immediate colour multisets are exact.

In particular the globally singleton upper colour on `E_0`, namely the
rotation of `0^{m-1}1^{m+2}`, now occurs on `E_0'=B_0A_4`, whose other
endpoint lies outside the old single-soliton owner cycle.


## 3. Exact old-component geometry

The five old edges lie on four PBBS/GK components
with lengths

\[
 n,\qquad n(2m-3),\qquad n(2m-5),\qquad n(2m-7).        \tag{3.1}
\]

More precisely:

* `E_0` lies on the single-soliton component of length `n`;
* `E_1` and `E_4` lie on the same `(m-1,1)` component of length
  `n(2m-3)`;
* `E_3` lies on one component of length `n(2m-5)`; and
* `E_2` lies on one component of length `n(2m-7)`.

This follows by applying the rooted-Dyck PBBS update to the complements of
the five displayed edges.  The resulting shape tours have periods

\[
                         1,\ 2m-3,\ 2m-5,\ 2m-7,        \tag{3.2}
\]

and their literal voltage sums are units modulo `n`; hence the displayed
states lie on physical components of the stated lengths.  The two words
`L_1,L_4` occur at two phases of the `2m-3` component.

For topology bookkeeping, orient each old edge from its ordinary-GK
endpoint `g_+(L_i)` to its complemented-GK endpoint `g_-(L_i)`.  Delete
`E_0,...,E_4`.  Direct substitution in the same rooted update gives the
endpoint return permutation

\[
                    0\mapsto0,\qquad
                    1\leftrightarrow4,\qquad
                    2\mapsto2,\qquad
                    3\mapsto3.                          \tag{3.3}
\]

That is, the single-soliton and the two other donor components each give
one residual path, while the `(m-1,1)` component is cut twice and gives
two residual paths joining the `1` and `4` ports crosswise.

The new matching `(2.1)` is the five-cycle on the exposed ports.  Composing
it with `(3.3)` gives exactly two return orbits.  Equivalently, deleting
five edges from four cycles produces five paths, and the five new edges
join those paths into two cycles.  Therefore

\[
             \boxed{c(F_m\triangle C_{10})=c(F_m)-2}     \tag{3.4}
\]

on the affected subsystem.

### Theorem 3.1 (rigid-cycle `C10` fusion)

For every `m>=5`, the switch `(2.1)` is a simple owner-degree-neutral
Johnson `C10`, preserves the complete lower and upper immediate palettes,
and replaces the four old cycles in `(3.1)` by two cycles.

## 4. Paired-`C6` factorization and q2 transparency

Write

\[
              e_i=A_iB_i,\qquad n_i=B_iA_{i-1},
\]

and introduce the internal Johnson chord

\[
                              c=A_3B_1.             \tag{4.1}
\]

The decagon factors as two simple alternating hexagonal switches:

\[
 \{e_1,e_2,e_3\}\longmapsto\{n_2,n_3,c\},          \tag{4.2}
\]

followed by

\[
 \{e_0,e_4,c\}\longmapsto\{n_0,n_1,n_4\}.          \tag{4.3}
\]

The chord occurs positively in `(4.2)` and negatively in `(4.3)`, so it
cancels from the net symmetric difference.  Direct intersections and
unions show that each phase separately preserves its three lower colours
and its three upper colours as multisets.

The q2 audit can be stated compactly on the five changed `A`-side turns.
For an owner `X`, if `e` is its changed incident diamond and `e^*` its
unchanged factor diamond, use the dual-PBBS convention

\[
 q_2(X)=\overline{(\bigcup e)\cup(\bigcup e^*)}.        \tag{4.4}
\]

Put

\[
\begin{aligned}
 X_0&=1^{m-2}0^{m+3},\\
 X_1&=0\,1^{m-3}0^{m+2}1,\\
 X_2&=00\,1^{m-4}0^{m+1}11,\\
 X_3&=00\,1^{m-4}0^m101,\\
 X_4&=0\,1^{m-3}0^m100.
\end{aligned}                                          \tag{4.5}
\]

At every `B_i` endpoint the selected q2 row is pointwise unchanged.  At
the `A` endpoints, the first phase `(4.2)` cyclically transports

\[
                              X_1\to X_2\to X_3\to X_1, \tag{4.6}
\]

while, in the post-first-phase state where `A_3` carries `X_1`, the second
phase `(4.3)` cyclically transports

\[
                              X_0\to X_1\to X_4\to X_0. \tag{4.7}
\]

These identities follow by one more forward/reverse parenthesis
cancellation at the unchanged companion edge of each displayed owner.
For `m>=6`, the maxima determining those companions are strict, so
`(4.6)`--`(4.7)` prove exact q2-multiset neutrality of both phases and of
the net `C10`.

At `m=5`, the immediate palettes and topology remain valid, but the first
phase has a nonzero q2 current.  Thus `m>=6` is the exact threshold for
the protected statement proved by this factorization.

### Theorem 4.1 (protected paired-hexagon repair)

For every `m>=6`, the `C10` `(2.1)` is a serially legal pair of simple
alternating `C6` switches with one cancelling internal chord.  It preserves owner
degree, both immediate colour multisets, and the complete selected q2
multiset, while replacing four old cycles by two.

## 5. Scope and consequences

The earlier singleton-colour theorem proves only that no representative
thinning *inside the fixed GK/PBBS factor* can hit the rigid cycle.  The
`C10` proves the sharp complementary fact: that obstruction disappears
in the ambient diamond-matching exchange space.

This does not by itself produce a path forest.  For `m>=6`, all four input
action sectors are wholly max-height selected and the transported packet
creates no omission, so the two output cycles are still unpunctured.  What
has been gained is topology compression: four forced donor cycles become
two, which costs only two named punctures under a bounded-component
compiler.  No whole-component selection assertion is made here at `m=5`.

The q2 row is now closed for `m>=6`.  Residence histories, q3 and deeper
shadows, arbitrary exterior upper contexts, and typed cap state remain
separate protected coordinates; no transparency in those coordinates is
inferred from q2 neutrality.

## 6. Reproduction

The independent enumerator

```text
scratch/search_gk_pbbs_general_owner_alternating_trade_20260813.py
```

reconstructs every old and new edge, checks lower/upper multisets and
owner degrees, and computes the exact component change.  For example,
`m=5,6` both return `component_delta=-2` on the displayed family.
The computation is an audit of the explicit identities, not a premise of
the theorem.
