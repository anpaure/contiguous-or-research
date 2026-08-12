# Exact branching law for the Greene--Kleitman middle projection

This note audits the middle projection from
`GK_TWO_SIDED_RAINBOW_FOREST.md` against the shift-compatible SCD target in
Section 10 of `PARTIAL_BLOCK_MULTISCALE.md`.  The Greene--Kleitman projection
is not merely a slightly branching version of the desired permutation: its
indegree distribution is asymptotically geometric and it lowers SCD radius
on every non-root edge.  A former claim that linearization requires deleting
asymptotically half of its edges was false and is retracted in Section 3.
The exact replacement is the rooted-tree DP in
`MATH_CORRECTION_GK_PROJECTION_LINEAR_SUBFOREST_TREE_DP_20260731.md`; no
asymptotic edit bound is claimed here.

Throughout, the dimension is `2m` and

\[
 W=\binom{2m}{m},\qquad
 K=\operatorname {Cat}_m=\frac{W}{m+1}.
\]

The projection forest has `W-K` edges.

## 1. Dyck-factor normal form

Regard `0` as an opening parenthesis and `1` as a closing parenthesis.  Apply
the usual noncrossing parenthesis matching.  A middle word in a
Greene--Kleitman chain of radius `d` has exactly `d` unmatched `1`s followed
by `d` unmatched `0`s, and has a unique factorization

\[
 D_0\,1\,D_1\,1\cdots 1\,D_d\,0\,D_{d+1}\,0\cdots
       0\,D_{2d},                                      \tag{1.1}
\]

where every `D_i` is a Dyck word.  The total semilength of the Dyck factors
is `m-d`.  Consequently the number of radius-`d` chains is

\[
 V_d=[x^{m-d}]C(x)^{2d+1}
 =\binom{2m}{m-d}-\binom{2m}{m-d-1},                   \tag{1.2}
\]

where

\[
 C(x)=1+xC(x)^2
\]

is the Catalan generating function.

The Greene--Kleitman middle projection switches the two central unmatched
letters in (1.1):

\[
 1\,D_d\,0\quad\longmapsto\quad 0\,D_d\,1.            \tag{1.3}
\]

The target has radius `d-1`.  Its central Dyck factor is

\[
 H=D_{d-1}\,(0D_d1)\,D_{d+1}.                          \tag{1.4}
\]

This proves at once that the projection lowers the SCD radius by one on every
non-singleton chain.  In particular it has no radius-preserving edge.

## 2. Exact indegree theorem

### Theorem 1

For `0<=j<=m`, the number of middle sets of indegree exactly `j` in the
oriented Greene--Kleitman projection forest is

\[
 \boxed{A_{m,j}=\binom{2m-j-1}{m-j}}.                  \tag{2.1}
\]

Equivalently, for `1<=t<=m`,

\[
 \boxed{\#\{X:\deg^-(X)\ge t\}
       =\binom{2m-t}{m-t}}.                            \tag{2.2}
\]

#### Proof

Consider a target of radius `d-1`.  Reversing (1.3) means choosing one
primitive component `0D1` of its central Dyck factor `H`; the factors before
it become `D_{d-1}`, the interior becomes `D_d`, and the factors after it
become `D_{d+1}`.  Hence its indegree is exactly the number of primitive
components of `H`.

A Dyck word with exactly `j` primitive components has generating function

\[
 (xC(x))^j.
\]

The other `2d-2` Dyck factors are unrestricted.  Therefore, for `j>=1`, the
number of radius-`d-1` targets of indegree `j` is

\[
 [x^{m-d+1-j}]C(x)^{2d-2+j}.                           \tag{2.3}
\]

Summing (2.3) over `d`, and putting `n=m-d+1-j`, gives

\[
 A_{m,j}
 =\sum_{n=0}^{m-j}[x^n]C(x)^{2m-j-2n}.                 \tag{2.4}
\]

The standard Lagrange-inversion identity

\[
 [x^n]C(x)^a=\frac{a}{2n+a}\binom{2n+a}{n}             \tag{2.5}
\]

turns the summand into

\[
 \frac{2m-j-2n}{2m-j}\binom{2m-j}{n}
 =\binom{2m-j-1}{n}-\binom{2m-j-1}{n-1}.               \tag{2.6}
\]

The sum telescopes, proving (2.1) for `j>=1`.  For `j=0`, the same calculation
counts all zero-indegree targets except the unique radius-`m` word; adding
that word gives

\[
 A_{m,0}=\binom{2m-1}{m}=W/2,
\]

which is again (2.1).  Finally, summing (2.1) over `j>=t` and using the
hockey-stick identity proves (2.2).  QED.

For every fixed `j`, (2.1) gives

\[
 \frac{A_{m,j}}{W}
 =\frac{m(m)_j}{(2m)_{j+1}}
 \longrightarrow 2^{-(j+1)}.                          \tag{2.7}
\]

Thus the indegree of a uniformly random middle vertex converges to the
geometric distribution

\[
 \Pr(J=j)=2^{-(j+1)},\qquad j=0,1,2,\ldots.             \tag{2.8}
\]

This is a positive-density branching phenomenon, not a boundary defect.

## 3. Exact branching and path-cover counts

Several useful counts now follow without approximation:

\[
 \begin{aligned}
 \#\{\deg^-=0\}&=\frac W2,\\
 \#\{\deg^-=1\}&=\binom{2m-2}{m-1},\\
 \#\{\deg^-\ge2\}&=\binom{2m-2}{m-2}
   =\frac{m-1}{2(2m-1)}W,                              \tag{3.1}\\
 \sum_X(\deg^-(X)-1)_+
   &=\frac W2-K
    =\frac{m-1}{2(m+1)}W.                              \tag{3.2}
 \end{aligned}
\]

In particular, asymptotically one quarter of all middle vertices branch, and
the total branching excess is asymptotically `W/2`.  The average indegree at
a branching vertex is exactly

\[
 \frac{3m}{m+1}\longrightarrow3.                      \tag{3.3}
\]

### Retracted Corollary 2

The former claim that every linear subforest has at most `W/2` edges was
incorrect.  Deleting a vertex's outgoing edge can permit two of its incoming
edges to remain, so the one-incoming-edge argument did not optimize over
arbitrary subforests.  The formulae formerly numbered (3.4)--(3.5) and the
asserted `(1/2-o(1))W` replacement bound are withdrawn.

The exact indegree law (3.1)--(3.3) is unaffected.  The correct optimization
is a rooted-tree dynamic program.  Its exact retained-edge values for
`m=3,...,7` are

    13, 44, 159, 588, 2188,

strictly larger than the obsolete `W/2` values
`10,35,126,462,1716`.  The recurrence and deterministic replay are in
`MATH_CORRECTION_GK_PROJECTION_LINEAR_SUBFOREST_TREE_DP_20260731.md`.
The plane-tree component theorem, bivariate generating function and
asymptotic analysis are now in
`MATH_THEOREM_CATALAN_MATCHING_SWITCH_RECTANGLES_AND_GK_EDIT_DISTANCE_20260731.md`.
They prove

\[
 {\Delta_m\over m\operatorname{Cat}_m}
 \longrightarrow0.356895867892\ldots,
\]

so the corrected edit barrier is still `Theta(W)`.

## 4. Failure of the shift-compatible SCD condition

The shift-compatible condition in `PARTIAL_BLOCK_MULTISCALE.md` requires the
middle projection to be a radius-preserving permutation, apart from an
allowed repair set.  Equation (1.3) proves instead that the standard
Greene--Kleitman projection sends

\[
 V_d\longrightarrow V_{d-1}\qquad(d\ge1).              \tag{4.1}
\]

There are

\[
 W-K=(1-o(1))W                                          \tag{4.2}
\]

positive-radius middle sets.  Hence deleting or altering only `o(W)` of the
standard projection edges cannot make it radius-preserving.  The desired
shift recurrence is not a small perturbation of this projection; it requires
a different SCD or a different choice of downward/upward labels on almost
every chain.

## 5. What the Gregor--Micka--Mutze Hamilton cycle does not supply

Gregor, Micka, and Mutze prove that the Greene--Kleitman SCD can be extended
to a Hamilton cycle of the entire hypercube
([*On the central levels problem*](https://arxiv.org/abs/1912.01566)).
Their cycle traverses every
symmetric chain monotonically and joins consecutive chains at their bottom
or top endpoints.  This is a theorem about **ordering whole chains and
connecting their endpoints**.

It does not change any of the intrinsic facts above:

1. the middle projection (1.3) still lowers radius;
2. its positive-density indegree branching remains;
3. the connector between two whole chains is a cube edge at their endpoints,
   not an assertion that their middle flags obey the label shift recurrence;
4. the recursive chain operations used in their ordering shorten or lengthen
   a chain by two, so consecutive chain radii generally differ by one rather
   than being preserved.

Even if one extracts a Johnson ordering of the middle members from that cycle,
ordinary Johnson adjacency supplies neither the missing rank-`m-1`/rank-`m+1`
colour pairing nor the higher identities

\[
 r_i(f(X))=r_{i+1}(X),\qquad
 u_i(f(X))=u_{i+1}(X).                                 \tag{5.1}
\]

Moreover, using the full cube Hamilton cycle literally costs `4^m` vertices,
whereas

\[
 4^m\sim\sqrt{\pi m}\,W,                               \tag{5.2}
\]

so its uncompressed traversal is too long by a factor of order `sqrt(m)`.
Compressing each chain to its middle member removes precisely the endpoint
and ordered-label information on which the hypercube connectors operate.

Thus the Hamilton-cycle theorem is useful evidence that the GK chains admit a
global recursive ordering, but it supplies neither the
\(\Delta_m=(0.356895867892\ldots+o(1))W\) colour-preserving changes required
by the corrected plane-tree edit theorem nor the radius-preserving shift
recurrence. Any use of that ordering in the OR problem needs an
additional compression theorem that transports endpoint connectors to
middle flags while preserving both shadows; no such implication follows from
the published Hamilton-cycle result.

## 6. Consequence for the global programme

The standard Greene--Kleitman middle projection should be removed from the
list of plausible `o(W)`-repair starting points.  Its exact role is instead a
diagnostic extremal example:

* it produces the correct two adjacent shadow colour sets exactly once;
* it is acyclic with only `K=o(W)` tree components;
* nevertheless, geometric indegree branching forces `Theta(W)` edge
  replacement before it becomes traversable as a middle word.

The remaining viable SCD target is genuinely different: construct an SCD
whose projection is born approximately radius-preserving and injective, or
construct the wreath/shift system directly without passing through the
Greene--Kleitman projection.
