# The authenticated `m=9` SCD multipath carrier: factor cuts and a rank-ten seam obstruction

Date: 2026-08-01  
Status: exact, source-relative finite theorem.  It closes the literal block
face specified below.  It is not a no-go for another SCD forest, another
minimum cut partition, a refinement by additional cuts, or unrestricted
`K17`.

## 0. Verdict

The authenticated flexible-SCD forest has `24,310` distinct rank-nine
owners, `19,448` selected Johnson edges and `4,862=Cat_9` path components.
It cannot be used as `4,862` intact depth-three blocks: only `3,649`
components are images of their isolated maximal depth-three source.

Cutting the exact short owner-run intervals repairs this first failure.  For
the frozen canonical partition

`scratch/h2_k17_m9_multicomponent_20260801/h2_residence_pieces.json`,

the minimum is

\[
       1,419\text{ cuts},\qquad P=6,281\text{ pieces}.       \tag{0.1}
\]

All pieces are isolated maximal-`D3` exact and every coordinate run internal
to a piece's rank-nine owner trace has length at least four.  The cut retains
`18,029=W-P` original Johnson edges.  It therefore leaves `P=6,281` raw
rank-eight lower colours outside the retained `D2` bank.  The generalized
linear compiler ledger is still numerically positive:

\[
 \begin{aligned}
  \text{residual lower targets}&=65,535-18,029=47,506,\\
  \text{singleton/pair cells plus one boundary triple}
      &=48,625+1=48,626,\\
  \text{slack}&=48,626-47,506=1,120=7,401-P.
 \end{aligned}                                             \tag{0.2}
\]

Nevertheless this exact partition has no upper-complete braid.  Cutting
destroys `1,419` distinct rank-ten targets.  Exhausting every ordered pair of
distinct pieces, both orientations, leaves **322** of those targets with no
seam whose concatenated maximal depth-three source even replays.  The same
322 remain unsupported after the owner-run and maximal-`D2` residence tests.
Thus the lower Hall/common-cap master is not reached.

## 1. The isolated maximal-source criterion

Let `R=(R_0,...,R_{s-1})` be a finite rank-nine owner block.  Its maximal
depth-three source is

\[
 E_p=\bigcap_{\max(0,p-3)\le i\le\min(p,s-1)}R_i,
       \qquad 0\le p\le s+2.                         \tag{1.1}
\]

Every source word whose depth-three row is `R` is coordinatewise contained
in `E`.  Consequently `R` is depth-three factorable iff all `E_p` are
nonempty and

\[
                   R_i=E_i\cup E_{i+1}\cup E_{i+2}\cup E_{i+3}.
                                                               \tag{1.2}
\]

Coordinatewise, (1.2) is equivalent to saying that every positive run in the
owner trace which is bounded by zeros on both sides has length at least four.
Boundary-clipped runs may be shorter.  This also proves monotonicity: adding
external rows at either end only intersects the boundary envelopes further,
so an isolated replay failure cannot be repaired by block ordering or caps.

The frozen forest has

\[
       3,649\text{ factorable components},\qquad
       1,213\text{ failing components}.               \tag{1.3}
\]

A four-owner literal core is

\[
 (0x0073f,0x0037f,0x1017f,0x1813f).                   \tag{1.4}
\]

Coordinate `0x00040` has trace `0,1,1,0`.  The maximal source is

\[
 (0x0073f,0x0033f,0x0013f,0x0013f,0x0013f,
   0x1013f,0x1813f),                                  \tag{1.5}
\]

so its second row replays as `0x0033f`, missing `0x00040` from the required
`0x0037f`.  Reversal gives the same defect.

## 2. Exact minimum cut and lower ledger

For one component, associate to every forbidden internal positive run the
interval of owner adjacencies at which a cut destroys its being internal.
These intervals lie on one path.  Greedy stabbing by increasing right
endpoint is minimum, with the usual disjoint-interval packing as its dual
certificate.  Applying this independently to all `4,862` components gives
(0.1).  An independent interval DP obtains the same total `6,281` pieces.

The selected `1,419` cut edges have distinct rank-eight intersections and
distinct rank-ten unions.  Hence the retained palettes have sizes

\[
             19,448-1,419=18,029                    \tag{2.1}
\]

on both shores.  Equation (0.2) is the exact no-seam-repair lower ledger:
the `P-1` inter-piece triples and the unusable opposite linear boundary
account for `P` omitted triple cells; one boundary triple remains in the
compiler bank.  A legal seam which realizes another distinct lower target
can only improve this scalar ledger.  Scalar positivity does not imply Hall
or one common cap.

The exact fixed-order compiler interface, had an upper-complete braid
survived, would be:

1. concatenate the oriented owner pieces and rebuild the global maximal
   source (1.1);
2. require every retained internal `D2` triple to equal its authenticated
   rank-eight intersection;
3. keep every `D3` owner and retained `D2` bit on at least one host;
4. match all `47,506` remaining lower targets into the `48,626`
   singleton/pair/boundary cells using individually legal caps; and
5. intersect all selected caps at each source position and replay every
   owner, retained `D2` row and selected lower cell in that **one** capped
   word.

Marginal Hall without step 5 is not a compiler certificate.

## 3. Rank-ten crossings reduce to one seam pair

### Lemma 3.1

Every physical source interval of OR-rank at least ten and length at least
four equals the union of the consecutive depth-three owner rows wholly
contained in it.  An interval of length at most three is contained in one
rank-nine owner window and therefore has rank at most nine.

### Proof

The consecutive length-four windows cover the source interval exactly; their
OR is therefore the interval OR.  The short case is immediate by containment
in the first or last owner window.  \(\square\)

### Lemma 3.2 (rank-ten seam reduction)

Suppose a rank-ten target `T` is witnessed by an owner interval crossing a
piece seam.  Let `L,R` be the distinct rank-nine owners immediately adjacent
to that seam.  Then

\[
                         L\cup R=T.                  \tag{3.1}
\]

### Proof

Both `L` and `R` lie in the witnessing interval, so `L union R` is contained
in `T`.  Distinct equal-rank sets have union-rank at least ten.  Since `T` has
rank ten, equality follows.  \(\square\)

Thus longer intervals and multiple seams cannot rescue a missing rank-ten
target unless at least one adjacent ordered piece pair already has endpoint
union `T`.  Moreover any globally legal seam is legal under the isolated
two-piece maximal envelope: exterior rows only shrink that envelope.  Hence
the isolated pair catalogue is a necessary superset of every global braid's
seams.

For each of the `1,419` post-cut rank-ten holes, the independent audit
enumerates the ten rank-nine facets of `T`, every oriented piece ending or
starting at one of those facets, and every ordered pair of distinct pieces.
It tests `53,780` candidate endpoint pairs.  Exact results at the three nested
stages are identical:

| seam gate | supported | zero |
|---|---:|---:|
| maximal `D3` source nonempty and exact replay | 1,097 | **322** |
| plus owner-run floor four | 1,097 | **322** |
| plus maximal-`D2` run floor three | 1,097 | **322** |

By Lemma 3.2, any one of these zero rows rules out an upper-complete braid of
the frozen pieces.  There are 322.

## 4. Audits and hashes

Primary static replay:

* `scratch/audit_h2_k17_m9_scd_multipath_static_20260801.py`;
  SHA-256 `3b301f193ef3837e6bc10b36c01b1806104b46f31d30c7fbd5dedd44cdc46bef`;
* `scratch/h2_k17_m9_scd_multipath_static_20260801.audit.json`;
  SHA-256 `cc2d01bfa7ba8d01be6001eede55bce45757079e8814b8a5a279a76b271250d9`,
  payload `ab3c7645310b62df1fff443b3b5352b0487e718867a71a37b9826e093d0d5a89`.

Independent cut/lower-ledger replay:

* `scratch/audit_h2_k17_m9_residence_piece_lower_ledger_20260801.py`;
  SHA-256 `685b2859aee23c8e7d17338f9ad75ecd5ba9fb9c13db0b75d325bd1b441a75dd`;
* `scratch/h2_k17_m9_residence_piece_lower_ledger_20260801.audit.json`;
  SHA-256 `ca6a7f329eb38f7ecd4c62ee8d43f657b29c9bcbe45fcc6a0624c2d36825523b`,
  payload `945106b306c0400bf4aecfa2cacd54548b0d4cc8add73ee8cf79b4fec46e6fc9`.

Independent targeted rank-ten replay:

* `scratch/audit_h2_k17_m9_rank10_pairwise_zero_provider_20260801.py`;
  SHA-256 `c50adcba3a896d3875e150d9a754e08f4b7cff1373a60b87a83e37aeeef121ec`;
* `scratch/h2_k17_m9_rank10_pairwise_zero_provider_20260801.audit.json`;
  SHA-256 `6e9268af9dc5e98303912bf0a21298d5195a00a0b93ad41f8328d37299d63659`,
  payload `e447d5b0d14e8b954f61f9ca00d756ca80cd4695af9fea41039fbe74849e20b1`.

The canonical piece and post-cut-hole inputs have SHA-256 values

* `9889b94b7d18078986965b5b78290b87b2ce8dde78bfe78b03ac3d9c5ad69f88`;
* `a0f5667bcd1aa5c0736afc7b350d40825ba822bf8496a6669b915669e2d5a098`.

The fixed-braid/compiler checker prepared for any surviving order is

`scratch/audit_h2_k17_m9_fixed_piece_braid_compiler_20260801.py`.

Its SHA-256 is
`ed3a08c4706661f245cfcf2aadec5de645705c01641900a859260fc305429964`.

Its Hall semantics are exact for one fixed braid; it was not launched on
H100 because the rank-ten zero-provider theorem closes this face first.

## 5. Scope

Proved infeasible: the authenticated `m=9` SCD forest used intact as `4,862`
blocks, and the specific authenticated `6,281`-piece minimum factor-cut
partition under arbitrary piece order and reversal.

Still open: a different minimum cut partition, more than `1,419` cuts, a
value-changing/non-SCD rethread, another SCD forest, and unrestricted `K17`.
No lower Hall, common-cap infeasibility, or unrestricted no-go is claimed.
