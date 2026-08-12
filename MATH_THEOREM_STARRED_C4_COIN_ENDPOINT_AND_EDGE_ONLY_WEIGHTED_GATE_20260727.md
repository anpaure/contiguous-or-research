# Starred \(C_4\), resource coins, and the edge-only weighted gate

Date: 2026-07-27

Scope: coefficient-one repaired-ring owner packing.

### Catalogue convention

Let \(H=(1+o(1))\sqrt{m\log m}\), put \(M=m+H\), and delete a
cyclic block of \(1\le \kappa=o(m)\) phases from each promotion ring.
Write

\[
 r=M-\kappa,\qquad K=r+1,\qquad
 \mu_\kappa=2((\kappa-H+1)_+)!.
\]

We work in the simple physical repaired-ring catalogue: an edge has one
rank-\(m-H\) root and \(r\) middle owners. Its middle-owner degree is

\[
 D_X={r(m!)^2\over (m-H)!\mu_\kappa}.
\tag{0.0}
\]

We use the already proved full-catalogue width-two estimate

\[
 \max_{e\not\ni X}
 |\{f:X\in f,\ f\cap e\ne\varnothing\}|
 \le (20+o(1)){D_X\over m^2}.
\tag{0.1}
\]

and the audited pair/root degree estimates

\[
 \max_{Y\ne X}{d(X,Y)\over D_X}
 \le {2+o(1)\over m^2},\qquad
 D_{\rm root}=(1+o(1))D_X.
\tag{0.2}
\]

All subcatalogues below consist of literal physical repaired edges; no
parallel representations or abstract incidence copies are introduced.

## 0. Verdict

The first edge-column tree theorem is correct, but it does not close
drift coherence.

There are three conclusions.

1. The positive edge \(C_4\) is starred:

   \[
   \sum_g\sum_{e:e\cap g=\varnothing}
       a(e)^{h-2}b(e,g)^2.
   \]

   Likewise the positive coin \(C_4\) has \(y\notin e\). Hence the
   same-resource \(K_{2,\Delta}\) obstruction asserted in
   MATH_THEOREM_COMPENSATION_COLUMN_C4_DRIFT_AND_SHARP_REPAIRED_RING_OBSTRUCTION_20260727.md
   is invalid: its events kill the protected index and are favorable.

2. Nevertheless, a legal separated-endpoint obstruction exists.
   A literal repaired-ring subcatalogue satisfies the stopped
   one-column influence

   \[
        \max_e a_X(e)/d_X=O(J^2/m^2)
   \]

   but its injective starred \(C_4\) energy is larger by
   \(\Omega(m/J^2)\) than the self-normalized estimate needed to infer
   drift coherence from that stopping condition alone. Thus the
   time-zero two-column mesh gives the extra \(m^{-2}\) only when its
   dynamic relative normalization is separately regenerated.

3. Compensation requires a separate stopped resource-column endpoint.
   The edge influence cap \(a(e)\le A\) does not imply it. An
   uncompensated edge-only process removes the explicit coin summand and
   preserves the exact two-density owner ledger. Exact balanced edge
   weights exist precisely under the joint Hall/Farkas inequality in
   Section 5. That inequality is not known hereditarily, and edge-only
   weighting does not remove the legal starred \(C_4\).

Consequently the owner near-packing is still conditional. The exact
surviving choices are:

* dynamically regenerate the starred \(C_4\) and resource endpoint
  incidence-weightedly; or
* prove the capped joint Hall inequality for diffuse edge-only weights,
  together with the weighted starred edge-column hierarchy.

## 1. Exact positive generator diagrams

Every repaired edge contains one root and \(r\) owner resources; write
\(K=r+1\).  In the compensated process the edge-clock rate is
\(\nu=(r\Delta)^{-1}\) and every resource coin has rate at most
\(r^{-1}\).

Fix a live owner \(X\). Let

\[
 \mathcal F_X=\{f:X\in f\},\qquad
 \mathcal R_X=\{e:X\notin e\},
\]

and put

\[
\begin{aligned}
 d_X&=|\mathcal F_X|,\\
 a(e)&=|\{f\in\mathcal F_X:f\cap e\ne\varnothing\}|,\\
 b(e,g)&=|\{f\in\mathcal F_X:
              f\cap e\ne\varnothing,\ f\cap g\ne\varnothing\}|.
\end{aligned}
\tag{1.1}
\]

For

\[
                         Y_h=\sum_{e\in\mathcal R_X}a(e)^h,
\tag{1.2}
\]

selection of \(g\) produces the exact decrement

\[
\begin{aligned}
 D_h^E(g)
 &=
 \sum_{\substack{e\in\mathcal R_X\\e\cap g\ne\varnothing}}a(e)^h\\
 &\quad+
 \sum_{\substack{e\in\mathcal R_X\\e\cap g=\varnothing}}
 \left[a(e)^h-(a(e)-b(e,g))^h\right].
\end{aligned}
\tag{1.3}
\]

If every eligible edge has clock rate \(\nu\), and
\(\mathsf K_X\le0\) denotes events killing the stopped center \(X\),
then the complete generator is

\[
 \boxed{
 \mathcal L Y_h
 =-\nu\sum_{g:X\notin g}D_h^E(g)
   +\mathcal L^\circ Y_h+\mathsf K_X.}
\tag{1.3a}
\]

The first sum is protected-index death. It is favorable in every upper
drift estimate. For \(h\ge2\), the first positive Taylor correction is
therefore

\[
 \boxed{
 \mathcal C_h^E(X)=
 \sum_{g\in\mathcal R_X}
 \sum_{\substack{e\in\mathcal R_X\\e\cap g=\varnothing}}
 a(e)^{h-2}b(e,g)^2.}
\tag{1.4}
\]

Indeed,

\[
 x^h-(x-z)^h
 \ge hx^{h-1}z-\binom h2x^{h-2}z^2
 \qquad(0\le z\le x).
\tag{1.4a}
\]

All diagrams in (1.4) have two distinct resource endpoints: if all four
incidences used one owner \(y\), then \(y\in e\cap g\), contrary to the
starred condition.

For compensation, let

\[
\begin{aligned}
 p(y)&=|\{f\in\mathcal F_X:y\in f\}|,\\
 c(e,y)&=|\{f\in\mathcal F_X:
                    f\cap e\ne\varnothing,\ y\in f\}|.
\end{aligned}
\tag{1.5}
\]

If \(y\ne X\) has coin rate \(\chi_y\), the exact noncentral coin
generator is

\[
\begin{aligned}
 \mathcal L^\circ Y_h
={}&-\sum_{y\ne X}\chi_y\sum_{e:y\in e}a(e)^h\\
 &+\sum_{\ell=1}^h(-1)^\ell\binom h\ell
 \sum_e\sum_{\substack{y\notin e\\y\ne X}}
 \chi_y a(e)^{h-\ell}c(e,y)^\ell.
\end{aligned}
\tag{1.6}
\]

Thus, for \(h\ge2\), the legal heterogeneous coin \(C_4\) is

\[
 \boxed{
 \mathcal C_h^\circ(X)=
 \sum_e\sum_{\substack{y\notin e\\y\ne X}}
 \chi_y a(e)^{h-2}c(e,y)^2.}
\tag{1.7}
\]

Coins at the center, or at a resource of the protected edge, are
terminal and favorable.

Equations (1.3) and (1.6) invalidate the retracted same-resource
construction recorded in the companion compensation-\(C_4\) draft.

### Exact equality and witness partitions

Expand \(b(e,g)^2\) using two displayed rows \(f_1,f_2\).
After applying the protected-index split in (1.3), the partitions are:

1. \(f_1=f_2\).  This is the row diagonal
   \(\sum_{e\perp g}a(e)^{h-2}b(e,g)\), a tree diagram.
2. \(e=g\), or more generally \(e\cap g\ne\varnothing\).  This is
   protected-index death, not a positive Taylor correction.
3. \(f_1\ne f_2\) and \(e\cap g=\varnothing\).  This is the only
   genuine starred \(C_4\).

For the third case, choose conflict witnesses

\[
 u_i\in f_i\cap e,\qquad v_i\in f_i\cap g.
\tag{1.8}
\]

The starred condition forces \(u_i\ne v_j\) for every \(i,j\).  Within
each column there are four witness partitions, according as

\[
 (u_1=u_2,\ v_1=v_2)\in
 \{(0,0),(1,0),(0,1),(1,1)\}.
\tag{1.9}
\]

The \((1,1)\) case is a legal double common-conflict diagram, but it
uses two distinct resources \(u\ne v\).  The illegal pattern is the
single-resource identification \(u=v\), because that puts the resource
in \(e\cap g\).

For the coin diagram, row collapse \(f_1=f_2\) is again a tree, and
\(y\in e\) is protected-index death.  In the genuine case
\(f_1\ne f_2,\ y\notin e\), choose \(u_i\in f_i\cap e\).  The two
witness partitions are \(u_1\ne u_2\) and \(u_1=u_2=u\).  The latter
is legal because its two common row resources are the distinct
endpoints \(y\ne u\).

This classification is exhaustive at the row/column equality level.
Multiple physical intersections may be expanded by exact
inclusion--exclusion over chosen witnesses; none of the later arguments
uses witness-level injectivity.

## 2. Correct compensation breadth and endpoint interpolation

All \(y\)-sums in this section range over noncentral coin-active
resources; in a stopped cluster they range only over its unprotected
resources.

The compensation tree theorem needs two separate stopped bounds:

\[
                         a(e)\le A,\qquad p(y)\le P.
\tag{2.1}
\]

The second does not follow from the first. Put

\[
 Q_h(y)=\sum_ea(e)^{h-1}c(e,y),
\qquad L=K\Delta,
\tag{2.2}
\]

where every path row has at most \(L\) edge columns and at most \(K\)
resource columns.

### Theorem 2.1 (two-colour tree breadth)

For every \(h,\ell\ge1\),

\[
 \boxed{
 \sum_yQ_h(y)^\ell
 \le
 d_XK L^\ell P^{\ell-1}A^{(h-1)\ell}.}
\tag{2.3}
\]

If \(\chi_y\le1/r\), then with

\[
                         y_h=d_XLA^{h-1}
\tag{2.4}
\]

one has

\[
 \boxed{
 \sum_y\chi_y\left({Q_h(y)\over y_h}\right)^\ell
 \le {K\over r}\left({P\over d_X}\right)^{\ell-1}.}
\tag{2.5}
\]

#### Proof

Expand the left side of (2.3). The diagram has one common resource
column \(y\), \(\ell\) edge columns, and \(h\ell\) path rows. It is a
tree. Root at one distinguished row. The common \(y\)-column costs at
most \(K\); its other \(\ell-1\) distinguished rows cost
\(P^{\ell-1}\); the edge columns cost \(L^\ell\); and their remaining
\((h-1)\ell\) rows cost \(A^{(h-1)\ell}\). This proves (2.3).
Multiplication by \(\max_y\chi_y\le1/r\) and division by \(y_h^\ell\)
give (2.5). \(\square\)

When the coin at \(y\) rings, protected indices \(e\ni y\) disappear
as well.  Put

\[
 S_h(y)=\sum_{e:y\in e}a(e)^h.
\tag{2.6}
\]

Then

\[
 S_h(y)\le\Delta A^h,\qquad
 \sum_yS_h(y)\le K Y_h\le K y_h.
\tag{2.7}
\]

Indeed, \(\sum_ea(e)\le d_XL\) by double counting row--edge
incidences, and hence
\(Y_h\le A^{h-1}\sum_ea(e)\le y_h\).

Maximum times first moment gives

\[
 \boxed{
 \sum_y\chi_y\left({S_h(y)\over y_h}\right)^\ell
 \le {K\over r}
 \left({A\over Kd_X}\right)^{\ell-1}.}
\tag{2.8}
\]

If \(D_h^\circ(y)\) is the complete coin decrement in (1.6), then

\[
 D_h^\circ(y)\le S_h(y)+hQ_h(y).
\tag{2.9}
\]

Combining (2.5), (2.8), and
\((u+v)^\ell\le2^{\ell-1}(u^\ell+v^\ell)\) yields the full
compensation-column jump estimate

\[
 \boxed{
 \sum_y\chi_y\left({D_h^\circ(y)\over y_h}\right)^\ell
 \le (2h)^\ell{K\over r}
 \left[
 \left({P\over d_X}\right)^{\ell-1}
 +
 \left({A\over Kd_X}\right)^{\ell-1}
 \right].}
\tag{2.10}
\]

Thus the compensation breadth and protected-index ledgers are complete
once the separate resource endpoint \(P\) is stopped.  No cyclic
diagram enters (2.10).

The implication \(p(y)\le A\) is valid only when the active \(y\)-star
contains an edge avoiding \(X\): such an edge sees every \(X,y\)-path.
If the whole \(y\)-star lies in the \(X\)-link, a separate pair-link
bound or weighted quarantine is necessary.

For a general stopped cluster \(C\), put
\(A_C=|\mathcal F_C|\) and

\[
 P_C(y)=|\{f\in\mathcal F_C:y\in f\}|,\qquad
 S_j^\circ(C)=\sum_y\chi_yP_C(y)^j.
\tag{2.11}
\]

Every option has at most \(r\) unprotected resources and
\(\chi_y\le1/r\), so

\[
                         S_1^\circ(C)\le A_C.
\tag{2.12}
\]

Let \(w_C\ge0\), \(\alpha\ge0\), and \(h\ge2\). Consequently the
endpoint condition

\[
 \sum_Cw_CS_h^\circ(C)
 \le\alpha^{h-1}\sum_Cw_CA_C^h
\tag{2.13}
\]

implies, for \(1\le\ell\le h\),

\[
 \sum_Cw_CA_C^{h-\ell}S_\ell^\circ(C)
 \le\alpha^{\ell-1}\sum_Cw_CA_C^h.
\tag{2.14}
\]

Indeed, put \(\theta=(\ell-1)/(h-1)\). Power-moment log-convexity for
the measure \(\sum_y\chi_y\delta_{P_C(y)}\) gives

\[
 S_\ell^\circ(C)
 \le \bigl(S_1^\circ(C)\bigr)^{1-\theta}
       \bigl(S_h^\circ(C)\bigr)^\theta
 \le A_C^{1-\theta}\bigl(S_h^\circ(C)\bigr)^\theta.
\]

Since
\(A_C^{h-\ell+1-\theta}=(A_C^h)^{1-\theta}\), Hölder over \(C\)
and (2.13) yield

\[
\begin{aligned}
 \sum_Cw_CA_C^{h-\ell}S_\ell^\circ(C)
 &\le
 \left(\sum_Cw_CA_C^h\right)^{1-\theta}
 \left(\sum_Cw_CS_h^\circ(C)\right)^\theta\\
 &\le
 \alpha^{(h-1)\theta}\sum_Cw_CA_C^h,
\end{aligned}
\]

which is (2.14). This is the exact resource-coin endpoint analogue.

## 3. A literal legal coin obstruction

### Theorem 3.1

For all sufficiently large \(m\), there is a literal repaired-ring
subcatalogue and a protected pair \((X;e)\) such that

\[
 d_X=2m^2,\qquad
 a_X(e)=c(e,y)=2={d_X\over m^2},
\tag{3.1}
\]

for an unprotected owner \(y\notin e\), while

\[
 \chi_y={1-O(m^{-2})\over r}.
\tag{3.2}
\]

Hence the off-diagonal part of the legal coin \(C_4\) is nonzero and

\[
 \chi_yc(e,y)^2=\Theta(A_C^2/m),
\tag{3.3}
\]

not \(O(m^{-2+o(1)}A_C^2)\).

#### Proof

Fix one root and cyclic frame, and take the complements of two deleted
\(\kappa\)-blocks whose retained \(r\)-blocks are shifted by one phase.
The resulting distinct repaired edges \(f^0,f^1\) share their root and
exactly \(r-1\) middle owners.
Choose distinct shared owners \(X,y,z\).

The owner \(z\) has factorial degree, while

\[
 d(z,X)+d(z,y)=O(d(z)/m^2).
\]

Choose a repaired edge \(e\ni z\) avoiding \(X,y\). Then \(f^0,f^1\)
meet \(e\), and \(y\notin e\).

The width-two influence bound and the pair-codegree bound exclude only
\(O(d(X)/m^2)\) edges through \(X\). Choose \(2m^2-2\) further
repaired edges through \(X\) which avoid \(e\cup\{y\}\). Retain exactly
these edges, \(f^0,f^1\), and \(e\). Then (3.1) holds.

The maximum resource degree is \(\Delta=d_X\), attained at \(X\), while
\(d(y)=2\). Therefore

\[
 \chi_y={\Delta-d(y)\over r\Delta}
 ={1-m^{-2}\over r}.
\]

Indeed, a resource outside \(e\) lies in at most the \(d_X\) retained
\(X\)-rows, while a resource in \(e\) lies only in \(e,f^0,f^1\),
because every additional \(X\)-row was chosen disjoint from \(e\).

The two distinct rows \(f^0,f^1\) give the genuine off-diagonal term
\(c(e,y)(c(e,y)-1)=2\) in (1.7). For the protected pair cluster
\((X;e)\), its row count is \(A_C=a_X(e)=2\), so (3.3) follows.
This proves the theorem. \(\square\)

The example is a literal physical subcatalogue. It is not asserted to
be vertex-induced, near-regular, or likely along the random trajectory.
It proves only that the first edge-column stopping condition does not
deterministically imply the coin endpoint (2.13).

## 4. A literal separated-endpoint starred \(C_4\)

The next theorem gives the corresponding edge-only obstruction to
deducing drift coherence from one-column stopping alone.

### Theorem 4.1

Let \(J=\Theta(\log m)\). For every \(2\le h\le J\), there is a literal
repaired-ring subcatalogue with current \(X\)-link \(\mathcal F\) and
external family \(\mathcal R\) such that, writing

\[
\begin{aligned}
 d&=|\mathcal F|,\\
 A&=\max_{e\in\mathcal R}a(e),\\
 L_X&=\max_{f\in\mathcal F}
 |\{e\in\mathcal R:e\cap f\ne\varnothing\}|,\\
 \Delta&=\Delta(\mathcal H'),\qquad L=K\Delta,
\end{aligned}
\]

one has

\[
 L_X=\Theta(d),\qquad
 \Delta=\Theta(d),\qquad {A\over d}=O(J^2/m^2),
\tag{4.1}
\]

but

\[
 { \displaystyle
 \sum_{\substack{e,g\in\mathcal R\\e\cap g=\varnothing}}
 a(e)^{h-2}b(e,g)^2
 \over
 \displaystyle\sum_{e\in\mathcal R}a(e)^h}
 \ge c d.
\tag{4.2}
\]

Since

\[
                         {A\over d}L=O(J^2d/m)=o(d),
\tag{4.3}
\]

the self-normalized cycle estimate

\[
 \mathcal C_h^E(X)
 \le C{A\over d}L\,Y_h
\tag{4.4}
\]

does not follow from stopped one-column influence and literal repaired
geometry.

#### Proof

For an edge through \(X\) in which \(X\) is an interior path vertex,
let \(\{Y,Z\}\) be its two adjacent owners. Write

\[
 Y=X-a+b,\qquad Z=X-c+d',
\]

where \(a\ne c\) and \(b\ne d'\). The consecutive-triple fibre

\[
 \mathcal F_{Y,X,Z}
 =\{f:Y,X,Z\text{ occur consecutively in }f\}
\]

has exact size

\[
 A_0=
 {2(r-2)(m-2)!^2\over(m-H)!\mu_\kappa}
 =
 D_X{2(r-2)\over r\,m^2(m-1)^2}.
\tag{4.5}
\]

Here
\(\mu_\kappa=2((\kappa-H+1)_+)!\) is the common formal-representation
multiplicity.  It cancels from every ratio in the proof.

There are

\[
                         {m^2(m-1)^2\over2}
\tag{4.6}
\]

local-neighbour types, and they partition the edges in which \(X\) is
interior. Consistently,

\[
 {m^2(m-1)^2\over2}A_0={r-2\over r}D_X.
\tag{4.6a}
\]

Regard the \(m^2\) Johnson neighbours of \(X\) as the cells of an
\(m\times m\) array. Two cells form a local pair precisely when their
rows and columns are distinct. A maximal matching in this graph leaves
an independent set, which lies in one row or one column; hence the
matching has size at least \((m^2-m)/2\).

Choose

\[
 P=\left\lfloor{m^2\over C_0J^2}\right\rfloor
\tag{4.7}
\]

endpoint-disjoint local types and set

\[
 \mathcal F=\bigcup_{i=1}^P\mathcal F_{Y_i,X,Z_i},
\qquad d=PA_0.
\tag{4.8}
\]

Within \(\mathcal F\), the paths containing \(Y_i\), or \(Z_i\), are
exactly the paths in the \(i\)-th fibre. Indeed, because \(H<M/2\),
two cyclic middle windows in a promotion frame are at Johnson distance
one only at adjacent phases. Thus a distance-one owner occurring with
interior \(X\) must be one of the two displayed neighbours of \(X\);
endpoint-disjointness then identifies the unique fibre.

For a selected endpoint \(y\), double counting with the width-two
influence bound gives

\[
 \sum_{e\ni y}\bigl(a_{\mathcal F}(e)-A_0\bigr)
 \le(20+o(1)){dD_X\over m^2}
 =O(A_0D_X/J^2).
\tag{4.9}
\]

Edges through \(y\) which also contain \(X\) or its paired endpoint form
only \(O(D_X/m^2)\) of the \(y\)-link. Thus all but \(O(1/J)\) of the
remaining edges satisfy

\[
 A_0\le a_{\mathcal F}(e)\le(1+J^{-1})A_0.
\tag{4.10}
\]

Call these edges good. Independently retain every physical edge in the
union of the good endpoint links with probability

\[
                         p={d\over D_X}.
\tag{4.11}
\]

Because every original vertex degree is at most
\((1+o(1))D_X\), Chernoff and a union bound over the
\(\exp(O(m))\) physical resources give

\[
 \Delta(\mathcal R)=O(d)
\tag{4.12}
\]

and \(\Theta(d)\) retained edges through every selected endpoint.
Adding \(\mathcal F\) gives \(d\le\Delta(\mathcal H')\le Cd\).

The same thinning estimate gives \(L_X=\Theta(d)\). The two endpoint
pools belonging to the fibre of \(f\) supply \(\Theta(d)\) columns.
For every other selected endpoint \(y\notin f\), the width-two bound
leaves at most \(O(D_X/m^2)\) full-catalogue columns through \(y\)
meeting \(f\); after thinning and summing over \(2P\) endpoints their
contribution is \(O(d/J^2)\). Chernoff and a union bound over all
\(f\in\mathcal F\) are valid because \(d\) is factorially large.

For each paired \(Y_i,Z_i\), discard edges containing both endpoints.
For a good edge \(e\ni Y_i\), \(e\not\ni Z_i\), the width-two bound
allows only \(O(D_X/m^2)\) full-catalogue edges through \(Z_i\) meeting
\(e\). Therefore the good endpoint pools contain
\((1-o(1))D_X^2\) disjoint ordered cross-pairs. After thinning, they
contain \((1-o(1))d^2\) such pairs simultaneously for every \(i\);
the variance is \(O(d^2+d^3)=o(d^4)\). Chebyshev gives failure
probability \(O(1/d)\) for a fixed \(i\), and \(P/d=o(1)\), so the
claims hold simultaneously.

A good edge belongs to exactly one selected endpoint pool: membership
in two pools would make it meet two disjoint fibres and force
\(a_{\mathcal F}(e)\ge2A_0>(1+J^{-1})A_0\). Hence an ordered pair is
charged to at most one type.
There are consequently \(\Omega(Pd^2)\) distinct pairs
\(e\cap g=\varnothing\) such that

\[
 b(e,g)\ge A_0.
\tag{4.13}
\]

Equations (4.10)--(4.13), and
\((1+1/J)^h\le e\), give

\[
\begin{aligned}
 \sum_{e\in\mathcal R}a(e)^h
 &\le C P dA_0^h,\\
 \sum_{e\perp g}a(e)^{h-2}b(e,g)^2
 &\ge cP d^2A_0^h.
\end{aligned}
\]

This proves (4.1)--(4.2). \(\square\)

Thus (4.2) is at the local spanning-tree scale. Indeed, the general
tree inequality is

\[
 \sum_{e\perp g}[b(e,g)]_2\le dL_X^2A,
\]

and here \(L_X=\Theta(d)\), \(A=\Theta(A_0)\), while the constructed
off-diagonal sum has order \(Pd^2A_0^2=d^3A_0\).

The collapsed part

\[
 \sum_{e\perp g}a(e)^{h-2}b(e,g)
 \le L\sum_ea(e)^{h-1}
\]

is a tree equality partition. Since \(A_0\to\infty\), the distinct-row
term \(2\binom{b(e,g)}2\) dominates in Theorem 4.1. The obstruction is
a genuine injective starred \(C_4\), not row collapse.

Theorem 4.1 does not contradict the time-zero estimate in
MATH_THEOREM_FIRST_C4_DRIFT_COHERENCE_SCALE_20260727.md. That estimate
assumes the dynamic two-column mesh with its current relative
normalization. Theorem 4.1 shows precisely that one-column stopping does
not imply that assumption.

## 5. An uncompensated edge-only weighted process

Let the initial root and owner sets have sizes

\[
                         N=|\mathcal A_0|,\qquad
                         W=|\mathcal X_0|,\qquad
                         \rho={rN\over W}.
\tag{5.0}
\]

Let an active residual have root set \(\mathcal A\), owner set
\(\mathcal X\), and one root plus \(r\) owners in every edge. In the
trajectory statement below, \(\mathcal A\) means **all** roots not yet
used by the matching; thus feasibility includes nonisolation of every
such root. Choose
nonnegative root-stochastic weights

\[
 \sum_{e:\operatorname{root}(e)=R}p_e=1
 \qquad(R\in\mathcal A),
\tag{5.1}
\]

and give edge \(e\) an exponential clock of rate \(p_e/K\).

Put

\[
                         \ell_Y=\sum_{e\ni Y}p_e.
\tag{5.2}
\]

Every root has hazard \(1/K\), every owner \(Y\) has hazard
\(\ell_Y/K\), and

\[
                         \sum_Y\ell_Y=r|\mathcal A|.
\tag{5.3}
\]

Define

\[
                         q={r|\mathcal A|\over|\mathcal X|}.
\tag{5.4}
\]

### Theorem 5.1 (exact balanced edge-only criterion)

There are root-stochastic weights satisfying

\[
                         \ell_Y=q\qquad(Y\in\mathcal X)
\tag{5.5}
\]

if and only if, for every signed owner potential
\(\beta\in\mathbb R^{\mathcal X}\),

\[
 \boxed{
 q\sum_{Y\in\mathcal X}\beta_Y
 \le
 \sum_{R\in\mathcal A}
 \max_{e:\operatorname{root}(e)=R}
 \sum_{Y\in e\cap\mathcal X}\beta_Y.}
\tag{JH}
\]

#### Proof

For each root \(R\), let

\[
 P_R=\operatorname{conv}
 \{\mathbf1_{e\cap\mathcal X}:e\text{ rooted at }R\}.
\]

The possible owner-load vectors are exactly the Minkowski sum
\(\sum_RP_R\). Condition (5.5) is the membership

\[
                         q\mathbf1_{\mathcal X}\in\sum_RP_R.
\]

By finite-dimensional separation, this holds exactly when every signed
linear functional \(\beta\) is at most the support function of the
Minkowski sum. Support functions add, and the support function of
\(P_R\) is the displayed maximum in (JH). \(\square\)

If one also requires diffuse weights, let \(\mathcal D_R\) denote the
actual current degree of root \(R\), and impose

\[
                         p_e\le {C\over\mathcal D_R}.
\tag{5.6}
\]

Provided the following capped root simplex is nonempty for every
\(R\), replace each maximum in (JH) by its support function:

\[
 \left\{(p_e):
 \sum_{e\text{ rooted at }R}p_e=1,\
 0\le p_e\le C/\mathcal D_R
 \right\}.
\tag{DJH}
\]

This capped joint Hall condition is exact and remains unproved in a
general endogenous residual.

### Exact trajectory if (JH) holds hereditarily

Assume that after every selected edge, (JH) remains feasible on all
still-unmatched roots and all live owners, and choose a balanced vector
of weights there. Then the predictable density equations are

\[
 {dx\over dt}=-{x\over K},\qquad
 {du\over dt}=-{qu\over K}.
\tag{5.7}
\]

Pathwise, after \(s\) selected edges,

\[
 x=1-{s\over N},\qquad
 u=1-{rs\over W}=1-\rho(1-x),
\qquad
 q={\rho x\over u}.
\tag{5.8}
\]

Indeed, when \(k\) roots remain, their aggregate selection rate is
\(k/K\). Hence the root-count process is the standard pure-death chain
with transition rate \(k/K\), so at time \(t\) its law is

\[
                         \operatorname{Bin}(N,e^{-t/K}).
\tag{5.8a}
\]

Thus (5.7) is coherent and, at

\[
                         T=K\log(1/z),
\]

the process has root density \(z+o(1)\) with probability \(1-o(1)\).
If \(N_T\) roots remain, its exact owner leave is

\[
                         L_T=W-rN+rN_T
                         =W-rN+rNz+o(W)
\tag{5.9}
\]

with probability \(1-o(1)\). For \(z=o(1)\), this is \(o(W)\), using
the repaired-ring calibration \(W-rN=o(W)\).

An edge-only process cannot give roots and owners one common marginal
hazard: incidence totals force an owner hazard \(q\) times the root
hazard, and \(q<1\) because \(W-rN>0\). The two-density trajectory
(5.8), not compensated common thinning, is the exact no-waste reference.

### Root-normalized weights and drift coherence

Without solving (JH), one can always put

\[
                         p_e={1\over d(\operatorname{root}(e))}
\tag{5.10}
\]

for nonisolated roots. This keeps the root hazard exact, but the owner
loads \(\ell_Y\) need not equal \(q\).

For a protected cluster \(C\), let \(\Pi_C\) be its protected resource
set and put

\[
 \mathcal G_C=\{g:g\cap\Pi_C=\varnothing\},\qquad
 \lambda_v^C=\sum_{\substack{g\in\mathcal G_C\\v\in g}}p_g.
\tag{5.10a}
\]

After separating events which meet \(\Pi_C\), let \(S_C(f)\) be the
unprotected resources of a row and define the admissible multiplicity
excess

\[
 J_p^C(S)=
 \sum_{v\in S}\lambda_v^C
 -
 \sum_{\substack{g\in\mathcal G_C\\g\cap S\ne\varnothing}}p_g.
\tag{5.11}
\]

The exact normalized admissible **kill-hazard excess** over the
two-density reference is

\[
 \boxed{
 \Gamma_C(t)=
 {1\over KA_C}
 \sum_{f\in\mathcal F_C}
 \left[
 \sum_{R\in S_C(f)\cap\mathcal A}(\lambda_R^C-1)
 +\sum_{Y\in S_C(f)\cap\mathcal X}(\lambda_Y^C-q)
 -J_p^C(S_C(f))
 \right].}
\tag{DC}
\]

The normalized drift discrepancy is \(-\Gamma_C\). Full drift control
also requires the separately exposed protected-resource hazard. The
required admissible condition is

\[
                         \int_0^T|\Gamma_C(t)|\,dt=o(1)
\tag{5.12}
\]

incidence-weightedly for every monitored class. Pointwise
\(|\ell_Y-q|\le\eta q\) alone does not imply (5.12), because
\(T=\Theta(K\log m)\).

Define

\[
 B_C(g)=|\{f\in\mathcal F_C:f\cap g\ne\varnothing\}|.
\tag{5.12a}
\]

The edge-only generator contains no explicit coin summand. With every
\(g\)-sum restricted to \(g\in\mathcal G_C\),

\[
 \mathcal LA_C^h
 =
 \sum_{\ell=1}^h(-1)^\ell\binom h\ell A_C^{h-\ell}
 {1\over K}\sum_{g\in\mathcal G_C}p_gB_C(g)^\ell,
\tag{5.13}
\]

after freezing at protected-resource death.

It does not erase resource concentration. For an unprotected resource
\(y\), define its admissible hazard

\[
 h_y^C={1\over K}
 \sum_{\substack{g\ni y\\g\text{ avoids protected resources}}}p_g.
\tag{5.14}
\]

Then

\[
 {1\over K}\sum_{g\in\mathcal G_C}p_gB_C(g)^\ell
 \ge h_y^C P_C(y)^\ell.
\tag{5.15}
\]

Thus resource powers move into the legal edge columns. Theorem 4.1
also remains an edge-only obstruction. Removing coins simplifies the
generator but does not prove the dynamic starred \(C_4\) hierarchy.

## 6. Exact surviving boundary

Proved here:

1. the starred edge and legal coin generators (1.3), (1.6);
2. the corrected two-colour compensation tree theorem;
3. the literal legal coin obstruction of Theorem 3.1;
4. the literal separated-endpoint starred \(C_4\) family of
   Theorem 4.1;
5. the exact balanced edge-only Hall/Farkas theorem; and
6. the two-density edge-only trajectory and the corrected admissible
   kill-hazard identity (DC).

Not proved:

1. that the starred \(C_4\) family in Theorem 4.1 is support-reachable
   or carries nonnegligible incidence along the random trajectory;
2. dynamic self-normalized regeneration of the starred \(C_4\);
3. the resource-coin endpoint (2.13) after endogenous restriction;
4. hereditary capped joint Hall (DJH);
5. admissible-load and protected-hazard control after cluster
   truncation; or
6. the coefficient-one owner near-packing.

The smallest compensated-process gate is the incidence-weighted legal
resource endpoint (2.13), together with the dynamic starred \(C_4\).
The smallest edge-only alternative is hereditary (DJH), the admissible
load/protected-hazard control exposed in (DC), and the same starred
edge-column hierarchy. With root-normalized weights, (DC) itself
replaces global balance but remains unproved.
