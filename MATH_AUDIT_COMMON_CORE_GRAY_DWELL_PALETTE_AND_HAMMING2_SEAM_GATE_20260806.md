# Audit of the common-core Gray dwell: exact palette signs and the Hamming-two seam obstruction

**Date:** 2026-08-06  
**Audited file:**
`MATH_THEOREM_COMMON_CORE_GRAY_SPINE_AND_RESIDENT_DWELL_REDUCTION_20260806.md`  
**Audited SHA-256:**
`106a88052714a4cb770e275e52d2b89c76191bdb8fc34e44bfc22851d86ad741`  
**Method:** exact cyclic-window and incidence-palette algebra; no
computation or search  
**Verdict:** the Boolean-to-Johnson spine, cyclic dwell, one-bit owner ports,
and square-Gray trace ordering are correct.  They do not yet give one
simple incidence chronology.  The exact missing content is stronger than
an unused intermediate owner: one-bit opening signs must obey a rank-step
law, and a two-add/two-delete seam has a one-intermediate palette
obstruction.

## 1. Inputs which audit cleanly

For `q=|T|` and

\[
 U(T)=\left(K-\{k_1,\ldots,k_{q-1}\}\right)\cup T,
\]

adding one external coordinate deletes `k_q`, so Theorem 1.1 is exact.
The external trace proves owner injectivity.

For the dwell block

\[
 V_{T,j}=T\cup W_j^h,qquad h=m-q,
\]

the cyclic `K`-windows give one positive run of length `h` and one zero
gap of length `q-1` for every `K` coordinate.  In the central band

\[
 d+2\le q\le m-d-1,
\]

both are at least `d+1`.  Owners belonging to different traces are
automatically distinct.

The phase-propagated nesting in Theorem 4.1 is also exact at owner level.
The saturating-cycle insertion in Theorem 5.1 gives a cyclic ordering with
trace Hamming distance at most two.  Under the spine map, equal-size
Hamming-two steps have Johnson distance one, while two-add/two-delete steps
have Johnson distance two.

## 2. Missing palettes of one opened dwell

Open the dwell cycle for a trace `T` by deleting the edge between the
adjacent cyclic windows

\[
                         W_a^h,qquad W_{a+\epsilon}^h,
 \qquad \epsilon\in\{+1,-1\}.
\]

The opened path starts at `W_a^h` and ends at `W_(a+epsilon)^h`.  Its one
missing lower and upper colours are

\[
 L_T(a,\epsilon)
 =T\cup\left(W_a^h\cap W_{a+\epsilon}^h\right),       \tag{2.1}
\]

and

\[
 A_T(a,\epsilon)
 =T\cup\left(W_a^h\cup W_{a+\epsilon}^h\right).       \tag{2.2}
\]

Every other internal dwell colour remains present.  A global simple
incidence chronology may reuse `(2.1)` or `(2.2)` at the seam, but may not
reuse any retained internal colour.

## 3. Exact sign law at one-bit seams

### Theorem 3.1 (palette-safe one-bit sign law)

Suppose

\[
                         T'=T\cup\{e\},
\]

so the new `K`-window length is `h-1`.  Use the phase-propagated owner seam
of Theorem 4.1.  Let `epsilon` be the opening sign of the `T` dwell and
`eta` the opening sign of the `T'` dwell.  The seam lower and upper colours
are both new relative to the retained dwell palettes if and only if

\[
                         \boxed{\epsilon=\eta=+1}.     \tag{3.1}
\]

For a deletion step `T to T-{e}`, the corresponding condition is

\[
                         \boxed{\epsilon=\eta=-1}.     \tag{3.2}
\]

#### Proof

For an addition, put `b=a+epsilon`, the phase of the old endpoint and new
start.  The seam lower colour is

\[
                         T\cup W_b^{h-1}.             \tag{3.3}
\]

If `epsilon=+1`, `(3.3)` is exactly the missing lower colour `(2.1)` of
the old dwell.  If `epsilon=-1`, it is a retained cyclic `(h-1)`-window
colour of that dwell and hence repeats a protected lower vertex.

The seam upper colour is

\[
                         T'\cup W_b^h.                 \tag{3.4}
\]

For the new `(h-1)`-window dwell, `(3.4)` is its missing upper colour
exactly when `eta=+1`; for `eta=-1` it is retained.  This proves `(3.1)`.
Reverse all inclusions for a deletion to obtain `(3.2)`.  \(\square\)

### Corollary 3.2 (pure one-bit Gray cycles cannot be palette-simple)

No nonconstant cyclic one-bit Gray ordering of traces, expanded by one
opened dwell per trace as above, is a simple lower-`q1` and upper-`q1`
incidence chronology.

#### Proof

The cyclic rank sequence has a local maximum and a local minimum.  At a
local extremum the incoming and outgoing one-bit steps have opposite signs,
while Theorem 3.1 requires the one opening sign of the intervening dwell to
equal both.  \(\square\)

Thus Corollary 1.2's multiplicity-two bound is not itself harmless for a
protected incidence skeleton.  A repeated lower colour is literally a
repeated lower vertex.

## 4. Same-rank Hamming-two seams are valid sign resets

Let

\[
                         T'=T-\{e\}+\{f\}
\]

have the same size as `T`, and use the same cyclic `K` window `W` at the
two seam owners.  Then the owners are Johnson adjacent.  Their seam colours
are

\[
 (T\cap T')\cup W,qquad (T\cup T')\cup W.            \tag{4.1}
\]

The external traces in `(4.1)` have sizes `q-1` and `q+1`, whereas every
internal colour of either adjacent dwell has external trace `T` or `T'`.
Hence the seam is locally palette-fresh, independent of the two opening
signs.

Consequently an equal-rank exchange can separate an increasing one-bit
run from a decreasing one-bit run and reset the sign required by Theorem
3.1.  This is the useful part of the square-Gray ordering.

## 5. One intermediate owner does not solve a two-add seam

The other Hamming-two type is genuinely different.

### Theorem 5.1 (one-intermediate collision dichotomy)

Let

\[
 T'=T\cup\{e,f\},\qquad |T|=q,qquad h=m-q,
\]

and take seam owners

\[
 O=T\cup W,qquad N=T'\cup W',                       \tag{5.1}
\]

where `W` is a cyclic `h`-window, `W'` is a cyclic `(h-2)`-window, and
`W' subset W`.  Any two-edge Johnson path `O-X-N` has, after exchanging
`e,f` if necessary,

\[
 X=(T\cup\{e\})\cup H,qquad
 W'\subset H\subset W,qquad |H|=h-1.                \tag{5.2}

Let `C=T union {e}`.  The first edge has upper colour

\[
                         C\cup W,                    \tag{5.3}
\]

and the second has lower colour

\[
                         C\cup W'.                   \tag{5.4}
\]

Both are colours of the cyclic dwell for the intermediate trace `C`.
They can both be absent from its opened path only when `W` and `W'` are
respectively the union and intersection of one adjacent pair of cyclic
`(h-1)`-windows.  In that case `H` is one of those two cyclic windows, so
`X` is already an owner of the `C` dwell.  Otherwise at least one of
`(5.3)`--`(5.4)` repeats a retained protected colour.

Therefore one intermediate owner cannot simultaneously be fresh in the
owner row and palette-safe.

#### Proof

Every common neighbour of the distance-two owners in `(5.1)` must perform
one of the two external insertions and one of the two `K` deletions, giving
`(5.2)`.  Equations `(5.3)`--`(5.4)` follow by union and intersection.

The internal upper colours of the `C` dwell are `C` plus cyclic
`h`-windows, and its internal lower colours are `C` plus cyclic
`(h-2)`-windows.  Opening that dwell removes exactly the paired union and
intersection belonging to one adjacent dwell edge.  Hence both seam
colours are missing exactly in the paired case stated.  The two
intermediate `K`-windows on that edge are precisely the only
`(h-1)`-sets between its intersection and union, so `H` is one of them.
This repeats an owner already used in the dwell.  \(\square\)

The deletion case is the reverse statement.

This proves that the phrase “a distance-two seam needs at most one
intermediate owner abstractly” is correct only at owner-graph level.  One
fresh intermediate is insufficient in the decorated incidence chronology.

### Theorem 5.2 (endpoint-deleted cube ordering avoids two-add seams)

For every `m>=2`, the nonempty proper subsets of an `m`-set admit one
cyclic ordering in which every consecutive pair is either at Hamming
distance one or is a same-rank one-exchange pair.  Under the spine map,
every such seam is one Johnson edge.  In particular, no two-add or
two-delete seam, and hence no instance of Theorem 5.1, is forced at the
trace-order level.

#### Proof

Take any Hamilton cycle of the `m`-cube and delete the vertices `emptyset`
and `E` from its cyclic order.  These two vertices are nonadjacent when
`m>=2`.  The two neighbours of `emptyset` are distinct singletons, so the
new seam across that deletion is a same-rank one-exchange pair.  The two
neighbours of `E` are distinct co-singletons, and give the second
same-rank one-exchange seam.  Every other consecutive pair remains an edge
of the cube.  The spine identities in Sections 1 and 4 convert both types
of trace step into Johnson adjacency.  \(\square\)

This theorem is only a trace-order simplification.  A one-bit edge still
obeys the opening-sign law of Theorem 3.1, so a local maximum or minimum of
the cube rank sequence can demand incompatible signs at its middle dwell.
Moreover, the physical seam still needs a noncolliding `K`-profile and all
split residence flags must be continued.  Thus Theorem 5.2 removes the
two-add/two-delete ear from the list of logically necessary trace steps;
it does not by itself construct the decorated chronology.

## 6. The opening exports a linear-size flag vector

Deleting the edge between two adjacent `h`-windows cuts through

* `h-1` positive `K`-runs, one for every coordinate in their intersection;
  and
* `(m-1)-(h+1)=q-2` zero gaps, one for every coordinate outside their
  union.

Thus one opened dwell exports

\[
                         (h-1)+(q-2)=m-3             \tag{6.1}
\]

split run/gap flags.  They are highly structured cyclic-interval flags,
but they are not one scalar or one coordinate flag.  The phase nesting in
Theorem 4.1 may automatically continue many of them; the remaining lemma
must state and prove that continuation explicitly.

## 7. Zero-spare trace-label factor reduction

For the symmetric central band put

\[
 a=d+2,qquad b=m-d-1,
\]

and define

\[
 \mathcal B=\bigcup_{q=a}^{b}\binom Eq,qquad
 \mathcal C=\bigcup_{s=a-1}^{b-1}\binom Es.           \tag{7.1}
\]

By binomial symmetry,

\[
 |\mathcal C|-|\mathcal B|
 =\binom m{a-1}-\binom mb=0.                         \tag{7.2}
\]

Make a bipartite graph `H` between `mathcal B` and `mathcal C` by joining
`T` to `S` exactly when

\[
                         S=T
 \quad\hbox{or}\quad
                         S\subset T, |T-S|=1.        \tag{7.3}
\]

The diagonal in `(7.3)` is present only when `S` lies in both displayed
bands.

### Theorem 7.1 (trace chronology equals an alternating factor)

A cyclic ordering of all traces in `mathcal B`, using only one-bit
inclusion seams and same-rank one-exchange seams, has pairwise distinct
external lower-colour labels if and only if its subdivision by those
labels is an alternating Hamilton cycle of `H`.

More generally, a disjoint union of such trace cycles is exactly a spanning
two-factor of `H`.

#### Proof

For a one-bit seam `T subset T'`, the external trace of the lower colour is
`T`.  In `H`, this is the two-edge segment

\[
                         T-T-T',                     \tag{7.4}
\]

using the diagonal incidence followed by containment.

For a same-rank exchange seam, the lower trace is

\[
                         S=T\cap T',
\]

and the corresponding segment is

\[
                         T-S-T'.                     \tag{7.5}
\]

Conversely, any two-edge segment of `H` between distinct trace vertices
has one of the forms `(7.4)`--`(7.5)`.  Subdividing every chronology seam
therefore gives a two-regular alternating subgraph.  Distinct lower labels
mean its `mathcal C` vertices are distinct.  Equation `(7.2)` makes the
construction zero-spare: a cyclic chronology has `|mathcal B|` seams and
must use every member of `mathcal C`.  Connectedness is exactly the
Hamilton condition.  \(\square\)

This reduction also identifies the remaining phase coupling.  If a seam
has external lower label `S in mathcal B`, then the `K` part of that seam
must be exactly the one lower colour omitted when the dwell cycle for `S`
was opened; otherwise it repeats a retained lower vertex of that dwell.
For `S in mathcal C-mathcal B` there is no `S`-dwell and no such collision.

Thus the **external-label-rainbow face** of the lower-palette gate is

\[
 \boxed{
 \text{one spanning alternating factor of }H
 +\text{ one compatible cyclic-window phase at every trace}.} \tag{7.6}
\]

The phase is not an independent decoration after the factor is chosen: it
also fixes the two owner ports and the split residence flags of that dwell.
This is a sufficient restricted face, not the full physical gate.  Two
different physical lower colours may have the same external trace and
different `K` profiles; noncyclic ears can exploit that extra multiplicity.

### Theorem 7.2 (one exact SCD matching)

The graph `H` always has a perfect matching.  More precisely, every
symmetric-chain decomposition of `2^E` supplies one.

#### Proof

Fix a symmetric chain with bottom rank `t` and top rank `m-t`.

If `t<=a-1`, its trace vertices in `mathcal B` have ranks `a,...,b`, while
its label vertices in `mathcal C` have ranks `a-1,...,b-1`.  Match every
trace vertex to its predecessor on the chain.

If `t>=a`, the trace and label portions of the chain are identical: both
have ranks

\[
                         t,t+1,\ldots,m-t.
\]

Match each trace to its diagonal copy.  These two cases exhaust the chain
bottoms.  The matchings on distinct chains are disjoint and cover every
vertex of both bands.  \(\square\)

Fixing this matching `M_0`, the exact unphased two-factor gate becomes the
ordinary residual Hall system

\[
 \boxed{
 H-M_0\text{ has a perfect matching}.}                \tag{7.7}
\]

Any such second matching would give a spanning alternating two-factor.
Making it one cycle, and satisfying the phase cocycle `(7.6)`, would remain
additional requirements.  Thus the restricted external-label-rainbow
problem has one explicit residual bipartite matching test.

In fact that residual matching is impossible in the external-label-rainbow
face.

### Theorem 7.3 (bottom-layer diagonal obstruction)

For `a=d+2=o(m)`, the graph `H` has no spanning two-factor for all
sufficiently large `m`.

#### Proof

Every bottom trace `T in binom(E,a)` is adjacent either to its diagonal
label `T in binom(E,a)` or to one of its `a` facets in
`binom(E,a-1)`.  In one perfect matching, at most

\[
                         \binom m{a-1}
\]

bottom traces can use facet labels.  Hence at least

\[
                         \binom ma-\binom m{a-1}       \tag{7.8}
\]

must use their diagonal edges.

A spanning bipartite two-factor decomposes into two edge-disjoint perfect
matchings.  There are only `binom(m,a)` diagonal edges at rank `a`, so
`(7.8)` would force

\[
 2\left(\binom ma-\binom m{a-1}\right)\le\binom ma,
\]

or equivalently

\[
                         \binom ma\le2\binom m{a-1}.   \tag{7.9}
\]

But

\[
 {\binom ma\over\binom m{a-1}}
 ={m-a+1\over a}>2
\]

for `a=d+2=o(m)` and all sufficiently large `m`, contradicting `(7.9)`.
\(\square\)

Therefore phase propagation and direct one-bit/same-rank seams alone
cannot produce the desired chronology.  Composite ears using distinct
noncyclic `K` profiles are not an optional convenience; they are forced by
an exact capacity inequality.

## 8. Corrected residual theorem

The exact next statement is:

> **Palette-resident square-Gray ear lemma.**  Choose a saturating cycle,
> an assignment and order of the omitted opposite-parity vertices, and one
> opening phase/sign for every dwell so that:
>
> 1. every rank-direction reversal is separated by a same-rank exchange,
>    or by a composite decorated ear;
> 2. every two-add/two-delete adjacency is replaced by an ear with at least
>    two fresh intermediate owners, or by a splice through the unique
>    intermediate dwell, while preserving owner-once;
> 3. every lower and upper seam colour is either fresh or is exactly the
>    missing colour of one opened dwell;
> 4. all `m-3` split run/gap flags at every opening are continued for the
>    required deadline; and
> 5. all choices are globally occurrence-disjoint.

Under this lemma, the central common-core damage bank lies on one resident,
palette-simple component.  The two rank tails contain only `2^{o(m)}`
traces and can then be appended by the rolling-collar halo method.

This is a much smaller and more structured gate than arbitrary
Hamiltonization of the original `2^m` path reservoir, but it is not yet
proved by the owner-level Gray theorem.

## 9. Scope

The audit does not alter the valid owner-level conclusions of the audited
file.  It adds three proof-safe boundaries:

1. the exact one-bit opening-sign law;
2. the one-intermediate Hamming-two no-go;
3. the `m-3`-flag residence ledger at every dwell opening; and
4. the zero-spare alternating-factor/phase-cocycle reduction `(7.6)`.

No claim about the full PBBS upper bank, the terminal common cap, or
`nu(k)<=B(k)+O(1)` follows without the corrected residual lemma.
