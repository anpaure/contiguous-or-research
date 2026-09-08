# K16 direct cycle dual: the separated master needs at least 104 cuts

Date: 2026-07-30

## Statement

For the frozen K16 length-eight source and its complete catalogue of 211,604
direction-coherent, positive-residence-safe seams, every selected balanced
port permutation that services all 93 fixed q<=3 defects contains at least
104 nonold seams and cuts.

The proof is one exact scale-two target-price and vertex-potential
certificate.  It supersedes all earlier source-relative cut floors through
101.

## Exact direct certificate

There are positive integer weights `b_t` on the 93 defects and an integer
potential `y_v` on the 12,870 ports such that

```text
b_t in {1,2,4} for every target,
sum_t b_t = 207,
y_v in {-4,-3,-2,-1,0,1,2},
```

and every physical catalogue seam `e:u->v` satisfies

\[
           \sum_{t\in H(e)}b_t\le2+y_v-y_u.            \tag{1}
\]

Here `H(e)` is the set of zero-baseline lower-q2 or upper-q3 defects gained
by the seam.  Exact integer replay checked all 211,604 inequalities in (1):
41,491 are tight, the minimum slack is zero and the maximum is seven.

Let `E` be the nonold seams selected by a balanced port permutation and put
`C=|E|`.  The selected seams are a disjoint union of directed port cycles,
so the potential terms in (1) telescope.  Every defect is serviced at least
once and every target weight is positive.  Therefore

\[
       2C
          \ge\sum_{e\in E}\sum_{t\in H(e)}b_t
          \ge\sum_tb_t
          =207.                                        \tag{2}
\]

It follows that

\[
                 C\ge\left\lceil\frac{207}{2}\right\rceil
                   =\boxed{104}.                       \tag{3}
\]

No SAT or floating-point assertion is used in (1)--(3).

## Shape and combinatorial interpretation

The prices cleanly coarsen the seven block weights in the old scale-20
certificate:

```text
old weight:     11  22  36  19  18  16  23
direct b_t:      1   2   4   2   2   2   4
```

Thus all 93 targets have positive price; their multiplicities are 15 targets
of price one, 60 of price two and 18 of price four.

The seven-valued port potential is a height function for an exact system of
difference constraints.  Rewriting (1) as

\[
                  y_v\ge y_u+b(H(e))-2                 \tag{4}
\]

makes its role transparent:

* a zero-hit seam may descend by at most two height levels;
* a price-one seam may descend by at most one;
* a price-two seam cannot descend;
* a price-four seam must rise by at least two;
* a double-hit seam uses the sum of its two prices.

A directed cycle has net height change zero, so its average serviced target
weight is at most two per seam.  The total demand 207 then gives (2).  This
is the combinatorial content of the potential; no simpler formula in terms
of transition position, deleted coordinate or inserted coordinate is visible
in the frozen factor.

## LP provenance and optimality flag

The unrestricted direct cycle dual is

\[
 \max\sum_t\beta_t
 \quad\text{subject to}\quad
 \beta(H(e))+z_u-z_v\le1\ (e),\qquad \beta_t\ge0.
\]

GLOP returned `OPTIMAL` with value `103.5`, all `beta_t` in
`{1/2,1,2}` and all port potentials in `(1/2)Z`.  Multiplying by two gives
the exact certificate above.  The first extracted floating primal basic
solution had 511 nonzero seams and no small common denominator, but a second
solve found an exact denominator-four primal supported on 174 dual-tight
seams.  Independent raw-binary replay verifies exact endpoint balance,
coverage numerator four at every target and objective `414/4=103.5`.
Consequently 103.5 is the exact optimum of the fractional balanced-service
LP.  Optimality is not needed for (3), but it shows that the next improvement
must be integral.

## Scope

This theorem is source-relative to the frozen direction-coherent,
q<=3/upper-width-four seam catalogue.  It uses only balance and service of
the 93 fixed defects; cut separation, physical reverse-edge, q1, survivor,
residence and deeper-shadow rows are not used.  It does not rule out another
K16 carrier or a transformation outside this catalogue, and it is not a K16
nonexistence theorem.

## Frozen audit lineage

```text
binary seam catalogue
  scratch/k16_len8_source_seam_ledger_20260730.bin
  SHA-256 832ddd883452e73c0f2462f8550e900d8ffcf01f7397f17b980dd552853b6657

floating direct-dual exploration (provenance only)
  scratch/k16_direct_cycle_dual_20260730.exploratory.json
  SHA-256 62856325262bd9e59f8a2ba9dd923534cf0b652fb9cedd730ef76b3ac77e7ca7

exact scale-two certificate
  scratch/k16_direct_cycle_dual_exact_20260730.audit.json
  SHA-256 29b4aae4bc889e07261725b275455a58583d949932a0eeabf65eae33eb7c460d

exact checker
  scratch/audit_k16_direct_cycle_dual_exact_20260730.py
  SHA-256 cfc13d9626994ffd82314e2a0124a2143f3081f5ea837d81ec6053a2abb281b5

H100 resource ledger
  scratch/k16_direct_cycle_dual_exact_20260730.resource.txt
  SHA-256 afbf09264335201654016f878e2b34d276376058409376d97fdd3e86fbab61ff

exploratory solver
  scratch/explore_k16_direct_cycle_dual_20260730.py
  SHA-256 2d1e3cd9ba9744039d2d2e4d7b11804c95135647af8ef27f7df03394df8f529d

floating primal extraction (optimality evidence only)
  scratch/k16_direct_cycle_primal_20260730.exploratory.json
  SHA-256 46ab8c33267b7d010930381fbff1134391244db7576d673d0f9bc2c6381cc968

primal extractor
  scratch/extract_k16_direct_cycle_primal_20260730.py
  SHA-256 ef7fa8b92ae58858423ae553b3e0c8e0cd9d1f7e48e5aafcf9181beaa1f0a208

exact denominator-four primal
  scratch/k16_floor104_scaled_primal_D4_20260730.audit.json
  SHA-256 74a7c2a48355b9827b433385982bb42c118fb4d1506e975a53efa023d230f136

independent exact primal audit
  scratch/k16_floor104_scaled_primal_D4_independent_20260730.audit.json
  SHA-256 ce286af2cfc56732bc57a4621e808b49d83f3e3c9cb0959b8a6da19860d84ae0
```

The H100 exact replay used one CPU, 347,628 KiB maximum RSS and 2.70 seconds
wall time.  It checked every seam inequality directly with Python integers.
