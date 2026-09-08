# The `k=15` radius-61 projection and q1-Hamilton switch geometry

## Alternating forest, radius-47 cut, and an exact compound circuit

Date: 2026-07-29

## Status and principal conclusions

Let

* `R` be the residence-clean strict resident factor;
* `J` be the 69-change joint upper-`q=1`/lower-`q=3` scaffold;
* `P` be the exact nearest degree-two projection of `J`;
* `H` be the supplied upper-`q=1`-complete physical Hamilton factor at
  distance 93 from `J`; and
* `Q` be its preceding upper-`q=1`-complete five-cycle factor at distance 94
  from `J`.

This note proves the following exact statements.

1. The pairwise choice distances are

   \[
        d(R,J)=69,\qquad d(J,P)=61,\qquad d(R,P)=69.     \tag{0.1}
   \]

2. The true expanded symmetric difference `J triangle P`, after cancelling
   only identical inclusion-edge orbits, is a forest of 21 trees.  Its 61
   full-choice endpoint-current columns are linearly independent.  Hence
   there is no nonempty alternating cycle and no nonempty endpoint-neutral
   subset of the direct `P <-> J` replacements.  A degree-two repair of `P`
   must introduce choices outside that overlay.  A new exact dual certificate
   proves, without any search assumption, that 61 is the minimum degree-only
   distance from `J`.

3. The expanded symmetric difference `R triangle P` has 168 exclusive
   inclusion-edge orbits, 152 incident vertices, and three connected
   components, so its cycle-space dimension is

   \[
                         168-152+3=19.                  \tag{0.2}
   \]

   A phase-labelled 19-cycle linear basis and a separate edge-disjoint
   alternating decomposition of lengths

   \[
                         60,48,40,12,6,2                \tag{0.3}
   \]

   are frozen explicitly.  All 64 subsets of the six edge-disjoint circuits
   are legal degree-two selectors.  None is upper-`q=1` complete; their best
   states have 45 holes.

4. Reversing one explicit `C_12` from `P` changes six owners, preserves
   degree two, reduces upper-`q=1` holes from 46 to 45, and reduces the
   physical component count from 21 to 7.  It does not improve residence:
   795 short-run defects remain.

5. Every degree-two upper-`q=1`-complete selector `F` obeys the new exact
   lower bound

   \[
                             \boxed{d(P,F)\ge47}.        \tag{0.4}
   \]

   Radius 46 is excluded by a four-vertex integer potential.  This proof
   uses neither residence, connectivity, voltage, lower-owner capacities,
   nor aggregate old-colour capacities.

6. The exact degree-plus-upper-`q=1` LP around `J` has optimum

   \[
   \frac{1277131056929583148784443}
        {17012931595358722031549}
   =75.0682532149\ldots .                              \tag{0.5}
   \]

   Hence every integral degree-two upper-`q=1` selector is at least 76
   choices from `J`.  An explicit 86-change selector gives the present
   degree/q1 interval `76 <= rho_J <= 86`.

7. The supplied `H` satisfies

   \[
       d(J,H)=93,\qquad d(P,H)=114,\qquad d(R,H)=126.   \tag{0.6}
   \]

   The `P/H` full-choice current matrix has rank 112 and nullity two, with
   neutral component blocks of 111 and 3 owners.  Its phase-labelled overlay
   has 310 arcs, 264 vertices, two components, and cycle-space dimension 48.
   A five-circuit legal Boolean subcube of expanded lengths

   \[
                            272,14,10,8,6               \tag{0.7}
   \]

   contains `H`; among its 32 states, only `H` is upper-`q=1` complete.

8. The 15-owner difference `Q triangle H` has four disjoint whole-choice
   current blocks `C_6,C_6,C_8,C_10`.  Their 16-state cube contains the
   aggregate-hole-count variant

   \[
                    H^*=Q+C_{6b}+C_{10}.                \tag{0.8}
   \]

   It is upper-`q=1` complete, is one physical Hamilton cycle of unit voltage,
   and has the same three centre distances as `H`.  It changes the supplied
   factor's aggregate lower `(q2,q3)` hole counts from `(56,22)` to `(56,21)`
   and upper `(q2,q3)` counts from `(16,1)` to `(15,0)`.  This is a count
   tradeoff, not targetwise or all-depth dominance: its lower-`q4` count
   increases from 4 to 5.

These are exact central-factor statements, not a contiguous-OR word.  Every
q1-complete Hamilton witness exhibited here still has at least 1,050
residence defects and deeper-shadow holes, and no common physical compiler or
literal word is certified.

## 1. Frozen inputs and provenance boundary

The three selections are stored in

```text
scratch/fixtures/k15_residence_hint_explicit_v1.json
scratch/fixtures/k15_joint_q1_q3_scaffold_hint_v1.json
scratch/k15_joint_scaffold_degreeonly_r61.json
scratch/k15_joint_scaffold_degreeonly_r61_hint.json
```

The supplied q1-complete factors and the mask-10 aggregate-count factor are

```text
scratch/k15_joint_scaffold_degree_atmost96_q1inc.json
scratch/k15_joint_q1ham_d93_snapshot.json
scratch/k15_joint_q1ham_d93_dominant_mask10.json
```

The four base-file SHA-256 values, in the first displayed order, are

```text
4482c3d448b3e314f89cc0c6e3f04a950e12a9e97ceb680da0478a00f2f4ee10
8e48bff3328b3440c479f4dd659f5350f4f17917160766612b968e5361a70fdb
5ad877cfa8f599d28fdddbcc0154c1bd4e73f850313ff3f8df59a5fd1f6089ac
13a293e435c77f2f4f9c04ebf2994acb47bec2b15fe3e7c5819f1e880d634058.
```

The `Q,H,H^*` file SHA-256 values are

```text
d0964d71cb74bb2956e645aede7253c999be28401e1df408164e7d1aea671e5e
76a83f012687f7382f8c140a51f1ad34702f9d393596d3d1d523a1c275c1e91f
a4ee63d4400f5f485701a6a08d9efd9c88c0bba1218c553baba5ded8d546675c.
```

The stable quotient choice table has SHA-256

```text
8d09676a3c073c5bb688c6ea61d8561087f560ebcc1fac775b9a97d33b1cf08a.
```

The explicit selection `P` is independently verified to choose one
loop-free choice at every one of the 429 lower owners and to have degree two
at every central rank-8 quotient vertex.  Its physical lift consists of

\[
        1\text{ cycle of length }3660,\quad
        5\text{ cycles of length }141,\quad
        15\text{ cycles of length }138.                 \tag{1.1}
\]

It has 795 residence defects and misses 46 upper-`q=1` colours, 55 lower
`q=2` colours, 20 lower `q=3` colours, and 77 upper colours over all upper
ranks.  Its nonzero upper-`q=1` load histogram is

\[
                    1^{183}2^{80}3^{20}4^4 5^2.         \tag{1.2}
\]

The nearestness of `P` is no longer conditional on an external radius sweep.
An exact `1/8`-integral LP dual has objective 61 and satisfies all 11,569
replacement inequalities.  Since `P` attains 61, every degree-two selector
`F` obeys

\[
                         d(J,F)\ge61.                    \tag{1.3}
\]

The solver-free verifier and theorem report are

```text
scratch/verify_k15_joint_scaffold_degree_projection.py
scratch/k15_joint_scaffold_degree_dual.certificate.json
MATH_CERTIFICATE_K15_JOINT_SCAFFOLD_DEGREE_DISTANCE61_20260729.md.
```

The label `OPTIMAL` in the stored `Q` file belongs to its fixed
radius-at-most-96 feasibility model.  It is not a global proof that distance
94 is optimal for any q1 problem.  Similarly, the `H` file is an explicit
feasible incumbent.  Every structural assertion below is reconstructed from
the displayed choices and does not use those solver-status labels.

## 2. Pairwise Hamming and colour geometry

At each lower owner, the three selected choices have the following exact
relation counts:

\[
\begin{array}{c|r}
\text{relation}&\text{owners}\\ \hline
R=J=P&346\\
R=J\ne P&14\\
R=P\ne J&14\\
J=P\ne R&22\\
R,J,P\text{ all distinct}&33.
\end{array}                                               \tag{2.1}
\]

This proves (0.1).

The resident misses 67 upper-`q=1` colours.  The projection repairs 28 of
them, still misses 39, and creates the seven new holes

\[
           1407,2543,2555,3773,3995,5751,7085.          \tag{2.2}
\]

Thus `P` has `39+7=46` holes.

The 61 changes from `J` to `P` split exactly as follows.

* Forty-six changes delete the unique `J` witness of a distinct final `P`
  hole.
* The other fifteen changes are endpoint-degree balancers.

Among the 46 witness erosions, 28 occur at all-distinct owners, 11 at owners
of type `R=P!=J`, and 7 at owners of type `R=J!=P`.

One tempting marginal repair is to restore those 46 `J` choices and no
others.  It does add all 46 missing colours, but it deletes the last current
witnesses of

\[
                           5807,6093,7851.               \tag{2.3}
\]

It therefore still has three upper-`q=1` holes.  Its endpoint-current vector
has support 127 and `L^1` norm 134, with positive mass 67.  Since one further
full-choice replacement changes at most four endpoint incidences, this fixed
46-choice layer is at least

\[
                            \left\lceil134/4\right\rceil=34  \tag{2.4}
\]

additional changes from degree two.  This is a bound around that fixed
marginal layer, not a global 80-change lower bound.

## 3. Exact expanded-overlay definitions

A catalogue choice `c=(L,a,b)` uses the two inclusion-edge orbits

\[
             (L,a),\qquad (L,b),                         \tag{3.1}
\]

whose upper endpoints are the canonical rank-8 orbits of `L+a` and `L+b`.
Two incidences cancel between selections only when their actual identifiers
`(L,coordinate)` agree.  Distinct coordinates leading to the same canonical
upper orbit remain distinct parallel inclusion-edge orbits.

For two selections `A,B`, colour every `A`-exclusive incidence red and every
`B`-exclusive incidence blue.  Orient

\[
     \text{red}:\quad U\longrightarrow L,
     \qquad
     \text{blue}:\quad L\longrightarrow U.              \tag{3.2}
\]

If both selections have degree two, the resulting directed multigraph is
Eulerian at every lower and upper vertex.  Its directed cycles are precisely
expanded alternating circuits.  Toggling one such circuit removes one red
and adds one blue incidence at every visit, and hence preserves degree two.
The resulting pair of incidences at every lower owner must still be checked
against the loop-free catalogue.

This actual-incidence definition is essential.  Connecting a changed lower
owner to the union of old and new endpoint **orbits** incorrectly retains
cancelled common incidences and can merge distinct components.

## 4. The `J triangle P` alternating-forest obstruction

### Theorem 4.1 (21-tree projection forest)

The true expanded exclusive graph `J triangle P` has

\[
       E=206,qquad V=227,qquad c=21,qquad E-V+c=0.     \tag{4.1}
\]

Its 21 components are therefore trees.  Their lower-owner sizes are

\[
                28,8,4,2,2,2,\underbrace{1,\ldots,1}_{15}. \tag{4.2}
\]

The 61 full-choice endpoint-current columns have rank 61 over `F_2`, hence
also over `Q`.  Consequently:

1. `J triangle P` contains no alternating circuit;
2. no nonempty subset or nonzero real combination of the 61 direct
   replacement currents is zero; and
3. `P` is the unique degree-two full-choice hybrid in the coordinate cube
   spanned by the displayed `J` and `P` choices.

#### Proof

The exact counts and connected components are reconstructed from the 206
actual exclusive incidence records.  Equation (4.1) and connectedness of
each component make every component a tree, so no closed alternating trail
exists.  Independently, an exact row reduction gives column rank 61 modulo
2.  A nonzero 61-by-61 minor modulo 2 is an odd, hence nonzero, integer
minor, so the columns are independent over `Q`.

If a second hybrid were degree two, the set of direct `P -> J` reversions
used by that hybrid would have zero total endpoint current.  Independence
forces that set to be empty.  ∎

The component colour effects under `P -> J` are recorded exactly.  In brief:

\[
\begin{array}{c|c|c}
\text{owner count}&\text{P holes restored}&\text{new old-colour holes}\\ \hline
28&18&0\\
8&7&\{6093\}\\
4&4&0\\
2&2&0\\
2&1&\{7403\}\\
2&2&0\\
15\text{ singletons}&12\text{ total}&0.
\end{array}                                               \tag{4.3}
\]

The three q1-auxiliary singleton components are rooted at lower owners
`1395,2669,2843`.  Table (4.3) is only a marginal ledger: Theorem 4.1 says
that none of its rows is an endpoint-neutral switch.  Any q1 repair built
from scaffold reversions must add new, exterior endpoint currents.

## 5. The grouped `R triangle P` kernel

For a changed lower owner `L`, put

\[
  \delta_L=\partial P_L-\partial R_L                  \tag{5.1}
\]

on the 429 central endpoint orbits.  There are 69 columns.  Their exact rank
over `F_2` is 66.  The following three disjoint indicator vectors have zero
integer current:

\[
\begin{aligned}
 C_1&=\{127\},\\
 C_3&=\{637,1645,2669\},\\
 C_{65}&=\{L:R_L\ne P_L\}\setminus(C_1\cup C_3).       \tag{5.2}
\end{aligned}
\]

Since they are independent and span the three-dimensional mod-2 kernel,
every **full-choice** `R/P` hybrid that remains degree two is a union of
these three blocks.  Conversely each union is degree two.  Thus there are
exactly eight such hybrids.

Their audited terminal statistics are

\[
\begin{array}{c|r|r|r|r}
\text{blocks}&d(R,\cdot)&q1\text{ holes}&\text{physical cycles}&
\text{residence defects}\\ \hline
\varnothing&0&67&1&0\\
C_1&1&67&15&15\\
C_3&3&66&1&30\\
C_1+C_3&4&66&1&45\\
C_{65}&65&47&7&720\\
C_1+C_{65}&66&47&21&750\\
C_3+C_{65}&68&46&25&765\\
C_1+C_3+C_{65}=P&69&46&21&795.
\end{array}                                               \tag{5.3}
\]

No full-choice hybrid is upper-`q=1` complete.

### 5.1 The explicit `C_3` colour-improving circuit

The three endpoint currents form the directed triangle

\[
        1661\longrightarrow2685\longrightarrow3693
        \longrightarrow1661,                            \tag{5.4}
\]

where these numbers are canonical rank-8 orbit representatives.  In quotient
vertex indices this is `69 -> 152 -> 262 -> 69`.

The complete records are

\[
\begin{array}{c|c|c|c|c}
L&\text{resident choice}&\text{projection choice}&
\text{old colour}&\text{new colour}\\ \hline
637&(637,8,10)&(637,8,11)&1917&2941\\
1645&(1645,8,11)&(1645,4,8)&3949&1917\\
2669&(2669,4,14)&(2669,10,14)&5371&7015.
\end{array}                                               \tag{5.5}
\]

Colour `1917` is relayed, the old colours `3949,5371` retain other witnesses,
and missing colour `2941` is gained; `7015` was already present.  Hence this
exact `C_6` improves 67 holes to 66 while preserving degree two.  It creates
30 residence defects, so it is not a decorated carrier switch.

### 5.2 The phase-only `C_1`

At lower owner 127,

\[
  (127,7,10)\longmapsto(127,10,14).                     \tag{5.6}
\]

Both choices have the same unordered quotient endpoint representatives
`{255,1151}`.  Their endpoint current is zero, but the distinct coordinates
7 and 14 are parallel phase-labelled incidences over endpoint 255, giving an
expanded alternating `C_2`.  Applied alone to `R`, it changes one physical
Hamilton lift into 15 cycles of length 429.  Thus zero contracted current
does not mean zero voltage/topological effect.

### 5.3 The large block

The block `C_65` contains 50 one-end and 15 two-end replacements.  It repairs
27 resident holes but creates exactly the seven holes in (2.2), leaving 47.
Its complete owner, choice, endpoint, phase, and colour signature is frozen
in the audit JSON; listing 65 records here would obscure the smaller exact
structures.

## 6. The expanded 19-cycle basis and legal six-circuit cube

The phase-labelled `R triangle P` expanded graph has

\[
       E=168,qquad V=152,qquad c=3,                    \tag{6.1}
\]

with component owner sizes `65,3,1`.  Each arc has signature

```text
(side, lower, coordinate, middle_index, phase_shift, choice_id),
```

where resident-exclusive arcs are directed upper-to-lower and
projection-exclusive arcs lower-to-upper.

### Theorem 6.1 (deterministic 19-cycle linear basis)

There is an exact simple directed alternating-cycle basis of lengths

\[
\begin{gathered}
 2,6,6,8,
 12,12,12,12,12,
 14,14,18,20,22,24,24,32,34,34.                         \tag{6.2}
\end{gathered}
\]

Its 19 incidence vectors are independent over `F_2` and over `Q`, and hence
span the cycle/circulation space of dimension 19.  Every basis row by itself
toggles `R` to a legal loop-free catalogue selector.

The construction is deterministic: for every directed arc, delete it and
use lexicographic breadth-first search from its head to its tail; deduplicate
the resulting cycles by arc set; then greedily retain highest-pivot
independent rows in increasing `(length,arc tuple)` order.

This is a **linear** basis, not a free Boolean switch basis.  The cycles
overlap.  For example, XORing basis rows 3 and 7 leaves owner 463 with zero
selected incidences and owner 1231 with four.  Linear cycle-space generation
must therefore be coupled with exact integer owner degrees.

### Theorem 6.2 (six edge-disjoint legal switch coordinates)

A canonical red-blue incidence pairing partitions all 168 exclusive arcs
into six edge-disjoint alternating circuits of lengths

\[
                           60,48,40,12,6,2.              \tag{6.3}
\]

Every one of their 64 subsets toggles `R` to a legal degree-two catalogue
selector.  Exhausting this finite six-dimensional cube gives:

* no upper-`q=1`-complete state;
* minimum hole count 45, attained by masks 23 and 55; and
* exactly one residence-clean state, the resident mask 0.

This 64-state audit is a finite basis audit, not a broad catalogue search.

### Corollary 6.3 (an explicit six-owner improvement of `P`)

Mask 55 is `P` with the canonical `C_12` reversed.  It changes the following
six projection choices:

\[
\begin{array}{c|c|c|c|c}
L&\text{old }P\text{ choice}&\text{new choice}&
\text{old colour}&\text{new colour}\\ \hline
319 &(319,6,13)&(319,6,9)&1533&895\\
829 &(829,1,13)&(829,10,13)&3325&7413\\
1213&(1213,9,14)&(1213,6,14)&3451&2555\\
1341&(1341,9,11)&(1341,7,11)&3901&3517\\
1453&(1453,4,11)&(1453,9,11)&3517&4013\\
1709&(1709,8,11)&(1709,4,11)&4013&3773.
\end{array}                                               \tag{6.4}
\]

The colour relay repairs projection holes `7413,2555,3773`, creates holes
`3325,3451`, and hence improves

\[
                    46\longrightarrow45.                \tag{6.5}
\]

The terminal selector is six choices from `P`, 64 choices from `R`, has
seven physical components, and retains all 795 residence defects.  Its
choice-list SHA-256 is

```text
aa814e3948068ef544b6ffe833ab2b435ce65706dc4ee91eaa0cf5a38a760793
```

and its six-owner phase-labelled switch SHA-256 is

```text
99511a948819513e5c5f8c198b0081ba32f3b4d6c9df2654d35acda3dab9d5c3.
```

Reversing the phase-only `C_2` as well gives the other 45-hole minimizer,
which is 63 choices from `R` and has 765 residence defects.  Neither is a
carrier.

## 7. A four-vertex potential excludes radius 46 around `P`

Let `H_P` be the 46 missing upper-`q=1` colours of `P`.  One changed choice
can add at most one member of `H_P`, so every complete selector is at least
46 changes from `P`.

At equality, every new choice must add a distinct member of `H_P`; there is
no spare old-colour relay.  Therefore every deleted old colour must have
`P`-load at least two.  Enumerating all such individually q1-safe actions
gives exactly

\[
  984=1\text{ zero-current}+482\text{ one-end}+501\text{ two-end}. \tag{7.1}
\]

For an action `a`, let

\[
       \delta_a=\partial e_{\rm new}(a)
                  -\partial e_{\rm old}(a).              \tag{7.2}
\]

Define an integer potential on canonical middle-orbit representatives by

\[
 \pi(5549)=1,qquad
 \pi(1781)=\pi(3387)=\pi(5811)=-1,                      \tag{7.3}
\]

and `pi=0` elsewhere.

### Theorem 7.1 (sharp radius-46 potential cut)

Every one of the 984 actions satisfies

\[
       \langle\pi,\delta_a\rangle
          \ge {\bf1}_{\{\operatorname{target}(a)=11627\}}. \tag{7.4}
\]

All six actions serving target `11627` have flux exactly one.  Hence no
degree-two upper-`q=1`-complete selector is at distance 46 from `P`, and

\[
                              d(P,F)\ge47.               \tag{7.5}
\]

#### Proof

The exact action audit has slack histogram

\[
                            0^{964}1^{20}                \tag{7.6}
\]

after subtracting the right side of (7.4).  A sharp completion must select
one action for each of the 46 targets.  Summing (7.4) gives total potential
flux at least one.  But both the source and terminal selectors have degree
two, so

\[
             \sum_a\delta_a=0,
             \qquad
             \left\langle\pi,\sum_a\delta_a\right\rangle=0,
\]

a contradiction.  ∎

For transparency, the six `11627` actions occur at lower owners

\[
                         1387,1453,1717,2411,3371,5421. \tag{7.7}
\]

Their old/new canonical endpoint pairs are respectively

\[
\begin{array}{c|c|c}
L&\text{old endpoints}&\text{new endpoints}\\ \hline
1387&\{1899,3435\}&\{3435,5549\}\\
1453&\{1469,3501\}&\{5549,5813\}\\
1717&\{1781,3765\}&\{5813,3435\}\\
2411&\{5811,5813\}&\{3435,5813\}\\
3371&\{3387,5549\}&\{3435,5549\}\\
5421&\{5783,5789\}&\{5549,5813\}.
\end{array}                                               \tag{7.8}
\]

The full action table and inequality are frozen in

```text
scratch/k15_projection_r46_potential_cut.certificate.json
```

with SHA-256

```text
94c951ab0d7a9cf14115f9cec21ac75157b382e86e7146f93151013e03e65251.
```

The solver-free verifier

```text
scratch/verify_k15_projection_r46_potential_cut.py
```

has SHA-256

```text
f2d2aa4f73ea688388278032857ccb275fc75245a5294bcbb608129df1f55c21
```

and reconstructs all 984 actions with action-signature SHA-256

```text
5b7c3becb823a75f32473729645064c07d798150ec748f7fb5d5acbc60849936.
```

No floating-point or optimization result is needed for Theorem 7.1.

## 8. Consequences at the first possible radius 47

### Theorem 8.1 (negative-potential or relay-ear dichotomy)

Every degree-two upper-`q=1` completion `F` with `d(P,F)=47` has at least one
of the following two structures.

1. **Negative-potential ear.**  After choosing one q1-safe service action for
   each of the 46 missing colours, the remaining forty-seventh action has

   \[
                         \langle\pi,\delta\rangle\le-1. \tag{8.1}
   \]

2. **Unique-colour relay ear.**  Some missing-colour service action deletes
   the unique current witness of an old colour, and the forty-seventh action
   restores that old colour.

#### Proof

If every service action deletes a colour of load at least two, all 46 belong
to the certified action set of Theorem 7.1, and their total potential flux is
at least one.  Endpoint balance forces the one remaining action to have flux
at most minus one.

Otherwise a service action deletes a load-one old colour.  Since its new
colour is one of the 46 initially missing colours, it cannot simultaneously
restore the deleted old colour.  The only spare action must do so.  ∎

Thus ordinary safe service cycles cannot be the first completion.  A
radius-47 candidate must contain an explicitly exceptional ear.

## 9. Three-centre distance constraints

The proved resident theorem gives

\[
       d(R,F)\ge68                                      \tag{9.1}
\]

for every degree-two upper-`q=1`-complete `F`.  Since `d(R,P)=69`, let

* `a_R` count owners with `P!=R` at which `F` reverts exactly to `R`; and
* `c_R` count owners with `P=R` at which `F` departs from that common choice.

Changes to a third choice at a `P!=R` owner remain distance one from `R`.
Therefore

\[
          d(R,F)=69-a_R+c_R,
          \qquad a_R\le c_R+1.                          \tag{9.2}
\]

For completeness, the exact `J`-centred q1 lower bound has a short dual
proof.  For every replacement action `a`, the stored rational multipliers
`q_v` (free), `r_L<=0`, and `s_c>=0` satisfy, in exact integer arithmetic,

\[
 q\mathbin{\cdot}\delta_a+r_{L(a)}+s_{\mathrm{new}(a)}
             -s_{\mathrm{old}(a)}\le1.
\]

Summing these 11,569 inequalities against any fractional degree/q1
projection gives

\[
 \sum_a x_a\ge
 \frac{1277131056929583148784443}
      {17012931595358722031549}
 =75.0682532149\ldots .
\]

The signs of `r,s` use respectively the one-action-per-owner upper bounds
and the q1-load lower bounds.  Taking a ceiling proves `d(J,F)>=76` for every
integral selector.  The exact primal attains the displayed fractional value,
so the rational LP statement itself is sharp.

Define analogously `a_J,c_J`.  Degree-only nearestness already gives
`d(J,F)>=61`, but upper-`q=1` completeness permits the stronger exact LP
bound

\[
 d(J,F)=61-a_J+c_J\ge76,
 \qquad c_J-a_J\ge15.                                  \tag{9.3}
\]

For `t=d(P,F)`, (9.3) implies

\[
                  a_J\le\left\lfloor\frac{t-15}{2}\right\rfloor. \tag{9.4}
\]

At the first possible radius `t=47`, at most 16 changes can directly restore
the original `J` choice.  Since one direct restoration adds at most one of
the 46 missing colours, at least 30 holes require witnesses not used by `J`.
Independently, all 39 holes common to `R` and `P` require nonresident choices,
because the resident factor contains no witness of those colours anywhere.

These are routing restrictions, not an existence theorem at radius 47.

## 10. The supplied Hamilton factor as an exact compound circulation

For a catalogue choice `c` at lower owner `L`, let

\[
 b(c)=e_{u(c)}+e_{v(c)}\in\mathbb Z^{429}              \tag{10.1}
\]

be its two-endpoint incidence vector.  A selector `S` is degree two exactly
when

\[
                       \sum_L b(S_L)=2\mathbf 1.        \tag{10.2}
\]

### Theorem 10.1 (affine projection fibre)

If `S` and `T` are degree-two selectors, then their signed symmetric
difference is an integral circulation.  Equivalently,

\[
                  \sum_L\bigl(b(T_L)-b(S_L)\bigr)=0.    \tag{10.3}
\]

After cancelling identical `(lower,coordinate)` incidences and orienting
`S`-exclusive arcs middle-to-lower and `T`-exclusive arcs lower-to-middle,
the expanded graph is Eulerian and decomposes into directed alternating
circuits.  Conversely, a set of whole-choice replacements preserves degree
two if and only if its total endpoint current is zero.

#### Proof

Subtract (10.2) for `S` and `T`.  At every lower node the number of incoming
and outgoing exclusive incidences is equal; at every middle node equality is
(10.3).  Hence the expanded directed graph is Eulerian and admits a directed
cycle decomposition.  The converse is the same identity read backwards. ∎

In particular, since both `P` and `H` correct the degree boundary of `J`,

\[
        \partial(H-J)=\partial(P-J),\qquad
        \partial(H-P)=0.                               \tag{10.4}
\]

Thus all degree-two projections of `J` form one affine current fibre; the
61-change point `P` is its nearest point, while `H` is a q1-complete
Hamilton point farther along its circulation lattice.

### 10.1 Exact statewise comparison

The owner partition of `(P,J,H)` is

\[
\begin{array}{c|r}
\text{relation}&\text{owners}\ \hline
P=J=H&308\\
P=J\ne H&60\\
J=H\ne P&28\\
P=H\ne J&7\\
P,J,H\text{ all distinct}&26.
\end{array}                                             \tag{10.5}
\]

Consequently

\[
 d(P,H)=60+28+26=114,
 \qquad d(J,H)-d(J,P)=60-28=32.                        \tag{10.6}
\]

This is the key correction to a misleading local interpretation: the
Hamilton point pays only 32 additional units in the objective centred at
`J`, but it is not a 32-choice repair of `P`.  It moves 114 owners, including
26 third-choice replacements.

### Theorem 10.2 (the `111+3` whole-choice relay)

The 114 full-choice endpoint-current columns for `P -> H` have exact rank
112 over `Q` and rank 112 modulo each of `2,3,5,101`.  Their support graph
has two components, on 111 and 3 lower owners.  The two component indicators
are neutral and form the complete kernel.  Hence exactly four binary `P/H`
hybrids are degree two:

\[
\begin{array}{c|r|r|r}
\text{enabled block}&q1\text{ holes}&\text{physical cycles}&
\text{residence defects}\ \hline
\varnothing&46&21&795\\
3\text{-owner block}&45&21&795\\
111\text{-owner block}&2&7&1065\\
111+3=H&0&1&1050.
\end{array}                                             \tag{10.7}
\]

The three-owner block is

\[
                  \{1339,1465,4775\},                  \tag{10.8}
\]

with directed endpoint triangle

\[
                  1467\longrightarrow5435
                  \longrightarrow4791\longrightarrow1467             \tag{10.9}
\]

and colour ledger

\[
 +\{5499,3515,5815\}-\{1531,5047,7605\}.              \tag{10.10}
\]

The 111-block leaves holes `{3515,5499}`.  The triangle restores both,
including the newly exposed relay colour `3515`.  Therefore `H` is the
unique q1-complete binary hybrid of `P` and `H`; independent hole additions
cannot explain the completion.

#### Proof

Exact elimination gives rank 112.  The two disjoint component indicators
give two independent rational kernel vectors, so the rational nullity is
exactly two.  Reduction modulo 2 shows that every binary kernel vector is a
union of the two blocks.  Direct colour and physical audits give (10.7)--
(10.10). ∎

### Theorem 10.3 (five-coordinate phase switch cube)

The full phase-labelled `P triangle H` overlay has

\[
             E=310,\qquad V=264,\qquad c=2,
             \qquad E-V+c=48.                          \tag{10.11}
\]

Its components have `(E,V,dimension,owners)` equal to

\[
                       (304,258,47,111),\qquad(6,6,1,3). \tag{10.12}
\]

A canonical arc pairing decomposes all 310 arcs into five edge-disjoint
legal switch coordinates:

\[
\begin{array}{c|r|r|r|r}
i&\text{expanded length}&\text{owner count}&
\text{phase voltage}&q1\text{ holes when used alone}\ \hline
0&272&103&10&11\\
1&14&7&6&44\\
2&10&5&0&46\\
3&8&4&3&46\\
4&6&3&0&45.
\end{array}                                             \tag{10.13}
\]

Every one of the 32 subsets is a loop-free degree-two catalogue selector.
Only mask `31`, using all five coordinates, is upper-`q=1` complete.  Along
the canonical prefix the hole count is

\[
                         46\to11\to7\to5\to2\to0.       \tag{10.14}
\]

The first circuit repairs 37 holes but creates `{2911,3451}`; the third
later creates `3515`; the fourth repairs `{2495,2911,3451}`; and the final
triangle repairs `{3515,5499}`.  This is a five-dimensional Boolean basis
for this particular compound exchange, not a basis of the full
48-dimensional ambient cycle space.

### 10.2 Audit of the supplied `H`

The factor `H` is one physical cycle of length 6,435.  Its oriented quotient
voltage is 7; reversing the orientation gives the stored strict voltage 8.
Its physical-cycle SHA-256 is

```text
6610ac7fc6d83da51e6679f2ca8caf82f4557a0aa751bf2bff03a53b30787c75.
```

It is upper-`q=1` complete, but has 1,050 residence defects and hole vectors

\[
\begin{aligned}
\text{lower }q=2,\ldots,7&=(56,22,4,1,0,0),\\
\text{upper }q=1,\ldots,7&=(0,16,1,0,0,0,0).
\end{aligned}                                           \tag{10.15}
\]

The `P -> H` q1 ledger has support 135 and `L^1` norm 142.  Exactly 47
changed choices cover all 46 holes of `P`, with colour `1951` covered twice;
the other 67 changes are auxiliary.  Twenty-five changed choices delete a
colour having `P`-load one, so downstream colour recreation is an essential
part of the compound.

## 11. The `Q/H` local atlas and an aggregate-count Hamilton tradeoff

The preceding factor `Q` is already degree two and q1-complete.  It consists
of one quotient cycle of length 429 and oriented voltage 10.  Since
`gcd(10,15)=5`, its lift consists of five cycles of length 1,287.  It has
1,050 residence defects and

\[
 d(J,Q)=94,\qquad d(P,Q)=115,\qquad d(R,Q)=127.         \tag{11.1}
\]

### Theorem 11.1 (four whole-choice current blocks)

The 15 changed owners from `Q` to `H` split into four disjoint neutral
whole-choice blocks:

\[
\begin{array}{c|l}
C_{6a}&747,875,1239\\
C_{6b}&4699,4715,4813\\
C_8&1211,1465,4775,4837\\
C_{10}&1583,1615,2365,2887,3373.
\end{array}                                             \tag{11.2}
\]

Every one of their 16 subsets is a legal degree-two selector.  The expanded
blocks are clean `C_6,C_8,C_10` circuits except `C_{6b}`, whose eight
exclusive incidences have cycle rank two: a contracted `C_6` with one
attached phase-only `C_2`.

With bit order `(C_{6a},C_{6b},C_8,C_{10})`, q1-complete masks are

\[
             0,1,4,5,8,9,10,11,12,13,14,15,            \tag{11.3}
\]

and physical-Hamilton masks are

\[
                         1,6,7,9,10,14,15.              \tag{11.4}
\]

Thus the q1-complete Hamilton masks at distance 93 from `J` are exactly
`10,14,15` within this cube.  The colour coupling is the implication

\[
                         C_{6b}\Longrightarrow C_{10}.  \tag{11.5}
\]

Indeed `C_{6b}` alone lowers the `J`-distance from 94 to 93 but deletes the
unique current witness of colour `6779`; `C_{10}` restores it.

### Corollary 11.2 (a radius-93 aggregate-hole-count exchange)

Let

\[
                         H^*=Q+C_{6b}+C_{10}.            \tag{11.6}
\]

Then `H^*` has

\[
            (d(R,H^*),d(J,H^*),d(P,H^*))=(126,93,114),  \tag{11.7}
\]

is upper-`q=1` complete, and is one physical Hamilton cycle.  Its oriented
quotient voltage is 7 and its reverse voltage is 8.  It has 1,050 residence
defects and

\[
\begin{aligned}
\text{lower }q=2,\ldots,7&=(56,21,5,1,0,0),\\
\text{upper }q=1,\ldots,7&=(0,15,0,0,0,0,0).
\end{aligned}                                           \tag{11.8}
\]

Compared with the supplied `H`, it reduces the aggregate lower-`q3` count
from 22 to 21, upper-`q2` from 16 to 15, and upper-`q3` from 1 to 0, but
increases lower `q4` from 4 to 5.  This is not targetwise inclusion: at lower
`q2`, `H`-only holes are `{679,1433}` and `H^*`-only holes are `{441,3221}`;
at lower `q3`, `H`-only holes are `{59,737}` and the `H^*`-only hole is
`805`.  The upper gains are nested: `H^*` removes q2 hole `5871` and q3 hole
`6127` and adds none; its new lower-q4 hole is `105`.  Thus this is a useful
aggregate-count tradeoff, not support dominance.  The centre distances,
topology, voltage class, and residence count are unchanged.  The choice SHA
and physical-cycle SHA are respectively

```text
67d8460472d9a1f1abe2161feaaaf4c32cdfddc814997aee4182c5d7e220988c
95553147b88df75fb62ba6be1d189fa7f3ff9fe3452f788033be48f44f1c7b07.
```

### Corollary 11.3 (one-owner phase Hamiltonization)

The finer phase overlay contains the following single-owner legal switch at
lower `4699`:

\[
 (4699,8,13)\longmapsto(4699,7,8).                      \tag{11.9}
\]

The choices have IDs `10654 -> 10648` and colours `6875 -> 5083`.  Their
quotient endpoint pair is the same, `{4827,4955}`, while the phase of the
`4827` incidence changes from 12 to 0.  Applying (11.9) to `Q` changes its
quotient voltage from 10 to 13, equivalently strict reverse voltage 2, and
therefore fuses the five physical cycles into one.  Both affected colours
remain present: their loads change from `(2,1)` to `(1,2)`.  Residence stays
at 1,050.  The resulting cycle SHA-256 is

```text
ec00a03d3e8caecc64d03ee66bfb454c4dc61875354d8c1160c580b08b5cc8f4.
```

Hence topology is locally cheap in this atlas.  The unresolved obstruction
is residence and deeper support, not Hamiltonization by itself.

### 11.4 Interface with the radius-46 potential

For `P -> H^*`, all 114 action fluxes under the four-vertex potential (7.3)
have histogram

\[
                         (-1)^3\,0^{108}\,(+1)^3.       \tag{11.10}
\]

The 47 services for the 46 `P`-holes have total flux `+2`; the 67 auxiliary
actions have total flux `-2`.  Ten service actions delete a singleton old
colour and each has an explicit restoring action.  Thus the construction
crosses the cut in both ways allowed by Theorem 8.1: genuine relay ears and
negative-potential auxiliaries.  It is not a radius-47 construction.

## 12. Current exact distance intervals

Let `rho_X` be the minimum distance from centre `X` to a degree-two
upper-`q=1`-complete selector, and let `eta_X` impose in addition one physical
Hamilton cycle of unit voltage.  The exact lower bounds and audited explicit
upper bounds give

\[
\begin{array}{c|c|c}
X&\rho_X&\eta_X\\ \hline
P&47\le\rho_P\le108&47\le\eta_P\le114\\
J&76\le\rho_J\le86&76\le\eta_J\le93\\
R&68\le\rho_R\le82&68\le\eta_R\le126.
\end{array}                                             \tag{12.1}
\]

The upper bounds for `P,J` in the middle column come from the explicit
86-change-from-`J` selector, which lies 108 choices from `P` and has seven
physical cycles.  The upper bound 82 from `R` comes from the explicit
selector stored under the legacy filename
`scratch/k15_resident_q1factor_d83_snapshot.json`; its actual reconstructed
distance is 82 and it has 15 physical cycles.  These files are feasible
witnesses, not optimality certificates.

The `J` lower bound is stronger than degree-only nearestness: it is the
ceiling of the exact fractional degree-plus-q1 optimum (0.5).  The `R` lower
bound is the proved radius-67 flow obstruction.  The `P` lower bound is
Theorem 7.1.  No entry in (12.1) includes residence, deeper shadows, cut
survival, or the literal compiler.

## 13. Machine-checkable switch signatures

The unified deterministic auditor is

```text
scratch/audit_k15_joint_scaffold_degreeonly_r61_overlay.py
```

with SHA-256

```text
0b4cdcddc21e3f9baa0269d32e0674d688eafab95b36dc3cb7b6a7c3f37d6ad4.
```

Its frozen output is

```text
scratch/k15_joint_scaffold_degreeonly_r61_overlay.audit.json
```

with SHA-256

```text
94ffed00bdfa112195617e16371015d617c94043c156d8a76f83a2d0c9fa6aff.
```

The live auditor output byte-matches the JSON.  Important internal digests
are

\[
\begin{array}{c|l}
\text{object}&\text{SHA-256}\\ \hline
168\text{-arc phase table}&
d0b795c540a9622d9ef12ccc70d2d7ec7d761ccd5541faf63ede8b5ef373f8b2\\
six-circuit 64-state cube&
17436c18fa2f6968ef8a62b8868b25eed80bfb97b47e9ba906b7ee696526f335\\
19-cycle BFS candidates&
72b13340496345c4431723e206eea3057ad63a7c24ff43fc31ff7a42d54865ea\\
19-cycle basis&
cde0e5278b706e73f2b8465fbd7d67cbf8c5f2c46807eaabfad638cd01f0387b.
\end{array}                                               \tag{13.1}
\]

The JSON contains, rather than merely hashes:

* all phase-labelled exclusive arcs;
* every one of the 19 basis cycles;
* all six edge-disjoint circuits and their owner lists;
* all 64 legal cube states and their exact audits;
* the full choices for the 45-hole minimizer;
* the six-owner `C_12` switch records;
* the three grouped current-kernel blocks and all eight hybrids;
* all 21 `J/P` forest-component signatures; and
* the complete sharp q1 action inventory around `P`.

The `P/H` affine and phase audit is

```text
scratch/audit_k15_joint_q1ham_d93_overlay.py
scratch/k15_joint_q1ham_d93_overlay.audit.json
```

with SHA-256 values

```text
937470f485d1eccd05e81a669350a0695496599aa4cb06fb9fab661d52f112cf
c12f7319164466d1cf988e8b7dce6d8a5d8e324e0dbd9cc15219f21303537897.
```

The 310-arc signature and 32-state phase-cube digests are

```text
b22678965ffdb60ecffcb6673a3ed18effd4b1535a7f75a2f8c71fbf1f3acc49
3a1b04d54ae68cdeca195a17b7896fa66c4c4c9f71de113cdf9fcda35a74f386.
```

The independently written `Q/H` four-block auditor, its frozen 16-state
output, and the materialized mask-10 factor are

```text
scratch/audit_k15_q1ham_d94_d93_four_circuit_cube.py
scratch/k15_joint_q1ham_d94_d93_four_circuit_cube.audit.json
scratch/k15_joint_q1ham_d93_dominant_mask10.json
```

Their SHA-256 values are

```text
b6c223b255d549a1756b066c3428ab69ae6192cf0898d77816bac5f261c2050b
34a6eeb41d46a0383d6f7b0e08d06ce1d4871949c2a8947a1b012a231c970955
a4ee63d4400f5f485701a6a08d9efd9c88c0bba1218c553baba5ded8d546675c.
```

The word `dominant` in the legacy artifact filename/schema predates the
all-depth audit; no support-dominance claim is made.

Both auditors were replayed locally without optimization; each live output
byte-matches its frozen JSON.  The exact degree-only and degree-plus-q1 dual
certificates were also replayed solver-free.  Their principal certificate
hashes are

```text
1b131a34658feab6f09146e0c7f46bcfa709b34cad1ba245de84a1285d8b14d2
31251f4d44b0a05d073283bac59c6d85010d67e683c98774b3527b91e41d5cee.
```

The two non-Hamilton upper-bound selectors used in (12.1) are

```text
scratch/k15_joint_q1factor_d86_snapshot.json
scratch/k15_resident_q1factor_d83_snapshot.json
```

with SHA-256 values

```text
6e38e638101f8f8a325f8ea8d70191e2d0a699970812df6861aca5e0ef1e2887
75b52aab37cf2b3a22d3ccb043ab3f76b94558ef5bacb1c45cf811befdf062a7.
```

## 14. Sharp remaining boundary

The direct `P -> J` route is closed: it is an alternating forest with no
cycle, and its 61 full-choice currents are independent.  The direct `R/P`
overlay supplies substantial exact mobility, including a 19-cycle linear
basis, a six-circuit legal cube, an explicit q1-improving `C_12`, and the
small colour-improving `C_6`.  Nevertheless:

* the full-choice `R/P` cube never completes upper `q=1`;
* the richer six-circuit cube bottoms out at 45 holes;
* only its resident state is residence-clean; and
* every global q1 completion is at least 47 changes from `P`.

The new factors settle degree two, q1 completeness, and Hamilton topology
together at finite `k=15`; they do not settle the decorated carrier problem.
The one-owner phase switch (11.9) proves that topology itself is cheap in the
local atlas.  What remains sharp is simultaneous preservation or repair of
residence and the complete deeper tower.

At the first possible `P`-radius, a candidate must still install either a
negative-potential ear or a unique-colour relay ear and couple it into an
owner-exact alternating compound.  The explicit `H^*` compound shows both
mechanisms at radius 114, but its 1,050 residence defects and shadow holes
make it unusable for the literal compiler.  A final factor must additionally
satisfy residence, every lower and upper shadow, cut survival, exact owner
Hall, and one common physical `Q`/word.  None of those gates follows from the
degree/q1/Hamilton results proved here.
