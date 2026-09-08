# Audit of the growing-block threshold, transverse toll, and compiler scale

Date: 2026-07-26

Method: pure mathematics only. No computation, search, solver, or web input
is used.

## 0. Verdict

The three reports

* `MATH_THEOREM_GROWING_BLOCK_PROFILE_SADDLE_THRESHOLD_20260726.md`,
* `MATH_THEOREM_GROWING_BLOCK_PROFILE_ROBUST_CROSSING_TOLL_20260726.md`, and
* `MATH_THEOREM_GROWING_BLOCK_PROFILE_THRESHOLD_AND_DIVERSE_COMPILER_ESCAPE_20260726.md`

are mutually consistent.  Their sharp common conclusion is as follows.
Let

\[
 W=\binom{2m}{m},\qquad H=A\sqrt m+O(1),\qquad
 \Lambda_b={2^b\over b}.
\]

For the full-\(b\)-block profile deficit \(\Delta_{b,q}\),

\[
 \log {\Delta_{b,H}\over \binom{2m}{m-H}}
 =-\left({A^2\over4}+o(1)\right)\Lambda_b
\]

when \(b\to\infty\) and \(2^b=o(\sqrt m)\).  At one Gaussian depth
every growing \(b\) therefore destroys the former linear deficit.  The
deficient strata themselves disappear at

\[
                         2^b\sim {2\over A}\sqrt m.
\]

The simultaneous depth ledger has the different sharp asymptotic

\[
 {1\over W}\sum_{q\le H}\Delta_{b,q}
 =\left({2\over3\sqrt\pi}+o(1)\right)
       {\sqrt m\over\Lambda_b^{3/2}}.
\]

Hence the full-block dual is \(o(W)\) over all protected depths exactly
on the escape side

\[
                         \Lambda_b\gg m^{1/3}.
\]

This is only an audit of this dual.  It is not a coefficient-one theorem.

## 1. Exact monotonicity

Let \(A_{r,k}\) count rank-\(r\) sets containing exactly \(k\) full
blocks.  For one block the rank/full indicator array has entries

\[
 c(j,0)=\binom bj\quad(0\le j<b),\qquad c(b,1)=1.
\]

Every ordered \(2\times2\) minor is nonnegative.  Products and
marginalization preserve TP\(_2\), equivalently convolution of these
arrays preserves TP\(_2\).  Thus \((A_{r,k})\) is TP\(_2\), and for
\(q>0\)

\[
             {A_{m,k}\over A_{m-q,k}}
\]

is nondecreasing in \(k\).  Therefore the positive target-deficit profiles
form one initial interval.  This exact fact validates using a single saddle
crossing; there are no omitted remote deficit islands.

The coefficient formula

\[
 A_{r,k}=\binom nk[z^{r-bk}]\bigl((1+z)^b-z^b\bigr)^{n-k}
\]

also shows that the crossing solves

\[
 {m\over2^b-1}-{b2^{b-1}\over2^b-1}k={q\over2}.
\]

## 2. One-depth saddle

The conditional mean number of full blocks is

\[
 \lambda_b={2m\over b2^b}(1+o(1)),
\]

and the crossing lies

\[
                         {A\sqrt m\over b}(1+o(1))
\]

below that mean.  Its conditional variance is \(\lambda_b(1+o(1))\).
Consequently the moderate-deviation cost is

\[
 {1\over2\lambda_b}\left({A\sqrt m\over b}\right)^2
 =\left({A^2\over4}+o(1)\right){2^b\over b}.
\]

If \(2^b/\sqrt m\to c\in(0,2/A)\), the displacement is a fixed fraction
of the rare-block mean and the correct Poisson rate is

\[
 \log {\Delta_{b,H}\over N_H}
 =-\left[{2\over c}I(1-Ac/2)+o(1)\right]{\sqrt m\over b},
 \qquad I(x)=1-x+x\log x.
\]

For \(c>2/A\), the formal crossing is negative.  Since the likelihood
ratio is increasing in \(k\), positivity at \(k=0\) proves
\(\Delta_{b,H}=0\) exactly for all large \(m\).

## 3. All-depth constant

Put

\[
 \varepsilon_b={2b\over2^b},\qquad
 z={q\over\sqrt{\varepsilon_bm}}.
\]

On bounded \(z\)-ranges the source-target experiment is locally normal.
The standardized mean shift is \(\varepsilon_bz+o(\varepsilon_b)\),
while

\[
 \log(W/N_q)=\varepsilon_bz^2+o(\varepsilon_b).
\]

Thus, with \(\phi,\Phi\) standard normal,

\[
 {\Delta_{b,q}\over W}
 =(1+o(1))\varepsilon_bz
       \{\phi(z)-z\Phi(-z)\}.
\]

The \(z\)-mesh is \((\varepsilon_bm)^{-1/2}\), and exponential tilting
gives an integrable Gaussian envelope.  Hence

\[
 {1\over W}\sum_{q\le H}\Delta_{b,q}
 =(1+o(1))\sqrt m\,\varepsilon_b^{3/2}
 \int_0^\infty z\{\phi(z)-z\Phi(-z)\}\,dz.
\]

Tonelli gives

\[
 \int_0^\infty z\{\phi(z)-z\Phi(-z)\}\,dz
 ={1\over3\sqrt{2\pi}},
\]

which yields the constant \(2/(3\sqrt\pi)\).  The contributing depths are

\[
                         q\asymp\sqrt{{2mb\over2^b}},
\]

not \(q\asymp H\).  This verifies why the aggregate transition is at
\(\Lambda_b\asymp m^{1/3}\), earlier than the half-logarithmic
one-depth disappearance threshold.

## 4. Exact transverse toll

Let \(K_q=\{k:T_{b,q}(k)>S_b(k)\}\).  An occurrence whose owner and
target profiles both stay on the same side of \(K_q\) cannot increase the
number of distinct targets hit in \(K_q\).  Therefore, outcome by outcome,

\[
 B_{b,q}^{\times}+M_{b,q}^{\pm}\ge
 \Delta_{b,q}:=\sum_k(T_{b,q}(k)-S_b(k))_+,
\]

separately for both signs.  Here \(B^{\times}\) counts depth-\(q\)
windows containing a cross-block physical axis, and \(M\) counts unhit
targets in the deficient profiles.  The stronger variation form is

\[
 \sum_X|F_b(T_X)-F_b(X)|+M_{b,q}^{-}\ge\Delta_{b,q}.
\]

If \(E_b^{\times}\) counts directed cross-block transitions, one
transition occurs in at most \(q\) depth-\(q\) windows.  Summing gives

\[
 {H(H+1)\over2}E_b^{\times}+sum_{q\le H}M_{b,q}^{\pm}
 \ge\sum_{q\le H}\Delta_{b,q}.
\]

Thus, when the aggregate holes are negligible compared with this dual,

\[
 {E_b^{\times}\over W}
 \ge\left({4\over3A^2\sqrt\pi}+o(1)\right)
 {1\over\sqrt m}\left({b\over2^b}\right)^{3/2}.
\]

This is necessary, not sufficient.  The directed earth-mover refinement
in the crossing report is stronger when missing targets are controlled in
the corresponding weighted norm.

The preceding (H^2) denominator is deliberately unconditional but is
not sharp near the all-depth threshold.  A fixed constant-factor band

\[
 q\asymp q_*:=\sqrt{m/\Lambda_b}
\]

already contains a constant fraction of the aggregate profile deficit.
On that band (D_{b,q}\asymp W/\Lambda_b), there are
\(\Theta(q_*)\) depths, and one transition belongs to only (O(q_*))
of the relevant windows at each depth.  Hence, if
\(\Lambda_b=O(m^{1/3})\) and the total hole budget is (o(W)), the sharper
necessary bound is

\[
 {E_b^{\times}\over W}
 =\Omega\!\left({1\over\sqrt{m\Lambda_b}}\right).
\]

At the critical scale this requires \(\Omega(W/m^{2/3})\) cross
transitions and \(\Omega(W)\) exceptional signed window occurrences.

## 5. Named regimes and the compiler correction

For \(b=c\log_2m\), the all-depth deficit has scale

\[
 {1\over W}\sum_{q\le H}\Delta_{b,q}
 \asymp (\log m)^{3/2}m^{(1-3c)/2}.
\]

Thus \(c=1/3\) is the power threshold, with the exact escape boundary

\[
 b={1\over3}\log_2m+\log_2\log_2m+\omega(1).
\]

For \(b=m^\alpha\), every full-block deficit is eventually empty.  The
same is true for a hypothetical block size
\(b=R\asymp\sqrt{mH}=m^{3/4}\).

In the actual rank-twisted compiler, however, \(R\) is not an invariant
block size.  The union of the rank-dependent matchings inside
\(A_j\dot\cup C_j\) is \(K_{d,d}\), so its coordinate-union components
have size

\[
                         b=2d.
\]

Therefore the actual full-profile escape criterion is

\[
                         {2^{2d}\over2d}\gg m^{1/3},
\]

or equivalently

\[
 d>{1\over6}\log_2m+{1\over2}\log_2\log_2m+\omega(1).
\]

The customary logarithmic macroblocks satisfy this with slack.  Increasing
\(R\) without increasing or crossing the macroblock components does not
affect this dual.

## 6. Exact boundary

There is no full-block-profile no-go covering all \(b=o(m)\).  Below the
all-depth threshold, a construction must pay the displayed crossing or
hole toll.  Above it, this particular dual is already \(o(W)\).  What
remains is the arbitrary-weight dispersed Hall/covariance problem; none of
the results audited here proves coefficient one.
