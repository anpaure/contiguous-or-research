# Self-audit: all two-sided Boolean subcubes pass protected Ore

**Date:** 2026-08-04  
**Verdict:** self-audit **GO**, pending independent audit.

## Algebraic checks

Put \(\rho=m-c\), \(a=\binom v{\rho-1}\).  The singleton-gluing
criterion contributes at most

\[
 {\rho-1\over c}\,c{v\choose\rho}
 =a{(\rho-1)(m-u)\over\rho}.
\]

The available singleton margin is \((m-12)a\).  Their comparison is
equivalent to

\[
 u+{m-u\over\rho}\ge12.
\]

If this fails, then \(u\le11\) and
\(\rho>(m-u)/(12-u)\ge(m-11)/12\).

If also \(c\le u\), both parameters are bounded, \(a\) is a central
binomial coefficient up to bounded shifts, and the exact normalized slack
is at least \(2/(m-1)\).  This dominates the
\(2^{m+o(m)}\)-edge protected bank.

If \(c>u\), then \(u\le10\).  The audited two-boundary criterion is exactly

\[
 a(c-u)\ge\rho N_\rho.

The failed singleton condition bounds \(\rho/m\) below by a fixed positive
constant (for example `1/13` for all sufficiently large `m`).  Uniform
Stirling estimates give \(a/N_\rho=2^{\Omega(m)}\), so
the inequality follows.

## Quantifier and scope checks

All three ingredients use the same alternative-random constant-spread
reservoir.  The common-\(G_2\) bank is not mixed into the proof.  Endpoint
cuts \(c=0\) and \(u=0\) are imported from the same frozen reservoir
theorem.  The result is only for two-sided Boolean subcubes; it makes no
arbitrary-family classification, factor-component, residence-gluing, or
common-cap claim.
