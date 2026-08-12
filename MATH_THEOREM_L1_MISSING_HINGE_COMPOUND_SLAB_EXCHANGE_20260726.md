# The exact \(L^1\) missing hinge under compound cross-parent slab exchanges

Date: 2026-07-26

Method: pure mathematics only. No computation, search, solver, or web input is
used.

## 0. Outcome

The authoritative constant-one target is the missing-shadow hinge

\[
 \mathfrak H
 =\sum_{q\le H,\epsilon,T}(1-L_q^\epsilon(T))_+,      \tag{0.1}
\]

or, equivalently,

\[
 \mathfrak X
 =\sum_{q,\epsilon}\left[
   \sum_T(L_q^\epsilon(T)-1)_+-(G-N_q)_+\right].      \tag{0.2}
\]

The forced deficit
\(\sum_{q,\epsilon}(N_q-G)_+=o(W)\) is already available, so
\(\mathfrak H=o(W)\) and \(\mathfrak X=o(W)\) are equivalent.

For cross-parent slab optimization the exact conclusions are as follows.

1. **One slab.** Remove the current two-packet slab shore and call the
   remaining load \(B_t\).  Put

   \[
   Z_t=\{T:B_t(T)=0\},\qquad
   u_{t,a}=|Z_t\cap I_{t,a}|.
   \]

   Then

   \[
   \boxed{
   \mathfrak H(B_t+\Gamma_{t,a})
    -\mathfrak H(B_t+\Gamma_{t,a_0})
   =u_{t,a_0}-u_{t,a}.}                              \tag{0.3}
   \]

   The same formula holds for repeat excess.  A state is one-slab locally
   minimal exactly when its current shore maximizes newly covered
   background zeros in every slab.

2. **Compound exchange.** For a simultaneously legal slab family \(S\),
   remove all its current shores.  Let \(Z_S\) be the zero set of the
   remaining background, and let \(U_S^0,U_S^1\) be the unions of the old
   and new slab images.  Then

   \[
   \boxed{
   \Delta_S\mathfrak H
   =|Z_S\cap U_S^0|-|Z_S\cap U_S^1|.}                \tag{0.4}
   \]

   Thus a compound exchange improves precisely when its new shores cover
   more of the common background-zero set.

3. **Residue form.** If

   \[
   R_c(S)=\sum_{t\in S}\Delta_{t,c},\qquad L_c'=L_c+R_c(S),
   \]

   then

   \[
   \boxed{
   \Delta_S\mathfrak H_c
    =|\{T:L_c(T)>0,\ R_c(T)=-L_c(T)\}|
      -|\{T:L_c(T)=0,\ R_c(T)>0\}|.}                \tag{0.5}
   \]

   Hence the hinge derivative depends only on the final literal residue,
   not on its decomposition into slabs.  It counts newly created holes
   minus filled old holes and ignores every other multiplicity change.

4. **No pairwise covariance formula.** The union score in (0.4) has the
   exact inclusion--exclusion expansion

   \[
   |Z_S\cap U_S^\sigma|
   =\sum_{\varnothing\ne J\subseteq S}
       (-1)^{|J|+1}
       \left|Z_S\cap\bigcap_{t\in J}I_{t}^{\sigma}\right|.
                                                               \tag{0.6}
   \]

   Thus the \(L^1\) analogue of overlap holonomy contains interactions of
   every order.  Pair moments \(E[X_tX_u]\), sufficient to describe the
   quadratic CPCR objective, do not determine expected missing mass.

5. **The local-minimum obstruction persists.** There is a scalable exact
   abstract slab-image model with

   \[
   G=N,\qquad
   \mathfrak H=\mathfrak X=\Omega(W_{\rm abs}),       \tag{0.7}
   \]

   in which every one-slab move strictly increases both objectives, while
   a four-slab correlated exchange makes them zero.  It is the same
   frustrated \(Q_3\) overlap holonomy, with state-independent private
   blocks.  It satisfies equal shore mass, within-shore injectivity, and
   the audited direction marginals.  As before, it is an abstract
   incidence model, not a literal diverse-order compiler realization.

6. **No generic submodular-flow reduction.** Coverage is a monotone
   submodular function of a freely chosen collection of option sets, but
   the legal problem maximizes that function subject to choosing exactly
   one complete option per slab.  Equivalently, missing mass is
   supermodular on the unrestricted option ground set.  On relative slab
   flip variables, where a move removes an old shore and adds a new one,
   the objective is generally neither submodular nor supermodular.  The
   \(Q_3\) trap has the pair potential

   \[
   \psi(0,0)=\psi(1,1)=L,\qquad
   \psi(0,1)=\psi(1,0)=0,                           \tag{0.8}
   \]

   which violates the graph-cut submodularity inequality.

The weaker target therefore removes CPCR's unnecessary overload and
quadratic penalties, but it does not turn cross-parent resolution into a
network flow.  The exact surviving theorem is a common all-depth
near-cover by compound legal slab/compiler states, or a literal geometric
theorem excluding frustrated union holonomy in the actual compiler atlas.

## 1. Exact missing/repeat ledger

Fix one signed depth \(c=(q,\epsilon)\).  Let

\[
 L_c(T)\in\mathbb Z_{\ge0},\qquad
 \sum_TL_c(T)=G,\qquad |\mathcal T_c|=N_c.           \tag{1.1}
\]

Define

\[
 H_c(L)=\sum_T(1-L_c(T))_+
       =|\{T:L_c(T)=0\}|,                            \tag{1.2}
\]

and

\[
 E_c(L)=\sum_T(L_c(T)-1)_+.                         \tag{1.3}
\]

Since the positive coordinates contribute one support unit and then
\(E_c\) repeat units,

\[
 \boxed{H_c(L)=N_c-G+E_c(L).}                       \tag{1.4}
\]

Put

\[
 X_c(L)=E_c(L)-(G-N_c)_+,\qquad
 F_c=(N_c-G)_+.
\]

Then

\[
 \boxed{H_c(L)=F_c+X_c(L).}                         \tag{1.5}
\]

The quantity \(F_c\) is state-independent.  Therefore every legal slab or
compiler exchange has

\[
 \boxed{\Delta H_c=\Delta E_c=\Delta X_c.}          \tag{1.6}
\]

This equality uses the full linear repeat hinge.  A capped overload
functional would not obey it.

## 2. Exact one-slab derivative

Let \(t\) be one compatible \(Q_{R+1}\)-slab.  Its current state is
\(a_0\), and an alternative state is \(a\).  At the fixed signed depth,
write

\[
 \Gamma_{t,a}(T)={\bf1}_{\{T\in I_{t,a}\}},
 \qquad
 |\operatorname {supp}\Gamma_{t,a}|=2s.             \tag{2.1}
\]

Remove the current shore:

\[
 B_t=L-\Gamma_{t,a_0}.                              \tag{2.2}
\]

Because the current shore is actually present, \(B_t\ge0\).  Put

\[
 Z_t=\{T:B_t(T)=0\}.                                \tag{2.3}
\]

For any replacement shore,

\[
 H_c(B_t+\Gamma_{t,a})
 =|\{T:B_t(T)=0,\ \Gamma_{t,a}(T)=0\}|
 =|Z_t|-|Z_t\cap I_{t,a}|.                          \tag{2.4}
\]

### Theorem 2.1 (one-slab hinge score)

\[
\boxed{
 H_c(B_t+\Gamma_{t,a})-H_c(B_t+\Gamma_{t,a_0})
 =\langle{\bf1}_{Z_t},\Gamma_{t,a_0}-\Gamma_{t,a}\rangle.}
                                                               \tag{2.5}
\]

Equivalently, with

\[
 u_{t,a}=|Z_t\cap I_{t,a}|,
\]

the change is \(u_{t,a_0}-u_{t,a}\).  By (1.6), the identical formula
holds for \(E_c\) and \(X_c\).

For the common all-depth objective, use

\[
 u_{t,a}^{\rm all}
 =\sum_{q\le H,\epsilon}
    |Z_{t,q}^\epsilon\cap I_{t,a,q}^\epsilon|.       \tag{2.6}
\]

The same one slab state \(a\) occurs in every summand, and

\[
 \Delta_a\mathfrak H
 =u_{t,a_0}^{\rm all}-u_{t,a}^{\rm all}.            \tag{2.7}
\]

### Corollary 2.2 (one-slab local-minimum criterion)

A legal resolution state is locally minimal under all one-slab changes if
and only if, for every compatible slab \(t\),

\[
 u_{t,a_0}^{\rm all}=\max_{a\in A_t}u_{t,a}^{\rm all}.           \tag{2.8}
\]

Neither equal image mass, direction-marginal balance, nor a large scatter
of the scores \(u_{t,a}\) implies that a positive-energy state violates
(2.8).

## 3. Exact compound derivative

Let \(S\) be a simultaneously legal family of pairwise owner-disjoint
slabs, with one chosen alternative state for every \(t\in S\).  Remove all
their current shores:

\[
 B_S=L-\sum_{t\in S}\Gamma_{t,a_t^0}\ge0.            \tag{3.1}
\]

Put

\[
 Z_S=\{T:B_S(T)=0\},\qquad
 U_S^0=\bigcup_{t\in S}I_{t,a_t^0},\qquad
 U_S^1=\bigcup_{t\in S}I_{t,a_t^1}.                 \tag{3.2}
\]

Although the slabs are owner-disjoint, their target images may overlap.
The old and new loads are

\[
 L^0=B_S+\sum_{t\in S}\Gamma_{t,a_t^0},\qquad
 L^1=B_S+\sum_{t\in S}\Gamma_{t,a_t^1}.              \tag{3.3}
\]

A target is missing precisely when it lies in \(Z_S\) and outside the
corresponding union.  Therefore:

### Theorem 3.1 (compound union-score formula)

\[
\boxed{
 H_c(L^1)-H_c(L^0)
 =|Z_S\cap U_S^0|-|Z_S\cap U_S^1|.}                 \tag{3.4}
\]

The same formula holds for repeat excess \(X_c\).

For all signed depths,

\[
 \boxed{
 \Delta_S\mathfrak H
 =\sum_{q\le H,\epsilon}
    \left(
      |Z_{S,q}^\epsilon\cap U_{S,q}^{0,\epsilon}|
      -|Z_{S,q}^\epsilon\cap U_{S,q}^{1,\epsilon}|
    \right).}                                       \tag{3.5}
\]

Thus compound descent is an exact common-background maximum-union problem.
The background \(Z_S\) depends on the entire exchanged family, so the
one-slab scores in Section 2 do not add.

### Inclusion--exclusion holonomy

For either shore \(\sigma\in\{0,1\}\),

\[
 |Z_S\cap U_S^\sigma|
 =\sum_{\varnothing\ne J\subseteq S}
    (-1)^{|J|+1}
    \left|Z_S\cap\bigcap_{t\in J}I_{t,a_t^\sigma}\right|.       \tag{3.6}
\]

The singleton terms are the direct slab scores relative to the common
background.  Intersections with \(|J|\ge2\) are the exact \(L^1\)
overlap holonomy.  Unlike the quadratic CPCR objective, it does not stop at
pairs.

## 4. Literal residue form and invariants

Define

\[
 \Delta_{t,c}
 =\Gamma_{t,a_t^1,c}-\Gamma_{t,a_t^0,c},
 \qquad
 R_c(S)=\sum_{t\in S}\Delta_{t,c}.                 \tag{4.1}
\]

Then \(L_c^1=L_c^0+R_c(S)\), and

\[
 \sum_TR_c(S;T)=0.                                  \tag{4.2}
\]

Because both the old and new loads are nonnegative integers:

### Theorem 4.1 (threshold-crossing residue formula)

\[
\boxed{
\begin{aligned}
 H_c(L_c+R_c)-H_c(L_c)
  &=|\{T:L_c(T)>0,\ R_c(T)=-L_c(T)\}|\\
  &\quad-|\{T:L_c(T)=0,\ R_c(T)>0\}|.
\end{aligned}}                                      \tag{4.3}
\]

#### Proof

At an old hole \(L_c(T)=0\), nonnegativity gives \(R_c(T)\ge0\); the hole
is filled exactly when \(R_c(T)>0\).  At an old covered target, a new hole
is created exactly when \(L_c(T)+R_c(T)=0\), or
\(R_c(T)=-L_c(T)\).  Every other target has the same missing indicator.
\(\square\)

Consequently:

* the hinge derivative depends only on the literal residue \(R_c(S)\);
* two compound decompositions with the same residue have the same cost;
* overload redistribution which crosses neither threshold is invisible;
* a residue \(R=0\) changes neither missing mass nor repeat excess.

The cross-parent slab direction derivative remains

\[
 \Pi_q^\epsilon R_q^\epsilon(S)
 =2qg_RB{\bf1}_S.                                   \tag{4.4}
\]

Hence every compound residue obeys

\[
 {1\over q}\Pi_q^-R_q^-
 ={1\over q}\Pi_q^+R_q^+
 =2g_RB{\bf1}_S,                                    \tag{4.5}
\]

and the normalized value is common to every protected depth.  A closed
axis circulation lies in the same direct-sum hard kernel

\[
 \mathcal K_{\rm lit}
 =\bigoplus_{q\le H,\epsilon=\pm}\ker\Pi_q^\epsilon. \tag{4.6}
\]

The weaker objective changes what must be controlled inside this kernel:
only zero-to-positive and positive-to-zero threshold crossings matter.

## 5. Fractional laws require all-order avoidance data

Let \(\mu\) be a joint distribution on legal complete slab/compiler states.
For a fixed target \(T\),

\[
 \mathbb E_\mu{\bf1}_{\{L(T)=0\}}
 =\Pr_\mu\{\text{no selected packet image contains }T\}.        \tag{5.1}
\]

If the choice groups are independent and

\[
 p_t(T)=\Pr(T\in I_{t,X_t}),
\]

then

\[
 \boxed{
 \mathbb E_\mu\mathfrak H
 =\sum_{c,T}\prod_t(1-p_{t,c}(T)).}                \tag{5.2}
\]

For a general correlated law, inclusion--exclusion gives

\[
 \Pr_\mu(L(T)=0)
 =1+\sum_{\varnothing\ne J}
    (-1)^{|J|}
    \Pr_\mu\{T\in I_{t,X_t}\text{ for every }t\in J\}.           \tag{5.3}
\]

Thus first moments do not determine the objective, and pair moments do not
determine it when a target can be supplied by three or more choice groups.
The correct fractional object is the full avoidance law, or a structural
bounded-overlap theorem reducing (5.3) to low order.

Conditional expectation still gives zero rounding gap once a legal joint
or product distribution with \(o(W)\) expected missing mass is constructed.
It does not construct the avoidance law.

## 6. The \(L^1\) Hamming-two local-minimum trap

The collision trap can be sharpened so that missing mass itself, not a
quadratic surrogate, is trapped.

Put

\[
 s=2^R,\qquad L={s\over2}.
\]

Index eight slab variables by \(v\in Q_3\).  Let

\[
 x_0(v)=v_1\oplus v_2.                              \tag{6.1}
\]

Every slab has its full resolution menu.  Map the current label at \(v\)
to color \(x_0(v)\), and every alternative label to color \(1-x_0(v)\).

For every cube edge \(e=uv\) and \(b\in\{0,1\}\), create a target block

\[
 T_{e,b},\qquad |T_{e,b}|=L,                        \tag{6.2}
\]

all disjoint.  For every vertex \(v\), create one state-independent private
block

\[
 P_v,\qquad |P_v|=L,                                \tag{6.3}
\]

disjoint from all shared blocks and other private blocks.  Define

\[
 I_{v,a}
 =P_v\ \dot\cup\
   \mathop{\dot\bigcup}_{e\ni v}T_{e,\chi_v(a)}.     \tag{6.4}
\]

Every image has size

\[
 |I_{v,a}|=4L=2s,                                   \tag{6.5}
\]

and may be partitioned arbitrarily into two disjoint \(s\)-packet images.
The target universe and occurrence mass are both

\[
 N=(8+2|E(Q_3)|)L=32L,\qquad
 G=8(4L)=32L.                                       \tag{6.6}
\]

For a color assignment \(x\), each private block has load one.  On one
cube edge:

* if its endpoint colors differ, both target blocks have load one;
* if its endpoint colors agree, one block has load two and the other load
  zero.

Therefore

\[
 \boxed{
 H(x)=E(x)=X(x)
 =L\,|\{uv\in E(Q_3):x(u)=x(v)\}|.}                 \tag{6.7}
\]

At \(x_0\), exactly the four direction-three edges are monochromatic, so

\[
                         H(x_0)=4L=\Omega(G).        \tag{6.8}
\]

Every vertex is incident with one monochromatic and two bichromatic edges.
Flipping one slab destroys one hole block and creates two, so

\[
                         \Delta H=+L.               \tag{6.9}
\]

Thus the state is a strict one-slab local minimum.

Now flip exactly the four vertices with \(v_3=1\).  The resulting coloring

\[
 x_\ast(v)=v_1\oplus v_2\oplus v_3
\]

is proper on every cube edge, and

\[
                         H(x_\ast)=E(x_\ast)=0.      \tag{6.10}
\]

This proves the claimed compound escape.  As in the quadratic audit, the
occurrences can be decorated with the exact inactive-direction and
depth-\(q\) support marginals without changing target loads.

If a ratio \(G>N\) is desired, append state-independent packet occurrences
on already covered target blocks.  Each appended occurrence increases
\(E\) and \(G-N\) by the same amount, while \(H\) and \(X\) remain
unchanged.  Hence the repeat-excess trap persists in the protected
\(G>N\) normalization.

The construction is an exact packet-image-incidence countermodel.  It is
not asserted to arise from the literal diverse-order compiler chronology.

## 7. Submodularity and flow audit

Let the option ground set be

\[
 \mathcal U=\{(t,a):t\text{ a slab and }a\in A_t\},
\]

and define coverage

\[
 F(S)=\left|\bigcup_{(t,a)\in S}I_{t,a}\right|.       \tag{7.1}
\]

On unrestricted subsets of \(\mathcal U\), \(F\) is monotone submodular.
But a legal state must choose exactly one option from every slab and must
respect slab-packing compatibility.  The desired problem is to maximize
\(F\) on this constrained family.  Equivalently,

\[
 H=N-F
\]

is supermodular on unrestricted option subsets and is being minimized on
the same constrained family.  This is not submodular minimization.

If one instead parametrizes a neighborhood of a current state by the set
of slabs which are flipped, every flip simultaneously removes an old
image and adds a new one.  The resulting set function can be neither
submodular nor supermodular.

The \(Q_3\) trap already gives an exact pairwise obstruction.  One shared
edge block contributes

\[
 \psi(0,0)=\psi(1,1)=L,\qquad
 \psi(0,1)=\psi(1,0)=0.                             \tag{7.2}
\]

For graph-cut minimization, binary submodularity requires

\[
 \psi(0,0)+\psi(1,1)
 \le\psi(0,1)+\psi(1,0).                            \tag{7.3}
\]

Here the two sides are \(2L\) and \(0\).  Thus the hinge objective contains
an antiferromagnetic, non-submodular interaction.  On a general overlap
graph, minimizing these terms is the complementary maximum-cut problem,
not a minimum-cost flow.

There are simple one-target witnesses showing that flip-set missing mass
can also violate either curvature sign:

* if a target is covered only when at least one of two slabs is flipped,
  its missing indicator is one only at \((x_1,x_2)=(0,0)\), which violates
  submodularity;
* if slab \(1\) covers the target exactly when \(x_1=0\), while slab
  \(2\) covers it exactly when \(x_2=1\), its missing indicator is one
  only at \((x_1,x_2)=(1,0)\), which violates supermodularity.

Together they rule out a uniform submodular or supermodular flip model.

## 8. Exact surviving \(L^1\) theorem

The weaker objective changes the global gate from floor covariance to
literal union coverage:

> Choose one common all-depth legal packet/slab/compiler state such that
> the union of its signed target images misses only \(o(W)\) targets in
> aggregate.

The slab primitive supplies legal cross-parent changes, and formulas
(3.4) and (4.3) give their exact compound effect.  What remains is one of:

1. an abundant compound-exchange theorem which covers more common
   background zeros than it uncovers, through all depths and both signs;
2. a literal compiler-geometric theorem excluding positive-density
   frustrated union holonomy;
3. a construction of a legal joint avoidance law with
   \(\sum_{c,T}\Pr(L_c(T)=0)=o(W)\); or
4. a structural bounded-overlap theorem reducing the all-order expansion
   (5.3) to a controllable low-order system.

The one-slab local-minimum route is false at the level of the proved slab
axioms, and the \(L^1\) weakening does not reveal a generic
submodular-flow structure.

## 9. Exact grouped-Hall successor

MATH_THEOREM_L1_RECAST_CROSS_PROFILE_PACKET_UNION_AND_GROUPED_HALL_20260726.md
gives an equivalent grouped formulation of the surviving near-cover
problem. For an owner-disjoint compound choice-group catalogue, the
minimum integral hole count equals the minimum product avoidance
functional

\[
 \sum_{c,T}\prod_g(1-p_{g,c}(T)).
\]

It also proves that the natural grouped rank inequalities

\[
 |A|\le\sum_g\max_{\omega}|A\cap I_{g,\omega}|
\]

are not sufficient: a tensorable two-group, four-target option catalogue
satisfies every such cut and exact mean-one marginals, but every state
has one hole and one repeat. If the feasible bundle systems were
matroids, the same rank inequalities would become sufficient by the
proved matroid-union formula. The physical alternatives are therefore
compound-exchange closure, direct homing, a correlated avoidance law, or
a geometric exclusion of the alternating grouped minor.
