# K17 round02 complete Hamming-two local/q1 no-go

**Date:** 2026-08-02  
**Status:** exact finite theorem for the frozen distinct-base, one-for-one
Hamming-two recut face.

## 1. Statement

Fix the authenticated round02 7,612-piece bank and its complete catalogue of
16,667 legal one-for-one recuts.  A *Hamming-two bank* replaces the selected
cut on exactly two distinct base pieces and changes nothing else.

> **Theorem 1.1 (complete fixed-face closure).** Every compatible Hamming-two
> bank either fails at least one of the five necessary local zero-row tests
> (`lower`, `out`, `in`, common `orientation`, or `rank10`) or its exact
> orientation-coupled `Q1_ONLY` formula is UNSAT.  Hence this face contains no
> locally admissible q1 completion of round02.

This is not a statement about a bank with an added or deleted cut, a C6/C8/q4
or other factor rethread, or a different dense refinement.  It makes no
claim about deeper shadows, strict global residence, connected topology, or
the terminal compiler outside the fixed formula.

## 2. The exact q1 formula

For a fixed bank, the Boolean atoms are all literal tail-state/head-state
seams satisfying the Johnson, selected-lower-colour, and relaxed two-block
residence predicates.  The formula imposes:

1. exactly one outgoing atom at every physical piece;
2. exactly one incoming atom at every physical piece;
3. exactly one atom of every selected lower colour; and
4. for every atom, the two implications fixing the common orientations of
   its tail and head pieces.

Thus satisfiability is precisely the existence of the advertised functional
q1 factor.  No connectivity or upper-row equation is silently included in
the `Q1_ONLY` formulas used below.

## 3. Complete anchor reduction

The frozen obstruction is the occurrence-labelled dual fan at quotient
sockets `L3669,L3670`, with physical owner masks

\[
 s=115442,\qquad t=115186,\qquad s\cap t=114930.
\]

If a Hamming-two bank retains this dual fan, it is q1-infeasible.  If it
destroys the fan, the exact unfiltered creator--colour-supplier join and
central-role audit prove that the bank contains one of exactly 21 anchors:
twelve selected non-`114930` socket escapes and nine central alternatives.
There are no additional nonanchor latent creator--supplier pairs.

Taking one anchor and one compatible recut, then deduplicating the two orders
of an anchor--anchor pair, gives exactly 349,642 banks.  Exact joint replay
finds 169,426 with

```text
zero_lower=zero_out=zero_in=zero_orientation=zero_rank10=0.
```

Every other anchored bank already fails a necessary local row.

## 4. Proof partition of the 169,426 locally clean banks

The clean set has the disjoint proof partition

\[
 169426=165713+49+3664.                              \tag{4.1}
\]

### 4.1 Semantic-core persistence: 165,713

For each authenticated single-anchor contradiction, the sequential-AMO
proof core was closed to complete occurrence-labelled out, in and colour
rows and rebuilt as a canonical pairwise-AMO semantic CNF.  Each such CNF is
UNSAT with a checked DRAT proof.

The persistence filter classifies a joint bank as UNSAT only when one
certified subsystem is unchanged at the literal physical-row level: no core
endpoint is replaced, no structurally relevant palette bit toggles, and no
new atom can enter a certified out, in, or colour row.  Consequently that
semantic contradiction is an UNSAT subformula of the joint bank.  The union
of the primary and independently authenticated alternate profiles certifies
exactly 165,713 clean banks.

### 4.2 Compensated dirty-central banks: 49

Seven individually dirty central anchors each have seven distinct-base
partners which repair the local ledger.  All 49 canonical banks were rebuilt
and all 49 exact q1 CNFs have independently checked DRAT UNSAT proofs.  These
cases are not counted in semantic persistence.

### 4.3 Fresh residual formulas: 3,664

The remainder has 3,664 distinct bank keys and 3,664 distinct exact
occurrence-delta signatures.  Every literal bank and `Q1_ONLY` CNF was freshly
built on H100 CPU.  All 3,664 formulas are UNSAT.

The retained certificate for every case was then audited uniformly:

1. regenerate the full CNF and recover its recorded SHA-256 exactly;
2. verify that every retained core clause occurs in the regenerated CNF; and
3. replay the retained core proof with `drat-trim`.

All 3,664 cases pass all three checks.  During the live solve, cases
273--275 received exit 126 when a worker script was replaced at cutover.
Those three resource failures were preserved verbatim and made no
mathematical inference.  Independent complete rebuild/solve/DRAT runs later
certified those same three banks; their certificates were then subjected to
the same uniform post-audit as the other 3,661.

Sections 3 and 4 prove Theorem 1.1.

## 5. Exact consequence and sharp scope

Within the frozen distinct-base one-for-one Hamming-two face, every bank
either retains a known q1 contradiction, violates a necessary local row, or
has a freshly certified UNSAT q1 formula.  A construction-admissible escape
must therefore leave this face, for example by changing the cut count or by
a genuine factor/circuit rethread.

This does **not** prove that a particular q4 move, or “higher order” in any
global sense, is necessary.  It also does not exclude socket escapes in a
larger move class.  The conclusion is exactly the corrected one requested:
the provider-only scan was insufficient, but the full non-`114930` one-cut
socket generator and its complete Hamming-two closure are now audited.

## 6. Frozen artifacts

The proof depends on the following already frozen ledgers:

| artifact | SHA-256 |
|:---|:---|
| round02 bank | `48670b1bf5388ed4c8f47a408e4659c145ec26dc3d6a6bb31cd379a1e70ad649` |
| latent-join audit | `0ee2c01a938b58eec8cb9b26161fcf3defbaf92a8f0ab4211b6c0b97bb09e284` |
| anchored clean-bank ledger | `9c4ecd1541a945bfae2be6d6534b28543a9c5c87745bdb8a47100dda274fb589` |
| anchored census audit | `12ee6bff96d4ab42b0f4c92ef642aedd4b4849f7cdd0632f8b2466d6275ea4df` |
| semantic-union count ledger | `f184ade82dc8f63ac5bd74bf2d89aed25a9d57f05dcc830782480e6bbf3c8fa0` |
| dirty-central49 proof manifest | `7959c9ce00d855cd187fe24e770e785f908dee5106cef8daf75480a75d55c0b6` |
| dirty-central49 theorem audit | `bf468abc0fd076613c81b21468f23e8e947e153eeff3d85e4bb52b15705e32f9` |
| exact residual case manifest | `860924cbb256d320ee35790e98ebd1e78bf0b01cdabf1bdbf9fdaef0929fa109` |
| independent cases273--275 summary | `e177efd6b92dc7fed753b341e98fc5d2441c663eb7162088cd52b801015dfeac` |
| final 3,664 proof manifest | `0706fee2c9dba89c6339ca2088c9edc021f0d5107f0c1ddf1e344129fa3f92d3` |
| retained-certificate hash manifest | `487170d4dfb48ef5315884d0b001762a22e5d8dcb00a75b99cf1cbe511f532cb` |
| all-3,664 uniform post-audit | `8777f67313b010091e7596d3b3539a9bb6424abae40be1d1fccb2e69d3df5f81` |
| final 3,664 theorem audit | `2717e038b4e10ee478b791c614a80b83cea6ca01e5eb156d9bfc898e952b5f37` |
| compressed complete certificate bundle | `029832edae396f1489d359b1d661480fc19e2467c5aacc3f8fc459f78d9eaef4` |

The complete compact residual certificate bundle is frozen under
`scratch/threadD_k17_exact3664_q1_20260802/`.  The final audit reports exactly
3,664 distinct banks, 0 SAT, 3,664 UNSAT, 0 resource-unknown, 3,664 regenerated
CNF hash matches, 3,664 core-subset checks, and 3,664 verified retained-core
proofs.  It binds the builder, proof manifest, retained-core hash manifest,
and uniform post-audit.
