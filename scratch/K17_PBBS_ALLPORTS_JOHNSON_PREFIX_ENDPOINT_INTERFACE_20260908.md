# Endpoint interface for the replacement all-ports Johnson prefix

Date: 2026-09-08.
Status: exact necessary constraints and conditional final-pin construction, with one bounded h100 check. This concerns the NEW all-ports Johnson prefix, not the superseded three-non-Johnson prefix.

## 1. Source and exact check

The replacement prefix and maximal depth-two factor are

    scratch/badsix_allports_johnson_306_owner_path.word
    scratch/badsix_allports_johnson_308_depth2_source.word.

The six canonical cycle/cut choices are all forward:

    116/33,118/32,122/31,129/30,138/29,115/0.

The construction record establishes 306 distinct rank-nine owners, only Johnson steps, no internal repeated rank-eight adjacency color, literal depth-two replay, and preservation of all proper upper targets against the 140 intact outside cycles. The current global adjacent rank-eight palette misses exactly

    H={43857,46420}.

One bounded ordinary-interval scan of the 308-letter maximal factor finds neither target. This is true both of intervals wholly inside stable physical positions 0,...,305 and of intervals using temporary boundary positions 306 or307. This observation alone would not exclude later capping; the endpoint theorem below controls that possibility.

## 2. The one-pivot exceptional positions

For a completion P,Q on the fixed schedule

    I_i=[i,i+2], i<306;
    I_i=[i,i+3], i>=306,

ending at physical position24312, the proved exceptional-facet theorem gives only three possible families for rank-eight targets absent from the final owner-adjacency palette:

1. initial prefixes [0,0] and [0,1];
2. the pivot cell [306,308]; and
3. final suffixes ending at24312.

The proof is in Section2 of

    scratch/K17_PBBS_PREFIX_RANK8_PROVIDER_INTERFACE_20260908.md.

That general theorem remains valid although the old specific prefix in that note is now ruled out. Each family contributes at most one distinct rank-eight target. All other lower cells of a rank-eight witness lie in two adjacent rank-nine owners and therefore have an adjacency-palette value.

The replacement has b=e_inside=0, so it does not meet the old prefix's b3 obstruction. The endpoint restrictions below leave a nonempty possible extension interface.

## 3. Neither hole admits an initial pin

The replacement's first owners are

    P_0=43613, P_1=43853, P_2=43877,

and its first maximal source letters are

    E_0=43613, E_1=43597, E_2=43589.

Neither43857 nor46420 is contained in P_0. Every initial exceptional witness is contained in the first owner interval, so neither target can be produced there under any cap preserving P_0. In particular there is no legal exact initial letter pin for either current hole.

This statement does not forbid pinning another facet of P_0 as a later boundary repair. Such a different facet would need its own actual missing-color obligation and simultaneous positive guards.

## 4. Neither hole admits the pivot, for any Q

The replacement retains the same terminal 51-owner block as the old prefix. Consequently

    P_305=103765, E_305=5461,
    P_305 minus E_305={bits15,16}.

To reproduce P_305 on[305,307], both bits15 and16 must appear at positions306 or307 in every subordinate source. Therefore a target on[306,308] must contain both. Both43857 and46420 omit bit16, so neither can use this exceptional pivot cell, regardless of the Q endpoints or later common caps.

Neither target is contained in P_305 either. Thus neither can be the adjacent-intersection color of the P/Q seam.

## 5. Exact final pin and available superowners

Let U be Q's final owner and V its penultimate owner, and suppose the complete maximal source already replays all owners. The last source letters are

    E_24311=V intersect U, E_24312=U.

For a chosen facet S of U, write U=S union{b}. Replacing the final letter by S preserves the last owner if and only if b belongs to V. Indeed b then survives at E_24311; if b is absent from V, every earlier position of the last owner interval is contained in V and cannot supply it. Earlier owner intervals do not use the final source position.

Thus a simple exact terminal prescription is

    A_24312=S,  b in A_24311.

The latter is a positive guard to retain during common-cap compilation. For Johnson-adjacent V,U, this says S differs from the already present adjacent facet V intersect U.

The available final owners and internal adjacency providers are:

| target S | remaining rank-nine superowners in Q |
|---:|---|
| 43857 | 43861,43889,43985,44881,47953,60241,109393 |
| 46420 | 46421,46428,46452,46548,46932,48468,62804 |

Each target has exactly two other superowners already in P: its original cut-block endpoints, at positions51,101 for43857 and204,254 for46420. The seven listed owners are therefore the complete remaining provider set, not a sampled menu.

Any two distinct owners in one row intersect exactly in S and give a candidate Johnson adjacency with that color. To use S at the final letter, choose U from its row and a remaining predecessor V containing its exceptional bit b=U minus S. If V is Johnson-adjacent to U, it must remove a coordinate of S, not b. This is an exact local endpoint condition; it does not prove that the prescribed V,U can be reached in a resident upper-complete Q.

## 6. Necessary extension choice

The initial and pivot exceptions cannot supply either current hole. The terminal suffix family can supply at most one. The P/Q adjacency cannot supply either. Therefore every universal one-pivot completion of the replacement prefix must have

    at least one of43857,46420
    as an adjacent intersection strictly inside Q.

A concrete local plan is either:

- recreate43857 as an internal Q adjacency and reserve46420 for the final exact pin;
- recreate46420 internally and reserve43857 for the final pin; or
- recreate both internally.

These are candidate source-level interfaces. A reserved adjacency color is not by itself a completed literal lower witness under arbitrary capping: the canonical overlap witness of a valid maximal Q source must remain an explicit positive obligation in the common-cap compiler. The terminal pin, when its guard is retained, is already a literal one-letter witness.

No universal extension or new value of nu(17) follows from this finite result.

## 7. Verification record

The check used only the two fixed literal files in

    /home/amodo/exact-b-k17-badsix-all-ports-20260908/

and enumerated ordinary interval unions for the two specified targets. It also checked their containment in P's endpoint owners, the mandatory pivot bits, and all nine superowners per target, separating the two in P from the seven remaining. No new port bank, DP, random experiment, or extension search was run.

The exact output is retained as

    scratch/k17_pbbs_allports_johnson_rank8_endpoint_interface_20260908.json.

All mathematical execution was on h100. The structural endpoint exclusions and final-pin equivalence are proved above.

## 8. Exact upper-rank credit of the replacement prefix

A final bounded check evaluated only the five NEW block seams and looked up their upper colors in the existing complete exclusive-target inventories. No eight-superset check, cycle census, or new search was rerun.

| zero-based seam edge | rank-ten union | exclusive reference supplier | among59 forced-unsafe cycles? |
|---:|---:|---:|---|
| 50 | 43993 | cycle102 | no |
| 101 | 44883 | cycle84 | no |
| 152 | 44375 | none | no |
| 203 | 48470 | cycle71 | no |
| 254 | 128340 | cycle69 | no |

The same results hold after the mountain C6 replacement: none of the five colors enters either new mountain component's exclusive family. Thus these five seams receive zero credit against the59 globally unique rank-ten edge colors that every complete linear rethread must recapture from the59 forced-unsafe reference cycles.

The replacement's last owner is still103765. Therefore the earlier complete check of its eight rank-ten supersets applies unchanged. None is exclusive to a forced-unsafe cycle, before or after the mountain replacement. Both the sole physical upper exception [305,308] and any rank-ten P/Q seam contain this last owner. Neither can earn one of the59 necessary private colors.

It follows that, for a universal one-pivot completion beginning with this replacement prefix,

    at least59 distinct rank-ten colors must be supplied by
    NEW owner edges strictly inside Q, relative to the reference factor.

This remains necessary under arbitrary Q rethreading, not merely one-cut-per-cycle concatenation. Every spanning linear owner path omits an edge from each reference cycle. In each of the59 unsafe cycles, every edge has a globally unique rank-ten adjacent-union color; selecting one omitted edge per cycle gives59 distinct absent reference colors. The upper-J theorem leaves only the pivot exception, which cannot supply them. The fixed prefix and P/Q seam cannot supply them either. Their new edges must therefore occur inside Q.

This is a count of distinct required adjacency colors, not extra physical letters. The59 need not be the same fixed targets for every Q: the omitted reference edges determine them. New Q edges can supply them, so the count does not rule out the construction.

Artifacts:

    scratch/audit_k17_allports_johnson_prefix_rank10_credit_20260908.py
    scratch/k17_pbbs_allports_johnson_rank10_seam_credit_20260908.json.

The original-prefix verifier and its artifacts were left unchanged. Mathematical execution for this five-seam update was only on h100.
