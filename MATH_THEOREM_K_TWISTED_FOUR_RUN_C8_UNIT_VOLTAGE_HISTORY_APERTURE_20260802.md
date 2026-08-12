# A twisted four-run `C8` unit-voltage role converter (nonminimal)

**Date:** 2026-08-02  
**Status:** unconditional occurrence-labelled quotient construction, exact unit
voltage for every odd modulus, exact immediate cap palettes, and exact
positive/negative internal history.  Ambient host planting, exterior ticket
acceptance, source factorization, upper ranks beyond `q1`, and the terminal
compiler are not claimed.

**Correction.**  This construction is valid but is not minimal.  The local
same-phase support-three orientation-flip obstruction does not exclude a
phase-split quotient triangle.  The latter gives a smaller unit-voltage
`C6`; see
`MATH_THEOREM_K_TWISTED_THREE_RUN_C6_DYADIC_PUMP_AND_HISTORY_APERTURE_20260802.md`.
All former claims in this note that the complete quotient `C6` face is
impossible or that `C8` is first are retracted.  The no-go remains valid
only when the private seam returns to the same physical endpoint phase.

## 0. Result

The same-phase physical Boolean `C6` cannot reverse a private seam while
retaining the four resource palettes.  This is the support-at-most-three
orientation-flip theorem in
`MATH_THEOREM_BOOLEAN_JOHNSON_SQUARE_OPEN_THREE_RETURN_MACRO_20260801.md`,
Theorem 4.2.  It does not cover a quotient triangle whose closing head is a
nonzero translate of its starting root.

The support-four Johnson square can also be made into a genuine pump rather
than a zero-holonomy local square.  Let the cyclic
deck group be `Z_n`, where

\[
                         n=2r-1
\tag{0.1}
\]

is any odd integer.  At history depth `d`, put `h=d+1` and assume

\[
                         r\ge 4h+1 .
\tag{0.2}
\]

There is a rank-`r` quotient Johnson `C4` whose development is one simple
cycle of length `4n`, whose quotient voltage is `+1`, and whose reverse has
voltage `-1`.  The two directed phases form an alternating incidence `C8`.
They use exactly the same **physical occurrence-labelled** lower and upper
palettes, not merely the same orbit names.  Every such colour occurs once.

Every positive coordinate run has length at least `4h` and every zero run
has length at least `4h-1`.  Thus both positive and negative depth-`d`
histories are internally legal.  Cutting one literal physical edge and its
opposite orientation leaves two history-safe paths with the same omitted
lower and upper occurrence.  The omitted oriented edge is the private
closure occurrence.  The correlated completed totals are `+1` and `-1`.
Both are signed powers of two and hence units modulo every odd `n`, including
composite `n`.

Therefore this `C8` is another valid pump, although the twisted three-run
`C6` is smaller and no `C10` is needed for the central fresh-pump row.  What remains
is to plant this quotient `C8` and match its exported endpoint histories to
the admitted domain of the later fixed-`z`, zero-holonomy ticket atlas.

## 1. Four-run base set

Let

\[
                         s=r-4h-1\ge0 .
\tag{1.1}
\]

Around `Z_n`, take a binary cyclic word with four one-run lengths

\[
                 (a_0,a_1,a_2,a_3)
                    =(h,h,h,h+1+s)
\tag{1.2}
\]

and four intervening zero-gap lengths

\[
                 (g_0,g_1,g_2,g_3)
                    =(h,h,h,h+s).
\tag{1.3}
\]

Their sums are `r` and `r-1`; hence they define a rank-`r` set
`A subset Z_n`.  Let `tau(x)=x+1`.  Write `p_i` for the first coordinate of
the `i`th one-run and `q_i` for the first zero immediately after that run.
Then

\[
        A-\tau A=\{p_0,p_1,p_2,p_3\},\qquad
        \tau A-A=\{q_0,q_1,q_2,q_3\}.
\tag{1.4}
\]

For `0<=j<=4`, define

\[
 R_j=
 A-\{p_0,\ldots,p_{j-1}\}
   +\{q_0,\ldots,q_{j-1}\}.
\tag{1.5}
\]

Each step shifts one complete one-run one coordinate to the right.  In
particular

\[
                         R_4=\tau A .
\tag{1.6}
\]

## 2. Quotient voltage and physical topology

Use `R_0,R_1,R_2,R_3` as quotient representatives and the four directed
edges

\[
 R_0\longrightarrow R_1\longrightarrow R_2
       \longrightarrow R_3\longrightarrow \tau R_0 .
\tag{2.1}
\]

The first three gains are zero and the last gain is `+1`.

### Theorem 2.1 (unit-voltage development)

The quotient word (2.1) has voltage `+1`.  Its physical development is

\[
 W_{4t+j}=\tau^tR_j,qquad t\in\mathbb Z_n,quad0\le j<4,
\tag{2.2}
\]

and is one simple directed cycle on `4n` distinct roots.  Complete reversal
uses the same undirected physical edges and has voltage `-1`.

#### Proof

The voltage assertion is read from (2.1).  In every `R_j`, `j<4`, the
fourth one-run is the unique run of length `h+1+s`, and it has not yet been
shifted.  If `tau^uR_i=tau^vR_j`, this unique run forces `u=v`; the prefix
of shifted runs in (1.5) then forces `i=j`.  Thus (2.2) has `4n` distinct
roots.  Since one quotient turn advances the developed phase by one after
four edges and `gcd(n,1)=1`, (2.2) is one cycle.  Reversal negates every
edge gain and hence the total.  \(\square\)

No primality is used.  In particular, `+/-1` is a unit for every odd
composite modulus as well.

## 3. Physical lower and upper occurrences are simple

For edge type `i`, put

\[
                         I_i=R_i-\{p_i\},\qquad
                         U_i=R_i+\{q_i\}.
\tag{3.1}
\]

The developed lower and upper occurrences are respectively
`tau^t I_i` and `tau^t U_i`.

### Theorem 3.1 (exact occurrence-labelled `q1` palettes)

The `4n` sets `tau^t I_i` are pairwise distinct, and the `4n` sets
`tau^t U_i` are pairwise distinct.  Consequently each directed phase uses
one copy of every displayed lower and upper occurrence, and reversal uses
the same physical palettes occurrencewise.

#### Proof

After deleting `p_i`, all four lower signatures have zero-gap vector

\[
                         (h,h,h,h+s+1).
\tag{3.2}
\]

The unique long last gap anchors cyclic phase.  For `i<3`, exactly run `i`
has length `h-1` while run 3 has length `h+1+s`; for `i=3`, the first three
runs have length `h` and the last has length `h+s`.  Thus the anchored
signature recovers `i`, and then `t`.

For the upper signatures, the zero-gap vectors are

\[
\begin{array}{c|c}
i&\text{zero-gap vector}\ \hline
0&(h-1,h,h,h+s)\\
1&(h-1,h-1,h,h+s+1)\\
2&(h,h-1,h-1,h+s+1)\\
3&(h,h,h-1,h+s).
\end{array}
\tag{3.3}
\]

Together with the unique long one-run (or, in the threshold case, the
unique changed last run), these four anchored cyclic signatures are
distinct and have trivial stabilizer.  Hence they recover `i,t`.  Reversal
does not change an undirected edge's intersection or union.  \(\square\)

Thus “cap exact” below is literal physical exactness; it is not an
unweighted quotient-orbit assertion.

## 4. Exact positive and negative histories

At event `4t+i`, the transition deletes and inserts

\[
                       \alpha_{4t+i}=p_i+t,qquad
                       \beta_{4t+i}=q_i+t.
\tag{4.1}
\]

The cyclic coordinate order is

\[
 p_0,q_0,p_1,q_1,p_2,q_2,p_3,q_3.
\tag{4.2}
\]

### Theorem 4.1 (two-sided history acceptance)

Every positive run in `W` has length `4a_i` for one `i`, and every zero run
has length at least

\[
                         \min_i(4g_i-1)=4h-1.
\tag{4.3}
\]

Hence every positive run is at least `4h` and every zero run is at least
`4h-1`.  In particular the event-stream residence and dual-residence tests
hold at depth `d`.

#### Proof

For a fixed coordinate, insertion at boundary `q_i` and the following
deletion at `p_i` are separated by `a_i` developed blocks and have the same
within-block offset.  This gives `4a_i`.  After deletion at `p_i`, the next
insertion is the preceding boundary `q_(i-1)`.  It is separated by
`g_(i-1)` blocks; changing the within-block offset can shorten this by at
most one event (the wrap case lengthens it).  This gives (4.3).  The
run-deficit/event-stream theorem now gives both directed history tests.
\(\square\)

Complete reversal preserves all run lengths.  If one physical edge is cut,
every newly truncated run meets a path endpoint; all remaining internal
runs retain the same lower bounds.  Thus the two opened orientations export
literal positive and negative endpoint histories, related by reversal.

## 5. The correlated cap/history/private-edge tuple

Let `e_*` be the physical closing edge

\[
             \tau^{n-1}R_3\longrightarrow R_0,
\tag{5.1}
\]

and let `e_*^op` be its opposite orientation.  Delete `e_*` from the
forward cycle and `e_*^op` from the reverse cycle.

### Theorem 5.1 (literal accepted pump state)

The two open paths have:

1. the same `4n-1` physical lower occurrences and the same `4n-1` physical
   upper occurrences;
2. branchwise private closure occurrences `e_*` and `e_*^op` carrying the
   one omitted lower/upper pair;
3. no internal positive or zero run shorter than `d+1`;
4. exact reversed positive and negative boundary-history tuples; and
5. completed quotient totals `+1` and `-1` when their own private edge is
   restored.

Regarded as one simultaneous alternating-circuit exchange, the immediate
cap monoid coordinate is

\[
                             (z,b)=(0,0),
\tag{5.2}
\]

because the two phases have identical occurrence-labelled cap sets.  The
full accepted records are correlated branch tuples

\[
 (0,0,\mathcal R^+,e_*,+1),\qquad
 (0,0,\mathcal R^-,e_*^{op},-1).
\tag{5.3}
\]

No cap state, history, edge, or voltage in one tuple is borrowed from the
other.

#### Proof

Items 1--2 follow from Theorem 3.1 and cutting opposite orientations of one
undirected edge.  Item 3 is Theorem 4.1 with clipped endpoint runs.  Item 4
is literal reversal.  Item 5 is Theorem 2.1.  Equality of complete cap
occurrences makes the atomic simultaneous exchange cap-neutral at every
physical cap, proving (5.2).  \(\square\)

The fibre of either fixed oriented private-edge branch contains a signed
power of two.  Hence it passes the finite-holonomy universal-unit criterion
without any cap backup.

## 6. The same-phase `C6` obstruction and why this does not imply minimality

The local no-go is scoped to a same-phase one-aperture interface.  Such an
interface must carry a directed private seam `E->F` in one phase and
`F->E` in the other while keeping its lower/upper pair and the complete
typed resource sets.  The support-three no-go cited in Section 0 is an
occurrence-level Boolean theorem.  It permits arbitrary choices of the
third roots; the Johnson common-neighbour dichotomy forces either the seam
lower or seam upper colour to repeat.  Therefore no complete four-resource
same-phase physical `C6` role converter exists on this face.  A ternary Boolean hex avoids the
repetition only because its complete toggle does **not** reverse the private
seam role: its head--owner attachment columns agree occurrencewise.

The phase-split quotient `C6` in the correction note evades this hypothesis:
its third edge ends at `tau A`, not `A`, and develops to a long physical
cycle rather than a Johnson triangle.  The construction above is support
four, so its two phases form `C8`, and it also exports `+/-1`.  Thus `C10`
is not the first actuator.  A raw
local Johnson square can have zero voltage and short runs; the four-run
twist is the essential quotient ingredient which simultaneously supplies
unit voltage and long histories.

## 7. Exact scope and remaining host row

This theorem closes only the child-native pump packet:

* literal owner/root simplicity inside the developed packet;
* exact occurrence-labelled `q1` palettes;
* one physical cycle in either phase;
* positive and negative internal history;
* one private opening; and
* a signed-dyadic correlated voltage branch.

It does **not** prove:

1. that the `4n` packet roots can be reserved in the global owner factor;
2. that its exported endpoint histories lie in the accepting exterior
   domain of a selected fixed-`z` completed ticket;
3. any source/erosion factorization;
4. any upper coverage beyond the immediate edge-union palette;
5. any exterior cross-window transparency; or
6. any common-cap/compiler matching.

The exact remaining compatibility lemma is therefore an ambient planting
statement: reserve the twisted `C8`, join its two endpoint histories to one
admitted fixed-`z` ticket state, and retain its private closing occurrence.
Once planted, every subsequent zero-holonomy completed ticket preserves the
unit voltage by localization.

## 8. Independent light replay

`scratch/audit_k_twisted_four_run_c8_unit_pump_20260802.py` independently
constructs the development, checks all root/lower/upper occurrences,
computes every coordinate run, and compares the complete forward/reverse
physical palettes.  It passes 48 cases (`1<=d<=12` and four slack values):

```text
PASS_TWISTED_FOUR_RUN_C8 cases= 48
formula n=8(d+1)+1+2*slack; voltage=+1 reverse=-1
last (12, 8, 121, 61, [51, 52])
```
