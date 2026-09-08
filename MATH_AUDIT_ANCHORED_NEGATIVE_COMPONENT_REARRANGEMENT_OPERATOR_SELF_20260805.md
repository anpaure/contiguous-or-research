# Self-audit: anchored negative-component rearrangement operator

**Date:** 2026-08-05  
**Audited source:**
`MATH_THEOREM_ANCHORED_NEGATIVE_COMPONENT_REARRANGEMENT_OPERATOR_20260805.md`  
**Source SHA at audit:**
`d25d240c3bafc39e4b581dfa5fbb0379dfa6dd9a76e00458d24227a146e0ba8b`  
**Verdict:** GO.  The atom convention, inequality direction, Lebesgue
identity, Rayleigh identification, and box-norm implication are correct.
The Rayleigh orbit convergence itself remains an explicit hypothesis.

## 1. Atom and Tonelli check

For a negative superlevel component `I=(x,x+ell)`,

\[
 \rho(I)\le\rho((x,x+\ell])\le\rho([0,\ell]).
\]

The definition

\[
 C_H(t)=\int\sum_j1_{\{t\le\ell_{s,j}\}}ds
\]

therefore gives exactly

\[
 \int C_Hd\rho
 =\int\sum_j\rho([0,\ell_{s,j}])ds.
\]

This includes atoms of `rho` at component lengths.  With Lebesgue measure,
the weak endpoint is null and

\[
 \int C_Hdt=\int\sum_j\ell_{s,j}ds=\int H_-dx.
\]

Hence

\[
 \int Hd\rho\ge\int(H_+-C_H)d\rho,
 \qquad
 \int\mathcal RH=\int H.
\]

The direction is the one needed for a lower bound.

## 2. Variation check

Pointwise

\[
 |H_+-C_H|=H_++C_H-2\min(H_+,C_H).
\]

Using equality of the `L1` mass of `C_H` and `H_-` gives the exact source
dissipation identity.  No sign or connectedness assumption is used.

## 3. Rayleigh first iterate

At depth `s`, the Rayleigh negative set is the single interval between
the equal-level endpoints.  Its length is `z(-s)`.  Since `z` is strictly
increasing,

\[
 C_K(t)=|\{s:0<s<-m,\ t\le z(-s)\}|=-u(t).
\]

Thus `K_+-C_K` is `K+u` before the first zero and `u` afterward, exactly
the authenticated first transformed kernel.  Its positive endpoint is
`P=K(0)+m`; its negative depth is `q=-u(b)`.  The authenticated count
window `q<P<2q` gives the second-iterate origin `P-q>0` exactly.

## 4. Box-norm implication

After normalizing `rho([0,1])=1`, use the disjoint partition

\[
 [0,1],(1,2],(2,3],\ldots.
\]

The anchored inequality bounds every block mass by one.  Therefore

\[
 \left|\int H\,d\rho\right|
 \le\sum_{j\ge0}\sup_{[j,j+1]}|H|.
\]

Iteration gives `int K d rho >= int K_n d rho`; convergence of the right
side to zero proves nonnegativity.  This argument does not infer box-norm
convergence from `L1` dissipation, and the source explicitly leaves that
as the remaining orbit lemma.

