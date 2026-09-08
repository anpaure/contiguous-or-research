# Fixed-`z` heptagons with two-bank decodable bi-history collars

**Date:** 2026-08-02  
**Lane:** A, bounded-load completed-ticket supply after voltage localization  
**Status:** unconditional local collar construction, exact atlas count, and
bounded nonprivate-resource load.  The one-cycle retained-fragment exposure
and the exterior accepting completion remain hypotheses.  No universal word,
Pascal child, deeper-upper, source, or compiler theorem is claimed.

## 0. Verdict

The fixed-`z` heptagon admits an explicit `O(d)` protected collar which does
not lose the central one-degree load saving.

Fix one rooted task `(X,a)`.  Choose two disjoint ordered deletion banks in
`X-{a}` and two disjoint ordered marker banks outside `X`.  Restrict the
seven free heptagon roles to avoid these banks.  At every moving endpoint
attach the same monotone deletion/marker rail of the first type; at every
retained endpoint attach the rail of the second type.

The two types are disjoint.  Therefore both the old seams `y_i -> x_i` and
the new seams `y_i -> x_(i+1)` pass every positive and negative depth-`d`
cross-collar test.  Each collar owner, facet, cap, incidence option, and
occurrence-labelled history event recovers its central endpoint and its
collar position.  Hence every nonprivate collar resource inherits the
`O(k^6)` load of a central endpoint.

The restricted atlas has the exact size

\[
 (r-1-2d)_2\,(k-r-2d)_4\,(k-r-2d-4)=\Theta(k^7)       \tag{0.1}
\]

in the central regime with `d=o(k)`.  Each old or new terminal-state bank
uses exactly `14+28d` protected incidence edges before any named backup
providers, hence `O(d)` resources.  The full switch-collision footprint is
larger and is recorded in Section 2.

The ray based at the fixed owner `X`, the fixed facet `X-{a}`, and their
fixed packet incidence are common to the task atlas.  Their complete
occurrence closures must be included in the private task anchor bank;
demanding `O(k^6)` load on private anchors would already contradict the
original rooted theorem because `X` itself occurs in every ticket.  All
load statements below are for nonprivate resources, which are the resources
relevant to cross-task packing.

This closes the local history/collar load row.  It does not choose the
unprotected retained paths so that the seven old cuts occur on one
co-oriented quotient cycle.  Among the local collar/history rows, that is
the remaining exterior gate.  Deeper upper support, source/compiler return,
aperture discharge, total sidecar displacement, and a child-native voltage
seed remain separate global requirements.

## 1. Central packet and private banks

Let `k,r,d` be positive integers with

\[
                 r\ge 2d+3,\qquad k-r\ge2d+5.           \tag{1.1}
\]

Fix a rank-`r` owner `X` and `a in X`.  Choose pairwise-disjoint ordered
tuples

\[
 D^x=(d^x_1,\ldots,d^x_d),\qquad
 D^y=(d^y_1,\ldots,d^y_d)                               \tag{1.2}
\]

in `X-{a}`, and pairwise-disjoint ordered tuples

\[
 M^x=(m^x_1,\ldots,m^x_d),\qquad
 M^y=(m^y_1,\ldots,m^y_d)                               \tag{1.3}
\]

in `[k]-X`.  The four banks are task-private.

Choose the fixed-`z` heptagon roles subject to

\[
\begin{aligned}
 b,c&\in X-\bigl(\{a\}\cup D^x\cup D^y\bigr),\quad b\ne c,\\
 p,q,s,t&\in[k]-\bigl(X\cup M^x\cup M^y\bigr),
                 \quad\hbox{ordered and distinct},\\
 z&\notin X\cup\{p,q,s,t\}\cup M^x\cup M^y.
\end{aligned}                                           \tag{1.4}
\]

Put `C=X-{a,b,c}` and use the seven triples

\[
 abc,\ abp,\ apq,\ pqs,\ cps,\ cpt,\ bct              \tag{1.5}
\]

to define `x_i,f_i,y_i` as in the fixed-`z` heptagon theorem.  Because
`D^x union D^y subset C`, every moving and retained owner contains both
deletion banks.  Because all external roles avoid the marker banks, every
packet endpoint avoids both marker banks.

### Lemma 1.1 (exact restricted count)

The number of labelled central packets satisfying (1.4) is

\[
 N_d=(r-1-2d)_2\,(k-r-2d)_4\,(k-r-2d-4).               \tag{1.6}
\]

In particular, if `r/k` stays in a compact subinterval of `(0,1)` and
`d=o(k)`, then `N_d=Theta(k^7)` with constants uniform on that interval.

#### Proof

After deleting `a` and the two deletion banks, there are `r-1-2d` choices
for the first ordered internal role and one fewer for the second.  There are
`k-r-2d` permitted external coordinates for the ordered four-tuple.  After
those four coordinates are chosen, exactly `k-r-2d-4` permitted choices for
`z` remain.  Multiplication gives (1.6).  The asymptotic statement follows
term by term. \(\square\)

Restricting an atlas cannot increase any central-token load.  Hence the
fixed-`z` theorem still gives an absolute `K_0` such that every nonanchor
central owner, facet, cap, or row option belongs to at most

\[
                             K_0k^6                    \tag{1.7}
\]

restricted packets.

## 2. The two monotone ray banks

For an ordered tuple `A`, write `A_[j]={A_1,...,A_j}`.  For every moving
endpoint `x_i` define

\[
        x_{i,j}=(x_i-D^x_{[j]})\cup M^x_{[j]}
                     \qquad(0\le j\le d),              \tag{2.1}
\]

and for every retained endpoint `y_i` define

\[
        y_{i,j}=(y_i-D^y_{[j]})\cup M^y_{[j]}
                     \qquad(0\le j\le d).              \tag{2.2}
\]

The corresponding rank-`(r-1)` facets are

\[
\begin{aligned}
 g^x_{i,j}&=x_i-D^x_{[j]}+M^x_{[j-1]},\\
 g^y_{i,j}&=y_i-D^y_{[j]}+M^y_{[j-1]}
                  \qquad(1\le j\le d).
\end{aligned}                                           \tag{2.3}
\]

Thus each ray step deletes `d^epsilon_j` and inserts `m^epsilon_j`.

### Theorem 2.1 (simple protected collar bank)

For either the seven old packet rows or the seven new packet rows, the
packet together with all fourteen rays (2.1)--(2.3) is a simple 2-bounded
incidence path bank.  It has

\[
        14+14d\text{ owner vertices},\qquad
        7+14d\text{ facet vertices},\qquad
        14+28d\text{ incidence edges}.                 \tag{2.4}
\]

#### Proof

Every ray step is a Johnson transition by construction.  At `j>=1`, an
`x`-ray owner has marker intersection exactly `M^x_[j]` and no `M^y`
marker; a `y`-ray owner has the dual signature.  Hence its ray type and
position are determined, and deleting the marker prefix and restoring the
deletion prefix recovers its central endpoint.  Distinct central endpoints
therefore give distinct internal ray owners.

For a ray facet with `j>=2`, the same argument uses marker prefix `[j-1]`.
At `j=1`, the endpoint is recovered by adjoining the known bank label
`d^x_1` or `d^y_1`.  An `x` first facet contains no `z`, whereas a `y` first
facet contains `z`, so the two types do not collide.  A packet facet contains
both deletion banks, while a first ray facet omits one of their labels;
hence packet and ray facets do not collide.

Each packet endpoint has one packet incidence and the first incidence of
one ray.  Internal ray vertices have degree two and far endpoints degree
one.  Counts in (2.4) are now immediate. \(\square\)

The counts in (2.4) apply to one old or one new terminal state.  A switch
collision ledger retaining both packet rows has `21+28d` distinct incidence
edges: seven retained packet incidences are common, while the seven old and
seven new moving incidences are distinct.  Its packet facets have degree
three, so that two-state ledger is not itself a 2-bounded protected bank.

## 3. Exact positive and negative seam histories

Orient a retained path so that it enters a retained endpoint `y_i` through
the reverse `y`-ray, crosses a packet seam, and exits a moving endpoint
through the forward `x`-ray.  The `d` most recent insertions and deletions
before the seam are, up to the fixed newest-first order,

\[
                              D^y,\qquad M^y,            \tag{3.1}
\]

and the first `d` deletions and insertions after the seam are

\[
                              D^x,\qquad M^x.            \tag{3.2}
\]

The seam `y_i -> x_j`, with `j=i` in the old state and `j=i+1` in the new
state, deletes `z` and inserts the unique active coordinate in `x_j-f_i`.
Both seam labels avoid all four banks by (1.4).

### Theorem 3.1 (two-state bi-history safety)

Every old seam `y_i -> x_i` and every new seam `y_i -> x_(i+1)` satisfies
all positive and negative depth-`d` cross-collar inequalities.  No ray
contains an internally completed positive or negative run of length at most
`d`.  The fourteen far ray endpoints export endpoint-labelled partial
bi-history relations: the ray-side half of each socket is determined by the
four ordered banks, while its triangular exterior domain remains to be
accepted.

#### Proof

For positive residence, the recent insertion bank `D^y`, the seam labels,
and the future deletion bank `D^x` are pairwise disjoint.  Hence the seam
deletion is absent from the preceding history, its insertion is absent from
the following deletion collar, and no preceding insertion is deleted in the
triangular cross-collar range.  For negative residence the identical
argument uses the pairwise-disjoint banks `M^y,M^x` and the same seam-label
avoidance.

Within one monotone ray every deletion label and insertion label is used
once, and the two banks are disjoint.  Thus no run starts and ends wholly
inside the ray within `d` transitions.  Runs meeting a far endpoint are not
silently certified; their exact entrance/exit histories are the exported
sockets. \(\square\)

The theorem certifies the history local to the packet and its collars.  It
does not assert that an arbitrary exterior continuation accepts the exported
sockets or is internally resident.

## 4. The decisive load count

Call a resource **private** if it belongs to the following literal closure
of the fixed rooted anchor and its four collar banks:

\[
 \mathcal P_{X,a}=\{X,X-\{a\},(X,X-\{a\})\}
 \cup\{\text{every owner, facet, incidence, cap and history occurrence
                  on the full }x_0=X\text{ ray}\}.       \tag{4.0}
\]

The four bank labels are private data as well, although bare labels are not
capacity-one physical resources.  In particular, the fixed facet
`f_6=X-{a}` and its packet incidence are private.  Without this closure that
incidence occurs in all `N_d` tickets and is a literal `Theta(k^7)`-load
counterexample.

All other owner, facet, cap, incidence, and history resources are
occurrence-labelled physical resources.  Bare coordinate names are not
capacity-one resources; their relevant occurrences are the transitions and
collar states above.

### Theorem 4.1 (bounded collar decoder)

Every nonprivate **ray or collar-extension** resource determines one of at
most two nonanchor central endpoint resources.  Every nonprivate central
packet resource already satisfies the direct bound (1.7).  Consequently
every nonprivate local resource has load at most

\[
                             2K_0k^6.                   \tag{4.1}
\]

The same bound holds for every ray upper cap and every occurrence-labelled
positive or negative history event.

#### Proof

Central packet owners, facets, caps, and row options use (1.7) directly; no
endpoint decoder is asserted for them.  For an internal ray owner,
intersection with `M^x union M^y` determines the
ray type and prefix length, after which (2.1) or (2.2) recovers the central
endpoint.  For a facet the same is true except at the first position, where
adjoining `d^x_1` or `d^y_1` gives at most two candidate endpoints.  A ray
upper cap at step `j` is

\[
              E-D^epsilon_{[j-1]}+M^epsilon_{[j]},      \tag{4.2}
\]

so its marker prefix again recovers `epsilon,j,E`.  Incidence options and
history events contain the same occurrence and step data.  Apply the
central endpoint load bound (1.7) and sum over at most two decoders. \(\square\)

### Corollary 4.2 (local bounded-load subatlas)

The restricted atlas consists of `N_d=Theta(k^7)` locally bi-history-safe
fixed-`z` tickets, uses `O(d)` resources per ticket, and has `O(k^6)` load on
every nonprivate central, collar-history, facet, owner, cap, or incidence
resource.

For cross-task packing, first choose the private physical closures pairwise
capacity-compatible (in the capacity-one model, disjoint), and prefilter
every atlas against every foreign private closure.  Write
\(\mathcal P_i=\mathcal P_{X_i,a_i}\) for task `i`; then

\[
 \mathcal A_i'=\{T\in\mathcal A_i:
       T\cap\bigcup_{j\ne i}\mathcal P_j=\varnothing\}. \tag{4.3}
\]

If \(p_d=\max_i|\mathcal P_i|=O(d)\) and `S_d=O(d)` bounds a nonprivate
ticket support, the decoder gives

\[
 |\mathcal A_i'|\ge N_d-2K_0(H-1)p_dk^6.               \tag{4.4}
\]

Ordinary greedy selection on the filtered atlases is valid whenever

\[
       N_d>2K_0(H-1)(p_d+S_d)k^6.                       \tag{4.5}
\]

In particular fixed `H` succeeds for `d=o(k)` after the task-private
closures have been chosen compatibly.  Pairwise disjoint private label
banks alone do not imply (4.3).

This is a local ticket statement.  A full completed-ticket transversal must
also restrict to tickets whose exported sockets occur in the required
one-cycle retained-path host.

## 5. Cap providers and protected-factor budget

Specialize in this section to the Middle-Levels host `k=2r-1`, so the
provider theorem's parameter `m` is `r`.

The pure fixed-`z` heptagon is cap-multiset exact, so its central switch
requires no duplicate backup.  Let a compatible exterior
source/aperture/compiler bank have counts

\[
                  v_O^{ext},\qquad v_F^{ext},\qquad L^{ext},       \tag{5.1}
\]

and let `q` be the number of additional **literal backup requests counted
with multiplicity**.  Every sidecar incidence claimed preserved must be
included in these three exterior counts.  For one ticket, the full protected
bank has

\[
\begin{aligned}
 v_O&=14+14d+v_O^{ext},\\
 v_F&=7+14d+v_F^{ext},\\
 L&=14+28d+L^{ext}.                                      \tag{5.2}
\end{aligned}
\]

The literal provider theorem postselects all `q` backups and extends the
bank to a spanning owner/facet two-factor whenever

\[
                     {r+1-v_O-2q\choose2}>v_F+q          \tag{5.3}
\]

and

\[
                              L+2q\le r-2.               \tag{5.4}
\]

For `v_O^{ext},v_F^{ext},L^{ext},q=O(d)` and `d=o(r)`, (5.3) is
eventually automatic; (5.4) is the load-bearing protected-edge budget.
Provider choices are made after the ticket, so provider socket menus and
provider-versus-collar loads do not enter (4.1).

For an `H`-ticket transversal, apply the theorem only after taking the union
of all selected protected banks.  If its aggregate counts are `V_O,V_F,L`
and its total literal request multiplicity is `q_tot`, the exact common-host
conditions are

\[
 {r+1-V_O-2q_{tot}\choose2}>V_F+q_{tot},\qquad
                         L+2q_{tot}\le r-2.              \tag{5.5}
\]

In the sidecar-free disjoint case one may use

\[
 V_O=H(14+14d),\quad V_F=H(7+14d),\quad
 L=H(14+28d).                                           \tag{5.6}
\]

Separate per-ticket completions do not imply one common factor.

The conclusion is literal and static.  The arbitrary two-factor completion
need not retain the one-cycle topology or accept the far history sockets.
Moreover a full free cyclic development multiplies the protected physical
bank by the orbit length, so (5.4) cannot be applied to a developed quotient
packet without a new equivariant extension theorem.

## 6. Voltage localization and the surviving exterior gate

In the required step-two face, traverse the retained fragment `P_i` from
`x_i` to `y_(i+1)`.  The corresponding old and new fixed-`z` seams are

\[
                   y_i\longrightarrow x_i,qquad
                   y_i\longrightarrow x_{i+1}.          \tag{6.1}
\]

In the phasewise fixed-`z` representatives all these seams have zero
intrinsic shift.  After any consistent endpoint gauge change `g`, their
total directed seam voltages agree by cyclic permutation of the seven moving
endpoints: the two sums are

\[
 \sum_i(g(x_i)-g(y_i)),\qquad
 \sum_i(g(x_{i+1})-g(y_i)).                            \tag{6.2}
\]

The fourteen collar rays are retained with the same
orientation and hence cancel in the old/new fragment ledger.  Therefore the
central packet plus these retained rays has zero displacement.  Any added
history, cap-provider, aperture, source/compiler, or topology-join seams
must also be entered in the complete-ticket ledger; the completed ticket is
neutral only when their aggregate contribution is zero.

The scalar cancellation theorem applies under the proof-safe sufficient
hypotheses that the seven retained fragments are co-oriented and the new
step-two pairing forms one quotient cycle.  Reversing a fragment contributes
minus twice its fragment voltage and may cancel only after an explicit signed
check; splitting the output requires separate per-component voltage ledgers.
A local label `h=0` alone is not enough.

A same-parity Pascal step changes the cyclic modulus.  The child must contain
one child-native unit-voltage seed before zero-displacement repairs can
preserve it.  The construction above neither supplies that seed nor proves
that the far sockets lie on one suitable host cycle.

Hence the exact remaining fixed-`z` theorem is now:

> Choose the unprotected continuation of the fourteen decoded ray sockets
> so that the seven old cuts lie on one co-oriented quotient cycle in
> step-one order, the step-two rethread is one cycle, every exterior history
> relation accepts, and all separately attached source/compiler/upper rows
> return.

No nonprivate moving-geodesic or local collar resource has excessive load
in this remaining problem; the declared private closure is handled by the
cross-private prefilter (4.3).

## 7. Scope audit

1. The private `X` ray has load `N_d`; it is deliberately part of the task
   anchor.  Calling it nonprivate would make an `O(k^6)` theorem impossible.
2. Two disjoint deletion banks (and two marker banks) are a clean sufficient
   design, not a proved necessity.  Reusing one bank in the same effective
   order can violate the triangular guard, whereas antitone reuse pairs
   positions with `s+t=d+1` and passes that guard.  Simplicity and decoding
   for such a one-bank variant are not asserted here.
3. Marker prefixes are load-bearing: without them a fixed resource may be
   decoded only after guessing one of `d` collar offsets, yielding merely
   `O(dk^6)` load.
4. The provider theorem needs both (5.3) and (5.4); the edge budget alone is
   insufficient.
5. The provider theorem proves only a static owner/facet host and named cap
   support.  It does not preserve connected topology or exterior histories.
6. The local atlas is physical.  An orbitwise application needs an existing
   equivariant factor and stabilizer-weighted resource ledger, or a new
   quotient protected-extension theorem.

## 8. Provenance

This theorem uses:

* `MATH_THEOREM_HEPTAGONAL_CAP_CIRCULATION_AND_PROSPECTIVE_ABUNDANCE_20260802.md`;
* `MATH_THEOREM_A_HEPTAGONAL_CAP_BACKUP_AND_BIHISTORY_TICKET_INTERFACE_20260802.md`;
* `MATH_THEOREM_HEPTAGON_PROTECTED_HOST_AND_DUPLICATE_CAP_BACKUPS_20260802.md`;
* `MATH_THEOREM_A_FIXED_Z_COMPLETED_TICKET_COLLAR_KERNEL_AND_POSTSELECTED_BACKUPS_20260802.md`;
* `MATH_AUDIT_A_FIXED_Z_ZERO_DISPLACEMENT_AND_COMPLETED_TICKET_LOAD_GATE_20260802.md`; and
* `MATH_AUDIT_A_ZERO_HOLONOMY_FRAGMENT_ORIENTATION_AND_SPLIT_COUNTEREXAMPLES_20260802.md`.

No finite search, SAT result, or independent-marginal overlap assumption is
used.
