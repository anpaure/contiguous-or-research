# AD16: global cross-cut fusion after the linear PBBS dominance seam

Date: 2026-07-25

Method: pure mathematics only. No web search, computation, finite search,
solver, or long-running job is used.

## 0. Exact outcome

Let \(X_i\) be a cyclic rank-\(k\) Johnson owner trajectory, let
\(\mathcal C\) be a set of \(J\) cut edges, and let \(H\) be the target
depth.  For a cut between \(X_{c-1}\) and \(X_c\), write

\[
 P^{(c)}_{s,t}=\bigcap_{i=c-s}^{c+t-1}X_i,
 \qquad s,t\ge1.
 \tag{0.1}
\]

The one-cut \(4H-1\) dominance seam is taken as proved.  This report
attacks only its global fusion and obtains the following exact boundary.

1.  The diagonal identity

    \[
    P^{(c)}_{s,t}=P^{(c+1)}_{s+1,t-1}
    \tag{0.2}
    \]

    quotients local seam cells precisely by their two global owner
    endpoints.  At depth \(q=s+t-1\), the number of resulting endpoint
    classes is

    \[
    \boxed{
    |F_q(\mathcal C)|=\sum_{j=1}^{J}\min(q,g_j),}
    \tag{0.3}
    \]

    where \(g_1,\ldots,g_J\) are the cyclic cut gaps.  Thus identity
    sharing is strong for dense cut clusters and gives no saving at depth
    \(q\) when all gaps are at least \(q\).

2.  A finite Johnson owner block has a **boundary-compatible global
    Pareto replacement**.  A block of \(M+1\) consecutive literal owner
    letters may be replaced by at most \(2M+1\) nonzero letters while
    preserving every old ambient interval OR and adding every nonempty
    floor-correct consecutive lower intersection in the block.  If
    \(M\le k-1\), the new length is exactly \(2M+1\), hence the exact
    increase is \(M\).  The prefix and suffix identities needed for
    literal splicing are proved below; they were not part of the earlier
    self-contained cluster statement.

    Applied to \(K\) cut clusters whose expanded owner blocks are
    pairwise disjoint, of diameters
    \(\Delta_1,\ldots,\Delta_K\), and satisfying
    \(\Delta_\alpha+2H-1\le k-1\), the exact local-regime increase is

    \[
    \boxed{
      E=\sum_{\alpha=1}^{K}(\Delta_\alpha+2H-1).}
    \tag{0.4}
    \]

    Consequently this replacement has \(E=o(HJ)\) exactly under

    \[
      K=o(J),\qquad
      \sum_\alpha\Delta_\alpha=o(HJ).
    \tag{0.5}
    \]

    It is a genuine positive literal fusion theorem.  It is not yet an
    instantiation in the frozen first-band facet-core word, because that
    baseline represents the owners by overlapping intervals rather than
    containing them as consecutive owner letters.

3.  There is a sharp no-go for **identity-only standalone gluing**.  For
    \(H\)-separated cuts, one fixed depth can contain
    \((H-1)J\) distinct floor-correct targets.  Any standalone seam atlas
    then has length at least \((H-1)J\), even with arbitrary helper
    letters.  Hence (0.2) cannot by itself yield \(o(HJ)\).

4.  Baseline recycling changes the lower bound qualitatively.  Suppose a
    word of length \(M+e\) represents \(M\) distinct mandatory targets of
    one rank and \(D_q\) distinct targets at each of the next \(H\) lower
    ranks.  Then literal chronology forces the new exact inequality

    \[
    \boxed{
      \sum_{q=1}^{H}(D_q-e)_+\le Me,}
    \qquad
    \boxed{
      e\ge {\sum_{q=1}^{H}D_q\over M+H}.}
    \tag{0.6}
    \]

    In the critical separated regime \(M=HJ\) and
    \(D_q\ge qJ/\mu\), this gives

    \[
      \boxed{
      e\ge {J(H+1)\over 2\mu(J+1)}.}
    \tag{0.7}
    \]

    Thus full baseline reuse still needs an opening toll of order \(H\),
    but endpoint counting does not force order \(HJ\) excess.

5.  More structurally, for bounded \(\mu\), any \(M+o(M)\) realization
    in the critical regime must put strict depth-\(\Theta(H)\) lower flags
    on a positive fraction of the mandatory starts.  A single physical letter can combine flag
    increments from different starts only when their selected pins all lie
    in every corresponding outer mandatory target.  Therefore a successful
    fusion must contain compatible pin bundles of size

    \[
       \boxed{
       \left({1\over2\mu}-o(1)\right)H.}
    \tag{0.8}
    \]

    The same condition holds independently on the right-endpoint
    skeleton.  This is a directly testable PBBS-specific gate for any
    packet satisfying the displayed critical separated,
    bounded-multiplicity hypotheses and assigned to one near-baseline
    realization; those hypotheses are not proved here for the canonical
    PBBS braid.  Equality of target states supplies neither the bundles nor
    their chronology.

6.  No stronger excess obstruction follows from Johnson legality,
    \(H\)-separated forced cuts, distinct floor-correct targets, or even an
    integral odd-graph lift.  An explicit fixed-core sliding trajectory
    with \(J\) forced separated collars has a literal word of length

    \[
       \boxed{M+2H}
    \tag{0.9}
    \]

    representing every lower and upper window through depth \(H\), while
    every standalone crossing atlas needs \(\Omega(HJ)\) letters.  For
    \(J\to\infty\), its added cost \(2H=o(HJ)\).  Hence order \(H\) is a
    sharp universal lower-bound scale on this fixed-core model, although
    no universal \(O(H)\) compiler for arbitrary Johnson paths is proved.

The lane is therefore exhausted at an exact boundary.  Global diagonal
sharing and mandatory-position counting do not prove coefficient one and
do not refute it.  If a canonical packet satisfies the critical defect
hypotheses above, the remaining positive PBBS theorem must build the
\(\Omega(H)\)-way compatible nested flags inside the actual first-band
facet-core braid.  A negative theorem on that route must prove, uniformly
over all admissible witness choices, that its bundle capacity is \(o(H)\),
or prove another literal-chronology incompatibility.  The closed
same-phase \(p+O(1)\) compiler is not used or reopened here.

## 1. The exact diagonal quotient

Work first on a cyclic owner trace of length \(\ell\), with all indices
modulo \(\ell\), and assume

\[
 1\le q\le H<\ell.
\]

Equivalently, all windows below may be read in their unique nonwrapping
integer lifts.  Put

\[
 P_{a,q}=\bigcap_{h=0}^{q}X_{a+h}.
 \tag{1.1}
\]

A \(q\)-transition owner window crosses the cut \(c\) exactly when its
start belongs to

\[
 \{c-q,c-q+1,\ldots,c-1\}.
 \tag{1.2}
\]

### Lemma 1.1 (global endpoint classes)

If \(s+t-1=q\), then

\[
 \boxed{P^{(c)}_{s,t}=P_{c-s,q}.}
 \tag{1.3}
\]

More generally,

\[
 \boxed{
 P^{(c)}_{s,t}
 =P^{(d)}_{s+d-c,\,t+c-d}}
 \tag{1.4}
\]

whenever all shifted parameters are positive and lie in the chosen
charts.  Thus, in the ambient chart containing cells at every cut, the
equivalence relation generated by the adjacent identity (0.2) has classes
exactly the global owner intervals \([a,a+q]\).  Restricting afterward to
selected-cut cells gives the required quotient; if intermediate cuts are
not displayed, formula (1.4) identifies the equal cells directly.

#### Proof

Both sides of (1.3) are the intersection over

\[
 [c-s,c+t-1]=[c-s,c-s+q].
\]

Formula (1.4) preserves the same two endpoints.  Conversely, changing the
displayed cut by one while preserving those endpoints changes
\((s,t)\) to \((s+1,t-1)\) or its inverse.  Repeating reaches every local
description of the same global interval.  No different global interval is
identified by these moves. \(\square\)

For a cut set \(\mathcal C\), define

\[
 F_q(\mathcal C)
 =\bigcup_{c\in\mathcal C}
   \{c-q,\ldots,c-1\}.
 \tag{1.5}
\]

### Lemma 1.2 (exact truncated-gap ledger)

If the cyclic gaps between consecutive cuts are
\(g_1,\ldots,g_J\), then

\[
 \boxed{
 |F_q(\mathcal C)|=\sum_{j=1}^{J}\min(q,g_j).}
 \tag{1.6}
\]

#### Proof

Partition the cycle into the \(J\) half-open inter-cut arcs ending at the
successive cuts.  In an arc of length \(g_j\), precisely its last
\(\min(q,g_j)\) start positions are within backward distance \(q\) of the
ending cut.  The arcs are disjoint and exhaust the cycle. \(\square\)

The diagonal identity may be supplemented by accidental equality of
different global intervals.  To separate the two phenomena, let
\(E_q\subseteq F_q(\mathcal C)\) be a family of floor-correct starts and
put

\[
 \mu_q=\max_T
 \bigl|\{a\in E_q:P_{a,q}=T\}\bigr|.
 \tag{1.7}
\]

The number \(D_q\) of distinct target values in this family satisfies

\[
 \boxed{
 D_q\ge\left\lceil {|E_q|\over\mu_q}\right\rceil.}
 \tag{1.8}
\]

Every one of these sets has the common floor rank \(k-q\).  In a literal
word, chosen intervals for distinct equal-rank sets have distinct left
endpoints: two intervals with one left endpoint are nested, hence their
ORs are comparable, while two distinct sets of one cardinality are
incomparable.  Therefore every standalone chart for them has length at
least \(D_q\).

In particular, when all cut gaps are at least \(q\), all starts are
floor-correct, and \(\mu_q\le\mu\), every standalone chart obeys

\[
 \boxed{L\ge {qJ\over\mu}.}
 \tag{1.9}
\]

This is the exact obstruction to treating (0.2) as a global word.  The
identity removes duplicate descriptions of one global interval; it does
not give a common literal endpoint for different target values.

## 2. Boundary-compatible global Pareto replacement

This section proves the positive chronology theorem used in (0.4).

Let

\[
 X_0,X_1,\ldots,X_M\in\binom{\Omega}{k},
 \qquad
 X_{i+1}=X_i-\{r_i\}+\{a_i\}
 \tag{2.1}
\]

be a finite Johnson path.  For \(0\le a\le b\le M\), put

\[
 L_{a,b}=\bigcap_{i=a}^{b}X_i,
 \qquad
 U_{a,b}=\bigcup_{i=a}^{b}X_i.
 \tag{2.2}
\]

Call \(L_{a,b}\) floor-correct when

\[
 |L_{a,b}|=k-(b-a).
 \tag{2.3}
\]

For each coordinate, split its indicator on \(0,\ldots,M\) into maximal
positive runs \([\alpha,\beta]\), and attach the point

\[
 p=(-\alpha,\beta).
 \tag{2.4}
\]

A query interval \([a,b]\) has point \(q=(-a,b)\).  A run contains the
query exactly when \(p\ge q\) coordinatewise.

### Lemma 2.1 (internal-run criterion)

The query \(L_{a,b}\) is floor-correct if and only if there is no maximal
positive run satisfying

\[
 a<\alpha\le\beta<b.
 \tag{2.5}
\]

Equivalently, no run point is strictly southwest of \(q=(-a,b)\).

#### Proof

Map every coordinate of \(X_a\setminus L_{a,b}\) to its first departure
among the \(b-a\) internal transitions.  This map is injective.

If (2.5) occurs, the departure at the end of that internal run is not the
first departure of a coordinate present at \(X_a\): the coordinate was
either absent initially or had already departed before its displayed
re-entry.  Hence at most \(b-a-1\) transitions are used and

\[
 |L_{a,b}|\ge k-(b-a)+1,
\]

so the query is not floor-correct.

Conversely, if (2.3) fails, fewer than \(b-a\) initial coordinates depart.
Some transition is therefore not the first departure of an initial
coordinate.  The coordinate removed there is noninitial or has departed
and re-entered.  Its current positive run starts after \(a\) and ends
before \(b\), giving (2.5). \(\square\)

Take the Pareto-minimal distinct run points, order them with first
coordinate increasing and second coordinate decreasing, and construct an
east-before-south unit path \(\Gamma\) through them from
\((-M,M)\) to \((0,0)\).  Every vertex \(z=(u,v)\) defines the valid owner
interval

\[
 I_z=[-u,v]
 \tag{2.6}
\]

and the set-letter

\[
 W_z=\bigcap_{i\in I_z}X_i.
 \tag{2.7}
\]

The path has exactly \(2M+1\) vertices.  The standard rectangle argument
gives the following fact: if a query point \(q\) has no run point strictly
southwest of it and \(p\ge q\) is a run point, then

\[
 \Gamma\cap[q,p]\ne\varnothing.
 \tag{2.8}
\]

Indeed, descend below \(p\) to a Pareto minimum.  If that minimum is
west/north of \(q\), move forward to the vertical line of \(q\); the
east-before-south convention and southwest exclusion prevent premature
descent.  If it is east/south, use the backward horizontal analogue.

Emit the nonzero \(W_z\)'s in the **reverse** order of \(\Gamma\), from
\((0,0)\) to \((-M,M)\), and call the resulting word \(Z\).

### Theorem 2.2 (boundary-compatible Pareto refinement)

The word \(Z\) has length at most \(2M+1\) and satisfies all of the
following.

1. Every nonempty floor-correct \(L_{a,b}\) is a contiguous OR of \(Z\).
2. Every \(U_{a,b}\) is a contiguous OR of \(Z\).
3. Every \(U_{0,b}\) is a prefix OR of \(Z\).
4. Every \(U_{a,M}\) is a suffix OR of \(Z\).
5. For arbitrary surrounding words \(A,B\), every set represented by an
   interval of

   \[
   A\,X_0X_1\cdots X_M\,B
   \tag{2.9}
   \]

   remains represented by an interval of

   \[
   A\,Z\,B.
   \tag{2.10}
   \]

If \(M\le k-1\), no \(W_z\) is zero, so \(|Z|=2M+1\) and (2.10) increases
the block length by exactly \(M\).

#### Proof

For a floor-correct query \(q=(-a,b)\), a vertex \(z\ge q\) has
\(I_z\supseteq[a,b]\), hence \(W_z\subseteq L_{a,b}\).  Conversely, take
\(x\in L_{a,b}\) and its positive run point \(p\ge q\).  Lemma 2.1 and
(2.8) give \(z\in\Gamma\cap[q,p]\).  Then \(I_z\) lies inside the run of
\(x\), so \(x\in W_z\).  Therefore

\[
 \boxed{
 L_{a,b}=
 \bigcup_{\substack{z\in\Gamma\\z\ge(-a,b)}}W_z.}
 \tag{2.11}
\]

Along either orientation of \(\Gamma\), the two coordinate inequalities
select a suffix and a prefix, so the selected vertices form a contiguous
subpath.

The singleton query \([i,i]\) is floor-correct.  Applying (2.11) and then
taking a union over \(a\le i\le b\) gives

\[
 \boxed{
 U_{a,b}=
 \bigcup_{\substack{z\in\Gamma\\I_z\cap[a,b]\ne\varnothing}}W_z.}
 \tag{2.12}
\]

In the reversed word, both endpoints of \(I_z\) are nondecreasing.  The
condition \(I_z\cap[a,b]\ne\varnothing\) is

\[
 \text{left}(I_z)\le b,
 \qquad
 \text{right}(I_z)\ge a.
 \tag{2.13}
\]

The first condition is a prefix and the second is a suffix; their
intersection is contiguous.  When \(a=0\), only the prefix restriction
remains, proving item 3.  When \(b=M\), only the suffix restriction
remains, proving item 4.

Deleting zero \(W_z\)'s changes no OR and preserves every convex subpath,
prefix, and suffix among the surviving positions.  This proves items 1--4
without a restriction on \(M\).

For item 5, classify an old interval by how it meets the owner block.  An
internal interval uses item 2.  An interval crossing only the left
boundary is an unchanged suffix of \(A\) followed by some \(U_{0,b}\),
so item 3 gives a literal replacement.  The right-boundary case uses item
4.  An interval crossing both boundaries uses all of \(Z\), whose OR is
\(U_{0,M}\).  Intervals disjoint from the block are unchanged.  This
exhausts all cases.

Finally, every \(I_z\) has at most \(M\) transitions, so

\[
 |W_z|\ge k-M.
\]

If \(M\le k-1\), all \(2M+1\) letters are nonzero. \(\square\)

### Corollary 2.3 (exact clustered replacement cost)

Let a cluster of selected cuts have extreme indices \(c_{\min}\) and
\(c_{\max}\), and put

\[
 \Delta=c_{\max}-c_{\min}.
 \tag{2.14}
\]

Every crossing owner window of at most \(H+1\) owners lies in

\[
 X_{c_{\min}-H},\ldots,X_{c_{\max}+H-1},
 \tag{2.15}
\]

whose edge span is

\[
 M=\Delta+2H-1.
 \tag{2.16}
\]

If (2.15) occurs as a literal consecutive owner block, Theorem 2.2
replaces it by a boundary-compatible word covering every upper crossing
union and every nonempty floor-correct lower crossing intersection.  When
\(M\le k-1\), its exact added length is

\[
 \boxed{\Delta+2H-1.}
 \tag{2.17}
\]

For \(K\) clusters whose expanded blocks (2.15) are pairwise
nonoverlapping literal substrings, and with
\(M_\alpha=\Delta_\alpha+2H-1\le k-1\) for every \(\alpha\), summing
(2.17) gives (0.4), and

\[
 {E\over HJ}
 = {\sum_\alpha\Delta_\alpha\over HJ}
   +\left(2-{1\over H}\right){K\over J}.
 \tag{2.18}
\]

Both terms are nonnegative, proving the criterion (0.5) in this exact
nonzero regime.  If expanded blocks overlap, they must first be merged.
If some \(M_\alpha>k-1\), Theorem 2.2 still gives an increase at most
\(M_\alpha\) after zero-cell deletion, but the exact formula and the lower
bound below are no longer asserted.

Still in the exact nonzero regime, if all selected cuts are mutually
\(H\)-separated along each cluster and cluster \(\alpha\) contains
\(r_\alpha\) cuts, then

\[
 \Delta_\alpha\ge H(r_\alpha-1),
\]

and hence

\[
 \Delta_\alpha+2H-1\ge Hr_\alpha.
 \tag{2.19}
\]

Thus this exact staircase replacement costs at least \(HJ\) in the
separated regime.  Diagonal cell equality has been fully used; a further
gain must thread the flags through other mandatory baseline starts.

## 3. Exact mandatory-baseline span inequality

The next theorem allows arbitrary recoding, arbitrary helper letters, and
arbitrary witness lengths.  It is not an appended-chart bound.

### Theorem 3.1 (two-sided baseline span budget)

Let a nonzero literal word \(w\) have length

\[
 |w|=M+e,
 \qquad M\ge1,\quad e\ge0.
 \tag{3.1}
\]

Suppose \(w\) represents

* \(M\) distinct mandatory targets of rank \(r\); and
* \(D_q\) distinct targets of rank \(r-q\), for every
  \(1\le q\le H\).

Then

\[
 \boxed{
 \sum_{q=1}^{H}(D_q-e)_+\le Me.}
 \tag{3.2}
\]

Consequently

\[
 \boxed{
 e\ge {\sum_{q=1}^{H}D_q\over M+H}.}
 \tag{3.3}
\]

The same conclusions hold if every use of left endpoints in the proof is
replaced by right endpoints.

#### Proof

Choose one witnessing interval \([\ell_i,r_i]\) for each mandatory target.
Distinct equal-rank target intervals form a containment antichain.  Hence
their left endpoints are \(M\) distinct positions, and their right
endpoints are also \(M\) distinct positions, inside \([M+e]\).

The minimum sum of an \(M\)-subset of \([M+e]\) is
\(1+\cdots+M\), and the maximum is
\((e+1)+\cdots+(e+M)\).  Therefore

\[
 \sum_{i=1}^{M}(r_i-\ell_i)
 =\sum_i r_i-\sum_i\ell_i
 \le Me.
 \tag{3.4}
\]

At lower rank \(r-q\), the \(D_q\) chosen witness starts are distinct.
At least

\[
 M+D_q-(M+e)=D_q-e
 \tag{3.5}
\]

of them coincide with mandatory starts, when this number is positive.

Fix a mandatory start \(\ell_i\).  Every lower-rank witness with this start
must end strictly before \(r_i\): a later endpoint would make its OR
contain the mandatory target, while an equal endpoint would give the same
set, both impossible at smaller rank.  Witnesses belonging to different
lower ranks have distinct endpoints.  Thus if \(h_i\) lower ranks use
\(\ell_i\), then

\[
 h_i\le r_i-\ell_i.
 \tag{3.6}
\]

Summing (3.5) over depths and (3.6) over mandatory starts, then using
(3.4), proves (3.2).  Since

\[
 (D_q-e)_+\ge D_q-e,
\]

(3.2) gives

\[
 \sum_qD_q-He\le Me,
\]

which is (3.3).  Reversing the word proves the right-endpoint version.
\(\square\)

### Corollary 3.2 (critical separated packet)

Assume one packet has

\[
 M=HJ
 \tag{3.7}
\]

mandatory targets and that, for a fixed \(\mu\ge1\),

\[
 D_q\ge {qJ\over\mu}
 \qquad(1\le q\le H).
 \tag{3.8}
\]

Then every literal realization has

\[
 \boxed{
 e\ge {J(H+1)\over2\mu(J+1)}.}
 \tag{3.9}
\]

#### Proof

Insert

\[
 \sum_{q=1}^{H}D_q
 \ge {JH(H+1)\over2\mu}
\]

and \(M=HJ\) into (3.3). \(\square\)

For bounded \(\mu\) and \(J\to\infty\), the required opening toll is
\(\Omega(H)\).  This is compatible with \(o(HJ)\); it proves that a
successful global compiler must open a whole depth-\(H\) flag once rather
than add only \(O(1)\) positions.

## 4. Flag concentration and compatible-pin capacity

The proof of Theorem 3.1 contains more structural information.

Let \(h_p\) be the number of lower ranks whose chosen witness shares a
given mandatory left endpoint \(p\).  Put

\[
 R=\sum_p h_p.
 \tag{4.1}
\]

Then

\[
 \boxed{
 R\ge\sum_{q=1}^{H}(D_q-e)_+
 \ge\sum_{q=1}^{H}D_q-He.}
 \tag{4.2}
\]

For every \(1\le d\le H\), if \(N_d=|\{p:h_p\ge d\}|\), then

\[
 R\le N_dH+(M-N_d)(d-1).
\]

Therefore

\[
 \boxed{
 N_d\ge
 \max\left\{0,
 \left\lceil{R-M(d-1)\over H-d+1}\right\rceil
 \right\}.}
 \tag{4.3}
\]

Thus a large total incidence \(R\) forces deep flags on many mandatory
starts; it cannot be hidden at a few exceptional endpoints.

At one such start \(p\), order its represented lower targets increasingly
by inclusion:

\[
 T_{p,1}\subsetneq T_{p,2}\subsetneq\cdots
 \subsetneq T_{p,h_p}\subsetneq U_p,
 \tag{4.4}
\]

where \(U_p\) is the outer mandatory target.  Choose pins

\[
 \xi_{p,1}\in T_{p,1},
 \qquad
 \xi_{p,j}\in T_{p,j}\setminus T_{p,j-1}\quad(j\ge2).
 \tag{4.5}
\]

These choices are possible because the targets are nonempty and the
inclusions are strict.

For the resulting request set

\[
 \mathcal Q=\{(p,j):1\le j\le h_p\},
\]

define \(\chi\) to be the largest cardinality of a subfamily
\(B\subseteq\mathcal Q\) such that the starts \(p\) in \(B\) are distinct
and

\[
 \boxed{
 \{\xi_{p,j}:(p,j)\in B\}
 \subseteq
 \bigcap_{(p,j)\in B}U_p.}
 \tag{4.6}
\]

When \(R=0\), the assertion below is vacuous.  Hence assume \(R>0\), so
\(\mathcal Q\ne\varnothing\) and \(\chi\ge1\).

### Lemma 4.1 (compatible-pin necessity)

Every literal realization obeys

\[
 \boxed{M+e\ge {R\over\chi}.}
 \tag{4.7}
\]

#### Proof

The common-start witness intervals in (4.4) have strictly increasing right
endpoints.  Pin \(\xi_{p,j}\) first appears in the disjoint word-position
annulus added between the witnesses for \(T_{p,j-1}\) and \(T_{p,j}\)
(with the evident initial annulus for \(j=1\)).  Assign the request
\((p,j)\) to one letter in that annulus containing its pin.  Therefore one
word position receives at most one request from any fixed start \(p\).

If one word position receives requests from several starts, its set-letter
contains all their pins.  It lies in every corresponding mandatory witness
interval, and every letter inside a witness for \(U_p\) is a subset of
\(U_p\).  Hence its assigned requests satisfy (4.6), so their number is at
most \(\chi\).  There are \(M+e\) positions and \(R\) requests, proving
(4.7). \(\square\)

Under (3.7)--(3.8) and \(e=o(HJ)\), equations (4.2) and (4.7) give

\[
 R\ge
 \left({1\over2\mu}-o(1)\right)MH
\]

and hence

\[
 \boxed{
 \chi\ge
 \left({1\over2\mu}-o(1)\right)H.}
 \tag{4.8}
\]

Applying the right-endpoint version of Theorem 3.1 gives an independent
right-handed bundle condition.  The conditions are necessary, not
sufficient: after finding the bundles one must still order their letters
so that every annulus is a literal contiguous interval.

For any canonical PBBS packet satisfying (3.7)--(3.8), with bounded
\(\mu\), globally required target values, and one assigned near-baseline
realization, this is the exact surviving edge-distribution test.  One may
construct the \(\Omega(H)\)-way bundles in the actual first-band
facet-core braid, with one chronology on both endpoint skeletons.  A
negative argument must instead bound the capacity by \(o(H)\) uniformly
over all admissible endpoint matchings and word-derived flags, or provide
a low-capacity valid pin choice for every such matching.  A bound for one
preselected canonical flag or pin system would not exclude a compiler
using different witnesses.

## 5. A sharp fixed-core global fusion model

The preceding \(\Omega(H)\) opening toll has the correct generic order.

Fix integers \(m,H,J\) with

\[
 H\ge2,\qquad J\ge1,
 \qquad
 M=2JH\le m+H.
 \tag{5.1}
\]

Choose a set \(G\) of size

\[
 |G|=m+1-H
 \tag{5.2}
\]

and distinct active coordinates
\(a_0,\ldots,a_{M-1}\), with indices modulo \(M\).  They fit in a ground
set of size \(2m+1\) by (5.1).  Define

\[
 \boxed{
 X_i=G\cup\{a_i,a_{i+1},\ldots,a_{i+H-1}\}.}
 \tag{5.3}
\]

This is a cyclic rank-\((m+1)\) Johnson trajectory: the transition from
\(X_i\) to \(X_{i+1}\) removes \(a_i\) and inserts \(a_{i+H}\).

### Theorem 5.1 (baseline-relative sliding compiler)

Put

\[
 E_j=G\cup\{a_j\}.
 \tag{5.4}
\]

Emit one period

\[
 E_0,E_1,\ldots,E_{M-1},
\]

repeat its first \(2H-1\) letters, and append the one letter \(G\).  The
result is a nonzero literal word of exact length

\[
 \boxed{M+2H}
 \tag{5.5}
\]

which represents every lower intersection and every upper union of at
most \(H+1\) consecutive owners in (5.3), including every owner and every
depth-one first-band core.

#### Proof

For \(0\le q\le H-1\), direct intersection gives

\[
 \boxed{
 \bigcap_{h=0}^{q}X_{i+h}
 =G\cup\{a_{i+q},\ldots,a_{i+H-1}\}
 =\bigcup_{j=i+q}^{i+H-1}E_j.}
 \tag{5.6}
\]

At depth \(H\), the intersection is the appended letter \(G\).  For
\(0\le q\le H\), direct union gives

\[
 \boxed{
 \bigcup_{h=0}^{q}X_{i+h}
 =G\cup\{a_i,\ldots,a_{i+H+q-1}\}
 =\bigcup_{j=i}^{i+H+q-1}E_j.}
 \tag{5.7}
\]

Every displayed index interval has at most \(2H\) letters.  Repeating the
first \(2H-1\) letters therefore linearizes every cyclic interval in
(5.6)--(5.7).  All letters contain \(G\), so they are nonzero. \(\square\)

The \(M\) owners are distinct mandatory same-rank targets.  For every
\(0\le q\le H-1\), the \(M\) lower targets in (5.6) are distinct and
floor-correct; at \(q=H\) there is the one common target \(G\).  Theorem
3.1 therefore gives the exact endpoint lower bound

\[
 \boxed{
 e\ge {M(H-1)+1\over M+H},}
 \tag{5.8}
\]

while Theorem 5.1 gives excess \(2H\).  Thus the \(\Theta(H)\) endpoint
lower-bound scale is sharp on this fixed-core model; this is not a
universal \(O(H)\)-excess theorem for arbitrary Johnson paths.

There is simultaneously a separated standalone obstruction.  For each
\(0\le t<J\), the coordinate

\[
 a_{(2t+1)H-1}
\]

has a positive owner run of exactly \(H\) owners,

\[
 [2tH,(2t+1)H-1].
 \tag{5.9}
\]

Its insertion-to-departure edge collar is

\[
 [\,2tH-1,\,(2t+1)H-1\,]
\]

in edge indices.  Consecutive displayed collars have \(H-1\) intervening
edge indices, so one representative chosen from each collar has cyclic
index distance at least \(H\).  Any cut decomposition with no internally
bounded positive run of at most \(H\) owners must hit every collar, and
therefore contains a \(J\)-cut subfamily with that separation.  Additional
cuts need not themselves be separated.

At depth \(q=H-1\), formula (5.6) becomes

\[
 \boxed{
 \bigcap_{h=0}^{H-1}X_{i+h}
 =G\cup\{a_{i+H-1}\}.}
 \tag{5.10}
\]

The \(H-1\) crossing-start families belonging to the \(J\) separated cuts
are disjoint, and all their targets in (5.10) are distinct.  Hence every
standalone occurrence-preserving seam atlas has length at least

\[
 \boxed{J(H-1).}
 \tag{5.11}
\]

Nevertheless the integrated word (5.5) has added length only \(2H\),
which is \(o(HJ)\) when \(J\to\infty\).

Finally, the construction is integrally odd-graph legal.  Put

\[
 A_i=[2m+1]\setminus X_i,
 \qquad
 B_i=X_i\cap X_{i+1}.
 \tag{5.12}
\]

Then \(A_i,B_i,A_{i+1}\) are rank-\(m\) sets, with consecutive pairs
disjoint, so

\[
 A_i,B_i,A_{i+1}
\]

is a literal two-edge odd-graph path for every \(i\), and the indices close
cyclically.  It is not proved that this alternating cycle is a component
of the canonical PBBS factor.  That qualification is decisive: the model
rules out a general Johnson/odd-graph excess no-go but does not settle the
canonical PBBS bundle capacity.

## 6. Audit of the decisive steps

### 6.1 Equality is not chronology

The domain of the adjacent identity is exact: in an \(H\times H\) chart,

\[
 t\ge2,
 \qquad
 s+1\le H.
\]

Under the triangular target restriction \(s+t-1\le H\), the second
inequality is automatic.  Equation (1.6) counts the complete transitive
closure of these identifications.  No additional literal position is
created by state equality.

### 6.2 Independent audit of boundary substitution

The new step in Theorem 2.2 is not the internal Pareto identity but the
two ambient boundary cases.  In the reversed path order, owner-interval
left endpoints and right endpoints are both nondecreasing.  Therefore:

* intervals meeting \([0,b]\) form a prefix;
* intervals meeting \([a,M]\) form a suffix; and
* intervals meeting a general \([a,b]\) form their contiguous
  prefix--suffix intersection.

These statements remain true after zero cells are deleted.  The four
possible interactions of an old ambient interval with the replaced block
(internal, left only, right only, both) are exhaustive.  Thus (2.10) is a
literal word substitution, not merely a target-support statement.

### 6.3 Every factor of the span budget

The factor \(Me\) in (3.2) is exact.  Among \(M\)-subsets of
\([M+e]\), the difference between the largest and smallest possible sums
is

\[
 [(e+1)+\cdots+(e+M)]-[1+\cdots+M]=Me.
\]

No factor two is lost.  A common-start lower witness consumes one distinct
right-endpoint slot strictly inside its mandatory witness; this gives
\(h_i\le r_i-\ell_i\), not \(2(r_i-\ell_i)\).  Word reversal supplies a
second necessary inequality but the two inequalities cannot simply be
added, because one inserted position may contribute to both endpoint
skeletons.

### 6.4 Scope of the upper compiler

The separate transition-pair/core upper compiler is valid, with exact
cyclic neighbourhood size

\[
 \sum_j\min(g_j,2H-1)
\]

and cyclic linearization toll at most \(2H-1\).  Its pair letters and cut
cores do not themselves preserve the mandatory middle owners, so its
length is not an excess bound until a baseline substitution is proved.
Theorem 2.2 supplies such a substitution only when the baseline contains
the literal consecutive owner block.

### 6.5 Exact proved and unproved boundary

Proved here:

* the exact global diagonal quotient and truncated-gap count;
* a boundary-compatible Pareto replacement with constants \(2M+1\) and
  exact increase \(M\) in the nonzero local regime;
* the exact cluster criterion (0.5) for \(o(HJ)\) under that replacement;
* the identity-only \(\Omega(HJ)\) standalone obstruction for separated,
  bounded-multiplicity targets;
* the arbitrary-baseline span inequality (0.6), including the exact
  \(\Omega(H)\) opening toll;
* the \(\Omega(H)\)-way compatible-pin necessity under the critical
  separated bounded-multiplicity packet hypotheses; and
* the \(M+2H\) fixed-core word showing that order \(H\) excess is
  sharp on that model even with forced separated cuts and an odd-graph
  lift.

Not proved:

* that the canonical PBBS first-band facet-core word contains literal
  owner blocks to which Theorem 2.2 can be applied;
* that its mandatory endpoints admit the compatible bundles (4.8);
* a common left-and-right chronology realizing those bundles;
* \(o(HJ)\) added length for arbitrary canonical PBBS cut distributions;
  or
* the coefficient-one theorem.

Conditional on first proving (3.7)--(3.8), bounded multiplicity, and an
assignment of the required target values to one near-baseline packet, the
next PBBS statement is narrower than a generic cross-cut seam theorem:

> For each growing canonical PBBS cut packet, recode the already mandatory
> first-band core positions so that a positive fraction of them carry
> strict depth-\(\Theta(H)\) lower flags on both endpoint skeletons, group
> their successive pins into \(\Omega(H)\)-way compatible bundles, and
> order the bundles in one literal word with only \(O(H)\) opening letters
> per growing packet.

If the packet sizes tend to infinity, an \(O(H)\) opening toll is
\(o(HJ)\), exactly as in Theorem 5.1.  Conversely, a canonical-PBBS proof
that every such compatible bundle has size \(o(H)\), uniformly over
admissible witness assignments and pin choices in the sense stated after
(4.8), would contradict (4.8) and rigorously close this conditional
baseline-fusion lane.  Neither the critical hypotheses nor either
alternative follows from the endpoint identity alone.
