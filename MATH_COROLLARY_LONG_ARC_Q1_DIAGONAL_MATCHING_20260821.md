# A diagonal q=1 matching of unbounded physical arcs

**Date:** 2026-08-21  
**Status:** unconditional qualitative q=1 matching corollary; no Gaussian-H
collar and no global wreath-factor completion

## 0. Corollary

Use the notation and the simple q=1 arc hypergraph from
`MATH_THEOREM_LONG_ARC_Q1_PROFILE_AND_ALL_DEPTH_RETIREMENT_GATE_20260821.md`.
Thus \(b=2r+1\), an edge contains \(\ell\) rank-r middle targets and
\(\ell\) rank-\((r-1)\) lower targets, and parameter multiplicity has been
quotiented out.

### Theorem 0.1 (slow diagonal long arcs)

There is an integer function

\[
                         \ell(r)\longrightarrow\infty,
 \qquad \ell(r)=o(r),                                  \tag{0.1}
\]

and a matching in the simple q=1 \(\ell(r)\)-arc hypergraph which leaves
only o(A) middle targets and o(A) lower targets uncovered, where
\(A=\binom{2r+1}r\).

Hence there is a target-disjoint family of genuine physical sliding-window
fragments whose lengths tend to infinity and which covers asymptotically all
of both q=1 shores.  Trimming any \(w(r)=o(\ell(r))\) starts per fragment
costs o(A) additional targets.

The theorem is deliberately qualitative.  Its diagonal \(\ell(r)\) may
grow arbitrarily slowly, so it does not imply
\(H(r)=o(\ell(r))\) for the prescribed
\(H(r)\asymp\sqrt{r\log r}\).  It also does not complete the fragments into
an exact factor of length-b wreaths.

## 1. Fixed arc length

Fix \(\ell\).  The exact formulas in the arc-profile theorem give, after
division by the common multiplicity \((r-\ell)!\),

\[
 {d_L\over d_M}={r+2\over r}=1+O(1/r),
 \qquad
 {\Delta_2\over d_M}=O_\ell(1/r).                    \tag{1.1}
\]

The simple hypergraph is \(2\ell\)-uniform, its minimum degree tends to
infinity, all vertex degrees are asymptotic, and its maximum pair codegree
is o of the common degree.  The standard fixed-uniformity
Pippenger--Frankl--Rödl almost-perfect matching theorem therefore gives,
for each fixed \(\ell\), a matching leaving

\[
                    o_\ell(|\mathcal M|+|\mathcal L|)=o_\ell(A)  \tag{1.2}
\]

vertices uncovered as \(r\to\infty\).  In particular the uncovered count
on each shore is o(A).

This invocation keeps \(2\ell\) fixed.  No growing-uniformity theorem is
being assumed.

## 2. Quantifier-safe diagonalization

For integer \(j\ge2\), apply the fixed-uniformity theorem with

\[
                         \ell=j,qquad \varepsilon_j=1/j.
\]

Choose thresholds \(R_j\) strictly increasing so that

1. \(R_j\ge j^2\); and
2. for every \(r\ge R_j\), the j-arc hypergraph has a matching leaving at
   most \((|\mathcal M|+|\mathcal L|)/j\) vertices uncovered.

Put

\[
 \ell(r)=\max\{j:R_j\le r\},                              \tag{2.1}
\]

using \(\ell(r)=1\) before the first threshold.  Then \(\ell(r)\to\infty\),
and \(R_{\ell(r)}\ge\ell(r)^2\) gives

\[
                         \ell(r)\le\sqrt r=o(r).       \tag{2.2}
\]

The chosen matching leaves at most

\[
 { |\mathcal M|+|\mathcal L|\over\ell(r)}=o(A)        \tag{2.3}
\]

vertices.  This proves Theorem 0.1.

There are \(O(A/\ell(r))\) selected fragments.  Deleting at most \(w(r)\)
starts from each therefore costs

\[
                  O\!\left({w(r)A\over\ell(r)}\right)=o(A)  \tag{2.4}
\]

when \(w(r)=o(\ell(r))\).

## 3. Scope

The corollary proves a genuine q=1 physical-fragment packing with unbounded
fragment length.  It does not provide a rate for \(\ell(r)\), a collar at
the target Gaussian H, correlated coverage at q>=2, a declining retirement
schedule, or a completion of the partial middle matching into a global
wreath factor.  Those are separate gates and are not hidden inside the
diagonal argument.

The exact degree and codegree inputs are audited by
`scratch/audit_long_arc_q1_profile_and_all_depth_gate_20260821.py`.
