# Tetrahedral segment braids give an exact one-unit Hall descent at `k=15`

Date: 2026-07-28

Status: proved general seam-coboundary theorem, proved exact tetrahedral
Shadow--Braid identity, and verified finite descent `29 -> 28` on the frozen
`k=15` carrier.  This is not yet an iterative descent theorem: the remaining
selection lemma must control the signed boundary current on every
near-critical Hall shore.

## 1. General three-cut segment braid

Let

\[
                    Q=(Q_0,\ldots,Q_{N-1})
\]

be a simple path in the Johnson graph `J(n,r)`.  Choose

\[
                         0<a<u\le v<N-1
\]

and write

\[
 A=Q[0,a),\quad B=Q[a,u),\quad C=Q[u,v+1),\quad D=Q[v+1,N).
\tag{1.1}
\]

Put

\[
 L=Q_{a-1},\quad b_0=Q_a,\quad b_1=Q_{u-1},\quad
 c_0=Q_u,\quad c_1=Q_v,\quad R=Q_{v+1}.
\tag{1.2}
\]

For an orientation sign, `F` means forward and `R` means reversed.

### Theorem 1.1 (endpoint criterion)

The reordered deck

\[
                         Q'=A\,C^\epsilon B^\eta D
\tag{1.3}
\]

is a Johnson path if and only if the following new seam edges exist:

\[
\begin{array}{c|c}
(\epsilon,\eta)&\text{required new seams}\\ \hline
FF&L\sim c_0,\ c_1\sim b_0,\ b_1\sim R,\\
RF&L\sim c_1,\ c_0\sim b_0,\ b_1\sim R,\\
FR&L\sim c_0,\ c_1\sim b_1,\ b_0\sim R,\\
RR&L\sim c_1,\ b_0\sim R.
\end{array}
\tag{1.4}
\]

In the last row, `c_0~b_1` is the old middle seam traversed backwards.
Under (1.4), `Q'` is deck-exact, retains the endpoints of `Q`, and changes
only three adjacent undirected edges; the `RR` case changes only two.

#### Proof

Every vertex of `Q` occurs once in (1.3), so the deck and endpoints are
unchanged.  Every edge internal to `A,B,C,D` is retained, possibly with its
orientation reversed.  The only unverified adjacencies are therefore the
three joins in (1.3), which are exactly the entries of (1.4).  Necessity is
immediate from those same joins.  \(\square\)

## 2. Exact multiscale seam coboundary

For `Phi` equal to union or intersection, define

\[
 T^\Phi_{q,i}(Q)=\Phi(Q_i,Q_{i+1},\ldots,Q_{i+q}).
\tag{2.1}
\]

For a set of cuts `C`, put

\[
 \operatorname{Cross}_q(\mathcal C)
 =\{i:\text{some }c\in\mathcal C\text{ satisfies }i<c\le i+q\}.
\tag{2.2}
\]

The old and new cut sets are

\[
 \mathcal C_- =\{a,u,v+1\},\qquad
 \mathcal C_+ =\{a,a+|C|,v+1\}.
\tag{2.3}
\]

### Theorem 2.1 (literal trace coboundary)

For every mask `S` and every `q>=1`,

\[
\begin{aligned}
 m^+_{q,\Phi}(S)-m^-_{q,\Phi}(S)
  ={}&\sum_{i\in\operatorname{Cross}_q(\mathcal C_+)}
       \mathbf1[T^\Phi_{q,i}(Q')=S]\\
   &-\sum_{i\in\operatorname{Cross}_q(\mathcal C_-)}
       \mathbf1[T^\Phi_{q,i}(Q)=S].
\end{aligned}
\tag{2.4}
\]

Consequently, at most `3q` old and `3q` new trace occurrences contribute,
and

\[
             \|m^+_{q,\Phi}-m^-_{q,\Phi}\|_1\le6q.
\tag{2.5}
\]

For `RR`, treating `BC` as one reversed block improves these bounds to
`2q,2q,4q`.

#### Proof

A length-`q+1` window not crossing a cut lies in one of `A,B,C,D`.  It has
one identical transported window after the braid.  Reversal changes the
order of its entries but not their union or intersection.  These internal
windows cancel bijectively, leaving exactly (2.4).  Each isolated cut is
crossed by at most `q` starts, which gives (2.5).  \(\square\)

Thus “only three seams change” is literal at `q=1`.  At depth `q`, as many
as `3q` crossing windows on each side change.  Internal shadows are
preserved as unlabelled multisets, not at their original positions or with
their original owners.

## 3. Tetrahedral Shadow--Braid normal form

The successful move has a clean endpoint explanation.

### Theorem 3.1 (tetrahedral exchange)

Let `K` have size `r-2`, and let `p,q,s,t` be four distinct coordinates
outside `K`.  Suppose the six boundary states in (1.2) are

\[
\begin{array}{lll}
L=K+\{q,t\},&b_0=K+\{q,s\},&b_1=K+\{p,s\},\\
c_0=K+\{s,t\},&c_1=K+\{p,q\},&R=K+\{p,t\}.
\end{array}
\tag{3.1}
\]

Then the `RF` braid \(A\,\operatorname{rev}(C)\,B\,D\) is Johnson-valid.  Its old seam
`(intersection,union)` pairs are

\[
\begin{aligned}
 &(K+q,\ K+\{q,s,t\}),\\
 &(K+s,\ K+\{p,s,t\}),\\
 &(K+p,\ K+\{p,q,t\}),
\end{aligned}
\tag{3.2}
\]

whereas its new pairs are

\[
\begin{aligned}
 &(K+q,\ K+\{p,q,t\}),\\
 &(K+s,\ K+\{q,s,t\}),\\
 &(K+p,\ K+\{p,s,t\}).
\end{aligned}
\tag{3.3}
\]

Hence every immediate lower port is fixed at its seam, while the three
upper ports undergo a 3-cycle.  Both complete `q=1` shadow multisets are
preserved exactly, but the lower--upper incidence pairing is recoupled.

#### Proof

Each required edge in the `RF` row of (1.4) joins two two-subsets of
`{p,q,s,t}` sharing one coordinate, so it is a Johnson edge.  Direct
intersection and union of the pairs gives (3.2)--(3.3).  \(\square\)

This is a suspended clean six-state packet: the six boundary states are all
two-subsets of four coordinates above the fixed core `K`, while the long
segments between them supply the exact deck transport.

## 4. The frozen `k=15` certificate

Take

\[
                         (a,u,v)=(471,2327,5456)
\tag{4.1}
\]

and the `RF` orientation.  Thus

\[
              A\mid B\mid C\mid D\longmapsto A\mid\operatorname{rev}(C)\mid B\mid D,
\tag{4.2}
\]

with `|B|=1856`, `|C|=3130`, old cuts `471,2327,5457`, and new cuts
`471,3601,5457`.

The six boundary masks are

\[
 (L,b_0,b_1,c_0,c_1,R)=(7277,6381,6319,7341,6255,7215).
\tag{4.3}
\]

In one-based coordinate notation, (3.1) holds with

\[
 K=\{1,3,4,6,12,13\},\qquad(p,q,s,t)=(2,7,8,11).
\tag{4.4}
\]

The old seam pairs are

\[
                 (6253,7405),\ (6317,7343),\ (6191,7279),
\tag{4.5}
\]

and the new pairs are

\[
                 (6253,7279),\ (6317,7405),\ (6191,7343).
\tag{4.6}
\]

### Theorem 4.1 (exact carrier and shadow audit)

The stored Hall-28 word is exactly the braid (4.2) applied to the frozen
Hall-29 word.  It has the following properties.

1. It is a permutation of all 6,435 rank-eight states and every consecutive
   pair is Johnson-adjacent.
2. It has no internal coordinate run shorter than four.  Its maximal
   four-window erosion is everywhere nonempty and has rank histogram

   \[
                     5:6432,\quad6:2,\quad7:2,\quad8:2.
   \]

3. The complete adjacent lower and upper **multiplicity vectors** are
   unchanged.
4. Every rank-`8+q` upper target remains covered for `1<=q<=7`.
5. The lower support hole counts at `q=1,2,3` remain respectively
   `4,21,4`; the four `q=1` holes are

   \[
                         \{5801,7267,8877,13620\}.
   \tag{4.7}
   \]

#### Proof

Materializing (4.2) gives byte-for-byte the stored middle path.  The deck,
adjacency, run, and erosion claims follow by literal scan.  Equations
(4.5)--(4.6), together with Theorem 2.1, prove item 3.  Literal support scans
of the at most `3q` seam windows prove items 4--5.  All equalities are
recomputed by the accompanying verifier.  \(\square\)

The deeper upper statement is support preservation, not multiplicity
preservation.  Endpoint Johnson tests alone do not imply it.

## 5. Exact census and its correction

The native exhaustive census is

\[
\begin{array}{c|rrrr|r}
 &FF&RF&FR&RR&\text{total}\\ \hline
\text{endpoint-safe}&141312&182775&183298&43097&550482\\
\text{resident}&1620&1797&1800&6796&12013\\
\text{upper-support-safe}&712&895&897&6739&9243.
\end{array}
\tag{5.1}
\]

The aggregate `12,013/9,243` is correct for the implemented catalogue, but
the `RR` column consists of ordinary two-cut reversals: the dummy middle cut
does not create a third changed seam.  Genuine three-seam totals are

\[
                         5217\quad\text{and}\quad2504.
\tag{5.2}
\]

The exhibited `RF` move is a genuine three-cut braid.

## 6. Hall-29 to Hall-28

Let `G^-` and `G^+` be the exact depth-three physical compiler graphs before
and after the braid.  Their common left shore consists of all 16,383
nonempty masks of rank at most seven.  Each graph has

\[
                     6438+6437+6436=19311
\tag{6.1}
\]

physical cells, with the full forced-carrier mandatory masks included.

### Theorem 6.1 (finite Hall descent)

The exact matching data are

\[
\begin{array}{c|cc}
 &G^-&G^+\\ \hline
\text{maximum matching}&16354&16355\\
\text{deficiency}&29&28\\
\text{zero-candidate targets}&7&7.
\end{array}
\tag{6.2}
\]

The zero set is unchanged:

\[
             \{2575,5801,13616,13620,17738,21641,29776\}.
\tag{6.3}
\]

In particular, the improvement does not come from creating a candidate for
a formerly zero-degree target.

Two independent exact matching implementations give (6.2).  Alternating
reachability from the unmatched left vertices supplies a minimum vertex
cover of the same size, so these are exact maxima, not merely displayed
matchings.

## 7. Exact boundary-bank descent theorem

The Hall change is genuinely local after cells are compared by their full
target-neighbourhood signatures.

Let two bipartite graphs have the same left shore `L`.  Cancel equal right
cells by the multiset of their complete neighbourhood signatures, obtaining

\[
                       G^-=H\sqcup B^-,\qquad G^+=H\sqcup B^+.
\tag{7.1}
\]

For \(X\subseteq L\), define

\[
 n_F(X)=|\{c\in F:N(c)\cap X\ne\varnothing\}|,
 \qquad I_B(X)=n_{B^+}(X)-n_{B^-}(X).
\tag{7.2}
\]

### Theorem 7.1 (signed Hall current)

Put

\[
 \delta^-(X)=|X|-n_H(X)-n_{B^-}(X),\qquad
 d=\max_X\delta^-(X),\qquad
 \sigma(X)=d-\delta^-(X).
\tag{7.3}
\]

Then

\[
             D(G^+)=\max_{X\subseteq L}\bigl(\delta^-(X)-I_B(X)\bigr).
\tag{7.4}
\]

In particular, the braid decreases deficiency by at least one if and only
if

\[
                    I_B(X)\ge1-\sigma(X)
                    \qquad\text{for every }X\subseteq L.
\tag{7.5}
\]

It is blocked precisely when some shore satisfies

\[
                         I_B(X)\le-\sigma(X).
\tag{7.6}
\]

If both boundary banks have size at most `b`, only shores with
`sigma(X)<=b` can block descent.

#### Proof

The deficiency form of Hall's theorem is

\[
 D(G)=\max_X\bigl(|X|-|N_G(X)|\bigr).
\]

Using the disjoint cell decomposition (7.1) gives

\[
 |X|-|N_{G^+}(X)|
 =\delta^-(X)-I_B(X),
\]

which proves (7.4).  Since all quantities are integral, `D(G^+)<=d-1` is
equivalent to (7.5).  Negating (7.5) gives (7.6).  Finally
`I_B(X)>=-b`, so a shore of slack greater than `b` cannot satisfy (7.6).
\(\square\)

There is an equivalent matching-rank form.  Define

\[
                 \operatorname{cap}_H(B)=\nu(H\sqcup B)-\nu(H).
\tag{7.7}
\]

Then

\[
 D(G^+)-D(G^-)
 =\operatorname{cap}_H(B^-)-\operatorname{cap}_H(B^+).
\tag{7.8}
\]

Thus the correct local potential is contracted occurrence capacity, not raw
target degree or total incidence.

### Corollary 7.2 (conditional descent algorithm)

Let a class of resident, shadow-safe carriers be closed under a specified
catalogue of segment braids.  If every deficient member admits a braid
satisfying (7.5), repeated braiding reaches Hall deficiency zero after at
most the initial deficiency many steps.

#### Proof

Each selected braid preserves membership in the class and lowers the
nonnegative integer deficiency by at least one.  \(\square\)

## 8. The concrete boundary current

For (4.1), exact signature cancellation gives

\[
                  |H|=19274,\qquad |B^-|=|B^+|=37.
\tag{8.1}
\]

The matching ranks are

\[
 \nu(H)=16336,\qquad
 \operatorname{cap}_H(B^-)=18,\qquad
 \operatorname{cap}_H(B^+)=19.
\tag{8.2}
\]

Equation (7.8) now proves `29 -> 28` directly.

For the old canonical deficient DM shore `S`,

\[
 |S|=1524,\qquad n_H(S)=1491,qquad
 n_{B^-}(S)=4,qquad n_{B^+}(S)=5.
\tag{8.3}
\]

Its old/new boundary-cell degrees into `S` are

\[
                         \{7,4,4,4\}\longrightarrow\{4,4,4,2,2\}.
\tag{8.4}
\]

Writing a cell as `(row depth,start)`, the exact old boundary neighbours in
`S` are

\[
\begin{array}{c|l}
(2,472)&6308,6309,6372,6373\\
(2,473)&20644,20645,20708,20709\\
(2,474)&16550,16551,16614,16615\\
(2,5454)&449,451,453,455,459,461,463,
\end{array}
\tag{8.5}
\]

and the new ones are

\[
\begin{array}{c|l}
(1,3602)&6308,6309\\
(2,474)&451,455,459,463\\
(2,3602)&6372,6373\\
(2,3603)&20580,20581,20708,20709\\
(2,3604)&16486,16487,16614,16615.
\end{array}
\tag{8.6}
\]

Thus the braid increases the number of usable capacity-one cells by one
while decreasing total incidence by three, collision excess by four, and
pair-collision potential by nineteen.  It is a cell-fission improvement,
not a marginal-support improvement.

The decisive split is

\[
 \{6308,6309,6372,6373\}
 \quad\longrightarrow\quad
 \{6308,6309\},\ \{6372,6373\}
\tag{8.7}
\]

on two distinct physical cells.  Nevertheless

\[
                    \deg_{G^-}(6308)=\deg_{G^+}(6308)=14,
\tag{8.8}
\]

and the same `+1` current persists on \(S\setminus\{6308\}\).  Therefore target 6308 is
not the cause of the descent and must not be imposed as a necessary target
for this lane.

The naive geometric claim `19,275 common + 36 boundary` is false for the
full compiler graph.  Mandatory carrier footprints alter nine apparently
internal cell profiles.  Exact full-signature cancellation recovers eight
elsewhere and gives the rigorous `19,274+37` decomposition (8.1).

## 9. What remains for an iterative theorem

The result proves a nontrivial descent direction and an exact criterion for
all future steps.  It does not prove that such a direction always exists.
The precise missing statement is:

> **Tetrahedral braid selection lemma (unproved).**  Every deficient
> resident carrier with complete protected upper support admits an
> endpoint-valid tetrahedral segment braid whose boundary current satisfies
> (7.5) simultaneously for every Hall shore of slack at most its boundary-
> bank size, while retaining the required lower and residence constraints.

The inverse of (4.2) is itself deck-exact, resident, upper-support-safe, and
lower-hole-neutral, but reverses the Hall improvement.  Hence deck,
residence, and shadow-support invariants alone cannot orient descent.  A
proof must use the contracted cell-capacity current or an equivalent
alternating-path/DM-shore statement.

## 10. Scope audit

1. Internal trace multisets are preserved, but physical positions,
   controller cells, owners, and ordered chronology are transported or
   reversed.  Those changes are exactly why Hall capacity can improve.
2. At `q>1`, upper **support** is preserved in the census; multiplicities
   can change.  The exact `q=1` lower and upper multiplicities are preserved
   by the tetrahedral identity.
3. Residence is not implied by endpoint Johnson legality.  Only runs
   incident with a new seam can change, and they were checked separately.
4. The finite descent is for the exact frozen `k=15` compiler graph.  It is
   not an all-`k` theorem and does not prove Hall deficiency zero.
5. The aggregate census includes the degenerate `RR` two-cut subfamily; the
   genuine three-cut counts are (5.2).

## 11. Reproduction

Run

```text
clang++ -O3 -DNDEBUG -std=c++20 \
  scratch/search_k15_segment_braid_native.cpp \
  -o /tmp/search_k15_segment_braid_native

/tmp/search_k15_segment_braid_native \
  scratch/k15_doubletrans_05_213_hall29.json 32767

python3 scratch/audit_k15_tetrahedral_segment_braid_hall28.py
```

The authoritative artifacts are

```text
scratch/search_k15_segment_braid_native.cpp
scratch/k15_segment_braid_hall28.json
scratch/audit_k15_tetrahedral_segment_braid_hall28.py
```

At audit time their first two SHA-256 hashes were respectively

```text
b927a37e2530380aa01420c1543e1b1ba60b04b6f0e525ee8014cd4db668ec13
a11aaa927367dc70cf57e4e550c1b7d0a81e480c2c3801a45381795851c4c283
```
