# Second-order endpoint consequences for unrestricted `k=11,n=465`

## Status and outcome

This note uses only the globally unrestricted selected-witness geometry.  It
does **not** assume a fixed derivative row, a Johnson path, or a connected
central forest.

The strongest new consequences are:

1. if the two central endpoint matchings leave a total defect `c`, then all
   but at most `c` masks in **each** central rank are exact two-sided shadows;
2. the endpoint defect strengthens the existing cumulative width inequalities
   from an additive `3` to the exact additive `c/2` form;
3. at least 186 selected rank-five intervals are simultaneously aligned with
   ranks four and six at both ends;
4. if a selected rank-six witness is a singleton, then the rank-six
   width-three count satisfies the strengthened profile cut

   \[
      \boxed{x_3\ge 93+2x_0};
   \]

5. the monotone schedules contain nontrivial contiguous blocks on which the
   exact two-sided shadow identities hold.

Items 1--3 and 5 are mostly propagation structure.  After forgetting the
actual endpoint alignments, the scalar part of item 2 projects to inequalities
already in the joint band ledger.  Item 4 is a strictly stronger scalar
profile cut than the previously encoded `x3>=93`.  It was independently
derived in the parallel general odd-dimensional ledger
`ODD_SHORT_POOL_SINGLETON_REFINEMENT.md`; Section 6 specializes that theorem
to the present endpoint analysis.

No solver or principal handoff is changed by this note.

## 1. Notation and the exact forest defect

Choose one interval for every rank-five and every rank-six target.  Let

```text
mL = number of common selected left endpoints,
mR = number of common selected right endpoints,
uL = 462-mL,
uR = 462-mR.
```

Both endpoint sets have size 462 inside 465 positions, so

\[
 459\le m_L,m_R\le462,
 \qquad 0\le u_L,u_R\le3.                         \tag{1}
\]

Join a rank-five vertex to a rank-six vertex by an `L` edge when their
selected intervals have the same left endpoint, and by an `R` edge when they
have the same right endpoint.  The inherited endpoint theorem says that each
colour is a matching, no pair gets both colours, and their union is a spanning
linear forest on 924 vertices.

Define

\[
 c:=u_L+u_R=924-m_L-m_R.                          \tag{2}
\]

Because a forest with 924 vertices and `mL+mR` edges has
`924-mL-mR` components, `c` is **exactly** its number of components.  Hence

\[
 1\le c\le6.                                      \tag{3}
\]

The lower bound `c>=1` is worth recording: `c=0` would make every vertex have
one edge of each colour, producing alternating cycles, contrary to the forest
theorem.

Each colour contributes the same number of incidences on the two rank
classes.  Therefore

\[
 \sum_{v\in {11\choose5}}(2-\deg v)
 =\sum_{v\in {11\choose6}}(2-\deg v)=c.          \tag{4}
\]

In particular, in each central rank at least

\[
 462-c\ge456                                      \tag{5}
\]

vertices have degree two.  Unlike the coarse bound 456, equation (5) reacts
to the actual endpoint omissions in a partial SAT assignment.

## 2. Exact meet and join shadows

### Lemma 1: rank-five meet identity

Let a selected rank-five interval have both an `L` neighbour and an `R`
neighbour.  If its mask is `S` and the two rank-six masks are `U,V`, then

\[
 S=U\cap V.                                       \tag{6}
\]

**Proof.**  Endpoint nesting gives `S subset U` and `S subset V`.  The two
neighbours are distinct vertices: otherwise the same pair would receive both
endpoint colours.  Each of `U,V` is a six-set containing the five-set `S`, so
they add two different elements to `S`.  Their intersection is exactly `S`.
\(\square\)

### Lemma 2: rank-six join identity

Let a selected rank-six interval have both endpoint neighbours.  If its mask
is `U` and the rank-five masks are `S,T`, then

\[
 U=S\cup T.                                       \tag{7}
\]

The proof is dual: `S,T` are distinct five-subsets of the same six-set.

Combining (4), (6), and (7) gives the exact unrestricted statement

```text
all but at most c rank-five targets are meets of their two forest neighbours;
all but at most c rank-six  targets are joins of their two forest neighbours.
```

This is stronger than merely saying that 456 vertices are internal: the
exception budget is the same exact component count `c` on both layers.

### Width-specific physical forms

Write width as right endpoint minus left endpoint.

* A degree-two rank-five width-two interval `[l,l+2]` has the forced
  rank-six neighbours

  \[
     [l,l+3]\quad\hbox{and}\quad[l-1,l+2].        \tag{8}
  \]

* A degree-two rank-six width-one interval `[l,l+1]` has the forced
  rank-five neighbours

  \[
     [l,l]\quad\hbox{and}\quad[l+1,l+1].         \tag{9}
  \]

These follow from strict endpoint nesting and the width caps two and three.
They expose exact local subblocks without introducing a fixed global row.

## 3. Coupled width-defect inequalities

Let

```text
x_j = number of selected rank-six witnesses of width j, 0<=j<=3,
y_j = number of selected rank-five witnesses of width j, 0<=j<=2.
```

For `t in {0,1,2}`, every forest neighbour of a rank-six interval of width at
most `t` is a rank-five interval of width at most `t-1`.  The rank-six
vertices in the former set have total degree at least

\[
 2\sum_{j=0}^{t}x_j-c,
\]

while the latter rank-five vertices have total degree at most

\[
 2\sum_{j=0}^{t-1}y_j.
\]

Thus

\[
 \boxed{
  2\left(\sum_{j=0}^{t}x_j-
          \sum_{j=0}^{t-1}y_j\right)\le c
 }
 \qquad(t=0,1,2).                                 \tag{10}
\]

Explicitly,

\[
 2x_0\le c,                                       \tag{11}
\]

\[
 2(x_0+x_1-y_0)\le c,                            \tag{12}
\]

\[
 2(y_2-x_3)\le c.                                \tag{13}
\]

The last form uses both layer totals 462.  Equation (11) also has a direct
interpretation: a rank-six width-zero interval has no possible strictly
shorter rank-five neighbour, so it is isolated and consumes two units of the
component deficiency.

Substituting only the worst-case `c<=6` into (10) recovers the existing
profile cuts

\[
 x_0\le3,
 \quad x_0+x_1\le y_0+3,
 \quad y_2\le x_3+3.                              \tag{14}
\]

Consequently (10) is **profile-redundant** after projecting away `mL,mR`.
It is nevertheless propagation-useful: as soon as either endpoint matching
has fewer omissions, `c` drops and all three inequalities tighten together.

### Degree-two counts by width

At most `c` vertices of either layer can have degree below two.  Therefore

\[
 \#\{\hbox{degree-two rank-five width-}j\}
 \ge (y_j-c)_+.                                   \tag{15}
\]

Every rank-six singleton consumes deficiency two.  Among positive-width
rank-six vertices the remaining deficiency is at most `c-2x0`, so

\[
 \#\{\hbox{degree-two rank-six width-}j\}
 \ge\bigl(x_j-(c-2x_0)\bigr)_+
 \qquad(j=1,2,3).                                 \tag{16}
\]

Equations (15)--(16), together with (8)--(9), are useful local propagation
statements even though their scalar projections add little.

## 4. Two-sided consequences of the multi-rank endpoint cuts

The inherited endpoint-alignment theorem gives, separately at the left and
right ends:

```text
at least 324 common rank-4/rank-5/rank-6 endpoints;
at least  24 common rank-3/rank-4/rank-5/rank-6 endpoints.
```

Endpoint injectivity identifies each such position with a unique selected
rank-five vertex.

### Proposition 3: at least 186 full rank-four diamonds

Let `A_L` and `A_R` be the rank-five vertices occurring in the two 324-sets.
Both are subsets of a 462-element rank-five layer, hence

\[
 |A_L\cap A_R|\ge324+324-462=186.                 \tag{17}
\]

For each vertex in this intersection, let `K_L,K_R` be the selected rank-four
masks sharing its left and right endpoints and let `U_L,U_R` be the analogous
rank-six masks.  If the rank-five mask is `S`, then

\[
 S=K_L\cup K_R=U_L\cap U_R.                      \tag{18}
\]

Indeed, the two lower neighbours are distinct four-subsets of `S`, and the
two upper neighbours are distinct six-supersets of `S`.  Thus at least 186
rank-five targets sit in an exact two-sided Boolean diamond.

This theorem is globally valid, but the current `ZL324/ZR324` summaries do
not name the actual rank-four witnesses.  Adding (18) to a solver therefore
requires links to the rank-four witness/shadow variables; it cannot be
obtained merely by conjoining the existing central summary bits.

### Proposition 4: one-sided four-rank chains become two-sided centrally

Among the at least 24 rank-five vertices in the **left** four-rank alignment
set, at most `uR` lack a right forest edge.  Hence at least

\[
 24-u_R=21+(m_R-459)                              \tag{19}
\]

have the physical pattern

\[
 [l,l]_{r=3}\subset[l,l+1]_{r=4}
 \subset[l,l+2]_{r=5}\subset[l,l+3]_{r=6},       \tag{20}
\]

together with the opposite rank-six neighbour `[l-1,l+2]`.  Dually, at
least

\[
 24-u_L=21+(m_L-459)                              \tag{21}
\]

right four-rank chains also have their opposite central neighbour.

Similarly, at least

\[
 324-u_R=321+(m_R-459)                            \tag{22}
\]

left rank-4/5/6 alignments have both central endpoint neighbours, and the
right-to-left dual lower bound is `321+(mL-459)`.

These are second-order alignment statements: they combine a lower-rank
endpoint intersection in one colour with the omission defect of the other
colour.

## 5. Forced contiguous two-sided subblocks

The monotone-band schedules make some of the degree statements spatial.

For rank five, width two occurs only in states `02` and `13`.  Each state is a
contiguous schedule block, so all width-two positions occupy at most two
blocks.  Removing the at most `c` vertices that fail degree two splits those
blocks into at most `c+2` degree-two runs.  Hence there is a contiguous run of
at least

\[
 \left\lceil\frac{y_2-c}{c+2}\right\rceil        \tag{23}
\]

degree-two rank-five width-two vertices.  The inherited fan cut gives
`y2>=87`; with `c<=6`, (23) is at least 11.  Every position of this run has
the forced meet geometry (8).

For rank six, width three is the single state `03`, hence it occupies one
contiguous block.  After the `2x0` deficiency consumed by isolated
singletons, at most `c-2x0` positive-width vertices fail degree two.  There is
therefore a contiguous degree-two width-three run of length at least

\[
 \left\lceil
  \frac{x_3-(c-2x_0)}{c-2x_0+1}
 \right\rceil.                                    \tag{24}
\]

Using `x3>=93` and `c<=6`, this is at least 13.  Section 6 strengthens the
numerator when `x0=1`.

These blocks are not new scalar profile cuts.  They are useful if the solver
materializes degree-two flags and propagates the exact meet/join equations
locally.

## 6. Singleton exclusion and a new pure profile cut

Suppose a selected rank-six witness is the singleton interval `[p,p]`, with
mask `U`.  Every other interval containing `p` has OR containing `U`.
Therefore it cannot witness a target of rank at most five, nor a different
rank-six target.  Since the selected rank-six family uses `[p,p]` for `U`, no
other selected interval in the target families counted below can contain
`p`.

The already proved `x0<=1` lets `x0` serve as the indicator for this case.

### Length at most two

The short-pool theorem supplies 549 distinct witnesses of ranks one through
four of length at most two.  Add the selected central intervals counted by
`y0+y1+x0+x1`.  There are 929 physical intervals of lengths one and two.

If `x0=1`, even when `p` is a boundary position there is at least one other
length-two interval containing `p`, and that slot is unavailable to all the
counted targets.  Hence

\[
 \boxed{x_0+x_1+y_0+y_1\le380-x_0}.              \tag{25}
\]

This strengthens the existing right side 380 in the singleton branch, but it
is numerically implied by the current fan and nesting cuts.  It is best kept
as a regression theorem or a local exclusion propagator.

### Length at most three

Every mask of ranks one through four has a witness of length at most three:
an interval of length at least four contains a selected rank-five witness and
therefore has rank at least five.  This accounts for

\[
 \sum_{s=1}^{4}{11\choose s}=561
\]

distinct intervals.  All 462 selected rank-five intervals also have length at
most three.  Finally, exactly `x0+x1+x2` selected rank-six intervals have
length at most three.  The physical pool has

\[
 465+464+463=1392
\]

slots.

If `x0=1`, a boundary singleton still lies in at least one additional interval
of length two and one additional interval of length three.  Both are
unavailable to every counted target.  Thus

\[
 561+462+(x_0+x_1+x_2)\le1392-2x_0,
\]

or equivalently

\[
 \boxed{x_0+x_1+x_2\le369-2x_0},                 \tag{26}
\]

\[
 \boxed{x_3\ge93+2x_0}.                          \tag{27}
\]

This cut is genuinely stronger than the earlier encoded scalar ledger.  (It
agrees with the independently derived general theorem in
`ODD_SHORT_POOL_SINGLETON_REFINEMENT.md`.)  For
example, the integer profile

```text
x = (1,0,367,94)
y = (0,371,91)
```

satisfies the previously proved fan, joint-short-pool, cumulative nesting,
and total-width inequalities, but violates (27).  This is only a profile
counterexample, not a realizable schedule; it is sufficient to prove that
(27) is not an arithmetic consequence of those earlier rows.

More generally, a singleton at a physical boundary excludes at least one
additional interval of each length `2,...,h`.  The cases `h=2,3` are the ones
that currently yield useful certified profile statements.

### Boundary localization gives a stronger joint short-pool cut

The preceding argument used only the weakest fact that a singleton may lie at
a physical boundary.  In the audited monotone rank-six band, it in fact **must**
lie there.

The cut `x3>=93` forces state `03` to occur.  A width-zero state comparable
with `03` in the coordinatewise state order can only be `00` or `33`.
Consequently, if `x0=1`, its unique occurrence is either the first schedule
slot in state `00`, giving `[0,0]`, or the last schedule slot in state `33`,
giving `[464,464]`.

Delete this boundary entry.  Every witness of rank at most five avoids it,
because any interval containing the entry has rank at least six.  Thus the
remaining contiguous word of length 464 still contains witnesses for all
masks of ranks one through five.

There are 462 selected rank-five witnesses in those 464 positions.  Their
endpoint slack is now two.  Hence every interval of length at least three in
the reduced word contains a selected rank-five witness, and every target of
ranks one through four has a witness of length at most two.  These lower
targets consume

\[
 \sum_{s=1}^{4}{11\choose s}=561
\]

distinct slots from the reduced length-at-most-two pool.  Add the `y0+y1`
selected rank-five short intervals and the `x1` non-singleton rank-six
length-two intervals.  The reduced word has

\[
 464+463=927
\]

singleton-or-pair slots, so in the `x0=1` branch

\[
 561+y_0+y_1+x_1\le927.
\]

Combining this branch with the already proved `x0=0` joint-pool row gives the
single valid inequality

\[
 \boxed{x_0+x_1+y_0+y_1\le380-13x_0},            \tag{28}
\]

or, equivalently,

\[
 \boxed{y_2\ge x_1+82+14x_0}.                    \tag{29}
\]

For `x0=1`, this says `y2>=x1+96`.  It is strictly stronger than (25) and is
the best new scalar consequence found in this pass.  It still does not
eliminate the singleton branch.

### Exact enumeration against the audited joint profile system

The checker

```text
scratch/enumerate_k11_second_order_profiles.cpp
```

enumerates every integer composition

```text
x0+x1+x2+x3 = 462,
y0+y1+y2    = 462
```

against the complete previously audited joint scalar rows: the rank-six fan
and width cuts, `x0<=1`, both refined rank-five fan cuts, both cumulative
nesting cuts, the joint short pool, and total-width separation 455.  It then
adds (27), followed by (28).  Counts are split by the exact value of `x0`.

| scalar system | `x0` | surviving `x` profiles | surviving `(x,y)` profiles |
|---|---:|---:|---:|
| previously audited joint system | 0 | 33,454 | 290,393,090 |
| previously audited joint system | 1 | 32,852 | 273,169,120 |
| plus `x3>=93+2*x0` | 0 | 33,454 | 290,393,090 |
| plus `x3>=93+2*x0` | 1 | 32,835 | 273,168,882 |
| plus boundary cut (28) | 0 | 33,454 | 290,393,090 |
| plus boundary cut (28) | 1 | 31,918 | 272,277,079 |

Thus (27) removes only 17 upper profiles and 238 joint profiles.  The sharper
boundary reduction removes a further 917 upper profiles and 891,803 joint
profiles, but more than 272 million integer profiles remain in the
`x0=1` branch.  The branch-sensitive all-odd width inequality

\[
 W_6-W_5\ge456-x_0
\]

removes no additional profile after the rows above; the checker verifies this
as a separate final stage.

Compile and run with GNU C++ using

```text
/opt/homebrew/bin/g++-15 -O3 -std=c++20 -Wall -Wextra -pedantic \
  scratch/enumerate_k11_second_order_profiles.cpp \
  -o /tmp/enumerate_k11_second_order_profiles
/tmp/enumerate_k11_second_order_profiles
```

### Explicit surviving singleton profile and endpoint schedule

The minimum-`x3` singleton profile surviving all the new scalar rows is

\[
 x=(1,0,366,95),
 \qquad y=(0,366,96).                             \tag{30}
\]

It is not merely an abstract integer tuple.  The following central interval
schedules realize its monotone states and all strict common-endpoint nesting:

\[
\begin{array}{ll}
 I^6_0=[0,0],&\\
 I^6_i=[i,i+2] & (1\le i\le366),\\
 I^6_i=[i,i+3] & (367\le i\le461),\\[2mm]
 I^5_i=[i+1,i+2] & (0\le i\le365),\\
 I^5_i=[i+1,i+3] & (366\le i\le461).
\end{array}                                      \tag{31}
\]

They have 461 common left endpoints and 460 common right endpoints, so their
two-colour endpoint graph has

\[
 c=924-461-460=3
\]

components.  All common endpoints obey strict rank-five-inside-rank-six
nesting.  The width-qualified 324- and 24-alignment counts are also satisfied
on both sides (indeed the relevant counts are at least 460 and 95).

No masks have been assigned in (31), so it is not an OR-array candidate.  It
is an explicit counterexample to any claim that the current **scalar and
central endpoint geometry alone** eliminates `x0=1`.  Any proof excluding
that branch must use mask-incidence, lower-rank identity, or stronger
multi-rank endpoint information rather than another consequence of the same
width totals.

## 7. Counterexamples to tempting overstatements

### Endpoint geometry does not force `c>=2`

On positions `0,...,464`, take abstract selected intervals

\[
 J_i=[i,i+2]\quad(r=5),
 \qquad I_i=[i,i+3]\quad(r=6),
 \qquad 0\le i\le461.                             \tag{32}
\]

All left endpoints are common, giving 462 `L` edges `J_i--I_i`.  The common
right endpoints give 461 `R` edges `J_i--I_{i-1}` for `1<=i<=461`.  Their
union is one alternating Hamilton path, so `c=1`.  Strict nesting and all
endpoint-width rules hold.  Thus no endpoint-only proof can strengthen (3)
to `c>=2`.  The example is an endpoint schedule, not a claim that compatible
array labels exist.

### Other invalid strengthenings

* The two 24-element four-rank alignment sets need not intersect: the crude
  lower bound is `24+24-462<0`.  One cannot claim 24 chains aligned through
  ranks three to six at **both** ends.
* A degree-two rank-five vertex has two **different** rank-six neighbours; it
  is false that one rank-six interval aligns with it at both endpoints.
* Up to `c` rank-five width-two vertices may fail degree two.  The exact meet
  formula is not valid for every such vertex.
* Singleton exclusion must use the physical-boundary minimum.  Uniformly one
  gets one extra forbidden length-two slot and two extra slots through length
  three, not the larger interior-position counts.

## 8. Compact encoding recommendation

### Immediate, low-risk scalar cut

The joint band circuit already derives the Boolean value

\[
 e=x_0\in\{0,1\}
\]

and rank-six boundaries `g1,...,g6` with

\[
 x_3=g_4-g_3.
\]

Strengthen the existing `x3>=93` comparator to

```text
g3 + 93 + 2*e <= g4.
```

This is one small guarded comparator.  In the existing unsigned bit-vector
convention, `2*e` is the two-bit vector `{-one,e}`.  The implementation should
remain behind the joint-band guard and receive the same exhaustive boundary
truth-table audit as the other profile rows.

The stronger singleton-branch cut (29) is also compact.  Let

\[
 x_{\rm short}=x_0+x_1=g_2+462-g_5.
\]

When `e=1`, equation (29) is `y2>=xshort+95`, or

\[
 g_2+557\le y_2+g_5.                             \tag{33}
\]

Guard this comparator by `e` and by the selected rank-five chain.  After
substituting the existing three exact `y2` formulas, the unsigned rows are

```text
A: g2 + 557 + h2 + h4 <= h3 + h5 + g5
B: g2 + 557 + h2      <= h3      + g5
C: g2 + 557 + h4      <= h5      + g5
```

where each row is active only under `e AND chain`.  This is much smaller than
materializing the 561 lower witnesses used in its proof.

### Exact component-defect propagation

If future endpoint summaries count `mL,mR`, expose

```text
c = 924-mL-mR
```

as a three-bit value and add (10).  An unsigned form avoiding division is

\[
 2\sum_{j=0}^{t}x_j+m_L+m_R
 \le
 2\sum_{j=0}^{t-1}y_j+924.                       \tag{34}
\]

This does not improve the final projected profile polytope when only `c<=6`
is known.  Its value is conditional propagation from endpoint omissions into
width states.

For greater propagation, define per-central-vertex `hasL`, `hasR`, and
`twoSided` summaries.  Under `twoSided`, emit the bitwise meet/join clauses
from (6)--(7).  These clauses are redundant consequences of exact interval OR
semantics, so they are safe strengthening clauses.  Counts (15)--(16) can be
added only if a size audit shows a benefit.

### What not to encode yet

The 186-diamond theorem becomes directly useful only when the actual
rank-four endpoint witness on each side is named.  The present
`ZL324/ZR324` summaries certify existence and width, not target identity.
Do not infer rank-four union equations from those summaries alone.

There is also a possible larger compression: retain the target permutation
for one central layer, derive every degree-two target of the other layer by
(6) or (7), and leave at most `c` generic exceptions.  This is mathematically
sound in principle, but the target-coverage/all-different circuit for the
derived layer must be designed and audited separately.  The shadow identities
alone do not prevent two different degree-two vertices from receiving the
same target.

## 9. Ledger classification

| statement | status | likely use |
|---|---|---|
| `c=uL+uR` is the exact component count | new exact refinement | endpoint propagation |
| at least `462-c` degree-two vertices per central layer | new exact refinement | meet/join clauses |
| exact meet/join identities (6)--(7) | new structural theorem | central compression/propagation |
| coupled inequalities (10) | profile-redundant after `c<=6` | useful before projection |
| at least 186 two-sided rank-four diamonds | new structural theorem | needs rank-four identity links |
| bounds (19)--(22) | new second-order alignment | local state propagation |
| contiguous blocks (23)--(24) | structural consequence | optional local reasoning |
| length-two singleton cut (25) | arithmetic-redundant | regression/local exclusion |
| `x3>=93+2x0` | independently confirmed strengthened scalar cut | immediate compact encoding |
| boundary-localized cut `y2>=x1+82+14x0` | new, strictly stronger in `x0=1` | guarded compact comparator |

All statements are necessary consequences only.  They neither produce a
length-465 array nor prove that none exists.
