# Two asymmetric stars: the orientation bound and the exceptional depth-two edge

Date: 2026-08-01  
Lane: Thread D, exact two-star trace algebra  
Status: exact local theorem.  This note strengthens the separated-selector
analysis to all four spatial orientations and records the unique adjacent
depth-two exception, including its extra joint-span debt.  It does not assert
that an exterior return for that debt exists.

## 0. Result

Take the exact asymmetric one-chain selector with a nonempty core `C` and
complementary bases

\[
 B_0=C\cup\{a\},\qquad B_1=C\cup\{b\},
\]

and strict prefix increments `f_1,...,f_(d-1)`.  Pair it with the reflected
suffix selector, whose strict increments, read away from its star, are
`f_d,...,f_2`.  The two star bases are complementary.

For every `d>=3`, **every** choice of the two active-fan orientations forces
the star separation

\[
                              \Delta\ge d+1.                 \tag{0.1}
\]

More precisely, the exact minimum is `d+1` when the fans point outward or
inward and `2d-1` when both point left or both point right.  At the global
minimum the outward/inward words coexist on support width `3d`; the two
same-direction minima have width `4d-2`.
But then no length-`(d+1)` owner window contains both stars.  The first
collar has star-spanning owners

\[
                 B_0\cup B_1\cup\{f_1,\ldots,f_i\},
                 \qquad 1\le i\le d-1,                     \tag{0.2}
\]

and the second has the reflected family.  Already the owners at `i=1,2`
have different ranks.  Hence no such pair is an equicardinal `D^d`
carrier when `d>=3`.  The target/address ledger may be closed abstractly
with prepared endpoint returns, but the literal common-carrier row fails.

Depth two is exceptional.  The two stars may be adjacent and may serve as
each other's forced opposite-base occurrence.  The four-source word is an
exact, phase-independent Johnson edge.  However deleting both stars exposes
one old interval spanning both cuts, with value `C+{f_1,f_2}`; the final word
has no cell of that value.  Thus the adjacent edge is a positive trace and
common-carrier macro, not a self-contained full lower-deck repair.

## 1. Forced occurrences of one asymmetric selector

Give a selector a star base `B_e`, an active-fan direction `sigma in
{-1,+1}`, and an ordered strict filler list `g_1,...,g_(d-1)`.  Its active
fan has values

\[
 B_e\subset B_e+g_1\subset\cdots\subset
 B_e+\{g_1,\ldots,g_{d-1}\}.                              \tag{1.1}
\]

Its destroyed crossing chain has the complementary base `B_(1-e)` and the
same filler flag (possibly read in reverse according to the side index).
Exactness forces two elementary facts.

1. The exclusive coordinate of `B_(1-e)-B_e` occurs at distance one on
   the inactive flank.  Indeed it is absent from the star and active fan,
   but it belongs to every crossing; on one flank the only threshold which
   covers every crossing is distance one.
2. The new filler `g_t` first occurs at distance `t` on the active flank.
   A prior occurrence would put it in the preceding strict fan cell, while
   absence at distance `t` would fail to create the prescribed increment.

Redundant copies of an already exposed filler may occur, but no source in a
fan prefix may contain a future filler.  These are just the coordinatewise
threshold equations of the one-star theorem.

## 2. All four orientations

Put the prefix star at `p`, the suffix star at `q>p`, and write
`Delta=q-p`.  The prefix ordered fillers are

\[
              f_1,f_2,\ldots,f_{d-1},                     \tag{2.1}
\]

whereas the suffix ordered fillers, read along its active fan, are

\[
              f_d,f_{d-1},\ldots,f_2.                     \tag{2.2}
\]

### Theorem 2.1 (exact orientation minima)

For `d>=3`, the exact minimum star separations are

\[
\begin{array}{c|cccc}
 \text{active directions}&\text{outward}&\text{inward}&
     \text{both left}&\text{both right}\\ \hline
 \Delta_{\min}&d+1&d+1&2d-1&2d-1\\
 \text{support width}&3d&3d&4d-2&4d-2
\end{array}                                                \tag{2.3}
\]

For `d=2`, the corresponding minima are `1,3,3,3` and the widths are
`4,6,6,6`; the first is the adjacent exception of Section 4.

#### Proof

There are four direction pairs.

* **Both fans point outward.**  If `2<=Delta<=d`, the opposite-base
  occurrence forced one step inside either star lies on the inactive flank
  of the other selector and belongs to one of its crossings.  It introduces
  that selector's own star-exclusive coordinate, which every complementary
  crossing target omits.  If `Delta=1`, the two stars do serve as the forced
  opposite bases, but the suffix source carrying its first filler `f_d`
  lies two steps to the right of the prefix star.  For `d>=3` that source
  belongs to a prefix crossing, while no prefix target contains `f_d`.

* **Both fans point inward.**  The case `Delta=1` puts the opposite star
  itself in the first active fan cell and is immediately impossible.  For
  `2<=Delta<=d`, choose a shared source at distances `t,u>=1` from the two
  stars, so `t+u=Delta`.  It must contain the prefix increment `f_t`.
  The suffix fan through distance `u` contains only
  `f_(d-u+1),...,f_d`.  Since `t+u<=d`, it excludes `f_t`, a contradiction.

* **Both active fans point left.**  For `Delta<=d-1`, the prefix star lies
  in the suffix active fan and introduces the active label which that fan
  omits.  At `Delta=d`, the farthest suffix increment is `f_2` and occurs at
  `p+1`, the nearest inactive source of the prefix selector.  That source
  belongs to every prefix crossing, including the first target
  `B_(1-e)+f_1`, which excludes `f_2`.  If
  `d+1<=Delta<=2d-2`, the farthest active source of the suffix is at
  `r=Delta-d+1`, where `2<=r<=d-1`, and contains `f_2`.  It is again on the
  inactive flank of the prefix and in its first crossing, which excludes
  `f_2`.  Hence `Delta>=2d-1`.

* **Both active fans point right.**  This is the reflection of the preceding
  case.

Thus the stated lower bounds hold.  They are attained as follows.  At
`Delta=d+1`, the outward words are (2.4)--(2.5) below.  For the inward
pair, the shared sources at positions `t=2,...,d-1` receive `C+f_t` from
both prescriptions.  At `Delta=2d-1`, same-direction supports are
disjoint and adjacent.  For `d=2`, the same checks give `1,3,3,3`.
\(\square\)

The bound is sharp.  With outward-facing active fans and stars at `0` and
`d+1`, use

\[
\begin{array}{lll}
 A_{-t}=C+f_t &(1\le t<d),& A_0=B_e,\\
 A_1=B_{1-e},&& A_t=C\quad(2\le t<d),
\end{array}                                                \tag{2.4}
\]

and, at the second star `s=d+1`,

\[
 A_s=B_{1-e},\quad A_{s-1}=B_e,\quad
 A_{s-t}=C\ (2\le t<d),\quad
 A_{s+t}=C+f_{d-t+1}\ (1\le t<d).                         \tag{2.5}
\]

The overlap is `2,...,d-1`, where both prescriptions are `C`.  The union of
the two supports is `[-(d-1),2d]`, of width `3d`.

## 3. Equicardinal obstruction and lower-deck delta

At separation at least `d+1`, a source interval of length `d+1` cannot meet
both stars.  The one-star trace identity therefore applies independently.
For the prefix collar, adjoining its star to destroyed crossing `i` gives
exactly (0.2); successive values gain the fresh filler `f_(i+1)`.  For
`d>=3` there are at least two such values, of different cardinalities.  No
choice of hidden copies or larger prospective caps changes their union.
This proves the equicardinal no-go in Section 0.

The two affected lower decks also direct-sum at separation `d+1`: no source
interval of length at most `d` contains both stars.  For a shorter crossing
with `u,v>=1` and `u+v<=d-1`, the prefix collar changes

\[
 B_{1-e}\cup\{f_1,\ldots,f_u\}
 \quad\longmapsto\quad
 B_0\cup B_1\cup\{f_1,\ldots,f_u\},                       \tag{3.1}
\]

and the suffix collar has the reflected formula

\[
 B_e\cup\{f_{d-v+1},\ldots,f_d\}
 \quad\longmapsto\quad
 B_0\cup B_1\cup\{f_{d-v+1},\ldots,f_d\}.                \tag{3.2}
\]

Thus both triangular collars gain the locally excluded active label.  Any
selected pins on these cells require literal return edges; scalar fan counts
do not preserve them.

Two source insertions increase the number of cells of lengths `1,...,d` by
exactly `2d`, provided the displayed support is internal.  The raw source
length charge is `+2`.  A zero-charge version needs two separately verified
deletions and all of their interval returns.

## 4. The adjacent depth-two edge

For `d=2`, put the stars at `0,1` and define, in phase `e`,

\[
 (A_{-1},A_0,A_1,A_2)
   =(C+f_1,\ B_e,\ B_{1-e},\ C+f_2).                       \tag{4.1}
\]

Then the prefix star at `0` has

\[
 \operatorname{NEW}^P=B_e+f_1,\qquad
 \operatorname{OLD}^P=B_{1-e}+f_1,                        \tag{4.2}
\]

and the suffix star at `1` has

\[
 \operatorname{NEW}^S=B_{1-e}+f_2,\qquad
 \operatorname{OLD}^S=B_e+f_2.                            \tag{4.3}
\]

The two depth-two owners are

\[
 U_1=C+\{a,b,f_1\},\qquad U_2=C+\{a,b,f_2\}.              \tag{4.4}
\]

They are phase independent, equicardinal, distinct, and adjacent in the
Johnson graph.  Taking the phase-independent star cap `B_0 union B_1`, the
two terminal words are nonempty and swap the two star addresses.  Hence
(4.1) is a literal common-cap, owner-simple local macro of source charge
`+2` and support width `4=2d`.

It is not closed relative to the word with both stars deleted.  The old
two-source word has the length-two cell

\[
                         J=C+\{f_1,f_2\}.                  \tag{4.5}
\]

The new length-two cells are

\[
 B_e+f_1,\qquad B_0\cup B_1,\qquad B_{1-e}+f_2,            \tag{4.6}
\]

and none equals `J`.  More explicitly, the complete old/new deck of lengths
at most two is

\[
\begin{array}{c|c}
 \text{old}&C+f_1,\ C+f_2,\ J\\
 \text{new}&C+f_1,\ B_e,\ B_{1-e},\ C+f_2,
       \ B_e+f_1,\ B_0\cup B_1,\ B_{1-e}+f_2.
\end{array}                                                \tag{4.7}
\]

The net cell count is `+4`, as required, but `J` needs a separate terminal
provider in the same common-cap state.  The central new cell
`B_0 union B_1` is not such a provider.  Therefore (4.1) is the smallest
positive trace/carrier exception and simultaneously the smallest exact
joint-span obstruction to a self-returning two-star packet.

## 5. Exact scope

The result rules out the literal composition of two individually exact
asymmetric selectors as a growing-depth equicardinal carrier.  It does not
rule out a two-star macro in which one collar ceases to be that selector, a
nonflat/facet bridge changes the owner equations, or compensating deletions
and exterior returns close (3.1)--(3.2).  Likewise the depth-two edge becomes
a complete packet if and only if its extra target `J` receives a legal
return together with the four OLD/NEW chain assignments in one terminal
common-cap word.

## 6. Independent exact audit

The source-prescription census

```text
scratch/audit_threadD_two_star_orientation_adjacent_gate_20260801.py
```

checks both phases and all four orientations through `d=24`.  The stronger
coordinatewise audit

```text
scratch/audit_threadD_two_star_orientation_redundant_copy_exhaustive_20260801.py
```

allows every redundant source copy consistent with the exact fan and
crossing OR equations.  For `2<=d<=6` it rejects all 196 subminimum
separations and realizes all 40 minima with nonempty literal words.  This is
a finite independent replay of the hypotheses used in Theorem 2.1, not the
source of its dimension-uniform proof.
