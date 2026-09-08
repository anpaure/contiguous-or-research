# K17 guarded residual completion: ghost-flow theorem and proof-safe pipeline

Date: 2026-07-31  
Status: exact theorem/referee audit; no K17 word or equality claim  
Scope: a persisted `active2649`-type guard choice whose selected seams have
distinct lower colours and are disjoint from the selected protected source
colours.

## 1. The distinction that the recourse must preserve

Let (F) be the lower-rainbow Johnson 2-factor on the (N) rank-nine
owners (U), and let (C) be the (N) rank-eight colours.  For
(d\in C), write (f_d) for the unique source-factor edge of colour (d).
Let (A) be the fixed seam bank and (P) the exact OR-union of old source
edges protected by the chosen witness guards.

Two conditions are immediate and exact:

1. distinct physical seams in (A) have distinct colours; and
2. no seam of colour (d) is compatible with (f_d\in P).

The second condition must use the **selected** protected bank (P), not all
currently uncut source edges.  If (f_d\notin P), selecting a seam of colour
(d) merely forces (f_d) to be ejected in the eventual factor.  It is an
obligation for residual completion, not a no-good.  Thus the correct fixed
bank is (R=A\cup P), with physical-edge identity used to deduplicate
several reasons protecting the same edge.

## 2. Exact ghost-colour closure

Let

\[
 D=\{(u,d):u\in U, d\in C, d\subset u\}
\]

be the middle-level incidence graph.  Fix a proposed omitted colour
(z\in C).  Form (D_z^\circ) by

* retaining all physical incidences ((u,d)\in D) with (d\ne z);
* deleting the physical incidences at (z); and
* adding a labelled ghost incidence ((u,z)^\ast) for every (u\in U).

Every protected or service Johnson edge (uv) of colour (d) forces both
physical incidences ((u,d)) and ((v,d)).  No ghost incidence is forced.

### Theorem 2.1 (ghost-cycle equivalence)

There is an undirected spanning lower-rainbow Johnson path containing the
forced physical bank (R) and omitting exactly colour (z) if and only if
there is a connected spanning 2-regular subgraph of (D_z^\circ) containing
all incidences forced by (R).

The correspondence is bijective after retaining the two labelled ghost
incidences.  They identify the two endpoints of the owner path.

#### Proof

Expand each Johnson path edge (uv), of colour (d=u\cap v), to
(u-d-v).  Every owner occurs once, and every colour except (z) occurs
once.  Join the two path endpoints through the ghost vertex (z).  The
result is a connected alternating 2-factor on (U\dot\cup C), hence one
Hamilton cycle in (D_z^\circ), and it contains every forced edge as its two
physical incidences.

Conversely, the colour vertex (z) in a connected 2-factor of
(D_z^\circ) has two distinct ghost neighbours.  Delete (z) and those two
ghost incidences.  What remains is an alternating Hamilton path.  At every
other colour (d), its two owner neighbours are distinct rank-nine
supersets of the same rank-eight set (d), so they form a Johnson edge of
colour (d).  Thus the projected owner path is spanning and uses every
colour other than (z) once.  Forced incidence pairs project back to their
forced Johnson edges.  \(\square\)

This theorem makes the ejection ledger literal.  If a nonfactor edge of
colour (d) is forced, the degree-two vertex (d) has no capacity for the
different source edge (f_d).  A protected (f_d) is therefore fatal;
an unprotected (f_d) is simply absent from the completion.

## 3. What is flow-exact and what is not

For a fixed hole \(z\), drop connectedness in Theorem 2.1.  Requiring degree
two at every vertex of \(D_z^\circ\), with the incidences of \(R\) forced,
is an ordinary bipartite \(b\)-flow.  The forced-degree test and every
max-flow/min-cut inequality are necessary and sufficient for this
**degree-cover projection**.  The row is Theorem 5.1 of
`MATH_THEOREM_K17_LARGECUT_GUARDED_COMMON_BASE_COMPLETION_20260731.md`,
applied to \(D_z^\circ\) with \(b\equiv2\).

Explicitly, if \(\rho_e\) is the exact physical-incidence OR of all selected
guards which force incidence \(e\), then every \(X\subseteq U\) and
\(Y\subseteq C\) obeys

\[
 2|X|+\sum_{e\in D_z^\circ(U\setminus X,Y)}\rho_e
 \le 2|Y|+|D_z^\circ(X,C\setminus Y)|.             \tag{3.1}
\]

Together with forced degree at most two, these rows are sufficient for the
fixed-hole degree cover.  Thus a minimum cut yields a linear Benders row in
the guard ORs.  If the omitted colour remains a master variable, (3.1) is a
conditional row guarded by the assertion that the hole is \(z\); it is not
valid unconditionally for the other ghost graphs.

Consequently:

* an infeasible flow supplies an exact obstruction for this fixed \(z\);
* a bank is excluded by flow alone only after every allowed \(z\) has been
  excluded, or an exact master has selected \(z\) and replayed the
  corresponding conditional cut;
* a feasible flow is only a disjoint union of alternating cycles;
* cycles in one returned flow do not prove that another flow cannot be
  connected.

Connectedness is exact after adding the standard proper-subset rows

\[
 \sum_{e\in E(S)}q_e\le |S|-1
 \qquad(\varnothing\ne S\subsetneq U\dot\cup C),       \tag{3.2}
\]

because all vertices already have degree two.  A lazy solver must keep
separating every proper cycle until it produces one alternating Hamilton
cycle or proves the complete model infeasible.

The existing
`scratch/solve_k17_prescribed_incidence_bflow_20260731.py` instead asks for
degree two in the unmodified physical incidence graph.  It is exact for a
balanced Johnson 2-factor containing its frozen bank.  It is **not** exact
for path completion: UNSAT need not exclude a path, SAT need not give one
component, and the first cyclic SAT completion is not a bank obstruction.
The ghost-colour construction is the required path-exact replacement.

## 4. Direction, collars, and topology

The ghost flow is orientation-free.  For exact directed recourse, orient the
alternating Hamilton cycle.  A directed Johnson arc (u\to v) of colour
(d) is the two-arc block

\[
                         u\to d\to v.              \tag{4.1}
\]

At the ghost colour it is (t\to z\to h); deleting (z) opens the owner
path at (h,t).  Force (4.1) for every selected directed seam and every
directed old-witness block.  Add in/out degree one at every expanded vertex,
forbid all proper directed subtours, and retain the complete collar support
of every context-dependent seam.  This is equivalent to the tail/head/
colour/graphic arc system in the large-cut theorem.

The following are only projections:

* the undirected ghost (b)-flow;
* separate incoming and outgoing bipartite matchings;
* pairwise tail--head, tail--colour, and colour--head Hall tests; and
* one arbitrary cycle-cover returned by any of those models.

They can prove failure when their exact projection is infeasible, but none
can certify direction-compatible Hamilton completion.  In particular, two
prescribed directed arcs may lie in opposite orientations of the same
undirected path.

## 5. End-to-end proof-safe pipeline

For every persisted guarded candidate, record source and catalogue hashes
and then perform the following stages.

1. **Guard replay.** Reconstruct the exact physical OR-bank (R=A\cup P).
   Check Johnson legality, physical-edge antisymmetry, owner degree at most
   two, seam-colour injectivity, and seam/protected-source colour
   disjointness.  Do not freeze unprotected source edges.
2. **Hole-conditional ghost flow.** For each still-allowed omitted colour
   (z), solve the forced degree-two flow on (D_z^\circ).  Persist every
   selected incidence or, on failure, both sides and capacities of a
   replayable minimum cut.  Endpoint choice is already internal: the two
   selected ghost incidences are the endpoints.
3. **Exact directed topology.** Lift to directed two-arc colour blocks,
   include the selected protected blocks and the complete certified return
   domain, and separate proper subtours to exhaustion.  The output must be a
   single directed owner path.  A degree cover with several components is
   not a positive certificate.
4. **Residence/collar replay.** Replay every coordinate run on that literal
   path.  All ejection-created boundaries and return seams must either have
   their selected certified collars or pass literal residence directly.
5. **Arbitrary-width upper replay.** For every start, accumulate consecutive
   unions until the union is full (or the linear path ends).  Audit every
   rank ten through seventeen target.  Rank ten may use the adjacent-union
   shortcut; no fixed-width shortcut is valid at deeper ranks.
6. **CEGAR feedback.** A missing upper target rejects this completed path,
   not automatically the whole guard bank.  Add a complete guarded witness
   disjunction when available; otherwise add only the whole-completion
   no-good.  The same rule applies to a residence failure.
7. **Compiler and literal word.** Feed the connected carrier to the exact
   lower compiler/staircase model, decode the literal word, and replay all
   (2^{17}-1) nonempty masks and the exact length.  Carrier success alone
   is not an equality certificate.

## 6. Exact negative certificates and weakest relaxations

The status `UNSAT` is justified only at the following scopes.

* **Local bank conflict:** persist the two conflicting physical edges (or a
  forced cycle/degree witness) and the selected guards which force them.
* **Ghost-flow cut:** state the hole (z), full incidence catalogue hash,
  forced incidence ORs, cut shores, residual demands, crossing capacity,
  and positive deficit.  To reject the bank without fixing (z), supply
  such a certificate for every allowed hole or an independently replayable
  exact disjunctive proof.
* **Topology/direction UNSAT:** use the complete directed return/collar
  catalogue and exhaust all lazy subtours.  Persist the model and a solver
  proof or a deletion-minimal assumption core replayed against that same
  complete catalogue.  Failure of one flow completion is not enough.
* **Literal upper/residence failure:** this is a certificate only against the
  decoded path.  A master-level no-good needs either a complete alternative
  witness enumeration or full recourse UNSAT under the guard assumptions.

A violated ghost-flow cut gives the weakest principled relaxation directly:
release or reselect guards whose forced incidences cross the offending cut,
or choose another omitted colour.  Its guarded linear inequality is the
forced-set min-cut row, with physical/incidence OR variables rather than
reason counts.  Do not relax seam-colour injectivity.  If degree flow passes
but a proper component is entirely forced, release at least one guard from
that forced component; if the component contains optional flow edges, add a
recourse subtour row instead of cutting the guard bank.

## 7. Required interpretation of the live lane

The first fully coupled master must therefore mean:

* all 2,649 active target choices are exported;
* selected seam colours are distinct;
* selected protected source colours are disjoint from seam colours;
* unprotected old source conflicts remain available as ejection cuts; and
* any positive is passed through Sections 5.2--5.7.

Upper-(q_1) exactness is only an upper-coverage statement.  It does not
imply ghost-flow feasibility, connectedness, lower-rainbow completion,
residence, compiler feasibility, or a literal universal word.
