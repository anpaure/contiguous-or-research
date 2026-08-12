# Diamond rectangles, alternating switches, and the true GK edit distance

Date: 2026-07-31  
Status: exact switch calculus and exact Greene--Kleitman linearization
enumerator; no all-dimension physical matching is claimed

## 1. Middle degrees are rectangle occupancies

Let \(|\Omega|=2m\), and put

\[
 \mathcal L=\binom\Omega{m-1},\qquad
 \mathcal U=\binom\Omega{m+1},\qquad
 \mathcal X=\binom\Omega m.
\]

Write \(B_m\) for the inclusion graph between \(\mathcal L\) and
\(\mathcal U\).  An edge \(e=(L,U)\) is the Boolean diamond whose lifted
Johnson edge is

\[
 \psi(e)=\{L+a,L+b\},\qquad U\setminus L=\{a,b\}.
\]

For \(X\in\mathcal X\), define the complete *diamond rectangle*

\[
 \mathcal R_X={(L,U):L\subset X\subset U, |L|=m-1, |U|=m+1\}.
 \tag{1.1}
\]

Its two shores have size \(m\), so \(\mathcal R_X\cong K_{m,m}\).

### Theorem 1 (rectangle identity)

For every edge set \(M\subseteq E(B_m)\),

\[
 \boxed{\deg_{\Psi(M)}(X)=|M\cap\mathcal R_X|.}       \tag{1.2}
\]

Every diamond edge belongs to exactly two rectangles, namely those indexed
by the two endpoints of its lifted Johnson edge.

#### Proof

The lifted edge \(\psi(L,U)\) is incident with \(X\) exactly when
\(L\subset X\subset U\).  This is precisely membership of \((L,U)\) in
\(\mathcal R_X\).  The two intermediate rank-\(m\) sets between \(L\) and
\(U\) are the two endpoints of \(\psi(L,U)\), proving the second assertion.
\(\square\)

Thus the physical degree gate is not an opaque geometric condition on a
perfect matching.  It is the family of capacity rows

\[
                  |M\cap\mathcal R_X|\le2
                  \qquad(X\in\mathcal X).              \tag{1.3}
\]

Together with the usual graphic inequalities for \(\Psi(M)\), these rows
are exactly the spanning-linear-forest gate.

## 2. Exact alternating-cycle switch law

Let \(M\) be a perfect matching of \(B_m\).  Let \(C\) be an alternating
cycle, with old matching half \(C^-\subset M\) and new half
\(C^+=C\setminus C^-\).  Put

\[
 M'=M\triangle C=(M\setminus C^-)\cup C^+.
\]

### Theorem 2 (switch, degree, forest, and filter laws)

1. \(M'\) is again a perfect lower--upper colour matching.
2. At every middle vertex,
   \[
   \deg_{\Psi(M')}(X)-\deg_{\Psi(M)}(X)
    =|C^+\cap\mathcal R_X|-|C^-\cap\mathcal R_X|.       \tag{2.1}
   \]
3. Assume \(F=\Psi(M)\) is a forest.  Delete the old lifted edges
   \(A=\Psi(C^-)\), contract every component of \(F-A\), and insert the
   new lifted edges \(B=\Psi(C^+)\) in the contracted multigraph
   \(\Gamma_C\).  Then
   \[
                    \Psi(M')\text{ is a forest}
       \quad\Longleftrightarrow\quad
                    \Gamma_C\text{ is a forest without loops}.          \tag{2.2}
   \]
4. If a prescribed partial matching \(D\) (for example a period-three
   filter bank) is to remain literally fixed, the switch preserves it
   exactly when the alternating cycle avoids every endpoint of \(D\).
   Equivalently all switches take place in
   \(B_m-V(D)\).  If only clean-subgroup equivariance is required, take a
   quotient alternating cycle and lift its full orbit; every exceptional
   quotient row is still matched once, although its chosen phase may change.

#### Proof

The first statement is the standard alternating-cycle exchange.  Equation
(2.1) is Theorem 1 applied before and after the exchange.  A cycle in
\((F-A)+B\) contracts to a loop or cycle of \(\Gamma_C\), and conversely a
loop or cycle of \(\Gamma_C\) expands through the unique paths in the
components of the forest \(F-A\).  This proves (2.2).  Finally, a matching
edge of \(D\) changes exactly when its matched endpoint lies on the
alternating cycle.  The quotient assertion follows from freeness of the
clean action on both shores. \(\square\)

This supplies a complete, checkable safety test for a large switch.  Mere
colour preservation does not imply physical acyclicity.

## 3. Every square is a hinge rotation

Every four-cycle of \(B_m\) has a unique middle pivot \(X\).  Choose
distinct \(a,b\in X\) and distinct \(y,z\notin X\).  Its old matching half
may be written

\[
 (X-a,X+y),\qquad (X-b,X+z),                            \tag{3.1}
\]

and its new half is

\[
 (X-a,X+z),\qquad (X-b,X+y).                            \tag{3.2}
\]

The corresponding physical edges change from

\[
 X\!-!(X-a+y),\quad X\!-!(X-b+z)
\]

to

\[
 X\!-!(X-a+z),\quad X\!-!(X-b+y).                   \tag{3.3}
\]

In particular every square is wholly contained in \(\mathcal R_X\), and

\[
             \deg_{\Psi(M')}(X)=\deg_{\Psi(M)}(X).      \tag{3.4}
\]

It reroutes two leaves of a fixed hinge; it never changes the load at the
hinge itself.

If the four nonpivot middle vertices in (3.3) are denoted by old leaves
\(P,Q\) and new leaves \(P',Q'\), then for

\[
                  \mathfrak b(F)=\sum_V(\deg_F(V)-2)_+
\]

the exact change is

\[
 \mathfrak b(F')-\mathfrak b(F)
 =-1_{\deg P\ge3}-1_{\deg Q\ge3}
   +1_{\deg P'\ge2}+1_{\deg Q'\ge2}.                  \tag{3.5}
\]

When \(F\) is a forest, the square remains acyclic exactly when, after the
two old hinge edges are removed, the two new leaves lie in two distinct
components, neither equal to the component containing \(X\).  This is the
two-edge specialization of (2.2).

Consequently arbitrary rewiring confined to the \(m\times m\) rectangle
\(\mathcal R_X\) can never repair an overload at \(X\).  At least one
alternating cycle must cross that rectangle boundary.

## 4. The GK components are pointed plane trees

The standard Greene--Kleitman projection matching has a useful exact
description which also corrects an earlier overestimate of its edit
distance.

Under the usual Dyck-word/plane-tree bijection, a central binary word is a
pair \((T,v)\), where \(T\) is a rooted plane tree with \(m\) edges and
\(v\) is one of its \(m+1\) vertices.  In the factorization along the
root--\(v\) path, the GK projection switch

\[
                  1D0\longmapsto0D1                    \tag{4.1}
\]

moves the distinguished vertex \(v\) to its parent and leaves \(T\)
unchanged.  Hence:

### Theorem 3 (plane-tree component theorem)

The \(\operatorname {Cat}_m\) physical components of the GK projection are
exactly the underlying trees of all rooted plane trees with \(m\) edges,
one component for each tree.  The \(m+1\) middle vertices in that component
are its possible distinguished vertices.

#### Proof

A radius-zero central word is a Dyck word and hence a rooted plane tree.
For a word of radius \(d\), its standard unmatched-letter factorization is
the contour decomposition of a pointed plane tree along the path of length
\(d\) from its root to the marked vertex.  Formula (4.1), which is the
literal GK middle projection, removes the last edge of this distinguished
path.  Repetition reaches the unique radius-zero Dyck word without changing
the side forests, hence without changing the underlying plane tree.
Conversely every nonroot pointed vertex has its parent edge, so all
\(m+1\) pointings occur and the component is exactly \(T\). \(\square\)

## 5. Exact maximum linear subforest of the GK projection

For a rooted plane tree \(T\), let \(A(T)\) be the maximum number of edges
retained with degree at most two when no parent edge enters the root, and
let \(B(T)\) be the corresponding maximum when one parent edge is already
used (the parent edge itself is not counted).  For children \(T_i\), put

\[
             g_i=1+B(T_i)-A(T_i)\in\{0,1\}.             \tag{5.1}
\]

If \(c\) children have \(g_i=1\), then

\[
 \begin{aligned}
 A(T)&=\sum_iA(T_i)+\min(2,c),\\
 B(T)&=\sum_iA(T_i)+\min(1,c).                          \tag{5.2}
 \end{aligned}
\]

The assertion \(g_i\in\{0,1\}\) and the formulas follow together by
induction.  Let

\[
 \delta(T)=|E(T)|-A(T),\qquad
 \Delta_m=\sum_{T\in\mathcal T_m}\delta(T),            \tag{5.3}
\]

where \(\mathcal T_m\) is the set of rooted plane trees with \(m\) edges.

### Theorem 4 (true GK edit distance)

The largest linear subforest contained in the GK projection has exactly

\[
                       m\operatorname {Cat}_m-\Delta_m \tag{5.4}
\]

edges.  Therefore every perfect lower--upper matching whose physical lift
is a linear forest differs from the GK matching in at least \(\Delta_m\)
matching edges.

#### Proof

The GK components are disjoint trees by Theorem 3, so their degree-two
subforest optimizations separate and (5.2) is exact on every component.
This proves (5.4).  The common edges of the GK matching and any matching
with a linear physical lift form a linear subforest of the GK projection.
They therefore number at most (5.4), while both matchings contain
\(m\operatorname {Cat}_m\) edges. \(\square\)

This replaces the false bound \(W/2\) previously stated in
`GK_PROJECTION_COUNTS.md`: that argument forgot that one may delete a
vertex's outgoing edge and retain two incoming edges.  A star already
refutes the old step.

There is an exact bivariate generating function for \(\Delta_m\).  Split
trees into type \(G\), where \(A(T)=B(T)\), and type \(H\), where
\(A(T)=B(T)+1\), and put

\[
 G(z,u)=\sum_{T\in G}z^{|E(T)|}u^{\delta(T)},\qquad
 H(z,u)=\sum_{T\in H}z^{|E(T)|}u^{\delta(T)}.
\]

With \(P=zG\) and \(Q=zuH\), the root sequence decomposition gives

\[
 \boxed{
 \begin{aligned}
 G&={1\over1-Q}+{P\over(1-Q)^2},\\
 H&={P^2\over(1-Q)^2(1-Q-uP)}.
 \end{aligned}}                                         \tag{5.5}
\]

Consequently

\[
 \Delta_m=[z^m]\,\left.\partial_u(G+H)\right|_{u=1}.   \tag{5.6}
\]

The first values are

\[
\begin{array}{c|rrrrrrrr}
m&1&2&3&4&5&6&7&8\\ \hline
\Delta_m&0&0&2&12&51&204&815&3236.
\end{array}                                             \tag{5.7}
\]

Finally, let \(p\in(0,1)\) be the unique root of

\[
                     p^3+2p^2-p-1=0.                   \tag{5.8}
\]

Standard conditioned-plane-tree singularity analysis applied to (5.5)
gives

\[
 {\Delta_m\over m\operatorname {Cat}_m}\longrightarrow
 \mu={1+p-p^2\over(1+p)^2}
      =0.356895867892\ldots .                           \tag{5.9}
\]

For completeness, the same constant follows from the critical geometric
Galton--Watson representation of a uniform plane tree.  A child has type
\(G\) with probability \(p\), and

\[
 p={1\over1+p}+{p\over(1+p)^2}.
\]

The root deletion toll is its number of children minus the smaller of two
and its number of type-\(G\) children.  Its expectation is exactly \(\mu\).

## 6. Sharp consequence for local-switch strategies

A matching alternating cycle of semilength at most \(s\) changes at most
\(s\) currently selected matching edges.  Hence any sequence taking the GK
matching to a physically linear matching needs at least

\[
                       \left\lceil{\Delta_m\over s}\right\rceil          \tag{6.1}
\]

such switches.  Square switches require at least \(\lceil\Delta_m/2\rceil\)
moves.  By (5.9), every bounded-locality strategy requires
\(\Theta\!\left(\binom{2m}m\right)\) moves.

Moreover the two alternating middle sets

\[
 E_m=\{0,2,\ldots,2m-2\},\qquad E_m^c
\]

have GK degree \(m\), and all their neighbours in the GK projection have
degree one.  Their selected matching edges lie in the rectangles
\(\mathcal R_{E_m}\) and \(\mathcal R_{E_m^c}\).  Any switches confined to
either rectangle merely permute the star spokes and leave the overload
unchanged.  Thus even the first extreme branch repair must export matching
mass across a GK component boundary.

This is a sharp impossibility for a *small local repair* of the standard GK
projection, not an obstruction to the desired all-\(m\) construction.  The
correct constructive target is a global alternating-cycle rethreading (or a
matching born inside the rectangle capacities), with every switch checked by
(2.1)--(2.2) and with the period-three filter rows retained in the residual
matching space.

## 7. A constructive two-rail mark normal form

There is a useful way to be born inside the rectangle capacities rather than
repairing GK.  Let \(\Gamma\) have size \(2m-1\), let

\[
 A_i\subset B_i\supset A_{i+1}\qquad(i\in\mathbb Z_n),
 \quad |A_i|=m-1,quad |B_i|=m,
 \quad n=\binom{2m-1}{m-1},                            \tag{7.1}
\]

be a middle-levels Hamilton cycle, and adjoin \(\infty\).  Put
\(A_i^+=A_i\cup\{\infty\}\), and define the same-rail Johnson chords

\[
 \alpha_i=A_i^+A_{i+1}^+,qquad
 \beta_i=B_iB_{i+1}.                                   \tag{7.2}
\]

Their two colour pairs are

\[
 \begin{aligned}
 \alpha_i &: ((A_i\cap A_{i+1})+\infty,\ B_i+\infty),\\
 \beta_i &: (A_{i+1},\ B_i\cup B_{i+1}).               \tag{7.3}
 \end{aligned}
\]

Let \(a_i,b_i\in\{0,1\}\) select \(\alpha_i,\beta_i\), respectively.
Assume

* the selected \(\alpha\)-lower colours enumerate
  \(\binom\Gamma{m-2}\);
* the selected \(\beta\)-upper colours enumerate
  \(\binom\Gamma{m+1}\).

Both selected banks then have size

\[
 n-K,\qquad K=\operatorname{Cat}_m,                    \tag{7.4}
\]

because \(n-\binom{2m-1}{m-2}=K\).  Define the residual shores

\[
 I=\{i:b_{i-1}=0\},\qquad J=\{j:a_j=0\}.               \tag{7.5}
\]

They both have size \(K\).  Suppose there is a bijection
\(f:I\to J\) satisfying

\[
                         A_i\subset B_{f(i)}.            \tag{7.6}
\]

For every \(i\in I\), add the cross-rail Johnson edge

\[
                         A_i^+B_{f(i)}.                 \tag{7.7}
\]

### Theorem 5 (marked two-rail matching law)

The selected same-rail chords and the cross edges (7.7) form a perfect
matching between *all* rank-\((m-1)\) and rank-\((m+1)\) colours of
\(\Gamma\cup\{\infty\}\).  Their physical degrees are exactly

\[
 \boxed{
 \begin{aligned}
 \deg(A_i^+)&=a_{i-1}+a_i+(1-b_{i-1}),\\
 \deg(B_i)&=b_{i-1}+b_i+(1-a_i).
 \end{aligned}}                                        \tag{7.8}
\]

Consequently the physical maximum degree is at most two if and only if

\[
 \boxed{
 \begin{aligned}
 a_{i-1}=a_i=1&\Longrightarrow b_{i-1}=1,\\
 b_{i-1}=b_i=1&\Longrightarrow a_i=1
 \end{aligned}}\qquad(i\in\mathbb Z_n).                \tag{7.9}
\]

Under (7.9), contract every nonempty same-rail path fragment.  The lift is a
linear forest if and only if the multigraph of cross edges between these
contracted fragments is acyclic (with cross edges incident with isolated
rail vertices retained literally).

#### Proof

The selected \(\alpha\)-edges cover exactly the lower colours containing
\(\infty\) and use the upper colour \(B_i+\infty\) when \(a_i=1\).
The selected \(\beta\)-edges cover exactly the upper colours avoiding
\(\infty\) and use lower colour \(A_i\) when \(b_{i-1}=1\).  Thus the
uncovered lower and upper colours are exactly the two shores (7.5), and a
cross edge (7.7) has colours \((A_i,B_{f(i)}+\infty)\).  The bijection gives
the perfect matching.

At \(A_i^+\), the only possible edges are its two adjacent \(\alpha\)-chords
and its unique residual cross edge; the latter occurs exactly when
\(b_{i-1}=0\).  The argument at \(B_i\) is complementary, proving (7.8).
The only way either displayed sum can exceed two gives (7.9).  With maximum
degree two, every component is a path or a cycle.  Contracting same-rail
paths preserves and reflects cycles, proving the final assertion. \(\square\)

This identifies the promising constructive alternative to GK switching.
The mark conditions (7.9) solve every rectangle-cap row locally; the remaining
tasks are the two same-rail rainbow selections, the residual containment
matching (7.6), and one global graphic condition.  Any change between two
such marked solutions decomposes into the alternating cycles of Theorem 2,
so (2.2) remains the exact exchange safety test.

If (7.6) is restricted to cross edges of the original middle-levels cycle,
the sharper trace theorem in
`MATH_THEOREM_CATALAN_MIDDLE_LEVELS_TRACE_DECORATION_EQUIVALENCE_20260731.md`
applies: the residual matching exists exactly when the marked positions
alternate by rail, is then unique, and its physical lift is cyclic exactly
when every unmarked run has length two and every marked run has odd length.
That theorem is a particularly clean sufficient subfamily of Theorem 5; the
more general containment matching here need not be unique or
middle-levels-resolvable.
