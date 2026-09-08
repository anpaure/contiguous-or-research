# Exact-equality frontier: fixed matching, interleaving, and trace constraints

2026-09-09, earlier-in-day record. **The finite frontier below is superseded
by the independently verified exact19/20 words:** nu(19)=92381,
nu(20)=184759 and mu(19)=92378. See
[the current exact record](K19_K20_OPTIMAL_AND_CYCLIC19_VERIFIED_20260909.md).
The first unsettled dimension is now21. The structural theorems here
retain their stated scopes.

Before those words were supplied, equality was established through18
and the finite bounds were

\[
 92381\le\nu(19)\le94161,\qquad
 184759\le\nu(20)\le188322.
\]

No new literal word or all-dimensional equality construction is claimed
here. The following completed results constrain the next construction and
extract reusable structure from the supplied optima. The separate
height-moment approximation result is recorded in
[its own method and certificate note](HEIGHT_ADAPTIVE_MOMENT_PREFIX_CERTIFICATE_METHOD_20260909.md).

## 1. The optimal17 carrier retains one complete canonical matching

The independently verified optimal17 word splits into actual cyclic
pieces of lengths85 and24225. From their three- and four-letter ORs,
recover the rank-eight labels L_i and rank-nine labels U_i. Define

    M_out(L_i)=U_i,    M_in(L_(i+1))=U_i.

A complete literal comparison proves that **M_out is exactly the
canonical PBBS matching on every one of the24,310 lower labels**.
The successful word changes M_in. Relative to the native matching,
6,732 incoming incidences agree and17,578 differ. The complete data are
rotation-equivariant, and all1,430 canonical quotient rows have been
recovered from the supplied literal, without its missing search history.

The incoming matching difference has360 nontrivial alternating circuits:
289 of length3,68 of length5, and one each of lengths34,170 and16,167.
The last is one circuit of length16,167, not two circuits. Its quotient
has a951-cycle. No sequence of individually safe small flips realizing
this global change has been established.

The source comparison also checks the two-step insertion/deletion
residence condition: the optimal carrier has zero violations; the
native carrier has119, all at height two. This verifies membership of
the successful word in a useful fixed-matching family. It does not
prove that every dimension has a resident, all-rank-covering matching
in that family, or that arbitrary alternate perfect matchings work.

[Proof and complete comparison artifacts](scratch/K17_OPTIMAL_CARRIER_FIXED_PBBS_MATCHING_AND_EXACT_DIFFERENCE_CERTIFICATE_20260909.md).

## 2. A paired-endpoint theorem strengthens the interleaving requirement

Let a word of length N use coordinates X together with z, and fix a rank
s on X. Let a count its distinct represented rank-s targets avoiding z,
and b its represented rank-(s+1) targets containing z. If R_out and R_in
count present-to-absent and absent-to-present transitions of z, then

\[
 \boxed{a+b\le N+R_{\rm out},\qquad a+b\le N+R_{\rm in}.}
\]

Choose one endpoint for every target in each family. Each family uses
distinct endpoints because suffix unions form a chain. At least a+b−N
endpoints are shared. At a shared endpoint the two target sets are
D and D union {z}. If q is the last marked position, the union of the
unmarked run from q+1 through that endpoint is exactly D: the old
witness is contained in this run, and the marked witness contains it.
An increasing run-prefix union takes at most one distinct rank-s value.
Distinct shared targets therefore inject into distinct noninitial
unmarked runs. Reversal proves the entrance version.

For a universal word, a=b=binom(|X|,s). In odd dimension2r+1, at target
length W(2r+1)+d, this yields

\[
 \boxed{R_{\rm out},R_{\rm in}\ge\max(0,\operatorname{Cat}_r-d).}
\]

In particular every coordinate of an exact19 word needs at least
**4,859 exits and4,859 entrances**, strengthening the earlier541 bound.
At exact17 the corresponding count is1,427. The endpoint-overlap step
and those numerical deficits occur in earlier research; the additional
run injection is the new strengthening. This is a necessary condition,
not an impossibility proof for exact equality.

[Complete proof, boundary cases and prior attribution](scratch/PAIRED_ENDPOINT_CATALAN_RUN_BOUND_INDEPENDENT_AUDIT_20260909.md).

One reviewed h100 diagnostic also passes all137,256 nonempty words on
three coordinates through length six, in both orientations:1,647,072
family checks and454,260 literal shared-witness replays. It separately
checks only the run/rank statistics of the already certified17/18
words, with their hashes pinned. At17 each coordinate has2,231 or2,232
exits and entrances, consistent with the new necessary bound. This
3.602-second run is a diagnostic of the proof, not a word search or a
new full-cube verification.
[Execution record](scratch/paired_endpoint_run_diagnostic_20260909/PROVENANCE.md).

## 3. The unmarked trace must change at the next odd step

If M letters avoid z and H_s of their maximal unmarked runs start with
a literal rank-s letter, the old-target endpoint budget gives

    R_total−H_s <= M−binom(|X|,s).

Combining it with the paired-endpoint theorem gives

\[
 H_s\ge\max\{0,3\binom{|X|}{s}-N-M\}.
\]

At N=B(19)=92381 and M=48623, there must be at least4,856 rank-nine
run starts and4,856 such run ends. An unmarked trace containing no
rank-nine literal instead needs at least53,479 letters,4,856 more than
the optimal18 length. These strengthen the earlier4,835-start and
605-extra-letter estimates for the same restricted trace regimes.

The actual optimal18 word has no rank-nine literal: every letter has
rank at most seven. More strongly, a complete shortest-witness census
certifies that **all48,622 internal insertion gaps are fatal** to some
old nine-set if a marked letter is inserted there. Its first nine-set
has endpoint3 and greatest possible witness start0; every later endpoint
has its own unique nine-set and a shortest witness crossing the preceding
gap. Thus an extension whose unmarked subsequence is exactly this word
must leave it contiguous.

Such a word has at most one exit and one entrance. The stronger paired
bound therefore gives length at least97,239. This supersedes97,234 for
this fixed-trace architecture. It is not a lower bound on unrestricted
nu(19), nor a claim that97,239 is achievable.

[Complete cut-core certificate](scratch/EXACT_INTERLEAVED_LIFT_RUN_START_BUDGET_AND_FIXED_TRACE_CUT_CORES_20260909.md)
and [every internal gap](scratch/k18_fixed_trace_cut_cores_20260909/every_interior_gap_certificate.jsonl).
The general occupied-cut criterion has earlier instances in the
fixed-K16 work; the independently checked exact18 instance is new here.

## 4. Exact compiler for genuinely interleaved tags

For a fixed sequence of old-coordinate projections, the old recency
partition P is independent of how new-coordinate tags are assigned.
After the first tag, let q be the most recent tagged position, B the union since q, and C
the union of B with the old projection at q. At that endpoint:

- Old targets are exactly the prefixes D of P with D contained in B.
- Marked targets D union {z} are exactly the prefixes containing C.
- The singleton {z} is available exactly when C is empty.

These conditions describe the whole conditional state, not just one
chosen witness. A tag resets B to empty and C to its current projection;
an untagged update unions its projection into both. Dual service of D
and D union {z} requires B=C=D.

There is also an exact finite protected-witness formulation. For every
old target D choose one projected interval J_D with union D. Let F be
the union of these protected positions and any forced-unmarked positions.
Let H_D be the union of positions over every projected witness for D.
Force every zero-projection position to be tagged, and require at least
one such position to supply {z}. An exact tag assignment exists precisely
when some such choice of protected witnesses makes F avoid every forced tag and
H_D minus F is nonempty for every D. Marking all positions outside F
then constructs the required assignment. These witness choices are
coupled; no general flow or integrality theorem is asserted.

[Full cursor and compiler proof](scratch/EXACT_MANY_RUN_RECENCY_CURSOR_AND_PROTECTED_WITNESS_COMPILER_20260909.md).

## 5. A separate pair-reservation tool, with its unresolved allocation gate

For two editable letters L,R with mandatory pins P,Q, a target S can be
the union of two nonempty proper subletters E,F exactly when

    P union Q subseteq S subseteq L union R,
    a in (S intersect R) minus P,
    b in (S intersect L) minus Q

for some distinct a,b. Taking E=(L intersect S) minus {a} and
F=(R intersect S) minus {b} proves sufficiency. Extra literal pin/union
conditions preserve every triple of a prescribed independent block
frame, hence every longer window.

Once a source, independent frame and retained rank-eight palette are
specified, a target-to-block-to-displaced-label flow exactly selects
distinct proper-pair reservations while keeping an old witness for
every rank-eight label. This does not solve the remaining lower-target
allocation or create an exact-length resident carrier.

In the particular H1/H2-frozen canonical19 bank, low-target counting
requires6,669 targets to have nonliteral witnesses. A pair that is
proper at its chosen block can still occur literally elsewhere. It
must not receive duplicate capacity credit. If T is the reserved set,
F the frozen H3 positions and L_F their distinct literal labels, then
literal completion of all remaining low targets requires

    |T minus L_F| >= 6669 + |F| - |L_F|.

This coupled capacity gate and all remaining target eligibility must be
checked before interpreting a raw flow value as constructive progress.
No such flow, lower CSP, or word search ran in this continuation.

[Pair-reservation lemma and scoped next gate](scratch/K19_GENUINE_PAIR_RESERVATION_LEMMA_AND_NEXT_FINITE_GATE_20260909.md).

A useful stronger acceptance condition is now explicit: choose one
retained native witness for every still-unprotected rank-eight label,
install coordinate backbones whose union is that label, and match every
remaining lower target to a distinct free position between its backbone
and its available source letter. A saturating matching constructs one
simultaneous cap preserving all designated witnesses. These choices must
be supplied together; the standalone reservation flow does not ensure
them and its execution is deferred.
[Coupled backbone and Hall theorem](scratch/K19_PAIR_RESERVATIONS_COUPLED_BACKBONE_HALL_CONDITION_20260909.md).

The next exact construction must meet these chronology, inventory,
all-rank coverage and boundary conditions simultaneously. The unchanged
PBBS constructor's exponentially large additive collar remains an
obstruction to attaining B merely by improving its period estimates.
