# R2 audit: compact-v3 + rank11 + union706 + balanced1564 rank12 child

Date: 2026-08-02  
Finite root: `/home/amodo/or15/work/r2_k17_v3_rank11_union706_balanced1564_child_20260802`

The successor uses the independently audited balanced carrier, not the
residence1547 leader, for its upper rows. Its factor and sparse model have
SHA-256 values
`a56ea34a57c05f2993c6999ad2b1f9fde79089dfd8bd94b08e0e4b784329ad7a`
and `35b8f9dd4287c336584ab54b8341e7a3cd1e394086fb0848cb405d6089827c9d`.
A fresh factor/deck verifier recovers 24,310 rank-8 facets and rank-9 owners,
19,448 rank-10 caps, 3,944 protected edges, 1,198 selected optional orbits,
factor/model equality, protected-reference equality, and one physical cycle.
It independently recovers 1,462 rank-11 holes and 238 rank-12 holes, forming
86 and 14 complete `Z_17` target orbits; ranks 13--17 are complete. The
carrier has 1,564 short positive runs and remains nonresident.

The all-phase clean-block producer and an independent semantic replay agree
on the 238 physical rank-12 holes and all 17 phases of their 14 orbits. Each
phase has 220 clean owners. The export has 14 distinct nonempty primary
no-goods, widths 216--309 and 3,918 literals total, backed by 33,575
component/persistent-hole rows and 52,360 exact incidence rows. The row bank
SHA-256 is
`3603b996044f55a4e2c5538c61032741a325956815fb3e13b1a0627fb49adcec`.

The raw union706 bank has SHA-256
`549c9aed6dc3306a580129800251f3b47316e29c4a6d777c60d086628d06c14a`.
Its 706 rows normalize as literal sets to 630 logical clauses; 76 reordered
duplicates disappear. Exactly 562 normalized clauses are already present in
the fixed compact-v3+rank11 parent. The 68-row residence delta has arity
profile `2:3, 3:32, 4:33` and SHA-256
`2c2ea61080a70760fdcf8b20829863c44d78774b4c2fcf73991978bebd650a14`.

None of the 14 clean-block rows collides with the parent or residence delta.
Global numeric lexicographic sorting and deduplication therefore produce an
82-row suffix with SHA-256
`50693a0df72d49add5aea2a3671d9d79fd7d3a2805cda9d7a2486f79ab5afd94`.
The exact child is

```text
p cnf 366131 2037556
SHA256 99d47ce36aa1c8cf14ce17d0e9d1c5908131604fd2f6f6e572831ae207709fce
```

The builder and a separately written whole-child checker verify the complete
parent body as a byte prefix, the complete parent clause-vector prefix, the
canonical 82-row suffix, and exact EOF. The external-input manifest binds the
parent, option map, factor, sparse model, physical-hole and orbit ledgers,
protected reference factor, and raw union706 bank; its SHA-256 is
`24d586a0ca90d7167df1c6a036d4c90a363873a8cb39275bf27f44789aba2a53`.
The full frozen package manifest has SHA-256
`c0ef20839030d2fea81e4e66adaab93d55f6fa492fb5b9f902cbb7a6f6377715`
and passes locally and at the finite root.

No solver was launched on this child. This is an append-only necessary-cut
master and carrier calibration only. It makes no SAT, residence, source,
compiler, opening, exterior-window, regeneration, or word claim.
