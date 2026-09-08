# `k=17`: proof-safe launch specification for the complete radius-three catalogue

**Date:** 2026-08-02  
**Lane:** A, pure theorem / D handoff  
**Status:** exact catalogue and certificate specification for the
one-for-one, three-distinct-base recut face.  No SAT instance is built or
solved here.  `LIBRARY_OPEN` below is an inconclusive promotion label, never
a q1-feasibility verdict.

## 1. Declared finite face

Let `B0` be the authenticated round-02 bank.  For every base `b`, let
`q0(b)` be its selected cut and let `C(b)` be its authenticated set of legal
cut choices.  The primitive catalogue is

\[
 \mathcal R=\{(b,q_0(b),q):q\in C(b)\setminus\{q_0(b)\}\}.   \tag{1.1}
\]

The present input has

\[
                         N=|\mathcal R|=16667.               \tag{1.2}
\]

A packet in the declared **radius-three face** is a set

\[
 S=\{g_0,g_1,g_2\}\subset\mathcal R                         \tag{1.3}
\]

whose three base fields are pairwise distinct.  Its final cut vector is

\[
 q_S(b)=
 \begin{cases}
   q,&(b,q_0(b),q)\in S,\\
   q_0(b),&\text{otherwise}.
 \end{cases}                                                 \tag{1.4}
\]

Overlapping same-base changes, a recut followed by another recut of the same
base, segment rethreads, correlated `C8` packets, `C8+recut`, and four or
more independent recuts are outside this catalogue.  In particular, the
atomic `3+1`-`C8` face from the companion theorem remains a separate launch.

Let `A21` be the authenticated twelve visible socket escapes plus the nine
central alternatives.  The frozen root-fan theorem says that every packet
in (1.3) which destroys the original `114930` q1 core meets `A21`.  Thus a
joint-zero-265 and q1-feasible packet in this face must meet `A21`.
Partition the authenticated q1 library into `L0`, whose entries are
unconditional contradictions, and `Lsucc`, whose entries are valid only
after a named pivot-footprint contraction.  `L0` is required to contain the
root-fan core and its unchanged-trace certificate.  Hence triples disjoint
from `A21` form one compressed, proof-certified rejection family; they are
not silently omitted from the declared face.

Closure of the current `3,664` Hamming-two portfolio is not assumed by the
catalogue theorem.  A run may be advertised as the *first new independent-
recut shell* only if a separately authenticated closure manifest for those
`3,664` banks is present and its hash agrees.  Otherwise the radius-three
catalogue is still exact, but that chronological label is unavailable.

## 2. Immutable keys and direct final-net reconstruction

### 2.1 Primitive keys

The primitive recut key is the literal triple

\[
                  \operatorname{rk}(g)=(b,q_0(b),q).         \tag{2.1}
\]

The primitive input is sorted lexicographically by (2.1), duplicate rows
are forbidden, and `rid(g)` is its zero-based position in that order.  A
numeric job id, dense piece id, or generation order is not a physical key.

The canonical packet key is

```
R3:<rid0>,<rid1>,<rid2>
```

with `rid0 < rid1 < rid2`.  The full three primitive keys are repeated in
the packet record so that a verifier need not trust `rid` alone.

### 2.2 Occurrences and q1 atoms

Every rebuilt oriented occurrence has a content key containing

* its immutable source/base key and selected cut;
* its side and orientation;
* its complete ordered owner trace; and
* every endpoint/role label used by a q1 row.

Call this key `OccKey`.  The canonical native q1-atom key is

\[
  \operatorname{AtomKey}(e)=
  (\operatorname{OccKey}(\tau(e)),
   \operatorname{OccKey}(\eta(e)),\gamma(e),\partial e),    \tag{2.2}
\]

together with the complete physical unit-capacity footprint of `e`.
Independent construction routes producing the same (2.2) are provenance
records for one atom, not parallel q1 variables.  Conversely, equal owner
masks do not identify different occurrence keys.

### 2.3 Direct reconstruction contract

For every subset `T subseteq S`, including dirty singleton and pair
subsets, the bank `B[T]` is rebuilt **directly** from the cut vector `q_T`.
Subset-mask bit `i` refers to canonical primitive `rid_i`.
The implementation must not obtain `B[S]` by applying three stored deltas in
some order.  It reconstructs from the raw physical input:

1. all path pieces and both oriented occurrence states;
2. the complete selected lower-colour multiset;
3. every legal q1 atom and its complete resource footprint;
4. every tail, head, orientation and colour row; and
5. the five frozen zero-265 coordinates.

For every physical datum `x`, store its eight-bit subset truth table

\[
          \bigl({\bf1}_{x\in B[T]}:T\subseteq S\bigr).       \tag{2.3}
\]

The genuinely new residue

\[
 J_T=E(B[T])\setminus\bigcup_{U\subsetneq T}E(B[U])         \tag{2.4}
\]

is therefore exact for unary, binary and ternary activation.  Deletions,
role moves, changed blockers, changed capacities and nonmonotone
compensations are obtained by the same eight-bank comparison, not inferred
from (2.4) alone.

## 3. Exact canonical generator and support bound

Order `A21` by its primitive `rid`.  For a compatible triple `S` meeting
`A21`, define its **primary anchor**

\[
             \alpha(S)=\min_{\rm rid}(S\cap A21).           \tag{3.1}
\]

The launch generator iterates an anchor `a` and an unordered pair
`{g,h}` from `R minus {a}`, but emits the proposal only when

1. `a,g,h` have distinct bases;
2. their `rid`s give three distinct primitives; and
3. `a=alpha({a,g,h})`.

It then writes the sorted canonical packet key.  No post hoc choice among
duplicate anchor proposals is permitted.

### Theorem 3.1 (no-duplicate canonicalization)

The preceding primary-anchor generator is a bijection onto the compatible
three-recut supports meeting `A21`.  Moreover the final cut vector (1.4)
recovers the canonical support uniquely.

#### Proof

Every compatible support meeting `A21` has the unique least anchor (3.1), so
it is emitted by that anchor.  A proposal under any other anchor in the same
support fails condition 3, and no anchor outside the support can emit its
three sorted primitive keys.  This proves generation exactly once.

For support recovery, the bases on which `q_S` differs from `q0` are exactly
the three bases of `S`.  At each such base, uniqueness of the primitive
table identifies the unique `(base,old,new)` record.  Thus equal final cut
vectors imply equal canonical supports. \(\square\)

Two different supports may have isomorphic q1 graphs; they remain different
physical packets.  Canonicalization removes duplicate physical supports,
not semantic isomorphism classes.

For each base put

\[
 n_b=|\{g\in\mathcal R:\operatorname{base}(g)=b\}|,
 \qquad
 a_b=|\{g\in A21:\operatorname{base}(g)=b\}|.              \tag{3.2}
\]

The exact number of canonical compatible supports before semantic filtering
is

\[
 \sum_{b<c<d}
 \bigl[n_bn_cn_d-(n_b-a_b)(n_c-a_c)(n_d-a_d)\bigr].         \tag{3.3}
\]

For the frozen base histogram this evaluates to

\[
 \begin{aligned}
 e_3(n)&=770,667,109,363,\\
 e_3(n-a)&=767,757,643,652,\\
 e_3(n)-e_3(n-a)&=\boxed{2,909,465,711}.
 \end{aligned}                                               \tag{3.4}
\]

The last number splits by the number of anchors in the support as

\[
 2,906,453,982\quad+\quad3,010,838\quad+\quad891.            \tag{3.5}
\]

Consequently the distinct-base anchor-first proposal stream has
`2,912,478,331` rows before the primary-anchor condition, of which exactly
`3,012,620` are secondary-anchor duplicates.  These are required audit
identities, not estimates.

Indeed, after choosing three distinct bases `b<c<d`, there are
`n_b*n_c*n_d` primitive triples and exactly
`(n_b-a_b)(n_c-a_c)(n_d-a_d)` avoid every anchor, proving (3.3).  Counting
an anchored triple once for each of its one, two or three anchors gives the
raw proposal count; subtracting the canonical count gives the displayed
duplicate count.  The three summands in (3.5) are the corresponding exact
anchor-multiplicity classes.

In particular it is at most

\[
 {N\choose3}-{N-21\choose3}=2,912,760,025,                 \tag{3.6}
\]

which is slightly sharper than the proposal bound
`21*binom(16666,2)=2,916,258,345`.  Formula (3.6) ignores same-base
incompatibility and is therefore larger than the exact value (3.3).

The complementary no-anchor family has the exact compressed count

\[
                  \sum_{b<c<d}(n_b-a_b)(n_c-a_c)(n_d-a_d). \tag{3.7}
\]

Together, (3.3) and (3.7) partition every compatible support-three packet
in the declared face.  Each member of (3.7) retains the authenticated root
fan and is therefore q1-infeasible.  No final provider degree or mask test
is used in this compressed rejection.

For an unconditional core `K in L0`, let `A_3(K)` be its authenticated
inclusion-minimal one-, two-, and three-recut dependency anchors.  The proof-safe
precondition

\[
   \forall K\in\mathcal L_0\quad
   \exists A\in A_3(K)\text{ with }A\subseteq S             \tag{3.8}
\]

may be imposed before full reconstruction.  Omitting a triple by (3.8) is
allowed only when the corresponding unchanged-core certificate is named.
An incomplete anchor table may be enlarged, but may not be used for a
negative omission.  A conditional entry of `Lsucc` may not be used in
(3.8), because its contradiction is not asserted before its named
contraction.

## 4. The proof-safe semantic sieve

### 4.1 Literal zero-265

After direct joint reconstruction, record separately

```
zero_lower  zero_out  zero_in  zero_orientation  zero_rank10
```

and retain a packet at this stage exactly when all five values are zero.
Their sum, a provider degree, a mask count, or the scores of proper subsets
is not a substitute.  A dirty singleton or pair may be repaired by the full
triple and therefore is never discarded before this joint replay.

### 4.2 Unconditional exact q1 cores

On the direct final atlas, reject a packet if an unconditional entry of
`L0` is certified by one of the following complete tests:

* an unchanged occurrence-labelled trace;
* a typed guarded-minor embedding, with blockers for every final provider
  outside each mapped positive row;
* a physical resource support `U` with exact positive deficiency; or
* an implication bicycle all of whose arcs have literal or independently
  replayed boundary-language derivations.

A core datum changing is not evidence that the core disappeared: every
permitted typed transport/embedding from the library manifest is checked on
the final atlas.  Provider degrees, owner masks and colour multiplicities
are prioritization data only.

### 4.3 Exact q1 successor-core filter

On the complete final q1 resource hypergraph, reconstruct the exact final
pivot resources `U0(B)` and signature family `Sigma_B(U0(B))`.  A relocated
central role changes `U0(B)`; the old socket masks may not be reused.  Each
signature contains its selected seams
and their complete socket/colour/protected-resource footprint.  Contract a
signature by deleting all consumed resources and every incident atom.

For each stored entry `K in Lsucc` and every permitted occurrence-labelled
embedding, test closure by exactly one authenticated mechanism:

* positive resource deficiency with complete outside footprints;
* a typed guarded-minor embedding with blockers for every extra provider;
  or
* an entailed implication bicycle with literal derivations of every arc.

The packet is rejected by the library exactly when

\[
 \forall P\in\Sigma_B(U_0)\quad
 \exists K\in\mathcal L_{\rm succ}:K\text{ closes }B/P.    \tag{4.1}
\]

It is promoted as `LIBRARY_OPEN` exactly when

\[
 \exists P\in\Sigma_B(U_0)\quad
 \forall K\in\mathcal L_{\rm succ}:K\text{ does not close }B/P. \tag{4.2}
\]

For (4.2), nonclosure is certified relative to the finite library: a
resource support supplies a compatible saturating family; a guarded minor
or bicycle supplies the named failed incidence, blocker, clause, vertex or
arc; and the embedding manifest proves that every permitted embedding was
examined.  Failure to finish that manifest is `UNKNOWN`, not `LIBRARY_OPEN`.
Such a named failure is an `OPEN_MANIFEST` certificate for the stored
derivation, not semantic non-entailment by all possible derivations.  The
latter requires a countermodel or a separately complete entailment replay.
If `Sigma_B(U0)` is empty, q1 infeasibility is immediate; it is not an open
branch.  An unconditional certificate may also occur in `Lsucc` only when
its validity after the declared contraction is separately proved.

### Theorem 4.1 (sound semantic prefilter)

A packet rejected by (3.8), an unconditional Section 4.2 certificate, or
(4.1) is q1-infeasible.  After unconditional closure, the set of packets
passing (4.2) is exactly the residue not refuted by the declared successor-
core proof system.

#### Proof

An omitted packet in (3.8) leaves the named authenticated q1 core unchanged.
Every Section 4.2 certificate entails an unconditional contradiction.  For
(4.1), every q1 solution induces one exact pivot footprint `P`; the
residual selection would solve `B/P`, contradicting the core closing that
branch.  Formula (4.2) is the literal negation of (4.1) over finite complete
signature and embedding manifests. \(\square\)

Passing (4.2) does not imply q1 feasibility.  It may expose a new Hall
shore, a larger resource support, or a core outside `L`.

### 4.4 Finite semantic-support bound

For a resource set `W`, write

\[
 \operatorname{Inc}_B(W)=\{e:\partial e\cap W\ne\varnothing\},
 \qquad \rho=\max_e|\partial e|.                         \tag{4.3}
\]

For a fixed footprint `P`, every declared semantic decision is determined
inside a kernel whose seam and resource sets satisfy

\[
\begin{aligned}
 |E_{\rm ker}|\le{}&|\operatorname{Inc}_B(U_0)|
 +\sum_{K\in Lsucc}
   |\operatorname{Inc}_{B/P}(U(K)\setminus\partial P)|\\
 &+\sum_{K\in L0\cup Lsucc}|E(D(K))|.
\end{aligned}                                             \tag{4.4}
\]

\[
 |R_{\rm ker}|\le |\partial P|+\rho|E_{\rm ker}|
 +\sum_{K\in L0\cup Lsucc}|R(D(K))|.                    \tag{4.5}
\]

Here `D(K)` is the complete guarded-minor/bicycle dependency cone; repeated
seams or resources only decrease the union sizes.  Indeed, a saturation
test uses only seams incident with its residual demanded support, and a
guarded minor or bicycle uses only its stored cone.  Complete footprints
contain every outside conflict resource.  Thus no omitted atom can cover a
demanded row or alter a stored implication.  Equations (4.4)--(4.5) are
finite exact support bounds for this `k=17` launch, not a dimension-uniform
small-interface theorem.

## 5. Canonical stream and launch artifacts

Every textual canonical file uses UTF-8/ASCII, LF line endings, decimal
integers without leading zeroes, tab-separated scalar fields, and comma-
separated lists sorted by the corresponding canonical key.  Empty lists are
written as `-`.  Records are sorted in typed lexicographic order—numeric on
integer components—by their declared key before hashing.  Bytewise sorting
of unpadded decimal packet strings is not the canonical order.

The launch root must contain the following.

1. `inputs.sha256`: relative path, byte length and SHA-256 for `B0`, the raw
   factor, cut-choice table, primitive recut table, `A21`, occurrence/atom
   reconstruction source, zero-265 source and ledger, unconditional-library
   manifest, successor-library manifest, and—if claimed—the `3,664` closure
   manifest.
2. `primitive_recuts.tsv`: `rid,base,old_cut,new_cut`; exactly the sorted
   unique table (1.1).
3. `anchors.tsv`: the 21 primitive keys, their `rid`, family and authenticated
   root-fan dependency record.
4. `implicit_rejections.tsv`: the canonical predicate `S intersect A21 =
   empty`, its unchanged-root-core certificate and the exact count (3.7).
5. `shards.tsv`: disjoint half-open ranges of canonical packet keys.  Shards
   are a scheduling device only; their union must be the full generator and
   their ranges may not overlap.
6. `generation.tsv`: for every emitted packet,
   `packet_key,rid0,rid1,rid2,primary_anchor,anchor_mask,base0,base1,base2`
   plus its canonical final-cut-vector digest.  `anchor_mask` is a
   zero-padded six-hex-digit lowercase mask in the frozen 21-anchor order.
7. `subset_banks.tsv`: one row for every `(packet_key,subset_mask)` with
   `subset_mask=0..7`, its direct cut-vector digest, occurrence digest, atom
   digest, resource-row digest and zero-265 ledger digest.
8. `datum_truth.tsv`: every changed occurrence, atom, role, row, capacity,
   guard or blocker, its eight-bit truth table, full footprint and
   inclusion-minimal activation supports.
9. `zero265.tsv`: the five unsummed final values and the independently
   recomputed row-ledger digest.
10. `footprints.tsv`: every exact `(packet,pivot,footprint)` signature, its
   seam keys, full consumed resources and residual-hypergraph digest.
11. `core_scan.tsv`: one row per
    `(packet,footprint,core,embedding)`, with `CLOSE` and its replayable proof
    or `OPEN_MANIFEST` and its replayable failure of the named stored
    derivation; semantic `OPEN` is reserved for a countermodel or complete
    entailment replay.
12. `rejected.tsv`: packet key, exactly one primary rejection class
    (`ZERO265`, `PERSISTENT_CORE`, `FINAL_CORE`, or `SUCCESSOR_COVER`) and
    the certificate key.  Additional rejection reasons may be listed
    separately.
13. `survivors.tsv`: packet key, final-bank digest, all five zero values,
    one open footprint key, successor-library manifest hash and nonclosure-
    bundle hash, plus the unconditional-library scan hash.  Its status string
    is exactly `LIBRARY_OPEN_NOT_Q1_VERDICT`.
14. `unknown.tsv`: every packet or shard whose reconstruction, embedding
    enumeration, resource calculation or audit did not finish.
15. `generation.audit.json`: the total distinct-base support count, the two
    partition counts (3.3)/(3.7), the three multiplicities (3.5), raw anchor
    proposals,
    incompatible proposals, nonprimary-anchor proposals, emitted canonical
    keys, stage counts and a declaration of the exact move class.
16. `independent.audit.json` and `SHA256SUMS`: the results of Section 6 and
    hashes of every authoritative output.

The mandatory survivor header is

```
packet_key	final_bank_sha256	zero_lower	zero_out	zero_in	zero_orientation	zero_rank10	open_footprint_key	l0_scan_sha256	lsucc_manifest_sha256	nonclosure_bundle_sha256	status
```

The mandatory generation header is

```
packet_key	rid0	rid1	rid2	primary_anchor	anchor_mask	base0	old0	new0	base1	old1	new1	base2	old2	new2	final_cut_vector_sha256
```

No field in either table is a mutable worker/job number.

The full unfiltered stream may be processed shardwise rather than retained
as one file.  In that case `generation.tsv` is a manifest of ordered shard
digests and counts, and the independent verifier regenerates and merge-
compares the canonical key stream.  A commutative checksum alone is not a
no-omission certificate.

## 6. Independent verifier and no-duplicate certificate

The verifier starts from the frozen raw inputs, not from the generator's
derived occurrence or provider tables.  It performs the following checks.

1. Rebuild `q0`, every `C(b)`, the sorted primitive table and `A21`; reject
   duplicate primitive or anchor keys.
2. Independently count all distinct-base triples, split them by intersection
   with `A21`, and verify (3.3)/(3.7).  Enumerate the anchored class in global
   lexicographic order and streaming merge-compare it against the primary-
   anchor generator.  Check strict key order, no repeated key and complete
   shard coverage.  Replay the unchanged root core for the compressed
   no-anchor class.
3. For every emitted key, rebuild (1.4), recover the support from
   `q_S-q0`, and require equality with its three primitive keys.  This is the
   physical no-duplicate check from Theorem 3.1.
4. Rebuild all eight subset banks directly.  Recompute occurrence keys,
   atom keys, complete footprints, truth tables and the final q1 atlas.
   Require uniqueness after canonical atom quotient and check all producer
   provenance lists.
5. Recompute the five zero-265 coordinates from their literal rows.
6. Replay every unconditional final-core status.  Reconstruct every pivot
   footprint and residual hypergraph; replay every stored `CLOSE` proof and
   every `OPEN` nonclosure witness against the exact conditional library and
   embedding manifest.
7. Recompute `rejected.tsv`, `survivors.tsv` and `unknown.tsv` and require an
   exact disjoint partition of the explicit canonical generator.  Together
   with `implicit_rejections.tsv`, require an exact partition of every
   compatible support-three packet in the declared face.

The verifier should be independently implemented.  Shared raw parsers may
be audited separately, but reusing the generator's derived packet, atom or
core-status tables is not an independent replay.

### Theorem 6.1 (launch completeness)

Assume the frozen inputs pass their hashes, the root-fan `A21` theorem and
all library certificates replay, the raw physical catalogues are complete,
and neither generator nor verifier reports `UNKNOWN`.  Then:

1. each compatible radius-three physical support meeting `A21` occurs
   exactly once in the canonical catalogue;
2. every packet in the declared face which is joint-zero-265 and not
   refuted by the successor-core system occurs exactly once in
   `survivors.tsv`; and
3. every packet omitted from `survivors.tsv` is either outside the declared
   face, fails a literal zero-265 row, or has a replayable q1 core
   certificate.

#### Proof

Theorem 3.1 gives statements 1 and the no-duplicate part of 2.  Direct
eight-subbank reconstruction gives all unary, pair and ternary effects, so
the zero-265 and final-provider tests omit no joint compensation.  Theorem
4.1 proves the two semantic rejection classes and identifies their exact
library-open complement.  The independent partition check accounts for
every generated key. \(\square\)

## 7. Fail-closed verdict semantics

Only the following terminal statuses are permitted.

* `REJECT_ZERO265`: literal joint local failure; no q1 claim is needed.
* `REJECT_Q1_CERTIFIED`: an independently replayed persistent-core or
  successor-cover certificate proves q1 infeasibility.
* `LIBRARY_OPEN_NOT_Q1_VERDICT`: all declared prefilters completed and one
  exact footprint remains open relative to `L`; this is the only survivor
  status.
* `OUTSIDE_DECLARED_FACE`: incompatible or wrong move type; no mathematical
  verdict about another move class.
* `UNKNOWN`: hash drift, parser disagreement, missing subset bank, incomplete
  embedding manifest, timeout, resource exit, truncated shard, failed proof
  replay, or generator/verifier disagreement.

An `UNKNOWN` row is never counted as rejected or survivor.  A packet may be
called q1 feasible only after a separate complete q1 witness is rebuilt and
independently replayed; that stage is outside this launch.

No rank-11-or-deeper upper shadow, residence, component topology, opening,
common cap, or compiler claim is made.  The `zero_rank10` coordinate is used
only because it belongs to the frozen zero-265 interface.

## 8. Frozen seed hashes and required prospective manifests

Under `scratch/threadD_k17_round02_anchored_two_recuts_20260802/`, the
present physical seed is:

* `k17_reset_twin_ferrers_bank_ml9_factor_20260801.tsv`:  
  `7c022f4050d6358bc5047532113814fdb46412db0018a0254cc82e056720d8df`;
* `k17_two_cut.candidates.tsv`:  
  `fa1133f5ffc8b70bf7d1713dfa930670508fb6bb6e1255d570f00ea851d00cc6`;
* `round02.bank.tsv`:  
  `48670b1bf5388ed4c8f47a408e4659c145ec26dc3d6a6bb31cd379a1e70ad649`;
* `round02.socket_escape_v2.tsv`:  
  `88893f08ea810662df0ef44be9d227ad53ff19485f27034d8827c6083f6b29ef`;
* `k17_round02_core_piece_recuts_20260801.tsv`:  
  `19164c31bb4a65f5cbe06a872eec9ca2e6def3655fea5ef26c30194cdb73744d`;
* `anchors.tsv`:  
  `eedf932033280d3bef390e49929400ea5612097fbafbf0b6ca78db709b6834c9`;
* `audit.json`:  
  `12ee6bff96d4ab42b0f4c92ef642aedd4b4849f7cdd0632f8b2466d6275ea4df`;
* `clean.tsv`:  
  `9c4ecd1541a945bfae2be6d6534b28543a9c5c87745bdb8a47100dda274fb589`;
* `scratch/threadD_k17_round02_delta_signatures_20260802/audit.json`:  
  `ddcd28ff60094b96426ac617a63b9e93aee0ab7c4e4c3aff0056ab8dc441bae4`.

Before launch D must additionally freeze, as named inputs rather than
working-directory conventions,

1. the exact `3,664` closure manifest if the chronological claim is used;
2. the complete unconditional and successor-library embedding manifests;
3. the occurrence/atom reconstructor and zero-265 replay sources; and
4. the independent verifier source.

Absence or drift of any required manifest is `UNKNOWN`; it may not be
silently replaced by the current working copy.

## 9. Relation to the earlier theorem

This specification instantiates the finite generator of
`MATH_THEOREM_A_K17_RADIUS3_AND_31C8_OCCURRENCE_ANCHOR_GENERATOR_20260802.md`
for the independent-recut face.  Its new content is the exact primary-anchor
canonicalization, the sharp distinct-base support formula, direct eight-bank
reconstruction contract, complete output schemas, independent stream
comparison and fail-closed launch semantics.  It neither supersedes nor
launches the separate atomic `3+1`-`C8` catalogue.
