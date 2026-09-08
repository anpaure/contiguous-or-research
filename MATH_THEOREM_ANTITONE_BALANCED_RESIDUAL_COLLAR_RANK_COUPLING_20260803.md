# Antitone balanced residual--collar coupling is exactly optimal

**Date:** 2026-08-03  
**Status:** unconditional integral rank-incidence theorem and exact
Gale--majorization min--max.  No computation is used.  The theorem does
**not** assign named Boolean targets to owners and does not produce literal
owner flags or a word chronology.

## 0. Outcome

The fixed-slack obstruction in
`MATH_THEOREM_COLLAR_HOLE_MAJORISATION_AND_FIXED_SLACK_WHOLE_CHUNK_BARRIER_20260803.md`
comes from the load vector of the parity-block residual chunks, not from the
joint scalar or rank marginals themselves.

Let `W` anonymous owner rows receive two disjoint banks.

* The **residual bank** is a bipartite-matching rank law: a bipartite graph
  `H=(A,B;E)` has edge multiplicities `n_e`, with

  \[
       n(\delta(v))\le W\qquad(v\in A\cup B).
  \tag{0.1}
  \]

  One residual pattern is a matching of `H`.
* The **collar bank** has columns `j\in J`, with integral multiplicities

  \[
                       0\le m_j\le W.
  \tag{0.2}
  \]

  One collar pattern is an arbitrary subset of `J`, so a column may occur
  at most once in one row.

Put

\[
             N_R=\sum_{e\in E}n_e,
             \qquad N_C=\sum_{j\in J}m_j,
             \qquad N=N_R+N_C.
\tag{0.3}
\]

Then the two banks admit an exact joint decomposition into `W` rows such
that

1. every residual edge `e` occurs in exactly `n_e` rows;
2. every residual row is a matching of `H`;
3. every collar column `j` occurs in exactly `m_j` rows;
4. no collar column repeats in one row; and
5. every total row load is either

   \[
                   \left\lfloor{N\over W}\right\rfloor
       \quad\hbox{or}\quad
                   \left\lceil{N\over W}\right\rceil.
   \tag{0.4}
   \]

The maximum in (0.4) is optimal by averaging.  In particular,

\[
                         N\le dW
       \quad\Longrightarrow\quad
                 \hbox{every row has load at most }d.
\tag{0.5}
\]

Thus the anonymous joint rank-incidence problem needs neither additive
depth one nor any asymptotic error: its exact optimum is `C=0`.

For a fixed, possibly very uneven residual load vector, the required depth
has an exact Gale formula.  If

\[
                  h_1^\downarrow\ge\cdots\ge h_W^\downarrow
\tag{0.6}
\]

are the residual row loads, then the least integer total depth admitting
the collar is

\[
 \boxed{
 t_*(h,m)=
 \max\left\{
  h_1^\downarrow,
  \max_{1\le x\le W}
  \left\lceil
  {\displaystyle
   \sum_{i=1}^{x}h_i^\downarrow+
   \sum_{j\in J}(m_j-W+x)_+
  \over x}
  \right\rceil
 \right\}.}
\tag{0.7}
\]

Among all integral residual load vectors of a prescribed total `N_R`, the
equitable vector minimizes (0.7) simultaneously for **every** collar
profile.  This is the precise antitone correction to the parity-block
construction.

## 1. Balanced realization of arbitrary collar columns

### Lemma 1.1 (balanced binary column realization)

Let `m_j` satisfy (0.2).  There is a zero--one matrix

\[
                 y\in\{0,1\}^{W\times J},
                 \qquad \sum_i y_{ij}=m_j,
\tag{1.1}
\]

whose row sums differ by at most one.  Hence, writing

\[
              N_C=q_CW+b,
              \qquad 0\le b<W,
\tag{1.2}
\]

exactly `b` rows have collar load `q_C+1` and the remaining rows have load
`q_C`.

### Proof

For each column `j`, initially choose any `m_j` distinct rows.  This gives
a zero--one matrix with the required column sums.

If rows `u,v` have degrees satisfying

\[
                         d(u)\ge d(v)+2,
\]

then some column is incident with `u` and not with `v`; otherwise
`N(u)\subseteq N(v)` and `d(u)\le d(v)`.  Move that column incidence from
`u` to `v`.  The matrix remains zero--one, every column sum is preserved,
and

\[
 (d(u)-1)^2+(d(v)+1)^2-d(u)^2-d(v)^2
 =-2(d(u)-d(v)-1)<0.
\]

The nonnegative integer potential `sum_i d(i)^2` forces termination.  At
termination all row degrees differ by at most one, and their sum is
`N_C`, which gives (1.2).  `square`

## 2. The exact antitone load law

### Lemma 2.1 (two equitable histograms couple equitably)

Suppose one bank has row loads

\[
 N_R=q_RW+a,
 \qquad
 h_i\in\{q_R,q_R+1\},
 \qquad
 |\{i:h_i=q_R+1\}|=a,
\tag{2.1}
\]

and another has

\[
 N_C=q_CW+b,
 \qquad
 \ell_i\in\{q_C,q_C+1\},
 \qquad
 |\{i:\ell_i=q_C+1\}|=b.
\tag{2.2}
\]

After a permutation of the second bank's rows, the combined loads
`h_i+ell_i` differ by at most one.  Their maximum is exactly

\[
                         \left\lceil{N_R+N_C\over W}\right\rceil.
\tag{2.3}
\]

### Proof

Pair the large rows of the second bank first with the small rows of the
first.  The number of rows which must be large in both banks is then

\[
                            (a+b-W)_+,
\tag{2.4}
\]

the smallest possible value.

If `a+b<W`, no double-large row is needed, and the combined loads are
`q_R+q_C` and `q_R+q_C+1`.  If `a+b=W`, every row has load
`q_R+q_C+1`.  If `a+b>W`, the loads are `q_R+q_C+1` and
`q_R+q_C+2`, with exactly `a+b-W` rows of the latter type.  These are
precisely the floor and ceiling of `(N_R+N_C)/W`.  The zero-remainder and
empty-bank cases are included.  `square`

This is an antitone coupling only at the anonymous-row level.  No owner
labels have yet been fixed, so the row permutation is legitimate.

## 3. Exact joint residual--collar theorem

### Theorem 3.1 (optimal integral joint coupling)

Under (0.1)--(0.3), the five conclusions in Section 0 hold.

### Proof

Replace every edge `e` of `H` by `n_e` parallel copies.  The resulting
bipartite multigraph has maximum degree at most `W`.  The balanced proper
edge-colouring lemma from
`MATH_THEOREM_NONCONTIGUOUS_RANK_LAW_EQUITABLE_INTEGER_DECOMPOSITION_20260803.md`
partitions these copies into exactly `W` matchings whose sizes differ by at
most one.  These are the residual rows, and their load histogram has the
form (2.1).

Apply Lemma 1.1 to the collar columns.  Its row histogram has the form
(2.2).  Permute the collar rows antitonely using Lemma 2.1, and superpose
the two banks.  All marginal and matching conditions survive the row
permutation, while (0.4) follows from (2.3).  Averaging gives the matching
lower bound on the maximum row load, so the result is exact.  Equation
(0.5) is immediate.  `square`

### Boolean-rank specialization

Let the residual rank indices form a path (or a disjoint union of paths),
where adjacent residual ranks may not occur in one owner pattern.  Give
rank `s` multiplicity `n_s`.  The path version of (0.1) is

\[
                  n_s\le W,
                  \qquad n_s+n_{s+1}\le W
                  \quad\hbox{on every residual adjacency}.
\tag{3.1}
\]

Let the disjoint collar ranks have multiplicities `m_j<=W`.  If

\[
                       \sum_s n_s+\sum_jm_j\le dW,
\tag{3.2}
\]

then there are `W` exact combined rank patterns of size at most `d`, with
no adjacent residual ranks and with every collar or residual rank occurring
with its prescribed multiplicity.

The residual and collar rank labels must be disjoint in this statement.  If
one numerical rank is represented in both banks, its two copies must first
be coalesced; otherwise the separate constructions could place both copies
in one row.

For the optimal triangular inventory, the audited noncontiguous-collar
inequalities give exactly (3.1)--(3.2).  Hence its entire anonymous
residual--collar rank inventory fits at depth `d`, with no additive slack.
This reproves the rank-pattern conclusion of the earlier single-graph
equitable decomposition, but now identifies the decisive covariance:
balance each bank and pair their heavy rows antitonely.

## 4. Sharp Gale min--max for a fixed residual load vector

Fix nonnegative integral residual loads `h_1,...,h_W` and collar
multiplicities `m_j<=W`.  At total depth `t`, row `i` has collar capacity

\[
                              c_i=t-h_i.
\tag{4.1}
\]

Necessarily `t>=max_i h_i`.

### Theorem 4.1 (fixed-residual collar min--max)

For an integer `t>=max_i h_i`, a collar zero--one matrix exists if and
only if either of the following equivalent systems holds:

\[
 \sum_{j\in Q}m_j
 \le
 \sum_{i=1}^{W}\min\{t-h_i,|Q|\}
 \qquad(Q\subseteq J),
\tag{4.2}
\]

or, after sorting the collar multiplicities decreasingly,

\[
 \sum_{j=1}^{q}m_j^\downarrow
 \le
 \sum_{i=1}^{W}\min\{t-h_i,q\}
 \qquad(1\le q\le |J|).
\tag{4.3}
\]

Equivalently, after sorting `h` decreasingly,

\[
 \sum_{i=1}^{x}(t-h_i^\downarrow)
 \ge
 \sum_{j\in J}(m_j-W+x)_+
 \qquad(1\le x\le W).
\tag{4.4}
\]

The least feasible `t` is exactly (0.7).

### Proof

Use the integral flow network

\[
 \mathrm{source}\longrightarrow j\longrightarrow i
                    \longrightarrow\mathrm{sink}
\]

with capacities `m_j,1,t-h_i`.  Max-flow/min-cut gives (4.2).  For a fixed
cardinality `q=|Q|`, its left side is largest on the `q` largest columns,
giving (4.3).

The equivalence with (4.4) is the conjugate Gale form proved in the
collar-hole majorization theorem: among `x` rows, column `j` forces
`(m_j-W+x)_+` incidences, while the least capacity of `x` rows is attained
on the `x` largest residual loads.  Solving (4.4) for the least integral
`t`, together with `t>=h_1^downarrow`, gives (0.7).  Integrality of max
flow gives a zero--one matrix whenever the cuts hold.  `square`

## 5. Equitable residual loading is universally optimal

Fix the total residual load

\[
                          N_R=q_RW+a,
                          \qquad 0\le a<W,
\tag{5.1}
\]

and let `bar h` be the equitable vector having `a` entries `q_R+1` and
`W-a` entries `q_R`.

### Theorem 5.1 (simultaneous Gale-cut extremality)

For every nonnegative integral vector `h` of total `N_R`, every collar
profile `m`, and every integer `t>=max_i h_i`,

\[
 \sum_i\min\{t-h_i,q\}
 \le
 \sum_i\min\{t-\bar h_i,q\}
 \qquad(q\ge0).
\tag{5.2}
\]

Consequently

\[
                         t_*(\bar h,m)\le t_*(h,m).
\tag{5.3}
\]

In fact,

\[
 \boxed{
 t_*(\bar h,m)=
 \left\lceil{N_R+N_C\over W}\right\rceil.}
\tag{5.4}
\]

### Proof

Every integral vector of total `N_R` majorizes the equitable vector
`bar h`.  For fixed `t` and `q`, the function

\[
                       f(x)=\min\{t-x,q\}
\]

is concave on `[0,t]`: it is first constant and then affine with slope
`-1`.  Karamata's inequality therefore gives (5.2).  Any `t` feasible for
`h` satisfies `t>=max h>=max bar h`, so (4.3) and (5.2) give (5.3).

The averaging bound gives

\[
                   t_*(\bar h,m)\ge
                   \left\lceil{N_R+N_C\over W}\right\rceil.
\]

Lemma 1.1 and the antitone coupling of Lemma 2.1 attain equality, proving
(5.4).  `square`

The parity-block full-chunk vector is highly majorized.  Theorem 5.1 says
that this is exactly the wrong anonymous load law for collar absorption:
equitable residual loading maximizes the right side of **every** collar
Gale cut simultaneously.

## 6. Exact remaining named-target lift

The theorem closes all of the following at once:

* the scalar lower-load budget;
* exact residual and collar rank multiplicities;
* the residual no-adjacent-rank law;
* integrality of the anonymous row schedule; and
* every anonymous collar Gale cut, at optimal depth `d`.

It does not label the rows by the actual owners

\[
                         T\in{[k]\choose r},
\]

and it does not label rank occurrences by actual Boolean targets.  Once
those labels are restored, a target assigned to row `T` must be contained
in `T`, and all targets placed at different ranks of one row must form one
nested flag.  An antitone permutation of collar rows is then not free: it
changes which owner must contain each target.

For a fixed combined pattern schedule `R_1,...,R_W` and fixed named
boundary families, the remaining lower-side object is the configuration
hypergraph whose vertices are

* the `W` pattern rows;
* the `W` rank-`r` owners; and
* every named nonboundary lower target;

and whose configuration edges choose one row, one owner, and one ordered
owner flag realizing all ranks in that row.  A perfect configuration
matching is exactly an integral named-flag realization.

The rank-separated named-target matroid theorem proves exact containment
and equitable loads after forgetting flag nesting.  The present theorem
proves exact rank patterns and optimal antitone collar covariance after
forgetting owner and target names.  Neither theorem proves that these two
integral projections intersect.

Beyond that named-flag matching, an OR word still requires a compatible
sliding chronology, occurrence labels, residence, and upper-witness guards.
No such implication is claimed here.

## 7. Proof-safe frontier

The unconditional conclusion is

\[
 \boxed{
 \text{joint scalar and rank incidence}
 \Longrightarrow
 \text{an exact depth-}d\text{ schedule}.}
\]

The sole lower-side lift not supplied is

\[
 \boxed{
 \text{anonymous antitone rank schedule}
 \Longrightarrow
 \text{one exact named nested-owner-flag schedule}.}
\]

Thus the collar-hole obstruction is not evidence for additive slack in the
full problem.  It is an exact diagnosis of one badly correlated whole-chunk
face.  At the rank-incidence level, the correct globally rechainized load
law has `C=0`.
