# O3: stopping-depth optimal transport, laminar packet rounding, and cyclic Hall obstructions

Date: 2026-07-25

Method: pure mathematics only. No web search, finite search, random experiment, or solver was used.

## 0. Exact outcome

Fix one oriented exact middle wreath factor. Owner stopping-depth alignment has an exact finite multi-marginal optimal-transport formulation in which one integral state is selected for each original wreath packet. Its objective is exactly

\[
\mathcal C=\sum_{q=1}^K\frac{R_q}{c_q},
\]

where \(R_q\) is the number of owners permanently released before depth \(q\). The fractional problem has an exact Kantorovich dual, so every dual potential is a weighted Hall certificate in precisely the requested units.

There are four positive integrality statements.

1. The time coordinate alone is a laminar tree transport. After a balanced resolution is fixed, grouping owners into literal cyclic arcs of size at most \(r\) multiplies the release cost by at most \(r\). Flexible row-local batches of size \(r\) incur only
   \[
   O_A(rW/\sqrt m)
   \]
   additive cost. Thus any \(r=o(\sqrt m)\) temporal packet granularity is harmless.
2. Nested hard-upper-quota survival packets have rank at most
   \[
   R_A=2+\max_{q\le K}c_q=O_A(1).
   \]
   A single threshold rounds their fractional laminar cover to integral stopping depths at cost at most \(R_A\) times fractional cost.
3. If canonical target fibers only merge and never split, the upper-cap stopping problem is an exact integral laminar flow, with an explicit antichain recursion for its optimum.
4. At one depth, selecting at most \(s_C\) released occurrences from each wreath is characterized exactly by a bipartite Hall inequality. Sequential selections using \(s_m=o(\sqrt m)\) owners per wreath have \(o(W)\) weighted cost.

None of these upper-safe theorems by itself enforces the lower capacities and all multilevel Hoffman staircase cuts of the residual Boolean network. The exact full packet state family is not known to be a polymatroid base family, and the most literal cyclic packet rules fail base exchange. The naive singleton-owner path matrix has a determinant-\(2\) minor already at two depths, although the audited fixed-release Boolean flow has a larger totally unimodular extension that neutralizes this minor.

There is also an exact Hall obstruction inside one fixed exact factor. If \(\Theta(\sqrt m)\) pairwise disjoint logarithmic coordinate stars each carry a Catalan-size floor deficit, then every balanced completion respecting permanent frozen prefixes has

\[
\mathcal C=\Omega_A(W),
\]

even though deficits of order \(W/n\) per rank are compatible in scale with \(o(W)\) weighted overload. No exact factor realizing these protected logarithmic-star deficits is constructed here. Therefore this is a theorem about what such a factor would force, not an exact-factor counterexample.

The surviving positive gate is now precise: round a fractionally cheap cyclic packet transport with \(o(\sqrt m)\) additional early releases per wreath while preserving every Boolean target quota and every residual Hoffman cut. The purely temporal, laminar, and bounded-rank parts do not obstruct this; the crossing endpoint fibers are the unresolved part.

## 1. Notation and the exact Hardy/tree cost

Put

\[
n=2m+1,\qquad
W=\binom nm,\qquad
B=\frac Wn=\operatorname{Cat}_m,
\]

\[
V_q=\binom{[n]}{m-q},\qquad
N_q=|V_q|,\qquad
c_q=\left\lfloor\frac W{N_q}\right\rfloor,
\]

and, for fixed \(A>0\),

\[
K=\lceil A\sqrt m\rceil.
\]

Uniformly for \(q\le K\),

\[
\frac W{N_q}
=\prod_{j=0}^{q-1}\frac{m+2+j}{m-j},
\qquad
\log\frac W{N_q}
=\frac{q(q+1)}m+O_A(m^{-1/2}).
\tag{1.1}
\]

Consequently, for all sufficiently large \(m\), one may use the explicit bound

\[
1\le c_q\le C_A,
\qquad
C_A:=\left\lceil e^{A^2+2}\right\rceil.
\tag{1.2}
\]

Fix one oriented exact middle wreath factor \(F\). Its \(B\) cyclic rows partition the owner set

\[
\Omega=\binom{[n]}m.
\]

For the unique pointed occurrence of \(X\) in its row, let

\[
X=L_0(X)\supset L_1(X)\supset\cdots\supset L_K(X)
\]

be the canonical factor flag. If \(P\) is a balanced nested resolution, define its first disagreement with the canonical flag by

\[
d_X(P)=\min\{q\ge1:P_q(X)\ne L_q(X)\},
\]

with \(d_X=K+1\) when there is no disagreement. The latest permanent stopping depth compatible with \(P\) is

\[
a(X)=d_X-1.
\]

Write

\[
H_d:=\sum_{q=d}^K\frac1{c_q},
\qquad H_{K+1}:=0,
\qquad
\Psi(a):=H_{a+1}.
\tag{1.3}
\]

Let

\[
D_q(P)=\{X:P_q(X)\ne L_q(X)\},
\qquad
U_q(P)=\bigcup_{s\le q}D_s(P).
\]

Then the permanently released owners before depth \(q\) are exactly \(U_q(P)\). Hence

\[
R_q=|U_q(P)|
\]

and the following identities and inequalities are exact:

\[
\boxed{
\mathcal C(F,P)
=\sum_{q=1}^K\frac{R_q}{c_q}
=\sum_{X\in\Omega}H_{d_X(P)}.
}
\tag{1.4}
\]

Moreover,

\[
\boxed{
\sum_{q=1}^K\frac{|D_q(P)|}{c_q}
\le \mathcal C(F,P)
\le \sum_{s=1}^K |D_s(P)|H_s.
}
\tag{1.5}
\]

Indeed, \(D_q\subseteq U_q\), while

\[
|U_q|\le\sum_{s\le q}|D_s|;
\]

summing and reversing the order gives the upper bound. This is the exact Hardy running-union transform responsible for the irreversibility of prefix freezing.

If \(O_q(L)\) is the minimum unlabelled overload of the canonical depth-\(q\) histogram above a balanced \(\{c_q,c_q+1\}\)-vector, then every balanced completion respecting the frozen prefixes has

\[
O_q(L)\le |D_q(P)|\le R_q.
\]

Because \(R_q\) is nondecreasing,

\[
\boxed{
\mathcal C(F,P)
\ge
\sum_{q=1}^K
\frac{\max_{s\le q}O_s(L)}{c_q}.
}
\tag{1.5a}
\]

This record-maximum lower bound is weaker than the protected-cut theorem in Section 9 but requires no packet hypothesis.

There is a literal tree-transport interpretation. Unfold all descendant flags rooted at \(X\) into the history tree \(\mathcal T_X\), and give each edge from level \(q-1\) to level \(q\) length \(1/(2c_q)\). Two depth-\(K\) histories first differing at depth \(d\) have tree distance

\[
2\sum_{q=d}^K\frac1{2c_q}=H_d.
\]

Thus

\[
H_{d_X(P)}=d_{\mathcal T_X}(L(X),P(X)).
\tag{1.6}
\]

The temporal geometry is therefore laminar and integral before history nodes with the same Boolean endpoint \((q,S)\) are identified. Those endpoint identifications are the nonlaminar part.

## 2. Exact cyclic-packet optimal transport

Let \(\mathcal C(F)\) be the set of \(B\) wreath rows. Write the owners of row \(C\) as

\[
X_{C,j},\qquad j\in\mathbb Z_n.
\]

For each row choose a finite catalog \(\Gamma_C\) of admissible joint packet states. A state \(\gamma\in\Gamma_C\) consists of:

- a nested Boolean path \(P^\gamma(X)\) through depth \(K\) for every \(X\in C\);
- a stopping depth \(a^\gamma(X)\in\{0,\ldots,K\}\) satisfying
  \[
  P_q^\gamma(X)=L_q(X)\qquad(q\le a^\gamma(X));
  \]
- any additional desired cyclic restrictions within the original row.

Define its depth-target occupancy and exact cost by

\[
h_{C,\gamma}(q,S)
=\#\{X\in C:P_q^\gamma(X)=S\},
\tag{2.1}
\]

\[
\kappa_{C,\gamma}
=\sum_{X\in C}\Psi(a^\gamma(X))
=\sum_{q=1}^K\frac{\#\{X\in C:a^\gamma(X)<q\}}{c_q}.
\tag{2.2}
\]

### Theorem 2.1 — exact packet transport ILP

The packet-constrained permanent-prefix alignment problem inside \(F\) is exactly

\[
\min
\sum_{C\in\mathcal C(F)}\sum_{\gamma\in\Gamma_C}
\kappa_{C,\gamma}x_{C,\gamma}
\tag{2.3}
\]

subject to

\[
\sum_{\gamma\in\Gamma_C}x_{C,\gamma}=1
\qquad(C\in\mathcal C(F)),
\tag{2.4}
\]

\[
c_q\le
\sum_C\sum_\gamma h_{C,\gamma}(q,S)x_{C,\gamma}
\le c_q+1
\qquad(q,S),
\tag{2.5}
\]

\[
x_{C,\gamma}\in\{0,1\}.
\tag{2.6}
\]

Every integral solution chooses one literal state for each row of the one fixed exact factor. The chosen owner paths form one common balanced nested resolution, and the objective equals \(\sum_qR_q/c_q\). Conversely, every catalog-admissible balanced alignment determines an integral solution. No factor is fractionally mixed in this equivalence.

When \(\Gamma_C\) is the Cartesian product, over the owners in \(C\), of every descendant path together with every legal stopping depth for that path, (2.3)--(2.6) is the unrestricted permanent-prefix alignment problem for the fixed factor. Restricting the catalogs is a stronger sufficient architecture.

### Theorem 2.2 — exact Kantorovich dual

Let

\[
\mathcal B=
\left\{
b: c_q\le b_{q,S}\le c_q+1,
\quad\sum_{S\in V_q}b_{q,S}=W\text{ for every }q
\right\}.
\]

Relax (2.6) to \(x_{C,\gamma}\ge0\). Its optimum is

\[
\boxed{
D_{\rm frac}
=\sup_{p}
\left[
\min_{b\in\mathcal B}\langle p,b\rangle
+\sum_C\min_{\gamma\in\Gamma_C}
\bigl(\kappa_{C,\gamma}-\langle p,h_{C,\gamma}\rangle\bigr)
\right].
}
\tag{2.7}
\]

For a fixed exact quota vector \(b\), this becomes

\[
\boxed{
D_{\rm frac}(b)
=\sup_p
\left[
\langle p,b\rangle
-\sum_C\max_{\gamma\in\Gamma_C}
\bigl(\langle p,h_{C,\gamma}\rangle-\kappa_{C,\gamma}\bigr)
\right].
}
\tag{2.8}
\]

Proof. Introduce the aggregate marginal \(b=\sum h_{C,\gamma}x_{C,\gamma}\), attach multiplier \(p\) to that equality, and minimize separately over \(b\in\mathcal B\) and over each row simplex. Finite-dimensional linear-programming duality gives (2.7). Fixing \(b\) gives (2.8). \(\square\)

The balanced term is explicit. If

\[
W=c_qN_q+\rho_q,
\qquad0\le\rho_q<N_q,
\]

and

\[
p_{q,(1)}\le\cdots\le p_{q,(N_q)},
\]

then

\[
\min_{b_q}\sum_Sp_{q,S}b_{q,S}
=c_q\sum_Sp_{q,S}+\sum_{i=1}^{\rho_q}p_{q,(i)}.
\tag{2.9}
\]

Thus (2.7) is a complete fractional Hall/Kantorovich certificate.

There is also a convenient direct Hall form. If \(p\ge0\), \(\beta>0\), and numbers \(\alpha_C\) satisfy

\[
\langle p,h_{C,\gamma}\rangle
\le \alpha_C+\beta\kappa_{C,\gamma}
\qquad(C,\gamma),
\tag{2.10}
\]

then every integral or fractional feasible alignment obeys

\[
\boxed{
\mathcal C
\ge
\frac{\langle p,c\rangle-\sum_C\alpha_C}{\beta},
}
\tag{2.11}
\]

where \(\langle p,c\rangle=\sum_{q,S}p_{q,S}c_q\). Indeed, the balanced aggregate occupancy is coordinatewise at least \(c\); sum (2.10) over the chosen row states.

### Boolean-DAG oracle when packet coupling is removed

In the unrestricted uncoupled catalog, once an owner path is fixed, the maximizing dual state uses the latest legal stopping depth: stopping earlier changes no endpoint occupancy and only increases \(\kappa\). Hence its cost is \(H_d\), where \(d\) is the path's first disagreement.

For one owner \(X\), put

\[
V_K(S)=p_K(S),
\qquad
V_q(S)=p_q(S)+\max_{T\lessdot S}V_{q+1}(T).
\tag{2.12}
\]

Then

\[
\begin{aligned}
\max_\gamma\bigl(\langle p,h_{X,\gamma}\rangle-\kappa_{X,\gamma}\bigr)
=\max\Biggl\{&
\sum_{q=1}^Kp_q(L_q(X)),\\
&\max_{1\le d\le K}
\left[
\sum_{q<d}p_q(L_q(X))-H_d
+\max_{\substack{T\lessdot L_{d-1}(X)\\T\ne L_d(X)}}V_d(T)
\right]
\Biggr\}.
\end{aligned}
\tag{2.13}
\]

The first term is the unchanged canonical flag; the term indexed by \(d\) first leaves it at depth \(d\). Thus the uncoupled fractional oracle is an ordinary longest-path calculation in the Boolean DAG. The integral cyclic joint selection and the common endpoint quotas are the remaining structure.

## 3. A conditional submodular-flow closure theorem

Augment every packet-state vector by its actual first-release count coordinates

\[
r_{C,\gamma}(d)
=\#\{X\in C:a^\gamma(X)+1=d\},
\qquad 1\le d\le K+1.
\]

Then the vector

\[
z_{C,\gamma}=(h_{C,\gamma},r_{C,\gamma})
\]

has fixed total, and

\[
\kappa_{C,\gamma}
=\sum_{d=1}^{K+1}H_dr_{C,\gamma}(d)
\]

is a modular linear functional of \(r_{C,\gamma}\). First-disagreement counts would not suffice when a packet state deliberately releases owners earlier than their path first diverges.

### Theorem 3.1 — integral polymatroid packet criterion

Suppose, as an additional hypothesis, that for every row \(C\) there is a normalized nondecreasing integer submodular rank function \(f_C\) on the same augmented coordinate set such that

\[
\{z_{C,\gamma}:\gamma\in\Gamma_C\}
=B(f_C)\cap\mathbb Z^E.
\tag{3.1}
\]

Then every fractionally feasible packet transport with integral coordinatewise quota bounds has an integral optimum of the same cost.

Proof. Polymatroid union gives

\[
\sum_CB(f_C)=B\!\left(\sum_Cf_C\right).
\]

An integral polymatroid base polytope is box-integral, so intersecting the aggregate base with the integral target-coordinate box has integral vertices. Choose an integral aggregate optimum. The integer polymatroid-union decomposition theorem splits it into integer points of the individual \(B(f_C)\); total-rank equality makes each summand a base. By (3.1), each summand is an actual packet state. The modular cost is unchanged. \(\square\)

The literal hypothesis (3.1) is essential. A projected base description or arbitrary grouped linear constraints do not suffice.

This criterion would close the fractional-to-integral step without asymptotic loss, but it fails for the most literal cyclic packet rules. Whole-wreath all-or-none release violates one-unit base exchange: exchanging one active marker between the all-active and all-released states produces a forbidden partially released state. Fixed-length cyclic intervals are not matroid bases either. For example, for \(n\ge5\), the cyclic edges \(\{0,1\}\) and \(\{2,3\}\) violate basis exchange when the element \(1\) is removed from the first edge.

Thus a useful submodular formulation would need an enlarged, genuinely exchange-closed state catalog; the raw all-or-none or circular-interval catalog is not one.

## 4. Exact packetization after a balanced resolution is fixed

This section separates finding a balanced \(P\) from packetizing its stopping times. Once \(P\) is fixed, releasing an owner earlier than \(d_X(P)\) remains feasible because \(P\) itself witnesses the suffix completion.

### Theorem 4.1 — bounded literal cyclic arcs

Partition the cyclic owner order of every wreath into half-open consecutive arcs of size at most \(r\). Treat each arc \(A\) as one indivisible stopping packet and put

\[
d(A)=\min_{X\in A}d_X(P).
\]

Stop every owner in \(A\) at depth \(d(A)-1\). Then \(P\) remains a balanced completion, and

\[
C_{\rm arc}=\sum_A|A|H_{d(A)}.
\]

If

\[
C_{\rm free}=\sum_XH_{d_X(P)},
\]

then exactly

\[
\boxed{
C_{\rm free}\le C_{\rm arc}\le rC_{\rm free}.
}
\tag{4.1}
\]

Proof. Since \(H_d\) decreases with \(d\), every owner in \(A\) has

\[
H_{d_X}\le H_{d(A)},
\]

which gives the lower bound. Some owner of \(A\) attains \(d(A)\), so

\[
|A|H_{d(A)}\le r\sum_{X\in A}H_{d_X}.
\]

Sum over the arcs. \(\square\)

Thus every fixed-size literal cyclic-arc packetization preserves an \(o(W)\) free owner-tail bound. It does not construct that bound.

### Theorem 4.2 — Ferrers--Hall batching in one row

Fix a row \(C\), and let

\[
D_q=\#\{X\in C:d_X(P)\le q\}.
\]

Set \(D_0=R_0=0\).

For an integer batch size \(r\ge1\), define

\[
R_q=\min\left\{n,r\left\lceil\frac{D_q}{r}\right\rceil\right\}.
\tag{4.2}
\]

Then

\[
D_q\le R_q\le D_q+r-1.
\tag{4.3}
\]

There is an integral schedule which releases exactly \(R_q\) row owners by depth \(q\), releases every owner no later than its deadline \(d_X\), and uses batches of size \(r\), apart from at most one residual batch.

Proof. Create \(R_q-R_{q-1}\) release slots at time \(q\), and \(n-R_K\) no-release slots at time \(K+1\). Sort owners by deadlines and slots by times. The prefix Hall inequalities are exactly \(D_q\le R_q\), so the \(i\)-th slot is no later than the \(i\)-th owner deadline. Matching in sorted order is feasible. The increments of (4.2) are multiples of \(r\), except for the single residual produced by the cap at \(n\). \(\square\)

The row surcharge is therefore

\[
\boxed{
C_{\rm batch}(C)
\le C_{\rm free}(C)+(r-1)H_1.
}
\tag{4.4}
\]

Across all \(B=W/n\) wreath rows,

\[
\boxed{
C_{\rm batch}
\le C_{\rm free}
+(r-1)\frac Wn\sum_{q=1}^K\frac1{c_q}
\le C_{\rm free}+O_A\!\left(\frac{rW}{\sqrt m}\right).
}
\tag{4.5}
\]

Hence \(r=o(\sqrt m)\) flexible row-packet granularity is asymptotically harmless.

More generally, suppose a fractional-to-integral packet rounding has cumulative release overshoot at most \(s_m\) per row at every depth. Then

\[
\boxed{
C_{\rm int}
\le C_{\rm frac}
+s_m\frac Wn\sum_{q=1}^K\frac1{c_q}
\le C_{\rm frac}+O_A\!\left(\frac{s_mW}{\sqrt m}\right).
}
\tag{4.6}
\]

The temporal cumulative distribution itself can be rounded with discrepancy less than one: if \(\bar R_{C,q}\) is nondecreasing, then

\[
\widehat R_{C,q}=\lfloor\bar R_{C,q}+\theta\rfloor
\]

is nondecreasing and satisfies

\[
|\widehat R_{C,q}-\bar R_{C,q}|<1.
\]

It may round downward, so this observation alone does not ensure deadline feasibility, target quotas, or cyclic states. Estimate (4.6) applies only to a feasible integral rounding whose cumulative counts are at most \(s_m\) above the fractional counts at every depth. The temporal discrepancy calculation shows that the exact remaining gate is endpoint-compatible packet rounding, not time-CDF rounding.

### Whole-wreath contamination

If all \(n\) owners of a wreath must share one stopping depth, put

\[
J_q=\#\{C:\exists X\in C\text{ with }d_X(P)\le q\}.
\]

Then the forced cost is exactly

\[
C_{\rm whole}=n\sum_{q=1}^K\frac{J_q}{c_q}.
\tag{4.7}
\]

For \(q\le K/2\), (1.2) gives

\[
C_{\rm whole}\ge\frac{nK}{2C_A}J_q.
\tag{4.8}
\]

Thus \(C_{\rm whole}=o(W)\) requires

\[
J_q=o_A(B/\sqrt m)
\qquad(q\le K/2).
\tag{4.9}
\]

Bounded owner packets are harmless; indiscriminate whole-row contamination is not.

## 5. Nested survival packets: a fixed-\(A\) integral rounding theorem

Fix balanced upper quotas

\[
b_q(S)\in\{c_q,c_q+1\}.
\]

At resource \((q,S)\), let

\[
\mathcal O_{q,S}=\{X:L_q(X)=S\}.
\]

A survival packet is any set

\[
P\subseteq\mathcal O_{q,S},
\qquad |P|=b_q(S)+1.
\tag{5.1}
\]

Let \(\mathcal H_q\) be the resulting resource-labelled hypergraph at depth \(q\). If

\[
x_{X,q}=\mathbf1_{\{a(X)<q\}},
\]

then \(x_{X,1}\le\cdots\le x_{X,K}\), and the frozen core satisfies every chosen upper quota if and only if

\[
\sum_{X\in P}x_{X,q}\ge1
\qquad(P\in\mathcal H_q).
\tag{5.2}
\]

Indeed, a quota is exceeded exactly when \(b_q(S)+1\) owners of the same resource all survive.

Consider the fractional nested packet-cover problem

\[
\Theta=min
\sum_{q=1}^K\frac1{c_q}\sum_Xx_{X,q}
\tag{5.3}
\]

subject to (5.2),

\[
0\le x_{X,1}\le\cdots\le x_{X,K}.
\tag{5.4}
\]

Values above one may be truncated to one.

### Theorem 5.1 — nested bounded-rank packet rounding

Put

\[
R_A:=2+\max_{q\le K}c_q\le C_A+2.
\tag{5.5}
\]

For every feasible fractional solution, define

\[
B_q=\{X:x_{X,q}\ge1/R_A\}.
\tag{5.6}
\]

Then \(B_1\subseteq\cdots\subseteq B_K\), every \(B_q\) covers \(\mathcal H_q\), and

\[
\boxed{
\sum_{q=1}^K\frac{|B_q|}{c_q}
\le R_A\Theta.
}
\tag{5.7}
\]

Proof. A survival packet has size

\[
b_q(S)+1\le c_q+2\le R_A.
\]

If it missed \(B_q\), every one of its coordinates would be strictly below \(1/R_A\), so its fractional sum would be strictly below one, contradicting (5.2). Nesting follows from (5.4), and

\[
\mathbf1_{B_q}(X)\le R_Ax_{X,q}
\]

gives (5.7). \(\square\)

Therefore a fractional nested upper-quota cover of cost \(o(W)\) gives integral owner stopping depths of cost \(o(W)\), for every fixed \(A\).

The exact laminar dual is also useful. Put

\[
z_{X,s}=x_{X,s}-x_{X,s-1},
\qquad x_{X,0}=0.
\]

Then the cost of \(z_{X,s}\) is \(H_s\), and LP duality gives

\[
\boxed{
\Theta=max\sum_{q,P}\lambda_{q,P}
}
\tag{5.8}
\]

over \(\lambda_{q,P}\ge0\) satisfying, for every owner \(X\) and release time \(s\),

\[
\boxed{
\sum_{q\ge s}\sum_{\substack{P\in\mathcal H_q\\X\in P}}
\lambda_{q,P}
\le H_s.
}
\tag{5.9}
\]

This is a suffix-capacitated fractional packet packing: an owner released at time \(s\) can pay at most its remaining tail \(H_s\).

If \(\vartheta_q\) denotes the ordinary fractional cover number of \(\mathcal H_q\), every nested feasible solution obeys

\[
\boxed{
\Theta\ge
\sum_{q=1}^K\frac{\max_{s\le q}\vartheta_s}{c_q}.
}
\tag{5.10}
\]

Indeed, \(x_{\cdot,q}\ge x_{\cdot,s}\) coordinatewise and hence has total at least \(\vartheta_s\) for every \(s\le q\). In particular, \(o(W)\) nested cover cost forces

\[
\vartheta_s=o(W/\sqrt m)
\qquad(s\le K/2).
\tag{5.11}
\]

There is a literal whole-wreath version. Replace the owner vertices by rows \(C\), with

\[
\mathcal O_{q,S}^{\rm row}
=\{C:S\text{ is a canonical depth-}q\text{ window of }C\}.
\]

A row contributes at most one occurrence to a fixed \(S\), so the same survival-packet equivalence and the same factor-\(R_A\) threshold hold. The owner-scaled cost is

\[
n\sum_q\frac{|B_q^{\rm row}|}{c_q}.
\]

This gives a rigorous integral common-wreath upper-quota stopping theorem, conditional only on a cheap fractional nested row cover. It still does not assert that the released suffixes can meet every lower quota.

## 6. One-depth row-cap Hall theorem

At a fixed depth \(q\), let

\[
H_{C,q}=\{L_q(X):X\in C\}.
\]

The \(n\) members of \(H_{C,q}\) are distinct. Let \(\delta(S)\) be a nonnegative integral number of occurrences of target \(S\) which must be released, and allow at most \(s_C\) released owners from row \(C\).

### Theorem 6.1 — exact capacitated Hall criterion

There is an integral selection of owner occurrences meeting every demand \(\delta(S)\) and using at most \(s_C\) owners from each row if and only if, for every \(\mathcal U\subseteq V_q\),

\[
\boxed{
\delta(\mathcal U)
\le
\sum_C\min\{s_C,|H_{C,q}\cap\mathcal U|\}.
}
\tag{6.1}
\]

Proof. Use a network

\[
\text{source}\longrightarrow S\longrightarrow C\longrightarrow\text{sink},
\]

with required total outflow \(\delta(S)\) from target \(S\), unit capacities on occurrence arcs \(S\to C\), and capacity \(s_C\) on \(C\to\)sink. For a target set \(\mathcal U\), minimizing the cut over whether each row accompanies \(\mathcal U\) contributes

\[
\min\{s_C,|H_{C,q}\cap\mathcal U|\}.
\]

Max-flow/min-cut gives (6.1), and integral capacities give an integral occurrence selection. \(\square\)

A natural demand is the frozen upper excess

\[
\delta_q(S)=(\mu_q(S)-c_q-1)_+.
\tag{6.2}
\]

Suppose Theorem 6.1 can be applied sequentially to the current active occurrences so that:

- each selected owner is new;
- every frozen upper excess is removed;
- every wreath loses at most \(s_m\) owners in total.

Then at most \(Bs_m\) owners are released, each at cost at most \(K\), and therefore

\[
\boxed{
\mathcal C
\le Bs_mK
=O_A\!\left(\frac{Ws_m}{\sqrt m}\right).
}
\tag{6.3}
\]

Thus \(s_m=o(\sqrt m)\), and in particular \(s_m=O_A(1)\), gives \(o(W)\) upper-safe release cost. The multidepth difficulty is to make the selections persistent and simultaneously compatible with the residual lower bounds; independent applications of (6.1) do not do that.

## 7. Exact laminar upper-cap flow and deterministic laminarization

For every depth-target pair define the owner fiber

\[
E_{q,S}=\{X:L_q(X)=S\}.
\]

### Theorem 7.1 — exact coarsening-fiber recursion

Assume the canonical fiber partitions coarsen with depth:

\[
L_q(X)=L_q(Y)
\Longrightarrow
L_{q+1}(X)=L_{q+1}(Y).
\tag{7.1}
\]

Thus, once two owners collide, they never split later. Regard equal subsets at consecutive times as distinct time-expanded nodes. The nonempty fibers form a rooted laminar forest. For a node \(V=E_{q,S}\), put

\[
\delta(V)=(|V|-c_q-1)_+.
\tag{7.2}
\]

If the children of \(V\) are its depth-\((q-1)\) fibers, define

\[
\boxed{
r(V)=\max\left\{\delta(V),
\sum_{U\text{ child of }V}r(U)\right\}.
}
\tag{7.3}
\]

Then \(r(V)\) is the componentwise-minimal integral number of owners which must have been released from \(V\) by depth \(q\) in order to enforce

\[
g_q(S)\le c_q+1
\]

at every layer. Consequently, the exact upper-cap-only optimum is

\[
\boxed{
D_{\rm lam}
=\sum_{q=1}^K\frac1{c_q}
\sum_{V\text{ at depth }q}r(V).
}
\tag{7.4}
\]

Proof. Any feasible released count \(y(V)\) must be at least \(\delta(V)\), and it must contain all releases inherited from the disjoint children:

\[
y(V)\ge\sum_Uy(U).
\]

Induction gives \(y(V)\ge r(V)\). Conversely, after carrying the child releases into \(V\), release exactly

\[
r(V)-\sum_Ur(U)
\]

additional active owners. This is possible because \(r(V)\le|V|\). Condition (7.1) ensures no owner identities have to be separated again. \(\square\)

Equivalently, \(r(V)\) is the maximum total \(\delta\)-weight of an antichain in the descendant subtree of \(V\). Also,

\[
r(V)\le\sum_{U\text{ descendant of }V}\delta(U).
\]

Writing

\[
D_q^+=\sum_{S\in V_q}(\mu_q(S)-c_q-1)_+,
\]

one obtains

\[
\boxed{
D_{\rm lam}
\le\sum_{q=1}^KD_q^+H_q.
}
\tag{7.5}
\]

Thus the right side being \(o(W)\) is sufficient for integral upper-safe laminar stopping under (7.1).

Actual factor fibers can merge and later split, so (7.1) is not automatic. There is nevertheless a deterministic pruning theorem which pays explicitly for splits.

For \(0\le q<K\), define

\[
\kappa_q(F)
=\sum_{S\in V_q}
\left[
\mu_q(S)-
\max_{\substack{T\subset S\\|T|=|S|-1}}
\#\{X:L_q(X)=S,\ L_{q+1}(X)=T\}
\right].
\tag{7.6}
\]

### Theorem 7.2 — split-defect pruning

There are individual-owner stopping depths for which

- every frozen load satisfies \(g_q(S)\le c_q+1\);
- no surviving collision ever splits at the next depth;
- the total cost is at most
  \[
  \boxed{
  \sum_{q=0}^{K-1}\kappa_q(F)\Psi(q)
  +\sum_{q=1}^KD_q^+\Psi(q-1).
  }
  \tag{7.7}
  \]

Proof. At an active fiber \(S\) at depth \(q\), retain the most frequent active child and stop every minority-child owner at depth \(q\). If the raw child counts are \(a_t\), if \(t_0\) maximizes them, and if the active counts satisfy \(b_t\le a_t\), then

\[
\sum_tb_t-\max_tb_t
\le\sum_tb_t-b_{t_0}
\le\sum_{t\ne t_0}a_t.
\]

Thus the number stopped after depth \(q\) is at most the corresponding summand of \(\kappa_q\), and each costs \(\Psi(q)\). Before layer \(q\), also stop enough active owners to reduce every load to \(c_q+1\). Since active load is no larger than the original \(\mu_q\), this uses at most \(D_q^+\) owners, each costing \(\Psi(q-1)\). Removing owners preserves every earlier no-split property. Summing proves (7.7). \(\square\)

Theorem 7.2 constructs an upper-safe stop pattern, not the suffix paths. It neither preserves whole-wreath release nor proves the residual Hoffman cuts.

## 8. The exact residual Hoffman gate

For arbitrary stopping depths, define

\[
g_q(S)=\#\{X:a(X)\ge q,\ L_q(X)=S\},
\]

and, for \(q<K\),

\[
\sigma_q(S)=\#\{X:a(X)=q,\ L_q(X)=S\}.
\]

Put

\[
R_K=\sum_{q<K}\sigma_q(V_q),
\qquad
\ell_q(S)=(c_q-g_q(S))_+,
\qquad
u_q(S)=c_q+1-g_q(S).
\tag{8.1}
\]

Assume \(g_q(S)\le c_q+1\). For arbitrary \(B_q\subseteq V_q\), let

\[
C_q=\partial B_{q-1}\subseteq V_q.
\]

The audited fixed-stop theorem says that an integral residual suffix flow exists if and only if, for every \(B_0,\ldots,B_{K-1}\), both

\[
\sum_{q<K}\sigma_q(B_q)
+\sum_{q=1}^{K-1}\ell_q(B_q\setminus C_q)
\le
\sum_{q=1}^{K-1}u_q(C_q\setminus B_q)
+u_K(C_K),
\tag{U}
\]

and

\[
\sum_{q<K}\sigma_q(B_q)
+\sum_{q=1}^{K-1}\ell_q(B_q\setminus C_q)
+\ell_K(V_K\setminus C_K)
\le
R_K+\sum_{q=1}^{K-1}u_q(C_q\setminus B_q).
\tag{L}
\]

For fixed stops, these are exactly Hoffman's cuts in the split Boolean network; integral capacities give an integral suffix flow.

Theorems 5.1, 6.1, 7.1, and 7.2 ensure only that every \(u_q(S)\) is nonnegative. They do not imply (U) and (L). This is the precise reason the upper-cap packet theorems are not yet a synchronization theorem.

There is no proved generic submodular-flow collapse of the joint stop-and-residual problem. For example, when a target initially has \(c+1\) frozen owners and \(R\) of them are released, its residual lower requirement is

\[
\ell(R)=(|R|-1)_+.
\tag{8.2}
\]

This function is supermodular, the correct sign for a generalized-polymatroid lower bound; it is therefore not by itself an obstruction. What remains unproved is the required cross-paramodularity among these lower bounds, the upper bounds, the release supplies, the crossing cyclic-row partitions, and every staircase preimage in (U) and (L). No violation of all possible extended submodular formulations is claimed.

## 9. Exact owner-cut Hall--Kantorovich obstruction

The following theorem applies to an arbitrary balanced completion, so it is stronger than an obstruction tied to a prescribed comparator.

For \(\mathcal A\subseteq V_q\), define

\[
\mu_q^L(\mathcal A)
=\#\{X:L_q(X)\in\mathcal A\},
\]

\[
\delta_q(\mathcal A)
=\bigl(c_q|\mathcal A|-\mu_q^L(\mathcal A)\bigr)_+,
\tag{9.1}
\]

and the gain-capable owner set

\[
G_q(\mathcal A)
=\left\{
X: L_q(X)\notin\mathcal A,
\ \exists S\in\mathcal A\text{ with }S\subseteq X
\right\}.
\tag{9.2}
\]

Let

\[
\mathcal R_q=\{X:a(X)<q\}.
\]

### Theorem 9.1 — exact cut service

Every balanced nested completion \(Q\) respecting the frozen prefixes satisfies

\[
\boxed{
|\mathcal R_q\cap G_q(\mathcal A)|
\ge\delta_q(\mathcal A).
}
\tag{9.3}
\]

Proof. Balance gives

\[
Q_q(\mathcal A)\ge c_q|\mathcal A|,
\]

so

\[
Q_q(\mathcal A)-L_q(\mathcal A)
\ge\delta_q(\mathcal A).
\]

Only an owner with \(L_q(X)\notin\mathcal A\) and \(Q_q(X)\in\mathcal A\) contributes positively. Such an owner lies in \(G_q(\mathcal A)\), and because it disagrees at depth \(q\), it lies in \(\mathcal R_q\). The number of positive contributors is at least the net increase. \(\square\)

Choose cuts \(\mathcal A_s\) at depths \(s\), and abbreviate

\[
\delta_s=\delta_s(\mathcal A_s),
\qquad G_s=G_s(\mathcal A_s).
\]

### Theorem 9.2 — weighted Hall dual

If \(\beta_s\ge0\) satisfies

\[
\boxed{
\sum_{\substack{s>a\\X\in G_s}}\beta_s
\le H_{a+1}
\qquad\text{for every }X\in\Omega,
\ a\in\{0,\ldots,K\},
}
\tag{9.4}
\]

then every permanent-prefix balanced completion satisfies

\[
\boxed{
\mathcal C\ge\sum_s\beta_s\delta_s.
}
\tag{9.5}
\]

Proof. Let \(z_{X,a}=1\) when owner \(X\) stops at \(a\). Theorem 9.1 gives

\[
\sum_{X\in G_s}\sum_{a<s}z_{X,a}\ge\delta_s.
\]

Multiply by \(\beta_s\), sum over \(s\), and apply (9.4) owner by owner. The right side is at most

\[
\sum_{X,a}H_{a+1}z_{X,a}=\mathcal C.
\]

\(\square\)

If every owner belongs to at most \(D\ge1\) of the gain sets \(G_s\), then

\[
\beta_s=\frac{H_s}{D}
\]

is feasible, since \(s>a\) implies \(H_s\le H_{a+1}\). Hence

\[
\boxed{
\mathcal C
\ge\frac1D\sum_s\delta_sH_s.
}
\tag{9.6}
\]

Equations (9.4)--(9.6) are valid Hall/transport dual certificates; equivalently, they belong to the exact dual of the displayed cut-service covering relaxation. Equality with the full packet-transport dual restricted to these prices is not asserted.

## 10. A concrete logarithmic-star obstruction

Let

\[
J=\lfloor K/2\rfloor,
\qquad
t=\lfloor\log_2 n\rfloor.
\]

Choose pairwise disjoint \(t\)-sets

\[
T_1,\ldots,T_J\subseteq[n].
\]

This is possible for all sufficiently large \(m\), because

\[
Jt=O_A(\sqrt m\log m)=o(m).
\]

For a \(t\)-set \(T\), put

\[
\mathcal G(T)=\{X\in\Omega:T\subseteq X\}.
\]

Its size is

\[
G_t:=|\mathcal G(T)|=\binom{n-t}{m-t},
\]

and

\[
\frac{G_t}{B}
=n\prod_{i=0}^{t-1}\frac{m-i}{n-i}
=(1+o(1))n2^{-t}.
\tag{10.1}
\]

Because \(2^t\le n<2^{t+1}\), this ratio oscillates between \(1+o(1)\) and \(2+o(1)\). In particular,

\[
G_t=\Theta(B).
\tag{10.2}
\]

For two disjoint \(t\)-sets,

\[
G_{2t}:=|\mathcal G(T_s)\cap\mathcal G(T_r)|
=\binom{n-2t}{m-2t},
\]

and

\[
\frac{G_{2t}}{G_t}
=\prod_{i=0}^{t-1}\frac{m-t-i}{n-t-i}
\le2^{-t}<\frac2n.
\tag{10.3}
\]

Thus

\[
G_{2t}=O(B/n).
\tag{10.4}
\]

### Theorem 10.1 — logarithmic-star Hall obstruction

Suppose that for every \(q\le J\) there is a family

\[
\mathcal A_q
\subseteq\{S\in V_q:T_q\subseteq S\}
\]

such that, for some fixed \(\eta>0\),

\[
\delta_q(\mathcal A_q)\ge\eta B.
\tag{10.5}
\]

Then every balanced nested completion respecting permanent frozen prefixes satisfies

\[
\boxed{
\mathcal C
\ge
\left(\frac{\eta A^2}{32C_A}+o(1)\right)W.
}
\tag{10.6}
\]

Proof. Every gain-capable owner for \(\mathcal A_q\) contains \(T_q\), so

\[
G_q(\mathcal A_q)\subseteq\mathcal G(T_q).
\]

Since \(\mathcal R_q\subseteq\mathcal R_J\), Theorem 9.1 gives sets

\[
E_q:=\mathcal R_J\cap G_q(\mathcal A_q)
\]

with \(|E_q|\ge\eta B\). Their pairwise intersections have size at most \(G_{2t}\). Bonferroni and (10.4) give

\[
\begin{aligned}
R_J
&\ge\left|\bigcup_{q\le J}E_q\right|\\
&\ge\eta BJ-\binom J2G_{2t}\\
&=\eta BJ-O_A(B)\\
&\ge\frac\eta2BJ
\end{aligned}
\]

eventually. Since \(R_r\ge R_J\) for \(r\ge J\),

\[
\mathcal C
\ge\frac{K-J+1}{C_A}R_J.
\]

Using \(B=W/n\), \(n=2m+1\), and \(J=(1/2+o(1))K\), the asymptotic coefficient is at least \(\eta A^2/(16C_A)\); the displayed \(1/32\) is a safe eventual constant. \(\square\)

The robust hypothesis can be written as a floor deficit. Define

\[
\Delta_q(T)
=\sum_{\substack{S\in V_q:\ T\subseteq S\\\mu_q(S)<c_q}}
(c_q-\mu_q(S)).
\tag{10.7}
\]

Taking the underfloor members of the \(T\)-star as \(\mathcal A_q\) gives

\[
\delta_q(\mathcal A_q)=\Delta_q(T).
\tag{10.8}
\]

For every balanced quota vector \(b_q\), equality of total masses gives

\[
\sum_S(\mu_q(S)-b_q(S))_+
=\sum_S(b_q(S)-\mu_q(S))_+
\ge\sum_S(c_q-\mu_q(S))_+.
\]

Minimizing the left side over balanced \(b_q\) shows

\[
\Delta_q(T)\le O_q(F).
\tag{10.8a}
\]

Thus

\[
\Delta_q(T_q)\ge\eta B
\qquad(q\le J)
\tag{10.9}
\]

for disjoint logarithmic stars implies (10.6).

For example, this obstruction is compatible with the MWB scale under the sufficient additional upper hypothesis

\[
O_q(F)=O_A(B)
\qquad(q\le K).
\]

Under that hypothesis,

\[
\sum_{q\le K}\frac{O_q(F)}{c_q}
=O_A(B\sqrt m)
=O_A(W/\sqrt m)
=o(W),
\tag{10.10}
\]

while prefix cost is linear. No factor satisfying (10.9) is known.

A transparent sufficient condition for (10.9) is an empty star: \(\mu_q(S)=0\) for every \(S\supseteq T_q\). Indeed, for

\[
\mathcal A_q=\{S\in V_q:T_q\subseteq S\},
\]

\[
|\mathcal A_q|
=\frac{G_t}{\lambda_{q,t}},
\qquad
\lambda_{q,t}
=\prod_{i=0}^{q-1}\frac{m+2+i}{m-t-i}
=O_A(1),
\tag{10.11}
\]

so \(c_q|\mathcal A_q|=\Theta_A(B)\).

The empty-star condition is not excluded by one-point margins alone. Let \(r=m-q\). Choose an integer random variable \(K_T\) supported on

\[
\left\{\left\lfloor\frac{tr}{n}\right\rfloor,
\left\lceil\frac{tr}{n}\right\rceil\right\}
\]

with mean \(tr/n\), and choose an \(r\)-set uniformly conditional on

\[
|S\cap T|=K_T.
\]

For the central window, \(K_T<t\), so no chosen set contains \(T\). Yet every coordinate has inclusion probability \(r/n\): for \(x\in T\) it is \(\mathbb E K_T/t\), and outside \(T\) it is \(\mathbb E(r-K_T)/(n-t)\). This verifies only fractional total mass and one-point margins, not integral quotas, nesting, cyclic bundling, or existence of an exact factor.

## 11. Whole-wreath packet Hall prices

Now impose the strong cyclic rule that every row \(C\) has one common stopping depth \(a_C\). Let

\[
\epsilon_q(S)=(\mu_q(S)-c_q-1)_+.
\tag{11.1}
\]

If \(C\) is released before \(q\), all \(n\) of its canonical depth-\(q\) occurrences leave the frozen core. Necessarily,

\[
\sum_{C:a_C<q}\mathbf1_{\{S\in H_{C,q}\}}
\ge\epsilon_q(S).
\tag{11.2}
\]

The fractional covering relaxation is

\[
\min\sum_{C,a}n\Psi(a)z_{C,a}
\tag{11.3}
\]

subject to

\[
\sum_C\sum_{a<q}
\mathbf1_{\{S\in H_{C,q}\}}z_{C,a}
\ge\epsilon_q(S),
\tag{11.4}
\]

\[
\sum_az_{C,a}=1,
\qquad z_{C,a}\ge0.
\tag{11.5}
\]

Its exact dual is

\[
\boxed{
\max_{\lambda\ge0}
\left[
\sum_{q,S}\lambda_{q,S}\epsilon_q(S)
+\sum_C\min_a
\left(
n\Psi(a)-\sum_{q>a}\lambda_q(H_{C,q})
\right)
\right].
}
\tag{11.6}
\]

In particular, any \(\lambda\ge0\) satisfying

\[
\sum_{q>a}\lambda_q(H_{C,q})
\le n\Psi(a)
\qquad(C,a)
\tag{11.7}
\]

certifies

\[
\boxed{
\mathcal C\ge\sum_{q,S}\lambda_{q,S}\epsilon_q(S).
}
\tag{11.8}
\]

For \(\mathcal U\subseteq V_q\), put

\[
d_q(\mathcal U)=\max_C|H_{C,q}\cap\mathcal U|,
\]

\[
\epsilon_q(\mathcal U)=\sum_{S\in\mathcal U}\epsilon_q(S).
\]

Taking a constant price on \(\mathcal U\) at depth \(q\) gives the one-cut bound

\[
\boxed{
\mathcal C
\ge
nH_q\frac{\epsilon_q(\mathcal U)}{d_q(\mathcal U)}.
}
\tag{11.9}
\]

The ratio is declared zero when \(d_q(\mathcal U)=0\), in which case \(\epsilon_q(\mathcal U)=0\). To verify (11.9), set

\[
\lambda_{q,S}=
\frac{nH_q}{d_q(\mathcal U)}\mathbf1_{\{S\in\mathcal U\}}.
\]

If \(a<q\), the row charge is at most \(nH_q\le n\Psi(a)\); if \(a\ge q\), it is zero.

For \(q\le K/2\),

\[
H_q\ge\frac K{2C_A},
\]

so

\[
\boxed{
\mathcal C
\ge
\frac{nK}{2C_A}
\frac{\epsilon_q(\mathcal U)}{d_q(\mathcal U)}.
}
\tag{11.10}
\]

Consequently,

\[
\mathcal C=o(W)
\Longrightarrow
\frac{\epsilon_q(\mathcal U)}{d_q(\mathcal U)}
=o\!\left(\frac B{\sqrt m}\right)
\tag{11.11}
\]

uniformly for every early \(q\) and every target family \(\mathcal U\). If the ratio is at least \(\varepsilon B/\sqrt m\), then

\[
\boxed{
\mathcal C\ge\frac{\varepsilon A}{2C_A}W
}
\tag{11.12}
\]

for all sufficiently large \(m\).

More generally, suppose early released owners must be partitioned into allowed packets \(P\), and define their maximum density in a target family by

\[
\eta_q(\mathcal U)
=\max_P\frac{|P\cap\{X:L_q(X)\in\mathcal U\}|}{|P|}.
\]

Releasing \(\epsilon_q(\mathcal U)\) relevant canonical occurrences costs at least

\[
\boxed{
H_q\frac{\epsilon_q(\mathcal U)}{\eta_q(\mathcal U)}.
}
\tag{11.13}
\]

If \(\eta_q(\mathcal U)=0<\epsilon_q(\mathcal U)\), the packet architecture is infeasible and the right side is \(+\infty\). If both quantities vanish, the ratio is defined as zero.

For whole rows, \(\eta_q(\mathcal U)=d_q(\mathcal U)/n\), recovering (11.9). This identifies packet dispersion, not raw excess alone, as the cyclic Hall parameter.

## 12. Why naive TU and circular integrality fail

### 12.1 A determinant-\(2\) owner-path minor

Let \(m\ge3\). In one actual wreath row take consecutive middle windows

\[
X=A\cup\{a\},
\qquad
Y=A\cup\{d\},
\qquad |A|=m-1.
\]

Choose distinct \(b,c\in A\), and put

\[
B=X\setminus\{b\},
\qquad
C=A\setminus\{b\},
\qquad
D=A\setminus\{c\}.
\]

The three rooted Boolean paths

\[
p_1:X\to A\to D,
\qquad
p_2:X\to B\to C,
\qquad
p_3:Y\to A\to C
\]

are valid. On the rows

\[
(\text{owner }X),
\qquad(q=1,A),
\qquad(q=2,C),
\]

their incidence matrix is

\[
\begin{pmatrix}
1&1&0\\
1&0&1\\
0&1&1
\end{pmatrix},
\qquad\det=-2.
\tag{12.1}
\]

Therefore the naive root-labelled path-configuration matrix is not totally unimodular, already using two owners of one cyclic packet.

This is not an integral Hall gap for the fixed-release problem. The ordinary Boolean suffix network may splice histories at \(A\), adding the paths

\[
X\to A\to C,
\qquad
Y\to A\to D.
\]

That larger arc-flow extension is exactly the audited totally unimodular Hoffman network. Thus (12.1) rules out only the naive path matrix. It neither contradicts fixed-stop integrality nor rules out every extended submodular formulation. The parity becomes genuine only for a packet catalog that retains owner identity through \(A\) and forbids cross-splicing.

### 12.2 Abstract odd-cycle packet parity

Let \(N=2h+1\) positions form an odd cycle. A late adjacent-pair packet \(y_i\) serves \(i,i+1\) at first-disagreement depth \(t\), and an earlier singleton \(z_i\) serves position \(i\) at depth \(s<t\). Exact service is

\[
y_{i-1}+y_i+z_i=1.
\tag{12.2}
\]

Give \(y_i\) cost \(2H_t\) and \(z_i\) cost \(H_s\). Fractionally,

\[
y_i=\frac12,
\qquad z_i=0
\]

has cost \(NH_t\). Integrally the selected pairs form a matching, so an odd cycle leaves at least one singleton, and one is sufficient. Summing (12.2),

\[
2\sum_i y_i+\sum_i z_i=N,
\]

and hence

\[
\boxed{
\operatorname{OPT}_{\rm frac}=NH_t,
\qquad
\operatorname{OPT}_{\mathbb Z}=NH_t+(H_s-H_t).
}
\tag{12.3}
\]

The adjacent-pair matrix is \(I+P\) for an odd cyclic shift and has determinant \(2\). Also,

\[
\frac{t-s}{C_A}
\le H_s-H_t
\le t-s.
\tag{12.4}
\]

This is a genuine abstract cyclic-packet parity gap, but it is not yet an actual wreath-state obstruction with balanced target quotas. Even if one copy occurred in every wreath, its total gap would be at most

\[
BK=O_A(W/\sqrt m)=o(W).
\tag{12.5}
\]

Thus a bounded parity defect per row cannot obstruct the desired theorem. For a Gaussian separation \(t-s=\Theta(\sqrt m)\), linear cost requires \(\Omega(\sqrt m)\) independent forced breakers per row; for constant separation it requires \(\Omega(m)\).

## 13. Exact cyclic trade exploration

The preceding obstructions become relevant only if they can be packetized inside one exact factor. Two exact structural facts delimit that problem.

### Lemma 13.1 — adjacent row swap ledger

Let

\[
\pi=(z_0,z_1,\ldots,z_{n-1})
\]

be one cyclic row, and let \(\pi'\) swap the adjacent symbols \(z_0,z_1\), oriented by this displayed swapped order rather than by its reversal. Then:

- the two middle-window packets share exactly \(n-2\) owners;
- exactly \(m\) shared owners contain neither swapped symbol, and all their flags agree;
- exactly \(m-1\) shared owners contain both symbols, and their deletion words differ by one adjacent transposition;
- as the window slides, the unique mismatch depth of these \(m-1\) owners runs bijectively through \(1,\ldots,m-1\);
- exactly two old middle owners leave and two new owners enter.

Proof. An \(m\)-window contains each fixed coordinate in exactly \(m\) phases and contains the adjacent pair in exactly \(m-1\) phases. Hence exactly two phases contain one but not the other, \(m-1\) contain both, and

\[
n-(m+1)=m
\]

contain neither. In a shared window containing both, the two coordinates occupy adjacent positions; their distance from the deleted end runs once through \(1,\ldots,m-1\). \(\square\)

For fixed \(A\) and all sufficiently large \(m\), one has \(K\le m-1\). Suppose \(s\) old rows can then be support-feasibly replaced by their adjacent-swapped rows, producing another exact factor. Align the old flags to the prescribed new flags. At each controlled depth there are exactly \(s\) shared rank-isolated mismatches, plus at most \(2s\) reowned exceptional owners. Therefore

\[
\text{labelled distance}
\le3s\sum_{q=1}^K\frac1{c_q},
\tag{13.1}
\]

while permanent alignment costs at least

\[
\boxed{
s\sum_{q=1}^KH_q
=s\sum_{q=1}^K\frac q{c_q}.
}
\tag{13.2}
\]

For \(s=\eta B\), (13.1) is \(O_A(W/\sqrt m)=o(W)\), whereas

\[
(13.2)
\ge\left(\frac{\eta A^2}{4C_A}+o(1)\right)W.
\tag{13.3}
\]

This is only a prescribed factor-to-factor separation. It obstructs existential balanced completion only if the new flags themselves give the needed balanced resolution or if the changed owners are protected by Hall cuts such as Theorem 10.1. Neither condition is proved.

### Lemma 13.2 — signed packetization by Johnson cycles

Partition

\[
[n]=P\sqcup Q\sqcup\{u,v,w\},
\qquad |P|=|Q|=m-1,
\]

and take the cyclic row

\[
C=(u,v,Q,w,P),
\]

with arbitrary fixed internal orders on \(P,Q\). Let \(C'\) swap \(u,v\). Exactly two middle windows change, and

\[
\boxed{
\mathbf1_{\mathcal W(C')}-\mathbf1_{\mathcal W(C)}
=e_{P\cup\{v\}}+e_{Q\cup\{u\}}
-e_{P\cup\{u\}}-e_{Q\cup\{v\}}.
}
\tag{13.4}
\]

Fix \(w\). If

\[
A_0,A_1,\ldots,A_s=A_0
\]

is a cycle in \(J([n]\setminus\{w\},m)\), and

\[
B_i=([n]\setminus\{w\})\setminus A_i,
\]

then the corresponding adjacent-swap row differences telescope:

\[
\sum_i
\left(
\mathbf1_{\mathcal W(C_i')}-\mathbf1_{\mathcal W(C_i)}
\right)
=\sum_i
(e_{A_{i+1}}+e_{B_{i+1}}-e_{A_i}-e_{B_i})
=0.
\tag{13.5}
\]

Thus every Johnson cycle is a signed exact middle-owner packet trade. If the old rows are pairwise middle-disjoint and belong to one exact factor, then equality of the total middle incidence vectors forces the new rows to be pairwise disjoint as well; replacing them is a literal exact-factor trade.

The missing condition is positivity/support. A fixed exact factor supplies only \(B\) old omitted-label-\(w\) states among \(\asymp mB\) possible complementary states, so counting alone does not force a Johnson cycle closed inside the available support. No positive-density support-feasible family is proved.

### Lemma 13.3 — fixed packet rigidity

The middle-window packet of one row determines its cyclic coordinate order up to dihedral symmetry. Indeed, within the packet two middle owners meet in \(m-1\) points exactly when they are consecutive windows, so the packet's Johnson adjacency graph recovers its defining \(C_n\).

Consequently, preserving the same middle packet permits only the same orientation or reversal. The same orientation leaves every flag unchanged. Reversal sends the two depth-\(q\) intervals rooted at a fixed owner to distinct opposite-end subintervals for every \(1\le q<m\). Thus reversal creates full-depth mismatch and no unlabelled row-histogram change.

Therefore the earlier arbitrary-owner rank-one swap obstruction cannot be realized merely by reorienting a fixed wreath packet. Genuine packetization requires a multirow exact trade such as (13.5), together with a still-unproved positivity theorem.

## 14. Quantified implications and remaining theorem

The exact positive implications proved here are:

\[
\begin{array}{c}
\text{fractional nested survival-packet cost }o(W)\\
\Downarrow\quad\text{factor }R_A=O_A(1)\\
\text{integral upper-safe owner or whole-row stops of cost }o(W),
\end{array}
\tag{14.1}
\]

\[
\begin{array}{c}
\text{one balanced }P\text{ with owner-tail cost }o(W)\\
\Downarrow\quad\text{bounded cyclic arcs or }r=o(\sqrt m)\text{ batching}\\
\text{integral row-local packets of cost }o(W)
\text{ (literal cyclic arcs in the first case), witnessed by the same }P,
\end{array}
\tag{14.2}
\]

and

\[
\begin{array}{c}
\text{coarsening fibers, or split/excess bound (7.7) }=o(W)\\
\Downarrow\\
\text{integral upper-safe laminar stops of cost }o(W).
\end{array}
\tag{14.3}
\]

To obtain a balanced nested resolution from (14.1) or (14.3), every cut (U) and (L) must still be proved. The exact packet ILP (2.3)--(2.6) includes those requirements automatically, but its natural relaxation is not generically integral.

The exact negative implication is:

\[
\begin{array}{c}
\Theta(\sqrt m)\text{ disjoint logarithmic stars with deficit }\Theta(B)\\
\Downarrow\\
\mathcal C=\Omega_A(W)
\end{array}
\tag{14.4}
\]

for every balanced completion in that fixed factor. This is conditional on the star deficits; no exact factor exhibiting them is known.

Neither (14.4), the determinant-\(2\) minor, nor the abstract odd-cycle parity refutes unlabelled fixed-window overload, MWB, labelled synchronization by a rejoining method, or a direct literal OR-word construction. The permanent-prefix cost functional can strictly overcharge rank-isolated rejoining repairs, as proved in the Boolean owner model; no existential exact-factor separation is proved here.

The sharp surviving route-specific theorem is:

> For every fixed \(A\), find in one exact factor a fractional or integral cyclic packet transport of base cost \(o(W)\), and round it while adding \(o(\sqrt m)\) early released owners per wreath, with all target quotas and all Hoffman staircase cuts preserved.

The additive estimate (4.6) then gives \(o(W)\) integral cost. A literal polymatroid representation satisfying (3.1) would prove this with zero rounding loss, but the all-or-none whole-row and fixed cyclic-interval catalogs exhibited in Section 3 fail the required exchange axioms. Conversely, a protected Hall construction at the scale of Theorem 10.1 would disprove this permanent-prefix route for that factor. Neither final alternative is resolved.

## 15. Independent audit record

The following decisive points were independently rederived after the proofs were assembled.

- The signs in the mobile-quota and fixed-quota Kantorovich duals (2.7)--(2.8) are correct.
- The cyclic-arc factor \(r\), Ferrers inequalities (4.2)--(4.5), and the \(o(\sqrt m)\)-overshoot scale (4.6) are exact.
- The conditional polymatroid theorem is valid only with the literal same-coordinate hypothesis (3.1); that restriction is stated.
- The laminar recursion, antichain interpretation, split-pruning indices, and one-depth Hall cut (6.1) are correct. Supermodularity of (8.2) is not claimed as a generalized-polymatroid obstruction.
- In Theorem 10.1, \(G_t=\Theta(B)\), not asymptotic to \(B\); the floor in \(t=\lfloor\log_2n\rfloor\) causes a bounded oscillation. The pair-overlap estimate and the safe constant \(\eta A^2/(32C_A)\) are correct.
- The determinant-\(2\) minor is only a failure of the naive path matrix. Cross-splicing in the fixed-release Boolean network restores the known totally unimodular extension.
- The odd-cycle model is explicitly labelled abstract, and the Johnson-cycle packet trade is explicitly conditional on support-feasible old rows.

No unproved cyclic positivity, exact-factor star construction, residual-Hoffman rounding, or reverse implication from overload to labelled synchronization is used.
