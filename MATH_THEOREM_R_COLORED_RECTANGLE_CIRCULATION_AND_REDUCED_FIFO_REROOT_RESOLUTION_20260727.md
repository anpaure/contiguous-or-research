# Colored rectangle circulation and the reduced-scale FIFO re-root gate

Date: 2026-07-27

Method: pure mathematics only. No computation, finite search, solver, or
web input is used.

## 0. Exact outcome

Put

\[
 n=2m,\qquad
 H=\left\lfloor\sqrt{m\log\log m}\right\rfloor,\qquad
 k=m-H,\qquad \ell=m+H,
\]

\[
 W=\binom{2m}{m},\qquad N=N_H=\binom{2m}{k},\qquad
 \lambda={W\over N},\qquad \rho=\lfloor\lambda\rfloor .
\tag{0.1}
\]

The per-top \(K_2\) cancellation problem has two sharply different
parts.

1.  The certified intrinsic static two-top boundary-\(K_2\) rectangle
    system is a signed graph incidence system. Every connected component
    carrying a nonzero collar is balanced, hence gauges to an ordinary
    network matrix.
    For the displayed two-endpoint divergence rows, its exact bounded
    flow feasibility conditions are Hoffman cuts, and every feasible
    integral instance has an integral solution. This does not include
    additional owner, capacity, port, or chronology rows.

2.  This integrality does **not** move the middle ledger around a closed
    rectangle circulation. After the same normalization that turns the
    collar columns into signed-incidence columns,

    \[
                         \Delta_{\rm mid}(x)=M_0D_\Sigma x.
    \tag{0.2}
    \]

    Thus \(D_\Sigma x=0\) implies \(\Delta_{\rm mid}(x)=0\). More
    generally two rectangle flows with the same full
    boundary-orbit option divergence have exactly the same middle
    action. Static cycle augmentation may alter congestion or provide
    chronological flexibility, but it does not itself certify a
    prefix-legal chronology and cannot change the desired endpoint
    displacement.

3.  The obstruction is genuinely ordered. With added connector seams,
    a traversed signed cycle \(C\) obeys the exact holonomy equation

    \[
      (1-P_C)c_{v_0}=-\sum_{e_i\in C}P_i s_{e_i}.
    \tag{0.3}
    \]

    Endpoint deck differences telescope, but connector length,
    seam-crossing occurrences, queue-arc usage, port usage, and an
    independently assigned voltage need not. They are not consequences
    of (0.2).

4.  A retained segment of length \(\rho\) has an exact two-endpoint
    trace derivative. In the natural facet-cycle implementation, a
    \(t\)-top collar-neutral re-root cycle necessarily satisfies

    \[
                              \boxed{t\rho\ge 2H.}
    \tag{0.4}
    \]

    Therefore the four-top overlapping-collar facet-cycle restriction
    cannot be shortened to the calibrated scale
    \(\rho\sim\log m\). Any implementation by that exact mechanism needs

    \[
                    t\ge\left\lceil {2H\over\rho}\right\rceil
                    =\Theta\!\left(
                    {\sqrt{m\log\log m}\over\log m}\right)
    \tag{0.5}
    \]

    coherently re-rooted carriers.

5.  There is an exact growing re-root cycle, not merely a projected
    circulation. On the ordered \(Q/P/E\) atlas define

    \[
                              F_r=S\circ O^{r-1}.
    \tag{0.6}
    \]

    If \(g=\gcd(\ell,r)\) and \(s_0=\ell/g\), its slot cycles have
    lengths

    \[
                    s_0+k\quad\hbox{once},\qquad
                    s_0\quad\hbox{\(g-1\) times}.
    \tag{0.7}
    \]

    At the first root return the whole ordered state closes iff

    \[
                          g=1\quad\hbox{or}\quad s_0\mid k.
    \tag{0.8}
    \]

    If \(1\le r<\ell/(2H)\), the second alternative is impossible.
    This includes \(r=\rho\) and \(r=\rho+1\) for all sufficiently large
    \(m\). Under this stated range,

    \[
                         \boxed{\gcd(m+H,r)=1}
    \tag{0.9}
    \]

    is necessary and sufficient for this fixed macro to be a root-simple
    ordered-slot/FIFO-zero-monodromy owner trajectory. When (0.9)
    holds, the cycle has \(2m\) root blocks and \(2mr\) elementary owner
    transitions. No independently assigned deck, tag, or packet voltage
    is included in this conclusion.

6.  Mixing \(r\)- and \((r+1)\)-blocks to make one top-slot lap does not
    remove monodromy. Every positive block word with total stride
    \(\ell\) moves the ordered exterior queue and fails even setwise root
    closure. This rules out only that one-lap adjacent-length schedule,
    not correlated multi-lap or componentwise floor repair.

7.  At the calibrated scale,

    \[
       \lambda=\log m+o(1),\qquad
       N=(1+o(1)){W\over\log m},\qquad
       \rho N=W-o(W).
    \tag{0.10}
    \]

    If \(\gcd(\ell,\rho)=1\) and a root near-factor is selected from the
    \(F_\rho\) catalogue, its scalar floor **occurrence count** is
    \(\rho N-o(W)=W-o(W)\). Both the root near-factor and pairwise
    distinct owner coverage are still unproved. Without that arithmetic
    hypothesis, the fixed \(F_\rho\) macro does not close. Using
    \(r=1\) with \(\rho\) clone colors supplies only a scalar
    multiplicity, not distinct-owner completion; Section 8 rules out the
    simplest one-lap \(\rho/(\rho+1)\) repair. Independently of \(r\),
    the separately proved oriented root-catalogue incidence count gives
    root degree \(k!\ell!\) and maximum relative root-pair codegree
    \(2/(k\ell)\). What remains unproved is an arithmetic-compatible
    **integral** selection together with exact middle-owner completion
    and all target capacities.

The pure rectangle-circulation route is therefore closed:
its balanced components are integral but its closed flows are
middle-null. The surviving coefficient-one gate is a matching/section
problem in the ordered-slot/FIFO-zero-monodromy catalogue. A route using
only the certified two-top rectangle and three-top re-root libraries is
further confined to one exact column-histogram fibre; general facet
cycles need not be. No coefficient-one theorem is claimed.

## 1. Reduced-scale calibration

The exact ratio in (0.1) is

\[
 \lambda
 =\prod_{j=1}^{H}{m+j\over m-j+1}.
\tag{1.1}
\]

Uniformly for \(H=o(m^{2/3})\), Taylor expansion gives

\[
 \log\lambda
 ={H^2\over m}
 +O\!\left(
 {H\over m}+{H^2\over m^2}+{H^4\over m^3}
 \right).
\tag{1.2}
\]

The \(O(H/m)\) term includes changing
\(\sqrt{m\log\log m}\) by the floor in \(H\). For the present \(H\),

\[
 {H^2\over m}
 =\log\log m+O(H/m)
\]

and the error in (1.2) is \(o(1/\log m)\). Hence

\[
 \log\lambda=\log\log m+o(1/\log m),
 \qquad
 \lambda=\log m+o(1).
\tag{1.3}
\]

It follows that

\[
 N={W\over\lambda}=(1+o(1)){W\over\log m}
\tag{1.4}
\]

and, exactly,

\[
 \rho N
 =(\lambda-\{\lambda\})N
 =W-\{\lambda\}N
 =W-o(W).
\tag{1.5}
\]

All asymptotic statements in this report are for sufficiently large
\(m\).

## 2. The signed rectangle incidence system

Let \(V\) be a finite family of oriented boundary orbits. Orbit \(v\)
has two states \(p_v^0,p_v^1\), oriented \(0\to1\), with collar and
middle differences

\[
 c_v=D_{\rm col}(p_v^1)-D_{\rm col}(p_v^0)\in L,
\qquad
 m_v=D_{\rm mid}(p_v^1)-D_{\rm mid}(p_v^0)\in L_0,
\tag{2.1}
\]

where \(L,L_0\) are free abelian target lattices. Reorienting orbit \(v\)
negates both vectors.

A physical two-top rectangle occurrence \(e\) touches distinct orbits
\(u,v\), with local directions
\(\epsilon_{u,e},\epsilon_{v,e}\in\{\pm1\}\). Its option column and
actions are

\[
 \widetilde d_e=\epsilon_{u,e}e_u+\epsilon_{v,e}e_v,
\tag{2.2}
\]

\[
 \epsilon_{u,e}c_u+\epsilon_{v,e}c_v=0,
\qquad
 \widetilde a_e=\epsilon_{u,e}m_u+\epsilon_{v,e}m_v.
\tag{2.3}
\]

Choose an endpoint listing \(e:u\to v\), and put

\[
 \alpha_e=\epsilon_{u,e},\qquad
 \sigma_e=-\epsilon_{u,e}\epsilon_{v,e}.
\tag{2.4}
\]

One must normalize the variable and action together:

\[
 d_e=\alpha_e\widetilde d_e=e_u-\sigma_e e_v,
\qquad
 a_e=\alpha_e\widetilde a_e=m_u-\sigma_e m_v.
\tag{2.5}
\]

If \(y_e\) is the physical coefficient, set \(x_e=\alpha_e y_e\).
Then \(d_ex_e=\widetilde d_ey_e\) and \(a_ex_e=\widetilde a_ey_e\).
For \(\alpha_e=-1\), physical bounds
\(\widetilde\ell_e\le y_e\le\widetilde u_e\) become

\[
                    -\widetilde u_e\le x_e\le-\widetilde\ell_e.
\tag{2.6}
\]

Thus (2.5) is not a formal sign change detached from the packet
multiplicity.

Let

\[
                         D_\Sigma=(d_e:e\in E).
\tag{2.7}
\]

Collar neutrality is now

\[
                              c_u=\sigma_e c_v.
\tag{2.8}
\]

### Theorem 2.1 (balance and exact Smith form)

Let \(K\) be a connected component of the loopless signed multigraph
underlying \(D_\Sigma\), with \(n_K\) vertices and \(q_K\) edges.

1. If one \(c_v\ne0\) on \(K\), then every signed cycle \(C\subseteq K\)
   is balanced:

   \[
                         \prod_{e\in C}\sigma_e=1.
   \tag{2.9}
   \]

2. If \(K\) is balanced, there is a gauge
   \(g_v\in\{\pm1\}\) such that

   \[
                             \sigma_{uv}=g_ug_v.
   \tag{2.10}
   \]

   After left multiplication by \(G=\operatorname{diag}(g_v)\), every
   column is, up to its ordinary orientation, \(e_u-e_v\). Hence the
   component is totally unimodular. Its rank is \(n_K-1\), its nonzero
   Smith factors are \(1^{n_K-1}\), and

   \[
    \operatorname{im}D_\Sigma[K]
       =\{b\in\mathbb Z^{V(K)}:g^Tb=0\},
   \tag{2.11}
   \]

   \[
    \operatorname{coker}D_\Sigma[K]\cong\mathbb Z,\qquad
    \operatorname{rank}\ker_{\mathbb Z}D_\Sigma[K]
       =q_K-n_K+1.
   \tag{2.12}
   \]

3. If \(K\) is unbalanced, its rank is \(n_K\), its Smith factors are

   \[
                              1^{n_K-1},2,
   \tag{2.13}
   \]

   and, after a spanning-tree gauge,

   \[
    \operatorname{im}D_\Sigma[K]
      =\left\{b\in\mathbb Z^{V(K)}:
      \sum_v b_v\equiv0\pmod2\right\}.
   \tag{2.14}
   \]

   Thus

   \[
    \operatorname{coker}D_\Sigma[K]\cong\mathbb Z/2,\qquad
    \operatorname{rank}\ker_{\mathbb Z}D_\Sigma[K]
      =q_K-n_K.
   \tag{2.15}
   \]

   In the seam-free collar system, such a component can occur only when
   all of its \(c_v\)'s vanish.

#### Proof

Transporting (2.8) around a cycle based at \(v\) gives

\[
                       c_v=\left(\prod_{e\in C}\sigma_e\right)c_v.
\]

If the sign product were \(-1\), then \(2c_v=0\). The lattice \(L\) is
torsion-free, so a nonzero collar excludes this. Connectivity and (2.8)
show that if one collar is nonzero, all are.

A signed graph is balanced exactly when signs can be written as
\(g_ug_v\). One obtains \(g\) by fixing a root and transporting signs
along a spanning tree; cycle balance makes this path-independent.
Equation (2.10) turns each column into an ordinary incidence column,
which proves total unimodularity, (2.11), and the balanced Smith data.

For an unbalanced component, gauge a spanning tree to ordinary
differences. The tree columns generate the zero-sum lattice. One
unbalanced chord becomes \(e_i+e_j\); modulo the tree lattice it is
twice a generator. This gives precisely the even-total lattice and the
Smith factor \(2\). The rank and kernel formulas follow. \(\square\)

A lone unbalanced cycle is not an integral circulation. Determinant-two
minors also mean that an unbalanced zero-collar bounded relaxation need
not be integral; for example the three columns

\[
                       e_1+e_2,\quad e_2+e_3,\quad e_3+e_1
\]

send \((1/2,1/2,1/2)\) to \((1,1,1)\), while no integral vector has
that image.

### Theorem 2.2 (exact bounded-flow cuts)

Suppose \(K\) is balanced. Consider

\[
 D_\Sigma x=b,\qquad \ell_e\le x_e\le u_e
\tag{2.16}
\]

with integral finite bounds. Let \(\widehat b=Gb\), orient each gauged
column \(Gd_e\) as an ordinary edge with tail coefficient \(+1\), and
write \(\delta^+(S),\delta^-(S)\) for edges leaving and entering
\(S\subseteq V(K)\). Then (2.16) is feasible iff, for every \(S\),

\[
 \ell(\delta^+(S))-u(\delta^-(S))
 \le \widehat b(S)
 \le
 u(\delta^+(S))-\ell(\delta^-(S)).
\tag{2.17}
\]

Whenever it is feasible, it has an integral solution.

#### Proof

Summing the ordinary incidence equations over \(S\) gives the two
necessary inequalities. For \(S=V(K)\), they include
\(\widehat b(V(K))=g^Tb=0\). After subtracting the lower bounds,
(2.17) is Hoffman's circulation criterion. The gauged incidence matrix,
together with bound rows, is totally unimodular, so every nonempty
integral bounded-flow polyhedron has an integral vertex. \(\square\)

Precisely, an additional endpoint color is harmless when there is a
homomorphism \(R:\mathbb Z^V\to A\) whose edge column is

\[
                              r_e=Rd_e.
\tag{2.18}
\]

Then every flow with divergence \(b\) has forced color total

\[
                              \sum_e r_ex_e=Rb.
\tag{2.19}
\]

This adds a compatibility equation, not an independent matrix row. An
arbitrary color row can destroy total unimodularity: appending
\((1,1,1)\) to the three incidence columns of a directed triangle gives
the minor

\[
 \begin{pmatrix}
 1&0&-1\\
 -1&1&0\\
 1&1&1
 \end{pmatrix},
\qquad\det=3.
\tag{2.20}
\]

Thus owner uniqueness, target capacities, independent tag
compatibility, port usage, prefix legality, and chronology rows require
a separate theorem.

## 3. Closed rectangle circulation is middle-null

Define the homomorphism

\[
 M_0:\mathbb Z^V\longrightarrow L_0,\qquad M_0e_v=m_v.
\tag{3.1}
\]

Equation (2.5) gives \(a_e=M_0d_e\). Therefore:

### Theorem 3.1 (boundary-orbit divergence determines all middle action)

For every normalized rectangle chain \(x\),

\[
                    \boxed{\Delta_{\rm mid}(x)=M_0D_\Sigma x.}
\tag{3.2}
\]

Consequently:

\[
 D_\Sigma x=0\quad\Longrightarrow\quad
 \Delta_{\rm mid}(x)=0,
\tag{3.3}
\]

and if \(D_\Sigma x=D_\Sigma x'\), then

\[
                 \Delta_{\rm mid}(x)=\Delta_{\rm mid}(x').
\tag{3.4}
\]

#### Proof

Sum \(a_e=M_0d_e\) with coefficients \(x_e\). \(\square\)

This is the exact answer to the per-top \(K_2\) cancellation proposal.
The network theorem in Section 2 can find integral rectangle flows with
a prescribed open divergence, subject to (2.17). It cannot use a closed
cycle to improve the middle displacement produced by that divergence.
Adding balanced cycles changes the representative \(x\), not its middle
action.

The statement is intentionally scoped. A three-top re-root packet, an
exterior-moving connector, a physical seam, an owner-capacity row, or a
queue voltage is not a two-endpoint rectangle column and is not ruled
out by (3.2).

## 4. Seam holonomy and the limit of coboundary arguments

Allow an oriented connector \(e:u\to v\) to have seam vector
\(s_e\in L\), with

\[
                         c_u-\sigma_ec_v+s_e=0.
\tag{4.1}
\]

Reverse traversal uses

\[
 \sigma_{\bar e}=\sigma_e,\qquad
 d_{\bar e}=e_v-\sigma_ee_u=-\sigma_ed_e,\qquad
 s_{\bar e}=-\sigma_es_e.
\tag{4.2}
\]

To re-express the same chain contribution one also sets
\(x_{\bar e}=-\sigma_ex_e\), with its interval of bounds transformed
by that sign.

For a traversed cycle

\[
 C=(v_0,e_0,v_1,\ldots,e_{t-1},v_t=v_0),
\]

first replace every oppositely stored edge by (4.2), and put

\[
 P_0=1,\qquad
 P_i=\prod_{j=0}^{i-1}\sigma_{e_j},\qquad P_C=P_t.
\tag{4.3}
\]

### Theorem 4.1 (exact signed seam holonomy)

\[
             \boxed{
             (1-P_C)c_{v_0}
             =-\sum_{i=0}^{t-1}P_i s_{e_i}.}
\tag{4.4}
\]

In particular, a balanced cycle has zero transported seam holonomy,
while an unbalanced cycle has

\[
                         \sum_iP_i s_{e_i}=-2c_{v_0}.
\tag{4.5}
\]

#### Proof

Multiply the \(i\)-th instance of (4.1) by \(P_i\). Since
\(P_{i+1}=P_i\sigma_{e_i}\), the collar terms telescope. \(\square\)

There is a second scope distinction. If \(\mathscr X\) is the graph of
complete literal states and \(F:\mathscr X\to A\) is a state potential,
then

\[
                         \lambda_F(e)=F(t(e))-F(s(e))
\tag{4.6}
\]

is an endpoint coboundary. Its sum on a chain depends only on the chain
boundary. This applies to a deck, tag, ordered port, or queue coordinate
only when that object is literally part of the endpoint state.

It does not apply automatically to connector length, seam-crossing
occurrence counts, queue-arc usage, port-use census, or an independently
assigned voltage. An abelian voltage vanishes only when the lifted sheet
also closes; a nonabelian voltage obeys an ordered product. Thus the
trace-null four-top Johnson square is an open state move
\(X\to S(X)\), not a closed physical chronology merely because its
provider-forgotten collars cancel.

## 5. Short retained segments force growing re-root cycles

Let \(U\) be an \(M\)-set and let
\(p:\mathbb Z/M\mathbb Z\to U\) be a cyclic bijective word. For retained
phase starts \(1,\ldots,\rho\), define the signed depth-\(s\) trace

\[
 \mathcal T_s^{(\rho)}(U,p)
 =\sum_{j=1}^{\rho}
 e_{\,U\setminus\{p_{j+s},p_{j+s+1},\ldots,p_{j+H-1}\}},
 \qquad -H\le s\le H.
\tag{5.1}
\]

Empty intervals at \(s=H\) are allowed. Let \(Sp\) be the one-step left
re-root, \((Sp)_j=p_{j+1}\). Direct cancellation of consecutive phase
starts gives

\[
 \mathcal T_s^{(\rho)}(U,Sp)-\mathcal T_s^{(\rho)}(U,p)
 =e_{E_s}-e_{A_s},
\tag{5.2}
\]

where

\[
 A_s=U\setminus\{p_{1+s},\ldots,p_H\},
\qquad
 E_s=U\setminus\{p_{\rho+1+s},\ldots,p_{\rho+H}\}.
\tag{5.3}
\]

Thus a short re-root has no bulk derivative, but its entrance and exit
\(2H\)-collars overlap.

### Theorem 5.1 (short-segment collar-cycle lower bound)

Let

\[
 H\ge1,\qquad 1\le\rho<2H,\qquad M\ge2H+\rho,\qquad t\ge2.
\tag{5.4}
\]

Take cyclically indexed \((M-1)\)-sets \(B_i\) with
\(|B_i\triangle B_{i+1}|=2\), and write

\[
 x_i\in B_{i+1}\setminus B_i,\qquad
 y_i\in B_i\setminus B_{i+1},
\]

\[
 U_i=B_i\cup B_{i+1}
     =B_i\mathbin{\dot\cup}\{x_i\}
     =B_{i+1}\mathbin{\dot\cup}\{y_i\}.
\tag{5.5}
\]

Suppose \(p_i\) is a cyclic bijective word on \(U_i\), and
\(C_i\) is an ordered \((2H-1)\)-tuple of distinct elements of \(B_i\),
with \(C_{i+t}=C_i\). Assume one nonwrapping chart of \(p_i\) has

\[
 (p_i(1-H),\ldots,p_i(H))=(C_i,x_i),
\tag{5.6}
\]

\[
 (p_i(\rho+1-H),\ldots,p_i(\rho+H))=(C_{i+1},y_i).
\tag{5.7}
\]

For \(-H\le s\le H-1\), these are exactly the entrance/exit collar
identifications used to telescope (5.2) seam by seam. At \(s=H\),
\(A_H=E_H=U_i\), so every carrier derivative is already zero. Then

\[
                              \boxed{t\rho\ge2H.}
\tag{5.8}
\]

#### Proof

The position intervals in (5.6) and (5.7) are translates by \(\rho\).
Their overlap has length \(L=2H-\rho\). Literal consistency of the
single word \(p_i\) gives

\[
 \operatorname{suf}_{L}(C_i,x_i)
 =
 \operatorname{pre}_{L}(C_{i+1},y_i).
\tag{5.9}
\]

Since \(L\le2H-1\), the right side lies entirely inside \(C_{i+1}\).
Hence \(x_i\) occurs in position \(2H-\rho\) of \(C_{i+1}\).

Inductively, whenever \(a\rho<2H\), the same \(x_i\) occurs in position
\(2H-a\rho\) of \(C_{i+a}\). Indeed, if
\((a+1)\rho<2H\), the current position exceeds \(\rho\), lies in the
overlap suffix in (5.9), and moves left by \(\rho\) in the next collar.

If \(t\rho<2H\), set \(a=t\). Since \(C_{i+t}=C_i\), this puts
\(x_i\) inside \(C_i\subseteq B_i\), contradicting
\(x_i\notin B_i\). \(\square\)

The theorem is a necessary condition for this exact overlapping-collar
facet-cycle mechanism, not a sufficiency theorem for arbitrary
exterior-moving connectors. At the reduced scale, (1.3) turns (5.8)
into (0.5). In particular, a fixed four-top square is unavailable.

## 6. The ordered queue convention

An \(H\)-transition safe arc

\[
                         (X_0,X_1,\ldots,X_H)
\tag{6.1}
\]

contains \(H+1\) owners and \(H\) Johnson transitions. Its de Bruijn
prefix and suffix overlap states contain \(H\) owners but only \(H-1\)
transitions:

\[
 (X_0,\ldots,X_{H-1}),\qquad (X_1,\ldots,X_H).
\tag{6.2}
\]

This is the relevant off-by-one. Physical \(H\)-window safety forbids
inserting any of the preceding \(H-1\) departures and, dually, forbids
deleting any of the preceding \(H-1\) arrivals. A move exactly \(H\)
transitions old may be reversed.

A raw top-recovering history may nevertheless record \(H\) transitions:

\[
 Q_t^-=(X_t;i_{t-H+1},\ldots,i_t;
             d_{t-H+1},\ldots,d_t),
\tag{6.3}
\]

where \(X_s=X_{s-1}-d_s+i_s\). Under \(H\)-geodesicity,

\[
 U_t=X_t\mathbin{\dot\cup}
 \{d_{t-H+1},\ldots,d_t\}.
\tag{6.4}
\]

Equality of raw past-history states (6.3) fixes the carrier top.
Equality of the overlap history (6.2) fixes only an
\((m+H-1)\)-facet and may leave two different exclusive top labels.
Conversely, a queue automaton that forbids reversing all \(H\) recorded
moves is one step too strong. An \(O\)-step in the macro below can
reinsert its departure exactly \(H\) moves later. This is physically
\(H\)-window safe even though it is not an arc of that overbuffered
automaton.

### Corollary 6.1 (correct physical queue degree)

From a raw past-history state \(Q_t^-\), a legal next transition
\(X_t\to X_t-d+i\) has

\[
 d\in X_t\setminus\{i_{t-H+2},\ldots,i_t\},
\qquad
 i\in X_t^c\setminus\{d_{t-H+2},\ldots,d_t\}.
\tag{6.5}
\]

Hence the exact indegree and outdegree of the minimally buffered
physical queue lift are

\[
                              \boxed{(m-H+1)^2.}
\tag{6.6}
\]

#### Proof

Each forbidden list in (6.5) has \(H-1\) distinct elements in the
appropriate side of \(X_t\). The oldest recorded move is eligible to be
reversed, so each choice set has size \(m-H+1\). The two choices are
independent. Reversing time proves the same indegree. \(\square\)

This corrects the degree \((m-H)^2\) of the earlier overbuffered
automaton; that automaton excluded one physically legal age-\(H\)
reversal.

## 7. Exact ordered-slot/FIFO-zero-monodromy re-root cycles

Let \(r\ge1\). An ordered state is

\[
 \Sigma=(Q^+=(q_0,\ldots,q_{H-1});
         P=(p_0,\ldots,p_{m-1});
         E=(e_0,\ldots,e_{k-1})).
\tag{7.1}
\]

Here \(Q^+\) is the list of the next \(H\) arrivals. It is not the raw
past-history state \(Q_t^-\) in (6.3).

Define

\[
 O\Sigma=
 (q_1,\ldots,q_{H-1},p_0;\
  p_1,\ldots,p_{m-1},q_0;\
  E),
\tag{7.2}
\]

\[
 S\Sigma=
 (q_1,\ldots,q_{H-1},e_0;\
  p_1,\ldots,p_{m-1},q_0;\
  e_1,\ldots,e_{k-1},p_0).
\tag{7.3}
\]

Both make the same middle-owner transition

\[
                           P\longmapsto P-p_0+q_0.
\tag{7.4}
\]

The map \(O\) keeps the root set \(E\) fixed, whereas \(S\) performs the
FIFO re-root \(E-e_0+p_0\). Put \(F_r=S\circ O^{r-1}\).

### Lemma 7.1 (every \(O/S\) chronology is locally \(H\)-geodesic)

For any word in \(O,S\), every \(H\) consecutive middle-owner
transitions form a Johnson geodesic.

#### Proof

The three lists \(Q,P,E\) remain a disjoint ordered partition of
\([2m]\). Starting at any time, both maps update \(P\) by deleting its
first entry, shifting left, and appending the first entry of \(Q\).
Because \(H\le m\), the next \(H\) departures are the first \(H\)
entries of the initial \(P\), regardless of the \(O/S\) choices.
Likewise, both maps delete the first entry of \(Q\), shift left, and
append one new entry; hence the next \(H\) arrivals are exactly the
initial \(H\) entries of \(Q\). These two lists are disjoint and each
has distinct entries. Therefore the \(H\)-transition walk has \(H\)
distinct departures, \(H\) distinct arrivals, and no arrival is later
deleted inside the block. This is precisely Johnson geodesicity.
\(\square\)

Order the \(\ell\) top slots cyclically by

\[
 u_0=Q_0,\quad
 u_1,\ldots,u_m=P_{m-1},\ldots,P_0,\quad
 u_{m+1},\ldots,u_{\ell-1}=Q_{H-1},\ldots,Q_1.
\tag{7.5}
\]

Then \(O\) sends \(u_i\) to \(u_{i+1}\). Relative to rotation by \(r\),
\(F_r\) replaces the arrow

\[
                         u_{m-r+1}\longrightarrow u_{m+1}
\tag{7.6}
\]

(indices modulo \(\ell\)) by the path through all \(E\)-slots. The
often-written arrow \(u_m\to u_{m+1}\) is correct only for \(r=1\).

### Theorem 7.1 (complete fixed-macro monodromy)

Let

\[
                          g=\gcd(\ell,r),\qquad s_0=\ell/g.
\tag{7.7}
\]

The slot cycles of \(F_r\) have lengths

\[
                   s_0+k\quad\hbox{once},\qquad
                   s_0\quad\hbox{\(g-1\) times}.
\tag{7.8}
\]

The root set first returns after \(s_0+k\) blocks. At that time the full
ordered state has returned iff

\[
                          g=1\quad\hbox{or}\quad s_0\mid k.
\tag{7.9}
\]

If \(1\le r<\ell/(2H)\), then, for all sufficiently large \(m\), this
is equivalent to \(\gcd(\ell,r)=1\). In particular this applies to
\(r=\rho\) and \(r=\rho+1\).

#### Proof

Rotation by \(r\) on the \(\ell\) top slots has \(g\) cycles, each of
length \(s_0\). The splice (7.6) inserts all \(k\) exterior slots into
one rotation cycle and leaves the other \(g-1\) cycles unchanged. This
proves (7.8). The splice places the \(k\) exterior/root slots as one
nonempty proper consecutive interval of the long cycle. No nonzero
rotation of a cycle preserves such an interval, so their set first
returns after the full length \(s_0+k\). Every short top cycle has then
returned iff \(s_0\mid(s_0+k)\), equivalently \(s_0\mid k\); if \(g=1\),
there is no short cycle.

Under \(r<\ell/(2H)\), since \(g\le r\),

\[
                         s_0={\ell\over g}\ge{\ell\over r}>2H.
\]

If \(s_0\mid\ell\) and \(s_0\mid k\), then
\(s_0\mid(\ell-k)=2H\), a contradiction. \(\square\)

When \(g=1\), all \(2m=\ell+k\) slots form one cycle. The exterior root
positions form a consecutive \(k\)-block, so the successive roots are
the \(2m\) cyclic consecutive \(k\)-windows of one coordinate order.
The chronology consists of \(2m\) \(F_r\)-blocks, hence \(2mr\)
elementary transitions. It closes the physical ordered state and is
\(H\)-window safe by Lemma 7.1.

This is a literal owner/root/queue trajectory, but it is not by itself
an authorized all-target packet or a factor of the even middle layer.
In general \(2m\nmid W\), and the frozen odd-ground-set middle-wreath
theorem cannot be invoked after the infinity cut without an additional
completion. External tag/voltage closure and all target capacities
remain separate requirements.

## 8. Adjacent block lengths do not close one top-slot lap

Let \(R=O\) on the top slots, fixing \(E\), and put

\[
                              T=SR^{-1},\qquad F_a=TR^a.
\tag{8.1}
\]

For positive block lengths \(a_0,\ldots,a_{K-1}\), set
\(A=\sum_i a_i\) and \(T_x=R^xTR^{-x}\). A direct collection of the
rotations gives

\[
\begin{aligned}
 P(\mathbf a)
 &=F_{a_{K-1}}\cdots F_{a_0}\\
 &=T_0T_{a_{K-1}}
   T_{a_{K-1}+a_{K-2}}\cdots
   T_{a_{K-1}+\cdots+a_1}R^A.
\end{aligned}
\tag{8.2}
\]

### Theorem 8.1 (one-lap mixed-length obstruction)

If every \(a_i>0\), \(K>0\), and \(A=\ell\), then

\[
                         P(\mathbf a)\ne1,\qquad
                         P(\mathbf a)E\ne E.
\tag{8.3}
\]

#### Proof

The suffix anchors in (8.2) are distinct modulo \(\ell\): their integer
representatives strictly increase between \(0\) and \(\ell-1\).
List the corresponding slots \(X_1,\ldots,X_K\) in the
right-to-left application order of the anchored factors in (8.2).
Since \(R^\ell=1\), those factors act on the ordered list

\[
                         (E_0,\ldots,E_{k-1},X_1,\ldots,X_K)
\tag{8.4}
\]

as left rotation by \(K\), fixing all other top slots. This is
nonidentity. The \(E\)-slots are a nonempty proper cyclic interval in
(8.4), so a nonzero rotation does not preserve their set. \(\square\)

For the internal one-lap stride remainder, write

\[
                          \ell=q\rho+\eta,\qquad0\le\eta<\rho.
\tag{8.5}
\]

If \(\eta>0\), use \(K=q\), with \(\eta\) blocks of length \(\rho+1\)
and \(q-\eta\) of length \(\rho\). If \(\eta=0\), use \(K=q-1\), with
\(\rho\) long and \(q-1-\rho\) short blocks. For large \(m\), all
displayed counts are nonnegative and \(0<K<k\). Every ordering fails
root closure by Theorem 8.1. This is not the global owner-floor
remainder \(W-\rho N\). Multiple laps and correlated componentwise floor
schedules are not ruled out; they must solve the full noncommutative
equation (8.2), not merely a gcd or total stride condition.

## 9. Root packing, owner completion, and the invariant fibre

### Proposition 9.1 (exact root and owner singleton marginals)

Let \(\mathcal C\) be a multiset of \(c\) closed cycles from Section 7,
where cycle \(i\) may use its own \(r_i\) satisfying
\(\gcd(\ell,r_i)=1\). Count the \(2m\) block-start roots of every cycle,
and count all \(2mr_i\) middle-owner states within cycle \(i\). Block
and phase indices are cyclic; phases are \(0,\ldots,r_i-1\), and the
terminal state equal to the initial state is not counted a second time.

Then every coordinate occurs in exactly

\[
                              kc
\tag{9.0a}
\]

of the root occurrences, and in exactly

\[
                              m\sum_{i=1}^{c}r_i
\tag{9.0b}
\]

of the middle-owner occurrences. In particular, if the root cycles are
pairwise root-disjoint and leave \(z=N-2mc\) roots unused, then the
root leave is coordinate-regular of degree

\[
                              {kz\over2m},
\qquad\hbox{so}\qquad
                              2m\mid kz.
\tag{9.0c}
\]

If all selected middle owners are distinct and leave

\[
                              d=W-2m\sum_i r_i
\tag{9.0d}
\]

middle sets unused, then the owner leave is coordinate-regular of degree
\(d/2\).

#### Proof

In one interval-wreath cycle, the \(2m\) roots are all cyclic
consecutive \(k\)-windows of one coordinate order. A fixed coordinate
belongs to exactly \(k\) of them, proving (9.0a).

Fix a within-block phase \(0\le j<r_i\). As the \(2m\) block starts run
around cycle \(i\), the \(2m\)-cycle \(F_{r_i}\) sends each coordinate
through every ordered slot exactly once. After applying the fixed
within-block prefix \(O^j\), the middle-owner positions are still a
fixed set of \(m\) slots. Hence every coordinate occurs in exactly
\(m\) owners at phase \(j\), and therefore in \(mr_i\) owners on the
whole cycle. Summing cycles proves (9.0b).

The complete \(k\)-uniform root layer has coordinate degree
\(\binom{2m-1}{k-1}=kN/(2m)\). Subtracting \(kc\) proves (9.0c).
The complete middle layer has coordinate degree \(W/2\); subtracting
(9.0b) proves the final assertion. \(\square\)

Thus scalar owner count is not the whole completion condition: any
leave used by an absorber must have these exact singleton marginals.
Conversely, whole ordered cycles introduce no singleton-marginal bias;
the unresolved obstruction starts at distinct-owner selection, higher
target profiles, ordered voltage, and—when only the narrow
rectangle/three-top library is used—the column-histogram fibre.

For every fixed admissible \(r\), retain orientation on the coordinate
cycles. The resulting oriented interval-wreath root catalogue has the
separately audited exact root degree

\[
                              D_R=k!\ell!
\tag{9.1}
\]

and maximum relative root-pair codegree

\[
                              {2\over k\ell}.
\tag{9.2}
\]

If a cycle and its reverse are identified as one simple hyperedge, the
degree in (9.1) is divided by \(2\); the relative pair-codegree bound
(9.2) is unchanged.

These are favorable fractional data. They do not by themselves prove a
near-perfect integral matching when each selected object must also carry
its \(2mr\) middle-owner occurrences, all prefix targets, and its ordered
queue state. Moreover, the scalar floor alignment is automatic for this
fixed catalogue only when \(r=\rho\) and
\(\gcd(\ell,\rho)=1\). The \(r=1\), \(\rho\)-clone alternative and any
multi-\(r\) mixture still require distinct-owner and root-capacity
completion.

Conditionally, suppose the selected physical family has
\(N-o(N)\) reduced-scale root blocks and its \(W-o(W)\) principal
middle-owner occurrences are globally pairwise distinct, both within
and across cycles. If an exact physical circulation joins the root
blocks into \(C\) components, the standard literal compiler has the
upper bound

\[
 L_{\rm word}
 \le T+2HC+K_{\rm conn}+\mathfrak H,
\tag{9.3}
\]

where \(T=(1+o(1))W\), \(K_{\rm conn}\) is the installed connector
length, and \(\mathfrak H\) is the complete residual target-hole ledger.
Thus that compiler certifies coefficient one if

\[
                    {N\over C}=\omega(H/\rho),
\quad
 K_{\rm conn}+\mathfrak H=o(W).
\tag{9.4}
\]

Equation (9.4) is a sufficient condition for this compiler, not a
universal lower bound on every possible word construction.
Conditionally, a compatible root near-factor by \(2m\)-block cycles
would have \(C\sim N/(2m)\), and its opening-collar term would be

\[
                         O(HN/m)=o(W).
\tag{9.5}
\]

There is an additional exact state-fibre restriction for the narrow
certified library. For rooted position \(j\) and coordinate label \(v\),
let

\[
 C_{j,v}
 =\#\{U:\hbox{the current rooted word on }U
          \hbox{ has label }v\hbox{ in position }j\}.
\tag{9.6}
\]

Every certified two-top rectangle merely swaps the two participating
labels in its two active columns, and every certified three-top re-root
packet cyclically permutes the same three labels in each of its two
active columns. Hence the entire matrix \((C_{j,v})\) is invariant under
both move families.

Therefore independently built root-cycle or owner factors cannot be
connected by that two-top/three-top library unless their endpoint tables
lie in the same column-histogram fibre.

This restriction is not universal. For a simultaneous facet-cycle
re-root \(p_i\mapsto Sp_i\), define

\[
                         A_{j,v}=\#\{i:p_i(j)=v\}.
\tag{9.7}
\]

Its exact column derivative is

\[
                         \Delta C_{j,v}=A_{j+1,v}-A_{j,v}.
\tag{9.8}
\]

Indeed, after a left shift, the label occupying column \(j\) is the old
label in column \(j+1\). For the four-top Johnson square this derivative
cannot vanish identically when \(\ell>4\): otherwise \(A_{j,v}\) would be
independent of \(j\), and summing over columns would give

\[
                         r_v=\ell A_{j,v},
\tag{9.9}
\]

where every label appearing in the four carriers has
\(1\le r_v\le4<\ell\). This is impossible. Thus the certified trace-neutral
four-top shift genuinely leaves the column-histogram fibre. General
facet-cycle shifts may do the same; their column divergence must be
balanced globally rather than silently set to zero.

The completion gate therefore has two branches. A chronology generated
only by the two-top/three-top library must remain in one common fibre.
A growing histogram-changing re-root circulation may escape that fibre,
but must account explicitly for (9.8), global owner simplicity, every
target-capacity row, queue voltage, and chronology. Abstract top support
alone resolves neither branch.

## 10. Exact implication boundary

Proved here:

1. the complete signed-incidence normalization of the collar-neutral
   rectangle system;
2. automatic balance on every nonzero-collar component;
3. exact balanced and unbalanced Smith forms;
4. exact Hoffman cuts and integral bounded flows on balanced components;
5. the middle coboundary identity (3.2), which closes the pure closed
   rectangle-circulation route;
6. the seam holonomy equation (4.4) and the precise scope of endpoint
   telescoping;
7. the short-segment lower bound \(t\rho\ge2H\);
8. the ordered \(O/S\) fixed-macro monodromy classification;
9. the one-lap mixed-\(\rho/(\rho+1)\) obstruction;
10. the exact coordinate-regular root and owner marginals of every
    closed gcd-one \(F_r\) cycle; and
11. the reduced-scale scalar and collar ledgers with all floor terms.

Imported from independently audited companion reports and used with
their exact scope:

1. the interval-wreath root degree \(k!\ell!\) and relative codegree
   \(2/(k\ell)\);
2. the \((C_{j,v})\) invariant for the certified rectangle and
   three-top re-root libraries; and
3. dense abstract Johnson top support.

Not proved:

1. an arithmetic-compatible near-perfect integral matching of genuine
   ordered-slot/FIFO-zero-monodromy interval-wreath cycles;
2. simultaneous exact middle-owner completion of such a matching;
3. all-depth target capacity and literal Hall completion;
4. a multi-lap solution of (8.2) with owner and queue constraints;
5. global cancellation and physical installation of the column
   divergence (9.8) for growing facet-cycle packets; or
6. the coefficient-one contiguous-OR theorem.

One sufficient surviving gate is consequently:

> Construct an owner-simple, target-capacitated,
> ordered-slot/FIFO-zero-monodromy integral section of the ordered
> interval-wreath catalogue whose components contain on average
> \(\omega(H/\rho)\) reduced-scale root blocks. Either keep the whole
> selection in one column-histogram fibre using the narrow certified
> library, or cancel the explicit histogram divergence (9.8) in a
> growing facet-cycle circulation. Include all external voltage and
> target rows.

Balanced rectangle circulation alone cannot decide this gate. It gives
network integrality on balanced components; independently, every closed
rectangle flow, balanced or unbalanced, is middle-null.
