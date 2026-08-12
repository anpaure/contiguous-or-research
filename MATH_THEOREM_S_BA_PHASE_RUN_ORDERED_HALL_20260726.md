# Phase-varying nested-star rotors: exact ordered-Hall factorization and the critical (BA)-run gate

Date: 2026-07-26

Method: pure mathematics only.  No computation, finite search, solver, or
external input is used.

## 0. Exact outcome

Put

\[
 n=2m+1,\qquad W=\binom{n}{m},\qquad C=BA,\qquad L=m(m+1).
\tag{0.1}
\]

The fixed-three-orbit packet is not the correct integral object.  There
are two separate issues: factor the selected (A)-sources into legal
nested-star atoms, and join their (A)-successors to later sources.  This
note separates them exactly.

1. There is an explicit phase-varying atom factor of the full permutation
   catalogue.  It is given by the positional three-cycle on positions
   (1,2,n), and every one of its atoms is legal through all depths.
   Thus the fixed-three-(BA)-orbit obstruction is not a local atom
   obstruction.

2. That particular factor cannot be sparsified while retaining exact
   (BA)-flow.  Its positional three-cycle together with (C) generates
   (S_n), so an integral source set invariant under both is empty or the
   entire (n!)-state catalogue.  The full choice has middle-owner load
   (2m!(m+1)!).

3. For an arbitrary source inventory, legal protected atoms have an exact
   integral ordered-Hall characterization.  In each protected suffix
   flag, the only variables are cyclic directed-triangle quotas
   (w_{abc}).  Besides the arc margins, the only state-to-corner Hall
   cuts are

   \[
       n_{ab,r}+w_{abr}\le N_{ab}.
   \tag{0.2}
   \]

   This is an if and only if, not a fractional relaxation.

4. Exact (BA)-flow is unnecessary for a path cover.  If (S) is the
   source set, keep (e\to Ae) and keep (Ae\to Ce) precisely when
   (Ce\in S).  In this forced alternating (A)/(B) subgraph, the resulting
   components are the cyclic (C)-runs of (S), and their exact path-cover
   number is

   \[
     \boxed{
     p_C(S)=\frac12|S\mathbin\triangle CS|+f_C(S),}
   \tag{0.3}
   \]

   where (f_C(S)) is the number of whole (C)-orbits contained in
   (S).  Formula (0.3) also has an exact split-copy ordered-Hall form.

5. The phase boundary cannot be smaller than order (W/m) in a bulk
   all-depth use.  For even (m), owner simplicity gives

   \[
      \Delta_C(S)\ge \frac{2|S|}{2(m+1)}
      =\frac{|S|}{m+1}.
   \tag{0.4}
   \]

   For odd (m), if the atom module occupies (U=2|S|) middle cells and
   the whole construction misses (h) immediate lower targets, then

   \[
      \boxed{
      (m+1)\Delta_C(S)
      \ge \frac U2-\frac{2W}{m+2}-h.}
   \tag{0.5}
   \]

   Hence (U=(1-o(1))W) and (h=o(W)) force
   (Delta_C(S)\ge(1/2-o(1))W/m).

6. This lower bound is compatible with the constant-one component
   ledger whenever (H=o(m)).  On a single (C)-orbit there are exact
   owner-simple blocks of (m+1) consecutive phases with one boundary
   per block.  The remaining gate is global and integral: select such
   long runs across many orbits, obey every owner row, and satisfy the
   flagwise triangle quotas simultaneously inside one SCD/collar
   catalogue.

Thus exact full-orbit (BA)-flow is closed as a bulk compiler, but the
noncomplete-run ordered-Hall route is not closed.  The new exact target is
a source set with

\[
  W-2|S|=o(W/H),\qquad p_C(S)=o(W/H),
\tag{0.6}
\]

together with the owner equations and the flagwise conditions below.
No such global source set or SCD is constructed here.

## 1. States, owners, flags, and legal atoms

Write a permutation state as

\[
 e=(x_1,\ldots,x_n)=(a,P,\mathbf K,b),
\tag{1.1}
\]

where (a=x_1), (b=x_n), (P=(x_2,\ldots,x_{m+1})), and

\[
 \mathbf K=(x_{m+2},\ldots,x_{n-1}).
\tag{1.2}
\]

Let (K) denote the underlying ((m-1))-set of (mathbf K), and put

\[
  \kappa(e)=\{x_1,\ldots,x_m\},\qquad
  \kappa(Ae)=\{x_2,\ldots,x_{m+1}\}.
\tag{1.3}
\]

For (0\le H\le m-1), the protected flag is

\[
 \Phi_H(e)=(K;x_{m+2},\ldots,x_{m+1+H}).
\tag{1.4}
\]

The boundary label is

\[
                         r(e)=x_{m+1}.
\tag{1.5}
\]

For a fixed flag (F), let

\[
                    Q_F=[n]\setminus K(F),\qquad |Q_F|=m+2.
\tag{1.6}
\]

Every state of flag (F) has (a,b,r(e)\in Q_F), pairwise distinct.
A protected nested-star atom is a triple

\[
 e_{ab},\quad e_{bc},\quad e_{ca}
\tag{1.7}
\]

with a common flag, three distinct endpoints (a,b,c), and

\[
 r(e_{ab})\ne c,\qquad r(e_{bc})\ne a,\qquad r(e_{ca})\ne b.
\tag{1.8}
\]

The already proved nested-star identity says that (1.7)--(1.8) gives
three legal (A)-switches whose signed lower/upper divergences cancel at
every protected depth.  Its six source/successor owners are distinct
inside the atom.

For a proposed source set (S), define its owner load by

\[
 u_X(S)=\sum_{e\in S}
 \left(
  {\mathbf 1}_{\{\kappa(e)=X\}}+{\mathbf 1}_{\{\kappa(Ae)=X\}}
 \right).
\tag{1.9}
\]

The exact owner equations are

\[
 u_X(S)\le1\quad\left(X\in\binom{[n]}m\right),
 \qquad
 \ell=W-\sum_Xu_X(S)=W-2|S|.
\tag{1.10}
\]

No cancellation is permitted in (1.10): it is literal owner simplicity.

## 2. An explicit full-catalogue phase factor

Define the positional map

\[
 \Psi(x_1,x_2,x_3,\ldots,x_{n-1},x_n)
   =(x_n,x_1,x_3,\ldots,x_{n-1},x_2).
\tag{2.1}
\]

It is the pullback three-cycle (\rho=(1\ n\ 2)), so
(Psi^3=1).

### Theorem 2.1 (literal all-depth phase factor)

For every (m\ge2), the (Psi)-orbits partition all (n!)
permutation states into legal canonical nested-star atoms.  Each atom is
legal at every protected height (0\le H\le m-1).

#### Proof

Put

\[
 a=x_1,\qquad c=x_2,\qquad b=x_n.
\]

The endpoint edges of (e,\Psi e,\Psi^2e) are respectively

\[
                   a\to b,\qquad b\to c,\qquad c\to a.
\tag{2.2}
\]

The positions (m+2,\ldots,n-1) are fixed by (Psi), so the three
states have the same full ordered suffix.  Their (P)-blocks are

\[
 (c,x_3,\ldots,x_{m+1}),\quad
 (a,x_3,\ldots,x_{m+1}),\quad
 (b,x_3,\ldots,x_{m+1}).
\tag{2.3}
\]

All end in the same label (r=x_{m+1}), and
(r\notin\{a,b,c\}).  Thus (1.8) holds at all depths.  Since the labels
are distinct, (Psi) has no fixed state.  Its orbits all have size
three and partition the catalogue. (square)

The theorem is a full-density state factor, not an owner factor.  Put

\[
                         D_0=m!(m+1)!.
\tag{2.4}
\]

Across all permutation states, every middle owner occurs (D_0) times
as a source owner and (D_0) times as a successor owner.  Hence the
full factor has load (2D_0) at every owner.

There is an exact fractional point: give every (C)-orbit and every
(Psi)-atom weight

\[
                         \frac1{2D_0}.
\tag{2.5}
\]

Every state-port equation and every owner equation then holds.  The next
theorem explains why this particular point has no nonzero integral sparse
rounding.

### Theorem 2.2 (the fixed positional factor is indivisible)

Let (sigma) be the pullback position permutation of (C).  Then

\[
 \sigma=(1,3,\ldots,2m-1)(2,4,\ldots,2m,n),
\tag{2.6}
\]

and

\[
                         \langle\sigma,\rho\rangle=S_n.
\tag{2.7}
\]

Consequently, a source set which is both a union of (Psi)-atoms and
exactly (C)-invariant is empty or the full state catalogue.

#### Proof

Write the two position cycles in (2.6) as

\[
 O_i=\sigma^i(1)\quad(i\in\mathbb Z_m),\qquad
 Q_j=\sigma^j(2)\quad(j\in\mathbb Z_{m+1}).
\]

Since (n=Q_m), the conjugates of (\rho) are

\[
 \sigma^t\rho\sigma^{-t}
   =(O_i,Q_{j-1},Q_j).
\tag{2.8}
\]

The Chinese remainder theorem makes ((i,j)) range independently over
(mathbb Z_m\times\mathbb Z_{m+1}).  For fixed (O_0), the cycles
((O_0,Q_{j-1},Q_j)) along a spanning path of the (Q)-vertices
generate the alternating group on ({O_0}\cup\{Q_j}).  This follows
inductively: (A(T)) together with a three-cycle containing two points
of (T) and one new point generates the alternating group on the enlarged
set.  The cycles ((O_i,Q_0,Q_1)) then adjoin the remaining (O_i)'s
one at a time.  Thus the conjugates generate (A_n).

The sign of (sigma) is

\[
 (-1)^{m-1}(-1)^m=-1,
\]

so adjoining (sigma) gives (S_n), proving (2.7).  A union of
(Psi)-atoms is (\rho)-invariant, and exact (C)-flow is
(sigma)-invariance.  Position permutations act transitively on the
permutation states, so simultaneous invariance gives the empty or full
catalogue. (square)

The statement concerns this one fixed positional factor.  It does not
rule out state-dependent atom partners; those are characterized next.

## 3. Exact flagwise ordered-Hall factorization

Fix an arbitrary source set (S) and a protected flag (F).  For
distinct (a,b,r\in Q_F), let

\[
 n^F_{ab,r}
 =\#\{e\in S:\Phi_H(e)=F, (a(e),b(e),r(e))=(a,b,r)\},
\tag{3.1}
\]

and put

\[
                         N^F_{ab}=\sum_{r\notin\{a,b\}}n^F_{ab,r}.
\tag{3.2}
\]

### Theorem 3.1 (integral directed-triangle transportation)

The states of (S) with flag (F) partition into protected nested-star
atoms if and only if there are nonnegative integers

\[
 w^F_{abc}=w^F_{bca}=w^F_{cab}
\tag{3.3}
\]

for every ordered triple of distinct points of (Q_F), with variables
identified under cyclic rotation as in (3.3), such that

\[
 \boxed{
 \sum_{c\in Q_F\setminus\{a,b\}}w^F_{abc}=N^F_{ab}}
 \qquad(a\ne b),
\tag{3.4}
\]

and

\[
 \boxed{
 n^F_{ab,r}+w^F_{abr}\le N^F_{ab}}
 \qquad(r\in Q_F\setminus\{a,b\}).
\tag{3.5}
\]

#### Proof: necessity

Let (w^F_{abc}) count atoms whose oriented endpoint triangle is

\[
                         a\to b\to c\to a.
\]

Cyclic rotation does not change the atom, proving (3.3).  Every state on
the arc (a\to b) belongs to exactly one such triangle, proving (3.4).
A state of boundary type (r) cannot use (r) as its third endpoint.
Therefore the (w^F_{abr}) slots with third endpoint (r) must be filled
by the (N^F_{ab}-n^F_{ab,r}) other states.  This is (3.5).

#### Proof: sufficiency

Fix one ordered arc (a\to b).  On the left make
(n^F_{ab,r}) individual state tokens of type (r).  On the right make
(w^F_{abc}) third-endpoint slots of type (c).  Join a token of type
(r) to a slot of type (c) exactly when (r\ne c).

This is a complete bipartite graph with the type-diagonal deleted.  The
two shores have equal size by (3.4).  Its capacitated Hall inequalities
reduce exactly to

\[
                   w^F_{abr}\le N^F_{ab}-n^F_{ab,r}.
\tag{3.6}
\]

Indeed, an arbitrary subset of slots all of one type (r) is dominated by
the full-type inequality (3.6).  Any set containing at least two slot
types sees every token, because a token forbids only its own type.  Thus
an integral perfect matching exists.

Perform this matching independently for every ordered arc.  For each
oriented triangle, label its (w^F_{abc}) matched slots consistently on
the three arcs (ab,bc,ca), and group equal labels.  Every group is a
triple satisfying (1.7)--(1.8), and all states are used once. (square)

### Corollary 3.2 (exact atom criterion for (S))

The whole set (S) partitions into protected atoms if and only if the
integer system (3.3)--(3.5) is feasible independently for every flag
(F).

No compatibility between distinct flags is needed.  In particular,
fixed orbit partners are unnecessary: a source can use different partner
orbits at every phase.

### 3.1 Useful exact cuts

For every feasible flag inventory,

\[
 \sum_bN^F_{ab}=\sum_bN^F_{ba}\qquad(a\in Q_F),
 \qquad
 3\mid\sum_{a\ne b}N^F_{ab}.
\tag{3.7}
\]

The first equation is endpoint Euler balance and the second counts three
arcs per triangle.

Fix a total order (<) on (Q_F), and write

\[
 M_F=\sum_{a\ne b}N^F_{ab},\qquad
 E_F^<=\sum_{a<b}N^F_{ab}.
\]

Every oriented triangle has one or two forward arcs, so

\[
                    \frac{M_F}{3}\le E_F^<\le\frac{2M_F}{3}.
\tag{3.8}
\]

The boundary marks give a sharper triangle capacity.  Put

\[
 U^F_{abc}=\min\left\{
 N^F_{ab}-n^F_{ab,c},
 N^F_{bc}-n^F_{bc,a},
 N^F_{ca}-n^F_{ca,b}
 \right\}.
\tag{3.9}
\]

Then

\[
              N^F_{ab}\le\sum_{c\notin\{a,b\}}U^F_{abc}.
\tag{3.10}
\]

More generally, the fractional relaxation of the triangle-quota system
is feasible if and only if, for every real arc weighting
(\theta=(\theta_{ab})),

\[
 \sum_{a\ne b}\theta_{ab}N^F_{ab}
 \le
 \sum_{\tau}U^F_\tau
       \left(\sum_{ab\in\tau}\theta_{ab}\right)_+,
\tag{3.11}
\]

where (\tau) ranges over oriented triangles.  This is the support-function
description of

\[
 \left\{\sum_\tau x_\tau{\bf1}_\tau:0\le x_\tau\le U^F_\tau\right\}.
\]

Equation (3.11) is only the exact *fractional* dual.  The integral theorem
is (3.3)--(3.5); no total-unimodularity claim is made for the triangle
incidence matrix.

### 3.2 Check on the full catalogue

For the full state catalogue and a fixed flag, put

\[
                         t_H=(m-1)!(m-1-H)!.
\tag{3.12}
\]

Then

\[
 n^F_{ab,r}=t_H,\qquad N^F_{ab}=m t_H.
\tag{3.13}
\]

The uniform choice

\[
                         w^F_{abc}=t_H
\tag{3.14}
\]

satisfies (3.4), and (3.5) becomes (2t_H\le mt_H).  This gives a
second proof of the full-density factor for (m\ge2), now in the exact
transportation normal form.

## 4. The exact (C)-run path cover

Assume (1.10) and the atom criterion of Corollary 3.2.  Keep the literal
(A)-transition

\[
                         e\longrightarrow Ae
\tag{4.1}
\]

for every (e\in S).  Whenever (Ce\in S), also keep

\[
                 Ae\longrightarrow B(Ae)=Ce.
\tag{4.2}
\]

Owner simplicity ensures that all selected state occurrences in
(4.1)--(4.2) are distinct.

Define

\[
 \Delta_C(S)=|S\setminus C^{-1}S|
             =\frac12|S\mathbin\triangle CS|,
\tag{4.3}
\]

and let (f_C(S)) be the number of (C)-orbits wholly contained in
(S).

### Theorem 4.1 (run decomposition and exact component number)

The graph (4.1)--(4.2) is the disjoint union of:

* one alternating directed path for every noncomplete cyclic (C)-run
  of (S); and
* one alternating directed cycle for every full (C)-orbit contained in
  (S).

After cutting one (B)-edge in each of the latter cycles, the minimum
path-cover component number is

\[
 \boxed{
 p_C(S)=\Delta_C(S)+f_C(S)
       =\frac12|S\mathbin\triangle CS|+f_C(S).}
\tag{4.4}
\]

#### Proof

If (e,Ce,\ldots,C^{q-1}e) is a maximal proper run, its selected states
occur in the single alternating path

\[
 e,Ae,Ce,ACe,\ldots,C^{q-1}e,AC^{q-1}e.
\tag{4.5}
\]

The exits of the proper runs are exactly
(S\setminus C^{-1}S), so their number is (Delta_C(S)).  A full
orbit has no exit and gives one directed cycle; one cut is necessary and
sufficient to make it a path.  Summing proves (4.4). (square)

### Theorem 4.2 (split-copy ordered-Hall form)

For a total order (prec) on (S), form a bipartite split graph with
left and right copies of (S), retaining

\[
                   e_L(Ce)_R
\quad\Longleftrightarrow\quad
                   Ce\in S\text{ and }e\prec Ce.
\tag{4.6}
\]

Then

\[
 \boxed{
 p_C(S)=
 \min_\prec\ \max_{\mathcal U\subseteq S}
 \bigl(|\mathcal U|-|N_\prec(\mathcal U)|\bigr).}
\tag{4.7}
\]

#### Proof

For fixed (prec), the retained edges already form a matching, because
(C) is a permutation; there is no further expansion selection hidden in
this special Hall formula.  By the deficiency form of Hall's theorem,
its matching deficiency is the inner maximum in (4.7).  Along every proper
run one may order the states in their (C)-direction and retain all
run edges.  Along a full orbit, any total order loses at least one cyclic
edge and an order loses exactly one.  Hence the minimum deficiency is one
per proper run and one per full orbit, which is (4.4). (square)

Exact (BA)-flow, (S=CS), is therefore only the zero-boundary extreme.
It is not required by the path-cover problem.

## 5. Exact owner/flag/run master theorem

### Theorem 5.1 (phase-varying alternating path systems)

Fix (m\ge3) and (0\le H\le m-1).  A set (S) supports an
owner-simple protected nested-star alternating path system if and only if:

1. the literal owner inequalities (1.10) hold;
2. for every protected flag (F), the integer quotas
   (3.3)--(3.5) are feasible.

Within the forced alternating (A)/(B) chronology (4.1)--(4.2), its exact
minimum number of paths is (p_C(S)) from (4.4).  The ambient bridge-one
digraph may contain additional promotion edges and can only lower that
number.  Conversely, the constructions in the proofs of
Theorems 3.1 and 4.1 build the atoms and the paths without changing any
owner or flag.

This is the rigorous flow/owner normal form sought in this lane.  Its
variables may be written directly as binary state variables (s_e) and
integer triangle variables (w^F_{abc}):

\[
 u_X(s)=\sum_e
 (\mathbf1_{\kappa(e)=X}+\mathbf1_{\kappa(Ae)=X})s_e\le1,
\tag{5.1}
\]

\[
 N^F_{ab}(s)=\sum_{c\notin\{a,b\}}w^F_{abc},
\tag{5.2}
\]

\[
 n^F_{ab,r}(s)+w^F_{abr}\le N^F_{ab}(s),
\tag{5.3}
\]

\[
 p=\frac12\sum_e|s_e-s_{C^{-1}e}|+f_C(s).
\tag{5.4}
\]

The factor (1/2) in (5.4) is outside the sum over all states.  Every
quantity in (5.1)--(5.4) is integral at a literal solution.

### Corollary 5.2 (conditional SCD/EP compiler)

Assume (H\ge1).  Suppose one full SCD, with radius-(H) collar
extensions, contains collar states whose literal state projections are
exactly the states (S\cup AS) of Theorem 5.1 in the required owner cells,
and suppose every retained transition (4.1)--(4.2) is therefore a
literal bridge-one edge of that collar catalogue.  Suppose
the (ell=W-2|S|) remaining SCD chains can be covered by (k_{\rm rem})
additional bridge-one paths.  Then the complete useful-state catalogue
has a bridge-one path cover with at most

\[
                         p_C(S)+k_{\rm rem}
\tag{5.5}
\]

components.  In particular, the EP target follows if

\[
 p_C(S)+k_{\rm rem}=o(W/H).
\tag{5.6}
\]

If no additional fusion of the remaining chains is available, one may
take (k_{\rm rem}=\ell).  The standard collar concatenation toll is at
most ((2H+1)(p_C+k_{\rm rem})), hence is (o(W)) under (5.6).

Corollary 5.2 is conditional.  Theorem 5.1 does not construct the one SCD
or the globally owner-disjoint source set.

## 6. The unavoidable critical phase boundary

The exact-run relaxation escapes the full-orbit contradiction, but it
cannot make its boundary arbitrarily small.

### Theorem 6.1 (even (m): middle-owner boundary law)

Let (m\ge2) be even and let (S) satisfy owner simplicity (1.10).
Then

\[
 \boxed{
 \Delta_C(S)\ge\frac{|S|}{m+1}
 =\frac{W-\ell}{2(m+1)}.}
\tag{6.1}
\]

#### Proof

For even (m), the position footprints obey

\[
        \kappa(C^{m+1}e)=\kappa(Ae)\qquad(e\in S).
\tag{6.2}
\]

If (e,C^{m+1}e\in S), (6.2) repeats one selected owner, contrary to
(1.10).  Thus

\[
                         S\cap C^{m+1}S=\varnothing.
\tag{6.3}
\]

For any permutation (C) and any (k\ge1), telescoping cyclic
boundaries gives

\[
 |S\setminus C^kS|\le k|S\setminus CS|=k\Delta_C(S).
\tag{6.4}
\]

Take (k=m+1).  The left side is (|S|) by (6.3), proving (6.1).
(square)

For odd (m), the obstruction moves to the first lower layer.  Define

\[
                         \lambda(e)=\{x_1,\ldots,x_{m-1}\}.
\tag{6.5}
\]

### Lemma 6.2 (odd (m): shifted lower footprint)

If (m\ge3) is odd, then

\[
                         \lambda(Ae)=\lambda(C^{m+1}e)
\tag{6.6}
\]

for every state (e).

#### Proof

The source lower footprint is (P^-=[m-1]), and the successor lower
footprint is (Q^-=\{2,\ldots,m\}).  On the length-(m) position cycle
of (C), exponent (m+1) is one step; on the length-((m+1)) cycle it
is zero.  Directly on the two cyclic-interval portions of (P^-), this
sends (P^-) to (Q^-). (square)

### Theorem 6.3 (odd (m): robust first-shadow boundary law)

Work in the one-sided rotor/SCD useful-state convention, in which each
middle cell carries one designated immediate-lower prefix.  Let an
owner-transversal construction use the atom source set (S) on

\[
                         U=2|S|
\tag{6.7}
\]

of its (W) middle cells, and allow the other (W-U) cells to be
arbitrary.  If (h) rank-((m-1)) lower targets are missing, then

\[
 \boxed{
 (m+1)\Delta_C(S)
 \ge \frac U2-\frac{2W}{m+2}-h.}
\tag{6.8}
\]

#### Proof

By (6.6), the atom module's lower support is at most

\[
 \begin{aligned}
 |\lambda(S\cup AS)|
 &\le |S\cup C^{m+1}S|\\
 &\le |S|+(m+1)\Delta_C(S).
 \end{aligned}
\tag{6.9}
\]

The second inequality is (6.4), with a harmless reversal of (C).
Every one of the other (W-U) middle cells supplies at most one further
immediate lower target.  Therefore total lower support is at most

\[
 W-\frac U2+(m+1)\Delta_C(S).
\tag{6.10}
\]

The target layer has size

\[
 N_1=\binom{2m+1}{m-1}=\frac{m}{m+2}W.
\tag{6.11}
\]

Requiring support at least (N_1-h) and rearranging (6.10) gives
(6.8). (square)

### Corollary 6.4 (full-orbit and near-flow consequences)

For odd (m), exact (BA)-flow has (Delta_C(S)=0).  Theorem 6.3
then gives

\[
                         U\le\frac{4W}{m+2}+2h.
\tag{6.12}
\]

Thus an exact-flow atom module with (h=o(W)) occupies only (o(W))
middle cells, regardless of its phase-varying atom partners.

More generally, if (U=(1-o(1))W) and (h=o(W)), then

\[
 \boxed{
 \Delta_C(S)\ge\left(\frac12-o(1)\right)\frac Wm.}
\tag{6.13}
\]

For even (m), (6.1) gives the same leading lower bound.  Since
(p_C(S)\ge\Delta_C(S)), a bulk use on either parity needs

\[
                         p_C(S)=\Omega(W/m).
\tag{6.14}
\]

This does not contradict (p_C(S)=o(W/H)) when (H=o(m)).

## 7. Exact critical blocks inside one (C)-orbit

The scale in Section 6 is locally attainable.

Fix a (C)-orbit

\[
                         v_j=C^jv_0\qquad(j\in\mathbb Z_L)
\]

and partition it into (m) consecutive blocks

\[
 D_b=\{v_{(m+1)b+a}:0\le a\le m\}
 \qquad(b\in\mathbb Z_m).
\tag{7.1}
\]

### Theorem 7.1 (owner-simple critical block schedule)

Let (I\subseteq\mathbb Z_m) contain no two cyclically consecutive
indices, and put

\[
                         S_I=\bigcup_{b\in I}D_b.
\tag{7.2}
\]

Then

\[
 |S_I|=(m+1)|I|,\qquad
 \Delta_C(S_I)=p_C(S_I)=|I|,
\tag{7.3}
\]

and all (2|S_I|) middle owners

\[
 \{\kappa(e),\kappa(Ae):e\in S_I\}
\tag{7.4}
\]

are distinct.  If (m) is odd, all (2|S_I|) immediate lower targets

\[
 \{\lambda(e),\lambda(Ae):e\in S_I\}
\tag{7.5}
\]

are also distinct.

#### Proof

Each selected (D_b) is one consecutive run of (m+1) states, and the
cyclic independence of (I) separates distinct selected blocks.  This
proves (7.3).

On a (C)-orbit, the source-owner map and successor-owner map are each
injective.  If (m) is odd, their images are disjoint on the whole
orbit.  If (m) is even, their only cross equality is the shift

\[
                         \kappa(A v_j)=\kappa(v_{j+m+1}).
\]

The latter moves (D_b) to (D_{b+1}), and cyclic independence excludes
simultaneous selection.  This proves (7.4).

For odd (m), the lower source map is injective on the orbit, while
Lemma 6.2 gives

\[
                         \lambda(A v_j)=\lambda(v_{j+m+1}).
\]

Again cyclic independence excludes the only cross collision, proving
(7.5). (square)

Taking (|I|=\lfloor m/2\rfloor) gives runs of exact length (m+1)
and

\[
 \Delta_C(S_I)=\lfloor m/2\rfloor,
 \qquad
 |S_I|=(m+1)\lfloor m/2\rfloor.
\tag{7.6}
\]

For even (m), this attains (6.1) with equality inside one orbit.  For
odd (m), it also removes the local twofold depth-one collision.  The
construction is deliberately only an orbitwise schedule: its states have
not been grouped with states from other orbits into nested-star atoms.

## 8. The precise surviving global gate

At (H=\sqrt m\,\omega(m)) with

\[
                         \omega(m)\to\infty,
 \qquad H=o(m),
\tag{8.1}
\]

the critical component scale satisfies

\[
                         \frac{W}{m}=o\left(\frac WH\right).
\tag{8.2}
\]

Thus the forced order-(W/m) boundary is affordable.  Equations
(3.3)--(3.5) show exactly what must be synchronized across the critical
blocks.

The surviving theorem is the following integral selection statement.

> **BA-run ordered-Hall SCD gate.**  Choose one full SCD with radius-(H)
> collar annotations and a binary source set (S) from those annotations
> such that:
>
> 1. (u_X(S)\le1) for every middle owner and
>    (W-2|S|=o(W/H)), or the remaining owners have an independent
>    (o(W/H))-component fusion;
> 2. every protected flag inventory has integer quotas satisfying
>    (3.3)--(3.5);
> 3. (p_C(S)=o(W/H));
> 4. the selected collars have aggregate missing lower and upper shadows
>    (o(W)) at all depths (q\le H).

Theorem 5.1 proves that items 1--3 are exactly the owner, atom, and flow
parts of this gate.  Theorem 7.1 supplies the correct local run scale.
No theorem here couples the orbitwise critical blocks into the one SCD or
proves item 4.  In particular:

* full-catalogue phase balance is not owner balance;
* endpoint Euler balance or histogram cancellation is not sufficient for
  the integral triangle quotas;
* the fractional dual (3.11) is not an integral completion theorem;
* exact full-orbit flow is unusable on positive density by Corollary 6.4;
* the fixed positional factor is indivisible by Theorem 2.2.

The missing object is therefore neither a fixed three-orbit packet nor an
exact (BA)-orbit factor.  It is a correlated matching of length
(Theta(m)) phase runs, with atom partners rematched flag by flag, inside
one integral SCD/collar atlas.

## 9. Independent audit of the decisive steps

The two decisive equivalences were checked in both directions.

1. In Theorem 3.1, after fixing (a\to b), a state forbids exactly one
   third-endpoint type, its boundary label.  Therefore every Hall cut with
   at least two slot types sees the whole state shore; the singleton cuts
   are exactly (3.5).  No hidden subset cut is omitted.  Cyclic equality
   of the three corner quotas is precisely what allows the three matched
   pools to be grouped into atoms.

2. In Theorem 4.1, every selected state has its forced (A)-edge, and it
   has a (B)-continuation if and only if its (C)-successor is selected.
   Hence indegree and outdegree cannot create branching: components are
   exactly cyclic runs.  A proper run contributes one boundary and one
   path; a full orbit contributes no boundary but needs exactly one cut.
   This accounts for the (+f_C(S)) term in (4.4).

The lower-bound audit also distinguishes the two parities correctly.
For even (m), the collision is at middle ownership and gives (6.1).
For odd (m), middle owners on a full alternating orbit are distinct, but
the shift reappears in the rank-((m-1)) footprint, giving (6.8).  Partner
variation changes only atom grouping; it cannot change either physical
footprint identity.

## 10. Proved/conditional boundary

Proved exactly:

* the full-catalogue all-depth phase-varying factor;
* the (S_n)-indivisibility of its fixed positional realization;
* the integral flagwise ordered-Hall theorem (3.3)--(3.5);
* the exact (C)-run component and split-copy Hall formulas;
* the even middle-owner and odd first-shadow robust boundary laws;
* owner-simple critical blocks of length (m+1).

Still conditional/unproved:

* a near-complete owner-disjoint selection of critical blocks;
* simultaneous feasibility of every flagwise quota system for that
  selection;
* embedding the selection in one full SCD with common all-depth collars;
* aggregate (o(W)) two-sided target leave;
* the coefficient-one theorem.
