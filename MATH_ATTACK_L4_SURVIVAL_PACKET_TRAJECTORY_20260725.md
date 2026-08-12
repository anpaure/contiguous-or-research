# Fourth-wave lane L: survival-packet trajectories, kinetic duality, and alternating Hall

Date: 2026-07-25

Method: pure mathematics only. No web search, finite search, random
experiment, solver, or computational enumeration was used.

## 0. Outcome

This report does **not** prove the fractional survival-packet theorem,
cyclic alignment, MWB, or the final contiguous-OR theorem. It proves an
exact dynamic reduction for fixed-star twin fibres, an exact kinetic
packet-packing dual for arbitrary finite exact-factor trajectories, a sharp
merge with the alternating-reservoir lemma, and a positive-density dual
obstruction around the canonical MSW factor.

The principal new positive theorem is this.

> **Path-union theorem.** On a monotone fixed-star twin trajectory, project
> every state-labelled survival packet to the common set of star traces and
> take their union. A slowly moving sequence of fractional packet covers is
> equivalent, up to the fixed packet-rank constant, to one static cover of
> this path-union hypergraph. Its exact dual is a packing of state-labelled
> packets with unit trace congestion.

If \(\Theta_{\rm path}\) is that static cover value, then

\[
\Theta_{\rm path}
\le M_\infty+V,
\tag{0.1}
\]

where

\[
M_\infty=\max_j\|x^{(j)}\|_1,
\qquad
V=\sum_j\|x^{(j)}-x^{(j-1)}\|_1.
\]

Conversely, one path-union cover of mass \(\Theta_{\rm path}\) gives

\[
M_\infty=\Theta_{\rm path},
\qquad
V\le2\Theta_{\rm path}
\tag{0.2}
\]

on a monotone path. Since every survival packet has rank at most
\(R_A=O_A(1)\), the following four target-scale statements are equivalent:

1. \(M_\infty+V=o_A(t/\sqrt m)\);
2. \(\Theta_{\rm path}=o_A(t/\sqrt m)\);
3. one trace set of size \(o_A(t/\sqrt m)\) meets every projected packet at
   every visited state;
4. the corresponding physical exceptional wreath families are quota-safe
   at every state and have total recourse \(o_A(t/\sqrt m)\).

Here \(t=\operatorname{Cat}_m\), and old and new twin wreaths are different
physical LP vertices. A changed trace of weight \(a\) contributes exactly
\(2a\), not zero, to physical \(\ell^1\) movement.

For fixed quotas and \(s\) distinct changed traces,

\[
\boxed{
\vartheta(F_0,\beta)
\le\Theta_{\rm path}
\le\vartheta(F_0,\beta)+s.
}
\tag{0.3}
\]

Thus a target-small base cover plus
\(s=o_A(t/\sqrt m)\) changed traces gives the requested slowly moving
trajectory. This is a stability theorem, not a construction of the base
cover or of useful twin cycles.

The exact negative theorem is equally sharp. Let

\[
C_m=\operatorname{Cat}_{m-4}
=\left(\frac1{256}+O(m^{-1})\right)t.
\]

The audited canonical disjoint-packet packing implies that a trajectory
starting at the canonical MSW factor has initial cover mass at least
\(C_m\). If it ends with target-small cover mass, its total fractional
movement is at least

\[
C_m-o_A(t/\sqrt m)=\Omega(t).
\tag{0.4}
\]

Its exact-factor edit length is also at least this large. Inside the native
\((2\,3)\)-component cube, a target-small state must lie at row distance at
least

\[
2C_m-o_A(t/\sqrt m)
=\left(\frac1{128}-o(1)\right)t.
\tag{0.5}
\]

This is a genuine dual packing obstruction to every subcritical
twin-switch search from the canonical basin. It is not factor-independent:
an audited exact factor at distance \(2C_m\) eliminates the displayed
canonical resource family after a compatible quota choice.

Finally, the packet and alternating-reservoir theories merge more strongly
than at the previous scale. If an integral packet cover \(B\) has

\[
|B|=o_A(t/\sqrt m),
\]

and the alternating directed cuts can be satisfied using only middle owners
in the rows \(B\), then no bounded-component or short-path hypothesis is
needed:

\[
\boxed{
\sum_{q\le K_A}\frac{T_q}{c_q}
\le n|B|\sum_{q\le K_A}\frac1{c_q}
=o_A(W).
}
\tag{0.6}
\]

Once a target-small common trace cover has been constructed, the remaining
merger step is support-feasible higher-order Hall plus adjacent-time
alternation inside the small exceptional wreath rows. Constructing that
cover and a useful exact twin basin remain independent open problems. The
survival-packet LP does not imply the target-family cuts.

## 1. Fixed-window normalization and explicit constants

Put

\[
n=2m+1,\qquad
W=\binom nm,\qquad
t=\frac Wn=\operatorname{Cat}_m,
\qquad
K=K_A=\lceil A\sqrt m\rceil.
\tag{1.1}
\]

At depth \(q\), write

\[
N_q=\binom n{m-q},
\qquad
\lambda_q=\frac W{N_q},
\qquad
c_q=\lfloor\lambda_q\rfloor.
\tag{1.2}
\]

The exact ratio is

\[
\lambda_q
=\prod_{i=0}^{q-1}
\left(1+\frac{2(i+1)}{m-i}\right).
\tag{1.3}
\]

Fix \(A\) before letting \(m\to\infty\). If
\(m\ge4(A+1)^2\), then \(K\le(A+1)\sqrt m\), and for \(q\le K\),

\[
\log\lambda_q
\le\sum_{i=0}^{q-1}\frac{2(i+1)}{m-i}
\le\frac{q(q+1)}{m-q+1}
\le2(A+1)(A+2).
\tag{1.4}
\]

Hence the explicit safe constants

\[
C_A:=\left\lceil e^{\,2(A+1)(A+2)}\right\rceil,
\qquad
R_A:=C_A+2
\tag{1.5}
\]

satisfy

\[
1\le c_q\le C_A,
\qquad
|P|\le R_A
\tag{1.6}
\]

for every survival packet \(P\) in the window. Also

\[
S_A(m):=\sum_{q=1}^{K}\frac1{c_q}
\le K\le(A+1)\sqrt m.
\tag{1.7}
\]

The sharper audited asymptotic is

\[
S_A(m)
=\left(s_A+o_A(1)\right)\sqrt m,
\qquad
s_A=\int_0^A\frac{dx}{\lfloor e^{x^2}\rfloor}.
\tag{1.8}
\]

No assertion below is uniform for \(A=A(m)\to\infty\).

For an exact factor \(F\), a balanced quota system is

\[
\beta_q(S)\in\{c_q,c_q+1\},
\qquad
\sum_S\beta_q(S)=W.
\tag{1.9}
\]

Let

\[
\mathcal O_F(q,S)
=\{E\in F:E\text{ owns }S
\text{ as a cyclic }(m-q)\text{-interval}\}.
\tag{1.10}
\]

A survival packet for \(a=(q,S)\) is a set

\[
P\subseteq\mathcal O_F(q,S),
\qquad
|P|=\beta_q(S)+1.
\tag{1.11}
\]

The audited equivalence says that \(B\subseteq F\) is an integral packet
cover if and only if

\[
\mu_q^{F\setminus B}(S)\le\beta_q(S)
\qquad(q\le K,\ S).
\tag{1.12}
\]

The fractional packet-cover value is

\[
\vartheta(F,\beta)
=\min\left\{
\sum_{E\in F}x_E:
x_E\ge0,\ 
\sum_{E\in P}x_E\ge1
\text{ for every packet }P
\right\}.
\tag{1.13}
\]

Weights may be truncated to \([0,1]\). Thresholding at \(1/R_A\) gives an
integral packet cover of size at most \(R_A\|x\|_1\).

Throughout this report “slowly moving” uses the audited recourse
normalization

\[
M_\infty=\max_j\|x^{(j)}\|_1,
\qquad
V=\sum_{j=1}^T
\|x^{(j)}-x^{(j-1)}\|_1.
\tag{1.14}
\]

If “total mass” is instead interpreted literally as
\(\sum_j\|x^{(j)}\|_1\), a common cover contributes
\((T+1)\Theta_{\rm path}\). Between two fixed-star fibre states all
differing cycle bits may be switched simultaneously, so an endpoint path
can be batched to two states and this holding factor becomes two.

## 2. The fixed-star path-union packet LP

Fix a coordinate \(v\) and a fixed family \(\mathcal T\) of
\(P_v\)-traces. Exact states in this star fibre choose one of the two
unoriented lifts of every trace, subject to the directed
\(\phi\)-cycle conservation law. Exactness makes trace projection
injective: two rows with the same trace would share all \(m\) middle targets
of that trace.

Let

\[
F_0,F_1,\ldots,F_T
\tag{2.1}
\]

be a finite trajectory of exact states in this fixed fibre. For each time
\(j\), let

\[
e_j:\mathcal T\longrightarrow F_j
\tag{2.2}
\]

be the active-lift bijection. Quotas \(\beta^{(j)}\) may vary for now.
Project every state-\(j\) packet \(P\subseteq F_j\) to

\[
\widehat P=e_j^{-1}(P)\subseteq\mathcal T,
\tag{2.3}
\]

retaining state and resource labels on parallel copies. Let
\(\mathcal H_{\rm path}\) be the union of all these projected packets, and
define

\[
\Theta_{\rm path}
=\min\left\{
\sum_{\tau\in\mathcal T}w_\tau:
w_\tau\ge0,\ 
\sum_{\tau\in Q}w_\tau\ge1
\quad(Q\in\mathcal H_{\rm path})
\right\}.
\tag{2.4}
\]

### Theorem 2.1 — exact trace-path reduction

Let \(x^{(j)}\) be arbitrary fractional packet covers of the physical
state hypergraphs, extended by zero to
\(\bigcup_jF_j\). Then

\[
\boxed{
\Theta_{\rm path}
\le
\max_j\|x^{(j)}\|_1
+\sum_{j=1}^T
\|x^{(j)}-x^{(j-1)}\|_1.
}
\tag{2.5}
\]

Conversely, let \(w\) cover \(\mathcal H_{\rm path}\), and define

\[
x^{(j)}_{e_j(\tau)}=w_\tau,
\qquad
x^{(j)}_E=0\quad(E\notin F_j).
\tag{2.6}
\]

Then every \(x^{(j)}\) is a packet cover,

\[
\|x^{(j)}\|_1=\|w\|_1,
\tag{2.7}
\]

and the exact physical movement identity is

\[
\boxed{
\|x^{(j)}-x^{(j-1)}\|_1
=2\sum_{\tau:e_j(\tau)\ne e_{j-1}(\tau)}w_\tau.
}
\tag{2.8}
\]

If the path is monotone, meaning every \(\phi\)-cycle bit and hence every
trace changes at most once, then

\[
\sum_j\|x^{(j)}-x^{(j-1)}\|_1
\le2\|w\|_1.
\tag{2.9}
\]

#### Proof

For the forward direction, put

\[
z_j(\tau)=x^{(j)}_{e_j(\tau)},
\qquad
w_\tau=\max_j z_j(\tau).
\tag{2.10}
\]

Every projected packet \(Q=e_j^{-1}(P)\) obeys

\[
\sum_{\tau\in Q}w_\tau
\ge\sum_{\tau\in Q}z_j(\tau)
=\sum_{E\in P}x^{(j)}_E
\ge1,
\]

so \(w\) covers \(\mathcal H_{\rm path}\).

For one scalar sequence,

\[
\max_jz_j
\le z_0+\sum_{j=1}^T(z_j-z_{j-1})_+.
\tag{2.11}
\]

If the active lift of \(\tau\) is unchanged at transition \(j\), its
positive scalar increment is at most the physical atom movement. If the
lift changes, the old and new wreath atoms are distinct, and their movement
contribution is

\[
z_{j-1}(\tau)+z_j(\tau)
\ge(z_j(\tau)-z_{j-1}(\tau))_+.
\]

Summing (2.11) over traces proves (2.5).

For the converse, packet coverage follows immediately from the definition
of the projected hypergraph. An unchanged trace contributes no movement.
A changed trace removes one physical atom of weight \(w_\tau\) and inserts
another physical atom of the same weight, giving exactly \(2w_\tau\).
This proves (2.7)--(2.8), and monotonicity gives (2.9). \(\square\)

### 2.1 Bounded-rank collapse to one common trace set

The path-union hypergraph has rank at most \(R_A\). Threshold an optimal
\(w\) at \(1/R_A\):

\[
C=\{\tau:w_\tau\ge1/R_A\}.
\tag{2.12}
\]

Then

\[
|C|\le R_A\Theta_{\rm path},
\tag{2.13}
\]

and \(C\) meets every projected packet. Put

\[
B_j=e_j(C)\subseteq F_j.
\tag{2.14}
\]

By exact packetization, every \(B_j\) is quota-safe. On a monotone path,

\[
|B_j|=|C|,
\qquad
\sum_j|B_j\triangle B_{j-1}|
=2\sum_j
|\{\tau\in C:e_j(\tau)\ne e_{j-1}(\tau)\}|
\le2|C|.
\tag{2.15}
\]

Combining Theorem 2.1 with (2.12)--(2.15) proves:

> **Corollary 2.2 — fixed-window little-\(o\) equivalence.** On a monotone
> fixed-star trajectory, the following are equivalent at scale
> \(t/\sqrt m\):
>
> 1. \(M_\infty=o_A(t/\sqrt m)\) and
>    \(V=o_A(t/\sqrt m)\);
> 2. \(\Theta_{\rm path}=o_A(t/\sqrt m)\);
> 3. one trace set \(C\), of size \(o_A(t/\sqrt m)\), meets every projected
>    survival packet at every visited state;
> 4. there is one common trace set \(C\) such that \(B_j=e_j(C)\) are
>    quota-safe, have pointwise size
>    \(o_A(t/\sqrt m)\), and total physical wreath recourse
>    \(o_A(t/\sqrt m)\).

The implications have explicit constants:

\[
(1)\Rightarrow(2):\quad
\Theta_{\rm path}\le M_\infty+V,
\]

\[
(2)\Rightarrow(3):\quad
|C|\le R_A\Theta_{\rm path},
\]

\[
(3)\Rightarrow(4):\quad
\max_j|B_j|=|C|,
\quad
\sum_j|B_j\triangle B_{j-1}|\le2|C|,
\]

and the indicator \(w=\mathbf1_C\) proves \((3)\Rightarrow(1)\).
Conversely, exact packetization applied to the families
\(B_j=e_j(C)\) proves \((4)\Rightarrow(3)\).

Thus bounded packet rank removes a second possible dynamic integrality
gap. The missing object is one common trace hard-quota core.

### 2.2 Exact dual and compressed cuts

Ordinary packet-cover duality gives

\[
\boxed{
\Theta_{\rm path}
=\max\left\{
\sum_{j,a,P}y_{j,a,P}:
y_{j,a,P}\ge0,\ 
\sum_{\substack{j,a,P:\\
\tau\in e_j^{-1}(P)}}y_{j,a,P}\le1
\quad(\tau\in\mathcal T)
\right\}.
}
\tag{2.16}
\]

Here \(a=(q,S)\), and state/resource-labelled parallel packets remain
parallel dual variables.

There is an exact compressed form. For each state-resource
\(\alpha=(j,q,S)\), let

\[
O_\alpha^{\rm tr}
=e_j^{-1}\mathcal O_{F_j}(q,S),
\qquad
k_\alpha=\beta_q^{(j)}(S)+1,
\]

retaining only \(|O_\alpha^{\rm tr}|\ge k_\alpha\). Then

\[
\boxed{
\begin{aligned}
\Theta_{\rm path}
=\max\ &\sum_\alpha Y_\alpha\\
\text{subject to }&
Y_\alpha\ge0,\\
&
\sum_\alpha Y_\alpha
\bigl(k_\alpha-|O_\alpha^{\rm tr}\setminus Z|\bigr)_+
\le|Z|
\qquad(Z\subseteq\mathcal T).
\end{aligned}
}
\tag{2.17}
\]

The proof is the audited hypersimplex decomposition followed by the
resource-to-trace capacitated flow. State labels merely create parallel
resources. Equation (2.17) is the exact dual packing obstruction to a
slow monotone twin trajectory.

### 2.3 A short-switch construction

Now freeze one balanced quota system \(\beta\) throughout the path. Let

\[
S=\{\tau\in\mathcal T:
e_j(\tau)\ne e_0(\tau)\text{ for some }j\},
\qquad s=|S|.
\tag{2.18}
\]

Let \(x^{(0)}\) cover the initial factor. Project it to \(w^{(0)}\) on
\(\mathcal T\), and put

\[
w_\tau=
\begin{cases}
1,&\tau\in S,\\
w_\tau^{(0)},&\tau\notin S.
\end{cases}
\tag{2.19}
\]

Any later projected packet which meets \(S\) is covered by a unit entry. A
packet avoiding \(S\) consists entirely of unchanged wreaths. Since the
quota is fixed, it was already a packet at time zero and is covered by
\(w^{(0)}\). Therefore \(w\) covers the whole path union and

\[
\|w\|_1\le\|x^{(0)}\|_1+s.
\tag{2.20}
\]

Together with time-zero restriction, this proves the exact sandwich

\[
\boxed{
\vartheta(F_0,\beta)
\le\Theta_{\rm path}
\le\vartheta(F_0,\beta)+s.
}
\tag{2.21}
\]

On a monotone path, the physical movement of (2.19) is exactly \(2s\) on
the switched traces, while thresholding gives

\[
|B_j|\le s+R_A\|x^{(0)}\|_1,
\qquad
\sum_j|B_j\triangle B_{j-1}|\le2s.
\tag{2.22}
\]

Consequently

\[
\vartheta(F_0,\beta)+s=o_A(t/\sqrt m)
\tag{2.23}
\]

is a sufficient slowly-moving-cover construction with no factor \(K_A\)
and no \(\sqrt m\) loss.

It is only a stability result. A nontrivial useful \(\phi\)-cycle need not
exist, the initial cover is not constructed, and changing the quota system
invalidates the persistence argument.

## 3. General edit stability and its deficient-packet dual

Let \(F,F'\) be exact factors, keep the same balanced quota system
\(\beta\), and put

\[
d(F,F')=|F\setminus F'|=|F'\setminus F|=d.
\tag{3.1}
\]

### Theorem 3.1 — row-edit Lipschitz theorem

\[
\boxed{
|\vartheta(F,\beta)-\vartheta(F',\beta)|\le d.
}
\tag{3.2}
\]

More strongly, if \(x\in[0,1]^F\) covers \(F\), retain its weights on
\(F\cap F'\), put weight one on \(F'\setminus F\), and put zero outside
\(F'\). The result \(x'\) covers \(F'\), with

\[
\|x'\|_1\le\|x\|_1+d,
\qquad
\|x'-x\|_1\le2d.
\tag{3.3}
\]

#### Proof

A packet of \(F'\) either contains a new wreath, whose weight is one, or
consists entirely of common wreaths. In the second case the same rows owned
the same resource in \(F\), and the fixed quota gives the same packet size,
so it was already a packet of \(F\). Thus \(x'\) covers. Reversing
\(F,F'\) proves (3.2). \(\square\)

Because the balanced quota space is independent of the factor, the
quota-minimized value

\[
\vartheta_A(F)=\min_{\beta\ {\rm balanced}}\vartheta(F,\beta)
\tag{3.4}
\]

also satisfies

\[
|\vartheta_A(F)-\vartheta_A(F')|\le d(F,F').
\tag{3.5}
\]

Along any frozen-quota exact twin trajectory with step sizes
\(d_j=d(F_{j-1},F_j)\) and total row-edit length

\[
L=\sum_{j=1}^Td_j,
\tag{3.6}
\]

cap \(x^{(0)}\) coordinatewise at one and recursively use (3.3). This gives

\[
\max_j\|x^{(j)}\|_1
\le\|x^{(0)}\|_1+L,
\qquad
\sum_j\|x^{(j)}-x^{(j-1)}\|_1
\le2L.
\tag{3.7}
\]

This is the strongest automatic statement supplied merely by row edits.

There is an exact one-step residual LP. Put

\[
C=F\cap F',\qquad
D=F\setminus F',\qquad
N=F'\setminus F,
\tag{3.8}
\]

and keep \(x\) fixed on \(C\). Define

\[
\Psi(x;F\to F')
=\min\left\{
\sum_{E\in N}z_E:
z_E\ge0\quad(E\in N),\qquad
\sum_{E\in P\cap N}z_E
\ge
\left(1-\sum_{E\in P\cap C}x_E\right)_+
\quad(P\in\mathcal P(F',\beta))
\right\}.
\tag{3.9}
\]

Its exact dual is

\[
\boxed{
\Psi
=\max\left\{
\sum_P
\left(1-x(P\cap C)\right)_+y_P:
y_P\ge0,\ 
\sum_{P\ni E}y_P\le1\quad(E\in N)
\right\}.
}
\tag{3.10}
\]

Thus

\[
\Psi\le|N|=d,
\qquad
\|x'-x\|_1
=\sum_{E\in D}x_E+\Psi
\tag{3.11}
\]

when common weights are frozen and an optimal extension is used. Equation
(3.10) is the exact local dual obstruction to a cheap **frozen-common**
extension. It is not the dual of unrestricted minimum movement, which may
also alter weights on \(C\).

Quota motion is a separate variable. In the abstract packet category, even
at zero factor edit, changing an isolated \(h\)-owner resource from quota
two to quota one changes its packet optimum from \(h/3\) to \(h/2\). A
compensating quota swap on an empty resource preserves the number of upper
quota cells. Therefore no black-box row-edit-only continuity theorem
survives arbitrary quota reselection. Whether exact wreath geometry gives a
stronger quota-continuity theorem remains open.

## 4. The exact kinetic packet-cover dual

The trace-path LP uses special fibre geometry. There is also an exact
dynamic dual for an arbitrary prescribed finite exact-factor trajectory.

Let

\[
\mathscr U=\bigcup_{j=0}^TF_j
\tag{4.1}
\]

be the physical wreath-atom universe. Extend every state cover by zero
outside \(F_j\). Let \(\mathcal P_j\) be the state-\(j\) packet hypergraph
for a prescribed balanced quota system \(\beta^{(j)}\).

For holding coefficients \(a_j\ge0\) and movement coefficients \(b_j\ge0\),
put

\[
\Phi_{a,b}
=\min_x\left[
\sum_{j=0}^Ta_j\|x^{(j)}\|_1
+\sum_{j=1}^Tb_j
\|x^{(j)}-x^{(j-1)}\|_1
\right],
\tag{4.2}
\]

subject to all packet-cover inequalities. Coordinatewise truncation at one
preserves feasibility and cannot increase (4.2).

### Theorem 4.1 — temporal packet-packing dual

Put

\[
p_{0,E}=p_{T+1,E}=0.
\]

Then

\[
\boxed{
\begin{aligned}
\Phi_{a,b}
=\max\ &\sum_{j=0}^T\sum_{P\in\mathcal P_j}y_{j,P}\\
\text{subject to }&
y_{j,P}\ge0,\\
&|p_{j,E}|\le b_j
\qquad(1\le j\le T),\\
&
\sum_{\substack{P\in\mathcal P_j\\E\in P}}y_{j,P}
\le
a_j+p_{j,E}-p_{j+1,E}
\qquad(E\in F_j).
\end{aligned}
}
\tag{4.3}
\]

There is no constraint at an inactive node \(E\notin F_j\).

#### Proof

Linearize each absolute difference with

\[
u_{j,E}\ge x_E^{(j)}-x_E^{(j-1)},
\qquad
u_{j,E}\ge x_E^{(j-1)}-x_E^{(j)}.
\]

Give the two inequalities nonnegative dual variables \(r_{j,E},s_{j,E}\).
The coefficient of \(u_{j,E}\) requires

\[
r_{j,E}+s_{j,E}\le b_j.
\]

Writing \(p_{j,E}=r_{j,E}-s_{j,E}\) is equivalent to
\(|p_{j,E}|\le b_j\). If

\[
g_{j,E}=\sum_{P\ni E}y_{j,P},
\]

the coefficient of an active \(x_E^{(j)}\) is

\[
a_j-g_{j,E}+p_{j,E}-p_{j+1,E}.
\]

Its infimum over \(x_E^{(j)}\ge0\) is finite exactly under the last
inequality of (4.3). Finite-dimensional LP duality proves the result.
\(\square\)

### 4.1 Max-mass version

The functional matching (1.14) is

\[
\Phi_{\max,b}
=\min_x\left[
\max_j\|x^{(j)}\|_1
+\sum_{j=1}^Tb_j
\|x^{(j)}-x^{(j-1)}\|_1
\right].
\tag{4.4}
\]

Introducing an epigraph variable \(M\ge0\), with
\(\|x^{(j)}\|_1\le M\), gives the exact dual

\[
\boxed{
\begin{aligned}
\Phi_{\max,b}
=\max\ &\sum_{j,P}y_{j,P}\\
\text{subject to }&
y_{j,P}\ge0,\quad
\alpha_j\ge0,\quad
\sum_j\alpha_j\le1,\\
&|p_{j,E}|\le b_j,\\
&
\sum_{P\ni E}y_{j,P}
\le
\alpha_j+p_{j,E}-p_{j+1,E}
\qquad(E\in F_j).
\end{aligned}
}
\tag{4.5}
\]

Thus the desired target is exactly

\[
\Phi_{\max,1}=o_A(t/\sqrt m).
\tag{4.6}
\]

The dual object is a spacetime packet packing. Each wreath-time load may be
paid by one global unit of holding capacity, distributed through the
\(\alpha_j\), and by temporal edge capacities
\(|p_{j,E}|\le1\).

### 4.2 Compressed kinetic cuts

For a state-resource \(a=(q,S)\), put

\[
O_{j,a}=\mathcal O_{F_j}(q,S),
\qquad
k_{j,a}=\beta_q^{(j)}(S)+1.
\]

In (4.3), let

\[
\rho_{j,E}=a_j+p_{j,E}-p_{j+1,E};
\tag{4.7}
\]

in (4.5), replace \(a_j\) by \(\alpha_j\). The packet variables at time
\(j\) compress to resource masses \(Y_{j,a}\ge0\). The exact conditions
are

\[
\rho_{j,E}\ge0\qquad(E\in F_j)
\tag{4.8}
\]

and, for every \(Z\subseteq F_j\),

\[
\boxed{
\sum_aY_{j,a}
\bigl(k_{j,a}-|O_{j,a}\setminus Z|\bigr)_+
\le
\sum_{E\in Z}\rho_{j,E}.
}
\tag{4.9}
\]

The objective is \(\max\sum_{j,a}Y_{j,a}\). This follows from the same
hypersimplex decomposition and resource-owner max-flow cuts as in the
static audited LP. No additional fractional obstruction is hidden.

### 4.3 Static and endpoint dual lifts

A static packet packing at any time \(s\) lifts into (4.5) by taking

\[
\alpha_s=1,\qquad p=0.
\]

Therefore

\[
\boxed{
\Phi_{\max,b}
\ge\max_s\vartheta(F_s,\beta^{(s)}).
}
\tag{4.10}
\]

There is also an endpoint form. Restrict Theorem 4.1 to the subtrajectory
\(s,\ldots,T\); equivalently, in the full trajectory give the final cover
mass coefficient one, put \(b_j=0\) for \(j\le s\), and put \(b_j=1\) for
\(j>s\). If \(s<T\), a static packet packing at time \(s\), with owner
congestion \(w_E\le1\), extends by

\[
p_{j,E}=
\begin{cases}
0,&j\le s,\\
-w_E,&s<j\le T.
\end{cases}
\tag{4.11}
\]

At time \(s\), the temporal divergence is \(w_E\); at time \(T\), the final
holding capacity is \(1-w_E\). If \(s=T\), instead take \(p=0\), and the
terminal holding capacity is one. Hence every cover trajectory satisfies

\[
\boxed{
\|x^{(T)}\|_1+
\sum_{j=s+1}^T
\|x^{(j)}-x^{(j-1)}\|_1
\ge\vartheta(F_s,\beta^{(s)}).
}
\tag{4.12}
\]

If a packet packing at time \(j-1\) is supported on packets lying entirely
inside the disappearing row set

\[
D_j=F_{j-1}\setminus F_j,
\]

then it gives the local movement obstruction

\[
\boxed{
\|x^{(j)}-x^{(j-1)}\|_1
\ge\sum_Py_P.
}
\tag{4.13}
\]

Indeed all weight on \(D_j\) must fall to zero, and dual packet coverage
lower-bounds that disappearing weight.

## 5. Canonical and native-cube dual obstructions

Let \(F_m^{\rm MSW}\) be the canonical exact factor and put

\[
C_m=\operatorname{Cat}_{m-4}.
\tag{5.1}
\]

The audited suffix construction gives \(C_m\) pairwise disjoint
depth-one survival packets for every balanced quota system. The exact ratio
is

\[
\frac{C_m}{t}
=
\frac{(m-2)(m-1)m(m+1)}
{16(2m-7)(2m-5)(2m-3)(2m-1)}
=\frac1{256}+O(m^{-1}).
\tag{5.2}
\]

Consequently

\[
\vartheta(F_m^{\rm MSW},\beta)\ge C_m
\tag{5.3}
\]

for every quota system containing depth one.

More generally, if \(F\) is at row-replacement distance

\[
d(F,F_m^{\rm MSW})=d,
\]

then at least \(C_m-d\) distinguished owner triples remain intact, and

\[
\boxed{
\vartheta(F,\beta)\ge(C_m-d)_+.
}
\tag{5.4}
\]

This bound is uniform over quota choices: after seeing whether
\(\beta_1(S)=1\) or \(2\), choose a two- or three-owner packet from the
intact triple.

### Theorem 5.1 — canonical kinetic barrier

If a prescribed trajectory visits a state \(F_s\) at canonical row distance
\(d_s\), then

\[
\Phi_{\max,1}\ge(C_m-d_s)_+.
\tag{5.5}
\]

If it starts at the canonical factor and ends with

\[
\|x^{(T)}\|_1=o_A(t/\sqrt m),
\]

then

\[
\boxed{
\sum_{j=1}^T
\|x^{(j)}-x^{(j-1)}\|_1
\ge
C_m-o_A(t/\sqrt m)
=\Omega(t).
}
\tag{5.6}
\]

Likewise, if \(k_j=d(F_{j-1},F_j)\) are twin-switch row volumes, reaching a
target-small packet state requires

\[
\boxed{
\sum_jk_j
\ge C_m-o_A(t/\sqrt m)
=\left(\frac1{256}-o(1)\right)t.
}
\tag{5.7}
\]

#### Proof

Equation (5.5) follows by putting the static disjoint-packet packing at time
\(s\) into (4.10). Equation (5.6) follows from (4.12), and (5.7) follows
from the edit Lipschitz theorem or from (5.4). \(\square\)

Therefore no target-scale slowly moving cover can start in the canonical
factor or in an \(o(t)\)-edit neighbourhood of it.

### 5.1 The sharper native \((2\,3)\)-cube bound

Inside the audited \((2\,3)\)-component cube of the canonical factor, every
nontrivial switched component costs at least two canonical rows and hits at
most one suffix certificate. Therefore a cube state at row distance \(d\)
satisfies

\[
\boxed{
\vartheta(F_\varepsilon,\beta)
\ge\left(C_m-\frac d2\right)_+.
}
\tag{5.8}
\]

A target-small state in that cube must have

\[
\boxed{
d\ge2C_m-o_A(t/\sqrt m)
=\left(\frac1{128}-o(1)\right)t.
}
\tag{5.9}
\]

This constant is exact for eliminating the displayed resource family.
Switching all audited size-two components
\(\mathcal C_{0,1100V}\) produces one exact factor
\(F_m^\dagger\) at distance \(2C_m\), and the contextual multiplicities
change exactly from

\[
\mu_{F_m^{\rm MSW}}(S_V)=3
\quad\text{to}\quad
\mu_{F_m^\dagger}(S_V)=2.
\tag{5.10}
\]

There are more than \(C_m\) upper depth-one quota slots, so assigning quota
two to every \(S_V\) removes all packets from this displayed resource
family. Unrelated resources may still have a large packet LP. Thus
(5.8)--(5.10) are a basin obstruction, not a factor-independent
counterexample to \(\mathrm{FSP}_A\).

## 6. Exact merger with alternating reservoirs

The survival LP is on wreath rows. The alternating-reservoir theorem is on
middle owners and target-family cuts. They meet through two exact
projections.

### 6.1 From balanced owner recourse to a packet cover

Fix one oriented exact factor \(F\), balanced target loads \(\beta_q\), and
one actual one-pass trajectory attaining those loads. Mark a wreath row if
any of its middle owners toggles at any controlled stage, and call the
marked family \(B_{\rm touch}\).

> **Lemma 6.1 — touch projection.** The family \(B_{\rm touch}\) is an
> integral survival-packet cover. Consequently, if \(T_q\) is the number of
> toggled middle owners at stage \(q\),
> \[
> \boxed{
> \vartheta(F,\beta)
> \le|B_{\rm touch}|
> \le\sum_{q\le K}T_q.
> }
> \tag{6.1}
> \]

#### Proof

If a packet \(P\) for \((q,S)\) avoided \(B_{\rm touch}\), every row in
\(P\) would retain its unique canonical occurrence of \(S\) at depth \(q\).
The final load would therefore satisfy

\[
\beta_q(S)\ge|P|=\beta_q(S)+1,
\]

a contradiction. Every touched row contains at least one toggle event, so
the second inequality follows. \(\square\)

For a probability distribution on balanced trajectories,

\[
x_E=\Pr(E\in B_{\rm touch})
\tag{6.2}
\]

is a fractional packet cover and

\[
\|x\|_1=\mathbb E|B_{\rm touch}|.
\tag{6.3}
\]

For a coupling at adjacent factor states,

\[
\|x^{(j)}-x^{(j-1)}\|_1
\le
\mathbb E
|B_{\rm touch}^{(j)}
\triangle B_{\rm touch}^{(j-1)}|.
\tag{6.4}
\]

Here both touch marginals and touched-row indicators are extended by zero
to the common physical wreath universe before taking either difference.

Thus alternating-reservoir recourse projects exactly into the audited
packet LP. It does not reach the packet target from ordinary CAHR:

\[
\vartheta(F,\beta)
\le\sum_qT_q
\le C_A\sum_q\frac{T_q}{c_q}.
\tag{6.5}
\]

The bound \(o(W)\) on the right is much weaker than
\(o_A(t/\sqrt m)\). To infer \(\mathrm{FSP}_A\) by touch projection one
needs the much stronger wreath-support concentration

\[
\sum_qT_q=o_A(t/\sqrt m),
\tag{6.6}
\]

or a theorem showing that many toggle events reuse the same
\(o_A(t/\sqrt m)\) rows.

### 6.2 Packet cover to exceptional-owner discrepancy

Conversely, let \(B\subseteq F\) be an integral packet cover and put

\[
G=F\setminus B,\qquad b=|B|.
\]

Then

\[
\mu_q^G\le\beta_q.
\tag{6.7}
\]

Define

\[
h_q=\beta_q-\mu_q^G\ge0,
\qquad
\nu_q=\mu_q^B.
\tag{6.8}
\]

Every wreath contributes exactly \(n\) occurrences at every depth, so

\[
\sum_Sh_q(S)
=\sum_S\nu_q(S)
=nb.
\tag{6.9}
\]

For the full-factor discrepancy

\[
\delta_q=\beta_q-\mu_q^F=h_q-\nu_q,
\tag{6.10}
\]

one has

\[
\boxed{
D_q:=\frac12\|\delta_q\|_1\le nb.
}
\tag{6.11}
\]

Thus packet coverage gives nonnegative quota holes of exactly the same
total mass as the exceptional-row occurrences. It does not assign those
occurrences to the holes.

### 6.3 Small-exceptional alternating-Hall lemma

For every \(q\), let \(R_q\) be a set of canonical owner arcs belonging
only to the \(nb\) middle owners in rows \(B\). Assume

\[
R_q\cap R_{q-1}=\varnothing
\tag{6.12}
\]

as owner sets, and, for every target family
\(U\subseteq\binom{[n]}{m-q}\),

\[
\boxed{
\delta_q(U)\le|\partial^-_{R_q}(U)|.
}
\tag{6.13}
\]

> **Theorem 6.2 — target-scale alternating completion.** Under
> (6.12)--(6.13), one actual ascending one-pass trajectory has balanced load
> \(\beta_q\) at every rank, leaves all rows of \(G\) canonical, and obeys
> \[
> \boxed{
> T_q\le|R_q|\le nb,
> \qquad
> \sum_{q\le K}\frac{T_q}{c_q}
> \le nbS_A(m).
> }
> \tag{6.14}
> \]

#### Proof

The directed cut theorem and incidence total unimodularity give a
\(0\)-\(1\) solution

\[
B_qx_q=\delta_q,\qquad
\operatorname{supp}x_q\subseteq R_q.
\]

Adjacent reservoir disjointness gives the exact no-toggle reset used in the
L3 alternating-reservoir proof, so the independently selected rank flows
are the decisions of one actual recurrence. Their rank loads are
\(\mu_q^F+B_qx_q=\beta_q\), and no owner in \(G\) toggles. Finally
\(|x_q|\le|R_q|\le nb\), proving (6.14). \(\square\)

No active-component order or path-length bound appears. At the much smaller
FSP exceptional-row scale, the total number of available reservoir edges is
already cheap enough.

If \(x\) is a fractional packet cover of mass \(M\), deterministic
thresholding gives \(b\le R_AM\). Therefore Theorem 6.2 gives

\[
\sum_{q\le K}\frac{T_q}{c_q}
\le nR_AS_A(m)M
\le nR_A(A+1)\sqrt m\,M.
\tag{6.15}
\]

Hence

\[
M=o_A(t/\sqrt m)
\quad\Longrightarrow\quad
\sum_{q\le K}\frac{T_q}{c_q}=o_A(nt)=o_A(W),
\tag{6.16}
\]

provided the independent cuts and alternation hypotheses hold.

The packet LP proves only (6.7)--(6.11). It does **not** prove (6.13), and
it does not split the exceptional owner arcs into adjacent-disjoint
reservoirs. The packet dual cuts range over wreath sets \(Z\subseteq F\);
the alternating cuts range over target families
\(U\subseteq\binom{[n]}{m-q}\). No implication between these two cut
systems is known.

### 6.4 Dynamic fixed-core corollary

Return to the fixed-star monotone path. Suppose the common trace cover
\(C\) from Section 2 contains every changed trace. Then

\[
G_j=F_j\setminus e_j(C)
\]

is literally the same wreath family \(G\) at every state. If the quota
system \(\beta\) is fixed, the hole vectors

\[
h_q=\beta_q-\mu_q^G
\]

are also fixed. The small exceptional families

\[
B_j=e_j(C)
\]

carry the varying active lifts, with

\[
|B_j|=|C|,
\qquad
\sum_j|B_j\triangle B_{j-1}|\le2|C|.
\tag{6.17}
\]

If every state admits adjacent-disjoint exceptional-owner reservoirs
satisfying (6.13), Theorem 6.2 supplies an exact balanced nested trajectory
inside each state with uniform cost

\[
n|C|S_A(m)=o_A(W).
\tag{6.18}
\]

Thus the exact remaining merger gate is:

\[
\boxed{
\text{one small common exceptional trace set}
+\text{ higher-order target Hall inside its active lifts}
+\text{ adjacent-stage alternation}.
}
\tag{6.19}
\]

Component diameter is no longer part of this target-scale gate.

### 6.5 Comparison with robust component recourse

The audited packet-to-overload inequality is

\[
\mathcal U_A(F):=
\sum_{q\le K}\frac{O_q(F)}{c_q}
\le3nK\,M.
\tag{6.20}
\]

If the robust reachable-state component hypothesis from L3 independently
holds, then quota-universal bad components of order at most \(L_A\) give

\[
\sum_q\frac{T_q}{c_q}
\le2(L_A-1)\mathcal U_A(F)
\le6(L_A-1)nK\,M,
\tag{6.21}
\]

while merely balanceable bad components of order at most \(L_A\) give

\[
\sum_q\frac{T_q}{c_q}
\le6(C_A+1)L_A\,nK\,M.
\tag{6.22}
\]

Both are \(o_A(W)\) when \(M=o_A(t/\sqrt m)\). These routes retain the
strong “every balanced-prefix reachable state” quantifier. The survival LP
does not prove it.

### 6.6 The remaining \(\sqrt m\) support-concentration gap

A fixed-star switch of \(k\) traces transports a balanced one-pass
trajectory to an approximate trajectory with rankwise residual
half-\(\ell^1\) at most \(3k\). A bounded-path retraction with parameter
\(p_A\) would use at most

\[
3p_Ak
\]

toggle events at each rank and hence at most

\[
3p_AkK=O_A(k\sqrt m)
\tag{6.23}
\]

**additional** wreath rows touched by the residual retraction, by the crude
union bound. Conditional on a base trajectory whose touched-row cover is
already target-small, making this additional support target-small requires

\[
k=o_A(t/m).
\tag{6.24}
\]

By contrast, relative to the same target-small base cover, the unit trace
buffer in (2.19) costs only \(k\) additional rows and allows

\[
k=o_A(t/\sqrt m).
\tag{6.25}
\]

Closing this factor-\(\sqrt m\) gap requires a simultaneous all-rank
retraction supported on \(O_A(k)\) wreath rows. Separate short paths at
each rank do not suffice.

## 7. Exact scope, nonimplications, and remaining theorem

### 7.1 Free trajectories do not weaken the static theorem

With no prescribed starting state or required evolution, a dynamic
existence theorem is not weaker than \(\mathrm{FSP}_A\): taking \(T=0\)
recovers the static problem, while any visited target-small state already
is an \(\mathrm{FSP}_A\) witness. The dynamic question has genuine extra
content only for a prescribed local evolution, prescribed starting basin,
or common-core requirement.

### 7.2 What has not been proved

None of the following implications is valid from the present results:

1. small weighted overload \(\Rightarrow\) small survival-packet cover;
2. packet coverage \(\Rightarrow\) alternating target-family Hall cuts;
3. quota-safe exceptional rows \(\Rightarrow\) nested assignment of their
   owners to all quota holes;
4. the L3 \(2k\) histogram, \(3k\) pointed, or \(7k\) fixed-cut bounds
   \(\Rightarrow\) small packet-cover movement;
5. CAHR cost \(o(W)\Rightarrow\mathrm{FSP}_A\);
6. destruction of the canonical packet certificate
   \(\Rightarrow\) a small packet LP in the resulting factor;
7. a small cover at one quota system
   \(\Rightarrow\) slow cover motion under arbitrary quota reselection.

The physical identity issue is essential. Packet-LP vertices are actual
unoriented wreath supports. Identifying an old row with its twin by a moving
trace label would erase the real cost \(2a\) of moving weight \(a\) between
two different atoms and would invalidate common-threshold recourse for
actual exceptional wreath families.

### 7.3 Clean fourth-wave target

A sufficient merged statement is:

> **Common-trace Survival-Hall theorem
> \(\mathrm{CTSH}_A\) — unproved.** For every fixed \(A>0\) and all
> sufficiently large \(m\), find a fixed-star exact-factor fibre, a finite
> monotone twin trajectory in that fibre, one
> fixed balanced quota system \(\beta\), and one trace set
> \(C\subseteq\mathcal T\), such that
> \[
> |C|=o_A(t/\sqrt m),
> \]
> \(C\) meets every projected survival packet at every visited state, and,
> at every state, the middle owners in the active lifts \(e_j(C)\) admit
> adjacent-disjoint canonical reservoirs satisfying every directed cut
> (6.13).

The path-union theorem gives slowly moving fractional and integral packet
covers. Theorem 6.2 gives exact balanced one-pass owner trajectories of cost
\(o_A(W)\). Fixed-window diagonalization then yields labelled
synchronization, hence MWB and the final OR theorem.

This theorem is stronger than \(\mathrm{FSP}_A\), because it also demands
labelled completion and a prescribed fibre evolution. The exact LP
obstruction to its common-trace cover clause can be written as either:

- a trace-congestion packing in (2.16)--(2.17) of mass
  \(\Omega_A(t/\sqrt m)\); or
- a spacetime physical-wreath packing in (4.5)--(4.9) of that mass.

These packet duals do not exhaust obstructions to
\(\mathrm{CTSH}_A\). The Hall clause may also fail through a target-family
cut

\[
\delta_q(U)>|\partial^-_{R_q}(U)|
\]

or through nonexistence of any adjacent-disjoint reservoir choice.

The canonical MSW packing supplies such an obstruction only in the
canonical and \(o(t)\)-edit basins. A factor-independent packing, or a
positive construction in a fixed-star fibre outside those basins, remains
open.

## 8. Audited ledger

### Proved

1. Explicit fixed-\(A\) bounds \(c_q\le C_A\),
   packet rank \(R_A=C_A+2\), and \(S_A\le(A+1)\sqrt m\).
2. Exact reduction of monotone fixed-star slow covers to one path-union
   trace LP.
3. Exact path-union packet-packing dual and compressed trace-cut form.
4. Fixed-window equivalence between fractional slow covers, one small
   common trace transversal, and slowly moving integral quota-safe
   exceptional families.
5. The short-switch buffer
   \(\Theta_{\rm path}\le\vartheta(F_0,\beta)+s\).
6. One-Lipschitz packet-cover value under fixed-quota row edits, the
   \(2d\) transport bound, and the exact deficient-packet extension dual.
7. Exact temporal-potential duality for arbitrary finite physical
   exact-factor trajectories, including max-mass, compressed cuts, endpoint
   lifts, and vanishing-packet movement certificates.
8. The canonical \(\Omega(t)\) kinetic obstruction and the sharper native
   \((2\,3)\)-cube constant \(1/128\).
9. Exact touch projection from balanced owner recourse to the
   survival-packet LP.
10. Exact packet-cover discrepancy ledger
    \(D_q\le n|B|\).
11. Target-scale alternating completion
    \(\sum_qT_q/c_q\le n|B|S_A\), with no component-size hypothesis.
12. The dynamic fixed-core corollary and the explicit remaining
    factor-\(\sqrt m\) row-support concentration gap.

### Still open

1. A target-small packet cover in any exact factor.
2. A target-small path-union cover in a fixed-star fibre outside the
   canonical \(o(t)\)-edit basin.
3. Alternating higher-order target Hall cuts inside the small exceptional
   rows.
4. A simultaneous all-rank retraction supported on \(O_A(k)\) wreath rows.
5. A factor-independent survival-packet packing obstruction.

The fourth-wave conclusion is therefore exact:

\[
\boxed{
\begin{gathered}
\text{fractional slow motion on a finite monotone fixed-star trajectory}
\iff
\text{one common trace packet cover},\\
\text{canonical and subcritical-edit basins are dual-obstructed},\\
\text{and target-scale exceptional rows make component diameter irrelevant.}\\
\text{The common trace cover, useful twin basin, and alternating Hall remain open.}
\end{gathered}
}
\]
