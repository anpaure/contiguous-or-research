# The double-factor recursion closes, but its trace alphabet does not grow

Date: 2026-07-26

Method: pure mathematics only.

> **Scope.**  The trace alphabet below is the augmented alphabet carrying
> the completed support `J`.  Its collision lower bounds remain valid for
> literal targets after `J` is forgotten.  Its noncollision statements do
> not imply literal target injectivity.

## 0. Outcome

There is an exact recursion for the double-factor input from
`MATH_THEOREM_DOUBLE_FACTOR_AFFINE_PARITY_COMPLETE_MAPPING_20260726.md`.
The clean invariant is slightly stronger than the outgoing-direction
identity used there: one must impose the same identity also on incoming
directions.  If the coordinate permutation is an involution, the parity
complete-mapping lift sends such a bidirectional double factor on (Q_r)
to one on (Q_{2r}).  Both new factors consist of isometric
(C_{4r})'s, and the new coordinate permutation is explicit.

This settles the cycle-structure part of the proposed recursion.  It also
gives a sharp negative answer for the trace-code part.  Under this
recursion every old cyclic direction order is merely replaced by the
adjacent-pair substitution

\[
                    i\longmapsto(b_i,a_i).                    \tag{0.1}
\]

Consequently the number of direction-order types never increases.  If
the seed has (K) types, then at aligned completed-pair depth (d) the
proportion of distinct tagged codes is at most

\[
                         \boxed{\frac{2Kr}{4^d}}.              \tag{0.2}
\]

Thus every recursion from a fixed finite seed has collision excess
((1-o(1))2^{2r-1}) as soon as
(d-\frac12\log_2r\to\infty), in particular throughout a Gaussian
window.  The recursion preserves exact ownership and the double-factor
relation, but it cannot produce near-injective augmented context codes.

## 1. Bidirectional double factors

For a neighbour permutation (G) of (Q_r), write

\[
 G(y)=y\oplus e_{\delta^+_G(y)},\qquad
 G^{-1}(y)=y\oplus e_{\delta^-_G(y)}.                \tag{1.1}
\]

Let (S\in S_r) act both on coordinates and on cube vectors.  Call
((G_0,G_1,S)) a **bidirectional double factor** if

\[
 \delta^+_1(y)=S\delta^+_0(y),\qquad
 \delta^-_1(y)=S\delta^-_0(y)                       \tag{1.2}
\]

for every (y\in Q_r).  The second equation is genuinely additional:
an outgoing same-vertex relation between two arbitrary permutations does
not imply the corresponding incoming relation.

The common-phase (Q_4) braid is bidirectional.  Indeed, at common phase
(j\), its outgoing directions are

\[
 1234\,1234\quad\hbox{and}\quad1432\,1432,
\]

and its incoming directions are the same two words shifted one phase
back.  Hence (1.2) holds with (S=(2\ 4)).

There is also a smaller seed.  On (Q_2), orient its unique square in the
two opposite directions.  The two direction words are (12,12) and
(21,21), and (1.2) holds with the fixed-point-free involution
(S=(1\ 2)).

## 2. The exact recursion

Assume henceforth that (S^2=I).  Put

\[
 E_r=\{p\in Q_r:|p|\equiv0\pmod2\}.
\]

For (p\in E_r), (x\in Q_r), and

\[
                         y=Sp\oplus x,               \tag{2.1}
\]

define two coarse neighbour permutations by their directions

\[
 d^0_p(x)=\delta^+_0(y),\qquad
 d^1_p(x)=S\delta^+_0(y)=\delta^+_1(y),              \tag{2.2}
\]

and put (F^j_p(x)=x\oplus e_{d^j_p(x)}).

For each (j\in\{0,1\}), apply the parity complete-mapping lift on
physical coordinate pairs ((a_i,b_i)), with

\[
                         x_i=a_i,\qquad p_i=a_i\oplus b_i.      \tag{2.3}
\]

Denote the resulting neighbour permutation of (Q_{2r}) by (H_j).
Finally define

\[
 \widehat S(a_i)=a_{S i},\qquad
 \widehat S(b_i)=b_{S i}.                            \tag{2.4}
\]

### Theorem 2.1 (bidirectional double-factor recursion)

If ((G_0,G_1,S)) is a bidirectional double factor and (S^2=I), then:

1. every family (F^j_p) satisfies all parity complete-mapping
   equations;
2. (H_0,H_1) are neighbour permutations of (Q_{2r});
3. their outgoing and incoming directions obey
   \[
   \delta^+_{H_1}(z)=\widehat S\delta^+_{H_0}(z),\qquad
   \delta^-_{H_1}(z)=\widehat S\delta^-_{H_0}(z);    \tag{2.5}
   \]
4. if every (G_j)-cycle is an isometric (C_{2r}), then every
   (H_j)-cycle is an isometric (C_{4r}).

Thus ((H_0,H_1,\widehat S)) is a bidirectional double factor at the
next scale.

#### Proof

First,

\[
 Sp\oplus F^0_p(x)=G_0(y),\qquad
 Sp\oplus F^1_p(x)=G_1(y),                           \tag{2.6}
\]

so every (F^j_p) is an affine vertex-conjugate of (G_j).  For the
two column maps (T^j_x(p)=p\oplus e_{d^j_p(x)}),

\[
\begin{aligned}
 S T^0_x(p)\oplus x
   &=y\oplus e_{S\delta^+_0(y)}=G_1(y),\\
 S T^1_x(p)\oplus x
   &=y\oplus e_{S^2\delta^+_0(y)}=G_0(y).
\end{aligned}                                      \tag{2.7}
\]

Both are bijections from one parity shore to the other.  This proves the
complete-mapping equations and hence the existence of (H_0,H_1).

It remains to check (2.5), because the odd shore uses inverse column
routing.  At an even state with transformed coordinate (y=Sp\oplus x),
the two outgoing physical directions are respectively

\[
                         b_{\delta^+_0(y)},\qquad
                         b_{S\delta^+_0(y)}.          \tag{2.8}
\]

At an odd state, put (z=Sp\oplus x).  The inverse (H_0)-column route
uses (G_1^{-1}z), whereas the inverse (H_1)-column route uses
(G_0^{-1}z).  Their labels are

\[
\begin{aligned}
 \delta^+_0(G_1^{-1}z)
   &=S^{-1}\delta^-_1(z)=\delta^-_0(z),\\
 \delta^+_1(G_0^{-1}z)
   &=S\delta^-_0(z),
\end{aligned}                                      \tag{2.9}
\]

where (1.2) and (S^{-1}=S) were used.  Thus the two outgoing physical
directions on the odd shore are

\[
                         a_{\delta^-_0(z)},\qquad
                         a_{S\delta^-_0(z)}.          \tag{2.10}
\]

Equations (2.8)--(2.10) prove the outgoing identity in (2.5).

The incoming calculation is the same with the two shores exchanged.  At
an odd state, its even predecessors have directions

\[
                         b_{\delta^-_0(z)},\qquad
                         b_{S\delta^-_0(z)},          \tag{2.11}
\]

and at an even state, its odd predecessors have directions

\[
                         a_{\delta^-_0(z)},\qquad
                         a_{S\delta^-_0(z)}.          \tag{2.12}
\]

This proves the incoming identity.

Finally, (H_j^2), restricted to an even context (p), is exactly
(F^j_p).  Hence a (2r)-cycle of (F^j_p) lifts to a (4r)-cycle.
Every coarse direction (i) is replaced by (b_i,a_i); consequently a
doubled-permutation word \(\pi\pi\) becomes

\[
 (b_{\pi_1},a_{\pi_1},\ldots,b_{\pi_r},a_{\pi_r})^2. \tag{2.13}
\]

This is again a doubled permutation, now of the (2r) physical
directions, and hence isometric.  \(\square\)

### Corollary 2.2 (two infinite explicit recursions)

The opposite orientations of the (Q_2) square give bidirectional double
factors on (Q_{2^t}) for every (t\ge1).  The common-phase (Q_4)
braid gives them on (Q_{2^{t+2}}) for every (t\ge0).

In the second family the involution fixes exactly half the directions at
every scale.  In the first family it is fixed-point-free at every scale.
Fixed points are therefore not needed for the recursion itself.

## 3. Exact cyclic-order propagation

Let (\mathscr O(G)) be the set of cyclic direction permutations, up to
cyclic rotation, occurring among the isometric cycles of (G), and put
(K(G)=|\mathscr O(G)|).

### Proposition 3.1 (order-library conservation)

For the recursion of Theorem 2.1,

\[
                         K(H_j)\le K(G_j).            \tag{3.1}
\]

More precisely, every cyclic order (\pi) in (G_j) is replaced by the
single order

\[
 \operatorname{pair}(\pi)
 =(b_{\pi_1},a_{\pi_1},\ldots,b_{\pi_r},a_{\pi_r}). \tag{3.2}
\]

#### Proof

Equation (2.6) shows that affine vertex conjugacy changes the starting
vertex but not the direction labels or their cyclic order.  Equation
(2.13) then gives (3.2).  \(\square\)

In particular, both finite seeds above have (K=1), and every iterate
still has (K=1).  No high-entropy schedule is created by the recursion.

## 4. The trace ceiling

Consider one parity lift from (Q_r) to (Q_{2r}).  There are

\[
                         N=2^{2r-1}                   \tag{4.1}
\]

aligned even-time starts.  A completed-pair window of coarse depth (d)
has physical trace code

\[
 \mathcal C_d(p,x)=
 (J_{p,d}(x),p|_{J_{p,d}(x)^c},x|_{J_{p,d}(x)^c}).   \tag{4.2}
\]

### Theorem 4.1 (finite-order-library ceiling)

If the coarse factor family uses at most (K) cyclic direction orders,
then

\[
 \boxed{
 |\operatorname {im}\mathcal C_d|
 \le Kr\,2^{2(r-d)},\qquad
 \frac{|\operatorname {im}\mathcal C_d|}{N}
 \le\frac{2Kr}{4^d}.}                               \tag{4.3}
\]

Consequently its collision deficit satisfies

\[
 N-|\operatorname {im}\mathcal C_d|
 \ge N\left(1-\frac{2Kr}{4^d}\right).               \tag{4.4}
\]

The same bounds hold for upper traces and for reversed aligned windows.

#### Proof

Each cyclic direction order has at most (r) length-(d) cyclic
intervals, so (J_{p,d}(x)) has at most (Kr) possible values.  Once
(J) is fixed, the two outside restrictions in (4.2) have at most
(2^{2(r-d)}) values.  This proves (4.3); subtracting from (4.1) proves
(4.4).  Reversal does not change the count.  \(\square\)

### Corollary 4.2 (the finite-seed recursion is trace-degenerate)

Start from any fixed finite bidirectional double factor and iterate
Theorem 2.1.  Then (K) remains bounded, and whenever

\[
                         d-\tfrac12\log_2r\longrightarrow\infty, \tag{4.5}
\]

the collision deficit is ((1-o(1))N).  In particular, at every Gaussian
depth (d=\Theta(\sqrt r)), almost every aligned start is lost to a
collision.  The aligned-code failure alone rules out simultaneous
near-injectivity of aligned and half-step traces.

Thus the exact recursion exists, but the conjunction requested in the
double-factor program does not: parity lifting a fixed finite seed cannot
both preserve the double-factor relation and generate near-injective
context trace codes.  A surviving recursion must introduce

\[
                         K_r\ge \frac{4^d}{2r}\,e^{-o(1)}        \tag{4.6}
\]

physically visible direction-order types by Gaussian depth (d), rather
than merely rephase a bounded library.

## 5. A seed-specific stronger obstruction

For completeness, the common-phase (Q_4) seed has an additional
invisible subgroup.  Its involution (S=(2\ 4)) fixes directions (1,3).
After (t) recursions, each base direction has become one contiguous
block of (2^t) physical directions, and the two fixed blocks remain
pointwise fixed by the iterated involution.

For every depth (d=o(2^t)), a proportion (1/2-o(1)) of cyclic
direction windows lie wholly inside those fixed blocks.  On each such
window (J),

\[
                         |J\cap S_t^{-1}J|=d.         \tag{5.1}
\]

The invisible parity subgroup from the affine trace formula therefore
has order (2^{d-1}) on half the phases.  This independently gives a
linear collision deficit.  The fixed-point-free (Q_2) seed removes this
particular subgroup obstruction, but Theorem 4.1 still kills its trace
code: its order library is also (K=1).

## 6. Exact boundary

Theorem 2.1 is a positive structural result: the former recursion gate is
not obstructed by ownership, physical cycle length, isometry, or the
same-vertex direction equations.  The necessary coordinate permutation
at the next scale is exactly (2.4).

The obstruction is information-theoretic and physical.  The adjacent
pair expansion remembers only a bounded cyclic-order library, while a
depth-(d) trace erases (2d-1) bits.  Neither hidden contexts nor affine
rephasing enlarges the visible trace alphabet.  Any next construction
must put exponentially many context-dependent order supports into the
actual direction sets seen by the target.
