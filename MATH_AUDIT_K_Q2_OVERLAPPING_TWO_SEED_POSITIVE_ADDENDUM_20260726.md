# Audit of the positive 80-owner two-seed addendum

Date: 2026-07-26

Audited sections: 6A--6D of
MATH_ATTACK_K_Q2_OVERLAPPING_TWO_SEED_COMPLETION_20260726.md.

Method: pure mathematics only.

## 0. Verdict

**PASS.**  The four covers, the lower ledgers
\[
                         48,\ 32,\ 32,\ 16,
\]
the shifted upper ledgers, the common \(\mathbb Z_4\) colouring, the
all-length suspension, and the near-spanning tensor packing are exact.

The induced local operator is stronger than an aggregate mean identity.
Relative to the base corner, the 80 owners split into four pointwise
categories:
\[
\begin{array}{c|c}
\text{category}&\text{density}\\ \hline
\text{source type zero}&2/5\\
\text{first-bit death}&1/5\\
\text{second-bit death}&1/5\\
\text{surviving source type one}&1/5.
\end{array}
\]
The two death bits are disjoint, not independent.  Selecting corner \(11\)
on one touched gadget therefore erases a
\(\operatorname{Bernoulli}(2/5)\) type contribution pointwise.

Consequently the visible-gadget count needed at depth \(q\) is
\[
 L^*_{\varepsilon,q}
 ={5\over2}\Delta_{\varepsilon,q}
 ={5q(2m-2\varepsilon-q-1)\over4(2m-1)}
 ={5q\over4}+O_A(1).
\]
The disjoint product tensor, which sees at most \(q\) gadgets, still has the
wrong drift \(2q/5\) instead of \(q/2+O_A(1)\).  A construction with average
visibility \(5/4+o(1)\), rather than the old \(3/2+o(1)\), has no remaining
Gaussian full-pair-type obstruction.

## 1. The four exact covers

The special cycles
\[
\begin{aligned}
S_1&=(125,235,345,145),&
S_2&=(126,246,346,136),\\
S_3&=(134,146,156,135),&
S_4&=(234,245,256,236)
\end{aligned}
\]
are physical Johnson \(Q_2\)'s with disjoint direction pairs
\[
13|24,\qquad14|23,\qquad36|45,\qquad35|46.
\]
Their sixteen vertices are distinct.  The four missing special states are
\[
                         123,\ 124,\ 356,\ 456.
\]
Thus at each of four fixed reservoir orientations the four \(S_j\)'s give
four cells, for sixteen special cells total.  The four missing states each
support one vertical reservoir square.  Hence
\(\mathscr F_{11}\) consists of twenty disjoint \(Q_2\)'s and covers all
80 owners once.

\(\mathscr F_{00}\) has twenty vertical cells, while
\(\mathscr F_{10}\) and \(\mathscr F_{01}\) are instances of the already
proved \(\mathscr D(M;r)\) construction.  All four corners are therefore
literal factors on identical support.

## 2. Pointwise lower operator and aggregate ledgers

Put
\[
\begin{aligned}
\mathcal A&=\{125,126,345,346\},\\
\mathcal B&=\{134,234,156,256\},\\
\mathcal C&=\{123,124,356,456\},\\
\mathcal T&=\{135,136,145,146,235,236,245,246\}.
\end{aligned}
\]
The source full-pair type is one on
\(\mathcal A\dot\cup\mathcal B\dot\cup\mathcal C\) and zero on
\(\mathcal T\).  Every special state has four reservoir orientations, so
the four classes have owner sizes \(16,16,16,32\).

With the displayed square orientations, the exact touched-edge identity is
\[
 f_{\epsilon_1,\epsilon_2}(X,Y)
 =f_{00}(X,Y)
  -\epsilon_1\mathbf1_{\mathcal A}(X)
  -\epsilon_2\mathbf1_{\mathcal B}(X).
\]
Indeed \(\mathscr F_{10}\) moves precisely the \(\mathcal A\) states from
vertical cells into zero-type special edges, \(\mathscr F_{01}\) does the
same to \(\mathcal B\), and \(\mathscr F_{11}\) places both families in
zero-type special edges.  The \(\mathcal C\) states remain vertical, and
\(\mathcal T\) already has type zero.

It follows immediately that the type-one counts are
\[
                         48,\ 32,\ 32,\ 16,
\]
and each Boolean edge has signed difference \(16(e_0-e_1)\).  At corner
\(11\), the decrement indicator is
\[
                         \mathbf1_{\mathcal A\cup\mathcal B},
\]
which is Bernoulli \(2/5\) under the uniform owner measure.

## 3. Upper ledger

For a vertical cell, every upper edge contains one forced full reservoir
pair, and it contains a second full base pair exactly when its fixed
special state lies in
\(\mathcal A\cup\mathcal B\cup\mathcal C\).

For every special edge in \(S_1,\ldots,S_4\), the two special coordinates
outside its four-coordinate union form a nonbase pair.  Hence its special
union contains exactly one base full pair.  The fixed reservoir
orientation contributes no full reservoir pair.  Thus all 64 special
edges of \(\mathscr F_{11}\) have upper type one, while the 16 vertical
edges over \(\mathcal C\) have upper type two.

The first three factors are complement-stable, and the same direct count
applies to the fourth.  Therefore the upper ledgers are exactly the lower
table shifted from \(f_0,f_1\) to \(f_1,f_2\).

## 4. Common phase and suspension

On every vertical reservoir square,
\[
                         c(X\cup y_k)=g(X)+k
\]
runs cyclically through \(0,1,2,3\).  The only nonvertical square types in
\(\mathscr F_{10}\), \(\mathscr F_{01}\), and \(\mathscr F_{11}\) have
the colour sequences listed in the report, each equal to
\((0,1,2,3)\) or its reversal up to rotation.  These lists exhaust every
nonvertical cell.

Orienting each square in increasing colour order makes the lifted
tail-orientation fibre above a base owner depend only on its common colour,
not on its factor owner.  The standard direction word
\[
 \alpha,\beta,e_1,\ldots,e_{h-2},
 \alpha,\beta,e_1,\ldots,e_{h-2}
\]
therefore gives four exact factors of one identical lifted support, each
with twenty disjoint physical \(C_{2h}\)'s.  No phase mismatch remains.

This proves common-support all-length exactness.  It does not prove that
the full labelled depth-\(q\) carrier vectors are affine.

## 5. Packing constants

A ten-coordinate block is eligible with probability
\[
                         80/2^{10}=5/64.
\]
With \(B=\lfloor m/10\rfloor\), the half-mean threshold is \(5B/128\)
and the Chernoff failure is at most \(e^{-5B/512}\).  A family of
\(P=\lfloor m/2\rfloor\) spectator pairs has half-mean threshold \(P/4\)
and failure at most \(e^{-P/16}\).  Conditioning fair bits on total rank
\(m\) costs at most \(2(m+1)\).  Thus the stated retained-owner bound is
correct.

Selector stability follows because a varied local block remains in
\(\mathcal U\), a varied spectator pair remains split, and every unselected
block is frozen.  Tensoring \(r\) selected gadgets and \(s\) spectators
gives
\[
                         20^r\text{ copies of }Q_{2r+s}
\]
for each of \(4^r\) resolutions.  If \(h=2r+s\) is a power of two, the
Hamming factor gives exactly \(G/(2h)\) long cycles.

## 6. Birth--death comparison

For a product-transversal shallow window which touches \(q\) distinct
corner-\(11\) gadgets, the decrement is
\[
                         \operatorname{Bin}(q,2/5),
\]
so its mean and variance are
\[
                         {2q\over5},\qquad {6q\over25}.
\]
The exact target mean displacement in odd sector \(\varepsilon\) is
\[
 \Delta_{\varepsilon,q}
 ={q(2m-2\varepsilon-q-1)\over2(2m-1)}
 ={q\over2}+O_A(1).
\]
The disjoint tensor therefore leaves the exact mean gap
\[
 \Delta_{\varepsilon,q}-{2q\over5}
 ={q(2m-10\varepsilon-5q-1)\over10(2m-1)}
 ={q\over10}+O_A(1).
\]

At \(q=x\sqrt m+o(\sqrt m)\), the symmetric product law tends to
\(N(-2x/5,1/16)\), while the target tends to
\(N(-x/2,1/16)\).  A midpoint threshold gives
\[
 \liminf d_{\rm TV}
 \ge 2\Phi(x/5)-1.
\]

Conversely, after
\[
 L^*_{\varepsilon,q}={5\over2}\Delta_{\varepsilon,q}
\]
visible gadgets, the erased-binomial fluctuation is \(O_p(m^{1/4})\).
It vanishes on the \(\sqrt m\) type scale, so the resulting law has the
same Gaussian limit as the uniform target law.  The one-depth increments
of \(L^*\) are
\[
 L^*_{\varepsilon,q+1}-L^*_{\varepsilon,q}
 ={5(m-\varepsilon-q-1)\over2(2m-1)}
 ={5\over4}+O_A(m^{-1/2}).
\]

Thus the gadget improves the required overlap multiplicity from \(3/2\)
to \(5/4\), but a disjoint product still cannot reach constant-one target
mixing.

