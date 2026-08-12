# Rayleigh residual jobs have a canonical geometric two-piece factorization

**Date:** 2026-08-05  
**Method:** pure mathematics; no search or solver  
**Status:** unconditional exact sufficient reduction.  Every job in the
first overlap-cancelled Rayleigh residual splits canonically at the minimum
of the original signed-tail kernel.  This converts the compact
two-to-three-socket problem into a one-to-three-halves fragmentation
problem with an explicit two-branch job density.  A fragmentation kernel
for that new pair would solve the Rayleigh coagulation, but is not proved
here.

## 1. The first transformed residual

Let `K` be the Rayleigh signed-tail kernel, let `b` be its first zero, and
let `c` be its unique minimum.  For `m<u<0`, write

\[
 K(\ell(u))=K(r(u))=u,
 \qquad \ell(u)<c<r(u),
\]

and

\[
 t=z(u)=r(u)-\ell(u).
\]

The map `z` is strictly increasing.  Put

\[
 u_b=z^{-1}(b),
 \qquad
 e=\ell(u_b),
 \qquad
 R=r(u_b)=e+b.
\]

After cancelling the transformed one-piece overlap on `(0,b)`, the
remaining job measure is parametrized exactly by

\[
 u\in(u_b,0),
 \qquad
 t=z(u)>b,
\]

with occurrence measure `du`.  Its mass is

\[
 J=-u_b.
\]

The remaining socket density is

\[
 g_2(y)=-K'(y)-u'(y),\qquad0<y<b,
\]

and its mass `S` satisfies

\[
 2J<S<3J.                                         \tag{1.1}
\]

## 2. Split every residual job at the old minimum

Define

\[
 d_-(u)=c-\ell(u),
 \qquad
 d_+(u)=r(u)-c.                                   \tag{2.1}
\]

Then

\[
 \boxed{z(u)=d_-(u)+d_+(u)}                       \tag{2.2}
\]

literally for every occurrence.  Let `eta_-` and `eta_+` be the
pushforwards of Lebesgue measure on `(u_b,0)` under `d_-` and `d_+`, and
put

\[
 \eta=\eta_-+\eta_+.
\]

### Proposition 2.1 (explicit natural-piece density)

The two branch densities are

\[
 \boxed{
 \eta_-(dy)=
 -K'(c-y){\bf1}_{(c-e,\,c-b)}(y)\,dy,}            \tag{2.3}
\]

and

\[
 \boxed{
 \eta_+(dy)=
 K'(c+y){\bf1}_{(R-c,\,\infty)}(y)\,dy.}          \tag{2.4}
\]

In particular,

\[
 \eta(0,\infty)=2J,                               \tag{2.5}
\]

and `eta_+` is the only unbounded branch and has a Gaussian tail.

### Proof

On the left inverse branch,

\[
 {d\ell\over du}={1\over K'(\ell)}<0,
 \qquad
 {dd_-\over du}=-{d\ell\over du}
 ={1\over-K'(\ell)}.
\]

Thus the pushforward density at `y=c-ell` is `-K'(c-y)`.  As `u`
runs from `u_b` to zero, `ell` runs from `e` down to `b`, giving the
support in (2.3).

Similarly,

\[
 {dr\over du}={1\over K'(r)}>0,
 \qquad
 {dd_+\over du}={1\over K'(r)},
\]

so the density at `y=r-c` is `K'(c+y)`.  The right endpoint runs from
`R` to infinity, proving (2.4).  Each branch has the parameter mass
`-u_b=J`, proving (2.5). `square`

### Proposition 2.2 (exact work identity)

The natural-piece measure and the residual socket measure have equal first
moments:

\[
 \boxed{
 \int_0^\infty y\,d\eta(y)
 =\int_0^b y g_2(y)\,dy.}                          \tag{2.6}
\]

### Proof

Using (2.2),

\[
 \int y\,d\eta(y)
 =\int_{u_b}^0\bigl(d_-(u)+d_+(u)\bigr)du
 =\int_{u_b}^0z(u)du.
\]

The last integral is exactly the work of the transformed jobs with
`z(u)>b`.  Cancellation of the common one-piece density preserves work,
so it equals the work of `g_2(y)dy`. `square`

## 3. Exact lifting theorem

### Theorem 3.1 (geometric fragmentation lift)

Suppose there is a finite-configuration coagulation kernel from the
natural-piece job measure `eta` to the residual socket measure

\[
 g_2(y){\bf1}_{(0,b)}dy.
\]

Then the first transformed residual job measure has a finite-configuration
coagulation, and hence the original Rayleigh pair has one.

### Proof

Disintegrate the assumed kernel over the value of a natural piece.  For
each original occurrence parameter `u`, sample independently from the
two conditional kernels belonging to `d_-(u)` and `d_+(u)`, and concatenate
their finite socket lists.  Their total is

\[
 d_-(u)+d_+(u)=z(u),
\]

so they coagulate the transformed job.  Aggregating over `du` uses the
socket marginal of the assumed kernel exactly once because the aggregate
natural-piece marginal is `eta`.

Now restore the cancelled transformed one-piece configurations, append
the first equal-level primary socket, and restore the original one-piece
overlap.  These are the exact lifting operations from the primary
subtraction theorem.  Every list remains finite. `square`

The implication is intentionally one-way.  A coagulation of a transformed
job need not respect its split at `c`.

## 4. The count problem becomes one-versus-two fragmentation

Equations (1.1), (2.5) give

\[
 \boxed{
 1<{S\over\eta(0,\infty)}<{3\over2}.}             \tag{4.1}
\]

Thus, at the scalar level, the natural pieces need only an average between
one and one-and-a-half output sockets.  If a fragmentation uses only one-
and two-socket outputs, the forced fractions are

\[
 \begin{aligned}
 \text{one-socket fraction}
 &=2-{S\over2J},\\
 \text{two-socket fraction}
 &={S\over2J}-1.
 \end{aligned}                                    \tag{4.2}
\]

Equivalently, a one-piece cancellation of mass

\[
 H_*=2\eta(0,\infty)-S=4J-S                      \tag{4.3}
\]

would leave exactly two socket occurrences per remaining natural piece.
Consequently a concrete next test is

\[
 \boxed{
 (\eta\wedge g_2dy)(0,\infty)\ge4J-S.}            \tag{4.4}
\]

If (4.4) holds, choose a common submeasure of mass `4J-S` and cancel it
as one-piece configurations.  The uncancelled measures retain equal work
and have socket count exactly twice job count.  One still must construct
their two-socket sum coupling; count equality alone does not do this.

Thus (4.4) is a useful literal overlap gate, not a completion theorem.

## 5. Relation to the high-tail construction

Only `eta_+` is unbounded, and its density `K'(c+y)` is Gaussian.  The
residual socket density has positive terminal lower limit at `b`.
Therefore the existing equal-split tail theorem applies directly to all
sufficiently remote bands of `eta_+`.  The remaining geometric
fragmentation problem is compact.

This route differs from splitting the transformed job itself into equal
pieces: its two primary pieces are dictated by the old minimum and retain
the exact equal-level geometry.  It also avoids the false assertion that
the whole residual socket density is monotone.

## 6. Exact frontier

The natural factorization reduces the Rayleigh compact problem to one
explicit pair:

\[
 \boxed{
 \eta(dy)=
 -K'(c-y){\bf1}_{(c-e,c-b)}dy
 +K'(c+y){\bf1}_{(R-c,\infty)}dy
 }
\]

against

\[
 \boxed{
 g_2(y)dy=\bigl(-K'(y)-u'(y)\bigr)
              {\bf1}_{(0,b)}dy.
 }

They have equal work and count ratio in `(1,3/2)`.  The surviving theorem
is an explicit fragmentation coupling for this pair, preferably after
the one-piece overlap (4.4) and Gaussian-tail removal.  No such coupling
is claimed here.

## 7. Frozen dependencies

1. `MATH_THEOREM_RAYLEIGH_EQUAL_LEVEL_PRIMARY_SUBTRACTION_20260805.md`.
2. `MATH_THEOREM_RAYLEIGH_FIRST_TRANSFORM_EXACT_TWO_THREE_COUNT_WINDOW_20260805.md`,
   SHA at use
   `1931d629efdcf12c2ec0167a004ead83e547050d44bc23464252dc0a1e062a10`.

