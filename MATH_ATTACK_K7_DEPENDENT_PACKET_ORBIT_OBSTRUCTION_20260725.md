# Lane K7: dependent packet selection, owner--distance capacity, and the native-colour orbit obstruction

Date: 2026-07-25

Method: pure mathematics only. No web search, finite search, solver, or
computer experiment is used.

## 0. Result and precise boundary

Put

\[
 n=2m+1,\qquad W=\binom nm,\qquad B=\frac Wn=\operatorname{Cat}_m.
\]

At depth \(q\), put

\[
 r_q=m-q,\qquad N_q=\binom n{r_q},\qquad
 W=c_qN_q+\rho_q,\quad 0\le \rho_q<N_q,
 \tag{0.1}
\]

so that \(c_q=\lfloor W/N_q\rfloor\). For fixed \(A>0\), let

\[
 H=\lceil A\sqrt m\rceil,
 \qquad S_A(m)=\sum_{q=1}^{H}\frac1{c_q}.
 \tag{0.2}
\]

This note proves two obstructions to upgrading the canonical Catalan packet
reservoir by a bounded-congestion dependent selection.

1. **Arbitrary fresh components still have an exact owner--distance speed
   limit.** Consider any adaptive path of integral exact factors. At every
   step one may choose a new coordinate transposition, recompute all ownership
   components, and switch arbitrary complete components with arbitrary
   state-dependent signs. If \(d_t(C)\) is the shorter cyclic distance between
   the two bridge letters in an old-side row \(C\) switched at time \(t\), then

   \[
   M_1(F_T)\ge M_1(F_0)-2\sum_{t,C}d_t(C),
   \tag{0.3}
   \]

   and the exact balanced-overflow ledger satisfies

   \[
   |J_A(F_T)-J_A(F_0)|
   \le 2S_A(m)\sum_{t,C}d_t(C).
   \tag{0.4}
   \]

   If \(\Gamma_d\) is the maximum, over middle owners, of the cumulative
   distance with which that owner is carried by switched rows, then

   \[
   \sum_{t,C}d_t(C)\le \Gamma_dB.
   \tag{0.5}
   \]

   Consequently, reducing \(\delta W\) first-shadow holes to \(o(W)\)
   requires

   \[
   \boxed{\Gamma_d\ge (\delta/2-o(1))n.}
   \tag{0.6}
   \]

   In particular, if unweighted owner congestion is at most \(R\) and all
   relevant bridge distances are at most \(D\), then

   \[
   \boxed{RD\ge (\delta/2-o(1))n.}
   \tag{0.7}
   \]

   Thus bounded congestion can escape only by producing macroscopic cyclic
   separation on a positive mass of rows. This theorem allows large freshly
   recomputed components; it is not restricted to the independent packet
   cube.

2. **All adaptive use of the fixed native Catalan colours is orbit-trapped.**
   Let

   \[
   \mathcal T_m=\{(2s+2\ \ 2s+3):0\le s\le m-2\},
   \qquad G_m=\langle\mathcal T_m\rangle.
   \tag{0.8}
   \]

   Start at any vertex of the full intrinsic \((2\ 3)\)-component cell of
   the canonical MSW factor. At depth \(q\), put \(d=m-q-2\). The AB7 private
   Catalan pile lies in a \(G_m\)-invariant target union \(\Omega_q\) with

   \[
   |\Omega_q|\le
   L_q:=2\binom{2d+1}{d}=(4d+2)\operatorname{Cat}_d,
   \tag{0.9}
   \]

   and every adaptive path using only freshly recomputed component switches
   with actual bridge in \(\mathcal T_m\) retains the exact mass bound

   \[
   \sum_{S\in\Omega_q}\mu_q(S)
   \ge M_q:=\operatorname{Cat}_d\operatorname{Cat}_q.
   \tag{0.10}
   \]

   This permits arbitrary component sizes, overlap across time, dependent
   signs, and recomputation.

   The exact quota floor forced by (0.9)--(0.10) is

   \[
   \boxed{
   O_q(F)\ge
   [M_q-c_qL_q-\min(L_q,\rho_q)]_+.
   }
   \tag{0.11}
   \]

   There is also an exact factorial floor. Put

   \[
   a_q=\left\lfloor\frac{M_q}{L_q}\right\rfloor
      =\left\lfloor\frac{\operatorname{Cat}_q}{4d+2}\right\rfloor,
   \quad s_q=M_q-a_qL_q,
   \quad u_q=a_q-c_q.
   \tag{0.12}
   \]

   Whenever \(u_q\ge1\), the undoubled balanced factorial excess obeys

   \[
   \boxed{
   2\Phi_q(F)
   \ge L_qu_q(u_q-1)+2s_qu_q.
   }
   \tag{0.13}
   \]

   At the Gaussian endpoint \(q=H\), (0.11) is only a sublinear lower bound:

   \[
   \frac{M_H}{W}
   \sim \frac1{32\sqrt\pi\,mH^{3/2}}
   =\Theta_A(m^{-7/4}).
   \tag{0.14}
   \]

   It therefore does **not** obstruct \(O_H=o(W)\). In contrast, (0.13)
   gives

   \[
   \boxed{
   \frac{\Phi_H(F)}W
   \ge (1-o(1))\frac{4^H}{256\pi m^2H^3}
   \longrightarrow\infty.
   }
   \tag{0.15}
   \]

   Since \(\binom{c_H+1}{2}=O_A(1)\), the normalized fixed-window factorial
   objective also diverges. Thus adaptive fixed-native-colour switching cannot
   repair the AB7 factorial obstruction.

   More generally, adjoining \(k\) arbitrary transposition colours enlarges
   the trapped target union by at most \(6^k\), and this black-box factor is
   sharp. Hence every fixed-frame palette with
   \(k\le(\log4/\log6-\varepsilon)H\) new colours still has
   \(\Phi_H/W\to\infty\). Release of the certified orbit-cardinality lower
   bound requires
   \(k\ge(\log4/\log6)H-O(\log m)\).

The scope boundary is sharp. The orbit theorem applies to a fixed physical
native colour set, or to one consistently transported native set in a single
co-moving frame. An arbitrary global relabelling followed by choosing the
new physical-native colours introduces conjugate transpositions outside the
old group and destroys the invariant. Hence (0.15) closes the fixed-native
factorial route, not adaptive use of genuinely new colours, not the balanced
overflow gate, and not the constant-one theorem.

## 1. Exact balanced-overflow and factorial baselines

Let \(\mu_q^F\) be the rank-\(r_q\) cyclic-interval load of an exact factor
\(F\). Its mass is always

\[
 \sum_{S\in\binom{[n]}{r_q}}\mu_q^F(S)=W.
 \tag{1.1}
\]

Let \(\mathcal B_q\) be the set of quota vectors having exactly \(\rho_q\)
entries \(c_q+1\) and all other entries \(c_q\). Define

\[
 O_q(F)=\frac12\min_{b\in\mathcal B_q}\|\mu_q^F-b\|_1,
 \qquad
 J_A(F)=\sum_{q=1}^{H}\frac{O_q(F)}{c_q}.
 \tag{1.2}
\]

For equal-mass integral vectors \(x,y\), distance to \(\mathcal B_q\) gives

\[
 |O_q(x)-O_q(y)|\le\frac12\|x-y\|_1.
 \tag{1.3}
\]

The undoubled balanced factorial excess is

\[
 \Phi_q(F)
 =\sum_S\binom{\mu_q^F(S)}2
 -\left[(N_q-\rho_q)\binom{c_q}{2}
        +\rho_q\binom{c_q+1}{2}\right].
 \tag{1.4}
\]

The exact floor identity is

\[
 2\Phi_q(F)
 =\sum_S(\mu_q^F(S)-c_q)(\mu_q^F(S)-c_q-1).
 \tag{1.5}
\]

Every summand in (1.5) is nonnegative for integral \(\mu_q^F(S)\).
No continuous relaxation of the quota floor is used below.

## 2. Arbitrary recomputed components: exact owner--distance capacity

Consider a finite path \(F_0,F_1,\ldots,F_T\) of integral exact factors.
A step may be a whole coordinate relabelling. Every other step has the
following form: choose a coordinate transposition \(\tau_t\), freshly compute
the ownership components of \(F_{t-1}\) versus \(\tau_tF_{t-1}\), and switch
an arbitrary family of complete components. Components switched in one overlay
are owner-disjoint, so they may equivalently be listed separately.

For a switched component \(K\), let \(C\in K\) run over its current old-side
rows. Write \(w_{C,r}\) for the indicator vector of cyclic \(r\)-intervals
of \(C\). If the two letters of \(\tau_t\) have shorter cyclic distance
\(d_t(C)\in\{1,\ldots,m\}\) in \(C\), then the exact row-displacement identity
is

\[
 \|\tau_tw_{C,r}-w_{C,r}\|_1
 =4\min(r,d_t(C))-4\mathbf1_{\{d_t(C)=r\}}
 \quad(2\le r\le m).
 \tag{2.1}
\]

Define the exact positive-action capacity

\[
 \lambda_r(d)=2\min(r,d)-2\mathbf1_{\{d=r\}},
 \tag{2.2}
\]

so \(\lambda_r(d)\) is one half of (2.1). Notice the always-valid bound

\[
 \lambda_r(d)\le2d.
 \tag{2.3}
\]

### Theorem 2.1 (adaptive component path capacity)

For every path above and every \(H\le m-2\),

\[
 \boxed{
 M_1(F_T)
 \ge M_1(F_0)-\sum_{t,C}\lambda_{m-1}(d_t(C)),
 }
 \tag{2.4}
\]

and

\[
 \boxed{
 |J_A(F_T)-J_A(F_0)|
 \le
 \sum_{t,C}\sum_{q=1}^{H}
 \frac{\lambda_{m-q}(d_t(C))}{c_q}.
 }
 \tag{2.5}
\]

Consequently (0.3)--(0.4) hold.

#### Proof

Switching one component changes the depth-\(q\) load by

\[
 v_{K,q}=\sum_{C\in K}(\tau_tw_{C,m-q}-w_{C,m-q}),
 \tag{2.6}
\]

up to reversing the displayed sign. By (2.1) and the triangle inequality,

\[
 \frac12\|v_{K,q}\|_1
 \le\sum_{C\in K}\lambda_{m-q}(d_t(C)).
 \tag{2.7}
\]

The vector \(v_{K,q}\) has total sum zero. Adding an integral zero-sum vector
can remove at most its total positive mass worth of zero coordinates, and that
positive mass is \(\|v_{K,q}\|_1/2\). Apply (2.7) with \(q=1\) and telescope
to prove (2.4).

Apply the exact Lipschitz inequality (1.3), divide by \(c_q\), sum over
depths, and telescope over all switched components to prove (2.5). Whole
coordinate relabellings change neither \(M_1\) nor \(J_A\). Finally use
(2.3), first at \(r=m-1\) and then at every \(r=m-q\), to obtain
(0.3)--(0.4). \(\square\)

### 2.1 Owner--distance congestion

Every current row \(C\) owns an \(n\)-element block \(U_t(C)\) of middle
masks. Define the cumulative owner--distance load

\[
 \gamma(X)=
 \sum_{t,C:\,X\in U_t(C)}d_t(C),
 \qquad
 \Gamma_d=\max_X\gamma(X).
 \tag{2.8}
\]

Double counting gives the exact identity

\[
 \sum_X\gamma(X)=n\sum_{t,C}d_t(C).
 \tag{2.9}
\]

Since there are \(W=nB\) middle owners, (2.9) proves

\[
 \sum_{t,C}d_t(C)
 \le\frac{\Gamma_dW}{n}=\Gamma_dB,
 \tag{2.10}
\]

which is (0.5). More intrinsically, the **average** owner--distance load is

\[
 \frac1W\sum_X\gamma(X)
 =\frac1B\sum_{t,C}d_t(C).
 \tag{2.11}
\]

Thus (0.6) is an average-load requirement, not merely a worst-owner artifact.

Suppose every middle owner occurs in at most \(R\) switched row blocks and
every relevant distance is at most \(D\). Then \(\Gamma_d\le RD\), proving
(0.7).

There is also a distributional strengthening. If the unweighted owner
congestion is at most \(R\) and \(\delta W-o(W)\) first-shadow holes are
removed, then at least \((\delta/2-o(1))B\) switched row occurrences satisfy

\[
 d_t(C)\ge \frac{\delta}{4R}n.
 \tag{2.12}
\]

Indeed there are at most \(RB\) row occurrences, every distance is at most
\(m<n/2\), and if fewer than \((\delta/2-o(1))B\) occurrences met (2.12),
then

\[
 \sum_{t,C}d_t(C)
 <\frac{\delta n}{4R}(RB)+\frac n2\left(\frac\delta2B-o(B)\right)
 =\frac\delta2nB-o(W),
\]

contradicting (0.3).

For the Gaussian window,

\[
 S_A(m)=(\kappa_A+o(1))\sqrt m,
 \qquad
 \kappa_A=\int_0^A\frac{dx}{\lfloor e^{x^2}\rfloor}.
 \tag{2.13}
\]

Hence reducing a starting value \(J_A(F_0)\ge\delta W\) to \(o(W)\)
requires

\[
 \Gamma_d
 \ge(\delta-o(1))\frac{n}{2S_A(m)}
 =\left(\frac\delta{\kappa_A}+o(1)\right)\sqrt m.
 \tag{2.14}
\]

Under the frozen macroscopic first-shadow premise, the stronger linear
requirement (0.6) applies.

## 3. The sharper universal-packet complexity ceiling

The universal common-tail two-for-two packet has much smaller action than
the sum of its individual row displacements. For one signed packet atom
\(z\), the audited exact footprint is

\[
 \frac12\|B_{m-q}z\|_1=
 \begin{cases}
 2,&q=1,\\
 4,&2\le q\le H.
 \end{cases}
 \tag{3.1}
\]

Let two integral exact factors \(F,G\) have an algebraic packet decomposition

\[
 [G]-[F]=\sum_{j=1}^{M}\varepsilon_jz_j,
 \qquad \varepsilon_j\in\{-1,1\},
 \tag{3.2}
\]

where every \(z_j\) is a relabelled universal contextual packet atom. No
independence, common starting atlas, or legal ordering of the atoms in (3.2)
is assumed.

### Theorem 3.1 (dependent algebraic packet ceiling)

For all sufficiently large \(m\), so that \(c_1=1\) and \(H\le m-2\),

\[
 \boxed{
 |J_A(G)-J_A(F)|\le M(4S_A(m)-2),
 }
 \tag{3.3}
\]

and

\[
 \boxed{M_1(G)\ge M_1(F)-2M.}
 \tag{3.4}
\]

#### Proof

Apply (1.3), (3.1), and the triangle inequality directly to the endpoint
identity (3.2). At depth one, each atom has exactly two positive unit cells,
so it can fill at most two old holes. \(\square\)

The endpoint formulation makes dependence irrelevant: a correlated random
selector, a deterministic dependent selector, and an adversarial selector
all obey the same bound outcome by outcome.

If each legal packet atom carries its certified \(2n\)-element middle-root
packet \(U_j\), define packet-owner congestion

\[
 D=\max_X|\{j:X\in U_j\}|.
 \tag{3.5}
\]

Then

\[
 2nM=\sum_j|U_j|
 \le DW,
 \qquad M\le\frac D2B.
 \tag{3.6}
\]

Thus

\[
 |J_A(G)-J_A(F)|\le D(2S_A-1)B,
 \qquad
 M_1(G)\ge M_1(F)-DB.
 \tag{3.7}
\]

In particular, bounded packet-owner congestion cannot remove a macroscopic
first-shadow defect. Repair requires \(D\ge(\delta-o(1))n\).

This theorem also applies to any actual word of arbitrary global relabellings
and fresh universal packet toggles. Pull every state back by its cumulative
global relabelling. A relabelling step then disappears, while every packet
step becomes one relabelled atom in (3.2). State-dependent packet choice and
fresh recomputation do not alter the conclusion.

For the exact K6 matching reservoir

\[
 L_m=\left(\frac{11}{72}+o(1)\right)B,
 \tag{3.8}
\]

if each reservoir label is used at most \(D_0\) times by an arbitrary
dependent commutator circuit whose leaves are universal packets, then
\(M\le D_0L_m\). Removing \(\delta W-o(W)\) holes therefore forces

\[
 \boxed{
 D_0\ge\left(\frac{36\delta}{11}-o(1)\right)n.
 }
 \tag{3.9}
\]

The corresponding all-band requirement is

\[
 D_0\ge
 \left(\frac{36\delta}{11\kappa_A}+o(1)\right)\sqrt m.
 \tag{3.10}
\]

Consequently a bounded-congestion dependent selection escapes the independent
cube ceiling only if recomputation creates a macro-move which is either outside
the universal packet lattice or has \(\Omega(n)\) packet complexity on average.

## 4. Adaptive native-colour orbit invariance

The transpositions in \(\mathcal T_m\) are pairwise disjoint. Thus
\(G_m\) is an elementary abelian two-group, but only setwise invariance of
its target orbits is needed.

### Theorem 4.1 (adaptive fixed-subgroup mass invariant)

Fix a depth \(q\) and a target union \(\Omega\subseteq\binom{[n]}{r_q}\)
which is invariant under every \(\tau\in\mathcal T_m\). Along an arbitrary
adaptive path of freshly recomputed complete-component switches whose actual
bridge transposition always belongs to \(\mathcal T_m\),

\[
 \boxed{
 \sum_{S\in\Omega}\mu_q^F(S)
 \text{ is constant.}
 }
 \tag{4.1}
\]

#### Proof

For a current \(\tau\)-component \(K\), let \(a_{K,q}\) be the old-side
load. Switching it changes the load by

\[
 \tau a_{K,q}-a_{K,q}.
 \tag{4.2}
\]

Since \(\tau\Omega=\Omega\), the sum of (4.2) over \(\Omega\) is zero.
This is componentwise, so arbitrary component subsets and arbitrary signs
may be used. It is statewise, so the component partition may be recomputed
after every preceding move. \(\square\)

### 4.1 The private Catalan orbit closure

Fix \(1\le q\le m-2\), put \(d=m-q-2\), and let
\(V\in\mathcal D_d\). The AB7 private target pair for
\(\tau_0=(2\ 3)\) is

\[
 p_V=\{S_V,\tau_0S_V\},
 \qquad
 S_V=\{2,n\}\cup(4+2q+\operatorname{Down}(V)).
 \tag{4.3}
\]

The down-step list has \(d\) entries in an interval of \(2d\) consecutive
step indices. Therefore its shifted coordinate support lies in

\[
 I_q=\{2q+4,2q+5,\ldots,2m\},
 \qquad |I_q|=2d+1.
 \tag{4.4}
\]

The set \(I_q\) is invariant under every native transposition which meets it:
it contains the complete pairs
\((2q+4\ \ 2q+5),\ldots,(2m-2\ \ 2m-1)\), while coordinate \(2m\)
is fixed by \(G_m\). Native prefix transpositions fix (4.3), \(\tau_0\)
only chooses one of \(2,3\), and \(n\) is fixed.

It follows that

\[
 G_m\{S_V,\tau_0S_V:V\in\mathcal D_d\}
 \subseteq
 \bigl\{\{\epsilon,n\}\cup D:
 \epsilon\in\{2,3\},\ D\in\tbinom{I_q}{d}\bigr\}.
 \tag{4.5}
\]

Define the left side of (4.5) to be \(\Omega_q\). Then

\[
 |\Omega_q|\le2\binom{2d+1}{d}.
 \tag{4.6}
\]

Using

\[
 \binom{2d+1}{d}=(2d+1)\operatorname{Cat}_d
 \tag{4.7}
\]

proves (0.9).

The AB7 private-pile theorem states that, at every vertex \(F\) of the full
intrinsic \(\tau_0\)-component cell,

\[
 \mu_q^F(S_V)+\mu_q^F(\tau_0S_V)
 \ge\operatorname{Cat}_q.
 \tag{4.8}
\]

The pairs in (4.8) are distinct as \(V\) varies. Summing over the
\(\operatorname{Cat}_d\) suffixes gives

\[
 \sum_{S\in\Omega_q}\mu_q^F(S)
 \ge\operatorname{Cat}_d\operatorname{Cat}_q=M_q.
 \tag{4.9}
\]

Now apply Theorem 4.1. This proves (0.10) along the entire adaptive
fixed-native-colour path.

### 4.2 A quantitative enlargement bound for new colours

The fixed-native obstruction does not disappear after adjoining only a few
new transpositions.

### Theorem 4.2 (finite palette-growth obstruction)

Let \(E\) be any set of \(k\) additional coordinate transpositions and put

\[
 \widehat G=\langle \mathcal T_m\cup E\rangle.
 \tag{4.10}
\]

Then

\[
 \boxed{
 |\widehat G\Omega_q|\le6^kL_q.
 }
 \tag{4.11}
\]

Consequently every adaptive path of freshly recomputed component switches
whose actual bridge colours lie in the fixed palette \(\mathcal T_m\cup E\)
retains mass at least \(M_q\) in a target union of cardinality at most

\[
 L_{q,k}:=\min(N_q,6^kL_q).
 \tag{4.12}
\]

#### Proof

The coordinate graph of \(\mathcal T_m\) consists of initial blocks
\(B_i\) of sizes \(b_i\in\{1,2\}\). Consider a connected component of the
enlarged coordinate graph which contains \(p\) initial blocks. For a fixed
native target profile, put

\[
 t_i=|S\cap B_i|,\qquad b=\sum_i b_i,\qquad t=\sum_i t_i.
 \tag{4.13}
\]

The native orbit on this component has size
\(\prod_i\binom{b_i}{t_i}\). The transpositions along the connected enlarged
graph generate \(\operatorname{Sym}(b)\), so the enlarged orbit has size
\(\binom bt\). Its expansion ratio satisfies

\[
 \frac{\binom bt}{\prod_i\binom{b_i}{t_i}}
 \le6^{p-1}.                                           \tag{4.13a}
\]

For \(p=1\), the ratio is one. For \(p\ge2\), its denominator is at least one,
\(b\le2p\), and

\[
 \binom bt\le\binom{2p}{p}\le6^{p-1}.
\]

The last inequality begins with \(\binom42=6\); each subsequent central
binomial ratio is \(2(2p+1)/(p+1)<4<6\).

If the enlarged coordinate components contain \(p_j\) initial blocks, they
require at least \(p_j-1\) of the new edges. Hence
\(\sum_j(p_j-1)\le k\), and multiplication of (4.13a) bounds the expansion of
each native subset orbit by \(6^k\). Apply this orbit by orbit to the
\(G_m\)-invariant union \(\Omega_q\). Enlarged-orbit overlaps only reduce the
union size, proving (4.11). The factor is sharp for the abstract block lemma:
one edge joining two size-two blocks with native profile counts \(0,2\)
expands one state to all six two-subsets.

The union \(\widehat G\Omega_q\) is invariant under every palette colour.
Theorem 4.1, with the identical componentwise proof, preserves its mass.
Truncating its cardinality bound at the whole target-layer size proves
(4.12). \(\square\)

Apply Theorem 5.2 below with \(L=L_{q,k}\). Whenever

\[
 x_{q,k}:=\frac{\operatorname{Cat}_q}{(4d+2)6^k}
 \ge4(c_q+1),
\tag{4.14}
\]

the truncation in (4.12) is inactive. Indeed \(M_q\le W\), while
\(W<(c_q+1)N_q\), so

\[
 6^kL_q=\frac{M_q}{x_{q,k}}
 \le\frac{W}{4(c_q+1)}<N_q.
 \tag{4.14a}
\]

The elementary estimates

\[
 \lfloor x_{q,k}\rfloor-c_q\ge\frac34x_{q,k},
 \qquad
 \lfloor x_{q,k}\rfloor-c_q-1\ge\frac12x_{q,k}
 \tag{4.15}
\]

give the safe finite bound

\[
 \boxed{
 \Phi_q(F)
 \ge\frac{\operatorname{Cat}_d\operatorname{Cat}_q^2}
 {32d\,6^k}.
 }
 \tag{4.16}
\]

Here (4.16) is asserted for \(d\ge1\), equivalently \(q\le m-3\).  When
\(d=0\), the exact floor in Theorem 5.2 remains the valid statement.

At \(q=H\), using

\[
 \operatorname{Cat}_H\ge\frac{4^H}{4H^2},
 \qquad
 \operatorname{Cat}_{m-H-2}>\frac{B}{4^{H+2}},
 \tag{4.17}
\]

gives

\[
 \boxed{
 \frac{\Phi_H(F)}W
 >\frac{4^H}{8192\,ndH^4\,6^k}.
 }
 \tag{4.18}
\]

If, in addition, \(x_{H,k}\to\infty\), the sharper asymptotic form is

\[
 \frac{\Phi_H(F)}W
 \ge(1-o(1))
 \frac{4^H}{256\pi m^2H^3\,6^k}.
 \tag{4.19}
\]

Therefore, for every fixed \(\varepsilon>0\), every palette with

\[
 k\le\left(\frac{\log4}{\log6}-\varepsilon\right)H
 \tag{4.20}
\]

still forces \(\Phi_H(F)/W\to\infty\). More precisely, release of the
certified orbit-cardinality lower bound requires

\[
 k\ge\frac{\log4}{\log6}H-O(\log m).
 \tag{4.21}
\]

Thus a successful native-packet continuation which eliminates this factorial
floor must create at least
\((\log4/\log6)H-O(\log m)\) genuinely new transposition colours in one fixed
frame, or
use transformations not represented by such a bounded transposition palette.

There is a direct commutator-support corollary. If a coordinate permutation
\(g\) has support size \(s\), then

\[
 g\mathcal T_mg^{-1}\setminus\mathcal T_m
 \quad\hbox{contains at most }s\hbox{ transpositions}.
 \tag{4.22}
\]

Indeed, a native matching edge with neither endpoint in \(\operatorname{supp}g\)
is fixed, and at most \(s\) native matching edges meet that support. Hence,
after transporting the private union into one common co-moving frame, a scheme
using the original and one transported native palette under an
\(s\)-supported preparation still satisfies (4.18) with \(k\le s\).
It follows that

\[
 \boxed{s\ge\frac{\log4}{\log6}H-O(\log m)}
 \tag{4.23}
\]

is necessary before this factorial orbit obstruction can disappear. Thus the
bounded-coordinate route to eliminating this private-pile factorial floor is
closed by the same argument; such a preparation needs
\(\Omega(H)=\Omega(\sqrt m)\) coordinate support. This is not a necessity
claim for balanced overflow.
This corollary does not cover repeated arbitrary re-framing: a global
relabelling moves the invariant union itself, so Theorem 4.1 must be restarted
in the transported frame.

## 5. Exact orbit-capacity floors

### Theorem 5.1 (quota overflow trapped in a small invariant union)

Let an integral load \(\mu\) of total mass \(W\) put at least \(M\) mass on
a target union \(\Omega\) of cardinality at most \(L\). Then

\[
 \boxed{
 O_q(\mu)\ge[M-c_qL-\min(L,\rho_q)]_+.
 }
 \tag{5.1}
\]

#### Proof

For every quota vector \(b\in\mathcal B_q\),

\[
 b(\Omega)\le c_q|\Omega|+\min(|\Omega|,\rho_q)
 \le c_qL+\min(L,\rho_q).
 \tag{5.2}
\]

Hence \(\mu(\Omega)-b(\Omega)\) is at least the positive part in (5.1).
Equal total masses force the same deficit outside \(\Omega\), so the
\(\ell^1\)-distance is at least twice that amount. Divide by two and minimize
over \(b\). \(\square\)

Applying Theorem 5.1 with \(M=M_q,L=L_q\) proves (0.11).

### Theorem 5.2 (exact integral factorial floor)

In the setting of Theorem 5.1, assume explicitly that
\(1\le L\le N_q\), and put

\[
 a=\lfloor M/L\rfloor,\qquad s=M-aL,\qquad u=a-c_q.
 \tag{5.3}
\]

If \(u\ge1\), then

\[
 \boxed{
 2\Phi_q(\mu)\ge Lu(u-1)+2su.
 }
 \tag{5.4}
\]

#### Proof

Every summand of the exact identity (1.5) is nonnegative. Enlarge \(\Omega\),
if necessary, by arbitrary **actual rank-\(r_q\) targets** to a set of exactly
\(L\) targets. (Here \(L\le N_q\); in the application, the displayed family
on the right of (4.5) itself has cardinality \(L_q\).) The load on this enlarged
set is still at least \(M\), and all targets outside it may be discarded.
Since \(a\ge c_q+1\), the function

\[
 x\longmapsto(x-c_q)(x-c_q-1)
 \]

is discretely convex on all integers. At a fixed total its sum is minimized
when all entries differ by at most one. Once the total is at least
\(L(c_q+1)\), this balanced minimum is nondecreasing in the total, because
raising any balanced entry \(x\ge c_q+1\) changes the summand by
\(2(x-c_q)\ge2\). Hence the minimum for total mass at least
\(M=aL+s\) is attained at total mass exactly \(M\), with \(L-s\) entries
\(a\) and \(s\) entries \(a+1\). Their
contribution is

\[
 (L-s)u(u-1)+s(u+1)u
 =Lu(u-1)+2su.
 \]

Use (1.5). \(\square\)

With \(M=M_q,L=L_q\), (5.3) is exactly (0.12), so (5.4) proves (0.13).

## 6. Gaussian asymptotics

Take \(q=H=\lceil A\sqrt m\rceil\) and \(d=m-H-2\). Both \(H,d\to\infty\),
and \(d/m\to1\). The Catalan asymptotic

\[
 \operatorname{Cat}_j
 =(1+o(1))\frac{4^j}{\sqrt\pi\,j^{3/2}}
 \tag{6.1}
\]

gives

\[
 \frac{M_H}{W}
 =\frac{\operatorname{Cat}_d\operatorname{Cat}_H}
 {n\operatorname{Cat}_m}
 \sim\frac1{16\sqrt\pi\,nH^{3/2}}
 \sim\frac1{32\sqrt\pi\,mH^{3/2}}.
 \tag{6.2}
\]

Moreover \(c_H=O_A(1)\), while

\[
 \frac{\operatorname{Cat}_H}{4d+2}\longrightarrow\infty.
 \tag{6.3}
\]

Thus the subtraction in (0.11) is negligible relative to \(M_H\), and the
right side of (0.11) is \((1-o(1))M_H\). Equation (6.2) proves (0.14).

For the factorial floor, \(u_H\sim a_H\sim\operatorname{Cat}_H/(4d+2)\)
and \(s_H<L_H\). Therefore (0.13) gives

\[
 \Phi_H(F)
 \ge(1-o(1))\frac12L_Ha_H^2
 =(1-o(1))\frac{\operatorname{Cat}_d\operatorname{Cat}_H^2}{8d}.
 \tag{6.4}
\]

Dividing by \(W=n\operatorname{Cat}_m\) and applying (6.1) once more gives

\[
 \frac{\Phi_H(F)}W
 \ge(1-o(1))\frac{4^H}{128\pi dnH^3}
 =(1-o(1))\frac{4^H}{256\pi m^2H^3},
 \tag{6.5}
\]

which tends to infinity and proves (0.15).

At a floor jump where \(e^{A^2}\) is an integer, \(c_H\) need not converge
to one fixed integer along every subsequence. This causes no problem:
\(W/N_H\to e^{A^2}\), so \(c_H\) and
\(\binom{c_H+1}{2}\) remain bounded by constants depending only on \(A\),
which is all that (6.3)--(6.5) use.

## 7. Adversarial scope audit

1. **Dependence versus action.** Correlating packet signs never enlarges the
   deterministic endpoint diameter in Theorem 3.1. Only a freshly generated
   move with large packet complexity, or one outside the universal packet
   lattice, can do so.

2. **Large components are included in Theorem 2.1.** The component may contain
   any number of rows. Its capacity is charged row by row through the exact
   cyclic distance. The theorem does not assume packet decomposition.

3. **Distance is the genuine escape.** Bounded unweighted owner congestion by
   itself is not a no-go for arbitrary large components: a transposition whose
   letters are at distance \(\Theta(n)\) in many rows has \(\Theta(n)\)
   first-shadow action per row. Equations (0.6)--(0.7) isolate precisely this
   amplification requirement.

4. **Fixed physical subgroup.** Theorem 4.1 survives arbitrary adaptive signs,
   component sizes, overlap, and recomputation, but only while every actual
   bridge lies in the fixed subgroup generators \(\mathcal T_m\). It also
   survives a consistently transported copy \(g\mathcal T_mg^{-1}\) if the
   target union is transported by the same single frame.

5. **Arbitrary re-framing escapes.** If a global relabelling is followed by
   choosing the physical-native colours again, then in the old frame the new
   bridges are conjugates not generally contained in \(G_m\). The old
   \(\Omega_q\)-mass need not be invariant. Likewise, redefining the canonical
   Dyck frame after every move is outside Theorem 4.1 unless the resulting
   conjugates preserve the same target union.

6. **Starting class.** The private mass (4.8) is proved at vertices of the full
   intrinsic \((2\ 3)\)-cell. The orbit invariant does not manufacture that
   mass at an arbitrary exact factor.

7. **Overflow versus factorial excess.** The trapped Gaussian private mass is
   only \(\Theta_A(Wm^{-7/4})\). Therefore its exact overflow floor is
   sublinear. Its average load inside the much smaller orbit closure is
   exponentially large, which forces the divergent factorial floor. Claiming
   a macroscopic balanced-overflow obstruction from (0.11) would be false.

8. **Literal exactness.** Every state in Theorems 2.1 and 4.1 is an integral
   exact wreath factor and hence has the usual literal contiguous-OR
   linearization. The algebraic Theorem 3.1 assumes both endpoints are integral
   exact factors; it uses no fractional endpoint or post-rounding.

The proved boundary is therefore:

> Bounded-congestion dependence cannot amplify universal packets. More
> generally, arbitrary recomputed components cannot repair a macroscopic first
> shadow without linear owner--distance exposure. Staying inside the fixed
> native Catalan colour group is even more rigid: it preserves a private-orbit
> mass which forces divergent Gaussian factorial excess. A viable positive
> scheme must introduce genuinely new conjugate colours and simultaneously
> create macroscopic cyclic distance, while controlling the exact balanced
> overflow rather than only factorial collision.
