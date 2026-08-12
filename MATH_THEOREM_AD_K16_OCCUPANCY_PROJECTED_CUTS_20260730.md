# K16 projected occupancy cuts and canonical blocker strengthening

Date: 2026-07-30  
Lane: AD  
Status: proved, solver-free; no SAT or UNSAT verdict

## 1. Frozen scope

This note concerns only the 1,412-variable interval-occupancy/blocker CNFs
for the fixed-gap profiles

\[
(4,9,4),\qquad(5,8,4),\qquad(5,9,3).
\]

The input statements are:

* `MATH_THEOREM_AD_K16_INTERVAL_OCCUPANCY_BLOCKER_COMPRESSION_20260730.md`,
  SHA-256
  `7ffa70336bec21ea2ecd9c6af5625e5dedb30ab6fd152c5d8dd5746e54390509`;
* `THREAD_K_K16_CLOSURE_NORMALIZED_THREE_PROFILE_COMPRESSION_20260730.md`,
  SHA-256
  `e4b2dad9f5e4c10ab65f3ec8ac6ec2fea44b5265c583a8cf20ca8c22fcb0666c`;
* the independent THREAD_K replay
  `scratch/k16_12873_signature_flow_c3_capacity_20260730.audit.json`,
  SHA-256
  `768964f4539792ce7b358d867453062a3c6711d292c344e72760df126ee02eb8`,
  payload SHA-256
  `f887d435b39d062182648d3deae76aee453d5577511c573b0ca61cd8b29cf54f`.

For a repair target \(T\), editable cell \(p\), block \(j\), and coordinate
\(q\), write \(o_{T,p}\), \(g_{T,j}\), and \(B_{p,q}\) for the existing
occupancy, block-control, and blocker variables.  The original forward row is

\[
o_{T,p}\longrightarrow B_{p,q}\qquad(q\notin T).       \tag{1.1}
\]

No claim below changes a gap, separator, or fixed carrier.

## 2. The terminal three-cell cut

Let

\[
\begin{split}
\mathcal S_C=\{&\mathtt{8c62},\mathtt{8c67},\mathtt{8ce6},
\mathtt{8ce7},\mathtt{9ce6},\mathtt{bcef},\\
&\mathtt{cc61},\mathtt{cc63},\mathtt{cc67},\mathtt{cce7},
\mathtt{ce61},\mathtt{ce63}\}.
\end{split}
\]

### Theorem 2.1 (terminal-control cardinality cut)

In profile \((5,9,3)\), every satisfying assignment obeys

\[
                 \sum_{T\in\mathcal S_C}g_{T,3}\le 10. \tag{2.1}
\]

This is encoded without auxiliaries by the twelve clauses

\[
 \bigvee_{T\in\mathcal S_C\setminus\{T_0\}}\neg g_{T,3}
              \qquad(T_0\in\mathcal S_C),              \tag{2.2}
\]

each of length eleven.

#### Proof

The occupancy at-least-one row chooses a cell for every target.  Its
occupancy-to-block implication makes the control of the used block true,
and pairwise at-most-one on the three controls makes the other two false.
Thus \(g_{T,3}=1\) exactly when the chosen interval for \(T\) lies in the
terminal block.  THREAD_K Theorem 7.4 proves that a three-cell terminal
collar realizes at most ten targets in \(\mathcal S_C\).  This is (2.1).
An assignment violates (2.1) exactly when some eleven-element subset is
all true, which is excluded by (2.2).  \(\square\)

For the current `5/9/3` map, the twelve terminal-control variable IDs are

\[
1029,1032,1035,1038,1050,1071,1083,1086,1089,1092,1095,1098.
\]

There is no corresponding theorem for either width-four terminal collar;
(2.1) must not be added to profiles \((4,9,4)\) or \((5,8,4)\).

## 3. Exact cell-conflict hypergraph

Set

\[
E=\mathtt{8000},\qquad N=\mathtt{9009},\qquad
Q=\{15,12,3,0\}.
\]

All 57 repair targets omit bit 8.  Exactly \(E,N\) omit bit 5.  Exactly
18 targets omit bit 15.  Consequently a family of targets active at one
cell has empty intersection only in one of two ways:

1. it contains \(E\) and a bit-15-free target; or
2. it does not contain \(E\), contains \(N\), and the omissions of its
   other members cover the four bits of \(Q\).

For the second case encode \(Q\setminus T\) as a four-bit word in the
order \((15,12,3,0)\).  After removing \(E,N\), the omission-pattern
multiplicities are

\[
\begin{array}{c|rrrrrrrrr}
d&0000&0010&0011&0100&0110&0111&1000&1100&1110\\ \hline
\#&13&2&1&7&12&2&8&7&3.
\end{array}                                             \tag{3.1}
\]

The inclusion-minimal two-pattern covers of `1111` and their target-level
counts are

\[
\begin{array}{c|r}
0011+1100&7\\
0011+1110&3\\
0111+1000&16\\
0111+1100&14\\
0111+1110&6
\end{array}
\qquad\text{(total 46)},                               \tag{3.2}
\]

and the inclusion-minimal three-pattern covers are

\[
0011+0100+1000\quad(56),\qquad
0011+0110+1000\quad(96),                              \tag{3.3}
\]

for a total of 152.  Patterns `0000` and `0010` occur but belong to no
minimal cover.

### Theorem 3.1 (complete minimal conflict clauses)

At each editable cell \(p\), nonempty active-target intersection is
equivalent to the following 216 clauses:

* the 18 binary clauses
  \[
       \neg o_{E,p}\vee\neg o_{T,p}\qquad(15\notin T); \tag{3.4}
  \]
* the 46 ternary clauses
  \[
       \neg o_{N,p}\vee\neg o_{T,p}\vee\neg o_{U,p}  \tag{3.5}
  \]
  for the target pairs whose omission patterns occur in (3.2); and
* the 152 four-literal clauses
  \[
 \neg o_{N,p}\vee\neg o_{T,p}\vee\neg o_{U,p}
                    \vee\neg o_{V,p}                  \tag{3.6}
  \]
  for the target triples whose omission patterns occur in (3.3).

Across 17 cells this is exactly

\[
              17(18+46+152)=3672                         \tag{3.7}
\]

short clauses.  Every one is a logical consequence of the original CNF.

#### Proof

If \(E\) is active, the intersection is contained in its sole bit 15.
It is empty exactly when some active target omits bit 15, giving (3.4).

Suppose \(E\) is inactive.  If \(N\) is also inactive, every active
target contains bit 5, so the intersection is nonempty.  If \(N\) is
active, the intersection is contained in \(N\), and it is empty exactly
when the companion omissions cover \(Q\).  The nine omission patterns and
multiplicities in (3.1) follow directly from the 57-target list.  Removing
dominated patterns and checking the four coordinates gives exactly the
five minimal pairs in (3.2) and two minimal triples in (3.3).  Their
products give \(46\) and \(152\).  Any larger cover contains one of these
minimal covers, so (3.5)--(3.6) are sufficient; necessity is immediate.

The original blocker/common-coordinate clauses are an extended encoding
of the same nonempty-intersection condition.  Hence every displayed
conflict is an implicate of the original CNF.  Each is prime in the
occupancy projection: deleting any active target from a listed minimal
family leaves a nonzero common coordinate.  \(\square\)

Thus the 3,672 clauses may either be appended as redundant projected cuts
or replace the 17 generic common-coordinate clauses in an exact derivative
encoding.  The latter statement concerns the occupancy projection; blocker
normalization is addressed next.

## 4. Canonical blocker definitions

For every cell and coordinate define

\[
 D_q=\{T\in R:q\notin T\}.
\]

Add the reverse row

\[
 B_{p,q}\longrightarrow\bigvee_{T\in D_q}o_{T,p},      \tag{4.1}
\]

or the unit \(\neg B_{p,q}\) if \(D_q=\varnothing\).  Together with
(1.1), this makes

\[
 B_{p,q}=\bigvee_{T:q\notin T}o_{T,p}.                 \tag{4.2}
\]

### Theorem 4.1 (projection-preserving canonicalization)

The 272 rows (4.1) preserve exactly the feasible projection onto all
occupancy and block-control variables.  They are not, however, logical
consequences for the existing auxiliary \(B\)-assignments.

#### Proof

Given any satisfying assignment of the original CNF, replace every blocker
by the right side of (4.2).  Forward implication (1.1) shows that this can
only change a blocker from true to false.  Every positive occurrence of a
blocker is in (1.1), which remains satisfied by (4.2).  All other blocker
occurrences are negative, in common-coordinate or durable-point clauses,
so lowering blockers cannot falsify them.  The resulting assignment obeys
(4.1) and has unchanged occupancy and controls.

Conversely every assignment satisfying the strengthened formula satisfies
the original formula because only clauses were added.  Therefore the
occupancy/control projections agree.  An original assignment may set an
unsupported blocker true, so (4.1) is not a formula-level implicate.
\(\square\)

The omission counts for bits \(0,\ldots,15\) are

\[
(4,45,24,21,41,2,17,44,57,38,12,29,32,40,24,18),       \tag{4.3}
\]

whose sum is 448.  Hence the 272 reverse clauses contain exactly

\[
17(448+16)=7888                                         \tag{4.4}
\]

literals.  The bit-5 subfamily alone consists of 17 ternary clauses

\[
             \neg B_{p,5}\vee o_{E,p}\vee o_{N,p},     \tag{4.5}
\]

and is the cheapest useful anchor-localization normalization.

For comparison, two short genuine implicates of the original CNF are

\[
\neg o_{E,p}\vee\neg B_{p,15},                         \tag{4.6}
\]

and

\[
\neg o_{N,p}\vee\neg B_{p,0}\vee\neg B_{p,3}
                 \vee\neg B_{p,12}\vee\neg B_{p,15}.  \tag{4.7}
\]

There are 17 of each.  They follow by resolving the original 16-coordinate
common clause with the forward blocker implications forced by \(E\) or
\(N\).  They are already subsumed semantically by the complete projected
conflict family but can shorten propagation paths in a blocker-led solver.

## 5. Optional exact block-control links

The current controls also admit the genuine redundant definition

\[
 g_{T,j}\longrightarrow\bigvee_{p\in P_j}o_{T,p}.      \tag{5.1}
\]

Indeed, if \(g_{T,j}\) is true and no cell of block \(j\) is occupied,
the target occupancy ALO chooses another block \(j'\); its forward link
forces \(g_{T,j'}\), contradicting control AMO.  Thus (5.1) is a logical
consequence, not merely a normalization.  There are \(57\cdot3=171\)
such rows.  They are optional; (2.1) is sound without them.

When a singleton anchor is used, the binary rows (3.4) immediately force
all 18 bit-15-free intervals away from its cell.  One may also add the
implied anchor-split clause

\[
 \neg o_{E,a}\vee\neg o_{T,\ell}\vee\neg o_{T,r}
 \quad(15\notin T,\ \ell<a<r\text{ in one block}),      \tag{5.2}
\]

because one-run contiguity would otherwise force \(o_{T,a}\).  Across all
possible anchor positions, (5.2) has respectively

\[
18\sum_j\binom{w_j}{3}=1656,1260,1710                  \tag{5.3}
\]

instances for the three profiles.  These are optional second-order
propagation cuts, not part of the minimal pack below.

## 6. Implementation-ready additive pack

Without introducing a variable, append:

1. 3,672 clauses (3.4)--(3.6);
2. 272 reverse blocker rows (4.1); and
3. only for profile \((5,9,3)\), twelve terminal rows (2.2).

The exact additive counts are therefore

\[
\begin{array}{c|c|c}
\text{profile}&\text{added clauses}&\text{new unanchored total}\\ \hline
(4,9,4)&3944&43004\\
(5,8,4)&3944&40926\\
(5,9,3)&3956&43476.
\end{array}                                             \tag{6.1}
\]

For an anchor-any instance, add its existing 136 singleton clauses to the
last column, giving 43,140, 41,062, and 43,612.  Appending the optional 171
block reverse links gives totals 43,175, 41,097, and 43,647 before anchor
clauses.

The new deterministic postprocessor

`scratch/strengthen_ad_k16_occupancy_blocker_cnf_20260730.py`

implements exactly this additive pack, validates the source
CNF/map hash link and all censuses, preserves the 1,412-variable header,
and emits a provenance audit.  It performs no solving.

The projected short clauses should expose an empty cell intersection as
soon as its few occupancy literals become true, rather than after blocker
propagation.  The terminal rows cut target placement before endpoint and
durability reasoning.  Reverse blocker rows eliminate unsupported blocker
truths and may help durable clauses, but many are long; (4.5) is the
smallest low-risk subset if clause traffic is a concern.  These are
propagation expectations, not a claim of runtime improvement.

## 7. Exact boundary

The 3,672 projected rows and twelve terminal rows are genuine logical
consequences of the original fixed-gap CNFs.  The 272 reverse blocker rows
are only projection-preserving canonicalization and must be described as
such.  None of these statements proves SAT or UNSAT, changes the three
fixed profiles, covers a different deletion/gap pattern, or establishes a
length-12,873 word.
