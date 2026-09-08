# Service-damped first-kill closure and the transported-ROc gate

**Date:** 2026-08-06  
**Method:** signed covariance/generator grouping, damped Green energy, and
operator-order coalescing of same-anchor stars; no computation or search  
**Status:** proof-safe sufficient theorem plus a minimal obstruction.  The
quadratic same-resource star and distinct-resource cross terms do not form
a new spectral gate once the birth coefficients form a capacity-faithful
positive suboperator.  The one remaining row is a transported one-entry
Hardy estimate for the unhit endpoint of a broken private switch.  A
two-coordinate example shows that hit-only `ROc` cannot imply it.

## 1. One coefficient-faithful birth

Use the service-damped pristine Gramian `R=R_a` from
`MATH_THEOREM_SERVICE_DAMPED_JOHNSON_LYAPUNOV_DUHAMEL_REDUCTION_20260806.md`.
Thus

\[
 R={B\over X}+aP^*RP,
 \qquad P=I-{L\over X},
 \qquad a=\rho^2,
\tag{1.1}
\]

and

\[
 L^{1/2}RL^{1/2}\le C I.
\tag{1.2}
\]

At one transition let `A` be the private-switch edges born into the
boundary, with their **actual hypothetical-survivor coefficients**.  The
capacity-faithful birth condition is

\[
 \boxed{0\le A\le L.}
\tag{CFB}
\]

This is stronger than saying that every boundary edge is geometrically a
Johnson edge.  It requires its full future/cylinder coefficient to be no
larger than the coefficient of that same edge in the complete private
generator.

Let `Delta B<=0` be the covariance rows killed at this transition.  The
signed one-step Duhamel source is

\[
 \mathcal S(f)=
 {1\over X}\langle f,\Delta Bf\rangle
 +{a\over X}\langle f,(ARP+P^*RA)f\rangle
 +{a\over X^2}\langle f,ARA f\rangle.
\tag{1.3}
\]

The first term is retained with its favorable sign.  No killed covariance
row is reused edge by edge.

## 2. Dimension-free signed source bound

### Theorem 2.1

Under `(CFB)`, for every `gamma>0`,

\[
 \boxed{
 [\mathcal S(f)]_+
 \le {a\gamma\over X}\langle f,Af\rangle
   +{C a\over\gamma X}\langle f,Rf\rangle
   +{C a\over X^2}\langle f,Af\rangle.}
\tag{2.1}
\]

In particular, with `gamma=d`,

\[
 \boxed{
 [\mathcal S(f)]_+
 \le {Cd\over X}\langle f,Af\rangle
   +{C\over dX}\langle f,Rf\rangle.}
\tag{2.2}
\]

The omitted `X^{-2}` term is absorbed by the first term for the central
range `X>>d^{-1}`.

#### Proof

Drop only the nonpositive covariance term.  By (1.2) and `(CFB)`,

\[
 ARA\le CA
\tag{2.3}
\]

and

\[
 |\langle f,ARPf\rangle|
 \le C\langle f,Af\rangle^{1/2}
       \langle f,Rf\rangle^{1/2}.
\tag{2.4}
\]

For (2.4), factor `A=L^{1/2}C_0L^{1/2}` with
`0<=C_0<=I`, then use Cauchy--Schwarz and

\[
 \langle RPf,L RPf\rangle\le C\langle f,Rf\rangle.
\]

Apply `2uv<=gamma u^2+gamma^{-1}v^2` to the two equal real linear terms,
and use (2.3) on the quadratic term.  This proves (2.1)--(2.2).
\(\square\)

The theorem is deliberately signed: the covariance loss is never replaced
by its absolute value.  The regular `K_3` first-kill example merely shows
that it may vanish; (2.2) remains valid because the damped service term is
kept.

## 3. Same-resource stars and distinct-resource pairs

Write the birth operator literally as

\[
 A=\sum_{e\in\partial_i(G)}w_e b_eb_e^*.
\tag{3.1}
\]

Then

\[
 \langle f,Af\rangle
 =\sum_{e\in\partial_i(G)}w_e(b_e^*f)^2.
\tag{3.2}
\]

No cross term occurs in (3.2).  More importantly, all cross terms in
`ARA`—including many different switches certified by the same physical
blocker resource—are already coalesced by (2.3).  Thus:

* a same-resource rooted star costs only its diagonal one-entry energy
  (3.2), provided its coefficients satisfy `(CFB)`;
* two distinct blocker resources do not require a separate resolvent
  estimate; if `(CFB)` is proved by expanding physical coefficients, their
  coefficient mismatch is exactly the existing `FE3` two-hit face;
* slot and owner-parallel edges remain in their named ledgers.

This avoids the false step “every off-diagonal switch pair is a distinct
physical two-hit.”  Same-resource off-diagonal pairs are handled by
positive-operator order, not mislabeled as `FE3`.

If coefficient mismatch prevents `(CFB)`, the proof-safe replacement is
to split

\[
 A=A^{\rm cap}+A^{\rm root}+A^{\rm two}+A^{\rm slot/owner},
\tag{3.3}
\]

where `A^cap` satisfies `(CFB)`, the same-resource excess is charged by a
rooted-star square, and distinct-resource excess is charged by `FE3`.
Equation (2.1) then applies to `A^cap`; the other three terms retain their
literal ledgers.

## 4. The exact remaining one-entry estimate

The second term in (2.2) is an absorbably small fraction of the damped
counterterm's own service.  Therefore the entire first-kill row closes if
the following estimate holds for the actual predictable vector and every
required marked cylinder:

\[
 \boxed{
 \mathbb E\sum_{i<\tau}{\beta_i d\over X_i}
      \langle f_i,A_i f_i\rangle
 \le C\mathsf A.}
\tag{TROc}
\]

Call `(TROc)` the **transported rooted-overlap estimate**.  It is not raw
boundary sparsity.  Every summand has the actual mark

\[
 b_e^*f_i=f_i(x_e)-f_i(y_e),
\tag{4.1}
\]

where the blocker hits the mate-side resource `y_e` and the surviving
candidate carries the unhit Johnson neighbour `x_e`.

The ordinary one-entry ledger directly sees the `f_i(y_e)^2` part.  The
new content of `(TROc)` is the transported `f_i(x_e)^2` part, with the
same hypothetical-survivor coefficient.  It may be proved by any one of:

1. a coefficient-faithful future-service ticket from `y_e` to `x_e`;
2. a signed covariance allocation which transports the killed mate row;
3. a rooted-star square which includes both endpoints; or
4. a chronological Hardy estimate for the surviving endpoint.

Once `(TROc)` holds, Theorem 2.1, damped service, and the already closed
adapted innovation/HDIR rows prove the base `GDIR` transfer.  Marked
families require the same finite occurrence replay.

## 5. Minimal counterexample to hit-only ROc

The transported endpoint cannot be deleted from the hypothesis.  Take one
Johnson edge `b=e_x-e_y`, let the selected blocker hit `y` but not `x`, and
choose

\[
 f_x=1,\qquad f_y=0.
\tag{5.1}
\]

Then

\[
 (b^*f)^2=1,
\tag{5.2}
\]

while every ledger which prices only the square at the physically hit
resource `y` sees zero.  The example persists inside a regular private
frame by taking the `K_3` model and the vector `(0,1,-1)` from the
first-kill counterexample.

Thus

\[
 \boxed{
 \text{hit-only one-entry control + distinct-hit FE3}
 \not\Longrightarrow (TROc).}
\tag{5.3}
\]

The smallest extra hypothesis is exactly transport of the one-entry ticket
across one Johnson switch, not a stronger spectral bound and not a raw
counting aperture.

## 6. Consequence and proof boundary

The service-damped algebra has now removed:

* the affine `E_1` and even `E_2` inverse-gap losses;
* all same-anchor quadratic cross terms under `(CFB)`;
* the need to sum absolute current-versus-pristine perturbations; and
* any separate `FE3` payment for the capacity-faithful `ARA` term.

The exact unresolved statement is

\[
 \boxed{(CFB)+(TROc)\quad\text{in the actual marked FIFO cylinders}.}
\]

If `(CFB)` fails only on the already classified one-/two-entry coefficient
faces, rooted-star plus `FE3` pricing in (3.3) is sufficient.  Neither
condition is proved here for the literal host, so this note is not an
unconditional `GDIR` or bottom theorem.
