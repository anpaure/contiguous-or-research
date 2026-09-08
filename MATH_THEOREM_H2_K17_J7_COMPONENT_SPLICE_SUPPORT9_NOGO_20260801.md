# The protected J7 path has no support-nine splice in the frozen MMM cycle

Date: 2026-08-01  
Lane: H2 / bounded J7 component splice  
Status: **exact finite no-go at changed-tail support nine; no statement for
support at least ten, another quotient factor, or global K17.**

## 1. Exact scope

The host remains the fixed 1430-orbit cycle
`scratch/k17_mmm_quotient_cycle.tsv`, SHA-256
`4439b89f56b513416a418cbe0f7e8d9fa9e1bff9538ff432c497aa8cb473145f`.
Its owner-orbit and lower-q1-orbit rows are both bijective and its voltage is
one modulo 17.

The two protected J7 orientations are

\[
 7711\to8077\to13623,
 \qquad13623\to8077\to7711.                           \tag{1.1}
\]

Both have nonempty six-cell literal sources realizing the certified type
IDs `(3,7,0)`.  The catalogue includes every same-successor rephasing: a
tail may retain the old successor orbit while changing its voltage and
lower/upper labels.

The corrected support-at-most-seven census and the exact support-eight
census are frozen separately.  Both are empty.

## 2. Closure enumeration

For a selected new labelled arc `u -> v` with lower label `l`, exact reuse
of the old head and lower palettes forces

\[
                  \sigma^{-1}(v),\ \lambda^{-1}(l)\in S,            \tag{2.1}
\]

where `S` is the changed-tail support, `sigma` is the old successor, and
`lambda` is the old tail-to-lower-colour bijection.  At a completed leaf,
owner and lower exactness is

\[
 \{v_u:u\in S\}=\sigma(S),\qquad
 \{l_u:u\in S\}=\lambda(S).                            \tag{2.2}
\]

Starting from each forced J7 orientation, the audit enumerates all 72
voltage-labelled quotient Johnson moves at every live tail, applies (2.1),
and rejects only when the closure exceeds nine.

### Theorem 2.1

No labelled successor exchange with exactly nine changed tails contains
either J7 orientation while preserving both the frozen owner and lower-q1
orbit bijections.

#### Proof

The exhaustive search visits

```text
forward:   29,569 closure states
reverse:  516,549 closure states
```

and finds zero leaves satisfying (2.2).

Every alleged support-nine solution traces an unpruned branch: choosing its
arc at each processed tail adds through (2.1) only tails in its final
support.  If the forced closure were a proper subset of the nine-tail
solution, it would itself be a balanced smaller J7 exchange; the already
verified support-at-most-eight no-go excludes that possibility.  Hence the
enumeration is complete. \(\square\)

## 3. Downstream interpretation

The census contains exact post-owner/lower filters for:

1. one-cycle quotient topology;
2. nonzero total voltage;
3. literal positive-run residence at both J7 boundaries in the 24,310-owner
   lift; and
4. pairwise-distinct new upper-q1 orbits with no newly lost old upper orbit.

All receive an empty input family.  Their zero survivor counts are therefore
vacuous; this theorem identifies owner/lower closure as the failing row and
does not claim a separate voltage, residence, or upper-q1 obstruction.

The original upper-q1 ledger is independently replayed as `996/1144`
covered orbits, `148` holes and `434` repeat units.

The survivor TSV contains only its header.  The smallest untested bounded
class on this fixed cycle is now support ten.  No support-ten search is
included here because the requested continuation was one bounded step.

## 4. Artifacts

```text
scratch/audit_h2_k17_j7_component_splice_support9_20260801.py
scratch/h2_k17_j7_component_splice_support9_20260801.audit.json
scratch/h2_k17_j7_component_splice_support9_20260801.survivors.tsv
```

The deterministic run remains lightweight and launches no SAT solver.  It
does not edit the project handoff/index and makes no claim for a different
owner cycle, a reselected lower matching, a forest embedding, ranks at least
eleven, or common-cap compilation.
