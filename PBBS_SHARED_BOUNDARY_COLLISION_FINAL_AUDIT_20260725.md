# Final audit of the shared-boundary PBBS collision theorem

Date: 2026-07-25

Audited files:

- PBBS_SHARED_BOUNDARY_COLLISION_20260725.md;
- PBBS_FIRST_HIT_BOUNDARY_SHARPENING_20260725.md;
- MATH_ATTACK_QST_TWO_SEAM_TRANSFER_KERNEL_20260725.md,
  especially Proposition 4.2.

## 0. Verdict

The shared-boundary theorem passes after one local proof repair:

\[
 z_{r,s,2\ell}
 \le C4^r\frac{(\ell+2)^2}{s^6\sqrt{\ell+1}},
 \tag{0.1}
\]

and consequently, for fixed \(A\),

\[
 L\log r=o(r^{1/5})
 \quad\Longrightarrow\quad
 Z_r(A,L)=o_A(B_r/\sqrt r).
 \tag{0.2}
\]

At the quotient-packing level, the appended fixed-\(a\) split is also
valid and removes the logarithm:

\[
 L=L(r)=o(r^{1/5})
 \quad\Longrightarrow\quad
 |\mathcal P_r(A,L)|=o_A(B_r/\sqrt r)
 \tag{0.3}
\]

for every quotient-edge-disjoint family in the stated sector.

The record-minimum parsing, both parity cases of the truncated
telescope, the boundary collision estimate, the conditional
anti-concentration, and the final summation are valid.

The proof repair is in source (3.5).  The source originally bounded

\[
 \int|\varphi(t)|^2\,dt
\]

and then claimed an \(O(s^{-2})\) largest atom by Fourier inversion.
That inference would give only \(O(s^{-1})\).  The pointwise estimate
already proved in the source instead gives

\[
 \int|\varphi(t)|\,dt=O(s^{-2}),
\]

which does imply the claimed bound.  Source (3.5) has been corrected
accordingly.

The proposed extra first-hit factor \(1/(h+3)\) does **not** hold for
all genuine returns.  Proposition 4.2 gives a genuine return in which
\(0S_s0\) crosses a dual-block separator.  Thus the retraction in
PBBS_FIRST_HIT_BOUNDARY_SHARPENING_20260725.md is necessary.  The
all-start frontier remains (0.2), while the packing frontier is (0.3);
the proposed \(r^{1/4}\) window remains invalid.

The surviving carrier state is two-dimensional: it must retain both
the unmatched walk height and the current dual-block index.

## 1. Exact record-minimum parsing

Write

\[
 U=(0S_{s-1})\cdots(0S_1),\qquad
 V=(\overline T_{s-1}0)\cdots(\overline T_00),
\]

and let their common balanced boundary word \(E\) have length
\(2\ell\).  Reindex

\[
 D_i=S_{s-i},\qquad
 h_i=\min\{s-i,i+\ell\},\qquad1\le i\le s-1,
\]

and put

\[
 F_{s,\ell}(z)=\prod_{i=1}^{s-1}C_{h_i}(z).
 \tag{1.1}
\]

### Lemma 1.1

In a word

\[
 W=(0D_1)(0D_2)\cdots
\]

with all \(D_i\) Dyck, the delimiter zeroes are exactly the successive
strict record-minimum steps.  Hence the decomposition of every finite
prefix is unique.

#### Proof

After delimiter \(i\), the walk is at height \(-i\).  The following
Dyck block stays at or above \(-i\) and returns to \(-i\).  The next
delimiter is therefore the first step reaching \(-i-1\).  Induction
identifies every delimiter. \(\square\)

For a possible balanced prefix \(E\), let

\[
 a=-\min_{0\le t\le2\ell}H_E(t).
\]

Then \(1\le a\le\ell\), and uniquely

\[
 E=(0D_1)\cdots(0D_{a-1})0P,
 \tag{1.2}
\]

where \(P\) is a nonnegative prefix of \(D_a\) ending at height \(a\).
If \(3\ell\le s\), then for \(i\le a\),

\[
 h_i=i+\ell.
 \tag{1.3}
\]

For the dual side,

\[
 \operatorname{rev}V
 =(0\operatorname{rev}\overline T_0)
  (0\operatorname{rev}\overline T_1)\cdots,
\]

and every \(\operatorname{rev}\overline T_j\) is Dyck.  Its nontrivial
caps in this order are again \(h_1,\ldots,h_{s-1}\).  Thus the same
parsing applies to \(\operatorname{rev}E\).

A common word begins with the first delimiter of \(U\) and ends with
the final delimiter of \(V\).  Therefore it begins and ends with zero.
The exact number of common words is

\[
 M_\ell=\binom{2\ell-2}{\ell}.
 \tag{1.4}
\]

In particular \(M_1=0\): the sector \(\Lambda=2\) is empty.

## 2. Exact fixed-boundary series

Use

\[
 Q_0=Q_1=1,\qquad
 Q_{j+1}=Q_j-zQ_{j-1},\qquad
 C_j=\frac{Q_j}{Q_{j+1}}.
\]

### Lemma 2.1

For every admissible fixed common word \(E\), the forward-array series
weighted by total semilength is

\[
 \boxed{
 G_E(z)=z^\ell C_\ell(z)F_{s,\ell}(z).
 }
 \tag{2.1}
\]

It is independent of \(E\), and the reversed-dual series is identical.

#### Proof

Put \(x^2=z\).  The walk-completion series from height \(a\) to zero,
confined to \([0,H]\), is the path-resolvent entry

\[
 R_{H,a}(x)=\frac{x^aQ_{H-a}(z)}{Q_{H+1}(z)}.
 \tag{2.2}
\]

In (1.2), the already fixed non-delimiter bits have length
\(2\ell-a\).  The partial block has cap \(a+\ell\).  Hence

\[
 \begin{aligned}
 G_E(z)
 &=x^{2\ell-a}R_{a+\ell,a}(x)
   \prod_{i>a}C_{h_i}(z)\\
 &=z^\ell\frac{Q_\ell(z)}{Q_{\ell+a+1}(z)}
   \prod_{i>a}C_{h_i}(z).
 \end{aligned}
\]

Since

\[
 \prod_{i=1}^{a}C_{\ell+i}(z)
 =\frac{Q_{\ell+1}(z)}{Q_{\ell+a+1}(z)},
\]

this is (2.1).  Reversing and complementing the dual blocks preserves
their Dyck property and gives the same ordered caps. \(\square\)

At \(z=1/4\),

\[
 Q_j(1/4)=\frac{j+1}{2^j},\qquad
 C_j(1/4)=\frac{2(j+1)}{j+2}.
 \tag{2.3}
\]

Therefore every fixed admissible boundary has exact one-sided
probability

\[
 \Pr(E)
 =4^{-\ell}C_\ell(1/4)
 =2\frac{\ell+1}{\ell+2}4^{-\ell}.
 \tag{2.4}
\]

For two independent capped arrays, the exact common-word probability is

\[
 M_\ell16^{-\ell}C_\ell(1/4)^2
 =\Theta\!\left(\frac{4^{-\ell}}{\sqrt{\ell}}\right).
 \tag{2.5}
\]

This verifies and sharpens source Lemma 2.1 and Corollary 2.2.  The
source's first-return estimate is safe: it only discards a further
normalizing factor at most one.

## 3. Truncated telescope

For

\[
 P_{s,\ell,h}(z)
 =\prod_{j=1}^{s-h-1}
 C_{\min\{j,s-j+\ell\}}(z),
\]

put

\[
 M=s+\ell,\qquad a=\ell+h+1.
\]

When \(M=2p\), its cap list is

\[
 1,2,\ldots,p,p-1,\ldots,a,
\]

and therefore

\[
 P_{s,\ell,h}(z)=\frac{Q_a(z)}{Q_p(z)Q_{p+1}(z)}.
 \tag{3.1}
\]

When \(M=2p+1\), the central cap \(p\) is repeated, giving

\[
 P_{s,\ell,h}(z)=\frac{Q_a(z)}{Q_{p+1}(z)^2}.
 \tag{3.2}
\]

Thus, with no index loss,

\[
 \boxed{
 P_{s,\ell,h}(z)=\frac{Q_a(z)}{Q_u(z)Q_v(z)},
 \quad |u-v|\le1,\quad u+v=s+\ell+1.
 }
 \tag{3.3}
\]

This confirms both parity cases in source Lemma 3.1.

## 4. Conditional anti-concentration

### Lemma 4.1

Uniformly for \(0\le h\le\ell\le c s\), the normalized critical
coefficient distribution of \(P_{s,\ell,h}\) has largest atom
\(O(s^{-2})\).

#### Proof

For \(z=e^{it}/4\), set

\[
 x=\sqrt{1-e^{it}},\qquad\Re x\ge0.
\]

The closed form

\[
 Q_j(z)=
 \frac{(1+x)^{j+1}-(1-x)^{j+1}}{2^{j+1}x}
\]

gives

\[
 \frac{|Q_a(e^{it}/4)|}{Q_a(1/4)}
 \le e^{a|x|}.
 \tag{4.1}
\]

For

\[
 H_u(z)=\frac{z^u}{Q_u(z)Q_{u+1}(z)},
\]

factoring the two differences in the displayed formula for \(Q_j\)
gives

\[
 |\varphi_{H_u}(t)|
 \le
 \begin{cases}
 1,&u|x|\le1,\\
 C(u|x|)^2e^{-c_0u|x|},&u|x|\ge1.
 \end{cases}
 \tag{4.2}
\]

If \(v=u\), use

\[
 \frac{z^{u-1}}{Q_u(z)^2}
 =C_{u-1}(z)H_{u-1}(z),
\]

whose normalized \(C_{u-1}\) factor has modulus at most one.  If
\(v=u+1\), use \(H_u\) directly.  Since
\(a\le2\ell+1\), choose \(c\) so that the exponential in (4.1) is
absorbed by (4.2).  As \(|x|\asymp\sqrt{|t|}\), substitution
\(y=u\sqrt{|t|}\) yields

\[
 \int_{-\pi}^{\pi}
 |\varphi_{P_{s,\ell,h}}(t)|\,dt
 \le\frac C{u^2}
 \le\frac C{s^2}.
 \tag{4.3}
\]

Fourier inversion proves the result. \(\square\)

After fixing \(E\), the blocks

\[
 S_1,\ldots,S_{s-a-1}
\]

remain independent with a product of the form (3.3).  The partial-block
completion and the entire conditioned dual side are then convolved with
this untouched sum.  Convolution cannot enlarge a largest atom.  A
mixture over \(E\) preserves the same bound.  This validates source
Corollary 3.2.

## 5. Exact capped common-boundary kernel

Summing (2.1) over the \(M_\ell\) possible common words gives the exact
rank-marked capped kernel

\[
 \mathcal Z_{s,\ell}(z)
 =M_\ell z^{s+\ell}C_\ell(z)^2F_{s,\ell}(z)^2.
 \tag{5.1}
\]

Using (3.3) with \(h=0\),

\[
 F_{s,\ell}(z)
 =\frac{Q_{\ell+1}(z)}{Q_u(z)Q_v(z)},
\]

so the common word cancels the numerator exactly:

\[
 \boxed{
 \mathcal Z_{s,\ell}(z)
 =M_\ell z^{s+\ell}
 \frac{Q_\ell(z)^2}{Q_u(z)^2Q_v(z)^2}.
 }
 \tag{5.2}
\]

At the critical point,

\[
 \boxed{
 \mathcal Z_{s,\ell}(1/4)
 =M_\ell4^{1-\ell}
 \frac{(\ell+1)^2}{(u+1)^2(v+1)^2}
 =\Theta\!\left(\frac{(\ell+1)^{3/2}}{s^4}\right).
 }
 \tag{5.3}
\]

Thus equality of the literal boundary words cancels the exponential
\(4^\ell\) loss, but leaves a polynomial \(\ell^{3/2}\) factor in this
capped relaxation.  Combining (4.3) and (5.3) gives

\[
 z_{r,s,2\ell}
 \le C4^r\frac{(\ell+2)^{3/2}}{s^6},
 \tag{5.4}
\]

which is equivalent to (0.1) up to absolute constants.

## 6. Summation

Take

\[
 s_0=\left\lfloor
 \sqrt{\frac r{K\log r}}
 \right\rfloor.
\]

The audited low-height spectral estimate makes \(s<s_0\) contribute
\(o(B_r/\sqrt r)\).  Under

\[
 L\log r=o(r^{1/5}),
\]

one has \(L=o(s_0)\), so (5.4) applies throughout the remaining range.
Then

\[
 \begin{aligned}
 \sum_{\ell\le L}\sum_{s\ge s_0}z_{r,s,2\ell}
 &\le
 C4^r
 \left(\sum_{\ell\le L}(\ell+2)^{3/2}\right)
 \left(\sum_{s\ge s_0}s^{-6}\right)\\
 &\le
 C4^r
 \frac{L^{5/2}(\log r)^{5/2}}{r^{5/2}}
 =o(B_r/\sqrt r).
 \end{aligned}
 \tag{6.1}
\]

This proves (0.2).

## 7. Audit of the retracted first-hit sharpening

The conditional one-block calculation is algebraically sound: if one
really has

\[
 T_h=X1\overline S_s1Y
\]

and the displayed steps are the first hits of \(h+1,h+2\), then the
relevant first-passage critical mass is \(1/(h+3)\).  A literal product
must allocate the second displayed \(1\) only once, because its
complement is the first zero of \(E\); failing to do so double-counts
one bit, though only by an absolute factor.

With that bit allocated once, the exact fixed-\(E\) dual ratio in the
one-block subclass is

\[
 z^\ell
 \frac{Q_{\ell+h+2}(z)}
      {Q_{h+2}(z)Q_{\ell+1}(z)},
\]

whose critical value is

\[
 2\,4^{-\ell}
 \frac{\ell+h+3}{(\ell+2)(h+3)}.
 \tag{7.0}
\]

Thus the proposed order \(4^{-\ell}/(h+3)\) is correct under the
extra containment hypothesis, but it cannot be multiplied naively by
the old full-\(E\) probability.

The associated reflection estimate is also sound.  If \(d(E)\) is the
reverse record depth, then

\[
 \#\{E:d(E)=d\}
 =
 \binom{2\ell-2}{\ell+d-1}
 -
 \binom{2\ell-2}{\ell+d},
 \qquad1\le d\le\ell-1,
 \tag{7.1}
\]

and hence

\[
 \sum_E\frac1{d(E)+2}
 =\Theta(4^\ell/\ell).
 \tag{7.2}
\]

These calculations do not apply globally, because their geometric
hypothesis is false.

### Proposition 7.1: separator-spanning obstruction

There is a genuine first zero-winding return with

\[
 (m,s,\Lambda)=(8,4,4),
\]

\[
 T_0=T_1=S_3=S_4=1100,
\]

all other \(T_j,S_j\) empty, and

\[
 \mathcal A=000011000110,\qquad
 \mathcal C=011000110000,
\]

\[
 R_s=R_0=000,\qquad
 O=011000110.
 \tag{7.3}
\]

Here

\[
 E=0110,\qquad0S_40=011000.
\]

In the dual certificate, \(0S_40\) is the suffix \(011\) of
\(\overline T_1=0011\), followed by the separator zero and the first
two zeroes of \(\overline T_0=0011\).  It is not contained in either
dual block.  Since \(T_0,T_1\) have length four while
\(1\overline S_41\) has length six, neither can satisfy the proposed
one-block factorization.

The reverse record depth of \(E=0110\) correctly identifies the block
containing the start of \(E\); it does **not** imply that the preceding
word \(0S_s0\) began in that same block.  This is the precise invalid
inference in the retracted sharpening.

The displayed roots in Proposition 4.2 have proper accumulated
deficits \(1,2,3\), all strictly below their corresponding terminal
first-maximum positions, and final accumulated deficit \(8\).  Thus
the example is a genuine first zero-winding return, not merely a formal
word overlap.

## 8. Log-free packing refinement

Theorem 6.1 appended to the source is valid with the explicit
quantifiers now printed there.

Let \(L=L(r)=o(r^{1/5})\), fix \(A>0\), and let
\(\mathcal P_r\) be any quotient-edge-disjoint family in the sector

\[
 s\le A\sqrt r,\qquad0<\Lambda\le2L.
\]

Fix \(0<a<A\).  The low-duration subfamily is itself an
edge-disjoint packing, so the already proved sub-Gaussian height
packing theorem gives

\[
 \frac{\sqrt r}{B_r}|\mathcal P_r(s\le a\sqrt r)|
 \le
 \frac{\sqrt r}{B_r}\overline\nu_{\le a\sqrt r}.
 \tag{8.1}
\]

This input is already a quotient-packing theorem.  No physical deck
factor \(2r+1\) is missing, and short quotient cycles are included in
its statement.

For fixed \(a\), the condition \(L=o(r^{1/5})\) implies uniformly on
\(\ell\le L\) and \(s>a\sqrt r\) that

\[
 3\ell<s-2,\qquad\ell\le cs
\]

for all sufficiently large \(r\).  Hence the coefficient estimate
(5.4) is applicable throughout the high part.  Summing it gives

\[
 \begin{aligned}
 |\mathcal P_r(s>a\sqrt r)|
 &\le
 C4^r
 \left(\sum_{\ell\le L}
       \frac{(\ell+2)^2}{\sqrt{\ell+1}}\right)
 \left(\sum_{s>a\sqrt r}s^{-6}\right)\\
 &\le
 Ca^{-5}4^r\frac{L^{5/2}}{r^{5/2}}.
 \end{aligned}
 \tag{8.2}
\]

Since

\[
 B_r/\sqrt r\asymp4^r/r^2,
\]

the normalized high part is

\[
 O_a\!\left(\frac{L^{5/2}}{\sqrt r}\right)
 =
 O_a\!\left(\frac{L}{r^{1/5}}\right)^{5/2}
 =o(1).
 \tag{8.3}
\]

Therefore, for every fixed \(a\in(0,A)\),

\[
 \limsup_{r\to\infty}
 \frac{\sqrt r}{B_r}|\mathcal P_r|
 \le
 \limsup_{r\to\infty}
 \frac{\sqrt r}{B_r}\overline\nu_{\le a\sqrt r}.
\]

Only now is \(a\downarrow0\) taken.  The sub-Gaussian height theorem
makes the right side vanish.  No estimate uniform in \(a\), no
explicit diagonal \(a=a(r)\), and no hidden \(A\)-dependent
normalization is used.

Thus the correct two frontiers are:

\[
 \begin{array}{c|c}
 \text{quantity}&\text{proved shared-boundary range}\\ \hline
 \text{all starts}&
 \Lambda=o(r^{1/5}/\log r)\\
 \text{quotient-edge-disjoint packing}&
 \Lambda=o(r^{1/5}).
 \end{array}
 \tag{8.4}
\]

## 9. Exact remaining gate

The log-free packing theorem does not control zero-winding packing
beyond \(\Lambda=o(r^{1/5})\).  Any further physical-carrier argument
must allow \(0S_s0\) to cross one or more dual separators.  Its
synchronized state must therefore include

\[
 (\text{unmatched height},\ \text{current dual-block index}).
\]

Equivalently, the remaining object is a two-dimensional
height/block-index transfer automaton, not one first-passage factor
inside a predetermined \(T_h\).  A coefficientwise or packing-level
bound giving subcritical mass for that automaton would improve the
current frontier; no such bound is proved here.

The positive-winding interior cell also remains separate and open.
Neither the shared-boundary theorem nor this audit proves the full
coefficient-one conjecture.
