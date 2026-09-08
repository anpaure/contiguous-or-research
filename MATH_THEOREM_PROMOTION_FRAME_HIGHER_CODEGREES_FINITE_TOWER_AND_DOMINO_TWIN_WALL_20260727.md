# Promotion-frame higher codegrees, finite backward towers, and the domino-twin wall

Date: 2026-07-27

Scope: constant-one owner resolution; pure mathematics only.  No
computation, search, solver, or fixed-uniformity matching theorem is used.

## 0. Verdict

Put

\[
 n=2m,\qquad M=m+H,\qquad
 \mathcal X=\binom{[2m]}m,\qquad
 \mathcal U=\binom{[2m]}M,
\tag{0.1}
\]

and assume

\[
 H\longrightarrow\infty,\qquad H=o(m),\qquad m\ge 4H.
\tag{0.2}
\]

An ordinary promotion frame is

\[
 F(U,\pi)=\{U\}\mathbin{\dot\cup}\mathcal O(U,\pi),
 \qquad
 \mathcal O(U,\pi)=
 \{\text{the }M\text{ cyclic }m\text{-windows of }\pi\}.
\tag{0.3}
\]

Every owner has degree

\[
 D=\binom mH m!H!={m!^2\over(m-H)!},
\tag{0.4}
\]

and every top has degree (R=(M-1)!).  At the packing calibration
(D/R=1-o(1)).

This note proves the following four exact statements.

1.  Let (2\le s\le L), where (L=o(H)).  For any (s) distinct
    owners (X_0,\ldots,X_{s-1}), the number (d(X_0,\ldots,X_{s-1}))
    of full physical frames containing all of them satisfies

    \[
     \boxed{
     {d(X_0,\ldots,X_{s-1})\over D}
     \le
     \left({C(s-1)^2\over m^2}\right)^{s-1}.}
    \tag{0.5}
    \]

    The exponent is sharp.  There are monotone consecutive families for
    which, with (t=s-1<H),

    \[
     {d(X_0,\ldots,X_t)\over D}={2\over(m)_t^2}.
    \tag{0.6}
    \]

    Here \((m)_t=m(m-1)\cdots(m-t+1)\).

    With one compatible top fixed, the corresponding bound is

    \[
     {d(U;X_0,\ldots,X_t)\over m!H!}
     \le
     \left({Ct^2\over mH}\right)^t.
    \tag{0.7}
    \]

2.  If an owner \(X\) is not a vertex of a full frame \(G\), then

    \[
     |\mathcal E(X)\cap\mathcal E(G)|\le {CD\over m^2}.
    \tag{0.7a}
    \]

    More generally let \(F,G\) be arbitrary full frames, first assign
    every shared top or owner resource to their common prefix, and put

    \[
     P=V(F)\cap V(G),\qquad
     F^\circ=V(F)\setminus P,\qquad
     G^\circ=V(G)\setminus P.
    \tag{0.7b}
    \]

    If \(\mathcal E(S)\) denotes the catalogue frames meeting a resource
    set \(S\), then

    \[
     \boxed{
     |(\mathcal E(F^\circ)\cap\mathcal E(G^\circ))
       \setminus\mathcal E(P)|
     \le {CD\over m}.}
    \tag{0.8}
    \]

    More generally, after global equality resolution, if
    \(A_1,\ldots,A_p,B\) are the residual arms of
    \(F_1,\ldots,F_p,G\), then

    \[
     \left|\mathcal E(B)\cap
       \bigcup_{i=1}^p\mathcal E(A_i)\right|
     \le {CpD\over m}.
    \tag{0.9}
    \]

    Thus at time zero, with the usual clock
    \(\nu_0=((M+1)\max\{D,R\})^{-1}\), the common-event rate is

    \[
     O(p/m^2).
    \tag{0.10}
    \]

3.  A finite ordered pair-column tower really would suffice if (0.10)
    had its expected hereditary form.  Precisely, a tower cut at
    (J=\lceil(\log m)^2\rceil) closes with multiplicative error

    \[
     \exp\!\left[
       O\left({T J^2\over m^2z^2}\right)
     \right]=1+o(1),
     \qquad
     T=(M+1)\log(1/z),\quad z=m^{-1/20}.
    \tag{0.11}
    \]

    Hence an infinite static tower is not intrinsically necessary.  The
    exact missing input is the pointwise current-state estimate

    \[
     a_J(t)\le {CJ^2\over m^2u(t)^2}
    \tag{PCE}
    \]

    for the equality-resolved terminal pair extension at the cutoff.

4.  PCE is false for arbitrary live subcatalogues, even inside the
    literal promotion-frame catalogue.  If (X,Y) are owners at
    Johnson distance one and one retains exactly the frames containing
    both, then

    \[
     \mathcal E_{XY}(X)=\mathcal E_{XY}(Y),\qquad
     |\mathcal E_{XY}(X)|={2D\over m^2}.
    \tag{0.12}
    \]

    The two owner stars are exact **domino twins**.  The residual
    catalogue meets

    \[
     \binom{m-1}{H-1}
    \tag{0.13}
    \]

    distinct tops but has matching number one.  Under the compensated
    clock its integrated live-state normalized drift coefficient over
    the reference interval down to density \(z\) is exactly

    \[
                         \log(1/z),
    \tag{0.14}
    \]

    while every ordered extension by a second disjoint event is empty.
    The core retains \(1-o(1)\) of its edges after deleting the vertices
    of any constructed \(O((\log m)^2)\)-edge disjoint history.
    Thus no finite high-order cutoff can manufacture PCE from static
    higher codegrees: the terminal common-event term can remain critical
    while the entire disjoint extension tower above it vanishes.

Consequently (0.5)--(0.10) supply the full static geometry requested by
the ordered pair-column proposal, and (0.11) proves that a finite cutoff
would be analytically adequate.  But (0.12)--(0.14) give a literal
physical obstruction to the needed hereditary pointwise bound.  A
near-perfect matching in the original unpruned catalogue is **not**
refuted.  Its remaining exact gate is a trajectory-specific theorem
showing that random deletion does not concentrate a positive weighted
mass onto domino-twin cores.  Static codegrees, at every finite order,
do not imply that statement.

## 1. Rooting a frame at one owner

Fix (X\in\mathcal X).  Every frame through (X) has a unique rooted
description

\[
 (A;x_1,\ldots,x_m;a_1,\ldots,a_H),
\tag{1.1}
\]

where

\[
 A\in\binom{[2m]\setminus X}H,
\tag{1.2}
\]

((x_1,\ldots,x_m)) is an ordering of (X), and
((a_1,\ldots,a_H)) is an ordering of (A).  The cyclic order is

\[
 x_1x_2\cdots x_m a_1a_2\cdots a_H,
\tag{1.3}
\]

modulo rotation.  The root is unique because (X) occurs exactly once
in the owner deck.  Thus the number of descriptions is

\[
 \binom mH m!H!=D.
\tag{1.4}
\]

Let (Y\ne X), put

\[
 L(Y)=X\setminus Y,\qquad E(Y)=Y\setminus X,
 \qquad d(Y)=|L(Y)|=|E(Y)|.
\tag{1.5}
\]

If (d(Y)<H), then (Y) lies in the rooted deck if and only if one of
the following two alternatives holds:

\[
\begin{array}{lll}
 +:&L(Y)=\{x_1,\ldots,x_d\},
 &E(Y)=\{a_1,\ldots,a_d\},\\[1mm]
 -:&L(Y)=\{x_{m-d+1},\ldots,x_m\},
 &E(Y)=\{a_{H-d+1},\ldots,a_H\}.
\end{array}
\tag{1.6}
\]

This is merely the literal effect of shifting the (m)-window right or
left by (d) positions.

### Lemma 1.1 (exact two-shore chain formula)

Let (Y_1,\ldots,Y_t) be distinct owners with
(1\le d_i=d(Y_i)<H).  Assign each (i) a sign
(\sigma_i\in\{+,-\}).  On either sign, list the distinct distances in
increasing order and write their positive successive gaps as

\[
 g_1^+,\ldots,g_a^+,qquad
 g_1^-,\ldots,g_b^-.
\tag{1.7}
\]

Put

\[
 p=\sum_{r=1}^a g_r^+,qquad
 q=\sum_{r=1}^b g_r^-.
\tag{1.8}
\]

Call the signing admissible if, separately on each sign, both the
(L(Y_i))'s and the (E(Y_i))'s form the prescribed nested chains; the
maximal (L)-sets on opposite signs are disjoint; and the maximal
(E)-sets have the prefix--suffix intersection forced by their sizes.

If (p+q\le H), the exact fraction of rooted descriptions realizing
this signing is

\[
 \boxed{
 \left[
 { (m-p-q)!\,
   \prod_{r=1}^a g_r^+!\,
   \prod_{r=1}^b g_r^-!
  \over m!}
 \right]^2.}
\tag{1.9}
\]

Nonadmissible signings contribute zero, and the events belonging to
distinct admissible signings are disjoint.

#### Proof

Formula (1.6) forces the nesting and disjointness conditions.  For an
admissible signing, the number of orders of (X) having the displayed
prefix and suffix checkpoint sets is

\[
 (m-p-q)!
 \prod_{r=1}^a g_r^+!
 \prod_{r=1}^b g_r^-!.
\tag{1.10}
\]

Now choose (A) and order it simultaneously, equivalently choose a
uniform ordered (H)-tuple without repetition from the (m)-element
set ([2m]\setminus X).  The prescribed prefix and suffix layers may be
ordered in the product of the gap factorials.  The middle
(H-p-q) positions may be filled by an arbitrary ordered tuple from
the remaining (m-p-q) labels.  Hence the number of choices is

\[
 \left(\prod g_r^+!\prod g_r^-!\right)
 { (m-p-q)!\over(m-H)!}.
\tag{1.11}
\]

The total number of ordered (H)-tuples is (m!/(m-H)!), so the
probability in (1.11) is the same factorial ratio as the probability in
(1.10).  Their product is (1.9).

For (0<d<H<m/2), a prescribed nonempty set cannot be simultaneously
the first and the last (d)-set of one order.  Thus the sign of every
realized owner is unique, proving disjointness of the signing events.
\(\square\)

### Theorem 1.2 (all fixed-order owner codegrees)

Let (L=o(H)).  Uniformly for (1\le t<L) and distinct owners
(X,Y_1,\ldots,Y_t),

\[
 {d(X,Y_1,\ldots,Y_t)\over D}
 \le \left({Ct^2\over m^2}\right)^t.
\tag{1.12}
\]

#### Proof

First suppose all (d_i<H) and consider an admissible signing with
(p+q\le H).  There are (t=a+b) nonempty gap layers and
(k=p+q\ge t).  Since (k\le2H<m/2),

\[
 { (m-k)!\prod g_r^+!\prod g_r^-!\over m!}
 ={\prod g_r^+!\prod g_r^-!\over(m)_k}
 \le {k!\over(m)_k}
 ={1\over\binom mk}
 \le {1\over\binom mt}
 \le\left({2t\over m}\right)^t.
\tag{1.13}
\]

There are at most (2^t) signings.  Equations (1.9) and (1.13) give

\[
 2^t\left({2t\over m}\right)^{2t}
 =\left({8t^2\over m^2}\right)^t.
\tag{1.14}
\]

If an admissible signing has \(p+q>H\), its maximal prefix and suffix
\(E\)-sets have union \(A\); hence the top extension \(A\) is forced.
The same is true if some \(d_i=H\), because then \(E(Y_i)=A\).
In the latter case the prescribed \(H\)-set in \(X\) may occupy at
most \(M\) cyclic positions.  Thus these cases have total probability
at most

\[
 {2^tM\over\binom mH}.
\tag{1.15}
\]

As (t\le L=o(H)) and (H=o(m)),

\[
 H\log(m/H)\gg t\log(m/t),
\tag{1.16}
\]

and its left side also dominates \(\log M\).  Hence (1.15) is smaller than
((Ct^2/m^2)^t), uniformly in the stated range.  Enlarging (C)
absorbs (1.14) and (1.15), proving (1.12).  \(\square\)

### Proposition 1.3 (sharp monotone chain)

Fix distinct labels (x_1,\ldots,x_t\in X) and
(a_1,\ldots,a_t\notin X), where (t<H), and put

\[
 Y_j=
 X\setminus\{x_1,\ldots,x_j\}
 \cup\{a_1,\ldots,a_j\},qquad1\le j\le t.
\tag{1.17}
\]

Then

\[
 {d(X,Y_1,\ldots,Y_t)\over D}={2\over(m)_t^2}.
\tag{1.18}
\]

#### Proof

The only admissible signings put all (Y_j)'s on one shore.  On either
shore the gaps are all one, (p=t,q=0), and (1.9) equals
(((m-t)!/m!)^2=(m)_t^{-2}).  The two shore events are disjoint.
\(\square\)

### Proposition 1.4 (one fixed top)

For a fixed compatible top (U\supset X), and uniformly for
(1\le t<L=o(H)),

\[
 {d(U;X,Y_1,\ldots,Y_t)\over m!H!}
 \le\left({Ct^2\over mH}\right)^t.
\tag{1.19}
\]

#### Proof

Here (A=U\setminus X) is fixed and the two random objects are an
order of (X) and an independent order of (A).  In the range
(p+q\le H), the analogue of (1.9) is

\[
 { (m-p-q)!\prod g!\over m!}
 { (H-p-q)!\prod g!\over H!}.
\tag{1.20}
\]

The argument in (1.13), once with (m) and once with (H), bounds
this by

\[
 \left({2t\over m}\right)^t
 \left({2t\over H}\right)^t.
\tag{1.21}
\]

Summing \(2^t\) signings gives (1.19).  If \(p+q>H\), the \(X\)-order
contains prescribed boundary pieces of total size greater than \(H\).
If an owner is at distance \(H\), its prescribed \(H\)-set must occur
as one of at most \(M\) cyclic \(H\)-blocks in the \(X\)-part of the
rooted order.  Thus all remaining cases have probability at most

\[
 {2^tM\over\binom mH},
\tag{1.22}
\]

which is negligible compared with the right-hand side of (1.19)
because \(t=o(H)\).  \(\square\)

## 2. A sharp static common-event bound

The following elementary interval lemma is the point at which the
complete cyclic geometry improves the crude (M^2\Delta_2) estimate.

### Lemma 2.1 (sphere intersections with one owner deck)

Let (X\in\mathcal X), let (G=F(V,\pi)), and let

\[
 a=|X\setminus V|.
\tag{2.1}
\]

For (a\le d<H),

\[
 \left|\{Y\in\mathcal O(G):d_J(X,Y)=d\}\right|
 \le4d-2a+1\le4d+1.
\tag{2.2}
\]

For (a>d) the set is empty.

#### Proof

Put (C=V\setminus X), so (|C|=H+a).  Every owner of (G) is
(Y=V\setminus B), where (B) is one of the cyclic (H)-intervals of
(\pi).  A direct count gives

\[
 d_J(X,Y)=|C\setminus B|.
\tag{2.3}
\]

Fix one valid interval (B_0).  If (B) is another, then both omit
exactly (d) members of (C), and therefore

\[
 |C\cap B\cap B_0|\ge |C|-2d=H+a-2d.
\tag{2.4}
\]

Since \(M\ge2H\), two cyclic \(H\)-intervals whose start positions have
circular distance \(\delta\le M/2\) intersect in at most \(H-\delta\)
points.  Equations (2.4) and this bound imply

\[
 \delta\le2d-a.
\tag{2.5}
\]

All valid starts consequently lie in the circular ball of radius
(2d-a) about the start of (B_0), which contains
(4d-2a+1) positions.  If (a>d), (2.3) is impossible.  \(\square\)

### Theorem 2.2 (fully equality-resolved common-event bounds)

If an owner \(X\) is not a vertex of an ordinary frame \(G\), then

\[
 |\mathcal E(X)\cap\mathcal E(G)|\le {CD\over m^2}.
\tag{2.6a}
\]

Let \(F,G\) now be arbitrary ordinary frames and resolve all physical
equalities before counting the cross event.  Thus put

\[
 P=V(F)\cap V(G),\qquad
 F^\circ=V(F)\setminus P,\qquad
 G^\circ=V(G)\setminus P.
\tag{2.6b}
\]

Then

\[
 |(\mathcal E(F^\circ)\cap\mathcal E(G^\circ))
     \setminus\mathcal E(P)|
 \le {CD\over m}.
\tag{2.6}
\]

The same conclusion holds for arbitrary residual arms
\(A\subseteq F^\circ\), \(B\subseteq G^\circ\).

The resolution in (2.6b) is essential.  Before it, a shared owner
\(X\in V(F)\cap V(G)\) contributes the diagonal
\(|\mathcal E(X)|=D\), and a shared compensation clock is also counted
twice.  In the exact union reference both belong to \(P\) once; the
positive cross term is only
\((\mathcal E(F^\circ)\cap\mathcal E(G^\circ))
\setminus\mathcal E(P)\).  The proof below bounds the larger
intersection before subtracting \(\mathcal E(P)\).

#### Proof

First count a common event frame through an arbitrary owner \(X\) and
an owner of \(G\), with multiplicity.  The exact owner-pair codegrees are

\[
 {d(X,Y)\over D}=
 \begin{cases}
  2\binom m d^{-2},&1\le d<H,\\[1mm]
  (m-H+1)\binom mH^{-2},&d=H,\\[1mm]
  0,&d>H.
 \end{cases}
\tag{2.7}
\]

Lemma 2.1 gives

\[
\begin{aligned}
 \sum_{Y\in\mathcal O(G)}d(X,Y)
 &\le D\left[
 2\sum_{d=1}^{H-1}{4d+1\over\binom md^2}
 +{M(m-H+1)\over\binom mH^2}
 \right]\\
 &\le {CD\over m^2}.
\end{aligned}
\tag{2.8}
\]

Indeed the \(d=1\) term is \(O(m^{-2})\); the sum over \(d\ge2\) is
\(O(H^2m^{-4})=o(m^{-2})\); and the \(d=H\) term is
superpolynomially smaller.  An event meeting \(G\) through its top and
also containing \(X\) contributes either zero or

\[
 m!H!={D\over\binom mH}=o(D/m^2).
\tag{2.8a}
\]

This proves (2.6a).  For the resolved two-arm statement, every owner
\(X\in F^\circ\) is absent from \(G^\circ\), so (2.8) applies without
the diagonal term \(d(X,X)=D\).  Summing over at most \(M\) owners of
\(F^\circ\) gives \(CD/m\).

It remains to count events using the top of one displayed frame and an
owner of the other.  A compatible top--owner pair lies in exactly
(m!H!) frames.  Hence both orientations together contribute at most

\[
 2M m!H!
 ={2MD\over\binom mH}=o(D/m).
\tag{2.9}
\]

If the two original frames have the same top, that top lies in \(P\)
and has already been removed from both arms.  Otherwise no event can
use both distinct top vertices.  The preceding counts may overcount
common events, so (2.6) follows.  Passing to subsets \(A,B\) can only
decrease the event-set intersection.  \(\square\)

Taking a union over (F_1,\ldots,F_p) proves (0.9).  Notice the gain:
the crude maximum-codegree estimate gives order
(M^2D/m^2=\Theta(D)), while the physical sphere census gives
(O(D/m)).

## 3. What a finite backward cutoff actually needs

We isolate the analytic issue without any promotion-specific notation.

### Lemma 3.1 (finite backward-tower lemma)

Let (F_0(t),\ldots,F_{J+1}(t)) be nonnegative stopped observables on
([t_0,t_1]), and suppose

\[
 \mathcal L F_j(t)\le\kappa(t)F_{j+1}(t),
 \qquad0\le j\le J,
\tag{3.1}
\]

where \(\kappa\ge0\).  Assume the pointwise terminal domination

\[
                         F_{J+1}(t)\le a_J(t)F_J(t).
\tag{3.2}
\]

Put

\[
 A(t)=\int_t^{t_1}\kappa(v)\,dv,
 \qquad
 \Phi_J(t)=\sum_{j=0}^J{A(t)^j\over j!}F_j(t).
\tag{3.3}
\]

Then

\[
 \mathcal L\Phi_J(t)\le\kappa(t)a_J(t)\Phi_J(t).
\tag{3.4}
\]

Consequently

\[
 \exp\left[-\int_{t_0}^t\kappa(v)a_J(v)\,dv\right]
 \Phi_J(t)
\tag{3.5}
\]

is a stopped supermartingale.  If initially

\[
 F_j(t_0)\le B\alpha^j\qquad(0\le j\le J),
\tag{3.6}
\]

then

\[
 \mathbb E F_0(t)
 \le B\exp\left[
 A(t_0)\alpha+
 \int_{t_0}^{t_1}\kappa(v)a_J(v)\,dv
 \right].
\tag{3.7}
\]

#### Proof

Differentiate the weights in (3.3), using (A'=-\kappa).  The term
from (F_{j+1}) cancels the derivative of the weight of (F_{j+1})
for every (j<J).  The only uncancelled positive term is

\[
 {\kappa A^J\over J!}F_{J+1}
 \le {\kappa a_JA^J\over J!}F_J
 \le\kappa a_J\Phi_J,
\tag{3.8}
\]

which proves (3.4)--(3.5).  At (t_0), (3.6) gives

\[
 \Phi_J(t_0)\le
 B\sum_{j=0}^J{(A(t_0)\alpha)^j\over j!}
 \le B e^{A(t_0)\alpha}.
\tag{3.9}
\]

Optional stopping proves (3.7).  \(\square\)

For the ordered pair-column tower, the exact union-deficit identity

\[
 (r_g-1)_+\le\binom{r_g}{2}
\tag{3.10}
\]

adds one common-event pair column.  A tower configuration of order
(J), together with its equality-resolved prefix factors, has
(O(J)) displayed marginal factors and hence (O(J^2)) possible
endpoint pairs.  Thus the sharp desired current-state estimate is

\[
 a_J(t)\le{CJ^2\over m^2u(t)^2}.
\tag{3.11}
\]

Equivalently, for two fully equality-resolved arms \(a,b\), put

\[
 \beta_t(a,b)
 ={1\over (M+1)\Delta_t}
 |\{g:g\cap a\ne\varnothing,\ g\cap b\ne\varnothing\}|.
\tag{3.11a}
\]

If a cutoff state has \(p=O(J)\) nonprivate arms, the exact pair
domination gives the top growth coefficient

\[
 q(t)\le\binom p2\max_{a,b}\beta_t(a,b).
\tag{3.11b}
\]

At time zero, Theorem 2.2 proves
\(\beta_0(a,b)=O(m^{-2})\) for fully equality-resolved arms,
including two rows sharing their protected center or top.
Theorem 1.2 supplies the corresponding static initializer.  Each pair
column exposes two witness incidences, so initializing a base excess
\(s\) through cutoff \(J\) requires the higher-codegree/path-mesh
certificate through

\[
                         2(s+J)\le L_{\rm pm},
\tag{3.11c}
\]

not merely \(s+J\le L_{\rm pm}\).

If (3.11) held hereditarily down to (u=z=m^{-1/20}), then with

\[
 J=\lceil(\log m)^2\rceil,\qquad
 T=(M+1)\log(1/z)=O(m\log m),
\tag{3.12}
\]

and bounded \(\kappa\),

\[
 \int_0^T\kappa a_J
 \le {CTJ^2\over m^2z^2}
 =O(m^{-9/10}(\log m)^5)=o(1).
\tag{3.13}
\]

The same calculation bounds (A(0)\alpha), since the static endpoint
factor at order at most (J) is
(O(J^2/m^2)).  Lemma 3.1 would therefore replace the infinite tower
by a finite (J)-level tower with (1+o(1)) loss.

This proves that the factorial/time-simplex part of the proposal is
sound.  It also identifies exactly what it does not prove: (3.11) is a
statement about the **current residual event set**, whereas Theorems
1.2 and 2.2 count the original catalogue.

The sharper top-state version, including the exact terminal coefficient
\(q(t)\), the \(O(p^2)\) arm-pair multiplicity, and the cutoff tail
\(\exp[-\Theta((\log m)^3)]\), is proved in
MATH_AUDIT_ORDINARY_FRAME_PAIR_COLUMN_FINITE_CUTOFF_AND_PAIR_STAR_20260727.md.
That audit reaches the same boundary: the finite cutoff is valid under
the dynamic whole-arm condition

\[
 \beta_t(a,b)\le m^{-2+o(1)}
\tag{HCE}
\]

outside aggregate \(o(E_t)\) incidence, and HCE is not a consequence of
static higher codegrees.

## 4. The literal domino-twin residual

### Theorem 4.1 (distance-one twin core)

Let (X,Y\in\mathcal X) have Johnson distance one, and let

\[
 \mathcal K_{XY}
 =\{F(U,\pi):X,Y\in\mathcal O(U,\pi)\}.
\tag{4.1}
\]

Regard this as a subhypergraph of the physical promotion-frame
catalogue, with no alteration of any retained edge.  Then:

1. its number of edges is

   \[
                    |\mathcal K_{XY}|={2D\over m^2};
   \tag{4.2}
   \]

2. the stars of \(X\) and \(Y\) are identical and equal to the complete
   edge set of \(\mathcal K_{XY}\);
3. its maximum degree is \(\Delta_{XY}=2D/m^2\);
4. it contains edges on exactly

   \[
                    \binom{m-1}{H-1}
   \tag{4.3}
   \]

   distinct top vertices; and
5. its matching number is one.

#### Proof

Equation (4.2) is the exact pair-codegree formula (2.7) at (d=1).
Every retained edge contains both (X) and (Y), proving equality of
their stars.  No vertex can have degree larger than the total number of
retained edges, so this common degree is the maximum.  A common top is
obtained by adjoining (H-1) labels to (X\cup Y), whose complement
outside (X\cup Y) has size (m-1); this gives (4.3).  Every such top
does support retained cycles by the block count used in the pair
codegree formula.  Finally, all retained edges share (X) and (Y),
so a matching contains at most one edge, and the catalogue is nonempty.
\(\square\)

### Corollary 4.2 (critical normalized drift with no upper tower)

Run the compensated clock on \(\mathcal K_{XY}\), with edge rate

\[
 \nu={1\over (M+1)\Delta_{XY}}.
\tag{4.4}
\]

While \(X,Y\) are live, the marginal deletion hazard of each is
\(1/(M+1)\), but their normalized common-event drift coefficient is
also

\[
 \nu\,|\mathcal E_{XY}(X)\cap\mathcal E_{XY}(Y)|
 ={1\over M+1}.
\tag{4.5}
\]

Consequently, over the deterministic reference interval

\[
 T=(M+1)\log(1/z),
\tag{4.6}
\]

the integrated normalized drift coefficient is exactly

\[
 \int_0^T{dt\over M+1}=\log(1/z).
\tag{4.7}
\]

Equation (4.7) is not asserted to be the pathwise compensator continued
after the first deletion: the realized compensator stops when the twin
pair dies.  It is the coefficient appearing in the normalized
first-moment/reference comparison for as long as the displayed
configuration is live.

On the other hand, there do not exist two disjoint retained event edges,
so every ordered disjoint extension tower above the first common-event
column is empty.

#### Proof

The star identity in Theorem 4.1 makes the intersection in (4.5) equal
to the full \(\Delta_{XY}\)-edge set at every live state of the isolated
twin catalogue.  Integrating this live-state coefficient over the
reference interval gives (4.7).  The last statement follows from
matching number one.
\(\square\)

### Theorem 4.3 (polylogarithmic histories do not remove the wall)

Let \(J=O((\log m)^2)\).  There are \(J\) mutually vertex-disjoint
physical frames \(Q_1,\ldots,Q_J\) avoiding \(X,Y\) such that the
subcatalogue

\[
 \mathcal K_{XY}^{\boldsymbol Q}
 =
 \{K\in\mathcal K_{XY}:
   K\cap(Q_1\cup\cdots\cup Q_J)=\varnothing\}
\tag{4.8a}
\]

satisfies

\[
 |\mathcal K_{XY}^{\boldsymbol Q}|
 =\left(2-o(1)\right){D\over m^2}.
\tag{4.8b}
\]

In particular one may expose a genuine \(J\)-edge matching history,
delete all of its vertices, and still retain an asymptotically full
domino-twin core among the surviving physical edges.

#### Proof

Choose the \(Q_i\)'s greedily.  After \(j\) choices, at most
\(j(M+1)\max\{D,R\}\) catalogue edges meet an already used vertex,
whereas the full catalogue has \(NR\) edges and \(N\) is exponential
in \(m\).  Avoiding the two additional owner stars of \(X,Y\) changes
nothing at this scale.  Thus \(J\) choices exist.

Their union contains \(JM\) owner vertices and \(J\) top vertices.
For every owner \(Z\notin\{X,Y\}\), Theorem 1.2 with \(t=2\) gives

\[
 d(X,Y,Z)\le {C D\over m^4}.
\tag{4.8c}
\]

Hence deleting all owner vertices of the \(Q_i\)'s removes from
\(\mathcal K_{XY}\) at most

\[
 {CJM D\over m^4}
 =O\left({J\over m}\right){D\over m^2}
 =o(D/m^2)
\tag{4.8d}
\]

edges.

The common tops of \(X,Y\) number
\(\binom{m-1}{H-1}\), and symmetry gives the same number of
\(X,Y\)-frames on each such top.  Deleting the \(J\) top vertices
therefore removes at most the fraction

\[
 {J\over\binom{m-1}{H-1}}=o(1)
\tag{4.8e}
\]

of the pair core.  Combine (4.2), (4.8d), and (4.8e).
\(\square\)

This is stronger than merely observing that a maximum-codegree bound can
inflate after restriction.  It is an exact physical residual in which
the terminal pair correction is order one, all higher **disjoint**
extensions vanish, and the root support is large.  Therefore no
inequality deducing PCE from a finite collection of static disjoint
higher-codegree bounds can be valid for all binary edge deletions.

Nor is the obstruction an artefact of allowing singleton owner arms.
Theorem 4.1 of
MATH_AUDIT_ORDINARY_FRAME_PAIR_COLUMN_FINITE_CUTOFF_AND_PAIR_STAR_20260727.md
constructs two complete physical frame arms \(f,f'\) in an
edge-deletion residual of maximum degree two, together with
\(\Theta(m)\) pairwise disjoint complete event frames meeting both.
Their normalized equality-resolved whole-arm common-event coefficient
is \(\Theta(1)\).  Thus the same hereditary failure occurs at the exact
arm granularity used by HCE.

The construction is not asserted to be a vertex-induced state reached
with appreciable probability by random greedy matching.  That
distinction is the surviving positive route.  One must prove a
trajectory-specific incidence-weighted assertion of the form

\[
 \sum_{(X,Y)\ \mathrm{live}}
 w_{XY}(t)
 { |\mathcal E_t(X)\cap\mathcal E_t(Y)|
  \over \Delta_t}
 =o(1)\sum_{(X,Y)\ \mathrm{live}}w_{XY}(t)
 \tag{4.9}
\]

for the actual prefix weights, after quarantining (o(W)) owner mass.
Neither (0.5) nor its all-order extension supplies (4.9) by itself.

## 5. Exact proved/conditional boundary

Proved unconditionally:

1. the exact two-shore chain formula (1.9);
2. the optimal fixed-order higher-codegree bound (1.12), with sharp
   family (1.18);
3. the fixed-top analogue (1.19);
4. the physical two-frame common-event bound (2.6);
5. the finite backward-tower lemma and the (o(1)) cutoff ledger
   (3.13); and
6. the literal domino-twin residual (4.1)--(4.7).

Not proved:

1. PCE along the actual random greedy trajectory;
2. the weighted anti-concentration statement (4.9);
3. a matching of (N-o(N)) ordinary frames;
4. seeded residual resilience after installing the conveyor bank; or
5. coefficient one.

Thus the ordered pair-column proposal has been reduced sharply, not
discarded.  Finite cutoff is adequate; hereditary common-event
anti-concentration is indispensable and cannot be replaced by static
higher codegrees, even at all finite orders.
