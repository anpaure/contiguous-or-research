# Audit of the $K=16$, length-$12873$, $4/9/4$ phase-fusion collar

Date: 2026-07-30  
Lane: R  
Status: exact encoding proved; generated instance authenticated; bounded solve ended `UNKNOWN`

## 1. Exact scope

Let $W=(w_0,\ldots,w_{12872})$ be

`scratch/k16_upper12874_best_delete.word`,

with SHA-256

`a72cc9e0ba87dabf1005ce750ffd738e7eeef92599a0d8f9dfe80b26f458a649`.

It is obtained by deleting zero-based position $1$, whose value is
`0x2800`, from the independently verified certificate
`answers/k16_upper12874.word` (SHA-256
`631e78e5e466423a6c53dbdd31c2157c006bb286f8c8534e2cddf50e751df75e`).

An independent suffix-OR recurrence gives

* length $12873$;
* every cell in \(\{1,\ldots,65535\}\);
* maximum live suffix-state count $11$;
* unique missing target $11373=\mathtt{0x2c6d}$.

The editable set is

\[
P=\{0,1,2,3\}\cup\{6435,\ldots,6443\}
  \cup\{12869,\ldots,12872\}.
\]

Thus the collar has phase sizes $4/9/4$, contains $17$ arbitrary
nonzero cells, and freezes the other $12856$ cells.  There is no Hamming
budget and no restriction on a new editable value except
$1\leq w'_p\leq65535$.  Every conclusion below is confined to this one
source and this one editable set; it is not a statement about all
length-$12873$ words or all collars of these sizes.

## 2. Exact interval normal form

Write the positions in increasing order as
$p_0<\cdots<p_{s-1}$, where $s=17$.  Removing them partitions the word
into fixed runs.  For $0\leq i\leq j<s$, define a pattern

\[
(i,j,F),
\]

where $F$ is the OR of:

1. a suffix (possibly empty) of the fixed run immediately before $p_i$;
2. every complete fixed gap between $p_i,p_{i+1},\ldots,p_j$; and
3. a prefix (possibly empty) of the fixed run immediately after $p_j$.

Patterns with the same triple $(i,j,F)$ are identified.

### Theorem 2.1 (fixed-run/consecutive-edit normal form)

For every assignment of nonzero masks to the editable cells, the set of
literal contiguous-interval ORs is exactly the union of:

* the interval ORs wholly contained in a fixed run; and
* the values

\[
F\mathbin\vee y_i\mathbin\vee y_{i+1}\mathbin\vee\cdots
 \mathbin\vee y_j
\tag{2.1}
\]

over all catalogue patterns $(i,j,F)$.

#### Proof

An interval avoiding $P$ lies wholly in one connected component of the
complement of $P$, hence wholly in one fixed run.

Otherwise, let $p_i$ and $p_j$ be its first and last editable
positions.  Contiguity forces it to contain every editable position
$p_i,p_{i+1},\ldots,p_j$, so its editable indices form a consecutive
block.  Its fixed cells are exactly a suffix of the run before $p_i$,
all complete intervening gaps, and a prefix of the run after $p_j$.
Its OR is therefore (2.1).

Conversely, choose endpoints realizing the selected suffix and prefix.
The interval between them contains precisely the indicated editable block
and fixed pieces, and hence realizes (2.1).  Collapsing equal suffix ORs,
prefix ORs, or final triples loses no attainable OR value.  This proves
both inclusions.  \(\square\)

The implementation in
`scratch/solve_ad_k16_12874_append_template_exact_20260730.py` realizes
this normal form in `fixed_run_coverage`, `suffix_ors`, `prefix_ors`, and
`changed_patterns`.  Empty fixed runs are handled by the explicit zero OR.

## 3. CNF equivalence

For each editable cell $p_i$ and coordinate $b\in\{0,\ldots,15\}$,
let $x_{i,b}$ be its bit.  The clause

\[
\bigvee_{b=0}^{15}x_{i,b}
\]

is exactly the nonzero-cell condition.

Targets already realized inside fixed runs require no clause.  For every
remaining target $T$ and every pattern $(i,j,F)$ with
$F\mathbin\&\neg T=0$, introduce a witness $z_{T,i,j,F}$.  Conditional
on this witness:

* if bit $b$ belongs to $T\setminus F$, require at least one of
  $x_{i,b},\ldots,x_{j,b}$;
* if bit $b\notin T$, require every one of
  $x_{i,b},\ldots,x_{j,b}$ to be zero.

Finally, require at least one witness for each residual target.

### Theorem 3.1 (CNF iff theorem)

The emitted CNF is satisfiable if and only if some assignment of nonzero
masks to the $17$ cells of $P$, with all other cells frozen, is a
universal length-$12873$ contiguous-OR word.

#### Proof

For a fixed witness, the conditional clauses say coordinate by coordinate
that

\[
F\vee y_i\vee\cdots\vee y_j=T.
\]

They are necessary and sufficient: every missing one-bit of $T\setminus F$
must be supplied by an editable cell, while a zero-bit of $T$ must occur
in none of them.  The target ALO clause selects one such equality witness.
By Theorem 2.1, this is equivalent to realizing $T$ by a literal interval.
Fixed-run targets persist under every assignment.  The cell ALO clauses
are equivalent to nonzero editable masks.  Applying these observations to
all targets gives both implications.  \(\square\)

This proof also shows that witness variables need only imply their pattern
constraints; the reverse implication is unnecessary.

## 4. Authenticated generated instance

The audited sources are:

* emitter
  `scratch/build_ad_k16_12873_phase_fusion_cnf_20260730.py`, SHA-256
  `a653e47a56307b3f648bfd98cf4471f8b46dbe944cb63ac071cf728523a292e6`;
* interval core
  `scratch/solve_ad_k16_12874_append_template_exact_20260730.py`, SHA-256
  `820bc726f4a9edafb69081e36f24712a0dfe2196ea33271bc661d690056b0cfb`;
* CNF core
  `scratch/build_ad_k16_12874_append_template_cnf_20260730.py`, SHA-256
  `2a2ffca7a27511e32ab4539e8ad0e34417ccba2da805bc00f406bf5ca0af7be0`.

The generated files copied from the H100 job are:

* `scratch/ad_k16_12873_phase_fusion_4_9_4.cnf`, SHA-256
  `206581940afea13d9be331cf4d44f028dda9f79c7ffc705dea3dd2a1c928cf80`;
* `scratch/ad_k16_12873_phase_fusion_4_9_4.cnf.map.json`, SHA-256
  `eb6f43d2b1a1b4838a6c5553840936a497abb8b4e57bccac8da6291bac378ac5`.

The map payload hash independently recomputes to

`31fa0be6295651058e4bc9e8057fbe868c97c0edd630d29423440996f9493b46`.

Direct recomputation from the source word and editable set gives:

* $461$ distinct interval patterns;
* $57$ targets not already covered within fixed runs;
* $272=17\cdot16$ bit variables;
* $4467$ witness variables;
* $4739$ variables total;
* $17$ cell ALO clauses;
* $57$ target ALO clauses;
* $33300$ positive-bit witness clauses;
* $112330$ zero-bit witness clauses;
* $145704$ clauses total.

The CNF header is `p cnf 4739 145704`; the file has exactly $145704$
terminated clause rows and maximum variable index $4739$.  Thus both the
map arithmetic and the physical DIMACS dimensions agree independently.
The map's ordered residual-target list, all $57$ witness counts, and the
contiguous witness-variable ranges also agree exactly with a fresh catalogue
reconstruction.

The independent checker
`scratch/audit_r_k16_12873_phase_fusion_cnf_20260730.py`, SHA-256
`078fb180b3fb7d08c008116e77e7a93f8e57507e6f0acc7f71d7c77b027c1f86`,
does not import either construction module.  It reimplements the interval
catalogue, replays the source, and compares the complete ordered DIMACS clause
stream.  It returned
`PASS_EXACT_CLAUSE_STREAM_AND_SOURCE_REPLAY`.  Its ledger is
`scratch/r_k16_12873_phase_fusion_cnf_independent_20260730.audit.json`,
SHA-256
`5101d32deb9998397e986363b7cc87344410a6bc7ba39ba8cb7be35a497a3e56`,
with payload SHA-256
`a1a75724a710a7bcb1087e811154698275eab1401dfecc5dbdb8f521ed63f0e2`.

## 5. SAT decoder audit

The decoder is
`scratch/decode_verify_ad_k16_12873_phase_fusion_cnf_20260730.py`, SHA-256
`5da1ba581d8194c11cea8bd46564606d34c9a395ea1f473ed89ee3903ca1ad3f`.
It pins the source and emitter hashes, checks the CNF against the map,
requires a SAT status and a complete assignment, decodes the $272$ bit
variables, rejects zero cells, and performs a fresh all-target suffix-OR
replay before writing a candidate.

Consequently, decoder acceptance is a sound positive certificate even
without trusting the witness-variable assignment.  A minor robustness
limitation is that the decoder does not independently recompute the map's
`payload_sha256`; this cannot create a false positive because the final
literal replay is decisive, but a damaged map could cause a false negative
or decode failure.  An independent final replay remains mandatory.

## 6. Monitored solver result: strict `UNKNOWN`

The sole monitored job was the pre-existing H100 CaDiCaL process in

`/home/amodo/or15/work/ad_k16_12873_phase_fusion_20260730`.  It used
CaDiCaL 3.0.1, binary SHA-256
`49c86c5f8447d768906dcd12d62fb4752e80a48a0d52bbc633929f32eec00b3d`,
under a $1260$-second wrapper timeout on one H100 CPU core.

No duplicate solver was launched by this audit.  The monitored process ended
with wrapper exit status $124$.  Both stdout and stderr are empty.  The
retained status files are:

* `scratch/ad_k16_12873_phase_fusion_4_9_4.cadical.exit`, four bytes,
  SHA-256
  `ca2ebdf97d7469496b1f4b78958f9dc8447efdcb623953fee7b6996b762f6fff`;
* `scratch/ad_k16_12873_phase_fusion_4_9_4.cadical.out`, empty;
* `scratch/ad_k16_12873_phase_fusion_4_9_4.cadical.err`, empty.

The interrupted run left a $1,662,013,440$-byte partial DRAT stream.  It is
not a complete proof, was not copied into the local certificate bundle, and
must not be checked or promoted as an UNSAT certificate.  There is likewise
no SAT assignment to decode.  The mathematically correct verdict is exactly
`UNKNOWN`.

For any later run, SAT may be promoted only after decoding and an independent
literal replay of all $65535$ nonzero targets.  An UNSAT solver line alone is
not a theorem: negative promotion requires a complete proof artifact and an
independently successful proof check.

## 7. Exact boundary

What is proved now is the correctness and exact scope of the finite
$4/9/4$ model and the authenticity of its generated CNF.  The bounded solve
does not decide feasibility.  The existence of a universal word on this
collar remains open.

## 8. Related $5/9/4$ monitors (not part of Theorems 2.1--3.1)

The related $5/9/4$ collar adds editable position $4$, so it has $18$
editable cells.  Its status must not be conflated with the $17$-cell
$4/9/4$ result above.

One dynamic model bundle was copied to
`scratch/root_k16_optimal_collar594_20260730.remote/`.  Its CNF has SHA-256
`9e7aa9728f6c9b7eab577856573f23c70a101770b0e42a56cf3b15a3a6670c04`,
$4576$ variables, and $139669$ clauses.  Its map has SHA-256
`3e143de530a16364f0af063797baf455c4daef6c9c69329f85cd2489f49bf7bb`.
The CaDiCaL output is exactly `c UNKNOWN` and the Kissat streams are empty.
The CaDiCaL output file has SHA-256
`8fba55cea0f98be36fab7b65349dda867a58aabfcf974a46098f5123830ac5cb`.
This bundle has no mathematical feasibility verdict.

A second direct model was copied as
`scratch/ad_k16_12873_delete_collar594_direct.cnf` and
`scratch/ad_k16_12873_delete_collar594_direct.map.json`, with respective
SHA-256 hashes
`bf70a573d2b5ecb0d21ea871e49d0535de83e92d43f30aed127fefc7cee662c1`
and
`73833bf57f52dfa66ad709b1b78c2d8ef09ccc625dfe0b388b24db5fcb7692e7`.
It has $5429$ variables and $169755$ clauses.  Its CaDiCaL seed-11
stream ends `c UNKNOWN` after SIGTERM; its Kissat seed-103 streams are
empty.  The CaDiCaL stream was copied as
`scratch/ad_k16_12873_delete_collar594_direct.seed11.out`, SHA-256
`5086810d8ebe8a84963527cb3cef3a498f23e53af2a2cff69e4e10bc6ef96bee`.
These runs are also strictly `UNKNOWN`.

The third monitored closure-normal-form CNF is
`scratch/ad_k16_deletep1_collar594_closure.model.cnf`, SHA-256
`cc73d7bf680d2698fd05f34bee74e1eb10427c95d2323013b4f8d5e387b948f2`,
with map SHA-256
`b557c13272198a2338ce1f0718c24a0a1692cd8c8e3b40b2071a125402b3c55a`.
It has $5338$ variables, $76653$ clauses, and $226792$ literals.  A
fresh local run of the independent checker reproduced the complete DIMACS
clause multiset and payload
`6459146484d1494413a8aeed6a69796f5fafe3a518f90bbed89b97c8228ce05e`.
The pre-existing proof-producing Kissat run reached its original
$1800$-second cap and ended with wrapper exit status $124$.  It emitted no
SAT or UNSAT line; stdout ends only with SIGTERM and stderr is empty.  The
small terminal files are:

* `scratch/ad_k16_deletep1_collar594_closure.solve.exit`, SHA-256
  `ca2ebdf97d7469496b1f4b78958f9dc8447efdcb623953fee7b6996b762f6fff`;
* `scratch/ad_k16_deletep1_collar594_closure.solve.stdout`, SHA-256
  `6093b8cc46b6988bafb4710d3363307cca33a18ea45f503ef806bc993adeb303`;
* `scratch/ad_k16_deletep1_collar594_closure.solve.stderr`, empty;
* `scratch/ad_k16_deletep1_collar594_closure.solve.resource`, SHA-256
  `97f19a91762025d2c8af36274ed0f746bdb347aa9c482a113be107ab53d7e40a`.

The resource ledger reports $30{:}00.01$ wall time and $115992$ KiB peak
RSS.  The interrupted binary DRAT stream is $2,251,292,672$ bytes, is not a
proof, and was deliberately not copied.  Hence this final related run is also
strictly `UNKNOWN`.
