# Hall 25: a strong \(C_8\) five-segment Shadow--Braid

Date: 2026-07-28

Status: proved structural theorem and exact Hall-25 compiler target.  This
note does not claim a realized strong-\(C_8\) occurrence.  Independently, a
two-braid six-cut compound has now been certified from Hall 25 to Hall 24;
see `THREAD_R_K15_HALL25_ODD_TURN_SIX_CUT_PORTAL_AUDIT_20260728.md`.

The complete resident, upper-safe `FF/RF/FR/RR` three-cut catalogue
has a strict local minimum at Hall deficiency \(25\).  The smallest
adjacent-shadow-exact boundary class which genuinely escapes that catalogue
contains a port-conserving strong \(C_8\).  It has the physical realization

\[
 A|B|C|D|E
 \longmapsto
 A|\overleftarrow D|\overleftarrow B|C|E.                 \tag{0.1}
\]

This move preserves the middle deck and both adjacent shadow multisets
algebraically.  Its deeper upper shadows and depth-three residence reduce
to four dependent seam collars.  On the audited Hall-25 compiler, one new
incidence in the first collar would open the literal augmenting path

\[
 21779-c_2-17683-c_1-21763-c_* .                          \tag{0.2}
\]

No **strong-\(C_8\)** occurrence satisfying all four collars and the
complete matching ledger is presently certified.  This no longer means
Hall 25 itself is a compound minimum: the separate six-cut portal compound
escapes it.

## 1. Hall-25 baseline

The authoritative chronology is
`scratch/k15_segment_braid_hall25.json`.  Its file SHA-256 is

```text
67a84c71f570dbdb8cdad5912b9bed333c4122e9237fed38d56690ad5bd0c473
```

and its comma-separated middle-path digest is

```text
0ddee21c54e6034e91f3e5b06d6ea2cef3c3a52a55539787d91d3fe2c9287df3
```

Independent reconstruction by
`scratch/audit_k15_segment_braid_descent.py` verifies:

- all \(6435\) rank-eight owners occur once in one Johnson path;
- depth-three residence holds;
- every upper support at depths \(q=1,\ldots,7\) is complete;
- the lower hole profile is \((4,19,4,1,0,0,0)\);
- the compiler graph has \(16383\) targets, \(19311\) cells, matching
  number \(16358\), and deficiency \(25\).

The complete one-move three-cut scan has

\[
551986\ {\rm Johnson},\qquad
12029\ {\rm resident},\qquad
9233\ {\rm upper\mbox{-}safe}
\]

candidates and no nonidentity state below Hall \(25\).  This is a
catalogue-local theorem.  It is now known to be defeated by bounded
lookahead: the certified score sequence is \(25\to25\to24\).

## 2. Flags are physical odd-graph turns

Let \(\Omega=[15]\).  A Johnson edge \(XY\), with
\(|X|=|Y|=8\), has the flag

\[
 R=X\cap Y,\qquad U=X\cup Y,
\]

where \((|R|,|U|)=(7,9)\) and \(R\subset U\).

### Lemma 2.1

Every such flag determines one unordered Johnson edge.  If

\[
 U\setminus R=\{x,y\},
\]

then the edge is

\[
 (R+x)(R+y).                                               \tag{2.1}
\]

Put \(C=\Omega\setminus U\).  Then \(|C|=6\),
\(C\cap R=\varnothing\), and the same flag is the unordered turn

\[
 (C+x)-R-(C+y)                                             \tag{2.2}
\]

in \(O_7=KG(15,7)\).  Complementing the two outside vertices of
(2.2) recovers the two middle owners in (2.1).

#### Proof

The two rank-eight sets strictly between \(R\) and \(U\) are \(R+x\)
and \(R+y\), and they differ by one exchange.  The sets \(C+x,C+y\)
are rank-seven sets disjoint from \(R\); their complements are
\(R+y,R+x\).  \(\square\)

Thus an adjacent-shadow trade reassigns complete odd-graph turns, not two
independent marginal symbols.

## 3. Primitive exact four-seam boundaries

For a flag \(f=(R,U)\), write

\[
\rho(f)={\bf e}_R,\qquad
\upsilon(f)={\bf e}_U,\qquad
\omega(f)={\bf e}_{R+x}+{\bf e}_{R+y},
\quad U\setminus R=\{x,y\}.                               \tag{3.1}
\]

Let \(z\) be the signed new-minus-old multiset of four seam flags in a
deck-exact reassembly.  Exact adjacent lower and upper multiplicities mean

\[
 \rho(z)=0,\qquad \upsilon(z)=0,                           \tag{3.2}
\]

while conservation of the eight cut endpoints forces

\[
 \omega(z)=0.                                              \tag{3.3}
\]

### Theorem 3.1

Cancel flags present on both sides and suppose the remaining signed
boundary is simple.  If it has at most four positive flags and satisfies
(3.2)--(3.3), its nontrivial part is one of:

1. an alternating \(C_6\), with the fourth seam cancelled;
2. one alternating \(C_8\) satisfying (3.3), called a strong \(C_8\);
3. two alternating flag \(C_4\)'s with opposite owner-boundary vectors.

In particular one isolated flag rectangle cannot be the boundary of a
deck-exact segment braid.

#### Proof

Flags are edges of the bipartite inclusion graph on rank-seven rows and
rank-nine columns.  Equation (3.2) balances positive and negative degree at
every vertex, so the signed graph decomposes into alternating even
circuits.  With at most four positive edges, the only nontrivial positive
mass partitions are \(3\), \(4\), and \(2+2\), apart from cancellations.

For the remaining assertion, let a flag rectangle have two distinct rows
and two distinct columns.  The two rank-seven rows cannot have union of
size nine, since then there is only one rank-nine column containing both;
their union therefore has size eight and their intersection has size six.
Consequently, for a rank-six \(K\) and distinct
\(a,b,c,d\notin K\), its rows are \(K+a,K+b\) and its columns are
\(K+a+b+c,K+a+b+d\).  Its owner boundary, up to sign, is

\[
[K+a+c]+[K+b+d]-[K+a+d]-[K+b+c],                          \tag{3.4}
\]

which is nonzero because these four middle owners are distinct.  Hence an
isolated \(C_4\) violates (3.3), while two rectangles must have exactly
opposite vectors (3.4).  \(\square\)

This theorem classifies the stronger adjacent-multiset-exact class.
Upper-support-only four-cut moves can have other boundary profiles.

## 4. The common-core strong \(C_8\)

The construction works in \(J(n,r)\) for \(n\ge r+3\).  Choose

\[
K\in\binom{[n]}{r-2}
\]

and distinct \(a_0,a_1,a_2,a_3,c\notin K\), with indices modulo four.
Set

\[
\begin{aligned}
R_i&=K+a_i, &
U_i&=K+a_i+a_{i+1}+c,\\
P_i&=K+a_i+a_{i+1}, &
F_i&=K+a_i+c.
\end{aligned}                                             \tag{4.1}
\]

### Theorem 4.1 (port-conserving strong \(C_8\))

The seam matchings

\[
E^-=\{P_iF_i:i\in\mathbb Z_4\},\qquad
E^+=\{P_iF_{i+1}:i\in\mathbb Z_4\}                        \tag{4.2}
\]

are Johnson matchings on the same eight distinct middle owners.  Moreover,

\[
\begin{aligned}
P_i\cap F_i&=R_i, & P_i\cup F_i&=U_i,\\
P_i\cap F_{i+1}&=R_{i+1}, & P_i\cup F_{i+1}&=U_i.
\end{aligned}                                             \tag{4.3}
\]

Thus the switch fixes every upper column \(U_i\), cyclically permutes the
four lower rows, and preserves the complete middle endpoint deck and both
adjacent shadow multisets.

#### Proof

All sets have the asserted ranks.  Distinctness of the five displayed
labels makes the eight \(P_i,F_i\) distinct.  Equations (4.3) are immediate
from their two added-label sets; they prove Johnson adjacency and the
row/column claims.  Both sides of (4.2) are perfect matchings of the same
eight owners.  \(\square\)

### Theorem 4.2 (five-segment realization)

Suppose the old path edges occur in the oriented order

\[
F_0\to P_0,\qquad P_1\to F_1,\qquad
P_2\to F_2,\qquad P_3\to F_3.                             \tag{4.4}
\]

The four cuts give

\[
\begin{aligned}
A&=(\ldots,F_0), & B&=(P_0,\ldots,P_1),\\
C&=(F_1,\ldots,P_2), & D&=(F_2,\ldots,P_3),\\
E&=(F_3,\ldots).
\end{aligned}                                             \tag{4.5}
\]

Then the sequence in (0.1) is a vertex-simple Johnson path with the same
global endpoints and middle deck.  Its interfaces are

\[
F_0P_3,\qquad F_2P_1,\qquad P_0F_1,\qquad P_2F_3,          \tag{4.6}
\]

which are exactly the four edges of \(E^+\).

#### Proof

Reversal preserves every internal undirected Johnson edge.  Reading (0.1)
gives (4.6), and Theorem 4.1 proves those four adjacencies.  The five
retained lists partition the old path, while \(A,E\) retain their
orientations.  \(\square\)

All four old and four new edges are distinct.  Since a three-cut braid
changes at most three unordered seams, this construction is genuinely
outside the exhausted Hall-25 catalogue.

It is an ambient odd-turn/flag \(C_8\), not a claim that the natural PBBS
\(M_1\) matching contains a \(C_8\): that matching is proved \(C_8\)-free.
PBBS supplies the turn coordinates and dependent chronology; an occurrence
in the evolved Hall-25 path must still be exhibited.

## 5. Exact four-collar ledger

For \(q\ge1\), let \({\cal O}_q,{\cal N}_q\) be the old and new starts of
length-\(q+1\) windows crossing at least one seam.  For every mask \(Z\),

\[
\begin{aligned}
\mu^\cup_{q,Z}(T')-\mu^\cup_{q,Z}(T)
&=\sum_{s\in{\cal N}_q}
 {\bf1}\!\left[\bigcup_{j=0}^{q}T'_{s+j}=Z\right]\\
&\quad-\sum_{s\in{\cal O}_q}
 {\bf1}\!\left[\bigcup_{j=0}^{q}T_{s+j}=Z\right],          \tag{5.1}
\end{aligned}
\]

and the same identity holds for intersections.

#### Proof

Every window internal to a retained segment has one translated or reversed
mate.  Union and intersection ignore reversal.  Exactly the crossing
windows remain.  \(\square\)

If all five segments exceed \(q\) vertices and the seams are
\(q\)-separated, then

\[
|{\cal O}_q|=|{\cal N}_q|=4q.                             \tag{5.2}
\]

Without separation, (5.1), counting a multi-seam window once, remains
exact.  Upper support through \(q=7\) survives exactly when

\[
\mu^\cup_{q,Z}(T)+\Delta^\cup_{q,Z}\ge1                   \tag{5.3}
\]

for every required \(Z\).  Under separation there are
\(4\sum_{q=1}^7q=112\) old and \(112\) new crossing-window evaluations.

For PBBS turns these signatures are dependent functions of the ordered
missing-colour word.  In the exact PBBS notation,

\[
F_i^{(q)}
=\bigcap_{h<q}B_{i+h}
=B_i\setminus\{z_{2i+1},\ldots,z_{2i+2q-3}\}.              \tag{5.4}
\]

Thus the four collars must be evaluated from the actual chronology, not
from independent seam signs.

Write \(T'_{j+1}=T'_j-\alpha_j+\beta_j\).  Depth-three residence holds
exactly when

\[
\beta_s\ne\alpha_t                                        \tag{5.5}
\]

for every \(0<t-s\le3\) whose transition interval crosses a new seam.  Four
mutually separated seams give \(9\) comparisons each, hence \(36\).
Reversal creates no internal test because it preserves coordinate-run
lengths.  The retained-interior charging argument also gives

\[
|\nu_H(T')-\nu_H(T)|\le4                                  \tag{5.6}
\]

for the maximum edge-disjoint packing of short residence intervals.

At compiler depth \(D=3\), a row-\(j\) cell, \(j=0,1,2\), starting at
\(p\) depends only on middle owners in

\[
[p-6,p+j+3].                                               \tag{5.7}
\]

One seam affects at most \(9+j\) starts in that row.  After canonical
transport of internal profiles, a four-seam braid has

\[
|B^-|\le120,\qquad |B^+|\le120,                            \tag{5.8}
\]

or at most \(240\) old-plus-new boundary profiles.

## 6. Exact Hall-25 DM currents

Let \(G\) be the Hall-25 compiler graph and \(S\) the left shore reachable
from unmatched targets by alternating paths under the independently
reconstructed maximum matching.  Then

\[
|S|=1320,\qquad |N_G(S)|=1295,                             \tag{6.1}
\]

with rank histogram \((8,72,359,881)\) in ranks \(4,5,6,7\) and
sorted-target digest

```text
89449e9fe9fb085c96ec911e3a9fad61f1e0409e4c6ef0133ed72677eb273e83
```

The connected component sizes \((|S_i|,|T_i|)\) of
\(G[S,N_G(S)]\) are

\[
\begin{gathered}
(165,163),\quad5(161,160),\quad2(160,159),\quad(5,4),\\
2(3,2),\quad6(2,1),\quad7(1,0).                           \tag{6.2}
\end{gathered}
\]

Thus the excess vector is \((2,1,\ldots,1)\in\mathbb Z^{24}\).  The seven
isolated targets are

\[
2575,5801,13616,13620,17738,21641,29776.                  \tag{6.3}
\]

For a proposed graph \(G'\), put

\[
J(X)=|N_{G'}(X)|-|N_G(X)|.                                \tag{6.4}
\]

### Proposition 6.1 (component-union cuts)

If \(h(G')\le24\), then for every \(I\subseteq[24]\),

\[
J\!\left(\bigcup_{i\in I}S_i\right)
\ge \sum_{i\in I}e_i-24
=1-\left(25-\sum_{i\in I}e_i\right),\qquad
e_i=|S_i|-|T_i|.                                          \tag{6.5}
\]

In particular \(J(S)\ge1\); after omitting a unit-excess component the
current must remain nonnegative, and after omitting the excess-two
component it must remain at least \(-1\).

#### Proof

Every neighbour of \(S_i\) lies in its component \(T_i\), so a union of
components has old defect \(\sum_{i\in I}e_i\).  Its new defect is that
quantity minus \(J\).  Requiring it to be at most \(24\) gives (6.5).
\(\square\)

These component cuts are necessary, not sufficient.  The exact formula is

\[
h(G')
=25-\min_X\left(25-(|X|-|N_G(X)|)+J(X)\right).             \tag{6.6}
\]

After profile cancellation, (5.8) makes \(J\) a signed function of at most
\(120\) old and \(120\) new profiles.  Equivalently, if \(M\) is an old
maximum matching and \(r\) of its edges disappear, the new graph needs
\(r+1\) vertex-disjoint augmenting paths relative to the surviving
matching in order to gain one rank.

## 7. A one-incidence Hall-24 certificate

Three old physical cells are

\[
\begin{array}{c|c|c|c}
\text{cell ID}&(\text{row},\text{start})&\Gamma(c)&M\text{-status}\\ \hline
13365&(2,490)&\{17683,21779\}&17683\text{ matched},\\
6928 &(1,490)&\{17665,17667,21761,21763\}&21763\text{ matched},\\
8714 &(1,2276)&\{1283,5379,17667,21763\}&\text{right-unmatched}.
\end{array}                                                \tag{7.1}
\]

Call them \(c_2,c_1,c_*\).  Target \(21779\) is left-unmatched.  Every
edge in (0.2) already exists except \(17683-c_1\); the two matching edges
on the path are \(c_2-17683\) and \(c_1-21763\).

### Theorem 7.1 (literal augmentation)

Let \(G'\) be the compiler graph of a legal common chronology.  If every
edge of the displayed old maximum matching \(M\) survives in \(G'\), the
other four edges of (0.2) survive, and \(17683-c_1\) is added, then

\[
\nu(G')\ge16359,\qquad h(G')\le24.                         \tag{7.2}
\]

#### Proof

The endpoints \(21779,c_*\) are unmatched by \(M\), and (0.2) alternates
outside and inside \(M\).  Toggling along it replaces two matched edges by
three.  \(\square\)

Retaining only the five local incidences is insufficient if other edges of
\(M\) disappear.  In that case the lost matching edges require disjoint
recoveries or the equivalent contracted-rank certificate.

At \(c_1\), the maximal erosion states, envelope, and mandatory set are

\[
(E_{490},E_{491})=(20739,21762),\qquad
\operatorname{env}=21763,\qquad
\operatorname{mand}=17665.                               \tag{7.3}
\]

A target \(X\) is adjacent exactly when

\[
X\subseteq\operatorname{env},\qquad
\operatorname{mand}\subseteq X,\qquad
E_{490}\cap X\ne\varnothing,\quad E_{491}\cap X\ne\varnothing.        \tag{7.4}
\]

For \(X=17683\), only the envelope test fails, and

\[
17683\setminus21763=\{5\}                                 \tag{7.5}
\]

in one-based coordinate notation.  A sufficient collar target is therefore:

1. make the new envelope contain \(17683\), restoring coordinate \(5\)
   without losing another required coordinate;
2. keep the new mandatory set inside \(17683\);
3. keep both erosion states incident with \(17683\);
4. retain \(M\), or supply all lost-edge recoveries.

This is a common-word incidence condition, not a separate rankwise pin.

## 8. A direct four-cut transport fails

For \(b\in\{526,527\}\), define from the Hall-25 path \(T\)

\[
Q_b=T[:488]\,[T_{2031}]\,T[b:2031]\,
\overleftarrow{T[488:b]}\,T[2032:].                       \tag{8.1}
\]

Both are deck-exact Johnson paths.  Their old cuts are
\(488,b,2031,2032\), and their new seams are

\[
488,489,2520-b,2032.                                      \tag{8.2}
\]

They fail all three remaining interfaces.

First, both delete the unique upper-\(q=1\) witness \(22411\).  Its old
edge \(21387-22283\) has lower intersection \(21259\).  The replacement
\(21387-21275\) retains that intersection but has union \(21403\), and no
new seam has union \(22411\).

Second, the residence violations, in
`(zero-based coordinate,start,end)` form, are

```text
b=526: (3,2030,2031), (4,1992,1993), (4,2032,2033),
       (5,489,490),   (9,1993,1995)
b=527: (3,2030,2031), (4,1991,1993), (4,2032,2033),
       (5,489,489),   (14,486,488)
```

Third, both compiler reconstructions fail at middle start \(489\),
coordinate \(6\): the owner contains coordinate \(6\), but none of its
four eligible carrier positions contains it.  The erosion states there are

```text
b=526: 21002, 4874, 4890, 4882
b=527:  4619, 4875, 4883, 4627
```

For \(b=526\) this is the first carrier failure.  For \(b=527\) there is
already an earlier failure at start \(486\), coordinate \(15\); the
coordinate-\(6\) failure at start \(489\) is nevertheless also present.

These paths are generic singleton/block transports, not strong \(C_8\)'s:
their old and new row/column flag multisets differ.  Their failure isolates
the need for companion balanced seams and does not obstruct Theorem 4.1.

## 9. Precise remaining certificate

A Hall-25 escape in the strong-\(C_8\) class is now exactly one tuple

\[
(K,a_0,a_1,a_2,a_3,c;p_0,p_1,p_2,p_3)                    \tag{9.1}
\]

such that:

1. the four old edges at the ordered cuts have port pattern (4.4);
2. the materialized chronology is the five-segment path (0.1);
3. its four dependent PBBS collars satisfy (5.3) through \(q=7\) and all
   residence inequalities (5.5);
4. its at-most-\(120\)-profile compiler boundary retains \(M\) and creates
   the incidence of Theorem 7.1, or supplies the complete replacement
   augmentations for every lost matched edge.

Deck exactness, path topology, and both adjacent shadow multisets then need
no further audit: they follow from Theorems 4.1--4.2.  No tuple satisfying
all four items is presently certified.  The three-cut local minimum does
not cover this class, while the failed transports in Section 8 lack its
strong-\(C_8\) balance.

The proved boundary is therefore exact: a first new PBBS/odd-turn atom
beyond the three-cut class is an integral five-segment strong \(C_8\), and
its decisive lower-compiler objective is the physical augmentation (0.2),
subject to the full four-collar and matching-retention ledgers.  The actual
known Hall-25 escape instead uses two coupled three-cut braids, equivalently
one six-cut/seven-segment port circulation; it does not realize the strong
\(C_8\) template.
