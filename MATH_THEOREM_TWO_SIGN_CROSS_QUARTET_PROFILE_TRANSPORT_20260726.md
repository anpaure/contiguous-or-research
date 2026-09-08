# Two-sign cross-quartet profile transport

Date: 2026-07-26

## 0. Result

The cross-quartet packet trade in
`MATH_THEOREM_QUARTET_RESOLUTION_TRADES_AND_STRUCTURED_CPM_GATE_20260726.md`
has two different internal comparison shores.  Keeping both shores removes
an asymmetry in the original statement.

Let (A,B) be disjoint four-sets and, for (1\le k\le4), put

\[
 V_k^+=\binom Ak\times\binom B{k-1},\qquad
 V_k^-=\binom A{k-1}\times\binom Bk.
\tag{0.1}
\]

The cross shore pairs a vertex of (V_k^+) to a vertex of (V_k^-) by
deleting one element of (A) and inserting one element of (B).  It has
local lower and upper block-size profiles

\[
            (k-1,k-1),\qquad (k,k),
\tag{0.2}
\]

respectively.  There are two internal shores:

* for (1\le k\le3), the **large-layer shore** factors the (k)-layer
  in (A) on (V_k^+), and the (k)-layer in (B) on (V_k^-);
* for (2\le k\le4), the **small-layer shore** factors the
  ((k-1))-layer in (B) on (V_k^+), and the ((k-1))-layer in (A)
  on (V_k^-).

Against the large-layer shore, the cross shore changes the upper profile
on all sectors (k=1,2,3), of total local density (13/32).  Against the
small-layer shore, it changes the lower profile on all sectors
(k=2,3,4), also of total local density (13/32).  After tensoring with
any disjoint (Q_{r-1}), both comparisons are exact owner trades by whole
(Q_r) packets, with no seam or collar loss.

Thus one paired-quartet local sector supplies positive owner-density
profile transport separately for both signs.  This is not yet
positive-density transport at depth-\(q\) occurrence scale: an elementary
cross packet has one crossing axis, and only a \(q/r\) fraction of its
depth-\(q\) windows contain that axis.  Nor are the owner sectors belonging
to several quartet pairs automatically disjoint.  The result therefore
does not prove `HCRT`; it only removes a local one-sign invariant.

## 1. The cross shore

Join (X\in V_k^+) to (Y\in V_k^-) when (Y) is obtained from (X)
by deleting one occupied coordinate of (A) and inserting one unoccupied
coordinate of (B).  The resulting bipartite graph is
(k(5-k))-regular, hence has a perfect matching.  Fix one such matching
(\Xi_k).

If (XY\in\Xi_k), then

\[
 \bigl(|(X\cap Y)\cap A|, |(X\cap Y)\cap B|\bigr)
      =(k-1,k-1),
\tag{1.1}
\]

and

\[
 \bigl(|(X\cup Y)\cap A|, |(X\cup Y)\cap B|\bigr)
      =(k,k).
\tag{1.2}
\]

These identities depend only on the two endpoint layers, not on the
chosen one-factor.

## 2. The two internal shores

Every nontrivial layer (J(4,j)), (j=1,2,3), has a one-factor.  Fix
one such factor whenever it is used below.

### Lemma 2.1 (large-layer shore)

For (1\le k\le3), there is an internal perfect matching
(\Lambda_k^{\rm big}) on (V_k^+\mathbin{\dot\cup}V_k^-) such that its
edges have profiles

\[
 \begin{array}{c|c|c}
  \text{sector}&\text{lower intersection}&\text{upper union}\\ \hline
  V_k^+&(k-1,k-1)&(k+1,k-1)\\
  V_k^-&(k-1,k-1)&(k-1,k+1).
 \end{array}
\tag{2.1}
\]

#### Proof

On (V_k^+), hold the (B)-coordinate fixed and use a one-factor of
(J(A,k)).  Two adjacent (k)-sets have intersection size (k-1) and
union size (k+1).  On (V_k^-), hold the (A)-coordinate fixed and
use a one-factor of (J(B,k)).  This proves both perfectness and (2.1).
\(\square\)

### Lemma 2.2 (small-layer shore)

For (2\le k\le4), there is an internal perfect matching
(\Lambda_k^{\rm small}) with profiles

\[
 \begin{array}{c|c|c}
  \text{sector}&\text{lower intersection}&\text{upper union}\\ \hline
  V_k^+&(k,k-2)&(k,k)\\
  V_k^-&(k-2,k)&(k,k).
 \end{array}
\tag{2.2}
\]

#### Proof

On (V_k^+), hold the (A)-coordinate fixed and factor
(J(B,k-1)).  On (V_k^-), hold the (B)-coordinate fixed and factor
(J(A,k-1)).  Adjacent ((k-1))-sets have intersection size (k-2)
and union size (k), proving (2.2). \(\square\)

## 3. Exact packet trades and their density

Let (Q\cong Q_{r-1}) use coordinate pairs disjoint from (A\cup B).
Tensor every edge of any shore above with (Q).  Each product is a
physical (Q_r) packet.  Since each shore is a perfect matching on the
same owner set (V_k^+\mathbin{\dot\cup}V_k^-), either of

\[
 \Lambda_k^{\rm big}\times Q\longleftrightarrow\Xi_k\times Q,
 \qquad
 \Lambda_k^{\rm small}\times Q\longleftrightarrow\Xi_k\times Q
\tag{3.1}
\]

is an exact owner trade whenever the corresponding internal shore exists.
No compiler interval crosses between packets, so all literal target
derivatives are additive and there is no boundary term.

For the large-layer comparison, (1.1) and (2.1) show that the lower
block-size profile is unchanged, while (1.2) and (2.1) show that the upper
profile changes.  Its local owner mass, over (k=1,2,3), is

\[
 2\sum_{k=1}^3\binom4k\binom4{k-1}
 =2(4+24+24)=104.
\tag{3.2}
\]

For the small-layer comparison, (1.2) and (2.2) show that the upper
profile is unchanged, while (1.1) and (2.2) show that the lower profile
changes.  Its mass is

\[
 2\sum_{k=2}^4\binom4k\binom4{k-1}
 =2(24+24+4)=104.
\tag{3.3}
\]

There are (2^8=256) local subsets of (A\cup B).  Under central-rank
conditioning on the remaining (2m-8) coordinates, every fixed local
pattern has probability (2^{-8}+o(1)), uniformly for rank displacement
(o(m)).  Therefore (3.2)--(3.3) give

\[
                    {104\over256}+o(1)
                    ={13\over32}+o(1)
\tag{3.4}
\]

owner density for each sign separately.

## 4. Audited boundary

Proved:

* exact lower-profile transport on (13/32+o(1)) owner density;
* exact upper-profile transport on (13/32+o(1)) owner density;
* whole-packet implementation with zero owner and seam boundary.

Not proved:

* that repeated changing pairings drive the joint all-depth floor energy
  to (o(W));
* that the two sign-specific comparisons can be scheduled without losing
  their common compiler chronology; or
* that a hierarchy accumulates \(\Omega(r/q)\) crossing axes in typical
  packets (if physical crossings are ultimately necessary); or
* the hierarchical defect-circulation statement `HCRT`.

The result strengthens the local input to `HCRT` and removes the possible
objection that the original cross-profile shore transports only one sign
on substantial owner mass.
