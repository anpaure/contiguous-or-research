# Closure of the two h=4 inert faces by a compact Gaussian slope bound

**Date:** 2026-08-04  
**Status:** unconditional pure-mathematical theorem.  It proves the
one-dimensional compact Gaussian gate and therefore closes both inert
faces of the five-slot size-four-efficient branch.  Together with the
separate active-threshold theorem, the entire h=4 branch is positive.  No
search or sampled numerical estimate is used.

We retain the notation of
`MATH_THEOREM_H4_INERT_ONE_DIMENSIONAL_COMPACT_GAUSSIAN_GATE_20260804.md`:

\[
A={\sqrt\pi\over2},
\quad C(\tau)=F_\tau(0),
\quad C=C(A),
\quad F_q=F_A(A/4),
\tag{0.1}
\]

\[
\eta_-=(C-F_q)_+,
\qquad
\eta_+=(F_q-C)_+,
\tag{0.2}

and

\[
\Xi(\delta)
=\max_{0\le u\le(A-4\delta)/5}
\left[
{u\over6}+\max\{\eta_+,\Delta_K(u,\delta)\}
\right].
\tag{0.3}

The remaining sufficient gate is

\[
C(A+\delta)>\eta_-+\Xi(\delta)+{1\over10000}
\qquad(0\le\delta\le A/4).
\tag{0.4}

## 1. Exact quarter-shift mismatch

### Lemma 1.1

One has

\[
                         F_q>C,
\qquad
0<\eta_+=F_q-C<{1\over800},
\qquad
\eta_-=0.
\tag{1.1}

### Proof

The following rational Gaussian bounds are direct positive-Taylor
certificates using `333/106<pi<22/7`; the two displayed tails are then
geometric:

\[
\begin{array}{c|cc}
 &\text{lower}&\text{upper}\\ \hline
e^{-\pi/4}&4559/10000&9119/20000\\
e^{-\pi}&27/625&2161/50000\\
e^{-9\pi/4}&1/1250&213/250000\\
e^{-9\pi/64}&1607/2500&643/1000\\
e^{-25\pi/64}&2931/10000&733/2500\\
e^{-81\pi/64}&187/10000&47/2500\\
e^{-169\pi/64}&3/12500&13/50000
\end{array}
\tag{1.2}

and

\[
\sum_{n\ge4}e^{-\pi n^2/4}<{1\over250000},
\qquad
\sum_{j\ge0}e^{-\pi(17/4+j)^2/4}<{1\over1000000}.
\tag{1.3}

For completeness, every entry in (1.2) follows by evaluating the positive
Taylor polynomial and its alternating/geometric remainder through degree
fourteen at the two rational bounds on `pi`; cross multiplication gives
the displayed fractions.  In (1.3), divide successive terms and bound by
the first ratio.

Now

\[
C=1-2e^{-\pi/4}-e^{-\pi}-e^{-9\pi/4}
  -\sum_{n\ge4}e^{-\pi n^2/4}.
\]

Equations (1.2)--(1.3) give

\[
                         {5503\over125000}<C<{221\over5000}.
\tag{1.4}

On the other hand,

\[
F_q
=1-e^{-9\pi/64}-e^{-25\pi/64}-e^{-81\pi/64}
   -e^{-169\pi/64}
   -\sum_{j\ge0}e^{-\pi(17/4+j)^2/4},
\]

so the same bounds give

\[
                         {44739\over1000000}<F_q<{1129\over25000}.
\tag{1.5}

The lower bound in (1.5) exceeds the upper bound in (1.4), proving
`F_q>C`.  Moreover

\[
F_q-C
<{1129\over25000}-{5503\over125000}
={142\over125000}<{1\over800}.
\]

This proves (1.1). \(\square\)

## 2. Two compact bounds for the kernel loss

### Lemma 2.1 (slope bound)

On `A/4<=w<=A/2`,

\[
                         0<-K'(w)<{3\over10}.
\tag{2.1}

### Proof

Put `a=A^2=pi/4`, `t=w/A`, and

\[
h(r)=r e^{-ar^2}.
\]

Then

\[
-K'(At)=2A\bigl(h(1-t)-h(1+t)\bigr).
\tag{2.2}

The bracket is positive on `1/4<=t<=1/2`; equivalently
`2 arctanh(t)<pi t`, which follows from
`arctanh(t)<=4t/3` and `8/3<pi`.

More precisely,

\[
h(1-t)-h(1+t)
=\left(e^{-a(1-t)^2}+e^{-a(1+t)^2}\right)
  \left(\tanh({\pi t\over2})-t\right).
\tag{2.3}

The first factor is `1-K(At)<1`, since the kernel decreases through
`A/2` and `K(A/2)>0`; the latter also follows directly from
`e^(-pi/16)<4109/5000` and `e^(-9pi/16)<171/1000`.  It remains to prove

\[
                         \tanh({\pi t\over2})-t<{1\over6}.
\tag{2.4}

The left side is strictly concave.  At `t=1/4`, use `tanh x<x` and
`pi<22/7`; at `t=1/2`, use
`tanh(pi/4)<2/3`, equivalently `e^(pi/2)<5`.

At a possible interior critical point put

\[
p={2\over\pi},
\qquad q=\sqrt{1-p}.
\]

Then the critical value is `q-p arctanh(q)`.  Since

\[
\operatorname{arctanh}(q)>q+{q^3\over3}+{q^5\over5},
\]

it is less than

\[
(1-p)^{3/2}\left(1-{p\over3}-{p(1-p)\over5}\right).
\tag{2.5}

This expression decreases in `p` on the relevant interval, while
`p>7/11`.  At `p=7/11` it equals

\[
{8\over11\sqrt{11}}{1346\over1815}<{1\over6};
\]

the last inequality follows by squaring positive integers.  This proves
(2.4).  Finally `A<8/9` gives

\[
-K'(At)<{2A\over6}<{8\over27}<{3\over10}.
\]

\(\square\)

### Lemma 2.2 (range bound)

For every admissible `u,delta`,

\[
\boxed{
\Delta_K(u,\delta)
<\min\left\{{3\delta\over10},{57\over1000}\right\}.
}
\tag{2.6}

### Proof

The mean-value theorem and Lemma 2.1 give the first bound.  Since every
interval in the definition of `Delta_K` lies inside `[A/4,A/2]`, monotone
decrease also gives

\[
\Delta_K(u,\delta)
\le K(A/4)-K(A/2).
\]

The additional exact bounds

\[
e^{-\pi/16}<{4109\over5000},
\qquad
e^{-9\pi/16}<{171\over1000}
\tag{2.7}

together with the lower quarter-shift bounds in (1.2) yield

\[
\begin{aligned}
K(A/4)-K(A/2)
&=e^{-\pi/16}+e^{-9\pi/16}
  -e^{-9\pi/64}-e^{-25\pi/64}\\
&<{569\over10000}<{57\over1000}.
\end{aligned}
\]

This proves (2.6). \(\square\)

## 3. Two ceiling endpoints and concavity

### Lemma 3.1

The ceiling train is increasing and strictly concave in its period on
`[A,infinity)`.  Moreover

\[
C(A)>{57\over1400},
\qquad
C(6A/5)>{63\over1000}.
\tag{3.1}

### Proof

Write

\[
C(\tau)=M-\sum_{q\ge1}e^{-(A+q\tau)^2},
\qquad M=1-2e^{-\pi/4}.
\]

Each summand after the minus sign has positive first derivative and
negative second derivative for `tau>=A`, because `A+q tau>=2A` and
`2(2A)^2=2pi>1`.  This proves monotonicity and strict concavity.  The first
bound in (3.1) is the frozen ceiling estimate.

For the second, `M>11/125`.  At `tau=6A/5`, the first tail exponent is
`121pi/100`, and successive exponents differ by at least `42pi/25`.
Positive Taylor estimates give

\[
e^{121\pi/100}>44,
\qquad
e^{42\pi/25}>100.
\]

Therefore

\[
\sum_{q\ge1}e^{-(A+6qA/5)^2}
<{1/44\over1-1/100}
={25\over1089}<{1\over40},
\]

and hence

\[
C(6A/5)>{11\over125}-{1\over40}={63\over1000}.
\]

\(\square\)

## 4. The scalar gate is positive

### Theorem 4.1

For every `0<=delta<=A/4`,

\[
\boxed{
C(A+\delta)>\eta_-+\Xi(\delta)+{1\over10000}.
}
\tag{4.1}

### Proof

By Lemmas 1.1 and 2.2,

\[
\eta_-=0,
\qquad
\Xi(\delta)
<{A-4\delta\over30}
+\max\left\{{1\over800},
             \min\left({3\delta\over10},{57\over1000}\right)
      \right\}.
\tag{4.2}

There are three intervals.

### (i) `0<=delta<=1/240`

The maximum in (4.2) is `1/800`, and its right side decreases with
`delta`, while `C(A+delta)` increases.  At `delta=0`, use `A<8/9`:

\[
{57\over1400}
-{4\over135}-{1\over800}-{1\over10000}
={36797\over3780000}>0.
\tag{4.3}

### (ii) `1/240<=delta<=19/100`

Now (4.2) becomes

\[
                         \Xi(\delta)<{A\over30}+{\delta\over6}.
\tag{4.4}

The function

\[
C(A+\delta)-{A\over30}-{\delta\over6}-{1\over10000}
\]

is concave, so its minimum on this interval occurs at an endpoint.  At
`delta=1/240`, (3.1) gives the positive lower margin

\[
{57\over1400}-{4\over135}-{1\over1440}-{1\over10000}>0.
\]

At `delta=19/100`, note that `19/100>A/5`, so monotonicity and Lemma 3.1
give `C(A+delta)>63/1000`.  On the other side,

\[
{A\over30}+{19\over600}+{1\over10000}
<{4\over135}+{19\over600}+{1\over10000}
={16577\over270000}<{63\over1000}.
\tag{4.5}

### (iii) `19/100<=delta<=A/4`

The compact range bound is now active, so the right side of (4.2) is

\[
{A-4\delta\over30}+{57\over1000},
\]

which decreases with `delta`; the ceiling train increases.  Its worst
endpoint is again `delta=19/100`, already settled by (4.5).

All intervals satisfy (4.1). \(\square\)

## 5. Consequence

### Corollary 5.1

Every five-slot size-four-efficient internally superadditive first-crossing
Bellman table has strictly positive functional.

### Proof

Monotone endpoint normalization reduces the branch to the active threshold
face `T=A` and the two inert faces `T=P+x`, `T=y+z`.  The separate threshold
theorem closes the active face.  Theorem 4.1 verifies the sufficient compact
gate for both inert faces, and the endpoint-period Bellman lower bound then
forces their literal functionals positive. \(\square\)

## 6. Scope

This closes the size-four-efficient branch at grid size five.  It does not
close the size-three- or size-five-efficient branches, all five-slot
tables, the universal Bellman inequality, or an OR-word construction.
