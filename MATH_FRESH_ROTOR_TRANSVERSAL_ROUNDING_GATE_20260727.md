# The fresh-rotor transversal as a projected circulation

Date: 2026-07-27

## 0. Outcome

The high-multiplicity fresh rotor is an exact **fractional** solution of a
projected circulation problem.  Reducing its multiplicity to one is not an
ordinary network-flow, bipartite-matching, or matroid-intersection rounding.
There are two independent reasons.

1.  Projection multiplicity and lower-colour constraints are side constraints
    on a network circulation.  Already at depth one their natural diamond
    matrix has a determinant-two minor, so total unimodularity is false.
2.  More importantly, rotor balance fixes only one-point cylinder marginals.
    CPCR is exactly a two-point collision functional.  Two distributions can
    have identical perfectly uniform one-point marginals and respectively
    zero and maximal collision.  Thus no theorem using only the balance proved
    in `MATH_ROTOR_HAZARD_SCHEDULE_20260727.md` can yield CPCR.

There is nevertheless a clean positive boundary.  If upper colours and all
higher cylinders are ignored, the depth-one lower-colour problem is exactly a
spanning 2-factor in a regular bipartite inclusion graph and is integral by
b-matching.  The new direct sigma-CSP makes the first nonlinear obstruction
completely explicit: upper coverage is a condition on the *pair* of incidence
edges chosen at each lower vertex.

The smallest exact replacement for the open fresh-rotor lemma is therefore a
**pair-balanced projected-circulation theorem**: decompose the uniform fresh
circulation into multiplicity-one lower-rainbow cycle covers whose aggregate
two-cylinder collision excess is `o(W)`.  Connectivity can be handled after
this only if the joining switches preserve the finite-memory labels cheaply.

## 1. The finite-memory automaton and its projected circulation polytope

Put

\[
 K=2r-1,\qquad
 \mathcal M=\binom{[K]}r,\qquad
 \mathcal L=\binom{[K]}{r-1},\qquad
 W=|\mathcal M|=|\mathcal L|.
\]

Let `Gamma_H=(V_H,E_H)` be the directed finite-memory exchange graph from
Section 4 of `MATH_ROTOR_HAZARD_SCHEDULE_20260727.md`.  A state records the
current middle set and enough recent directed swaps to decide freshness
through depth `H`.  Every arc `e` has the following labels:

* `tau(e) in M`, its current middle set;
* `kappa(e) in L`, its immediate lower intersection colour;
* `ell_{q,-}(e) in binom([K],r-q)` and
  `ell_{q,+}(e) in binom([K],r+q)`, the intersection and union of the
  encoded `q`-window, for `q<=H`.

Write `D` for the vertex-arc incidence matrix of `Gamma_H`, and write `P_0`,
`P_-`, and `A_{q,\pm}` for the corresponding 0-1 label-incidence matrices.
Consider

\[
 \mathcal P_H=
 \left\{z\ge0:
 Dz=0,\quad P_0z={\bf1}_{\mathcal M},\quad
 P_-z={\bf1}_{\mathcal L}\right\}.
\tag{1.1}
\]

This is the closed-cycle normalization.  An endpoint-rooted one-hole path is
obtained either by adjoining its prescribed terminal closing edge of colour
`C_*`, when that edge is available, or by replacing `Dz=0` and `P_-z=1` by
the corresponding two endpoint imbalances and the single lower-colour
deficit.  Every integrality and collision statement below is unchanged by
this rank-one boundary modification.

### Proposition 1.1 (integral points are lower-rainbow cycle covers)

Every integral point of (1.1) is 0-1 and is a disjoint union of directed
cycles in `Gamma_H`.  Its projection visits every middle set exactly once,
uses every immediate lower colour exactly once, and is fresh through depth
`H`.  Conversely, every such lifted cycle cover gives an integral point of
(1.1).

#### Proof

The equation `P_0z=1` and integrality imply that at most one selected arc can
have any prescribed middle label, hence every selected multiplicity is 0 or
1.  Flow conservation makes the selected arcs Eulerian at every lifted state,
so their support is a disjoint union of directed cycles.  The two partition
equations give the asserted projection and lower-colour multiplicities.  The
converse is immediate.  \(\square\)

The uniform high-multiplicity rotor circulation, divided by its common middle
multiplicity, is a point `x^* in P_H`.  Symmetry gives

\[
 A_{q,\pm}x^*=\lambda_{q,\pm}{\bf1}
\tag{1.2}
\]

at every audited depth.  Thus the rotor theorem supplies an exact fractional
point of (1.1), not an integral point and not a convex decomposition into the
integral points of (1.1).

Connected support is an additional condition: an integral point of (1.1) is
a Hamilton cycle only when its support has one component.  Connectivity is
not a matroid constraint and is deliberately separated below.

## 2. The direct depth-one sigma-CSP

For every `X in L`, choose

\[
 \sigma(X)=A\in\binom{[K]}{r+1},\qquad X\subset A.
\tag{2.1}
\]

If `A\setminus X={a,b}`, this choice inserts the two edges

\[
 X-(X+a),\qquad X-(X+b)
\tag{2.2}
\]

in the bipartite inclusion graph between `L` and `M`.

### Proposition 2.1 (sigma is precisely a coloured 2-factor)

The conditions

1. one value `sigma(X)` for every `X in L`, and
2. every `Y in M` is incident with exactly two of the edges (2.2),

are equivalent to a spanning simple 2-factor of the `r`-regular bipartite
inclusion graph `B(L,M)`.  Under this correspondence, the upper set
`sigma(X)` is the union colour of the pair selected at `X`.  Consequently
surjectivity of `sigma` is exactly hole-free immediate-upper coverage.

#### Proof

A choice (2.1) chooses two distinct neighbours of `X` in `B(L,M)`.  Hence
condition 1 is degree two on the `L` shore, and condition 2 is degree two on
the `M` shore.  Conversely, the two middle neighbours of a lower set `X`
have the form `X+a,X+b` and determine the unique upper set `X+{a,b}`.
The last assertion follows from

\[
 (X+a)\cup(X+b)=X+\{a,b\}=\sigma(X).
\]

\(\square\)

Thus the first two conditions are an ordinary bipartite b-factor problem.
Since `B(L,M)` is regular and balanced, it has a 1-factorization and hence a
spanning 2-factor.

The upper-surjection condition is not another free Hall constraint.  With
binary variables `z_{X,A}` it gives

\[
\begin{aligned}
 \sum_{A\supset X}z_{X,A}&=1 &&(X\in\mathcal L),\\
 \sum_{X\subset Y\subset A}z_{X,A}&=2 &&(Y\in\mathcal M),\\
 \sum_{X\subset A}z_{X,A}&\ge1 &&(A\in\mathcal U),
\end{aligned}
\tag{2.3}
\]

where `U=binom([K],r+1)`.  A column of (2.3) represents an entire Boolean
diamond: one lower vertex, its two middle vertices, and one upper vertex.

### Proposition 2.2 (the diamond matrix is not totally unimodular)

For every `r>=3`, the constraint matrix in (2.3) contains a square minor of
determinant `2`.

#### Proof

Fix `X in L` and three distinct letters `a,b,c` outside `X`.  Take the three
columns

\[
 z_{X,X+\{a,b\}},\quad z_{X,X+\{a,c\}},\quad
 z_{X,X+\{b,c\}}
\]

and the three middle rows indexed by `X+a,X+b,X+c`.  The resulting submatrix
is, up to row and column order,

\[
 \begin{pmatrix}
 1&1&0\\
 1&0&1\\
 0&1&1
 \end{pmatrix},
\]

whose determinant is `-2`.  \(\square\)

This is a precise obstruction to a TU/network-flow proof of simultaneous
middle degree and upper coverage.  It is not a nonexistence result; it says
that the special Boolean geometry, rather than generic b-matching
integrality, must be used.

### Proposition 2.3 (what the two separate Hall arguments prove)

* Ignoring upper colours, the middle-degree problem is integral by the
  bipartite 2-factor theorem.
* Ignoring middle degrees, a surjection `sigma:L onto U` with `X subset
  sigma(X)` exists by Hall.

Neither assertion implies their conjunction.

#### Proof

Only the second statement needs comment.  In the bipartite containment graph
between `L` and `U`, a left vertex has degree

\[
 d_L=\binom r2,
\]

and a right vertex has degree

\[
 d_U=\binom{r+1}2>d_L.
\]

For `S subset U`, double counting edges out of `S` gives

\[
 d_U|S|\le d_L|N(S)|,
\]

so `|N(S)|>=|S|`.  Match every upper set to a distinct contained lower set,
then assign the unused lower sets arbitrarily to containing upper sets.  This
is a surjection.  The middle-degree equations do not occur in this Hall
argument.  \(\square\)

There is also no fractional capacity obstruction to the conjunction.  The
constant assignment

\[
 z^*_{X,A}=\binom r2^{-1}\qquad(X\subset A)
\tag{2.4}
\]

satisfies the first two equations of (2.3), and every upper load equals

\[
 \frac{\binom{r+1}2}{\binom r2}
 =\frac{r+1}{r-1}.
\tag{2.5}
\]

The direct sigma-CSP is therefore the exact q=1 face of the general integral
transversal problem: fractionally perfect, separately integral in its two
projections, but not covered by a common Hall/TU theorem.

### 2.4 The two orthogonal Johnson clique decompositions

There is a useful phase-free way to remember (2.3).  Every edge of the
Johnson graph on `M` belongs to exactly one lower clique

\[
 K_X=\{X+a:a\notin X\}\qquad(X\in\mathcal L)
\]

and exactly one upper clique

\[
 K^A=\{A-a:a\in A\}\qquad(A\in\mathcal U).
\]

Its lower and upper colours are respectively its intersection and union.
The sigma-CSP asks for a graph `F subset J(K,r)` which

1. chooses exactly one edge from every lower clique `K_X`;
2. has degree two at every middle vertex;
3. meets every upper clique `K^A`;
4. and, for a Hamilton solution, is connected.

Thus q=1 is an orthogonal-clique transversal problem.  Conditions 1--2 are
the bipartite 2-factor of Proposition 2.1; condition 3 is a covering
constraint in the *other* clique decomposition.  This is why treating the
upper sets as merely another shore of the first matching graph loses the
essential coupling.

Under complementation, this is the paired-perfect-matching normal form of
`MATH_THEOREM_ODD_JOHNSON_DOUBLE_RAINBOW_PAIRED_MATCHING_GATE_20260726.md`.
That note fixes one perfect matching and searches for a second whose relative
permutation has one cycle and whose complementary colour map is surjective.
The sigma formulation instead exposes the same object as a lower-clique
transversal on the complementary Johnson shore.  The formulations are
equivalent; neither supplies upper surjectivity from Hall alone.

## 3. A positive convex-hull statement before upper colours

The uniform diamond vector (2.4), after upper constraints are omitted, is in
the convex hull of integral spanning 2-factors.

### Proposition 3.1 (symmetrized 2-factor decomposition)

Choose any spanning 2-factor `F` of `B(L,M)` and average its coordinate
images over `S_K`.  The resulting distribution on spanning 2-factors chooses
every flag `(X,A)` with probability exactly `1/binom(r,2)`.

#### Proof

The symmetric group is transitive on flags `X subset A` with rank difference
two.  Every 2-factor chooses exactly one such flag at each `X`, hence exactly
`W` flags.  There are `W binom(r,2)` flags in total.  Orbit averaging
therefore gives marginal `1/binom(r,2)` to every flag.  \(\square\)

This cleanly locates the first obstruction.  Reducing multiplicity to one
while preserving middle and lower degrees is already possible with the exact
uniform one-point marginal.  What is missing is pairwise repulsion among
flags with the same upper or deeper-cylinder label.

There is no hidden averaging gain in Proposition 3.1.  Coordinate
permutations merely permute the upper load vector, so every member of the
orbit of `F` has exactly the same upper hole count and the same factorial
excess as `F`.  Orbit symmetrization repairs the one-point marginal while
leaving the second-order defect unchanged.  This is the depth-one analogue
of the earlier relabelling-invariance obstruction for wreath factors.

There is, however, a second and more useful averaging operation: pair the
colour classes of an entire 1-factorization.

### Proposition 3.2 (the orthogonal-factorization identity)

Assume `r>=3`.

Let

\[
 E(B)=M_1\dot\cup\cdots\dot\cup M_r
\]

be a 1-factorization of the lower--middle inclusion graph.  For a colour pair
`p={i,j}`, put `F_p=M_i union M_j`; this is a spanning 2-factor.  For an
upper set `A` and a lower set `X subset A`, let `p_A(X)` be the unordered pair
of colours on the two incidence edges from `X` to the two middle sets in the
diamond `[X,A]`, and put

\[
 m_A(p)=|\{X\subset A:|X|=r-1,\ p_A(X)=p\}|.
\tag{3.1}
\]

Then `m_A(p)` is exactly the upper load of `A` in `F_p`.  Moreover, writing

\[
 d=\binom r2,
 \qquad
 \Delta_A=\sum_{p\in\binom{[r]}2}\binom{m_A(p)}2-r,
\tag{3.2}
\]

one has `Delta_A>=0` and the exact identity

\[
 \boxed{
 \frac1d\sum_{p\in\binom{[r]}2}\Phi_1^+(F_p)
 =\frac2d\sum_{A\in\mathcal U}\Delta_A.}
\tag{3.3}
\]

#### Proof

At `X`, the two edges chosen by `F_p` are exactly the diamond `[X,A]` iff
`p_A(X)=p`; this proves the load statement.  There are

\[
 \binom{r+1}2=d+r
\]

lower sets inside `A`, so `sum_p m_A(p)=d+r`.  Among `d` nonnegative integer
loads of this total, convexity of `binom{x}{2}` gives

\[
 \sum_p\binom{m_A(p)}2\ge r;
\]

for `r>3` equality means `r` loads two and all remaining loads one; for
`r=3` it means all three loads are two.  Hence `Delta_A>=0`.

Now sum the equal-target pair count first over factors and then over upper
sets:

\[
 \sum_pP_1^+(F_p)=\sum_A\sum_p\binom{m_A(p)}2.
\]

For one factor the balanced minimum is

\[
 P^{\min}=W-|\mathcal U|=\frac{2W}{r+1}.
\]

Since `|U|=W(r-1)/(r+1)`,

\[
 dP^{\min}=r|\mathcal U|.
\]

Subtract this equality and apply Proposition 4.1 factor by factor to obtain
(3.3).  \(\square\)

### Corollary 3.3 (a concrete q=1 sufficient theorem)

If a 1-factorization satisfies

\[
 \frac1{|\mathcal U|}\sum_A\Delta_A=o(r^2),
\tag{3.4}
\]

then some pair `F_p` has immediate-upper factorial excess `o(W)`.  If the
stronger bound `Delta_A=O(r)` holds on average, some pair has excess
`O(W/r)`.

Thus a locally almost-orthogonal 1-factorization is a completely explicit
q=1 pair-rounding theorem.  Choosing `p` uniformly already gives the exact
uniform incidence-edge marginal `2/r` and the exact uniform diamond marginal
`1/binom(r,2)`; identity (3.3), not generic negative correlation, determines
its second moment.  The remaining difficulty is to construct a
1-factorization for which the pair-colour maps `X mapsto p_A(X)` are nearly
surjective for most `A`, and then to retain analogous control for the
higher-depth alternating paths of `F_p`.

This averaging route complements the fixed-first-matching exchange route in
the paired-matching note.  It searches all `binom(r,2)` pairs in one
1-factorization at once.  Identity (3.3) can choose a pair with small colour
defect, but it says nothing about the cycle type of `F_p`; the relative
matching permutation must still be one cycle, or its components must be
joined at controlled cylinder cost.

The local maps in Proposition 3.2 have an additional exact regularity which
is not visible from the global averaging alone.

### Proposition 3.4 (the local colour-pair multigraph is regular)

For each upper set `A`, form a loopless multigraph `G_A` on colour vertex set
`[r]` by inserting one edge `p_A(X)` for every lower `X subset A`.  Then

\[
 \boxed{G_A\text{ is }(r+1)\text{-regular on }r\text{ vertices}.}
\tag{3.5}
\]

Moreover, if

\[
 h_A=|\{p:m_A(p)=0\}|,
\]

then

\[
 \boxed{
 \Delta_A=h_A+
 \sum_{p:m_A(p)\ge3}\binom{m_A(p)-1}{2}.}
\tag{3.6}
\]

In particular `Delta_A=0` iff `G_A` consists of one copy of the complete
graph `K_r` plus a spanning 2-factor (with the second copy of an edge allowed
along that 2-factor).

#### Proof

Fix a factor colour `i`.  Its degree in `G_A` is the number of edges of the
perfect matching `M_i` whose lower and middle endpoints both lie below `A`.
There are exactly `r+1` middle subsets `Y` of `A`.  Each has exactly one
incident edge in `M_i`, and its matched lower endpoint is automatically a
subset of `Y` and hence of `A`.  Thus every one of these `r+1` edges is
internal to the interval below `A`, and the degree of colour `i` in `G_A` is
exactly `r+1`.  This proves (3.5) directly.

Since `sum_p m_A(p)=d+r`, the total excess above one on the nonempty colour
pairs is `r+h_A`.  For every integer `m>=1`,

\[
 \binom m2=(m-1)+\binom{m-1}2.
\]

Substitute this into (3.2) to obtain (3.6).  Finally `Delta_A=0` means every
pair occurs and no pair occurs more than twice.  Removing one copy of every
edge of `K_r` leaves a 2-regular spanning multigraph by (3.5).  The converse
is immediate.  \(\square\)

This is a sharp algebraic target: construct a 1-factorization of the Boolean
middle incidence graph for which most local colour-pair multigraphs `G_A`
are close to `K_r` plus a 2-factor.  A random occupancy heuristic gives
`Delta_A=Theta(r^2)` and only `Theta(W)` CPCR after (3.3); the desired
`o(W)` conclusion is exactly the assertion that the local factorization is
asymptotically more orthogonal than random.

### 3.5 Opposite-dart orthogonality

The same local structure has a useful design-theoretic normal form.  Write
the elements of `A` as local vertices.  For distinct `a,b in A`, define

\[
 \chi_A(a,b)=
 \text{the factor colour of }
 (A-\{a,b\})-(A-\{a\}).
\tag{3.7}
\]

Then:

1. for each fixed `a`, the map `b mapsto chi_A(a,b)` is a permutation of
   `[r]`;
2. `chi_A(a,b) ne chi_A(b,a)`;
3. `m_A({i,j})` is the number of undirected local edges `{a,b}` whose two
   opposite darts have colour pair `{i,j}`.

#### Proof

The `r` lower neighbours of the middle vertex `A-{a}` have all `r` factor
colours exactly once, proving 1.  The two displayed incidence edges for
opposite darts share the lower endpoint `A-{a,b}` and therefore have
different colours in a proper edge-colouring, proving 2.  Statement 3 is the
definition of `p_A`.  \(\square\)

Thus `Delta_A=0` says that a row-Latin colouring of the directed complete
graph on `r+1` local vertices pairs opposite darts so as to realize every
unordered pair of the `r` factor colours, with exactly the edges of one
2-factor repeated.  This resembles a Room/Howell-type local design, but the
tables for distinct `A` are not independent: every incidence edge belongs
to `r-1` such upper intervals and must carry one common global factor colour.
The q=1 construction problem is precisely to make these heavily overlapping
opposite-dart tables asymptotically orthogonal.

## 4. CPCR is exactly excess pair collision

Let a selected integral cycle cover have, at one signed depth, target loads
`L_S`, total load `W`, target count `N`, mean

\[
 \lambda=W/N=c+\theta,
 \qquad c=\lfloor\lambda\rfloor,
 \qquad t=W-cN.
\]

The minimum possible number of unordered equal-target pairs is

\[
 P^{\min}=N\binom c2+tc,
\tag{4.1}
\]

attained exactly by loads in `{c,c+1}`.  Put

\[
 P=\sum_S\binom{L_S}{2}.
\]

### Proposition 4.1 (factorial excess identity)

\[
 \boxed{
 \sum_S(L_S-c)(L_S-c-1)=2(P-P^{\min}).}
\tag{4.2}
\]

#### Proof

Both sides expand to

\[
 \sum_SL_S(L_S-1)-2cW+Nc(c+1).
\]

\(\square\)

For candidate lifted arcs `e,f`, define the collision kernel

\[
 K_q^\pm(e,f)
 =\mathbf1\{\ell_{q,\pm}(e)=\ell_{q,\pm}(f)\}.
\tag{4.3}
\]

For a 0-1 selection vector `z`,

\[
 P_q^\pm(z)=
 \sum_{e<f}K_q^\pm(e,f)z_ez_f.
\tag{4.4}

Hence the CPCR objective is a quadratic conflict cost on the integral points
of (1.1), not a linear discrepancy of the one-point cylinder loads.

## 5. Why exact rotor balance alone cannot be rounded to CPCR

The following elementary packet example is the decisive logical warning.

### Proposition 5.1 (identical marginals, opposite collision behaviour)

Let positions and targets both be `Z_s`.  There are two distributions on
maps from positions to targets:

* choose `a` uniformly and use `i mapsto i+a`;
* choose `a` uniformly and use `i mapsto a` for every `i`.

For every position-target pair `(i,j)`, both distributions have marginal
probability `1/s`.  In the first distribution every target load is one.  In
the second, one target has load `s` and all other targets have load zero.

Thus perfect one-point balance is compatible with both zero and maximal
pair collision.  \(\square\)

The phenomenon persists even when every outcome is an integral perfect
matching, so it is not an artefact of allowing arbitrary maps.

### Proposition 5.2 (affine perfect-matchings with identical marginals)

Let `s` be prime and take the complete bipartite graph with both shores
identified with `F_s`.  Give an edge `(i,j)` the target colour

\[
 \ell(i,j)=j-i.
\]

Consider the following two distributions on perfect matchings.

1. Choose `b` uniformly and use `j=i+b`.
2. Choose `(a,b)` uniformly subject to `a ne 1`, and use `j=ai+b`.

Both distributions select every edge with probability exactly `1/s`.  In
the first distribution all `s` selected edges have one common target colour.
In the second, every target colour occurs exactly once in every outcome.

#### Proof

All displayed affine maps are permutations.  In the first family, a fixed
edge `(i,j)` determines the unique value `b=j-i`.  In the second, for each of
the `s-1` permitted values of `a`, it determines the unique `b=j-ai`; hence
its probability is `(s-1)/(s(s-1))=1/s`.  For the first family the colour is
identically `b`.  For the second it is `(a-1)i+b`, a permutation of `F_s`
because `a-1 ne 0`.  \(\square\)

Thus even exact common-base constraints plus exact uniform edge marginals do
not determine the second-order target profile.  Any positive theorem for the
Boolean carrier must exploit its cylinder geometry, not merely the fact that
the normalized point lies in a perfect-matching or b-factor polytope.

### Proposition 5.3 (the black-box negative-correlation ceiling)

Suppose a distribution on feasible integral selections has the correct
one-point target means

\[
 \mathbb E L_S=\lambda=W/N
\]

and, within every target fibre, its selected-candidate indicators are
pairwise negatively correlated.  Then at that depth

\[
 \mathbb E\sum_S(L_S-\lambda)^2\le W
\tag{5.2}
\]

and consequently

\[
 0\le\mathbb E\Phi_q\le W,
\tag{5.3}
\]

where `Phi_q` is the floor-corrected factorial excess.

#### Proof

Write `L_S=sum_{e in F_S}Z_e`.  Negative correlation gives

\[
 \operatorname{Var}L_S
 \le\sum_{e\in F_S}\operatorname{Var}Z_e
 \le\sum_{e\in F_S}\mathbb EZ_e.
\]

Sum over the disjoint target fibres.  Every selected object has exactly one
target at the given depth, so the last sum is `W`.  The means are exact, hence
the left side of (5.2) is the sum of these variances.  Finally

\[
 \Phi_q=E_q-E_q^{\min}
\]

with `E_q^{min}>=0`, while `Phi_q>=0` on integral loads.  This proves
(5.3).  \(\square\)

For both signs and `H` depths, averaging can therefore extract at best the
generic guarantee

\[
 \sum_{q\le H,\pm}\Phi_q=O(HW)
\tag{5.4}
\]

from such a black box.  This is rigorous `O(W)` progress at each individual
depth, but it is not the required `o(W)` aggregate when `H` grows.  A proof
must beat ordinary negative dependence by enforcing almost-hard capacity in
all cylinder fibres simultaneously.

When the distribution is presented by a tractable sequential exposure, the
same averaging proof can of course be derandomized by conditional
expectation.  A marginal oracle alone does not provide such an exposure, so
algorithmic derandomization is a separate issue and is not being assumed.

### 5.4 The exact spread hypothesis for two random perfect matchings

The q=1 proposal "take two random perfect matchings" can be isolated
cleanly.  Let `(M_0,M_1)` be a random ordered pair of edge-disjoint perfect
matchings of `B(L,M)`, and let `sigma(X)` be the union of the two middle
neighbours of `X`.  Suppose that for every upper set `A` and distinct
`X,X' subset A`,

\[
 \Pr\bigl(\sigma(X)=A,\ \sigma(X')=A\bigr)
 \le \frac{C}{r^4}
\tag{5.5}
\]

for an absolute constant `C`.  Then

\[
 \mathbb E\sum_A\binom{L_A}{2}=O_C(W),
 \qquad
 \mathbb E\Phi_1^+=O_C(W).
\tag{5.6}
\]

#### Proof

There are `d_U=binom(r+1,2)` lower sets contained in a fixed `A`.  Hence

\[
 \mathbb E\binom{L_A}{2}
 \le \binom{d_U}{2}\frac{C}{r^4}=O_C(1).
\]

There are `|U|<W` upper sets.  Sum, then use Proposition 4.1.  \(\square\)

A sufficient route to (5.5) would be a perfect-matching measure with uniform
edge marginals and `O(r^{-2})` inclusion probability for every prescribed
pair of vertex-disjoint edges: after expanding the two orientations at each
of `X,X'`, independence of the two matching draws gives (5.5), up to the
additional problem of coupling the draws to be edge-disjoint.  Neither this
uniform two-edge estimate nor its preservation under the disjoint coupling
is automatic for perfect matchings of a general regular bipartite graph.

Even if (5.5) is proved, it yields only the generic `O(W)` q=1 bound, not the
required `o(W)` aggregate.  At depth `q`, a target event is determined by an
alternating path containing `Theta(q)` matching edges.  A two-matching proof
through growing `H` would therefore need uniform high-order spread for pairs
of such paths, not merely negative dependence of individual edges.  This is
another exact reason that the de Bruijn cylinder structure cannot be replaced
by a black-box random-perfect-matching estimate.

Theorem 3.1 and Section 4 of the rotor note prove the analogue of the common
one-point marginals.  They do not provide a joint law on multiplicity-one
cycle covers, much less the pair marginals needed in (4.4).

Standard dependent rounding is also quantitatively too weak as a black box.
A negative-correlation guarantee of the form

\[
 \Pr(Z_e=Z_f=1)\le x_e x_f
\tag{5.1}
\]

only bounds each depth at the independent collision scale `Theta(W)` when
the target mean is `Theta(1)`.  Summed over a growing number of depths this
is `Theta(HW)`, whereas CPCR requires `o(W)` in aggregate.  The required
rounding must be a near-capacity contention-resolution theorem in every
cylinder partition simultaneously, not ordinary concentration around its
mean.

The same diagnosis rules out a black-box discrepancy invocation.  Every
selected arc belongs to only one fibre at each signed depth, so the cylinder
matrix has column sparsity `O(H)`, and standard partial-colouring theorems may
give additive discrepancy `O(sqrt(H))` (or polylogarithmic variants).  Here
the mean load at the shallow depths is `1+o(1)`.  Even additive discrepancy
one permits a positive density of loads zero and two; that already has
`Theta(W)` factorial excess at one depth.  The target is therefore not small
linear discrepancy.  It is almost-everywhere occupancy at the exact integer
capacity, a much stronger one-sided assertion.

Nor is the sigma system a direct matroid intersection.  Choosing one flag at
each lower set is a partition-matroid base, but degree two on every middle
set is a graph b-factor condition, upper surjectivity is a nonhereditary
lower-quota condition, and connectedness is not matroidal.  Dropping any one
of these makes familiar integral machinery visible; keeping them together
is precisely the problem.

The same point has a polyhedral formulation.  Let

\[
 \varphi_c(j)=(j-c)(j-c-1)\qquad(j\in\mathbb Z_{\ge0})
\]

and extend it linearly between consecutive integers.  This extension is
convex, is zero on `[c,c+1]`, and agrees with CPCR on integral loads.  The
uniform fractional rotor point has zero cost in this convexified objective.
The open lemma asks for an integral point with total cost `o(W)`.  It is
therefore exactly an asymptotically vanishing integrality-gap theorem for
the projected circulation (1.1) with all cylinder partitions added.

## 6. The smallest exact gate

Let `Z_H` be the set of integral points of (1.1), without imposing
connectedness.  For `z in Z_H`, define

\[
 \operatorname{Coll}_H(z)
 =\sum_{q\le H}\sum_{\pm}
   \bigl(P_q^\pm(z)-P_{q,\pm}^{\min}\bigr).
\tag{6.1}
\]

By Proposition 4.1, the factorial-excess condition in the fresh-rotor lemma
is exactly `Coll_H(z)=o(W)`.

### Pair-balanced projected-circulation lemma (open)

For some required `H=H(r)`, the polytope (1.1) has an integral point `z`
such that

\[
 \operatorname{Coll}_H(z)=o(W)
\tag{6.2}
\]

and the number of directed components of its support is small enough to be
joined with `o(W)` total cylinder damage.

Equivalently, it suffices to construct a probability distribution on
lower-rainbow fresh cycle covers for which

\[
 \mathbb E\operatorname{Coll}_H(z)=o(W);
\tag{6.3}
\]

then one member of its support satisfies (6.2).  The normalized universal
rotor circulation gives the desired *first* marginals of such a distribution
but not its existence.

This formulation removes three distractions:

1. scalar section schedules are already solved;
2. one-point cylinder balance is already solved;
3. middle and lower multiplicity alone are already integrally solvable at
   depth one.

The unresolved object is a second-order, multi-partition contention theorem
inside a projected circulation.

### 6.1 Two integral decompositions of the same first-order point

At depth one, the current constructions can be viewed as two incompatible
integral explanations of the same symmetric fractional statistics.

* Symmetrized MSW wreath factors are exactly middle-spanning and have the
  strongest possible residence/freshness, but an individual factor need not
  be lower-rainbow or pair-balanced.
* Symmetrized PBBS transition factors are lower-rainbow and have
  `o(W)` immediate-upper defect in the proved regime, but the individual
  chronology does not have the required growing residence delay.

After coordinate symmetrization both have the same uniform one-point middle,
lower, and diamond marginals.  The desired carrier transversal is not a new
fractional point between them; it is an integral point lying in the
intersection of their two good-support properties.  Equality of the orbit
averages gives no coupling between the supports.  This explains why convex
averaging repeatedly appears to solve the problem and repeatedly stops at
the same place.

## 7. Connectivity and the cost of joining components

Suppose an integral cycle cover has a uniform load cap `B` through depth
`H`.  Replacing a constant number of transition edges in a local cycle join
changes at most `O(q)` q-windows.  Consequently one such join changes total
factorial excess through depth `H` by at most

\[
 O(BH^2).
\tag{7.1}
\]

Thus a cover with `s` components can be joined by local fresh switches at a
total cost `O(BsH^2)`, provided the required switches exist.  In particular,
the component count `s=O(W/r)` is harmless for `H=o(sqrt(r))` and bounded
`B`:

\[
 BsH^2=O\left(\frac{BWH^2}{r}\right)=o(W).
\tag{7.2}
\]

This explains exactly why the PBBS-scale component bound is sufficient in
the already-proved `H=o(sqrt(r))` regime and why Gaussian-scale joining needs
either history-matched switches or a stronger component bound.  Connectivity
is a real final gate, but it should be attacked after (6.2), not mixed into
the first rounding theorem.

## 8. Recommended attack

The next useful theorem is not a generic discrepancy theorem.  It should
construct one of the following equivalent certificates.

1. A distribution on fresh lower-rainbow cycle covers with the pair bound
   (6.3).
2. A contention-resolution scheme for the cylinder fibres which keeps every
   load in `{c_q,c_q+1}` except for `o(W)` aggregate units.
3. An explicit Boolean-lattice diamond factor at q=1 together with a
   recursive extension whose new depth-q collision cost is summable.

At q=1, the direct sigma-CSP (2.3) is the right finite object.  Hall proves
upper surjectivity only when the middle-degree equations are deleted, while
b-matching proves the middle-degree equations only when upper colours are
deleted.  A proof of their conjunction must use the diamond geometry.  At
higher depth, the same phenomenon becomes the pair-balanced projected
circulation lemma.

This is the strongest reduction supported by the current rotor theorem.  It
also explains why invoking TU, matroid intersection, swap rounding, or the
entropy method from one-point marginals would leave a genuine gap.
