# Lane O master redirect: Gaussian boundary saturation for integral prefix freezing

## Outcome

There is an exact obstruction to the proposed robust-flow implementation of
common-owner prefix freezing.

Fix \(A>0\) and \(K=\lceil A\sqrt m\rceil\). At a positive-length
subinterval of the Gaussian window, the balanced quota is \(1/2\). If
integral stopping depths are upper-safe, have permanent weighted cost
\(o(W)\), and their residual Boolean suffix network satisfies all Hoffman
cuts, then at every rank in that subinterval the frozen load has the
following forced form:

\[
\begin{split}
\#\{S:g_q(S)=0\}&=o(W/\sqrt m),\\
\#\{S:g_q(S)=2\}&=\rho_q+o(W/\sqrt m),
\end{split}
\tag{0.1}
\]

where \(W=N_q+\rho_q\), and uniformly

\[
\rho_q\ge (\gamma_A+o(1))W
\tag{0.2}
\]

for an explicit constant \(\gamma_A>0\). Thus a positive density of
residual nodes has **zero upper capacity** at each of
\(\Theta_A(\sqrt m)\) consecutive layers. In fact the number of such
nodes differs from the arithmetically forced number \(\rho_q\) by at most
the number \(R_q\) of already released owners.

Consequently, any theorem which leaves one unit of residual upper slack at
every node, or outside \(o(W)\) exceptional nodes, has cost
\(\Omega_A(W\sqrt m)\), not \(o(W)\). This statement is integral,
factor-independent, and therefore remains valid inside every literal exact
wreath factor.

Two further exact no-go statements are proved below. Coordinate relabeling
does not change the optimal permanent-prefix cost of an exact factor, and a
relabeling chosen independently of a fixed balanced resolution has expected
cost \(\Omega_A(W\sqrt m)\). Also, individual exact middle
\(t\)-star totals and cyclic span geometry alone give no positive
lower-star expansion at logarithmic \(t\); the first genuine mixed-star
restriction is proved and shown to be quantitatively subcritical.

These results close the robust-slack, optimized-intrinsic orbit-improvement,
and uniform independent orbit-averaging versions of the prefix-freezing
lane. For star arguments they prove a narrower result: the individual
exact \(t\)-star total plus row-span identity has a zero forced envelope,
and the first displayed \((q+1)\)-fold disjoint mixed constraint is
subcritical. They do **not** exhaust higher mixed/union-star correlations,
or disprove a singular boundary solution of all Hoffman inequalities.
Such a solution would have to operate with the nearly forced \(1/2\)
histogram (0.1), not in the interior of the capacity polytope.

## 1. Integral setup

Put

\[
n=2m+1,\qquad W=\binom{n}{m},\qquad
V_q=\binom{[n]}{m-q},\qquad N_q=|V_q|,
\]

and write the Euclidean division

\[
W=c_qN_q+\rho_q,\qquad
c_q=\left\lfloor\frac{W}{N_q}\right\rfloor,\qquad
0\le \rho_q<N_q.
\tag{1.1}
\]

An integral nested owner system consists of one path

\[
L_0(X)=X\supset L_1(X)\supset\cdots\supset L_K(X),\qquad
|L_q(X)|=m-q,
\]

for every \(X\in V_0\). In the exact-wreath application these are the
oriented canonical deletion flags of one exact middle wreath factor. None
of Theorems 3.1 or 5.1 below uses more than integrality of the paths.

Choose a stopping depth \(a(X)\in\{0,\ldots,K\}\). Define

\[
g_q(S)=\#\{X:a(X)\ge q,\ L_q(X)=S\},\qquad
R_q=\#\{X:a(X)<q\}.
\tag{1.2}
\]

Thus \(g_q\) is the frozen load and \(R_q\) is the amount of residual flow
at layer \(q\). In particular,

\[
\sum_{S\in V_q}g_q(S)=W-R_q,\qquad
0=R_0\le R_1\le\cdots\le R_K.
\tag{1.3}
\]

The permanent weighted release cost is

\[
\mathcal C_A(a)
=\sum_{X\in V_0}\sum_{q>a(X)}\frac1{c_q}
=\sum_{q=1}^K\frac{R_q}{c_q}.
\tag{1.4}
\]

The frozen load is **upper-safe** if

\[
g_q(S)\le c_q+1
\tag{1.5}
\]

for every \(q,S\). An integral balanced residual completion is a nested
suffix flow of mass \(R_q\) at layer \(q\), with node loads \(h_q(S)\ge0\),
such that

\[
b_q(S):=g_q(S)+h_q(S)\in\{c_q,c_q+1\}
\tag{1.6}
\]

for all \(q,S\). Since \(\sum_Sb_q(S)=W\), exactly \(\rho_q\) nodes have
final load \(c_q+1\).

## 2. Exact Hoffman criterion, included to fix the boundary being studied

For \(q<K\), let

\[
\sigma_q(S)=\#\{X:a(X)=q,\ L_q(X)=S\}.
\]

Put

\[
\ell_q(S)=(c_q-g_q(S))_+,\qquad
u_q(S)=c_q+1-g_q(S).
\tag{2.1}
\]

For \(B_q\subseteq V_q\), write
\(C_q=\partial B_{q-1}\subseteq V_q\) for its immediate lower Boolean
shadow. The standard split-node circulation gives the following exact
integral theorem.

### Theorem 2.1 (staircase Hoffman cuts)

Assume (1.5). An integral balanced residual suffix flow exists if and
only if, for every sequence \(B_0,\ldots,B_{K-1}\), both

\[
\begin{aligned}
\sum_{q<K}\sigma_q(B_q)
+\sum_{q=1}^{K-1}\ell_q(B_q\setminus C_q)
\le{}&
\sum_{q=1}^{K-1}u_q(C_q\setminus B_q)+u_K(C_K)
\tag{U}
\end{aligned}
\]

and

\[
\begin{aligned}
\sum_{q<K}\sigma_q(B_q)
+\sum_{q=1}^{K-1}\ell_q(B_q\setminus C_q)
+\ell_K(V_K\setminus C_K)
\le{}&
R_K+\sum_{q=1}^{K-1}u_q(C_q\setminus B_q)
\tag{L}
\end{aligned}
\]

hold.

#### Proof

For layers \(1,\ldots,K\), split every residual node into a pre-node and
post-node, joined by an arc with lower and upper capacities
\([\ell_q(S),u_q(S)]\). Layer \(0\) is post-only. Put the unbounded Boolean
inclusion arcs from every layer-\(q\) post-node to its layer-\(q+1\)
pre-neighbors. From a source \(s\), inject exactly \(\sigma_q(S)\) units
into each release post-node at layers \(0,\ldots,K-1\). Drain every
layer-\(K\) post-node into a sink \(t\), and close the circulation by the
fixed arc

\[
t\longrightarrow s
\quad\hbox{with capacity interval}\quad [R_K,R_K].
\]

A finite Hoffman cut must be closed under every unbounded inclusion arc.
After this closure is imposed, minimizing over whether each pre-node lies
on the cut gives (U) and (L), according to the side on which the fixed
return arc lies. The lower capacity \(R_K\) on that arc is exactly the
\(R_K\) term in (L). Conversely these are every finite Hoffman cut.
All capacities are integral and the split-node network matrix is totally
unimodular, so circulation feasibility gives an integral residual flow.
After deleting the fixed return arc, integral path decomposition gives
one suffix path for every released owner unit; concatenate these paths to
the corresponding frozen prefixes. This produces an integral balanced
nested owner resolution. \(\square\)

The new obstruction below is not a failure of these cuts. It describes
where every low-cost feasible point satisfying them must lie.

## 3. Exact saturation identity

For an upper-safe frozen load define

\[
Z_q=\{S\in V_q:g_q(S)=c_q+1\},\qquad
D_q=\sum_{S\in V_q}(c_q-g_q(S))_+.
\tag{3.1}
\]

Thus \(Z_q\) is exactly the set of nodes with zero residual upper capacity,
and \(D_q\) is the total residual lower demand.

### Theorem 3.1 (arithmetic saturation law)

For every integral upper-safe frozen load,

\[
\boxed{|Z_q|-D_q=\rho_q-R_q.}
\tag{3.2}
\]

If a balanced residual completion exists, then

\[
\boxed{D_q\le R_q,\qquad
       \rho_q-R_q\le |Z_q|\le\rho_q,}
\tag{3.3}
\]

and equivalently

\[
\boxed{R_q=D_q+(\rho_q-|Z_q|).}
\tag{3.4}
\]

If

\[
\mathcal H_q=\{S:b_q(S)=c_q+1\}
\]

is the final high-quota family of a particular completion, then, exactly,

\[
\boxed{Z_q\subseteq\mathcal H_q,\qquad
|\mathcal H_q\setminus Z_q|
=\rho_q-|Z_q|=R_q-D_q.}
\tag{3.4a}
\]

#### Proof

By (1.1) and (1.3),

\[
\sum_{S\in V_q}(g_q(S)-c_q)=\rho_q-R_q.
\tag{3.5}
\]

Integrality and upper-safety imply that the positive part of the left side
is exactly one for each \(S\in Z_q\), hence totals \(|Z_q|\). Its negative
part totals \(D_q\). This proves (3.2).

If a residual completion exists, its total mass at layer \(q\) is \(R_q\),
while it must supply at least \(D_q\) units to meet all lower node bounds.
Thus \(D_q\le R_q\). Equation (3.2) then gives
\(|Z_q|\le\rho_q\), as well as the lower bound in (3.3), and rearrangement
gives (3.4). Equivalently, the \(R_q\) released units split exactly into
\(D_q\) forced deficit-filling units and \(\rho_q-|Z_q|\) still-unfrozen
upper-quota units. A frozen saturated node cannot accept residual mass,
so \(Z_q\subseteq\mathcal H_q\); since \(|\mathcal H_q|=\rho_q\), this
also proves (3.4a). \(\square\)

When \(c_q=1\), put

\[
z_i(q)=\#\{S:g_q(S)=i\},\qquad i=0,1,2.
\]

Then \(D_q=z_0(q)\), \(|Z_q|=z_2(q)\), and Theorem 3.1 becomes the exact
identity

\[
\boxed{z_2(q)-z_0(q)=\rho_q-R_q.}
\tag{3.6}
\]

For a feasible residual flow,

\[
z_0(q)\le R_q,\qquad
|z_2(q)-\rho_q|\le R_q.
\tag{3.7}
\]

No expansion theorem, probabilistic estimate, or wreath property enters
these identities.

## 4. An explicit \(c_q=1\) Gaussian subband

Write

\[
\lambda_q=\frac W{N_q}
=\prod_{j=0}^{q-1}\frac{m+2+j}{m-j}.
\tag{4.1}
\]

For \(q<m\), set \(x_j=2(j+1)/(m-j)\). The elementary inequalities

\[
\frac{x}{1+x}\le\log(1+x)\le x
\]

give the exact bounds

\[
\boxed{
\frac{q(q+1)}{m+q+1}
\le \log\lambda_q
\le \frac{q(q+1)}{m-q+1}.}
\tag{4.2}
\]

Indeed, for the lower bound the \(j\)-th denominator is
\(m+j+2\le m+q+1\), while for the upper bound it is
\(m-j\ge m-q+1\), and \(\sum_{j<q}2(j+1)=q(q+1)\).

Define the explicit constants

\[
\xi_A=\min\left\{\frac A4,\frac{\sqrt{\log2}}2\right\},\qquad
\gamma_A=1-\exp(-\xi_A^2/4)>0,
\tag{4.3}
\]

and the integer interval

\[
I_m(A)=
\left[
\left\lceil\frac{\xi_A}{2}\sqrt m\right\rceil,
\left\lfloor\xi_A\sqrt m\right\rfloor
\right].
\tag{4.4}
\]

Uniformly for \(q\in I_m(A)\), (4.2) gives

\[
\log\lambda_q\le\xi_A^2+o_A(1)
\le\frac{\log2}{4}+o_A(1)<\log2,
\]

so, for all sufficiently large \(m\),

\[
\boxed{c_q=1.}
\tag{4.5}
\]

The lower half of (4.2) gives

\[
\frac{\rho_q}{W}=1-\frac1{\lambda_q}
\ge1-\exp(-\xi_A^2/4+o_A(1))
=\gamma_A+o_A(1)
\tag{4.6}
\]

uniformly on this interval. Also

\[
|I_m(A)|=(\xi_A/2+o_A(1))\sqrt m.
\tag{4.7}
\]

For a uniform bound on all \(t\le K\), put

\[
C_A=\left\lceil\exp(2(A+1)(A+2))\right\rceil.
\tag{4.8}
\]

For sufficiently large \(m\), (4.2),
\(t\le(A+1)\sqrt m\), \(t+1\le(A+2)\sqrt m\), and
\(m-t+1\ge m/2\) show

\[
c_t\le C_A\qquad(1\le t\le K).
\tag{4.9}
\]

Consequently, if

\[
H_q=\sum_{t=q}^K\frac1{c_t},
\tag{4.10}
\]

then for \(q\in I_m(A)\),

\[
\boxed{
H_q\ge\frac{K-q+1}{C_A}
\ge\frac{A-\xi_A}{C_A}\sqrt m.}
\tag{4.11}
\]

## 5. Gaussian boundary-rigidity theorem

### Theorem 5.1 (low permanent cost forces macroscopic saturation)

Fix \(A>0\). Suppose, for each \(m\), that integral stopping depths are
upper-safe, that all Hoffman inequalities (U) and (L) hold, and that

\[
\mathcal C_A(a)=o(W).
\tag{5.1}
\]

Then, uniformly for every \(q\in I_m(A)\),

\[
\boxed{R_q=o(W/\sqrt m),}
\tag{5.2}
\]

\[
\boxed{D_q=o(W/\sqrt m),\qquad
       0\le\rho_q-|Z_q|=o(W/\sqrt m),}
\tag{5.3}
\]

and for the high-quota family of every feasible completion,

\[
\boxed{|\mathcal H_q\mathbin{\triangle} Z_q|
=|\mathcal H_q\setminus Z_q|
=o(W/\sqrt m).}
\tag{5.3a}
\]

and, because \(c_q=1\),

\[
\boxed{
z_0(q)=o(W/\sqrt m),\qquad
z_2(q)=\rho_q+o(W/\sqrt m)
       \ge(\gamma_A+o_A(1))W.}
\tag{5.4}
\]

Thus at each of \((\xi_A/2+o_A(1))\sqrt m\) consecutive layers, a positive
density of residual nodes has upper capacity zero.

#### Proof

The monotonicity of \(R_t\), (1.4), and (4.11) give, for each
\(q\in I_m(A)\),

\[
\mathcal C_A(a)
\ge R_q\sum_{t=q}^K\frac1{c_t}
=R_qH_q
\ge R_q\frac{A-\xi_A}{C_A}\sqrt m.
\tag{5.5}
\]

Equation (5.1) proves (5.2), uniformly. By Theorem 2.1 there is an
integral residual completion, so (3.3) gives (5.3). Equations (3.6),
(3.7), and (4.6) give (5.4), while (3.4a) gives (5.3a).
\(\square\)

The same proof gives a quantitative converse obstruction without any
little-oh notation.

### Corollary 5.2 (robust upper slack costs \(W\sqrt m\))

For every feasible upper-safe stopping scheme, every \(q\in I_m(A)\)
satisfies

\[
\boxed{
\mathcal C_A(a)
\ge
\frac{A-\xi_A}{C_A}\sqrt m\,
(\rho_q-|Z_q|)_+.}
\tag{5.6}
\]

In particular:

1. If every residual node has at least one unit of upper slack at one such
   layer, then \(Z_q=\varnothing\) and

   \[
   \mathcal C_A(a)
   \ge
   \left(
   \frac{\gamma_A(A-\xi_A)}{C_A}+o_A(1)
   \right)W\sqrt m.
   \tag{5.7}
   \]

2. More generally, if \(|Z_q|\le\zeta W\) for a fixed
   \(0\le\zeta<\gamma_A\), then

   \[
   \mathcal C_A(a)
   \ge
   \left(
   \frac{(\gamma_A-\zeta)(A-\xi_A)}{C_A}+o_A(1)
   \right)W\sqrt m.
   \tag{5.8}
   \]

3. Even allowing \(o(W)\) saturated exceptions still gives the leading
   constant in (5.7).

#### Proof

Theorem 3.1 gives

\[
R_q=D_q+\rho_q-|Z_q|\ge(\rho_q-|Z_q|)_+.
\]

Insert this in (5.5), then use (4.6). \(\square\)

This is the promised exact obstruction to robust flow. A low-cost proof
cannot first create uniform positive capacity and then invoke expansion or
generic circulation robustness: the arithmetically correct low-cost point
is on \(\rho_q+o(W/\sqrt m)\) upper facets at each critical layer.

### Exact-wreath collision consequence

Now suppose the owner paths do come from one exact oriented wreath factor
\(F\), and let \(\mu_q^F(S)\) be its full depth-\(q\) load. Since frozen
occurrences are a subset of full occurrences,

\[
g_q(S)\le\mu_q^F(S).
\]

Put

\[
P_q(F)=\sum_{S\in V_q}\binom{\mu_q^F(S)}2.
\tag{5.9}
\]

Every \(S\in Z_q\) contains two frozen occurrences, necessarily from
distinct rows, and therefore contributes at least one to \(P_q(F)\). Hence

\[
P_q(F)\ge |Z_q|.
\tag{5.10}
\]

Under the hypotheses of Theorem 5.1,

\[
\boxed{
\sum_{q\in I_m(A)}P_q(F)
\ge
\left(\frac{\xi_A\gamma_A}{2}+o_A(1)\right)W\sqrt m.}
\tag{5.11}
\]

This is an exact necessary wreath lemma. It is not an overload lower
bound: a perfectly balanced \(1/2\) profile already has exactly \(\rho_q\)
unavoidable collision pairs. The point of (5.11) is that robust-flow
arguments cannot treat collisions or zero-capacity nodes as a sparse
exception.

## 6. Intrinsic orbit invariance and uniform independent averaging

Let \(F\) be an oriented exact wreath factor. For a balanced nested
resolution \(P\), define the first disagreement depth

\[
d_{F,P}(X)=\min\{q\in[1,K]:L_q^F(X)\ne P_q(X)\},
\]

with \(d_{F,P}(X)=K+1\) if there is no disagreement. Put

\[
H_{K+1}=0,\qquad H_d=\sum_{q=d}^K\frac1{c_q},
\]

and define the optimal permanent-prefix cost of \(F\) by

\[
\Phi_K(F)=\min_{P\ {\rm balanced}}
\sum_{X\in V_0}H_{d_{F,P}(X)}.
\tag{6.1}
\]

For a fixed \(P\), the summand is exactly the cheapest permanent stopping
cost compatible with retaining the common prefix of \(L^F(X)\) and
\(P(X)\).

### Theorem 6.1 (orbit invariance and independent-alignment lower bound)

For every coordinate permutation \(\sigma\in S_n\),

\[
\boxed{\Phi_K(\sigma F)=\Phi_K(F).}
\tag{6.2}
\]

Moreover, for every fixed balanced nested resolution \(P\), if \(\sigma\)
is uniform in \(S_n\), then

\[
\boxed{
\mathbb E_\sigma
\sum_XH_{d_{\sigma F,P}(X)}
\ge
\left(1-\frac1m\right)WH_1
\ge
\left(1-\frac1m\right)\frac{A}{C_A}W\sqrt m.}
\tag{6.3}
\]

#### Proof

Transporting a resolution by \(\sigma\) preserves nesting and every balanced
quota. The correspondence \(P\mapsto\sigma P\) is a bijection, and

\[
d_{\sigma F,\sigma P}(\sigma X)=d_{F,P}(X).
\]

This proves (6.2).

Fix \(X\). Let \(\delta_\sigma(X)\in X\) be the first point deleted by the
transported factor \(\sigma F\) at root \(X\). The stabilizer of \(X\) acts
transitively on \(X\). For every \(\tau\) in this stabilizer, the bijection
\(\sigma\mapsto\tau\sigma\) gives

\[
\delta_{\tau\sigma}(X)=\tau\delta_\sigma(X).
\]

Therefore \(\delta_\sigma(X)\) is uniform on the \(m\) points of \(X\).
The fixed resolution \(P\) deletes one specified point of \(X\), so the
probability of agreement at depth one is \(1/m\). Every depth-one
disagreement contributes \(H_1\), giving the first inequality in (6.3).
The second follows from \(H_1\ge K/C_A\ge A\sqrt m/C_A\). \(\square\)

Thus relabeling one known exact factor cannot improve its optimum at all.
For a fixed balanced resolution, a **uniform independently chosen**
coordinate relabeling gives order-maximal expected permanent cost. This
average does not say that every relabeling is bad, and it does not exclude
a rare relabeling which aligns well with that fixed resolution. It does
show that uniform independent orbit averaging supplies no low-cost
expectation. Any positive theorem must correlate the factor, the
relabeling if one is used, and the balanced resolution.

Throughout this section an orientation is part of \(F\). If one also
minimizes over row orientations, transporting those orientations by
\(\sigma\) gives the same bijection, so the optimized intrinsic value
remains coordinate-orbit invariant.

## 7. Exact cyclic \(t\)-star identity and its limitation

This section checks whether exact middle ownership supplies the robust
lower-star expansion missing from Section 5. It does not.

Write an oriented row \(\rho\) as a cyclic order, and let
\(I_\rho(j,s)\) be its cyclic interval of \(s\) consecutive coordinates
starting at phase \(j\in\mathbb Z_n\). For a \(t\)-set \(T\), define

\[
h_s^\rho(T)=\#\{j:T\subseteq I_\rho(j,s)\}.
\tag{7.1}
\]

### Theorem 7.1 (row-span truncation identity)

For \(1\le t\le m\) and \(0\le q<m\),

\[
\boxed{h_{m-q}^\rho(T)=(h_m^\rho(T)-q)_+.}
\tag{7.2}
\]

If \(F\) is an exact middle wreath factor with \(B=W/n\) rows, and

\[
M_q^F(T)=\sum_{S\supseteq T}\mu_q^F(S),\qquad
G_t=\binom{n-t}{m-t},
\]

then

\[
\boxed{
M_q^F(T)=\sum_{\rho\in F}(h_m^\rho(T)-q)_+
\ge(G_t-qB)_+.}
\tag{7.3}
\]

#### Proof

List the clockwise edge gaps between consecutive points of \(T\) as
\(d_1,\ldots,d_t\), so \(\sum_i d_i=n\), and put

\[
D=\max_i d_i,\qquad \ell=n-D+1.
\]

The complement of an \(s\)-window is an \((n-s)\)-window. Thus
\(T\subseteq I_\rho(j,s)\) exactly when that complementary window lies
inside one empty gap of \(T\). A gap with edge-length \(d_i\), hence
\(d_i-1\) internal vertices, contains

\[
(d_i-(n-s))_+
\]

such complementary windows. Since \(s\le m\) and
\(n-s\ge m+1>n/2\), at most one gap can contribute. Consequently

\[
h_s^\rho(T)=\sum_i(d_i-(n-s))_+=(s-\ell+1)_+.
\tag{7.2a}
\]

In particular,

\[
h_m^\rho(T)=m-\ell+1,\qquad
h_{m-q}^\rho(T)=(m-q-\ell+1)_+,
\]

when \(\ell\le m\), and both relevant counts vanish when \(\ell>m\).
This proves (7.2), including the latter boundary case.

Exact middle ownership says that the \(m\)-windows over all rows are every
\(m\)-set once. Therefore

\[
\sum_{\rho\in F}h_m^\rho(T)=G_t.
\tag{7.4}
\]

The first equality in (7.3) follows by counting lower interval occurrences
containing \(T\), row by row. Finally
\((x-q)_+\ge x-q\) and \((x-q)_+\ge0\); summing and using (7.4) gives the
lower bound. \(\square\)

The bound can be completely vacuous well below the Gaussian scale. Take

\[
t=\lfloor\log_2 n\rfloor.
\]

Then

\[
\frac{G_t}{B}
=n\frac{(m)_t}{(n)_t}
<n2^{-t}<2.
\tag{7.5}
\]

Consequently, for every \(q\ge2\), the forced lower bound in (7.3) is
zero. This zero is best possible from the numerical data
\(\sum_\rho h_m^\rho(T)=G_t\) alone: distribute the integer mass \(G_t<2B\)
among the \(B\) rows with each entry at most \(2\le q\). Such a numerical
distribution has \(\sum_\rho(h_m^\rho(T)-q)_+=0\).

This is a limitation theorem, not a construction of an exact factor with an
empty star. It proves that exact middle \(t\)-design counts plus the
row-span identity do not themselves furnish the positive lower-star
expansion or upper-capacity slack needed by a robust Hoffman argument.
Additional correlated row geometry or higher mixed exact-cover data would
be essential.

There is, however, one genuine mixed exact-cover restriction. Its exact
size shows why it still does not reach the prefix-freezing obstruction
scale.

### Theorem 7.2 (disjoint mixed-star inequality)

Let \(1\le q<m\), and let \(T_1,\ldots,T_{q+1}\) be pairwise disjoint
\(t\)-sets with
\((q+1)t\le m\). Then every exact middle wreath factor satisfies

\[
\boxed{
\sum_{i=1}^{q+1}M_q^F(T_i)
\ge(q+1)G_{(q+1)t},\qquad
G_u=\binom{n-u}{m-u}.}
\tag{7.6}
\]

More generally, if \((q+1)t\le m\), then for \(r\ge q+1\) pairwise
disjoint \(t\)-sets,

\[
\boxed{\sum_{i=1}^rM_q^F(T_i)\ge rG_{(q+1)t}.}
\tag{7.7}
\]

In particular, at most \(q\) members of a pairwise disjoint family can
have completely empty depth-\(q\) stars.

#### Proof

Fix one cyclic row \(\rho\), and let \(P_i\subseteq\mathbb Z_n\) be the
cyclic interval of middle-window starts whose windows contain \(T_i\).
Write \(\rho_j\) for the coordinate occupying phase \(j\).
Its length is

\[
x_i=|P_i|=h_m^\rho(T_i).
\]

If \(c=|\bigcap_iP_i|=0\), the rowwise inequality below is trivial.
Otherwise lift all \(P_i\) to integer intervals
\([a_i,b_i]\) about one common start. This lift is unique after fixing the
common phase because
\(|P_i|=h_m^\rho(T_i)\le m-t+1\le m<n/2\). Put

\[
A=\max_i a_i,\qquad C=\min_i b_i,\qquad c=C-A+1.
\]

At the last allowed start \(b_i\), shifting the middle window one step
forward loses the coordinate \(\rho_{b_i}\); hence
\(\rho_{b_i}\in T_i\). At the
first allowed start \(a_i\), shifting one step backward loses the
coordinate \(\rho_{a_i+m-1}\); hence
\(\rho_{a_i+m-1}\in T_i\). Since the \(T_i\) are disjoint and \(\rho\)
is a cyclic bijection, all \(a_i\)'s are distinct modulo \(n\), as are all
\(b_i\)'s. Their chosen lifts are therefore distinct integers. There are
\(q+1\) of each. Therefore

\[
\sum_i a_i\le(q+1)A-\frac{q(q+1)}2,
\qquad
\sum_i b_i\ge(q+1)C+\frac{q(q+1)}2.
\]

Since \(x_i=b_i-a_i+1\),

\[
\sum_i x_i\ge(q+1)(c+q).
\]

It follows that

\[
\sum_i(x_i-q)_+\ge\sum_i(x_i-q)\ge(q+1)c.
\tag{7.8}
\]

Sum (7.8) over the rows of \(F\). The left side becomes
\(\sum_iM_q^F(T_i)\) by (7.3). The sum of the common-intersection sizes
\(c\) counts middle owners containing the disjoint union
\(\bigcup_iT_i\). Exact middle ownership makes that count exactly
\(G_{(q+1)t}\), proving (7.6).

Apply (7.6) to every \((q+1)\)-subfamily of \(T_1,\ldots,T_r\).
Every \(M_q^F(T_i)\) occurs \(\binom{r-1}{q}\) times, whereas

\[
(q+1)\binom r{q+1}=r\binom{r-1}q.
\]

Division proves (7.7). \(\square\)

For \(t=\lfloor\log_2 n\rfloor\),

\[
\frac{G_{(q+1)t}}B
=n\frac{(m)_{(q+1)t}}{(n)_{(q+1)t}}
<n2^{-(q+1)t}
<\frac{2^{q+1}}{n^q}.
\tag{7.9}
\]

Thus, whenever \((q+1)t\le m\), the exact mixed restriction rules out
\(q+1\) simultaneous empty disjoint stars, but the lower-star occurrence
mass forced by (7.6) is \(o(B)\) at every \(q\ge1\),
and therefore cannot by itself exclude a fixed \(\eta B\) Hall deficit.
In the Gaussian regime,
an empty logarithmic star contains only \(\Theta_A(B)=\Theta_A(W/m)\)
quota cells. The saturation theorem permits the larger scale
\(o(W/\sqrt m)=o(B\sqrt m)\), which still allows \(\Theta(B)\) holes.
Hence Theorem 7.2
and Gaussian saturation are quantitatively compatible; their combination
does not give an exact-factor prefix impossibility. Theorem 7.2 is also a
same-depth statement; it does not couple one protected logarithmic star at
each of several different depths.

### Known exact packet obstructions are also subcritical

The two packet-cardinality facts in this paragraph are imported audited
theorems, respectively from
MATH_ATTACK_AA6_OWNER_RECOURSE_AND_ORBIT_CAPACITY_20260725.md and
MATH_ATTACK_G_PACKET_CUT_DUAL_DICHOTOMY_20260725.md; the stopping-cost
comparison is made here. The strongest presently certified depth-one
exact-factor packet families have Catalan, not critical, size. For the
canonical MSW factor, the
pairwise row-disjoint load-three targets force

\[
R_1\ge \operatorname{Cat}_{m-4}
=\left(\frac1{256}+O(m^{-1})\right)B.
\tag{7.10}
\]

After the audited switched repair destroys that displayed family, prefix
suspension supplies a different disjoint family of size

\[
\operatorname{Cat}_{m-4}-\operatorname{Cat}_{m-6}
=\left(\frac{15}{4096}+O(m^{-1})\right)B.
\tag{7.11}
\]

Either lower bound contributes only

\[
\Theta(B)H_1=\Theta_A(B\sqrt m)
=\Theta_A(W/\sqrt m)=o(W)
\tag{7.12}
\]

to permanent cost. A literal exact-factor counterexample at depth one
would need

\[
R_1=\Omega(W/\sqrt m)=\Omega(B\sqrt m),
\tag{7.13}
\]

a further factor \(\sqrt m\) beyond (7.10)--(7.11). Thus the known exact
MSW packets close row-exceptional scales, but do not close individual-owner
prefix freezing.

## 8. Quantitative composition into the constant-one route

The preceding theorems are negative architecture results, but it is useful
to state exactly what a surviving boundary theorem would imply.

Suppose that for every fixed \(A>0\) and all sufficiently large \(m\), one
constructs:

1. one integral exact oriented middle wreath factor \(F_m\);
2. integral owner stopping depths \(a(X)\);
3. upper-safe frozen loads satisfying every cut (U) and (L); and
4. permanent cost \(\mathcal C_A(a)=o(W)\).

Theorem 2.1 then supplies an integral balanced nested residual flow \(P\).
Every owner frozen through depth \(q\) agrees there, so the labelled mismatch

\[
e_q(F_m,P)=\#\{X:L_q^{F_m}(X)\ne P_q(X)\}
\]

satisfies

\[
e_q(F_m,P)\le R_q.
\]

Therefore

\[
\boxed{
\sum_{q=1}^K\frac{e_q(F_m,P)}{c_q}
\le\mathcal C_A(a)=o(W).}
\tag{8.1}
\]

This is precisely the integral fixed-window labelled synchronization input
to the audited literal common-owner construction. That construction stays
inside the exact middle factor and turns (8.1) into a contiguous-OR word
whose central-window length is \(W+o(W)\). Solving this for every fixed
\(A\), followed by the already audited diagonalization and outer-tail
argument, yields

\[
\nu(k)\le(1+o(1))W(k).
\]

No fractional factor, fractional owner, or nonliteral existential projection
is used in this implication.

Theorems 5.1, 6.1, and 7.1 show that such a proof cannot be obtained by any
of the following mechanisms:

- creating positive residual upper slack at all but \(o(W)\) nodes and then
  applying a robust-flow theorem;
- choosing a good coordinate relabeling from the orbit of one known exact
  factor;
- using a uniform coordinate relabeling independent of one fixed balanced
  resolution as a low-expected-cost alignment; or
- deriving the needed expansion only from exact middle \(t\)-star counts
  and the rowwise cyclic-span formula.

The last bullet concerns the individual marginal identity (7.3) and the
subcritical disjoint mixed constraint (7.6). It does not rule out an
argument using the full hierarchy of mixed or union-star exact-cover
correlations, which has not been classified here.

The sole surviving form of this lane is a boundary theorem: at every
\(q\in I_m(A)\), almost every lower-quota cell must already have frozen load
one, almost exactly \(\rho_q\) cells must already have frozen load two, and an
\(o(W/\sqrt m)\)-mass residual flow must satisfy every multilevel staircase
cut through this positive-density zero-capacity boundary.

## 9. Exact scope and unproved lemmas

The following statements are proved in this report:

1. the exact integral saturation and high-family identities
   (3.2)--(3.4a);
2. the explicit Gaussian constants (4.3)--(4.11);
3. the uniform boundary-rigidity theorem (5.2)--(5.4);
4. the \(W\sqrt m\) robust-slack lower bounds (5.6)--(5.8);
5. the exact-factor collision consequence (5.11);
6. coordinate-orbit invariance and the independent-alignment lower bound
   (6.2)--(6.3); and
7. the cyclic row-span and exact individual-star identities (7.2)--(7.5);
8. the genuine mixed exact-factor star inequality (7.6)--(7.9); and
9. the subcritical scale comparison (7.12)--(7.13) for the audited exact
   MSW packet theorems (7.10)--(7.11).

The following statements remain **UNPROVED**:

- existence of a low-cost boundary solution satisfying every Hoffman cut;
- existence of one exact factor whose canonical flags are simultaneously
  balanced, or sufficiently close to balanced, through a fixed Gaussian
  window;
- a wreath-specific theorem turning fixed-window unlabelled overload into
  the stronger common-owner synchronization (8.1); and
- an exact-factor counterexample showing that every boundary solution has
  linear cost.

Accordingly, this report does not claim a proof or disproof of the
constant-one conjecture. It is a definitive no-go for the robust-slack,
intrinsic orbit-improvement, and uniform independent orbit-averaging
implementations of permanent prefix freezing.

## 10. Independent audit record

The decisive calculations were independently rederived.

- From \(W=c_qN_q+\rho_q\) and
  \(\sum_Sg_q=W-R_q\), the signed excess is exactly
  \(\rho_q-R_q\). Under the integral upper bound \(g_q\le c_q+1\), its
  positive part is \(|Z_q|\), with no missing multiplicity. The sign in
  (3.2) is therefore fixed.
- The conclusion \(D_q\le R_q\), and hence \(|Z_q|\le\rho_q\), uses
  residual feasibility. Upper-safety alone does not imply it. This
  hypothesis is stated explicitly in Theorems 3.1 and 5.1.
- Both sides of (4.2) were obtained directly from
  \(x/(1+x)\le\log(1+x)\le x\). The choice
  \(\xi_A\le\sqrt{\log2}/2\) leaves a factor-four margin below the threshold
  \(\log2\), so \(c_q=1\) is uniform on \(I_m(A)\).
- The lower density is
  \(1-e^{-\xi_A^2/4}\), not \(1-e^{-\xi_A^2}\); the factor \(1/4\) comes
  from the lower endpoint \(q=(\xi_A/2)\sqrt m\).
- Monotonicity of \(R_t\) is used in the direction
  \(\mathcal C_A\ge R_qH_q\). Since
  \(H_q\ge(A-\xi_A)\sqrt m/C_A\), \(o(W)\) cost gives the stronger rate
  \(R_q=o(W/\sqrt m)\), uniformly.
- In the \(c_q=1\) identity, \(z_0\le R_q\) again requires a feasible
  nonnegative residual completion. With that hypothesis,
  \(|z_2-\rho_q|\le R_q\) is exact.
- The collision lower bound is only the unavoidable balanced collision
  floor and is not an overload estimate. No contradiction with exact
  factors is inferred from it.
- Coordinate invariance concerns the minimum over resolutions correlated
  with the factor. The expectation in (6.3) concerns a fixed resolution
  chosen independently. These two quantifiers are not interchanged.
- The logarithmic-star calculation proves insufficiency of the displayed
  moment data, not existence of a literal exact factor attaining the zero
  numerical envelope.
- The row-span proof was checked with the cyclic gap formula
  \(h_s=\sum_i(d_i-(n-s))_+\). Since \(n-s>n/2\), at most one gap
  contributes; this handles tied short spans and the case in which no
  \(m\)-window contains \(T\).
- In Theorem 7.2, pairwise disjointness is used twice and cannot be omitted:
  it makes the \(q+1\) left boundary points distinct and the \(q+1\) right
  boundary points distinct. The binomial averaging identity is
  \((q+1)\binom r{q+1}=r\binom{r-1}q\), so no factor is lost in (7.7).
- The exact MSW packet lower bounds are only \(\Theta(B)\). Multiplication
  by the Gaussian Hardy tail gives \(\Theta(W/\sqrt m)\), not
  \(\Theta(W)\); they are therefore not exact-factor counterexamples to
  individual-owner prefix freezing.

No finite search, computation, asymptotic nonintegral rounding, or web input
is used.
