# The projective Room atlas: exact cocycle and mandatory curvature

Date: 2026-07-27

Method: pure mathematics.  No finite search is used.

## 0. Outcome

Let

\[
 \Omega=[2r-1],\qquad \mathcal U=\binom{\Omega}{r+1},
 \qquad P=\mathbb P^1(\mathbb F_r),\qquad C=\mathbb F_r,
\]

where `r` is a prime power, and let

\[
 Q:\{(u,v)\in P^2:u\ne v\}\longrightarrow C
\]

be the locally perfect finite-field chart from
`LOCALLY_ORTHOGONAL_FACTORIZATION_PROJECTIVE_ATLAS_20260727.md`.

For each `A in U`, choose a point chart `theta_A:A->P` and a colour gauge
`gamma_A in Sym(C)`, and set

\[
 q_A(a,b)=\gamma_AQ(\theta_A(a),\theta_A(b)).
\tag{0.1}
\]

Every chart in isolation has `Delta_A=0`.  The global overlap condition is
equivalent to one exact statement:

> The row-transport permutations on the Johnson graph `J(2r-1,r+1)` form
> an `S_r`-valued coboundary.

This eliminates all colour gauges from the construction problem.  The
cycle constraints need only be checked on two local configurations:

1. top triangles contained in an `(r+2)`-set;
2. commuting exchange squares contained in an `(r+3)`-set.

Triangles whose charts share one common `r`-set are automatically flat.

There is also a genuine cohomological obstruction.  The point-chart
connection cannot be flat: a flat connection would develop to one global
injection

\[
 \Omega\hookrightarrow P,
\]

impossible because `2r-1>r+1`.  Thus any successful construction must carry
nontrivial coordinate holonomy, and the row transports of `Q` must cancel
it exactly.  On every elementary top triangle or exchange square the
coordinate holonomy is either the identity or one transposition.  The
missing algebraic datum is therefore a **binary curvature field**, not a
new large matching problem.

This rules out every globally labelled, affine-normalized, or flat
Möbius/projective ansatz.  It reduces the positive problem to one finite
`(r+2)`-point identity plus one `(r+3)`-point commuting identity.

## 1. Punctured row maps

For `u in P`, write

\[
 R_u:P\setminus\{u\}\longrightarrow C,
 \qquad R_u(v)=Q(u,v).
\tag{1.1}
\]

The finite-field chart theorem says that every `R_u` is a bijection.

Two chart vertices `A,A' in U` are adjacent when

\[
 Y=A\cap A',\qquad |Y|=r.
\]

Write

\[
 a=A\setminus A',\qquad a'=A'\setminus A.
\]

There is a unique permutation

\[
 \tau_{A,A'}\in\operatorname{Sym}(P)
\tag{1.2}
\]

such that

\[
 \tau_{A,A'}(\theta_A(x))=\theta_{A'}(x)quad(x\in Y),
 \qquad
 \tau_{A,A'}(\theta_A(a))=\theta_{A'}(a').
\tag{1.3}
\]

The first `r` equations determine the map on all but one point of `P`, and
the last equation supplies the missing image.  Clearly

\[
 \tau_{A',A}=\tau_{A,A'}^{-1}.
\tag{1.4}
\]

Define the **row transport** on the oriented edge `A->A'` by

\[
 h_{A,A'}
 :=R_{\theta_{A'}(a')}\circ
   \tau_{A,A'}\circ
   R_{\theta_A(a)}^{-1}
 \in\operatorname{Sym}(C).
\tag{1.5}
\]

The middle expression in (1.5) is restricted from
`P-{theta_A(a)}` to `P-{theta_A'(a')}`, as it should be.

## 2. Exact cocycle theorem

### Theorem 2.1 (colour gauges are exactly a trivialization of `h`)

The locally perfect charts (0.1) satisfy the global overlap condition if
and only if

\[
 \boxed{h_{A,A'}=\gamma_{A'}^{-1}\gamma_A}
\tag{2.1}
\]

for every adjacent pair `A,A'`.

Consequently, point charts `(theta_A)` admit colour gauges `(gamma_A)` if
and only if, for every closed walk

\[
 A_0,A_1,\ldots,A_t=A_0
\]

in `J(2r-1,r+1)`,

\[
 \boxed{
 h_{A_{t-1},A_t}\cdots h_{A_1,A_2}h_{A_0,A_1}=1.}
\tag{2.2}
\]

#### Proof

For `b in Y`, the overlap equation is

\[
 \gamma_A R_{\theta_A(a)}(\theta_A(b))
 =
 \gamma_{A'}R_{\theta_{A'}(a')}(\theta_{A'}(b)).
\]

Use (1.3), then let `b` range over all of `Y`.  The source row is a
bijection onto `C`, so the displayed identity is equivalent to

\[
 \gamma_A=\gamma_{A'}h_{A,A'},
\]

which is (2.1).

If gauges exist, multiplying (2.1) around a closed walk telescopes and gives
(2.2).  Conversely, fix a base chart `A_0` and a value of `gamma_A0`.  For
any `A`, define `gamma_A` by transporting along a path from `A_0` to `A`.
Condition (2.2) makes the result path-independent, and (2.1) then holds on
every edge. \(\square\)

Thus the global construction is no longer a simultaneous system involving
all the colour gauges.  Choose only the point charts; compute `h` by (1.5);
prove that `h` is flat.

## 3. A local cycle basis

Put `k=r+1`.  The vertices of the chart graph are the `k`-subsets of
`Omega`, and an edge is one basis exchange.

There are three elementary closed walks.

1. **Star triangle:** `A_i=Y+a_i`, where `|Y|=k-1` and the three `a_i`
   are distinct.
2. **Top triangle:** `A_i=B-a_i`, where `|B|=k+1` and the three `a_i`
   are distinct.
3. **Exchange square:** perform two exchanges with disjoint removed and
   inserted elements in either order.

### Lemma 3.1 (basis-exchange homotopy)

After attaching a 2-cell along every star triangle, top triangle, and
exchange square, the basis graph of the uniform matroid is simply connected.
Equivalently, a group-valued edge labelling has trivial holonomy on every
closed walk if and only if it has trivial holonomy on these elementary
triangles and squares.

#### Proof

Write a path as a word of single-element exchanges.  Two exchanges with
disjoint removed and inserted elements commute across an exchange square.
Two consecutive exchanges sharing a removed or inserted element can be
replaced by the third side of a star or top triangle.  Given a closed word,
commute the exchange which first inserts a chosen element until it is next
to the exchange which removes that element, using squares; if an exchange
shares an endpoint, shorten across a triangle first.  Cancel the resulting
backtrack.  Induction on the length reduces every closed word to the empty
word. \(\square\)

### Lemma 3.2 (star triangles are automatically flat)

For every choice of point charts, the row transports have trivial holonomy
on every star triangle.

#### Proof

Let the three charts be `A_i=Y+a_i`.  On the edge `A_i->A_j`, the source
row is centred at `a_i` and the target row at `a_j`.  Hence at the
intermediate chart the target row of one edge is exactly the source row of
the next edge.  The row maps in (1.5) telescope.  The coordinate
transitions also telescope: their product fixes the `r` labels of the
common physical set `Y` and carries the successive missing label around
`a_1->a_2->a_3->a_1`.  It is therefore the identity on all `r+1` labels.
Thus the product of the three `h`'s is the identity. \(\square\)

### Corollary 3.3 (smallest exact gluing gate)

It is necessary and sufficient to verify (2.2) only for

* top triangles on `r+2` physical points, and
* exchange squares on `r+3` physical points.

In particular, the first nontrivial condition is finite and local; no
global Hamiltonicity or matching theorem occurs in it.

For a top triangle inside `B in binom(Omega,r+2)`, write

\[
 A_i=B\setminus\{i\}.
\]

For distinct `i,j,k in B`, its exact equation is

\[
 \boxed{h_{A_k,A_i}h_{A_j,A_k}h_{A_i,A_j}=1,}
\tag{3.1}
\]

where every factor is the explicit punctured-row permutation (1.5).  This
is the `(r+2)`-point patch equation.

## 4. Mandatory coordinate curvature

The point transitions `(tau_A,A')` themselves form an
`S_(r+1)`-connection on the chart graph.  Unlike `h`, this connection cannot
be flat.

### Theorem 4.1 (no flat point atlas)

For `r>2`, every family of point charts `theta_A:A->P` has nontrivial
coordinate holonomy on some closed walk of `J(2r-1,r+1)`.  Hence it has
nontrivial holonomy on some elementary top triangle or exchange square.

On either elementary configuration, the nontrivial holonomy is a single
transposition.

#### Proof

Suppose every coordinate holonomy were trivial.  Fix a base chart and
parallel-transport every chart back to it.  Trivial holonomy makes the
transport path-independent.  If a physical point `x` lies in two charts,
the transported value of `theta_A(x)` is the same, since a path inside the
connected family of charts containing `x` compares that same point on every
overlap.  We obtain a global map

\[
 \theta:\Omega\longrightarrow P.
\]

Any two points of `Omega` lie together in some `(r+1)`-set, and that chart
is injective.  Therefore `theta` is globally injective.  This is impossible,
because

\[
 |\Omega|=2r-1>r+1=|P|.
\]

Lemma 3.1 now supplies an elementary configuration with nontrivial
holonomy.  A top triangle or exchange square has a common physical
intersection of size `r-1`.  Its coordinate holonomy fixes the labels of
all those points.  A permutation of `r+1` labels fixing `r-1` labels is
either the identity or the transposition of the remaining two. \(\square\)

This is the decisive difference between ordinary chart gluing and the
present problem:

\[
 \boxed{
 \text{coordinate connection curved}
 \quad+\quad
 \text{row-transport connection flat}.}
\tag{4.1}
\]

The nonlinear row maps of `Q` must cancel a nonzero binary curvature field.

## 5. Exact parity shadow

Taking signs in (2.2) gives a necessary `F_2` cocycle equation.  For every
oriented chart edge put

\[
 \epsilon(A,A')=\operatorname{sgn}(h_{A,A'})\in\{\pm1\}.
\tag{5.1}
\]

Then a necessary condition for gluing is

\[
 \prod_{e\in C}\epsilon(e)=+1
\tag{5.2}
\]

on every top triangle and exchange square.  Conversely, (5.2) is exactly
the obstruction to trivializing the **sign projection** of the colour
connection.  It does not imply the full `S_r` equation, but it is the first
rigorous test for any proposed formula.

In terms of (1.5), each factor is explicitly

\[
 \epsilon(A,A')
 =\operatorname{sgn}
 \left(
 R_{\theta_{A'}(a')}\tau_{A,A'}R_{\theta_A(a)}^{-1}
 \right).
\tag{5.3}
\]

Thus a candidate atlas which fails one parity check is impossible before
any higher permutation calculation is attempted.

## 6. Candidate classes ruled out

### Proposition 6.1 (no globally labelled restriction atlas)

There is no map `theta:Omega->P` and no family `g_A in Sym(P)` such that

\[
 \theta_A(x)=g_A(\theta(x))\qquad(x\in A)
\tag{6.1}
\]

and every `theta_A` is bijective.

#### Proof

If two physical points had the same global label, place them together in
an `(r+1)`-set `A`.  Equation (6.1) would give them the same `theta_A`
label, contradicting injectivity.  Hence `theta` would inject
`2r-1` points into `r+1` labels. \(\square\)

This rules out, in one statement:

* restriction of one global finite-field labelling;
* an affine or Möbius normalization of one global labelling;
* any ansatz whose entire `A`-dependence is postcomposition by a chart
  gauge;
* any point-transition formula of the coboundary form
  `tau_A,A'=g_A' g_A^{-1}`.

The obstruction is not lack of a clever normalization.  A successful
formula must alter relative labels inside a chart and generate the mandatory
transposition curvature of Theorem 4.1.

## 7. The finite patch problem

The first positive target is now completely local.

Fix an `(r+2)`-set `B`.  For every `i in B`, choose

\[
 \theta_i:B\setminus\{i\}\longrightarrow P,
 \qquad \gamma_i\in\operatorname{Sym}(C).
\]

The patch equations are, for distinct `i,j` and every
`b in B\setminus\{i,j\}`,

\[
 \boxed{
 \gamma_i Q(\theta_i(j),\theta_i(b))
 =
 \gamma_j Q(\theta_j(i),\theta_j(b)).}
\tag{7.1}
\]

They say exactly that all `r+2` locally perfect charts induce the same
colours on their common middle--lower incidence edges.  Eliminating the
`gamma_i` gives precisely the top-triangle equations (3.1).

Accordingly:

* if (7.1) has no solution with nontrivial coordinate holonomy, the entire
  projective Room-atlas route is impossible;
* if it has such a solution, the next and only additional local condition
  is compatibility of two patches across the exchange square on `r+3`
  points.

This is a strict reduction from charts on all
`binom(2r-1,r+1)` upper sets to two finite identities on `r+2` and `r+3`
points.

### Proposition 7.1 (the natural one-extra-point prolongation fails)

Let

\[
 B=P\mathbin{\dot\cup}\{*\}.
\]

Take the base chart on `A_*=P` to be the identity.  For each finite
`i in F_r`, form the chart on `A_i=B-{i}` by replacing the omitted point
`i` with `*` and then applying an affine permutation

\[
 g_i(x)=\lambda_i x+c_i\quad(x\in\mathbb F_r),
 \qquad g_i(\infty)=\infty,qquad \lambda_i\ne0.
\tag{7.2}
\]

That is,

\[
 \theta_i(*)=g_i(i),\qquad
 \theta_i(x)=g_i(x)\quad(x\in P\setminus\{i\}).
\tag{7.3}
\]

For the linear finite-field chart (2.1) of the previous note, no choice of
colour gauges makes these `r+1` charts coherent when `r>=4`.

#### Proof

Write `s=alpha+beta`.  Coherence between the base chart `A_*` and `A_i`
on their common `r`-set forces, after fixing the base colour gauge, the
normalization

\[
 z\longmapsto\frac{z-sc_i}{\lambda_i}
\tag{7.4}
\]

on the colour output of chart `A_i`.  Indeed, for finite `u ne v`,

\[
 Q(g_i(u),g_i(v))
 =\lambda_iQ(u,v)+sc_i,
\]

and the same identity holds when `v=\infty` by the definition of `Q`.

Now take distinct finite `i,j` and a finite
`b notin {i,j}`.  On the overlap of `A_i` and `A_j`, the normalized colour
assigned by `A_i` is

\[
 Q(j,b),
\]

whereas the normalized colour assigned by `A_j` is

\[
 Q(i,b).
\]

Their difference is `alpha(j-i)`, which is nonzero.  Hence the overlap
equation fails. \(\square\)

The unshifted replacement atlas is the special case `g_i=1`; it fails even
more visibly at the common point `*`, where it asks for

\[
 Q(j,i)=Q(i,j),
\]

contrary to skewness.

Proposition 7.1 is stronger than the flat-atlas obstruction for this
candidate: the replacement charts do have the required transposition
coordinate curvature (`tau_ij` swaps `i` and `j`), but their row transport
is not flat.  Thus merely inserting the correct binary curvature is not
enough; it must be inserted in the specific nonlinear form cancelled by
the rows of `Q`.

### Theorem 7.2 (complete normalization of an arbitrary top patch)

The arbitrary `(r+2)`-point patch problem is equivalent to a system on only
`r+1` permutations of `P`.

More precisely, identify the physical patch with

\[
 B=\{0\}\mathbin{\dot\cup}P
\]

and use the chart omitting `0` as the base chart, with point coordinates
and colour gauge both equal to the identity.  For every `i in P`, choose an
arbitrary permutation

\[
 \pi_i\in\operatorname{Sym}(P),
 \qquad u_i:=\pi_i(i),
\tag{7.5}
\]

and define

\[
 \Gamma_i
 :=R_i\circ\pi_i^{-1}\circ R_{u_i}^{-1}
 \in\operatorname{Sym}(C).
\tag{7.6}
\]

Then a coherent patch exists if and only if the permutations `(pi_i)` can
be chosen so that, for all distinct `i,j,x in P`,

\[
 \boxed{
 \Gamma_iQ(\pi_i(j),\pi_i(x))
 =
 \Gamma_jQ(\pi_j(i),\pi_j(x)).}
\tag{7.7}
\]

Given such permutations, the nonbase chart omitting `i` is

\[
 \theta_i(0)=\pi_i(i),\qquad
 \theta_i(x)=\pi_i(x)\quad(x\in P\setminus\{i\}),
 \qquad
 \gamma_i=\Gamma_i.
\tag{7.8}
\]

No additional equation at the physical point `0` is needed.

#### Proof

Start with an arbitrary coherent patch and normalize the chart omitting `0`
to the identity.  For the chart omitting `i`, define `pi_i` by (7.8).  The
overlap with the base chart says, for every `x ne i`,

\[
 R_i(x)=\gamma_iR_{u_i}(\pi_i(x)).
\tag{7.9}
\]

All three maps in (7.9) are bijections on the corresponding punctured
sets, so (7.9) is equivalent to `gamma_i=Gamma_i` in (7.6).  Thus one
arbitrary permutation `pi_i` determines both the point chart and its colour
gauge.

Now consider the overlap of the charts omitting `i` and `j`.  At a physical
point `x in P-{i,j}`, its equation is exactly (7.7).  At the remaining
common physical point `0`, the equation would be

\[
 \Gamma_iQ(\pi_i(j),\pi_i(i))
 =
 \Gamma_jQ(\pi_j(i),\pi_j(j)).
\tag{7.10}
\]

For fixed `i,j`, the left side of (7.7), as `x` ranges over
`P-{i,j}`, consists of `r-1` distinct colours: it is the restriction of a
bijection from `P-{j}` to `C`.  The right side has the same property and
the two restrictions agree by (7.7).  Each full bijection has exactly one
unused colour.  Its value at `x=i` on the left and at `x=j` on the right
must therefore be that same unused colour.  This is precisely (7.10).

Conversely, (7.9), (7.7), and the automatic equation (7.10) are all patch
overlaps, so (7.8) gives a coherent patch. \(\square\)

### Corollary 7.3 (symmetric punctured-conjugacy form)

Define, for distinct `i,j,x`,

\[
 D_i(j,x)=\Gamma_iQ(\pi_i(j),\pi_i(x)).
\tag{7.11}
\]

The entire first finite gate is

\[
 \boxed{D_i(j,x)=D_j(i,x).}
\tag{7.12}
\]

Thus the unresolved object is not an arbitrary collection of `r+2` point
charts and `r+2` colour gauges.  It is a family of `r+1` permutations whose
punctured conjugates of the rows of `Q` are symmetric in their first two
physical indices.

Proposition 7.1 says that no solution of (7.12) lies in the affine
replacement class.  A positive construction must use permutations
`pi_i` outside the affine/projective chart automorphism group.

### Theorem 7.4 (sign obstruction: no top patch for prime-power `r>=7`)

For the finite-field chart `Q` of Theorem 2.1, the normalized system
(7.7) has no solution for any prime power

\[
 r\ge7.
\]

Consequently the locally perfect projective Room charts cannot be glued
even on one `(r+2)`-point patch, and hence cannot produce a global Boolean
1-factorization, for any such `r`.

#### Proof

Write `q=r`, `N=q+1=|P|`.  Complete every punctured row to a permutation of
`P=C union {infinity}` by defining

\[
 \widehat R_u(u)=\infty,
 \qquad
 \widehat R_u(v)=Q(u,v)\quad(v\ne u).
\tag{7.13}
\]

Likewise, for the normalized isotope in (7.11), complete its row by

\[
 \widehat D_i^{,j}(j)=\infty,
 \qquad
 \widehat D_i^{,j}(x)=D_i(j,x)\quad(x\ne j).
\tag{7.14}
\]

For distinct `i,j`, equation (7.7) and its automatic missing-value equation
say exactly

\[
 \widehat D_j^{,i}
 =\widehat D_i^{,j}\circ(i\ j).
\tag{7.15}
\]

Indeed the two permutations agree off `{i,j}`; the first maps `i` to
infinity and `j` to the common missing finite colour, while the second does
the reverse.  Taking signs gives

\[
 \operatorname{sgn}(\widehat D_j^{,i})
 =-\operatorname{sgn}(\widehat D_i^{,j}).
\tag{7.16}
\]

Extend `Gamma_i` to fix infinity.  From (7.11),

\[
 \widehat D_i^{,j}
 =\widehat\Gamma_i\,
  \widehat R_{\pi_i(j)}\,
  \pi_i.
\]

Put

\[
 K_i=\operatorname{sgn}(\widehat\Gamma_i)
     \operatorname{sgn}(\pi_i),
 \qquad
 \rho(u)=\operatorname{sgn}(\widehat R_u).
\]

Then (7.16) becomes

\[
 K_j\rho(\pi_j(i))=-K_i\rho(\pi_i(j)).
\tag{7.17}
\]

We now compute only the number of possible values of `rho`.  For finite
`u`, let `T_a` be translation by `a` on `F_q`, fixing infinity.  Formula
(2.1) gives

\[
 \widehat R_u=T_{(\alpha+\beta)u}\,
                  \widehat R_0\,T_{-u}.
\tag{7.18}
\]

Every translation has positive sign when `q>=4`: in odd characteristic
its nontrivial cycles have odd prime length, and in characteristic two it
is a product of `q/2`, hence an even number, of transpositions.  Therefore

\[
 \rho(u)=\rho_f\qquad(u\in\mathbb F_q)
\tag{7.19}
\]

is constant on all finite row centres.  The remaining value
`rho(infinity)` is either `rho_f` or `-rho_f`.

If it is `rho_f`, then (7.17) says `K_j=-K_i` for every distinct pair
`i,j`, impossible on a triangle.

It remains to treat

\[
 \rho(\infty)=-\rho_f.
\tag{7.20}
\]

For each `i in P`, let

\[
 t(i)=\pi_i^{-1}(\infty).
\]

Multiplying (7.17) around a triple `{i,j,k}` cancels the three `K`-values
and shows that an odd number of the six directed relations

\[
 t(i)=j, t(i)=k, t(j)=i, t(j)=k, t(k)=i, t(k)=j
\tag{7.21}
\]

must hold.

Form a simple graph `H` on `P` by putting `ij in E(H)` exactly when one of
`t(i)=j,t(j)=i` holds but not both.  Condition (7.21) says that every
triangle of the complete graph contains an odd number of edges of `H`:

\[
 1_H(ij)+1_H(jk)+1_H(ki)=1\pmod2.
\tag{7.22}
\]

Fixing one vertex in (7.22) shows that `H` is the disjoint union of two
cliques: two vertices are adjacent precisely when their incidences to the
fixed vertex are equal, after placing the fixed vertex in the appropriate
class.

On the other hand, every edge of `H` consumes at least one nonloop arc
`i->t(i)`.  Since there is at most one such arc out of each vertex,

\[
 |E(H)|\le N.
\tag{7.23}
\]

The minimum number of edges in a union of two cliques on `N` vertices is

\[
 \min_s\left\{\binom s2+\binom{N-s}2\right\}.
\]

This exceeds `N` for every `N>=7`.  Since `N=q+1` and there is no prime
power `q=6`, it exceeds `N` for every prime power `q>=7`, contradicting
(7.23). \(\square\)

### Corollary 7.5 (disposition of the projective-chart lane)

The finite-field construction proves that `Delta_A=0` has no local
one-chart obstruction, but Theorem 7.4 proves that these optimal charts do
not admit even the first required overlap patch in the asymptotic regime.
Thus the projective Room-atlas route is closed for all prime powers
`r>=7`.  The exceptional patch orders `r=4,5` are not decided by the sign
argument and have no asymptotic consequence.

## 8. Final gate

The projective locally-perfect construction is equivalent to the following
two-stage theorem.

1. **Curved patch:** solve (7.1) with a transposition coordinate holonomy.
2. **Flat row transport:** arrange those patches so that the induced `h`
   also satisfies every exchange-square identity.

The cohomological audit first proves that zero-curvature, globally labelled,
rank-one, affine-normalized, and Möbius-normalized constructions cannot
work.  Theorem 7.4 then refutes **all** curved atlases made from the fixed
finite-field chart `Q` in every prime-power order `r>=7`.  A different local
`Delta=0` chart, with a genuinely different completed-row sign profile,
would be required to reopen this exact-local-orthogonality route.

Before Theorem 7.4, the nonlinear resource required was:

\[
 \boxed{
 \text{a controlled }\mathbb Z_2\text{ coordinate curvature
 annihilated by the punctured-row action of }Q.}
\]
