# Independent audit: adaptive PBBS phase fragmentation and zero-reset ledger

**Date:** 2026-08-07  
**Audited source:**
`MATH_THEOREM_PBBS_ADAPTIVE_PHASE_FRAGMENTATION_ZERO_RESET_LEDGER_20260807.md`  
**Source SHA-256 at audit:**
`d5aa9c43e729b43f3127d2f2911a73fad5cbbe6b906e04b14422a4f97c4c45a7`  
**Verdict:** **PASS** for the SCD fragmentation, asymptotic census, and
abstract endpoint-chain injection.  The theorem really removes the
positive theta reset deficit at zero abstract endpoint charge.  It does
not physicalize the rephased chart.  The exact physical residual condition
needs the envelope-aware and nonempty-letter clauses stated in Section 5
below.

## 1. Deep-segment length and eligible-bank census

The deep band is the inclusive rank interval

\[
 [d+1,t-1].
\]

An SCD chain starting at rank \(j>d+1\) reaches rank \(t-1\), and its
intersection with this band is

\[
 j,j+1,\ldots,t-1,
\]

of length

\[
 (t-1)-j+1=t-j.
\]

Thus for \(j_r=t-d-r\) the length is exactly \(d+r\).  There is no
off-by-one error.

For \(1\le r\le d-2\), the start ranks run from \(t-d-1\) down through
\(t-2d+2\).  Since the number of SCD chains starting at rank \(j\) is

\[
 c_j={n\choose j}-{n\choose j-1},
\]

the sum telescopes to

\[
 \sum_{r=1}^{d-2}c_{t-d-r}
 ={n\choose t-d-1}-{n\choose t-2d+1}.
\]

The two ranks are

\[
 m-2d-1,\qquad m-3d+1.
\]

For \(n=2m+1\),

\[
 \frac{{n\choose m-a}}{{n\choose m}}
 =\exp\!\left(-\frac{a^2}{m}+o(1)\right)
\]

uniformly for \(a=O(\sqrt m)\).  Since
\(d^2/n\to\pi/8\), hence \(d^2/m\to\pi/4\), the two terms converge to
\(e^{-\pi}\) and \(e^{-9\pi/4}\).  Therefore

\[
 \frac{E_{n,d}}W\longrightarrow
 e^{-\pi}-e^{-9\pi/4}=0.04236247\ldots .
\]

This is much larger than

\[
 \theta=4\sum_{a\ge1}e^{-4\pi a^2}
 =1.3949369\ldots\times10^{-5}.
\]

The strict comparison in Theorem 3.1 is valid.

## 2. One-rank phase-shift piece counts

Let \(L=ad+r\), \(0\le r<d\), and replace the top length-\(d\) piece by
one of length \(d-1\).  The remainder is

\[
 (a-1)d+(r+1).
\]

The exact changes are therefore

\[
\begin{array}{c|c}
r&(\Delta P,\Delta F)\\ \hline
0&(1,-1),\\
1\le r\le d-2&(0,-1),\\
r=d-1&(0,0).
\end{array}
\]

In particular \(\Delta(P+F)\) is respectively \(0,-1,0\).  Lemma 2.2
and the summation in Theorem 4.2 are exact.

For the selected two-piece bank, the replacement

\[
 (d,r)\rightsquigarrow(r+1,d-1)
\]

preserves total length and piece count and removes exactly one full piece.
Consequently choosing \(H=F-(g-P)\) eligible chains gives

\[
 P'=P,\qquad F'=g-P,\qquad P'+F'=g.
\]

No scalar endpoint deficit remains.

## 3. Balanced phase assignment

The phase neighborhoods are genuinely nested.  Phase \(a\) has offset

\[
 \delta_a=1+\left\lceil\frac{a(d-2)}Q\right\rceil
\]

and accepts exactly the remainder classes

\[
 r\le k_a:=\left\lceil\frac{a(d-2)}Q\right\rceil.
\]

The start-rank multiplicities \(w_r\) decrease eventually.  Hence their
first \(k_a\) classes contain at least \((a/Q)E_{n,d}\) chains.  The
prefix sums of the balanced quotas are
\(\lfloor aE_{n,d}/Q\rfloor\), so the nested-neighborhood Hall criterion
applies.  No divisibility hypothesis is hidden here.

## 4. Section 5 does not use a common maximum rank

Corollary 5.1 of
`MATH_THEOREM_PBBS_MERGED_LONG_REGION_SCD_CAPACITY_ESCAPE_20260806.md`
requires only:

1. a partition of the named deep targets into inclusion chains of length
   at most \(d\);
2. no more pieces than physical endpoint chains; and
3. that the unique piece on each SCD chain containing rank \(t-1\) be
   placed on suffix depths ending at \(d\).

Every other piece may occupy any consecutive block of suffix lengths.
The common-maximum-rank hypothesis belongs to the separate slabwise
antichain-top realization theorem; it is not used by the abstract
endpoint-chain injection.

Rephasing preserves the partition into saturated SCD subchains, preserves
the unique rank-\((t-1)\) piece on every relevant chain, and keeps every
piece length at most \(d\).  Therefore Section 5 is valid exactly as an
abstract named-target interval injection.  It makes no literal source-word
claim, and Section 7 correctly leaves that realization open.

## 5. Exact physical residual lemma

The source's condition (7.10) is the right coordinatewise cover-free
condition when there are no source-position envelopes.  For the full
literal statement, include the envelopes and source-letter nonemptiness as
follows.

Let \(V\) be the existing physical positions.  Let \(\mathcal I\) be the
family of every interval whose OR value is prescribed, including the
rephased lower cells and any fixed owner windows that must remain exact.
Write \(T(I)\subseteq[n]\) for the prescribed value of \(I\), and let
\(P_i\subseteq[n]\) be the allowed PBBS owner envelope at position \(i\).
For each coordinate \(x\), define

\[
 N_x=\bigcup_{I\in\mathcal I:\ x\notin T(I)}I,
 \qquad
 U_x=\{i\in V:x\in P_i\}\setminus N_x.
\]

Then there are **nonempty** letters \(A_i\subseteq P_i\) satisfying

\[
 \bigcup_{i\in I}A_i=T(I)
 \qquad(I\in\mathcal I)
\]

if and only if both conditions hold:

\[
 \boxed{I\cap U_x\ne\varnothing
 \quad(I\in\mathcal I,\ x\in T(I))}
 \tag{5.1}
\]

and

\[
 \boxed{P_i\cap\bigcap_{I\in\mathcal I:\ i\in I}T(I)
 \ne\varnothing
 \quad(i\in V).}
 \tag{5.2}
\]

The empty intersection in (5.2) is interpreted as the whole coordinate
set.

Necessity is immediate.  For sufficiency, for each positive pair
\((x,I)\) choose one point of \(I\cap U_x\) and place \(x\) there.  This
realizes every required positive incidence and no forbidden incidence.
Then, for each still-empty position \(i\), choose a coordinate from (5.2)
and add it at \(i\).  Such an addition is envelope-legal and cannot alter
any prescribed interval value.

Thus the exact unresolved physical theorem is not another scalar or SCD
packing statement.  It is to choose the endpoint injection and PBBS owner
envelopes so that (5.1)--(5.2) hold simultaneously, while also preserving
the independent residence, upper-spectrum, and compiler requirements.
Theorem 7.1 proves that the required injection cannot be obtained by simply
placing the two rephased companion pieces at adjacent endpoints, so a
global interlacing/common-history construction is genuinely necessary.

## 6. Final scope

The audited theorem proves, unconditionally:

\[
\boxed{
\text{adaptive SCD fragmentation removes the theta reset deficit with
zero abstract endpoint charge.}}
\]

It does **not** yet prove the adaptive-phase merged PBBS chart theorem, a
literal PBBS word, \(\nu(k)\le B(k)+O(1)\), or \(\nu(k)=B(k)\).
