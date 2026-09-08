# Audit of the residence-redistribution automaton and the `m=5` endpoint lock

Date: 2026-07-31  
Status: independent mathematical and deterministic-replay audit PASS after
the scope corrections recorded below

## 1. Scope

This note audits

```text
MATH_THEOREM_AD_RESIDENCE_REDISTRIBUTION_AUTOMATON_AND_M5_ENDPOINT_LOCK_20260731.md
MATH_THEOREM_AD_M5_RESIDENCE_RETHREAD_REGENERATION_AND_29_SEAM_OBSTRUCTION_20260731.md
scratch/audit_ad_m5_residence_clean_triple_endpoint_obstruction_20260731.py
scratch/ad_m5_residence_clean_triple_endpoint_obstruction_20260731.audit.json
```

against the frozen residence-clean `m=5` matching of item2188.  It does not
audit an all-`m` construction, a joined `m=5` chronology or a compiler
matching; none is claimed.

Two proof audits were performed independently.  One checked the run budget,
capped automaton, endpoint-lock implication and every finite count.  The
other checked the erosion-envelope support formulas and their cyclic versus
linear scope.  Both pass after the corrections in Section 5.

## 2. General mathematics

Let

\[
 M={2m\choose m},\qquad N={2m\choose {m-1}},\qquad
 K=M-N=\operatorname {Cat}_m.
\]

For any two-sided-rainbow Catalan path forest, a fixed coordinate occurs on
\({2m-1\choose m-1}\) middle vertices and on
\({2m-1\choose m-2}\) selected edges.  Their difference is exactly (K),
so there are (K) component-runs in that coordinate.  A Johnson seam merges
one run for each of its (m-1) common coordinates.  Hence after (c) seams
the total run count is

\[
                         2mK-(m-1)c.
\]

The Hamilton-path and cyclic values are respectively

\[
                         (m+1)K+m-1,qquad (m+1)K.
\]

Since the cyclic one-mass is (mM=m(m+1)K), the cyclic average positive-run
length is exactly (m).  These identities are unconditional.  Only the
comparison (d+1=\Theta(\sqrt m)) belongs to the intended calibrated
compiler regime.

The automaton on states

\[
                         \{0,1,\ldots,D,\star\}
\]

is exact.  The initial state `star` exempts precisely the positive run which
touches the left endpoint; the undefined transition from an ordinary state
(1,\ldots,D-1) on a zero catches precisely a bounded short run; accepting
every final state exempts precisely the run which touches the right
endpoint.  Composition of the component transformations is therefore an
if-and-only-if characterization for a fixed oriented component word.

The endpoint-lock theorem is a necessary implication only, as stated.  A
component used internally in a resident word must be the centre of a
resident predecessor--component--successor triple.  Thus more than two
components having no such triple precludes a linear joining.  The converse
is neither stated nor true, since a short run may span more than three
components.  The immediate-safe inequalities are a sufficient subclass;
an all-one component may transport a short open run and make them
unnecessarily strict.

## 3. Exact finite replay

The deterministic replay reconstructs the item2188 perfect diamond
matching, its `210` Johnson edges and its `42` path components.  It verifies
that every strictly internal positive coordinate run has length at least
three.  It then enumerates, without SAT or stochastic search,

\[
\begin{array}{c|r}
\text{oriented component states}&84\\
\text{directed Johnson connector arcs}&608\\
\text{formal unoriented port pairs}&304\\
\text{distinct physical connector edges}&293\\
\text{oriented predecessor--centre--successor candidates}&4270\\
\text{resident oriented triples}&220.
\end{array}
\]

Exactly the following fourteen components have no resident centre triple in
either orientation:

\[
             0,5,10,14,15,20,21,27,29,31,34,36,38,39.
\]

A linear word has only two endpoint slots.  Therefore every orientation and
permutation of these forty-two intact paths fails depth-two residence.  This
is a solver-free implication and does not depend on the deeper service
rows.

The replay also verifies a raw one-seam provider for each of the twenty-one
fixed-width/depth-aligned deep debts.  The counts distinguish oriented-state
arcs from distinct physical connector edges.  In particular `0x1f6` and
`0x375` each have only one distinct physical provider edge.  These are
individual zero-host checks only: no residence, distinct-port, connector-
colour, connectivity or simultaneous-scheduling condition is imposed.

## 4. Independent support lower bound

The old `31` internal `0110` runs have exact interval packing/transversal
number `29`.  At equality there are `84` candidate deleted edges and `427`
loopless lower-to-upper palette arcs.  The exact degree-at-most-two
relaxation has `511` variables and `15,154` clauses.  Its DRAT proof and the
extracted core both verify independently.  Since acyclicity was omitted,
UNSAT of this relaxation proves that no support-29 two-palette physical
path-forest rethread exists.

Together with the item2188 support-119 witness, this gives the scoped
central-subsystem bracket

\[
                         30\le s_{\rm int}\le119.
\]

The bracket concerns exact q1 palettes, middle degree/forest topology and
path-internal residence.  It does not assert feasibility at support `30`,
endpoint joining, deeper flags or compiler Hall at support `119`.

## 5. Corrections applied during audit

The final theorem text incorporates all of the following:

1. an unauthenticated sentence saying a finite model closed in presolve was
   removed; the fourteen-lock proof needs no solver;
2. the `21` debts are called fixed-width/depth-aligned flag debts, not the
   arbitrary-width upper/compiler service list;
3. the calibrated (d+1=\Theta(\sqrt m)) comparison is separated from the
   unconditional run identity;
4. (b_\ell=\sum_P\min(\ell,|P|)) is stated for maximal common fragments of
   cyclic closures; for a fixed linear opening the changed internal start
   set is a subset of that boundary family, and changed endpoint halos are
   listed separately;
5. the (b_{h+1}\) compiler bound is restricted to occurrence-aligned,
   transported OR values.  Absolute-position pins, controller footprints
   and nonaligned representative choices need additional phase support;
6. oriented-state provider counts and distinct physical-edge counts are
   both displayed, with no simultaneous matching inference; and
7. the older regeneration note now says that no joined all-depth/compiler
   chronology is claimed, rather than denying the internally clean rethread
   supplied by item2188.

## 6. Frozen hashes

At this audit freeze:

```text
MATH_THEOREM_AD_RESIDENCE_REDISTRIBUTION_AUTOMATON_AND_M5_ENDPOINT_LOCK_20260731.md
  4230331d35b89b52fa9a244f272e9628426da74a08683319eec634655a094771
MATH_THEOREM_AD_M5_RESIDENCE_RETHREAD_REGENERATION_AND_29_SEAM_OBSTRUCTION_20260731.md
  427bd6eb41f3aa7667825637b7ad0aba9dd0f25ae89252fb312d011c73e73757
MATH_AUDIT_AD_M5_INTERNAL_RUNSPAN_TRANSVERSAL_20260731.md
  d9956bf573aa47ae660d67d0409b00a2c15fb72c65afdf0204d9f5cffaadd75a
scratch/audit_ad_m5_residence_clean_triple_endpoint_obstruction_20260731.py
  5caa1f40fb25ec5bd9e7c4c830cd324f7c42aefd871314a6c9ed2c7ef24a8268
scratch/ad_m5_residence_clean_triple_endpoint_obstruction_20260731.audit.json
  20ef12db7867d4b3c64b6ddab6e02034eb6ed4242a6709ec518992c024f23301
```

The endpoint JSON canonical payload is

```text
c251bab8047d5ec7773533daf4b3dc8768b8b10ff3eba829bcffabdf89a474d2
```

The support-29 proof artifacts are:

```text
scratch/audit_ad_m5_tau29_degree2_unsat_20260731.py
  d726bde5afff0be6270d5df183ca599009839091802c03532e43e7196237051d
scratch/ad_m5_tau29_degree2_20260731.cnf
  eb542e3ee0f3c3a8829c5c278c71c2df159585e2740b11cbf62f4f67ecfa2c1c
scratch/ad_m5_tau29_degree2_20260731.drat
  65dd5aaca70ffdcd0e1ef0693a8276f235b65774c0f936fd92ad74bfc2c9c129
scratch/ad_m5_tau29_degree2_unsat_20260731.audit.json
  0c29befc651b55e5a6fcff20eaef44f54d41739438bf5a7f6525df9c85b03950
```

The last JSON has canonical payload

```text
5b69c235d467b70c0e0212ecd539b5b1a8af46325a482a6722ed58c81a333a72
```

## 7. Exact remaining gate

The residence-clean item2188 matching proves that central residence is not
intrinsically impossible.  Its intact component bank is nevertheless
endpoint-locked.  A successful next object must change path interiors again
so that at most two components remain locked (or avoid that component bank),
retain both q1 palettes and forest topology, service all deep debts in one
resident literal chronology, and only then satisfy the erosion/compiler
Hall rows.  No all-`m` construction supplying those correlated choices has
been proved.
