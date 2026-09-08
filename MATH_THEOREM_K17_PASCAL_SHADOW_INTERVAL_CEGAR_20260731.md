# Exact interval CEGAR for the (K16\to K17) Pascal-shadow transversal

## 1. Finite instance and scope

Let

* `T` be the authenticated `c7be` (K16) rank-eight carrier of length
  (12870);
* (c_p=T_p\cup T_{p+1}), (0\le p<12869), be its rank-nine edge
  colours; and
* (P(c)=\{p:c_p=c\}).

Every one of the (11440=\binom{16}{9}) colours occurs.  The exact
multiplicity census is


\[
  1^{10111}\,2^{1229}\,3^{100}.
\]

An **occurrence transversal** chooses one (p(c)\in P(c)) for each colour.
Reading the retained colours in increasing order of (p(c)) gives a
permutation (U) of the rank-nine layer.  This note solves the exact
encoding problem


\[
  \text{choose }p(c)\text{ so every }S\subseteq[16],\ |S|\ge10,
  \text{ is a contiguous OR in }U. \tag{1}
\]

It does **not** assert that (1) is satisfiable.  Nor does it address the K17
schedule, singleton, lower-Hall, or common-cap compiler gates.

## 2. Raw-interval equivalence

For a fixed target (S\), call (c) *good* when (c\subseteq S), and a
*blocker* otherwise.

### Theorem 2.1 (exact raw-interval criterion)

For an occurrence transversal (p), the following are equivalent.

1. (S) is the OR of a contiguous subword of (U).
2. There is a raw-position interval ([a,b]\subseteq[0,12868]) such that
   * no retained blocker lies in ([a,b]); and
   * for every (x\in S), some retained good occurrence in ([a,b])
     contains (x).

#### Proof

If (U_i\vee\cdots\vee U_j=S), take (a=p(U_i)) and (b=p(U_j)).
Every retained occurrence between them is one of (U_i,\ldots,U_j), hence
is good, and their OR contains every bit of (S).

Conversely, the retained occurrences in ([a,b]) form a contiguous subword
of (U).  They are all subsets of (S), while the second condition says
their OR contains (S).  Their OR is therefore exactly (S).  (square)

This removes the apparent quadratic family of possible intervals: existence
of one interval can be encoded by two monotone boundary words.

## 3. Exact SAT block for one target

The global choice encoding is seed-at-zero.  For a colour with occurrences
(0,\ldots,m-1), choose one seed option (s), introduce one Boolean
(x_{c,o}) for each (o\ne s), and impose pairwise at-most-one.  Option
(o\ne s) is selected iff (x_{c,o}=1); the seed is selected iff every
(x_{c,o}=0).  Thus exactly one occurrence is selected without an ALO
clause.  The fixed instance has only


\[
1229+2\cdot100=1429
\]

global choice variables.

For a target (S), introduce (L_p,R_p) for every raw position and impose


\[
L_p\Rightarrow L_{p+1},\qquad R_{p+1}\Rightarrow R_p. \tag{2}
\]

Hence (L\wedge R) is one interval (possibly empty).  For every blocker
occurrence at (p), impose


\[
\operatorname{selected}(p)\Rightarrow \neg(L_p\wedge R_p). \tag{3}
\]

For every good occurrence introduce (z_p), impose


\[
z_p\Rightarrow L_p,\quad z_p\Rightarrow R_p,\quad
z_p\Rightarrow\operatorname{selected}(p), \tag{4}
\]

and for each bit (x\in S), impose


\[
\bigvee_{p:\ c_p\subseteq S,\ x\in c_p}z_p. \tag{5}
\]

The seed option in (3) expands to one clause containing its positive
alternative variables; in (4) it expands to one binary clause per negative
alternative.  Thus all constraints are ordinary CNF.

### Theorem 3.1 (equisatisfiability)

For fixed global occurrence choices, the target block (2)--(5) is
satisfiable iff (S) is a contiguous OR of (U).

#### Proof

Any satisfying (L,R,z) gives the interval in Theorem 2.1.  Equations (3)
and (5) give its two conditions.  Conversely, given a witness ([a,b]), set
(L_p=[p\ge a]), (R_p=[p\le b]), and select enough retained good
occurrences as (z)-witnesses to cover every bit.  All clauses hold.
(square)

Therefore conjoining one block per target is an exact formulation of (1).

## 4. Fixed-blocker compression and sound CEGAR

The (10111) multiplicity-one colours are permanently selected.  For a
target (S), their blocker occurrences split the raw line into gaps, and
every witness interval lies wholly inside one gap.  Moreover an interval may
be shrunk to the positions of its first and last selected good occurrences.
Therefore it is enough to enumerate pairs of good raw endpoints inside these
fixed-blocker gaps.

For the 73 retained-seed holes, the maximum gap length is 13 and the total
number of reduced candidate intervals is only **85**.  Introduce one guard
(y_I) per candidate.  Its clauses say:

* every repeated blocker occurrence in (I) is unselected; and
* for every target bit not supplied by a fixed good colour, some selected
  repeated good occurrence in (I) supplies it.

Together with an ALO over the candidate guards, this is exactly the DNF form
of Theorem 2.1.  Using explicit one-hot occurrence variables, the complete
73-target instance has only


\[
2843\text{ variables},\qquad3301\text{ clauses}. \tag{6}
\]

The independent implementation is

`scratch/search_k17_pascal_shadow_gap_cegar_20260731.cpp`.

For comparison, enumerating every nontrivial old upper target, deduplicating
exact guard signatures, gives 13763 unconditional targets, 1130 active
targets, 9365 guards, maximum gap 13, and an exact full formula with 12123
variables and 50272 clauses.  This census is implemented independently in

`scratch/build_k17_pascal_arbitrary_interval_cnf_20260731.cpp`.

The boundary-word encoding of Section 3 remains useful when there are few or
no multiplicity-one blockers; the gap encoding is the sharp formulation for
this carrier.

### Sound CEGAR principle

Start from any occurrence transversal, compute its actual missing targets,
and activate their exact blocks.  Solve, independently reconstruct (U),
and add every newly missing target.  Then:

* every SAT model covers all targets activated so far;
* every round with remaining holes strictly enlarges the active set;
* SAT with no holes is a literal certificate for (1); and
* UNSAT at any round proves that (1) is impossible for this fixed K16
  carrier, because an upper-complete transversal would satisfy every active
  block.

The generic boundary-word implementation is

`scratch/search_k17_pascal_shadow_cegar_20260731.cpp`.

It independently replays every SAT model before accepting it.  The retained
73-hole heuristic seed is encoded as the all-false occurrence phase, which is
only a search hint and is not a restriction.

## 5. Exact finite audit

The independent audit

`scratch/audit_k17_pascal_shadow_interval_cegar_20260731.py`

authenticates all inputs and reports:

* 12869 raw occurrences and 11440 colours;
* 1329 movable colours and 1429 non-seed Boolean variables;
* retained-seed defect 73, with histogram
  (10^{63},11^9,12^1);
* no false raw-interval witness for any of those 73 holes;
* a positive raw-interval replay at every rank (10,\ldots,16); and
* all 73 current holes are individually feasible when occurrence choices are
  free; and
* the two-target opposite-choice core in Section 6 is reproduced without a
  solver.

The last fact is exact.  For a fixed left endpoint (a), a blocker colour
(c) can be kept out of ([a,b]) iff


\[
\min P(c)<a\quad\text{or}\quad b<\max P(c).
\]

Thus the maximal legal right endpoint is


\[
b_{\max}(a)=\min_{c\not\subseteq S,\ \min P(c)\ge a}\max P(c)-1,
\]

and a witness exists iff, for some (a), every bit of (S) has a good raw
occurrence between (a) and (b_{\max}(a)).  A descending linear scan checks
this criterion.

For all 73 seed holes together, the uncompressed boundary-word CNF has


\[
1{,}882{,}082\text{ variables},\qquad
2{,}821{,}653\text{ clauses}. \tag{7}
\]

As a light syntax/decoder validation, one active target produced a SAT model
with 27,179 variables and 38,731 clauses; three active targets produced a SAT
model with 78,680 variables and 115,996 clauses.  Independent semantic replay
confirmed every active target in both models.  Those models had 396 other
holes, so these are encoding checks, not progress claims for (1).

Those light tests preceded the fixed-blocker compression and are retained as
an independent check of the generic encoding.

Audit payload SHA-256:

`428348ad40d925d5e192a37f6e821459f5b824c5471137cd3a05d2bd0c6bdc49`.

## 6. Solver-free opposite-choice core

Let


\[
c=0x0bf5,\qquad P(c)=\{9176,10616\}.
\]

For (S_1=0x1bf5), fixed blockers leave exactly one reduced candidate,
([9175,9176]).  Its fixed good colours have union `0x1bb5`; bit 6 is
missing, and its only provider in the interval is colour (c) at 9176.
Thus (S_1) forces (p(c)=9176).

For (S_2=0x0ff5), fixed blockers leave exactly one undominated reduced
candidate, ([10615,10616]).  Its fixed good colours have union `0x0fe5`;
bit 4 is missing, and its only provider is (c) at 10616.  Thus (S_2)
forces (p(c)=10616).

The two requirements contradict the exact-one occurrence choice for (c).
Hence:

### Theorem 6.1 (fixed-carrier no-go)

No selection of one existing occurrence of every rank-nine edge colour from
the authenticated `c7be` K16 chronology is upper-complete.

The compact CNF cross-check on just these two targets has 2760 variables,
2862 clauses, two candidate guards, and is UNSAT.  The proof above is
solver-free; the CNF is only an independently generated replay.

The full primary proof and its separate literal audit are recorded in

`MATH_THEOREM_K17_PASCAL_OCCURRENCE_INTERVAL_AND_OPPOSITE_CHOICE_NOGO_20260731.md`

and

`scratch/audit_k17_pascal_occurrence_selection_nogo_20260731.py`.

## 7. Exact status

The former heuristic question is completely decided **negatively for this
fixed carrier**.  Every current hole is individually feasible, but two are
simultaneously incompatible.  This is the smallest possible kind of global
coupling obstruction and explains why coordinate descent could reduce the
defect without reaching zero.

The scope is narrow and important: this is not a K17 no-go.  It rules out only
the rule “retain exactly one existing q1 occurrence of every colour from this
fixed K16 chronology.”  A successful induction must rethread/change the
source chronology, permit a richer two-shore selection, or use a different
carrier.  The exact interval/guard formulation remains reusable as a cheap
forced-literal screen for every proposed replacement carrier.
