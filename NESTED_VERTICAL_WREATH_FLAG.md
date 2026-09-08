# A nested vertical-wreath flag and the two-coordinate sector ledger

## Status

The fully vertical exact factor on nine coordinates contains a literal

\[
   Q_5\subset Q_7\subset Q_9
\]

flag of fully vertical exact wreath factors.  The flag is stronger than a
coincidence of projected middle layers: at both steps the retained rows are
exactly the maximum-separation rows for the deleted coordinate pair.  Thus
the numbers of retained rows are the consecutive Catalan numbers

\[
   C_2=2,\qquad C_3=5,\qquad C_4=14.
\]

An exhaustive independent checker is
`scratch/check_nested_vertical_wreath_flag.py`.

The flag also reveals the correct numerical shape of a two-coordinate lift.
For a saturated lift from `2m-1` to `2m+1` coordinates, `C_{m-1}` inherited
rows may be placed at maximum separation, but the remaining

\[
 C_m-C_{m-1}=\frac{3(m-1)}{m+1}C_{m-1}
\]

rows must have smaller separation.  Their mean separation is forced to be
`(m+1)/3`.  In particular, the clean `Q_9 -> Q_11` target consists of
fourteen inherited type-five rows and twenty-eight new type-two rows.

This is a finite exact-cover formulation, not yet a construction of the
`Q_11` factor.

## 1. Definitions

For a cyclic order `pi` on a set of size `2m+1`, its wreath is the family of
all cyclic intervals of `pi`.  A family of `C_m` cyclic orders is an exact
middle factor if its length-`m` intervals partition
`binom([2m+1],m)`.  It is fully vertical if its cyclic intervals cover every
proper nonempty subset.

Fix two coordinates `a,b`.  The **type** of a row is

\[
 h=\min\{\operatorname{dist}_\pi(a,b),
          2m+1-\operatorname{dist}_\pi(a,b)\},
 \qquad 1\le h\le m.
\tag{1.1}
\]

Deleting `a,b` from a row means deleting the two symbols and retaining the
induced cyclic order on the other `2m-1` symbols.

## 2. The explicit Catalan flag

Number the rows of `m4_fully_vertical_wreath_factor.txt` from one to
fourteen.

### Theorem 2.1

Delete coordinates `{2,9}` and retain rows

\[
  2,3,5,6,11.
\tag{2.1}
\]

The resulting five orders form a fully vertical exact factor on
`{1,3,4,5,6,7,8}`.  They are

```text
1 3 7 4 5 6 8
1 4 7 6 3 8 5
1 5 7 3 8 4 6
1 6 3 4 5 8 7
1 4 8 7 6 5 3
```

Inside this `Q_7` factor, delete `{1,3}` and retain its second and third
rows.  The resulting two orders

```text
4 7 6 8 5
5 7 8 4 6
```

form a fully vertical exact factor on `{4,5,6,7,8}`.

Moreover, the five retained `Q_9` rows are exactly all type-four rows for
the pair `{2,9}`, and the two retained `Q_7` rows are exactly all type-three
rows for the pair `{1,3}`.

#### Verification

Direct enumeration gives the type histograms

\[
\begin{array}{c|rrrr}
&h=1&h=2&h=3&h=4\\ \hline
Q_9\text{ relative to }\{2,9\}&4&4&1&5,
\end{array}
\tag{2.2}
\]

and

\[
\begin{array}{c|rrr}
&h=1&h=2&h=3\\ \hline
Q_7\text{ relative to }\{1,3\}&2&1&2.
\end{array}
\tag{2.3}
\]

The retained rows therefore are precisely the maximum-type rows.  Literal
set enumeration verifies that the `5*7=35` length-three intervals in (2.1)
are all 35 three-subsets, and that every other proper rank is covered.  The
same calculation gives all ten two-subsets from the two projected `Q_5`
rows and full vertical coverage there.

### Theorem 2.2 (exhaustive uniqueness at the first projection)

Among all 36 choices of a deleted coordinate pair and all
`binom(14,5)=2002` five-row subsets, the certificate has exactly two
projected exact `Q_7` factors:

\[
\begin{array}{c|c}
\text{deleted pair}&\text{retained original rows}\\ \hline
\{2,9\}&2,3,5,6,11,\\
\{5,6\}&1,5,7,9,14.
\end{array}
\tag{2.4}
\]

Both are fully vertical.  Each contains exactly 35 projected exact `Q_5`
flags.  In either core, 19 of the 21 deleted coordinate pairs participate:
four pairs support one row-pair choice, fourteen support two choices, and
one supports three.  All ten row pairs participate, five in three flags and
five in four flags.

Thus the `Q_7` core is highly constrained inside the `Q_9` certificate,
whereas its `Q_5` subcores are flexible.  Only the first core in (2.4) is the
maximum-type recursive core for its deleted pair.

## 3. Exact sector counts for two new coordinates

Let a length-`m` interval be classified by how many of `a,b` it contains.

### Lemma 3.1 (row-type ledger)

A type-`h` row has respectively

\[
  m+1-h,\qquad 2h,\qquad m-h
\tag{3.1}
\]

length-`m` intervals containing zero, one, and two of `a,b`.

#### Proof

The starts of windows containing both marked points form an intersection of
two cyclic start intervals.  Since the shorter marked-point distance is
`h<=m` and the other distance is at least `m+1`, this intersection has size
`m-h`.  Each marked point lies in exactly `m` length-`m` windows, so the
number containing exactly one is `2m-2(m-h)=2h`.  Subtracting from the
`2m+1` total windows leaves `m+1-h`.  QED.

Let `r_h` be the number of type-`h` rows in any exact middle factor.  The
three coordinate sectors have sizes

\[
 \binom{2m-1}{m},\qquad
 2\binom{2m-1}{m-1},\qquad
 \binom{2m-1}{m-2}.
\tag{3.2}
\]

Consequently exactness forces

\[
 \sum_{h=1}^m r_h=C_m,
 \qquad
 \sum_{h=1}^m h r_h=inom{2m-1}{m-1}
                  =\frac{m+1}{2}C_m.
\tag{3.3}
\]

The other two sector equations follow from these.

## 4. The saturated Catalan lift

Suppose exactly `C_{m-1}` rows are type `m`, and after deletion of `a,b`
their projections form a fully vertical exact factor on `2m-1` points.
Call these rows inherited.  Write `s_h=r_h` for `h<m`.

### Theorem 4.1 (forced new-row ledger)

The new rows obey

\[
 \sum_{h<m}s_h=C_m-C_{m-1}
   =\frac{3(m-1)}{m+1}C_{m-1},
 \qquad
 \sum_{h<m}h s_h=(m-1)C_{m-1}.
\tag{4.1}
\]

Their mean type is therefore

\[
 \frac{m+1}{3}.
\tag{4.2}
\]

Their required contributions to the zero-, one-, and two-new-coordinate
sectors are

\[
 2(m-1)C_{m-1},\qquad
 2(m-1)C_{m-1},\qquad
 \binom{2m-1}{m-2},
\tag{4.3}
\]

respectively.

#### Proof

Use

\[
 C_m=\frac{2(2m-1)}{m+1}C_{m-1}
\tag{4.4}
\]

in (3.3), and subtract the contribution `m C_{m-1}` of the inherited
rows.  Equations (4.1)--(4.3) follow by elementary simplification.  QED.

This proves that the obvious insertion-only lift fails: maximum-separation
rows have `m-h=0`, so no collection consisting only of such rows can cover a
single middle target containing both new coordinates.  The smaller types
are not optional defects; they carry the entire two-new-coordinate sector.

There is a more precise description of what the inherited rows accomplish.
Write a type-`m` row as

\[
 (a,x_1,\ldots,x_{m-1},b,y_1,\ldots,y_m).
\tag{4.5}
\]

After deleting `a,b`, the one-new-coordinate windows project onto every
length-`m-1` interval of the old cyclic order.  Exactly one projection,
`{x_1,...,x_{m-1}}`, occurs twice, once with each new coordinate; every
other projection occurs once with one of the two tags.  Hence an inherited
old factor covers one tagged copy of every old middle set and both tags of
exactly `C_{m-1}` pivot sets.  The new rows must supply the opposite tag on
the remaining `2(m-1)C_{m-1}` middle sets, in addition to the other two
sectors in (4.3).

The observed schedules are

\[
\begin{array}{c|rrrr|r}
\text{lift}&s_1&s_2&s_3&s_4&r_m\\ \hline
Q_5\to Q_7&2&1&&&2,\\
Q_7\to Q_9&4&4&1&&5.
\end{array}
\tag{4.6}
\]

Both satisfy (4.1) exactly.

## 5. A finite `Q_9 -> Q_11` lift target

Here `m=5`, `C_4=14`, and `C_5=42`.  Equation (4.1) says that the 28 new
rows have total type 56.  The cleanest solution is

\[
 r_5=14,\qquad r_2=28,
 \qquad r_1=r_3=r_4=0.
\tag{5.1}
\]

Its middle-sector ledger is

\[
\begin{array}{c|rrr|r}
\text{rows}&0\text{ new}&1\text{ new}&2\text{ new}&\text{count}\\ \hline
14\text{ type }5&14&140&0&14,\\
28\text{ type }2&112&112&84&28,\\ \hline
\text{total}&126&252&84&42.
\end{array}
\tag{5.2}

These are exactly
`binom(9,5)`, `2 binom(9,4)`, and `binom(9,3)`.

More generally, if the 28 new rows have counts `s_1,...,s_4`, then

\[
 s_1=s_3+2s_4,
 \qquad
 s_2=28-2s_3-3s_4,
 \qquad 2s_3+3s_4\le28.
\tag{5.3}
\]

Thus (5.1) is the unique one-type schedule, not a necessary restriction.

### Exact-cover formulation

Take the verified fourteen-row `Q_9` factor on old coordinates `[9]` and
new coordinates `a,b`.

1. For each old row choose one of its 18 unoriented type-five insertions of
   `a,b`.  There are nine possible pivot cuts and two tag orientations.
2. Choose 28 type-two cyclic orders on the eleven coordinates.  With `a`
   fixed as the cyclic origin and the orientation chosen so that `b` is at
   distance two, there are exactly `9!=362880` candidates.
3. Impose exact-one coverage on all `binom(11,5)=462` middle targets.
4. Impose at-least-one coverage on ranks one through four.  Complementation
   then gives ranks six through ten.

This uses 252 inherited-row candidates plus 362880 new-row candidates,
fourteen inherited group constraints, one 28-row cardinality constraint,
462 exact-cover constraints, and 561 lower-rank coverage constraints before
encoding auxiliaries.  It is a concrete finite lift problem rather than the
unstructured search over arbitrary 42-row factors.

Satisfying this formulation would produce a fully vertical exact `Q_11`
factor and prove the next step of the vertical-wreath recursion.  The present
note proves the ledger and the nested seed, but not satisfiability.

## 6. Verification

Run

```text
python3 scratch/check_nested_vertical_wreath_flag.py
```

The checker:

1. independently re-verifies the original `Q_9` factor;
2. exhausts all 72072 candidate `Q_7` projections and finds exactly (2.4);
3. exhausts all 210 candidate `Q_5` projections inside each core and finds
   35 in each;
4. verifies full vertical coverage of every reported factor;
5. checks the maximum-type claims, Catalan identities, and the exact
   `14+28` sector ledger (5.2).
