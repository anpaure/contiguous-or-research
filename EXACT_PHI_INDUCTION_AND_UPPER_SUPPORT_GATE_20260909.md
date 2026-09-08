# Two-coordinate induction: a local construction and an essential coverage constraint

2026-09-09. The all-dimensional goal remains open. The verified finite
equalities through dimension20 are unchanged; the next target is
`nu(21)=B(21)=352719`.

The current useful direction is a two-coordinate induction retaining the
canonical outgoing matching Phi, as the actual optimal17 and19 carriers
do. This continuation establishes disjoint path pieces for that induction and
disproves a tempting shortcut in its coverage proof. It does not construct
an optimal21 word or an all-dimensional family.

## 1. A canonical local path with a controlled coordinate run

[Full constructive proof](scratch/CANONICAL_PHI_BALANCED_BLOCK_BARRIER_AND_MINIMAL_RUN_SECTOR_EXCURSION_20260909.md).
Let the parent have2r+1 coordinates, and let q be the required minimum
length of a positive coordinate run in its lower-state chronology.
For q>=2 and r>=q+2, take a fixed-root port `L=0D`, with D a Dyck word,
and append two adjacent new coordinates a,b initially equal to10.
Assume a legitimate incoming age history, with a already of age at leastq.

There is a self-avoiding canonical-Phi path of q+2 transitions through
the new-coordinate sectors

    10 -> 00 -> 01 -> 11 -> ... -> 11 -> 10.

It visits one00 state, one01 state and q-1 distinct11 states. Every
deleted coordinate is old enough; b has a positive lower run of exactlyq
and an upper-owner run of exactlyq+1. The endpoint has a of ageq.
Every insertion is forced by Phi, while sufficient aged deletions exist
by the explicit count in the proof. This works for growingq, not only
the triple-window examples.

When the incoming history is the lifted history of a q-resident parent
factor with successor sigma, following its first two deletions makes
the00 and01 ownership maps `Phi(L)` and `sigma(L)` injective. The first11
old part is the specific facet

    sigma(L) intersect sigma^2(L).

Distinctness of these facets and of all subsequent11 paths remains an
allocation condition. It is not licensed by the local path theorem.
The proof also supplies an injective exit map: add the first-minimum zero
to an old rank-(r-1) state. Its inverse deletes the up-step immediately
after the last prefix minimum. Thus distinct terminal11 states have
distinct10 exits. The full age vectors still matter when pieces are joined.

The prescribed entrance was tested at all4862 fixed-root ports of the
actual19 parent. All three entrance steps and their ages pass, but blindly
following both parent deletions gives375 collision pairs in the first11
bank. [Complete fixed-port certificate](scratch/K19_FIXED_ROOT_PRESCRIBED_PARENT_SECTOR_PORT_CERTIFICATE_20260909.md)
records every port and collision. This tests one specified rule; it does
not exclude choosing a different second deletion.

These statements received independent internal pure-proof reviews. They
do not claim that all pieces fit together, preserve every higher target,
or supply a simultaneous short-window compiler and safe opening.

### A complete disjoint bank when q=3

The375 prescribed collisions can be removed by a proof, without another
search. At the third step, every old coordinate in `P minus {u}` has been
present in three successive child states, so ANY of them is old enough
to delete. Distinct P give a family of `(r-1)`-sets after removing u.
The standard small-family shadow bound and Hall's theorem select distinct
`(r-2)`-subsets whenever

    Cat_r <= binom(2r-3,r-1).

The ratio is `4(2r-1)/(r(r+1))`, at most one for r>=7. This reuses the
repository's existing shadow/Hall argument; the underlying shadow bound
is the Lovasz form of Kruskal–Katona, stated in
[Keevash's primary paper](https://arxiv.org/pdf/0806.2023).
Adding u back supplies distinct first11 old states K contained in P.

Now deliberately delete u in the one internal11 step. It has age three,
so the deletion is legal. Writing `J(K)=K+kappa(K)`, the full path is

    L+a,
    Phi(L),
    P+b,
    K+a+b,
    (J(K)-u)+a+b,
    J(J(K)-u)+a.

Both maps J are injective. All first K contain u, while every `J(K)-u`
omits u, so the two11 banks are disjoint. The final old states have prefix
minimum at most-2; every input root port0D has minimum-1. Thus outputs
are also distinct from every input. Different new-coordinate sectors
separate all other banks. The complete six-state, five-transition paths
are mutually vertex-disjoint, and Phi injectivity also prevents repeated
upper owners. Both u and b have lower runs exactly three; a has exit age
three.

This proves existence of4862 disjoint pieces for the actual19 parent.
No explicit Hall matching was computed. The pieces are not yet a spanning
21-coordinate cycle: their exits may lie among untouched parent states,
their continuation ages must be reconciled, and full target coverage and
an optimal opening remain separate requirements.
[Independent shadow and path-bank audit](scratch/Q3_FIRST11_COLLISION_REPAIR_BY_SMALL_SHADOW_HALL_INDEPENDENT_AUDIT_20260909.md)
records the reviewed scope.

## 2. Phi, Hamiltonicity and residence do not imply upper coverage

[Explicit counterexample and proof](scratch/PHI_HAMILTON_RESIDENCE_DOES_NOT_FORCE_FIRST_UPPER_COVERAGE_20260909.md).
Start with the actual verified19 carrier. Write its rank-nine cycle as
R and keep the canonical rank-ten owner `U_i=Phi(R_i)` at each state.
For zero-based indices a=7898, b=53069 and c=78118, replace its order by

    R[:a] + R[b:c] + R[a:b] + R[c:].

This changes exactly three incoming matching assignments. Full replay
verifies that all92378 lower and upper labels remain distinct, the
carrier is one Hamilton cycle, and every residence exclusion still holds.
Nevertheless it loses rank-eleven target109931. Every one of that target's
eleven rank-ten subsets is isolated from the others in the new upper
chronology, so no cyclic upper interval of any length represents it.

This is a counterexample to a proposed implication, not to the supplied
optimal word or to exact equality. It has a nonempty source preserving
the required middle windows. Any lower-cap compiler preserving those
four-window owners must still miss109931: longer source intervals are
unions of consecutive owners and shorter ones have rank at mostten.

The fixed diagnostic examined all1216 recorded three-circuits independently
on the original carrier. Of these,361 preserve both Hamiltonicity and
residence, and19 lose a rank-eleven target. The first example was then
materialized and checked globally, independently of the local screening.
One source-reviewed h100 run finished within its60CPU/90wall/2GiB limits.
[Full result](scratch/k19_phi_upper_three_circuit_diagnostic_20260909/complete_diagnostic_certificate.json)
and [global replay](scratch/k19_phi_upper_three_circuit_diagnostic_20260909/counterexample_full_replay.json)
retain the exact scope, hashes and witnesses of absence.

The additional first-higher constraint has an exact form. Give an incoming
edge `U -> R` the color `U union Phi(R)`. The incoming matching must cover
every rank-(r+2) color. Ordinary matching, connectivity and residence
constraints do not imply this color requirement. Still-higher ranks need
their own coverage proof as well.

## 3. The opening obligation has a smaller exact description

[Completion-run formulation](scratch/EXACT_OPENING_COMPLETION_RUNS_PRINCIPAL_FILTER_AND_FIXED19_DIAGNOSTIC_20260909.md).
The retained exact-width theorem already makes the middle witness lengths
uniform: q and q+1. It also forces q to grow at least on the square-root
scale. These are existing results, not extra hypotheses introduced here.

Opening a universal width cycle with its nextq letters opens its upper
owner chronology with no additional owner letters. A target lost at the
removed edge must contain both endpoint owners, hence their rank-(r+2)
union. For19, only255 proper targets lie in that specified filter.

For each target, its maximal compatible owner runs give an exact test.
Two complete runs protect it. If only the run across the cut is complete,
the latest first occurrence and earliest last occurrence of its coordinates
decide whether a witness survives on either side. This makes the inherited
witness-core criterion explicit; it is not an automatic safe-opening
theorem.

The one fixed supplied19 cut passed this inspection. Of its255 relevant
targets,229 have an incomplete compatible run across the cut,25 have
another complete run, and exactly one needs a one-sided witness in the
unique complete crossing run. That target is515158, of rank12; its
surviving source witness is the final six letters of the optimal word,
at zero-based half-open interval[92375,92381).

That target's sole complete owner run is[92375,92378] inclusive. Its two
minimal witnesses are[92375,92377] and[92376,92378]. Their common internal
edge is the edge entering92377. Consequently moving the opening back one
phase, to92377, would lose this target. This follows from the computed
complete witness family; it is not a second cut search. Even this already
universal cycle therefore does not admit its three-letter opening at
every phase.

The diagnostic recovered all20827 inclusion-minimal owner witnesses for
these targets;20807 survive the cut. It separately checked coordinate
occurrence extrema and replayed a surviving owner/source witness for
every target. [Executed fixed-cut certificate](scratch/k19_fixed_cut_255_20260909/single_cut_255_target_certificate.json)
records the complete scope. Only the existing phase was inspected; no
cut search, word edit or new universal-word construction was performed.

## 4. Remaining construction problem

**A stronger obstruction now rules out completing the entire fixed-root
entrance bank.** The [fresh-arrival theorem](scratch/Q3_ALL_ROOT_ENTRANCE_BANK_FORCES_ONE_STEP_RUNS_20260909.md)
applies before any Hall facets or whole01 paths are chosen. For every
Dyck word D of semilength r-1, the lower00 state011D can only be reached
nontrivially by inserting its second old bit. If every prescribed root
entrance remains, its only available successor is101D, which immediately
deletes that bit. This creates a positive run of lengthone.

Consequently no strict spanning canonical-Phi factor with residence at
leasttwo can retain all Cat_r first entrances. Distinct011D states must
instead use distinct root heads whose prescribed incoming edges have been
changed: at least Cat_(r-1) first incidences must be replaced or reopened.
This is a restriction on the proposed induction data, not on arbitrary
canonical-Phi factors or optimal words. The pairwise disjoint local-path
theorem remains correct, but wholesale completion is impossible.

The subsequent pure analysis makes the gluing problem more explicit.
[The exit theorem](scratch/Q3_EXCURSION_EXIT_AGE_TEST_AND_EXACT_OUTPUT_ENCODING_20260909.md)
shows that the two fresh old coordinates at an exit have ages2 and1.
Following the prescribed parent thereafter is legal exactly when the
first parent deletion avoids both and the second avoids the age-one
coordinate. Both coordinates are recoverable from the output's prefix
walk, so this is a finite two-step predicate on each proposed facet.
The unfiltered shadow argument does not automatically remain valid after
these exclusions are imposed.

[The exact degree ledger](scratch/Q3_EXCURSION_PARENT_COPY_DEGREE_DEFICITS_AND_DIRECT_SPLICE_OBSTRUCTION_20260909.md)
also rules out inserting the bank and repairing only direct edges of an
otherwise unchanged parent10 copy. The mandatory cuts either leave a
mouth with no eligible missing head or already close an isolated component.
Additional sectors and/or additional reopened parent edges are necessary.
This is specific to that direct-splice architecture, not to exact equality.

There is a positive extension: [the complete sector law](scratch/COMPLETE_CANONICAL_PHI_SECTOR_LAW_AND_EXPLICIT_01_STRIP_EXTENSION_20260909.md)
gives a first-return path cover of the entire01 sector. Its fixed-root
unit paths are precisely the corresponding edges of the excursion bank,
so the remaining paths can be added without inventory collisions. The
resulting residual matching problem has three explicit incidence bands;
its ages, connectivity and target coverage are still unproved.

The next construction must select or replace ports before extending its
paths, respecting the mandatory Cat_(r-1) changed incidences. Filling the
unused sectors while keeping all current first entrances is not a viable
remaining task. Any revised bank still needs age-compatible connections,
all-rank upper coverage, simultaneous lower-target compilation and a safe
opening at the exact endpoint budget.

There is now an explicit locally legal replacement bank. The
[two-step age proof](scratch/Q3_ROOT_SOCKET_TWO_STEP_AGES_AND_CORRECTED_1110_HEADS_20260909.md)
rules out the naive110D head: it deletes the third old bit at exact age2.
Every D-one instead has age>=3. WritingD=1R and deleting its first bit
gives1110R, a distinct private head for each forced source011D. The
[complete incidence menu](scratch/FORCED_111_D_FREED_HEAD_MENUS_AND_PRIVATE_DYCK_BANKS_20260909.md)
proves that freeing exactly these heads forces the intended matching.
This resolves one local replacement choice, not the surrounding inventory
or history supply. A conditional connector is
000D11 -> 001D10 -> 011D00 -> 1110R00, requiring initial b-age>=3 and
a-age>=2; those ages must come from an actual incoming history.

The [backward-age interface](scratch/CANONICAL_PHI_BACKWARD_AGE_OBLIGATIONS_AND_INITIAL_PLATEAU_THEOREM_20260909.md)
now handles arbitraryq and genuine boundary ages. It gives exact forced
ages on0^j1^(j+1)D00 and an injective age-legal replacement atj=q-2.
This supplies a local mechanism for growing residence rather than assuming
the q3 age freedom generalizes. A repeated-state backward walk still does
not certify a one-copy middle factor, connectivity or all-rank coverage.

The growing-window case has an additional limitation: the
[forbidden-facet theorem](scratch/SMALL_FAMILY_SHADOW_HALL_WITH_FORBIDDEN_FACETS_LIMITATION_20260909.md)
shows that distinctness and the Catalan family-size bound alone cease to
guarantee Hall after only O(log r) arbitrary forbidden removals per left
state. This abstract counterexample does not realize actual correlated
parent ages; a positive larger-q argument must exploit that extra
structure rather than assume arbitrary age exclusions preserve Hall.

The research snapshot requested by the user was already committed and
pushed as `dfc1a9270a4d681c6ef5975daae81810719a5c82`. This subsequent
research is recorded locally; no new push is claimed.
