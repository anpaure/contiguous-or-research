# Symmetry sweep for `k=14,...,20`

Date: 2026-07-27

## 1. Exact census

For each central layer, the table gives the number of coordinate-rotation
orbits by orbit size.  The last two columns give the total number of orbits
under coordinate dihedral symmetry and under
`x -> ax+b` over `Z/kZ`, respectively.

| `k` | central rank | `W` | `d` | rotation-orbit distribution | `#D_k` | `#Aff(Z_k)` |
|---:|---:|---:|---:|---|---:|---:|
| 14 | 7 | 3432 | 2 | `2^1,14^245` | 133 | 47 |
| 15 | 8 | 6435 | 3 | `15^429` | 232 | 66 |
| 16 | 8 | 12870 | 3 | `2^1,4^1,8^8,16^800` | 440 | 129 |
| 17 | 9 | 24310 | 3 | `17^1430` | 750 | 95 |
| 18 | 9 | 48620 | 3 | `2^1,6^3,18^2700` | 1387 | 471 |
| 19 | 10 | 92378 | 3 | `19^4862` | 2494 | 280 |
| 20 | 10 | 184756 | 3 | `2^1,4^1,10^25,20^9225` | 4752 | 1279 |

Here `s^a` means `a` orbits of size `s`.  Reproduce with

```sh
python3 scratch/sigma_symmetry_sweep_k14_k20.py
```

For the two prime cases, the full affine distributions are

\[
k=17:\quad 34^1,68^1,136^8,272^{85},
\]

and

\[
k=19:\quad 38^1,114^3,171^{14},342^{262}.
\]

Thus the raw affine quotients have only 95 and 280 objects.  Those numbers
are tempting but misleading for a single chronology.

## 2. Two decisive symmetry obstructions

### Mixed rotation orbits rule out an equivariant Hamilton chronology

Let `tau` be the coordinate `k`-cycle.  If a Hamilton cycle on the complete
central layer were `tau`-invariant, then `tau` would act as an automorphism
of that cycle.  Its action on the central layer has order `k`.  An
automorphism of a cycle of order greater than two is a rotation, and all of
its vertex orbits have the same length.

Consequently the mixed orbit distributions at

\[
k=14,16,18,20
\]

are a statewise obstruction: none of these dimensions admits a
translation-equivariant single central Hamilton cycle.  The alternating
central mask already gives the size-two orbit in every case.  Raw cyclic,
dihedral, and affine quotient sizes for these even dimensions therefore do
not define an instant lift; one would first obtain a multi-cycle object and
then have to break symmetry while joining it.

This is also why `k=14` is a false positive.  Its affine quotient has only
47 central orbits, close to the small `k=12` census, but the size-two orbit
prevents that quotient from lifting to one equivariant chronology.

### Full `AGL(1,p)` symmetry is too large for one cycle

The coordinate action of `AGL(1,p)` on a nontrivial uniform layer is
faithful.  If one Hamilton cycle were invariant under the full affine
group, this faithful action would embed

\[
C_p\rtimes C_{p-1}
\]

into the dihedral automorphism group of a cycle.  A subgroup of a dihedral
group can act on its odd-order rotation subgroup only by the two
automorphisms `+1` and `-1`.  Hence the multiplier subgroup has order at
most two, contradicting `p-1>2`.

Therefore the 95-object and 280-object affine quotients at `p=17,19` cannot
themselves yield a single affine-equivariant chronology.  The largest
compatible coordinate symmetry is the ordinary dihedral group generated
by translations and inversion.  The honest sizes are therefore 750 and
2494 dihedral orbits, or 1430 and 4862 translation orbits if reflection is
not built in.  Full affine symmetry remains useful only for a catalogue or
a multi-factor scaffold whose symmetry is later broken.

## 3. The genuine exception: `k=15`

Write `k=2m+1`.  Lucas' theorem gives

\[
\binom{2m+1}{m}\equiv1\pmod2
\quad\Longleftrightarrow\quad
m\mathbin{\&}(m+1)=0
\quad\Longleftrightarrow\quad
m=2^t-1.
\]

Thus in the present range the only odd dimension with odd middle width is

\[
k=15=2^4-1,\qquad W=6435.
\]

On the two middle levels, complementation is a fixed-point-free involution
swapping the two shores.  If `W` is odd, it may act on a Hamilton cycle as
the half-turn rotation by `W` steps, which also swaps the two shores.  It
commutes with the coordinate `C_15`, and

\[
C_{15}\times C_2\cong C_{30}.
\]

Hence translation and complementation can both act as rotations of one
middle-level Hamilton cycle.  The `2W` vertices then reduce to

\[
\frac{2W}{30}=429
\]

rotational packets.  Adding coordinate inversion is still cycle-compatible
and gives 232 dihedral packets.  Complementation simultaneously identifies
lower and upper shadow conditions.

For `k=17,19`, `W` is even.  The half-turn of a `2W`-cycle preserves the
bipartition, whereas complementation swaps it.  Since complement commutes
with translation, it cannot instead be represented by a reflection while a
nontrivial translation is represented by a rotation.  The extra factor-two
compression is therefore unique to `k=15` in this sweep.

The Frobenius/multiplier order-four symmetry visible from
`F_16^*` does **not** extend this instant quotient: any multiplier subgroup
of order greater than two runs into the affine-to-dihedral obstruction of
Section 2.

## 4. Odd-to-even arithmetic

For an odd dimension `2m-1` and the following even dimension `2m`,

\[
W(2m)=2W(2m-1).
\]

The exact lower-bound parameters are

| lift | odd `d` | even `d` | `B_even-2B_odd` |
|---|---:|---:|---:|
| `13 -> 14` | 3 | 2 | -4 |
| `15 -> 16` | 3 | 3 | -3 |
| `17 -> 18` | 3 | 3 | -3 |
| `19 -> 20` | 3 | 3 | -3 |

The last three pairs have a cleaner arithmetic interpretation.  A two-sector
lift that shares one common three-cell boundary tail would have length

\[
2W_{\rm odd}+3=B_{\rm even}
\]

exactly.  Thus `15 -> 16`, `17 -> 18`, and `19 -> 20` are
arithmetically perfect conditional lifts.  This is only a capacity identity.
The exact audit in `MATH_ODD_EVEN_SHARED_TAIL_LIFT_20260727.md` shows that a
valid lift additionally needs a bi-resident dual chronology, a matching
erosion boundary, and the full marked seam-cover condition; none follows
from an arbitrary exact odd word.

The `13 -> 14` pair is less natural: besides sharing the odd tail, the lift
must lower the depth from three to two.  It needs one additional compression
and is not an automatic consequence of a future `k=13` solution.

## 5. Candidate ranking

1. **`k=15`: the only genuine symmetry instant-shot.** It has 429
   translation-complement packets, 232 dihedral packets, no short central
   rotation orbit, and exact lower/upper complement coherence.  This is the
   sole case in `14..20` with a new symmetry unavailable at `k=13`.
2. **`k=16`, conditional on `k=15`.** Direct equivariance is obstructed,
   but the odd-to-even capacity is exact if a common depth-three boundary
   tail can be shared.
3. **`k=17`: valid prime rotor, not an instant small quotient.** The honest
   translation quotient has 1430 states (dihedral 750).  The 95-state AGL
   figure cannot lift to one affine-invariant cycle.
4. **`k=18`, conditional on `k=17`.** Same exact shared-tail arithmetic;
   direct rotational symmetry is obstructed by short central orbits.
5. **`k=19` then `k=20`.** The prime rotor is legitimate but already has
   4862 translation states; its affine 280-state quotient is incompatible
   with one chronology.  `k=20` is only attractive as a conditional lift.
6. **`k=14`: superficially small, structurally false as an equivariant
   shot.** Its raw cyclic/dihedral/affine counts are 246/133/47, but the
   unique size-two central orbit forbids a single invariant Hamilton cycle,
   and the `13 -> 14` depth drop spoils the clean lift arithmetic.

The concise verdict is that no `AGL(1,17)` or `AGL(1,19)` miracle survives
the cycle-automorphism test.  `k=15` is the one exceptional dimension worth
an immediate symmetry-reduced construction attempt; the even cases should
be approached as odd-to-even lifts, not as direct cyclic quotients.
