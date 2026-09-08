# A compact exact search for the `k=11`, `sigma=369` boundary-reservoir branch

## 1. Scope and final status

This note originally designed a constructive search for the sufficient branch
supplied by `SINGLE_SWITCH_MAXIMAL_SHADOW_THEOREM.md`.  It is deliberately
separate from the unrestricted `2.88`-million-variable array CNF.

The branch is **not** known to be without loss of generality.  A satisfying
row would give an optimal length-`465` nonzero array and prove

\[
\nu(11)=465,
\qquad N(11)=466.
\]

The completed design exposed a short counting contradiction: the required
rainbow `1011`-core row and twelve-cell reservoir cannot coexist.  Therefore
this branch is now **proved impossible without computation**.  This does not
refute the unrestricted equality case, because a length-465 solution need not
use the canonical single-switch maximal-shadow/rainbow-core ansatz.

This is stronger than merely fixing the `02|03` ordered-witness schedule in
the existing full-array solver.  That arithmetic branch fixes which selected
rank-six witnesses are triples or quadruples; it does not by itself impose
the rainbow meet triangle, upper union triangle, or twelve-cell reservoir
labeling designed here.

The key compression is that the search object is a permutation of the `462`
six-sets.  No array entries and no witnesses for all `2047` targets are needed.
Once the row is found, the array is reconstructed coordinatewise.  The only
factor-label problem left after the row search is a `12` by `12` boundary
assignment with a constant-size pin test.

## 2. Exact `k=11` geometry

Put

\[
k=11,\qquad r=6,\qquad M=\binom{11}{6}=462,
\qquad d=3,\qquad n=M+d=465.
\]

There are

\[
L=\sum_{s=1}^{5}\binom{11}{s}=1023
\]

nonempty lower masks, and the arithmetic short-cell surplus is

\[
\sigma=3M+\binom42-L=369.
\]

For a proposed rank-six row

\[
C=(C_1,\ldots,C_{462}),
\]

use the prescribed central intervals

\[
I_i=[i,\rho_i],\qquad
\rho_i=\begin{cases}
i+2,&1\le i\le369,\\
i+3,&370\le i\le462.
\end{cases}                                      \tag{2.1}
\]

Thus the first `369` central witnesses are triples and the final `93` are
quadruples.  The central right endpoints omit exactly `1,2,372`.

For `p<q`, the literal common core is

\[
J_{p,q}=\bigcap_{i=p}^{q}I_i=[q,\rho_p].          \tag{2.2}
\]

The `1011` nontrivial feasible cores are exactly

\[
\begin{array}{ll}
C_p\cap C_{p+1},
\quad C_p\cap C_{p+1}\cap C_{p+2},
  &1\le p\le369,\\[1mm]
C_p\cap C_{p+1},
  &370\le p\le461,\\
C_p\cap C_{p+1}\cap C_{p+2},
  &370\le p\le460,\\
C_p\cap C_{p+1}\cap C_{p+2}\cap C_{p+3},
  &370\le p\le459.
\end{array}                                      \tag{2.3}
\]

Their count is

\[
369+369+92+91+90=1011.                            \tag{2.4}
\]

The twelve reservoir cells are

\[
\begin{array}{lll}
K_1=[1,1],&K_2=[1,2],&K_3=[2,2],\\
K_4=[370,372],&K_5=[371,372],&K_6=[372,372],\\
K_7=[463,463],&K_8=[463,464],&K_9=[463,465],\\
K_{10}=[464,464],&K_{11}=[464,465],&K_{12}=[465,465].
\end{array}                                      \tag{2.5}
\]

Together, the `369` shortened central cells, the `1011` cores, and these
`12` cells partition all

\[
465+464+463=1392
\]

physical intervals of lengths at most three.

## 2A. No-go theorem: the rainbow bulk is already impossible

### Theorem

Let `q` be the number of nonempty lower masks omitted by any pairwise-distinct
nonzero family containing all `461` adjacent-pair cores and all `460`
consecutive-triple cores of a rank-six permutation.  Then

\[
q\ge66.                                           \tag{2A.1}
\]

In particular, Gate R2 would omit only

\[
q=1023-1011=12,
\]

so no row can satisfy Gate R2.  The full branch is UNSAT even before imposing
mixed runs, upper shadows, reservoir labels, or pin survival.

### Proof

Every adjacent-pair intersection

\[
P_i=C_i\cap C_{i+1},\qquad1\le i\le461,
\]

is a selected core.  A deeper selected core cannot have rank five: it is
contained in one of its adjacent-pair cores, whose rank is at most five, so a
rank-five deeper core would equal that pair core and violate distinctness.
Thus every represented rank-five mask occurs among the `461` pair cores.

At most `q` of the `462` rank-five masks are omitted.  Hence at least `462-q`
pair cores have rank five, leaving at most

\[
461-(462-q)=q-1                                  \tag{2A.2}
\]

lower-rank pair cores.

There are `460` consecutive-triple cores

\[
T_i=C_i\cap C_{i+1}\cap C_{i+2}=P_i\cap P_{i+1},
\qquad1\le i\le460.
\]

If both `P_i` and `P_(i+1)` have rank five, they are distinct five-subsets of
the common six-set `C_(i+1)`.  They omit different elements of that six-set,
so their intersection `T_i` has rank exactly four.  Each of the at most
`q-1` exceptional pair cores can affect at most two triples.  Therefore at
least

\[
460-2(q-1)=462-2q                                \tag{2A.3}
\]

triple cores are rank-four masks.

The selected cores, hence these triple cores, are distinct.  But the
eleven-cube contains only

\[
\binom{11}{4}=330
\]

rank-four masks.  Consequently `462-2q<=330`, which is exactly `q>=66`.
This contradicts `q=12`.  \(\square\)

### Optional reservoir sharpening

The reservoir poset gives an even larger numerical contradiction, although
it is not needed.  Only its three maximal cells `K_2,K_4,K_9` can carry
distinct rank-five lower labels.  Thus at most three omitted masks can have
rank five, at least `459` pair cores have rank five, and at least `456` triple
cores are forced to be distinct rank-four masks.  The primary theorem is
stronger conceptually because it proves Gate R2 impossible without using any
reservoir property.

### Consequence for the implementation

The evaluator, exact reservoir solver, reconstruction, and verifier below are
retained as machine-checkable regression tools for the theorem's geometry.
The heuristic search must not be launched: it is searching an empty branch.
Further `k=11` work must relax at least one of the following:

* the canonical single-switch schedule;
* the requirement that all `1011` feasible meet cores be distinct;
* the demand that precisely those cores plus the twelve reservoir cells
  saturate the entire lower ideal.

## 3. The smallest constructive row state

The natural C++ state is simply

```text
uint16_t C[462]
```

containing every eleven-bit mask of popcount six exactly once.  In this
representation rank six and permutation constraints are true by construction;
permutation-preserving moves never need to reconsider them.

A row is accepted precisely when it passes the following three gates.

### Gate R1: exact mixed factorability

For every coordinate, every internal positive run `[a,b]` in its incidence
word must satisfy

\[
b-a+1\ge
\begin{cases}
3,&a\le370,\\
4,&a\ge371.
\end{cases}                                      \tag{3.1}
\]

Runs touching either end of the row are unrestricted.  This is necessary and
sufficient for the central schedule (2.1) to factor.

Equivalently, for each coordinate the following internal patterns are
forbidden:

* starts `2,...,370`: `010` and `0110`;
* starts `371,...,461`: `010`;
* starts `371,...,460`: `0110`;
* starts `371,...,459`: `01110`.

There are exactly

\[
11(369+369+91+90+89)=11088                   \tag{3.2}
\]

such constant-width forbidden-pattern clauses in a Boolean encoding.

### Gate R2: a rainbow nonzero bulk meet triangle

Compute the `1011` masks in (2.3).  Require all of them to be nonzero and
pairwise distinct.

No separate rank constraint is needed.  Every core involves at least two
distinct rank-six row values, so every such intersection automatically has
rank at most five.  Therefore Gate R2 produces exactly `1011` different
members of the `1023`-element punctured lower ideal.

### Gate R3: the complete upper union triangle

Require that, for every mask `T` of rank `7,8,9,10,11`, there is a nonempty
consecutive block with

\[
C_p\cup C_{p+1}\cup\cdots\cup C_q=T.             \tag{3.3}
\]

There are

\[
\binom{11}{7}+\binom{11}{8}+\binom{11}{9}
 +\binom{11}{10}+\binom{11}{11}=562              \tag{3.4}
\]

upper targets.  The full rank-eleven target is automatic from the rank-six
permutation, but retaining it in the verifier is harmless.

All consecutive unions can be enumerated in `O(Mk)` time by the standard
distinct-suffix-OR recurrence.  At one right endpoint there are at most six
different suffix unions because their ranks form a strict chain from six to
eleven.

## 4. What follows automatically from the three row gates

Several apparently global constraints require no search variables.

1. **All central masks.**  The row itself is the entire rank-six layer.
2. **All but twelve lower masks.**  Gate R2 leaves the exact complement

   \[
   \mathcal D=\{S:1\le |S|\le5\}
       \setminus\{\text{the 1011 core values}\},
   \qquad |\mathcal D|=12.                         \tag{4.1}
   \]

   Thus there are no variables selecting which masks remain; they are
   computed from the row.
3. **Literal bulk witnesses.**  Gate R1 and the maximal-shadow theorem imply
   that every core in (2.3) is the exact OR of its physical interval (2.2)
   in the maximal factor.
4. **Literal upper witnesses.**  Every factor which still realizes all
   central intervals realizes (3.3) on the physical hull `[p,rho_q]`.
   Consequently sparse boundary repair can never damage Gate R3 once the
   central pins survive.
5. **All negative-bit conditions.**  They are enforced automatically by the
   legal-position construction below.  Only positive pins need testing.

These were the compression identities motivating the row search.  The no-go
theorem in Section 2A now shows that Gate R2 makes the compressed target empty.

## 5. The exact twelve-cell reservoir problem

Fix a row passing R1--R3, list the twelve masks in `mathcal D`, and choose a
bijection

\[
\pi:\{K_1,\ldots,K_{12}\}\longrightarrow\mathcal D.
                                                               \tag{5.1}
\]

For coordinate `x`, first define the central legal set

\[
Z_x=\{j:x\in C_i\text{ for every }i\text{ with }j\in I_i\}.
                                                               \tag{5.2}
\]

After assigning the reservoir, the surviving legal set is

\[
Z'_x=Z_x\setminus
 \bigcup_{a:x\notin\pi(K_a)}K_a.                  \tag{5.3}
\]

The reconstructed factor is deterministic:

\[
A_j=\{x:j\in Z'_x\},\qquad1\le j\le465.           \tag{5.4}
\]

The assignment is valid if and only if the following positive pins all
survive:

\[
\begin{array}{ll}
I_i\cap Z'_x\ne\varnothing,&x\in C_i,\\
J_{p,q}\cap Z'_x\ne\varnothing,&
 x\in C_p\cap\cdots\cap C_q,\\
K_a\cap Z'_x\ne\varnothing,&x\in\pi(K_a).
\end{array}                                      \tag{5.5}
\]

These are necessary and sufficient, not a relaxation.

### 5.1 A tiny SAT encoding after the row is fixed

Let `D_1,...,D_12` be the masks in (4.1).  Introduce only

\[
y_{a,t}\quad(1\le a,t\le12),                     \tag{5.6}
\]

where `y_(a,t)` means `pi(K_a)=D_t`.  The `144` primary variables obey one
exactly-one constraint in every row and every column.

For a convenient Tseitin encoding one may additionally use

\[
\ell_{a,x}=1_{x\in\pi(K_a)}\quad(132\text{ variables})
\]

and one local legal variable for each of the `8*11=88` pairs
`(j,x)` with `j` in the modification zone.  The complete fixed-row reservoir
instance therefore has only `144` primary variables, or `364` variables with
all convenient auxiliaries.  Pairwise exactly-one clauses are already tiny;
a sequential encoding is optional.

A cheap necessary candidate edge is

\[
D_t\subseteq\bigcup_{j\in K_a}\{x:j\in Z_x\}.     \tag{5.7}
\]

Deleting all `y_(a,t)` which fail (5.7), then checking a bipartite perfect
matching, is a useful preliminary filter.  It is not sufficient because two
different reservoir labels can delete one another's pins.

There is also a free order-theoretic filter.  Physical interval containment
forces label containment:

\[
K_a\subsetneq K_b\Longrightarrow
\pi(K_a)\subsetneq\pi(K_b),                       \tag{5.7a}
\]

where strictness follows because the twelve labels are distinct.  In
particular, the switch labels form the three-chain

\[
\pi(K_6)\subsetneq\pi(K_5)\subsetneq\pi(K_4),
\]

the left labels satisfy `pi(K_1),pi(K_3) subsetneq pi(K_2)`, and the terminal
six labels must embed the interval-containment poset on three points.  Its
cover relations are

```text
K7 < K8,   K10 < K8,   K8 < K9,
K10 < K11, K12 < K11,  K11 < K9.
```

These binary compatibility clauses drastically reduce the `12!` nominal
search before any pin formula is evaluated.

### 5.2 Explicit local Boolean formulas

The modification zone is exactly

\[
\Omega=\{1,2,370,371,372,463,464,465\}.            \tag{5.8}
\]

Writing juxtaposition for conjunction and `ell_(a,x)` for the bit of the
label on `K_a`, the only changed legal-position formulas are

\[
\begin{array}{ll}
z'_{x,1}=C_{1,x}\ell_{1,x}\ell_{2,x},
&z'_{x,2}=C_{1,x}C_{2,x}\ell_{2,x}\ell_{3,x},\\
z'_{x,370}=C_{368,x}C_{369,x}C_{370,x}\ell_{4,x},
&z'_{x,371}=C_{369,x}C_{370,x}C_{371,x}
             \ell_{4,x}\ell_{5,x},\\
z'_{x,372}=C_{370,x}C_{371,x}C_{372,x}
             \ell_{4,x}\ell_{5,x}\ell_{6,x},\\
z'_{x,463}=C_{460,x}C_{461,x}C_{462,x}
             \ell_{7,x}\ell_{8,x}\ell_{9,x},\\
z'_{x,464}=C_{461,x}C_{462,x}
             \ell_{8,x}\ell_{9,x}\ell_{10,x}\ell_{11,x},\\
z'_{x,465}=C_{462,x}
             \ell_{9,x}\ell_{11,x}\ell_{12,x}.
\end{array}                                      \tag{5.9}
\]

For each proposed assignment `y_(a,t)`, every bit of `D_t` adds the
conditional reservoir-pin clause

\[
y_{a,t}\Longrightarrow
 \bigvee_{j\in K_a}z'_{x,j}.                      \tag{5.10}
\]

The central and meet labels are fixed once the row is fixed, so their
remaining conditions are ordinary disjunctions of the relevant `z'` values.

### 5.3 The complete list of potentially affected old witnesses

Only ten central intervals meet `Omega`:

\[
I_1,I_2, I_{368},I_{369},I_{370},I_{371},I_{372},
 I_{460},I_{461},I_{462}.                          \tag{5.11}
\]

Only eleven nontrivial meet cores meet `Omega`:

\[
\begin{array}{lll}
J_{1,2}=[2,3],\\
J_{368,369}=[369,370],&J_{368,370}=[370,370],\\
J_{369,370}=[370,371],&J_{369,371}=[371,371],\\
J_{370,371}=[371,373],&J_{370,372}=[372,373],
 &J_{371,372}=[372,374],\\
J_{460,461}=[461,463],&J_{460,462}=[462,463],
 &J_{461,462}=[462,464].
\end{array}                                      \tag{5.12}
\]

For a fixed row, even a condition from (5.11)--(5.12) is automatic if its
old legal pin set contains a point outside `Omega`.  Thus an implementation
should generate clauses only for the genuinely vulnerable `(interval,bit)`
pairs.  Before this filtering there are at most

\[
10\cdot6+11\cdot5+12\cdot5=175                  \tag{5.13}
\]

positive-pin tests.  This is the concrete `O(kd^2)` residual gate.

## 6. A compact exact SAT/CEGAR row formulation

The following formulation is retained to make the refuted branch completely
machine-checkable.  It must not be launched as a search.  Before the no-go
theorem was noticed, it would have been far smaller than the unrestricted
array formula.

Let `V` be the `462` rank-six masks.

* `p_(i,v)` says row position `i` contains vertex `v`: `462^2=213444`
  variables.
* `c_(i,x)` is the coordinate incidence bit: `462*11=5082` variables.
* `m_(e,x)` is the bit of one of the `1011` meet cores:
  `1011*11=11121` variables.

Thus the static semantic core has

\[
213444+5082+11121=229647                         \tag{6.1}
\]

variables before cardinality auxiliaries.

Permutation can be encoded economically by:

1. one at-least-one clause for every position;
2. one exactly-one constraint for every vertex column.

There are `462` true column variables in total and `462` nonempty rows, so
row at-most-one constraints follow by counting.  With a sequential AMO only
on the columns, this uses `462*461=212982` auxiliary variables rather than
duplicating row and column AMOs.

Channel incidence by

\[
p_{i,v}\Longrightarrow c_{i,x}\quad(x\in v),
\qquad
c_{i,x}\Longrightarrow\bigvee_{v\ni x}p_{i,v}.   \tag{6.2}
\]

This uses `213444*6=1280664` binary implications and `5082` reverse
clauses.  Since each row selects one vertex, clauses for `x notin v` are
unnecessary.

Define each meet bit as the conjunction of the two, three, or four
incidence bits in its block.  The total sum of block lengths is

\[
369\cdot2+369\cdot3+92\cdot2+91\cdot3+90\cdot4
=2662,                                           \tag{6.3}
\]

so all meet equivalences take only

\[
11(2662+1011)=40403                              \tag{6.4}
\]

clauses, plus `1011` nonzero clauses.

With the standard `3n-4`-clause sequential AMO on each of the `462` vertex
columns, the whole static base before collision and upper-witness cuts has
approximately

\[
442629\text{ variables},\qquad1977656\text{ clauses}.           \tag{6.4a}
\]

This count includes `212982` sequential-counter auxiliaries.  It is a useful
scale comparison, not a claim that this particular cardinality encoding is
optimal.

Do **not** statically encode all pairwise meet inequalities.  When two cores
`e,f` collide at the concrete mask `S`, add the single 22-literal cut

\[
\neg[m_e=S]\ \lor\ \neg[m_f=S].                  \tag{6.5}
\]

Repeated separation is finite and usually much smaller than the roughly
`5.6` million XOR auxiliaries of a static pairwise encoding.

Upper targets should also be separated lazily.  For a missing target `T`,
add one exact interval-witness module.  A linear three-state automaton
(`before`, `inside`, `after`) chooses a nonempty contiguous set of row
positions.  Inside positions must satisfy `C_i subseteq T`, and for each
`x in T` at least one inside position must contain `x`.  This is equivalent
to saying that the chosen interval union is exactly `T`.  The module needs
only `O(M|T|)` variables and clauses and is added at most once for each of
the `561` nonautomatic upper targets.

An independent verifier separates, in this order:

1. meet collisions;
2. missing rank-seven unions;
3. missing ranks eight, nine, and ten.

The rank-seven constraints are usually the rigid part.  A rank-seven target
is covered exactly when two adjacent row vertices are both six-subsets of
it; no longer dedicated witness module is needed for that rank.

The twelve-cell SAT of Section 5 is run only after a row passes every row
gate.  This avoids introducing `12*1023` possible reservoir-label variables
or more than a million meet-to-mask equality indicators into the row CNF.

## 7. Archived staged constructive design — do not run

Section 2A proves that no state can pass Stage A's bulk gate.  The implementation
therefore exposes only the evaluators and exact checkers and refuses a heavy
`--search` command.  The stages below document the abandoned design so its
constraints and tests remain reproducible.

### Stage A: permutation-preserving C++ search

Use a known middle-level/rank-six path or an existing `k=11` checkpoint as a
seed.  Search directly on the `462` masks with moves that preserve the
permutation:

* adjacent swaps and short block rotations;
* Johnson-valid 2-opt reversals when preserving useful rank-seven edges;
* three-edge segment relocation;
* paired block moves across the `369|93` switch.

Maintain the lexicographic score

```text
(mixed_run_deficit,
 zero_bulk_cores,
 1011 - distinct_nonzero_bulk_cores,
 missing_rank7,
 missing_rank8,
 missing_rank9,
 missing_rank10,
 reservoir_infeasibility)
```

or use several portfolios with the lower and upper terms interchanged.  A
full score recomputation is cheap: `1011` intersections, `5082` incidence
bits, and at most `6*462` distinct suffix unions.

The preliminary reservoir score can be the deficiency of the containment
matching (5.7).  Invoke the exact `144`-variable pin SAT only after this
matching is perfect and the row gates are nearly or fully complete.

### Stage B: exact reservoir assignment

For every row passing R1--R3:

1. compute the twelve-mask complement (4.1);
2. remove impossible assignment edges using (5.7);
3. solve the `12` by `12` bijection with (5.9)--(5.12);
4. reconstruct all `465` entries from (5.4);
5. verify all `465*466/2=108345` physical intervals and, independently,
   the distinct-suffix-OR recurrence.

If Stage B is UNSAT, this is only a local rejection of that row.  Its small
UNSAT core identifies which boundary tuple and missing masks should be
changed by the next C++ move.

### Stage C: exact branch-and-cut fallback

If heuristic row search stalls, use the `229647`-variable semantic SAT core
of Section 6 with lazy meet and upper-shadow separation.  This searches the
same mathematical object and remains independent of the unrestricted array
CNF.  A final SAT model plus the twelve-cell assignment is a complete
constructive certificate.  An UNSAT proof is a theorem only about the
single-switch branch.

## 8. Counterfactual certificate check

For completeness, suppose the checkers were given a row and reservoir
assignment despite Section 2A.

* R1 makes the row factorable on (2.1).
* R2 and the maximal-shadow theorem realize `1011` distinct nonzero lower
  masks on the cores (2.2).
* The reservoir complement and the exact pin test realize the other twelve
  lower masks while preserving every central mask and every selected core.
* The row is a rank-six permutation, so all central masks occur.
* R3 and the hull identity realize every upper mask in the same sparse
  factor.

Hence (5.4) covers all `2047` nonzero masks in `465` positions.  The proved
rank-count lower bound is `465`, so this factor is globally shortest even
though the searched branch was only sufficient.  Prepending one zero gives
the globally shortest answer to the original problem at `k=11`, of length
`466`.

The counterfactual checker decomposes the branch into

\[
\boxed{
\text{one 462-vertex rank-six permutation}
+\text{ one 144-variable boundary assignment}.}
\]

There would be no remaining global pin-label SAT once the central row existed,
but Section 2A proves that the required row does not exist.  The actual
`k=11` problem must therefore return to the unrestricted monotone-band/
endpoint-forest formulation or use a different variable-window schedule.
