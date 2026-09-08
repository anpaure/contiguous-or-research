# Audit of Fable §8c: run spectrum, neighbor exceedance, and the claimed staircase

## 1. Outcome

The run-spectrum inequality in §8c has a correct and useful core.  With the
span convention used in `THREE_BOX_PHASE_SEPARATION_RESEARCH.md`, its exact
form is

\[
 \operatorname{Def}_R(h)
 :=\sum_{i=1}^{M_a}(h-\lambda_i)_+
 \le B_a(h)+(C_\alpha+C_\beta+h)D
 \le B_a(h)+(2\sigma+h)D,                 \tag{1.1}
\]

where

\[
 B_a(h):=hM_a-|S_h|,
 \qquad M_a=3a^2+3a+1,                   \tag{1.2}
\]

and the chosen run at every index is internal, avoids that index, and has
one-sided span at most `sigma`.  This is valid for every fixed witness
selection, every fixed admissible run assignment, and every `h`
simultaneously.  No assumption `D=o(a^2)` is needed for (1.1).

The deductions made from (1.1) in §8c are much too strong, however.  In
particular, (1.1) gives a **capped sum law**, not concentration at individual
indices.  It does not imply that all but `o(a^2)` indices have avoiding runs
of length `(4/3-o(1))a`, and it certainly does not imply that every local run
near almost every index is that long.  Consequently the asserted partition
into rides, the `9a/4` ride count, the three-phase handoff, and the exact
transportation equations are not forced theorems.

The strongest staircase-like conclusion currently proved is weaker but
still substantial:

> In a covering word with `D=o(a^2)`, the selected-middle order contains,
> for every fixed `0<delta<4/3`, `Theta_delta(a)` long directed peak
> plateaux, each on a central coordinate line and longer than
> `(4/3-delta)a`; a positive-density set of length-`(4a+2)` windows contains
> only such long peak plateaux.  These corridors occupy
> `Omega_delta(a^2)` positions in total.  They need not partition the
> order, and their transitions are not classified.

This is exactly the corridor theorem already proved in
`UNIVERSAL_CAPPED_RUN_COVER.md`.  The proposed “staircase windmill” remains
one possible extremal geometry, not the uniquely forced geometry.

## 2. Exact audit of Theorem I

Select one middle witness

\[
 I_i=[\ell_i,r_i],\qquad
 \ell_i=i+\alpha_i,\quad r_i=i+\beta_i,
 \quad w_i=\beta_i-\alpha_i,
\]

for each of the `M_a` middle targets.  Fix an assignment
`i -> R_i=[u_i,v_i]` of internal threshold runs such that `i` is not in
`R_i`, and put `lambda_i=v_i-u_i`.  Suppose its one-sided span is at most
`sigma`, in the precise convention

\[
 v_i+1-i\le\sigma\quad(i<u_i),
 \qquad i-(u_i-1)\le\sigma\quad(i>v_i).   \tag{2.1}
\]

The capped heterogeneous run lemma gives

\[
 \sum_i\min(w_i,h)
 \le \sum_i\min(\lambda_i,h)
       +(C_\alpha+C_\beta)D.              \tag{2.2}
\]

Every fixed adjacent increment of `alpha` can be charged by at most
`sigma` indices, and the same is true for `beta`; hence

\[
 C_\alpha\le\sigma,\qquad C_\beta\le\sigma. \tag{2.3}
\]

Fan-capped avoidance says

\[
 |S_h|\le\sum_i\min(w_i,h)+hD.            \tag{2.4}
\]

Combining (2.2)--(2.4), and using

\[
 \sum_i\min(\lambda_i,h)
   =hM_a-\sum_i(h-\lambda_i)_+,
\]

proves (1.1).  This also proves the simultaneity in `h`: once the witnesses
and runs are fixed, the same deterministic inequalities may be applied at
every cap.

If only a subset `J` is assigned, the exact statement is

\[
 |S_h|\le
 \sum_{i\in J}\min(\lambda_i,h)+(M_a-|J|)h
 +(C_\alpha+C_\beta+h)D.                 \tag{2.5}
\]

Equivalently, set `lambda_i=h` at an unassigned index when discussing that
one cap.

### 2.1 The off-by-one in the universal span

The universal peak theorem puts a rightward run inside
`[i+1,i+4a+2]`.  Under (2.1), this implies

\[
 v_i+1-i\le4a+3,                          \tag{2.6}
\]

not `4a+2`.  Thus its automatic congestion constant is `4a+3`.  This is an
irrelevant asymptotic one-unit correction, but the exact ledger in §8c.1
uses the wrong convention.  The forward/backward windows cover every index
without a gap for `a>=3`; the isolated small case `a=2` needs a separate
choice at its central index and is irrelevant to the asymptotic statement.

### 2.2 Exact budgets

Let `N_q` be the number of points at distance `q` below the middle rank.
For `1<=q<=a`, `N_q=M_a-q^2`; for `a<q<=3a`,
`N_q=binom(3a-q+2,2)`.  Therefore, for `1<=h<=3a-1`,

\[
 B_a(h)=\sum_{q=1}^h(M_a-N_q).            \tag{2.7}
\]

In particular, for `h<=a`,

\[
 B_a(h)=\sum_{q=1}^h q^2
 =\frac{h(h+1)(2h+1)}6.                   \tag{2.8}
\]

Thus the small-cap statement is

\[
 \operatorname{Def}_R(h)
 \le \frac{h(h+1)(2h+1)}6+(2\sigma+h)D,  \tag{2.9}
\]

not merely `h^3/3+O(aD)`; there is also an `O(h^2)` term if one writes an
asymptotic expansion.

The clean full-lower-half cap is `h_*=3a-1`, because the zero point is not a
target.  Here

\[
 |S_{h_*}|=V_a
 =4a^3+\frac92a^2+\frac32a-1             \tag{2.10}
\]

and

\[
 B_a(h_*)
 =5a^3+\frac32a^2-\frac32a.              \tag{2.11}
\]

Consequently

\[
 \sum_i\min(\lambda_i,3a-1)
 \ge V_a-(2\sigma+3a-1)D.                \tag{2.12}
\]

For the universal span `sigma=4a+3`, the error coefficient is `11a+5`.
If `D=o(a^2)`, (2.12) gives average capped run cost

\[
 \frac1{M_a}\sum_i\min(\lambda_i,3a-1)
 \ge (4/3-o(1))a.                         \tag{2.13}
\]

This is the valid meaning of the `4a/3` constant.

### 2.3 Quantifiers and assignment dependence

The phrase “any assignment” in Theorem I is correct, but it must not be
read as “every nearby run is long.”  What is proved is:

* fix one admissible run at every index;
* the capped costs of those chosen runs satisfy (1.1);
* because congestion follows only from span, one may in particular choose
  at each index a minimum-cost run among the span-bounded admissible runs.

The last choice gives an order-invariant statistic

\[
 \lambda_\sigma^*(i)
 =\min\{\lambda(R):R\text{ is internal, avoids }i,
                    \text{ and has one-sided span }\le\sigma\}. \tag{2.14}
\]

Equation (1.1) holds for this minimum assignment as well.  It controls the
**sum of the minima**.  It does not give a pointwise lower bound on those
minima, and a fortiori does not control all other runs.

For `0<=t<h`, the actual exceptional-set consequence is

\[
 \#\{i:\lambda_\sigma^*(i)\le t\}
 \le
 \frac{B_a(h)+(2\sigma+h)D}{h-t}.         \tag{2.15}
\]

This follows because each counted index contributes at least `h-t` to
`Def_R(h)`.  Formula (2.15), optimized over `h`, is the strongest direct
pointwise statement furnished by Theorem I.

At thresholds proportional to `a`, the right side of (2.15) is generally
`Theta(a^2)`, not `o(a^2)`.  In particular it gives no almost-everywhere
claim at `t=(4/3-o(1))a`.

### 2.4 A concrete logical counterexample to concentration

The failure is not a minor Markov-inequality issue.  At leading order the
entire spectrum (all caps, not just `h=3a-1`) permits the following abstract
distribution:

* `3/5` of the indices have `lambda=a`;
* `2/5` have `lambda=2a`.

Write `x=h/a`.  Its normalized deficiency is

\[
 a^{-3}\operatorname{Def}(h)=
 \begin{cases}
 0,&0\le x\le1,\\
 \frac95(x-1)+o(1),&1\le x\le2,\\
 3x-\frac{21}{5}+o(1),&2\le x\le3.
 \end{cases}                              \tag{2.16}
\]

The normalized budget is

\[
 a^{-3}B_a(h)=
 \begin{cases}
 x^3/3+o(1),&0\le x\le1,\\
 -x^3/6+3x^2/2-3x/2+1/2+o(1),&1\le x\le3.
 \end{cases}                              \tag{2.17}
\]

The right side of (2.17) dominates (2.16) throughout `[0,3]` (even the
larger coefficient `2(x-1)` and the larger tail `3x-4` fit).  Hence the
run-spectrum inequalities alone are compatible with a positive majority
of all indices having run cost only `a`, far below `4a/3`, compensated by
the remaining indices of cost `2a`.

This abstract spectrum need not itself come from an order; its role is to
disprove the claimed logical implication from Theorem I.  Any theorem that
rules it out must use additional geometric information.

## 3. Audit of Corollary H

The first sentence of Corollary H is correct, but it is not sharp.  If all
middle targets use literal singleton witnesses, then `w_i=0`.  Applying
Lemma B at cap `a` indeed gives

\[
 D\ge |S_a|/a=(8/3-o(1))a^2.             \tag{3.1}
\]

Cap `h=1` is stronger.  Since `|S_1|=M_a-1`, it gives

\[
 D\ge M_a-1=3a^2+3a.                     \tag{3.2}
\]

More generally, let `K` selected middle witnesses have width at most
`r<h`.  Since the other widths contribute at most `h`, Lemma B gives the
exact distributional bound

\[
 K(h-r)\le B_a(h)+hD.                    \tag{3.3}
\]

For literal witnesses (`r=0`) and `h=1`,

\[
 K\le D+1.                               \tag{3.4}
\]

Thus a word with `D=o(a^2)` really does use literal middle witnesses only
at `o(a^2)` indices.

What is not proved is the sentence that almost every middle witness has
width at least `(8/9-o(1))a`.  The cap-`a` inequality proves only

\[
 \frac1{M_a}\sum_i\min(w_i,a)
 \ge (8/9-o(1))a.                        \tag{3.5}
\]

As with run lengths, a capped average is not concentration.  Even the
leading all-cap inequalities permit, abstractly, one third of the widths
to be `2a/3` and two thirds to be `2a`; this has a positive fraction well
below `8a/9`.  The valid replacement for every claimed width-density
statement is (3.3).

## 4. Audit of Theorem J

There is a correct local scalar lemma here.

Let consecutive middle points be `p=T_i`, `q=T_{i+1}`, and suppose
`q_c>p_c`.  Put `tau=p_c+1`.  The maximal component `R=[i+1,v]` of
`T_j(c)>=tau` containing `q`

* starts at `i+1`, because `p_c<tau<=q_c`;
* avoids `i`;
* is internal unless it reaches the right word boundary; and
* has one-sided span

\[
 v+1-i=\lambda(R)+2,                     \tag{4.1}
\]

not `lambda+1` under the audited convention `lambda=|R|-1`.

Also, every pair of distinct points on the same rank is incomparable.
Thus every consecutive pair has a coordinate which increases (and one
which decreases).  This is the simple reason behind the final sentence of
Theorem J.

The invalid step is “hence for all but `o(a^2)` indices it must have length
at least `(4/3-o(1))a`.”  Theorem I supplies no such concentration.

A correct global version is the following.  Let `K_t` be a set of indices
at which one can choose an **internal** neighbor-exceedance run of cost at
most `t`, with `t+2<=sigma`.  Use those runs at the indices in `K_t` and any
span-`sigma` admissible runs elsewhere.  Then for every `t<h`,

\[
 |K_t|\le
 \frac{B_a(h)+(2\sigma+h)D}{h-t}.         \tag{4.2}
\]

Short right-boundary exceedance runs affect at most `6a` indices: for each
of the three coordinates and each of its `2a` nontrivial thresholds there
is only one final threshold component and hence only one possible start.
There is an analogous `6a` bound at the left boundary.  They can be added
as an `O(a)` exceptional term if both orientations are used.

Two further distinctions matter:

1. A neighbor-exceedance run is generally a nonconstant superlevel
   component.  It need not be a constant-coordinate plateau or a ride on a
   line.
2. A peak plateau is a special threshold run and is a line ride, but a
   lower threshold may join several varying-coordinate portions.  Thus
   long threshold runs do not by themselves imply the plateau geometry
   asserted after Theorem J.

## 5. What geometry is actually forced

Use the universal peak assignment from `UNIVERSAL_CAPPED_RUN_COVER.md`.
For each forward window of length `L=4a+2`, let `q_i` be the minimum cost of
an internal peak plateau contained in that window.  Then

\[
 q_i\le2a,
\]

the assignment has congestion `O(a)`, and it omits only `O(a)` tail
indices.  Applying the corrected Theorem I at `h=3a-1` gives, whenever
`D=o(a^2)`,

\[
 \sum_i q_i\ge(4-o(1))a^3.               \tag{5.1}
\]

Proposition 8 and Lemmas 9--10 of `UNIVERSAL_CAPPED_RUN_COVER.md` now give
the following theorem.

### Theorem K (the proved long-corridor consequence)

For every fixed `0<delta<4/3`, at least

\[
 \left(\frac{3\delta}{2/3+\delta}-o(1)\right)a^2       \tag{5.2}
\]

forward windows have

\[
 q_i>(4/3-\delta)a.                    \tag{5.3}
\]

Consequently the order contains `Theta_delta(a)` distinct peak plateaux
with more than `(4/3-delta)a` positions.  Each is a directed subsequence of
one coordinate line, its other coordinates are strictly monotone, and its
fixed level satisfies

\[
 |c|<(2/3+\delta)a+O(1).                 \tag{5.4}
\]

Their plateau-edge sets are pairwise disjoint, so there are only `O(a)` of
them, while (5.2) gives the matching `Omega_delta(a)` lower bound.  Their
total occupied mass is `Omega_delta(a^2)`.  For `delta<1/3`, two such
plateaux cannot lie on the same geometric coordinate line, because their
combined lengths exceed the `2a+1` points available on that line for all
sufficiently large `a`.

This is the strongest proved bridge from the run spectrum to line
geometry.  It forces a positive-density corridor packing, not a partition.

## 6. Ledger for the six claimed staircase consequences

1. **Every ride has length at least `(4/3-o(1))a`: not proved.**  Theorem K
   supplies only `Theta(a)` long peak rides accounting for a positive
   density of windows.  Other positions and shorter rides may remain.

2. **At most one ride per line: conditionally correct only for rides longer
   than `a+1/2`.**  It applies to the long plateaux in Theorem K when
   `delta<1/3`; it says nothing about shorter plateaux.

3. **About `9a/4` rides which partition the hexagon: not proved.**  The
   count divides the total mass by an assumed common ride length and hence
   already assumes the missing partition.  The proved count is only
   `Theta_delta(a)` and has no `9/4` constant.

4. **Three-phase cyclic handoff: not proved.**  A nonconforming seam can
   create a short exceedance run locally, but (4.2) permits a positive
   density of short-run indices at proportional thresholds.  No argument
   shows every seam, or all but `o(a)` seams, is conforming.  Nor does a
   long superlevel component have to become the next constant-coordinate
   ride.

5. **Drifting trapezoid trajectory: heuristic.**  It is a description of
   one way to satisfy the proposed handoffs, not a consequence of the
   capped sum law.

6. **Exact line-cover transportation equations: conditional tautology,
   not a forced theorem.**  They follow if rides are already known to
   partition every point exactly once.  That premise is precisely what has
   not been proved.

The “design window”

\[
 (4/3)a\lesssim L\lesssim(1+1/\sqrt2)a
\]

is a correct crude feasibility calculation **inside the conjectural
one-ride-per-line partition model**.  It does not establish that every
surviving order belongs to that model.

## 7. Status of the advertised consequences

* A hypothetical assignment with every selected run of cost `a` is indeed
  incompatible with `D=o(a^2)`, by (2.12).  This is a valid conditional
  “minimal windmill dies” statement.
* The ring cost estimate was explicitly marked “machine check pending” in
  §8a, so §8c cannot relabel it proved merely by invoking Theorem I.
* The random-order `Omega(a^2)` assertion was explicitly marked heuristic
  in the earlier ledger because its maximal-gap/dependence argument was
  missing.  Theorem I proves the implication from a cheap random run cover,
  not the existence of that cover with high probability.
* `SHORT_PEAK_DENSITY.md` gives an explicit order in which only
  `(3/8+O(1/a))` of the universal windows contain a peak of cost at most
  `a`.  This independently rules out the proposed route from a universal
  high density of short peaks to the staircase conclusion.

## 8. Correct replacement for §8c

The durable theorem ledger should read:

1. **Proved:** the exact run-spectrum inequality (1.1), with universal
   span `4a+3` in the audited convention.
2. **Proved:** the minimum-span-run exceptional bound (2.15).
3. **Proved:** literal middle witnesses satisfy `K<=D+1`; general width
   tails satisfy (3.3).
4. **Proved:** the local neighbor-exceedance lemma and its aggregate form
   (4.2), with an `O(a)` boundary correction.
5. **Proved:** the long-corridor Theorem K.
6. **Open:** whether every such corridor packing admits a cheap
   heterogeneous run assignment (`(4-epsilon)a^3`), or whether a rotating
   triangular braid escapes it.
7. **Conjectural:** ride partition, `9a/4` count, exact three-phase handoff,
   trapezoid waves, and exact line-transport equations.

The next genuinely mathematical gate is therefore not to solve the exact
transportation problem of the asserted staircase.  It is first to prove a
**transition lemma** for the much larger class allowed by Theorem K:

> A positive-density packing of long directed central-line peak plateaux
> either creates enough short non-peak threshold components near its joins
> to lower the capped assignment cost below `(4-epsilon)a^3`, or obeys a
> rigorously stated global braid law.

Only the second outcome would justify passing to a staircase/transportation
classification.
