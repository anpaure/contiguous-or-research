# Independent GO audit: six-slot `h=4` inactive quarter boundary

**Date:** 2026-08-04  
**Audited source:**
`MATH_THEOREM_SIX_SLOT_H4_INACTIVE_QUARTER_BOUNDARY_COMPLETE_POSITIVITY_20260804.md`  
**Audited SHA256:**
`60ebf810ad63bafd01fa19661780fad8a0fc1a52c2266f1a58995cc5fe635dc1`

## Verdict

**PASS / GO in the exact stated scope.**  On `u=P/4`, the complementary
ceiling gives `P<=4A/5`; together with `P>=2tau/3` this yields

\[
\tau\le6A/5,quad \tau/6\le u\le A/5,quad
5\tau/6\le P+u\le A.
\]

Thus both upper shifts lie in the independently verified brace range.

For `u/A` between `1/6` and `1/5`, the compact kernel decreases.  Its
endpoint value exceeds `9/125`; the complete period tail is below
`19/1000`.  Hence

\[
F_\tau(u)>{53\over1000}.
\]

For the upper shift, `(P+u)/A>17/20`; the compact bound is greater than
`-13/250`, while its complete period tail is below `1/1000`.  Therefore

\[
F_\tau(P+u)>-{53\over1000},qquad
F_\tau(u)+F_\tau(P+u)>0.
\]

If the low minimum is `C(tau)`, the two brace bounds give
`mathfrak R>21/20000`.  If it is `F_tau(u)`, one brace bound plus the
strict complementary-pair positivity gives

\[
\mathfrak R>{11\over20000}-{1\over20000}
={1\over2000}>0.
\]

The two cases include the low switch.  Together with the closed active
side, this closes the full quarter boundary and its complement-boundary
junction.  It does not sign the moving `P=2tau/3` face or the remaining
low-switch face.
