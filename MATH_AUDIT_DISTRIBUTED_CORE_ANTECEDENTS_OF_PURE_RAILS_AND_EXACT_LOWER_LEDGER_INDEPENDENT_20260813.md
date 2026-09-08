# Independent audit: distributed-core antecedents of pure rails

**Date:** 2026-08-13  
**Verdict:** **PASS**, with one harmless notation typo.  
**Frozen source:** `MATH_THEOREM_DISTRIBUTED_CORE_ANTECEDENTS_OF_PURE_RAILS_AND_EXACT_LOWER_LEDGER_20260813.md`  
**Source SHA-256:** `eac1ca770e464600427cd3b922851e9ff41c784be41730807d80ea47cffefce4`

This was a proof-level audit.  No search, solver, or substantive local computation was used.

## 1. Cyclic-period issue

The current source handles the possible period error correctly.  For a general period
`N`, each core coordinate is assigned an arbitrary cyclic hitting set `E_f` meeting
every `q`-arc.  The residue-class specialization

\[
E_f=\{i:i\equiv s\pmod q\},\qquad G_i=F_{i\bmod q},
\]

is invoked only under the explicit assumption `q|N`.  That restriction is necessary:
a cyclic colouring in which every `q`-arc contains every colour forces the colour word
to have period `q`, hence forces `q|N` if every colour occurs in the intended phase
pattern.

The minimum cyclic hitting-set size is indeed `ceil(N/q)`.  If the selected positions
are read cyclically, every gap between consecutive selected positions is at most `q`;
conversely that gap condition meets every `q`-arc.  Composing `N` into the requisite
number of positive parts at most `q` gives equality.

## 2. Exact ledger and ranks

The interval identity

\[
A[i,\ell]=\Bigl(\bigcup_{t=0}^{\ell-1}G_{i+t}\Bigr)
\cup\{x_i,\ldots,x_{i+\ell-1}\}
\]

is literal because the toggle labels are distinct and disjoint from the core.  Every
interval of length at least `q` contains a `q`-arc and hence emits every core coordinate,
so the owner and all longer-row transport claims follow exactly.  For `ell<q`, the rank
formula is also exact.

Under `q|N`, the phase blocks encountered by a strict-lower interval are distinct.  A
cyclically balanced placement of the `b` large blocks gives either
`floor(b ell/q)` or `ceil(b ell/q)` large phases in every `ell`-arc, so (4.6) is valid.
With `|F|=R-q`, the displayed typical rank simplifies exactly to

\[
\ell+\frac{R-q}{q}\ell=\frac Rq\ell,
\]

up to the stated unit rounding error.

The private-toggle theorem is correct: `x_i` occurs at source address `i` only, making
adjacent letters incomparable and furnishing both private endpoints of every owner-row
transition.

## 3. Period `2q+1` single-cell programmer

For

\[
E_a=\{a-1,a,a+q\}\subseteq\mathbb Z_{2q+1},
\]

the cyclic gaps are `1,q,q`, hence `E_a` is a minimum `q`-arc hitting set.  For the
marked interval `J=[i,i+ell-1]`, `1<=ell<q`,

\[
E_{i-1}=\{i-2,i-1,i+q-1\}
\]

misses `J`, whereas `E_i` contains `i`.  Assigning `E_i` to the desired core mask and
`E_(i-1)` to its complement therefore emits exactly that mask in `J`.  Formula (2.1)
then proves (5.5).

The rank-span statement is exact: as `ell` ranges from `1` to `q-1` and
`|H|` ranges from `0` to `R-q`, the intervals

\[
[\ell,R-q+\ell]
\]

cover every integer rank from `1` through `R-1` (under the stated eventual parameter
regime).

## 4. Scope

The source correctly limits Theorem 5.1 to programming **one designated cell**.
Several cells impose simultaneous hit/avoid constraints on the same schedules `E_f` and
need not be compatible.  The theorem also does not construct a global pure-rail factor,
cover every lower target simultaneously, join closed rails into a linear chronology, or
control exterior seam intervals.  Those are accurately retained as separate gates.

The only defect found is the typographical expression
`\mathcal H_{N,q}^{,F}` in (4.9); it should denote the Cartesian power
`\mathcal H_{N,q}^{F}` (or, more explicitly, `\mathcal H_{N,q}^{|F|}`).
It does not affect any statement or proof.
