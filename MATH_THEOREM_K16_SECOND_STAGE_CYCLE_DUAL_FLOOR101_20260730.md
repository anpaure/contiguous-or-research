# K16 scale-140 cycle dual: the separated master needs at least 101 cuts

Date: 2026-07-30

## Statement

For the frozen K16 length-eight source and its complete catalogue of 211,604
direction-coherent, positive-residence-safe seams, every selected balanced
port permutation that services all 93 fixed q<=3 defects contains at least
101 nonold seams and cuts.

This is a direct solver-independent target-price and vertex-potential
certificate.  It supersedes the source-relative floors 95--99.

## Direct certificate

There are nonnegative integer weights `W'_t` on the 93 defects and an integer
potential `Phi'_v` on the 12,870 ports such that

```text
sum_t W'_t = 14028
```

and every physical catalogue seam `e:u->v` satisfies

\[
       \sum_{t\in H(e)} W'_t
          \le 140+\Phi'_v-\Phi'_u.                    \tag{1}
\]

Here `H(e)` is the set of zero-baseline lower-q2 or upper-q3 defects gained
by the seam.  All 211,604 inequalities in (1) were replayed with exact
integer arithmetic; 34,031 are tight and the minimum slack is zero.

Let `E` be the nonold seams selected by a balanced port permutation and let
`C=|E|`.  The selected seams are a disjoint union of directed port cycles,
so the potential terms in (1) telescope.  Every defect is serviced at least
once and every `W'_t` is nonnegative.  Therefore

\[
  140C
    \ge \sum_{e\in E}\sum_{t\in H(e)}W'_t
    \ge \sum_tW'_t
    =14028.                                           \tag{2}
\]

Consequently

\[
                 C\ge\left\lceil\frac{14028}{140}\right\rceil
                   =\boxed{101}.                     \tag{3}
\]

No SAT or floating-point claim is used in (1)--(3).

## Provenance: the two-stage derivation

The earlier scale-20 certificate has defect weights `w_t` of total 1899 and
an integer port potential `phi_v` satisfying

\[
        w(H(e))\le20+\phi_v-\phi_u.
\]

Define the nonnegative integral reduced cost

\[
        \rho(e)=20+\phi_v-\phi_u-w(H(e)).
\]

A floating GLOP exploration of the second-stage cycle dual returned optimum
105.0.  Its target prices and port potentials lie, to numerical precision,
in `(1/7)Z`.  Multiplying by seven gives nonnegative integers `A_t` and
integers `P_v` with

```text
sum_t A_t = 735
```

and, for every seam,

\[
   \sum_{t\in H(e)}A_t+P_u-P_v\le7\rho(e).            \tag{4}
\]

Exact integer replay verifies (4).  The direct certificate is simply the
algebraic collapse

\[
       W'_t=7w_t+A_t,\qquad \Phi'_v=7\phi_v+P_v.
\]

Substituting these definitions into (4) gives (1), and

\[
       \sum_tW'_t=7\cdot1899+735=14028.
\]

The floating LP found the certificate; exact integer replay proves it.
Optimality of the exploratory LP is not needed for the cut floor.

## Scope

This theorem is source-relative to the frozen direction-coherent,
q<=3/upper-width-four separated seam catalogue.  It needs only balanced port
cycles and service of the 93 fixed defects; cut separation, physical
reverse-edge, q1, survivor, residence and deeper-shadow rows are not used.
It does not rule out another K16 carrier or a transformation outside this
catalogue, and it is not a K16 nonexistence theorem.

## Frozen audit lineage

```text
binary seam catalogue
  scratch/k16_len8_source_seam_ledger_20260730.bin
  SHA-256 832ddd883452e73c0f2462f8550e900d8ffcf01f7397f17b980dd552853b6657

base scale-20 certificate
  scratch/k16_provider_weight_potential_floor95_20260730.audit.json
  SHA-256 7d64defc48cdacbde21aeab3757d051bc2a63623f263d110eb5922749db44e56

floating exploration (provenance only)
  scratch/k16_second_stage_cycle_dual_20260730.exploratory.json
  SHA-256 7049c20541189b2a9fd9e2f5bbf0915eaa8926f0a61b4bd6138bdbe4997ea4f5

exact scale-seven and collapsed scale-140 certificate
  scratch/k16_second_stage_cycle_dual_exact_20260730.audit.json
  SHA-256 1a36ce80af98b5db58ce55a4401e9ccba8bea1f12fd0af2ee73e0a932fdbe285

exact checker
  scratch/audit_k16_second_stage_cycle_dual_exact_20260730.py
  SHA-256 843d36429b14b543660682f7d22488c2c944f273028e5f995805229d4b29b911

H100 resource ledger
  scratch/k16_second_stage_cycle_dual_exact_20260730.resource.txt
  SHA-256 4863d05201fa26c60caf7fa44b5eda89d0308ac7b49ce18e5b1b46f27b00c8a3
```

The H100 exact replay used one CPU, 349,312 KiB maximum RSS and 3.01 seconds
wall time.  It checked every seam inequality directly with Python integers.
