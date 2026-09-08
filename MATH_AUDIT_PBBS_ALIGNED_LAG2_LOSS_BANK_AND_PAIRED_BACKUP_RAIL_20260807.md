# Audit of the aligned lag-two loss bank and paired backup rail

**Date:** 2026-08-07  
**Scope:** independent hand audit of the exact interval families, resource
separation, rail length, and protected-factor accounting in
`MATH_THEOREM_PBBS_ALIGNED_LAG2_LOSS_BANK_AND_PAIRED_BACKUP_RAIL_20260807.md`.
No finite search is used.

## 1. One-collar interval partition

Exceptional positions and core pieces are:

| positions | source core contribution |
|---|---|
| \(b^-\) | \(C_0\) |
| \(u\) | none |
| \(a_1,\ldots,a_{d-1}\) | \(Q+a_0\) |
| \(z\) | \(C_0\) |
| \(b,v\) | none |

A wholly exceptional interval has its old value iff it meets one
\(C_0\)-position and one \(Q+a_0\)-position.  The complement consists of
the interval families of

\[
 (b^-,u),\quad (z,b,v),\quad
 (u,a_1,\ldots,a_{d-1}),\quad (b,v).
\]

After removing the duplicate singleton \(u\) and the contained
\((b,v)\)-deck, the counts are

\[
 \binom{d+1}{2}+2+6=\binom{d+1}{2}+8.
\]

**Result:** PASS.

## 2. Paired-tail identity

For four distinct labels \(z_1,b,v,z_2\),

\[
 \operatorname{Deck}(z_1,b,v)
 \cup\operatorname{Deck}(z_2,v,b)
 =
 \operatorname{Deck}_{\le3}(z_1,b,v,z_2)
\]

where the right side means intervals wholly contained in the first or
last three positions.  This follows because reversal does not change the
set-valued interval family:

\[
 \operatorname{Deck}(z_2,v,b)=\operatorname{Deck}(b,v,z_2).
\]

Thus four positions replace two independent three-position tail backups.

**Result:** PASS.

## 3. Rail length

The common prefix has length \(d+1\).  Each packet pair uses four tail
positions, and an unpaired packet uses three.  Therefore

\[
 R_0=d+1+4\lfloor p/2\rfloor+3(p\bmod2)
 =d+1+2p+(p\bmod2).
\]

At maximal positive residue,

\[
 R_0\le d+2+d(d+1)=d^2+2d+2
 =\left(\frac\pi4+o(1)\right)m.
\]

**Result:** PASS.

## 4. Resource separation

Every packet owner/palette vertex contains its private \(z_j\).  The
\(z\)-pool is disjoint from the common labels and every endpoint pool, so
cross-packet equality is impossible.  Inside a packet, the fresh labels
\(b^-,u,y_j,w_j\) separate vertices of equal rank.  Distinct
\(C_{0,j}\)'s separate the flag bottoms.

**Result:** PASS, conditional only on the explicit availability inequality
\(\binom{|G|}{d-1}\ge p\), which holds asymptotically in the intended
range.

## 5. Protected-factor budget

The backup rail has \(R\) owner vertices and \(R\) immediate-upper
vertices, hence \(2R\) protected incidence edges and protected parameter
\(H_{\rm back}=R\).  The clean packet bank has \(4p\) incidence edges and
parameter \(H_{\rm clean}=2p\).

Separately,

\[
 H_{\rm back}/m\le\pi/4+o(1),\qquad
 H_{\rm clean}/m\le\pi/4+o(1),
\]

so the C4--spectral theorem applies to either one.  Jointly its sufficient
parameter can be

\[
 H_{\rm back}+H_{\rm clean}\le\pi m/2+o(m),
\]

outside the theorem's hypothesis \(H< m+1\).

**Result:** PASS.  This is correctly recorded as an open joint-extension
gate, not as a no-go for every possible joint construction.

## 6. Scope exclusions

The theorem does not claim:

1. a Hamilton cycle containing the backup rail;
2. a two-factor containing the union of backup rail and all packets;
3. arbitrary-width upper coverage of the completed carrier;
4. a literal antecedent realizing the completed owner factor; or
5. a same-parity regenerative induction.

It supplies exactly the missing-value atlas and its compressed literal
backup rail.

**Overall audit:** PASS within the stated scope.

