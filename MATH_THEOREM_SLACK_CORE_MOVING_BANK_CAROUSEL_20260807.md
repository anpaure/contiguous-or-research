# A slack core gives a flexible moving-bank carousel at zero positional cost

**Date:** 2026-08-07  
**Input:** `MATH_THEOREM_MOVING_BANK_SINGLE_BULGE_CAROUSEL_20260807.md`  
**Status:** exact local theorem.  It preserves the flat owner cycle and the
complete triangular suffix-rank ledger while allowing the low-source core to
move with the high bank.  It does not prove an owner-disjoint packing or a
globally collision-free choice of all bridge decorations.

## 1. Parameters and the slack-core data

Use

\[
 n=2m+1,\qquad D=d+1,\qquad s=m-2d,
\]

and choose integers

\[
 a\ge0,\qquad h=d+a,\qquad p=s-1-a\ge0.
\tag{1.1}
\]

Let \(R\ge2\), put \(L=Rd\), and let

\[
 K_0,K_1,\ldots,K_{R-1}\in {[n]\choose h+1}
\]

be a cyclic simple Johnson walk:

\[
|K_{j-1}\cap K_j|=h.
\tag{1.2}
\]

Let \(g_j\) be the unique incoming coordinate in \(K_j-K_{j-1}\), and put
\(H_j=K_j-\{g_j\}\).  Then \(|H_j|=h>d\) when \(a>0\), and the high
source below is \(P\cup H_j\cup\{g_j\}\).  If
\(g_j\in K_{j+1}\) (as in the cyclic-block family of Section 5), the
incoming coordinate is literally captured into \(H_{j+1}\).

Write \(B=\bigcup_jK_j\).  The literal aperture condition is

\[
 p+|B|+R(d-1)\le n.
\tag{1.3}
\]

Choose

\[
 C_j\in {K_j\cap K_{j+1}\choose a}
\tag{1.4}
\]

for every \(j\in\mathbb Z_R\).  Let \(P\) be a \(p\)-set disjoint from
all the moving-bank coordinates, and choose mutually disjoint private banks

\[
 Z_j=\{z_{j,1},\ldots,z_{j,d-1}\}
\]

disjoint from \(P\cup\bigcup_jK_j\).

Define the cyclic source word of length \(L\) by

\[
 A_{jd+r}=
 \begin{cases}
  P\cup K_j,&r=0,\\
  P\cup C_j\cup\{z_{j,r}\},&1\le r<d.
 \end{cases}
\tag{1.5}
\]

The inclusion \(C_j\subseteq K_j\cap K_{j+1}\) is the exact compatibility
condition: the low filler following high \(j\) already lies in both high
banks that can meet it in a depth-\(D\) window.

## 2. Flat owners and exact Johnson motion

### Theorem 2.1 (slack-core flat carousel)

Every \(D=d+1\) consecutive source letters in (1.5) have union of rank
\(m\).  Consecutive owner unions differ by one deletion and one insertion.
If the private \(Z\)-labels are all distinct, then all \(L\) owners are
distinct, so the owner row is a simple rank-\(m\) Johnson cycle.

#### Proof

Consider first the owner ending at \(jd+r\), where \(1\le r<d\).  Its
unique high source is \(P\cup K_j\).  The low sources preceding and following
that high use \(C_{j-1}\) and \(C_j\), respectively.  By (1.4), both filler
sets lie in \(K_j\).  The owner therefore consists of \(P\), the
\((h+1)\)-set \(K_j\), and exactly \(d\) private \(Z\)-labels.  Its rank is

\[
 p+(h+1)+d=(s-1-a)+(d+a+1)+d=m.
\tag{2.1}
\]

The owner ending at the high position \(jd\) contains the two high banks
\(K_{j-1},K_j\), the complete private bank \(Z_{j-1}\), and no other new
coordinates.  By (1.2), \(|K_{j-1}\cup K_j|=h+2\), so its rank is

\[
 p+(h+2)+(d-1)=m.
\tag{2.2}
\]

At an ordinary low shift one old \(Z\)-label leaves and one new \(Z\)-label
enters.  From a high endpoint to the next low endpoint, the unique element
of \(K_{j-1}-K_j\) leaves and \(z_{j,1}\) enters.  From the last low endpoint
to the next high endpoint, the last old \(Z\)-label leaves and the unique
element of \(K_{j+1}-K_j\) enters.  Thus every step is one Johnson exchange.

Finally, intersection with the global private \(Z\)-bank records the same
complete-bank or suffix/prefix address as in the ordinary moving-bank
carousel, and recovers the endpoint.  Hence the owners are distinct.
\(\square\)

## 3. The triangular suffix ledger is unchanged

Give endpoint \(jd+r\) age \(r\).  Let \(S_{j,r;q}\) be the union of the
last \(q\) source letters ending there, for \(1\le q\le d\).

### Theorem 3.1 (exact slack-core suffix profile)

For every endpoint and depth,

\[
 |S_{j,r;q}|=
 \begin{cases}
  s+q-1,&q\le r,\\
  m-d+q-1,&q>r.
 \end{cases}
\tag{3.1}
\]

Thus the complete rank multiplicity ledger is identical to the ordinary
single-bulge carousel.

#### Proof

If \(q\le r\), all \(q\) letters are low letters in period \(j\).  Their
union is \(P\cup C_j\) plus \(q\) private labels, and hence has rank

\[
 p+a+q=s+q-1.
\]

If \(q>r\), the suffix contains the high bank \(K_j\).  Any low filler in
the suffix is either \(C_j\) or \(C_{j-1}\), and both are already contained
in \(K_j\).  There are exactly \(q-1\) private labels.  Therefore its rank is

\[
 p+(h+1)+(q-1)
 =(s-1-a)+(d+a+1)+(q-1)
 =m-d+q-1.
\]

This proves (3.1). \(\square\)

The private \(Z\)-trace recovers every low marked occurrence.  If the
\(K_j\)'s are pairwise distinct, the bank part recovers \(j\) for every high
marked occurrence, after which the \(Z\)-trace recovers the endpoint and
depth.  Hence all marked targets are distinct inside one carousel.

## 4. Local saturated chains

At a low endpoint in period \(j\), the rank-\(s\) source base is

\[
 P\cup C_j\cup\{z_{j,r}\}.
\tag{4.1}
\]

The difference \(K_j-C_j\) has exactly \(d+1\) elements.  Order those
elements.  After the endpoint's low marked suffix chain has reached its
last low target, use the first \(d\) as bridge additions and reserve the
last one for the first marked high target.  This gives exactly the same
saturated gap between the low and high marked suffix chains as in the
ordinary carousel.

At a high endpoint choose any

\[
 E_j\in {K_j\choose a+1}.
\tag{4.2}
\]

Then \(P\cup E_j\) has rank \(s\), while \(|K_j-E_j|=d\).  Add the first
\(d-1\) remaining elements as bridge steps and reserve the last for the
first marked high target.  Thus every endpoint has a literal saturated
chain through rank \(m-1\).

The rank statement is unconditional.  Pairwise distinctness of all bridge
targets is an additional decoration problem: it follows from suitable
choices of the \(E_j\)'s and orders in explicit cyclic-block families, but
is not asserted for an arbitrary Johnson walk.

## 5. Explicit nonconstant fillers and residence

Let \(B=\{b_0,\ldots,b_{R-1}\}\) be cyclic and suppose

\[
 R\ge h+2.
\tag{5.1}
\]

Set

\[
 K_j=\{b_j,b_{j+1},\ldots,b_{j+h}\},
 \qquad
 C_j=\{b_{j+1},\ldots,b_{j+a}\}.
\tag{5.2}
\]

Then (1.2) and (1.4) hold and the fillers genuinely move when \(a>0\).
The same \(R\) and the same \(L=Rd\) may be used for any

\[
 0\le a\le R-d-2,
\tag{5.3}
\]

so this flexibility costs no additional source position.  Its total
coordinate support is

\[
 |P|+|B|+|Z|=s-1-a+Rd,
\tag{5.4}
\]

which is smaller by \(a\) than the unslacked support at the same \(R\).
Thus the exact aperture condition for this explicit family is

\[
 Rd\le n-s+1+a.
\tag{5.5}
\]

For a fixed \(B\)-coordinate, the owner-positive run has length

\[
 (h+1)d+1,
\tag{5.6}
\]

and its unique owner gap has length

\[
 (R-h-1)d-1.
\tag{5.7}
\]

Thus the construction is positive-resident whenever (5.1) holds, and is
bi-resident whenever

\[
 R\ge h+3.
\tag{5.8}
\]

More generally, for an arbitrary cyclic Johnson walk, a coordinate present
in \(\ell\ge1\) consecutive \(K\)-banks has an owner run of length
\(\ell d+1\), while a gap of \(g\) bank phases produces an owner gap of
length \(gd-1\).  Hence positive bank runs need only be nonempty, and every
bank gap of at least two phases is depth-\(d\) resident.  This permits
nonuniform residence lengths.

## 6. Gauge boundary and the exact limitation

If all fillers are one fixed set \(C_j=C\), the construction is not new:
\(P\cup C\) is the ordinary permanent core and \(K_j-C\) is the ordinary
moving bank.  Genuine flexibility begins only when the \(C_j\)'s vary.

The varying fillers change the complete rank-\(s\) inventory from one
full star into a family with moving centres

\[
 P\cup C_j.
\tag{6.1}
\]

Together with the choices (4.2) and the bridge orders, this supplies a
large decoration fibre that may be used for named-target and compiler
coupling after an owner bank has been chosen.

It does **not** remove the generic owner-packing barrier.  In the symmetric
rooted owner hypergraph every carousel still contains exactly \(2L\)
ordered adjacent-owner pairs.  The same incidence calculation as for the
ordinary carousel gives

\[
 {\Delta_2\over D_{\rm own}}
 \ge {2\over m(m+1)},
\tag{6.2}
\]

with equality at the adjacent-owner orbit when no other owner-pair orbit is
larger.  The smaller centre \(|P|=s-1-a\) and larger outside-owner pattern
cancel in this ratio.  Therefore slack creates target-decoration and
residence freedom, but by itself gives no stronger theorem for selecting a
\(\theta\)-density owner-disjoint carousel bank.
