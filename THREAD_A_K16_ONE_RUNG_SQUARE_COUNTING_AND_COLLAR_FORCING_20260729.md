# Counting and collar forcing for one-rung square-corner splices

Date: 2026-07-29

Status: theorem.  The note gives an exact duplicate-square count, a
profile-compressed upper bound for collar-unsafe squares, and a checkable
sufficient inequality forcing a safe one-rung splice.  It also proves that
the scalar upper-colour and bi-resident run/gap counts alone cannot make
that inequality positive at `k=15`.  No parent birail factor and no `k=16`
word are claimed.

## 1. Setup and counting convention

Let

\[
 |X|=2r-1,\qquad W=\binom{2r-1}{r},
\]

and let `F` be a Hamilton cycle of `J(X,r)` satisfying the hypotheses of
`THREAD_A_K16_ONE_RUNG_SQUARE_CORNER_SPLICE_THEOREM_20260729.md`:

* \(\lambda:E(F)\to\binom X{r-1}\) is bijective;
* the parent upper colours \(\upsilon(e)\) cover
  \(\binom X{r+1}\); and
* every cyclic one-run and zero-run has at least \(D\) vertices.

For every \(L\in\binom X{r-1}\), write

\[
 e_L=\lambda^{-1}(L).
\]

An unoriented colour-aware square has two opposite one-rung corners.  The
checker calls each corner a `colour_aware_square`.  We therefore reserve

\[
 Q=\#\{\text{unoriented square cells}\},
 \qquad
 C=2Q=\#\{\text{oriented one-rung corners}\}.
\tag{1.1}
\]

At `k=15`, \(r=8\), \(D=4\), and \(W=6435\).

## 2. The square graph and its unconditional count

For `L`, let

\[
 A_L=\{a,b\}\subseteq X\setminus L
\tag{2.1}
\]

be the two extension elements for which the endpoints of \(e_L\) are
\(L\cup\{a\}\) and \(L\cup\{b\}\).  At the complementary middle vertex
\(\bar L\), the two incident edges of `F` have lower labels

\[
 \bar L\setminus\{c\},\qquad \bar L\setminus\{d\}.
\]

Put

\[
 B_L=\{c,d\}\subseteq X\setminus L.
\tag{2.2}
\]

### Lemma 2.1 (exact local square degree)

The number of oriented square corners whose A cut is \(e_L\) is

\[
 |A_L\cap B_L|.
\tag{2.3}
\]

Consequently

\[
 C=\sum_L|A_L\cap B_L|,
 \qquad
 W\max\{0,4-r\}\le C\le2W.
\tag{2.4}
\]

#### Proof

Choose the endpoint \(P=L\cup\{a\}\) of \(e_L\).  The one-rung theorem
forces the partner edge to have lower colour

\[
 K=\bar P=\bar L\setminus\{a\}
\]

and forces that edge to be incident with \(\bar L\).  This happens exactly
when \(a\in B_L\).  Since `a` is an endpoint extension of \(e_L\) exactly
when \(a\in A_L\), the valid endpoint roles are precisely
\(A_L\cap B_L\).  Both sets have size two in the `r`-set \(X\setminus L\),
so their intersection lies between \(\max\{0,4-r\}\) and two.  Summing
gives (2.4).  \(\square\)

In particular, the local two-subset/marginal argument gives no positive
square lower bound once \(r\ge4\).  This does not exclude a deeper global
Hamilton-cycle theorem forcing \(C>0\).  The observed large catalogues are
genuine correlations of the particular factor, not consequences of this
marginal density calculation.

Define the **square graph** \(\Gamma_F\) on the parent edges by joining
\(e_L\) to \(e_K\) when

\[
 X=L\mathbin{\dot\cup}K\mathbin{\dot\cup}\{a\}
\]

and both edges use the common extension `a`.  It is simple,
\(\Delta(\Gamma_F)\le2\), and its edges are exactly the unoriented square
cells.  Thus

\[
 Q=e(\Gamma_F),\qquad C=2e(\Gamma_F).
\tag{2.5}
\]

## 3. Exact duplicate-safe count

Let

\[
 \mathcal U=\{e\in E(F):\mu(\upsilon(e))=1\}
\tag{3.1}
\]

be the parent edges carrying singleton upper colours.  A square is
duplicate-safe exactly when neither of its two vertices in \(\Gamma_F\)
lies in \(\mathcal U\).

### Theorem 3.1 (duplicate-safe square formula)

The oriented duplicate-safe count is

\[
\begin{aligned}
 C_{\rm dup}
 &=2e\bigl(\Gamma_F[E(F)\setminus\mathcal U]\bigr)\\
 &=C-2d_{\Gamma_F}(\mathcal U)+2e_{\Gamma_F}(\mathcal U),
\end{aligned}
\tag{3.2}
\]

where \(d_{\Gamma_F}(\mathcal U)=\sum_{e\in\mathcal U}d_{\Gamma_F}(e)\)
and \(e_{\Gamma_F}(\mathcal U)\) counts square edges with both endpoints
in \(\mathcal U\).  Hence

\[
 C_{\rm dup}\ge C-2d_{\Gamma_F}(\mathcal U)
              \ge C-4|\mathcal U|.
\tag{3.3}
\]

In particular, a duplicate-safe square exists if and only if
\(\mathcal U\) is not a vertex cover of \(\Gamma_F\).

#### Proof

The number of square-graph edges incident with \(\mathcal U\) is
\(d_{\Gamma_F}(\mathcal U)-e_{\Gamma_F}(\mathcal U)\).  Subtracting these
from \(Q=C/2\) gives (3.2).  The two inequalities use
\(e_{\Gamma_F}(\mathcal U)\ge0\) and
\(\Delta(\Gamma_F)\le2\).  The vertex-cover statement is the same identity
with positivity in place of the count.  \(\square\)

### 3.1 What upper-colour multiplicities alone imply

Put

\[
 M=\binom{2r-1}{r+1}=\frac{r-1}{r+1}W,
 \qquad
 E=W-M=\frac{2W}{r+1}.
\tag{3.4}
\]

For \(r\ge3\), a fixed upper colour `U` has \(r+1\) rank-`r` facets forming a proper
subset of the Hamilton cycle.  The cycle edges induced on a proper set of
\(r+1\) vertices form a linear forest, so

\[
 1\le\mu(U)\le r.
\tag{3.5}
\]

If `t` upper colours have load at least two, then

\[
 \left\lceil\frac E{r-1}\right\rceil\le t\le E,
 \qquad
 |\mathcal U|=M-t,
 \qquad
 |E(F)\setminus\mathcal U|=E+t.
\tag{3.6}
\]

The restriction \(r\ge3\) is necessary here: at \(r=2\), the facets of
the sole upper colour are the whole three-cycle, and its load is `3`, not
at most `r`.  All `k=15` statements lie in the \(r=8\) regime.

For `k=15`, this becomes

\[
 M=5005,\qquad E=1430,\qquad 205\le t\le1430,
\tag{3.7}
\]

and therefore

\[
 3575\le|\mathcal U|\le4800,
 \qquad
 1635\le|E(F)\setminus\mathcal U|\le2860.
\tag{3.8}
\]

Even the maximal square graph has only \(Q\le W=6435\) edges, so the
coarse lower bound \(Q-2|\mathcal U|\) is negative throughout (3.8).
Thus upper-load cardinalities cannot force a duplicate-safe square.

There is also a structural cardinality barrier.  The labels of adjacent
vertices of \(\Gamma_F\) are disjoint `(r-1)`-sets, so \(\Gamma_F\) is a
maximum-degree-two subgraph of \(KG(2r-1,r-1)\).  An odd cycle in this
Kneser graph has length at least \(2r-1\): in each two steps an
`(r-1)`-set changes by at most one element, while the last set of the odd
cycle must be disjoint from the first.  Taking alternating vertices on
paths and even cycles, and \((\ell+1)/2\) vertices on each odd cycle of
length \(\ell\ge2r-1\), gives

\[
 \tau(\Gamma_F)\le\frac r{2r-1}W.
\tag{3.9}
\]

At `r=8`, the right side is `3432`, below the unavoidable
\(|\mathcal U|\ge3575\).  Hence the singleton-edge *cardinality* is large
enough to be a square-graph vertex cover.  This does not prove that the
actual set \(\mathcal U\) is such a cover; it proves that a marginal
counting argument cannot exclude that obstruction.

## 4. Exact run count and endpoint ages

Fix \(x\in X\), and let \(\rho_x\) be the number of cyclic positive runs
of `x` on `F`.  It is also the number of cyclic zero-runs.

### Lemma 4.1 (uniform run count forced by q1 exactness)

For every coordinate,

\[
 \rho_x=\frac W{2r-1},
 \qquad
 \sum_x\rho_x=W.
\tag{4.1}
\]

#### Proof

Let \(N=\binom{2r-2}{r-1}\) be the number of middle vertices containing
`x`.  Counting endpoint incidences of factor edges at those vertices gives
`2N`.  Exactly \(\binom{2r-2}{r-2}\) lower colours contain `x`, and their
edges contribute two such incidences each.  Every edge toggling `x`
contributes one.  Therefore the number of toggling edges is

\[
 2\left(\binom{2r-2}{r-1}-\binom{2r-2}{r-2}\right)
 =\frac{2W}{2r-1}.
\]

Every cyclic positive run has two toggle edges, proving the first identity;
summing it over the `2r-1` coordinates proves the second.  \(\square\)

For an oriented cut endpoint and a coordinate present there, its
**positive age** is the number of consecutive present states exposed at
that endpoint after the cut.  In a cyclic positive run of length at least
`D`, for every \(1\le j\le D-2\) there are exactly two oriented internal
cut endpoints having age `j`, one measured from each end of the run.
Consequently, on any subcatalogue of square corners,

\[
 a_{x,j}\le2\rho_x,qquad b_{x,j}\le2\rho_x,
\tag{4.2}
\]

for the A-positive and complementary-B-positive age counts defined below.

## 5. A profile-compressed collar theorem

Restrict now to the \(C_{\rm dup}\) duplicate-safe oriented corners.  For
a corner `s`, use the exact normal form

\[
 X=L_s\mathbin{\dot\cup}K_s\mathbin{\dot\cup}\{a_s\},
 \qquad
 e_s=\{L_s+a_s,L_s+u_s\},
 \qquad
 f_s=\{K_s+a_s,K_s+v_s\}.
\tag{5.1}
\]

Only the coordinates \(x\in L_s\setminus\{v_s\}\) can violate the seam.
For these rows, let \(\alpha_x(s),\beta_x(s)\) be the A and B positive
endpoint ages.  Put, for \(1\le j\le D-2\),

\[
\begin{aligned}
 a_{x,j}&=|\{s:x\in L_s\setminus\{v_s\},\ \alpha_x(s)=j\}|,\\
 b_{x,j}&=|\{s:x\in L_s\setminus\{v_s\},\ \beta_x(s)=j\}|.
\end{aligned}
\tag{5.2}
\]

Use cumulative notation \(a_{x,\le j}=\sum_{i\le j}a_{x,i}\), with an
empty sum equal to zero, and similarly for `b`.  Define

\[
 M_x=\min_{0\le j\le D-2}
 \left(a_{x,\le j}+b_{x,\le D-2-j}\right).
\tag{5.3}
\]

### Theorem 5.1 (Ferrers collar bound)

The number of duplicate-safe corners that are collar-unsafe for coordinate
`x` is at most \(M_x\).  Hence

\[
 N_{\rm safe}\ge C_{\rm dup}-\sum_{x\in X}M_x.
\tag{5.4}
\]

In particular, the checkable strict inequality

\[
 \boxed{C_{\rm dup}>\sum_xM_x}
\tag{5.5}
\]

forces at least one duplicate-safe, residence-safe one-rung splice.

#### Proof

For fixed `x`, give each candidate one left token of weight
\(\alpha_x(s)\) and one right token of weight \(\beta_x(s)\).  A bad
candidate pairs tokens satisfying

\[
 \alpha_x(s)+\beta_x(s)\le D-1.
\tag{5.6}
\]

Thus the bad candidates form a matching in the Ferrers bipartite graph on
the age classes \(i+j\le D-1\).  For every \(0\le j\le D-2\), all left
tokens of age at most `j` together with all right tokens of age at most
\(D-2-j\) cover every edge of this Ferrers graph.  Conversely, the usual
threshold exchange turns a minimum vertex cover into one of these forms.
By the bipartite matching/vertex-cover theorem, its maximum matching size
is exactly the minimum in (5.3), and the actual bad matching has at most
that many edges.  Taking the union over coordinates gives (5.4), and
(5.5) makes its right side positive.  \(\square\)

The threshold-exchange sentence is not needed for validity of the upper
bound: each displayed threshold set is already a vertex cover.  It shows
that `M_x` is the sharp upper bound obtainable from these two age
histograms alone.

### Corollary 5.2 (the exact `k=15` profile)

At \(D=4\),

\[
 M_x=\min\{b_{x,1}+b_{x,2},\ a_{x,1}+b_{x,1},\
             a_{x,1}+a_{x,2}\}.
\tag{5.7}
\]

Therefore the explicit sufficient inequality is

\[
\boxed{
 C_{\rm dup}>
 \sum_{x\in X}
 \min\{b_{x,1}+b_{x,2},\ a_{x,1}+b_{x,1},\
                         a_{x,1}+a_{x,2}\}.}
\tag{5.8}
\]

There is an even cheaper exact row test.  At a fixed oriented endpoint,
at most one coordinate has a given positive age: it is the coordinate
inserted at the corresponding Johnson transition.  Let \(A_1,A_2\) and
\(B_1,B_2\) be those labels, or a null symbol when the relevant dangerous
row is absent.  Take the null symbols to be slot-specific (equivalently,
compare only nonnull labels in `X`), so two absent rows never create a
collision.  A `k=15` corner is collar-safe exactly when

\[
 A_1\ne B_1,\qquad A_1\ne B_2,\qquad A_2\ne B_1.
\tag{5.9}
\]

These are precisely the possible bad age pairs `(1,1)`, `(1,2)`, and
`(2,1)`.

## 6. The run/gap-only bound is necessarily too weak

By (4.2), choosing `j=0` in (5.3) gives

\[
 M_x\le2(D-2)\rho_x.
\]

Together with (4.1),

\[
 \sum_xM_x\le2(D-2)W.
\tag{6.1}
\]

This is the strongest worst-case bound supplied coordinatewise by the
separated endpoint-age histograms: their marginal capacities permit every
available shallow A age to be paired with a compatible shallow B age.  No
physical factor saturating all of those marginal pairings simultaneously
is asserted.

At `k=15`, (6.1) is

\[
 \sum_xM_x\le4W=25740,
\tag{6.2}
\]

whereas \(C_{\rm dup}\le C\le2W=12870\).  More generally, for every
\(D\ge3\), the strict scalar inequality

\[
 C_{\rm dup}>2(D-2)W
\]

cannot be forced from \(C_{\rm dup}\le2W\).  Thus the scalar
bi-resident run/gap estimates cannot prove existence through (5.5).  The
joint antipodal square/endpoint-age correlation in (5.3), or the exact
three-comparison audit (5.9), is indispensable for this forcing theorem.
A separate global theorem coupling those objects is not ruled out.

This is a no-go for the marginal counting proof, not a construction of a
Hamilton factor with no safe square.

## 7. Combined forcing inequalities

Substituting the exact duplicate formula (3.2) into (5.5) gives the
strongest profile-checkable form:

\[
\boxed{
 C-2d_{\Gamma_F}(\mathcal U)+2e_{\Gamma_F}(\mathcal U)
 >\sum_xM_x.}
\tag{7.1}
\]

The progressively coarser but still rigorous sufficient conditions are

\[
 C-2d_{\Gamma_F}(\mathcal U)>\sum_xM_x
\tag{7.2}
\]

and

\[
 C-4|\mathcal U|>\sum_xM_x.
\tag{7.3}
\]

At `k=15`, (7.1) together with (5.7) is the recommended finite theorem:
it uses only the square graph, the upper-load-one flags, and two capped
endpoint ages on each rail.  It does not construct any child path before
certifying positivity.

The exact inclusion--exclusion of the three age-label collisions, including
the crossed-swap refund, and the minimal abstract obstruction are proved in
`THREAD_A_K16_ONE_RUNG_EXACT_COLLISION_KERNEL_AND_TRACE_OBSTRUCTION_20260729.md`.

## 8. Independent audit of the current checker

The static audit of
`scratch/audit_k16_biresident_one_rung_splice_20260729.py` found no
mathematical false-PASS gap.

* For an A edge `e`, it sets \(L=\lambda(e)\), locates the complementary
  parent vertex \(\bar L\), and scans its two incident edges `f`.  Its
  endpoint test is equivalent to
  \(f=\lambda^{-1}(\bar P)\) and (2.3).
* Its two `upper_load >= 2` rows are exactly the two duplicate conditions.
* Its A and complementary-B path orientations are the orientations used in
  the one-rung theorem.
* Its full output residence scan checks internally bounded positive runs,
  not output bi-residence.  Under the audited parent hypotheses this is
  equivalent to the six normal-form rows and hence to (5.9).
* `colour_aware_squares` and `duplicate_safe_squares` count oriented
  corners `C`, not unoriented square cells `Q`.

Two implementation cautions remain.  The emitted JSON key named `cycle`
contains a linear path.  Also, the checker currently reconstructs and
scans a length-`2W` child path for every duplicate-safe corner, costing
\(O(CW)\) after suppressing fixed-rank factors.  The theorem gives a
proof-safe \(O(CrD)\) prefilter: precompute capped endpoint ages, apply
(5.9), and replay the full child path only for the first passing row.  This
is an efficiency recommendation, not a correctness repair.

No input birail PASS or one-rung output report was present during this
audit, so the numerical sides of (5.8) and (7.1) have not yet been
evaluated.

## 9. Heuristic boundary (not used in any theorem)

If the two 2-subsets \(A_L,B_L\) in Section 2 behaved independently, one
would expect \(|A_L\cap B_L|=4/r\).  If the two endpoint-age label streams
also mixed independently at `k=15`, the three bad comparisons in (5.9)
would have total first-moment intensity about `3/15`.  These heuristics
suggest that a structured birail PASS may contain safe corners.

Neither independence statement follows from Hamiltonicity, q1 exactness,
upper completeness, or bi-residence.  The square involution may correlate
the two streams, and the singleton-upper set may cover the entire square
graph.  Therefore no heuristic estimate is used in (3.2), (5.4), or
(7.1).
