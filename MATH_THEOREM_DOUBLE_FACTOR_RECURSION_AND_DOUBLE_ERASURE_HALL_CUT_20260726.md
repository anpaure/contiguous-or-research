# Corrected double-factor recursion: tagged trace closure and literal-target obstruction

Date: 2026-07-26

Method: pure mathematics only.  No computation, search, solver, or web
input is used.

> **Correction boundary.**  The originally displayed crossed child
> `P_1^times`, which applied `G_1` to the opposite state, is false.  At
> `u=0000`, `v=1100`, its direction is `R3` while the required image of
> the zeroth-child direction is `R1`.  Sections 3 and 5 below use the
> repaired crossed witness `C_S`, whose direction at `(u,v)` is defined
> from the same state used by the zeroth child.  It is a neighbour
> permutation by an explicit shorewise inverse.  The row factor and all
> tagged-code recursion statements are thereby restored.
>
> A second correction remains decisive: the augmented code supplies `J`
> as metadata, whereas a literal lower or upper OR target need not reveal
> `J`.  Every positive conclusion below is therefore explicitly a tagged
> trace theorem.  Negative collisions of the tagged code remain literal
> collisions after the tag is forgotten.

## 0. Outcome

The affine complete-mapping theorem and its corrected physical `Q_4`
certificate are valid.  On the `128` aligned even-time starts, the exact
fibre laws of the **tagged** code

\[
                         (J,p|_{J^c},x|_{J^c})
\tag{0.1a}
\]

are

\[
\boxed{
\begin{array}{c|rrrr}
d&1&2&3&4\\ \hline
\text{fibre degree}&1&2&8&128\\
\text{number of traces}&128&64&16&1\\
\text{cap-one collision excess}&0&64&112&127.
\end{array}}
\tag{0.1}
\]

Thus the finite seed does not reduce tagged erased-parity multiplicity,
and direct tensor powers multiply its nontrivial fibres.  Since forgetting
`J` only merges fibres, these are also rigorous lower bounds for literal
target collisions.

There are two exact recursive certificate operations.  The parallel
operation recurses the two old neighbour permutations on the same child
state.  The repaired crossed operation retains the physical row child
`P_0=R(G_0)` and defines its witness directly by

\[
 C_S(u,v)=
 \begin{cases}
 (u,v\oplus e_{S\delta_0(u)}),&|u|+|v|=0\pmod2,\\
 (u\oplus e_{S\delta_0(v)},v),&|u|+|v|=1\pmod2.
 \end{cases}
\tag{0.2a}
\]

The relevant context permutations are

1. the **parallel** recursion has context permutation (S\sqcup S);
2. the **crossed** recursion has context permutation
   
   \[
   L i\longleftrightarrow R(Si).
   \tag{0.2}
   \]

The zeroth row child consists of physical isometric `C_(4h)` cycles.  The
witness child need only be a neighbour permutation; its cycle structure
is irrelevant to the affine complete-mapping lemma.

For the fully crossed repaired recursion, the tagged code still fails
near-injectivity at Gaussian depth.  In dimensions

\[
                         R=2^{2n},\qquad d=\sqrt R=2^n,
\tag{0.3}
\]

its aligned tagged cap-one collision excess satisfies the lower bound

\[
 \boxed{
 {\Delta_{R,d}\over 2^{2R-1}}
 \ge {1\over 6-2^{2-n}}
 ={1\over6}+o(1).}
\tag{0.4}
\]

The same-tag collisions counted here are literal collisions as well.

Cross once using (0.2a), then recurse in parallel.  Dyadic balance makes
every `d<=R/8` direction window a transversal of the context permutation.
For the tagged code, its fibres are exactly those of

\[
 \boxed{
 \Theta_{S,d}(y)=
 \left(
 J_d(y),
 y\big|_{[R]\setminus(J_d(y)\cup S J_d(y))},
 \bigoplus_{i\in S J_d(y)}y_i
 \right).}
\tag{0.5}
\]

If `Delta(Theta)` denotes cap-one excess, the augmented affine code has
the exact excess

\[
 \boxed{
 \Delta_{\rm tag}(R,d)=2^{R-1}\Delta(\Theta_{S,d}),
 \qquad
 {\Delta_{\rm tag}(R,d)\over2^{2R-1}}
 ={\Delta(\Theta_{S,d})\over2^R}.}
\tag{0.6}
\]

The late-cross phase gate can in fact be closed exactly.  In every bottom
`Q_8` block, the selected direction and the six coordinates outside its
selected `S_8`-pair recover the two erased coordinates.  This works for
both forward and reverse windows.  Consequently

\[
                         \Delta(\Theta_{S,d}^{+})
 =\Delta(\Theta_{S,d}^{-})=0
 \qquad(d\le R/8),
\tag{0.7}
\]

and the aligned **tagged** lower and upper trace maps are injective at every
completed depth `d<=R/8`.

The four half-step sectors likewise reduce to tagged aligned codes without
losing an exterior `p`- or `x`-bit.  This proves tagged half-step
injectivity in the same envelope range.  It does **not** prove literal OR
injectivity: a completed pair and an untouched `00` pair have the same
lower restriction, a completed pair and an untouched `11` pair have the
same upper restriction, and a partial boundary can masquerade as an
untouched split pair.  Recovering `J` and the boundary from the raw target
is the exact surviving local gate.

## 1. Audit of the affine complete-mapping identity

Let (G_0,G_1) be neighbour permutations of (Q_r), with outgoing
directions (delta _0,delta _1), and let (S\in S_r) satisfy

\[
                         \delta _1(y)=S\delta _0(y)
                         \qquad(y\in Q_r).
\tag{1.1}
\]

For even (p), put

\[
 y=Sp\oplus x,\qquad d_p(x)=\delta _0(y),\qquad
 F_p(x)=x\oplus e_{d_p(x)}.
\tag{1.2}
\]

For fixed (p), translation by (Sp) gives

\[
                         Sp\oplus F_p(x)=G_0(Sp\oplus x).
\tag{1.3}
\]

Thus (F_p) is a translated conjugate of (G_0).  For fixed (x), if
(T_x(p)=p\oplus e_{d_p(x)}), then

\[
 S T_x(p)\oplus x
 =y\oplus e_{S\delta _0(y)}
 =G_1(y).
\tag{1.4}
\]

The affine map (p\mapsto Sp\oplus x) takes the even shore bijectively to
one parity shore, and a neighbour permutation bijects that shore with the
opposite shore.  Hence (T_x) is a bijection from even to odd contexts.
This proves the complete-mapping lemma with the parity bookkeeping
explicit.

For the physical lift, one coarse move in direction (i) is expanded as
(b_i,a_i).  Equation (1.3) shows that a coarse isometric (C_{2r})
becomes a physical isometric (C_{4r}).  No assertion about (G_1)'s
edges being disjoint from those of (G_0) is needed.

### The corrected `Q_4` certificate

The physical second factor is the antipodally completed factor with word

\[
                         1432\,1432,
\tag{1.5}
\]

not the earlier nonisometric word (1432\,1234).  With the common phase
classes in the displayed `Q_4` table, the ownerwise direction rows are

\[
\begin{array}{c|rrrrrrrr}
j&0&1&2&3&4&5&6&7\\ \hline
\delta _0&1&2&3&4&1&2&3&4\\
\delta _1&1&4&3&2&1&4&3&2.
\end{array}
\tag{1.6}
\]

Thus (1.1) holds for (S=(2\ 4)).  This verifies the `Q_4`
instantiation owner by owner.

## 2. Exact seed trace degrees

For an aligned coarse (d)-window, put

\[
 J_d(y)=
 \{\delta _0(y),\delta _0(G_0y),\ldots,
                         \delta _0(G_0^{d-1}y)\}.
\tag{2.1}
\]

After adjoining the moved support `J` as a tag, the aligned lower and
upper targets have the same augmented code:

\[
 \mathcal C_d(p,x)=
 \left(J_d(y),p|_{J_d(y)^c},x|_{J_d(y)^c}\right).
\tag{2.2}
\]

Indeed a completed physical pair is empty in the lower target and full in
the upper target, while an untouched pair records the same two state bits
for both signs.  The word `tagged` is essential: an untouched `00` pair
looks empty in a lower target and an untouched `11` pair looks full in an
upper target, so the raw target need not determine `J`.

In the `Q_4` certificate, the support (J_d(y)) is the cyclic (d)-set
in (1234) determined by the phase of (y) modulo four.  The four phase
fibres are the affine cosets

\[
 H,quad1000+H,quad1100+H,quad1110+H,
 \qquad
 H=\{(a,b,a,b):a,b\in\mathbb F_2\}.
\tag{2.3}
\]

Fix (J) and compare two starts in one code fibre.  Write their
differences in the variables ((p,y)) as ((z,w)).  They obey

\[
 |z|=0\pmod2,qquad z|_{J^c}=0,qquad
 (w\oplus Sz)|_{J^c}=0,qquad w\in H
\tag{2.4}
\]

for (d<4); for (d=4), (w) is arbitrary.  The dimensions of the
solution spaces in (2.4) are respectively

\[
                         0,quad1,quad3,quad7.
\tag{2.5}
\]

For completeness:

* at (d=1), an even vector on a singleton is zero, and three zero
  coordinates force (w=0);
* at (d=2), (z) has one even degree of freedom and determines the
  unique compatible (w\in H);
* at (d=3), (z) has two degrees of freedom and the one visible
  coordinate leaves one degree in (H);
* at (d=4), the even (z) has dimension three and arbitrary (w) has
  dimension four.

Exponentiating (2.5) proves all fibre degrees in (0.1).  Dividing the
(128) starts by those degrees gives the number of traces, and
(128-R_d) gives the cap-one excess.

The eight even contexts use only two distinct coarse factors.  The
translation stabilizer of (delta _0) is

\[
 L=\langle0101,1010\rangle,
\tag{2.6}
\]

so the factor choice sees only the quotient bit

\[
                         p_1\oplus p_3=p_2\oplus p_4.
\tag{2.7}
\]

This is a second, independent certificate that the finite phase hash has
only one bit of effective context dependence.

### Direct tensors

If independent seed cells are exposed at local depths
(d_1,\ldots,d_k), the tagged trace code is the Cartesian product of the
local codes.  Hence every nonempty tagged fibre has degree

\[
                         \prod_{s=1}^k\mu_{d_s},
 \qquad(\mu_1,\mu_2,\mu_3,\mu_4)=(1,2,8,128).
\tag{2.8}
\]

This is an equality, not a second-moment bound.  Direct tensoring of the
seed therefore multiplies rather than removes every nontrivial local
collision.

## 3. Two exact recursive double-factor operations

Let `G_0,G_1` be neighbour permutations in dimension `h` satisfying
`delta_1(z)=S delta_0(z)` at every owner, and suppose every component of
`G_0` is an isometric `C_(2h)`.  No cycle hypothesis on `G_1` is needed.
Write a child
vertex as ((u,v)\in Q_h^L\times Q_h^R), and put

\[
                         \epsilon(u,v)=|u|+|v|\pmod2.
\tag{3.1}
\]

Define the common zeroth child by

\[
 P_0(u,v)=
 \begin{cases}
   (G_0u,v),&\epsilon=0,\\
   (u,G_0v),&\epsilon=1.
 \end{cases}
\tag{3.2}
\]

The parallel witness is

\[
 P_1^{\parallel}(u,v)=
 \begin{cases}
   (G_1u,v),&\epsilon=0,\\
   (u,G_1v),&\epsilon=1,
 \end{cases}
\tag{3.3}
\]

The originally proposed crossed witness

\[
 \widetilde P_1^{\times}(u,v)=
 \begin{cases}
   (u,G_1v),&\epsilon=0,\\
   (G_1u,v),&\epsilon=1.
 \end{cases}
\tag{3.4}
\]

is false: it compares the direction of `G_0` at one half-state with the
direction of `G_1` at the other.

Indeed, for the `Q_4` seed, take `u=0000` and `v=1100`.  Both have even
parity, `delta_0(u)=1`, and `delta_1(v)=3`.  The required crossed image is
`R1`, whereas (3.4) uses `R3`.

The repaired crossed witness is

\[
 C_S(u,v)=
 \begin{cases}
  (u,v\oplus e_{S\delta_0(u)}),&\epsilon=0,\\
  (u\oplus e_{S\delta_0(v)},v),&\epsilon=1.
 \end{cases}
\tag{3.4a}
\]

Put

\[
\begin{aligned}
 S^{\parallel}(Li)&=L(Si),&
 S^{\parallel}(Ri)&=R(Si),\\
 S^{\times}(Li)&=R(Si),&
 S^{\times}(Ri)&=L(Si).
\end{aligned}
\tag{3.5}
\]

### Theorem 3.1 (parallel and crossed recursion)

Both

\[
 (P_0,P_1^{\parallel},S^{\parallel})
 \quad\hbox{and}\quad
 (P_0,C_S,S^{\times})
\tag{3.6}
\]
are complete-mapping certificates in dimension `2h`.  Every component of
the common row child `P_0` is an isometric `C_(4h)`.  If `G_1` is also an
isometric `C_(2h)` factor, the parallel witness has the same cycle
property; no such assertion is made or needed for `C_S`.

#### Proof

Every move of `P_0` toggles total parity, so its two sides alternate and

\[
                         P_0^2(u,v)=(G_0u,G_0v).
\tag{3.7}
\]

The simultaneous parent orbit has exact length (2h), so the child orbit
has exact length (4h).  During its first (2h) moves, it makes (h)
consecutive moves in each parent.  Every parent coordinate is therefore
used exactly once.  The next (2h) child directions repeat the first
(2h), because a parent isometric direction word has period (h).
Thus the child word is (Pi\Pi) for a permutation (Pi) of all (2h)
coordinates, proving isometry.

The same shorewise inverse argument proves that `P_1^parallel` is a
neighbour permutation.  Its direction at the same child owner is `S`
applied within the same half, proving the relation with `S^parallel`.

For `C_S`, an odd target `(u,v)` has the unique even predecessor

\[
                         (u,v\oplus e_{S\delta_0(u)}),
\tag{3.8}
\]

and an even target `(u,v)` has the unique odd predecessor

\[
                         (u\oplus e_{S\delta_0(v)},v).
\tag{3.9}
\]

Thus `C_S` is a neighbour permutation.  At an even owner, `P_0` uses
`L i`, where `i=delta_0(u)`, while `C_S` uses `R(Si)`.  At an odd owner,
`P_0` uses `R i`, where `i=delta_0(v)`, while `C_S` uses `L(Si)`.  This is
exactly the same-owner relation with `S^times`.  \(\square\)

If `S` is an involution, so are both descendants.  The crossed descendant
is fixed-point-free, irrespective of fixed points of `S`.

## 4. The invisible affine subgroup

The following invariant applies to every affine double factor, recursive
or not.  Fix a completed support (J) and put

\[
                         I_S(J)=J\cap S^{-1}J.
\tag{4.1}
\]

For every even vector (z) supported on (I_S(J)), define

\[
                         (p,x)\longmapsto
                         (p\oplus z,x\oplus Sz).
\tag{4.2}
\]

This leaves (y=Sp\oplus x) unchanged, and hence leaves the complete
direction trajectory and (J) unchanged.  Both changed vectors are
supported on (J), so (4.2) also leaves the exterior physical state
unchanged.  Therefore every tagged trace fibre over (J) has degree divisible
by

\[
 \boxed{
 2^{\max\{|J\cap S^{-1}J|-1,0\}}.}
\tag{4.3}
\]

For the parallel recursion started directly from (S_4=(2\ 4)), exactly
half the coordinates remain fixed.  If (f(J)) is the number of fixed
coordinates in a (d)-window, then averaging over all starts gives

\[
                         \mathbb E f(J)=d/2.
\tag{4.4}
\]

Indeed every coordinate belongs to exactly a (d/R) fraction of the
direction windows of an isometric factor.  Since (f\le d),

\[
 \Pr(f\ge2)\ge{d-2\over2(d-1)}.
\tag{4.5}
\]

All starts in this event lie in non-singleton tagged fibres.  Since their
tags and exterior states agree, they are also literal target collisions. A
non-singleton fibre of size (m) contributes (m-1\ge m/2) to cap-one
excess.  Thus this pure parallel recursion has

\[
 {\Delta_{R,d}\over2^{2R-1}}
 \ge {d-2\over4(d-1)}
 ={1\over4}+o(1)
\tag{4.6}
\]

whenever (d\to\infty).

## 5. Exact second moment for the fully crossed recursion

Start from the corrected dimension-four certificate and use the repaired
crossed witness (3.4a) at every level.  Denote its zeroth factor and context
permutation in dimension (h=4\cdot2^t) by (G_h) and (S_h).

For a uniform (Y\in Q_h), let (J_{h,a}(Y)) be the support of its first
(a) outgoing directions.  For distinct coordinates (i,j), put

\[
 \alpha_{h,a}(i,j)
 =\Pr(i,j\in J_{h,a}(Y)),
\tag{5.1}
\]

and define the joined pair-square

\[
 \Gamma_{h,a}
 =\sum_{i\ne j}
   \alpha_{h,a}(i,j)
   \alpha_{h,a}(S_hi,S_hj).
\tag{5.2}
\]

Every coordinate belongs to an (a/h) fraction of the windows.  This
follows by counting, on every (C_{2h}), the (a) starts whose window
contains either occurrence of a fixed direction.

When (h=2g) and (a=2u), alternation gives the exact set identity

\[
 J_{h,2u}(Y_L,Y_R)
 =LJ_{g,u}(Y_L)\mathbin{\dot\cup}RJ_{g,u}(Y_R).
\tag{5.3}
\]

The two parent starts are independent and uniform.  Since (S_h) swaps
the halves, ordered coordinate pairs lying in one half contribute
(2\Gamma_{g,u}) to (5.2).  For a cross-half ordered pair, its two
inclusion events are independent and each has probability (u/g).
There are (2g^2) ordered cross-half pairs.  Hence

\[
 \boxed{
 \Gamma_{2g,2u}
 =2\Gamma_{g,u}+{2u^4\over g^2}.}
\tag{5.4}
\]

### Lemma 5.1 (closed pair-square law)

If (a) is a power of two and the recursion has at least
(log_2a) levels below dimension (h), then

\[
 \boxed{
 \Gamma_{h,a}
 =\left(1-{1\over a}\right)
   \left({a^2\over h}\right)^2.}
\tag{5.5}
\]

#### Proof

For (a=1), no ordered pair belongs to the window and both sides vanish.
Assume the formula for ((g,u)), where (a=2u).  Put
(lambda=a^2/h=2u^2/g).  Equations (5.4) and the induction hypothesis
give

\[
\begin{aligned}
 \Gamma_{h,a}
 &=2\left(1-{1\over u}\right)
       \left({u^2\over g}\right)^2
   +2\left({u^2\over g}\right)^2\\
 &=\left(1-{1\over2u}\right)\lambda^2.
\end{aligned}
\]

This is (5.5).  \(\square\)

Now pass once more from (h) to (R=2h), and take an even depth
(d=2a).  A (d)-window has the form

\[
                         J=LA\mathbin{\dot\cup}RB,
\tag{5.6}
\]

where (A,B) are independent copies of (J_{h,a}).  Let

\[
                         C=|S_hA\cap B|.
\tag{5.7}
\]

The one-coordinate marginal and (5.2) give

\[
\boxed{
 \mathbb EC={a^2\over h}=:\lambda,
 \qquad
 \mathbb E[C(C-1)]
 =\left(1-{1\over a}\right)\lambda^2.}
\tag{5.8}
\]

Consequently

\[
 \Pr(C>0)
 \ge{(\mathbb EC)^2\over\mathbb EC^2}
 ={\lambda\over1+(1-1/a)\lambda}.
\tag{5.9}
\]

The inequality is Cauchy--Schwarz applied to
(C\mathbf1_{\{C>0\}}).

The crossed permutation (S_R) pairs (Li) with (R(S_hi)).  Therefore

\[
                         |J\cap S_R^{-1}J|=2C.
\tag{5.10}
\]

On (C>0), the subgroup (4.3) makes the tagged fibre non-singleton.  Every
member has the same moved support and exterior state, so it also gives the
same literal target.  Since (p) and (y=S_Rp\oplus x) are independent and
uniform, (5.9) is also the fraction of all affine starts lying over such
supports.  The same fibre-to-excess estimate used in (4.6) yields

\[
 \boxed{
 {\Delta_{R,d}\over2^{2R-1}}
 \ge
 {\lambda\over2\{1+(1-1/a)\lambda\}}.}
\tag{5.11}
\]

For (0.3), (a=2^{n-1}), (h=R/2), and (lambda=1/2).  Substitution
in (5.11) is exactly (0.4).  Thus the fully crossed recursion has a
positive Gaussian collision density.

## 6. A recursion which evades the overlap subgroup

Apply the repaired crossed construction (3.4a) once to the `Q_4`
certificate.  The resulting
permutation (S_8) is a fixed-point-free involution, and every one of its
transposition pairs is contained in that eight-coordinate child block.
At all higher levels use parallel recursion.  In dimension

\[
                         R=8\cdot2^t,
\tag{6.1}
\]

the resulting (S_R) is the direct sum of (2^t) copies of (S_8).

The product recursion is dyadically balanced: a direction window of
length (d) meets every bottom eight-coordinate block in either

\[
                         \left\lfloor{8d\over R}\right\rfloor
 \quad\hbox{or}\quad
                         \left\lceil{8d\over R}\right\rceil
\tag{6.2}
\]

coordinates.  This follows inductively from the exact alternation in
(5.3).  Hence, for `d<=R/8`, every bottom block contributes at most one
coordinate.  Since (S_8) has no fixed coordinate and preserves each
bottom block,

\[
                         J\cap S_RJ=\varnothing
\tag{6.3}
\]

for every such window.  In particular (6.3) holds throughout every fixed
Gaussian band once (R) is large.

Thus neither (4.3), (4.6), nor the crossed second moment proves a no-go
for this late-cross recursion.  Sections 7.2--7.4 show that this is not
merely an escape from one obstruction: its aligned phase code is exactly
injective.

## 7. Exact reduction to the double-erasure phase code

Let (S) be a fixed-point-free involution, and suppose a support (J)
satisfies (J\cap SJ=\varnothing).  Put

\[
                         R_J=[r]\setminus(J\cup SJ).
\tag{7.1}
\]

Define the phase code

\[
 \Theta_{S,d}(y)
 =\left(J_d(y),y|_{R_{J_d(y)}},
             \bigoplus_{i\in S J_d(y)}y_i\right).
\tag{7.2}
\]

### Theorem 7.1 (tagged fibres equal double-erasure fibres)

Fix an augmented affine trace code

\[
                         (J,p|_{J^c},x|_{J^c}).
\tag{7.3}
\]

Its source fibre is in canonical bijection with the fibre of (7.2) having

\[
\begin{aligned}
 y|_{R_J}
   &=(x\oplus Sp)|_{R_J},\\
 \bigoplus_{i\in SJ}y_i
   &=\bigoplus_{i\in SJ}x_i
      \oplus\bigoplus_{i\in J^c}p_i.
\end{aligned}
\tag{7.4}
\]

#### Proof

On (R_J), both endpoints of every (S)-pair lie outside (J), so the
visible (p,x) determine (y=x\oplus Sp), proving the first line.
For (i=Sj\in SJ),

\[
                         y_{Sj}=x_{Sj}\oplus p_j.
\tag{7.5}
\]

The unknown word (p|_J) must have parity

\[
                         \bigoplus_{j\in J}p_j
                         =\bigoplus_{i\in J^c}p_i,
\tag{7.6}
\]

because the full context is even.  Xoring (7.5) over (j\in J) gives the
second line of (7.4).

Conversely, let (y) satisfy the specified phase code.  Equation (7.5)
uniquely determines every erased bit

\[
                         p_j=x_{Sj}\oplus y_{Sj}.
\tag{7.7}
\]

The parity coordinate in (7.4) makes (7.6) automatic, so the completed
(p) is even.  Finally (x=y\oplus Sp) uniquely supplies the erased
(x|_J), while agreeing with the given exterior word by (7.4)--(7.7).
This construction is inverse to taking (y=Sp\oplus x).  \(\square\)

If a phase-code fibre in (7.2) has degree (m), it is replicated by
exactly (2^{r-1}) augmented trace labels.  Indeed choose the
(r-d) visible context bits freely and choose the (d) visible bits
(x|_{SJ}) subject to the one parity equation in (7.4).  There are

\[
                         2^{r-d}2^{d-1}=2^{r-1}
\tag{7.8}
\]

choices.  Summing (m-1) over the fibres proves (0.6).

### 7.2 The punctured direction fibres in the bottom `Q_4`

Let `delta_0` be the outgoing direction function of the corrected first
`Q_4` factor, and put

\[
 L_0=\langle0101,1010\rangle.
\tag{7.9}
\]

Its four outgoing direction fibres are affine cosets

\[
 C_i^+=\{z:\delta_0(z)=i\}=c_i+L_0.
\tag{7.10}
\]

Every nonzero word of `L_0` has weight two or four.  Consequently, for
every coordinate `i`, deletion of coordinate `i` is injective on every
coset of `L_0`: two members agreeing off `i` would differ by either zero
or the weight-one word `e_i`, and `e_i` is not in `L_0`.

The incoming direction fibre is

\[
 C_i^-
 =\{z:\delta_0(G_0^{-1}z)=i\}
 =G_0(C_i^+)=C_i^++e_i.
\tag{7.11}
\]

It is another coset of `L_0`, so the same one-coordinate puncturing
property holds for incoming directions.

### 7.3 Forward and reverse recovery in the crossed `Q_8`

Write a bottom `Q_8` state as `z=(z_L,z_R)`, and put

\[
                         \varepsilon(z)=|z_L|+|z_R|\pmod2.
\tag{7.12}
\]

The zeroth crossed child from (3.2) has forward outgoing direction

\[
 \rho_8^+(z)=
 \begin{cases}
  L i,&\varepsilon(z)=0,\ \delta_0(z_L)=i,\\
  R i,&\varepsilon(z)=1,\ \delta_0(z_R)=i.
 \end{cases}
\tag{7.13}
\]

Recall that

\[
 S_8(Li)=R(S_4i),\qquad S_8(Ri)=L(S_4i),
 \qquad S_4=(2\ 4).
\tag{7.14}
\]

Suppose first that the selected direction is `q=Li`.  The six coordinates
outside `{q,S_8q}` contain the other three bits of `z_L`.  The condition
`delta_0(z_L)=i` and the puncturing property of `C_i^+` recover the missing
bit `z_{Li}`.  The selected side in (7.13) gives
`varepsilon(z)=0`; total block parity then recovers the only missing right
bit `z_{R(S_4i)}`.  The case `q=Ri` is identical with left and right
interchanged and `varepsilon(z)=1`.  Thus

\[
 (\rho_8^+(z),z|_{[8]\setminus\{q,S_8q\}})
 \quad\hbox{determines }z.
\tag{7.15}
\]

For the reverse traversal, the direction of the first reverse move from
`z` is the direction entering `z` under the forward factor.  Its exact
formula is

\[
 \rho_8^-(z)=
 \begin{cases}
  R i,&\varepsilon(z)=0,\ \delta_0(G_0^{-1}z_R)=i,\\
  L i,&\varepsilon(z)=1,\ \delta_0(G_0^{-1}z_L)=i.
 \end{cases}
\tag{7.16}
\]

The reversal of the side convention is essential: a current even state
has an odd predecessor, and that predecessor moved in the right factor;
a current odd state has an even predecessor, which moved in the left
factor.  Now use the puncturing property of `C_i^-` from (7.11), followed
by the parity value read from the selected side.  This proves

\[
 (\rho_8^-(z),z|_{[8]\setminus\{q,S_8q\}})
 \quad\hbox{determines }z
\tag{7.17}
\]

as well.

### 7.4 Global visitation and exact injectivity

At every parallel recursion level, a global successor advances exactly
one child factor by one local successor step.  Therefore the subsequence
of a global orbit seen in any fixed bottom `Q_8` block is its forward
`P_0` orbit, with idle times inserted.  The reverse global orbit similarly
follows the local `P_0^{-1}` orbit.

Let a forward or reverse window have `d<=R/8`.  By (6.2), it uses at most
one direction in each bottom block.  Before that unique local move, no
earlier move of the window has changed the block.  Hence the local state
at the move is exactly the restriction of the global starting state `y`
to that block.  This remains true for cyclic windows crossing a component
seam: uniqueness of the local visit, not a linear choice of root, is the
only fact used.

The support `J_d^+(y)` or `J_d^-(y)` identifies the selected direction
`q` in every touched block.  The exterior word in the double-erasure code
records the other six coordinates.  Equations (7.15) and (7.17) recover
the full state of every touched block.  An untouched block is recorded in
full.  Thus even the parity coordinate in (7.2) is redundant.

### Theorem 7.2 (late-cross double-erasure rainbow theorem)

For the cross-once-then-parallel recursion in dimension `R=8*2^t`, both
maps

\[
 y\longmapsto
 \left(J_d^\pm(y),
 y|_{[R]\setminus(J_d^\pm(y)\cup S_RJ_d^\pm(y))}
 \right)
\tag{7.18}
\]

are injective for every `d<=R/8`.  Consequently

\[
                         \Delta(\Theta_{S_R,d}^+)
 =\Delta(\Theta_{S_R,d}^-)=0,
\tag{7.19}
\]

and Theorem 7.1 gives exact injectivity of both aligned augmented trace
codes:

\[
                         \Delta_{\rm tag}^+(R,d)
 =\Delta_{\rm tag}^-(R,d)=0.
\tag{7.20}
\]

In particular, every fixed Gaussian band `d=Theta(sqrt(R))` lies in this
range for all sufficiently large `R`.

Before Theorem 7.2, the exact remaining Hall cut for the late-cross
recursion was

\[
 \boxed{
 \sum_{\theta}
       \bigl(|\Theta_{S,d}^{-1}(\theta)|-1\bigr)_+
       =o(2^r).}
\tag{7.21}
\]

Theorem 7.2 proves the stronger equality zero for both orientations and
all `d<=R/8`.  Notice that the ordinary recursive rainbow statement

\[
                         y\longmapsto(J_d(y),y|_{J_d(y)^c})
\tag{7.22}
\]

would not by itself imply this conclusion: (7.2) additionally erases the
`d` mate coordinates `SJ`.  The new input is the punctured-coset recovery
in each bottom block.

The raw alphabet of (7.2) has size at most

\[
                         2\binom rd2^{r-2d}.
\tag{7.23}
\]

Thus it reproduces the universal capacity obstruction at half depth, but
Theorem 7.2 shows that the available alphabet is used without collision
through `d<=R/8`.

### 7.5 Exact half-step audit

It remains to pass from even-time aligned windows to every physical start
phase and length parity.  Fix an even coarse context `p`, and write the
forward lifted orbit as

\[
 E_t=(p,x_t)
 \xrightarrow{\ b_{i_t}\ }
 O_t=(p\oplus e_{i_t},x_t)
 \xrightarrow{\ a_{i_t}\ }
 E_{t+1}=(p,x_{t+1}),
 \qquad x_{t+1}=x_t\oplus e_{i_t}.
\tag{7.24}
\]

Put `i_s=i_{t+s}`.  The following table lists all four forward sectors.
The envelope `A` is the set of coarse directions whose physical pairs
are either completed or partially used.

\[
\begin{array}{c|c|l|c}
\text{start}&\text{edge length}&\text{physical direction word}
 &\text{aligned code determined}\\ \hline
E_t&2d&
 (b_{i_0}a_{i_0})\cdots(b_{i_{d-1}}a_{i_{d-1}})
 &\mathcal C_d^+(p,x_t)\\
E_t&2d+1&
 (b_{i_0}a_{i_0})\cdots(b_{i_{d-1}}a_{i_{d-1}})b_{i_d}
 &\mathcal C_{d+1}^+(p,x_t)\\
O_t&2d&
 a_{i_0}(b_{i_1}a_{i_1})\cdots
 (b_{i_{d-1}}a_{i_{d-1}})b_{i_d}
 &\mathcal C_{d+1}^+(p,x_t)\\
O_t&2d+1&
 a_{i_0}(b_{i_1}a_{i_1})\cdots
 (b_{i_d}a_{i_d})
 &\mathcal C_{d+1}^+(p,x_t).
\end{array}
\tag{7.25}
\]

The third row is for `d>=1`; the fourth includes `d=0`.  In the first row
the envelope is

\[
                         A=\{i_0,\ldots,i_{d-1}\}.
\tag{7.26}
\]

In each other row it is

\[
                         A=\{i_0,\ldots,i_d\}.
\tag{7.27}
\]

For an even start and odd length, the tagged half-step code also retains the
`a_{i_d}` endpoint.  For an odd start and even length it retains the
leading `b_{i_0}` and trailing `a_{i_d}` endpoints.  For an odd start and
odd length it retains the leading `b_{i_0}` endpoint.  These are extra
data; none is needed to form the aligned code in the last column.

Indeed, on every `k` outside `A`, neither `a_k` nor `b_k` is moved.  Their
unchanged physical state gives exactly

\[
                         x_{t,k}=a_k,
 \qquad                  p_k=a_k\oplus b_k.
\tag{7.28}
\]

Thus the tagged half-step code gives `p|_{A^c}` and `x_t|_{A^c}` with no
lost outside bit.  Its supplied full and partial pair pattern identifies every member
of `A`: in the third row the `a`-only boundary is the leading direction
and the `b`-only boundary is the trailing direction.  Hence it determines
the aligned code displayed in (7.25).

For reverse traversal, put `j_s=i_{t-1-s}`.  Starting at `E_t`, one
reverse coarse pair has physical word

\[
                         a_{j_s},b_{j_s}.
\tag{7.29}
\]

The four reverse sectors are exactly (7.25) with `b,a` interchanged,
`i_s` replaced by `j_s`, and `C^+` replaced by `C^-`.  In particular, an
odd reverse start has a leading `b`-only boundary, while an odd reverse
length has a trailing `a`-only boundary.  Outside its envelope, the odd
state differs from its even anchor only in the leading boundary pair, so
(7.28) again recovers the full exterior restriction of the even anchor.

### Theorem 7.3 (all four tagged half-step sectors)

Let `W` be a forward or reverse physical window in the late-cross factor.
Let `k(W)` be the size of its completed coarse envelope.  Explicitly,

\[
 k(W)=
 \begin{cases}
  \ell/2,&\text{even start and even edge length }\ell,\\
  \lfloor\ell/2\rfloor+1,&\text{otherwise}.
 \end{cases}
\tag{7.30}
\]

If `k(W)<=R/8`, then both augmented codes, with the full/partial support
pattern adjoined, determine the starting occurrence uniquely.

#### Proof

By (7.25) and its reverse version, the tagged half-step code determines an
aligned code of depth `k(W)`.  Theorem 7.2 recovers its even anchor.  For
an even physical start this is the starting state.  For an odd physical
start, the boundary direction identifies the unique half-edge from the
anchor to the start, and hence recovers the odd starting state as well.
The lifted successor or predecessor is deterministic, so the entire
window occurrence is recovered.  The tagged lower and upper codes carry
the same exterior state and differ only by making moved coordinates empty
or full, so the argument applies to both signs.  \(\square\)

In particular, a phase-uniform sufficient condition for every tagged
window code of edge length `ell` is

\[
                         \left\lfloor{\ell\over2}\right\rfloor+1
                         \le {R\over8}.
\tag{7.31}
\]

### 7.6 Why the literal OR theorem does not follow

The support and boundary pattern used above are not determined by one raw
lower or upper target.  On a single physical pair, a completed coarse move
can have the trajectory

\[
                         00\longrightarrow01\longrightarrow11.
\tag{7.32}
\]

Its lower intersection is `00`, identical to an untouched pair in state
`00`.  Its upper union is `11`, identical to an untouched pair in state
`11`.  Likewise a one-edge partial trajectory has intersection equal to
one endpoint state, which can be the state of an untouched pair.  Thus a
raw target need not reveal either a completed member of `J` or a partial
boundary pair.

There are literal whole-cell collisions already in the `r=4` affine seed.
Take even context `p=0000`.  Since

\[
                         \delta_0(1010)=1,
 \qquad                  \delta_0(0010)=2,
\tag{7.32a}
\]

the depth-one lower targets from these two starts have pair-state vectors

\[
\begin{array}{c|c|c}
x&J&\text{lower target on pairs }1,2,3,4\\ \hline
1010&\{1\}&(00,00,11,00)\\
0010&\{2\}&(00,00,11,00).
\end{array}
\tag{7.32b}
\]

Thus the raw lower target is equal although the moved support differs.
Likewise

\[
                         \delta_0(0101)=1,
 \qquad                  \delta_0(1101)=2,
\tag{7.32c}
\]

and the two depth-one upper targets are both

\[
                         (11,11,00,11),
\tag{7.32d}
\]

with supports `{1}` and `{2}` respectively.  This is an actual collision,
not merely a failure of a proposed local decoder.

Consequently Theorem 7.3 proves the half-step claim only after the support
pattern is tagged.  To obtain literal OR injectivity one still needs an
intrinsic decoder

\[
 \text{raw lower target}\longmapsto(J,\text{boundary roles}),
 \qquad
 \text{raw upper target}\longmapsto(J,\text{boundary roles}),
\tag{7.33}
\]

or a separate argument proving that targets arising from different tags
are disjoint.  Neither is supplied by the affine parity lift.

## 8. Proved boundary

Proved here:

1. the affine complete-mapping proof and corrected physical `Q_4`
   instantiation;
2. the exact seed trace degrees (0.1), showing no parity improvement;
3. multiplicative failure of direct tensor powers;
4. two literal recursive double-factor operations;
5. positive Gaussian collision density for the pure parallel and fully
   crossed recursions;
6. an explicit late-cross recursion for which the overlap subgroup is
   identically trivial at shallow depth;
7. the exact augmented-code-to-phase identity (0.6);
8. exact forward and reverse double-erasure injectivity, and hence exact
   aligned tagged-code injectivity, for every `d<=R/8`; and
9. exact tagged half-step injectivity in all four start/length sectors
   whenever the completed envelope has size at most `R/8`.

Not proved here:

* recovery of `J` and boundary roles from a literal lower or upper target;
* exclusion of collisions between different support tags; and
* the outer packet coupling after a literal local trace code is obtained.

Therefore the `Q_4` seed is not itself a trace improvement, and the two
most homogeneous recursions are rigorously closed.  The asymmetric
late-cross recursion nevertheless converts that seed into an exact
two-sided **tagged** code throughout the entire shallow range `d<=R/8`,
and Theorem 7.3 closes every tagged half-step convention in the same
envelope range.  The literal OR lane remains open at the tag-recovery gate
(7.33), before outer packet coupling.
