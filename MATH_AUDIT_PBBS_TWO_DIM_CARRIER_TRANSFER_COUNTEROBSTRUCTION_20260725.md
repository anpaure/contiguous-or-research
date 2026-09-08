# Audit of the two-dimensional carrier-transfer counter-obstruction

Date: 2026-07-25

Audited report:
PBBS_TWO_DIM_CARRIER_TRANSFER_COUNTEROBSTRUCTION_20260725.md.

Method: pure mathematics only; no computation, search, or solver.

## 0. Verdict

The fixed-prefix formula, the separator-spanning conditional mass, the
maximum-record one-pair matrix, its powers and resolvent, the physical
first-passage resets, and the source-\(e_0\)/all-ones-sink telescope are
correct.

One numerical correction is required:

\[
 \boxed{{2\over3}\le\Xi_{\ell,J}<{3\over2}}
\]

is the valid uniform bound.  The asserted upper bound \(4/3\) is false;
for \(\ell=1\) and \(J\to\infty\), \(\Xi_{\ell,J}\to3/2\).

The exact scope is:

* Sections 1--2 count a marked independent capped-array relaxation, not
  conditional probabilities of actual PBBS roots.
* Sections 3--4 are exact for the free one-seam corridor language and
  use the physical first-passage source and sink.
* They do not impose a second transported phase or the complete
  inter-time PBBS chronology.

Thus the report rigorously closes the one-phase block-index shortcut.
It does not obstruct a joint two-phase transfer theorem.

## 1. Fixed-prefix completion

For a legal prefix \(w\), put

\[
 y=\operatorname {net}(w),\qquad
 a=-\min H_w,\qquad p=a+y.
\]

The prefix contains \(a\) deterministic delimiters and
\(|w|-a\) bits belonging to Dyck blocks.  In the current block of cap
\(L+a\), the completion kernel from height \(p\) is

\[
 R_{L+a,p}(x)
 ={x^pQ_{L-y}(x^2)\over Q_{L+a+1}(x^2)}.
\]

The first \(a\) block partition functions telescope to

\[
 \prod_{i=1}^{a}C_{L+i}(z)
 ={Q_{L+1}(z)\over Q_{L+a+1}(z)}.
\]

Consequently the normalized prefix series is

\[
 x^{|w|+y}{Q_{L-y}(x^2)\over Q_{L+1}(x^2)}.
\]

At \(x=1/2\),

\[
 \boxed{
 \Pr(\mathscr D_L\text{ begins with }w)
 =2^{1-|w|}{L-y+1\over L+2}.}
\]

All exponents and indices in Theorem 1.1 pass.  The check \(w=0\) gives
probability one.

## 2. Separator-spanning extension and \(\Xi\)

For \(B=\operatorname {rev}E\), one has \(|B|=2\ell\) and net zero.
For

\[
 W_S=\operatorname {rev}(S)0,
\]

the word \(BW_S\) has length \(2\ell+|S|+1\) and net \(-1\).  Dividing
the two instances of Theorem 1.1 gives

\[
 \boxed{
 \Pr(W_S\mid B)
 =2^{-|S|-1}{\ell+2\over\ell+1}.}
\]

The cap legality is valid: while reading \(\operatorname {rev}(S)\),
ordinary height never exceeds its value at the end of \(B\), and the
height above a new record minimum is at most the new record depth, hence
below the increasing cap \(\ell+a\).

Summing marked choices of \(S\) of height at most \(J\) gives

\[
 \boxed{
 \Xi_{\ell,J}
 ={(\ell+2)(J+1)\over(\ell+1)(J+2)}.}
\]

Since

\[
 1<{\,\ell+2\over\ell+1}\le{3\over2},
\qquad
 {2\over3}\le{J+1\over J+2}<1,
\]

the corrected uniform bounds are

\[
 {2\over3}\le\Xi_{\ell,J}<{3\over2}.
\]

The limit \(\Xi_{\ell,J}\to1\) when both parameters tend to infinity is
correct.

Different \(S\)'s need not define disjoint prefix cylinders.  Therefore
\(\Xi\) is a marked transfer mass, as stated in the report, not a
probability of a disjoint union and not an actual-root count.

## 3. Maximum-record one-pair operator

Let

\[
 A=s-u,\qquad b=u-1,
\]

and let \(h\) be the maximum lower-loop depth.  A renewal pair has net
zero and minimum \(-h\), so an incoming record state \(p\) updates by

\[
 p'=\max(p,h),\qquad \Delta a=p'-p.
\]

The exact-height lower-loop series is

\[
 D_h=C_h-C_{h-1},
\]

and the upper loop contributes \(C_A\).  Hence

\[
 \mathsf R_{p,p}=zC_AC_p,
\]

\[
 \mathsf R_{p,q}
 =zC_A(C_q-C_{q-1})y^{q-p}\quad(q>p),
\]

with no entries below the diagonal.  Row summation telescopes to

\[
 zC_AC_b=\rho_{s,u}.
\]

For \(k\) pairs, the terminal record is the maximum of the incoming state
and the \(k\) loop depths.  Thus

\[
 (\mathsf R^k)_{p,q}
 =\begin{cases}
 \lambda_p^k,&q=p,\\
 (\lambda_q^k-\lambda_{q-1}^k)y^{q-p},&q>p,\\
 0,&q<p,
 \end{cases}
\qquad
 \lambda_q=zC_AC_q.
\]

Summing \(k\ge0\) proves (3.8).  At \(z=1/4\),

\[
 \lambda_q
 ={(A+1)(q+1)\over(A+2)(q+2)}.
\]

Direct subtraction gives

\[
 [(I-\mathsf R)^{-1}]_{p,p}
 ={(A+2)(p+2)\over A+p+3}\le p+2,
\]

\[
 [(I-\mathsf R)^{-1}]_{p,q}
 ={(A+2)(A+1)\over
 (A+q+3)(A+q+2)}\le1
\quad(q>p).
\]

Every formula in (3.4)--(3.9) passes.

At \(p=b\), the diagonal is

\[
 {(u+1)(s-u+2)\over s+2}
 =\Theta_\varepsilon(s)
\]

for a central seam.  The critical mean semilength of one pair is

\[
 1+{A\over3}+{b\over3}={s+2\over3}.
\]

Therefore \(k=\Theta(s)\) pairs have expected semilength
\(\Theta(s^2)\).  This verifies the stated scale in expectation.  A
coefficientwise lower bound on a fixed Gaussian window would additionally
require a variance or concentration estimate; it is not proved merely by
the mean identity.

## 4. Physical resets and the all-ones sink

If \(F_d\) is a downward top-to-bottom first passage of depth \(d\), then
every prefix of \(\operatorname {rev}F_d\) has net at least \(-d\), and
the full word ends at \(-d\).  Appending it to a record state \(p\le d\)
therefore lowers the global minimum by \(d-p\) and finishes at record
height zero.  Lemma 4.1 passes.

In reverse corridor order, the first word
\(\operatorname {rev}F_b\) resets every incoming \(p\le b\) to zero.
The renewal pairs can finish in any state \(q\le A+1\).  The terminal
word \(0\operatorname {rev}F_A\) has net and minimum \(-(A+1)\), so it
resets every such \(q\) to zero.  It need not be a strict first-passage
word after reversal; the reset conclusion only uses its minimum and
endpoint and remains correct.

Thus the physical source is \(e_0\), while the physical sink accepts
every intermediate state:

\[
 \text{source}=e_0,\qquad
 \text{sink}=\mathbf 1.
\]

For the reverse-oriented maximum-state operator,

\[
 \widehat G_{0,0}=1,
\]

\[
 \widehat G_{0,q}
 ={1\over1-\widehat\lambda_q}
 -{1\over1-\widehat\lambda_{q-1}},
\qquad
 \widehat\lambda_q=zC_bC_{q-1}.
\]

Therefore

\[
 \boxed{
 e_0^{\mathsf T}\widehat G\,\mathbf1
 =\sum_{q=0}^{A+1}\widehat G_{0,q}
 ={1\over1-zC_bC_A}
 ={1\over1-\rho_{s,u}}.}
\]

This independently verifies (5.13) in
CONSTANT_ONE_FOCUSED_FRONTIER_20260725.md.  There is no off-by-one term:
\(\widehat\lambda_0=0\) supplies the initial \(1\), and
\(\widehat\lambda_{A+1}=zC_bC_A\) is the final telescope.

The overlap bit shared with the preceding chamber is not counted twice:
it is the first bit of the physical reverse corridor and the final zero
of \(W_S\), with the concatenation cut placed at that bit.

## 5. Actual versus relaxed scope

The reversed dual array in Sections 1--2 uses independent Boltzmann
blocks with only the audited caps.  Actual PBBS roots inject into this
language, but arbitrary marked block choices need not satisfy all
transition identities of one root.  Hence Theorems 1.1--2.1 are exact
ambient transfer calculations.

The seam decomposition in Sections 3--4 is exact for every literal
top-to-bottom corridor, including corridors occurring in actual PBBS
roots.  Conversely it enumerates every free cap-valid corridor and does
not retain:

* a second transported phase;
* compatibility with the rest of the \(S/T\) staircase;
* quotient edge-disjointness.

The scalar restoration is therefore a genuine theorem about the
one-phase free-corridor factor.  It proves that marking one block record
cannot improve that factor.  It does not show that actual PBBS roots
realize a Catalan-dense scalar mode after all other chronology is imposed.

The correct boundary is exactly the report's final conclusion: any
further gain must be cross-phase, global-chronological, or packing-based.

## 6. Required correction

Replace (2.8) by

\[
 \boxed{{2\over3}\le\Xi_{\ell,J}<{3\over2}.}
\]

No other algebraic or index correction is required.

No coefficient-one conclusion follows from this audit.
