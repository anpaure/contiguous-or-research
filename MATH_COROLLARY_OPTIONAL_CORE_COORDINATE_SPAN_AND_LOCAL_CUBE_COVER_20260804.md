# Optional cores require a two-deadline coordinate span

**Date:** 2026-08-04  
**Method:** pure mathematics; exact corollary of the sharp partial-shadow
bound  
**Status:** unconditional, subject only to the cited sharp optional-core
theorem.  This is a localization obstruction, not an elimination of the
global optional core.

## 0. Outcome

Let `B` be a family contained in one rank of a Boolean lattice and suppose

\[
 |B|\ge {2D-1\choose D-1}+1,\qquad D\ge2.             \tag{0.1}
\]

Write

\[
 C(B)=\bigcap_{S\in B}S,\qquad
 U(B)=\bigcup_{S\in B}S,
 \qquad h(B)=|U(B)\setminus C(B)|.                    \tag{0.2}
\]

Then

\[
                         \boxed{h(B)\ge2D.}           \tag{0.3}
\]

More generally, if `B` is covered by `t` Boolean intervals whose free
coordinate dimensions are at most `h`, then

\[
 \boxed{
 t\ge
 \left\lceil
 {\binom{2D-1}{D-1}+1
  \over
  \binom{h}{\lfloor h/2\rfloor}}
 \right\rceil.}                                      \tag{0.4}
\]

For the optional bootstrap core, `D=d-3`; hence every positive core obeys

\[
 \boxed{
 \left|\bigcup B^-\setminus\bigcap B^-\right|
 \ge2d-6.}                                           \tag{0.5}
\]

If it is covered by active apertures of dimension at most `d-3+C`, for a
fixed constant `C`, their number is

\[
                    \boxed{t\ge 2^{d-C+O(1)}}.        \tag{0.6}
\]

Thus a surviving optional obstruction cannot be localized inside one
deadline-sized packet, or inside any bounded number of such packets.  Any
proof which shows that all optional damage is supported on `O(1)` local
`d+O(1)`-coordinate apertures automatically eliminates the core for all
sufficiently large dimensions.

## 1. A fixed-rank slice of a Boolean interval

### Lemma 1.1

Let `F` be a family of sets of one common rank, and suppose

\[
                         X\subseteq S\subseteq Y
                         \qquad(S\in F),              \tag{1.1}
\]

where `|Y-X|=h`.  Then

\[
 |F|\le {h\choose t}
      \le {h\choose\lfloor h/2\rfloor},              \tag{1.2}
\]

where `t=|S|-|X|` is independent of `S`.

#### Proof

The map `S -> S-X` injects `F` into the rank-`t` layer of the Boolean
lattice on `Y-X`.  This proves the first inequality.  Unimodality of the
binomial coefficients proves the second. \(\square\)

### Lemma 1.2

For positive integers `h`, the central binomial coefficient

\[
                         c_h={h\choose\lfloor h/2\rfloor}
                                                               \tag{1.3}
\]

is strictly increasing.  In particular, if `h<=2D-1`, then

\[
                         c_h\le {2D-1\choose D-1}.    \tag{1.4}
\]

#### Proof

For `h=2a`,

\[
 {2a+1\choose a}/{2a\choose a}={2a+1\over a+1}>1,
\]

and for `h=2a+1`,

\[
 {2a+2\choose a+1}/{2a+1\choose a}=2>1.
\]

This proves strict monotonicity and (1.4). \(\square\)

## 2. Coordinate-span theorem

### Theorem 2.1

Equation (0.1) implies (0.3).

#### Proof

Every member of `B` lies in the Boolean interval

\[
                         [C(B),U(B)].                 \tag{2.1}
\]

Its free-coordinate dimension is `h(B)`.  Lemma 1.1 gives

\[
 |B|\le {h(B)\choose\lfloor h(B)/2\rfloor}.          \tag{2.2}
\]

If `h(B)<=2D-1`, Lemma 1.2 makes the right side at most
`binom(2D-1,D-1)`, contradicting (0.1).  Therefore `h(B)>=2D`.
\(\square\)

The strict `+1` in (0.1) is essential for the last unit.  Without it, the
lifted middle layer of a `(2D-1)`-dimensional interval attains equality and
has coordinate span exactly `2D-1`.

## 3. Local-cube cover number

### Theorem 3.1

If `B` is covered by Boolean intervals

\[
                         [X_i,Y_i],\qquad
                         |Y_i-X_i|\le h
                         \quad(1\le i\le t),          \tag{3.1}
\]

then (0.4) holds.

#### Proof

Apply Lemma 1.1 to the fixed-rank family
`B cap [X_i,Y_i]`.  Each interval contains at most
`binom(h,floor(h/2))` members of `B`.  The union bound gives

\[
 |B|\le t{h\choose\lfloor h/2\rfloor}.               \tag{3.2}
\]

Combine this with (0.1) and take ceilings. \(\square\)

For fixed `C` and `h=D+C`, the central-binomial estimates give

\[
 {\binom{2D-1}{D-1}
  \over
  \binom{D+C}{\lfloor(D+C)/2\rfloor}}
 =2^{D-C+O(1)},                                      \tag{3.3}
\]

which proves (0.6) after substituting `D=d-3`.  No uniformity or
disjointness of the covering intervals is required.

## 4. Application and exact scope

The sharp optional threshold-shadow theorem proves

\[
 |B^-|\ge {2d-7\choose d-4}+1
          ={2D-1\choose D-1}+1,
 \qquad D=d-3.                                      \tag{4.1}
\]

Theorem 2.1 gives (0.5), and Theorem 3.1 gives the local-aperture cover
bound.

This eliminates every proposed optional obstruction for which an
independent theorem confines all of `B^-` to a bounded collection of
deadline-sized Boolean intervals.  It does **not** prove that the present
global reservoir has such a localization.  Different vertices of the
bootstrap core may propagate through different owner gaps and collectively
use at least `2d-6` coordinates.  Establishing a bounded local cover, or
exploiting this forced global spread against the trace chronology, remains
the next step.

## 5. Dependency

- `MATH_THEOREM_SHARP_OPTIONAL_THRESHOLD_SHADOW_VIA_PARTIAL_SHADOW_20260804.md`
