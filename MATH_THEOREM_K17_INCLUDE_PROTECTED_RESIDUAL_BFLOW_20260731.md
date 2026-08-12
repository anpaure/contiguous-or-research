# K17 include-protected residual \(b\)-flow and topology boundary

## 0. Scope

This note gives the exact lower-factor recourse for a **fixed persisted
physical bank**. The bank consists of selected seam edges together with
the old/source edges which the selected upper witnesses actually protect.
It does not include an old source edge merely because that edge survived a
preliminary scaffold cut.

The result is exact for the unrestricted Johnson edge catalogue. If the
residual catalogue is filtered by direction, residence, collar, or history,
the flow remains a necessary obstruction but is not sufficient unless every
pair selected at a colour is physically allowed by that filtered catalogue.

Let \(V\) be the \(N\) rank-\(r\) owners and let \(\mathcal C\) be the \(N\)
rank-\((r-1)\) lower colours. For a physical Johnson edge \(e=uv\), put

\[
                         \chi(e)=u\cap v.
\]

Fix a lower-rainbow Johnson \(2\)-factor \(F\), and write \(f_c\) for its
unique edge of colour \(c\).

## 1. The fixed bank and exact local gate

Let \(K\subseteq E(J)\) be the physical edge set forced by the persisted
seams and selected protected witnesses. Repeated reasons for retaining the
same physical edge are ORed before forming \(K\). Put

\[
 C_K=\{\chi(e):e\in K\},\qquad
 d_K(v)=2-\deg_K(v).
\]

The elementary necessary conditions are

\[
 \deg_K(v)\le2\quad(v\in V),\qquad
 |K\cap\chi^{-1}(c)|\le1\quad(c\in\mathcal C).       \tag{1.1}
\]

The second condition is exactly where distinct seam colours and
disjointness from selected protected source colours enter. A seam of colour
\(c\) may coexist with an *unprotected* source edge \(f_c\) in the old
scaffold: the eventual completion must then eject \(f_c\). Such a conflict
is not a violation of (1.1).

## 2. Contracted include-protected flow

Fix a candidate omitted colour \(z\in\mathcal C\setminus C_K\). Introduce
one dummy right vertex \(\partial\), representing the two endpoints of the
eventual path, and form the bipartite graph

\[
 B_z=(V,L_z;D_z),\qquad
 L_z=(\mathcal C\setminus(C_K\cup\{z\}))\cup\{\partial\}. \tag{2.1}
\]

For \(c\ne\partial\), put \(vc\in D_z\) iff \(c\subset v\); put
\(v\partial\in D_z\) for every \(v\in V\). Every real right vertex and
\(\partial\) has demand \(2\), while owner \(v\) has demand \(d_K(v)\).
The totals agree:

\[
 \sum_{v\in V}d_K(v)=2N-2|K|
 =2\bigl(N-|K|-1\bigr)+2=2|L_z|.                 \tag{2.2}
\]

### Theorem 2.1 (exact include-protected \(b\)-flow)

Assume (1.1). There is a spanning undirected lower-rainbow
degree-\((2,\ldots,2,1,1)\) subgraph which contains \(K\), omits precisely
the colour \(z\), and is allowed to have cycle components, if and only if
for every \(X\subseteq V\) and \(Y\subseteq L_z\),

\[
 \boxed{
 d_K(X)\le 2|Y|+|D_z\cap(X\times(L_z\setminus Y))|.
 }                                                        \tag{2.3}
\]

Equivalently, define

\[
 \delta_z(K)=\max_{X\subseteq V,\,Y\subseteq L_z}
 \left[d_K(X)-2|Y|-|D_z\cap(X\times(L_z\setminus Y))|\right]_+ . \tag{2.4}
\]

Then the fixed bank has an undirected factor completion with omitted colour
\(z\) exactly when \(\delta_z(K)=0\). Thus the variable-hole factor gate is

\[
             \min_{z\in\mathcal C\setminus C_K}\delta_z(K)=0. \tag{2.5}
\]

The two endpoints are not enumerated: they are the two distinct owners
whose edges to \(\partial\) carry flow.

#### Proof

Make a network with arcs \(s\to v\) of capacity \(d_K(v)\), arcs \(v\to a\)
of capacity one for \(va\in D_z\), and arcs \(a\to t\) of capacity two for
\(a\in L_z\). Its total required flow is (2.2). The cut with source side
\(\{s\}\cup X\cup Y\) has capacity

\[
 d_K(V\setminus X)+|D_z\cap(X\times(L_z\setminus Y))|+2|Y|.
\]

It has capacity at least \(d_K(V)\) exactly when (2.3) holds. Hence
max-flow/min-cut and flow integrality give an integral degree-saturating
flow exactly under (2.3).

At every real colour \(c\), its two unit incidences select two distinct
owners \(u,v\supset c\). They determine the Johnson edge \(uv\) of colour
\(c\). The two dummy incidences select distinct owners and reduce their
physical degrees from two to one. Adding the already forced edges \(K\)
therefore gives the claimed lower-rainbow spanning degree pattern.
Conversely, expand every selected physical edge into its two owner-colour
incidences and send the two endpoint deficits to \(\partial\). This is a
saturating integral flow. \(\square\)

### Corollary 2.2 (the ejection distinction is automatic)

If a seam \(e\in K\setminus F\) has colour \(c\), then the colour vertex
\(c\) is removed in (2.1). Consequently \(f_c\) cannot occur in any
completion and is ejected. If \(f_c\) was not protected, this is legal. If
\(f_c\in K\), colour simplicity (1.1) fails before the flow is run.

This is the exact distinction between a fatal selected-bank conflict and an
unprotected ejection obligation.

## 3. Exact source-cut and endpoint ledger

Let \(q_e\) be the selected physical-edge indicators in any completion, let
\(p_v\) indicate its two endpoints, and let \(z_c\) indicate the omitted
colour. Define the eventual source-cut variable

\[
                         c_c=1-q_{f_c}.                    \tag{3.1}
\]

Then the completion obeys the exact equations

\[
 \boxed{
 \sum_{e\notin F:\,\chi(e)=c}q_e+z_c=c_c
 }                                                        \tag{3.2}
\]

and

\[
 \boxed{
 \sum_{e\notin F:\,e\ni v}q_e+p_v
      =\sum_{c:\,v\in f_c}c_c .
 }                                                        \tag{3.3}
\]

Moreover

\[
 \sum_vp_v=2,\qquad \sum_cz_c=1,\qquad
 \sum_{e\notin F}q_e=\sum_cc_c-1.                         \tag{3.4}
\]

#### Proof

For colour \(c\), either \(f_c\) survives, or exactly one nonfactor edge of
colour \(c\) is selected, or \(c\) is the unique omitted colour. This gives
(3.2). At owner \(v\), the source factor supplies two incidences. Every cut
source incidence must be replaced by a nonfactor incidence or absorbed by
an endpoint; rearranging the owner degree equation gives (3.3). Summing
(3.2) gives the last equality in (3.4). \(\square\)

## 4. Branch-independent min-cut rows and certified release

The contracted form is best for auditing a fixed candidate. For CEGAR,
retain the full graph for a fixed omitted colour \(z\):

\[
 \widetilde L_z=(\mathcal C\setminus\{z\})\cup\{\partial\},
\]

with all owner-colour and endpoint incidences. Let \(\rho_{v,c}\) be the
exact OR that the guarded bank forces incidence \(vc\); there are no forced
dummy incidences. The omitted branch also requires

\[
                    \rho_{v,z}=0\qquad(v\in V),            \tag{4.0}
\]

or, with a variable omitted-colour selector, the eager rows
\(\rho_{v,c}+z_c\le1\). Forced local degrees must be at most two. Every
completion satisfies, for all \(X\subseteq V\) and
\(Y\subseteq\widetilde L_z\),

\[
 \boxed{
 2|X|+
 \sum_{\substack{v\notin X,\ c\in Y\\c\ne\partial}}
       \rho_{v,c}
 \le
 2|Y|+
 |\widetilde D_z\cap(X\times(\widetilde L_z\setminus Y))|.
 }                                                        \tag{4.1}
\]

For integral guards, (4.1) is necessary and sufficient for the
degree/colour flow with omitted colour \(z\). It is the forced-edge
max-flow cut after the forced incidences have been deleted and their
degrees subtracted. In a variable-hole master it is imposed conditionally
on \(z_c=1\), or separated after fixing the omitted-colour branch.

Suppose a fixed bank violates (4.1) by \(\Delta>0\). For a forced physical
edge \(e=uv\) of colour \(c\), define its coefficient in this cut by

\[
 a_{X,Y}(e)=\mathbf1_{c\in Y}
       \bigl(\mathbf1_{u\notin X}+\mathbf1_{v\notin X}\bigr)
       \in\{0,1,2\}.                                     \tag{4.2}
\]

Any relaxed bank capable of passing this same flow branch must release a
set \(H\subseteq K\) satisfying

\[
                   \sum_{e\in H}a_{X,Y}(e)\ge\Delta.      \tag{4.3}
\]

In particular, at least \(\lceil\Delta/2\rceil\) physical bank edges must be
released. Equation (4.1), expressed in exact physical-incidence ORs, is the
weakest reusable linear relaxation certified by this min-cut. It does not
assert that satisfying this one row suffices: all subsequently violated
cuts, and at least one omitted-colour branch, must pass. Nor does a cut for
one \(z\) force any release if another omitted-colour branch already passes;
a variable-hole obstruction consists of a failed certificate for every
\(z\notin C_K\).

## 5. Where topology begins

A passing flow can be one path together with cycles. This is not a factor
certificate for the equality lane.

For fixed \(z\), work on the augmented incidence ground
\(\widetilde D_z\). Let

* \(M_V\) be the partition matroid of capacity two on every owner star;
* \(M_L\) be the partition matroid of capacity two on every right star;
* \(M_G\) be the direct sum of the graphic matroid on the **real**
  owner-colour incidences and the free matroid on the endpoint edges
  \(v\partial\).

### Theorem 5.1 (exact undirected topology lift)

There is an undirected lower-rainbow Hamilton path containing \(K\) and
omitting \(z\) if and only if the forced incidence bank extends to a common
independent set of \(M_V,M_L,M_G\) of size \(2N\).

#### Proof

A size-\(2N\) set independent in the two partition matroids saturates every
owner and right star. Exactly two endpoint edges are selected, at distinct
owners. Hence there are \(2N-2\) real incidences on the
\(2N-1\) real vertices \(V\cup(\mathcal C\setminus\{z\})\). Every real
vertex is incident: real colours have degree two, and an owner has at most
one endpoint edge. Graphic independence therefore makes the real incidence
graph a tree. Suppressing each degree-two colour vertex gives a spanning
owner path. The converse follows by subdividing the colours of a Hamilton
path and adding its two endpoint edges. \(\square\)

Equivalently, if \(a_i\) are the selected real incidence variables, the
topology layer adds the lazy graphic rows

\[
       \sum_{i\in\widetilde D_z[Z]}a_i\le |Z|-1
       \qquad
       (\varnothing\ne Z\subseteq
          V\cup(\mathcal C\setminus\{z\})),                \tag{5.1}
\]

where endpoint edges incident with \(\partial\) are excluded from the sum.
Together with the two exact partition-degree systems and total size \(2N\),
these rows are a direct executable formulation of Theorem 5.1.

Thus ordinary max-flow is the exact degree/colour boundary, while topology
is a three-matroid common-independence problem. A cyclic max-flow witness is
not an obstruction: a different flow may be acyclic. A topology no-good is
proof-safe only after the common-independent-set recourse is itself proved
infeasible, or after a replayed assumption core from an exact formulation.

Direction, prescribed seam orientations, residence, compiler chronology,
and arbitrary-width upper witnesses remain subsequent literal constraints.
No statement here proves a K17 word or equality.
