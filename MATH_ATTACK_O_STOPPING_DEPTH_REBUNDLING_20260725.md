# O: owner stopping times and literal global rebundling of cyclic flags

Date: 2026-07-25

Method: pure mathematics only. No web search, finite search, random experiment, solver, or computational enumeration was used.

## 0. Outcome

This report studies the literal cyclic version of stopping-time rebundling.
Start with one oriented exact middle wreath factor \(F\), freeze the canonical
flag of each middle owner \(X\) through an owner-specific depth \(a(X)\), and
require every released suffix to be the canonical suffix of a second
oriented exact wreath factor \(G\). The depth-\(q\) loads of \(G\) must be
balanced:

\[
\mu_q^G(S)\in\{c_q,c_q+1\}.
\]

This is stronger than the previously audited Boolean suffix-flow problem.
In the Boolean problem, released owner paths may splice independently in the
inclusion network. Here the \(n\) flags of every selected row must come from
one cyclic coordinate order, and the selected rows must partition the whole
middle layer.

Four exact results are proved.

1. **Exact row-state matching.** Joint choice of \(G\), the stopping depths,
   and balanced quotas is an integral minimum-cost exact-cover problem over
   prefix-compatible oriented row states. Its cost is exactly
   \[
   \mathcal C=\sum_{q=1}^K\frac{R_q}{c_q}.
   \]
   The fractional relaxation has a complete Kantorovich/Farkas dual.

2. **A genuine \(o(W)\) rounding regime.** For a fixed integral balanced
   quota system, if a fractional row-state cover has cost \(o(W)\), every
   forest component of its support incidence graph rounds integrally with
   no loss. If all nonforest components have
   extendible owner-volume
   \[
   L=o(W/\sqrt m),
   \]
   the whole solution rounds to a literal exact factor with cost \(o(W)\).

3. **Exact legal-exchange stability.** Any support-feasible family of
   multirow exchanges whose endpoint factor is balanced has exact stopping
   cost equal to the sum of the cells' Hardy first-disagreement costs. In
   particular, even if every old row participates, at most
   \(r_m=o(\sqrt m)\) released owners per old row imply
   \(\mathcal C=o(W)\). A contaminated family of
   \(o(B/\sqrt m)\) whole rows is also harmless.

4. **Sharp cuts.** At one depth, arbitrary owner-tail rebundling is governed
   exactly by a gain-capable Hall inequality. Literal synchronous row
   rebundling obeys a stronger cyclic packet-cap cut. A cyclic
   rank-\((m-q)\) packet contains at most
   \[
   (m-q-t+1)_+
   \]
   members of a \(t\)-star. Finally, the earlier logarithmic-star obstruction
   survives every literal global rebundling: Catalan-size deficits on
   \(\Theta(\sqrt m)\) nearly disjoint stars force
   \[
   \mathcal C=\Omega_A(W).
   \]

No balanced endpoint factor satisfying the positive sparse-support
hypotheses is constructed here, and no exact factor with the protected
logarithmic-star deficits is constructed either. The report therefore
isolates both a nontrivial integral \(o(W)\) regime and the sharp available
cut obstruction, without claiming the missing existence theorem.

## 1. Fixed-window normalization and the two meanings of rebundling

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

The exact ratio is

\[
\frac W{N_q}
=\prod_{j=0}^{q-1}\frac{m+2+j}{m-j}.
\tag{1.1}
\]

For all sufficiently large \(m\), the explicit safe constant

\[
C_A:=\left\lceil e^{\,2(A+1)(A+2)}\right\rceil
\tag{1.2}
\]

satisfies

\[
1\le c_q\le C_A
\qquad(1\le q\le K).
\tag{1.3}
\]

Write

\[
H_d:=\sum_{q=d}^K\frac1{c_q},
\qquad H_{K+1}:=0.
\tag{1.4}
\]

Thus

\[
\frac{K-d+1}{C_A}\le H_d\le K-d+1.
\tag{1.5}
\]

Fix an oriented exact factor \(F\). For every middle owner
\(X\in\binom{[n]}m\), let

\[
X=L_0^F(X)\supset L_1^F(X)\supset\cdots\supset L_K^F(X)
\tag{1.6}
\]

be its canonical cyclic-interval flag.

Choose stopping depths

\[
a(X)\in\{0,\ldots,K\}.
\]

The owners released before depth \(q\) are

\[
\mathcal R_q=\{X:a(X)<q\},
\qquad R_q=|\mathcal R_q|.
\tag{1.7}
\]

The permanent stopping cost is exactly

\[
\boxed{
\mathcal C(a)
=\sum_{q=1}^K\frac{R_q}{c_q}
=\sum_XH_{a(X)+1}.
}
\tag{1.8}
\]

The first equality follows by counting the contribution of each owner at
every depth after its stop.

There are two distinct completion problems.

### Boolean suffix rebundling

After \(a(X)\), owner \(X\) may follow an arbitrary descending Boolean path.
For fixed stops, the split inclusion network and its two Hoffman staircase
families are necessary and sufficient; integral capacities give an integral
balanced nested resolution. Histories may splice independently at a common
Boolean endpoint.

### Literal cyclic rebundling

There must be a second oriented exact factor \(G\) such that

\[
L_q^G(X)=L_q^F(X)
\qquad(q\le a(X))
\tag{1.9}
\]

and

\[
\mu_q^G(S)\in\{c_q,c_q+1\}
\qquad(q\le K).
\tag{1.10}
\]

Now the released tails are globally rebundled into the literal rows of
\(G\). Necessarily,

\[
\text{literal cyclic rebundling}
\Longrightarrow
\text{Boolean Hoffman completion}.
\tag{1.11}
\]

No converse is proved. Everything below concerns the stronger literal
problem.

## 2. Exact joint row-state matching

For an oriented cyclic order \(\rho\), let

\[
M(\rho)=\{I_\rho(j,m):j\in\mathbb Z_n\}
\]

be its \(n\)-owner middle packet, and write

\[
L_q^\rho(I_\rho(j,m))=I_\rho(j,m-q)
\]

for its oriented flag.

A **row state**

\[
s=(\rho,a_s)
\]

consists of an oriented row \(\rho\) and a stopping depth
\(a_s(X)\in\{0,\ldots,K\}\) for every \(X\in M(\rho)\), satisfying

\[
L_q^\rho(X)=L_q^F(X)
\qquad(q\le a_s(X)).
\tag{2.1}
\]

Define its owner incidence, target incidence, and cost by

\[
m_s(X)=\mathbf1_{\{X\in M(\rho)\}},
\tag{2.2}
\]

\[
h_s(q,S)
=\#\{X\in M(\rho):L_q^\rho(X)=S\},
\tag{2.3}
\]

\[
\kappa_s
=\sum_{X\in M(\rho)}H_{a_s(X)+1}.
\tag{2.4}
\]

For every fixed \(q\), the \(n\) cyclic \((m-q)\)-intervals of one row are
distinct, so

\[
h_s(q,S)\in\{0,1\}.
\tag{2.5}
\]

### Theorem 2.1 — exact stopping/rebundling ILP

Literal cyclic rebundling is exactly the integer program

\[
\min\sum_s\kappa_sx_s
\tag{2.6}
\]

subject to

\[
\sum_sm_s(X)x_s=1
\qquad(X\in\Omega),
\tag{2.7}
\]

\[
c_q\le\sum_sh_s(q,S)x_s\le c_q+1
\qquad(q\le K,\ S\in V_q),
\tag{2.8}
\]

\[
x_s\in\{0,1\}.
\tag{2.9}
\]

Every integral solution chooses \(B\) pairwise middle-disjoint oriented
rows, hence one exact factor \(G\). Equation (2.1) supplies the frozen
prefixes, (2.8) says that every depth load is balanced, and (2.4) sums to
\(\sum_qR_q/c_q\). Conversely, every literal completion \((G,a)\) chooses
one state for each row of \(G\) and gives an integral solution.

This remains integral inside one exact factor; no fractional exact factor
is used in the equivalence.

### Fixed stops and decorated residual clones

Fix \(a\) and balanced quota vectors

\[
b_q(S)\in\{c_q,c_q+1\}.
\]

The frozen load is

\[
g_q(S)
=\#\{X:a(X)\ge q,\ L_q^F(X)=S\}.
\tag{2.10}
\]

Assume

\[
g_q(S)\le b_q(S),
\tag{2.11}
\]

and put

\[
s_q(S)=b_q(S)-g_q(S).
\tag{2.12}
\]

Since \(\sum_Sg_q(S)=W-R_q\),

\[
\boxed{
\sum_{S\in V_q}s_q(S)=R_q.
}
\tag{2.13}
\]

Call an oriented row \(\rho\) \(a\)-compatible when

\[
L_q^\rho(X)=L_q^F(X)
\qquad(X\in M(\rho),\ q\le a(X)).
\tag{2.14}
\]

Form a decorated hypergraph with:

- one vertex for each middle owner \(X\);
- \(s_q(S)\) labelled clones of every residual cell \((q,S)\);
- for every \(a\)-compatible row, one decorated edge variant for every
  injection of each released occurrence
  \((X,q)\), \(q>a(X)\), into a labelled clone of its cell
  \((q,L_q^\rho(X))\); the edge also contains the row's \(n\) owner
  vertices.

### Theorem 2.2 — exact decorated-row equivalence

The following are equivalent.

1. There is an oriented exact factor \(G\) satisfying (1.9) and
   \[
   \mu_q^G=b_q
   \qquad(q\le K).
   \]
2. The decorated row hypergraph has a perfect matching covering every owner
   vertex and every residual clone exactly once.

Proof. The rows of \(G\) cover every owner exactly once. Their frozen
occurrences give \(g_q\), while their released occurrences give
\(b_q-g_q=s_q\), so label the latter by the residual clones. Conversely, a
perfect matching partitions the middle owners into cyclic rows and hence
gives an exact factor. Compatibility supplies \(g_q\), and clone coverage
supplies exactly \(s_q\), so the total load is \(b_q\). \(\square\)

Theorem 2.2 identifies the additional content beyond Hoffman flow: it is a
decorated cyclic-row exact-cover theorem.

## 3. Fractional duality and sharp one-rank cuts

Let

\[
\mathcal B=
\left\{
b:\ c_q\le b_q(S)\le c_q+1,\ 
\sum_{S\in V_q}b_q(S)=W\text{ for every }q
\right\}.
\tag{3.1}
\]

Relax \(x_s\ge0\).

### Theorem 3.1 — exact fractional Kantorovich dual

For fixed balanced \(b\), replace (2.8) by the equalities

\[
\sum_sh_s(q,S)x_s=b_q(S).
\]

The fractional optimum of this fixed-quota system is

\[
\boxed{
D_{\rm frac}(b)
=\max_{u,p}
\left[
\sum_{X\in\Omega}u_X+\sum_{q,S}p_{q,S}b_q(S)
\right]
}
\tag{3.2}
\]

subject to

\[
\boxed{
\sum_{X\in M(\rho)}u_X
+\sum_{q,S}p_{q,S}h_s(q,S)
\le\kappa_s
\qquad(s).
}
\tag{3.3}
\]

The owner prices \(u_X\) and target prices \(p_{q,S}\) are unrestricted in
sign.

If the balanced quota vector is chosen jointly, then

\[
\boxed{
D_{\rm frac}
=\max_{u,p}
\left[
\sum_Xu_X+\min_{b\in\mathcal B}\langle p,b\rangle
\right]
}
\tag{3.4}
\]

under the same state inequalities (3.3).

Proof. These are the ordinary duals of the equality-constrained row-state
cover, with \(b\) introduced as the aggregate target marginal in the mobile
case. Minimization over \(b\in\mathcal B\) gives (3.4). \(\square\)

Every feasible \((u,p)\) is an exact fractional cut obstruction in the
requested weighted units. Absence of such a cut proves only fractional
feasibility; integral rebundling additionally needs normality or an
integer-decomposition theorem for the row-state hypergraph.

For fixed \(a,b\), Theorem 2.2 has the following exact Farkas alternative.
Let \(h_\rho^{\rm rel}\) be the released-occurrence vector of an
\(a\)-compatible row. Fractional decorated rebundling exists if and only if,
whenever

\[
\sum_{X\in M(\rho)}\alpha_X
+\langle\phi,h_\rho^{\rm rel}\rangle
\le0
\qquad(\rho),
\tag{3.5}
\]

one has

\[
\boxed{
\sum_{X\in\Omega}\alpha_X+\langle\phi,s\rangle\le0.
}
\tag{3.6}
\]

This is sharp fractionally and necessary integrally.

### Theorem 3.2 — exact one-rank released-owner Hall cut

Fix a depth \(q\), stops \(a\), and a balanced quota \(b_q\), and assume

\[
g_q(S)\le b_q(S)
\qquad(S\in V_q).
\]

Put

\[
\mathcal O_q(\mathcal A)
=\{X:L_q^F(X)\in\mathcal A\},
\tag{3.7}
\]

\[
\mathcal N_q(\mathcal A)
=\{X:\exists S\in\mathcal A\text{ with }S\subseteq X\},
\tag{3.8}
\]

\[
\mathcal G_q(\mathcal A)
=\mathcal N_q(\mathcal A)\setminus\mathcal O_q(\mathcal A).
\tag{3.9}
\]

There is an independent integral assignment of the released owners
\(\mathcal R_q\) to the residual slots \(s_q=b_q-g_q\), with owner \(X\)
assigned only to an \((m-q)\)-subset of \(X\), if and only if, for every
\(\mathcal A\subseteq V_q\),

\[
\boxed{
b_q(\mathcal A)-\mu_q^F(\mathcal A)
\le
|\mathcal R_q\cap\mathcal G_q(\mathcal A)|.
}
\tag{3.10}
\]

Proof. The bipartite clone Hall theorem says exactly

\[
s_q(\mathcal A)
\le
|\mathcal R_q\cap\mathcal N_q(\mathcal A)|.
\tag{3.11}
\]

But

\[
s_q(\mathcal A)
=b_q(\mathcal A)-\mu_q^F(\mathcal A)
+|\mathcal R_q\cap\mathcal O_q(\mathcal A)|,
\]

and \(\mathcal O_q(\mathcal A)\subseteq\mathcal N_q(\mathcal A)\).
Subtracting the common term gives (3.10). Integral capacities give an
integral assignment. \(\square\)

Thus (3.10) is the sharp one-rank cut. Literal cyclic rebundling implies
it, but the converse only assigns one layer independently and does not
enforce nesting or cyclic row packets.

Since \(b_q(S)\ge c_q\), every literal completion also satisfies

\[
\boxed{
|\mathcal R_q\cap\mathcal G_q(\mathcal A)|
\ge
\delta_q(\mathcal A),
\qquad
\delta_q(\mathcal A)
:=\bigl(c_q|\mathcal A|-\mu_q^F(\mathcal A)\bigr)_+.
}
\tag{3.12}
\]

## 4. A nontrivial integral \(o(W)\) rounding regime

The full row-state matrix is not known to be integral. It is integral on
forest supports.

Let \(x\) be a fractional feasible solution for a fixed integral balanced
\(b\), with target equalities as in Theorem 3.1.
Form its bipartite support incidence graph:

- one side consists of every owner constraint and every target-cell
  constraint;
- the other side consists of the positive-weight row-state columns;
- a constraint vertex is joined to a state column when that column has
  incidence one in the constraint.

### Theorem 4.1 — forest-support rounding

If this support incidence graph is a forest, there is an integral literal
cyclic rebundling of cost at most the fractional cost.

More generally, suppose the nonforest support components together contain
exactly \(L\) owner vertices, and suppose their residual owner and
target-demand system is internally exactly coverable by row states whose
entire owner and target incidence lies in that bad resource union, without
using any resource from a forest component. Here \(L\) is owner-volume, not
the number of rows, states, or constraint vertices. Then

\[
\boxed{
C_{\rm int}\le C_{\rm frac}+LH_1
\le C_{\rm frac}+LK.
}
\tag{4.1}
\]

Consequently,

\[
C_{\rm frac}=o(W),
\qquad
L=o(W/\sqrt m)
\tag{4.2}
\]

imply a literal integral completion with

\[
C_{\rm int}=o(W).
\tag{4.3}
\]

Proof. The \(0\)-\(1\) incidence matrix of a bipartite forest is totally
unimodular. Indeed, every square subgraph has an isolated vertex or a
degree-one vertex, so determinant expansion inducts to \(0,\pm1\).
Therefore every forest component with integral right-hand side has an
integral minimum-cost solution of no larger cost.

Round all forest components and retain them. By hypothesis, exactly cover
the bad union internally. Every one of its \(L\) owners can be stopped at
depth zero, costing at most \(H_1\). Hence the bad completion costs at most
\(LH_1\), which proves (4.1). Equations (1.5) and (4.2) give (4.3).
\(\square\)

The internal extendibility clause is essential. A small owner leave need
not itself admit a wreath decomposition, and repairing it may otherwise
force changes in already rounded rows.

## 5. Support-feasible exchange cells and explicit \(o(W)\) regimes

A legal cyclic exchange cell is a pair

\[
\tau=(\mathcal R_\tau^-,\mathcal R_\tau^+)
\]

of equally sized collections of oriented rows satisfying the exact
middle-owner identity

\[
\sum_{\rho\in\mathcal R_\tau^-}
\mathbf1_{M(\rho)}
=
\sum_{\rho\in\mathcal R_\tau^+}
\mathbf1_{M(\rho)}.
\tag{5.1}
\]

Suppose:

- \(\mathcal R_\tau^-\subseteq F\);
- the old owner supports of different selected cells are disjoint;
- replacing every selected old collection by its new collection produces
  an oriented factor \(G\) whose depth loads are balanced through \(K\).

The disjointness and (5.1) make \(G\) a literal exact factor.

For an owner in an exchange support, define

\[
d_\tau(X)
=\min\{q\ge1:L_q^G(X)\ne L_q^F(X)\},
\tag{5.2}
\]

with \(d_\tau(X)=K+1\) if there is no old/new disagreement through depth
\(K\). Put

\[
r_{\tau,q}
=\#\{X\in\operatorname{supp}\tau:d_\tau(X)\le q\},
\tag{5.3}
\]

\[
\chi_A(\tau)
=\sum_{X\in\operatorname{supp}\tau}H_{d_\tau(X)}
=\sum_{q=1}^K\frac{r_{\tau,q}}{c_q}.
\tag{5.4}
\]

### Theorem 5.1 — exact legal-exchange realization

Set

\[
a(X)=d_\tau(X)-1
\]

on exchanged owners and \(a(X)=K\) on unchanged owners. Then:

1. every frozen old prefix agrees with its new \(G\)-prefix;
2. the frozen load is coordinatewise at most the balanced \(G\)-load;
3. the released tails are globally rebundled into the literal rows of
   \(G\);
4. the exact stopping cost is
   \[
   \boxed{
   \mathcal C=\sum_\tau\chi_A(\tau).
   }
   \tag{5.5}
   \]

Proof. The definition of \(d_\tau(X)\) gives prefix agreement. Therefore
every frozen occurrence is one of the occurrences counted by
\(\mu_q^G\), so the frozen histogram is a submultiset of the balanced
\(G\)-histogram. The remaining \(G\)-occurrences are precisely the
released suffix occurrences. Finally, disjoint exchange supports and
(1.8) give (5.5). \(\square\)

Theorem 5.1 gives several quantitative nontrivial regimes.

### Hardy cost per exchange cell

Let

\[
p_\tau=|\mathcal R_\tau^-|.
\]

Since the old supports are disjoint,

\[
\sum_\tau p_\tau\le B.
\tag{5.6}
\]

If

\[
\chi_A(\tau)\le\varepsilon_m\,np_\tau
\qquad(\tau)
\tag{5.7}
\]

with \(\varepsilon_m\to0\), then

\[
\boxed{
\mathcal C\le\varepsilon_mW=o(W).
}
\tag{5.8}
\]

Thus the correct size of a cyclic exchange is its Hardy
first-disagreement cost, not its row count.

### Per-old-row disagreement envelope

For every old row \(C\in F\), put

\[
r_{C,q}
=\#\{X\in C:d(X)\le q\}.
\]

If

\[
r_{C,q}\le\rho_q
\qquad(C,q),
\tag{5.9}
\]

then

\[
\boxed{
\frac{\mathcal C}{W}
\le
\frac1n\sum_{q=1}^K\frac{\rho_q}{c_q}.
}
\tag{5.10}
\]

Indeed, \(R_q=\sum_Cr_{C,q}\le B\rho_q\) and \(W=nB\).
Consequently,

\[
\sum_{q=1}^K\frac{\rho_q}{c_q}=o(n)
\quad\Longrightarrow\quad
\mathcal C=o(W).
\tag{5.11}
\]

If at most \(r_m\) owners of each old row ever disagree through depth
\(K\), then

\[
\boxed{
\frac{\mathcal C}{W}
\le\frac{r_mH_1}{n}
\le\frac{r_m\lceil A\sqrt m\rceil}{2m+1}.
}
\tag{5.12}
\]

Hence

\[
\boxed{
r_m=o(\sqrt m)
\quad\Longrightarrow\quad
\mathcal C=o(W).
}
\tag{5.13}
\]

This permits every old row to participate, provided only
\(o(\sqrt m)\) of its \(n\) owners acquire an early disagreement. More
quantitatively, if \(r_m\le\varepsilon\sqrt m\), then

\[
\limsup_{m\to\infty}\frac{\mathcal C}{W}
\le\frac{\varepsilon A}{2}.
\tag{5.14}
\]

### Sparse contaminated rows

If only \(t_m\) old rows participate, then even releasing all their owners
at depth zero gives

\[
\boxed{
\mathcal C\le t_mnH_1,
\qquad
\frac{\mathcal C}{W}\le\frac{t_mK}{B}.
}
\tag{5.15}
\]

Therefore

\[
\boxed{
t_m=o(B/\sqrt m)
\quad\Longrightarrow\quad
\mathcal C=o(W).
}
\tag{5.16}
\]

If \(t_m\le\varepsilon B/\sqrt m\), the normalized cost is at most
\(\varepsilon A+o(1)\).

### Late releases

If at most \(M_m\) owners are ever released and all first disagreements
occur at depth at least \(d_0\), then

\[
\boxed{
\mathcal C\le M_mH_{d_0}.
}
\tag{5.17}
\]

Thus \(M_mH_{d_0}=o(W)\) is sufficient.

All these conclusions are literal exact-row statements once the stipulated
support-feasible balanced exchange family exists.

## 6. Cyclic packet cuts for synchronous releases

The gain cut (3.10) is universal, including mixed rows in which different
owners have different stopping depths. Stronger cyclic cuts require an
additional synchrony hypothesis.

Fix \(q\), put

\[
r=m-q,
\]

and suppose the released set \(\mathcal R_q\) is a union of \(p\) complete
rows of the endpoint factor \(G\). Thus

\[
R_q=np.
\tag{6.1}
\]

For a target family \(\mathcal U\subseteq V_q\), define the cyclic packet
capacity

\[
d_q^{\rm cyc}(\mathcal U)
=
\max_{\rho}
\#\{j\in\mathbb Z_n:I_\rho(j,r)\in\mathcal U\},
\tag{6.2}
\]

where the maximum is over allowed released rows.

Since every released row contributes at most
\(d_q^{\rm cyc}(\mathcal U)\) residual occurrences to \(\mathcal U\),

\[
s_q(\mathcal U)
\le p\,d_q^{\rm cyc}(\mathcal U).
\tag{6.3}
\]

Also,

\[
s_q(\mathcal U)
=b_q(\mathcal U)-g_q(\mathcal U)
\ge
\bigl(c_q|\mathcal U|-\mu_q^F(\mathcal U)\bigr)_+.
\tag{6.4}
\]

Hence:

### Theorem 6.1 — synchronous cyclic Hall cut

For every \(\mathcal U\subseteq V_q\),

\[
\boxed{
R_q
\ge
n\left\lceil
\frac{\delta_q(\mathcal U)}
{d_q^{\rm cyc}(\mathcal U)}
\right\rceil,
\qquad
\delta_q(\mathcal U)
=\bigl(c_q|\mathcal U|-\mu_q^F(\mathcal U)\bigr)_+.
}
\tag{6.5}
\]

If the denominator is zero and the numerator is positive, the synchronous
packet architecture is infeasible. If both vanish, the ratio is defined as
zero.

### Lemma 6.2 — exact cyclic star capacity

Let \(T\subseteq[n]\), \(1\le |T|=t\), and

\[
\mathcal U_T=\{S\in V_q:T\subseteq S\}.
\]

Then

\[
\boxed{
d_q^{\rm cyc}(\mathcal U_T)
\le(r-t+1)_+.
}
\tag{6.6}
\]

The universal bound is sharp: when \(t\le r\), an unrestricted row in
which the points of \(T\) are consecutive attains equality. A restricted
allowed-row catalog may have smaller capacity. When \(t>r\), both sides are
zero.

Proof. If \(t>r\), no \(r\)-set contains \(T\), so the claim is immediate.
Assume \(t\le r\). Fix one point \(x\in T\). The union of all cyclic \(r\)-intervals
containing \(x\) has at most \(2r-1<n\) coordinates, because
\(r=m-q<n/2\). Cut the circle outside this union. Every \(r\)-interval
containing \(T\) now lifts to an ordinary line interval. The shortest line
interval spanning the \(t\) distinct points of \(T\) has length at least
\(t\). If its length is \(\ell\), at most

\[
r-\ell+1\le r-t+1
\]

length-\(r\) intervals can contain it. Consecutive \(T\) has
\(\ell=t\), giving equality. \(\square\)

Combining (6.5)--(6.6), if

\[
\mathcal A\subseteq\mathcal U_T,
\]

then

\[
\boxed{
R_q
\ge
n\left\lceil
\frac{\delta_q(\mathcal A)}
{(m-q-t+1)_+}
\right\rceil.
}
\tag{6.7}
\]

The zero-denominator convention is the one in Theorem 6.1.

For \(q\le K/2\), (1.5) gives

\[
\sum_{j=1}^K\frac{R_j}{c_j}
\ge R_qH_q
\ge \frac{K}{2C_A}R_q.
\tag{6.8}
\]

Thus, for fixed \(\varepsilon>0\),

\[
\delta_q(\mathcal A)\ge\varepsilon\frac W{\sqrt m}
\quad\Longrightarrow\quad
\boxed{
\mathcal C
\ge
\left(\frac{\varepsilon A}{C_A}+o(1)\right)W.
}
\tag{6.9}
\]

This is twice the leading one-cut constant obtained from the unrestricted
owner inequality \(R_q\ge\delta_q\). It is valid only under synchronous
complete-row release at depth \(q\).

### Point-regular packet invariant

The same synchrony gives, for every coordinate \(x\),

\[
\#\{X\in\mathcal R_q:x\in X\}=mp.
\tag{6.10}
\]

Equivalently, for every coordinate weight \(\theta\) with
\(\sum_x\theta_x=0\),

\[
\sum_{X\in\mathcal R_q}\sum_{x\in X}\theta_x=0.
\tag{6.11}
\]

For a \(t\)-set \(T\), take

\[
w_T(X)=|X\cap T|-\frac{mt}{n}.
\]

Every forced gain owner containing \(T\) has weight
\(t(m+1)/n\), while every owner has weight at least \(-tm/n\).
If a Hall family \(\mathcal A\subseteq\mathcal U_T\) forces \(\delta\)
such gain owners, (6.11) implies

\[
\boxed{
R_q\ge\frac nm\,\delta.
}
\tag{6.12}
\]

Again, this strengthened constant is unavailable when rows mix stopping
depths.

## 7. The universal logarithmic-star obstruction survives rebundling

The next theorem needs no synchronous row release and applies to every
literal cyclic completion.

Let

\[
J=\lfloor K/2\rfloor,
\qquad
t=\lfloor\log_2n\rfloor.
\tag{7.1}
\]

Choose pairwise disjoint \(t\)-sets

\[
T_1,\ldots,T_J.
\tag{7.2}
\]

This is possible because \(Jt=o(m)\). For each \(q\le J\), let

\[
\mathcal A_q
\subseteq
\{S\in V_q:T_q\subseteq S\}
\]

and suppose

\[
\delta_q
:=\bigl(c_q|\mathcal A_q|-\mu_q^F(\mathcal A_q)\bigr)_+
\ge\eta B
\tag{7.3}
\]

for some fixed \(\eta>0\).

Put

\[
\mathcal G(T)
=\{X\in\Omega:T\subseteq X\},
\]

\[
G_t=|\mathcal G(T)|
=\binom{n-t}{m-t},
\qquad
G_{2t}=\binom{n-2t}{m-2t}.
\tag{7.4}
\]

Then

\[
G_t=\Theta(B),
\qquad
G_{2t}=O(B/n).
\tag{7.5}
\]

Indeed,

\[
\frac{G_t}{B}
=n\prod_{i=0}^{t-1}\frac{m-i}{n-i}
=(1+o(1))n2^{-t}=\Theta(1),
\]

while

\[
\frac{G_{2t}}{G_t}
=\prod_{i=0}^{t-1}
\frac{m-t-i}{n-t-i}
\le2^{-t}<\frac2n.
\]

### Theorem 7.1 — global star cut

Every literal cyclic completion satisfies

\[
\boxed{
R_J
\ge
\sum_{q=1}^J\delta_q
-\binom J2G_{2t}.
}
\tag{7.6}
\]

Consequently, under (7.3),

\[
\boxed{
\mathcal C
\ge
\frac{K-J+1}{C_A}
\left(
\eta BJ-\binom J2G_{2t}
\right)
=
\left(\frac{\eta A^2}{8C_A}+o_A(1)\right)W.
}
\tag{7.7}
\]

In particular, for all sufficiently large \(m\),

\[
\mathcal C
\ge
\frac{\eta A^2}{16C_A}W.
\tag{7.8}
\]

In fact, the proof uses only owner containment, balance, and permanent
release, so the same inequality holds for an arbitrary balanced Boolean
completion respecting the frozen prefixes.

Proof. The gain cut (3.12) supplies a set \(Z_q\) of at least
\(\delta_q\) owners which move into \(\mathcal A_q\). Every member of
\(Z_q\) contains \(T_q\) and is released before depth \(q\), so

\[
Z_q\subseteq\mathcal R_J\cap\mathcal G(T_q).
\]

Bonferroni gives

\[
\left|\bigcup_{q\le J}Z_q\right|
\ge
\sum_{q\le J}|Z_q|
-\sum_{q<s}|Z_q\cap Z_s|.
\]

The pair intersection is at most \(G_{2t}\), proving (7.6). Since releases
are permanent, \(R_r\ge R_J\) for every \(r\ge J\); (1.3) gives the first
inequality in (7.7). Finally,

\[
\frac{BJ(K-J)}W
=\frac{J(K-J)}n
=\left(\frac{A^2}{8}+o_A(1)\right),
\]

and the overlap contribution is

\[
O_A(B)\cdot O_A(\sqrt m)=o(W).
\]

This proves (7.7)--(7.8). \(\square\)

The present universal packet argument obtains no stronger leading order
than this multistar cut. Divisibility and point-regularity add only
lower-order corrections to the displayed proof. Nor does the naive
rowwise block-dispersion argument give a universal anti-concentration:
because \(Jt=o(n)\), one cyclic word can place all the disjoint blocks
\(T_q\) consecutively and give each star its maximum packet service.
Any stronger multistar packet theorem needs an additional rowwise
dispersion hypothesis.

No exact factor satisfying (7.3) is presently constructed. Theorem 7.1 is
therefore a sharp conditional obstruction, not an exact-factor
counterexample.

## 8. Row-local rigidity and the rank-isolated barrier

### Theorem 8.1 — fixed middle-packet rigidity

For \(m\ge2\), the packet of \(n\) middle windows of one row determines its cyclic
coordinate order up to dihedral symmetry.

Proof. Within the packet, two middle windows intersect in \(m-1\) points
exactly when they are consecutive. Thus the Johnson adjacency graph on the
packet recovers the defining \(C_n\). Consecutive set differences recover
the coordinate labels around that cycle, up to direction and rotation.
\(\square\)

Consequently, an oriented row with the same middle packet as an old row is
either the original orientation or its reversal. The original orientation
changes no flag. Reversal changes the depth-\(q\) interval of every owner
for every \(1\le q<m\). Hence every nontrivial same-packet rebundling has

\[
d(X)=1
\qquad\text{for all }n\text{ owners}
\]

and exact cost

\[
\boxed{
nH_1.
}
\tag{8.1}
\]

Therefore sparse owner-specific stops cannot be literalized independently
while preserving each participating row's middle packet. Any construction
using the \(o(\sqrt m)\)-per-old-row envelope from (5.9) must genuinely
exchange middle owners among multiple rows.

There is a second warning. Suppose a support-feasible exchange of \(s\)
rows is obtained by swapping one adjacent coordinate pair in every row,
with the displayed old and new orientations. The two row packets share
\(n-2\) owners. Among the shared owners, one owner has a rank-isolated first
disagreement at each depth

\[
1,\ldots,m-1.
\]

For fixed \(A\) and large \(m\), \(K\le m-1\), so permanent stopping costs
at least

\[
\boxed{
s\sum_{d=1}^KH_d
=s\sum_{q=1}^K\frac q{c_q}
\ge
s\,\frac{K(K+1)}{2C_A}.
}
\tag{8.2}
\]

If \(s=\eta B\), then

\[
\boxed{
\mathcal C
\ge
\left(\frac{\eta A^2}{4C_A}+o_A(1)\right)W.
}
\tag{8.3}
\]

Thus a positive density of rank-isolated cyclic trades is cheap for the
ordinary labelled mismatch sum but not for permanent stopping times.
This is only a prescribed factor-to-factor barrier. No positive-density
support-feasible adjacent-swap trade, balanced endpoint, or Hall protection
is constructed, so (8.3) does not obstruct choosing a different balanced
endpoint factor.

## 9. Exact implication scope and remaining theorem

The positive theorem proved here is:

> If, for every fixed \(A\), the row-state relaxation for some fixed
> integral balanced quota system has cost \(o(W)\), and all of its cyclic
> support nonintegrality is confined to an internally extendible owner leave
> of size \(o(W/\sqrt m)\), then it has a literal integral cyclic completion
> of cost \(o(W)\).

The legal-exchange theorem gives a more concrete sufficient form:

> Construct support-disjoint multirow exchanges whose endpoint exact factor
> is balanced through \(K\) and whose per-old-row profile satisfies
> \[
> \sum_{q=1}^K\frac{\rho_q}{c_q}=o(n).
> \]
> Then the old flags admit owner-specific stopping depths, all released
> tails are globally rebundled into the new exact rows, all frozen prefixes
> fit the balanced quotas, and
> \[
> \sum_{q=1}^K\frac{R_q}{c_q}=o(W).
> \]

What remains unproved is the cyclic positivity/existence statement
producing such a balanced endpoint or such a cheap fractional row-state
cover. In particular:

- Boolean Hoffman feasibility does not imply decorated-row exact cover;
- rankwise owner Hall cuts do not imply nesting or row packetization;
- a fractional row-state cover need not be integral outside the
  forest/small-extendible regime;
- same-packet orientation changes are rigid and cannot realize sparse
  owner stops;
- positive-density adjacent-symbol trades pay \(\Theta_A(W)\) permanent
  cost;
- the logarithmic-star cuts give a conditional \(\Omega_A(W)\)
  obstruction, but no factor realizing them is known.

An endpoint \(G\) satisfying (1.10) is a depth-perfect exact factor on the
fixed window, a statement stronger than unlabelled MWB and stronger than
the already sufficient labelled synchronization theorem. Accordingly, the
failure of this literal route would not refute MWB, arbitrary balanced
Boolean rebundling, a rejoining owner scheme, or a direct OR-word
construction.

The exact surviving gate is:

\[
\boxed{
\begin{gathered}
\text{find a cheap fractional or legal-exchange cyclic row cover,}\\
\text{prove forest/small-leave integrality or another normality theorem,}\\
\text{and avoid the gain-capable and logarithmic-star cuts.}
\end{gathered}
}
\]

## 10. Independent audit record

Three independent adversarial audits rederived the decisive steps. The
following points passed after the stated corrections were incorporated.

1. The fixed-quota dual (3.2)--(3.3) uses target equalities
   \(Hx=b\); the mobile-quota dual (3.4) has the correct minimization over
   \(\mathcal B\). All signs are correct.
2. The decorated-row equivalence is exact when every clone injection is
   included as an edge variant. Its Farkas system is fractional; no
   integral Hall characterization is claimed.
3. Forest-support total unimodularity is valid for a fixed integral
   balanced quota vector. The bad-component completion must keep its entire
   owner and target incidence inside the bad resource union. Under that
   hypothesis, the surcharge \(LH_1\le LK\) and the scale
   \(L=o(W/\sqrt m)\) are exact.
4. The legal-exchange identity and the constants in
   (5.12), (5.15), and (5.17) are correct.
5. The one-rank Hall equivalence requires \(g_q\le b_q\), as stated.
   The cyclic star and point-regularity improvements require
   \(\mathcal R_q\) itself to be a union of complete endpoint rows.
6. The common-cut proof of Lemma 6.2 handles all cyclic intervals
   simultaneously. Its positive-part and zero-denominator conventions are
   explicit.
7. The coefficient in (6.9), the logarithmic-star asymptotic coefficient
   \(\eta A^2/(8C_A)\), the safe eventual coefficient
   \(\eta A^2/(16C_A)\), and the adjacent-swap coefficient
   \(\eta A^2/(4C_A)\) all check.
8. The adjacent-swap estimate is only a prescribed factor-to-factor
   barrier. The logarithmic-star theorem is conditional on deficits in one
   exact factor. Neither is presented as an existential exact-factor
   counterexample.

No unproved normality, cyclic positivity, balanced endpoint construction,
or reverse implication from Boolean Hoffman flow is used.
