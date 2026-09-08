# Independent algebra audit: two regular factors as a private router

**Date:** 2026-08-04  
**Audited theorem:**
`MATH_THEOREM_TWO_REGULAR_FACTOR_PRIVATE_ROUTER_COMPOSITION_20260804.md`

## 1. Load ledger

For each chain `g-p-s`, assign weight `1/(hq)`.

* claim `g`: `h q` chains, load `1`;
* prefix `gp`: `q` chains, load `1/h`;
* port `p`: `deg_B(p) q` chains, load `deg_B(p)/h <= 1`;
* suffix `ps`: `deg_B(p)` chains, load `deg_B(p)/(hq) <= 1/q`;
* sink `s`: load

  \[
   {1\over hq}\sum_{p:ps\in E_H}\deg_B(p)
   \le {h\deg_H(s)\over hq}\le1.
  \]

Every displayed inequality uses exactly one stated degree hypothesis.

## 2. Integrality audit

After node splitting, all physical and terminal capacities are integral.
The fractional flow has value `|G|`, equal to the total capacity of the
claim-start arcs.  Integral max flow therefore saturates every claim-start
arc.  Unit sink arcs force distinct terminals.  Type legality must be
port-uniform across all gain neighbours because integral flow may choose
any displayed continuation at a port; this is stated explicitly.

## 3. Hall cross-check

For `Y subseteq P`, left `q`-regularity and right degree at most `q` give

\[
       q|Y|\le q|N_H(Y)|.
\]

Thus `H` alone has a matching saturating `P`.  This agrees with the flow
proof and shows that the theorem is a concrete sufficient certificate for
full residual port rank, not a weakening of the exact Rado condition.

## 4. Scope exclusions

The proof does not derive:

* a physical port injection from an abstract Middle Levels factor;
* survival after an unspecified or adaptive compensation linkage;
* private literal incidence bundles from Boolean values alone;
* compatibility of two separately constructed factors;
* the protected pivot, all-width upper bank, or background compiler.

Within the fixed-state private-lift hypotheses, the theorem and load
calculation are valid.
