# Adversarial audit of the all-odd compiler: exact non-one-core normalization

Date: 2026-07-29

Status: **general one-core normalization refuted; unrestricted compiler and
q1 boundary theorem survive; exact replacement theorem proved**.

## 1. Verdict

For a fixed rank-`r` middle chronology `T`, feasibility of the unrestricted
depth-`d` compiler `COMP_d(T)` does **not** imply the existence of an
antecedent satisfying

\[
                              DA=DP,                      \tag{1.1}
\]

where `P` is the maximal depth-`d` erosion of `T`.  The smallest retained
verified capacity counterexample in the audited odd range is the optimal
`k=9` word.  It has a feasible and
universal unrestricted antecedent of length `128`, while every lower-complete
one-core antecedent would need at least `129` distinct literal letters.

The exact quantifier boundary is

\[
 \underbrace{\exists A\;\operatorname{COMP}_d(T,A)}_{G(T)}
 \quad\not\Longrightarrow\quad
 \underbrace{\exists C\le P:\ DC=DP\text{ and }C
              \text{ passes residual Hall}}_{O(T)}.       \tag{1.2}
\]

The reverse implication `O(T) => G(T)` is true.  At `k=11` and `k=13`, both
`G(T)` and `O(T)` happen to hold for the same retained middle chronologies,
but the one-core witnesses are global rewrites.  The retained antecedents,
and even their canonical negative-window closure artifacts, refute repair
supported only on the depth-three boundary halos of these two retained
antecedents.

The correct normalization of arbitrary `COMP_d(T)` solutions is the
**negative-window interval closure** of Section 7.  It preserves every lower
target through one canonically selected witness, the middle chronology,
nonemptiness, and all upper rows, but it need not satisfy (1.1).  Thus an
all-odd proof must retain the unrestricted pinned
compiler.  The one-core/Hall model is an optional stronger branch only when
its separate existence is proved.

## 2. Exact setup

Fix a finite ground set `[k]`, integers

\[
                       1\le d<r,\qquad W\ge2,
\]

and a linear sequence

\[
 T=(T_0,\ldots,T_{W-1})
\]

of rank-`r` sets.  Write `D` for adjacent union, so

\[
 (D^dA)_i=\bigcup_{p=i}^{i+d}A_p.                        \tag{2.1}
\]

Assume consecutive entries of `T` are Johnson adjacent and every internal
positive coordinate run in `T` has length at least `d+1`.  Define its maximal
depth-`d` erosion by

\[
 P_p=\bigcap_{\max(0,p-d)\le i\le\min(W-1,p)}T_i,
 \qquad 0\le p<W+d.                                      \tag{2.2}
\]

Put `N=W+d` and `h=r-d`.

### Lemma 2.1 (maximal envelope and fixed upper chronology)

If a nonempty word `A` of length `N` satisfies `D^dA=T`, then

\[
 A\le P,
 \qquad D^dP=T,                                          \tag{2.3}
\]

and for every `j>=0`,

\[
                         D^{d+j}A=D^jT.                  \tag{2.4}
\]

Every rank-below-`r` interval witness in `A` has length at most `d`.

#### Proof

If source position `p` lies in middle window `[i,i+d]`, then
`A_p subseteq T_i`.  Intersecting all such `T_i` gives `A_p subseteq P_p`.
Every `P_p` contributing to middle window `i` is contained in `T_i`, so
`D^dP<=T`; monotonicity and `A<=P` give

\[
                  T=D^dA\le D^dP\le T.
\]

This proves (2.3).  Equation (2.4) follows by applying `D^j`.  Finally, an
interval of at least `d+1` source positions contains a full source window
whose union is a rank-`r` entry of `T`, and therefore cannot have rank below
`r`.  QED.

### Lemma 2.2 (intermediate erosion grading)

For `0<=j<=d` and `0<=p<W+d-j`,

\[
 (D^jP)_p=
 \bigcap_{\max(0,p-(d-j))\le i\le\min(W-1,p)}T_i.         \tag{2.5}
\]

Consequently every cell of `D^jP` has rank at least

\[
                            r-d+j=h+j.                   \tag{2.6}
\]

#### Proof

Work one coordinate at a time.  Formula (2.2) erodes each positive run of
the coordinate by `d` positions, with the usual truncation at the two global
ends.  Since every internal run has length at least `d+1`, applying `j`
adjacent unions restores exactly `j` layers of that erosion.  The result is
erosion by `d-j`, which is (2.5).

The right side of (2.5) intersects at most `d-j+1` consecutive Johnson
states.  Each transition can delete at most one element from the running
intersection, so its rank is at least `r-(d-j)=h+j`.  QED.

## 3. The exact unrestricted compiler survives

For fixed `T`, `COMP_d(T)` consists of a nonempty sequence `A_p subseteq P_p`
such that:

1. for every `i` and every `x in T_i`, at least one of
   `A_i,...,A_(i+d)` contains `x`; and
2. for every nonempty `S subseteq [k]` with `|S|<r`, some source interval of
   length at most `d` contains every coordinate of `S` and no coordinate
   outside `S`.

The first clause is exactly `D^dA=T`; the second is exactly literal lower
coverage by Lemma 2.1.  Hence:

### Theorem 3.1 (unrestricted fixed-chronology equivalence)

`COMP_d(T)` is feasible if and only if there is a nonempty length-`W+d` word
`A` with `D^dA=T` which covers every target of rank below `r` by a literal
contiguous OR.

If, in addition, every target above rank `r` is a contiguous union of entries
of `T`, then the same `A` is universal: an interval `T_i,...,T_j` lifts to

\[
                  A_i\cup A_{i+1}\cup\cdots\cup A_{j+d}. \tag{3.1}
\]

#### Proof

The equivalence is the two compiler clauses above.  Equation (3.1) is (2.1)
followed by associativity of union.  QED.

No equation `DA=DP` is used here.  The PBBS alternating-circuit algebra, the
component cut--join identities, and the upper safe-opening/kernel criterion
also concern the middle factor or `T` itself and survive unchanged.  What
does not survive is the reduction of the lower compiler to literal source
targets and ordinary Hall.

## 4. What one-core grading actually proves

Define the fixed positive lower spectrum

\[
 \mathcal K^+(P)=\bigcup_{j=1}^{d-1}\operatorname{supp}(D^jP)             \tag{4.1}
\]

and the exact residual family

\[
 \mathcal F(P)=
 \{S\subseteq[k]:1\le |S|<r,\ S\notin\mathcal K^+(P)\}.                 \tag{4.2}
\]

A **one-core** is a word `C` satisfying

\[
 C_p\subseteq P_p,
 \qquad C_p\cup C_{p+1}=P_p\cup P_{p+1}.                 \tag{4.3}
\]

For fixed `C`, put

\[
 N_C(S)=\{p:C_p\subseteq S\subseteq P_p\}.               \tag{4.4}
\]

### Theorem 4.1 (exact one-core/maximal-default theorem)

The following are equivalent.

1. There is a nonempty universal lower antecedent `A` with `DA=DP` and
   `D^dA=T`.
2. There is a one-core `C` for which

   \[
   \left|\bigcup_{S\in X}N_C(S)\right|\ge |X|
   \quad\text{for every }X\subseteq\mathcal F(P).         \tag{4.5}
   \]

3. There is such an antecedent in **maximal-default form**: one distinct
   position is assigned literally to each target in `F(P)`, and every
   unassigned position equals `P_p`.

#### Proof

Assume `DA=DP`.  For every interval of length `ell>=2`,

\[
 \bigcup_{t=p}^{p+\ell-1}A_t
 =\bigcup_{t=p}^{p+\ell-2}(DA)_t
 =(D^{\ell-1}P)_p.                                      \tag{4.6}
\]

Thus a target in `F(P)` cannot use an interval of lengths `2,...,d`; by
Lemma 2.1 it cannot use a longer interval either.  It must occur literally
as one `A_p`.  Distinct targets require distinct positions, and taking
`C=A` gives a matching in (4.4), hence (4.5).

Conversely, take a matching saturating `F(P)`.  At a position matched to `S`
put `A_p=S`; at every unmatched position put `A_p=P_p`.  Then

\[
                            C\le A\le P.
\]

Equation (4.3) sandwiches `DA` between `DC=DP` and `DP`, so `DA=DP`.
Every default is nonempty because Lemma 2.2 gives `|P_p|>=h>0`, and every
matched target is nonempty.  The matching supplies `F(P)` literally and the
positive rows supply every other lower target.  This proves all three
equivalences.  QED.

Prescribed pins require contracted Hall: each pin `S@p` must satisfy
`C_p subseteq S subseteq P_p`.  Pins sharing a position must prescribe the
same mask, after which identical pins are deduplicated.  Every pinned
position is removed, even if its target lies outside `F(P)`; each target of
`F(P)` supplied by one or more pins is removed once; and (4.5) is imposed on
the remaining graph.

Theorem 4.1 is exact, but it is exact only inside the one-core class.

## 5. The decisive literal-capacity obstruction

### Theorem 5.1 (one-core literal-capacity inequality)

If a universal lower antecedent satisfying `DA=DP` exists, then

\[
                  \boxed{\sum_{s=1}^{r-d}{k\choose s}\le W+d.}           \tag{5.1}
\]

More generally, any nonempty `A` with `D^dA=T` and `DA=DP` which omits `b`
targets of ranks at most `r-d` satisfies

\[
 b\ge
 \max\left\{0,\sum_{s=1}^{r-d}{k\choose s}-(W+d)\right\}. \tag{5.1a}
\]

#### Proof

Put `h=r-d`.  By (4.6) and Lemma 2.2, an interval of length
`2<=ell<=d` has rank at least

\[
                         h+\ell-1>h.
\]

An interval of length at least `d+1` contains a rank-`r` middle window.
Therefore every covered target of rank at most `h` must be a literal source
letter.
There are `sum_(s=1)^h binom(k,s)` distinct such targets and only `W+d`
source positions.  If `b` of them may be omitted, at most `W+d` of the
remaining targets can be literal, giving (5.1a).  QED.

This obstruction is independent of the choice of one-core and independent
of Hall refinements.

### Theorem 5.2 (exact `k=9` counterexample to normalization)

For `k=9`, the implication `G(T)=>O(T)` in (1.2) is false.

#### Proof

Here

\[
 r=5,\qquad W={9\choose5}=126,\qquad d=2,
 \qquad h=3,\qquad N=128.                                \tag{5.2}
\]

The deadline arithmetic is exact:

\[
 \Lambda=\sum_{s=1}^4{9\choose s}=255,
 \qquad 1\cdot126+{2\choose2}=127<255,
 \qquad 2\cdot126+{3\choose2}=255.                      \tag{5.3}
\]

But the one-core capacity is

\[
 {9\choose1}+{9\choose2}+{9\choose3}
 =9+36+84=129>128.                                      \tag{5.4}
\]

Thus Theorem 5.1 forbids every lower-complete one-core antecedent for every resident
Johnson chronology at these parameters.

On the other hand, the retained word

```text
scratch/claude_quotient_hardened_20260729/fixtures/k09_literal.word
```

has SHA-256

```text
0f282a2c5bb61c0ea48d49c5966eafba3ceb8a30cc40150a92764c1321c21b7c.
```

Solver-independent replay gives:

* length `128` and all `511` nonempty masks covered;
* `D^2A` is a Johnson path through all `126` rank-five masks;
* all `128` source values are distinct, with ranks `1^9,2^36,3^83`;
* all `127` adjacent unions are distinct and disjoint from the source values,
  with ranks `3^1,4^126`;
* these `255` values biject exactly onto every lower target;
* the unique nonliteral rank-at-most-three target is

  \[
                 416=A_0\cup A_1=384\cup32;              \tag{5.5}
  \]

* the maximal erosion has ranks `3^124,4^2,5^2`, while `DP` has ranks
  `4^125,5^2`; in particular `(DP)_0=419`, so (5.5) would be contaminated
  by one-core grading; and
* `DA` differs from `DP` at edges `0` and `126`; the second unrestricted
  boundary residual is the rank-four value `291=(DA)_126`.

Hence the word is a feasible `COMP_2(T)` antecedent, while (5.4) proves that
no lower-complete one-core antecedent exists for the same `T`.  QED.

The exact one-core residual family here actually has `130` members: all
`129` masks of ranks at most three and the rank-four boundary residual
`291`.  The carrier-independent subfamily of `129` already exceeds the
entire source capacity by one.

### Post-`k=15` arithmetic consequence

The same necessary test gives:

| `k` | `r` | `d(k)` | `h=r-d` | `sum_(s<=h) binom(k,s)` | `W+d` | slack |
|---:|---:|---:|---:|---:|---:|---:|
| 15 | 8 | 3 | 5 | 4,943 | 6,438 | +1,495 |
| 17 | 9 | 3 | 6 | 21,777 | 24,313 | +2,536 |
| 19 | 10 | 3 | 7 | 94,183 | 92,381 | -1,802 |
| 21 | 11 | 3 | 8 | 401,929 | 352,719 | -49,210 |

Thus the lower-complete one-core architecture is arithmetically impossible at `k=19` and
`k=21`, for every resident Johnson chronology.  Even an approximate
one-core must omit at least `1,802` and `49,210` low targets respectively,
far exceeding the `2d=6` endpoint-cell bank.  This does not prove
`COMP_d(T)` feasible there; it proves conditionally that, if an unrestricted
compiler succeeds, no lossless or six-boundary-hole one-core normalization
can represent it.

## 6. Exact promotion repair and why it is not a normalization theorem

Let `A` be any feasible unrestricted antecedent and define the labelled
defect on source edge `i` by

\[
 \Delta_i=(P_i\cup P_{i+1})\setminus(A_i\cup A_{i+1}).    \tag{6.1}
\]

For a set of source positions `V`, define the monotone promotion

\[
 A^V_p=
 \begin{cases}
 P_p,&p\in V,\\
 A_p,&p\notin V.
 \end{cases}                                             \tag{6.2}
\]

### Theorem 6.1 (exact labelled path repair)

The promoted word satisfies `DA^V=DP` if and only if, for every edge `i`
and every `x in Delta_i`, at least one endpoint `p in {i,i+1} intersect V`
satisfies `x in P_p`.  Whenever this holds,

\[
                          D^dA^V=T.                       \tag{6.3}
\]

A minimum-cardinality such `V` is found exactly by a two-state dynamic
program along the source path.

#### Proof

Promotion only adds elements already in `P`.  On edge `i`, equality with
`P_i union P_(i+1)` holds precisely when every element missing in (6.1) is
supplied by a promoted endpoint which contains it.  This is the displayed
condition.  Its constraints involve only the two endpoint-selection bits of
the current path edge, so retaining the optimum costs for whether the current
vertex is selected gives an exact two-state dynamic program.

Finally `A<=A^V<=P`; applying `D^d` and using (2.3) sandwiches `D^dA^V`
between `T` and `T`.  QED.

### Corollary 6.2 (unavoidable changed positions)

Let

\[
 E_{\rm def}=\{i:\Delta_i\ne\varnothing\}.
\]

Every word `B` with `DB=DP` must differ from the original `A` on a vertex
cover of the path-edge set `E_def`.  Hence

\[
 \bigl|\{p:B_p\ne A_p\}\bigr|\ge\tau(E_{\rm def}),       \tag{6.4}
\]

where a block of `ell` consecutive defective edges contributes
`ceil(ell/2)` to `tau`.

#### Proof

If neither endpoint of a defective edge changes, its adjacent union remains
`A_i union A_(i+1)`, which differs from `DP` on that edge.  Thus the change
set meets every defective edge.  The path vertex-cover formula is elementary
blockwise.  QED.

Promotion can destroy lower witnesses by adding contaminating coordinates.
Choose one actual witness interval `I_S` of length at most `d` for each lower
target `S`.  The chosen intervals for distinct targets are distinct, because
one physical interval has only one OR-value.  Every chosen witness disjoint
from `V` survives, and a source position belongs to at most

\[
                         1+2+\cdots+d={d+1\choose2}       \tag{6.5}
\]

such physical intervals.  Therefore at most

\[
                         |V|{d+1\choose2}                \tag{6.6}
\]

chosen witnesses can be endangered.  This is only a union-bound ledger;
`|V|` need not be small, `V` need not lie at the boundary, and an endangered
target need not have an alternative witness.

For a selected repair `V`, put `C=A^V`.  A lower-complete one-core antecedent
`B` with

\[
                         C\le B\le P                     \tag{6.7}
\]

exists if and only if the fixed-core graph `N_C(S)` satisfies Hall on
`F(P)`.  This follows directly from Theorem 4.1.  It is the exact conditional
completion theorem after promotion; it is not an automatic consequence of
the original `COMP_d(T)` solution.

## 7. The valid canonical unrestricted normalization

The correct closure keeps interval witnesses instead of forcing them into
single source letters.

Fix a total order on physical source intervals.  Given a feasible antecedent
`A`, choose the first actual interval witness `phi_A(S)` for every lower
target `S`.  For each coordinate `x`, define

\[
 Z_x(\phi_A)=
 \{p:x\in P_p\}\setminus
 \bigcup_{S:\,x\notin S}\phi_A(S),                       \tag{7.1}
\]

and define

\[
 \mathcal C(A)_p=\{x:p\in Z_x(\phi_A)\}.                 \tag{7.2}
\]

### Theorem 7.1 (negative-window closure)

For every feasible `COMP_d(T)` antecedent `A`,

\[
                         A\le\mathcal C(A)\le P.          \tag{7.3}
\]

The word `C(A)` is nonempty, has `D^d C(A)=T`, preserves each selected lower
witness exactly, and has all the same upper derivative rows as `A`.
Iterating `C` with the fixed first-witness rule terminates at a deterministic
fixed point inside the finite box `P`.

#### Proof

If `x in A_p`, no actual witness interval containing `p` and labelled by a
target omitting `x` can exist.  Hence every bit of `A` survives (7.1), while
the definition gives `C(A)<=P`; this proves (7.3) and nonemptiness.

On a selected interval `phi_A(S)`, equation (7.1) excludes every coordinate
outside `S`.  Since `A<=C(A)` and the interval already had union `S` in `A`,
every coordinate of `S` remains present somewhere on the interval.  Its new
union is therefore still exactly `S`.

The sandwich (7.3) and (2.3) give `D^d C(A)=T`; (2.4) fixes all upper rows.
At every later iteration the same argument gives a feasible word containing
the previous one.  Strict iterations add at least one of the finitely many
incidences in `P`, so the process terminates.  QED.

This closure is canonical relative to the declared interval order and the
starting antecedent.  It preserves coverage with **zero** boundary loss, but
it generally remains outside the one-core class.  This is the correct
replacement for the false one-core normalization.

## 8. Exact `k=11` and `k=13` audit

The retained optimal words are not one-core, and they cannot be repaired by
changing only the depth-three boundary halos.

| case | retained `DA!=DP` edges | defect blocks | vertex-cover lower bound | minimum monotone promotions | deepest defect | masks missing after that promotion |
|---:|---:|---:|---:|---:|---:|---:|
| `k=11` | 5 | 3 | 3 | 3 | 123 | 4 |
| `k=13` | 209 | 192 | 192 | 192 | 857 | 102 |

For `k=11`, the exact defective edges are

\[
                         \{0,1,123,462,463\}.             \tag{8.1}
\]

The minimum promotion positions are `{1,124,463}`.  The promoted word keeps
the same third derivative and satisfies `DA=DP`, but loses exactly masks

\[
                         1,16,154,155.                    \tag{8.2}
\]

The interior edge `123` alone disproves every depth-three-boundary-only
repair of this retained antecedent.

For `k=13`, the `209` defective edges form `175` isolated blocks and `17`
blocks of length two.  Thus every one-core word, not just every monotone
promotion, must differ from the retained antecedent at at least

\[
                         175+17=192                       \tag{8.3}
\]

source positions.  A minimum promotion loses `102` masks, with rank
histogram

\[
                         1^5,2^9,3^8,4^{80}.              \tag{8.4}
\]

The retained negative-window closure artifacts preserve universality but
remain ungraded:

| case | closure SHA-256 | `DA!=DP` edges | interior edges outside depth-three halos | vertex-cover lower bound |
|---:|:---|---:|---:|---:|
| `k=11` | `3be742fade22d023241f947b9a25c823a80ede57d76b47630638ace2dda9303f` | 3 | 1 (`123`) | 2 |
| `k=13` | `698fb173d05583da447ffe025c7f27cbb4ceb4b06ec0298827060ae6809debe0` | 84 | 82 | 77 |

These are counterexamples to maps supported on the depth-three boundary
halos and give exact lower bounds on the edits of **these retained
antecedents**, but neither chronology is a counterexample to existential
one-core feasibility.  New same-chronology global replacements pass:

| `k` | one-core word SHA-256 | same `D^3` | `DA=DP` | full coverage | changed source cells from retained |
|---:|:---|:---:|:---:|---:|---:|
| 11 | `77948a035af179339e4dfc88f56efb11039daa33beef657b5ca215836448dc5b` | yes | yes | `2047/2047` | 134 |
| 13 | `749f3bbc21c62fd2a89148401ba078d4543ef71867d7ae8e2eea82cbb10e9858` | yes | yes | `8191/8191` | 1014 |

Therefore `k=11,13` provide positive finite instances of `O(T)`, not a
uniform implication `G(T)=>O(T)` and not a bounded local normalization of
their retained antecedents.

## 9. The q1 boundary theorem survives without one-core grading

### Theorem 9.1 (two extreme q1 channels for arbitrary antecedents)

Let `A` be any nonempty word with `D^dA=T`, with no assumption `DA=DP`.
Among the rank-`r-1` targets absent from the internal
Johnson-intersection palette, at most two can be witnessed by `A`: one by a
source prefix containing position `0` and one by a source suffix containing
position `W+d-1`.  In particular, if `A` is lower-complete, the internal
palette has at most two holes.

#### Proof

By Lemma 2.1, a rank-`r-1` witness interval `I=[a,b]` has length at most `d`.
If it avoids both extreme source positions, then

\[
 1\le a\le b\le W+d-2.
\]

The integer interval

\[
 [\max(0,b-d),\ \min(W-2,a-1)]
\]

is nonempty: `b-d<=a-1` by the length bound, and the two displayed endpoint
inequalities handle the global truncations.  Choose `i` in it.  Then

\[
 I\subseteq[i+1,i+d]
 =[i,i+d]\cap[i+1,i+d+1].                               \tag{9.1}
\]

Thus its union is contained in `T_i intersection T_(i+1)`.  Both sets have
rank `r-1`, so they are equal.  Such a target is an internal Johnson colour.

Every palette-absent colour witnessed by `A` must therefore use the leftmost
or rightmost source position.  All prefix unions are nested, and all suffix
unions are nested.  Two distinct nested sets cannot both have rank `r-1`, so
each end supplies at most one.  If `A` is lower-complete, every palette hole
is witnessed, giving the final assertion.  QED.

For a q1-rainbow opening of `c` components, let `R` be the `c` deleted cut
colours and `Q` the distinct cut colours restored by seams.  The theorem
gives the exact necessary palette inequality

\[
                       |R\setminus Q|\le2,
 \qquad |R\cap Q|\ge c-2.                               \tag{9.2}
\]

Endpoint side-assignment still requires the exact two-vertex Hall test as a
q1 pin necessity.  Simultaneous sufficiency remains the full pinned
`COMP_d(T)`, because those endpoint prefixes and every other lower target
share source coordinates.  This q1 result is valid for unrestricted
`COMP_d(T)`.  The deeper nested `2q`
cell allocation and the one-core Hall inequalities are not: an unrestricted
antecedent may realize a deeper target by a genuine multi-letter interval,
as the `k=9` target `416` demonstrates at `q=2`, the first depth beyond q1.

## 10. Correct all-odd replacement theorem

### Theorem 10.1 (fixed-path dichotomy)

Let `T` be an upper-safe resident Johnson ordering of every rank-`r` set
exactly once, so `W=binom(k,r)`.

1. A universal word of length `W+d` with middle chronology `T` exists if and
   only if `G(T)`, the unrestricted system `COMP_d(T)`, is feasible.
2. A universal word of that length in the one-core/maximal-default subclass
   exists if and only if `O(T)`, the core-plus-Hall condition of Theorem 4.1,
   holds.
3. `O(T)=>G(T)`, but the converse is false by Theorem 5.2.

If `W=binom(k,r)`, `d=d(k)`, and the independent deadline theorem gives the
lower bound `W+d`, a positive word in item 1 is optimal.  Optimality is not a
consequence of this compiler theorem alone.

#### Proof

Items 1 and 2 are Theorems 3.1 and 4.1 plus upper safety.  A universal
one-core antecedent is an unrestricted antecedent, giving item 3 in the
forward direction; Theorem 5.2
refutes the reverse direction.  The final sentence imports the separate
lower bound.  QED.

Accordingly, the general PBBS--Markov component reduction must end in:

1. an upper-safe resident opening;
2. the unrestricted **pinned** `COMP_d(T)` system; and
3. the q1 palette/endpoint constraints (9.2).

Replacing item 2 by one-core Hall is sound only after explicitly assuming
or proving `O(T)` for that chronology.  At `k=19` and `k=21`, Theorem 5.1
rules out that optional branch before any Hall computation.

The audit does not assert an optimal formula for the minimum number of holes
in an arbitrary approximate one-core.  What is proved is the universal lower
bound (5.1a), the lossless counterexample at `k=9`, the `2d`-boundary
obstruction at `k=19,21`, and the exact local-repair lower bounds in Section
8.

## 11. Reproducibility and proved scope

The solver-free scope audit is

```text
scratch/audit_ad_allodd_comp_onecore_scope_20260729.py
scratch/ad_allodd_comp_onecore_scope_20260729.audit.json
```

It hash-pins and replays the `k=9`, `k=11`, and `k=13` literal words, checks
their middle chronologies and one-core status, and records the exact capacity
table through `k=21`.

Its source/output SHA-256 values are

```text
9b6d44426baf8d3c836a4a12aaf85bfbe5bd4bb9cf02d1bb656e69ecd9bf76c1
73c009bf480af90ebbb7e02e3111060b3a01342245818d8cdf8b156cdf6a5055
```

and the output's semantic payload digest is
`09b1ee6a502c2d45605413d9c7e565cd9dd8ae07214c6aa4098b05588d56e277`.

The local-normalization audit is

```text
scratch/audit_ad_k11_k13_onecore_normalization_20260729.py
scratch/ad_k11_k13_onecore_normalization_20260729.audit.json
```

Its source/output SHA-256 values are

```text
6f903ecfa739dccdab68420011a415f83e650defda67f954ffe615eb79db43b1
4dc34b45ffca2b8d1e9374881702b0aff3d99e59776c28a7e67104d27cdcbe67
```

The fact that the retained `k=11,13` closure words are terminal
first-witness fixed points, rather than merely universal closure artifacts,
is certified separately by

```text
scratch/analyze_raw_optimal_compiler_normal_form.py
scratch/raw_optimal_k01_k14_compiler_normal_form_audit.json
```

with SHA-256 values

```text
34736cf1521935c40508b2a0dc5aec1bf9d4ed2dfde8ee6fba1c5448e69eff8b
33457ecdd9c96bc78eac7f2e2f35dc408315d986ea90ed3bd94d3d8b7527c913.
```

The same-chronology `k=11` proof artifact and its independent auditor are

```text
scratch/ad_k11_fixed_chronology_onecore_20260729.word
scratch/audit_ad_k11_fixed_chronology_onecore_20260729.py
scratch/ad_k11_fixed_chronology_onecore_20260729.audit.json
```

and the corresponding `k=13` word is

```text
scratch/ad_k13_fixed_chronology_onecore_20260729.word.
```

No SAT or search result is needed to verify any positive word: direct
interval-OR replay is the proof.  The one-shot solvers used to discover the
same-chronology replacements are provenance only.  No claim is made that
every `COMP_d(T)` solution has a one-core replacement; Theorem 5.2 proves the
opposite.
