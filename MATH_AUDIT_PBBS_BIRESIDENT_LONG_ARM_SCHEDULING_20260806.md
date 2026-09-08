# Audit of two-sided PBBS long-arm scheduling

**Date:** 2026-08-06  
**Method:** exact run/gap interval scheduling and proof-scope audit; no
computation or finite search  
**Audited files:**

- `MATH_THEOREM_TAGGED_CONNECTOR_ANTECEDENT_SCHEDULING_AND_CAP_OBSTRUCTION_20260806.md`
- `MATH_THEOREM_LONG_ONE_TAG_PORT_ARMS_AND_RESIDENT_TAGGED_CHAIN_20260806.md`

## 1. Event inequalities

Let `V_0=A,...,V_ell=B` be a shortest Johnson geodesic.  A coordinate
`x in A-B` is deleted at edge `p`, and `y in B-A` is inserted at edge `q`.
If `lambda_+(x)` is the positive age at the left endpoint and
`rho_0(x)` the zero age at the right endpoint, then the two required
inequalities for the deletion are

\[
 \lambda_+(x)+p-1\ge\delta+1,
 \qquad
 \ell-p+\rho_0(x)\ge\delta+1.
\]

Thus

\[
 \delta+2-\lambda_+(x)\le p
 \le \ell+\rho_0(x)-\delta-1.
\tag{1.1}
\]

The insertion inequalities are the exact dual:

\[
 \delta+2-\lambda_0(y)\le q
 \le \ell+\rho_+(y)-\delta-1.
\tag{1.2}
\]

The endpoint counts in (1.1)--(1.2) are correct: `p-1` and `q-1` count
the internal owners strictly before the event, while `ell-p` and `ell-q`
count those at and after the changed state before the right endpoint age.

## 2. Unit-age lemma on both polarities

At a Johnson cut, among present coordinates, every positive age at most
`s` comes from one of the last `s` insertions.  Hence there are at most
`s`.  Among absent coordinates, every zero age at most `s` comes from one
of the last `s` deletions, so the same bound holds.  Reversing the trace
gives both right-age statements.  No residence assumption is needed for
this clipped-age bound.

## 3. Interval-Hall aperture

For unit jobs with nonempty interval lists `[r_j,u_j]`, Hall reduces to

\[
 \#\{j:r_j\ge a,\ u_j\le b\}\le b-a+1
 \quad(1\le a\le b\le\ell).
\tag{3.1}
\]

Assume `ell>=2delta+1`.  Every list (1.1) or (1.2) is nonempty because
its release is at most `delta+1` and its deadline is at least
`ell-delta>=delta+1`.

For a deletion job counted in (3.1),

\[
 \lambda_+(x)\le\delta+2-a,
 \qquad
 \rho_0(x)\le\delta+1+b-\ell.
\tag{3.2}
\]

If `b<=delta`, the second quantity is at most zero, so no job is counted.
If `b>=delta+1` and `a>=2`, the first quantity is at most `delta` and the
unit-age lemma bounds the count by

\[
 \delta+2-a\le b-a+1.
\]

If `b>=delta+1` and `a=1`, use the second quantity.  In the range
`1,...,delta` it is at most `b`; if it is nonpositive the count is zero;
if it is `delta+1`, then `b=ell` and the trivial total-job bound `ell=b`
applies.  This covers the clipped endpoint case omitted by the first draft
of the proof.  Insertion jobs are identical with the two polarities
interchanged.  Thus the `2delta+1` aperture is proof-safe.

Coordinates present at both endpoints have a positive interval across all
`ell+1` connector owners; coordinates absent at both have the analogous
zero interval.  Both exceed the required length.

## 4. Global segment order is not circular

The long-chain construction can be scheduled in three stages, so the age
profiles used by a connector are genuinely fixed rather than assumed.

1. Schedule every exit arm from its fixed block outward, using only the
   positive-left deletion releases and zero-left insertion releases.  A
   length `delta+1` arm suffices.  This exports concrete left-age profiles
   at its far port.
2. Schedule every entrance arm from its far port inward, using only the
   zero-right deletion deadlines and positive-right insertion deadlines.
   This exports concrete right-age profiles at its far port.
3. Schedule each connector against those two already fixed profiles using
   Section 3.  Its `2delta+1` distance aperture suffices.

The deletion and insertion permutations of a shortest Johnson path are
independent, so the two job systems do not create a hidden third matching.
The first-deleted and last-inserted pair tags have full positive and zero
ages through their adjacent arms.  Fresh one-edge whiskers additionally
require the swapped non-tag to have the appropriate full zero age; only
`delta` outside coordinates are excluded, so this choice is available in
the linear outside shore.

## 5. Distance supply

The one-tag arm has length `L=floor(R/4)`, and `delta=O(sqrt R)`, hence
`L>=2delta+1` for all sufficiently large `R`.  Its terminal constant-weight
shell has size `exp(Theta(R))`.  A radius-`2delta` Johnson ball has size at
most

\[
 (2\delta+1)R^{4\delta}=\exp(o(R)).
\]

Therefore `O(sqrt R)` far ports can be chosen pairwise at distance at least
`2delta+1`, while retaining the clean-resource geodesic event.  Their
shortest pair-tag connectors inherit the required aperture.

## 6. Exact scope

The audit passes the following statement:

> Conditional on biresident literal histories for the fixed pentagon and
> collar blocks, the long one-tag arms and pair-tag connectors can absorb
> all internal positive-run and zero-gap flags with no added source
> positions.

It does **not** prove any of the following:

1. the zero-gap half on the fixed pentagon halos;
2. biresident histories on unprotected completion cycles;
3. occurrence-bijective old/new common-history transport;
4. fusion of all residual factor cycles into one source chronology; or
5. typed common-cap suffix rank after compensation.

In particular, the raw one-step arm ports and their unique tag signatures
do not exclude a common unit-capacity typed suffix bottleneck.  The result
closes the long-chain residence/gap aperture, not the remaining literal
history or cap gates.

