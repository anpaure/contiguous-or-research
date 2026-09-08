# Independent review of the actual-parent 0P1 age supply

Date: 2026-09-09. Pure-proof review **PASS**; no execution.

Read the complete
[0P1 source-age theorem](ACTUAL_PARENT_0P1_EMBEDDING_CONNECTOR_AGE_SUPPLY_AND_BAD_EDGE_CRITERION_20260909.md).
This is distinct from the smaller-input00X11 embedding: a is an active parent
coordinate and b alone is permanently present.

The shifted-height proof of `Phi_child(0P1)=0Phi_parent(P)1` checks. At a
port P=00D1, with D=1R, the three connector deletions b,a,d have ages
infinity,alpha+1,gamma+2, where alpha and gamma are their actual parent ages
at the port. Since gamma>=1, legality for residence3 is exactly alpha>=2.

The inverse classification includes all containing uppers. Adding the first
parent zero gives10D1; its last minimum0 is the final Dyck return, so inverse
Phi removesa and gives predecessor10D0. Adding the second zero gives the
Phi self-return. Adding a D-zero makes the last minimum−2 the final Dyck
return before that flipped zero; the inverse removes the subsequent D-one,
not a. Hence alpha=1 if and only if the specified incoming edge is10D0→00D1.
No other incoming case is missing.

For any subset of passing ports, all new lower states have b=0 while every
embedded lower has b=1; the three new banks have distinct initial prefixes.
The first consumed upper is reused, the other two are outside the embedded
upper inventory, and all maps from D are injective. Thus the ledger
M+3h used lower states and M+2h consumed uppers/assigned edges is exact.

The free upper1110R01 starts with11. Every missing input head0sigma(00D1)1
starts with00 because Phi_parent(00D1)=01D1. One facet deletion cannot remove
both initial ones, so no direct matching of only these free ends to these
heads closes the paths. The inherited boundary-age requirements remain
necessary for later gluing.

The theorem is a finite input gate and conditional path bank. It does not
assert how many ports pass in the actual nineteen-coordinate carrier, a
residual matching, or a full child word. Numerical counts await the separately
reviewed and authorized fixed-input diagnostic.

## Full pre-execution source review

Read the complete
[fixed actual19 checker](audit_actual19_embedded_corrected21_connector_ages_20260909.py)
and its [review plan](ACTUAL19_EMBEDDED_CORRECTED21_CONNECTOR_AGE_DIAGNOSTIC_REVIEW_PLAN_20260909.md):
**PASS**. Reviewed source SHA-256:
`27388f115066d5f6270a8d8957bc3503d81ddf231aa5e65d989afeef0663a6dd`.
No execution by this reviewer.

The bit embedding is exactly0P1: parent coordinate18 becomes active childa19,
while b20 is permanent. The checker reconstructs the pinned complete19
middle carrier, checks canonical Phi and residence, and tests embedding
commutation on its entire factor. Recursive Dyck generation and a separate
scan of the named lower layer identify the same fixed port family.

Exact cyclic a and first-D-bit ages are independently replayed backwards at
each port. Enumerating every containing upper independently checks the sole
bad-predecessor formula. Three embedded parent states suffice for the actual
threshold3 connector replay: the reported finite deletion ages are3,
`min(alpha,3)+1`, and `min(gamma,3)+2`, while the separately computed exact
ages retain infinity,alpha+1,gamma+2. The finite replay therefore does not
mistake truncated age data for smaller true ages.

All four lower banks, all three used-upper banks, and their injectivity are
checked without assuming a zero bad count. Good and bad lists are complete,
and the quoted1430 is a comparison field. Resource interruption cannot
produce the final PASS certificate; the plan correctly treats it as incomplete.
The30 CPU/45 wall/1 GiB/128 MiB file controls and input/source provenance are
explicit. The source does not execute a parent cut, residual matching, or
spanning child construction.
