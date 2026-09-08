# Independent mathematical attack: universal contiguous-subarray OR arrays

Act as an independent research mathematician taking over this problem. Use maximum depth. Do not merely summarize the handoff, and do not recommend blind brute force as the main result.

## Problem

For `0 <= k < 20`, determine the shortest integer array with entries in `[0,2^k)` such that every mask in `[0,2^k)` is the bitwise OR of a nonempty contiguous subarray. Equivalently solve the zero-free nonzero-mask problem of length `nu(k)` and then insert one literal zero, giving `N(k)=nu(k)+1` for `k>=1` and `N(0)=1`.

## Required reading

Read these files completely before drawing conclusions:

1. `MATHEMATICAL_HANDOFF.md`
2. `k14_two_sided_factorable_hall_path.txt`
3. `k14_short_interval_containment_matching.txt`
4. `pinnable_factor_sat.cpp`
5. `analyze_pin_core.cpp`
6. `k14_targeted_relocate.cpp`
7. `k14_two_relocations.cpp`
8. `verify_containment_matching.cpp`

Use the files as data, but audit every claimed theorem. Clearly distinguish proved mathematics, machine-certified finite facts, plausible lemmas, and conjectures.

## Certified ledger

- Exact nonzero values are known for `k=1..10` and `k=12`:
  `1,2,4,7,12,21,37,72,128,254`, and `nu(12)=926`.
- `k=11` remains `465 <= nu(11) <= 508`.
- The rank-slack lower bound gives `nu(14) >= 3434`.
- The uploaded `k=14` row has 3432 distinct rank-7 masks, all 3003 rank-6 adjacent-intersection colors, all 3003 rank-8 adjacent-union colors, and no forbidden internal coordinate run shorter than three.
- It has a perfect 6475-target containment matching into the 6867 singleton/pair slots, but containment Hall is weaker than simultaneous pin survival.
- Its complete consecutive-union coverage is:
  rank 7: 3432/3432; rank 8: 3003/3003; rank 9: 1700/2002; rank 10: 939/1001; rank 11: 361/364; ranks 12--14 complete.
- Exact factor SAT proves that original row is unpinnable. A minimal assumption core is the four-mask star
  `{3209,3241,3465,7305}`, where `S=3209` has rank five and the other three are `S` plus one bit.
- For that core, every candidate slot for `S` either collides with the unique forced slot of a rank-6 superset or deletes the sole legal pin of the extra coordinate in a central window. This has been exhaustively certified.

## New repair experiment

A three-edge segment relocation preserves the Hamilton vertex set. We restricted to relocations preserving both complete edge-color layers and the delay-two run condition. Exact SAT cores then guided which missing rank-5 triple-intersection envelope to create.

The initial repair sequence successfully promoted several core masks while preserving every earlier promotion:

`3209 -> 1132 -> 9762 -> 397 -> 5187 -> 9314 -> 13696 -> 167`, followed by branching.

Along a strong branch, the number of distinct rank-5 triple intersections rose from 1818 to at least 1838, while the upper rank-9..11 deficit fell from 367 to roughly 340--350. Every saved branch retained both complete edge-color layers and zero run deficit.

The exact pinning cores repeatedly collapse to a small collection of rank-5 stars. Observed directed transitions under two-relocation repairs include:

- `10448 -> 1797 -> 9858`
- `9520 -> 7744 -> 4652`
- `8486 -> 5344 -> 1174`
- `1797 -> 4652` on another branch
- `4652 -> 1174` on a repaired branch
- several other families directly funnel to `1174`

For some rows, mask `1174` cannot be promoted by any pair of individually two-color-preserving relocations, even when the first relocation is allowed to violate the run condition temporarily. This is only a local move-class obstruction, not an impossibility theorem for the central-row ansatz.

## Primary mathematical tasks

Push the mathematics, not just the computation. In priority order:

1. Find a theorem that upgrades containment Hall to simultaneous pin survival for delay two under checkable expansion/local-geometry hypotheses, or produce a precise counterexample explaining what additional invariant is necessary.
2. Analyze the recurring rank-5 star cores abstractly. Characterize exactly when a star is fatal, and derive a local surgery/augmenting-path theorem that repairs one while preserving the two edge-color layers and run factorability. Go beyond the current two-relocation move class.
3. Determine whether pinning can be formulated as a tractable flow, matroid intersection, interval bigraph problem, 2-SAT instance, bounded-treewidth CSP, or augmenting-path system by exploiting one-dimensional interval geometry and delay two. Prove equivalence if possible.
4. Couple lower pin repair with upper-shadow completion. Seek a potential or absorber theorem showing that core repairs can be arranged without losing complete ranks 8 and eventually cover ranks 9--11.
5. Use the unrestricted monotone-band theorem: any hypothetical length-3434 optimum has at least 3040 consecutive fixed triple witnesses. Determine whether the fixed-row case can be proved necessary after strengthening the counting argument, or whether the at-most-392 boundary deformation can absorb pin obstructions.
6. If exact `k=14` remains out of reach, derive a genuinely new rigorous lemma or improved upper/lower bound that materially narrows the problem. Secondary targets are mathematical reductions between `k=12,13,14` and the unresolved `k=11` case.

## Required output

Produce a standalone research report with:

- an audited theorem ledger;
- the strongest new proved statements, with complete proofs;
- any counterexamples or gaps found in the supplied reasoning;
- a concrete construction theorem or exact finite reduction for the next step;
- a prioritized plan that is mathematical first and computational only where it certifies a sharply defined finite lemma.

Do not claim `nu(14)=3434` without an independently verifiable 3434-entry nonzero array or a complete proof. Do not confuse existence of some factor `D^2 A=T` with existence of a lower-universal pinned factor.

Heavy computation must not be run on this Mac. If computation is indispensable, only specify the exact remote experiment or use the already supplied certificates; concentrate this pass on mathematics.
