# Buffered hexagons: exact transversal reductions and the missing global-load gate

Date: 2026-07-31  
Status: **conditional sufficient reduction** for
`nu(k) <= B(k)+O(1)`, together with the exact extra hypotheses needed to
make the proposed packet count valid.  The hypotheses are not presently
proved for the Catalan host.  No buffered-packet abundance theorem is
claimed here.

## 0. Outcome

The proposed list-versus-conflict calculation is correct after three scope
repairs.

1. The primary selector is Haxell's independent-transversal theorem, which
   accepts the original unequal lists and the exact equality threshold
   `min |P_tau| >= 2 Delta`.  Truncation is needed only for the weaker LLL
   comparison; padding is never valid.
2. Pairwise nonconflict must imply global composability.  This is not
   automatic for upper witnesses, common-cap Hall rows, or topology.
3. The bounded exceptional set must have a bounded terminal completion
   cost.  An arbitrary cap or topology task cannot simply be appended as a
   singleton mask.

With those repairs, lists of order `m^2` and total cross-list conflict degree
`O(m d(k))` imply a constant additive upper bound.  Haxell's theorem is the
primary selector; the direct LLL is retained only as a weaker comparison.
The central unproved estimate is global: it must count conflicts over packets
in **all other task lists**, not merely over the `m^2` choices inside one
source incidence.

## 1. A proof-safe packet transversal theorem

Fix a defective child scaffold `S_k` of physical length at most

\[
                         B(k)+c_0.                         \tag{1.1}
\]

Let `T` be its finite task set and `E subset T` a set of exceptional tasks.
For each `tau in T-E`, let `P_tau` be a list of whole repair packets.  Put a
symmetric incompatibility relation `~` on packets belonging to different
tasks.

Assume, for some integer `L>=1`:

* **list supply:** `|P_tau| >= L` for every `tau in T-E`;
* **global packet load:** every packet is incompatible with at most `Delta`
  packets in the union of all other lists;
* **composition closure:** every transversal choosing one packet from every
  `P_tau` and containing no incompatible pair can be applied simultaneously
  to `S_k`, without increasing its length, and leaves only the tasks in `E`;
* **terminal repair:** every resulting exceptional state has a universal
  completion using at most `c_1 |E|+c_2` appended letters.

### Theorem 1.1 (Haxell packet selector; primary form)

Make the packet-conflict graph `G`: its vertices are all candidate packets,
its vertex partition consists of the task lists, and two vertices in
different parts are adjacent exactly when the packets are incompatible.
Delete any within-part edges, which are irrelevant because a transversal
uses one vertex from each part.  If

\[
                 \min_{\tau\in T-E}|P_\tau|\ge2\Delta,     \tag{1.2}
\]

then

\[
                \nu(k)\le B(k)+c_0+c_1|E|+c_2.           \tag{1.3}
\]

### Proof

Haxell's independent-transversal theorem says that a graph of maximum degree
`Delta` whose vertex partition is `2 Delta`-thick has an independent
transversal; equality is allowed.  Apply it directly to the original task
blocks.  No truncation, padding, or equal-size assumption is used.  The
resulting transversal has no incompatible pair, so composition closure and
terminal repair give (1.3).  \(\square\)

The cited result is P. E. Haxell, *A condition for matchability in
hypergraphs*, Graphs and Combinatorics **11** (1995), 245--248, together
with its graph/list-colouring formulation in P. E. Haxell, *A note on
vertex list colouring*, Combinatorics, Probability and Computing **10**
(2001), 345--347.

### Theorem 1.2 (per-list average-degree pruning)

For a packet `p in P_tau`, let `deg_ext(p)` count its incompatible packets
in all other task lists.  Suppose

\[
 {1\over|P_\tau|}\sum_{p\in P_\tau}\deg_{\rm ext}(p)
       \le\overline\Delta\quad(\tau\in T-E),
 \qquad
 L_0:=\min_\tau|P_\tau|\ge8\overline\Delta.          \tag{1.4}
\]

Then the conclusion (1.3) holds.

#### Proof

When `barDelta=0`, every external degree is zero and any transversal works.
Otherwise delete from each list every packet of external degree greater than
`2 barDelta`.  Markov's inequality retains at least half of every list, so
each retained block has size at least `L_0/2>=4 barDelta`.  Deleting vertices
cannot increase degree, and the induced conflict graph has maximum degree at
most `2 barDelta`.  Its blocks are therefore `2 Delta_ind`-thick, including
the equality case.  Theorem 1.1 applies.  \(\square\)

This is an average over the candidates of **each list separately**.  A
global average can hide one completely blocked task and is insufficient.

### Corollary 1.3

Suppose `|E| <= h_0`,

\[
       \min_\tau|P_\tau|\ge \alpha m^2,\qquad
                  \Delta\le\beta m d(k),                 \tag{1.5}
\]

for absolute positive constants, and `d(k)=Theta(sqrt(m))`.  Then (1.2)
holds for all sufficiently large `m`, because

\[
             {\min_\tau|P_\tau|\over\Delta}=Omega(sqrt m).
\]

The finitely many smaller dimensions can be absorbed into one additive
constant, so `nu(k)=B(k)+O(1)`.

### Theorem 1.4 (weaker LLL comparison)

Let `L=min_tau |P_tau|` and truncate every task list arbitrarily to exactly
`L` candidates.  If

\[
                  e\,{2L\Delta+1\over L^2}\le1,             \tag{1.6}
\]

then the conclusion (1.3) also holds.

Indeed, choose one packet uniformly and independently from every truncated
list.  A bad event selects one incompatible pair and has probability
`L^{-2}`.  The number of conflict edges mentioning one task is at most
`L Delta`, so a bad event has dependency degree at most `2L Delta`.
The symmetric Lovasz local lemma and (1.6) give a conflict-free
transversal.  This argument is strictly weaker in its constant and discards
options from larger lists; it is not the primary selector.

## 2. A checkable resource form of composition closure

The composition hypothesis in Theorem 1.1 is load-bearing.  Pairwise legal
packets can otherwise fail collectively.  For example, three packets may
destroy three different witnesses of one upper target even though every
pair leaves a witness; three locally acyclic splices may form a global
cycle; and individually feasible cap augmentations need not have disjoint
paths.

A sufficient resource-token implementation is the following.  It is useful
to distinguish ordinary capacity tokens from the directed witness relation:
write `R_0(p)` for the ordinary support, `A(p)` for the witness anchors
exported by `p`, and `D(p)` for the witness anchors which `p` can destroy.

1. Every packet has finite sets `R_0(p),A(p),D(p)`.
2. Packets are declared incompatible whenever their ordinary supports
   intersect, or an anchor exported by either packet is damaged by the
   other:
   \[
    R_0(p)\cap R_0(q)\ne\varnothing,\quad
    A(p)\cap D(q)\ne\varnothing,\quad\hbox{or}\quad
    D(p)\cap A(q)\ne\varnothing.
   \]
3. Every packet replacement has exactly the same typed boundary state as the
   piece it replaces.  In particular it preserves component connectivity and
   endpoint type at its boundary.
4. Before the random choice is made, every upper target either has one fixed
   protected witness disjoint from **every candidate support**, or is
   assigned to one mandatory task `tau(T)` such that **every** packet in
   `P_tau(T)` carries a replacement witness for `T` and records its anchor in
   `A(p)`.  Every packet which can destroy that witness records the same
   anchor in `D(p)`, so the two packets conflict.
5. Every common-cap source carries a complete alternating-path ticket to a
   sink, and all vertices and sink capacities on that path are tokens.
6. Residence and owner/palette currents are literal packet invariants, not
   debts deferred to a later global repair.

Under these conditions, disjoint ordinary packet supports commute, the fixed upper
witness bank survives, the packet selected from `P_tau(T)` supplies the
replacement witness assigned to `T`, the alternating paths are
vertex-disjoint, and every local replacement has the same boundary
connectivity.  Therefore a conflict-free transversal is globally
composable.

The upper-witness clause cannot be replaced by the assertion that each
packet is harmless in isolation.  It needs a common protected bank or an
equivalent union-closed acceptance invariant.

## 3. The exact global congestion lemma that yields `O(md)`

For an ordinary token `r`, put

\[
 \lambda_0(r)=\sum_{\tau\in T}|\{p\in P_\tau:r\in R_0(p)\}|,
 \qquad
 \lambda_\times=
 \max_{\tau,\ p\in P_\tau,\ r\in R_0(p)}
 \sum_{\sigma\ne\tau}|\{q\in P_\sigma:r\in R_0(q)\}|.   \tag{3.1}
\]

Thus `lambda_times` is a genuinely cross-list load; alternatives in the same
list are not charged because only one of them is selected.  All loads in
this section are measured on the actual lists used by Haxell; for the LLL
comparison only, they are recomputed after the truncation in Theorem 1.4.
If each packet uses at most `s` ordinary tokens, then

\[
 \#\{q\text{ conflicting with }p\text{ through }R_0\}
                         \le |R_0(p)|\lambda_\times
                                      \le s\lambda_\times.  \tag{3.2}
\]

Thus

\[
              s=O(d),\qquad \lambda_\times=O(m)             \tag{3.3}
\]

implies the desired global conflict degree `Delta=O(md)`.

More concretely, if every token occurs in lists belonging to at most `a`
tasks and occurs in at most `h` options of any one incident list, then

\[
                    \lambda_\times\le(a-1)h.                 \tag{3.4}
\]

The factor `a-1` cannot be omitted.  A bound of `O(m)` options **per one
other task** is not a global `O(m)` load when a token occurs in many task
lists.

Replacement-witness anchors need an analogous two-sided load row.  Define

\[
 \kappa_D=\max_{\tau,r}\sum_{\sigma\ne\tau}
       |\{q\in P_\sigma:r\in D(q)\}|,\qquad
 \kappa_A=\max_{\tau,r}\sum_{\sigma\ne\tau}
       |\{q\in P_\sigma:r\in A(q)\}|.                \tag{3.5a}
\]

Suppose one packet exports at most `a_A` anchors and can destroy at most
`a_D` anchors.  If every incompatibility is one of the three tokenized
types in Section 2, then

\[
 \Delta\le s\lambda_\times+a_A\kappa_D+a_D\kappa_A.         \tag{3.5}
\]

Indeed, fix `p in P_tau`.  Every conflicting packet in another list is
witnessed by an ordinary token in `R_0(p)`, an anchor in `A(p)` which that
packet damages, or an anchor in `D(p)` which that packet exports.  Taking
the union bound over these three witness sets gives (3.5).  This is why all
four loads are cross-list loads relative to the list of `p`; a total load
with an unremoved same-list contribution is not the selector degree.

The primary Haxell row supplied by these load bounds is

\[
 \min_\tau|P_\tau|
   \ge2(s\lambda_\times+a_A\kappa_D+a_D\kappa_A).          \tag{3.6}
\]

After truncating every list to size `L`, the weaker sufficient LLL row is
therefore

\[
 e\{2L(s\lambda_\times+a_A\kappa_D+a_D\kappa_A)+1\}
       \le L^2.                                      \tag{3.6-LLL}
\]

This identifies a preliminary theorem absent from a purely local hexagon
count: tasks must first be assigned to source incidences with bounded load.
A convenient sufficient form is a **private-anchor map** assigning every
nonexceptional task to a source incidence such that

* each task is assigned one anchor;
* each cap-one source incidence carries at most one task (constant load
  greater than one is allowed only after supplying physically distinct
  clones or contracting the common source token); and
* after the assignment, every physical/colour/cap/topology token belongs to
  packet choices from only `O(1)` nearby anchors.

For one fixed anchor a token may then leave one free hexagon coordinate,
giving `O(m)` candidate packets containing it.  Without bounded anchor load,
the same token can occur in packets from exponentially many task lists, and
the raw `m^2` supply says nothing about (3.3).

### Proposition 3.1 (raw full-atlas load is cubic, not linear)

Take all oriented middle-level incidences `C subset C+a` as tasks and all
`m^2` parameter pairs `(b,c)` in (4.1) as labelled candidates.  Put

\[
                  I=\binom{2m+1}{m}(m+1),\qquad L=m^2.       \tag{3.7}
\]

There are `I` tasks and `IL` labelled candidates.  Every geometric C6 is
labelled once from each of its six incidences.  Consequently the exact
global labelled-candidate loads are

\[
 \lambda_{\rm incidence}=6m^2,\qquad
 \lambda_{m}=\lambda_{m+1}=3(m+1)m^2.                       \tag{3.8}
\]

Here the latter two rows refer to one fixed rank-`m` or rank-`m+1` vertex
of the circuit.  In particular every candidate for a task
`C subset C+a` contains both target vertices `C,C+a`, and all `L` candidates
from its own list contain them.  Thus its cross-list conflict degree in the
literal cap-one vertex-token graph is at least

\[
             3(m+1)m^2-m^2=(3m+2)L.                         \tag{3.9}
\]

Even if only the six incidence tokens are charged, the anchor incidence
alone gives `6m^2-m^2=5L` cross-list candidates.  Therefore neither
Haxell's row (1.2) nor the LLL row (1.6) follows from the unpruned full
atlas.  A bounded-load task subset or a load-balanced pruning is a genuinely
new hypothesis.

This obstruction is specific to the full atlas containing all `I` incidence
tasks.  It does not rule out a sparse, state-dependent regenerative source
set.  Such a route remains conditionally possible, but it must separately
prove both its source-exposure bound and the cross-list loads on the actual
reachable lists.

#### Proof

For a fixed oriented incidence, the neighbours of the anchor in the C6
recover `b` and `c`, so its `m^2` parameter pairs give distinct labelled
circuits.  Counting circuit--incidence pairs says that every geometric C6
has six task labels, which proves the first load in (3.8).  Every candidate
contains three vertices on each shore.  Coordinate transitivity and
double-counting give

\[
 {3IL\over\binom{2m+1}{m}}=3(m+1)m^2
\]

on either shore.  Subtract the `L` candidates in the anchor's own task list
to obtain (3.9).  \(\square\)

### Proposition 3.2 (private appended anchors do not replace global Hall)

For every `m>=2`, let there be `m+1` tasks.  Task `t` has the `m^2`
distinct packets

\[
              p_{t,a,b}\quad(a,b\in[m]).                    \tag{3.10}
\]

Packet `p_{t,a,b}` uses one shared cap-one resource `r_a`, one task-private
anchor `h_t`, and one candidate-private token `z_{t,a,b}`.  The anchors and
private tokens cause no cross-task conflict.  Nevertheless no independent
transversal exists: `m+1` selected packets would require `m+1` distinct
members of the `m`-element bank `{r_1,...,r_m}`.

Each list has exactly `m^2` choices and a fixed `r_a` occurs in only `m`
choices of any one task.  Globally it occurs in `(m+1)m` choices, and a
candidate has exactly `m^2` cross-list neighbours through `r_a`.  Thus
`Delta=L=m^2` (the `Theta(md)` scale when `d=m`), Hall fails, and both
`L>=2Delta` and the LLL constant fail.  The smallest nontrivial instance is
`m=2`: three four-packet lists compete for two shared resources.

## 4. What the incidence-hexagon count proves

For odd ground-set size `2m+1`, fix an incidence

\[
                         C\subset C+a,qquad |C|=m.
\]

For each `b in C` and `c notin C+a`, the standard six-incidence circuit is

\[
 C,\ C+a,\ C-b+a,\ C-b+a+c,\ C-b+c,\ C+c.            \tag{4.1}
\]

There are exactly `m^2` choices `(b,c)`, and alternating the circuit has zero
owner and immediate-palette boundary.

To convert this parameter count into `Omega(m^2)` distinct whole packets one
still needs:

* bounded multiplicity of the map `(b,c) -> packet`;
* a guard theorem saying all rejected pairs lie in a set of size `O(md)`;
  and
* the global token-load estimate of Section 3.

### Proposition 4.1 (exact bad-pair star-cover row)

For one task, form the bipartite bad-pair graph

\[
       B_\tau\subseteq C\times(\Omega\setminus(C+a)),       \tag{4.2}
\]

putting an edge `bc` exactly when the corresponding buffered hex is rejected
by at least one declared guard.  If `B_tau` has a vertex cover
`F_b union F_c` of order at most `g d`, then

\[
 |E(B_\tau)|
   \le m(|F_b|+|F_c|)\le gm d,\qquad
 |P_\tau|\ge m^2-gmd.                                    \tag{4.3}
\]

Equivalently, by Konig's theorem it is enough to prove that the maximum
matching rank of `B_tau` is at most `g d`.  A protected-ray or ray-order
proof is precisely such a star cover: each exceptional `b`-ray or `c`-ray
contributes one star of at most `m` edges.

#### Proof

Every bad edge is incident with `F_b union F_c`.  Charge it to one incident
cover vertex; each cover vertex has degree at most `m`.  This proves (4.3).
Konig's theorem gives the equivalent matching formulation.  \(\square\)

The converse counting implication is false: `|E(B_tau)|=O(md)` alone does
not force an `O(d)` vertex cover.  For example, when `m=d^2`, a perfect
matching in the `m` by `m` pair graph has only `m=O(md)` bad pairs but has
minimum vertex cover `m`, not `O(d)`.  Thus the star-cover/matching-rank row
is a sufficient structural way to prove the rejection count, not a
consequence of that count.  If only list supply is at issue, a directly
proved `O(md)` edge bound is enough.

The elementary forbidden-coordinate calculation is the special case in
which `b` or `c` belongs to a declared label set `F` of order `O(d)`.
Constant packet support alone does **not** imply (4.3): a guard can reject
all pairs in `B_0 times C_0` with `|B_0|,|C_0|=Theta(m)`.  That bad-pair
graph has `Theta(m^2)` edges and minimum star cover `Theta(m)`, even though
each individual C6 still has constant support.  Arbitrary-width witness and
common-cap conditions are not automatically star-covered; the protected-ray
and alternating-linkage theorems must prove this exact row rather than
assuming cylinder loss.

## 5. A rigorous weaker contraction route

Let `Phi_k` be a literal-weighted regenerative defect, and suppose a lift
exposes a source set `U` with

\[
                         |U|\le4\Phi_k+b_0.             \tag{5.1}
\]

Equation (5.1), with `b_0` absolute, is an assumption of this route, not a
previously proved Catalan exposure bound.  The existing regenerative
contraction theorem likewise assumes that its additive seam/collar term is
absolute.  The exact AD--RSB collar theorem bounds losses in terms of the
actual changed physical-seam count `s` and explicitly does not bound `s`;
therefore it does not supply an absolute `b_0`.  A sparse-route proof needs
a separate exposure/physical-lift theorem establishing (5.1).  Proposition
3.1 neither proves nor refutes such a theorem, because it concerns the full
task atlas rather than the reachable set `U`.

For each source `u`, let `P_u` be its ticket options in one explicitly
specified matroid `M` (in particular a gammoid), and put
`P_X=union_(u in X)P_u`.  Write `r_M` for the matroid rank.  Equivalently,
one may use a literal bipartite source-to-sink graph, in which case
`r_M(P_X)` is the transversal-matroid rank computed by maximum matching.
Assume the all-cut bound

\[
 r_M(P_X)\ge\left(1-A{d(k)\over k}\right)|X|-\gamma
 \qquad(X\subseteq U).                                  \tag{5.2}
\]

If `q` is the maximum size of a partial transversal whose representatives
are independent in `M`, Rado's deficiency formula gives

\[
 |U|-q=\max_{X\subseteq U}\bigl(|X|-r_M(P_X)\bigr)
 \le A{d(k)\over k}|U|+\gamma.                          \tag{5.3}
\]

If each unmatched source contributes at most `w_0` units of literal defect
and every other row is regenerated without extra loss, then

\[
 \Phi_{k+2}\le4w_0A{d(k)\over k}\Phi_k+O(1).           \tag{5.4}
\]

Since `d(k)/k=Theta(k^{-1/2})`, each parity subsequence eventually satisfies
`Phi_{k+2} <= Phi_k/2+C`; hence `Phi_k=O(1)`.  A separate terminal theorem
converting bounded `Phi` into bounded appended literal masks then gives
`nu(k)<=B(k)+O(1)`.

The absolute-exposure hypothesis (5.1), the matroid/gammoid hypothesis, the
all-cut hypothesis (5.2), the
defect-to-terminal conversion, and the zero-loss regeneration of the other
rows are separate assumptions.  For a generic pairwise-compatibility
system, "maximum number of mutually compatible tickets" need not be a
matroid rank, need not be submodular, and Rado's deficiency formula is not
available.  The recurrence itself is exact once the stated matroidal inputs
are supplied.

### 5.1 Bounded reachable-task salvage is conditional

Suppose `Phi_k<=E` and (5.1) is known with absolute `b_0`.  Then the exposed
set has absolute size

\[
                         |U|\le H:=4E+b_0.             \tag{5.5}
\]

For such a set, an injective source-private anchor assignment and a
per-list multiplicity bound `kappa m` for every noncore physical or colour
token give external load at most `(H-1)kappa m`.  The same conclusion holds
for cap tickets only if their complete path vertices and sink tokens obey
the same multiplicity bound.  Thus bounded reachable task mass would remove
the full-atlas density obstruction and, with `O(d)` packet support, give
`Delta=O(md)`.

However, (5.1) is not presently a consequence of the same-parity Pascal
theorems.  The coefficient four is proved only for passive descendants of
an already declared upper hole over two new coordinates.  The fully guarded
state has three additional rows:

* the one-unit residence tax may create many internal hazards; after a
  nonflat repair they can be grouped into one compound collar task per
  changed seam only if that repair hits every hazard;
* exposed cut/seam upper casualties likewise group into at most `s`
  compound tasks by the exact bound `b_ell<=ell s`, but this is useful only
  after proving `s<=a Phi+s_0`; and
* no functorial parent-to-child common-cap map is known, so the compiler row
  is a reset rather than a bounded inherited halo, although its bounded-span
  seam deltas can be included in the same compound tasks.

Accordingly, bounded `Phi` does not currently imply bounded `|U|`.  The
finite-task argument above is a valid conditional salvage theorem, while an
all-parameter physical-lift estimate `s<=a Phi+s_0` plus an absolute
nonseam compiler-birth bound remains a separate missing Pascal theorem.  The
exact compound-task and finite-bank greedy implication is proved in
`MATH_THEOREM_R_REACHABLE_COMPOUND_SEAM_COLLAR_GREEDY_INDUCTION_20260731.md`.

## 6. The narrowed theorem target

The most useful next statement is therefore:

> **Composable buffered-hexagon atlas.**  After an injective assignment of
> nonexceptional tasks to private source incidences, a positive proportion
> of the `m^2` hexagons at every anchor lift to boundary-equivalent,
> resident, upper-bank-preserving, cap-ticketed whole packets.  Each packet
> uses `O(d)` tokens; every source-fixed token is private to its own list;
> and every other token has cross-list multiplicity `O(m)`.  The exceptional
> terminal state has bounded literal completion cost.

This hypothesis implies `nu(k)=B(k)+O(1)` by the primary Theorem 1.1 (or by
the weaker Theorem 1.4).  Its four genuinely
open ingredients are:

1. injective, source-private task-to-anchor assignment;
2. positive-density lifting after arbitrary-width witness guards;
3. `O(m)` **cross-list** token load after cap and topology tickets are
   added; and
4. boundary-equivalent composition plus a bounded terminal sidecar.

The raw `m^2` C6 count proves the central supply but none of these four
correlation statements.  Conversely, no exact zero-defect all-`k` braid is
needed once these four statements hold.

## 7. Exact audit and scope

Run

```text
python3 scratch/audit_catalan_buffered_hexagon_global_load_gate_20260731.py
```

The audit literally enumerates the complete labelled incidence-C6 atlases
at `m=2,3`, checks `m^2` distinct circuits per task, six task labels per
geometric circuit, and the exact incidence/vertex loads (3.8).  It also
replays the `m=2` private-anchor counterexample exhaustively, checks the
average-degree pruning equality rows, exhausts the ordinary-token and
directed-anchor load bounds on their smallest nontrivial alphabets, and
checks both tight complete-star bad-pair rows and the converse perfect-
matching counterexamples.  The frozen output is

```text
scratch/catalan_buffered_hexagon_global_load_gate_20260731.audit.json
```

Its scope is the raw labelled C6 atlas and the abstract selector reductions.
It does not construct a load-balanced Catalan task subatlas, prove the
absolute sparse-source exposure row (5.1), prove the star-cover guard for
physical packets, establish composition closure, or prove
`nu(k)<=B(k)+O(1)` unconditionally.
