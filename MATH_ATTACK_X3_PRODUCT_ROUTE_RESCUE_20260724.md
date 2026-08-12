# Third-wave lane X: product-route rescue after the plateau obstruction

Date: 2026-07-24

## 0. Outcome and theorem ledger

Throughout the asymptotic discussion \(k\ge2\).  Put

\[
 W(k)=\binom{k}{\lfloor k/2\rfloor},
\]

and let \(\nu(k)\) be the minimum length of a Boolean word whose contiguous
ORs contain every nonempty subset of \([k]\).  For a product of chains

\[
 Q(\boldsymbol\ell)=\prod_{i=1}^{d}[0,\ell_i],
\]

write \(g_d(\boldsymbol\ell)\) for the minimum length of a nonzero
contiguous-maximum word for the box, and write \(w_d(\boldsymbol\ell)\) for
its width.  For the singleton zero box the convention is

\[
 g_d(0,\ldots,0)=0,\qquad w_d(0,\ldots,0)=1.
\]

The first-wave dominant-ray route and the second-wave hierarchical-ray route
cannot be repaired by changing the aspect-ratio cone.  The audited obstruction
already gives, for fixed \(0<a<b\) and \(c>2b\),

\[
 \liminf_{r\to\infty}
 \frac{g_3(ar,br,cr)-(ar+1)(br+1)}{r^2}
 \ge
 \frac{ab(c-2b)}{c+5a+5b}>0.
\tag{0.1}
\]

This report proves a substantially broader obstruction and then gives the
surviving exact replacement reduction.

### Proved here

1. **General flat-plateau theorem.**  Let \(Q\) be any product of chains of
   size \(B\) and total height \(S>0\).  If \(L>S\), then

   \[
   \boxed{
   g(Q\times[0,L])-B
   \ge
   \left\lceil\frac{B(L-S)}{2L}\right\rceil .}
   \tag{0.2}
   \]

   The width of the box is exactly \(B\).  The proof permits arbitrary
   foreign letters and arbitrary witness intervals crossing every proposed
   seam.

2. **Fixed-atomic-count product no-go.**  Fix \(t\ge2\).  Uniformly over
   every split \(s_1+\cdots+s_t=k\), including boundary splits, and every
   choice of SCDs in the coordinate blocks, independently servicing the
   resulting \(t\)-chain product parents costs

   \[
   \boxed{(1+\epsilon_t)W(k)-o(W(k))}
   \tag{0.3}
   \]

   for a constant \(\epsilon_t>0\) depending only on \(t\).  Concretely,
   take \(K=2\) in Theorems 3.1--3.2 and write
   \(\epsilon_t:=\epsilon_{t,2}\).  This remains
   true if the construction performs arbitrary height-dependent reblocking,
   noncentered cutting, or fused processing *inside each parent*.  It rules
   out the former Gaussian-averaged four-box gate (GF4), compact four-box
   variants that imply it, the former uniform separately paid all-parent
   adjacent-child-fusion gate, and the separately paid four-box MTF gate.

3. **Exact non-product packet aggregation.**  If the chains of one Boolean
   SCD are divided into packets \(P\), and packet \(P\) has a literal word of
   length \(n(P)\), then

   \[
   \boxed{
   \nu(k)\le W(k)+\sum_P\bigl(n(P)-q(P)\bigr),}
   \tag{0.4}
   \]

   where \(q(P)\) is the number of SCD chains in the packet.  More generally,
   an MTF packet walk gives the exact global bound

   \[
   \boxed{
   \nu(k)
   \le W(k)
      +\sum_\alpha(t_\alpha-M_\alpha)
      +\sum_\alpha(b_\alpha-1).}
   \tag{0.5}
   \]

   Here \(M_\alpha\) is the number of middle-layer targets in packet
   \(\alpha\), \(t_\alpha\) is its number of visited MTF states, and
   \(b_\alpha\) is the number of blocks in its initial state.  Every term in
   (0.5) is integral and comes from a literal Boolean word.

4. **Packet scale and braid necessities.**  Independently serviced packets
   in a near-width construction cannot all be shorter than the Gaussian
   scale.  In a packetization of one SCD, at least
   \((3/4-o(1))W(k)\) chains must lie in packets containing at least

   \[
   \frac{\sqrt{k}}8-\frac12
   \tag{0.6}
   \]

   SCD chains.  A genuine global braid can escape this packet lower bound,
   but a near-width braid must reuse endpoints across \(\Omega(W(k))\) box
   incidences and across \(\Omega(W(k)/\sqrt{k})\) physical endpoint
   positions.  Its interval assignment must also satisfy an exact
   coordinatewise safe-pin condition proved below.

### The sole positive gate left by this lane — UNPROVED

It is enough to construct non-product MTF packets satisfying

\[
 \boxed{
 \sum_\alpha(t_\alpha-M_\alpha)=o(W(k)),
 \qquad
 \sum_\alpha(b_\alpha-1)=o(W(k)).}
\tag{0.7}
\]

A convenient stronger sufficient form is

\[
 \#\{\text{packets}\}=o(W(k)/k),
 \qquad
 \sum_\alpha(t_\alpha-M_\alpha)=o(W(k)),
\tag{0.8}
\]

because every ordered partition has at most \(k\) blocks.  No construction
meeting (0.7) or (0.8) is proved here.  Thus this report does not prove the
coefficient-one conjecture.  It replaces the false fixed-product gate by an
exact global non-product gate and proves that the packets must genuinely
cross atomic product parents.

---

## 1. Exact SCD bookkeeping

For an SCD of the \(s\)-cube, let \(c_s(h)\) be the number of chains of
height \(h\).  This number is independent of the SCD.  If
\(h\equiv s\pmod2\), then

\[
 c_s(h)
 =\binom{s}{(s-h)/2}-\binom{s}{(s-h)/2-1}
 =\frac{2(h+1)}{s+h+2}\binom{s}{(s-h)/2};
\tag{1.1}
\]

otherwise \(c_s(h)=0\).  Consequently

\[
 \sum_hc_s(h)=W(s),
 \qquad
 \sum_hc_s(h)(h+1)=2^s.
\tag{1.2}
\]

The following two standard consequences of (1.1) are included with the
quantifiers needed later.

### Lemma 1.1 — a uniform size-biased cutoff

There is an absolute constant \(C_0\ge1\) such that, for every integer
\(s\ge0\),

\[
 \sum_{h\le C_0\sqrt{s+1}}c_s(h)(h+1)\ge2^{s-1}.
\tag{1.3}
\]

#### Proof

The exact formula (1.1) gives the needed ratio estimate directly.  For
example, when \(s=2n\) and \(h=2r\),

\[
 \frac{\binom{2n}{n-r}}{\binom{2n}{n}}
 =\prod_{q=1}^{r}\frac{n-q+1}{n+q}
 \le
 \exp\!\left(-\sum_{q=1}^{r}\frac{2q-1}{n+q}\right)
 \le C\exp\!\left(-c\frac{r^2}{n+1}\right).
\]

The odd case is the same product with half-step endpoints.  Multiplying by
the prefactor in (1.1) gives absolute constants \(C,c>0\) such that

\[
 \frac{c_s(h)}{W(s)}
 \le
 C\frac{h+1}{s+1}
       \exp\!\left(-c\frac{h^2}{s+1}\right).
\tag{1.4}
\]

Summing (1.4) over the parity lattice gives

\[
 \sum_hc_s(h)(h+1)^3
 \le C_1W(s)(s+1)^{3/2}
\tag{1.5}
\]

for an absolute \(C_1\).  Indeed, after the factor \((s+1)^{-1}\),
the relevant Gaussian sum is bounded by a constant multiple of
\(\int_0^\infty(x+1)^4e^{-cx^2/(s+1)}dx=O((s+1)^{5/2})\).
Central-binomial estimates also give

\[
 W(s)\sqrt{s+1}\le C_2 2^s.
\tag{1.6}
\]

For \(D\ge1\), (1.5) therefore implies

\[
 \begin{aligned}
 \sum_{h>D\sqrt{s+1}}c_s(h)(h+1)
 &\le \frac1{D^2(s+1)}
       \sum_hc_s(h)(h+1)^3\\
 &\le \frac{C_1C_2}{D^2}2^s.
 \end{aligned}
\tag{1.7}
\]

Choose \(D\) so that \(C_1C_2/D^2\le1/2\), and enlarge it to cover the
finitely many small values hidden in (1.4).  Equation (1.2) then gives
(1.3). \(\square\)

### Lemma 1.2 — a fixed high-chain window

For every fixed \(A>0\),

\[
 \frac1{W(s)}
 \sum_{A\sqrt s\le h\le(A+1)\sqrt s}c_s(h)
 \longrightarrow
 u(A):=e^{-A^2/2}-e^{-(A+1)^2/2}>0,
\tag{1.8}
\]

with the required parity rounding.

#### Proof

Uniformly for \(h=x\sqrt s\) in a fixed compact positive interval,
Stirling's formula in (1.1) gives

\[
 \frac{c_s(h)}{W(s)}
 =\frac{2x}{\sqrt s}e^{-x^2/2}+o(s^{-1/2}).
\tag{1.9}
\]

Admissible heights are spaced by two, so (1.9) is the Riemann sum for
\(\int_A^{A+1}xe^{-x^2/2}dx=u(A)\). \(\square\)

The same calculation, with the Gaussian bound (1.4) controlling the
unbounded tail, gives for every fixed \(a\ge0\)

\[
 \boxed{
 \frac1{W(s)}\sum_{h\ge a\sqrt s}c_s(h)
 \longrightarrow e^{-a^2/2}.}
\tag{1.9a}
\]

Multiplying (1.9) by \(h+1\), and using
\(W(s)\sqrt{s}/2^s\to\sqrt{2/\pi}\), also gives the size-biased window law

\[
 \boxed{
 \frac1{2^s}
 \sum_{a\sqrt s\le h\le b\sqrt s}c_s(h)(h+1)
 \longrightarrow
 \sqrt{\frac2\pi}\int_a^b x^2e^{-x^2/2}\,dx>0}
\tag{1.9b}
\]

for every fixed \(0<a<b<\infty\).

Now split \([k]\) into blocks of dimensions \(s_1,\ldots,s_t\), and choose
an arbitrary SCD in every block.  A tuple of block chains is a literal
join-embedded product parent.  Since every block chain is centered in its
block cube, every product parent is centered at the global middle rank.
The parents partition the Boolean cube; hence their widths add exactly:

\[
 \boxed{
 \sum_{\text{product parents }P}w(P)=W(k).}
\tag{1.10}
\]

There is no averaging or fractional assignment in (1.10).

---

## 2. The generalized plateau endpoint theorem

Let

\[
 Q=\prod_{i=1}^{d-1}[0,p_i],
 \qquad
 B=|Q|=\prod_{i<d}(p_i+1),
 \qquad
 S=\sum_{i<d}p_i>0,
\tag{2.1}
\]

and let \(P=Q\times[0,L]\), where \(L>S\).  Put

\[
 H=L-S.
\tag{2.2}
\]

For every rank \(r=S,S+1,\ldots,L\), the rank-\(r\) layer of \(P\) contains
one point above every \(q\in Q\): its last coordinate is
\(r-\operatorname{rank}_Q(q)\).  Thus these \(H+1\) layers all have size
\(B\).  Projection onto \(Q\) gives a chain cover by \(B\) chains, while a
full plateau layer is an antichain of size \(B\).  Therefore

\[
 w(P)=B.
\tag{2.3}
\]

### Theorem 2.1 — flat-plateau endpoint lower bound

For \(S>0\) and \(L>S\), every word covering \(P\) satisfies

\[
 \boxed{
 g(P)-B
 \ge
 \left\lceil\frac{B(L-S)}{2L}\right\rceil .}
\tag{2.4}
\]

The same conclusion holds for an affine Boolean translate of the box and
when every chosen witness is permitted to use arbitrary foreign letters.

#### Proof

Choose one witnessing interval for every target in every plateau layer.
Group the targets first by common physical left endpoint and then, in a
second partition, by common physical right endpoint.  At a fixed left
endpoint, extending the right endpoint only enlarges the interval union;
hence each group is a chain in the product order.  The same is true at a
fixed right endpoint.

Consider either endpoint partition.  Let its number of chains be

\[
 C=B+\delta.
\tag{2.5}
\]

Every plateau layer occupies exactly \(B\) of these chains.  Two consecutive
layers therefore occupy at least \(B-\delta\) common chains.  The two points
in any common chain are comparable and their ranks differ by one, so they
form a genuine product-poset cover.  Across the \(H\) adjacent pairs of
plateau layers, the endpoint partition uses at least

\[
 H(B-\delta)
\tag{2.6}
\]

covers.

Put

\[
 \phi(q,z)=\operatorname{rank}_Q(q),
 \qquad 0\le\phi\le S.
\tag{2.7}
\]

The bottom and top plateau layers have identical \(\phi\)-multisets.  Exactly
\(B\) partition chains meet the bottom layer and exactly \(B\) meet the top
layer.  The other \(\delta\) chains start internally and the other
\(\delta\) chains end internally.  If \(M=\sum_{q\in Q}\operatorname{rank}_Q(q)\),
then the sum of the starting potentials is at least \(M\), while the sum of
the ending potentials is at most \(M+S\delta\).  Telescoping on all partition
chains shows that their total transverse potential increase is at most

\[
 S\delta.
\tag{2.8}
\]

Every cover counted in (2.6) either increases \(\phi\) by one or is a cover
in the last-coordinate direction.  Consequently this endpoint partition
uses at least

\[
 H(B-\delta)-S\delta=HB-L\delta
\tag{2.9}
\]

last-coordinate covers.  A negative right side is harmless; equivalently the
lower bound is \([HB-L\delta]_+\).

The left- and right-endpoint partitions cannot use the same cover.  If they
did, its two distinct endpoint targets would have both the same left endpoint
and the same right endpoint, so one physical interval would have two
different unions.  There are exactly \(BH\) last-coordinate covers in the
plateau slab.  Applying (2.9) to the two partitions gives

\[
 2HB-L(\delta_L+\delta_R)\le BH,
\]

and hence

\[
 \delta_L+\delta_R\ge\frac{BH}{L}.
\tag{2.10}
\]

If the word has length \(n\), then each endpoint partition has at most
\(n\) classes.  Therefore \(\delta_L,\delta_R\le n-B\), and (2.10) gives

\[
 n-B\ge\frac{BH}{2L}.
\tag{2.11}
\]

Integrality gives (2.4).

Only target inclusion and physical endpoints entered the argument.  The
letters inside a witness need not lie in the box, and a Boolean common base
is present in every translated target and cancels from all comparisons.
Thus seams and affine translation do not change the proof. \(\square\)

### The zero-base exception

When \(S=0\), the relative box is the chain \([0,L]\).  If its local zero
is the global empty target, that point is not required, and the correct
separate identity is

\[
 \boxed{g_1(L)=L.}
\tag{2.12}
\]

Indeed, every interval maximum is one of the word letters, so \(L\) distinct
nonzero chain values require at least \(L\) letters; listing them gives
equality.

For an affine Boolean chain with a nonempty common base, the local zero is an
actual nonempty target.  If all \(L+1\) chain points are selected, the proof
of Theorem 2.1 runs with \(B=1,S=0,H=L\) and gives the endpoint statement

\[
 \boxed{\delta_L+\delta_R\ge1.}
\tag{2.13}
\]

This affine case will be used in Section 7.1.

---

## 3. Every fixed number of separately paid product factors fails

The next theorem is uniform both in the coordinate dimensions and in the
chosen SCDs.

### Theorem 3.1 — positive exact width in a giant-side sector

Fix integers \(t\ge2\) and a real \(K>1\).  There is a constant
\(\beta_{t,K}>0\) such that the following holds for all sufficiently large
\(k\).

For every dimension split

\[
 s_1+\cdots+s_t=k
\tag{3.1}
\]

and arbitrary SCDs of the block cubes, a family of product parents of total
exact width at least \(\beta_{t,K}W(k)\) has one side \(L\) satisfying

\[
 L>K\sum_{i\ne j}\ell_i.
\tag{3.2}
\]

#### Proof

Relabel so that

\[
 s_j=\max_i s_i\ge k/t.
\tag{3.3}
\]

Let \(C_0\) be from Lemma 1.1.  Choose a fixed constant

\[
 A>2KC_0(t-1).
\tag{3.4}
\]

Use the event

\[
 A\sqrt{s_j}\le L\le(A+1)\sqrt{s_j}
\tag{3.5}
\]

in the distinguished block and

\[
 \ell_i\le C_0\sqrt{s_i+1}\qquad(i\ne j)
\tag{3.6}
\]

in every other block.  Since \(s_i\le s_j\) and \(s_j\to\infty\), equations
(3.4)--(3.6) imply (3.2) for all sufficiently large \(k\).

For such a parent put

\[
 S=\sum_{i\ne j}\ell_i,
 \qquad
 B=\prod_{i\ne j}(\ell_i+1).
\tag{3.7}
\]

Since \(L>S\), its exact width is \(B\).  By Lemmas 1.1 and 1.2, after
decreasing the limiting constant in (1.8), the total event width is at least

\[
 \begin{aligned}
 &\left(\sum_{L\text{ in }(3.5)}c_{s_j}(L)\right)
  \prod_{i\ne j}
  \left(\sum_{\ell_i\text{ in }(3.6)}
          c_{s_i}(\ell_i)(\ell_i+1)\right)\\
 &\hspace{2cm}\ge
 u_A W(s_j)\,2^{k-s_j-(t-1)},
 \end{aligned}
\tag{3.8}
\]

where one may take, for all large \(k\),

\[
 u_A=\frac12\left(e^{-A^2/2}-e^{-(A+1)^2/2}\right)>0.
\tag{3.9}
\]

The coefficient convolution gives the exact inequality

\[
 W(k)\le W(s_j)2^{k-s_j}:
\tag{3.10}
\]

indeed, each coefficient of
\((1+x)^k=(1+x)^{s_j}(1+x)^{k-s_j}\) is at most
\(W(s_j)2^{k-s_j}\).  Thus (3.8) is at least

\[
 \beta_{t,K}W(k),
 \qquad
 \boxed{\beta_{t,K}=u_A2^{-(t-1)}>0.}
\tag{3.11}
\]

This is uniform over (3.1), including zero-dimensional and submacroscopic
blocks. \(\square\)

### Theorem 3.2 — fixed-\(t\) isolated-parent no-go

Under the hypotheses of Theorem 3.1, suppose every atomic product parent is
serviced by its own literal word, with no witness interval or physical letter
shared between distinct parents.  Then there is \(\epsilon_{t,K}>0\) such
that

\[
 \boxed{
 \sum_P g(P)\ge(1+\epsilon_{t,K})W(k)}
\tag{3.12}
\]

for all sufficiently large \(k\).  One may take any fixed

\[
 0<\epsilon_{t,K}<
 \frac{K-1}{2K}\,\beta_{t,K}.
\tag{3.13}
\]

The same lower bound applies if arbitrary additional initialization or
translated-origin letters are charged.

#### Proof

For an event parent with \(S>0\), Theorem 2.1 and \(L>KS\) give

\[
 g(P)-w(P)
 \ge
 \frac{B(L-S)}{2L}
 >\theta_KB,
 \qquad
 \theta_K:=\frac{K-1}{2K}.
\tag{3.14}
\]

If \(S=0\), then \(B=1\), and (2.12) gives
\(g(P)-w(P)=L-1\ge\theta_K\) for all large \(k\).
Theorem 3.1 therefore supplies excess at least
\(\theta_K\beta_{t,K}W(k)\).

Every other positive-height product box has \(g(P)\ge w(P)\).  One way to
see this is to group represented targets by a common right endpoint; the
groups are chains, so the number of word positions is at least the width of
the nonzero target poset.  The only negative convention is the all-zero
parent, for which \(g-w=-1\).

Its multiplicity is negligible uniformly in (3.1).  If
\(z_s=c_s(0)\), then

\[
 \frac{z_{s_j}}{W(s_j)}\le\frac{2}{s_j+2},
\tag{3.15}
\]

and \(\prod_iW(s_i)\le W(k)\), because the product of block middle
antichains is an antichain in the \(k\)-cube.  Hence

\[
 \prod_i z_{s_i}
 \le \frac{2}{s_j+2}\prod_iW(s_i)
 =o(W(k)).
\tag{3.16}
\]

Combine (1.10), (3.14), and (3.16), then choose
\(\epsilon_{t,K}<\theta_K\beta_{t,K}\). \(\square\)

### Consequences

1. For balanced positive-proportion blocks, the number of \(t\)-chain
   parents is \(\Theta(2^k/k^{t/2})\).  Equation (3.12) therefore says that
   their mean local excess is

   \[
   \Omega_t\!\left(k^{(t-1)/2}\right).
   \tag{3.17}
   \]

   For \(t=4\), this is \(\Omega(k^{3/2})\), exactly the scale that GF4
   required to be little-oh.  Thus GF4 is false.

2. Any compact four-box theorem implying
   \(g_4=w_4+o(R^3)\) uniformly also fails.  For balanced four blocks, refine
   the event in Theorem 3.1 by putting each nondistinguished height in a fixed
   positive Rayleigh window \([a_iR,b_iR]\).  The size-biased law (1.9b)
   shows that this compact positive subevent retains positive exact
   width.  Every one of its parents has \(B=\Theta(R^3)\), so (3.14) gives
   individual defect \(\Omega(R^3)\).

3. A uniformly \(o(R^2)\)-excess adjacent-child fusion inside each
   four-parent would sum to \(o(R^3)\) in that parent, so the former uniform
   separately paid all-parent APF gate also fails.  This says nothing against
   a construction whose packets cross distinct four-parents.

4. Suppose a bottom-respecting MTF cover of a four-box uses \(\tau(P)\)
   states and initialization cost \(O(R)\).  It gives a literal word of
   length at most \(\tau(P)+O(R)\), so

   \[
   \tau(P)-w(P)\ge g(P)-w(P)-O(R).
   \tag{3.18}
   \]

   On the compact positive subevent from item 2, the first term on the right
   is \(\Omega(R^3)\).  Hence the separately paid four-box MTF average gate
   is false as well.  Dimension four is not the first surviving separately
   paid dimension.

5. The proof is uniform over deterministic dimension splits.  Randomly
   choosing one whole separately paid split cannot help.  A targetwise
   mixture of overlapping splits is instead an incompatible integral
   allocation and is not covered by this sentence.  The constant obtained
   here is not uniform when \(t=t(k)\to\infty\): the selected high window
   moves outward with \(t\), and \(\beta_{t,K}\) tends rapidly to zero.
   Growing atomic dimension remains outside this no-go.

---

## 4. Adaptive refinement inside a parent

Theorem 3.2 already allows arbitrary processing inside a fixed parent: no
internal algorithm can have length below \(g(P)\).  There is also a useful
structural statement showing why an exactly centered refinement cannot steer
the giant-side parents into an easier three-box cone.

Let \(P=Q\times[0,L]\) be an event parent, put

\[
 D=L-S>0,
 \qquad
 T=L+S,
\tag{4.1}
\]

and suppose \(P\) is partitioned into literal join-embedded affine product
leaves.  Each factor is required to be a saturated ambient Boolean chain,
with disjoint coordinate support from the other factors (or, equivalently
for this argument, with a cover-preserving product embedding).  For a leaf
\(\lambda\), let \(\delta_\lambda\) be its bottom-rank shift and let
\(H_\lambda\) be the sum of its side heights.

### Strong centering hypothesis

The following exact identity, not merely equality of floored middle ranks, is
required:

\[
 \boxed{2\delta_\lambda+H_\lambda=T.}
\tag{4.2}
\]

Under these hypotheses, refining every leaf by an internal SCD gives an SCD
of the whole parent: internal leaf covers are ambient covers, and every
resulting chain has absolute endpoint-rank sum \(T\).

### Lemma 4.1 — all parent SCD chains are long

Every chain in every SCD of \(P\) has height at least \(D=L-S\).

#### Proof

The rank numbers of \(P\) are constant and equal to \(B\) from rank \(S\)
through rank \(L\).  In an SCD centered at total rank \(T\), the number of
chains beginning at a rank \(r\le\lfloor T/2\rfloor\) is the rank-number
difference \(a_r-a_{r-1}\).  No chain therefore begins above rank \(S\).
Its height is \(T-2r\ge T-2S=L-S=D\). \(\square\)

For a three-chain leaf, zero-pad if necessary and sort its heights as
\(x\le y\le z\).  The minimum chain height in an SCD of that product is

\[
 h_{\min}(x,y,z)=
 \begin{cases}
 z-x-y,&z\ge x+y,\\
 (x+y+z)\bmod2,&z<x+y.
 \end{cases}
\tag{4.3}
\]

This follows directly from the rank-number differences: in the plateau case
the last chains begin at rank \(x+y\), while in the strict central-growth
case the last chains begin at \(\lfloor(x+y+z)/2\rfloor\).

By Lemma 4.1, (4.3) must be at least \(D\).  On the event in Theorem 3.1,
\(D\to\infty\), so the second case of (4.3) is impossible and

\[
 \boxed{z-x-y\ge D.}
\tag{4.4}
\]

Thus every three-chain leaf is itself deep in the plateau sector.  If
\(x+y>0\), Theorem 2.1 gives

\[
 \begin{aligned}
 g(\lambda)-w(\lambda)
 &\ge \frac{w(\lambda)(z-x-y)}{2z}\\
 &\ge \frac{w(\lambda)D}{2(L+S)}
 >\frac{K-1}{2(K+1)}w(\lambda).
 \end{aligned}
\tag{4.5}
\]

If \(x=y=0\), the leaf is a chain with \(z\ge D\ge2\), and
\(g_1(z)-1=z-1\), which is stronger.  A dimension-zero leaf is impossible
because it would contribute a height-zero chain to the parent SCD.

Finally, exact centering makes widths add at the parent middle rank:

\[
 \sum_\lambda w(\lambda)=B.
\tag{4.6}
\]

Therefore a separately paid exactly centered refinement into at most
three-chain leaves retains a fixed fractional parent defect.  Sharing leaf
origins does not remove this endpoint defect.  However, one must not say that
arbitrary singleton origins are literally free while still counting their
widths in the baseline: each separately paid leaf must cover its actual
central targets.

The strong hypothesis (4.2) is essential.  The weaker condition

\[
 \delta_\lambda+\left\lfloor H_\lambda/2\right\rfloor
 =\left\lfloor T/2\right\rfloor
\]

does not control parity, and the union of the internal leaf SCDs need not be
an SCD of the parent.

### Scope for adaptive coordinate menus

A fixed finite menu of *compatible* adaptive splits is also covered whenever
all its cells have a common fixed atomic product refinement and distinct
atomic parents are still serviced independently.  Incompatible overlapping
decompositions, with target-by-target cherry-picking among their cells, do
not form a partition and require a new integral allocation theorem.  They
are not ruled out by relabeling the menu as one decomposition.

---

## 5. The valid replacement: non-product SCD packets

The preceding no-go concerns the place at which payment is separated, not
the use of SCDs themselves.  SCD chains remain an exact width certificate if
they are packetized across product-parent boundaries.

### Theorem 5.1 — literal SCD packet aggregation

Fix one SCD \(\mathcal D\) of \(2^{[k]}\), with its \(W=W(k)\) chains.
Partition these chains into packets \(P\).  Let \(U(P)\) be the union of the
targets in the chains in \(P\), and let \(q(P)\) be the number of chains in
the packet.  Then

\[
 \operatorname{width}(U(P))=q(P).
\tag{5.1}
\]

If a literal word of length \(n(P)\) covers \(U(P)\setminus\{\varnothing\}\),
then \(n(P)\ge q(P)\), and concatenating all packet words gives

\[
 \boxed{
 \nu(k)\le
 \sum_Pn(P)
 =W+\sum_P(n(P)-q(P)).}
\tag{5.2}
\]

#### Proof

The \(q(P)\) SCD chains cover \(U(P)\), so its width is at most \(q(P)\).
Every symmetric chain meets the upper middle rank \(\lceil k/2\rceil\)
exactly once, and
these \(q(P)\) middle elements form an antichain, proving (5.1).  Choose one
witnessing interval for every nonempty packet target and group the chosen
targets by their common right endpoint.  This partitions them into at most
\(n(P)\) inclusion chains, so \(n(P)\ge q(P)\).  Every witness interval
remains inside its packet segment after concatenation.  Finally
\(\sum_Pq(P)=W\), proving (5.2). \(\square\)

The theorem is deliberately non-product: a useful packet must contain chains
from many of the bad atomic parents in Theorem 3.1.

### Ordered partitions and MTF updates

An ordered partition of \([k]\) is a tuple

\[
 \Pi=(B_1,\ldots,B_b)
\tag{5.3}
\]

of disjoint nonempty blocks with union \([k]\).  Its nonempty prefix-union
chain is

\[
 \operatorname{Pref}(\Pi)
 =\{B_1,B_1\cup B_2,\ldots,B_1\cup\cdots\cup B_b\}.
\tag{5.4}
\]

For a nonempty update mask \(X\), define

\[
 M_X(\Pi)
 =(X,B_1\setminus X,\ldots,B_b\setminus X),
\tag{5.5}
\]

deleting empty blocks.  If \(\Pi\) is the last-occurrence ordered partition
of a Boolean word prefix, appending \(X\) changes the state exactly to
\(M_X(\Pi)\); the suffix ORs ending there are exactly the prefix unions in
(5.4).

### Theorem 5.2 — exact packet-MTF aggregation

Partition all nonempty Boolean targets into packets \(\mathcal P_\alpha\).
For packet \(\alpha\), suppose there is an MTF walk

\[
 \Pi_{\alpha,1},\ldots,\Pi_{\alpha,t_\alpha}
\tag{5.6}
\]

whose prefix-union chains collectively cover \(\mathcal P_\alpha\).  Let
\(b_\alpha\) be the number of blocks of \(\Pi_{\alpha,1}\), and let

\[
 M_\alpha
 =\left|\mathcal P_\alpha\cap
   \binom{[k]}{\lceil k/2\rceil}\right|.
\tag{5.7}
\]

Then \(t_\alpha\ge M_\alpha\), and

\[
 \boxed{
 \nu(k)\le W(k)
 +\sum_\alpha(t_\alpha-M_\alpha)
 +\sum_\alpha(b_\alpha-1).}
\tag{5.8}
\]

#### Proof

Initialize \(\Pi_{\alpha,1}=(B_1,\ldots,B_{b_\alpha})\) by appending its
blocks in reverse order,

\[
 B_{b_\alpha},\ldots,B_1.
\tag{5.9}
\]

Their last occurrences are then ordered as \(B_1,\ldots,B_{b_\alpha}\).
Append the \(t_\alpha-1\) update masks giving the subsequent states in
(5.6).  This is a literal packet word of length

\[
 b_\alpha+t_\alpha-1.
\tag{5.10}
\]

A prefix-union chain contains at most one member of the middle antichain, so
\(t_\alpha\ge M_\alpha\).  Concatenate the packet words.  Since the target
packets partition the middle layer,

\[
 \sum_\alpha M_\alpha=W(k).
\tag{5.11}
\]

Now sum the identity

\[
 b_\alpha+t_\alpha-1
 =M_\alpha+(t_\alpha-M_\alpha)+(b_\alpha-1)
\]

and use (5.11). \(\square\)

This proves (0.5)--(0.8) with no common-owner or fractional-synchronization
assumption.

Conversely, grouping the targets of any universal word by a chosen common
right endpoint covers the Boolean lattice by at most as many inclusion
chains as there are word positions.  The middle antichain therefore gives
the standard lower bound \(\nu(k)\ge W(k)\).  Consequently either (0.7) or
(0.8), together with (5.8), would prove
\(\nu(k)=(1+o(1))W(k)\).

### State-aware SCD path form

A useful special case chooses one designated MTF state visit for each of the
\(W\) chains of an SCD, together with \(A\ge0\) auxiliary or repeated state
visits.  Partition the resulting visits into MTF paths.  If path \(a\) starts
with a state having \(b_a\) blocks, then the construction above has exact
length

\[
 \boxed{
 W+A+\sum_a(b_a-1).}
\tag{5.12}
\]

Thus the exact missing state-transversal gate is

\[
 A+\sum_a(b_a-1)=o(W).
\tag{5.13}
\]

### A particularly economical forest target — UNPROVED

For \(k=2m\), the number of height-zero SCD chains is

\[
 c_{2m}(0)=\frac{W}{m+1}.
\tag{5.14}
\]

Such a singleton middle chain has a canonical exposing state with two
nonempty blocks.  If there existed a genuine MTF forest with one designated
state per SCD chain, with **exactly these shortest chains as its roots, and
with their selected root states equal to those canonical two-block exposing
states**, then (5.12) would give

\[
 \nu(2m)\le W+\frac{W}{m+1}=W+O(W/k).
\tag{5.15}
\]

For \(k=2m+1\), the shortest height-one chains number

\[
 c_{2m+1}(1)=\frac{2W}{m+2},
\tag{5.16}
\]

and their canonical exposing states have three blocks.  A forest rooted
exactly there, whose selected root states are those canonical three-block
states, would give

\[
 \nu(2m+1)
 \le W+2c_{2m+1}(1)
 =W+\frac{4W}{m+2}.
\tag{5.17}
\]

The existence assertions in the preceding two paragraphs are **UNPROVED**.
The arithmetic is conditional and exact.  An arbitrary MTF forest is not
entitled to the root counts (5.14) or (5.16); those chains must actually be
declared roots, or a no-incoming-edge theorem must force them.  Nor does the
choice of a root chain alone justify a two- or three-block reset: the selected
root state must be the stated canonical exposing state, since outgoing MTF
compatibility could otherwise force a different state in the same exposing
fiber.

Two natural candidates do not establish this gate:

* The standard Greene--Kleitman last-pair map omits \(W(k-1)\) chain
  templates from its image.  Any injectively selected path forest using only
  those last-pair arcs therefore has at least
  \(W(k-1)=(1/2+o(1))W(k)\) roots and pays \(\Omega(W)\) reset toll.  The raw
  many-to-one map is not itself asserted to be a path cover.

* In even dimension, a two-sided central-projection forest may have only
  \(\operatorname{Cat}_m=W/(m+1)\) abstract components, but the central-square
  transition barrier shows that at least
  \(W-2\operatorname{Cat}_m-1=\Theta(W)\) of its internal adjacencies are not
  one-step MTF transitions.  Repairing only the Catalan many seams therefore
  does not produce (5.13).

These failures concern the named maps, not an arbitrary state-aware MTF
forest.

---

## 6. Independently serviced packets must be mesoscopic

The non-product gate cannot be satisfied by breaking the lattice into very
small independently initialized pieces.

### Proposition 6.1 — interval-capacity lower bound

Suppose the nonempty Boolean targets are partitioned into arbitrary packets,
and packet \(P\) is serviced by an independent word of length \(n_P\).  Then

\[
 \sum_P\binom{n_P+1}{2}\ge2^k-1.
\tag{6.1}
\]

If \(N=\sum_Pn_P=(1+o(1))W(k)\), then

\[
 \boxed{
 \max_Pn_P
 \ge (\sqrt{2\pi}+o(1))\sqrt{k}.}
\tag{6.2}
\]

#### Proof

A length-\(n_P\) word has only \(\binom{n_P+1}{2}\) nonempty intervals, and
distinct targets require distinct intervals, proving (6.1).  If
\(n_*=\max_Pn_P\), then

\[
 2^k-1
 \le\frac12\sum_Pn_P(n_P+1)
 \le\frac12N(n_*+1).
\]

Thus

\[
 n_*\ge\frac{2(2^k-1)}N-1.
\tag{6.3}
\]

Using \(W(k)=(1+o(1))2^k\sqrt{2/(\pi k)}\) gives (6.2). \(\square\)

For packets made from one SCD there is a stronger mass statement.

### Theorem 6.2 — most SCD chains require large packets

Partition the chains of one SCD into packets \(P\).  Let \(q_P\) be the
number of chains and let \(n_P\) be the length of an independent literal word
covering the packet.  If

\[
 \sum_Pn_P=W(k)+o(W(k)),
\tag{6.4}
\]

then at least \((3/4-o(1))W(k)\) SCD chains lie in packets satisfying

\[
 \boxed{q_P\ge\frac{\sqrt{k}}8-\frac12.}
\tag{6.5}
\]

#### Proof

Call a chain tall if its height is at least \(\sqrt{k}/2\).  The explicit
Rayleigh tail (1.9a), with \(a=1/2\), gives

\[
 \frac{\#\{\text{tall chains}\}}{W(k)}
 \longrightarrow e^{-1/8}>\frac78.
\tag{6.6}
\]

Put \(e_P=n_P-q_P\ge0\).  Equation (6.4) says
\(\sum_Pe_P=o(W)\).  Packets with \(e_P>q_P\) contain a total of only
\(o(W)\) chains.  Every remaining packet has \(n_P\le2q_P\).

Now discard every remaining packet containing fewer than \(q_P/2\) tall
chains.  Within each such packet the number of tall chains is smaller than
the number of short chains.  By (6.6), all short chains together number less
than \((1/8+o(1))W\).  Consequently more than

\[
 \left(\frac78-\frac18-o(1)\right)W
 =\left(\frac34-o(1)\right)W
\tag{6.7}
\]

tall chains remain in packets having both

\[
 n_P\le2q_P,
 \qquad
 \#\{\text{tall chains in }P\}\ge q_P/2.
\tag{6.8}
\]

Such a packet contains at least \(q_P\sqrt{k}/4\) distinct nonzero targets.
The possible loss of the empty target is absorbed by the extra endpoint in
each tall chain.  On the other hand its word has at most

\[
 \binom{n_P+1}{2}
 \le\binom{2q_P+1}{2}=2q_P^2+q_P
\tag{6.9}
\]

intervals.  Hence

\[
 \frac{q_P\sqrt{k}}4\le2q_P^2+q_P,
\]

which is equivalent to (6.5). \(\square\)

Theorems 6.1 and 6.2 apply to independently serviced packets.  A global word
whose intervals cross packet boundaries is not a concatenation of those
packet words and can escape these bounds.

---

## 7. What a genuine global box braid must do

The fixed-product no-go does not imply a lower bound for a single global
word, because one physical endpoint can serve selected witnesses from many
parents.  The following statements quantify that escape and audit its literal
feasibility.

### 7.1 Endpoint incidence forced by the giant-side parents

Use the event family from Theorem 3.1.  In each event parent select all its
plateau targets.  In every other nonzero parent select one full local middle
layer.  For a physical word position \(r\), let

\[
 \ell_r=\#\{\text{parents having a selected witness with left endpoint }r\},
\]

and define \(r_r\) analogously for right endpoints.  Put

\[
 \mathcal C_\partial
 =\sum_r\bigl((\ell_r-1)_++(r_r-1)_+\bigr).
\tag{7.1}
\]

For an event parent, the proof of Theorem 2.1 gives the stronger endpoint
statement

\[
 (C_L-B)+(C_R-B)
 \ge\frac{B(L-S)}L
 >\frac{K-1}{K}B=2\theta_KB.
\tag{7.2}
\]

For \(S>0\), this is exactly (2.10).  If an event parent has \(S=0\), then
\(B=1\) and, by (3.5), \(L\le(A+1)\sqrt{k}<k\) for all large \(k\).  Since
the parent is centered in the \(k\)-cube, its absolute bottom rank is
\((k-L)/2>0\); its local zero is therefore a nonempty Boolean target.  Select
all \(L+1\) chain points.  Equation (2.13) gives
\(\delta_L+\delta_R\ge1>(K-1)/K\), so (7.2) holds in this case as well.
All-zero non-event parents are omitted at the \(o(W)\) cost in (3.16).

Every other selected middle layer requires at least its width in each
endpoint partition.  Summing (7.2), using (1.10), Theorem 3.1, and the
\(o(W)\) zero-parent exception, gives

\[
 \sum_r(\ell_r+r_r)
 \ge2W+2\theta_K\beta_{t,K}W-o(W).
\tag{7.3}
\]

For nonnegative integers \(x_r\),

\[
 \sum_rx_r\le n+\sum_r(x_r-1)_+.
\tag{7.4}
\]

Therefore every length-\(n\) global word satisfies

\[
 \boxed{
 \mathcal C_\partial
 \ge
 2\theta_K\beta_{t,K}W-2(n-W)-o(W).}
\tag{7.5}
\]

In particular, if \(n=W+o(W)\), a linear number of endpoint-parent
incidences must be shared.

There is also a physical-position consequence.  At a common left endpoint,
all represented targets form a strict inclusion chain; hence their ranks are
strictly increasing.  Let \(\sigma_L(r)\) be the difference between the
largest and smallest selected ranks at left endpoint \(r\), with value zero
when at most one parent occurs.  Then

\[
 (\ell_r-1)_+\le\sigma_L(r),
 \qquad
 (r_r-1)_+\le\sigma_R(r).
\tag{7.6}
\]

Every product parent is centered at the global middle rank.  Its selected
plateau has global rank span \(L-S\le(A+1)\sqrt{k}\), and every non-event
target was selected at the middle.  Thus all selected ranks lie in one
interval containing at most

\[
 T_k=(A+1)\sqrt{k}+3
\tag{7.7}
\]

integer ranks.  If \(P_\partial\) is the number of physical positions shared
by at least two parents on the left or on the right, then

\[
 \sum_r(\sigma_L(r)+\sigma_R(r))
 \le2P_\partial(T_k-1).
\tag{7.8}
\]

Combining (7.5)--(7.8), a near-width word must have

\[
 \boxed{P_\partial=\Omega_{t,K}(W(k)/\sqrt{k}).}
\tag{7.9}
\]

This is necessary, not contradictory: a sublinear number of very
high-degree portals can meet (7.9).

### 7.2 Exact Safe-Pin Factorization

Endpoint capacity does not ensure that one set of Boolean letters realizes
all the desired interval unions.  The exact missing compatibility test is
coordinatewise.

Let a family \(\mathcal F\) of nonempty targets be assigned prescribed
nonempty intervals

\[
 I_T\subseteq[n]\qquad(T\in\mathcal F).
\tag{7.10}
\]

For each coordinate \(x\in[k]\), define its safe positions by

\[
 U_x=[n]\setminus
 \bigcup_{T\in\mathcal F:\,x\notin T}I_T.
\tag{7.11}
\]

### Theorem 7.1 — Safe-Pin Factorization

There are Boolean letters \(A_1,\ldots,A_n\), temporarily allowing empty
letters, such that

\[
 \bigcup_{j\in I_T}A_j=T
 \qquad\text{for every }T\in\mathcal F
\tag{7.12}
\]

if and only if

\[
 \boxed{
 I_T\cap U_x\ne\varnothing
 \quad\text{for every }T\in\mathcal F\text{ and every }x\in T.}
\tag{7.13}
\]

After deleting empty letters, (7.12) becomes an ordinary nonzero Boolean word
of length at most \(n\), with the retained images of all intervals still
contiguous and nonempty.

#### Proof

If (7.12) holds and \(x\notin T\), no position of \(I_T\) can contain
\(x\).  Thus every position containing \(x\) lies in \(U_x\).  If \(x\in T\),
some position of \(I_T\) must contain it, proving (7.13).

Conversely, set

\[
 A_j=\{x:j\in U_x\}.
\tag{7.14}
\]

If \(x\notin T\), (7.11) gives \(I_T\cap U_x=\varnothing\), so \(x\) is
absent from the union in (7.12).  If \(x\in T\), condition (7.13) puts
\(x\) into that union.  Hence the union is exactly \(T\).  Deleting empty
positions preserves the order, sends every interval to an interval of the
retained word, and (because \(T\ne\varnothing\)) leaves that image nonempty.
\(\square\)

Thus endpoint sharing and rank-span provide only capacity.  Safe-Pin
Factorization controls the negative constraints: a coordinate used to pin a
positive target must survive every overlapping interval of every target that
excludes it.

### 7.3 A no-go for sparse editing of isolated words

There is a simple but useful distinction between a genuinely new braid and
identifying a few seam tokens in pre-existing local words.

Take \(k=3s\) with \(s\) even and use the equal three-block decomposition.
Theorem 3.2, with \(t=3\) and \(K=2\), gives a fixed \(\delta_0>0\) and
separate total length

\[
 L_{\rm sep}\ge(1+\delta_0)W(k)-o(W(k))
\tag{7.15}
\]

for some fixed \(\delta_0>0\).  It has

\[
 \#\{\text{product parents}\}=\Theta(W(k)/k).
\tag{7.16}
\]

In the local word for parent \(P\), declare a mutable occurrence set \(E_P\).
Suppose every occurrence outside the \(E_P\)'s is preserved injectively as a
distinct physical position of the proposed global word.  Mutable occurrences
may be deleted, rewritten, or identified with unbounded multiplicity.  Then

\[
 n\ge L_{\rm sep}-\sum_P|E_P|.
\tag{7.17}
\]

Consequently, if

\[
 \max_P\frac{|E_P|}{k}\longrightarrow0,
\tag{7.17a}
\]

then (7.16) gives
\(\sum_P|E_P|=o(W)\), and

\[
 n\ge(1+\delta_0-o(1))W.
\tag{7.18}
\]

This is only an identification/editing no-go.  A construction that discards
the isolated local words and synthesizes a new \(\Theta(W)\)-scale braid is
outside (7.17), as it must be.

---

## 8. Exact route map and caveat ledger

### Closed routes

* No fixed \(t\) coordinate split, balanced or unbalanced, works by paying
  one word per atomic product parent.
* Randomly choosing one whole fixed-\(t\), separately paid split does not
  change that conclusion; targetwise use of overlapping splits is the
  incompatible-allocation case below.
* Height-adaptive cutting inside a parent does not help; in the strongly
  centered three-leaf setting it provably leaves every leaf in a plateau
  cone.
* A separately paid fused four-box word, a separately paid four-box MTF walk,
  and the former uniform separately paid all-parent adjacent-child fusion all
  retain \(\Omega(W)\) aggregate excess.
* Adding or identifying only \(o(k)\) occurrence tokens per equal
  three-block parent cannot amortize the gap.
* Uniformly \(o(\sqrt{k})\)-length independent packets are impossible, and
  most chains of an SCD must be aggregated in packets of
  \(\Omega(\sqrt{k})\) chains.

### Surviving routes

1. **Non-product SCD/MTF packets.**  Prove (0.7), or the stronger (0.8).
   Equations (5.8) and (5.12) then construct a literal OR word with exact
   coefficient-one accounting.

2. **A global box braid.**  Assign witnesses across many atomic parents,
   meet the endpoint incidence and rank-span necessities (7.5)--(7.9), and
   satisfy Safe-Pin Factorization (7.13).  This requires reorganization of a
   leading \(\Theta(W)\) amount of witness infrastructure.

3. **Growing atomic dimension.**  Let \(t=t(k)\to\infty\).  The constant in
   Theorem 3.1 is not uniform in this regime.  Any such route still needs an
   independent proof that reset/origin costs and all exceptional sectors are
   \(o(W)\).

4. **An incompatible integral allocation.**  Overlapping product
   decompositions may conceivably be used if every Boolean target is assigned
   once and the assigned pieces admit joint literal witnesses.  Merely
   choosing the cheapest overlapping cell target by target is not yet a
   decomposition or a word.

### Scope cautions

* The fixed-\(t\) theorem concerns separate payment between atomic parents.
  It does not sum \(g(P)\) lower bounds against a single global word; the
  endpoint-sharing theorem is the correct statement in that setting.
* The centered-leaf theorem requires the exact affine identity (4.2),
  saturated rank-preserving factors, and actual central-target coverage.
* The packet lower bounds in Section 6 concern concatenated independent
  packet words.  Cross-packet intervals escape them.
* Safe-Pin Factorization is an exact feasibility test for a *given* interval
  assignment.  It does not construct a near-width assignment.
* The hypothetical forests leading to (5.15) and (5.17) are unproved.  Their
  root counts cannot be inferred for an arbitrary forest.
* Nothing here proves MWB, any exact-wreath overload statement, or labelled
  common-owner synchronization.  The positive reduction stays integral by
  directly constructing literal Boolean OR words.

The final conclusion is therefore sharp for this lane:

\[
 \boxed{
 \begin{minipage}{0.88\linewidth}
 Every fixed-dimensional, separately paid product architecture is obstructed
 on a positive fraction of exact Boolean width.  The valid replacement is a
 non-product packet/MTF or global-braid theorem whose exact error is the
 state surplus plus the reset surplus in (0.5).  Proving that surplus to be
 \(o(W(k))\) remains open.
 \end{minipage}}
\]
