# PBBS tagged collars: the endpoint overlap is real, but its complete upper residue is polynomially packable

**Date:** 2026-08-06  
**Method:** literal PBBS set calculus, nested-interval counting, and a
rank-stratified probabilistic packing argument; no computation or search  
**Status:** proof-safe audit and reduction.  The global tag reservoir does
separate all collar interiors, but the literal all-five collar bank is not a
path forest: consecutive heights share one tail/head owner.  Deleting the
incoming collars at that one role, and instead collaring the free outgoing
role-zero heads, leaves an unconditional five-collar protected forest.  Its
entire remaining upper current is a prospectively fixed bank with only
`O(HR)` targets in each excess-rank stratum, and those targets admit a
simultaneous low-exposure protected backup bank.  A
direction/colour-compatible completion, clipped residence, one literal
antecedent, and the typed cap are not proved here.

## 1. Notation

Use the height-pentagon notation on `Omega={0,1,...,2r}` and put

\[
                         R=r+1.
\]

Thus the owner shore has rank `R`.  Let

\[
 A_h=0\,1^h0^h(10)^{r-h},
 \qquad U_h=\Omega\setminus A_h.
\tag{1.1}
\]

For one height pentagon, write the old and new contracted owner edges as

\[
 P_{h,i}Q_{h,i}\quad\longleftrightarrow\quad
 P_{h,i}Q_{h,i+1},
 \qquad i\in\mathbb Z_5.
\tag{1.2}
\]

The rank-`r` exchange states satisfy

\[
 Q_{h,i}=\Omega\setminus Z_h^i,
 \qquad P_{h,i}=\Omega\setminus g(Z_h^i),
\tag{1.3}
\]

where `g=f^2` is the centred PBBS successor.

## 2. Audit of the global tag reservoir

For `h>=4`, the common rank-`R-3=r-2` core is

\[
 G_h={h+2,h+3,\ldots,2h}
      \mathbin{\dot\cup}
      \{2h+4,2h+6,\ldots,2r\}.
\tag{2.1}
\]

Hence

\[
 J_H=\{2H+2,2H+4,\ldots,2r\}
      \subseteq\bigcap_{h=4}^{H-1}G_h,
 \qquad |J_H|=r-H.
\tag{2.2}
\]

The calculation in
`MATH_THEOREM_PBBS_GLOBAL_TAG_RESERVOIR_PLANTS_SYNCHRONIZED_COLLARS_20260806.md`
is correct: if every collar path `p` receives a distinct tag `g_p in J_H`,
the deleted block `D_p` contains `g_p` and no other global tag, and `g_p`
is the first deleted letter, then

\[
 S_p(t)\cap\mathcal T=\mathcal T\setminus\{g_p\}
 \quad(t\ge1),
\tag{2.3}
\]

and every protected lower colour on the path has the same signature.
Thus the **interiors** of all selected collars are mutually owner- and
lower-colour-disjoint and avoid every pentagon resource containing all
global tags.

The endpoint topology does not follow from (2.3).  In fact it fails for the
literal all-five bank.

## 3. Exact adjacent-height endpoint overlap

For `h>=4`, all five PBBS successors delete the coordinate `p=h+1`.  At
role zero,

\[
 g(Z_h^0)=Z_h^0-\{h+1\}+\{1\}=A_h=Z_{h-1}^1.
\tag{3.1}
\]

Taking complements gives the binding identity

\[
 \boxed{P_{h,0}=Q_{h-1,1}=U_h.}
\tag{3.2}
\]

### Lemma 3.1 (this is the only high-height tail/head overlap)

For `h,h'>=4`,

\[
 P_{h,i}=Q_{h',j}
\]

if and only if `h'=h-1`, `i=0`, and `j=1`.

#### Proof

Every `g(Z_h^i)` contains the interval `3,...,h` and omits `h+1`.
Every `Z_{h'}^j` contains `3,...,h'+1`, together with only two labels from

\[
 \{0,1,2,2h'+1,2h'+2\}
\]

outside its fixed core.

If `h'>=h`, then `Z_{h'}^j` contains `h+1`, so equality is impossible.
If `h'<=h-2`, the fixed zero block of `Z_{h'}^j` begins at `h'+2`.
When `h>=h'+4`, at least the three consecutive coordinates
`h'+2,h'+3,h'+4` would have to be supplied by only two active labels.
When `h=h'+2`, the one missing coordinate `h'+2` is not one of
`2h'+1,2h'+2` for `h'>=4`; when `h=h'+3`, the two missing coordinates
`h'+2,h'+3` are likewise not the two high active labels.  Thus equality is
again impossible.

It remains to take `h'=h-1`.  Put

\[
 B=(L_h-\{h+1\}).
\]

Then `L_{h-1}=B+{2h+1}`.  The five active triples in `g(Z_h^i)` show that
only

\[
 g(Z_h^0)=B+\{1,2,2h+1\}=Z_{h-1}^1
\]

matches one of the five active pairs over `L_{h-1}`.  This is (3.1).
Taking complements completes the proof. \(\square\)

The `P` endpoints are mutually distinct because `g` is a bijection and the
exchange states are distinct; the `Q` endpoints are mutually distinct for
the same reason.

### Corollary 3.2 (degree-three obstruction)

After the simultaneous head shifts, the role-zero edges are

\[
 U_hU_{h+1}\qquad(4\le h<H).
\tag{3.3}
\]

They form the height spine.  At the owner `U_h`, the two spine edges already
use both factor degrees.  An independent synchronized collar ending at
`P_{h,0}=U_h` would add a third protected edge.  Therefore the all-five
collar bank is not a protected path forest.

There is a tempting first-edge fusion.  From `U_h` to `U_{h-1}` one deletes
`2h-1 in G_h` and inserts `h in Omega\G_h`, so this edge can be the first
sliding-window step of the height-`h` role-zero collar.  It cannot be
continued: `U_{h-1}` is already incident with both neighbouring spine
edges.  Adding the second collar step again creates degree three.

## 4. The naive zero-arc cancellation is false

Before the head shifts, the two consecutive cut edges at `U_h` form the
three-owner segment

\[
 P_{h-1,1},\ U_h,\ Q_{h,0}.
\tag{4.1}
\]

After the shifts, the corresponding spine segment is

\[
 U_{h-1},\ U_h,\ U_{h+1}.
\tag{4.2}
\]

Their union values are not equal.  Indeed,

\[
 \begin{aligned}
 (P_{h-1,1}\cup U_h\cup Q_{h,0})^c
   &=A_h\setminus\{1,h\},\\
 (U_{h-1}\cup U_h\cup U_{h+1})^c
   &=A_h\setminus\{h,2h+1\}.
 \end{aligned}
\tag{4.3}
\]

Thus, writing

\[
 Y_h=U_h\cup\{1,h\},
 \qquad \widehat Y_h=U_h\cup\{h,2h+1\},
\tag{4.4}
\]

the old zero-arc target is `Y_h` and the new spine target is
`widehat Y_h`.  Both have rank `R+2`, and they differ.

The first identity in (4.3) uses

\[
 g(Z_{h-1}^1)=A_h-\{h\}+\{0\},
 \qquad Z_h^0=A_h-\{1\}+\{h+1\};
\]

the second uses

\[
 A_{h-1}=A_h-\{h\}+\{2h-1\},
 \qquad A_{h+1}=A_h-\{2h+1\}+\{h+1\}.
\]

In particular, the q1 common-deletion identities cannot simply be unioned
edgewise across a zero-length intercut arc.  The targets `Y_h` are distinct:
`A_h\setminus{1,h}` contains `2,...,h-1` and omits `h`, so `h` is recovered
from the set.

## 5. An unconditional five-collar protected forest

Delete the role-zero collar at every high height and retain the collars at
roles `1,2,3,4`.  In addition, put one full-union sliding collar immediately
**after** the old head `Q_{h,0}`.  This outgoing endpoint is not involved in
the overlap (3.2), by Lemma 3.1.  Give these `5(H-4)` paths distinct tags
from `J_H`, with the same missing-tag construction as in Section 2.  The
four incoming collars at one height retain their common exterior ordering;
the outgoing role-zero collar may use an independent ordering.

### Theorem 5.1 (five-collar forest)

For all sufficiently large `r` in the range

\[
 H=O(\sqrt r),\qquad \delta=O(\sqrt r),
\]

the old pentagon edge bank together with the five collars just described at
every high height is an incidence path forest.  The same is true after all
head shifts.

#### Proof

Lemma 3.1 says that the only cross-height endpoint overlaps are the
role-zero/role-one height-spine overlaps.  At every `P_{h,i}`, `i=1,2,3,4`,
the incoming collar edge and the corresponding old (or new) pentagon edge
give degree two.  Role-zero tails receive no incoming collar.  Every
`Q_{h,0}` receives its outgoing collar and is otherwise incident only with
its pentagon edge.  The role-zero overlaps form a path, not a cycle; every
other pentagon edge is extended only at its declared free endpoint.

The missing-tag signatures separate all positive collar owners and lower
colours from one another and from the pentagon bank.  Within one collar,
simplicity is the corrected sliding-window lemma.  Hence the combined bank
is 2-bounded and acyclic on both shores. \(\square\)

For one high pentagon the five collars and five pentagon edges contribute

\[
 2\bigl(5(r+3)+5\bigr)=10(r+4)
\tag{5.1}
\]

incidence edges.  The proof-safe exposures are

\[
 \alpha\le85(H-4)+O(1),
 \qquad
 \beta\le30(H-4)+O(1).
\tag{5.2}
\]

Thus the bank has `e=O(Hr)=O(r^(3/2))` and
`alpha,beta=O(sqrt r)`, and the polynomial protected-factor theorem extends
it to an **uncoloured spanning two-factor**.

This last adjective is load-bearing: that theorem does not by itself make
all prescribed PBBS head edges one globally compatible directed matching,
nor does it control how the protected path components are joined.

## 6. Exact, prospective residual upper-current census

Assume now that a direction-compatible old factor contains the five-collar
bank, with each collar immediately before its declared tail.  Choose the
first common exterior coordinate outside every one of the five screen
unions.  Then every nontrivial current described below has excess rank at
least two.

Let `L=r+3` be the collar length parameter.  The head shift sends old role
`j` to the incoming profile at role `j-1`.  Roles `1,2,3,4` have the same
common-excess profile.  Role zero has only its endpoint before the preceding
cut.  Therefore the common-excess bijection leaves only:

1. old one-cut intervals at role `j=1` whose incoming penetration is at
   least two owners; and
2. old intervals crossing the two adjacent cuts at a zero arc `U_h`.

Every interval crossing at least three cuts contains an entire positive-
length intercut arc.  That arc contains a full-union collar, so the target
is `Omega`.  The same is true for a two-cut interval not using a zero arc.

The role-one outgoing arc is itself the zero arc ending at the next
role-zero tail, so item 1 is completely determined by the protected
incoming collar.  In item 2, the protected incoming collar at
`P_{h-1,1}` and the protected outgoing collar at `Q_{h,0}` determine both
exterior penetrations.  Once either complete collar is included, the value
is `Omega`.  Hence the whole residual target family is fixed **before** the
unprotected factor is completed.

For a fixed incoming penetration `u`, the outgoing prefix unions in the
zero-arc bank are nested as their depth varies.  At any fixed target rank,
a nested family contains at most one set.  There are at most `L` non-full
incoming depths.
Consequently, if `mathcal D_s` is the set of all residual targets of rank
`R+s`, then

\[
 \boxed{|\mathcal D_s|\le 2(H-4)L+O(1)}
 \qquad(2\le s\le R-1).
\tag{6.1}
\]

The first term pays the unmatched role-one one-cut bank and the second the
zero-arc two-cut bank.  Equation (4.4) shows that the latter bank is
genuinely nonempty before alternative witnesses are credited.

Thus the failure of the all-five collar is not an arbitrary exponential
exterior tensor.  It is a rank-stratified polynomial leave with

\[
 \max_s|\mathcal D_s|=O(HR)=O(R^{3/2}),
 \qquad
 \sum_s|\mathcal D_s|=O(HR^2)=O(R^{5/2}).
\tag{6.2}
\]

## 7. A general rank-stratified backup-packing theorem

The next theorem is independent of PBBS.

### Theorem 7.1 (polynomial upper backups with sub-half exposure)

Work in the balanced middle-level incidence graph on a ground set of size
`2R-1`.  Let `P_0` be a protected incidence path forest satisfying

\[
 |V(P_0)|=O(M),
 \qquad \alpha(P_0),\beta(P_0)=o(R).
\tag{7.1}
\]

Let `mathcal D_s` be literal upper targets of rank `R+s`, where

\[
 2\le s\le R-1,
 \qquad |\mathcal D_s|\le M,
 \qquad M=O(R^{3/2}).
\tag{7.2}
\]

Then, for all sufficiently large `R`, one can choose one owner-path witness
for every target in `union_s mathcal D_s` such that

* the witnesses are mutually vertex-disjoint and avoid `P_0`;
* every witness has literal owner union equal to its target;
* their union with `P_0` is an incidence path forest;
* the combined exposure satisfies

  \[
  \alpha,\beta\le R/3;
  \tag{7.3}
  \]

* the total protected incidence size is polynomial, in fact

  \[
  e=O(MR^2).
  \tag{7.4}
  \]

Consequently the combined bank extends to a spanning two-factor by the
polynomial protected-factor theorem.

#### Proof

Fix `Z in mathcal D_s`.  Partition

\[
 Z=C\mathbin{\dot\cup}A\mathbin{\dot\cup}B,
 \qquad |C|=R-s,quad |A|=|B|=s,
\]

and write `A={a_1,...,a_s}`, `B={b_1,...,b_s}`.  The owners

\[
 V_i=C\cup\{b_1,\ldots,b_i\}
          \cup\{a_{i+1},\ldots,a_s\},
 \qquad 0\le i\le s,
\tag{7.5}
\]

form a simple Johnson path.  Its `s` lower colours are distinct and

\[
 \bigcup_{i=0}^sV_i=Z.
\tag{7.6}
\]

Choose witnesses in increasing order of `s`.  Before choosing a target in
stratum `s`, let `Q_R,Q_(R-1)` be the owner and lower-colour vertices already
used.  The number of such vertices is at most

\[
 |Q_R|,|Q_{R-1}|\le C_0M(s+1)^2.
\tag{7.7}
\]

Apply a uniformly random permutation of `Z` to (7.5).  The probability of
hitting the forbidden bank is at most

\[
 \varepsilon_s
 \le
 { (s+1)|Q_R|\over {R+s\choose R}}
 +{ s|Q_{R-1}|\over {R+s\choose R-1}}.
\tag{7.8}
\]

For `s=2`, this is `O(M/R^2)=O(R^(-1/2))`.  For each fixed
`3<=s<=7` it is smaller.  For `s>=8`, the denominators are at least of
orders `R^8` and `R^9`, while the numerator is `O(MR^3)=O(R^(9/2))`.
Thus

\[
                         \sup_s\varepsilon_s=o(1).
\tag{7.9}
\]

There is always an avoiding permutation.  Choose uniformly from the
avoiding permutations and continue.  This proves disjointness.

It remains to control exposures.  Fix a rank-`R-1` vertex `x`.  Under an
unconditioned random permutation of `Z`, the probability that the path has
an owner containing `x` is at most

\[
 a_s={ (s+1)^2\over {R+s\choose R}}.
\tag{7.10}
\]

Moreover one path has at most two owners containing `x`, because
nonconsecutive owners in (7.5) intersect in rank at most `R-2`.

Fix instead a rank-`R` owner `U`.  The probability that the path has a
lower colour contained in `U` is at most

\[
 b_s={sR\over {R+s\choose R-1}},
\tag{7.11}
\]

and at most two path lower colours can be contained in `U`: nonconsecutive
lower colours have union rank at least `R+1`.

Conditioning on avoidance multiplies (7.10)--(7.11) by at most
`1/(1-epsilon_s)=1+o(1)`.  Therefore, for every fixed star, the sum of the
conditional hit probabilities over all tasks is

\[
 \begin{aligned}
 \mu_\alpha
 &\le(1+o(1))M\sum_{s=2}^{R-1}
       {(s+1)^2\over {R+s\choose R}}
   =O(M/R^2)=o(1),\\
 \mu_\beta
 &\le(1+o(1))M\sum_{s=2}^{R-1}
       {sR\over {R+s\choose R-1}}
   =O(M/R^2)=o(1).
 \end{aligned}
\tag{7.12}

For adapted Bernoulli trials with conditional probabilities bounded by
`p_j`, the standard exponential-moment proof gives

\[
 \Pr\!\left(\sum I_j\ge q\right)
 \le\left({e\sum p_j\over q}\right)^q.
\tag{7.13}

Since one task contributes at most two units to either exposure, an
exposure of `R/4` requires at least `R/8` hit tasks.  Equations
(7.12)--(7.13) make the probability for one star

\[
                         \exp(-\Omega(R\log R)).
\tag{7.14}

There are fewer than `2^(2R)` stars on each shore.  A union bound therefore
shows that, with positive probability, every backup exposure is at most
`R/4`.  Adding (7.1) gives (7.3) for large `R`.

Finally, each target in stratum `s` uses `2s` protected incidence edges.
Summing `|mathcal D_s|<=M` over `s` gives (7.4).  The bank is a path forest,
has polynomial size, and has both exposures below half by a fixed linear
margin, so the polynomial protected-factor theorem applies. \(\square\)

## 8. PBBS consequence and exact remaining gate

Apply Theorem 7.1 with

\[
 M=2(H-4)(r+3)+O(1)=O(R^{3/2})
\]

and with `P_0` equal to the five-collar pentagon forest from Theorem 5.1.
Equations (6.1)--(6.2) supply the target census.  Hence the complete
prospectively named residual upper bank has simultaneous protected
alternative witnesses in one **uncoloured** owner/`q1` two-factor.  The
extra outgoing collars are what make this application quantifier-correct:
without them the zero-arc targets would depend on the subsequently chosen
unprotected outgoing arcs, and re-completing the factor after naming the
backups could change the target bank.

This is not yet the PBBS correlated planting theorem.  Four rows remain:

1. **Directed/coloured completion.**  The protected extension theorem does
   not guarantee that every declared `P--Q` edge lies in one compatible
   matching orientation, or that all collar directions agree after the
   protected components are joined.
2. **Clipped residence.**  The sliding collars have correct internal runs
   but export boundary-age flags.  The uncoloured factor completion does not
   absorb them.
3. **One literal source history.**  Owner residence on the protected pieces
   does not imply a single depth-`delta` antecedent for the completed factor,
   nor the rank-three common histories required by lower-cell transport.
4. **Typed cap.**  Target-valued owner paths do not provide the
   occurrence/phase-labelled, capacity-disjoint routes of the common cap.

There is nevertheless no *additional* cap matching created by the upper
backup bank once a terminal antecedent exists.  If one directed component
has source letters `A_j` and owners

\[
 T_j=\bigcup_{q=0}^{\delta}A_{j+q},
\]

then every protected backup path

\[
 T_i,T_{i+1},\ldots,T_{i+s}
\]

lifts to the source interval

\[
 A_i,A_{i+1},\ldots,A_{i+\delta+s},
\]

with exactly the same union value.  Different target values give different
source occurrences automatically.  Thus the backups are a cap-passive
**upper protected minor** after the antecedent is fixed.  What they do not
supply is the antecedent itself, the strict-lower common-history cell map,
or the private typed suffix rank required by the regular factor-router
theorem.  An abstract two-factor cannot be promoted to that router merely
because these upper minors are disjoint.

Thus cross-pentagon collar interiors, the exact endpoint obstruction, the
entire residual upper-target census, and its graph-level backup/factor
packing are now settled.  The surviving obstruction is genuinely the
correlated directed source/cap realization, not owner supply or
set-theoretic upper coverage.

## 9. Dependencies and scope

Used:

* `MATH_THEOREM_PBBS_AH_LADDER_PENTAGON_RETURN_20260805.md`;
* `MATH_THEOREM_PBBS_HEIGHT_PENTAGON_FORCED_Q1_AND_RIGHT_RAY_REGENERATION_20260805.md`;
* `MATH_THEOREM_PBBS_SYNCHRONIZED_INCOMING_COLLAR_CANCELS_COMPLETE_UPPER_CURRENT_20260805.md`;
* `MATH_THEOREM_PBBS_GLOBAL_TAG_RESERVOIR_PLANTS_SYNCHRONIZED_COLLARS_20260806.md`;
* `MATH_THEOREM_POLYNOMIAL_PROTECTED_FOREST_EXTENSION_FROM_TWO_EXPOSURES_20260805.md`.

Not used: a solver, a finite census, or an unproved assertion that an
uncoloured protected factor is automatically a PBBS/source/cap factor.
