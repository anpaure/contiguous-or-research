# Independent audit: renewal blocks, forced-departure collars, and atomic separation

**Date:** 2026-08-04  
**Method:** independent symbolic proof replay; pure mathematics; no search,
solver, or finite computational census  
**Audited theorem:**
`MATH_THEOREM_RENEWAL_BLOCKS_FORCED_DEPARTURE_COLLARS_AND_ATOMIC_SEPARATION_20260804.md`  
**Audited theorem SHA-256:**
`96c994803f7af52a98583862c34365b4b610d403d073afbad08ab7df88d3f739`  
**Audited self-audit SHA-256:**
`6001a90299a436ed4bbde8b095b63ea432ff72f6d41cda91823949c998050d27`  
**Verdict:** **INDEPENDENT-GO at the stated fixed-oriented-walk,
right-aligned-collar scope.**

The renewal criterion, right-aligned uniqueness, canonical spelling,
forced future-intersection law, nested selector, depth-three Hall
reduction, and rank-identical separation example are exact.  During this
audit two scope/wording corrections were made before freezing the theorem:

1. the canonical time-to-departure statement now assumes, exactly as the
   underlying audited serialization theorem does, that no coordinate is
   present at every cyclic root; it also states the intended nonempty-full-
   flag range `q>=d`;
2. the paragraph following the collar-defect formula now refers to (4.7),
   not to the unrelated definition (4.4).

Neither correction changes the mathematical mechanism or the intended
complete-coatom-layer application.

## 1. Scope and cyclic conventions

The theorem fixes one oriented cyclic rank-`q` Johnson walk

\[
 Q_{i+1}=Q_i-\{\alpha_i\}+\{\beta_i\}.
\]

No coordinate is ubiquitous, so each positive cyclic run has a genuine
entry, a genuine departure, and a finite remaining-run time `tau_i(x)`.
The residence hypothesis says every such run has at least `d` roots.  This
is precisely the fixed-factor convention in the independently audited
flag-interval serialization theorem.  The additional `q>=d` assumption
ensures that the bottom canonical threshold has rank

\[
 q-(d-1)=q-d+1\ge1,
\]

so the displayed complete threshold chain is a nonempty strict flag.
Complete use of the rank-`q` layer implies non-ubiquity in the intended
application.

All arguments are componentwise.  They neither join different factor
cycles nor assert that a protected spanning two-factor has one component.

## 2. Renewal-block DAG equivalence

On a positive run indexed `0,...,ell-1`, a literal age path begins at zero,
ends at `d-1`, and at each survival step either resets to zero or increments
by one.  If `z` is its last zero, then

\[
 \ell-1-z=d-1,
 \qquad z=\ell-d.
\]

Consecutive zeros are at distance at most `d`, since a longer block would
attempt age `d` before its next renewal.  Inside a block starting at `z`,
the age at `t` is exactly `t-z`; hence the fixed interval constraints are
exactly (1.4) and (1.5).  Conversely, distances from the latest selected
renewal give only legal reset/increment transitions, respect every allowed
interval, and force the correct entry and terminal ages.  Thus the DAG is
neither a relaxation nor a strengthening of the run automaton.

When `ell=d`, the convention is the harmless degenerate case `s=0` and
`z_0=ell-d=0`; the sole final block is checked by (1.5).  No endpoint
condition is lost.

## 3. Right-aligned uniqueness and the absence of a later Hall choice

A right-aligned flag of length `m_i` has declared addresses

\[
 c_i,c_i+1,\ldots,d-1,
 \qquad c_i=d-m_i.
\]

For fixed ages, the literal suffix union at address `u` is the functional
sublevel set

\[
 \{x\in Q_i:a_i(x)\le u\}.
\]

Therefore every named member is forced to be

\[
 S^i_j=\{x\in Q_i:a_i(x)\le c_i+j-1\}.
\]

The displayed sets form a compatible flag exactly when they are nonempty
and strict.  Once the ages and cutoff are fixed, an occurrence has one set
value, so the maximum number of targets from a family carried by the table
is simply the number of distinct requested values present in the induced
deck.  There is no residual target-to-occurrence Hall competition.

This is only an age-first normal form.  It does not produce ages whose
value deck contains the required named targets.

## 4. Canonical time-to-departure spelling

For a present coordinate let `tau_i(x)` count the remaining roots in its
current positive run, including `Q_i`, and define

\[
 a_i^*(x)=\max(0,d-\tau_i(x)).
\]

Entry has `tau>=d` and age zero; departure has `tau=1` and age `d-1`.  For
a survivor, `tau` decreases by one.  Thus `2<=tau<=d` produces an age
increment, while `tau>=d+1` produces a legal zero-to-zero refresh.  These
are exactly the literal shift equations.  The reconstruction theorem for
the fixed age partitions then gives one cyclic source spelling; no extra
cross-coordinate condition is being assumed.

For `0<=j<d`, the next `j` departures

\[
 \alpha_i,\ldots,\alpha_{i+j-1}
\]

are distinct elements already present in `Q_i`.  A later entry followed by
one of these departures, or two such departures of the same coordinate,
would create a positive run shorter than `d`.  Hence

\[
 I_{i,j}=\bigcap_{u=0}^{j}Q_{i+u}
        =Q_i-\{\alpha_i,\ldots,\alpha_{i+j-1}\},
 \qquad |I_{i,j}|=q-j.
\]

At `Q_i`, the coordinate `alpha_(i+u)` has canonical age `d-1-u`; every
other present coordinate has age zero.  Therefore the age-`t` sublevel set
is exactly

\[
 F_t^i=I_{i,d-1-t}.
\]

This proves the canonical spelling and all its future-intersection
identities.  It also confirms the theorem's limitation: the canonical
word may contain many unselected duplicate central values.

## 5. Forced future-intersection collars in every spelling

The canonical choice is not needed for the rigidity statement.  In an
arbitrary literal spelling, `alpha_(i+u)` reaches terminal age `d-1` at
root `i+u`.  Tracing backward through `u<d` survival steps forces its age
at `Q_i` to be `d-1-u`; any intervening reset leaves too few increments to
reach terminal age.

If a right-aligned flag has consecutive top ranks `q-h,...,q`, its top
members occur at consecutive addresses `d-h-1,...,d-1`.  Consecutive rank
difference one forces each age class

\[
 C^i_{d-h},\ldots,C^i_{d-1}
\]

to be a singleton.  The forced departure queue occupies those singletons,
so deleting the top `j` age classes gives

\[
 S_{q-j}=Q_i-\{\alpha_i,\ldots,\alpha_{i+j-1}\}=I_{i,j}.
\]

Thus the theorem proves equality of named collar values, not merely owner
containment or an endpoint aperture.

## 6. Nested banks: exact necessity and collar-only sufficiency

Let `R_j` be the roots whose collar extends at least `j` steps below the
top.  These banks are nested.  If every rank-`q-j` collar target is used
exactly once, forced-collar rigidity makes

\[
 i\longmapsto I_{i,j}
\]

a bijection from `R_j` to the complete rank-`q-j` layer.  Conversely, if
such nested bijective banks are given, the single canonical spelling
contains every selected value at address `d-j-1`; nestedness makes the
selected values at each root one flag.

The converse is exactly collar-only.  It does not allocate lower residual
targets, suppress unselected canonical thresholds, bound duplicate waste,
or supply a safe linear opening.

## 7. Depth three reduces to one ordinary matching

For `d=3`, a root gives one multigraph edge

\[
 I_{i,2}\longleftrightarrow I_{i,1}.
\]

If nested banks exist, the roots in `R_2` use every depth-two colour once
and distinct depth-one colours, hence form a matching saturating the
depth-two shore.  The depth-one deck is necessarily surjective.

Conversely, choose a matching saturating the depth-two shore and use its
distinct root indices as `R_2`.  For each unused depth-one colour,
surjectivity supplies a root in that colour's fibre.  Those fibres are
pairwise disjoint, and none meets `R_2` because the matching used different
depth-one colours.  Adding one root from each fibre produces `R_1` and the
required bijection.  This proves both directions without a three-way
integrality assumption.

## 8. Rank-identical good/bad separation

At depth two, let

\[
 Q=\{1,2,4\},\qquad Q'=\{1,3,4\},
\]

with old bottom member `{1}`.  Both new bottom members `{3,4}` and `{1,3}`
have rank two, contain the newborn `3`, and share the same root, address,
row-load, rank-histogram, containment, and endpoint-aperture data.

For `{3,4}`, the new terminal class is `{1}`, contained in the old age-zero
class `{1}`; the survivor transition is literal.  For `{1,3}`, the new
terminal class is `{4}`, not contained in the old age-zero class; survivor
`4` would have to remain at terminal age one, whereas its only legal next
move is reset to zero.  Hence this turn is impossible.

The example proves a local rank-only separation.  It does not assert that
either two-root fragment extends to a complete resident owner-exact
factor, and the theorem says so explicitly.

## 9. Exact proof boundary

The audited theorem is consistent with, and strictly refines, the earlier
fixed-flag serialization theorem.  It proves:

* an exact renewal-DAG reparameterization of each already fixed run
  automaton;
* one canonical accepting spelling on every factor satisfying its stated
  residence and scope hypotheses;
* rigidity of every selected right-aligned consecutive top collar; and
* an exact nested-colour selector, with an ordinary-Hall reduction at
  depth three.

It does **not** prove:

* existence of the nested bijective root banks on a protected factor;
* an atomic-to-named renewal lift for ranks below `r-d`;
* coefficient-one or bounded-waste lower coverage;
* connectedness, upper completeness, component fusion, or a safe opening;
* preservation of `Lambda-O(1)` marks through that opening; or
* `nu(k)<=B(k)+O(1)`.

Within those exclusions, the theorem is independently proof-safe.
