# Independent audit: two-level cube exponential optional core

**Date:** 2026-08-04  
**Method:** independent symbolic proof replay; no computation, search, or
solver  
**Audited theorem:**
`MATH_THEOREM_OPTIONAL_BOOTSTRAP_TWO_LEVEL_CUBE_EXPONENTIAL_CORE_20260804.md`

## Verdict

**GO.**  Every implication is valid with the stated scope.  The argument
uses only the induced-edge inequality for the Boolean cube, the two adjacent
rank layers, and the exact optional-core degree ledger.  It proves

\[
 |B|+|Q|\ge2^D,
 \qquad
 |B|\ge\frac{2^D}{1+m/D},
\]

and therefore

\[
 |B^-|\ge\frac{2^{d-3}}{1+m/(d-3)}
        =2^{\Omega(\sqrt m)}.
\]

It does not prove the sharper central-binomial candidate.

## 1. Cube edge inequality

Split a finite cube family `S` into sections of sizes `a<=b`.  There are at
most `a` crossing matching edges.  The inductive estimate reduces exactly
to

\[
 t\log_2t+2t\le(1+t)\log_2(1+t),\qquad t=a/b\in[0,1].
\]

After multiplying by `ln 2`, the right-minus-left function is

\[
 f(t)=(1+t)\ln(1+t)-t\ln t-2t\ln2.
\]

It has `f(0)=f(1)=0` and

\[
 f''(t)=-\frac1{t(1+t)}<0.
\]

A concave function lies above the chord between its endpoints, so `f>=0`.
The induction and the factor `1/2` are correct.

## 2. Two-level specialization

For

\[
 B\subseteq\binom{[2m-1]}{m-1},\qquad
 Q\subseteq\binom{[2m-1]}m,
\]

the cube graph induced by `B union Q` has no same-shore edges; its edges are
exactly containments `x subset U`.  If `n=|B|`, `q=|Q|`, and `N=n+q`, then

\[
 E\ge Dq\ge DN/2
\]

because `q>=n`.  Cube isoperimetry gives

\[
 E\le N\log_2N/2,
\]

so `N>=2^D`.  There is no hidden regularity or induced-neighbourhood
assumption in this step.

Each lower vertex has exactly

\[
 (2m-1)-(m-1)=m
\]

upper neighbours in the full Boolean lattice.  Hence `E<=mn`, while
`E>=Dq`, giving `q<=mn/D`.  Consequently

\[
 2^D\le n+q\le n(1+m/D),
\]

which is the claimed lower bound on `n`.

## 3. Optional-core substitution

For the minimal positive optional core, the preceding bootstrap theorem
gives:

1. at least `|B^-|+1` positive-capacity owners; and
2. at least `d-3` members of `B^-` in every such owner.

Thus the theorem applies with `D=d-3`.  Since `d=Theta(sqrt m)`, one has
`m/(d-3)=Theta(d)` for all sufficiently large `m`; dividing `2^(d-3)` by
this polynomial factor retains `2^{Omega(sqrt m)}` growth.

## 4. Exact scope

The proof does not use strict two-Hall beyond the already-derived facts
`|Q|>|B^-|` and minimum positive-owner degree `d-3`.  It consequently also
applies to any Boolean two-level pair satisfying those two numerical rows.

The affine-plane abstract counterexample is irrelevant because its
incidence graph is not an induced subgraph of two consecutive Boolean
levels with containment edges.  Conversely, this cube-edge theorem alone
cannot yield

\[
 |B|\ge\binom{2D-1}{D-1};
\]

the latter would require a genuinely rank-sensitive two-level
edge/threshold-shadow inequality, whereas the general cube inequality
forgets that all vertices lie in only two ranks.
