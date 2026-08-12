# Independent audit: anchored negative-component rearrangement operator

**Date:** 2026-08-05  
**Method:** independent line-by-line mathematical audit; no search or solver  
**Audited source:**
`MATH_THEOREM_ANCHORED_NEGATIVE_COMPONENT_REARRANGEMENT_OPERATOR_20260805.md`  
**Audited SHA-256:**
`d25d240c3bafc39e4b581dfa5fbb0379dfa6dd9a76e00458d24227a146e0ba8b`  
**Verdict:** **GO, with the iteration-domain qualification already stated
in Theorem 5.1.**  The rearrangement inequality, mass identity, exact
variation identity, first Rayleigh iterate, and box-norm implication are
correct.  The Rayleigh orbit convergence is not proved by the source.

## 1. Component and atom conventions

For a relative-open negative superlevel component `I` of length `ell`,
write it as `(x,x+ell)` when `x>0`; a component meeting the boundary is
`[0,ell)` in the relative topology.  In either case

\[
 \rho(I)\le \rho((x,x+\ell])\le\rho([0,\ell])
\]

in the first case, while `rho(I)<=rho([0,ell])` is immediate in the
boundary case.  Thus atoms at a right endpoint cause no problem.  The
weak convention `t<=ell` in `C_H` gives exactly

\[
 \int C_H(t)\,d\rho(t)
 =\int_0^\infty\sum_j\rho([0,\ell_{s,j}])\,ds.
\]

Tonelli is applicable because every integrand is nonnegative.  With
Lebesgue measure, layer cake gives

\[
 \int C_H=\int H_-.
\]

Subtracting the first display from the unchanged positive part has the
direction claimed in Theorem 2.1.

## 2. Variation and first Rayleigh iterate

The pointwise identity

\[
 |H_+-C_H|=H_++C_H-2\min(H_+,C_H)
\]

and `int C_H=int H_-` prove Proposition 3.1 exactly.

For the Rayleigh kernel, a depth-`s` negative superlevel has the single
component of length `z(-s)`.  Since `z` is increasing and
`u=z^{-1}`,

\[
 t\le z(-s)\quad\Longleftrightarrow\quad
 0<s\le-u(t),
\]

so `C_K(t)=-u(t)`.  This gives the displayed first transform.  The
one-well theorem gives one negative component at every level of that
transform, of total depth `q`; hence

\[
 (\mathcal R^2K)(0)=P-q>0
\]

from the independently authenticated `q<P<2q` window.

## 3. Box-norm passage

If `rho([0,1])=0`, the anchored inequality with unit windows kills every
unit interval and hence all of `rho`.  Otherwise normalize this mass to
one and use the disjoint partition

\[
 [0,1],(1,2],(2,3],\ldots .
\]

Each block has `rho`-mass at most one, including the possible atom at the
origin in the first block.  Therefore

\[
 \left|\int K_n\,d\rho\right|\le\|K_n\|_\square.
\]

Together with the iterated rearrangement inequalities, box convergence
implies the claimed nonnegativity.

## 4. Exact scope qualification

The source initially defines `mathcal R` for continuous integrable
kernels.  A profile `C_H` is always nonincreasing and measurable but need
not be continuous for a completely general input.  Thus the phrase
"every iterate is defined" in Theorem 5.1 is a real hypothesis: one must
either extend the operator to the measurable finite-profile domain or
prove the required regularity for the Rayleigh orbit.  The source does
not silently assume this row; Section 6 explicitly leaves existence and
box convergence of all iterates open.

No conclusion about the truth of the Rayleigh rearrangement-orbit lemma,
or about an OR-word construction, follows from the audited theorem alone.

