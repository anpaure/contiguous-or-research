# K17 support-three row commutators versus literal ternary HexLift

**Date:** 2026-08-01  
**Lane:** K, functional Hall and topology coupling  
**Status:** exact comparison of the six authenticated serial row circuits
with the Boolean-hex fusion theorem; an exact strict/general HexLift
criterion; and an exact Hall/topology conjunction.  No new computation is
used.  No K17 topology certificate is claimed.

## 0. Verdict

None of the six authenticated K17 support-three certificates is a literal
ternary component triple in its frozen scope.

There are two independent reasons.

1.  Each certificate is a **row-table substitution** in the overlapping
    support-two shell \(C_{\rm ov}(F)\).  Its audits rebuild the legal
    transition graph and its maximum matchings, but select no exact directed
    factor, no three old factor edges, and no component decomposition.  The
    frozen component profile is explicitly null.  Therefore the hypothesis
    “the three old edges lie on three distinct directed cycles” is not even
    an object in those certificates.
2.  The strict lossless depth-three Boolean HexLift is a chordless type-8
    cubic: exactly three type-\((6,1,1)\) head rows change, each row delta is
    the difference of two rank-six suffix resources, and no legal
    support-two intermediate exists.  Every one of the six K17 circuits
    migrates at least two age types, has at least one row delta of support
    greater than two, and belongs by construction to \(C_{\rm ov}(F)\).
    Thus all six fail the strict HexLift criterion.

This does not prove that no completion or non-common-state flag lift can
place a Boolean hex near one of the six tables.  That generalized question
was not audited: it needs occurrence-labelled old/new turn atoms and a
selected factor.

There is an exact positive criterion.  A row circuit can be both a ternary
topology fusion candidate and a one-unit functional-Hall descent precisely
when it has a generalized HexLift witness whose old atoms occupy three
distinct cycle components **and** its neighbour-set change satisfies every
functional Hall cut inequality.  Separate topology and Hall certificates
do not imply that one matching realizes both; a common residual/forced-edge
extension row is additionally necessary for a literal combined factor.

The opposite-seam theorem remains decisive on the fixed
zero-extra-quarantine face.  The two reset orientations cannot be completed
there by one independent Cartesian gain ear each, because their typed
old-pair tail supports never agree.  The six K17 row commutators are closed
resource-zero substitutions and do not evade that tail-set obstruction or
the odd attachment-parity gate.  The active fixed-host reset use therefore
requires a larger coupled HexLift with an open gain/loss state.  Separately
private one-ear modules remain only an abstract option until their common
exterior contraction is proved independently.

## 1. Three distinct levels of support three

The following objects must not be identified.

1. A **static row circuit** changes three selected flags and has zero total
   target/type resource delta.
2. A **functional graph circuit** changes the set of legal root--owner or
   tail--head incidences and may improve a maximum matching.
3. A **ternary component triple** is a selected six-atom Boolean hex inside
   one directed four-resource factor, with its three old atoms on three
   distinct directed cycle components.

The K17 serial certificates prove (1) and a matching gain in (2).  The
Boolean-hex fusion theorem starts with (3).  Passing from (1) to (3) requires
a physical occurrence lift and a factor selection; it is not a consequence
of resource-delta equality.

## 2. The strict depth-three HexLift

Let \(S\) have rank \(m-2\), let \(a,b,c,u\notin S\) be distinct, and put

\[
\begin{array}{lll}
 A=S+a+u,&B=S+a+c,&C=S+c+u,\\
 D=S+b+c,&E=S+b+u,&F=S+a+b.
\end{array}                                                \tag{2.1}
\]

The old and new atoms are

\[
 O=\{A\to B,C\to D,E\to F\},\qquad
 N=\{A\to F,C\to B,E\to D\}.                             \tag{2.2}
\]

Choose \(w\in S\).  The strict lossless depth-three flag lift keeps the
three tail flags \((u,w)\) at \(A,C,E\), and changes the head flags at
\((B,D,F)\) from

\[
                         (w,a),(w,c),(w,b)                  \tag{2.3}
\]

to

\[
                         (w,c),(w,b),(w,a).                 \tag{2.4}
\]

At K17, every row in (2.3)--(2.4) has type

\[
                         (|C_0|,|C_1|,|C_2|)=(6,1,1),       \tag{2.5}
\]

which is type ID 8 in the authenticated tables.  The rank-seven suffix is
rootwise fixed.  The three signed row deltas are therefore

\[
 e_{R_a}-e_{R_c},\qquad
 e_{R_c}-e_{R_b},\qquad
 e_{R_b}-e_{R_a},                                          \tag{2.6}
\]

for three rank-six resources \(R_a,R_b,R_c\).  Each delta has support two.
The legal option graph is the chordless \(C_6\), so there is no legal
support-two factorization.

### Proposition 2.1 (strict HexLift fingerprint)

A K17 row circuit is the strict common-state HexLift (2.1)--(2.4) only if:

1. its three rows all have type transition \(8\to8\);
2. every row delta has exactly one positive and one negative rank-six
   resource, with the telescoping pattern (2.6); and
3. the simultaneous triple has no legal resource-zero support-two
   intermediate.

These conditions are necessary before physical root phases and component
placement are considered.

#### Proof

Equations (2.3)--(2.5) give item 1.  Root-minus-\(w\) is fixed at rank seven,
while (2.4) cyclically permutes exactly the three rank-six suffixes, giving
item 2.  The structural-zero \(C_6\) proves item 3.  \(\square\)

## 3. Exact audit comparison with the six serial K17 circuits

The six authenticated moves are the stages in

```text
scratch/threadA_k17_commonfirst_support3_serial_chain_20260801.manifest.tsv
```

Their literal row ledgers give the following complete comparison.  “Delta
supports” lists the numbers of nonzero signed resource coordinates in the
three row deltas.  “Incidence delta” is the number of changed projected
root--owner availability edges recorded in `edge_delta.tsv`; it is not a
selected physical edge count.

| stage | roots | type transitions | delta supports | common rank | old-cut \(\kappa\) | packet rank | incidence delta |
|---|---|---|---|---:|---:|---:|---:|
| `2e919→4f5` | 81,437,1380 | 1→5, 5→5, 5→1 | 3,2,3 | 1141→1142 | 1 | 1172→1173 | 4 |
| `4f5→1852` | 216,558,1348 | 8→8, 8→0, 0→8 | 2,5,5 | 1142→1143 | 2 | 1173→1173 | 8 |
| `1852→0c27` | 93,1251,1306 | 6→0, 0→6, 7→7 | 3,3,2 | 1143→1144 | 1 | 1173→1173 | 4 |
| `0c27→b355` | 353,365,503 | 0→6, 6→0, 0→0 | 3,5,2 | 1144→1145 | 2 | 1173→1173 | 7 |
| `b355→45a0` | 449,563,1055 | 0→6, 3→0, 6→3 | 5,3,6 | 1145→1146 | 2 | 1173→1173 | 8 |
| `45a0→89c9` | 1001,1062,1202 | 8→1, 7→8, 1→7 | 3,4,3 | 1146→1147 | 2 | 1173→1173 | 7 |

Every row triple has zero total static resource delta, and every displayed
common-rank gain and Hall-cut value was independently replayed in the frozen
audits.  But none passes item 1 of Proposition 2.1; five have no unchanged
type-8 row at all, and the remaining stage has only one.  Each also has a
row delta of support greater than two, and every stage was generated inside
\(C_{\rm ov}(F)\), contradicting items 2--3.

### Theorem 3.1 (exact classification of the frozen six)

None of the six authenticated serial K17 moves is a strict lossless
depth-three Boolean HexLift.  None is a certified ternary component triple:
the audits contain no selected exact factor, no designated old/new hex
atoms, and no cycle-component profile.

The proof-safe status of a **generalized**, non-common-state HexLift at any
of the six endpoints is `UNKNOWN`, not `UNSAT`.

#### Proof

The first assertion follows row by row from Proposition 2.1 and the table.
For the second, the independent audit scope explicitly excludes topology
and reports `quotient_component_profile:null`; moreover all common matchings
have rank below 1430.  Hence the data required by the definition of a
ternary component triple were neither selected nor verified.  This is an
absence of a literal certificate, not an exhaustive nonexistence theorem for
other factor completions.  \(\square\)

The common matching gains are nevertheless real.  They show that
type-migrating support-three row circuits can improve functional attachment.
They do not show that the same circuit merges components.

## 4. General HexLift criterion

Let \(F,F'\) be exact static flag tables differing at three rooted rows, and
let \({\cal A}(F),{\cal A}(F')\) be their occurrence-labelled legal turn
atlases.  A **generalized HexLift witness** consists of:

1. six pairwise-distinct physical middle occurrences \(A,B,C,D,E,F\)
   satisfying (2.1) for some \(S,a,b,c,u\);
2. the three old atoms \(O\) from (2.2) belonging to \({\cal A}(F)\), and
   the three new atoms \(N\) belonging to \({\cal A}(F')\);
3. literal equality of the old and new lower, owner, tail and head
   occurrence multisets;
4. equality of every declared static target/type/rail ledger between
   \(F\) and \(F'\); and
5. a selected directed four-resource matching \(M\subseteq{\cal A}(F)\)
   containing \(O\).

The witness is a **ternary component triple** when the three members of
\(O\) lie on three distinct directed cycle components of the physical
projection of \(M\).

### Theorem 4.1 (exact HexLift and fusion criterion)

Conditions 1--5 are necessary and sufficient for the replacement

\[
                         M'=(M-O)\cup N                       \tag{4.1}
\]

to be a literal resource-exact Boolean-hex factor toggle compatible with
the two flag tables.  If the witness is a ternary component triple, it
decreases the directed cycle count by exactly two.

#### Proof

Conditions 1--3 are exactly the occurrence-labelled Boolean-hex identity,
so replacing \(O\) by \(N\) preserves all four matching shores.  Condition
4 is precisely static table transparency and condition 5 makes the old
phase selected rather than merely available.  Therefore (4.1) is a legal
factor toggle.  Conversely, any literal Boolean-hex factor toggle supplies
these data by reading its six atoms and its ambient selected matching.

Deleting one selected edge from each of three distinct directed cycles
produces three directed paths, and the new edges concatenate them into one
cycle.  Thus three cycles become one.  If old edges lie on paths or two lie
on the same component, other cut-and-join outcomes are possible; they are
outside the specifically defined ternary three-cycle fusion witness.
\(\square\)

For a *same-background* toggle one may strengthen condition 5 to

\[
 M=R\mathbin{\dot\cup}O,qquad
 M'=R\mathbin{\dot\cup}N                                  \tag{4.2}
\]

with one occurrence-labelled residual matching \(R\).  This is the exact
common-residual condition needed by a phase-paired module.

## 5. Exact conjunction with functional Hall descent

Fix a functional attachment \(\vartheta\), let \(B_\vartheta(F)\) be the
predecessor graph, and write

\[
 D=\max_Y\bigl(|Y|-|N_F(Y)|\bigr).                         \tag{5.1}
\]

For the row circuit \(C:F\to F'\), put

\[
 \kappa_C(Y)=|N_{F'}(Y)-N_F(Y)|-|N_F(Y)-N_{F'}(Y)|.        \tag{5.2}
\]

### Theorem 5.1 (topology-plus-cut criterion)

A row circuit is simultaneously

* a prospective ternary three-cycle fusion, and
* a one-unit improvement of the functional predecessor matching rank

if and only if:

1. it has a generalized HexLift witness whose three old atoms lie on three
   distinct directed cycle components; and
2. for every head set \(Y\),

\[
 \kappa_C(Y)\ge |Y|-|N_F(Y)|-D+1.                         \tag{5.3}
\]

Under these conditions the topology toggle changes \(c\) to \(c-2\), and
the new functional graph has matching rank at least
\(|V|-D+1\).

#### Proof

Theorem 4.1 is equivalent to the first conclusion.  The functional Hall
cut min--max theorem is equivalent to (5.3) and the second conclusion.  The
two statements concern the same row circuit, so their conjunction is
necessary and sufficient for the two declared objective changes.  \(\square\)

The word **prospective** is load-bearing.  Separate witnesses for items
1--2 need not be realized by one final factor.  A literal joint realization
additionally requires a common extension: after forcing \(O\) in the old
matching and \(N\) in the new matching, the residual matching/augmenting
linkage must exist in the corresponding contracted atlases.  Equivalently,
one must pass the forced-edge Hall/Rado test after deleting the common four
resource sets.  Neither component distinctness nor (5.3) implies this
co-realization row.

For a quick sufficient cut test, it is enough that the hex circuit adds one
new external punctured-facet neighbour to a critical shore and preserves at
least one old witness for every old neighbour, **and** that the analogous
nonloss inequalities hold on every other critical or near-critical Hall
shore.  Positivity on only the canonical K17 shore is necessary but not
sufficient.

## 6. Reconciliation with the opposite-seam no-go

The phase-paired single-ear no-go proves that opposite orientations of one
reset seam have no pair of independent Cartesian gain ears with the same
old-pair tail resource set.  The six K17 commutators do not evade it:

* they are closed resource-zero row substitutions, not gain ears through a
  state with one free tail/head/owner/lower tuple;
* they provide no common residual factor contraction; and
* matching-closed Boolean-hex circuits have even attachment parity, whereas
  the rolling-reset phase exchange requires an odd attachment return.

Thus the first live reset use is a **coupled multi-ear generalized
HexLift**.  It must cancel the opposite-seam tail difference internally,
retain an open gain/loss state until the odd attachment return is installed,
and then pass the exact criteria of Sections 4--5.  A large menu of static
row commutators, even cut-positive ones, is not a substitute for that
module.

## 7. Exact boundary

What is proved:

* the strict Boolean HexLift fingerprint;
* failure of all six K17 serial circuits on that fingerprint;
* absence of any frozen ternary component certificate in their audit scope;
* an exact generalized HexLift/component criterion; and
* the exact all-cut condition for simultaneous prospective topology and
  functional-Hall improvement.

What remains open:

* whether a generalized HexLift occurs in some completion near any of the
  six K17 tables;
* whether one such lift has its old atoms on three distinct components;
* whether forced old/new hex phases admit a common residual matching while
  satisfying every Hall cut; and
* whether a coupled multi-ear module can also meet residence, arbitrary
  upper shadows, voltage, opening and compiler constraints.

No conclusion about \(\nu(k)\) follows.

## 8. Frozen inputs

```text
MATH_THEOREM_BOOLEAN_HEX_THREE_CYCLE_FUSION_AND_TERNARY_CONTRACTION_20260801.md
MATH_THEOREM_D3_BOOLEAN_HEX_RESET_SPLICE_AND_PRIVATE_UPPER_OBSTRUCTION_20260801.md
MATH_THEOREM_OPPOSITE_SEAM_CARTESIAN_GAIN_EAR_COMMON_RESIDUAL_NOGO_20260801.md
MATH_THEOREM_A_D3_NORMALIZED_RESOURCE_CIRCUITS_AND_FUNCTIONAL_CUT_DESCENT_BOUNDARY_20260801.md
MATH_THEOREM_A_K17_2E919_CRITICAL_SHORE_SUPPORT3_COMMUTATOR_ESCAPE_20260801.md
scratch/threadA_k17_commonfirst_support3_serial_chain_20260801.manifest.tsv
scratch/threadA_k17_{2e919,4f5,1852,0c27,b355,45a0}_dm_support3_commutator_20260801/literal_ledger.tsv
scratch/threadA_k17_{2e919,4f5,1852,0c27,b355,45a0}_dm_support3_commutator_20260801/edge_delta.tsv
```

All numerical values in Section 3 are copied from independently replayed,
frozen ledgers and audits.  No new computation is used.
