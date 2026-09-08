# Audit of the uniform dense-top queue fixed-additive waste no-go

**Date:** 2026-08-07  
**Audited file:**
*MATH_THEOREM_UNIFORM_DENSE_TOP_QUEUE_FIXED_ADDITIVE_WASTE_NOGO_20260807.md*  
**Verdict:** The fixed-additive contradiction is literally valid for all
sufficiently large **odd** dimensions \(k=2m+1\), provided the queue
profiles are actual suffix intervals in the universal word.  The local and
global depths agree without a parity or \(\pm1\) reindex, and the Gaussian
constants \(e^{-\pi/4}\) and \(e^{-\pi\ell^2/4}\) are correct.  Two
corrections are required:

1. Lemma 1.1 is missing an additive \(d\) in its displayed upper bound.
2. For \(M\ge\alpha W\), the proof gives a lower bound
   \((\alpha-o(1))dW\), not equality \((\alpha+o(1))dW\) unless
   \(M=(\alpha+o(1))W\).

Both corrections are asymptotically harmless.  The theorem does not, as
written, cover even \(k\), and it does not apply to abstract chart roles
which have not yet been materialized as physical intervals.

## 1. Exact parameter dictionary

The global monotone-deadline notation is

\[
 r=\left\lceil\frac{k}{2}\right\rceil,\qquad
 W=\binom{k}{r},\qquad
 d=d(k),
\tag{1.1}
\]

where

\[
 dW+\binom{d+1}{2}
 \ge
 \Lambda:=\sum_{s=1}^{r-1}\binom{k}{s}
\tag{1.2}
\]

and \(d\) is minimal.  For odd

\[
 k=2m+1
\tag{1.3}
\]

this becomes

\[
 r=m+1,\qquad
 W=\binom{2m+1}{m+1}=\binom{2m+1}{m},
\qquad
 \Lambda=\sum_{s=1}^{m}\binom{2m+1}{s}.
\tag{1.4}
\]

The local dense-top theorem uses the lower member \(m\) of the central
pair as its owner rank and the **same** integer \(d=d(k)\) as its suffix
depth:

\[
 q=d+1,\qquad
 \rho=m-q=m-d-1.
\tag{1.5}
\]

Thus the maps are

\[
\boxed{
 k_{\rm global}=n_{\rm local}=2m+1,\quad
 d_{\rm global}=d_{\rm local},\quad
 r_{\rm global}=m+1,\quad
 \operatorname{rank}(O)=m.
}
\tag{1.6}
\]

There is no missing \(\pm1\).  The apparent shift comes from using the two
equal central layers for different roles: the monotone deadline selects
rank \(m+1\), whereas the queue owner lies at rank \(m\).  The queue's
upper \(q1\) colour is at rank \(m+1\).

The top target has rank

\[
 \rho=m-d-1,
\tag{1.7}
\]

exactly the rank \(t-1\) in the odd merged-PBBS notation
\(t=m-d\).  Its proper suffix lengths are

\[
 1,\ldots,q-1=d.
\tag{1.8}
\]

At physical length

\[
 B(k)+C=W+d+C=W+e,
\tag{1.9}
\]

one has \(e=d+C\), so every queue suffix cell in (1.8) lies in the global
short band of lengths at most \(e\).

The explicit weight-\(q\) queue additionally needs

\[
 q^2=(d+1)^2\le m.
\tag{1.10}
\]

This holds for all sufficiently large odd parameters because

\[
 \frac{d^2}{m}\longrightarrow\frac{\pi}{4}<1.
\tag{1.11}
\]

Accordingly, the stated asymptotic theorem has a genuine local component
to which it applies.

Nothing in this dictionary proves the analogous statement for even
\(k=2m\).  An even dense-top profile and its rank histogram would have to
be stated separately.  The theorem's status should therefore say
“sufficiently large odd \(k\).”

## 2. Correction to the fixed-additive slack bound

For a word of length \(W+e\), the number of intervals of lengths at most
\(e\) is correctly

\[
 e(W+e)-\binom e2
 =eW+\binom{e+1}{2}.
\tag{2.1}
\]

The established monotone-deadline lemma puts every target of rank below
\(r\) in this short band.  Hence the exact surplus is

\[
 \Sigma_e=eW+\binom{e+1}{2}-\Lambda.
\tag{2.2}
\]

Minimality of \(d\) gives

\[
 (d-1)W+\binom d2<\Lambda.
\tag{2.3}
\]

Substituting \(e=d+C\) into (2.2) and using (2.3) yields

\[
\begin{aligned}
 \Sigma_{d+C}
 &<(C+1)W+
   \left[\binom{d+C+1}{2}-\binom d2\right]\\
 &=(C+1)W+(C+1)d+\binom{C+1}{2}.
\end{aligned}
\tag{2.4}
\]

The submitted display (1.5) has \(Cd\) rather than \((C+1)d\).  For
\(C=0\), minimality gives only

\[
 \Sigma_d<W+d,
\tag{2.5}
\]

not \(\Sigma_d<W\).  An integer version of the corrected bound is

\[
 \Sigma_{d+C}
 \le
 (C+1)W+(C+1)d+\binom{C+1}{2}-1.
\tag{2.6}
\]

For fixed \(C\), (2.4) is still \(O(W)\), since \(d=o(W)\).  Therefore
the missing \(d\) does not affect the final contradiction.

## 3. The physical-cell waste inequality is sound

Suppose \(E\) is a set of \(M\) actual endpoints of one literal word and
that, at every \(e\in E\), its suffix interval of length \(j\) has rank

\[
 r_j=m-(q-j)q
\qquad(1\le j\le q-1).
\tag{3.1}
\]

For a fixed \(j\le q-2\), these are \(M\) distinct physical intervals and
there are only

\[
 N_{r_j}=\binom{k}{r_j}
\tag{3.2}
\]

possible values of that rank.  After choosing at most one occurrence for
each distinct target value, at least

\[
 (M-N_{r_j})_+
\tag{3.3}
\]

cells remain duplicate or unassigned.  Different \(j\)'s mean different
interval lengths, hence different physical intervals.  Summing (3.3) is
therefore valid.

This forced waste really consumes the global slack \(\Sigma_e\).  Every
cell counted in (3.3):

* has interval length \(j\le d\le e\);
* has rank \(r_j<r=m+1\); and
* can witness only its one union value.

All \(\Lambda\) strict-lower targets already require one distinct short
interval each.  Thus every extra occurrence counted in (3.3) is among the
\(\Sigma_e\) short intervals left after those witnesses are selected.  In
particular,

\[
\boxed{
 \sum_{j=1}^{q-2}(M-N_{r_j})_+
 \le \Sigma_{d+C}
}
\tag{3.4}
\]

is necessary for any literal word of length \(B(k)+C\).

This step is architecture-free once the suffix cells are physical.  It
does **not** apply merely because an abstract merged chart has \(M\)
formal endpoint roles of the indicated ranks.  The roles must be realized
as the actual intervals ending at \(E\).  The audited theorem makes this
literal hypothesis in Section 2, so its contradiction is genuine rather
than a ledger-only statement.  Display (3.4) should nevertheless be added
to make the interface explicit.

## 4. Gaussian constants

For \(a\ge0\),

\[
 \frac{\binom{2m+1}{m-a}}{\binom{2m+1}{m}}
 =
 \prod_{u=0}^{a-1}\frac{m-u}{m+2+u}.
\tag{4.1}
\]

Uniformly for \(a=O(\sqrt m)\),

\[
 \log
 \frac{\binom{2m+1}{m-a}}{\binom{2m+1}{m}}
 =
 -\frac{a^2}{m}+o(1).
\tag{4.2}
\]

Taking \(a=q=d+1\) and using (1.11) gives

\[
 \frac{\binom{k}{\rho}}{W}
 \longrightarrow e^{-\pi/4}.
\tag{4.3}
\]

For each fixed \(\ell\),

\[
 \frac{\binom{k}{m-\ell q}}{W}
 \longrightarrow e^{-\pi\ell^2/4}.
\tag{4.4}
\]

Thus both displayed constants in the primary theorem are correct.  The
replacement of \(d\) by \(q=d+1\) changes only \(o(1)\) in the exponent.

The tail estimate used there is also valid.  Comparing the layers at
successive \(\ell\)'s by \(q\) adjacent-binomial ratios gives a bound of
the form

\[
 \frac{\binom{k}{m-\ell q}}{W}
 \le C_0e^{-c_0\ell^2}
\qquad(\ell\ge2)
\tag{4.5}
\]

with absolute positive constants for all sufficiently large parameters.
Hence

\[
 \sum_{\ell=2}^{q-1}\binom{k}{m-\ell q}=O(W).
\tag{4.6}
\]

No unrecorded factor of two occurs: here \(k=2m+1\), so the central
Gaussian exponent is \(-a^2/m\), and \(d^2/m\to\pi/4\).

## 5. Corrected waste conclusions

Let

\[
 A=\binom{k}{\rho}.
\tag{5.1}
\]

For \(M=A\), the exact forced-waste sum satisfies

\[
\begin{aligned}
 \sum_{j=1}^{q-2}(A-N_{r_j})_+
 &\ge
 (q-2)A-\sum_{\ell=2}^{q-1}\binom{k}{m-\ell q}\\
 &=\bigl(e^{-\pi/4}+o(1)\bigr)dW.
\end{aligned}
\tag{5.2}
\]

It is at most \((q-2)A\), so the asymptotic equality claimed in (3.2) is
correct if \(\mathcal W(A)\) denotes this forced waste among the displayed
queue cells.

Together, (2.4), (3.4), and (5.2) give the literal contradiction

\[
 \Theta(dW)\le O(W)
\tag{5.3}
\]

for every fixed \(C\), since \(d\to\infty\).

For the positive-density extension, if merely

\[
 M\ge\alpha W
\tag{5.4}
\]

for fixed \(\alpha>0\), the proof gives

\[
 \sum_{j=1}^{q-2}(M-N_{r_j})_+
 \ge(\alpha-o(1))dW.
\tag{5.5}
\]

This is enough for the same contradiction.  The stronger notation
\((\alpha+o(1))dW\) is justified only when

\[
 M=(\alpha+o(1))W.
\tag{5.6}
\]

For arbitrary \(M\ge\alpha W\), the leading coefficient follows \(M/W\),
not the chosen lower bound \(\alpha\).

## 6. Final scope

After the two corrections, the theorem proves:

> For every fixed \(C\) and all sufficiently large odd \(k=2m+1\), no
> universal literal word of length \(B(k)+C\) can contain the uniform
> weight-\((d(k)+1)\) queue suffix profile at a positive-density set of
> actual endpoints.

In particular it rules out assigning every rank-\((m-d-1)\) top target to
such an endpoint.  This is stronger than an obstruction to copying closed
queue rings: the endpoints may be distributed among arbitrary components.

It does not rule out:

* even dimensions without a separate parity-specific profile analysis;
* an abstract merged-region rank ledger before literal interval
  realization;
* a zero-density queue bank; or
* mixed profiles whose aggregate row histogram follows the triangular
  target demand.

The no-go therefore supports the mixed pull-clock conclusion, but only in
the stated odd, literal, fixed-additive scope.
