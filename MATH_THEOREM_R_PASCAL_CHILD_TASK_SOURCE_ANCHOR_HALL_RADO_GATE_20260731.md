# Pascal-child tasks versus middle-incidence anchors: exact Hall/Rado cuts and the private-source gate

Date: 2026-07-31  
Lane: R, bounded-load private anchors  
Status: exact statewise task--source min--max, exact suspended-C6
target--anchor factorization, an unconditional raw Hall theorem, and a
conditional bounded-task salvage.  The current buffered-hex and correlated-
C6 hypotheses do not prove the required guarded private-source theorem, and
no unconditional `B(k)+O(1)` conclusion is claimed.

## 0. Verdict

There is no task--source graph determined only by the Pascal parameters.
It is determined by a **literal child state**: its occurrence-labelled
unresolved tasks, its occurrence-labelled middle incidences, the mandatory
owner slots at those incidences, and the complete guarded packet menus.
Once these data are fixed, the bounded-load assignment has an exact answer.

There is one important canonical subgraph.  In the bare four-sector Pascal
attachment, the tasks are the `C` path components with distinct `X`-shore
endpoints `R_i`, and a source indexed by `P` is eligible exactly when
`P subset R_i`.  This graph has an injective task-saturating matching by a
one-line facet-incidence Hall count.  Thus bare component attachment has
congestion one.  The later residence, exposed-witness, topology, and
compiler tasks are not those component tasks; their guarded graph remains
state-dependent.

For source capacities `b(s)`, the minimum number of tasks which must remain
unassigned is

\[
 \delta_b(G)=
 \max_{X\subseteq {\cal T}}
 \left(|X|-\sum_{s\in N_G(X)}b(s)\right)_+.                 \tag{0.1}
\]

When mandatory owner slots are represented by a matroid `M` on the source
occurrences, the exact replacement is the Rado deficiency

\[
 \delta_M(G)=
 \max_{X\subseteq {\cal T}}
       \bigl(|X|-r_M(N_G(X))\bigr)_+.                         \tag{0.2}
\]

Thus an `O(1)` exceptional set is equivalent to an `O(1)` maximum cut
deficiency.  Marginal source degrees are not a substitute for these all-set
cuts.

The native suspended gain-one C6 does have a useful exact positive row.  A
target atom has `2n` canonical middle-incidence anchors, and exactly `n-2`
canonical packets over each anchor.  In a resource-simple target bank
(distinct upper target colours), a fixed anchor belongs to at most `n-1`
target neighbourhoods.  Hence the unguarded target--anchor graph has an
injective assignment, and any guarded graph with `d` surviving anchors per
task has a source assignment of congestion at most

\[
                         \left\lceil{n-1\over d}\right\rceil. \tag{0.3}
\]

This does **not** close the buffered Haxell step.  Pinning one suspended C6
target to one canonical anchor leaves only `n-2` choices, not the required
quadratic list.  Conversely, in the standard buffered incidence C6, one
fixed anchor carries `m^2` choices, but its fixed source tokens occur in all
`m^2` choices.  Therefore strict `O(m)` cross-list token load forces source-
fixed tokens to be private; constant source congestion greater than one is
already too weak.

There is a bounded-task salvage.  If at most `H=O(1)` target tasks are
actually reachable and every task retains more than `3(H-1)` canonical
anchors, a greedy choice makes both endpoints of all chosen middle
incidences distinct.  The native noncore physical/colour loads are then
`O(Hn)=O(n)`.  Complete cap paths, replacement-witness rays, and topology
tickets still need independent locality/Rado theorems.

Finally, no existing regenerative theorem proves that the reachable source
set is absolutely bounded.  The estimate

\[
                         |U|\le4\Phi+b_0                         \tag{0.4}
\]

is an explicit supposition in the buffered-hex reduction.  The regenerative
and bounded-spine notes are conditional on a contracting successor theorem;
their `K17` calibration is not a bounded-defect child.

## 1. The actual occurrence-labelled task--source graph

Let `S` be one fixed literal Pascal-child scaffold.  Its source bank is a
finite set `A(S)` of occurrences

\[
        s=(\iota,C,H,\xi),\qquad
        C\in{\Omega\choose m},\quad
        H\in{\Omega\choose m+1},\quad C\subset H.               \tag{1.1}
\]

Here `\iota` distinguishes repeated occurrences of one geometric incidence,
and `\xi` is the mandatory literal owner/cap slot.  These labels cannot be
discarded: two geometrically equal incidences at different chronology
positions may have different witness, residence, topology, or cap states.

Let `{\cal T}(S)` be the occurrence-labelled unresolved task bank after the
scaffold is fixed.  A task may be a grouped palette obligation, a protected
upper-witness obligation, a residence packet, a topology slot, or a complete
cap-routing obligation.  For every task `tau` and source occurrence `s`, let

\[
                         {\cal P}_{\tau,s}                      \tag{1.2}
\]

be the actual list of whole packets based at `s` which repair `tau` and pass
all guards already imposed at the assignment stage.  Fix a required local
list threshold `L_*` and define

\[
 G_{L_*}(S)=({\cal T}(S),A(S);E),\qquad
 \tau s\in E\iff |{\cal P}_{\tau,s}|\ge L_*.                    \tag{1.3}
\]

One may instead use the nonempty graph `L_*=1`; the thresholded form records
the list size that will remain after a source is chosen.  This is the actual
task--source graph.  Neither
`MATH_THEOREM_BUFFERED_HEXAGON_LLL_REDUCTION_AND_MISSING_LOAD_GATE_20260731.md`
nor
`MATH_THEOREM_H2_CATALAN_CORRELATED_C6_PLANTING_AND_REROUTER_CUT_20260731.md`
specifies (1.2) for every reachable Pascal child.

### Theorem 1.1 (capacitated Hall with exact exceptions)

Give each source occurrence `s` a nonnegative integer capacity `b(s)`.  The
maximum number of distinct tasks which can be assigned to eligible sources,
using `s` at most `b(s)` times, is

\[
 \nu_b(G)=
 \min_{X\subseteq{\cal T}}
 \left(|{\cal T}\setminus X|+
       \sum_{s\in N_G(X)}b(s)\right).                            \tag{1.4}
\]

Consequently all but at most `h` tasks can be assigned if and only if

\[
 |X|\le \sum_{s\in N_G(X)}b(s)+h
                    \qquad(X\subseteq{\cal T}).                  \tag{1.5}
\]

In particular, an injective private-source assignment is equivalent to

\[
                         |N_G(X)|\ge |X|\quad(X\subseteq{\cal T}).\tag{1.6}
\]

#### Proof

Replace `s` by `b(s)` clones and apply the deficient form of Hall's theorem.
Equivalently, use the integral source--task--sink flow network.  The maximum
matching formula is (1.4), and subtracting it from `|{\cal T}|` gives
(0.1) and (1.5).  QED.

The cut `X` attaining (0.1) is a literal proof-producing obstruction.  It
also identifies which tasks may be declared exceptional; merely knowing
that each individual task has many sources does not bound (0.1).

## 2. Mandatory owner slots and the exact Rado cut

Let `w(s)` be the physical owner of the mandatory slot `xi` in (1.1), and
let `kappa(w)` be its residual source capacity.  On the source ground set
define the partition matroid

\[
 r_\kappa(Y)=
 \sum_w\min\{\kappa(w),|Y\cap A_w|\},
 \qquad A_w=\{s:w(s)=w\}.                                      \tag{2.1}
\]

More generally, `M` may be a gammoid of complete source-to-cap-sink tickets
or any explicitly specified matroid on the source occurrences.

### Theorem 2.1 (owner-slot/gammoid Rado deficiency)

The maximum number of tasks having distinct representatives whose source
set is independent in `M` is

\[
 \nu_M(G)=
 \min_{X\subseteq{\cal T}}
       \bigl(|{\cal T}\setminus X|+r_M(N_G(X))\bigr).            \tag{2.2}
\]

Thus all but at most `h` tasks can be served if and only if

\[
                    r_M(N_G(X))\ge |X|-h
                         \qquad(X\subseteq{\cal T}).             \tag{2.3}
\]

For the mandatory-owner partition matroid this is the explicit cut family

\[
 \sum_w\min\{\kappa(w),|N_G(X)\cap A_w|\}
                         \ge |X|-h.                              \tag{2.4}
\]

#### Proof

Rado's independent-transversal theorem gives the full criterion
`r_M(N(X))>=|X|`.  Adjoin freely independent dummy representatives, or use
the standard deficient Rado formula, to obtain (2.2)--(2.3).  Substitution
of (2.1) gives (2.4).  QED.

One owner-slot cut is genuinely exact.  Simultaneously imposing unrelated
lower-colour, owner-slot, cap-path, and topology quotas need not define one
matroid.  In particular, requiring the selected incidences to have distinct
lower **and** upper endpoints is a rainbow matching in a bipartite graph,
not independence in either endpoint partition matroid separately.  Passing
all one-resource Rado cuts is then only a relaxation of the common integer
selection problem.

The smallest owner-slot obstruction at capacity `q` consists of `q+1`
tasks all of whose eligible source occurrences use one owner `w`, with
`kappa(w)=q`.  For the full task set `X`, (2.4) reads

\[
                            q<q+1.                              \tag{2.5}
\]

This local star is present in the Boolean incidence host around the facets
of one middle owner.  The current correlated-C6 hypotheses do not forbid a
guarded task bank from concentrating on such a star.

## 2A. The closed bare four-sector attachment graph

Use the four-sector notation on

\[
                         V_0=[2m-1].                            \tag{2.5a}
\]

The raw Pascal construction supplies `C` vertex-disjoint path components
with pairwise distinct `X`-shore endpoints

\[
                         X_{R_i}=R_i+x,qquad
                         R_i\in{V_0\choose m}.                   \tag{2.6}
\]

There is one attachment task `tau_i` per component.  For
`P in {V_0 choose m-1}`, define the typed source incidence

\[
 s_P^x:\quad P+x\subset A_P=P+x+y.                              \tag{2.7}
\]

It is eligible for `tau_i` exactly when `P subset R_i`.  If `R_i=P+b`,
the two physical incidences contract to the required Johnson attachment

\[
                         A_P\ --\ X_{R_i}.                       \tag{2.8}
\]

### Theorem 2.2 (load-one bare Pascal attachment)

The graph `tau_i -- s_P^x` defined by `P subset R_i` has a matching
saturating all `C` tasks.  The chosen sources have distinct lower colours
`P+x`, distinct owners `A_P`, and distinct source incidences.

#### Proof

For any task set `J`, its distinct endpoint sets `R_i` contribute exactly
`m|J|` facet incidences.  A fixed `(m-1)`-set `P` has exactly `m` rank-`m`
supersets inside the `(2m-1)`-set `V_0`, so it is incident with at most `m`
members of the selected endpoint bank.  Therefore

\[
                         m|J|\le m|N(J)|,
 \qquad                  |N(J)|\ge|J|.                          \tag{2.9}
\]

Hall's theorem gives the matching, and distinct `P` give all three stated
private source resources.  QED.

The analogous `y`-source is eligible from the other component endpoint.
The two sources at one `P` share owner `A_P`; the exact common-owner row is
the partition-matroid Rado cut (2.4).  Restricting to the `x` shore proves
it automatically for bare attachment.  This theorem is the attachment
result of
`MATH_THEOREM_PASCAL_ATTACHMENT_HALL_AND_PRIVATE_ANCHOR_LOAD_OBSTRUCTION_20260731.md`.

It does not define the later guarded repair graph (1.3).  Nor does source
privacy by itself bound auxiliary C6 or cap-ticket codegrees; those are the
separate load rows treated below.

## 3. Exact canonical anchors of one suspended gain-one C6 target

Now use the side parameter of the suspended-C6 theorem.  Let
`|Omega|=2n`, and let

\[
 A=(D,V;(D+p,i),(D+q,j)),\qquad
 |D|=n,\quad V=D+p+q                                    \tag{3.1}
\]

be one formal target atom.  For `b in D` and `a in {p,q}`, let `s` denote
the other member of `{p,q}` and define

\[
 \sigma(A;b,a)=
 \bigl(C_{b,a}\subset H_b\bigr),\qquad
 C_{b,a}=D-b+a,\quad H_b=V-b=C_{b,a}+s.                       \tag{3.2}
\]

Use the literal slot at `H_b` named by `X_{as}` in the suspended-hex
notation.

### Lemma 3.1 (target--anchor factorization)

The canonical `2n(n-2)` suspended packets through `A` factor as

\[
 \boxed{
 \{(b,a,c):b\in D, a\in\{p,q\}, c\in\Omega\setminus V\}
   =\mathop{\dot\bigcup}_{b,a}
      \{\sigma(A;b,a)\}\times(\Omega\setminus V).}             \tag{3.3}
\]

There are exactly `2n` distinct source incidences in (3.2), and exactly
`n-2` canonical packets over each one.  Their lower endpoints are all
distinct.  Their owner endpoints are the `n` sets `H_b`, each occurring for
the two orientations `a=p,q`.

#### Proof

Put `K=D-b`.  In the suspended-hex notation,

\[
 D_a=K+a=D-b+a=C_{b,a},\qquad
 X_{as}=K+a+s=V-b=H_b.                                  \tag{3.4}
\]

The incidence `D_a subset X_as` occurs in both the off atom `e_a` and the
on atom `f_a`, so it is a genuine common source incidence of the packet.
The remaining parameter is exactly `c notin V`, giving `n-2` packets.

The owner `H_b` recovers `b=V\setminus H_b`.  Given the incidence, the
element `s=H_b\setminus C_{b,a}` recovers `a` as the other member of
`V\setminus D`; hence the `2n` incidences are distinct.  Alternatively,
the lower endpoints for equal orientations recover `b`, while endpoints
with opposite orientations cannot coincide because one contains `p` and
the other contains `q`, neither of which lies in `D`.  This also proves
lower-endpoint distinctness.  QED.

The same local identity on the odd four-sector host of order `2m+1` has
`|D|=m`, `|V|=m+2`, and therefore `m-1` exterior choices.  It factors as

\[
                    2m\text{ anchors}\times(m-1)
                    =2m(m-1)\text{ packets}.                    \tag{3.4a}
\]

Only the exterior-coordinate count changes; the anchor formula (3.2) and
the endpoint multiplicities are identical.

This factorization is important for the list scale.  The quadratic count is
the product of a linear anchor bank and a linear free-coordinate bank.  A
map assigning `A` to one source incidence retains only `n-2` canonical
options.  It cannot cite the full `2n(n-2)` count after the assignment.

### Lemma 3.2 (right degree in a resource-simple target bank)

Let `{\cal A}` be a target bank in which the upper resources `V(A)` are
pairwise distinct.  A fixed geometric incidence `C subset H` belongs to the
canonical anchor neighbourhoods of at most `n-1` targets in `{\cal A}`.

#### Proof

Write `H=C+s`.  If (3.2) equals `C subset H`, then

\[
                         V(A)=H+b                             \tag{3.5}
\]

for the uniquely recovered `b notin H`.  There are exactly
`|Omega\setminus H|=n-1` choices of `b`, and the resource-simple hypothesis
allows at most one target for each resulting upper resource.  QED.

### Theorem 3.3 (raw and guarded source congestion)

In the unguarded canonical graph from a resource-simple target bank to its
middle-incidence anchors, there is an injective target--source assignment.

More generally, let guards retain an arbitrary anchor set `N(A)` for every
target, and put

\[
                         d_0=\min_A|N(A)|.                       \tag{3.6}
\]

There is an assignment of every target to a surviving anchor with maximum
incidence congestion at most

\[
                         B=\left\lceil{n-1\over d_0}\right\rceil.\tag{3.7}
\]

If every target retains at least `L` canonical packets, then

\[
 d_0\ge\left\lceil{L\over n-2}\right\rceil,
 \qquad
 B\le
 \left\lceil{(n-1)(n-2)\over L}\right\rceil.                  \tag{3.8}
\]

In particular, retention of a `rho` fraction of the full canonical menu
gives `B<=ceil((n-1)/(2 rho n))=O_rho(1)`.

#### Proof

For any target subset `X`, count its surviving target--anchor incidences.
There are at least `d_0|X|`.  Lemma 3.2 bounds the degree of every anchor by
`n-1`, so

\[
                         |N(X)|\ge {d_0\over n-1}|X|.             \tag{3.9}
\]

Thus `B|N(X)|>=|X|` for every `X`, and Theorem 1.1 assigns all targets with
capacity `B` at every source.  In the full graph `d_0=2n>n-1`, so ordinary
Hall gives an injective assignment.  Finally, one anchor supports at most
`n-2` canonical packets, proving (3.8).  QED.

The conclusion is exact for incidence congestion but is not the strict
private-source conclusion needed for `O(n)` Haxell load.  If two quadratic
lists share one source-fixed token, that token already has quadratic
cross-list load.  Thus (3.7) is useful as a routing theorem, but any value
`B>1` still needs further pruning or packet grouping.

## 4. Bounded-task source-private salvage

For one target `A`, let `L(A)` and `W(A)` be respectively the lower and
owner endpoint projections of its surviving canonical anchors.
Lemma 3.1 implies that the anchor-to-lower map is injective and the
anchor-to-owner map has fibres of order at most two.

### Theorem 4.1 (finite-bank greedy private sources)

Let `{\cal A}` contain at most `H` target tasks.  Suppose every target has
more than `3(H-1)` surviving canonical anchors.  Then one can choose one
anchor per task so that all chosen lower endpoints are distinct and all
chosen owner endpoints are distinct.  In particular the source incidences,
their source-fixed lower colours, and their mandatory owners are private.

#### Proof

Order the tasks arbitrarily.  After `j` choices, at most `j` anchors of the
next task are forbidden by the used lower endpoints, because its lower
projection is injective.  At most `2j` further anchors are forbidden by the
used owners, because its owner fibres have size at most two.  Fewer than
`3H` anchors are therefore forbidden at every step, and the stated strict
inequality leaves a legal choice.  QED.

For the full canonical bank, the hypothesis is `2n>3(H-1)`.  If every task
retains `L` packets, it is enough by (3.8) that

\[
                         L>3(H-1)(n-2).                         \tag{4.1}
\]

Thus any quadratic surviving menu supplies private sources for a genuinely
bounded task bank once `n` is large.  The conclusion chooses one packet
anchor; it does not leave a quadratic packet list at that one anchor.

### Corollary 4.2 (local native-token load for bounded tasks)

Assume the hypotheses of Theorem 4.1 and source-fixed token privacy.  If a
noncore physical or colour token occurs in at most `kappa n` candidates of
any one remaining task list, then its cross-list load is at most

\[
                            (H-1)\kappa n.                       \tag{4.2}
\]

For the native suspended C6 one may take `kappa=2` for the owner roles and
`kappa=1` for the local semantic cap-pair roles.  Hence an `O(d)` native
support has local physical/colour conflict degree `O(Hnd)=O(nd)`.

#### Proof

Source-fixed terms have no cross-list contribution.  There are at most
`H-1` other lists, each contributing at most `kappa n` candidates.  Sum over
the `O(d)` tokens of one packet.  The exact native multiplicities are those
in Lemma 1.2 of
`MATH_THEOREM_R_BUFFERED_C6_WEIGHTED_ANCHOR_AND_TOKEN_LOAD_20260731.md`.
QED.

This corollary does not cover a complete alternating cap path, an
arbitrary-width replacement witness, or a topology ticket.  A token common
to all candidates of even two lists has quadratic load, and a cap cut vertex
can force exactly that behaviour.  Those rows require their own private
ticket or gammoid expansion theorem.

### Proposition 4.3 (exact cap-ticket cut)

Suppose two task sources can reach every permitted cap sink only through one
cap-one vertex `z`.  Then their complete-ticket gammoid has

\[
                         r_{\rm cap}(\{\tau_1,\tau_2\})=1<2.      \tag{4.3}
\]

If every packet option in both quadratic local lists carries such a ticket,
then every option has at least the full size of the other list as external
cap-token load, namely `Omega(n^2)`.

#### Proof

Deleting `z` separates both sources from every allowed sink, so Menger's
theorem gives maximum vertex-disjoint linkage one.  This is the gammoid
rank.  The menu-load statement follows because every ticket contains `z`.
QED.

Thus even a successful native physical/colour assignment does not bound the
cap load.  The all-set Rado cuts certify existence of one linkage; a
separate menu-dispersion theorem is still needed to bound Haxell's conflict
degree over every unselected alternative.

## 5. Why the current theorems do not supply the guarded graph cuts

### 5.1 The correlated planting theorem supplies a different quantifier

The correlated-C6 planting theorem begins with one prepacked bank whose
complete packet supports are pairwise resource-disjoint.  For a selected
target subbank this makes source privacy automatic, but it provides one
preselected packet per target, not a quadratic Haxell list per task.  Its
target Hall cut pairs the lower and upper leave.  Its owner cut

\[
       |X|\le\sum_{w\in N(X)}\kappa_F(w)                         \tag{5.1}
\]

is necessary for selecting one packet per target.  Neither cut defines the
statewise graph (1.3) for all Pascal-child defect tasks, proves (1.5) with a
bounded exception, or bounds the menu load of complete cap and witness
tickets.

The full formal target catalogue has the raw `2n(n-2)` count, but by
Lemma 3.1 this count is spread over `2n` sources.  Positive survival of the
packet count gives the constant-congestion result (3.7); it does not by
itself give injective source privacy or simultaneous endpoint/cap locality.

There is an exact obstruction already on the actual attachment variables.
Write the chosen attachment as

\[
 D_i=P_i+x,qquad V_i=R_i+x+y,qquad P_i\subset R_i.             \tag{5.1a}
\]

For a rank-`m` set `R`, put

\[
 d_{\rm ext}(R)=
 \#\{i:P_i\subset R,\ R_i\ne R\}.                              \tag{5.1b}
\]

The suspended packet from task `i` uses the auxiliary slot `R+x` in
exactly `2m` options whenever `P_i subset R` and `R_i ne R`.  Therefore its
external menu load is at least

\[
                             2m\,d_{\rm ext}(R).                 \tag{5.1c}
\]

Thus `O(m)` load requires `max_R d_ext(R)=O(1)`, a dispersion statement not
contained in Theorem 2.2.  The requirement is sharp against the current
scalar endpoint hypotheses: take all task endpoints `R_i` to be the
`m`-subsets of a set `W` of order `m+s` and choose arbitrary facets
`P_i subset R_i`.  Double counting gives

\[
                         \max_Rd_{\rm ext}(R)\ge s.              \tag{5.1d}
\]

One may take `s=m-O(log m)` while keeping the family below the Catalan task
count, forcing an auxiliary-slot load `Omega(m^2)`.  This is a scoped
counterexample to deriving load from task count and distinct endpoints; it
does not assert that the concentrated endpoint family has already been
realized by a complete old-colour-exact bridge bank.  The full construction
and count are in
`MATH_THEOREM_PASCAL_ATTACHMENT_HALL_AND_PRIVATE_ANCHOR_LOAD_OBSTRUCTION_20260731.md`.

### 5.2 The buffered incidence atlas has the opposite factorization

For a standard middle incidence `C subset C+a` on a `(2m+1)`-set, the
buffered zero-boundary C6 has `m^2` choices `(b,c)` **at that one fixed
source**.  Every one contains the fixed source incidence and its two source
vertices.  Thus two task lists assigned to the same source have quadratic
mutual token load.  More generally the exact weighted load is

\[
                    m^2N_0(r)+mN_1(r)+N_2(r),                    \tag{5.2}
\]

as proved in
`MATH_THEOREM_R_BUFFERED_C6_WEIGHTED_ANCHOR_AND_TOKEN_LOAD_20260731.md`.
Consequently `O(m)` load requires `N_0(r)=0` across other lists, not merely
`N_0(r)=O(1)`.

The two quadratic counts therefore cannot be silently combined:

* suspended gain-one C6: `2n` sources times `n-2` choices per source;
* buffered zero-boundary incidence C6: one source times `m^2` choices.

A theorem transporting a gain-one task to a buffered source while preserving
the complete boundary, witness, topology, and cap state is an additional
construction, not a consequence of either local count.

### 5.3 Bounded reachable tasks are not yet a theorem

Section 5 of the buffered-hex reduction says:

> suppose a lift exposes a source set `U` with `|U|<=4 Phi_k+b_0`.

This is a hypothesis.  The regenerative guarded-switch theorem is explicitly
conditional on a guarded Hall-expansion/contraction theorem.  The
bounded-defect spine theorem is likewise a conditional implication from a
contracting successor or bounded sidecar.  Its authenticated `K17`
calibration records thousands of strict-run and upper defects and explicitly
states that it is not a bounded-defect child.  Therefore Corollary 4.2 cannot
currently be invoked along an all-parameter spine.

If an independent theorem later proves `Phi=O(1)` and (0.4), then
`H=O(1)` and Theorem 4.1 closes the native source assignment for all large
parameters.  One would still need source-fixed cap/witness privacy and the
complete-ticket locality asserted after Corollary 4.2.

## 6. Exact remaining private-anchor theorem

For every reachable Pascal child, after all upper-ray, residence, topology,
and cap guards have been installed, prove one of the following.

1. **Full-bank form.**  The statewise graph (1.3) has injective Hall
   deficiency `O(1)`; the chosen sources have private fixed tokens; their
   weighted one-free/zero-free profiles obey (5.2) with `O(m)` load for every
   physical, colour, witness, topology, and cap token.
2. **Bounded-task form.**  Prove independently that the reachable task bank
   has absolute order `H`, retain more than `3(H-1)` anchors per task, apply
   Theorem 4.1, and prove private complete cap/witness tickets for the chosen
   finite bank.

In either form, a failed Hall row (1.5), owner/gammoid Rado row (2.3), or
weighted token quota is a literal obstruction.  Passing the marginal C6
counts without these common cuts does not imply the `O(m)` global load needed
by the final Haxell selector.
