# Protected odd upper-diamond marginals: exact flow extensions and the synchronization gate

Date: 2026-08-01  
Lane: additive-one rooted Catalan forest / protected pivot host  
Status: two unconditional exact protected-extension theorems.  The first
selects one diamond for every upper colour with distinct lower colours.  The
second selects one Johnson edge for every upper colour with middle degree at
most two.  Both retain a fixed (O(\sqrt m)) pivot bank in the range already
available to the protected-factor theorem.  Their simultaneous realization,
and then acyclicity/rooting, remain open.

## 1. Setup

Let

\[
 \Omega=[2m-1],\qquad
 \mathcal L={\Omega\choose m-1},\qquad
 \mathcal M={\Omega\choose m},\qquad
 \mathcal U={\Omega\choose m+1}.
\]

Write

\[
 W=|\mathcal L|=|\mathcal M|={2m-1\choose m},
 \qquad U=|\mathcal U|,
 \qquad C=W-U=\operatorname {Cat}_m.                  \tag{1.1}
\]

An upper diamond is a pair `(L,R)` with

\[
 L\in\mathcal L,\qquad R\in\mathcal U,\qquad L\subset R.
\]

Writing `R-L={a,b}`, its physical Johnson edge is

\[
                    \psi(L,R)=\{L+a,L+b\}.             \tag{1.2}
\]

The desired first-stage rooted Catalan object is a set of `U` such diamonds
which uses every `R` once, uses every `L` at most once, and whose physical
graph has maximum degree at most two, ideally with no cycle.

## 2. Exact protected upper/lower transversal

Let (D) be the bipartite distance-two containment graph on
\(\mathcal U\mathbin{\dot\cup}\mathcal L\).

### Lemma 2.1 (two-step central surplus)

For every nonempty (A\subseteq\mathcal U),

\[
                         |N_D(A)|\ge |A|+m.             \tag{2.1}
\]

#### Proof

Let \(\partial A\subseteq\mathcal M\) be the first lower shadow.  The sharp
one-step central-shadow theorem gives

\[
                         |\partial A|\ge |A|+m.         \tag{2.2}
\]

The containment graph between ranks `m` and `m-1` of `[2m-1]` is balanced
and `m`-regular.  Edge counting, equivalently normalized matching, gives

\[
                         |\partial(\partial A)|
                              \ge|\partial A|.          \tag{2.3}
\]

The left side is `|N_D(A)|`.  Combining (2.2)--(2.3) proves (2.1).
\(\square\)

### Theorem 2.2 (protected outer-transversal extension)

Let (P) be any matching in (D) of size (t\le m).  Then (P) extends to a
matching saturating every upper vertex (R\in\mathcal U).

Equivalently, any at most `m` prescribed upper/lower diamond tickets with
separately distinct upper and lower colours extend to an upper-exact,
lower-injective diamond selection.

#### Proof

Delete the `t` prescribed vertices on each shore.  For every nonempty family
`A` of remaining upper vertices, Lemma 2.1 gives

\[
 |N_D(A)\setminus V_{\mathcal L}(P)|
       \ge |A|+m-t\ge|A|.                              \tag{2.4}
\]

Hall saturates the remaining upper vertices.  Adjoin `P`. \(\square\)

This theorem is exact and integral.  It imposes no control on the degrees or
cycles of the physical graph `psi(P)`.

## 3. Exact protected upper/owner cap-two extension

Let (G) be the ordinary incidence graph on
\(\mathcal U\mathbin{\dot\cup}\mathcal M\), with (T\sim R) iff
\(T\subset R\).  It is ((m+1,m-1))-biregular.

A subgraph (F\subseteq G) with

\[
 d_F(R)=2\quad(R\in\mathcal U),
 \qquad d_F(T)\le2\quad(T\in\mathcal M)                \tag{3.1}
\]

selects, at every upper colour, two distinct middle facets.  Joining those
facets gives one Johnson edge of upper colour `R`, and its physical degree
at an owner `T` is exactly `d_F(T)`.  Thus (3.1) is the cap-two upper-exact
problem with the lower-colour row omitted.

For (A\subseteq\mathcal U), put

\[
 d_A(T)=|\{R\in A:T\subset R\}|,
 \qquad S_2(A)=\sum_{T\in\mathcal M}\min\{2,d_A(T)\}.  \tag{3.2}
\]

### Lemma 3.1 (capacity-two surplus)

For (m\ge3) and every nonempty (A\subseteq\mathcal U),

\[
                         S_2(A)-2|A|\ge m-1.            \tag{3.3}
\]

#### Proof

Put `a=|A|`, `N=|N_G(A)|`, and `g=N-a`.  Lemma 2.1's first-shadow step
gives `g>=m`.  Every right degree satisfies `1<=d_A(T)<=m-1`, and for this
range

\[
       \min\{2,j\}\ge1+{j-1\over m-2}.                 \tag{3.4}
\]

Also

\[
                         \sum_Td_A(T)=(m+1)a.           \tag{3.5}
\]

Summing (3.4) over `N_G(A)` and subtracting `2a` gives

\[
\begin{aligned}
 S_2(A)-2a
 &\ge N+{(m+1)a-N\over m-2}-2a\\
 &= {2a+(m-3)g\over m-2}\\
 &\ge {2+(m-3)m\over m-2}=m-1.                        \tag{3.6}
\end{aligned}
\]

For `m=3`, (3.4) is equality and the same calculation applies. \(\square\)

### Theorem 3.2 (small protected cap-two extension)

Let (P\subseteq G) have maximum degree at most two and

\[
                             |E(P)|\le m-1.             \tag{3.7}
\]

Then `P` extends to a subgraph `F` satisfying (3.1).

#### Proof

Suppose not, and take an edge-minimal nonextendable (H\subseteq P).  On the
residual graph (G_0=G-E(H)), give an upper vertex residual demand

\[
 b(R)=2-d_H(R)
\]

and a middle vertex residual capacity

\[
 b(T)=2-d_H(T).
\]

The bipartite capacitated matching theorem (equivalently max-flow min-cut)
says that completion exists iff, for every (A\subseteq\mathcal U),

\[
 \sum_{R\in A}b(R)
 \le
 \sum_{T\in\mathcal M}
       \min\{b(T),d_{G_0}(T,A)\}.                      \tag{3.8}
\]

Choose a violating `A`.  No edge of `H` is incident with `A`.  Indeed, if
`e=RT in H` with `R in A`, delete `e` from `H`.  In (3.8) the left side
rises by one.  Restoring `e` and raising `b(T)` can increase the right side
by at most one.  The strict integral violation therefore survives,
contradicting edge-minimality.

Consequently the left side of (3.8) is `2|A|` and
`d_(G_0)(T,A)=d_A(T)`.  Moreover

\[
 \min\{2-d_H(T),d_A(T)\}
 \ge \min\{2,d_A(T)\}-d_H(T).                         \tag{3.9}
\]

Writing `h=|E(H)|`, the right side of (3.8) is at least

\[
 S_2(A)-h\ge2|A|+(m-1)-h\ge2|A|,                     \tag{3.10}
\]

by Lemma 3.1 and `h<=m-1`.  This contradicts the strict violation.
\(\square\)

Without protection, (3.1) also follows immediately by properly
`(m+1)`-edge-colouring the bipartite graph `G` and taking any two colour
classes.  Theorem 3.2 is stronger because it retains an arbitrary small
2-bounded incidence bank.

It does not make the intersections of the selected Johnson edges distinct,
and it does not exclude cycle components.

## 4. An exact outer-rainbow forest from Greene--Kleitman

There is also one exact construction which combines both outer colours and
acyclicity, but not owner cap two.

Take the standard Greene--Kleitman symmetric-chain decomposition of
\(B_{2m-1}\).  Every (R\in\mathcal U) lies on a unique chain containing the
consecutive ranks

\[
                         L\subset T\subset R,
 \qquad |L|=m-1,\quad|T|=m.                            \tag{4.1}
\]

Let `H` be the other middle corner of `[L,R]`, and select the edge `TH`.

### Theorem 4.1 (odd rooted Catalan forest, without cap two)

The selected (U) edges use every upper colour exactly once and distinct
lower colours.  Their physical graph is a spanning forest on
\(\mathcal M\) with exactly

\[
                         W-U=C=\operatorname {Cat}_m   \tag{4.2}
\]

components.

#### Proof

The SCD partitions every layer and a chain contains at most one set of each
rank, so the upper and lower colours in (4.1) are separately injective; all
upper colours occur.

Use the standard Greene--Kleitman convention which greedily brackets every
`01`, and then turns the unbracketed zero positions into ones from left to
right.  If `a<b` are the two successive free-zero positions used between
`L` and `R`, then

\[
                         T=L+a,\qquad H=L+b.
\]

Orient `T->H`.  The potential

\[
                         \omega(S)=\sum_{x\in S}x
\]

rises by `b-a>0`,
so there is no directed cycle.  Every selected vertex has outdegree at most
one; an undirected cycle would force every vertex on it to have outdegree
one and hence would be directed.  Thus the graph is a forest.  Its component
count is vertices minus edges, namely `W-U=C`. \(\square\)

The degree defect is real and linear in `m`.  Put

\[
                         X_*=1(01)^{m-1}.              \tag{4.3}
\]

For `1<=j<=m-1`, the word

\[
              L_j=1(01)^{j-1}00(01)^{m-1-j}           \tag{4.4}
\]

has the two displayed zeros as its first two free zeros, and its alternate
middle corner is `X_*`.  These give `m-1` distinct selected edges incident
with `X_*`.  The chain of `X_*` does not reach rank `m+1`, so `X_*` is not
an on-chain tail of another selected edge.  In fact these are all its
incident selected edges: deleting the initial one from `X_*` leaves only
one free zero, while deleting the one in the `j`th `01` pair leaves exactly
the displayed `00`, whose first free zero is forced.  Hence its physical
degree is exactly `m-1`, violating cap two for every `m>=4`.  The weaker
lower bound `d(X_*)\ge m-1` already suffices for the obstruction.

Thus even the exact outer-rainbow Catalan forest does not solve the owner
capacity row.

## 5. The fixed tight-pivot bank survives both marginal theorems

One repaired collared pivot path has `3h` Johnson transitions.  Suppose `H`
copies have globally distinct upper and lower q1 colours and pairwise
disjoint owner/lower incidence resources.  Let `P_dia` be their `3Hh`
upper/lower diamond tickets, and let `P_inc` be their `6Hh` lifted
upper/owner incidences.

If

\[
                             6Hh\le m-2,               \tag{5.1}
\]

then

\[
                    |P_{dia}|=3Hh\le m,\qquad
                    |P_{inc}|=6Hh\le m-1.              \tag{5.2}
\]

Theorem 2.2 therefore extends `P_dia` to an upper-exact lower-injective
diamond selection.  Independently, Theorem 3.2 extends `P_inc` to an
upper-exact cap-two owner selection.

Both statements retain the same literal pivot bank.  They do not assert
that one common completion has both properties.

For fixed `H` and `h=\Theta(\sqrt m)`, condition (5.1) holds in every
sufficiently large dimension.

## 6. Why the two flow theorems do not synchronize automatically

Introduce one binary variable `x_(L,R)` for every upper diamond.  The exact
simultaneous non-topological selector is

\[
\begin{aligned}
 \sum_{L\subset R}x_{L,R}&=1 &&(R\in\mathcal U),\\
 \sum_{R\supset L}x_{L,R}&\le1 &&(L\in\mathcal L),\\
 \sum_{(L,R):\,T\in\psi(L,R)}x_{L,R}&\le2
                                      &&(T\in\mathcal M),\\
 x_{L,R}&\in\{0,1\}.                                  \tag{6.1}
\end{aligned}
\]

The first two rows alone are Theorem 2.2.  The first and third rows alone
are Theorem 3.2 after replacing one selected diamond by its two incidences.
Their conjunction is not an ordinary bipartite flow.

Already at one fixed lower colour `L` and three absent coordinates `a,b,c`,
the three columns

\[
 (L,L+a+b),\quad(L,L+a+c),\quad(L,L+b+c)
\]

on the three owner rows `L+a,L+b,L+c` contain

\[
 \begin{pmatrix}
 1&1&0\\
 1&0&1\\
 0&1&1
 \end{pmatrix},
 \qquad\det=-2.                                       \tag{6.2}
\]

Thus the natural constraint matrix is not totally unimodular; the two
marginal max-flow proofs cannot be identified by a direct TU argument.

The marginal implications also fail inside the Boolean host.

* For `m>=4`, choose one owner `T`, three distinct outside points `b_i`,
  and three distinct `a_i in T`.  The three diamonds

  \[
       (T-a_i,\ T+b_i),\qquad i=1,2,3,                 \tag{6.3}
  \]

  have distinct upper and lower colours but all physical edges meet `T`.
  Theorem 2.2 extends them to a complete outer transversal, still with
  owner degree at least three.
* For `m>=5`, fix `L` and four distinct absent points `a,b,c,d`.  The two
  physical edges

  \[
       (L+a)(L+b),\qquad(L+c)(L+d)                     \tag{6.4}
  \]

  form a four-incidence, degree-one protected bank whose two upper colours
  are distinct but whose lower colour is repeated.  Theorem 3.2 extends it
  to a complete cap-two upper selection, still repeating `L`.

So neither exact marginal theorem contains the other.

There is nevertheless no scalar or fractional obstruction.  Give every
diamond weight

\[
                         {1\over {m+1\choose2}}.        \tag{6.5}
\]

Every upper row has load one, every lower row has load
`(m-1)/(m+1)<1`, and every owner row has load
`2(m-1)/(m+1)<2`.  The remaining gate is integral correlation.

## 7. Exact remaining theorem

The next non-topological statement is:

> **Protected odd upper-diamond synchronization.**  System (6.1) has an
> integral solution containing the repaired (O(\sqrt m)) pivot bank.

Once this holds, its physical graph has maximum degree two and is a disjoint
union of paths and cycles.  The only remaining physical-topology condition
is to eliminate the cycles, equivalently add the graphic inequalities

\[
       |E(S)|\le |S|-1\qquad(\varnothing\ne S\subseteq\mathcal M). \tag{7.1}
\]

For the fixed-`M0` rooted Hamilton-path certificate there is one further
correlation: orienting the path components must yield tail/head incidences
which extend to the same perfect root matching and whose `C-1` connectors
use the free ports as one directed component path.  An unrooted cap-two
forest alone does not supply that head/root condition.

This qualification is essential, not merely formal.  The independent
fixed-root audit
`MATH_THEOREM_OWNER_LAYER_RAINBOW_PATH_CUT_COUNTEREXAMPLE_AND_ACYCLIC_HALL_20260801.md`
gives, already at `m=3`, three protected arcs with distinct tails, heads and
upper colours which form a directed linear forest but do not extend to any
Hamilton path for their fixed root matching.  The pivot phase and the root
matching must therefore be selected prospectively and in correlation.

Thus this note closes both protected flow marginals and an exact
outer-rainbow forest marginal.  It does not claim their common integral
selector, acyclicity after synchronization, or the rooted Catalan connector.
