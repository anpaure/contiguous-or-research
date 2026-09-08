# Independent fillers factor the residence gate, but sealed filler ancestry cannot regenerate

Date: 2026-07-31  
Status: exact all-parameter residence factorization, exact symmetry and
finite-bank obstruction, guard-jump reduction, and one independently
replayed `n=5` filler substitution.  No all-parameter guarded-filler supply,
DERF, deep-shadow, or compiler theorem is claimed.

## 0. Result

The independent-`c`-rail theorem has a stronger consequence than palette
substitution, but a weaker one than automatic guarded induction.

1. **Residence factors exactly.**  For every guard width `h`, the complete
   internal residence predicate of the two-parent strict lift is the direct
   product of the predicate on the filler `G` and the predicate on the
   structural three-sector support built from `F`.  At `h=3` this is a
   literal factorization of the cubic selected-edge CNF.
2. **A symmetry bank cannot clean a dirty filler.**  Coordinate
   permutations, path permutations and path reversals preserve the two
   run spectra.  Global complementation only exchanges positive and zero
   runs.  Thus rotations of a dirty child, such as those used to audit the
   substitution theorem, prove independence but do not supply a guard.
3. **A finite two-parent bank closed under the same sealed lift is not
   right-total.**  Following the filler parent at every generation exposes
   an induced isolated copy of one seed forest.  Unless a seed (or its
   complement) has no bounded internal positive run at all, its finite run
   survives forever and eventually violates every unbounded deadline
   sequence.
4. **Only guard jumps require external regeneration.**  For a nondecreasing
   guard schedule, an accepted forest itself is a legal filler whenever the
   next guard is unchanged.  At a jump one needs a same-parameter
   palette-preserving promotion to the new guard.  For the deadline schedule
   `h_n=d(2n)+1`, the guards are nondecreasing and have only `O(sqrt(n))`
   jumps through parameter `n`.
5. **The decoupling is useful in a real instance.**  Substituting the known
   residence-clean parameter-five Catalan forest into the authenticated
   structural `n=5 -> 6` lift removes all `44` copied bad cubic windows.
   Both palettes remain exact, the support remains a `132`-path forest, and
   the remaining bad-window count is exactly `100`.  Those `100` clauses
   belong to the structural/seam factor and are not repaired by filler
   substitution.
6. **The ideal escape is nonempty through parameter four.**  Explicit
   Catalan forests of `5` antipodal three-edge geodesics and `14` antipodal
   four-edge geodesics exist at parameters three and four.  Every coordinate
   flips once on every path, so they have no internal positive or zero run
   and are safe for every guard width.

The correct positive target is therefore a **guard-promotion theorem at the
deadline jumps**, not a claim that the independent substitution itself
manufactures `G`.

## 1. Guard radius and the exact product law

Let `G` be a Catalan linear forest on the `n`-subsets of a `2n`-set
`Omega`.  For a path of `G` and a coordinate `x`, read the membership bits
of `x` along that path.  Put

\[
 \rho_+(G)=\min\{\text{length of a positive run bounded strictly inside a
 path}\},                                                   \tag{1.1}
\]

with value `infinity` if there is no such run.  Define `rho_-(G)` by zero
runs, equivalently

\[
                         \rho_-(G)=\rho_+(\overline G).           \tag{1.2}
\]

Call `G` **`h`-safe** when `rho_+(G)>=h`.

Fix structural data `(F,Q,S^-,S^+)` in the strict direct-edgewise lift.
Write `R(F,Q,S^-,S^+)` for the complete support in sectors `0,z,cz`,
including both seam families, and write

\[
 H(F,G)= (c+G)\;\dot\cup\; R(F,Q,S^-,S^+).                       \tag{1.3}
\]

The union is genuinely disjoint: no structural edge or seam is incident
with a `c`-only middle vertex.

### Theorem 1.1 (guard product factorization)

Assume both terms in (1.3) are path forests and the complete lower palette
is injective.  For every `h>=2`,

\[
 H(F,G)\text{ is }h\text{-safe}
 \quad\Longleftrightarrow\quad
 G\text{ is }h\text{-safe and }R(F,Q,S^-,S^+)\text{ is }h\text{-safe}.
                                                               \tag{1.4}
\]

At `h=3`, if `Phi_3` denotes the unified selected-edge cubic residence CNF,
then

\[
 \Phi_3(H(F,G))=\Phi_3(G)\wedge
                 \Phi_3(R(F,Q,S^-,S^+)),                         \tag{1.5}
\]

and the two factors have disjoint variables.  The first factor is true
exactly when `G` contains no three-edge path

\[
 v_0-v_1-v_2-v_3,
 \qquad (v_1\cap v_2)\setminus(v_0\cup v_3)\ne\varnothing.       \tag{1.6}
\]

#### Proof

Every path of `H(F,G)` lies wholly in one of the two terms of (1.3).  For
an old coordinate, its word on `c+G` is its word on `G`; the new coordinate
`c` is constant one and `z` is constant zero.  A constant positive run
touches both path ends and is not internal.  This proves (1.4).

For `h=3`, the unified automaton contributes one clause for each selected
bad three-edge path.  There is no path meeting both summands of (1.3), so
the clause set is their disjoint union.  Every edge of `c+G` is forced;
hence a bad filler triple would reduce its clause to the empty clause, and
absence of such a triple is sufficient by the cubic residence theorem.
This proves (1.5)--(1.6).  `square`

### Corollary 1.2 (Cartesian immediate guarded gate)

At the level of immediate palettes, physical linearity and internal
residence, the feasible set is a Cartesian product:

\[
 \{\text{guarded fillers }G\}\times
 \{\text{guarded structural strict selections }(F,Q,S^-,S^+)\}. \tag{1.7}
\]

Deep-shadow delivery and compiler ownership are not asserted to factor;
they may use windows contributed by both terms and remain part of RSB.

## 2. What coordinate symmetries can and cannot supply

Let `Gamma_n` be generated by permutations of `Omega`, permutations and
reversals of path components, and global complementation.

### Theorem 2.1 (symmetry-bank invariant)

Coordinate and path permutations and path reversals preserve both
`rho_+` and `rho_-`.  Global complementation exchanges them.  Consequently

\[
 \{\rho_+(\gamma G):\gamma\in\Gamma_n\}
       =\{\rho_+(G),\rho_-(G)\}.                              \tag{2.1}
\]

In particular, if both values on the right are below `h`, no symmetry image
of `G` is an `h`-safe filler.

#### Proof

The first three operations only relabel coordinate words or reverse them,
and therefore preserve their run lengths.  Complementation exchanges zero
and one in every word.  `square`

This puts the earlier coordinate-rotation replay in its exact place: it
shows that the rail is physically independent, but it cannot improve the
residence radius of the copied chronology.

There is nevertheless one useful bank consequence.  If `G` is `h`-safe,
then every coordinate permutation of `G` is `h`-safe.  For any
coordinate-equivariant multiset statistic `W_q(G)` of rank-`s` masks—for
example fixed-depth unions or intersections of consecutive vertices—the
uniform permutation orbit satisfies

\[
 {1\over(2n)!}\sum_{\pi\in S_{2n}}
       \mu_{W_q(\pi G)}(A)
   ={ |W_q(G)|\over\binom{2n}s}
       \qquad\left(A\in\binom\Omega s\right).                 \tag{2.2}
\]

This gives uniform **fractional** shadow marginals inside a safe filler
bank.  It does not select one permutation satisfying every integral shadow
or compiler condition.

## 3. The immortal sealed-rail obstruction

Call a family of constructions a **sealed filler recursion** if every new
forest is obtained from `H(F,G)` by operations in `Gamma`, with both parents
drawn from the preceding bank, and no operation internally rethreads the
isolated `c+G` components.

### Theorem 3.1 (finite-bank no-go)

Let `B` be a finite seed bank and suppose

\[
 R(B)=\max_{G\in B}\max\{\rho_+(G),\rho_-(G)\}<\infty.          \tag{3.1}
\]

Every descendant of `B` under a sealed filler recursion has positive guard
radius at most `R(B)`.  Hence such a recursion cannot supply fillers for an
unbounded guard schedule.

#### Proof

Starting at a descendant, repeatedly follow the parent used as its filler.
At each step the entire filler is an induced union of isolated components
in the child.  The chain ends at a seed `G in B`.  After all coordinate
permutations and possible complements, the descendant therefore contains
an isolated copy of either `G` or `bar G`, with every internal run length
unchanged.  Its positive guard radius is at most
`max(rho_+(G),rho_-(G))`, proving the claim.  `square`

### Corollary 3.2 (exact escape routes)

A right-total filler construction must use at least one of the following.

1. A seed with `rho_+=infinity` (or its complement), which is internally
   safe at every guard width.
2. An infinite dimension-indexed supply of genuinely new guarded forests.
3. Infinitely many **regeneration nodes** which rethread every surviving
   sealed ancestry before its finite run becomes illegal.

Adding more structural parents, rotating coordinates, or alternating which
parent is named `F` and which is named `G` does not evade Theorem 3.1: the
filler ancestry is still present.

This is an obstruction to a particular recursive mechanism, not to guarded
Catalan forests.  A forest with no internal positive run at all would defeat
the hypothesis (3.1) and would be an ideal universal filler.

### Theorem 3.3 (antipodal-geodesic characterization)

Let `G` be a Catalan linear forest at parameter `n`, and put
`K=Cat_n`.  The following are equivalent.

1. `rho_+(G)=rho_-(G)=infinity`.
2. Every component of `G` has exactly `n` edges and every ground
   coordinate flips exactly once on that component.
3. Every component is a Johnson geodesic from an `n`-set to its complement.

Any such forest is a universal internal-residence filler for every guard
width.

#### Proof

If a binary coordinate word has at least two transitions, the run between
two consecutive transitions is an internal positive or zero run.  Thus (1)
implies that every coordinate flips at most once on each path.  A path with
`e` Johnson edges has `2e` coordinate flips, so `e<=n`.

A Catalan forest has

\[
 \binom{2n}{n-1}=n\operatorname {Cat}_n=nK             \tag{3.2}
\]

edges in `K` path components.  Since every component has at most `n` edges,
equality forces every one to have `n` edges and every one of the `2n`
coordinates to flip once.  Its endpoints are therefore complements and
the path has minimum possible Johnson length `n`, proving (2)--(3).
Conversely a complement geodesic flips every coordinate once, so every
coordinate word is monotone and has no internal run of either type.
`square`

### Proposition 3.4 (explicit universal fillers at parameters three and four)

At parameter three, the following five paths form an antipodal-geodesic
Catalan forest (vertices are six-bit masks):

```text
13 41 35 50
19 22 14 44
21 28 56 42
25 49 52 38
26 11  7 37
```

They partition all twenty three-sets.  Their fifteen intersections are all
two-sets, their fifteen unions are all four-sets, and every terminal pair is
complementary.  Hence Theorem 3.3 makes this one filler safe for every
future residence width at the parameter-three base.

At parameter four, the following fourteen paths give the next exact case:

```text
 15  30  60 120 240
 29  89  90 114 226
 92  86  54  51 163
 58  27 147 135 197
 23  71  78 204 232
 53  45 108 106 202
102 101  85 149 153
 77 141 142 170 178
 39 166 150 154 216
 99 195 210 212 156
116 180 184 169 139
 46  43  75 201 209
 57 105 225 228 198
 83 113 177 165 172
```

They partition all seventy four-sets, their fifty-six intersections are all
three-sets, and their fifty-six unions are all five-sets.  Every terminal
pair is complementary, so Theorem 3.3 again gives universal residence.

The all-parameter statement

> every parameter admits an antipodal-geodesic Catalan forest

would solve the independent filler-supply problem completely.  It is now
verified at `n=3,4`, not in general.  It is stronger than the jump-localized
promotion target below.

The base certificate is independently replayed by

```text
scratch/audit_catalan_antipodal_geodesic_filler_n3_20260731.py
```

which writes

```text
scratch/catalan_antipodal_geodesic_filler_n3_20260731.audit.json
```

The parameter-four certificate and its independent replay are

```text
scratch/catalan_antipodal_geodesic_filler_n4_20260731.witness.txt
scratch/audit_catalan_antipodal_geodesic_filler_n4_20260731.py
scratch/catalan_antipodal_geodesic_filler_n4_20260731.audit.json
```

The witness was found by exact cover over all `20,160` unoriented
complement geodesics.  One path was fixed without loss because the full
coordinate group is transitive on directed complement geodesics.  The
search source is

```text
scratch/search_catalan_antipodal_geodesic_filler_n4_dlx_20260731.cpp
```

## 4. Guard jumps localize the needed regeneration

Let `(h_n)` be a nondecreasing integer guard schedule.  Suppose a guarded
structural lift theorem is available at width `h_{n+1}` for the three-sector
factor in (1.3).

### Theorem 4.1 (jump-localized filler induction)

Assume an accepted `h_n`-safe Catalan forest is available at parameter `n`.

* If `h_{n+1}=h_n`, it may itself be used as the independent filler.
* If `h_{n+1}>h_n`, it is enough to produce, at parameter `n`, any Catalan
  forest `G_n` which is `h_{n+1}`-safe; it need not be the structural
  parent and need not preserve that parent's direct-incidence data.

Together with an `h_{n+1}`-safe structural factor, the output is
`h_{n+1}`-safe by Theorem 1.1.  Thus same-parameter filler regeneration is
needed only at guard jumps.

The theorem concerns residence plus the immediate forest/palette gate.
For full RSB the promoted filler must also export whatever private shadow
and compiler data are actually consumed from the `c` rail.

### Proposition 4.2 (the deadline schedule has sparse jumps)

For the even deadline sequence put

\[
 W_n=\binom{2n}{n},\qquad
 \Lambda_n=\sum_{s=1}^{n-1}\binom{2n}s
          ={4^n-W_n\over2}-1,                              \tag{4.1}
\]

and

\[
 d_n=\min\left\{d:dW_n+\binom{d+1}2\ge\Lambda_n\right\},
 \qquad h_n=d_n+1.                                         \tag{4.2}
\]

Then `(d_n)` and `(h_n)` are nondecreasing.  Moreover

\[
 d_n={\sqrt{\pi n}\over2}+O(1),                            \tag{4.3}
\]

so there are only `O(sqrt(n))` guard jumps through parameter `n`.

#### Proof

For fixed `d`, divide (4.2) by `W_n`.  The left correction
`binom(d+1,2)/W_n` decreases with `n`.  On the other side,

\[
 {\Lambda_n\over W_n}
 ={1\over2}\left({4^n\over W_n}-1\right)-{1\over W_n}.       \tag{4.4}
\]

The ratio `4^n/W_n` strictly increases because

\[
 {4^{n+1}/W_{n+1}\over4^n/W_n}
 ={2(n+1)\over2n+1}>1,                                    \tag{4.5}
\]

and `-1/W_n` also increases.  Therefore, once a fixed `d` fails, it fails
at every later parameter; the minimum `d_n` is nondecreasing.  Stirling's
formula in (4.4) gives (4.3).  A nondecreasing integer sequence makes at
most `d_n-d_1=O(sqrt(n))` jumps.  `square`

Theorem 4.1 and Proposition 4.2 replace the vague request for a
forever-ahead child by a sharper target:

> **Guard-promotion target.**  At each deadline jump, construct one
> same-parameter exact-palette Catalan forest avoiding all residence motifs
> below the new width; between jumps, propagate the current guard with the
> ordinary joint structural lift.

## 5. Relation to Middle Levels and PBBS constructions

An ordinary Middle Levels Hamilton cycle or PBBS factor does not by itself
supply `G`: the filler must be a Catalan linear forest with both immediate
palettes exact.  The decorated Middle Levels 2-factor theorem would supply
the latter, but the decoration/linearity conditions do not imply the guard
clauses (1.6) or their wider analogues.

The exact sufficient classical target is therefore a **guarded decorated
Middle Levels 2-factor**: its diamond lift must be a Catalan linear forest
and must avoid every `0 1^r 0`, `r<h`, motif on its physical components.
This is a legitimate source of an independent filler, but its all-parameter
existence is not currently a theorem.  The same warning applies to PBBS:
all-depth set coverage is not the exact two-palette plus path-forest plus
residence statement required here.

At `h=3`, the extra condition is precisely the local cubic automaton, so a
factor-supported search may add it without any new global residence state.
This is an encoding reduction, not an existence proof.

There is a sharper classical reduction for the ideal filler of Theorem 3.3.

### Theorem 5.1 (one-rainbow complement-path equivalence)

Antipodal-geodesic Catalan forests at parameter `n` are in bijection with
spanning path factors of the two consecutive Boolean levels

\[
             \binom{[2n]}n\quad\hbox{and}\quad
             \binom{[2n]}{n+1}                              \tag{5.1}
\]

whose components have the form

\[
 X_0\subset Y_0\supset X_1\subset\cdots\subset
 Y_{n-1}\supset X_n=\overline {X_0},                        \tag{5.2}
\]

and whose lower turns

\[
                         X_i\cap X_{i+1}                    \tag{5.3}
\]

enumerate every `(n-1)`-set exactly once.

#### Proof

Given the Catalan forest, insert `Y_i=X_i union X_(i+1)` on every edge.
Its upper palette is exact, so the `Y_i` enumerate level `n+1`; its lower
palette says exactly that (5.3) is bijective.  Theorem 3.3 gives the
complement endpoints and length `n`.

Conversely, project every alternating path (5.2) to its `X`-vertices.
The factor partitions all middle vertices, every union is its distinct
intermediate `Y_i`, and (5.3) is the exact lower palette.  This is an
antipodal-geodesic Catalan forest.  `square`

The canonical MSW/Chung--Feller factor already supplies the complement-path
factor (5.2): it partitions the middle level into `Cat_n` flaw paths and
its `Y_i` enumerate the upper level.  Hence it is automatically universal
for residence.  What it does **not** supply is the lower-turn bijection
(5.3).  The universal filler problem is therefore one additional rainbow
condition on a complement-path factor, rather than a new run-length
problem.

This also explains why the simplest two-parent repair is not yet a theorem.
The canonical factor has the upper rainbow; a complemented conjugate has
the lower rainbow.  Selecting diamonds from their union is the exact
functional-pseudoforest matching problem already audited in
`MATH_THEOREM_CHUNG_FELLER_TWO_PARENT_FUNCTIONAL_PEEL_AND_CONJUGATE_CENSUS_20260731.md`.
The same-frame/dihedral construction fails Hall from parameter four onward
in that finite census, and an arbitrary perfect matching can also destroy
the complement-path topology.  Thus two parents are a meaningful search
space, but not a proved filler supply.

The strongest small case is now exact.  At parameter four, exhaust all
`8!` coordinate conjugates and all `1,162` perfect matchings in the `108`
Hall-perfect two-parent unions.  Exactly two matchings are Catalan linear
forests, but **none** is antipodal-geodesic.  Therefore one arbitrary
conjugated complementary parent does not supply a universal filler at
`n=4`.  This is a no-go for that two-parent family only; it does not exclude
the full complementary-geodesic hypergraph or a larger parent bank.  The
parameter-four certificate in Proposition 3.4 proves that distinction is
load-bearing: the full hypergraph is SAT even though the entire
one-conjugate family contains no solution.

The exhaustive replay is

```text
scratch/audit_catalan_two_parent_antipodal_filler_m4_nogo_20260731.py
```

and writes

```text
scratch/catalan_two_parent_antipodal_filler_m4_nogo_20260731.audit.json
```

The clean all-parameter filler target can now be stated in either of two
equivalent ways:

> rethread a Chung--Feller-type complement path factor so that all lower
> turns are rainbow; or construct an antipodal-geodesic Catalan forest.

Both formulations automatically satisfy every width of the residence
automaton.  Neither existence statement is currently proved.

### Theorem 5.2 (exact complementary-geodesic hypergraph form)

Let `G_n` be the hypergraph whose candidate objects are unoriented
length-`n` Johnson geodesics from an `n`-set to its complement.  A candidate
contains as resources

* its `n+1` middle vertices;
* its `n` consecutive lower intersections; and
* its `n` consecutive upper unions.

Then antipodal-geodesic Catalan forests at parameter `n` are exactly the
perfect resource matchings of `G_n`.

#### Proof

A perfect resource matching uses

\[
 {1\over n+1}\binom{2n}n=\operatorname {Cat}_n            \tag{5.4}
\]

geodesics.  Exact coverage of the first resource class partitions every
middle vertex into those paths; exact coverage of the other two classes is
precisely the lower and upper palette condition.  Conversely every
antipodal-geodesic Catalan forest supplies those three exact partitions.
`square`

The exact regularity theorem already recorded in
`MATH_ATTACK_O2_FIRST_SHADOW_FACTOR_20260724.md` gives every resource the
same candidate degree

\[
                         {n+1\over2}(n!)^2.              \tag{5.5}
\]

Thus uniform weight is a fractional perfect matching.  The filler problem
has no fractional or residence obstruction in this model; the missing row
is an **integral** perfect matching across the three resource classes.
This is a promising independent supply route because it constructs a fresh
universally safe `G_n` at each dimension and therefore bypasses sealed
filler ancestry entirely.  The regularity/fractional solution does not by
itself imply the exact matching.

Proposition 3.4 proves an integral perfect resource matching for `n=3,4`.
The all-parameter matching theorem remains open.

## 6. Exact parameter-five substitution

The residence-clean parameter-five certificate in

```text
scratch/catalan_m5_residence_rethread_c4c6_candidate_20260731.txt
```

is a `42`-path Catalan linear forest on the five-subsets of a ten-set.  It
has both immediate palettes exact and no internal positive run of length
one or two.  Use it as `G` in the authenticated structural `n=5 -> 6`
strict lift, leaving `F,Q,S^-,S^+` and every seam untouched.

### Theorem 6.1 (finite guarded-filler payoff)

The substituted support has `792` edges, exact ambient lower and upper
palettes, maximum degree two, no cycle, and exactly `132` path components.
Its minimum-three bad-window census is

\[
 \begin{array}{c|rrrr}
 &\text{total}&\text{0 transitions}&\text{1 transition}&\text{2 transitions}\\
 \hline
 \text{original structural child as filler}&144&57&36&51\\
 \text{independent residence-clean filler}&100&13&36&51.
 \end{array}                                               \tag{6.1}
\]

The `44` removed windows are exactly the bad triples in the old copied
`c` rail.  The remaining body defects lie in sectors

\[
                         0:3,\qquad z:2,\qquad cz:8.          \tag{6.2}
\]

#### Proof

Palette exactness, acyclicity and the component count follow from the
independent-filler theorem.  The filler certificate has no bad cubic path,
so (1.5) removes its complete `c`-factor.  The complementary three-sector
support is unchanged, giving (6.1)--(6.2).  The independent audit below
reconstructs all edges and verifies these counts without trusting either
claimed path list.  `square`

Reproduce with

```text
python3 scratch/audit_catalan_guarded_independent_filler_m5_20260731.py
```

which writes

```text
scratch/catalan_guarded_independent_filler_m5_20260731.audit.json
```

The conclusion is deliberately two-sided.  Independent fillers remove a
real inherited obstruction, but even the best currently known finite filler
leaves the structural `Q`/side/seam clauses untouched.  The next theorem
must combine guard promotion for `G` with the joint DERF selection on `F`;
neither is a substitute for the other.
