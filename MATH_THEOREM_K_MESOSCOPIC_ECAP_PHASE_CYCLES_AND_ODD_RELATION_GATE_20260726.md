# Mesoscopic ECAP: complement-phase cycles, near-half cuts, and the odd-relation gate

Date: 2026-07-26

Method: pure mathematics only.  No computation, finite search, solver, or
web input is used.

## 0. Outcome

This note treats the revised scale

\[
 q_0=\lceil m^{1/4}\rceil,
 \qquad H=\lfloor\beta\sqrt{m\log m}\rfloor,
 \qquad \beta>0\text{ fixed}.
\tag{0.1}
\]

Put

\[
 W=\binom{2m}{m},\qquad B=C_m={W\over m+1},
 \qquad N_q=\binom{2m}{m-q},
\tag{0.2}
\]

\[
 K_0=\left\lfloor{N_{q_0}\over2m}\right\rfloor.
\tag{0.3}
\]

Then

\[
 {N_{q_0}\over W}
 =1-{1\over\sqrt m}+O(m^{-3/4}),
\tag{0.4}
\]

\[
 {K_0\over B}
 ={1\over2}-{1\over2\sqrt m}+O(m^{-3/4}).
\tag{0.5}
\]

Thus the exact complement-graph problem is now a near-bisection problem,
at deficit

\[
 \Delta_m={B\over2}-K_0
 ={B\over2\sqrt m}+O(Bm^{-3/4}).
\tag{0.6}
\]

The proposed associahedron route is false.  The canonical infinity-cut
complement graph is not the rotation graph on binary trees: already for
(m=3) it is a doubled edge disjoint from a triangle, whereas the
associahedron graph is a simple five-cycle.

There is, however, an exact replacement.  Let (i_t(x)) be the phase-
(t) middle state of the canonical Chung--Feller row rooted at the Dyck
word (x), and put

\[
 c_t=i_{m-t}^{-1}\circ({\rm complement})\circ i_t.
\tag{0.7}
\]

For (1\le t<m/2), the labelled edges indexed by phase (t) form the
cycle multigraph of the permutation (c_t).  If (m) is even, the
central phase contributes one perfect matching.  These factors are
edge-disjoint and their union is the complete cut complement graph.

Write (o_t) for the number of odd cycles of (c_t).  Every
(K_0)-row set (S) satisfies the exact near-half lower bound

\[
 \boxed{
 e_{G_0}(S)
 \ge\sum_{1\le t<m/2}
       \left({o_t\over2}-\Delta_m\right)_+.}
\tag{0.8}
\]

For an extensive reciprocal-(C_8) bank with
(u=\lfloor\alpha m\rfloor), (0<\alpha<1/2), every global mask (A)
satisfies

\[
 \boxed{
 e_{G_A}(S)
 \ge\sum_{1\le t<m/2}
       \left({o_t\over2}-\Delta_m\right)_+
       -\left({\alpha\over16}+o(1)\right)W.}
\tag{0.9}
\]

Consequently, if

\[
 \liminf_{m\to\infty}{1\over m}
 \sum_{1\le t<m/2}
 \left({o_t\over B}-{1\over\sqrt m}\right)_+
 >{\alpha\over8},
\tag{0.10}
\]

then every extensive-(C_8) state has (Omega(W)) middle collision at
the required row density, and ECAP fails.  A lower bound strictly larger
than (1/16) on the left of (0.10) closes every permissible
(alpha<1/2).

No such odd-cycle census is presently proved.  Formula (0.10) is the
sharp structural replacement for the inapplicable pentagon-face
argument.  The all-depth interval condition supplies an additional
canonical robustness test, but no present theorem evaluates it on the
MSW phase-cycle shores.

## 1. The revised packet density

The exact central-binomial ratio is

\[
 {N_q\over W}=\prod_{j=1}^q{m-j+1\over m+j}.
\tag{1.1}
\]

Uniformly for (q=O(m^{1/4})), termwise logarithmic expansion gives

\[
 \log{N_q\over W}=-{q^2\over m}+O(m^{-1}).
\tag{1.2}
\]

For (q_0=\lceil m^{1/4}\rceil),

\[
 {q_0^2\over m}=m^{-1/2}+O(m^{-3/4}),
\tag{1.3}
\]

and exponentiation proves (0.4).  Since (B=W/(m+1)),

\[
 {K_0\over B}
 ={m+1\over2m}{N_{q_0}\over W}+o(m^{-1})
 ={1\over2}-{1\over2\sqrt m}+O(m^{-3/4}),
\tag{1.4}
\]

which proves (0.5)--(0.6).  The floor error in (K_0) is exponentially
smaller than the displayed terms.

The physical packet count and collar remain harmless:

\[
 K_0=(1/2+o(1))B=o(W/H),
\tag{1.5}
\]

\[
 2HK_0=O\!\left(W\sqrt{{\log m}\over m}\right)=o(W).
\tag{1.6}
\]

## 2. Refutation of the associahedron identification

For completeness, the five canonical semilength-three traces are

\[
\begin{array}{c|cccc}
123&123&136&146&456\\
124&124&126&156&356\\
125&125&145&345&346\\
134&134&234&236&256\\
135&135&235&245&246.
\end{array}
\tag{2.1}
\]

The two internal primary tokens in each row are the middle two entries.
Pairing them by complementation gives

\[
 136\leftrightarrow245,\qquad
 146\leftrightarrow235,
\tag{2.2}
\]

and

\[
 126\leftrightarrow345,\qquad
 156\leftrightarrow234,\qquad
 145\leftrightarrow236.
\tag{2.3}
\]

Thus rows (123,135) are joined by two parallel edges and rows
(124,125,134) form a triangle.  The graph is disconnected and has a
parallel edge.  The dimension-two associahedron graph on the same five
Catalan vertices is the simple cycle (C_5).  Hence:

\[
 \boxed{G_0\text{ is not the associahedron rotation graph.}}
\tag{2.4}
\]

In particular, pentagonal two-faces of the associahedron cannot be used
to lower-bound induced edges in (G_0).  Any such argument would concern
the wrong graph.

## 3. Exact complement-phase decomposition

For every Dyck root (x\), let

\[
 X_0(x),X_1(x),\ldots,X_m(x)
\tag{3.1}
\]

be the successive rank-(m) primary states in its canonical MSW row.
The Chung--Feller theorem says that, for every (t),

\[
 i_t:D_m\longrightarrow D_{2m}^t,\qquad i_t(x)=X_t(x),
\tag{3.2}
\]

is a bijection onto the (t)-th flaw layer.  Complementation maps that
layer bijectively to the ((m-t))-th flaw layer, so (0.7) defines a
permutation of (D_m).  It obeys

\[
                         c_{m-t}=c_t^{-1},
 \qquad c_0=c_m=1.
\tag{3.3}
\]

### Theorem 3.1 (phase-cycle factorization of (G_0))

For (1\le t<m/2), let (H_t) be the labelled multigraph

\[
 V(H_t)=D_m,\qquad
 E(H_t)=\bigl\{\{x,c_t(x)\}:x\in D_m\bigr\}.
\tag{3.4}
\]

Every (c_t) is fixed-point-free.  A permutation cycle of length two
therefore gives a doubled edge in (H_t), while a cycle of length at
least three gives the corresponding ordinary cycle.

If (m) is even, (c_{m/2}) is a fixed-point-free involution; let
(M_{m/2}) contain one edge for each of its two-cycles.  Then, as a
labelled edge-disjoint union,

\[
 \boxed{
 G_0=mathop{\dot\bigcup}_{1\le t<m/2}H_t
       \mathbin{\dot\cup}
       \begin{cases}
       M_{m/2},&m\text{ even},\\
       \varnothing,&m\text{ odd}.
       \end{cases}}
\tag{3.5}
\]

#### Proof

The nonport primary token at phase (t) in row (x) is (i_t(x)).
Its complement is

\[
 \overline{i_t(x)}=i_{m-t}(c_t(x)).
\tag{3.6}
\]

Thus its complement-graph half-edge is paired with the phase-((m-t))
half-edge in row (c_t(x)).  When (t<m/2), indexing by all (x)
counts every complementary token pair between phases (t) and (m-t)
exactly once, which is (3.4).

If (c_t(x)=x), row (x) would own two complementary nonport primary
tokens.  This is impossible in a cut row: the only complementary pair
among its primary windows is its two ports.  Hence (c_t) has no fixed
point.

At (t=m/2), complementation acts within one phase.  It is a fixed-point-
free involution and each complementary pair must be counted once, giving
the matching (M_{m/2}).  The phases (1,ldots,m-1) exhaust the
nonport tokens, so the displayed factors exhaust (G_0).  Their total
degree is

\[
 2\left\lfloor{m-1\over2}\right\rfloor
       +{\bf1}_{\{m\ {\rm even}\}}=m-1,
\]

as required. \(\square\)

At (m=3), the unique permutation (c_1) has one two-cycle and one
three-cycle, recovering Section 2 exactly.

## 4. The exact near-half induced-edge inequality

Let (o_t) be the number of odd cycles in the disjoint cycle
decomposition of (c_t).  Fixed points do not occur, so every such cycle
has length at least three.

### Lemma 4.1 (cycle-cover independence deficit)

For every (S\subseteq D_m), (|S|=B/2-\Delta),

\[
 \boxed{
 e_{H_t}(S)\ge\left({o_t\over2}-\Delta\right)_+.}
\tag{4.1}
\]

#### Proof

The independence number of an even cycle of length (ell) is
(ell/2), and that of an odd cycle is ((ell-1)/2).  Parallelism on a
two-cycle does not change its independence number.  Therefore

\[
 \alpha(H_t)={B-o_t\over2}.
\tag{4.2}
\]

On one cycle, selecting (s) vertices creates at least
((s-\lfloor\ell/2\rfloor)_+) internal labelled edges: for
(s>\ell/2), the degree identity and the bound of two boundary edges per
unselected vertex give at least (2s-ell), which is no smaller than the
claimed quantity.  Summing over cycles and using

\[
 \sum_C(a_C)_+\ge\left(\sum_Ca_C\right)_+
\]

gives

\[
 e_{H_t}(S)
 \ge(|S|-\alpha(H_t))_+
 =\left({o_t\over2}-\Delta\right)_+.
\]

\(\square\)

Summing Lemma 4.1 over the edge-disjoint phase factors proves (0.8).
Notice the exact threshold: an odd-cycle count (o_t\le2\Delta_m) can be
absorbed by the near-half row deficit at that phase without forcing an
edge.  At the present scale,

\[
 {2\Delta_m\over B}
 ={1\over\sqrt m}+O(m^{-3/4}).
\tag{4.3}
\]

Thus one needs odd-cycle counts above (B/\sqrt m) on a positive number
of phases before (0.8) becomes informative.

## 5. Comparison with the extensive reciprocal bank

One reciprocal-(C_8) rectangle swaps two nonport primary tokens (Q,R)
between two fixed-port rows (x,y).  If their complementary tokens are
owned by (z,w), respectively, its complement-graph edit is

\[
                  xz,yw\quad\longleftrightarrow\quad yz,xw.
\tag{5.1}
\]

For (s_v={\bf1}_{\{v\in S\}}), the exact induced-edge difference is

\[
 (s_y-s_x)(s_z-s_w)\in\{-1,0,1\}.
\tag{5.2}
\]

Hence a rectangle can improve (e(S)) only when its source row pair and
its dual complement-owner pair are both split by (S).

Let (J(x)) be the eligible slot set of root (x).  For a global mask
(A\), put

\[
 I_A(S)=\sum_{x\in S}|A\cap J(x)|.
\tag{5.3}
\]

Sequentially applying (5.2) gives

\[
 |e_{G_A}(S)-e_{G_0}(S)|\le I_A(S).
\tag{5.4}
\]

The exact one- and two-slot Catalan censuses give, for
(z_x=|J(x)|),

\[
 {1\over B}\sum_xz_x={\alpha m\over8}+O_\alpha(1),
 \qquad
 {1\over B}\sum_x(z_x-\bar z)^2=O_\alpha(m).
\tag{5.5}
\]

Since (K_0/B=1/2+o(1)), Cauchy--Schwarz yields

\[
 \max_{|S|=K_0}\sum_{x\in S}|J(x)|
 =\left({\alpha\over16}+o(1)\right)W.
\tag{5.6}
\]

Here Cauchy--Schwarz gives the upper bound.  The matching lower bound
follows by averaging the incidence over all \(K_0\)-subsets: its mean is
\(K_0\bar z=(\alpha/16+o(1))W\).

Combining (0.8), (5.4), and (5.6) proves (0.9).

Define

\[
 \Theta_m={1\over m}
 \sum_{1\le t<m/2}
 \left({o_t\over B}-{2\Delta_m\over B}\right)_+.
\tag{5.7}
\]

Because (W=(m+1)B), (0.9) becomes

\[
 \boxed{
 {e_{G_A}(S)\over W}
 \ge {m\over2(m+1)}\Theta_m
          -{\alpha\over16}-o(1).}
\tag{5.8}
\]

Equations (4.3) and (5.8) prove the obstruction criterion (0.10).

The constant comparison is exact:

* the selected-row reciprocal incidence budget is
  ((\alpha/16+o(1))W);
* each incidence can reduce (e(S)) by at most one;
* the physical middle collision is (2e(S));
* therefore the collision repair ceiling is
  ((\alpha/8+o(1))W<(1/16+o(1))W).

The complete bank contains (uC_{m-2}=(\alpha/16+o(1))W) rectangles,
so at this near-half density essentially the full raw bank scale is
visible.  The obstruction is not lack of raw rectangles; it is whether
their globally coupled two-switch signs can overcome the phase-cycle
oddness.

## 6. Odd relations: the exact analogue of a pentagon charge

The phase-cycle bound has a useful group form.  Let

\[
                         \chi_S(x)\in\{0,1\}
\]

be the shore bit of a row.  For one complement-phase permutation, define
the monochromatic transition count

\[
 M_t(S)=|\{x:\chi_S(c_t x)=\chi_S(x)\}|.
\tag{6.1}
\]

### Lemma 6.1 (exact monochromatic identity)

If (|S|=B/2-\Delta), then

\[
 \boxed{M_t(S)=2e_{H_t}(S)+2\Delta.}
\tag{6.2}
\]

#### Proof

Let (a) be the number of directed transitions from (S) to (S), and
(d) the number from (S^c) to (S^c).  By (3.4), (a=e_{H_t}(S)).
Since (c_t) is a permutation, the two crossing directions have the same
size (|S|-a).  Therefore

\[
 d=B-a-2(|S|-a)=a+2\Delta,
\]

and (M_t=a+d=2a+2\Delta). \(\square\)

### Theorem 6.2 (odd phase-word charge)

Suppose

\[
 c_{t_L}^{\varepsilon_L}\cdots
 c_{t_1}^{\varepsilon_1}=1,
 \qquad \varepsilon_j\in\{-1,1\},
\tag{6.3}
\]

is a permutation identity of odd length (L).  Then every
(|S|=B/2-\Delta) satisfies

\[
 \boxed{
 \sum_{j=1}^{L}e_{H_{t_j}}(S)
       \ge {B\over2}-L\Delta.}
\tag{6.4}
\]

The same conclusion holds for an identity on an invariant subset
(Omega\subseteq D_m), with (B) replaced by (|\Omega|) and with the
shore imbalance inside (Omega) charged explicitly.

#### Proof

Start at any row (x) and follow the (L) phase-permutation steps in
(6.3).  The endpoint is again (x).  Hence the shore bit changes an even
number of times.  Since (L) is odd, at least one of the (L) steps is
monochromatic.  Summing over all starting rows gives

\[
 B\le\sum_{j=1}^{L}M_{t_j}(S).
\tag{6.5}
\]

Inversion does not change the number of monochromatic transitions.  Apply
Lemma 6.1 to every summand and rearrange to obtain (6.4). \(\square\)

This theorem is the correct abstract version of the desired pentagon
charge.  A bounded-congestion family of (Theta(m)) odd phase relations,
each acting on (Theta(B)) rows and of length (o(\sqrt m)), would force
(Omega(mB)=Omega(W)) induced-edge mass at the near-half density.  The
associahedron pentagons do not furnish such relations because they are not
cycles of (G_0).  Constructing or excluding an adequate phase-relation
family is an exact remaining algebraic problem.

## 7. Shallow and all-depth interval robustness

Let (h_q(S,A)) be the lower rank-((m-q)) hole count of the selected cut
orders.  One active reciprocal slot on one selected row makes exactly two
adjacent transpositions in that row.  At every proper interval length,
their combined occurrence action is at most four.  Therefore

\[
 \boxed{
 |h_q(S,A)-h_q(S,0)|\le4I_A(S)
 \le\left({\alpha\over4}+o(1)\right)W}
\tag{7.1}
\]

for every (q), uniformly at the scale (0.1).  Upper holes obey the same
identity by complementation.

Define the exact quantity

\[
 Z_m=\max_{\substack{S\subseteq D_m\\|S|=K_0}}
          \sum_{x\in S}|J(x)|
     =\left({\alpha\over16}+o(1)\right)W
\tag{7.2}
\]

using the exact maximum in (5.6), and put

\[
\begin{aligned}
 {\cal R}^{\rm meso}_{\alpha,\beta}(m)
 =\min_{|S|=K_0}\bigg[&
  \left(
    \sum_{1\le t<m/2}
       \left({o_t\over2}-\Delta_m\right)_+-Z_m
  \right)_+\\
 &+\sum_{q=q_0}^{H}(h_q(S,0)-4Z_m)_+
 \bigg].
\end{aligned}
\tag{7.3}

The first term is independent of (S), but it is displayed inside the
same functional to emphasize the common selection.

### Corollary 7.1 (mesoscopic hereditary obstruction)

If the extensive common-factor ECAP holds at (0.1), then

\[
 \boxed{{\cal R}^{\rm meso}_{\alpha,\beta}(m)=o(W).}
\tag{7.4}
\]

More precisely, its witnessing canonical row sets must satisfy

\[
 \sum_{q=q_0}^{H}
      \left(h_q(S,0)-4Z_m\right)_+
 =o(W).
\tag{7.5}
\]

#### Proof

The middle term follows from (0.9).  Equation (7.1), nonnegativity of
holes, and summation over the same selected row set give (7.5), hence
(7.4).  Keeping the exact threshold \(4Z_m\) is essential: an unspecified
per-depth \(o(W)\) error cannot be summed over
\(H-q_0+1\to\infty\) depths. \(\square\)

The raw summed action ceiling across the whole interval is

\[
 4(H-q_0+1)Z_m
 =\left({\alpha\beta\over4}+o(1)\right)
      W\sqrt{m\log m}.
\tag{7.6}
\]

This is of the same order as the total occurrence mass of the annulus and
does not prove a positive selection theorem.  It also shows why checking
only total trade supply is inconclusive.  ECAP needs the canonical excess
above the per-depth hinge (4Z_m) to have aggregate (o(W)), and it needs
one global mask to realize the correct signs in the complete hereditary
flag profile.

## 8. Proved boundary

The following are unconditional.

1. The associahedron identification, and hence its pentagon-face argument,
   is false for the canonical infinity-cut complement graph.
2. The exact graph is the union of the complement-phase permutation cycle
   multigraphs (3.5).
3. The odd-cycle census gives the near-half lower bound (0.8).
4. Reciprocal-(C_8) action subtracts at most
   ((\alpha/16+o(1))W) from that induced-edge bound.
5. Bounded odd phase relations obey the exact charge (6.4).
6. The same selected incidence budget yields the hereditary interval-hole
   test (7.5).

The unresolved quantities are now exact.

1. Determine the cycle counts (o_t) of the Chung--Feller complement
   permutations (c_t), or construct a bounded-congestion family of odd
   phase relations.  Condition (0.10) is sufficient for a middle-rank
   obstruction.
2. If the odd-cycle mean is too small to obstruct, construct a row shore
   which is simultaneously near-alternating for almost every (c_t).
3. On that same shore, prove or refute the aggregate canonical flag margin
   (7.5), and only then align one global reciprocal mask with all remaining
   middle and interval signs.

No coefficient-one conclusion is claimed.  The result replaces an
incorrect geometric model by the exact algebraic graph and supplies the
sharp constant comparison needed at the revised mesoscopic entrance
scale.
