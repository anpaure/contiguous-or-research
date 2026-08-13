# Whole good pair cells cannot partition the odd middle layer

**Date:** 2026-08-13  
**Status:** unconditional arithmetic obstruction.  It applies to any number of
sentinel-plus-pair structures and is independent of how strongly their good cells
cover the owner layer.

## 1. Setup

Put

\[
 k=2R-1,qquad p=R-1,qquad
 W=\binom{2p+1}{p+1},
\]

and let

\[
                         M=q+\lceil3\log_2p\rceil.
\]

For any sentinel-plus-perfect-matching pair structure, a dimension-\(m\) pair cell
is a Boolean cube \(Q_m\), hence has exactly \(2^m\) owners.  A cell is good for the
long-run construction only when \(m\ge M\).

## 2. Divisibility obstruction

### Theorem 2.1

No pairwise disjoint family of whole good pair cells, chosen from any number of pair
structures, partitions the rank-\(R\) owner layer.

#### Proof

Every good cell has cardinality \(2^m\) with \(m\ge M\).  Therefore the cardinality
of every disjoint union of whole good cells is divisible by \(2^M\).  An exact
partition would imply

\[
                         2^M\mid W.                       \tag{2.1}
\]

For a positive integer \(n\), write \(s_2(n)\) for its binary digit sum.  Legendre's
formula gives

\[
\begin{aligned}
 v_2(W)
 &=s_2(p+1)+s_2(p)-s_2(2p+1)\\
 &=s_2(p+1)-1.                                           \tag{2.2}
\end{aligned}
\]

Indeed, \(2p+1\) is the binary word for \(p\) shifted left once and followed by a
one, so \(s_2(2p+1)=s_2(p)+1\).  Consequently

\[
 v_2(W)=s_2(p+1)-1\le \lfloor\log_2(p+1)\rfloor.         \tag{2.3}
\]

For \(q\ge2\) and \(p\ge2\),

\[
 M=q+\lceil3\log_2p\rceil
   >\lfloor\log_2(p+1)\rfloor
   \ge v_2(W).                                           \tag{2.4}
\]

Thus (2.1) is false.  \(\square\)

### Corollary 2.2 (exact residue gate)

If a disjoint union of whole good cells leaves \(D\) owners uncovered, then

\[
                         D\equiv W\pmod {2^M}.             \tag{2.5}
\]

In particular it cannot have \(D=0\).  Its least arithmetically possible leave is
the nonzero residue \(W\bmod 2^M\); realizing that residue is a separate geometric
problem and is not asserted here.

## 3. Consequence for the three-structure cover

`MATH_THEOREM_THREE_PAIR_STRUCTURES_COVER_EVERY_OWNER_BY_A_GOOD_CELL_20260813.md`
proves that three pair structures eventually cover every owner set-theoretically.
Theorem 2.1 shows that no selection of their intact good cubes can turn that cover
into an exact owner factor.  The obstruction persists even if arbitrarily many pair
structures are supplied.

Therefore every successful factor construction must use at least one genuinely
cross-cell operation: cut good cubes and rethread the fragments, introduce smaller
non-cube resident components, or absorb the residue through a relative trade.  Better
set-cover estimates alone cannot close the factor gate.
