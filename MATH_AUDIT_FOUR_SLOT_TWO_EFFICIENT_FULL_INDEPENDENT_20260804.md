# Independent audit: complete four-slot two-efficient positivity

**Date:** 2026-08-04  
**Verdict:** **PASS**  
**Method:** pure algebra, Gaussian calculus, and exact rational arithmetic only;
no search, SAT/CP solver, remote machine, or floating-point sign decision was
used.

## 1. Frozen inputs and exact scope

Audited theorem:

`MATH_THEOREM_FOUR_SLOT_TWO_EFFICIENT_NORMALIZED_SUBRANGE_AND_PULSE_GATE_20260804.md`

SHA-256:

`47819d25abf75877b6bc723ed593354bb0e76582635996227ac9c48812b986c8`

The exact-rational replay artifact is

`scratch/n4_two_efficient_independent_audit_20260804/exact_rational_replay.py`

with SHA-256

`85efa0f6b48206f95660242b36827a3cdeeca0345d78222d40bd7eb7ae01f1ec`.

Running it locally gives `PASS: exact rational replay`.  Every assertion is
an inequality in `fractions.Fraction`; printed decimal approximations are not
used by the script.

This audit certifies only the theorem's stated scope: the complete
**two-slot-efficient** branch of the `n=4` Bellman problem.  It does not
certify the three-slot-efficient branch, the four-state Apéry branch, the
universal Bellman inequality, or any OR-word upper bound.

## 2. Normal form, transient, and three-slot reuse

The branch assumptions are

\[
 T=2y,\qquad x\le r=z-y\le y/2.
\]

In the source-open range, `A/2 <= y < A`, so
`0 <= x <= r < A/2`.  Directly, for `0<=u<=1/2`,

\[
 \log {h(1-u)\over h(1+u)}
 =4au-2\operatorname {artanh}u\ge0,
 \qquad a={\pi\over4},
\]

because its derivative is
`pi-2/(1-u^2)>0` on this interval.  Hence `K` is decreasing there and
`K(x)-K(r)>=0` has the stated direction.

For `y+r>=A`, the table `(0,x,y,y+r)` satisfies

\[
 y\ge2x,\qquad r\ge x,\qquad2(y+r)\le3y.
\]

It is therefore exactly the already-proved normalized three-slot regime-I
table.  Its Bellman sum is literally
`L_2(y;r)+K(x)-K(r)`; no term is dropped or compared.  The reduction in
Theorem 2.1 is sound.

## 3. Compact expansion and pulse identity

For `1/2<=t<1`, the unshifted train has compact indices `q=0,1`; all
later indices use the negative Gaussian tail (with the formulas agreeing at
the boundary).  If `s+t<1`, the shifted train likewise has compact indices
`q=0,1`; if `s+t>1`, only `q=0` is compact.  Expanding these terms gives
exactly (3.2) and (3.3).  At `s+t=1`, the disappearing compact contribution
is `1-exp(0)=0`, so the two formulas really do agree.

Direct integration of (4.1) gives

\[
 \sigma([v,\infty))=K(v).
\]

The even/odd split
`C(y/2)=C(y)+F_y(y/2)` is exact, and subtracting the two tail sums gives
the disjoint periodic half-cells in (4.3).  Gaussian absolute convergence
justifies the exchange of sum and signed measure.  Thus (4.4) is exact.

## 4. Low-period derivative and cell certificates

With `h(u)=u exp(-au^2)`, differentiation of the shifted train in the
two-compact region gives

\[
 {d\over ds}F_{At}(As)
 =2A^2\left(\sum_{q\ge0}h(1+s+qt)
             -h(1-s)-h(1-t-s)\right)
 =-2A^2W_t(s).
\]

Thus (5.14) has both the right scale and the right sign.

For the tail in (5.2), `h` is decreasing on the relevant interval and

\[
 \sum_{q\ge1}h(1+s+qt)
 \le h(x)+h(x+t)+{1\over t}\int_{x+t}^{\infty}h(u)\,du,
\]

which is precisely (5.2).  The second derivative calculation is also
sign-safe: `h''` is increasing on `[2/3,4/3]`, `h''(v)<=0`, both tail
arguments have nonnegative `h''`, and the final Gaussian-tail term is
strictly convex.  Hence `H_t''<0`, so endpoint checking is sufficient.

The replay artifact expands every quantity in (5.11)--(5.12) as a single
exact rational number.  All sixteen bounds in (5.13) are strict.  The
smallest margins above the displayed comparison constants occur at:

\[
\begin{array}{c|c|c}
\text{family}&i&\text{strict margin}\ 
\hline
B^{(0)}&0&>0\\
B^{(1)}&7&>0
\end{array}
\]

and the exact positive numerator and denominator of each margin are printed
by the hash-bound replay artifact.  This establishes Lemma 5.1 and Theorem
5.2 without a numerical approximation to `pi` or an exponential.

## 5. Lemma 6.1: enlarged monotonicity rectangle

On

\[
 2/3\le t\le4/5,\qquad0\le s\le1-t,
\]

one still has

\[
 1\pm s\in[2/3,4/3],\qquad
 v=1-t-s\in[0,1/3],
\]

and both tail arguments exceed `3/2`.  The concavity proof for `H_t`
therefore transfers without changing a sign.

At `s=1-t`, the exact arguments are

\[
 t,\quad2-t,\quad0,\quad2,\quad2+t.
\]

The `h(t)` term is bounded below by the minimum of its two endpoint lower
bounds because `h` is unimodal; every negatively signed term in (6.5) is
evaluated at the endpoint where it is largest.  The denominator and
Gaussian argument in the final tail term are likewise both worst at the
left endpoint.

The exact replay verifies all sixteen rational inequalities in (6.6).  The
smallest margins occur at `i=7`, and are exactly positive for both
`D_i^(0)-1/40` and `D_i^(1)-1/2000`.  Thus the critical-point method is only
needed for `t>=4/5`, as claimed.

## 6. Lemma 6.2: independent line-by-line audit

Put

\[
 u=1-s,\quad v=1-t-s,\quad w=1+s,\quad d=w+t.
\]

### 6.1 Critical identity and tail pricing

At an interior critical point, the derivative identity is exactly

\[
 h(u)+h(v)=\sum_{q\ge0}h(w+qt).
\tag{A}
\]

For every `q>=1`, `w+qt>=d`, whence

\[
 e^{-a(w+qt)^2}={h(w+qt)\over w+qt}
 \le {h(w+qt)\over d}.
\]

Summing and using (A) proves (6.9), including the `-h(w)` term.  In this
strict interior region, the shifted train has exactly two compact terms.
Replacing its complete Gaussian tail by (6.9) gives (6.10); there is no
unpaid or double-counted term.

After multiplication by `d`, the coefficients are

\[
 d+u=2+t,\qquad d+v=2,\qquad d-w=t,
\]

so the three-Gaussian collapse (6.11) is exact.  With `q=1-t`, `p=s`, it
becomes (6.12) on the exact triangle `0<=p<=q<=1/5`.

### 6.2 Direction of the `q` reduction

Differentiating (6.12) gives exactly

\[
 G_q=-2+E(1-p)+E(1+p)+4a(q-p)E(q-p).
\]

The exact rational Taylor bounds give

\[
 E(1-p)<{2\over3},\qquad E(1+p)<{1\over2},
 \qquad4a(q-p)E(q-p)<{22\over35}.
\]

Their sum is `377/210<2`, leaving the exact derivative budget
`43/210`.  Hence `G_q<0`, so the minimum really is at the **largest**
allowed `q`, namely `q=1/5`.  The direction used in the theorem is correct.

### 6.3 Strong convexity

For `E(x)=exp(-ax^2)`, `E''` is increasing on `[4/5,6/5]`.  Monotonicity
in the rational parameter `a` and the degree-eight Taylor upper bound give

\[
 E''(1)<{5\over12},\qquad E''(6/5)<{13\over20}.
\]

The exact margins replay to

\[
 {11564900567125\over1566597272297676}>0
\]

and

\[
 {1106801691988021367\over112285938337733975180}>0,
\]

respectively.

For `0<=x<=1/5`,

\[
 -2E''(x)
 >4{157\over200}{164\over175}{339\over350}
 ={2182143\over765625}>{27\over10}.
\]

Consequently

\[
 G_*''>{27\over10}-{14\over5}{5\over12}
                -{4\over5}{13\over20}
 ={76\over75}>1.
\]

### 6.4 Endpoint data and quadratic loss

At `p=0`, the formulas reduce exactly to

\[
 G_*(0)={18\over5}(1-e^{-a})-2e^{-a/25}
\]

and

\[
 G_*'(0)=2-4ae^{-a}-{4a\over5}e^{-a/25}.
\]

Replacing the exponentials only in the sign-safe direction gives the two
strict rational statements (6.18)--(6.19).  The replayed margins above the
stated bounds are

\[
 {503671511911690427004484115532164185782667001661382141131
  \over
  105082634064794488648723308508607459338190981032541529188600}>0
\]

and

\[
 {205023359668225010655055020797614860233
  \over
  24463593351823817444481245599347403482260}>0.
\]

Since `G_*''>1`,

\[
 G_*(p)>G_*(0)+G_*'(0)p+{p^2\over2}.
\]

The minimum possible loss from the final two terms is `-1/800`, attained
at `p=1/20`.  Therefore

\[
 G_*(p)>{3\over200}-{1\over800}={11\over800}>0.
\]

This verifies every implication from (6.8) through (6.20).

## 7. Final minimization and verdict

For fixed `t>=4/5`, the compact `s` interval has only three kinds of
minimizer:

* `s=0`, where `L_2=2C(y)>0`;
* `s=1-t`, where `y+r=A` and Theorem 2.1 with zero transient (`x=r`)
  gives `L_2>0`;
* an interior critical point, where Lemma 6.2 gives `F_y(r)>0` and the
  all-ceiling theorem gives `C(y)>0`.

The transient is nonnegative everywhere in this branch.  Hence Theorem 6.3
is proved in its stated scope.

**Final independent verdict: PASS.**
