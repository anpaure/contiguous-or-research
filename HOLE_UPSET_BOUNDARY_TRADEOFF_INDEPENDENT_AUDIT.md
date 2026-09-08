# Independent audit: upward high-hole boundary tradeoff

## Verdict

**PASS**, subject only to the explicit scope conventions listed below.  I
found no reversed inequality, missing edge class, or counterexample.  The
high-hole upset improves the degree-four deletion estimate to the claimed
interpolating bound

\[
e_{\rm sel}\ge \max\{E-2\sigma-2h,0\},
\]

and the resulting moment and projection inequalities are valid.  The
`k=11` and `q369` arithmetic also checks exactly.  This is a genuine stronger
necessary condition, but it yields no new exact value through `k=19`.

Audited files and SHA-256 values:

```text
0b89fafa1da4e03504b45ff9b2deeceab3a3ddbacd3051a23dc9b272bfa3df8b  HOLE_UPSET_BOUNDARY_TRADEOFF.md
ce081423fd0de7c20dea06a3491b03629928292f460b9dfa139e0fe16d2d1a0d  check_hole_upset_moments.cpp
c0fb74ec7d908f2eae4a253ec5ed7372e0a1db06123289f20d28470688cb86b6  HOLE_UPSET_NUMERICAL_CHECK_K19.txt
```

## Scope conventions that should be stated explicitly

The theorem uses the same hypotheses as the previously audited
boundary-moment theorem:

1. `d>=1`;
2. the array is the zero-free word for `nu(k)` (the nonempty-entry
   assumption is needed only for the `2r-3` rhombus refinement);
3. one distinct short witness has been selected for every nonempty mask of
   rank below `r`;
4. `binom(x,q)=0` when `q>x` or `q<0`;
5. the minimization in (6), as implemented, is over the integers
   `h in {0,...,sigma}`.

The first three follow automatically in the intended equality-length setup.
Writing them in Section 1 would make the result self-contained.  If the
minimum in (6) were read as a real minimum, the displayed condition would
remain necessary but would be slightly weaker than the checker.

## 1. High holes really are an upset

Let `I` be an unselected short cell with `|U(I)|>=r`, and let `J` be a short
superinterval.  Monotonicity of union gives `|U(J)|>=r`.  A selected cell is
one of the chosen witnesses for a target of rank below `r`, so `J` cannot be
selected.  Hence `J` is another high hole.  This proves the full physical
upset assertion; it is not merely monotonicity of the hole labels.

No uniqueness assumption beyond selecting one witness per lower target is
missing: different target masks necessarily select different physical cells,
because one cell has only one OR value.

## 2. Audit of the incident-edge count

Orient every cover edge toward its one-position extension.  An edge is
incident with the high upset if and only if its upper endpoint is high:

- if the upper endpoint is high this is immediate;
- if only the lower endpoint is known high, upward closure makes the upper
  endpoint high as well.

Every edge has a unique upper endpoint, and a short interval has at most two
immediate subintervals.  Therefore all edges incident with high holes number
at most

\[
2|H_\ge|=2(\sigma-h).
\]

After deleting those edges, every remaining hole-incident edge touches a low
hole.  The interval-band cover graph has maximum degree four, so their union
has size at most `4h`.  Double counting among low holes only makes this upper
bound looser.  Thus at most

\[
2(\sigma-h)+4h=2\sigma+2h
\]

edges are removed.  Subtracting from

\[
E=(d-1)(2n-d)
\]

and truncating at zero proves (1).  In particular, no high-to-high edge or
low-to-high edge is omitted from the charge: both are charged to their high
upper endpoint.

## 3. Audit of the hole moment and selected-edge gradient

A low hole has rank at most `r-1`, so it avoids at least `k-r+1`
coordinates.  It contributes at least

\[
\binom{k-r+1}{q}
\]

to `H_q`; high holes contribute nonnegatively.  This proves (2), including
all large-`q` cases under the zero-binomial convention.

For a selected cover edge `I proper-subset J`, the selected labels are
distinct lower masks and satisfy `U(I) proper-subset U(J)`.  If their ranks
are `s<t`, then `s<=r-2` and `t<=r-1`.  Its gradient is

\[
\binom{k-s}{q}-\binom{k-t}{q}
=\sum_{u=s}^{t-1}\binom{k-u-1}{q-1}
\ge \binom{k-r+1}{q-1}.
\]

Multiplying this minimum by the selected-edge lower bound proves (4).  The
direction is correct: more selected edges force a larger lower bound on
`G_q`.

## 4. Weighted inequality, projection, and minimization

Substitution into the previously audited identity

\[
dZ_q\ge R_q+H_q+\frac d4G_q
\]

gives (5) with no loss of sign.  Projection to a fixed `q`-set deletes
exactly the positions disjoint from it and leaves a universal zero-free word
on that `q`-set after empty projections are removed.  Therefore

\[
Z_q\le \binom{k}{q}(n-\nu(q))
     \le \binom{k}{q}(n-B(q)).
\]

Combining this upper bound on the left side with the lower bound (5), then
minimizing over the unknown integer `h`, proves (6).  Minimizing over every
integer in `[0,sigma]` is safe even though not every value need be geometrically
realizable: enlarging the feasible set only weakens the necessary condition.

The new scalar expression dominates the old one pointwise in `h`, because

\[
\max(E-2\sigma-2h,0)\ge\max(E-4\sigma,0)
\]

for `h<=sigma`, and the low-hole moment is nonnegative.  “Strict
strengthening” should be understood structurally or for instances such as
`k=11`; equality can occur in degenerate parameters (`d=1`, zero gradients,
and similar cases).

## 5. Rhombus rank ceilings

For outer, side, and inner intervals in one band rhombus,

\[
|U(O)|+|U(I)|\le |U(L)|+|U(R)|
\]

has the stated direction.  If `O` is a minimal high hole, both side ORs have
rank at most `r-1`.  Hence `|U(O)|<=2r-2` for a length-two outer interval.
For outer length at least three, the inner interval is nonempty; in the
zero-free word its OR has rank at least one, giving `|U(O)|<=2r-3`.

The limitation in the note is real.  Minimal singleton high holes have no
nonempty inner interval and can generate large upward cones, so these ceilings
cannot be converted into an unconditional positive hole moment without an
additional location/zero-run argument.

## 6. Independent `k=11` arithmetic

For `k=11,r=6,n=465,d=3`, direct recomputation gives

```text
M     = 462
L     = 1023
sigma = 3*462 + binom(4,2) - 1023 = 369
E     = 2*(930-3) = 1854
E-2*sigma = 1116
R_1   = 11*(C(10,1)+...+C(10,5)) = 7007
```

Thus

\[
3Z_1\ge7007+6h+\frac34(1116-2h)
       =7844+\frac92h.
\]

The integer minimum is at `h=0`.  The projection cap is

\[
3\binom{11}{1}(465-B(1))=15312,
\]

so the unscaled margin is `7468`.

In the exact `q369` saturation branch, the 369 holes are the prescribed
rank-six triples.  They are top-row high holes, so the edge count `1116` is
in fact exact, and

\[
H_q=369\binom5q.
\]

At `q=1` the right side is

\[
7007+369\cdot5+\frac34\,1116=9689,
\]

leaving margin `5623`, exactly as stated.

## 7. Checker audit

I compiled the checker independently under C++20 and reproduced every data
row in `HOLE_UPSET_NUMERICAL_CHECK_K19.txt`; only the report's prose/header
format differs from the executable's raw output.  The final result is

```text
checked_through=19 violations=0
```

I also independently enumerated **every** integer `h=0,...,sigma` for every
`q` and every maximizing rank through `k=19`.  The minimum objective value
always matched the checker's reduced candidate set:

```text
full_h_audit_through_19 mismatches=0
```

The endpoint/breakpoint reduction is valid because the objective is affine
on either side of `E-2*sigma-2h=0`.  The use of `__int128` for the multiplied
inequality is safe, while all `long long` intermediate values are easily in
range for the documented scope `k<20`.

One presentational point is worth retaining: the table's globally smallest
`k=11` margin occurs at `q=10` (`margin4=27808`), whereas the prose separately
discusses `q=1` to expose the nonzero edge-gradient improvement
(`margin4=29872`).  These statements are consistent.

## Final assessment

The theorem is correct and useful as an unrestricted lower-bound
strengthening.  Its novelty is the coupling

\[
\text{high-hole upset geometry}
\quad\longleftrightarrow\quad
\text{edge deletion}
\quad\longleftrightarrow\quad
\text{low-hole avoidance moment}.
\]

The averaged scalar projection is nevertheless far from contradiction at
`k=11`; resolving the exact problem still requires retaining hole locations,
the unsummed `Q`-indexed run constraints, or stronger pin/endpoint coupling.

## Addendum: audit of the rhombus/cone refinement (9)--(13)

**PASS.**  The later cone refinement is also mathematically valid.  It was
added after the first audit pass, so the details are recorded separately
here.

### Cone capacities

An interior singleton position lies in at most

\[
1+2+\cdots+d=\binom{d+1}{2}=C_1
\]

short intervals.  A fixed nonsingleton interval of length `ell>=2` has at
most

\[
\sum_{t=0}^{d-\ell}(t+1)
=\binom{d-\ell+2}{2}
\le\binom d2=C_2
\]

short superintervals.  Boundary truncation only reduces these numbers.
Every high hole lies above a minimal high hole in the finite containment
poset.  The union of the minimal-hole cones has size `sigma-h`; bounding a
union by the sum of its cone sizes therefore gives

\[
C_1x+C_2m\ge\sigma-h.
\]

Cone overlaps make this inequality weaker, never invalid.

### The `+2x` edge correction

All high-incident edges are still counted by the indegrees of their high
upper endpoints.  A nonsingleton upper interval has at most two immediate
subintervals, whereas a singleton upper endpoint has none.  Hence the
high-edge deletion charge improves from `2(sigma-h)` to

\[
2(\sigma-h-x).
\]

Adding at most `4h` remaining low-hole incidences yields

\[
e_{\rm sel}\ge
\max\{E-2(\sigma-h-x)-4h,0\}
=\max\{E-2\sigma-2h+2x,0\},
\]

so the sign and coefficient of `+2x` in (10) are correct.

### Minimal nonsingleton moment

The rhombus ceiling gives rank at most `2r-2` for a minimal length-two high
hole and at most `2r-3` at greater length.  Therefore every minimal
nonsingleton high hole avoids at least

\[
c=\max\{k-2r+2,0\}
\]

coordinates and contributes at least `binom(c,q)` to `H_q`.  These `m`
holes are distinct from the `h` low holes, so

\[
H_q\ge h\binom{k-r+1}{q}+m\binom cq
\]

without double counting.  Using the weaker length-two ceiling uniformly is
deliberate and safe.

Every actual triple `(h,x,m)` satisfies (13), so minimizing (12) over the
displayed integer relaxation is valid.  The natural additional constraint

```text
x + m <= sigma - h
```

is also true because the minimal high holes are themselves distinct high
holes.  Its omission does **not** invalidate the theorem: it only enlarges
the minimization domain and may weaken the numerical lower bound.  Adding it
would be a harmless potential sharpening.

The sentence about central ranks should read “at the **upper** middle rank in
odd dimension, `c=1`, and at the middle rank in even dimension, `c=2`.”  At
the lower of the two equal middle ranks in odd dimension, `c=3`.  This is a
wording correction, not a theorem defect.

### Independent `k=11,q=1` optimization

Here

```text
sigma=369, E=1854, d=3, C1=6, C2=3, c=1.
```

After multiplication by four, (12) becomes

\[
24h+4m+3\max\{1116-2h+2x,0\},
\]

subject to `6x+3m>=369-h`.  Exhaustive enumeration of all integer `h` and
`x`, with the least admissible `m`, gives the unique optimum

```text
h=0, x=61, m=1,
selected edges = 1116 + 2*61 = 1238,
extra4 = 3718,
extra = 929.5.
```

This also follows from the positive-region expression

\[
3348+18h+6x+4m:
\]

`x` supplies six units of cone capacity at cost six, while `m` supplies
three at cost four; thus `h=0`, 61 singleton cones cover 366 holes, and one
nonsingleton cone covers the remaining three.  Taking 62 singleton cones
costs `930`, slightly more.  Therefore

\[
3Z_1\ge7007+929.5=7936.5
\]

and the projection slack is indeed `15312-7936.5=7375.5`.

### Checker limitation

`check_hole_upset_moments.cpp` currently implements only the earlier
two-variable tradeoff (6).  It does **not** enumerate `(h,x,m)` or reproduce
the cone-refined `929.5` value.  Section 8 accurately says that it evaluates
(6), so this is not a false claim, but the cone result lacks a dedicated
checked implementation.  The independent exhaustive calculation above
certifies the stated `k=11` minimizer.  A future reproducibility update should
either add a second checker or extend the existing one while retaining both
reported bounds.
