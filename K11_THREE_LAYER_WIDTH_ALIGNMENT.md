# Boundary-sensitive width alignment across ranks 5, 6, and 7

## 1. Scope and outcome

Assume hypothetically that a universal zero-free `k=11` word has length 465.
Choose one witness for every target in ranks five, six, and seven.  Use the
canonical rank-five/rank-six choice in which every literal central target is
represented by a singleton.

Write

```text
y_j = number of selected rank-five witnesses of width j,  0<=j<=2,
x_j = number of selected rank-six witnesses of width j,  0<=j<=3,
z_j = number of selected rank-seven witnesses of width j, 0<=j<=9.
```

Here width is physical length minus one.  The upper limits for ranks five and
six are the established rank-slack bounds.  The rank-seven upper limit nine
is the exact containment-blocker deadline

```text
465-(C(11,6)-C(7,6)) = 465-(462-7) = 10
```

on physical length.  Rank filtration also gives

```text
y_0<=134,  x_0<=1,  z_0=0.                       (1.1)
```

Define the full and four-truncated rank-seven width moments by

```text
W_7 := sum_(j=0)^9 j*z_j,
T_7 := sum_(j=0)^9 min(j,4)*z_j.
```

The proof below actually gives the stronger truncated consequence

```text
T_7>=930+3*x_0.                                   (1.2)
```

Using the already proved boundary-localized singleton cut in the Type-I
branch strengthens this to

```text
Type I  (x_0=1): T_7>=940.                        (1.3)
```

Type II has `x_0=0`, so (1.2) gives `T_7>=930`.  Since `W_7>=T_7`, the
previous full-width bounds remain valid, but the truncated form is strictly
more useful when generic exception witnesses are projected away.

Both 930 and 940 are attained by integer profiles satisfying the complete
current central scalar ledger and all boundary-sensitive inequalities below.
Thus there is no contradiction.  The useful output is a new rank-seven width
moment and an exact family of local three-layer compatibility cuts.

## 2. Exact omission parameters

For endpoint colour `epsilon in {L,R}`, let `E_r^epsilon` be the selected
endpoint set in rank `r`.  Its size is the size of that rank layer.  Define

```text
d_epsilon = |E_6^epsilon \ E_5^epsilon|,
e_epsilon = |E_7^epsilon \ E_6^epsilon|.
```

Since ranks five and six each use 462 endpoints among 465,

```text
0<=d_epsilon<=3.                                  (2.1)
```

Since the complement of `E_6^epsilon` has only three positions,

```text
0<=e_epsilon<=3.                                  (2.2)
```

Put

```text
q=min(d_L,d_R),  e=min(e_L,e_R).                  (2.3)
```

A selected rank-six singleton cannot share either endpoint with a rank-five
witness.  Consequently

```text
x_0<=q.                                           (2.4)
```

The endpoint set common to all three ranks has size at least

```text
330-d_epsilon-e_epsilon >=324.                    (2.5)
```

Indeed, among the 330 rank-seven endpoints, at most `e_epsilon` lie outside
the rank-six endpoint set, and at most `d_epsilon` further endpoints lie in
`E_6^epsilon\E_5^epsilon`.  This refines the bare inclusion-exclusion count
by recording where its six possible losses occur.

## 3. Exact cumulative width inequalities

Put

```text
X_t=sum_(j<=t)x_j,  Y_t=sum_(j<=t)y_j,
Z_t=sum_(j<=t)z_j,
```

with a cumulative sum equal to zero below index zero.

At one endpoint, all but `d_epsilon` selected rank-six intervals share that
endpoint with rank five.  Strict nesting then lowers width by at least one.
Therefore

```text
X_t <= d_epsilon+Y_(t-1).                         (3.1)
```

Likewise, rank seven versus rank six gives

```text
Z_t <= e_epsilon+X_(t-1).                         (3.2)
```

Both statements hold separately at the left and right ends.  In particular,

```text
x_0+x_1 <= y_0+q,
y_2       <= x_3+q,                               (3.3)
```

and

```text
Z_t <= e+X_(t-1).                                 (3.4)
```

Equation (3.1) is the boundary-resolved version of the existing central
cumulative nesting cut.  Equation (3.2) is its upper-layer analogue.  The
older adjacent-shadow theorem contains the corresponding endpoint geometry,
but its rank-seven width-profile projection was not previously recorded.

## 4. Named three-layer endpoint capacity

For one endpoint colour, define

```text
r_epsilon=|E_7^epsilon \ (E_5^epsilon intersect E_6^epsilon)|.
```

Then

```text
r_epsilon<=d_epsilon+e_epsilon.                   (4.1)
```

Let `H_t^epsilon` count physical endpoints common to ranks five and six at
which their selected widths satisfy

```text
w_5<=t-2 and w_6<=t-1.
```

Every rank-seven witness of width at most `t` whose endpoint is common to
both lower schedules must use one of those compatible central endpoint
states.  Endpoint injectivity gives the exact named-capacity inequality

```text
Z_t <= r_epsilon+H_t^epsilon.                     (4.2)
```

For the only nontrivial small thresholds:

```text
H_2 counts exactly the central state pair (w_5,w_6)=(0,1);

H_3 counts exactly (0,1), (0,2), and (1,2).
```

This is stronger as a named-position propagator than replacing `H_t` by a
profile total.  After forgetting endpoint identities, its scalar projection
is implied by composing (3.1) and (3.2).  It should therefore be regarded as
a local SAT cut, not as a new scalar lower bound.

## 5. Rank-seven truncated-width moment

The rank-five fan inequality already proves

```text
y_1+2y_2>=549+4x_0.
```

Using `y_0+y_1+y_2=462`, this is

```text
y_2>=y_0+87+4x_0.                                 (5.1)
```

Equations (3.3) and (5.1) give

```text
x_1<=y_0+q-x_0,
x_3>=y_0+87+4x_0-q.                               (5.2)
```

Since `z_0=0`, the four-term tail-sum identity and (3.4) give

```text
T_7 = sum_(t=0)^3 (330-Z_t)
    =1320-(Z_0+Z_1+Z_2+Z_3).                     (5.3)
```

where

```text
Z_0=0,
Z_1<=e+x_0,
Z_2<=e+x_0+x_1,
Z_3<=min(330,e+462-x_3).                          (5.4)
```

If `x_3<=132+e`, substitute `Z_3<=330` in (5.3).  The second inequality in
(5.2) then gives `y_0<=45+e+q-4x_0`, and the first inequality in (5.2)
finishes the estimate.  If `x_3>=132+e`, substitute the other branch of the
minimum in (5.4) and use (5.2) directly.  Both cases give the same exact
boundary-sensitive inequality

```text
boxed: T_7>=945-3e+3x_0-2q.                       (5.5)
```

Since `e,q<=3`, equation (1.2) follows.

## 6. Type-I strengthening

When `x_0=1`, the boundary-localized short-pool theorem already proves

```text
y_2>=x_1+96.                                      (6.1)
```

Combining (6.1) with `y_2<=x_3+q` gives

```text
x_3-x_1>=96-q.                                    (6.2)
```

Repeat the two cases in Section 5.  If `x_3<=132+e`, then
`x_1<=36+e+q`; if `x_3>=132+e`, use (6.2) directly.  Both yield

```text
boxed (Type I): T_7>=952-3e-q>=940.               (6.3)
```

## 7. Exact arithmetic feasibility

The worst boundary values are `e=q=3`.  The following Type-II profiles
attain (1.2):

```text
x=(0,54,273,135),
y=(51,273,138),
z=(0,3,54,273,0,0,0,0,0,0),
T_7=W_7=930.                                      (7.1)
```

The following Type-I profiles satisfy the stronger boundary-localized row
and the existing named-cell row `y_2>=96+y_0`, and attain (1.3):

```text
x=(1,42,284,135),
y=(40,284,138),
z=(0,4,42,284,0,0,0,0,0,0),
T_7=W_7=940.                                      (7.2)
```

They are abstract integer profiles, not interval-labelled OR words.  They
prove that the universal joint scalar ledger plus the new width hierarchy
remains feasible.  The Type-II profile may be placed in the permitted
one-low-component/no-duplicate subcase, for which the conditional
two-component/duplicate `y_2` rows do not apply.  The Type-I profile also
passes its branch-specific named-cell row.  The checker exhausts every
integer central profile under these applicable rows and reproduces the
parameterized minima (5.5) and (6.3).

## 8. SAT use

A direct implementation needs only the three width thresholds two, three,
and four.  Under the existing adjacent-shadow compression, count the active
crossed targets and give every inactive target the maximum truncated credit
four.  If `A_7` is the number of active targets and `T_7^active` their total
selected truncated width, the exact safe projection is

```text
T_7^active+4(330-A_7) >=930+3*x_0.                (8.1)
```

Equivalently, every crossed target contributes its unavoidable width-one
unit and three virtual threshold bits.  Force all three bits true when the
target is inactive.  If `D_7` counts false virtual bits, (8.1) becomes

```text
D_7<=390-3*x_0.                                   (8.2)
```

In Type I the stronger (1.3) gives `D_7<=380`; Type II gives `D_7<=390`.
This is the preferred guarded SAT cut.  It requires adjacent shadows and the
relevant rank-filtration branch, but no containment cap: truncation at four
already bounds the credit of every generic witness.  The former
nine-threshold full-width projection is valid but superseded.

The lower-overhead alternative is to encode the local implications (4.2)
for widths two and three using existing endpoint summaries.  Those clauses
are profile-redundant but can propagate before the large global width counter
is decided.

No inequality in this note changes `465<=nu(11)<=477`.
