# The weakest double-turn two-factor target and the exact `r=3` `C8` repair

**Date:** 2026-08-05  
**Method:** pure mathematics; no computation, search, or solver

## 0. Outcome

Let `r >= 2`, let `Omega` be a `(2r-1)`-set, and write

\[
 \mathcal L={\Omega\choose r-1},\qquad
 \mathcal M={\Omega\choose r},\qquad
 \mathcal U={\Omega\choose r+1},
\]

\[
 W=|\mathcal L|=|\mathcal M|,qquad
 U=|\mathcal U|,qquad
 C=W-U=\operatorname {Cat}_r.                         \tag{0.1}
\]

Dropping Hamiltonicity from the double-turn problem leaves one exact
coloured-perfect-matching theorem:

> Find a spanning two-factor of `ML(2r-1)` whose upper-turn colours cover
> every member of `mathcal U`.

Lower exactness is automatic because a spanning factor uses every lower
vertex exactly once.  After fixing one incidence perfect matching, the
target is one perfect matching in an `(r-1)`-regular residual graph meeting
every one of `U` canonical colour classes.  Each colour class has exactly
`r+1` edges, and the uniform fractional matching gives it load

\[
 {r+1\over r-1}>1.                                    \tag{0.2}
\]

Thus the two-factor relaxation removes only monodromy.  The generic
perfect-matching formulation retains a genuine integral colour-covering
gate, but the current repository already contains an explicit solution:
the complement of the centered PBBS factor.  Consequently the
double-turn **two-factor exists unconditionally for every `r`**.  The first
remaining Catalan-forest row is only the selection of one occurrence per
upper colour so that the omitted occurrences hit every PBBS component.

For the explicit `r=3` upper-tight Hamilton cycle in the companion GMM
audit, the lower defect is repaired by one support-minimal two-edge switch.
Its literal Middle Levels symmetric difference is one bipartite `C8` with
an old-old/new-new edge pattern, not a standard alternating `C6`.  The
switch splits the owner Hamilton cycle into two 5-cycles,
preserves the entire upper-turn multiset, and makes all ten lower colours
exact.

## 1. Flag normal form

Every Johnson edge `XY` on `mathcal M` determines the Boolean flag

\[
 A=X\cap Y\in\mathcal L,qquad R=X\cup Y\in\mathcal U,qquad A\subset R.
                                                               \tag{1.1}
\]

Conversely, if `A subset R`, then `R setminus A={a,b}` and the flag lifts
to the unique Johnson edge

\[
 \lambda(A,R)=\{A+a,A+b\}.                            \tag{1.2}
\]

### Theorem 1.1 (weakest double-turn two-factor target)

A flag family `F subseteq {(A,R):A subset R}` lifts to a spanning
double-turn two-factor on `mathcal M` if and only if

\[
 d_F(A)=1\qquad(A\in\mathcal L),                     \tag{1.3}
\]

\[
 d_F(R)\ge1\qquad(R\in\mathcal U),                   \tag{1.4}
\]

and every `X in mathcal M` has degree two in the lifted graph
`Lambda(F)`.

It lifts to one double-turn Hamilton cycle if and only if, additionally,
`Lambda(F)` is connected.

#### Proof

Every selected flag contributes one Johnson edge with lower colour `A` and
upper colour `R`.  A spanning Middle Levels two-factor uses every lower
vertex once, giving (1.3); upper-turn surjectivity is (1.4); and the owner
degree row is exactly degree two in `Lambda(F)`.  A finite two-regular
spanning graph is Hamiltonian exactly when it is connected. \(\square\)

Because (1.3) selects `W` flags, (1.4) has total excess

\[
 \sum_{R\in\mathcal U}(d_F(R)-1)=W-U=C.               \tag{1.5}
\]

No path ordering, monodromy, or component bound belongs to the weakest
two-factor statement.

## 2. Paired-perfect-matching normal form

Let `B` be the rank-`(r-1)/r` containment graph with shores
`mathcal L,mathcal M`.  It is `r`-regular on both sides.  Every spanning
two-factor of `B` is the union of two edge-disjoint perfect matchings
`M_0,M_1`.

Write

\[
 f_j:\mathcal L\longrightarrow\mathcal M
\]

for the incidence bijection defined by `M_j`.  At `A in mathcal L`, the
projected Johnson edge is

\[
 f_0(A)f_1(A),
\]

and its upper-turn colour is

\[
 c(A)=f_0(A)\cup f_1(A)\in\mathcal U.                \tag{2.1}
\]

### Theorem 2.1 (single residual matching gate)

Fix any perfect matching `M_0` of `B`.  There is a double-turn two-factor
containing `M_0` if and only if the residual graph `B-M_0` has a perfect
matching `M_1` satisfying

\[
 \{c(A):A\in\mathcal L\}=\mathcal U.                 \tag{2.2}
\]

The components of the lifted factor are the cycles of

\[
 \sigma=f_1^{-1}f_0\quad\hbox{on }\mathcal L.         \tag{2.3}
\]

Thus the Hamilton version adds only the condition that `sigma` is one
cycle.

#### Proof

The matching union has degree two at every vertex of both shores, and every
factor splits into two alternating perfect matchings.  Formula (2.1) is the
turn at `A`.  Two alternating matching steps act by (2.3), so its cycles are
exactly the factor components. \(\square\)

For `R in mathcal U`, define the residual colour class

\[
 \mathcal C_R=
 \{A X\in E(B-M_0): f_0(A)\cup X=R\}.                \tag{2.4}
\]

### Lemma 2.2 (exact colour-class size)

For every `R in mathcal U`,

\[
 |\mathcal C_R|=r+1.                                 \tag{2.5}
\]

#### Proof

For every rank-`r` facet `Y` of `R`, let

\[
 A=f_0^{-1}(Y).
\]

Then `A subset Y subset R`.  The two elements of `R setminus A` produce
the two rank-`r` sets between `A` and `R`: one is `Y`, and call the other
one `X`.  The edge `AX` lies outside `M_0` and has colour `R`.  This gives
one member of `mathcal C_R` for each of the `r+1` facets `Y`.

Conversely, every edge in `mathcal C_R` recovers its facet
`Y=f_0(A)`, so the construction is bijective. \(\square\)

The residual graph is `(r-1)`-regular.  Giving every residual edge weight
`1/(r-1)` satisfies every matching degree equation and gives each colour
class weight

\[
 \sum_{e\in\mathcal C_R}{1\over r-1}
 ={r+1\over r-1}.                                    \tag{2.6}
\]

Hence the generic two-factor target has an exact strictly feasible
fractional colour cover.  This LP observation alone does not round it, but
the PBBS construction below supplies an explicit integral point.

## 2A. The centered PBBS factor closes the two-factor target

Put

\[
 m=r-1,qquad |\Omega|=2m+1=2r-1.
\]

Let `f` be the centered PBBS permutation of

\[
 \mathcal X={\Omega\choose m}.
\]

The audited PBBS angle theorem supplies the Johnson two-factor

\[
 F_m=\bigl\{e_X=\{f^{-1}(X),f(X)\}:X\in\mathcal X\bigr\}       \tag{2.7}
\]

with

\[
 f^{-1}(X)\cup f(X)=X^c,                             \tag{2.8}
\]

and

\[
 \chi(X)=f^{-1}(X)\cap f(X)                         \tag{2.9}
\]

covering every rank-`(m-1)` set, each with multiplicity between one and
three.  Its number of components is at most `Cat_m`.

Complement every owner of `F_m`; call the resulting rank-`(m+1)=r`
two-factor `G_r`.

### Theorem 2.3 (unconditional double-turn two-factor)

For every `r>=3`, `G_r` is a spanning Johnson two-factor on
`binom(Omega,r)` satisfying

\[
 \{A\cap B:AB\in E(G_r)\}={\Omega\choose r-1},       \tag{2.10}
\]

with every colour in (2.10) occurring exactly once, and

\[
 \{A\cup B:AB\in E(G_r)\}={\Omega\choose r+1}.       \tag{2.11}
\]

It therefore lifts to a spanning double-turn two-factor of
`ML(2r-1)`.  It has at most

\[
 \operatorname {Cat}_{r-1}                          \tag{2.12}
\]

components.  Every upper-turn colour has multiplicity between one and
three.  The case `r=2` is the unique six-cycle `ML(3)`.

#### Proof

For the edge `e_X={A,B}` of `F_m`, its complementary edge has

\[
 A^c\cap B^c=(A\cup B)^c=(X^c)^c=X.                 \tag{2.13}
\]

As `X` runs over all rank-`m=r-1` sets, (2.10) is bijective.  Also

\[
 A^c\cup B^c=(A\cap B)^c=\chi(X)^c.                 \tag{2.14}
\]

Angle surjectivity makes these complements cover every rank

\[
 (2m+1)-(m-1)=m+2=r+1
\]

set, proving (2.11).  Complementation preserves degrees and components,
so `G_r` is a spanning two-factor with the PBBS component bound.  Equations
(2.13)--(2.14) also preserve angle multiplicities.  Inserting the unique
rank-`(r-1)` intersection on every edge gives the claimed Middle Levels
factor. \(\square\)

Thus the all-`r` fusion hierarchy begins

\[
 \boxed{
 \text{double-turn two-factor: solved}
 \quad<\quad
 \text{graphic upper transversal: open}
 \quad<\quad
 \text{double-turn Hamilton cycle: open}.}          \tag{2.15}
\]

## 3. The weakest form that already gives a Catalan forest

A double-turn two-factor alone need not yield a linear forest after one
upper occurrence per colour is retained: an entire factor cycle could be
retained.

### Theorem 3.1 (graphic upper-transversal criterion)

Let `G` be a double-turn two-factor.  It contains a spanning upper-exact,
lower-injective `C`-component linear forest if and only if there is a set
`T subseteq E(G)` such that

1. `T` contains exactly one edge of every upper colour in `mathcal U`; and
2. `E(G) setminus T` meets every cycle component of `G`.

#### Proof

The first condition gives `|T|=U` and upper exactness.  Lower colours are
injective on every subgraph of the lifted factor.  A subgraph of a
two-factor is acyclic exactly when at least one edge is omitted from every
factor cycle, which is condition 2.  In that case its spanning version has

\[
 W-U=C
\]

components.  The converse is immediate. \(\square\)

Thus the weakest **fusion** target is Theorem 1.1; the weakest target useful
for Catalan linearization is Theorem 1.1 plus the graphic transversal of
Theorem 3.1.  Hamiltonicity is one sufficient way to make condition 2
automatic, but it is stronger than necessary.

For `G_r`, the fusion target is already supplied by Theorem 2.3.  The
graphic transversal has the following exact capacitated-Hall form.

Let `mathscr K` be the set of cycle components of `G_r`.  For an upper
colour `R`, let `E_R` be its occurrence set and put

\[
 \mu_R=|E_R|\in\{1,2,3\},\qquad q_R=\mu_R-1.          \tag{3.1}
\]

Build the simple bipartite incidence graph `H` between `mathscr K` and the
nonsingleton upper colours, joining `K` to `R` when `K` contains an
occurrence of `R`.  Give colour vertex `R` capacity `q_R`.

For `mathscr S subseteq mathscr K`, put

\[
 n_R(\mathscr S)
 =|\{K\in\mathscr S:K\cap E_R\ne\varnothing\}|.     \tag{3.2}
\]

### Theorem 3.2 (exact PBBS omission-Hall criterion)

The PBBS factor `G_r` has a graphic upper transversal if and only if

\[
 |\mathscr S|
 \le
 \sum_{R\in\mathcal U}\min\{q_R,n_R(\mathscr S)\}
 \qquad(\mathscr S\subseteq\mathscr K).              \tag{3.3}
\]

Equivalently, the cycle vertices of `H` admit a capacitated matching into
the colour vertices, with capacity `q_R` at `R`.

#### Proof

Retaining one occurrence of every colour is equivalent to omitting exactly
`q_R` occurrences of colour `R`.  The retained graph is acyclic exactly
when at least one occurrence is omitted from every factor cycle.

If such omissions exist, choose one omitted occurrence on each cycle.  A
colour `R` is chosen at most `q_R` times, giving the capacitated matching.

Conversely, realize every matched pair `K-R` by one occurrence of `R` on
`K`; occurrences assigned to different cycles are automatically distinct.
For each colour, add arbitrary still-unselected occurrences until exactly
`q_R` have been omitted.  This is possible because at most `q_R` were used
by the matching and `q_R<mu_R`.  The resulting omissions hit every cycle
and leave exactly one occurrence of every colour.

In the simple incidence graph, colour `R` can serve at most one demand
from each incident cycle and at most `q_R` demands in total.  The standard
capacitated matching cut at `R` is therefore
`min(q_R,n_R(mathscr S))`, giving exactly (3.3). \(\square\)

The same target is a standard matroid intersection.  On `E(G_r)`, let
`P` be the partition matroid with blocks `E_R` and capacity one, and let
`M(G_r)` be the graphic matroid.  A graphic upper transversal is exactly a
common independent set of size `U`, necessarily a base of `P`.  Edmonds'
formula gives the equivalent all-subset inequalities

\[
 r_P(A)+r_{M(G_r)}(E(G_r)\setminus A)\ge U
 \qquad(A\subseteq E(G_r)).                          \tag{3.4}
\]

The cycle-capacity form (3.3) is the specialized, smaller min--max theorem.

### Corollary 3.3 (local weighted-repeat sufficient condition)

For a factor cycle `K`, define its **deduplicated weighted repeat mass** by

\[
 \omega(K)=
 \sum_{R:\,K\cap E_R\ne\varnothing}{q_R\over\mu_R}. \tag{3.5}
\]

If

\[
                         \omega(K)\ge1
                         \qquad(K\in\mathscr K),     \tag{3.6}
\]

then `G_r` has a graphic upper transversal.

#### Proof

For `mathscr S subseteq mathscr K`, sum (3.6) over its cycles:

\[
 |\mathscr S|
 \le\sum_R n_R(\mathscr S){q_R\over\mu_R}.
\]

Since `n_R(mathscr S)<=mu_R`,

\[
 n_R(\mathscr S){q_R\over\mu_R}
 \le\min\{q_R,n_R(\mathscr S)\}.
\]

Theorem 3.2 applies.  The sum in (3.5) is over distinct colour incidences,
not occurrences: two occurrences of one colour on the same cycle
contribute only once. \(\square\)

### Corollary 3.4 (uniform two-repeat sufficient condition)

If every component of `G_r` is incident with at least two **distinct**
nonsingleton upper colours, then a graphic upper transversal exists.

#### Proof

Every nonsingleton colour has

\[
 {q_R\over\mu_R}={\mu_R-1\over\mu_R}\ge{1\over2}.
\]

Two distinct such colours on a cycle give `omega(K)>=1`, so Corollary 3.3
applies. \(\square\)

PBBS supplies substantial aggregate room:

\[
 \sum_Rq_R=C=\operatorname {Cat}_r,qquad
 |\mathscr K|\le\operatorname {Cat}_{r-1}<C.          \tag{3.7}
\]

Moreover the number of occurrences belonging to nonsingleton colours is
at least `3C/2` by the audited PBBS multiplicity ledger.  These scalar facts
do not imply (3.3): removable occurrences could in principle avoid one
factor component or concentrate behind a small cycle cut.  The exact new
all-dimensional target is therefore (3.3), the local weighted condition
(3.6), or the concrete two-repeat-per-component condition of Corollary 3.4.

The present PBBS structure theorems do not yet imply (3.6).  Orbit
homomesy proves only that every `f`-orbit has length `ell(2r-1)`, and hence
controls the number and lengths of the `f^{-2}` components.  The
fixed-point theorem proves the global angle multiplicities
`1<=mu_R<=3`.  Neither theorem localizes the nonsingleton colours among
those components.  Thus no componentwise repeat lower bound is silently
being assumed here.

### 3A. Exact relation to the PBBS `q2` Pascal section gate

Before complementation, the same centered PBBS factor has every rank-`r`
edge union exactly once and every rank-`r-2` angle colour between one and
three times.  The direct PBBS Dyck theorem proves more.  If the two factor
edges adjacent at owner `A` have angle colours

\[
 Y^-(A)=f^{-2}(A)\cap A,
 \qquad
 Y^+(A)=A\cap f^2(A),
\]

then

\[
 Y^-(A)\cap Y^+(A)=f^{-2}(A)\cap A\cap f^2(A)       \tag{3.8}
\]

has rank `r-3`, and these values cover every member of
`binom(Omega,r-3)`.

Consequently the unsectioned PBBS factor already supplies the complete
`q1` and `q2` turn decks required by the Pascal route.  Its remaining
section problem is exact and integral: choose one occurrence of every
rank-`r-2` angle colour so that

1. the omitted occurrences hit every PBBS factor cycle; and
2. every rank-`r-3` colour in (3.8) is witnessed at some owner for which
   both adjacent angle occurrences were chosen.

Ignoring condition 2, condition 1 is precisely Theorem 3.2 with the roles
of intersections and unions interchanged.  Thus the omission Hall theorem
is the exact graphic half of the `q2` turn-section gate; adjacent-pair
coverage is the remaining correlated section row.  Complete `q2` coverage
of the full PBBS factor does not imply that a one-occurrence section
preserves it.

## 4. The `r=3` upper-tight counterexample

On `[5]`, start from the upper-surjective Hamilton cycle

\[
 C_+=
 (345,145,245,235,135,134,124,125,123,234).           \tag{4.1}
\]

Its lower-colour sequence is

\[
 45,45,25,35,13,14,12,12,23,34.                      \tag{4.2}
\]

Thus `45` and `12` repeat, while `15` and `24` are missing.  Its upper
colours are the five rank-four sets, each twice.

Remove the two owner edges

\[
 145-245,qquad124-125,                                \tag{4.3}
\]

and add

\[
 145-125,qquad245-124.                                \tag{4.4}
\]

### Theorem 4.1 (one-switch repair)

The switch (4.3)--(4.4) produces the two owner cycles

\[
 (125,123,234,345,145),                               \tag{4.5}
\]

\[
 (245,235,135,134,124).                               \tag{4.6}
\]

Their ten lower colours enumerate `binom([5],2)` exactly once, and their
upper colours are unchanged from `C_+`, hence every rank-four colour occurs
twice.  Therefore their incidence lifts form a double-turn spanning
two-factor of `ML(5)`.

#### Proof

The removed edges have lower colours `45,12`; the added edges have lower
colours

\[
 145\cap125=15,qquad245\cap124=24.                   \tag{4.7}
\]

This replaces exactly the two surplus occurrences in (4.2) by the two
missing colours.  All four old and new owner edges have the same upper
colour:

\[
 145\cup245=124\cup125=145\cup125=245\cup124=1245.    \tag{4.8}
\]

Thus the full upper multiset is unchanged.  Cutting (4.3) and reconnecting
as in (4.4) gives exactly the cycles (4.5)--(4.6). \(\square\)

## 5. Why the repair is a `C8` surgery, not a `C6` factor exchange

Lift the two removed owner edges through their old lower colours and the
two added owner edges through their new lower colours.  Their symmetric
difference is the bipartite incidence cycle

\[
 145-45-245-24-124-12-125-15-145.                    \tag{5.1}
\]

This is an octahedral-square `C8`: on the four active labels
`5,4,2,1`, its lower vertices are

\[
 45,24,12,15.
\]

Around (5.1), the edge-status word is

\[
 \mathrm{old},\mathrm{old},\mathrm{new},\mathrm{new},
 \mathrm{old},\mathrm{old},\mathrm{new},\mathrm{new}.          \tag{5.2}
\]

Thus this is not an alternating perfect-matching flip.  It replaces two
old length-two paths through the duplicated lower colours by two new
length-two paths through the missing lower colours; this is exactly
(4.3)--(4.4).

The starting cycle `C_+` is not the projection of a spanning Middle Levels
factor: lower vertices `45,12` would have degree four in its naive lift and
`15,24` degree zero.  Therefore a standard alternating `C6` **factor
exchange is not even defined on this source state**; those exchanges start
and end inside the perfect-matching/two-factor fibre.

Moreover, among repairs which leave every other owner adjacency fixed, two
projected edges must be removed (one from each repeated lower colour) and
two must be inserted (one for each missing lower colour).  Their whole
incidence lifts have four old and four new edges, so (5.1) is the
support-minimal literal defect repair.  It cannot be represented by one
standard incidence `C6` factor exchange.

There is also a direct support obstruction: the lower-degree correction is
nonzero at the four distinct vertices

\[
 45,12,15,24.                                                 \tag{5.3}
\]

A Boolean-incidence `C6` has only three vertices on the lower shore.
Consequently no surgery supported on one literal `C6`, under any choice of
old/new status and with all exterior incidences fixed, can perform this
four-vertex correction.

This does not assert that no more global rethreading of the augmented
rank-`3/4` tight enumeration, informally also called a “hexagon move”, could
reach some other double-turn Hamilton cycle.  It gives the proof-safe
answer for the standard factor-exchange meaning: the exact local repair is
one `C8`, and it naturally lands in a two-factor rather than one cycle.

## 6. Conclusion

Dropping Hamiltonicity exposes the shortest same-edge fusion object:

\[
 \boxed{
 \begin{gathered}
 \text{two edge-disjoint perfect matchings of `ML(2r-1)`}\\
 \text{whose `W` lower turns cover all `U` upper colours.}
 \end{gathered}}                                               \tag{6.1}
\]

Equivalently, after fixing one matching, find one residual perfect matching
meeting every canonical `(r+1)`-edge colour class.  No component or
monodromy condition remains.  The complemented centered PBBS construction
proves that this target exists for every `r`.  To obtain the Catalan forest,
add only the graphic-transversal condition of Theorem 3.1, equivalently the
capacitated Hall system (3.3).  Corollary 3.3 gives the sharper local
weighted-repeat sufficient condition, and Corollary 3.4 reduces it further
to the concrete assertion that every PBBS component meets two distinct
nonsingleton angle colours.

The `r=3` fixture confirms that this relaxation is real: the defective
upper-tight Hamilton order enters the exact two-factor fibre by one
support-minimal `C8` repair.
