# Lane S7: exact dynamic flag fusion for the nonstandard recursive Hall lift

Date: 2026-07-25

Method: pure mathematics only.  No web search, computation, finite search,
SAT solver, or long-running local job is used.

## 0. Proved endpoint

This report proves the exact cross-layer compatibility theorem missing from
the one-layer forced-target formulation.  It does **not** prove the required
asymptotic estimate and therefore does not prove the constant-one theorem.

For an arbitrary prescribed radius assignment and arbitrary initial directed
Johnson path forest, the following are proved.

1. All lower and upper perfect matchings through every recursive layer fuse
   exactly into two nested systems of Boolean endpoint flags.  Conversely,
   every such pair of flag systems constructs one integral saturated band
   SCD.  There is no fractional or separate-depth object in this
   equivalence.
2. Within the no-reintroduction/no-merger recursive Hall architecture, for
   purposes of all future forced-target lifts, a reachable history has
   the lossless Markov state
   \((F_h,L_h,R_h)\): the retained labelled forest and the two current
   endpoint bijections.  The interior singleton order may be discarded.
3. It is never advantageous for the total new-deletion budget to delete an
   edge which is presently liftable.  Thus maximal retention may be imposed
   without loss.
4. The whole dynamic optimization is the following single static integral
   maximization.  An initial edge is *durable* when the two endpoint-
   intersection identities hold at every layer before either endpoint's
   prescribed stopping time.  Then

   \[
   \boxed{
   K_H^{\min}
   =|E^\circ|-
     \max_{(\mathbf L,\mathbf R)}
        |E^{\rm dur}(\mathbf L,\mathbf R)| .}
   \tag{0.1}
   \]

   In particular, the exact baseline is the number \(|E^\circ|\) of
   initially internal edges, not a sum of edge counts over the layers.
   Failures at many layers can be fused only by concentrating them on the
   same initial edges, each of which is charged once at its first failure.
5. A general cross-layer obstruction test follows.  Durable triangular arrays
   along an initial path force a sliding window of outgoing coordinates to
   be distinct, with its future half inside the central owner and its past
   half outside.  A family of violating windows gives the exact hitting
   bound

   \[
   K_H^{\min}\ge
   \left\lceil\frac{|\mathcal V_q|}{2q+2}\right\rceil.
   \tag{0.2}
   \]

   For the intended odd-cut input this test is vacuous: every odd-cut path
   is a complementary Johnson geodesic, and its outgoing-coordinate windows
   automatically have the required distinctness and membership pattern.
   Thus (0.2) is a valid audit tool for other initial forests, not a claimed
   quantitative obstruction to the odd-cut CRHL.

Consequently the nonstandard recursive Hall gate is now equivalent, with no
remaining dynamic-compatibility qualification, to proving that the maximum
in (0.1) is \(|E^\circ|-o(W/H)\) for the prescribed odd-cut forest and
globally contiguous lifetime assignment.  That estimate is **unproved**.

## 1. Exact finite setup

Let

\[
 n=2m,\qquad
 N_h=\binom{2m}{m-h},\qquad
 c_h=N_h-N_{h+1},
 \tag{1.1}
\]

and fix an integer

\[
 1\le H\le m.
 \tag{1.2}
\]

Let

\[
 X=\binom{[2m]}m
 \tag{1.3}
\]

be the set of labelled middle owners.  Prescribe a lifetime map

\[
 \tau:X\longrightarrow\{0,1,\ldots,H\}
 \tag{1.4}
\]

with the exact multiplicities

\[
 |\tau^{-1}(h)|=c_h\quad(0\le h<H),
 \qquad
 |\tau^{-1}(H)|=N_H.
 \tag{1.5}
\]

Put

\[
 X_h=\{v\in X:\tau(v)\ge h\}.
 \tag{1.6}
\]

Then, exactly,

\[
 |X_h|=N_h\qquad(0\le h\le H).
 \tag{1.7}
\]

In the constrained recursive Hall construction, a fixed concatenation of
the odd-cut paths is divided into globally contiguous blocks of sizes

\[
 c_0,c_1,\ldots,c_{H-1},N_H.
 \tag{1.8}
\]

The value of \(\tau\) is the block label, so every \(X_h\) is one global
suffix.  The theorems below do not need contiguity and hence apply, in
particular, to this prescribed choice.

Let \(F_0\) be any directed path forest on \(X\) every edge of which is an
ordinary radius-zero rotor, equivalently a directed Johnson edge.  Write

\[
 e:v\longrightarrow w,
 \qquad
 w=v-\{x_e\}+\{y_e\}.
 \tag{1.9}
\]

For the intended application \(F_0\) is the exact odd-cut forest.  No
property special to that forest is used until the final implication scope.

## 2. Global endpoint flags are exactly integral band SCDs

### Definition 2.1 (lower and upper-complement flag systems)

A lower flag system for \(\tau\) is a family of bijections

\[
 L_h:X_h\longrightarrow\binom{[2m]}{m-h}
 \qquad(0\le h\le H)
 \tag{2.1}
\]

such that

\[
 L_0(v)=v,
 \qquad
 L_{h+1}(v)\subset L_h(v)
 \quad(v\in X_{h+1}).
 \tag{2.2}
\]

An upper-complement flag system is a family of bijections

\[
 R_h:X_h\longrightarrow\binom{[2m]}{m-h}
 \qquad(0\le h\le H)
 \tag{2.3}
\]

such that

\[
 R_0(v)=[2m]\setminus v,
 \qquad
 R_{h+1}(v)\subset R_h(v)
 \quad(v\in X_{h+1}).
 \tag{2.4}
\]

All maps in (2.1) and (2.3) are literal bijections, not fractional
matchings.  Let \(\mathfrak F^-_\tau\) and \(\mathfrak F^+_\tau\) denote
the two finite sets of flag systems.

### Theorem 2.2 (exact flag--band-SCD equivalence)

Pairs

\[
 (\mathbf L,\mathbf R)
 \in\mathfrak F^-_\tau\times\mathfrak F^+_\tau
 \tag{2.5}
\]

are in bijection with integral saturated symmetric-chain decompositions of
the depth-\(H\) central band whose chain centred at \(v\) has radius
\(\tau(v)\).

More explicitly, for \(v\in X\), put \(r=\tau(v)\), and for
\(0\le j<r\) let

\[
 \ell_j(v)\text{ be the unique element of }
 L_j(v)\setminus L_{j+1}(v),
 \tag{2.6}
\]

\[
 u_j(v)\text{ be the unique element of }
 R_j(v)\setminus R_{j+1}(v).
 \tag{2.7}
\]

Then the chain of owner \(v\) is represented by the integral state

\[
 \omega_r(v)=
 \bigl(
 L_r(v);
 \ell_{r-1}(v),\ldots,\ell_0(v),
 u_0(v),\ldots,u_{r-1}(v);
 R_r(v)
 \bigr).
 \tag{2.8}
\]

#### Proof

The inclusions and rank differences show that (2.6)--(2.7) are well
defined single coordinates.  Since every \(L_j(v)\) lies in
\(L_0(v)=v\), every \(R_j(v)\) lies in
\(R_0(v)=[2m]\setminus v\), and the two sides are disjoint.  Thus the
three blocks in (2.8) partition \([2m]\).

Starting from \(L_r(v)\), add in order

\[
 \ell_{r-1}(v),\ldots,\ell_0(v),
 u_0(v),\ldots,u_{r-1}(v).
 \tag{2.9}
\]

This gives a saturated chain from rank \(m-r\) through rank \(m+r\).
After the first \(r-h\) additions its rank-\((m-h)\) member is exactly
\(L_h(v)\).  Its rank-\((m+h)\) member is exactly

\[
 [2m]\setminus R_h(v).
 \tag{2.10}
\]

For fixed \(h\), the owners whose chains meet these ranks are precisely
\(X_h\).  The bijectivity of \(L_h\) covers every rank-\((m-h)\) mask
once, and the bijectivity of \(R_h\) covers every rank-\((m+h)\) mask
once after complementation.  Hence the chains form one exact integral band
SCD.

Conversely, take such a band SCD.  Every chain has a unique middle member
\(v\).  Define \(L_h(v)\) to be its rank-\((m-h)\) member and
\(R_h(v)\) to be the complement of its rank-\((m+h)\) member.  Saturation
gives (2.2) and (2.4), while exact rank coverage gives the two
bijections.  The successive differences recover the chain order, so the
two constructions are inverse.  \(\square\)

### Corollary 2.3 (matching compatibility across all layers)

A recursively chosen sequence of lower and upper perfect matchings exists
through depth \(H\) if and only if

\[
 \mathfrak F^-_\tau\ne\varnothing,
 \qquad
 \mathfrak F^+_\tau\ne\varnothing.
 \tag{2.11}
\]

The lower and upper feasibility problems are independent; their rotor-edge
reward will be coupled below.

#### Proof

At layer \(h\), a lower perfect matching sends each
\(v\in X_{h+1}\) to one rank-\((m-h-1)\) subset of \(L_h(v)\), and
does so bijectively.  Calling that target \(L_{h+1}(v)\) gives exactly
(2.1)--(2.2).  Iteration gives a lower flag system, and the converse reads
off its consecutive bijections.  The upper-complement argument is
identical.  Since the lower flags remain inside \(v\) and the upper flags
inside its complement, any pair is simultaneously realizable by Theorem
2.2.  \(\square\)

This is a compatibility theorem, not an assertion that (2.11) holds for
the globally contiguous lifetime assignment.  It identifies the exact
single integral object whose existence must be proved.

## 3. The forced-target rule is endpoint-only

Suppose at depth \(h\) the states of two owners are joined by a directed
rotor edge

\[
 \omega_h(v)\longrightarrow\omega_h(w).
 \tag{3.1}
\]

Write their endpoints as \(L_h(v),R_h(v)\) and
\(L_h(w),R_h(w)\).

### Lemma 3.1 (intersection form of forced targets)

The two forced targets of (3.1) are exactly

\[
 \lambda_h(v,w)=L_h(v)\cap L_h(w),
 \qquad
 \rho_h(v,w)=R_h(v)\cap R_h(w).
 \tag{3.2}
\]

For a pair of next-layer endpoint bijections \(L_{h+1},R_{h+1}\), the
edge lifts if and only if

\[
 \boxed{
 L_{h+1}(v)=L_h(v)\cap L_h(w),
 \qquad
 R_{h+1}(w)=R_h(v)\cap R_h(w).}
 \tag{3.3}
\]

This statement includes \(h=0\).

#### Proof

For \(h\ge1\), write

\[
 \omega_h(v)=(L;z_1,\ldots,z_{2h};R).
\]

If the rotor edge removes \(x\in L\) and inserts \(y\in R\), then

\[
 L_h(w)=L-\{x\}+\{y\},
 \qquad
 R_h(w)=R-\{y\}+\{z_{2h}\}.
 \tag{3.4}
\]

Thus the intersections in (3.2) are \(L-\{x\}\) and
\(R-\{y\}\), precisely the previously proved lower and
upper-complement forced targets.  At \(h=0\),

\[
 L_0(w)=L_0(v)-\{x\}+\{y\},
 \qquad
 R_0(w)=R_0(v)-\{y\}+\{x\},
 \tag{3.5}
\]

and the same intersection formula holds.

It remains only to audit the two apparent inequalities in the one-edge
lift criterion.  If the lower coordinate removed at \(w\) were \(y\),
then

\[
 L_{h+1}(w)=L_h(w)-\{y\}
            =L_h(v)-\{x\}=L_{h+1}(v),
\]

contradicting injectivity of \(L_{h+1}\).  If the upper-complement
coordinate removed at \(v\) were \(y\), then

\[
 R_{h+1}(v)=R_h(v)-\{y\}=R_{h+1}(w),
\]

contradicting injectivity of \(R_{h+1}\).  Hence the two equalities in
(3.3) are both necessary and sufficient.  \(\square\)

The important point is that no interior coordinate of the singleton queue
appears in (3.3).

## 4. A lossless finite Markov state and exact Bellman recurrence

At depth \(h\), let \(F_h\) be the retained directed path forest on
\(X_h\).  Every edge of \(F_h\) is labelled by its original edge in
\(F_0\).  As in the stated CRHL architecture, later forests may retain or
delete active inherited edges but may not introduce a new edge outside the
current forest.  Define the compressed state

\[
 \sigma_h=(F_h,L_h,R_h).
 \tag{4.1}
\]

The fixed data \((F_0,\tau)\) are not repeated in the state.

### Theorem 4.1 (lossless state compression)

Within this no-reintroduction architecture, two reachable recursive
histories which have the same triple (4.1) have
exactly the same feasible compressed successors, with exactly the same
new-deletion costs, at every remaining depth.  Thus the entire interior
singleton words may be forgotten without losing any information relevant
to future matching feasibility or rotor retention.

#### Proof

From \(\sigma_h\), a possible next lower matching is exactly a bijection

\[
 L':X_{h+1}\longrightarrow\binom{[2m]}{m-h-1},
 \qquad L'(v)\subset L_h(v),
 \tag{4.2}
\]

and a possible next upper-complement matching is exactly a bijection

\[
 R':X_{h+1}\longrightarrow\binom{[2m]}{m-h-1},
 \qquad R'(v)\subset R_h(v).
 \tag{4.3}
\]

These conditions depend only on \(L_h,R_h\).  By Lemma 3.1, the edges of
the active induced forest which can be retained are exactly

\[
 \begin{split}
 \Gamma_h(\sigma_h;L',R')
 =\{v\to w\in E(F_h[X_{h+1}]):{}&
 L'(v)=L_h(v)\cap L_h(w),\\
 &R'(w)=R_h(v)\cap R_h(w)\}.
 \end{split}
 \tag{4.4}
\]

This too depends only on (4.1).  The chosen endpoints reconstruct genuine
next states by prepending the unique element of
\(L_h(v)\setminus L'(v)\) and appending the unique element of
\(R_h(v)\setminus R'(v)\).  Lemma 3.1 guarantees every retained edge,
regardless of the older interior singleton order.  Induction over the
remaining layers proves future equivalence.  \(\square\)

### Lemma 4.2 (maximal retention without loss)

For minimization of

\[
 K_H=\sum_{h=0}^{H-1}k_h,
 \tag{4.5}
\]

where \(k_h\) is the number of additional edges deleted inside the active
induced forest at layer \(h\), there is an optimum satisfying

\[
 F_{h+1}=\Gamma_h(\sigma_h;L_{h+1},R_{h+1})
 \quad(0\le h<H).
 \tag{4.6}
\]

#### Proof

Suppose a presently eligible edge is nevertheless deleted at layer \(h\).
Keep it instead.  At every later layer, keep it while both endpoints remain
active and (3.3) continues to hold.  If (3.3) first fails later, delete the
edge then; this replaces one deletion by one deletion.  If an endpoint
stops first, the edge leaves the active induced forest and no additional
deletion is paid.  Reinstating it creates neither a branch nor a cycle,
because every retained forest remains a subgraph of the original directed
path forest.  Endpoint choices and all other edges are unchanged.  Hence
\(K_H\) does not increase.  Repeating proves (4.6).  \(\square\)

Define \(D_h(\sigma)\) to be the minimum cumulative new-deletion count of
a history reaching the compressed state \(\sigma\) at depth \(h\), with
\(+\infty\) for an unreachable state.  At depth zero there is one state

\[
 \sigma_0=(F_0,v\mapsto v,v\mapsto[2m]\setminus v),
 \qquad D_0(\sigma_0)=0.
 \tag{4.7}
\]

### Corollary 4.3 (exact Bellman equation)

Restricting to the maximal successors (4.6), the exact recurrence is

\[
 \boxed{
 D_{h+1}(F',L',R')
 =\min_{\substack{\sigma=(F,L,R)\\
                   (L',R')\text{ satisfy }(4.2)\text{--}(4.3)\\
                   F'=\Gamma_h(\sigma;L',R')}}
 \left[
 D_h(\sigma)+|E(F[X_{h+1}])|-|E(F')|
 \right].}
 \tag{4.8}
\]

Consequently

\[
 K_H^{\min}=\min_{\sigma\text{ at depth }H}D_H(\sigma).
 \tag{4.9}
\]

This is a finite exact dynamic program, not an efficient algorithmic claim.
In particular, (4.8) does not justify replacing the displayed state by the
scalar one-layer value \(M_h^\star\): its successor relation uses the
identities of the retained labelled edges and both endpoint bijections.
No claim is made here that some different, presently unknown sufficient
statistic cannot compress these data further.

The forest coordinate in (4.1) is genuinely historical.  Current endpoint
sets alone do not record whether an edge failed at an earlier layer.  For
example, at two successive lower removals the orders \((x,a)\) and
\((a,x)\) lead to the same final endpoint after deleting \(\{x,a\}\),
but an original edge forcing first removal \(x\) survives the former
history and fails in the latter.  The theorem says that no data beyond
\((F_h,L_h,R_h)\) are needed.

## 5. Static global dynamic fusion

For an initial edge \(e=v\to w\), define its common lifetime

\[
 r(e)=\min\{\tau(v),\tau(w)\}.
 \tag{5.1}
\]

The edges ever lying inside an active induced forest are

\[
 E^\circ=\{e\in E(F_0):r(e)\ge1\}.
 \tag{5.2}
\]

For a pair of endpoint flag systems, call \(e=v\to w\) *durable* when,
for every integer \(h\) with \(0\le h<r(e)\),

\[
 L_{h+1}(v)=L_h(v)\cap L_h(w),
 \tag{5.3}
\]

\[
 R_{h+1}(w)=R_h(v)\cap R_h(w).
 \tag{5.4}
\]

Let \(E^{\rm dur}(\mathbf L,\mathbf R)\) be the set of durable edges.

### Theorem 5.1 (exact global flag-agreement formula)

For every finite \((m,H,F_0,\tau)\) satisfying (1.1)--(1.9),

\[
 \boxed{
 K_H^{\min}
 =|E^\circ|-
   \max_{\substack{\mathbf L\in\mathfrak F^-_\tau\\
                    \mathbf R\in\mathfrak F^+_\tau}}
   |E^{\rm dur}(\mathbf L,\mathbf R)|.}
 \tag{5.5}
\]

If either flag family is empty, the recursive band extension is infeasible;
in that case the right side is left undefined rather than interpreted as a
finite deletion budget.

#### Proof

Fix a pair of flag systems and use maximal retention.  We claim inductively
that an initial edge \(e\) belongs to \(F_h\) precisely when

\[
 r(e)\ge h
 \quad\text{and}\quad
 (5.3)\text{--}(5.4) hold for every }0\le j<h.
 \tag{5.6}
\]

The assertion is immediate at \(h=0\).  Given it at \(h\), the edge lies
in the active induced forest for the next lift precisely when
\(r(e)\ge h+1\).  Lemma 3.1 and maximal retention say that it enters
\(F_{h+1}\) precisely when the two identities at level \(h\) also hold.
This proves (5.6).

Every nondurable edge of \(E^\circ\) therefore has a unique first failed
level.  It is counted once in the corresponding \(k_h\).  A durable edge
survives until an endpoint reaches its prescribed stopping level and is
never counted in any \(k_h\).  Hence, for these flags,

\[
 \sum_{h=0}^{H-1}k_h
 =|E^\circ|-|E^{\rm dur}(\mathbf L,\mathbf R)|.
 \tag{5.7}
\]

Minimizing (5.7) over flags gives an upper bound for the dynamic optimum.
Conversely, every dynamic sequence supplies a pair of flag systems by
Corollary 2.3, and Lemma 4.2 replaces it by maximal retention without
increasing its deletion count.  Equation (5.7) then applies.  This proves
(5.5).  \(\square\)

### Corollary 5.2 (exact first-failure union)

For fixed flags, let \(B_h\) be the initial edges which satisfy all earlier
intersection identities, are active through layer \(h+1\), and first fail
one of (5.3)--(5.4) at level \(h\).  Then the sets \(B_h\) are disjoint and

\[
 k_h=|B_h|,
 \qquad
 K_H=\left|\bigsqcup_{h=0}^{H-1}B_h\right|.
 \tag{5.8}
\]

Thus summing independently optimized raw layer deficiencies is not the
global optimization.  A successful construction may make many potential
later incompatibilities disappear by paying once on a common small set of
edges; conversely, unrelated one-layer maximizers need not select the same
survivor set.

### Corollary 5.3 (separation of the two flag defects)

For fixed flags, let \(B^-(\mathbf L)\) be the edges which fail at least one
lower identity (5.3) before stopping, and define \(B^+(\mathbf R)\)
analogously from (5.4).  Then

\[
 K_H(\mathbf L,\mathbf R)
 =|B^-(\mathbf L)\cup B^+(\mathbf R)|.
 \tag{5.9}
\]

In particular,

\[
 \max\{|B^-|,|B^+|\}
 \le K_H
 \le |B^-|+|B^+|.
 \tag{5.10}
\]

The lower and upper flag feasibility problems factor, but their good-edge
sets must agree on almost all initial edges.  This is the exact multilevel
analogue of the one-layer paired-rainbow/Boolean-extendability gap.

## 6. Coordinate-shift rigidity and a multilevel obstruction test

The static identities have a useful coordinate form which does not appear
in the one-layer defect.

For \(v\in X_{h+1}\), retain the notation

\[
 \ell_h(v)=L_h(v)\setminus L_{h+1}(v),
 \qquad
 u_h(v)=R_h(v)\setminus R_{h+1}(v).
 \tag{6.1}
\]

### Lemma 6.1 (coordinate shifts on a durable edge)

Let \(e:v\to w\) be durable through levels
\(0,\ldots,r-1\), where \(1\le r\le r(e)\), and let

\[
 x_e=v\setminus w.
 \tag{6.2}
\]

Then

\[
 \ell_0(v)=x_e,
 \qquad
 u_0(w)=x_e,
 \tag{6.3}
\]

and, for \(1\le h<r\),

\[
 \boxed{
 \ell_h(v)=\ell_{h-1}(w),
 \qquad
 u_h(w)=u_{h-1}(v).}
 \tag{6.4}
\]

#### Proof

At radius zero, the lower forced target at the source is
\(v-\{x_e\}\), proving the first equality in (6.3).  Since

\[
 R_0(w)=R_0(v)-\{y_e\}+\{x_e\},
\]

the upper-complement forced target at \(w\) removes \(x_e\), proving the
second equality.

When an edge is lifted from depth \(h-1\) to depth \(h\), the new rotor
coordinate removed from the lower endpoint of its source is
\(\ell_{h-1}(w)\); this is the first-coordinate comparison in the exact
one-edge lift.  Survival through the following layer forces the source to
remove that coordinate, giving the first identity in (6.4).  The last
singleton coordinate of the source at depth \(h\) is
\(u_{h-1}(v)\); the upper forced-target identity makes \(w\) remove it,
giving the second identity.  Equivalently, both statements follow by
taking single-element differences in (5.3)--(5.4).  \(\square\)

Now let

\[
 v_0\to v_1\to\cdots\to v_s
 \tag{6.5}
\]

be a directed path of \(F_0\), and put

\[
 x_i=v_i\setminus v_{i+1}
 \qquad(0\le i<s).
 \tag{6.6}
\]

### Corollary 6.2 (durable triangular window)

Fix indices \(i,q\) for which all displayed edges exist.  Assume that for
each \(0\le j\le q\),

* the future edge \(e_{i+j}\) is durable through at least
  \(q-j+1\) levels; and
* the past edge \(e_{i-j-1}\) is durable through at least
  \(q-j+1\) levels.

Then

\[
 \ell_q(v_i)=x_{i+q},
 \qquad
 u_q(v_i)=x_{i-q-1},
 \tag{6.7}
\]

and, more fully,

\[
 \{x_i,x_{i+1},\ldots,x_{i+q}\}\subseteq v_i,
 \tag{6.8}
\]

\[
 \{x_{i-q-1},\ldots,x_{i-2},x_{i-1}\}
 \subseteq[2m]\setminus v_i.
 \tag{6.9}
\]

All \(2q+2\) coordinates in (6.8)--(6.9) are pairwise distinct.

#### Proof

Iterating the lower identity in (6.4) gives

\[
 \ell_q(v_i)=\ell_{q-1}(v_{i+1})
 =\cdots=\ell_0(v_{i+q})=x_{i+q}.
\]

Doing this for every depth from zero to \(q\) identifies the lower removal
sequence at \(v_i\) with \(x_i,\ldots,x_{i+q}\).  These coordinates are
distinct and lie in \(v_i\), because they are successive removals from the
nested lower flag rooted at \(v_i\).  The upper identity gives

\[
 u_q(v_i)=u_{q-1}(v_{i-1})
 =\cdots=u_0(v_{i-q})=x_{i-q-1}.
\]

The past coordinates are successive removals from the upper-complement
flag rooted at \([2m]\setminus v_i\), so they are distinct and lie outside
\(v_i\).  The two groups are disjoint because one lies inside \(v_i\) and
the other outside.  \(\square\)

The lifetimes needed in this corollary are explicit: for each edge which is
required durable through \(t\) levels, its common lifetime (5.1) must be at
least \(t\).

### Theorem 6.3 (exact violating-window hitting bound)

Fix \(q\ge0\).  Let \(\mathcal V_q\) be any set of indices \(i\) on the
initial paths satisfying both of the following.

1. Every edge in the future and past triangles of Corollary 6.2 has the
   common lifetime required there.
2. The base-coordinate conclusion (6.8)--(6.9), including pairwise
   distinctness, is false.

Then every recursively compatible flag pair obeys

\[
 \boxed{
 K_H\ge
 \left\lceil\frac{|\mathcal V_q|}{2q+2}\right\rceil.}
 \tag{6.10}
\]

#### Proof

For every \(i\in\mathcal V_q\), Corollary 6.2 shows that at least one of
the \(2q+2\) initial edges

\[
 e_{i-q-1},\ldots,e_{i-1},e_i,\ldots,e_{i+q}
 \tag{6.11}
\]

is nondurable.  All these edges have positive common lifetime by
hypothesis, so every such nondurable edge is counted in \(K_H\) by Theorem
5.1.  A fixed initial edge belongs to at most \(2q+2\) intervals of the
form (6.11).  Double counting the incidences between violating windows and
nondurable edges yields

\[
 |\mathcal V_q|\le(2q+2)K_H.
\]

Since \(K_H\) is an integer, (6.10) follows.  \(\square\)

This is a genuine cross-layer obstruction: it is invisible to any single
forced-target multigraph.  The next corollary shows that it does not fire on
the intended odd-cut input.

### Corollary 6.4 (the violating-window test is empty on odd-cut paths)

Suppose an initial path is a complementary Johnson geodesic

\[
 v_0\to v_1\to\cdots\to v_m=[2m]\setminus v_0.
 \tag{6.12}
\]

Then its outgoing coordinates \(x_0,\ldots,x_{m-1}\) are the \(m\)
distinct elements of \(v_0\), and for every \(i\),

\[
 \{x_i,\ldots,x_{m-1}\}\subseteq v_i,
 \qquad
 \{x_0,\ldots,x_{i-1}\}\subseteq[2m]\setminus v_i.
 \tag{6.13}
\]

Consequently every defined interior window satisfies (6.8)--(6.9), and

\[
 \mathcal V_q=\varnothing
 \tag{6.14}
\]

for every \(q\) on every exact odd-cut path.

#### Proof

The Johnson distance between \(v_0\) and its complement is \(m\), equal to
the length of (6.12).  Thus the path is geodesic: no element removed from
\(v_0\) can be reinserted, and each of the \(m\) elements of \(v_0\) is
removed exactly once.  After \(i\) steps, precisely
\(x_0,\ldots,x_{i-1}\) have been removed.  This proves (6.13), the
pairwise distinctness, and hence (6.14).  The audited odd-cut forest consists
of such complementary geodesics.  \(\square\)

## 7. Exact application to the constrained recursive Hall gate

Return to

\[
 W=\binom{2m}{m},
 \qquad
 H=\lceil A\sqrt m\rceil
 \tag{7.1}
\]

for fixed \(A>0\).  For all sufficiently large \(m\), (1.2) holds.  Use
the exact odd-cut directed forest and the globally contiguous lifetime
assignment (1.8).  Define the integral global flag defect

\[
 \mathfrak K_{m,A}
 :=|E^\circ|-
   \max_{\substack{\mathbf L\in\mathfrak F^-_\tau\\
                    \mathbf R\in\mathfrak F^+_\tau}}
   |E^{\rm dur}(\mathbf L,\mathbf R)|,
 \tag{7.2}
\]

provided both flag families are nonempty.

### Theorem 7.1 (CRHL with the dynamic qualifier removed)

For each fixed \(A>0\), the no-merger nonstandard recursive Hall route
satisfies its required deletion assertion if and only if

\[
 \mathfrak F^-_\tau\ne\varnothing,
 \qquad
 \mathfrak F^+_\tau\ne\varnothing,
 \qquad
 \boxed{\mathfrak K_{m,A}=o(W/H)}.
 \tag{7.3}
\]

Under (7.3), the endpoint flags construct one literal integral saturated
depth-\(H\) band SCD, the canonical durable-edge forests introduce exactly
\(K_H=\mathfrak K_{m,A}\) new cuts, and no merger is introduced.

#### Proof

Theorem 2.2 proves exact integral band-SCD construction from the flags.
Theorem 5.1 identifies the least possible new-deletion count with
\(\mathfrak K_{m,A}\).  Every forest in the canonical construction is a
subgraph of the initial directed path forest, so no merger occurs.  This
proves both directions.  \(\square\)

For reference, at the first active layer the exact baseline in (7.2) is

\[
 |E^\circ|=|E(F_0[X_1])|=N_1-b_{A,0},
 \tag{7.4}
\]

where \(b_{A,0}\) is the number of nonempty active suffix runs in the
odd-cut paths.  In particular

\[
 1\le b_{A,0}\le \operatorname{Cat}_m
 \tag{7.5}
\]

when \(X_1\ne\varnothing\).  Formula (7.4), rather than
\(\sum_h|E(F_h[X_{h+1}])|\), is the exact floor from which durable edges
are subtracted.

Combining (7.3) with the already proved recursive toll ledger gives, only
conditionally,

\[
 \widehat\Phi_H
 \le H(H-1)+2H(\operatorname{Cat}_m+1)
      +2H\mathfrak K_{m,A}=o(W).
 \tag{7.6}
\]

The existing central-band extension then completes the band SCD to one
full integral SCD without changing any band chain or retained rotor edge.
Every retained forest path is a genuine directed rotor path and therefore
has the established literal contiguous-OR realization with exact prefix
toll \(2h\) per component at radius \(h\).

## 8. Proved and unproved boundary

### Proved

1. Exact fusion of all recursive lower and upper perfect matchings into
   two nested integral flag systems, and the converse reconstruction of one
   common band SCD.
2. Exact lossless dynamic state \((F_h,L_h,R_h)\) and Bellman recurrence
   (4.8) for the no-reintroduction/no-merger CRHL architecture.
3. Maximal retention without loss for the total deletion budget.
4. Exact static durable-edge formula (5.5), including the first-failure
   accounting and the correct initial-edge baseline.
5. Exact coordinate-shift rigidity and the general cross-layer obstruction
   (6.10), together with the proof that this particular obstruction is
   identically zero on the intended odd-cut forest.
6. Exact equivalence (7.3) between the surviving no-merger CRHL deletion
   gate and one paired multilevel flag-agreement estimate.

### Unproved

1. Nonemptiness of both flag families for the prescribed globally
   contiguous odd-cut lifetime assignment.
2. The decisive asymptotic estimate

   \[
   \mathfrak K_{m,A}=o(W/H).
   \]

3. Any different cross-layer obstruction which is nonzero on complementary
   odd-cut geodesics; Corollary 6.4 closes the simple outgoing-coordinate
   window test on that input.

Accordingly, this report proves the requested recursive compatibility and
global dynamic fusion theorem but not its needed asymptotic solution.  It
neither proves nor refutes

\[
 \nu(k)\le(1+o(1))W(k).
\]

The exact remaining mathematical gate in this lane is now the static,
integral, paired-flag agreement estimate (7.3); no independent choice of
one-layer maximizers and no untracked singleton-order compatibility remains.

### Independent audit note

An independent adversarial audit checked the flag--band equivalence, the
endpoint-only Markov quotient, delayed-cut/maximal-retention lemma, static
first-failure formula, and every index in the triangular-window argument.
It found those statements correct.  The audit identified the material scope
point now incorporated as Corollary 6.4: the elementary coordinate-window
test is vacuous on complementary odd-cut geodesics and therefore cannot be
used as the missing asymptotic obstruction for CRHL.
