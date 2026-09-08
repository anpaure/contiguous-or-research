# Three-antichain endpoint packing

## 1. The correct three-colour object

Let `F_1,F_2,F_3` be pairwise disjoint antichains in the punctured Boolean
lattice, and put

```text
V=|F_1|+|F_2|+|F_3|.
```

A **rainbow chain block** is a chain of two or three targets containing at
most one target from each `F_i`.  A **pairwise-forest endpoint packing** is a
pair of collections `L,R` of rainbow chain blocks such that:

1. the blocks in each of `L` and `R` are vertex-disjoint;
2. no target pair occurs together in both an `L`-block and an `R`-block;
3. for every pair of colours `i<j`, join two targets when they occur together
   in a block and retain only colours `i,j`; the resulting bipartite graph is
   a linear forest.

The weight of the packing is

```text
omega(L,R)=sum_(B in L union R)(|B|-1).
```

Let `Lambda_3(F_1,F_2,F_3)` be the maximum possible weight.  This is an
endpoint relaxation: it remembers all three colours and the competition for
the two endpoint incidences of each target, but it does not assert that every
abstract packing is realized by physical intervals.

### Theorem 1 (three-antichain endpoint packing)

Every universal contiguous-OR word of length `n` satisfies

```text
n >= V-floor(Lambda_3(F_1,F_2,F_3)/2).              (1.1)
```

### Proof

Choose one witness interval for every target in `F_1 union F_2 union F_3`.
Group the witnesses first by common left endpoint and then by common right
endpoint.  Delete singleton groups.

Within one antichain, selected witnesses have distinct left endpoints and
distinct right endpoints.  Thus every remaining group is rainbow.  Intervals
sharing an endpoint are nested, so their OR labels form a chain.  The left
groups are vertex-disjoint, as are the right groups.  Two distinct targets
cannot share both endpoints, because then they would have the same physical
interval and hence the same OR value.

Fix two colours.  Their projected left groups and right groups are matchings.
Their union is acyclic by the two-antichain endpoint-forest lemma: an
alternating cycle would make a nontrivial cyclic shift preserve the strict
endpoint order within either antichain.  Therefore every bichromatic
projection is a linear forest, and the physical endpoint groups form an
admissible packing.

If `e_L,e_R` are the numbers of distinct selected left and right endpoints,
the physical packing has weight

```text
(V-e_L)+(V-e_R) >= 2(V-n).
```

It is therefore at most `Lambda_3`.  Rearranging and using integrality proves
(1.1).  QED.

## 2. A computable joint relaxation

For `i<j`, let

```text
lambda_ij=lambda(F_i,F_j)
```

be the maximum edge count of a linear forest in the cross-comparability graph
of `F_i,F_j`.  Let `w` be the width of the union poset
`F_1 union F_2 union F_3`, and put

```text
P=lambda_12+lambda_13+lambda_23,

Lambda_hat_3=min(
    P,
    2(V-w),
    floor((2V+P)/3)
).                                                   (2.1)
```

### Theorem 2 (three-way overlap cap)

```text
Lambda_3(F_1,F_2,F_3) <= Lambda_hat_3,               (2.2)
```

and consequently

```text
n >= V-floor(Lambda_hat_3/2).                        (2.3)
```

### Proof

In an admissible packing let `a_2,a_3` be the total numbers of blocks of
sizes two and three.  Its weight, total number of projected pair edges, and
total nontrivial vertex incidences are respectively

```text
S=a_2+2a_3,
p=a_2+3a_3,
D=2a_2+3a_3.
```

Every bichromatic projection is a linear forest, so

```text
p<=P.                                                (2.4)
```

After adjoining singleton blocks, either side is a chain partition of the
union family.  Dilworth therefore gives weight at most `V-w` on either side:

```text
S<=2(V-w).                                           (2.5)
```

Every target has at most one nontrivial block incidence on each side, hence
`D<=2V`.  The exact identity

```text
D=3S-p
```

and (2.4) give

```text
S<=floor((2V+P)/3).                                  (2.6)
```

Finally `S<=p<=P`.  Taking the minimum of these three caps proves (2.2).
QED.

The incidence cap (2.6) is genuinely three-way.  A size-three endpoint block
saves two endpoint positions, uses three projected pair edges, and consumes
three of the common two-incidence-per-target budget.  This information is
lost when the three pair inequalities are merely added.

## 3. Exact compatibility with the two-family theorem

If `F_3` is empty, then

```text
Lambda_3(F_1,F_2,empty)=lambda(F_1,F_2),
Lambda_hat_3=lambda(F_1,F_2).                        (3.1)
```

Indeed, an admissible packing is then a linear forest whose edges have been
split into left and right matchings.  Conversely, alternately two-colour the
edges of every path in any linear forest; the two colour classes are valid
left and right matchings.  This proves the first equality.

For the second, a linear forest has at most `V` edges.  Also its matching
number is at least half its edge count, while Dilworth identifies the maximum
cross-comparability matching size with `V-w`.  Hence

```text
lambda<=2(V-w),
lambda<=floor((2V+lambda)/3),
```

so the minimum in (2.1) is exactly `lambda`.  Thus Theorems 1--2 extend the
two-antichain theorem without weakening it.

The extension can be stronger than every constituent pair bound and the
ordinary width bound.  On `[3]` take

```text
F_1={{1}},  F_2={{2}},  F_3={{1,3}}.
```

Here `V=3`, `w=2`, and `(lambda_12,lambda_13,lambda_23)=(0,1,0)`.
Theorem 2 gives `n>=3`, whereas every pair theorem and the union-width bound
give only two.  Even summing the three raw pair inequalities gives only two.

## 4. Why a global forest theorem is false

Three colours do **not** force the full shared-endpoint graph to be acyclic.
Consider the six-position word

```text
({3},{1},{0},{0},{2},{4}).
```

Select the following intervals and divide their OR labels into three
antichains:

```text
colour A:
 A_1=[1,4] -> {0,1,3},       A_2=[3,6] -> {0,2,4};

colour B:
 B_1=[1,5] -> {0,1,2,3},     B_2=[2,6] -> {0,1,2,4};

colour C:
 C_1=[2,4] -> {0,1},         C_2=[3,5] -> {0,2}.
```

The shared endpoints form the alternating cycle

```text
A_1 -L- B_1 -R- C_2 -L- A_2 -R- B_2 -L- C_1 -R- A_1.
```

Every displayed endpoint pair is comparable, every colour class is an
antichain, and every bichromatic projection consists of two disjoint edges.
Thus the cycle is physically realizable and cannot be prohibited.  The valid
universal cycle law is the bichromatic linear-forest condition in Theorem 1,
not global acyclicity.

## 5. Exact finite implications of the computable relaxation

The checker `scratch/check_three_antichain_endpoint_packing.py` exhausts all
disjoint triples of arbitrary punctured-cube antichains through `k=4`, using
exact pairwise linear-forest maxima and exact union widths.  The maxima of
the computable bound (2.3) are

| `k` | 1 | 2 | 3 | 4 |
|---:|---:|---:|---:|---:|
| max three-family bound | 1 | 2 | 4 | 6 |

It also checks all triples of complete rank layers through `k=5`; their
maxima are `4,6,11` for `k=3,4,5`.  Thus this first tractable relaxation does
not improve the existing lower bounds in those dimensions.

At `k=11`, take the full central triple of ranks `5,6,7`.  Then

```text
V=462+462+330=1254,
w=462,
(lambda_56,lambda_57,lambda_67)=(923,660,660).
```

The first value follows from a middle-level Hamilton path.  The other two
attain the elementary `2*330` cap; the checker supplies explicit greedy
forests.  Therefore

```text
P=2243,
Lambda_hat_3=min(2243,1584,floor(4751/3))=1583,
n>=1254-floor(1583/2)=463.                           (5.1)
```

The ranks `4,5,6` give the same arithmetic.  Hence the computable three-way
cap remains two positions below `B(11)=465`.  This does not determine the
exact packing number `Lambda_3`: simultaneous nonattainment of the three
pair forests, or additional endpoint-order constraints, could still lower
it.  What is ruled out is the naive global-forest shortcut, and what is
proved is the precise pairwise-forest/rainbow-block relaxation above.

