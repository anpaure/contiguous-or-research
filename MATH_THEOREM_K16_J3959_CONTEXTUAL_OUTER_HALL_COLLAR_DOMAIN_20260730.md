# K16 `j3959`: contextual outer Hall collars and the source-compensated embedding gate

Date: 2026-07-30  
Lane: K, cross-lane integration  
Status: **exact destination-local collar theorem; global occurrence embedding remains open**

## 1. Correction being made

The fixed proposed right boundary

```text
4d39 | 0767 076d 027f
```

must not be used constructively.  Coordinate `0002` has trace `0,1,0` on the first three displayed rows, so the middle row `0767` reconstructs at most as `0765` at every positive depth.  This remains a valid permanent rejection rule for that literal adjacency.

The replacement is not another fixed boundary.  It is the authenticated finite domain

```text
scratch/k16_j3959_outer_hall_collar_20260730/local_collars.tsv
```

of contextualized, occurrence-labelled 19-row collars.  The theorem below states exactly what this new domain proves and what it does not.

## 2. Collar normal form

Let \(\mathcal M_3\) be the `2250` members of the `5166` nested-service block atlas which pass the independently audited depth-three internal projection.  Every \(B\in\mathcal M_3\) has the form

```text
B = V0 V1 V2 4a79 4e39 4d39
```

and supplies the four upper witnesses

\[
  ca79<ea79<eb79,
  \qquad 4e79.
\]

Every emitted collar has the occurrence-labelled form

\[
  C=L_4L_3L_2L_1L_0\mid B\mid
  0779,2771,2765\mid R_j\mid E_j,
\tag{2.1}
\]

where the five-row predecessor is selected from the authenticated left-boundary catalogue and \(j\in\{0,1,2\}\).  The three universal right-port tails are

| \(j\) | \(R_j\mid E_j\) | physical indices |
|---:|---|---|
| 0 | `6665 46e5 4ec5 | 5e85 5c95` | `3955,3954,3953 | 3952,3951` |
| 1 | `26e5 06f5 42f5 | 60f5 70f4` | `6356,6355,6354 | 6353,6352` |
| 2 | `a665 c665 c6c5 | ce85 dc85` | `10395,10394,10393 | 10392,10391` |

The shared left port uses physical indices `3753,3752,3751`.

There are `19132` admissible `(block, predecessor)` pairs.  Each extends through all three universal ports, giving

\[
  3\cdot19132=57396
\tag{2.2}
\]

collars, exactly `19132` in each port fibre.  Every block occurs in every fibre.  The number of predecessors per block per port lies in `1,...,14`, with block histogram

```text
1:7, 2:15, 3:43, 4:74, 5:164, 6:144, 7:291,
8:301, 9:428, 10:240, 11:289, 12:198, 13:50, 14:6.
```

The qualifier “three” means three **universal full-domain P+star ports**.  An independent enumeration of all `130` occurrence-disjoint minimal `P=2665` ports finds `11` locally feasible right ports.  Exactly the three displayed ports support the full domain: each gives `19132` collars and reaches all `2250` blocks.  The other eight are partial-domain ports, each giving `120` collars on `120` blocks.  Thus “three” is not a claim that no other local right port exists.

## 3. Exact local replay theorem

For a collar \(C=(T_0,\ldots,T_{18})\), put

\[
  E_p=T_{p-2}\cap T_{p-1}\cap T_p,
  \qquad 2\le p\le18.
\]

For an interval \(I=[a,b)\), let \(U(I)=\bigcup_{p\in I}E_p\).  Let \(M(I)\) contain a coordinate whenever the complete depth-two carrier of that coordinate for some fully contextualized row is contained in \(I\).

### Theorem 3.1 (57,396 exact local collars)

For every catalogue row:

1. the nineteen physical source indices and the nineteen row values are pairwise distinct;
2. every \(E_p\) is nonempty;
3. every row \(T_r\), `2 <= r <= 16`, satisfies

   \[
     T_r=E_r\cup E_{r+1}\cup E_{r+2};
   \]

4. the three distinct interval vertices

   \[
   I_Q=[7,8),\qquad I_P=[14,16),\qquad I_S=[15,16)
   \tag{3.1}
   \]

   satisfy the full individual cell law

   \[
   M(I_X)\subseteq X\subseteq U(I_X),
   \qquad E_p\cap X\ne\varnothing\quad(p\in I_X)
   \tag{3.2}
   \]

   for

   \[
     Q=8000,qquad P=2665,qquad S=0665;
   \]
5. one common local letter vector simultaneously realizes all three interval ORs in (3.1) and still reconstructs every row `2,...,16`.

#### Proof

This is a finite computer-assisted theorem with two independent replays.  Both reconstruct every row from its physical `skip_indices`, rebuild all triple-intersection envelopes, derive mandatory masks from complete coordinate carriers, impose the per-envelope hit condition in (3.2), and replay the common letter vector obtained by intersecting the maximal envelope letters with all three target restrictions.  All `57396` rows pass and there are zero role or simultaneous-replay failures. \(\square\)

The producer selected role layouts

```text
Q 7:8, P 14:16, S 15:16     57,216 times;
Q 7:8, P 14:16, S  2:4         180 times.
```

The stronger audit shows that the fixed layout (3.1) works for all `57396`; the exceptional producer choice was unnecessary.

Rows `0,1,17,18` are exterior context only.  The theorem does not reconstruct them.

## 4. Exact attachment-state quotient

For one coordinate at depth two, a boundary positive run of length at least three needs no exterior support; a run of length two needs the near exterior row; and a run of length one needs both near and far exterior rows.  Applying this coordinatewise gives four required masks

\[
  (L_{\mathrm{far}},L_{\mathrm{near}},
    R_{\mathrm{near}},R_{\mathrm{far}}).
\tag{4.1}
\]

### Theorem 4.1 (finite exterior interface)

The collar domain has exactly `124` incoming far/near requirement states.  Its three outgoing near/far states are

```text
port 0: 1010,0010
port 1: 1800,1000
port 2: 3000,1000.
```

All `124*3=372` Cartesian attachment states occur.  Coordinatewise containment of the four masks (4.1) in two chosen exterior rows on each side is necessary and sufficient to reconstruct every fixed collar row.

This is the exact finite interface which a source-compensated segment braid must use; a raw endpoint-mask join is insufficient.

## 5. Loss-aware Hall scope

The three intervals (3.1) give three distinct right vertices for the local Hall graph.  If the six old private leaf cells are retained, assign `8000`, `2665`, and `0665` to these vertices and the six leaves to their old private cells.  This saturates the canonical nine-target Hall shore.

Moving the nineteen source occurrences can itself damage an old private-cell halo.  An independent occurrence-aware replay charges every such loss and recomputes the nine-target matching:

| result | collars |
|---|---:|
| matching number 9 | 57,216 |
| matching number 8 | 180 |

Each universal port contributes `19072` passing and `60` failing collars, and every one of the `2250` blocks remains represented in every passing branch.  The `180` failures have three local candidate cells but lose too much old-shore supply; they are not valid lossless Hall certificates without an additional repair.

Therefore the proof-safe source-embedding domain is the `57216` loss-aware collars.  The other `180` may still be useful only if the global construction explicitly repairs their lost old cell.

This is still not a full lower-compiler theorem.  Other lower targets may lose cells, and global simultaneous `COMP_d` constraints outside the collar remain unaudited.

## 6. Occurrence and upper-shadow scope

Every collar uses the fixed `M` anchors at positions `3959,4620,4621`.  All collars avoid the source occurrences of `Q`, `P`, `F1`, `F2`, and the two tail-flat pairs.  Exactly `13314` use at least one of the old `L` positions `12823,12824,12825`.

The reserved three-row `6f79` provider

```text
2a79@913, 6a39@4513, 4f19@1633
```

is disjoint from every collar, but it is only reserved: no complete occurrence path has yet placed and replayed it together with a collar.

Consequently these objects are alternative physical embeddings of the six-row `M` service block.  They are not extra packets which may be appended to the frozen post-flat construction of item 2046 without resegmenting that construction.

## 7. Correct replacement for the universal-boundary lane

The exact logical update is:

- retain the `0002` isolated-run theorem as a no-go for the literal adjacency `4d39,0767,076d`;
- retire `0767,076d,027f` as a constructive universal boundary;
- replace it by the `57216` loss-aware contextual collar domain, or by all `57396` rows if old-cell repair is explicitly modelled.

This discharges two destination-local gates:

1. exact replay of every completely contextualized collar row; and
2. a simultaneous three-role local letter assignment for `8000,2665,0665`.

It does **not** discharge source-compensated global embedding.

## 8. Sharp remaining embedding theorem

Let \(C\) be one loss-aware collar and let \(\alpha(C)\), \(\omega(C)\) be one of its `372` attachment states.  A sufficient global embedding theorem must construct one occurrence path which:

1. supplies exterior rows satisfying \(\alpha(C),\omega(C)\), hence reconstructs collar rows `0,1,17,18`;
2. deletes and reconnects all nineteen physical source occurrences while preserving the exact three-flat phase, horizon bounds, and scalar capacity;
3. preserves the four upper witnesses inside `M`, places the reserved `6f79` triple, and preserves every old arbitrary-width upper witness;
4. retains the six private Hall cells or replays the complete nine-target shore and then the full lower matching;
5. extends the collar's local common letter vector to the full global `COMP_d` system.

Under these five hypotheses, the contextual collar upgrades to a complete `j3959` carrier/compiler.  None of the five is implied merely by membership in the local catalogue.  In particular, the collar does not by itself repair the pre-flat donor outdegree isolated in items 2046--2048.

This is the correct finite domain for the ongoing S4 source-compensated embedding search.

## 9. Frozen artifacts

Production catalogue:

```text
scratch/build_k16_j3959_outer_hall_collar_catalogue_20260730.py
SHA256 de228a92ab77ea541055b2c8fd1c6dc97120dcdcbc76a854f812504344f73496

scratch/k16_j3959_outer_hall_collar_20260730/local_collars.tsv
SHA256 d57e379c10b4932307296e056b68107b49dffe9953c3ecc913444b466cb8d5be

scratch/k16_j3959_outer_hall_collar_20260730/local_collars.audit.json
SHA256 ef86d28e3e1062e2749a62fa4bac428b431cbc9fbc78da4d59195219746487c4
payload 9787061030038ac9c3c66f978bcb3560af4c2f28d7bfef60edd4b37064d9433a
```

Independent physical/interval replay:

```text
scratch/audit_k16_j3959_outer_hall_collar_independent_20260730.py
SHA256 b2bc1bd2fab899cb6f0ca694d0a2584f5e51bff553fe9fcae9f93ad765be1d1a

scratch/k16_j3959_outer_hall_collar_20260730/independent_replay.audit.json
SHA256 a6b3761001c6437d4cd11b3ba80fb9b97c72b5e2f4b3dbceea3a5d54aab786d4
payload 211f132262f78be3865f832781a10114c72a50cd876249d9e0ff47e4c4630613
```

Independent full-cell and simultaneous-letter replay:

```text
scratch/audit_k16_j3959_outer_hall_collar_full_cells_20260730.py
SHA256 c428ffc8f2cf494a838e432bb4637d18a7c4a1ec9b4bdb0b49c37e7ee43586f3

scratch/k16_j3959_outer_hall_collar_full_cells_audit_20260730/independent_full_cells.audit.json
SHA256 3636b454c2d026825317c48eb7db6fe09fd368a0ad20b11c90f710b2eb45df1c
payload f00688a211f90ae2b5b8486c92287088c21192df5cb506d91eae259ed4f82ac2
```

Loss-aware Hall and attachment-state audit:

```text
scratch/audit_k16_j3959_p_port_star_join_semantics_20260730.py
SHA256 17d7985c83a4ab67f70523cc712d7fb4d70aadc80821876586a643de880720e5

scratch/k16_j3959_p_port_star_join_semantics_20260730.audit.json
SHA256 df968aca4145caec63430eff1efa48b6f64f8758c9c280c52612bd1a98d7e45e
payload 917c8a2c85452935de17108ee717a309d5a71d5043d18043ab678dae34c6f0fc
```

Right-boundary quotient:

```text
scratch/audit_k16_j3959_alternative_right_boundary_trace_quotient_20260730.py
SHA256 d5b8fb54885ee2d80a7ba0ad14c41e6ff3924d1555c58f2dcdd252fdfe5d1676

scratch/k16_j3959_alternative_right_boundary_trace_quotient_20260730.audit.json
SHA256 940850e1fea4f739d14e3279ececc7be5f1cf3f3041b1f9aeda4033942e8d4cd
payload 5d4fdf0d653ce786f03a5581d91c4bdcb883ab41ebe8aa244756e2f7a89dee6d
```
