# Canonical K17 deficiency-21 DM geometry, exact cut credit, and the common/common no-go

**Date:** 2026-08-03  
**Status:** exact theorem and SHA-bound exhaustive audit on the canonical
drop-12 parent. This proves a necessary-cut no-go for the parent-local
exact-common modes; it does not replace child-local maximum-matching
certification and does not assert a K17 word.

## 1. Frozen state and full DM decomposition

The fixed-final table has SHA
`fa49188250bf194c8218d8afb5bf5f9220e4a73fd1267824bc7ed0b2868bbb7c`.
Its hard-head supplier graph has

\[
 |R|=16,898,\quad |E|=74,935,\quad
 \nu(G)=16,877,\quad \delta(G)=21,                 \tag{1.1}
\]

and semantic graph hash `f80fe0c9b65f2471`.

Orient unmatched supplier edges from a hard head to a supplier and matched
edges from a supplier to a hard head. The full alternating digraph has 17,462
strongly connected components:

| DM type | SCCs | supplier vertices | head vertices | unmatched vertices |
|---|---:|---:|---:|---:|
| right-deficient | 25 | 2 | 23 | 21 heads |
| left-surplus | 16,037 | 23,598 | 16,165 | 7,433 suppliers |
| balanced | 1,400 | 710 | 710 | 0 |

Nineteen hard heads are isolated zero-degree SCCs. The other six vertices in
the right-deficient part form two directed alternating paths:

\[
  13148\longrightarrow12973\longrightarrow12948,
  \qquad
  15103\longrightarrow14851\longrightarrow1490.       \tag{1.2}
\]

The arrows alternate unmatched, then matched. Thus the minimal
maximum-deficiency shore has the following 23 heads and exactly two suppliers.

| row | owner | root | literal target chain | ranks | degree | matched supplier |
|---:|---:|---:|---|---|---:|---:|
| 1154 | 73172 | 7636 | 1236,3540,7636 | 5,7,8 | 0 | - |
| 1160 | 7665 | 7664 | 240,3568,7664 | 4,7,8 | 0 | - |
| 1490 | 75256 | 9720 | 8440,9464,9720 | 6,7,8 | 1 | 14851 |
| 3078 | 17383 | 17255 | 16481,16743,17255 | 4,7,8 | 0 | - |
| 5831 | 30418 | 29394 | 80,13010,29394 | 2,7,8 | 0 | - |
| 5916 | 62550 | 29782 | 13394,29778,29782 | 6,7,8 | 0 | - |
| 6301 | 31664 | 31536 | 2864,15152,31536 | 5,7,8 | 0 | - |
| 6426 | 32480 | 32448 | 3712,16064,32448 | 4,7,8 | 0 | - |
| 8827 | 43836 | 43828 | 35332,43796,43828 | 4,7,8 | 0 | - |
| 11752 | 59034 | 58010 | 25224,57994,58010 | 5,7,8 | 0 | - |
| 12310 | 61152 | 60640 | 224,27872,60640 | 3,7,8 | 0 | - |
| 12691 | 63362 | 63106 | 5634,30338,63106 | 4,7,8 | 0 | - |
| 12693 | 63176 | 63112 | 648,30344,63112 | 3,7,8 | 0 | - |
| 12816 | 64224 | 64192 | 2112,31424,64192 | 2,7,8 | 0 | - |
| 12948 | 66542 | 66414 | 14,65902,66414 | 3,7,8 | 1 | 12973 |
| 13148 | 67534 | 67406 | 66380,66382,67406 | 6,7,8 | 1 | unmatched |
| 15103 | 77048 | 76024 | 73752,75896,76024 | 4,7,8 | 1 | unmatched |
| 15484 | 110342 | 77574 | 77568,77570,77574 | 6,7,8 | 0 | - |
| 16378 | 90598 | 82406 | 81990,82150,82406 | 5,7,8 | 0 | - |
| 16506 | 115672 | 82904 | 81992,82392,82904 | 4,7,8 | 0 | - |
| 17140 | 85968 | 85456 | 65984,83408,85456 | 4,7,8 | 0 | - |
| 18494 | 93244 | 92220 | 75780,92188,92220 | 4,7,8 | 0 | - |
| 22839 | 116980 | 116976 | 51216,116848,116976 | 4,7,8 | 0 | - |

The literal suppliers are:

| supplier | owner | root | chain | ranks | incident Hall heads |
|---:|---:|---:|---|---|---|
| 12973 | 82894 | 66510 | 65998,66510 | 7,8 | 12948 (matched), 13148 |
| 14851 | 79096 | 75000 | 9304,75000 | 5,8 | 1490 (matched), 15103 |

The four 6/9/4 flag masks are, in that order, `0x44`, `0x20000033`,
`0x1020200`, and `0x44`. There are no other incidences into this shore.

## 2. Exact cut-credit identity

Let

\[
 H=\{\text{the 23 heads above}\},\qquad
 S=N_G(H)=\{12973,14851\}.                              \tag{2.1}
\]

Consider any **jointly materialized** family of local modes \(F\). Let
\(D_F\subseteq H\) be the old Hall heads retired by those modes. Complete the
semantic head universe by giving every retired head its own private dummy
supplier, and put

\[
 S_F=N_{G_F}(H\setminus D_F).                           \tag{2.2}
\]

The child neighborhood of the fixed semantic shore is exactly
\(g_F(H)=|D_F|+|S_F|\). Consequently,

\[
 \boxed{\kappa_F(H)=23-|D_F|-|S_F|=21-c_H(F)},          \tag{2.3}
\]

where

\[
 \boxed{c_H(F)=|D_F|+|S_F|-2
        =|D_F|+|G_F|-|C_F|.}                            \tag{2.4}
\]

Here \(G_F=S_F\setminus S\) is the set of new supplier identities and
\(C_F=S\setminus S_F\) is the set of incumbent-supplier casualties.

This score is not additive. For two modes \(i,j\), the exact formula is

\[
c_H(i,j)=|D_i\cup D_j|+
 \left|N_{G_{ij}}\bigl(H\setminus(D_i\cup D_j)\bigr)\right|-2. \tag{2.5}
\]

It is evaluated after both modes are materialized, so it prices cross-mode
head retirement, repeated identities, endpoint overlap, and casualties.

One transfer changes only two supplier rows and retires at most one head, so
\(c_H(F)\le3|F|\) before casualties. At least seven transfers are therefore
required merely to close this 21-unit cut completely. A one-step contraction
to deficiency at most 20 necessarily has \(c_H(F)\ge1\), but that condition is
not sufficient: near-tight shores must also respect their erosion budgets.

There is an exact child-local certification. Let \(M\) be the parent matching,
retain a largest \(M_0\subseteq M\cap E(G_F)\), write
\(|M_0|=16,877-q\), and let \(p\) be the maximum number of vertex-disjoint
\(M_0\)-augmenting paths in the child. Then

\[
 \boxed{\delta(G_F)=21+q-p.}                            \tag{2.6}
\]

Thus exact contraction is equivalent to \(p\ge q+1\). Formula (2.6), or a
fresh maximum matching, is mandatory after the incumbent-cut filter.

## 3. Exhaustive exact-common audit

The canonical catalogue has 3,494 phase-common, occurrence-pin-safe modes.
Exactly 11 touch incumbent endpoints, leaving 3,483 modes literally
applicable to the fixed final. Twenty-six use their own newly created LLR host
as an occurrence witness; this is valid self-support and was retained.

The exact audit rebuilt both changed supplier menus for every applicable
mode and tested every incidence into \(H\). It found:

* no mode retires a member of \(H\);
* no mode creates a new supplier identity for \(H\);
* 3,482 modes leave both old suppliers intact and have \(c_H=0\);
* edge 52847 alone touches an old supplier: it changes row 14851 and destroys
  both of its Hall incidences, so \(c_H=-1\).

The joint resource audit checked all 5,221,318 resource-disjoint pairs:

| joint cut credit | pairs |
|---:|---:|
| 0 | 5,219,031 |
| -1 | 2,287 |
| positive | 0 |

Therefore

\[
 \boxed{\text{No pair of canonical exact-common modes can contract the
 transported deficiency-21 Hall cut.}}                  \tag{3.1}
\]

This is an unconditional no-go for that fixed pair face; it does not use an
additive approximation.

## 4. Forced source-to-helper form

The separately authenticated structural search found 468 one-mode children
of matching rank 16,878:

* 70 retirement sources keep two Hall suppliers and retire one head (67 retire
  row 12948 and three retire zero head 16378);
* 398 actuator sources keep all heads and create a third supplier identity.

The exact source-role replay shows that each actuator supplies exactly one
old Hall head. Across all 468 sources, the affected-head multiplicities are

```text
1154:9, 1160:3, 1490:19, 5831:1, 5916:6, 6426:16,
11752:14, 12310:99, 12691:1, 12693:2, 12816:90,
12948:105, 13148:1, 15103:1, 15484:17, 16378:60,
17140:2, 18494:2, 22839:20.
```

No source reaches heads 3078, 6301, 8827, or 16506. The retained-parent
matching casualty count in (2.6) is \(q=0,1,2\) for respectively 226, 194,
and 48 sources. The exact child Hall shore is `21/1` for 126 sources and
`22/2` for 342 sources. This is the precise def20-to-def19 starting geometry;
there is no single universal child shore that can safely be transported
across all 468 choices.

The first 468-source occurrence run excluded the 23-row cross-phase union in
both phases. It was exact only on that stronger restricted face and, by
itself, did **not** prove unary common-state zero under the true capacity
rule. A subsequent phase-separated replay restored the six
opposite-phase-only opportunities but still removed all 20 incumbent
structural endpoints from the witness bank. Ten of those endpoints are
already-materialized LLR hosts and are valid unreserved long-state providers.

The final host-admitting replay corrects both restrictions. It reserves
the 20 incumbent endpoints phase by phase, retains the exact flag semantics,
and explicitly admits all ten immutable incumbent LLR hosts as witness rows.
It again finds zero common-state survivors among all 468 structural sources.
The primary source, audit, and manifest SHA-256 values are respectively
`ff7c84e8c7701493b31b33d6a4019ac9c873ef697c137a3a31b073c25eff8331`,
`a1b67315af62cbe222aede6e4b9f5dd5a85ebf6100d831f220e8b46bc3c6faf6`,
and `94101008273ed54928cd818daab8142bf03b007fba106477c71009b4d0ffcb03`.
An independent reconstruction admitted the same ten hosts and reproduced the
empty positive ledger byte for byte; its source, audit, and manifest hashes
are `92d929b0aae6a6f7e908b8ad0754e3f02871051ec78daf116094132e4ffcbf1d`,
`22947f62a855bdf32613100f294dcd541b9541ac31db06b04075e8665ba17fde`,
and `860741486619423d87d1f685234f49692fd39a2a7025c2ead72c904cb90c4891`.
Hence unary common-state zero is now exact under the true host-admitting
capacity rule.

Combining only the exact supplier fact with (3.1) gives the unconditional
dichotomy

\[
 \boxed{\text{Any two-mode target-20 candidate contains a non-common
 structural supplier source.}}                         \tag{4.1}
\]

By the authenticated host-admitting unary zero, the second mode is forced to
act as an occurrence helper. An exact-common mode cannot be the supplier
actuator. Edge 52847 additionally spends one unit of source credit unless the
joint child creates a compensating Hall neighbor.

For completeness, the exact receiver predicate is as follows. In phase
\(\phi\), let \({\cal L}_0^\phi\) be the flagged long-state bank. For source
\(s\) and helper \(h\), joint materialization gives

\[
 {\cal L}_{s,h}^\phi=
 \bigl({\cal L}_0^\phi\setminus\{D_s^\phi,D_h^\phi\}\bigr)
 \cup\{H_s^\phi,H_h^\phi\},                             \tag{4.2}
\]

where \(D_x\) is the removed donor LMR state and \(H_x\) the created host LLR
state, with all four flags retained. For each new short \(x\in\{s,h\}\) and
declared state \(\sigma=(q,\alpha,\beta)\), let
\(W_x^\phi(\sigma;s,h)\) be the literal predecessor/successor pairs in
\({\cal L}_{s,h}^\phi\) satisfying incoming, outgoing, and common-five-cell
equations.

The pair passes exactly when common states \(\sigma_s,\sigma_h\) and one
witness from every \(W_x^\phi\) can be selected while preserving fixed rows,
per-phase occurrence capacity, cross-phase flag consistency, endpoint
capacity, and permitted own-host self-support.

Because source \(s\) is certified to have no common state before helper
\(h\) is added, deletion of \(D_h\) cannot create a witness. Hence
every feasible pair uses the newly added helper state \(H_h^\phi\) in some
phase of the source witness. For every source surviving the exact unary
rerun, the pair search is therefore the directed receiver catalogue

\[
 \text{one of 468 supplier sources}
 \longrightarrow
 \text{a helper LLR filling a missing occurrence role}. \tag{4.3}
\]

Every survivor of (4.2)--(4.3) must still be jointly materialized and checked
by (2.6); one-mode credits cannot be added.

## 5. Frozen evidence and scope

Authoritative H100 root:
`/home/amodo/or15/work/k17_def21_hall_geometry_20260803`.

Key hashes:

* `hall_heads.tsv`: `479302b36bf84710d2f5339177d28fd1db86127573646a23009c1bf6252cc5ca`
* `hall_suppliers.tsv`: `5686f140d3ad542a0d5ed2df5dd832cba1427d208ec9dad21cbb6cd217be3abb`
* `hall_edges.tsv`: `d53d8b325c16c2b3ba9071c4ca3f0193af41645e7dc0da7fb1a24b0b76fdd2c8`
* `dm_scc.tsv`: `f0471e168fa81d48eef3122fd5f3f493f1f1132d565d07e96a2274250c3cd04f`
* `common_mode_cut_effects.tsv`: `f528ed3a5e593a955328d167a2a0ca619ad88501e5f431d41da789361ff04a68`
* positive-pair ledger (header only):
  `0c193717d18e285598f051283cfdd6fbe333bece35a100590afdef08a8614740`
* 468 source-role ledger:
  `35b66fdb3f2d9bb30849a995f6b2250ef5dd4cf2856eda6c13b62c8cedd9ae75`

Independent 468-source evidence:

* scores: `84a4475d2d3d445ff8acc827cbf22ce56b539294208ab482ebe4e8e6f4308cb7`
* restricted-union occurrence results (not sufficient alone):
  `21ab1c4f987c54d835306394c86a7aef0b96ead2caeaf31153b9513889a91050`
* restricted-union occurrence audit:
  `01c6c895b823f95281461ce909546f21d20f33ef14bd66e8d0b676e0fda7645e`
* phase-separated but still endpoint-overconstrained unary audit (historical,
  not the final scope):
  `79a4776ab79ec8f44b45fd4374e7bd3cd0d41ddc8daa47152dfc63af88233c0a`
* primary host-admitting source:
  `ff7c84e8c7701493b31b33d6a4019ac9c873ef697c137a3a31b073c25eff8331`
* primary host-admitting audit:
  `a1b67315af62cbe222aede6e4b9f5dd5a85ebf6100d831f220e8b46bc3c6faf6`
* primary host-admitting manifest:
  `94101008273ed54928cd818daab8142bf03b007fba106477c71009b4d0ffcb03`
* independent host-admitting V2 source:
  `92d929b0aae6a6f7e908b8ad0754e3f02871051ec78daf116094132e4ffcbf1d`
* independent host-admitting V2 audit:
  `22947f62a855bdf32613100f294dcd541b9541ac31db06b04075e8665ba17fde`
* final empty-positive ledger:
  `b8fc3ec81082a23d9f86d98b3f51e0a8586a9d1806e8a1c4a49dac7cd43535b5`
* independent host-admitting V2 manifest:
  `860741486619423d87d1f685234f49692fd39a2a7025c2ead72c904cb90c4891`

This closes only the canonical exact-common/common pair face and reduces the
live pair search to a non-common supplier source plus exact partner recourse;
the authenticated source-local common-zero certificate forces directed
rescue through a new partner host. Chronology,
residence, arbitrary upper coverage, common-cap compilation, and the final
K17 word remain separate gates.
