# Third-wave A: the endpoint dual in higher-dimensional products

Date: 2026-07-24

## 0. Verdict

For integers \(p_1,\ldots,p_d\ge 0\), let

\[
 \mathcal Q(\boldsymbol p)=\prod_{i=1}^d[0,p_i]
\]

with the coordinatewise order, and let \(g_d(\boldsymbol p)\) be the least
length of a word of nonzero points of \(\mathcal Q(\boldsymbol p)\) whose
nonempty contiguous coordinatewise maxima contain every nonzero point of
the box.  Write \(w_d(\boldsymbol p)\) for the width of the box.

The two-endpoint potential dual is dimension-free.  Put

\[
 B=\prod_{i=1}^{d-1}(p_i+1),\qquad
 0<P=\sum_{i=1}^{d-1}p_i\le p_d=r,\qquad H=r-P.
\]

Then \(w_d=B\), and every universal word satisfies

\[
 \boxed{
 g_d(p_1,\ldots,p_{d-1},r)
 \ge B+
 \left\lceil\frac{B(r-P)}{2r}\right\rceil .}
 \tag{0.1}
\]

The stronger endpoint-partition form is an exact necessary inequality.  If
witnesses are selected for all targets in the full plateau and \(C_L,C_R\)
are the actual numbers
of nonempty left- and right-endpoint classes, then

\[
 \boxed{
 r\bigl((C_L-B)+(C_R-B)\bigr)\ge B(r-P).}
 \tag{0.2}
\]

Equivalently, if \(\delta_\sigma=C_\sigma-B\), then the two endpoint
partitions obey the exact vertical-capacity inequality

\[
 \boxed{
 [BH-r\delta_L]_+ +[BH-r\delta_R]_+\le BH.}
 \tag{0.3}
\]

There is no asymptotic, fractional, saturation, or prescribed-order
assumption in (0.1)--(0.3).

The flat inequality is silent at \(r=P\).  An exact sloped-shoulder
extension proved below shows that this silence is not genuine feasibility.
For every fixed ray in dimension \(d\ge3\) on the closed dominance cone

\[
 p_d\ge p_1+\cdots+p_{d-1},
\]

the local excess is a positive proportion of the width scale.  In
particular,

\[
 \liminf_{t\to\infty}
 \frac{g_4(t,t,t,3t)-(t+1)^3}{t^3}
 \ge \frac{49}{512}.
 \tag{0.4}
\]

Thus the proposed uniform compact four-box coefficient-one theorem, CB4,
the thick four-box lemma, GF4, and the uniform all-parent conclusions of
DPDA and APF are false as stated.  This does **not** disprove the global
contiguous-OR width conjecture: the obstruction is for a standalone local
box, or for an architecture which pays such boxes independently.

No unproved lemma is used in the new endpoint bounds.  The DPDA/APF
no-gos use the previously proved implications from those statements to a
uniform local four-box estimate.

## 1. The two endpoint partitions

The common combinatorial input is independent of dimension.

### Lemma 1.1 (orthogonal endpoint partitions)

Let \(v_1,\ldots,v_n\) be a word in a product of chains.  Let
\(\mathcal T\) be any represented target family, and select one witnessing
interval

\[
 I_T=[\ell_T,r_T]
\]

for every \(T\in\mathcal T\).  Group the targets first by common left
endpoint and then by common right endpoint.  The resulting partitions
\(\mathcal L,\mathcal R\) have the following properties.

1. Every class in either partition is a poset chain.
2. Each partition has at most \(n\) nonempty classes.
3. A class of \(\mathcal L\) and a class of \(\mathcal R\) intersect in at
   most one target.

#### Proof

For a fixed left endpoint, increasing the right endpoint enlarges the
interval, so its coordinatewise maximum can only increase.  This gives a
chain.  The same argument, extending intervals to the left while fixing
the right endpoint, gives the other chain partition.  There are at most
\(n\) possible physical endpoints.

If one left class and one right class shared two distinct targets, both
targets would have the same selected interval \([\ell,r]\).  That physical
interval has one coordinatewise maximum, so the targets would be equal, a
contradiction.  This proves orthogonality. \(\square\)

## 2. Exact capacity on a flat plateau

We now prove (0.1)--(0.3).

### Theorem 2.1 (exact endpoint-partition plateau capacity)

Assume

\[
 r\ge P:=\sum_{i=1}^{d-1}p_i>0,\qquad
 B:=\prod_{i=1}^{d-1}(p_i+1),\qquad H=r-P.
\]

For \(0\le j\le H\), let

\[
 \Lambda_j=
 \left\{
 (x_1,\ldots,x_{d-1},P+j-x_1-\cdots-x_{d-1}):
 0\le x_i\le p_i
 \right\}.
 \tag{2.1}
\]

Select arbitrary witnesses for every target in
\(\bigcup_{j=0}^H\Lambda_j\), and let \(C_L,C_R\) be the actual class
counts in Lemma 1.1.  Put

\[
 \delta_L=C_L-B,\qquad \delta_R=C_R-B.
\]

Then \(\delta_L,\delta_R\ge0\), and (0.2)--(0.3) hold.

#### Proof

Every \(\Lambda_j\) is a rank layer and has exactly one point above each
base point \((x_1,\ldots,x_{d-1})\).  Hence it is an antichain of size
\(B\).  Each endpoint partition therefore has at least \(B\) classes.

Consider either endpoint partition and write its class count as
\(C=B+\delta\).  Let \(A_j\) be the set of its classes meeting
\(\Lambda_j\).  A chain meets an antichain at most once, so

\[
 |A_j|=B,
 \qquad
 |A_j\cap A_{j+1}|\ge 2B-C=B-\delta.
 \tag{2.2}
\]

Two comparable points in adjacent total ranks form a genuine cover.
Summing (2.2) over the \(H\) transitions, this partition uses at least

\[
 H(B-\delta)
 \tag{2.3}
\]

cover edges between adjacent plateau layers.

Use the transverse potential

\[
 \phi(x_1,\ldots,x_d)=x_1+\cdots+x_{d-1},
 \qquad 0\le\phi\le P.
 \tag{2.4}
\]

The bottom and top boundary layers have the same \(\phi\)-multiset: both
contain one copy of \(\sum_{i<d}x_i\) for every base point.  Exactly
\(C-B=\delta\) endpoint chains start internally, and exactly \(\delta\)
end internally.  Telescoping \(\phi\) along all chains therefore gives

\[
 \sum_{K}\bigl(\phi(\max K)-\phi(\min K)\bigr)
 \le P\delta.
 \tag{2.5}
\]

A cover in one of the first \(d-1\) coordinates raises \(\phi\) by one;
a cover in the last coordinate leaves it fixed.  Skipped comparisons in a
chain consume nonnegative potential and only make (2.5) more generous.
Thus at most \(P\delta\) of the covers counted in (2.3) are transverse,
and the number of last-coordinate covers used by this partition is at
least

\[
 [H(B-\delta)-P\delta]_+
 =[BH-r\delta]_+.
 \tag{2.6}
\]

The plateau slab contains exactly \(BH\) last-coordinate covers.  Such a
cover cannot occur in both endpoint partitions: otherwise its two target
endpoints would lie together in one left class and one right class,
contradicting Lemma 1.1.  Adding (2.6) for the two partitions proves (0.3).

For completeness, put \(a=BH/r\).  For nonnegative \(u,v\),

\[
 (a-u)_++(a-v)_+\le a
 \quad\Longleftrightarrow\quad
 u+v\ge a.
 \tag{2.7}
\]

Indeed, if both \(u,v<a\), this is direct algebra; if one is at least
\(a\), both statements are automatic.  Dividing (0.3) by \(r\) and using
(2.7) proves (0.2). \(\square\)

### Corollary 2.2 (word length and width)

Under the hypotheses of Theorem 2.1,

\[
 w_d(p_1,\ldots,p_{d-1},r)=B
\]

and (0.1) holds.

#### Proof

Projection onto the first \(d-1\) coordinates is injective on every
antichain, because two points in the same last-coordinate column are
comparable.  Thus every antichain has size at most \(B\), while any
\(\Lambda_j\) has size \(B\).  Hence the width is \(B\).

If a word has length \(n=B+D\), Lemma 1.1 gives

\[
 C_L,C_R\le n,
 \qquad
 \delta_L,\delta_R\le D.
\]

Equation (0.2) now gives

\[
 B(r-P)\le r(\delta_L+\delta_R)\le2rD.
\]

Since \(D\) is integral, this is exactly (0.1). \(\square\)

The proof did not use the exclusion of the zero point as a possible word
letter; it used only that the selected plateau targets are nonzero, which
is ensured by \(P>0\).  Hence (0.1)--(0.3) remain valid for translated
local boxes whose abstract origin is also allowed as a physical letter.

The case \(H=0\) is correctly degenerate: the flat capacity says only
\(g_d\ge B\).  The next section recovers the missing boundary information.

## 3. Exact sloped-shoulder extension

The following finite theorem contains the flat result at \(k=0\) and is
strictly stronger near the plateau boundary.

### Theorem 3.1 (exact symmetric shoulder inequality)

Let

\[
 Q_0=\prod_{i=1}^{m}[0,p_i],
 \qquad m=d-1,
 \qquad B=|Q_0|=\prod_{i=1}^{m}(p_i+1),
 \qquad P=\sum_{i=1}^{m}p_i>0,
\]

and let \(a_s\) be the number of base points of rank \(s\).  Thus

\[
 a_s=a_{P-s}
 \tag{3.1}
\]

by coordinate complementation.  Assume \(r\ge P\), and choose an integer
\(0\le k<P\).  Define

\[
 F_k=\sum_{s=0}^{k-1}a_s,
 \qquad
 E_k=\sum_{j=1}^k F_j,
 \qquad
 M_k=\sum_{s=0}^{k-1}s\,a_s,
 \qquad
 J=r-P+2k.
 \tag{3.2}
\]

If a universal word for \(Q_0\times[0,r]\) has length \(B+D\), then

\[
 \boxed{
 2(r+2k)D\ge
 J B+4F_k-6E_k+4M_k-4PF_k.}
 \tag{3.3}
\]

Consequently,

\[
 D\ge
 \max\left\{0,
 \left\lceil
 \frac{J B+4F_k-6E_k+4M_k-4PF_k}{2(r+2k)}
 \right\rceil\right\}.
 \tag{3.4}
\]

#### Proof

Use all targets whose total ranks lie from \(P-k\) through \(r+k\).
There are \(J+1\) layers.  At distance \(j\) down the lower shoulder, or
distance \(j\) up the upper shoulder, the layer omits exactly \(F_j\)
base points.  This uses (3.1).  Hence either boundary layer has size

\[
 B_0=B-F_k,
 \tag{3.5}
\]

and the exact number of band targets is

\[
 T=(J+1)B-2E_k.
 \tag{3.6}
\]

Every one of the \(B\) last-coordinate columns meets the band in a
nonempty contiguous interval.  Its number of vertical covers is one less
than its number of band targets.  Therefore the total last-coordinate
cover capacity in the band is

\[
 A_v=T-B=JB-2E_k.
 \tag{3.7}
\]

The lower boundary omits the base points of ranks \(P-s\), \(0\le s<k\),
whose total potential is \(PF_k-M_k\).  The upper boundary omits the base
points of ranks \(s\), \(0\le s<k\), whose total potential is \(M_k\).
For the potential \(\phi=\operatorname{rank}_{Q_0}\), the upper-minus-lower
boundary difference is therefore

\[
 \Delta_\phi=PF_k-2M_k.
 \tag{3.8}
\]

Consider one endpoint partition with \(C\) nonempty classes.  If adjacent
band layers have sizes \(b_i,b_{i+1}\), their occupied class sets intersect
in at least \(b_i+b_{i+1}-C\).  A negative lower bound remains valid.
Summing over all \(J\) transitions forces at least

\[
 \sum_{i=0}^{J-1}(b_i+b_{i+1}-C)
 =2T-2B_0-JC
 \tag{3.9}
\]

cover edges in this partition.

Exactly \(B_0\) classes start on the lower boundary and \(B_0\) end on the
upper boundary.  The other \(C-B_0\) starts and ends are internal.  As in
(2.5), telescoping the transverse potential shows that the number of
transverse covers counted in (3.9) is at most

\[
 \Delta_\phi+P(C-B_0).
 \tag{3.10}
\]

Thus this partition uses at least

\[
 2T-2B_0-\Delta_\phi+PB_0-(J+P)C
 \tag{3.11}
\]

last-coordinate covers.  This lower bound may be negative, which is
harmless.

Apply (3.11) to the two orthogonal endpoint partitions.  They cannot share
a last-coordinate cover, so

\[
 2(2T-2B_0-\Delta_\phi+PB_0)
 -(J+P)(C_L+C_R)
 \le A_v.
 \tag{3.12}
\]

Both class counts are at most the word length \(B+D\).  Since the
coefficient of their sum in (3.12) is negative, substituting
\(C_L+C_R\le2(B+D)\) in the correct direction gives

\[
 2(2T-2B_0-\Delta_\phi+PB_0)
 -2(J+P)(B+D)
 \le A_v.
 \tag{3.13}
\]

Insert (3.5)--(3.8), use \(J+P=r+2k\), and collect terms.  The right-hand
side after solving for \(D\) is

\[
 JB+4F_k-6E_k+4M_k-4PF_k,
\]

which proves (3.3).  Integrality and \(D\ge0\) give (3.4). \(\square\)

### Corollary 3.2 (cap-free product formula)

If additionally

\[
 0\le k\le p_{\min}:=\min_i p_i,
\]

then, with \(m=d-1\),

\[
 F_k=\binom{k+m-1}{m},\qquad
 E_k=\binom{k+m}{m+1},\qquad
 M_k=m\binom{k+m-1}{m+1}.
 \tag{3.14}
\]

Thus the exact numerator in (3.3) is

\[
 \boxed{
 \begin{aligned}
 N_k={}&(r-P+2k)B+4\binom{k+m-1}{m}
-6\binom{k+m}{m+1}\\
&+4m\binom{k+m-1}{m+1}
-4P\binom{k+m-1}{m}.
 \end{aligned}}
 \tag{3.15}
\]

#### Proof

Below rank \(k\), no coordinate cap is active, so

\[
 a_s=\binom{s+m-1}{m-1}\qquad(0\le s<k).
\]

The first two identities in (3.14) are the hockey-stick identity.  The
third follows from

\[
 s\binom{s+m-1}{m-1}=m\binom{s+m-1}{m}
\]

and one more hockey-stick summation. \(\square\)

For \(m=2\), formula (3.15) reduces exactly to

\[
 (r-P+2k)B+\frac{k(k+1)(k-6P-4)}3,
\]

the audited three-dimensional sloped-band numerator.

## 4. Fixed-ray consequence on the closed dominance cone

The shoulder correction is of leading order at the boundary in every
dimension \(d\ge3\).

### Theorem 4.1 (positive relative excess on every closed plateau ray)

Let \(m=d-1\ge2\), and let

\[
 p_i=a_i t+O(1),\qquad r=ct+O(1),
\]

where all \(a_i>0\), \(c\ge S:=\sum_i a_i\), and \(r\ge P=\sum_i p_i\)
for all sufficiently large \(t\).  Put

\[
 B=\prod_i(p_i+1),\qquad V=\prod_i a_i.
\]

For every fixed \(x\) with \(0\le x<\min_i a_i\), choose
\(k=xt+O(1)\).  Then

\[
 \boxed{
 \liminf_{t\to\infty}
 \frac{g_d(p_1,\ldots,p_m,r)-B}{t^m}
 \ge \max\{0,\Gamma_{m,\boldsymbol a,c}(x)\},}
 \tag{4.1}
\]

where

\[
 \boxed{
 \Gamma_{m,\boldsymbol a,c}(x)=
 \frac{
 V(c-S+2x)-\dfrac{4S}{m!}x^m
 +\dfrac{4m-6}{(m+1)!}x^{m+1}
 }{2(c+2x)}.}
 \tag{4.2}
\]

In particular, the right side is positive for some admissible \(x\) on
every ray with \(c\ge S\).

#### Proof

For \(k=xt+O(1)\), (3.14) gives

\[
\begin{aligned}
 B&=Vt^m+O(t^{m-1}),\\
 F_k&=\frac{x^m}{m!}t^m+O(t^{m-1}),\\
 E_k&=\frac{x^{m+1}}{(m+1)!}t^{m+1}+O(t^m),\\
 M_k&=\frac{m x^{m+1}}{(m+1)!}t^{m+1}+O(t^m).
\end{aligned}
 \tag{4.3}
\]

Also \(P=St+O(1)\) and
\(J=(c-S+2x)t+O(1)\).  Divide (3.3) by \(t^{m+1}\).  The term \(4F_k\)
is one order lower, while the remaining terms give the numerator in
(4.2); the denominator tends to \(2(c+2x)\).  This proves (4.1).

If \(c>S\), take \(x=0\).  Then

\[
 \Gamma(0)=\frac{V(c-S)}{2c}>0.
 \tag{4.4}
\]

If \(c=S\), the numerator becomes

\[
 \Psi_m(x)=
 2Vx-\frac{4S}{m!}x^m
 +\frac{4m-6}{(m+1)!}x^{m+1}.
 \tag{4.5}
\]

Because \(m\ge2\), this is \(2Vx+O(x^m)>0\) for all sufficiently small
fixed \(x>0\).  An explicit safe choice is any

\[
 0<x\le\frac12\min\left\{
 \min_i a_i,
 \left(\frac{Vm!}{4S}\right)^{1/(m-1)}
 \right\}.
 \tag{4.6}
\]

Indeed, the negative term in (4.5) is then at most \(Vx\), while the final
term is nonnegative.  Hence \(\Psi_m(x)\ge Vx>0\). \(\square\)

Since \(B\sim Vt^m\), Theorem 4.1 says equivalently that

\[
 g_d-w_d=\Omega(B)
\]

on every fixed ray in the closed dominance cone, for every \(d\ge3\).

## 5. The four-box formulas and explicit witnesses against coefficient one

Let the three base sides be \(p,q,s\), let the long side be \(r\), and put

\[
 P=p+q+s,\qquad B=(p+1)(q+1)(s+1).
\]

For \(0\le k\le\min(p,q,s)\), (3.3) becomes

\[
\boxed{
\begin{aligned}
2(r+2k)D\ge{}&(r-P+2k)B
+4\binom{k+2}{3}-6\binom{k+3}{4}\\
&+12\binom{k+2}{4}-4P\binom{k+2}{3}.
\end{aligned}}
\tag{5.1}
\]

On a fixed ray

\[
 (p,q,s,r)=(at,bt,ct,\rho t)+O(1),
 \qquad \rho\ge a+b+c,
\]

formula (4.2) is

\[
 \Gamma_4(x)=
 \frac{
 abc(\rho-a-b-c+2x)
 -\dfrac{2(a+b+c)}3x^3+\dfrac14x^4
 }{2(\rho+2x)}.
 \tag{5.2}
\]

Two useful exact-ray consequences are:

\[
 \liminf_{t\to\infty}
 \frac{g_4(t,t,t,4t)-(t+1)^3}{t^3}
 \ge\frac18,
 \tag{5.3}
\]

from the flat theorem, and

\[
 \liminf_{t\to\infty}
 \frac{g_4(t,t,t,3t)-(t+1)^3}{t^3}
 \ge\frac{49}{512},
 \tag{5.4}
\]

from (5.2) with \(x=1/2\).  Indeed, the numerator in (5.2) is then

\[
 1-\frac14+\frac1{64}=\frac{49}{64},
\]

and the denominator is \(8\).

These are lower bounds for unrestricted words inside the whole four-box.
They do not assume a drain, slicing order, reset, raster, or child
decomposition.

## 6. Exact no-go consequences for four-box routes

### 6.1 Uniform local coefficient one is false

There is no estimate

\[
 g_4(\boldsymbol\ell)
 =w_4(\boldsymbol\ell)+o(R^3)
 \tag{6.1}
\]

uniform over all fixed compact positive aspect-ratio sectors.  A single
boundary ray \((R,R,R,3R)\) contradicts it.  More quantitatively, for a
sector

\[
 \delta R\le\ell_i\le CR,
\]

the flat theorem contradicts uniform coefficient one whenever
\(C>3\delta\), and (5.4) also covers \(C=3\delta\) after scaling.

In particular:

* **CB4 is false.**  Its quantifier includes, for example, the compact
  sector \(R\le\ell_i\le3R\).
* The compact four-box theorem recorded in the first-wave synthesis and
  the all-height uniform theorem in the general route decision are false
  with their present quantifiers.
* The **thick four-box lemma** is false.  On \((R,R,R,3R)\), its two
  shortest sides satisfy
  \((R+1)^2>(6R+1)^{2-\varepsilon}\) for every fixed
  \(\varepsilon>0\) and all large \(R\), but its asserted error
  \(O(R^{3-\varepsilon})\) contradicts (5.4).
* Any stated **DPDA** or **APF** which, by its proved concatenation
  implication, yields (6.1) uniformly for every parent is false.  The
  present theorem supplies a parent-level contradiction even though its
  witnesses are allowed to cross all proposed child seams.

This is a no-go for the full compact or all-parent quantifier.  It does not
contradict a theorem restricted to a compact subset of

\[
 \max_i\ell_i<\sum_{j\ne i}\ell_j
\]

with a fixed interior margin, and it does not touch the equal cube.

### 6.2 The Gaussian-averaged four-box gate GF4 is false

The fixed-ray obstruction is not confined to a probability-zero set of
chain heights.  Consider a partition of the Boolean coordinates into four
positive-proportion blocks of sizes

\[
 s_i=\alpha_i k+O(1),\qquad \alpha_i>0,\qquad
 \sum_{i=1}^4s_i=k,\qquad \sum_{i=1}^4\alpha_i=1.
\]

Choose one chain uniformly from an SCD in each block, independently, and
let \(L_i\) be its edge height.  The SCD height multiset is invariant, and
on the appropriate parity lattice

\[
 \Pr(L_i=\ell)=
 \frac{
 \binom{s_i}{(s_i-\ell)/2}
 -\binom{s_i}{(s_i-\ell)/2-1}
 }{\binom{s_i}{\lfloor s_i/2\rfloor}}.
 \tag{6.2}
\]

To justify (6.2), a symmetric chain with bottom rank \(j\) has edge height
\(s_i-2j\).  At rank \(j\le\lfloor s_i/2\rfloor\), the difference between
the numbers of chains already present at ranks \(j\) and \(j-1\) is

\[
 \binom{s_i}{j}-\binom{s_i}{j-1},
\]

so this is exactly the number of chains with bottom rank \(j\).  This also
shows directly that the height multiset is independent of the chosen SCD.
For \(\ell=x\sqrt{s_i}+O(1)\), uniformly for \(x\) in a fixed compact
subset of \((0,\infty)\),

\[
 \frac{\binom{s_i}{(s_i-\ell)/2}}
 {\binom{s_i}{\lfloor s_i/2\rfloor}}
 =e^{-x^2/2}(1+o(1)),
\]

while

\[
 1-\frac{(s_i-\ell)/2}{(s_i+\ell)/2+1}
 =\frac{2x}{\sqrt{s_i}}(1+o(1)).
\]

The allowed \(x\)-values have lattice spacing \(2/\sqrt{s_i}\).  Dividing
the probability mass by that spacing gives the limiting density

\[
 f(x)=x e^{-x^2/2},\qquad x>0.
 \tag{6.3}
\]

In particular, every fixed compact positive height window has positive
limiting probability.  Choose four such windows so that throughout their
Cartesian product

\[
 L_4-L_1-L_2-L_3\ge\eta\sqrt{k}
 \tag{6.4}
\]

for some \(\eta>0\), while all four heights remain between positive
constant multiples of \(\sqrt{k}\).  This event has probability bounded
below by a positive constant.  On it, Theorem 2.1 gives

\[
\begin{aligned}
 E_4(L_1,L_2,L_3,L_4)
 &:=g_4-w_4\\
 &\ge
 \frac{(L_1+1)(L_2+1)(L_3+1)
 (L_4-L_1-L_2-L_3)}{2L_4}\\
 &\ge c_0 k^{3/2}
\end{aligned}
 \tag{6.5}
\]

for a constant \(c_0>0\).  Therefore

\[
 \boxed{
 \mathbb E E_4(L_1,L_2,L_3,L_4)=\Omega(k^{3/2}).}
 \tag{6.6}
\]

This directly refutes GF4, which asked for \(o(k^{3/2})\).

There is also an architecture-level consequence.  The exact local-width
identity for the four-block product decomposition is

\[
 \sum_{\text{four-chain boxes}}w_4=W(k),
 \tag{6.7}
\]

where \(W(k)=\binom{k}{\lfloor k/2\rfloor}\).  Indeed, if the four
chosen symmetric chains have bottom ranks with sum \(A\) and edge heights
with sum \(h\), then \(h=k-2A\); the global middle rank cuts their product
in its local middle rank.  Since the chain products partition the Boolean
lattice, their local middle layers partition the global middle layer.

The number of boxes is

\[
 \prod_{i=1}^4 W(s_i)=\Theta\!\left(\frac{W(k)}{k^{3/2}}\right)
 \tag{6.8}
\]

by the central binomial estimate.  Multiplying (6.6) by (6.8) shows that
any architecture which pays the four-chain boxes independently has total
excess \(\Omega(W(k))\), not \(o(W(k))\).  Thus fixed four-box independent
aggregation does not have coefficient one.

The same observation does not apply to a construction which shares
letters and witnesses globally across different four-chain parents; such
a construction is no longer the independently paid local-box route.

## 7. Adversarial audit

The strongest claims above were checked against the following possible
failure modes.

1. **Width versus projected column count.**  The equality \(w_d=B\) is
   used only when \(r\ge P>0\).  Positivity of \(P\) ensures that every
   selected plateau target is nonzero; without it, \(\Lambda_0\) would be
   the excluded zero target.  The width equality follows from both a full
   layer of size \(B\) and the projection upper bound.  No width formula
   outside the plateau is assumed.

2. **Unsaturated endpoint chains.**  Neither proof assumes that an
   endpoint chain meets every band layer.  Intersections of occupied class
   sets give only the covers actually forced.  Skips make the potential
   upper bound more generous, never invalid.

3. **Negative one-partition demands.**  The flat theorem retains the
   positive parts in (0.3).  In the shoulder theorem, (3.11) is allowed to
   be negative; summing two valid lower bounds still gives (3.12).

4. **Double-counting physical covers.**  A cover used by both endpoint
   partitions would place its two target endpoints in the intersection of
   one left class and one right class.  Lemma 1.1 forbids this.  The total
   capacities \(BH\) and \(A_v=T-B\) count each last-coordinate cover once.

5. **Potential boundary sign.**  Formula (3.8) follows by explicitly
   subtracting the omitted high-rank mass from the lower boundary and the
   omitted low-rank mass from the upper boundary.  This is why the term is
   \(PF_k-2M_k\), not its negative.

6. **Direction of the chain-count substitution.**  The coefficient of
   \(C_L+C_R\) in (3.12) is \(-(J+P)\).  Therefore replacing that sum by
   its upper bound \(2(B+D)\) decreases the left side and preserves the
   necessary inequality.  Reversing this direction would be invalid.

7. **Cap-free range.**  The abstract formula (3.3) uses the exact rank
   counts and is valid for every \(k<P\).  The binomial specialization
   (3.14)--(3.15) is asserted only for \(k\le\min_i p_i\), where no base
   coordinate cap is active.

8. **Boundary arithmetic.**  For \(m=3\), (4.2) gives the coefficients
   \(-2S/3\) and \(1/4\).  At \((1,1,1,3)\), \(x=1/2\) gives numerator
   \(49/64\) and denominator \(8\), hence \(49/512\).  At
   \((1,1,1,4)\), \(x=0\) gives \(1/8\).

9. **Averaging versus a single ray.**  The GF4 refutation uses an open
   compact strict-plateau event with positive limiting SCD-height mass, not
   the single equality ray of (5.4).

10. **Local versus global scope.**  A universal word inside one dominant
    box has leading excess.  This proves no lower bound for an arbitrary
    Boolean word which fuses different product parents, and it proves no
    failure of the global contiguous-OR conjecture.

## 8. Final theorem ledger

Unconditional results proved here are:

* the dimension-free exact endpoint capacity inequalities (0.2)--(0.3);
* the exact local word lower bound (0.1);
* the exact symmetric-shoulder inequality (3.3) and product formula
  (3.15);
* positive width-scale excess on every fixed closed-dominance ray in every
  dimension \(d\ge3\);
* the explicit four-box boundary constant \(49/512\); and
* the averaged lower bound (6.6), closing GF4 and independently paid
  fixed-four-box aggregation.

The exact obstruction left outside this theorem is geometric, not an
unproved step: the endpoint dual does not decide the polygon-interior
sector, including the equal four-cube, and it does not control arbitrary
cross-parent global fusion.
