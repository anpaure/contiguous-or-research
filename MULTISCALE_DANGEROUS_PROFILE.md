# The scalar multiscale dangerous-profile constraints are insufficient

## 1. Outcome

Consider only the following information about directed peak plateaux:

1. their ordering-edge sets are disjoint;
2. a plateau on coordinate level `t` has cost at most `2a-|t|`;
3. for every threshold `1<c<4/3`, its normalized excess profile is

   \[
   e_a(c)=\frac1{a^2}\sum_j(\lambda_j-ca)_+;          \tag{1.1}
   \]

4. the first-dangerous seam profile is

   \[
   H_a(c)=\frac1{a^3}
   \sum_{j\ge2}(\lambda_j-ca)_+
      \min\{g_{j-1},,4a+2-\lambda_j\}.              \tag{1.2}
   \]

These scalar constraints do **not** force a threshold `c<4/3` satisfying

\[
                         3c+2e_a(c)+H_a(c)<4.         \tag{1.3}

There is an explicit feasible abstract profile with

\[
 e_a(c)=\frac32-c,qquad H_a(c)=O(a^{-1}),            \tag{1.4}
\]

for every fixed `1<c<4/3`.  Its service coefficient is therefore

\[
             3c+2e_a(c)+H_a(c)=3+c+o(1)>4.           \tag{1.5}

The profile uses only half of the available global edge mass and can place
all designated plateaux on distinct parallel coordinate lines.  Thus the
failure is not caused by saturating a dubious pooled line count.

There is also a saturated scalar profile with total plateau edge mass
`(3+o(1))a^2` for which the coefficient is bounded even farther above four.

Consequently no optimization of `e(c)` and the nonnegative seam expression
`H(c)`, using only edge disjointness and coordinate-line capacities, can
close the three-box argument.  A successful theorem must use transition
sign compatibility, cross-direction line intersections, a run-spectrum
survival constraint, or another genuinely non-scalar feature.

## 2. Normalized scalar formulation

Put

\[
                         x_j=\lambda_j/a\in(0,2].    \tag{2.1}
\]

Encode the length distribution by the finite measure

\[
                         \mu_a=\frac1a\sum_j\delta_{x_j}. \tag{2.2}

Then

\[
 e_a(c)=\int(x-c)_+\,d\mu_a(x).                     \tag{2.3}

Ordering-edge disjointness gives

\[
 \int x\,d\mu_a(x)
 =\frac1{a^2}\sum_j\lambda_j
 \le3+O(a^{-1}).                                    \tag{2.4}

There is a second scalar consequence of coordinate-line capacity.  If
`x>1`, two plateaux of cost at least `xa` cannot use the same coordinate
line, since that line has at most `2a` ordering edges.  A line can carry
such a plateau only when

\[
                         |t|\le(2-x)a.                \tag{2.5}

Across the three coordinate directions there are

\[
                         6(2-x)a+O(1)                 \tag{2.6}

eligible lines.  Hence any scalar limit `mu` must obey the survival-count
bound

\[
                         \mu([x,2])\le6(2-x),
                         \qquad 1<x\le2.             \tag{2.7}

The counterexamples below satisfy both (2.4) and (2.7) with room.

For normalized predecessor gaps `y_j=g_j/a`, the seam term has the formal
limit

\[
 H(c)=\lim\frac1a\sum_{x_j>c}
       (x_j-c)\min\{y_{j-1},4-x_j+o(1)\}.            \tag{2.8}

The known unconditional estimates

\[
 0\le H(c)\le4e(c),
 \qquad
 H(c)\le(2-c)(3-\sigma),                             \tag{2.9}

where `sigma=int x dmu`, are upper bounds only.  In particular, they do
not prevent an adversarial profile from having `H(c)=0` or `o(1)`.

## 3. A one-atom obstruction

Take the limiting measure

\[
                              \mu=\delta_{3/2}.       \tag{3.1}

It represents `a+o(a)` plateaux, each of cost `(3/2+o(1))a`.

### 3.1 Scalar feasibility

Its edge mass is

\[
                         \int x\,d\mu=3/2<3.         \tag{3.2}

At a tail threshold `1<x<=3/2`,

\[
 \mu([x,2])=1
 \le6(2-x),                                         \tag{3.3}

whose smallest right side in this range is three.  For `x>3/2`, the left
side is zero.  Thus the pooled coordinate-line count has a factor-three
margin.

Set every gap between consecutive designated plateaux to one word position.
Then `g_j/a ->0` and

\[
                              H(c)=0                 \tag{3.4}

in the normalized limit.  Any remaining `Theta(a^2)` nonplateau positions
may be placed before the first designated plateau and after the last.  Such
boundary reservoirs do not enter the sum (1.2), except for the already
lower-order first-plateau boundary term in the first-dangerous theorem.

### 3.2 Failure of every useful threshold

For `1<c<4/3`, the atom lies above the threshold and

\[
                         e(c)=\frac32-c.             \tag{3.5}

Consequently

\[
 3c+2e(c)+H(c)=3c+3-2c=3+c>4.                      \tag{3.6}

As `c` decreases to the allowed endpoint one, the expression tends to four
from above; it never becomes strictly smaller than four.  Taking a
multiscale average of the same inequalities cannot help, because (3.6) is
at least four at every individual allowed scale.

This proves that the desired threshold theorem is false at the level of
the normalized scalar constraints.

## 4. Explicit finite abstract realization

Let `a` be even.  Set

\[
                         m=a,qquad \lambda_j=3a/2
                         \quad(1\le j\le m),         \tag{4.1}

and put one separator position between consecutive plateau blocks:

\[
                         g_j=1\quad(1\le j<m).       \tag{4.2}

The plateau edges total

\[
                         E=m\lambda_j=\frac32a^2
                         \le M_a-1.                  \tag{4.3}

The disjoint plateau blocks plus their separators use

\[
 m(\lambda_j+1)+(m-1)
 =\frac32a^2+2a-1<M_a                               \tag{4.4}

word positions.  Place all remaining positions outside the chain of
designated blocks.  Thus the finite interval/edge bookkeeping is feasible.

The line-capacity bookkeeping is feasible even without mixing coordinate
directions.  A fixed coordinate has `a+1` integer levels with

\[
                         |t|\le a/2.                 \tag{4.5}

Each corresponding line has edge capacity

\[
                         2a-|t|\ge3a/2.              \tag{4.6}

Assign the `a` designated plateaux to `a` distinct such parallel lines.
Their vertex sets can be chosen disjoint because parallel coordinate lines
are disjoint.  If desired, the `a-1` separators and two outer neighbours
can be chosen from the `a+1` points of the line at level `-a`; their fixed
coordinate is below every level in (4.5), so each designated block is a
genuine fixed-coordinate peak.  Within each block, order the selected line
points monotonically in a cross coordinate, making it directed.

This constructs an actual collection of disjoint directed internal peak
blocks and one-point seams inside `H_a`.  It does not claim that an arbitrary
completion of the unused `Theta(a^2)` points creates no additional
dangerous plateaux.  No such completion claim is needed: this is a
countermodel to deductions made from the stated scalar constraints alone.

For every fixed `1<c<4/3`, all designated blocks are dangerous and

\[
 e_a(c)=\frac1{a^2}\,a\left(\frac32a-ca\right)
       =\frac32-c,                                   \tag{4.7}
\]

while

\[
 \begin{aligned}
 H_a(c)
 &=\frac1{a^3}(a-1)left(\frac32-c\right)a\cdot1\\
 &=O(a^{-1}).                                        \tag{4.8}
 \end{aligned}

Equations (4.7)--(4.8) give the finite form of (3.6).

## 5. A saturated scalar counterprofile

Even adding the requirement that dangerous plateau edges asymptotically
exhaust the entire word does not rescue the scalar optimization.

Take

\[
                              \mu=2\delta_{3/2}.      \tag{5.1}

Then

\[
 \int x\,d\mu=3,                                    \tag{5.2}

and the line-count condition at `x=3/2` is

\[
                         2\le6(2-3/2)=3.             \tag{5.3}

At the abstract interval level, use `2a` blocks of cost `3a/2`, place them
adjacently (`g_j=0`), and use distinct eligible coordinate lines.  Their
edge mass is `3a^2`, and their vertices require

\[
                         3a^2+2a<M_a                 \tag{5.4}

positions, so both the edge and vertex ledgers fit.  This is deliberately a
scalar/line-capacity model; it does not impose cross-direction intersection
or transition-sign compatibility.

Here

\[
 e(c)=2(3/2-c)=3-2c,qquad H(c)=0,                   \tag{5.5}

and hence

\[
                         3c+2e(c)=6-c
                         \ge14/3>4                  \tag{5.6}

throughout `1<c<4/3`.

Thus neither low total edge mass nor unused boundary mass is essential to
the counterexample.

## 6. General single-scale family

The same obstruction is not isolated.  Let

\[
                         \mu=s\delta_x,qquad
                         4/3\le x<2,                 \tag{6.1}

with zero normalized seam cost.  Then, for `c<4/3`,

\[
                         e(c)=s(x-c),
 \qquad
 F(c):=3c+2e(c)=3c+2s(x-c).                         \tag{6.2}

The scalar feasibility conditions are

\[
                         sx\le3,qquad
                         s\le6(2-x).                 \tag{6.3}

If `s<=3/2`, the slope of `F` is nonnegative and its infimum on
`(1,4/3)` is

\[
                         3+2s(x-1).                  \tag{6.4}

Hence every feasible pair satisfying

\[
                         s(x-1)\ge1/2                \tag{6.5}

defeats all thresholds.  The profile `(s,x)=(1,3/2)` is the equality case.

If `s>=3/2`, the slope is nonpositive and the infimum is attained as
`c` tends to `4/3`:

\[
                         4+2s(x-4/3)\ge4.            \tag{6.6}

For example, saturating the edge budget with `s=3/x` is line-feasible when

\[
 \frac3x\le6(2-x)
 \quad\Longleftrightarrow\quad
 x\le1+\frac1{\sqrt2},                               \tag{6.7}

and every `x in (4/3,1+1/sqrt(2)]` gives a strict scalar obstruction.

This continuum of profiles shows that small perturbations or a finite set
of extra thresholds cannot repair the argument.

## 7. What additional mathematics is necessary

The counterprofiles exploit facts invisible to `e(c)` and `H(c)`:

* many long plateaux may use the same coordinate direction but different
  levels;
* almost all nonplateau mass may sit at a word boundary, where it does not
  enter the predecessor-gap seam sum;
* one-point separators make the normalized seam profile vanish; and
* the scalar line ledger knows nothing about the signs required to join two
  peak blocks or about new peaks created in the other coordinates.

At least one of the following is needed to proceed.

1. **Transition geometry.**  Use A/B-turn or level-transport inequalities
   that couple the fixed levels and directions of consecutive plateaux.
2. **Cross-line intersection constraints.**  The saturated profile assigns
   many blocks to different coordinate directions but ignores competition
   for their intersection points.
3. **A survivor/run-spectrum condition.**  A large dangerous-free boundary
   reservoir is cheaply serviced and may already make the underlying order
   incompatible with the global lower run-cost requirement.  This
   information is absent from the scalar edge and line ledgers.
4. **A boundary-sensitive seam functional.**  The current `H(c)` ignores
   the large gap before the first dangerous plateau and after the last.
5. **Extension below `c=1`.**  For the basic atom,
   `3c+2e(c)=3+c<4` when `c<1`.  The restriction `c>1` is therefore
   mathematically active; extending the service theorem to a lower
   threshold would defeat this particular profile.

Without one of these additions, the one-dimensional multiscale program is
provably underdetermined.

## 8. Theorem ledger

**Proved here:** edge disjointness plus coordinate-line capacity does not
force any `1<c<4/3` with `3c+2e(c)+H(c)<4`; the finite profile
(4.1)--(4.8) is an explicit countermodel.

**Also proved:** the failure persists under full scalar edge-mass
saturation and throughout the one-atom family (6.1)--(6.7).

**Not claimed:** that either abstract profile extends to a complete order of
`H_a` with no additional dangerous plateaux, or that the first-dangerous
service theorem itself is false.  The conclusion is exactly that the named
scalar constraints are insufficient; additional geometry may still rule
out every such profile in an actual survivor.
