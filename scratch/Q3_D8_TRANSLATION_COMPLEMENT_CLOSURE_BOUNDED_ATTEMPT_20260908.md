# Complement closure enlarges the orbit pool; bounded solve remains open

2026-09-08. One complete h100 catalogue and one 18-second CP-SAT
attempt. All target orbits are individually eligible in this relaxed
family. The solver returned UNKNOWN, with no witness and no
infeasibility proof. No mathematical restart or second solve ran.

The cover_selectors agent independently read the full note, source,
catalogue, and saved solver summary and reported an audit PASS for
the family, pairing, critical screen, two-class symmetry reduction,
model, replay code, and UNKNOWN scope. The replay code was audited
but was not executed, because no witness was returned.

## 1. Exact relaxed family

Use coordinates E=F_2^3, a linear hyperplane H, v outside H, and any
full ternary four-coordinate geodesic C on H. The partner chain is
D=C+v. Develop C x D under all translations and global value
complementation x -> 2-x. Short shores retain ranks 1,...,7.

There are 2520 labelled full shore words, or 630 after translating
their first axis to zero. Thus the seven H and four v choices give
17640 translation orbits before quotienting by complementation.
For a canonical word w with first axis zero, its canonical
complement-reversed word is

    refl(w) = reverse(w) xor w[-1],                   (1)

where xor acts on every coordinate label. This is an involution.
The 2184 fixed translation orbits are exactly the individually
self-complementary family from the preceding attempt. Pairing the
others gives

    (17640 + 2184)/2 = 9912                          (2)

combined short-orbit candidates. Of these, 2184 contain four physical
rows and 7728 contain eight physical rows. Their charges are 56 and
112 respectively.

Full candidates are kept from the original self-complementary family:
four physical full rectangles per orbit, with first two shore steps
on the same coordinate. There are 336 such candidates, of charge 72.

The finite target is 164 short rectangles and four full rectangles,
with exactly one selected full orbit. Its actual charge would be

    164*14 + 4*18 = 2368.                             (3)

The rank-seven occurrence budget is exactly 1016. Because the bank
is complement-closed, exact rank-seven coverage gives exact rank-nine
coverage as well.

## 2. Complete catalogue and necessary collision filter

There are 891 target translation orbits and 127 rank-seven translation
orbits. Every rank-seven orbit has eight members. A four-row short
orbit contributes 24 critical occurrences and an eight-row short
orbit contributes 48. Therefore a candidate can occur in a bank
meeting (3) only if it covers respectively three or six distinct
rank-seven translation orbits: any intrinsic repeated occurrence
would violate the exact global occurrence budget.

The complete h100 catalogue returned:

| Short-orbit type | Generated | Admissible | Rejected for critical repetition |
| --- | ---: | ---: | ---: |
| Four physical rows | 2184 | 2184 | 0 |
| Eight physical rows | 7728 | 3024 | 4704 |
| Total | 9912 | 5208 | 4704 |

Together with all 336 full candidates, the admissible pool covers
all 891 target orbits and all 127 critical target orbits. In
particular, the previously missing target

    (2,1,1,1,2,0,0,0),

whose little-endian ternary code is 203, is now eligible. Thus dropping
individual shore complement-translation symmetry resolves the
previous explicit eligibility obstruction.

Individual eligibility is only a necessary condition. It does not
give a simultaneous cover at charge 2368.

## 3. Exact two-class symmetry reduction for the full choice

The 336 full choices form two classes under GL(3,2), acting on the
coordinate labels. To see this, normalize the first axis to zero.
The first half of a full word is 00ab; its symmetry parameter h is
nonzero, and a,b lie in the other h-pair. Thus either b=a or b=a+h.
The three vectors h,a,v are a basis of E. A linear change of
coordinates can send this basis to 1,2,4.

Consequently a cover, if it exists, can be moved so its one full
orbit uses H={0,1,2,3}, v=4, and one of

    00223311,   00232311.                             (4)

The entire enlarged short family, its critical-collision condition,
and every target constraint are invariant under GL(3,2). Restricting
the full choice to these two representatives therefore preserves
existence. This is an exact symmetry reduction, not a sampled pool.

## 4. The one bounded model and its outcome

The CP-SAT model had 5210 Boolean variables: one for each of the
5208 admissible short combined orbits and the two canonical full
choices in (4). It imposed:

* coverage at least one for every target translation orbit;
* coverage exactly one for each rank-seven translation orbit;
* exactly one selected full orbit;
* a sum of 164 selected short physical rectangles, counting each
  short-orbit variable with its row count four or eight.

The solve used two search workers, random seed zero, an 18-second
solver time limit, and stop-after-first-solution. The outcome was

    status: UNKNOWN
    solver wall time: 18.003078891 seconds
    process time including setup: 18.435696110129356 seconds
    branches: 805750
    conflicts: 13317.

No witness was returned. No literal witness replay ran. The source
contains an independent replay stage that would expand all selected
row orbits and check every one of the 6561 target loads, critical
loads, strict-chain comparisons, row count, and actual charge, but
that stage was never reached.

The result leaves this finite family open. It proves neither the
existence of the proposed cover nor impossibility within the family.

## 5. Artifacts and runtime accounting

The relaxed catalogue took 0.3158333171159029 seconds. Including the
preceding stricter catalogue (0.26377706974744797 seconds) and this
one solver process, the total mathematical runtime of the allocated
attempts was approximately 19.015306497 seconds, below 25 seconds.
Both processes ran on h100 with two-CPU affinity and a 3 GiB
address-space limit. The fresh catalogue had a five-second outer
process cap; the solver process had a 24-second outer cap. There
was one solver call and no restart.

Files:

* `q3_d8_translation_complement_closure_attempt_20260908.py`;
* `Q3_D8_TRANSLATION_COMPLEMENT_CLOSURE_CATALOGUE_SUMMARY_20260908.json`;
* `Q3_D8_TRANSLATION_COMPLEMENT_CLOSURE_SOLVER_SUMMARY_20260908.json`;
* `Q3_D8_TRANSLATION_COMPLEMENT_CLOSURE_CATALOGUE_20260908.json`.

The complete catalogue records all target representatives, ranks,
and orbit sizes, and every admissible candidate's literal word,
reflection partner, shore hyperplane, translation, physical row
count, full target-orbit incidence, and critical incidence.

Commands:

```text
ssh h100 'timeout 5s python3 - catalogue' < scratch/q3_d8_translation_complement_closure_attempt_20260908.py > scratch/Q3_D8_TRANSLATION_COMPLEMENT_CLOSURE_CATALOGUE_SUMMARY_20260908.json
ssh h100 'timeout 24s python3 - solve' < scratch/q3_d8_translation_complement_closure_attempt_20260908.py > scratch/Q3_D8_TRANSLATION_COMPLEMENT_CLOSURE_SOLVER_SUMMARY_20260908.json
```
