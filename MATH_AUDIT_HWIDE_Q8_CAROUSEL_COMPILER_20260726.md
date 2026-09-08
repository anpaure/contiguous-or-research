# Audit of the `H`-wide controller for the `Q_8` carousel

Date: 2026-07-26

Files compared:

* `MATH_THEOREM_HWIDE_COMPILER_CONTROLLER_FOR_Q8_CAROUSEL_20260726.md`;
* `MATH_ATTACK_K_Q8_OWNER_CAROUSEL_CPM_EMSF_BOUNDARY_20260726.md`;
* `MATH_OBSTRUCTION_Q8_CAROUSEL_LITERAL_TURNAROUND_SEAM_20260726.md`.

## 0. Verdict

The controller construction removes the literal quadratic turnaround
fibre.  The word orientation at both antipodal turnarounds is correct,
the mixed controller/core decoder is valid through every `q<=H`, the
remaining payload seams are genuinely same-oriented, and the
`O(H)`-per-macrocycle seam ledger is a safe upper bound.

The doubled word is a simple isometric `C_(2D)`.  It lies inside a
physical `Q_D`, but its owner support is **not** a `Q_D` subcube.  It has
only `2D` owners.  Thus any outer argument requiring packet support
`2^D` is not supplied by this theorem; the source file correctly says
that it factors only its declared cyclic union.

Two corrections are required for the ambient implementation.

1. Four frozen tag pairs consume four additional physical pair slots.
   The choice of `L` in (7.3) can give `D>m-4`, in which case the active
   pairs and tags do not fit in `[2m]`.  Reserve those slots explicitly.
2. The inherited parity-indexed payload frame ledger needs `L` even, or
   an explicit phase reset.  The word remains isometric for odd `L`, but
   Section 3 does not supply the reset required by the earlier carousel
   audit.

Both are harmless to the asymptotic result.  Taking

\[
 L=2\left\lfloor {m-r-12\over16}\right\rfloor         \tag{0.1}
\]

makes `L` even and gives

\[
                         m-19\le D=r+8+8L\le m-4.     \tag{0.2}
\]

Hence `L~m/8`, `D=Theta(m)`, the tags fit, and the seam bound remains
`O(HG/m)=o(G)`.

The local theorem still does not prove that these sparse cyclic carriers
pack `W-o(W)` owners or have negligible cross-macrocycle target
collisions.

## 1. Exact word orientation

The controller cycle has direction word

\[
                         \kappa\kappa=BABA,
 \qquad |A|=|B|=n\ge H.                               \tag{1.1}
\]

The macro first half is

\[
                         \Pi=B\,\Sigma\,A.            \tag{1.2}
\]

Therefore the complete word is

\[
 B\,\Sigma^{\uparrow}\,A\ |
 B\,\Sigma^{\downarrow}\,A\ |
 B\,\Sigma^{\uparrow}\,A,                            \tag{1.3}
\]

where the arrows record the payload-bit orientation, not reversal of the
written direction order.  The first use of every payload direction sends
zero to one; the repeated use sends one to zero.

At each vertical bar, the controller projection is exactly

\[
                         A|B,                          \tag{1.4}
\]

a cyclic interval of `BABA`.  Since the suffix `A` and prefix `B` both
have at least `H` directions, every window of at most `H` edges crossing
either turnaround lies wholly in the controller.  The positive compiler
theorem supplies both forward and reverse literal injectivity through
length

\[
                         n/2-1\ge H.                  \tag{1.5}
\]

Thus neither of the raw up/down payload fibres from the obstruction note
survives.

The actual up/down payloads are even farther apart: between the final
increasing run and the first decreasing run lie `A`, `B`, and the next
`Q_8` seam direction.  A protected window cannot traverse that collar.

## 2. Mixed controller/core windows

A window meeting `B|Sigma` or `Sigma|A`, but not a global turnaround,
has `d>=1` controller moves and `q-d` core moves.  Restricting its signed
literal target to the controller pairs gives a trace of exactly `d`
consecutive controller directions.

In the coordinate-disjoint Johnson realization:

* a lower controller trace has rank lower by `d`;
* an upper controller trace has rank higher by `d`.

Thus the restriction determines `d`.  Compiler injectivity then recovers
the controller start, orientation, and controller cycle.  The boundary
side and the remaining number `q-d` are fixed, so the macro start is
recovered.  A core-only window has controller depth zero and cannot
collide with it.

Frozen four-bit base-cycle tags distinguish the sixteen `Q_8` base
cycles.  Different controller cycles already have disjoint literal
controller states.  With these tags included in the coordinate budget,
the mixed-boundary decoder is complete.

## 3. Same-oriented payload seams

Inside the first `Sigma`, every payload run is increasing.  Inside the
second, every run is decreasing.  Hence each internal seam has collars

\[
                         \uparrow|w_t|\uparrow
 \quad\text{or}\quad
                         \downarrow|w_t|\downarrow.    \tag{3.1}
\]

The `w_0` occurrence at the beginning of each `Sigma` has a controller
collar and is covered by Section 2; treating it in the uniform count only
overestimates the collision charge.

For an increasing seam, write `a+b=q-1`.  The left lower restriction is

\[
                         1^{L-a}0^a,                  \tag{3.2}
\]

and the right upper restriction is

\[
                         1^b0^{L-b}.                  \tag{3.3}
\]

Thus the lower target determines `a`, while the upper target determines
`b`; since `q` is fixed, either sign determines the split.  Complementing
gives the decreasing case.  Earlier all-one and later all-zero payload
blocks identify the seam index and distinguish the two antipodal copies.

A depth-`q` window cannot meet two `Q_8` seams because consecutive seams
are `L+1` edges apart and `q<=H<=L`.  Only the adjacent endpoint cases can
collide with a nonseam window.  Therefore the source bound of at most two
collisions per seam and sign is safe.  With at most sixteen seam
occurrences,

\[
                         E_q^-+E_q^+\le64              \tag{3.4}
\]

per macrocycle is valid, albeit nonoptimal.

For `M` owner-disjoint macros, `G=2DM`, and summing (3.4) gives

\[
 \sum_{q\le H}(E_q^-+E_q^+)
 \le64HM={32H\over D}G.                               \tag{3.5}
\]

No depth has been double-counted on behalf of another.

## 4. Isometry and the actual support

The first-half word `Pi` contains exactly once:

* all `r` controller directions;
* all eight `Q_8` directions; and
* all `8L` payload directions.

They are physically disjoint, so `Pi` is a permutation of `D` directions.
The doubled word `Pi Pi` is therefore a simple isometric `C_(2D)`.

It does **not** span the ambient `Q_D`.  Its support size is `2D`, whereas
`Q_D` has `2^D` vertices.  The first failure occurs already at `D=3`:
the doubled word

\[
                         123123
\]

from `000` visits

\[
 000,100,110,111,011,001,000,                          \tag{4.1}
\]

and omits `010` and `101`.  For the present `D=Theta(m)`, the gap is
exponential.

The theorem's disjointness assertion is nevertheless correct.  Every
macro owner projects to the chosen `Q_8` cycle and controller cycle; two
macros with disjoint projection in either factor cannot meet.  This gives
an exact cycle factor of the declared union, not a factor of the full
Cartesian owner packet.

## 5. Coordinate and phase budgets

There are `D` active split pairs.  Four frozen split tag pairs use eight
more physical coordinates and contribute four selected coordinates to
every owner.  To embed in the middle layer of `[2m]`, one needs

\[
                         D+4\le m.                    \tag{5.1}
\]

The original choice

\[
                         L=\left\lfloor{m-r-8\over8}\right\rfloor
\]

ensures only `D<=m`, so it can violate (5.1).  Formula (0.1) repairs this
and also makes `L` even.  The unused coordinates number

\[
                         2(m-D-4),                    \tag{5.2}
\]

and one may freeze any `m-D-4` of them into the exterior core.

The evenness condition addresses the phase warning already present in
the owner-carousel audit.  Seam `w_t` occurs at position `t(L+1)` in the
payload-expanded first half.  If `L` is even, this position has parity
`t`, as in the original phase-indexed ledger.  If `L` is odd, every such
position is even.  The smallest mismatch is `L=1`: `w_1` occurs at
position two although the inherited stage ledger expects odd parity.
The prescribed doubled word remains an isometric cube cycle, but the
claimed inherited payload frame requires a reset not constructed in the
source theorem.

## 6. Final boundary

After reserving the tags and taking `L` even, the following are proved:

1. exact literal decoding at both global turnarounds for every `q<=H`;
2. exact mixed controller/core decoding;
3. same-oriented internal seam collision at most `64` per depth and
   macrocycle;
4. a simple isometric `C_(2D)` on each declared support; and
5. aggregate new seam collision `O(HG/m)=o(G)`.

Still open:

1. an owner-disjoint packing of these `2D`-owner sparse cycles on
   `W-o(W)` middle owners;
2. a factorization of any full `Q_D` support--none is supplied here;
3. inherited payload collisions and cross-macrocycle target collisions;
4. escape from the standard carousel's bottom-kernel obstruction; and
5. `CPM`/`EMSF`.

