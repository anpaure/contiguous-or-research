# Soundness reconciliation for the promoted `k=15` q2-only pair-cover factor

Date: 2026-07-29

Status: `PASS` for the exact scope promoted in handoff item 1849.  The artifact
is not a resident double-shadow sigma candidate, and a verifier which requires
those stronger gates correctly rejects it.  No pair-cover H100 process remains
active after this audit.

## 1. Artifact under audit

The exact artifact is

```text
scratch/k15_global_pair_cover_q2complete_raw_20260729.json
SHA-256 59fb88bd84180d16348e0b86f234362d0df490cefa160977fe939e1f837f5dc1
```

Its stable compact-JSON selected-incidence digest is

```text
f1a5c676af5fadcf376bf2f3d5b7eec5298e47a825653896a84988225597ab61
```

The promoted claim is exactly:

1. the 429 explicit quotient rows lift to a spanning physical middle
   `2`-factor;
2. all 6,435 rank-eight middle states occur once;
3. all 6,435 rank-seven lower-`q1` colours occur once;
4. all 5,005 physical rank-six lower-`q2` targets occur.

The artifact was explicitly reported to have upper-`q1` holes and residence
defects.  Neither upper-`q1` completeness nor residence four belongs to this
particular positive claim.

## 2. Fresh independent replay

The new fail-closed auditor is

```text
scratch/audit_k15_paircover_q2_claim_reconciliation_20260729.py
SHA-256 4addba9f5287c298cefb69719f59e172dad02eb89ce8494e0efb392009867435
```

It imports neither pair-cover implementation nor the sigma SAT generator.
It rebuilds the voltage-labelled quotient from the 429 literal rows
`[lower,a,b]`, then expands every physical cycle.

The retained output is

```text
scratch/k15_paircover_q2_claim_reconciliation_20260729.audit.json
SHA-256 34df852f95c59c318e05ee8f4faea5910d07efd8b0d086083adfb72f04d12e1e
```

with status

```text
PASS_CLAIM_SCOPE
```

## 3. Doubled-edge reconciliation

The independently rebuilt quotient catalogue has

```text
edge orbits                         3432
endpoint multiplicities       1^3404 2^14
```

so the fourteen voltage-distinct doubled endpoint pairs are present and are
not collapsed.  The selected artifact uses exactly one edge from three of
those doubled pairs and no edge from the other eleven; it never selects both
members of a doubled pair.  Hence its projected Johnson quotient has zero
loops.  The explicit choice rows and the selected incidence-ID list induce
the same 858 edge orbits exactly; their symmetric difference is empty.

This directly rules out the suspected doubled-edge decoding error for this
artifact.

## 4. Literal physical result

Direct expansion gives two quotient components.  With the auditor's chosen
orientations their data are

```text
rank-8 quotient vertices     voltage       physical lift
105                              14          one 1575-cycle
324                              13          one 4860-cycle
```

Voltage 13 is the opposite orientation of voltage 2.  Thus the invariant
voltage classes are `{1,14}` and `{2,13}`, agreeing with the earlier report.

The physical ledgers are

```text
middle rank 8             6435 / 6435, load 1^6435
lower q1 rank 7           6435 / 6435, load 1^6435
lower q2 rank 6           5005 / 5005
```

The physical lower-`q2` load histogram is

```text
1^3705 2^1170 3^130.
```

After dividing by the exact orbit lift multiplicity, the quotient-occurrence
histogram is

```text
1^249 2^78 3^8.
```

Therefore `P_Psi=102` and the quotient-normalized collision excess is
`Xi_Q=8`, exactly as item 1849 states.

## 5. Short-orbit audit

The two short rank-six representatives are 3171 and 5285.  Each has orbit
size five.  For each representative, all five physical members occur with
load exactly three:

```text
3171: 3,3,3,3,3
5285: 3,3,3,3,3.
```

Thus each short orbit has quotient-occurrence load one and physical member
load `15/5=3`.  All ten short-orbit physical targets are present.  The
artifact therefore passes the composite-orbit coverage rule; it never
mistakes quotient cap two for physical cap two.

## 6. Why the stronger sigma auditor rejects it

The fresh replay also reproduces the two advertised nonclaims:

```text
upper q1             3945 / 5005, hence 1060 physical holes
minimum run                     2
residence-four bad runs      1215
residence-four shortfall     1680
```

`scratch/audit_sigma_factor_candidate_20260729.py` is intentionally a
verifier for a **resident double-shadow** factor.  It requires both complete
upper `q1` and complete lower `q2`, and it rejects any minimum run below
`d+1=4`.  It also expects the separate
`global-rainbow-factor-candidate-v1` schema.  Therefore applying it directly
to the q2-only pair-cover artifact either rejects the schema or, after a
faithful choice translation, rejects the two missing stronger gates above.

That failure is expected and does not contradict the q2-only claim.  As a
second independent check, the grouped trusted implementation
`SigmaInstance.verify_factor` was run on the same 429 choices with residence
auditing disabled.  It returned

```text
physical cycles       2, lengths 1575 and 4860
unique middle         6435
unique upper q1       3945
unique lower q2       5005
minimum run           2.
```

## 7. Verdict and process cleanup

The promoted item 1849 factor does **not** fail its independent physical
claim.  No retraction is warranted.  The alleged contradiction is a scope
mismatch between a q2-only factor certificate and a verifier for the
strictly stronger resident double-shadow gate.

All still-running superseded pair-cover jobs located during this
reconciliation were terminated on the H100 CPU host.  No solver status is
used in this verdict.
