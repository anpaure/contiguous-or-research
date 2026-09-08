# Large-defect dichotomy for the three-box seam method

## 1. Outcome

This note removes the hypothesis `D=o(a^2)` from the **conclusion** of the
atomic quantitative-seam theorem.  It does not remove `D` from the exact
run-spectrum inequality; instead it keeps that error term and turns it into a
quadratic lower bound on `D`.

Let

\[
 H_a=\{(x,y,z)\in\mathbb Z^3:x+y+z=0,
                     |x|,|y|,|z|\le a\},
 \qquad M_a=3a^2+3a+1.
\]

Select one witness for every middle target in a universal three-chain-box
word of length

\[
                         N_a=M_a+D_a.
\]

As in the audited seam papers, let

\[
 \mu_a={1\over a}\sum_P\delta_{\lambda(P)/a}
\]

be the normalized measure of directed internal coordinate-peak plateaux in
the induced order of the selected middle targets.

The main new conclusion is the following.

> **Theorem A (atomic profiles pay quadratic defect).**  Suppose
> \[
>      \mu_a\Longrightarrow2\delta_x,
>      \qquad {4\over3}\le x\le {3\over2}.
> \]
> If such universal words exist, then
> \[
>  \liminf_{a\to\infty}{D_a\over a^2}
>  \ge {4-3x+S_*(x)\over7}>0,                 \tag{1.1}
> \]
> where
> \[
> S_*(x)=x\left(\sqrt{x(6x-7)}-\sqrt{3-2x}\right)^2. \tag{1.2}
> \]
> In particular, uniformly over the displayed interval,
> \[
>       \liminf {D_a\over a^2}\ge {8\over189}.       \tag{1.3}
> \]

At the formerly balanced survivor `x=4/3`, (1.1) gives

\[
             \liminf {D_a\over a^2}\ge {4\over63}.   \tag{1.4}
\]

Keeping the whole cap spectrum improves (1.4) to

\[
 \liminf {D_a\over a^2}
 \ge \max_{2\le y\le3}
 {F(y)-32/9\over4+y}=0.0657\ldots,             \tag{1.5}
\]

where

\[
 F(y)={y^3\over6}-{3y^2\over2}+{9y\over2}-{1\over2}. \tag{1.6}
\]

The maximizer in (1.5) is `y=3-t`, where `t` is the unique root in `(0,1)`
of

\[
                         6t^3-63t^2+8=0.             \tag{1.7}
\]

Thus the earlier statement

\[
 D=o(a^2)\quad\Longrightarrow\quad
 2\delta_x\text{ is impossible}
\]

is the zero-defect boundary of a stronger statement: every such atomic
geometry forces a fixed positive fraction of the middle-layer size as
additional word length.

There is also a general transfer principle.

> **Theorem B (cost saving implies quadratic defect).**  Suppose a structural
> class of selected middle orders admits, on all but `O(a)` indices, a
> forward assignment of internal avoiding threshold runs such that
> 
> * every run lies in a forward window of edge length `4a+2`;
> * every assigned run has cost at most `2a+O(1)`; and
> * the total assigned cost is at most
>   \[
>                      (U+o(1))a^3.
>   \]
> 
> Then every universal word in that class satisfies
> \[
>  \liminf {D_a\over a^2}\ge
>  \sup_{2<y\le3}{(F(y)-U)_+\over4+y}.                \tag{1.8}
> \]
> In particular, the cap `y=3` gives
> \[
>  \liminf {D_a\over a^2}\ge{(4-U)_+\over7}.         \tag{1.9}
> \]

This theorem is the exact way to exploit the alternative `D=Omega(a^2)`.
For the fixed-dimensional aggregation program, such a branch already has
quadratic local error and therefore cannot establish a subquadratic
three-box construction.

The note does **not** prove that all three-box words have quadratic defect.
The broad mixed threshold ledger from `MIXED_PROFILE_SEAM_NEXT.md` has
`U>=4` at every threshold in the present scalar relaxation, so Theorem B
gives no positive bound for it.  That is the real remaining obstruction.

## 2. Exact finite defect inequality

Choose one witness interval for each of the `M_a` middle targets and order
them by increasing left endpoint.  Write

\[
 I_i=[i+\alpha_i,i+\beta_i],
 \qquad0\le\alpha_1\le\cdots\le\alpha_{M_a}\le D_a,
 \qquad0\le\beta_1\le\cdots\le\beta_{M_a}\le D_a.
\]

Here also `alpha_i<=beta_i`, since every selected witness interval is
nonempty.

Fix an assignment of internal coordinate-threshold runs to a set
`J subseteq [M_a]`.  Let `lambda_i` be the edge length of the run assigned to
`i`.  If all runs point right and lie in

\[
                         [i+1,i+4a+2],                \tag{2.1}
\]

then the audited charge convention gives

\[
 C_\alpha\le4a+3,
 \qquad C_\beta=0.                                  \tag{2.2}
\]

For every integer cap `h`, the subset run-spectrum inequality is

\[
 |S_h|\le
 \sum_{i\in J}\min(\lambda_i,h)
 +(M_a-|J|)h+(C_\alpha+C_\beta+h)D_a.               \tag{2.3}
\]

Here `S_h` is the family of nonzero lower targets at middle-rank distance at
most `h`.  Equation (2.3) is exact; it requires no asymptotic assumption on
`D_a`.

Take

\[
 h=3a-1,
 \qquad
 |S_h|=V_a=4a^3+{9\over2}a^2+{3\over2}a-1.          \tag{2.4}
\]

The first-dangerous assignment omits at most

\[
                         L=4a+2                      \tag{2.5}
\]

final indices.  Every dangerous plateau costs at most `2a`, every fallback
run costs less than `2a`, and every seam-local replacement used below also
costs at most `2a+O(1)`.  Hence the cap does not truncate the selected costs
for all sufficiently large `a`.  From (2.2)--(2.5), their total cost `Q`
satisfies the exact lower bound

\[
\begin{aligned}
 Q
 &\ge V_a-(4a+2)(3a-1)-(7a+2)D_a\\
 &=4a^3-{15\over2}a^2-{1\over2}a+1-(7a+2)D_a.
                                                               \tag{2.6}
\end{aligned}
\]

This is the term that was previously abbreviated as

\[
                         Q\ge(4-o(1))a^3
\]

under `D=o(a^2)`.  Keeping it is the entire source of the large-defect
dichotomy.

### 2.1 All caps between `2a` and `3a`

Let `h/a -> y` with `2<y<=3`.  The exact rank-slice calculation in
`FABLE_RUN_SPECTRUM_AUDIT.md` gives

\[
 { |S_h|\over a^3}\longrightarrow F(y),             \tag{2.7}
\]

where `F` is (1.6).  Indeed, the normalized complement budget is

\[
 b(y)=-{y^3\over6}+{3y^2\over2}-{3y\over2}+{1\over2},
\]

and `F(y)=3y-b(y)`.  Since all assigned costs are at most `2a+O(1)`, the
minimum in (2.3) may again be removed.  The `O(a)` omitted indices contribute
only `O(a^2)`.  Therefore, if

\[
                         {D_a\over a^2}\to\delta<\infty,
\]

then

\[
                  \liminf {Q\over a^3}
                  \ge F(y)-(4+y)\delta.              \tag{2.8}
\]

If `liminf D_a/a^2=+infinity`, every lower bound asserted in this note is
automatic.  Mere unboundedness is not enough, since an oscillating sequence
can still have a finite-liminf subsequence.

## 3. Proof of the transfer theorem

Assume the hypotheses of Theorem B.  If the liminf of `D_a/a^2` is finite,
pass to a subsequence attaining that liminf and on which

\[
                  {D_a\over a^2}\to\delta
\]

and on which the total assigned cost is at most `(U+o(1))a^3`.  If the
liminf is infinite, the conclusion is immediate.

For every fixed `2<y<3`, equation (2.8) gives

\[
                         U\ge F(y)-(4+y)\delta.
\]

Consequently

\[
                   \delta\ge{(F(y)-U)_+\over4+y}.
\]

Taking the supremum over `2<y<3` proves (1.8); writing a closed endpoint at
`y=3` means the continuous limit `y upward 3`.  Letting `y` tend to `3` and
using `F(3)=4` gives (1.9).  This proves Theorem B.

Notice the direction of the theorem.  A cheap run assignment does not by
itself contradict universality when `D` is quadratic.  Instead, the physical
endpoint slack must pay for the discrepancy, and (1.8) measures the required
payment.

## 4. Atomic application

Assume

\[
                         \mu_a\Longrightarrow2\delta_x,
 \qquad4/3\le x\le3/2.                               \tag{4.1}
\]

The fixed-threshold seam theorem, with the optimized gap cutoff from
`MIXED_PROFILE_SEAM_NEXT.md`, gives the following precise limiting statement:
for every numerical `tau>0`, after choosing one fixed dangerous threshold
sufficiently close to `x`, it constructs a forward span-`4a+3` assignment
whose total cost satisfies

\[
 {Q\over a^3}\le 3x-S_*(x)+\tau+o(1).               \tag{4.2}
\]

No use of `D=o(a^2)` occurs in this construction.  The ingredients are:

1. atomic convergence supplies `(2+o(1))a` regular dangerous plateaux;
2. an absorbed seam consumes a positive fixed line in the interval
   `[x-1,2-x]`, with aggregate line capacity `3dt`;
3. the complement gaps have normalized total mass `3-2x+o(1)`;
4. every remaining seam with gap at most the chosen cutoff supplies a
   seam-local internal run;
5. the exact safe first-dangerous service intervals are pairwise disjoint;
   and
6. their optimized guaranteed saving is exactly `S_*(x)a^3-o(a^3)`.

All runs in the resulting assignment have cost at most `2a+O(1)` and lie in
the same forward windows as the original first-dangerous assignment.  Thus
Theorem B applies with

\[
                         U(x)=3x-S_*(x).              \tag{4.3}
\]

Taking `y=3` first proves (1.1) with `tau` subtracted from its numerator.
Letting `tau` tend to zero **after** the `a -> infinity` limit proves (1.1)
as stated.  No threshold depending on `a` is used.

### 4.1 Positivity and the uniform constant

The optimized saving is at least the saving obtained from the admissible
unoptimized cutoff `r=1`:

\[
 S_*(x)\ge S_0(x):=(8x-10)x(x-1).                   \tag{4.4}
\]

The independently audited polynomial calculation gives

\[
 S_0(x)-(3x-4)
 =8x^3-18x^2+7x+4\ge{8\over27}                     \tag{4.5}
\]

throughout `[4/3,3/2]`.  Equations (4.4)--(4.5) imply

\[
                 4-3x+S_*(x)\ge{8\over27},          \tag{4.6}
\]

which proves (1.3).  At `x=4/3`, the optimized saving is `4/9`, giving
(1.4).

### 4.2 Cap optimization at the balanced endpoint

At `x=4/3`, equation (4.2) has

\[
                         U=4-{4\over9}={32\over9}.   \tag{4.7}
\]

Put `t=3-y`.  Since

\[
                         F(3-t)=4-{t^3\over6},       \tag{4.8}
\]

Theorem B gives

\[
 {D_a\over a^2}\gtrsim
 R(t):={{4\over9}-{t^3\over6}\over7-t},
 \qquad0\le t<1.                                   \tag{4.9}
\]

The numerator is positive on this interval.  Differentiation gives

\[
 \operatorname{sgn}R'(t)
 =\operatorname{sgn}\!\left({4\over9}-{7\over2}t^2
                                  +{1\over3}t^3\right).       \tag{4.10}
\]

The expression in parentheses is strictly decreasing on `(0,1)`, changes
sign exactly once, and vanishes precisely at (1.7).  This proves (1.5).

### 4.3 Combination with the unconditional cross-line cutoff

The positive-seam/cross-line theorem in the inherited ledger proves, without
any hypothesis on `D`, that an atomic profile is geometrically impossible
when

\[
 x>1+{8-2\sqrt3\over13}=1.348\ldots .                \tag{4.11}
\]

Consequently the atomic branch has now been closed in the exact dichotomic
sense relevant to the three-box program:

* above (4.11), no selected middle ordering with that profile exists at any
  defect; and
* in the remaining narrow interval beginning at `4/3`, every such universal
  word has the positive quadratic defect supplied by Theorem A.

The quadratic statement remains valid, though vacuous, in the geometrically
impossible part of the interval.

## 5. A finite-band version

The same transfer removes `D=o(a^2)` from the conclusion of the uniform
mixed-band theorem.

Fix `x in [4/3,3/2]` and a sufficiently small numerical `epsilon>0`.  Suppose
the dangerous list contains between `(2-epsilon)a` and `(2+epsilon)a`
plateaux of normalized lengths in `[x-epsilon,x+epsilon]`, and at most
`epsilon a` other plateaux.  The finite proof in
`MIXED_PROFILE_SEAM_NEXT.md` constructs a forward assignment with

\[
 {Q\over a^3}\le U_\epsilon(x)+o(1),                 \tag{5.1}
\]

where

\[
\begin{aligned}
 C_\epsilon(x)
   &=8x-10-(10+x)\epsilon+\epsilon^2,\\
 U_\epsilon(x)
   &=3x+29\epsilon+15\epsilon^2\\
   &\quad-C_\epsilon(x)_+(x-\epsilon)(x-1-\epsilon).
                                                               \tag{5.2}
\end{aligned}
\]

For one absolute sufficiently small `epsilon_0`, compactness and the
uniform margin (4.5) give

\[
 \eta_\epsilon:=inf_{4/3\le x\le3/2}
                         (4-U_\epsilon(x))>0          \tag{5.3}
\]

whenever `0<epsilon<=epsilon_0` (after shrinking `epsilon_0` if necessary).
Theorem B therefore yields

\[
              \liminf {D_a\over a^2}
              \ge {\eta_\epsilon\over7}>0.           \tag{5.4}
\]

Thus an entire non-atomic neighbourhood of the atomic segment forces
quadratic defect; it is not merely forbidden at `D=o(a^2)`.

## 6. What the large-defect branch means

The three-box aggregation program seeks a uniform local estimate

\[
 g_3(p,q,r)\le w(p,q,r)+O((1+p+q+r)^{2-\delta})
\]

for some `delta>0`.  On the diagonal cube, the selected middle width is
`M_a=3a^2+O(a)`.  A lower bound

\[
                         D_a\ge\kappa a^2             \tag{6.1}
\]

is therefore already a constant-fraction local excess:

\[
 {N_a\over M_a}\ge1+{\kappa\over3}+o(1).             \tag{6.2}
\]

It does not need to be contradicted.  It is exactly the negative conclusion
that a subquadratic three-box construction cannot have this geometry.

This makes the use of `D=o(a^2)` logically harmless in a proof by
contradiction aimed at a quadratic local lower bound.  If no constant
`kappa>0` satisfied (6.1) for the local optimum, one could choose a sequence
of universal words with `D_a/a^2 -> 0`.  The small-defect theory would then
apply to that sequence.  Conversely, excluding every possible limiting
small-defect geometry would prove some positive quadratic lower bound by this
subsequence argument, even if it did not provide a numerical constant.

This observation does **not** solve the original Boolean-lattice problem.
The three-box lemma is one proposed route to an asymptotically optimal upper
construction.  Proving quadratic local excess would close that route
negatively, not construct the required global OR arrays.

## 7. The true surviving obstruction

The broad measure

\[
                         \mu(dx)=2\mathbf1_{[1,2]}(x)\,dx     \tag{7.1}
\]

from `MIXED_PROFILE_SEAM_NEXT.md` is the correct stress test.  For every
fixed threshold `1<c<2`, it admits a feasible reduced ledger with

\[
                         \mathcal U_c(\mu)>4.          \tag{7.2}
\]

The coupling and gap allocation are allowed to depend on `c`; line capacity
is aggregated as `3dt`.  Because the scalar seam method does not even produce
`U<4`, Theorem B yields no positive lower bound on `D` for this profile.
Adding a quadratic `D` error can only weaken the lower ledger further.

This is a genuine obstruction to the **method**, but not a realizable
counterexample.  The thresholdwise ledgers do not prove the existence of:

1. one successor order whose tail deletions induce every displayed coupling;
2. direction labels matching predecessor rises to successor fixed lines;
3. a placement of the prescribed gap mass in the cross-line desert;
4. compatible line intersections and additive triples; or
5. a permutation of `H_a`.

The exact missing theorem is therefore the following.

> **Multiscale realizability gap.**  Prove that every actual small-defect
> selected middle order has, at some common continuity threshold, a
> direction-labelled nested seam ledger with modified cost strictly below
> four; or construct one actual order realizing a compatible broad ledger.

Independent optimization at each threshold cannot establish this statement.
The couplings must be nested under deletion of shorter plateaux, or the three
direction resources and cross-line gap positions must be coupled globally.

## 8. Adversarial audit

### 8.1 Where `D=o(a^2)` was used

It was used only when (2.6) was simplified to `Q>=(4-o(1))a^3`.  The
seam-local maximum, high-line absorption capacity, gap count, safe service
intervals, first-dangerous upper cost, and optimized atomic saving do not use
small `D`.  Retaining `(7a+2)D` therefore gives a valid quantitative theorem.

### 8.2 Endpoint congestion

The coefficient is `7`, not `11`, because the assignment used here is
one-sided.  Every run lies to the right of its assigned index, so
`C_beta=0`; `C_alpha<=4a+3`.  The additional fan term is `hD`, giving
`(7a+2)D` at `h=3a-1`.  Using the symmetric universal span bound `11aD`
would be valid but weaker.

### 8.3 Omitted starts

The assignment omits only the final `4a+2` indices.  At cap `O(a)` these
cost `O(a^2)` in total.  There is no `O(aD)` or `O(a^2D)` penalty attached
to each omission.

### 8.4 Cap truncation

The cap optimization is restricted to `y>2`.  Dangerous peak plateaux have
edge length at most `2a`; fallback and seam-local runs are no longer than
`2a+O(1)`.  Thus
the total upper cost remains the ordinary, not capped, cost.  Nothing is
asserted for a cap below `2a`.

### 8.5 Oscillating defect

Every conclusion uses `liminf`.  Passing to a subsequence attaining a finite
defect-ratio liminf is legitimate.  If the liminf is infinite, the claimed
positive lower bound is automatic.  A large limsup by itself is irrelevant.

### 8.6 No hidden atomic concentration from the run spectrum

Atomicity is an explicit hypothesis on the plateau measure.  It is not
deduced from a capped average, and no pointwise ceiling on local run costs is
used.  The rejected `A'/B'`, poison-union, and staircase claims play no role.

### 8.7 Aggregate line capacity

Using `3dt` relaxes the three direction-labelled capacities.  This may
overestimate absorption and therefore underestimate the guaranteed saving.
That direction is safe for a lower bound on saving and hence safe for the
quadratic-defect conclusion.  It cannot certify realizability of the broad
ledger.

### 8.8 Meaning of the conclusion

`D=Omega(a^2)` is not an impossibility theorem for universal local words.
It says their length is a constant factor above the middle width.  It blocks
the subquadratic local-construction route but does not by itself settle the
global OR-array conjecture.

### 8.9 Remaining scalar obstruction

The broad ledger already survives with `D=0` in the reduced functional.
Therefore no rearrangement of the exact `(C+h)D` error can close the mixed
case.  A new constraint must enter before the defect transfer theorem can be
applied.

## 9. Theorem ledger

### Proved here

1. The exact finite lower cost (2.6), with the one-sided coefficient
   `(7a+2)D`.
2. The all-cap quantitative transfer Theorem B.
3. Atomic profiles `2 delta_x`, `4/3<=x<=3/2`, force the explicit quadratic
   defect (1.1), uniformly at least `8/189`.
4. The balanced atom forces at least `4/63` by the full lower-half cap and
   `0.0657...` after cap optimization.
5. The uniform mixed band in the audited stability theorem forces a positive
   quadratic defect, with explicit formula (5.4).
6. For proving a quadratic three-box lower bound, the branch
   `D` not `o(a^2)` is already the desired local excess rather than an
   unhandled case.

### Not proved

1. That every limiting plateau profile supplies a run assignment with
   `U<4`.
2. That the broad thresholdwise ledger is realizable by one order.
3. A direction-labelled or multiscale coupling theorem.
4. A quadratic lower bound for unrestricted three-box words.
5. A subquadratic three-box construction.
6. The all-`k` OR-array conjecture.

The next mathematical step is not another scalar optimization of `D`.  It is
to prove a nested-tail or direction-labelled realizability constraint strong
enough to make `U<4` for every actual small-defect order.  Theorem B will then
automatically convert that strict cost gap into a quadratic lower bound on
the local word length.
