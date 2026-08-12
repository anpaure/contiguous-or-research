# Lane K audit: exact Catalan mass and carrier cells around the early two-boundary square

Date: 2026-07-26

Method: pure mathematics only. No computation, search, solver, script, or web
input is used.

## 0. Verdict

Write

\[
                         C_t=\operatorname{Cat}_t.
\]

Assume the proposed two-boundary occurrence atlas really has the four
disjoint strata

\[
 \Omega_{11}\simeq\mathcal D_s,qquad
 \Omega_{10}\simeq\mathcal D_{s-1},\qquad
 \Omega_{01}\simeq\mathcal D_{s-1},\qquad
 \Omega_{00}\simeq\mathcal D_{s-2}.                  \tag{0.1}
\]

Here the first and second subscripts record whether the left and right
boundary bits, respectively, are visible. Then the exact occurrence mass is

\[
                         M_s=C_s+2C_{s-1}+C_{s-2}.     \tag{0.2}
\]

The frequently quoted constants are only asymptotic:

\[
 \boxed{
 \frac{M_s}{C_s}
 =\frac{5s(5s-7)}{4(2s-3)(2s-1)}
 =\frac{25}{16}
  +\frac{15(4s-5)}{16(2s-3)(2s-1)}.}                 \tag{0.3}
\]

Thus \(M_s/C_s>25/16\) at every finite scale. If all four strata collapse
onto the same four physical Boolean cells, the sharp scalar cap condition is

\[
 \boxed{
 \frac{C_s}{p}
 \le \kappa_s
 :=\frac{16(2s-3)(2s-1)}{5s(5s-7)}.}                 \tag{0.4}
\]

One has

\[
 \boxed{
 \kappa_s<\frac{64}{25},qquad
 \frac{64}{25}-\kappa_s
 =\frac{48(4s-5)}{25s(5s-7)}.}                       \tag{0.5}
\]

Hence \(64/25\) is the limiting threshold, not an exact safe finite-\(s\)
condition.

The physical-carrier issue changes the answer. A fully separated carrier has
three left symbols and three right symbols and therefore supplies the nine
targets of a literal \(3\times3\) grid. In that case the sharp scalar
conditions are

\[
                         C_s\le4p,qquad
                         C_{s-1}\le2p,qquad
                         C_{s-2}\le p.                \tag{0.6}
\]

At the first scale with \(C_s\ge p\), all three hold strictly except possibly
the harmless equality in the first inequality: indeed \(C_s<4p\) and
\(C_{s-1}<p\). Thus the \(25/16\) total-mass toll disappears if the five
collar/background cells are genuinely distinct from the central square.

The existing \(D_4\) Boolean-square certificate proves only the four central
targets. It does not specify the two collar carrier symbols or the background
carrier and therefore proves neither four-cell collapse nor nine-cell
separation. The authoritative condition for an intermediate carrier pattern
is the capacitated Hall criterion in Section 5.

## 1. Exact Catalan decomposition

The four-stratum statement (0.1) has a simple exact meaning. A bulk
occurrence sees both boundary switches and retains a free Dyck filling of
semilength \(s\). A left- or right-collar occurrence consumes one prescribed
boundary peak, leaving a free filling of semilength \(s-1\). A background
occurrence consumes both prescribed boundary peaks, leaving a filling of
semilength \(s-2\).

Whenever the two prescribed peaks are distinguished in the aligned context,
deleting them is invertible. Therefore the four deletion maps are bijections
onto the four Dyck families in (0.1), and the strata are disjoint because
their two visibility bits differ. This proves (0.2).

This paragraph is an audit of the standard optional-boundary-peak atlas. It
is not supplied merely by the two marked rows in the isolated (D_4) factor.
For a claimed physical deployment one must still display the distinguished
peaks, the occurrence-to-stratum map, and the assertion that no additional
crossing slots enter the same target family.

## 2. Exact ratio and the status of (25/16)

The Catalan quotients are

\[
 \frac{C_{s-1}}{C_s}
 =\frac{s+1}{2(2s-1)},                                \tag{2.1}
\]

and

\[
 \frac{C_{s-2}}{C_s}
 =\frac{s(s+1)}{4(2s-3)(2s-1)}.                       \tag{2.2}
\]

Consequently

\[
\begin{aligned}
 \frac{M_s}{C_s}
 &=1+\frac{s+1}{2s-1}
   +\frac{s(s+1)}{4(2s-3)(2s-1)}\\
 &=\frac{5s(5s-7)}{4(2s-3)(2s-1)}.                   \tag{2.3}
\end{aligned}
\]

Subtracting (25/16) gives the positive correction in (0.3). Thus

\[
                         \frac{M_s}{C_s}\downarrow\frac{25}{16}
                         \quad(s\to\infty),            \tag{2.4}
\]

but replacing the exact ratio by (25/16) undercounts the finite-scale
mass. For example,

\[
 \frac{M_3}{C_3}=2,qquad
 \frac{M_4}{C_4}=\frac{13}{7},qquad
 \frac{M_5}{C_5}=\frac{25}{14}.                       \tag{2.5}
\]

## 3. Four-cell collapse and the exact \(64/25\) correction

Suppose all strata use the same four physical cells, indexed by
\((\epsilon,\eta)\in\{0,1\}^2\). In the ideal scalar model:

* the \(C_s\) bulk tokens may use all four cells;
* the left collar may use the two cells \((0,0),(1,0)\);
* the right collar may use \((0,0),(0,1)\); and
* the \(C_{s-2}\) background is fixed at \((0,0)\).

Put

\[
                         d=C_s,qquad c=C_{s-1},qquad b=C_{s-2}. \tag{3.1}
\]

### Theorem 3.1 (sharp scalar four-cell condition)

Assume the occurrences within each displayed stratum can be routed
integrally among its permitted cells. Then all four loads can be made at
most \(p\) if and only if

\[
                         d+2c+b\le4p.                 \tag{3.2}
\]

#### Proof

Necessity is total capacity. For sufficiency, put the background in cell
\(00\), the complete left collar in cell \(10\), and the complete right
collar in cell \(01\). Their loads are \((b,c,c,0)\), all below \(p\) because

\[
                         b\le c<p                     \tag{3.3}
\]

at the minimal early scale. The residual capacities of the four cells have
total

\[
                         4p-b-2c\ge d.                \tag{3.4}
\]

Distribute the \(d\) bulk tokens integrally through those residual slots.
This proves sufficiency. \(\square\)

Divide (3.2) by \(p\) and use (0.3). The exact normalized condition is
(0.4). Formula (0.5) follows by direct subtraction. Thus \(64/25\) is an
asymptotic mnemonic and is slightly too permissive at every finite scale.

The theorem is a scalar routing statement. It does not prove that the two
ownership-component partitions can realize an arbitrary bulk allocation;
that is the separate joint-discrepancy gate.

## 4. A fully carrier-resolved nine-cell atlas

Let the left boundary have active labels

\[
                         \lambda_0,\lambda_1
\]

and inactive carrier label \(\lambda_*\). Let the right boundary have
active labels

\[
                         \rho_0,\rho_1
\]

and inactive carrier label \(\rho_*\). Assume these six labels are distinct,
the left and right alphabets are disjoint, and all are outside a common core
\(K\). Define

\[
                         T_{ij}=K\cup\{\lambda_i,\rho_j\},
                         \qquad i,j\in\{0,1,*\}.       \tag{4.1}
\]

### Lemma 4.1 (nine distinct physical cells)

The nine sets in (4.1) are pairwise distinct.

#### Proof

Intersection with the left alphabet recovers \(i\), and intersection with
the right alphabet recovers \(j\). \(\square\)

The four Catalan strata occupy exactly

\[
\begin{array}{c|c|c}
\text{stratum}&\text{mass}&\text{physical cells}\\ \hline
\Omega_{11}&C_s&T_{00},T_{01},T_{10},T_{11}\\
\Omega_{10}&C_{s-1}&T_{0*},T_{1*}\\
\Omega_{01}&C_{s-1}&T_{*0},T_{*1}\\
\Omega_{00}&C_{s-2}&T_{**}.
\end{array}                                           \tag{4.2}
\]

### Theorem 4.2 (sharp scalar nine-cell condition)

Under the same integral-routing idealization, all nine loads can be kept at
most \(p\) if and only if

\[
                         C_s\le4p,qquad
                         C_{s-1}\le2p,qquad
                         C_{s-2}\le p.                \tag{4.3}
\]

#### Proof

The four support sets in (4.2) are disjoint. Their respective capacities are
\(4p,2p,2p,p\), proving necessity. If the four inequalities hold, distribute
each stratum independently among its own cells; integral capacities give an
integral allocation. \(\square\)

At \(s=\min\{t:C_t\ge p\}\), one has

\[
 C_{s-1}<p,qquad C_{s-2}<p,qquad
 C_s<\left(4-\frac6{s+1}\right)p<4p.                 \tag{4.4}
\]

Thus the nine-cell carrier is scalar-cap-safe throughout the entire early
overshoot interval. Its only nontrivial remaining issue is balanced routing
of the \(C_s\) bulk among the four central cells.

If the left and right bulk choices are constant on two partitions whose
blocks have size at most \(B\), the two-partition discrepancy theorem gives
the explicit sufficient integral bound

\[
             \max_{\epsilon,\eta}n_{\epsilon,\eta}
             \le \frac{C_s}{4}+\frac34\sqrt{BC_s}.      \tag{4.5}
\]

Hence the separated nine-cell atlas is fully cap-safe whenever

\[
                         \frac{C_s}{4}+\frac34\sqrt{BC_s}\le p.   \tag{4.6}
\]

For fixed \(B\), in particular \(B=14\), this follows for large \(p\) from
the exact Catalan slack

\[
                         p-\frac{C_s}{4}>
                         \frac{3p}{2(s+1)}.             \tag{4.7}
\]

This conclusion still presupposes occurrence coverage and independent exact
legality of the two packet partitions.

## 5. Every intermediate carrier: the sharp Hall condition

The carrier labels may collide after the ambient push-forward. Let

\[
 \varphi:\{0,1,*\}^2\longrightarrow\mathcal T          \tag{5.1}
\]

send a formal cell to its physical target. Put

\[
\begin{aligned}
 S_B&=\varphi(\{0,1\}\times\{0,1\}),\\
 S_L&=\varphi(\{0,1\}\times\{*\}),\\
 S_R&=\varphi(\{*\}\times\{0,1\}),\\
 S_0&=\{\varphi(*,*)\}.
\end{aligned}                                          \tag{5.2}
\]

Assign demands

\[
                         m_B=C_s,\quad m_L=m_R=C_{s-1},\quad
                         m_0=C_{s-2}.                  \tag{5.3}
\]

### Theorem 5.1 (carrier-collapse max-flow criterion)

In the homogeneous scalar routing model, a cap-\(p\) allocation exists if
and only if, for every subfamily

\[
                         \mathcal A\subseteq\{B,L,R,0\},
\]

one has

\[
 \boxed{
       \sum_{A\in\mathcal A}m_A
       \le p\left|\bigcup_{A\in\mathcal A}S_A\right|.} \tag{5.4}
\]

#### Proof

Make a bipartite flow network. A source node \(A\) has supply \(m_A\) and
is joined to every target in \(S_A\). Every target has capacity \(p\) to the
sink. The integral max-flow/min-cut theorem says that all supplies can be
routed exactly when every source subset has total demand at most the total
capacity of its neighbourhood, which is (5.4). All capacities are integral,
so a feasible flow may be integral. \(\square\)

Equation (5.4) is the sharp scalar answer for five, six, seven, or eight
physical cells as well as for the two extremes above. It also shows why the
number of cells by itself is insufficient: their incidence with the four
strata matters.

For the real component problem, replace the four homogeneous source nodes by
the actual occurrence blocks allowed to switch together. The same max-flow
condition remains necessary, but independent routing inside one source node
may fail; the two-partition discrepancy theorem is one sufficient rounding
tool once all block sizes are controlled.

The \(3\times3\) count is exact only for a **uniform** carrier alphabet with
one inactive symbol on each side and one common core. A row- or start-dependent
outer collar can refine one formal cell into several physical targets. In
that generality there is no nine-cell upper bound from the local \(D_4\)
certificate: one must replace (5.1) by the literal occurrence map

\[
                         \omega\longmapsto\Phi_\omega(T_\omega)           \tag{5.5}
\]

and apply capacitated Hall to the resulting occurrence--target graph. More
physical cells can only improve scalar capacity, but their availability may
be correlated by the common exact-factor choice.

## 6. What the existing \(D_4\) certificate proves

The certified marked rows give two disjoint active pairs, for example

\[
                         \{4,7\},\qquad\{2,6\},        \tag{6.1}
\]

and, with one common interior core \(K\), the four targets

\[
 K\cup\{4,2\},\quad K\cup\{4,6\},\quad
 K\cup\{7,2\},\quad K\cup\{7,6\}.                   \tag{6.2}
\]

Therefore it proves the four central cells in (4.2) are literal and
distinct.

It does **not** provide, in the isolated factor certificate,

1. a left inactive carrier \(\lambda_*\) for every left-collar occurrence;
2. a right inactive carrier \(\rho_*\) for every right-collar occurrence;
3. a common background target \(T_{**}\);
4. disjointness of those five targets from (6.2); or
5. the assertion that the four Catalan strata in (0.1) are the complete
   occurrence multiset landing in this carrier orbit.

Those data belong to a row- and start-resolved parent completion. Hence the
current theorem supports two conditional conclusions, not one unconditional
constant:

* under full four-cell collapse, the exact threshold is \(\kappa_s\) in
  (0.4), asymptotic to \(64/25\) from below;
* under a six-label separated carrier, there are nine physical cells and the
  sharp scalar condition is (4.3), automatically satisfied at the early
  scale.

No choice between these cases is justified until the physical parent carrier
is displayed.

## 7. Scope

The report settles the Catalan arithmetic and every scalar carrier-collision
pattern. It does not prove balanced four-cell realizability, product
compatibility of the left and right packet partitions, or a favourable
multidepth residual-cap sign. Those remain exactly the geometric and
rounding gates identified in the early-scale capacity theorem.

An independent audit verified (0.3)--(0.5), the \(4+2+2+1\) formal-cell
decomposition, and the two sharp scalar cap criteria. It also emphasized
that the Catalan families in (0.1) may overlap as untagged Dyck rows; their
disjointness is as indexed \((\text{row},\text{start})\) occurrences.
Cross-family target identification or separation is entirely a carrier
statement.
