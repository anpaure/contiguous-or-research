# Literal rank-six rigidity in an optimal eleven-bit array

## Outcome

For a hypothetical universal nonzero eleven-bit array of length 465:

1. at most one distinct rank-six mask occurs literally;
2. every literal rank-six entry is at position `0` or `464`;
3. the two boundary positions cannot both have rank six.

Consequently there is at most one literal rank-six **occurrence** in the whole
array.  Since coordinate permutations and word reversal preserve universality,
an existence search may WLOG require

```text
the only possible rank-six entry is A[0]=63.
```

This statement permits either `A[0]=63` or no rank-six entry at all.

## 1. At most one distinct mask

The audited odd cross-layer theorem applies to every independently chosen
rank-five/rank-six witness family and gives `x0<=1`, where `x0` is the number
of selected rank-six singleton witnesses.

If two distinct rank-six masks occurred as array entries, deliberately choose
their two singleton occurrences as the corresponding witnesses and choose all
other central witnesses arbitrarily.  This would give `x0>=2`, a
contradiction.  Thus all literal rank-six entries, if any, have one common
mask `C`.

## 2. Every occurrence is at a word boundary

Fix any literal occurrence `[p,p]` of `C` and deliberately select it as the
rank-six witness for `C`.  The rank-six band inequalities force at least one
width-three witness, so state `03` occurs in the coordinatewise monotone
rank-six schedule.  The only width-zero states comparable with `03` are `00`
and `33`.  Since `x0<=1`, a selected `00` singleton is the unique first slot
and lies at physical position zero, while a selected `33` singleton is the
unique last slot and lies at physical position 464.

Therefore the deliberately selected position `p` belongs to `{0,464}`.
Because the argument applies to every literal occurrence separately, no
rank-six entry can occur in an interior position.

## 3. Both endpoints cannot occur

Assume for contradiction that both `A[0]` and `A[464]` have rank six.  They
have the same mask by Section 1.  Any interval whose OR has rank at most five
avoids both endpoints, so the interior word

```text
A[1],...,A[463]
```

of length 463 still represents every mask of ranks one through five.

In particular it represents all

```text
C(11,5)=462
```

rank-five masks.  Select one witnessing interval for each and sort by left
endpoint.  Equal-rank nonnesting gives 462 distinct left and right endpoints
inside 463 positions, so the `i`th selected interval lies inside `[i,i+1]`.
Every physical interval of length at least two consequently contains a
selected rank-five witness and has OR rank at least five.

Every target of ranks one through four must therefore be represented by a
singleton entry of the 463-position interior word.  But there are

\[
 {11\choose1}+{11\choose2}+{11\choose3}+{11\choose4}
 =11+55+165+330=561
\]

distinct such targets.  One physical singleton has one OR value, so 463
positions cannot represent 561 different masks.  This contradiction proves
that at most one boundary occurrence exists.

## 4. Canonical existence normal form

If the unique literal rank-six occurrence is at position 464, reverse the
array.  Contiguous intervals remain contiguous and their OR values are
unchanged as a family, so the occurrence moves to position zero.  If its mask
is `C`, apply a coordinate permutation sending `C` to

```text
{0,1,2,3,4,5}, decimal 63.
```

Coordinate permutations commute with OR and biject the target masks.  Thus
every isomorphism class with a literal rank-six entry has a representative
with `A[0]=63`; arrays with no rank-six entry need no transformation.

Equivalently, a symmetry-reduced exact solver may forbid:

```text
every rank-six mask at positions 1,...,464;
every rank-six mask other than 63 at position 0.
```

This is a satisfiability-preserving normal form, not a necessary condition on
one fixed labelling and orientation.

## 5. CNF consequence

For a fixed forbidden eleven-bit mask `S` at position `p`, the single clause

```text
(OR_(b in S) -A[p,b]) OR (OR_(b not in S) A[p,b])
```

is false exactly when `A[p]=S`.

The complete canonical-left normal form therefore uses

```text
position 0:   461 forbidden rank-six masks,
positions 1..464: 464*462 forbidden rank-six masks,
total clauses: 461+464*462 = 214,829,
variables: 0.
```

Compared with the already implemented canonical-mask gate (214,365 clauses),
the full literal-rigidity normal form needs only 464 additional clauses: it
forbids mask 63 at positions 1 through 464.

## 6. Scope

The first three statements are coordinate-labelled necessary theorems except
for the common-mask name; Section 4 additionally uses reversal and coordinate
symmetry to choose the representative `A[0]=63`.  No fixed derivative row,
Johnson adjacency, connected forest, or computational search result is used.

The theorem does not say that a rank-six literal must occur.  It gives a
two-branch normal form: either there is none, or the first entry is 63 and no
other entry has rank six.
