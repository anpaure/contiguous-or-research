# Lane-A independent audit of the K16 floor-105 equality elimination

Date: 2026-07-30

## 1. Audited conclusion

Let `G` be the frozen 211,604-seam catalogue with binary SHA-256

```text
832ddd883452e73c0f2462f8550e900d8ffcf01f7397f17b980dd552853b6657.
```

Let the canonical exact scale-two dual be the artifact of SHA-256

```text
29b4aae4bc889e07261725b275455a58583d949932a0eeabf65eae33eb7c460d.
```

Every binary, endpoint-balanced, port-capacitated seam selection in `G` that
services all 93 frozen lower-q2 and upper-q3 defects uses at least 105 seams.

This is an independent proof of the physical floor-105 conclusion.  It does
not use either equality-case CP-SAT verdict.  The repeated-target equality
face is eliminated by two explicit parity locks; the exact-once equality
face is eliminated by a full-CNF LRAT certificate.

The canonical theorem proves the stronger no-port-capacity statement by a
separate compact-DRAT package.  The compact Lane-A LRAT below retains the
physical at-most-one port capacity.  This distinction is deliberate: the
Lane-A proof is sufficient for every separated-port permutation, but by
itself does not establish the stronger uncapacitated relaxation theorem.

## 2. Scale-two ledger and exhaustive equality split

The dual gives positive weights

```text
b_t in {1,2,4},       sum_t b_t = 207,
```

and an integer port potential `y`.  For a seam `e:u->v`, define

```text
s(e) = 2 + y_v - y_u - sum_{t in H(e)} b_t >= 0.       (2.1)
```

Let `x_e` be a binary balanced selection, `C=sum_e x_e`, and let `mu_t`
be target `t`'s service multiplicity.  Endpoint balance cancels the potential
in (2.1), giving the exact identity

```text
2 C = sum_t b_t mu_t + sum_e s(e)x_e
    = 207 + sum_t b_t(mu_t-1) + sum_e s(e)x_e.          (2.2)
```

The exact dual already gives `C>=104`.  If `C=104`, the two nonnegative
integer residuals on the last line of (2.2) sum to one.  Therefore precisely
one of the following holds:

1. every target has multiplicity one and total seam slack is one;
2. every selected seam is tight and exactly one weight-one target has
   multiplicity two, while every other target has multiplicity one.

This split is exhaustive.  In particular, no assumption about CP-SAT
presolve or search enters it.

## 3. A combinatorial parity obstruction to the repeated-target face

Only cycle-eligible tight seams can occur in a balanced all-tight selection.
Raw replay finds 41,491 tight seams and 1,930 cycle-eligible tight seams.  On
each of those 1,930 seams `e:u->v`, the following two coefficientwise
identities hold over `F_2`:

```text
|H(e) intersect T_1| = 1_{P_1}(u)+1_{P_1}(v),
T_1={35044,36935,40066},
P_1={12545,12560,12575};                                (3.1)

|H(e) intersect T_2| = 1_{P_2}(u)+1_{P_2}(v),
T_2={33337,50976,58385},
P_2={12554,12569,12584}.                                (3.2)
```

For each identity, 1,924 seams have both sides zero and six have both sides
one; there are no failures.  The audit artifact records all twelve nonzero
seams explicitly.

Summing (3.1) or (3.2) over any balanced selected circulation cancels the
port-boundary side: every selected incidence at a port occurs once incoming
and once outgoing.  Hence each target triple has even total service.

On equality face 2, if `r` is the repeated target, the service of `T_i` is

```text
3 + 1_{r in T_i}.
```

Evenness forces `r` to lie in both `T_1` and `T_2`.  The triples are
disjoint, a contradiction.  This eliminates all fifteen possible repeated
weight-one targets without port capacity, SAT, or CP-SAT.

The restriction to cycle-eligible tight seams is sound: every seam in a
finite nonnegative balanced selection lies on a selected directed cycle,
hence in a cyclic strongly connected component of the ambient tight graph.
The identities are not asserted on irrelevant non-cycle-eligible arcs.

## 4. Exact-once face: independently checked LRAT certificate

On equality face 1, every selected seam has slack zero or one and exactly one
selected seam has slack one.  Every selected seam lies in a cyclic SCC of the
ambient slack-at-most-one graph.  The exact censuses are

```text
slack-at-most-one seams              74,879
cycle-eligible seams                 15,340
cycle-eligible provider seams         3,399
cycle-eligible slack-one seams        9,203
active ports                           4,695.
```

The deterministic CNF uses one primary variable for each cycle-eligible seam.
At every active port it introduces one activity variable and clauses

```text
x_e -> activity                         for every incident selected direction,
activity -> OR(outgoing seams),
activity -> OR(incoming seams),
AMO(outgoing seams),
AMO(incoming seams).
```

The AMO rows use the standard Sinz sequential encoding.  These clauses force
selected indegree and outdegree to be equal and to belong to `{0,1}`.  Loops
are handled correctly because their one variable occurs once on each shore.

The CNF also contains exact-one rows for each of the 93 target-provider banks
and for the set of slack-one seams.  No explicit count-104 row is needed:
exact service, exact slack one and balanced telescoping in (2.2) give

```text
1 = 2C-207,
```

so any satisfying assignment automatically has `C=104`.

The resulting full formula has

```text
54,018 variables,
135,771 clauses,
SHA-256 4dbf00e3886f9f39419bf6e8e57ab90f3ef8838fb19d71f91ceca702e7dff2b4.
```

Kissat emitted a DRAT refutation.  `drat-trim` verified that proof and emitted
an LRAT proof; `lrat-check` then verified the LRAT directly against the full
original 54,018-variable, 135,771-clause CNF, not merely against the extracted
core:

```text
DRAT SHA-256 931ea827e6ccb37497a8cd09c984d35732d2ca4751cb125ae8735a67bd698fee,
LRAT SHA-256 955901bd496a9cc5f88b193eaad2fa5d637ba215cdc045a332db2bc12d97de6c,
drat-trim: s VERIFIED,
lrat-check: VERIFIED, exit 0.
```

Thus equality face 1 is empty independently of the earlier CP-SAT run.

## 5. Lineage hardening and adversarial audit

The first builder version pinned the binary and dual but did not itself pin
the imported catalogue parser.  This was a provenance gap, not a semantic
one.  The hardened builder now pins parser SHA-256

```text
c88f13823c0c57a1934b5fcc541301fa13476bf2ca48b3fc614ed13087604ff2
```

and records it in the manifest.  A capped H100 regeneration with hardened
builder SHA-256

```text
59f5447c6687dfab76a4f579a780b45570b24ba626e765a17ea7d335d69ab411
```

reproduced the identical CNF SHA-256 `4dbf00e3...`.  The hardened manifest has
SHA-256

```text
9efad108a2b8ec617b1360b6b12253b9ca9e70fac6466e05954c7bb6f380eefd.
```

An independent semantic counteraudit verified:

- cyclic-SCC pruning is implication-safe;
- the activity and Sinz clauses encode balanced degree in `{0,1}`;
- hit sets are deduplicated before the 93 exact-one rows are formed;
- the exact-one slack row and exclusion of slack-greater-than-one seams are
  correct;
- the count row is genuinely redundant by (2.2);
- CNF syntax has the declared variable and clause counts;
- the LRAT was checked against the full CNF.

No semantic gap remains in the floor-105 derivation.

## 6. Conclusion and scope

The scale-two dual gives `C>=104`.  Section 3 excludes equality face 2 and
Section 4 excludes equality face 1.  Therefore

```text
C >= 105.                                                (6.1)
```

This conclusion is source-relative to the frozen direction-coherent
q<=3/upper-width-four seam catalogue.  The independent Lane-A proof uses
binary seam selection, endpoint balance, physical at-most-one port capacity,
and service of the 93 defects.  It omits separation, reverse-edge, q1,
survivor, residence and deeper-shadow constraints.  It neither asserts
attainability at 105 nor constrains another carrier or an unrestricted move
family.

## 7. Frozen Lane-A artifacts

```text
repeat-face parity verifier
  scratch/threadA_verify_k16_floor104_repeat_parity_20260730.py
  SHA-256 8bbcba60ebd3e9d7a1e9b3fa6b6b55a46094aef5d287dcbc90fbc960bc8487b6

repeat-face parity audit
  scratch/threadA_k16_floor104_repeat_parity_v2_20260730.audit.json
  SHA-256 e6bfb1ce649b685980ab483920a7655ce03e236fc03d37dac2fe9b0d3ef7c9a9

hardened exact-once CNF builder
  scratch/threadA_build_k16_floor104_exactonce_cnf_20260730.py
  SHA-256 59f5447c6687dfab76a4f579a780b45570b24ba626e765a17ea7d335d69ab411

hardened regeneration manifest
  scratch/threadA_k16_floor104_exactonce_hardened_20260730.manifest.json
  SHA-256 9efad108a2b8ec617b1360b6b12253b9ca9e70fac6466e05954c7bb6f380eefd

full exact-once CNF
  scratch/threadA_k16_floor104_exactonce_20260730.cnf
  SHA-256 4dbf00e3886f9f39419bf6e8e57ab90f3ef8838fb19d71f91ceca702e7dff2b4

DRAT proof
  scratch/threadA_k16_floor104_exactonce_20260730.drat
  SHA-256 931ea827e6ccb37497a8cd09c984d35732d2ca4751cb125ae8735a67bd698fee

LRAT proof
  scratch/threadA_k16_floor104_exactonce_20260730.lrat
  SHA-256 955901bd496a9cc5f88b193eaad2fa5d637ba215cdc045a332db2bc12d97de6c

proof-bundle audit
  scratch/threadA_k16_floor104_exactonce_lrat_certificate_20260730.audit.json
  SHA-256 028c41239cb1bed53c0e67ece21372d06e8e07cd11c585065930a9d1730cd4a9

drat-trim verification output
  scratch/threadA_k16_floor104_exactonce_20260730.drat_check.stdout.txt
  SHA-256 973cf279e8bb3ccf6520bea305449b7080b474e9a80e8fde74317ab0ed4e113c

lrat-check verification output
  scratch/threadA_k16_floor104_exactonce_20260730.lrat_check.stdout.txt
  SHA-256 3f05b86dd0f8f17efa504b9d3e7d9db5b2f1cc5cacdc76f9094bc91d538c7da0

hardened build resource ledger
  scratch/threadA_k16_floor104_exactonce_hardened_20260730.build.resource.txt
  SHA-256 dadb27986960a75a15b9fe0ff4ad9d0689f5372f7816a5de59cdd8477db7cf3a
```
