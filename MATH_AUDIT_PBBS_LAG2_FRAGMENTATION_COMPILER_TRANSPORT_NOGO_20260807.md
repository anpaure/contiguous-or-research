# Audit of the lag-two fragmentation compiler-transport no-go

**Date:** 2026-08-07  
**Audited theorem:**
`MATH_THEOREM_PBBS_LAG2_FRAGMENTATION_COMPILER_TRANSPORT_NOGO_20260807.md`  
**Method:** exact symbolic interval audit; no computation or search  
**Verdict:** PASS.  The theorem proves a local loss of \(d-1\) named
strict-lower values in the natural ordinary fixed-core off-state.  Its
global scope exclusions are necessary and correctly stated.

## 1. Ordinary uniqueness

Every ordinary source letter is \(G+\tau_t\), with distinct
\(\tau_t\notin G\).  Hence an ordinary interval is \(G\) plus exactly the
toggles at its positions.  The value \(G+a_i\) can occur only at the
one-letter \(a_i\)-position.  Its rank is \(|G|+1=m-d-1<m\), so it is in
the strict-lower compiler domain.

## 2. Fragmented absence

After fragmentation, there is no ordinary \(a_i\)-letter.  Any interval
meeting another ordinary letter gains that letter's noncore toggle.

Inside the exceptional block, \(Q+a_0\) and \(C_0\) occur in disjoint
letter types.  Every exceptional letter carrying \(C_0\) also carries
either \(b^-\) or \(z\), neither of which belongs to \(G+a_i\).  Thus no
exceptional interval has value \(G+a_i\).  The optional \(d=2\) final
enrichment supplies only \(Q+a_0\) and does not change this conclusion.

The interval cases are exhaustive, and the \(d-1\) values are distinct.
Therefore no exact-value occurrence injection exists on the complete old
strict-lower deck.

## 3. Scope

The result rules out only the ordinary-fixed-core-to-fragmented rewrite as
a compiler-functorial step.  It does not rule out a remote duplicate of a
lost value, a parent state in which the collar is already fragmented, or a
different packet.  The conditional \(h(d-1)\) bank count explicitly
requires cross-collar target distinctness.  No statement about deep-upper
coverage, Hamiltonicity, or the existence of the alternative backup bank
is made.
