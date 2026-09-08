# Independent mathematical audit of the product route after DRAY

## Verdict

\[
\boxed{\textbf{PASS}}
\]

I audited `PRODUCT_ROUTE_AFTER_DRAY_NO_GO_20260724.md` independently and
without web search, computation, or finite experimentation.  The main
claims are correct:

1. the Rayleigh order-statistic event has exact limiting mass \(1/5\);
2. every compact subcone of the dominant sector contributes
   \(\Omega(W(k))\) aggregate excess for fixed positive block proportions;
3. the separate-three-box architecture fails for every sequence of
   three-way block splits, including fixed, vanishing, and zero-dimensional
   blocks;
4. fully merging extra atomic factors into three macroblock SCDs does not
   change the relevant height histograms;
5. for a fixed positive-proportion \(d\)-block split, the exact averaged
   gate is
   \[
   \mathbb E E_d(L_1,\ldots,L_d)=o(k^{(d-1)/2});
   \]
6. APF is used only as one sufficient route to the four-box gate, never as
   a necessary condition.

The source now states the origin convention exactly: the fully anchored
abstract ledger includes every local origin, and passing to the nonzero-word
convention deletes the unique global empty mask, shifting that ledger by at
most one.  Thus the literal lower ledger can be

\[
W(k)+\sum E_3-1
\]

rather than exactly \(W(k)+\sum E_3\).  This is precisely the distinction
now made in Section 4.  It changes none of the normalized lower bounds, and
the later formula with an \(O(\mathcal B_k)\) origin term is also safe.

---

## 1. The SCD height law is normalized correctly

For an SCD of the \(s\)-cube, a chain of edge height \(h\) starts in rank

\[
a=\frac{s-h}{2}.
\]

The number of such chains is forced by rank counting:

\[
c_s(h)=\binom sa-\binom s{a-1}.
\]

Hence the chain-height multiset is independent of the chosen SCD.  This
already proves the histogram-invariance statement later used for
macroblocks.

For \(h=y\sqrt s\), the local central-binomial ratio and the difference of
successive binomial coefficients give

\[
\frac{c_s(h)}{W(s)}
\sim \frac{2y}{\sqrt s}e^{-y^2/2}.
\]

The allowed heights lie on a mesh of spacing \(2/\sqrt s\), so the limiting
density is indeed

\[
f_Y(y)=ye^{-y^2/2},\qquad y>0.
\]

Thus the normalization in equation (4) of the source is the standard
Rayleigh law, with no missing factor of two.  Independent choices of chains
from disjoint block SCDs give independent limiting heights.

The deletion-of-zero-letters observation is also literal.  Deleting all
zero relative letters compresses every old interval to a contiguous
interval of the remaining word, and it does not change the maximum of a
nonzero witness.  Only the zero target itself can disappear.

---

## 2. Exact order-statistic mass \(1/5\)

Let

\[
Z_i=Y_i^2/2.
\]

Then the \(Z_i\) are independent rate-one exponentials.  For one prescribed
ordering of the two smaller variables and one prescribed largest variable,

\[
\{Y_1<Y_2,\ Y_3>2Y_2\}
=\{Z_1<Z_2,\ Z_3>4Z_2\}.
\]

Conditioning on \(Z_2=t\) gives

\[
\begin{aligned}
\Pr(Z_1<Z_2,\ Z_3>4Z_2)
&=\int_0^\infty(1-e^{-t})e^{-4t}e^{-t}\,dt\\
&=\int_0^\infty(e^{-5t}-e^{-6t})\,dt\\
&=\frac15-\frac16=\frac1{30}.
\end{aligned}
\]

There are three choices of the largest variable and two orders of the
smaller variables.  The six events are disjoint outside a null tie set, so

\[
\Pr(Y_{(3)}>2Y_{(2)})=6\cdot\frac1{30}=\frac15.
\]

Joint weak convergence transfers this to the three equal-block SCD heights.
The event boundary consists only of ties and the hypersurfaces
\(Y_i=2Y_j\), all null under the continuous limiting density.  Thus parity
of the finite height lattice causes no loss.

For unequal fixed positive proportions \(\alpha_i\), the scaled variables
have densities

\[
f_{\alpha_i}(x)=\frac{x}{\alpha_i}e^{-x^2/(2\alpha_i)},
\]

which are strictly positive on \((0,\infty)\).  Therefore every nonempty
open rectangle compactly contained in

\[
0<x<y,\qquad z>2y
\]

has positive limiting probability.  The proof does not require a uniform
positive probability over all block proportions; it needs only a positive
constant for each fixed proportion triple.

---

## 3. Uniform DRAY loss on compact dominant cones

Let

\[
(p,q,r)=\sqrt k\,(x,y,z)
\]

lie in a compact subset of

\[
0<x<y,\qquad z>2y.
\]

The compactness margins imply

\[
p=\Theta(\sqrt k),\quad q=\Theta(\sqrt k),\quad
r-2q=\Omega(\sqrt k).
\]

In particular \(r>p+q\), since \(p<q\).  Hence the finite DRAY theorem
applies, the width is

\[
M=(p+1)(q+1)=\Theta(k),
\]

and

\[
\frac{r-\varepsilon}{2}-q=\Omega(\sqrt k).
\]

Also

\[
s_0=p+q+2=\Theta(\sqrt k),\qquad
K=\Theta(\sqrt k),\qquad B=s_0+O(1).
\]

The last estimate follows more sharply than is needed: because

\[
K=2\left\lfloor\frac{M}{2s_0}\right\rfloor,
\]

one has \(0\le M-Ks_0<2s_0\), while \(K=\Theta(\sqrt k)\).  Thus the DRAY
numerator is \(\Omega(k^{3/2})\) and its denominator is \(O(\sqrt k)\),
giving

\[
E_3(p,q,r)\ge \kappa_C k.
\]

Keeping the leading terms gives exactly the source's refined expression

\[
\frac{E_3(p,q,r)}k
\ge
\frac{xy(z-2y)}{z+5x+5y}-o_C(1).
\]

Indeed, \(B\sim(x+y)\sqrt k\) and

\[
h+2B\sim\frac{z+5x+5y}{2}\sqrt k,
\]

while the numerator is

\[
\frac{xy(z-2y)}2k^{3/2}+o(k^{3/2}).
\]

---

## 4. Compact-cone mass aggregates to \(\Omega(W(k))\)

For fixed positive block proportions,

\[
\mathcal B_k=W(s_1)W(s_2)W(s_3)
\]

is the number of product boxes.  Central-binomial asymptotics give

\[
\frac{\mathcal B_k}{W(k)}
\sim
\frac{2}{\pi\sqrt{\alpha_1\alpha_2\alpha_3}}\frac1k.
\]

Choose any closed rectangular set \(C\) with nonempty interior compactly
contained in the dominant cone.  Its limiting probability is some
\(\pi_C>0\), and every corresponding box has excess at least
\(\kappa_Ck\).  Therefore

\[
\frac{\mathcal B_k\mathbb E E_3}{W(k)}
\ge
\frac{2\kappa_C\pi_C}
{\pi\sqrt{\alpha_1\alpha_2\alpha_3}}+o(1).
\]

This verifies both scales in the source:

* the bad sector contains a positive fraction of boxes;
* there are \(\Theta(W(k)/k)\) such boxes and each costs \(\Theta(k)\), so
  their total isolated excess is \(\Theta(W(k))\).

The exact product-SCD width identity

\[
\sum_{\rm boxes}w_3=W(k)
\]

then turns the excess lower bound into a leading-constant obstruction.

### The corrected origin ledger

For every positive-height local box, \(g_3=w_3+E_3\).  For an all-zero
abstract box, \(g_3=0\) and \(w_3=1\), while its nonempty translated origin
restores the width unit.  Counting every abstract local origin gives the
fully anchored ledger used by the source.  Passing to the genuine
nonzero-word convention removes the unique global zero and can shift the
ledger by at most one.  Consequently writing

\[
L_{\rm sep}=W+\sum E_3+O(\mathcal B_k)
\]

is always valid.  The revised source records this convention explicitly,
so there is no remaining ledger defect.

---

## 5. Audit of every arbitrary-split branch

Let

\[
0\le s_1\le s_2\le s_3,\qquad s_1+s_2+s_3=k.
\]

The universal estimate

\[
\frac{W(s_1)W(s_2)W(s_3)}{W(k)}
\asymp
\frac{\sqrt{k+1}}
{\sqrt{(s_1+1)(s_2+1)(s_3+1)}}
\]

is correct with absolute implicit constants.  Each case in Section 5
then closes as follows.

### 5.1 All three block sizes tend to infinity

The height windows

\[
p\in[\sqrt{s_1},2\sqrt{s_1}],\quad
q\in[4\sqrt{s_2},5\sqrt{s_2}],\quad
r\in[12\sqrt{s_3},13\sqrt{s_3}]
\]

have product probability bounded below by an absolute positive constant.
They imply

\[
p<q,qquad r-2q\ge2\sqrt{s_3}.
\]

In the disparate-scale DRAY estimate,

\[
M=\Theta(\sqrt{s_1s_2}),
\]

the dominance margin is \(\Omega(\sqrt{s_3})\), and the denominator is
\(O(\sqrt{s_3})\).  Since \(M/s_0=\Theta(\sqrt{s_1})\to\infty\), the
condition \(K\ge2\) holds.  Therefore

\[
E_3=\Omega(\sqrt{s_1s_2}).
\]

Multiplying by the product-box ratio yields

\[
\sqrt{s_1s_2}\,rac{W(s_1)W(s_2)W(s_3)}{W(k)}
\asymp \sqrt{\frac{k}{s_3+1}}=\Omega(1).
\]

No comparability among \(s_1,s_2,s_3\) is being assumed here.

### 5.2 The smallest block is fixed positive, the other two grow

Suppose \(s_1=d\ge1\).  Every SCD of the \(d\)-cube has exactly one chain
of height \(d\), so selecting it has probability \(1/W(d)\), a fixed
positive constant.  This probability factor is implicit in the source and
does not affect the order calculation.

Choose

\[
q\in[a\sqrt{s_2},b\sqrt{s_2}],
\qquad
r\in[C_d\sqrt{s_3},(C_d+1)\sqrt{s_3}]
\]

with fixed \(0<a<b\).  The number of nonzero box targets is

\[
T=(d+1)(q+1)(r+1)-1.
\]

A length-\(N\) word has at most \(N(N+1)/2\) intervals, so

\[
N\ge\frac{\sqrt{8T+1}-1}{2}.
\]

Because \(s_3\ge s_2\), choosing \(C_d\) sufficiently large makes this
strictly larger than

\[
(1+\delta_d)(d+1)(q+1).
\]

At the same time \(r>d+q\), so the width is exactly
\((d+1)(q+1)\).  Hence

\[
E_3=\Omega_d(\sqrt{s_2}).
\]

After aggregation,

\[
\sqrt{s_2}\,rac{W(d)W(s_2)W(s_3)}{W(k)}
\asymp_d\sqrt{\frac{k}{s_3+1}}=\Omega_d(1).
\]

### 5.3 Only the largest block grows

After passage to a subsequence, \(s_1,s_2\) are fixed.  If both are
positive, select their unique longest chains and take
\(r=\Theta(\sqrt{s_3})\).  The target count is \(\Theta(r)\), so interval
counting gives

\[
g_3=\Omega(\sqrt r)=\Omega(s_3^{1/4}),
\]

whereas the local width is fixed.  The selected family has
\(\Theta(W(k))\) boxes, up to a fixed multiplicative constant, so the
normalized excess actually diverges.

### 5.4 One block is zero-dimensional

If \(s_1=0<s_2\), the local problem is two-dimensional.  A witness for
\((i,0)\) must contain an actual letter \((i,0)\), and similarly for
\((0,j)\).  These \(p+q\) required values are distinct, proving

\[
g_2(p,q)\ge p+q.
\]

For \(p\le q\), the width is \(p+1\), hence

\[
E_2(p,q)\ge q-1.
\]

If \(s_2\to\infty\), choose separated Rayleigh windows so that
\(p\asymp\sqrt{s_2}\) and \(q\asymp\sqrt{s_3}\) with \(p<q\).  If
\(s_2\) is fixed positive, choose its unique longest chain instead.  In
both cases the aggregate normalized contribution is bounded below (and is
usually divergent).

### 5.5 Two blocks are zero-dimensional

If \(s_1=s_2=0\), then a one-dimensional word covering
\(1,\ldots,r\) needs at least one occurrence of every value, so
\(g_1(r)\ge r\).  A positive fraction of SCD chains have
\(r=\Theta(\sqrt k)\), while there are \(W(k)\) chains.  The normalized
excess therefore diverges.

### 5.6 Exhaustion of all sequences

If the claimed positive liminf failed, there would be a subsequence on
which the nonnegative normalized excess tends to zero.  Passing to further
subsequences makes \(s_2\) either bounded or divergent, and, in the latter
case, makes \(s_1\) either fixed or divergent.  The cases above exhaust all
possibilities and contradict convergence to zero.  This validates the
source's stronger statement for every sequence of three-way splits.

---

## 6. Macroblock histogram invariance

The number of chains of every height in an SCD of an \(S\)-cube is forced
by rank counts and equals

\[
\binom S{(S-h)/2}-\binom S{(S-h)/2-1}.
\]

Consequently, if several atomic Boolean blocks are fully merged by any
valid SCD/outer-hook merge tree into a macroblock of dimension \(S\), the
final height histogram is exactly the same as that of every other SCD of
the \(S\)-cube.  For three disjoint macroblocks, the product-box histogram
therefore depends only on \((S_1,S_2,S_3)\).  Section 5 applies without any
change.

This conclusion is deliberately limited to the architecture that fully
merges to three SCD factors and then pays the resulting three-boxes
separately.  Retaining four or more factors and covering a fused
higher-dimensional box is a different problem and is not ruled out.

---

## 7. Exact averaged \(d\)-box gate

For fixed \(d\) and fixed positive proportions \(s_i=\alpha_i k+O(1)\),
the number of product boxes is

\[
\mathcal B_{d,k}=\prod_{i=1}^dW(s_i).
\]

The product-SCD width identity gives

\[
\sum_{\rm boxes}w_d=W(k).
\]

The exact sum of local excesses is

\[
\mathcal B_{d,k}\mathbb E E_d(L_1,\ldots,L_d).
\]

Translated origins and the all-zero abstract boxes contribute only
\(O(\mathcal B_{d,k})\).  Central-binomial asymptotics yield

\[
\frac{\mathcal B_{d,k}}{W(k)}
\sim
\frac{(2/\pi)^{(d-1)/2}}
{\sqrt{\alpha_1\cdots\alpha_d}\,k^{(d-1)/2}}.
\]

Since \(\mathcal B_{d,k}=o(W(k))\), the origin term is negligible.  Thus
the separate fused-\(d\)-box architecture has leading constant one if and
only if

\[
\boxed{
\mathbb E E_d(L_1,\ldots,L_d)=o(k^{(d-1)/2}).
}
\]

The exponent and constant in the source's formula (38) are both correct.
For \(d=3\), the compact dominant cone disproves the gate.  Therefore the
first fixed-dimensional candidate not eliminated by this argument is
\(d=4\), with averaged target \(o(k^{3/2})\).

---

## 8. APF is sufficient only

The logical direction in the source is correct:

\[
\mathrm{APF}\Longrightarrow
E_4(\boldsymbol\ell)=o(R^3)
\Longrightarrow \mathrm{GF4}
\Longrightarrow W(k)+o(W(k))
\]

for the four-block product architecture.

An exact outer-hook drain has \(O(R)\) three-box children and preserves the
width sum.  Pairing consecutive children and spending

\[
w_3(C_{2j})+w_3(C_{2j+1})+o(R^2)
\]

per pair gives total error

\[
O(R)\,o(R^2)=o(R^3),
\]

provided the little-oh is uniform on the stated compact parent aspect
sets.  An unpaired terminal child costs only \(O(R^2)=o(R^3)\), and the
\(O(R)\) inter-packet anchors are also negligible.  Standard fixed-moment
Rayleigh tail bounds plus the polynomial face/slice upper bound dispose of
parent boxes outside a chosen compact aspect set.

Nothing in the proof derives APF from GF4 or from the existence of an
arbitrary fused four-box word.  A direct four-box construction, a packet
using more than two children, or global nonadjacent sharing could satisfy
GF4 while violating APF.  The source states this explicitly.  Therefore
APF is one concrete sufficient implementation theorem, not a necessary
form of the remaining product-route gate.

---

## 9. Final audit conclusion

The DRAY obstruction is correctly amplified from a single ray to a
positive-mass cone and then to global width order.  The proof does not lose
control when block proportions escape to the boundary: it uses DRAY only
while the smallest block grows, interval counting for fixed positive small
blocks, and pure-axis counting for absent blocks.  The macroblock and
fixed-\(d\) statements follow from exact SCD height and width ledgers.

Accordingly, the source correctly rules out every separately paid
three-box product decomposition and correctly identifies the
Gaussian-averaged fused four-box gate as the first surviving
fixed-dimensional product route.  It does not claim that GF4 or APF has
been proved.
