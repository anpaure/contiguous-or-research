# Audit of the phase-capacity overload criterion

Date: 2026-07-26

Method: pure mathematics only.

## 0. Verdict

The hereditary Catalan plateau gives a valid no-go for cyclic rephasing of
the canonical MSW seed.  However, the proposed replacement target

\[
 \operatorname{OV}(F)=
 \max_{q\le p^{1/4}}\sum_{\widehat S}(M_q(\widehat S)-p)^+=0
\tag{0.1}
\]

is stronger than necessary.  Raw load above the \(p\) phase slots can be
paid for by the unavoidable global duplicate mass \(W-N_q\).

The sharp seed-level capacity obstruction is

\[
 \boxed{
 \operatorname{Exc}_q(F)=
 \left[
 \sum_{\widehat S}(M_q(\widehat S)-p)^+
 -(W-N_q)
 \right]_+.}
\tag{0.2}
\]

Any phase assignment has at least \(\operatorname{Exc}_q(F)\) holes at
depth \(q\).  Thus an MWB-scale construction needs the appropriate
weighted aggregate of \(\operatorname{Exc}_q\) to be \(o(W)\), not raw
overload identically zero.

This correction does not rescue canonical MSW: its hereditary plateau
overload is much larger than \(W-N_q\) throughout the range in which the
phase-capacity theorem is applied.

## 1. Exact counting identity

At depth \(q\), partition the actual targets into phase orbits
\(\widehat S\), each of size \(p\).  Let \(M_q(\widehat S)\) be the total
number of seed occurrences assigned to that orbit before phases are
chosen.  Row-by-row rephasing preserves \(M_q(\widehat S)\).

Whatever phases are chosen, orbit \(\widehat S\) can cover at most

\[
                         \min\{M_q(\widehat S),p\}
\tag{1.1}
\]

distinct targets.  Since the total number of occurrences is \(W\),

\[
 \begin{aligned}
 \sum_{\widehat S}\min\{M_q(\widehat S),p\}
 &=
 \sum_{\widehat S}M_q(\widehat S)
 -\sum_{\widehat S}(M_q(\widehat S)-p)^+\\
 &=W-\sum_{\widehat S}(M_q(\widehat S)-p)^+.
 \end{aligned}
\tag{1.2}
\]

There are \(N_q\) targets.  Therefore every phase assignment has at least

\[
 \begin{aligned}
 H_q'
 &\ge
 N_q-
 \left(
 W-\sum_{\widehat S}(M_q(\widehat S)-p)^+
 \right)\\
 &=
 \sum_{\widehat S}(M_q(\widehat S)-p)^+-(W-N_q)
 \end{aligned}
\tag{1.3}
\]

holes, with the right side replaced by its positive part.  This proves
(0.2).

Equation (1.3) is only a lower bound.  Even
\(\operatorname{Exc}_q(F)=0\) does not supply a legal phase assignment:
middle exactness and simultaneous near-surjectivity at all depths remain
a coupled Latin-type problem.

## 2. Why the MSW no-go is unchanged

For \(q\le p^{1/4}\),

\[
 W-N_q
 =
 O\!\left(\frac{q^2}{p}W\right)
 \le O\!\left(\frac W{\sqrt p}\right).
\tag{2.1}
\]

The hereditary embedded-excursion fibres in the canonical MSW seed give
raw phase overload of order at least

\[
                         \frac{W}{(\log p)^{3/2}}
\tag{2.2}
\]

on the relevant depths.  Since

\[
 \frac{W}{(\log p)^{3/2}}
 \gg
 \frac W{\sqrt p},
\tag{2.3}
\]

subtracting the unavoidable surplus in (0.2) changes no conclusion.
Canonical MSW followed by arbitrary cyclic row rephasing is still ruled
out.

## 3. The hash does not by itself solve the seed problem

A label which separates all subtree replacements of size \(r\) eliminates
that particular blind fibre.  It does not imply

\[
                         M_q(\widehat S)\le p
\tag{3.1}
\]

for every phase orbit: unrelated Dyck words or unrelated local changes
may still collide at the same target.  Nor does it prove that the twisted
rows retain exact middle ownership.

The correct constructive target has two logically separate parts.

1. Construct an exact middle seed \(F\) with
   \[
   \sum_q w_q\,\operatorname{Exc}_q(F)=o(W)
   \tag{3.2}
   \]
   for the weights required by the transfer theorem.
2. Prove a single legal phase assignment which nearly attains the orbit
   capacities simultaneously at all relevant depths.

Breaking excursion-blindness is a concrete way to attack the first part,
but it is not yet either part of the theorem.
