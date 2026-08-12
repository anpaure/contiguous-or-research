# Lane W: finite `CAA_29`, moving-DM separation, and an exact five-parent certificate search

Date: 2026-07-28

## Deployment correction (authoritative)

The theorem statements below remain valid, but the adaptive-motif deployment
described in former Sections 6--8 is superseded by
`MATH_AUDIT_W_CAA29_H100_DEPLOYMENT_SOFT_HOMOTOPY_AND_BRANCH_SCOPE_20260728.md`.
One exact five-parent shore expands to about 11.8 million motifs / 474 MB, so
the launch now persists exact 19,311-position Hall rows and never builds motif
TSVs by default.  On H100 use repository `/dev/shm/k15_rotation` and export
`PYTHONPATH=/dev/shm/orlib`.

All transpositions in this lane are **zero-based bit indices**.  Thus
`(1,12),(3,4),(10,11),(3,13)` mean the one-based mathematical coordinate
pairs `(2,13),(4,5),(11,12),(4,14)`.

**Index convention.** Every coordinate tuple copied from a relabel screen in
this note is zero based.  In particular `[1,12]_0=(2,13)_1`.

## 0. Verdict

`CAA_29` is now a literal finite certificate problem.  Three corrections are
essential.

1. The state score is the **actual maximum compiler matching number**
   \[
      \mu(C)=\nu(G_C),
   \]
   certified by a matching and an equal-size vertex cover.  It is not the
   size of an arbitrarily carried matching and not the number of old DM cuts
   repaired.
2. A packet carries its complete successor permutation.  Parity and genus
   are exact audits, but neither they nor the number of subtours is a Markov
   state.  The full successor-cycle words are retained, and an accepted
   packet endpoint is traversed to prove that it has one cycle.
3. If success records have total reverse congestion \(A_+\), the entropy
   polynomial begins \(A_+x\), not \(x\).  Coefficient one requires the
   combined map from predecessor/trial to output to be injective after
   forgetting the trial label.

For a transition \(C\to Q\), a strict increase in \(\mu\) is equivalent to
the complete moving-DM inequality over **every** target shore.  It therefore
cannot merely relocate deficiency.

There is also a sharp conceptual simplification.  An explicit finite closed
atlas satisfying the entropy theorem necessarily already contains a
terminal Hall-zero carrier.  With unrestricted correlated packets, `CAA_29`
is equivalent to finding that carrier directly.  Entropy compression is
non-tautological only after imposing a reusable support/template restriction
and proving its Laurent inequality.

Accordingly, the implemented finite route is a moving-DM Benders search:

* every candidate is exactly Hamilton, residence-safe, and upper-complete;
* every deficient candidate returns its current exact DM shore;
* that shore is added as an exact physical-cell Hall constraint;
* acceptance is only \(\mu(C)=16383\), independently recomputed; and
* a terminal result carries a 16,383-edge matching and a König cover.

This procedure is finite and cannot accept a relocated Hall-29 block.  The
search code and verifier are complete, but no H100 job was run: all three
saved H100 endpoints are offline and the installed RunPod CLI has no API
key.  No Hall-zero carrier is claimed.

## 1. Frozen five-parent catalogue

The phrase “five parents” is ambiguous elsewhere in the repository.  This
lane uses exactly
\[
 \mathcal P_W={
 P_{29},
 (1,12)P_{29},
 (3,4)P_{29},
 (10,11)P_{29},
 (3,13)P_{29}
 \}.
 \tag{1.1}
\]
The four displayed transpositions use zero-based bit labels in
`{0,...,14}`.
The base artifact is
`scratch/k15_doubletrans_05_213_hall29.json`, with SHA-256
\[
 5516482eadaba4f8fb9549b41c79c3b949df2e3224ce68f9dacd3b5b6bc2d21c.
 \tag{1.2}
\]
Every run materializes the four relabels from this base and freezes all five
hashes in its manifest.

The union has exactly 21,023 normal directed arcs, with source-multiplicity
histogram
\[
 {1:14714, 2:2860, 3:2238, 4:1033, 5:178}.
 \tag{1.3}
\]
Its normal outdegree histogram is
\[
 {1:178, 2:1137, 3:2498, 4:2028, 5:593},
 \tag{1.4}
\]
apart from the unique terminal source of each linear parent representation.

Adjoin the dummy \(\partial\).  The only augmented endpoint arcs in this
catalogue are
\[
 (7779,\partial),qquad
 (\partial,9901),quad(\partial,9909),quad(\partial,10925).
 \tag{1.5}
\]
Thus the augmented union has 21,027 arcs.

The general directed-parent solver formerly allowed the dummy to attach to
every middle vertex.  That larger model is not the successor-factor space
of (1.1).  The new option `--parent-dummy-only` imposes exactly (1.5), and
the finite search always enables it.  The independent verifier checks the
same condition from the hashed parent paths.

## 2. Canonical legal states and exact rollback score

Let
\[
 X=\binom{[15]}8\cup\{\partial\},qquad |X|=6436.
 \tag{2.1}
\]
A legal carrier \(C\) is a successor permutation on \(X\) such that:

1. every selected arc lies in the augmented union (1.1);
2. \(C\) has one cycle;
3. cutting at \(\partial\) gives no forbidden residence path of two through
   four normal arcs; and
4. all
   \[
      \sum_{q=1}^7\binom{15}{8+q}=9949
   \]
   upper targets have literal non-wrapping witnesses.

For a legal carrier, let \(G_C=(\mathcal T,\mathcal C;E_C)\) be its exact
physical compiler graph.  Here
\[
 |mathcal T|=16383,qquad |mathcal C|=19311.
 \tag{2.2}
\]
Define
\[
 \mu(C)=\nu(G_C),qquad
 \delta(C)=16383-\mu(C),qquad
 h(C)=\mu(C)-16354.
 \tag{2.3}
\]
The initial carrier has \(h=0\); the unique terminal score is \(h=29\).

### Theorem 2.1 (primal-dual score certificate)

Suppose \(M_C\) is a matching and
\[
 K_C=K_C^{\mathcal T}\mathbin{\dot\cup}K_C^{\mathcal C}
 \]
is a vertex cover of \(G_C\) with
\[
 |M_C|=|K_C|=s.
 \tag{2.4}
\]
Then \(\mu(C)=s\).  Moreover, putting
\[
 A_C=\mathcal T\setminus K_C^{\mathcal T},
 \tag{2.5}
\]
one has
\[
 N_C(A_C)=K_C^{\mathcal C},qquad
 |A_C|-|N_C(A_C)|=16383-s.
 \tag{2.6}
\]

#### Proof

Weak duality gives \(|M|\le|K|\) for every matching and vertex cover.
Equality in (2.4) proves optimality of both.

Because \(K_C\) covers every edge, every neighbour of a target outside
\(K_C^{\mathcal T}\) lies in \(K_C^{\mathcal C}\).  Hence
\(N_C(A_C)\subseteq K_C^{\mathcal C}\), and
\[
 |A_C|-|K_C^{\mathcal C}|
 =16383-|K_C^{\mathcal T}|-|K_C^{\mathcal C}|
 =16383-s.
\]
Hall deficiency cannot exceed \(16383-s\), because \(s\) is the maximum
matching size.  Therefore the displayed inclusion must be equality, proving
(2.6). \(\square\)

Auxiliary matching, cover, and upper-witness choices are canonically chosen
under fixed total orders.  This avoids multiplying one physical carrier
into many flag states and paying that artificial multiplicity in reverse
congestion.

## 3. Complete correlated packet and circuit certificate

Let \(C,Q\) be successor factors in the five-parent union, with \(C\)
Hamilton, and put
\[
 \rho=C^{-1}Q.
 \tag{3.1}
\]
The nontrivial cycles of \(\rho\) are exactly the vertex-disjoint alternating
successor cycles switched in the packet \(C\to Q\).  Thus the relative-cycle
list is a complete correlated packet description; its constituent cycles
are not claimed to be independently Hamilton-safe.

Put
\[
 s(C,Q)=6436-c(\rho).
 \tag{3.2}
\]

### Theorem 3.1 (exact packet topology ledger)

There is an integer \(g(C,Q)\ge0\) for which
\[
 c(Q)=1+s(C,Q)-2g(C,Q).
 \tag{3.3}
\]
Consequently \(Q\) is Hamilton exactly when its complete successor
partition has one member, \(s(C,Q)\) is even, and
\[
 g(C,Q)=s(C,Q)/2.
 \tag{3.4}
\]

#### Proof

The permutations \(C\) and \(\rho\) define a connected orientable
permutation map: \(C\) is transitive.  Euler's formula gives
\[
 2-2g
 =c(C)+c(\rho)-6436+c(C\rho)
 =1+c(\rho)-6436+c(Q).
\]
Substitute (3.2) and rearrange. \(\square\)

Parity, genus, and the scalar \(c(Q)\) do not determine how a later packet
meets the present subtours.  A finite state therefore retains the full
successor permutation.  For an atomic completed candidate, traversing from
\(\partial\) for 6436 steps is a complete subtour certificate.

The implemented packet record contains:

* the changed-tail count;
* every nontrivial relative-cycle word and its length;
* \(s(C,Q)\bmod2\);
* \(c(Q)\) and \(g(C,Q)\); and
* the size of the \(\partial\)-orbit.

The verifier requires \(c(Q)=1\), \(g=s/2\), and a \(\partial\)-orbit of
size 6436.

## 4. Matching gain is exactly the all-shore condition

For \(A\subseteq\mathcal T\), write
\[
 g_C(A)=|A|-|N_C(A)|,qquad
 v_{C,Q}(A)=|N_Q(A)|-|N_C(A)|.
 \tag{4.1}
\]

### Theorem 4.1 (moving-DM/all-shore transition theorem)

For an integer \(d\), the inequality
\[
 \mu(Q)\ge\mu(C)+d
 \tag{4.2}
\]
holds if and only if, for every \(A\subseteq\mathcal T\),
\[
 \boxed{
 v_{C,Q}(A)
 \ge g_C(A)-\delta(C)+d.}
 \tag{4.3}
\]

#### Proof

Hall's deficiency formula turns (4.2) into
\[
 g_Q(A)\le\delta(C)-d
 \quad\text{for every }A.
\]
Since \(g_Q(A)=g_C(A)-v_{C,Q}(A)\), this is exactly (4.3). \(\square\)

Thus a positive exact score increment cannot be an equal-deficiency
relocation.  At level \(h\), a one-level success is equivalently
\[
 |N_Q(A)|\ge |A|-(28-h)
 \quad(A\subseteq\mathcal T).
 \tag{4.4}
\]
At \(h=28\), the successful output already satisfies ordinary Hall on every
shore; \(h=29\) is terminal.

The native Hall auditor now has an optional `--certificate` mode.  It emits
the exact matching edges and the König cover
\[
 (\mathcal T\setminus DM_L)\mathbin{\dot\cup}DM_R.
 \tag{4.5}
\]
The independent verifier reconstructs every physical compiler edge, checks
the matching, checks that (4.5) covers every edge, and recomputes \(\mu\).

## 5. Correct low-congestion atlas inequality

Type a packet by its absolute symmetric-difference arc set
\[
 D(C,Q)=E(C)\mathbin\triangle E(Q)
 \tag{5.1}
\]
and score increment \(d=\mu(Q)-\mu(C)\).

### Lemma 5.1 (unit reverse congestion for absolute packet types)

Given \(Q\), \(D\), and \(d\), there is at most one predecessor \(C\):
\[
 E(C)=E(Q)\mathbin\triangle D.
 \tag{5.2}
\]
If a state does not use the same absolute \(D\) in two trial slots, the
backward congestion of type \((D,d)\) is at most one.

#### Proof

Symmetric difference is an involution, so (5.2) fixes the entire predecessor
successor set.  The remaining legality and score tests can reject it but
cannot create another predecessor. \(\square\)

Let \(\mathcal S\) be a finite closed set of nonterminal canonical states,
containing the initial state.  Give every state exactly \(R\) distinct
trials.  A trial either reaches a terminal carrier or reaches another state
of \(\mathcal S\).  Let \(\mathfrak B\) be the set of nonterminal absolute
types used.

### Theorem 5.2 (finite unit-congestion `CAA_29`)

If some rational \(x>0\) satisfies
\[
 \boxed{
   \sum_{(D,d)\in\mathfrak B}x^d<R,}
 \tag{5.3}
\]
then a finite trial word reaches a terminal carrier.

#### Proof

For a nonterminal length-\(N\) history, record its final state and its
sequence of absolute types.  Lemma 5.1 reconstructs at most one history.
If the final score is \(m\), the recorded increments sum to
\(m-\mu(C_0)\).  The weighted number of records is bounded by
\[
 \left(\sum_{(D,d)\in\mathfrak B}x^d\right)^N
 \sum_m |\{C\in\mathcal S:\mu(C)=m\}|x^{\mu(C_0)-m}.
\]
The second factor is fixed.  Under (5.3), this is \(o(R^N)\), while there
are \(R^N\) input words.  Some word must terminate. \(\square\)

For coarser types or duplicate trial slots, replace each term by
\(c_{D,d}x^d\), with its exact reverse congestion.  In the traditional
success/rollback grouping this gives
\[
 F(x)=A_+x+\sum_{\ell\ge1}A_\ell x^{1-\ell}.
 \tag{5.4}
\]
If only rollback lengths one and two occur, the exact threshold is
\[
 R>A_1+2\sqrt{A_+A_2}.
 \tag{5.5}
\]

The success-volume cut
\[
 s_h|\mathcal Q_h|\le A_+|\mathcal Q_{h+1}|
 \tag{5.6}
\]
is necessary whenever every level-\(h\) state has at least \(s_h\)
successful trials.  It follows by counting predecessor/trial pairs by their
output and success type.  This is why arbitrary matching and upper-witness
flags must be canonicalized.

### Proposition 5.3 (an explicit closed atlas already contains the answer)

With unrestricted correlated packets, the following are equivalent:

1. the five-parent union contains a terminal Hall-zero carrier;
2. an explicit finite `CAA_29` atlas exists; and
3. an atlas exists with only the initial nonterminal state and one terminal
   trial.

#### Proof

An atlas satisfying Theorem 5.2 reaches a terminal state, proving
\(2\Rightarrow1\).  The implication \(3\Rightarrow2\) is immediate.  If a
terminal \(Q\) exists, the nontrivial cycles of \(C_0^{-1}Q\) form one
correlated packet from the initial carrier to \(Q\).  Take \(R=1\) and no
nonterminal record types; (5.3) is \(0<1\). \(\square\)

Thus a finite atlas search is a useful generator or heuristic, but it is not
a smaller positive certificate than the terminal carrier.  A theorem-level
entropy advance requires a restricted reusable packet library.

## 6. Finite moving-DM Benders decision theorem

Let \(\Omega\) be the finite legal carrier set in the exact augmented union
(1.1).  Begin with no shores.  At round \(i\), find a carrier \(C_i\in\Omega\)
satisfying
\[
 |N_{C_i}(A)|\ge|A|
 \quad\text{for every previously accumulated shore }A.
 \tag{6.1}
\]
Compute a maximum matching and minimum cover.  If \(\mu(C_i)=16383\), stop.
Otherwise add the maximizing shore \(A_i\) from (2.5), imposing
\[
 |N_C(A_i)|\ge|A_i|
 \tag{6.2}
\]
on all later candidates.

### Theorem 6.1 (finite relocation-safe separation)

The procedure terminates after finitely many rounds.  It returns a Hall-zero
carrier if one exists and the carrier subproblem is solved exactly; otherwise
the accumulated exact model is infeasible.  No Hall-zero carrier is ever
excluded, and no deficient carrier can recur.

#### Proof

Every Hall-zero carrier satisfies (6.2) for every shore, so no separating cut
excludes one.  For the current deficient candidate, (2.6) gives
\[
 |N_{C_i}(A_i)|=|A_i|-\delta(C_i)<|A_i|,
\]
so its new cut excludes it.  A duplicate shore is impossible for a later
candidate, because that shore's exact constraint is already active.  Since
\(\Omega\) is finite, the process terminates. \(\square\)

This theorem permits deficiency to move during the search.  It forbids the
search from mistaking that movement for success: every moved maximizing
shore is separated, and the only positive terminal is the full matching.

For depth three, the exact predicate in (6.2) has a finite compact encoding:

* centered interior cell states use exactly 5, 6, and 7 selected normal arcs
  at row depths 0, 1, and 2;
* the order channel supplies the two endpoint guards for each interior
  state; and
* the first/last eight-edge order states encode all 36 boundary cells
  exactly.

The production encoding is now the exact position-indexed formulation: one
claim per physical cell and one fitting shore target chosen conditionally on
that claim.  It is equisatisfiable with (6.2).  The old native adaptive-motif
builder remains a reproducibility tool only.  A measured single shore already
contains about 11.8 million motifs, so merging such catalogues is not a viable
iterative representation.

An exact positive output is independently checkable.  A CP-SAT
`INFEASIBLE` status is not promoted here to a solver-independent theorem
without a separately checkable proof log.

## 7. Implemented files and certificate checks

The implementation is:

* `scratch/search_k15_caa29_five_parent_benders.py` — materializes and hashes
  the five parents, persists exact position-indexed DM shores, runs the exact
  carrier model, independently audits Hall, adds the current DM shore, and
  records the packet topology ledger;
* `scratch/verify_k15_caa29_five_parent_certificate.py` — reconstructs the
  five-parent arc union, checks normal and dummy arc provenance, recomputes
  relative cycles/parity/genus/subtours, rechecks residence and all upper
  targets, rebuilds the compiler graph, and checks the terminal matching and
  König cover;
* `scratch/search_k15_directed_parent_union_cpsat.py` — has the exact
  `--parent-dummy-only` restriction, the shared 19,311-position channel,
  repeatable hard shore files, and a distinct soft-to-hard homotopy;
* `scratch/fast_k15_hall_dm.cpp` — now has `--certificate`, emitting matching
  edges and minimum-cover shores; and
* `scratch/launch_k15_caa29_h100_cpu.sh` — rebuilds the Hall auditor and
  launches a one-cut position-channel smoke by default on an H100 host.

Every manifest records:

1. the base and four relabel parent paths with hashes;
2. every candidate path and hash;
3. every moving-DM shore and its exact deficient neighbourhood;
4. the relative-cycle packet ledger between successive candidates;
5. the exact matching value at every candidate; and
6. for a terminal result, the 16,383 matching edges and same-size vertex
   cover.

The terminal verifier checks every matching edge against the rebuilt
physical compiler graph and checks that the emitted cover meets every graph
edge.  Hence the terminal score is not a trusted scalar field.

Lightweight local validation completed:

* all Python files pass bytecode compilation;
* the modified Hall auditor compiles and its `--certificate` mode emits an
  exact 16,354-edge matching and cover on the incumbent;
* the position-shore encoding has an independent formula/carrier/native
  equality audit;
* parent materialization produces five paths, starts
  \(\{9901,9909,10925\}\), and end \(7779\); and
* the H100 launch script passes shell syntax checking.

No CP carrier search was run locally.

## 8. H100 execution boundary

The three saved RunPod SSH endpoints were probed and all returned immediate
connection refusal:

* `157.157.221.30:13754`;
* `157.157.221.29:29276`;
* `157.157.221.30:48138`.

The installed `runpodctl` reports that no API key is configured, so a new
pod cannot be started from this environment.  Local Python also lacks
OR-Tools, and the user prohibited heavy local work.  Therefore no finite
carrier solve was launched.

On a reachable H100 host, the first required run is the bounded one-cut smoke

```bash
cd /dev/shm/k15_rotation
export PYTHONPATH=/dev/shm/orlib
scratch/launch_k15_caa29_h100_cpu.sh \
  /dev/shm/caa29_position /dev/shm/k15_rotation smoke
```

The repository and `PYTHONPATH` values are part of the audited H100 contract.
The smoke uses two outer rounds, so at most its second solve contains the
first persisted position shore.  The per-shore model is much smaller than
11.8 million motif indicators but still large; a full run is not authorized
by the representation theorem alone.  `TIMEOUT`, `UNKNOWN`, or the round
limit is inconclusive.  Only an independently verified `HALL_PASS` is a
positive mathematical result.

## 9. Precise proved/unproved boundary

Proved:

1. complete finite correlated-packet parametrization by relative cycles;
2. exact parity/genus/full-subtour packet certificate;
3. exact compiler-rank score by matching-cover duality;
4. equivalence between score gain and every moving-DM shore inequality;
5. unit reverse congestion for absolute symmetric-difference packet types;
6. the corrected finite Laurent criterion;
7. equivalence of unrestricted explicit atlas existence and terminal-carrier
   existence; and
8. a finite, relocation-safe dynamic-DM decision procedure with an
   independent positive verifier.

Unproved:

1. a support/template-restricted low-congestion atlas satisfying (5.3);
2. existence of a Hall-zero carrier in the hashed five-parent union; and
3. any constant-one consequence.

The remaining mathematical alternative is now sharp: prove (5.3) for a
restricted reusable packet family, or obtain the terminal carrier from the
finite search.  Old-zero positivity and any fixed DM list are insufficient.
