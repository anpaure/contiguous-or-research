# A captured private coordinate moves the single-bulge reset bank at zero owner cost

**Date:** 2026-08-07  
**Method:** one-step bank capture at consecutive high phases  
**Status:** audited exact local construction; see
`MATH_AUDIT_MOVING_BANK_SINGLE_BULGE_CAROUSEL_20260807.md`.  It removes the
fixed-\(H\) hypothesis from the single-bulge ring and replaces it by a
cyclic Johnson walk of reset banks.  It does not pack different carousels,
join their owner cycles, or prove an all-dimensional upper bound.

## 1. Parameters and data

Use the odd triangular parameters

\[
 n=2m+1,\qquad D=d+1,\qquad s=m-2d,
\tag{1.1}
\]

and assume \(d\ge2\), \(s\ge1\).  Choose an integer \(R\) and put

\[
 R\ge d+2,\qquad L=Rd.
\tag{1.2}
\]

Assume the elementary aperture inequality

\[
                         L\le n-s+1.
\tag{1.3}
\]

At the optimal deadline one may take \(R=d+2\), and in fact
\(R=\lfloor(1+\varepsilon)d\rfloor\) for any fixed
\(0<\varepsilon<4/\pi-1\), for all sufficiently large parameters, because
\(d^2/m\to\pi/4<1\).

Choose pairwise disjoint sets

\[
 P,\quad B=\{b_0,\ldots,b_{R-1}\},\quad
 Z=\{z_{j,r}:j\in\mathbb Z_R,\ 1\le r<d\}
\tag{1.4}
\]

with

\[
 |P|=s-1,\qquad |B|=R,\qquad |Z|=R(d-1).
\tag{1.5}
\]

All indices on the \(b\)'s and on \(j\) are cyclic modulo \(R\).  Define

\[
 H_j=\{b_j,b_{j+1},\ldots,b_{j+d-1}\},
 \qquad g_j=b_{j+d}.
\tag{1.6}
\]

Then

\[
 |H_j|=d,\qquad g_j\notin H_j,
 \qquad H_{j+1}=H_j-\{b_j\}+\{g_j\}.
\tag{1.7}
\]

Define a cyclic source word of length \(L\) by

\[
 A_{jd+r}=
 \begin{cases}
  P\cup H_j\cup\{g_j\},&r=0,\\
  P\cup\{z_{j,r}\},&1\le r<d.
 \end{cases}
\tag{1.8}
\]

Thus every period has one high source followed by \(d-1\) low sources.
The high-private coordinate \(g_j\) is captured into the next reset bank
\(H_{j+1}\).

## 2. Flat moving owners

### Theorem 2.1 (moving-bank flat-owner carousel)

Every \(D=d+1\) consecutive source letters in (1.8) have union of rank
\(m\).  Consecutive owner unions differ by one deletion and one insertion.
All \(L\) owners are distinct.  Hence the \(D\)-window row is a simple
rank-\(m\) Johnson cycle.

#### Proof

First let a \(D\)-window end at \(jd+r\), where \(1\le r<d\).  It contains
the unique high source at \(jd\).  Its \(D\) private coordinates are

\[
 z_{j-1,r},\ldots,z_{j-1,d-1},\quad
 g_j,\quad z_{j,1},\ldots,z_{j,r}.
\tag{2.1}
\]

They are distinct and disjoint from \(H_j\).  Outside \(P\), the owner
therefore has rank

\[
                         d+D=2d+1.
\tag{2.2}
\]

Now let the window end at the high position \(jd\).  It contains the two
high sources at \((j-1)d\) and \(jd\).  By (1.7),

\[
                         H_{j-1}\cup H_j
                         =H_{j-1}\cup\{g_{j-1}\}
\tag{2.3}
\]

has size \(d+1\).  The private coordinates in the window are

\[
 g_{j-1},z_{j-1,1},\ldots,z_{j-1,d-1},g_j.
\tag{2.4}
\]

They have size \(D\), and their unique intersection with (2.3) is
\(\{g_{j-1}\}\).  Thus their combined rank is again

\[
                         (d+1)+D-1=2d+1.
\tag{2.5}
\]

Adding \(|P|=s-1\) to (2.2) or (2.5) gives

\[
                         (s-1)+(2d+1)=m.
\tag{2.6}
\]

At an ordinary low shift the window drops one \(z\)-coordinate and adds
one \(z\)-coordinate.  At the shift from a high endpoint to the next low
endpoint, the old high source leaves: the captured coordinate
\(g_{j-1}\) remains through \(H_j\), while the unique bank coordinate
\(b_{j-1}\in H_{j-1}-H_j\) leaves and \(z_{j,1}\) enters.  At the shift
from the last low endpoint to the next high endpoint, the new bank
difference \(g_j\) is already present as the high-private coordinate, so
the only net change is the outgoing \(z\)-coordinate versus the new
high-private coordinate.  Every step is therefore one Johnson exchange.

Finally, intersection with the globally private \(Z\)-bank recovers the
cyclic low-label interval of the owner.  For a high endpoint this is the
complete \((d-1)\)-set of the preceding period; for a low endpoint it is
the nontrivial suffix/prefix split in (2.1).  These sets recover \((j,r)\),
so the owners are pairwise distinct. \(\square\)

### Corollary 2.2 (literal regeneration and residence)

The complete source and bank state returns after \(L\) positions.  Every
coordinate in \(Z\) has one positive owner run of length \(D\) and one gap
of length \(L-D\).  Every coordinate in \(B\) has a positive owner run of
length at least \(D\).  Its unique owner gap has length

\[
                         (R-d-1)d-1.
\tag{2.7}
\]

Thus the exact positive-run residence condition needed for the depth-\(d\)
literal antecedent always holds.  If \(R\ge d+3\), then (2.7) is at least
\(D\), so every nonpermanent coordinate is bi-resident.  For the minimal
choice \(R=d+2\), the \(B\)-gap is only \(d-1\), so that carousel is only
an odd-side positive-residence factor.

## 3. The single-bulge rank profile survives unchanged

Give the endpoint \(jd+r\) age \(a=r\).  For \(1\le q\le d\), let
\(Z_{j,r;q}\) be the union of the last \(q\) source letters ending there.

### Theorem 3.1 (exact triangular profile)

\[
 |Z_{j,r;q}|=
 \begin{cases}
  s+q-1,&q\le r,\\
  m-d+q-1,&q>r.
 \end{cases}
\tag{3.1}
\]

Consequently every period has the same age profiles and the same triangular
rank multiplicity ledger as the fixed-bank single-bulge construction.

#### Proof

If \(q\le r\), the suffix contains \(q\) low sources and no high source,
so its union is \(P\) plus \(q\) distinct \(Z\)-labels.  If \(q>r\), it
contains the unique high source at \(jd\), together with \(q-1\) low
private labels.  The set \(H_j\cup\{g_j\}\) has size \(d+1\) and is
disjoint from those low labels.  The two displayed ranks follow. \(\square\)

All marked suffix targets in one carousel are distinct.  In the low band,
their intersection with \(Z\) recovers the endpoint and depth.  In the
high band, intersection with \(B\) is the cyclic \((d+1)\)-block

\[
                         H_j\cup\{g_j\}
                         =\{b_j,b_{j+1},\ldots,b_{j+d}\},
\tag{3.2}
\]

which recovers \(j\), since \(d+1<R\), after which the \(Z\)-part recovers
the endpoint and depth.  When \(R=d+2\), (3.2) is the facet
\(B-\{b_{j-1}\}\).

## 4. Exact bridge chains with moving banks

At a low endpoint of age \(a\ge1\), let

\[
 I_{j,a}=\{z_{j,1},\ldots,z_{j,a}\}.
\tag{4.1}
\]

Bridge the rank gap by adjoining the elements of \(H_j\) in any order.
The next marked high target then adjoins \(g_j\).  At the high endpoint,
start from \(P\cup\{g_j\}\), adjoin the first \(d-1\) elements of an
order on \(H_j\), and reserve its last element for the first marked high
target.  Exactly as in the fixed-bank hinge, this gives a saturated chain
from rank \(s\) through rank \(m-1\) for every endpoint.

For the high endpoints choose the reverse cyclic order

\[
 b_{j+d-1},b_{j+d-2},\ldots,b_j
\tag{4.2}
\]

on \(H_j\).

### Theorem 4.1 (internal all-depth target simplicity)

The marked and bridge targets of all \(L\) endpoint chains are pairwise
distinct within one carousel.

#### Proof

Every low-endpoint bridge target contains the nonempty set \(I_{j,a}\) of
globally private \(Z\)-coordinates.  That set recovers \((j,a)\); within
one endpoint, the intersection with \(H_j\) recovers the bridge offset.

A high-endpoint bridge target contains no \(Z\)-coordinate.  With the
order (4.2), its part in \(B\) is a cyclic interval ending at \(g_j\), of
length between one and \(d\).  Since \(|B|=R>d+1\), cyclic intervals of a
fixed proper length have distinct endpoints, so these targets are distinct
over all \(j\) and offsets.

Low marked targets contain no \(B\)-coordinate.  High marked targets have
the \(B\)-block (3.2), which recovers \(j\); their \(Z\)-part then recovers
the remaining address.  A low bridge has both a nonempty \(Z\)-part and a
proper nonempty \(B\)-part, whereas a high bridge has no \(Z\)-part, a low
marked target has no \(B\)-part, and a high marked target contains a
\((d+1)\)-element \(B\)-block.  Therefore no cross-type equality is
possible. \(\square\)

## 5. What the carousel changes

The fixed-bank length-\(3d\) ring forces all three reset periods to use one
common \(d\)-set \(H\).  The carousel instead supplies

\[
                         R
\tag{5.1}
\]

different reset banks, forming the cyclic Johnson walk

\[
 H_{j+1}=H_j-b_j+g_j,
\tag{5.2}
\]

while retaining:

* a flat simple rank-\(m\) owner cycle;
* the exact single-bulge triangular rank ledger;
* literal regeneration with no appended reset position; and
* an internally collision-free saturated lower chain at every endpoint.

Taking \(R=\Theta(d)\), its component length is \(Rd=\Theta(n)\), so a
theta-density reset bank would use \(\Theta(W/d^2)\), rather than
\(\Theta(W/d)\), literal components.

The surviving global theorem is still substantial: choose many such
carousels with disjoint named target inventories and owners, fuse their
owner cycles, and retain the arbitrary-width upper and terminal compiler
rows.  The present theorem does not claim that global packing.  Its gain is
that the formerly common reset bank is now a mobile cyclic-block rail with
an explicit literal transport law.

## 6. The complete base row still packs far above the theta demand

The rank-\(s\) target at every low endpoint is \(P\cup\{z_{j,r}\}\), and
the rank-\(s\) bridge base at every high endpoint is
\(P\cup\{g_j\}\).  Hence the complete rank-\(s\) inventory of one
carousel is exactly the \(L\)-petal star

\[
 \mathcal B(P,F)=\{P\cup\{x\}:x\in F\},
 \qquad F=B\mathbin{\dot\cup}Z,\quad |F|=L.
\tag{6.1}
\]

Put

\[
 \mathcal C={ [n]\choose s-1},\qquad
 \mathcal V={ [n]\choose s},\qquad
 C=|\mathcal C|,\quad V=|\mathcal V|,\quad
 v=n-s+1.
\tag{6.2}
\]

### Theorem 6.1 (integral carousel-base packing)

Assume \(L\le v\).  There is a family of carousels whose complete
rank-\(s\) inventories are pairwise disjoint.  If \(M\) is its number of
carousels and \(U=LM\) its number of endpoints, then

\[
 \boxed{
 M\ge {C(v-L+1)\over Ls+v-L+1}}
\tag{6.3}
\]

and

\[
 \boxed{
 {U\over V}\ge
 {Ls(v-L+1)\over v(Ls+v-L+1)}.}
\tag{6.4}
\]

#### Proof

Greedily choose an unused centre \(P\) having at least \(L\) unused
rank-\(s\) supersets, reserve any \(L\) of them, and stop when no such
centre remains.  Partition the selected petal labels arbitrarily into a
cyclic \(R\)-set \(B\) and the labelled low bank \(Z\); Sections 1--4
then lift the star to a carousel.

At termination every unused centre is incident with at least \(v-L+1\)
used rank-\(s\) targets.  Each used target contains exactly \(s\) centres,
so

\[
                         (C-M)(v-L+1)\le MLs.
\tag{6.5}
\]

This gives (6.3).  The incidence identity \(Cv=Vs\) gives (6.4).
\(\square\)

For the minimal carousel \(R=d+2\),

\[
 {L\over v}={d(d+2)\over m+2d+2}\longrightarrow {\pi\over4},
 \qquad {Ls\over v}\longrightarrow\infty.
\tag{6.6}
\]

Consequently

\[
 {U\over W}\longrightarrow
 \left(1-{\pi\over4}\right)e^{-\pi}>600\theta,
 \qquad
 \theta=4\sum_{a\ge1}e^{-4\pi a^2}.
\tag{6.7}
\]

Thus the longer moving-bank component retains hundreds of times the exact
bottom-row capacity needed by the reset ledger.  The next global rows are
owner disjointness and the simultaneous higher-target occurrence linkage;
(6.7) alone does not imply either one.
