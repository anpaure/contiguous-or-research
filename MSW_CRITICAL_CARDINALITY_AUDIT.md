# The canonical MSW defect fails the critical Catalan recurrence numerically

## 1. Purpose

The targetwise ECO programme asks whether the missing shadows of the
unchanged MSW wreath factor satisfy a recurrence with the critical Catalan
coefficient

\[
 E_{m+1,H}\leq {C_{m+1}\over C_m}E_{m,H}+B_{m,H},
 \qquad {1\over M}\sum_{m<M}{B_{m,H}\over C_m}\longrightarrow0.       \tag{1.1}
\]

Here `C_m` is the `m`-th Catalan number.  The occurrence-projection theorem
in `MSW_ECO_TARGET_PROJECTION.md` gives the correct local deletion graph,
but a capacitated Hall theorem can only prove (1.1) if the cardinalities on
the two sides permit it.  This note audits that necessary condition at the
first shadow depth.

The conclusion is negative for all presently computed dimensions and is
structurally unfavorable asymptotically: a critical recurrence with a
Cesaro-sub-Catalan error would force the canonical MSW missing fraction to
tend to zero.  The exact data instead increase from `0.0476` at `m=4` to
`0.2465` at `m=12`.

This is not an all-dimensional disproof, because no positive limiting
missing fraction has yet been proved.  It is, however, a necessary
cardinality gate that should precede any further Hall analysis.

## 2. Exact first-shadow ledger

Let

\[
 N_m={2m+1\choose m-1},\qquad
 L_m=\#\{\hbox{missing rank-}(m-1)\hbox{ targets}\}.                 \tag{2.1}
\]

Complementation gives the same number of missing rank-`m+2` targets, so the
two-sided depth-one defect is

\[
                         E_m=2L_m.                                  \tag{2.2}
\]

Put

\[
 A_m={C_{m+1}\over C_m}={2(2m+1)\over m+2}.                         \tag{2.3}
\]

For any inequality

\[
                         E_{m+1}\le A_mE_m+B_m                       \tag{2.4}
\]

one necessarily has

\[
 B_m\ge 2\max\{0,L_{m+1}-A_mL_m\}.                                 \tag{2.5}
\]

The exact enumerations in `ODD_GRAPH_EXACT_WREATH_FACTOR.md` give:

\[
\begin{array}{c|r|r|c|c|c}
m&N_m&L_m&L_m/N_m&
(L_{m+1}-A_mL_m)/C_m&
2(L_{m+1}-A_mL_m)/C_m\\ \hline
4&84&4&0.047619&1.428571&2.857143\\
5&330&32&0.096970&1.795918&3.591837\\
6&1287&176&0.136752&2.007576&4.015152\\
7&5005&837&0.167233&2.142191&4.284382\\
8&19448&3709&0.190714&2.238042&4.476084\\
9&75582&15811&0.209190&2.311843&4.623686\\
10&293930&65860&0.224067&2.371219&4.742439\\
11&1144066&270337&0.236295&2.420184&4.840368\\
12&4457400&1098850&0.246523&-&-
\end{array}                                                         \tag{2.6}
\]

Thus in every available transition the *minimum possible* exceptional term
is already a positive Catalan multiple, and the normalized residual is
increasing.  No choice of edges in the deletion graph can change (2.5).

The `m=8` missing fraction printed as `0.190765` in
`MSW_SHALLOW_DEFECT_AUDIT.md` is a harmless decimal typo; the exact ratio is
`3709/19448=0.1907137...`.

## 3. Normalized telescoping theorem

The cardinality obstruction has a particularly transparent form after
Catalan normalization.  Define

\[
 e_m={E_m\over C_m},\qquad p_m={L_m\over N_m}.                       \tag{3.1}
\]

Since the coefficient in (2.4) is exactly `C_(m+1)/C_m`, division by
`C_(m+1)` gives

\[
 e_{m+1}\le e_m+{B_m\over C_{m+1}}.                                \tag{3.2}
\]

Also

\[
 {N_m\over C_m}={m(2m+1)\over m+2},
 \qquad
 e_m=2p_m{m(2m+1)\over m+2}=(4+o(1))m p_m.                         \tag{3.3}
\]

### Theorem 1 (critical recurrence forces vanishing miss density)

If nonnegative `B_m` satisfy (2.4) and

\[
 {1\over M}\sum_{m<M}{B_m\over C_m}\longrightarrow0,              \tag{3.4}
\]

then

\[
                              p_m\longrightarrow0.                  \tag{3.5}
\]

### Proof

The ratios `C_(m+1)/C_m` stay between two positive constants, so (3.4) is
equivalent to the same statement with `C_(m+1)` in the denominator.
Telescoping (3.2) gives

\[
 e_M\le e_{m_0}+
       \sum_{m=m_0}^{M-1}{B_m\over C_{m+1}}=o(M).                  \tag{3.6}
\]

Equation (3.3) now gives `p_M=o(1)`.  QED.

The contrapositive is the useful statement: if the canonical MSW first
shadow has positive limiting miss density, then *no* targetwise deletion
flow can have a Cesaro-sub-Catalan residual at the critical coefficient.
In fact, if `liminf p_m >= p>0`, the positive normalized increments obey

\[
 \liminf_{M\to\infty}{1\over M}
 \sum_{m<M}\max\{0,e_{m+1}-e_m\}\ge 4p,                            \tag{3.7}
\]

because their sum dominates `e_M-e_(m_0)`.

## 4. Exact residual identity

There is also a direct expression showing the scale of the obstruction.
One has

\[
\begin{aligned}
 {L_{m+1}-A_mL_m\over C_m}
  ={}& {2(m+1)(2m+1)(2m+3)\over(m+2)(m+3)}
       (p_{m+1}-p_m)\\
   &+{4(2m+1)(m^2+5m+3)\over(m+2)^2(m+3)}p_m.          \tag{4.1}
\end{aligned}
\]

The two coefficients are respectively `8m+O(1)` and `8+O(1/m)`.
Consequently, if

\[
 p_m\to p>0,qquad p_{m+1}-p_m=o(1/m),                            \tag{4.2}
\]

then the unavoidable residual tends to

\[
 {L_{m+1}-A_mL_m\over C_m}\to8p,qquad
 {E_{m+1}-A_mE_m\over C_m}\to16p.                                \tag{4.3}
\]

For orientation only, the current data are compatible with a positive
limit somewhere around `1/3` (a random-occupancy heuristic would instead
suggest a constant near `1/e`).  No value is claimed.  If `p=1/3`, (4.3)
would give the two-sided Catalan residual `16C_m/3`, close to the increasing
finite values in (2.6).

## 5. Consequence for the research programme

The targetwise ECO deletion graph remains mathematically correct, but for
the **unchanged canonical MSW factor** its critical Hall theorem should not
be the next main target.  It can succeed with Cesaro-sub-Catalan loss only
if one first proves the surprising assertion `p_m -> 0`, contrary to every
computed value.

The productive alternatives are:

1. prove a positive lower limit (or merely a positive Cesaro lower density)
   for `p_m`, which would close the canonical critical-ECO branch
   rigorously;
2. perform positive-density integral component switches or another global
   re-bundling *before* applying ECO, so that the new factor has
   `o(N_m)` first-shadow defect;
3. replace the MSW vertical factor entirely by the nested-rainbow
   cyclic-interval resolution isolated in the main handoff.

The correct asymptotic question is therefore not whether individual MSW
holes have many deletion parents.  They do.  It is whether the factor can
be globally rewired so that the *number* of holes becomes submacroscopic.

