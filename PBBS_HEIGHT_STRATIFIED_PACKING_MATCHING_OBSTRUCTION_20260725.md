# PBBS height-stratified quotient packing

Date: 2026-07-25

Status: corrected after the independent counteraudit of the false
\(d(D)=1\) converse.

## 0. Theorem

Put \(N=2r+1\) and \(B_r=\operatorname{Cat}_r\).  Let
\(\overline\nu_H(r)\) be the maximum number of pairwise
quotient-edge-disjoint nonwrapping residence intervals of residence at most
\(H\) on the long step-two PBBS quotient cycles.  There is an absolute
constant \(C\) such that, uniformly in \(H\),

\[
 \boxed{\overline\nu_H(r)\le C\frac{B_r}{\sqrt r}.} \tag{0.1}
\]

Consequently, for fixed \(A>0\) and \(H=\lceil A\sqrt r\rceil\), the deck
inequality gives

\[
 \boxed{\nu_H(P_r)=O_A(B_r\sqrt r).}               \tag{0.2}
\]

This removes the earlier \(\sqrt{\log r}\) loss in the quotient upper
bound.  It neither proves nor refutes \(RP_A\).

An earlier version of this note claimed a matching lower bound from all
primitive roots.  That claim is retracted: \(d(D)=1\) does not imply a
zero-winding return.  No part of the proof below uses that false converse.

## 1. Height is an exact quotient invariant

Mark the first up-step attaining the maximum of a Dyck word and write

\[
 D=P1Q.
\]

The one-step normalized PBBS map is

\[
 \phi D=\overline Q,0,\overline P.
\]

If \(h=\operatorname{ht}(D)\), a prefix of \(Q\), read after the marked
step, has increment between \(-h\) and zero.  Therefore the corresponding
prefix of \(\overline Q\) has height between zero and \(h\), and the whole
\(\overline Q\) ends at height \(h\).  After the displayed zero, every
prefix of \(\overline P\) has height \(h-1-H_P(t)\in[0,h-1]\).  Hence

\[
 \boxed{\operatorname{ht}(\phi D)=\operatorname{ht}(D).}      \tag{1.1}
\]

In particular \(\tau=\phi^2\) preserves height, so every directed edge in
one quotient \(\tau\)-cycle belongs to a single height stratum.

## 2. Height-local edge capacity

Let

\[
 b_{r,h}=\#\{D\in\mathcal D_r:\operatorname{ht}(D)=h\}.
\]

A residence-\(\ell\) return has omitted-label gap \(2\ell-1\).  The exact
peak-deletion height--gap theorem gives

\[
 2\ell-1\ge2h+1,
 \qquad\text{hence}\qquad \ell\ge h+1              \tag{2.1}
\]

when the initial root has height \(h\).  Its quotient trace, including the
insertion and removal transitions, contains \(\ell+1\ge h+2\) edges.

Split any family counted by \(\overline\nu_H(r)\) by initial height.  By
(1.1), every trace edge of a height-\(h\) member remains in the height-
\(h\) stratum.  Nonwrapping makes its trace edges distinct.  Therefore

\[
 (h+2)|\mathcal P_h|\le b_{r,h},
\]

and

\[
 \boxed{
 \overline\nu_H(r)
 \le\sum_{h=1}^{\min(r,H-1)}\frac{b_{r,h}}{h+2}.}   \tag{2.2}
\]

This is a trace-capacity inequality, not a pointwise fibre charge.  It
retains every Pascal slot and all overlap among long-cycle traces.

## 3. Reciprocal Dyck-height bound

Let \(F_r(t)\) count semilength-\(r\) Dyck paths of height at most \(t\).
The path-graph spectral formula is

\[
 F_r(t)=\frac2{t+2}\sum_{j=1}^{t+1}
 \sin^2\frac{\pi j}{t+2}
 \left(2\cos\frac{\pi j}{t+2}\right)^{2r}.         \tag{3.1}
\]

Pair \(j\) with \(t+2-j\), put \(q=\min(j,t+2-j)\), and use

\[
 \sin x\le x,
 \qquad \cos x\le e^{-x^2/2}\quad(0\le x\le\pi/2).
\]

For \(1\le t\le\sqrt r\),

\[
 F_r(t)
 \le \frac{C4^r}{t^3}e^{-c r/t^2}
 \le C B_r\left(\frac{\sqrt r}{t}\right)^3
             e^{-c r/t^2},                         \tag{3.2}
\]

where the last step is the elementary Wallis estimate
\(B_r\asymp4^r/r^{3/2}\).

Heights at least \(\sqrt r\) contribute at most \(B_r/\sqrt r\) to
\(\sum_hb_{r,h}/(h+2)\).  On the dyadic class

\[
 2^{-j-1}\sqrt r<h\le2^{-j}\sqrt r,
\]

equation (3.2) bounds the contribution by

\[
 \frac{CB_r}{\sqrt r},2^{4j}e^{-c4^j}.             \tag{3.3}
\]

The series in (3.3) is summable.  Thus

\[
 \boxed{
 \sum_{h=1}^r\frac{b_{r,h}}{h+2}
 \le C\frac{B_r}{\sqrt r}.}                        \tag{3.4}
\]

Combining (2.2) and (3.4) proves (0.1).

For \(H=O_A(\sqrt r)\), the quotient short-cycle edge count satisfies

\[
 Z_H\le(2H+2)N^{2H+2}=\exp(o(r)).
\]

The exact deck inequality

\[
 \nu_H(P_r)\le2N\overline\nu_H(r)+NZ_H
\]

then proves (0.2).

## 4. Audit boundary

1. Height invariance is exact under each one-step quotient move; it is not
   an endpoint-only estimate.
2. The denominator \(h+2\) includes both insertion and removal transition
   edges.
3. The charge is used only on nonwrapping long-cycle intervals.
4. No primitive-root, \(d=1\), sector-shift, or zero-winding converse is
   invoked.
5. The conclusion remains a factor \(\Theta(\sqrt r)\) above the quotient
   scale \(B_r/N\) required by \(RP_A\).

