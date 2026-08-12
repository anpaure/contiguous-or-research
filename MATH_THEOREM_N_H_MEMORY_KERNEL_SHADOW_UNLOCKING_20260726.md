# Exact H-memory kernel trades and shadow unlocking

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or
web input is used.

## 0. Result

Fix an integral \(H\)-safe owner circulation \(z\) on the safe path
columns \(\Gamma_H\). There is an exact necessary-and-sufficient
description of every run-neutral, cap-safe successor trade.

A signed integer path vector \(\delta\) is such a trade precisely when:

1. \(z+\delta\ge0\);
2. \(\delta\) has zero sum in every root-owner fibre;
3. \(\delta\) has zero prefix-minus-suffix flow at every
   \((H-1)\)-memory state;
4. its first-deletion count is zero at every coordinate;
5. its induced signed shadow effect remains inside every prescribed load
   interval.

The first three conditions say that \(z+\delta\) is another integral
\(H\)-safe owner successor. The fourth says that its common run vector is
the same. The fifth is exactly cap safety; no independent shadow argument
is hidden.

For every such trade, the shadow effects \(g_j^\pm\) obey

\[
 B_{m-j}g_j^-=0,\qquad B_{m+j}g_j^+=0
 \qquad(1\le j\le H).                              \tag{0.1}
\]

More generally, if the run vector changes by \(\Delta r\), the right
sides are \(-j\Delta r\) and \(j\Delta r\).

There is also an exact adjacent-depth flow identity. The lower effects at
depths \(q,q+1\) are the two marginals of one signed flow

\[
 p_{q,T,S}^-\qquad(S\subset T,\ |T\setminus S|=1),               \tag{0.2}
\]

and the upper effects are the marginals of the dual inclusion flow.
If a demanded target \(T\) is locked because every
\(S\in\partial T\) is saturated, then any cap-safe trade with
\(g_{q,T}^->0\) necessarily contains an alternating pivot

\[
                         T\longrightarrow S\longleftarrow T',
                                                               \tag{0.3}
\]

with positive flow on \(T\to S\) and negative flow on \(T'\to S\).
Thus the trade must displace an old enclosing occurrence at the same time
as it inserts the new one. A terminal collar whose added rows extend to
safe nested depth-\((q+1)\) flags and remain subject to the same child
caps cannot break a complete lock by additions alone.

Conversely, any integer \(\delta\) satisfying the five kernel conditions
and having \(g_{q,T}^-\ge1\) is a legal exact shadow-unlocking operation.
This formulation does not assume a pre-existing closed component-switch
lane: legality is certified globally by the root and memory equations.
Inside a fixed \(D_r\)-transversal or other frozen fibre, its additional
constraint rows must also annihilate \(\delta\), as stated in Section 2.1.

The open theorem is abundance. Point-balanced alternating pivots in the
shadow inclusion graph are not guaranteed by the projected identities to
lift to short, sign-compatible integer circuits of the \(H\)-memory
kernel. Even when they lift, all other depths
and both signs may consume saturated rows. A coefficient-one absorber
requires many bounded-overlap lifts with controlled support and cycle toll.

## 1. The H-memory matrices

Let

\[
 \gamma=(X_0,X_1,\ldots,X_H)\in\Gamma_H
\]

be a safe Johnson path. Put

\[
 \operatorname{pre}\gamma=(X_0,\ldots,X_{H-1}),
 \qquad
 \operatorname{suf}\gamma=(X_1,\ldots,X_H).
\]

For the first transition, write

\[
 d(\gamma)=X_0\setminus X_1,\qquad
 a(\gamma)=X_1\setminus X_0.
\]

Both are singleton coordinates.

Define the root matrix \(A\), memory matrix \(M\), deletion matrix \(D\),
and signed shadow matrices \(S_j^\pm\) by

\[
 A_{X,\gamma}=\mathbf1_{\{X_0=X\}},                \tag{1.1}
\]

\[
 M_{\sigma,\gamma}
 =\mathbf1_{\{\operatorname{pre}\gamma=\sigma\}}
  -\mathbf1_{\{\operatorname{suf}\gamma=\sigma\}},              \tag{1.2}
\]

\[
 D_{v,\gamma}=\mathbf1_{\{d(\gamma)=v\}},          \tag{1.3}
\]

\[
 (S_j^-)_{T,\gamma}
 =\mathbf1_{\{L_j(\gamma)=T\}},\qquad
 (S_j^+)_{U,\gamma}
 =\mathbf1_{\{U_j(\gamma)=U\}}.                   \tag{1.4}
\]

Here

\[
 L_j(\gamma)=\bigcap_{i=0}^jX_i,\qquad
 U_j(\gamma)=\bigcup_{i=0}^jX_i.
\]

An integral owner successor is represented by

\[
 z\in\mathbb Z_{\ge0}^{\Gamma_H},\qquad
 Az=\mathbf1,\qquad Mz=0.                          \tag{1.5}
\]

The root equations make every nonzero entry of \(z\) equal to one. The
memory equations stitch the selected columns into cyclic \(H\)-windows,
so (1.5) is exactly an \(H\)-safe owner permutation.

Its run vector and signed histograms are

\[
 r(z)=Dz,\qquad \mu_j^\pm(z)=S_j^\pm z.            \tag{1.6}
\]

## 2. Exact kernel-trade theorem

For every signed row \(r=(j,\epsilon,T)\), fix an allowed integer interval

\[
                         \ell_r\le\mu_r\le u_r.     \tag{2.1}
\]

Examples are \(0\le\mu_r\le2\) in the cap-two preload and
\(c_j\le\mu_r\le c_j+1\) for exact balanced quotas.

### Theorem 2.1 (necessary and sufficient exact trade conditions)

Let \(z\) satisfy (1.5) and (2.1). For
\(\delta\in\mathbb Z^{\Gamma_H}\), put

\[
 z'=z+\delta,\qquad
 g_j^\pm=S_j^\pm\delta.                            \tag{2.2}
\]

Then \(z'\) is another integral \(H\)-safe owner successor, has the same
run vector as \(z\), and respects every interval (2.1) if and only if

\[
\boxed{
\begin{aligned}
 z+\delta&\ge0,\\
 A\delta&=0,\\
 M\delta&=0,\\
 D\delta&=0,\\
 \ell_j^\pm-\mu_j^\pm(z)
 \ \le\ g_j^\pm&\le\
 u_j^\pm-\mu_j^\pm(z)
 \qquad(1\le j\le H).
\end{aligned}}                                                     \tag{2.3}
\]

#### Proof

Necessity follows by subtracting the equations for \(z\) and \(z'\).

Conversely, the first three lines of (2.3) give

\[
 z'\in\mathbb Z_{\ge0}^{\Gamma_H},\qquad
 Az'=\mathbf1,\qquad Mz'=0.
\]

The integral overlap-circulation theorem therefore turns \(z'\) into an
\(H\)-safe owner permutation. The fourth line gives

\[
 r(z')-r(z)=D\delta=0.
\]

The last line is exactly

\[
 \ell_j^\pm\le S_j^\pm z'\le u_j^\pm.
\]

Thus all claimed properties hold. \(\square\)

No connected owner-component hypothesis occurs in Theorem 2.1. The trade
may wind through many owner cycles and memory states. Exact ownership and
chronology are expressed by \(A\delta=M\delta=0\).

### 2.1 Additional fixed-fibre constraints

Theorem 2.1 is an iff for the unrestricted safe Johnson catalogue
\(\Gamma_H\). A fixed \(D_r\)-transversal, prescribed exact-factor fibre,
or other frozen structure is not automatically encoded by \(A,M,D\).

If the extra structure has linear incidence equations

\[
                         Cz=b,                     \tag{2.4a}
\]

then the exact trade theorem acquires the additional necessary and
sufficient row

\[
                         C\delta=0.                \tag{2.4b}
\]

If compatibility is columnwise, one may instead restrict \(\Gamma_H\) to
compatible columns, but then the overlap-circulation equivalence must be
reproved for that restricted catalogue. A genuinely nonlinear fibre
condition requires its own closure theorem. Consequently the present
kernel theorem must not be quoted verbatim as an iff inside a fixed
\(D_r\)-fibre until one of these encodings is supplied.

### Corollary 2.2 (signed-circuit form)

Write

\[
 \delta=\delta^+-\delta^-,
\qquad
 \delta^\pm\in\mathbb Z_{\ge0}^{\Gamma_H},
\qquad
 \operatorname{supp}\delta^+\cap
 \operatorname{supp}\delta^-=\varnothing.
\]

For an integral base \(z\), the feasibility condition \(z+\delta\ge0\)
is equivalent to

\[
                         \delta^-\le z.             \tag{2.4}
\]

In every changed root fibre, \(A\delta=0\) removes the unique old selected
path and inserts one new selected path. The equation \(M\delta=0\) says
that these root replacements form a signed circulation in the memory
state digraph, coupled across memory components by the root-fibre
exchanges. After reversing negative flow, each pure memory flow decomposes
into directed flow cycles. This does not prove an edge-sign-alternating
circuit decomposition in the original memory graph.

The shadow matrices alone do not see this lift. A proposed target-row
circuit satisfying every marginal identity below has not thereby
established \(M\delta=0\).

## 3. The common-run effect identities

For a vector \(x\) on \(k\)-subsets, define its point-incidence vector by

\[
                         (B_kx)_v=\sum_{T\ni v}x_T.              \tag{3.1}
\]

### Theorem 3.1 (effect factorization through the run vector)

Suppose

\[
                         A\delta=0,\qquad M\delta=0.             \tag{3.2}
\]

Put

\[
                         \Delta r=D\delta.
\]

Then, for every \(1\le j\le H\),

\[
 B_{m-j}S_j^-\delta=-j\Delta r,                  \tag{3.3}
\]

\[
 B_{m+j}S_j^+\delta= j\Delta r.                  \tag{3.4}
\]

In particular, \(D\delta=0\) is equivalent to zero point effect at any
one positive depth and implies zero point effect at every depth and both
signs.

#### Proof

Safety gives on each column

\[
 \mathbf1_{\{v\in L_j(\gamma)\}}
 =\mathbf1_{\{v\in X_0\}}
  -\sum_{i=0}^{j-1}
    \mathbf1_{\{X_i\setminus X_{i+1}=\{v\}\}},     \tag{3.5}
\]

\[
 \mathbf1_{\{v\in U_j(\gamma)\}}
 =\mathbf1_{\{v\in X_0\}}
  +\sum_{i=0}^{j-1}
    \mathbf1_{\{X_{i+1}\setminus X_i=\{v\}\}}.     \tag{3.6}
\]

Root balance cancels the first terms. Memory balance makes the signed
marginal of the transition in position \(i\) equal to its marginal in
position zero: group first by \(\operatorname{pre}\gamma\), replace its
total by the equal \(\operatorname{suf}\gamma\) total, and shift the local
transition function one position. The same argument makes the signed
state marginals at positions zero and one equal. Their coordinatewise
membership difference is insertion minus deletion, so the signed
insertion and deletion marginals agree. Equations (3.3)--(3.4) follow.
\(\square\)

### Corollary 3.2 (strongest point barrier)

If a desired family of histogram effects \(g_j^\pm\) is produced by an
exact trade, then there is one integer vector \(\Delta r\), with
\(\sum_v\Delta r_v=0\), such that

\[
 B_{m-j}g_j^-=-j\Delta r,\qquad
 B_{m+j}g_j^+=j\Delta r                           \tag{3.7}
\]

for every \(1\le j\le H\).

For a run-neutral trade, all point-incidence vectors in (3.7) vanish.
This condition does not force \(g_j^\pm=0\); it places them in the
point-incidence kernels.

The identities (3.7) are necessary but not sufficient for a memory lift.
The exact sufficiency theorem is (2.3), which retains the column variable
\(\delta\).

## 4. Exact adjacent-depth shadow flow

Fix \(1\le q<H\). Every safe lower flag satisfies

\[
 L_{q+1}(\gamma)\subset L_q(\gamma),\qquad
 |L_q(\gamma)\setminus L_{q+1}(\gamma)|=1.         \tag{4.1}
\]

Define the signed lower pair flow

\[
 p_{q,T,S}^-(\delta)
 =\sum_{\substack{\gamma:
          L_q(\gamma)=T\\L_{q+1}(\gamma)=S}}
      \delta_\gamma,                               \tag{4.2}
\]

where \(S\in\partial T\). Dually, define

\[
 p_{q,U,V}^+(\delta)
 =\sum_{\substack{\gamma:
          U_q(\gamma)=U\\U_{q+1}(\gamma)=V}}
      \delta_\gamma,                               \tag{4.3}
\]

where \(V\in\nabla U\).

### Lemma 4.1 (exact two marginals)

\[
 g_{q,T}^-=\sum_{S\in\partial T}p_{q,T,S}^-,       \tag{4.4}
\]

\[
 g_{q+1,S}^-=
 \sum_{\substack{T\supset S\\|T\setminus S|=1}}
 p_{q,T,S}^-,                                     \tag{4.5}
\]

and

\[
 g_{q,U}^+=\sum_{V\in\nabla U}p_{q,U,V}^+,         \tag{4.6}
\]

\[
 g_{q+1,V}^+=
 \sum_{\substack{U\subset V\\|V\setminus U|=1}}
 p_{q,U,V}^+.                                     \tag{4.7}
\]

#### Proof

Every column has exactly one adjacent-depth lower pair and exactly one
adjacent-depth upper pair. Summing (4.2)--(4.3) first over the deeper
endpoint and then over the shallower endpoint gives the two marginals.
\(\square\)

Equations (4.4)--(4.7) are the exact local effect identities. They rule
out independently chosen effects at adjacent depths even before memory
liftability is considered.

Conversely, given integer vectors \(g_q,g_{q+1}\) of equal total sum, an
integer signed edge flow on the complete consecutive-rank inclusion graph
with those two marginals exists. This follows by routing unit imbalances
along a spanning tree of the connected bipartite inclusion graph.
Therefore the abstract two-row marginal lift is not the difficult step.
The hard condition is to prove that the chosen \(p\) is the projection of one
\(\delta\) satisfying \(A\delta=M\delta=0\) and every other-depth cap.

## 5. Exact shadow-turnover theorem

Let \(T\) be a lower target at depth \(1\le q<H\). Assume that every member of
its lower shadow is saturated:

\[
 \mu_{q+1,S}^-(z)=u_{q+1,S}^-
 \qquad(S\in\partial T).                          \tag{5.1}
\]

### Theorem 5.1 (a locked target forces an alternating pivot)

Let \(\delta\) satisfy the exact trade conditions (2.3), and suppose

\[
                         g_{q,T}^-\ge1.             \tag{5.2}
\]

Then there are \(S\in\partial T\) and another rank-\((m-q)\) target
\(T'\ne T\), with \(S\subset T'\), such that

\[
                         p_{q,T,S}^->0,\qquad
                         p_{q,T',S}^-<0.            \tag{5.3}
\]

Thus the projected trade contains the alternating shadow pivot

\[
                         T\to S\leftarrow T'.       \tag{5.4}
\]

#### Proof

By (4.4) and (5.2), some \(S\in\partial T\) has
\(p_{q,T,S}^->0\). Since \(S\) is saturated, cap safety gives

\[
                         g_{q+1,S}^-\le0.
\]

Using (4.5),

\[
 \sum_{\substack{T''\supset S\\|T''\setminus S|=1}}
 p_{q,T'',S}^-\le0.
\]

The \(T\)-summand is positive, so at least one other summand is negative.
This is (5.3). \(\square\)

The upper statement is identical with
\(U\to V\leftarrow U'\), where \(V\in\nabla U\).

Theorem 5.1 strengthens the cardinal shadow-lock statement. It does not
merely say that some saturated row must change: it identifies the exact
alternating incidence pivot forced in the projection of every legal
unlocking trade.

### Corollary 5.2 (coordinate balance of projected pivots)

Write

\[
 T=S+x,\qquad T'=S+y.
\]

The elementary pivot \(T\to S\leftarrow T'\) changes the depth-\(q\)
point vector by

\[
                         e_x-e_y.                  \tag{5.5}
\]

Hence a collection of lower pivots which leaves depth \(q+1\) unchanged
is point-neutral exactly when its directed coordinate arcs

\[
                         y\longrightarrow x
\]

form an Eulerian signed multigraph: indegree equals outdegree at every
coordinate.

This is a useful projected design rule for a run-neutral absorber. It is
not sufficient for legality, because the coordinate-balanced pivot
collection may fail to lift through \(M\delta=0\), or may violate another
depth or the upper sign.

## 6. The exact abstract escape operation

### Definition 6.1 (memory-kernel shadow-unlocking circuit)

Relative to an integral base circulation \(z\), a lower unlocking circuit
for a demanded target \(T\) is an integer vector
\(\delta\in\mathbb Z^{\Gamma_H}\) satisfying:

\[
\begin{aligned}
 z+\delta&\ge0,\\
 A\delta&=M\delta=D\delta=0,\\
 C\delta&=0\quad\text{when fixed-fibre rows are active},\\
 \ell-\mu(z)&\le S\delta\le u-\mu(z),\\
 (S_q^-\delta)_T&\ge1.
\end{aligned}                                      \tag{6.1}
\]

An upper unlocking circuit is defined dually.

### Theorem 6.2 (legality and sufficiency)

Every circuit in Definition 6.1 is a legal exact \(H\)-safe successor
operation. It preserves:

1. every owner exactly once;
2. the full \(H\)-step chronology;
3. the common coordinate run vector;
4. every signed target cap and floor at every protected depth;
5. every additional fixed-fibre row \(Cz=b\), when present.

It increases the demanded target load by at least one. If that target was
shadow-locked, its adjacent-depth projection necessarily contains the
alternating turnover in Theorem 5.1.

Conversely, the difference of any two integral \(H\)-safe successors with
these preservation properties and with increased load at \(T\) is a
circuit in Definition 6.1.

#### Proof

The forward implication is Theorem 2.1 together with the last line of
(6.1). The turnover conclusion is Theorem 5.1. The converse follows by
subtracting the two root, memory, run, and cap systems. \(\square\)

This is the desired escape operation without a closed
component-switch assumption. A circuit may be supported on a global
alternating collection of old and new \(H\)-path columns.

## 7. What abundance theorem remains open

The exact algebra above leaves seven genuinely nontrivial requirements.

1. **Integer memory lift.** A signed shadow flow \(p\) with correct
   marginals and coordinate balance is not guaranteed merely by those
   identities to lie in the projection of
   \[
      \ker_{\mathbb Z}A\cap\ker_{\mathbb Z}M\cap\ker_{\mathbb Z}D.
   \]
2. **Sign compatibility with the base.** Negative columns must satisfy
   \(\delta^-\le z\); an abstract lattice vector may try to remove an
   unselected path.
3. **All-depth caps.** A pivot designed at \(q,q+1\) has forced shadows at
   every other depth and at the opposite sign.
4. **Short support.** To absorb \(o(W)\) defects economically, one needs
   circuits using few roots or a bounded amortized number of roots per
   repair.
5. **Bounded overlap and parallel routing.** Many demanded targets must be
   assigned circuits whose positive and negative row consumptions do not
   collide.
6. **Cycle and seam control.** The resulting successor must retain
   \(o(W/H)\) owner cycles, or the final linearization toll is not \(o(W)\).
   The number of cycles is not a linear row of (2.3).
7. **Fixed-fibre legality.** In the \(D_r\)-transversal lane, one must
   encode and preserve the transversal constraint by \(C\delta=0\), or
   prove the restricted-column overlap theorem. The unrestricted
   \(A/M/D\) kernel does not supply this automatically.

The symmetric fractional circulation proves none of these integer
abundance properties. The certified 24-owner pair-frame trade gives one
nonzero run-neutral kernel-shadow signature, but its depth-two
multiplicity and global packing are not cap-safe at the required scale.

A sufficient positive theorem would say that, throughout the intended
rounding trajectory, every demanded target admits a circuit (6.1) of
support \(O_A(1)\) or \(m^{o(1)}\), and that a linear-sized family of such
circuits has bounded row and memory overlap, quantitative sequential cap
slack, total support and seam toll \(o(W)\), \(o(W/H)\) final owner cycles,
and a certified literal-OR linearization. No such theorem is currently
proved.

## 8. Grouped endpoint Hall and complement symmetry

MATH_THEOREM_H_MEMORY_COMPLEMENT_GROUPED_HALL_AND_SLAB_CUT_TEST_20260726.md
recasts the kernel condition as an endpoint/path-cover theorem. For
owner-disjoint path groups, \(M z=0\) is exactly cancellation of all
path endpoints. Coordinate complementation acts freely on memory states
and exchanges lower traces with complements of upper traces.

In an endpoint-separated connector atlas, complement-symmetric closure is
therefore a perfect matching problem on endpoint orbits, with the usual
Hall and alternating-path theorem. In a general slab catalogue, residual
memory cycles are only projections: a legal augmentation must retain
whole group differences. Its exact one-sided gain is the common-background
target-union gain, not an endpoint quantity.

Every complete cross-parent slab resolution is itself a zero-boundary
memory circulation. Hence slabs remove the static mixed-profile cut as a
formal invariant, but the present Hamming-two reachability theorem gives
no lower bound on their literal target escape. The exact positive target
is a complement-closed family of group-valid memory circuits with
quantitatively positive union gain.

An independent audit verified the \(A/M/D\)/cap iff, the arbitrary-signed
\(\delta\) point identities, the adjacent-depth marginal equations, and
the forced locked-target pivot. It also identified and corrected the
signed-circulation wording and the fixed-\(D_r\) scope requirement above.
