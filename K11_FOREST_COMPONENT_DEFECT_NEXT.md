# Exact component-defect refinements for unrestricted `k=11,n=465`

## Status and outcome

This note continues the unrestricted selected-witness analysis.  It assumes
neither a fixed derivative row nor a connected central path.

The new proved consequences are:

1. the two endpoint defects `uL,uR` separately strengthen every cumulative
   width cut; branching on their exact values removes between two and six
   percent of the surviving scalar profiles unless both equal three;
2. the already materialized endpoint-alignment counts sharpen adaptively from
   `324,24` to `327-u,27-u` in a colour with defect `u`;
3. at least `192-c` rank-five targets, where `c=uL+uR`, lie in a full
   rank-four/rank-five/rank-six two-sided diamond;
4. every component is monotone in both central witness orders, and every
   two-edge shadow is local: its two same-rank indices differ by at most six;
5. the minimal component cases are rigid.  In particular, in the literal
   singleton branch `e=1,c=2`, the singleton is isolated and the other 923
   central vertices form one alternating Hamilton path.  If the ordered
   rank-five masks are `S0,...,S461` and the singleton rank-six mask is `U0`,
   then

   ```text
   U(i+1) = S(i) union S(i+1),  0<=i<=460.
   ```

6. in the `e=1` branch, deleting the boundary singleton reduces the generic
   rank-three and rank-four shadow exception budgets from six to four.

An explicit endpoint schedule survives **all** present scalar and endpoint
cuts with `e=1,c=2`.  Thus the new rigidity does not by itself eliminate the
literal-singleton branch; mask incidence is essential.

The independent arithmetic and endpoint checker is

```text
scratch/enumerate_k11_component_defect_profiles.cpp
```

No solver or principal handoff is edited by this note.

## 1. Notation

Choose one witness interval for every rank-five and every rank-six mask.  Let

```text
mL = number of common selected left endpoints,
mR = number of common selected right endpoints,
uL = 462-mL,
uR = 462-mR,
c  = uL+uR.
```

The two common-endpoint relations are matchings.  Their union is the inherited
spanning linear forest on the 924 central masks, and `c` is exactly its number
of components.  Therefore

\[
 0\le u_L,u_R\le3,\qquad1\le c\le6.             \tag{1.1}
\]

Write

```text
x_j = selected rank-six witnesses of width j, 0<=j<=3,
y_j = selected rank-five witnesses of width j, 0<=j<=2.
```

As before, width is physical length minus one.  Put

\[
 X_t=\sum_{j=0}^t x_j,
 \qquad Y_t=\sum_{j=0}^t y_j.                    \tag{1.2}
\]

## 2. The exact coloured defect cuts

### Theorem 1

For each endpoint colour `q in {L,R}`, with defect `u_q`,

\[
 \boxed{X_t-Y_{t-1}\le u_q}\qquad(0\le t\le2), \tag{2.1}
\]

where `Y_{-1}=0`.  Equivalently, with

\[
 u_*:=\min(u_L,u_R),
\]

\[
 \boxed{x_0\le u_*},                             \tag{2.2}
\]

\[
 \boxed{x_0+x_1-y_0\le u_*},                    \tag{2.3}
\]

\[
 \boxed{y_2-x_3\le u_*}.                        \tag{2.4}
\]

#### Proof

Fix one endpoint colour.  Every matched rank-six interval of width at most
`t` is paired, at the common endpoint, with a proper rank-five subinterval.
Its lower width is therefore at most `t-1`.  At most `u_q` of the `X_t`
rank-six intervals are unmatched in this colour, while the endpoint matching
is injective.  Hence `X_t-u_q<=Y_(t-1)`, proving (2.1).  Taking both colours
gives (2.2)--(2.4).  The final form uses both layer totals 462.  \(\square\)

Summing only the two colours gives the earlier rows

\[
 2(X_t-Y_{t-1})\le c.                            \tag{2.5}
\]

The coloured version is strictly stronger whenever `uL!=uR`.  After
projecting away the exact endpoint defects, `u_*=3` remains possible and the
new rows collapse to the already encoded worst-case cuts.  Their value is in
a small exact-defect portfolio, not as one more unbranched scalar row.

### A weighted matching inequality

For completeness, let

\[
 \mu_6(u)=\sum_{s=1}^3
   \left(u-\sum_{j=0}^{s-1}x_j\right)_+,          \tag{2.6}
\]

the minimum total width of `u` unmatched rank-six vertices, and

\[
 \mu_5(u)=\min(u,y_1+y_2)+\min(u,y_2),           \tag{2.7}
\]

the maximum total width of `u` unmatched rank-five vertices.  The matching
in a colour of defect `u` has `462-u` edges, and each matched upper interval
has width at least one larger than its lower mate.  Consequently

\[
 \boxed{W_6-W_5\ge462-u+\mu_6(u)-\mu_5(u)}.      \tag{2.8}
\]

In the current audited profile region `y2>=87` and `u<=3`, so
`mu5(u)=2u`.  Exhaustive arithmetic checking found that (2.8) removes no
profile beyond (2.1) and the existing rows.  It is a useful regression
identity, but it should not receive a separate SAT circuit.

## 3. Defect-sensitive endpoint alignment

Let `C_L` be the set of physical positions common to the selected rank-five
and rank-six left endpoints.  It has size

\[
 |C_L|=m_L=462-u_L.                              \tag{3.1}
\]

The selected rank-four left endpoint set has size 330.  Therefore

\[
 |L_4\cap C_L|
 \ge330+(462-u_L)-465
 =327-u_L.                                       \tag{3.2}
\]

At each such endpoint the rank-four, rank-five, and rank-six intervals are
strictly nested.  Hence the rank-five width is at least one and the rank-six
width at least two.  Thus the already defined left alignment count satisfies

\[
 \boxed{Z^L_{324}\ge327-u_L}.                    \tag{3.3}
\]

The right-hand dual is

\[
 \boxed{Z^R_{324}\ge327-u_R}.                    \tag{3.4}
\]

Adding the 165 rank-three endpoints gives

\[
 |L_3\cap L_4\cap C_L|
 \ge165+330+(462-u_L)-2\cdot465
 =27-u_L.                                        \tag{3.5}
\]

The four widths are then forced to be `0,1,2,3`, so

\[
 \boxed{Z^L_{24}\ge27-u_L},
 \qquad
 \boxed{Z^R_{24}\ge27-u_R}.                     \tag{3.6}
\]

Equations (3.3)--(3.6) recover the old constants `324,24` only at the maximum
defect `u=3`.  If exact common-endpoint counters are available, the compact
forms are

```text
mL <= ZL324+135,       mR <= ZR324+135,
mL <= ZL24 +435,       mR <= ZR24 +435.
```

### Corollary 2: full rank-four diamonds

Identify every alignment position with its unique selected rank-five target.
Let `A_L,A_R` be the rank-five target sets counted in (3.3)--(3.4).  Then

\[
 |A_L\cap A_R|
 \ge(327-u_L)+(327-u_R)-462
 =192-c.                                         \tag{3.7}
\]

For every target `S` in this intersection there are distinct rank-four masks
`K_L,K_R` and distinct rank-six masks `U_L,U_R` with

\[
 \boxed{S=K_L\cup K_R=U_L\cap U_R}.             \tag{3.8}
\]

The two lower masks are distinct because one selected rank-four interval
cannot share both endpoints with the different-valued rank-five interval;
the upper masks are distinct by the no-double-colour central forest theorem.
Containment and the adjacent ranks then force (3.8).

Similarly, at least `27-c` of the four-rank chains aligned on either one side
also have the opposite central neighbour, and at least `327-c` of the
three-rank alignments on either side have both central neighbours.  These
replace the coarse constants 21 and 321 by exact component-sensitive forms.

## 4. Ordered-component theorem

Order the selected rank-five intervals by left endpoint as

\[
 P_0,P_1,\ldots,P_{461},
\]

and the selected rank-six intervals similarly as

\[
 Q_0,Q_1,\ldots,Q_{461}.
\]

Equal-rank noncontainment implies that both right-endpoint orders are the
same as these left-endpoint orders.

### Theorem 3: components are monotone and six-local

Every component of the central forest can be oriented so that its rank-five
indices and its rank-six indices both increase strictly along the component.
Moreover, whenever two same-rank vertices are distance two in a component,
their ordered indices differ by at most six.

#### Proof

Suppose

```text
P_i --L-- Q_j --R-- P_i'.
```

The first equality is at the left endpoint and the second at the right.  The
rank-six interval properly contains both rank-five intervals, so

\[
 \ell(P_i)=\ell(Q_j)<\ell(P_{i'}),
 \qquad
 r(P_i)<r(Q_j)=r(P_{i'}).                        \tag{4.1}
\]

Thus `i<i'`.  The dual two-edge step

```text
Q_j --R-- P_i --L-- Q_j'
```

gives `j<j'`.  Since colours alternate in a component, one orientation makes
all such steps forward.

For either central family, its `i`th left and right endpoints lie between
`i` and `i+3`, because 462 distinct endpoints occupy 465 positions.  An
equal-endpoint edge therefore joins central order indices differing by at
most three.  A two-edge step differs by at most six.  \(\square\)

### Corollary 4: local exact shadows

At least `462-c` targets in each central rank have degree two.  By Theorem 3,
each such rank-six target is the union of two selected rank-five targets whose
order indices differ by at most six, and each such rank-five target is the
intersection of two rank-six targets whose indices differ by at most six.

This is stronger than the previous unqualified meet/join count: it confines
every forced shadow to a constant-width band in the two target orders.

The theorem also shows that the central forest is not an arbitrary
six-component middle-level forest.  It is a cover by at most six monotone,
six-local alternating paths.

## 5. Exact minimal-component cases

### Component-type bookkeeping

Let `a5` be the number of components having one more rank-five than rank-six
vertex and `a6` the reverse number.  Equality of the two layer sizes forces

\[
 a_5=a_6=:a.                                     \tag{5.1}
\]

Let `dL` be the number of balanced components whose two endpoint deficiencies
are both colour `L`, and define `dR` dually.  Every imbalanced component has
one missing incidence of each colour.  Hence

\[
 u_L=a+d_L,qquad u_R=a+d_R,qquad
 c=2a+d_L+d_R.                                   \tag{5.2}
\]

An isolated rank-six singleton is an upper-heavy component, so in the
literal branch

\[
 e=1\Longrightarrow a\ge1,\qquad u_L,u_R\ge1,\qquad c\ge2. \tag{5.3}
\]

### The case `c=1`

Here `e=0` and the forest is one alternating Hamilton path through all 924
central masks.  By Theorem 3 its same-layer subsequences must be exactly the
two complete witness orders.  Therefore

```text
the 461 unions of consecutive ordered rank-five masks
are distinct and equal all but one rank-six mask;

the 461 intersections of consecutive ordered rank-six masks
are distinct and equal all but one rank-five mask.
```

Thus `c=1` is already a two-sided rainbow Johnson-path ansatz, although it was
derived from the unrestricted forest rather than assumed.

It also has a finite width-profile law.  One endpoint colour is a perfect
order-preserving matching, hence pairs `P_i` with `Q_i`.  After contracting
those perfect edges, the other order-preserving matching has 461 edges and
must connect all 462 contracted vertices.  Its single omission pair is
therefore at opposite ends and it is the unit shift.  Up to reversing the
word,

\[
 Q_i=[\ell(P_i),r(P_{i+1})]\quad(0\le i\le460), \tag{5.3a}
\]

while `Q461` is a proper same-left extension of `P461`.

The 462 rank-five right endpoints occupy 462 of 465 positions, so the total
gap excess in (5.3a) is at most three.  Choose the boundary width
`b=width(P461)` and write `z_j=y_j-1_(b=j)`.  The last proper extension has
width

\[
 b+1+e,\qquad0\le e\le2-b.                     \tag{5.3b}
\]

For the other 461 intervals there are nonnegative `a01,a02,a12` with

\[
 a_{01}+2a_{02}+a_{12}\le3                      \tag{5.3c}
\]

such that

\[
\begin{aligned}
 x_1&=z_0-a_{01}-a_{02}+1_{b+1+e=1},\\
 x_2&=z_1+a_{01}-a_{12}+1_{b+1+e=2},\\
 x_3&=z_2+a_{02}+a_{12}+1_{b+1+e=3}.
\end{aligned}                                    \tag{5.3d}
\]

In particular,

\[
 462\le W_6-W_5\le467.                          \tag{5.3e}
\]

The full promotion relation reduces the `e=0,c=1` joint profile count from
271,663,750 to **609,086**, retaining the same 32,755 upper profiles.

### The literal case `e=1,c=2`

The selected rank-six singleton has degree zero, hence is one component.  It
already contributes both units of rank-six degree deficiency.  There is only
one other component, containing all 462 rank-five vertices and all 461
remaining rank-six vertices.  It is an alternating Hamilton path with its two
endpoints in rank five.

In the anchored orientation the singleton is `Q0`.  The monotonicity theorem
forces the remaining path to have the exact order

\[
 P_0,Q_1,P_1,Q_2,\ldots,Q_{461},P_{461}.         \tag{5.4}
\]

Consequently, for `0<=i<=460`,

\[
 \boxed{\operatorname{mask}(Q_{i+1})
 =\operatorname{mask}(P_i)\cup\operatorname{mask}(P_{i+1})}, \tag{5.5}
\]

and for `1<=i<=460`,

\[
 \boxed{\operatorname{mask}(P_i)
 =\operatorname{mask}(Q_i)\cap\operatorname{mask}(Q_{i+1})}. \tag{5.6}
\]

Physically,

\[
 Q_{i+1}=[\ell(P_i),r(P_{i+1})].                 \tag{5.7}
\]

Write `p_i=width(P_i)` and `q_j=width(Q_j)`.  Equation (5.7) gives the two
exact formulas

\[
 q_{i+1}=p_i+\bigl(r(P_{i+1})-r(P_i)\bigr)
          =p_{i+1}+\bigl(\ell(P_{i+1})-\ell(P_i)\bigr). \tag{5.8}
\]

After deleting the boundary singleton, the 462 rank-five left endpoints and
the 462 right endpoints each occupy 462 positions inside a 464-position
word.  Thus, separately on the left and right,

\[
 \sum_{i=0}^{460}
 \bigl(\operatorname{gap}_i-1\bigr)\le2.         \tag{5.9}
\]

This yields a sharp two-ended profile law.  Remove the width of `P461` from
`(y0,y1,y2)`.  Shift the three bins up by one, and permit at most two total
units of further upward promotion.  The result must be `(x1,x2,x3)`.  The
same statement must hold after removing the width of `P0`.

More explicitly, for each end there are a boundary width `b in {0,1,2}` and
nonnegative integers `a01,a02,a12` such that

\[
 a_{01}+2a_{02}+a_{12}\le2,                     \tag{5.10}
\]

and, writing `z_j=y_j-1_(b=j)`,

\[
\begin{aligned}
 x_1&=z_0-a_{01}-a_{02},\\
 x_2&=z_1+a_{01}-a_{12},\\
 x_3&=z_2+a_{02}+a_{12}.
\end{aligned}                                    \tag{5.11}
\]

There must be one representation for the first endpoint and another for the
last endpoint; if their boundary widths are equal, the corresponding `y`
bin must contain at least two intervals.  Immediate scalar consequences are

\[
 x_1\le y_0\le x_1+3,                            \tag{5.12}
\]

\[
 x_3-2\le y_2\le x_3+1,                         \tag{5.13}
\]

and

\[
 459\le W_6-W_5\le463.                          \tag{5.14}
\]

The complete finite relation (5.10)--(5.11), not merely these three
projections, reduces the surviving `e=1,uL=uR=1` joint profiles from
260,613,875 to **372,855** while retaining 31,455 upper profiles.

Thus this branch is exactly a Hamilton ordering of all rank-five masks whose
461 adjacent union colours are all rank-six masks except the literal
singleton mask.  This is a much smaller exact search object than the original
array formula.  It remains only one defect branch; it cannot replace the
unrestricted search.

## 6. Extra branch-one compression below the centre

This section uses the already audited boundary localization of the literal
rank-six singleton.  Delete that boundary entry.  The remaining word has
length 464 and still represents every mask of ranks one through five.  The
462 selected rank-five witnesses now have slack two, so every rank-one through
rank-four mask has a witness of length at most two.

There is also a direct improvement to the compressed shadow exception counts.
For rank `s in {3,4}`, let `R=\binom{11}{s}`.  Its selected endpoint set and the
rank-five endpoint set live in 464 positions and have sizes `R` and 462.
They therefore share at least `R-2` endpoints in each colour.  At least

\[
 (R-2)+(R-2)-R=R-4                             \tag{6.1}
\]

rank-`s` targets are crossed on both sides.  Hence, specifically in branch
`e=1`,

```text
rank three: at least 161/165 crossed, at most four generic exceptions;
rank four:  at least 326/330 crossed, at most four generic exceptions.
```

The existing unbranched reductions use six generic slots in each layer.  A
branch-specialized build may safely use four, and every direct or generic
rank-at-most-four witness may be capped at physical length two.

## 7. Exhaustive arithmetic projection

The checker enumerates all integer profiles surviving the complete audited
joint system **including** the two singleton refinements

```text
x3>=93+2*x0,
y2>=x1+82+14*x0.
```

The baseline counts are

| branch | upper profiles | joint profiles |
|---:|---:|---:|
| `e=0` | 33,454 | 290,393,090 |
| `e=1` | 31,918 | 272,277,079 |

Adding the exact coloured-defect rows gives the following table.  Only
`uL<=uR` is printed because the scalar rows are symmetric under exchanging
the colours.

| `e` | `(uL,uR)` | `c` | upper profiles | joint profiles |
|---:|---:|---:|---:|---:|
|0|(0,1),(0,2),(0,3)|1,2,3|32,755|271,663,750|
|0|(1,1),(1,2),(1,3)|2,3,4|33,118|277,874,634|
|0|(2,2),(2,3)|4,5|33,351|284,118,058|
|0|(3,3)|6|33,454|290,393,090|
|1|(1,1),(1,2),(1,3)|2,3,4|31,455|260,613,875|
|1|(2,2),(2,3)|4,5|31,687|266,445,484|
|1|(3,3)|6|31,918|272,277,079|

For the minimal literal branch, the two-ended promotion law gives the further
row.  The corresponding `e=0,c=1` promotion law is included for comparison.

| `e` | `(uL,uR)` | extra structure | upper profiles | joint profiles |
|---:|---:|---|---:|---:|
|0|(0,1)|one-ended law (5.3b)--(5.3d)|32,755|609,086|
|1|(1,1)|two-ended law (5.10)--(5.11)|31,455|372,855|

The weighted inequality (2.8) produces exactly the same counts after the
cumulative rows.  Thus the proposed useful portfolio cut is (2.1), not
(2.8).

For `e=0`, reversal remains available and one may impose `uL<=uR` WLOG.  In
the anchored `e=1` branch reversal would move the forced entry from the left
boundary to the right boundary, so a solver retaining `A[0]=63` must keep
both ordered defect pairs.  The table may still merge them because its scalar
counts are identical.

## 8. Sharp endpoint counterexample in the singleton branch

No endpoint/profile argument can strengthen (5.3) to `c>=3`.  Define the
rank-five selected intervals `P_i`, `0<=i<=461`, by

\[
 P_i=\begin{cases}
 [i+1,i+2],&0\le i\le365,\\
 [i+1,i+3],&366\le i\le461,
 \end{cases}                                     \tag{8.1}
\]

and define the rank-six selected intervals by

\[
 Q_0=[0,0],
 \qquad
 Q_j=[\ell(P_{j-1}),r(P_j)]\quad(1\le j\le461). \tag{8.2}
\]

Their profiles are

\[
 x=(1,0,365,96),qquad y=(0,366,96).             \tag{8.3}
\]

Both endpoint colours have 461 matches, so

\[
 u_L=u_R=1,qquad c=2.                           \tag{8.4}
\]

The singleton `Q0` is isolated and the other intervals form exactly the path
(5.4).  Every common endpoint is strictly nested.  The four current endpoint
alignment populations are

```text
ZL324=461, ZR324=461, ZL24=95, ZR24=96.
```

The profile satisfies every audited fan, short-pool, cumulative, total-width,
singleton, and component-defect inequality.

The schedule can even be labelled consistently on **both central layers**.
The middle-levels graph on the rank-five and rank-six subsets of `[11]` has a
Hamilton cycle.  Delete the chosen rank-six vertex `C=63` from such a cycle
and orient the remaining alternating Hamilton path.  Label `P_0,...,P_461`
and `Q_1,...,Q_461` in its path order and label `Q_0` by `C`.  Every physical
forest edge in (8.1)--(8.2) is then an actual inclusion edge, and (5.5)--(5.6)
hold for the labels.

This still is not an OR-array candidate: no array entries have been found
whose interval ORs equal all these labelled witnesses, and no lower/upper
noncentral ranks have been represented.  It is, however, an adversarial
certificate that scalar counts, endpoint geometry, **and the complete central
mask incidence problem together** neither eliminate `e=1` nor force `c>=3`.

Likewise the previously recorded schedules

```text
P_i=[i,i+2], Q_i=[i,i+3]
```

show that endpoint geometry permits `e=0,c=1`.

## 9. Encoding priorities

The following additions are globally safe and compact once exact endpoint
defects are counted:

1. branch on `uL,uR in {0,1,2,3}` and add (2.1);
2. add the adaptive alignment inequalities (3.3)--(3.6);
3. in branch `e=1`, reduce both lower shadow exception pools from six to four
   and cap every rank-at-most-four generic witness at length two;
4. give the minimal branches `c=1` and `e=1,c=2` specialized central
   encodings using Section 5 rather than the generic forest formula.

If a generic rather than specialized `e=1,c=2` build is retained, the cheap
projections (5.12)--(5.14) should be added immediately.  The full profile law
has only seven promotion types and three boundary-width choices per end, so a
small guarded table or selector circuit can encode it exactly.

The `c=1` law is similarly tiny: there are three possible boundary widths,
at most three endpoint-extension choices, and only finitely many promotion
triples of weighted sum at most three.

The local six-band shadow theorem in Corollary 4 is mathematically stronger
than the existing raw forest statement.  Encoding it by deriving one central
layer from the other is promising, but it needs a separately audited
all-different target circuit; it is not just a scalar clause.

The `192-c` diamond theorem similarly needs target-indexed left/right
alignment flags.  The present position-only population counters cannot by
themselves assert the mask identities (3.8).

## 10. Theorem/conjecture ledger

| statement | status |
|---|---|
| exact coloured cuts (2.1)--(2.4) | proved |
| weighted row (2.8) | proved; arithmetic-redundant in current system |
| adaptive endpoint counts (3.3)--(3.6) | proved |
| at least `192-c` full diamonds | proved |
| monotone, six-local component theorem | proved |
| exact `c=1` two-sided rainbow reduction | proved |
| `c=1` promotion law (5.3a)--(5.3e) | proved |
| exact `e=1,c=2` Hamilton reduction | proved |
| two-ended promotion law (5.10)--(5.14) | proved |
| branch-one four-exception reductions | proved |
| `e=1` impossible | **not proved**; endpoint counterexample survives |
| `c>=3` in branch one | false at endpoint/profile level; no mask theorem known |
| central-layer mask labelling of (8.1)--(8.2) | proved from middle-levels Hamiltonicity |
| realization of that labelled skeleton by one OR array | not proved |

These results do not settle satisfiability of the length-465 formula.  They
replace one coarse six-component search by a finite defect portfolio and
identify two sharply smaller exact central subproblems.
