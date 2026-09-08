# Hamming-two slab collision derivatives and the local-minimum gate

Date: 2026-07-26

Method: pure mathematics only.  No computation, search, solver, or web
input is used.

## 0. Result

For the full family of \(Q_{R+1}\) slab resolutions, the one-depth
factorial collision derivative has an exact score form.  Remove the two
current packets of a slab and call the remaining target load \(B\).  If
\(\Gamma_a\) is the aggregate \(0/1\) target image of resolution \(a\),
then

\[
 {\cal C}(B+\Gamma_a)-{\cal C}(B+\Gamma_0)
   =\langle B,\Gamma_a-\Gamma_0\rangle.             \tag{0.1}
\]

Thus every resolution receives the scalar score

\[
                         s_a=\langle B,\Gamma_a\rangle,          \tag{0.2}
\]

and a negative move exists exactly when the current score is not minimal.
The sum and squared sum of all derivatives are the first moment and
variance of these scores; they do not force either sign.

This rules out a formal \(M\)-convex conclusion from slab ownership and
image cardinalities alone.  An explicit scalable abstract slab-image
model is constructed below with:

* eight independent \(Q_{R+1}\)-resolution variables;
* exact two-packet image mass \(2^{R+1}\) in every resolution;
* no within-resolution repeat;
* floor energy \(Q=W_{\rm abs}/4=\Omega(W_{\rm abs})\);
* every one-slab move strictly increasing the energy; and
* another simultaneous choice having \(Q=0\).

The trap is the standard frustrated \(Q_3\) overlap holonomy: each target
block rewards opposite choices on one cube edge, while a nonoptimal
cut is one-flip stable.

The countermodel is exact at the owner/image-incidence level, and it may
be decorated with the required resolution direction marginals.  It is
not claimed here to be a literal Johnson/compiler realization.  It proves
that an actual descent theorem must use additional cyclic geometry of the
literal images.  The exact remaining positive statement is:

> Every literal rank-twisted packet factor which is locally minimal for
> all compatible Hamming-two slabs has aggregate floor energy \(o(W)\).

No identity presently proved implies this statement.  A squared-scatter
bound alone is insufficient.

The same score reduction holds for a common weighted sum over all depths
and both signs.  One-depth improving directions can conflict, and the
abstract trap survives by placing its mobile incidence in one typed part
and using private identical incidence in the other parts.

## 1. One slab and one signed depth

Fix a signed depth \(c=(\epsilon,q)\).  Let \(t\) be one compatible
physical \(Q_{R+1}\) slab in the current owner factor.  Its available
states consist of its \(R+1\) facet resolutions, refined if desired by all
certified compiler conjugates on the two packets.  Write this finite state
set as \(A_t\).

For \(a\in A_t\), let

\[
                         \Gamma_{t,a}(T)
  =\mathbf1_{\{T\text{ occurs in resolution }a\}}.  \tag{1.1}
\]

The two packets in one resolution have disjoint trace images because
their frozen facet coordinate remains visible.  Hence

\[
 \Gamma_{t,a}(T)\in\{0,1\},\qquad
 \sum_T\Gamma_{t,a}(T)=2^{R+1}=:m_t.                \tag{1.2}
\]

Let \(a_0\) be the current state and remove its contribution from the
global load:

\[
                         B_t=Z-\Gamma_{t,a_0}.       \tag{1.3}
\]

This background is independent of which replacement state \(a\) is
tested.

Put

\[
                         \Delta_{t,a}
    =\Gamma_{t,a}-\Gamma_{t,a_0}.                   \tag{1.4}
\]

Then

\[
 \sum_T\Delta_{t,a}(T)=0,\qquad
 \Delta_{t,a}(T)\in\{-1,0,1\}.                     \tag{1.5}
\]

## 2. Exact collision and floor-energy derivative

For integral \(B\ge0\) and \(\Gamma\in\{0,1\}^{\mathcal T}\),

\[
                         \binom{B(T)+\Gamma(T)}2
 =\binom{B(T)}2+B(T)\Gamma(T).                      \tag{2.1}
\]

Therefore:

### Theorem 2.1 (slab score formula)

For every alternative state \(a\in A_t\),

\[
 \boxed{
 {\cal C}(B_t+\Gamma_{t,a})
   -{\cal C}(B_t+\Gamma_{t,a_0})
 =\langle B_t,\Delta_{t,a}\rangle.}                \tag{2.2}
\]

If

\[
 Q_c(Z)=\sum_T(Z(T)-c_c)(Z(T)-c_c-1)               \tag{2.3}
\]

is the floor energy at this typed depth, then

\[
 \boxed{
 Q_c(B_t+\Gamma_{t,a})
  -Q_c(B_t+\Gamma_{t,a_0})
 =2\langle B_t,\Delta_{t,a}\rangle.}               \tag{2.4}
\]

#### Proof

Sum (2.1) for the two resolution states and subtract to obtain (2.2).
For (2.4), use

\[
 f(z+1)-f(z)=2(z-c_c),
 \qquad f(z)=(z-c_c)(z-c_c-1).
\]

The \(c_c\)-term cancels because \(\sum_T\Delta_{t,a}(T)=0\).
\(\square\)

Equivalently, using the current total load \(Z\),

\[
 {\cal C}(Z+\Delta_{t,a})-{\cal C}(Z)
 =\langle Z,\Delta_{t,a}\rangle
    +\frac12\|\Delta_{t,a}\|_2^2.                  \tag{2.5}
\]

Indeed

\[
 \langle\Gamma_{t,a_0},\Delta_{t,a}\rangle
   =-\frac12\|\Delta_{t,a}\|_2^2.
\]

Formula (2.2) is cleaner because it absorbs the positive self-cost into
the removal of the old shore.

## 3. Sum and squared-sum identities

Let

\[
 K_t=|A_t|,\qquad
 s_{t,a}=\langle B_t,\Gamma_{t,a}\rangle,\qquad
 \bar s_t={1\over K_t}\sum_{a\in A_t}s_{t,a}.       \tag{3.1}
\]

Write

\[
                         d_{t,a}
  =\langle B_t,\Delta_{t,a}\rangle
  =s_{t,a}-s_{t,a_0}.                               \tag{3.2}
\]

### Theorem 3.1 (resolution first and second moments)

\[
 \boxed{
 \sum_{a\in A_t}d_{t,a}
   =K_t(\bar s_t-s_{t,a_0}).}                       \tag{3.3}
\]

Moreover

\[
 \boxed{
 \sum_{a\in A_t}d_{t,a}^2
  =\sum_{a\in A_t}(s_{t,a}-\bar s_t)^2
     +K_t(s_{t,a_0}-\bar s_t)^2.}                  \tag{3.4}
\]

If all ordered changes \(a\to b\) are included, then

\[
 \boxed{
 \sum_{a,b}(s_{t,b}-s_{t,a})=0,}                   \tag{3.5}
\]

and

\[
 \boxed{
 \sum_{a,b}(s_{t,b}-s_{t,a})^2
   =2K_t\sum_a(s_{t,a}-\bar s_t)^2.}               \tag{3.6}
\]

#### Proof

Equation (3.3) is immediate from (3.2).  Expand

\[
 s_{t,a}-s_{t,a_0}
 =(s_{t,a}-\bar s_t)+(\bar s_t-s_{t,a_0})
\]

and use \(\sum_a(s_{t,a}-\bar s_t)=0\) to get (3.4).
Ordered-pair antisymmetry gives (3.5), and expanding the square gives
(3.6). \(\square\)

In matrix form,

\[
 \sum_a d_{t,a}^2
 =\left\langle B_t,
     \left(\sum_a\Delta_{t,a}\Delta_{t,a}^{\mathsf T}\right)
     B_t\right\rangle.                              \tag{3.7}
\]

The matrix in (3.7) is the literal derivative scatter of the slab.
Large scatter only says that the alternative scores are dispersed.  It
does not say that one lies below the current score.

### Corollary 3.2 (exact local-minimum criterion)

The current resolution is locally minimal for factorial collision energy,
and equivalently for floor energy, if and only if

\[
                         s_{t,a_0}=\min_{a\in A_t}s_{t,a}.       \tag{3.8}
\]

At a local minimum all terms \(d_{t,a}\) are nonnegative.  Their squared
sum may nevertheless be arbitrarily large.

## 4. Why summing over all slabs does not close descent

For a fixed factor, apply (3.3)--(3.4) separately to every compatible
slab \(t\).  The background

\[
                         B_t=Z-\Gamma_{t,a_0}
\]

depends on \(t\), so there is no cancellation between the first moments
unless an additional incidence theorem is proved.

The full move graph is undirected: every resolution change has its
inverse.  Consequently, if one sums energy derivatives over **all
oriented edges of the entire configuration graph**, the sum is zero by
pair cancellation.  This global identity gives no negative outgoing edge
at a specified configuration.

A valid descent theorem would need a statement of the form

\[
 Q(Z)\ge\varepsilon W
 \quad\Longrightarrow\quad
 \exists\,t,a:
    s_{t,a}<s_{t,a_0},                              \tag{4.1}
\]

or quantitatively

\[
 \sum_t\left(s_{t,a_0}-\min_as_{t,a}\right)
   \ge c\,Q(Z)-o(W).                                \tag{4.2}
\]

Neither the owner slab resolution theorem, the direction-marginal IDP,
nor the norm bound
\(\|\Delta_{t,a}\|_1\le4\cdot2^R\) implies (4.1) or (4.2).

## 5. A strict scalable local-minimum countermodel

This section gives an exact packet-image incidence model satisfying the
mass and no-diagonal properties of slab resolutions.  It shows that an
\(M\)-convex local-to-global theorem cannot follow from those properties
alone.

Put

\[
                         s=2^R,\qquad L={s\over2}.   \tag{5.1}
\]

Index eight independent slab variables by the vertices
\(v\in Q_3\).  Every variable has the full \(K=R+1\) resolution labels.
Choose one distinguished current label \(a_v^0\), and define a binary
color map

\[
 \chi_v(a_v^0)=x_0(v),\qquad
 \chi_v(a)=1-x_0(v)\quad(a\ne a_v^0),               \tag{5.2}
\]

where

\[
                         x_0(v)=v_1\oplus v_2.       \tag{5.3}
\]

For every edge \(e=uv\) of \(Q_3\) and \(b\in\{0,1\}\), create a target
block

\[
                         T_{e,b},\qquad |T_{e,b}|=L,              \tag{5.4}
\]

all blocks disjoint.  For every vertex \(v\) and resolution \(a\), also
create a private block

\[
                         P_{v,a},\qquad |P_{v,a}|=L,              \tag{5.5}
\]

disjoint from all other blocks.

Define the aggregate two-packet image of resolution \(a\) at \(v\) by

\[
 I_{v,a}
 =P_{v,a}\ \dot\cup\
   \mathop{\dot\bigcup}_{e\ni v}T_{e,\chi_v(a)}.    \tag{5.6}
\]

Every vertex of \(Q_3\) has degree three, so

\[
                         |I_{v,a}|=L+3L=4L=2s.      \tag{5.7}
\]

Partition \(I_{v,a}\) arbitrarily into two \(s\)-sets.  These are the
two packet images of this abstract slab resolution.  Thus every state has
the correct two-packet image mass and no within-resolution repeat.

### Theorem 5.1 (strict slab trap)

At the current choice \(a_v^0\) for every \(v\):

1. the factorial collision energy is

   \[
                            {\cal C}=4L=2s;
                                                               \tag{5.8}
   \]
2. changing any one slab to any other resolution increases
   \({\cal C}\) by exactly \(L\);
3. the floor energy, with baseline \(c=0\), is

   \[
                            Q=2{\cal C}=4s;
                                                               \tag{5.9}
   \]
4. the total owner mass is

   \[
                            W_{\rm abs}=8(2s)=16s,
                                                               \tag{5.10}
   \]

   so \(Q=W_{\rm abs}/4\); and
5. another simultaneous resolution choice has \({\cal C}=Q=0\).

#### Proof

The private blocks have load one and create no collision.  On a cube edge
\(e=uv\), the shared block \(T_{e,b}\) has load two precisely when
\(x(u)=x(v)=b\).  Hence

\[
             {\cal C}(x)
       =L\,|\{uv\in E(Q_3):x(u)=x(v)\}|.            \tag{5.11}
\]

For \(x_0(v)=v_1\oplus v_2\), exactly the four direction-three edges are
monochromatic, proving (5.8).

Every vertex is incident with one monochromatic edge and two bichromatic
edges.  Flipping its color destroys one collision block and creates two,
so the energy rises by \(L\).  By (5.2), every alternative resolution
flips that color.  This proves strict local minimality.

Since the target catalogue includes all private option blocks, its size
exceeds the occurrence mass, so the balanced collision baseline is zero
and \(Q=2{\cal C}\).  Equations (5.9)--(5.10) follow.

Finally choose colors

\[
                         x_\ast(v)=v_1\oplus v_2\oplus v_3.
\]

Every cube edge is then bichromatic.  At vertices with \(v_3=0\), keep
the current resolution; at vertices with \(v_3=1\), choose any alternative
resolution.  Equation (5.11) gives zero collision energy. \(\square\)

### Derivative sums in the trap

Every slab has \(K-1=R\) alternatives, all with derivative \(L\).  Hence
at the bad state

\[
 \sum_{v}\sum_{a\ne a_v^0}
   \langle B_v,\Delta_{v,a}\rangle
       =8RL,                                        \tag{5.12}
\]

while

\[
 \sum_{v}\sum_{a\ne a_v^0}
   \langle B_v,\Delta_{v,a}\rangle^2
       =8RL^2.                                      \tag{5.13}
\]

Both are large and positive.  In particular, a lower bound on the
squared derivative sum is compatible with a strict bad local minimum.

## 6. Direction-marginal compatibility of the countermodel

At depth one, a genuine resolution inactive in direction \(j\) has
occurrence-direction vector

\[
                         2g_R(\mathbf1-e_j).
                                                               \tag{6.1}
\]

The abstract target blocks in Section 5 carry target identities, while a
direction is a label on an **occurrence**.  A shared target may be reached
by different Johnson directions in different packets.  Therefore the
occurrences of every \(I_{v,a}\) can be assigned direction labels
independently so that (6.1) holds: split its \(2s\) incidences equally,
\(2g_R\) to every active direction and zero to the inactive direction.

This decoration preserves every target load and every energy calculation.
Likewise, at depth \(q<R\), assign the audited support-incidence marginal
\(2qg_R\) to each active direction.  Thus even exact normalized
hypersimplex direction data do not rule out the incidence trap.

This remains an abstract incidence decoration, not a proof that the
blocks (5.4)--(5.6) arise as literal traces of the parity-complete
compiler.

## 7. Common all-depth weighted energy

Let \(c\) range over all signed depths and let \(w_c\ge0\).  For one slab
state \(a\), put

\[
 s_{t,a}^{\rm all}
   =\sum_cw_c\langle B_{t,c},\Gamma_{t,a,c}\rangle. \tag{7.1}
\]

The aggregate floor-energy derivative is

\[
 \boxed{
 Q_{\rm all}(a)-Q_{\rm all}(a_0)
   =2\bigl(s_{t,a}^{\rm all}-s_{t,a_0}^{\rm all}\bigr).}
                                                               \tag{7.2}
\]

Hence Theorems 3.1 and Corollary 3.2 apply verbatim with the all-depth
scores (7.1).

An improving move at one depth need not improve (7.2), because the same
resolution controls every typed part.  Conversely, the countermodel of
Section 5 can be placed in one signed depth, while all other typed images
are made private and state-dependent with no intersections.  Those other
parts contribute zero energy and zero derivative.  The strict local trap
therefore persists for the common weighted objective.

For the actual compiler, images at different depths cannot be specified
independently in this way.  A positive theorem must exploit that common
chronology.  The present packet theorem supplies injectivity but no
cross-depth sign-coherence identity for the derivatives.

## 8. Actual literal boundary

The abstract trap proves the following negative statement rigorously:

> Exact ownership, the full \(R+1\) resolution menu, equal image mass,
> within-resolution injectivity, exact direction marginals, and large
> derivative scatter do not imply a negative-energy Hamming-two slab
> move.

It does **not** prove that the literal rank-twisted diverse-order compiler
has a bad local minimum.  Literal cyclic geometry could in principle
exclude the \(Q_3\) overlap holonomy.

The exact actual gate is a local-minimum theorem using that geometry:

\[
 \boxed{
 \begin{gathered}
 \langle B_{t,c},\Gamma_{t,a,c}-\Gamma_{t,a_0,c}\rangle
 \ge0
 \quad\text{for every compatible slab state }(t,a),\\
 \text{simultaneously over the weighted signed depths}
 \quad\Longrightarrow\quad
 Q_{\rm all}=o(W).
 \end{gathered}}                                   \tag{8.1}
\]

Equivalently, one may prove the quantitative deficit inequality (4.2).
That theorem requires an actual literal derivative Gram or a
cycle-geometric exclusion of frustrated overlap clauses.  No such result
is presently available.

## 9. Audited boundary

Proved:

* exact one-depth collision and floor-energy score derivatives;
* exact first- and second-moment identities over all slab resolutions;
* exact characterization of slab-local minima;
* an explicit scalable strict local-minimum countermodel with
  \(Q=\Omega(W_{\rm abs})\) and a zero-energy global state;
* compatibility of that countermodel with the normalized direction
  marginals; and
* the common all-depth weighted score reduction.

Not proved:

* literal realization of the countermodel by the diverse-order compiler;
* a bad local minimum in the actual rank-twisted atlas; or
* the positive literal local-minimum theorem (8.1).

The collision-energy problem is therefore not \(M\)-convex at the level
of the presently proved slab axioms.  The surviving issue is a literal
cyclic-geometry theorem, not another derivative-sum calculation.
