# Audit of the Catalan two-rail endpoint-complement theorem

Date: 2026-07-31  
Status: PASS after three scope clarifications incorporated in the audited
files

## 1. Verdict

The forced crossing count, endpoint-complement classification,
duplicate-floor endpoint equation, immediate-upper formulas, protected
compiler implication, and K15/K16 calibrations are correct.

The audit required three clarifications, all now present.

1. The conclusion that cross deletion gives two Catalan path forests is for
   a connected/Hamilton factor, or is conditional on the deleted same-rail
   graphs being forests.  A disconnected degree-two factor may contain a
   pure-rail cycle.
2. In the duplicate-cut corollary, every source rail cycle must be hit.  The
   endpoint equation and containment Hall alone do not say that the deleted
   rails are exactly (K)-path forests.
3. In the converse forest theorem, an isolated marked path is impossible:
   its two endpoint occurrences have the same label and would duplicate one
   cross lower colour.  This supplies the stated nontriviality of EC1.

No all-(m) existence or coefficient-one conclusion was inferred from the
finite anatomy.

## 2. Algebraic audit

Let

\[
 M=\binom{2m}{m},\qquad N=\binom{2m}{m+1},\qquad
 K=M-N=\operatorname{Cat}_m.
\]

If a spanning Johnson 2-factor has (2R) cross edges, degree sums give

\[
 e_{UU}=N-R,qquad e_{CC}=M-R.
\]

Only (CC) edges supply the (N) tagged lower colours, hence (Rle K).
The (UU) and cross edges jointly supply the (M) untagged colours, hence
(N+Rge M) and (Rge K).  Thus (R=K), giving

\[
 (e_{UU},e_{CC},e_{UC})=(N-K,N,2K).
\]

The factor has (M+N) edges and the child lower palette has (M+N)
members, so coverage is exact.  This proves the forced-count theorem with
no asymptotic assumption.

For the forest theorem, the three lower banks are disjoint:

\[
 z+\binom{[2m]}{m-1},qquad L,qquad
 \binom{[2m]}m\setminus L.
\]

The last bank is exactly the set of marked endpoint labels because a cross
edge (U--(z+C)) has lower colour (C).  Endpoint containment matching
restores degree two.  Contracting the rail paths preserves components, so
the one-cycle criterion is exact.  The converse uses the same disjoint
banks and, with the isolated-path clarification above, is reversible inside
the forest fibre.

## 3. Duplicate-floor and finite-row audit

When the marked pre-factor has lower profile (1^{N-K}2^K), retaining the
complete tagged palette forces exactly one cut from each doubled class.
The unmarked retained palette is

\[
 \lambda_U(E(G_U))\setminus\lambda_U(D_U).
\]

Since each seam colour is its marked endpoint, exact untagged coverage is
equivalent to

\[
 \partial D_C=mathcal E\mathbin{\dot\cup}\lambda_U(D_U).
\]

The pointwise incidence rows (4.5) are exactly this multiset identity.
Their right sides are zero or one because (mathcal E) is disjoint from
the injective unmarked edge-colour set.  They therefore also force the
marked cut bank to be a matching.  Ordinary Hall is necessary and
sufficient for endpoint containment only; contracted subtour cuts remain
necessary for one-cycle monodromy.

The (m=2) example in the theorem independently confirms that deleting one
edge of each doubled marked colour need not satisfy the endpoint equation:
the chosen endpoint multiset repeats (14).

The hosted one-of-two theorem is correctly scoped as a strict sufficient
subfamily.  For fixed host injection, after checking that the fixed colours
are distinct, its remaining choice is 2-SAT: every forbidden assignment or
pairwise retained-colour/cut-endpoint collision is a unit or binary clause.
The cap-two theorem supplies the upper-union floor, not a lower-intersection
floor.

## 4. Upper, residence, and compiler audit

An unmarked internal edge has no-(z) upper colour.  Every cross edge and
marked internal edge has upper colour containing (z).  Consequently a
no-(z) upper target can only survive internally in an unmarked fragment,
which proves (6.1) and the no-(z) cut-kernel statement.

For a marked upper target (z+U), every retained marked edge of underlying
union (U) contributes once, and every cut-port occurrence at the unmarked
vertex (U) receives one seam of union (z+U).  This gives formula (6.2)
exactly.

The positive (z)-runs are the marked fragments and the zero (z)-runs
are the unmarked fragments.  Hence the stated one-sided and dual length
conditions are correct.  The reset-product implication (Psi_d=0) is also
correct: a run crossing two or more seams contains a whole fragment; the
internal and one-seam cases are explicit hypotheses.  Without those
hypotheses, the exact positional inequality (Psi_dle\mathrm{slack}),
not seam count, is required.

After one cross opening, lower rainbowness leaves exactly its colour
(ho) missing.  A literal (ho)-port, the all-depth cut kernel,
chain-aligned staircase, and one integral common cap are exactly P1--P4
plus the terminal compiler of the global theorem.  The claimed conditional
equality therefore follows from the independent lower bound.

## 5. Finite replay and scope

The independent lightweight replay verifies, for every distinguished
coordinate at K15,

\[
 (M,N,K)=(3432,3003,429),\qquad
 (e_{UU},e_{CC},e_{UC})=(2574,3003,858),
\]

the complete squarefree lower palette, (429) paths on each rail, and
literal containment at every cross edge.  Its contracted cycles have
lengths (852) and (6), hence product cycle type ((426)(3)).  The
hosted-square compatibility graph has eleven isolated cross seams for every
coordinate, so this factor is a positive instance of the broad palette
ledger but a rigorous non-instance of the narrow hosted switch.

For the K16 source path, the replay gives rank-nine union profile

\[
                         1^{10111}2^{1229}3^{100}.
\]

The triple loads and non-Johnson endpoints rule out a one-edge closure to
the required cap-two union-floor cycle.  The rank-seven intersection triple
loads are not used as an obstruction to the weaker retained-forest theorem.

The finite result is scoped to the authenticated K15 factor and K16 path.
It neither excludes a nonlocal K15 component merger nor a different K16
cap-two source.

## 6. Frozen files

* `MATH_THEOREM_K_CATALAN_TWO_RAIL_ENDPOINT_COMPLEMENT_BRAID_20260731.md`
  SHA-256 `6bb2b61c7854ec046003988f6d9ec17f5bd79675f18d4619a558a2e5eb3d1abd`.
* `MATH_THEOREM_K_GLOBAL_PBBS_SLACK_COMPONENT_PACKAGING_20260731.md`
  pre-handoff theorem SHA-256
  `cbad695cf64f65a8ae84949f4ed9cd54ef71edcf3f8c37e62161a44a5862d7f0`.
* `MATH_THEOREM_CATALAN_TWO_RAIL_RAINBOW_SWITCH_REDUCTION_20260731.md`
  SHA-256 `216bbc4e7cf726d979a4ba6e1dcb1cdcfdf3e77503e547761e8a513b8a3809d6`.
* `MATH_AUDIT_K_CATALAN_TWO_RAIL_K15_K16_ANATOMY_20260731.md`
  SHA-256 `80be52e5a4d3bd0101e32e8d9bcfdead40e4673b7f88e2b3c661a80b2ceeb4a8`.
* `scratch/audit_k_catalan_two_rail_k15_k16_anatomy_20260731.py`
  SHA-256 `66093f202483d8ab7a0a220259abc34a2ddfa25bd1f797677f5c62dad0cb0ec8`.
* `scratch/k_catalan_two_rail_k15_k16_anatomy_20260731.audit.json`
  SHA-256 `08b040396712839571a9990e9e9d7b42115828eecc4c5aea2879af609d327ab5`.

The symbolic audit was adversarially repeated by an independent proof
agent.  The finite replayer imports neither a solver nor the theorem proof;
it reconstructs every physical edge and palette directly.
