# The cyclic second-cut provider gate for the `k=17` GK tail

Date: 2026-07-31  
Status: exact finite structural census and supported-provider Hall scan.  The
adjacent-cut representatives `s=1,16` pass the unrestricted
rank-six/rank-eight Hall gate; the displayed perfect provider matching is not
itself a physical ear packing, and the natural length-`3/4` schedule is
solver-free impossible.  No `k=17` word or upper bound is claimed.

## 1. The shifted two-pivot forests

For a rank-six mask `c` on the cyclic coordinate set `Z_17`, let `p_s(c)` be
the last-maximum Greene--Kleitman pivot in the cyclic order starting at `s`.
For `1 <= s <= 16`, put an edge

\[
  c\cup\{p_0(c)\}\;--\;c\cup\{p_s(c)\}
\]

whenever the two pivots differ, and call the resulting rank-seven graph
`F_s`.  Each pivot map is injective, so every vertex has degree at most two.
The exact finite replay additionally proves that every component of every
`F_s` is a path.

Rotation by `-s` sends the two pivot shores `(p_0,p_s)` to
`(p_{17-s},p_0)`.  It therefore gives a literal, colour-preserving-up-to-
rotation isomorphism

\[
                         F_s\cong F_{17-s}.          \tag{1.1}
\]

Thus only `s=1,...,8` need independent provider computations.

For each path and every available width `w=2,...,8`, take the union of `w`
consecutive rank-seven vertices.  Exact enumeration proves that these unions
all have rank `6+w` and are pairwise distinct, globally across all components.
In particular, the rank-eight edge bank and rank-nine internal-turn bank are
injective for every shift.

## 2. Exact structural and scalar census

Write `e_s,v_s,c_s` for the edge, nonisolated-vertex and component counts.
The nonisomorphic representatives have:

| `s` | `e_s` | `v_s` | `c_s` | internal turns | unused rank-7 | missing rank-6 |
|---:|---:|---:|---:|---:|---:|---:|
| 1 | 3640 | 7280 | 3640 | 0 | 12168 | 8736 |
| 2 | 5278 | 8918 | 3640 | 1638 | 10530 | 7098 |
| 3 | 6916 | 11557 | 4641 | 2275 | 7891 | 5460 |
| 4 | 7982 | 12623 | 4641 | 3341 | 6825 | 4394 |
| 5 | 8916 | 13975 | 5059 | 3857 | 5473 | 3460 |
| 6 | 9520 | 14579 | 5059 | 4461 | 4869 | 2856 |
| 7 | 9956 | 15180 | 5224 | 4732 | 4268 | 2420 |
| 8 | 10152 | 15376 | 5224 | 4928 | 4072 | 2224 |

The row for `17-s` is identical to that for `s` by (1.1).  Since each graph
is a forest, `v_s=e_s+c_s`.  Consequently the proposed tail dimensions
telescope for every shift:

\[
\begin{aligned}
 I_s&=16911-v_s,\\
 A_s&=c_s-1,\\
 N_s&=16910-e_s,\\
 N_s-(12376-e_s)&=4534.
\end{aligned}                                                   \tag{2.1}
\]

Here `I_s` is the inserted-owner budget, `A_s` the number of joining ears,
`N_s` the number of new edges, and the last line is the unavoidable number
of repeated rank-six payloads after every missing rank-six colour is served.
Equation (2.1) is arithmetic only; it does not pack ears.

## 3. Shift-parametric supported-provider theorem

For a fixed `F_s`, classify its degree-one vertices as old endpoints and its
unused rank-seven vertices as possible internal ear vertices.  Form every
Johnson edge on those vertices which

1. avoids the retained rank-eight bank;
2. has fresh forced boundary turns at old endpoints; and
3. does not directly close one seed component.

At every unused vertex retain only pairs of incident edges forming a fresh
rank-nine turn with distinct local boundary turns.  Repeatedly delete a wedge
whose edge is gone and an edge lacking a surviving wedge at an unused end.
Call the greatest fixed point `A_s^*`.

Make a bipartite graph `B_s` from missing rank-six colours to fresh rank-eight
colours, joining `c` to `q` when an edge of `A_s^*` has intersection `c` and
union `q`.

### Theorem 3.1

Any locally clean arbitrary-length ear completion of the immutable forest
`F_s` with distinct new rank-eight colours induces a matching of `B_s`
saturating every missing rank-six colour.

### Proof

The chosen edges and their chosen wedges form a post-fixed subsystem of the
monotone support operator, hence survive in its greatest fixed point.  Choose
one carrier edge for each missing rank-six colour.  Its rank-eight union is a
neighbour in `B_s`, and global rank-eight injectivity makes these neighbours
distinct.  This is the required matching. \(\square\)

## 4. Complete cyclic Hall scan

Exact support peeling and independent matching replay give:

| representative `s` | left rows | right colours | incidences | zero rows | rank | deficiency | DM `L/R` |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 8736 | 13817 | 272992 | 0 | **8736** | **0** | 0/0 |
| 2 | 7098 | 13741 | 240187 | 550 | 6459 | 639 | 1384/745 |
| 3 | 5460 | 8730 | 131567 | 220 | 5208 | 252 | 522/270 |
| 4 | 4394 | 9136 | 116616 | 520 | 3794 | 600 | 1282/682 |
| 5 | 3460 | 7910 | 66501 | 232 | 3199 | 261 | 499/238 |
| 6 | 2856 | 7221 | 57843 | 432 | 2365 | 491 | 989/498 |
| 7 | 2420 | 6714 | 36427 | 360 | 2046 | 374 | 444/70 |
| 8 | 2224 | 6530 | 33564 | 416 | 1780 | 444 | 584/140 |

Therefore `s=1` and its rotation `s=16` are the only shifts which pass this
necessary provider gate.  The fixed-`s=9` Hall obstruction is not invariant
under changing the second cyclic cut.

For `s=1`, a materialized file lists all `8736` provider rows and one explicit
perfect matching.  An independent implementation materializes all
`20,973,132` raw wedges, repeats the fixed-point peel, obtains `454,930`
active edges and `20,772,564` active wedges, reconstructs the exact
`272,992`-incidence relation, recomputes matching rank `8736`, and validates
every displayed matched pair.

## 5. The first physical-capacity obstruction

The explicit perfect matching proves only a colour transversal.  Its unique
carrier edge for `(c,q)` has the two rank-seven endpoints strictly between
`c` and `q`.  On these `8736` carrier edges the induced degree histograms are

\[
\begin{array}{c|rrrr}
 &0&1&2&3\\\hline
\text{old endpoint}&3091&3417&730&42
\end{array}
\]

and

\[
\begin{array}{c|rrrrr}
 &0&1&2&3&4\\\hline
\text{unused vertex}&4564&3281&3806&492&25.
\end{array}
\]

Thus `772` old endpoints exceed their capacity one, `517` unused vertices
exceed capacity two, and the maximum selected degree is four.  The selected
carrier graph has `3066` nontrivial components: `2796` unbranched acyclic
components, `261` branched acyclic components, and nine cyclic components,
all nine of which are also branched.  It is not a physical ear packing.

There is a particularly simple exact scalar schedule for `s=1`.  If all
`3639` ears have length three or four, then

\[
 x_3+x_4=3639,qquad 2x_3+3x_4=9631,
\]

so necessarily

\[
                       (x_3,x_4)=(1286,2353).        \tag{5.1}
\]

It has `7278` endpoint--unused edges, `5992` unused--unused edges and no
endpoint--endpoint edge.  Filter the authenticated supported-provider
relation by deleting precisely those options whose two carrier endpoints are
both old endpoints.  The raw type counts and filtered result are

\[
\begin{array}{c|rrr}
\text{carrier type}&EE&EU&UU\\\hline
\text{supported incidences}&20655&66574&185763,
\end{array}
\]

and

\[
\begin{array}{c|c}
\text{filtered incidences}&252337\\
\text{filtered rank-eight resources}&11947\\
\text{literal zero rank-six rows}&572\\
\text{matching rank}&8164/8736.
\end{array}                                                    \tag{5.2}
\]

Every nonzero row can be matched, so the canonical DM witness is exactly the
`572` zero rows against the empty neighbourhood.  By Theorem 3.1, every new
edge in the natural schedule is `EU` or `UU`; hence any missing colour among
those `572` would need a provider which does not exist even in the greatest
locally supported relaxation.  Therefore the exact schedule (5.1) is
impossible on the immutable `s=1` forest, and by rotation also on `s=16`.

This does not close arbitrary-length adjacent-cut ears.  Allowing direct
length-one `EE` ears restores the full provider graph, after which a genuinely
joint rank-six/rank-eight/rank-seven-capacitated transversal, compatible
wedges, filler edges, global rank-nine freshness and quotient topology remain
open.

## 6. Exact forced-direct core and the residual gate

The `572` rows in (5.2) force at least `572` direct `EE` ears.  The smallest
simple scalar ledger using exactly those forced direct ears is

\[
                         (x_1,x_4,x_5)=(572,2637,430).           \tag{6.1}
\]

Indeed it has `3639` ears, `9631` inserted unused owners, `13270` new edges
and `16909` new turns.  Its edge-type totals are

\[
                         EE=572,\qquad EU=6134,\qquad UU=6564. \tag{6.2}
\]

Restrict each exceptional row to its direct providers.  This gives `3861`
options on `1001` fresh rank-eight colours and `1573` candidate base
endpoints.  The exact packing problem is

* one option for every exceptional rank-six row;
* capacity one on its rank-eight union; and
* capacity one on each base endpoint.

It has an explicit integral solution.  Independent literal replay verifies

\[
 572\text{ distinct rank-eight colours},\quad
 1144\text{ distinct base endpoints},\quad
 1144\text{ distinct boundary rank-nine turns}.                \tag{6.3}
\]

The `1144` endpoints lie in `1144` distinct seed-matching components.  Hence
the direct ears form a quotient matching: `572` components of order two and
`2496` isolated seed components, with no quotient cycle.  Exactly `6136`
base endpoints remain unused; the `3067` long ears in (6.1) must use `6134`
of them and leave the final two endpoints.

After charging this fixed direct bank, the residual supported-provider graph
has

\[
\begin{array}{c|c}
\text{rank-six rows}&8164\\
\text{fresh rank-eight resources}&11906\\
\text{incidences}&242771=57008\ (EU)+185763\ (UU)\\
\text{zero rows}&0\\
\text{ordinary matching rank}&8164.
\end{array}                                                     \tag{6.4}

Thus the direct core clears colour, base-port and local two-boundary-turn
capacity, and the residual ordinary colour matching also passes.

An exact residual capacitated selection is also now known.  It chooses
`3065` `EU` and `5099` `UU` provider edges, with distinct rank-eight colours,
old-endpoint capacity one, unused-vertex capacity two, and all `3065`
remaining endpoint boundary turns distinct from each other and from the
direct bank.  Its degree data are

\[
\begin{array}{c|rrr}
&0&1&2\\\hline
\text{remaining old endpoints}&3071&3065&0\\
\text{unused vertices}&4416&2241&5511.
\end{array}                                                     \tag{6.5}
\]

Consequently the `4534` repeated-colour fillers must have exact type counts

\[
                         3069\ (EU),\qquad1465\ (UU),           \tag{6.6}
\]

and exactly `1879` currently zero-degree unused vertices must be activated.
This closes the marginal rank-six/rank-eight/rank-seven capacity gate, but
not the physical one.  Among the `5511` currently degree-two unused centres,
`17` selected edge pairs are not legal wedges.  Of the remaining `5494`
centres, central rank-nine turns have `1503` repetition units and `261`
additional collisions with the boundary-turn bank, for total current
rank-nine collision debt `1764`.  The provider graph together with all
`3640` seed edges has maximum degree two, `2660` components and cycle excess
four, realized by four cyclic components.

If alternating reassignment removes the wedge/turn defects and the four
cyclic components without changing the capacity vector, the clean provider graph has
`2656` path components.  Adding the `1879` new unused singleton vertices
gives `4535` nodes, and the `4534` filler edges in (6.6) must form a spanning
tree.  With final degree at most two, that tree is automatically one path
with exactly two old endpoints.  This port-Hamilton/fresh-turn problem is the
live exact gate; the particular `x_4/x_5` segmentation in (6.1) need not be
preserved during the final path construction.

## 7. Authenticated artifacts

Structural scan:

```text
scratch/audit_h2_k17_cyclic_second_cut_scan_20260731.py
SHA-256 267c92a6e191f555307ac249a6bdc45527906be6880cf8f8079cb27a8da0b26e

scratch/h2_k17_cyclic_second_cut_scan_20260731.audit.json
SHA-256 223303227ecc142fea38a63ad33efef323e62f836ca830798c1c877dac8cbe2c
canonical payload b96118f31730ba4d62e102b296a053b64284381f875df4db800dfc7503bcb4d0
```

Hall scan and aggregate audit:

```text
scratch/h2_k17_cyclic_supported_hall_20260731/frozen_generator.cpp
SHA-256 e2a48fd41b0359d48735ca333a38d2c259c0d0f78e02130c081e4a96332a4546

scratch/audit_h2_k17_cyclic_supported_hall_20260731.py
SHA-256 3a629fa937e583e97b86ac967e9fa61961ad412e7ab97d7312ac0162c5a834e9

scratch/h2_k17_cyclic_supported_hall_20260731.audit.json
SHA-256 13001dc1f7787c11f8fcc0f3dc34b419d5ab1864ee2abb3deca3d4445cf6b14b
canonical payload d3c0951ba69e060abed39703bcabb916f7992e33cb286699a7da5775ef28b1b9
```

Explicit matching and independent materialized-wedge verifier:

```text
scratch/h2_k17_cyclic_supported_hall_20260731/shift01.providers.tsv
SHA-256 6b2d9802d028cca79064278a65020d8ec28e3cc1b04d59c518d29b66b1a68e97

scratch/h2_k17_cyclic_supported_hall_20260731/frozen_materialized_verifier.cpp
SHA-256 0885204b906eeec41f255bfb9cf4b96c3d1435e7fd691f34e8f6a280bc9b8406

scratch/h2_k17_cyclic_supported_hall_20260731/shift01.independent.audit.json
SHA-256 bef31aae59ed7c30ae8b1589d21dad98fa9cf73ad9d76c60140dab84359aa587
```

Natural-schedule `EE` filter and independent matching:

```text
scratch/audit_h2_k17_shift1_noee_provider_gate_20260731.py
SHA-256 9a35fa45fc0255044aab8326e0074ea5f320915d12e00239f36397d24322daf7

scratch/h2_k17_shift1_noee_provider_gate_20260731.audit.json
SHA-256 7661dda7837f5da584876d72057d72cbace6ea25c232d1e60784821a07715d60
canonical payload 73b392ef204a58f9eccd85330fa5334316ef0b797bfb0e4e727ab3f42be9b291

scratch/h2_k17_shift1_noee_zero_rows_20260731.txt
SHA-256 705e0139b344927d26cfcc98ae3015b6ca8b7e238b5dda729eed4ecb8731b884

scratch/h2_k17_shift1_noee_matching_20260731.tsv
SHA-256 332b0241ace912af6d25bf5c93fdd6f5a580ef4a39b7b2b90fa8c3e369a5e851
```

Forced-direct bank and independent replay:

```text
scratch/independent_k17_gk_shift1_exceptional_bb_20260731.tsv
SHA-256 7abcbd84c926a4b6fb7154b2b2554d07282508eae10e7b411e2b9a2217231b8d

scratch/independent_k17_gk_shift1_exceptional_bb_solver_20260731.audit.json
SHA-256 c158086da97fd84f60fae3583b72e7618267392fe7fc60eef1f0eae0828ada17
canonical payload 43d53307bc5390af2bee701d8def373f64a1f6b437c3b0477d518697557eb234

scratch/audit_independent_k17_gk_shift1_exceptional_bb_20260731.py
SHA-256 cb5d02279a96999978cafafda64590e6143a1578e8e31b66c016b3e405152855

scratch/independent_k17_gk_shift1_exceptional_bb_replay_20260731.audit.json
SHA-256 093320445d2178cda408cdbea6255a3a6784fa820fc94e569b99d9f123e51353
canonical payload 9b9c6825c7629fd2c40f99973f49833adab649d6cee4f7e3bca97249f5d212d2
```

Residual capacitated selection and independent defect replay:

```text
scratch/independent_k17_gk_shift1_residual_cap_20260731.tsv
SHA-256 7e5706b65996e6d303108114c69f41c381a8743799da048c928eb9b2e50a47ff

scratch/independent_k17_gk_shift1_residual_cap_solver_20260731.audit.json
SHA-256 7e98c74b8606171d10f2d712b2d107c59e5859e83b52474327dc1a793076e095
canonical payload 9123cb1e37ff9d1baf2bad2ba7caf98ec89aec0b6e5ad1db25f5cb9951e96f32

scratch/audit_independent_k17_gk_shift1_residual_cap_20260731.py
SHA-256 f2ddfdd0d9017189a59e0c5e1c3accf39ce5a6a69165539731a15d5ce1afad47

scratch/independent_k17_gk_shift1_residual_cap_replay_20260731.audit.json
SHA-256 6b9f5389e59d086cadda4be9e7bd146991c050fa1231513097bed7f30b6157cc
canonical payload 952b19f4df8b8a920107448a9b66bc4e1c4d2ee6b5760538933222d23c538ff5

scratch/audit_ad_k17_gk_shift1_residual_cap_topology_20260731.py
SHA-256 c750d371b91e577364013b8bc65029bbc0c1527b9316e32aec54071a880a1679

scratch/ad_k17_gk_shift1_residual_cap_topology_20260731.audit.json
SHA-256 eea2d143f4b3c0fa9476ea7c125e3486a9046792587854a4b6079cd800a7a1a2
canonical payload 8837b6ca82a5910646b03c9f2c2c59f075b3ed7ae13e095cbecd6a3fa0a50b66
```

The scope stops at the stated provider and first physical-capacity gates.
It neither constructs the `13270` new edges nor certifies the prefix,
higher shadows, residence, common-cap compiler, or a length-`24313` word.
