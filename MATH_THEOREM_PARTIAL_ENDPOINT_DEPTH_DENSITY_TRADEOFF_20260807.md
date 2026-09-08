# Partial endpoint depth versus physical density

**Date:** 2026-08-07  
**Method:** arbitrary-gap overlap of truncated suffix chains and the
architecture-free endpoint-interval lemma  
**Status:** unconditional.  It proves that bounded puncturing of a full
two-rail endpoint does not evade the fixed-additive obstruction.  A packet
family occurring at fixed positive density must delete a positive fraction
of the \(d\) endpoint depths.

## 1. Truncated full endpoints

Let

\[
 n=2m+1,\qquad s=m-2d,\qquad W={n\choose m},
\]

and let a universal word have length

\[
                         N=W+d+C.                         \tag{1.1}
\]

For \(1\le h\le d\), call position \(i\) an **\(h\)-full endpoint** if

\[
 \left|A_{i-j+1}\cup\cdots\cup A_i\right|=s+j-1
 \qquad(1\le j\le h).                                   \tag{1.2}
\]

Write \(E_h\) for the set of such endpoints.  Thus \(E_d\) is the full
endpoint set considered in the fixed-additive density no-go.

## 2. Arbitrary-gap overlap

### Lemma 2.1

Let \(i,i+g\in E_h\), where \(1\le g\le h-1\).  Then the complete
\((h+g)\)-letter span of their two depth-\(h\) suffixes has rank at most

\[
                         \boxed{s+h+g-1}.                 \tag{2.1}
\]

#### Proof

Let \(X,Y\) be the two depth-\(h\) suffix unions.  Their overlap is the
depth-\((h-g)\) suffix at the first endpoint.  By (1.2),

\[
 |X|=|Y|=s+h-1,
 \qquad |X\cap Y|\ge s+h-g-1.
\]

Therefore

\[
 |X\cup Y|
 \le2(s+h-1)-(s+h-g-1)=s+h+g-1.
\]

The union \(X\cup Y\) is the complete source span. \(\square\)

## 3. The partial-depth forbidden annulus

Put

\[
                         a=d+C+1-h.                       \tag{3.1}
\]

### Theorem 3.1

Assume

\[
                         2h\ge d+C+2.                     \tag{3.2}
\]

No two members of \(E_h\) have separation

\[
                         \boxed{a\le g\le h-1}.           \tag{3.3}
\]

#### Proof

If \(g\ge a\), the two-suffix span has length

\[
 h+g\ge h+a=d+C+1.
\]

It therefore contains a length-\((d+C+1)\) interval.  Lemma 2.1 bounds
the union of even the whole span by

\[
 s+h+g-1
 \le s+2h-2
 \le m-2<m,                                               \tag{3.4}
\]

because \(h\le d\).  But the endpoint-interval lemma says that every
length-\((d+C+1)\) interval in a universal word of length \(W+d+C\)
contains a selected rank-\(m\) witness and hence has rank at least \(m\).
This is a contradiction.  Condition (3.2) is exactly the assertion that
the interval (3.3) is nonempty. \(\square\)

### Theorem 3.2 (density bound)

Under (3.2),

\[
 \boxed{
 |E_h|\le
 (d+C+1-h)
 \left(1+\left\lfloor{N-1\over h}\right\rfloor\right).}
                                                               \tag{3.5}
\]

#### Proof

Greedily choose the least remaining endpoint \(x\), and put all endpoints
in

\[
                         [x,x+a-1]
\]

into its cluster.  A cluster has at most \(a\) integer positions.  The
next cluster anchor is at distance at least \(a\); Theorem 3.1 forces it
to be at distance at least \(h\).  Thus there are at most
\(1+\lfloor(N-1)/h\rfloor\) anchors. \(\square\)

For \(h=d\), equation (3.5) becomes the full-endpoint density theorem.

## 4. Positive density requires a linear puncture

### Corollary 4.1

Fix \(\eta>0\), and suppose

\[
                         |E_h|\ge\eta W.                  \tag{4.1}
\]

If \(h>(d+C+1)/2\), then

\[
 d+C+1-h
 \ge {\eta Wh\over N+h-1}.                              \tag{4.2}
\]

In the fixed-additive regime \(C=O(1)\), if \(h/d\to1\), this gives

\[
                         d-h\ge(\eta-o(1))d.              \tag{4.3}
\]

More symmetrically, along any subsequence with \(h/d\to\alpha>1/2\),
(3.5) implies

\[
                         \eta\le{1-\alpha\over\alpha}+o(1),
 \qquad
                         \alpha\le{1\over1+\eta}+o(1).   \tag{4.4}
\]

#### Proof

Combine (3.5) and (4.1), and use

\[
 1+\left\lfloor{N-1\over h}\right\rfloor
 \le {N+h-1\over h}.
\]

This gives (4.2).  Since \(N/W\to1\), equations (4.3)--(4.4) follow by
division by \(d\) and taking limits. \(\square\)

For the theta-density reset demand, \(\eta=\theta>0\), any surviving
endpoint chart must therefore omit at least

\[
                         (\theta-o(1))d                  \tag{4.5}
\]

of the top depths if the remaining depth is asymptotic to \(d\).
Although \(\theta\) is numerically small, (4.5) diverges with \(k\).

## 5. Consequences for reset-interface design

The following modifications of the old two-full-rail packet are still
insufficient for \(B(k)+O(1)\):

* deleting one endpoint depth;
* deleting any bounded number of endpoint depths;
* adding one punctured coordinate while retaining \(d-O(1)\) marked
  suffix levels;
* a bounded toggle/polarity field; or
* a bounded-state guard which changes history but leaves the truncated
  suffix profile (1.2) at \(d-O(1)\) depths.

The first quantitatively viable suffix endpoint has depth at most

\[
                         {d\over1+\theta}+o(d),            \tag{5.1}
\]

or else the construction must abandon the saturated suffix profile itself.
Thus the next positive architecture must reroute a growing bank of top
lower targets through another compiler interface; a bounded endpoint-state
repair cannot suffice.

