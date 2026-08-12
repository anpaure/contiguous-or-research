# Audit of Dong--Mao, the central two-bank reduction, and the common-base gate

**Date:** 2026-08-02  
**Lane:** A, integral fixed-core/common-base rounding  
**Status:** independent primary-source and theorem audit.  The central
complementary bi-packing lemma remains unproved.

## 0. Verdict

The main reduction in
`MATH_THEOREM_CENTRAL_TWO_INTERVAL_BANK_REDUCTION_AND_ENGEL_RANGE_GATE_20260802.md`
is sound after four scope qualifications.

1. Two central interval banks whose lower and upper palettes partition the
   two outer levels give exactly the four static resource rows.  Their union
   is a maximum-degree-two graph; it is a Catalan linear forest exactly when
   it is acyclic.
2. The bank-size inequalities are necessary capacity rows, not an existence
   theorem.
3. Dong--Mao's theorem does not supply even the first bank at the central
   parameters.  It applies only in its stated noncentral range or on a
   fixed-core slice that remains in that range.
4. Neither one nor two cycle-lemma banks gives a circuit-complete absorber.
   Recolouring an alternating cycle leaves the underlying cycle unchanged;
   a genuine interval-replacement circuit is still required.

The newly added fixed-ground-bipartition obstruction is also correct.  It
rules out the simplest parity construction for every `m>=3` and forces any
positive two-bank construction to obtain bipartiteness from the selected
graph or from a state-dependent parity.

The exact positive integration with the current common-base lane is
conditional but useful: an independently constructed complementary
bi-packing supplies one integral static central table.  It must first embed
in one exact owner--named-payload table.  On a flag-homogeneous Cartesian
literal-state cylinder over that same table whose modes preserve all four
central labels and every guard, the Hoffman cuts in Corollary 2.3 of the
skip-port theorem are then necessary and sufficient for one-copy state
completion.  No averaging across different interval tables is licensed.

## 1. Primary-source audit

The audited source is Dong and Mao, *Engel's Interval Packing Problem in the
Boolean Lattice*, arXiv:2607.04794v1, 6 July 2026.  The saved PDF has SHA

```text
267f8fccd7a2448c8c031d8a584adff25827d8d22c23d7a088b9ffff4a06daf1
```

and is mirrored at

```text
scratch/a_dong_mao_common_base_audit_20260802/2607.04794.pdf.
```

Their Theorem 1.2 says that, writing `u=ell+r`, the maximum number of
pairwise disjoint maximal intervals is `binom(n,ell)` under

\[
                         n\ge (\ell+1)r+\ell.          \tag{1.1}
\]

The critical equality case uses one cycle-lemma construction.  The general
case recursively separates sets avoiding the last coordinate from sets
containing it.  This recursion constructs one packing; it does not assert
exchange connectivity among packings.

For `r=2`, their Section 4.2 leaves open the range

\[
                  {3\ell+4\over2}<n<3\ell+2.          \tag{1.2}
\]

The paper asks whether the elementary minimum of the three level-capacity
bounds is always attained there.  It does not answer that question.

## 2. Exact central substitution and capacity

For the central Boolean diamonds,

\[
 n=2m,\qquad \ell=m-1,\qquad r=2.                    \tag{2.1}
\]

Condition (1.1) becomes

\[
                              2m\ge3m-1,              \tag{2.2}
\]

which fails for every `m>=2`.  Moreover

\[
            {3(m-1)+4\over2}<2m<3(m-1)+2             \tag{2.3}
\]

holds exactly for `m>=2`, so these parameters lie strictly inside the open
range (1.2), not merely just outside the proved range.

Put

\[
 K=\operatorname {Cat}_m,\qquad
 N={2m\choose m-1}=mK,\qquad
 W={2m\choose m}=(m+1)K.                             \tag{2.4}
\]

A three-level interval consumes two middle sets.  Thus one central interval
packing has size at most `W/2`.  If the two complementary banks have sizes
`b_0,b_1`, then

\[
 b_0+b_1=N,
 \qquad {W\over2}-{W\over m+1}\le b_e\le {W\over2}. \tag{2.5}
\]

Equivalently, if `Delta_e=W-2b_e`, then

\[
                  \Delta_0+\Delta_1=2K.              \tag{2.6}
\]

These equations are exact and necessary.  They do not characterize
feasibility.  In particular, equal bank sizes are not required, and asking
both banks to have size `W/2` is incompatible with `b_0+b_1=N<W`.

For the raw odd three-level calibrations one likewise obtains

\[
\begin{array}{c|c|c|c|c}
 (n,\ell)&{n\choose\ell}&{n\choose\ell+1}
          &3\ell+2&\text{capacity ceiling}\\ \hline
 (19,7)&50388&75582&23&37791\\
 (21,8)&203490&293930&26&146965.
\end{array}                                           \tag{2.7}
\]

Both rows are in (1.2).  Dong--Mao therefore does not settle the K19/K21
central three-level gate either.

## 3. Audit of the two-bank theorem

Let `I_0,I_1` be interval packings with disjoint-union lower palettes and
disjoint-union upper palettes equal to the two full outer levels.  Each
`I_e` is a matching on the middle-level Johnson graph, because two intervals
in one packing share no middle set.  Hence `I_0 union I_1` has maximum
degree two, and its nontrivial components are alternating paths or even
cycles.

Orient each path consistently and each cycle cyclically.  Every middle
vertex then occurs at most once as a tail and at most once as a head.  The
outer palette hypotheses give every lower and upper resource exactly once.
Thus all four static resource rows hold.  The graphic row holds exactly
when there is no cycle.

Conversely, alternate the two colours along every path of a Catalan linear
forest.  Each colour class is a middle matching, hence an interval packing,
and the two colour classes still partition both outer palettes.  The
zero-cycle complementary bi-packing statement is therefore equivalent to
the central linear-forest statement.  Isolated middle vertices are harmless
length-zero paths.

Deleting one edge per alternating cycle proves only a `c`-defect forest:
it loses one lower and one upper colour for every deleted edge.  It is not
an exact cycle absorber.

The small exact regression script

```text
scratch/a_dong_mao_common_base_audit_20260802/
  audit_a_dong_mao_central_bipacking_20260802.py
```

enumerates all ordered pairs of edge-disjoint matchings through seven
middle vertices and verifies the path/even-cycle decomposition.  This is a
regression check; the proof above is dimension-uniform.

## 4. What one Dong--Mao bank really supplies

In the proved range, Dong--Mao supplies one family indexed by **every**
bottom-level set.  It is a genuine static partial common basis after any
chosen subfamily is retained:

* lower endpoints are distinct;
* upper endpoints are distinct; and
* the two middle endpoints of different intervals are distinct.

This is useful static data.  It does not give an absorber.

First, at central parameters the full bank cannot exist: `2N>W`.  Second,
inside one fixed interval packing, all middle endpoints are private.  If
its Johnson edges are oriented, reversing any nonempty subset changes the
tail/head incidence at private middle vertices; no other reversed edge can
cancel those changes.  Thus the isolated orientation modes contain no
nonzero resource-neutral role circuit.

The coordinate recursion also supplies no missing circuit.  Its two child
families lie in the disjoint `n`-absent and `n`-present sectors and together
form one packing.  They are not two complementary central banks.  Running
the construction with two coordinate orders gives two packings, but the
paper proves neither complementary outer palettes nor a bounded alternating
exchange decomposition between them.

Even after a complementary pair is found, the obvious cycle operations are
insufficient.  Swapping bank colours on an alternating cycle or reversing
its cyclic orientation preserves the uncoloured Johnson union, hence
preserves the cycle defect.  Exact cycle elimination needs a third/external
interval-replacement circuit or a connected protected exchange graph.

In algebraic terms, let every permitted replacement mode have signed named
resource vector `delta_j`.  A closed absorber is a nonzero bounded integer
vector in

\[
                            \ker_{\mathbb Z}[\delta_j]. \tag{4.1}
\]

Circuit completeness further requires legal bounded generators that
connect every relevant nonempty fibre.  Dong--Mao proves existence of one
packing, not nontriviality, generation, normality, or physical realizability
of (4.1).

## 5. Exact fixed-core partial implication

There is one useful way to import the theorem without leaving its range.
Fix a core `H` of size `h`, fix `A subseteq H` with `|A|=i`, and restrict to
intervals whose intersection with `H` is exactly `A`.  Deleting `A` identifies
this slice with

\[
             P_{n-h;\,\ell-i,\,\ell-i+2}.            \tag{5.1}
\]

Dong--Mao supplies a full bottom-saturating interval bank on this slice if

\[
                         n-h\ge3(\ell-i)+2.           \tag{5.2}
\]

Different fixed-core slices are resource-disjoint.  Consequently all slices
passing (5.2) may be united into a certified **partial** interval bank.  The
ineligible slices and the complementary outer-palette condition remain.

By complementing the outside cube, the opposite full top-saturating slice
is certified when

\[
                         2(n-h)\le3(\ell-i)+4.        \tag{5.3}
\]

For the fixed-triple K19 calibration `(n,ell,h)=(19,7,3)`, (5.2) holds only
for `i=3`; it gives the `binom(16,4)=1820` exceptional full-core slice.  For
the K21 calibration `(21,8,8)`, the important `i=4` slice fails by one:
`13<3*4+2=14`; only `i>=5` lies in the proved range.  Thus the theorem can
seed some off-central orbit types but does not settle the load-bearing
central type.  In the same K21 calibration, (5.3) applies to the extreme
`i=0` slice; this is another off-central partial bank, not a complement for
the missing `i=4` bank.

There is a stronger unconditional partial bank, independently frozen in
`MATH_THEOREM_DONG_MAO_FIXED_CORE_DIAMOND_BANK_AND_TWO_BANK_FUSION_GATE_20260802.md`.
Split `[2m]=H dotcup K` with `|K|=5`.  In every fixed `H`-pattern, use the
sharp fibre banks of sizes `(1,5,5,1)` on the four possible three-level
ranges of `B_5`; the two size-five fibres are the critical Dong--Mao
`(5,1,2)` construction and its complement.  The union over all `H`-patterns
is one literal central interval bank of size

\[
 D_m=2{2m-5\choose m-1}+10{2m-5\choose m-2},         \tag{5.4}
\]

with exact middle-capacity density

\[
 {D_m\over\frac12{2m\choose m}}
   ={m(3m-4)\over(2m-1)(2m-3)}\longrightarrow{3\over4}. \tag{5.5}
\]

It is maximum among banks that preserve every `H`-pattern.  This is the
precise positive answer to the **partial common-basis** part of the present
audit: one recursive critical interval bank supplies three quarters of the
middle capacity asymptotically.  It still is not a circuit-complete absorber
or a two-bank completion.  Indeed

\[
                         2D_m<{2m\choose m-1}         \tag{5.6}
\]

for every `m>=6`; two copies are then cardinality-insufficient before outer
palette complementarity, cross-bank collisions, or topology is tested.

## 6. Fixed coordinate parity is not the missing construction

The new Proposition 6.1 in the two-bank note is exact.  Suppose every
selected interval adds one coordinate from each side of a fixed partition
`[2m]=A dotcup B`.  Covering every `(m-1)`-set forces `|A|,|B|>=m`, hence
`|A|=|B|=m`.  For each `a in A`, the lower set `A-{a}` must add `a` and a
coordinate of `B`.  The resulting Johnson edge is incident with the same
middle vertex `A`.  The `m` distinct lower colours therefore force degree
at least `m` at `A`, contradicting tail/head capacity two when `m>=3`.

So a positive construction cannot impose one coordinate parity on the
whole diamond catalogue.  The remaining viable forms are:

1. a parity or potential chosen from the selected graph/state rather than
   fixed on coordinates;
2. a bank-dependent parity with explicit overload compensation; or
3. no prior parity, followed by direct acyclic/graphic selection.

There is an exact selected-graph replacement for the failed coordinate
cut.  Let `F` be a chosen diamond set and let
`beta:E(F)->{0,1}` be its bank label.  Then the following are equivalent:

1. both bank classes are matchings on the middle layer;
2. `beta` is a proper two-edge-colouring of `F`;
3. every component of `F` is a path or an even cycle.

In this case choose, separately on every component, a vertex phase
`pi:V(F)->{0,1}` satisfying

\[
                         \pi(u)+\pi(v)=1\pmod2        \tag{6.1}
\]

on every selected edge.  Orient an edge `uv` from `u` to `v` exactly when
`pi(u)=beta(uv)`.  At a degree-two vertex the incident bank labels differ,
so exactly one edge enters and one leaves.  This proves tail/head capacity
without any coordinate-defined parity.  A path becomes a consistently
oriented path; an even cycle becomes a directed cycle.  Thus the remaining
topology row is still precisely

\[
                 |E_F(S)|\le |S|-1
                 \qquad(\varnothing\ne S\subseteq\mathcal M). \tag{6.2}
\]

This is the proof-safe state-dependent route: select the two bank matchings
first, derive `pi` componentwise, and impose (6.2).  It evades Proposition
6.1 but does not prove that the required selected graph exists.

## 7. Exact common-base insertion

The complementary bi-packing lemma is a structured integral **static**
face of the skip-port/common-base master.  The composition is as follows.

1. Choose one literal complementary bi-packing and, if exact central
   topology is required, demand that its union be acyclic.
2. Embed that object, all noncentral roles, and the protected bank `P` into
   one exact residual owner--named-payload table.  This step must be
   literal; an orbit average of several bi-packings is not one table.
3. Put `eta=partial P`, require `eta(V)=0`, and retain literal residual Hall
   for the exact free-role set.
4. On the same table, require one flag-homogeneous Cartesian state menu
   `A_i times H_i` per free role, constant on all four central labels and
   every retained guard.
5. Check every shifted Hoffman inequality

   \[
           \ell_A(X)-r_H(X)\le\eta(X).               \tag{7.1}
   \]

The fixed Johnson middle tail/head labels in the bi-packing are not
automatically the variable rotor tail/head states in (7.1).  If a model
identifies them, the menus must be singletons on those labels or carry the
extra matching rows explicitly.  With this qualification, Corollaries
2.3--2.4 of
`MATH_THEOREM_A_FIXED_CORE_SKIP_PORT_COMMON_BASE_AND_TORSION_ABSORBER_20260802.md`
then give an integral one-copy state completion.  The two-bank theorem
removes the static central four-resource correlation on this face; it does
not prove the Cartesian state cylinder or (7.1).

If one edge per alternating cycle is deleted, the role set, protected
boundary, and residual menus change.  Hoffman feasibility is not hereditary:
the reduced table and `eta` must be rebuilt and (7.1) checked again.

The Boolean K11 `C10` Smith-2 obstruction is a sharp compatibility check.
Its five static rank-4-to-rank-5 chains and owners are valid, and its ten
literal states form one primitive directed cycle with integral orbit totals.
Nevertheless state balance forces `2c=1`.  Hence static interval packing and
even a complete primitive chronology circuit do not remove the literal
cokernel gate.  The exact artifact is

```text
MATH_THEOREM_A_BOOLEAN_C10_NESTED_STATE_SMITH2_ORBIT_LIFT_OBSTRUCTION_20260802.md
```

with SHA

```text
9556c805f001a150d042e7b8051088207862c493c66221ef81c869ae90e9c986.
```

## 8. Remaining theorem

The weakest exact live statement is now a conjunction, not a citation:

1. construct a central complementary bi-packing, preferably acyclic or with
   a protected cycle-replacement atlas;
2. on that same table construct ROTS-compatible Cartesian state rectangles
   passing (7.1), or clear the literal Smith class and prove unit-normality;
3. reserve a connected Euler skeleton if one-cycle topology is required.

Residence, deep upper shadows, source factorability, common cap, compiler,
and a universal word remain outside this audit.
