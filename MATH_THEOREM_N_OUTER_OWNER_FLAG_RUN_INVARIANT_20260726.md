# Outer adjacent-deletion flags: exact memory circulation, symmetric fractional feasibility, and the common run-count obstruction

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or
web input is used.

## 0. Outcome

Put

\[
 V=[2m],\qquad
 \mathcal M=\binom Vm,\qquad
 W=|\mathcal M|=\binom{2m}m.                         \tag{0.1}
\]

An outer owner successor is one permutation \(P\in\operatorname {Sym}(\mathcal
M)\) whose edges are Johnson edges. It is \(H\)-safe when every first
\(j\le H\) transitions from every cyclic start form a geodesic. Then

\[
 P^jX=X\setminus A_j(X)\ \cup\ B_j(X),\qquad
 |A_j(X)|=|B_j(X)|=j,                               \tag{0.2}
\]

where \(A_j(X)\subset X\), \(B_j(X)\subset X^c\), and both families are
nested. Its literal signed targets are

\[
 L_j(X)=\bigcap_{i=0}^jP^iX=X\setminus A_j(X),\qquad
 U_j(X)=\bigcup_{i=0}^jP^iX=X\cup B_j(X).            \tag{0.3}
\]

For

\[
 N_j=\binom{2m}{m-j},\qquad
 W=c_jN_j+\rho_j,\qquad
 c_j=\left\lfloor{W\over N_j}\right\rfloor,          \tag{0.4}
\]

the sharp quota-balanced demand is

\[
 \mu_j^-(S):=\#\{X:L_j(X)=S\}\in\{c_j,c_j+1\},       \tag{0.5}
\]

\[
 \mu_j^+(T):=\#\{X:U_j(X)=T\}\in\{c_j,c_j+1\}        \tag{0.6}
\]

at every \(j\le H\). The same \(P\) must satisfy all depths and both signs.

This note proves four exact conclusions.

1. Prescribed lower and upper SCD/nested-flow flags arise from one owner
   permutation if and only if their induced middle maps obey the semigroup
   identities

   \[
                            R_j=R_1^j.                \tag{0.7}
   \]

   Separate depthwise matching, separate lower/upper flow, and even
   bijectivity of every \(R_j\) do not imply (0.7).

2. The complete problem has an exact integral circulation formulation on
   \(H\)-step safe Johnson paths. The root rows, memory-overlap rows, and
   every signed quota row occur in one system. Averaging all coordinate
   conjugates of one wreath cycle gives a symmetric fractional solution
   with target load exactly \(W/N_j\) at every depth. Thus there is no
   fractional Hall obstruction.

3. Every integral solution has one common coordinate run vector

   \[
                            R=(R_v:v\in V),\qquad
                            \sum_vR_v=W,              \tag{0.8}
   \]

   which controls all signed point margins:

   \[
   \boxed{
   \sum_{S\ni v}\mu_j^-(S)={W\over2}-jR_v,\qquad
   \sum_{T\ni v}\mu_j^+(T)={W\over2}+jR_v.}          \tag{0.9}
   \]

   If \(\mathcal H_j^\pm\) are the \(\rho_j\) targets receiving the high
   quota \(c_j+1\), and \(h_{j,v}^\pm\) are their point degrees, then

   \[
   \boxed{
   h_{j,v}^-=
   {(m-j)\rho_j\over2m}
   -j\left(R_v-{W\over2m}\right),}                  \tag{0.10}
   \]

   \[
   \boxed{
   h_{j,v}^++h_{j,v}^-=\rho_j.}                     \tag{0.11}
   \]

   Hence all high-quota designs at all depths must lie on one affine
   integer line indexed by the same \(R_v\).

4. Exact quota balance is false as a universal theorem. For

   \[
                            m=3,\qquad H=2,           \tag{0.12}
   \]

   every depth-two lower singleton load equals \(10-2R_v\), hence is
   even. Balance would require loads \(3\) or \(4\); all six would have to
   be \(4\), whose sum is \(24\ne W=20\). Therefore

   \[
   \boxed{\text{no \(2\)-safe owner permutation on }\binom{[6]}3
          \text{ has balanced depth-two intersections}.}       \tag{0.13}
   \]

This counterexample closes an exact recursion claimed uniformly in \(m,H\),
including every SCD-promotion, Gray-surgery, or overlap-matching
implementation. It does **not** prove a Gaussian asymptotic no-go. The
surviving constant-one target is an integral near-balanced rounding of the
memory circulation, allowing \(o(W)\) aggregate target deficit and
\(o(W/H)\) cycles; the arithmetic obstruction above may then be absorbed.

## 1. Geodesic flags are exactly the required first swaps

For a Johnson edge \(Y\to PY\), write

\[
 \alpha(Y)=Y\setminus PY,\qquad
 \beta(Y)=PY\setminus Y.                             \tag{1.1}
\]

Both are singletons, which we identify with their coordinates. For a start
\(X\), put

\[
 A_j(X)=\{\alpha(P^iX):0\le i<j\},\qquad
 B_j(X)=\{\beta(P^iX):0\le i<j\}.                   \tag{1.2}
\]

### Lemma 1.1 (exact geodesic criterion)

For fixed \(X\) and \(j\), the following are equivalent.

1. \(d_J(X,P^jX)=j\).
2. The displayed \(j\)-edge \(P\)-path is geodesic.
3. The deleted coordinates in (1.2) are \(j\) distinct elements of \(X\),
   and the added coordinates are \(j\) distinct elements of \(X^c\).

Under these conditions, (0.2)--(0.3) hold.

#### Proof

The path has length \(j\), so equality of endpoint distance and length is
equivalent to geodesicity. A shortest Johnson path from \(X\) never
re-adds a deleted coordinate and never deletes a newly added coordinate:
either event would spend two transitions without increasing endpoint
distance. Thus its deletions are distinct members of \(X\), and its
additions are distinct members of \(X^c\). Conversely, such a path ends at
\(X\setminus A_j\cup B_j\), whose Johnson distance from \(X\) is \(j\).

Every element of \(X\setminus A_j\) persists through the whole path, while
each member of \(A_j\) is absent after its deletion. No added coordinate
belongs to the initial state. This proves the intersection identity.
The union identity is dual. \(\square\)

The criterion must hold cyclically, including starts crossing every cycle
cut. Equivalently, any coordinate used as either endpoint of a swap cannot
be used again within the next \(H-1\) transitions.

The flags also satisfy the exact cocycle identities

\[
 A_{j+k}(X)=A_j(X)\ \dot\cup\ A_k(P^jX),            \tag{1.3}
\]

\[
 B_{j+k}(X)=B_j(X)\ \dot\cup\ B_k(P^jX)             \tag{1.4}
\]

whenever \(j+k\le H\).

## 2. The semigroup obstruction to post hoc SCD promotion

Suppose independently of \(P\) that every owner \(X\) has prescribed flags

\[
 X=L_0^*(X)\supset L_1^*(X)\supset\cdots\supset L_H^*(X),        \tag{2.1}
\]

\[
 X=U_0^*(X)\subset U_1^*(X)\subset\cdots\subset U_H^*(X),        \tag{2.2}
\]

with one deletion and one addition at each step. Write

\[
 A_j^*(X)=X\setminus L_j^*(X),\qquad
 B_j^*(X)=U_j^*(X)\setminus X,                                  \tag{2.3}
\]

and define the induced middle maps

\[
 R_j(X)=X\setminus A_j^*(X)\ \cup\ B_j^*(X).         \tag{2.4}
\]

### Theorem 2.1 (power-consistency criterion)

One owner permutation realizes every prescribed flag through depth \(H\)
if and only if

\[
 R_1\in\operatorname {Sym}(\mathcal M),\qquad
 R_j=R_1^j\quad(0\le j\le H).                       \tag{2.5}
\]

Equivalently, if

\[
 a_j(X)=A_j^*(X)\setminus A_{j-1}^*(X),\qquad
 b_j(X)=B_j^*(X)\setminus B_{j-1}^*(X),              \tag{2.6}
\]

then, with \(P=R_1\),

\[
 a_t(PX)=a_{t+1}(X),\qquad
 b_t(PX)=b_{t+1}(X)\qquad(t<H).                     \tag{2.7}
\]

#### Proof

If \(P\) realizes the flags, then (2.4) is \(P^jX\), proving (2.5);
shifting the same trajectory by one step gives (2.7).

Conversely, (2.5) makes \(R_1\) the required owner permutation and makes
its first \(j\) transitions end at the prescribed \(R_j(X)\). The nesting
in (2.1)--(2.2), or equivalently (2.7), shows that those transitions use
the displayed distinct deletion and addition words. Lemma 1.1 then
identifies their intersections and unions with the prescribed flags.
\(\square\)

The standard layered Boolean flow proves the existence of integral flags
whose target loads are \(c_j\) or \(c_j+1\) at every depth. The SCD
construction gives one distinguished occurrence of every target and
nested coherence. Neither theorem supplies (2.5). This is the exact reason
that balancing the ranks first and applying promotion afterward is not a
valid construction.

## 3. Exact \(H\)-memory overlap circulation

Let \(\Gamma_H\) be the set of safe Johnson paths

\[
 \gamma=(X_0,X_1,\ldots,X_H)                                   \tag{3.1}
\]

of length \(H\). Put

\[
 \operatorname {pre}\gamma=(X_0,\ldots,X_{H-1}),\qquad
 \operatorname {suf}\gamma=(X_1,\ldots,X_H).        \tag{3.2}
\]

For each \(\gamma\), its depth-\(j\) targets are

\[
 L_j(\gamma)=\bigcap_{i=0}^jX_i,\qquad
 U_j(\gamma)=\bigcup_{i=0}^jX_i.                    \tag{3.3}
\]

Introduce \(z_\gamma\in\mathbb Z_{\ge0}\).

### Theorem 3.1 (integral overlap-circulation equivalence)

An \(H\)-safe owner permutation satisfying (0.5)--(0.6) exists if and only
if there is an integral solution of

\[
 \sum_{\gamma:X_0=X}z_\gamma=1
 \qquad(X\in\mathcal M),                             \tag{3.4}
\]

\[
 \sum_{\gamma:\operatorname {pre}\gamma=\sigma}z_\gamma
 =
 \sum_{\gamma:\operatorname {suf}\gamma=\sigma}z_\gamma
 \qquad(\sigma\in\Gamma_{H-1}),                     \tag{3.5}
\]

\[
 c_j\le
 \sum_{\gamma:L_j(\gamma)=S}z_\gamma
 \le c_j+1
 \qquad(S\in\tbinom V{m-j}),                        \tag{3.6}
\]

\[
 c_j\le
 \sum_{\gamma:U_j(\gamma)=T}z_\gamma
 \le c_j+1
 \qquad(T\in\tbinom V{m+j})                         \tag{3.7}
\]

for every \(j\le H\).

#### Proof

Given \(P\), take one \(H\)-window from every root \(X\). The root,
memory, and quota equations are immediate.

Conversely, (3.4) makes every \(z_\gamma\) binary and gives at most one
selected outgoing memory edge above a fixed root. Hence every memory state
has selected outdegree at most one. Equation (3.5) makes its indegree equal
to its outdegree, so the selected memory edges are vertex-disjoint directed
cycles. The shift from a selected path beginning at \(X\) enters the unique
selected path beginning at \(X_1\). Consequently

\[
                            P(X)=X_1                \tag{3.8}
\]

is a well-defined permutation of all owners, and its \(H\)-windows are
exactly the selected paths. Equations (3.6)--(3.7) give the quotas.
\(\square\)

This is a colored circulation, not an ordinary bipartite matching. Matching
the first transitions does not force the selected head path to be the path
used at its own outgoing transition; the memory equations (3.5) are the
missing constraints.

### Theorem 3.2 (exact fractional dual)

The real relaxation of (3.4)--(3.7) is feasible if and only if the following
holds. For every collection of real numbers

\[
 \alpha_X,\qquad\phi_\sigma,\qquad
 y_{j,S}^-,y_{j,T}^+                                  \tag{3.9}
\]

satisfying, for every \(\gamma\in\Gamma_H\),

\[
 \alpha_{X_0}+\phi_{\operatorname {pre}\gamma}
 -\phi_{\operatorname {suf}\gamma}
 +\sum_{j=1}^H
   \bigl(y_{j,L_j(\gamma)}^-+y_{j,U_j(\gamma)}^+\bigr)
 \ge0,                                                \tag{3.10}
\]

one has

\[
 \sum_X\alpha_X
 +\sum_{j,S}\bigl(c_jy_{j,S}^-+\max\{0,y_{j,S}^-\}\bigr)
 +\sum_{j,T}\bigl(c_jy_{j,T}^++\max\{0,y_{j,T}^+\}\bigr)
 \ge0.                                                \tag{3.11}
\]

#### Proof

For each quota row write its throughput as \(c_j+t\), with
\(0\le t\le1\). Multiply the root, memory, and quota equalities by
\(\alpha,\phi,y\). If (3.10) holds, the contribution of \(z\ge0\) is
nonnegative, while

\[
                             -ty\ge-\max\{0,y\}.       \tag{3.12}
\]

This proves necessity of (3.11). The converse is the standard separating
hyperplane/Farkas theorem applied to the nonnegative \(z\)-orthant and the
product box \(0\le t\le1\). \(\square\)

### Theorem 3.3 (symmetric fractional feasibility)

For every \(H\le m\), the relaxation in Theorem 3.2 is feasible with

\[
 \mu_j^-(S)=\mu_j^+(T)={W\over N_j}                 \tag{3.13}
\]

for every target of the appropriate rank.

#### Proof

Fix one cyclic coordinate order

\[
 \pi=(v_0,v_1,\ldots,v_{2m-1})
\]

and its wreath cycle

\[
 X_i=\{v_i,v_{i+1},\ldots,v_{i+m-1}\}
 \qquad(i\in\mathbb Z_{2m}).                         \tag{3.14}
\]

Every block of at most \(m\) transitions is geodesic. Include all
\(H\)-windows of every coordinate conjugate of this cycle with one common
weight, normalized so that every root owner has total weight one. Full
cycles give memory conservation. The symmetric group on \(V\) is
transitive on the roots and on each lower and upper target layer, so every
target at depth \(j\) has one common load. Its total load is \(W\), hence
that common value is \(W/N_j\), which lies in \([c_j,c_j+1]\). \(\square\)

Thus separate Hall cuts, including every SCD-rank Hall inequality, cannot
disprove the outer construction. The obstruction is an integral
chronology invariant.

## 4. The common run-count theorem

Decompose \(P\) into directed cycles. For a coordinate \(v\), record on
each cycle the cyclic binary word

\[
                         \epsilon_i(v)=\mathbf1_{\{v\in X_i\}}.  \tag{4.1}
\]

Define \(R_v\) invariantly as the total number of \(0\to1\) transitions
over all these cyclic words. Equivalently, it is the total number of
\(1\)-runs on the nonconstant words, the total number of transitions which
delete \(v\), and the total number which add \(v\). A cycle on which the
coordinate is constantly zero or constantly one contributes zero.

### Theorem 4.1 (all-depth signed point margins)

If \(P\) is \(H\)-safe, then every nonconstant \(0\)-run and \(1\)-run in
(4.1) has length at least \(H\), and for every \(j\le H\), (0.9) holds.
Moreover,

\[
                            \sum_{v\in V}R_v=W.       \tag{4.2}
\]

#### Proof

If \(v\) were toggled twice within at most \(H\) transitions, the
corresponding path would use one coordinate twice and would not be
geodesic. Thus all runs have length at least \(H\).

A \(1\)-run of length \(\ell\) contains exactly \(\ell-j\) starts whose
next \(j+1\) states all contain \(v\). Summing over all \(1\)-runs gives

\[
 \#\{X:v\in L_j(X)\}
 =\#\{X:v\in X\}-jR_v
 ={W\over2}-jR_v.                                  \tag{4.3}
\]

Here \(\#\{X:v\in X\}=\binom{2m-1}{m-1}=W/2\).
The zero-word calculation gives \(W/2-jR_v\) starts whose entire window
omits \(v\), so

\[
 \#\{X:v\in U_j(X)\}={W\over2}+jR_v.                \tag{4.4}
\]

Constant coordinate words on a cycle satisfy the same equations with
\(R_v=0\). Finally, each of the \(W\) owner transitions deletes one
coordinate, proving (4.2). \(\square\)

This theorem is independent of SCD choice, promotion grammar, cycle
lengths, and the method used to solve the overlap graph.

## 5. Exact quota arithmetic at all depths

Let

\[
 \mathcal H_j^-=\{S:\mu_j^-(S)=c_j+1\},\qquad
 \mathcal H_j^+=\{T:\mu_j^+(T)=c_j+1\}.             \tag{5.1}
\]

Both families have cardinality \(\rho_j\). Put

\[
 h_{j,v}^-=\#\{S\in\mathcal H_j^-:v\in S\},\qquad
 h_{j,v}^+=\#\{T\in\mathcal H_j^+:v\in T\}.          \tag{5.2}
\]

### Theorem 5.1 (common high-quota degree line)

Every quota-balanced \(H\)-safe owner permutation satisfies

\[
 h_{j,v}^-=
 {W\over2}-jR_v
 -c_j\binom{2m-1}{m-j-1},                           \tag{5.3}
\]

\[
 h_{j,v}^+=
 {W\over2}+jR_v
 -c_j\binom{2m-1}{m+j-1}.                           \tag{5.4}
\]

Equivalently, (0.10)--(0.11) hold. In particular,

\[
 h_{j,v}^-\equiv
 {W\over2}
 -c_j\binom{2m-1}{m-j-1}\pmod j,                    \tag{5.5}
\]

and for every two protected depths \(j,k\),

\[
 {\,{(m-j)\rho_j\over2m}-h_{j,v}^-\over j}
 =
 {\,{(m-k)\rho_k\over2m}-h_{k,v}^-\over k}
 =
 R_v-{W\over2m}.                                    \tag{5.6}
\]

#### Proof

At depth \(j\), the \(c_j\)-baseline contributes

\[
 c_j\binom{2m-1}{m-j-1}                             \tag{5.7}
\]

to the lower point degree of \(v\); every high target containing \(v\)
contributes one more. Equating this with (4.3) proves (5.3). The upper
proof uses (4.4).

Use \(W=c_jN_j+\rho_j\), together with

\[
 \binom{2m-1}{m-j-1}={m-j\over2m}N_j,\qquad
 \binom{2m-1}{m+j-1}={m+j\over2m}N_j,               \tag{5.8}
\]

to obtain (0.10) and

\[
 h_{j,v}^+={(m+j)\rho_j\over2m}
 +j\left(R_v-{W\over2m}\right).                     \tag{5.9}
\]

Their sum is \(\rho_j\). Reducing (5.3) modulo \(j\) gives (5.5), and
solving (0.10) for the common centered run count gives (5.6). \(\square\)

The relation \(h^-+h^+=\rho_j\) says that the two signs are complementary
at the point-margin level. It does not assert that the actual high-target
families are setwise complements.

### Corollary 5.2 (residual arithmetic cut)

Write

\[
                         W=2mr+s,\qquad0<s<2m.       \tag{5.10}
\]

Then exact balance at depth \(j<m\) requires

\[
 \boxed{
 \rho_j\ge
 \max\left\{
 \left\lceil{j(2m-s)\over m-j}\right\rceil,\,
 \left\lceil{js\over m+j}\right\rceil
 \right\}.}                                         \tag{5.11}
\]

In particular, if \(\rho_j=0\) at any protected depth
\(1\le j\le m-1\), then \(2m\mid W\).

#### Proof

Since the integer run counts sum to \(W\), some \(R_v\le r\) and some
\(R_w\ge r+1\). For the first coordinate,

\[
 R_v-{W\over2m}\le-{s\over2m};
\]

for the second,

\[
 R_w-{W\over2m}\ge{2m-s\over2m}.
\]

Every point degree in a family of \(\rho_j\) high targets lies between
\(0\) and \(\rho_j\). Insert the first inequality into (0.10) and use
\(h^-_{j,v}\le\rho_j\); insert the second and use
\(h^-_{j,w}\ge0\). Rearrangement gives the two terms in (5.11).

If \(\rho_j=0\), equations (0.10)--(0.11) force
\(R_v=W/(2m)\) for every \(v\), which is integral only when \(2m\mid W\).
\(\square\)

## 6. Exact counterexamples

### Theorem 6.1 (the \(m=3,H=2\) obstruction)

There is no \(2\)-safe owner permutation on \(\binom{[6]}3\) satisfying
the balanced lower quota at depth two.

#### Proof

Here

\[
 W=20,\qquad N_2=\binom61=6,\qquad
 c_2=3,\qquad\rho_2=2.                              \tag{6.1}
\]

The lower targets are the six singletons. Theorem 4.1 gives

\[
                         \mu_2^-(\{v\})=10-2R_v.     \tag{6.2}
\]

This is even. Of the two permitted loads \(3,4\), only \(4\) is even, so
all six singleton loads would be \(4\). Their total would be \(24\), but
every one of the \(W=20\) starts supplies exactly one depth-two target.
Contradiction. \(\square\)

The proof uses one sign only. Hence adding upper quotas, SCD structure, or
more overlap options cannot repair it.

### Theorem 6.2 (infinite full-depth obstruction)

Let \(m\ge3\). Exact balance at depth \(j=m-1\) forces

\[
                            2m\mid\binom{2m}m.        \tag{6.3}
\]

Consequently it fails for every odd prime \(m\).

#### Proof

At depth \(m-1\), the lower targets are singletons and

\[
 \mu_{m-1}^-(\{v\})
 ={W\over2}-(m-1)R_v
 \equiv {W\over2}\pmod{m-1}.                        \tag{6.4}
\]

All singleton loads therefore have one common residue modulo \(m-1\).
The two balanced quotas are consecutive, so for \(m-1\ge2\) they cannot
both occur. Unless their remainder is zero, both must occur to give total
load \(W\). Thus all loads are equal and \(2m\mid W\).

If \(m=p\) is an odd prime, then

\[
 \binom{2p}p
 =2\binom{2p-1}{p-1}
 =2\prod_{i=1}^{p-1}{p+i\over i}
 \equiv2\pmod p.                                    \tag{6.5}
\]

Hence \(p\nmid W\), so \(2p\nmid W\). \(\square\)

Theorem 6.2 is a full-depth obstruction; it does not apply to the desired
Gaussian regime \(H=o(m)\). Theorem 6.1 is enough to refute a universal
exact recursion, but not an eventual asymptotic theorem.

## 7. Exact SCD-promotion obstruction

The traces of an \(H\)-safe \(P\) themselves carry a useful promotion
recursion. For \(q<H\),

\[
 L_{q+1}(X)=L_q(X)\cap L_q(PX),\qquad
 U_{q+1}(X)=U_q(X)\cup U_q(PX).                    \tag{7.1}
\]

If the successive deleted and added coordinates from \(X\) are
\(a_1,a_2,\ldots\) and \(b_1,b_2,\ldots\), then

\[
 L_q(PX)=L_q(X)\setminus\{a_{q+1}\}\cup\{b_1\},     \tag{7.2}
\]

\[
 U_q(PX)=U_q(X)\setminus\{a_1\}\cup\{b_{q+1}\}.     \tag{7.3}
\]

Thus the rank-\((m-q)\) occurrence digraph has one arc

\[
                         L_q(X)\longrightarrow L_q(PX)           \tag{7.4}
\]

per owner, colored by its common facet \(L_{q+1}(X)\). It is Eulerian:
the indegree and outdegree of a target \(T\) both equal
\(\mu_q^-(T)\). The upper occurrence digraph is the dual construction.
These one-step Eulerian identities are necessary but do not themselves
select a symmetric-chain transversal.

For each \(q\), form the bipartite occurrence multigraph
\(\mathcal G_q(P)\). Its lower vertices are the rank-\((m-q)\) targets,
its upper vertices are the rank-\((m+q)\) targets, and owner \(X\) gives
the edge

\[
                         L_q(X)\ --\ U_q(X).          \tag{7.5}
\]

### Theorem 7.1 (laminar trace-contained central-band criterion)

The traces of \(P\) contain a symmetric-chain partition of the complete
central band of ranks \(m-H,\ldots,m+H\) if and only if there are variables

\[
                         y_{X,q}\in\{0,1\}            \tag{7.6}
\]

such that

\[
 y_{X,0}=1,\qquad y_{X,q+1}\le y_{X,q},              \tag{7.7}
\]

and, for every target at every depth,

\[
 \sum_{X:L_q(X)=S}y_{X,q}=1,\qquad
 \sum_{X:U_q(X)=T}y_{X,q}=1.                         \tag{7.8}
\]

In particular, \(\mathcal G_q(P)\) must contain a perfect matching for
every \(q\). Its exact one-depth obstruction is

\[
 \delta_q(P)=
 \max_{\mathcal A}
 \bigl(|\mathcal A|-|N_{\mathcal G_q(P)}(\mathcal A)|\bigr)_+.   \tag{7.9}
\]

#### Proof

Given (7.6)--(7.8), put

\[
                         r_X=\max\{q:y_{X,q}=1\}.     \tag{7.10}
\]

The chain

\[
 L_{r_X}(X)\subset\cdots\subset L_1(X)\subset X
 \subset U_1(X)\subset\cdots\subset U_{r_X}(X)       \tag{7.11}
\]

is saturated and symmetric. Equation (7.8) says that these chains contain
every set at every rank \(m-H,\ldots,m+H\) exactly once. Conversely, every
such central-band chain partition defines \(y_{X,q}=1\) precisely when
the chain centered at \(X\) reaches depth \(q\). The monotonicity and
equations follow. At fixed \(q\), the selected owner edges are exactly a
perfect matching of (7.5), and Hall's theorem gives (7.9). \(\square\)

The matchings must be laminar in owner edges. Vanishing of every
\(\delta_q(P)\) separately is not sufficient for (7.7).

### Corollary 7.2 (unit-floor component invariant)

Assume \(c_q=1\) and both raw signed histograms at depth \(q\) are balanced.
Then every vertex of \(\mathcal G_q(P)\) has degree one or two, so every
component is an alternating path or an even cycle. Moreover,

\[
 \delta_q(P)=
 \#\{\text{path components whose two endpoints are lower vertices}\}.
                                                               \tag{7.12}
\]

This equals the number of path components whose two endpoints are upper
vertices. Hence a perfect matching exists if and only if every path has
one endpoint on each shore.

If deeper owner edges have already been prescribed, a path component can
extend them only when all prescribed edges lie in its unique alternating
perfect matching. In an even cycle, they must all lie in one common
alternating parity class. These are the exact cross-depth parity conflicts
left after all one-depth Hall deficiencies vanish.

#### Proof

A bipartite graph of minimum degree one and maximum degree two has only the
stated components. An alternating path with two lower endpoints has one
more lower than upper vertex and contributes Hall deficiency one; every
other component contributes zero to the lower-shore deficiency. Equality
of the two shore sizes forces the number of lower--lower and upper--upper
paths to agree. The matching and extension statements follow from the
unique alternating matching of a path and the two alternating matchings
of an even cycle. \(\square\)

### Proposition 7.3 (balanced marginals do not imply SCD promotion)

On the six owners \(\binom{[4]}2\), define

\[
                         P=(13,12,23,34)(14,24),      \tag{7.13}
\]

where, for example, \(13=\{1,3\}\). This is a Johnson permutation. Its
six depth-one \((L_1,U_1)\)-colors are

\[
 (1,123),(2,123),(3,234),(3,134),(4,124),(4,124).    \tag{7.14}
\]

Both marginals are exactly balanced: the lower loads are
\((1,1,2,2)\), and the upper loads are \((2,2,1,1)\). Nevertheless, the
two lower vertices \(1,2\) have the single common neighbor \(123\).
Therefore

\[
                         \delta_1(P)\ge1,             \tag{7.15}
\]

and no depth-one trace-contained two-sided central-band transversal exists.

This is independent of the run-count obstruction: it shows that even a
permutation whose two signed quota histograms are perfect need not admit
the trace-contained central-band SCD owner selection needed by promotion.
No extension of an arbitrary selected central-band partition through the
outer Boolean ranks is asserted.

## 8. Consequences for the proposed construction routes

### 8.1 SCD promotion

An SCD or the uniform Boolean layered flow supplies nested flags and
excellent marginal quotas. To become one owner successor, those flags must
also satisfy Theorem 2.1. Every resulting promotion permutation must then
satisfy the common run equations (0.9)--(0.11). The \(m=3\) obstruction
shows that no choice of SCD, extension, or promotion rule can establish the
exact theorem in all dimensions.

Theorem 7.1 adds a second requirement: even if the raw traces are
quota-balanced, their paired occurrences must satisfy the laminar Hall
system (7.6)--(7.8).

### 8.2 Overlap matching

The correct overlap object is the \(H\)-memory circulation
(3.4)--(3.7), not the bipartite graph of first successors. Theorem 3.3
proves every fractional cut feasible. Any positive result must therefore
round a highly non-TU colored circulation while preserving the common
integer run vector and all quota rows. Ordinary Hall matching omits the
memory potentials in (3.10).

### 8.3 Gray-code surgery

Suppose \(P'\) is obtained from \(P\) by changing the outgoing transition
at \(s\) owner tails, while remaining a permutation. At depth \(j\), only
the \(j\) cyclic starts whose windows contain a changed transition can be
altered per changed tail. Therefore at most \(js\) lower targets and
\(js\) upper targets can be lost. If

\[
 \Delta_H(P)=\sum_{j=1}^H
   \bigl(M_j^-(P)+M_j^+(P)\bigr)                    \tag{8.1}
\]

is the aggregate signed number of missing targets, then

\[
 \boxed{
 \Delta_H(P')\le\Delta_H(P)+sH(H+1).}               \tag{8.2}
\]

Thus generic surgery on \(s\) edges preserves the all-depth
\(o(W)\)-deficit gate only under \(sH^2=o(W)\). The weaker seam estimate
\(sH=o(W)\) is insufficient unless the surgery preserves the signed target
multisets more exactly.

### 8.4 Exact surviving boundary

The exact floor/ceiling problem is arithmetically false, but exact balance
is stronger than the constant-one compiler needs. A viable theorem may
allow:

1. an owner leave \(o(W)\);
2. aggregate signed target deficit \(o(W)\);
3. \(o(W/H)\) owner cycles, so the \(2H\)-per-cycle linearization toll is
   \(o(W)\); and
4. all remaining cyclic windows \(H\)-safe.

The symmetric fractional solution shows that this target is not blocked by
any linear Hall dual. The missing theorem is an integral rounding or
algebraic construction for (3.4)--(3.7), with approximate quotas and few
cycles, that respects the common run vector (0.8). No such rounding is
proved here.

For the odd ambient middle layer \(\binom{[2m+1]}m\), the geodesic,
semigroup, and memory-circulation theorems are unchanged. The two signed
layer sizes are no longer equal:

\[
 N_j^-=\binom{2m+1}{m-j},\qquad
 N_j^+=\binom{2m+1}{m+j}=N_{j-1}^-,
\]

so the symmetric point formulas (0.9)--(0.11) must be replaced by their
separate lower/upper versions. No odd-ambient arithmetic obstruction is
claimed by this note.

An independent audit rederived the run formulas, the absence of a factor
two in \(\sum_vR_v=W\), the residual constants in (5.11), both finite
counterexamples, the memory-circulation equivalence, and the
Hoffman--Farkas sign in (3.11). It also verified that Theorem 7.1 has
exactly the stated central-band scope and no unproved full-SCD extension.
