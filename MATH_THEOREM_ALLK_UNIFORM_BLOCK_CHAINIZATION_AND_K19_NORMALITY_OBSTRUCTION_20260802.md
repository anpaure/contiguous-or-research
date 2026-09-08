# All-`k` uniform-block chainization and the exact K19 normality obstruction

**Date:** 2026-08-02  
**Status:** unconditional static coupling/chainization theorems, an
unconditional `\(2d+1\)` owner-chain factor, and exact finite/asymptotic
obstructions to the consecutive whole-rank route. The same-depth K19
partial-rank repair was subsequently closed by the fixed-triple theorem
cited in Section 5. An all-`k` `\(d+O(1)\)` block system and every literal
serialization statement remain explicitly **unproved**.

## 0. Verdict

Assume \(k\ge3\); the smaller dimensions are immediate. Put

\[
 r=\left\lceil\frac k2\right\rceil,
 \qquad W={k\choose r},
 \qquad \mathcal L=\{S\subseteq[k]:1\le |S|<r\},
 \qquad \Lambda=|\mathcal L|,
\]

and

\[
 d=\min\left\{q:qW+{q+1\choose2}\ge\Lambda\right\},
 \qquad B(k)=W+d.                                      \tag{0.1}
\]

The K17 three-level proof does generalize, but its exact scope is a
**normal block system**, not an automatic all-`k` theorem.

1. Any stochastically ordered partition of complete Boolean ranks has one
   joint containment coupling with uniform marginal on every block.
   Separated consecutive blocks are the simplest special case.
2. If every block has size at most `\(W\)`, appending the complete rank-`r`
   owner level and applying Dilworth gives `\(W\)` owner-rooted chains, with
   at most one lower target from each block.
3. Greedy consecutive full-rank packing therefore gives an unconditional
   all-`k` anchored factor of depth at most `\(2d+1\)`.  This improves the
   coefficient in the static factor, but it is not `\(d+O(1)\)`.
4. On the odd K17 continuation, K19 is the first zero-boundary failure.
   In fact K19 has no depth-three **whole-rank normal compression**, even if
   ranks may be interlaced between the two non-top blocks.
5. Splitting the K19 analogue of the bottom bank into four complete-rank
   blocks repairs the static theorem unconditionally:

   \[
      [1,6]\mid[7]\mid[8]\mid[9].                    \tag{0.2}
   \]

   This is one extra static payload cell, the budget corresponding to
   `\(B(19)+1\)`.  It is **not** a word construction.
6. Retaining the separated monotone three-level architecture requires a
   partial split of rank seven. The exact size interval is proved below.
   The subsequent fixed-triple construction
   \(X={[19]\choose7}\setminus\{S:H\subseteq S\}\), \(|H|=3\), proves the
   normalized-Hall property and closes this finite clause.
7. Consecutive unsplit packing cannot yield `\(d+O(1)\)` blocks: its excess
   over `\(d\)` is `\(\Omega(\sqrt k)\)`.  The first odd failure of even the
   `\(d+1\)` budget is K121.  Interlaced blocks can beat consecutive packing
   (an exact K31 example is given below), so this asymptotic no-go does
   **not** refute the full stochastic-block programme.

No statement below supplies source chronology, exact overlaps, endpoint
aperture, address/history guards, residence, upper shadows, a common cap,
or cross-depth regeneration.  In particular, no `\(B(k)+O(1)\)` upper bound
for `\(\nu(k)\)` is claimed.

## 1. The joint uniform-block coupling

For a nonempty set of ranks `\(R_i\subseteq\{0,\ldots,k\}\)`, put

\[
 P_i=\bigcup_{s\in R_i}{[k]\choose s},
 \qquad N_i=|P_i|=\sum_{s\in R_i}{k\choose s},         \tag{1.1}
\]

and define its binomial-weighted rank law by

\[
 \alpha_i(s)=\frac{{k\choose s}}{N_i}\mathbf 1_{s\in R_i}. \tag{1.2}
\]

The rank sets in this section are pairwise disjoint.  Declare elements in
one `\(P_i\)` incomparable and, for `\(i<j\)`, retain ordinary set
containment from `\(P_i\)` to `\(P_j\)`.

### Theorem 1.1 (exact stochastic-rank criterion)

There is a random nested sequence

\[
                         X_0\subsetneq X_1\subsetneq\cdots\subsetneq X_q
                                                               \tag{1.3}
\]

such that `\(X_i\)` is uniform on `\(P_i\)` for every `\(i\)` if and only if

\[
            \alpha_0\preceq_{\rm st}\alpha_1
              \preceq_{\rm st}\cdots\preceq_{\rm st}\alpha_q. \tag{1.4}
\]

Equivalently, for every adjacent pair and every threshold `\(t\)`,

\[
 {\sum_{s\in R_i,\ s\ge t}{k\choose s}\over N_i}
 \le
 {\sum_{s\in R_{i+1},\ s\ge t}{k\choose s}\over N_{i+1}}.  \tag{1.5}
\]

#### Proof

Necessity follows by applying cardinality to (1.3).

For sufficiency, use one uniform `\(U\in[0,1]\)` to quantile-couple random
ranks `\(Q_i\sim\alpha_i\)`.  Stochastic order gives
`\(Q_0\le\cdots\le Q_q\)` almost surely; disjoint rank supports make all
successive inequalities strict.  Independently choose one uniform
permutation `\(\pi\)` of `\([k]\)` and let `\(X_i\)` be its `\(Q_i\)`-prefix.
The prefixes are nested.  For a fixed `\(S\in P_i\)` of rank `\(s\)`,

\[
 \Pr(X_i=S)=\Pr(Q_i=s){1\over{k\choose s}}
            ={1\over N_i}.                              \tag{1.6}
\]

Thus every marginal is uniform.  `\(\square\)`

If `\(max R_i<\min R_{i+1}\)`, condition (1.4) is automatic.  For two such
blocks the pair coupling has the explicit form

\[
 \mu(S,T)=\mathbf 1_{S\subset T}
 { {k\choose |S|}\over
   N_iN_{i+1}{|T|\choose |S|}}
 =\mathbf 1_{S\subset T}
 { {k\choose |T|}\over
   N_iN_{i+1}{k-|S|\choose |T|-|S|}}.                \tag{1.7}
\]

Summing (1.7) over `\(T\)` gives `\(1/N_i\)`; summing over `\(S\)` gives
`\(1/N_{i+1}\)`.  Formula (1.7) specializes exactly to both couplings in the
K17 theorem.

### Theorem 1.2 (LYM, width, and owner attachment)

Assume (1.4), and put `\(M=\max_iN_i\)`.  Every antichain `\(A\)` in the
levelled containment poset satisfies

\[
                  \sum_i {|A\cap P_i|\over N_i}\le1,          \tag{1.8}
\]

and the width is exactly `\(M\)`.

In particular, let `\(P_q={[k]\choose r}\)` be the complete owner level,
so `\(N_q=W\)`, and suppose `\(N_i\le W\)` for every earlier block.  Then
the union of all blocks has a partition into exactly `\(W\)` chains, each
containing one owner.  Removing the owners gives an anchored lower-target
factor of depth at most `\(q\)`.

#### Proof

The random chain of Theorem 1.1 meets an antichain at most once.  Taking
expectations gives (1.8).  Hence

\[
 { |A|\over M}\le\sum_i {|A\cap P_i|\over N_i}\le1.           \tag{1.9}
\]

One largest level is itself an antichain, so the width is `\(M\)`.  Dilworth
partitions the poset into `\(M\)` chains.  In the owner case `\(M=W\)`, and
the `\(W\)` owner elements force exactly one owner into every chain.
`\(\square\)`

This integrates owner attachment into the coupling proof and works in both
parities.

## 2. Partial blocks: the exact regenerative hypothesis

For arbitrary disjoint families `\(P,Q\subseteq2^{[k]}\)`, let
`\(N_Q(F)\)` be the members of `\(Q\)` containing at least one member of
`\(F\subseteq P\)`.

### Theorem 2.1 (normalized Hall is exact)

A containment-supported coupling with uniform marginals on `\(P\)` and
`\(Q\)` exists if and only if

\[
          { |N_Q(F)|\over |Q|}\ge { |F|\over |P|}
                    \qquad(F\subseteq P).                       \tag{2.1}
\]

Consequently, if a residual lower target bank is partitioned into
`\(q\)` families of size at most `\(W\)`, (2.1) holds at every adjacent pair,
and it also holds from the last family to the complete owner level, then it
has an anchored `\(q\)`-chain factor.

#### Proof

Scale the desired coupling so every member of `\(P\)` supplies one unit and
every member of `\(Q\)` demands `\(|P|/|Q|\)` units.  The max-flow cuts are
exactly (2.1).  Adjacent couplings glue through their common uniform
marginals; Theorem 1.2 then applies.  `\(\square\)`

For complete separated rank blocks, (2.1) is proved by (1.7).  For a
partial rank, a Ferrers-punctured block, or a selected regenerative shore,
cardinality alone does not imply (2.1).  The existence of all-`k` blocks
with `\(q\le d+C\)` satisfying these cuts for one absolute `\(C\)` is
**UNPROVED**.

## 3. An unconditional all-`k` `\(2d+1\)` factor

Partition the complete strict-lower ranks consecutively, greedily putting
the longest possible next interval of ranks into a block of mass at most
`\(W\)`.  Let `\(g(k)\)` be the number of blocks.

### Theorem 3.1 (greedy optimality and the factor-two bound)

The greedy partition minimizes the number of consecutive whole-rank blocks,
and

\[
                         g(k)\le2d(k)+1.                       \tag{3.1}
\]

Hence every strict lower ideal has an unconditional anchored chain factor
of depth at most `\(2d+1\)`.

#### Proof

If the greedy first block ends at rank `\(u\)`, no feasible first block can
end later.  Deleting the longest feasible prefix can only decrease the
minimum number of blocks needed for the suffix.  Induction proves greedy
optimality.

Let `\(D=\lceil\Lambda/W\rceil\)`.  Whenever greedy closes a block, its load
plus the first item of the next block exceeds `\(W\)`.  Pairing consecutive
greedy blocks therefore shows `\(g\le2D-1\)`, the standard next-fit bound.
The exact deadline arithmetic gives `\(d\le D\le d+1\)`, and hence
`\(g\le2d+1\)`.  Append the owner level and apply Theorems 1.1--1.2.
`\(\square\)`

This is a static chain theorem only.  Its potential source budget is
`\(W+O(d)\)`, not `\(B+O(1)\)`.

## 4. K19: the first odd obstruction after K17

For K19,

\[
 r=10,\qquad W={19\choose9}=92\,378,
 \qquad\Lambda=262\,143,qquad d=3,qquad h=(\Lambda-dW)_+=0. \tag{4.1}
\]

The relevant rank masses are

\[
 \sum_{s=1}^{6}{19\choose s}=43\,795,\quad
 {19\choose7}=50\,388,\quad
 {19\choose8}=75\,582,\quad
 {19\choose9}=92\,378.                                \tag{4.2}
\]

### Proposition 4.1 (consecutive packing fails exactly)

There is no three-block consecutive full-rank compression of the K19
strict lower ideal with every block of size at most `\(W\)`.

#### Proof

Rank nine already has size `\(W\)` and is its own top block.  The other two
blocks would split ranks one through eight at a cut `\(j\)`.  If `\(j\le6\)`,
the later block contains ranks seven and eight, of total mass

\[
                         50\,388+75\,582=125\,970>W.            \tag{4.3}
\]

If `\(j\ge7\)`, the earlier block contains ranks one through seven, of mass

\[
                         43\,795+50\,388=94\,183>W.             \tag{4.4}
\]

Thus every cut fails.  The minimum capacity casualty over all cuts is
`\(94\,183-W=1\,805\)`.  `\(\square\)`

### Theorem 4.2 (even allowing interlacing cannot preserve normality)

There is no partition of the complete ranks one through eight into two
blocks `\(A,B\)`, each of size at most `\(W\)`, whose rank laws satisfy
`\(\alpha_A\preceq_{\rm st}\alpha_B\)`.  Therefore no depth-three
**whole-rank uniform-block coupling proof** exists at K19.

#### Proof

The two block masses sum to `\(169\,765\)`, so each is at least

\[
                         169\,765-W=77\,387.                    \tag{4.5}
\]

Ranks eight and seven must be in different blocks because of (4.3).  The
block without rank eight must also contain rank six: otherwise even rank
seven together with every rank one through five has mass only `\(67\,051\)`,
contradicting (4.5).

Write `\(A\)` for the block containing ranks six and seven and `\(B\)` for
the block containing rank eight.  `\(B\)` cannot precede `\(A\)`, since a
rank-eight source would have no superset in `\(A\)`.  Thus normality would
require `\(A\preceq_{\rm st}B\)`.

The block `\(B\)` contains at least one rank from one through five by
(4.5); let `\(t\)` be the least such rank.  The lower-tail form of stochastic
dominance requires

\[
 { {19\choose t}\over |B|}
 \le {\sum_{s<t}{19\choose s}\over |A|}.                       \tag{4.6}
\]

But `\(|B|/|A|\le92\,378/77\,387<1.194\)`, while the five possible ratios on
the left after rearrangement are

\[
 \infty,\quad 9,\quad {969\over190},\quad {3876\over1159},
 \quad {11628\over5035}>2.30.                                 \tag{4.7}
\]

Every possibility violates (4.6).  `\(\square\)`

The theorem is deliberately scoped.  It rules out the generalized
**whole-rank normal-compression proof**, not an arbitrary depth-three chain
partition of the uncompressed Boolean ideal.

Across both parities, the earlier zero-boundary whole-rank normal obstruction
is K14 (`\(d=2\)`).  Indeed, `\(W=3432\)` and ranks four and five have total
mass `\(3003\)`.  Rank six, also of mass `\(3003\)`, must be in the later
block, while capacity forces ranks four and five into the earlier block.  If
rank three is later, the threshold-four tail masses are equal but the earlier
total is smaller, violating stochastic order.  If rank three is earlier,
the threshold-three inequality requires its block to have size at least
`\(3423\)`, while capacity permits only rank one in addition and gives at
most `\(3381\)`.  Thus K14 fails as claimed.  K19 is the first odd failure
and the first on the post-K17 route.  The active raw-capacity exceptions K6
and K9 occur earlier, but their canonical Ferrers-punctured residual matching
problems pass.  These parity and active-boundary qualifications are
load-bearing.

## 5. Two exact K19 repairs

### Corollary 5.1 (unconditional one-extra-level repair)

The four separated blocks

\[
 \bigcup_{s=1}^{6}{[19]\choose s},\quad
 {[19]\choose7},\quad {[19]\choose8},\quad {[19]\choose9}       \tag{5.1}
\]

have sizes

\[
                   43\,795,\quad50\,388,\quad75\,582,\quad92\,378. \tag{5.2}
\]

Appending the rank-ten owner level and applying Theorem 1.2 partitions the
strict lower ideal into `\(W\)` owner-rooted chains of depth at most four.

This is the unconditional **static regenerative split**: split the
overcrowded K19 analogue of the K17 bottom bank into ranks `\([1,6]\)` and
rank seven.  It consumes one extra payload level and has zero target
casualties.

### Proposition 5.2 (canonical separated same-depth partial split)

A rank-separated three-block repair whose only shared boundary rank is
rank seven must have

\[
 \begin{aligned}
 P_0&=\bigcup_{s=1}^{6}{[19]\choose s}\ \cup X,\\
 P_1&=\left({[19]\choose7}\setminus X\right)
          \cup {[19]\choose8},\\
 P_2&={[19]\choose9},
 \end{aligned}                                                  \tag{5.3}
\]

where

\[
                         33\,592\le |X|\le48\,583.              \tag{5.4}
\]

#### Proof

The inequalities `\(|P_0|\le W\)` and `\(|P_1|\le W\)` are respectively

\[
        |X|\le92\,378-43\,795=48\,583,
\]

and

\[
        |X|\ge50\,388+75\,582-92\,378=33\,592.                 \tag{5.5}
\]

`\(\square\)`

**Subsequent closure of the K19 split clause.** Fix a triple
\(H\subset[19]\) and take

\[
 X={[19]\choose7}\setminus
   \{S\in{[19]\choose7}:H\subseteq S\}.
\]

Then \(|X|=48\,568\), and exact fixed-core orbit transports prove every
normalized-Hall inequality for \(P_0\to P_1\to P_2\). See
`MATH_THEOREM_K19_K21_FIXED_CORE_NORMAL_SPLITS_AND_ALLK_ORBIT_TRANSPORT_GATE_20260802.md`.
This closes the finite static clause only; a fractional division of a rank
would not by itself prove normalized Hall, and no Catalan-pivot connector
is used here.

## 6. Why consecutive compression cannot give `\(B+O(1)\)`

### Theorem 6.1 (unbounded consecutive-block excess)

Along odd dimensions,

\[
                         g(k)-d(k)=\Omega(\sqrt k).              \tag{6.1}
\]

Consequently no fixed number of extra consecutive unsplit rank blocks can
give a `\(d+O(1)\)` static factor.

#### Proof

Write `\(k=2m+1\)` and

\[
 a_j={2m+1\choose m-j},\qquad W={2m+1\choose m}.                 \tag{6.2}
\]

For `\(j=x\sqrt m+O(1)\)`, the product formula gives, uniformly for `\(x\)`
in a fixed compact interval,

\[
 {a_j\over W}
 =\prod_{\ell=0}^{j-1}{m-\ell\over m+2+\ell}
 =\exp(-x^2+o(1)).                                               \tag{6.3}
\]

Choose fixed constants

\[
          \sqrt{\log(4/3)}<a<b<\sqrt{\log2}.                    \tag{6.4}
\]

For all sufficiently large `\(m\)`, every rank whose distance `\(j\)` lies
in `\([a\sqrt m,b\sqrt m]\)` has mass strictly between `\(W/2\)` and
`\(3W/4\)`.  There are `\(\Theta(\sqrt m)\)` consecutive such ranks.  No
capacity-`\(W\)` block contains two of them.  Except for at most the two
boundary blocks of this band, their blocks are singletons and each wastes
at least `\(W/4\)` capacity.

Thus the total unused capacity of any consecutive block packing is
`\(\Omega(W\sqrt m)\)`.  Since `\(gW=\Lambda+\)` unused capacity and
`\(d=\Lambda/W+O(1)\)`, (6.1) follows.  `\(\square\)`

The canonical Ferrers bank has only `\(O(d^2)=O(k)\)` targets and lies in
low ranks.  It cannot change the exponential-scale central-band waste in
this proof.

An exact greedy/DP audit gives the first odd failure of the one-extra-level
consecutive budget as

\[
                         k=121,qquad d=7,qquad g=9.             \tag{6.5}
\]

The audit checks every odd `\(k<121\)` as well as K121 with integer
arithmetic.

### Proposition 6.2 (interlacing can repair a consecutive failure)

At K31, `\(d=4\)` and consecutive packing needs five blocks, but the four
rank blocks

\[
 \{1,\ldots,10,12\},\quad\{11,13\},\quad\{14\},\quad\{15\}     \tag{6.6}
\]

have masses

\[
 217\,093\,713,\quad290\,925\,390,\quad265\,182\,525,
 \quad300\,540\,195=W,                                         \tag{6.7}
\]

and satisfy (1.5).  The only nonautomatic threshold compares

\[
 {141\,120\,525\over217\,093\,713}
 <{206\,253\,075\over290\,925\,390}.                           \tag{6.8}
\]

Hence Theorem 1.2 gives a depth-four static factor at K31.

This example is why Theorem 6.1 is not promoted to a no-go for arbitrary
stochastically ordered whole-rank blocks.  The all-`\(k\)` existence of
`\(d+C\)` such interlaced blocks is **UNPROVED**.

## 7. Exact remaining implications

The new unconditional implication is

\[
 \boxed{
 \begin{array}{c}
 \text{stochastically ordered complete-rank blocks}\\
 \text{or arbitrary blocks satisfying normalized Hall}
 \end{array}}
 \Longrightarrow
 \boxed{\text{an exact static anchored chain factor}.}          \tag{7.1}
\]

The weakest static all-`\(k\)` hypothesis capable of yielding a bounded
additive chain depth is now explicit:

> **UNPROVED `RBS_C`.**  After the canonical Ferrers sidecar is fixed, the
> residual strict-lower bank can be partitioned into at most `\(d+C\)`
> families of size at most `\(W\)`, with normalized Hall at every adjacent
> containment graph and at the final owner graph, for one absolute `\(C\)`.

`RBS_C` would prove a static anchored `\(d+C\)` factor.  It would still not
prove `\(\nu(k)\le B(k)+C\)`.  The first physical connector remains one
common overlap serialization of those frozen owner chains whose state arcs
are balanced and connected, together with:

* endpoint aperture;
* global overlap/address/history guards;
* depth residence and every required upper witness;
* the common cap and lower compiler; and
* a genuine output-to-next-input regenerative relay on the same frozen
  slices.

All these physical clauses are **UNPROVED** here.  In particular, the K17
constructive chain table validates the input to this theorem but does not
validate any of those clauses.

## 8. Independent audit boundary

The companion audit

```text
MATH_AUDIT_ALLK_UNIFORM_BLOCK_CHAINIZATION_AND_K19_NORMALITY_OBSTRUCTION_20260802.md
scratch/audit_allk_uniform_block_chainization_20260802.py
```

checks with exact integers:

* greedy packing against an independent dynamic programme through K121;
* the K17 and K19 block masses and stochastic inequalities;
* all 48 capacity-feasible ordered whole-rank K19 two-block assignments,
  none of which is stochastically ordered;
* the exact K19 minimum cut casualty `\(1\,805\)` and split interval
  (5.4);
* the first odd `\(d+1\)` consecutive failure K121; and
* the interlaced K31 repair.

The computation audits finite arithmetic only.  The coupling, Hall, LYM,
Dilworth, K19 analytic obstruction, and asymptotic statements are proved
above and do not depend on the program.
