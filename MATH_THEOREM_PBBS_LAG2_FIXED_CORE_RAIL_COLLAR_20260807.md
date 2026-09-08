# The clean lag-two promotion packet has an exact fixed-core resident rail collar

**Date:** 2026-08-07  
**Status:** unconditional local/common-history theorem.  It upgrades the
clean lag-two (B+2) packet to a flat simple biresident rail segment with
both q1 colours, both immediate upper colours, the saturated lower flag,
and the forced successor coatom all literal.  It does not pack a
positive-density family of overlapping packets or construct the global
one-copy factor.

## 1. Data

Put

\[
 L=d+2.
\]

Choose pairwise disjoint data

\[
 Q,quad C_0,quad \{a_0\},quad
 A_1=\{a_1,\ldots,a_{d-1}\},quad
 \{b^-,u,z,b,v\}
\]

with

\[
 |Q|=m-2d-2,qquad |C_0|=|A_1|=d-1.
 \tag{1.1}
\]

Define

\[
 G:=Q\mathbin{\dot\cup}C_0\mathbin{\dot\cup}\{a_0\},
 \qquad |G|=m-L,
 \tag{1.2}
\]

\[
 M:=Q\mathbin{\dot\cup}\{a_0\}\mathbin{\dot\cup}A_1,
 \qquad |M|=m-d-2,
 \tag{1.3}
\]

and

\[
 C:=C_0\mathbin{\dot\cup}\{z\},qquad |C|=d.
 \tag{1.4}
\]

All labels in

\[
 b^-,u,a_1,\ldots,a_{d-1},z,b,v
 \tag{1.5}
\]

lie outside \(G\).

## 2. The fragmented source segment

Take a cyclic toggle stream of length

\[
 2L\le R\le |[n]\setminus G|=m+L+1=m+d+3,
 \tag{2.0}
\]

whose labels are distinct elements of \([n]\setminus G\),
containing the consecutive substring

\[
 b^-,u,a_1,\ldots,a_{d-1},z,b,v.
 \tag{2.1}
\]

At ordinary positions carrying toggle \(x\), use the source letter

\[
 G\cup\{x\}.
 \tag{2.2}
\]

On the displayed substring replace those ordinary letters by

\[
 C_0\cup\{b^-\},\quad \{u\},\quad
 Q\cup\{a_0,a_1\},\ldots,Q\cup\{a_0,a_{d-1}\},
 \quad C_0\cup\{z\},\quad \{b\},\quad \{v\}.
\tag{2.3}
\]

When \(d=2\), replace the final \(\{v\}\) additionally by
\(Q\cup\{a_0,v\}\).  These endpoint enrichments use only coordinates
of the fixed core \(G\); they do not change any length-\(L\) owner value.

Every exceptional letter contains only its designated toggle outside the
fixed core \(G\).

### Theorem 2.1 (fixed-core window identity)

Every length-\(L\) source window has union

\[
 \boxed{G\cup\{\text{its }L\text{ consecutive toggle labels}\}.}
 \tag{2.4}
\]

#### Proof

Any window not wholly contained in (2.3) contains an ordinary letter and
hence all of \(G\).  The exceptional substring has length \(L+2\), so
there are three wholly exceptional length-\(L\) windows.  Each contains
at least one \(Q+a_0+a_i\) letter and the \(C_0+z\) letter.  These supply

\[
 (Q+a_0)\cup C_0=G.
\]

No exceptional letter introduces a toggle other than the label assigned
to its position.  This proves (2.4). \(\square\)

### Corollary 2.2 (owner and residence rows)

All length-\(L\) values have rank \(m\) and form a simple Johnson cycle.
Every noncore coordinate has one owner run of length \(L\) and a gap of
length \(R-L\ge L\); every coordinate of \(G\) is permanent.  Both
immediate set-theoretic palettes are simple and are represented by the
native length-\((L-1)\) overlaps and length-\((L+1)\) spans, including
the two seams adjoining the exceptional substring.

#### Proof

Sliding an \(L\)-toggle interval deletes one toggle and inserts the next.
Distinct proper intervals in a cycle of distinct labels are distinct.
One source occurrence belongs to exactly \(L\) consecutive owner windows,
and the complement has length \(R-L\).  Intersections and unions of
adjacent owners are \(G\) plus the shared \(L-1\) and total \(L+1\)
toggle labels.  The entering length-\((L-1)\) seam contains
\(C_0+b^-\), the \(Q+a_0+a_i\) bank, and hence all of \(G\).  The
outgoing seam already contains an ordinary \(G\)-letter when \(d\ge3\);
for \(d=2\), the stated enrichment of the final \(v\)-letter supplies
the missing \(Q+a_0\).  Thus the native seam unions equal the
set-theoretic overlaps as well. \(\square\)

## 3. Exact promotion rows

Index the exceptional letters in (2.3) by

\[
 0,1,ldots,L+1
\]

in the displayed order.  The three owner windows starting at (0,1,2)
are

\[
 T_-=M\cup C\cup\{u,b^-\},
 \]

\[
 T_0=M\cup C\cup\{u,b\},
 \]

\[
 T_+=M\cup C\cup\{b,v\}.
 \tag{3.1}
\]

Their two literal lower colours are

\[
 I_-=T_-\cap T_0=M\cup C\cup\{u\},
 \]

\[
 I_+=T_0\cap T_+=M\cup C\cup\{b\},
 \tag{3.2}
\]

and their literal upper colours are

\[
 J_-=T_-\cup T_0=M\cup C\cup\{u,b^-,b\},
 \]

\[
 J_+=T_0\cup T_+=M\cup C\cup\{u,b,v\}.
 \tag{3.3}
\]

At the endpoint just before the (C_0+z) letter, the final (d-1) and
(d) suffix unions are

\[
 M,qquad U=M\cup\{u\}.
 \tag{3.4}
\]

At the endpoint carrying (b), the interval from the first
(Q+a_0+a_i) letter through (b) has value

\[
 Y=M\cup C\cup\{b\}=I_+.
 \tag{3.5}
\]

Thus (u\notin Y) and

\[
 T_0=Y\cup\{u\},
 \tag{3.6}
\]

which is the authoritative PBBS forced successor-coatom relation.

### Theorem 3.1 (complete local ticket)

The fixed-core rail contains, in one literal history,

1. the complete saturated suffix piece ending in (M\subset U);
2. the forced successor coatom--owner edge (Y\subset T_0);
3. a three-owner simple Johnson path;
4. both native q1 colours;
5. both native immediate-upper colours; and
6. two-sided owner residence (L=d+2).

It exports no local immediate-palette or forced-coatom sidecar.

#### Proof

The union of the (d-1) letters (Q+a_0+a_i) is (M); adjoining the
preceding singleton (u) gives (U).  Adjoining (C_0+z=C) and the
following singleton (b), while excluding (u), gives (3.5).  The owner
and palette identities are the three consecutive cases of the fixed-core
window identity. \(\square\)

## 4. Exact remaining gate

One isolated packet may be placed in a fixed-core rail without any local
repair.  A positive-density family is not obtained by taking disjoint
copies, because each displayed substring has length (L+2=\Theta(d)\).

For starts (s) in one ambient source word, the exact shared-history
state is

\[
 M_s=\bigcup_{t=s+2}^{s+L-2}A_t,qquad
 C_s=A_{s+L-1}.
 \tag{4.1}
\]

The global theorem must choose a positive-density start set and source
letters so that all overlapping prescriptions agree, while the resulting
owners and upper colours form one-copy factors and the remaining lower
targets admit one common compiler.  The local collar proves that
residence and every immediate named row are compatible with such a cache;
it does not prove the cache/factor theorem itself.
