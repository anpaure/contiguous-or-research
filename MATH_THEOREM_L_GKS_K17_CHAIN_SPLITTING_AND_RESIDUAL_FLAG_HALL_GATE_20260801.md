# The GKS prime-necklace chain cover does not by itself give the `k=17` cap-three age factor: exact splitting debt, rooted packetization, and the automatic owner lift

Date: 2026-08-01  
Lane: L, direct-age-source static orbit compiler  
Status: primary-source audit, exact `k=17` chain census, a literal
cover-atlas obstruction, an automatic unguarded one-endpoint owner lift,
and an exact contracted rooted-packet model;
no transition-compatible flag cover or optimal word is claimed

## 0. Verdict

Griggs--Killian--Savage (GKS) prove that for prime `n` one may choose one
representative from every cyclic necklace so that the resulting
representative poset has a saturated symmetric-chain decomposition (SCD)
with a chain cover mapping.  For every nonroot chain `C`, its starter covers
one element of the parent chain `pi(C)`, and its terminator is covered by one
element of that parent chain.

At `n=17`, this supplies an excellent canonical quotient containment seed:
there are exactly 1430 chains, one rank-nine owner and one rank-eight target
per chain.  It does **not** prove the prescribed cap-three age-flag factor.

There are three exact reasons.

1. The native lower half of an early symmetric chain contains up to eight
   nonempty targets, while one age owner has only three marked slots including
   its rank-eight slot.  The exact native overflow is 553 target orbits.
2. Splitting every native lower chain into pieces of size at most three gives
   at least 1802 pieces, so at least 372 cross-chain fusions are necessary
   before only 1430 final owner packets remain.
3. The GKS **start-side cover rays** alone fail a six-target Hall cut at the
   root chain.  Its interior rank-two through rank-seven elements have only
   the native root owner in that certified atlas, whose non-rank-eight
   capacity is two.  Thus at least four non-cover containment placements are
   unavoidable.

The exact positive use of GKS is therefore as a seed for a larger packet
catalogue.  In the **unguarded static** problem, assignment of completed
packets to their current rank-nine owners is in fact automatic: match the
distinct rank-eight packet roots through the regular rank-eight/rank-nine
orbit-incidence multigraph.  The only static existence gate is the rooted
short-chain packetization of ranks two through eight.  Moreover, the
authenticated controlled GKS surgery now constructs its entire rank-six/
seven/eight layer; the residual static gate is only the rank-two--five
low-to-head attachment.  Successor ownership, transition compatibility,
voltage, and any external-carrier guards remain downstream.

## 1. What the GKS theorem actually supplies

Let `R_17` be the GKS representative poset.  For a nonconstant necklace its
representative is the rotation with lexicographically minimum finite block
code.  The Greene--Kleitman successor `tau` preserves this representative
choice in the range used by the construction.  On the nonconstant part the
chains are

\[
                         J_z=(z,\tau z,\ldots,\tau^{k(z)-1}z), \tag{1.1}
\]

and are saturated and symmetric.  GKS then add the two constant necklaces to
the separately extended root chain.

For a nonroot starter `z`, GKS delete its last one to obtain `alpha(z)` and
set

\[
                         \pi(J_z)=J_{\alpha(z)},       \tag{1.2}
\]

except for the stated rank-two attachment to the root chain.  Their proof
shows that `alpha(z)` is itself the parent starter and that the two chain
endpoints have the required cover relations.

The load-bearing scope is:

* (1.2) gives a rooted chain-cover tree and two endpoint cover edges per
  nonroot chain;
* it does not state that an arbitrary interior fragment of one chain is
  contained in the rank-nine member of another chain; and
* except for the stated rank-two-to-root attachment, its parent has starter
  rank one lower and is therefore a **longer** symmetric chain, not an
  automatic spare-capacity recipient.

The GKS result is cited from the primary paper:

> J. R. Griggs, C. E. Killian, C. D. Savage,
> “Venn Diagrams and Symmetric Chain Decompositions in the Boolean Lattice,”
> *Electronic Journal of Combinatorics* 11 (2004), R2,
> DOI `10.37236/1755`.

## 2. Exact `n=17` chain census

Let

\[
 N_0=N_{17}=1,
 \qquad N_s={1\over17}\binom{17}{s}
                  \quad(1\leq s\leq16).             \tag{2.1}
\]

For `0<=s<=8`,

\[
             (N_s)=(1,1,8,40,140,364,728,1144,1430). \tag{2.2}
\]

In any SCD, the number `q_a` of chains starting at rank `a` is

\[
                         q_a=N_a-N_{a-1},             \tag{2.3}
\]

where `N_(-1)=0`.  Hence the nonzero `k=17` start census is

\[
\begin{array}{c|rrrrrrrr}
a&0&2&3&4&5&6&7&8\\ \hline
q_a&1&7&32&100&224&364&416&286.
\end{array}                                            \tag{2.4}
\]

The sum is 1430.  Every chain contains one rank-eight element `Q_C` and one
rank-nine owner `T_C`, with `Q_C subset T_C`.

Let `ell_a` be the number of nonempty lower targets of ranks one through
eight on a chain starting at `a`.  Then

\[
                  \ell_0=8,
                  \qquad \ell_a=9-a\quad(a\geq1).     \tag{2.5}
\]

## 3. Native cap-three overflow and fragmentation

One age packet has three proper suffix slots, one of which is its rank-eight
target.  Keeping a GKS chain on its native owner therefore forces at least

\[
                         (\ell_a-3)_+                 \tag{3.1}
\]

of its lower targets to migrate.

### Proposition 3.1 (exact native migration floor)

The total native overflow is

\[
\begin{aligned}
 \Phi_{\rm GKS}
  &=1(8-3)+7(7-3)+32(6-3)+100(5-3)+224(4-3)\\
  &=\boxed{553}.                                      \tag{3.2}
\end{aligned}
\]

The short-chain spare is

\[
                         416+2(286)=988,              \tag{3.3}
\]

and `988-553=435`, exactly the scalar slack in the age certificate.

Thus scalar capacity is perfect but requires extensive cross-chain
reassignment.

### Proposition 3.2 (splitting alone creates too many pieces)

If each native lower chain is split into consecutive fragments of size at
most three, the minimum fragment count is

\[
\begin{aligned}
 F_{\rm split}
 &=1\lceil8/3\rceil
   +7\lceil7/3\rceil
   +32\lceil6/3\rceil
   +100\lceil5/3\rceil\\
 &\quad+224\lceil4/3\rceil
   +364\lceil3/3\rceil
   +416\lceil2/3\rceil
   +286\lceil1/3\rceil\\
 &=\boxed{1802}.                                      \tag{3.4}
\end{aligned}
\]

Since only 1430 final owners exist, at least

\[
                         1802-1430=372                \tag{3.5}
\]

fragment mergers must combine material from different original chains.
The SCD partition and scalar chain splitting do not provide these 372
comparabilities.

## 4. A sharp obstruction for the literal GKS cover-ray atlas

Let the root chain be

\[
 R_0\subset R_1\subset\cdots\subset R_{17},
 \qquad R_s=1^s0^{17-s}.                              \tag{4.1}
\]

Define the **GKS start-ray atlas** to contain:

1. every native lower containment `S subset Q_C subset T_C` along one GKS
   chain; and
2. containments obtained by iterating the certified start-side cover edges
   `alpha(z) subset z` up the chain-cover tree.

The terminator-side cover edge lies above the rank-nine owner (or covers a
rank-nine terminator when the child starts at rank eight) and points toward
the parent upper element.  By itself it certifies no additional strict-lower
target contained in the child's or parent's rank-nine owner, so it adds no
edge to this lower-host atlas.

In the explicit GKS mapping, every nonroot parent attachment lands at the
parent **starter**.  The exceptional attachment to the root occurs from a
rank-two starter and lands at `R_1`.  Therefore no iterated nonroot start ray
lands at any root interior element

\[
                         R_2,R_3,\ldots,R_7.           \tag{4.2}
\]

### Theorem 4.1 (root-interior Hall obstruction)

In the GKS start-ray atlas, the six targets in (4.2) have only the native
root owner.  Since that owner has only two non-rank-eight age slots,

\[
                         6>2|N(\{R_2,\ldots,R_7\})|=2. \tag{4.3}
\]

Consequently no chain splitting which uses only native containments and
iterated GKS start-cover rays can produce the prescribed cap-three factor.
At least four of the six root-interior targets require genuinely non-cover
owner containments.

#### Proof

Native SCD chains partition the representative poset, so (4.2) occurs
natively only on the root chain.  The GKS parent formula (1.2) says every
start-side cover target is a chain starter.  The only root starter is `R_0`,
and the one special nonroot-to-root lower attachment is `R_1`.  Thus no
other owner is certified by this atlas for any member of (4.2).  One final
age packet can select at most two of them in addition to its rank-eight
target, proving (4.3). \(\square\)

This theorem is scoped to the literal cover-ray atlas.  It does not say that
the targets in (4.2) lack other rank-nine supersets; the full cyclic
containment graph has many and satisfies normalized matching.  Those extra
edges are exactly the residual bank which must now be used.

## 5. Prescribed rank patterns and why the native SCD is insufficient

Ignoring the unmarked singleton repetitions, the certificate packet shapes
are

\[
\begin{split}
 &(1,6,8),(1,7,8),(2,7,8),(3,6,8),(3,7,8),\\
 &(4,7,8),(5,6,8),(5,7,8),(6,7,8),                  \tag{5.1}
\end{split}
\]

with the authenticated multiplicities.

If every target remained on its native SCD chain, then at each rank `s` all
`N_s` chains which meet rank `s` would have to receive a type supporting
`s`.  These chain families are nested as `s` grows.  The support families
in (5.1) are not nested: for example, the eight rank-two types are `C`,
whereas the forty rank-three types are `D,E`.  Hence even before the
cap-three overflow count, a native type placement cannot cover both layers.

The cover mapping supplies useful nested ancestor starters, but Theorem 4.1
shows that it does not supply every migration required by (5.1).

## 6. Automatic unguarded one-endpoint owner lift

Let `O_8` and `O_9` denote the rank-eight and rank-nine cyclic-orbit sets.
Both have size 1430.  Form the aligned-containment quotient **multigraph**

\[
                     G_{8,9}=(O_8,O_9;E),            \tag{6.1}
\]

where a parallel edge records a relative cyclic shift for which `Q subset T`.
Every node on either shore has multidegree nine: a rank-eight set has nine
rank-nine supersets, and a rank-nine set has nine rank-eight subsets.

### Theorem 6.1 (automatic current-owner matching)

The simple support of `G_{8,9}` has a perfect matching.  More strongly, the
9-regular multigraph is a disjoint union of nine perfect matchings.

#### Proof

For `X subset O_8`, the `9|X|` incident multiedges end in `N(X)`, while each
right node receives at most nine of them.  Hence

\[
                            |N(X)|\geq |X|.           \tag{6.2}
\]

Hall gives a perfect matching in the simple support.  Equivalently, bipartite
edge colouring decomposes the regular multigraph into nine one-factors.
\(\square\)

Choose an actual parallel edge for every matched orbit pair.  It records a
shift under which `Q subset T` literally.  Rotating the whole packet by that
shift then lifts the assignment equivariantly through all 17 physical phases.

A **full lower packet** before this lift is data

\[
                         K=(c;S_a\subset S_b\subset Q), \tag{6.3}
\]

where

* `c` is one of the nine certified types;
* `a=c_0`, `b=c_0+c_1`, and `|Q|=8`;
* `S_a,S_b,Q` are target-orbit representatives with the displayed literal
  inclusions; and
* for types `A,B`, the rank-one entry may be declared unmarked, with exactly
  one rank-one entry marked globally.

A **packetization** `Kcal` consists of 1430 such packets with the certified
type multiplicities which use every rank-two through rank-eight target orbit
exactly once and designate exactly one of the 436 rank-one suffix occurrences
as marked.  The other singleton suffixes are physical but unmarked.

Given a matching edge `Q subset T`, define

\[
 C_0=S_a,\qquad C_1=S_b\setminus S_a,\qquad
 C_2=Q\setminus S_b,\qquad C_3=T\setminus Q.         \tag{6.4}
\]

These are disjoint, have the prescribed age-type sizes, and `C_3` is the
unique oldest singleton.  Thus Theorem 6.1 proves:

\[
 \boxed{\text{every unguarded rooted packetization has a static current-owner
 assignment.}}                                      \tag{6.5}
\]

The word **unguarded** is load bearing.  The theorem assigns only the current
owner `T`.  It does not choose a successor `T'=Q union {beta}`, prove
`Q=T intersection T'`, or place these incidences on one Johnson cycle.  It
also ceases to be automatic when an absolute phase, oldest label, owner bin,
transition, or external trace guard deletes aligned-containment edges.  Such
variants require Hall again on the pruned graph.

## 7. The contracted rooted short-chain exact cover

The static model can now be written without owner variables.  Let `O_s` be
the rank-`s` orbit set.  Choose a 286-element set `H_6 subset O_6` of
rank-six **heads**, and partition

\[
\begin{array}{rcl}
 H_6&=&A_6\sqcup D_6\sqcup G_6,
       \qquad (|A_6|,|D_6|,|G_6|)=(139,20,127),\\
 O_7&=&B_7\sqcup C_7\sqcup E_7\sqcup F_7\sqcup H_7\sqcup I_7,\\
 &&(|B_7|,|C_7|,|E_7|,|F_7|,|H_7|,|I_7|)
       =(297,8,20,140,237,442).                      \tag{7.1}
\end{array}
\]

There are exactly 1430 heads.  The contracted data are:

1. a containment bijection from `H_6 sqcup O_7` to `O_8`;
2. containment bijections

   \[
   \begin{array}{c|c}
   \text{lower targets}&\text{head slots}\\ \hline
   O_2&C_7\\
   O_3&D_6\sqcup E_7\\
   O_4&F_7\\
   O_5&G_6\sqcup H_7\\
   O_6\setminus H_6&I_7;
   \end{array}                                      \tag{7.2}
   \]
3. one designated singleton occurrence in an `A_6` or `B_7` packet.

### Theorem 7.1 (two-layer packetization equivalence)

An unguarded prescribed-shape packetization exists if and only if the data
in (7.1)--(7.2) exist.

#### Proof

In every packet the rank `b=c_0+c_1` target is its head.  The type table says
that precisely `A,D,G` have rank-six heads, with total 286, and precisely
`B,C,E,F,H,I` have rank-seven heads, with total 1144.  Reading the lower
target in every non-`A,B` packet gives exactly (7.2); the counts on its two
shores are respectively `8,40,140,364,442`.  The packet roots give the first
bijection.  This proves necessity.

Conversely, append each lower target in (7.2) below its head, append each head
below its matched rank-eight root, and assign the type named by its bin.
Every rank-two through rank-seven orbit occurs once, every rank-eight root
occurs once, and all inclusions and type multiplicities are correct.  For
each `A` or `B` head choose any contained singleton; the rank-one orbit is
unique, and designating exactly one of these 436 occurrences completes the
marked lower deck. \(\square\)

### Corollary 7.2 (the authenticated GKS surgery closes the central layer)

For the explicit GKS decomposition, the head-to-root bijection in item 1
and the last row of (7.2) exist.

#### Proof

The native central census is

\[
             728\ (6<7<8),\qquad416\ (7<8),\qquad286\ (8). \tag{7.3}
\]

The controlled-surgery certificate matches the 286 rank-eight-start roots
to 286 distinct rank-six targets contained in them.  Move those targets out
of their native triples.  The result is

\[
             442\ (6<7<8),\qquad286\ (6<8),\qquad702\ (7<8), \tag{7.4}
\]

using every target at ranks six, seven, and eight once.  Take the 286 moved
rank-six targets as `H_6`; the 442 retained triples give the bijection
`O_6 setminus H_6 -> I_7`.  Every resulting rank-six or rank-seven head is
already contained in its displayed rank-eight root. \(\square\)

This is frozen independently in
`MATH_THEOREM_A_K17_GKS_RANK678_CONTROLLED_SURGERY_AND_LOW_FLAG_GATE_20260801.md`
(SHA-256 `e81937e57d3efebacb00aae8737a3e394ff895147d064aaf912d43c242ea833b`)
and its literal 286-edge certificate
`scratch/threadA_k17_gks_rank678_surgery_20260801.tsv`
(SHA-256 `921691cb12940fd05ef5d68938cd6fa3bdc953f5b12226ca0a39357315265baa`).
The frozen audit payload has SHA-256
`4270becd566084776e7046532322068a92d1b78def4853f3692d21e661f55771`
and status `PASS_K17_GKS_RANK678_CONTROLLED_SURGERY`.

Before inserting the controlled-surgery certificate, the exact first cut
for the generic head-to-root layer is the mixed-rank Hall family

\[
 |\Gamma_8(X_6)\cup\Gamma_8(X_7)|
       \geq |X_6|+|X_7|
 \quad(X_6\subseteq H_6,\ X_7\subseteq O_7).         \tag{7.5}
\]

Each row of (7.2) has its ordinary Hall inequalities in the corresponding
containment graph.  Those six matching families, coupled only through the
choice of the bins, are an exact smaller model.  Single-rank normalized
matching does not imply the mixed-rank cut (7.5).  Corollary 7.2 supplies
one certified solution of (7.5) and of the rank-six row.

Equivalently, let `P_c(Q)` be all literal nested chains of type `c` rooted at
one orbit `Q`, and put \(P(Q)=\bigcup_cP_c(Q)\).  Binary variables `z_P`
need only satisfy

\[
 \sum_{P\in P(Q)}z_P=1,
 \qquad \sum_{P:\,\operatorname{type}(P)=c}z_P=m_c,
 \qquad \sum_{\substack{P:\ s\in R(\operatorname{type}(P)),\\P_s=O}}z_P=1
                                                               \tag{7.6}
\]

for every root `Q`, type `c`, and target orbit `O` of ranks two through
seven.  There are no packet--owner variables.  Theorem 6.1 supplies the
current owner afterwards by any one of the nine incidence one-factors.

After Corollary 7.2, only four low/head systems remain:

\[
 O_2\longrightarrow C_7,\qquad
 O_3\longrightarrow D_6\sqcup E_7,\qquad
 O_4\longrightarrow F_7,\qquad
 O_5\longrightarrow G_6\sqcup H_7.                 \tag{7.7}
\]

For a fixed subdivision of the certified central packets into these type
bins, each arrow is ordinary aligned-containment Hall.  The exact remaining
static GKS gate is to choose the subdivision so all four Hall systems hold
simultaneously.  Theorem 4.1 proves that the literal cover-ray subatlas
cannot do this alone; off-tree Boolean containments are necessary.

## 8. Transition-compatible direct source

Theorems 6.1 and 7.1 are static.  The direct-age-source formulation
additionally orders the matched owners on a quotient Johnson cycle and
requires adjacent age partitions to satisfy the changing-owner survivor
inclusions, with the closing condition twisted by the total voltage.  The
static incidence one-factor may therefore have to be rechosen jointly with
that chronology; its unconditional existence is not chronology compatibility.

Once that transition-compatible flag exact cover exists, its appended
age-zero classes are the final source letters.  The lower suffix witnesses
are literal, so **no separate lower common-cap theorem remains**.

Common cap is a distinct gate only if the GKS/age packets are embedded into
an external pre-existing envelope carrier.  In that variant, the physical
target-to-cell bank must carry a free diagonal cyclic action and satisfy
quotient Hall, and it must also be trace guarded or pass the literal maximal-
cap equations.  Neither property follows from the GKS cover tree.

## 9. Exact frontier

The GKS seed changes the live question from arbitrary containment to a
structured augmentation problem:

\[
\boxed{
\begin{array}{c}
\text{prime-necklace SCD + cover tree}\quad\text{(proved)}\\
\Downarrow\\
\text{553 migrations, at least 372 cross-chain fusions,}\\
\text{and at least four non-cover root placements}\quad\text{(proved)}\\
\Downarrow\\
\text{rank-six/seven/eight controlled GKS surgery}\quad\text{(proved)}\\
\Downarrow\\
\text{rank-two--five low/head systems (7.7)}\quad\text{(open)}\\
\Downarrow\\
\text{automatic static current-owner lift}\quad\text{(proved)}\\
\Downarrow\\
\text{transition-compatible quotient flag cycle with twisted voltage}
   \quad\text{(open)}\\
\Downarrow\\
\text{direct literal lower source; upper-safe opening remains.}
\end{array}}
\]

Ordinary necklace SCD is therefore a strong static seed, not a proof of the
cap-three compiler.  The central controlled surgery is now exact.  The
residual static gate is four coupled low/head Hall systems, not packet--owner
Hall.  It is followed by the successor/transition system.
