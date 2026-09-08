# The literal two-coordinate insertion lift from `Q_9` to `Q_11` is impossible

## Status

Start from the fully vertical fourteen-wreath factor in
`m4_fully_vertical_wreath_factor.txt`.  Above each of its cyclic orders,
insert the two new symbols `10,11` into arbitrary cyclic gaps, allowing both
orders when they share a gap, and identify cycles modulo rotation and
reversal.

There is **no** choice of 42 resulting eleven-cycles whose length-five cyclic
intervals partition `binom([11],5)`.  In particular, this lift fails before
one imposes any coverage requirement at ranks one through four.

The exhaustive SAT instance is small and UNSAT, but the result does not need
SAT: Sections 3--5 give a two-target Hall obstruction involving only source
rows 1, 4, and 11.  The independent verifier is
`scratch/verify_q11_wreath_insertion_obstruction.py` and the compact
certificate is `q11_wreath_insertion_obstruction_certificate.txt`.

This theorem concerns only the literal insertion family.  It is not an
obstruction to general wreath factors on eleven coordinates.

## 1. Candidate enumeration

Fix a cyclic source order on nine symbols.  If symbols 10 and 11 enter
different old gaps, there are `9*8=72` labelled choices.  If they enter the
same gap, there are `9*2=18` choices, because either order is possible.
Thus every source order has exactly

\[
72+18=90
\]

dihedral insertion classes.  The fourteen source orders produce disjoint
families, since deleting 10 and 11 recovers the source dihedral class.
Consequently the complete search family has

\[
14\cdot90=1260
\]

candidates.

Every rank-five target belongs to at least twenty candidates.  Hence the
failure is not caused by a target with no available representative.

## 2. The three rank-five sectors

Partition the rank-five targets according to the number of new symbols they
contain.  Their cardinalities are

\[
\binom95=126,\qquad 2\binom94=252,\qquad \binom93=84.
\tag{2.1}
\]

For a candidate cycle `omega`, let `a(omega)` be the number of its length-five
windows containing both new symbols.  Each fixed symbol belongs to exactly
five length-five windows of an eleven-cycle.  Inclusion-exclusion therefore
gives the exact sector profile

\[
(\#0\text{-new},\#1\text{-new},\#2\text{-new})
  =(a+1,10-2a,a).
\tag{2.2}
\]

Suppose hypothetically that selected candidates cover the one-new and
two-new targets exactly.  If `N` is their number, summing (2.2) gives

\[
\sum a=84,\qquad 10N-2\sum a=252,
\]

and hence

\[
N=42.
\tag{2.3}
\]

Thus the contradiction below does not use the 126 zero-new targets at all.

## 3. Every source row would have to choose a clean triple

Let `pi_b` be source row `b`.  Its nine cyclic rank-four intervals occur in
no other source row, because the `Q_9` factor is exact at rank four.
Accordingly, each tagged target

\[
\{10\}\cup I_{\pi_b}(j,4),\qquad
\{11\}\cup I_{\pi_b}(j,4)
\]

can be covered only by an insertion candidate above row `b`.

Let `n_b` candidates be selected above row `b`, and put
`A_b=sum a(omega)` over them.  Exact coverage of these eighteen tagged
targets and (2.2) imply

\[
10n_b-2A_b=18,
\qquad A_b=5n_b-9.
\tag{3.1}
\]

A two-new window contains three old symbols, and those symbols are a cyclic
rank-three interval of `pi_b`.  There are only nine such triples.  Global
rank-five exactness makes the `A_b` two-new windows distinct, so

\[
A_b\le9,
\qquad n_b\le3.
\tag{3.2}
\]

Equation (2.3) and the fourteen inequalities (3.2) force equality
everywhere:

\[
n_b=3,\qquad A_b=6\quad(1\le b\le14).
\tag{3.3}
\]

Hence every source row must choose a **clean local packet** of three
insertion candidates.  It covers the eighteen one-new targets exactly and
six distinct old cyclic triples in the two-new sector.  Write `D_b` for the
three omitted old cyclic triples.

## 4. The local omission lemma

### Lemma 4.1

For any cyclic source order, exactly 60 triples of insertion candidates are
clean local packets.  They induce 30 different omission packets, each twice.
In cyclic position indices modulo 9, the omission packets are exactly the
three-subsets whose cyclic gap multiset is one of

\[
\{1,1,7\},\qquad \{1,2,6\},\qquad \{3,3,3\}.
\tag{4.1}
\]

### Verification

There are only 90 candidates.  The independent checker literally enumerates
their one-new and two-new length-five windows, performs exact cover of the
eighteen one-new targets with three candidates, rejects a packet if its six
two-new targets collide, and compares the resulting omission patterns with
(4.1).  This produces `60=2*30` for every source row.

The source factor's cyclic rank-three multiplicity histogram is

\[
44\text{ triples at multiplicity }1,quad
38\text{ at multiplicity }2,quad
2\text{ at multiplicity }3.
\tag{4.2}
\]

A triple of multiplicity `mu` must occur in exactly `mu-1` omission packets:
all `mu` source rows can potentially supply its two-new target, and exactly
one must retain it.  In particular, multiplicity-one triples may not be
omitted.  Removing from (4.1) every packet containing such a triple leaves
the domain sizes

```text
1, 2, 9, 10, 6, 14, 5, 4, 3, 20, 2, 4, 6, 3.
```

## 5. A two-target Hall obstruction

Write `129` for the set `{1,2,9}`, and similarly for other triples.

The only legal omission packet above source row 1 is

\[
D_1=\{456,567,678\}.
\tag{5.1}
\]

The triple 129 occurs in source rows 1 and 4 only.  Since row 1 cannot omit
129, exact coverage forces

\[
129\in D_4.
\tag{5.2}
\]

The only legal omission packets above source row 11 are

\[
\{267,148,478\},\qquad \{148,478,139\}.
\tag{5.3}
\]

The triple 356 occurs in source rows 4 and 11 only.  Neither packet in (5.3)
omits it, so exact coverage forces

\[
356\in D_4.
\tag{5.4}
\]

However, the ten legal omission packets above source row 4 are

```text
{124,248,358}  {124,248,129}  {124,358,679}  {124,129,679}
{356,248,358}  {356,567,358}  {356,358,679}  {567,358,679}
{356,567,679}  {567,129,679}.
```

None contains both 129 and 356, contradicting (5.2)--(5.4).  This proves:

### Theorem 5.1

No family of two-symbol insertions above the certified fourteen-row `Q_9`
factor exactly covers `binom([11],5)`.  Therefore no member of this family is
a vertically complete `Q_11` wreath factor.

## 6. SAT cross-check

`scratch/search_q11_wreath_insertion.py` independently constructs a CNF with
one variable per insertion candidate and Sinz exact-one constraints for all
462 middle targets.

```text
middle only:       14,658 variables   40,194 clauses   UNSAT
ranks 1--4 added:  14,658 variables   40,755 clauses   UNSAT
```

Kissat proves the middle instance UNSAT in 91 conflicts.  The retained
solver artifacts are

```text
scratch/q11_wreath_insertion_middle.cnf
scratch/q11_wreath_insertion_middle.drat
scratch/q11_wreath_insertion_full.cnf
```

The DRAT trace is supplemental; Theorem 5.1 and the independent enumerator
already constitute a direct proof.

## 7. Consequence for the global programme

The fully vertical `Q_9` factor does not admit the most literal two-coordinate
induction.  The obstruction is sharper than a loss of lower shadows: the
middle exact cover itself fails, and it fails in the sectors containing the
new coordinates.

Any successful `Q_9 -> Q_11` recursion must therefore permit at least one of:

1. changing the underlying fourteen-row factor before lifting;
2. reordering old coordinates inside lifted cycles rather than merely
   inserting the new ones;
3. using switches that couple candidates descending from different source
   rows;
4. abandoning a one-parent-per-wreath lift.

This negative result narrows the recursion search, but it neither proves nor
disproves the conjectural shortest OR length at `k=11`.

## 8. Frozen hashes

```text
043b69d3d36932925a066238fe7f8f7f692cb1a462b98ba334770f6d2caf7f4a  m4_fully_vertical_wreath_factor.txt
868b77b2fe9f58869a6605949ae9cdad6ee5957e53f5c0eabb06be055d45f384  scratch/search_q11_wreath_insertion.py
2b6c676a6221490be3502e896c7745866f6c77128493d2ca24b9145f512867ee  scratch/verify_q11_wreath_insertion_obstruction.py
5fb152b230103e834751d255deea06a974be1f909cbddfc127532ac787c7c3b9  q11_wreath_insertion_obstruction_certificate.txt
7d87ae4c37731fcb711d6c9ac03cb47ed3144216c5d3d033ac27366925f321f0  scratch/q11_wreath_insertion_middle.cnf
e87b83eec5cd22656fe40c2cb326f43a716b90f34f2a8b5047c552c52f0adf18  scratch/q11_wreath_insertion_middle.drat
67016f621132b3d76db3e4b7068fd4018d95f0e3c7c9020e27e49e464058a179  scratch/q11_wreath_insertion_full.cnf
```
