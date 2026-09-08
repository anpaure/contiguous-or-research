# Independent audit of `LARGE_DEFECT_DICHOTOMY_NEXT.md`

## 1. Verdict

**PASS WITH ONE LOCAL QUANTIFIER REPAIR.**

The large-defect transfer is sound under the inherited three-box framework.
In particular, I independently verified all of the following.

1. For the forward first-dangerous assignment,
   
   \[
     C_\alpha\le 4a+3,\qquad C_\beta=0.
   \]

2. At the full lower-half cap `h=3a-1`, the exact endpoint-slack coefficient
   is therefore

   \[
             C_\alpha+C_\beta+h=7a+2,
   \]

   rather than the symmetric-assignment coefficient `11a+O(1)`.

3. If only the final `L=4a+2` starts are omitted, the exact finite lower
   cost is

   \[
   Q\ge 4a^3-\frac{15}{2}a^2-\frac12a+1-(7a+2)D_a.
   \]

4. For every fixed `2<y<=3`, a cap with `h/a->y` gives

   \[
       \liminf \frac{Q}{a^3}
       \ge F(y)-(4+y)\delta,
       \qquad
       \delta=\lim \frac{D_a}{a^2},
   \]

   where

   \[
       F(y)=\frac{y^3}{6}-\frac{3y^2}{2}
             +\frac{9y}{2}-\frac12.
   \]

5. The optimized atomic saving can genuinely be transferred before the
   defect comparison.  More precisely, for each fixed atom location
   `x in [4/3,3/2]` and each fixed `tau>0`, the audited seam construction
   supplies an assignment with

   \[
        \frac{Q}{a^3}\le 3x-S_*(x)+\tau+o(1),
   \]

   and

   \[
     S_*(x)=x\left(\sqrt{x(6x-7)}-\sqrt{3-2x}\right)^2.
   \]

6. Consequently

   \[
     \liminf\frac{D_a}{a^2}
       \ge \frac{4-3x+S_*(x)}7,
   \]

   with the advertised weaker uniform bound `8/189`, the balanced bound
   `4/63`, and the all-cap improvement `0.0657635...` all correct.

7. The finite-band version follows by exactly the same transfer.  Its
   positive constant is uniform because the zero-band margin is at least
   `8/27` on the compact interval `[4/3,3/2]`.

The one actual defect in the source was a quantifier sentence saying that an
**unbounded** sequence `D_a/a^2` makes every lower bound automatic.  This is
false for an oscillating sequence with a finite liminf.  The proof needs a
subsequence attaining the liminf.  I patched that sentence, the corresponding
proof wording, and the adversarial-audit wording.  I also added the omitted
normal-form condition `alpha_i<=beta_i` and fixed two typographical phrases.
No theorem coefficient or conclusion changed.

The result remains conditional in exactly the way stated in the source.  It
does not show that every plateau profile has quadratic defect, and it does
not establish the three-box or Boolean-array conjecture.

## 2. Sources checked

I checked the proposed note against the complete statements and conventions
in:

- `FABLE_RUN_SPECTRUM_AUDIT.md`;
- `FIRST_DANGEROUS_GLOBAL_SERVICE.md` and its independent audit;
- `FABLE_QUANTITATIVE_SEAM_TRACE_AUDIT.md`;
- `FABLE_QUANTITATIVE_SEAM_REPAIR_INDEPENDENT_AUDIT.md`;
- `MIXED_PROFILE_SEAM_NEXT.md`; and
- `MIXED_PROFILE_SEAM_INDEPENDENT_AUDIT.md`.

In particular, I did not import the rejected staircase, poison-union,
pointwise run-ceiling, or `A'/B'` claims from the live Fable trace.

## 3. Exact endpoint-slack calculation

Choose one witness for each of the `M_a=3a^2+3a+1` middle targets in a word
of length `M_a+D_a`.  Ordering these intervals by their left endpoints gives

\[
 I_i=[i+\alpha_i,i+\beta_i],
\]

where both offset sequences are nondecreasing, lie in `[0,D_a]`, and satisfy
`alpha_i<=beta_i`.

For an assigned set of indices `J`, the audited subset run-spectrum inequality
is

\[
 |S_h|\le
 \sum_{i\in J}\min(\lambda_i,h)
 +(M_a-|J|)h+(C_\alpha+C_\beta+h)D_a.       \tag{3.1}
\]

This formula is deterministic and finite.  It makes no small-defect
assumption.

Every run in the first-dangerous and modified seam assignments lies in

\[
                         [i+1,i+4a+2].
\]

With edge cost `lambda=v-u`, the endpoint-charge convention uses
`v+1-i`.  Hence the correct one-sided span is `4a+3`.  Every assignment
points right, so a fixed alpha increment is crossed by at most `4a+3`
starts and no beta increment is crossed:

\[
                       C_\alpha\le4a+3,
              \qquad C_\beta=0.                    \tag{3.2}
\]

This confirms that using the symmetric bound `2(4a+3)` would be safe but
unnecessarily weak.

At cap `h=3a-1`, all chosen costs are below the cap for large `a`: dangerous
plateaux have at most `2a` edges, cheap first-dangerous runs have less than
`2a` edges, and the repaired seam-local runs have at most `2a+O(1)` edges.
The assignment may be taken on every start `1,...,M_a-L`, with
`L=4a+2`.  Shared plateau endpoints do not have to be omitted; the original
first-dangerous rule is defined there as well.

The exact target count is

\[
 |S_{3a-1}|=V_a
 =4a^3+\frac92a^2+\frac32a-1.             \tag{3.3}
\]

The omitted-start contribution is

\[
 (4a+2)(3a-1)=12a^2+2a-2,                 \tag{3.4}
\]

while

\[
 C_\alpha+C_\beta+h=(4a+3)+(3a-1)=7a+2.  \tag{3.5}
\]

Subtracting (3.4) and the defect term from (3.3) gives exactly

\[
 Q\ge4a^3-\frac{15}{2}a^2-\frac12a+1-(7a+2)D_a.   \tag{3.6}
\]

There is no hidden penalty per omitted start and no factor `D_a` attached to
the `O(a^2)` omission term.

## 4. Audit of every proportional cap

For `h/a->y` with `1<=y<=3`, the lower-target count is obtained by integrating
the exact rank slices.  In the range needed here, `2<y<=3`, this gives

\[
 \begin{aligned}
 \frac{|S_h|}{a^3}
 &\longrightarrow
 \int_0^1(3-t^2)\,dt
 +\frac12\int_1^y(3-t)^2\,dt\\
 &=4-\frac{(3-y)^3}{6}\\
 &=\frac{y^3}{6}-\frac{3y^2}{2}
   +\frac{9y}{2}-\frac12
 =F(y).                                             \tag{4.1}
 \end{aligned}
\]

If `D_a/a^2->delta<infinity`, then from (3.1):

- the `O(a)` omitted starts contribute `O(a^2)=o(a^3)`;
- `C_alpha/a->4`;
- `h/a->y`; and
- all selected costs are below the cap because `y>2`.

Therefore

\[
        \liminf\frac Q{a^3}\ge F(y)-(4+y)\delta.   \tag{4.2}
\]

The denominator `4+y` in Theorem B is consequently exact for this
assignment architecture.

To prove a liminf statement, choose a subsequence attaining
`liminf D_a/a^2`.  If that liminf is infinite, the desired positive bound is
automatic.  Merely having an infinite limsup is irrelevant; this is the
local quantifier repair made to the source.

Now suppose the same orders admit assignments with

\[
                         Q\le(U+o(1))a^3.
\]

Combining with (4.2) gives, at every fixed `2<y<=3`,

\[
 \delta\ge\frac{F(y)-U}{4+y}.
\]

Since `delta>=0`, taking positive parts and the supremum proves

\[
 \delta\ge\sup_{2<y\le3}
       \frac{(F(y)-U)_+}{4+y}.                       \tag{4.3}
\]

Letting `y->3`, or directly using `h=3a-1`, gives

\[
                         \delta\ge\frac{(4-U)_+}{7}. \tag{4.4}
\]

This verifies Theorem B, including its quantifiers.

## 5. Reconstruction of the optimized atomic upper assignment

Assume

\[
              \mu_a\Longrightarrow2\delta_x,
        \qquad 4/3\le x\le3/2.                     \tag{5.1}
\]

The important point is that the construction of a cheap run assignment is
independent of `D_a=o(a^2)`.  Small defect was used in the earlier papers
only to compare that assignment with the lower capped-cost law.

Choose a fixed dangerous threshold

\[
                            c=x-\zeta,
\]

where `zeta>0` is numerical and fixed before `a->infinity`.  Atomic
convergence gives

\[
                         e_c\longrightarrow2\zeta.
\]

The audited first-dangerous estimate therefore gives

\[
 \begin{aligned}
 \frac{Q_{fd}}{a^3}
 &\le3c+2e_c+(4-c)e_c+o(1)\\
 &\le3x+(9-2x)\zeta+2\zeta^2+o(1).                 \tag{5.2}
 \end{aligned}
\]

For a fixed gap cutoff `r>0`, the aggregate line capacity absorbs at most

\[
                         3(3-2x)a+o(a)
\]

seams, and the total complement-gap mass is

\[
                         (3-2x)a^2+o(a^2).
\]

Markov's inequality therefore leaves normalized nonabsorbed, gap-at-most-`r`
seam mass at least

\[
       \left[6x-7-\frac{3-2x}{r}\right]_+.         \tag{5.3}
\]

In the optimizing range, each such seam has at least `xa-o(a)` disjoint safe
starts and saves at least `(x-r)a-o(a)` at each.  Thus its total guaranteed
saving coefficient is

\[
 S_r(x)=x\left[6x-7-\frac{3-2x}{r}\right]_+(x-r)_+. \tag{5.4}
\]

On the positive interior, differentiating (5.4) gives

\[
             r_*(x)=\sqrt{\frac{x(3-2x)}{6x-7}}.   \tag{5.5}
\]

The audited support checks give `0<r_*<x` and `r_*<=4-2x` for
`4/3<=x<3/2`.  At `x=3/2`, this is a boundary limit `r_*->0+`; no zero
gap cutoff is inserted into a finite proof.  Substitution yields

\[
 \begin{aligned}
 S_*(x)
 &=x\left(x(6x-7)+(3-2x)
       -2\sqrt{x(6x-7)(3-2x)}\right)\\
 &=x\left(\sqrt{x(6x-7)}-\sqrt{3-2x}\right)^2.    \tag{5.6}
 \end{aligned}
\]

Given `tau>0`, first choose a positive fixed `r` sufficiently close to the
optimizer (or sufficiently small at `x=3/2`), and then choose `zeta>0`
sufficiently small.  The band tolerance in the weak-convergence argument can
then be chosen smaller still.  Combining (5.2) with the repaired safe-service
subtraction gives

\[
              \frac Q{a^3}
              \le3x-S_*(x)+\tau+o(1).              \tag{5.7}
\]

All parameters in this argument are fixed numerical constants before the
limit in `a`.  This validates the exact transfer that was the most delicate
step in Theorem A.

## 6. Atomic defect coefficients

Apply (4.4) to (5.7), then let `tau->0` after the `a`-limit.  This gives

\[
 \liminf\frac{D_a}{a^2}
 \ge\frac{4-3x+S_*(x)}7.                            \tag{6.1}
\]

The old admissible cutoff `r=1` gives the weaker saving

\[
                         S_0(x)=(8x-10)x(x-1).
\]

Direct expansion gives

\[
 S_0(x)-(3x-4)=8x^3-18x^2+7x+4.                   \tag{6.2}
\]

Its derivative is `24x^2-36x+7`, which is positive throughout
`[4/3,3/2]`, and its value at `4/3` is `8/27`.  Since `S_*>=S_0`,

\[
 4-3x+S_*(x)\ge\frac8{27},
\]

and hence

\[
                 \liminf\frac{D_a}{a^2}\ge\frac8{189}. \tag{6.3}
\]

At the balanced endpoint,

\[
                      S_*(4/3)=\frac49,
\]

so (6.1) gives

\[
                 \liminf\frac{D_a}{a^2}\ge\frac4{63}. \tag{6.4}
\]

The advertised uniform constant is therefore valid, though deliberately
weaker than the optimized endpoint value.

## 7. All-cap optimization at `x=4/3`

At the balanced atom, the upper cost is

\[
                         U=4-\frac49=\frac{32}{9}.
\]

Write `t=3-y`, so `0<=t<1`.  Equation (4.1) simplifies exactly to

\[
                         F(3-t)=4-\frac{t^3}{6}.
\]

The defect lower bound becomes

\[
 R(t)=\frac{4/9-t^3/6}{7-t}.                       \tag{7.1}
\]

Its derivative has the sign of

\[
                 \frac49-\frac72t^2+\frac13t^3.
\]

After multiplying by `18`, the critical equation is

\[
                         6t^3-63t^2+8=0.            \tag{7.2}
\]

The left side is strictly decreasing on `(0,1)`, is positive at zero, and
negative at one.  Hence there is exactly one critical point, and it is the
maximizer.  Numerically,

\[
 t=0.3626665511255889\ldots,
 \qquad
 R(t)=0.0657635136526647\ldots.                    \tag{7.3}
\]

This verifies equations (1.5)--(1.7).

## 8. Finite-band transfer

The inherited finite mixed-band theorem constructs, without using small
defect in the construction itself, an assignment with

\[
 \frac Q{a^3}\le U_\varepsilon(x)+o(1),
\]

where

\[
 \begin{aligned}
 C_\varepsilon(x)
   &=8x-10-(10+x)\varepsilon+\varepsilon^2,\\
 U_\varepsilon(x)
   &=3x+29\varepsilon+15\varepsilon^2\\
   &\quad-C_\varepsilon(x)_+
       (x-\varepsilon)(x-1-\varepsilon).
 \end{aligned}                                    \tag{8.1}
\]

At `epsilon=0`,

\[
 4-U_0(x)=S_0(x)-(3x-4)\ge8/27                     \tag{8.2}
\]

uniformly on the compact interval `[4/3,3/2]`.  The positive-part operation
is continuous.  Therefore one absolute sufficiently small `epsilon_0`
makes

\[
 \eta_\varepsilon
 :=\inf_{4/3\le x\le3/2}(4-U_\varepsilon(x))>0
\]

for every fixed `0<epsilon<=epsilon_0`.  Equation (4.4) then gives

\[
              \liminf\frac{D_a}{a^2}
              \ge\frac{\eta_\varepsilon}{7}>0.    \tag{8.3}
\]

Thus the finite-band conclusion is valid with uniform quantifiers.  It does
not assert a uniform positive constant as `epsilon` is allowed to leave the
chosen small interval.

## 9. Adversarial stress tests

### 9.1 Oscillating defect

Take a hypothetical sequence whose defect ratios alternate between a bounded
value and values tending to infinity.  The source's original “unbounded is
automatic” sentence would not handle it.  Passing to the subsequence
attaining the liminf does, and atomic or finite-band hypotheses remain true
on that subsequence.

### 9.2 Endpoint versus symmetric congestion

Replacing the one-sided assignment by an arbitrary two-sided assignment
would change the coefficient from `7` to at most `11`.  Nothing in the
source silently makes that replacement: both the first-dangerous runs and
every seam-local replacement remain in the same forward window.  Therefore
`7a+2` is legitimate, not optimistic.

### 9.3 Reused seam-local runs

One threshold component may be assigned to `Theta(a)` starts.  This does not
increase endpoint congestion beyond `4a+3`, because every such start lies
within the same forward-span bound.  The service intervals are disjoint only
to prevent double-counting the cost saving; run identity is irrelevant to
the heterogeneous run lemma.

### 9.4 Cap endpoint `y=2`

The transfer theorem uses `y>2`, since a cost of `2a+O(1)` need not be below
a cap asymptotic to exactly `2a`.  The maximization in the balanced formula
may harmlessly be written with the closed endpoint `y=2` by continuity, but
no finite cap-truncation claim is made there.

### 9.5 Atomic endpoint `x=3/2`

The formal optimizer has `r_*=0`.  The proof uses a fixed positive cutoff
and then lets it approach zero through the external `tau` tolerance.  It
does not use a zero denominator in the long-gap Markov bound.

### 9.6 Large defect does not imply impossibility

The conclusion `D_a>=kappa a^2` is a lower bound on local word length, not a
contradiction.  It rules out a subquadratic-error three-box construction with
that geometry.  It does not rule out universal words and does not construct
or exclude the desired Boolean OR arrays.

### 9.7 Broad mixed profile

The broad measure `2 1_[1,2] dx` has a feasible reduced thresholdwise ledger
with adversarial value above four for every fixed `1<c<2`, as completed in
the independent mixed-profile audit.  Theorem B consequently gives no
positive defect lower bound for that relaxation.  This is consistent with,
and not a counterexample to, the atomic theorem.

## 10. Exact scope

### Certified

1. The exact finite defect inequality and coefficient `7a+2`.
2. The all-cap transfer formula with denominator `4+y`.
3. The optimized atomic assignment and the use of `S_*(x)`.
4. The explicit atomic defect bound and its uniform corollary.
5. The balanced all-cap optimization.
6. The finite mixed-band quadratic-defect conclusion.
7. The interpretation of the large-defect branch as constant-fraction local
   excess.

### Not certified or claimed

1. A strict-sub-four assignment for every plateau profile.
2. Realizability of the broad static threshold ledgers by one ordering.
3. Direction-labelled or nested multiscale compatibility.
4. A quadratic lower bound for unrestricted three-box words.
5. A subquadratic three-box construction.
6. The all-`k` contiguous-OR conjecture.

The next valid target is therefore exactly the one stated in the source: add
a realizability constraint coupling thresholds, directions, and gap placement.
Further scalar manipulation of the endpoint-defect term cannot eliminate the
broad relaxed ledger.
