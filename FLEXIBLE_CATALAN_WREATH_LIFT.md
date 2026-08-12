# Flexible Catalan wreath lifts: the parent-packet obstruction

## 1. Verdict

Allowing arbitrary reordering of the old rows, and even allowing arbitrary
balanced eight-switches before lifting, does **not** rescue the literal
two-coordinate insertion recursion in general.

Let the old dimension be `2m-1` and the new dimension be `2m+1`.  Start with
an arbitrary exact wreath factor on the old coordinates.  Suppose every new
wreath is obtained by inserting the two new coordinates into one old row;
the old row is called its parent.  Exact middle coverage forces every old
row to have the same number

\[
 q_m=\frac{2(2m-1)}{m+1}=4-\frac6{m+1}
\tag{1.1}
\]

of children.  Consequently this architecture is possible only when
`m+1` divides `6`, namely

\[
 m\in\{1,2,5\}.
\tag{1.2}
\]

This is an all-dimensional obstruction.  It is independent of the choice of
old factor, its row order, vertical shadow quality, and its balanced-switch
component.  In particular, a literal parent-preserving lift cannot be an
induction proving vertical wreath factors in every odd dimension.

The first open Boolean case is the exceptional integral case `m=5`, i.e.
`Q_9 -> Q_11`.  There each parent has exactly three children.  Requiring all
three new-coordinate sectors to be exact collapses the thirty omission
patterns from the earlier one/two-sector audit to exactly three phases:

\[
 \{0,3,6\},\qquad \{1,4,7\},\qquad \{2,5,8\}.
\tag{1.3}
\]

Thus the completely flexible exceptional lift is an exact phase problem:
choose **any** exact `Q_9` wreath factor and one of the three phases on each
of its fourteen rows so that the six retained cyclic triples per row
partition all 84 triples.  This strictly contains the previously rejected
fixed-factor insertion search.

The exact search for this exceptional phase problem is finite and currently
unresolved.  The general obstruction (1.1), however, is proved.

## 2. Exact old and new factors

Let `V` have size `2m-1`, and let `a,b` be the two new coordinates.  An old
exact factor `F` is a family of cyclic orders `pi` on `V` whose cyclic
intervals of length `m-1` partition

\[
 \binom{V}{m-1}.
\tag{2.1}
\]

The complementary length-`m` intervals then also partition
`binom(V,m)`.

An insertion child of `pi` is a cyclic order `omega` on
`V union {a,b}` obtained by inserting `a,b` into the cyclic gaps of `pi`,
without changing the old cyclic order.  Deleting `a,b` from `omega` recovers
`pi`.

Classify the length-`m` windows of `omega` by whether they contain zero, one,
or two new coordinates.  If the shorter cyclic distance between `a,b` in
`omega` is `h`, then the exact sector profile is

\[
 (z,o,t)=(m+1-h,\ 2h,\ m-h).
\tag{2.2}
\]

This is the row-type ledger from the nested-wreath analysis.

## 3. The parent-packet theorem

For an old row `pi`, let `P_pi` be all selected new rows whose deletion of
`a,b` is `pi`.

### Theorem 3.1 (local ownership)

If the selected insertion children form an exact middle factor on
`V union {a,b}`, then, separately for every old row `pi`:

1. the zero-new windows of `P_pi` are exactly the `2m-1` cyclic length-`m`
   intervals of `pi`, each once;
2. for each tag `a` and `b`, the one-new windows of `P_pi`, after deleting
   the tag, are exactly the `2m-1` cyclic length-`m-1` intervals of `pi`,
   each once.

#### Proof

A one-new target `{a} union S` projects to a cyclic length-`m-1` interval
`S` in the parent row of any child that realizes it.  By (2.1), exactly one
old row contains `S` as such an interval.  Hence both tagged copies of every
old middle target have a unique parent, and exact new coverage forces the
second assertion parent by parent.

Likewise, an old `m`-set `T` is a cyclic length-`m` interval in `pi` exactly
when its complement `V\T` is a cyclic length-`m-1` interval there.  Equation
(2.1) therefore gives every zero-new target a unique parent as well.  Exact
coverage gives the first assertion.  QED.

### Theorem 3.2 (uniform child-count obstruction)

Every parent has exactly `q_m` children, with `q_m` given by (1.1).
Consequently a parent-preserving insertion lift can exist only for
`m in {1,2,5}`.

#### Proof

Let a fixed parent have `q` children of types `h_1,...,h_q`.  Theorem 3.1
and the one-new entry of (2.2) give

\[
 2\sum_{j=1}^q h_j=2(2m-1),
 \qquad\text{so}\qquad
 \sum_jh_j=2m-1.
\tag{3.1}
\]

The zero-new entry of (2.2) gives

\[
 \sum_{j=1}^q(m+1-h_j)=2m-1.
\tag{3.2}
\]

Substituting (3.1) into (3.2) yields

\[
 q(m+1)=2(2m-1),
\tag{3.3}
\]

which is (1.1).  Since `q` is an integer, `m+1` divides `6`.  For positive
`m`, this leaves `m=1,2,5`.  QED.

### Corollary 3.3 (switch invariance)

Arbitrary reorderings of the old rows and arbitrary balanced two-wreath
eight-switches cannot evade Theorem 3.2.  Such operations change which old
factor is used but do not change unique ownership or the sector counts.

This is the promised general answer to the switch-enlarged literal lift: the
obstruction survives the enlargement.

## 4. Exact parent-packet equivalence

The preceding proof gives a useful formulation even when the arithmetic is
integral.

For a parent `pi`, call a set of insertion children a **saturated parent
packet** when its zero-new and one-new sectors satisfy Theorem 3.1.  Its
two-new windows, after deleting `a,b`, form a multiset of cyclic
length-`m-2` intervals of `pi`; call this its export.

### Theorem 4.1 (packet gluing)

Fix an exact old factor `F`.  A family of insertion children is an exact new
middle factor if and only if:

1. the children above every `pi in F` form a saturated parent packet; and
2. the exports of all parent packets partition `binom(V,m-2)`.

#### Proof

Necessity of the first condition is Theorem 3.1.  The two-new sector consists
exactly of `{a,b} union R` with `R in binom(V,m-2)`, so exactness gives the
second condition.  Conversely, the first condition partitions the zero- and
one-new sectors, and the second partitions the two-new sector.  These are all
members of `binom(V union {a,b},m)`.  QED.

This theorem is the all-dimensional replacement for the vague instruction
"insert two symbols and repair the shadows": it isolates a finite local
packet catalogue and one global export exact cover.

## 5. The exceptional `Q_9 -> Q_11` phase theorem

Set `m=5`.  Theorem 3.2 gives `q_5=3`.  A parent row has nine old cyclic
triples, and its three children must export six of them.  The other three are
the omission packet.

### Lemma 5.1 (complete local classification)

For one nine-cycle there are 90 dihedral two-symbol insertions.  Among all
triples of these candidates, exactly six triples are saturated parent
packets.  Their omission positions are

\[
 036,\quad147,\quad258,
\tag{5.1}
\]

and each phase has exactly two insertion realizations.

The independent checker exhausts `C(90,3)=117480` candidate triples.  It
tests the zero-new, one-new, and two-new windows literally.  This is small
enough that the exhaustive statement is itself a transparent certificate.

Notice the distinction from the previous local lemma: if the zero-new sector
is ignored there are 60 packets with 30 omission patterns.  Twenty-seven of
those patterns necessarily duplicate a zero-new target.  They cannot occur
in an exact `Q_11` factor.

### Theorem 5.2 (flexible phase equivalence)

There is a parent-preserving exact lift from some exact `Q_9` factor if and
only if there exist fourteen cyclic orders `pi_i` and phases
`e_i in {0,1,2}` such that

1. their length-four intervals partition `binom([9],4)`; and
2. the length-three intervals in positions not congruent to `e_i mod 3`
   partition `binom([9],3)`.

Every satisfying phase system expands in exactly `2^14` ways to an exact
`Q_11` middle factor.

#### Proof

Apply Theorem 4.1 and Lemma 5.1.  The first condition is precisely old middle
exactness.  For phase `e_i`, the export is the six old triples outside that
residue class.  Export exactness is the second condition.  Each phase has two
independent local realizations.  QED.

This permits arbitrary old-row reordering.  Balanced switches are included
because they simply navigate among possible exact fourteen-row factors.

## 6. Exact search and verification

`scratch/search_flexible_q9_q11_lift.py` searches Theorem 5.2 rather than a
fixed old certificate.  Coordinate symmetry fixes the row
`1,2,...,9` and phase `036`.  After deleting immediate conflicts, the exact
CNF has

```text
12,524 old-row candidates
31,272 row-phase candidates
362,697 variables
991,125 clauses
```

It imposes exact-one constraints on the remaining rank-four and retained
rank-three targets.  A SAT model is expanded to 42 explicit eleven-cycles
and checked again.

`scratch/search_q9_switch_liftable.py` explores the balanced-switch component
with the same exact three-phase condition.  It is a candidate generator, not
a proof of connectedness.

`scratch/verify_flexible_catalan_wreath_lift.py` is independent of both
searches.  Without any solver it verifies Lemma 5.1.  Given a 42-row
certificate it also verifies:

* 14 parents with 3 children each;
* exact old rank-four coverage;
* the three-phase rule and exact exports;
* exact new rank-five coverage; and
* the missing counts at every cyclic depth.

## 7. Mathematical consequence

The old-order-preserving obstruction was not merely a defect of one
fourteen-row `Q_9` factor.  At almost every dimension it is forced before
one examines Hall defects or shadow quality at all.  The only nontrivial
integral exception is exactly `Q_9 -> Q_11`, where the broad search reduces
to the three-phase exact cover of Theorem 5.2.

Therefore a genuine all-dimensional Catalan recursion must break parent
ownership: some new wreaths must mix arcs descending from different old
rows, as balanced two-wreath switches naturally do, or must be genuinely new
rows with no single old parent.  The nested `14+28` ledger has precisely this
form.  The next positive theorem should operate on cross-parent packets, not
on more elaborate insertion choices within one parent.
