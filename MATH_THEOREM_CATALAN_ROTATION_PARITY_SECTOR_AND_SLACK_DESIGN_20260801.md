# Rotation parity sectors and the exact middle-slack design

Date: 2026-08-01  
Status: unconditional structural reduction for the exact central Catalan
factor.  It removes every nonfree outer necklace when `m` is odd and gives
exact endpoint-slack identities for every cap-two factor.  It does not prove
the remaining full-orbit selector or the forest-or-bank dichotomy.

## 0. Outcome

Let `C_(2m)` act by coordinate rotation on

\[
 \mathcal L=\binom{[2m]}{m-1},\qquad
 \mathcal M=\binom{[2m]}m,\qquad
 \mathcal U=\binom{[2m]}{m+1}.
\]

There are two exact simplifications.

1. If `m` is even, the rotation action on both outer layers is free.
   If `m=2h+1` is odd, every nonfree outer set is a union of antipodal
   pairs and has stabilizer exactly two.  The nonfree lower and upper
   necklaces form an independent quotient block of size `Cat_h` on each
   shore.
2. That entire nonfree block always has an invariant exact realization
   whose physical middle edges are pairwise vertex-disjoint.  It is therefore
   already a linear forest and consumes one, rather than two, units of every
   middle capacity it meets.

Consequently, for odd `m`, the difficult rotation-selector problem may be
restricted to full lower and upper necklaces.  No cross-size orbit is needed
or even permitted by outer simplicity.

For any exact cap-two selector, invariant or not, put

\[
                         y_T=2-d_F(T)\quad(T\in\mathcal M).
\]

Then the free middle slots form an exact balanced one-design:

\[
 \sum_Ty_T=2\operatorname {Cat}_m,\qquad
 \sum_{T\ni z}y_T=\operatorname {Cat}_m
                         \quad(z\in[2m]).                 \tag{0.1}
\]

Moreover the average slack over the middle facets of either an upper colour
or a lower colour is exactly two.  This proves a global endpoint bank for
pentagonal exchanges.  It does not force that bank to meet a prescribed
cycle edge or force the two companion matching edges of a pentagonal packet.

## 1. Stabilizers on the two outer layers

### Lemma 1.1 (stabilizer divisibility)

If a subset of a cyclic `n`-set has size `r` and stabilizer order `s`, then
`s` divides both `n` and `r`.

#### Proof

The stabilizer partitions the coordinates into orbits of size `s`.  An
invariant subset is a union of those orbits, so `s` divides its cardinality.
It also divides the group order `n`.  \(\square\)

For `n=2m`,

\[
 \gcd(2m,m-1)=\gcd(2,m-1),\qquad
 \gcd(2m,m+1)=\gcd(2,m+1).                           \tag{1.1}
\]

Hence both outer actions are free when `m` is even.  When `m` is odd, an
outer stabilizer has order one or two.  Write `tau(i)=i+m`.  The sets with
stabilizer two are exactly the `tau`-invariant sets.

Put `m=2h+1`.  Such a lower set and upper set have the forms

\[
 L(A)=\bigcup_{a\in A}\{a,a+m\},\quad |A|=h,
\]

\[
 U(B)=\bigcup_{b\in B}\{b,b+m\},\quad |B|=h+1,       \tag{1.2}
\]

where `A,B` are subsets of `Z_m`.  Rotation on either rank of `Z_m` is
free, since `gcd(m,h)=gcd(m,h+1)=1`.  Therefore the number of nonfree outer
necklaces on either shore is

\[
 {1\over m}\binom mh
   ={1\over h+1}\binom{2h}h
   =\operatorname {Cat}_h.                            \tag{1.3}
\]

The total outer-necklace count is consequently

\[
 |\mathcal L/C_{2m}|=|\mathcal U/C_{2m}|=
 \begin{cases}
  \binom{2m}{m-1}/(2m),&m\text{ even},\\[1mm]
  \bigl(\binom{2m}{m-1}+\binom m{(m-1)/2}\bigr)/(2m),
      &m\text{ odd}.
 \end{cases}                                          \tag{1.4}
\]

## 2. The nonfree block is an automatic forest

### Theorem 2.1 (antipodal-sector factor)

For every odd `m=2h+1`, the nonfree lower and upper necklaces admit a
`C_(2m)`-invariant exact outer matching.  Its physical Johnson edges are
pairwise vertex-disjoint.  In particular this sector is a linear forest and
has literal middle load at most one.

#### Proof

By (1.2), containment `L(A) subset U(B)` is exactly `A subset B` in the
two middle levels `h,h+1` of `B_m`.  Their inclusion graph is an
`(h+1)`-regular bipartite graph, and `C_m` acts freely on both shores.
Its quotient, retaining parallel-edge multiplicity, is again a regular
bipartite multigraph.  Hall's theorem gives a perfect matching of its
`Cat_h` quotient vertices.

Develop one matched quotient edge `A subset B=A+{b}`.  Its literal diamond
is

\[
 L(A)\subset U(B),
\]

and its physical edge has endpoints

\[
 L(A)+\{b\},\qquad L(A)+\{b+m\}.                     \tag{2.1}
\]

Each endpoint contains exactly the `h` complete antipodal pairs indexed by
`A` and one singleton in the pair indexed by `b`.  Thus the endpoint itself
recovers `A`, `b`, and which endpoint of that last pair was used.  No endpoint
can occur in two developed quotient edges.  Hence all physical edges are
vertex-disjoint.  \(\square\)

### Corollary 2.2 (exact parity split)

An outer-simple diamond orbit projects bijectively to its lower and upper
orbits, so those two orbit sizes are equal.  For odd `m`, no candidate joins
a full outer necklace to a half-length outer necklace.  The selector margins
therefore split into independent full/full and half/half blocks, and Theorem
2.1 solves the latter block unconditionally.

The remaining full/full block may use the one residual capacity slot at a
middle vertex occupied by the antipodal sector.  The theorem does not claim
that the two physical supports are disjoint.

## 3. Every cap-two factor has a balanced slack bank

Let `F` be any set of `N=binom(2m,m-1)` physical Johnson edges whose lower
intersections enumerate `mathcal L` and whose upper unions enumerate
`mathcal U`.  Assume `d_F(T)<=2` for every middle set and define `y_T` as in
(0.1).  Put

\[
 W=\binom{2m}m,\qquad C=\operatorname {Cat}_m={W\over m+1}.
\]

### Theorem 3.1 (exact one-design of free slots)

The identities (0.1) hold.

#### Proof

Every selected edge has two middle endpoints, so

\[
 \sum_Ty_T=2W-2N=2(W-N)=2C.                          \tag{3.1}
\]

Fix a coordinate `z`.  Let

\[
 A=\binom{2m-1}{m-2},\qquad B=\binom{2m-1}m.
\]

Exactly `A` selected lower colours contain `z` and exactly `B` selected
upper colours contain `z`.  If `z` lies in the lower colour, both physical
endpoints contain it.  If it lies in the upper but not the lower colour,
exactly one endpoint contains it.  Therefore

\[
 \sum_{T\ni z}d_F(T)=2A+(B-A)=A+B.                  \tag{3.2}
\]

There are `binom(2m-1,m-1)=B` middle sets containing `z`.  Hence

\[
 \sum_{T\ni z}y_T=2B-(A+B)=B-A=C,                  \tag{3.3}
\]

where the final identity follows from
`A/B=(m-1)/(m+1)` and `2B=W`.  \(\square\)

The multiplicity `y_T` is two at an isolated middle vertex, one at a path
endpoint, and zero at an internal path or cycle vertex.  Thus Theorem 3.1 is
an exact statement about the combined endpoint-plus-isolate bank, not only
an average-degree calculation.

### Corollary 3.2 (outer facet average)

Define

\[
 s(U)=\sum_{T\subset U,\ |T|=m}y_T,qquad
 s(L)=\sum_{T\supset L,\ |T|=m}y_T.
\]

Then

\[
 \sum_{U\in\mathcal U}s(U)=2N,qquad
 \sum_{L\in\mathcal L}s(L)=2N.                     \tag{3.4}
\]

In particular both means are exactly two.

#### Proof

Every middle set lies in exactly `m` upper `(m+1)`-sets and contains exactly
`m` lower `(m-1)`-sets.  Both sums in (3.4) are therefore
`m sum_T y_T=2m C=2N`.  \(\square\)

## 4. Consequence for the forest-or-bank programme

The parity sector is no longer part of the all-`m` obstruction.  A proof may
choose its antipodal matching first, then solve only the full-orbit margins.
The balanced slack theorem proves that every exact cap-two selector has the
right global quantity and coordinate distribution of new-endpoint capacity
for pentagonal exchanges.

What remains genuinely correlated is:

1. placing slack on the facets of the particular upper colours carried by
   residual cycle orbits;
2. finding the two companion matched diamonds which make the corresponding
   alternating quotient `C6`; and
3. ensuring that a rotation-closed collection of those `C6`s increases
   graphic rank while retaining the literal cap rows.

Thus neither ordinary Hall nor the one-design identities alone prove the
forest-or-pentagonal-bank dichotomy.  They remove the periodic outer sector
and the scalar/coordinate endpoint-supply objections exactly.

## 5. Mechanical replay

Run

```text
python3 scratch/audit_catalan_rotation_parity_sector_20260801.py
```

It checks the orbit classification and formulas for `2<=m<=12`, constructs
quotient perfect matchings for every odd `m<=15`, develops them literally,
and verifies exact nonfree outer coverage and pairwise-disjoint physical
endpoints.

