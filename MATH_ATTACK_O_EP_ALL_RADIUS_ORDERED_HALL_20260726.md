# EP_A: full-collar bridge graph and the all-radius ordered-Hall obstruction

Date: 2026-07-26

Pure mathematics only. No finite search, computation, or probabilistic
selection is used.

## 0. Outcome and precise boundary

Put

\[
 W=\binom{2m}{m},\qquad N_q=\binom{2m}{m-q},\qquad
 H=\lceil A\sqrt m\rceil
\]

for fixed \(A>0\).  The decorated-SCD extension assertion
\(\mathrm{EP}_A\) asks for one clipped symmetric-chain decomposition,
one radius-\(H\) collar on each of its \(W\) chains, and a bridge-one
path cover with

\[
 p=o_A(W/H).
\]

All finite statements below assume \(1\le H<m\).  For fixed \(A\) and
\(H=\lceil A\sqrt m\rceil\), this holds for all sufficiently large
\(m\).

This report does **not** prove \(\mathrm{EP}_A\).  It derives an exact
ordered-Hall formulation and a new selector-independent obstruction that
holds simultaneously at every radius \(1\le q\le H\).  Its principal
conclusions are as follows.

1. The full collar-state bridge digraph is in/out regular of degree
   \[
   1+(m-H)^2+2H(m-H)=1+m^2-H^2.
   \]
   This ambient degree does not survive the SCD and collar selections in
   a form that implies Hall expansion.

2. If two distinct selected chains both have tag at least \(q\), then
   every full bridge-one arc between them projects, after absorbing the
   outer \(H-q\) collar coordinates, to a genuine radius-\(q\) rotor
   arc.  A late full promotion, rather than a full rotor, may induce that
   projected rotor arc.

3. Let \(\kappa_q(\mathcal D)\) be the minimum number of paths covering
   the \(N_q\) radius-\(q\) truncations of the tag-at-least-\(q\) chains
   by radius-\(q\) rotor arcs.  Every \(p\)-path EP cover satisfies,
   simultaneously for every \(q\),
   \[
   \boxed{\kappa_q(\mathcal D)\le W-N_q+p.}
   \]
   This has an exact ordered-Hall form.  At \(q=1\), EP therefore
   requires an almost spanning radius-one rotor linear forest:
   \[
   \kappa_1(\mathcal D)=o_A(W/H).
   \]

4. The compatible forest must be coherent across radii.  If an edge
   between tags \(d,d'\) is weighted by \(\min(d,d')\), then one directed
   linear forest in the hierarchical rotor graph must have weight at
   least
   \[
   \bigl(\Phi_A+o_A(1)\bigr)W\sqrt m,
   \qquad
   \Phi_A=\int_0^{\min(A,\sqrt{\log2})}(2e^{-t^2}-1)\,dt>0.
   \]
   In particular it has a positive density of edges for every fixed
   \(A>0\), even when the old top-tag binary cut is silent.

5. There is an exact capacitated Hall formula, before collars are chosen,
   for the least possible mismatch between entrance and exit
   \(2q\)-word histograms.  It is a literal obstruction on one SCD, not a
   marginal degree estimate.

6. Independently, contraction of promotion fibres gives
   \[
   \boxed{p+r\ge N_H,}
   \]
   where \(r\) is the number of genuine full-\(H\) rotor arcs in the
   cover.  Thus EP needs
   \(r\ge(e^{-A^2}-o_A(1))W\).  Projected shallow rotors supplied by deep
   promotions cannot replace this full-rotor requirement.

7. The earlier claim that the clipped BTK tag-\(H\) rotor graph is empty
   is false.  An explicit rotor edge exists for every \(1\le H<m\).
   Consequently the BTK corollary in
   `MATH_ATTACK_EP_TAGH_COMMON_BASE_RECURSIVE_AUDIT_20260725.md` cannot be
   used.  This correction does not affect the all-radius theorem proved
   here.

The exact remaining positive gate is therefore a correlated SCD and
collar selection satisfying the full ordered-Hall inequalities, the
simultaneous all-radius inequalities, and the full-top fibre cut with
\(o_A(W/H)\) deficiency.  No argument from the ambient degree and radius
census alone supplies such a selection.

## 1. Clipped SCD census and collar extensions

Let \(\mathcal D\) be a symmetric-chain decomposition of the Boolean
lattice on \([2m]\), clipped to the ranks
\(m-H,\ldots,m+H\).  Every clipped chain has a tag
\(d\in\{0,\ldots,H\}\) and can be written

\[
 (A;c_1,\ldots,c_{2d};B),
 \qquad |A|=|B|=m-d,
 \tag{1.1}
\]

where its masks are

\[
 A\subset A+c_1\subset\cdots\subset A+c_1+\cdots+c_{2d},
 \tag{1.2}
\]

and \(A\), \(\{c_1,\ldots,c_{2d}\}\), and \(B\) partition
\([2m]\).  Its middle owner is

\[
 X=A+\{c_1,\ldots,c_d\}.
 \tag{1.3}
\]

Let \(\gamma_d\) be the number of tag-\(d\) chains.  At rank
\(m-q\), precisely the chains of tag at least \(q\) occur, one mask per
chain.  Hence

\[
 \sum_{d=q}^H\gamma_d=N_q.
 \tag{1.4}
\]

Taking consecutive differences gives the exact clipped census

\[
 \boxed{
 \gamma_d=N_d-N_{d+1}\quad(0\le d<H),\qquad
 \gamma_H=N_H,
 }
 \tag{1.5}
\]

and in particular \(\sum_{d=0}^H\gamma_d=W\).  Explicitly,

\[
 \gamma_d
 =\frac{2d+1}{m+d+1}N_d
 \quad(d<H).
 \tag{1.6}
\]

A radius-\(H\) collar extension of (1.1) chooses ordered distinct
coordinates

\[
 \alpha_1,\ldots,\alpha_{H-d}\in A,
 \qquad
 \beta_1,\ldots,\beta_{H-d}\in B
 \tag{1.7}
\]

and produces

\[
 \omega=(L;z_1,\ldots,z_{2H};R),
 \tag{1.8}
\]

where

\[
 L=A\setminus\{\alpha_1,\ldots,\alpha_{H-d}\},\qquad
 R=B\setminus\{\beta_1,\ldots,\beta_{H-d}\},
 \tag{1.9}
\]

and

\[
 z=(\alpha_1,\ldots,\alpha_{H-d},
 c_1,\ldots,c_{2d},
 \beta_1,\ldots,\beta_{H-d}).
 \tag{1.10}
\]

Thus the number of extensions of a tag-\(d\) chain is exactly

\[
 \boxed{E_{d,H}=\bigl((m-d)_{H-d}\bigr)^2.}
 \tag{1.11}
\]

The middle owner and full lower and upper collar masks are

\[
 X(\omega)=L+\{z_1,\ldots,z_H\},
 \tag{1.12}
\]

\[
 D_H(\omega)=L,
 \qquad
 U_H(\omega)=L+\{z_1,\ldots,z_{2H}\}=[2m]\setminus R.
 \tag{1.13}
\]

For tag \(H\), (1.11) equals one.  These boundary chains have no collar
freedom.

## 2. The directed bridge-one graph on all full collar states

Let \(\Omega_H\) consist of all states (1.8) in which
\(L,R,\{z_1,\ldots,z_{2H}\}\) partition \([2m]\),
\(|L|=|R|=m-H\), and the \(z_i\) are ordered.  Put

\[
 r=m-H.
\]

The directed bridge-one graph \(\mathfrak B_H\) has the following
complete successor list.

* Identity:
  \[
  (L;z_1,\ldots,z_{2H};R).
  \tag{2.1}
  \]

* Rotor, for \(x\in L\), \(y\in R\):
  \[
  (L-x+y;\ x,z_1,\ldots,z_{2H-1};\ R-y+z_{2H}).
  \tag{2.2}
  \]

* Promotion, for \(x\in L\), \(1\le j\le2H\):
  \[
  (L-x+z_j;\ x,z_1,\ldots,\widehat z_j,\ldots,z_{2H};\ R).
  \tag{2.3}
  \]

### Proposition 2.1 (exact regular degree)

The graph \(\mathfrak B_H\) is in/out regular of degree

\[
 \boxed{1+r^2+2Hr=1+m^2-H^2.}
 \tag{2.4}
\]

#### Proof

The successor counts in (2.1)--(2.3) are respectively \(1,r^2,2Hr\).
Different parameter choices give different successors: a rotor is
identified by its new first word coordinate and the change in \(R\),
while a promotion preserves \(R\) and is identified by its new first
coordinate and omitted old word coordinate.

For predecessors of a fixed state, a rotor predecessor is determined by
choosing the entering coordinate in its current lower block and the old
last word coordinate in its current residual block, giving \(r^2\)
choices.  A promotion predecessor is determined by a coordinate in the
current lower block and one of \(2H\) insertion slots, giving \(2Hr\)
choices.  Together with identity this proves equal indegree and outdegree.
\(\square\)

The identity loop cannot join different selected chains.  Nor can a
promotion with \(j\le H\): it preserves the middle owner, and an SCD has
only one chain through each middle owner.  These elementary exclusions
already show why the raw degree is not the selected degree.

## 3. Exact full-state ordered-Hall formulation of EP

Choose one collar \(e(C)\in\operatorname{Ext}_H(C)\) for every chain
\(C\in\mathcal D\).  For a total order \(\prec\) on the \(W\) chains,
form a split bipartite graph

\[
 B_\prec(\mathcal D,e)
 \tag{3.1}
\]

with left and right copies of \(\mathcal D\), putting
\(C_LC'_R\) in the graph exactly when

\[
 C\prec C'
 \quad\hbox{and}\quad
 e(C)\longrightarrow e(C')
 \text{ in }\mathfrak B_H.
 \tag{3.2}
\]

Let \(p(\mathcal D,e)\) be the minimum number of directed paths in a
vertex partition of the selected states.

### Theorem 3.1 (exact ordered-Hall equality)

For every fixed \((\mathcal D,e)\),

\[
 \boxed{
 p(\mathcal D,e)
 =\min_\prec\bigl(W-\nu(B_\prec(\mathcal D,e))\bigr)
 =\min_\prec\max_{\mathcal A\subseteq\mathcal D}
 \bigl(|\mathcal A|-|N_{B_\prec}(\mathcal A)|\bigr).
 }
 \tag{3.3}
\]

#### Proof

Given a directed path cover, order the vertices consistently along every
path and extend this to a total order.  Its \(W-p\) path arcs form a
matching in (3.1), because every selected vertex has at most one incoming
and one outgoing path arc.  Hence
\(W-\nu(B_\prec)\le p\).

Conversely, a matching in \(B_\prec\) gives every vertex indegree and
outdegree at most one.  All selected arcs increase in \(\prec\), so they
contain no directed cycle.  They therefore form a directed linear forest
with \(W-|M|\) path components.  Maximizing \(|M|\) and minimizing over
orders proves the first equality.  The second is the bipartite deficiency
form of Hall's theorem.
\(\square\)

Consequently, if

\[
 P_{m,H}:=min_{\mathcal D}\min_e\min_\prec
 \max_{\mathcal A\subseteq\mathcal D}
 \bigl(|\mathcal A|-|N_{B_\prec}(\mathcal A)|\bigr),
 \tag{3.4}
\]

then the exact statement \(\mathrm{EP}_A\) is

\[
 \boxed{P_{m,H}=o_A(W/H).}
 \tag{3.5}
\]

The minimization over collars must occur before the Hall neighbourhoods
are tested.  Taking the union of edges realizable under different collars
is invalid: the same selected collar of a chain must support both its
incoming and outgoing path arcs.

## 4. Absorbed truncation and the all-radius rigidity theorem

Fix \(0\le q\le H\) and write

\[
 a=H-q,\qquad b=H+q.
 \tag{4.1}
\]

For a full state \(\omega=(L;z_1,\ldots,z_{2H};R)\), define

\[
 \tau_q\omega
 =\bigl(D_q;w_1,\ldots,w_{2q};E_q\bigr),
 \tag{4.2}
\]

where

\[
 D_q=L+\{z_1,\ldots,z_a\},
 \qquad w_i=z_{a+i},
 \tag{4.3}
\]

\[
 E_q=R+\{z_{b+1},\ldots,z_{2H}\}.
 \tag{4.4}
\]

Its upper mask is

\[
 T_q=[2m]\setminus E_q
 =L+\{z_1,\ldots,z_b\}.
 \tag{4.5}
\]

Empty intervals in (4.3)--(4.4) are omitted.

### Lemma 4.1 (truncation is forced by the SCD chain)

If the underlying chain has tag \(d\ge q\), then \(\tau_q\omega\) is
independent of the chosen radius-\(H\) collar and is exactly the segment
of that SCD chain between ranks \(m-q\) and \(m+q\).  More explicitly,

\[
 D_q=A+\{c_1,\ldots,c_{d-q}\},
 \tag{4.6}
\]

\[
 (w_1,\ldots,w_{2q})
 =(c_{d-q+1},\ldots,c_{d+q}),
 \tag{4.7}
\]

\[
 E_q=B+\{c_{d+q+1},\ldots,c_{2d}\}.
 \tag{4.8}
\]

#### Proof

Substitute (1.9)--(1.10) into (4.3)--(4.4).  The first
\(H-d\) word entries restore every removed lower collar coordinate, and
the next \(d-q\) entries are \(c_1,\ldots,c_{d-q}\), giving (4.6).
The central positions give (4.7).  On the other side, the final
\(H-d\) entries restore the removed upper collar coordinates and leave
the central suffix in (4.8).
\(\square\)

Let

\[
 \mathcal D_{\ge q}=\{C\in\mathcal D:\operatorname{tag}(C)\ge q\}.
 \tag{4.9}
\]

By (1.4), \(|\mathcal D_{\ge q}|=N_q\).  Moreover, both maps

\[
 C\mapsto D_q(C),\qquad C\mapsto T_q(C)
 \tag{4.10}
\]

are bijections from \(\mathcal D_{\ge q}\) to the ranks \(m-q\) and
\(m+q\), respectively.  They are injective because distinct SCD chains
are mask-disjoint, and the cardinalities agree.

### Theorem 4.2 (all-radius bridge rigidity)

Let \(1\le q\le H\).  If a full bridge-one arc joins selected collars of
two distinct chains in \(\mathcal D_{\ge q}\), then their truncations
under \(\tau_q\) form a genuine directed radius-\(q\) rotor arc.

#### Proof

First suppose \(q<H\), so \(a\ge1\).

For a full rotor (2.2), direct substitution in (4.2) gives

\[
 D'_q=D_q-z_a+y,
 \tag{4.11}
\]

\[
 (w'_1,\ldots,w'_{2q})
 =(z_a,w_1,\ldots,w_{2q-1}),
 \tag{4.12}
\]

\[
 E'_q=E_q-y+w_{2q}.
 \tag{4.13}
\]

This is exactly the radius-\(q\) rotor rule, with departure \(z_a\) and
entry \(y\).

For a promotion (2.3), there are three exact slot regimes:

\[
\begin{array}{c|c}
1\le j\le a & \tau_q\omega'=\tau_q\omega,\\[1mm]
a<j\le b & \text{a radius-}q\text{ promotion at slot }j-a,\\[1mm]
b<j\le2H & \text{a radius-}q\text{ rotor.}
\end{array}
\tag{4.14}
\]

In the first regime the transferred coordinates are entirely absorbed
into \(D_q\).  Thus the lower mask \(D_q\) is unchanged, which is
impossible for two distinct chains by (4.10).

In the middle regime,

\[
 D'_q=D_q-z_a+z_j,
 \tag{4.15}
\]

\[
 w'=(z_a,w_1,\ldots,\widehat{w_{j-a}},\ldots,w_{2q}),
 \qquad E'_q=E_q.
 \tag{4.16}
\]

Equivalently \(T'_q=T_q\).  This is impossible for two distinct SCD
chains by upper-endpoint injectivity in (4.10).

In the last regime, \(z_j\in E_q\), and substitution gives

\[
 D'_q=D_q-z_a+z_j,
 \tag{4.17}
\]

\[
 w'=(z_a,w_1,\ldots,w_{2q-1}),
 \tag{4.18}
\]

\[
 E'_q=E_q-z_j+w_{2q}.
 \tag{4.19}
\]

This is precisely a radius-\(q\) rotor with departure \(z_a\) and entry
\(z_j\).

When \(q=H\), \(\tau_H\) is the full state.  Every promotion preserves
the full upper mask \(T_H\), so (4.10) excludes it between distinct
tag-\(H\) chains.  The remaining nonidentity case is the original
full rotor.  This proves the theorem.
\(\square\)

The common-SCD hypothesis is essential.  Arbitrary ambient states joined
by a promotion in a middle slot can have the same rank-\((m+q)\) mask;
the exclusion works only because two selected chains of one SCD cannot
share that mask.

One useful immediate consequence is the following slot restriction.  If
a promotion joins distinct positive-tag SCD chains of tags \(d,d'\), then
with \(q=\min(d,d')\),

\[
 \boxed{j>H+q.}
 \tag{4.20}
\]

At the omitted boundary \(q=0\), one has

\[
 \tau_0\omega=(X(\omega);\ ;X(\omega)^c).
 \tag{4.21}
\]

Promotions with \(j\le H\) preserve \(X\) and hence cannot join two
distinct chains of one SCD.  Full rotors and promotions with \(j>H\)
project respectively to the ordinary Johnson moves

\[
 X\longmapsto X-z_H+y,
 \qquad
 X\longmapsto X-z_H+z_j.
 \tag{4.22}
\]

This is a consistency check, but it is not called a positive-radius rotor
state and supplies no additional SCD census cut.

## 5. Multiscale path census and exact ordered-Hall cuts

Let \(G_q(\mathcal D)\) be the directed radius-\(q\) rotor graph on
\(\mathcal D_{\ge q}\): an arc \(C\to C'\) means that the forced
truncations \(\tau_q C\to\tau_q C'\) obey the radius-\(q\) rotor rule.
For \(S\subseteq\mathcal D_{\ge q}\), let

\[
 \lambda_q(S)=\max\{|E(F)|:F\subseteq G_q[S]
 \text{ is a directed vertex-disjoint linear forest}\},
 \tag{5.1}
\]

and

\[
 \kappa_q(S)=|S|-\lambda_q(S).
 \tag{5.2}
\]

Thus \(\kappa_q(S)\) is the minimum number of paths in a spanning
directed rotor path cover of \(S\).

### Theorem 5.1 (all-radius subset obstruction)

If one decoration of \(\mathcal D\) has a full bridge-one path cover with
\(p\) paths, then for every \(1\le q\le H\) and every
\(S\subseteq\mathcal D_{\ge q}\),

\[
 \boxed{
 \kappa_q(S)\le W-|S|+p,
 }
 \tag{5.3}
\]

or equivalently

\[
 \boxed{
 p\ge
 \bigl(2|S|-W-\lambda_q(S)\bigr)_+.
 }
 \tag{5.4}
\]

In particular,

\[
 \boxed{
 \kappa_q(\mathcal D_{\ge q})\le W-N_q+p,
 }
 \tag{5.5}
\]

\[
 \boxed{
 p\ge
 \bigl(2N_q-W-\lambda_q(\mathcal D_{\ge q})\bigr)_+.
 }
 \tag{5.6}
\]

#### Proof

Delete from the full \(p\)-path cover the \(W-|S|\) vertices outside
\(S\).  Deleting one vertex from a family of paths increases the number
of remaining runs by at most one.  Hence the vertices of \(S\) lie in at
most

\[
 p+W-|S|
 \tag{5.7}
\]

surviving runs.  Every edge in such a run is a full bridge-one edge
between distinct chains of tag at least \(q\), and Theorem 4.2 projects it
to a radius-\(q\) rotor edge.  The projected runs are therefore a
spanning rotor path cover of \(S\), proving (5.3).  Equations
(5.4)--(5.6) follow from (5.2) and \(|\mathcal D_{\ge q}|=N_q\).
\(\square\)

### Theorem 5.2 (simultaneous ordered-Hall form)

For a total order \(\prec\) on \(\mathcal D\), let
\(B_{q,\prec}[S]\) be the split bipartite graph whose edges are the
radius-\(q\) rotor arcs in \(G_q[S]\) that increase in \(\prec\).  Then

\[
 \kappa_q(S)
 =\min_\prec\max_{\mathcal A\subseteq S}
 \bigl(|\mathcal A|-|N_{B_{q,\prec}[S]}(\mathcal A)|\bigr).
 \tag{5.8}
\]

More strongly, a full \(p\)-path EP cover has one common topological order
\(\prec\) for which, simultaneously for all \(q,S,\mathcal A\),

\[
 \boxed{
 |\mathcal A|-|N_{B_{q,\prec}[S]}(\mathcal A)|
 \le W-|S|+p.
 }
 \tag{5.9}
\]

#### Proof

As in Theorem 3.1, a forward split matching is precisely a directed
linear forest, after optimizing over total orders.  Hall's deficiency
formula gives (5.8).

For a fixed full path cover, take one total order increasing along all of
its paths.  The deletion argument in Theorem 5.1 leaves at least
\(2|S|-W-p\) internal arcs on \(S\).  These arcs form a matching in
\(B_{q,\prec}[S]\).  Hence

\[
 |S|-\nu(B_{q,\prec}[S])\le W-|S|+p.
\]

Applying Hall's equality to the left side proves (5.9).
\(\square\)

Define the selector-independent multiscale ordered deficiency

\[
 \Delta_{\rm ms}(\mathcal D,\prec)
 =\max_{\substack{1\le q\le H\\S\subseteq\mathcal D_{\ge q}\\
 \mathcal A\subseteq S}}
 \left(
 |\mathcal A|-|N_{B_{q,\prec}[S]}(\mathcal A)|-(W-|S|)
 \right)_+.
 \tag{5.10}
\]

Then every EP cover obeys the exact necessary inequality

\[
 p\ge\Delta_{\rm ms}(\mathcal D,\prec)
 \tag{5.11}
\]

for its topological order.  Thus

\[
 \boxed{
 \min_{\mathcal D,\prec}\Delta_{\rm ms}(\mathcal D,\prec)
 \not=o_A(W/H)
 }
 \tag{5.12}
\]

would be a definitive ordered-Hall refutation of \(\mathrm{EP}_A\).
Conversely, a small value in (5.12) is not sufficient: it uses the relaxed
radius-\(q\) rotor graphs and does not yet choose mutually compatible full
collars.  Exact sufficiency is (3.3)--(3.5).

## 6. Quantitative consequences of the exact radius census

The exact ratio is

\[
 \frac{N_q}{W}
 =\prod_{i=0}^{q-1}\frac{m-i}{m+i+1}.
 \tag{6.1}
\]

Uniformly for \(q\le A\sqrt m\), Taylor expansion gives

\[
 \log\frac{N_q}{W}
 =-\frac{q^2}{m}
 +O_A(m^{-1/2}).
 \tag{6.2}
\]

More generally, for \(q=o(m)\), before specializing \(q\), one may use

\[
 \log\frac{N_q}{W}
 =-\frac{q^2}{m}
 +O\!\left(\frac qm+\frac{q^3}{m^2}\right).
 \tag{6.3}
\]

For \(q=1\),

\[
 N_1=\frac{m}{m+1}W,
 \qquad W-N_1=\frac{W}{m+1}.
 \tag{6.4}
\]

Therefore (5.5) implies under EP

\[
 \boxed{
 \kappa_1(\mathcal D)
 \le\frac{W}{m+1}+o_A(W/H)
 =o_A(W/H).
 }
 \tag{6.5}
\]

Thus the same completed SCD must already have an almost spanning
radius-one rotor linear forest on all of its positive-tag truncations.
This is not the old fixed-\(q=2\) issue; it is the first member of a nested
family required through the entire Gaussian window.

If \(1\le q\le H\) and \(q=o(\sqrt m)\), (5.6) and (6.3) give

\[
 \boxed{
 \lambda_q(\mathcal D_{\ge q})
 \ge W-O(q^2W/m)-o_A(W/H).
 }
 \tag{6.6}
\]

If \(q=\lfloor\alpha\sqrt m\rfloor\le H\), with fixed
\(0<\alpha<\sqrt{\log2}\), then

\[
 \boxed{
 \lambda_q(\mathcal D_{\ge q})
 \ge\bigl(2e^{-\alpha^2}-1-o_A(1)\bigr)W.
 }
 \tag{6.7}
\]

All these conditions must hold for one SCD and, in the ordered form, one
global order.  A construction of good tag-\(H\) packets followed by an
arbitrary completion at smaller tags therefore does not address EP.

## 7. Exact collar-port Hall obstruction

The preceding rotor graphs forget which radius-\(q\) departure is exposed
by the chosen full collar.  For \(1\le q<H\), define for
\(C\in\mathcal D_{\ge q}\)

\[
 \ell_q(C)=(z_{H-q+1},\ldots,z_{H+q}),
 \tag{7.1}
\]

\[
 r_{q,e}(C)=(z_{H-q},\ldots,z_{H+q-1}).
 \tag{7.2}
\]

The first is the forced central radius-\(q\) word.  The second is its
one-step-left exit word and can depend on the collar selection.

By (4.12) and (4.18), every full bridge arc internal to
\(\mathcal D_{\ge q}\) obeys

\[
 \boxed{r_{q,e}(C)=\ell_q(C').}
 \tag{7.3}
\]

Let \(R_{q,e}(\sigma)\) and \(L_q(\sigma)\) be the histograms of these
two words over ordered \(2q\)-tuples \(\sigma\).  Both have total mass
\(N_q\).

### Proposition 7.1 (literal port-imbalance cut)

Every full bridge path cover with \(p\) paths satisfies

\[
 \boxed{
 \frac12\sum_\sigma
 |R_{q,e}(\sigma)-L_q(\sigma)|
 \le W-N_q+p.
 }
 \tag{7.4}
\]

#### Proof

By (7.3), internal arcs can match only equal exit and entrance words.
Their number is therefore at most

\[
 \sum_\sigma\min(R_{q,e}(\sigma),L_q(\sigma))
 =N_q-\frac12\|R_{q,e}-L_q\|_1.
 \tag{7.5}
\]

The run census in Theorem 5.1 gives at least \(2N_q-W-p\) internal
arcs.  Combining the two inequalities proves (7.4).
\(\square\)

There is an exact pre-decoration minimization of the left side.  Let
\(\mathcal C_q\) be the tag-exactly-\(q\) chains.  A member

\[
 K=(A;c_1,\ldots,c_{2q};B)
 \tag{7.6}
\]

has the exit-word menu

\[
 \boxed{
 \mathcal M_q(K)
 =\{(a,c_1,\ldots,c_{2q-1}):a\in A\}.
 }
 \tag{7.7}
\]

Indeed \(z_{H-q}\) is the last lower collar coordinate, and any
\(a\in A\) can occupy that position; the remaining \(H-q-1\) lower
collar coordinates can then be ordered arbitrarily.  For tags greater
than \(q\), the exit word is internal to the original chain and is
already forced.

Let \(F_q(\sigma)\) count the forced exit words contributed by chains of
tag greater than \(q\).  Put

\[
 \mathcal E_q^{\rm port}
 =\sum_\sigma(F_q(\sigma)-L_q(\sigma))_+,
 \tag{7.8}
\]

\[
 b_\sigma=(L_q(\sigma)-F_q(\sigma))_+.
 \tag{7.9}
\]

Form the capacitated bipartite graph from \(\mathcal C_q\) to word bins,
with neighbourhoods (7.7) and bin capacities \(b_\sigma\).  Let \(M_q\)
be its maximum capacitated matching size.

### Theorem 7.2 (exact collar-selection Hall formula)

The least possible port imbalance at radius \(q\), over all collar
choices, is

\[
 \boxed{
 \mathfrak I_q(\mathcal D)
 :=\min_e\frac12\|R_{q,e}-L_q\|_1
 =\mathcal E_q^{\rm port}+\gamma_q-M_q.
 }
 \tag{7.10}
\]

Equivalently, by capacitated Hall,

\[
 \boxed{
 \mathfrak I_q(\mathcal D)
 =\mathcal E_q^{\rm port}+
 \max_{\mathcal S\subseteq\mathcal C_q}
 \left(
 |\mathcal S|-\sum_{\sigma\in N(\mathcal S)}b_\sigma
 \right)_+.
 }
 \tag{7.11}
\]

Every EP decoration consequently satisfies

\[
 \boxed{
 p\ge
 \bigl(\mathfrak I_q(\mathcal D)-(W-N_q)\bigr)_+.
 }
 \tag{7.12}
\]

#### Proof

The forced histogram \(F_q\) has mass \(N_q-\gamma_q\), while \(L_q\)
has mass \(N_q\).  Hence

\[
 \sum_\sigma b_\sigma=\gamma_q+\mathcal E_q^{\rm port}.
 \tag{7.13}
\]

Each tag-\(q\) chain assigned to an available deficit slot reduces the
unmatched deficit by one and creates no excess.  At most \(M_q\) chains
can be assigned this way.  Every one of the remaining
\(\gamma_q-M_q\) chains must add one unit outside the remaining deficit
capacity, producing one unit of final excess.  Since the final entrance
and exit masses agree, total positive excess equals total negative
deficit.  The minimum total variation is therefore
\(\mathcal E_q^{\rm port}+\gamma_q-M_q\), proving (7.10).

The capacitated matching deficiency formula is

\[
 \gamma_q-M_q
 =\max_{\mathcal S\subseteq\mathcal C_q}
 \left(
 |\mathcal S|-\sum_{\sigma\in N(\mathcal S)}b_\sigma
 \right)_+,
\]

which gives (7.11).  Finally combine (7.10) with Proposition 7.1.
\(\square\)

These port minimizations can be realized simultaneously for all
\(q<H\).  The only extension coordinate affecting (7.2) freely at depth
\(q\) belongs to a tag-exactly-\(q\) chain; for deeper tags it is forced,
and shallower tags do not occur in \(\mathcal D_{\ge q}\).  Thus the
free decisions for distinct \(q\) lie on disjoint chain classes.  This is
a genuine positive collar-selection statement.  It does not choose the
upper collar orders or prove the full chronological Hall inequalities
(3.3).

For later use, the elementary product bound

\[
 W-N_q\le\frac{q^2}{m}W
 \tag{7.14}
\]

follows from (6.1) and
\(1-\prod_i(1-a_i)\le\sum_i a_i\).  Therefore EP forces

\[
 \mathfrak I_q(\mathcal D)=o_A(W/H)
 \tag{7.15}
\]

whenever \(q^2H/m\to0\); for \(H\asymp\sqrt m\), this includes every
\(q=o(m^{1/4})\).

## 8. Why degree \(1+m^2-H^2\) does not give Hall expansion

Fix \(1\le q<H\) and a selected full source state whose underlying SCD
chain has tag at least \(q\).  The ambient degree (2.4) splits exactly as

\[
 \boxed{
 1+m^2-H^2
 =\underbrace{1+H(m-H)}_{\text{identity or same middle owner}}
 +\underbrace{q(m-H)}_{\substack{H<j\le H+q;\\T_q\text{ preserved}}}
 +\underbrace{(m-H)(m-q)}_{\text{possible projected }q\text{-rotors}}.
 }
 \tag{8.1}
\]

The last term consists of

\[
 (m-H)^2
 \]

full rotors and

\[
 (H-q)(m-H)
 \]

late promotions.  Under \(\tau_q\), these collapse in fibres of size
\(m-H\) to only \(m-q\) distinct radius-\(q\) successor states:

* the \(m-H\) residual entries \(y\in R\) coming from full rotors;
* the \(H-q\) entries \(z_j\), \(j>H+q\), coming from late promotions.

The lower-coordinate choice \(x\in L\) disappears after absorption and
accounts for the fibre multiplicity.  Since an SCD has at most one chain
with a given forced radius-\(q\) state, the actual selected bridge
outdegree from one decorated source into
\(\mathcal D_{\ge q}\) is at most \(m-q\), and can be zero.

The high-tag hypothesis on the source is necessary for that last bound.
If the source has tag below \(q\), its incidental mask \(T_q\) is not an
SCD member of the source chain, so the middle-slot promotions can also hit
the unique high-tag chain that owns \(T_q\).  The same argument then gives
only the general bound \(m-q+1\).

At \(q=H\), there is no absorption: all promotions preserve the full top
and are forbidden between distinct tag-\(H\) chains, while the
\((m-H)^2\) full rotors remain distinct candidates.  In neither case does
regularity of the ambient graph imply any one of the Hall inequalities
(3.3), (5.9), or (7.11).

## 9. A coherent weighted obstruction across all radii

The separate conditions (5.5) could in principle be witnessed by
different rotor forests.  A real EP cover supplies one forest, so one can
sum the radius requirements coherently.

Define the directed hierarchical rotor graph \(\mathcal R(\mathcal D)\)
on positive-tag chains as follows.  For chains \(C,C'\) with tags \(d,d'\),
put

\[
 \rho(C,C')=\min(d,d').
 \tag{9.1}
\]

There is an arc \(C\to C'\) if \(\rho(C,C')\ge1\) and
\(\tau_{\rho(C,C')}C\to\tau_{\rho(C,C')}C'\) is a rotor arc.  Give it
weight \(\rho(C,C')\).  A rotor at radius \(r\) truncates to a rotor at
every positive radius \(1\le q\le r\), by the same direct calculation as
(4.11)--(4.13); the radius-zero boundary is the Johnson convention
(4.21)--(4.22).

Let \(\Lambda_{\rm lin}(\mathcal D)\) be the maximum total weight of a
directed vertex-disjoint linear forest in \(\mathcal R(\mathcal D)\).

### Theorem 9.1 (simultaneous weighted-radius obstruction)

Every full bridge-one path cover with \(p\) paths satisfies

\[
 \boxed{
 \Lambda_{\rm lin}(\mathcal D)
 \ge\sum_{q=1}^H(2N_q-W-p)_+.
 }
 \tag{9.2}
\]

#### Proof

Let \(e_q\) be the number of cover arcs whose two endpoint chains both
have tag at least \(q\).  The deletion/run argument gives

\[
 e_q\ge(2N_q-W-p)_+.
 \tag{9.3}
\]

The positive-tag arcs of the full path cover form one directed linear
forest in \(\mathcal R(\mathcal D)\) by Theorem 4.2.  An arc between tags
\(d,d'\) is counted in \(e_q\) exactly for
\(q=1,\ldots,\min(d,d')\).  Therefore its hierarchical weight is exactly
its total contribution to \(\sum_qe_q\).  Hence the weight of this one
forest is

\[
 \sum_{q=1}^He_q
 \ge\sum_{q=1}^H(2N_q-W-p)_+,
\]

proving (9.2).
\(\square\)

For \(H=\lceil A\sqrt m\rceil\), equations (6.1)--(6.2) and a Riemann
sum give

\[
 \sum_{q=1}^H(2N_q-W)_+
 =\bigl(\Phi_A+o_A(1)\bigr)W\sqrt m,
 \tag{9.4}
\]

where

\[
 \Phi_A
 =\int_0^{\min(A,\sqrt{\log2})}(2e^{-t^2}-1)\,dt>0.
 \tag{9.5}
\]

Since \((x-p)_+\ge x_+-p\) and \(Hp=o_A(W)\) under EP, (9.2) yields

\[
 \boxed{
 \Lambda_{\rm lin}(\mathcal D)
 \ge\bigl(\Phi_A+o_A(1)\bigr)W\sqrt m.
 }
 \tag{9.6}
\]

Every edge has weight at most \(H=(A+o(1))\sqrt m\).  Consequently the
same hierarchical forest has at least

\[
 \boxed{
 \left(\frac{\Phi_A}{A}+o_A(1)\right)W
 }
 \tag{9.7}
\]

edges.  This is a positive-density coherent multiradius requirement for
every fixed \(A>0\).

There is also an exact weighted Hall dual.  For a total order \(\prec\),
let \(K_\prec(\mathcal D)\) be the split bipartite graph of forward
hierarchical rotor arcs, retaining the weights (9.1).  Its maximum-weight
matching value is

\[
 \Lambda_\prec
 =\min\left\{
 \sum_Cu_C+\sum_Cv_C:
 u_C+v_{C'}\ge\rho(C,C')
 \text{ on every forward arc }C\to C',\quad u,v\ge0
 \right\}.
 \tag{9.8}
\]

The bipartite system is totally dual integral, so integral weights admit
an integral optimum.  Moreover

\[
 \Lambda_{\rm lin}(\mathcal D)=\max_\prec\Lambda_\prec.
 \tag{9.9}
\]

Thus, if for every total order \(\prec\) there exist (possibly
\(\prec\)-dependent) feasible dual potentials of total cost below the
right side of (9.2), they give an exact ordered weighted-Hall obstruction.
Dropping the order gives a more restrictive but simpler certificate for
the same obstruction: one feasible dual on every hierarchical rotor arc
upper-bounds all possible ordered forests at once, although the resulting
numerical upper bound is generally weaker than an order-specific optimum.

## 10. The independent full-top fibre cut

Promotion preserves the full upper collar mask \(U_H\); a full rotor
changes it.  Every rank-\((m+H)\) mask \(U\) is the actual top endpoint
of exactly one tag-\(H\) chain, whose selected collar is forced.  Hence
every one of the \(N_H\) top fibres contains a selected anchor.

### Proposition 10.1 (full-rotor density)

If a full bridge path cover has \(p\) paths and \(r\) genuine full rotor
arcs, then

\[
 \boxed{p+r\ge N_H.}
 \tag{10.1}
\]

#### Proof

Delete the \(r\) full rotor arcs from the path forest.  The number of
components becomes exactly \(p+r\).  Every remaining nontrivial arc is a
promotion and therefore stays inside one top fibre.  Since the selected
vertices include an anchor in each of the \(N_H\) distinct fibres, the
remaining forest has at least \(N_H\) components.
\(\square\)

From (6.1),

\[
 \frac{N_H}{W}=e^{-A^2+O_A(m^{-1/2})}.
 \tag{10.2}
\]

Thus EP forces

\[
 \boxed{
 r\ge\bigl(e^{-A^2}-o_A(1)\bigr)W.
 }
 \tag{10.3}
\]

This cut is complementary to Theorem 9.1.  A late promotion at
\(j>H+q\) is a rotor after radius-\(q\) truncation, and may help satisfy
the shallow Hall cuts, but it preserves \(U_H\).  It cannot pay the
positive-density full-rotor requirement (10.3).

## 11. A sharp positive sufficient packet statement

The obstruction identifies what a positive recursive construction would
have to accomplish at every tag, not merely at tag \(H\).

Fix a power of two \(\ell\) with \(2H\le\ell\le m\).  We use here the
audited local packet theorem from
`ROTOR_MULTI_FRAME_PACKET_RESOLUTION_20260725.md`: a recursive
orientation-cube cycle supplies, for every tag \(d\le H\), a packet of
\(2\ell\) pairwise mask-disjoint radius-\(d\) chains whose canonical
radius-\(H\) collar lifts form one bridge-one rotor cycle.  This local
packet theorem is an input; the global packing assumed below is not.

### Proposition 11.1 (all-tag packet sufficiency)

Suppose one clipped SCD can be partitioned, except for \(r\) exceptional
chains, into such same-tag packets of \(2\ell\) chains, and choose the
canonical full collars on the packet chains.  Then the selected full
states have a bridge path cover with

\[
 \boxed{
 p\le\frac{W-r}{2\ell}+r.
 }
 \tag{11.1}
\]

Consequently, if \(\ell\asymp m\) and \(r=o_A(W/H)\), then
\(\mathrm{EP}_A\) holds.

#### Proof

Cut one edge in each packet rotor cycle and retain every other packet
edge.  Make each exceptional state a singleton.  There are
\((W-r)/(2\ell)\) packets, proving (11.1).  If \(\ell\asymp m\), the
packet term is \(O(W/m)=o(W/H)\).
\(\square\)

There is no tag-census congruence obstruction at the required
exceptional-set scale.  Taking the residue of every \(\gamma_d\) modulo
\(2\ell\) leaves at most

\[
 (H+1)(2\ell-1)=O(Hm)=o(W/H)
 \tag{11.2}
\]

chains.  What is unproved is the actual integral, multiframe,
mask-disjoint packet packing whose complement is an SCD.  Equation (11.2)
only removes divisibility as a possible excuse; it does not construct the
packing.

## 12. Audited correction: clipped BTK has rotor edges

The native-radius BTK theorem says that two distinct BTK chains, viewed at
their own common native radius, do not form a same-radius rotor edge.  It
does **not** survive arbitrary clipping, because the tag-\(H\) class of a
clipped SCD mixes chains of many native radii.

For every \(1\le H<m\), the principal BTK chain has the clipped state

\[
 \omega_0=
 (\{1,\ldots,m-H\};\
 m-H+1,\ldots,m+H;\
 \{m+H+1,\ldots,2m\}).
 \tag{12.1}
\]

Apply the full rotor with

\[
 x=m-H,\qquad y=2m.
 \tag{12.2}
\]

The successor is

\[
 \omega_1=
 (\{1,\ldots,m-H-1\}\cup\{2m\};\
 m-H,m-H+1,\ldots,m+H-1;\
 \{m+H,\ldots,2m-1\}).
 \tag{12.3}
\]

This is exactly the \(H\)-clipping of the BTK chain with fixed matched
pair \((2m-1,2m)\): coordinate \(2m\) is fixed in, coordinate
\(2m-1\) is fixed out, and the remaining coordinates form its free
principal chain.  Both (12.1) and (12.3) reach the two clipped boundary
ranks, so both are tag-\(H\) states.  They are distinct and form a genuine
rotor edge.

Already for \(m=2,H=1\), this reads

\[
 (\{1\};2,3;\{4\})
 \longrightarrow
 (\{4\};1,2;\{3\}).
 \tag{12.4}
\]

Therefore the assertion that the clipped BTK tag-\(H\) induced rotor graph
is empty, and the EP no-go deduced from that assertion, must be withdrawn.
No conclusion about the full multiscale Hall deficiencies of BTK follows
from this one edge; evaluating them remains open.

## 13. Final proved/conditional boundary

The following statements are proved in this report.

* The exact full-state bridge graph and its degree (2.4).
* The exact full selected-state ordered-Hall equality (3.3).
* Extension-independent SCD truncation and all-radius bridge rigidity
  (Theorem 4.2), including every slot boundary.
* The subset and simultaneous ordered-Hall cuts (5.3)--(5.12).
* The exact shallow and Gaussian quantitative requirements
  (6.5)--(6.7).
* The exact value of the necessary collar-port mismatch relaxation and
  its capacitated Hall dual (7.10)--(7.12).
* The collapse of ambient degree to only \(m-q\) possible shallow
  high-tag successors from a selected tag-at-least-\(q\) full state
  (8.1).
* The coherent weighted all-radius necessary obstruction (9.2)--(9.9).
* The independent full-top rotor-density cut (10.1)--(10.3).
* The all-tag packet sufficient condition (11.1).
* The explicit correction to the clipped-BTK assertion (12.1)--(12.4).

The following statements remain unproved.

1. Existence of an SCD for which the ordered deficiencies in (5.9) are
   \(o_A(W/H)\) simultaneously at all radii.
2. Existence of collar choices satisfying the full state-consistent Hall
   system (3.3), even when all separate port minima (7.10) are small.
3. An all-tag multiframe recursive-packet packing with
   \(o_A(W/H)\) exceptional chains and an SCD-completable mask leave.

Thus the ambient bridge degree and exact SCD radius census do not prove
\(\mathrm{EP}_A\).  The sharp current obstruction is the ordered,
state-consistent Hall system (3.3), with the new selector-independent
multiscale cuts (5.9), collar-capacity cuts (7.11), coherent weighted cut
(9.2), and full-top cut (10.1) as mandatory projections.
