# Independent audit: full period-eight two-spike closure and canonical compression

**Date:** 2026-08-04  
**Target:** MATH_THEOREM_APERY_PERIOD8_TWO_SPIKE_FULL_CLOSURE_AND_CANONICAL_COMPRESSION_20260804.md  
**Target SHA-256:** 76f1ced69d953d0ed0d6f1b4dd20566fcf5d6a657158c4b6de5b349e155e8e27  
**Method:** direct reconstruction from the frozen scalar, train bounds, and
period-eight gap inequalities. The target's self-audit was not used as a
proof input.  
**Verdict:** **PASS / GO without source correction.**

No enumeration, solver, numerical search, Python, or H100 computation was
used.

## 1. Frozen inputs

The target's dependency hashes agree byte-for-byte:

| input | SHA-256 |
|---|---|
| period-eight scalar source | 6bd6f88141be70ea8f6e5305f491c2745699baf32daf913f6d67253178b7eb92 |
| compact quarter bounds and decrease | fc8b2dee92dd3bb9afab390c8507db51fec05c6ca4e9d46ac4948c7422d042a7 |
| theta half-interval lemma | f974aeda114df4c933a396c06de51596bccd2fea18066412d45f7a18df62a0e3 |

The inherited exact scalar is

\[
\begin{aligned}
 \mathcal E(v,\eta)
 ={}&C+g(1/D)
 +\sum_{j=2}^{4}f(j/D)
 -\sum_{j=1}^{3}f((v+j)/D)\\
 &+\sum_{j=1}^{3}g((v+j)/D),
 \qquad D=7+2v-\eta,
\end{aligned}
\]

and the literal clock satisfies \(\Phi(W)\ge\mathcal E(v,\eta)\).

## 2. Point-location audit for the new chamber

The new chamber is

\[
 v>{9+\eta\over2},\qquad v>3,\qquad0\le\eta<1.
\]

The first inequality is exactly \(D>16\), so

\[
 0<2/D<3/D<4/D<1/4.
\]

For the reflected points,

\[
 {v+1\over D}>{1\over4}
 \quad\Longleftrightarrow\quad
 2v>3-\eta,
\]

which follows strictly from \(v>3\). At the other endpoint,

\[
 {v+3\over D}<{1\over2}
 \quad\Longleftrightarrow\quad
 \eta<1.
\]

The intermediate reflected point lies between these. Thus all three
positive-sign early compact terms use the quarter lower bound, while all
three negative-sign reflected compact terms lie in the interval on which
the train decreases from its quarter value.

## 3. Train and theta ledger

The exact authenticated estimates are

\[
 C>{57\over1400},\qquad
 f(x)>{57\over1400}\quad(0\le x\le1/4),
\]

\[
 f(1/4)<{293\over6000},\qquad
 f\text{ decreasing on }[1/4,1/2].
\]

Hence the ceiling term plus three early terms contribute more than
\(4(57/1400)\), while the three adverse compact terms cost less than
\(3(293/6000)\).

The reflected theta arguments are all in \((1/4,1/2)\), where the theta
error is positive. The only potentially negative theta term is
\(g(1/D)>-1/20000\). Therefore

\[
\begin{aligned}
 \mathcal E
 &>4{57\over1400}
   -3{293\over6000}
   -{1\over20000}\\
 &={22800-20510-7\over140000}
 ={2283\over140000}>0.
\end{aligned}
\]

Every strict inequality is correctly oriented. Together with the older
\(D\le16\) chamber, this closes the full honest two-spike parameter domain.

## 4. Arbitrary depth-three excess audit

For an arbitrary period-eight depth-three word, write

\[
\begin{aligned}
 \gamma_2+\gamma_3+\gamma_4&=3a+\ell,\\
 \gamma_5&=a+\beta,\\
 \gamma_6+\gamma_7&=2a+r,\\
 \gamma_8&=a+\tau.
\end{aligned}
\]

The exact depth-three conditions yield

\[
 \tau>2a+\ell,\qquad
 \beta>\tau+r-\ell-a.
\]

With \(\delta=P-8a=\ell+\beta+r+\tau\),

\[
 \delta>2\tau+2r-a
 >4a+2\ell+2r-a
 \ge3a.
\]

Thus the claimed strict total-excess bound is correct.

## 5. Canonical representative audit

The interval

\[
 \max\{2a,\delta/2\}<z<(\delta+a)/2
\]

is nonempty if and only if \(\delta>3a\): the upper endpoint exceeds
\(2a\) exactly in that case, and it always exceeds \(\delta/2\) because
\(a>0\).

Set \(t'=a+z\), \(b'=a+\delta-z\). Then:

\[
 t'>3a
\]

because \(z>2a\);

\[
 t'>b'
\]

because \(z>\delta/2\); and

\[
 b'>t'-a
\]

because \(z<(\delta+a)/2\). These are stronger than the exact honest
two-spike conditions. The period calculation is literal:

\[
 6a+b'+t'=8a+\delta=P.
\]

Thus first gap, period, and exact threshold \(A=P+a\) are all preserved,
and the representative is honest with \(H=3\).

## 6. Compression-scope audit

The construction above is only a same-marginal combinatorial
representative. It proves neither

\[
 \Phi(W_{\rm original})\ge\Phi(W_{\rm two\text{-}spike})
\]

nor the analogous endpoint-period inequality. The source explicitly states
this in its status, Section 4, and final scope. It correctly identifies
functional monotonicity as an open gate rather than treating the
representative as a proof of arbitrary period-eight positivity.

## Final verdict

The complete two-spike family is closed, the same-\((a,P)\) representative
exists for every period-eight depth-three word, and no functional
comparison is claimed. The target is proof-safe as written.
