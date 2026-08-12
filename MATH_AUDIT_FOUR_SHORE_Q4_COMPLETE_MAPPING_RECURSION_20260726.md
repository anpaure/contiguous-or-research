# Four-shore \(Q_4\) complete mappings: exact recursion and entropy gate

Date: 2026-07-26

Method: direct hand verification and exact permutation algebra.  No
computation, search, solver, or web input is used.

## 0. Verdict

Let

\[
 A=(1\ 3),\qquad B=(2\ 4),\qquad S=AB=(1\ 3)(2\ 4). \tag{0.1}
\]

Starting with the standard \(Q_4\) direction field
\(1234\,1234\), all four same-vertex fields

\[
                         \delta_g=g\delta_0,
 \qquad g\in\{1,A,B,S\},                             \tag{0.2}
\]

are exact isometric \(C_8\)-factors.  Their half-orders are

\[
\begin{array}{c|c}
g&\text{half-order}\\ \hline
1&1234\\
A&3214\\
B&1432\\
S&3412.
\end{array}                                           \tag{0.3}
\]

The two bits commute at the direction-label level, and the opposite-shore
map \(S\) is fixed-point-free.

There is a positive recursive theorem.  Pair shore \(g\) with shore
\(Sg\) in the affine parity complete mapping.  All four row maps and all
four column maps are exact.  Their physical lifts form a new four-shore
system on \(Q_8\), and this construction iterates.  At every stage:

* the opposite shore moves every physical direction;
* every component is an isometric maximum cube cycle;
* every row and column map is bijective;
* the universal predecessor identity needed at odd states is preserved.

The straightforward recursion does **not** make completed-support entropy
grow at rate one.  It applies the deterministic substitution

\[
                         i\longmapsto b_i,a_i          \tag{0.4}
\]

to the same four orders.  Thus the number of order types remains four at
every scale.  The aligned trace entropy bound is therefore

\[
 \#\operatorname {codes}\le4r\,2^{2(r-d)},          \tag{0.5}
\]

and almost all starts collide once
\(d-\tfrac12\log_2r\to\infty\).

The fixed-point-free opposite shore does remove the separate partner-overlap
kernel: in the recursive orders, \(S\) sends every position to the position
halfway around the half-order, so \(J\cap S(J)=\varnothing\) for every
interval \(|J|<r/2\).  What is missing is order entropy, not displacement.

To add a shore bit contextwise, one must mix two perfect matchings in every
row and simultaneously mix their opposite partners in every column.  Such
a mixture is bijective exactly when its selector is constant on every
alternating component of both matching overlays.  At the base \(Q_4\)
level this system does have nonconstant linear solutions, computed in
Section 5.  They add one exact order bit.  Iterating one bit per dimension
doubling gives only \(O(\log r)\) bits, not rate one.  The first interface
is a high-dimensional simultaneous component quotient within one scale.

## 1. The four factors explicitly

Use the vertices

\[
\begin{array}{c|cccccccc}
j&0&1&2&3&4&5&6&7\\ \hline
a_j&0000&1000&1100&1110&1111&0111&0011&0001\\
b_j&0101&1101&1001&1011&1010&0010&0110&0100.
\end{array}                                           \tag{1.1}
\]

The identity shore is

\[
 (a_0,a_1,a_2,a_3,a_4,a_5,a_6,a_7)
 \mathbin{\dot\cup}
 (b_0,b_1,b_2,b_3,b_4,b_5,b_6,b_7),                  \tag{1.2}
\]

with word \(1234\,1234\).

The \(B\)-shore is the corrected antipodal braid

\[
\begin{aligned}
 &(a_0,a_1,b_2,b_3,a_4,a_5,b_6,b_7),\\
 &(b_0,b_1,a_2,a_3,b_4,b_5,a_6,a_7),                 \tag{1.3}
\end{aligned}

with word \(1432\,1432\).

The \(A\)-shore is

\[
\begin{aligned}
 &(a_0,b_5,b_6,a_3,a_4,b_1,b_2,a_7),\\
 &(b_0,a_5,a_6,b_3,b_4,a_1,a_2,b_7),                 \tag{1.4}
\end{aligned}

with word \(3214\,3214\).

Finally, the \(S\)-shore is

\[
\begin{aligned}
 &(a_0,b_5,a_6,b_3,a_4,b_1,a_2,b_7),\\
 &(b_0,a_5,b_6,a_3,b_4,a_1,b_2,a_7),                 \tag{1.5}
\end{aligned}

with word \(3412\,3412\).

Every row in (1.2)--(1.5) contains eight distinct owners, the paired rows
are disjoint, and each successive difference is the corresponding letter
of (0.3), repeated antipodally.  Hence all eight displayed cycles are
isometric and all four shores are exact factors.

At each owner \(y\), the four outgoing directions are literally

\[
 \delta_0(y),\quad A\delta_0(y),\quad
 B\delta_0(y),\quad S\delta_0(y).                    \tag{1.6}
\]

Thus the Klein multiplication is a same-vertex identity, not merely a
relation between abstract words.

## 2. Universal predecessor compatibility

For every target owner \(z\), the incoming identity-shore label at the
predecessor is independent of the shore used to locate that predecessor:

\[
 \boxed{
  \delta_0(G_g^{-1}z)=\iota(z)
  \quad(g\in\{1,A,B,S\}).}                           \tag{2.1}
\]

To see this, index \(z\) by its column \(j\) in (1.1).  Directly from
(1.2)--(1.5), the common value is

\[
\begin{array}{c|cccccccc}
j&0&1&2&3&4&5&6&7\\ \hline
\iota&4&1&2&3&4&1&2&3.
\end{array}                                           \tag{2.2}
\]

This is stronger than the two-shore predecessor identity.  It is the
reason all four lifts remain related at their odd states.

There is no one common \(\mathbb Z_8\) phase advancing on all four shores.
For instance the identity shore forces
\(c(a_j)=j+\alpha\), \(c(b_j)=j+\beta\).  At \(a_0\), the \(S\)-successor
is \(b_5\), forcing \(\beta-\alpha=4\); at \(a_1\), the \(S\)-successor
is \(b_2\), forcing \(\beta-\alpha=0\).  Thus the common-phase suspension
theorem cannot be invoked for the fixed-point-free opposite pair.

This phase failure does not affect the closed parity lift below; it does
mean that an exterior ported use would need a new phase/collar compiler.

## 3. Four simultaneous affine complete mappings

Let \(p\) be even, let \(x\in Q_r\), and assume at some recursive scale we
have four shore factors \(G_g\) satisfying

\[
 G_g(y)=y+e_{g\delta_0(y)},                           \tag{3.1}
\]

together with the universal predecessor identity (2.1).  Use the
fixed-point-free opposite involution \(S\), and put

\[
 y=Sp+x,\qquad d_p^g(x)=g\delta_0(y).                \tag{3.2}
\]

### Lemma 3.1 (four row/column systems)

For every \(g\in\{1,A,B,S\}\),

\[
 F_p^g(x)=x+e_{d_p^g(x)}                              \tag{3.3}
\]

is a row permutation, and

\[
 T_x^g(p)=p+e_{d_p^g(x)}                              \tag{3.4}
\]

is a bijection from the even to the odd context shore.

#### Proof

The affine row change gives

\[
 Sp+F_p^g(x)=G_g(y).                                 \tag{3.5}
\]

For the column map, commutativity of the Klein group and \(S^2=1\) give

\[
 S T_x^g(p)+x
 =y+e_{Sg\delta_0(y)}=G_{Sg}(y).                    \tag{3.6}
\]

Thus every row and column is conjugate to one of the four exact factors.
\(\square\)

Lift the pair \((G_g,G_{Sg})\) by toggling first \(b_{d_p^g(x)}\) and
then \(a_{d_p^g(x)}\).  Denote the physical neighbor permutation by
\(L_g\).

### Theorem 3.2 (four-shore recursive closure)

The four \(L_g\)'s are exact isometric \(C_{4r}\)-factors of \(Q_{2r}\).
At every common physical owner their directions satisfy

\[
                         \widetilde\delta_g
 =\widetilde g\,\widetilde\delta_0,                 \tag{3.7}
\]

where \(\widetilde g\) acts by \(g\) on the indices of both the \(a\)- and
\(b\)-directions.  The lifted system again satisfies a universal
predecessor identity, so the construction iterates.

#### Proof

Two physical steps induce (3.3), so a coarse doubled-permutation word is
expanded by (0.4) and remains doubled.  Hence every lifted cycle is
isometric.

At even states, (3.7) is immediate from (3.2).  At an odd state with
transformed coordinate \(y'\), shore \(g\) uses direction

\[
 a_{g\delta_0(G_{Sg}^{-1}y')}.
\]

Equation (2.1) makes the subscript independent of \(g\), proving (3.7).

For an odd target, the four predecessors are even and (2.1) directly makes
their evaluated \(L_1\)-directions equal.  For an even target \(z\), the
odd predecessor on shore \(g\) has transformed state

\[
                         G_{Sg}G_g^{-1}z.             \tag{3.8}
\]

Evaluating the base lifted direction there introduces
\(\delta_0(G_S^{-1}G_{Sg}G_g^{-1}z)\).  Apply (2.1) at
\(G_{Sg}G_g^{-1}z\) to replace \(G_S^{-1}\) by \(G_{Sg}^{-1}\); the
expression becomes \(\delta_0(G_g^{-1}z)=\iota(z)\), independent of
\(g\).  Thus universal predecessor compatibility also recurses.
\(\square\)

Since \(S\) has no fixed coordinate, \(\widetilde S\) has no fixed
physical direction.  Hence the opposite-shore displacement property holds
at every recursive scale.

## 4. Displacement is exact but entropy does not grow

In every base half-order in (0.3), the two members of each \(S\)-pair occur
two positions apart.  Under (0.4), their lifted positions remain separated
by half the new half-order.  Inductively,

\[
 S\text{ acts on half-order positions as a shift by }r/2.             \tag{4.1}
\]

Therefore, for every consecutive completed set \(J\) of size \(d<r/2\),

\[
                         J\cap S(J)=\varnothing.      \tag{4.2}
\]

The partner-overlap trace kernel is exactly zero in the protected range.

On the other hand, deterministic adjacent expansion sends each of the four
base orders to one lifted order and creates no new order choice.  Thus

\[
                         K_r=4                       \tag{4.3}
\]

at every scale.  Applying the order-entropy count to aligned depth \(d\)
gives (0.5), and hence collision excess at least

\[
                         2^{2r-1}-4r\,2^{2(r-d)}.     \tag{4.4}
\]

Thus “every direction is moved by the opposite shore” and “completed
support encodes the erased context” are independent requirements.  The
four-shore recursion proves the first and fails the second.

## 5. Why a context shore bit is a new matching theorem

Try to use the \(A\)-bit contextwise.  At a point \((p,x)\), choose

\[
                         g(p,x)\in\{1,A\}.            \tag{5.1}
\]

For fixed \(p\), the row edges are selected from the two perfect matchings
conjugate to \(G_1,G_A\).  For fixed \(x\), the column edges are selected
from the opposite matchings conjugate to \(G_S,G_B\).

### Lemma 5.1 (two-matching selector criterion)

Let \(M_0,M_1:L\to R\) be bijections.  A selector
\(q:L\to\{0,1\}\) makes

\[
                         M_q(u)=M_{q(u)}(u)            \tag{5.2}
\]

a bijection if and only if \(q\) is constant on every nontrivial alternating
component of \(M_0\cup M_1\).  Doubled common edges impose no condition.

#### Proof

Every component of the union of two bipartite perfect matchings is an even
alternating cycle or a doubled edge.  On an alternating cycle, the only
subsets containing one edge at each left and right vertex are the two
alternating perfect matchings.  Thus all left vertices in that component
must choose the same shore.  The converse is immediate. \(\square\)

Apply Lemma 5.1 in every row and every column.  A context bit
\(q(p,x)\) is legal exactly when it is simultaneously constant on

1. every alternating component of the row overlay \((G_1,G_A)\), after
   the affine translation belonging to \(p\); and
2. every alternating component of the column overlay \((G_S,G_B)\), after
   the affine translation belonging to \(x\).

Equivalently, \(q\) must be constant on every component of the equivalence
relation generated jointly by these row and column alternating cycles.

### Lemma 5.2 (one exact nonconstant context bit)

At the base \(Q_4\) level put

\[
                         u=e_1+e_3.                  \tag{5.3}
\]

The nontrivial alternating components of \((G_1,G_A)\) are the pairs
\(\{y,y+u\}\) at the phases where \(\delta_0(y)\in\{1,3\}\); the phases
with directions \(2,4\) are doubled common edges.  The pair
\((G_S,G_B)\) has the same component translation, since

\[
                         Su=u.                       \tag{5.4}
\]

Therefore every linear form \(\ell\) with \(\ell(u)=0\) gives a legal
simultaneous selector

\[
                         q(p,x)=\ell(p).              \tag{5.5}
\]

#### Proof

The row selector is constant in \(x\), so every row uses one whole shore.
For a fixed column \(x\), an alternating step changes the transformed
variable \(y=Sp+x\) by \(u\), and hence changes \(p\) by
\(S^{-1}u=u\).  Equation \(\ell(u)=0\) makes (5.5) constant on every
column alternating component.  Lemma 5.1 proves both bijectivities.
\(\square\)

Thus the four-shore square genuinely inserts one context-dependent order
bit.  If one inserts only one such bit at each recursive doubling, after
\(t\) levels the number of order types is at most

\[
                         4\cdot2^t=O(r),              \tag{5.6}
\]

so Theorem 4.1 still gives exponential collision at every
\(d-O(\log r)\to\infty\).  A rate-one compiler needs \(\Theta(d)\)
simultaneously legal component bits at the same scale, not one new bit per
scale.

### Exact remaining gate \(\mathrm{KLEIN\mbox{-}LATIN}(r,H)\)

Construct a nonconstant selector satisfying both component systems such
that its induced cycle orders have at least

\[
                         2^{H-o(H)}                  \tag{5.7}
\]

protected-interval types and the completed-support trace codes are
near-injective through depth \(H/2\).

The base quotient is nontrivial by Lemma 5.2.  The unresolved question is
whether the growing joint row/column equivalence relation has
\(\Theta(H)\) independent component labels whose induced interval sets are
an erasure code, rather than merely \(O(\log r)\) scale labels.

This simultaneous alternating-cycle quotient—not fixed-point-free
displacement, row bijectivity, column bijectivity, or physical cycle
closure—is the first unresolved interface.
