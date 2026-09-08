# K16 rational target-potential theorem: the frozen base catalogue needs at least 101 cuts

Date: 2026-07-30

## 1. Theorem

Consider the authenticated 12,870-port, 211,604-seam catalogue built from the
frozen K16 length-eight source factor.  For a seam `e:u->v`, let `H(e)` be its
set of newly serviced members of the fixed bank `D` of 93 lower-q2 and
upper-q3 defects.

There are positive integer target weights `W_t` and integer port potentials
`Phi_v` at scale 140 such that

```text
sum_{t in H(e)} W_t <= 140 + Phi_v - Phi_u              (1.1)
```

for every one of the 211,604 seams, and

```text
sum_{t in D} W_t = 14028.                               (1.2)
```

Consequently every balanced selected port permutation which services every
defect in `D` has at least

```text
ceil(14028/140) = 101                                   (1.3)
```

selected seams and cuts.

This theorem is solver-independent once the displayed integer certificate is
given.  It strictly supersedes the special-cycle floor 98 in the same frozen
catalogue.

## 2. Construction of the exact rational certificate

The earlier scale-20 certificate gives positive integer target weights `w_t`
and integer port potentials `phi_v` satisfying

```text
rho(e) := 20 + phi_v - phi_u - sum_{t in H(e)} w_t >= 0, (2.1)
sum_t w_t = 1899.                                        (2.2)
```

The new exact artifact contains nonnegative integers `A_t` and integers
`P_v` with

```text
sum_t A_t = 735,                                         (2.3)
sum_{t in H(e)} A_t + P_u - P_v <= 7 rho(e)              (2.4)
```

for every seam.  The replayed ranges and census are

```text
A_t in [0,105],       44 of the 93 A_t are positive,
P_v in [-266,154],
211604 inequalities checked,
34031 tight inequalities,
exact slack range [0,553].                               (2.5)
```

Define

```text
W_t   := 7 w_t + A_t,
Phi_v := 7 phi_v + P_v.                                  (2.6)
```

Multiplying (2.1) by seven and rearranging (2.4) gives

```text
sum_{t in H(e)} (7w_t+A_t)
 <= 140 + (7phi_v+P_v) - (7phi_u+P_u),
```

which is (1.1).  Moreover every `W_t` is positive and

```text
sum_t W_t = 7*1899 + 735 = 14028,
```

which proves (1.2).

The floating-point LP recorded in the discovery artifact was used only to
find the denominator-seven arrays.  Validity uses neither its claimed
optimality nor floating-point tolerances: the checker rounds to the asserted
integer numerators and then verifies all 211,604 inequalities by integer
arithmetic.  The output artifact stores the resulting exact arrays.

## 3. Balanced-circulation proof

Let `x_e` be the multiplicity of selected seam `e`, and put

```text
C = sum_e x_e,
mu_t = sum_{e:t in H(e)} x_e.
```

Endpoint balance means that at every port the total selected outflow equals
the total selected inflow.  Summing (1.1) with multiplicities `x_e` therefore
cancels `Phi` exactly and gives

```text
sum_t mu_t W_t <= 140 C.                                 (3.1)
```

Service of all 93 defects says `mu_t>=1`.  Since `W_t>0`, (3.1) and (1.2)
imply

```text
140 C >= sum_t mu_t W_t >= sum_t W_t = 14028.
```

Thus `C>=101`, proving (1.3).  The argument allows repeated target service
and repeated seam multiplicities; it therefore applies a fortiori to the
binary vertex-disjoint port permutations of the separated master.

Equivalently, in the two-stage language, (2.4) proves that every balanced
service circulation has base reduced cost at least `735/7=105`.  Combining
this with weighted demand 1899 gives

```text
20 C >= 1899 + 105 = 2004.
```

## 4. Independent audit of the superseded floor-98 kernel

The hardened floor-98 replay verifies the stronger form of its no-double-hit
claim.  Each of `46811,56173,60854` has exactly 60 provider seams; every such
seam services only that one defect, and the three provider banks are pairwise
disjoint.

For a nonempty subset `S` of those three targets, let `f(S)` be the minimum
reduced cost of a closed directed walk containing a provider of every member
of `S`.  Forward and independent reverse Dijkstra implementations agree:

```text
f({t}) = 17,       f({s,t}) = 39,       f(T) = 55.        (4.1)
```

These are exact values for the permissive closed-walk functional, hence lower
bounds for physical selected cycles.  Choosing one provider occurrence for
each target and partitioning them by selected cycle gives reduced cost at
least

```text
min(17+17+17, 39+17, 55) = 51.
```

Thus the floor-98 proof is sound.  Its canonical note has been patched to
avoid calling the permissive values exact simple-cycle minima and to make the
partition step explicit.  The present rational potential makes that
three-target argument numerically obsolete but independently confirms it.

## 5. Preserved weak-cone evidence

Before the rational certificate was found, an independent continuous
exact-96 no-repeat relaxation was solved on the H100 CPU.  It retained only
port balance, exactly 96 seams, exact one-time service of the 93 targets and
total base reduced cost 21; it omitted separation, reverse-edge, q1,
survivor, residence and deeper-shadow rows.  GLOP returned `INFEASIBLE` after
208,346 iterations and 121.77 seconds for the 211,604 seam variables, 12,870
used-port variables and 25,835 rows.

This LP result is preserved as independent computational evidence, but it is
strictly weaker than—and unnecessary for—the exact floor-101 proof above.
No floating dual extracted from that run is used here.

```text
driver
  scratch/audit_k16_exact96_norepeat_balanced_lp_20260730.py
  SHA-256 edde0c084114ae9d5bcda4810ff487ba576b0f610da37077d527efe286c3c6fa

audit
  scratch/k16_exact96_norepeat_balanced_lp_20260730.audit.json
  SHA-256 380c3342c7edf3d25bc3a47820f1c2be26ab4010e888cd434eb356ecd697f767
  payload SHA-256 0931ebcf366814d7bf92e4cd2570f1b9447124b13700ccf2e39445fe7371804a

H100 resource ledger
  scratch/k16_exact96_norepeat_balanced_lp_20260730.resource.txt
  SHA-256 2b2f21ea7a29c00c9a2b18f5d1e0d2e9600245d54491edff4d076333c491fdb0
```

## 6. Scope and remaining boundary

The result uses only endpoint balance and service of the frozen 93-target
bank.  It does **not** use cut separation, reverse-edge exclusion, q1 return,
survivor rows, residence, or deeper-shadow CEGAR.  Conversely it applies only
to the authenticated direction-coherent q<=3/upper-width-four seam catalogue
of this fixed source factor.  It is not a K16 nonexistence theorem, does not
cover an unrestricted rethread or another carrier, and does not assert that a
101-cut balanced assignment exists.  Sharpness of 101 is open.

## 7. Frozen lineage

```text
seam catalogue
  scratch/k16_len8_source_seam_ledger_20260730.bin
  SHA-256 832ddd883452e73c0f2462f8550e900d8ffcf01f7397f17b980dd552853b6657

base scale-20 certificate
  scratch/k16_provider_weight_potential_floor95_20260730.audit.json
  SHA-256 7d64defc48cdacbde21aeab3757d051bc2a63623f263d110eb5922749db44e56

discovery output (not used as a numerical proof)
  scratch/k16_second_stage_cycle_dual_20260730.exploratory.json
  SHA-256 7049c20541189b2a9fd9e2f5bbf0915eaa8926f0a61b4bd6138bdbe4997ea4f5

exact integer checker
  scratch/audit_k16_second_stage_cycle_dual_exact_20260730.py
  SHA-256 843d36429b14b543660682f7d22488c2c944f273028e5f995805229d4b29b911

exact primary combined-potential artifact
  scratch/threadA_k16_rational_target_potential_floor101_20260730.audit.json
  SHA-256 31cce7abe1a6d514eec03dafc5826c1b4d8d0638fb9fb561b62379dcb9d1d908
  payload SHA-256 b27e53f41432bc6e8b9b97eafa3385457ce18c7924859609b36eec77f06f21df

exact numerator artifact consumed by the independent replay
  scratch/threadA_k16_second_stage_cycle_dual_floor101_20260730.audit.json
  SHA-256 0aac96523f11d633a1b892ba07384dd5a6ef1e02c62e572b98b5617f473a3fa2
  payload SHA-256 dd4bb1790f9a021ba8838814ade7d0628f3571f7e772e43ca57ab2cf4a8f2b70

H100 CPU resource ledger
  scratch/threadA_k16_rational_target_potential_floor101_20260730.resource.txt
  SHA-256 3cebb45c04baeae6a5bbbfb18d532b61414929e8f85ec085f734671a50c7861f

independent raw-binary verifier (no catalogue parser or floating input)
  scratch/threadA_verify_k16_second_stage_cycle_dual_floor101_20260730.py
  SHA-256 59faf8098566bfe0a77c4b0934d488028875dac5a7243bbae02c6e645d4e6a95

independent raw-binary audit
  scratch/threadA_k16_second_stage_cycle_dual_floor101_independent_20260730.audit.json
  SHA-256 398545adfaca6e3d554947f3444026ea07c138da9fc71915e1cb9ca9fec7783c
  payload SHA-256 fa03111968e5c52346a6aa24a89d405554e5efd6546d3a56544ed7fe7d6ce2bc

independent audit resource ledger
  scratch/threadA_k16_second_stage_cycle_dual_floor101_independent_20260730.resource.txt
  SHA-256 390486e8f8a9deb781cfa02b1752bfbe385e4e282150508bacab7fe563a5742f
```

The capped primary replay used one H100 CPU, a 2 GiB address limit, 2.44
seconds wall time, and 348,800 KiB maximum resident memory.  The independent
raw parser used 37,400 KiB maximum resident memory and also exited zero.
