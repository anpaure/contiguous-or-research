# Boolean interval geometry for the upper occurrence section:
# a polynomial dependency bound, a logarithmic-redundancy LLL, and the
# literal six-cycle obstruction

**Date:** 2026-08-04  
**Scope:** pure occurrence-labelled Johnson-cycle mathematics  
**Status:** unconditional sufficient theorem for a concrete factor class
and an unconditional Boolean local obstruction.  No all-parameter factor,
resident source, compiler, or `B+1` word is claimed.

## 0. Outcome

Let `F` be a directed cycle cover on rank-`m` Boolean owners, and colour an
edge by the rank-`(m+1)` union of its two ends.  The earlier product-measure
theorem reduces the retained-old upper gate to a blocker LLL, but leaves its
literal dependency degree as a host hypothesis.

For Boolean interval witnesses that dependency is automatically
polynomial.  A fixed physical edge belongs to at most `q` directed
`q`-edge intervals.  Consequently one q1 colour of multiplicity at most
`M` occurs in the bad-event scope of at most

\[
 M S_m,
 \qquad
 S_m=\sum_{q=2}^{m-1}q={m(m-1)\over2}-1,             \tag{0.1}
\]

higher targets.  This turns the abstract blocker LLL into the following
explicit Boolean host theorem.

* If every higher target is either already witnessed using only
  deterministic q1 colours, or has `t=Theta(log m)` geodesic witnesses with
  pairwise-disjoint **random-colour** scopes, each using at most a fixed
  number `A` of repeated colours;
* if every q1 colour has bounded multiplicity `M`; and
* if either every factor component has `Theta(log m)` independent breaker
  edges or the complete menu envelope leaves a capacitated private reserve
  edge in every component,

then one occurrence section simultaneously retains one witness of every
higher target and breaks every old cycle.  Hence it is an upper-exact
all-width rooted forest.

For fixed `A,M`, logarithmic redundancy is enough for the vulnerable
targets because their failure probability is `m^{-Omega(1)}`, whereas the
exact Boolean dependency degree is only `O(m^2 log m)`.

There is a necessary low-width correction.  A cycle cover has at most `W`
geodesic windows of any fixed width.  At q2,

\[
 {W\over {2m-1\choose m+2}}
 ={(m+1)(m+2)\over(m-1)(m-2)}<2\qquad(m\ge9).       \tag{0.2}
\]

Thus every q2 target cannot have two witnesses, let alone logarithmically
many.  The nonvacuous theorem is the **hybrid** form: almost every low-width
target must have a deterministic-safe witness, and only a small vulnerable
leave receives logarithmic witness menus.

Boolean geometry does **not** make compatibility automatic.  For every
`m>=4` there is a literal six-cycle in `J(2m-1,m)` with adjacent equal q1
colours and two distinct rank-`(m+2)` targets whose unique admissible old
witnesses force the two different occurrences.  Each target is separately
feasible and every occurrence section breaks the cycle, but no section
retains both.  The abstract four-cycle word `R,A,R,B` is itself
Boolean-impossible; six edges are enough for the obstruction.

Thus the positive target is now quantitative and the negative boundary is
literal:

\[
 \boxed{\text{bounded repeated-colour load}
       +\text{logarithmic colour-disjoint witness diversity}}
                                                               \tag{0.3}
\]

is a sufficient upper host class, while individual Boolean witness
feasibility is not.

## 1. Boolean factor and random coordinates

Let

\[
                         \Omega=[2m-1],
 \qquad                  \mathcal O={\Omega\choose m}.            \tag{1.1}
\]

Let `F` be a directed cycle cover on `mathcal O` using Johnson edges.  For
an occurrence `e=UV`, put

\[
                         u(e)=U\cup V\in{\Omega\choose m+1}.       \tag{1.2}
\]

Assume `u` is surjective.  Write

\[
 E_R=u^{-1}(R),\qquad \mu_R=|E_R|,\qquad b_R=\mu_R-1.              \tag{1.3}
\]

Fix a rainbow protected bank `P`.  As usual, its occurrence domain is

\[
 \Omega_R^P=
 \begin{cases}
  \{p\},&P\cap E_R=\{p\},\\
  E_R,&P\cap E_R=\varnothing.
 \end{cases}                                                       \tag{1.4}
\]

Call `R` **random** when `|Omega_R^P|>=2`; otherwise its occurrence
coordinate is deterministic.  Independently and uniformly sample

\[
                         a_R\in\Omega_R^P.                          \tag{1.5}
\]

Assume throughout the positive theorem that

\[
                         \mu_R\le M                                \tag{1.6}
\]

for every q1 colour, where `M>=2`.

For a proper higher target `X` of rank `m+q`, a **geodesic witness** is a
directed cyclic interval of exactly `q` edges whose owner union is `X`.
It is admissible when it contains at most one occurrence of each q1 colour
and agrees with every protected domain in (1.4).  Its random scope is

\[
 S^+(I)=\{R:\ |\Omega_R^P|\ge2,
                 I\text{ uses an occurrence of }R\}.               \tag{1.7}
\]

Deterministic colours are deliberately omitted from (1.7).  They create no
probabilistic dependency once admissibility has been checked.

## 2. The Boolean interval-incidence bound

### Lemma 2.1 (one edge has only `q` positions)

Let `e` be an edge of a directed cycle of length `ell`.  For
`1<=q<ell`, exactly `q` directed `q`-edge cyclic intervals contain `e`.
For a directed path the number is at most `q`.

#### Proof

In a cyclic interval containing `e`, the edge `e` may occupy positions
`1,...,q`, and its position determines the start uniquely.  On a path some
of these starts may cross a boundary.  \(\square\)

Only simple proper intervals are used below; a full cyclic traversal cannot
survive any cycle-breaking occurrence section.

### Lemma 2.2 (one colour meets only polynomially many target events)

Choose an arbitrary restricted family of geodesic witnesses for every
higher target.  For a fixed q1 colour `R`, the number of distinct targets
having at least one chosen witness whose random scope contains `R` is at
most

\[
                         \mu_R S_m,
 \qquad S_m={m(m-1)\over2}-1.                        \tag{2.1}
\]

#### Proof

Fix one occurrence `e in E_R`.  At rank `m+q`, every chosen geodesic
witness containing `e` is a directed `q`-edge interval.  By Lemma 2.1 there
are at most `q` such intervals.  One interval has one fixed owner union, so
it contributes to at most one target.  Sum over `2<=q<=m-1` and then over
the `mu_R` occurrences.  Repeated counting of one target only enlarges the
bound.  \(\square\)

The estimate is independent of the total central width
`binom(2m-1,m)`.  This is the useful Boolean input absent from the abstract
occurrence-section theorem.

## 3. A joint target-and-component blocker LLL

Fix integers `t,s>=1` and `A>=0`.  Assume the following menus have been
declared.

1. For every proper higher target `X`, choose exactly `t` admissible
   geodesic witnesses
   
   \[
                          \mathcal L_X=\{I_{X,1},...,I_{X,t}\}       \tag{3.1}
   \]
   
   whose random scopes are pairwise disjoint and satisfy
   
   \[
                          |S^+(I_{X,j})|\le A.                       \tag{3.2}
   \]

2. A factor component containing two occurrences of one q1 colour is
   called **automatically broken**: one occurrence section can never keep
   both.  In every other component `K`, choose a breaker bank `Z_K` of
   exactly `s` edges whose colours are random.  Since such a component is
   q1-rainbow, these `s` colours are distinct.

Put

\[
 S_m={m(m-1)\over2}-1,
 \qquad B=\max\{At,s\},                              \tag{3.3}
\]

and

\[
 p=\max\left\{(1-M^{-A})^t, 2^{-s}\right\}.         \tag{3.4}
\]

### Theorem 3.1 (Boolean interval blocker LLL)

If

\[
 \boxed{
 e\,p\,B M(S_m+1)\le1,}                             \tag{3.5}
\]

then there is an occurrence section which

* contains `P`;
* keeps exactly one occurrence of every q1 colour;
* retains one chosen old interval witness of every proper higher target;
  and
* omits an edge of every component of `F`.

Its selected edge set is therefore an upper-exact all-width directed path
forest.

#### Proof

For a chosen admissible witness `I`, uniform sampling gives

\[
 \Pr(I\text{ is retained})
   =\prod_{R\in S^+(I)}{1\over|\Omega_R^P|}
   \ge M^{-A}.                                       \tag{3.6}
\]

The `t` witness events for one target are independent because their random
scopes are disjoint.  Hence the target-failure event `B_X` has

\[
                         \Pr(B_X)\le(1-M^{-A})^t.     \tag{3.7}
\]

For a nonautomatic component `K`, let `C_K` be the event that every edge
of `Z_K` is selected.  The breaker colours are distinct random variables,
so

\[
                         \Pr(C_K)
  =\prod_{e\in Z_K}{1\over|\Omega_{u(e)}^P|}
  \le2^{-s}.                                         \tag{3.8}
\]

Avoiding `C_K` omits an edge of `Z_K` and therefore breaks `K`.

Use the variable-dependency graph: two bad events are adjacent when they
share a random q1 colour.  Lemma 2.2 says one colour lies in at most
`mu_R S_m` target-event scopes.  It lies in breaker banks of at most
`mu_R` components, because each physical occurrence belongs to one
component.  Thus every random colour lies in at most

\[
                         \mu_R(S_m+1)\le M(S_m+1)     \tag{3.9}
\]

bad-event scopes.  Every target event uses at most `At` variables and every
component event uses `s`; therefore the dependency degree is at most

\[
                         \Delta\le BM(S_m+1)-1.       \tag{3.10}
\]

Equations (3.4)--(3.5) are exactly the symmetric Lovasz local lemma
condition `e p (Delta+1)<=1`.  Avoiding all target events retains a witness
of every target.  Automatic components are broken under every section, and
avoiding the remaining component events breaks every other component.
The occurrence section itself keeps exactly one edge of each q1 colour and
the domains force `P`.  A proper subset of every directed cycle is a path
forest.  \(\square\)

### Corollary 3.2 (fixed multiplicity and fixed local load)

Fix `A` and `M`.  For all sufficiently large `m`, Theorem 3.1 applies with

\[
 t=\left\lceil6M^A\log m\right\rceil,
 \qquad
 s=\left\lceil{6\log m\over\log2}\right\rceil.      \tag{3.11}
\]

#### Proof

Using `1-x<=e^{-x}`,

\[
 (1-M^{-A})^t\le m^{-6},
 \qquad 2^{-s}\le m^{-6}.                            \tag{3.12}
\]

For fixed `A,M`, the factor `BM(S_m+1)` is `O_(A,M)(m^2 log m)`.  Hence
the left side of (3.5) is `O_(A,M)(m^{-4}log m)`, which is below one for
all sufficiently large `m`.  \(\square\)

This corollary is a genuine all-parameter implication for the displayed
factor class.  It does not prove that such menus and breaker banks exist in
the PBBS, SCD, or protected pivot factors.

The uniform hypothesis is intentionally transparent but is impossible at
the lowest widths once `t>=2`.  The useful nonuniform form follows.

### Corollary 3.3 (deterministic-safe / vulnerable hybrid)

Call a target **deterministic-safe** when it has an admissible geodesic
witness `I` with

\[
                             S^+(I)=\varnothing.      \tag{3.13}
\]

Such a witness is retained by every occurrence section.  Let `mathcal V`
be any remaining vulnerable target family.  If every `X in mathcal V` has
the `t` witnesses of (3.1)--(3.2), every nonautomatic component has the
breaker bank in Item 2, and (3.5) holds, then the conclusion of Theorem 3.1
holds for **all** higher targets.

#### Proof

Create bad events only for `X in mathcal V` and for the nonautomatic
components.  Deterministic-safe witnesses require no random coordinate.
Deleting bad events can only decrease every variable load and dependency
degree used in Theorem 3.1.  \(\square\)

### Proposition 3.4 (exact fixed-width menu budget)

Let

\[
                         W={2m-1\choose m},
 \qquad                  N_q={2m-1\choose m+q}.       \tag{3.14}
\]

At one fixed width `q`, suppose every rank-`(m+q)` target receives at least
one geodesic witness and `V_q` of those targets receive `t` witnesses.  Then

\[
                         N_q+(t-1)V_q\le W.           \tag{3.15}
\]

In particular,

\[
 {W\over N_2}={(m+1)(m+2)\over(m-1)(m-2)},           \tag{3.16}
\]

so for `m>=9` a uniform `t>=2` q2 menu is impossible.  More generally,

\[
 {V_2\over N_2}
 \le {6m\over(m-1)(m-2)(t-1)}.                       \tag{3.17}
\]

Thus logarithmic q2 menus can be assigned to at most an
`O(1/(m log m))` fraction of the q2 targets.

#### Proof

Every directed cycle component has at most its edge count many directed
`q`-edge starts, and short components have fewer admissible proper
intervals.  Hence the whole cycle cover has at most `W` geodesic
`q`-windows.  One window has one owner union and cannot serve two different
targets.  The declared menus use at least `N_q+(t-1)V_q` distinct windows,
proving (3.15).

The binomial ratio in (3.16) is direct.  Subtracting one gives

\[
 {W-N_2\over N_2}
 ={(m+1)(m+2)-(m-1)(m-2)\over(m-1)(m-2)}
 ={6m\over(m-1)(m-2)}.                               \tag{3.18}
\]

Combine (3.15) with (3.18).  The ratio in (3.16) is below two exactly for
integer `m>=9`.  \(\square\)

## 4. Target-only LLL plus immutable private reserves

In the hybrid setting, put `mathcal L_X={I_X}` for a chosen
deterministic-safe witness of every target outside `mathcal V`, and retain
the `t`-element menu (3.1) for targets in `mathcal V`.

Let

\[
 A_{\mathcal L}=P\cup
   \bigcup_X\bigcup_{I\in\mathcal L_X}E(I)           \tag{4.1}
\]

be the complete restricted menu envelope.

### Lemma 4.1 (private reserve map implies reserve Hall)

Suppose every component `K` has a designated edge

\[
 d_K\in E(K)-A_{\mathcal L},                         \tag{4.2}
\]

and for every colour `R`, at most `b_R=mu_R-1` of the designated edges have
colour `R`.  Then the immutable reserve Hall inequalities

\[
 |Y|\le
 \sum_{R:N_R^{\rm res}(A_{\mathcal L})\cap Y\ne\varnothing}b_R
 \qquad(Y\subseteq\operatorname {Comp}(F))           \tag{4.3}
\]

hold.

#### Proof

The components in `Y` contribute `|Y|` designated edges.  Group them by
colour.  Every used colour `R` belongs to the sum on the right of (4.3),
because its designated occurrence lies outside `A_L` in a
component of `Y`.  Its group has size at most `b_R`.  Summing the group
bounds proves (4.3).  \(\square\)

### Theorem 4.2 (reserve-decoupled Boolean blocker LLL)

Assume one deterministic-safe witness for every target outside a vulnerable
family `mathcal V`, the target menus (3.1)--(3.2) for every member of
`mathcal V`, the multiplicity bound (1.6), and the private reserve map of
Lemma 4.1.  If

\[
 \boxed{
 e(1-M^{-A})^t\,At\,M S_m\le1,}                     \tag{4.4}
\]

then the same upper-exact all-width rooted forest exists.  In particular,
for fixed `A,M`, `t=ceil(6M^A log m)` suffices for all sufficiently large
`m`.

#### Proof

Run the local lemma only on the vulnerable target-failure events.  Lemma 2.2 now gives
variable load at most `M S_m`, event scope at most `At`, and (4.4) is the
symmetric LLL condition.  The resulting occurrence section supplies a
rainbow witness bank inside `A_L`.  Lemma 4.1 supplies immutable
reserve Hall, so the reserve-extension theorem gives a possibly different
section containing that bank and breaking every component.  The asymptotic
claim follows as in Corollary 3.2.  \(\square\)

The reserve version separates the two hard geometric tasks cleanly:
logarithmically many low-repeat witnesses for every target, and one
capacity-faithful private deletion edge per old component.

## 5. A literal Boolean occurrence-section obstruction

The abstract four-cycle obstruction need not itself be Boolean.  The next
construction is.

Fix `m>=4`.  Choose a set `C` of size `m-2` and five further coordinates
`a,b,c,d,e`, all disjoint.  The remaining `m-4` coordinates of `[2m-1]`,
if any, are unused.  In `J(2m-1,m)` consider the owner cycle

\[
 \begin{aligned}
 V_0&=C+ad,&V_1&=C+ab,&V_2&=C+ac,\\
 V_3&=C+bc,&V_4&=C+ce,&V_5&=C+de.
 \end{aligned}                                       \tag{5.1}
\]

Every consecutive pair, including `V_5,V_0`, intersects in rank `m-1`.
Its six q1 colours are

\[
 C+abd,\qquad
 \underbrace{C+abc}_{R},\qquad
 \underbrace{C+abc}_{R},\qquad
 C+bce,\qquad C+cde,\qquad C+ade.                  \tag{5.2}
\]

Define two rank-`(m+2)` targets

\[
                         X=C+abcd,
 \qquad                  Y=C+abce.                   \tag{5.3}
\]

### Theorem 5.1 (Boolean six-cycle forced-occurrence no-go)

On the cycle (5.1), `X` has exactly one admissible old interval witness,
namely `V_0,V_1,V_2`, and `Y` has exactly one, namely
`V_2,V_3,V_4`.  The first forces the first occurrence of `R` in (5.2), and
the second forces the second occurrence.  Hence no occurrence section
retains both targets.

Each target separately has an occurrence section retaining it, and every
occurrence section breaks the cycle.

#### Proof

The six directed two-edge interval unions are

\[
 C+abcd,\qquad C+abc,\qquad C+abce,\qquad
 C+bcde,\qquad C+acde,\qquad C+abde.               \tag{5.4}
\]

The five rank-`(m+2)` values in (5.4) are distinct.  Thus the displayed
two-edge witnesses of `X` and `Y` are unique at minimum width.

The only longer block of owners contained in `X` extends its displayed
witness through `V_3`; it uses both consecutive `R` occurrences and is not
admissible.  Any interval extending in the other direction contains `e`
and has union not contained in `X`.  The same argument for `Y` uses the
block `V_1,V_2,V_3,V_4`: its longer extension also contains both `R`
occurrences, while extension through `V_0` or `V_5` introduces `d`.
Therefore the two displayed witnesses are the unique admissible witnesses
at every width.

An occurrence section chooses exactly one of the two `R` edges, so it
cannot realize both forced witnesses.  Choosing either one realizes its
corresponding target because all other colours in (5.2) are unique.  The
same choice omits the other `R` edge, and therefore breaks the six-cycle.
\(\square\)

### Proposition 5.2 (why the abstract four-cycle pattern is not Boolean)

There is no rank-`m` Johnson four-cycle whose opposite edge colours are the
same `R` while either intervening edge has a different colour.

#### Proof

If `V_0 union V_1=R=V_2 union V_3`, all four rank-`m` owners are facets of
the rank-`(m+1)` set `R`.  Hence `V_1 union V_2` and `V_3 union V_0` are
rank-`(m+1)` subsets of `R`, so both equal `R`.  \(\square\)

Theorem 5.1 therefore supplies a small literal replacement for the
abstract obstruction.  It is a Boolean cycle component, not a theorem that
this component extends to a complete protected upper-surjective spanning
factor.

## 6. Exact frontier

The upper occurrence-section row has acquired one positive all-parameter
factor class and one sharp Boolean warning.

* A q1 colour has only `O(Mm^2)` target-event incidence, independent of the
  exponential owner count.
* Constant repeated-colour load per witness plus logarithmically many
  random-colour-disjoint witnesses makes every **vulnerable** blocker event
  small enough for the LLL.
* Fixed-width window count forces almost all low-width targets to be
  deterministic-safe; at q2 only an `O(1/(m log m))` fraction can carry
  logarithmic alternative menus.
* Components may be handled either by logarithmically many random breaker
  edges or by an immutable capacitated private reserve map.
* Literal Johnson interval geometry still permits incompatible forced
  occurrences; the six-cycle (5.1) is an explicit example.

To use Theorem 3.1 or 4.2 in the `B+1` construction, one must still build a
single protected resident factor satisfying the stated bounded-multiplicity
and logarithmic-diversity conditions, and co-instantiate it with the lower
source and router.  Neither theorem follows from q1 exactness, upper
surjectivity, residence, or component Hall separately.

The new constructive target is nevertheless substantially more local than
an arbitrary dual join:

\[
 \boxed{
 \begin{array}{c}
 \mu_R=O(1),\\
 \text{each target is deterministic-safe, except a small vulnerable leave},\\
 \text{each vulnerable target has }\Theta(\log m)\text{ witnesses},\\
 \text{each witness meets }O(1)\text{ repeated colours},\\
 \text{and components have logarithmic breakers or private reserves.}
 \end{array}}                                        \tag{6.1}
\]

## 7. Input ledger

The following workspace files were read before this theorem was written.
Hashes name the exact bytes used.

* `MATH_THEOREM_BPLUS1_OCCURRENCE_SECTION_DUAL_JOIN_TREE_RESERVE_HALL_AND_BLOCKER_LLL_20260804.md`  
  `9e329db1beeb6614a7ea43e5e18b72fea9619c2c57882b010d977376b49677b9`
* `MATH_AUDIT_BPLUS1_OCCURRENCE_SECTION_DUAL_JOIN_TREE_RESERVE_HALL_AND_BLOCKER_LLL_INDEPENDENT_20260804.md`  
  `89bdcdde7ea20a36aa2a93fa31b6cab5e646115673c024d87560dfb830c082a8`
* `MATH_THEOREM_BPLUS1_RAINBOW_FOREST_BLOCKER_CSP_AND_MATROID_MINMAX_20260804.md`  
  `e9d32b46c907ef85bf1fb791de57d6d6918fb26746521f91ef876b4d919e4c2e`
* `MATH_THEOREM_BPLUS1_ALLWIDTH_RAINBOW_WITNESS_BANK_AND_SAFE_OPENING_20260803.md`  
  `f44ff6af870e6ef188444193e7c1755bb1441832f3a477a11bc0bda0505d5958`

No finite search, solver, enumeration, or random experiment is used.
