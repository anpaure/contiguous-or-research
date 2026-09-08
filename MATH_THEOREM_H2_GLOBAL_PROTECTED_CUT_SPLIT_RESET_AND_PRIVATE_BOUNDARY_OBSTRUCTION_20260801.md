# Global protected-cut rotation, one-split flag normalization, and the private-boundary obstruction

Date: 2026-08-01  
Lane: H2, regenerative split sidecar  
Status: exact interval-word theorem, exact matching-safe reset criterion, and
an exact no-automatic-contraction family.  A Pascal/Johnson host, deadline
acceptance, and common-cap feasibility are hypotheses, not conclusions.

## 0. Outcome

Write a linear source word as

\[
                              W=P\,M\,Q
\]

and rotate whole blocks to (W^*=M\,Q\,P).  The physical-cell change is
exact.  Intervals internal to (P), and all intervals internal to (MQ)
(including every interval crossing (M\mid Q)), are unchanged.  The lost
cells are precisely

\[
                    \operatorname{Suf}(P)\,
                    \operatorname{Pre}(MQ),               \tag{0.1}
\]

and the gained cells are precisely

\[
                    \operatorname{Suf}(MQ)\,
                    \operatorname{Pre}(P).                \tag{0.2}
\]

Both families have (|P|(|M|+|Q|)) physical cells.  Equality here is at the
cell level; their OR values may collide.

For the endpoint carves

\[
\begin{aligned}
 P&=(T,\{f_{d-1}\},\ldots,\{f_2\}),
       &&T=B\cup\{f_d\},\\
 Q&=(\{f_{d-1}\},\ldots,\{f_2\},Z),
       &&Z=A\cup\{f_1\},                                  \tag{0.3}
\end{aligned}
\]

the new (Q\mid P) seam is

\[
                 \cdots,\{f_2\},Z,T,\{f_{d-1}\},\cdots . \tag{0.4}
\]

It has the two exact flag rays

\[
 \alpha_i=A\cup\{f_1,\ldots,f_i\}\quad(1\le i\le d-1),
 \qquad
 \beta_j=B\cup\{f_j,\ldots,f_d\}\quad(2\le j\le d),     \tag{0.5}
\]

and the ((d-1)^2) physical cross-grid cells

\[
                              \alpha_i\cup\beta_j.         \tag{0.6}
\]

The flag values in (0.5) already existed inside (Q) and (P) before the
rotation.  What the rotation supplies is adjacency: contract (Z,T) to the
one actual letter (X=Z\cup T), and (0.5) becomes exactly the two **carved
local** partial-endpoint rays of the single marked split
(X\mapsto Z,T).  The grid
(0.6) consists of full-block lifts through (X).  Thus the rotation gives a
one-boundary normalization, not automatic creation of new flag masks.

There is an exact conditional reset theorem.  Put into one residual bank all
old rows not represented by frozen admissible assignments after rotation and
coarsening--including lost-cut, relocation-inadmissible, and
contraction-invalid rows--together with (0.5) and all new tasks.  If this bank
has a saturating matching to free admissible cells and the combined matching
passes every coupled guard, then, after contracting (g) old marked
boundaries,

\[
                              \Phi'\le\Phi-g+1.            \tag{0.7}
\]

Full reclaim gives (Phi'\le1), and (g\ge\theta\Phi) gives
(Phi'\le(1-\theta)\Phi+1).

The Hall antecedent is indispensable.  For every (d\ge2) and every
(t\ge1), there is a literal word for which the rotation preserves the
entire old interval-OR deck and (0.4)--(0.6) hold, but (t) private marked
boundaries inside (M) remain essential.  Hence the global wrap does not by
itself reclaim even one old boundary, let alone a positive fraction.

## 1. Exact physical-cell partition

For a nonempty word (R=(r_0,\ldots,r_{s-1})), write

\[
 \operatorname{Pre}_j(R)=(r_0,\ldots,r_j),\qquad
 \operatorname{Suf}_i(R)=(r_i,\ldots,r_{s-1}),             \tag{1.1}
\]

and use \(\bigvee R\) for the union of its letters.  Physical cells retain
their labelled source occurrences, so two cells with equal OR values remain
distinct.

### Theorem 1.1 (rotation partition)

Let (P,M,Q) be nonempty labelled words.  Between (W=PMQ) and
(W^*=MQP):

1. the common physical cells are exactly the intervals internal to (P)
   together with the intervals internal to (MQ);
2. the lost physical cells are exactly
   
   \[
       \operatorname{Suf}_i(P)\operatorname{Pre}_j(MQ);
                                                               \tag{1.2}
   \]
3. the gained physical cells are exactly
   
   \[
       \operatorname{Suf}_i(MQ)\operatorname{Pre}_j(P).        \tag{1.3}
   \]

Consequently both exceptional families have
(|P|(|M|+|Q|)) cells.  More explicitly, the lost OR values are

\[
\begin{array}{ll}
 \bigvee\operatorname{Suf}_i(P)\cup
 \bigvee\operatorname{Pre}_j(M),
     &\text{when the old endpoint lies in }M,\\[1mm]
 \bigvee\operatorname{Suf}_i(P)\cup\bigvee M\cup
 \bigvee\operatorname{Pre}_j(Q),
     &\text{when it lies in }Q,                              \tag{1.4}
\end{array}
\]

and the gained OR values are

\[
\begin{array}{ll}
 \bigvee\operatorname{Suf}_i(Q)\cup
 \bigvee\operatorname{Pre}_j(P),
     &\text{when the new start lies in }Q,\\[1mm]
 \bigvee\operatorname{Suf}_i(M)\cup\bigvee Q\cup
 \bigvee\operatorname{Pre}_j(P),
     &\text{when it lies in }M.                              \tag{1.5}
\end{array}
\]

#### Proof

An interval has the same labelled occurrence sequence in both orders exactly
when it lies wholly in the unchanged block (P), or wholly in the unchanged
concatenation (MQ).  Every other old interval begins in (P) and ends in
(M) or (Q), which is (1.2).  Every other new interval begins in (M) or
(Q) and ends in (P), which is (1.3).  Choosing the two endpoints gives
the counts.  Taking unions and separating the endpoint according to its
block gives (1.4)--(1.5).  \(square\)

In particular, (M\mid Q) is not a damaged seam.  All damage is charged to
the old (P\mid M) cut, including the cells which continue through all of
(M) into a prefix of (Q).

## 2. Cover-safe and matching-safe protected cuts

Let ({\cal I}_{\rm com},{\cal I}_{\rm lost},{\cal I}_{\rm new}) be the
three cell banks in Theorem 1.1.

### Corollary 2.1 (ordinary coverage)

The rotation preserves every old interval-OR value if and only if

\[
 \{\bigvee I:I\in{\cal I}_{\rm lost}\}
 \subseteq
 \{\bigvee I:I\in{\cal I}_{\rm com}\cup{\cal I}_{\rm new}\}. \tag{2.1}
\]

This is the exact unlabelled protected-cut test.  Counts of lost and gained
cells are not sufficient because their values can have unrelated
multiplicities.

### Theorem 2.2 (fixed-matching Hall test)

Let (mu) be an occurrence-labelled target-to-cell matching in (W).  Keep
exactly those assignments whose cell lies in ({\cal I}_{\rm com}) **and
remains admissible at its relocated position in \(W^*\)**.  Let (D) contain
every other old target row (whether its cell was lost or merely became
inadmissible after relocation), together with any new task rows to be
installed.  Let \(C_{\rm free}\) be all
admissible cells of (W^*) not occupied by the retained assignments.  Here
admissibility means cell-local conditions such as value, width, or deadline;
constraints coupling several selected cells are checked after the matching
is chosen.  Form the equality graph

\[
 dJ\in E \quad\Longleftrightarrow\quad
             \bigvee J=d
       \quad\text{and }J\text{ passes every stated cell-local guard}. \tag{2.2}
\]

The fixed common part of (mu) extends after rotation if and only if

\[
                         |N(Y)|\ge |Y|\qquad(Y\subseteq D).      \tag{2.3}
\]

#### Proof

The retained common assignments remain admissible literal equalities on
distinct cells.  All
remaining rows must use \(C_{\rm free}\); Hall's theorem is exactly (2.3).
\(square\)

Allowing the common part itself to move simply replaces (2.3) by Hall on all
target rows and all admissible cells of (W^*).  No marginal target count,
deck inclusion, or scalar capacity implies this occurrence-labelled test.
Hall is exact for the equality matching only.  A topology, common-cap, or
other constraint depending jointly on several chosen cells remains a
separate condition on the combined selected matching.

## 3. The carved seam and its full cross-grid

Assume (d\ge2).  Let \(A,B\) be arbitrary nonempty sets, possibly
overlapping, and let \(f_1,\ldots,f_d\) be distinct labels outside
\(A\cup B\).  Define (P,Q,Z,T) by (0.3).  For (i,j) in the
ranges of (0.5), the suffix of (Q) beginning at ({f_i}) (with the
singleton (Z) used for (i=1)) has OR (alpha_i).  The prefix of (P)
ending at ({f_j}) (with the singleton (T) used for (j=d)) has OR
\(\beta_j\).

### Theorem 3.1 (one-split flag and grid identity)

In (W^*=MQP):

1. the (d-1) displayed suffix cells of (Q) have values
   (alpha_1,\ldots,alpha_{d-1});
2. the (d-1) displayed prefix cells of (P) have values
   \(\beta_d,\ldots,\beta_2\);
3. for every pair ((i,j)), the physical cell crossing (Q\mid P) from the
   left-ray start of (alpha_i) to the right-ray end of \(\beta_j\) has
   value
   
   \[
                              \alpha_i\cup\beta_j.          \tag{3.1}
   \]

There are exactly ((d-1)^2) such physical cells.  Their values need not be
distinct.

Now contract the adjacent letters (Z,T) to (X=Z\cup T).  The contracted
word is

\[
 M,(\{f_{d-1}\},\ldots,\{f_2\}),X,
   (\{f_{d-1}\},\ldots,\{f_2\}).                          \tag{3.2}
\]

Expanding (X\mapsto Z,T) recovers (W^*).  Every cell in (3.1) is the
full-block lift of the corresponding cell through (X).  The cells
\(\alpha_i\) and \(\beta_j\) are precisely the local left and right
partial-endpoint rays.  Hence one actual split boundary carries both flags
while preserving every interval of the contracted core.

#### Proof

The suffix and prefix unions telescope along the two reversed singleton
filler traces, proving (0.5).  Concatenating one suffix and one prefix gives
(3.1).  It contains both (Z) and (T), so after contraction it contains
the whole letter (X); conversely its expansion is the same physical cell.
Cells ending at (Z), or beginning at (T), omit exactly one half and are
the two partial rays.  The general block-contraction lemma preserves every
full-block cell.  \(square\)

The theorem makes a useful scope distinction.  Rotation does not newly
cover (0.5): those cells were already internal to (Q) and (P), hence are
in ({\cal I}_{\rm com}).  It makes the two banks adjacent and therefore
normalizes them to one actual split of (X).  It also creates the cross-grid
(3.1), which belongs to the first line of the gained family (1.5).

## 4. Exact conditional regenerative reset

Let an old state have a chosen \(\Phi\)-minimizing protected refinement
presentation with (Phi) marked boundaries and an occurrence-labelled
matching.  Assume every marked replacement block in this chosen presentation
lies wholly inside (P) or wholly inside
(MQ), so the rotation transports its pieces without separating them.  In
particular, the old cut (P\mid M) is between refinement blocks, not inside
one.  Perform the
rotation, regard (Z\mid T) as one new marked boundary of (X), and choose a
set (R) of (g) old boundaries to contract.  Freeze any assignments which
remain admissible and literal after these operations.  Put in one residual
bank:

* every old target row not represented by a frozen assignment, including
  lost-cut, relocation-inadmissible, and contraction-invalid rows;
* the two flag banks (0.5), unless already saturated by retained cells; and
* every genuinely new transition task.

### Theorem 4.1 (protected-cut split reset)

If this residual bank satisfies Hall against distinct admissible cells of the
rotated, coarsened, (Z\mid T)-split word **not occupied by the frozen
assignments**, and if one resulting residual matching together with the
frozen assignments passes the required owner, Johnson, residence, deadline,
upper, topology and common-cap guards, then

\[
                              \Phi'\le\Phi-g+1.            \tag{4.1}
\]

In particular, contracting all old essential boundaries gives
(Phi'\le1).  Contracting at least \(\theta\Phi\) gives

\[
                         \Phi'\le(1-\theta)\Phi+1.          \tag{4.2}
\]

#### Proof

The residual Hall matching, together with the frozen assignments, preserves
all protected and new rows.  The only retained marked boundaries are the
(Phi-g) uncontracted old ones and (Z\mid T).  This proves (4.1), and
(4.2) follows immediately.  \(square\)

This is the strongest reset implication provided by the rotation.  The
theorem does not assert its Hall or physical antecedents.  In particular,
the (2(d-1)) flag cells can already saturate the complete local ray bank;
they are not spare occurrence capacity for unrelated old rows.

## 5. A deck-safe rotation with zero boundary reclaim

The missing antecedent is real even at the interval-word level.

Fix (d\ge2) and the carves (0.3).  Choose a nonempty private core (K),
pairwise fresh labels (a_i,b_i), and put

\[
 C_i=K\cup\{a_i\},\qquad D_i=K\cup\{b_i\},\qquad
 X_i=C_i\cup D_i\quad(1\le i\le t).                       \tag{5.1}
\]

Let (Omega) be the union of every label used by (P,Q,C_i,D_i), and set

\[
                 M=(\Omega,C_1,D_1,\ldots,C_t,D_t).        \tag{5.2}
\]

Protect the singleton target row (C_i) at every marked boundary
(C_i\mid D_i).

### Theorem 5.1 (private-boundary obstruction)

For every (d\ge2,t\ge1):

1. (PMQ\mapsto MQP) preserves every old interval-OR value;
2. the seam satisfies the complete flag and grid identities of Theorem 3.1;
3. none of the (t) marked boundaries in (5.2) is contractible while
   preserving all (C_i).

Thus (g=0), although the cut is cover-safe and the one-split flag host is
present.

#### Proof

By Theorem 1.1, every lost old cell starts in (P) and crosses into (M).
It therefore contains the first middle letter (Omega), so its OR is
(Omega).  The singleton middle cell (Omega) survives the rotation.
Every other old cell is common.  This proves complete deck preservation.

Theorem 3.1 applies verbatim because the private middle does not change the
local (Q\mid P) seam.

The cell (C_i) is a singleton witness for its protected row.  After
contracting (C_i,D_i), the replacement (X_i) contains the extra private
label (b_i).  Every other singleton letter either omits (K), contains a
different private label, or is (Omega); every interval of at least two
letters contains an extra label.  Hence no interval has OR (C_i).  This
argument is independent for all (i), so simultaneous contraction of any
nonempty subset loses at least the corresponding protected row.  \(square\)

The construction is an abstract source-word obstruction.  It does not claim
that (5.2) is a Pascal inverse, a Johnson source, or a common-cap word.  It
does prove that protected global rotation plus exact flag planting alone
cannot imply a positive reclaim fraction.

## 6. Surviving all-dimensional gate

The global carve changes the regenerative question from local host existence
to one exact correlated certificate:

1. the old (P\mid M) cut must pass the fixed-matching Hall test (2.3), not
   merely an unlabelled deck test;
2. the contraction (3.2) and its re-expansion must be accepted by the actual
   Pascal/Johnson/deadline/common-cap guards;
3. the new seam matching must rehouse the dependency rows of all, or a fixed
   fraction, of the old essential boundaries.

Rows 1--2 give a legal cost-one terminal host.  Row 3 is exactly the missing
regenerative contraction theorem.  Without it the rotation changes the
normal form but proves no bound stronger than (Phi'\le\Phi+1).

## 7. Independent finite replay

Run

```text
python3 scratch/audit_h2_global_protected_cut_split_reset_20260801.py
```

The dependency-free audit:

* exhausts all nonempty two-bit words for every block-size triple
  (|P|,|M|,|Q|\in\{1,2\}), checking the physical common/lost/gained
  partition and every value formula;
* replays both flag rays, all ((d-1)^2) physical cross-grid cells, and every
  full-block contraction lift for (2\le d\le32), and separately repeats the
  seam identities with nonempty \(A\cap B\); and
* replays the deck-safe private-boundary family for (2\le d\le8) and
  (1\le t\le8), including every simultaneous contraction subset.

It reports

```text
PASS_H2_GLOBAL_PROTECTED_CUT_SPLIT_RESET
payload_sha256=4026c2cbcef356488294b203d7f739ed15d432918af87f195a5ac1019dbb1d6b
```

No claim here proves an unrestricted Pascal host, fixed-width compiler,
common-cap assignment, or all-(k) recurrence.
