# Exact mod-457 obstruction to every one-column expansion of the C106 SSSSS basis

Date: 2026-07-30  
Lane: AD, independent exact circulation-lattice audit  
Status: **proved for the frozen source-relative SSSSS equality model**

## 1. Frozen inputs and scope

The inputs are:

- seam ledger `scratch/k16_len8_source_seam_ledger_20260730.bin`, SHA-256
  `832ddd883452e73c0f2462f8550e900d8ffcf01f7397f17b980dd552853b6657`;
- exact target weights and endpoint potential
  `scratch/k16_direct_cycle_dual_exact_20260730.audit.json`, SHA-256
  `29b4aae4bc889e07261725b275455a58583d949932a0eeabf65eae33eb7c460d`;
- the 662-column SSSSS fractional support
  `scratch/k16_floor106_s5_pdlp_20260730.json`, SHA-256
  `e934799a0f881163e621236a530b4127253a4b032653eeb21876f40e81fad00a`;
- the complete parity-odd, same-support-component one-column bank
  `scratch/ad_k16_c106_sssss_parity_escape_bank_20260730.tsv`, SHA-256
  `cb021f38ab5e423804bcb8bb885aa20026f34ef59eb93b0500dd716cfc573600`.

Let (S) be the frozen 662-column support and let (mathcal T) be the 93
defect targets. For a seam (e), write (u(e),v(e)) for its directed
endpoints and (H(e)\subseteq\mathcal T) for its serviced targets. Define

\[
 f(e)=\bigl(\mathbf 1_{t\in H(e)}:t\in\mathcal T;\,1\bigr)\in\mathbb Z^{94}.
\]

The last coordinate is selected mass. The desired SSSSS right-hand side is

\[
 b=(1^{93};106).
\]

Endpoint balance and (f(x)=b) imply direct slack five, since the frozen
weighted accounting identity gives

\[
 \sum_e s(e)x_e=2\sum_e x_e-
 \sum_{t\in\mathcal T}w_t\sum_{e:t\in H(e)}x_e
 =212-207=5.
\]

The result below relaxes nonnegativity, Boolean bounds, capacity one, q1,
separation, residence, survivor, reverse-edge and connectivity conditions.
It is therefore a necessary obstruction for every stronger physical model,
but says nothing about expansions by two or more outside columns.

## 2. The integral support-cycle matrix

Choose a spanning forest of the undirected support graph. It has 571 vertices,
three components and hence (571-3=568) tree edges. The 94 non-tree support
edges give 94 signed fundamental circulations (z_1,\ldots,z_{94}).

### Lemma 2.1 (integral completeness of the basis)

The (z_j) form a (mathbb Z)-basis of

\[
 \ker_{\mathbb Z} B_S,
\]

where (B_S) is the directed endpoint-incidence matrix of (S).

#### Proof

In any integral circulation, the coefficient on each non-tree edge can be
eliminated by subtracting that integer multiple of its signed fundamental
cycle. The remainder is an integral circulation supported on a forest, hence
zero by peeling leaves. Independence follows because fundamental cycle
(z_j) contains its own non-tree edge with coefficient one and no other
fundamental cycle contains that non-tree edge. ∎

Let (M\in\mathbb Z^{94\times94}) have column (f(z_j)). The independent
fraction-free replay gives

\[
 \det M=-7452780650347681984140640
\]

and the exact factorization

\[
 |\det M|
 =2^5\cdot5\cdot457\cdot63079\cdot33852407\cdot47731799.
\]

Modulo 457, (M) has rank 93. Thus its left nullspace is one-dimensional.

## 3. Direct mod-457 edge certificate

The audit artifact freezes the unique nonzero row

\[
 a=(a_t:t\in\mathcal T;\,a_0)\in(\mathbb Z/457\mathbb Z)^{94}
\]

normalized by

\[
 a\cdot b=1\pmod {457}.
\]

Here (a_0=241); all 93 target coefficients are listed exactly in the audit
artifact. Since (aM=0), the support-edge label

\[
 \ell(e)=a_0+\sum_{t\in H(e)}a_t
\]

has zero circulation around every support cycle. Consequently it is a
coboundary on each support component: there is a frozen potential

\[
 p:V(S)\longrightarrow\mathbb Z/457\mathbb Z
\]

such that, for every (e\in S),

\[
 R(e):=\ell(e)+p(u(e))-p(v(e))=0\pmod {457}. \tag{3.1}
\]

The artifact lists all 571 values of (p) and directly replays (3.1) on all
662 support seams. Extend (p) by zero away from (V(S)).

### Theorem 3.1 (global modular escape equation)

For every integral seam vector (x) satisfying endpoint balance and the 93
exact-once target equations together with selected mass 106,

\[
 \sum_{e\notin S} R(e)x_e=1\pmod {457}. \tag{3.2}
\]

#### Proof

Endpoint balance cancels the potential terms:

\[
 \sum_e\bigl(p(u(e))-p(v(e))\bigr)x_e=0.
\]

The service and count equations give

\[
 \sum_e\ell(e)x_e=a\cdot b=1\pmod {457}.
\]

All support terms vanish by (3.1), leaving (3.2). No sign, positivity,
capacity or Boolean hypothesis is used. ∎

## 4. Exact radius-one no-go

The already frozen mod-2 support certificate forces any one-outside-column
solution to use a parity-odd outside seam. Endpoint balance forces the two
endpoints of that seam to lie in the same support component: a single edge
cannot repair a componentwise endpoint imbalance, nor can it balance a new
vertex. Nonnegative total slack five forces its individual slack to be at most
five. These three necessary conditions give exactly the 298 rows of the frozen
escape bank.

The direct mod-457 replay evaluates (R(h)) for every one of these 298 seams.
Exactly zero have the required residue:

\[
 \#\{h:R(h)=1\pmod {457}\}=0. \tag{4.1}
\]

### Corollary 4.1 (radius-one integral infeasibility)

There is no integral endpoint-balanced vector supported on (S\cup\{h}),
with (x_h=1), that services all 93 targets exactly once and has selected mass
106, for any of the 298 possible one-column seams (h).

This is stronger than the observed CP-SAT presolve infeasibility: it already
holds in the unrestricted signed integral circulation lattice.

### Corollary 4.2 (valid expansion cut)

Every binary SSSSS solution in the full frozen seam catalogue satisfies

\[
 \boxed{\sum_{e\notin S}x_e\ge2.} \tag{4.2}
\]

Indeed zero outside columns are excluded by the mod-2 support certificate and
one outside column is excluded by Corollary 4.1.

For a radius-two annealer or exact master, the stronger reusable constraint is
not merely (4.2), but the modular row (3.2). Candidate pairs must have corrected
residues summing to one modulo 457, in addition to the independent mod-2 escape
syndrome and endpoint-balance requirements.

## 5. Frozen replay artifacts

The earlier unsuffixed JSON with SHA prefix `b255ab9c` is **superseded and
must not be cited**: a later presentation loop shadowed its serialized
`modulus` field, although the computations themselves had used 457. Version 2
renames the loop variables and has fail-closed assertions that the serialized
modulus is 457 and that exactly 298 candidates are rejected.

- Checker:
  `scratch/audit_ad_k16_c106_sssss_radius1_lattice_20260730.py`, SHA-256
  `d75430205f7941be821dd63d54cf94f5c961662ab175f3f7d8b12356b124e0e1`.
- Exact certificate:
  `scratch/ad_k16_c106_sssss_radius1_mod457_separator_v2_20260730.audit.json`,
  SHA-256
  `e2fa6fa2fe42152566af9a771b029af3b1977f1b61e62dfe58527b500ed35aff`.
- Certificate payload SHA-256:
  `5c53ab031a84b0061582d5c50cf01a1c79ebd97d6d8418a33a81631fad36cc4c`.

The checker reads the raw binary seam ledger, reconstructs the 94 fundamental
integral cycles, recomputes the exact determinant by fraction-free Bareiss
elimination, recomputes the mod-457 null row and vertex potential, verifies
zero corrected residue on every support edge, and evaluates all 298 candidate
residues. Its measured local-light execution time was below two seconds; it
invokes no SAT/CP solver and performs no search over seam selections.

## 6. Precise boundary

Proved:

1. the complete one-outside-column SSSSS face is empty over the integer
   circulation lattice;
2. the globally valid modular equation (3.2);
3. the exact expansion lower bound (4.2).

Not proved:

1. feasibility or infeasibility with two or more outside seams;
2. any physical carrier satisfying q1, residence, separation or connectivity;
3. a C106 construction, or a floor above 106.
