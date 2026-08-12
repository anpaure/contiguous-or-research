# Period-eight depth-three Apéry clocks: full two-spike closure and canonical compression

**Date:** 2026-08-04  
**Status:** unconditional pure-mathematical theorem and reduction. It closes
the complete honest period-eight two-spike depth-three family. It also proves
that every period-eight depth-three gap word has a same-first-gap,
same-period canonical two-spike representative. It does not prove that this
compression is monotone for the Bellman functional.

## 1. The residual scalar

The preceding period-eight theorem reduces the honest two-spike family

\[
 (a,a,a,a,b,a,a,t),\qquad
 t\ge b,\qquad t>3a,\qquad b>t-a
\tag{1.1}
\]

to

\[
 v={t\over a}>3,\qquad
 \eta={t-b\over a},\qquad
 0\le\eta<1,\qquad
 D=7+2v-\eta,
\tag{1.2}
\]

and the endpoint-period scalar

\[
\boxed{
\begin{aligned}
 \mathcal E(v,\eta)
 ={}&C+g(1/D)
 +\sum_{j=2}^{4}f(j/D)
 -\sum_{j=1}^{3}f((v+j)/D)\\
 &+\sum_{j=1}^{3}g((v+j)/D),
\end{aligned}}
\tag{1.3}
\]

with

\[
                         \Phi(W)\ge\mathcal E(v,\eta).
\tag{1.4}
\]

Here

\[
 F(w)=\sum_{q\ge0}K(qA+w),\qquad
 f(x)=F(Ax),\qquad g(x)=\rho(Ax),\qquad C=F(0).
\tag{1.5}
\]

The previous theorem already proves

\[
 \mathcal E(v,\eta)>{333\over140000}
 \quad\hbox{when}\quad
 3<v\le{9+\eta\over2}.
\tag{1.6}
\]

## 2. Closure of the remaining scalar chamber

### Theorem 2.1

For every

\[
                         v>{9+\eta\over2},
\tag{2.1}
\]

one has

\[
 \boxed{
 \mathcal E(v,\eta)>{2283\over140000}>0.}
\tag{2.2}
\]

Consequently every honest two-spike word in (1.1) has

\[
                         \boxed{\Phi(W)>0.}
\tag{2.3}
\]

#### Proof

Condition (2.1) is equivalent to \(D>16\). Hence

\[
 0<{2\over D}<{3\over D}<{4\over D}<{1\over4}.
\tag{2.4}
\]

On the reflected ray,

\[
 {v+1\over D}>{1\over4}
\tag{2.5}
\]

because \(2v>3-\eta\), while

\[
 {v+3\over D}<{1\over2}
\tag{2.6}
\]

because \(\eta<1\). Thus all three reflected points lie in
\((1/4,1/2)\).

The authenticated compact-train bounds are

\[
 C>{57\over1400},\qquad
 f(x)>{57\over1400}\quad(0\le x\le1/4),
\tag{2.7}
\]

\[
 f(1/4)<{293\over6000},
\qquad
 f\ \hbox{is decreasing on }[1/4,1/2].
\tag{2.8}
\]

Therefore the three early values in (1.3) each exceed \(57/1400\), and
the three adverse reflected compact values each are smaller than
\(293/6000\).

The theta error is positive on \([1/4,1/2]\). Hence all three reflected
theta terms in (1.3) are positive, while

\[
                         g(1/D)>-{1\over20000}.
\tag{2.9}
\]

Substitution into (1.3) gives

\[
\begin{aligned}
 \mathcal E(v,\eta)
 &>4{57\over1400}
   -3{293\over6000}
   -{1\over20000}\\
 &={2283\over140000}>0.
\end{aligned}
\tag{2.10}
\]

This proves (2.2), and (1.4) proves (2.3). \(\square\)

Combining (1.6) and Theorem 2.1 closes the scalar on its full honest domain.

## 3. Every period-eight depth-three word has a canonical two-spike representative

Let an arbitrary honest period-eight depth-three word have first gap \(a\)
and period \(P\). Put

\[
                         \delta=P-8a.
\tag{3.1}
\]

### Theorem 3.1 (same-marginal two-spike compression)

One has

\[
                         \boxed{\delta>3a.}
\tag{3.2}
\]

There exist \(b',t'\) such that

\[
 (a,a,a,a,b',a,a,t')
\tag{3.3}
\]

is an honest depth-three word with the same first gap \(a\), the same
period \(P\), and hence the same exact threshold \(A=P+a\).

#### Proof

Use the exact period-eight notation

\[
\begin{aligned}
 \gamma_2+\gamma_3+\gamma_4&=3a+\ell,\\
 \gamma_5&=a+\beta,\\
 \gamma_6+\gamma_7&=2a+r,\\
 \gamma_8&=a+\tau,
\end{aligned}
\qquad \ell,\beta,r,\tau\ge0.
\tag{3.4}
\]

The two depth-three inequalities are

\[
 \tau>2a+\ell,
\qquad
 \beta>\tau+r-\ell-a.
\tag{3.5}
\]

Since

\[
 \delta=\ell+\beta+r+\tau,
\]

equations (3.5) give

\[
 \delta>2\tau+2r-a>3a.
\tag{3.6}
\]

Choose a number \(z\) satisfying

\[
 \max\left\{2a,{\delta\over2}\right\}
 <z<{\,\delta+a\over2}.
\tag{3.7}
\]

The interval is nonempty precisely because \(\delta>3a\). Set

\[
                         t'=a+z,\qquad b'=a+\delta-z.
\tag{3.8}
\]

Then

\[
 t'>3a,\qquad t'>b',\qquad b'>t'-a.
\tag{3.9}
\]

The period is

\[
 6a+b'+t'=8a+\delta=P.
\]

The exact two-spike classification therefore says that (3.3) is honest
and has depth three. \(\square\)

## 4. The exact remaining compression gate

Theorem 3.1 is combinatorial, not variational. It does not prove either

\[
 \Phi(W_{\rm original})\ge\Phi(W_{\rm two\text{-}spike})
\tag{4.1}
\]

or the analogous inequality for the endpoint-period comparisons.
Neither inequality follows merely from coordinatewise shift order because
the compact train is one-mode rather than globally monotone.

Thus period-eight depth-three positivity has been reduced to the following
single remaining statement:

> **Functional compression gate.** For every honest period-eight
> depth-three word, some same-\((a,P)\) canonical two-spike representative
> from Theorem 3.1 has endpoint-period value no larger than the original.

If this gate holds, the full two-spike closure above proves positivity of
every period-eight depth-three formal clock. The gate is not asserted here.

## 5. Scope and frozen dependencies

This theorem closes the complete sparsest two-spike face. It does not sign
arbitrary period-eight depth-three words, larger periods, higher overlap
depth, threshold overshoot, later first crossing, or finite physical
shoulders.

| role | file | SHA-256 |
|---|---|---|
| period-eight classification and scalar | MATH_THEOREM_APERY_FIRST_H3_EIGHT_PERIOD_TWO_SPIKE_SCALAR_20260804.md | 6bd6f88141be70ea8f6e5305f491c2745699baf32daf913f6d67253178b7eb92 |
| period-eight scalar self-audit | MATH_AUDIT_APERY_FIRST_H3_EIGHT_PERIOD_TWO_SPIKE_SCALAR_SELF_20260804.md | ae19e0344315a224407bd5f19533368b8bd1cf03c76236865c64dfcde0834646 |
| compact quarter bounds and decrease | MATH_THEOREM_COMPLEMENTARY_PAIR_TRAIN_AND_H4_INERT_SCALAR_REDUCTION_20260804.md | fc8b2dee92dd3bb9afab390c8507db51fec05c6ca4e9d46ac4948c7422d042a7 |
| theta half-interval positivity | MATH_LEMMA_THETA_HALF_INTERVAL_MONOTONICITY_AND_HALF_ROOT_SUMS_20260804.md | f974aeda114df4c933a396c06de51596bccd2fea18066412d45f7a18df62a0e3 |
