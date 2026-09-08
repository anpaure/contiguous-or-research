# Exact 20-letter singleton extension of the user's native 291-word

Date: 2026-09-08. Status: proved and verified for the displayed finite words.

The user supplied the native 35-cycle, eight-cycle graft, and rooted 291-word
audited in `USER_NATIVE35_GRAFT280_AND_ROOTED291_INDEPENDENT_CERTIFICATE_20260908.md`.
The present extension is an independently constructed continuation of that
literal 291-word. It introduces its fourteen missing singleton targets while
every appended endpoint supplies a previously absent rank-eight triple union
and a previously absent rank-nine four-window union.

Exactly twenty letters suffice. Twenty is minimal among continuations that
keep all newly ending triple windows at rank eight. The resulting 311-word is
also optimal for its own complete 1,979-target family. This is a partial-family
result, not a universal word on the 17-cube and not a value of nu(17).

## 1. Exact legal-letter rule and the two-singleton gadget

Write L, B, A, T for the current unions of the last one, two, three and four
letters. At a stable frontier they are nested with cardinalities 6,7,8,9.
For an appended letter X, the new triple and four-window are B union X and
A union X. They have cardinalities eight and nine if and only if

    X={z} union V,  z outside A,  V subset B.

Indeed, their ranks require |X minus B|=|X minus A|=1, so the same unique
outside coordinate z is outside A and everything else in X lies in B.
If the new four-window must be new, z is actually outside T: the only member
of T minus A would simply reproduce the already realized owner T. The two
remaining freshness checks are B union {z} absent from the full old rank-eight
inventory and A union {z} absent from the full old rank-nine inventory.

Append a singleton z satisfying these checks. The suffix-rank profile becomes
(1,7,8,9). Append another fresh singleton w outside the new owner, checking its
new triple L union {z,w} and four-window B union {z,w}. The profile becomes
(1,2,8,9). Choose a in L and v outside L union {z,w}, and append

    X=(L minus {a}) union {v}.

The new triple is (L minus {a}) union {z,w,v}, of rank eight, and the new
four-window is L union {z,w,v}, of rank nine. If both are fresh, the profile is
again (6,7,8,9). Thus this three-letter gadget introduces two singletons and
restores the frontier. The last pair does not need a restoring letter.

At the original endpoint, (L,B,A,T)=(318,382,510,1022). The missing singleton
coordinates are exactly 1 through 14. The immediately legal missing singleton
menu, including global freshness checks, is exactly {11,12,13,14}.

## 2. Literal continuation and deterministic selection trace

Coordinates x correspond to bit x-1 of a mask. Append these twenty masks:

    1024,1,16686,
    64,16,17454,
    128,256,17423,
    512,32,17431,
    2048,4096,17491,
    8,4,17521,
    8192,2.

The selected missing singleton pairs and restoring choices are:

| Round | Singleton coordinates | Restoring mask | Removed coordinate a | Added coordinate v | Legal ordered pairs | Complete candidates |
|---:|:---|---:|---:|---:|---:|---:|
| 1 | 11,1 | 16686 | 5 | 15 | 20 | 885 |
| 2 | 7,5 | 17454 | 9 | 11 | 36 | 1704 |
| 3 | 8,9 | 17423 | 6 | 1 | 25 | 1200 |
| 4 | 10,6 | 17431 | 4 | 5 | 16 | 734 |
| 5 | 12,13 | 17491 | 3 | 7 | 8 | 330 |
| 6 | 4,3 | 17521 | 2 | 6 | 4 | 187 |
| 7 | 14,2 | none | none | none | 1 | 1 |

At each stable frontier the verifier enumerated precisely the legal ordered
pairs of missing singleton coordinates and the six-letter restorations in
Section 1. Its deterministic score first minimizes pending singleton
coordinates in the resulting last letter, then in its owner, then maximizes
the next immediate singleton menu, then avoids using a pending singleton as
the restoring fresh coordinate, and finally breaks ties by the masks. There
was no leading filler, global backtracking, random search, or larger fallback
family. All seven stages succeeded in this fixed family.

## 3. Exact coverage, rank potential, and lower-rank incidence accounting

An independent fixed-word census enumerates all 48,516 nonempty ordinary
intervals of the 311-word. Every distinct target is stored with its rank,
one exact zero-based start/end witness, and its full occurrence count.

All 1,876 targets of the original prefix survive. There are 103 new targets,
giving 1,979 in total. All seventeen singleton targets are present. The counts
at ranks 1 through 17, in order, are

    17,31,57,84,89,158,149,308,308,219,190,147,114,63,32,12,1.

The twenty new rank-eight triple targets and twenty new rank-nine four-window
targets are globally new when appended. Consequently D_8=D_9=308.
At rank nine the exact recency-potential identity from the preceding native
certificate gives

    N-D_9=L_9+b_9(P_N)+E_9=0+3+0=3.

The native prefix had 548 distinct targets below rank eight, with 582
below-eight recency-prefix incidences, hence 34 repeated incidences. Each
appended endpoint has precisely two such prefix unions, so the extension
adds 40 incidences. It supplies 37 new distinct below-eight targets, hence
three additional repeated incidences. The final counts are therefore

    distinct below eight = 585,
    below-eight incidences = 622,
    repeated below-eight incidences = 37,
    distinct below nine = 893.

The extension certificate records all twenty new middle/facet witnesses,
the thirty-seven new below-eight masks, the selected gadget trace, and the
potential identity. The independent complete census records every target.

## 4. The twenty-letter extension is minimal under the stated triple condition

Each of the fourteen missing singleton targets requires an appended singleton
letter: a nonempty interval union equal to a singleton can contain only that
singleton letter (empty letters, if allowed, cannot help create the target).
At least fourteen appended positions are therefore singleton letters.

Three consecutive singleton letters have union of size at most three and so
cannot be a newly ending rank-eight triple. Every consecutive run of appended
singleton letters has length at most two. With f nonsingleton separators,
there are at most f+1 such runs, giving at most 2(f+1) singleton positions.
Fourteen singleton positions force f>=6. The continuation has length at least
14+6=20, and the displayed one attains this bound.

This argument applies to any continuation satisfying the rank-eight triple
condition, not just the particular restoring gadgets. It does not rule out
shorter unrestricted edits or continuations that abandon that condition.

## 5. The 311-word is optimal for its complete target family

Let a word cover M specified distinct rank-nine targets and Lambda specified
targets of smaller rank, and write its length M+t. Select one interval for
each rank-nine target. The selected intervals form an antichain, so their
ordered endpoints have the form [i+alpha_i,i+beta_i] with
0<=alpha_i<=beta_i<=t. Every interval avoiding all selected intervals has
length at most t. A required lower-rank target must use such an interval.
There are at most

    tM+t(t+1)/2

intervals of length at most t, and hence at most that many distinct required
lower-rank targets. This bound uses only the selected M targets; it permits
the realizing word to produce additional rank-nine targets.

For the full 311-word family, M=308 and Lambda=893. At t=2 the bound is
2*308+3=619<893. Thus any word realizing this family has length at least
308+3=311. The displayed literal word proves equality for this family.

## 6. Separate bounded obstruction to pair-preserving singleton shrinkage

The parent's independent fixed host census examined all 291 original letter
positions and all fourteen missing singleton coordinates. A replacement of
letter E_i by a singleton S subset E_i preserves each adjacent pair union
exactly when E_i minus each existing neighbor is contained in S. None of the
fourteen singleton coordinates has even one such position.

The saved certificate is
`native35_user_graft_20260908/native291_singleton_host_census.json`.
This excludes that individual shrinking recipe on the original fixed word.
It does not exclude coordinated edits, other notions of target preservation,
or arbitrary continuations.

## 7. Exact artifacts and execution scope

All literal and data files below are in `scratch/native35_user_graft_20260908/`:

* `native311_all_singletons.word`: full usable 311-letter word.
* `native20_singleton_extension.word`: twenty appended masks.
* `native291_singleton_extension_certificate.json`: complete gadget trace,
  new middle/facet endpoint witnesses, lower-rank census and potential.
* `native311_all_interval_witness_census.json`: all 1,979 target witnesses
  and occurrence counts across all 48,516 ordinary intervals.

The original output names `native291_singleton_extension.word` and
`native291_singletons_extended.word` are retained as identical provenance
copies. Scripts are

    scratch/extend_native291_singletons_fixed_gadgets_20260908.py
    scratch/certify_native311_interval_census_20260908.py.

Both mathematical executions took place only on h100 in
`/home/amodo/exact-b-native35-user-graft-20260908/`, with limits of 90 CPU
seconds, 110 wall seconds, and 1 GiB address space per process. The first run
performed the single bounded gadget selection; the second only enumerated
the fixed completed word. Both returned PASS. No full-cube source, existing
PBBS bank, master handoff, or unavailable static inventory was modified.
