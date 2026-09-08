# K17 drop-12: exact closure of the S47 residual pair face

## Claim

On the canonical parent

- compressed table `e878bf19654d8478b4552451a3b5c9a54716e1383d2513c59d680091e10b5ffb`, and
- final table `fa49188250bf194c8218d8afb5bf5f9220e4a73fd1267824bc7ed0b2868bbb7c`,

there is no exact two-mode common-occurrence packing in the directed residual
face

\[
  \mathcal D=\{(s,p):s\in S_{47},\ p\in S_{47}\cup Z_{112099},
  \text{ the two transfers have disjoint endpoints}\}.
\]

The authenticated census is

\[
  |\mathcal D|=5{,}268{,}793
  =5{,}267{,}163\ (S\times Z)+1{,}630\ (S\times S).
\]

The `S x S` part contains 815 reversed descriptions of the same unordered
child. Therefore the physical-child census is

\[
  5{,}267{,}163+815=\boxed{5{,}267{,}978}
\]

unique two-mode children.

Consequently no member of this residual pair face reaches the supplier replay
stage. This is an occurrence-face closure, not a supplier-rank claim about a
different face.

This was the last open residual two-mode face in the frozen finite
classification. Together with the already closed H-source and common/common
faces, it leaves no two-mode route from the canonical parent. The next finite
frontier is the irreducible three-mode H-source face, where a surviving source
option must use both helper hosts.

## Lossless reduction

The corrected unary ledger for all 47 S modes has an empty host-admitting
common menu. It already permits the source's newly inserted host and tests all
declared states. Therefore, in any two-mode packing containing a source
`s`, at least one source-role ticket must consume the partner host. If it did
not, deleting the partner donor could only remove available long states, and
the alleged source option would project to a unary host-admitting option,
contradicting the authenticated unary zero.

For each phase, the partner-host aperture screen performs the simultaneous
source/partner donor deletion and host insertion and retains every source
same-key witness compatible with that necessary partner-host use. It also
reserves the 20 incumbent occurrence rows in that phase and preserves the
opposite-phase flag restriction. Hence rejection by this screen is lossless
for exact common occurrence.

The complete directed domain of 5,268,793 endpoint-disjoint pairs produced
only three phasewise necessary survivors:

| source edge | partner edge |
|---:|---:|
| 92903 | 25925 |
| 92903 | 25927 |
| 92903 | 25929 |

The three-row upper ledger has SHA-256
`f3f643bd5740507d7ad14874b74d99bbc2b7d4c1114ed7dde543cd6db5c486cd`.
An upper row is only necessary evidence; its diagnostic bit is not an exact
packing certificate and was not used for pruning.

## Exact three-row replay

The bounded verifier replays exactly those three directed rows. For each pair
and each phase it:

1. deletes both donor long states and inserts all four flag states of both new
   hosts;
2. excludes all 7,213 private ticket rows;
3. reserves 20 incumbent rows per phase, with a 23-row union and 17 shared
   rows;
4. enumerates every physical predecessor/successor tuple for all 90 declared
   keys of the source and partner roles;
5. requires equal declared state across phases separately for each role;
6. enforces phase-local inter-role footprint disjointness; and
7. enforces global cross-phase row-to-flag coalescing.

The exact ledger is:

| source | partner | source p0 | source p1 | partner p0 | partner p1 | exact packing |
|---:|---:|---:|---:|---:|---:|---:|
| 92903 | 25925 | 1 | 1 | 0 | 1 | 0 |
| 92903 | 25927 | 1 | 1 | 0 | 0 | 0 |
| 92903 | 25929 | 1 | 1 | 0 | 0 | 0 |

Thus every necessary survivor fails already because the partner has no
phase-0 tuple. The verifier reports `requests=3`,
`occurrence_positive_pairs=0`, and `source_anchor_options_seen=3`.

Combining the lossless upper implication

\[
  \text{exact packing in }\mathcal D\Longrightarrow (s,p)\in U
\]

with the exact result `U -> empty` proves the claim.

## Frozen identities

Unary and class inputs:

- S47 unary ledger: `8311bb9909d22e8361c50d700909c46ed9e287df1aa2f91842d5328068c6c8c2`;
- unary audit: `78d722f86deadf220bdec233f834481a047f57231db5feda794a4b225bae89ab`;
- unary producer source: `cce8801b06aa232eb387f2334feb133058ea6d73b84429fbe13a163983145200`;
- all-U H/S/Z/N class ledger: `160fd9c41409ef8bc99977efbeae4a5e45b8da4c492792cdb0ba4d7273d9f58c`;
- class producer audit: `0ef424731eff130de4d9af1aae7d58cdf765b5f695c30ad19da624fdf8ed4df6`;
- independent class audit: `aaef0f9c3923800c4ed353b8f8a0f72196c7c9a79c3c04729babe540d8a3a478`.

Upper result:

- upper source: `80042630bbd302620df9c85bb83c6be2ed48f7e3a3f0b1e82fcf9341bb35414c`;
- upper binary: `f9d1c95be1b54ff5232fc270bceed11ac1c3f017c62dccafdf48de5e09b81d50`;
- upper ledger: `f3f643bd5740507d7ad14874b74d99bbc2b7d4c1114ed7dde543cd6db5c486cd`;
- upper audit: `4fc8fe69f6787b15ed27a033e3e0866d40cc5db61a2bab78d7eae2b9e65a7bd1`;
- upper final-manifest file: `5001a00197011073d9629407c1ca5a395c325115cc0230ab78b563cb4ca1756b`.

Exact replay:

- verifier source: `58a04a32f9a282f1aceca20823116ad4c2a1ca578feabb1f69d5b83861a4367c`;
- occurrence primitives: `d19703b6233ea7fee6f113e8e48cd244f8bfabfabc1b22e5bb43dc82c14fb38f`;
- H100 binary: `2b4aa79258dc7b3e3aaab6c4568096a02fb303054bca5068d6026f711cef2a2d`;
- run-input manifest: `293051bce99cbacf1c5147a8fced71884ddf1ed8440eeb7ed16863735ed53e49`;
- exact ledger: `5eb03ef94410cb21fd346fd76226680de766b6aafac626a205449da1ced65b88`;
- exact audit: `324b9bf45a466d1bfdf107772b7abf715e86f6f553253a679e240f6364b49413`;
- output manifest: `e5f606ee2afeb4d6bd85dc5edf788b9e24996f84db7140263dcdc8b4d1b90566`;
- final-manifest file: `bd4451e9804cfb369eff7df5e6ec68fd4a645b1e0151ae41f6859287049fbde8`.

H100 run root:
`/home/amodo/or15/work/codex_019fc39a_k17_s47_exact3_20260803`.

Local frozen output bundle:
`scratch/codex_019fc39a_k17_s47_exact3_20260803`.

## Scope exclusions

This result does not close triples, the H468 supplier-improving source face,
or any face outside `S47 x (S or Z)`. It makes no chronology, residence,
upper, compiler, cyclic-presentation, or K17-word claim. Phase 1 is the
authenticated transported-owner phase, not an independently asserted native
phase-1 realization. The exact zero makes supplier materialization/replay
unnecessary for this face; it does not replace supplier replay for any future
occurrence-positive candidate.
