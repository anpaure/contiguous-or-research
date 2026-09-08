# Audit: fixed-`z` two-bank collar count, history, load, and scope

**Date:** 2026-08-02  
**Audited file:**
`MATH_THEOREM_A_FIXED_Z_TWO_BANK_DECODABLE_HISTORY_COLLAR_AND_BOUNDED_LOAD_SUBATLAS_20260802.md`  
**Verdict:** the restricted count, statewise ray geometry, both history
polarities, and the central decoder are correct.  Two exact scope repairs
are required: the protected-factor constants need `k=2r-1`, and the
`14+28d` edge count is statewise rather than the full old/new ticket
footprint.  Two further “only remaining gate” formulations must be narrowed.
No finite search is used.

## 1. Restricted atlas count: PASS

The fixed banks remove `2d` values from `X-{a}` and `2d` values from the
external coordinate set.  Therefore the ordered internal pair has

\[
                         (r-1-2d)_2
\]

choices, the ordered external four-tuple has

\[
                         (k-r-2d)_4
\]

choices, and after it is chosen the common retained label has exactly

\[
                         k-r-2d-4
\]

choices.  Thus

\[
 N_d=(r-1-2d)_2(k-r-2d)_4(k-r-2d-4)                  \tag{1.1}
\]

is exact for labelled role assignments.  In a fixed central-density window
and with `d=o(k)`, this is uniformly `Theta(k^7)`.

The identities `D^x union D^y subset C` and endpoint avoidance of both
marker banks are also correct: `b,c` avoid both deletion banks, while all
external roles and `z` avoid both marker banks.

## 2. Ray simplicity and 2-boundedness: statewise PASS

For a central endpoint `E`, the ray owner and facet at position `j` are

\[
 E_j=E-D_{[j]}+M_{[j]},\qquad
 G_j=E-D_{[j]}+M_{[j-1]}.                              \tag{2.1}
\]

For `j>=1`, the marker intersection of `E_j` determines the bank type and
`j`, and then recovers `E`.  For `j>=2`, the same is true of `G_j`.  At
`j=1`, adjoining `d^x_1` or `d^y_1` gives at most two possible endpoints.
In fact the two first-facet types are separated atlas-wide by their deletion
banks: an `x` first facet contains all of `D^y`, while a `y` first facet
omits `d^y_1`; dually for `D^x`.  The proof's `z` distinction is sufficient
inside one packet, but the deletion-bank signature is the safer
cross-packet decoder.

Packet endpoints avoid all markers, so no internal ray owner collides with
a packet owner.  Packet facets contain both deletion banks and no markers;
ray facets either contain a marker or omit a deletion-bank value.  Hence no
ray facet collides with a packet facet.  The two ray types are disjoint by
their marker/deletion signatures.

It follows that for **either one old state or one new state** the displayed
bank has exactly

\[
\begin{array}{c|c}
\text{owners}&14+14d\\
\text{facets}&7+14d\\
\text{incidence edges}&14+28d
\end{array}                                             \tag{2.2}
\]

and is simple and 2-bounded.  Packet owners have degree two, internal ray
owners and every facet have degree two, and far owners have degree one.

### Scope defect 2.1 (the two-state footprint is not (2.2))

The old and new packet states share the seven retained incidences
`y_i-f_i` but use respectively `x_i-f_i` and `x_(i+1)-f_i`.  Their central
union therefore has

\[
                         7+7+7=21                       \tag{2.3}
\]

incidence edges, not `14`, and every packet facet has degree three in that
union.  Thus the statement “each ticket uses exactly `14+28d` protected
incidence edges” is correct only for a chosen terminal state.  The full
old/new occurrence footprint has `21+28d` distinct incidence edges and is
not 2-bounded.  This does not hurt the terminal protected-factor theorem,
which uses one state, but the resource ledger for a switch must include both
old and new rows.

## 3. Positive and negative histories: PASS

Traverse the `y` ray backwards into `y_i`, then the seam, then the `x` ray
forwards out of `x_j`.  Immediately before the seam, newest-first event
banks are

\[
 \text{positive insertions }D^y,qquad
 \text{negative-start deletions }M^y.                  \tag{3.1}
\]

Immediately after the seam, the first event banks are

\[
 \text{positive-ending deletions }D^x,qquad
 \text{negative-ending insertions }M^x.                \tag{3.2}
\]

The seam `y_i -> x_j` deletes `z` and inserts
`alpha=x_j-f_i`.  The required positive inequalities are

\[
 z\notin D^y,qquad \alpha\notin D^x,qquad
                         D^y\cap D^x=\varnothing,       \tag{3.3}
\]

and the negative inequalities are

\[
 \alpha\notin M^y,qquad z\notin M^x,qquad
                         M^y\cap M^x=\varnothing.       \tag{3.4}
\]

All hold from the role restrictions and pairwise-disjoint banks, for both
`j=i` and `j=i+1`.  These stronger full-disjointness rows imply every
triangular depth-`d` cross-collar inequality.

Inside one monotone ray, a deleted `D` label is not reinserted and an
inserted `M` label is not deleted.  Hence no positive or negative run is
both born and killed inside the ray.  Runs reaching the far endpoint are
properly exported rather than certified.  The local two-polarity history
claim is exact.

The scope statement is also correct: nothing here proves that the exterior
accepts the fourteen exported sockets.

There is a terminology qualification.  A length-`d` monotone ray resets the
history seen at its packet end, but its far end is not an unconditional
fixed bi-history state.  The first ray deletion/insertion still tests the
unknown exterior past, and dually the far end of an outgoing ray constrains
the exterior future.  What is exported is an endpoint-labelled partial
relation (equivalently, a fixed ray-side half-socket plus its triangular
entrance/exit domain), not a universally accepted literal socket.  The
file's final exterior caveat preserves the mathematics, but the phrase
“literal bi-history sockets determined by the four ordered banks” should be
read in this relational sense.

## 4. Decoder and load: PASS, with private-anchor qualification

A ray owner determines `(epsilon,j,E)` exactly through its marker prefix.
A ray facet does the same except at `j=1`, where there are at most two
candidate endpoint decoders.  The ray cap at step `j` is

\[
                    E-D_{[j-1]}+M_{[j]},                \tag{4.1}
\]

so its marker prefix recovers `(epsilon,j,E)`.  Physical incidences and
occurrence-labelled history events contain at least the same endpoint/step
information.  Therefore every nonprivate collar resource maps to at most
two nonanchor central endpoint tokens, giving load at most `2K_0k^6`.

Packet resources cannot add a hidden third decoder: packet owners/caps avoid
markers, and packet facets contain both deletion banks, whereas ray
resources have the signatures described in Section 2.

The qualification is essential.  Both `x_0=X` and

\[
                         f_6=X-\{a\}                     \tag{4.2}
\]

are common to the entire rooted atlas.  The whole `x_0` ray and the anchor
facet occurrence must be explicitly private.  With that convention, the
greedy transversal inequality

\[
             N_d>(H-1)S_d(2K_0k^6)                     \tag{4.3}
\]

is valid after private banks of different tasks have been made compatible.

The resource notion must remain occurrence-labelled.  The abstract bank
tuples themselves are common to all alternatives but are not capacity-one
physical resources.

## 5. Provider constants: conditional PASS, missing global hypothesis

For one terminal state the counts

\[
 v_O=14+14d,qquad v_F=7+14d,qquad L=14+28d           \tag{5.1}
\]

are correct.  Substitution into the protected duplicate-provider theorem
gives

\[
 {r+1-(14+14d)-2q\choose2}>7+14d+q                    \tag{5.2}
\]

and

\[
                         14+28d+2q\le r-2.              \tag{5.3}
\]

For `q=O(d)` and `d=o(r)`, both eventually hold.

### Scope defect 5.1 (the protected-factor theorem needs `k=2r-1`)

The file begins with arbitrary `k,r,d`, but the protected extension theorem
used in Section 5 is the theorem for

\[
             ML_r:\quad { [2r-1]\choose r-1}
                         \leftrightarrow {[2r-1]\choose r}.     \tag{5.4}
\]

Thus (5.2)--(5.3) and the spanning-two-factor conclusion require

\[
                         k=2r-1                         \tag{5.5}
\]

unless a separate protected-factor theorem for general `J(k,r)` is cited.
The local count, ray geometry, history, and decoder do not need (5.5), but
the provider/host section does.

The provider conclusion is statewise and static.  It does not expose both
old and new rows relative to one incumbent, make the completion connected,
or accept the exported history sockets.  A full free cyclic development
also exceeds the `r-2` physical protected-edge budget, as the source note
correctly states.

Equations (5.2)--(5.3) are the one-ticket constants.  If `H` tickets are
first selected and all backups are then postselected jointly, the exact
safe substitution is instead

\[
\begin{aligned}
 v_O&\le H(14+14d),\\
 v_F&\le H(7+14d),\\
 L&=H(14+28d),
\end{aligned}                                           \tag{5.6}
\]

with `q` equal to the total backup-request multiplicity.  For fixed `H`
and `d=o(r)` the asymptotic conclusion is unchanged, but the displayed
single-ticket inequalities must not be reused verbatim for a joint bank.

## 6. Topology and voltage: PASS under the stated retained-fragment face

With every `y` ray traversed towards the packet and every `x` ray away from
it, the rays occur identically in old and new states and cancel from the
signed retained-fragment ledger.  The central seam sums are

\[
 \sum_i\delta(y_i,x_i),qquad
 \sum_i\delta(y_i,x_{i+1}),                             \tag{6.1}
\]

which agree by cyclic permutation of the moving endpoints.  Thus the local
collar-completed switch has zero seam displacement.

Voltage preservation still requires:

1. every retained fragment is co-oriented;
2. the new step-two pairing is one quotient cycle; and
3. every additional exterior/source/compiler/opening seam is included in
   the total displacement.

The local collar theorem supplies none of the unprotected continuation in
these three rows.  A child-native unit-voltage seed is also still required
after a Pascal modulus change.

## 7. Wording defects and corrected overall scope

Two summary sentences are too strong.

1. Section 0 says the topology/exterior row is “the only missing part of a
   fully completed fixed-`z` ticket.”  The same file excludes deeper uppers,
   source, compiler, and the Pascal child seed, and Section 6 later lists
   them.  The sentence is correct only after “among the central local
   collar/load rows” is inserted.
2. “Each ticket uses exactly `14+28d` protected incidence edges” must say
   “each old or new terminal state bank.”  The two-state switch footprint is
   (2.3) plus the common rays and is not itself 2-bounded.

After these repairs, the strongest proved conclusion is:

> For each rooted central task there are `Theta(k^7)` labelled fixed-`z`
> central packets admitting explicit statewise-simple, locally bi-history-
> safe `O(d)` collars, with `O(k^6)` load on every nonprivate
> occurrence-labelled local resource.  Under `k=2r-1`, one selected terminal
> bank plus named backups has a static two-factor completion whenever
> (5.2)--(5.3) hold.

Still open are common-incumbent old/new exposure, exterior history
acceptance, one-cycle topology, zero total sidecar displacement, deeper
uppers, source/compiler return, and the child-native voltage seed.

## 8. The claimed one-bank no-go is false without an order qualification

The two disjoint banks are a clean sufficient construction, but they are
not essential to the cross-collar inequality.  Let the recent insertion
positions before the seam be `s=1,...,d` and the future deletion positions
after it be `t=1,...,d`.  Equality of one label is forbidden only when

\[
                              s+t\le d.                 \tag{8.1}
\]

If one underlying deletion bank is reused with the antitone pairing

\[
                         t=d+1-s,                       \tag{8.2}
\]

then every repeated label has `s+t=d+1` and passes the exact triangular
guard.  The same construction applies to the marker/negative bank.

Thus a shared bank in the **same effective order** creates short runs (the
near-seam labels are indeed dangerous), but the file's unqualified claim
that two deletion banks are essential is false.  Whether the antitone
one-bank variant retains all simplicity/decoder properties is a separate
local construction question; it is not needed for the validity of the
proved two-bank theorem.

No marginal palette or provider count was used in this audit.
