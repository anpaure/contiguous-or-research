# Fixed-parameter fine-strip integrality, a slow diagonal, and the exact boundary of matching/flow rounding

Date: 2026-07-26

Method: pure mathematics.  The only external input is the standard
fixed-uniformity Pippenger--Frankl--Rödl almost-perfect matching theorem,
stated explicitly below.  It is used only with two integers (H,h) fixed
before (m\to\infty).

## 0. Outcome

Let

\[
 W=\binom{2m}{m},\qquad
 \tau_{m,H,h}
\]

be the integral labelled fine-strip cover optimum, and recall its exact
fractional value

\[
 \tau^*_{m,H,h}
 =W+\frac Hh\binom{2m}{m-1}.                         \tag{0.1}
\]

The following is unconditional.

> **Theorem A (fixed-parameter SCI).**  For every pair of fixed integers
> (1\le H<h), as (m\to\infty),
> \[
>  \boxed{\tau_{m,H,h}=\tau^*_{m,H,h}+o_{H,h}(W).}   \tag{0.2}
> \]

Consequently there are integer sequences

\[
 H_m\longrightarrow\infty,qquad
 h_m\longrightarrow\infty,qquad
 \frac{H_m}{h_m}\longrightarrow0                    \tag{0.3}
\]

for which

\[
 \boxed{\tau_{m,H_m,h_m}=W+o(W).}                   \tag{0.4}
\]

Thus the fine-strip integrality gap is not bounded below by a positive
fraction of (W) merely because the number of audited depths tends to
infinity.  It vanishes on an arbitrarily slowly growing diagonal.

This does **not** prove the coefficient-one theorem.  The diagonal supplied
by the fixed-rank matching theorem can be much smaller than (sqrt m),
whereas economical product-SCD tails require
(H_m/\sqrt m\to\infty).

Two exact obstructions explain why the proof cannot be substituted at the
target parameters

\[
 H=\lceil\sqrt{m\log m}\rceil,qquad h=m^{3/4+o(1)}. \tag{0.5}
\]

1. The direct target-by-strip incidence matrix is not totally unimodular;
   it contains a (3\times3) determinant-two minor already on the middle
   layer.
2. A matching in the full band strip hypergraph contains at most
   (N_H/(2h)) strips and therefore covers at most (N_H) middle owners.
   At (0.5), (N_H/W=m^{-1+o(1)}), so such a matching misses
   ((1-o(1))W) middle owners.

The Gaussian theorem must therefore be a genuinely **capacitated** integral
cover: it must allow the forced multiplicities in the smaller ranks.  It
cannot be obtained by ordinary full-band matching, direct total
unimodularity, or an unqualified fixed-uniformity citation.

## 1. The band hypergraph

Fix (H<h).  Let

\[
 \mathcal V_{m,H}
 =\bigcup_{d=-H}^{H}\binom{[2m]}{m+d}.               \tag{1.1}
\]

For every physical (2h)-strip (C), make one hyperedge

\[
 e(C)=\mathcal T_H(C).                               \tag{1.2}
\]

At the middle rank a strip has (2h) targets, and at each nonzero signed
depth it again has (2h) targets.  Hence this is the

\[
 k=2h(2H+1)                                          \tag{1.3}
\]

uniform hypergraph \(\mathcal H_{m,H,h}\).

Write

\[
 N_q=\binom{2m}{m-q}.
\]

The degree of a vertex in either signed depth-(q) layer is

\[
 D_q=\frac{(m+q)!(m-q)!}{2(m-h)!^2}.                 \tag{1.4}
\]

For fixed (H,h), uniformly for (0\le q\le H),

\[
 \frac{D_q}{D_0}
 =\frac{(m+q)!(m-q)!}{m!^2}
 =1+O_{H}(m^{-1}).                                   \tag{1.5}
\]

The exact strip-pair codegree formula gives

\[
 \max_{S\ne T}
 \frac{d(S,T)}{\min\{d(S),d(T)\}}
 \le \frac{2}{m-H+1}.                               \tag{1.6}
\]

It follows from (1.5)--(1.6) that, with (D=D_0),

\[
 d(v)=(1+o(1))D\quad(v\in\mathcal V_{m,H}),
 \qquad
 \Delta_2=o(D).                                     \tag{1.7}
\]

The hypergraph is simple.  Indeed, the middle support of a physical strip
induces its (2h)-cycle in the Johnson graph: two of its states are Johnson
adjacent exactly when their cyclic distance is one.  Thus the middle
support recovers the cyclic order up to rotation and reversal, and then its
intersection recovers the core.

## 2. Fixed-uniformity almost-perfect matching

We use the following standard form of the Pippenger--Frankl--Rödl theorem.

> **Fixed-rank matching theorem.**  Fix (k\).  Let
> (\mathcal G_n\) be simple (k)-uniform hypergraphs and suppose there are
> numbers (D_n\to\infty) such that
> \[
>   d(v)=(1+o(1))D_n\quad\text{uniformly in }v,
>   \qquad \Delta_2(\mathcal G_n)=o(D_n).
> \]
> Then (\mathcal G_n\) has a matching leaving (o(|V(\mathcal G_n)|))
> vertices uncovered.

For fixed (H,h), equation (1.3) fixes (k), while (1.7) verifies the
hypotheses.  Therefore (\mathcal H_{m,H,h}\) has a matching

\[
 \mathcal M\subseteq\mathscr C_{m,h}                 \tag{2.1}
\]

which leaves

\[
 Z=o_{H,h}(|\mathcal V_{m,H}|)=o_{H,h}(W)            \tag{2.2}
\]

band targets uncovered.  The chosen strips are disjoint at every audited
rank, in particular on the middle layer.

Let (s=|\mathcal M|).  Since its hyperedges are disjoint,

\[
 ks=|\mathcal V_{m,H}|-Z.                            \tag{2.3}
\]

Select these whole strips in the integral fine-strip program and select
the (Z) uncovered targets as singleton repairs.  This gives the integral
objective

\[
 J=(2h+2H)s+Z.                                       \tag{2.4}
\]

Put

\[
 \rho=\frac{2h+2H}{2h(2H+1)}
 =\frac{1+H/h}{2H+1}.                                \tag{2.5}
\]

Equations (2.3)--(2.5) give

\[
 J=\rho|\mathcal V_{m,H}|+(1-\rho)Z.                \tag{2.6}
\]

For fixed (H),

\[
 N_q=W\bigl(1+O_H(m^{-1})\bigr),
\]

and therefore

\[
 |\mathcal V_{m,H}|
 =W+2\sum_{q=1}^{H}N_q
 =(2H+1)W+O_H(W/m).                                  \tag{2.7}
\]

Substitution into (2.6), followed by (2.2), yields

\[
 J=(1+H/h)W+o_{H,h}(W).                              \tag{2.8}
\]

On the other hand,

\[
 \tau^*_{m,H,h}
 =W+\frac HhN_1
 =(1+H/h)W+O_{H,h}(W/m).                             \tag{2.9}
\]

Since \(\tau^*\le\tau\le J\), equations (2.8)--(2.9) prove Theorem A.

Notice what made the ordinary matching legitimate here: for fixed (H),
all (2H+1) layer sizes differ by only (O(W/m)=o(W)).  This ceases to be
true in a Gaussian or super-Gaussian window.

## 3. A slowly growing unconditional diagonal

For every integer (j\ge1), apply Theorem A with

\[
 H=j,\qquad h=j^2+1.                                 \tag{3.1}
\]

Choose increasing thresholds (M_j\) so that for (m\ge M_j),

\[
 \frac{\tau_{m,j,j^2+1}-\tau^*_{m,j,j^2+1}}W
 \le\frac1j,                                        \tag{3.2}
\]

and enlarge them so that (M_j\ge(j^2+2)^4\).  Define

\[
 j(m)=\max\{j:M_j\le m\},\qquad
 H_m=j(m),\qquad h_m=j(m)^2+1.                       \tag{3.3}
\]

Then (j(m)\to\infty), (h_m<m), and

\[
 \frac{H_m}{h_m}\le\frac1{j(m)}\longrightarrow0.  \tag{3.4}
\]

Equations (0.1), (3.2), and (3.4) give

\[
 \tau_{m,H_m,h_m}
 \le W+\frac{H_m}{h_m}N_1+\frac W{j(m)}
 =W+o(W),                                            \tag{3.5}
\]

which proves (0.4).

The imposed (M_j\ge(j^2+2)^4\) makes

\[
 H_m\le m^{1/8}=o(\sqrt m).                          \tag{3.6}
\]

This is not claimed to be an intrinsic ceiling; it only records that a
qualitative fixed-(k) theorem supplies no useful Gaussian rate.

## 4. The direct incidence matrix is not TU

The failure of direct total unimodularity already occurs on three middle
rows.

Assume (2\le h\le m-1).  Choose an ((m-2))-set (R) and four distinct
points (a,b,c,d\notin R).  Put

\[
 S_1=R\cup\{a,b\},\qquad
 S_2=R\cup\{a,c\},\qquad
 S_3=R\cup\{a,d\}.                                  \tag{4.1}
\]

Any adjacent pair of middle sets extends to a physical (2h)-strip.  More
precisely, for (S_1,S_2), choose a core (K\subset S_1\cap S_2) of size
(m-h), put (z_0=b,z_h=c), order the remaining (h-1) points of
((S_1\cap S_2)\setminus K) as (z_1,\ldots,z_{h-1}), and choose
(z_{h+1},\ldots,z_{2h-1}) outside (S_1\cup S_2\), avoiding (d).
There are enough points because (h\le m-1).  The resulting strip contains
(S_1,S_2) and excludes (d), so it does not contain (S_3).  Call it
(C_{12}).

Cyclically repeating the construction, while excluding respectively
(b) and (c), gives strips (C_{23}) and (C_{31}).  On the three rows
(S_1,S_2,S_3) and three columns (C_{12},C_{23},C_{31}), the incidence
matrix is

\[
 \begin{pmatrix}
  1&0&1\\
  1&1&0\\
  0&1&1
 \end{pmatrix},                                     \tag{4.2}
\]

whose determinant is (2).  Therefore:

> **Theorem B (non-TU).**  For (2\le h\le m-1), the physical
> target-by-strip incidence matrix is not totally unimodular, even after
> restriction to the middle layer.  Adding singleton identity columns does
> not change this conclusion.

Thus the fractional optimum cannot be rounded merely by declaring the
displayed LP to be a network matrix.  An exact-flow proof would need a
genuinely larger extended formulation and additional structure.

## 5. Why full-band matching collapses at the target scale

Let a family of strips be a matching in the full band hypergraph.  At the
signed outer layer (m-H), every strip consumes (2h) distinct vertices.
Hence

\[
 |\mathcal M|\le\frac{N_H}{2h}.                      \tag{5.1}
\]

The same strips cover exactly (2h|\mathcal M|) middle vertices, so

\[
 \left|\bigcup_{C\in\mathcal M}M(C)\right|\le N_H.  \tag{5.2}
\]

The middle-layer estimate by itself is not yet an objective obstruction:
the fractional optimum already has a baseline term (W).  The strict gap
comes from considering the middle layer together with the two signed
depth-one layers.  If (s=|\mathcal M|), disjointness implies that exactly
(2hs) targets are covered in each of these three layers.  Therefore any
completion of this matching by singleton repairs has objective (J)
satisfying

\[
\begin{aligned}
 J
 &\ge (2h+2H)s+(W-2hs)+2(N_1-2hs)\\
 &=W+2N_1+(2H-4h)s\\
 &\ge W+2N_1-\left(2-\frac Hh\right)N_H .           \tag{5.3}
\end{aligned}
\]

The last inequality uses (H<h), so (2H-4h<0), together with
(s\le N_H/(2h)).

For (H=o(m^{2/3})),

\[
 \log\frac{N_H}{W}
 =-\frac{H^2}{m}+O\!\left(\frac{H^3}{m^2}+\frac Hm\right). \tag{5.4}
\]

At (H=\lceil\sqrt{m\log m}\rceil), this gives

\[
 \frac{N_H}{W}=m^{-1+o(1)}.                          \tag{5.5}
\]

Since (N_1=(1-o(1))W), equations (5.3)--(5.5) show that every
full-band matching followed by singleton repair has

\[
 J\ge(3-o(1))W,                                      \tag{5.6}
\]

whereas

\[
 \tau^*_{m,H,h}=W+\frac HhN_1=(1+o(1))W             \tag{5.7}
\]

at the target parameters.  More generally, if
(H/\sqrt m\to A\in(0,\infty]), (H=o(m^{2/3})), and (H/h\to0),
then (N_H/W\to e^{-A^2}) (with (e^{-\infty}=0)), and (5.3) gives

\[
 \liminf\frac JW\ge3-2e^{-A^2}>1
 =\lim\frac{\tau^*_{m,H,h}}W .                      \tag{5.8}
\]

This proves:

> **Theorem C (outer-capacity obstruction).**  At any Gaussian or
> super-Gaussian cutoff (H/\sqrt m\to A\in(0,\infty]), with
> (H=o(m^{2/3})) and (H/h\to0), an ordinary matching in the complete
> band hypergraph followed by singleton repair has a positive linear
> objective gap above \(\tau^*\).  At the target cutoff the objective is at
> least ((3-o(1))W).  The needed integral object must use rank-dependent
> capacities approximately (W/N_q), rather than forbid all target
> collisions.

Theorem C is not an obstruction to SCI itself.  The fractional optimum
deliberately overcovers the smaller layers.  It is an exact obstruction only
to replacing the cover problem by an ordinary matching problem.

## 6. Audited frontier

Theorems A--C give the following precise answer to the three natural
rounding proposals.

* **LP duality:** the fractional value is exact, and fixed-parameter
  integrality follows asymptotically, so there is no static positive
  fractional cut.
* **Exact flow/TU:** the literal incidence matrix is non-TU by (4.2).
* **Randomized/near-matching rounding:** fixed-rank Pippenger rounding works
  and even diagonalizes to (H_m\to\infty), but full-band matching fails
  at (H\asymp\sqrt{m\log m}) by the outer-rank capacity bound.

The still-open statement for

\[
 H=\sqrt{m\log m},\qquad h=m^{3/4+o(1)}
\]

is a capacitated, chronology-correlated rounding theorem.  A useful positive
form is to choose (W+o(W)) total occurrences and obtain aggregate
floor/ceiling discrepancy (o(W)) over all signed ranks.  No theorem in
this note supplies that growing-rank capacity synchronization.
