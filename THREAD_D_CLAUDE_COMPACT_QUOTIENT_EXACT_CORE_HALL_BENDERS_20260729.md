# Claude compact quotient to exact core/Hall Benders integration

Date: 2026-07-29

Status: fail-closed adapter, exact cyclic equivariant one-core/matching
subproblem, implemented whole-selector logic-Benders interface, a guarded
schema hook for the stronger decorated-shore rows, positive current-source
`k=11` calibration, and bounded `k=15` H100 smoke. No new `k=15` carrier or
word is claimed.

Authoritative implementation:

~~~text
scratch/threadD_claude_exact_benders_adapter.py
~~~

Solver-free regressions:

~~~text
scratch/test_threadD_claude_exact_benders_adapter.py
~~~

## 1. Outcome

Claude's current compact quotient source is now connected to the repository
compiler through a trust boundary with four stages:

~~~text
frozen cpsat.py choice table
    -> independently normalized explicit owner selector/cycle
    -> exact all-one-core plus physical matching subproblem
    -> weighted quotient Hall replay and independent word verification.
~~~

The source is pinned to SHA-256

~~~text
fed3719c52fa211af63941a842dd37ad2c3dd3b4556e473b23372f82919726f0.
~~~

Bare foreign IDs are rejected unless the JSON itself also pins this source
hash and the exact repository choice-table hash. These digest fields pin the
ID-table interpretation; they do not prove which program generated the IDs.
Explicit geometric triples can be audited without generator provenance, but
the output then says that the source is only the mapping source, not the
generator. Any supplied digest is checked even on an explicit-triple input.

The exact subproblem does not use the `ready15.py` forced-port mask and does
not sample cores. It quantifies over every cyclic equivariant one-core and
every physical target-to-position matching. Only a conclusive all-core
failure emits a compiler Benders cut.

## 2. Foreign schema and catalogue audit

The current Claude program writes raw selections as

~~~json
{"k": 11, "sel": [/* bare integer IDs */]}
~~~

with optional diagnostic fields. It does not serialize the directed arc
orientation, physical cycle, voltage, source digest, or table digest.
Consequently a raw historical file cannot be attributed to the current
source merely because today's table still decodes it.

For odd `k`, the adapter independently regenerates Claude's ordered
no-self-loop table

\[
  (\ell,a,b),\qquad
  \ell\in [N],\quad a<b,\quad
  \rho(\,L_\ell\cup\{a\}\,)\ne
  \rho(\,L_\ell\cup\{b\}\,),
\tag{2.1}
\]

and compares it entry by entry with `QuotientCatalogue`. The relevant exact
counts and repository table hashes are

| k | choices | directed arcs | table SHA-256 |
|---:|---:|---:|---|
| 11 | 625 | 1,250 | `74ab216905b70964...` |
| 15 | 11,998 | 23,996 | `8d09676a3c073c5b...` |

No ID is skipped. An input must contain exactly `N` distinct in-range
choices, one at every lower owner.

The Claude ordered-table digest hashes `[lower_index,a,b]`; the repository
choice-table digest hashes `[lower_mask,a,b]`. Both encodings and both
digests are named explicitly in every new normalized artifact.

### Explicit cycle checks

If a physical cycle is supplied, the adapter requires:

1. exactly `W` distinct rank-`r` masks;
2. a Johnson edge at every cyclic adjacency;
3. each edge belonging to the selected choice set;
4. each selected edge orbit occurring exactly `k` times;
5. one consistent directed quotient arc for all phases of each choice;
6. equivalence to the independently reconstructed factor cycle up to rotation
   and reversal; and
7. an exactly recomputed unit voltage matching any claimed oriented voltage.

If no cycle is supplied, the repository reconstructs one and labels its
orientation as reconstructed. It never pretends that Claude's lost directed
orientation was recovered.

If both `cycle` and `physical_cycle` aliases occur, they must be literally
equal. This deliberately rejects even reversal-equivalent ambiguous payloads.

Duplicate JSON keys, unknown top-level fields, malformed types, noncanonical
or quotient-loop choices, missing owners, and asserted shadow diagnostics
which disagree with the repository audit all fail closed.

## 3. Carrier gate used before Hall

Let `T=(T_i)` be the reconstructed strict spiral and let `d=d(k)`. The
cyclic maximal erosion is

\[
       P_i=\bigcap_{a=0}^{d}T_{i-a},\qquad D^dP=T.       \tag{3.1}
\]

The adapter requires:

* exact depth-`d` residence;
* every required cyclic lower row of depths `2,\ldots,d-1`; and
* unrestricted upper coverage at every depth.

At `d=3` this requires lower q2, but lower q3 remains a compiler/Hall
condition. Rank-`h=r-d` targets are literal target vertices. If one is
absent from `P`, it has zero Hall degree and the exact subproblem rejects it.
This is the correct treatment of Claude's q3 diagnostic.

The normalized status

~~~text
CARRIER_AUDITED_COMPILER_PENDING
~~~

means only that these carrier gates pass. It does not claim a one-core,
Hall matching, safe cut, or word.

## 4. Exact cyclic equivariant one-core model

Assume

\[
     T_{i+N}=\rho^vT_i,\qquad \gcd(v,k)=1.               \tag{4.1}
\]

Let `u_b` mean that coordinate zero is omitted from the core at base
position `b`. For the support bits

\[
     p_b={\bf1}_{0\in P_b},
\]

the complete one-core constraints are

\[
 u_b=0\quad(p_b=0),                                     \tag{4.2}
\]

\[
 u_b+u_{b+1}\le1\quad(p_b=p_{b+1}=1),                  \tag{4.3}
\]

and if exactly one of `p_b,p_{b+1}` is one, the corresponding omission is
zero. These are precisely the coordinate-zero equations `DC=DP`.

Equivariance transports coordinate `x` at physical position `i` to

\[
       b(i,x)=i-Nxv^{-1}\pmod W.                         \tag{4.4}
\]

Thus

\[
 x\in C_i
 \quad\Longleftrightarrow\quad
 x\in P_i\ \hbox{and}\ u_{b(i,x)}=0.                    \tag{4.5}
\]

For every nonempty target `S` with `|S|\le h` and every position `i` with
`S\subseteq P_i`, introduce `f_{S,i}`. The exact assignment equations are

\[
 \sum_i f_{S,i}=1,\qquad
 \sum_S f_{S,i}\le1,                                    \tag{4.6}
\]

and

\[
 f_{S,i}=1
 \quad\Longrightarrow\quad
 u_{b(i,x)}=1
 \quad(x\in P_i\setminus S).                            \tag{4.7}
\]

### Theorem 4.1 (exact all-core equivalence)

The integral solutions of (4.2)--(4.7) are exactly the pairs consisting of
an equivariant cyclic one-core `C\subseteq P` with `DC=DP` and a physical
matching saturating every target of rank at most `h`.

#### Proof

Equations (4.2)--(4.3) are the vertex-cover equations for coordinate zero's
support. Equation (4.4) transports that one trace through the unit-voltage
action, so (4.5) gives every coordinate trace and preserves `DC=DP`.
Equations (4.6) are an injective target assignment. Given
`S\subseteq P_i`, (4.7) is equivalent to omitting every core coordinate
outside `S`, hence `C_i\subseteq S\subseteq P_i`. This proves both
directions. QED.

The model contains no `ready15` mask. In particular, it does not replace
`C` by the forced endpoint set
`(P_i\setminus P_{i-1})\cup(P_i\setminus P_{i+1})`.

The implementation records a canonical text-proto hash and all rebuild
parameters. An `EXACT_CORE_HALL_INFEASIBLE` result is an OR-Tools audit of
this exact model, not a DRAT-style independently checked proof payload; the
mathematical equivalence above is what fixes its scope.

## 5. Weighted quotient Hall and physical lift

Before the exact core solve, the adapter computes the core-free envelope
graph

\[
       S\sim i\quad\Longleftrightarrow\quad S\subseteq P_i. \tag{5.1}
\]

Every genuine core graph is a subgraph of (5.1). Hence weighted quotient
Hall failure in (5.1) is an exact all-core obstruction, although passing it
is only a relaxation.

After (4.2)--(4.7) succeeds, the adapter reconstructs the literal core and
the physical graph

\[
       S\sim i\quad\Longleftrightarrow\quad
       C_i\subseteq S\subseteq P_i.                      \tag{5.2}
\]

It then independently reruns weighted quotient Hall:

\[
  \sum_{O\in X}|O|\le k\,|N_{\rm quot}(X)|
  \quad\hbox{for every target-orbit shore }X.            \tag{5.3}
\]

The quotient flow is followed by a new ordinary physical maximum matching.
The emitted word is not trusted from the CP-SAT assignment.

This is the cyclic theorem: it has `W` physical matching positions. The
final `d` letters are duplicates appended only after a safe opening is
chosen. They are not credited as `W+d` independent cyclic capacity. The
linear opening-dependent Hall model from the preceding Task-D postprocessor
is a different, broader architecture and is not conflated with (5.3).

## 6. Physical word emission

For a passing core and matching put

\[
 A_i=S\quad\hbox{at a matched position},\qquad
 A_i=P_i\quad\hbox{otherwise}.                          \tag{6.1}
\]

Then `C\subseteq A\subseteq P`, and consequently

\[
              DA=DP,\qquad D^dA=T.                      \tag{6.2}
\]

The adapter enumerates every upper-safe cut. At cut `c` it rotates the
cyclic `W`-letter word and appends its first `d` letters, producing length
`W+d`. Before writing, it checks that the linear `D^d` row equals the exact
oriented carrier at that cut and directly enumerates all interval ORs.
Finally, `scratch/verify_exact_or_word.py` independently checks every
nonempty mask and the exact middle row.

Only this last path may return

~~~text
VERIFIED_OPTIMAL.
~~~

## 7. Implemented selector Benders and the decorated-shore hook

Let `F` be the complete incumbent set of `N` Claude choice IDs. Suppose one
of the following exact fixed-selector failures occurs:

1. the independent carrier gate fails;
2. the core-free envelope Hall graph fails;
3. the all-core model (4.2)--(4.7) is `INFEASIBLE`; or
4. the carrier has no upper-safe opening in the stated graded architecture.

Then the adapter emits

\[
             \boxed{\ \sum_{e\in F}x_e\le N-1.\ }       \tag{7.1}
\]

### Theorem 7.1 (scope of the selector no-good)

Equation (7.1) is valid for Claude's frozen no-self-loop selector master in
the failure architecture printed with the cut.

#### Proof

A connected undirected two-factor has only cyclic rotations and reversal as
physical traversals. Residence, lower/upper interval support, existence of
an equivariant one-core and physical matching, and existence of a safe cut
are invariant under these operations. The exact failures above therefore
reject every direction assigned to the same complete undirected selector.
Claude's owner equations choose exactly `N` choices, so (7.1) excludes
precisely that selector. QED.

The JSON cut includes

~~~json
["nogood", [/* the N frozen Claude IDs */]]
~~~

and can be appended directly to Claude's `lazy` list. It also contains the
source/table hashes, selected-ID hash, inequality, failure status, and scope.

No cut is emitted for:

* `UNKNOWN` or a timed feasible incumbent;
* failure of one sampled core;
* a fixed-core Hall shore before all cores are quantified;
* an unpinned ID file; or
* Claude `PASS`/`FULLPASS` text without repository replay.

This whole-selector cut is deliberately weaker than a reified
history-signature Hall cut, but it is unconditional and immediately
consumable by the current compact master.

### 7.2 Stronger additive row: interface contract only

`MATH_THEOREM_COMPILER_READY_DECORATED_PAIR_ROOT_ARC_CEGAR_20260729.md`
proves the sharper row

\[
 \sum_{j,Z}g_j^X(Z)y_{j,\mathcal C,Z}\ge
 \left\lceil {\sum_{O\in X}w(O)\over k}\right\rceil,       \tag{7.2}
\]

where `X` is a deficient target-orbit shore, `Z` is one of the 8/16 legal
omission states, and `y` is an exact combined six-middle-state/five-directed-
arc collar and omission-state literal. This cuts every guarded collar/state
configuration with the same deficient shore, not just one selector.

The adapter now publishes the machine-readable hook

~~~text
threadD-claude-shore-state-additive-cut-v1
kind: linear_ge
projection_level: carrier-collar+omission-state
status: SHORE_CUT_INTERFACE_ONLY_NOT_INSTALLED.
~~~

This is a schema/interface contract, not a row materializer or verifier. Its
manifest requires explicit orbit weights and `b(X)`, explicit omission
masks rather than opaque indices, a complete collar/state literal registry,
one-hot and stable-transition constraints including the twisted seam, exact
literal equivalences, and hashes of the catalogue, registry, coefficients,
shore, envelope, state cycle, neighborhood, and flow.

This stronger row is **not implemented in Claude's live master**. The current
`QModel` exposes undirected choice literals and choice-level lazy clauses, but
not the required directed-collar/core-state literals or an inner Hall oracle
returning an incumbent omission cycle. Projecting (7.2) directly onto choice
IDs would be unsound. Accordingly the only installed negative row in this
iteration is `EXACT_SELECTOR_NOGOOD`; the additive schema has no
`claude_lazy` field.

## 8. Current-source `k=11` calibration

The current source `fed3719c...` was loaded on H100 CPU and its live
`QModel` table was compared entry by entry with the adapter. The positive
run used the independently validated explicit carrier only as a branching
hint; the live current-source model re-solved the undirected selection in
0.440 seconds. Its `solve()` API does not return directed arc variables.
The repository therefore reconstructed and independently audited the
orientation (unit voltage 6); this is not a claim that the solver recovered
the explicit hint's reverse, voltage-5 orientation, nor that the older
schema-less fixture was originally generated by this source.

The exact core/Hall subproblem then had

~~~text
462 omission variables
3,234 physical assignment variables
3,696 total variables
5,355 constraints
0.074 solver seconds.
~~~

Both envelope and actual-core weighted Hall were

~~~text
231 / 231.
~~~

The final word has length 465 and SHA-256

~~~text
0b526c51062dc7d352a8074708d940cf727dc4f945c019756d9b04d7ed5716e6.
~~~

The H100 verifier and a second local invocation both report

~~~text
covered masks       2047 / 2047
middle row exact    true
status              VERIFIED_OPTIMAL.
~~~

The retained audit explicitly records the hint's historical/provenance role
and the fresh live selector hash. It does not claim a novel selector.

## 9. Exact Hall-failure/Benders calibration

To exercise the negative interface, the historical q3-skip ID list was used
only as an untrusted branching hint. The exact 42 IDs are retained inside
the audit as well as in `scratch/cpsat_k11_rnd1.json`; the live current-source
model re-solved that selector in 0.444 seconds. The independent carrier gate
passed, but the core-free envelope Hall graph gave

~~~text
flow / demand             220 / 231
physical deficiency       11
deficient target orbit    81
deficient position blocks 0.
~~~

Therefore no one-core can repair this carrier. The emitted exact cut is

\[
       \sum_{e\in F}x_e\le41,
\]

with cut hash

~~~text
0b92ec15d17d25e5f26c73bf6d8d3a0dd71a2dc411f832dcde4fbcba5dd0e509.
~~~

This digest is recomputed after the `source_round` annotation and exactly
matches the stored cut with only the digest field removed. The artifact also
retains the normalized explicit choice triples and records

~~~text
failure_status                 ENVELOPE_HALL_INFEASIBLE
ready15_forced_ports_used      false.
~~~

The one-round driver terminates as `MAX_ROUNDS` after storing the cut. That
status is not an infeasibility claim; only the stored selector no-good is a
proved conclusion.

## 10. Bounded `k=15` H100 smoke

The current compact source constructed the exact `k=15` master with

~~~text
W=6435, N=429, choices=11998, directed arcs=23996.
~~~

With one round, eight CPU workers, and a ten-second solver cap, it returned

~~~text
Claude solve status    UNKNOWN
solver time            10.477 s
total wall time        14.607 s.
~~~

No selector was returned. Consequently the core/Hall subproblem was not
started, no Benders cut was emitted, and no word exists from this run. This
is only a bounded construction/runtime smoke.

## 11. Artifacts

~~~text
5eaf8f2412fd5054d66382e6c16dd6de0bb35087c101f89522ea2ee8a2034e23  scratch/threadD_claude_exact_benders_adapter.py
fc02ed9b1b185bc45d2b1f3de5b862d516f54807473421b8da8d5df941059d03  scratch/test_threadD_claude_exact_benders_adapter.py
fed3719c52fa211af63941a842dd37ad2c3dd3b4556e473b23372f82919726f0  scratch/threadD_claude_cpsat_fed3719c.py
040e1b739c6a21163b14a3a0e9255a806ada3b41d87ac54ead835998f63d25c7  scratch/k11_current_hinted_resolve.audit.json
1cebfad8a73797be74e336035667de615718e92077e7dbba75d0fe8b738a5128  scratch/k11_current_hinted_resolve.normalized.json
0b526c51062dc7d352a8074708d940cf727dc4f945c019756d9b04d7ed5716e6  scratch/k11_current_hinted_resolve.word
31f574cdc79878ff101ae59086f0b7ce860825aa20ce6b6d1e028db21bf9b910  scratch/k11_current_corefail_resolve.audit.json
b48eca7e4f9308acb95ca00092b182baf85cd8a39f21dc9fb46cc05d8d390ab4  scratch/k11_current_corefail_resolve.normalized.json
0e7df64311d707681057e6cbf024c922379c87728fdfdb42a09baa754f769d07  scratch/k15_bounded_smoke.audit.json
4edbb1f0b3ea1697500ba31fc5e3fbe315494b7a94c37dedbc6e59741b6ee990  scratch/claude_k11_cpsat3_cycle.json
61b11e618650609d341cd4f4e4eaef51ea4ab1244a9e539396922e34092f3fa3  scratch/cpsat_k11_rnd1.json
~~~

The mutable foreign working tree remains outside the repository. Its exact
accepted source bytes are retained read-only as
`scratch/threadD_claude_cpsat_fed3719c.py`; the adapter accepts them only at
the full `fed3719c...` digest and does not install dependencies.

## 12. Reproduction

Lightweight local audit:

~~~text
python3 -m py_compile \
  scratch/threadD_claude_exact_benders_adapter.py \
  scratch/test_threadD_claude_exact_benders_adapter.py
python3 scratch/test_threadD_claude_exact_benders_adapter.py
~~~

Exact compile on H100 CPU:

~~~text
PYTHONPATH=/dev/shm/orlib python3 \
  scratch/threadD_claude_exact_benders_adapter.py compile INPUT.json \
  --claude-source claude_cpsat_fed3719c.py \
  --normalized normalized.json --audit compile.audit.json \
  --cut benders.json --word candidate.word
~~~

Bounded live Benders search:

~~~text
PYTHONPATH=/dev/shm/orlib python3 \
  scratch/threadD_claude_exact_benders_adapter.py benders-search \
  --k 15 --claude-source claude_cpsat_fed3719c.py \
  --audit smoke.audit.json --normalized carrier.json --word candidate.word \
  --max-rounds 1 --round-timeout 10 --core-timeout 10 --workers 8
~~~

## 13. Remaining gate

The fail-closed integration and the installed whole-selector cut scope are
closed. The stronger shore-state row becomes operational only after the
master gains exact directed-collar/omission-state registry literals and the
subproblem is refactored into an omission-state outer cycle plus an inner
weighted-Hall separator. Independently, the open `k=15` existence problem is
still to make the compact outer master return a resident, upper-complete,
lower-q2-complete strict selector whose exact all-core/Hall subproblem is
feasible. A passing outer selector, a sampled core, or a `ready15 READY` line
is not enough. The bounded smoke supplied no `k=15` candidate, so the
rigorous frontier remains unchanged.
