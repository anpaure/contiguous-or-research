# Line G: the survival-packet cut dual, its null space, and the exact remaining dichotomy

Date: 2026-07-25

Method: pure mathematics only. No web search, finite search, random experiment,
or solver is used. The packet-Hall theorem and the two canonical obstruction
reports named below are treated as audited inputs. Every additional assertion
proved here is proved explicitly.

## 0. Verdict

Fix \(A>0\), and put

\[
n=2m+1,\qquad W=\binom nm,\qquad
t=\frac Wn=\operatorname {Cat}_m,\qquad
H=\lceil A\sqrt m\rceil .
\]

This report proves neither of the two requested asymptotic endpoints.

* No constant \(c_A>0\) is proved for which every exact factor and every
  balanced quota system have
  \(\vartheta(F,\beta)\ge c_At\).
* No genuine all-\(m\) noncanonical exact factor and quota system is constructed
  with
  \(\vartheta(F,\beta)=o_A(t/\sqrt m)\).

Moreover, these two alternatives are not logically exhaustive. If

\[
\Theta_A(m)=\min_{F\ {\rm exact}}\min_{\beta\ {\rm balanced}}
             \vartheta(F,\beta),
\]

then, for example, an intermediate law
\(\Theta_A(m)\asymp t/m^{1/4}\), or an oscillatory law, satisfies neither
alternative. Thus the requested “dichotomy” is presently an open trichotomy:

\[
\Theta_A=\Omega_A(t),\qquad
\Theta_A=o_A(t/\sqrt m),\qquad
\text{or neither.}
\tag{0.1}
\]

The rigorous advance is an exact reduction of both endpoints to the actual
owner hypergraph.

1. If \(\nu(F,\beta)\) is the largest family of vertex-disjoint survival
   packets, then
   \[
   \nu(F,\beta)\le\vartheta(F,\beta)\le R_A\nu(F,\beta),
   \tag{0.2}
   \]
   where \(R_A=O_A(1)\) is the maximum packet size. Thus the universal
   endpoint is exactly a linear packet-matching theorem, up to \(R_A\), and
   the constructive endpoint is exactly a sub-\(t/\sqrt m\) matching theorem.
2. Balanced quotas can be eliminated. A quota-free number \(b_A(F)\), defined
   by two elementary conditions on the loads left after deleting one common
   row set, satisfies
   \[
   \min_\beta\vartheta(F,\beta)\le b_A(F)
   \le R_A\min_\beta\vartheta(F,\beta).
   \tag{0.3}
   \]
3. In the important capped regime
   \(\mu_q^F(S)\le c_q+1\), quota minimization is exactly a labelled
   owner-hypergraph transversal problem: at depth \(q\), one must choose and
   cover exactly \(D_q\) high owner sets, and the same row weights cover all
   depths.
4. There is an explicit zero-packet **abstract** common-owner model satisfying
   all separate-depth degree totals and even all global coordinate point
   margins. It is not an exact wreath factor because its per-owner labels need
   not be cyclic intervals or nested across depths. Hence counts, balanced
   quotas, point margins, and the compressed cuts as abstract incidence
   constraints cannot prove a universal positive lower bound. The missing
   input is precisely cyclic, cross-depth realizability.

The canonical MSW factor and its first noncanonical repair remain at positive
Catalan packet distance by the audited canonical and prefix-suspension
theorems. Thus the known local rebundlings do not enter the null space found
here.

## 1. Exact setup

Throughout the packet problem the controlled depths are
\(1\le q\le H\); for fixed \(A\) and sufficiently large \(m\), all are
proper. At depth \(q\), set

\[
r_q=m-q,\qquad
N_q=\binom n{r_q},\qquad
c_q=\left\lfloor\frac W{N_q}\right\rfloor,\qquad
\rho_q=W-c_qN_q.
\tag{1.1}
\]

A balanced quota system has

\[
\beta_q(S)\in\{c_q,c_q+1\},\qquad
\sum_{S\in\binom{[n]}{r_q}}\beta_q(S)=W.
\tag{1.2}
\]

Equivalently, exactly \(\rho_q\) targets receive upper quota \(c_q+1\).
For fixed \(A\), the exact ratio

\[
\frac W{N_q}
=\prod_{j=0}^{q-1}\frac{m+2+j}{m-j}
\]

is bounded above by a constant depending only on \(A\) whenever
\(q\le H\). Hence

\[
R_A:=\max_{q\le H}(c_q+2)=O_A(1).
\tag{1.3}
\]

Let \(F\) be an exact middle wreath factor. Thus \(|F|=t\), and every
\(m\)-subset is owned by exactly one row. For
\(a=(q,S)\), define

\[
O_a=O_{q,S}
=\{E\in F:S\text{ is a cyclic length-}r_q\text{ interval of }E\},
\qquad h_a=|O_a|,\qquad k_a=\beta_q(S)+1.
\tag{1.4}
\]

The survival packets labelled by \(a\) are all \(k_a\)-subsets of \(O_a\).
They exist exactly when \(h_a\ge k_a\). The fractional packet-cover value is

\[
\vartheta(F,\beta)
=\min\left\{
\sum_{E\in F}x_E:
x_E\ge0,\
\sum_{E\in P}x_E\ge1
\text{ for every survival packet }P
\right\}.
\tag{1.5}
\]

Repeated owner sets attached to different resources are retained as labelled
parallel edges. They give repeated cover inequalities, but their labels matter
when quota slots are counted.

Every row owns exactly \(n\) distinct targets at each proper depth. Moreover,
a fixed coordinate lies in exactly \(r_q\) of those intervals. Therefore

\[
\sum_Sh_{q,S}=nt=W,\qquad
\sum_{S\ni i}h_{q,S}=r_qt\quad(i\in[n]),
\tag{1.6}
\]

and each owner has incidence degree \(nH\) over the whole controlled window.

## 2. The exact compressed cut dual

The following is the audited theorem from
PACKET_HALL_RECOURSE_20260725.md, restated to fix the language used below.

### Theorem 2.1 (packet-flow dual)

Let

\[
\mathcal V=\{a:h_a\ge k_a\}.
\]

Then \(\vartheta(F,\beta)\) is the maximum of
\(\sum_{a\in\mathcal V}Y_a\) over \(Y_a\ge0\) satisfying

\[
\boxed{
\sum_{a\in\mathcal V}
Y_a\bigl(k_a-|O_a\setminus Z|\bigr)_+
\le |Z|\qquad(Z\subseteq F).
}
\tag{2.1}
\]

Equivalently, one may introduce owner flows \(z_{a,E}\) and require

\[
0\le z_{a,E}\le Y_a,\qquad
\sum_{E\in O_a}z_{a,E}=k_aY_a,\qquad
\sum_{a:E\in O_a}z_{a,E}\le1.
\tag{2.2}
\]

#### Proof sketch of equivalence

The ordinary dual of (1.5) puts nonnegative weight on packets, with total
packet weight through each owner at most one. For a resource \(a\), aggregate
its packet weights to \(Y_a\), and aggregate their incidences at \(E\) to
\(z_{a,E}\). This gives (2.2). Conversely,
\((z_{a,E}/Y_a)_{E\in O_a}\) lies in

\[
\{u\in[0,1]^{O_a}:\sum_Eu_E=k_a\},
\]

the convex hull of the incidence vectors of the \(k_a\)-subsets of \(O_a\),
so it decomposes back into packet weights. Finally, (2.2) is a bipartite
flow problem from resources to owners. Its cut at \(Z\subseteq F\) forces
resource \(a\) to send at least
\(Y_a(k_a-|O_a\setminus Z|)_+\) units into \(Z\). Max-flow/min-cut gives
exactly (2.1). Thus there is no additional fractional Hall obstruction.
\(\square\)

For later use, the primal constraints for all packets of one resource are
also exactly

\[
\operatorname{Bot}_{k_a}(x;O_a)\ge1,
\tag{2.3}
\]

where \(\operatorname{Bot}_k\) is the sum of the \(k\) smallest owner
weights.

## 3. Packet matching and quota elimination

### Theorem 3.1 (integral packet-matching equivalence)

Let \(\nu(F,\beta)\) be the maximum number of pairwise vertex-disjoint
survival packets. Then

\[
\boxed{
\nu(F,\beta)\le\vartheta(F,\beta)\le R_A\nu(F,\beta).
}
\tag{3.1}
\]

#### Proof

A disjoint packet family is a feasible integral packet packing, hence a
feasible dual solution of value its cardinality. This gives
\(\nu\le\vartheta\).

Take a maximum packet matching \(\mathcal M\). It is maximal, so the union
\(U=\bigcup_{P\in\mathcal M}P\) meets every survival packet: otherwise a
packet disjoint from \(U\) could be added. Thus \(U\) is an integral packet
cover, and

\[
\vartheta(F,\beta)\le |U|
\le R_A|\mathcal M|=R_A\nu(F,\beta).
\]

This also covers the empty packet hypergraph, when both sides vanish.
\(\square\)

We next remove quota variables entirely. For \(B\subseteq F\), put

\[
g_{q,S}(B)=|O_{q,S}\setminus B|.
\tag{3.2}
\]

Define \(b_A(F)\) to be the minimum \(|B|\) such that, simultaneously for
every \(q\le H\),

\[
g_{q,S}(B)\le c_q+1\quad\text{for every }S,
\tag{3.3}
\]

and

\[
\bigl|\{S:g_{q,S}(B)=c_q+1\}\bigr|\le\rho_q.
\tag{3.4}
\]

### Theorem 3.2 (quota-free residual balancing)

Let \(\tau(F,\beta)\) be the minimum size of an integral packet cover.
Then

\[
\boxed{
b_A(F)=\min_{\beta\ {\rm balanced}}\tau(F,\beta).
}
\tag{3.5}
\]

Consequently,

\[
\boxed{
\min_\beta\vartheta(F,\beta)
\le b_A(F)
\le R_A\min_\beta\vartheta(F,\beta).
}
\tag{3.6}
\]

#### Proof

Suppose \(B\) is safe for a balanced quota \(\beta\). Then
\(g_{q,S}(B)\le\beta_q(S)\le c_q+1\), proving (3.3). Every cell with
residual load \(c_q+1\) must receive upper quota. There are exactly
\(\rho_q\) upper quotas, proving (3.4).

Conversely, suppose (3.3)--(3.4) hold. At depth \(q\), assign upper quota
to every target with residual load \(c_q+1\). Pad this set arbitrarily until
exactly \(\rho_q\) targets have upper quota. All remaining targets have load
at most \(c_q\), so the resulting balanced quota dominates every residual
load. Hence \(B\) is a packet cover for that quota. Minimizing in both
directions proves (3.5).

The left inequality in (3.6) is fractional relaxation. Choose a quota
minimizing \(\vartheta\). The maximal-matching construction in Theorem 3.1
gives

\[
\tau(F,\beta)\le R_A\nu(F,\beta)\le R_A\vartheta(F,\beta).
\]

Together with (3.5), this proves the right inequality. The same \(B\) serves
every depth; no depthwise owner reassignment has been introduced. \(\square\)

Define the three global minima

\[
\begin{aligned}
\Theta_A(m)&=\min_{F,\beta}\vartheta(F,\beta),\\
\mathsf N_A(m)&=\min_{F,\beta}\nu(F,\beta),\\
\mathsf B_A(m)&=\min_F b_A(F),
\end{aligned}
\tag{3.7}
\]

where \(F\) is always exact and \(\beta\) balanced. Taking minima in
Theorems 3.1--3.2 gives

\[
\boxed{
\mathsf N_A\le\Theta_A\le R_A\mathsf N_A,\qquad
\Theta_A\le\mathsf B_A\le R_A\Theta_A.
}
\tag{3.8}
\]

Thus, with no loss other than a constant depending on \(A\):

* the universal Catalan obstruction is equivalent to
  \(\mathsf N_A=\Omega_A(t)\), or to \(\mathsf B_A=\Omega_A(t)\);
* \(\mathrm{FSP}_A\) is equivalent to
  \(\mathsf N_A=o_A(t/\sqrt m)\), or to
  \(\mathsf B_A=o_A(t/\sqrt m)\).

This is an exact scale reduction, not a proof that one of the two scales
must occur.

## 4. An explicit cut certificate: incidence energy

For each depth \(q\), define

\[
\mathcal V_q=\{(q,S):h_{q,S}\ge k_{q,S}\},\qquad
\Xi_q(F,\beta)=\sum_{a\in\mathcal V_q}\frac{h_a}{k_a},
\tag{4.1}
\]

and put \(\Xi=\sum_{q\le H}\Xi_q\).

### Theorem 4.1 (incidence-energy sandwich)

For every exact factor and balanced quota system,

\[
\boxed{
\max_{q\le H}\frac{\Xi_q}{n}
\le\vartheta(F,\beta)
\le\Xi.
}
\tag{4.2}
\]

In particular,

\[
\frac{\Xi}{nH}\le\vartheta(F,\beta)\le\Xi.
\tag{4.3}
\]

#### Proof

Fix one depth \(q\). In the lifted dual (2.2), set, for
\(a\in\mathcal V_q\),

\[
Y_a=\frac{h_a}{nk_a},\qquad
z_{a,E}=\frac1n\quad(E\in O_a),
\tag{4.4}
\]

and set all other variables to zero. Since \(h_a\ge k_a\), one has
\(z_{a,E}\le Y_a\), while

\[
\sum_{E\in O_a}z_{a,E}=\frac{h_a}{n}=k_aY_a.
\]

Each row owns exactly \(n\) resources at depth \(q\), so its total
\(z\)-load is at most one. The dual value is \(\Xi_q/n\). Maximizing over
\(q\) proves the lower bound in (4.2). Averaging those depthwise bounds
gives (4.3).

For the upper bound, put

\[
u_E=\sum_{a\in\mathcal V:E\in O_a}\frac1{k_a},\qquad
x_E=\min\{1,u_E\}.
\tag{4.5}
\]

If \(P\subseteq O_a\) is a \(k_a\)-packet, then every \(E\in P\) has
\(x_E\ge1/k_a\), and hence \(\sum_{E\in P}x_E\ge1\). Thus \(x\) is a
fractional packet cover. Moreover,

\[
\sum_Ex_E\le\sum_Eu_E
=\sum_{a\in\mathcal V}\frac{h_a}{k_a}=\Xi.
\]

This proves the theorem. \(\square\)

### Corollary 4.2 (overload, holes, and forced prebalance)

Let

\[
\Omega_q(F,\beta)=\sum_S(h_{q,S}-\beta_q(S))_+,\qquad
M_q(F)=|\{S:h_{q,S}=0\}|.
\tag{4.6}
\]

Then

\[
\boxed{
\vartheta(F,\beta)
\ge\frac{\Omega_q(F,\beta)}{nR_A}
\ge\frac{M_q(F)}{nR_A}
\qquad(q\le H).
}
\tag{4.7}
\]

If \(\vartheta(F,\beta)=o_A(t/\sqrt m)\), then, for every controlled depth,

\[
\sum_{a\in\mathcal V_q}h_a=o_A(W/\sqrt m),\qquad
M_q=o_A(W/\sqrt m),
\tag{4.8}
\]

and over the whole window,

\[
\sum_{q\le H}\sum_{a\in\mathcal V_q}h_a=o_A(W).
\tag{4.9}
\]

#### Proof

For \(a\in\mathcal V_q\), write
\(d_a=h_a-\beta(a)\ge1\). Since \(k_a\le R_A\),

\[
\frac{h_a}{k_a}\ge\frac{d_a}{R_A}.
\]

Thus \(\Xi_q\ge\Omega_q/R_A\), and (4.2) gives the first inequality in
(4.7). Because the load and quota totals both equal \(W\), total overload
equals total underload. Every hole contributes at least one unit of
underload, so \(\Omega_q\ge M_q\).

Also

\[
\sum_{a\in\mathcal V_q}h_a\le R_A\Xi_q
\le R_An\vartheta.
\]

At the FSP scale this is \(o_A(W/\sqrt m)\). Summing the same inequality
over \(H=O_A(\sqrt m)\) depths gives (4.9). \(\square\)

Thus an FSP witness cannot merely concentrate a large amount of overload on
few resource labels: at each depth, the entire owner incidence supported on
over-capacity cells must already be \(o(W/\sqrt m)\).

## 5. Exact depth-one optimization

At depth one, for \(m\ge3\),

\[
c_1=1,\qquad
N_1=\binom n{m-1}=\frac m{m+2}W,\qquad
\rho_1=W-N_1=\frac{2W}{m+2}.
\tag{5.1}
\]

Write \(h_S=\mu_1^F(S)\), and define

\[
B_1(F)=\frac12\sum_{S:h_S\ge2}h_S,
\tag{5.2}
\]

and

\[
s(h)=
\begin{cases}
0,&h\le1,\\
1,&h=2,\\
h/6,&h\ge3.
\end{cases}
\tag{5.3}
\]

Let \(s_{(1)}\ge\cdots\ge s_{(N_1)}\) be these savings in decreasing
order.

### Theorem 5.1 (optimized depth-one incidence energy)

If \(\Xi_1^*(F)=\min_{\beta_1}\Xi_1(F,\beta_1)\), then

\[
\boxed{
\Xi_1^*(F)=B_1(F)-\sum_{j=1}^{\rho_1}s_{(j)}.
}
\tag{5.4}
\]

Writing
\(\vartheta_1^*(F)=\min_{\beta_1}\vartheta_1(F,\beta_1)\) for the packet
problem restricted to depth one,

\[
\boxed{
\frac{\Xi_1^*(F)}n
\le\vartheta_1^*(F)
\le\Xi_1^*(F).
}
\tag{5.5}
\]

#### Proof

If every target initially receives lower quota one, its contribution to
\(\Xi_1\) is \(h/2\) for \(h\ge2\), and zero otherwise. This totals
\(B_1(F)\). Changing one target to upper quota two changes its contribution
as follows:

* for \(h\le1\), both contributions are zero;
* for \(h=2\), the contribution drops from one to zero;
* for \(h\ge3\), it drops from \(h/2\) to \(h/3\).

The savings are exactly (5.3). A balanced quota has exactly \(\rho_1\)
upper cells, so choosing the \(\rho_1\) largest savings proves (5.4).
The two inequalities in (5.5) are Theorem 4.1 applied to the one-depth
problem and then minimized over quotas. \(\square\)

There is also a histogram lower bound valid without a cap-two hypothesis.
At depth one every fixed target occurrence pairs two distinct middle
supersets, and distinct occurrences use disjoint middle supersets because
the factor owns every middle set once. Hence

\[
h_S\le u_m:=\left\lfloor\frac{m+2}{2}\right\rfloor.
\tag{5.6}
\]

For \(m\ge4\), put

\[
\gamma_m=\min\left\{
\frac{u_m}{2(u_m-1)},
\frac{u_m}{3(u_m-2)}
\right\}.
\tag{5.7}
\]

If

\[
D_{\beta,1}=\sum_S(h_S-\beta_1(S))_+,
\]

then, term by term on violating cells,

\[
\frac{h_S}{\beta_1(S)+1}
\ge\gamma_m(h_S-\beta_1(S)).
\]

Indeed the two possible ratios are
\(h/[2(h-1)]\) for lower quota and \(h/[3(h-2)]\) for upper quota; both
decrease with \(h\), so (5.6) gives (5.7). Therefore

\[
\boxed{
\vartheta_1(F,\beta_1)
\ge\frac{\gamma_m}{n}D_{\beta,1}
\ge\frac{\gamma_m}{n}M_1(F).
}
\tag{5.8}
\]

Since equal total masses give

\[
D_{\beta,1}=\frac12\sum_S|h_S-\beta_1(S)|,
\]

we also have

\[
\boxed{
\vartheta_1^*(F)
\ge\frac{\gamma_m}{2n}
\min_{\beta_1}\|\mu_1^F-\beta_1\|_1.
}
\tag{5.9}
\]

This makes a possible universal route exact: a uniform asymptotic
first-shadow separation of order \(W\) would imply a Catalan packet lower
bound. Such a separation is **unproved** and is only sufficient rather than
equivalent. Its finite-dimensional analogue has a zero-defect counterexample
at \(m=4\), so it cannot follow from a dimension-free parity or margin
identity.

Finally, \(\Xi_1(F,\beta_1)=0\) exactly when
\(h_S\le\beta_1(S)\) for every \(S\). Equality of total masses then forces
\(h_S=\beta_1(S)\) pointwise. Thus the depth-one null space consists exactly
of perfectly balanced \(1/2\)-valued histograms.

## 6. The capped-deficit theorem

Assume now that one exact factor satisfies the simultaneous cap

\[
h_{q,S}\le c_q+1
\qquad(q\le H,\ S\in\tbinom{[n]}{r_q}).
\tag{6.1}
\]

Define

\[
\mathcal H_q^+=\{S:h_{q,S}=c_q+1\},\qquad
D_q=\sum_S(c_q-h_{q,S})_+.
\tag{6.2}
\]

### Theorem 6.1 (exact capped quota optimization)

Under (6.1),

\[
\boxed{|\mathcal H_q^+|=\rho_q+D_q.}
\tag{6.3}
\]

For \(B\subseteq F\), let

\[
i_q(B)=|\{S\in\mathcal H_q^+:O_{q,S}\cap B\ne\varnothing\}|.
\tag{6.4}
\]

Then

\[
\boxed{
b_A(F)=\min\{|B|:i_q(B)\ge D_q\text{ for every }q\le H\}.
}
\tag{6.5}
\]

Moreover,

\[
\boxed{
\min_\beta\vartheta(F,\beta)
=
\min_{\substack{J_q\subseteq\mathcal H_q^+\\|J_q|=D_q\ (q\le H)}}
\tau_f\bigl(\{O_{q,S}:q\le H,\ S\in J_q\}\bigr),
}
\tag{6.6}
\]

where \(\tau_f\) is fractional vertex cover and the resource labels are
retained.

#### Proof

Mass conservation gives

\[
\rho_q=W-c_qN_q=\sum_S(h_{q,S}-c_q).
\]

Under the cap, every positive summand equals one, while the total magnitude
of the negative summands is \(D_q\). This proves (6.3).

The only full-factor loads equal to \(c_q+1\) are those in
\(\mathcal H_q^+\). Such a cell remains at \(c_q+1\) after deleting \(B\)
exactly when \(B\) misses its owner set. Consequently the number of residual
high cells is

\[
|\mathcal H_q^+|-i_q(B)=\rho_q+D_q-i_q(B).
\]

Condition (3.4) is therefore equivalent to \(i_q(B)\ge D_q\); condition
(3.3) is automatic. Theorem 3.2 proves (6.5).

For the fractional assertion, a nonhigh cell has \(h\le c_q\), so it
creates no packet under either quota. A high cell has \(h=c_q+1\). Under
upper quota it creates no packet; under lower quota its unique packet is
its full owner set \(O_{q,S}\). There are \(\rho_q\) upper quota slots and
\(\rho_q+D_q\) high cells.

An optimal quota never wastes an upper slot on a nonhigh cell while leaving
a high cell low: moving that slot to the high cell deletes one constraint and
creates none. Hence exactly \(D_q\) high labels remain low, and every labelled
choice \(J_q\) of size \(D_q\) is realized by a balanced quota. This proves
(6.6). Identical owner sets attached to distinct targets give duplicate
cover constraints; the duplicates do not alter \(\tau_f\), while their labels
correctly consume distinct quota slots. \(\square\)

Equivalently, the right side of (6.6) is

\[
\min\left\{
\sum_Ex_E:
x_E\ge0\ (E\in F),\
\bigl|\{S\in\mathcal H_q^+:
          \sum_{E\in O_{q,S}}x_E\ge1\}\bigr|
\ge D_q\quad(q\le H)
\right\}.
\tag{6.7}
\]

### Corollary 6.2 (exact cap-regime bounds)

Under (6.1),

\[
\boxed{
\max_{q\le H}\frac{D_q}{n}
\le\min_\beta\vartheta(F,\beta)
\le b_A(F)
\le\sum_{q\le H}D_q.
}
\tag{6.8}
\]

In addition, interpreting the summand as zero when \(D_q=0\),

\[
\boxed{
b_A(F)
\le\sum_{q\le H}
\min\left\{
D_q,
\left\lceil\frac{tD_q}{\rho_q+D_q}\right\rceil
\right\}.
}
\tag{6.9}
\]

#### Proof

Fix a choice \(J_q\) in (6.6). At one depth, give every selected owner set
dual packet weight \(1/n\). Each row owns only \(n\) targets at that depth,
so the congestion is at most one. This gives fractional matching value
\(D_q/n\), proving the lower bound in (6.8). Selecting one arbitrary owner
from each of \(D_q\) chosen high cells, and taking the union over depths,
gives the last bound in (6.8).

For (6.9), at depth \(q\) the high owner hypergraph has
\(|\mathcal H_q^+|=\rho_q+D_q\) edges, each of size \(c_q+1\). Its owner
degrees sum to
\((c_q+1)|\mathcal H_q^+|\). The \(b\) highest-degree owners therefore
carry at least

\[
\frac{b(c_q+1)|\mathcal H_q^+|}{t}
\]

incidences. One high edge contributes at most \(c_q+1\) of those
incidences, so those owners hit at least
\(b|\mathcal H_q^+|/t\) distinct high labels. Taking

\[
b=\left\lceil\frac{tD_q}{|\mathcal H_q^+|}\right\rceil
\]

hits at least \(D_q\) labels. Alternatively, one owner from each of any
\(D_q\) edges uses at most \(D_q\) rows. Union these choices over \(q\) and
apply (6.5). \(\square\)

For \(q=1\) and cap \(h_S\le2\), \(D_1\) is exactly the number of holes.
The selected owner sets in (6.6) are two-element edges, recovering the
audited depth-one graph reduction as a special case. Theorem 6.1 extends it
simultaneously to every bounded capacity and preserves one common owner set.

The clean constructive target is now literal:

> **Capped common-hitter lemma (unproved).** For every fixed \(A\), construct
> one exact factor satisfying (6.1) and one common set
> \(B\subseteq F\), with \(|B|=o_A(t/\sqrt m)\), such that
> \(i_q(B)\ge D_q\) for every \(q\le H\).

By (3.6) and (6.5), this proves \(\mathrm{FSP}_A\). Within the capped regime
it is necessary up to the fixed constant \(R_A\), not merely a convenient
stronger surrogate. The histogram-only condition that the right side of
(6.9) be \(o_A(t/\sqrt m)\) is a stronger sufficient condition.

## 7. The scalar null model

The next theorem identifies exactly why a universal proof cannot come from
separate degree and margin arithmetic.

### Theorem 7.1 (abstract zero-packet common-owner model)

For every fixed \(A\) and all sufficiently large \(m\), there is an abstract
incidence system on the same \(t\) owner labels at all depths \(0\le q\le H\)
with the following properties.

1. Every depth-\(q\) target has load \(c_q\) or \(c_q+1\), with total load
   \(W\).
2. Every owner has degree exactly \(n\) at every depth.
3. For \(r_q=m-q\), every coordinate has the exact global point margin
   \(r_qt\).
4. At depth zero every middle target has load one.
5. Every survival-packet hypergraph is empty; hence
   \(\vartheta=0\) and every compressed cut is vacuous.

This incidence system need not, and is not claimed to, be an exact wreath
factor.

#### Proof

Fix a depth \(q\), abbreviate \(r=r_q\), \(N=N_q\), \(c=c_q\), and
\(\rho=\rho_q\). First choose a simple \(r\)-uniform family
\(\mathscr D_q\subseteq\binom{[n]}r\) of size \(\rho\) which is regular on
coordinates.

The required common degree is

\[
d=\frac{r\rho}{n}
=rt-c\binom{n-1}{r-1},
\tag{7.1}
\]

which is an integer. To prove existence, among all \(\rho\)-element simple
\(r\)-uniform families choose one minimizing the sum of squared coordinate
degrees. If two coordinates \(x,y\) have degrees
\(d_x\ge d_y+2\), there is an edge containing \(x\) but not \(y\) whose
replacement \(x\mapsto y\) is absent. Indeed, otherwise the replacement
map injects all \(x\)-not-\(y\) edges into the \(y\)-not-\(x\) edges, forcing
\(d_x\le d_y\). Performing the absent replacement preserves simplicity and
decreases the degree-square sum by

\[
(d_x-1)^2+(d_y+1)^2-d_x^2-d_y^2
=-2(d_x-d_y)+2<0,
\]

a contradiction. Thus all coordinate degrees differ by at most one. Their
average is the integer \(d\), so all equal \(d\).

Set

\[
\beta_q(S)=c+1\quad(S\in\mathscr D_q),\qquad
\beta_q(S)=c\quad(S\notin\mathscr D_q).
\tag{7.2}
\]

This quota is balanced, and its point margin at coordinate \(i\) is

\[
c\binom{n-1}{r-1}+d=rt.
\tag{7.3}
\]

Now enumerate the \(N\) target labels as \(a_1,\ldots,a_N\), enumerate the
abstract owners cyclically as \(E_0,\ldots,E_{t-1}\), and put

\[
L_j=\sum_{i<j}\beta_q(a_i),\qquad
O_{a_j}=\{E_{(L_j+s)\bmod t}:0\le s<\beta_q(a_j)\}.
\tag{7.4}
\]

For fixed \(A\), \(\beta_q(a_j)\le R_A-1<t\) for large \(m\), so every
owner set in (7.4) is simple. The concatenated slots run through

\[
\sum_j\beta_q(a_j)=W=nt
\]

consecutive residues modulo \(t\), so every owner occurs exactly \(n\)
times. The target loads are \(h_{a_j}=|O_{a_j}|=\beta_q(a_j)\), and (7.3)
gives the desired global point margins. Carry out the construction
independently at every depth on the same owner labels. At depth zero,
\(N_0=W,c_0=1,\rho_0=0\), so all owner sets are singletons and every middle
label is uniquely owned.

Since \(h_a=\beta(a)<\beta(a)+1=k_a\) everywhere, there is no survival
packet. This proves all five assertions. \(\square\)

The model does **not** say that the \(n\) target labels assigned to one owner
are the cyclic intervals of one coordinate order. It also imposes no
cross-depth nesting and does not ensure that the depth-zero labels belonging
to one owner form one middle wreath. Those are exactly the constraints
discarded by the abstract model.

Consequently any proof of a universal positive packet lower bound must use
per-owner cyclic realizability and/or common cross-depth nesting. Separate
load totals, owner degrees, global point margins, balanced quota arithmetic,
and the compressed cut inequalities on arbitrary incidence systems leave a
literal zero-value null state.

## 8. What the known noncanonical constructions do and do not show

The following results are audited inputs, not new claims of this report.

1. For the canonical MSW factor, every balanced quota system containing
   depth one satisfies
   \[
   \vartheta(F_m^{\rm MSW},\beta)
   \ge\operatorname {Cat}_{m-4}
   =\left(\frac1{256}+O(m^{-1})\right)t.
   \tag{8.1}
   \]
   This is a matching of pairwise disjoint survival packets. It is stable
   under \(d\) row replacements with lower bound
   \((\operatorname {Cat}_{m-4}-d)_+\).
2. The genuine switched factor \(F_m^\dagger\) removes the displayed
   canonical packet family, but prefix suspension supplies another disjoint
   family of size
   \[
   \operatorname {Cat}_{m-4}-\operatorname {Cat}_{m-6}
   =\left(\frac{15}{4096}+O(m^{-1})\right)t.
   \tag{8.2}
   \]
   More generally, bounded-prefix-cylinder rebundlings retain at least
   \(\operatorname {Cat}_{m-5}\sim t/1024\) packets.
3. At \(m=4\), there is a certified exact \(14\)-wreath factor whose
   depth-one loads consist of \(42\) singles and \(42\) doubles, with no
   holes and no triples. Assigning upper quota two to the doubles gives an
   empty depth-one packet hypergraph. This is a genuine finite-dimensional
   cyclic null state, but it is neither an all-\(m\) construction nor a
   full-window FSP witness.

Thus the universal obstruction is not a parity, total-degree, point-margin,
or depth-one finite-dimensional theorem. Conversely, the first explicit
noncanonical repairs remain in a positive-density prefix-suspension basin.
Any successful factor must globally rebundle a positive fraction of the
rows, meet essentially every primitive first-return class, and still realize
all depths by one common family of cyclic owners.

## 9. Exact remaining lemmas

There are two endpoint lemmas, and no theorem here selects between them.

### Universal endpoint

The exact cut-dual statement is:

> **Actual-owner cut expansion (unproved).** For every fixed \(A\), there is
> \(c_A>0\) such that, for every sufficiently large \(m\), every exact factor
> \(F\), and every balanced quota system, there are \(Y_a\ge0\) with
> \[
> \sum_aY_a\ge c_At
> \]
> and
> \[
> \sum_aY_a(k_a-|O_a\setminus Z|)_+\le|Z|
> \quad(Z\subseteq F).
> \]

By Theorem 2.1 this is exactly the desired universal lower bound. By
Theorem 3.1 it is equivalent up to \(R_A\) to the smaller combinatorial
statement that every actual packet hypergraph contains \(\Omega_A(t)\)
pairwise vertex-disjoint packets.

A sufficient but non-equivalent one-depth replacement is the asymptotic
first-shadow separation

\[
\min_{\beta_1}\|\mu_1^F-\beta_1\|_1\ge\delta W
\tag{9.1}
\]

for every exact factor. It would imply the universal endpoint by (5.9), but
it is unproved; the exact \(m=4\) zero-defect factor rules out any proof based
only on dimension-free parity or margin identities.

### Constructive endpoint

Without any cap hypothesis, the exact quota-free target is:

> **Residual balancing construction (unproved).** Construct one exact factor
> \(F\) and one common row set
> \(B\subseteq F\), with \(|B|=o_A(t/\sqrt m)\), such that at every
> \(q\le H\) the residual loads satisfy (3.3)--(3.4).

By Theorem 3.2 this is equivalent, within \(R_A\), to
\(\mathrm{FSP}_A\). Under the natural cap (6.1), its smallest form is the
capped common-hitter lemma following Corollary 6.2.

Theorem 7.1 proves that the residual target is feasible in a model retaining
all separate scalar margins. The unresolved obstruction is therefore not
quota choice, fractional Hall, bounded-rank rounding, or marginal balance.
It is the realization of the nearly balanced incidence pattern by one exact
family of cyclic wreaths with common nested ownership across all controlled
depths.

## 10. Adversarial audit ledger

The following potential overclaims have been checked explicitly.

1. **The two proposed asymptotic branches are not called exhaustive.**
   Equation (0.1) preserves the intermediate regime.
2. **Minimizing quotas does not interchange an invalid min and max.**
   Theorem 3.2 first characterizes, for a fixed deleted set \(B\), whether
   some balanced quota dominates its residual loads; only then are the two
   finite minima taken.
3. **The same owners are used at every depth.** Conditions (3.3)--(3.4),
   (6.5), and (6.7) use one common \(B\) or one common weight vector \(x\).
   No depthwise factor or owner reassignment occurs.
4. **Parallel owner sets cause no quota error.** They are labelled when
   selecting the \(D_q\) low-quota high cells. Their repeated fractional
   cover inequalities may be deleted only after the quota labels have been
   counted.
5. **The matching upper bound is valid.** It uses the union of a maximal
   packet matching as a vertex cover; maximum implies maximal. It does not
   assert integrality of the fractional matching polytope.
6. **The incidence-energy certificate has the correct normalization.** One
   owner has \(n\) incidences at one depth and \(nH\) over the window. This
   yields \(\Xi_q/n\), not \(\Xi_q\), as the automatic dual lower bound.
7. **The cap formula is genuinely exact.** Under (6.1), a high lower-quota
   cell has exactly one packet, its entire owner set; a nonhigh cell has none.
   No unlisted packet survives.
8. **The abstract null model is not promoted to a factor.** It satisfies
   global point margins but not per-owner cyclic intervals, middle-wreath
   grouping, or cross-depth nesting. It is an obstruction to scalar proofs,
   not an FSP construction.
9. **Known canonical results are basin results.** Their positive Catalan
   matchings exclude the canonical and bounded-prefix architectures, not the
   whole exact-factor fibre.

An independent adversarial audit checked Sections 3--7 theorem by theorem.
It confirmed the matching inequalities, both directions of quota elimination,
the \(n\)-normalized cut certificates, depth-one quota optimization, the cap
identity and quota minimization, the top-degree estimate (6.9), and the
regular-hypergraph exchange in Theorem 7.1. It found two presentation defects,
now repaired:
(6.7) needed the explicit constraint \(x_E\ge0\), and the proof of (3.6) now
uses the integral maximal-matching cover proved in Theorem 3.1. No other
theorem-level correction was found. Every lemma explicitly labelled
“unproved” remains a genuine gap; no endpoint of (0.1) is claimed.
