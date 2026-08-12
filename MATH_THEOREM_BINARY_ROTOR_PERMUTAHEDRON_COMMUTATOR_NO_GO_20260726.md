# Binary rotors: commuting squares pay one separation defect, while braid hexagons violate owner flow

Date: 2026-07-26

Method: pure mathematics only.  No computation, search, solver, or
external input is used.

## 0. Outcome

Put

\[
 n=2m+1,
 \qquad m\ge2.
 \tag{0.1}
\]

For a selected binary-rotor \(A\)-switch at the state

\[
 \pi=(x_1,\ldots,x_n),
 \tag{0.2}
\]

write

\[
 K_r(\pi)=\{x_{n-r+1},\ldots,x_{n-1}\},
 \qquad
 \partial_r(\pi)=
  {\bf e}_{K_r(\pi)+x_n}-
  {\bf e}_{K_r(\pi)+x_1}.
 \tag{0.3}
\]

Thus \(\partial_r\) is the rank-\(r\) summand in the exact upper--lower
rotor divergence.  The switch exchanges the cyclically adjacent pair
\(x_n,x_1\), and its endpoint arrow is \(x_1\to x_n\).

This note classifies the two elementary permutahedron commutators.

1. **A commuting four-switch square is never all-depth neutral.**  If
   its two swapped pairs are separated by ordered blocks of lengths
   \(x,y\), then the two possible defect ranks are

   \[
                        r_x=x+2,
                        \qquad r_y=y+2,
                        \qquad r_x+r_y=n.
   \tag{0.4}
   \]

   Its nested divergence vanishes at every rank except \(r_x,r_y\).
   Exactly one of these ranks lies in \(\{1,\ldots,m\}\), and at that
   rank the residual is one Johnson rectangle with

   \[
       \boxed{\frac12\|D_r\|_1=2.}
   \tag{0.5}
   \]

   Hence every formal square pays aggregate protected divergence exactly
   two.  Moreover, at rank \(m\) at least one opposite edge pair has the
   same union colour.  The selected-\(A\) union-injectivity theorem then
   forbids the square in an owner-transversal rotor circulation.

2. **A six-switch braid hexagon is algebraically perfect but physically
   illegal.**  Its six flags cancel exactly at every rank

   \[
                         \boxed{D_r=0\quad(1\le r\le m).}
   \tag{0.6}
   \]

   However, three alternating switches form a top Johnson triangle at
   rank \(m\).  Their three union colours coincide, so their forced
   \(A\)-successors have the same middle owner.  Thus no owner-transversal
   flow can contain the braid hexagon.

3. Every two-dimensional face of the ordinary permutahedron is one of
   these two types.  Therefore

   \[
   \boxed{\begin{gathered}
   \text{no elementary four-/six-switch permutahedron face is both}\\
   \text{owner-flow legal and nested-divergence zero}
   \end{gathered}}
   \tag{0.7}
   \]

4. The natural nonfacial six-cycle made from three pairwise commuting
   swaps is also nonneutral.  It bounds three commuting squares, whose
   separation rectangles have disjoint pair-parity supports.  Its exact
   protected cost is

   \[
      \boxed{{1\over2}\sum_{r=1}^m\|D_r\|_1=6.}
   \tag{0.8}
   \]

The obstruction is not a universal positivity theorem for arbitrary
four-switch sets.  Section 5 gives an explicit four-switch nested Johnson
rectangle whose divergence is zero at every rank and whose eight source
and forced-successor owners are all compatible.  It is not a
permutahedron face and is not yet a completed circulation.  Thus the
remaining constructive gate is precisely a **cross-carrier, non-face
flow completion** of that atom; adding another elementary commutator face
cannot solve it.

No coefficient-one conclusion is claimed.

## 1. The flag of one adjacent swap

Let a cyclic order contain the adjacent ordered pair \(u,v\).  Rotate it
so that

\[
                         \pi=(v,Z,u).
 \tag{1.1}
\]

The \(A\)-move swaps the cyclic pair \(u,v\) to \(v,u\).  If
\(Q_r(u)\) is the set of the \(r-1\) labels immediately preceding \(u\)
in the old cyclic order, then (0.3) becomes

\[
 \boxed{
 \partial_r(u,v)=
   {\bf e}_{Q_r(u)+u}-{\bf e}_{Q_r(u)+v}.}
 \tag{1.2}
\]

In words, the permutahedron edge \(uv\to vu\) carries the Johnson arrow
\(v\to u\), decorated by the predecessor flag of \(u\).

Only underlying sets occur in (1.2).  Consequently, if a disjoint
adjacent swap happens between an edge and its reverse traversal, the two
flag contributions remain exact opposites except at the unique rank whose
predecessor window cuts between the two labels of that other swap.  The
next section makes this statement exact.

## 2. Exact divergence of a commuting square

Write the initial cyclic order as

\[
                         C_0=(a,b,X,c,d,Y),
 \tag{2.1}
\]

where \(X,Y\) are disjoint ordered blocks, possibly empty, of lengths

\[
                         |X|=x,
 \qquad |Y|=y,
 \qquad x+y=n-4.
 \tag{2.2}
\]

Traverse the commuting square

\[
 \begin{aligned}
 C_0&=(a,b,X,c,d,Y),\\
 C_1&=(b,a,X,c,d,Y),\\
 C_2&=(b,a,X,d,c,Y),\\
 C_3&=(a,b,X,d,c,Y),\\
 C_4&=C_0.
 \end{aligned}
 \tag{2.3}
\]

Let \(D_r^\square\) be the sum of the four switch flags (1.2).

### Theorem 2.1 (complementary-rank square derivative)

Put

\[
                         r_Y=y+2,
 \qquad r_X=x+2.
 \tag{2.4}
\]

Then \(r_X+r_Y=n\), and

\[
 D_r^\square=0
 \qquad
 \left(r\notin\{r_X,r_Y\}\right).
 \tag{2.5}
\]

At the two exceptional ranks,

\[
 \begin{aligned}
 D_{r_Y}^\square
 &= {\bf e}_{Y+a+d}+{\bf e}_{Y+b+c}
   -{\bf e}_{Y+b+d}-{\bf e}_{Y+a+c},\\
 D_{r_X}^\square
 &= {\bf e}_{X+a+c}+{\bf e}_{X+b+d}
   -{\bf e}_{X+a+d}-{\bf e}_{X+b+c}.
 \end{aligned}
 \tag{2.6}
\]

Each displayed residual has four distinct coordinates and therefore

\[
                         \frac12\|D_{r_X}^\square\|_1
 =\frac12\|D_{r_Y}^\square\|_1=2.
 \tag{2.7}
\]

#### Proof

Compare the first and third edges, which traverse the \(a,b\) swap in
opposite directions.  The predecessor block before this pair is unchanged
unless it contains exactly one of \(c,d\).  Since the block \(Y\) lies
between \(d\) and \(a\), this occurs exactly when its size is

\[
                         r-1=y+1,
 \tag{2.8}
\]

that is, at \(r=r_Y\).  At this rank the first edge has core
\(Y+d\), while the reverse edge has core \(Y+c\).  Their sum is

\[
 ({\bf e}_{Y+a+d}-{\bf e}_{Y+b+d})
 +({\bf e}_{Y+b+c}-{\bf e}_{Y+a+c}),
 \tag{2.9}
\]

the first line of (2.6).  At every other rank the two contributions
cancel.

The second and fourth edges give the reciprocal calculation.  Their
predecessor blocks cut the \(a,b\) pair exactly when \(r-1=x+1\),
which is \(r=r_X\), and their residual is the second line of (2.6).
Equation (2.2) gives

\[
                         r_X+r_Y=x+y+4=n.
 \tag{2.10}
\]

All four sets in either rectangle are distinct because \(a,b,c,d\) are
distinct and disjoint from \(X,Y\).  This proves (2.5)--(2.7).
\(\square\)

Since \(n=2m+1\), exactly one of \(r_X,r_Y\) is at most \(m\).  We
therefore obtain the precise positive-cost statement.

### Corollary 2.2 (protected square cost)

For the complete protected half \(1\le r\le m\),

\[
 \boxed{
 {1\over2}\sum_{r=1}^{m}\|D_r^\square\|_1=2.}
 \tag{2.11}
\]

This cost is independent of the separation of the two swaps; the
separation only chooses the rank at which it is paid.

## 3. Owner-flow obstruction for the square

For a selected \(A\)-switch \(e\), define its rank-\(m\) union colour

\[
 U_e=K_m(e)\cup\{x_1,x_n\}.
 \tag{3.1}
\]

Its forced \(A\)-successor has middle owner \([n]\setminus U_e\).
Consequently the map \(e\mapsto U_e\) is injective on the selected
\(A\)-switches of every owner-transversal rotor circulation.

### Theorem 3.1 (no physical commuting square)

The four edges of (2.3) cannot all be selected \(A\)-switches in one
owner-transversal rotor circulation.

#### Proof

The two traversals of the \(a,b\) edge have the same rank-\(m\) core
unless \(m=r_Y\).  If \(m\ne r_Y\), they have the same endpoint pair
and the same core, hence the same union colour, contradicting (3.1).

If \(m=r_Y\), then (2.10) gives \(r_X=m+1\).  The two traversals of the
\(c,d\) edge therefore have the same rank-\(m\) core and the same union
colour, again contradicting (3.1). \(\square\)

Thus the square is already excluded by owner flow.  Corollary 2.2 is
still useful: even in a relaxed packet ledger which separates its four
sources across carriers, the elementary square leaves a nonzero protected
rank rectangle.

## 4. The braid hexagon: exact cancellation and exact owner collision

Let \(O\) be an ordered block of the remaining \(n-3\) labels, and
consider the standard braid face

\[
 \begin{aligned}
 C_0&=(O,a,b,c),\\
 C_1&=(O,b,a,c),\\
 C_2&=(O,b,c,a),\\
 C_3&=(O,c,b,a),\\
 C_4&=(O,c,a,b),\\
 C_5&=(O,a,c,b),\\
 C_6&=C_0.
 \end{aligned}
 \tag{4.1}
\]

Let \(D_r^\hexagon\) be the sum of its six switch flags.

### Theorem 4.1 (all-rank braid cancellation)

For every \(1\le r\le m\),

\[
                         \boxed{D_r^\hexagon=0.}
 \tag{4.2}
\]

#### Proof

First take the three swaps in positions one and two of the displayed
three-label block.  If \(Q_r\) is the set of the final \(r-1\) labels
of \(O\), their sum is

\[
 ({\bf e}_{Q_r+a}-{\bf e}_{Q_r+b})
 +({\bf e}_{Q_r+b}-{\bf e}_{Q_r+c})
 +({\bf e}_{Q_r+c}-{\bf e}_{Q_r+a})=0.
 \tag{4.3}
\]

At \(r=1\), the other three swaps give the coordinate telescope

\[
                         (a-c)+(b-a)+(c-b)=0.
 \tag{4.4}
\]

For \(r\ge2\), let \(J_r\) be the set of the final \(r-2\) labels of
\(O\).  The other three contributions are

\[
 ({\bf e}_{J_r+a+b}-{\bf e}_{J_r+b+c})
 +({\bf e}_{J_r+b+c}-{\bf e}_{J_r+a+c})
 +({\bf e}_{J_r+a+c}-{\bf e}_{J_r+a+b})=0.
 \tag{4.5}
\]

Equations (4.3)--(4.5) prove (4.2). \(\square\)

The two telescopes have different Johnson geometry.  At rank \(m\), the
first is a star triangle and the second is a top triangle.

### Theorem 4.2 (top-triangle owner obstruction)

No owner-transversal rotor circulation contains all six \(A\)-switches
of (4.1).

#### Proof

At rank \(m\), put

\[
                         J=J_m,
 \qquad |J|=m-2.
 \tag{4.6}
\]

The three switches in (4.5) all have the union colour

\[
                         U=J\cup\{a,b,c\}.
 \tag{4.7}
\]

Their three forced \(A\)-successors therefore have the identical middle
owner \([n]\setminus U\).  The sources are distinct, and \(A\) is a
bijection, so the successors are distinct states in one owner fibre.
This contradicts owner transversality. \(\square\)

Thus the braid face solves the signed cocycle exactly but fails the
physical owner ledger exactly.  A later inverse braid cannot repair the
already duplicated successor owner without changing the intervening
state selection; that change is a cross-carrier activation, not a legal
use of the same face.

### Corollary 4.3 (complete elementary-face no-go)

No two-dimensional permutahedron face supplies a legal zero-divergence
rotor commutator.

#### Proof

The permutahedron graph is generated by the adjacent transpositions
\(s_i\).  Two distinct generators either commute,

\[
 |i-j|>1,
 \qquad
 s_is_j=s_js_i,
\]

in which case their rank-two face is the four-cycle of Section 2, or
they are adjacent,

\[
 |i-j|=1,
 \qquad
 s_is_js_i=s_js_is_j,
\]

in which case their rank-two face is the six-cycle of Section 4.  These
are the two rank-two parabolic subgroups of the type-\(A\) Coxeter
system.  Theorems 3.1 and 4.2 exclude them respectively. \(\square\)

## 5. A zero-divergence four-switch atom outside the permutahedron face

The preceding no-go must not be promoted to a positivity statement for
arbitrary switch sets.  There is a locally owner-compatible four-switch
rectangle.

Partition the ground set as

\[
 [n]=J\sqcup R\sqcup\{a,b,c,d\},
 \qquad |J|=m-2,
 \qquad |R|=m-1.
 \tag{5.1}
\]

Fix an order \(\mathbf J\) of \(J\).  Choose orders

\[
 P_d\text{ of }R+d,
 \quad P_a\text{ of }R+a,
 \quad P_c\text{ of }R+c,
 \quad P_b\text{ of }R+b,
 \tag{5.2}
\]

each ending in a member of \(R\).  Define

\[
 \begin{aligned}
 \pi_1&=(a,P_d,\mathbf J,c,b),\\
 \pi_2&=(c,P_a,\mathbf J,b,d),\\
 \pi_3&=(b,P_c,\mathbf J,d,a),\\
 \pi_4&=(d,P_b,\mathbf J,a,c).
 \end{aligned}
 \tag{5.3}
\]

Use the \(A\)-transition at all four states.

### Proposition 5.1 (local nested rectangle)

The four switches in (5.3) satisfy

\[
                         \sum_{i=1}^4\partial_r(\pi_i)=0
 \qquad(1\le r\le m).
 \tag{5.4}
\]

Their four source owners are pairwise distinct, their four forced
\(A\)-successor owners are pairwise distinct, and no source owner equals
a successor owner.

#### Proof

At rank one the endpoint arrows are

\[
                         a\to b,
 \quad c\to d,
 \quad b\to a,
 \quad d\to c,
 \tag{5.5}
\]

and sum to zero.  For \(r\ge2\), let \(J_r\) be the set of the final
\(r-2\) labels of \(\mathbf J\).  The four contributions are

\[
 \begin{aligned}
 &{\bf e}_{J_r+b+c}-{\bf e}_{J_r+a+c},\\
 &{\bf e}_{J_r+b+d}-{\bf e}_{J_r+b+c},\\
 &{\bf e}_{J_r+a+d}-{\bf e}_{J_r+b+d},\\
 &{\bf e}_{J_r+a+c}-{\bf e}_{J_r+a+d}.
 \end{aligned}
 \tag{5.6}
\]

They telescope, proving (5.4).

The four successor owners are the underlying sets of the \(P\)-blocks:

\[
                         R+d,
 \quad R+a,
 \quad R+c,
 \quad R+b,
 \tag{5.7}
\]

and are distinct.  If \(r_i\in R\) is the last member of the
corresponding \(P\)-block, the source owners are

\[
 \begin{aligned}
 &(R-r_1)+a+d,\\
 &(R-r_2)+a+c,\\
 &(R-r_3)+b+c,\\
 &(R-r_4)+b+d.
 \end{aligned}
 \tag{5.8}
\]

Their pairs of coordinates outside \(R\) are distinct, so the source
owners are pairwise distinct.  Each source owner contains two of
\(a,b,c,d\), while every successor owner contains one; hence the two
families are disjoint. \(\square\)

Proposition 5.1 is not yet a legal rotor circulation.  The four source
arcs need selected predecessors, and the four successor arcs need
selected continuations, all without reusing an owner.  The square theorem
proves that they cannot be completed by putting the four states around one
elementary commuting face.  They require a non-face, cross-carrier flow
completion.

## 6. A nonfacial six-cycle of commuting swaps

Let \(s_1,s_2,s_3\) swap three pairwise disjoint adjacent pairs

\[
                         P_i=\{a_i,b_i\}
 \qquad(i=1,2,3)
 \tag{6.1}
\]

in one cyclic order.  The generators commute.  The word

\[
                         s_1s_2s_3s_1s_2s_3
 \tag{6.2}
\]

traces the standard six-cycle in their 3-cube.

### Theorem 6.1 (commuting-cube cost)

If \(D_r^{\rm cube}\) is the sum of the six nested switch flags along
(6.2), then

\[
 \boxed{
 {1\over2}\sum_{r=1}^{m}\|D_r^{\rm cube}\|_1=6.}
 \tag{6.3}
\]

#### Proof

In bit coordinates, the cycle is

\[
 000,100,110,111,011,001,000.
 \tag{6.4}
\]

It is the oriented boundary of three square faces: the \((1,2)\)-face
at bit 3 equal to zero, the \((2,3)\)-face at bit 1 equal to zero, and
the \((1,3)\)-face at bit 2 equal to one.  Internal cube edges occur in
opposite directions and cancel as nested flags.  Therefore

\[
 D^{\rm cube}=\pm D^{12}\pm D^{23}\pm D^{13},
 \tag{6.5}
\]

where each \(D^{ij}\) is the commuting-square derivative of Theorem 2.1.
Each square contributes one protected separation rectangle of
half-\(\ell^1\) norm two.

It remains to rule out cancellation between those rectangles.  Every
target in the \((i,j)\)-rectangle contains exactly one label from each of
\(P_i,P_j\).  Its predecessor core contains either both labels or no
label from the remaining pair \(P_k\): the interval boundary already
cuts one of \(P_i,P_j\), and cannot also cut the disjoint adjacent pair
\(P_k\).  Thus the three rectangle supports have, modulo two, the
pair-count signatures

\[
                         110,
 \qquad 011,
 \qquad 101.
 \tag{6.6}
\]

They are pairwise disjoint, even when two separation rectangles occur at
the same rank.  Their three half-\(\ell^1\) norms therefore add, giving
\(2+2+2=6\). \(\square\)

Thus adding a third commuting direction cannot absorb the square defect.
The only zero-divergence standard six-switch contour remains the braid
hexagon, which Theorem 4.2 excludes by owner flow.

## 7. Exact boundary

The elementary permutahedron search is closed:

* commuting squares have protected divergence cost exactly two and also
  fail the rank-\(m\) union-injectivity audit;
* braid hexagons have zero nested divergence but fail the forced-successor
  owner audit on one top triangle;
* commuting-cube hexagons have protected divergence cost exactly six; and
* these are the only two-dimensional permutahedron faces.

The smallest surviving signed atom is the four-switch rectangle (5.3).
Its owner fibres are locally compatible, so a universal positive
divergence theorem is false.  What remains is the following exact lemma.

> **Non-face four-switch flow-completion lemma — open.**  Complete a
> owner-disjoint family of atoms (5.3) into a Boolean de Bruijn
> circulation so that all but \(o(W/H)\) selected \(A\)-transitions lie
> in those atoms, while retaining lower-prefix coverage and arranging
> \(o(W/m)\) components.

Such a completion would cancel its nested \(A\)-switch divergences exactly
and would use no additive seam.  Conversely, repeating square or braid
faces, or commuting-cube hexagons, cannot provide it.
