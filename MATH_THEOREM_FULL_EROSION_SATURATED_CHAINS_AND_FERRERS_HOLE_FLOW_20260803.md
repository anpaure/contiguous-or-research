# Full erosion gives saturated chains; every other factor is a Ferrers-hole flow

**Date:** 2026-08-03  
**Status:** unconditional theorem for every fixed resident complete cyclic
Johnson carrier.  It gives the exact full-erosion deck, an exact normal form for all
literal factors on that carrier, an integral one-coordinate path-flow model,
and a positive-density obstruction to using the full factor itself.  No
computation is used.  It does **not** construct a carrier with the required
named-target deck.

## 0. Outcome

Let \(1\le d<r<k\), put \(W={k\choose r}\), and let

\[
 T_0,T_1,\ldots,T_{W-1}\in {[k]\choose r},\qquad
 T_{i+1}=T_i-\{\alpha_i\}+\{\beta_i\},
 \tag{0.1}
\]

be a **complete** cyclic Johnson carrier (the (T_i)'s are all distinct),
and suppose every positive coordinate run has length at least (d+1).
Put

\[
 E_j=\bigcap_{i=j-d}^{j}T_i,
 \qquad
 C^*_{j,q}=\bigcup_{h=j}^{j+q-1}E_h
 \quad(1\le q\le d).
 \tag{0.2}
\]

Then

\[
 \boxed{
 C^*_{j,q}
 =\bigcap_{i=j+q-1-d}^{j}T_i
 =T_j\setminus
   \{\beta_{j+q-1-d},\ldots,\beta_{j-1}\}.}
 \tag{0.3}
\]

In particular,

\[
 |C^*_{j,q}|=s_q:=r-d+q-1,                         \tag{0.4}
\]

and, for every fixed \(j\),

\[
 C^*_{j,1}\subsetneq C^*_{j,2}\subsetneq\cdots
 \subsetneq C^*_{j,d}                               \tag{0.5}
\]

is a saturated Boolean chain through the ranks
\(r-d,r-d+1,\ldots,r-1\).  For fixed \(q\), the row is a cyclic
rank-\(s_q\) Johnson walk:

\[
 \boxed{
 C^*_{j+1,q}
 =C^*_{j,q}-\{\alpha_j\}
             +\{\beta_{j+q-1-d}\}.}
 \tag{0.6}
\]

Thus the fixed full factor has an especially simple target allocator.  A
target is adjacent only to cells whose **value equals that target**.  The
matching graph is a disjoint union of stars, and all rank-\(s_q\) targets
are allocable in row \(q\) exactly when the walk in (0.6) is surjective onto
\({[k]\choose s_q}\).  There is no nontrivial Hall cut on this fixed face.

This positive laminarity is nevertheless far from a lower compiler.  Even
after granting all \({d+1\choose2}\) linear boundary cells arbitrary
values, the full factor has defect at least

\[
 \boxed{
 \left[\sum_{s=1}^{r-d-1}{k\choose s}-{d+1\choose2}\right]_+.}
 \tag{0.7}
\]

At the central rank, using
\(d/\sqrt{k}\longrightarrow\sqrt{\pi/8}\), the omitted proportion of the
strict lower ideal tends to

\[
 \boxed{
 2\Phi\!\left(-\sqrt{\pi/2}\right)=0.210\ldots .}
 \tag{0.8}
\]

So the fully dense maximal factor itself has positive-density lower defect.
Together with the sparse-rail barrier, this shows that a successful factor
must tune its deletion gaps; neither a bounded number of sparse rails nor
the zero-deletion extreme can work.

There is an exact normal form for those deletions.  Every literal factor on
the fixed carrier is obtained from the full erosion supports by choosing,
inside each erosion run, disjoint internal **hole blocks** of lengths at
most \(d\), with a retained occurrence between consecutive blocks.  A hole
block \(B\) of length \(\ell\) removes its coordinate from precisely the
Ferrers triangle

\[
 \mathcal F(B)={(j,q):I_{j,q}\subseteq B, 1\le q\le\ell\},
 \qquad I_{j,q}=[j,j+q-1].                           \tag{0.9}
\]

It removes \((\ell-q+1)_+\) incidences from row \(q\).  If \(N_\ell\) is the
total number of length-\(\ell\) hole blocks and

\[
 H_q=\sum_j\left|\bigcup_{h=j}^{j+q-1}A_h\right|,
 \qquad
 \Delta_q=s_qW-H_q,                                 \tag{0.10}
\]

then

\[
 \boxed{
 \Delta_q=\sum_{\ell=q}^{d}(\ell-q+1)N_\ell,
 \qquad
 N_q=\Delta_q-2\Delta_{q+1}+\Delta_{q+2},}
 \tag{0.11}
\]

where \(\Delta_{d+1}=\Delta_{d+2}=0\).  Hence the aggregate deficit
sequence is nonnegative, decreasing, and discretely convex.  Conversely,
these conditions, integrality, and one explicit run-packing condition are
sufficient.  This is the exact dense analogue of the gap-energy identity.

Finally, after arbitrary additive prices are placed on coordinate--cell
absences, optimizing the occurrence schedule for one coordinate is an
integral longest-path problem: retained erosion occurrences are path
vertices and an arc of length \(g\le d+1\) creates one hole of length
\(g-1\).  Thus the schedule-only dense face is a product of network-flow
polytopes.  Named-target assignment couples the coordinates at each cell
and destroys this product structure; in general it is not one matching,
laminar matroid, or network flow.  The known local odd cover cycle survives
on this face.  The precise positive reduction is therefore:

\[
 \boxed{
 \text{integral path flow per coordinate}
 \quad+\quad
 \text{one global named-signature coupling}.}
 \tag{0.12}
\]

## 1. The full-erosion chain formula

All indices below are cyclic.  Fix \(j,q\), and put

\[
 a=j+q-1-d.                                          \tag{1.1}
\]

The interval of owners in (0.3) contains \(d-q+2\) owners and
\(d-q+1\) Johnson transitions.

### Lemma 1.1 (last-arrival formula)

One has

\[
 \bigcap_{i=a}^{j}T_i
 =T_j\setminus\{\beta_a,\ldots,\beta_{j-1}\}.       \tag{1.2}
\]

The displayed arrival labels are distinct.

### Proof

If \(x\in T_j\) but is absent from one owner in \([a,j]\), its last
arrival before \(T_j\) occurs at some transition in \([a,j-1]\).  Thus
\(x\) is one of the displayed \(\beta\)'s.  Conversely, \(\beta_i\) is
absent from \(T_i\), so it cannot belong to the intersection.

Two equal arrival labels within the displayed transition interval would
enclose a positive run of length at most \(d\), contrary to the residence
floor \(d+1\).  Hence all \(d-q+1\) labels are distinct. \(\square\)

The interval-intersection identity

\[
 \bigcup_{h=j}^{j+q-1}E_h
 =\bigcap_{i=j+q-1-d}^{j}T_i                         \tag{1.3}
\]

is the exact maximal-aperture identity.  Here is the union step explicitly.
Lemma 1.1 at \(q=1\) gives

\[
 E_h=T_h\setminus\{\beta_{h-d},\ldots,\beta_{h-1}\}.             \tag{1.3a}
\]

Sliding the owner-intersection window by one position gives

\[
 E_{h+1}=E_h-\{\alpha_h\}+\{\beta_{h-d}\}.                      \tag{1.3b}
\]

Indeed, residence prevents either displayed coordinate from disappearing
or reappearing elsewhere inside the window of at most \(d+1\) owners.
Consequently the only new elements encountered in
\(E_j,E_{j+1},\ldots,E_{j+q-1}\) are
\(\beta_{j-d},\ldots,\beta_{j+q-2-d}\).  Adding these to (1.3a)
cancels the first \(q-1\) entries of its deletion list and yields

\[
 \bigcup_{h=j}^{j+q-1}E_h
 =T_j\setminus
   \{\beta_{j+q-1-d},\ldots,\beta_{j-1}\}.
 \tag{1.3c}
\]

Lemma 1.1 identifies (1.3c) with the right side of (1.3), proving
(0.3)--(0.4).
Increasing \(q\) by one deletes the first label from the deletion list, so

\[
 C^*_{j,q+1}
 =C^*_{j,q}\cup\{\beta_{j+q-1-d}\}.                \tag{1.4}
\]

This proves the saturated chain (0.5).

### Lemma 1.2 (row recurrence)

Equation (0.6) holds, and the deleted and inserted coordinates are
distinct.

### Proof

Passing from the owner interval \([a,j]\) to \([a+1,j+1]\) removes the
only obstruction to the newly arrived coordinate \(\beta_a\), and adds
the owner in which \(\alpha_j\) has just departed.  Every other coordinate
has the same all-owner status.  Thus the set change is exactly (0.6).

If \(\alpha_j=\beta_a\), that coordinate's positive run from its arrival
at transition \(a\) to its departure at transition \(j\) would contain
\(j-a=d-q+1\le d\) owners.  Residence excludes this. \(\square\)

The full intersection in (1.3) cannot in general be replaced by the
intersection of its two endpoint owners.  Positive residence places no
lower bound on a negative gap: a coordinate may lie in two long positive
runs separated by a short absence inside \([a,j]\).  The endpoint
intersection then contains it while (1.3) does not.  Thus (1.2), not an
endpoint-only formula, is the exact simplification available under the
stated hypotheses.

## 2. Exact allocation on the fixed full schedule

Let

\[
 \mathcal I_q={C^*_{j,q}:j\in\mathbb Z_W\}.         \tag{2.1}
\]

Because different rows have different ranks, their image families are
disjoint.

### Theorem 2.1 (full-deck multiplicity criterion)

For the fixed factor \(A_j=E_j\), a family \(\mathcal L\) of named lower
targets can be assigned to distinct cyclic cells if and only if every
target \(S\in\mathcal L\) occurs as at least one value \(C^*_{j,q}\).
In particular, every target in the band \(r-d\le |S|<r\) is assignable if
and only if

\[
 \mathcal I_q={[k]\choose s_q}
 \qquad(1\le q\le d).                               \tag{2.2}
\]

### Proof

A fixed source factor gives every physical cell one value.  The
target--cell graph therefore has an edge precisely when the target equals
that value.  Its connected components are stars, one for each distinct
value.  Since named Boolean targets occur once on the target shore, a
target is matchable exactly when its star is nonempty.  Rank separation
then gives (2.2). \(\square\)

Consequently, after granting \(B_\partial={d+1\choose2}\) boundary cells
arbitrary values, the full-factor defect obeys the sharper exact bound

\[
 \delta_{\rm full}\ge
 \left[
 \Lambda-\sum_{q=1}^{d}|\mathcal I_q|-B_\partial
 \right]_+.                                         \tag{2.3}
\]

Since no cyclic full-factor cell has rank below \(r-d\), (0.7) follows.

### Theorem 2.2 (central asymptotic obstruction)

At \(r=\lceil k/2\rceil\), the right side of (0.7), divided by
\(\Lambda\), tends to (0.8).

### Proof

Let \(X_k\sim\operatorname{Bin}(k,1/2)\).  The strict lower ideal has

\[
 {\Lambda\over2^k}=\Pr(1\le X_k<r)\longrightarrow {1\over2}.       \tag{2.4}
\]

Also

\[
 {r-d-1-k/2\over\sqrt{k}/2}
 \longrightarrow-\sqrt{\pi/2}.                     \tag{2.5}
\]

The central limit theorem gives

\[
 {1\over2^k}\sum_{s=1}^{r-d-1}{k\choose s}
 \longrightarrow\Phi(-\sqrt{\pi/2}).               \tag{2.6}
\]

The boundary allowance is polynomial and hence negligible compared with
\(\Lambda\).  Dividing (2.6) by (2.4) proves (0.8). \(\square\)

## 3. Every factor is full erosion minus Ferrers holes

Let \(A=(A_h)\) be any depth-\(d\) factor of the fixed carrier and define

\[
 Z_x=\{h:x\in A_h\},\qquad R_x=\{h:x\in E_h\}.      \tag{3.1}
\]

Every positive owner run of \(x\) gives one erosion interval
\(R=[u,v]\subseteq R_x\).

### Theorem 3.1 (exact hole normal form)

The following data are equivalent.

1. A depth-\(d\) factor \(A\) of the fixed carrier.
2. For every erosion interval \(R=[u,v]\), a retained set
   \(Z_x\cap R\) which contains \(u,v\) and whose consecutive retained
   positions have gaps at most \(d+1\).
3. For every erosion interval, a family of pairwise disjoint internal hole
   blocks, each of length at most \(d\), with at least one retained point
   between consecutive blocks.

The correspondence is \(A_h=\{x:h\in Z_x\}\).

### Proof

Every source letter lies in every owner whose window contains it, so
\(A_h\subseteq E_h\).  The compulsory arrival and departure footprint
forces both endpoints of every erosion interval into \(Z_x\).  An owner
containing \(x\) is supplied exactly when its supplier interval meets
\(Z_x\); on an erosion run this is equivalent to the absence of a hole of
length \(d+1\).  This proves that 1 implies 2 and that 2 and 3 are the same
data.

Conversely, define \(A_h\) from data 2.  It is contained in \(E_h\), and
the gap bound makes every owner supplier interval meet \(Z_x\).  Thus all
owners are recovered exactly.  The departure coordinate \(\alpha_h\) is
the retained right endpoint of one erosion interval at position \(h\), so
every \(A_h\) is nonempty. \(\square\)

For such a factor put

\[
 C_{j,q}(A)=\bigcup_{h=j}^{j+q-1}A_h.               \tag{3.2}
\]

### Theorem 3.2 (Ferrers deletion formula)

For every cell,

\[
 \boxed{
 C_{j,q}(A)=C^*_{j,q}\setminus
 \{x:I_{j,q}\subseteq B
       \text{ for some hole block }B\text{ of }x\}.}
 \tag{3.3}
\]

A length-\(\ell\) hole block deletes its coordinate from exactly
\((\ell-q+1)_+\) row-\(q\) cells and from
\({\ell+1\choose2}\) cells over all short rows.

### Proof

A coordinate belongs to \(C^*_{j,q}\) exactly when
\(I_{j,q}\cap R_x\ne\varnothing\), and it belongs to \(C_{j,q}(A)\)
exactly when \(I_{j,q}\cap Z_x\ne\varnothing\).  A cell of length at most
\(d\) meets at most one erosion interval.  If it crosses an endpoint of
that interval, it contains a retained endpoint.  Hence it can meet
\(R_x\) but miss \(Z_x\) exactly when the whole cell interval lies inside
one hole block.  This proves (3.3).

A length-\(q\) interval lies inside a fixed length-\(\ell\) block in
\(\ell-q+1\) positions when \(q\le\ell\), and in none otherwise.  Summing
over \(q\) gives \({\ell+1\choose2}\). \(\square\)

## 4. Aggregate Ferrers inversion and its placement caveat

Let \(N_\ell\) count all length-\(\ell\) hole blocks, with coordinate and
erosion-run multiplicity.  Summing Theorem 3.2 proves the first identity in
(0.11).  Taking two successive differences proves the second.

### Theorem 4.1 (exact aggregate row-total cone)

A proposed integral vector of row-total cardinalities
\((H_1,\ldots,H_d)\) is realized by some factor of the fixed carrier if and
only if the following hold.  It records
\(H_q=\sum_j|C_{j,q}(A)|\); it is not the histogram of individual cell
ranks and carries no named-target assignment data.

1. With \(\Delta_q=s_qW-H_q\) and
   \(\Delta_{d+1}=\Delta_{d+2}=0\), all numbers

   \[
   N_q=\Delta_q-2\Delta_{q+1}+\Delta_{q+2}           \tag{4.1}
   \]

   are nonnegative integers.
2. The resulting hole blocks can be distributed among the erosion runs.
   Explicitly, if an erosion run \(R\) has \(n_R\) positions, there are
   nonnegative integers \(n_{R,\ell}\) such that

   \[
   \sum_Rn_{R,\ell}=N_\ell,
   \qquad
   \sum_{\ell=1}^{d}(\ell+1)n_{R,\ell}\le n_R-1
   \quad(R).                                         \tag{4.2}
   \]

Condition 1 says equivalently that \(\Delta\) is a nonnegative,
nonincreasing, discretely convex integer sequence with the displayed zero
boundary.  Condition 2 is genuine literal placement data and cannot be
discarded from a fixed-carrier theorem.

### Proof

Necessity of 1 is (0.11).  If a run contains \(t\) hole blocks of total
length \(L\), it needs the two retained endpoints and at least \(t-1\)
retained separators.  Thus \(L+t\le n_R-1\), which is exactly (4.2).

Conversely, (4.2) lets us place the prescribed blocks from left to right,
with one retained position between consecutive blocks and retained run
endpoints; unused positions are also retained.  Theorem 3.1 produces a
factor.  The inversion formula then gives exactly the proposed row totals.
\(\square\)

The total rank loss is

\[
 \sum_{q=1}^{d}\Delta_q
 =\sum_{\ell=1}^{d}{\ell+1\choose2}N_\ell.          \tag{4.3}
\]

This is the Ferrers form of the convex gap energy: a marker gap
\(g=\ell+1\) costs \({g\choose2}\).

Aggregate feasibility says nothing about which named targets occur.  It is
therefore a necessary and sufficient theorem only for row-rank totals, not
for the coloured lower compiler.

## 5. The exact integral path-flow face

Fix one erosion interval \(R=[u,v]\) and arbitrary weights
\(w_{j,q}\) for deleting its coordinate from cell \((j,q)\).  Give a hole
block \(B=[a+1,b-1]\), where \(a,b\) are consecutive retained positions,
the weight

\[
 \omega(a,b)=
 \sum_{q=1}^{b-a-1}\ 
 \sum_{j=a+1}^{b-q}w_{j,q}.                          \tag{5.1}
\]

Make the acyclic graph on the positions of \(R\), with an arc
\(a\to b\) whenever

\[
                         1\le b-a\le d+1.            \tag{5.2}
\]

### Theorem 5.1 (one-coordinate network-flow theorem)

Valid occurrence schedules on \(R\) are in bijection with directed paths
from \(u\) to \(v\) in this graph.  Under the bijection, the total weight
of deleted coordinate--cell incidences is the sum of the arc weights
\(\omega\).  Consequently every additive one-coordinate optimization is a
unit-capacity integral longest- or shortest-path problem.

For the whole carrier, separable objectives over coordinates and erosion
runs are optimized by the direct product of these integral path flows.

### Proof

The vertices of a path are precisely the retained occurrences.  An arc of
length \(g\) leaves the \(g-1\) intervening positions as one hole block;
(5.2) is exactly the owner-hitting bound.  Theorem 3.2 says that its deleted
cell incidences are precisely those summed in (5.1).  Conversely every
valid schedule lists its retained positions as such a path.  Path-flow
integrality is standard. \(\square\)

This is the strongest unconditional flow reduction on a fixed arbitrary
carrier.  It optimizes occurrence signatures, not named-target assignment.

## 6. What is laminar, and where laminarity stops

For one fixed start \(j\), not only the envelopes but also the mandatory
collars are nested:

\[
 K_{j,1}\subseteq K_{j,2}\subseteq\cdots\subseteq K_{j,d},
 \qquad
 C^*_{j,1}\subsetneq\cdots\subsetneq C^*_{j,d}.     \tag{6.1}
\]

Therefore, for a fixed target \(S\), the set of indices \(q\) satisfying

\[
                         K_{j,q}\subseteq S\subseteq C^*_{j,q}   \tag{6.2}
\]

is an interval of \(q\)'s: the envelope condition gives a lower cutoff and
the collar condition an upper cutoff.  The individual aperture graph on
one column is thus convex bipartite.  If targets are first partitioned
among columns, their **individual** aperture assignment inside each column
is an ordinary convex matching problem.

This does not make arbitrary simultaneous pins laminar.  A coordinate
introduced at a later nested target needs a private occurrence in the
corresponding interval shell, and cells with different starts cross.  The
exact simultaneous object remains a target--cell matching coupled to the
product of the path flows in Section 5.  Equivalently, for a completely
specified cell deck, each coordinate's zero cells must be a disjoint union
of Ferrers triangles as in (0.9).

The coupling is genuinely nonintegral in general.  A literal depth-three
Johnson segment supports three aperture-compatible assignments whose
pairwise owner-cover conflicts form a triangle: the integral optimum is
one while the cover-cut relaxation has the half-vector of value \(3/2\).
Thus neither the per-coordinate network matrices nor the columnwise convex
graphs combine into one totally unimodular matrix, laminar matroid, or
ordinary matching theorem on an arbitrary fixed carrier.

There are two exact positive subfaces.

1. **Fixed signature.**  Once all path-flow choices are fixed, every cell
   has one value; target allocation is the star matching of Theorem 2.1.
2. **Nested private shells.**  If targets assigned down one nested column
   form an inclusion chain and every newly introduced coordinate has a
   protected point in the new shell, order-preserving assignment is an
   integral DAG path flow.

## 7. Consequence for the general construction

The sparse-rail theorem forces \(\Omega(d)\) occurrence phases for bounded
defect.  Theorem 2.2 now rules out the opposite endpoint \(A=E\): maximum
occurrence density leaves a fixed positive fraction of the lower ideal
below its saturated-chain band.

The first viable dense face must therefore choose a nontrivial distribution
of hole lengths.  Its aggregate rank profile lies in the exact Ferrers cone
(0.11), and its literal occurrence choices lie in the integral path-flow
product of Theorem 5.1.  What remains is one coloured theorem:

> Choose those paths so that the resulting named cell signatures contain
> all but \(O(1)\) strict-lower targets, while the same carrier retains its
> upper, topology, and regenerative gates.

The present theorem proves that no aggregate convexity, occurrence
integrality, or full-erosion chainization obstruction remains before that
coloured coupling.  It equally proves that those facts alone do not solve
the coupling.
