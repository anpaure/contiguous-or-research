# Consecutive full deep endpoints have an unavoidable deadline-sized central deficit

**Date:** 2026-08-07  
**Method:** use the shared depth-((d-1)) suffix, then apply the
architecture-free endpoint-interval lemma  
**Status:** unconditional for \(d\ge2\), which is the asymptotic regime at
issue.  It rules out every unguarded adjacent-full-piece packet at the exact
bound and identifies the minimum rank contribution of a fixed-additive reset.

## 1. Full endpoints

For a word (A=(A_1,\ldots,A_N)), put

\[
 Z_{i,j}=A_{i-j+1}\cup\cdots\cup A_i,
 \qquad1\le j\le d.                                      \tag{1.1}
\]

Call (i) a full rank-(s) endpoint when

\[
                         |Z_{i,j}|=s+j-1
                         \qquad(1\le j\le d).             \tag{1.2}
\]

Use the top deep-slab parameters

\[
                         s=m-2d,\qquad t=m-d.              \tag{1.3}
\]

Thus the depth-(d) target has rank (t-1), and the depth-((d-1))
target has rank (t-2).

## 2. Exact adjacent-pair bound

### Theorem 2.1 (deadline-sized deficit)

Assume \(d\ge2\).  If (i) and (i+1) are both full rank-(s) endpoints, then

\[
 \boxed{
   \left|A_{i-d+1}\cup\cdots\cup A_{i+1}\right|
       \le t=m-d.}                                       \tag{2.1}
\]

#### Proof

Put

\[
 X=Z_{i,d},\qquad Y=Z_{i+1,d},
 \qquad H=Z_{i,d-1}
          =A_{i-d+2}\cup\cdots\cup A_i.                 \tag{2.2}
\]

The shared (d-1) letters give (H\subseteq X\cap Y).  By fullness,

\[
                         |X|=|Y|=t-1,
 \qquad |H|=t-2.                                         \tag{2.3}
\]

Therefore

\[
                         |X\cup Y|
 \le2(t-1)-(t-2)=t.                                     \tag{2.4}
\]

Finally (X\cup Y) is exactly the union of the (d+1) letters from
(i-d+1) through (i+1). \(\square\)

The bound uses no common-core, star, SCD, PBBS, or owner-factor hypothesis.
The common-core and product-diagonal packets attain equality in (2.1), but
equality is still (d) ranks below the middle layer.

## 3. Exact-bound no-go

Let

\[
                         W={2m+1\choose m}.
\]

The architecture-free endpoint-interval lemma says that in any universal
word of length (W+e), every interval of length (e+1) contains one of
the (W) selected rank-(m) witness intervals, and hence has union rank at
least (m).

At the exact lower bound (e=d).  The interval in (2.1) has length
(d+1=e+1), but rank at most (m-d<m), a contradiction.

### Corollary 3.1

For \(d\ge2\), no universal word of length (B(k)=W+d) contains two
consecutive full rank-(s=m-2d) endpoints.

Consequently, none of the following can pay the theta reset deficit by an
unguarded adjacent pair at the exact bound:

* a common-core two-endpoint star packet;
* the fixed-coordinate or multiseparator two-rail SCD packet;
* a product-SCD diagonal run; or
* any other construction whose claimed saving is a pair of adjacent full
  endpoints with ranks (1.2).

Their formerly open owner-envelope gate is locally impossible, not merely
unproved.

## 4. The precise (B+1) guard obligation

At length (W+d+1), every interval of length (d+2) has rank at least
(m).  If an adjacent full pair lies internally, its two one-letter
extensions are

\[
 A_{i-d}\cup X\cup Y,
 \qquad
 X\cup Y\cup A_{i+2}.                                    \tag{4.1}
\]

Theorem 2.1 implies the necessary inequalities

\[
 \boxed{
 |A_{i-d}\setminus(X\cup Y)|\ge d,
 \qquad
 |A_{i+2}\setminus(X\cup Y)|\ge d.}                     \tag{4.2}
\]

More generally, at length (W+d+C), every length-((d+C+1)) extension
of the pair must contribute at least (d) new coordinates outside
(X\cup Y) across its (C) guard positions.

Thus fixed additive slack does not remove the reset problem by scalar
counting.  It creates a bounded number of physical guard positions, but
those positions must collectively carry a deadline-sized fresh-coordinate
bank and must be reusable without accumulating positions.

Equation (4.2) is necessary, not sufficient: the guards must also preserve
their own lower targets, every upper witness, residence, and the terminal
compiler.

## 5. Revised construction target

The correct local object is a **guarded full-pair reset**:

1. two full endpoint chains carrying the desired named lower targets;
2. left and right guards contributing at least (d) fresh coordinates as
   in (4.2);
3. selected central windows equal to prescribed rank-(m) owners;
4. a bounded-state mechanism allowing the guard bank to be transported and
   reused across many reset events;
5. complete upper and compiler transparency.

Proving a positive-density, nonaccumulating bank of these guarded resets
would repair the theta deficit for a (B(k)+1) construction.  The present
theorem proves only the obstruction and the minimum rank contribution.
