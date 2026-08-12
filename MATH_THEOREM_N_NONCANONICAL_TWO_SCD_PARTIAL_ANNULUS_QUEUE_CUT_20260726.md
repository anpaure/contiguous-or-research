# Noncanonical and two-SCD schedules for the corrected partial annulus:
# exact selector flow, queue stationarity, and universal path-cover cuts

Date: 2026-07-26

Method: pure mathematics only. No computation, search, solver, or web
input is used.

## 0. Outcome

Put

\[
 n=2m,\qquad W=\binom{2m}{m},\qquad
 N_q=\binom{2m}{m-q},
\]

and fix

\[
 q_0=\lceil a\sqrt m\rceil,\qquad
 H=\lfloor b\sqrt m\rfloor,\qquad 0<a<b.
\]

Write \(N=N_{q_0}\). The corrected partial-annulus ledger needs only
these \(N\) middle occurrences to be bundled. The other \(W-N\) middle
masks may be written once each as singleton letters. Thus an owner-simple
exact-provider family with a bridge-one path cover having \(p\) paths
gives

\[
 \boxed{L\le W+2Hp.}                                          \tag{0.1}
\]

This note formulates the noncanonical/two-SCD selection and chronology
problem exactly and proves universal cuts which survive the full
\(q_0!^2\) ordering freedom at the unprescribed depths below \(q_0\).

For a selected state with owner \(X\), put

\[
 A_X=X\setminus L_{q_0}(X),\qquad
 B_X=U_{q_0}(X)\setminus X.
\]

Both are \(q_0\)-sets. Along every owner-simple exact bridge-one path,
the queue--cache dynamics force

\[
 \boxed{B_{X_{i+q_0}}=A_{X_i}}                                \tag{0.2}
\]

away from the first and last \(q_0\) vertices. Hence, if \(a_C,b_C\)
are the two block histograms,

\[
 \boxed{
 p\ge \frac1{2q_0}
 \sum_{C\in\binom{[2m]}{q_0}}|a_C-b_C|.}                     \tag{0.3}
\]

If \(M_x\) is the number of selected middle occurrences containing
coordinate \(x\), exact lower and upper entrance coverage gives

\[
 \boxed{
 p\ge \frac1{2q_0^2}
 \sum_{x=1}^{2m}|2M_x-N|.}                                   \tag{0.4}
\]

The fixed lower tails give another refinement-independent cut. Define

\[
 \kappa_{\rm out}(X)
 =(\alpha_{q_0+2}(X),\ldots,\alpha_H(X)),
\]

\[
 \kappa_{\rm in}(X)
 =(\alpha_{q_0+1}(X),\ldots,\alpha_{H-1}(X)).
\]

If \(O_\kappa,I_\kappa\) are their histograms, then

\[
 \boxed{
 p\ge \frac12\sum_\kappa|O_\kappa-I_\kappa|.}                 \tag{0.5}
\]

For two SCDs, the provider and owner choice is itself an exact directed
cut on the rank-\((m-q_0)\) layer. Every designated signed target hole
and every repeated middle owner is one directed \(1\to0\) cut arc.

The cuts are universal in the corrected exact-provider, owner-simple
bridge-one model. Robust forms below charge middle-owner collision
excess before applying them. They do not yet give a positive lower bound
after optimizing over all SCD pairs: a complement-balanced owner support
can make (0.4) vanish, and short-chain extensions can alter some tail
contexts. No construction with \(p=o(W/H)\) is proved.

## 1. The corrected partial compiler ledger

For any SCD \(\mathscr D\) of \(B_{2m}\), the chains of radius at least
\(q_0\) are indexed by their rank-\((m-q_0)\) members. Hence

\[
 |\mathscr D_{\ge q_0}|=N.                                   \tag{1.1}
\]

Their middle members are distinct. For every \(q_0\le q\le H\), the
chains of radius at least \(q\) meet each of ranks \(m-q\) and \(m+q\)
exactly once. Thus their native flags give exact signed provider
bijections at every controlled depth. Chains shorter than \(H\) may be
extended arbitrarily; their extra flags can add witnesses but cannot
remove the native ones.

### Proposition 1.1 (literal partial compiler)

Suppose \(N\) selected useful-state occurrences have \(D\) distinct
middle owners, their selected bridge-one graph has a path cover with
\(p\) paths, and their actual signed hole counts are \(h_q^-,h_q^+\).
Then

\[
 \boxed{
 L\le W+2Hp+(N-D)
 +\sum_{q=q_0}^{H}(h_q^-+h_q^+).}                            \tag{1.2}
\]

#### Proof

A path containing \(s\) useful states has a hard-started realization of
length \(s+2H\). All paths cost \(N+2Hp\). Append every middle owner not
already represented, costing \(W-D\), and append every remaining signed
annular target once. This proves (1.2). \(\square\)

There is no additional charge for the \(W-N\) unbundled middle masks:
they are already among the \(W-D\) singleton completions.

## 2. Exact two-SCD selection as a directed cut

Let \(\mathscr D_0,\mathscr D_1\) be arbitrary SCDs and put

\[
 \mathcal R=\binom{[2m]}{m-q_0}.
\]

For \(T\in\mathcal R\), let \(C_c(T)\) be the unique chain of
\(\mathscr D_c\) containing \(T\). A selector

\[
 z:\mathcal R\to\{0,1\}                                      \tag{2.1}
\]

chooses \(C_{z(T)}(T)\). Thus exactly \(N\) occurrences are selected and
rank \(m-q_0\) is covered exactly once.

For a lower target \(S\) of rank \(m-q\), let
\(r^-_{c,q}(S)\in\mathcal R\) be the rank-\((m-q_0)\) member of the
\(\mathscr D_c\)-chain through \(S\). For an upper target \(U\) of rank
\(m+q\), define \(r^+_{c,q}(U)\) analogously.

### Theorem 2.1 (directed selector ledger)

The designated selected-provider load of a signed target \(S\) is

\[
 (1-z(r^\sigma_{0,q}(S)))+z(r^\sigma_{1,q}(S)),
 \qquad \sigma\in\{-,+\}.                                    \tag{2.2}
\]

It is missed exactly when

\[
 z(r^\sigma_{0,q}(S))=1,\qquad
 z(r^\sigma_{1,q}(S))=0.                                    \tag{2.3}
\]

If a middle owner \(X\) lies on radius-at-least-\(q_0\) chains in both
SCDs, let \(\mu_c(X)\in\mathcal R\) be the entrance member of that
chain. The owner is selected twice exactly when

\[
 z(\mu_1(X))=1,\qquad z(\mu_0(X))=0.                         \tag{2.4}
\]

Form a directed multigraph \(\Gamma\) on \(\mathcal R\) by putting

\[
 r^\sigma_{0,q}(S)\longrightarrow r^\sigma_{1,q}(S)          \tag{2.5}
\]

for every signed target and \(q_0\le q\le H\), and putting the reversed
owner arc

\[
 \mu_1(X)\longrightarrow\mu_0(X)                             \tag{2.6}
\]

for every owner long in both decompositions. If
\(Z=\{T:z(T)=1\}\), then, with multiplicity,

\[
 \boxed{
 |\delta_\Gamma^+(Z)|
 =C_{\rm mid}(z)+
 \sum_{q=q_0}^{H}(h_q^-(z)+h_q^+(z)).}                       \tag{2.7}
\]

Here the holes refer to designated native providers. Extension flags can
only improve the actual physical support.

#### Proof

The \(\mathscr D_0\)-provider of a target is selected precisely when its
root has selector value zero; the \(\mathscr D_1\)-provider is selected
precisely when its root has value one. This gives (2.2), whose only zero
pattern is (2.3).

Within one SCD, different entrance roots have different middle owners.
Thus a repeated owner consists exactly of its selected chain from each
SCD, which is pattern (2.4). Equations (2.3)--(2.4) identify every error
with one directed \(1\to0\) crossing. \(\square\)

### Corollary 2.2 (exact-provider component form)

Requiring every designated signed target to have load exactly one is
equivalent to

\[
 z(r^\sigma_{0,q}(S))=z(r^\sigma_{1,q}(S))                   \tag{2.8}
\]

for every \(q,S,\sigma\). Thus \(z\) is constant on every component of
the undirected target-pair graph. Owner simplicity adds

\[
 z(\mu_1(X))\le z(\mu_0(X)).                                 \tag{2.9}
\]

After contracting target components, feasible mixed choices are exactly
the forward-closed \(0/1\) sets of this implication preorder. Both
constant selectors remain feasible and recover the two pure SCD
scaffolds. Provider equations alone therefore give no universal
two-SCD obstruction.

The target part of \(\Gamma\) has

\[
 2\sum_{q=q_0}^{H}N_q
 =\left(2\int_a^b e^{-x^2}\,dx+o(1)\right)W\sqrt m            \tag{2.10}
\]

arcs. The corrected weak gate asks for directed boundary \(o(W)\), not
merely small constant conductance in this layered graph.

## 3. The full \(q_0\)-memory state

Fix a selected occurrence with owner \(X\), lower targets \(L_q(X)\),
and upper targets \(U_q(X)\) for \(q_0\le q\le H\). Put

\[
 A_X=X\setminus L_{q_0}(X),\qquad
 B_X=U_{q_0}(X)\setminus X.                                  \tag{3.1}
\]

For \(q_0<d\le H\), let

\[
 \alpha_d(X)=L_{d-1}(X)\setminus L_d(X),\qquad
 \beta_d(X)=U_d(X)\setminus U_{d-1}(X).                      \tag{3.2}
\]

Choose arbitrary orderings

\[
 (\alpha_1(X),\ldots,\alpha_{q_0}(X))
 \quad\text{of }A_X,                                         \tag{3.3}
\]

\[
 (\beta_1(X),\ldots,\beta_{q_0}(X))
 \quad\text{of }B_X.                                         \tag{3.4}
\]

Thus every isolated partial state has \(q_0!^2\) entrance refinements,
in addition to any extension choices beyond its native tag. Write

\[
 \boldsymbol\alpha_X=(\alpha_1,\ldots,\alpha_H),\qquad
 \boldsymbol\beta_X=(\beta_1,\ldots,\beta_H).                 \tag{3.5}
\]

The full useful ordered partition is

\[
 \omega_X=
 \bigl(
 L_H(X);\alpha_H,\ldots,\alpha_1,
 \beta_1,\ldots,\beta_H;
 [2m]\setminus U_H(X)
 \bigr).                                                      \tag{3.6}
\]

It exposes all prescribed partial flags. The \(q_0!^2\) freedom is real
for an isolated state, but it is not fresh at each internal path vertex.

## 4. Exact bridge-one queue--cache dynamics

### Lemma 4.1 (queue--cache normal form)

Let \(X\ne Y\), with

\[
 Y=X-a+b,\qquad a\in X,\quad b\notin X.                      \tag{4.1}
\]

There is an owner-changing bridge-one arc
\(\omega_X\to\omega_Y\) if and only if:

\[
 a=\alpha_1(X),                                               \tag{4.2}
\]

for some \(x\in L_H(X)\),

\[
 \boldsymbol\alpha_Y
 =(\alpha_2(X),\ldots,\alpha_H(X),x),                         \tag{4.3}
\]

and, on putting

\[
 e=
 \begin{cases}
  b,&b\in\{\beta_1(X),\ldots,\beta_H(X)\},\\
  \beta_H(X),&b\notin\{\beta_1(X),\ldots,\beta_H(X)\},
 \end{cases}                                                  \tag{4.4}
\]

one has

\[
 \boldsymbol\beta_Y
 =\bigl(\alpha_1(X),
  (\beta_1(X),\ldots,\beta_H(X))\setminus e\bigr),             \tag{4.5}
\]

with the unaffected cache entries retaining their order.

The first case of (4.4) is a promotion; the second is a genuine rotor.

#### Proof

In (3.6), the middle boundary occurs after the lower residual and the
\(H\) lower singleton blocks. An owner-changing update must move the
last lower singleton \(\alpha_1(X)\) across this boundary, proving
(4.2). The other \(H-1\) lower singletons retain their order, while the
new last singleton comes from \(L_H(X)\), giving (4.3).

The departed coordinate becomes the first absent coordinate and hence
the first cache block. If the arrival \(b\) was already cached, it is
removed from the cache. Otherwise the oldest cache entry \(\beta_H(X)\)
falls into the upper residual. This gives (4.4)--(4.5). Conversely the
displayed block identities are exactly the ordered partition produced
by the corresponding bridge-one update. \(\square\)

For completeness, the forced residual updates are

\[
 L_H(Y)=L_H(X)-x+b,
\]

and

\[
 [2m]\setminus U_H(Y)=
 \begin{cases}
  [2m]\setminus U_H(X),&b\text{ was cached},\\
  ([2m]\setminus U_H(X))-b+\beta_H(X),&b\text{ was residual}.
 \end{cases}
\]

These identities also give a direct check of the converse in Lemma 4.1.

The upper word is a cache, not a second symmetric FIFO.

### Lemma 4.2 (early promotions are excluded)

Assume the selected upper depth-\(q_0\) targets are pairwise distinct. In
every selected owner-changing bridge, either the bridge is a rotor or a
promotion removes \(\beta_j(X)\) with

\[
 \boxed{j>q_0.}                                               \tag{4.6}
\]

#### Proof

If \(b=\beta_j(X)\) with \(j\le q_0\), (4.5) gives

\[
 B_Y=\{a\}\cup(B_X\setminus\{b\}).
\]

Together with \(Y=X-a+b\), this yields

\[
 U_{q_0}(Y)=Y\cup B_Y=X\cup B_X=U_{q_0}(X),                  \tag{4.7}
\]

contradicting upper entrance injectivity. \(\square\)

The argument is independent of a common SCD and applies to cross-SCD
arcs. If upper entrance repeats are allowed, each early promotion lies
inside a repeated upper-target fibre. A path forest contains at most the
upper entrance repeat excess many such arcs.

## 5. The corrected residence staircase

Let

\[
 \omega_{X_0}\longrightarrow\omega_{X_1}\longrightarrow
 \cdots\longrightarrow\omega_{X_{s-1}}                       \tag{5.1}
\]

be one path in an owner-simple selected family. Write

\[
 d_i=\alpha_1(X_i)=X_i\setminus X_{i+1}                       \tag{5.2}
\]

when the edge exists. Iterating (4.3) gives

\[
 \alpha_j(X_i)=d_{i+j-1}                                     \tag{5.3}
\]

whenever the required \(j\) subsequent edges exist. Hence

\[
 A_{X_i}=\{d_i,d_{i+1},\ldots,d_{i+q_0-1}\}.                 \tag{5.4}
\]

By Lemma 4.2, the first \(q_0\) cache entries update as

\[
 (\beta_1,\ldots,\beta_{q_0})(X_{i+1})
 =(d_i,\beta_1(X_i),\ldots,\beta_{q_0-1}(X_i)).               \tag{5.5}
\]

After \(q_0\) steps,

\[
 \boxed{
 B_{X_{i+q_0}}
 =\{d_i,d_{i+1},\ldots,d_{i+q_0-1}\}
 =A_{X_i}.}                                                   \tag{5.6}
\]

Thus the first \(q_0\) deletion labels are freely orderable only at a
path start. At an internal vertex they are the next \(q_0\) departures;
the first \(q_0\) cache labels are the preceding \(q_0\) departures in
reverse order.

## 6. Universal entrance-block and point-margin cuts

For \(C\in\binom{[2m]}{q_0}\), put

\[
 a_C=|\{X:A_X=C\}|,\qquad b_C=|\{X:B_X=C\}|.                  \tag{6.1}
\]

### Theorem 6.1 (entrance-block total variation)

Every owner-simple, exact-entrance bridge-one path cover satisfies

\[
 \boxed{
 \frac12\sum_C|a_C-b_C|\le q_0p.}                             \tag{6.2}
\]

Equivalently, for every
\(\mathcal C\subseteq\binom{[2m]}{q_0}\),

\[
 \sum_{C\in\mathcal C}(a_C-b_C)\le q_0p.                     \tag{6.3}
\]

#### Proof

A path of \(s\) vertices supplies \((s-q_0)_+\) pairings (5.6).
After canceling them, at most \(\min\{q_0,s\}\) blocks remain on each
side. Their signed histogram has \(\ell^1\)-norm at most twice that
number. Sum over paths. Since the total signed mass is zero, its largest
cut is one half of its \(\ell^1\)-norm. \(\square\)

For a family with middle collision excess \(C_{\rm mid}\), delete all
forest arcs lying inside one owner fibre. There are at most
\(C_{\rm mid}\) such arcs. If \(e_{\rm early}\) early promotions remain,
each spoils at most \(q_0\) pairings. Thus

\[
 \boxed{
 \frac12\sum_C|a_C-b_C|
 \le q_0(p+C_{\rm mid}+e_{\rm early}).}                       \tag{6.4}
\]

Here \(e_{\rm early}\) is at most the upper entrance repeat excess.

### Theorem 6.2 (point-margin cut)

Assume the selected lower and upper entrance targets are each bijections
onto their complete ranks and the selected owners are distinct. Let

\[
 M_x=|\{X:x\in X\}|.
\]

Then

\[
 \boxed{
 p\ge \frac1{2q_0^2}
 \sum_{x=1}^{2m}|2M_x-N|.}                                   \tag{6.5}
\]

#### Proof

Let \(A_x,B_x\) be the numbers of entrance blocks \(A_X,B_X\) containing
\(x\). Exact lower and upper entrance coverage gives

\[
 A_x=M_x-\binom{2m-1}{m-q_0-1},                              \tag{6.6}
\]

\[
 B_x=\binom{2m-1}{m+q_0-1}-M_x
 =\binom{2m-1}{m-q_0}-M_x.                                  \tag{6.7}
\]

Pascal's identity says

\[
 \binom{2m-1}{m-q_0-1}+
 \binom{2m-1}{m-q_0}=N,
\]

so

\[
 A_x-B_x=2M_x-N.                                             \tag{6.8}
\]

Writing \(f_C=a_C-b_C\),

\[
 2M_x-N=\sum_{C\ni x}f_C.
\]

Therefore

\[
 \sum_x|2M_x-N|
 \le q_0\sum_C|f_C|
 \le 2q_0^2p,
\]

by Theorem 6.1. \(\square\)

Without owner simplicity, deleting same-owner forest arcs gives

\[
 \boxed{
 p+C_{\rm mid}\ge
 \frac1{2q_0^2}\sum_{x=1}^{2m}|2M_x-N|.}                     \tag{6.9}
\]

At Gaussian scale, \(p=o(W/H)\) forces

\[
 \sum_C|a_C-b_C|=o(W),\qquad
 \sum_x|2M_x-N|=o(W\sqrt m).                                 \tag{6.10}
\]

## 7. Lower-tail de Bruijn and contextwise Hall cuts

For a chosen full refinement define

\[
 P_X=(\alpha_1(X),\ldots,\alpha_{H-1}(X)),\qquad
 S_X=(\alpha_2(X),\ldots,\alpha_H(X)).                       \tag{7.1}
\]

Every owner-changing bridge obeys \(S_X=P_Y\). Let

\[
 O_w=|\{X:S_X=w\}|,\qquad I_w=|\{X:P_X=w\}|.
\]

### Theorem 7.1 (full-context cut)

Every owner-simple path cover satisfies

\[
 \boxed{
 p\ge \frac12\sum_w|O_w-I_w|.}                               \tag{7.2}
\]

#### Proof

At most \(\sum_w\min\{O_w,I_w\}\) path edges can be selected. A forest
with \(N\) vertices and \(p\) paths has \(N-p\) edges, while

\[
 \sum_w\min\{O_w,I_w\}
 =N-\frac12\sum_w|O_w-I_w|.
\]

Rearrange. \(\square\)

Projecting away the freely ordered first \(q_0\) entries gives the
contexts from (0.5). Their equality is still necessary on every bridge.

### Corollary 7.2 (refinement-independent tail cut)

For every owner-simple selected family and every choice of entrance
permutations,

\[
 \boxed{
 p\ge\Delta_{\rm tail}:=
 \frac12\sum_\kappa|O_\kappa-I_\kappa|.}                     \tag{7.3}
\]

For a family with collision excess \(C_{\rm mid}\), the robust versions
of (7.2)--(7.3) hold with \(p\) replaced by \(p+C_{\rm mid}\).

#### Proof

Equation (4.3) gives

\[
 \kappa_{\rm out}(X)=\kappa_{\rm in}(Y)
\]

on each owner-changing bridge. Apply the same matching count after
deleting same-owner forest arcs if necessary. \(\square\)

This is literally a Hall cut. Every neighbor of the source family with
\(\kappa_{\rm out}\in\mathcal K\) lies in the target family with
\(\kappa_{\rm in}\in\mathcal K\).

There is also an exact local decomposition. Fix an owner-simple selected
family, all refinements, and a total order \(\prec\). For each full
context \(w\), put

\[
 \mathcal L_w=\{X:S_X=w\},\qquad
 \mathcal R_w=\{Y:P_Y=w\},
\]

and let \(G_w\) have shores \(\mathcal L_w,\mathcal R_w\) and the legal
forward bridge-one arcs \(X\to Y\). Then the minimum forward path count
for these fixed choices is

\[
 \boxed{
 p_{\min}=\sum_w\bigl(O_w-\nu(G_w)\bigr)
 =\sum_w\max_{\mathcal A\subseteq\mathcal L_w}
 \bigl(|\mathcal A|-|N_{G_w}(\mathcal A)|\bigr).}             \tag{7.4}
\]

Indeed the global bipartite graph is the disjoint union of these context
graphs, and \(\prec\) excludes directed cycles.

### Short-chain extension caveat

The entrance cuts use no extension choices. The tail cut is universal
after extensions are chosen, but those choices can change its histogram.

Fix \(q_0+2\le s\le H\). Under exact provider balance and owner
simplicity, exactly \(N_s\) selected chains have native tag at least
\(s\). On them form native out/in keys

\[
 (\alpha_{q_0+2},\ldots,\alpha_s),\qquad
 (\alpha_{q_0+1},\ldots,\alpha_{s-1}),
\]

with histograms \(O_s^{\rm nat},I_s^{\rm nat}\). The other \(N-N_s\)
states can reduce an \(\ell^1\)-difference by at most two each. Hence

\[
 \boxed{
 p\ge\frac12
 \left(
 \|O_s^{\rm nat}-I_s^{\rm nat}\|_1-2(N-N_s)
 \right)_+.}                                                 \tag{7.5}
\]

## 8. Exact lifted path-cover program and recourse

For every \(c,T\), expand \(C_c(T)\) into all useful states obtained by
choosing:

1. an ordering of its lower entrance block;
2. an ordering of its upper entrance block; and
3. every required extension from its native tag to \(H\).

Choose one color and one lift over every \(T\in\mathcal R\), subject to
the desired provider and owner equations. Fix a total order \(\prec\).
Put an edge \(v_Lw_R\) exactly when \(v\prec w\) and Lemma 4.1 holds.
Write \(\eta\) for this complete lift/refinement assignment.

### Theorem 8.1 (ordered-Hall formulation)

For fixed choices, the minimum number of forward bridge-one paths is

\[
 \boxed{
 p=\max_{\mathcal A}
 \bigl(|\mathcal A|-|N(\mathcal A)|\bigr).}                  \tag{8.1}
\]

Optimizing gives

\[
 \boxed{
 p_*=\min_{z,\eta,\prec}
 \max_{\mathcal A}
 \bigl(|\mathcal A|-|N_{G_{z,\eta,\prec}}(\mathcal A)|\bigr),} \tag{8.2}
\]

with the minimum restricted to owner-simple exact-provider selections
for the strong gate.

#### Proof

A matching of size \(r\) gives an acyclic linear forest with \(N-r\)
paths. Conversely every path forest has a topological order and gives
such a matching. Hall's deficiency theorem completes the proof.
\(\square\)

The same lift must support both the incoming and outgoing arc of an
internal state. Projecting to existential base-state adjacency loses this
recourse constraint. For instance, with \(q_0=2\), one proposed incident
edge may force the order \((p,q)\) of a block \(\{p,q\}\), while the
other forces \((q,p)\). Both projected adjacencies exist, but no single
lift realizes their composition.

For weak selections, the certified sufficient objective is

\[
 \boxed{
 2Hp+C_{\rm mid}+
 \sum_{q=q_0}^{H}(h_q^-+h_q^+).}                             \tag{8.3}
\]

The holes here are designated-provider holes. This is not asserted to
equal the unrestricted physical optimum when same-owner bridges or
accidental extension witnesses are allowed. Proving (8.3) is \(o(W)\)
would nevertheless finish the fixed annulus.

## 9. Inherited all-depth run cuts

Let \(V_q\) be the selected chains whose native tag is at least \(q\).
In the exact one-provider, owner-simple model,

\[
 |V_q|=N_q.                                                   \tag{9.1}
\]

On a union of \(p\) paths, the number of \(V_q\)--\(V_q\) arcs is at
least

\[
 2N_q-N-p.                                                    \tag{9.2}
\]

Indeed the marked vertices form at most \(N-N_q+p\) nonempty runs.
Every such arc centrally truncates to a genuine radius-\(q\) rotor: a
promotion remaining a promotion after truncation would preserve the
upper depth-\(q\) target, contradicting exact provider injectivity.

If \(\Lambda_q\) is the maximum protected linear-forest size on \(V_q\),
then

\[
 \boxed{
 p\ge(2N_q-N-\Lambda_q)_+.}                                  \tag{9.3}
\]

At \(q=H\), \(\Lambda_H\) is genuine full-radius rotor capacity. Thus
\(p=o(W/H)\) requires

\[
 \Lambda_H\ge
 \bigl(2e^{-b^2}-e^{-a^2}-o(1)\bigr)W.                       \tag{9.4}
\]

The coefficient is positive exactly when

\[
 b^2-a^2<\log2.                                               \tag{9.5}
\]

For a weak provider histogram with \(h_q\) holes and duplicate excess
\(c_q\), one has \(|V_q|=N_q-h_q+c_q\). At most \(c_q\) internal arcs
can remain inside repeated upper-target fibres. Delete also at most
\(C_{\rm mid}\) same-owner forest arcs. The number \(R_q\) of protected
owner-changing arcs therefore obeys

\[
 \boxed{
 R_q\ge
 \bigl(2N_q-N-p-2h_q+c_q-C_{\rm mid}\bigr)_+.}                \tag{9.6}
\]

These run cuts are necessary but not universally contradictory. In the
complete compatibility relaxation, ordering states by nonincreasing tag
makes every \(V_q\) one interval and satisfies all height-only demands.
A fatal theorem must bound actual lifted compatibility, not only radii.

## 10. Why the collapsed-port shortcut is invalid

Collapsing the \(q_0\) unprescribed deletions into one set-valued letter
makes all members of \(A_X\) appear to have one port and suggests a
linear spacing obstruction. That restriction is absent here.

A legal conveyor has

\[
 \alpha_i(X_t)=d_{t+i-1},\qquad
 \alpha_i(X_{t+1})=\alpha_{i+1}(X_t).
\]

The \(q_0\) entrance coordinates occupy distinct queue depths and move
one level per update. They are not simultaneous same-port demands.
Therefore the GMM depth-\((1,2)\) defect and collapsed-first-block
spacing counts cannot be promoted to universal obstructions for the
corrected partial model.

## 11. Proved and conditional boundary

Proved:

1. the corrected \(N_{q_0}\)-occurrence compiler ledger;
2. the exact two-SCD directed selector identity (2.7);
3. the full \(q_0!^2\) entrance freedom and exact queue--cache bridge;
4. exclusion of early promotions under exact upper entrance injectivity;
5. the residence identity \(B_{i+q_0}=A_i\);
6. the entrance-block cut with exact factor \(q_0\);
7. the point-margin cut with exact factor \(2q_0^2\);
8. the context Hall cuts and extension caveat;
9. the exact lifted ordered-Hall program and recourse trap; and
10. the all-depth protected-run hierarchy.

The decisive constants were audited independently:

* one path of \(s\) states leaves
  \(\min\{q_0,s\}\) unmatched blocks on each side;
* projecting a \(q_0\)-block histogram to point incidences costs exactly
  \(q_0\);
* an early promotion preserves \(U_{q_0}\), while a late promotion leaves
  the first-\(q_0\) FIFO update intact; and
* the context imbalance is half the \(\ell^1\)-distance because both
  histograms have mass \(N\).

Not proved:

1. a noncanonical or two-SCD lift with \(p=o(W/H)\);
2. a universal positive lower bound on the block or tail discrepancies
   after optimizing all SCD and extension choices;
3. the positive-density top rotor forest required in the narrow annulus;
   or
4. coefficient one.

The surviving finite integral theorem is now precise: choose a
two-SCD directed-cut selector with \(o(W)\) provider/owner boundary,
choose one common queue lift at every selected root, and solve the
contextwise Hall system so that

\[
 2Hp+C_{\rm mid}+
 \sum_{q=q_0}^{H}(h_q^-+h_q^+)=o(W).
\]

The cuts (6.2), (6.5), (7.3), and (9.3) are mandatory for every such
owner-simple exact construction. They are the theorem-level advance of
this lane; the final path-cover existence remains open.
