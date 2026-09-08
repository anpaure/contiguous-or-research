# K16 seven-hole parent: protected fourth-buffer census

Date: 2026-07-30  
Lane: AD  
Status: **complete H100 census; no upper-complete fourth-buffer word**

The frozen source is

`scratch/search_ad_k16_partiala_fourthbuffer_upperrepair_20260730.cpp`

with SHA-256

`ca1ab222707e2ac86f65c99f3a63c3dee2bbc55b1594124c5f1f1f9d44fe0e43`.

It passed a C++20 syntax-only compilation and was not executed locally.
Input/source manifest:

`scratch/ad_k16_partiala_fourthbuffer_upperrepair_20260730.INPUTS.sha256`

SHA-256:

`2cfc96d812f50f54aa88e46876baf775423f3be27cb9998b58effbb22d57e8e9`.

Before enumeration the binary reconstructs from authenticated bad2 the fixed
parent

```text
A'=[2213,2214), C=[4634,4683) forward, B=[1266,1295) reverse,
destination order ACB.
```

It requires exact middle replay, exactly three dynamic flats, capacity 32063,
and exact unrestricted upper-hole set

```text
1f3c 1f3e 557c 783b 793b 7c39 7e39.
```

The fourth packet (D) ranges over every source-exact interval of length at
most 64 in either orientation whose strict six-row halo is disjoint from
(B), (C), and the entire protected source region `[2183,2223)`.  Its
context lies before the first flat and at least six rows from destination
3846.  There are exactly 20,230 oriented (D) packets.  Testing all 24
orders gives

\[
20,230\cdot24=485,520
\]

formal arrangements.

Every destination survivor receives literal full middle and unrestricted
upper replay.  Every exact row is logged with the complete upper-hole list;
every upper-complete word is materialized and deduplicated by an exact disk
comparison.  The strict protected-region exclusion retains the five
source-return ear charts proved in
`THREAD_AD_K16_EXACT229_RESTRICTED_A_ENDPOINT_RIGIDITY_20260730.md`.

The completeness scope excludes touching source halos, (D) of length at
least 65, changed (A',B,C), nonconsecutive packet placement, moving the
destination, and arbitrary row substitution.  A zero-output run therefore
would close only this protected four-packet normal form.

## Completed census

The frozen source was compiled and run on one H100 CPU core with a
600-second timeout and 2 GiB address-space cap.  It returned

```text
d_oriented=20230
formal=485520
destination_pass=42
exact_rows=42
best_holes=7
upper_rows=0
unique_upper=0
```

The 42 exact-middle rows have upper-hole-count histogram

```text
7:6, 8:14, 9:15, 10:5, 11:2.
```

Every one of the 42 rows still misses the six masks

```text
1f3c 1f3e 783b 793b 7c39 7e39.
```

The seventh parent hole `557c` survives in 41 of 42 rows; the exceptional
row creates other holes and still has more than six.  Thus no fourth packet
in the stated strict-halo face repairs even the six-mask invariant core, and
none reaches the Hall stage.  This is a complete scoped no-go, not an
unrestricted upper obstruction.
