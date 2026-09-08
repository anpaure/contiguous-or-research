# Top-strip first moment and noncascading quarantine: exact boundary

Date: 2026-07-27

Scope: constant-one repaired promotion-ring slow-greedy hierarchy.

## 0. Verdict

Let

\[
 L=C_1(\log m)^2,\qquad
 \rho_*=\left\lfloor{L-2\over4}\right\rfloor+1,\qquad
 z=m^{-1/20},
\]

and put

\[
 \alpha={CL^4\over m^2z^2}=m^{-19/10+o(1)}.
\tag{0.1}
\]

The numerical top-strip argument is valid:

\[
 \sum_{\rho=\rho_*}^{L}
 \exp[O(\rho\log(\rho+1))]\alpha^{\rho/4}
 =
 \exp[-\Omega((\log m)^3)].
\tag{0.2}
\]

Consequently an incidence-normalized stopped first-moment theorem at
scale \(O(\alpha^\rho)\) would give a soft quarantine whose terminal
matching cost is \(o(N_H)\) roots and \(o(W)\) owners. The soft
quarantine is genuinely noncascading: no catalogue edge is suppressed
during the stochastic trajectory.

That stopped first-moment theorem has not been proved. The exact missing
term is a common future event joining the already exposed prefix to the
last physical row. Neither the one-row \(q=1\) identity nor the static
mixed-diagram theorem bounds this term relative to the current depleted
reference.

In particular, the unconditional closure asserted in
MATH_THEOREM_AGGREGATE_FIRST_MOMENT_TOP_STRIP_QUARANTINE_20260727.md
does not follow from its stated inputs. Its ordered pair-column tower
has three gaps:

1. equal formal rows must be normalized by physical survivor blocks;
2. a future event meeting two protected columns has positive normalized
   drift and cannot be discarded as terminal; and
3. the static row-exploration initializer is certified only to finite
   physical excess, not for the asserted infinite tower.

This note proves the exact hazard identity, the conditional additive
closure, the complete \(\alpha^\rho\) quarantine arithmetic, and a
noncascading terminal-discard theorem. It also gives an ordinary-frame
edge-deleted pair-star and an abstract hard-quarantine cascade showing
why the missing dynamic input cannot be replaced by a blanket
deletion-hereditary inference or by recursive cleaning.

The coefficient-one owner near-packing therefore remains conditional.

## 1. Exact physical-union first moment

Every active repaired edge contains one root and \(k=(1+o(1))m\)
owners; put \(K=k+1\). In the compensated process put

\[
 \Delta_t=\max_vd_t(v),\qquad
 \nu_t={1\over k\Delta_t},\qquad
 \chi_t(v)={\Delta_t-d_t(v)\over k\Delta_t}.
\tag{1.1}
\]

For a finite active resource set \(S\), write

\[
 \mathcal E_t(S)=\bigcup_{v\in S}\mathcal E_t(v),\qquad
 J_t(S)=\sum_{v\in S}d_t(v)-|\mathcal E_t(S)|.
\tag{1.2}
\]

### Lemma 1.1 (exact compensated union hazard)

The rate of an event deleting at least one resource of \(S\) is

\[
 \boxed{
 \Lambda_t(S)
 ={ |S|\over k}-\nu_tJ_t(S).}
\tag{1.3}
\]

If \(P\cap R=\varnothing\), then

\[
 \boxed{
 \Lambda_t(P\cup R)
 =\Lambda_t(P)+\Lambda_t(R)
 -\nu_t|\mathcal E_t(P)\cap\mathcal E_t(R)|.}
\tag{1.4}
\]

#### Proof

The edge clocks contribute
\(\nu_t|\mathcal E_t(S)|\), while the independent compensation clocks
contribute \(\sum_{v\in S}\chi_t(v)\). Substitution of (1.1) gives
(1.3). Moreover

\[
\begin{aligned}
 J_t(P\cup R)-J_t(P)-J_t(R)
 &=
 |\mathcal E_t(P)|+|\mathcal E_t(R)|
 -|\mathcal E_t(P\cup R)|\\
 &=|\mathcal E_t(P)\cap\mathcal E_t(R)|.
\end{aligned}
\]

Insert this identity into (1.3). \(\square\)

Now fully resolve row equalities and physical resource equalities in a
mixed diagram. Expose all but its last physical row. Let \(P_C\) be
the union of distinct prefix resources and, for a compatible last row
\(f\), put

\[
                         R_C(f)=V(f)\setminus P_C.
\tag{1.5}
\]

Terminal deletion of \(P_C\) cancels the prefix-survival derivative of
the physical-union reference. After removing the already audited
internal prefix and one-row errors, the remaining positive term is

\[
 \boxed{
 \mathsf X_C=
 \sum_{f\in\mathcal F_C}
 |\mathcal E_t(P_C)\cap\mathcal E_t(R_C(f))|.}
\tag{1.6}
\]

Equivalently,

\[
 \mathsf X_C
 \le
 \sum_{f\in\mathcal F_C}
 \sum_{p\in P_C}\sum_{y\in R_C(f)}d_t(p,y).
\tag{1.7}
\]

There is no separate physical coin term in (1.6): after equality
resolution, \(P_C\cap R_C(f)=\varnothing\), and compensation clocks are
indexed by single resources. A formal common-coin term is precisely a
resource equality which must be resolved before the physical-union
reference is differentiated.

## 2. Why the old \(q=1\) input does not compose

The one-row first-moment theorem controls the internal term
\(J_t(R_C(f))\). Formula (1.6) is different: it is a future selected
edge meeting both a protected prefix resource and a genuinely new
last-row resource. Reversing (1.7) displays one new two-incidence
column, so it raises physical excess by one.

This extra term is not a formal nicety.

### Proposition 2.1 (marginals do not imply joint first moment)

For every \(k\ge2\), there is a \(k\)-uniform compensated process in
which every single resource has hazard \(1/k\), but two distinct
resources have joint hazard \(1/k\), not \(2/k\).

#### Proof

Take one active edge

\[
                         g=\{p,q\}\cup F,\qquad |F|=k-2.
\]

Every active resource has degree one, \(\Delta=1\), and compensation
rate zero. The sole edge rings at rate \(1/k\). Hence

\[
 \Lambda(\{p\})=\Lambda(\{q\})
 =\Lambda(\{p,q\})={1\over k}.
\]

The ratio of joint survival to the product marginal reference at time
\(t\) is \(e^{t/k}\). At
\(T=k\log(1/z)\), the integrated normalized cross hazard is
\(\log(1/z)\), not \(o(1)\). \(\square\)

This abstract example is not asserted to be a repaired-ring trajectory
state. It proves the logical point: exact compensated marginals and the
sign of terminal prefix death do not imply a mixed first-moment
comparison.

### Equality and protected-column corrections

If \(a\) formal rows collapse to \(b<a\) physical rows, a coherent
dynamic reference has \(b\) row-survival factors. The unused static
factor \(d_0(X)^{a-b}\) is equality credit; it may be frozen over a
reference slab, but it may not be replaced by \(d_t(X)^{a-b}\).
Otherwise the reference decays \(a\) times while the physical row dies
only \(b\) times.

Likewise, suppose a displayed configuration contains two protected
columns and a future event of rate \(\lambda\) meets both. For the raw
configuration indicator,

\[
                         \mathcal LZ=-\lambda Z,
\]

whereas a product base with two marginal protected-column factors has
\(\dot B/B=-2\lambda\). Therefore

\[
                         \mathcal L(Z/B)=+\lambda Z/B.
\tag{2.1}
\]

Meeting a protected column is terminal for the raw count, but it is not
automatically favorable after transport by a product base. Any valid
tower must include row--column and column--column joint-deletion states,
or use a complete physical-union reference.

Finally, adjoining \(j\) ordered pair columns raises excess by \(j\).
The proved static theorem initializes this tower only while the total
physical witness order stays in its certified range. Fixing the row set
does not give an all-order initializer.

## 3. The exact conditional additive gate

Let \(\tau\) be an equality-resolved physical top-strip type. If it has
\(\widetilde s(\tau)\) distinct physical witness incidences and
\(c(\tau)\) nonempty physical columns, put

\[
                         \rho=\widetilde s(\tau)-c(\tau),
\qquad \rho_*\le\rho\le L.
\tag{3.0}
\]

Let \(B_{\tau,X}(t)\) be its physical-union current reference without
the factor \(\alpha^\rho\). It uses one survivor factor per physical
row/resource block. Any surplus formal-copy factor used by the static
theorem is frozen as equality credit, rather than evolved as another
survivor factor. The interface back to the formal graded hierarchy is
part of the conditional package below. Mark one actual live owner incidence through
the center and normalize the aggregate marked mass by

\[
                         \mathfrak I_O(t)=kE_{\rm ref}(t).
\tag{3.1}
\]

Explicitly,

\[
 U_\tau(t)=
 {1\over kE_{\rm ref}(t)}
 \sum_Xd_t(X){Z_{\tau,X}(t)\over B_{\tau,X}(t)},
\tag{3.1a}
\]

with \(d_t(X)\) realized by summing over actual marked live incidences
and resolving mark equalities. Denote the resulting stopped observable
by \(U_\tau(t)\).
The root-marked version uses
\(\mathfrak I_R(t)=E_{\rm ref}(t)\).

A clean sufficient current-residual inequality is the following
cross-prefix estimate.

The conditional package also includes the equality-resolved static
initializer

\[
                         \mathbb EU_\tau(0)
 \le C_\tau\alpha^\rho,
\qquad
 C_\tau\le\exp[C\rho\log(\rho+1)],
\tag{SI}
\]

including the frozen equality credits and the marked private-column
EGF.

### XPC (cross-prefix child)

For every predictable marked subcohort and every stopping time, outside
already stopped marked incidence,

\[
 \boxed{
 \mathcal G U_\tau(t)
 \le
 \bar\epsilon_\tau(t)U_\tau(t)
 +C_\tau L^{C_2}\alpha^{\rho+1},\qquad
 \int_0^T|\bar\epsilon_\tau(t)|\,dt=o(1).}
\tag{XPC}
\]

Here \(\bar\epsilon_\tau:[0,T]\to[0,\infty)\) is a deterministic
integrable envelope (uniform over the predictable cohort and stopping
rule). This deterministic-envelope clause is essential: a reserve
defined by integrating a trajectory-dependent error into the future
need not be adapted.

The additive source must include:

1. the edge term (1.6);
2. the marked-incidence equality partitions;
3. future events meeting protected prefix columns; and
4. the marked derivative of the private-column exponential generating
   function.

Static row exploration proves XPC at time zero for resource-disjoint
columns. It does not prove XPC in an endogenous residual, nor its
non-disjoint protected-column and marked-private extensions.
Likewise, (SI) is certified only at the slab at which its physical
initializer is actually proved. A frozen equality credit may be carried
forward from that slab, but the time-zero static theorem does not by
itself reinitialize the credit at a later random slab boundary.

There is a useful sharper sufficient input. For a one-row cluster put

\[
 A_C(g)=|\{f\in\mathcal F_C:
                 g\cap R_C(f)\ne\varnothing\}|.
\]

Assume the hereditary relative influence cap

\[
 \max_g{A_C(g)\over A_C}
 \le a_t,\qquad
 a_t\le L^{C_3}\alpha.
\tag{3.2}
\]

If the compressed prefix has \(|P_C|\le C Lk\), then

\[
\begin{aligned}
 \mathsf X_C
 &\le\sum_{p\in P_C}\sum_{g\ni p}A_C(g)\\
 &\le |P_C|\Delta_ta_tA_C,
\end{aligned}
\]

and hence

\[
 \boxed{
 \nu_t\mathsf X_C\le CLa_tA_C.}
\tag{3.3}
\]

Since \(T L^{C_3+1}\alpha=o(1)\), (3.3) gives the required integrated
cross-prefix error for compressed prefixes. A complete proof still
needs the marked private-column EGF analogue of (3.3); private columns
cannot simply be omitted from the differentiated reference.

The cap (3.2), including its stopped persistence, is not currently
proved at the top witness order. Proving its maximal persistence asks
for the same next cross-prefix child. Thus using (3.2) without a new
argument is circular.

### Lemma 3.1 (exact pair-summed cross-prefix coefficient)

Pointwise control in (3.2) can be weakened, but not eliminated.  For a
nonnegative weighted family of exposed prefixes put

\[
 \Theta_t=
 {\displaystyle
  \sum_Cw_C\sum_{p\in P_C}\sum_{g\ni p}A_C(g)
  \over\displaystyle
  \Delta_t\sum_Cw_C|P_C|A_C},
 \qquad A_C=|\mathcal F_C|,
\tag{3.4}
\]

with \(\Theta_t=0\) when the denominator vanishes.  Then, if
\(|P_C|\le C Lk\),

\[
 \boxed{
 \nu_t\sum_Cw_C\mathsf X_C
 \le {\Theta_t\over k}\sum_Cw_C|P_C|A_C
 \le C L\Theta_t\sum_Cw_CA_C.}
\tag{3.5}
\]

#### Proof

Equation (1.7), followed by reversal of the \((f,g)\)-sum, gives

\[
 \sum_Cw_C\mathsf X_C
 \le
 \sum_Cw_C\sum_{p\in P_C}\sum_{g\ni p}A_C(g).
\]

Insert (3.4) and \(\nu_t=(k\Delta_t)^{-1}\); the prefix-size bound
gives the second inequality. \(\square\)

Thus the aggregate condition

\[
                         \Theta_t\le L^{C_4}\alpha
\tag{3.6}
\]

is enough for the edge part of XPC, even when no individual
\(A_C(g)/A_C\) is small.  It must hold for the adaptively surviving
marked cohort and be supplemented by the protected-column and marked
private-EGF terms.  Section 7 shows that (3.6) is not a deterministic
consequence of the ordinary-frame static analogue under arbitrary edge
deletion.  It does not refute a repaired-ring trajectory estimate.

## 4. Conditional additive closure and maximal charge

This section proves everything that follows from XPC.

Put

\[
 E_\tau(t)=\int_0^t\bar\epsilon_\tau(s)\,ds,
\qquad
 a_\tau(t)=C_\tau L^{C_2}\alpha^{\rho+1}.
\]

Define

\[
 V_\tau(t)=
 e^{-E_\tau(t)}U_\tau(t)
 +\int_t^T e^{-E_\tau(s)}a_\tau(s)\,ds.
\tag{4.1}
\]

### Lemma 4.1 (correct additive reserve)

Under XPC, \(V_\tau\) is a nonnegative stopped supermartingale and

\[
 \mathbb EV_\tau(0)
 \le
 C_\tau\alpha^\rho
 +C_\tau TL^{C_2}\alpha^{\rho+1}
 \le 2C_\tau\alpha^\rho,
\tag{4.2}
\]

where \(C_\tau\le\exp[C\rho\log(\rho+1)]\).

#### Proof

The integrating factor gives

\[
 \mathcal G(e^{-E_\tau}U_\tau)
 \le e^{-E_\tau}a_\tau.
\]

The derivative of the future reserve in (4.1) is the negative of the
right side. This proves the supermartingale assertion. The initializer
(SI) gives the first term in (4.2), and

\[
 TL^{C_2}\alpha=m^{-9/10+o(1)}=o(1)
\]

gives the second. \(\square\)

For rigor under adaptive stopping, let \(U_\tau^{\rm act}\) contain only
marks whose centers have not yet crossed. At a first crossing, remove
the corresponding marked summands from \(U_\tau^{\rm act}\) after the
crossing jump and add their post-jump contemporaneous value, multiplied
by \(e^{-E_\tau(t)}\), to a cemetery bank \(\mathscr C_\tau\). The
hereditary cohort clause in XPC applies to \(U_\tau^{\rm act}\). Hence

\[
 \mathscr C_\tau(t)+e^{-E_\tau(t)}U_\tau^{\rm act}(t)
 +\int_t^T e^{-E_\tau(s)}a_\tau(s)\,ds
\tag{4.2a}
\]

is a supermartingale: transfers to the bank are neutral in
(4.2a), and between transfers Lemma 4.1 applies. Thus stopped mass is
banked at its crossing normalization rather than silently discarded.

Stop a center when

\[
 \sum_{\rho=\rho_*}^{L}\ \sum_{\tau\in\mathcal T_\rho}
 \alpha^{-3\rho/4}
 {Z_{\tau,X}(t)\over B_{\tau,X}(t)}>1.
\tag{4.3}
\]

Apply Lemma 4.1 to actual marked incidences and stop all marks through a
center at its first crossing. At a crossing the weighted potential
dominates the center's normalized current crossing incidence, since
\(e^{-E_\tau(t)}=e^{o(1)}\). Therefore the
expected total normalized crossing charge is at most

\[
\begin{aligned}
 \beta_0
 &\le
 C\sum_{\rho=\rho_*}^{L}
 \exp[C\rho\log(\rho+1)]\alpha^{\rho/4}\\
 &\le\exp[-c_0L\log m]
 \le\exp[-c_1(\log m)^3].
\end{aligned}
\tag{4.4}
\]

One Markov inequality at level \(\beta_0^{1/2}\) gives, with probability
\(1-o(1)\),

\[
 \boxed{
 \sum_{X\in Q_O}
 {d_{\tau_X}(X)\over kE_{\rm ref}(\tau_X)}
 +
 \sum_{R\in Q_R}
 {d_{\tau_R}(R)\over E_{\rm ref}(\tau_R)}
 \le
 \beta,}
\tag{4.5}
\]

where

\[
                         \beta=\exp[-c(\log m)^3].
\tag{4.6}
\]

Thus \(\alpha^\rho\) does beat every polynomial type, checkpoint, and
incidence factor. The unproved part is XPC, not the numerical
summation.

## 5. Soft quarantine is exactly noncascading

Keep every edge physically active during the trajectory. Stop only the
observables centered at \(Q_O\cup Q_R\). This changes no degree, no
clock, and no compensation rate, so it creates no suppression
generation.

Assume the ordinary degree stop

\[
 d_t(X)\ge c\mathcal D_O(t),\qquad
 d_t(R)\ge c\mathcal D_R(t)
\tag{5.1}
\]

at every crossing, and assume \(0<x_t,u_t\le1\). Write

\[
 E_{\rm ref}(t)=Nx_t\mathcal D_R(t),\qquad
 \mathcal D_O(t)={\rho_0x_t\over u_t}\mathcal D_R(t),
\qquad
 W={kN\over\rho_0}.
\tag{5.2}
\]

In the repaired-ring packing calibration \(\rho_0=1-o(1)\); for the
argument below it is enough to assume explicitly that
\(\rho_0\ge c_0>0\).
All crossing charges and degree lower bounds are evaluated in the same
pre-jump state.  A center killed by that jump is terminal and is not
declared newly crossed by the post-jump convention.

For an owner crossing,

\[
 {d_{\tau_X}(X)\over kE_{\rm ref}(\tau_X)}
 \ge
 {c\rho_0\over kNu_{\tau_X}}
 ={c\over Wu_{\tau_X}}
 \ge {c\over W}.
\tag{5.3}
\]

For a root crossing,

\[
 {d_{\tau_R}(R)\over E_{\rm ref}(\tau_R)}
 \ge {c\over Nx_{\tau_R}}
 \ge {c\over N}.
\tag{5.4}
\]

Equations (4.5), (5.3), and (5.4) give

\[
                         |Q_O|\le C\beta W,
\qquad
                         |Q_R|\le C\beta N.
\tag{5.5}
\]

At the terminal time, discard every selected matching edge which
contains a resource of \(Q_O\cup Q_R\). Since selected edges are
pairwise resource-disjoint, assign each discarded edge to one such
resource. Hence the number of discarded matching edges is at most

\[
 |Q_O|+|Q_R|
 \le C\beta N\left(1+{k\over\rho_0}\right)
 =O(\beta kN)=o(N).
\tag{5.6}
\]

The additional owner leave is at most

\[
 k(|Q_O|+|Q_R|)
 \le C\beta kW=o(W),
\tag{5.7}
\]

because \(\beta k\to0\). This proves a literal terminal matching
repair without any online deletion or cascade.

More exactly, if \(\mathcal M\) is the matching before this repair,
\(\mathcal M'\) is the retained matching,

\[
 s=N-|\mathcal M|,
 \qquad q=|\mathcal M\setminus\mathcal M'|,
\]

then

\[
 N-|\mathcal M'|=s+q,
 \qquad
 W-k|\mathcal M'|
 =(W-kN)+k(s+q)
 =(1-\rho_0)W+k(s+q).
\tag{5.7a}
\]

Section 5 bounds the *additional* cost \(q\) by (5.6).  The total
near-packing conclusion also uses \(s=o(N)\), supplied only by the
underlying trajectory theorem.

### One-generation primary-star deletion

For comparison with an online deletion scheme, let \(Q\) be a primary
bad-owner set of *current-state* incidence

\[
                         B=\sum_{X\in Q}d(X).
\]

Delete only the active edges meeting \(Q\), and let \(S\) be that edge
set. Then exactly

\[
 |S|\le B,\qquad
 \sum_R\Delta d(R)=|S|,\qquad
 \sum_X\Delta d(X)=k|S|\le kB.
\tag{5.8}
\]

At a fractional-loss threshold \(\eta>0\), the collateral degree masses
are at most

\[
 \sum_{R:\Delta d(R)>\eta d(R)}d(R)\le {B\over\eta},
\qquad
 \sum_{X:\Delta d(X)>\eta d(X)}d(X)\le {kB\over\eta}.
\tag{5.9}
\]

Record those collateral vertices analytically, but do not delete their
remaining stars. Thus this is only a one-generation primary-star
deletion with a collateral defect ledger, not a fully cleaned residual.
If in the current state

\[
                         B\le\beta kE,
\tag{5.10}
\]

where \(E\) is the number of active edges, choose
\(\eta=\sqrt{\beta k}\). Then the root collateral degree mass is at
most \(\eta E=o(E)\), while the owner collateral degree mass is at most
\(k\eta E=o(E)\) (and hence also \(o(kE)\)), because
\(k\eta=\sqrt{\beta k^3}=o(1)\). These conclusions use the small products
\(\beta k/\eta=\eta\) and
\(\beta k^2/\eta=k\eta\), not smallness of \(k/\eta\).
The time-separated crossing charge (4.5) does not by itself imply the
raw current-state hypothesis (5.10).

## 6. Recursive hard quarantine cannot be inferred

The absence of a cascade in Section 5 uses soft stopping. An arbitrarily
iterated hard closure does not follow from a small seed and an
\(O(m^{-2})\) pair-codegree ratio.

### Proposition 6.1 (linear layered cascade)

For every \(k\ge3\), prime \(p\ge k\), and \(h\ge1\), there is a linear
\(k\)-uniform hypergraph in which a seed of incidence fraction

\[
 {k-2\over k((k-1)^h-1)}
\tag{6.1}
\]

causes the recursive rule which quarantines after loss of *at least*
half the current predecessor-layer degree to delete the whole
hypergraph.

#### Proof

Let

\[
 V_i=[k-1]^i\times\mathbb F_p,\qquad 0\le i\le h.
\]

For \(w\in[k-1]^i\), \(a,j\in\mathbb F_p\), and \(0\le i<h\), put

\[
 e_{i,w,a,j}
 =
 \{(w,a)\}
 \cup
 \{(wc,a+cj):1\le c\le k-1\}.
\tag{6.2}
\]

Because \(p\ge k\), the labels \(1,\ldots,k-1\) are distinct nonzero
elements of \(\mathbb F_p\). Every internal vertex has \(p\) incoming
and \(p\) outgoing edges.
Two vertices lie in at most one common edge: for two children the two
linear equations determine \((a,j)\), and for a parent--child pair
they determine \(j\).

Delete the edges incident with \(V_0\). Every vertex of \(V_1\) loses
its \(p\) incoming edges, half of its degree immediately before that
predecessor-layer deletion, and is quarantined. The same statement at
each successive layer deletes \(V_2,\ldots,V_h\) (the terminal layer
loses all of its incident edges). There are

\[
 p^2\sum_{i=0}^{h-1}(k-1)^i
\]

edges and \(p^2\) seed incidences, which gives (6.1). \(\square\)

For \(k\asymp m\) and \(h=\Theta((\log m)^2)\), (6.1) is
\(\exp[-\Theta((\log m)^3)]\), while the pair-codegree ratio is at most
\(1/p\le m^{-2}\) when \(p\ge m^2\). Thus the \(\alpha^\rho\) scale
does not justify recursive hard closure. This is an abstract method
obstruction, not a literal repaired-ring residual.

## 7. An ordinary-frame residual obstruction to a universal pointwise child bound

In this section only, let \(K_{\rm full}=M+1\) be the size of an
ordinary full promotion frame; this is distinct from the repaired-edge
size used in Sections 1--6.

Let \(f,f'\) be two ordinary full promotion-frame rows whose
equality-resolved new resource
parts contain \(cK_{\rm full}\) pairs

\[
 y_i\in f\setminus f',\qquad
 z_i\in f'\setminus f,\qquad
 d_J(y_i,z_i)=1.
\]

Choose pairwise resource-disjoint promotion-frame edges
\(g_i\ni y_i,z_i\), and retain only
\(f,f',g_1,\ldots,g_{cK_{\rm full}}\). The exact distance-one pair link and the
path-mesh endpoint bound allow the \(g_i\) to be chosen greedily.
The complete greedy link audit is the pair-star construction in
MATH_AUDIT_ORDINARY_FRAME_PAIR_COLUMN_FINITE_CUTOFF_AND_PAIR_STAR_20260727.md.
The ordinary-frame subcatalogue is obtainable by edge deletion, has
\(\Delta=2\), and satisfies

\[
 {|\{g:g\cap(f\setminus f')\ne\varnothing,\
          g\cap(f'\setminus f)\ne\varnothing\}|
  \over K_{\rm full}\Delta}
 =\Theta(1).
\tag{7.1}
\]

Thus no \(o(1)\) universal pointwise whole-arm/common-event fraction
follows for every deletion residual from the time-zero static geometry.
This does not refute the trajectory-specific incidence-averaged XPC.
It shows that a proof of XPC must use that trajectory or its stopped
incidence averaging, rather than a hereditary pointwise child bound.
No claim is made that this edge-deleted subcatalogue is a
vertex-induced or dynamically reachable state of the compensated
process. The greedy construction uses the uniform triple-link estimate
conditional on the fixed distance-one pair proved in the cited
pair-star audit; an unconditional endpoint estimate alone would not
suffice.

The same construction also defeats the pair-summed coefficient (3.4),
not merely a pointwise maximum.  Let
\(\ell=\lfloor cK_{\rm full}\rfloor\), choose

\[
 \rho_*\le\rho\le\min\{L,\lfloor\ell/2\rfloor\},
\]

and display \(g_1,\ldots,g_\rho\) as protected columns between the two
rows \(f,f'\).  These columns are mutually resource-disjoint, each has
two distinct physical row incidences, and hence the displayed type has

\[
                 \widetilde s=2\rho,qquad c=\rho,qquad
                 \widetilde s-c=\rho.
\tag{7.1a}
\]

Choose one of the shared owners \(X\in f\cap f'\) as center, and require
\(f,f'\) to be distinct physical row blocks.  Expose \(f\) and the
protected columns as the prefix and take \(f'\) as the sole last-row
option in this edge-deleted subcatalogue.  The greedy pair-star theorem
makes every \(g_i\) avoid
\((f\cup f')\setminus\{y_i,z_i\}\), and hence avoid \(X\).  Thus
\(f'\) is indeed the sole remaining row through \(X\), so \(A_C=1\),
while every
\(g_j\), \(j>\rho\), is a future common event between a prefix owner
and a genuinely new last-row owner.  Since \(\Delta=2\) and
\(|P_C|\le(\rho+1)K_{\rm full}\),

\[
 \Theta_t
 \ge {\ell-\rho\over2(\rho+1)K_{\rm full}}
 \ge {c'\over\rho+1}.
\tag{7.1b}
\]

For \(\rho=\Theta((\log m)^2)\), this is much larger than
\(L^{O(1)}\alpha=m^{-19/10+o(1)}\).  Thus neither pointwise nor
pair-summed current-residual control follows from the ordinary-frame
static analogue under arbitrary edge deletion.  This remains an
ordinary-frame deletion-subcatalogue obstruction; without a repaired
lift it says nothing about repaired-ring residuals, and it is not a
vertex-induced stopped-trajectory counterexample.

Under the additional stopped pair-spread condition

\[
 d_t(y,z)\le\delta_t\Delta_t
\qquad(y\ne z),
\tag{7.2}
\]

for all distinct physical resources in the two arms (owners and top
roots alike),

two equality-resolved physical arms obey

\[
 \beta_t(f,f')
 \le K_{\rm full}\delta_t.
\tag{7.3}
\]

This follows by summing \(d_t(y,z)\) over at most
\(K_{\rm full}^2\) cross pairs and dividing by the free column scale
\(K_{\rm full}\Delta_t\).
At \(\delta_t=O(m^{-2})\), (7.3) gives the useful
pointwise scale \(O(1/m)\), but its full-time integral need not be
small. It does not supply the first strong
\(\alpha\)-child at the top order, nor the marked private-column
identity.

From this point onward return to the repaired catalogue and its edge
size \(K=k+1\).  For equality-resolved repaired arms define

\[
 \beta_t^{\rm rep}(F,F')=
 { |\{g:g\text{ meets genuinely new resources of both }F,F'\}| 
   \over K\Delta_t}.
\tag{7.3a}
\]

The density loss makes this quantitative.  For an initially saturating
pair in the independent-survivor reference trajectory, conditional on
the usual one-point degree comparison, the neutral reference scale is

\[
 {d^{\rm ref}_2(t)\over D^{\rm ref}(t)}
 \asymp {1\over m^2u_t},
 \qquad u_t=e^{-t/k}.
\tag{7.4}
\]

The analogous repaired witness-sum estimate is then only
\(\beta_t^{\rm rep}=O((mu_t)^{-1})\), and

\[
             \int_0^{k\log(1/z)}{dt\over mu_t}
             =\Theta(1/z),
\tag{7.5}
\]

which diverges for \(z=m^{-1/20}\).  This says that the scalar
pair-spread envelope cannot by itself imply XPC; it does not say that
the actual trajectory contribution diverges.  A natural summable
whole-arm target is instead

\[
 \beta_t^{\rm rep}(F,F')
 \le {L^{O(1)}\over m^2u_t};
\tag{HCE_u}
\]

for every equality-resolved displayed arm pair outside stopped
incidence.  For the compressed-core edge cross term with \(p=O(L)\)
arms, its total pair contribution is

\[
 \int_0^T\binom p2\beta_t^{\rm rep}\,dt
 \le {L^{O(1)}\over mz}=o(1).
\tag{7.6}
\]

This controls only the repaired compressed-core *edge* common-event
term.  Protected-column intersections, all physical equality shapes,
the marked private-column EGF, and the formal-to-physical interface are
still required for full XPC.

A candidate package for proving \((\mathrm{HCE}_u)\) starts with the
following incidence-weighted factorial census.  For
\(h=\Theta(\log m)\), let
\(\mathcal D_h(F,F';t)\) be the ordered common-event tuples whose new
resources outside \(F\cup F'\) are mutually disjoint.  One asks for

\[
 \sum_{F,F'}w_t(F,F')|\mathcal D_h(F,F';t)|
 \le (Ch)^{Ch}
      \left({\Delta_t\over mu_t}\right)^h
      \sum_{F,F'}w_t(F,F'),
\tag{PSF}
\]

together with the analogous bound for every equality/intersection shape
of overlapping new resources.  The existing static higher-codegree
census is intended to initialize these quantities, but that requires an
explicit check of its certified total-order range and of every overlap
shape constant.  The complete physical-union reference removes the
compensation-fibre error exactly.  The protected-column terms, marked
private-column EGF, and formal-to-physical interface remain separate.
Even the family of inequalities (PSF) is not by itself a proof of
\((\mathrm{HCE}_u)\): one must also prove (i) a controlled decomposition
of the full \(h\)-th power into those overlap/equality shapes and (ii) a
weighted extraction lemma sending exceptional arm pairs into the same
stopped owner/root incidence ledger used in Section 5.  Stopped dynamic
propagation and these two interfaces are open.  Thus (PSF) is only one
component of a proposed trajectory-specific route to the edge part of
XPC.  With \(h=\Theta(\log m)\) and only a polylogarithmic factorial
threshold, its direct Markov saving is
\(\exp[-\Theta(\log m\log\log m)]\); the stronger cemetery scale
\(\exp[-\Theta((\log m)^3)]\) would still have to come from the
\(\alpha^\rho\) top-type weight (or a stronger moment).

## 8. Exact remaining lemma

The unconditional output of this note is therefore exactly the
following.

1. Lemma 1.1 gives the complete physical-union edge/coin hazard and the
   cross-prefix correction.
2. Lemma 3.1 identifies a natural exact pair-summed coefficient
   which would control that correction.
3. The \(\alpha^\rho\) type sum (0.2) and the terminal conversion in
   Section 5 are complete once the stopped first moment is supplied.
4. Soft quarantine is noncascading because it changes no active edge;
   recursive hard quarantine is not justified, by Proposition 6.1.
5. The ordinary-frame protected pair-star (7.1a)--(7.1b) shows that
   neither pointwise nor pair-summed current-residual control is
   deletion-hereditary in that ordinary-frame analogue.

No aggregate repaired-ring first-moment theorem is proved here.

For the stopping rule (4.3), the exact logical gate is the following
banked aggregate first-moment inequality.  Put

\[
 \mathcal P_O(T)=
 \sum_{\rho=\rho_*}^{L}\sum_{\tau\in\mathcal T_\rho}
 \alpha^{-3\rho/4}
 \left(\mathscr C_\tau(T)
       +e^{-E_\tau(T)}U_\tau^{\rm act}(T)\right).
\tag{BFI-0}
\]

The missing assertion is

\[
 \boxed{
 \mathbb E\mathcal P_O(T)
 \le
 2\sum_{\rho=\rho_*}^{L}\sum_{\tau\in\mathcal T_\rho}
 C_\tau\alpha^{\rho/4},}
\tag{BFI}
\]

and the identical root-marked statement.  This is the precise banked
estimate consumed by (4.4)--(4.6); an integrated compensator estimate
implying (BFI) would be enough.  It need only concern the one
adaptively surviving cohort generated by (4.3), not every imaginable
predictable cohort.

A clean, stronger generator package sufficient for (BFI) is:

> **Hereditary marked cross-prefix census (XPC package).** Along the
> compensated repaired-ring trajectory, the equality-resolved
> top-strip types and their root-marked analogues satisfy (SI) and XPC
> for the actual adaptively surviving cohort, with a common
> deterministic error envelope, the certified physical initializer,
> protected column-intersection terms, and the marked private-column
> EGF and formal-to-physical interface included.

For the edge part, a stronger sufficient condition is the one-row cap
(3.2).  A more geometric candidate is the equality-shape-completed
factorial package around (PSF), including the power decomposition and
weighted extraction lemma, yielding \((\mathrm{HCE}_u)\).  Either route
must still be combined with the protected-column, marked-private, and
formal-to-physical terms listed in XPC.
A different sufficient route is a globally propagated physical-union
tower with a finite strong initializer and a proved fixed-arm tail.

Static \(\alpha^\rho\), exact compensated marginals, and the graded
moment ceiling do not prove (BFI). Conditional on the XPC package,
Sections 4--5 complete the aggregate first-moment and noncascading quarantine
gate. Without it, constant one is not yet proved.
