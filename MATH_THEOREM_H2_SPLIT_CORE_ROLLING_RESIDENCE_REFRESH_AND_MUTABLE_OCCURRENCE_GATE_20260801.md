# Split-core rolling residence refresh and the mutable-occurrence gate

Date: 2026-08-01  
Status: exact packet-local theorem and independently replayed obstruction.
The pivot/geodesic, native lower-`q1`, two-ray socket, and local cap formulas
are taken as frozen inputs.  No global Pascal-sector transport, common-cap
compiler, or `B+O(1)` recurrence is claimed.

## 0. Verdict

Let a pairwise-disjoint split-core packet start at depth `b`, and let
`h=b+t` after `t` deadline jumps.  The canonical inherited `K2` state has a
sharp signed-residence deadline: the pair born at jump `i` is resident iff

\[
                         t\le b+2i-2.                 \tag{0.1}
\]

There are four different refresh statements, and they must not be
conflated.

1. **Fixed named owner/q1 rows: no-go.**  The boundary-clipped occurrence
   of an expiring label is its unique provider throughout one outer owner
   block.  Any replacement fixing those owners must retain the old label
   and may not add a fresh one.  The triangular socket and the local
   four-sector packet contain no complementary occurrence of the displaced
   owner targets.
2. **Residence and local geometry only: positive.**  At the deadline of
   pair `i`, replace its two outer occurrences by one packet-fresh label
   `z_i`.  The old pair becomes permanently resident, and `z_i` is
   permanently resident.  Owner ranks, Johnson adjacency, simplicity,
   both native q1 injections, the central `K2` sites, rays, and static
   socket survive.  But this changes `Theta(h)` named target tickets.
3. **Protected-bank quantifier: positive.**  Release the old sector and
   protect the current refreshed diamond paths instead.  They have distinct
   upper/lower colours, owner degree at most two, and size `O(h)=o(m)` in
   the triangular regime.  Their incidence lift is an exact input to the
   small protected-factor theorem.  This removes individual old-owner and
   old-lower rehosting at the abstract factor level, but not upper-decorated
   topology, literal occurrences, or common cap.
4. **Whole outer-sector recompile: conditional positive.**  Co-ordering the
   two shared outer banks gives an indefinitely resident, constant-schema
   recurrence with no extra source length.  It replaces canonical outer
   owner/q1 identities from the second jump onward.  It is therefore a
   valid local normal form only conditional on a global two-sector target,
   chronology, and common-cap transport theorem.

Thus one rolling residence service every two jumps is locally possible,
but it is not an `O(1)` physical sidecar theorem.  Constantly many edited
source cells do not imply constantly many displaced compiler rows.

## 1. Canonical traces and service calendar

Use the canonical shared-bank state

\[
\begin{aligned}
 \Lambda_t&=(\alpha_t,\ldots,\alpha_1,\bar\Lambda),&
 D_t^+&=(\bar D^+,\alpha_1,\ldots,\alpha_t),\\
 P_t&=(\bar P,\gamma_1,\ldots,\gamma_t),&
 D_t^-&=(\gamma_t,\ldots,\gamma_1,\bar D^-).
\end{aligned}                                             \tag{1.1}
\]

The complete owner traces are

\[
\begin{aligned}
 \operatorname{tr}(\alpha_i)
   &=0^{t-i}1^{h+1}0^{2b+2i-1}1^{t-i+1},\\
 \operatorname{tr}(\gamma_i)
   &=1^{t-i+1}0^{2b+2i-1}1^{h+1}0^{t-i}.
\end{aligned}                                             \tag{1.2}
\]

Hence (0.1) holds.  The first pair expires before jump `b+1`; after that,
one unserviced first-generation pair reaches its deadline every two jumps:

\[
                         t_i=b+2i-1.                  \tag{1.3}
\]

This is only a necessary service calendar.  The next two sections identify
what a literal service costs.

## 2. Exact fixed-owner cap obstruction

For a source word `A`, a source position `p`, and an incident depth-`h`
owner window `I`, write

\[
 O_I=\bigcup_{q\in I}A_q,
 \qquad R_I=\bigcup_{q\in I\setminus\{p\}}A_q.       \tag{2.1}
\]

### Lemma 2.1 (one-position owner cap)

Replacing `A_p` by a set `F` preserves every incident named owner exactly
iff

\[
 \bigcup_{I\ni p}(O_I-R_I)
       \ \subseteq\ F\ \subseteq\
 \bigcap_{I\ni p}O_I.                                \tag{2.2}
\]

#### Proof

For one window, `R_I union F=O_I` iff `O_I-R_I subseteq F subseteq O_I`.
Intersect the upper bounds and unite the lower bounds over all incident
windows.  \(\square\)

Put

\[
 a=t-i+1,\qquad v=b+i-1.                              \tag{2.3}
\]

The outer `gamma_i` occurrence is incident exactly with

\[
                         L_0,\ldots,L_{a-1},          \tag{2.4}
\]

and the outer `alpha_i` occurrence exactly with

\[
                         R_v,\ldots,R_{h-1}.          \tag{2.5}
\]

Both blocks have size `a`.  The central copy is more than `h` source
positions away, so the outer source cell uniquely supplies `gamma_i` or
`alpha_i` to every owner in its block.

### Theorem 2.2 (fixed named rows forbid rolling refresh)

Any replacement of the outer `gamma_i` cell that preserves (2.4) contains
`gamma_i`; any replacement of the outer `alpha_i` cell that preserves
(2.5) contains `alpha_i`.  A packet-fresh coordinate lies outside the
right-hand cap in (2.2).  Therefore neither deletion, relocation, nor a
fresh-coordinate replacement of one boundary copy can both repair the
duplicate trace and preserve all named owner rows.

The same statement already has packet-local singleton Hall witnesses.
After a nontrivial fresh relabelling, old `L_0` and old `R_(h-1)` have no
depth-`h` occurrence in the refreshed packet.  Their `q^-`/`q^+` type
excludes the central row, and their lambda-prefix/rho-suffix signatures
force the same outer index where the refreshed label is wrong.  The
`P/S` socket fan has smaller rank and cannot host either owner.  Thus the
local complementary-owner occurrence graph contains two zero-neighbour
rows.

This is stronger than a marginal Hall deficit: it is the literal common-cap
obstruction at the changed source positions.

## 3. The exact residence-only rolling actuator

At the first illegal jump of pair `i`, (1.3) gives

\[
       h=2b+2i-1,\qquad a=b+i.                        \tag{3.1}
\]

Replace both boundary-clipped singleton cells

\[
                   \{\gamma_i\},\{\alpha_i\}
                   \quad\longmapsto\quad \{z_i\},\{z_i\},  \tag{3.2}
\]

where `z_i` is packet-fresh.

### Theorem 3.1 (permanent local residence repair)

Immediately after (3.2),

\[
                         \operatorname{tr}(z_i)
                           =1^a0^{2h}1^a.             \tag{3.3}
\]

After `u` further inherited jumps,

\[
                         \operatorname{tr}(z_i)
                           =1^{a+u}0^{2h+u}1^{a+u}.   \tag{3.4}
\]

The remaining `alpha_i` and `gamma_i` copies each have one positive run of
length `h+u+1`.  Hence all three labels are permanently signed-resident.
The refreshed owner row remains equicardinal, simple, and Johnson; its
lower and upper q1 rows retain the correct ranks and are injective.  The
central owner row, enriched `K2` cells, task `X`, rays, and socket aperture
are unchanged.

One-sided replacement repairs only one of `alpha_i,gamma_i`, so two source
positions are necessary.  One fresh coordinate is sufficient.

#### Proof

At service, both outer occurrences support boundary-clipped runs of length
`a`.  The owner trace has total length `3h+1`, giving the middle zero-run
`3h+1-2a=2h`.  Every later jump moves each occurrence one owner farther
from its boundary and lengthens the middle gap by one, proving (3.4).
Since `2h+u >= h+u+1`, the gap remains legal.  Removing the outer copy of
each old label leaves its central run only.  Fresh relabelling replaces one
coordinate uniformly on each affected consecutive outer block; the
cutoff-index proof of Johnson adjacency and q1 injectivity is unchanged.
No changed cell meets the central task/ray source intervals.  \(\square\)

### Exact ticket cost

The actuator (3.2) changes exactly

\[
 \boxed{2a\text{ owners},\quad 2a-2\text{ lower-q1 values},
        \quad2a\text{ upper-q1 values}.}              \tag{3.5}
\]

At service `a=b+i`; already the first service changes `2b+2` owner values.
Every displaced old outer target is absent from the refreshed packet by
the signature argument of Theorem 2.2.  Thus a two-source-cell residence
repair exports `6a-2=Theta(h)` named target tickets.  A valid global use
must release and rehost the entire signed-difference sector, pass exterior
typed Hall, and replay one Johnson chronology/common cap.

Replacing the expiring outer label by a suitable existing opposite-sector
label can avoid new coordinate support in small instances, but it does not
change (3.5).  Such a label is an owner-sector actuator, not a local
compiler closure.

The direct rolling implementation also needs the `z_i` to be distinct.
Two consecutive services using the same `z` put equal labels in adjacent
slots of each carried outer bank; a window containing both then loses one
owner coordinate and produces a non-Johnson/stutter edge.  Thus (3.2) uses
one new packet label per service.  Co-ordering in Section 4 avoids this
growing support, but only by accepting its whole-sector recompilation gate.

### Theorem 3.2 (the refreshed sector is a protected diamond bank)

Put `v=h-a`.  After (3.2), write

\[
 \widehat L_u=(L_u-\gamma_i)+z_i\quad(0\le u<a),
 \qquad
 \widehat R_u=(R_u-\alpha_i)+z_i\quad(v\le u<h).      \tag{3.6}
\]

Select the diamonds on the two owner paths

\[
 \widehat L_0-\cdots-\widehat L_{a-1}-L_a,
 \qquad
 R_{v-1}-\widehat R_v-\cdots-\widehat R_{h-1}.       \tag{3.7}
\]

For every edge `T--H`, its diamond resources are

\[
                         (T\cap H,\ T\cup H,\ T,\ H). \tag{3.8}
\]

The bank `P_z` in (3.7) has exactly

\[
 \begin{array}{c|c}
 \text{diamonds / lower colours / upper colours}&2a\\
 \text{physical owners}&2a+2\\
 \text{occupied labelled owner slots}&4a
 \end{array}                                           \tag{3.9}
\]

and consists of two vertex-disjoint paths.  Its four endpoints have owner
degree one and its other `2a-2` owners have degree two.

All upper colours are distinct.  On an internal left edge they are the old
colours under `gamma_i -> z_i`, and on an internal right edge under
`alpha_i -> z_i`; `q^-` and `q^+` separate the shores.  The `2a-2`
internal lower colours are transformed in the same way and contain `z_i`.
The two seam lower colours are unchanged, contain no `z_i`, and are
distinct from every internal colour and from each other.  Thus `P_z`
satisfies exactly the protected-diamond hypotheses:

\[
 \boxed{\text{upper injective, lower injective, owner degree at most two,
               linear forest}.}                      \tag{3.10}
\]

Sharing `z_i` between the two shores causes no resource collision: the
resources are whole owner/colour sets, not coordinate degrees, and no
owner window sees both source occurrences.

At the service deadline, `2a=h+1`.  Hence `|P_z|=h+1=o(m)` whenever
`h=o(m)`, in particular for `h=Theta(sqrt(m))`.  Its owner--lower incidence
lift subdivides every diamond and has `4a=2h+2` edges.  The small
protected-factor theorem therefore puts it in a spanning owner/lower-q1
two-factor whenever

                         4a+c\le m-2,                 \tag{3.11}

where `c` counts any other protected incidence edges.  Protecting the whole
refreshed `3h`-diamond packet path instead costs `6h+c<=m-2`.  Separately,
the protected owner-slot theorem may retain `P_z` in its `o(m)` diamond
bank.  These are compatible input certificates, not a proof that the
two-factor and upper-exact selector can be chosen simultaneously.

More strongly, Theorem 1.1 of
`MATH_THEOREM_ODD_DIAMOND_ONE_TO_TWO_ALTERNATING_FOREST_AND_PROTECTED_CUT_20260801.md`
applies directly in the triangular regime.  Assign the two incidences at
every degree-two owner to its two labelled slots.  Since `P_z` (or the full
refreshed packet path) is an `O(sqrt(m))` owner-slot matching with forest
projection, it is contained unconditionally in a physical linear-forest
matching of order `U-o(W)`.  The missing `o(W)` uppers still require the
theorem's all-cut alternating-forest expansion and contracted graphic test;
neither exact cover-down nor the literal source/common-cap lift follows
from the protected start.

The phase replacement is essential.  An old and new seam diamond have the
same lower colour and different upper colours, so both cannot be retained;
including both also exhausts the unchanged anchor before its continuation.
Release the old sector and protect the current refreshed phase.  Its union
with the unchanged packet complement is exactly the full refreshed path and
passes the cap-two/forest test.

### Corollary 3.3 (rolling debt consolidates rather than sums)

After `t>=b+1` jumps, carry out every due service with pairwise-distinct
fresh labels.  The supports of successive services are nested.  Relative
to the canonical phase, the entire **current** changed-upper bank is exactly

\[
 P_t^-:L_0-\cdots-L_t,
 \qquad
 P_t^+:R_{b-1}-\cdots-R_{h-1}.                       \tag{3.12}
\]

It has `2t` diamonds, `2t` distinct lower colours, `2t` distinct upper
colours, `2t+2` owners, `4t` occupied owner slots, and two components.
Thus it remains `O(h)=o(m)`.  Do not unite the historical per-service
certificates: later services rewrite their owner masks, and their formal
union need not be cap two.  Recompile at each stage and protect only the
current plus state.

The number of service labels at time `t` is

\[
 s(t)=\max\{0,\lfloor(t-b+1)/2\rfloor\}=O(h).         \tag{3.13}
\]

Starting from disjoint banks, the inherited overlap of the `t` alpha/gamma
pairs saves `2t` labels, while the refresh adds `s(t)`.  The exact support
is therefore `m+3h-2t+s(t)`.  A literal packet-fresh supply exists inside
`[2m-1]` under

\[
                         3h-2t+s(t)\le m-1,           \tag{3.14}
\]

which holds eventually in the triangular regime.

Equations (3.10)--(3.14) resolve the local owner/lower/degree/acyclic row.
The small protected-factor completion spans every owner and lower vertex,
so the displaced old owner/lower values need not be individually hosted in
that abstract factor.  Still open are joint adjacent-upper surjectivity,
rooted component control, literal source halos and singleton alias choices,
mutable-bottom occurrences, exterior/deep rows, and one common cap.

## 4. A conditional co-ordered outer-sector normal form

Keep the two central banks as in (1.1), but co-order the outer copies:

\[
\begin{aligned}
 D_t^+&=(\bar D^+,\alpha_t,\ldots,\alpha_1),\\
 D_t^-&=(\gamma_1,\ldots,\gamma_t,\bar D^-).
\end{aligned}                                             \tag{4.1}
\]

Each new outer copy is inserted at the fixed barred/shared seam.

### Theorem 4.1 (indefinite residence under co-ordering)

In (4.1),

\[
\begin{aligned}
 \operatorname{tr}(\alpha_i)
   &=0^{t-i}1^{h+1}0^{h+b}1^i,\\
 \operatorname{tr}(\gamma_i)
   &=1^i0^{h+b}1^{h+1}0^{t-i}.
\end{aligned}                                             \tag{4.2}
\]

Thus every shared label is resident for every `t`.  At each fixed depth,
the owner path remains equicardinal, simple, and Johnson, and both native
q1 palettes remain literal, correctly ranked, and injective.  The central
`M` owners, inherited `K2` positions, task, rays, socket, and qualitative
four-sector itinerary are unchanged.  Starting in this normal form, one
jump uses one fixed-seam insertion on each shore and no extra source cell.

It is not the canonical Pascal transport.  From `t=2` onward, reversing the
shared suffix/prefix changes internal `L/R` owner and q1 identities.  The
displaced canonical masks are absent locally by the same seam-label and
prefix/suffix signature argument as in Theorem 2.2.  Switching a canonical
packet to (4.1) reverses a growing outer subbank; starting co-ordered avoids
that repeated physical reversal but still requires a global theorem that
accepts the two outer sectors as released/recompiled compound tickets.

Therefore (4.1) is an exact constant-schema **conditional** residence
normal form, not an unconditional `O(1)` recurrence.

### Theorem 4.2 (two-block transposition criterion)

Let `tau=(alpha z)` be a coordinate transposition.  Suppose two disjoint
source collars have disjoint owner-support intervals `J,K`, every owner in
`J` contains `alpha` but not `z`, every owner in `K` contains `z` but not
`alpha`, and no owner outside `J union K` changes.  Conjugate both collars
by `tau`.  The owner multiset is preserved exactly when

\[
                   \mathcal O(K)=\tau(\mathcal O(J))  \tag{4.3}
\]

as multisets (with either fixed orientation or a declared reversal).
Under (4.3), every strictly internal lower and upper q1 value is exchanged
with its `tau`-mate automatically.

The four entering/exiting palette edges are not automatic.  Their exact
condition is equality, before and after conjugation, of the multiset of

\[
                    (V\cap W,\ V\cup W)              \tag{4.4}
\]

over the four exterior--collar adjacencies, together with Johnson
adjacency.  A convenient sufficient form pairs the two left seams and the
two right seams under `tau` (or makes a seam endpoint pair invariant as an
unordered pair).  More explicitly, if an old Johnson edge `E--V` keeps
`E` fixed and conjugates a non-`tau`-fixed `V`, then `E--tau(V)` is Johnson
iff `E` is `tau`-fixed.  Conjugating both endpoints preserves the edge
automatically.  The four lower-colour and four upper-colour multisets must
separately be `tau`-invariant; every nonfixed boundary colour needs its
mate.  At source level, every depth-`h` prefix/suffix halo crossing a cut
must likewise be `tau`-fixed or conjugately paired.  Source overlap,
residence, and common-cap rows remain additional literal conditions.  Thus
(4.3)--(4.4) are the exact owner/palette part of the proposed two-block
conjugation.

### Theorem 4.3 (no packet-local conjugate at first expiry)

At first expiry `t=b+1,h=2b+1`, the clipped support blocks are

\[
 J_\gamma=(L_0,\ldots,L_b),\qquad
 J_\alpha=(R_b,\ldots,R_{2b}).                       \tag{4.5}
\]

A source occurrence with the same clipped support size `b+1` must occupy
one of the two positions at distance `b` from a word boundary.  These are
exactly the displayed outer `gamma_1` and `alpha_1` cells.  Hence the only
packet-local candidate partner for one is the other.

That candidate fails before (4.4).  The seam owners `L_b` and `R_b`
already contain both `alpha_1` and `gamma_1`, because the central support
starts or ends exactly at the clipped-block boundary.  Swapping only the
two outer singleton cells therefore makes each seam owner lose one
coordinate without gaining one.  Both drop rank, four adjacent owner edges
cease to be Johnson, and lower-q1 injection fails.  Moreover
`(alpha_1 gamma_1)` fixes `q^-` and `q^+`, so it cannot send the left block
to the right block.

Equivalently, for every packet coordinate `z` absent from `J_alpha`, the
sequence `tau(J_alpha)` is absent as a forward or reversed contiguous owner
block; the symmetric statement holds for `J_gamma`.  The triangular socket
has strict-lower rank, and the four-sector bank supplies only the failed
opposite clipped block.  Thus no local two-block conjugation repairs first
expiry while preserving the owner/palette multisets.

An exterior conjugate collar remains a genuine conditional escape.  It
must satisfy (4.3), all four equations (4.4), the exact occurrence-support
condition, and the common-cap/source replay.  This is a global owner-block
exchange hypothesis, not a packet-local sidecar.

There is a useful abstract reversed-orientation control.  If
`A=(A_0,A_1,A_2)` is a simple Johnson path, all six owners below are
distinct, and `A_2` is not `tau`-fixed, then

\[
 W=(A_0,A_1,A_2,\tau A_2,\tau A_1,\tau A_0),
 qquad \tau W=\operatorname{rev}(W).                \tag{4.6}
\]

The middle edge is Johnson and all internal palette values occur in
`tau`-pairs.  This is the smallest conjugate-palindrome for the three-owner
first-expiry block.  It is not present in the canonical packet, and its two
exterior seams still require fixed/paired sockets.  Using the same outside
anchor twice would violate simple linear chronology; a literal realization
therefore remains an exterior paired-sector rethread with full source
halos.

## 5. Packet-local mutable-bottom occurrence graph

Let

\[
 S_1=B\cup\{\rho_1\},\qquad
 G=(C\cup X_R)\cup\{\rho_1\}.                         \tag{5.1}
\]

The task cell `[X]` is immediately followed by `[G]`, and their union is
`S_1`.  Every other packet source letter contains a tag outside `S_1`.

### Theorem 5.1 (exact aperture occurrence graph)

Among all nonempty packet intervals whose OR is strictly below `S_1`, the
only two are

\[
                         [X]\mapsto X,qquad [G]\mapsto G.  \tag{5.2}
\]

Consequently the untyped incidence graph between strict aperture targets
and packet intervals consists of two isolated edges and

\[
                         2^{|S_1|}-4                 \tag{5.3}
\]

isolated target vertices.  Any cap-, deadline-, or address-typed graph is a
subgraph.  Restricted to the private fan, only `X` occurs strictly below
`S_1`: every `S_i` is at least `S_1`, and every `P_i` contains a lambda tag.

A jump preserves the two values in (5.2) and shifts both source addresses
by `+2`.  A plateau preserves `X` but replaces `G` by `G+beta`.  Thus only
`X` is indefinitely packet-local.  A generic mutable socket bottom cannot
be physicalized without exterior occurrences.

#### Proof

An interval using any source position other than `[X]` or `[G]` contains a
coordinate outside `S_1`.  Inside the two-position block, the two singleton
intervals have values `X,G`, while their union is exactly `S_1` and hence
is not strict.  This proves (5.2)--(5.3).  The transition statements are
the literal inherited block identities.  \(\square\)

### Corollary 5.2 (exact conditional two-ticket release)

For one abstract rotation

\[
                         a\leftarrow x\ b\leftarrow y\ c,  \tag{5.4}
\]

release the selected physical occurrences of `x` and `y` from the current
matching.  Let `N_x` be the remaining compatible occurrences of target
`x` at address `a`, and `N_y` those of target `y` at address `b`.  In the
ordinary distinct-mask model, `x!=y` makes these two occurrence fibres
disjoint.  A replacement matching exists iff

\[
                         N_x\ne\varnothing,qquad N_y\ne\varnothing.  \tag{5.5}
\]

This gives a constant **schema** of two occurrence pointers.  It is
conditional on exterior hosts, residence, and the simultaneous common-cap
replay; Theorem 5.1 shows that those hosts cannot be inferred from the
packet.

## 6. Exact surviving gate

The local actuator and co-ordered normal form prove that the long internal
zero-gap is not an immutable geometric obstruction.  The protected-bank
recast also removes the `Theta(h)` **owner/lower-factor** ticket objection:
the current refreshed phase is legal input rather than an error to be
undone.  The remaining theorem is nevertheless global:

> Extend the current protected bank to one upper-decorated rooted physical
> chronology, and simultaneously construct a typed exterior occurrence
> matching and common maximal word retaining the socket's two mutable-bottom
> tickets and the inherited upper/deep rows.

The abstract spanning two-factor automatically recovers every displaced
owner and lower colour elsewhere.  It does not recover the literal old
source intervals, force the remaining upper colours, control components,
or certify one common cap.  Co-ordering has the same physical whole-sector
gate.  The known three-primary quotient warning is consistent with this
scope: no claim is made that a global symmetry repair is confined to
`O(1)` exceptional orbits.

## 7. Independent replay

The dependency-free audit

```text
scratch/audit_h2_split_core_rolling_refresh_and_occurrence_20260801.py
```

reconstructs the literal enriched packet, carries repeated jumps, checks
(1.2), the owner-cap obstruction, every count in (3.5), sequential fresh
rolling services, the single-service and consolidated protected-bank
resource ledgers, the co-ordered traces and palette geometry, the two-block
conjugation obstruction, and the exact aperture graph.  Its fail-closed
JSON is

```text
scratch/h2_split_core_rolling_refresh_and_occurrence_20260801.audit.json
```
