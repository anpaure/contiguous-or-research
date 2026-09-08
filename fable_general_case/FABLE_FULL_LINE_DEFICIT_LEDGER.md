# Ledger for the full-line deficit resolution

All rows at bottom threshold `c -> 1+`, full-line branch, `D_word = o(a^2)`.
`eps_d = sqrt(6 gamma_des)`, `eps = sqrt(6 delta)`. Status column:
PROVED (here or cited), UNPROVED (explicitly missing), CONVENTION
(program-wide standing assumption).

## Constraint rows

| Row | Statement | Source | Status | X(delta) |
|-----|-----------|--------|--------|----------|
| L1 | `ell = 3 - delta`; marginals mass `f`, moment `3 - delta` | hypothesis + seam algebra | PROVED | tight |
| L2 | `delta = gamma_int + gamma_term`; `int z drho = gamma_int` | Lemma 3.1 (dep. A1) | PROVED | tight, `gamma_term = 0` |
| L3 | `D_a/a^2 = gamma_des <= delta` | Lemma 4.1 (dep. A2) | PROVED | tight, `gamma_des = delta` |
| L4 | `P + 2N >= 3 - eps_d`; `A <= P <= 2f - 3 + eps_d` | Thm 5.1 step (5.2) | PROVED | equality |
| L5 | `C <= min{4f - 6 + 2 eps_d, 3 - 2delta + eps_d}` | Thm 5.1 step (5.3) | PROVED | equality at `f_0` |
| L6 | gap charge `<= 3 gamma_int`; coefficient 3 pointwise sharp | SMALL_DEFICIT seal Lem 4.1 | PROVED (cited) | tight at `(2,2,1)` direction |
| L7 | `U(1+) <= 3 - f + C + 3 gamma_int` | seam identity + L6 | PROVED | equality |
| L8 | `A_d <= 1`; `tau_A >= sum A_d^2/2`; `iota_A >= sum_{d<e}((A_d+A_e-1)_+)^2/2`; `tau_A + iota_A <= 2f - 3 + delta` | Lemma 6.1 + ABSORBED_FLOW (4.5) | PROVED | slack |
| L9 | coarea (5.1) of ABSORBED_FLOW for all weights `w` | cited | PROVED (cited) | slack (wedge-triangle count) |

## Value rows

| Row | Statement | Status |
|-----|-----------|--------|
| V1 | `U(1+) <= 15/4 + (5/4) eps_d + 3 gamma_int - (3/2) delta` | PROVED (Thm 5.1) |
| V2 | `U(1+) <= 15/4 + (5/4) eps_d + (3/2) delta` | PROVED (V1 + L2) |
| V3 | Exclusion iff `gamma_des < (1 - 6delta)^2/150`, `delta < 1/6` | PROVED (Cor 5.2) |
| V4 | Diagonal `gamma_des = delta` recovers `delta_0 = (81 - sqrt(6525))/36 = (sqrt29 - 5)^2/24` | PROVED (audit check) |
| V5 | `gamma_des = 0` closes all `delta < 1/6` | PROVED (V3) |
| V6 | Bottom-threshold optimality of this charge (no sweep helps) | PROVED (Thm 7.1) |
| V7 | `U_X(1+) = 15/4 + (5/4) eps + (3/2) delta > 4` on `delta >= delta_0` | PROVED (scalar evaluation) |

## Open rows

| Row | Statement | Status |
|-----|-----------|--------|
| O1 | **Lemma M**: `U(1+) <= V2-bound - mu * gamma_des` for some `mu > 0` (desert-occupancy discount) | **UNPROVED — the one missing lemma** |
| O2 | Reduction: Lemma M with `mu >= 75/(8(1 - 6 delta_1))` closes all `delta < delta_1` | PROVED (Thm 9.1) |
| O3 | Target constants: `mu >= 9.375` (any `delta_1 -> 0+` gain), `mu >= 12.5` (`delta_1 = 1/24`), `mu -> infinity` as `delta_1 -> 1/6` | PROVED arithmetic; erratum in resolution S9 item 4 ("12" -> "12.5") |
| O4 | Regime `delta >= 1/6` | OPEN — outside every row above |
| O5 | Outcome A (universal sub-four threshold) | NOT REACHED |
| O6 | Outcome B (genuine process, `U >= 4` everywhere) | NOT REACHED — X is dual ledger only, not a word/process |

## Dependency flags

| Flag | Content | Risk |
|------|---------|------|
| A1 | bottom-threshold gap partition (MULTISCALE Thm 2.1, vertex convention) | LOW (audited there) |
| A2 | middle word is a Hamilton path of `H_a` (program encoding) | LOW (standing convention) |
| M | Lemma M | OPEN — sole mathematical gap |

## Surviving region after this note

```text
S = { (delta, gamma_des) : (1-6delta)^2/150 <= gamma_des <= delta < 1/6 }
    union { delta >= 1/6 }.
```

Every full-line process outside `S` is excluded (V3). Every process inside
`S` is excluded conditionally on Lemma M with the O3 constants. The dual
ledger X(delta) sits on the boundary component `gamma_des = delta` of `S`
and certifies that rows L1-L9 alone cannot exclude `S` (V7): any future
proof must add information beyond the six audited families, and Lemma M is
the narrowest such addition — single-threshold, no lifetimes, no coupling.
