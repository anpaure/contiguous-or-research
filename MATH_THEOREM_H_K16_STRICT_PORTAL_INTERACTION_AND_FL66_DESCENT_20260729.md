# Lane H: strict-portal interaction and the (k=16) failed-literal descent to 66

Date: 2026-07-29  
Status: exact solver-free finite theorem; no (k=16) word claimed  
Scope: fixed resident factor (R), physical q1-complete middle factors, inherited positive-run rows

## 1. Fixed objects and notation

Fix

```text
R = scratch/k16_pbbs_oriented_noaa_softq1_resume1_20260729.json
SHA-256 d28491b708d5a83e8abcde20fda8ad523cd58f9c662f46ae2d9c2507ba73e951
```

and write Φ(Q,R) for the complete two-choice failed-literal potential:
after exact signed-row unit propagation, probe both Boolean values of every
variable occurring in an unhit motif row with exactly two live blue
variables; Φ is the number for which both branches propagate to a
contradiction.  Thus

\[
\Phi(Q,R)>0\quad\Longrightarrow\quad
\text{the fixed }(Q,R)\text{ overlay is infeasible}.
\tag{1.1}
\]

The converse is not asserted.  In particular, Φ is neither Hall
deficiency nor the number of all unassigned variables.

Use the packet labels

\[
\begin{aligned}
A={}&\{(7526,7782),(7526,15714),(15466,15714)\},\\
B={}&\{(47458,63810),(48210,63570),(63570,63810)\},\\
C={}&\{(62050,64034),(62514,63538),(63538,64034)\}.
\end{aligned}
\tag{1.2}
\]

Here (C) is the strongest common single-motif nine-row affine IIS.  The
older 17-row implication packet uses the two distinct motifs (A,B).
These labels are not interchangeable.

## 2. Flag-permutation normal form

For a physical middle edge (e=XY), put

\[
L(e)=X\cap Y,\qquad U(e)=X\cup Y.
\]

The flag ((L,U)), with (|L|=7,|U|=9,L\subset U), determines its unique
physical Johnson edge.  Therefore an exact lower-and-upper-token-preserving
exchange with deleted edges (e_1,\ldots,e_r) has, after occurrence
labelling, added flags

\[
(L(e_i),U(e_{\pi(i)}))\qquad(i\in[r])
\tag{2.1}
\]

for a permutation π.  The crossed flags must be legal, their endpoint
multiset must equal the deleted endpoint multiset, and the alternating
support must have the required connectedness.

### Lemma 2.1 (no nontrivial strict (C_4))

No spanning factor admits a nontrivial connected strict-token two-edge
exchange.

#### Proof

After deleting fixed points of π, the only possibility is a transposition.
Let the two deleted flags be ((L_1,U_1),(L_2,U_2)).  If a crossed flag is an
old flag, the exchange is trivial.  Otherwise legality gives

\[
L_1\cup L_2\subseteq U_1\cap U_2.
\]

The left side has size at least eight and the right side at most eight, so
both equal one rank-eight vertex.  It is an endpoint of both deleted factor
edges, contradicting that the deleted shore of an alternating (C_4) is a
matching. □

For three deleted edges the only connected nontrivial token permutation is
a 3-cycle.  For four deleted edges the possibilities after fixed-point
cancellation are a 4-cycle or two 2-cycles; in the latter case the two token
rectangles must have opposite physical endpoint boundaries.  These cases
give an exhaustive bounded incidence enumeration: enumerate every legal
crossed flag, impose exact endpoint balance, then impose connectedness.

## 3. Complete strict (C_6/C_8) packet census

At zero-unit-core candidate 1, the distinguished targets are all edges of
(A,B,C) and the two affine-support edges

\[
(59438,63526),\qquad(63526,63750).
\tag{3.1}
\]

The exact incidence catalogue has 501,327 legal crossed-token arcs.  The
complete strict (C_6) census contains exactly two moves:

```text
C6_c
delete (43182,59558), (47150,47270), (59438,63526)
add    (43182,47270), (47150,63526), (59438,59558)

C6_d
delete (63526,63750), (63622,63650), (63778,63874)
add    (63526,63622), (63650,63874), (63750,63778)
```

Both touch only the affine support, not a closure edge of (A,B,C).

The complete strict (C_8) census contains exactly two moves:

```text
C8_B
delete (39394,47554), (47458,63810),
       (55714,55746), (63778,63874)
add    (39394,55746), (47458,47554),
       (55714,63874), (63778,63810)

C8_C
delete (27702,30774), (29750,61494),
       (59446,60466), (62514,63538)
add    (27702,59446), (29750,30774),
       (60466,63538), (61494,62514)
```

The first destroys (B) and preserves (C); the second destroys (C) and
preserves (B).  Both preserve the complete lower and upper token
multisets.  Their vertex supports are disjoint, so their union is a literal
simultaneous factor switch.  An independent direct physical meet-in-the-
middle audit, not using the token-permutation implementation, found roughly
21,500--25,800 simple alternating (C_8)'s per distinguished edge and again
found precisely these two strict cycles.

This proves completeness of the displayed strict (C_6/C_8) list within
the stated packet.  It does not exclude non-strict trades that preserve only
q1 support.

## 4. Interaction at candidate 1 and at the old FL73 frontier

At candidate 1,

\[
\Phi=93,qquad \operatorname{Res}=2250.
\]

The strict (C8_B+C8_C) composition gives

\[
(\Phi,\operatorname{Res},\#\mathrm{components})
=(84,2250,4),
\tag{4.1}
\]

destroying both (B,C) while retaining (A).  The 84 double-failing
variables are an exact subset of the original 93: nine disappear and none
is created.  Thus the strict composition is a genuine descent, although not
the best previously known C6 ladder.

The relevant interaction is different at the later exact endpoint

```text
scratch/k16_q1_endpoint_resume1_failedlit73_20260729.json
SHA-256 fa7d6edce1a71012d317220a97e0cf8900dd14d385087ea3a6d920a64d16e513
```

which has Φ=73, 2,240 short runs, and four components.  There are exactly
six unordered pairs of the four strict portals above.  Literal replay gives:

| pair | status | Φ | short runs | components |
|---|---|---:|---:|---:|
| `C6_c+C6_d` | valid | 74 | 2243 | 2 |
| `C6_c+C8_B` | valid | **68** | 2241 | 3 |
| `C6_c+C8_C` | valid | 73 | 2243 | 2 |
| `C6_d+C8_B` | degree-incompatible | -- | -- | -- |
| `C6_d+C8_C` | valid | 73 | 2243 | 1 |
| `C8_B+C8_C` | valid | **68** | 2242 | 1 |

For every valid row, exact degree two, every Johnson edge, and both complete
q1 shores were replayed before Φ was evaluated.  Consequently the former
FL73 frontier is not locally minimal.  Two distinct strict compositions
give FL68; one optimizes residence, while the other is already one physical
cycle.

The connected endpoint is frozen at

```text
scratch/k16_q1_endpoint_fl68_res2242_c1_20260729.json
SHA-256 c7729e0dfbd28f40179e67a855a6bf7e2b47f580591474c042105a554bc8009c
```

and has physical cycle length 12,870, zero q1 holes, 2,242 short runs, and a
complete failed-literal census of 68 on a 967-variable bank.

## 5. The FL68 proof packet and the FL66 descent

At connected FL68 the smallest displayed failed-literal proof has two motif
rows.  One is the old (A) row.  The other has closure

\[
E=\{(40280,44376),(40280,56656),(44370,44376)\}.
\tag{5.1}
\]

Take every blue edge occurring in this 19-row proof: twelve distinct edges
in total.  Orienting a target deleted edge, then alternating through a
Johnson nonfactor edge and one of the two incident factor edges, enumerates
every connected (C_4) and (C_6) through that packet.  The direct census
has exactly eleven q1-support-preserving trades; six destroy (E), and all
six have zero static blocker.

The best move is the alternating (C_4)

```text
delete (40217,40273), (40280,56656)
add    (40217,40280), (40273,56656).
```

It preserves both complete q1 shores, keeps the factor connected, destroys
(E), and gives

\[
\boxed{
(\Phi,\operatorname{Res},\#\mathrm{components})
: (68,2242,1)\longmapsto(66,2241,1).}
\tag{5.2}
\]

The new exact endpoint is

```text
scratch/k16_q1_endpoint_fl66_res2241_20260729.json
SHA-256 501522201cf784be499b251f1c1dc7c0d86f121e53ad470bf5cb2d2ff16507da
physical-edge digest cbe35c7a7b5c16594225ed22454cb2eb243f6177ffc2c4fe9596560663215c51
```

## 6. Exact residual boundary

FL66 is still solver-free infeasible.  Its complete detector data are

```text
unhit two-choice motifs       507
candidate bank               965
double-failing variables      66
smallest displayed row union  23
```

One smallest displayed proof is rooted at blue edge
((52419,54467)) and contains the three literal length-one motifs

\[
\begin{aligned}
M_1&=\{(51433,55497),(51433,59593)\},\\
M_2&=\{(61455,61575),(61511,61575)\},\\
M_3&=\{(50375,52419),(52419,54467)\}.
\end{aligned}
\tag{6.1}
\]

The full blue support of this 23-row proof is

```text
(27843,58563) (29891,61635) (35035,51403) (50375,52419)
(51403,51658) (51433,55497) (51433,59593) (52419,54467)
(52673,60609) (53699,61635) (55491,55506) (55491,55619)
(57543,58563) (59593,60041) (61455,61575) (61511,61575).
```

This is the next exact packet bank.  No overlay, resident completion, COMP3
compiler, or (k=16) word follows from FL66; equation (1.1) certifies the
opposite for the fixed (R).

## 7. Frozen proof artifacts

```text
scratch/k16_common_packet_strict_token_c6_20260729.enumeration.json
SHA-256 1d72c952e2be52ae81470622225549b49b0dc00d9c7dc4a83de8b35fcbf3cc3b

scratch/k16_common_packet_strict_token_c8_20260729.enumeration.json
SHA-256 044419f18dfd6b2e677cddc0133629cf8c5e15d7331f695647099d6ef13cdcd5

scratch/k16_fl73_strict_portal_pairs_20260729.audit.json
SHA-256 8d74a13f4198be0c233fd21c7bcbb946d5b0fe31d2de946fe19570293b6d0107

scratch/k16_fl68_core_q1_c4c6_20260729.enumeration.json
SHA-256 f39cbcbd5db97cc0f574dca0182a40132c71bc79e1a9d3c5cdc4ff3540de5601

scratch/k16_fl68_core_q1_c4c6_failed_literal_potential_20260729.audit.json
SHA-256 94f1c670d9b0b7078f6719497e8ef0359160138e4554ac20e26ba961b2ba07ab

scratch/k16_fl66_res2241_failed_literal_fullbank_20260729.audit.json
SHA-256 5fdff87ec96fdad12a56ad445fe5a8555cc0529df038713141a0c6211091f24a
```

All searches and replays used deterministic local-light combinatorics.  No
SAT/CP solve, H100 launch, GPU job, or web query was used.
