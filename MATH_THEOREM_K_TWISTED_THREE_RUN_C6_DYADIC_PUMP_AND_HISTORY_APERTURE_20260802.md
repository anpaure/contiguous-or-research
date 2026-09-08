# A twisted three-run quotient `C6` is a literal dyadic fresh pump

**Date:** 2026-08-02  
**Status:** unconditional occurrence-labelled quotient construction, exact
unit voltage for every odd modulus, simple owner/lower/upper development,
and exact positive/negative internal history with a private physical
opening.  Ambient owner-factor planting, exterior history admission, source
factorization, upper ranks beyond `q1`, and the terminal compiler are not
claimed.

## 0. Result and correction to the same-phase `C6` no-go

The same-phase support-three orientation-flip no-go is correct but is not a
quotient `C6` no-go.  It assumes that the third edge returns to the same
physical root.  A phase-split quotient triangle may instead return to a
translate of that root.  Its development is a long physical cycle, not a
physical Johnson triangle, so the common-lower/common-upper triangle
obstruction does not apply.

This distinction yields the requested first actuator.  Let

\[
                         n=2r-1
\tag{0.1}
\]

be any odd modulus, put `h=d+1`, and assume

\[
                         r\ge3h+1 .
\tag{0.2}
\]

There is a rank-`r` quotient Johnson triangle with voltage `+1`.  Its
reverse has voltage `-1`; the two directed phases form an alternating
incidence `C6`.  The physical development of either phase is one simple
cycle on `3n` roots, with `3n` distinct lower occurrences and `3n` distinct
upper occurrences.  Every positive coordinate run has length at least
`3h`, and every zero run has length at least `3h-1`, so both directed
history tests pass at depth `d`.

Cutting one literal physical edge and the opposite edge in the reverse
phase gives two internally history-safe paths with the same omitted
lower/upper occurrence and branchwise private closures.  Their completed
totals are `+1` and `-1`.  Hence a fixed correlated branch contains a
signed power of two and is coprime to every odd modulus, composite or prime.

Thus `C6`, not `C8` or `C10`, is the first possible actuator once a genuine
phase-split endpoint is allowed.  A same-phase physical `C6` remains
impossible on the private-seam orientation-flip face.

## 1. Three-run construction

Let

\[
                         s=r-3h-1\ge0 .
\tag{1.1}
\]

Around `Z_n`, take a rank-`r` set `A` whose cyclic binary trace has one-run
lengths

\[
                    (a_0,a_1,a_2)=(h,h,h+1+s)
\tag{1.2}
\]

and intervening zero-gap lengths

\[
                    (g_0,g_1,g_2)=(h,h,h+s).
\tag{1.3}
\]

The sums are `r` and `r-1`.  Let `tau(x)=x+1`, let `p_i` be the first
coordinate of one-run `i`, and let `q_i` be the first zero after that run.
Then

\[
 A-\tau A=\{p_0,p_1,p_2\},\qquad
 \tau A-A=\{q_0,q_1,q_2\}.
\tag{1.4}
\]

Define

\[
 R_j=A-\{p_0,\ldots,p_{j-1}\}
          +\{q_0,\ldots,q_{j-1}\},qquad0\le j\le3.
\tag{1.5}
\]

Each step shifts one full one-run one coordinate to the right, and

\[
                              R_3=\tau A .
\tag{1.6}
\]

## 2. Voltage and one physical cycle

Use `R_0,R_1,R_2` as quotient representatives and take the directed edges

\[
              R_0\longrightarrow R_1\longrightarrow R_2
                    \longrightarrow\tau R_0 .
\tag{2.1}
\]

### Theorem 2.1 (literal `+1/-1` development)

The quotient cycle (2.1) has voltage `+1`.  Its development

\[
 W_{3t+j}=\tau^tR_j,qquad t\in\mathbb Z_n,quad0\le j<3,
\tag{2.2}
\]

is one directed cycle on `3n` distinct physical roots.  Its complete
reversal has voltage `-1` and is the same physical cycle with the opposite
orientation.

#### Proof

The first two edges of (2.1) have gain zero and the closing edge has gain
one.  In each chosen representative `R_j`, the third one-run is the unique
run of length `h+1+s` and has not yet been shifted.  Thus an equality
`tau^uR_i=tau^vR_j` first forces `u=v` by the unique long-run position, and
then forces `i=j` by the prefix of shifted runs.  Hence all `3n` roots are
distinct.  The phase advance after one quotient circuit is `+1`, so the
number of developed components is `gcd(n,1)=1`.  Reversal negates the
voltage.  \(\square\)

This proof is unchanged when `n` is composite.

### Corollary 2.2 (the two quotient matchings form one `C6`)

On typed quotient tail and head copies, the forward phase sends root class
`i` to `i+1`, while the reverse phase sends it to `i-1`, with indices in
`Z_3`.  Their union is therefore one alternating `C6`.  On physical typed
occurrences, the analogous overlay is one alternating cycle of length
`6n`.

#### Proof

The union of two perfect matchings is controlled by their relative
permutation.  On quotient classes that permutation advances by two in
`Z_3`, hence is one 3-cycle and gives one alternating `C6`.  On the physical
cycle of length `3n`, it advances by two.  Since `3n` is odd,
`gcd(3n,2)=1`, so there is one physical alternating component.  \(\square\)

## 3. Exact occurrence-labelled immediate palettes

Put

\[
                         I_i=R_i-\{p_i\},\qquad
                         U_i=R_i+\{q_i\}.
\tag{3.1}
\]

The physical lower and upper occurrences of edge type `i` are
`tau^tI_i` and `tau^tU_i`.

### Theorem 3.1 (simple lower and upper palettes)

All `3n` developed lower occurrences are distinct, and all `3n` developed
upper occurrences are distinct.  The forward and reverse phases use these
same physical occurrences exactly once.

#### Proof

After deleting `p_i`, all three lower signatures have zero-gap vector

\[
                         (h,h,h+s+1).
\tag{3.2}
\]

Its unique last long gap anchors cyclic phase.  For `i=0,1`, precisely
run `i` has length `h-1` while the last run has length `h+1+s`; for `i=2`,
the first two runs have length `h` and the last has length `h+s`.  Thus the
signature recovers `i` and then the phase.

For the upper colours, the zero-gap vectors are

\[
\begin{array}{c|c}
i&\text{zero-gap vector}\\ \hline
0&(h-1,h,h+s)\\
1&(h-1,h-1,h+s+1)\\
2&(h,h-1,h+s).
\end{array}
\tag{3.3}
\]

Together with the one-run lengths after extending run `i`, these are three
distinct anchored cyclic signatures with trivial stabilizer.  Reversal
changes no physical edge intersection or union.  \(\square\)

Therefore every cap statement below is literal and occurrence-labelled;
it is not merely an equality of unweighted quotient orbits.

## 4. Exact two-sided history

At event `3t+i`, the edge deletes and inserts

\[
                     \alpha_{3t+i}=p_i+t,qquad
                     \beta_{3t+i}=q_i+t.
\tag{4.1}
\]

The coordinate boundary order is

\[
                         p_0,q_0,p_1,q_1,p_2,q_2.
\tag{4.2}
\]

### Theorem 4.1 (positive and negative history acceptance)

Every positive run in `W` has length `3a_i` for one `i`, and every zero run
has length at least

\[
                         \min_i(3g_i-1)=3h-1.
\tag{4.3}
\]

Thus every positive run is at least `3h` and every zero run at least
`3h-1`; both event-stream history tests hold at depth `d`.

#### Proof

For a fixed coordinate, insertion at `q_i` and the following deletion at
`p_i` are `a_i` developed blocks apart and have the same within-block
offset, giving `3a_i`.  From deletion at `p_i` to the next insertion at the
preceding `q_(i-1)` there are `g_(i-1)` blocks; the within-block offset can
shorten this by at most one event.  This proves (4.3), and the exact
run-deficit/event-stream identities give the two directed history tests.
\(\square\)

Reversal preserves every cyclic run.  After cutting one edge, every run
affected by the cut is an endpoint-clipped run; all internal runs retain
the same bounds.

## 5. Full occurrence-labelled accepted branch

Let

\[
                    e_*:\tau^{n-1}R_2\longrightarrow R_0
\tag{5.1}
\]

be one literal physical closing edge, and let `e_*^op` be its opposite
orientation.  Cut these from the forward and reverse cycles respectively.

### Theorem 5.1 (correlated cap/history/private-edge fibre)

The two open paths have the same `3n-1` physical lower occurrences and the
same `3n-1` physical upper occurrences.  They export exact reversed
positive and negative endpoint histories, and their private closures are
respectively `e_*` and `e_*^op`, carrying the one omitted lower/upper pair.
Restoring their own closure gives completed totals `+1` and `-1`.

As one atomic simultaneous alternating-circuit exchange, the cap signature
is

\[
                              (z,b)=(0,0).
\tag{5.2}
\]

The two non-mixed accepted records are

\[
 (0,0,\mathcal R^+,e_*,+1),\qquad
 (0,0,\mathcal R^-,e_*^{op},-1).
\tag{5.3}
\]

In particular each fixed oriented-private-edge fibre contains a signed
power of two.

#### Proof

The palette statement is Theorem 3.1 after removing opposite orientations
of one undirected physical edge.  The history assertion follows from
Theorem 4.1 and clipping.  The voltage assertion is Theorem 2.1.  The full
physical cap sets agree occurrencewise, so the atomic exchange has zero
terminal cap current and no artificial prefix debt.  Every entry in each
tuple comes from the same literal branch.  \(\square\)

The tuple is internally accepted.  Its endpoint histories are explicit,
but an ambient fixed-`z` ticket must still be chosen whose exterior history
domain contains them; this is a planting/interface theorem, not part of
the local packet.

## 6. Exact relation to the local triangle obstruction

If the closing gain in (2.1) is forced to zero, the three quotient roots
form a physical Johnson triangle.  The Johnson common-neighbour dichotomy
then forces either a repeated lower or repeated upper colour, so an exact
private-seam orientation converter is impossible.  Here the closing head
is `tau R_0`, not `R_0`; the physical component has length `3n` and has no
triangle.  This is precisely the phase-split occurrence which the local
support-three theorem does not cover.

The standard ternary Boolean hex is a different zero-gain `C6`: its
complete head--owner attachment columns agree occurrencewise, so it is not
this role converter.  The present twisted quotient `C6` changes the global
orientation of a developed cycle and carries the nonzero phase at its
private closure.

## 7. Scope and remaining fixed-`z` interface

The theorem closes the local fresh-pump rows:

* quotient support three / alternating incidence `C6`;
* one physical developed cycle;
* simple physical owner, lower and upper occurrences;
* a branchwise private aperture;
* positive and negative internal history; and
* a universally coprime completed total.

It does not prove:

1. protected reservation of the `3n` roots in a global owner factor;
2. acceptance of the exported endpoint histories by a selected exterior
   fixed-`z` completed ticket;
3. source/erosion factorization;
4. upper coverage beyond the edge-union row;
5. exterior cross-window transparency; or
6. terminal common-cap/compiler matching.

Once the ambient interface in items 1--2 is proved, all later fixed-`z`
zero-holonomy repairs preserve this `+/-1` seed by voltage localization.

### Corollary 7.1 (exact product-monoid compatibility)

Fix the `+1` branch and write its local protected state as

\[
              \Sigma_0=(z_0,b_0,\mathcal R_0,e_*,v_0)
                       =(0,0,\mathcal R^+,e_*,1).
\tag{7.1}
\]

Let `T_1,...,T_H` be completed fixed-`z` tickets, each disjoint from the
private occurrence `e_*`, each topology-safe on the current one-cycle
factor, and each of zero seam displacement.  Write their cap/history
states as \((z_i,b_i,\mathcal R_i)\).  Then their protected product has

\[
\begin{aligned}
 v_{0\cdots H}&=1,\\
 z_{0\cdots H}&=\sum_{i=1}^H z_i,\\
 b_{0\cdots H}&=b_1\star\cdots\star b_H,\\
 \mathcal R_{0\cdots H}
   &=\mathcal R_H\circ\cdots\circ\mathcal R_1
        \circ\mathcal R_0,
\end{aligned}
\tag{7.2}
\]

where `star` is the exact cap-prefix composition law.  In particular, if
all later tickets are cap-neutral with zero prefix debt and the composed
history relation accepts the exported endpoint state, the unit seed,
cap state, and private closure survive unchanged through all `H` repairs.

#### Proof

Zero seam displacement preserves voltage at every serial prefix.  The cap
and history coordinates compose by the protected product-monoid theorem,
and disjointness retains `e_*`.  \(\square\)

This corollary is conditional exactly where it should be: the present
construction supplies the explicit state \(\mathcal R_0\), but it does not
prove that a positive-density fixed-`z` exterior atlas admits that state.
The ambient cap/history socket is the remaining interface, not another
voltage pump.

## 8. Independent light replay

`scratch/audit_k_twisted_three_run_c6_unit_pump_20260802.py` reconstructs
the packet from the formulas and checks roots, every physical lower/upper
occurrence, every coordinate run, and reversal counters.  It passes 64
cases (`1<=d<=16`, slack `0,1,3,8`):

```text
PASS_TWISTED_THREE_RUN_C6 cases= 64
formula n=6(d+1)+1+2*slack; voltage=+1 reverse=-1
last (16, 8, 119, 60, [50, 51])
```
