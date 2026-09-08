# An owner-preserving all-shuffle hierarchy inside tensor packets

Date: 2026-07-26

Method: pure mathematics only.

## 0. Result

The tensor packet admits an exact owner-preserving all-shuffle
construction at the level of direction catalogues.

Tensor \(r\) copies of the eight-coordinate pair-frame associator and fix
one shore. Its six local \(C_4\)'s partition the 24 local owners. Taking
Cartesian products gives

\[
 6^r
\]

pairwise owner-disjoint cells, each isomorphic to

\[
 Q_2^{\square r}=Q_{2r}.
\]

Among them are \(4^r\) **main cells** using the four big local squares in
every associator block. All these main cells have the same \(2r\) physical
pair directions.

Assume \(d=2r\) is a power of two. On \(Q_d\), use the recursive
half-depth rainbow factor: it partitions every vertex into isometric
\(C_{2d}\)'s, and its forward and reverse labelled shadow maps are
injective for every \(q\leq d/2=r\). Conjugating this factor by any
coordinate permutation \(\sigma\in S_d\) preserves the exact vertex
partition and permutes its direction catalogue by \(\sigma\).

There is a set \(\mathscr S\subseteq S_d\) of size

\[
 |\mathscr S|
 \leq
 (2r\log 2+2)\left(\frac94\right)^r
 <4^r
\]

for all sufficiently large \(r\), such that, simultaneously for every
\(q\leq r\), the direction catalogues of the conjugate factors
\(\{F_d^\sigma:\sigma\in\mathscr S\}\) contain every
\(q\)-subset of the common \(d\)-direction frame.

Assign the conjugates in \(\mathscr S\) to distinct main cells, use any
conjugate on the remaining main cells, and use the base recursive factor on
all other product cells. Since the cells are owner-disjoint, their union is
one exact cycle factor of the whole tensor packet. It has:

1. every tensor owner exactly once;
2. only physical isometric \(C_{4r}\)'s;
3. exact within-cell two-sided shadow injectivity through \(q=r\);
4. the complete physical direction catalogue
   \[
    \binom{[2r]}q
   \]
   on the common main-cell frame, simultaneously for all \(q\leq r\).

Thus the realized depth-\(q\) catalogue entropy is

\[
 \log_2\binom{2r}{q}
 =2rH_2\!\left(\frac q{2r}\right)+O(\log r)
 \geq2q-O(\log r),
\]

because \(H_2(x)\geq2x\) on \(0\leq x\leq1/2\). This meets the sharp
cross-sector \(2q\) profile-entropy threshold, up to logarithmic terms,
without changing any owner.

The construction does not prove coefficient one. It gives complete
direction support and exact local shadow injectivity, but not cross-cell
physical-shadow injectivity. Moreover, the complete catalogue lies in one
fixed special-pair frame, so the fixed-frame type-capacity obstruction
still applies. The remaining theorem must coordinate the conjugates with
the associator shores and packet embeddings so that equal physical shadows
from different cells are suppressed.

## 1. The tensor packet contains many disjoint cubes

In one associator block \(B_i\), fix either shore
\(\varepsilon_i\in\{0,1\}\). The local factor consists of six disjoint
isometric \(C_4\)'s:

* four main squares, one for each reservoir orientation;
* two reservoir squares.

Each \(C_4\) is a physical \(Q_2\). The six cycles partition the same 24
local middle owners.

For a fixed shore vector

\[
 \varepsilon=(\varepsilon_1,\ldots,\varepsilon_r),
\]

choose one of the six local squares in every block and take their Cartesian
product. The resulting graph is

\[
 C_4^{\square r}=Q_2^{\square r}=Q_{2r}.
\tag{1.1}
\]

There are \(6^r\) such choices.

### Lemma 1.1 (exact tensor-cell partition)

The \(6^r\) cells in (1.1) are pairwise vertex-disjoint and partition the
entire tensor owner support \(\mathcal V^r\).

#### Proof

Every local owner belongs to exactly one of the six local cycles. Therefore
an owner tuple belongs to the unique product cell obtained by taking its
local owner cycle in every coordinate block. Cartesian products of
different local choices are disjoint. \(\square\)

In each block, the four main squares have the same two physical pair-flip
directions; only their fixed reservoir orientation differs. Hence:

### Lemma 1.2 (common-frame main cells)

The \(4^r\) product cells obtained by choosing a main square in every block
are owner-disjoint \(Q_{2r}\)'s with one common set

\[
 \mathcal D=\{p_{i,0},p_{i,1}:1\leq i\leq r\}
\tag{1.2}
\]

of \(2r\) physical pair directions.

The shore vector changes the pair frame in each associator block, but for
one fixed shore vector the frame (1.2) is common to all main cells.

## 2. The recursive rainbow factor and its conjugates

Let \(d=2^t\). Define a neighbor permutation \(F_d:Q_d\to Q_d\)
recursively. Let \(F_1\) toggle its only coordinate. If \(d=2a\) and
\(x=(u,v)\in Q_a\times Q_a\), put

\[
 F_{2a}(u,v)=
 \begin{cases}
  (F_a(u),v),&|u|+|v|\equiv0\pmod2,\\
  (u,F_a(v)),&|u|+|v|\equiv1\pmod2.
 \end{cases}
\tag{2.1}
\]

### Theorem 2.1 (recursive half-depth rainbow factor)

The cycles of \(F_d\):

1. partition \(Q_d\);
2. all have length \(2d\);
3. have direction word \(\pi\pi\) for a permutation \(\pi\) of the
   \(d\) coordinates;
4. have injective forward and reverse labelled shadow maps for every
   \(q\leq d/2\).

#### Proof sketch

Every move changes total parity, so the two halves in (2.1) move
alternately, and

\[
 F_{2a}^{2s}(u,v)=(F_a^s(u),F_a^s(v)).
\tag{2.2}
\]

Induction gives exact period \(4a=2(2a)\) and shows that every coordinate
occurs exactly once in each half-period.

For an even window \(q=2s\), its labelled shadow splits into the two
depth-\(s\) labelled shadows in the child cubes. For \(q=2s+1\), the two
deleted-coordinate cardinalities reveal which child moved first, after
which the data split into depths \(s+1\) and \(s\). Induction recovers the
starting vertex. The inverse recursion has the same form, proving the
reverse assertion. \(\square\)

For \(\sigma\in S_d\), let the same symbol denote the coordinate
automorphism of \(Q_d\), and define

\[
 F_d^\sigma=\sigma F_d\sigma^{-1}.
\tag{2.3}
\]

When a tensor cell is physically embedded, this automorphism need not come
from one permutation of the ambient ground coordinates. It is the
bit-coordinate automorphism of that particular product cube: permute its
\(d\) binary phase coordinates and then regroup the output bits into the
original local \(Q_2\)'s. Every output bit string is still one owner of the
same product cell, and every one-bit edge is still the corresponding
physical pair flip. This is sufficient for an exact physical cycle factor.

### Lemma 2.2 (owner-preserving conjugation)

Every \(F_d^\sigma\) is an exact cycle factor of the same vertex set
\(Q_d\), with the same cycle lengths and the same two-sided injectivity
range. If \(\mathcal A_q\subseteq\binom{[d]}q\) is the collection of
depth-\(q\) direction sets occurring in \(F_d\), then the corresponding
collection for \(F_d^\sigma\) is

\[
 \sigma\mathcal A_q.
\tag{2.4}
\]

#### Proof

Coordinate permutation is a cube automorphism. It bijects vertices and
edges, conjugates cycles to cycles, and applies \(\sigma\) to every
direction word and every labelled shadow. \(\square\)

This is the basic owner-preserving shuffle operation: the owners do not
move between cells or acquire multiplicity; only their cycle ownership and
direction hierarchy change.

## 3. The intrinsic catalogue of one rainbow factor

The recursive injectivity already forces exponentially many direction
sets.

### Lemma 3.1 (intrinsic direction entropy)

For every \(q\leq d/2\),

\[
 \boxed{|\mathcal A_q|\geq2^q.}
\tag{3.1}
\]

#### Proof

For a fixed \(q\)-direction set \(D\), a labelled lower shadow has at most
\(2^{d-q}\) outside orientations. The forward shadow map is injective on
all \(2^d\) starts, so

\[
 2^d\leq|\mathcal A_q|2^{d-q}.
\]

This gives (3.1). \(\square\)

One cell therefore carries at least \(q\) bits of direction-catalogue
entropy at depth \(q\), while retaining exact owner coverage.

## 4. Covering every direction set by conjugates

The next elementary orbit-cover lemma turns the intrinsic \(2^q\) catalogue
into the complete \(\binom dq\) catalogue.

### Lemma 4.1 (random conjugate cover)

Let \(\mathcal A\subseteq\binom{[d]}q\) have size \(a>0\). There are
permutations \(\sigma_1,\ldots,\sigma_K\in S_d\), with

\[
 K\leq
 \left\lceil
 \frac{\binom dq}{a}
 \left(\log\binom dq+1\right)
 \right\rceil,
\tag{4.1}
\]

such that

\[
 \bigcup_{j=1}^K\sigma_j\mathcal A=\binom{[d]}q.
\tag{4.2}
\]

#### Proof

For uniform \(\sigma\in S_d\) and fixed
\(J\in\binom{[d]}q\), transitivity gives

\[
 \Pr(J\in\sigma\mathcal A)=\frac a{\binom dq}.
\]

For \(K\) independent permutations, the probability that \(J\) is never
covered is at most

\[
 \exp\!\left(-\frac{Ka}{\binom dq}\right).
\]

With \(K\) as in (4.1), the expected number of uncovered \(J\)'s is less
than one. Hence some choice covers them all. \(\square\)

Apply Lemma 4.1 to \(\mathcal A_q\) for each \(1\leq q\leq d/2\), and take
the union of the resulting permutation families. By (3.1), the total
number \(K_{\leq d/2}\) of required conjugates satisfies

\[
\begin{aligned}
 K_{\leq d/2}
 &\leq
 \sum_{q=1}^{d/2}
 \frac{\binom dq}{2^q}
 \left(\log\binom dq+2\right)\\
 &\leq
 (d\log 2+2)
 \sum_{q=0}^{d}\binom dq2^{-q}\\
 &=(d\log 2+2)\left(\frac32\right)^d.
\end{aligned}
\tag{4.3}
\]

For \(d=2r\), this is

\[
 K_{\leq r}
 \leq(2r\log 2+2)\left(\frac94\right)^r
 <4^r
\tag{4.4}
\]

for all sufficiently large \(r\).

The logarithms in (4.1)--(4.4) are natural. Their bases affect only the
displayed polynomial factor.

## 5. One exact tensor factor carrying the full catalogue

We now install the conjugates without changing any owner.

### Theorem 5.1 (owner-preserving all-shuffle tensor factor)

Let \(d=2r\) be a power of two and let \(r\) be sufficiently large. Fix
one shore vector of the \(r\)-fold tensor associator. There is one exact
cycle factor \(\mathfrak F\) of its full owner support such that:

1. every component of \(\mathfrak F\) is a physical isometric
   \(C_{2d}=C_{4r}\);
2. every middle owner occurs in exactly one component;
3. inside every tensor \(Q_d\)-cell, both labelled shadow maps are
   injective for every \(q\leq r\);
4. among the \(4^r\) common-frame main cells, the physical
   \(q\)-direction catalogue is exactly
   \[
    \binom{\mathcal D}q
   \]
   for every \(q\leq r\).

#### Proof

Use Section 4 to choose a simultaneous conjugate family
\(\mathscr S\) of size less than \(4^r\). Assign its members injectively to
distinct main cells from Lemma 1.2. On the cell assigned \(\sigma\), install
the factor \(F_d^\sigma\), using the common physical direction
identification (1.2). On every unassigned main cell and on every non-main
cell, install any copy of \(F_d\) after choosing its local cube-coordinate
identification.

By Lemma 1.1 the cells are vertex-disjoint and cover the tensor support.
By Lemma 2.2 every installed object is an exact factor of its cell into
physical isometric \(C_{2d}\)'s. Their union is therefore an exact factor,
proving assertions 1 and 2. Lemma 2.2 and Theorem 2.1 give assertion 3.

For fixed \(q\leq r\), the assigned main cells carry the catalogues
\(\sigma\mathcal A_q\) for the simultaneous family \(\mathscr S\).
Their union is \(\binom{\mathcal D}q\) by (4.2). No direction set outside
\(\binom{\mathcal D}q\) exists on these common-frame cells, proving
assertion 4. \(\square\)

The phrase “without changing owners” is literal: the tensor cells are the
same fixed disjoint owner sets before and after the conjugate choices, and
each chosen factor partitions its assigned cell exactly.

## 6. Hierarchical realization of the conjugations

Fix a balanced binary tree on the \(d\) coordinate directions. At a node
with \(a\) left and \(b\) right leaves, an \((a,b)\)-shuffle interleaves
the child orders while preserving their internal orders.

Every permutation \(\sigma\in S_d\) has a unique recursive description:
its restrictions give the two child permutations, and its left/right
membership word gives the parent shuffle. Thus the conjugates used in
Theorem 5.1 can be generated by recursively varying:

1. the coordinate split seen at each node;
2. the two child order factors;
3. the interleaving shuffle at the parent.

Conjugation is important here. An arbitrary shuffle need not itself tile a
parent product torus by translates of one path. Instead, the complete
recursive factor is first constructed and then transported by the cube
automorphism \(\sigma\). Exact cycle partition is automatic at every
cell, so no unproved torus-tiling assertion is being used.

The geometric hierarchy height is \(O(\log d)\), while its effective branch
entropy can be as large as \(\log_2(d!)\). Theorem 5.1 uses only the
subfamily required by (4.3).

## 7. Catalogue entropy and the \(2q\) threshold

Theorem 5.1 realizes every \(q\)-subset of a common \(d=2r\) direction
frame. Therefore

\[
 \log_2|\mathcal E_q|
 =\log_2\binom{2r}{q}.
\tag{7.1}
\]

Writing \(x=q/(2r)\leq1/2\), the binary entropy estimate gives

\[
 \log_2\binom{2r}{q}
 =2rH_2(x)+O(\log r).
\tag{7.2}
\]

Concavity of \(H_2\) and the chord joining
\((0,0)\) to \((1/2,1)\) give

\[
 H_2(x)\geq2x,
\]

so

\[
 \boxed{
 \log_2|\mathcal E_q|\geq2q-O(\log r).
 }
\tag{7.3}
\]

At the endpoint \(q=r\),

\[
 \log_2\binom{2r}{r}
 =2r-\frac12\log_2(\pi r)+O(1/r)
 =2q-O(\log r).
\tag{7.4}
\]

This identifies how the sharp entropy is assembled:

* one recursive rainbow factor contributes at least \(2^q\) intrinsic
  direction sets, or \(q\) bits;
* approximately \(\binom{2r}{q}/2^q\) conjugate placements distribute that
  intrinsic catalogue over the full orbit;
* their combined catalogue has entropy
  \(\log_2\binom{2r}{q}\geq2q-O(\log r)\).

Equivalently, since one cyclic order exposes at most \(2r\)
\(q\)-intervals, the exact factor contains at least

\[
 \frac{\binom{2r}{q}}{2r}
\]

effective order profiles at depth \(q\). Its profile entropy is therefore
\(2q-O(\log r)\), meeting the global
\(L+\log_2P\geq2q-o(q)\) threshold.

## 8. What this does and does not solve

### Proved

1. All-shuffle coordinate hierarchies can be realized by exact
   owner-preserving cycle factors, by conjugating the recursive rainbow
   factor rather than trying to tile every product torus with an arbitrary
   monotone path.
2. A single exact tensor factor can deploy enough different conjugates on
   disjoint cells to contain every \(q\)-direction set simultaneously for
   all \(q\leq r\).
3. Every installed cell factor is two-sided shadow-injective through
   \(r\).
4. The realized direction/profile entropy reaches the sharp
   \(2q-O(\log r)\) scale.

### Still open

1. **Cross-cell collisions.** Shadow injectivity is proved inside each
   \(Q_{2r}\) cell. Equal physical lower or upper targets may occur in two
   different tensor cells.
2. **Fixed-frame type capacity.** The complete catalogue in Theorem 5.1
   uses the one common special-pair frame \(\mathcal D\). It cannot by
   itself repair the fixed-coordinate-pair type imbalance.
3. **Associator-shore synchronization.** Different shore vectors provide
   different pair frames on the same tensor owner support, but the local
   overlap component is connected. One cannot simply use one shore on
   some owners and the other shore on the rest without a new exact
   component decomposition.
4. **Global packet selection.** Tensor packets embedded in different
   ground-coordinate locations overlap in owners. Choosing the cellwise
   factors above across all packets remains an integral packing problem.
5. **Radius census.** The Catalan radius-pure allocation needed by the
   coefficient-one SCD compiler has not been imposed.

The exact successor is therefore a cross-cell assignment theorem:

> Choose the conjugate label of every tensor cell, together with compatible
> associator shores and packet embeddings, so that the union remains an
> exact owner factor and the physical shadow maps have total collision
> excess \(o(W)\) through every fixed Gaussian window.

The present theorem removes the inner hierarchy/order obstruction. Any
remaining failure of the tensor-associator lane must come from physical
cross-cell collisions, frame mixing, or integral packet ownership—not from
insufficient owner-preserving \(q\)-direction entropy.
