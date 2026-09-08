# Exact CRT-914 radius-two interface for the C106 SSSSS support

Date: 2026-07-30  
Lane: AD  
Status: **proved and independently replayed for the frozen source-relative equality catalogue**

## 1. Combined residue theorem

Let (S) be the frozen 662-seam fractional support. The authenticated support
certificates give two corrected edge residues:

- \(\rho_e\in\mathbb Z/2\mathbb Z\), zero on (S), with desired SSSSS total one;
- \(R_e\in\mathbb Z/457\mathbb Z\), zero on (S), with desired total one.

Define the unique CRT lift in \([0,914)\) by

\[
 q_e=R_e+457\delta_e,
 \qquad \delta_e\equiv\rho_e-R_e\pmod2,
 \qquad \delta_e\in\{0,1\}. \tag{1.1}
\]

Then every integral endpoint-balanced C106 SSSSS selection satisfies

\[
 \boxed{\sum_{e\notin S}q_ex_e\equiv1\pmod{914}}, \tag{1.2}
\]

and (q_e=0) on every support seam. This follows immediately by reducing
(1.2) modulo 2 and 457 and applying the Chinese remainder theorem.

The authoritative mod-457 input is
`scratch/ad_k16_c106_sssss_radius1_mod457_separator_v2_20260730.audit.json`,
SHA-256 `e2fa6fa2fe42152566af9a771b029af3b1977f1b61e62dfe58527b500ed35aff`.
The mod-2 input is
`scratch/ad_k16_c106_sssss_support_parity_escape_20260730.audit.json`,
SHA-256 `d44c78780df5be82808d42f61ce1337f0f3cb18cde307f0222cf30a52c8705f5`.

## 2. Endpoint quotient and exact two-edge normal form

Contract each connected component of the undirected support graph. The three
support classes are:

| class | minimum port | vertices | support seams |
|---:|---:|---:|---:|
| 0 | 140 | 565 | 656 |
| 1 | 4363 | 2 | 2 |
| 2 | 6491 | 4 | 4 |

Every non-support port (v) is retained as singleton class (3+v).

### Lemma 2.1 (two-edge quotient balance)

Two distinct outside seams have endpoint imbalance completable by a signed
integral support flow if and only if their quotient arcs either:

1. are both loops, each lying within a support component; or
2. form a directed 2-cycle between the same two distinct quotient classes.

Necessity follows because support edges move no net incidence between quotient
classes. Conversely, zero quotient incidence leaves an integer zero-sum demand
inside each connected support component, and a support spanning tree realizes
every such demand integrally.

The two outside seams themselves respect endpoint capacity one exactly when
their raw tails are distinct and their raw heads are distinct. This statement
does not assert capacity one for the later support completion.

### Theorem 2.2 (complete radius-two structural interface)

For distinct outside seams (a,b), the following are jointly equivalent to
the CRT equation, quotient endpoint balance, outside-edge capacity one and the
nonnegative slack-five budget:

1. (s(a)+s(b)\le5);
2. (q_a+q_b\equiv1\pmod{914});
3. their raw tails are distinct;
4. their raw heads are distinct;
5. both are quotient loops, or they form a directed quotient 2-cycle.

This is exact for the stated interface. It is only necessary for the full
service lattice and physical carrier model.

## 3. Compact catalogue and exact census

The authoritative seam catalogue is
`scratch/ad_k16_c106_sssss_crt914_outside_slack5_v2_20260730.tsv`, SHA-256
`da46d259648bf01db3b678cfafca857a49cac79c47f05e5abb3de90b457bb69e`.

It has 210,763 data rows and eight columns:

```text
seam_id  slack  q  tail_port  head_port  tail_class  head_class  topology
```

It is sufficient to enumerate Theorem 2.2 without reopening the binary seam
ledger and is not a raw pair dump. Exact seam counts are:

- slack histogram (0,\ldots,5): ((40884,33339,74854,29927,30191,1568));
- 645 quotient loops and 210,118 quotient arcs;
- 560 nonempty loop buckets and 210,018 nonempty directed-arc buckets.

Bucket counting and an independent explicit replay both give exactly 208
unordered structural pairs:

\[
 \boxed{204\text{ loop--loop pairs}+4\text{ directed 2-cycles}=208}. \tag{3.1}
\]

Their slack-sum histograms for sums (0,\ldots,5) are respectively

\[
 (7,9,37,48,73,30),\qquad (0,0,0,2,1,1). \tag{3.2}
\]

No pair dump is frozen. The SHA-256 of the sorted canonical 208-pair set is
`55d24bcc086ceea1941759958cbac79b8212a272e7ee2a34f1cf51b67cd696a7`.

Nonnegativity and exact-once service additionally require

\[
 H(a)\cap H(b)=\varnothing. \tag{3.3}
\]

An independent raw-ledger replay finds that all 208 structural pairs already
satisfy (3.3): 208 survive and zero are rejected. Thus target-disjointness is
necessary but gives no further reduction on this bank. Pair hashes use
unordered seam-ID pairs: each pair is stored as
`(min(seam_a,seam_b),max(seam_a,seam_b))`, then the list is sorted
lexicographically before hashing.

## 4. Frozen artifacts

- Builder:
  `scratch/build_ad_k16_c106_sssss_crt914_radius2_interface_20260730.py`,
  SHA-256 `a7460f69f305d3a363f7b3d557f615999dde994979d6e51847f1c0b3898093c0`.
- Manifest:
  `scratch/ad_k16_c106_sssss_crt914_radius2_v2_20260730.audit.json`,
  SHA-256 `9dce75365e9ce98cd16f8096ea206803e8f83326919cc7b4e01e41ebcc62f4ff`,
  payload `adb22c4a988aa28b21545a5fed645ebe7ea43a740878dffa46e14820d3f417b1`.
- Independent explicit-pair auditor:
  `scratch/audit_ad_k16_c106_sssss_crt914_radius2_pairs_20260730.py`,
  SHA-256 `70bcdc7cb7b57264e20c155e4b323ac72400a213fcc34bc4c6dbc251c264a067`.
- Independent replay:
  `scratch/ad_k16_c106_sssss_crt914_radius2_pairs_replay_20260730.audit.json`,
  SHA-256 `bd33a7a86c27aa45cbc6d9178165e90b065fb633309fa75478a8707820a3c26c`,
  payload `620a816024ed530e6d67a716a4559fa942566805b1661740b1adc769911c14b5`.
- Target-disjoint auditor:
  `scratch/audit_ad_k16_c106_sssss_crt914_radius2_service_disjoint_20260730.py`,
  SHA-256 `58fbf06c9975296fe2e89fe7cd6694299727102b3002eaf1b8d51980862a531b`.
- Target-disjoint replay:
  `scratch/ad_k16_c106_sssss_crt914_radius2_service_disjoint_20260730.audit.json`,
  SHA-256 `d74a1cf145dcf6660772055931f80dff0ede34138e9fe185ff8822f0064c20e0`,
  payload `42bc348d70fcdc4260ea43788d8edcb08718fcada615d1686398bc132910e8f4`.

The independent auditor does not reuse the builder's bucket formulas. It
explicitly checks all loop pairs, isolates reciprocal quotient classes in a
separate TSV pass, checks their cross-products, and reproduces both counts,
both slack histograms and the pair-set hash.

## 5. Boundary and next stage

Proved: the global CRT-914 row, the exact quotient/capacity/slack radius-two
normal form, the complete 208-pair census, and target-disjointness of all 208
pairs.

Not proved: extension of any pair through the full integral support-service
lattice; nonnegative or capacity-one support completion; q1, residence,
separation or connectivity; C106 feasibility; or any floor above 106.

The next exact stage needs only 208 fixed-pair support-completion checks. A raw
radius-two cross-product over 210,763 outside seams is redundant.
