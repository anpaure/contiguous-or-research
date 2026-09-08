# Audit of `ROTATING_BRAID_ANALYSIS.md`

## 1. Verdict

The direct-braid argument is mathematically sound under its intended meaning
that successive displayed plateau intervals are disjoint and immediately
consecutive in the word.  In particular, the following are correct:

* the A/B turn classification and the prohibition on consecutive B turns;
* the A-turn inequality
  \(
    \lambda_j\le t_{j-1}+t_j+t_{j+1}-2;
  \)
* the pooled-level multiplicity bound of three;
* the majorization leading to `287/96`;
* the conversion from edge mass to the stated `287/288` vertex-density
  bound;
* the general near-`4/3` formula `Phi(c)` and its numerical evaluation at
  `c=4/3-1/1000`;
* the top-line lemma, the imported `3/8` density counterexample, and the
  warning that edge defect alone is not a weighted cover.

No false theorem was found.  The main quantitative theorem is, however,
strictly weaker than what its own hypotheses imply.  The proof uses the
lower bound `lambda_j>(4/3)a` only to obtain `m<=(9/4)a+O(1)`.  Combining the
same lower bound with the final level ledger improves the coefficient to

\[
 \boxed{
 \sum_j\lambda(P_j)
 \le {4+2\sqrt6\over3}a^2+O(a)
 <\left(3-{1\over30}\right)a^2+O(a).}
 \tag{1.1}
\]

Thus a critical direct braid leaves at least

\[
 {5-2\sqrt6\over3}a^2-O(a)
 >{1\over30}a^2-O(a)
 \tag{1.2}
\]

ordering edges outside the displayed plateaux, and its displayed vertex
density is at most

\[
 {4+2\sqrt6\over9}+o(1)<{89\over90}+o(1).
 \tag{1.3}
\]

This strengthens `1/96` and `287/288`, respectively.  It still does not by
itself prove the universal weighted capped-run constant is below four.

## 2. Definitions and scope

The count

\[
 |H_a|=3a^2+3a+1
\]

is the standard centered hexagon count.  A fixed coordinate line `c=t` has
`2a+1-|t|` points.

The proofs of Lemmas 2 and 3 require the following precise interpretation of
“successive plateaux are adjacent”:

```text
if P_j=[l_j,r_j], then l_(j+1)=r_j+1.
```

Peak plateaux belonging to different coordinates can in general intersect
in one word position.  Such a one-position overlap is not the adjacency
model used in the join proofs.  This is a definitional ambiguity worth
removing in a future edit, but not a mathematical error under the explicit
concatenation interpretation used throughout the note.

The cleanliness assumption is used only to exclude the short peak supplied
by two consecutive B turns.  Since that peak has cost zero or one, any clean
scale tending to infinity would suffice for that step.

## 3. A/B classification and transition inequalities

For an internal block `P_j`, put

```text
p = c_(j-1),   c = c_j,   n = c_(j+1).
```

The three coordinates are distinct.  On the line `c=t_j`, the other two sum
to `-t_j`; since the block is directed, exactly one increases and the other
decreases.  This gives exactly the two stated types:

```text
A: p decreases, n increases;
B: p increases, n decreases.
```

If `P_j,P_(j+1)` are both B, the repeated third coordinate
`e=c_(j-1)=c_(j+2)` increases up to their join and decreases after it.  If
the two boundary values differ, the larger boundary point is a singleton
strict maximum.  If they agree, the two points are a two-position maximum.
The costs are zero or one.  Hence B blocks are independent and

\[
 B\le A+1.
\]

For an A block, let `F,L` be its first and last points.  Peak maximality of
the immediately adjacent plateaux gives

\[
 p(F)\le t_{j-1}-1,\qquad n(L)\le t_{j+1}-1.
\]

Strict integral increase of `n` on `lambda_j` word edges gives

\[
 \lambda_j\le n(L)-n(F)
 =p(F)+n(L)+t_j
 \le t_{j-1}+t_j+t_{j+1}-2.
\]

All signs and endpoint directions in the source are therefore correct.

## 4. Capacity and weighted-level ledger

The line capacity gives

\[
 \lambda_j\le2a-|t_j|.
\]

Under `lambda_j>(4/3)a`, this forces `|t_j|<2a/3`.  Two displayed long
plateaux cannot use the same coordinate and level: their vertex sets would
have more than `8a/3` points, while the line has at most `2a+1`.  Hence each
integer level has at most three occurrences after the coordinate directions
are pooled.

Internal plateau edge sets are disjoint, including across different
coordinates.  Thus

\[
 \sum_j\lambda_j\le |H_a|-1=3a^2+3a,
\]

and the crude block-count consequence is

\[
 m\le {9\over4}a+O(1).
\]

Now define `d_j` as in the source.  An internal B position has exactly two A
neighbours, and summing the A inequalities gives

\[
 \sum_j\lambda_j
 \le2aB+\sum_{j\in A}d_jt_j
       +\sum_{j\in B}(2t_j-|t_j|)+O(a).
\]

The inequality

\[
 2t-|t|\le t
\]

is equality for nonnegative `t` and a valid relaxation for negative `t`.
Also

\[
 \sum_{j\in A}d_j=3A-2B+O(1).
\]

Among `A` weights in `[1,3]` with this sum, the vector

\[
 (3^{A-B},1^B)
\]

majorizes every competitor.  After adjoining the `B` unit weights, the
relaxed weight multiset is

\[
 (3^{A-B},1^{2B}).
\]

If `S_a(r)` denotes the sum of the `r` greatest pooled levels, then grouping
the three copies of each integer level gives, uniformly for `r=O(a)`,

\[
 S_a(r)={2a\over3}r-{r^2\over6}+O(a).
\]

Rearrangement therefore gives exactly

\[
 \sum_j\lambda_j
 \le2aB+2S_a(A-B)+S_a(A+B)+O(a).
 \tag{4.1}
\]

The use of pooled levels is a relaxation: it forgets which coordinate
direction supplies each occurrence.  That can weaken the bound but cannot
invalidate it.

## 5. Independent recomputation of `287/96`

Write `A=alpha*a`, `B=beta*a`.  Expanding (4.1) gives

\[
 F(\alpha,\beta)
 =2\alpha+{4\over3}\beta-{1\over2}\alpha^2
   +{1\over3}\alpha\beta-{1\over2}\beta^2.
\]

With `s=alpha+beta`,

\[
 F=2s-{s^2\over2}
   +\left({4s\over3}-{2\over3}\right)\beta
   -{4\over3}\beta^2.
\]

For `s>1/2`, the constrained maximizer is interior and equals

\[
 \beta={s\over2}-{1\over4}.
\]

The resulting one-variable envelope is

\[
 G(s)=-{s^2\over6}+{5s\over3}+{1\over12}.
 \tag{5.1}
\]

It is increasing throughout the relevant interval.  If one uses only
`s<=9/4`, then

\[
 G(9/4)={287\over96}.
\]

The optimizer has

\[
 (\alpha,\beta)=\left({11\over8},{7\over8}\right),
\]

and direct substitution reproduces `63/32+49/48=287/96`.  The constant in
the source is therefore algebraically correct.

The edge-to-vertex conversion is also correct.  The displayed plateaux use
at most

\[
 \sum_j(\lambda_j+1)=\sum_j\lambda_j+O(a)
\]

vertices, so division by `|H_a|=3a^2+O(a)` gives `287/288+o(1)`.  This is a
vertex-union density, not a density of forward windows serviced by those
plateaux.  Service intervals can overlap heavily, so no window-density
claim follows from it.

## 6. Stronger mass-feasibility optimization

The maximizer `s=9/4` used above is incompatible, to leading order, with the
lower length hypothesis.  Indeed, every one of the `m=s*a+O(1)` blocks has
cost greater than `(4/3)a`, so

\[
 {1\over a^2}\sum_j\lambda_j\ge {4\over3}s-o(1).
 \tag{6.1}
\]

Combining (6.1) with the upper envelope (5.1) forces

\[
 {4\over3}s\le G(s)+o(1).
\]

Ignoring the vanishing term and multiplying by 12 gives

\[
 -2s^2+4s+1\ge0.
\]

Consequently

\[
 s\le s_*:=1+{\sqrt6\over2}+o(1),
\]

which is strictly smaller than `9/4`.  Since `G` is increasing,

\[
 \sum_j\lambda_j
 \le G(s_*)a^2+O(a)
 ={4\over3}s_*a^2+O(a)
 ={4+2\sqrt6\over3}a^2+O(a).
\]

Finally,

\[
 {4+2\sqrt6\over3}<{89\over30}
\]

is equivalent, after clearing denominators, to
`20*sqrt(6)<49`, whose square is the strict integer inequality
`2400<2401`.  This proves (1.1)--(1.3) with completely explicit rational
room.

## 7. Robust threshold audit and strengthening

For a general threshold `lambda_j>c*a`, put `h=2-c`.  The pooled-level
asymptotic is

\[
 S_{a,c}(r)=har-{r^2\over6}+O(a).
\]

Before feeding back the lower mass, the optimized fixed-`s` envelope is

\[
 G_c(s)=-{s^2\over6}+(3-c)s+{3\over4}(2c-3)^2,
 \tag{7.1}
\]

provided `c` is near `4/3` and the beta optimizer is interior.  Substituting
the crude `s=3/c` gives exactly the source formula

\[
 \Phi(c)={18\over c}-9-{9\over2c^2}
 +{3\over16}\left(4c+{4\over c}-6\right)^2.
\]

At `c=4/3-1/1000`, direct evaluation gives

\[
 \Phi(c)=2.9943855828\ldots<2.9944<3-{1\over200}.
\]

Thus the robust claim in the source is correct.

The stronger feasibility condition is `c*s<=G_c(s)`.  Near `4/3`, its
positive root is

\[
 s_*(c)={3\over2}(2+\sqrt6)(3-2c),
\]

and the improved edge coefficient is

\[
 C(c)=c\,s_*(c)
 ={3c\over2}(2+\sqrt6)(3-2c).
 \tag{7.2}
\]

This branch is active while `s_*(c)<=3/c`.  On the branch containing `4/3`
this means

\[
 c\ge {3+\sqrt{25-8\sqrt6}\over4}
   =1.3311670401\ldots .
\]

In particular it is active at `c=4/3-1/1000`.  There

\[
 C(c)=2.9818863608\ldots<3-{1\over56}.
\]

So the robust conclusion can be strengthened from an edge defect `1/200`
to `1/56` at the displayed perturbation.

## 8. Top lines and the explicit density counterexample

The three top lines `x=a`, `y=a`, `z=a` are pairwise disjoint and each has
`a+1` points.  A maximal occurrence block of a top line that meets neither
word endpoint is automatically a peak: its neighbouring values cannot
equal `a` by maximality and cannot exceed `a`.  If a top line has no such
internal block, at least one of its occurrence blocks uses a word endpoint.
Only two disjoint top lines can use the two endpoints, so the third supplies
an internal peak of cost at most `a`.  Lemma 4 is correct.

For the imported high-line suffix, the selected mass is

\[
 3\sum_{t>a/2}^{a-1}(2a+1-t)
 ={15\over8}a^2+O(a),
\]

leaving `9a^2/8+O(a)` points in the arbitrary prefix.  The exact source
`SHORT_PEAK_DENSITY.md` verifies that only `3/8+O(1/a)` of the forward
windows can contain a peak of cost at most `a`.  At each displayed join the
shared boundary coordinate is `-a` and hence a valley, so this construction
is consistent with the A-turn sign ledger.

The weighted arithmetic is also correct.  Increasing levels make the one
cross-level discrepancy only `O(a^2)`, and

\[
 3\sum_{t=a/2+O(1)}^{a-1}(2a+1-t)(2a-t)
 ={19\over8}a^3+O(a^2).
\]

Adding the universal `2a` charge on the `9a^2/8+O(a)` complement gives
`37a^3/8+O(a^2)`.  As the source says, this is merely the cost of one
assignment, not a lower bound on the optimum.

## 9. What can be said about the weighted `<4` target

The stronger edge constant still does not control all starts outside the
braid.  It does, however, give a sharper and useful near-closure statement.

Let `P_1,...,P_m` be a disjoint adjacent direct braid, let
`lambda_j=lambda(P_j)`, and put `L=4a+2`.  Every admissible forward start
lying in `P_j`, for `j<m`, sees the whole next block `P_(j+1)`: after the
start there are at most `2a` remaining positions of `P_j` and at most
`2a+1` positions of `P_(j+1)`.  Hence

\[
 q_i\le\lambda_{j+1}
\]

for those starts, and their total charge is at most

\[
 \sum_{j<m}(\lambda_j+1)\lambda_{j+1}.
 \tag{9.1}
\]

Each plateau is used only by starts in the preceding block, so this
assignment also has congestion at most `2a+1`.

For `x,y in [(4/3)a,2a]`, the elementary secant inequality

\[
 xy\le {5a\over3}(x+y)-{8a^2\over3}
 \tag{9.2}
\]

follows from writing `x=(4/3)a+u`, `y=(4/3)a+v` and using
`uv<=(a/3)(u+v)`.  Add the nonnegative closing product to (9.1), sum (9.2)
cyclically, and write `m=s*a`.  This gives

\[
 \sum_j\lambda_j\lambda_{j+1}
 \le\left({10\over3}G(s)-{8\over3}s\right)a^3+O(a^2).
\]

On the feasible interval this expression is increasing up to `s_*`: its
derivative is `(26-10s)/9>0` there.  Since
`G(s_*)=(4/3)s_*`, the result is

\[
 \sum_{j<m}\lambda_j\lambda_{j+1}
 \le {16+8\sqrt6\over9}a^3+O(a^2)
 =3.9551019935\ldots a^3+O(a^2).
 \tag{9.3}
\]

Thus the starts physically lying in the displayed braid already admit a
charge below the global critical constant four.  The numerical margin is

\[
 4-{16+8\sqrt6\over9}=0.0448980064\ldots.
\]

This does **not** settle all starts.  The precise missing inequality retains
the actual normalized braid edge mass and block count

\[
 \sigma={1\over a^2}\sum_j\lambda_j,
 \qquad s={m\over a}.
\]

The next-block assignment costs at most

\[
 \left({10\over3}\sigma-{8\over3}s\right)a^3+O(a^2),
\]

and leaves at most `(3-sigma)a^2+O(a)` leading-order start positions outside
the displayed braid.  Therefore a gap/transition theorem sufficient for a
strict universal saving is

\[
 Q_{\rm gap}
 \le\left(4-\varepsilon-{10\over3}\sigma
                  +{8\over3}s\right)a^3+o(a^3),
 \tag{9.4}
\]

uniformly over every feasible pair

\[
 {4\over3}s\le\sigma\le G(s),
 \qquad 0\le s\le s_*.
\]

Equivalently, when `sigma<3`, the required average gap-start charge is

\[
 \left[
 {4-(10/3)\sigma+(8/3)s\over3-\sigma}
 -{\varepsilon\over3-\sigma}
 \right]a+o(a).
 \tag{9.5}
\]

At the extremal feasible point, the uncovered word mass is

\[
 \left(3-{4+2\sqrt6\over3}\right)a^2+O(a),
\]

and the margin in (9.3) is exactly `(4/3)a` times that mass.  Consequently,
at that extremal endpoint, (9.4) reduces to the particularly transparent
requirement:

> Service the non-braid/gap starts at average cost strictly below `(4/3)a`,
> with compatible `O(a)` congestion.

Away from the extremal endpoint, `4a/3` is not a uniform sufficient average:
the right side of (9.5) can be smaller.  Thus the full target is the
parameter-sensitive inequality (9.4), not merely its endpoint specialization.

The universal `2a` fallback is too expensive and gives approximately
`4.02245a^3`, so the source is correct not to claim closure.  The improved
calculation sharpens the missing transition-gadget theorem to the explicit
budget (9.4), rather than merely asking it to turn an unspecified edge defect
into a binary coverage fraction.

## 10. Final ledger

* No source theorem is false.
* `287/96` is a correct relaxed majorization maximum, but not the strongest
  consequence of the stated long-block hypothesis.
* The exact strengthened edge coefficient is `(4+2*sqrt(6))/3`, giving a
  rationally certified `1/30` edge defect and `1/90` vertex-density defect.
* At threshold `4/3-1/1000`, the source's `1/200` robust defect is valid and
  can be strengthened to `1/56`.
* The braid-internal next-plateau assignment has leading cost at most
  `(16+8*sqrt(6))/9=3.95510...`, but arbitrary gap starts remain outside
  that bound.
* The mathematically precise next target is the parameter-sensitive
  gap/transition budget (9.4).  Its extremal endpoint asks for average cost
  below `(4/3)a`, but smaller braid masses can require a lower average.
