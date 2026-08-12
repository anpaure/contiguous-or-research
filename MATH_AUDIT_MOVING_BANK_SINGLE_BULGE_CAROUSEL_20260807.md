# Audit of the moving-bank single-bulge carousel

**Date:** 2026-08-07  
**Audited file:** `MATH_THEOREM_MOVING_BANK_SINGLE_BULGE_CAROUSEL_20260807.md`  
**Verdict:** PASS, including the generalized range \(R\ge d+2\), with one
minor integer-parameter clarification.  The flat owner row, cyclic wrap,
Johnson simplicity, exact positive and zero runs, suffix ranks and internal
all-depth target simplicity all check.  For \(R>d+2\), the double-high
owner and high marked targets use proper cyclic \(B\)-blocks rather than
facets; the proofs need only their lengths and addresses.

## 1. Coordinate aperture

For arbitrary \(R\ge d+2\), the coordinates outside \(P\) are

\[
 |B|+|Z|=R+R(d-1)=Rd=L.
\]

Thus condition \(L\le n-s+1=|[n]\setminus P|\) is exactly the required
fit condition.  At the triangular deadline,
\(d^2/m\to\pi/4<1\), so \(R=d+2\) and \(R=d+3\) both fit for all
sufficiently large parameters.  More generally, if
\(0<\varepsilon<4/\pi-1\), an integer choice
\(R=(1+\varepsilon)d+O(1)\) fits.  The theorem's phrase
\(R=(1+\varepsilon)d\) should be read with an integer rounding unless the
product is integral.

## 2. Every \(D\)-window

Write \(O_{j,r}\) for the \(D=d+1\) window ending at position \(jd+r\).

For \(1\le r<d\), the window contains the unique high source at \(jd\).
Its \(Z\)-part is

\[
 \{z_{j-1,r},\ldots,z_{j-1,d-1}\}
 \cup
 \{z_{j,1},\ldots,z_{j,r}\},
\]

of size \(d\).  Its \(B\)-part is

\[
 H_j\cup\{g_j\}=\{b_j,b_{j+1},\ldots,b_{j+d}\},
\]

of size \(d+1\).  When \(R=d+2\), this is
\(B\setminus\{b_{j-1}\}\); for larger \(R\) it is a proper cyclic
block.  Hence the part outside \(P\) has size \(2d+1\).

For \(r=0\), the window contains both highs \((j-1)d\) and \(jd\), and
the complete preceding low block.  Its \(B\)-part is the cyclic block

\[
 H_{j-1}\cup\{g_{j-1}\}\cup H_j\cup\{g_j\}
 =\{b_{j-1},b_j,\ldots,b_{j+d}\}.
\]

This has size \(d+2\) because \(R\ge d+2\); only at the minimal value
is it all of \(B\).  Equivalently, \(H_{j-1}\cup H_j\) has size
\(d+1\), contains \(g_{j-1}\), and omits \(g_j\).  The \(Z\)-part has
size \(d-1\).  Again the outside rank is
\((d+2)+(d-1)=2d+1\).  Adding
\(|P|=s-1\) gives rank \(m\) in both cases.

This explicitly checks the potentially dangerous double-high window.

## 3. Johnson exchanges and simplicity

The three transition types are, with all \(B\)-indices read modulo \(R\):

\[
 \begin{array}{c|c|c}
 \text{transition}&\text{deleted}&\text{inserted}\\ \hline
 O_{j,0}\to O_{j,1}&b_{j-1}&z_{j,1}\\
 O_{j,r}\to O_{j,r+1}&z_{j-1,r}&z_{j,r+1}\\
 O_{j,d-1}\to O_{j+1,0}&z_{j-1,d-1}&g_{j+1}=b_{j-1}.
 \end{array}
\]

Thus every step is one deletion and one insertion, including both seams.
The identities remain valid at the cyclic wrap because the displayed
index blocks have length at most \(d+2\le R\).  At equality the
double-high block is all of \(B\); above equality it is proper.

At a high endpoint, intersection with \(Z\) is the whole preceding
\((d-1)\)-set \(Z_{j-1,*}\).  At a low endpoint it is a size-\(d\)
suffix/prefix split between the labelled blocks \(j-1,j\).  These
intersections recover \((j,r)\), so no owners repeat.  The wrap transition
uses the same formula modulo arbitrary \(R\ge d+2\).

## 4. Positive residence

A coordinate \(z_{j,r}\) occurs in one source position, hence in exactly
the \(D\) consecutive owner windows containing that position.

A coordinate \(b_t\) is present in the low-ending owners of precisely the
\(d+1\) periods

\[
                         j=t-d,t-d+1,\ldots,t,
\]

and in the high-ending owners of the \(d+2\) periods

\[
                         j=t-d,t-d+1,\ldots,t+1.
\]

After the high endpoint of period \(t+1\), the trace is zero on its
remaining \(d-1\) low endpoints and on all \(d\) endpoints of the
\(R-d-2\) intervening periods.  Hence its unique zero run has exact length

\[
 (d-1)+(R-d-2)d=(R-d-1)d-1.
\]

The complementary positive run has length

\[
 L-((R-d-1)d-1)=d(d+1)+1\ge D.
\]

For \(R=d+2\), the zero run is \(d-1\).  For \(R\ge d+3\), it is at
least \(2d-1\ge d+1=D\).  A \(Z\)-coordinate has positive run \(D\)
and gap \(L-D\ge D\), so every nonpermanent coordinate is bi-resident
when \(R\ge d+3\).

## 5. Suffix ranks

For an endpoint of age \(r\), a suffix of length \(q\le r\) contains
only \(q\) low sources, hence has rank

\[
                         |P|+q=s+q-1.
\]

For \(q>r\), it contains exactly the current high source and \(q-1\)
low labels.  Its rank is

\[
 |P|+|H_j\cup\{g_j\}|+(q-1)
   =(s-1)+(d+1)+(q-1)=m-d+q-1.
\]

The restriction \(q\le d\) is important: it prevents the suffix from
reaching the preceding high.

Low marked targets are addressed by their labelled \(Z\)-intervals.
High marked targets have the cyclic block

\[
                         \{b_j,b_{j+1},\ldots,b_{j+d}\}
\]

of length \(d+1<R\), which recovers its start \(j\), and their labelled
\(Z\)-part then recovers age and depth.  At \(R=d+2\) this block happens
to be a facet; no facet property is used.  Hence marked targets are simple.

## 6. Bridge and marked collision classes

For a low endpoint, every bridge target has the nonempty private address

\[
                         I_{j,a}=\{z_{j,1},\ldots,z_{j,a}\}.
\]

It recovers \((j,a)\); the \(B\)-prefix size and content recover the
bridge offset.  Thus all low bridges are distinct for arbitrary local
orders on \(H_j\).

For a high endpoint, use the order

\[
                         b_{j+d-1},\ldots,b_j.
\]

The bridge targets are the base \(P+g_j\) and the first \(d-1\) prefix
extensions.  Their \(B\)-parts are the cyclic intervals ending at \(g_j\)
of lengths \(1,\ldots,d\).  Since \(|B|=R>d+1\), endpoint plus proper
length identifies each interval.  These targets are pairwise distinct.

The last element \(b_j\) is **not** a bridge addition: adding it produces

\[
                         P\cup H_j\cup\{g_j\},
\]

the first marked high target.  Section 4 should be read with this standard
fixed-hinge convention.  If “adjoin the elements of \(H_j\)” were read as
including all \(d\) elements inside the bridge bank, that final set would
duplicate the marked target.  This is a wording issue, not an issue in the
displayed collision proof, which explicitly uses bridge lengths
\(1,\ldots,d\).

Finally the four target types are separated by their \((B,Z)\)-profiles:

\[
 \begin{array}{c|c|c}
 &B\text{-part}&Z\text{-part}\\ \hline
 \text{low marked}&\varnothing&\ne\varnothing\\
 \text{low bridge}&1,\ldots,d&\ne\varnothing\\
 \text{high bridge}&1,\ldots,d&\varnothing\\
 \text{high marked}&d+1&\text{arbitrary}.
 \end{array}
\]

No cross-type equality is possible.  This completes the collision audit.

## 7. Scope

The theorem is a valid local all-depth carousel for every integer
\(R\ge d+2\) satisfying the aperture bound.  It proves no disjointness
between different carousels, no owner-factor decomposition, no cycle
fusion, no arbitrary-upper deck and no terminal compiler.  Those global
rows remain exactly as stated in the candidate.
