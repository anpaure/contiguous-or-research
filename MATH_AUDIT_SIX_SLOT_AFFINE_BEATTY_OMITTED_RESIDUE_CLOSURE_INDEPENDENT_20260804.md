# Independent audit: six-slot affine Beatty omitted-residue closure

**Date:** 2026-08-04  
**Verdict:** **GO.**  The explicit affine setup-cost clock at grid six has
strictly positive Bellman functional.  The residue partition, compact and
tail expansion, degree-seventeen Taylor direction, exact rational
certificate, and final all-ceiling comparison all check.

## 1. Exact binding and dependencies

Audited theorem:

`MATH_THEOREM_SIX_SLOT_AFFINE_BEATTY_OMITTED_RESIDUE_CLOSURE_20260804.md`

SHA-256:

`0bfc91a873e559234f89231abeb6f14ef30ef43c7b727e8a8c391e7e0e0b5c46`

Its frozen dependency hashes match the current workspace:

| role | SHA-256 |
|---|---|
| affine setup-cost clock | `408aacd10f2e20bf26364f6464d06a7d0fb9c4d179e93e21b8a26482ce7405ce` |
| strict arithmetic all-ceiling theorem | `c3a2c1858f59fa32e61d2f9a9252085ad7fb01f3521ab5cb46998705123e103d` |

No theorem byte was changed during this audit.

## 2. Residue partition identity

In units `d=A/10`, the affine clock uses the five residue classes

\[
                         0,1,3,5,7\pmod 9.
\]

The omitted train uses

\[
                         2,4,6,8\pmod 9.
\]

These are disjoint and exhaust `Z/9Z`, so absolute convergence permits
the exact regrouping

\[
                         C(d)=\Phi_6+\Omega.
\]

No multiplicity or initial term is lost: `K(0)` belongs to the selected
zero residue.

## 3. Compact and first-tail expansion

For omitted compact residues `r=2,4,6,8`, the two normalized Gaussian
arguments in `K(rd)` are

\[
 \{1-r/10,1+r/10\}.
\]

Their union is exactly

\[
 \left\{{1\over5},{2\over5},{3\over5},{4\over5},
 {6\over5},{7\over5},{8\over5},{9\over5}\right\}.
\]

The first tail row `q=1` has normalized arguments

\[
 1+{9+r\over10}
 \in\left\{{21\over10},{23\over10},{5\over2},{27\over10}\right\}.
\]

Every `q>=2` summand lies strictly above `A` and is a strictly negative
Gaussian tail.  Retaining the four compact constants, their eight
Gaussians, and the four first-tail Gaussians therefore gives the
proof-safe strict upper bound

\[
 \Omega<4-\sum_{t\in\mathcal T}e^{-\pi t^2/4}
\]

with exactly the theorem's twelve-element set `mathcal T`.

## 4. Exact `Q_17` certificate

For

\[
 Q_{17}(x)=\sum_{j=0}^{17}{(-x)^j\over j!},
\]

Taylor's theorem gives

\[
 e^{-x}=Q_{17}(x)+{e^{-\xi}x^{18}\over18!}>Q_{17}(x)
 \qquad(x>0).
\]

The sign is correct precisely because the retained degree is odd and the
degree-eighteen remainder is positive.  Since `pi<22/7`,

\[
 {\pi t^2\over4}<{11t^2\over14},
\]

and monotonicity of the exponential gives

\[
 e^{-\pi t^2/4}>e^{-11t^2/14}>Q_{17}(11t^2/14).
\]

I independently reconstructed the exact rational sum over the twelve
arguments.  After subtracting `401/100` it is

\[
 {1107521168275515646975339594998344921314175828988640776532351139
  \over
  2464861067577089663016747663360000000000000000000000000000000000000},
\]

exactly matching the theorem, with positive numerator and denominator.
Thus

\[
 \sum_{t\in\mathcal T}e^{-\pi t^2/4}>{401\over100},
 \qquad
 \Omega<-{1\over100}.
\]

No decimal estimate, sampled interval, or truncated-tail sign assumption
enters this comparison.

## 5. Positivity and the general residue identity

The arithmetic all-ceiling theorem gives `C(A/10)>0`.  Hence

\[
 \Phi_6=C(A/10)-\Omega
       >C(A/10)+{1\over100}>{1\over100}.
\]

This closes the explicit affine grid-six clock, not the complete `h=5`
branch.

For the balanced all-grid family, write `m=qh+r`, `0<=r<h`.  The exact
Beatty clock satisfies

\[
 {V_{qh}\over d_h}=q(2h-1),
 \qquad
 {V_{qh+r}\over d_h}=q(2h-1)+(2r-1)\quad(r>0).
\]

Thus its selected residues modulo `2h-1` are exactly zero and the positive
odd residues through `2h-3`; the omitted residues are exactly the positive
even residues through `2h-2`.  This independently verifies the general
identity

\[
                         C(d_h)=\Phi_h+\Omega_h.
\]

Only `h=5` is signed by the theorem's finite certificate.  No conclusion
about all balanced affine clocks, every six-slot branch, the universal
Bellman inequality, or an OR-word upper bound is inferred.
