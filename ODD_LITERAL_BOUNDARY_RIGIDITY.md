# Literal upper-middle rigidity in odd dimensions

## Theorem

Let

```text
k=2r+1,
M=C(k,r)=C(k,r+1),
n=M+d.
```

Assume `d>=2`, a universal nonzero array of length `n` exists, and the exact
cross-layer inequalities force

```text
x0<=1,
xd>0,
```

for every selected rank-`r+1` witness family.  Put

```text
L=sum_(s=1)^(r-1) C(k,s).
```

If

\[
 L>\sum_{ell=1}^{d-2}(n-2-ell+1),                 \tag{1}
\]

where the sum is zero for `d<=2`, then:

1. at most one distinct rank-`r+1` mask occurs literally;
2. every such occurrence lies at the first or last array position;
3. at most one such occurrence exists in total.

Consequently, up to coordinate permutation and word reversal, the only
possible literal rank-`r+1` entry is the canonical mask on the first `r+1`
coordinates at position zero.  No occurrence is required.

## 1. Distinct-mask bound

If two distinct rank-`r+1` masks occur as entries, deliberately select their
singleton occurrences as their two witnesses and select every other central
witness arbitrarily.  This gives `x0>=2`, contradicting the hypothesis that
the cross-layer theorem applies to every witness choice and gives `x0<=1`.

Thus all literal upper-middle entries, if any, have one common mask `C`.

## 2. Boundary localization

Select any particular occurrence `[p,p]` of `C` as the witness for `C`.
After sorting the `M` selected upper-middle witnesses, their states

```text
(alpha_i,beta_i), 0<=alpha_i<=beta_i<=d,
```

are coordinatewise nondecreasing.  A width-`d` witness has the unique state
`(0,d)`.  A width-zero state `(a,a)` is comparable with `(0,d)` only when
`a=0` or `a=d`.

Since `x_d>0`, state `(0,d)` occurs.  Since `x0<=1`, a selected `(0,0)`
singleton is the unique first slot and lies at physical position zero; a
selected `(d,d)` singleton is the unique last slot and lies at physical
position

```text
(M-1)+d=n-1.
```

The deliberately selected occurrence must therefore be a word endpoint.
Applying the argument to each occurrence separately excludes every interior
rank-`r+1` entry.

## 3. Two endpoint occurrences are impossible under (1)

Assume both endpoint entries have rank `r+1`.  Any interval representing a
target of rank at most `r` avoids both endpoints.  Hence the interior word of
length

```text
n-2=M+d-2
```

still represents every rank-`r` mask and every lower target.

Select the `M` rank-`r` witnesses in this shorter word.  Their endpoint slack
is `d-2`.  Therefore every physical interval of length at least `d-1`
contains a selected rank-`r` witness and has OR rank at least `r`.  Every
target of rank at most `r-1` must be represented by an interval of length at
most `d-2`.

The number of such physical intervals is the right side of (1), while there
are `L` distinct lower targets.  One interval has one OR value, so (1) is a
contradiction.  At most one endpoint occurrence exists.

## 4. Exact application at the rank-count lengths below 20

At `n=B(k)` for odd `7<=k<20`, the audited width ledger gives `x0<=1`, and
the short-pool theorem gives the following positive lower bounds on `x_d`:

```text
k:       7    9    11    13     15      17       19
xd >=:  25  126    93   657   3507   16909    77381
d:       2    2     3     3      3       3        3
```

For `d=2`, condition (1) is simply `L>0`.  For `d=3`, its right side is the
interior word length `M+1`.  The exact comparisons are

```text
k=11:  L=561    > M+1=463
k=13:  L=2379   > M+1=1717
k=15:  L=9948   > M+1=6436
k=17:  L=41225  > M+1=24311
k=19:  L=169765 > M+1=92379.
```

Thus every conjectural equality case in odd dimensions `7<=k<20` has at
most one literal rank-`r+1` occurrence, and it is at a word endpoint.

## 5. Canonical existence normal form

Word reversal preserves the family of contiguous intervals, and coordinate
permutations commute with OR and biject the target masks.  If the unique
literal upper-middle occurrence is at the final position, reverse the word;
then permute its mask to

```text
{0,...,r}.
```

Every isomorphism class therefore has a representative in which either no
rank-`r+1` entry occurs or the sole occurrence is the canonical mask at
position zero.  This is a satisfiability-preserving normal form, not a
coordinate-labelled/oriented necessity.

## 6. Scope

The theorem is conditional only on three explicit, independently checkable
inequalities: `x0<=1`, `xd>0`, and (1).  It assumes neither a fixed derivative
row nor Johnson adjacency.  At the proposed odd lengths below 20 all three
hypotheses are already proved by the unrestricted width theory.

For completeness, when `d=1`, two upper-middle endpoint entries are already
impossible because deleting them leaves only `M-1` positions in which to
place witnesses for `M` incomparable rank-`r` masks.  This separate trivial
case is not needed by any row in Section 4.

The theorem does not prove that any proposed length is attainable.  It gives
a strong symmetry reduction for exact searches and a structural invariant
that every eventual construction must satisfy.
