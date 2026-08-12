# Independent audit of the mixed-seed first-eligible suffix Hall theorem

Date: 2026-07-26

Audited source:
`MATH_AUDIT_FIRST_ELIGIBLE_B4_MIXED_SEED_SUFFIX_HALL_20260726.md`.

Method: pure mathematics only.

## 0. Verdict

The suffix Hall theorem is mathematically valid after three substantive
clarifications and two scope edits. Its central advantage over the earlier
triangular-class obstruction is real: suffix conservation uses only physical
support localization. It is therefore insensitive to affine phases,
arbitrary cycle orders, and repeated visits to an active block, provided no
component transition imports a coordinate from the protected suffix.

The hypergeometric constants are correct. For a suffix occupying asymptotic
coordinate density \(1/4\), the middle variance is \(3m/32\), the signed
mean shift at depth \(A\sqrt m\) is \(A\sqrt m/4\), and hence the standardized
shift is \(A\sqrt{2/3}\).

The required corrections are:

1. The localization lemma needs an explicit predictability/nonanticipation
   hypothesis: the seed requested at the current block must be measurable
   with respect to the anchor and previously frozen scan data, and the anchor
   must not reveal the current scanned block. Packet stability proves that at
   most one seed can be accepted at a fresh block; by itself it does not give
   a binomial scan if a global rule is allowed to inspect future/current block
   states.
2. For a fractional component cover, (3.3) bounds the fractional singleton
   deficit
   \[
      D_q^\pm=\sum_T(1-\ell_q^\pm(T))_+,
   \]
   not the number of targets having strictly zero load. A fractional mixture
   can give every target a small positive load while retaining a linear
   coverage deficit.
3. In the enlarged owner-importing cross-seed menu, Proposition 3.1 must use
   the effective exceptional mass from (7.3), not the literal original-owner
   count \(U_m\). Section 7 notices this correctly; it should be propagated
   into the theorem and Proposition 3.1 rather than left as a later caveat.
4. Delete or qualify “for one whole seed choice per packet the sharper
   multiplier is at most three.” It is clear only for a menu of three global
   seed resolutions. For arbitrary mixed words in \(\{0,1,2\}^r\), the
   robust envelope is the displayed \(6^r/4^r=(3/2)^r\).
5. State explicitly that “arbitrary affine/revisiting order” means arbitrary
   physical components supported on the selected active coordinates. An
   affine or cross-packet trade which moves a suffix coordinate is outside the
   theorem and is exactly the stated escape.

With these edits the theorem is a robust fixed-atlas no-go, including the
completed 24-owner common carrier and fractional owner-balanced mixtures.

## 1. Predictable-seed lemma

The three supports

\[
 \mathcal A_c=\binom{[4]}2\setminus M_c
\]

have size four and pairwise intersection size two. If a stable decision rule
takes value \(c\) anywhere, it must take value \(c\) on all of
\(\mathcal A_c\). Two different seed values would therefore disagree on
\(\mathcal A_c\cap\mathcal A_d\), proving Lemma 1.1.

The final probabilistic conclusion requires the filtration statement

\[
 c_i\in\sigma(\text{anchor and blocks preceding }B_i),             \tag{A.1}
\]

before \(B_i\) is exposed. Then, conditionally on the past,

\[
 \Pr\{X|_{B_i}\in\mathcal A_{c_i}\mid\mathcal F_{i-1}\}=1/4.     \tag{A.2}
\]

The chain rule shows that the success indicators are iid
\(\operatorname{Bernoulli}(1/4)\), even though \(c_i\) may adapt to every
previous failure or success. This proves the asserted binomial law.

If an anchor is external or uses coordinates disjoint from the scanned
blocks, conditioning on it preserves (A.2). A rule allowed to inspect the
fresh block or future blocks is not covered without a separate conditional
probability proof.

## 2. Localization and the middle slice

There are \((3/8+o(1))m\) complete four-blocks before the terminal quarter.
Their success count has mean

\[
 (3/32+o(1))m.
\]

Since \(r=o(m)\), Chernoff gives \(e^{-cm}\) failure before the suffix.
The clean conditioning argument is unconditional:

\[
 \Pr\{\text{localization fails}\mid |X|=m\}
 \le
 \frac{e^{-cm}}{2^{-2m}\binom{2m}m}
 =O(\sqrt m)e^{-cm}=e^{-\Omega(m)}.                 \tag{A.3}
\]

Thus no separate claim that middle conditioning costs \(O(\sqrt m)\) after
fixing an arbitrary \(o(m)\)-coordinate anchor is needed. If one does first
condition on such an anchor, the worst correction can be \(e^{o(m)}\), still
harmless against \(e^{-cm}\), but not always literally \(O(\sqrt m)\).

Packet stability makes localization constant across every original packet.
For the enlarged cross-seed menu, its exceptional component-occurrence mass
is bounded by

\[
 U_{\mathrm{eff}}
 :=U_m^{\mathrm{leave}}+(3/2)^rU_m^{\mathrm{bad}}
 =e^{-\Omega(m)}W,                                  \tag{A.4}
\]

because \(r=o(m)\). This is the quantity which should occur in the final Hall
inequality.

## 3. Fractional capacity statement

Let \(y_C\ge0\) be component weights satisfying exact middle ownership

\[
 \sum_{C\ni X}y_C=1\qquad(X\text{ a middle owner}).                 \tag{A.5}
\]

For every normal component, suffix conservation implies that its weighted
occurrences in \(\mathcal Z_{q,a}^-\) are charged to starting owners with
\(|X\cap R|\le a\). Their total weight is at most \(B_a\). The upper sign is
charged to the complementary owner event. Exceptional associated components
contribute at most \(U_{\mathrm{eff}}\).

If \(\ell_q^\pm(T)\) is the fractional target load, then

\[
 \sum_{T\in\mathcal Z_{q,a}^\pm}\ell_q^\pm(T)
 \le B_a+U_{\mathrm{eff}}.                           \tag{A.6}
\]

Consequently

\[
 \boxed{
 D_q^\pm:=\sum_T(1-\ell_q^\pm(T))_+
 \ge |\mathcal Z_{q,a}^\pm|-B_a-U_{\mathrm{eff}}.}  \tag{A.7}
\]

For an integral exact factor, \(D_q^\pm\) is exactly the hole count, so the
same right side gives (3.3) for \(M_q^\pm\). With integral loads, every
target of load zero contributes one and every target of positive load
contributes zero.

Equation (A.7), rather than a statement about strictly positive fractional
support, is the correct fractional Hall theorem.

## 4. Hypergeometric constants

Put \(N=2m\), suffix size \(s=(1/2+o(1))m\), and
\(\gamma=s/N=1/4+o(1)\). For a middle \(m\)-set,

\[
 \operatorname{Var}|X\cap R|
 =m\gamma(1-\gamma)\frac{m}{2m-1}
 =(3/32+o(1))m.                                     \tag{A.8}
\]

For a lower \((m-q)\)-set with \(q=A\sqrt m+O(1)\), the mean is

\[
 (m-q)\gamma=s/2-(A/4+o(1))\sqrt m,                 \tag{A.9}
\]

and its variance is again \((3/32+o(1))m\). The upper mean is shifted by
the opposite amount. Therefore, for

\[
 a=s/2-x\sqrt{3m/32}+O(1),
\]

the limiting standardized displacement is

\[
 d-x,qquad d=\frac{A/4}{\sqrt{3/32}}=A\sqrt{2/3}.  \tag{A.10}
\]

Together with

\[
 \binom{2m}{m-q}/W\to e^{-A^2},                    \tag{A.11}
\]

this proves

\[
 \frac{B_a}{W}\to\Phi(-x),
 \qquad
 \frac{|\mathcal Z_{q,a}^\pm|}{W}
 \to e^{-A^2}\Phi(A\sqrt{2/3}-x).                  \tag{A.12}
\]

Mills' ratio makes the ratio
\(\Phi(A\sqrt{2/3}-x)/\Phi(-x)\) grow exponentially in \(x\), so some fixed
\(x=x_A\) gives the required positive gap. All constants in Section 4 are
correct.

## 5. Coverage of affine and revisiting orders

Lemma 2.2 requires neither a direction order nor packetwise injectivity. It
uses only

\[
 X|_R\text{ is constant on every normal component}.                 \tag{A.13}
\]

Hence the theorem covers all of the following without modification:

1. arbitrary affine/Hamming resolution classes inside a packet;
2. arbitrary cyclic or nonrecursive orders;
3. repeated visits to one selected four-block;
4. arbitrary local seed changes and orientations; and
5. fractional mixtures of those components preserving (A.5).

This remains true even if packetwise shadow injectivity fails. The theorem
does not cover an affine relabelling which sends an active direction into
\(R\), a cross-packet component whose physical support meets \(R\), or a
moving block atlas which changes the protected suffix during the chronology.

## 6. Clean theorem statement

### Theorem (predictable first-eligible suffix Hall cut)

Fix \(A>0\). Partition all but \(o(m)\) coordinates into one ordered atlas
of bounded blocks and reserve a terminal coordinate suffix
\(R\) with \(|R|=(1/2+o(1))m\). At each scan stage, let the requested local
\(B_4\) seed be measurable with respect to an anchor disjoint from the fresh
block and the previously frozen scan data. Assume:

1. the local rule is packet-stable and first-eligible;
2. the packet dimension satisfies \(h=2r\), \(r\to\infty\), \(r=o(m)\),
   and \(A\sqrt m\le\min\{H,r\}\);
3. all but \(e^{-\Omega(m)}W\) middle owner mass belongs to exact-owner
   components whose physical vertices vary only on their selected packet
   coordinates; and
4. the effective mass of components associated with scans reaching \(R\),
   including every owner-importing cross-seed alternative, is
   \(e^{-\Omega(m)}W\).

Put \(q=\lfloor A\sqrt m\rfloor\). Then there is
\(\kappa_A>0\), depending only on \(A\), such that every integral exact
middle factor obeys

\[
 M_q^-\ge(\kappa_A-o(1))W,
 \qquad
 M_q^+\ge(\kappa_A-o(1))W.                           \tag{A.14}
\]

Every fractional exact-owner component cover obeys the corresponding
singleton-deficit bounds

\[
 \sum_T(1-\ell_q^-(T))_+
 \ge(\kappa_A-o(1))W,
 \qquad
 \sum_T(1-\ell_q^+(T))_+
 \ge(\kappa_A-o(1))W.                               \tag{A.15}
\]

One may take

\[
 \kappa_A=
 e^{-A^2}\Phi(A\sqrt{2/3}-x_A)-\Phi(-x_A)>0         \tag{A.16}
\]

for any fixed \(x_A>A\sqrt{2/3}\) sufficiently large.

The conclusion permits arbitrary affine resolutions, component orders,
local orientations, repeated visits to active blocks, and global dependence
among component choices. It fails to apply only when the physical component
support itself transports coordinates into the protected suffix or when the
ambient ordered atlas is changed.
