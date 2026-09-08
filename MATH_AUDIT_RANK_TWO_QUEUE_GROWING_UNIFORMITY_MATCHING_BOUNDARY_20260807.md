# The rank-two queue crosses the Grable hypothesis but not the fixed-density conclusion

**Date:** 2026-08-07  
**Status:** proof-safe audit of the owner-copy matching scale.  The owner-only
rank-two queue satisfies the familiar growing-uniformity codegree hypothesis,
but the corresponding published leftover exponent does not imply a fixed
positive owner density when the queue length grows.  Adding all lower target
roles at once destroys even that hypothesis.  A sequential coupling theorem
is still required.

## 1. Owner-copy hypergraph of the rank-two queue

Use

\[
 n=2m+1,\qquad p=d+1,\qquad c=m-2p,
 \qquad \ell=3p .
\tag{1.1}
\]

The permanent core has size \(c\), the \(p\) phase supports are disjoint
triples, and one queue owner contains two points from each phase support.
Thus every abstract owner has rank

\[
                         c+2p=m,
\tag{1.2}
\]

and a complete queue contains \(\ell=3p\) owners.

Let \(\mathcal H_{\rm q}\) be the parameterized copy hypergraph on the
rank-\(m\) layer: every injection of the abstract core and the \(3p\) phase
labels into \([n]\) gives one \(\ell\)-edge consisting of the queue owners.
As in the moving-carousel incidence calculation, it is regular of degree

\[
 \Delta=\ell m!(m+1)_p.
\tag{1.3}
\]

For \(1\le q\le p\), let \(a_q\) be the number of ordered abstract owner
pairs at Johnson distance \(q\).  Two rank-\(m\) vertices \(X,Y\) at distance
\(q\) have codegree

\[
 \Delta(X,Y)
 =a_q(m-q)!(q!)^2(m+1-q)_{p-q},
\tag{1.4}
\]

and hence

\[
 \frac{\Delta(X,Y)}{\Delta}
 =\frac{a_q/\ell}{\binom mq\binom{m+1}q}.
\tag{1.5}
\]

### Lemma 1.1 (exact maximum pair-codegree)

For \(p\ge3\), the only Johnson-distance-one pairs of abstract queue owners
are consecutive owners of the queue cycle.  Consequently

\[
 a_1=2\ell
 \quad\hbox{and}\quad
 \boxed{\frac{\Delta_2}{\Delta}=\frac2{m(m+1)}}
\tag{1.6}
\]

for all sufficiently large parameters.

#### Proof

At time \(i=up+a\), with \(0\le a<p\), the omission state of the \(p\)
phase triples is

\[
 (\underbrace{u,\ldots,u}_{a+1},
  \underbrace{u-1,\ldots,u-1}_{p-a-1})\in(\mathbb Z_3)^p.
\tag{1.7}
\]

The Johnson distance of two owners is the Hamming distance of their omission
states.  In a forward displacement \(0<t<3p\), every phase advances either
\(\lfloor t/p\rfloor\) or \(\lceil t/p\rceil\) times.  The Hamming distance
is one only for \(t=1\) or \(t=3p-1\).  Thus \(a_1=2\ell\).  For \(q\ge2\),
use \(a_q/\ell\le\ell-1\) in (1.5).  Since \(\ell=O(\sqrt m)\), those terms
are \(O(m^{-7/2})\), whereas the \(q=1\) term is \(2/[m(m+1)]\).  This proves
(1.6). \(\square\)

Uniform parallel multiplicities in the parameterized model may be quotiented
out.  They change neither regularity nor any ratio in (1.5)--(1.6).

## 2. The growing-uniformity parameter tends to zero

Let

\[
                         N=\binom{2m+1}{m}.
\tag{2.1}
\]

At the optimal deadline,

\[
 d^2/m\longrightarrow\pi/4,
 \qquad \ell=3(d+1),
 \qquad \log N=(2\log2+o(1))m.
\tag{2.2}
\]

The standard growing-uniformity parameter is therefore

\[
 x_m:=\ell\log N\,\frac{\Delta_2}{\Delta}
 =\frac{\ell\log N\,2}{m(m+1)}
 \sim\frac{12(\log2)d}{m}
 \sim\frac{9\pi\log2}{\ell}.
\tag{2.3}
\]

In particular,

\[
                         x_m=\Theta(\ell^{-1})=o(1).
\tag{2.4}
\]

Thus the owner-only queue really does satisfy the hypothesis scale

\[
                         \Delta_2=o\!\left(
                         \frac{\Delta}{\ell\log N}\right).
\tag{2.5}

## 3. Why this is not a near-perfect matching theorem here

The quantitative Grable/Kostochka--Rödl leftover bound at this scale has the
form

\[
 U(\mathcal H)
 \le N\left(
       \frac{kC\log N}{D}
      \right)^{1/(2k-1+o(1))}
\tag{3.1}

for a \(k\)-uniform, \(D\)-regular hypergraph of maximum codegree \(C\).
Even granting uniform applicability of (3.1) along the present growing
sequence, substituting \(k=\ell\) and (2.3) gives

\[
 x_m^{1/(2\ell-1+o(1))}
 =\exp\left(-\frac{\log\ell+O(1)}{2\ell}
             +o(\ell^{-1})\right)
 =1-\Theta\!\left(\frac{\log\ell}{\ell}\right).
\tag{3.2}

Under that hypothetical uniform reading, the displayed upper bound on the
leftover differs from \(N\) only on the scale

\[
                         \Theta\!\left(
                         \frac{\log\ell}{\ell}
                         \right)N,
\tag{3.3}

which tends to zero as a fraction of \(N\).  Thus even this formal
substitution does not imply coverage of \(\theta N\) for any fixed
\(\theta>0\), and a fortiori does not imply a near-perfect owner packing.
The published formulation has fixed-uniformity quantifiers, so (3.3) is a
scale diagnostic, not an unconditional growing-\(\ell\) consequence.  The
implication from (2.5) to a near-perfect matching is valid when the
uniformity is fixed; it is not a valid diagonal inference when
\(\ell\to\infty\).  To make (3.1) itself yield \(o(N)\) leftover with
growing \(\ell\), one would need

\[
                         -\log x_m=\omega(\ell),
\tag{3.4}

whereas here \(-\log x_m=\Theta(\log\ell)\).

## 4. Monolithic inclusion of all lower roles fails earlier

A complete rank-two ring has \(d\) marked lower targets at each of its
\(\ell=3p\) endpoints.  Thus the monolithic owner-plus-target packet has
uniformity at least

\[
                         k_{\rm full}=3pd=\Theta(m).
\tag{4.1}

Its vertex set contains the middle owner shore, so the owner-owner pair from
(1.6) remains a valid codegree witness relative to the natural owner-shore
degree.  Also its total vertex count is at least \(N\).  Therefore, even
under the optimistic assumption that a partite regularization of the other
shores creates no larger normalized codegree, the owner-shore parameter is

\[
 \begin{aligned}
 k_{\rm full}\log N\,\frac{\Delta_2}{\Delta}
 &\ge 3pd\,(2\log2+o(1))m\,\frac2{m(m+1)}\\
 &\longrightarrow 3\pi\log2>6.5.
 \end{aligned}
\tag{4.2}

Thus the natural monolithic all-depth formulation does not even satisfy the
\(o(1)\) hypothesis (2.5).  Before regularization its rank shores have
different degrees, which is an additional reason that an ordinary regular
matching theorem cannot be invoked directly.  Equation (4.2) shows that
balancing those shores cannot be justified merely by quoting the owner-only
codegree estimate.  This reproduces, at the queue scale, the same constant
boundary met by the length-\(\Theta(n)\) moving carousel.

## 5. Exact remaining matching statement

The rank-two queue improves the owner packet from \(\Theta(n)\) to
\(\Theta(\sqrt n)\), and (2.5) is a real gain.  What it does **not** yet
provide is the fixed positive density required by the reset ledger.

A sufficient owner theorem is the following growing-uniformity partial
nibble statement at the present scale:

> If \(k=\Theta(\sqrt{\log N})\), a transitive \(k\)-uniform regular copy
> hypergraph with
> \(\Delta_2/\Delta=O((\log N)^{-2})\) and the queue's full distance
> inventory has a matching covering a fixed prescribed fraction of its
> vertices.

After that owner selection, the \(d\) lower target roles must be coupled
sequentially, using the factor-of-more-than-3000 target-capacity margin.
The sequential theorem must ensure that the cumulative loss over all
\(d\) layers is bounded away from the required \(\theta\)-density.  Treating
all layers as one hyperedge cannot prove this, by (4.2).

The proof frontier is therefore:

\[
 \boxed{
 \text{fixed-density queue-owner packing}
 \quad+\quad
 \text{robust sequential target-role coupling}.}
\tag{5.1}

The first term is strictly weaker than near-perfect packing, but strictly
stronger than the growing-uniformity consequence currently supplied by
(3.1).
