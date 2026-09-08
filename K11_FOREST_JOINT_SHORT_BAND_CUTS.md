# New globally valid rank-five/rank-six band cuts for `k=11,n=465`

## Status

This note proves five additional necessary inequalities for the exact
unrestricted forest/band solver.  They are independent of the fixed-row
ansatz and are not yet implemented in `k11_forest_sat.cpp`.

Let

```text
x_j = number of selected rank-six witnesses of width j,  0<=j<=3,
y_j = number of selected rank-five witnesses of width j,  0<=j<=2.
```

Here width means `right-left`, so physical length is width plus one.  The new
cuts are

\[
\boxed{x_0\le1},                                        \tag{0}
\]

\[
\boxed{y_0+x_0\le135},                                  \tag{1}
\]

\[
\boxed{y_1+2y_2\ge549+4x_0},                            \tag{2}
\]

and the genuinely coupled short-pool cut

\[
\boxed{x_0+x_1+y_0+y_1\le380}.                          \tag{3}
\]

Endpoint nesting also gives

\[
\boxed{x_0+x_1\le y_0+3},
\qquad
\boxed{x_0+x_1+x_2\le y_0+y_1+3}.                     \tag{4}
\]

Finally, total central width satisfies

\[
\boxed{(x_1+2x_2+3x_3)-(y_1+2y_2)\ge455}.             \tag{4b}
\]

Equivalently, because `y_0+y_1+y_2=462`, (2)--(3) say

\[
 y_2\ge y_0+87+4x_0,
 \qquad
 y_2\ge x_0+x_1+82.                                    \tag{4a}
\]

The arithmetic checker is
`scratch/verify_k11_forest_joint_short_cuts.cpp`.

## 1. The two rank-five fan cuts

Choose one witnessing interval for every rank-five mask and sort those 462
intervals by left endpoint.  The unrestricted band theorem gives

\[
 I_i=[i+\alpha_i,i+\beta_i],\qquad
 0\le\alpha_i\le\beta_i\le3.
\]

Every selected rank-five witness has physical length at most three, since an
interval of length at least four contains a selected rank-six witness.
Therefore its width is at most two and the only counts are `y_0,y_1,y_2`.

Every witness of a mask of rank at most four avoids containing a complete
selected rank-five interval.  Apply the exact fan-capped avoidance theorem to
the rank-four antichain.  Its size is 330 and its chain height is one, while
the endpoint slack is `D=3`.  Hence

\[
 330\le\sum_i\min(w_i,1)+3
     =(462-y_0)+3,
\]

which first gives `y_0<=135`.

Now apply the same theorem to the complete nonzero ideal of ranks one through
four.  It contains

\[
 {11\choose1}+{11\choose2}+{11\choose3}+{11\choose4}
 =11+55+165+330=561
\]

masks and has chain height four.  Since every rank-five width is at most two,

\[
 561\le\sum_i\min(w_i,4)+4D
     =y_1+2y_2+12.
\]

This first gives `y_1+2y_2>=549`.  Section 2 sharpens both inequalities when
`x_0=1`.  No central-row or Johnson-path property has been used.

## 2. Omitted-endpoint sums sharpen `x_0<=3` to `x_0<=1`

Let `O_L` and `O_R` be the positions omitted respectively by the 462 selected
rank-five left endpoints and right endpoints.  Both sets have cardinality
three.  Since the occupied endpoint sets are the complements of `O_L,O_R`
inside `{0,...,464}`, summing all selected rank-five widths gives the exact
identity

\[
 \sum_i w_i
 =\sum_i(r_i-l_i)
 =\sum_{p\in O_L}p-\sum_{p\in O_R}p.              \tag{5}
\]

Now take a selected rank-six singleton witness `[p,p]`.  Position `p` cannot
be a selected rank-five left endpoint: an interval of rank five with the same
left endpoint would either equal `[p,p]` or contain it, in either case forcing
an impossible containment between a six-set and a five-set.  The same
argument applies at the right endpoint.  Hence every rank-six width-zero
witness contributes a distinct position to `O_L intersect O_R`, and

\[
 |O_L\cap O_R|\ge x_0.                              \tag{6}
\]

If two three-element subsets of `{0,...,464}` have `c` common elements, the
common contributions cancel in (5).  With `q=3-c`, the largest possible
difference of their sums is obtained by taking the `q` largest positions on
the left and the `q` smallest on the right:

\[
 \sum O_L-\sum O_R\le q(465-q).                    \tag{7}
\]

Combining (5)--(7) with `c>=x_0` gives the useful finite inequality

\[
 y_1+2y_2\le (3-x_0)(462+x_0).                     \tag{8}
\]

For `x_0>=2`, the right side is at most `1*464=464`, contradicting the
proved lower bound `y_1+2y_2>=549`.  Therefore

\[
 \boxed{x_0\le1}.                                   \tag{9}
\]

This strictly improves the currently encoded `x_0<=3`.  In the existing
rank-six boundary notation it merely changes

```text
b1 + 459 <= b6
```

to

```text
b1 + 461 <= b6,
```

so it requires no new variables or circuit topology.

There is a further fan refinement.  If `[p,p]` is a selected rank-six
singleton, then no witness of rank at most four can end at `p`: every such
interval contains the rank-six array entry at `p`.  The position `p` is one of
the three rank-five right-endpoint omissions, but its free-endpoint
contribution to the fan-capped theorem is therefore zero rather than the
generic chain-height cap.

For the rank-four antichain this removes `x_0` from the three free endpoint
units and gives

\[
 330\le(462-y_0)+(3-x_0),
 \qquad\hbox{so}\qquad y_0+x_0\le135.              \tag{9a}
\]

For the complete rank-one-through-four ideal, each such endpoint removes four
units of free fan capacity:

\[
 561\le y_1+2y_2+4(3-x_0),
\]

or

\[
 y_1+2y_2\ge549+4x_0.                              \tag{9b}
\]

These are the sharpened cuts (1)--(2).  Because `x_0<=1`, their only extra
case is transparent: if `x_0=1`, then `y_0<=134` and
`y_2>=y_0+91`.

## 3. Cross-layer cumulative nesting

For `t in {0,1,2}`, consider the selected rank-six intervals of width at most
`t`.  Their left endpoints are distinct, and the selected rank-five left
endpoint set omits only three physical positions.  Therefore at least

\[
 x_0+x_1+\cdots+x_t-3
\]

of these endpoints are shared with selected rank-five intervals.

At a shared left endpoint, the rank-five interval is a proper prefix of the
rank-six interval.  It cannot contain the rank-six interval, because that
would force a six-set to be contained in a five-set; equality is impossible
for the same reason.  Hence a shared rank-six interval of width at most `t`
is paired injectively with a rank-five interval of width at most `t-1`.
It follows that

\[
 \sum_{j=0}^{t}x_j\le3+\sum_{j=0}^{t-1}y_j.       \tag{10}
\]

For `t=0` this recovers the weaker `x_0<=3`.  The two nontrivial cases are

\[
 x_0+x_1\le y_0+3,
 \qquad
 x_0+x_1+x_2\le y_0+y_1+3.                       \tag{11}
\]

The second is equivalently `y_2<=x_3+3`.  The same inequalities follow from
right endpoints, but at the profile level that duplicate information gives
no stronger scalar bound.

There is also a useful summed nesting corollary.  Directly, if `d` is the
number of selected rank-six left endpoints not used by the selected rank-five
row, then `d<=3`, there are `462-d` common endpoints, and there are `d`
rank-five-only endpoints.  Every common endpoint contributes a width
difference at least one, rank-six-only widths are nonnegative, and
rank-five-only widths are at most two.  This already gives

\[
 \sum_i w_i^{(6)}-\sum_i w_i^{(5)}
 \ge (462-d)-2d
 =462-3d\ge453.                                    \tag{12}
\]

In profile notation this is exactly

\[
 (x_1+2x_2+3x_3)-(y_1+2y_2)\ge453.                \tag{12a}
\]

The right-endpoint matching independently yields the same scalar inequality.
The new profile cuts sharpen it by two.  Summing `x_0<=1` and the two
inequalities (11) gives

\[
 3x_0+2x_1+x_2\le2y_0+y_1+7.
\]

Using `sum x_j=sum y_j=462`, this is exactly

\[
 (x_1+2x_2+3x_3)-(y_1+2y_2)\ge455.                \tag{12b}
\]

Thus the 455 inequality is a compact regression consequence of the stronger
cumulative cuts, not an additional independent constraint.

Together, the first inequality in (11) and (2) imply

\[
 y_2\ge y_0+87\ge x_0+x_1+84,
\]

so the short-pool inequality (3) is numerically redundant after all the new
cuts are installed.  It remains valuable as an independent theorem and as a
regression check on any future encoding.

## 4. Two elementary short-witness lemmas

The array may be assumed zero-free.  In fact a zero entry in a length-465
candidate could be deleted while preserving all nonzero interval ORs,
contradicting the proved lower bound 465.

Every rank-one mask has a singleton witness: every nonzero entry of an
interval whose OR is `{a}` equals `{a}`.

Every rank-two mask has a witness of physical length at most two.  Let its
bits be `a,b`.  If a witnessing interval contains an entry `{a,b}`, that entry
is a singleton witness.  Otherwise every entry in the interval is `{a}` or
`{b}`.  Both values occur, so somewhere the word changes between them; that
adjacent pair has OR `{a,b}`.

Thus all 11 rank-one masks and all 55 rank-two masks consume distinct slots
from the singleton/adjacent-pair pool.

## 5. Forced short rank-three and rank-four witnesses

The endpoint-crossing theorem in
`K11_FOREST_RANK3_SHADOW_REDUCTION.md` proves that at least 159 of the 165
rank-three masks have a witness of physical length at most two.

The already-audited adjacent-shadow theorem proves that at least 324 of the
330 rank-four masks have a witness of physical length at most two.

Both statements hold simultaneously for arbitrary witness choices against
the same selected rank-five row: each is a direct endpoint-set
inclusion-exclusion theorem, not an existential choice of a specially
favourable row.

Consequently lower ranks already require at least

\[
 11+55+159+324=549                               \tag{13}
\]

distinct physical singleton or adjacent-pair intervals.

## 6. The joint short-pool inequality

There are exactly

\[
 465+464=929                                     \tag{14}

\]

physical intervals of length one or two.

Among the selected central witnesses, precisely `y_0+y_1` rank-five
intervals and `x_0+x_1` rank-six intervals lie in this pool.  They are all
distinct from one another and from the 549 lower witnesses in (5): a physical
interval has a unique OR value, while all these selected targets are distinct
and have different ranks where appropriate.

Counting them in (14) gives

\[
 549+(y_0+y_1)+(x_0+x_1)\le929,
\]

which proves (3).

This proof is global.  In particular, it does not assume that all selected
rank-six witnesses are four-windows or that either central forest is
connected.

## 7. Relation to the existing rank-six boundary circuit

With the existing rank-six band cuts enabled, its schedule lies on

```text
00, 01, 02, 03, 13, 23, 33
```

and the current note's `b_2,b_5` notation gives

\[
 x_0+x_1=b_2+462-b_5.
\]

Therefore the coupled cut can also be written

\[
 y_2+b_5-b_2\ge544.                              \tag{15}

\]

For rank five, state `03` is already forbidden.  Every monotone rank-five
schedule extends to one of the four maximal chains

```text
00 01 02 12 13 23 33
00 01 02 12 22 23 33
00 01 11 12 13 23 33
00 01 11 12 22 23 33.
```

The last chain has no width-two state and is ruled out immediately by (2).
On all chains, `y_0` counts states `00,11,22,33`, while `y_2` counts states
`02,13`.  This permits a small guarded boundary circuit rather than a generic
462-input pseudo-Boolean encoding.  That circuit should be designed and
independently audited before changing the production solver.

### Exact small boundary-circuit sketch

There is a direct extension of the already-audited rank-six circuit.  The
fourth maximal rank-five chain above has no width-two state and violates
`y_2>=y_0+87`, so introduce an exact-one selector only for the first three
chains, call them `A,B,C`.  A selected chain forbids every state outside it.

Use one common family of six transition positions

\[
 0\le h_1\le\cdots\le h_6\le462
\]

for the selected rank-five chain.  The same 463-way one-hot transition
selectors and nine-bit extraction used by `BandCutPlan` are exact here; their
state-order implications are merely guarded by the three-way chain selector.
Let `g_1,...,g_6` be the already-existing rank-six boundaries.  Then

\[
 x_0=g_1+462-g_6,
 \quad x_0+x_1=g_2+462-g_5,
 \quad x_3=g_4-g_3.                                  \tag{16}
\]

The rank-five profile is given by the following exact table.

| selected chain | `y_0` | `y_2` |
|---|---|---|
| A: `00 01 02 12 13 23 33` | `462+h1-h6` | `h3+h5-h2-h4` |
| B: `00 01 02 12 22 23 33` | `462+h1+h5-h4-h6` | `h3-h2` |
| C: `00 01 11 12 13 23 33` | `462+h1+h3-h2-h6` | `h5-h4` |

All necessary comparisons can be written without signed arithmetic.  Besides
the global sharpening

```text
g1 + 461 <= g6,
```

guard the following four rows by the selected chain:

```text
Let e=x0 in {0,1}.

A:
  h1 + 327 + e             <= h6
  h2 + h4 + h1 + 549 + 4e  <= h3 + h5 + h6
  g2 + h6                  <= h1 + g5 + 3
  h3 + h5 + g3             <= h2 + h4 + g4 + 3

B:
  h1 + h5 + 327 + e        <= h4 + h6
  h2 + h1 + h5 + 549 + 4e  <= h3 + h4 + h6
  g2 + h4 + h6             <= h1 + h5 + g5 + 3
  h3 + g3                  <= h2 + g4 + 3

C:
  h1 + h3 + 327 + e        <= h2 + h6
  h4 + h1 + h3 + 549 + 4e  <= h5 + h2 + h6
  g2 + h2 + h6             <= h1 + h3 + g5 + 3
  h5 + g3                  <= h4 + g4 + 3.
```

In each block these are, respectively, `y0+x0<=135`,
`y2>=y0+87+4x0`, `x0+x1<=y0+3`, and `y2<=x3+3` after substituting
the table and (16).  Eleven-bit ripple adders suffice for every side.  Prefix
equality comparators become conditional simply by adding the negated chain
selector to each comparison clause; the arithmetic wires themselves may be
shared.

The total-width cut uses the already-extracted rank-six expression

\[
 W_6=g_4+g_5+g_6-g_1-g_2-g_3
\]

and `W_5=462-y_0+y_2` from the table.  Its comparator is the unsigned
rearrangement

\[
 917+y_2+g_1+g_2+g_3
 \le y_0+g_4+g_5+g_6,                              \tag{17}
\]

again guarded by the selected rank-five chain after substituting its
`y_0,y_2` formulas.

This gives an exact circuit with only three chain selectors, six additional
boundary integers, and a constant number of small adders/comparators.  It
should be implemented behind a new guard and checked against exhaustive
integer boundary profiles before deployment; the present note intentionally
stops at the proved circuit specification.

## 8. Scope

The inequalities are necessary cuts only.  They do not establish SAT or
UNSAT at length 465.  Their purpose is to prune central endpoint profiles in
the globally exact unrestricted solver.  As always, a SAT candidate requires
independent OR verification, while an UNSAT result requires an archived
CNF/proof pair and independent proof checking.
