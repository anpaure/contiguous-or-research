# Independent audit of `NONCANONICAL_TRIANGULAR_BRAID.md`

## Verdict

The principal arguments are correct.

* The peak-edge incidence identity is exact.
* The lower bounds on peak--peak edges and peak/nonpeak portals are valid for
  unrestricted witnesses over the triangular alphabet.
* The nested-ceiling arithmetic in the linear excess theorem is correct.
* The portal two-chain-grid normal form is exact.
* The fixed-`u` three-provider gadget covers every positive-height target,
  including all boundary cases `u=0`, `u=1`, and `u=R-1`.
* For `R>=2`, the literal concatenation of all gadgets plus the peak spine
  has length exactly `(3R^2+R)/2`.
* The displayed `R=3,4,5` words contain every triangular cell and exhaustively
  cover all `14,30,55` targets.

There are two scope corrections.

1. At the degenerate value `R=1`, the literal gadget-plus-spine procedure
   has length three, whereas `(3R^2+R)/2=2`.  There are no positive-height
   targets, so one should omit `G_0` and use only the two-point peak spine.
   The formula and proof are exact for `R>=2`, including every intended
   asymptotic case.
2. The three-provider concatenation covers the entire **target family**, but
   it need not contain every triangular cell.  For example, when `R=4`, the
   cell `E_(4,2)` is not emitted by any `G_u`.  Thus it is not a spanning
   word of the type assumed by the repetition lower bound.  The source calls
   it an abstract grid certificate and does not use it as a near-once upper
   bound; any summary calling it a spanning construction would be wrong.

The observed quadratic excess

\[
 \left\lfloor\frac{(R-1)^2}{4}\right\rfloor
\]

remains conjectural.  The strict-interior antichain has that cardinality,
but no injection from its targets to excess occurrences is proved.

## 1. Alphabet and target counts

The triangular alphabet is

\[
 \mathcal T_R=\{P_0\}\cup
 \{E_{s,y}:1\le s\le R,\ 0\le y<s\}.
\]

It has

\[
                    |\mathcal T_R|=1+\sum_{s=1}^{R}s
                    =1+\frac{R(R+1)}2
\]

cells.  Its peaks are exactly `P_0,...,P_R`, so there are `R+1` peak labels.

For fixed upper endpoint `r`, there are `r` choices of `u` and `r` choices
of `x`.  Therefore the number of targets is

\[
                  \sum_{r=1}^{R}r^2
                  =\frac{R(R+1)(2R+1)}6.
\]

This gives `14,30,55` for `R=3,4,5`, as used by the certificates.

All repetition counts in Section 2 assume a **spanning** word over this
alphabet: every cell occurs at least once and there are no outside-alphabet
entries.  If outside entries are allowed, or if unused triangular cells may
be omitted, `P<=R+1+q` no longer has the asserted meaning.

## 2. Zero-height peak edges

For each `i=0,...,R-1`, a witness for

\[
                       [i,i+1]\times\{0\}
\]

contains only height-zero cells, hence only peaks.  Its first-coordinate
minimum and maximum force it to contain both `P_i` and `P_(i+1)` and no peak
label outside `{i,i+1}`.  Walking inside the witness from one label to the
other produces a physical adjacent transition

\[
                         P_iP_{i+1}\quad\text{or}\quad P_{i+1}P_i.
\]

One physical transition has one unordered label pair and therefore cannot
serve two different values of `i`.  Thus the number `a` of peak--peak
physical edges satisfies

\[
                              a\ge R.
\]

Repeated equal-peak adjacencies may contribute to `a` but do not help this
count.  Lemma 1 is exact as a lower bound.

## 3. First positive layer and portal capacity

For `i=1,...,R-1`, a witness for

\[
                         [i,i+1]\times[0,1]
\]

contains a peak to attain minimum height zero and a height-one nonpeak to
attain maximum height one.  It must cross at least one physical portal.

If a portal has labels `P_j` and `E_(s,1)`, containment in this bounding box
forces

\[
                         j,s\in\{i,i+1\}.
\]

If `j!=s`, the unordered pair is `{i,i+1}` and determines `i` uniquely.  If
`j=s`, then `j` can be the lower or upper first-coordinate endpoint, giving
at most `i=j` and `i=j-1` after respecting the boundary range.  Thus one
portal can be assigned to at most two of the `R-1` targets and

\[
                         b\ge\left\lceil\frac{R-1}{2}\right\rceil.
\]

At `i=1` and `i=R-1` one of the two formal equal-label choices may fall
outside the allowed range; this only lowers capacity and does not weaken the
bound.

## 4. Peak-edge incidence identity and rounding

Let `P` be the number of peak occurrences and let `e` be the number of word
endpoints occupied by peaks.  Sum physical degrees over peak occurrences.

* Every internal peak occurrence contributes two and every peak endpoint
  contributes one, giving `2P-e`.
* Every peak--peak edge contributes two, every portal contributes one, and a
  nonpeak--nonpeak edge contributes zero.

Therefore

\[
                            2P-e=2a+b.
\]

Since a spanning word of length `|T_R|+q` has at most `R+1+q` peak
occurrences,

\[
\begin{aligned}
 b&=2P-e-2a\\
  &\le2P-2a\\
  &\le2(R+1+q)-2R=2q+2.
\end{aligned}
\]

Combining this with the portal lower bound gives

\[
 q\ge
 \left\lceil
   \frac{\lceil(R-1)/2\rceil-2}{2}
 \right\rceil.
\]

The elementary identity

\[
                      \left\lceil\frac{R-1}{2}\right\rceil
                      =\left\lfloor\frac R2\right\rfloor
\]

proves the displayed form

\[
 \boxed{
 q\ge
 \left\lceil
   \frac{\lfloor R/2\rfloor-2}{2}
 \right\rceil.
 }
\]

This remains a valid, possibly negative or zero, lower bound at the smallest
`R`.  For `R>=3`, the separately proved exact-once obstruction supplies
`q>=1`.  As `R` grows, the bound is `R/4-O(1)`.

Dropping `e` makes the estimate slightly weaker but never invalid; no hidden
assumption about the word endpoints is made.

## 5. Portal normal form

Every positive-height witness contains a peak and a nonpeak, so it crosses a
portal.  Fix a portal between positions `p,p+1`.  Bounding boxes of intervals
ending at `p` form a nested chain as their left endpoint moves left, and
bounding boxes of intervals starting at `p+1` form a nested chain as their
right endpoint moves right.

For `l<=p<j`, the interval `[l,j]` is the union of the adjacent intervals
`[l,p]` and `[p+1,j]`.  Its bounding rectangle is consequently the
coordinatewise rectangle join

\[
                         L_l\vee R_j.
\]

This proves both directions of Proposition 4.  A universal spanning word
with `q=O(R)` has `b<=2q+2=O(R)` portals, so its target witnesses can be
assigned among `O(R)` such grids.

The word “equivalent” in the discussion is structural: the grids must arise
as the actual left/right interval chains of one physical word.  An abstract
list of arbitrary chain grids is not by itself a word construction.

## 6. Audit of the fixed-`u` gadget

For `0<=u<R`, the left chain is

\[
 L_u=(E_{R,1},E_{R-1,1},\ldots,
       E_{\max(u+1,2),1},P_u).
\]

For `2<=t<=R-1`,

\[
 Q_{u,t}=E_{\max(u,t+1),t}.
\]

This is always legal: its first coordinate is at least `t+1`, and it is at
most `R` because both `u<=R-1` and `t+1<=R`.

### Height one

A positive target with `x=1` necessarily has `r>=2`.  Since `u<r`,

\[
                       r\ge\max(u+1,2),
\]

so `E_(r,1)` appears in `L_u`.  The interval from this term down to `P_u`
has first-coordinate extrema `u,r` and height extrema `0,1`.

### Height at least two

For `2<=x<r`, start at `E_(r,1)`, continue through `P_u`, and end at
`Q_(u,x)`.  The post-peak heights are `2,3,...,x`.  For every such height
`t`,

\[
                      \max(u,t+1)\le r
\]

because `u<r` and `t+1<=x+1<=r`.  All first coordinates lie between `u`
and `r`; the initial provider attains `r`, the peak attains `u`, and the
height providers attain maximum height `x`.  The bounding box is exactly
the target.

### Boundary values of `u`

* `u=0`: positive targets have `r>=2`, and the left chain starts at
  `E_(R,1)` and ends at `E_(2,1),P_0`; every required initial provider is
  present.  For `Q_(0,t)`, the first coordinate is `t+1`.
* `u=1`: again every positive target has `r>=2`; the same column-one chain
  ends at `E_(2,1),P_1`, and `Q_(1,t)=E_(t+1,t)`.
* `u=R-1`: the only possible upper endpoint is `r=R`.  The left chain is
  `(E_(R,1),P_(R-1))`.  For `2<=t<=R-2`,
  `Q_(R-1,t)=E_(R-1,t)`, while
  `Q_(R-1,R-1)=E_(R,R-1)`.  All are at most the required upper endpoint
  `R` and strictly above their heights.

Thus Proposition 5 has no boundary gap.

## 7. Exact gadget length

Assume `R>=2`.  The `Q` tail has exactly `R-2` terms for every `u`.

For `u=0,1`, the column-one part has `R-1` terms and adding `P_u` gives

\[
                         |L_u|=R,qquad |G_u|=2R-2.
\]

For `2<=u<=R-1`, it has `R-u` column-one terms and one peak, so

\[
                         |L_u|=R-u+1,qquad
                         |G_u|=2R-u-1.
\]

Therefore

\[
\begin{aligned}
 \sum_{u=0}^{R-1}|G_u|
 &=2(2R-2)+\sum_{u=2}^{R-1}(2R-u-1)\\
 &=\frac{3R^2-R-2}{2}.
\end{aligned}
\]

Appending the peak spine of length `R+1` gives

\[
 \frac{3R^2-R-2}{2}+R+1
 =\boxed{\frac{3R^2+R}{2}}.
\]

For `R=2`, the sum over `u=2,...,R-1` is empty and the same arithmetic gives
length seven.  At `R=1`, the case split `u=0,1` no longer describes two
values of `u`: the literal gadget consists only of `P_0`, and appending the
two-point spine gives length three.  Since no positive target exists, omit
that redundant gadget and use the spine of length two; this is the value of
the displayed polynomial.

The gadget word is not spanning in general.  For example, `E_(4,2)` is
absent at `R=4`: all height-two `Q` providers have first coordinate
`max(u,3)`, which is at most three unless `u=4`, an inadmissible value.  This
does not affect target coverage because first-coordinate maximum four can be
supplied independently by a column-one provider.

## 8. Strict-interior antichain

At depth `R-1`, write `a=r-u`, so

\[
                          x=R-1-a.
\]

The strict boundary conditions and `x<r` give

\[
 r\ge a+1,qquad r\ge R-a,qquad r\le R-1.
\]

The number of choices is therefore

\[
 R-\max(a+1,R-a)=\min(a,R-1-a).
\]

Summing for `a=1,...,R-2` yields

\[
 \sum_{a=1}^{R-2}\min(a,R-1-a)
 =\left\lfloor\frac{(R-1)^2}{4}\right\rfloor.
\]

Proper containment of bounding boxes strictly increases the depth
`r-u+x`; hence distinct targets at one depth are incomparable.  The family
is indeed an antichain.

What is missing is a charging theorem from these targets to excess physical
occurrences.  Distinct target endpoints need not be repeated letters, and
one repeated letter can change several portal grids.  Equation (5.5) remains
a conjecture, exactly as the source says.

## 9. Independent finite verification

The three displayed certificates were exhaustively checked by enumerating
every contiguous interval, recording its four bounding extrema, and
comparing against every target.  The checker was compiled with `-O3` and run
on the remote Linux worker rather than locally.  Its output was

```text
R=3 n=8 span=1 miss=0
R=4 n=13 span=1 miss=0
R=5 n=20 span=1 miss=0
```

The alphabet sizes are respectively `7,11,16`, so the words have exactly
`1,2,4` excess occurrences.  The target counts are `14,30,55`.  Direct set
comparison also confirms that every triangular cell occurs at least once.

These data certify only the three finite cases.  They establish neither a
recurrence nor the conjectural quadratic lower bound.

## 10. Scope ledger

| Claim | Audit status | Qualification |
|---|---|---|
| `a>=R` zero-layer bound | proved | Requires a spanning word over `T_R`. |
| `b>=ceil((R-1)/2)` portal bound | proved | One portal serves at most two first-positive targets. |
| Incidence identity `2P-e=2a+b` | proved exactly | Includes both endpoint possibilities. |
| Linear repetition lower bound | proved | Nested-ceiling equality is correct. |
| `q>=1` for `R>=3` | inherited and correct | Exact-once triangular permutation obstruction. |
| Portal two-chain-grid normal form | proved | Grids must arise from one physical word. |
| Fixed-`u` gadget | proved | All `u=0,1,R-1` cases checked explicitly. |
| Gadget length `(3R^2+R)/2` | proved for `R>=2` | At `R=1`, omit redundant `G_0` and use the peak spine. |
| Gadget concatenation covers every target | proved | It does not necessarily contain every alphabet cell. |
| Strict-interior antichain size | proved exactly | Does not imply a repetition lower bound. |
| `R=3,4,5` certificates | independently verified | Spanning and zero missing targets. |
| Quadratic excess formula | conjectural | Supported only by the three finite values and antichain cardinality. |
| `|T_R|+O(R)` construction | open | Neither proved nor disproved. |

## 11. Safe handoff statement

The following statement preserves every necessary scope restriction.

> For a spanning word over the triangular alphabet, let `q` be its number of
> repeated occurrences.  Peak-edge incidence and first-positive portal
> capacity give
> \[
> q\ge
> \left\lceil\frac{\lfloor R/2\rfloor-2}{2}\right\rceil
> =R/4-O(1),
> \]
> together with the independent bound `q>=1` for `R>=3`.  This lower bound
> permits arbitrary noncanonical witnesses but does not cover words using
> outside-alphabet entries.

> Every positive-height witness crosses a portal, and each portal supplies a
> join grid of two nested bounding-box chains.  For each fixed lower endpoint
> `u`, the explicit gadget `G_u` realizes every positive-height target with
> that `u`; all `R` gadgets plus a peak spine have length
> `(3R^2+R)/2` for `R>=2`.  This is an abstract target-covering word, not a
> spanning near-once construction.

> The spanning certificates at `R=3,4,5` have excess `1,2,4`.  Their agreement
> with `floor((R-1)^2/4)` is conjectural and supplies no all-`R` lower or upper
> bound.

