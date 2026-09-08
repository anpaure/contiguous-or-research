# K16 second Hall-24 parent: forward-rethread audit

Date: 2026-07-30  
Status: **complete scoped no-go for moved blocks of length at least 13**

## Source

The source

```text
scratch/defect_transport_sparse_bad2_20260730/pass1_hallswap16/hit_14.targets
SHA256 9f78f5ac6bd0348d9309985884ec55c5825dfe1921a71b8f2d47494809910536
```

has exact literal middle replay, 32,063 compiler cells, flats at
`6320,12869,12871`, generalized Hall deficiency 24, and sole unrestricted
upper hole `0x4e7e` (rank ten).

The move class is again

\[
    P X Y Z\longmapsto P Y X Z,
    \qquad |X|\ge13,\quad |Y|\ge1,                    \tag{1}
\]

with every block interior kept forward.

## Endpoint signature

For a rank-ten target, an immediate pair is not sufficient.  At each new
seam the census takes the maximal consecutive run of rank-eight rows lying
below `0x4e7e` and tests whether its OR is the target.  This is necessary and
sufficient for a new witness crossing that seam.  It also covers a witness
crossing both `P|Y` and `Y|X` when the intervening `Y` run is short.  Because
the source lacks the target, every new witness crosses at least one new seam.

The generalized production engine is

```text
scratch/search_k16_h24_forward_block_rethread_20260730.cpp
SHA256 40ed9e4a01d583ef646190354bd28076d024f0a8292d50e3be7ecf4678c25fd0
```

and ran on the H100 host CPU.  It enumerated

```text
9197855 endpoint-signature boundary triples
   1019 literal exact-middle chronologies
     17 exact-middle and unrestricted-upper-complete chronologies.
```

The frozen transcript is

```text
scratch/k16_h24_4e7e_forward_rethread_20260730/run_all.stderr
SHA256 5a86b2f510eba49e737a28175b498c78ee4d7bc0203482c722ca3b05f49adfb2
scratch/k16_h24_4e7e_forward_rethread_20260730/summary_all.tsv
SHA256 85d12726c37776d4e358ed078b32e0f5633df1c6207aeed6cb7e1e01c1fe6dbe
```

Every one of the 17 outputs was then independently replayed for literal
middle equality and all unrestricted upper ORs and passed.  The complete
26,332-target generalized Hall audit gives the deficiency multiset

```text
28,29,30,41,66,69,70,71,110,115,123,124,
6417,8309,9194,9326,10718.
```

The best output is

```text
move (a,b,c)=(140,281,6608), |X|=141, |Y|=6327
scratch/k16_h24_4e7e_forward_rethread_20260730/all/candidate_0.targets
SHA256 26c127dd4a711405237454575e084f9bb7414311ad8cc80186022ac7c1a55433
```

It is exact and upper-complete but has 31,922 compiler cells and Hall
deficiency 28.  Two capacity-preserving outputs exist:

```text
candidate_8: Hall deficiency 30
candidate_9: Hall deficiency 29,
```

so preserving the three flat positions does not preserve Hall 24 either.
The 17 words and their independent Hall JSONs are frozen under

```text
scratch/k16_h24_4e7e_forward_rethread_20260730/all/
```

## Conclusion

No forward-block rethread (1) of this second Hall-24 parent simultaneously
has exact middle replay, complete upper coverage, and Hall deficiency at most
24.  The result is scoped to one move with `|X|>=13`; it does not close a
second compensating rethread, a reversed block, or another parent.
