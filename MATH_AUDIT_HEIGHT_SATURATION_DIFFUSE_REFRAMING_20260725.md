# Audit of the canonical-frame diffuse-reframing theorem

Date: 2026-07-25

Audited source:
`MATH_ATTACK_HEIGHT_SATURATION_DIFFUSE_REFRAMING_20260725.md`.

Method: pure mathematics only.  No computation, finite search, solver, or
external input is used.

## 0. Verdict

The partial-frame atlas, its exact parity kernels, the Gaussian
coefficient bound, and the stable-window packing argument are correct.
After one endpoint-convention patch, the theorem

\[
 \#\{I:\ a\sqrt m\le h(I)\le A\sqrt m,
       \ R(I)\le s(I)/(4q)\}
 \le C_{a,A}2^{-q}{\operatorname {Cat}_m\over\sqrt m}
 \tag{0.1}
\]

holds with the stated quantifiers for every integer

\[
 1\le q\le \left\lfloor{\lceil a\sqrt m\rceil\over4}\right\rfloor .
\]

There is no use of the false implication
\(d(D)=1\Rightarrow\) zero-winding height return.  The proof applies to
every winding class because it uses only height invariance, the universal
height--gap inequality, literal canonical frames, and disjoint quotient
edges.

The one patch is genuinely needed for an exact floor statement.  The
source theorem assumes \(s(I)\le H_A\).  Its former definition

\[
 h_+(m)=\min\{\lfloor A\sqrt m\rfloor,H_A-1\}
\]

silently imposed the different convention \(s(I)+1\le H_A\) when
\(A\sqrt m\) is integral.  It has been replaced by
\(h_+(m)=\lfloor A\sqrt m\rfloor\), and the alternative convention is
now stated separately.  This changes no asymptotic conclusion.

## 1. Literal frame and canonicality audit

Let the first deepest spine of a height-\(h\) Dyck root be written

\[
 D=A_0,1A_1,1\cdots1A_{h-1},1
       0B_{h-1}0\cdots0B_1,0B_0.                 \tag{1.1}
\]

At depth \(k\), a forest before the selected spine child must have
height at most \(h-k-1\); equality \(h-k\) would produce an earlier
deepest leaf.  A forest after that child may have height \(h-k\), since a
later tie does not alter the first deepest spine.  These are exactly the
strict/weak conventions used in the source.

The literal block rotation is

\[
 \tau D=B_0,1A_0,1\cdots1A_{h-1},0
             0B_{h-1}0\cdots0B_1.                \tag{1.2}
\]

When the displayed spine remains canonical, this gives

\[
 A'_0=B_0,\qquad A'_i=A_{i-1}\ (1\le i<h),       \tag{1.3}
\]

\[
 B'_i=B_{i+1}\ (0\le i<h-1),\qquad
 B'_{h-1}=\varnothing .                           \tag{1.4}
\]

No forest is omitted incorrectly at the top: \(A_{h-1}\) is already
forced empty by its original strict height-zero cap.

### 1.1 The \(A\)-caps

After \(j\) preserved transitions, the original \(A_k\) is a pre-spine
forest at depth \(k+j\), as long as it remains in the frame.  Its strict
cap is

\[
 \operatorname {ht}(A_k)\le h-k-j-1.
\]

The strongest cap through rounds \(0,\ldots,q\) is therefore

\[
 \boxed{\operatorname {ht}(A_k)
 \le\max\{h-k-q-1,0\}.}                           \tag{1.5}
\]

The maximum with zero is correct rather than an illicit relaxation.  Once
the displayed right side would become negative, \(A_k\) was already
forced empty at the preceding top-level occurrence and then leaves the
frame.

### 1.2 The \(B\)-caps

For \(0\le j\le k\), the original \(B_k\) remains after the spine and
moves upward through the post-spine levels.  Its strongest cap in this
part is its initial cap \(h-k\).  For \(j>k\), it has crossed the root
seam and is a pre-spine forest at depth \(j-1-k\), hence has strict cap

\[
 h-(j-1-k)-1=h-j+k.
\]

The strongest cap through round \(q\) is exactly

\[
 \boxed{\operatorname {ht}(B_k)
 \le\min\{h-k,h-q+k\}
 =h-\max\{k,q-k\}.}                               \tag{1.6}
\]

Conversely, (1.5)--(1.6) keep every pre-spine forest strictly below the
displayed height and every post-spine forest weakly below it at every
round.  Induction using (1.3)--(1.4) therefore proves sufficiency, not
merely necessity.  This closes the possible canonicality gap.

Since the forests are uniquely delimited and independent after the spine
is fixed, their generating function is exactly

\[
 z^h\prod_{k=0}^{h-1}
 C_{\max\{h-k-q-1,0\}}(z)
 C_{h-\max\{k,q-k\}}(z).                          \tag{1.7}
\]

At \(q=0\), this becomes

\[
 {z^h\over F_h(z)F_{h+1}(z)},                    \tag{1.8}
\]

the standard exact generating function for height exactly \(h\).  This
is an independent endpoint check on all depth indices.

## 2. Exact telescoping and coefficientwise domination

Relaxing (1.6) to the original cap \(h-k\) enlarges each forest language
coefficientwise.  Since all coefficients are nonnegative,

\[
 \sum_{m\ge h}c_{m,h}^{(q)}z^m
 \preceq
 z^h
 \left(\prod_{j=1}^{h-q-1}C_j(z)\right)
 \left(\prod_{j=1}^{h}C_j(z)\right)
 ={z^h\over F_{h-q}(z)F_{h+1}(z)}.               \tag{2.1}
\]

Thus the majorant has the correct direction and no phase-dependent forest
has been counted with a smaller cap.

The unrelaxed product telescopes as follows.  If \(q=2r\), the \(A\)
factor is \(F_{h-2r}^{-1}\), while the \(B\) factor is

\[
 {1\over F_{h-r+1}}{F_{h-2r}\over F_{h-r}}.
\]

Hence

\[
 \boxed{
 \sum_{m\ge h}c_{m,h}^{(2r)}z^m
 ={z^h\over F_{h-r}(z)F_{h-r+1}(z)}.}            \tag{2.2}
\]

If \(q=2r+1\), the \(A\) factor is
\(F_{h-2r-1}^{-1}\), and the \(B\) factor is

\[
 {1\over F_{h-r}}{F_{h-2r-1}\over F_{h-r}}.
\]

Therefore

\[
 \boxed{
 \sum_{m\ge h}c_{m,h}^{(2r+1)}z^m
 ={z^h\over F_{h-r}(z)^2}.}                      \tag{2.3}
\]

The formulas also hold at the endpoint \(q=h\), using empty products and
\(F_0=F_1=1\).  At \(z=1/4\), division by (1.8) gives exactly

\[
 2^{-q}{(h+1)(h+2)\over
 (w+1)(w+2-\mathbf1_{\{q\text{ odd}\}})},
 \qquad w=h-\lfloor q/2\rfloor.                  \tag{2.4}
\]

Thus the factor \(2^{-q}\) is intrinsic to the exact atlas and is not an
artifact of (2.1).

## 3. Gaussian coefficient audit

Set

\[
 A_j(x)={x^j\over F_j(x^2)},\qquad
 G_j(x)={x^j\over F_{j+1}(x^2)}.
\]

For \(q=2r\), (2.2) becomes

\[
 x^qA_w(x)G_w(x),qquad w=h-r,                   \tag{3.1}
\]

and for \(q=2r+1\), (2.3) becomes

\[
 x^{q-1}A_w(x)^2.                                \tag{3.2}
\]

Consequently the relevant normalized convolution indices are exactly

\[
 2m-q\qquad\hbox{and}\qquad2m-q+1,             \tag{3.3}
\]

and the prefactors are \(4^m2^{-q}\) and
\(4^m2^{1-q}\), respectively.  This verifies both the parity shift and
the apparent factor two in the odd case.

When \(q\le h/2\) and \(a\sqrt m\le h\le A\sqrt m\), one has

\[
 {3h\over4}\le w\le h,
\]

and each index in (3.3) is \(\Theta_{a,A}(m)\).  In every two-factor
convolution one time is at least half the total.  The audited finite-strip
estimates give \(O(w^{-3})\) for that factor and \(O(w^{-1})\) for the
other factor's total mass.  Hence

\[
 c_{m,h}^{(q)}\le C_{a,A}4^m2^{-q}h^{-4}.         \tag{3.4}
\]

Finally,

\[
 \sum_{h\ge a\sqrt m}h^{-4}=O_a(m^{-3/2}),
 \qquad
 B_m\asymp4^m m^{-3/2},                           \tag{3.5}
\]

so the total number of Gaussian-band \(q\)-stable roots is at most
\(C_{a,A}2^{-q}B_m\).  All constants are uniform in the allowed \(q\).

## 4. Stable windows along a packed return trace

Let a return have step-two core roots

\[
 D_0,D_1,\ldots,D_{s-1}.
\]

A \(q\)-transition window can start at
\(0\le t\le s-q-1\), so there are exactly \(s-q\) candidates.  A frame
change at one of the \(s-1\) internal transitions belongs to at most
\(q\) such windows.  Therefore at least

\[
 s-q-qR(I)                                         \tag{4.1}
\]

starts are \(q\)-stable.  This is a union bound, so overlapping invalid
windows cannot make it false.  If \(q\le s/4\) and
\(R(I)\le s/(4q)\), (4.1) is at least \(s/2\).

The height--gap theorem gives \(s\ge h\) under the source's convention
that \(s\) is the number of deficit-carrying step-two core roots.  Thus a
Gaussian-band interval supplies at least \(a\sqrt m/2\) stable witnesses.
Quotient-edge-disjointness makes all the core roots belonging to different
selected intervals distinct.  Hence the witnesses are globally distinct,
and division of the root count by \(a\sqrt m/2\) proves (0.1).

This is the essential tensorization step: it is an incidence count on the
actual return traces, not multiplication of a marginal atlas density by a
separate interval-length probability.

## 5. Floors and exact residual boundary

Under the stated convention \(s(I)\le H_A\), the literal Gaussian band is

\[
 h_-(m)=\lceil a\sqrt m\rceil,\qquad
 h_+(m)=\lfloor A\sqrt m\rfloor.                 \tag{5.1}
\]

If instead the parameter \(H_A\) counts the final odd edge and the
hypothesis is \(s(I)+1\le H_A\), then and only then the upper endpoint is

\[
 \min\{\lfloor A\sqrt m\rfloor,H_A-1\}.          \tag{5.2}
\]

With (5.1), all floors in the theorem are exact.  The dyadic
small-height estimate is also correct and yields a coefficient
\(\eta(a)\downarrow0\).

The proved residual statement is therefore sharp in logical scope:

\[
 \boxed{
 \text{critical reciprocal-height saturation requires a positive
 density of canonical frame changes.}}
\]

The report does not show that the linearly reframing class is large, nor
that it is small.  Settling the corrected coefficient-one gate now
requires either a compatibility bound for a linear number of successive
frame changes or an actual PBBS family realizing critical packing with
that chronology.  The audit finds no hidden canonicality, coefficient,
or trace-incidence gap before this residual.
