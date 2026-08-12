# Audit of central transfer-line factorization

## Verdict

**PASS after two explicit repairs.**

The two-coordinate transfer criterion, its linked-line construction, the
fixed-delay factorization, the half-depth corollary, and the exact triangular
criterion are correct.  They give a genuine local reduction of the four-box
portal problem.  They do not supply the still-required global superposition
of the different line foliations, so no asymptotic upper constant changes.

The submitted proof needs these corrections:

1. The line point has weight `|y|-delta=2m`, not
   `|y|-2delta=2m`.  The displayed definition of the point is correct; only
   that proof sentence has the extra subtraction.
2. In the `H(y)=empty` composition chart, the box constraints must be kept:

   ```text
   max(1,delta-m) <= z_i <= delta.
   ```

   Positivity alone is sufficient only when `delta<=m`.  For `delta>m`, the
   lower bound enforces `y_i<=m`, and the upper bound enforces `y_i>=0`.

## 1. Exact transfer criterion

Let `y in [0,m]^4` have weight `2m+delta`.  Hold the two coordinates outside
`{i,j}` fixed at their target values.  The remaining coordinate sum at every
middle point is

```text
y_i+y_j-delta.
```

Attaining `y_i` therefore requires the other coordinate to equal
`y_j-delta`, and conversely.  Thus a transfer line exists exactly when

```text
y_i>=delta and y_j>=delta.
```

When this holds, the points

```text
T_t = y-delta*e_i-t*e_j+t*e_i,  0<=t<=delta,
```

all have weight `|y|-delta=2m`, lie in the box, and are bounded above by
`y`.  Their join is `y`, while their meet is

```text
y-delta*e_i-delta*e_j.
```

Successive points differ by `e_i-e_j`, so this is an adjacent middle-level
line.

## 2. Exact local factor

Represent a box coordinate by the corresponding prefix of a coordinate
chain of atoms.  Along `T_0,...,T_delta`, each atom occurs in exactly one of
four patterns: all windows, a boundary prefix, a boundary suffix, or no
window.  These patterns admit an explicit delay-`delta` factor on positions
`0,...,2delta`:

- put a full-support atom at position `delta`;
- put an atom supported on windows `0,...,b` at position `b`;
- put an atom supported on windows `a,...,delta` at position `a+delta`.

The length-`delta+1` sliding unions reproduce the line exactly.  This is also
the direct finite proof of local pin survival; no abstract interval labeling
is being assumed.

## 3. Half-depth and triangular forms

If `2delta<=m` and fewer than two coordinates of `y` were at least `delta`,
then

```text
|y| < m+3delta <= 2m+delta,
```

a contradiction.  Hence every target through depth `m/2` has some transfer
line.

For

```text
Y(c;u,r,x)=(c+r,m-c,x,m-u),
delta=r+x-u,
```

coordinate three is always below `delta`.  The other three coordinates meet
the transfer threshold precisely under

```text
A: x<=c+u,
B: r+x<=m,
C: r+x-u<=m-c.
```

Therefore a two-provider line exists exactly when at least two of `A,B,C`
hold.  The residual jointly thick family is exactly the set on which at
least two fail.

## 4. Corrected thick-cone chart

Put `H(y)={i:y_i>=delta}`.  Transfer failure is equivalent to
`|H(y)|<=1`, and can occur only beyond half depth.

If `H(y)={i}`, set

```text
a=m-y_i,
z_j=delta-y_j  (j!=i).
```

Then

```text
0<=a<=m-delta,
z_j>=1,
a+sum_(j!=i) z_j=2delta-m.
```

These conditions already force all remaining coordinate bounds because this
case has `delta<=m`.

If `H(y)=empty`, set `z_i=delta-y_i`.  The exact chart is

```text
sum_i z_i=3delta-2m,
max(1,delta-m)<=z_i<=delta.
```

The additional bounds are essential when `delta>m`.

## 5. Remaining gate

For a fixed transfer pair, maximal transfer lines partition the middle
level, and all targets admissible to that pair occur as intervals on those
lines.  The unresolved theorem is simultaneous physical superposition of
the relevant foliations, plus a subcubic braid for the corrected thick cone.
Separate concatenation repeats a positive fraction of the middle level and
does not imply a leading constant of one.

Thus this package removes the *local* factor and pin obstruction for every
line-admissible target, but leaves the global ordering/reset cost intact.

## 6. Exhaustive regression

The independent checker

```text
scratch/audit_central_transfer_lines.py
```

enumerates all upper targets through `m=10`, checks every coordinate-pair
criterion, joins, meets, explicit delay factors, the half-depth result, the
triangular criterion, and both corrected thick-cone charts.  It reports

```text
PASS upper_targets=21449 triangular_targets=3289 m<=10
```

Its SHA-256 is

```text
e54e7bd2eaf06eb85842f74c46f3d80fff3a75b2cada605277f1316f855d33f2.
```
