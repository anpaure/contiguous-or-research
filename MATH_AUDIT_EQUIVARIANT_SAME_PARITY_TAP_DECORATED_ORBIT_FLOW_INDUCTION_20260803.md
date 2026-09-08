# Audit: fresh-pair stabilizer growth and same-parity orbit-flow induction

**Date:** 2026-08-03  
**Scope:** pure mathematics only; no finite-dimensional computation or
solver evidence.

## 0. Frozen objects and verdict

The audited source note is
`MATH_THEOREM_FRESH_PAIR_COMMON_STABILIZER_GROWTH_20260803.md` at SHA-256

```text
1930b17ca91dd0f6a9ff089d9bc7818794ebe8204b0376484ac3bf997ad72b98
```

Its orbit arithmetic, residual-subgroup Corollaries 2.4 and 5.2, one-arrow
`C_k` action, persistent-sidecar capacity separation/replacement,
post-deletion defect/router face, terminal-only charge rule, and item 8's
one-materialized-child coinstantiation and certified `C_(k+2)` reframing
are **GO**.  Same-period coupling is now restricted to a covered invariant
capacity-faithful matching/flow gate or a separately proved exact
`q`-divisibility theorem.  The conclusion remains correctly conditional on
a closed recurrent outer core and the other tap/repair hypotheses.

The exact source SHA is therefore **GO as a conditional pure-mathematics
theorem**.  Three independent proof reads of this exact digest found no
remaining correction.

The corrected fold is
`MATH_THEOREM_EQUIVARIANT_SAME_PARITY_TAP_DECORATED_ORBIT_FLOW_INDUCTION_20260803.md`
at SHA-256

```text
a07ac985c4d2c28918efe09db311f463bcf461f0d5999edb85536bc3d9a875c6
```

That theorem is **GO as a conditional same-parity induction theorem**.
Three independent proof reads of this exact digest found no remaining
mathematical overclaim.

## 1. Stabilizer arithmetic

For `k=2r-1` and an old subset of rank `s=r+a`,

\[
 \gcd(k,s)=\gcd(k,2a+1),
 \qquad
 |C_kS|\ge {k\over\gcd(k,s)}\ge {k\over|2a+1|}.
\]

The denominator is a nonzero odd integer.  Consequently the parent middle
ranks `r-1,r` are free.  In the child's two middle ranks `r,r+1`, the old
rank offsets are respectively

\[
                 \{0,-1,-2\},\qquad\{1,0,-1\},
\]

so every fresh-occupancy sector has period at least `k/3`.  More generally,
an old-rank band `|s-r|<=D(k)` has minimum period at least
`k/(2D(k)+1)`, which is `Omega(sqrt(k))` when
`D(k)=O(sqrt(k))`.

## 2. Addresses and the actual residual group

The inheritance statement is valid only for a literal equivariant
projection

\[
                    S(g\omega)=gS(\omega).
\]

It gives

\[
 \operatorname{Stab}(\omega)
 \subseteq\operatorname{Stab}(S(\omega)),
 \qquad |C_kS(\omega)|\mid |C_k\omega|.
\]

If `H_k<=C_k` is the subgroup stabilizing all fully pinned pre-gate arrow
data and `h_k=|H_k|`, the proof-safe bound is

\[
 |H_k\omega|
 \ge {h_k\over\gcd(k,r+a)}
 \ge {h_k\over|2a+1|}.
\]

Thus the full `k/|2a+1|` estimate requires `H_k=C_k`; the general growth
hypothesis is `h_k/(2D(k)+1) -> infinity`.  Forgetting the old-subset label,
coalescing physical addresses, or choosing a nonequivariant representative
is a quotient operation and receives no inheritance bound.

## 3. Exact-period divisibility

Common period is not sufficient for an arbitrary integer program.  The
folded Lemma 6.5 therefore assumes that the complete matching incidence
graph or directed node-split flow network is `H_k`-invariant, including all
arcs, capacities, balances, bounds, and quotas, and that every finite
physical capacity in the stratum has exact period `q`.  The unique cyclic
kernel of order `h_k/q` then fixes every displayed object; the quotient
`C_q` acts freely, and the matching deficiency or flow corank is a
nonnegative multiple of `q`.

Different periods share no finite physical capacity.  Same-period gates may
be coupled only if the compound is still a capacity-faithful invariant
bipartite-matching or node-split-flow gate covered by that lemma, or if a
separate exact `q`-divisibility theorem is supplied.  This excludes an
unsupported promotion for general hypergraph or joint integer programs.

It follows that a uniform per-stratum defect bound `C` vanishes whenever

\[
                 {h_k\over2D(k)+1}>C.
\]

This is simultaneous over all exact-period strata; it does not require the
number of literal orbits to be bounded.

## 4. Correct regenerative interface

The folded Corollary 6.7 makes four distinctions that are necessary for
iteration.

1. The residual action stabilizes the fully pinned **pre-gate** instance.
   A later integral lift may break symmetry, but its literal output is
   authenticated.
2. Every persistent exception outside the period-pure bulk is saturated or
   exported as a bounded typed sidecar and replaced, rather than
   accumulated, in the successor.  After its capacities are fixed and
   deleted, the residual strata remain invariant and capacity-disjoint.
3. Only terminal-only exceptions may be discharged by literal repair or
   target-bypass charge.
4. The selected output must be reframed into a fully pinned,
   next-action-admissible `C_(k+2)` state.

The last condition is independent.  On the child, the one-arrow `C_k`
action fixes the fresh pair; it is not the full old-coordinate rotation
needed for the next `(k+2)->(k+4)` arrow.  Period growth therefore does not
prove successive-arrow compatibility.  An authenticated change-of-group,
groupoid, or equivalent re-gauging theorem is still required.

## 5. Scope

The result promotes only invariant, capacity-faithful, period-pure inner
matching/flow gates.  It does not promote bounded aggregate deficiency of
the outer state graph without that graph's own same-period decomposition
and per-period bound.  Nor does it construct a finite quotient: even one
free middle-rank period contains exponentially many literal subset orbits.
A fixed symbolic generator, complete-state congruence, authenticated
literal output, recurrent two-tap core, and rolling change-of-group
interface remain hypotheses.

Accordingly the fold proves a proof-safe conditional implication, not an
unconditional `B(k)+O(1)` bound.
