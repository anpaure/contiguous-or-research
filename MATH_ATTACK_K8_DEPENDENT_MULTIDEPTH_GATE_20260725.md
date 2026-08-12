# Lane K8: dependent commutator seams, exact multidepth signing, and the palette-width obstruction

Date: 2026-07-25

Method: pure mathematics only. No web search, finite search, solver, computer
experiment, or long local job is used.

## 0. Exact outcome

Put

\[
 n=2m+1,\qquad W=\binom nm,\qquad
 B=\frac Wn=\operatorname{Cat}_m,
 \qquad H=\lceil A\sqrt m\rceil,
\]

where \(A>0\) is fixed. At depth \(q\), put

\[
 N_q=\binom n{m-q},\qquad
 W=c_qN_q+\rho_q,\quad 0\le\rho_q<N_q,
\]

Take \(m\) sufficiently large that \(H\le m-2\), and let \(O_q\) be half the
\(\ell^1\)-distance from the integral quota
vectors with \(\rho_q\) entries \(c_q+1\) and all other entries \(c_q\). Write

\[
 J_A(F)=\sum_{q=1}^{H}\frac{O_q(F)}{c_q},
 \qquad
 S_A(m)=\sum_{q=1}^{H}\frac1{c_q}
       =(\kappa_A+o(1))\sqrt m,
\]

where

\[
 \kappa_A=\int_0^A\frac{dx}{\lfloor e^{x^2}\rfloor}.
\]

This report proves four new statements.

### A. A dependent packet cut creates linearly many genuine fresh seams

Let \(v_m\) be the exact maximum matching size in the contextual packet graph
of the canonical MSW factor. Thus

\[
 v_m=\left(\frac{11}{72}+o(1)\right)B.
\]

For \(m\ge5\), there exist a nonnative transposition \(\rho\) and a
deterministic dependent choice of the \(v_m\) packet sides such that the pulled-back fresh
\(\rho\)-overlay contains at least

\[
 \boxed{
 s_m\ge
 \frac{v_m(2n-4)m(m-4)}
 {4(2m^2+1)}
 =\left(\frac{11}{288}-o(1)\right)W
 }
 \tag{0.1}
\]

pairwise distinct, loopless, genuine piecewise-commutator seams. The union
\(Z_m\) of fresh components meeting these seams contains at least

\[
 \boxed{
 |Z_m|\ge\frac{2s_m}{n-3}
 =\left(\frac{11}{144}-o(1)\right)B
 }
 \tag{0.2}
\]

left rows. Every counted seam starts at a root genuinely moved by its packet
transposition. None is singleton--singleton identity-gauge turnover. The
preparation has persistent middle-root congestion one.

Thus genuine seam supply and positive mixed-component row mass are
unconditionally established. The theorem does not disperse this mass among
many distinct components: one fresh component could contain all of \(Z_m\).
Nor does it supply lower-rank targetwise leakage or a productive common signing
of the fresh components.

### B. The fresh multidepth signing problem has an exact TU solution

Fix one exact factor and one fresh transposition overlay. For every moved target
pair \(p=\{S,\rho S\}\) and fresh component \(C\), let

\[
 z_{pC}=a_{pC}(S)-a_{pC}(\rho S),
 \qquad
 \ell_p=\sum_C(a_{pC}(S)+a_{pC}(\rho S)).
\]

Form the single all-depth matrix \(Z=(z_{pC})\), using the same component
columns for every \(q\le H\). Suppose:

1. every \(\rho\)-fixed target already has load \(c_q\) or \(c_q+1\);
2. every moved pair at depth \(q\) has
   \(\ell_p\in\{2c_q,2c_q+1,2c_q+2\}\);
3. every leakage coefficient belongs to \(\{-1,0,1\}\); and
4. after deleting one simultaneously chosen joint row set
   \(\mathcal R=\bigsqcup_q\mathcal R_q\), the remaining all-depth matrix is
   totally unimodular.

Then one common whole-component signing gives

\[
 \boxed{
 O_q\le(c_q+1)|\mathcal R_q|,
 \qquad
 J_A\le
 \sum_{q\le H}\left(1+\frac1{c_q}\right)|\mathcal R_q|
 \le2|\mathcal R|.
 }
 \tag{0.3}
\]

In particular, \(\mathcal R=\varnothing\) gives exact floor/ceiling balance at
every depth, while \(|\mathcal R|=o(W)\) gives \(J_A=o(W)\). A forest support
is one sufficient TU case, but not the only one. In width two, TU is exactly
the absence of signed-cycle holonomy. Bounded row and column degrees alone do
not suffice: disjoint signed triangles force one-third of their constraints
to fail.

This is an actual integral global switch theorem, conditional only on explicit
geometry of one fresh overlay. The seam theorem does not prove its three
profile/leakage hypotheses or the near-TU hypothesis.
Complementary upper-rank pairs may be appended as further rows of the same
joint matrix; the proof and the simultaneous-sign quantifier are unchanged.

### C. Bounded-congestion dependence has an exact action ceiling

For an arbitrary adaptive path consisting of freshly recomputed universal
aligned two-for-two packet switches, let \(U_t\) be the invariant \(2n\)-root
packet at step \(t\), let \(M_1(F)\) denote the number of missing
rank-\((m-1)\) targets, and define

\[
 \Delta=\max_X|\{t:X\in U_t\}|.
\]

If the path has \(M\) packet moves, then

\[
 \boxed{
 M\le\frac{\Delta B}{2},\qquad
 M_1(F_0)-M_1(F_M)\le\Delta B,
 }
 \tag{0.4}
\]

and

\[
 \boxed{
 |J_A(F_M)-J_A(F_0)|
 \le\Delta B(2S_A-1).
 }
 \tag{0.5}
\]

Consequently, removing \(\delta W-o(W)\) first-shadow holes requires

\[
 \boxed{\Delta\ge(\delta-o(1))n,}
 \tag{0.6}
\]

while a drop of \(\delta W-o(W)\) in \(J_A\) requires

\[
 \boxed{
 \Delta\ge
 \frac{(\delta-o(1))n}{2S_A-1}
 =\left(\frac\delta{\kappa_A}+o(1)\right)\sqrt m.
 }
 \tag{0.7}
\]

There is also an arbitrary-large-component version. If a switched old row
\(C\) sees the two bridge letters at shorter cyclic distance \(d_t(C)\), then

\[
 \lambda_r(d)=2\min(r,d)-2\mathbf1_{\{r=d\}},
 \qquad 2\le r\le m,
 \tag{0.8}
\]

is its exact positive rank-\(r\) action. Along any adaptive sequence of
arbitrary freshly recomputed complete-component switches,

\[
 M_1(F_T)\ge M_1(F_0)-\sum_{t,C}\lambda_{m-1}(d_t(C)),
 \tag{0.9}
\]

\[
 |J_A(F_T)-J_A(F_0)|
 \le\sum_{t,C}\sum_{q\le H}
 \frac{\lambda_{m-q}(d_t(C))}{c_q}.
 \tag{0.10}
\]

If

\[
 \Gamma_d=\max_X
 \sum_{t,C:\,X\in U_t(C)}d_t(C),
\]

then \(\sum_{t,C}d_t(C)\le\Gamma_dB\). Hence first-shadow repair requires

\[
 \boxed{\Gamma_d\ge(\delta/2-o(1))n.}
 \tag{0.11}
\]

Thus a bounded unweighted congestion \(R\) can escape through arbitrary large
components only if their cyclic bridge distance reaches \(D\) with

\[
 \boxed{RD\ge(\delta/2-o(1))n.}
 \tag{0.12}
\]

### D. Fewer than about \((\log4/\log6)H\) new bridge colours remain orbit-trapped

Write

\[
 \alpha_*=\frac{\log4}{\log6}=0.773705\ldots.
\]

Let

\[
 \mathcal T_m=\{(2s+2\ \ 2s+3):0\le s\le m-2\}
\]

be the fixed native contextual palette. Start at any vertex of the full
intrinsic \((2\ 3)\)-component cell of the canonical factor. Adjoin any fixed
set \(E\) of \(k\) further transpositions, and permit an arbitrary adaptive
sequence of complete-component switches using colours in
\(\mathcal T_m\cup E\).

For \(d=m-q-2\), there is an invariant target union of size at most

\[
 \boxed{
 L_{q,k}=\min\!\left\{N_q,
 6^k(4d+2)\operatorname{Cat}_d\right\}
 }
 \tag{0.13}
\]

which retains mass at least

\[
 M_q=\operatorname{Cat}_d\operatorname{Cat}_q.
 \tag{0.14}
\]

This gives the exact quota floor

\[
 \boxed{
 O_q\ge[M_q-c_qL_{q,k}-\min(L_{q,k},\rho_q)]_+.
 }
 \tag{0.15}
\]

It also gives an exact integral factorial floor. Put

\[
 a=\lfloor M_q/L_{q,k}\rfloor,
 \quad s=M_q-aL_{q,k},
 \quad u=a-c_q.
\]

Whenever \(u\ge1\),

\[
 \boxed{
 2\Phi_q\ge L_{q,k}u(u-1)+2su.
 }
 \tag{0.16}
\]

At \(q=H\), if

\[
 \frac{\operatorname{Cat}_H}{(4d+2)6^k}
 \ge4(c_H+1),
\]

then the safe finite bound is

\[
 \boxed{
 \frac{\Phi_H}{W}
 >\frac{4^H}{8192\,ndH^4\,6^k}.
 }
 \tag{0.17}
\]

Therefore every fixed \(\varepsilon>0\) and every palette with

\[
 k\le\left(\frac{\log4}{\log6}-\varepsilon\right)H
 \tag{0.18}
\]

still has \(\Phi_H/W\to\infty\). To make the certified lower bound cease to
diverge it is necessary that

\[
 \boxed{
 k\ge\frac{\log4}{\log6}H-O(\log m).
 }
 \tag{0.19}
\]

For \(k=0\), the linear quota floor (0.15) is only
\(\Theta_A(Wm^{-7/4})=o(W)\). Thus this is a factorial/collision obstruction,
not a macroscopic balanced-overflow obstruction and not a disproof of the
coefficient-one theorem.

Taken together, (0.1)--(0.19) give the precise answer to the assigned gate:
dependence does create a positive-density reservoir of genuine seams and
seam-incident rows inside fresh components,
but bounded packet congestion cannot use it directly, a single new bridge is
far below the multidepth palette width needed to release the private Catalan
pile, and near-total-unimodularity of the actual all-depth leakage matrix is
one exact sufficient remaining selection condition.

## 1. Proof of the genuine-seam theorem

### 1.1 Exact moved-root support

After the universal packet rotation and relabelling, its two old rows have
omitted-label words

\[
 C=(\delta,\beta,\gamma,\alpha,T),
 \qquad
 D=(\beta,\alpha,\delta,\gamma,T),
\]

and the packet colour is \(\tau=(\beta\ \gamma)\). Under the inverse step-two
map on cyclic positions, the two bridge letters have shorter distances \(m\)
in \(C\) and \(m-1\) in \(D\). Two labels at distance \(d\le m\) are
separated by exactly \(2d\) cyclic middle windows. Hence \(\tau\) moves

\[
 n-1\quad\text{roots in }C,
 \qquad
 n-3\quad\text{roots in }D.
\]

For a packet root cell \(U_i\) and its moved part \(Q_i\), therefore,

\[
 |U_i|=2n,\qquad |Q_i|=2n-4.                         \tag{1.1}
\]

The number eight in the all-rank signed packet footprint comes from
four-row histogram cancellation. It is not the middle-root support in (1.1).

### 1.2 External arc count and the pinned dependent cut

Every root in \(J(n,m)\) has degree \(m(m+1)\). A root in \(Q_i\) has at
most \(|U_i|-1=2n-1\) neighbours inside its packet cell, and hence at least

\[
 d_*=m(m+1)-(2n-1)=m^2-3m-1                         \tag{1.2}
\]

external neighbours. Orient these edges away from \(Q_i\), and let
\(A_\rho\) be the directed arcs of coordinate colour \(\rho\). Then

\[
 \sum_\rho|A_\rho|\ge v_m(2n-4)d_*.                  \tag{1.3}
\]

A fixed colour has at most \(v_m(2n-4)\) such arcs. Delete all \(m-1\)
colours in the full native contextual palette \(\mathcal T_m\). The remaining
arc count is at least \(v_m(2n-4)(d_*-(m-1))\), so averaging gives a genuinely
nonnative \(\rho\) with

\[
 |A_\rho|\ge
 \frac{v_m(2n-4)m(m-4)}{2m^2+1}.                    \tag{1.4}
\]

Give each matched packet cell a bit and pin all unmatched cells to zero. An
arc from cell \(i\) to matched cell \(j\) is active when
\(\varepsilon_i=1,\varepsilon_j=0\); an arc to an unmatched cell is active
when \(\varepsilon_i=1\). Under fair bits these events have probabilities
\(1/4\) and \(1/2\), respectively. Conditional expectation therefore gives
one deterministic dependent assignment with at least \(|A_\rho|/4\) active
arcs.

### 1.3 Every active arc is a distinct loopless commutator seam

Let \(\alpha\) apply \(\tau_i\) on a selected packet cell and the identity on
an unselected cell. Pulling the prepared factor back to its parent row labels,
the fresh relation is generated on roots by

\[
 \theta=\alpha\rho\alpha.                             \tag{1.5}
\]

For an active arc \(X\to X'=\rho X\), with \(X\in Q_i\), put
\(Y=\tau_iX\). Then

\[
 \alpha Y=X,\qquad \alpha X'=X',\qquad \theta Y=X'.  \tag{1.6}
\]

The roots \(Y,X'\) lie in distinct cells and have distinct owners. Moreover,

\[
 \theta Y=\rho X\ne\rho Y,                            \tag{1.7}
\]

so this is a genuine piecewise-commutator seam, not merely a coarse cell edge.
The involution \(\alpha\) bijects old unoriented \(\rho\)-orbits with fresh
unoriented \(\theta\)-orbits, and a bit-one--to--bit-zero orbit has only one
active orientation. Thus distinct active arcs yield distinct fresh edges.
Equations (1.4)--(1.7) prove (0.1).

In a transposition overlay a row has loopless owner degree at most

\[
 2\min(d,m-1)\le n-3.
\]

Each seam supplies two distinct incidences, so
\(2s_m\le(n-3)|Z_m|\), proving (0.2). For every \(L\), either a mixed fresh
component contains more than \(L\) rows or there are at least
\(\lceil |Z_m|/L\rceil\) such components.

## 2. Proof of the exact dependent multidepth signing theorem

Fix the fresh component set \(\mathscr C\). Giving component \(C\) a sign
\(\varepsilon_C\in\{-1,+1\}\) gives pair loads

\[
 \mu_q^\varepsilon(S)=\frac{\ell_p+D_p(\varepsilon)}2,
 \qquad
 \mu_q^\varepsilon(\rho S)=\frac{\ell_p-D_p(\varepsilon)}2,
 \tag{2.1}
\]

where

\[
 D_p(\varepsilon)=\sum_C\varepsilon_Cz_{pC}.          \tag{2.2}
\]

Under unit leakage,

\[
 \ell_p\equiv\sum_Cz_{pC}\pmod2.                    \tag{2.3}
\]

Let \(Z'\) be the matrix after the simultaneous joint deletion
\(\mathcal R\), and put \(s=Z'\mathbf1\). Consider

\[
 P=\left\{x\in[0,1]^{\mathscr C}:
 \left\lfloor\frac{s_p}{2}\right\rfloor
 \le (Z'x)_p\le
 \left\lceil\frac{s_p}{2}\right\rceil
 \text{ for every retained }p\right\}.               \tag{2.4}
\]

The half-vector belongs to \(P\). Since \(Z'\) is TU, the constraint matrix
obtained by stacking \(Z',-Z',I,-I\) is TU. With integral right sides, the
nonempty bounded polytope \(P\) has an integral vertex. Choose
\(x\in\{0,1\}^{\mathscr C}\) there and set
\(\varepsilon=\mathbf1-2x\). Then every retained row has

\[
 D_p=0\quad(\ell_p\text{ even}),
 \qquad
 |D_p|=1\quad(\ell_p\text{ odd}).                    \tag{2.5}
\]

Together with the permitted pair totals, (2.1) gives respectively

\[
 (c_q,c_q),\qquad
 \{c_q,c_q+1\},\qquad
 (c_q+1,c_q+1).                                       \tag{2.6}
\]

For a deleted pair, the half-\(\ell^1\) distance to a same-total quota pair is
at most \(c_q+1\). Choose such a same-total quota on every deleted pair. Along
with (2.6) and the fixed-target quotas, these quotas have total \(W\), so
exactly \(\rho_q\) of them are ceilings; there is no hidden quota remainder.
Summing the deleted-pair errors proves (0.3). Choosing a spanning
forest and deleting the constraint endpoint of each nonforest edge gives the
valid sufficient estimate \(|\mathcal R|\le\beta\), where \(\beta\) is the
cyclomatic excess of the joint incidence graph. This forest estimate is not
necessary for TU and cannot handle a linear row supply on only \(B\) columns;
a genuinely nonforest TU matrix can.

The last assertion has an exact count. If a forest incidence graph contains
\(C\) constraint rows of width at least two and \(t\) nonempty component
columns, then

\[
 2C\le |E|\le C+t-1,
 \qquad\text{hence}\qquad C\le t-1\le B-1.           \tag{2.7}
\]

If the original instance has at least \(\delta W\) constraint rows of width at
least two and deleting \(R\) rows leaves a forest, then
\(R\ge\delta W-B=(\delta-o(1))W\). Thus the forest corollary cannot be the
one-round Gaussian solution for a linear supply of nontrivial rows; the full
TU alternative is materially stronger because a TU matrix may have
\(\Theta(W)\) rows on \(B\) columns.

For width-two rows meeting columns \(C,D\), define

\[
 r_p=-z_{pC}z_{pD}.
\]

Parity-optimality is \(\varepsilon_C\varepsilon_D=r_p\). Hence all rows are
simultaneously soluble exactly when \(\prod_{p\in\gamma}r_p=1\) on every
cycle. A violating cycle has a square minor of determinant \(\pm2\); a
consistent signed graph can be switched to an oriented incidence matrix and
is TU. This is the exact signed-holonomy interpretation. In particular,
bounded incidence degree, without cycle-sign control, is insufficient.

## 3. Proof of the two congestion ceilings

### 3.1 Universal packet atoms

Each packet root set \(U_t\) has \(2n\) roots. Double counting
\((t,X)\) with \(X\in U_t\) gives

\[
 2nM\le\Delta W=\Delta nB,
\]

which is (0.4)'s first inequality. One universal packet has exactly two
positive first-shadow cells, so it fills at most two old holes. Its exact
half-\(\ell^1\) action is \(2\) at \(q=1\) and \(4\) for \(2\le q\le H\).
The quota distance is half-\(\ell^1\)-Lipschitz, whence one move changes
\(J_A\) by at most

\[
 \frac2{c_1}+4\sum_{q=2}^{H}\frac1{c_q}=4S_A-2,
\]

because \(c_1=1\) for \(m\ge3\). Telescoping proves (0.4)--(0.7). This is
pathwise and allows arbitrary dependence, overlap, reuse, and fresh
recomputation of the packet atoms.

### 3.2 Arbitrary freshly recomputed components

For one row \(C\), let \(w_{C,r}\) be its cyclic rank-\(r\) interval
indicator. If the bridge letters have shorter distance \(d\), then

\[
 \|\tau w_{C,r}-w_{C,r}\|_1
 =4\min(r,d)-4\mathbf1_{\{r=d\}}.                    \tag{3.1}
\]

Indeed, \(2\min(r,d)\) old intervals separate the letters; exactly when
\(r=d\), two of them are interchanged within the old interval family and
cancel. Half of (3.1) is (0.8). Sum (3.1) over the rows of every switched
component, use the triangle inequality and the quota Lipschitz bound, and
then telescope. This proves (0.9)--(0.10).

If \(U_t(C)\) is the current row's \(n\)-root middle block, double counting
the weighted incidences gives

\[
 n\sum_{t,C}d_t(C)
 =\sum_X\sum_{t,C:\,X\in U_t(C)}d_t(C)
 \le\Gamma_dW,
\]

so \(\sum d_t(C)\le\Gamma_dB\). Since
\(\lambda_r(d)\le2d\), equations (0.11)--(0.12) follow. Thus the surviving
large-component route has an explicit cost: it must combine low owner
congestion with macroscopic cyclic separation, rather than merely having many
rows in a component.

## 4. Proof of the palette-width obstruction

### 4.1 The native private pile

Fix \(q\) and put \(d=m-q-2\). For
\(V\in\mathcal D_d\), the audited private pair for
\(\tau_0=(2\ 3)\) is

\[
 p_V=\{S_V,\tau_0S_V\},
 \qquad
 S_V=\{2,n\}\cup(4+2q+\operatorname{Down}(V)).       \tag{4.1}
\]

The pairs are distinct and the canonical intrinsic cell has

\[
 \mu_q(S_V)+\mu_q(\tau_0S_V)\ge\operatorname{Cat}_q. \tag{4.2}
\]

The shifted down-step coordinates lie in a native-pair-invariant block

\[
 I_q=\{2q+4,\ldots,2m\},\qquad |I_q|=2d+1.           \tag{4.3}
\]

Hence the native group orbit of all private pairs lies in

\[
 \{\{\epsilon,n\}\cup D:
 \epsilon\in\{2,3\},\ D\in\tbinom{I_q}{d}\},
\]

which has size

\[
 2\binom{2d+1}{d}=(4d+2)\operatorname{Cat}_d.        \tag{4.4}
\]

Summing (4.2) over \(V\) gives the mass (0.14).

Every complete-component switch with bridge \(\tau\) changes the rank load
by \((\tau-I)a\). Total load on a target union invariant under \(\tau\) is
therefore exactly unchanged, component by component, even when components and
signs are chosen adaptively.

### 4.2 Adding \(k\) nonnative colours enlarges the orbit by at most \(6^k\)

The coordinate graph of \(\mathcal T_m\) has initial blocks \(B_i\) of sizes
\(b_i\in\{1,2\}\). Consider one final coordinate component formed by joining
\(p\) initial blocks. For a target profile with
\(t_i=|S\cap B_i|\), put \(b=\sum_i b_i\) and \(t=\sum_i t_i\). Its native
orbit has size

\[
 \prod_i\binom{b_i}{t_i},
\]

while the transpositions of the connected final coordinate graph generate
\(\operatorname{Sym}(b)\), so its enlarged orbit has size \(\binom bt\). The
expansion ratio is therefore

\[
 R=\frac{\binom bt}{\prod_i\binom{b_i}{t_i}}
 \le6^{p-1}.                                           \tag{4.4a}
\]

For \(p=1\), the ratio is one. For \(p\ge2\), the denominator is at least one,
\(b\le2p\), and

\[
 \binom bt\le\binom{2p}{p}\le6^{p-1}.
\]

The last inequality starts with \(\binom42=6\); each successive central
binomial ratio is \(2(2p+1)/(p+1)<4<6\). If the final components contain
\(p_j\) initial blocks, they require at least \(p_j-1\) of the new edges, so
\(\sum_j(p_j-1)\le k\). Multiplying (4.4a) gives expansion at most \(6^k\)
for each native orbit. Applying this orbit by orbit to the native-invariant
union proves (0.13); overlap of enlarged orbits only lowers the union size.
The constant is sharp for this block argument: one edge joining two size-two
blocks with profile counts \(0,2\) expands one state to all six two-subsets.
Componentwise orbit-mass invariance preserves (0.14).

### 4.3 Exact floors

An integral quota vector places at most

\[
 c_qL+\min(L,\rho_q)
\]

mass on any \(L\)-element target union. Equal total mass forces an equal
deficit outside, proving (0.15).

For the factorial floor, use the exact identity

\[
 2\Phi_q=\sum_S
 (\mu_q(S)-c_q)(\mu_q(S)-c_q-1).                     \tag{4.5}
\]

Every summand is nonnegative on integer loads. For \(1\le L\le N_q\), among
\(L\) bins carrying total mass at least \(M\), with
\(a=\lfloor M/L\rfloor\ge c_q+1\), discrete convexity minimizes (4.5) at
\(L-s\) entries \(a\) and \(s\) entries \(a+1\). This is (0.16).

If

\[
 x=\frac{\operatorname{Cat}_q}{(4d+2)6^k}
 \ge4(c_q+1),
\]

then the truncation in (0.13) is inactive, because
\(6^k(4d+2)\operatorname{Cat}_d=M_q/x
\le W/[4(c_q+1)]<N_q\). Moreover \(u\ge3x/4\),
\(u-1\ge x/2\), and for \(d\ge1\)

\[
 \Phi_q\ge
 \frac{\operatorname{Cat}_d\operatorname{Cat}_q^2}
 {32d\,6^k}.                                         \tag{4.6}
\]

At \(q=H\), use

\[
 \operatorname{Cat}_H\ge\frac{4^H}{4H^2},
 \qquad
 \operatorname{Cat}_{m-H-2}>
 \frac{B}{4^{H+2}}
\]

to obtain (0.17). Since
\[
 \frac{4^H}{6^k}
 =\exp(H\log4-k\log6),
\]

so (0.18)--(0.19) follow. The sharper
asymptotic coefficient

\[
 \frac{\Phi_H}{W}
 \ge(1-o(1))
 \frac{4^H}{256\pi m^2H^3\,6^k}
\]

is valid whenever \(x_{H,k}\to\infty\), including every regime in (0.18).

If a single co-moving preparation compares \(\mathcal T_m\) with
\(g\mathcal T_mg^{-1}\) and \(g\) has coordinate support \(s\), only native
pairs incident with that support can change, so at most \(s\) new palette
colours are introduced. In that one common frame, release of the certified
factorial floor requires

\[
 s\ge\frac{\log4}{\log6}H-O(\log m).
\]

This corollary does not cover repeated arbitrary re-framing: a global
relabelling moves the invariant target union itself, and the proof must be
restarted in the transported frame.

## 5. Exact proved/conditional boundary

The following advance is unconditional.

* A congestion-one dependent packet preparation creates
  \((11/288-o(1))W\) genuine nonnative commutator seams and puts
  \((11/144-o(1))B\) rows in fresh mixed components.
* Any subsequent choice of whole fresh component sides remains an integral
  exact wreath factor and therefore has literal contiguous-OR linearization.
* Bounded-congestion packet reuse cannot itself change the required
  multidepth ledger by order \(W\).
* Even arbitrary fresh large components must pay the owner--distance capacity
  (0.11).
* For every fixed \(\varepsilon>0\), a fixed native palette plus at most
  \((\log4/\log6-\varepsilon)H\) new bridge colours retains divergent Gaussian
  factorial excess. More generally the certified release threshold is
  \(k\ge(\log4/\log6)H-O(\log m)\).

The following is an exact sufficient theorem, but its canonical hypotheses are
not yet proved.

> One fresh overlay with floor-compatible pair totals, unit leakage, and an
> all-depth leakage matrix made TU by deleting \(o(W)\) target-pair rows admits
> one common integral signing with \(J_A=o(W)\).

The remaining geometric gate is therefore narrower than the former
"find many seams" request. One must prove that the seams in (0.1) leak
nonlocally into \(\Theta(W)\) lower- and upper-rank target pairs and make the
resulting joint leakage matrix TU after deleting \(o(W)\) rows, or establish
another equally strong dependent discrepancy theorem. In the width-two
specialization, this is exactly an \(o(W)\) signed-cycle-frustration condition.
Separately, any route which aims to eliminate the certified private-pile
factorial floor while staying in one fixed palette frame must introduce at
least \((\log4/\log6)H-O(\log m)\) genuinely new bridge colours. That
palette-width condition is not proved necessary for balanced overflow or for
the coefficient-one theorem.

There is a concrete reason the middle seams do not already give this. For a
fixed \(\rho=(a\ b)\), at most \(4B\) owner incidences are directly aligned
with the first-shadow core of their middle-root edge: \(a\) or \(b\) must be
one of two boundary labels in its row. Therefore all but \(o(W)\) of the seam
supply needs genuinely nonlocal component containment before it becomes a
useful lower-shadow NAE constraint.

No theorem here proves \(J_A=o(W)\) for the canonical factor, proves the
coefficient-one bound, or obstructs it. The palette theorem is deliberately
limited to factorial collision: its corresponding linear overflow floor is
sublinear. This is the precise proved/conditional boundary.

## 6. Independent audit

The new package was audited independently in three directions.

1. The seam audit rederived the inverse-step-two distances \(m,m-1\), the
   support \(2n-4\), the external degree \(m^2-3m-1\), deletion of native
   colours, the pinned factor \(1/4\), injectivity of active arcs, the
   \(n-3\) loopless degree, and both constants \(11/288\) and \(11/144\).
2. The signing audit checked the parity identity, TU polytope integrality,
   negative and positive odd row sums, the single simultaneous all-depth
   deletion quantifier, exact quota remainders, the deleted-pair
   \(c_q+1\) bound, and the width-two signed-cycle criterion.
3. The obstruction audit checked the row-distance cancellation at \(r=d\),
   all factors of two in the congestion ledger, the sharp \(6^k\) orbit
   expansion, the exact quota and factorial floors, and the
   \((\log4/\log6)H-O(\log m)\) threshold.
   It imposed the necessary guards \(d\ge1\) in (4.6) and
   \(x_{H,k}\to\infty\) for the sharper asymptotic coefficient.

Full component proofs and auxiliary variants are also recorded in:

* `MATH_ATTACK_K7_DEPENDENT_COMMUTATOR_NAE_20260725.md`;
* `MATH_ATTACK_K7_BOUNDED_PACKET_LINEAGE_CEILING_20260725.md`;
* `MATH_ATTACK_K7_DEPENDENT_PACKET_ORBIT_OBSTRUCTION_20260725.md`.
