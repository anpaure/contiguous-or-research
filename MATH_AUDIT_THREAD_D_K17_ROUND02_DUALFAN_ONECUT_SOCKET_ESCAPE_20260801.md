# Exact one-cut escape audit for the `114930` dual fan

Date: 2026-08-01  
Lane: Thread D, `k=17` dense refinement  
Scope: the frozen `round02` cut bank and its complete one-cut substitution
catalogue.  This note proves neither residence nor any deeper-shadow or
compiler statement.

## 1. Index-free decoding of the two central sockets

The two physical paths called `L3669` and `L3670` in the extracted CNF have
the following invariant owner signatures (masks are decimal):

\[
 P_s:64081\longrightarrow 115442,qquad |P_s|=8,
 \tag{1.1}
\]

\[
 P_t:115696\longrightarrow 115186,qquad |P_t|=2.
 \tag{1.2}
\]

Thus

\[
 s=115442=\mathtt{0x1c2f2},\qquad
 t=115186=\mathtt{0x1c1f2}.
 \tag{1.3}
\]

They are Johnson adjacent and

\[
 s\cap t=114930=\mathtt{0x1c0f2},\qquad
 s\cup t=115698=\mathtt{0x1c3f2}.
 \tag{1.4}
\]

The direct seam is not resident: the `s`-exclusive coordinate has inward
age `4`, whereas the `t`-exclusive coordinate has age `2`; at depth three
the latter is short.  Every seam in the verified extracted core incident to
these two sockets has lower colour `114930`.  Hence the quotient obstruction
is the dual fan

\[
             \{s,t\}\longrightarrow\{114930\}.
 \tag{1.5}
\]

This decoding does not use mutable piece numbers.  The independent source
locates the two paths by the four endpoint owner masks and lengths, and only
then checks that the legacy numbers are `3669,3670`.

## 2. Complete breaker criterion at radius one

Assume a one-cut substitution preserves the zero-265 ledger.  As long as
the invariant paths (1.1)--(1.2) retain endpoints `s,t`, every orientation
of either path still consumes one seam at its central endpoint.  Therefore
the projected dual-fan certificate can be destroyed only by one of:

1. a selected, resident seam of a lower colour other than `114930` incident
   to `s` or `t` (in either directed role);
2. a selected, resident direct `s--t` seam of colour `114930`, which services
   the two sockets with one colour occurrence;
3. a cut substitution which moves one of the invariant central socket roles,
   including deletion of the unique selected `114930` row.

Conversely each event removes the two-socket/one-colour Hall certificate.
It need not make the complete q1 formula satisfiable; it is exactly a
certificate breaker.

To see completeness, observe that changing a remote path without producing
an incident seam leaves the two socket colour neighbourhoods unchanged.
Changing the other endpoint or orientation of `P_s` or `P_t` also does not
remove the central requirement: both orientations use the same central
owner, once as a head and once as a tail.  The only remaining possibility is
literal relocation of that endpoint, which is item 3.

## 3. Exact census and independent replay

Lane L exhausts all `16,667` one-cut substitutions.  Exactly `13,043`
preserve every zero-265 row.  The corrected socket census finds exactly
`12` certificate breakers, all of type 1.  There are no type-2 breakers.
The independent owner-mask replay reproduces the exact zero-265 score, atom
count, selected lower colour, residence test, and directed socket counts for
every row.

| base | old cut | new cut | socket | new lower colour | out | in |
|---:|---:|---:|:---:|---:|---:|---:|
| 540 | 2838 | 2842 | `t` | 115122 | 8 | 8 |
| 3680 | 19815 | 19818 | `t` | 98802 | 6 | 6 |
| 1284 | 6831 | 6832 | `s` | 82674 | 5 | 5 |
| 3613 | 19443 | 19445 | `t` | 115058 | 5 | 5 |
| 1379 | 7364 | 7380 | `t` | 115154 | 4 | 4 |
| 1801 | 9773 | 9771 | `s` | 99058 | 4 | 4 |
| 3254 | 17426 | 17428 | `t` | 49650 | 4 | 4 |
| 1532 | 8180 | 8181 | `s` | 115378 | 3 | 3 |
| 2251 | 12065 | 12067 | `t` | 115170 | 2 | 2 |
| 3029 | 16232 | 16234 | `s` | 115410 | 2 | 2 |
| 3344 | 17953 | 17957 | `t` | 82418 | 2 | 2 |
| 2251 | 12065 | 12066 | `s` | 115426 | 1 | 1 |

The `out/in` columns count directed legal seams, not distinct colours.  The
12 rows give exactly 12 distinct `(move,socket,new-colour)` triples and 92
directed noncore seams in total.

## 4. The colour-removal/role-relocation case

The core colour has no occurrence among the immutable base cuts and exactly
one occurrence among the selected split cuts.  It is cut `9933` in base
piece `1835`.  The sole role-changing substitution is

\[
       1835:9933\;(114930)\longrightarrow 9932\;(115184).
 \tag{4.1}
\]

It moves `t=115186` off the left socket of the old physical path and removes
the selected `114930` row.  Exact replay gives

\[
 (Z_L,Z_{out},Z_{in},Z_{coh},Z_{10})=(0,0,0,1,0).
 \tag{4.2}
\]

Thus (4.1) is not zero-265-preserving and is correctly excluded from the 12
rows.  This also closes the possible indexing loophole: no clean one-cut
move relocates either invariant central socket.

For completeness, the `s`-side base `1834` has nine literal recuts.  Exactly
the incumbent `9924` and recut `9923` pass the zero-265 ledger; both keep
`s=115442` as the same endpoint socket.  The other seven (`9925` through
`9931`) each create exactly one zero lower row.  Thus the central menu has
two clean positions but only one nontrivial clean recut, and neither is a
role escape.  On the `t` side, (4.1) is the only alternative and has the
coherent-orientation failure (4.2).

## 5. Consequence

The earlier provider-only statement is strictly insufficient: radius one
does contain twelve non-`114930` socket escapes.  Hence one may not infer
that a C6/C8 or two-cut move is necessary from stability of the `114930`
provider degree.

All twelve complete q1 formulas were subsequently DRAT-verified UNSAT.  The
exact manifest is:

| i | q1 CNF SHA256 | DRAT SHA256 | core clauses | core SHA256 |
|---:|:---|:---|---:|:---|
| 0 | `a81ff7eea422f6cde20d266ad219a3d97b2d49ab8d69e29a0eb05dbd2153e7b3` | `2be12fabdf952af4a80012a12aa7147418e4a3dd3351ee27976591598f4f6313` | 22 | `3ac26da7e6c011cb0a79afca71ad2876bf739bd69fa438f770f2e0b20529c493` |
| 1 | `9a171648b7c85233f7efee410c4ae7d0e37895f4bc24eb783188b54df9bfe3c0` | `7075f42e5952f51f7f9d555b039283a96464810b9fecf442155fc59d3865c61e` | 148 | `f8f6709d20ab158fd72135cf3d72f0faad1947cb61dca1f4350f5c14891b5325` |
| 2 | `18812a00b6446c1a10a4be00e853b1d046e68f56fcd0794e88753a527f95cc92` | `33f41276af07404754df74fbb1538a858548570470b16ae5cb56f45fed3cdf57` | 148 | `0d22eb5d186bb33ee819584ebfaa495d3d017011adc97e41ffaea9306e288037` |
| 3 | `fc39c7d6a665c56cf5e5da09028ad8b1251ac40bcbc7626816d1b6e0953e21e2` | `df06c0151aecf3ccfe621440b5e4f3c335794d755f6037579d12a233aadbfa93` | 148 | `b41f5e3e84070fed4a08b20a995eb137558f88e7f679e5e7ea238766889989a9` |
| 4 | `a69919dc85fa8d8396d395c3069f570385c7b95d0c9f25903a688437b4e78b2d` | `e585159859331da91cf9844b790ebe1232b25e4f4847923fc0db75908b338c0f` | 148 | `9ae6b04ff811230a91ceb362467cab26db30982f223248ae248ba52e38d35891` |
| 5 | `c788cc56948f409728a38542ef8e59135d6bf2cc6dcfd9706690654ad93f65ed` | `8303e816518f0c4ae0987942bd742ce3c1351266720eddbc6843522fa4794513` | 175 | `b3e13736fa6e6fc36f0d43b2f3aa2192299093750e4a8203514f7d224556dc2c` |
| 6 | `1c582e15afcb275cd4beb1985f2f8c91667cd080c3f380283cb9409ae20cbcb0` | `5fef071a39c20ecd986737800722949243a477086f35010649905a03a00c718e` | 41 | `d915a347749fd2047f899d4f7998eebd5192187bfa971d46314a829a5a05380f` |
| 7 | `1928e69c0c38f66a73c576e244974634f35f60e30487d05863c0c4e982bafa4f` | `d8d7488d369ddd45f27bef7290559cb28e7efe8e9cc102bdfa29183939dc79da` | 39 | `67879729f276738584141a6fd08684e9f7b3477bc25f6eacc0328a61a79f7682` |
| 8 | `257f28e346a418f212933e8428256cc7ebd8cf80140514564264ee243de257b5` | `beef263b7df1ba2d17c99dc46791bdd2f39f9a6c3b238f154e65cd98b6c0f528` | 41 | `c7a6908e7527fd546353a1cba48353d9182085c99cebb892ffb67d02905e3c` |
| 9 | `171e42a64ffaf54603e1c09ded5c2f129d15e1d09c0ef4a0c4c5478b5c5eda5f` | `d511ce1efc1aa08d8debdc904ea1ae86b6ea8ba4c54c44ad02bc1a982329bc97` | 148 | `0dd94be3df57b64b795763a1cba48353d9182085c99cebb892ffb67d02905e3c` |
| 10 | `bcc429e982351ef595338a9b9a67661c48405b4828970c1c81197defc5a8c806` | `4bb75a67fa080cdfff301b90dd1077e23b7758ccc82cfd52cc047e0742b71197` | 148 | `f004f566727699bb0fac65ba8dbd44d0b6292e3c223c3bc337026704e0e44a0e` |
| 11 | `8afc0d2966e255d05d91f7adcfe6ac8fe5c32fd02ada8fa8414e92837199093c` | `6c6436702b65f8cbd397b0f846a4d4e70df1fa0cb06dc6dbc08c14cab67176a8` | 148 | `1ba20f0bf55c5306c6dbe639869426ea4eaa710338b80aa1c69c2c9bd17d6c40` |

### Residual-core classification

The owner-mask replay shows that none of the twelve failures is merely the
untouched `114930` fan.  The residual cores fall into four reusable types:

1. Candidate 0 (a `t`-escape) is a new one-colour dual fan of colour
   `118996`.  Its owner graph is the path
   `119508--127188--119004--119028`; the forced sockets are the two
   nonadjacent requirements at `127188` and `119028`.
2. Candidates `1,2,3,4,9,10,11` have the same one-colour dual fan of colour
   `115308`: central sockets `115310,119404` see the same five-owner leaf
   bank.  Candidate 5 contains this same 28-seam fan plus one pendant seam of
   colour `117348`; the pendant is not a replacement for either central
   socket.
3. Candidates `6,8` have the same two-colour bow tie with colours
   `35275,35786` around socket `35787`.
4. Candidate 7 has the analogous smaller two-colour bow tie with colours
   `31844,32352` around socket `32356`.

In particular, an `s`-escape and a `t`-escape can land in the identical
`115308` core (candidates 2 and 1 respectively).  Pair search should therefore
price the residual named colours/sockets above, rather than merely pairing
one repair on each side of the original `114930` fan.

## 6. Reproducible files

Inputs and Lane-L census:

- `scratch/l_k17_dense_q1_cegar_20260801/round02.bank.tsv`;
- `scratch/threadD_k17_mask114930_core_20260801/round02.socket_escape_v2.tsv`;
- `scratch/threadD_k17_mask114930_core_20260801/round02.socket_escape_v2.out`.

Independent decoding/replay:

- `scratch/audit_threadD_k17_round02_dualfan_owner_masks_20260801.cpp`;
- `scratch/audit_threadD_k17_round02_dualfan_socket_escape_20260801.cpp`;
- `scratch/threadD_k17_mask114930_core_20260801/round02.socket_escape.independent.tsv`;
- `scratch/threadD_k17_mask114930_core_20260801/round02.socket_escape.independent.audit.json`.

DRAT cores and owner-graph classification:

- `scratch/l_k17_dense_q1_cegar_20260801/proof_manifest.tsv`;
- `scratch/threadD_k17_round02_socket_escape_cores_20260801/cores.summary.tsv`;
- `scratch/threadD_k17_round02_socket_escape_cores_20260801/owner_core_classification.tsv`;
- `scratch/audit_threadD_k17_round02_escape_core_owner_graph_20260801.cpp`;
- `scratch/threadD_k17_round02_socket_escape_cores_20260801/escape00.owner_graph.tsv`;
- `scratch/threadD_k17_round02_socket_escape_cores_20260801/escape02.owner_graph.tsv`.

The replay status is
`PASS_THREADD_K17_ROUND02_DUALFAN_SOCKET_ESCAPE_REPLAY`.
