# Independent audit: first-aligned MSW packet versus the compound low spine

**Date:** 2026-08-13  
**Verdict:** **PASS.**  
**Frozen source:** MATH_OBSTRUCTION_FIRST_ALIGNED_MSW_PACKET_DOES_NOT_CONTAIN_COMPOUND_LOW_SPINE_AND_EXACT_HALO_CONFLICT_20260813.md  
**Source SHA-256:** 78669ed4a02bffe58413cdcb22a50eafcdc421c29a045e5ad4ca2efdf09a9bf6

This audit checked the explicit roots, the fixed seam, the marker-separation argument,
and the \(2d-7\) upper-collision family.  Substantive finite replay was run on H100; the
local machine was used only for proof and file inspection.

## 1. Explicit first-aligned rows

All four words in (2.1)--(2.2) have length \(2m\), contain equally many zeroes and ones,
and satisfy the Dyck prefix inequalities for every \(m\ge7\).  The repeated \((10)\)
tail is neutral and the terminal \(00\) closes the initial height two.

The first eligible aligned block is the claimed one in each pair, so both inverse
trades occur in the complete first-aligned packet.  Direct application of the inverse-
triple row formula gives the three displayed windows \(C_4,U_4,U_5\).

An additional H100 check at \(m=7,14,30\) locates \(C_4\) in positive row zero and
\(U_4\) in positive row one of the first trade, while \(U_5\) lies in positive row
zero of the second trade.  Exact-factor disjointness then implies that no other positive
row can contain either owner.  Hence \(C_4\) and \(U_5\) are in different wreath rows
and the edge \(C_4U_5\) is absent from the completed factor.  Theorem 2.1 and
Corollary 2.2 are therefore exact, not merely embedding failures.

## 2. Marker separation

In the cyclic row \((2,3,E,0,1,O)\), the consecutive pair \(0,1\) makes the
fixed-length window containing \(0\) and omitting \(1\) unique.

* At length \(m+1\) it starts at \(3\).
* At length \(m\) it is \(E\cup\{0\}\).
* At length \(m+2\) it starts with \(2,3\).

The portal flip-list identity places \(2m-1\) in \(E\).  Thus the three claims of
Lemma 3.1 follow.  The compound seam resources all contain \(0\) and omit \(1,2,3\);
after choosing the free screens outside \(\{1,2,3,2m-1\}\), their owner and lower rows
also omit \(2m-1\).  Comparing the unique-window alternatives proves the
owner/lower/upper separation in Corollary 3.2.  The argument is value-level only and
correctly does not infer that the compound seam edge already occurs in the factor.

## 3. Upper collision family

For (4.1), the three disjoint displayed parts have sizes

\[
                    5,\qquad m-q-1,\qquad q-2,
\]

so \(\lvert Q_{A,q}\rvert=m+2\).  Under \(m\ge3d+2\), the low even markers
\(2A,2A+2\) do not overlap the terminal even tail.  The low even pair recovers \(A\),
while the odd cut/tail recovers \(q\); hence the displayed values are distinct.

For every \(q=2,\ldots,d-3\), both \(A=q+1,q+2\) are legal and contribute two
collisions.  At \(q=d-2\), only \(A=d-1\) is legal.  The total is therefore

\[
                         2(d-4)+1=2d-7.
\]

The protected index \(-A\) lies in \([-d,q+d+1]\), and reversal preserves the cyclic
window value, moving it to the reflected collar.  Theorem 4.1 has the correct range,
rank, distinctness, orientation, and count.

## 4. Scope

The source cleanly distinguishes:

1. value separation between selected portal collars and named compound seam resources;
2. repeated nonmiddle upper values among selected collars; and
3. absence of the required compound edge from the whole deterministic first-aligned
   factor.

Only the third is a middle-incidence obstruction.  Repeated uppers are harmless when
upper coverage is merely an inequality, but obstruct distinct exact upper tickets.  A
relative row trade preserving the selected packet rows and the full owner/lower
signature remains genuinely necessary.

No mathematical or scope correction was found.
