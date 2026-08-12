# Physical endpoint fusion for the two-colour product-SCD paths

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or
web input is used.

## 0. Exact outcome

This note addresses physical fusion of the two-colour product-SCD union
paths.  Three different assertions have to be kept separate:

1. the new middle-owner successor is a literal Johnson edge;
2. every crossing window has the correct lower and upper ranks; and
3. the signed target maps remain globally one-hot.

The first two admit an exact local solution.  The third remains a global
column-routing problem.

All assertions are about the alternating **union paths** of the two
product-SCD colours.  The splice preserves middle owners and signed
union-path flags; it is not asserted to preserve either colour matching
separately.

Let \(H\ge2\), and let \(R\ge4H-3\).  For statements about a complete
packet factor, also assume that \(R\) is an admissible compiler dimension
(in the standard construction, \(R\) is a power of two, so
\(2R\mid2^R\)).  Inside a physical
\(Q_{R+1}\), take one \(C_{2R}\) compiler cycle in each of two opposite
facets.  The following are proved.

* Merely changing the opposite-facet resolution of the \(Q_{R+1}\)
  does not fuse anything.  Both resolutions have exactly

  \[
                         {2^R\over R}                         \tag{0.1}
  \]

  standard \(C_{2R}\)-components.

* A physical two-cut splice can merge one cycle in each facet into one
  \(C_{4R}\).  If the two compiler orders have four disjoint
  \(H-1\) fringes, the new cycle is cyclically two-sided \(H\)-safe and
  its lower and upper target maps are injective at every depth
  \(q\le H\).

* At each fixed sign and depth \(q\), this absorber deletes exactly
  \(2q\) old target identities and creates exactly \(2q\) new target
  identities.  The two affected sets are disjoint and

  \[
   \left\|
     \mathbf 1_{\mathcal I_{\rm new,q}^{\pm}}
       -\mathbf 1_{\mathcal I_{\rm old,q}^{\pm}}
   \right\|_1=4q.                                             \tag{0.2}
  \]

  Thus the aggregate two-sign displacement through \(H\) is exactly

  \[
                             4H(H+1).                          \tag{0.3}
  \]

  Nevertheless the number of locally realized targets does not fall.
  If the new columns are routed into columns vacated elsewhere or into
  genuine old holes, the net missing-target loss can be zero.  Hence
  there is no unconditional \(H\)-loss theorem for physical fusion.

* The lower and upper point-margin derivatives of one \(i\to e\)
  absorber are respectively

  \[
                 q(\chi_i-\chi_e),\qquad
                 q(\chi_e-\chi_i),                             \tag{0.4}
  \]

  where \(\chi_j\) is the incidence vector of the two physical
  endpoints of axis \(j\).  An Eulerian circulation of axis replacements
  therefore cancels all point margins, for both signs and every depth,
  exactly.

The positive theorem is deliberately local: it concerns one paired
cycle, containing \(4R\) owners.  It does **not** prove that the cycles
of two complete \(Q_R\)-facet factors can be paired with the required
fringes, nor that crossing columns belonging to different absorbers are
disjoint.  The exact remaining assertion is a simultaneous, all-depth,
two-sign target-column configuration Hall theorem.  Axis balance or a
radius-reset circulation is only its point projection.

There is also a sharp conditional toll.  If an attempted seam has a
shortest directed residence of inclusive span \(\rho\le H\), then the
affected sign has at least

\[
                    \binom{H-\rho+2}{2}                        \tag{0.5}
\]

rank-invalid crossing occurrences.  This is an actual missing-target
lower bound only when those occurrences are frozen distinct one-hot
slots which cannot be reassigned elsewhere.  Without that external
hypothesis it is a chronology-capacity loss, not a global hole-count
loss.  Keeping the components cut instead has the exact standard
full-radius collar price \(2H+1\).  Thus an unsafe seam has the rigorous
fallback/recourse price

\[
       \min\left\{2H+1,\binom{H-\rho+2}{2}\right\}             \tag{0.6}
\]

under frozen-slot, one-token-per-displaced-flag repair accounting, but
(0.6) is not an unconditional hole or word-length lower bound without
that repair convention.

No coefficient-one conclusion is claimed.

## 1. Exact two-sided chronology

Let

\[
                       X_0,X_1,\ldots,X_s
\]

be a directed walk in \(J(n,m)\), written

\[
                       X_{t+1}=X_t-a_t+b_t,                    \tag{1.1}
\]

where \(a_t\in X_t\) and \(b_t\notin X_t\).  Put

\[
                       \sigma_t=\{a_t,b_t\}.                   \tag{1.2}
\]

For a \(q\)-edge window beginning at \(t\), define

\[
 L_q(t)=\bigcap_{j=0}^{q}X_{t+j},\qquad
 U_q(t)=\bigcup_{j=0}^{q}X_{t+j}.                              \tag{1.3}
\]

For \(u<v\), a relation \(b_u=a_v\) is an insertion-removal
residence, and \(a_u=b_v\) is a removal-reinsertion residence.  Its
inclusive span is

\[
                              \rho=v-u+1.                       \tag{1.4}
\]

### Theorem 1.1 (two-sided residence criterion)

For a \(q\)-edge window, the following hold.

1. \(|L_q(t)|=m-q\) if and only if the window contains no relation
   \(b_u=a_v\) with \(u<v\).
2. \(|U_q(t)|=m+q\) if and only if the window contains no relation
   \(a_u=b_v\) with \(u<v\).
3. Both equalities hold if and only if the \(q\) support pairs
   \(\sigma_t,\ldots,\sigma_{t+q-1}\) are pairwise disjoint.

#### Proof

The intersection loses one new member of the initial owner at every
edge precisely when no removal deletes a coordinate inserted earlier in
the window.  This proves the first assertion.  Dually, the union gains
one coordinate initially absent at every edge precisely when no later
insertion restores a coordinate removed earlier in the window.  This
proves the second assertion.

Either directed residence makes two support pairs intersect.  Conversely,
suppose two support pairs intersect.  An opposite-role intersection is
already one of the two displayed residences.  If the same coordinate is
removed twice, legality forces it to be reinserted between the two
removals, producing directed residences.  If it is inserted twice,
legality forces an intervening removal, with the same conclusion.  Thus
absence of both kinds of residence is equivalent to pairwise support
disjointness. \(\square\)

### Corollary 1.2 (exact \(H\)-memory state)

A concatenation of internally two-sided \(H\)-safe paths remains
two-sided \(H\)-safe if and only if, at each newly read transition,
its support pair is disjoint from each of the previous \(H-1\) support
pairs which has not yet expired.  For a cyclic component the same test
must be imposed across the final closure.

Thus the exact evolving state is the ordered suffix

\[
   \mathfrak s_t=(\sigma_{t-H+1},\ldots,\sigma_{t-1}),          \tag{1.5}
\]

with ages retained and expired entries deleted.  A reset colour which
does not change the physical transition does not alter (1.5).

#### Proof

Every window of at most \(H\) edges has pairwise disjoint supports if
and only if each new support passes the stated suffix test.  Apply
Theorem 1.1. \(\square\)

The state is essential when the pieces being fused have fewer than
\(H\) edges.  Pairwise seam compatibility is not transitive.  For
example, the three exchanges

\[
                 (a\to x),\qquad(b\to c),\qquad(x\to d)        \tag{1.6}
\]

may each be legal at the adjacent interface, but the first and third
supports intersect.  The three-edge lower flag has rank \(m-2\), not
\(m-3\).

### Owner and component constraints

For a seam from a tail owner \(X\) to a head owner \(Y\), literal
factorhood requires

\[
                    |X\setminus Y|=|Y\setminus X|=1.           \tag{1.7}
\]

The unique seam support is

\[
                 \sigma(X,Y)=(X\setminus Y)\cup(Y\setminus X).\tag{1.8}
\]

If open paths are fused, every endpoint port has indegree and outdegree
at most one, and the selected seam graph must be a path forest unless a
cyclic output component is explicitly intended.  Each new seam is read
in the history created by all earlier seams.  Consequently a matching in
the unlifted endpoint graph is not sufficient: it must lift to the state
graph whose vertices include (1.5).

## 2. Exact chronology toll and its scope

### Theorem 2.1 (invalid-window count)

Suppose a shortest cross-seam insertion-removal residence has inclusive
span \(\rho\le H\), and both sides have full \(H\)-collars.  For every
\(q\in[\rho,H]\), exactly \(q-\rho+1\) placements of a \(q\)-edge
window contain this fixed offending pair.  Each such window has lower
rank greater than \(m-q\).  Hence this residence forces at least

\[
 \sum_{q=\rho}^{H}(q-\rho+1)
                  ={(H-\rho+1)(H-\rho+2)\over2}                \tag{2.1}
\]

rank-invalid lower occurrences.  The removal-reinsertion statement is
identical for upper flags.

If a physical axis is toggled and then toggled back within the window,
both directed residences occur, so the same count applies to both
signs.

#### Proof

At depth \(q\), the left endpoint of a window containing two fixed
edges at inclusive span \(\rho\) has \(q-\rho+1\) possible positions.
Theorem 1.1 makes every such window invalid for the stated sign.  Sum
over \(q\). \(\square\)

### Proposition 2.2 (safe open-seam census)

Let two open, internally two-sided \(H\)-safe paths have at least
\(H-1\) edges available on each side of a proposed Johnson seam.  If the
seam passes the memory test (1.5), then at signed depth \(q\le H\):

1. every old internal target occurrence is unchanged;
2. exactly \(q\) new windows cross the seam; and
3. all \(q\) crossing windows have the correct signed rank.

If, for both signs and every \(q\le H\), those crossing target columns
are mutually distinct and avoid the old occupied columns, then the fused
open path remains one-hot and its missing-target count cannot increase.

#### Proof

A crossing \(q\)-window is determined by the number
\(0,1,\ldots,q-1\) of its non-seam edges taken on the left, which gives
exactly \(q\) placements.  The memory test and Theorem 1.1 give their
ranks.  No old internal window changes.  The final assertion is precisely
injectivity of the union of the old and crossing target images.
\(\square\)

Thus even at the open-path level there is no local \(H\)-loss law.  The
obstruction is the availability of unoccupied literal columns for all
crossing windows, not their mere existence.

There are three distinct ledgers.

* Equation (2.1) is unconditionally a count of invalid chronological
  occurrences.
* It is a loss of assigned one-hot flags if every such occurrence owns a
  prescribed distinct slot which is unavailable to the rest of the
  construction.
* It is a global missing-target loss only after an external Hall cut
  proves that the displaced targets cannot be supplied elsewhere.

The last implication does not follow from chronology alone.

In the standard full-radius linearization, a path component with \(v\)
useful middle states has length \(v+2H+1\).  Refusing a seam and retaining
one additional component therefore costs exactly \(2H+1\) entries.
Under the frozen-slot hypothesis and the convention that each displaced
assigned flag is repaired by its own literal token, the cheaper of
cutting and locally repairing has cost given by (0.6).  In particular,
\(o(H)\) recourse for an unsafe
seam forces

\[
                       H-\rho=o(\sqrt H),                        \tag{2.2}
\]

unless \(\rho>H\), in which case the seam is exactly safe.

### Product-SCD scale

The number of nonempty central product-SCD diagonal paths is

\[
 p_0=\binom m{\lfloor m/2\rfloor}^{2}
    =\left({2\over\sqrt\pi}+o(1)\right){W\over\sqrt m},
 \qquad W=\binom{2m}{m}.                                      \tag{2.3}
\]

If \(H/\sqrt m\to\infty\), reducing this to \(o(W/H)\) components
requires

\[
 f=p_0-o(W/H)
   =\left({2\over\sqrt\pi}+o(1)\right){W\over\sqrt m}          \tag{2.4}
\]

net component fusions.  Paying the full-radius cut fallback at all of
them costs

\[
 (2H+1)f
   =\left({4\over\sqrt\pi}+o(1)\right)
      {H\over\sqrt m}\,W
   =\omega(W).                                                  \tag{2.5}
\]

Thus almost all needed fusions must be physically safe and column-useful;
one cannot pay an independent \(H\)-scale fallback at every seam.

For a high-high fusion of two short product-SCD diagonals, overlap of
the relevant active alphabet gives a directed residence of span at most

\[
                             h(P)+h(Q)+1.                        \tag{2.6}
\]

Consequently, when \(h(P)+h(Q)=o(H)\), such an overlap produces
\(H-o(H)\) bad depths and \(\tfrac12H^2-o(H^2)\) bad occurrences for
the affected sign.  A viable short-path seam must therefore eliminate
both directed overlaps, not merely balance their number.

## 3. Why a complete slab re-resolution is not fusion

Let a physical \(Q_{R+1}\) have axes \(D\cup\{e\}\), with
\(|D|=R\).  Resolving it into the two opposite \(e\)-facets gives two
\(Q_R\)'s.  Resolving it instead into the two opposite \(i\)-facets,
where \(i\in D\), gives another two \(Q_R\)'s on exactly the same owner
union.  In this section assume that the standard \(C_{2R}\)-factor
exists on \(Q_R\).

### Proposition 3.1 (component neutrality)

After installing the standard isometric \(C_{2R}\)-compiler in every
facet, either resolution has exactly

\[
        2\,{2^R\over2R}={2^R\over R}                            \tag{3.1}
\]

components.  Therefore the owner-preserving cross-parent slab trade
changes packet membership and target columns but does not reduce the
component count.

#### Proof

Each \(Q_R\) factor has \(2^R/(2R)\) cycles.  There are two facets in
either resolution. \(\square\)

The same conclusion applies to a radius-reset label which merely chooses
a different abstract channel while leaving each physical successor
unchanged.  Component fusion requires a new physical edge operation.

## 4. A diverse-order physical \(2\)-opt absorber

We now give such an operation.  Regard each active axis as a disjoint
physical pair.  An owner of the orientation cube chooses one endpoint of
each pair.

Fix a cut axis \(i\in D\) and a fresh slab axis \(e\notin D\).  Since

\[
                        R-1\ge4(H-1),                            \tag{4.1}
\]

choose pairwise disjoint ordered blocks

\[
 A_0,A_1,B_0,B_1\subseteq D\setminus\{i\},
 \qquad |A_j|=|B_j|=H-1.                                      \tag{4.2}
\]

Complete them to permutations

\[
                       \pi_j=(i,A_j,\kappa_j,B_j),
                       \qquad j=0,1.                            \tag{4.3}
\]

In the two opposite \(e\)-facets take translated isometric cycles with
direction necklaces \(\pi_0\pi_0\) and \(\pi_1\pi_1\).  Base them so
that their first \(i\)-edges project to the same \(i\)-edge of \(Q_D\).
Write those parallel edges as

\[
                    A_0'-B_0',\qquad A_1'-B_1',                 \tag{4.4}
\]

where corresponding primed endpoints have equal \(i\)-orientation.
Delete (4.4), and add the two \(e\)-edges joining equal
\(i\)-orientations.

If \(u_j\) is the residual \(2R-1\) direction word obtained after
deleting the first \(i\) in \(\pi_j\pi_j\), the new direction necklace
is

\[
                         u_0,e,\operatorname{rev}(u_1),e.       \tag{4.5}
\]

### Theorem 4.1 (paired-cycle absorber)

The operation above has all of the following properties.

1. It is a literal owner-preserving \(2\)-opt in \(Q_{R+1}\).
2. It merges the two old \(C_{2R}\)'s into one simple \(C_{4R}\).
3. The new cycle is cyclically two-sided \(H\)-safe.
4. For every \(q\le H\), both signed target maps on the \(4R\) starts
   of the new cycle are injective.

#### Proof: factorhood and component count

The deleted edges are parallel \(i\)-edges in opposite \(e\)-facets.
Joining corresponding endpoints changes only the \(e\)-orientation, so
both new edges are literal cube edges and hence literal Johnson edges.
A two-cut cross-join of two distinct cycles produces one cycle on their
disjoint vertex union.  This proves the first two assertions.

#### Proof: cyclic \(H\)-safety

Every subword internal to \(u_j\) is safe: in
\(\pi_j\pi_j\), two occurrences of the same direction are exactly
\(R\) positions apart, and \(H<R\).

At one \(e\)-seam, the two length-\((H-1)\) fringes are \(B_0\) and
\(B_1\); at the other they are \(A_1\) and \(A_0\).  By (4.2), a
crossing word of length \(q\le H\) consists of \(e\) and disjoint
suffix/prefix pieces of total length \(q-1\).  All its directions are
distinct.  The two occurrences of \(e\) in (4.5) are \(2R\) positions
apart.  Theorem 1.1 proves the third assertion.

#### Proof: local one-hotness

For a window whose touched-axis set is \(J\), either signed target
recovers the following face descriptor:

\[
              \bigl(J,\hbox{chosen endpoint on every axis outside }J\bigr).
                                                                    \tag{4.6}
\]

Indeed, a lower target contains neither endpoint of a touched pair and
one endpoint of every untouched pair; an upper target contains both
endpoints of a touched pair and one endpoint of every untouched pair.

Windows internal to the two residual old paths are injective, and their
untouched \(e\)-orientations distinguish the two facets.  A new crossing
target has \(e\in J\), so it cannot equal any internal target.

At the \(B\)-seam, a crossing support is

\[
 \{e\}\cup\operatorname{Suf}_{\ell}(B_0\text{-fringe})
       \cup\operatorname{Suf}_{q-1-\ell}(B_1\text{-fringe})    \tag{4.7}
\]

for a unique split \(0\le\ell\le q-1\).  Disjointness of the fringe
blocks recovers \(\ell\).  The \(A\)-seam is identical.  Supports at
the two seams are different for \(q\ge2\), while for \(q=1\) the two
targets are distinguished by their opposite untouched \(i\)-orientations.
Thus all crossing starts, and hence all \(4R\) starts, have different
descriptors.  This proves the fourth assertion. \(\square\)

Theorem 4.1 is a theorem about one pair of compiler cycles.  It does not
assert cross-cycle injectivity for a factor of the whole slab.

## 5. Exact target-column ledger

Fix a sign and \(q\le H\).  A directed \(q\)-window of an old cycle is
affected precisely when it contains its deleted \(i\)-edge.  There are
\(q\) such starts per deleted edge and hence \(2q\) in total.  Similarly,
there are \(2q\) new starts whose windows contain one of the two new
\(e\)-edges.  The two collars are disjoint because \(q<R\).

### Theorem 5.1 (exact column displacement)

For either sign,

\[
 \begin{aligned}
 |\mathcal I_{\rm old,q}^{\pm}|
   &=|\mathcal I_{\rm new,q}^{\pm}|=4R,\\
 |\mathcal I_{\rm old,q}^{\pm}
       \cap\mathcal I_{\rm new,q}^{\pm}|
   &=4R-2q,\\
 |\mathcal I_{\rm old,q}^{\pm}
       \setminus\mathcal I_{\rm new,q}^{\pm}|
   &=|\mathcal I_{\rm new,q}^{\pm}
       \setminus\mathcal I_{\rm old,q}^{\pm}|=2q.
                                                               \tag{5.1}
 \end{aligned}
\]

Consequently (0.2) and (0.3) hold.

#### Proof

Every unaffected window traverses exactly the same vertex set, possibly
in reverse order, so its intersection and union are unchanged.  The old
affected targets have \(i\) touched and \(e\) untouched.  The new
affected targets have \(e\) touched and \(i\) untouched: the remaining
\(i\)-occurrence is at distance at least \(R>H\) from either seam.
Descriptor (4.6) therefore makes the old and new affected images
disjoint.  Theorem 4.1 makes each image internally one-hot.  This proves
(5.1).  Summing \(4q\) over \(q\le H\) and over two signs gives (0.3).
\(\square\)

Let \(B_q^{\pm}(T)\) be the load from all starts outside this absorber.
The exact hole-count derivative is

\[
 \mathcal H_q^{\pm}(B+\Gamma_{\rm new})
  -\mathcal H_q^{\pm}(B+\Gamma_{\rm old})
 =\sum_{T:B_q^{\pm}(T)=0}
   \bigl(\Gamma_{\rm old,q}^{\pm}(T)
        -\Gamma_{\rm new,q}^{\pm}(T)\bigr).                   \tag{5.2}
\]

Its absolute value is at most \(2q\), but it may be any value allowed by
the background, including zero.  Equation (5.2) is why (0.3) is not a
missing-target lower bound.

If the old complete atlas is one-hot, and every new column is disjoint
from the unchanged occupied columns and from every other new column,
then the new atlas is also one-hot.  Since the old and new occurrence
masses agree, its hole count is exactly unchanged.  Target identities
have moved, but missing-target loss is zero.

## 6. Why synchronized fusion fails

The different orders in (4.3) are load-bearing.  Suppose instead that
\(\pi_0=\pi_1\).  Each of the two seams in (4.5) then has a local
direction pattern

\[
                              d,e,d.                             \tag{6.1}
\]

### Proposition 6.1 (synchronized quadratic toll)

At every depth \(q\ge3\), exactly \(2(q-2)\) crossing windows are
rank-invalid, for each sign.  The remaining valid seam flags collide in
pairs.  Therefore the signed support falls by exactly

\[
                              2(q-1)                             \tag{6.2}
\]

at depth \(q\), and the cumulative loss for one sign through \(H\) is

\[
                              H(H-1).                            \tag{6.3}
\]

Across both signs the loss is \(2H(H-1)\).

#### Proof

A \(q\)-window contains both copies of \(d\) in one motif in exactly
\(q-2\) positions.  There are two motifs, and Theorem 1.1 makes these
windows invalid.  Among the two boundary placements which contain \(e\)
but not both copies of \(d\), the two facets have the same touched-axis
set and the same untouched orientation descriptor, producing one repeat
at each seam.  Thus each seam loses \(q-2\) invalid occurrences and one
additional support unit, which gives (6.2).  Summation gives (6.3).
\(\square\)

For synchronized orders the \(2H+1\) cut fallback is asymptotically
cheaper than the quadratic certificate loss.  A common phase or common
order is therefore not a fusion mechanism.

## 7. Exact point margins and reset circulation

Let \(\chi_j\) denote the incidence vector of the two ground
coordinates forming physical axis \(j\).

### Theorem 7.1 (point derivative)

For the \(i\to e\) absorber and either depth \(q\le H\), the new-minus-old
lower point-incidence vector is

\[
                              q(\chi_i-\chi_e),                  \tag{7.1}
\]

and the upper derivative is

\[
                              q(\chi_e-\chi_i).                  \tag{7.2}
\]

#### Proof

In the \(2q\) old affected lower targets, axis \(i\) is touched and
contributes neither endpoint, whereas the two \(e\)-facets together
contribute each \(e\)-endpoint exactly \(q\) times.  In the new targets,
\(e\) is touched and the two \(i\)-orientations each occur \(q\) times.
This gives (7.1).  For upper targets a touched axis contributes both
endpoints.  Subtracting gives (7.2). \(\square\)

### Corollary 7.2 (Eulerian cancellation)

For a multiset of absorbers \(i_s\to e_s\), if

\[
             \sum_s(\chi_{e_s}-\chi_{i_s})=0,                  \tag{7.3}
\]

then their aggregate lower and upper point-margin derivatives vanish
exactly, simultaneously for every \(q\le H\).  In particular, an
Eulerian circulation on the physical-axis replacement graph satisfies
(7.3).

This is not a literal column theorem.  Distinct target families can have
identical point margins.

## 8. Conditional multiway fusion theorem

The preceding local absorber isolates the exact global hypothesis.
Start from a globally one-hot signed atlas and a forest \(F\) on its old
cycle components.  For every forest edge \(s\in E(F)=\mathcal S\),
choose one cut edge in each incident component.  A component may be
incident with several forest edges, but all chosen cyclic
\(H\)-collars on that component must be pairwise disjoint.  The
cross-joins must also be chosen so that the resulting new seam collars
are pairwise disjoint.  Here disjoint means that no directed
\(q\)-window, for any \(q\le H\), meets two selected cut or seam edges.
For
\(c=(\pm,q)\), let

\[
 A_{s,c}=\hbox{the (2q) old affected columns},\qquad
 N_{s,c}=\hbox{the (2q) proposed new crossing columns}.       \tag{8.1}
\]

Let \(O_c\) be the set of columns retained by all unchanged starts after
all \(A_{s,c}\) are removed.

### Theorem 8.1 (sharp sufficient splice theorem)

Suppose the same absorber choice at every depth and sign satisfies:

1. **owners:** for each \(s\), its two cut edges are parallel physical
   \(i_s\)-edges in opposite \(e_s\)-facets; different selected cut
   edges are distinct, and both the old cut collars and the resulting new
   seam collars are disjoint in the sense above;
2. **chronology:** every paired cut passes the two-fringe condition of
   Theorem 4.1, and the complete multi-seam word passes the evolving
   state test (1.5), including cyclic closure;
3. **columns:** for every \(c=(\pm,q)\), each local crossing image has
   \(|N_{s,c}|=2q\), the sets \(N_{s,c}\) are pairwise disjoint, and

   \[
                              N_{s,c}\cap O_c=\varnothing;      \tag{8.2}
   \]

4. **component graph:** the selected pairs are the edges of the forest
   \(F\), and the cross-joins are oriented so that they can be applied in
   a leaf order, each time between two distinct current components.

Then all splices together produce a literal exact middle-owner factor,
are two-sided \(H\)-safe, and preserve global one-hotness at every
signed depth \(q\le H\).  The component count falls by exactly
\(|\mathcal S|\), and the global number of missing targets at every
signed depth is unchanged.  If the original factor has \(G\) owners and
\(p_0\) components, the standard full-radius linearization of the result
is a literal contiguous-OR word of length

\[
                 G+(2H+1)(p_0-|\mathcal S|).                   \tag{8.3}
\]

#### Proof

Condition 1 preserves every owner exactly once.  Applying the forest
edges in leaf order, every \(2\)-opt joins two distinct current
components and therefore reduces the component count by one; no selected
cut edge is used twice.  Disjoint \(H\)-collars ensure that a later
splice does not alter an already checked local fringe.  Condition 2 and
Theorem 1.1 prove two-sided
\(H\)-safety.  The unchanged columns are one-hot by hypothesis.
Condition 3 makes every new crossing column distinct from those columns
and from every other crossing column, so the new atlas is one-hot.

At fixed \(c\), disjoint collars imply that the operation removes
\(2q|\mathcal S|\) columns and
adds the same number of distinct columns outside \(O_c\).  Hence occupied
support, and therefore the number of holes, is unchanged.  The final
formula is the exact full-radius component collar applied to the new
component count. \(\square\)

Condition (8.2) permits a new column of one absorber to occupy a column
vacated by another absorber.  It also permits use of a pre-existing
boundary hole.  This is the exact mechanism by which the raw
\(\Theta(H^2)\) displacement of each absorber could have zero hole cost.

The unproved statement is the following.

> **Unproved target-column configuration Hall gate.**  In a common exact
> packet tiling of the product-SCD owner set, find a positive-density
> growing forest of parallel cycle cuts and select one diverse-order
> absorber option for each forest edge so that all old and new collars
> are disjoint and (8.2) holds simultaneously for both signs and every
> \(q\le H\), while the forest coalesces the old cycles into only
> \(o(W/H)\) final components.

This is not a separate matching at each depth.  One physical absorber
option determines all \(2H\) column sets \(N_{s,c}\) at once.  The gate
is therefore a configuration matching or set-packing theorem with
coupled columns.

## 9. Radius resets: what they solve and what they do not

The cross-parent \(Q_{R+1}\) trade and the growing status-orbit reset
atlas provide abundant physical candidate axes and can satisfy an
Eulerian law such as (7.3).  They therefore solve the following
projections of the fusion problem:

* owner preservation inside each traded slab;
* literal Johnson adjacency of every proposed \(2\)-opt edge;
* two-sided local \(H\)-safety when the diverse fringes are installed;
* linear parent-status pair breaking; and
* exact all-depth point-margin cancellation under (7.3).

They do not by themselves solve:

* pairing all compiler cycles by parallel cut edges;
* installing the required four disjoint fringes in one common exact
  factorization;
* disjointness of crossing descriptors belonging to different cycle
  pairs; or
* avoidance of the globally occupied target columns \(O_c\).

A fixed-level reset colour which leaves the physical successor unchanged
cannot reduce components at all.  A growing physical \(2\)-opt is
necessary.  Conversely, even a dense family of physical \(2\)-opts with
perfect axis-Euler balance can have linear or worse literal collision
excess, because (7.3) is only the point projection of (8.2).

For \(g\) selected absorbers, the raw, per-absorber signed-column motion
is exactly

\[
                            4gH(H+1).                            \tag{9.1}
\]

before cross-absorber cancellation.  Achieving aggregate missing-target
loss \(o(H)\) per fusion requires routing all but \(o(gH)\) of the
potentially lost support units, out of \(2gH(H+1)\) old affected signed
columns.  Thus the unmatched fraction must be \(o(1/H)\).  Point-margin
balance alone is far too coarse to certify this.

## 10. Independent audit and exact boundary

The chronology calculation and the slab calculation were audited
independently.

The chronology audit confirmed:

* pairwise support disjointness, rather than either one-sided residence
  condition alone, is the exact two-sign invariant;
* histories of short intermediate paths compose, so a static endpoint
  matching is insufficient;
* the product-SCD overlap span in (2.6) is \(h(P)+h(Q)+1\); and
* invalid occurrence, assigned target, and global hole loss must not be
  identified without an external Hall cut.

The slab audit confirmed:

* the threshold \(R\ge4H-3\);
* the two seam fringe criterion;
* local two-sign injectivity of the fused \(C_{4R}\);
* the exact constants \(2q,4q,4H(H+1)\); and
* the point derivatives (7.1)--(7.2).

It also confirmed the decisive scope limitation: Theorem 4.1 is only a
single paired-cycle theorem.  Cross-gadget injectivity does not follow
from the existing diverse-order compiler theorem.

### Proved

* the exact two-sided chronology and owner constraints;
* the triangular short-residence occurrence toll;
* the exact \(2H+1\) cut recourse and its product-SCD global consequence;
* component neutrality of a full \(Q_{R+1}\) re-resolution;
* an explicit safe, locally one-hot, physical two-cycle absorber for
  \(R\ge4H-3\);
* its exact all-depth target displacement and point derivatives;
* exact point cancellation for an Eulerian reset circulation; and
* the necessary-and-sufficient column condition in the multiway
  sufficient theorem.

### Not proved

* a positive-density common exact tiling by compatible paired cycles;
* preservation of either product-SCD colour as a separate matching;
* the coupled target-column configuration Hall gate;
* \(o(H)\) missing-target loss per fusion for the product-SCD family;
* \(o(W/H)\) final components together with \(o(W)\) total literal
  target error; or
* coefficient one.

The lane therefore ends at a genuine positive local theorem, not an
unconditional no-go.  Diverse physical endpoint fusion is possible and
can have zero local support loss.  The sole surviving obstruction is
global literal column routing in the same evolving \(H\)-memory state;
neither slab re-resolution nor radius-reset point balance proves it.
