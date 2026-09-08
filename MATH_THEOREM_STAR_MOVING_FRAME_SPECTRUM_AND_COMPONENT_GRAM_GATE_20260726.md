# Star moving frames: exact target spectrum and the integral component-Gram gate

Date: 2026-07-26

Method: pure mathematics only.  The valid recursive context-array factor is
taken as the local input.  No computation, search, solver, or web result is
used.

## 0. Verdict

Put \(n=2m\).  There is a minimum-size connected transposition catalogue

\[
 {\cal S}_\star=\{(1\ n),(2\ n),\ldots,(n-1\ n)\}.                \tag{0.1}
\]

It has \(n-1=2m-1\) moves and uses at most \(n\) physical frames after the
base frame is included.  On every target layer
\(\binom{[n]}k\), simultaneously for all \(1\le k\le n-1\), its normalized
frame operator

\[
 P_\star={1\over n-1}\sum_{i<n}\rho_k((i\ n))                    \tag{0.2}
\]

has constants as its only fixed vectors and has exact spectral gap

\[
                         \boxed{\gamma_\star={1\over n-1}.}      \tag{0.3}
\]

The fair component-heat midpoint is

\[
                         K_\star={I+P_\star\over2}               \tag{0.4}
\]

and has exact gap \(1/(2(n-1))\).  Every realization of this heat is an
integral exact factor: on each overlay component one takes all cycles from
one of the two frames.  No cycle is cut, no new seam is introduced, and one
common choice serves every signed depth.

This supplies the requested sparse, all-harmonic spectral catalogue.  It
does **not** by itself supply integral discrepancy descent.  If \(a\) and
\(b=\rho_k(\tau)a\) are the two target-load vectors and their common-owner
overlay has components \(C\), put

\[
                         d_C=a_C-b_C.                            \tag{0.5}
\]

Fair independent integral component choices obey the exact floor-energy
identity

\[
 \boxed{
 \mathbb E Q(z)-Q(a)
 ={1\over4}\left(\sum_C\|d_C\|_2^2-\Big\|\sum_Cd_C\Big\|_2^2\right)
 =-{1\over2}\sum_{C<D}\langle d_C,d_D\rangle .}                 \tag{0.6}
\]

Thus the target spectral gap controls \(\|\sum_Cd_C\|_2^2\), whereas
integral heat also pays \(\sum_C\|d_C\|_2^2\).  A single overlay component
replenishes the spectral gain exactly.  More generally, spectrum alone
gives no sign to (0.6).  The exact missing theorem is a positive joined
component-Gram estimate, not another target-module expansion estimate.

There are two complementary sharpness statements.

* Among catalogues made of transpositions, every connected catalogue has
  at least \(n-1\) moves, and no such averaging operator has gap larger
  than \(2/(n-1)\).  The star is minimum-size and is within a factor two of
  the optimal gap; the complete transposition catalogue attains the upper
  bound.
* A one-step exact uniformizer on the central target layer needs at least
  \(\binom n{n/2}\) coordinate frames.  Hence a sparse catalogue can mix
  only by iteration; it cannot be an exact one-shot design.

The proved boundary is therefore precise.  Sparse fractional mixing is
closed, as is componentwise integrality.  Their composition requires the
cross-component inequality displayed in Section 7 below.  Without it, a
spectral proof of simultaneous integral all-depth rounding is invalid.

## 1. Target modules and moving frames

For \(0\le k\le n\), let

\[
                 V_k=\mathbb R^{\binom{[n]}k}                     \tag{1.1}
\]

with the orthonormal coordinate basis indexed by the \(k\)-sets.  The
coordinate action is

\[
                 (\rho_k(\sigma)f)(T)=f(\sigma^{-1}T).           \tag{1.2}
\]

Fix any exact recursive context-array factor \(F\) on one common owner
universe.  At a signed depth \(j=(q,\epsilon)\), write

\[
 a_j(T)=\#\{\hbox{owner starts of }F\hbox{ whose }j\hbox{-target is }T\}.
                                                                    \tag{1.3}
\]

Coordinate conjugation is literal, so

\[
                 a_j(\sigma F)=\rho_{m+\epsilon q}(\sigma)a_j(F).
                                                                    \tag{1.4}
\]

The local context array and its trace decoder are transported with the
cycle.  In particular (1.4) holds at all depths at once; there is no
depthwise choice.

For \(i<n\), put \(s_i=(i\ n)\) and \(F_i=s_iF\).  The moving catalogue
consists of the \(n-1\) moves \(s_i\), or equivalently the at most \(n\)
frames

\[
                         F,F_1,\ldots,F_{n-1}.                    \tag{1.5}
\]

All are exact factors with the same cycle lengths and the same number of
cycles.

## 2. Exact spectrum of the star catalogue

Let \(r=\min(k,n-k)\).  The permutation module on \(k\)-sets has the
multiplicity-free decomposition

\[
                         V_k=\bigoplus_{j=0}^{r}S^{(n-j,j)}.      \tag{2.1}
\]

The operator \((n-1)P_\star\) is the Jucys--Murphy element

\[
                         J_n=\sum_{i<n}(i\ n).                   \tag{2.2}
\]

In the standard-tableau basis of \(S^\lambda\), \(J_n\) has eigenvalue
equal to the content, column minus row, of the box occupied by \(n\).
For \(\lambda=(n-j,j)\), that box must be one of the removable corners.
Consequently the complete spectrum of \(P_\star\) on \(V_k\) is

\[
\begin{array}{c|c|c}
\hbox{corner}&\hbox{eigenvalue}&\hbox{multiplicity}\ \\ \hline
j=0&1&1\\[2mm]
\hbox{end of row 1}&{n-j-1\over n-1}
 &f^{(n-j-1,j)}\quad(1\le j\le r,\ j<n/2),\\[2mm]
\hbox{end of row 2}&{j-2\over n-1}
 &f^{(n-j,j-1)}\quad(1\le j\le r).
\end{array}                                                       \tag{2.3}
\]

Here

\[
                 f^{(a,b)}={a-b+1\over a+1}\binom{a+b}{b}       \tag{2.4}
\]

is the number of standard tableaux of two-row shape \((a,b)\).  When
numeric eigenvalues in (2.3) coincide, their displayed multiplicities are
added.

For completeness, the two standard representation facts used above admit
the following short proofs.  The inclusion maps between consecutive subset
layers give the orthogonal harmonic decomposition; the new part appearing
at level \(j\) has dimension

\[
                         \binom nj-\binom n{j-1}=f^{(n-j,j)},     \tag{2.5}
\]

which is the two-row module \(S^{(n-j,j)}\), proving (2.1).  For (2.2),
successively restricting a standard tableau from \(S_n\) to \(S_{n-1}\)
is multiplicity free.  The sum of transpositions \(J_n\) commutes with
\(S_{n-1}\), hence is scalar on each restriction summand.  Subtracting the
central transposition sums of \(S_n\) and \(S_{n-1}\) gives that scalar as
the content of the removed box.  This proves (2.3).

For \(n\ge4\), every nonconstant eigenvalue in (2.3) has absolute value at
most

\[
                         {n-2\over n-1},                         \tag{2.6}
\]

and equality occurs in the \((n-1,1)\) summand.  This proves (0.3), both
as a Poincare gap and as an \(L^2\) contraction gap.  Applying the affine
map \(x\mapsto(1+x)/2\) to (2.3) proves the gap assertion for \(K_\star\).

Because every central signed layer \(k=m\pm q\), \(q<m\), contains the
\((n-1,1)\) summand, these gaps are exact simultaneously at every protected
depth.  On the direct sum of any number of signed layers, with arbitrary
positive layer weights, the gap is unchanged.

## 3. Optimality among transposition catalogues

Let \(E\subseteq\binom{[n]}2\), and average the corresponding coordinate
transpositions:

\[
                         P_E={1\over |E|}\sum_{uv\in E}\rho((uv)).
                                                                    \tag{3.1}
\]

Regard \(E\) as the edge set of a graph \(G\) on \([n]\).  On the
one-coordinate module \(V_1\), direct calculation gives

\[
                         I-P_E={L_G\over |E|},                    \tag{3.2}
\]

where \(L_G\) is the ordinary graph Laplacian.  Hence a positive gap on
every nonconstant target harmonic forces \(G\) to be connected and thus

\[
                         |E|\ge n-1.                              \tag{3.3}
\]

Moreover, the sum of the \(n-1\) nonzero Laplacian eigenvalues is
\(2|E|\), so

\[
 \operatorname {gap}(P_E)
 \le {\lambda_2(L_G)\over |E|}
 \le {2\over n-1}.                                                \tag{3.4}
\]

For the star, \(\lambda_2(L_G)=1\) and \(|E|=n-1\), which recovers
\(1/(n-1)\).  For the complete graph,
\(\lambda_2(L_G)=n\) and \(|E|=\binom n2\), so (3.4) is attained.

Indeed, the complete-transposition operator is central and on harmonic
degree \(j\) has eigenvalue

\[
                 1-{j(n-j+1)\over\binom n2}.                     \tag{3.5}
\]

Its exact nonconstant gap is \(2/(n-1)\).  Thus the linear star catalogue
loses only a factor two in gap relative to the best possible
transposition average and uses the least possible number of moves.

## 4. Fractional simultaneous all-depth contraction

Suppose the target-load vector at each signed depth has total mass \(W\),
and set

\[
 N_j=\binom n{m+\epsilon q},\qquad
 \lambda_j={W\over N_j},\qquad
 h_j=a_j-\lambda_j{\bf1}.                                      \tag{4.1}
\]

Then \(h_j\perp{\bf1}\), and after \(t\) star-frame convolution layers,

\[
                         \|P_\star^th_j\|_2
 \le \left(1-{1\over n-1}\right)^t\|h_j\|_2.                  \tag{4.2}
\]

Since \(\lambda_j\ge1\), the fractional missing unit demand satisfies

\[
\begin{aligned}
 D_j(t)
 &=\sum_T\bigl(1-(\lambda_j{\bf1}+P_\star^th_j)(T)\bigr)_+\\
 &\le \sqrt{N_j}\left(1-{1\over n-1}\right)^t\|h_j\|_2.
\end{aligned}                                                    \tag{4.3}
\]

Consequently, for both signs and all \(1\le q\le H\),

\[
 \boxed{
 \sum_{q\le H,\epsilon}D_{q,\epsilon}(t)
 \le \left(1-{1\over n-1}\right)^t
 \sum_{q\le H,\epsilon}\sqrt{N_{q,\epsilon}}\|h_{q,\epsilon}\|_2.}
                                                                    \tag{4.4}
\]

This is one common convolution; the depths are not rounded separately.

A completely assumption-free bound follows from nonnegativity and total
mass \(W\):

\[
                         \|h_j\|_2\le W,qquad N_j\le W.         \tag{4.5}
\]

Thus the right side of (4.4) is at most

\[
                         2H W^{3/2}e^{-t/(n-1)}.                  \tag{4.6}
\]

For any \(\omega(n)\to\infty\), it is at most \(W/\omega(n)\) once

\[
 t\ge(n-1)\left({1\over2}\log W+\log(2H\omega(n))\right).       \tag{4.7}
\]

For polynomial \(H\), this is

\[
                         t=\left({\log2\over2}+o(1)\right)n^2.   \tag{4.8}
\]

Fair component heat uses \(K_\star\) rather than \(P_\star\), so the same
worst-case estimate holds with the right side of (4.7) multiplied by two.

Equations (4.4)--(4.8) are fractional statements.  The convolution is an
exact rational multicover supported on words in the \(n-1\) star moves;
it is not one integral factor.

## 5. Why a sparse one-step exact design is impossible

Let \(\mu\) be a probability measure supported on \(s\) coordinate
permutations.  Suppose its operator on the central layer is the exact
uniform projection:

\[
                         \sum_g\mu(g)\rho_m(g)={J\over W},       \tag{5.1}
\]

where \(J\) is the all-one matrix.  Fix a central set \(X\).  The row of
the left side indexed by \(X\) is supported on at most the \(s\) sets
\(gX\), while the corresponding row of \(J/W\) is positive on all \(W\)
central sets.  Therefore

\[
                         \boxed{s\ge W.}                         \tag{5.2}
\]

In particular, if \(H\le S_n\) is a subgroup and one averages exactly
over \(H\), absence of nonconstant fixed vectors on the central layer
forces \(H\) to be transitive there, whence again

\[
                         |H|\ge W.                               \tag{5.3}
\]

So coset or subgroup averaging cannot give a subexponential one-shot exact
uniformizer.  Iterated sparse spectral mixing and one-step exact design are
genuinely different mechanisms.

## 6. Integral component choices and exact legality

Fix one move \(\tau\in{\cal S}_\star\).  Superpose the two exact
equal-cycle-length factors \(F\) and \(\tau F\) on their common owner
universe.  A connected component of the union contains every whole cycle
of either factor which meets it.  Consequently one may, independently on
each component, retain either all \(F\)-cycles or all \(\tau F\)-cycles.

Every resulting object is again an exact factor:

1. every owner belongs to exactly one selected cycle;
2. every selected cycle is a literal old cycle, so all recurrence and
   trace guarantees are unchanged;
3. all signed depths use the same component choice;
4. no cycle is spliced, so the cycle count and the run/seam ledger do not
   increase.

The equal-cycle-length hypothesis implies that each overlay component
contains the same number of cycles from the two shores.  Thus even the
componentwise cycle count is unchanged.

This legality statement requires a common exact owner universe.  A partial
atlas and a conjugate partial atlas usually have different owner leaves;
their overlay cannot be rounded by this argument until the leaves have a
common exact completion.  This is an owner constraint, not a spectral one.

There is an exact warning at the coarser pair-status level.  Let \(M\) be
the perfect matching underlying the base coordinate frame, and let \(p\)
be its fixed-point-free involution.  The union of the star-conjugate
matchings

\[
                         M\cup\bigcup_{i<n}s_iM                  \tag{6.1}
\]

contains every edge \(\{n,x\}\).  For \(x=p(n)\), this is the base edge.
For every other \(x\), conjugating \(M\) by
\(s_{p(x)}=(p(x)\ n)\) sends the edge \(\{p(x),x\}\) to
\(\{n,x\}\).  Thus (6.1) is connected.

The exclusion graph of a connected coordinate graph is connected on every
nontrivial fixed-cardinality layer: along a spanning tree, move occupied
coordinates one edge at a time to a fixed canonical set.  Consequently the
common pair-status support of the star catalogue on the middle layer is
one global component.  If the allowed integral variables are only whole
pair-status shores, the star catalogue is therefore globally locked and
(0.6) has \(\Xi={\cal D}\).  The only possible escape within the present
catalogue is that the **finer exact cycle-factor overlay** splits this
global pair-status support and has positive joined cross-Gram.  Pair-status
connectivity alone neither proves nor rules out that finer splitting.

## 7. The exact component-Gram obstruction

We now prove (0.6), including the floor baseline.  Fix one signed layer and
write \(a=\sum_Ca_C\), \(b=\sum_Cb_C\), where \(a_C,b_C\) are the target
loads contributed by the common owner set of overlay component \(C\).  Put

\[
                 d_C=a_C-b_C,qquad d=a-b=\sum_Cd_C.             \tag{7.1}
\]

Choose independent fair signs \(\varepsilon_C\).  The integral output is

\[
 z={a+b\over2}+{1\over2}\sum_C\varepsilon_Cd_C.                 \tag{7.2}
\]

Let \(c=\lfloor W/N\rfloor\).  For an integral load vector of total \(W\),
define its exact floor/ceiling excess

\[
                         Q(z)=\sum_T(z_T-c)(z_T-c-1).             \tag{7.3}
\]

Every summand is nonnegative.  It vanishes exactly at \(c,c+1\), and a
missing target contributes \(c(c+1)\).  Hence

\[
                         \#\{T:z_T=0\}\le {Q(z)\over c(c+1)}.    \tag{7.4}
\]

If \(\theta=W/N-c\), then, because the total load is fixed,

\[
                         Q(z)=\|z-(W/N){\bf1}\|_2^2
                                  -N\theta(1-\theta).            \tag{7.5}
\]

The subtracted term is constant under every component choice.  Taking the
square in (7.2) and using independence of the signs gives

\[
 \mathbb E Q(z)
 =\left\|{a+b\over2}-{W\over N}{\bf1}\right\|_2^2
   +{1\over4}\sum_C\|d_C\|_2^2-N\theta(1-\theta).               \tag{7.6}
\]

Coordinate relabeling gives \(Q(a)=Q(b)\).  The parallelogram identity
therefore gives

\[
 Q(a)=\left\|{a+b\over2}-{W\over N}{\bf1}\right\|_2^2
       +{1\over4}\|d\|_2^2-N\theta(1-\theta).                   \tag{7.7}
\]

Subtracting (7.7) from (7.6) proves (0.6).

The formula adds over all signed depths, with arbitrary nonnegative layer
weights.  In particular it is already a simultaneous all-\(q\) identity.

Average now over \(\tau\in{\cal S}_\star\).  With

\[
\begin{aligned}
 {\cal D}(a)&={1\over n-1}\sum_\tau\|a-\rho(\tau)a\|_2^2,\\
 \Xi(a)&={1\over n-1}\sum_\tau\sum_{C\in{\cal C}_\tau}
                  \|d_{\tau,C}\|_2^2,
\end{aligned}                                                    \tag{7.8}
\]

one fair integral star-heat step satisfies exactly

\[
                         \mathbb E Q_{\rm new}
 =Q_{\rm old}-{1\over4}\bigl({\cal D}(a)-\Xi(a)\bigr).          \tag{7.9}
\]

The spectral theorem gives, for the centered raw energy,

\[
                         {\cal D}(a)\ge {2\over n-1}
                         \left\|a-{W\over N}{\bf1}\right\|_2^2.
                                                                    \tag{7.10}
\]

But it gives no upper bound on \(\Xi(a)\).  A sufficient quantitative
component theorem would be

\[
                         \boxed{\Xi(a)\le(1-\kappa){\cal D}(a)}  \tag{7.11}
\]

for some useful \(\kappa>0\), after summing the protected layers.  Under
(7.11), one step removes at least

\[
                 {\kappa\over2(n-1)}
                 \left\|a-{W\over N}{\bf1}\right\|_2^2         \tag{7.12}
\]

from expected floor energy.  Conversely:

* if the overlay has one component, then \(\Xi={\cal D}\) and the heat is
  exactly energy-flat;
* if the component differences are mutually orthogonal, again
  \(\Xi={\cal D}\);
* negative joined cross-Gram makes \(\Xi>{\cal D}\) and heat increases
  the expected energy.

Thus (7.11), or an equivalent state-adaptive signed version, is the exact
additional statement needed to convert the star spectrum into an integral
contraction theorem.

## 8. Global-frame rounding cannot use the gap

There is a particularly simple obstruction if component recombination is
not used.  Every word \(g\) in the star moves produces merely the conjugate
factor \(gF\).  Both the number of missing targets and the floor energy are
coordinate-relabeling invariants:

\[
                         Q(\rho(g)a)=Q(a),\qquad
 \#\{T:(\rho(g)a)(T)=0\}=\#\{T:a(T)=0\}.                         \tag{8.1}
\]

Hence no integral selection of one frame word improves either statistic,
even though their fractional average converges to the constant load by
Section 4.

More quantitatively, if a random integral rule is supported only on global
conjugates and has fractional mean \(\bar a\), then

\[
 \mathbb E\|a_{\rm int}-(W/N){\bf1}\|_2^2
 =\|a-(W/N){\bf1}\|_2^2,                                      \tag{8.2}
\]

while

\[
 \operatorname {Var}(a_{\rm int})
 =\|a-(W/N){\bf1}\|_2^2
  -\|\bar a-(W/N){\bf1}\|_2^2.                                \tag{8.3}
\]

The rounding variance replenishes exactly all fractional spectral descent.
Equation (0.6) is the componentwise refinement of this identity.

## 9. Proved boundary

The following are now unconditional.

1. A linear-size exact moving-frame catalogue has a spectral gap on every
   nonconstant harmonic of every protected target rank.
2. Its exact spectrum, multiplicities, optimum transposition-gap scale, and
   worst-case fractional all-depth mixing time are known.
3. Every pairwise component realization remains an integral exact factor
   and creates no cycle or seam cost.
4. A sparse one-step exact uniform design is impossible.
5. Fractional spectral contraction does not imply integral descent.  The
   discrepancy between the two is exactly the joined component Gram in
   (0.6), with the correct floor/ceiling baseline.

Accordingly, a proof of coefficient one through this catalogue must establish
(7.11), or a stronger deterministic discrepancy selection, for the actual
recursive context-array overlays.  If those overlays have one giant component
on the charged mass, (0.6) is a complete spectral no-go for this route.  If
they have many components, their cross-Gram signs and sizes—not the target
harmonic gap—are the remaining data to compute.
