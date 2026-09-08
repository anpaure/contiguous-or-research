# Independent audit of `ODD_CROSS_LAYER_WIDTH_THEORY.md`

## 1. Verdict

**PASS, with two scope clarifications and no mathematical correction.**

I independently rederived the equal-rank endpoint bands, the cross-layer
cumulative inequalities, the summed width separation, the omitted-endpoint
identity, the upper-singleton fan sharpening, the `q_*` obstruction, and the
entire table for odd `7 <= k < 20`.

The potentially delicate quantifier in the source is valid:

> At a conjectural rank-count length in every odd dimension
> `7 <= k < 20`, the array itself can contain literal rank-`r+1` entries of
> at most one **distinct mask**.

This is stronger than a restriction on one auxiliary witness choice.  If two
distinct rank-`r+1` masks occurred literally, select their singleton
occurrences as the witnesses for those two upper targets, select witnesses
for all remaining upper targets arbitrarily, and independently select the
lower witnesses.  Every theorem in the note applies to this deliberately
chosen pair of witness families and yields `x0 <= 1`, a contradiction.
Repeated literal occurrences of the same rank-`r+1` mask are not excluded.

The two recommended wording qualifications are:

1. The displayed constraints are exact **necessary inequalities**, not a
   sufficient characterization of realizable profiles.
2. As an abstract numerical definition, `q_*` should be assigned `+infinity`
   if its defining set is empty.  Under the note's hypothesis that a
   universal candidate exists, the set is automatically nonempty because
   the actual value `q=d-x0` belongs to it.

Neither qualification changes any theorem or any entry of the finite table.

## 2. Equal-rank endpoint bands

Use zero-based physical positions `0,...,M+d-1`.  In a selected witness
family for one rank, two different intervals cannot be nested: nesting of
physical intervals implies inclusion of their OR masks, while distinct
equal-rank masks are incomparable.  After ordering by left endpoint,

```text
l_0 < ... < l_(M-1),
u_0 < ... < u_(M-1).
```

Both are increasing `M`-subsets of an `M+d` element universe, so

```text
i <= l_i <= u_i <= i+d.
```

Thus every selected upper rank-`r+1` witness has width at most `d`.

If a physical interval `[a,b]` has length at least `d+1`, then
`a <= M-1`, and the selected upper interval with index `a` satisfies

```text
[l_a,u_a] subset [a,a+d] subset [a,b].
```

An interval whose OR has rank `r` cannot contain this upper witness.  Hence
every selected lower rank-`r` witness has length at most `d`, or width at
most `d-1`.  There is no fixed-row or derivative assumption here.

## 3. Cumulative cross-layer nesting

Let `X_t=sum_(j<=t)x_j` and `Y_t=sum_(j<=t)y_j`.  Among the `X_t` upper
left endpoints, at most `d` are omitted by the lower left-endpoint set.  At
every shared left endpoint, the lower witness must end strictly before the
upper witness; otherwise it contains the latter.  Therefore an upper width
at most `t` injects into a lower width at most `t-1`, except for at most `d`
omitted endpoints:

```text
X_t <= d+Y_(t-1),  0 <= t <= d.
```

The same proof works at right endpoints.  Summing `t=1,...,d-1` gives

```text
sum X_t       = d*M-W_x-x0,
sum Y_(t-1)   = (d-1)*M-W_y,
```

and hence

```text
W_x-W_y >= M-d*(d-1)-x0.
```

The empty-sum boundary case `d=1` is also correct: lower widths are all zero,
`X_0<=1`, and the displayed separation reduces to `W_x>=M-x0`.

## 4. Omitted endpoints

Let `O_L,O_R` be the `d` positions omitted by the selected lower left and
right endpoint sets.  If `P` is the sum of all physical indices, then

```text
sum selected left  = P-sum(O_L),
sum selected right = P-sum(O_R).
```

Therefore the sign in the source is correct:

```text
W_y=sum(O_L)-sum(O_R).
```

If `[p,p]` is a selected upper witness, then the entry at `p` has rank
`r+1`.  No rank-`r` witness can begin or end at `p`, since it would contain
that entry.  Thus `p` lies in `O_L intersection O_R`.  The `x0` singleton
targets use distinct physical positions, so

```text
c=|O_L intersection O_R| >= x0.
```

After deleting the common points, the two residual omitted sets are disjoint
`q=d-c` subsets of `0,...,n-1`.  Their sum difference is at most the
difference between the top and bottom `q` positions:

```text
q*(n-q)=(d-c)*(M+c).
```

This extremum is attainable for fixed `c` when `M>=d`: there are enough
remaining positions to place the `c` common omissions.  Moreover

```text
f(c+1)-f(c)=d-M-2*c-1 < 0,
```

so `c>=x0` yields

```text
W_y <= (d-x0)*(M+x0).
```

There is no boundary-index error in this calculation.

## 5. Fan sharpening and its quantifiers

Every witness for a target of rank at most `r-1` avoids containing a complete
selected lower rank-`r` interval.  The independently audited fan theorem
therefore gives, for a distinct target family `F` of inclusion-chain height
at most `h`,

```text
|F| <= sum_j min(j,h)*y_j+h*d.
```

At a selected upper singleton position `p`, no such lower target can have a
witness ending at `p`: every interval ending there contains the rank-`r+1`
entry at `p`.  In the right-endpoint fan proof, this particular omitted
endpoint contributes zero, rather than the generic cap `h`.  The `x0`
positions are distinct, giving exactly the valid sharpening

```text
|F| <= sum_j min(j,h)*y_j+h*(d-x0).
```

This argument is unaffected by how witnesses for the other targets were
chosen.  It is also enough to use only the right-endpoint fan; no unjustified
simultaneous use of the left and right inequalities occurs.

For the rank-`r-1` antichain, `h=1` and

```text
C(2r+1,r-1)=M*r/(r+2),
```

so

```text
y0+x0 <= M+d-C(2r+1,r-1)=2*M/(r+2)+d.
```

For the complete nonempty lower ideal through rank `r-1`, the chain height
is exactly `r-1` and

```text
L=sum_(s=1)^(r-1)C(2r+1,s)=2^(2r)-1-M.
```

Thus

```text
W_y >= L-(r-1)*(d-x0).
```

When `d<=r`, every lower width is at most `d-1<=r-1`, so the capped width
sum equals `W_y`, as stated.

## 6. The `q_*` obstruction

Set `q=d-x0`.  Combining the lower fan bound with the omitted-endpoint upper
bound gives

```text
L <= q*(M+d+r-1-q).
```

The actual integer `q` is feasible in this inequality.  Therefore, if

```text
q_* = min{q in {0,...,d}: L<=q*(M+d+r-1-q)},
```

then `q>=q_*` and

```text
x0<=d-q_*.
```

Dropping the negative quadratic term correctly gives

```text
x0 <= d-ceil(L/(M+d+r-1)).
```

For the source's characterization of when this scalar inequality alone
forces `x0<=1`, put `g(q)=q*(M+d+r-1-q)`.  The discrete increment is

```text
g(q+1)-g(q)=M+d+r-2*q-2.
```

Under `d>=2` and `M+r>=d`, this is nonnegative throughout the needed range,
so the largest value with `q<=d-2` is

```text
g(d-2)=(d-2)*(M+r+1).
```

Consequently

```text
L>(d-2)*(M+r+1)
```

is exactly the condition for this one-dimensional obstruction to exclude
all `q<=d-2`.  The source correctly does not infer existence when it fails.

## 7. Independent finite arithmetic

The supplied checker has SHA-256

```text
5c4f7a2117b91dae15bc87e4c957e056b91f55687fbcef8a61e6f247994a1478
```

and compiles cleanly with

```text
g++ -O3 -std=c++20 -Wall -Wextra -pedantic
```

It recomputes every rank-slack value before taking the maximum.  Its exact
output is:

```text
k  r  M      B      d  L       q_*  x0 cap
7  3  35     37     2  28      1    1
9  4  126    128    2  129     1    1
11 5  462    465    3  561     2    1
13 6  1716   1719   3  2379    2    1
15 7  6435   6438   3  9948    2    1
17 8  24310  24313  3  41225   2    1
19 9  92378  92381  3  169765  2    1
```

I also checked the secondary columns directly from

```text
y0+x0 <= M+d-C(k,r-1),
W_y >= L-(r-1)*d+(r-1)*x0,
W_x-W_y >= M-d*(d-1)-1.
```

They reproduce, respectively,

```text
16,44,135,432,1433,4865,16799;
24,123,549,2364,9930,41204,169741;
32,123,455,1709,6428,24303,92371.
```

All constants and signs in the source table are correct.

## 8. Certified scope

The audited result applies to any hypothetical universal nonzero OR array of
length

```text
n=C(2r+1,r)+d
```

with `d>=1` and `M=C(2r+1,r)>=d`.  It is unrestricted: selected witnesses
may have all permitted monotone-band shapes, and the array entries may be
arbitrary masks.  One may substitute any proposed length, not only `B(k)`.

At `d=B(k)-M` for odd `7<=k<20`, it proves the globally valid array-level
restriction that the set of distinct rank-`r+1` masks occurring as literal
entries has cardinality at most one.  It does **not** bound how many times
that one mask may be repeated, characterize all feasible width profiles, or
prove existence/nonexistence at the unresolved dimensions.

