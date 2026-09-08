# Final GO audit: factor-first trace slices and the Pascal endpoint connector

**Date:** 2026-08-04  
**Method:** independent pure mathematics; no search, solver, sampled
computation, or H100 work.  
**Verdict:** **GO after two exact corrections.**  The corrected theorem is
an unconditional reduction to a physical endpoint matching with prescribed
quotient topology.  It does **not** prove that this matching exists, does
not prescribe its endpoints, and imports no residence, deeper-upper, or
common-cap conclusion.

## 0. Frozen audited object and dependencies

The audited successor is

`MATH_THEOREM_FACTOR_FIRST_TRACE_SLICE_PASCAL_CONNECTOR_REDUCTION_20260804.md`

with SHA-256

`5556951c9fd8abcf9c1997d3939e8ca8bbb1492ca38e6da87eda4cdfa3dd4e03`.

Its three named dependencies have the following exact hashes:

- `MATH_THEOREM_CYCLIC_COMMON_HISTORY_HINGE_RING_AND_SHORT_DECK_INVARIANCE_20260804.md`  
  `96b9f8717c138dfac7df2a4d1c439392de1a3313c9e57114d2e1cd6f145b90ba`;
- `MATH_THEOREM_COMMON_CORE_HYBRID_CLIPPED_RESIDENT_WITNESS_RESERVOIR_20260804.md`  
  `f9cd82ff39c3fb6979bd2c70e92223af6f7bb171d4ede422a023b7d2c6809314`;
- `MATH_THEOREM_Q1_RAINBOW_JOHNSON_SATURATING_INTERFACE_20260726.md`  
  `fbcb016be136c5348aecb67ad8ae281a72d921ca178cf0e6642f74a38459ef6d`.

The corrections made during audit were:

1. the residual-label formula in (4.2) is
   \[
   r_T=\max\{0,l_q-v_q+1\},
   \]
   not a maximum with `1`; in the label-smaller chamber every same-trace
   label is used and `r_T=0`;
2. the introductory and post-Theorem-4.1 witness claims now explicitly
   concern nonempty damage traces below the co-singleton rank.  The empty
   and full traces are boundary slices and were never proved to have a
   component whose union is `K union T`.

The first correction is substantive at the displayed-formula level but
agrees with the proof and with Section 5's `r_T=0` ledger.  Neither
correction changes the endpoint reduction.

## 1. Difference-one coordinates and trace-slice counts

For an owner `U`, let `T=U cap E` and `A=K setminus U`.  The rank equation

\[
 (m-1-|A|)+|T|=m
\]

is equivalent to `|T|=|A|+1`, giving the unique owner coordinate

\[
 u(A,T)=(K\setminus A)\cup T.
\]

For a lower vertex `x`, the analogous equation is `|S|=|B|`, giving

\[
 \ell(B,S)=(K\setminus B)\cup S.
\]

Containment between these two ranks differs by one literal coordinate.
Adding a `K` coordinate gives `T=S` and `B=A+a`; adding an `E`
coordinate gives `A=B` and `T=S+e`.  These alternatives are disjoint and
exhaust all incidences.  Therefore a fixed trace of size `q` has exactly

\[
 v_q={m-1\choose q-1},\qquad l_q={m-1\choose q}
\]

owner and same-trace lower vertices, and its same-trace incidence graph is
the subdivision of the consecutive-level incidence graph on `K`.

The boundary conventions are important and consistent: at `q=0` there is
one residual lower vertex and no owner; at `q=m` there is one owner and no
same-trace lower vertex.  These boundary slices participate in the global
connector ledger but not in the proper common-history damage family.

## 2. Exact endpoint-completion equivalence

A forest edge between owner indices `A,A'` has the unique label
`B=A union A'`.  Label injectivity therefore makes the lifted slice paths
vertex-disjoint on both shores.  A nontrivial path has precisely two
missing owner incidences; a singleton is correctly represented by two
labelled missing-incidence slots.

After the slice paths are fixed:

- every internal owner already has degree two;
- every used same-trace lower vertex already has degree two;
- every component has exactly two endpoint slots;
- every residual lower vertex needs exactly two incidences.

Consequently a matching of all endpoint slots to both capacity copies of
all residual lower vertices is exactly the residual degree equation.  The
extra physical rule for a singleton is necessary and sufficient: it
forbids using the same simple owner--lower incidence twice.  No analogous
rule is needed for a nontrivial path because its endpoint owners are
distinct.

Conversely, the residual incidences of any spanning two-factor give such a
physical matching.  Thus Theorem 2.1 is a true iff statement.  It is an
iff for the defined **physical** matching, not a claim that ordinary Hall
alone automatically enforces the singleton rule or the requested cycle
partition.

Suppressing each slice path preserves connectivity.  In the quotient,
every component vertex and every residual-lower connector vertex has
degree two.  Hence quotient cycles and completed-factor cycles correspond
bijectively, including the harmless possibility of a two-vertex parallel
cycle in the quotient.  A one-cycle completion is therefore exactly a
connected alternating 2-factor on `mathscr C sqcup mathscr R`; a requested
cycle partition is an additional constraint on the physical matching, not
an existence consequence.

## 3. Pascal balance and the prefix square

For a trace `T`, a forest on `v_q` vertices with `b_T` components uses
`v_q-b_T` labels, so

\[
 r_T=l_q-v_q+b_T.
\]

The component choices cancel after summing within trace size `q`:

\[
 R_q-C_q={m\choose q}(l_q-v_q).
\]

With `a_q={m-1 choose q}`, Pascal gives

\[
 {m\choose q}=a_q+a_{q-1},\qquad l_q-v_q=a_q-a_{q-1},
\]

and therefore

\[
 R_q-C_q=a_q^2-a_{q-1}^2.
\]

Summing through rank `q` gives exactly `a_q^2`.  At `q=m`, with
`a_m=0`, this yields `|mathscr R|=|mathscr C|`.  This verifies both the
global endpoint balance and the stated Pascal prefix-square identity with
no assumption that the individual `b_T` are equal.

## 4. GMM saturating-cycle applicability and the slice cover

The invoked dependency records the exact Gregor--Mička--Mütze corollary:
the incidence graph between two consecutive nonextreme Boolean levels has
a simple cycle saturating its smaller shore.  Here the ambient cube has
dimension `n=m-1`, and

\[
 2\le q\le m-2
 \quad\Longleftrightarrow\quad
 1\le q-1<q\le n-1.
\]

Thus neither degenerate star pair `(0,1)` nor `(n-1,n)` is invoked.  The
two shores have sizes `v_q` and `l_q`, so the theorem applies exactly in
the two cases used in Theorem 4.1.  The dependency supplies only this
simple saturating cycle; it supplies no preferred cut, endpoint,
residence, deeper upper deck, or probability law.

If `v_q<=l_q`, projection of the simple saturating cycle gives a cycle on
all `v_q` owner indices with `v_q` distinct labels.  Removing one projected
edge gives one Hamilton path, hence

\[
 b_T=1,qquad r_T=l_q-v_q+1.
\]

If `v_q>l_q`, the cycle contains all `l_q` labels and `l_q` owner indices.
An outside owner `A_*` has a rank-`q` superset `B`, and every such label is
on the cycle.  Replacing one incidence at `B` by `A_*B` opens the cycle
into one alternating path using all `l_q` labels and `l_q+1` owners.
Keeping the other owners as singletons gives

\[
 b_T=v_q-l_q,qquad r_T=0.
\]

These two chambers are exactly

\[
 b_T=\max\{1,v_q-l_q\},\qquad
 r_T=\max\{0,l_q-v_q+1\}.
\]

In the first chamber the distinguished path contains every
`(q-1)`-subset `A` of `K`; their intersection is empty because
`1<=q-1<=|K|-1`.  In the second chamber every rank-`q` label occurs on the
distinguished path, and for each `x in K` there is such a label avoiding
`x`; an incident owner index also avoids `x`.  In either case the union of
the actual owners is exactly `K union T`.  At `q=1`, the unique owner is
literally `K union T`.  Thus the deterministic witness conclusion is
valid for every damage trace with `1<=|T|<=m-2`.

## 5. Co-singletons and the cross-trace witness interface

For `|T|=m-1`, owner indices are the `(m-2)`-subsets of the `(m-1)`-set
`K`, so every actual owner contains exactly one `K` coordinate.  There is
only one same-trace lower label, `B=K`.  A simple two-factor can use it
between at most two owners.  Hence a same-trace component contains at most
two `K` coordinates, which is short of all of `K` when `m>=4`.  The no-go
is exact.

Using that sole label once gives one two-owner path and `m-3` singletons,
so `b_T=m-2=v_q-l_q` and `r_T=0`.  This independently confirms that the
correct formula in Section 4 must allow zero residual labels.

For each cyclic co-singleton `T_(i,m-1)`, all components in the nested
trace slices `T_(i,q)` lie inside `K union T_(i,m-1)`.  The first
`q=1` component already contains every coordinate of `K`, and the nested
external traces together contain `T_(i,m-1)`.  Therefore any genuinely
consecutive quotient segment through the displayed components has union
exactly `K union T_(i,m-1)`.  This proves Section 7's sufficient witness
claim.  It does not prove that the endpoint connector contains those
segments.

## 6. Literal ring-hinge identification

With `K=B union {b}` and the full external cyclic order, direct substitution
gives

\[
 L_i=u(\varnothing,\{a_i\}),\qquad
 I_i=\ell(\{b\},\{a_i\}),\qquad
 R_i=u(\{b\},\{a_{i-1},a_i\}).
\]

The `q=1` slice is a singleton and uses no same-trace lower label, so
`I_i` is residual.  In the `q=2` slice the projected saturating cycle is a
Hamilton cycle on singleton indices; cutting an edge incident with `{b}`
makes `{b}` a path endpoint.  Therefore `I_i` is literally eligible to
join the required `q=1` and `q=2` endpoint slots.  It is not a second copy
or an abstract colour identification.

The alternative owner

\[
 R_{i+1}=u(\{b\},\{a_i,a_{i+1}\})
\]

is adjacent through the same lower vertex `I_i`.  Reassigning that one
endpoint incidence is consequently exactly the cyclic ring-head switch
of the frozen hinge theorem and changes no slice forest.  This verifies
the literal connector interpretation.  It does not prove that the
remaining endpoint choices coexist with the switch.

## 7. Scope firewall

The corrected theorem proves only:

1. exact slice path covers with deterministic common-core witnesses below
   the co-singleton rank;
2. the co-singleton same-trace no-go and a sufficient cross-trace chain
   interface;
3. exact equality and prefix-square counts for residual endpoints;
4. equivalence between factor completion and one physical endpoint
   matching, with quotient topology read literally;
5. literal inclusion of the old ring hinges among connector choices.

It does **not** prove any of the following:

- existence of the physical endpoint matching;
- a prescribed endpoint or prescribed cycle partition from GMM;
- that a completed factor is connected;
- residence of the expanded chronology;
- preservation or completion of arbitrary-width upper targets outside the
  explicitly identified common-core component witnesses;
- a terminal lower/common-cap compiler;
- regeneration in the Pascal lift;
- `nu(k)<=B(k)+O(1)` or exact all-`k` equality.

The hybrid clipped-resident reservoir is cited only to explain why the
co-singleton exception has a known cross-trace local geometry.  Its
residence conclusion is not transferred to an arbitrary endpoint-factor
completion.  Likewise, the hinge theorem supplies the literal local
switch identity, not global planting under all guards.

Subject to this firewall, the corrected factor-first reduction is
mathematically sound.
