# Proof audit: rolling-collar/upper-reservoir coextension and one-cycle residence bridge

**Date:** 2026-08-06  
**Audited theorem:**
`MATH_THEOREM_ROLLING_COLLAR_UPPER_RESERVOIR_COEXTENSION_AND_RESIDENCE_PORT_GATE_20260806.md`  
**Audited SHA-256:**
`86c25794c84f1b8e2ce72e4d531d38af59f028e2985d5a4b9efde7573f5c1c3b`  
**Method:** line-by-line mathematical dependency and quantifier audit; no
computation or finite search  
**Verdict:** **GO, with the scope stated in the theorem.**  The complete
low bank has one cyclic bi-resident protected realization, and it coextends
with the clipped-resident common-core upper-damage reservoir to an exact
owner/lower-`q1` factor.  Global upper completeness and decoration of the
residual factor remain open.

## 1. Cross-reservoir entropy

The common-core reservoir has `O(m2^m)` incidences.  Enlarging every role by
one middle-level neighbourhood costs only a polynomial factor, so its halo
has size `2^(m+o(m))`.

For a fixed target `S`, `|S|<=d=o(m)`.  Every collar or bridge halo role has
rank `m+O(1)` and fixes only `O(d)` coordinate labels.  Its pointwise-
stabilizer orbit has size

\[
                         2^{2m-o(m)}.
\]

There are `2^{o(m)}` collar/bridge roles and `2^{m+o(m)}` reservoir roles.
Thus the two collision budgets are respectively

\[
 2^{o(m)}2^{-2m+o(m)}=o(1)
\]

and

\[
 2^{m+o(m)}2^{-2m+o(m)}=2^{-m+o(m)}.
\]

This verifies both the original collar-bank separation and the stronger
one-cycle separation from the reservoir.

## 2. The explicit bridge

The outgoing marker phase is

\[
 B+R
 \to B+(R-r_0)+\ell_0
 \to\cdots\to B+L.
\]

It uses `d+1` exchanges.  The background phase then changes `B` to `B'`
one coordinate at a time while retaining `L`.  Cross-disjointness of
`R,L,B,B'` makes the concatenation a monotone Johnson geodesic of length

\[
 d+1+|B-B'|\le m.
\]

For `r_j`, the first collar supplies `d-j+1` owner occurrences and the
bridge supplies `j`; for `ell_j`, the bridge supplies at least `d-j`
before the next collar supplies `j+1`.  Both totals are `d+1`.  Background
coordinates persist through a complete collar on the side where they are
introduced or deleted.  The positive-residence calculation is exact.

## 3. Zero-gap check

No coordinate is both deleted and inserted in one bridge.  Each background
avoids all marker banks in a fixed-radius neighbourhood.  Therefore, after
a background coordinate disappears, it cannot return before a complete
intervening collar has passed.

Auxiliary markers are not reused locally.  A fixed target coordinate can
occur in consecutive target blocks, but then its two marker runs are
separated by the entire `d+1`-exchange marker bridge.  These exhaust the
possible locally consecutive appearances.  Hence every nonconstant zero
gap on the cyclic chain has length at least `d+1`.

## 4. Simplicity of the complete chain

Within a collar, its marker windows are a monotone Johnson geodesic.
Within a bridge, Theorem 6.1 is a monotone geodesic.  For adjacent phases,
the full incoming or outgoing auxiliary marker bank distinguishes all
nonshared roles; neighbouring backgrounds avoid those banks.

Any remaining role pair has disjoint background-variable support.  After
conditioning on its `O(d)` fixed labels, one role is invariant on a central
stabilizer orbit of size `2^(2m-o(m))` and is independent of the other.
The enlarged-halo pair count is

\[
                         O(m^4L_d^2)=2^{o(m)}.
\]

The union bound therefore excludes every nonlocal equality.  In
particular:

* no nonconsecutive protected owners share a lower facet;
* no ambient owner contains protected lower colours from two nonadjacent
  path positions; and
* no immediate-upper colour repeats.

Thus the one-cycle halo has

\[
 \ell(x)\le2,qquad z_U\le2,
\]

and has no endpoint term.

## 5. Source-ticket preservation

Every target position retains the complete local owner window used in

\[
 \bigcap_{h=0}^dT_{p-h}=B+z_p.
\]

The bridge begins only after the retained collar endpoint.  Since every
positive run on the global cycle has length at least `d+1`, the maximal-
antecedent theorem applies globally.  At a target position the mandatory
core remains the singleton `z_p=s_p`.  The target blocks occupy disjoint
physical positions, so all singleton thinnings may be made simultaneously.

## 6. Protected Ore transfer

Halo separation means the combined exposure is the maximum of the
reservoir and cycle exposures, not their sum.  Therefore

\[
 \ell_P(x)\le10,qquad e_P^{\rm priv}(x)\le10,qquad
 z_U(P)\le9.
\]

The common-core bank still has the only `2m` exceptional top endpoints,
and total protected size remains `O(m2^m)`.  The general maximum-degree-two
protected Ore criterion permits a protected cyclic component.  It has no
endpoint loss, so the small-shore estimate improves; the optional co-small
and near-shadow arguments are unchanged.  The exact residual `b`-matching
therefore gives a spanning two-factor containing both banks.

## 7. Exact scope

The audited theorem closes these rows simultaneously:

1. literal realization of every target of rank at most `d`;
2. one cyclic bi-resident host for the complete low bank;
3. simple owner, lower-`q1`, and upper-`q1` protected palettes;
4. the complete localized common-core upper-damage reservoir; and
5. exact protected owner/lower-`q1` factor extension.

It does not prove:

1. residence of the unprotected residual factor;
2. the global all-width upper deck outside the localized damage family;
3. `O(1)` components for the residual factor;
4. an upper-safe fusion/opening of the protected cycle;
5. terminal common-cap/compiler compatibility; or
6. `nu(k)<=B(k)+O(1)`.

Accordingly the theorem is a genuine decorated-skeleton closure, not the
full decorated-completion theorem.
