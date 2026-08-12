# The full `D_4/H_4` target polytope, reversal, and the root-support obstruction

Date: 2026-07-26

Method: pure mathematics.  Every finite assertion below is obtained from
the displayed fourteen-row factor and is proved by the indicated orbit
calculation.

## 0. Result

Let

\[
 H=\langle\alpha,\beta,\gamma\rangle,
 \qquad
 \alpha=(2\ 3),\quad\beta=(4\ 5),\quad\gamma=(6\ 7),
 \tag{0.1}
\]

and let `G` be the new exact `D_4`-port factor from
`MATH_THEOREM_D4_PAIR23_PORT_FACTOR_20260726.md`.  Let `G^dagger` be its
literal reflected path reversal, defined in Section 1.  The full library

\[
                 {\cal L}=\{hG,hG^\dagger:h\in H\}                 \tag{0.2}
\]

has sixteen distinct first-insertion histograms.  Write `n_i` for the
number of roots whose first inserted coordinate is `i`, and put

\[
 s_1=n_2+n_3,\qquad s_2=n_4+n_5,\qquad s_3=n_6+n_7.                \tag{0.3}
\]

The exact histogram polytope is four dimensional.  Its points are
precisely

\[
\boxed{
\begin{gathered}
 n_1=0,\qquad n_8=5,\qquad 0\le\lambda\le1,\\
 (s_1,s_2,s_3)=(3+2\lambda,\ 4-3\lambda,\ 2+\lambda),\\
 \lambda\le n_2\le3+\lambda,\qquad
 0\le n_4\le4-3\lambda,\qquad
 \lambda\le n_6\le2.
\end{gathered}}                                                   \tag{0.4}
\]

All sixteen library histograms are vertices.  Eight form the forward
`H`-orbit at `lambda=1`, and eight form the reversed `H`-orbit at
`lambda=0`; path reversal exchanges these two orbits.

There is an exact rootwise obstruction to the proposed uniform four-state
packet:

\[
 \boxed{b_1^{L}(1234)=b_1^{L}(1235)=8\quad\hbox{for every }L\in{\cal L}.}
                                                                    \tag{0.5}
\]

The other twelve roots have four-element support across the full library,
but (0.5) shows that the library cannot offer four states at one boundary
for **every** `D_4` occurrence.  The orbit

\[
                              \{1234,1235\}                         \tag{0.6}
\]

is invariant under both `H` and reflected reversal, so no allowed context
relabeling removes the obstruction.  Moreover, even on the twelve flexible
roots the choices are factor-coupled: one state of (0.2) chooses all
fourteen rows and all collar profiles simultaneously.

More precisely, the whole-root assignment polytope has the sixteen
one-hot maps displayed in (3.5) as its vertices and has affine dimension
exactly thirteen.  It is therefore very far from the product of its
twelve four-point flexible row projections.

The exact packet lattice and the full carrier/collar action are given in
Sections 4 and 6.  In particular, the four-state fixed-port seed at
`P=1256` is genuine, but it does not extend to a root-uniform eight-joint-
cell packet.

## 1. The valid reflected reversal

Let

\[
                         R(i)=9-i\qquad(1\le i\le8),                \tag{1.1}
\]

and, for a four-set `P`, put

\[
                         \mu(P)=R([8]\setminus P).                 \tag{1.2}
\]

The map `mu` preserves `D_4`.  If the row of `G` rooted at `Q` is

\[
 X_0(Q),X_1(Q),X_2(Q),X_3(Q),X_4(Q)=Q^c,                          \tag{1.3}
\]

define the reversed row at `P`, where `Q=mu(P)`, by

\[
                     X_t^\dagger(P)=R X_{4-t}(Q).                  \tag{1.4}
\]

Indeed, `mu` is an involution, so

\[
 X_0^\dagger(P)=R(Q^c)=P,
 \qquad
 X_4^\dagger(P)=RQ=P^c.                                           \tag{1.5}
\]

The seventy `X`-states are merely permuted by (1.4).  Consecutive unions
are sent by

\[
 X_t^\dagger(P)\cup X_{t+1}^\dagger(P)
   =R\bigl(X_{4-t}(Q)\cup X_{3-t}(Q)\bigr),                       \tag{1.6}
\]

so the fifty-six `Y`-states are also merely permuted.  Thus `G^dagger` is
a valid exact `D_4`-port factor.

Write the coordinate word of the row at `Q` as

\[
 q(Q)=(a_1,a_2,a_3,a_4,b_1,b_2,b_3,b_4,9).                       \tag{1.7}
\]

Equation (1.4) gives, exactly,

\[
 q^\dagger(P)=
 (Rb_4,Rb_3,Rb_2,Rb_1,Ra_4,Ra_3,Ra_2,Ra_1,9),
 \qquad Q=\mu(P).                                                  \tag{1.8}
\]

In particular

\[
                         b_1^{G^\dagger}(P)=R a_4^G(\mu(P)).       \tag{1.9}
\]

For `h in H`, the reanchored conjugate at the fixed physical root `P` is

\[
 q_{h,+}(P)=h q(h^{-1}P),\qquad
 q_{h,-}(P)=h q^\dagger(h^{-1}P).                                 \tag{1.10}
\]

Every element of `H` is an involution, although (1.10) is written in the
form valid for an arbitrary group.

This reflected reversal must not be replaced by the tempting statewise
complement-reversal

\[
                         \widehat X_t=[8]\setminus X_{4-t}.       \tag{1.11}
\]

That operation keeps the root equal to `P`, but it is not an exact
factor.  In the rows rooted at `1234` and `1235`, respectively,

\[
 1238\cap1368=138=1358\cap1378.                                  \tag{1.12}
\]

Under (1.11) both edges would therefore have the same adjacent union
`[8]\setminus138=24567`, so the `Y`-ledger repeats.  Bare phase reversal
without `R` is exact but is rooted on `D_4^c`, not on the fixed `D_4`
shore.  Consequently (1.4), followed by `H`, is the relevant full
same-port reversal library.

## 2. The two marked ledgers

The first-insertion ledger of `G` is

\[
\begin{array}{c|cccccccccccccc}
P&1234&1235&1236&1237&1245&1246&1247&1256&1257&1345&1346&1347&1356&1357\\ \hline
b_1^G(P)&8&8&7&8&3&3&3&7&3&6&8&8&2&4.
\end{array}                                                        \tag{2.1}
\]

The fourth deletion coordinates read from the same paths are

\[
\begin{array}{c|cccccccccccccc}
P&1234&1235&1236&1237&1245&1246&1247&1256&1257&1345&1346&1347&1356&1357\\ \hline
a_4^G(P)&1&1&6&1&5&2&2&6&5&5&1&1&6&5.
\end{array}                                                        \tag{2.2}
\]

The mirror map has cycles

\[
\begin{gathered}
1234, 1235, (1236\ 1245), (1237\ 1345), 1246,
(1247\ 1346),\quad1256, (1257\ 1356), 1347, 1357.
\end{gathered}                                                     \tag{2.3}
\]

Substitution in (1.9) therefore gives

\[
\begin{array}{c|cccccccccccccc}
P&1234&1235&1236&1237&1245&1246&1247&1256&1257&1345&1346&1347&1356&1357\\ \hline
b_1^{G^\dagger}(P)&8&8&4&4&3&7&8&3&3&8&7&8&4&4.
\end{array}                                                        \tag{2.4}
\]

Consequently the two factor histograms are

\[
\begin{aligned}
 v^+&=e_2+4e_3+e_4+e_6+2e_7+5e_8,\\
 v^-&=3e_3+4e_4+2e_7+5e_8.                                      \tag{2.5}
\end{aligned}
\]

These have pair totals

\[
 (s_1,s_2,s_3)(v^+)=(5,1,3),\qquad
 (s_1,s_2,s_3)(v^-)=(3,4,2).                                     \tag{2.6}
\]

## 3. Every rootwise menu

In the following table `i^k` means that target `i` occurs for exactly
`k` of the eight conjugates in the indicated orientation.

\[
\begin{array}{c|l|l|l}
P&\{b_1^{hG}(P):h\in H\}&
  \{b_1^{hG^\dagger}(P):h\in H\}&
  \text{support in the full library}\\ \hline
1234&8^8&8^8&\{8\}\\
1235&8^8&8^8&\{8\}\\
1236&7^4,8^4&4^4,5^4&\{4,5,7,8\}\\
1237&6^4,8^4&4^4,5^4&\{4,5,6,8\}\\
1245&3^4,6^2,7^2&3^4,8^4&\{3,6,7,8\}\\
1246&3^4,5,7,8^2&3^2,5^2,7^2,8^2&\{3,5,7,8\}\\
1247&3^4,5,6,8^2&3^2,5^2,6^2,8^2&\{3,5,6,8\}\\
1256&3^4,4,7,8^2&3^2,4^2,7^2,8^2&\{3,4,7,8\}\\
1257&3^4,4,6,8^2&3^2,4^2,6^2,8^2&\{3,4,6,8\}\\
1345&2^4,6^2,7^2&2^4,8^4&\{2,6,7,8\}\\
1346&2^4,5,7,8^2&2^2,5^2,7^2,8^2&\{2,5,7,8\}\\
1347&2^4,5,6,8^2&2^2,5^2,6^2,8^2&\{2,5,6,8\}\\
1356&2^4,4,7,8^2&2^2,4^2,7^2,8^2&\{2,4,7,8\}\\
1357&2^4,4,6,8^2&2^2,4^2,6^2,8^2&\{2,4,6,8\}.
\end{array}                                                       \tag{3.1}
\]

Here entries without an exponent have multiplicity one.  To prove the
table without fourteen independent calculations, note that `H` has four
port orbits

\[
\begin{aligned}
 A&=\{1234,1235\},&B&=\{1236,1237\},\\
 C&=\{1245,1345\},&D&=\{1246,1247,1256,1257,
                         1346,1347,1356,1357\}.                   \tag{3.2}
\end{aligned}
\]

On the regular orbit `D`, it is enough to calculate at `1256`.  Equations
(2.1) and (2.4) give respectively

\[
 3^4,4,7,8^2
 \qquad\hbox{and}\qquad
 3^2,4^2,7^2,8^2.                                                 \tag{3.3}
\]

Applying the unique element carrying `1256` to the desired root gives all
eight `D`-rows of (3.1).  The two-element orbits are read directly from
(2.1)--(2.4), with their stabilizers supplying the displayed
multiplicities.  This proves (3.1).

The last column has the sharper closed form

\[
 \operatorname {supp}_{\mathcal L}(P)=
 \begin{cases}
  \{8\},&P\in\{1234,1235\},\\
  [8]\setminus P,&P\in D_4\setminus\{1234,1235\}.
 \end{cases}                                                     \tag{3.3a}
\]

The second line is the largest support any first insertion at root `P`
could have, since it must lie outside `P`.  Thus the twelve flexible rows
are marginally maximally flexible; the failure is concentrated exactly on
the two-root orbit `A`.

In particular, `A` remains invariant when reversal is adjoined: `mu`
fixes each member of `A`.  This proves the obstruction (0.5) with the same
quantifiers as the proposed root-uniform packet.

### 3.1 The whole-root assignment polytope

Fix the root order

\[
\begin{split}
 &(1234,1235,1236,1237,1245,1246,1247,1256,1257,\\
 &\hspace{42mm}1345,1346,1347,1356,1357).                       \tag{3.4}
\end{split}
\]

For a factor `L`, let `z(L)` be the element of
`R^(D_4 times [8])` whose `P`-row is the one-hot vector
`e_(b_1^L(P))`.  The exact sixteen target maps, written as their fourteen
target labels in the order (3.4), are

\[
\begin{array}{c|l|l}
h&z(hG)&z(hG^\dagger)\\ \hline
1&88783337368824&88443783387844\\
\gamma&88863333678842&88443863388644\\
\beta&88783733362588&88553337885578\\
\beta\gamma&88863363375288&88553338685586\\
\alpha&88786883422272&88448784427822\\
\alpha\gamma&88867884322226&88448864428622\\
\alpha\beta&88786358827222&88558557822278\\
\alpha\beta\gamma&88867538822622&88558558622286.
\end{array}                                                       \tag{3.5}
\]

Spaces have only been suppressed to keep the table narrow: every string
in (3.5) has fourteen one-digit entries.  For example, its first forward
row is exactly (2.1), and its first reversed row is exactly (2.4).

Define

\[
 {\cal A}=\operatorname {conv}\{z(hG),z(hG^\dagger):h\in H\}.     \tag{3.6}
\]

The histogram map `z -> sum_P z_P` sends the sixteen points in (3.5) to
the sixteen distinct vertices of the histogram polytope proved in Section
4.  Consequently every point in (3.5) is itself a vertex of (3.6).

These are also the only deterministic row-assignment points in
\(\mathcal A\).  Indeed, if a convex combination of the sixteen one-hot tensors
is itself one-hot in every row, then every tensor receiving positive
weight must agree with it in every row.  The sixteen target maps in (3.5)
are distinct, so the combination is a single vertex.  Thus convexification
does not hide any legal rowwise splice of different conjugates.

### Proposition 3.2 (exact affine dimension)

\[
                         \boxed{\dim_{\rm aff}{\cal A}=13.}       \tag{3.7}
\]

#### Proof

We give a character calculation which is short enough to audit by hand.
Identify the regular port orbit `D` in (3.2) with `H` by `k -> k(1256)`,
using group order

\[
              (1,\gamma,\beta,\beta\gamma,
                         \alpha,\alpha\gamma,
                         \alpha\beta,\alpha\beta\gamma).         \tag{3.8}
\]

The base targets on this orbit are

\[
 t^+=(7,3,3,3,2,4,8,8),\qquad
 t^-=(3,3,7,8,4,4,7,8).                                         \tag{3.9}
\]

Let a character of `H` be indexed by `(A,B,C) in {0,1}^3`, and abbreviate

\[
                 a=(-1)^A,\qquad b=(-1)^B,\qquad c=(-1)^C.        \tag{3.10}
\]

Decompose the target-coordinate representation into the invariant pair
classes and the three antisymmetric vectors

\[
 e_2-e_3,\qquad e_4-e_5,\qquad e_6-e_7.                           \tag{3.11}
\]

For the total character `(A,B,C)`, Fourier summation of the eight entries
in (3.9) gives the following selected components of the forward and
reversed projections:

\[
\begin{array}{c|cc}
\text{component}&Z^+_{A,B,C}&Z^-_{A,B,C}\\ \hline
E_3&1&b(1+a)\\
e_2-e_3&-(a+b+c+bc)&-(1+c)\\
e_4-e_5&ac&a(1+c)\\
e_6-e_7&-1&-b(1+a).
\end{array}                                                       \tag{3.12}
\]

For clarity about the only twist in (3.12): the diagonal action on roots
and labels shifts the domain character of `e_(2j)-e_(2j+1)` by the
character of the corresponding transposition.  Direct summation gives
the four entries shown.

If `a=c=-1`, every invariant pair-class component and every
antisymmetric component of `Z^-` vanishes on `D`.  It vanishes on all
other root orbits as well: on `A` the reversed assignment is constant, on
`B` it is invariant under `alpha`, and on `C` it is invariant under
`gamma`.  Hence

\[
                         Z^-_{A,B,C}=0
       \quad\text{when }(A,C)=(1,1).                              \tag{3.13}
\]

On the other hand `Z^+` is nonzero there, since its last component in
(3.12) is `-1`.  Thus each of these two characters contributes dimension
one.

For each of the remaining six characters, the two projections are
linearly independent already on `D`:

* if `a=-1,c=1`, the reversed last component is zero, its second component
  is `-2`, and the forward last component is `-1`;
* if `a=1,c=-1`, the reversed third component is zero while its last
  component is nonzero, whereas the forward third component is `-1`;
* if `a=c=1,b=-1`, the third components rule out the ratio forced by the
  first and last rows of (3.12);
* if `a=b=c=1`, those rows would force ratio two, while the second row has
  values `-4,-2`.

The eight character spaces are a direct sum.  Therefore the linear span
of the sixteen assignment tensors has dimension

\[
                         6\cdot2+2\cdot1=14.                       \tag{3.14}
\]

For any fixed root, summing its eight target coordinates is a linear
functional taking value one on every assignment tensor.  Hence the affine
dimension is one less than their linear-span dimension, proving (3.7).
\(\square\)

It follows in particular that

\[
 {\cal A}\subsetneq
 \prod_{P\in{\cal D}_4}
      \operatorname {conv}\{e_i:i\in\operatorname {supp}_{\cal L}(P)\}.
                                                                    \tag{3.15}
\]

Even after deleting the two forced rows, the right side has affine
dimension `12 times 3=36`, whereas the left side has dimension at most
thirteen.  Thus the rootwise four-label menus do not tensorize.

## 4. Exact convex hull and integer packet lattice

The forward orbit consists of the eight points

\[
\begin{gathered}
 n_1=0,quad n_8=5,\\
 (n_2,n_3)\in\{(1,4),(4,1)\},\\
 (n_4,n_5)\in\{(1,0),(0,1)\},\\
 (n_6,n_7)\in\{(1,2),(2,1)\}.                                  \tag{4.1}
\end{gathered}
\]

The reversed orbit consists of

\[
\begin{gathered}
 n_1=0,quad n_8=5,\\
 (n_2,n_3)\in\{(0,3),(3,0)\},\\
 (n_4,n_5)\in\{(4,0),(0,4)\},\\
 (n_6,n_7)\in\{(0,2),(2,0)\}.                                  \tag{4.2}
\end{gathered}
\]

Thus each orbit hull is a product of three intervals.  In a convex
combination of the two hulls, let `lambda` be the total forward weight.
The pair sums determine `lambda` uniquely, and the cross-section is

\[
 \lambda\operatorname {conv}(Hv^+)
 +(1-\lambda)\operatorname {conv}(Hv^-).                          \tag{4.3}
\]

Taking the Minkowski sum of the three pairs of intervals in
(4.1)--(4.2) gives exactly (0.4).  Conversely every point satisfying
(0.4) lies in (4.3), so no inequality is missing.

The pair-sum functional `s_3` exposes the two endpoint hulls.  Within
either endpoint hull, independent signs of the three coordinate
imbalances expose every corner.  Hence all sixteen orbit points, and no
other points, are vertices.  The affine equations may equivalently be
written

\[
 n_1=0,quad n_8=5,quad s_1+s_2+s_3=9,quad s_1-2s_3=-1.          \tag{4.4}
\]

Let

\[
 u_1=e_2-e_3,qquad u_2=e_4-e_5,qquad u_3=e_6-e_7                 \tag{4.5}
\]

and choose the orientations in (2.5) as bases.  The difference between
the reversed and forward bases is

\[
 w=-e_2-e_3+3e_4-e_6.                                            \tag{4.6}
\]

Differences inside the forward orbit generate `3u_1,u_2,u_3`; the
reversed orbit adds only `3u_1,4u_2,2u_3`.  Therefore the exact affine
lattice generated by the sixteen histograms is

\[
 \boxed{v^++\Lambda,\qquad
        \Lambda=\mathbb Zw+3\math Zu_1+\math Zu_2+\math Zu_3.}    \tag{4.7}
\]

Equivalently it consists of the integral solutions of (4.4) satisfying

\[
                         n_2-n_3\equiv3\pmod 6.                   \tag{4.8}
\]

For completeness, this equivalence is constructive.  Once `s_3` is
fixed, the coefficient of `w` is fixed by the change in `s_3`; (4.8)
then makes the remaining pair-1 displacement a multiple of `3u_1`, and
the two other within-pair displacements are arbitrary multiples of
`u_2,u_3`.

There is an even sharper integral statement for a literal packet of `N`
library factors.  If exactly `t` of them use forward orientation, then

\[
\boxed{
 S_1=3N+2t,\qquad S_2=4N-3t,\qquad S_3=2N+t,qquad N_8=5N.}        \tag{4.9}
\]

If `D_i` denotes the coordinate imbalance inside pair `i`, then the exact
attainable sets are

\[
\begin{aligned}
 D_1&\in\Bigl\{3\sum_{j=1}^N\epsilon_j:\epsilon_j\in\{-1,1\}\Bigr\},\\
 D_2&\in\Bigl\{\sum_{j=1}^t\epsilon_j
                   +4\sum_{j=1}^{N-t}\eta_j:
                    \epsilon_j,\eta_j\in\{-1,1\}\Bigr\},\\
 D_3&\in\Bigl\{\sum_{j=1}^t\epsilon_j
                   +2\sum_{j=1}^{N-t}\eta_j:
                    \epsilon_j,\eta_j\in\{-1,1\}\Bigr\}.
                                                                    \tag{4.10}
\end{aligned}
\]

The three sign families can be chosen independently, because
`alpha,beta,gamma` are independent.  In particular

\[
 D_1\equiv3N\pmod6,qquad D_2\equiv D_3\equiv t\pmod2.             \tag{4.11}
\]

Equations (4.9)--(4.11) are the exact aggregate coupling left after
arbitrary integer coefficients and allowed context relabelings.  They are
strictly stronger than membership of the real convex hull.

## 5. The signed transition polytope

There are two natural transition conventions, and they should not be
confused.

First, relative to one fixed canonical MSW factor, whose histogram is

\[
                         v^0=5e_2+2e_4+2e_6+5e_8,                 \tag{5.1}
\]

the transition polytope is simply the translate

\[
                              {\cal P}-v^0,                       \tag{5.2}
\]

where `P` is (0.4).

For an equivariant Haar replacement one instead compares `hG^epsilon`
with the equally conjugated canonical factor `hF^epsilon`.  Reflected
reversal preserves the canonical MSW factor, and the two base transition
vectors, in coordinate order `2,...,7`, are

\[
 d^+=(-4,4,-1,0,-1,2),\qquad
 d^-=(-5,3,2,0,-2,2).                                             \tag{5.3}
\]

Let `r_i=d_{2i}+d_{2i+1}` for `i=1,2,3`.  The exact equivariant
transition polytope is

\[
\boxed{
\begin{gathered}
 0\le\lambda\le1,qquad
 (r_1,r_2,r_3)=(-2+2\lambda,\ 2-3\lambda,\ \lambda),\\
 -5+\lambda\le d_2\le3+\lambda,\\
 -\lambda\le d_4\le2-2\lambda,\\
 -2+\lambda\le d_6\le2.
\end{gathered}}                                                    \tag{5.4}
\]

It again has sixteen vertices in two `H`-orbits.  Its affine equations
are

\[
                  r_1+r_2+r_3=0,qquad r_1-2r_3=-2.                \tag{5.5}
\]

Its affine lattice is

\[
 \boxed{d^++\Lambda_{\rm tr},\qquad
 \Lambda_{\rm tr}=\mathbb Zw+8\math Zu_1+\math Zu_2+\math Zu_3,} \tag{5.6}
\]

or, equivalently, the integral solutions of (5.5) with

\[
                         d_2-d_3\equiv8\pmod {16}.                 \tag{5.7}
\]

Indeed the forward within-pair generators are
`8u_1,u_2,3u_3`, the reversed generators are
`8u_1,2u_2,4u_3`, and `gcd(3,4)=1`.  This proves (5.6) and (5.7).

## 6. The complete carrier/collar tensor

The marked histogram is only one projection.  For `1<=ell<=8` and
`j in Z_9`, put

\[
 I_{\ell,j}(q)=\{q_j,q_{j+1},\ldots,q_{j+\ell-1}\},                \tag{6.1}
\]

with cyclic indices, and define the complete local profile

\[
 U^{h,\epsilon}_{\ell,j}
   =\sum_{P\in{\cal D}_4}e_{I_{\ell,j}(q_{h,\epsilon}(P))}.        \tag{6.2}
\]

Changing variables `Q=h^{-1}P` in (6.2) gives

\[
 U^{h,+}_{\ell,j}=h_*U^{1,+}_{\ell,j}.                            \tag{6.3}
\]

The index permutation in (1.8) is `k -> 7-k mod 9`.  Hence

\[
\boxed{
 U^{h,-}_{\ell,j}=h_*R_*U^{1,+}_{\ell,\,8-j-\ell}.}               \tag{6.4}
\]

The row-resolved statement, needed when exterior carriers depend on the
root, is

\[
\begin{aligned}
 U^{h,+}_{\ell,j;P}
   &=h_*U^{1,+}_{\ell,j;h^{-1}P},\\
 U^{h,-}_{\ell,j;P}
   &=h_*R_*U^{1,+}_{\ell,\,8-j-\ell;\,\mu(h^{-1}P)}.
                                                                    \tag{6.4a}
\end{aligned}
\]

All start indices in (6.4)--(6.4a) are modulo nine.  Thus reversal changes
the collar offset as well as the marked coordinate.

Thus the **actual** local library is the sixteen-point tensor orbit

\[
 {\cal C}=\operatorname {conv}
   \left\{(U^{h,\epsilon}_{\ell,j})_{\ell,j}:
                        h\in H,\ \epsilon\in\{+,-\}\right\}.    \tag{6.5}
\]

The marked polytope (0.4) is only the projection `ell=1,j=4` of
(6.5).  A factor choice selects one whole vertex of (6.5); it cannot
select one vertex at `b_1` and unrelated vertices at collar starts.
Relative to a fixed canonical factor the complete transition tensor is

\[
 \Delta^{h,\epsilon}_{\ell,j}
       =U^{h,\epsilon}_{\ell,j}-U^{\rm MSW}_{\ell,j};              \tag{6.5a}
\]

for an equivariant Haar replacement the second term is conjugated and
reversed by the same `(h,epsilon)`.  Thus (6.5), translated in either of
these two precise ways, is also the exact full-collar transition
polytope.

There is a compact exact collision census for this tensor.  Put

\[
 \widehat m_{\ell,j}
  =\max_{h,\epsilon,S}
       |\{P:I_{\ell,j}(q_{h,\epsilon}(P))=S\}|.          \tag{6.5b}
\]

For the forward orbit the corresponding numbers are the audited table in
`MATH_THEOREM_D4_H4_ORBIT_AND_CARRIER_CAPACITY_20260726.md`.  Equation
(6.4) proves that the reversed number at `(ell,j)` is the forward number
at `(ell,8-j-ell)`.  Hence, entrywise taking the larger of the two, one
gets

\[
\begin{array}{c|rrrrrrrrr}
\ell\backslash j&0&1&2&3&4&5&6&7&8\\ \hline
1&5&4&5&5&5&5&4&5&14\\
2&2&2&2&5&2&2&2&5&5\\
3&1&1&2&2&1&1&2&2&2\\
4&1&1&1&1&1&1&1&1&1\\
5&1&1&1&1&1&1&1&1&1\\
6&2&2&2&1&1&2&2&1&1\\
7&5&5&2&2&2&5&2&2&2\\
8&14&5&4&5&5&5&5&4&5.
\end{array}                                                     \tag{6.5c}
\]

Thus every nonconstant local carrier has collision multiplicity at most
five in every library state.  The two constant profiles are `(1,8)`, with
target `{9}`, and `(8,0)`, with target `[8]`.  Four further rowwise fixed
ledgers are `(4,0)`, `(4,4)`, `(5,4)`, and `(5,8)`, giving respectively
`P`, `P^c`, `P^c union {9}`, and `P union {9}`.  This collision bound is
not a balancing theorem: distinct rows may have distinct exterior
carriers, and one common `(h,epsilon)` still controls every profile in a
factor packet.

There are four exact all-factor ownership identities.  Since every row
word is a permutation of `[9]`,

\[
\begin{aligned}
 \sum_{j\in\mathbb Z_9}U^{h,\epsilon}_{1,j}
   &=14\sum_{i=1}^9e_{\{i\}},\\
 \sum_{j\in\mathbb Z_9}U^{h,\epsilon}_{8,j}
   &=14\sum_{i=1}^9e_{[9]\setminus\{i\}}.                         \tag{6.6}
\end{aligned}
\]

For length four, starts `j=0,...,4` are the five `X`-states in a row,
while starts `j=5,...,8` are the complements in `[9]` of its four
`Y`-states.  Exact `X/Y` ownership therefore gives

\[
\begin{aligned}
 \sum_jU^{h,\epsilon}_{4,j}&=\sum_{S\in\binom{[9]}4}e_S,\\
 \sum_jU^{h,\epsilon}_{5,j}&=\sum_{S\in\binom{[9]}5}e_S.          \tag{6.7}
\end{aligned}
\]

The second identity is also the complement of the first.  Consequently
every marked motion is repaid across the complete start ledger at lengths
`1,4,5,8`.  This is a local all-start identity; after physical
push-forward it can be summed before applying the carrier only when the
carrier and injection are common.  Start-resolved motion can still occur
at those lengths away from the six fixed profiles following (6.5c).  At
lengths `2,3,6,7`, even the aggregate all-start profile need not cancel.

Finally, in an ambient context with affine local labeling `iota` and
fixed exterior carrier `O`, the physical profile is exactly the pushforward

\[
              e_S\longmapsto e_{O\cup\iota(S)}.                   \tag{6.8}
\]

For several carrier classes, (6.8) is applied to each class, but the same
pair `(h,epsilon)` must be used in every one of them belonging to the same
factor packet.  This is the full carrier coupling.  It rules out treating
the four marked labels in a flexible row as four occurrencewise free bins.

## 7. Exact decision boundary

The finite calculation proves all of the following.

1. The fixed port `1256` and, more generally, every root outside `A`, has
   four marked labels across the complete conjugacy/reversal library.
2. The roots `1234,1235` have the singleton menu `{8}`.  Hence a complete
   root-scale packet cannot supply four first-boundary states to every
   loaded occurrence if its charged family contains all fourteen port
   rows.  Replication does not dilute the obstruction: exactly `2N` of
   the `14N` rows in `N` complete packets are frozen.  If *charged* is
   reserved only for rows whose target is movable, then the exact positive
   statement is that all twelve charged rows have four marginal labels;
   one must separately absorb the frozen `1/7` mass and respect the joint
   tensor (6.5).
3. Every factor state has exactly five `b_1=8` rows.  This is also the
   universal endpoint-pair ownership law for an exact anchored `D_4`
   factor: applying the `X/Y` pair margin to the universal port pair
   `(1,8)` gives five rows with insertion of `8` no later than deletion
   of `1`; the `X` pair count is fifteen, forcing all five gaps to equal
   three, hence insertion time one and deletion time four.
4. Equations (4.9)--(4.10) and the tensor orbit (6.5), not merely the
   marked support table, are the exact constraints on integer packets.
   The congruences (4.11) are necessary consequences only; for fixed `N`
   they do not replace the bounded signed-sum sets in (4.10).

If a genuinely independent binary opposite-boundary choice acts in a
disjoint coordinate block, the twelve flexible roots have eight formal
joint cells, whereas `1234,1235` have only two.  Without such an
independent product certificate the exact joint support is instead the
image of the same sixteen vertices under the two-boundary carrier map;
four marginal labels alone do not prove eight physical cells.

In particular, the reversal sign already present in this library cannot
silently be counted again as an independent binary coordinate.  Even if a
second boundary perfectly records the sign `epsilon`, the exact numbers
of phase-labelled marked states

\[
 |\{(\epsilon,b_1^{hG^\epsilon}(P)):h\in H,\epsilon\in\{+,-\}\}|
                                                                    \tag{7.1}
\]

in the root order (3.4) are

\[
                 (2,2,4,4,5,8,8,8,8,5,8,8,8,8).       \tag{7.2}
\]

This is just the sum of the forward and reversed support sizes in (3.1),
because the phase label distinguishes the two halves.  Thus the
reversal-as-the-opposite-bit interpretation gives eight cells only on the
regular eight-root orbit.  Any physical collar can only identify entries
of (7.1), not create additional ones.

Thus the new factor supplies a genuine four-state seed on twelve ports,
but the requested all-root four-state primitive is absent from its full
`H`/reversal conjugacy library.  To obtain eight joint cells uniformly one
must either add a factor whose allowed conjugacy moves the invariant port
orbit `A`, or prove that the charged root-scale occurrence family avoids
`A` and then solve the still nontrivial common-tensor balancing problem in
(6.5).  No coefficient-one conclusion follows from the finite seed alone.
