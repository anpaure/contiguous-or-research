# Audit: the flag-coherent SCD one-baseline reduction

Date: 2026-07-26

## Verdict

After one correction to the displayed shallow asymptotic, the conditional
reduction in
`MATH_THEOREM_FLAG_COHERENT_SCD_ONE_BASELINE_REDUCTION_20260726.md` is
valid.  In particular, no second middle-layer baseline is hidden in the
construction.  The only unproved mathematical input is the stated
bridge-one path-cover estimate

\[
 \min_{\mathcal D}\operatorname{fcpath}_{q_0,H}(\mathcal D)
 =o(W/H).
\]

The original relative formula

\[
 2\sum_{q<q_0}(N_q-N_{q_0})
 =\left(\frac43+o(1)\right)\frac{Wq_0^3}{m}
\]

silently required \(q_0\to\infty\), although the theorem allowed bounded
\(q_0\).  It has been replaced by the uniform formula

\[
 2\sum_{q=1}^{q_0-1}(N_q-N_{q_0})
 =\frac{W}{3m}(q_0-1)q_0(4q_0+1)
 +O\!\left(W\frac{q_0^5+q_0^3}{m^2}\right).
\]

This is \(o(W)\) under \(q_0=o(m^{1/3})\), including bounded \(q_0\),
and reduces to the former \(4/3\) leading form when \(q_0\to\infty\).
Thus the correction does not weaken the theorem or change the proposed
scale \(q_0=\lceil m^{1/4}\rceil\).

## 1. SCD census and shallow flags

Every symmetric chain in \(B_{2m}\) contains exactly one rank-\(m\)
member.  A chain reaches rank \(m-q\) (equivalently rank \(m+q\)) if and
only if its radius is at least \(q\).  Since an SCD partitions either
rank,

\[
 |\mathcal D_{\ge q}|=\binom{2m}{m-q}=N_q.
\]

Therefore \(|\Omega|=N_{q_0}\).  If \(q<q_0\), every chain in \(\Omega\)
contains its original two rank-\(m\pm q\) members, and distinct chains
cannot contain the same member.  Hence the two load vectors are
zero-one, each has support exactly \(N_{q_0}\), and

\[
 E_q^-=E_q^+=0,
 \qquad M_q^-=M_q^+=N_q-N_{q_0}.
\]

All quantifiers here are exact; no packet divisibility or rounding term is
present because every one of the \(N_{q_0}\) retained chains is used.

## 2. Outer collars preserve exactly the flags claimed

Let a retained chain have radius \(d<H\).  Choose \(H-d\) distinct
elements of \(C_{-d}\), order them, and delete them successively to extend
the lower flag to rank \(m-H\).  Independently choose and order \(H-d\)
elements outside \(C_d\), and add them successively to extend the upper
flag to rank \(m+H\).  The two choices are disjoint automatically, and the
result is a genuine complete radius-\(H\) state.  It preserves every
original member \(C_j\) for \(|j|\le d\).  If \(d\ge H\), restriction of
the original chain gives the unique required radius-\(H\) state.

Consequently, for fixed \(q_0\le q\le H\), every chain of radius at least
\(q\) supplies its actual SCD member at rank \(m-q\) and at rank \(m+q\).
Those chains are precisely \(\mathcal D_{\ge q}\), and the two provider
maps are bijections onto the two ranks.  Chains with radius below \(q\)
may contribute extra witnesses through their collars, but cannot remove a
designated witness.  Thus annular coverage is literal and simultaneous at
all depths \(q_0\le q\le H\).

## 3. Literal bridge-one compilation and the baseline

A hard start for a complete state

\[
 (L;z_1,\ldots,z_{2H};R)
\]

uses the \(2H+1\) letters

\[
 \{z_{2H}\},\ldots,\{z_1\},L.
\]

The exact bridge-one common-arrival relation permits the next complete
state to be exposed by appending one new letter.  Hence a directed path on
\(s\) states costs \(s+2H\), and a cover by \(p\) paths costs

\[
 N_{q_0}+2Hp.
\]

The retained original middle members are distinct.  Appending the other
\(W-N_{q_0}\) middle masks as literal singleton letters raises the cost to
exactly \(W+2Hp\).  Appending each missing shallow signed target adds

\[
 2\sum_{q=1}^{q_0-1}(N_q-N_{q_0})
\]

letters.  Concatenation cannot destroy an internal contiguous-union
witness; intervals crossing a seam only create additional witnesses.
This proves the exact one-baseline ledger.

For fixed decorated states, the path-cover number is equivalently

\[
 \min_{\prec}\operatorname{def}(G_\prec),
\]

where \(G_\prec\) is the bipartite forward bridge graph.  A forward
matching is a directed linear forest, while every directed path cover has
a total order extending all of its path orders.  Thus no acyclicity
assumption is missing from the Hall formulation.

## 4. Shallow asymptotic

For \(q\le q_0=o(\sqrt m)\), the exact product formula

\[
 \frac{N_q}{W}
 =\prod_{i=1}^q\frac{m-i+1}{m+i}
\]

gives uniformly

\[
 \frac{N_q}{W}
 =1-\frac{q^2}{m}
 +O\!\left(\frac{q_0^4+q_0^2}{m^2}\right).
\]

Summing the error over \(q<q_0\) and using

\[
 \sum_{q=1}^{q_0-1}(q_0^2-q^2)
 =\frac{(q_0-1)q_0(4q_0+1)}6
\]

proves the corrected uniform expansion in the verdict.  Under
\(q_0=o(m^{1/3})\), both the principal term and the error are \(o(W)\).

## 5. Exterior and parity interface

The central compiler covers every rank from \(m-H\) through \(m+H\),
inclusive.  The audited product-SCD word with parameter
\(r=m-H-1\) covers every nonempty target of rank at most \(m-H-1\) or at
least \(m+H+1\).  Thus there is neither a gap nor an overlap charge at the
interface.  Its length is \(o(W)\) exactly in the regime
\(H/\sqrt m\to\infty\); the theorem assumes this regime.  Appending the
word preserves all previous witnesses.

This proves

\[
 \nu(2m)\le \binom{2m}{m}+o\!\binom{2m}{m}
\]

conditional on the path-cover gate.  The standard one-coordinate trimmed
lift has twice the length and covers all nonempty targets in dimension
\(2m+1\); since

\[
 \binom{2m+1}{m}\sim2\binom{2m}{m},
\]

the same coefficient follows in odd dimensions.  The empty target, if it
is not represented by the empty interval under the standing convention,
costs only one additive entry and has no asymptotic effect.

## 6. Certified boundary

The following are certified:

1. the chain count \(|\Omega|=N_{q_0}\);
2. exact zero shallow collision excess and the exact shallow hole count;
3. simultaneous annular coverage by the same retained states;
4. existence of every claimed collar extension while preserving all
   original flags used by the proof;
5. exact literal length \(W+2Hp+2\sum_{q<q_0}(N_q-N_{q_0})\);
6. the corrected shallow asymptotic and its quantifiers; and
7. the product-SCD and even-to-odd interfaces.

What remains unproved is exactly the existence of a full SCD and one
simultaneous collar choice whose bridge-one path-cover number is
\(o(W/H)\).  The reduction does not turn independent depthwise matchings
into such a history, and makes no claim that the open gate is routine.
