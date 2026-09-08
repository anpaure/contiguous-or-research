# A growing \(D_s\) balanced first-edge compiler

Date: 2026-07-26

Method: pure mathematics only. No computation, search, solver, or web input
is used.

## 0. Outcome

Fix \(s\ge2\), and put

\[
 J=[2s],\qquad {\cal D}={\cal D}_s,\qquad
 B=|{\cal D}|=\operatorname {Cat}_s,
\]

and let a \(D_s\)-port path have the form

\[
 P=X_0\subset Y_0\supset X_1\subset\cdots
 \subset Y_{s-1}\supset X_s=\overline P.
\tag{0.1}
\]

The first inserted coordinate is

\[
                         b_1(P)=Y_0\setminus P.
\tag{0.2}
\]

There are three distinct levels of the growing first-edge problem.

1. **Rowwise legality and Catalan balance.** This level has an explicit
   integral solution. For

   \[
    E_j=\{2j,2j+1\}\quad(1\le j<s),\qquad
    E_s=\{2s,1\},
   \]

   put

   \[
                    w_{s,j}=\operatorname {Cat}_{j-1}
                              \operatorname {Cat}_{s-j}.
\tag{0.3}
   \]

   There is a deterministic assignment of one individually legal clean
   entrance

   \[
                  P\subset Y_0(P)\supset X_1(P)
\tag{0.4}
   \]

   to every \(P\in{\cal D}\) such that

   \[
   \#\{P:b_1(P)\in E_j\}=w_{s,j}\quad(1\le j\le s)
\tag{0.5}
   \]

   and, for \(j<s\), the two coordinates in \(E_j\) receive
   \(\lfloor w_{s,j}/2\rfloor\) and
   \(\lceil w_{s,j}/2\rceil\) roots. At the endpoint pair,

   \[
                   \#\{P:b_1(P)=2s\}
                        =\operatorname {Cat}_{s-1},
   \qquad
                   \#\{P:b_1(P)=1\}=0.
\tag{0.6}
   \]

   The rule is obtained from first return, Chung--Feller rotation, the
   even-pair group \(H_s\), and one integral transportation flow.

   For \(j<s\), the numbers \(w_{s,j}\) are the chosen first-return
   **design quotas**, not invariants of every port factor. Already at
   \(s=4\), complete port factors can transfer mass between adjacent
   internal bins. Only the endpoint quota (0.6) is universal.

2. **Collision-free entrance ownership.** The rule in (0.4) need not make
   all \(X_1(P)\)'s and all \(Y_0(P)\)'s distinct. The exact collision-free
   assertion is a four-partite matching problem, called
   \(\mathrm{BFE}_s\) below. It has an explicit fractional solution with the
   exact Catalan quotas (0.5), but integrality is not proved.

3. **Completion.** Even a collision-free balanced entrance need not extend
   automatically. After the first edges are frozen, completion is exactly a
   residual clean-path matching, or equivalently two ordinary residual
   perfect matchings plus the complement-monodromy condition. Theorem 6.1
   gives the necessary-and-sufficient formulation.

Thus the first nontrivial growing achievement is exact: Catalan-balanced
legal first edges exist root by root, and the full port-path system has a
balanced rational point. The remaining obstruction is not scalar capacity;
it is correlated \(X/Y\) ownership followed by endpoint monodromy.

## 1. Two unavoidable endpoint laws

Every Dyck root contains coordinate \(1\) and omits coordinate \(2s\).
For one rooted path, let

\[
 d_P=\text{the deletion time of }1,\qquad
 r_P=\text{the insertion time of }2s.
\tag{1.1}
\]

Both lie in \(\{1,\ldots,s\}\).

### Theorem 1.1 (universal endpoint quota)

Every \(D_s\)-port complement path factor satisfies

\[
 \boxed{\#\{P:b_1(P)=2s\}=\operatorname {Cat}_{s-1}.}
\tag{1.2}
\]

On exactly those rows, \(2s\) is inserted at time one and \(1\) is deleted
at time \(s\).

### Proof

The number of \(s\)-sets containing both \(1,2s\) is

\[
                         \binom{2s-2}{s-2},
\tag{1.3}
\]

whereas the number of \((s+1)\)-sets containing both is

\[
                         \binom{2s-2}{s-1}.
\tag{1.4}
\]

In one path, the \(Y\)-pair count exceeds the \(X\)-pair count by one
exactly when \(r_P\le d_P\). Exact \(X/Y\)-ownership therefore gives

\[
 \#\{P:r_P\le d_P\}
 =\binom{2s-2}{s-1}-\binom{2s-2}{s-2}
 =\operatorname {Cat}_{s-1}.
\tag{1.5}
\]

The number of \(X\)-states on that row containing both coordinates is
\((d_P-r_P)_+\). Summing over the factor gives (1.3). But

\[
 \binom{2s-2}{s-2}
      =(s-1)\operatorname {Cat}_{s-1},
\tag{1.6}
\]

and the \(\operatorname {Cat}_{s-1}\) positive summands in (1.5) are each
at most \(s-1\). Equality forces every one of them to equal \(s-1\).
Thus \(r_P=1,d_P=s\) on precisely those rows. This is equivalent to
\(b_1(P)=2s\), proving the theorem. \(\square\)

Coordinate \(1\) cannot be inserted because it belongs to every root. Thus
(0.6) is compulsory, not merely a design choice.

## 2. First-return Catalan bins

Write a Dyck root in first-return form

\[
                         P=1u0v,
\tag{2.1}
\]

where \(u\in{\cal D}_{j-1}\) and \(v\in{\cal D}_{s-j}\). Its first
primitive component has semilength \(j\). Hence the first-return class

\[
 {\cal D}_{s,j}
 =\{1u0v:u\in{\cal D}_{j-1},\ v\in{\cal D}_{s-j}\}
\tag{2.2}
\]

has cardinality

\[
                         |{\cal D}_{s,j}|=w_{s,j}.
\tag{2.3}
\]

The Catalan convolution gives

\[
                         \sum_{j=1}^s w_{s,j}=B.
\tag{2.4}
\]

In the canonical MSW path, the first insertion at a root in
\({\cal D}_{s,j}\) is the closing coordinate \(2j\). Thus the canonical
first-edge histogram is

\[
                         \sum_{j=1}^s w_{s,j}e_{2j}.
\tag{2.5}
\]

The accompanying Chung--Feller phase maps are the cycle-lemma
factorization

\[
 \binom Js=\mathop{\dot\bigcup}_{t=0}^{s}L_t,\qquad
 |L_t|=B,
\tag{2.6}
\]

with \(L_0={\cal D}\), \(L_s=\overline{\cal D}\), and the canonical map
\(P\mapsto X_t^0(P)\) a bijection from \({\cal D}\) to \(L_t\). This is
the rotation structure used below: conjugating the whole cycle-lemma path,
rather than changing one label in isolation, keeps every candidate entrance
inside a genuine complement path factor.

The purpose of the balanced compiler is to retain the exact bin masses
\(w_{s,j}\), while splitting every nonendpoint bin across its adjacent
coordinate pair \(E_j\).

## 3. The even-pair rotation overlay

Put

\[
 H_s=\langle(2\ 3),(4\ 5),\ldots,(2s-2\ 2s-1)\rangle
       \cong C_2^{\,s-1}.
\tag{3.1}
\]

Swapping the steps at positions \(2i,2i+1\) preserves the flaw number of
every balanced path: immediately before the pair the height is odd and
therefore nonzero; exchanging \(+-\) with \(-+\) cannot change whether
either step lies below zero. Consequently every \(h\in H_s\) preserves
\({\cal D}_s\) and every Chung--Feller layer.

Let

\[
 \gamma_0(Q)=
 \bigl(Q=X_0^0(Q)\subset Y_0^0(Q)\supset X_1^0(Q)
       \subset\cdots\supset X_s^0(Q)=\overline Q\bigr)
\tag{3.2}
\]

be the canonical path rooted at \(Q\). For \(h\in H_s\) and
\(P\in{\cal D}\), define the reindexed conjugate path

\[
                         \gamma_h(P)=h\gamma_0(h^{-1}P).
\tag{3.3}
\]

This is again a complete \(D_s\)-port factor: coordinate relabelling
preserves both shores, \(H_s\) preserves the Dyck root family, and
complementation commutes with \(h\).

Write its entrance as

\[
 P\subset Y_h(P)\supset X_h(P),
\tag{3.4}
\]

and its insertion label as

\[
 b_h(P)=Y_h(P)\setminus P
       =h\!\left(2\kappa(h^{-1}P)\right),
\tag{3.5}
\]

where \(\kappa(Q)\) is the first-return semilength of \(Q\). Formula (3.5)
is the promised first-return/rotation rule.

### Theorem 3.1 (balanced rational compiler)

Give every entrance (3.4) weight \(1/|H_s|\). Then:

1. every root has total weight one;
2. the load of every \(X\)-state and every \(Y\)-state is at most one;
3. every weighted row is clean and ends at its prescribed complement;
4. the first-insertion histogram is

   \[
   \boxed{
    \operatorname {Cat}_{s-1}e_{2s}
     +\frac12\sum_{j=1}^{s-1}
       w_{s,j}(e_{2j}+e_{2j+1}).}
\tag{3.6}
   \]

Moreover, averaging the entire paths \(\gamma_h(P)\), rather than only
their entrances, gives a fractional exact \(D_s\)-port path factor with
the same histogram (3.6).

### Proof

For fixed \(h\), the paths \(\{\gamma_h(P):P\in{\cal D}\}\) form an exact
factor. Thus they use every root once, every \(X\)-state once, and every
\(Y\)-state once. Averaging exact factors gives root load one and complete
fractional \(X/Y\)-ownership. Restricting to their first entrances can only
decrease an individual \(X\)- or \(Y\)-load, proving Items 1--3.

For fixed \(h\), the roots \(h^{-1}P\) still run through all of
\({\cal D}\). Hence bin \(j\) contributes \(w_{s,j}\) labels, all at
\(h(2j)\). For \(j<s\), exactly half the elements of \(H_s\) fix \(2j\)
and half send it to \(2j+1\). Every \(h\) fixes \(1,2s\). Averaging gives
(3.6). The last assertion follows by averaging the full path ledgers.
\(\square\)

This proves that there is no fractional Catalan-capacity obstruction at the
first edge, at either ownership shore, or in the full complement-path
system.

## 4. An integral rowwise balanced rule

For a root \(P\), let

\[
                         \Lambda(P)=\{b_h(P):h\in H_s\}.
\tag{4.1}
\]

Make a flow network with:

* one unit-supply node for every \(P\in{\cal D}\);
* a coordinate node for every \(b\in[2s]\);
* a pair node for every \(E_j\);
* an arc \(P\to b\) exactly when \(b\in\Lambda(P)\);
* arcs \(b\to E_j\) for \(b\in E_j\);
* demand \(w_{s,j}\) at \(E_j\).

At the coordinate arcs impose

\[
\begin{aligned}
\lfloor w_{s,j}/2\rfloor
 &\le q_{2j},q_{2j+1}
 \le\lceil w_{s,j}/2\rceil
 &&(j<s),\\
q_{2s}&=\operatorname {Cat}_{s-1},\qquad q_1=0.
\end{aligned}
\tag{4.2}
\]

### Theorem 4.1 (integral balanced label compiler)

The network has an integral unit flow. Consequently one can assign every
root \(P\) a label \(b(P)\in\Lambda(P)\) so that (0.5)--(0.6) hold and the
two labels in every \(E_j\), \(j<s\), differ in load by at most one.

For every selected arc \(P\to b(P)\), choose the lexicographically first
\(h(P)\in H_s\) satisfying \(b_{h(P)}(P)=b(P)\), and set

\[
 Y_0(P)=Y_{h(P)}(P),\qquad X_1(P)=X_{h(P)}(P).
\tag{4.3}
\]

Then (4.3) is an individually legal clean first edge for every root.

### Proof

The uniform \(H_s\)-average in Theorem 3.1 supplies a fractional flow.
At pair \(E_j\) its mass is exactly \(w_{s,j}\); at its two coordinate
nodes the masses are \(w_{s,j}/2\), which satisfy the interval constraints
(4.2). The endpoint masses are those in (0.6).

This is an ordinary capacitated network with integral supplies, demands,
lower bounds, and upper bounds. Its incidence matrix is totally unimodular,
so fractional feasibility implies an integral flow. The integral flow
selects one allowed label at every root and has the required coordinate and
pair totals.

Every witness \(h(P)\) comes from the genuine port factor (3.3). Hence
\(P\subset Y_{h(P)}(P)\supset X_{h(P)}(P)\) is a Johnson entrance,
\(X_{h(P)}(P)\notin{\cal D}\cup\overline{\cal D}\), and its insertion label
is \(b(P)\). This proves rowwise legality and cleanliness. \(\square\)

The flow is deterministic after fixing lexicographic orders: take the
lexicographically first integral flow and then the first witnesses \(h(P)\).
No probabilistic selection is hidden in the rule.

### Parity audit

The two loads in \(E_j\) can be exactly equal unless \(w_{s,j}\) is odd.
The Catalan parity theorem says that \(\operatorname {Cat}_n\) is odd
exactly when \(n=2^a-1\). Therefore

\[
 w_{s,j}\ \hbox{is odd}
 \quad\Longleftrightarrow\quad
 j=2^a,\quad s-j=2^b-1
\tag{4.4}
\]

for some \(a,b\ge0\). Formula (4.2) is therefore the sharp integral
rounding of (3.6), with no unrecorded parity loss.

## 5. The exact entrance-matching gate

Theorem 4.1 does not assert that the selected \(X_1(P)\)'s or
\(Y_0(P)\)'s are globally distinct. This is the first genuine integral
gate.

Define the **balanced first-entrance hypergraph** \({\cal E}_s\) as follows.
Its vertices are

\[
 {\cal D}\ \dot\cup\
 \left(\binom Js\setminus({\cal D}\cup\overline{\cal D})\right)
 \ \dot\cup\ \binom J{s+1}
 \ \dot\cup\ [2s].
\tag{5.1}
\]

For every \(P\in{\cal D}\) and \(h\in H_s\), include the hyperedge

\[
                         e(P,h)=
       \{P,\ X_h(P),\ Y_h(P),\ b_h(P)\}.
\tag{5.2}
\]

### Problem \(\mathrm{BFE}_s\)

Choose one edge incident with every root, at most one edge incident with
every \(X\)- or \(Y\)-resource, and coordinate degrees satisfying
(4.2)--(0.6).

### Proposition 5.1

The uniform weights \(1/|H_s|\) form a fractional solution of
\(\mathrm{BFE}_s\). An integral solution is exactly a collision-free,
Catalan-balanced entrance assignment.

### Proof

Theorem 3.1 gives root load one, \(X/Y\)-loads at most one, and the balanced
coordinate degrees. Conversely, an integral hypergraph matching has one
legal entrance per root, distinct \(X_1\)'s and \(Y_0\)'s, and precisely the
stated quotas. \(\square\)

This formulation audits the rounding boundary. Ordinary transportation
integrality proves Theorem 4.1 only after the \(X/Y\) resource rows are
discarded. With those rows restored, (5.2) is a four-partite hypergraph;
no generic total-unimodularity claim is available.

## 6. Exact completion after the entrances

Assume now that an integral solution of \(\mathrm{BFE}_s\) has been chosen.
Write

\[
 {\cal S}_1=\{X_1(P):P\in{\cal D}\},\qquad
 {\cal T}_0=\{Y_0(P):P\in{\cal D}\}.
\tag{6.1}
\]

Both sets have size \(B\), and \({\cal S}_1\) avoids
\({\cal D}\cup\overline{\cal D}\).

For \(P\in{\cal D}\), let \(\Gamma_\epsilon(P)\) be the set of clean
geodesics

\[
 P,X_1(P),X_2,\ldots,X_{s-1},\overline P
\tag{6.2}
\]

whose first adjacent union is the prescribed \(Y_0(P)\). For
\(\gamma\in\Gamma_\epsilon(P)\), additionally require

\[
 X_2,\ldots,X_{s-1}\notin{\cal S}_1,\qquad
 Y_1,\ldots,Y_{s-1}\notin{\cal T}_0,
\tag{6.2a}
\]

and define its remaining resource set

\[
 R_\epsilon(\gamma)=
 \{X_2,\ldots,X_{s-1}\}
 \mathbin{\dot\cup}
 \{Y_1,\ldots,Y_{s-1}\}.
\tag{6.3}
\]

The residual resource universe is

\[
\begin{aligned}
 {\cal R}_\epsilon={}&
 \left[
 \binom Js\setminus
   ({\cal D}\cup\overline{\cal D}\cup{\cal S}_1)
 \right]\\
 &\mathbin{\dot\cup}
 \left[\binom J{s+1}\setminus{\cal T}_0\right].
\end{aligned}
\tag{6.4}
\]

Its size is

\[
 |{\cal R}_\epsilon|
 =(s-2)B+(s-1)B=(2s-3)B,
\tag{6.5}
\]

while every set (6.3) has \(2s-3\) resources.

### Theorem 6.1 (necessary-and-sufficient residual completion)

The balanced entrances extend to an exact \(D_s\)-port factor if and only
if one can select one \(\gamma_P\in\Gamma_\epsilon(P)\) for every root so
that the sets

\[
                         R_\epsilon(\gamma_P)
\tag{6.6}
\]

are pairwise disjoint.

### Proof

Necessity is literal ownership: distinct completed paths cannot share an
internal \(X\)-state or a \(Y\)-colour.

Conversely, the selected resources are disjoint and their total number is

\[
                         B(2s-3)=|{\cal R}_\epsilon|.
\]

They therefore exhaust (6.4). Together with the prescribed roots,
first states, first colours, and complementary endpoints, the paths own
every \(X\)- and \(Y\)-vertex once. Their endpoints are fixed row by row,
so they are the desired port factor. \(\square\)

### Equivalent two-matching form

The same completion can be stated with two ordinary perfect matchings:

\[
\begin{aligned}
 M^\uparrow_{\rm rem}:&
 \binom Js\setminus({\cal D}\cup\overline{\cal D})
 \longleftrightarrow
 \binom J{s+1}\setminus{\cal T}_0,\\
 M^\downarrow_{\rm rem}:&
 \binom J{s+1}\setminus{\cal T}_0
 \longleftrightarrow
 \binom Js\setminus({\cal D}\cup{\cal S}_1).
\end{aligned}
\tag{6.7}
\]

Both sides in each line have \((s-1)B\) vertices. Edges are containments.
After adjoining the fixed incidences

\[
                         P-Y_0(P)-X_1(P),
\tag{6.8}
\]

the union must have no cycle and must join every \(P\) to
\(\overline P\). Thus ordinary Hall inequalities for the two matchings are
necessary, and sufficient for the two ownership ledgers, but complement
monodromy remains an additional exact condition.

## 7. A sufficient Ordered-Hall completion theorem

Let \(\vec G_\epsilon\) be a directed support containing the fixed arcs
(6.8), allowed up-arcs \(X\to Y\), and allowed down-arcs \(Y\to X\).
Assume:

1. \(\vec G_\epsilon\) is acyclic;
2. the two residual bipartite graphs in (6.7) satisfy all Hall
   inequalities;
3. every root reaches its own complement;
4. in the root-to-complement reachability graph, the complement matching
   is the unique perfect matching.

### Theorem 7.1

Under Conditions 1--4, the prescribed balanced entrances extend to an
exact \(D_s\)-port path factor.

### Proof

Hall gives the two residual perfect matchings. Adjoin (6.8). Every
nonendpoint \(X\)-vertex has one outgoing up-edge, every nonroot
\(X\)-vertex has one incoming down-edge, and every \(Y\)-vertex has one of
each. Acyclicity excludes a closed internal component, so the selected
arcs form a path cover from the Dyck roots to the complementary endpoints.

The induced endpoint matching is a perfect matching in the reachability
graph. Condition 4 forces it to be the prescribed complement matching.
There are \(B\) paths and exactly \(2sB\) selected incidence edges. Every
root-to-complement path has at least \(2s\) incidence edges, so all paths
have exactly \(2s\). They are geodesic and exhaust both shores. \(\square\)

This theorem is sufficient rather than necessary; its purpose is to make a
constructive completion certificate finite and auditable.

## 8. Exact remaining lemma

The growing first-edge problem is reduced to the following integral
statement.

> **BCF\(_s\).** The balanced first-entrance hypergraph \({\cal E}_s\)
> has an integral matching satisfying (4.2), and one such matching admits
> either the residual exact cover of Theorem 6.1 or an Ordered-Hall support
> satisfying Theorem 7.1.

Theorem 3.1 proves the full fractional analogue of BCF\(_s\), including
the endpoint pairing, because it averages actual complete port factors.
Theorem 4.1 proves its rootwise integral label projection. Neither theorem
rounds the shared \(X/Y\) resources.

Accordingly:

* the Catalan quotas are exact and floor-free at pair level;
* their only coordinate rounding is the explicit parity in (4.4);
* there is no fractional ownership or completion deficit;
* a generic probabilistic or TU assertion is not being assumed;
* the unresolved step is correlated integral selection in (5.2), followed
  by complement-monodromy control.
