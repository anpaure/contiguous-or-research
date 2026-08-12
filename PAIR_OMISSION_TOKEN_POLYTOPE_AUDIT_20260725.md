# The clustered token polytope: exact fractional point, non-TU minor, and the required correlation sign

Date: 2026-07-25

This note formulates the clustered balanced token problem from
`PAIR_OMISSION_CLUSTERED_TOKEN_REDUCTION_20260725.md` as an integer program.
It records three exact facts.

1. The fully symmetric token system has a fractional point with exact
   central matching marginals, exact uniform flag means at every depth, and
   row-run cost (O(W/m)).
2. Adding only the first upper-flag capacities already destroys total
   unimodularity: the constraint matrix contains an explicit determinant-
   two minor.
3. Standard negatively correlated matching rounding has the wrong
   correlation sign.  It creates (Theta(W)) source-row runs.  A successful
   rounding must be positively correlated along intervals of one physical
   row, while remaining repulsive across equal target labels.

Thus a network-flow proof does solve the marginal flag table, but not the
simultaneous physical clustering.  The exact missing object is a block-
correlated rounding, not ordinary swap or pipage rounding.

## 1. Variables and constraints

Use the coordinate-symmetric orbit token multigraph.  A token

\[
 e=(P,\pi,i)
\]

has central endpoints

\[
 S(e)\in\binom{[n]}{m-1},\qquad
 Y(e)\in\binom{[n]}m,
\]

and signed flags

\[
 L_q(e)\in\binom{[n]}{m-q},\qquad
 U_q(e)\in\binom{[n]}{m+q}
 \quad(1\le q\le H).
\]

Let (x_e\in\{0,1\}).  The central matching constraints are

\[
 \sum_{e:S(e)=S}x_e=1
 \quad(S\in V_-),
\tag{1.1}
\]

\[
 \sum_{e:Y(e)=Y}x_e\le1
 \quad(Y\in V_0).
\tag{1.2}
\]

For a flag target (T), put

\[
 \ell_{q,T}^- =\sum_{e:L_q(e)=T}x_e,
 \qquad
 \ell_{q,T}^+ =\sum_{e:U_q(e)=T}x_e.
\tag{1.3}
\]

Balanced flag capacities ask that these integers lie in the two adjacent
integer levels around their forced means, or more generally that their
weighted balanced overload have total (o(W)).

Finally fix one cut in every cyclic source row (R), and order its tokens

\[
 e_{R,0},e_{R,1},\ldots,e_{R,L-1},qquad L=2m-1.
\]

Introduce run-start variables (z_{R,i}\ge0) satisfying

\[
 z_{R,0}\ge x_{R,0},
 \qquad
 z_{R,i}\ge x_{R,i}-x_{R,i-1}\quad(1\le i<L).
\tag{1.4}
\]

For binary (x), minimizing

\[
 J(x)=\sum_{R,i}z_{R,i}
\tag{1.5}
\]

counts the selected linear runs exactly.  Choosing a different cut changes
the cyclic run count by at most one per used row, which is harmless at the
(O(W/m)) row scale.

## 2. The exact symmetric fractional point

Let the orbit multiplicity be (M).  The central degrees are

\[
 d_-=M\binom{m+2}{2},\qquad
 d_0=M\binom{m+1}{2}.
\tag{2.1}
\]

Assign

\[
 \boxed{x_e^*=1/d_-}
\tag{2.2}
\]

to every token.  Then every lower constraint (1.1) has value one, while

\[
 \sum_{e:Y(e)=Y}x_e^*
 =\frac{d_0}{d_-}
 =\frac{m}{m+2}
 =\frac{|V_-|}{|V_0|}<1.
\tag{2.3}
\]

Coordinate transitivity gives, for every target in a fixed signed rank,

\[
 \ell_{q,T}^{\pm}(x^*)
 =\frac{|V_-|}{\binom{n}{m\pm q}},
\tag{2.4}
\]

the exact forced mean of an integral lower-saturating matching.

Along each source row, (2.2) is constant.  In (1.4) take

\[
 z_{R,0}=1/d_-,\qquad z_{R,i}=0\quad(i>0).
\]

The number of orbit rows divided by (d_-) is exactly the number of rows
in one lower-perfect colour, namely

\[
 \frac{|V_-|}{2m-1}=O(W/m).
\tag{2.5}
\]

Thus

\[
 \boxed{J(x^*)=\frac{|V_-|}{2m-1}=O(W/m)=o(W/H)}
\tag{2.6}
\]

throughout the Gaussian range.  There is no fractional capacity, flag, or
run-cost obstruction.

There is a stronger integral interpretation of this point.  Let (M_0)
be the clustered first-avoided matching of Theorem 5.1, and take its complete
coordinate-permutation orbit inside the symmetric token multigraph.  The
coordinate group is transitive on labelled start tokens, every orbit member
has (|V_-|) tokens, and every orbit member has the same run count as
(M_0).  Hence

\[
 \boxed{
 x^*=\mathbb E_{\sigma\in S_n}{\bf1}_{\sigma M_0}.}
\tag{2.7}
\]

In particular (x^*) lies in the convex hull of integral matchings each
satisfying

\[
 J=O(W\log^2m/m)=o(W/H).
\tag{2.8}
\]

So even the simultaneous *fractional* flag balance and *integral* low-run
condition are compatible in one convex resolution.  The remaining gap is
purely nonlinear: coordinate relabelling only permutes every flag-load
histogram, and therefore preserves its balanced-overload and collision
energy.  Averaging (2.7) makes the mean vector uniform, but no individual
orbit member has smaller energy than (M_0).  A proof must interpolate
between structurally different clustered matchings, rather than merely
average coordinate copies of one.

## 3. A determinant-two minor at the first upper flag

Without the flag rows, (1.1)--(1.2) are the bipartite matching matrix and
are totally unimodular.  This ceases to hold as soon as the first upper
flags are constrained.

### Proposition 3.1

The incidence matrix whose rows include lower targets, middle targets, and
rank-((m+1)) first-upper targets contains the minor

\[
 \begin{pmatrix}
 1&1&0\\
 0&1&1\\
 1&0&1
 \end{pmatrix},
\tag{3.1}
\]

whose determinant is (2).  Hence neither this matrix nor the full
clustered flag matrix is totally unimodular.

### Proof

Let (C) be an ((m-1))-set and choose distinct coordinates

\[
 a,b,c\notin C,
\]

as well as (d\in C).  Put

\[
 \begin{aligned}
 S_1&=C,\\
 Y_1&=C+a,\\
 Y_2&=C+b,\\
 Z_1&=C+a+b,\\
 Z_2&=C+b+c,\\
 S_3&=(C-d)+b.
 \end{aligned}
\tag{3.2}
\]

Consider the three saturated two-step flags

\[
 e_1=(S_1,Y_1,Z_1),\qquad
 e_2=(S_1,Y_2,Z_2),\qquad
 e_3=(S_3,Y_2,Z_1).
\tag{3.3}
\]

Every such flag embeds in a pair-omission row: choose the omitted pair in
the complement of its top set, order the two added coordinates at the two
endpoints, and complete the cyclic order.  The symmetric orbit token system
therefore contains all three tokens.

Restrict the incidence matrix to columns (e_1,e_2,e_3) and rows

\[
 S_1,quad Y_2,quad Z_1.
\]

The resulting matrix is (3.1).  \(\square\)

This is the standard three-dimensional-matching triangle in literal flag
coordinates.  It shows that adding clones or lower/upper capacity arcs to
the bipartite network cannot by itself preserve integrality.  Any positive
polyhedral theorem must use more than total unimodularity of the marginal
flow network.

## 4. Ordinary dependent rounding has the wrong sign

Let a random integral lower-saturating matching (X) have the uniform
marginals

\[
 \Pr(e\in X)=1/d_-.
\tag{4.1}
\]

For one linearly cut source row, its expected number of selected runs is

\[
 \mathbb E J_R
 =\Pr(e_{R,0}\in X)
 +\sum_{i=1}^{L-1}
 \left[
 \Pr(e_{R,i}\in X)
 -\Pr(e_{R,i-1},e_{R,i}\in X)
 \right].
\tag{4.2}
\]

Summing over all rows and using that the total expected number of selected
tokens is (|V_-|), we obtain

\[
 \mathbb E J(X)
 =|V_-|
 -\sum_R\sum_{i=1}^{L-1}
 \Pr(e_{R,i-1},e_{R,i}\in X)
 +O(W/m).
\tag{4.3}
\]

Suppose the rounding is negatively correlated on distinct token variables,
as in the standard swap-, pipage-, or contention-resolution paradigm:

\[
 \Pr(e,f\in X)le\Pr(e\in X)\Pr(f\in X)=d_-^{-2}.
\tag{4.4}
\]

The total number of consecutive token pairs is

\[
 (1+o(1))|V_-|d_-.
\]

Therefore (4.3)--(4.4) give

\[
 \boxed{
 \mathbb E J(X)
 \ge |V_-|\left(1-O(1/d_-)\right)
 =\Theta(W).}
\tag{4.5}
\]

This is larger than the permitted (o(W/H)) by a factor of order (H).

Conversely, (4.3) shows exactly what is required for a successful random
rounding:

\[
 \sum_R\sum_i
 \Pr(e_{R,i-1},e_{R,i}\in X)
 =|V_-|-o(W/H).
\tag{4.6}
\]

Equivalently, conditional on a typical selected token, its predecessor in
the same physical row must also be selected with probability

\[
 1-o(1/H).
\tag{4.7}
\]

The rounding must therefore be almost maximally **positively correlated**
along row intervals.  At the same time, tokens carrying the same middle or
flag target must be negatively correlated to enforce capacities.  These are
the two competing correlation signs hidden by a rank-free matching
formulation.

## 5. Exact block-rounding gate

Equations (2.6), (3.1), and (4.7) leave one viable polyhedral route.
Introduce interval-block variables on every physical row, rather than
rounding individual token variables.  A block variable simultaneously
selects a consecutive run of length (gg H); this builds (4.7) into the
atom.  Conflicts between blocks are imposed at their central and flag
targets.

The resulting integer program has the desired run cost automatically, but
its columns are precisely long two-parent Pascal segments.  Its matching
problem is therefore the whole-row/segment packing gate, not a disguised
network flow.  A sufficient rounding theorem would be:

> **Positive-along-rows, negative-across-targets rounding theorem.**  Round
> the uniform point (2.2) into an integral lower-saturating matching so that
> (4.6) holds and the total balanced flag overload is (o(W)).

Any proof via a random process must expose the block variables explicitly.
Tokenwise negative-correlation machinery cannot establish the theorem.

This does not rule out a specialized block-dependent rounding.  It
identifies its exact quantitative requirements and proves that neither a
TU extension nor standard dependent rounding supplies it.
