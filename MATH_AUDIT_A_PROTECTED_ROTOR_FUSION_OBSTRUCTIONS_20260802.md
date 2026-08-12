# Audit of protected rotor fusion curvature and saturated hinges

**Date:** 2026-08-02  
**Audited theorem:**
`MATH_THEOREM_A_PROTECTED_ROTOR_FUSION_CURVATURE_AND_SATURATED_HINGE_OBSTRUCTIONS_20260802.md`,
SHA-256
`d069f243e6f3838215236bc97af8e84aadab7a7c2e3c0cb41b87cd7f662f54b5`.

## Exact replay

The lightweight verifier
`scratch/audit_a_protected_rotor_fusion_obstructions_20260802.py`, SHA-256
`49d0cf5b7e03fce94c325a48c916022cd2d39c678f11f54701035af436ca6234`,
returns

```text
PASS
protected_permutations=2
z3_signature_tables=81 zero_curvature=27
chordless_six_cycle_holonomy=1 rectangle_tests=0
residence_thresholds=3..40 sharp_L3_mass=6
saturated_subset_checks=665
```

It checks four independent points.

1. The two-state selector has exactly two permutations: the identity is
   protected and disconnected; the transposition is owner-exact and
   connected but loses the sole protected row.
2. All `3^4=81` `2x2` signature tables over `Z/3Z` satisfy the zero mixed-
   curvature condition exactly when the base-row/base-column coboundary
   reconstruction succeeds.  A separate chordless bipartite six-cycle has
   no `2x2` rectangle but alternating holonomy one.  Thus cross-role
   transparency requires zero holonomy on every compatibility cycle;
   rectangle tests suffice only on a rectangle-generated cycle space.
3. The four-port family `(1,L-1,L-1,1)` has old run lengths `(L,L)` and
   crossed lengths `(2,2L-2)` for every `3<=L<=40`.  Exhausting weights in
   `{1,...,5}^4` confirms that total mass six is sharp at `L=3`.
4. All 665 nonempty subset containments on a six-point universe confirm the
   saturated-state rank argument: if the already-saturated union is `T`
   and the adjacent owner `T union x` also has rank `|T|`, then the owner
   (not necessarily the letter `x`) equals `T`.

## Direct formula audit of the hinge boundary

For the literal hinge construction, the decisive formula is checked from
the displayed letters rather than inferred from the verifier.

* If `1<=ell<=d-1`, the middle spine unions to `S_ell`; therefore
  `B_0 union M=T` for every advertised tail choice.
* If `ell=0`, `B_0=T` directly.
* If `ell=d`, the tail unions to `(T\S_1) union A`, so saturation is
  equivalent to `S_1 subseteq A` and occurs for exactly
  `2^(|S_d|-|S_1|)` choices.

Thus the theorem does not incorrectly discard all full-depth hinges.

## Scope boundaries

The two-state protected row is an abstract rotor certificate, not a claimed
Boolean interval-OR realization.  The four-port certificate is a literal
binary residence interface, but it does not supply a rank-uniform Johnson
owner table.  Conversely, the saturated-tail lemma is a literal flat
rank-`r` one-copy obstruction, but it concerns the current hinge
construction, not every possible unsaturated hinge atlas.

Accordingly the note proves neither a canonical one-copy obstruction nor a
failure of `B(k)+O(1)`.  It proves that the currently available hinge-TU
rounding and unguarded colour-neutral fusion cannot be composed without new
unsaturated states and protected-interface control.
