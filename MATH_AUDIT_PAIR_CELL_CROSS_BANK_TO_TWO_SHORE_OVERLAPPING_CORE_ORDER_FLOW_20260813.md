# Audit: pair-cell cross bank inside the two-shore overlapping-core order flow

**Date:** 2026-08-13  
**Verdict:** **PASS.**  The cross-edge incidence formulas, simultaneous
owner/lower role ledger, cyclic-orbit construction, two-shore fractional
concentration, protected-lift residual equations, and joint codegree
obstruction all replay exactly.  The result is a fractional/order-system
bridge, not an integral factor theorem.

**Frozen theorem:**
`MATH_THEOREM_PAIR_CELL_CROSS_BANK_EMBEDS_IN_TWO_SHORE_OVERLAPPING_CORE_ORDER_FLOW_20260813.md`  
**Theorem SHA-256:**
`b280d1a8844d62d21e2cc8ff6c2d9aa6373022f58ded50f99d81df64380056be`

**Verifier:** `verify_pair_cell_cross_bank_two_shore_role_flow.py`  
**Verifier SHA-256:**
`b2b3c6ac2a69a69e0fe817b25bfc0bca19d10298144ee52d8ad8bb64a5d0e7e9`

## 1. Pure-rail cross incidence

For the pure rail

\[
 A_i=C\cup\{x_i,\ldots,x_{i+q-1}\},
\]

the transition `A_iA_(i+1)` exchanges exactly `x_i,x_(i+q)`.  It is
internal to the fixed pair structure exactly when those two coordinates
are a matched pair.  Because the period satisfies `N>2q`, one matched pair
cannot occur at both cyclic orientations of the distance-`q` chord.  Thus
the number of internal transitions is at most `floor(N/2)`, and every rail
has at least `ceil(N/2)` cross transitions.

Every toggle coordinate occurs in two transition supports.  The full
`F_2^p` signature therefore vanishes on a closed rail, while its scalar
charge is its period modulo two.  A shell collection of total period `W`
accordingly supplies at least `W/2` cross edges and total charge `W mod 2`.
This is independent of the named-order choice and is substantially larger
than the low-cell lower bound from the preceding theorem.

## 2. Exact two-shore point ledger

A core point of a period-`N` shell occurs in all `N` owner windows and all
`N` lower windows.  A toggle point occurs respectively in `q` and `q-1`
windows.  If `K_x` is weighted core load and `U_x` is toggle-support degree,
exactness on both equal shores gives

\[
 K_x+qU_x={R\over k}W,
 \qquad
 K_x+(q-1)U_x={R-1\over k}W.
\]

Their difference forces

\[
 U_x=W/k,\qquad K_x=(R-q)W/k.
\]

Here `W/k=Cat_p`, so there is no divisibility defect.  This derivation is
both necessary and exactly the simultaneous ground-point role condition.

For periods `n=2q+2,n+1`, write

\[
 W/k=nA+(n+1)B.
\]

A full orbit of one disjoint base pair `(C,T)` under a regular `k`-cycle
contains each point in `c` cores and in `N` supports.  Hence an orbit block
of period `N` contributes `Nc` weighted core load and `N` support load at
every point.  Taking `A,B` blocks proves the exact role vector.  The coin
representation used in the theorem is nonnegative under its stated
`W/k>=n^2-1` hypothesis.

## 3. Simultaneous named fractional checkpoint

For one uniformly random base shell, followed by a uniform cyclic order,
a fixed named owner and a fixed named lower colour each receive expected
load `N/W`.  Taking all `k` cyclic translates preserves that marginal and
makes the block mean `kN/W`, while its contribution is bounded by `kb`.
Orbit blocks are independent, their total mean is one, and the exact point
roles hold for every outcome.  The variance bound

\[
                         \sum\operatorname {Var}X\le kb
\]

and Bernstein's inequality give the stated simultaneous
\(1\pm4\sqrt{kb\log(8W)}\) bounds after a union over both `W`-vertex
shores.  For the two short periods, \(b=O(q^2 4^{-q})\), so the error is
\(e^{-\Omega(q)}\) centrally.

Thus the construction genuinely combines two properties previously proved
separately: exact ground-point roles and named fractional uniformity.  It
does not make the named loads exactly one or select integral orders.

## 4. Integral system and protected lift

One order variable per shell/order, one token equation, one equation for
every named owner `q`-window, and one equation for every named lower
`(q-1)`-window are necessary and sufficient for a pure-rail exact coloured
factor.  The lower equations are not a proxy: they are literally the edge
intersection colours of the selected owner cycles.

After protecting the transversal lift with point loads `y_x,z_x`,
subtraction of its two shores gives the exact residual targets

\[
 U_x=W/k-y_x+z_x,
 \qquad
 K_x=cW/k+(q-1)y_x-qz_x.
\]

Their total degrees and both residual point equations check.  They are
positive asymptotically because the lift has size `2^p` whereas `W/k` is
of order `4^p/poly(p)`.  No allocation achieving these nonuniform targets
while avoiding every protected owner and colour is claimed.

## 5. Forced joint codegree

In the complete two-shore orbit hypergraph, a rail occurrence of owner
`A` contains exactly two rail lower colours which are facets of `A`: its
two incident edge colours.  No other cyclic `(q-1)`-window lies inside its
cyclic `q`-window.  Summing codegrees over the `R` facets of `A` gives twice
the degree of `A`; stabilizer symmetry makes the summands equal.  Hence

\[
                         \deg(A,L)/D=2/R
                         \qquad(L\subset A).
\]

The joint edge size is `2N`, so the squared-rank collision expression is at
least `8N^2/R`, which is `Theta(1)` when `N=2q+O(1)` and
`q=Theta(sqrt R)`.  This does not disprove an integral matching.  It does
show that the favorable owner-only vanishing-collision calculation cannot
be copied after adding literal lower vertices.

## 6. Verifier replay

The verifier returned `PASS` for `(p,q)=(5,2)` and `(7,3)`.  It checked:

* every displayed rail's owner and lower decks, transition exchanges,
  cross count, signature, and two incident facets per owner;
* exact cyclic-orbit weighted core and support degrees;
* both owner and lower point degrees;
* total period and charge;
* exact named-load expectation one on both shores; and
* the protected reflected-Gray-lift residual role formulas.

At `(p,q)=(7,3)` it produced `795` genuine shell tokens of total period
`6435`, weighted core degree `2145`, support degree `429`, odd total charge,
and positive protected residual role ranges.  The displayed arbitrary orbit
bases happened to make all `6435` transitions cross; the theorem uses only
the universal lower bound `ceil(W/2)`.

The verifier is a finite identity checker.  It does not solve the integral
two-shore ordering equations, upper support, transition collars, source
flags, or component fusion.

## 7. Frozen prerequisite ledger

| Role | File | SHA-256 |
|---|---|---|
| positive overlapping-core role flow and owner order gate | `MATH_THEOREM_OVERLAPPING_CORE_POSITIVE_ROLE_FLOW_AND_ORDERING_GATE_20260813.md` | `67a90e9c9be887533ce9659cfca9d8e1e68c9b43a4894ef985cae1e329106eef` |
| named-owner random-shell fractional checkpoint | `MATH_THEOREM_RANDOM_SHELL_NAMED_ORDER_FRACTIONAL_CHECKPOINT_20260813.md` | `af5307f0010a0eb5a370a775157f82839edbec2ce91ffda3954e3d6c79ca5be8` |
| exact coloured owner/lower factor gate | `MATH_REDUCTION_PAIR_CELL_CYCLES_VERSUS_PROTECTED_MSW_ROWS_EXACT_COLORED_F_FACTOR_GATE_20260813.md` | `742b63d17c0c092557483066c81ee4aecfff95cfe4d7e5beab18a204bebcfdcb` |
| pair-cell parity and low-cell cross lower bound | `MATH_THEOREM_PAIR_CELL_PARITY_CHARGE_TRIANGLE_AND_EXPONENTIAL_CROSS_EDGE_LOWER_BOUND_20260813.md` | `f89034566a28883910566016cff373166ef80131cba894c44b4e269b6f241f78` |
