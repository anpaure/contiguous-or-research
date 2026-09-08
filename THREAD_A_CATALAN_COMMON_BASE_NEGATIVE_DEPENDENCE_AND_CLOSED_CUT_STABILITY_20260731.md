# Quasirandom common bases: exchange rounding, closed-cut stability, and the rooted-star boundary

Date: 2026-07-31  
Status: exact negative-dependence obstruction, exact endpoint-orientation
cut theorem, exact sufficient exchange theorems, and exact Galois/spectral
reduction of the closed-cut tail.  The Boolean stability/container estimate
needed to finish the quasirandom common-basis theorem remains open.

## 1. Verdict and scope

Use

\[
 M=\binom{2n}{n},\qquad N=\binom{2n}{n-1},\qquad
 P=\binom{2n}{n-2},\qquad K=\operatorname {Cat}_n,
\]
\[
 C=M-P=\operatorname {Cat}_{n+1},\qquad
 R=N-C=P-K,\qquad q=C/N,\qquad r=R/N.               \tag{1.1}
\]

For every oriented child Catalan path forest \(F\), the unrestricted
two-step upper and lower pullbacks have a common \(C\)-element deletion
basis \(Q\).  Their common-base polytope contains

\[
                              q\mathbf 1_F.           \tag{1.2}
\]

The previous punctured-side theorem proves that a \(Q\) satisfying five
local quasirandom bounds has \(P-o(P)\) physical side forests on both
shores.  This note establishes the exact boundary of attempts to put those
bounds on a common basis.

1. Strongly-Rayleigh or balanced measures on the two individual matroids
   do not survive common-base intersection in general.  A four-element
   transversal example forces positive correlation.
2. If the actual Boolean common bases satisfy basis exchange, then
   pipage/swap rounding of (1.2) proves the full cylinder inequality and
   closes the asymptotic common-\(Q\) bridge.
3. In the strict direct-edge catalogue the occurrence graphs are
   orientation-independent.  Orientation is exactly one coupled Boolean
   endpoint choice per path, and simultaneous two-shore SBE is an explicit
   signed threshold cut system which must be solved *before* choosing
   \(Q\).  It has an exact orientation-only union-bound/LLL sufficient
   theorem.
4. An unshifted strict cylinder inequality is already false at \(n=3\):
   eleven of fifteen edges are forced.  The correct sufficient statement
   contracts the forced core and uses a shifted, nonuniform cylinder law.
5. Uniform unconditioned \(Q\) has an exact Galois-closed Hall-cut normal
   form.  Scalar KK is strengthened to an exact four-term threshold gap,
   and spectral equality cuts are classified.  Coordinate-star cuts have
   exponentially negligible tails.
6. What remains for the closed-cut route is one quantitative
   stability/container estimate for near-KK Galois-closed pairs.
7. The rooted-star graphic formulation is downstream.  It gives an exact
   forest-envelope Hall theorem, but neither direct occurrence degrees nor
   the graphic row imply the required common-base negative dependence.

No all-dimensional exact collar, residence, compiler, \(K17\), or
\(\nu=B\) theorem is claimed.

## 2. Common-base intersections need not be negatively dependent

### Theorem 2.1 (four-element intersection obstruction)

On \(E=\{1,2,3,4\}\), let \(M_1\) and \(M_2\) be the rank-two partition
matroids with blocks

\[
 M_1:\{1,2\}\mid\{3,4\},\qquad
 M_2:\{1,3\}\mid\{2,4\}.                            \tag{2.1}
\]

Both are transversal, representable, strongly Rayleigh and uniformly
dense.  The common bases are exactly

\[
                         \mathcal B=\{\{1,4\},\{2,3\}\}.             \tag{2.2}
\]

No full-support probability measure on \(\mathcal B\) is pairwise
negatively correlated.  In particular, no such measure is balanced,
negative-cylinder or strongly Rayleigh.

#### Proof

The basis lists of the two partition matroids intersect in (2.2).  If the
first basis has probability \(p\in(0,1)\), then

\[
 \Pr(1,4)=p,\qquad \Pr(1)=\Pr(4)=p,
\]

and hence

\[
                         \Pr(1,4)=p>p^2=\Pr(1)\Pr(4).                \tag{2.3}
\]

Exact marginals \(1/2\) force \(p=1/2\), so the violation remains.  The
support also fails basis exchange.  Equivalently, for \(a,b>0\),

\[
                              az_1z_4+bz_2z_3                         \tag{2.4}
\]

is not real stable: the support of a homogeneous multiaffine stable
polynomial is a matroid base family.  \(\square\)

Every representable transversal pullback separately has a determinantal
strongly-Rayleigh basis measure.  Theorem 2.1 proves that taking the
coefficientwise intersection of the two basis supports does not preserve
stability.  Thus (1.2), common-base integrality and individual determinant
measures do not imply the desired concentration.

## 3. A Boolean exchange theorem would suffice

Let \(\mathcal B\) be the actual family of unrestricted common
\(C\)-bases on \(F\).

### Theorem 3.1 (matroidal common bases imply the cylinder bound)

Suppose \(\mathcal B\) is the base family of a matroid \(M_{\cap}\) on
\(F\).  Equivalently, it is enough to prove the basis-exchange axiom; a
convenient stronger target is symmetric exchange:

\[
\begin{split}
&B_1,B_2\in\mathcal B,\ e\in B_1\setminus B_2\\
&\qquad\Longrightarrow
\exists f\in B_2\setminus B_1:
B_1-e+f,\ B_2-f+e\in\mathcal B.                     \tag{3.1}
\end{split}
\]

Then there is a probability distribution on \(\mathcal B\) satisfying

\[
                 \Pr(A\subseteq Q)\le q^{|A|}
                 \qquad(A\subseteq F).               \tag{3.2}
\]

Consequently the quasirandom common-basis Hypothesis 6.7 of
THREAD_A_CATALAN_TWO_COORDINATE_COMMON_Q_AND_PUNCTURED_FOREST_NIBBLE_20260731.md
holds, and both punctured shores have \(P-o(P)\) side forests.

#### Proof

By (1.2), \(x=q\mathbf 1_F\) lies in the convex hull of
\(\{\mathbf 1_B:B\in\mathcal B\}\), which under the hypothesis is the base
polytope of \(M_{\cap}\).  Apply pipage or swap rounding inside this base
polytope.  For completeness, along an exchange direction

\[
                           x_i\mapsto x_i+t,\qquad x_j\mapsto x_j-t,
\]

the monomial \(\prod_{e\in A}x_e\) is constant or affine unless
\(i,j\in A\), in which case its varying factor is

\[
                              (x_i+t)(x_j-t),
\]

a concave quadratic.  Choosing the two feasible endpoints with barycentric
probabilities preserving the current expectation therefore makes every
such monomial a supermartingale.  Iterating to a base gives

\[
 \mathbb E\prod_{e\in A}\mathbf1[e\in Q]
 \le\prod_{e\in A}x_e=q^{|A|},
\]

which is (3.2).  The previously proved factorial-moment argument converts
(3.2) into all five local quasirandom bounds.  \(\square\)

The theorem uses no assertion that the uniform distribution on
\(\mathcal B\) is balanced.  It constructs a suitable distribution from
the fractional point.  What is open is (3.1), or any weaker
Boolean-specific alternating-circuit rounding theorem with comparable
concentration.

### Corollary 3.2 (forced-core shifted version)

Let \(Z=\bigcap_{Q\in\mathcal B}Q\), contract \(Z\), and suppose the
residual common-base family is matroidal.  If its base polytope contains a
point \(x\) such that, for every local family \(L\),

\[
 |Z\cap L|\le b_L/2,\qquad
 \sum_{e\in L\setminus Z}x_e\le\lambda_L,            \tag{3.3}
\]

where

\[
 (\lambda_L)\le(5,3n,6,6,5n),\qquad
 (b_L)=(4n/\log n,20n,4n/\log n,4n/\log n,30n),
\]

then some common basis satisfies all five local bounds.

#### Proof

Swap-round the residual point \(x\).  The same supermartingale argument
gives the nonuniform cylinders

\[
                    \Pr(A\subseteq Q\setminus Z)\le\prod_{e\in A}x_e.
\]

The shifted-cylinder theorem in
THREAD_A_CATALAN_STRICT_FORCED_CORE_SHIFTED_CYLINDER_AND_FOREST_ENVELOPE_20260731.md
then gives the simultaneous local bounds.  \(\square\)

## 4. Strict occurrence laws: exact help and exact limitation

In the strict direct-edge catalogue, every extreme outer colour has
occurrence degree \(n+2\), while a middle \(n\)-set \(D\) has degree

\[
                               n-d_F(D)\le n.          \tag{4.1}
\]

Therefore every extreme family \(\mathcal A\) has

\[
                 |N(\mathcal A)|
                 \ge\left\lceil{n+2\over n}|\mathcal A|\right\rceil.
                                                                  \tag{4.2}
\]

This proves one-sided unpunctured Hall.  It does not prove that a random
deletion bank remains matchable.  Indeed the deletion density is

\[
 q={2(2n+1)\over n(n+2)},
\]

and applying only (4.2) after average deletion yields the factor

\[
 (1-q){n+2\over n}
 ={n^2-2n-2\over n^2}
 =1-{2\over n}-{2\over n^2}<1.                      \tag{4.3}
\]

Thus the exact degree-count expansion is too small even to certify
mean-survival of the strict Hall row.  More structure is necessary.

### Theorem 4.1 (orientation is exactly a two-shore endpoint cut system)

Fix the underlying *unoriented* Catalan path forest.  Write its \(K\)
components, with an arbitrary reference direction, as

\[
             P_j=(a_j,\ldots,b_j),\qquad 1\le j\le K,
\]

and let \(\varepsilon_j\in\{0,1\}\) reverse the reference direction when
\(\varepsilon_j=1\).  For a singleton component take \(a_j=b_j\); its
bit is inert.  The two strict occurrence graphs

\[
                 G^-=(O^-,X),\qquad G^+=(O^+,X)       \tag{4.4}
\]

are independent of \(\varepsilon\).  The weight-one terminal omitted from
the upper tail image and the weight-one terminal omitted from the lower
head image are, respectively,

\[
\begin{array}{c|cc}
 &\varepsilon_j=0&\varepsilon_j=1\\ \hline
 \zeta_j^-&b_j&a_j\\
 \zeta_j^+&a_j&b_j.
\end{array}                                           \tag{4.5}
\]

For \(\sigma\in\{-,+\}\), \({\cal U}\subseteq O^\sigma\), and
\(W=N_{G^\sigma}({\cal U})\), define

\[
 d_\sigma({\cal U})=
 \max\left\{0,
 \left\lceil{N|{\cal U}|-R|W|\over C}\right\rceil
 \right\}.                                           \tag{4.6}
\]

Then an orientation is SBE on both shores if and only if

\[
 \boxed{
 \sum_{j=1}^K {\bf1}[\zeta_j^\sigma(\varepsilon_j)\in W]
       \ge d_\sigma({\cal U})
 \quad(\sigma\in\{-,+\},\ {\cal U}\subseteq O^\sigma).}
                                                            \tag{4.7}
\]

It is enough in (4.7) to use outer families closed under

\[
 {\cal U}\longmapsto
 \{o\in O^\sigma:N(o)\subseteq N({\cal U})\}.        \tag{4.8}
\]

In reference variables, an upper row of (4.7) has left side

\[
 \sum_j\bigl((1-\varepsilon_j){\bf1}[b_j\in W]
              +\varepsilon_j{\bf1}[a_j\in W]\bigr),  \tag{4.9}
\]

while the lower row has left side

\[
 \sum_j\bigl((1-\varepsilon_j){\bf1}[a_j\in W]
              +\varepsilon_j{\bf1}[b_j\in W]\bigr). \tag{4.10}
\]

Thus simultaneous SBE is a finite signed Boolean threshold system.  It
contains no \(Q\)-variable.

#### Proof

For an undirected child edge with endpoints \(t,h\), the labels
\(L=t\cap h\), \(U=t\cup h\), the conditions defining an occurrence, and
its undirected physical edge are unchanged when \(t,h\) are exchanged.
Hence both occurrence graphs are orientation-independent.  On a coherently
oriented path, the tail image omits the final endpoint and the head image
omits the initial endpoint, proving (4.5).

Every nonterminal path vertex has weight \(r=R/N\).  On each component,
the one vertex omitted from the relevant endpoint image has weight one,
which is \(r+q\), where \(q=C/N=1-r\).  Consequently

\[
 y_\varepsilon^\sigma(W)
   =r|W|+q\sum_j{\bf1}[\zeta_j^\sigma(\varepsilon_j)\in W].        \tag{4.11}
\]

The inequality \(|{\cal U}|\le y_\varepsilon^\sigma(W)\), multiplied by
\(N\), is exactly (4.7), because its left-hand terminal count is integral.
For fixed \(W=N({\cal U})\), adjoining every outer vertex whose whole
neighbourhood lies in \(W\) does not change \(W\) and only strengthens the
inequality.  This proves the closure reduction (4.8), and (4.9)--(4.10)
are (4.5) written in Boolean coordinates. \(\square\)

The quantifier order is therefore

\[
 \boxed{\text{orient endpoints}\ \longrightarrow\
        \text{verify two-shore SBE}\ \longrightarrow\
        \text{choose a common basis }Q\ \longrightarrow\
        \text{choose physical/rooted representatives}.}          \tag{4.12}
\]

The common-basis distribution supplied after the second arrow is not used
to prove the first arrow.  Conversely, changing \(Q\) cannot repair a
failed endpoint inequality in (4.7).

### Theorem 4.2 (an exact orientation tail/LLL criterion)

Index the closed rows in (4.7) by \(\rho\).  For its middle-neighbour set
\(W_\rho\), put

\[
 b_\rho=|\{j:a_j,b_j\in W_\rho\}|,\qquad
 I_\rho=\{j:{\bf1}[a_j\in W_\rho]\ne
                  {\bf1}[b_j\in W_\rho]\},\qquad
 a_\rho=|I_\rho|,                                    \tag{4.13}
\]

and let \(d_\rho\) be (4.6).  Under independent fair path orientations,
the left side of row \(\rho\) has the exact law

\[
                  b_\rho+\operatorname {Bin}(a_\rho,1/2).         \tag{4.14}
\]

Define its exact failure bound

\[
 p_\rho=
 \begin{cases}
 0,&d_\rho\le b_\rho,\\[2mm]
 2^{-a_\rho}\displaystyle\sum_{i=0}^{d_\rho-b_\rho-1}
                  \binom{a_\rho}{i},
       &b_\rho<d_\rho\le b_\rho+a_\rho,\\[4mm]
 1,&d_\rho>b_\rho+a_\rho.
 \end{cases}                                         \tag{4.15}
\]

Either of the following is sufficient for a two-shore SBE orientation.

1. \(\sum_\rho p_\rho<1\).
2. There are \(x_\rho\in(0,1)\) such that
   \[
   p_\rho\le x_\rho
       \prod_{\rho'\sim\rho}(1-x_{\rho'}),          \tag{4.16}
   \]
   where \(\rho\sim\rho'\) when the two rows depend on a common path
   variable, equivalently \(I_\rho\cap I_{\rho'}\ne\varnothing\).

In particular, when

\[
 \gamma_\rho=b_\rho+a_\rho/2-d_\rho+1>0,
\]

Hoeffding gives

\[
                  p_\rho\le
       \exp\left(-{2\gamma_\rho^2\over a_\rho}\right)           \tag{4.17}
\]

for every nonconstant row.

#### Proof

A path with both terminals in \(W_\rho\) contributes one for either
orientation; a path with neither contributes zero; a path with exactly one
contributes an independent fair bit.  This proves (4.14)--(4.15).  The
first assertion is the union bound.  The second is the asymmetric Lovasz
local lemma applied to the genuinely independent path-orientation bits.
Finally failure means the binomial variable is at most
\(d_\rho-b_\rho-1\); (4.17) is the standard lower-tail Hoeffding bound.
\(\square\)

This theorem invokes product randomness only for the freely chosen path
orientations.  It makes no product-like or negative-dependence assertion
about \(Q\) or about common bases.  Its unproved all-dimensional input is
now a cut count/dependency estimate for the closed endpoint rows, rather
than an orientation-preservation claim hidden inside common-base rounding.

The exact finite boundary is sharp.  On the authenticated \(n=4\) child,
the supplied exhaustive endpoint audit finds \(7600\) of the \(2^{14}\)
labelled orientations SBE on both shores.  Four singleton bits are inert,
so intrinsically this is \(475\) of \(2^{10}\) endpoint states.  Reversing
stored path 4 or 13 alone repairs the previously stored orientation.  At
the fixed \(n=3\) forest, neither shore has an SBE orientation, although
direct common bases exist.  Hence SBE is a sufficient Boolean orientation
certificate, not a necessary condition for strict common-basis existence.
The orientation-invariance proof and finite endpoint census are recorded in
`MATH_THEOREM_R_CATALAN_EDGEWISE_ROOTED_DOUBLE_RAINBOW_EAR_AND_TWO_PARENT_GATE_20260731.md`;
the present theorem uses only their stated unoriented occurrence catalogue
and endpoint choices.
The frozen audit script/JSON hashes are

```text
4361e959059e0108aacb0828c9b63d63d69d27e54df23bbc206529619f1abd25
b48e0909321c2dbabc8cb6a10d5c4b65b9330ae87e9b73be454b7c1981a8f9bf
```

and the JSON canonical payload hash independently recomputes as
`a47f662abc6024c77ba0b0786b04199f6bb4847cb375783aad3114f0fa850647`.

### Corollary 4.3 (exact endpoint-flip absorber criterion)

For an orientation \(\varepsilon\), write the slack of row \(\rho\) as

\[
 \ell_\rho(\varepsilon)=
 \sum_j{\bf1}[\zeta_j^\sigma(\varepsilon_j)\in W_\rho]-d_\rho.
                                                               \tag{4.18}
\]

If \(J\subseteq[K]\) is a set of paths to reverse, put

\[
 \Delta_\rho(J)=\sum_{j\in J}
 \left({\bf1}[\zeta_j^\sigma(1-\varepsilon_j)\in W_\rho]
      -{\bf1}[\zeta_j^\sigma(\varepsilon_j)\in W_\rho]\right).
                                                               \tag{4.19}
\]

Then reversing precisely \(J\) gives two-shore SBE if and only if

\[
                       \ell_\rho(\varepsilon)+\Delta_\rho(J)\ge0
                       \qquad\text{for every closed row }\rho.   \tag{4.20}
\]

In particular one path flip is legal from an SBE orientation exactly when
it decreases no tight row.  From an infeasible orientation, the exact test
is still (4.20): if all negative slacks equal \(-1\), the flip must increase
every deficient row and may decrease no zero-slack row; any row of slack at
most \(-2\) rules out a one-flip repair.
Moreover every repair has Hamming size at least

\[
       \max_\rho\bigl(-\ell_\rho(\varepsilon)\bigr)_+,
\]

because one path reversal improves any fixed row by at most one.

#### Proof

Each path contributes one endpoint indicator to each row, independently
of every other path.  Reversal exchanges its two endpoint indicators, so
the change is exactly the corresponding summand of (4.19).  Substitution
in (4.7) proves (4.20). \(\square\)

Thus a bounded orientation absorber is not a common-basis exchange: it is
a set \(J\) satisfying the signed cut inequalities (4.20).  This is the
correct object for preserving SBE through a structural recursion.

### Theorem 4.4 (fractional endpoint dual and the first integral obstruction)

Index all active closed rows on both shores by \({\cal R}\), and let
\(\ell_{\rho j}(e)\in\{0,1\}\) be the contribution of path \(j\) to row
\(\rho\) when its orientation bit is \(e\).  The fractional endpoint
system interpolates independently on each path:

\[
 \sum_j\bigl((1-x_j)\ell_{\rho j}(0)
                   +x_j\ell_{\rho j}(1)\bigr)\ge d_\rho,
 \qquad 0\le x_j\le1.                                \tag{4.21}
\]

It is feasible if and only if, for every \(\lambda_\rho\ge0\),

\[
 \boxed{
 \sum_{\rho\in{\cal R}}\lambda_\rho d_\rho
 \le
 \sum_{j=1}^K\max_{e\in\{0,1\}}
       \sum_{\rho\in{\cal R}}\lambda_\rho\ell_{\rho j}(e).}    \tag{4.22}
\]

In particular, if some orientation simultaneously satisfies one upper row
with neighbour bank \(S\) and one lower row with neighbour bank \(T\), then
the catalogue necessarily obeys

\[
\begin{split}
d_-(S)+d_+(T)\le\sum_j\max\{&
 {\bf1}[b_j\in S]+{\bf1}[a_j\in T],\\
 &{\bf1}[a_j\in S]+{\bf1}[b_j\in T]\}.
                                                               \tag{4.23}
\end{split}
\]

If the signed coefficient matrix of (4.21) is totally unimodular (in
particular, if it has a network-matrix representation), then (4.22)
implies an integral SBE orientation.  Without such structure the
implication is false: the abstract endpoint constraints

\[
 x_i+x_j\ge1,\qquad (1-x_i)+(1-x_j)\ge1             \tag{4.24}
\]

on every edge of an odd triangle have the fractional solution
\(x_1=x_2=x_3=1/2\), but no Boolean solution.

#### Proof

The attainable fractional row-load vectors form the Minkowski sum

\[
 \sum_j\operatorname {conv}\{\ell_{\cdot j}(0),
                                      \ell_{\cdot j}(1)\}.
\]

This convex body meets the coordinatewise upper orthant based at
\((d_\rho)\) exactly when no nonnegative separating functional exists.
Its support function at \(\lambda\ge0\) separates path by path and is the
right side of (4.22), proving the equivalence.  Equation (4.23) is the
special choice of two unit dual weights.  Total unimodularity of the row
matrix together with the box rows makes every vertex of (4.21) integral.
Finally (4.24) forces \(x_i+x_j=1\) on every triangle edge, impossible
integrally around an odd cycle. \(\square\)

There is also a biased version of Theorem 4.2.  For independent
\(X_j\sim\operatorname {Bernoulli}(p_j)\), put

\[
 s_\rho=\mathbb E\sum_j\ell_{\rho j}(X_j)-d_\rho>0,
 \qquad
 v_\rho=|\{j:\ell_{\rho j}(0)\ne\ell_{\rho j}(1)\}|.             \tag{4.25}
\]

Then

\[
 \Pr(\rho\text{ fails})\le
             \exp(-2s_\rho^2/v_\rho).              \tag{4.26}
\]

Thus the union bound or the same variable-event LLL applies after choosing
nonuniform endpoint biases.  This is the exact probabilistic form in which
a recursive orientation invariant could be proved.  Condition (4.22), or
even all its two-row instances (4.23), remains only fractional/necessary
unless one also proves TU, a discrepancy bound, or direct elimination of
the signed odd circuits.

The physical direct-occurrence degree is

\[
 d_F^-(Y)=\sum_{x\in Y}d_F(Y-x)-2,                  \tag{4.27}
\]

with the deletion-dual formula below.  If this degree is zero, a strict
no-empty side forces the unique child edge of upper colour \(Y\) into
\(Q\).  Hence

\[
                  Z^-(F)\cup Z^+(F)\subseteq Q,\qquad
                  |Z^\pm(F)|\le K.                  \tag{4.28}
\]

At \(n=3\), the authenticated strict common bases are

\[
 E(F)-\{0\},\quad E(F)-\{1\},\quad
 E(F)-\{5\},\quad E(F)-\{11\}.                         \tag{4.29}
\]

Their intersection has eleven forced edges.  Therefore no law on the
strict common bases has all marginals \(14/15\), and the unshifted
cylinder bound fails at order one.  Contracting the core leaves
\(U_{3,4}\), whose uniform base law obeys negative cylinders.  This is why
Corollary 3.2, rather than (3.2), is the correct strict target.

## 5. Rooted-star graphic formulation

For one side forest \(J\) on its \(N\) physical owners and anchor bank
\(B\), where \(|B|=C\), add a root \(\rho\).  Then

\[
\begin{split}
&J\text{ is a }P\text{-edge forest and every component meets }B\\
&\quad\Longleftrightarrow
\exists {\cal R}_\rho\subseteq\{\rho b:b\in B\},\quad
 |{\cal R}_\rho|=N-P=C-K,\\
&\hspace{50mm}J\cup {\cal R}_\rho\text{ is a spanning tree}. \tag{5.1}
\end{split}
\]

Thus one exact side is an intersection of two palette partition bases, a
rooted graphic base, and the overlapping capacities

\[
                         d_J(v)\le1\ (v\in B),\qquad
                         d_J(v)\le2\ (v\notin B).      \tag{5.2}
\]

The graphic spanning-tree measure is determinantal and strongly Rayleigh.
This does not solve the side row: simultaneous conditioning on both
overlapping palette bases is a common-base intersection, and Theorem 2.1
shows that such intersections need not retain negative dependence.

### Theorem 5.1 (the rooted row alone is a Higgs-lift matroid)

Let \(\widehat M\) be the labelled graphic matroid on the side occurrence
ground together with the full root star \(R_\rho\).  Put

\[
                 L=\widehat M\backslash R_\rho,\qquad
                 Q_0=\widehat M/R_\rho.              \tag{5.3}
\]

Then \(Q_0\) is a quotient of \(L\).  If the augmented candidate graph is
connected and \(r(L)\ge P\), the \(K\)-th Higgs lift

\[
 \mathcal H=H^K_{Q_0,L},\qquad
 r_{\mathcal H}(X)=
 \min\{r_{Q_0}(X)+K,r_L(X)\}                         \tag{5.4}
\]

has rank \(P\), and its \(P\)-element bases are exactly the side-edge sets
which are forests and have no anchor-free component.

#### Proof

The full root star has rank \(C\), and connectedness gives

\[
 r(Q_0)=r(\widehat M)-C=N-C,\qquad (N-C)+K=P.
\]

For \(|J|=P\), equation (5.4) has value \(P\) exactly when

\[
                         r_L(J)=P,\qquad r_{Q_0}(J)=N-C.
\]

The first equality says \(J\) is a forest.  The second is equivalent to
\(r_{\widehat M}(J\cup R_\rho)=N\), which says every component of \(J\)
meets the root star.  \(\square\)

Thus the rooted topology row by itself is an honest matroid base row and
can use matroid rounding.  The full feasible shore still intersects this
Higgs base with two palette partition bases and the overlapping capacities.
It need not be matroidal: in the authenticated strict \(n=3\) fibre, two
feasible rooted shores differ by one alternating \(C_6\), while no
one-element symmetric exchange is palette-legal.  The whole three-edge
half-circuit is graphic-minimal.

### Theorem 5.2 (forest-envelope Hall class)

Fix \(N-P\) distinct root edges.  Suppose an atom subcatalogue
\(\mathcal A_0\) satisfies:

1. its physical projection is injective, and all projected edges together
   with the root edges form a forest;
2. exposing every atom of \(\mathcal A_0\) respects (5.2); and
3. its bipartite graph between the two \(P\)-element palette banks obeys
   Hall.

Then \(\mathcal A_0\) contains a perfect palette matching whose physical
lift is an anchor-capped, no-empty side forest.

#### Proof

Hall supplies a \(P\)-atom perfect palette matching \(J\).  By hypotheses
1--2, \(J\) plus the \(N-P\) root edges is a capacity-safe forest with
\(N\) edges on \(N+1\) vertices.  It is therefore a spanning tree.  Apply
(5.1).  \(\square\)

The direct occurrence degree law proves Hall in the full strict candidate
graph, not in a capacity-safe forest envelope.  Constructing two such
envelopes for one rounded common \(Q\) remains an additional exact row.

## 6. Galois-closed reformulation of the Hall tail

Let

\[
 X=\binom{[2n]}n,\qquad Y=\binom{[2n]}{n+2},
\]

with containment incidence.  For a closed cut

\[
 A=A_T=\{x:N(x)\subseteq T\},\qquad T=N(A),
\]

put

\[
 H=Y\setminus T,\qquad B=X\setminus A.              \tag{6.1}
\]

Fix one shore \(\sigma\), its terminal bank \(E_\sigma\subset X\), and
the endpoint-image bijection

\[
              \tau_\sigma:E(F)\longrightarrow X\setminus E_\sigma.
\]

For \(Q\subseteq E(F)\), write \(Q_\sigma=\tau_\sigma(Q)\) and
\(D_\sigma=X\setminus Q_\sigma\).  This notation is essential: the edge
set \(Q\) and its shore-specific middle image are different objects.

### Theorem 6.1 (Galois pair and random-omission law)

\[
                    B=N(H),\qquad
                    H=\{y:N(y)\subseteq B\}.          \tag{6.2}
\]

Thus closed cuts are exactly Galois-closed two-step Boolean pairs.  Put

\[
 b=|B|,\qquad z=|H|,\qquad
 h_\sigma=|E_\sigma\cap B|,\qquad d=b-z.
\]

For a uniform unconditioned \(C\)-subset \(Q\subseteq E(F)\),

\[
 Z_{B,H}^\sigma:=|Q_\sigma\cap B|
 \sim\operatorname {Hypergeom}(N,b-h_\sigma,C),      \tag{6.3}
\]

and this cut violates Hall exactly when

\[
                              Z_{B,H}^\sigma\ge d+1.   \tag{6.4}
\]

#### Proof

An \(x\) lies outside \(A_T\) exactly when it has a neighbour outside
\(T\), giving \(B=N(H)\).  A \(y\) lies outside \(T=N(A)\) exactly when
none of its rank-\(n\) facets lies in \(A\), giving the second equality.
Also \(D_\sigma=X\setminus Q_\sigma\), so

\[
 |D_\sigma\cap B|=b-Z_{B,H}^\sigma.
\]

The complement form of Hall is \(|D_\sigma\cap B|\ge z\), which is
equivalent to (6.4).  The bijection \(\tau_\sigma\) maps uniform \(Q\) to a
uniform \(C\)-subset of the \(N\) nonterminal middle vertices, giving
(6.3).  The opposite shore uses its coupled opposite terminal bank, but
the same statement applies shore by shore.
\(\square\)

## 7. Exact KK threshold gap

Assume \(n\ge4\).  Return to \(k=|A|\),
\(e=|E_\sigma\cap A|\), \(t=|T|\), and define \(x\) by

\[
                         k=\binom{x}{n},\qquad
                         g(k)=\binom{x}{n-2}.          \tag{7.1}
\]

The shore-specific retained load has the exact law

\[
 |D_\sigma\cap A|
   \mathrel{\overset{d}{=}}e+\operatorname {Hypergeom}(N,k-e,R),
\]

and Hall fails on this cut when the hypergeometric term is at least
\(t-e+1\).

Lovász--Kruskal--Katona gives \(t\ge g(k)\).  Put

\[
 \Psi(k)=g(k)-rk-qK,\qquad \delta_{\rm KK}=t-g(k).
\]

### Theorem 7.1 (four-term threshold decomposition, \(n\ge4\))

For \(k\ge K\), the Hall threshold in the retained-set formulation exceeds
its hypergeometric mean by exactly

\[
\boxed{
 (t-e+1)-r(k-e)
 =\Psi(k)+\delta_{\rm KK}+q(K-e)+1.
}                                                       \tag{7.2}
\]

Every term on the right is nonnegative, and

\[
 \Psi(k)\ge {M-k\over N}\bigl(g(K)-K\bigr),            \tag{7.3}
\]
\[
 g(K)-K=(2+o(1)){K\log_2 n\over n}.                   \tag{7.4}
\]

For \(k<K\), Hall failure is deterministically impossible.

#### Proof

Identity (7.2) is direct expansion using \(q=1-r\).  The function \(g\) is
concave.  Since

\[
 \Psi(M)=0,\qquad \Psi(K)=g(K)-K>0,
\]

where the strict inequality for \(n\ge4\) is equivalent to

\[
 K<\binom{2n-2}{n}
 \quad\Longleftrightarrow\quad n^2-4n+1>0,
\]

it lies above the chord between these endpoints, proving (7.3).  For
(7.4), write \(x=2n-\delta\) in (7.1) at \(k=K=M/(n+1)\).
Logarithmic differentiation of \(\binom{x}{n}\) gives

\[
                         \delta=(1+o(1))\log_2 n.
\]

Substitution in

\[
 {g(K)\over K}
 ={n(n-1)\over(x-n+1)(x-n+2)}
\]

gives (7.4).  If \(k<K\), the small-family shadow inequality gives
\(t\ge k\), while the sampled load never exceeds \(k\).  \(\square\)

Thus a dangerous cut must simultaneously be near equality in KK, nearly
contain the fixed shore endpoint bank \(E_\sigma\), and lie sufficiently
close to the global cut.

## 8. Spectral extremals

The normalized rank-\(n\)/rank-\((n+2)\) inclusion operator has

\[
 \sigma_1^2={n-2\over n+2},\qquad
 \sigma_2^2={(n-2)(n-3)\over(n+2)(n+1)}.             \tag{8.1}
\]

### Theorem 8.1 (cross-independent density bound, \(n\ge4\))

Put

\[
                         \alpha=|A|/M,\qquad \tau=|T|/P.
\]

Then

\[
                  \tau\ge{(n+2)\alpha\over n-2+4\alpha}.            \tag{8.2}
\]

Apart from empty/full cuts, equality holds exactly for a coordinate star

\[
 A_i=\{x:i\in x\},\qquad T_i=\{y:i\in y\}.            \tag{8.3}
\]

#### Proof

There are no incidence edges from \(A\) to \(Y\setminus T\).  Expander
mixing and the first nontrivial singular value give

\[
 \alpha(1-\tau)\le\sigma_1^2(1-\alpha)\tau,
\]

which rearranges to (8.2).  Equality forces both centered indicators into
the first Johnson eigenspaces.  Hence \(1_A\) is affine in the coordinate
indicators on the middle slice.  A swap of two coordinates shows that a
Boolean affine function on a fixed-weight slice is constant, one coordinate
indicator, or its complement.  The complement has \(N(A)=Y\), leaving
(8.3) as the only proper equality case.  \(\square\)

The gap to the next eigenspace is only

\[
 \sigma_1^2-\sigma_2^2
 ={4(n-2)\over(n+1)(n+2)}=\Theta(1/n).               \tag{8.4}
\]

Therefore exact equality classification does not itself count the
near-equality cuts.

### Theorem 8.2 (coordinate-star tails are negligible)

For (8.3),

\[
 k=M/2,\qquad t={n-1\over2(n+1)}M,
\]
\[
 b=M/2,\qquad z={n-2\over2n}P,\qquad
 d=b-z={3n\over(n+1)(n+2)}M.                         \tag{8.5}
\]

The mean in (6.3) is at most

\[
 \mu_{\max}=qM/2={2n+1\over n(n+2)}M,
\]

so \(d/\mu_{\max}\to3/2\).  Hence

\[
 \Pr(Z_{B,H}^\sigma\ge d+1)
 \le\exp\left[-\bigl(3\log(3/2)-1-o(1)\bigr)K\right].               \tag{8.6}
\]

There are only \(2n\) coordinate stars, so their total contribution is
\(o(1)\).  The two-coordinate stars

\[
 A_{ij}=\{x:\{i,j\}\subseteq x\}
\]

have \(|A_{ij}|=|N(A_{ij})|=\binom{2n-2}{n}\) and are deterministically
Hall-safe.

#### Proof

The counts in (8.5) follow by coordinate incidence and the binomial ratios
in (1.1).  Apply the hypergeometric Chernoff exponent
\(\mu[(1+\delta)\log(1+\delta)-\delta]\); after division by \(K\), its
limit is \(3\log(3/2)-1\).  The final assertion has threshold equal to the
entire family size.  \(\square\)

## 9. Exact remaining container theorem

For a closed cut define

\[
 \mu_T=r(k-e),\qquad \Gamma_T=(t-e+1)-\mu_T,
\]

\[
 I(T)=\mu_T\left[
 \left(1+{\Gamma_T\over\mu_T}\right)
 \log\left(1+{\Gamma_T\over\mu_T}\right)
 -{\Gamma_T\over\mu_T}\right],                       \tag{9.1}
\]

with \(I(T)=\infty\) when the threshold exceeds the population support.
The hypergeometric Chernoff bound gives

\[
                         \Pr(T\text{ violates Hall})\le e^{-I(T)}. \tag{9.2}
\]

### Hypothesis 9.1 (rate-container bound)

There exist \(\eta>0\) and \(u_n\to\infty\) such that every proper
contributing closed cut has \(I(T)\ge u_n\), and for every dyadic
\(u\ge u_n\),

\[
 \#\{T=N(A_T):u\le I(T)<2u\}
 \le\exp((1-\eta)u).                                  \tag{9.3}
\]

Then the closed-cut union sum denoted (6.16) in
`THREAD_A_CATALAN_TWO_COORDINATE_COMMON_Q_AND_PUNCTURED_FOREST_NIBBLE_20260731.md`
is \(o(1)\).

#### Proof

In a dyadic rate class, (9.2) makes the total contribution at most
\(\exp(-\eta u)\).  Summing over dyadic \(u\ge u_n\) tends to zero.
\(\square\)

By (7.2), the threshold gap is exactly the sum of the three nonconstant
quantities

\[
                         \Psi(k),\qquad
                         \delta_{\rm KK},\qquad K-e                  \tag{9.4}
\]

together with one.  Hence a low-rate cut can occur only when this sum is
small enough relative to its varying hypergeometric mean in (9.1).  No
componentwise equivalence is asserted.  Thus the remaining closed-cut
theorem is a quantitative stability/container theorem for Galois-closed
two-step Boolean pairs that are simultaneously near KK equality and nearly
contain the fixed endpoint bank.

Scalar KK gives the threshold but not the count.  The spectral theorem
classifies exact equality, but its \(\Theta(1/n)\) eigengap does not imply
(9.3).  The strict occurrence and rooted-star conditions are downstream
physical rows and impose no proved restriction on the unrestricted closed
cuts.

## 10. Precise proved/conditional boundary

The following are proved.

1. Generic strongly-Rayleigh and balanced-matroid arguments cannot be
   applied after intersecting the two common-base supports.
2. Matroidal exchange of the actual Boolean common bases would imply the
   full cylinder estimate by swap rounding.
3. For a fixed unoriented forest, simultaneous strict SBE is exactly the
   endpoint Boolean cut system (4.7); the random-orientation tail/LLL
   criterion in Theorem 4.2 is rigorous and independent of \(Q\).
4. In the strict direct catalogue, forced-core contraction and shifted
   cylinders are necessary in general and sufficient under the explicit
   local intensity bounds.
5. Rooted graphic feasibility has an exact forest-envelope Hall sufficient
   class.
6. Uniform closed cuts have the Galois normal form, four-term KK gap and
   spectral classification above; all coordinate-star extremals are
   harmless.

The smallest unproved alternatives are:

* prove Boolean common-base exchange (3.1), or a bounded-circuit rounding
  theorem with the same cylinder consequence; or
* prove the rate-container estimate (9.3).

For strict recursive preservation there is a preceding, logically separate
alternative: prove the endpoint-orientation cut tail (4.15)--(4.16) for the
produced path forests.  This establishes SBE and only then exposes the
balanced common-base face.

Even either result gives the asymptotic \(P-o(P)\) common-\(Q\) side
forest, not the exact zero-leave side theorem.  Exact recursion still
requires strict representatives or unrestricted physical diamonds,
rooted-star/attachment topology, and downstream residence/shadow/compiler
rows.

## 11. Adversarial audit

1. The four-element obstruction is an abstract transversal intersection,
   not a counterexample inside the Boolean Catalan family.
2. Individual representability or strong Rayleighness is never transferred
   through support intersection.
3. Theorem 3.1 assumes a new Boolean-specific exchange axiom; it does not
   infer it from uniform density.
4. The strict \(n=3\) forced core concerns the direct-edge/no-empty family,
   not the unrestricted common bases.
5. Equation (4.3) is a failure of the degree-count proof, not a proof that
   a random strict bank is infeasible.
6. The random bits in Theorem 4.2 orient paths; they are not common-basis
   indicators.  No concentration statement for \(Q\) is smuggled through
   that theorem.
7. The \(n=4\) count is finite evidence for feasibility of the endpoint
   system, not an all-dimensional orientation theorem; the \(n=3\) failure
   proves SBE is not necessary.
8. The rooted-star graphic measure is not conditioned on both palettes
   under any claimed stability theorem.
9. The spectral theorem classifies equality only.  No quantitative FKN or
   container estimate is assumed.
10. Hypothesis 9.1 remains explicitly unproved.
