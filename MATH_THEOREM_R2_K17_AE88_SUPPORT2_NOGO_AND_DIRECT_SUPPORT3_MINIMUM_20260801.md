# `k=17` R2: support-two no-go and support-three minimum for the first common-live gain at `ae88`

Date: 2026-08-01  
Lane: R2 / synchronized common attachment-state matching  
Status: exact scoped minimum theorem with exhaustive support-`<=2` census and
independent support-three replay

## 0. The result

Let `F0` be the rooted flag factor

```text
scratch/laneK_k17_commonfirst_serial_20260801/
  common_serial02_4213_seed20260801.final_rows.tsv
SHA256 ae88fc0b489a5b436ca3c2fe10462d80a18aed6cec8e03df871d5abe96561beb
```

Its loop-free packet matching is `1171`.  Its common both-live root--owner
graph has maximum matching `1141`, deficiency `289`, and canonical Hall shore
`306 -> 17`.  Relative to this exact factor and the complete declared literal
flag menu, define the terminal changed-root support

\[
 \sigma(F)=|\{q:f_q\ne f_q^0\}|.                         \tag{0.1}
\]

The following minimum is now exact.

### Theorem 0.1 (minimum support for the first common-live gain)

Among palette-neutral terminal flag maps whose literal transition geometry
and both-live root--owner incidences are rebuilt simultaneously, the minimum
support for a common matching strictly above `1141` is

\[
                         \boxed{\sigma_{\min}=3}.          \tag{0.2}
\]

More precisely:

1. the identity has common matching `1141`;
2. every one of the `3,449,137` nonidentity terminal maps with
   `1 <= sigma <= 2` has common matching at most `1141`; and
3. the three-root map at roots `81,437,1380` has common matching `1142`.

The support-`<=2` lower bound is a complete finite census, not an inference
from the earlier heuristic selector.  It includes the previously open class
of two distinct-root zero-delta unary moves applied jointly.  The positive
map was independently replayed directly from `F0`; it is not obtained by
retaining the four-root `ae88 -> 2e919` serial packet.

The theorem concerns only the static palette-neutral resource ledger,
literal loop-free transition reconstruction, and the projected common-live
root--owner matching.  It does **not** prove a statewise common transversal,
the `M=1430` max-closure master, connected topology, voltage, upper rows,
opening, residence, source-word chronology, or compiler feasibility.

## 1. Complete terminal support-two normal form

For root `q`, let `f_q^0` be its incumbent flag, let `F_q` be its complete
literal option menu, and write

\[
 \Delta_{qf}=r_q(f)-r_q(f_q^0)                            \tag{1.1}
\]

for the exact type/lower-target resource difference.  The rank-six target
coordinate is shared by its two nested roles, exactly as in the frozen
ledger.  With binary final-flag variables `p_qf` and changed-root variables
`d_q`, the support-bounded palette-neutral master is

\[
 \sum_{f\in F_q}p_{qf}=1,
 \qquad d_q=1-p_{qf_q^0},                                 \tag{1.2}
\]

\[
 \sum_q d_q\le s,
 \qquad
 \sum_{q,f}\Delta_{qf}p_{qf}=0.                          \tag{1.3}
\]

All equalities in (1.3) are coordinatewise.  This final-map formulation is
independent of how a move might be serialized.

### Lemma 1.1 (support-two dichotomy)

Every nonidentity feasible map of support at most two is exactly one of:

1. one zero-delta literal replacement;
2. two zero-delta replacements on distinct roots; or
3. two distinct-root nonzero replacements with opposite deltas.

The three classes are disjoint.

#### Proof

At support one, (1.3) forces the one delta to be zero.  At support two, if
the changed roots are `q,r`, then

\[
                         \Delta_{qf}+\Delta_{rg}=0.        \tag{1.4}
\]

If one delta is zero, so is the other; otherwise they are nonzero opposites.
Distinct roots are forced by the one-hot equations (1.2).  These alternatives
are exhaustive and mutually exclusive.  \(\square\)

Let

\[
 \mathcal U=\{(q,f):f\ne f_q^0,\ \Delta_{qf}=0\}          \tag{1.5}
\]

and let `B` be the canonically ordered set of distinct-root nonzero
opposite-delta pairs.  If `u_q` is the number of members of `U` at root `q`,
the missing synergistic class is

\[
 \mathcal D=\{\{u,v\}\subseteq\mathcal U:
              \operatorname{root}(u)\ne\operatorname{root}(v)\},
 \qquad
 |\mathcal D|={1\over2}\left(|\mathcal U|^2-\sum_qu_q^2\right). \tag{1.6}
\]

For `F0` the exact counts are

| terminal class | count |
|---|---:|
| support-one unary, `U` | 2,545 |
| support-two nonzero opposite-delta, `B` | 215,304 |
| support-two distinct-root unary pairs, `D` | 3,231,288 |
| all nonidentity support-`<=2` maps | **3,449,137** |

Lemma 1.1 proves that this is a complete terminal-map partition.  In
particular, any overlapping or serial sequence whose *final* support is two
is already represented.

## 2. Exact synchronized selector

The liveness layer must be derived from final flags, not from a sum of
per-move edge scores.  Let `Omega` be the complete option-labelled state
universe and `A` the complete option-labelled literal transition universe.
For a literal arc `alpha=(s,t)`, the exact endpoint conjunction is

\[
 c_\alpha=p_{\operatorname{root}(s),f(s)}
           \wedge p_{\operatorname{root}(t),f(t)}.        \tag{2.1}
\]

Define outgoing, incoming, and both-live bits by

\[
 \ell_s^+=\bigvee_{\alpha:\operatorname{tail}\alpha=s}c_\alpha,
 \quad
 \ell_s^-=\bigvee_{\alpha:\operatorname{head}\alpha=s}c_\alpha,
 \quad
 b_s=\ell_s^+\wedge\ell_s^-,                              \tag{2.2}
\]

and the projected incidence bit

\[
 e_{qo}=\bigvee_{s:\operatorname{root}(s)=q,
                       \operatorname{owner}(s)=o}b_s.     \tag{2.3}
\]

Every conjunction and disjunction in (2.1)--(2.3) is imposed in both
directions.  This captures the genuinely synergistic possibility in which
two unary moves provide the missing incoming and outgoing witnesses of one
state.  It also captures changed--changed endpoint interactions and all edge
deletions.

A common attachment-state matching is selected jointly with binary `w_s`:

\[
 w_s\le b_s,
 \qquad
 \sum_{s:\operatorname{root}(s)=q}w_s\le1,
 \qquad
 \sum_{s:\operatorname{owner}(s)=o}w_s\le1,
 \qquad C=\sum_sw_s.                                     \tag{2.4}
\]

For a root set `R`, put

\[
 n_{R,o}=\bigvee_{q\in R}e_{qo}.                         \tag{2.5}
\]

The exact Hall/Benders epigraph is

\[
 \boxed{C+|R|-\sum_on_{R,o}\le1430
                     \qquad(R\subseteq P).}              \tag{2.6}
\]

Thus the first-gain decision `C >= 1142` is feasible exactly when

\[
 \boxed{\sum_on_{R,o}\ge |R|-288
                     \qquad(R\subseteq P).}              \tag{2.7}
\]

For an integral selector incumbent, the network

```text
source -> root q     capacity 1
root q -> owner o    capacity 1431 when e_qo=1
owner o -> sink      capacity 1
```

has minimum cut equal to the final common matching number.  A cut below
`1142` returns an exact violated row (2.7).  This is a proof-safe Benders
separator: the graph is rebuilt from the complete final flag map before the
cut is priced.

For a one-hot finite candidate bank `H`, the equivalent row is

\[
 \sum_{h\in H}|N_{G_h}(R)|z_h\ge |R|-288.                \tag{2.8}
\]

Its coefficient is computed from the whole synchronized terminal map `h`,
never by adding independently measured circuit gains.

## 3. Crossing every old tight shore while charging survival

For an old deficiency-289 shore `R`, define distinct-owner additions and
losses

\[
 A_R=N_G(R)\setminus N_0(R),
 \qquad L_R=N_0(R)\setminus N_G(R).                      \tag{3.1}
\]

The exact old-tight-shore condition is

\[
                  \boxed{|A_R|-|L_R|\ge1.}               \tag{3.2}
\]

One external incidence is not enough if an old neighbourhood owner is lost.
To expose survival inside a binary selector, define

\[
 s_{R,o}=\bigvee_{\substack{q\in R\\(q,o)\in E_0}}e_{qo},
 \qquad
 r_{R,o}=\bigvee_{\substack{q\in R\\(q,o)\notin E_0}}e_{qo},
 \qquad n_{R,o}=s_{R,o}\vee r_{R,o}.                    \tag{3.3}
\]

Then (3.2) is the single simultaneous crossing-and-survival row

\[
 \boxed{
 \sum_{o\notin N_0(R)}r_{R,o}
 -\sum_{o\in N_0(R)}(1-n_{R,o})\ge1.}                   \tag{3.4}
\]

All current tight shores can be separated at once.  Let `C` be the old ae88
DM condensation.  A tight shore is represented by a forward-closed
component family `K` containing every PLUS component and no MINUS component.
Build the weighted closure network

```text
source -> component C       capacity |O_C|, C in PLUS or CORE
component C -> component D  capacity 2861 for every DM implication C -> D
source -> PLUS component    capacity 2861
MINUS component -> sink     capacity 2861
component C(q) -> owner o   capacity 2861 for every final edge (q,o)
owner o -> sink             capacity 1.
```

The value `2861=2*1430+1` exceeds every hard-arc-free cut, whose value is at
most `B+1430=2458`; hence no minimum cut crosses a hard arc.  For ae88,

\[
 B=\sum_{C\in\mathrm{PLUS}\cup\mathrm{CORE}}|O_C|
   =17+1011=1028.                                        \tag{3.5}
\]

If `K` is the source-side component family and `R_K` its root shore, the
finite cut value is

\[
 B-|N_0(R_K)|+|N_G(R_K)|
   =1028+|A_{R_K}|-|L_{R_K}|.                            \tag{3.6}
\]

Consequently

\[
                  \boxed{\operatorname{mincut}\ge1029}  \tag{3.7}
\]

is equivalent to (3.2) for **every** current deficiency-289 shore.  This
closure cut is an exact necessary screen, not a sufficient gain test: an old
deficiency-288 shore can lose an owner and become the new blocker.  The full
Hall separator (2.7) remains authoritative.

The closure network is a formulation theorem, not an executed census
certificate in the present artifacts: SCC membership and the complete DM
condensation were not frozen here.  The finite no-go below instead uses one
sound canonical-shore rejection followed by the stronger full Hall matching
computation for every survivor.

Nor may an exhaustive decision force all edges of one frozen maximum
matching to survive.  Such a restriction would exclude valid rematchings.
For auditing only, fix an old 1,141-edge matching `J0`, let

\[
 q(G)=|J_0\setminus E(G)|,                               \tag{3.8}
\]

and augment from the surviving matching of size `1141-q(G)`.  Define `a(G)`
to be the number of augmentations in a complete augmentation to a maximum
matching, equivalently `a(G)=nu(G)-(1141-q(G))`.  Then

\[
 \nu(G)=1141-q(G)+a(G),
 \qquad
 \nu(G)\ge1142\iff a(G)\ge q(G)+1.                      \tag{3.9}
\]

Thus incumbent-edge losses are charged exactly while replacement and
rematching remain allowed.

## 4. The full state max-closure layer

The common-live matching above is only an outer relaxation.  If `x_s`
selects one option-labelled state at each root and owner and `M` is the
literal transition matching, the exact state recourse remains

\[
 \boxed{M+x(X)-x(\Gamma^+(X))\le1430
                    \qquad(X\subseteq\Omega).}           \tag{4.1}
\]

For fixed `x`, separate (4.1) with

```text
source -> tail state s      capacity x_s
tail s -> head state t      capacity 1431 for every literal arc s -> t
head state t -> sink        capacity x_t.
```

The minimum cut equals the maximum transition matching.  Its source-side
tail family returns the violated row (4.1).  The support census in this note
does not solve this state selector and makes no claim that `M=1430` is
attainable.  Equation (4.1) is frozen here to prevent the projected
root--owner result from being promoted to a common-master solution.

## 5. Exhaustive support-`<=2` decision

The exact census used the partition of Lemma 1.1.  Each candidate was
installed simultaneously into the aggregate flag table; all incident
literal transitions, in/out liveness, both-live states, and projected
root--owner incidences were then rebuilt.

The old canonical `306 -> 17` shore was used only as a sound early rejection:
if its signed owner change `kappa=|A|-|L|` was nonpositive, Hall already
bounded the final matching by `1141`.  Every candidate with `kappa>0`
received a fresh full common matching computation.  No additive edge score,
single-move liveness delta, or frozen matching-survival assumption was used.

Eight deterministic shards produced the following complete transcript.

| class | candidates | canonical `kappa>0` | old matching fully survives | both | common gain |
|---|---:|---:|---:|---:|---:|
| support-one unary | 2,545 | 11 | 547 | 1 | 0 |
| support-two opposite delta | 215,304 | 15,922 | 973 | 39 | 0 |
| support-two unary pair | 3,231,288 | 27,878 | 148,092 | 541 | 0 |
| **total** | **3,449,137** | **43,811** | **149,612** | **581** | **0** |

The number of lost edges from the diagnostic old matching had histogram

```text
lost edges       0       1       2       3       4       5      6     7    8   9  10
candidates  149612  579673  962199  920686  554053  218241  54960  8840  815  57   1
```

The transcript verifier checked candidate IDs `0..3449136` exactly once,
the three class intervals and counts, every identity
`new_head=17+added-lost`, every surviving-matching augmentation identity
(3.9), and zero recorded common gains.  Its aggregate audit is

```text
scratch/r2_k17_ae88_sync_support2_20260801/aggregate.audit.json
SHA256 7be2b0b0164f2eaa236c15f011113e94af3c3864de808798f2085c727eaa1b73
status PASS_COMPLETE_SUPPORT_LE2_TRANSCRIPT_NO_COMMON_GAIN
```

This separate checker verifies transcript coverage and arithmetic; it does
not rebuild all candidate geometries or independently certify a Hall shore
for each recorded full-matching value.  Those literal reconstructions and
exact matching computations are the responsibility of the separately hashed
O3 census engine and are reproducible from its source and complete ledgers.

The eight complete uncompressed ledger hashes and the hashes of their local
compressed copies are bound by the final frozen audit in Section 8.

### Corollary 5.1 (support lower bound)

No palette-neutral terminal map relative to ae88 with `sigma <= 2` raises
the common-live root--owner matching above `1141`.

#### Proof

The identity is the independently calibrated ae88 baseline.  Lemma 1.1
partitions every nonidentity support-`<=2` map into the three exhaustively
enumerated classes.  A candidate rejected by nonpositive canonical `kappa`
retains an explicit deficiency-289 Hall shore.  Every remaining candidate
was evaluated by a fresh exact maximum matching and none exceeded `1141`.
\(\square\)

## 6. Direct primitive support-three witness

The terminal triple is

| root | option ID | exact resource delta |
|---:|---:|---|
| 81 | 155575 | `-2,+6,+86` |
| 437 | 833409 | `-86,+132` |
| 1380 | 2627699 | `+2,-6,-132` |

The three nonzero deltas sum coordinatewise to zero.  Because no singleton
delta is zero, no proper nonempty subfamily sums to zero; the circuit is
primitive.

Applied directly to ae88, it gives

```text
final rows SHA256 18d628112278df5b80fa852fe1694738a1e610eff820e06de3e87cc664e17c7a
packet matching                     1171 -> 1172
common matching                     1141 -> 1142
common deficiency                    289 -> 288
final common Hall shore                   305 -> 17
old 306-root shore head                17 -> 18
old-shore added owners                    {246}
old-shore lost owners                         {}
lost edges of diagnostic old matching          0
```

An independent literal verifier checked the baseline and final byte hashes,
all changed rows and option IDs, the complete lower resource ledger, the
three nonzero deltas and their zero sum, every loop-free transition, packet
and common matching values, the old-shore owner accounting, and an explicit
1,142-edge common matching:

```text
scratch/r2_k17_ae88_sync_support2_20260801/
  direct_support3.independent.audit.json
    SHA256 2e8aaaba423a4b52e8f9fe02edd3424500c73d1ada199b795e50b2203cabf231
  direct_support3.matching.tsv
    SHA256 40a98a50ea10c05bc733c68d6ee87aeab9333d1331e004a2ff83d7d47c571494
  direct_support3.steps.tsv
    SHA256 042b3d59c8e8e3745fc9ab1f888e828684072acb6d3ab8c09d445a8348fa5468
```

The audit status is `PASS_AE88_DIRECT_PRIMITIVE3_COMMON_GAIN`.  Corollary
5.1 supplies the lower bound and this witness supplies the upper bound,
proving Theorem 0.1.

## 7. Relation to the authenticated `4f5` serial rebase

The same three terminal rows were first found in the authenticated
`2e919 -> 4f5` overlapping-support-two commutator shell.  The intervening
`ae88 -> 2e919` packet changes roots `52,184,1090,1263`, disjoint from
`81,437,1380`.  Stable root/option IDs and the resource ledger therefore
allow the three terminal rows to be transported, but liveness, matching, and
Hall cuts do not transport and were rebuilt from ae88.

The direct final SHA `18d628...` is not `4f5fb7...`: it intentionally omits
the four serial roots.  No `2e919` or `4f5` support-three catalogue was
re-enumerated here.  The old `19,141,938`-triple `C_ov(2e919)` census serves
only as authenticated provenance for the candidate; the new theorem rests on
the direct ae88 literal replay.

## 8. Execution and frozen boundary

All finite enumeration ran as `g++ -O3 -std=c++20 -DNDEBUG` CPU work on
`h100` through `ssh -o ClearAllForwardings=yes`, in the unique directory

```text
/home/amodo/or15/work/r2_k17_ae88_sync_support2_20260801_019f8128_r2
```

No heavy local enumeration or Python was used.  The principal source and
remote binary hashes are

| artifact | SHA-256 |
|---|---|
| support-`<=2` census source | `312eb2d19a62142f94cfdf8a20f4044314ac33658937973b8787d04a2cb8e17c` |
| census dependency | `05c5e077ae904c0a6ba46cf258790780165f078a0f140b95ee9553d04a92d6fb` |
| remote census binary | `d99dc2a44a73bffebf45f116010ae0bd6b856e3b9795c6fe8b5d968c81635049` |
| transcript verifier source | `01027214834706d73dd83154a60bd125becf29404de9b851a74b4162d98d8ec7` |
| remote transcript verifier binary | `ce8cfb559daceb4eb0e2db18ffd091046d51e6b17970b193c23f07314e2885fb` |
| direct support-three verifier source | `023bd131f4750b50d3b46e1646b71db64480d29df55501075b32b84019be0eb0` |
| direct verifier dependency | `0d0f68bc3524579b940f8797a7dacc2dd531d7417f132c92ffbf09ee906e7d23` |
| remote direct verifier binary | `e21727ab7edafff4dfe41edb55b19ed59fb220b0c448c0ce7bd3da0eba89a618` |

The machine-readable freeze is

```text
scratch/r2_k17_ae88_sync_support2_20260801/frozen_scope.audit.json
```

It binds the theorem, exact scope, source and binary hashes, all eight shard
audits, all eight complete transcript ledger hashes, compressed replay
copies, the aggregate audit, the direct final rows, steps, matching, and
independent audit.

Even the achieved common matching `1142` leaves deficiency `288`.  It does
not select compatible states or satisfy (4.1), and it carries no conclusion
about topology, voltage, upper rows, opening, residence, or the compiler.
