# Gate C: fixed-band containment rigidity

**Status (2026-08-22).**  The theorem below is proved.  It gives a sharp
structural restriction on any cross-split trade: no product atom using a
genuinely different split is contained in a fixed central two-slice band.
Consequently an exact coverage-preserving trade supported inside a
completed band cannot escape to another split.  A useful cross-split
absorber must change the covered set across the boundary of that band.

## 1. Definitions

Let

\[
 b=2h+1\ge5,
 \qquad |\Omega|=2b,
 \qquad \mathcal V={\Omega\choose b}.
\]

For a reference `b`-set `P subset Omega`, define

\[
 \mathcal C(P)=
 \{S\in\mathcal V:|S\cap P|\in\{h,h+1\}\}.           \tag{1.1}
\]

Let `A dotcup B=Omega`, with both blocks of size `b`, and let `alpha,beta`
be cyclic orders on `A,B`.  The corresponding all-split product atom is

\[
 E(A,\alpha,\beta)=
 \{I_\alpha(i,h)\cup I_\beta(j,h+1):
                         i,j\in\mathbb Z_b\}.          \tag{1.2}
\]

The unordered coordinate split of this atom is `{A,B}`.

## 2. The rigidity theorem

### Theorem 2.1 (fixed-band containment rigidity)

For every product atom `E(A,alpha,beta)` and every reference set `P`,

\[
                 E(A,\alpha,\beta)\subseteq\mathcal C(P)           \tag{2.1}
\]

if and only if

\[
                              A=P\quad\text{or}\quad A=\Omega-P.   \tag{2.2}
\]

Equivalently, an atom is contained in `mathcal C(P)` precisely when its
unordered split is `{P,Omega-P}`.

#### Proof

Replacing `P` by `Omega-P` leaves `mathcal C(P)` unchanged.  We may
therefore assume

\[
                         p:=|P\cap A|\le h.             \tag{2.3}
\]

Write the membership indicators of `P cap A` in cyclic order `alpha` as a
binary word `(a_i)` with `p` ones, and put

\[
                         x_i=\sum_{q=0}^{h-1}a_{i+q}.   \tag{2.4}
\]

Since `|P|=|A|=|B|=b`, the set `B-P` also has size `p`.  Take its binary
membership word in cyclic order `beta`.  The complement in `B` of a cyclic
`(h+1)`-interval is a cyclic `h`-interval; after a harmless cyclic
reindexing, let `(t_j)` be the resulting length-`h` window-count sequence
of that `p`-one word.

For the atom cell indexed by `(i,j)`, direct counting gives

\[
 |(I_\alpha(i,h)\cup I_\beta(j,h+1))\cap P|
                      =h+1-p+x_i+t_j.                 \tag{2.5}
\]

Thus the cell belongs to `mathcal C(P)` if and only if

\[
                         x_i+t_j\in\{p-1,p\}.           \tag{2.6}
\]

If the whole atom is contained in the band, (2.6) holds for every pair
`(i,j)`.  Consequently

\[
 \bigl(\max_i x_i-\min_i x_i\bigr)
 +\bigl(\max_j t_j-\min_j t_j\bigr)\le1,              \tag{2.7}
\]

because the range of all pairwise sums is the sum of the two individual
ranges and is contained in two consecutive integers.

Suppose `1<=p<=h`.  Neither underlying binary word is constant.  Moreover,
its length-`h` cyclic window-count sequence cannot be constant.  Indeed,
if `(x_i)` were constant, then

\[
                         0=x_{i+1}-x_i=a_{i+h}-a_i     \tag{2.8}
\]

for every `i`.  Since

\[
                         \gcd(h,2h+1)=1,               \tag{2.9}
\]

translation by `h` is one cycle on `Z_b`, so (2.8) would make every
`a_i` equal.  This contradicts `1<=p<b`.  The same argument applies to
`(t_j)`.  Both ranges in (2.7) are therefore at least one, contradicting
(2.7).

Hence `p=0`.  Under the normalization (2.3), this says `P cap A` is empty.
As both `P` and `B` have size `b`, it follows that `P=B=Omega-A`.  Undoing
the optional complementation of `P` gives (2.2).

Conversely, if `A=P`, every atom cell has exactly `h` points in `P`; if
`A=Omega-P`, every cell has exactly `h+1` points in `P`.  In either case
the whole atom lies in `mathcal C(P)`.  \(\square\)

## 3. Consequences for trades and absorbers

### Corollary 3.1 (no cross-split exact trade inside one band)

Let `mathcal M_0,mathcal M_1` be two atom matchings with the same covered
vertex set `U`, and suppose

\[
                              U\subseteq\mathcal C(P).  \tag{3.1}
\]

Then every atom in both matchings uses the unordered split
`{P,Omega-P}`.

#### Proof

Every atom in either matching is a subset of its covered union `U`, hence
of `mathcal C(P)`.  Apply Theorem 2.1.  \(\square\)

In particular, if a completed fixed-band factor is replaced without
changing its covered vertex set, every replacement atom still uses the
same split.  Exact `q`-to-`q` trades supported inside the band cannot create
cross-split motion.

### Corollary 3.2 (required interface of a cross-split escape)

Every atom introduced from a different split contains at least one vertex
outside `mathcal C(P)`.  Consequently, if all atoms removed by an exchange
were contained in `mathcal C(P)`, the exchange must cover a formerly
uncovered outside-band vertex.  If in addition the exchange uses equally
many old and new atoms, cardinality forces it to release the same number of
formerly covered vertices, so its covered set moves across the band
boundary.

The theorem does not forbid such non-coverage-preserving absorbers.  It
identifies the boundary interface that every successful construction must
possess.

## 4. Relation to the crossing theorem

The separate fixed-band crossing theorem says every product atom meets
`mathcal C(P)` in at least `2b` vertices.  Theorem 2.1 supplies the opposite
extreme:

\[
 |E\cap\mathcal C(P)|=b^2
 \quad\Longleftrightarrow\quad
 \text{the atom uses the reference split}.            \tag{4.1}
\]

Thus a genuinely cross-split atom necessarily has vertices on both sides
of the fixed-band boundary.  Any cross-split absorber must coordinate those
inside-band conflicts with outside-band holes; a trade search restricted to
an exactly covered fixed band cannot find one.
