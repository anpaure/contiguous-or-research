# Audit of `MATH_ATTACK_T_THREEBOX_SHELL_REPORT_RAW_20260724.md`

## 1. Verdict

The report contains three sound architecture-local theorems:

1. the reset-free literal triangular-shell word and its exact coverage;
2. a quadratic obstruction for every monotone-band order made of contiguous
   complete radius rings;
3. a quadratic obstruction for the stated fixed-coordinate raster order;
4. the ordered-occurrence factor of the literal shell cannot be compressed.

The first, third, and fourth results check with the displayed constants.  The
general ring obstruction is also correct; a direct run-cover proof below
actually improves its asymptotic constant from `2/21` to `2/15`.

Two material qualifications are required.

* The sharper “canonical ring cut” estimate

  ```text
  sum_i d_i <= 2a^3+2a^2+1+7aD
  ```

  is not proved or even attached to a precise definition of the canonical
  cut in the raw report.  Its claimed `1/5` consequence must be removed or
  supplied with an explicit index-to-run assignment and congestion audit.
* The five bullets under “Exact surviving gap” are design guidance, not all
  proved necessities.  Only the monotone-factor/shell-order disjunction and
  the need for literal lower-target witnesses follow directly.  Positive-
  proportion radius interleaving, avoidance of **every** bounded-component
  net, and long cross-radius corridors are unproved extrapolations.

The compact balanced three-box theorem and primitive-ray theorem remain open.
None of the quadratic lower bounds applies to unrestricted middle orders or
nonmonotone occurrence factorizations.

## 2. Definitions and inherited exact facts

The local invariant `g_3(p,q,r)` is the minimum length of a nonzero word of
box points whose nonempty contiguous coordinatewise maxima cover every
nonzero target.  The width is the largest rank coefficient.

For `[0,2a]^3`, the middle rank is `3a`, its size is

```text
M_a=3a^2+3a+1,
```

and the number of nonzero targets strictly below it is

```text
V_a=((2a+1)^3-M_a)/2-1
   =4a^3+(9/2)a^2+(3/2)a-1.                           (2.1)
```

If the selected middle witnesses, sorted by left endpoint, are

```text
I_i=[i+alpha_i,i+beta_i],
0<=alpha_i<=beta_i<=D,
```

then both offset sequences are nondecreasing.  Put
`d_i=beta_i-alpha_i`.  The audited rank-capped-start lemma is

```text
V_a <= sum_i d_i+(3a-1)D.                             (2.2)
```

This is unrestricted once the selected middle witnesses are fixed.  The
architectural restrictions enter only in the upper bounds on `sum_i d_i`.

For an internal positive threshold run `[u,v]`, coordinate factorability
implies

```text
r_(u-1)+2 <= ell_(v+1),
beta_(u-1)-alpha_(v+1) <= v-u.                        (2.3)
```

The raw wording “a pin for the run” should mean that the corridor must
contain at least one coordinate occurrence; it does not assert that one
common pin serves the whole run.  Only the necessary inequality (2.3) is
used.

## 3. Literal triangular-shell braid

### 3.1 Length

The first edge of `C_t` has `t+1` entries.  The second and third lists each
have `t` entries, so

```text
|C_t|=3t+1.
```

Replacing the four-entry `C_1` by `(B_1,C_1,A_1)` saves one position.  Hence,
for `R>=2`,

```text
|W_R|=sum_(t=1)^R(3t+1)-1
     =3R(R+1)/2+R-1.                                  (3.1)
```

### 3.2 Witness audit

Let `(x,y,z)` be nonzero and `t=max(x,y,z)`.

If `y=t`, the indicated interval follows the first edge into `B_t` and then
the second edge:

```text
(x,t-x,0), ..., B_t, ..., (0,t-z,z).
```

Its three maxima are exactly `(x,t,z)`.

If `y<t` and `z=t`, the interval

```text
(0,y,t-y), ..., C_t, ..., (x,0,t-x)
```

has maximum `(x,y,t)`.

In the remaining case, `x=t` and `y,z<t`.  For `t>=2`, the point

```text
(t-1-z,0,z)
```

is on the third edge of `C_(t-1)`, with the endpoint case `z=t-1` equal to
`C_(t-1)`.  Its suffix reaches terminal `A_(t-1)`, crosses the literal seam
to initial `A_t`, and stops at `(t-y,y,0)`.  The old suffix contributes
maximum `(t-1,0,z)`, the seam contributes `x=t`, and the new prefix
contributes `y`; the total is `(t,y,z)`.  This remains valid at `t=2` with
the shortened order `B_1,C_1,A_1`.

The two generic within-shell descriptions are not literally in the modified
`C_1` order for every max-one target, so `t=1` must be treated as the stated
special check.  The shortened block covers

```text
010, 001, 100, 011, 101, 111,
```

while `110` occurs literally on the first edge of `C_2`.  Thus all nonzero
targets are covered for `R>=2`, proving (3.1) as an upper bound for
`g_3(R,R,R)`.

### 3.3 Width comparison

For `R=2s`, inclusion-exclusion at rank `3s` gives

```text
w_R=C(3s+2,2)-3C(s+1,2)=3s^2+3s+1.
```

For `R=2s+1`, the middle rank is `3s+1` and

```text
w_R=C(3s+3,2)-3C(s+1,2)=3(s+1)^2.
```

Substitution in (3.1) gives exactly

```text
|W_R|=2w_R-floor(R/2)-3.
```

Therefore the braid is genuinely reset-free and literal, but its leading
constant is two times width.

## 4. General contiguous-ring obstruction

### 4.1 Internal extreme runs

Translate the middle layer to

```text
H_a={(x,y,z):x+y+z=0, |x|,|y|,|z|<=a}.
```

On the radius-`r` ring, each of

```text
x=r, y=r, z=r
```

is a positive threshold support of `r+1` consecutive vertices.  These three
positive sides are disjoint.  For `r>=2`, one linearization cut can spoil at
most one of them: consecutive positive sides are separated by a negative
side having an interior vertex.  Hence at least two are internal.  At
`r=1`, at least one survives; that bounded ring can simply be left
unassigned below.

This is slightly stronger and more precise than the raw statement “at least
one survives.”  Two surviving runs are what make a simple complete charging
argument possible.

### 4.2 Explicit heterogeneous assignment

For every `r>=2`, choose two surviving internal positive sides.  Assign each
of the `6r` indices on that ring to the first side unless it lies in that
side, in which case assign it to the second.  The assigned run never contains
the index.  Every assigned run has

```text
lambda=v-u=r,
```

and its one-sided span from the assigned index is at most the ring-block
length `6r<=6a`.  Leave the six radius-one indices and the center unassigned.

For completeness, the heterogeneous run-cover calculation is as follows.
If `i<u`, (2.3) and monotonicity give

```text
d_i <= lambda+alpha_(v+1)-alpha_i.
```

If `i>v`, the symmetric bound is

```text
d_i <= lambda+beta_i-beta_(u-1).
```

Expanding into adjacent offset increments, a fixed alpha or beta increment
is charged at most `6a` times.  The total variation of each offset sequence
is at most `D`; each of the seven unassigned widths is at most `D`.  Therefore

```text
sum_i d_i
 <= sum_(r=2)^a 6r^2+(12a+7)D
 = 2a^3+3a^2+a-6+(12a+7)D.                           (4.1)
```

For `a>=2`, (4.1) is stronger than the raw bound

```text
sum_i d_i
 <=2a^3+6a^2+4a+1+18aD.                              (4.2)
```

Indeed the constant-term difference is `3a^2+3a+7`, and the `D`
coefficient difference is `6a-7`, both positive.  At `a=1`, (4.2) is
trivial from `sum_i d_i<=M_aD`.  Thus the raw general inequality is valid,
although the sentence “selecting one run per ring” does not by itself
describe a complete assignment; the two-run assignment above repairs the
proof.

This argument depends only on each complete ring being one contiguous block.
Its orientation, cut, and position among the other complete ring blocks are
irrelevant because all assigned spans remain inside the same block.

### 4.3 Lower bound on excess

Combining raw inequality (4.2) with (2.2) gives

```text
D >= [2a^3-(3/2)a^2-(5/2)a-2]/(21a-1),
```

so the displayed `(2/21+o(1))a^2` conclusion is arithmetically correct.

The stronger certified ledger (4.1) gives

```text
V_a
 <=2a^3+3a^2+a-6+(15a+6)D,
```

and hence

```text
D >= [2a^3+(3/2)a^2+(1/2)a+5]/(15a+6)
   = (2/15+o(1))a^2.                                  (4.3)
```

Thus the general contiguous-ring architecture is ruled out even somewhat
more strongly than claimed.

### 4.4 Uncertified canonical-cut claim

The raw report next states

```text
sum_i d_i<=2a^3+2a^2+1+7aD
```

for “the canonical ring cut.”  It provides neither:

* a definition of that cut and orientation convention;
* the internal threshold run assigned to each middle index;
* the exact sum of the assigned run lengths; nor
* the alpha/beta congestion calculation giving `7a`.

No earlier audited file contains this exact formula.  Consequently the
`(1/5+o(1))a^2` conclusion is an unproved gate, not an audited theorem.  It
may be true, but it must not be cited until the missing certificate is
written down and checked.

### 4.5 Architectural scope

Equations (4.2)--(4.3) apply when the order induced by the selected middle
witnesses consists of complete contiguous radius rings.  They allow
arbitrary ring cuts, orientations, and even permutations of the complete
ring blocks.  They do not apply after genuine cross-radius arc interleaving,
nor to a proposed shell factor whose occurrence intervals are not globally
ordered by both endpoints.

## 5. Fixed-coordinate raster obstruction

### 5.1 Short endpoint components

Order the centered middle hexagon by increasing `x`; each fixed-`x` row is
contiguous and monotone in `y`, with arbitrary orientation.  Let `e_x` be
the unique maximum-`y` point of row `x`.

Use the threshold `y>=y(e_x)`.  Inside row `x`, only `e_x` meets this
threshold.  In an adjacent row the maximum `y` changes by at most one, so a
component crossing the row seam contains at most two points of that adjacent
row.  Since the high-`y` segment touches only one end of a nontrivial row,
the component cannot continue through two row seams.  Thus the maximal
positive component containing `e_x` has at most three ordered targets and
`lambda<=2`.

If this run is `[u,v]`, with `e=e_x in [u,v]`, the pin inequality gives

```text
d_e
 <= lambda+(beta_e-beta_(u-1))
            +(alpha_(v+1)-alpha_e).                  (5.1)
```

At the two global boundaries use the harmless conventions `beta_0=0` and
`alpha_(M_a+1)=D`; the extended total variations remain at most `D`.
Each endpoint run has length at most three, so each adjacent alpha or beta
increment is charged by at most three endpoints.  With `2a+1` rows,

```text
sum_x d_(e_x) <=2(2a+1)+6D.                           (5.2)
```

This supplies the proof omitted from the raw report.

### 5.2 Extending endpoint control to all indices

The number of targets in two consecutive rows is at most `4a+2`, so
consecutive selected row endpoints are at index distance at most

```text
H=4a+2.
```

Assign every middle index to a neighboring selected endpoint.  Each endpoint
is used at most `H` times.  For `i<e`,

```text
d_i<=d_e+alpha_e-alpha_i,
```

and for `i>e`,

```text
d_i<=d_e+beta_i-beta_e.
```

The two variation charges have congestion at most `H`, and hence contribute
at most `2HD`.  Using (5.2),

```text
sum_i d_i
 <=H(4a+2+6D)+2HD
 =(4a+2)(4a+2+8D).                                   (5.3)
```

Combining (5.3) with (2.2) gives exactly

```text
D >= [V_a-(4a+2)^2]/(35a+15)
   = (4/35+o(1))a^2.                                  (5.4)
```

Both the denominator and leading constant in the raw report are correct.

### 5.3 Balanced unequal boxes

The uniform extension is valid once “natural raster” is defined in the same
way at a middle rank of `[0,p]x[0,q]x[0,r]`.  If
`delta R<=p,q,r<=CR`, then:

* there are `Theta_(delta,C)(R)` rows;
* every row and every gap between consecutive maximum-coordinate endpoints
  has length `O_C(R)`;
* the row maximum changes by at most one, so the endpoint threshold component
  still has bounded size;
* the number of nonzero targets below the middle is `Theta_(delta,C)(R^3)`,
  while the middle rank and its width are `Theta(R)` and `O(R^2)` in the
  relevant factors.

Repeating (5.1)--(5.3) gives

```text
sum_i d_i=O_C(R^2+RD),
```

and the rank-capped-start lemma gives

```text
D=Omega_(delta,C)(R^2).
```

Thus the asymptotic extension is sound under this explicit fixed-coordinate,
contiguous-monotone-row definition.  It is not a statement about arbitrary
rasters, row interleavings, or nonmonotone within-row orders.

## 6. Ordered factor compression of the shell word

Let `T_1,...,T_L` be the virtual occurrences of `W_R`, and suppose

```text
J_i=[a_i,b_i],
```

represents `T_i`, with both endpoint sequences nondecreasing.  If
`b_(i+1)=b_i`, then `a_i<=a_(i+1)` implies

```text
J_(i+1) subseteq J_i,
T_(i+1)<=T_i.                                         (6.1)
```

Every adjacency inside a shell joins two distinct rank-`t` points, hence
incomparable points.  Every shell seam is

```text
A_t<A_(t+1),
```

which also contradicts the reverse comparison in (6.1).  The modified
`B_1,C_1,A_1` block has the same adjacent-incomparability property.  Thus

```text
b_1<b_2<...<b_L,
```

and a physical word needs `n>=L=|W_R|` positions.

Taking the physical word itself to be `W_R` and `J_i=[i,i]` attains equality.
Therefore the optimum among globally ordered occurrence representations—and
hence among globally ordered linked factors—is exactly `|W_R|`.

This is an architecture-local result.  It assumes every virtual occurrence,
including repeated shell endpoints, receives an interval in the original
order.  It does not rule out:

* a different literal braid;
* deletion or rebundling of virtual occurrences with a new coverage proof;
* intervals whose endpoint orders cross; or
* a physical construction not obtained by factoring `W_R`.

For a factor proof that transfers all virtual interval witnesses, adjacent
`J_i` must additionally have connected union.  Singleton certificates do,
and the lower bound above does not need this extra linkage hypothesis.

## 7. Scope audit of the final claims

The exact theorem ledger is:

* `W_R` is an unconditional literal upper construction of length
  `(2-o(1))w_R`.
* Complete contiguous radius-ring middle orders require
  `D=Omega(a^2)`; (4.3) gives a certified leading constant `2/15`.
* The stated fixed-coordinate raster orders require `D=Omega(a^2)`; in the
  cube the certified constant is `4/35`.
* A globally ordered occurrence factor of this particular shell word cannot
  shorten it.

The following raw-report bullets are not exact consequences:

* “interleave radii on a positive proportion of the surface” requires a
  stability theorem for orders in which only some rings are broken;
* “avoid every `O(R)`-spaced net of bounded threshold components” requires a
  quantified heterogeneous run-cover hypothesis and congestion bound;
* “use long cross-radius coordinate corridors” is a plausible design
  response, not a proved necessity.

What is proved is narrower: a successful construction must leave the two
audited ring/raster architectures, and a compression of `W_R` must abandon
its globally ordered factor structure or change the virtual shell order.
Any proposed replacement must still prove literal coverage of lower targets;
meet/upper-shadow coverage alone is insufficient.

Accordingly, the primitive-ray statement

```text
g_3(at,bt,ct)=w(at,bt,ct)+o(t^2)
```

remains entirely open, including the cubic ray.  Nothing here changes the
global all-dimensional bound without an additional unrestricted three-box
theorem.
