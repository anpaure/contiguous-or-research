# Fixed additive length forbids a positive density of full deep endpoints

**Date:** 2026-08-07  
**Method:** overlap rank bound plus the architecture-free endpoint-interval
lemma  
**Status:** theorem.  Independently audited in three separate pure-math
lanes; no correction was required.

## 1. Setup

Let a word have length

\[
                         N=W+d+C,
\]

where \(C\ge0\) is fixed.  Put

\[
 Z_{i,j}=A_{i-j+1}\cup\cdots\cup A_i,
 \qquad 1\le j\le d,
\]

and call \(i\) a **full rank-\(s\) endpoint** when

\[
                         |Z_{i,j}|=s+j-1
                         \qquad(1\le j\le d).
\]

Use the top deep-slab parameters

\[
                         s=m-2d,
 \qquad                    t=m-d.
\]

The endpoint-interval lemma says that every interval of length
\(d+C+1\) in a universal word of length \(W+d+C\) contains a selected
rank-\(m\) witness interval.  Its union therefore has rank at least \(m\).

Throughout, assume \(d\ge C+2\).

## 2. The overlap bound at arbitrary separation

### Lemma 2.1

Let \(i\) and \(i+g\) be full endpoints, where
\(1\le g\le d-1\).  Then their complete source span has length \(d+g\)
and rank at most

\[
 \boxed{
 \left|A_{i-d+1}\cup\cdots\cup A_{i+g}\right|
       \le t+g-1=m-d+g-1.}
 \tag{2.1}
\]

#### Proof

Put

\[
 X=Z_{i,d},\qquad Y=Z_{i+g,d},
 \qquad H=Z_{i,d-g}.
\]

The \(d-g\) letters defining \(H\) are precisely the common part of the
two source windows, so \(H\subseteq X\cap Y\).  Fullness gives

\[
 |X|=|Y|=t-1,
 \qquad |H|=s+d-g-1=t-g-1.
\]

Consequently

\[
 |X\cup Y|
 \le 2(t-1)-(t-g-1)=t+g-1.
\]

The union \(X\cup Y\) is exactly the union of the \(d+g\) source letters
from \(i-d+1\) through \(i+g\).  This proves (2.1). \(\square\)

## 3. Forbidden separation annulus

### Theorem 3.1

Two full endpoints cannot have separation

\[
                         C+1\le g\le d-1.
 \tag{3.1}
\]

#### Proof

Their complete span has length \(d+g\ge d+C+1\), so it contains an
interval of length \(d+C+1\).  The union of that subinterval is contained
in \(X\cup Y\).  By Lemma 2.1 its rank is at most

\[
                         m-d+g-1\le m-2<m,
\]

contradicting the endpoint-interval lemma. \(\square\)

Thus every pair of full endpoints is either **close**, at distance at most
\(C\), or **far**, at distance at least \(d\).

## 4. Guard obligation inside a close cluster

If \(1\le g\le C\), extend the complete \((d+g)\)-letter span to any
containing interval of length \(d+C+1\).  The extension uses
\(C+1-g\) guard positions.  If \(G\) denotes the union of their letters,
then

\[
 \boxed{
 |G\setminus(X\cup Y)|\ge d-g+1.}
 \tag{4.1}
\]

Indeed, the extended interval has rank at least \(m\), whereas (2.1)
bounds the old span by \(m-d+g-1\).

This includes the adjacent \(B+1\) obligation as \(C=g=1\): the single
outside guard in either in-range extension must contribute at least \(d\)
fresh coordinates.

## 5. Density theorem

### Theorem 5.1

If \(E\) is the set of full endpoints in an \(N\)-letter universal word,
then

\[
 \boxed{
 |E|\le (C+1)\left(1+\left\lfloor{N-1\over d}\right\rfloor\right).}
 \tag{5.1}
\]

In particular, for fixed \(C\),

\[
                         {|E|\over W}=O((C+1)/d)=O_C(1/d)=o(1).
 \tag{5.2}
\]

#### Proof

Greedily take the least remaining endpoint \(a_j\), and put into its
cluster every endpoint in \([a_j,a_j+C]\).  A cluster contains at most
\(C+1\) integer positions.

If \(a_{j+1}\) is the least endpoint in the next cluster, then
\(a_{j+1}-a_j>C\).  The forbidden-annulus theorem forces

\[
                         a_{j+1}-a_j\ge d.
\]

The cluster anchors are therefore \(d\)-separated in \([1,N]\), so their
number is at most \(1+\lfloor(N-1)/d\rfloor\).  Multiplying by the maximum
cluster size proves (5.1). \(\square\)

## 6. Consequence for fixed-additive constructions

Any architecture requiring \(\eta W\) full endpoints for a constant
\(\eta>0\) is impossible at length \(B(k)+C\) for every fixed \(C\) and all
sufficiently large \(k\).  This rules out positive-density implementations
of:

* fixed-coordinate and multiseparator full two-rail packets;
* long product-SCD full diagonal runs;
* adjacent guarded full-pair banks; and
* any other theta repair whose marked occurrence is a full depth-\(d\)
  endpoint of base rank \(m-2d\).

The result does **not** rule out boundedly many full endpoints.  Nor does it
rule out constructions using partial endpoints, varying base ranks or
depths, nonflat selected-owner schedules, or one global chronology in which
the lower targets are not delivered by positive-density full endpoint
chains.

The constructive target for \(B(k)+O(1)\) must therefore leave the
positive-density full-endpoint paradigm, rather than merely add a reusable
guard to it.
