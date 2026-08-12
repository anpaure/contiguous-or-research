# Independent audit: K17 bottom-token matching and compound relay theorem

Date: 2026-08-02

## Verdict

`MATH_THEOREM_K17_BOTTOM_TOKEN_PERFECT_MATCHING_AND_COMPOUND_RELAY_CIRCUITS_20260802.md` is mathematically sound for its defined static bottom-relocation class, including the added Theorem 2.7 and conditional Corollary 2.8. The verdict is **PASS with scope and wording qualifications**, not a compiler or universal-word promotion.

The audited theorem file has SHA-256 `14cac3906bb24b30ef080a7ee9624a6f1a833235fab12c4373460614b264c2fe`.

## Finite K17 reconstruction

A new parser independently compared the authenticated origin table
`origin.res1972.tsv` (SHA-256 `db960ce5b51e0fdea7b048d35d48ca737096b16ee73a20df873beb0517e5f185`)
with the relocated `round047.table.tsv` (SHA-256 `95dee6e9718f9067d4bd5c860f7763a45ee03785bdbb13b20b8d95540a7a2735`). It verified:

- 24,310 physical rows and all 65,535 nonempty rank-at-most-eight targets exactly once in both tables;
- origin length histogram `(1748,3899,18663)`;
- exactly 1,748 free receivers, 18,646 eligible hard rows, 3,899 fixed length-two rows, and 17 fixed rank-one-bottom long rows;
- relocated histogram `(0,7395,16915)`;
- all owners, roots, fixed rows and hard suffixes retained on their physical rows;
- every eligible bottom token used exactly once through a legal containment edge;
- exactly 16,898 real-occupied and 1,748 dummy-occupied hard slots.

The complete legal real-placement graph has 401,754 token-to-free edges and 2,129,483 token-to-hard edges. The dummy quotient witness covers all 18,646 tokens and all 1,748 required free rows; restoring the 1,748 dummies gives a perfect matching of size 20,394. The graph contains 119,345 currently applicable relay four-cycles, independently witnessing the atomic relay construction.

## TU and dummy-free formulation

Corollaries 2.2 and 2.3 are correct. In system (2.1), each placement variable occurs once in a real-token degree row and once in a receiver-capacity row. Multiplying every token row by `-1` converts this to the directed node-arc incidence matrix of a bipartite graph. Such a matrix is totally unimodular; adding identity slack columns for hard-slot inequalities preserves total unimodularity. Integral right-hand sides therefore give integral extreme points.

Summing the 18,646 token equalities and the 1,748 free-receiver equalities forces exactly `18646-1748=16898` real-occupied hard slots, leaving exactly 1,748 shorts. No explicit dummy bank is needed.

The phrase “every fractional outer payload point rounds integrally” is imprecise. What is proved is integral extreme points, convex decomposition into integral tables, and an integral optimum for every linear objective. Arbitrary coordinatewise rounding need not preserve feasibility or cost.

## Exact Hall conditions

Corollary 2.4 is exact. For a left set containing real tokens `X` and no dummies, Hall gives

`|N_F(X)| + |N_H(X)| >= |X|`.

If at least one dummy is present, its neighborhood contains every hard slot. For `t` dummies Hall becomes

`18646 + |N_F(X)| >= |X| + t`.

The strongest case is all 1,748 dummies, yielding

`|N_F(X)| >= |X| - 16898`.

These two families exhaust left subsets of the balanced augmented graph, so they are jointly necessary and sufficient. Corollary 2.5 follows by replacing the complete hard neighborhood of a dummy by the prescribed bank `A`.

## Theorem 2.7

The contraction/duality claim is correct.

Let `E = F disjoint-union Hslot`, with `|E|=20394`, and let `M` be the transversal matroid induced by the 18,646 real tokens. The native hard placements already show `r(M)=18646`. Under outer feasibility, `F` is independent and `r_M(F)=1748`. Therefore

- `M/F` has ground set `Hslot` of size 18,646;
- `r(M/F)=18646-1748=16898`;
- `(M/F)^*` has rank `18646-16898=1748`.

A table with short set `S` occupies exactly `F union (Hslot minus S)` with real tokens. This is a basis of `M` containing `F` exactly when `Hslot minus S` is a basis of `M/F`, exactly when `S` is a basis of the dual. Both directions and the claimed rank 1,748 are valid.

The exchange language is valid, although an explicit fundamental circuit should be understood relative to a chosen matching representative; a transversal basis may admit more than one representing matching.

## Conditional common-base scope

Corollary 2.8 correctly states Edmonds’ common-base criterion for two matroids of common rank 1,748 on the hard-slot ground set:

`r_short(X) + r_sock(Hslot minus X) >= 1748` for every `X`.

It is conditional on a separate proof that `M_sock` is a matroid whose bases are exactly the socket-feasible short sets. A bank of genuinely private, injectively assigned socket tickets gives a transversal-matroid example. The actual K17 `1S` system has shared long-tail/head degree, flag and common-cell constraints, so this corollary does not currently reduce that system to matroid intersection. The theorem states this limitation correctly.

Proposition 2.9 is a valid warning. Its three singleton socket menus give independent feasible sets `\{a\}` and `\{b,c\}`, but neither augmentation `\{a,b\}` nor `\{a,c\}` is feasible. This violates the independent-set augmentation axiom and proves that occurrence-labelled tail/head socket matchability is not automatically matroidal. The phrase “basis-exchange augmentation” there should be read as the ordinary independent-set augmentation axiom; the counterexample itself is correct.

## Relay-circuit and scope qualifications

The alternating four-cycle relay and symmetric-difference circuit proofs are standard and correct. Because bottom-relocated tables identify dummy permutations, “the symmetric difference of two tables” should be read after choosing dummy-labeled matching representatives.

The all-dimensional lemma is correct for the defined movable-bottom class. Its closing nonintegrality sentence must remain restricted to that class; unrelated payload coupling rows could also destroy integrality.

Finally, the theorem file labels itself an exact static-table theorem but does not directly bind “the current three-level K17 table” to immutable hashes. This audit supplies such a binding; adding those hashes to the theorem itself would make it self-authenticating.

## Evidence

The frozen finite audit is in `scratch/audit_k17_bottom_token_matching_theorem_20260802/`:

- `audit_k17_bottom_token_matching_theorem_20260802.cpp`: independent parser and complete graph/witness checker;
- `theorem_finite.audit.json`: exact census, graph and relay metrics;
- `bottom_matching.witness.tsv`: all 18,646 token placements;
- `THEOREM_LOGIC.audit.json`: TU, Hall, Theorem 2.7 and scope verdicts.

Its persistent H100 root is `/home/amodo/or15/work/audit_k17_bottom_token_matching_theorem_root_20260802/`.
