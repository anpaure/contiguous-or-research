# Cross-audit of the higher-dimensional and four-box endpoint duals

Date: 2026-07-25

Audited sources:

- `MATH_ATTACK_A3_ENDPOINT_DUAL_HIGHER_DIM_20260724.md`;
- `MATH_ATTACK_G3_FOURBOX_ENDPOINT_DUAL_20260724.md`.

## 0. Verdict

\[
\boxed{\textbf{PASS}}
\]

The dimension-free plateau inequality, the exact shoulder theorem, its
four-dimensional specialization, the fixed-ray asymptotics, and the
four-block SCD aggregation are correct.  In particular, the constant

\[
\frac{49}{512}
\]

on the boundary ray \((1,1,1,3)\) is correct.

The two reports use different but exactly equivalent forms of the
four-box shoulder correction.  No mathematical source patch was needed.
The only important scope boundary is already stated correctly in both
reports: the lower bound kills independently paid local boxes and every
local parent theorem which would imply width plus \(o(R^3)\), but it does
not lower-bound an arbitrary global Boolean word which shares letters and
endpoints across different product parents.

## 1. Dimension-free flat plateau

Let

\[
Q_0=\prod_{i=1}^{d-1}[0,p_i],\qquad
B=|Q_0|,\qquad P=\sum_{i<d}p_i,\qquad r\ge P,
\]

and put \(H=r-P\).  For every \(0\le j\le H\), the displayed plateau
layer

\[
\Lambda_j=
\{(x,P+j-|x|):x\in Q_0\}
\]

is valid and has exactly \(B\) points.  Projection to \(Q_0\) is
injective on every antichain, while \(\Lambda_j\) itself is an antichain.
Thus

\[
w_d(p_1,\ldots,p_{d-1},r)=B.
\]

For one endpoint partition with \(C=B+\delta\) nonempty classes, the
occupied-class sets in two consecutive plateau layers intersect in at
least \(B-\delta\) classes.  Since the layers have adjacent total ranks,
every such common class supplies a genuine target-poset cover.  The
transverse potential

\[
\phi(x)=x_1+\cdots+x_{d-1}
\]

has the same multiset on the two plateau boundaries.  There are exactly
\(\delta\) internal starts and \(\delta\) internal ends, so telescoping
gives transverse-cover capacity at most \(P\delta\).  Therefore this
partition uses at least

\[
[H(B-\delta)-P\delta]_+=[BH-r\delta]_+
\]

last-coordinate covers.

The left and right endpoint partitions cannot share one such cover: its
two target endpoints would be two common elements of one left class and
one right class.  Since the slab has exactly \(BH\) vertical covers,

\[
[BH-r\delta_L]_++[BH-r\delta_R]_+\le BH.
\]

For \(a=BH/r\) and nonnegative \(u,v\),

\[
(a-u)_++(a-v)_+\le a
\quad\Longleftrightarrow\quad
u+v\ge a.
\]

This proves the exact endpoint-partition form

\[
r(\delta_L+\delta_R)\ge B(r-P).
\]

If the physical word has length \(B+D\), then
\(\delta_L,\delta_R\le D\), and hence

\[
g_d\ge B+
\left\lceil\frac{B(r-P)}{2r}\right\rceil.
\]

No saturation, preferred witness, physical adjacency, or prescribed
traversal is used.  The scarce objects are target-poset cover edges.

## 2. Exact shoulder theorem

For the band of total ranks \(P-k,\ldots,r+k\), put

\[
J=r-P+2k,
\quad
F_k=\sum_{s<k}a_s,
\quad
E_k=\sum_{j=1}^kF_j,
\quad
M_k=\sum_{s<k}s a_s.
\]

The source ledger checks exactly:

\[
B_0=B-F_k,
\qquad
T=(J+1)B-2E_k,
\qquad
A_v=T-B=JB-2E_k.
\]

The boundary-potential difference has the stated sign:

\[
\Delta_\phi=PF_k-2M_k.
\]

Indeed, the lower boundary omits the high-rank complements of the
low-rank corner, of potential mass \(PF_k-M_k\), while the upper boundary
omits the low corner, of mass \(M_k\).

For one endpoint partition with \(C\) classes, adjacent occupied-class
intersections force at least

\[
2T-2B_0-JC
\]

band covers.  The transverse contribution is at most

\[
\Delta_\phi+P(C-B_0).
\]

Thus the vertical-cover lower bound is

\[
2T-2B_0-\Delta_\phi+PB_0-(J+P)C.
\]

Adding the two orthogonal endpoint partitions and using the exact vertical
capacity \(A_v\) gives the source inequality.  The substitution

\[
C_L+C_R\le 2(B+D)
\]

has the correct direction because its coefficient is \(-(J+P)\).  Direct
collection of terms yields

\[
\boxed{
2(r+2k)D\ge
JB+4F_k-6E_k+4M_k-4PF_k.}
\]

The use of possibly negative one-partition lower bounds is harmless: each
is still a valid lower bound, and their sum remains bounded by the actual
available vertical covers.

When \(k\le\min_i p_i\), no cap is active below rank \(k\), and the three
closed forms

\[
F_k=\binom{k+m-1}{m},\quad
E_k=\binom{k+m}{m+1},\quad
M_k=m\binom{k+m-1}{m+1}
\]

are correct.

## 3. Reconciliation of the two four-box formulas

Set \(m=3\), let the base sides be \(p,q,s\), let the long side be \(r\),
and put

\[
P=p+q+s,qquad B=(p+1)(q+1)(s+1).
\]

The higher-dimensional report gives the correction

\[
4\binom{k+2}{3}-6\binom{k+3}{4}
+12\binom{k+2}{4}-4P\binom{k+2}{3}.
\]

The four-box report gives

\[
6\binom{k+2}{4}-(4P+2)\binom{k+2}{3}.
\]

They are identical, since

\[
\binom{k+3}{4}
=\binom{k+2}{4}+\binom{k+2}{3}.
\]

Thus both sources prove the same finite theorem:

\[
\boxed{
\begin{aligned}
2(r+2k)D\ge{}&(r-P+2k)B\\
&+6\binom{k+2}{4}
-(4P+2)\binom{k+2}{3}.
\end{aligned}}
\]

The positive part and ceiling in the exact integer lower bound are also
necessary and correctly retained.

## 4. Fixed-ray constants

On

\[
(p_1,\ldots,p_m,r)
=(a_1t,\ldots,a_mt,ct)+O(1),
\]

with \(c\ge S=\sum_i a_i\), \(V=\prod_i a_i\), and
\(k=xt+O(1)\), the exact shoulder formula gives

\[
\Gamma_{m,\boldsymbol a,c}(x)=
\frac{
V(c-S+2x)-\frac{4S}{m!}x^m
+\frac{4m-6}{(m+1)!}x^{m+1}
}{2(c+2x)}.
\]

All powers and constants follow from

\[
F_k\sim\frac{x^m}{m!}t^m,qquad
E_k\sim\frac{x^{m+1}}{(m+1)!}t^{m+1},qquad
M_k\sim\frac{m x^{m+1}}{(m+1)!}t^{m+1}.
\]

For \(c>S\), \(x=0\) gives a positive flat contribution.  For \(c=S\)
and \(m\ge2\), the numerator is \(2Vx+O(x^m)\), so it is positive for
all sufficiently small fixed \(x>0\).  Hence the claimed positive
width-scale excess on every fixed ray of the closed dominance cone is
valid.

For four boxes,

\[
\Gamma_4(x)=
\frac{
abc(\rho-a-b-c+2x)
-\frac{2(a+b+c)}3x^3+\frac14x^4
}{2(\rho+2x)}.
\]

At \((a,b,c,\rho)=(1,1,1,3)\) and \(x=1/2\), its numerator is

\[
1-\frac14+\frac1{64}=\frac{49}{64},
\]

and its denominator is

\[
2(3+1)=8.
\]

Therefore

\[
\boxed{
\liminf_{t\to\infty}
\frac{g_4(t,t,t,3t)-(t+1)^3}{t^3}
\ge\frac{49}{512}.}
\]

Likewise \((1,1,1,4)\), \(x=0\), gives \(1/8\).

## 5. Independent literal-witness specialization

The additional ordered-witness corroboration in the four-box report is
also internally valid.  At the full middle layer

\[
h=\left\lfloor\frac{P+s}{2}\right\rfloor,
\]

the exact number of nonzero lower targets is

\[
L_{<h}=V\frac{s-\epsilon}{2}-1.
\]

The endpoint-order representation

\[
\ell_i=i+\alpha_i,\qquad r_i=i+\beta_i
\]

and the start-capacity inequality are unchanged from the audited
three-box proof.  The four-coordinate valley argument gives a run in every
\(P+2\) consecutive middle targets.  Plateau extraction followed, when
needed, by the three-coordinate valley argument in a fixed-coordinate
slice gives edge length at most \(q+r\) for \(p\le q\le r\).  The displayed
sharpness order is valid in the middle layer and has exactly one internal
positive run, the \(x=p\) plateau of edge length \(q+r\).

The one-pin gap and paired-block congestion therefore yield

\[
\sum_i(r_i-\ell_i)\le(q+r)V+2BD,
\]

and the fixed-ray constant

\[
\frac{abc(d-2b-2c)}{d+5a+5b+5c}
\]

has the correct factor of two after dividing numerator and denominator.
This corroboration is not needed for the endpoint-dual theorem.

## 6. Four-block SCD aggregation

### 6.1 Height law

For a block of size \(n\), the number of SCD chains of edge height
\(\ell\equiv n\pmod2\) is

\[
a_n(\ell)=
\binom n{(n-\ell)/2}
-\binom n{(n-\ell)/2-1}.
\]

For \(\ell=x\sqrt n+O(1)\), division by the total chain count \(W(n)\)
gives a lattice distribution with limiting Rayleigh density

\[
f(x)=xe^{-x^2/2},\qquad x>0.
\]

In the equal four-block normalization \(N=4n\), \(R=\sqrt N=2\sqrt n\),
this implies

\[
\Pr(uR\le L\le vR)
\longrightarrow e^{-2u^2}-e^{-2v^2}.
\]

The constants in the two reports are therefore consistent; they merely
use \(L/\sqrt n\) and \(L/R\), respectively.

### 6.2 Positive-mass strict-dominance sector

For equal blocks, the windows

\[
L_1,L_2,L_3\in[0.1R,0.2R],qquad
L_4\in[0.7R,0.8R]
\]

have fixed positive limiting probability.  Throughout this event,

\[
L_4-(L_1+L_2+L_3)\ge0.1R,
\qquad
(L_1+1)(L_2+1)(L_3+1)\ge0.001R^3.
\]

The flat bound consequently gives local excess at least

\[
(1-o(1))\frac{R^3}{16000}.
\]

The number of four-chain product boxes is \(W(n)^4\), and

\[
W(n)^4R^3=\Theta(W(N)).
\]

Moreover, the product-chain boxes partition the Boolean lattice, and the
central section of each product box is its width layer.  Therefore

\[
\sum_{\mathcal B}w_4(\mathcal B)=W(N).
\]

It follows that any construction which pays one universal local word per
box has length at least

\[
(1+\kappa)W(N)
\]

for some fixed \(\kappa>0\).  The translated-origin anchors are not the
source of this loss.  The only local boxes for which \(g_4<w_4\) are the
all-zero boxes, and their total number is \(o(W(N))\).

For arbitrary positive-proportion four-block splits, the same conclusion
follows by selecting compact Rayleigh windows on which one height strictly
dominates the other three.  Equivalently,

\[
\mathbb E\bigl[g_4(L_1,L_2,L_3,L_4)-w_4(L_1,L_2,L_3,L_4)\bigr]
=\Omega(N^{3/2}).
\]

This correctly refutes GF4 and every independently paid fixed-four-box
aggregation theorem with the stated quantifiers.

## 7. Scope and cross-parent sharing

The local endpoint theorem allows witnesses to use the entire local word
and to cross every proposed child seam.  Hence any APF or DPDA statement
whose already-proved implication is a uniform parent estimate

\[
g_4(\boldsymbol\ell)=w_4(\boldsymbol\ell)+o(R^3)
\]

is false as stated.  This is stronger than the earlier three-box DRAY
no-go.

It is not a global Boolean lower bound.  Projection of one global Boolean
word onto a fixed product-chain box, followed by deletion of zero
projections, does produce a valid local range-maximum word.  Consequently,
if \(d_j\) is the number of boxes in which global letter \(j\) has nonzero
projection, then

\[
\sum_jd_j\ge\sum_{\mathcal B}g_4(\mathcal B).
\]

Thus a hypothetical global word of length \(W(N)+o(W(N))\) must have

\[
\sum_j(d_j-1)_+=\Omega(W(N)).
\]

The analogous endpoint-incidence ledger is also valid, because the flat
endpoint proof groups witnesses by their actual physical endpoints and
does not require their intervals to remain inside a local-box block.

These ledgers prove that sparse bounded-degree portals cannot repair the
local loss.  They leave open positions of unbounded box degree, genuinely
global corridors, abandonment of the fixed product partition, and other
cross-parent fusion mechanisms.  Both sources state this boundary
correctly.

## 8. Final audit ledger

| Claim | Verdict |
|---|---|
| Dimension-free plateau width and endpoint capacity | PASS |
| Exact shoulder population and potential ledgers | PASS |
| Chain-count substitution direction | PASS |
| Cap-free binomial specialization | PASS |
| Equivalence of the two four-box formulas | PASS |
| Fixed-ray asymptotics | PASS |
| Boundary constant \(49/512\) | PASS |
| Long-ray literal corroboration | PASS |
| Rayleigh SCD height law | PASS |
| Exact product-width aggregation | PASS |
| GF4 / independently paid four-box no-go | PASS |
| Local/global scope qualification | PASS |

No source patch was made.
