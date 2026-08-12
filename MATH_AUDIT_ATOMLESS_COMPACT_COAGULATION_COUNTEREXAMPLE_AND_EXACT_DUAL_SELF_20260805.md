# Self-audit: compact coagulation counterexample and exact dual

**Date:** 2026-08-05  
**Method:** independent line-by-line mathematical replay; no computation or
search  
**Audited file:** MATH_THEOREM_ATOMLESS_COMPACT_COAGULATION_COUNTEREXAMPLE_AND_EXACT_DUAL_20260805.md  
**Verdict:** **PASS**, with the scope restrictions in Section 6 below.

## 1. Counterexample arithmetic

The job density \(50\mathbf1_{[1,51/50]}\) has mass one and mean
\[
 {1+51/50\over2}={101\over100}.
\]

The functions \(19y^{18}\) and \(19(1-y)^{18}\) are probability densities
with means \(19/20\) and \(1/20\).  Hence the socket density
\[
 g(y)={1\over10}+{43\over45}19y^{18}
                 +{47\over45}19(1-y)^{18}
\]
has mass
\[
 {1\over10}+{90\over45}={21\over10}
\]
and work
\[
 {1\over20}+{43\cdot19+47\over45\cdot20}
 ={45+817+47\over900}
 ={909\over900}={101\over100}.
\]
It is continuous and at least \(1/10\) on \((0,1)\).

For \(t=51/100\), one has \(t^{19}<10^{-3}\).  Therefore
\[
 \nu((t,1))
 >{49\over1000}+{43\over45}{999\over1000}
 ={45162\over45000}>1.
\]
Two values larger than \(t\) sum to more than \(51/50\), the largest job.
Every job consequently supplies at most one such occurrence, contradicting
the displayed tail mass.  This validates the no-go independently of any
duality theorem.

The count ratio is \(21/10\), so the example really lies strictly between
two and three sockets per job.  It is stronger than the elementary
count-shortage counterexample.

The continuous separator also checks.  Choose \(s>51/100\) while the upper
tail still has mass greater than one, and a continuous \(w\in[0,1]\)
supported above \(s\) with \(\int w\,d\nu>1\).  For
\[
 C\ge\max\{s^{-1},(2s-51/50)^{-1}\},
 \qquad a(y)=Cy-w(y),
\]
the price is nonnegative.  A cover using at most one positive-\(w\) piece
costs at least \(Cx-1\).  If it uses \(k\ge2\), then its cost relative to
\(Cx-1\) is at least
\[
 C(ks-51/50)-k+1.
\]
This is nonnegative at \(k=2\) and nondecreasing thereafter.  Thus
\(a^\star(x)\ge Cx-1\), while equal work and \(\int w\,d\nu>1\) make the
right side of the price inequality strictly smaller.  The separator is
therefore genuinely continuous and belongs to the theorem's stated dual
class.

## 2. Universal count and tail cuts

If \(n\) pieces are all strictly below \(b\), their sum is strictly below
\(nb\).  Thus \(n>x/b\), whose least integer solution is
\(\lfloor x/b\rfloor+1\).

If \(k\) pieces are strictly above \(t\), then exact summation gives
\(kt<x\).  The largest integer satisfying this strict inequality is
\(\lceil x/t\rceil-1\), including the case \(x/t\in\mathbb Z\).
Integration proves both stated cuts.

## 3. Generic covering-price iff theorem

The proof is the standard closed upward-cone argument, and all required
compactness rows are present:

1. narrow convergence of the available finite measures gives bounded total
   mass and uniform tightness in the Polish interval \((0,b)\);
2. domination of the used marginal prevents endpoint escape;
3. bounded expected configuration size gives tightness across the disjoint
   arity components;
4. the cover inequality is closed;
5. nonnegative compactly supported tests and Portmanteau retain domination
   of the limiting used marginal.

The available-measure set is therefore convex, closed, and upward.  A
separating continuous functional must be represented by a nonnegative
bounded continuous price: a negative value at any point would be contradicted
by adding arbitrarily much available mass there.

Pointwise minimization is legitimate.  On
\([1/M,b-1/M]\), redundant-piece deletion bounds arity uniformly, and compact
measurable selection applies.  The restricted costs decrease to the
unrestricted covering closure.  Repetition of a fixed interior socket gives
a common bounded-cost cover because the job support is compact.

At equal work, the sum of cover overshoot and unused socket work is zero.
Both are nonnegative.  Hence covers are exact and every available socket is
used.  Finite socket mass makes configuration arity finite almost surely.

Thus the price family is genuinely necessary and sufficient, not merely a
necessary relaxation.

## 4. Interval-flow equivalence

Ordering the pieces of each job partitions \([0,x)\), giving occupation
\(\mu((t,\infty))\).  Conversely the distributional start/end identity is
\[
 \sigma_1-\sigma_0=\mu-\mu([b,L])\delta_0.
\]
Directed path decomposition is valid because all edges have positive length.
An unused circulation would have constant integrable occupation density and
therefore zero occupation and zero edge mass.  The total edge intensity is
\(\nu(0,b)<\infty\), so infinite paths have zero source-path measure.

For the product ansatz \(\eta=q\otimes\nu\), Fubini gives occupation
\[
 \int_{[0,t]}\nu((t-a,b))\,dq(a).
\]
Therefore the stated renewal identity is a valid sufficient condition.  It
is not asserted to be necessary.

## 5. Compact gapped signed dual

If every socket is at least \(q>0\) and every job is at most \(\max J\),
arity is at most \(\lfloor\max J/q\rfloor\).  The exact configuration space
is consequently a finite union of compact spaces.  Measures with a fixed
job marginal form a compact convex set, and the occurrence-marginal image is
compact convex.  Ordinary separation gives exactly the signed price family
in the theorem.  The assumption that the relevant job fibres are nonempty is
explicit and necessary.

## 6. Scope

The theorem does not show that the Rayleigh compact pair violates a price
cut.  The counterexample only proves that its qualitative rows cannot imply
feasibility generically.  The Rayleigh-specific task remains either:

* prove every covering-price inequality for its actual densities; or
* construct its interval flow/coagulation directly.

The finite-arity theorem applies after the bottom-primary reduction only on
the representable job support.  It removes analytic closedness and
unbounded-arity issues, but it does not make its signed inequalities
automatic.

For sockets in the open interval \((q,b)\), the exact representable set is
\(\bigcup_{n\ge1}(nq,nb)\): the forward inclusion is immediate, and the
reverse uses \(n\) equal pieces.  When \(q<b/2\) these intervals overlap
from the first one onward.  At equality they miss the isolated value \(b\);
for \(q>b/2\) there are finitely many further gaps before eventual overlap.
Thus the source correctly warns that the bottom-primary coupling itself must
be chosen to avoid the nonrepresentable remainder set.
