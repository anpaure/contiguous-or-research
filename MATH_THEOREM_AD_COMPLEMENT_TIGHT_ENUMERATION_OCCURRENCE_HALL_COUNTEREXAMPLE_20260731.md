# Complement-symmetric tight enumerations reduce to perfect 2-matchings, and fail completely at `m=3`

Date: 2026-07-31  
Status: exact all-dimension reduction; complete solver-free `m=2,3` audits;
dimension-minimal nonvacuous counterexample to complement-symmetric local
repair; no obstruction to asymmetric terminal cycles or general Catalan
Linear Matching

## 0. Verdict

Let `Omega=[2m]`, and let a tight cyclic enumeration of ranks `m-1,m`
project to a Hamilton cycle `C` of `J(2m,m)`.  At this interface, tightness
is exactly lower-colour completeness.  If the projected Hamilton cycle is
invariant under complementation, its upper colours are complete as well.
This still does **not** imply the occurrence Hall condition.

The correct symmetric quotient is a graph `D(C)` on the rank-`m-1`
colours.  A complement orbit of physical Johnson edges with colours

```text
lower L, upper U
```

becomes the undirected Kneser edge

```text
L -- complement(U).
```

After the upper shore is identified with the lower shore by complement,
the lower-versus-upper occurrence graph is precisely the bipartite double
cover of `D(C)`.  Therefore:

> `C` has a perfect occurrence matching if and only if `D(C)` has a
> perfect 2-matching, equivalently a spanning vertex-disjoint union of
> ordinary edges and odd cycles.  Allowing arbitrary cycles is
> existence-equivalent, since every even cycle splits into alternating
> ordinary edges.

This is the exact checkable condition.  In Hall form it is

\[
             |N_{D(C)}(A)|\ge |A|
             \qquad(A\subseteq\tbinom\Omega{m-1}).       \tag{0.1}
\]

Complement symmetry plus two-sided surjectivity says only that `D(C)` has
no isolated vertex.  It does not imply (0.1).

The proposed universal local-repair statement is false in its strongest
natural interpretation.  At `m=3` the complete complement quotient can be
exhausted without a solver:

```text
rooted/reversal quotient Hamilton cycles                 181440
connected physical complement-half-turn Hamilton lifts    88704
lower-tight (hence also upper-tight) Hamilton lifts          3024
with a perfect occurrence matching                              0
```

Their occurrence matching-rank histogram is

\[
                  10^{864}\,12^{1440}\,14^{720}<15.       \tag{0.2}
\]

Every one of the `3024` transfer graphs is a spanning forest with `15`
vertices, `10` edges, and five components.  A forest on an odd number of
vertices has no perfect 2-matching.  Consequently **no sequence of local or
nonlocal switches whose terminal state remains a complement-symmetric
lower-tight Hamilton cycle can repair occurrence Hall at `m=3`**.  This
conclusion is independent of the switch catalogue and is stronger than a
bounded-radius no-go.

At `m=2`, all four complement-invariant Hamilton cycles miss one colour on
each shore; no complement-symmetric tight input exists.  Thus `m=3` is the
smallest nonvacuous failure.

The escape is asymmetric.  The existing audited `m=3` two-cycle union
contains an asymmetric cap-two `Cat_3`-path forest whose occurrences form a
perfect matching, even though no spanning two-factor in that union does.
More generally, once any Hamilton cycle has a perfect occurrence matching,
the selected physical occurrences form a spanning `Cat_m`-path forest and
hence an ordered four-transversal.  The present theorem refutes a symmetry
shortcut, not Catalan Linear Matching.

## 1. Tight-enumeration interface and terminology

Put

\[
 \mathcal L=\binom\Omega{m-1},\qquad
 \mathcal X=\binom\Omega m,\qquad
 \mathcal U=\binom\Omega{m+1},                       \tag{1.1}
\]

\[
 K=\operatorname {Cat}_m,\qquad
 N=|\mathcal L|=|\mathcal U|=mK,\qquad
 M=|\mathcal X|=(m+1)K=N+K.                          \tag{1.2}
\]

A tight cyclic enumeration of the two levels `m-1,m` has no consecutive
lower-level vertices.  Suppressing every lower vertex gives a Hamilton
cycle `C` on all `M` middle owners.  Every listed lower vertex is the
intersection of the two neighbouring owners, so every member of
`mathcal L` occurs.

Conversely, given any Hamilton cycle of `J(2m,m)` with complete lower
support, select one occurrence of each lower colour and subdivide that edge
by its intersection.  All other Johnson edges remain direct two-bit steps.
The resulting enumeration attains the exact tight distance `2M`.

Thus, at the projected-owner interface,

\[
 \boxed{\text{two-level tight enumeration}
 \iff\text{lower-complete Johnson Hamilton cycle}.}   \tag{1.3}
\]

There is a terminology caveat.  Plain complementation does not preserve
the two levels `{m-1,m}`: it sends rank `m-1` to rank `m+1`.  Therefore a
literal two-level listing is not plain-complement invariant.  Throughout
this note, **complement-symmetric tight enumeration** means that its
projected middle-owner Hamilton cycle is complement invariant.  Equivalently,
the lower-tight enumeration is paired with its complement-dual upper-tight
enumeration on the same projected owner cycle.

## 2. Complement necessarily acts as a half-turn

Assume `m>=2`.  Complementation has no fixed rank-`m` vertex.  It also fixes
no Johnson edge setwise: a fixed edge would have endpoints `X,X^c`, whose
Johnson distance is `m`, not one.

An involution of an abstract cycle is a half-turn, a vertex-axis reflection,
or an edge-axis reflection.  The two reflection types would respectively
fix a vertex or an edge.  Hence:

### Lemma 2.1

On every complement-invariant Hamilton cycle of `J(2m,m)`, complement acts
as the half-turn.

The central binomial coefficient `M` is even for `m>=1`, so this action is
arithmetically possible.  If

\[
                         X_{i+M/2}=X_i^c,              \tag{2.1}
\]

then edge occurrences are paired as `e,e^c`.

### Lemma 2.2 (a single symmetric Hamilton path is impossible)

For `m>=2`, no Hamilton path of `J(2m,m)` is invariant under plain
complementation.

#### Proof

The only nonidentity automorphism of a finite path is reversal.  Since
`M` is even, reversal fixes the central path edge setwise.  Plain
complementation fixes no Johnson edge setwise, by the argument above.
The identity action is also impossible because complementation fixes no
middle owner.  \(\square\)

Thus a complement-symmetric SCD/path construction must use a paired path
family or first close to a cycle; one invariant spanning path cannot be the
projected object.

## 3. The complement transfer graph

For a Johnson edge occurrence `e=XY`, put

\[
             \ell(e)=X\cap Y\in\mathcal L,
             \qquad u(e)=X\cup Y\in\mathcal U.       \tag{3.1}
\]

Define `D(C)` on vertex set `mathcal L`.  For every complement orbit
`{e,e^c}`, insert the undirected edge

\[
                    \ell(e)\;--\;u(e)^c.             \tag{3.2}
\]

The endpoints in (3.2) are disjoint `(m-1)`-sets, because
`ell(e) subset u(e)`.  Hence `D(C)` is a subgraph of
`KG(2m,m-1)`.

The definition is independent of the representative `e`: the complement
edge has

\[
        \ell(e^c)=u(e)^c,\qquad u(e^c)^c=\ell(e).     \tag{3.3}
\]

Moreover, one pair of endpoints in (3.2) determines one complement orbit
of physical Johnson edges.  If `L,T` are disjoint rank-`m-1` sets, the two
remaining coordinates are `a,b`, and the orbit is

\[
 \{(L+a)(L+b),\ (T+a)(T+b)\}.                         \tag{3.4}
\]

Thus `D(C)` is simple and has exactly `M/2` edges.

### Lemma 3.1 (load identity)

For every `L in mathcal L`,

\[
              d_{D(C)}(L)=\#\{e\in E(C):\ell(e)=L\}. \tag{3.5}
\]

Consequently lower completeness is equivalent to `D(C)` having no
isolated vertex.  By (3.3), it is simultaneously equivalent to upper
completeness.

#### Proof

Every transfer edge incident with `L` has exactly one oriented physical
occurrence whose lower colour is `L`; conversely every such occurrence
belongs to that transfer orbit.  This is a bijection.  Equation (3.3)
gives the upper statement.  \(\square\)

In the tight case this gives the exact sparse ledger

\[
 |V(D(C))|=mK,qquad |E(D(C))|={(m+1)K\over2},qquad
 \sum_L\bigl(d_{D(C)}(L)-1\bigr)=K.                 \tag{3.6}
\]

Thus complement symmetry turns the `K` unavoidable repeated lower
occurrences into exactly `K` units of degree excess.  It does not control
how those units are distributed among components, which is precisely what
perfect 2-matching Hall sees.

## 4. Exact occurrence-Hall theorem

Let `G(C)` be the bipartite occurrence graph on
`mathcal L sqcup mathcal U`, with one occurrence edge
`ell(e)--u(e)` for every physical cycle edge.  Relabel the upper vertex
`U` by `U^c in mathcal L`.  Equations (3.2)--(3.3) show that every transfer
edge `L--T` produces exactly the two bipartite incidences

\[
                 L_{\rm left}--T_{\rm right},\qquad
                 T_{\rm left}--L_{\rm right}.         \tag{4.1}
\]

Thus `G(C)` is the bipartite double cover of `D(C)`.

### Theorem 4.1 (complement occurrence criterion)

The following are equivalent.

1. `G(C)` has a perfect occurrence matching.
2. For every `A subseteq mathcal L`, inequality (0.1) holds.
3. There is a permutation `sigma` of `mathcal L` such that
   `L--sigma(L)` is an edge of `D(C)` for every `L`.
4. `D(C)` contains a spanning vertex-disjoint union of ordinary edges and
   odd cycles (a perfect 2-matching in the standard normalization).
5. For every `S subseteq mathcal L`, the number `i(D(C)-S)` of isolated
   vertices of `D(C)-S` is at most `|S|`.

#### Proof

The equivalence of 1 and 2 is Hall's theorem applied to (4.1).  Relabelling
both shores by `mathcal L` turns a perfect bipartite matching into the
permutation in 3.  Decompose that permutation into cycles.  A two-cycle
uses the two orientations of one ordinary edge; every longer permutation
cycle is an ordinary cycle of `D(C)`.  Replace every even ordinary cycle by
its alternating ordinary edges; this leaves only ordinary edges and odd
cycles.  Conversely, orient every odd cycle and use both directions of
every isolated matching edge.  This gives the required permutation.

For 2 implies 5, let `I` be the isolated vertices of `D(C)-S`.  Then
`N(I) subseteq S`, so Hall gives `|I|<=|N(I)|<=|S|`.  Conversely, if Hall
fails for `A`, put `I=A setminus N(A)`.  The set `I` is independent,
`N(I) subseteq N(A) setminus A`, and

\[
 |I|-|N(A)\setminus A|=|A|-|N(A)|>0.
\]

Taking `S=N(I)` therefore makes every member of `I` isolated in `D(C)-S`
and gives `i(D(C)-S)>=|I|>|S|`, contradicting 5.  \(\square\)

This theorem supplies useful checkable special cases.

The full condition is polynomially checkable: construct the bipartite
double cover and run one ordinary maximum-matching algorithm.  The
isolated-vertex form in item 5 is the exact Tutte-style obstruction; it is
not an extra assumption.

* If `D(C)` is a forest, occurrence Hall holds exactly when the forest has
  an ordinary perfect matching; leaf peeling checks this.
* If `Delta(D(C))<=2`, every component is a path or cycle.  Occurrence Hall
  holds exactly when every path has even order; cycles of either parity are
  allowed.
* Merely requiring minimum degree one is insufficient.  A three-vertex
  path is the smallest abstract obstruction.

This is the complement-symmetric analogue of the gap-Hall warning for
Middle Levels decorations.  Two-sided surjectivity remains a marginal
condition; the same physical occurrence must satisfy both palettes.

## 5. From an occurrence matching to the ordered four-transversal

Suppose Theorem 4.1 holds, and select the `N` matched physical occurrences.
Because `N<M`, this is a proper edge subset of the one Hamilton cycle `C`.
It therefore has maximum physical degree at most two and is acyclic.
Retain all unused middle owners as isolates.  Its component count is

\[
                         M-N=K=\operatorname {Cat}_m. \tag{5.1}
\]

Orient every path.  For the selected edge of lower colour `L`, write its
tail and head as

\[
 T_L=L+a_L,\qquad H_L=L+b_L,\qquad
 U_L=L+\{a_L,b_L\}.                                   \tag{5.2}
\]

The lower colours index the edges, occurrence matching makes the `U_L`
bijective, path orientation makes both `T_L` and `H_L` injective, and the
physical forest has no directed cycle.  Hence (5.2) is exactly the ordered
four-transversal normal form.

Thus a positive complement-Hall theorem would immediately prove Catalan
Linear Matching.  Section 6 shows that complement symmetry cannot provide
that theorem by itself.

The support implication does not require a cycle.  If `P` is any Hamilton
path of `J(2m,m)` and its lower-versus-upper occurrence graph has a perfect
matching, the `N` selected path edges are again a spanning linear forest
with exactly `M-N=K` components and give the same ordered
four-transversal.  What fails in the symmetric path route is earlier:
Lemma 2.2 rules out one plain-complement-invariant Hamilton path.  No claim
about a particular noncyclic tight-enumeration endpoint convention is used
here.

## 6. Complete `m=2` audit

There are `16` Hamilton cycles of `J(4,2)` after fixing one root and
quotienting reversal.

```text
complement invariant, supports (3,3), occurrence rank 3       4
asymmetric, supports (4,4), occurrence rank 4                 12
```

Therefore every complement-invariant cycle misses one lower and one upper
colour, while all twelve two-sided-complete cycles are asymmetric and pass
occurrence Hall.  This independently replays Proposition 7 of
`TWO_SIDED_CATALAN_LIFT.md` and shows that the symmetric tight class is
empty at `m=2`.

## 7. Complete `m=3` quotient audit

Use bitmasks on `[6]`.  The ten complement pairs of middle triples have
canonical representatives

```text
7,11,13,14,19,21,22,25,26,28.
```

### Lemma 7.1 (the owner quotient is `K10`)

Between every two distinct complement pairs there is exactly one complement
orbit of Johnson edges.

#### Proof

Let the pairs be `[X]` and `[Y]`.  They are distinct, so after replacing
`Y` by `Y^c` if necessary, `|X cap Y|=2`; exactly one of `Y,Y^c` has this
property.  Hence `XY` is a Johnson edge, as is its complement, and the
other two cross-pairs are not Johnson edges.  This gives one edge orbit.
\(\square\)

Consequently every complement-invariant physical Hamilton cycle projects
to a Hamilton cycle of `K10`.  Conversely, each quotient edge has a fixed
binary lift voltage.  A quotient `10`-cycle lifts either to two `10`-cycles
or to one complement-half-turn `20`-cycle according as the XOR of its ten
voltages is zero or one.

Fixing quotient vertex zero and quotienting reversal gives exactly

\[
                            9!/2=181{,}440            \tag{7.1}
\]

cycles, so the finite enumeration is complete.  It gives:

```text
quotient cycles                                         181440
odd-voltage / connected physical lifts                   88704
connected lifts whose transfer graph spans all 15 colours 3024
perfect occurrence matchings                                 0
```

For every one of the `3024` tight lifts, the transfer graph has ten edges,
is a forest, and has five components.  The exact component-size census is

```text
2,2,3,3,5     1440
2,2,3,4,4      720
2,3,3,3,4      720
3,3,3,3,3      144
```

Since a forest has no cycle component, its perfect 2-matchings are just
ordinary perfect matchings.  Its order is `15`, so none exists.  Independent
bipartite augmentation gives the finer matching-rank histogram (0.2).

One maximum-rank example is the half-turn cycle

```text
7 11 13 44 14 26 25 41 35 42
56 52 50 19 49 37 38 22 28 21
```

It is lower- and upper-complete and has occurrence matching rank `14`.
Its explicit Hall obstruction is

\[
                       \{17,18\}\longmapsto\{51\}.    \tag{7.2}
\]

Both lower colours `17` and `18` have only upper neighbour `51`.

### Corollary 7.2 (unrestricted symmetric-terminal switch no-go)

At `m=3`, no complement-symmetric lower-tight Hamilton cycle admits a
perfect occurrence matching.  Therefore no sequence of switches, of any
support size and using any Johnson edges, can succeed if its terminal state
is required to remain in that class.

The corollary allows intermediate states to break symmetry or tightness; it
only uses the exhaustive terminal classification.  It does **not** exclude
a terminal asymmetric Hamilton cycle, a decorated 2-factor, or a direct
linear forest.  It also does not say that the canonical GMM implementation
visits all `3024` cycles; the equivalence (1.3) says that all `3024` are
valid tight-enumeration projections at the mathematical interface.

## 8. Relation to existing local-switch results

The old frozen `m=3` cycle `P` and its complement `P^c` supplied a narrower
forty-edge test.  Inside `P union P^c` there are `124`
complement-invariant spanning two-factors, `36` Hamilton cycles, and six
lower/upper-complete Hamilton cycles; none has a common transversal.  This
is consistent with the previously audited `6272`-factor two-cycle lock.

The new `K10` quotient census strictly strengthens that result for the
symmetry question: it includes every complement-invariant Hamilton cycle
of `J(6,3)`, including switches that use edges outside `P union P^c`.

Standard incidence-hexagon and alternating-circuit repairs remain useful
only if they are allowed to leave the complement-symmetric terminal class.
This mirrors the audited `ML(7)` gap-Hall example, where a single hexagon
repairs a fixed asymmetric trace.  Neither example permits the inference

```text
two-sided surjectivity + symmetry => occurrence Hall.
```

## 9. Exact surviving all-`m` target

The tight-enumeration/SCD route may still succeed, but the sufficient state
must export more than complement symmetry.  One exact formulation is:

> Construct a lower-complete Hamilton cycle `C` of `J(2m,m)` such that its
> occurrence graph has a perfect matching.  In the complement-symmetric
> subclass this is exactly the perfect-2-matching condition of Theorem 4.1;
> outside that subclass it is ordinary bipartite occurrence Hall.

For recursive proofs, a checkable exported certificate can be any one of:

1. the perfect occurrence matching itself;
2. all Hall inequalities for the bipartite occurrence graph;
3. under complement symmetry, a spanning edge/cycle cover of `D(C)`;
4. in a degree-two or forest state, the corresponding componentwise parity
   or leaf-peeling certificate.

An SCD supplies exact rank ownership but does not automatically supply any
of these occurrence correlations.  Complement-pairing an SCD closes only
the marginal duality.  The `m=3` theorem proves that no universal
symmetry-preserving local repair lemma can fill the gap.

## 10. Artifacts and hashes

Primary audit:

* `scratch/audit_ad_tight_enumeration_complement_occurrence_hall_20260731.py`,
  SHA-256 `3b7b068ced40ca99e4977c753e07717cf65a40703820e479e347074f6173bc3b`;
* `scratch/ad_tight_enumeration_complement_occurrence_hall_20260731.audit.json`,
  SHA-256 `81d7ec07678d198964d511703655830d4be929a88a15deff331e76d5f6b6066e`,
  payload `71b4d8562cf7cb8e23fd503cb40053bf3c87aede7d5cc1c1f9c5886507c23f95`.

Independent replay, using union-find plus ordinary graph matching rather
than the primary bipartite augmenter:

* `scratch/verify_ad_tight_enumeration_complement_occurrence_hall_20260731.py`,
  SHA-256 `86b54ef53d4d7e61beff7e290f9b56bc326badef5abefdcfcddc66f7aaeaf757`;
* `scratch/ad_tight_enumeration_complement_occurrence_hall_20260731.independent.audit.json`,
  SHA-256 `769d62d612f35b642f0838424c244fc1cacc01027fcd0a5a2a41e2ae226de031`,
  payload `cf7ba242f9827b4166a77317b8e1b5d600832090ba96138ceb729cb7f9e4434c`.

Authoritative inputs checked in this audit:

* `MATH_AUDIT_TIGHT_ENUMERATION_MIDDLE_LEVELS_AND_FACTOR_BLIND_INTERFACE_20260726.md`,
  SHA-256 `65d595e7c88566f3eb7fa687ad0c11660dfc9138b3e4ebc285a8f905022231f0`;
* `TWO_SIDED_CATALAN_LIFT.md`,
  SHA-256 `095cb79fc3c4332b61965c58ac00e43df3fe7ec17f5a25b7fa66727f1556a82d`;
* `MATH_THEOREM_CATALAN_TWO_CYCLE_HYBRID_LOCK_AND_FOREST_ESCAPE_20260731.md`,
  SHA-256 `59c2aa3cbe2e391f7ba5aed081dba56ae12928744bf6844d242a72b658f4df6e`;
* `MATH_THEOREM_CATALAN_ALTERNATING_TURN_SDR_HALL_AND_M4_COUNTEREXAMPLE_20260731.md`,
  SHA-256 `c19f5e7a5bef20a16ca6fc0f475cb6084f7d3ed4a07b5c657611231c9ab5aec0`;
* `MATH_AUDIT_K_GMM_BLOCK_CONTIGUITY_SMALL_FIXTURES_20260731.md`,
  SHA-256 `81a03d4d67173d490b402c4718c8d858a35291e188a9626eaa371c38b50dfeed`.

No web source, SAT solver, or long-running computation was used.  The two
complete finite audits each run in under one second on the local fixture.
