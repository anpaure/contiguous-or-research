# The Johnson square is the minimal coupled open three-return macro

**Date:** 2026-08-01  
**Lane:** K, opened rolling-reset return / owner-changing primitive  
**Status:** unconditional four-resource construction and support-minimality
theorem.  The packet gives one attachment return and both predecessor
parity returns in one literal Boolean trade.  Its two internal owner words
are reversals, so their complete internal interval-OR spectra and coordinate
run inventories agree.  Exterior cross-windows, a guarded depth-`d` word
embedding, compiler incidence, and a global reset splice are not claimed.

## 0. Result

Let a legal directed Boolean-diamond atom be

\[
                         (L,U;T,H),
 \qquad L=T\cap H,\quad U=T\cup H,\quad |T|=|H|=m.
\tag{0.1}
\]

There is a support-four two-phase trade with the same distinct lower,
upper, tail and head resources in both phases such that:

1. the complete physical phases are the two orientations of one Johnson
   `C4`;
2. after omitting one seam orientation from each phase, the head--owner
   overlay is one alternating path;
3. the tail--head overlay is exactly two alternating three-edge paths with
   opposite endpoint parity;
4. the lower--tail overlay is one further alternating path;
5. the omitted old/new seam atoms use one common lower/upper pair and the
   two opposite tail/head orientations;
6. the two open middle-owner words are literal reversals, hence have the
   same complete internal interval-union spectrum and the same coordinate
   run-length inventory.

No resource-exact orientation-flip trade has support two or three.  Thus
support four is sharp in this four-resource model.

This closes the *central projection algebra* requested by the opened
rolling reset.  It is stronger than three independent ternary ears because
the two parity returns share their seam colours inside one coupled packet.

## 1. The square

Let `K` have rank `m-2`, and choose four distinct labels

\[
                            x,y,z,w\notin K.
\]

Put

\[
\begin{aligned}
 V_0&=K+x+z,&V_1&=K+x+y,\\
 V_2&=K+y+w,&V_3&=K+z+w.
\end{aligned}                                               \tag{1.1}
\]

Read indices modulo four and set

\[
                         L_i=V_i\cap V_{i+1},
 \qquad                  U_i=V_i\cup V_{i+1}.               \tag{1.2}
\]

Explicitly,

\[
\begin{array}{c|c|c}
i&L_i&U_i\\ \hline
0&K+x&K+x+y+z\\
1&K+y&K+x+y+w\\
2&K+w&K+y+z+w\\
3&K+z&K+x+z+w.
\end{array}                                                  \tag{1.3}
\]

All four `V_i`, all four `L_i`, and all four `U_i` are distinct.  Define

\[
 \mathcal C^+
   =\{(L_i,U_i;V_i,V_{i+1}):0\le i<4\},                    \tag{1.4}
\]

\[
 \mathcal C^-
   =\{(L_i,U_i;V_{i+1},V_i):0\le i<4\}.                    \tag{1.5}
\]

### Theorem 1.1 (exact square trade)

Both `C+` and `C-` are four-resource matchings and use exactly the same
lower, upper, tail and head resource sets:

\[
 \{L_0,L_1,L_2,L_3\},\quad
 \{U_0,U_1,U_2,U_3\},\quad
 \{V_0,V_1,V_2,V_3\},\quad
 \{V_0,V_1,V_2,V_3\}.                                     \tag{1.6}
\]

Their directed physical projections are respectively

\[
 V_0\to V_1\to V_2\to V_3\to V_0                         \tag{1.7}
\]

and the reverse cycle.

#### Proof

Equations (1.1)--(1.3) verify legality of every atom.  Distinctness in
each of the four typed resource shores is immediate from the displayed
active-coordinate patterns.  Reversal changes only the typed tail/head
assignment and leaves (1.6) fixed.  Equation (1.7) follows from the atom
order. \(\square\)

## 2. Open the seam

Omit

\[
 s^+=(L_0,U_0;V_0,V_1)\quad\hbox{from }\mathcal C^+,
\]

and

\[
 s^-=(L_0,U_0;V_1,V_0)\quad\hbox{from }\mathcal C^-.
\tag{2.1}
\]

Write the remaining three-atom phases as `R+` and `R-`.  They use the
same lower and upper resources

\[
                         \{L_1,L_2,L_3\},
 \qquad                  \{U_1,U_2,U_3\}.                  \tag{2.2}
\]

Their typed holes are

\[
\begin{array}{c|cc}
 &\hbox{missing tail}&\hbox{missing head}\\ \hline
\mathcal R^+&V_0&V_1\\
\mathcal R^-&V_1&V_0.
\end{array}                                                  \tag{2.3}
\]

Thus (2.1) is a genuine common seam interface: the same `L_0,U_0` closes
either phase, with opposite typed orientation.

For an atom `a=(L,U;T,H)`, use the projections

\[
 \pi_-(a)=(L,T),\qquad \pi_0(a)=(T,H),\qquad
 \pi_+(a)=(H,U).                                           \tag{2.4}
\]

### Theorem 2.1 (one attachment and two predecessor returns)

The symmetric-difference overlay of the two open phases has the following
literal components.

The head--owner attachment projection is the single six-edge path

\[
 V_0-U_3-V_3-U_2-V_2-U_1-V_1.                             \tag{2.5}
\]

The lower--tail projection is the single six-edge path

\[
 V_0-L_3-V_3-L_2-V_2-L_1-V_1.                             \tag{2.6}
\]

On typed tail and head copies, the predecessor projection is the disjoint
union of the two three-edge paths

\[
 V_0^- - V_3^+ - V_2^- - V_1^+,                           \tag{2.7}
\]

\[
 V_1^- - V_2^+ - V_3^- - V_0^+.                           \tag{2.8}
\]

In particular, (2.5) is one attachment return, while (2.7)--(2.8) are the
two crossed predecessor-parity returns exported by an opened even rolling
reset.  Unlike three private hex corridors, all three are projections of
the same three old and three new literal atoms.

#### Proof

The old physical edges are

\[
                         V_1\to V_2,quad
                         V_2\to V_3,quad
                         V_3\to V_0,
\]

and the new ones are their reversals.  Projecting these six atoms via
(2.4) gives (2.5)--(2.8) directly.  Each internal projection vertex has
degree two and each displayed endpoint has degree one, so there are no
additional components. \(\square\)

## 3. Internal all-width and residence guards

The three old edges form the middle-owner word

\[
                         P^+=(V_1,V_2,V_3,V_0),             \tag{3.1}
\]

while the three new edges form

\[
                         P^-=(V_0,V_3,V_2,V_1)
                              =\operatorname{rev}(P^+).     \tag{3.2}
\]

### Theorem 3.1 (internal interval-OR transparency)

For every width `ell=1,2,3,4`, the multisets of internal contiguous unions
of width `ell` in `P+` and `P-` agree exactly.  More generally, reversal
gives a value-preserving bijection between *all* internal intervals:

\[
 \bigcup_{j=a}^{b}P_j^+
 =
 \bigcup_{j=3-b}^{3-a}P_j^- .                              \tag{3.3}
\]

#### Proof

Equation (3.2) identifies the two indexed blocks by reversal.  Reversal
maps every interval `[a,b]` to `[3-b,3-a]` and does not change its set
union, proving (3.3). \(\square\)

### Theorem 3.2 (internal residence invariance)

For every coordinate `c`, its binary trace across `P-` is the reverse of
its trace across `P+`.  Hence the complete run-length multiset agrees,
including the lengths of all internal positive and zero runs.  Any linear
residence/run-length condition imposed solely on this four-owner block and
invariant under exchanging its two ends holds in one phase if and only if
it holds in the other.

#### Proof

Membership of `c` in (3.2) is obtained by reversing the four membership
bits in (3.1).  Reversal preserves run lengths and swaps the two boundary
runs. \(\square\)

### Corollary 3.3 (the raw square is not strictly resident)

The trace of the private coordinate \(w\) on \(P^+\) is

\[
                              0,1,1,0.
\]

It therefore has an internal positive run of length two.  Under the
repository's strict depth-\(d\) convention the minimum internal positive
run is \(d+1\), so the uncollared square fails residence for every
\(d\ge2\).  Theorem 3.2 says that both phases fail in the same way; it does
not make either phase resident.

These are **internal** guard theorems.  An interval crossing from this
block into an ambient word, or a coordinate run joined to an exterior run,
need not be preserved.  That exterior collar is an explicit remaining
gate in Section 6.

## 4. Sharp support minimality

Call two size-`s` states an **orientation-flip trade through**

\[
 e=(L,U;E,F),\qquad e^{\rm op}=(L,U;F,E)                   \tag{4.1}
\]

if both states are four-resource matchings, have identical lower, upper,
tail and head resource sets, the old state contains `e`, and the new state
contains `e^op`.

### Lemma 4.1 (Johnson common-neighbour dichotomy)

Let `E` and `F` be adjacent rank-`m` sets, with

\[
                         L=E\cap F,qquad U=E\cup F.
\]

Every third rank-`m` set `A` adjacent to both `E` and `F` has exactly one
of the following forms:

1. **common lower:** `A=L+c` for some `c` outside `U`, and
   `A cap E=A cap F=L`;
2. **common upper:** `A=(L-b)+ (E-L)+(F-L)` for some `b in L`, and
   `A union E=A union F=U`.

Thus every Johnson triangle has either one common immediate-lower colour
or one common immediate-upper colour.

#### Proof

Write `E=L+p` and `F=L+q`.  If `A` contains neither `p,q`, adjacency to
both forces `L subset A`, giving case 1.  If `A` contains both, adjacency
forces `|A cap L|=m-2`, giving case 2.  If it contains exactly one of
`p,q`, the two intersection ranks with `E,F` differ, so it cannot be
adjacent to both. \(\square\)

### Theorem 4.2 (no support at most three)

There is no orientation-flip trade of support two or three.

#### Proof

At support two, equality of the typed tail and head resource sets forces
the other old atom to be `F->E`, namely `e^op`.  It repeats both `L` and
`U` with `e`, contradicting the matching condition.

At support three, write the common tail set as `{E,F,A}` and the common
head set as `{F,E,B}`.  In the old phase, `E->F` is selected.  The
remaining matching cannot use `F->E`, since that would again repeat `L,U`;
therefore it must contain

\[
                         F\to B,qquad A\to E.              \tag{4.2}
\]

In the new phase, `F->E` is selected, so the remaining two atoms must be

\[
                         E\to B,qquad A\to F.              \tag{4.3}
\]

Hence `A` is adjacent to both `E` and `F`.  By Lemma 4.1 it either shares
the seam lower colour `L` on both edges or shares the seam upper colour
`U` on both edges.  Then (4.2) repeats that colour with `e` in the old
state, and (4.3) repeats it with `e^op` in the new state.  Either way one
phase is not a four-resource matching. \(\square\)

### Corollary 4.3 (support four is minimal)

The square (1.4)--(1.5) is a support-four orientation-flip trade, and
Theorem 4.2 excludes every smaller support.  Thus four is sharp.

There is also a useful parity separation from the standard ternary Boolean
hex.  A forward ternary hex fixes the attachment matching, and its literal
reverse changes attachment by a three-cycle.  Every product of such
match-closed ternary toggles has even attachment parity.  The square changes
attachment by a four-cycle, which is odd.  Therefore this orientation flip
is not a hidden composition of ternary-hex switches inside the same fixed
four-resource fibre.

## 5. Relation to the `q`-gon calculation

The Boolean `q`-gon has the correct abstract reset permutation signature,
but its reflected reversed stage and forward stage meet on opposite
orientations of the same intermediate edges.  The naive serial history is
a closed doubleton and repeats owners.  The square avoids this failure by
making the opposite seam orientations **alternative closures of one
support-four trade**, not simultaneous private stages.

Thus the new macro is the smallest literal central answer to the earlier
three-private-corridor no-go.  It does not require a `q`-long role-conversion
palette merely to realize the three boundary projections.

## 6. Exact scope: what remains open

The theorem proves only the occurrence-resolved central four-resource and
internal-block statements above.  It does **not** yet prove any of the
following.

1. **Guarded word planting.**  No theorem here embeds `P+` and `P-` at one
   common location of a full carrier with the same exterior chronology.
2. **Exterior residence.**  The internal coordinate traces reverse, but
   their boundary runs may merge differently with exterior runs.
3. **Exterior arbitrary-width upper transparency.**  Internal interval
   unions agree at every width, but intervals crossing either packet
   boundary can change.
4. **Depth-`d` flag realization.**  No common suffix/age table or legal
   erosion envelope is supplied.
5. **Compiler/common cap.**  Equality of immediate lower colours does not
   give a common occurrence-labelled lower matching, and no terminal Hall
   theorem is asserted.
6. **Global reset splice.**  The square endpoints still must be identified
   with the opened reset endpoints inside one resource-simple ambient host;
   the contracted residual hosts and all protected tickets must agree.
7. **Global topology or optimum.**  The packet alone proves neither a
   Hamilton carrier, a `k=17` word, nor `nu(k)<=B(k)+O(1)`.

The exact next lemma is a **guarded square planting theorem**: place this
minimal open macro so that its exterior crossing intervals and boundary
coordinate runs agree in the two phases, while carrying one common terminal
compiler matching.

## 7. Independent H100 `-O3` replay

Two independent C++ audits accompany the theorem.

`scratch/audit_boolean_johnson_square_open_return_macro_20260801.cpp`
constructs the square for every `2<=m<=20`, verifies all four resource
palettes, the one attachment path, the one lower--tail path, the two
predecessor paths, and the Johnson common-neighbour dichotomy.

`scratch/audit_boolean_orientation_flip_trade_min_support_20260801.cpp`
independently enumerates the complete `m=3` Boolean-diamond atom universe.
It exhausts supports two and three and finds the displayed square first at
support four.

The H100 commands were

```text
g++ -std=c++20 -O3 -Wall -Wextra -pedantic \
  scratch/audit_boolean_johnson_square_open_return_macro_20260801.cpp \
  -o /dev/shm/audit_boolean_johnson_square_open_return_macro_20260801
/dev/shm/audit_boolean_johnson_square_open_return_macro_20260801

g++ -std=c++20 -O3 -DNDEBUG \
  scratch/audit_boolean_orientation_flip_trade_min_support_20260801.cpp \
  -o /dev/shm/audit_boolean_orientation_flip_trade_min_support_20260801
/dev/shm/audit_boolean_orientation_flip_trade_min_support_20260801 3 4
```

The frozen outputs are

```text
PASS_BOOLEAN_JOHNSON_SQUARE_OPEN_RETURN m=2..20 palettes=exact
full_phases=opposite_C4 open_attachment=path6
open_lower_tail=path6 open_predecessor=path3+path3
internal_OR=all_widths traces=reversed
support3_common_neighbour_dichotomy=PASS

m=3 atoms=180 candidates=150
NO support=2 oldstates=150 newtries=0
NO support=3 oldstates=9220 newtries=128
FOUND support=4
```

Full transcripts are in

* `scratch/audit_boolean_johnson_square_open_return_macro_20260801.out`;
* `scratch/audit_boolean_orientation_flip_trade_min_support_20260801.out`.
