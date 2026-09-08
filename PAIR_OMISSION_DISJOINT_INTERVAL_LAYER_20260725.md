# Disjoint adjacent interval charts tensorize exactly

Date: 2026-07-25

## 1. Setup

Put \(n=2m+1\), with \(m\ge3\), and fix disjoint coordinate pairs

\[
P_1,P_2,\ldots,P_m,
\]

and use the first-avoided-pair token matching with this priority order.  For
each odd \(j\), put

\[
A_j=P_j,\qquad B_j=P_{j+1},
\]

let \(\theta_j\) exchange \(A_j\) and \(B_j\) coordinatewise, and choose
the local factors so that

\[
F_{B_j}=\theta_jF_{A_j}.
\tag{1.1}
\]

The changed lower domain is

\[
\mathcal D_j=\left\{S:\ |S|=m-1,\quad
 S\cap(A_j\cup B_j)=\varnothing,\quad
 S\cap P_h\ne\varnothing\ (h<j)\right\}.
\tag{1.2}
\]

Break \(\mathcal D_j\) into maximal consecutive intervals in the rows of
\(F_{A_j}\).  On each interval independently choose either all old
\(A_j\)-tokens or all conjugate \(B_j\)-tokens.  The one-block legality and
floor-descent theorem is proved in
`MATH_AUDIT_PAIR_OMISSION_INTERVAL_CORNERS_AND_FLOOR_DESCENT_20260725.md`.

The point of this note is that all odd blocks may be used at once.  This was
not contained in the earlier single-chart statement.

All multidepth assertions below use

\[
1\le H\le m-2,
\tag{1.3}
\]

so that every upper cyclic window used in packetization is proper.

## 2. Owner categories

For a set \(Y\) which avoids at least one priority pair, write

\[
\kappa(Y)=\min\{h:Y\cap P_h=\varnothing\}.
\]

### Lemma 2.1

If \(S\in\mathcal D_j\), then the owner of either token choice over \(S\)
has category in \(\{j,j+1\}\).

### Proof

The old owner \(Y_A(S)\) contains \(S\), meets every \(P_h\) for \(h<j\),
and avoids \(A_j\).  Hence \(\kappa(Y_A(S))=j\).

The conjugate owner

\[
Y_B(S)=\theta_jY_A(S)
\]

still meets every earlier pair and avoids \(B_j\).  If the one coordinate
of \(Y_A(S)\setminus S\) lies in \(B_j\), then \(Y_B(S)\) meets \(A_j\)
and has category \(j+1\).  Otherwise it avoids \(A_j\) as well and has
category \(j\).  These are the only cases.  \(\square\)

The domains \(\mathcal D_j\) for distinct \(j\)'s are disjoint: a member
of \(\mathcal D_j\) avoids \(P_j\), whereas a member of \(\mathcal D_k\)
with \(k>j\) must meet \(P_j\).

## 3. Exact product legality

### Theorem 3.1

Choose interval bits independently in every odd block

\[
(P_1,P_2),(P_3,P_4),\ldots.
\]

Every joint corner is a lower-saturating, middle-injective integral token
matching.

### Proof

Every lower target lies in at most one changed domain, so lower saturation
is automatic.  Within one block, arbitrary tokenwise choices have distinct
middle owners by the single-chart mixed-owner lemma.

For two different odd indices \(j\ne k\), Lemma 2.1 confines the two owner
families to the disjoint category sets

\[
\{j,j+1\}\quad\text{and}\quad\{k,k+1\}.
\]

They therefore cannot share an owner.  Finally, a changed choice cannot
collide with the unchanged background: its old version coexists with the
background in the coherent first-avoided matching, and its conjugate
version coexists with the same background in the coherently swapped
matching for that block.  Thus every owner is used at most once.  \(\square\)

## 4. Tensorized floor descent

For odd \(j\), let \(\mathscr I_j\) be its physical interval family, and
let

\[
\mathcal C_j=
\sum_{q=1}^H w_q^+
\sum_{U:\,U\cap B_j\ne\varnothing}
\binom{\mu_{j,q,U}}2
\tag{4.1}
\]

be the activated collision count in its changed upper stratum.  Different
odd blocks have disjoint first-avoided upper strata, so their flag
innovations have disjoint target-coordinate supports.

### Theorem 4.1

For independent fair interval bits in all odd blocks,

\[
\boxed{
\mathbb E\mathcal Q_w(M_\varepsilon)
=\mathcal Q_w(M_0)-\sum_{\substack{j\text{ odd}\\j<m}}\mathcal C_j.}
\tag{4.2}
\]

Consequently some integral joint corner satisfies

\[
\boxed{
\mathcal Q_w(M_\varepsilon)
\le \mathcal Q_w(M_0)-\sum_{\substack{j\text{ odd}\\j<m}}\mathcal C_j.}
\tag{4.3}
\]

### Proof

The single-block floor identity applies after conditioning on every other
block, because those other innovations lie in disjoint lower domains,
owner categories, and upper target strata.  Iterating conditional
expectation over the odd blocks proves (4.2), and (4.3) follows.  \(\square\)

If \(r_j=|\mathscr I_j|\), the same tensorization gives

\[
J(M_\varepsilon)-J(M_0)
\le2\sum_{\substack{j\text{ odd}\\j<m}}r_j.
\tag{4.4}
\]

The exact carrier estimates from the single-chart audit imply

\[
\sum_{\substack{j\text{ odd}\\j<m}}r_j
=O\!\left(\frac{W\log^2m}{m}\right).
\tag{4.5}
\]

Hence, uniformly for

\[
H=o(m/\log^2m),
\]

the entire odd layer has

\[
H\,[J(M_\varepsilon)-J(M_0)]=o(W).
\tag{4.6}
\]

Since the coherent base also has
\(J(M_0)=O(W\log^2m/m)\), every joint corner satisfies

\[
2J(M_\varepsilon)
\le 2J(M_0)+4\sum_{j\text{ odd}}r_j
=O(W\log^2m/m).
\tag{4.6a}
\]

In particular, for \(H=\lceil L\sqrt m\rceil\) with fixed \(L\), the
total run-endpoint count is \(o(W/H)\) and
\(HJ(M_\varepsilon)=o(W)\).

### Proposition 4.2 (the first-upper layer is exactly invisible)

For every adjacent block \(j\),

\[
\boxed{\mathcal C_{j,1}=0.}
\tag{4.7}
\]

In fact, every interval corner has exactly the same depth-one upper
factorial-floor energy as the coherent base.

### Proof

Suppose two distinct token occurrences with lower endpoints \(S,T\) have
the same first-upper target \(U\).  Their collars

\[
C_S=U\setminus S,\qquad C_T=U\setminus T
\]

have size two.  For either occurrence, deleting a collar point from \(U\)
gives one of its two adjacent rank-\(m\) windows.  If
\(C_S\cap C_T\ne\varnothing\), deleting a common collar point therefore
identifies an adjacent rank-\(m\) window occurrence for the two tokens.
Exactness puts their starts in the same row at distance at most one.  At
distance one their proper length-\((m+1)\) windows are distinct, while at
distance zero they are the same occurrence.  Hence distinct occurrences
satisfy

\[
C_S\cap C_T=\varnothing.
\]

If \(S,T\in\mathcal D_j\) and \(U\cap B_j\ne\varnothing\), then both
lower endpoints avoid \(B_j\), so

\[
\varnothing\ne U\cap B_j\subseteq C_S\cap C_T,
\]

a contradiction.  Therefore every activated first-upper target has
multiplicity at most one, proving (4.7).

More strongly, the nonfixed changed targets form disjoint two-point orbits
\(\{U,\theta_jU\}\), with one moving occurrence on each orbit.  If the
base loads on such an orbit are \((a,b)\), the coherent endpoint both moves
that occurrence and exchanges the two coordinates.  Thus
\((a-1,b+1)=(b,a)\), so \(a=b+1\).  An arbitrary interval choice either
leaves \((b+1,b)\) fixed or exchanges it to \((b,b+1)\).  Every
coordinate-separable factorial-floor energy is invariant under this
exchange, orbit by orbit.  \(\square\)

## 5. Exact remaining limitation

Theorem 4.1 is one legal many-chart layer, not yet a contraction theorem.
It charges only duplicate pairs activated inside one of the disjoint
two-category blocks.  In particular it fixes every lower flag, and an upper
duplicate whose two missing \((q+1)\)-sets have no coordinate in the
relevant partner pair is invisible.  Proposition 4.2 shows that it is
completely flat at \(q=1\); all positive descent starts at \(q=2\).

The even adjacent layer overlaps the owner-category sets of the odd layer,
so its legality after an already chosen mixed odd corner does not follow
from Theorem 3.1.  A subsequent common-base theorem does prove simultaneous
legality of *all* adjacent blocks and identifies their negative neighboring
Gram terms; see
`MATH_ATTACK_PAIR_PRIORITY_OVERLAPPING_LAYER_JOINED_GRAM_20260725.md`.
What remains unproved is a uniform charged-coverage inequality for that
joined Gram, together with a recentering theorem which renews the atlas
after a mixed corner.

No constant-one conclusion is claimed here.

## 6. Independent-audit addendum

The tensorization above is correct.  In the background argument of
Theorem 3.1, “background” is understood to mean targets outside
\(\bigcup_j\mathcal D_j\); tokens changed in another block are separated
by the disjoint owner-category pairs \(\{j,j+1\}\).  Likewise, every
nonzero upper innovation of block \(j\) is supported only on first-avoided
categories \(\{j,j+1\}\), which proves the cross-block orthogonality used
in Theorem 4.1.

The audit also strengthens “odd indices” to every independent set
\(\Lambda\subseteq\{1,\ldots,m-1\}\) with \(|j-k|\ge2\).  The proof and
the pointwise depth-one flatness are recorded in full in the audit below.

The complete audit, including exact run-endpoint accounting and the
conditional iteration recurrence, is in
`MATH_AUDIT_PAIR_OMISSION_DISJOINT_INTERVAL_LAYER_20260725.md`.

For the recursively conjugate
chain \(F_{j+1}=\theta_jF_j\), arbitrary interval choices in *all*
overlapping adjacent blocks are simultaneously legal.  Neighboring-block
Gram terms have the opposite sign and produce an additional joined-target
descent.  This is proved in
`MATH_ATTACK_PAIR_PRIORITY_OVERLAPPING_LAYER_JOINED_GRAM_20260725.md`.
