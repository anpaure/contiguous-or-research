# Three-chart coercivity audit: exact kernels, floor plateaux, and the PBBS boundary

Date: 2026-07-25

Method: pure mathematics only. No computation, search, solver, or
long-running job is used.

## 0. Verdict

Put

\[
 n=2m+1,\qquad W=\binom nm,\qquad
 B=\operatorname{Cat}_m=\frac Wn,\qquad
 H=\lceil A\sqrt m\rceil,
\]

where \(A>0\) is fixed. Then

\[
 HB=\left(\frac A2+o_A(1)\right)\frac W{\sqrt m},
 \qquad
 \frac WH=\left(\frac1A+o_A(1)\right)\frac W{\sqrt m}.
\tag{0.1}
\]

The audit gives four exact conclusions.

1. The PBBS adjacent-pair interval families are simultaneously legal for
   all adjacent blocks. Their target graphs are directed paths, and their
   exact doubled floor drop on one path is

   \[
   \mathscr D_{\rm path}
   =2\sum_i\ell_i(d_i-\ell_i)
    +2\sum_i\ell_i\ell_{i+1}.
   \tag{0.2}
   \]

   Its zero set consists exactly of complete swaps on a matching of
   nonadjacent positive-capacity edges.

2. At a current endpoint, the exact stacked owner-fixed spike marginal is

   \[
   a_e=2\sum_p w_p
   \bigl(x_p(v_{e,p})-x_p(u_{e,p})+1\bigr).
   \tag{0.3}
   \]

   In one source phase all spike cross-Grams are nonnegative. Hence no
   spike subset descends if and only if \(a_e\ge0\) for every admissible
   occurrence arc. The exact one-round interval-then-spike null set is
   obtained by imposing these inequalities at every zero-drop interval
   endpoint.

3. This floor-corrected null set is not \(o(W)\)-dimensional as a family of
   formal projected current states. Already in the rank-two projection it
   contains an affine Boolean family whose affine span has dimension
   \(R=\Theta(W)\). Its terminal point
   has

   \[
   Q_2=2R=\Theta(W),\qquad
   \mathscr D_{{\rm int},2}=0,
   \qquad
   \sup_F\bigl[Q_2(x)-Q_2(x+z_F)\bigr]=0,
   \tag{0.4}
   \]

   and therefore \(Q_2/(HB)=\Theta_A(\sqrt m)\). This is a canonical
   diffuse floor wall, not a high-multiplicity defect.

4. Conclusion 3 is an exact projected obstruction, not a physical
   full-\(H\) PBBS counterexample. The missing lift has two genuine pieces:
   nested higher-rank spike shields and one canonical PBBS row chronology.
   Conversely, the PBBS \(q=1\) seed makes the first rank cheap, and a
   joint choice of the leftover coordinate and the ordered pair matching
   makes one coordinate-subtotal wall Catalan-cheap. Neither fact controls
   arbitrary predecessor components.

Thus the proposed three-chart coercivity theorem is false as a consequence
of the chart algebra and floor arithmetic alone. The theorem restricted to
actual low-run PBBS-reachable states remains open. Its exact missing
statement is the diffuse-plateau exclusion in Section 8 below. No
constant-one conclusion follows.

## 1. Two different meanings of “nullspace”

These must be separated.

At signed depth \(q\), let \(\Omega_q\) be the target layer. If

\[
 T_q=c_q|\Omega_q|+s_q,
 \qquad 0\le s_q<|\Omega_q|,
\]

the doubled factorial-floor excess is

\[
 Q_q(x)=\sum_{Z\in\Omega_q}
       (x_Z-c_q)(x_Z-c_q-1).
\tag{1.1}
\]

On a fixed-mass fibre, \(Q_q(x)-\sum_Zx_Z^2\) is constant. Thus every
energy-difference calculation with squared loads is exactly
floor-corrected.

For fixed nonnegative signed-rank weights, write

\[
 Q_H(x)=\sum_{\sigma\in\{+,-\}}
        \sum_{q=1}^H w_q^\sigma Q_q^\sigma(x).
\tag{1.2}
\]

There are nevertheless two different null objects.

* The **linear incidence kernel** is the orthogonal complement of the
  span of the chart columns. It is a vector space.
* The **current-endpoint zero-descent set** consists of integral load
  profiles from which no permitted chart corner decreases (1.1). Because
  the one-edge marginal contains the affine \(+1\) in (0.3), this is a
  cone, or after fixing the mass a finite union of polyhedra; it need not
  be a vector space.

The canonical wall in Section 6 belongs to the second object even though
its overload-to-floor spike directions are visible to the linear
incidence form. Calling the two objects one “quadratic nullspace” hides
the endpoint-orientation obstruction.

## 2. The formal linear kernel and its exact component floor

Fix one signed rank \(q\). Form a graph \(\mathcal G_q\) on
\(\Omega_q\) by granting separately every projected atomic target move
which underlies either an interval packet or an owner-fixed spike. This
is an optimistic relaxation: an actual packet is a sum of occurrence
columns, and one stacked spike can change several ranks at once.

### Theorem 2.1 (component kernel)

If \(C\) ranges over the connected components of \(\mathcal G_q\), then

\[
 \operatorname{span}\{\mathbf e_Y-\mathbf e_X:XY\in E(\mathcal G_q)\}
 =\left\{z:\sum_{X\in C}z_X=0\text{ for every }C\right\},
\tag{2.1}
\]

and hence

\[
 \ker \mathcal B_q
 =\operatorname{span}\{\mathbf1_C:C\in\operatorname{Comp}(\mathcal G_q)\}
\tag{2.2}
\]

for every incidence quadratic form

\[
 \mathcal B_q(f)=\sum_{XY\in E(\mathcal G_q)}
 \lambda_{XY}(f_Y-f_X)^2,
 \qquad \lambda_{XY}>0.
\]

The actual packetized, stacked catalog can have a larger kernel, never a
smaller one.

#### Proof

Every edge incidence has sum zero on each component. Conversely, in a
connected component choose a spanning tree and a root \(X_0\). The tree
incidences generate every vector
\(\mathbf e_X-\mathbf e_{X_0}\), and these vectors span the component's
zero-sum subspace. Components have disjoint supports, proving (2.1).
Orthogonal complementation proves (2.2). Granting projected atomic edges
enlarges the physical span, so it can only shrink its orthogonal kernel.
\(\square\)

There is also an exact arithmetic floor retained by these component
totals. If a component has size \(N_C\) and invariant mass

\[
 M_C=N_Ca_C+r_C,\qquad 0\le r_C<N_C,
\]

then discrete convexity puts loads \(a_C+1\) on \(r_C\) vertices and
\(a_C\) on all remaining vertices. Substitution into (1.1) gives

\[
 \boxed{
 Q_{q,C}^{\min}
 =2\left[N_C\binom{a_C}{2}+r_Ca_C\right]
  -2c_qM_C+c_q(c_q+1)N_C.}
\tag{2.3}
\]

Therefore

\[
 \mathfrak F_q(x)=\sum_CQ_{q,C}^{\min}
\tag{2.4}
\]

is the exact residual floor for the formal unrestricted signed edge
transport. A physical chart sequence may retain more energy because its
edges are packetized, directed at the current endpoint, and coupled across
ranks.

There is a further audit point. Formula (2.2) is exact rank by rank for
the optimistic projected graph; it is not automatically an equality for
the actual stacked physical form. If \(\mathscr D_H\) is the catalog of
actual stacked packet and spike columns and

\[
 \mathcal B_H^{\rm stack}(f)
 =\sum_{d\in\mathscr D_H}\lambda_d
   |\langle f,d\rangle_w|^2,
 \qquad\lambda_d>0,
\]

then its exact linear kernel is

\[
 \boxed{
 \ker\mathcal B_H^{\rm stack}
 =\bigcap_{d\in\mathscr D_H}d^\perp.}
\tag{2.5a}
\]

The direct sum of the component-indicator spaces in (2.2) is contained
in (2.5a), because every rank projection of every actual column has zero
sum on each projected component. Equality would require independent
physical realization of the rank projections; no such triangularization
has been proved. The exact useful structural description for the actual
current menu is therefore the nonlinear criterion (5.1), not an
unproved direct-sum assertion.

The kernel can genuinely be linear-dimensional under central legality
alone. For every \(q\ge3\), one can choose a legal lower token system for
which all targets containing a fixed two-set \(D\) are isolated in the
owner-spike predecessor graph. Their number is

\[
 \binom{n-2}{m-q-2}
 =\frac{(m-q)(m-q-1)}{n(n-1)}\binom n{m-q}
 =\Theta_A(W)
\tag{2.5}
\]

uniformly for \(q\le A\sqrt m\). Indeed, for every central root
\(R\supset D\), choose its depth-\(q\) target inside \(R\setminus D\).
Every projected lower spike is a Johnson edge inside \(R\); it cannot
reach a target containing both points of \(D\), which is at Johnson
distance at least two from the chosen target. The long upper interval
charts fix all lower flags. This proves (2.5) with the same chart
quantifiers. Such systems need not have PBBS low-run chronology.

## 3. Exact all-adjacent interval form

For the recursively conjugate PBBS phases, a nonfixed category-\(j\)
target \(U\) is sent by the adjacent exchange to a category-\(j+1\)
target \(V\). Each target has at most one incoming and at most one
outgoing adjacent edge, and category strictly increases. Thus every
target component is a directed path.

The full owner audit permits all adjacent blocks simultaneously. The only
case not contained in the disjoint parity-layer theorem is a candidate
from block \(j\) meeting one from block \(j+1\). If their owners coincide,
the common owner avoids both exchanged pairs. Conjugacy and injectivity
then identify their lower roots, contradicting the disjoint candidate
conditions. Hence no new ownership collision occurs.

Fix one path, label its vertices \(0,1,\ldots,s\), and write its current
loads as

\[
 x_0\ge x_1\ge\cdots\ge x_s,
 \qquad d_i=x_i-x_{i+1}.
\tag{3.1}
\]

The coherent adjacent swap moves exactly \(d_i\) occurrences across edge
\(i\). If a packet corner moves \(0\le\ell_i\le d_i\), then, with
\(\ell_{-1}=\ell_s=0\),

\[
 y_i=x_i+\ell_{i-1}-\ell_i.
\]

Direct expansion gives

\[
 \begin{aligned}
 \|y\|_2^2-\|x\|_2^2
 &=-2\sum_i d_i\ell_i
   +\sum_{i=0}^s(\ell_{i-1}-\ell_i)^2\\
 &=-2\sum_i\ell_i(d_i-\ell_i)
   -2\sum_i\ell_i\ell_{i+1}.
 \end{aligned}
\tag{3.2}
\]

Mass is fixed, so (3.2) is also the exact change of (1.1). This proves
(0.2). Every summand is nonnegative, and therefore

\[
 \mathscr D_{\rm path}=0
 \quad\Longleftrightarrow\quad
 \ell_i\in\{0,d_i\}\ \text{for every }i,
 \quad \ell_i\ell_{i+1}=0\ \text{for every }i.
\tag{3.3}
\]

There is a useful packetwise restatement. No corner of the complete
adjacent interval cube descends exactly when, on every path,

1. every positive-capacity edge is carried by a single physical packet;
2. the positive-capacity edges form a matching.

If one edge contains two nonempty packets, selecting exactly one gives
\(0<\ell_i<d_i\) and a strict first term in (0.2). If two consecutive
positive edges exist, selecting both complete packets gives a strict
second term. Conversely the two conditions force (3.3) for every corner.

Under the PBBS residence hypothesis

\[
 \rho_H=o\!\left(
 \frac{\binom{2m-1}{m-1}}{H\log m}
 \right),
\tag{3.4}
\]

the physical all-adjacent packet count satisfies

\[
 r_{\rm all}=o(W/H),\qquad
 \Delta J\le2r_{\rm all}=o(W/H).
\tag{3.5}
\]

All lower flags are fixed by these charts.

## 4. Exact current-endpoint spike form

Consider owner-fixed spike occurrences in one actual source phase. At a
changed rank \(p\), occurrence \(e\) moves one unit from \(u_{e,p}\) to
\(v_{e,p}\), so its column is

\[
 d_{e,p}=\mathbf e_{v_{e,p}}-\mathbf e_{u_{e,p}}.
\]

The old targets avoid the omitted source pair and the image targets meet
it. Hence old/image cross equalities are impossible. For distinct
occurrences \(e,f\),

\[
 \langle d_e,d_f\rangle_w
 =\sum_p w_p\left(
 \mathbf1_{u_{e,p}=u_{f,p}}+
 \mathbf1_{v_{e,p}=v_{f,p}}
 \right)\ge0.
\tag{4.1}
\]

For a selected set \(F\), fixed-mass expansion of (1.1) gives exactly

\[
 Q(x+\textstyle\sum_{e\in F}d_e)-Q(x)
 =\sum_{e\in F}a_e
  +2\sum_{\{e,f\}\subset F}\langle d_e,d_f\rangle_w,
\tag{4.2}
\]

where \(a_e\) is (0.3). It follows immediately that

\[
 \boxed{
 \text{no owner-fixed spike subset descends}
 \Longleftrightarrow a_e\ge0
 \text{ for every admissible occurrence arc }e.}
\tag{4.3}
\]

Within this cone, a chosen set is flat exactly when every selected
\(a_e=0\) and all its distinct selected columns are pairwise orthogonal.
The lower owner-fixed spike has the identical law in the lower signed
summand.

If a common Bernoulli bias \(s\in[0,1]\) is applied to a selected family,
put

\[
 D=\sum_{e,p}w_p
 \bigl(x_p(u_{e,p})-1-x_p(v_{e,p})\bigr),
 \qquad
 G=2\sum_{e<f}\langle d_e,d_f\rangle_w.
\]

Then

\[
 \mathbb E_sQ-Q=s^2G-2sD,
\tag{4.4}
\]

and the optimal guaranteed descent is

\[
 \Psi(D,G)=
 \begin{cases}
 0,&D\le0,\\
 D^2/G,&0<D<G,\\
 2D-G,&D\ge G>0,\\
 2D,&G=0<D.
 \end{cases}
\tag{4.5}
\]

This is a current-endpoint statement; positive cross-Gram alone does not
orient the descent.

## 5. Exact one-round combined null set

Let \(\mathscr O_{\rm int}(M)\) be the set of endpoints obtained by
zero-drop interval corners satisfying (3.3). Then a current state \(M\)
admits no descent by one complete interval cube followed by one spike
step if and only if both conditions hold:

\[
 \begin{cases}
 \text{every positive interval edge is packet-monochromatic and the}\\
 \qquad\text{positive edges form a matching on every target path};\\[2mm]
 a_e(M')\ge0\quad
 \text{for every }M'\in\mathscr O_{\rm int}(M)
 \text{ and every admissible spike arc }e.
 \end{cases}
\tag{5.1}
\]

Indeed, failure of the first condition gives a strict interval corner by
Section 3. Subject to the first condition all interval corners are flat;
then failure of the second condition gives a descending singleton spike
by (4.2). If neither fails, (4.2) and the nonnegative cross-Grams show that
every subsequent spike subset is nondecreasing.

For renewed state-adaptive charts, (5.1) must be imposed on the iterated
flat-orbit closure, because the interval packets and spike arcs are rebuilt
at the new endpoint. This is the exact renewal quantifier; one-round
nullity alone does not settle it.

## 6. A canonical diffuse floor plateau

We now show that (5.1) has a linear-dimensional projected family. This is
the promised obstruction.

At upper depth two in the autonomous selected-token core,

\[
 K_2=\binom{2m+1}{m+2}
     =\binom{2m+1}{m-1}=T_2,
\]

so the exact floor is the all-one vector. Fix the first two priority pairs
\(P_1,P_2\). Choose four more coordinates, split as two pairs
\(B_1,B_2\), outside \(P_1\cup P_2\), put \(B=B_1\cup B_2\), and define

\[
 \mathcal U=
 \left\{B\cup C:
 C\in\binom{[n]\setminus(P_1\cup P_2\cup B)}{m-2}
 \right\}.
\tag{6.1}
\]

Thus

\[
 F_m=|\mathcal U|=\binom{2m-7}{m-2}
 =\left(\frac1{256}+o(1)\right)W.
\tag{6.2}
\]

The asymptotic follows from

\[
 \frac{F_m}{W}
 =\frac{m(m-1)(m+1)m(m-1)(m-2)(m-3)(m-4)}
 {(2m+1)(2m)(2m-1)(2m-2)(2m-3)(2m-4)(2m-5)(2m-6)}.
\]

Choose \(R=\lfloor F_m/2\rfloor\) pairwise distinct overload targets
\(U_1,\ldots,U_R\in\mathcal U\), and choose \(R\) further distinct holes
\(Z_1,\ldots,Z_R\) among the targets avoiding \(P_1\cup P_2\). Put

\[
 h_r=\mathbf e_{U_r}-\mathbf e_{Z_r},
 \qquad
 x^S=\mathbf1+\sum_{r\in S}h_r
 \quad(S\subseteq[R]).
\tag{6.3}
\]

The vectors \(h_r\) have disjoint supports and are linearly independent.
Thus the profiles (6.3) have affine span of dimension
\(R=\Theta(W)\). For each \(S\), equip precisely the selected overloads
with the two displayed projected occurrences below; this is a family of
projected current incidence states, not one fixed occurrence graph with
variable loads. At its terminal point \(x=x^{[R]}\), every overload has
load two, every hole load zero, and every other target load one. Its mass
is \(K_2\), and

\[
 Q_2(x)=\sum_U(x_U-1)(x_U-2)=2R
 =\left(\frac1{256}+o(1)\right)W.
\tag{6.4}
\]

Every target in (6.3) avoids \(P_1\cup P_2\). It is category one, is
fixed by the \(P_1,P_2\) exchange, has no incoming category edge, and is
not acted on by later adjacent blocks. Hence every overload and hole is
isolated from all adjacent target paths. Every remaining path vertex has
load one, so every remaining path capacity is zero. Therefore the exact
interval charge is zero.

The overloads also admit explicit projected nested occurrences. Writing
\(B_1=\{b_1,b_2\}\), \(B_2=\{b_3,b_4\}\), attach to
\(U=B\cup C\) the two chains

\[
 C\cup B_2
 \subset C\cup B_2\cup\{b_1\}
 \subset U,
\]

\[
 C\cup B_1
 \subset C\cup B_1\cup\{b_3\}
 \subset U.
\tag{6.5}
\]

Their owners and depth-one predecessors are pairwise distinct as \(C\)
varies. An owner-fixed spike at distinguished depth one or two replaces
one entering coordinate by a marker from \(P_1\). Every possible
rank-two image therefore meets \(P_1\), whereas every overload and hole
avoids \(P_1\). All these image targets have load one. Consequently an arc
out of an overload has marginal

\[
 2(x_v-x_u+1)=2(1-2+1)=0.
\]

An arc out of a load-one target has marginal \(2x_v\ge0\), and a hole
contains no occurrence. Equation (4.2) now proves that no projected spike
subset descends. Shared images only add nonnegative cross-Gram.

Finally, from (0.1) and (6.4),

\[
 \frac{Q_2(x)}{HB}
 =\left(\frac1{128A}+o_A(1)\right)\sqrt m
 \longrightarrow\infty.
\tag{6.6}
\]

This proves (0.4) and the claimed linear-dimensional diffuse plateau.

The qualification is essential: (6.5) is an exact rank-two
target/occurrence construction. It does not prove that these
\(\Theta(W)\) chains occur in the required long order in one canonical
PBBS factor, nor that the same occurrences have nonnegative stacked
marginals at ranks \(3,\ldots,H\). Grouping their labels into
\(O(W/m)=o(W/H)\) abstract packets is only packet-incidence bookkeeping,
not a physical PBBS realization.

## 7. What PBBS already removes

The PBBS (q=1) seed has upper defect

\[
 Q_1^+=O(W\log m/m)=o(HB),
\tag{7.1}
\]

and exact lower saturation. The interval theorem never increases this
defect. Thus the first rank is inside the Catalan reservoir and contributes
no missing coercive direction.

There is also one deeper PBBS-specific gain. Put

\[
 A_0=\binom{2m-1}{m-1},
 \qquad B=\frac{2A_0}{m+1}.
\]

For a uniformly chosen leftover coordinate \(\star\) and a uniformly
ordered perfect matching of the other (2m-2) local coordinates, consider
a base start containing \(\star\). Conditional on (k) earlier pairs
meeting that start, the next pair lies wholly in its (m)-point
complement with probability at least

\[
 \frac{\binom{m-k}{2}}{\binom{2m-2-2k}{2}}
 =\frac{m-k}{2(2m-2k-3)}>\frac14.
\tag{7.2}
\]

Hence its retained-phase multiplicity has expectation at most four.
Summing the exact (H-1) deleted coordinates of each depth-(H) flag and
then averaging over \(\star\) gives

\[
 \mathbb E D^{\rm prin}_{H,\star}
 \le\frac{4(H-1)A_0}{2m-1}.
\tag{7.3}
\]

The same random matching satisfies

\[
 \mathbb E\sum_{j\le\ell_0}F_j
 \le\frac{A_0\ell_0(\ell_0+1)}{m-1},
 \qquad \ell_0=\lceil20\log m\rceil.
\tag{7.4}
\]

Normalize (7.3) and (7.4) by twice their respective right sides. The
expected normalized sum is at most one, so one joint choice obeys

\[
 D^{\rm prin}_{H,\star}
 \le\frac{8HA_0}{2m-1}
 =(2+o(1))HB,
\tag{7.5}
\]

and

\[
 \sum_{j\le\ell_0}F_j
 \le\frac{2A_0\ell_0(\ell_0+1)}{m-1}
 =O(W\log^2m/m).
\tag{7.6}
\]

For the autonomous completed (W)-token PBBS ledger, the q1-color and
arithmetic-completion exceptional count is
(O(W\log m/m)=o(HB)). Therefore, for every (q\le H),

\[
 \left|M_{q,\star}-\frac{m-q}{n}W\right|=O_A(HB).
\tag{7.7}
\]

Balancing loads separately on the two sides of the \(\star\)-cut and
moving the required (O_A(HB)) units across the cut costs at most four
per unit in the doubled floor polynomial. Thus the rank-(q) floor with
this one subtotal prescribed is (O_A(HB)).

This controls exactly one linear functional, not the component masses in
(2.3). Owner-fixed spikes can cross the \(\star\)-cut, and actual
predecessor components may refine both sides. Also, extra collar-induced
literal windows presently have only an (o(W)) count; an
(O_A(HB)) discrepancy bound for that collar ledger is not yet proved.
Thus (7.7) must not be promoted to a full physical component-floor
theorem.

## 8. Exact surviving PBBS theorem

For a current physical PBBS endpoint (M), let

\[
 \mathfrak C(M)=
 \sup_{I,\mathscr S}
 \left[\mathscr D_{\rm int}(I)
       +\Psi(D_{I,\mathscr S},G_{I,\mathscr S})\right],
\tag{8.1}
\]

where (I) is a legal all-adjacent interval corner, the spike family is
chosen after recomputing the current endpoint (M_I), and the total new
run cost is (o(W/H)). Sections 3 and 4 prove the exact endpoint bound

\[
 Q_H(M')\le Q_H(M)-\mathfrak C(M)
\tag{8.2}
\]

for some literal corner (M'). They do not prove coercivity of
\(\mathfrak C\).

The missing positive theorem can now be stated without hiding a kernel:
there must be constants \(\gamma_A>0\), (C_A<\infty) such that every
PBBS-reachable current state with the required low-run ledger satisfies

\[
 \boxed{
 \mathfrak C(M)\ge
 \gamma_A\bigl(Q_H(M)-C_AHB\bigr).}
\tag{8.3}
\]

Equivalently, every state in the iterated version of the exact null set
(5.1) must have

\[
 Q_H(M)=O_A(HB).
\tag{8.4}
\]

On the lower side, (8.4) requires both the weighted component-floor bound

\[
 \sum_{q\le H}w_q^-\mathfrak F_q(M)=O_A(HB)
\tag{8.5}
\]

and an endpoint-oriented frame on the component-mean-zero complement.
On the upper side it requires exclusion or fusion of the diffuse
load-two/floor-image shields of Section 6 throughout their renewed flat
orbit.

The rank-two construction proves that (8.3) cannot follow from the three
chart identities, central saturation, and owner injectivity alone. The
PBBS estimate (7.7) proves that the simplest one-coordinate version of
the obstruction is cheap in the autonomous seed. Neither result decides
(8.3) for actual low-run PBBS-reachable states. This is the precise
proved/conditional boundary.
