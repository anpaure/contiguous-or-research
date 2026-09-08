# Thread A: K16 carrier-3 occurrence donor graph and shuttle audit

## 1. Frozen object

Let $Q$ be the rank-eight chronology

```
scratch/threadA_k16_carrier3_defect_token_20260730/carrier_3.targets
```

with SHA-256

```
6d1f85644ed71212d29405d2595cb538e386cb8055632f0797fa5350b4b339e0
```

Independent replay proves that $Q$ is obtained from
`scratch/k16_resident_state2_upper2_targets.txt` by the forward pattern-4
transposition with cuts `(5725,6388,12826)`.  Its flats are
`(5769,12869,12871)`, its proper-prefix capacity is 31,512, its maximal
envelope has no zero, and it is `G0`-exact and upper-complete.

Write $G=(L,R,E)$ for its exact generalized-COMP3 Hall graph.  Thus $L$
is the set of all 26,332 nonempty masks of rank below eight, $R$ is the set
of 31,512 proper-prefix source cells, and $(S,c)∈E$ precisely when cell
$c$ can realize $S$ under the maximal-envelope and forced-middle-carrier
conditions.  Independent reconstruction gives 350,892 incidences and a
maximum matching $M$ of size 26,310.

The saved maximum matching exposes the following 22 rank-seven roots:

```
11cd 4879 4c39 504f 50ae 50cd 7134 834d 9534 9744 a0da
a153 a30e af01 b0ac c89c cc29 d20d d4e0 e690 ed04 f230
```

The alternating Hall shore is an exact cut


\[
 X\subseteq L,\qquad Y=N_G(X),\qquad |X|=519,\quad |Y|=497.       \tag{1.1}
\]

The 22-root list is tied to the displayed maximum matching.  The certified
cut (1.1), rather than that particular root list, is the invariant object
used in any repair argument below.

## 2. Exact defect-token graph

For $S,T∈X$ and $c∈Y$, put an occurrence-labelled arc

\[
                 S\mathrel{\mathop{\longrightarrow}^{c}}T
       \quad\Longleftrightarrow\quad (S,c)\in E\text{ and }M(c)=T. \tag{2.1}
\]

This has an exact operational meaning: assigning the literal cell $c$ to
$S$ services $S$ and moves the unmatched token to its current owner
$T$.  No cell in $Y$ is free.

### Theorem 2.1 (root normal form)

The roots `4879` and `4c39` have degree zero in $G$.  Each of the other
20 roots has exactly one incident cell, and that cell is matched to the
rank-six cofacet shown below.

| root | matched owner | cell | physical interval |
|---|---|---:|---:|
| `11cd` | `01cd` | 8183 | `[2727,2730)` |
| `504f` | `404f` | 6584 | `[2194,2197)` |
| `50ae` | `10ae` | 443 | `[147,150)` |
| `50cd` | `40cd` | 8186 | `[2728,2731)` |
| `7134` | `7114` | 10757 | `[3585,3588)` |
| `834d` | `824d` | 27431 | `[10830,10832)` |
| `9534` | `8534` | 21041 | `[7635,7637)` |
| `9744` | `9344` | 20313 | `[7271,7273)` |
| `a0da` | `a05a` | 21391 | `[7810,7812)` |
| `a153` | `2153` | 20189 | `[7209,7211)` |
| `a30e` | `830e` | 19757 | `[6993,6995)` |
| `af01` | `a701` | 28895 | `[11562,11564)` |
| `b0ac` | `b0a4` | 23961 | `[9095,9097)` |
| `c89c` | `c81c` | 22467 | `[8348,8350)` |
| `cc29` | `4c29` | 28775 | `[11502,11504)` |
| `d20d` | `d205` | 20539 | `[7384,7386)` |
| `d4e0` | `c4e0` | 18947 | `[6588,6590)` |
| `e690` | `6690` | 21073 | `[7651,7653)` |
| `ed04` | `ec04` | 20859 | `[7544,7546)` |
| `f230` | `7230` | 18905 | `[6567,6569)` |

Moreover, the induced bipartite graph on $X\cup Y$ has 19 connected
components.  Three have gaps two and sizes

\[
 (72,70),\quad(53,51),\quad(50,48),                         \tag{2.2}
\]

with root pairs `{7134,f230}`, `{504f,50cd}`, and `{50ae,b0ac}`.  Fourteen
nontrivial components have gap one, and the two degree-zero roots form the
two remaining `(1,0)` components.

#### Proof

Reconstruct every cell from the forced depth sequence, compute its allowed
union and mandatory mask, and enumerate the exact incidence predicate.  The
saved matching is injective and every saved pair is an incidence.  For each
of the 22 roots, direct lookup gives the displayed degree and labelled cell.
Breadth-first search in the induced bipartite graph gives the component
partition and (2.2).  The component left and right counts sum to 519 and
497, respectively.  \(\square\)

## 3. Rank-seven surplus pregraph

For a rank-seven mask $D$, let

\[
                  \mu(D)=|N_G(D)|                            \tag{3.1}
\]

be its number of literal candidate cells.  For a root $Z$, define a
surplus donor occurrence to be a pair $(D,c)$ satisfying

\[
 |Z\mathbin\triangle D|=2,\qquad \mu(D)\ge2,\qquad c\in N_G(D). \tag{3.2}
\]

Condition (3.2) is deliberately only an algebraic prefilter.  It says that
one Johnson swap changes the donor colour to the receiver colour and that
one occurrence of $D$ can be spent without making $D$ hostless.  It is
the complete prefilter for this restricted one-coordinate pure-surplus
architecture, but it is neither necessary for a general compound atom nor
sufficient for one legal chronology exchange.

### Theorem 3.1 (complete surplus catalogue)

Across the 22 roots, (3.2) gives exactly

\[
 229\text{ receiver--donor mask edges},\qquad
 464\text{ occurrence-labelled edges},                     \tag{3.3}
\]

using 217 distinct donor masks.  Exactly two roots have no surplus donor:

\[
                         \texttt{11cd},\qquad\texttt{50ae}. \tag{3.4}
\]

Every one of the 464 labelled donor cells has allowed union exactly equal to
its donor mask; none is counted merely through a larger-envelope submask.

Their minimum Johnson distance to a multi-occurrence rank-seven donor is
two, so the restricted one-swap pure-surplus architecture cannot service
either.

The two genuine zero-host roots are not isolated in the surplus pregraph:

\[
\begin{aligned}
 N^+(\texttt{4879})
   &=\{\texttt{4a39},\texttt{6871},\texttt{8879},
       \texttt{c859},\texttt{c869}\},\\
 N^+(\texttt{4c39})
   &=\{\texttt{4a39},\texttt{cc31}\}.
\end{aligned}                                               \tag{3.5}
\]

Every donor in (3.5) has multiplicity two.  In particular, static donor
abundance does not explain the absence of a host for either zero target.

The bipartite pregraph from roots to literal donor cells has matching number
exactly 20.  The upper bound follows from (3.4); the audit emits a 20-edge
certificate using 20 distinct donor masks.  Every selected donor has
multiplicity two and is used once, so one physical occurrence of every donor
remains.  One deterministic certificate is:

| receiver | donor | cell | interval |
|---|---|---:|---:|
| `4879` | `6871` | 9080 | `[3026,3029)` |
| `4c39` | `cc31` | 28773 | `[11501,11503)` |
| `504f` | `d047` | 24777 | `[9503,9505)` |
| `50cd` | `d08d` | 19881 | `[7055,7057)` |
| `7134` | `d134` | 22889 | `[8559,8561)` |
| `834d` | `864d` | 17679 | `[5954,5956)` |
| `9534` | `9d30` | 17483 | `[5856,5858)` |
| `9744` | `874c` | 17681 | `[5955,5957)` |
| `a0da` | `a1d8` | 18013 | `[6121,6123)` |
| `a153` | `b152` | 18085 | `[6157,6159)` |
| `a30e` | `a316` | 18855 | `[6542,6544)` |
| `af01` | `ad11` | 17831 | `[6030,6032)` |
| `b0ac` | `b0aa` | 17445 | `[5837,5839)` |
| `c89c` | `d894` | 17503 | `[5866,5868)` |
| `cc29` | `8d29` | 17775 | `[6002,6004)` |
| `d20d` | `d20b` | 17791 | `[6010,6012)` |
| `d4e0` | `d4c4` | 17507 | `[5868,5870)` |
| `e690` | `c6d0` | 18177 | `[6203,6205)` |
| `ed04` | `ed40` | 18107 | `[6168,6170)` |
| `f230` | `b231` | 18003 | `[6116,6118)` |

All 20 displayed cells lie outside the old shore $Y$.  Therefore each is
an exterior *potential* Hall port if a legal chronology atom can retype that
cell from its donor to its receiver without destroying another old shore
cell.  Pairwise distinctness alone is not such an atom and is not a compiler
certificate.

#### Proof

Each rank-seven mask has exactly 63 Johnson neighbours.  Test their exact
candidate lists against (3.2), retaining the physical cell identifier,
start, length, allowed union and mandatory mask.  This gives (3.3)--(3.5).
A standard augmenting-path matching on the resulting 22-by-cell graph gives
the displayed 20 distinct cells; direct comparison with $Y$ proves that
all are exterior.  The two isolated left vertices prove optimality.  \(\square\)

## 4. The exact old-cut escape requirement

### Lemma 4.1 (necessary Hall escape)

Let $H$ be any modified incidence graph on the same left and right vertex
sets.  If, for an integer $0 ≤ r ≤ 22$,

\[
                         \nu(H)\ge \nu(G)+r,                 \tag{4.1}
\]

then the old witness satisfies

\[
 |N_H(X)\setminus Y|-|Y\setminus N_H(X)|\ge r.             \tag{4.2}
\]

#### Proof

By the deficiency form of Hall's theorem, (4.1) implies that every left set,
and hence $X$, has deficiency at most `22-r` in $H$.  Since
`|X|-|Y|=22`, this says `|N_H(X)|>=|Y|+r`, which is exactly (4.2).  \(\square\)

Condition (4.2) is necessary, not sufficient.  A proposed physical atom must
still be replayed and either exhibit the claimed larger matching or preserve
a named exterior matching while providing the corresponding residual
matching.  In particular, full Hall requires net exterior gain at least 22
for this old shore.  Also, a useful portal may serve any of the 519 targets
in $X$, not only one of the 22 displayed matching roots.

## 5. Comparison with the authenticated C0/C1 shuttles

The authenticated old service receivers are `1639` and `1879`.  Neither is
one of the 22 roots, and neither belongs to $X$.  The old pure donors
`9439` and `9859` also lie outside $X$.  In fact the two old receiver--donor
pairs satisfy the unrestricted rank-seven surplus predicate on carrier 3,
but neither is an edge of the **root-restricted** pregraph of Section 3 and
neither adds a neighbour to the old Hall shore.

There is one mask-level coincidence: `8879`, one of the three donor species
considered in the old C1 search, is a surplus donor for receiver `4879` in
(3.5).  The authenticated C1 atom, however, creates `1879`, not `4879`, and
is tied to a different source chronology.  This coincidence is not a
physical service atom.  Among the four C1 upper-safe residual debts, only
`0d35` belongs to $X$; its sign is negative, so that signed ledger cannot
improve the old cut by itself.

For completeness, literal pattern-4 transplantation of all seven proved old
cut triples onto $Q$ was replayed.  Every transplant fails the exact middle
carrier before Hall:

| old atom | bad middle rows |
|---|---:|
| C0 pure | 10 |
| C0 upper-safe | 9 |
| C1 pure | 7 |
| C1 upper-safe, debt `0d35` | 10 |
| C1 upper-safe, debt `4b38` | 4 |
| C1 upper-safe, debt `3871` | 8 |
| C1 upper-safe, debt `0579` | 9 |

Thus **none of the currently authenticated shuttles services carrier 3**.
This statement is exact for those seven source-labelled atoms.  It does not
exclude a carrier-3-specific conjugate, a longer compound atom, or a portal
into another target of $X$.

## 6. Exact remaining gate

The positive information is the 20-cell exterior certificate in Theorem
3.1.  The 20 labelled ports themselves account for at most 20 of the 22 net
exterior neighbours required by Lemma 4.1 for full Hall; a physical atom may,
of course, have additional incidence effects, which must be replayed.  This
agrees with the independently proved Pascal-tower description of the same
shore: its 22-element missing-provider diagonal is indexed by nineteen
rank-five masks, one rank-six mask, and the two rank-seven masks
`4879,4c39`.  Thus the 22 chosen
rank-seven matching roots are useful token coordinates, but are not the
intrinsic 22 repair targets.

The smallest direct continuation toward a strict `22 -> 21` improvement is
to realize one of the labelled retypings by a chronology move that
simultaneously

1. preserves `G0`, maximal-envelope replay, capacity and all upper masks;
2. retains every old $X$-to-$Y$ incidence needed by a protected matching;
3. makes its exterior cell a candidate for the stated receiver; and
4. raises the exact matching size from 26,310 to at least 26,311.

Any strategy confined to the Section-3 one-coordinate pure-surplus pregraph
cannot serve all 22 displayed roots because of (3.4).  A full repair must
instead leave that restricted architecture for `11cd` and `50ae`, enter
their deficient components through another target of $X$, or transport the
intrinsic Pascal diagonal directly.

## 7. Authentication and scope

Primary reproducer:

```
scratch/audit_a_k16_carrier3_occurrence_donor_graph_20260730.py
  SHA 39c0b76a4ee571a133a35f6e23266fc1c940d8c5a1cd8c3c9d4c318328aed93b
```

Machine-readable audit:

```
scratch/threadA_k16_carrier3_defect_token_20260730/
  carrier_3.occurrence_donor_graph.audit.json
    SHA 5f0a8ac417e3b412285c2493841354057aec5054a4cc6bf9ce1d45c517c9d14b
    payload 002e86e9c484053cc1ee99c924a0fd577c2b13a5867106f7ea34f4021db840ab
```

The independently replayed input Hall audit has SHA
`56a89bd61470a5a670fc19b0e9bc71374adbcdd6666f55f29308707fd53ded0a`
and payload
`d5ff52d8de1c9327fd1fcc393075041ddfe98eaae639edb6155e173a027cff45`.
The independent G0/upper-support audit has SHA
`6719776eb558578261acbf434de05f2ea21f128e9e84e90d60b0dfcf4f93a36f`.
The intrinsic-diagonal comparison in Section 6 uses
`MATH_THEOREM_K16_CARRIER3_PASCAL_HALL_TOWER_20260730.md`, SHA
`b0ca14d24907a59e13582b3c4a0f1dfcb99efe7d698089be9999c259802cb425`.

The audit uses no phase-labelled wrapper output.  It reconstructs every
envelope, mandatory mask and incidence directly from the authenticated native
chronology.  Its surplus graph is complete only for rank-seven Johnson
distance-one donors of multiplicity at least two.  Rank-distance two,
non-Johnson exchanges, exceptional changed-cell corrections and compound
chronology atoms are outside that catalogue.

This note proves neither a universal compiler nor `nu(16)=12873`.  The exact
K16 bracket remains

\[
                       12873\le\nu(16)\le12874.
\]
