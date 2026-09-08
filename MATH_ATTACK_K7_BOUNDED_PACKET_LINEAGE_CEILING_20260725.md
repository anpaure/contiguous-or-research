# Lane K7: bounded-lineage ceiling for dependent contextual-packet schedules

Date: 2026-07-25

Method: pure mathematics only. No computation, finite search, solver, or web input
is used.

## 0. Result and exact boundary

Put

\[
 n=2m+1,\qquad W=\binom{n}{m},\qquad
 B=\frac Wn=\operatorname{Cat}_m.
\]

Consider an arbitrary adaptive sequence of literal exact wreath factors

\[
 F_0,F_1,\ldots,F_M.                                      \tag{0.1}
\]

At step \(t\), suppose \(F_t\) is obtained from \(F_{t-1}\) by one freshly
applicable universal aligned common-tail two-for-two packet switch.  The packet
may be chosen after seeing the entire preceding path.  Packets may overlap, be
reused, have different coordinate transpositions, and be newly recomputed at
every step.

Let \(U_t\subseteq\binom{[n]}m\) be the union of the middle masks owned by the
two negative wreaths at step \(t\).  Define the persistent middle-root
congestion

\[
 \Delta=\max_{X\in\binom{[n]}m}
 \bigl|\{t:X\in U_t\}\bigr|.                            \tag{0.2}
\]

Then the number of packet switches satisfies the exact inequality

\[
 \boxed{M\le \frac{\Delta B}{2}.}                       \tag{0.3}
\]

If \(M_1(F)\) is the number of missing rank-\((m-1)\) targets, then

\[
 \boxed{M_1(F_0)-M_1(F_M)\le \Delta B.}                 \tag{0.4}
\]

Consequently, for every fixed \(\delta>0\),

\[
 M_1(F_0)\ge\delta W,\qquad M_1(F_M)=o(W)
 \quad\Longrightarrow\quad
 \boxed{\Delta\ge(\delta-o(1))n.}                      \tag{0.5}
\]

Thus no bounded-congestion, or even \(o(n)\)-congestion, dependent selection of
the canonical contextual packet atoms can escape the first-shadow ceiling.
This remains true under arbitrary overlap, reuse, adaptive signs, and fresh
recomputation.

There is an exact multidepth version with the integral floor baselines retained.
For \(1\le q\le H\le m-2\), put

\[
 N_q=\binom n{m-q},\qquad W=c_qN_q+r_q,\qquad
 c_q=\left\lfloor\frac W{N_q}\right\rfloor,\quad
 0\le r_q<N_q.                                         \tag{0.6}
\]

Let \(\mathcal B_q\) consist of the integral quota vectors having exactly
\(r_q\) coordinates \(c_q+1\) and all other coordinates \(c_q\), and define

\[
 O_q(F)=\frac12\min_{b\in\mathcal B_q}
       \|\mu_q(F)-b\|_1,\qquad
 J_H(F)=\sum_{q=1}^H\frac{O_q(F)}{c_q},                 \tag{0.7}
\]

where \(\mu_q(F)\) is the rank-\((m-q)\) cyclic-interval load vector.  For
\(m\ge3\), \(c_1=1\).  If

\[
 S_H(m)=\sum_{q=1}^H\frac1{c_q},                       \tag{0.8}
\]

then

\[
 \boxed{
 |J_H(F_M)-J_H(F_0)|
 \le \Delta B\,(2S_H(m)-1).
 }                                                       \tag{0.9}
\]

For \(H=\lceil A\sqrt m\rceil\), fixed \(A>0\), write

\[
 \kappa_A=\int_0^A\frac{dx}{\lfloor e^{x^2}\rfloor}.
                                                               \tag{0.10}
\]

Then \(S_H=(\kappa_A+o(1))\sqrt m\).  Hence

\[
 J_H(F_0)\ge\delta W,\qquad J_H(F_M)=o(W)
 \quad\Longrightarrow\quad
 \boxed{
 \Delta\ge
 \frac{(\delta-o(1))n}{2S_H-1}
 =\left(\frac\delta{\kappa_A}+o(1)\right)\sqrt m.
 }                                                       \tag{0.11}
\]

Under the frozen macroscopic first-shadow premise, (0.5), rather than (0.11),
is the stronger conclusion.

The theorem does **not** cover a fresh large transposition component switched as
one indivisible move when that move has no legal decomposition into universal
aligned packet microsteps.  Such a component is precisely the surviving
commutator escape.  Merely choosing the original overlapping packet edges by a
dependent discrepancy, flow, LLL, or colouring rule is now closed unless the
resulting literal schedule incurs linear middle-root congestion.

## 1. Literal packet roots and the switch-count identity

Every wreath in an exact factor owns exactly \(n\) distinct middle masks, and
different wreaths own disjoint middle masks.  Therefore the two negative rows of
step \(t\) own exactly

\[
 |U_t|=2n                                                   \tag{1.1}
\]

middle roots.  The universal two-for-two identity says that the two positive
rows partition this same set \(U_t\); in particular the step is a genuine
integral exact-factor move.  No fractional superposition is being counted.

Double-count the incidence set

\[
 \mathcal I=\{(t,X):X\in U_t\}.                         \tag{1.2}
\]

By (1.1),

\[
 |\mathcal I|=2nM.                                     \tag{1.3}
\]

By the definition of \(\Delta\), every one of the \(W\) fixed middle masks
occurs in at most \(\Delta\) pairs in \(\mathcal I\), so

\[
 |\mathcal I|\le\Delta W=\Delta nB.                    \tag{1.4}
\]

Combining (1.3)--(1.4) and cancelling \(n\) proves (0.3).

This proof is pathwise.  Nothing assumes that the packet atlas was fixed at
time zero, that different packets are disjoint, that the signs are random, or
that the transpositions commute.

## 2. Exact first-shadow speed limit

The audited universal four-arm identity gives, for one aligned packet \(z_t\),

\[
 \|B_{m-1}z_t\|_1=4.                                   \tag{2.1}
\]

More precisely, its rank-\((m-1)\) action has two \(+1\) and two \(-1\)
coordinates.  A previously missing target can cease to be missing only at a
positive coordinate.  Therefore one step can reduce the number of holes by at
most two:

\[
 M_1(F_{t-1})-M_1(F_t)\le2.                            \tag{2.2}
\]

Sum (2.2) over the path and apply (0.3):

\[
 M_1(F_0)-M_1(F_M)\le2M\le\Delta B,                   \tag{2.3}
\]

which proves (0.4).  Since \(W=nB\), the hypotheses in (0.5) turn (2.3)
into

\[
 (\delta-o(1))nB\le\Delta B.
\]

This proves (0.5) with its exact leading constant.

## 3. Exact floor-aware multidepth bound

For equal-total vectors, distance to the quota set is Lipschitz:

\[
 |O_q(\mu+d)-O_q(\mu)|
 \le\frac12\|d\|_1.                                   \tag{3.1}
\]

Indeed, distance to a fixed set is 1-Lipschitz in \(\ell^1\), and (0.7)
contains the factor \(1/2\).

The universal packet footprint is exact:

\[
 \frac12\|B_{m-q}z_t\|_1=
 \begin{cases}
 2,&q=1,\\
 4,&2\le q\le H.
 \end{cases}                                           \tag{3.2}
\]

Thus one packet changes \(J_H\) in absolute value by at most

\[
 \frac2{c_1}+4\sum_{q=2}^H\frac1{c_q}.                \tag{3.3}
\]

For \(m\ge3\),

\[
 c_1=\left\lfloor\frac{m+2}{m}\right\rfloor=1,
\]

so (3.3) is exactly

\[
 4S_H-2.                                               \tag{3.4}
\]

Telescoping and then using (0.3) gives

\[
\begin{aligned}
 |J_H(F_M)-J_H(F_0)|
 &\le M(4S_H-2)\\
 &\le\frac{\Delta B}{2}(4S_H-2)
 =\Delta B(2S_H-1),
\end{aligned}                                          \tag{3.5}
\]

which is (0.9).  Notice that all floors \(c_q\) remain inside the exact
finite-\(m\) inequality.

For \(q=O_A(\sqrt m)\),

\[
 \frac W{N_q}
 =\prod_{i=0}^{q-1}\frac{m+2+i}{m-i},
\qquad
 \log\frac W{N_q}
 =\frac{q(q+1)}m+O_A(m^{-1/2}).                        \tag{3.6}
\]

The Riemann sum, with the finitely many floor jump points ignored as a
measure-zero set, gives

\[
 S_H=(\kappa_A+o(1))\sqrt m.                           \tag{3.7}
\]

Substitution into (3.5), using \(W=nB\), proves (0.11).

At depth one, every quota entry is at least one.  Hence each hole contributes
at least one unit to the quota deficit, and equal total mass gives

\[
 O_1(F)\ge M_1(F).                                     \tag{3.8}
\]

Thus a frozen lower bound \(M_1(F_0)\ge\delta W\) also implies
\(J_H(F_0)\ge\delta W\), although the direct estimate (0.5) is stronger.

## 4. Why row lineage is not the invariant

A two-for-two switch replaces two old wreaths by two new wreaths partitioning
the same \(2n\) middle roots.  There is generally no distinguished bijection
from the old pair to the new pair: each new wreath can own roots formerly split
between both old wreaths.  Consequently a statement such as "each row lineage
is used at most \(D\) times" is undefined unless an additional lineage pairing
is supplied as part of the construction.  Different artificial pairings can
give different congestion counts.

The middle masks themselves have fixed identities throughout the path.  The
sets \(U_t\) in (0.2) are therefore canonical and make the double count
(1.3)--(1.4) immune to all rebundling ambiguity.  If a proposed construction
does provide a persistent row-lineage system, its congestion estimate is useful
only after it is converted to a bound on (0.2).

## 5. Proved and surviving boundary

The following is proved with exact constants:

* arbitrary adaptive, overlapping, repeatedly recomputed universal aligned
  packet schedules satisfy (0.3), (0.4), and (0.9);
* repairing a macroscopic first-shadow defect requires a middle root to lie in
  linearly many packet supports, as in (0.5);
* without the frozen first-shadow premise, an order-\(W\) Gaussian-window drop
  still requires congestion of order \(\sqrt m\), with the constant in (0.11);
* every endpoint and every intermediate state is an integral exact factor, so
  standard wreath linearization gives literal contiguous-OR realizability.

The following is not proved and is not excluded:

* prepare by aligned packets, recompute a different transposition overlay, and
  switch a large fresh component whose lower-shadow action is not a sum of legal
  aligned packet microsteps;
* prove targetwise sign dispersion inside those fresh components and select
  their sides with a near-perfect multidepth discrepancy theorem.

Accordingly, bounded-congestion dependent selection of the **native contextual
packet atoms** is rigorously closed.  Quantitative multidepth balancing can escape
only through genuinely nonlocal fresh components or through linear root reuse;
bounded overlap by itself is insufficient.

## 6. A floor-exact dependent signing theorem for one fresh overlay

The preceding ceiling leaves an indivisible fresh component switch open.  This
section gives an exact dependent-selection theorem for such components.  It is a
genuine positive lemma: under a unit-leakage and low-cyclomatic hypothesis, one
common component signing balances every depth simultaneously.  It also pinpoints
why bounded incidence degrees alone are insufficient.

Fix an exact factor \(F\) and a coordinate transposition \(\rho\).  Let
\(\mathscr C\) be the component partition of the freshly recomputed
\(F\)-versus-\(\rho F\) owner overlay.  Every choice
\(\varepsilon\in\{-1,+1\}^{\mathscr C}\), where \(+1\) retains a component and
\(-1\) switches it, gives a literal integral exact factor \(F_\varepsilon\).

At depth \(q\), take a moved target pair

\[
 p=\{S,\rho S\},\qquad S\ne\rho S.                    \tag{6.1}
\]

For \(C\in\mathscr C\), let

\[
 a_{pC}=\#\{\text{rank-}(m-q)\text{ occurrences of }S
                 \text{ in rows of }C\},
\]

\[
 b_{pC}=\#\{\text{rank-}(m-q)\text{ occurrences of }\rho S
                 \text{ in rows of }C\},              \tag{6.2}
\]

and put

\[
 z_{pC}=a_{pC}-b_{pC},\qquad
 \ell_p=\sum_C(a_{pC}+b_{pC}).                         \tag{6.3}
\]

Switching \(C\) interchanges \(a_{pC}\) and \(b_{pC}\).  Therefore the two
loads in the signed factor are exactly

\[
 \boxed{
 \mu_q^{\varepsilon}(S)
 =\frac{\ell_p+D_p(\varepsilon)}2,
 \qquad
 \mu_q^{\varepsilon}(\rho S)
 =\frac{\ell_p-D_p(\varepsilon)}2,
 }
                                                               \tag{6.4}
\]

where

\[
 D_p(\varepsilon)=\sum_{C\in\mathscr C}\varepsilon_Cz_{pC}.
                                                               \tag{6.5}
\]

This is an identity of integral occurrence counts, not a signed relaxation.

Construct a bipartite graph \(G\).  Its left vertices are all moved pairs
\((q,p)\), simultaneously over \(1\le q\le H\), and its right vertices are
the fresh components \(C\in\mathscr C\).  Join \((q,p)\) to \(C\) exactly
when \(z_{pC}\ne0\).

### Theorem 6.1 (simultaneous component-forest signing)

Assume the following four conditions.

1. Every \(\rho\)-fixed target already has load \(c_q\) or \(c_q+1\).
2. Every moved pair at depth \(q\) has

   \[
   \ell_p\in\{2c_q,2c_q+1,2c_q+2\}.                  \tag{6.6}
   \]

3. Leakage is unit:

   \[
   z_{pC}\in\{-1,0,1\}                                \tag{6.7}
   \]

   for every pair and component.
4. The incidence graph \(G\) is a forest.

Then there is one component signing \(\varepsilon\) such that, simultaneously
for every \(q\le H\), every target load in \(F_\varepsilon\) is \(c_q\) or
\(c_q+1\).  Hence

\[
 \boxed{O_q(F_\varepsilon)=0\quad(1\le q\le H),
 \qquad J_H(F_\varepsilon)=0.}                         \tag{6.8}
\]

#### Proof

Ignore isolated left vertices for the moment.  Root each nontrivial component
of the bipartite forest at an arbitrary component vertex.  Give every root
component either sign.  Traverse away from the root.

When a constraint vertex \((q,p)\) is reached, exactly one adjacent component
is its parent and already has a sign.  Every other adjacent component is a
child whose sign has not yet been chosen.  If the constraint degree \(d\) is
even, choose the \(d-1\) child contributions
\(\varepsilon_Cz_{pC}\in\{-1,+1\}\) to sum to the negative of the parent
contribution.  This is possible because \(d-1\) is odd.  It gives

\[
 D_p=0.                                                 \tag{6.9}
\]

If \(d\) is odd, choose the \(d-1\) child contributions to sum to zero.  This
is possible because \(d-1\) is even, and it gives

\[
 |D_p|=1.                                               \tag{6.10}
\]

The child component signs are now fixed and serve as parent signs at all later
constraint vertices.  Acyclicity ensures that no sign is assigned twice.

For every \(C\),

\[
 a_{pC}+b_{pC}\equiv a_{pC}-b_{pC}=z_{pC}\pmod2.
                                                               \tag{6.11}
\]

Under (6.7), a nonzero \(z_{pC}\) is odd and a zero \(z_{pC}\) comes from an
even \(a_{pC}+b_{pC}\).  Hence

\[
 \ell_p\equiv d\pmod2.                                 \tag{6.12}
\]

Thus (6.9)--(6.10) say exactly that \(D_p=0\) when \(\ell_p\) is even and
\(|D_p|=1\) when \(\ell_p\) is odd.  Together with (6.4) and (6.6), this gives

\[
 \{\mu_q^\varepsilon(S),\mu_q^\varepsilon(\rho S)\}
 =
 \begin{cases}
 \{c_q,c_q\},&\ell_p=2c_q,\\
 \{c_q,c_q+1\},&\ell_p=2c_q+1,\\
 \{c_q+1,c_q+1\},&\ell_p=2c_q+2.
 \end{cases}                                           \tag{6.13}
\]

An isolated constraint has every \(z_{pC}=0\), so (6.11) makes \(\ell_p\)
even and its two loads are already equal.  Equation (6.6) then gives the first
or third line of (6.13).  The fixed targets are balanced by hypothesis 1.

All target loads are therefore floor or ceiling.  Since their total is \(W\),
exactly \(r_q=W-c_qN_q\) of them are ceilings.  Thus the vector belongs to
\(\mathcal B_q\), proving (6.8).  Finally, the chosen signs switch whole fresh
owner components, so the selected endpoint is an integral exact wreath factor.
\(\square\)

The forest hypothesis has a useful exact strengthening.  Let \(Z\) be the
joint integer matrix, with rows indexed by all moved pairs \((q,p)\), columns
indexed by \(C\in\mathscr C\), and entries \(Z_{pC}=z_{pC}\).

### Theorem 6.1A (totally-unimodular component signing)

In Theorem 6.1, replace hypothesis 4 by

\[
 \boxed{Z\text{ is totally unimodular}.}               \tag{6.13a}
\]

Then the same exact simultaneous conclusion (6.8) holds.

#### Proof

Put \(s=Z\mathbf1\), and consider

\[
 P=\left\{x\in[0,1]^{\mathscr C}:
 \left\lfloor\frac{s_p}{2}\right\rfloor
 \le (Zx)_p\le
 \left\lceil\frac{s_p}{2}\right\rceil
 \text{ for every }p\right\}.                         \tag{6.13b}
\]

The point \(x=\frac12\mathbf1\) belongs to \(P\), so \(P\ne\varnothing\).
Total unimodularity of \(Z\), together with the integral right sides and the
box constraints, implies that every vertex of \(P\) is integral.  Choose an
integral vertex \(x\in\{0,1\}^{\mathscr C}\), and put

\[
 \varepsilon_C=1-2x_C.                                 \tag{6.13c}
\]

Then

\[
 D(\varepsilon)=Z\varepsilon=s-2Zx.                   \tag{6.13d}
\]

Thus \(D_p=0\) when \(s_p\) is even and \(|D_p|=1\) when \(s_p\) is odd.
By (6.11)--(6.12), \(s_p\equiv\ell_p\pmod2\).  Equations
(6.4), (6.6), and (6.13d) now give (6.13) exactly, and the remainder of
Theorem 6.1's proof applies. \(\square\)

A signed \(\{-1,0,1\}\)-matrix whose bipartite support graph is a forest is
totally unimodular.  Indeed, every nonempty square submatrix has a row or column
with at most one nonzero entry--otherwise its finite support would contain a
cycle--and determinant expansion inducts on its order.  Thus Theorem 6.1 is a
special case of Theorem 6.1A.  The direct rooted proof was retained because it
exhibits the dependent signing explicitly and makes the absence of sign
conflicts transparent.

### Theorem 6.2 (near-forest quantitative form)

Retain hypotheses 1--3 of Theorem 6.1.  Suppose there are simultaneously
chosen sets \(\mathcal R_q\) of moved-pair constraint vertices, with
\(|\mathcal R_q|=R_q\), such that deleting the single joint set
\(\bigcup_{q=1}^H\mathcal R_q\) makes the remaining all-depth matrix totally
unimodular.  (It is enough that the remaining joint incidence graph be a
forest.)  Then one common
component signing satisfies

\[
 \boxed{
 O_q(F_\varepsilon)\le(c_q+1)R_q,
 \qquad
 J_H(F_\varepsilon)
 \le\sum_{q=1}^H\left(1+\frac1{c_q}\right)R_q
 \le2\sum_{q=1}^HR_q.
 }                                                       \tag{6.14}
\]

In particular,

\[
 \sum_{q=1}^HR_q=o(W)\quad\Longrightarrow\quad
 J_H(F_\varepsilon)=o(W).                              \tag{6.15}
\]

#### Proof

Apply Theorem 6.1A to the remaining matrix.  Every undeleted pair is exactly
balanced.  For a deleted pair with total \(\ell_p\),
choose its quota pair to have the same total: \((c_q,c_q)\), an orientation of
\((c_q,c_q+1)\), or \((c_q+1,c_q+1)\), according to the three cases in
(6.6).  Because the actual two loads are nonnegative integers with this same
total, their half-\(\ell^1\) distance from a suitable such quota pair is at most
\(c_q+1\).  Summing over the \(R_q\) exceptional pairs proves the first
inequality in (6.14).

The quotas selected on every pair, together with the fixed-target quotas, have
total \(W\), and hence contain exactly \(r_q\) ceiling entries.  They form an
element of \(\mathcal B_q\).  Divide by \(c_q\), sum over \(q\), and use
\(c_q\ge1\) to prove the rest of (6.14). \(\square\)

If the finite incidence graph has cyclomatic excess

\[
 \beta(G)=|E(G)|-|V(G)|+\operatorname{comp}(G),         \tag{6.16}
\]

then one may take

\[
 \sum_qR_q\le\beta(G).                                 \tag{6.17}
\]

Indeed, choose a spanning forest.  For every nonforest edge, mark its constraint
endpoint and delete all marked constraint vertices.  At most \(\beta(G)\)
vertices are marked, and the remaining graph is a subgraph of the spanning
forest.  Hence \(\beta(G)=o(W)\), together with hypotheses 1--3, is an exact
sufficient condition for the required \(o(W)\) multidepth floor overflow.

### 6.1 Exact width-two holonomy criterion

The TU condition has a transparent form when every nontrivial constraint row
has exactly two unit entries.  Regard the component columns as vertices of a
signed multigraph.  If row \(p\) meets \(C,D\), put

\[
 r_p=-z_{pC}z_{pD}\in\{-1,+1\}.                       \tag{6.17a}
\]

Parity-optimal discrepancy on this even row is equivalent to

\[
 \varepsilon_C\varepsilon_D=r_p.                      \tag{6.17b}
\]

Thus all width-two rows are simultaneously soluble if and only if

\[
 \boxed{\prod_{p\in\gamma}r_p=1
 \quad\text{for every graph cycle }\gamma.}            \tag{6.17c}
\]

Indeed, necessity follows by multiplying (6.17b) around a cycle.  For
sufficiency, choose one sign in each connected component and propagate it along
paths; (6.17c) makes the result path-independent.

When (6.17c) holds, switch column signs according to one solution of
(6.17b).  Up to multiplying individual rows by \(-1\), every width-two row
then has entries \((+1,-1)\).  The resulting matrix is the transpose of an
oriented graph incidence matrix and is totally unimodular.  Column and row sign
changes preserve total unimodularity, so the original leakage matrix is TU.

Conversely, a cycle violating (6.17c) has a square cycle submatrix of determinant
\(\pm2\) (expand after switching all but one edge to the oriented form), and the
matrix is not TU.  Hence, in the width-two regime, total unimodularity is
**exactly** absence of signed-cycle holonomy.  Deleting \(o(W)\) target rows to
make the system TU is precisely a weighted frustration/odd-cycle-edge deletion
condition, not a degree condition.

### 6.2 Bounded degrees alone do not imply the signing gate

Even at depth one, bounded target and component congestion cannot replace the
low-cyclomatic condition.  Suppose a hole \(S\) is paired with \(\rho S\), and
the occurrences at \(\rho S\) lie in component groups of positive sizes
\(h_C\).  After signing, both members of the pair are nonmissing exactly when
the selected component set is neither empty nor the entire support

\[
 \mathcal H_S=\{C:h_C>0\}.                              \tag{6.18}
\]

Thus simultaneous hole repair is exactly the property-B/NAE colouring problem
for the hyperedges \(\mathcal H_S\).  When every \(|\mathcal H_S|=2\), it is
exactly a graph cut problem.

A disjoint union of triangles has target degree two and component degree two,
yet every two-colouring leaves at least one edge per triangle monochromatic.
Therefore at least one third of its constraints fail.  This is a rigorous
abstract obstruction to any theorem whose only hypotheses are bounded row or
target incidence degrees.  It is not asserted here that the canonical MSW fresh
overlay realizes disjoint triangles; rather, it proves that the missing MSW
input must control global sign frustration--for example by (6.16)--and cannot be
replaced by congestion bounds alone.

The exact remaining canonical statement is now sharply testable: find one fresh
nonlocal overlay for which the pair totals (6.6), unit leakage (6.7), and
\(o(W)\) constraint-side feedback set all hold across the Gaussian window.  The
selection and literal exact-factor completion would then follow from Theorem
6.2 without any independent rounding loss.
