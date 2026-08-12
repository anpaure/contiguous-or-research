# K16 exact229 partial-A plus third-buffer enumerator

Date: 2026-07-30  
Lane: AD, component-level source return  
Status: **complete H100 census; no exact-and-upper-complete carrier**

## Frozen source

Enumerator:

`scratch/search_ad_k16_exact229_partiala_thirdbuffer_20260730.cpp`

SHA-256:

`d89ee4af10ca3883e528814b1ed1c82086e92c096beb27c5afadb9f586ac5c8d`.

Companion inherited primitive source:

`scratch/search_ad_k16_bad2_splitbuffer_pair_20260730.cpp`

SHA-256:

`65abf0532b0bbfced9041cbc3d22b48a66ffc7044525e412c37890a62c36d655`.

The translation unit passes

```text
clang++ -std=c++20 -O0 -fsyntax-only
```

locally.  The enumerator itself has not been executed locally or remotely.

## Fail-closed provenance

Before compilation/execution, the launcher must run `sha256sum -c` from the
repository root on

`scratch/ad_k16_exact229_partiala_thirdbuffer_20260730.INPUTS.sha256`.

Manifest SHA-256:

`0e3031b80891094e4b6a6c3e0629c14eb9793042e6f7ee1712a68b3ac0a72ad7`.

It authenticates both C++ sources and the two input chronologies:

* bad2: `dc336b93f981d09bbba9f44969bef46da51c6feeab595b05c2fd6b26b340638d`;
* exact229: `cae23cfcedbc9d193ebd9191045edd0e5c14f56af5fc96a802b8cefa7cd7e974`.

The binary additionally reconstructs exact229 from full forward
`A=[2186,2217)` followed by fixed reverse `B=[1266,1295)`, compares the whole
12,873-row vector with the supplied exact229 file, and replays exact229's full
middle and unrestricted upper semantics before entering the census.

## Exact catalogue

The packet (A') ranges over precisely the 27 source-exact nonempty
subintervals of `[2192,2214)`, with both orientations.  This is asserted
against the frozen explicit list.  Every such deletion leaves both endpoint
target halos

```text
[2183,2192) and [2214,2223)
```

untouched; the independent restricted-A audit proves that these halos retain
the five exact lower-provider signatures for `091d`, `291c`, `291d`, `2e28`,
and `2f28`.

Packet (B=[1266,1295)) is fixed in reverse orientation.

Packet (C) ranges over every interval satisfying all of:

1. length 1 through 64, both orientations;
2. literal source-gap depth-three replay;
3. its six-row context lies before the first equality, namely
   `C.lo>=6` and `C.hi+6<=6320`;
4. it lies at least six rows from old destination 3846;
5. the inherited strict halo predicate separates it from (B) and from the
   entire protected interval `[2183,2223)`: there is one untouched row beyond
   the six-row dependence radius.

There is deliberately no old `4400/4401` exclusion.  The resulting exact
catalogue has 20,510 oriented (C) packets, asserted in the binary.

For every oriented (A') and (C), all six orders of the three packets are
tested consecutively before old row 3846.  Hence the exact labelled size is

\[
27\cdot2\cdot20510\cdot6=6,645,240.
\]

## Semantic audit

For each arrangement the program:

1. tests every destination-crossing seven-row depth-three identity literally;
2. deletes each of (A',B,C) once and inserts each once, preserving the row
   multiset and length exactly;
3. reconstructs dynamic depths from actual equalities and performs the full
   maximal-envelope middle replay;
4. aborts if local seam legality and full middle replay disagree;
5. enumerates all unrestricted upper interval unions;
6. emits only upper-complete carriers.

Output deduplication is exact.  A double 64-bit digest only selects a disk
bucket.  On equal digest, every prior word in that bucket is reread and all
12,873 rows are compared before declaring a duplicate.  Therefore hash
collision cannot suppress a distinct output.

## Exact completeness boundary

The census is exhaustive only for:

* the frozen bad2 source;
* fixed reverse (B);
* one of the 27 protected interior (A') intervals;
* one strict-halo-separated (C) of length at most 64;
* three consecutive packets at fixed destination 3846.

It does not cover touching/interacting source halos, (C) of length at least
65, a changed (B), nonconsecutive destination placement, a moving cut, or
changed target values.  Therefore a zero-output run would be a scoped
normal-form no-go, not a K16 impossibility theorem.

## Completed census

The source was compiled and run on one H100 CPU core with a 600-second
timeout and 2 GiB address-space cap.  The exact result was

```text
a_intervals=27
a_oriented=54
c_oriented=20510
formal=6645240
destination_pass=2
full_exact=2
upper_complete_rows=0
unique_upper=0
```

The two labelled exact rows are the same physical chronology: singleton
`A'=[2213,2214)` (its two orientations coincide),
`C=[4634,4683)` forward, destination order `ACB`.  Its complete upper-hole
set is

```text
1f3c 1f3e 557c 783b 793b 7c39 7e39.
```

Thus all 6,645,240 formal arrangements in the stated strict-halo face fail
before Hall: only one physical middle-exact word survives, and it has seven
literal upper debts.  The scope boundary above remains essential.
