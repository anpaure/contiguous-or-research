# Audit of the fixed-additive full-endpoint density no-go

**Date:** 2026-08-07  
**Audited file:**
`MATH_THEOREM_FIXED_ADDITIVE_FULL_ENDPOINT_DENSITY_NOGO_20260807.md`  
**Verdict:** PASS, with the stated large-d and linear-word scope.

## 1. Overlap identity

For endpoints (i) and (i+g), (1\le g\le d-1), the two depth-(d)
windows overlap in exactly the (d-g) source positions defining

\[
                         H=Z_{i,d-g}.
\]

Fullness gives

\[
 |X|=|Y|=t-1,
 \qquad |H|=s+d-g-1=t-g-1.
\]

Thus

\[
 |X\cup Y|\le2(t-1)-(t-g-1)=t+g-1.
\]

The complete span really is (X\cup Y) and has (d+g) letters.  There is
no missing boundary letter or cyclic assumption in this calculation.

## 2. Forbidden annulus

If (C+1\le g\le d-1), the span contains a linear interval of length

\[
                         d+C+1.
\]

The architecture-free endpoint-interval lemma applies because a word of
length (W+d+C) has endpoint excess (e=d+C).  Every such interval has
union rank at least (m), whereas the whole containing span has rank at
most

\[
                         t+g-1\le m-2.
\]

The contradiction is therefore strict by two ranks; endpoint choices or
owner architecture cannot affect it.

## 3. Cluster count

Greedy clusters based at their least endpoint contain only positions in an
interval of length (C+1), hence at most (C+1) endpoints.  Consecutive
anchors differ by more than (C); the forbidden annulus promotes that gap
to at least (d).  At most

\[
                         1+\left\lfloor{N-1\over d}\right\rfloor
\]

anchors fit in a linear word of length (N).  Multiplication gives the
claimed bound.  Endpoints in the first (d-1) positions are simply absent
from the definition of a complete depth-(d) suffix and do not create a
boundary exception.

## 4. Scope and stronger flat-row corollary

The proof is linear.  A cyclic application requires choosing a cut outside
one cluster or paying one additional boundary cluster; this does not change
the (O(W/d)) asymptotic, but it is not needed for the stated theorem.

If every (d+1)-letter window itself is a rank-(m) (D^d) owner, the
same overlap bound gives a stronger local statement: no two full endpoints
can have separation (1\le g\le d-1).  Indeed their span contains a
(d+1)-letter window, while the union of the entire span has rank

\[
                         t+g-1\le m-2.
\]

Hence an external rolling guard cannot rescue the old full-pair packet
without changing its suffix profile.  The rank-two block queue and the
single-bulge triangular hinge are genuine profile changes and therefore do
not contradict the audited theorem.
