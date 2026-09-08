# A positive-density uniform dense-top queue is incompatible with fixed additive overhead

**Date:** 2026-08-07  
**Method:** exact short-cell slack and rank-layer capacity  
**Status:** unconditional obstruction.  The weight-\(d+1\) queue is an
exact local common-history component, but copies of this one uniform
profile cannot realize a positive density of the complete top row in any
word of length \(B(k)+O(1)\).  Their lower-row waste is \(\Theta(dW)\),
whereas fixed additive overhead provides only \(O(W)\) waste capacity.
Thus the global construction must mix profiles, as predicted by the
triangular pull-clock circulation; it cannot be a factor of identical
uniform queues.

## 1. The global short-cell slack

Let

\[
 r=\left\lceil\frac k2\right\rceil,\qquad
 W={k\choose r},\qquad
 \Lambda=\sum_{s=1}^{r-1}{k\choose s},
\tag{1.1}
\]

and let \(d\) be the least integer satisfying

\[
 dW+{d+1\choose2}\ge\Lambda.
\tag{1.2}
\]

For a word of length \(W+e\), the number of intervals of length at most
\(e\) is

\[
 e(W+e)-{e\choose2}=eW+{e+1\choose2}.
\tag{1.3}
\]

All strict-lower targets must be witnessed by such short intervals.  Thus
the maximum number of short cells which may repeat a value or remain
unused is

\[
 \Sigma_e=eW+{e+1\choose2}-\Lambda.
\tag{1.4}
\]

### Lemma 1.1 (fixed additive slack is only \(O(W)\))

For every fixed \(C\ge0\), at length \(B(k)+C=W+d+C\),

\[
 \boxed{
 \Sigma_{d+C}<(C+1)W+(C+1)d+{C+1\choose2}.}
\tag{1.5}
\]

#### Proof

Minimality of \(d\) gives

\[
 (d-1)W+{d\choose2}<\Lambda.
\]

Subtract this strict lower bound from (1.4), with \(e=d+C\).  Since

\[
 {d+C+1\choose2}-{d\choose2}
 =(C+1)d+{C+1\choose2},
\]

the result is (1.5). \(\square\)

## 2. The uniform queue profile

Use the odd notation

\[
 k=2m+1,qquad q=d+1,qquad \rho=m-q.
\tag{2.1}
\]

At every endpoint of the weight-\(q\) block queue, the proper suffix cells
have the fixed ranks

\[
 r_j=m-(q-j)q,\qquad 1\le j\le q-1,
\tag{2.2}
\]

and the top cell has rank

\[
 r_{q-1}=m-q=\rho.
\tag{2.3}
\]

Suppose a global literal word has a set \(E\) of \(M\) endpoints at which
all the cells in (2.2) retain this queue profile.  They need not belong to
the same queue component.

### Lemma 2.1 (exact forced waste)

The cells ending at \(E\) force at least

\[
 \boxed{
 \mathcal W(M)
 \ge
 \sum_{j=1}^{q-2}
 \left(M-{k\choose r_j}\right)_+
 }
\tag{2.4}

repeated or unused strict-lower cells.

#### Proof

For fixed \(j\), the \(M\) suffix intervals are different physical cells,
but every one of their values belongs to the rank-\(r_j\) layer, which has
only \(\binom{k}{r_j}\) possible values.  At least the positive part in
(2.4) is therefore a duplicate or an unassigned cell.  Different \(j\)'s
are different interval lengths, hence different physical cells, so the
bounds add. \(\square\)

## 3. Complete top saturation has \(\Theta(dW)\) waste

Put

\[
 A={k\choose \rho}.
\tag{3.1}
\]

Using one uniform queue endpoint for every top target means \(M=A\).

### Theorem 3.1 (uniform dense-top fixed-additive no-go)

At the optimal deadline,

\[
 \boxed{
 \mathcal W(A)=\bigl(e^{-\pi/4}+o(1)\bigr)dW.
 }
\tag{3.2}

Consequently, for every fixed \(C\), no word of length \(B(k)+C\) can
use the uniform weight-\(d+1\) queue profile at all rank-\(\rho\) top
targets once \(k\) is sufficiently large.

More generally, the same conclusion holds if the queue profile occurs at
\(M\ge\alpha W\) endpoints for any fixed \(\alpha>0\).

#### Proof

The central local limit estimate and \(d^2/m\to\pi/4\) give

\[
 \frac AW\longrightarrow e^{-\pi/4}.
\tag{3.3}
\]

Write \(\ell=q-j\).  Then \(r_j=m-\ell q\), and for every fixed
\(\ell\),

\[
 \frac1W{k\choose m-\ell q}
 \longrightarrow e^{-\pi\ell^2/4}.
\tag{3.4}
\]

The sum of all layers with \(\ell\ge2\) is \(O(W)\).  One proof is to
use the adjacent-binomial ratio to dominate the tail uniformly by a
convergent Gaussian series; (3.4) then identifies its fixed initial
terms.  Hence Lemma 2.1 gives

\[
 \begin{aligned}
 \mathcal W(A)
 &\ge (q-2)A-
       \sum_{\ell=2}^{q-1}{k\choose m-\ell q}\\
 &=\bigl(e^{-\pi/4}+o(1)\bigr)dW.
 \end{aligned}
\tag{3.5}

The reverse inequality \(\mathcal W(A)\le(q-2)A\) gives (3.2).
For fixed \(C\), (1.5) is \(O(W)\), while (3.2) is
\(\Theta(dW)\) and \(d\to\infty\), a contradiction.

If \(M\ge\alpha W\), all but \(O(1)\) of the layers in (2.4) have size
\(o(W)\), so (2.4) is at least \((\alpha-o(1))dW\), giving the same
contradiction.  Every forced duplicate or unused cell counted in (2.4)
belongs to the global short-cell waste counted by \(\Sigma_{d+C}\), so
\(\mathcal W(M)\le\Sigma_{d+C}\) is the required interface to Lemma 1.1.
Finally, \(q^2=(d+1)^2\le m\) for all sufficiently large odd \(k\), since
\(d^2/m\to\pi/4<1\); hence the underlying uniform queue components are
indeed feasible in the range being ruled out. \(\square\)

## 4. Consequence for the construction programme

The local queue theorem remains valuable: it proves that literal common
history, flat owners, Johnson adjacency, both immediate palettes,
residence, and regeneration are mutually compatible.  The present theorem
shows exactly why that component cannot simply be copied across the whole
top layer.

The global chronology must vary its proper suffix ranks so that its
aggregate rank histogram follows the triangular lower-layer demand.  This
is precisely the role of the already-proved stationary pull-clock
circulation: its mixture of high positions and pull blocks has the correct
rank marginals.  The sharpened remaining problem is therefore:

> round the pull-clock mixture to one owner-once resident chronology while
> retaining the local top-row normal form and the protected upper/compiler
> interfaces.

The missing theorem is a mixed-profile integral rotor fusion, not a
uniform-component matching.
