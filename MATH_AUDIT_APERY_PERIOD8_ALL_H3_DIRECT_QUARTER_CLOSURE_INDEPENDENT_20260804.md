# Independent audit: complete period-eight depth-three direct closure

**Date:** 2026-08-04  
**Audited theorem:**
`MATH_THEOREM_APERY_PERIOD8_ALL_H3_DIRECT_QUARTER_CLOSURE_20260804.md`  
**Audited SHA-256:**
`93f40df626f7356ccb5dd890818fd9214f3db3f65cce9f649ca1db4270603815`  
**Verdict:** **GO after two endpoint/domain clarifications incorporated in
the source.**  The complete exact-first-carry period-eight `H=3` formal
branch is strictly positive with margin `859/210000`.  No computation or
search is used.

## 1. Period-eight reflected-ray domain

Overlap depth three implies at least three intervals, so `u>=3`.  The
general disjoint-ray inequality is

\[
                         u+1<8-u,
\]

which gives `u<=3`.  Hence `u=3`.

The three early and reflected endpoints are

\[
 X_i={s_{i+1}\over A},
 \qquad
 Y_i={A-s_{8-i}\over A},
 \qquad1\le i\le3.
\]

Strictly increasing shifts make both endpoint sequences strictly
increasing.  The carry inequalities give `X_i<=Y_i`.  Since `u=3`,
`s_5>A/2`; hence `Y_3=(A-s_5)/A<1/2`, and consequently every `X_i,Y_i`
lies in `(0,1/2)`.  These are exactly the domains used by the compact-train
and theta estimates.

The reflected-ray identity has no middle residue at `h=8,u=3`, because
the nominal middle range `u+2,...,h-u-1` is `5,...,4`.  Thus it reduces
exactly to

\[
 E(s)=C+g(\alpha)+
 \sum_{i=1}^3\bigl(f(X_i)-f(Y_i)+g(Y_i)\bigr).
\]

The exact-first-carry endpoint comparison gives `Phi(W)>=E(s)`.

## 2. Prefix minimality and terminal block maximality

Fix `1<=i<=7`.  Prefix minimality says that the initial cyclic block of
`8-i` gaps has minimum sum among all cyclic blocks of that length.  The
complement of any such block is a cyclic `i`-block, and the two sums add
to `P`.  Complementation reverses the order, so the complement of the
initial block—the terminal `i`-gap suffix—is a maximum cyclic `i`-block.

Every gap occurs in exactly `i` of the eight cyclic `i`-blocks, so their
average sum is `iP/8`.  Therefore

\[
 \gamma_7+\gamma_8\ge{P\over4},
 \qquad
 \gamma_6+\gamma_7+\gamma_8\ge{3P\over8}.
\]

Using `A=P+a`,

\[
 \begin{aligned}
 Y_2-{1\over4}
 &\ge {a+P/4\over P+a}-{1\over4}
 ={3a\over4(P+a)}>0,\\
 Y_3-{3\over8}
 &\ge {a+3P/8\over P+a}-{3\over8}
 ={5a\over8(P+a)}>0.
 \end{aligned}
\]

Hence

\[
                         Y_2>{1\over4},
 \qquad                  Y_3>{3\over8}>{1\over4},
\]

with strictness coming solely from `a>0`.  No compression or special gap
word is used.

## 3. Pair ending at or beyond the quarter

Assume

\[
                         0<X\le Y<1/2,
 \qquad                  Y\ge1/4.
\]

If `X>=1/4`, the compact train decreases on `[1/4,1/2]`, so
`f(X)>=f(Y)`, while `g(Y)>0` including at `Y=1/4`.

If `X<1/4`, use

\[
 f(X)>{57\over1400},
 \qquad
 f(Y)\le f(1/4)<{293\over6000},
 \qquad g(Y)>0.
\]

Thus in both cases

\[
 f(X)-f(Y)+g(Y)> {57\over1400}-{293\over6000}
 =-{341\over42000}.
\]

The non-strict endpoint `Y=1/4` is essential for the exhaustive first-pair
case split.  The final source now states it correctly.

## 4. Unrestricted first pair

When `Y<1/4`, also `X<1/4`.  The global half-interval upper bound and
theta absolute bound give

\[
 \begin{aligned}
 f(X)-f(Y)+g(Y)
 &>{57\over1400}-{61\over1000}-{1\over20000}\\
 &=-{71\over3500}-{1\over20000}.
 \end{aligned}
\]

When `Y>=1/4`, the preceding quarter lemma is stronger, because

\[
 {341\over42000}<{71\over3500}
 <{71\over3500}+{1\over20000}.
\]

Thus the first pair is completely covered, including the quarter endpoint.

## 5. Theta domains and signs

The minimum-gap theorem gives every cyclic gap at least `a`, so

\[
                         P\ge8a,
 \qquad
 0<\alpha={a\over P+a}\le{1\over9}<{1\over2}.
\]

Therefore

\[
                         g(\alpha)>-{1\over20000}.
\]

The terminal-block bounds put `Y_2,Y_3` strictly beyond the quarter, so

\[
                         g(Y_2)>0,
 \qquad                  g(Y_3)>0.
\]

The sign of `g(Y_1)` is not assumed; it is included in the unrestricted
first-pair loss.  This accounts for exactly two possible negative theta
charges: `g(alpha)` and `g(Y_1)`.

## 6. Exact rational margin and strictness

Apply the unrestricted bound to pair one, and the quarter bound to pairs
two and three.  Together with `C>57/1400` and the theta bound at `alpha`,

\[
 E(s)>{57\over1400}
       -{71\over3500}
       -2{341\over42000}
       -{2\over20000}.
\]

On denominator `420000`, the numerator ledger is

\[
 17100-8520-6820-42=1718.
\]

Hence

\[
 E(s)>{1718\over420000}
      ={859\over210000}>0.
\]

At least the cited train/theta inequalities are strict, so the final
margin is strict.  Since `Phi(W)>=E(s)`,

\[
                         \Phi(W)>{859\over210000}.
\]

## 7. Scope verdict

The proof covers every honest exact-first-carry period-eight formal clock
whose reflected-ray overlap depth is three.  It does not use or restore
the false same-marginal two-spike compression.  It does not cover period
nine or larger, threshold overshoot, a later first crossing, the finite
physical Apéry shoulder, endpoint-critical clocks, universal Bellman
positivity, or an OR-word upper bound.

