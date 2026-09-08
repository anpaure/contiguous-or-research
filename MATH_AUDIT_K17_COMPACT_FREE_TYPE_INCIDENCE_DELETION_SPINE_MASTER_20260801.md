# K17 compact incidence/deletion-spine master: exact free-type scope and implementation audit

Date: 2026-08-01  
Lane: K  
Status: exact reduction and proof-carrying engine implemented; the bounded H100 run reported in Section 8 is an existence search, not a theorem of feasibility or infeasibility

## 1. Scope correction

The authenticated cyclic word

```text
scratch/k17_age_type_euler_word_20260801.tsv
```

is one sufficient order of the nine age types.  It is not without loss of
generality.  Accordingly the engine has three logically separate layers.

1. The **outer incidence master** chooses no age type at all.  It chooses a
   spanning degree-two subgraph of the actual voltage-labelled rank-8/rank-9
   incidence quotient, with the native rank-7 and rank-10 turn palettes
   imposed eagerly.
2. The **fixed-e55 inner** is an explicitly labelled sufficient-subclass
   probe.  It imposes a cyclic shift of the displayed e55 word.
3. The **free-type inner** allows every certified type at every quotient
   layer and imposes only the exact type masses.  This is the load-bearing
   companion for rejecting a selected outer cycle.

Thus:

* SAT in either inner model is a positive fixed-cycle certificate;
* UNSAT in fixed-e55 says nothing about another type order;
* UNSAT in free-type rejects only the selected outer cycle; and
* no finite collection of such fixed-cycle rejections is a global UNSAT
  certificate unless the outer master itself is subsequently proved UNSAT
  with all those sound no-goods.

## 2. Outer incidence formulation

Let `N=1430`.  The quotient incidence multigraph has

```text
1430 rank-9 owner vertices,
1430 rank-8 facet vertices,
12870 voltage-labelled incidences,
degree 9 on both shores.
```

The incidence bits have degree exactly two at every vertex.  For each pair
of incidences selected at an owner, an AND variable records its rank-7
intersection turn; for each pair selected at a facet, an AND variable records
its rank-10 union turn.  There are `51480` turn variables on each shore and
`1144` eager orbit-surjection rows on each shore.  A connected selected
2-factor is exactly the union of two incidence perfect matchings whose
composition is one owner cycle.

Connectivity is separated by ordinary component-boundary clauses.  A
connected candidate is then decoded in both orientations.  Its accumulated
incidence voltage must be nonzero modulo 17.  A zero-voltage or otherwise
factor-specific failure contributes only the exact selected-factor no-good.

## 3. Exact local residence cuts

Write the oriented owner cycle as `T_i` and its exchange labels as

```text
T_(i+1) = T_i - alpha_i + beta_i.
```

The four-deletion spine is

```text
alpha_i, alpha_(i+1), alpha_(i+2), alpha_(i+3)
```

pulled into the gauge of `T_i`; it must consist of four distinct members of
`T_i`.  This is equivalent on the physical 17-lap lift to every positive
coordinate run having length at least four.

For a short run `[a,b]` of length `L<4`, the run is fixed by the `L+1`
bracketing Johnson steps `a-1,...,b`.  Each step uses two selected incidence
edges.  The negative disjunction of those at most eight incidence variables
is therefore a valid local cut.  The separator regenerates the complete
24,310-owner lift and asserts the equivalence between absence of these short
runs and the four-deletion spine before emitting a cut.

## 4. Free-type coarse rank-7 cuts are necessary

Let `R` be the number of exact length-four positive runs, `S_R` the number
of distinct native rank-7 colours occurring at such runs, and `S_N` the
number of distinct native rank-7 colours occurring away from them.

The exact type masses are

```text
(139,297,8,20,20,140,127,237,442).
```

They imply the following necessary inequalities for every free type order:

\[
 R\ge 436,\qquad S_R\ge 297,\qquad R+S_N\ge1283.       \tag{4.1}
\]

Indeed, `c_0=1` occurs in types 0 and 1, hence `139+297=436`
times.  The forced future-deletion anchor `alpha_(i+3)` and the freshly
inserted `beta_(i-1)` both lie in this singleton class, so each such position
is an exact length-four run.  Type 1 occurs 297 times and also emits the
native rank-7 suffix; exactness of that suffix row forces 297 distinct run
colours.  Finally type 0 consumes 139 run positions without emitting a
rank-7 suffix.  Every one of the 1144 rank-7 colours not available away from
runs must occupy another run position, whence

\[
 R\ge (1144-S_N)+139.
\]

These inequalities are pruning only.  They do not replace the free inner
exact cover.

## 5. Free-type inner formulation

For a fixed oriented outer cycle, the deletion spine fixes one member of
each of the four age classes.  The residual five labels have, for the nine
types, local domain sizes

```text
5,1,5,30,10,10,5,5,1.
```

The fixed-e55 instance therefore has exactly 5,494 semantic options.  The
free companion has all 72 options at each of 1,430 layers, hence 102,960
primary option variables.  It enforces:

* exactly one local state per layer;
* all three survivor inclusions, including the voltage-twisted last-to-first
  relation;
* the nine exact type masses by compact binary ripple counters; and
* every quotient suffix colour at ranks 2 through 7 exactly once (2,424
  exact-cover rows).  Rank 8 is the selected facet palette and rank 9 is the
  owner palette.

No transition-count table from e55 is imposed in free mode: a selected
cyclic flag sequence itself certifies its legal transitions.

The independent SAT decoder does not trust the semantic map.  It rebuilds
all options and primary variable IDs, replays every DIMACS clause, checks the
type masses and twisted survivor relations, expands all 17 voltage laps,
reconstructs the four-letter source owners, and verifies physical lower
coverage at ranks 1 through 9.

## 6. Strict-upper opening is a separate exact oracle

For a depth-three source word

\[
T_i=A_i\cup A_{i+1}\cup A_{i+2}\cup A_{i+3},
\]

an owner block `[a,b]` is exactly the source block `[a,b+3]`.  Consequently
the 3-trimmed source cut core is the ordinary owner-block cut core.  A source
cut before `A_c` corresponds to owner dart tail `c-1`.

For each owner start it suffices to retain the first endpoint at which each
new coordinate arrives.  These first-growth events include a witness for
every strict-upper union achieved from that start.  The opening oracle tests
all 1,430 translation-orbit cuts on the full 24,310-owner lift.  Before doing
so it independently replays rank, Johnson adjacency, twisted closure, both
quotient palettes, and all 2,860 distinct selected incidence variables.

If no root is safe, its clause blocks only that exact undirected selected
factor.  Reversal does not change the set of cyclic owner blocks, so the
factor-level scope is sound.

## 7. Authenticated implementation

```text
scratch/build_k17_age_incidence_cycle_master_20260801.cpp
SHA256 aec77a0cd3140b79e8e2757a6fd8e842fce821c631d1ac2dad7763c8c132bf4f

scratch/separate_k17_age_incidence_cycle_master_20260801.cpp
SHA256 13b1695f848bd9c5ccba26e424f3aafe4fefad17f402ce253c8676fea0c408cf

scratch/build_k17_age_fixed_cycle_residual_master_20260801.cpp
SHA256 5e8dcc3a247e8d12fd83e4b3886b99373468fdbd9fc1d8033c9887712d558ec9

scratch/audit_k17_age_fixed_cycle_residual_master_20260801.cpp
SHA256 eed18a339e50a684376c4c077c1a56fc7aa0fc8b133598f1d9a999f6c1e68d58

scratch/audit_k17_age_incidence_upper_opening_20260801.cpp
SHA256 7346334b0e281905dea414d16f885623ebe72e01976f7f774ba6d2ff3420256c

scratch/run_k17_age_incidence_cegar_h100_20260801.sh
SHA256 216902dd3971e1c884a455140a567e3e753cfe2a6bcd4d3cf3fd2f6043941d96

scratch/run_k17_age_free_inner_h100_20260801.sh
SHA256 f0c4249bf00349b52a1180956943d6749f4e09010c000fc81a13a885f4bb644d
```

The inner decoder received an independent warning-clean GCC/Clang source
audit.  The upper-opening oracle was independently checked line by line and
smoke-tested on the authenticated MMM quotient calibration; it correctly
returned a scoped no-opening result there rather than a global conclusion.
The optional outer modes were also cross-audited: their incidence/rank-10
prefix IDs agree, the exact variable/clause delta is reproduced, all carried
lazy clauses use only incidence variables `1,...,12870`, and rank-10-only
separation converts missing native rank-7 support into an exact-factor cut.

## 8. Bounded H100 run

The outer builder has two independently audited modes.  The exact default,
after importing 959 previously generated incidence-only cuts, has

```text
115830 variables
578107 clauses
12870 incidence variables
51480 rank-7 turn variables
51480 rank-10 turn variables
1144 rank-7 rows
1144 rank-10 rows
959 lazy rows
```

That fully eager face reached the 300-second first-round cap and is therefore
`UNKNOWN`.  The requested split mode `--rank10-only` has, before lazy cuts,

```text
64350 variables
421564 clauses
12870 incidence variables
51480 rank-10 turn variables
1144 eager rank-10 rows
```

It defers native rank 7 to the proof-safe separator and ultimately to the
free inner exact rows.  The separator still recomputes native rank-7 geometry
on every connected candidate and applies (4.1); absent rank-7 support causes
an exact selected-factor no-good, never a global conclusion.  Incidence and
rank-10 variable IDs are identical in the two modes, so all accumulated lazy
incidence cuts transfer literally.

It runs on one H100 CPU core under `nice 15`, a 4-GiB virtual-memory cap, and
a 300-second per-round limit.  No GPU and no `/dev/shm` output are used.  The
working directory is

```text
/home/amodo/or15/work/laneK_age_quotient_20260801
```

At freeze time the rank-10-only run status is **IN PROGRESS / UNKNOWN**.  This
is not a negative result.  If an outer candidate appears, the pipeline first applies
the exact upper-opening oracle, then the free-type inner, and accepts SAT only
after the independent 17-lap literal decoder passes.  Fixed-e55 is not used as
a rejection gate.

## 9. Exact remaining boundary

The compact master removes the false fixed-order quantifier and the earlier
25-million-clause dart skeleton.  It does not prove that a suitable cycle
exists.  The unresolved finite statement is:

> Some connected nonzero-voltage incidence 2-factor satisfies the deletion
> spine, the free 72-state exact-mass suffix system, and a strict-upper-safe
> opening.

Failure of fixed e55 is irrelevant to this statement.  A global negative
claim requires exhaustion of the type-free outer master together with
proof-safe no-goods from the free inner and opening oracle.

## 10. Complement-dual/direct-`A` sufficient subclass

A subsequent exact restriction removes the coupled immediate-palette row but
does not replace the unrestricted master.  If `C` is complement and one
incidence perfect matching `D` is chosen, put

\[
                       H=C D^{-1}C,
        \qquad A=C D.
\]

The rank-7 turn at a complemented owner is the literal complement of the
corresponding rank-10 turn, including multiplicity.  Thus rank-10 surjection
implies rank-7 surjection.  On the other hand the factor successor is

\[
                         H^{-1}D=A^2.
\]

Since `N=1430` is even, the unchanged dual factor can never be one quotient
cycle.  Constraining `A` itself to be a 1,430-cycle gives exactly two
715-owner parity cycles; a later connector must leave the dual face.

The direct search formulation uses one variable for each of the 12,870
voltage-labelled odd-graph arcs

\[
                     a\longmapsto C(a)+n.
\]

If the incoming label at `a` is `p` and the outgoing label is `n`, its two
immediate turn colours are

\[
                  C(a)+\{p,n\},\qquad a-\{p,n\}.
\]

It therefore needs 12,870 arc variables and 51,480 unordered turn variables.
The clean lazy-`A` model has 64,350 variables and 325,754 clauses; the exact
rooted-order model has 95,810 variables and 925,391 clauses.  An independent
audit checked all 218,790 physical phase arcs, all 12,870 exported `D/H`
incidences, both turn formulas, and all formula counts.

```text
MATH_AUDIT_K_K17_COMPLEMENT_DUAL_ONE_MATCHING_PALETTE_AND_TOPOLOGY_20260801.md
SHA256 48d11f446b3a42deb38d54f5f7136ecd8e54cc56dde38778e969f85ea98910c8

MATH_THEOREM_K17_EXACT_INCIDENCE_CYCLE_AND_COMPLEMENT_DUAL_COMPANIONS_20260801.md
SHA256 39cf1ce6484c80008878701c2b06ff3acedea1f3157f36e70617f1a2f88d9209

scratch/build_k17_age_direct_A_cycle_master_20260801.cpp
SHA256 b746baf534e2a1b4be1a5e0e7a37829c821e76a94e587e6bb61c9b41d0465d27

scratch/separate_decode_k17_age_direct_A_cycle_master_20260801.cpp
SHA256 a32b8935e714e8dfbb48ce9a9f97b6769713addea251ee3351c4888684f52086

scratch/audit_k17_age_direct_A_cycle_master_20260801.cpp
SHA256 aa0eb5dcd9b6cd8ac78163cfeb318c7cda00b48ef2b373dfa75ccb5d0368017d

scratch/k17_age_direct_A_cycle_master_20260801.audit.json
SHA256 6707ffa234544bcef286871ad1c85ac780b17a8cf83b63d01c978fa5290d3bc6
status PASS
```

The clean lazy run found a 146-component first cover, then reached its
300-second second-round cap; its status is `UNKNOWN`.  The exact-order run is
bounded separately.  Neither status has any implication outside this
explicit sufficient subclass.  If a direct seed is found, the exact next
test is a non-dual rectangle or longer alternating circuit between the two
parity cycles.  For each changed colour `Z` and rank `r in {7,10}` it must
satisfy

\[
                 \mu_r(Z)-m_r^-(Z)+m_r^+(Z)\ge1,
\]

and its joined quotient voltage must be nonzero.  The 286 repeat units per
shore are exact available capacity, not by themselves an existence proof for
such a rectangle.

## 11. Authenticated shell and fixed-exterior update

The direct seed is now exact, but it is not the previously anticipated
`715+715` `A` anatomy.  Its frozen `A` has cycle lengths `[1429,1]`; the
complement-dual factor has the same quotient lengths.  Both immediate
palettes are complete.  Independent D- and H-side cross catalogues find zero
geometric rectangles across the singleton/long-cycle cut.

The singleton-centred direct-`A` fixed-exterior LNS is exact.  Radius two
(146 roots, 612 free arcs) is DRAT-verified UNSAT; radius three (771 roots,
4,976 free arcs) timed out and is UNKNOWN.  A separate exhaustive assignment
census closes strict-dual single switches through support eight.  Its best
support-six row makes `A` Hamilton but leaves exactly one complementary
rank10/rank7 ticket.

A non-dual H-side support-eight circuit instead gives one quotient factor
cycle of voltage 9 and complete rank10, with only rank7 holes
`0x00e0f,0x01547`.  No one-shore single repair circuit through support eleven
closes those tickets.  With D frozen, the two immediate palette rows become
linear edge labels.  The resulting multiple-cycle provider-halo master is
DRAT-UNSAT at radius one (332 roots, 1,356 free H incidences); radius two
(1,266 roots, 9,246 free incidences) is UNKNOWN after its 300-second cap.

All exact statements, proof hashes, independent scope audits and the
fixed-D linear theorem are frozen in

```text
MATH_THEOREM_K17_COMPLEMENT_DUAL_SINGLETON_DIRECT_A_TOPOLOGY_LNS_20260801.md
```

These results solve only topology plus the immediate turn palettes in a
fixed seed family.  They do not discharge the free-type deletion spine,
residence, upper opening, deeper shadows or compiler gates of Sections 5--9.
