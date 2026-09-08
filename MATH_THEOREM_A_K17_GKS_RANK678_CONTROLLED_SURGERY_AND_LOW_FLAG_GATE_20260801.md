# `k=17`: controlled GKS surgery at ranks `6,7,8` and the exact residual low-flag gate

Date: 2026-08-01  
Lane: A, Catalan-orbit age flags from a prime-necklace SCD  
Status: unconditional exact central-rank construction for the explicit GKS
decomposition; exact two-vertex obstruction to the strict chain-cover-only
atlas; the lower-rank flag attachment and changing-owner chronology remain
open

## 0. Result

Let `J` be the Griggs--Killian--Savage (GKS) symmetric-chain
decomposition of the `n=17` necklace-representative poset.  At the central
three lower ranks its native chain census is

\[
 728\ (6<7<8),\qquad 416\ (7<8),\qquad 286\ (8).
 \tag{0.1}
\]

The connected age certificate instead needs

\[
 \boxed{442\ (6<7<8),\qquad286\ (6<8),\qquad702\ (7<8).}
 \tag{0.2}
\]

There is an exact controlled surgery from (0.1) to (0.2).  Match every one
of the 286 chains born at rank eight to a distinct rank-six element lying
below its rank-eight starter, remove that rank-six element from its native
central triple, and attach it to the rank-eight starter.  A literal
286-edge matching has been materialized and independently replayable.

The strict two-step GKS chain-cover map does **not** supply this matching.
Its 286 rank-eight starters have only 205 distinct rank-six grandparents;
35 grandparents have two such descendants and 23 have three.  In
particular two starters with the same grandparent form a smallest Hall
obstruction, `2>1`.  Any successful surgery uses at least

\[
                         286-205=81                 \tag{0.3}
\]

non-grandparent containment links.  The full necklace-containment graph
has the required matching.

This settles the entire rank-`6,7,8` static split and permits the exact nine
type multiplicities to be placed on the resulting three shapes.  It does
not yet attach all rank-`2,...,5` target orbits, satisfy the connected age
word, or produce an upper-safe physical opening.

## 1. The GKS input and its exact central census

For prime `n`, GKS select one representative of every cyclic necklace by
the least finite block code and apply the Greene--Kleitman successor to
obtain an SCD with a chain-cover map.  If a nonroot chain starts at `z`, its
parent starts at

\[
                         \alpha(z),                  \tag{1.1}
\]

where `alpha` changes the last one in `z` to zero.  Thus a chain born at
rank eight has the certified start-side ray

\[
             \alpha^2(z)\subset\alpha(z)\subset z,  \tag{1.2}
\]

of ranks `6,7,8`.

Write

\[
 N_s={1\over17}{17\choose s}\quad(1\le s\le16).
\]

The central values are

\[
                         N_6=728,quad N_7=1144,
                         \quad N_8=N_9=1430.         \tag{1.3}
\]

The number of SCD chains born at rank `s` is `N_s-N_(s-1)`.  Hence 728
chains meet rank six, 416 additional chains are born at rank seven, and
286 additional chains are born at rank eight.  This proves (0.1).

## 2. Abstract central-surgery lemma

Let an SCD of a rank-symmetric poset have the central form (0.1).  Denote
the chains meeting rank six by `L`, the chains born at rank seven by `M`,
and those born at rank eight by `H`.  For `C in L`, write

\[
             Q_6(C)<Q_7(C)<Q_8(C)<T_9(C),            \tag{2.1}
\]

and use the analogous notation on `M,H`.

### Lemma 2.1 (one matching is exactly the central surgery)

Suppose there is an injection

\[
                         \phi:H\longrightarrow L    \tag{2.2}
\]

such that, for every `D in H`, aligned representatives satisfy

\[
                         Q_6(\phi(D))\subset Q_8(D). \tag{2.3}
\]

Then all rank-six, rank-seven, rank-eight and rank-nine elements split
exactly into the packets

\[
\begin{array}{ll}
 Q_6(C)<Q_7(C)<Q_8(C)<T_9(C),
       & C\in L\setminus\phi(H),\\[2mm]
 Q_7(C)<Q_8(C)<T_9(C),
       & C\in\phi(H),\\[2mm]
 Q_7(C)<Q_8(C)<T_9(C),
       & C\in M,\\[2mm]
 Q_6(\phi(D))<Q_8(D)<T_9(D),
       & D\in H.
\end{array}                                           \tag{2.4}
\]

Their shape counts are exactly (0.2).

#### Proof

Injection makes the rank-six entries moved in the last line pairwise
distinct.  Each is removed from exactly the native triple in the second
line.  Thus every rank-six element is used once.  The surgery does not move
any rank-seven, rank-eight, or rank-nine element, so those ranks are also
used once.  There are `728-286=442` first-line packets, `286` last-line
packets, and `286+416=702` second- and third-line packets.  Equation (2.3)
gives the only nonnative comparison.  \(\square\)

Conversely, any surgery which leaves every rank-seven/rank-eight/rank-nine
incidence native and changes only the rank-six attachment determines an
injection (2.2).  Thus the matching is necessary and sufficient for this
precisely scoped surgery class.

## 3. Exact `n=17` matching and the strict-cover obstruction

Form a bipartite graph `B` as follows.

* The left shore is the 286 GKS rank-eight starters `Q_8(D)`, `D in H`.
* The right shore is the 728 rank-six elements `Q_6(C)`, `C in L`.
* Join the two necklace representatives when some common cyclic alignment
  satisfies `Q_6(C) subset Q_8(D)`.

The exact reconstruction of the GKS representative poset and its SCD gives
the left-degree histogram

\[
 21^1,\qquad26^6,\qquad27^{40},\qquad28^{239}.        \tag{3.1}
\]

In particular this is not the sparse chain-cover tree.  Exact bipartite
matching gives

\[
                         \nu(B)=286.                 \tag{3.2}
\]

The 286 matched aligned containments are frozen in

```text
scratch/threadA_k17_gks_rank678_surgery_20260801.tsv
```

The recorded shift acts on the rank-six representative (right cyclic
rotation in the audit convention), and every row literally verifies
`rot(Q_6,shift) subset Q_8`.  The two shores are both repetition-free.
Thus the TSV itself verifies the matching independently of the matching
algorithm, and Lemma 2.1 proves (0.2).

For comparison, restrict every left vertex to the single rank-six
grandparent `alpha^2(z)` supplied by (1.2).  The image has size 205 and
grandparent multiplicities

\[
                         1^{147},\quad2^{35},\quad3^{23}. \tag{3.3}
\]

Hence this restricted graph has global deficiency `286-205=81`.  More
sharply, any two children of one of the 35 double grandparents already
have a one-point neighbourhood.  This is a two-vertex Hall cut and is the
smallest possible nontrivial Hall obstruction.  A matching can use at most
205 grandparent edges, proving the non-cover-link floor (0.3).

The exhaustive part here is small and theorem-faithful: it enumerates the
`2^17` strings, chooses the unique GKS block-code representative, rebuilds
the SCD by the published successor, verifies all 7,712 representatives and
the birth histogram, and then runs bipartite matching on the displayed
`286 x 728` containment graph.  It is not a search over owner chronologies.

## 4. Exact agreement with the nine certified age types

Use the certified names and masses

\[
\begin{array}{c|c|c}
\text{types}&\text{central suffix shape}&\text{total mass}\\ \hline
I&(6<7<8)&442\\
A,D,G&(6<8)&139+20+127=286\\
B,C,E,F,H&(7<8)&297+8+20+140+237=702.
\end{array}                                           \tag{4.1}
\]

Therefore assign type `I` to the 442 intact triples, split the 286 skip
packets into `A,D,G` with counts `139,20,127`, and split the 702 pair
packets into `B,C,E,F,H` with counts `297,8,20,140,237`.  This realizes
the exact nine type multiplicities and every tight target orbit at ranks
six, seven and eight.

The phrase "realizes the type multiplicities" in this section concerns the
central shape and counts.  A type also asks for its lower suffix.  Those
lower suffixes are the residual gate below.

At this static quotient stage, the cross packet may rotate its moved
rank-six orbit to the phase recorded in the TSV, while the vacated native
rank-seven/rank-eight fragment keeps its own phase: the rank-six orbit no
longer occurs in that fragment.  Once a rank-nine owner chronology and its
edge voltages are fixed, those phases cease to be independent.  The TSV is
therefore not by itself a representative-level chronological lift.

## 5. Exact residual low-flag gate

After Section 4, the only distinct tight lower targets still to be attached
are

\[
       8\text{ at rank }2,quad40\text{ at rank }3,quad
       140\text{ at rank }4,quad364\text{ at rank }5. \tag{5.1}
\]

Their required packet classes are

\[
\begin{array}{c|cc}
\text{rank}&(6<8)\text{ packets}&(7<8)\text{ packets}\\ \hline
2&0&8\ (C)\\
3&20\ (D)&20\ (E)\\
4&0&140\ (F)\\
5&127\ (G)&237\ (H).
\end{array}                                           \tag{5.2}
\]

The remaining 139 skip packets and 297 pair packets are types `A,B`; their
rank-one suffixes use the one slack singleton orbit and impose no distinct
rank-`2,...,5` target row at the static stage.

Fix a subdivision of the skip and pair packets into the type bins of
(4.1).  For `s=2,3,4,5`, join a rank-`s` target orbit to a packet of the
corresponding type when some common alignment places the target inside the
packet's rank-six or rank-seven base.  Then the lower targets attach if and
only if, for every `s` and every family `X` of rank-`s` target orbits,

\[
               |N_s(X)|\ge |X|.                     \tag{5.3}
\]

This is ordinary Hall because different ranks use disjoint one-cell slots.
The existential residual statement is to choose the type subdivision in
(4.1) so that all four systems (5.3) hold simultaneously.

The previously frozen unrestricted static flag certificate proves that
some cross-chain age-flag factor exists.  It does not prove that its central
skeleton is the particular controlled GKS surgery (2.4).  Thus (5.3), not
the already-solved scalar counts, is the exact remaining static GKS gate.

## 6. Chronology boundary

Even a positive solution of (5.3) is static.  The connected type word

```text
scratch/k17_age_type_euler_word_20260801.tsv
SHA256 e55bea5534c80560755dbc34a1f40e5cb9e67bca23e82d72caf902d2a1fd39f8
```

must still be put on a quotient Johnson cycle with voltage-twisted labelled
age partitions.  In particular the changing-owner survivor inclusions,
the forced lag-four returns at its 436 zero-refresh positions, nonzero
voltage, and an upper-safe physical opening are not consequences of the
central matching (3.2).

Accordingly this theorem is a genuine controlled SCD surgery and removes
the `286` rank-eight-start bottleneck.  It is not a proof of
`nu(17)=24313`.

## 7. Exact artifacts

```text
scratch/audit_threadA_k17_gks_rank678_surgery_20260801.py
scratch/threadA_k17_gks_rank678_surgery_20260801.tsv
scratch/threadA_k17_gks_rank678_surgery_20260801.audit.json
```

The audit status is

```text
PASS_K17_GKS_RANK678_CONTROLLED_SURGERY
```

with exact census

```text
GKS chains                         1430
rank-eight starters                286
rank-six elements                  728
full-containment matching          286
distinct strict grandparents       205
strict grandparent deficiency       81
```

## 8. Source

The GKS construction used above is Theorem 3 of J. R. Griggs,
C. E. Killian and C. D. Savage, *Venn Diagrams and Symmetric Chain
Decompositions in the Boolean Lattice*, Electronic Journal of
Combinatorics 11 (2004), R2, DOI `10.37236/1755`.
