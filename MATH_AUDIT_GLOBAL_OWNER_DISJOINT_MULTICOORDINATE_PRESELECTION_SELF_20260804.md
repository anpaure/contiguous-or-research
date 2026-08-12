# Self-audit: global-owner-disjoint multicoordinate preselection

**Date:** 2026-08-04  
**Verdict:** **GO**, subject to independent audit.  This checks only the
abstract Middle Levels preselection and the resulting protected-factor
collision ledger.  It does not certify common-cap activation or routing.

## 1. Hall union bound

For distinct injected lower sets `L_i,L_j`, a common rank-`m` upper
neighbour is forced to equal `L_i union L_j`; hence

\[
                         |A_i^q\cap A_j^q|\le1.
\]

Bonferroni's first lower bound is therefore

\[
 \left|\bigcup_{i\in X}A_i^q\right|
 \ge xL_q-{x\choose2}.
\]

At coordinate `q`, the earlier selected bank has exactly `qp` values and
is disjoint from the fixed forbidden bank.  Deleting both banks loses at
most `f+qp` from the **union**, not from every menu.  Thus the Hall surplus
is exactly bounded below by

\[
 Q_q(x)=x(L_q-1)-{x\choose2}-f-qp.
\]

This quadratic is concave, so its minimum on the integer interval
`1<=x<=p` lies at `1` or `p`.  The displayed conditions `(H_q)` are exactly
those two endpoint inequalities.  The induction consequently makes all
selected upper values distinct across every previous coordinate.

## 2. Simple sufficient row

Put `F_q=f+qp`.  If `p<=L_q` and `F_q<=L_q-1`, then

\[
 Q_q(1)=L_q-1-F_q\ge0.
\]

For `p>=2`,

\[
\begin{aligned}
 Q_q(p)
 &\ge p(L_q-1)-{p\choose2}-(L_q-1)\\
 &=(p-1)(L_q-1-p/2)\ge0,
\end{aligned}
\]

because `L_q>=p` implies `L_q-1-p/2>=p/2-1>=0`.  The case `p=1` is the
first endpoint.  Hence `(H'_q)` really implies `(H_q)`.

## 3. Two-coordinate collision ledger

The same injected lower vertex is used once in each coordinate, so its
selected degree is exactly two.  Global upper disjointness makes every
selected upper degree at most one.  Every selected edge is distinct, and
there are exactly `2p` of them.  Thus the selected bank is 2-bounded and
the small protected-factor theorem applies precisely under the separately
stated compatibility row with `P_*`.

The occurrence-lift theorem then gives loads

\[
                         d_M(L)=2,qquad d_M(U)\le1,
 \qquad d_M(\text{halfport})=1.
\]

Only the upper-owner alias has been removed.  The theorem correctly leaves
the shared lower source, common-cap activation, suffix linkage, typing,
product closure, opening and global decoration outside its conclusion.

## 4. Artifact

The audited theorem is
`MATH_THEOREM_GLOBAL_OWNER_DISJOINT_MULTICOORDINATE_PRESELECTION_20260804.md`
at pre-independent-audit SHA
`fab1d624778ddf687867fad2969d5821a3383dd38f8e6da7e5e26d571f4a69f9`.

