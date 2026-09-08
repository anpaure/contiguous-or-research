# Coloured interval cuts and the two-shore residual factor

## 1. Scope

This note isolates the general mathematics behind the new `k=16`
residence certificate.  The ground points below are selected quotient edge
orbits, in their order around a fixed quotient cycle.  A bad residence motif
is the set of consecutive edge orbits supporting one short physical run.

There are two logically different steps.

1. Delete at least one old edge from every bad interval.
2. Restore degree two and every lost `q1` palette row by new same-shore
   edges.

The first step is an interval problem.  Once the cross edges are fixed, the
degree and `q1` parts of the second step split into one problem on each
shore.  Connectivity, voltage, and bad intervals created by the new edges
do **not** split and are not claimed here.

There is a further ordering constraint which is easy to miss.  A minimum
same-shore interval cut can expose degree at the wrong endpoints for a lost
palette row.  Endpoint palette accessibility must therefore be imposed
while the cut is chosen, before either residual factor is solved.  The
canonical `k=16` cut below fails this precondition even though its uncoloured
degree completion is feasible.

## 2. The exact coloured cyclic-interval theorem

Let `C` be a finite cyclically ordered set and let `I` be a family of
nonempty proper cyclic intervals of `C`.  For `U subseteq C`, call points of
`U` allowed.  Write

\[
 \tau_U(\mathcal I)=
 \min\{|T|:T\subseteq U,\ T\cap I\ne\varnothing\text{ for all }I\in\mathcal I\},
 \tag{2.1}
\]

with value infinity if no such set exists.  Let

\[
 \nu_U(\mathcal I)=\max\{|\mathcal J|:\mathcal J\subseteq\mathcal I,
 \ (I\cap U)_{I\in\mathcal J}\text{ are nonempty and pairwise disjoint}\}.
 \tag{2.2}
\]

Notice that disjointness in (2.2) is disjointness of the *allowed traces*,
not necessarily disjointness of the original cyclic intervals.

### Theorem 2.1 (cuttable coloured-interval min--max)

Assume that some `c_0 in C` belongs to no member of `I`.  If every member of
`I` meets `U subseteq C`, then

\[
 \tau_U(\mathcal I)=\nu_U(\mathcal I),                         \tag{2.3}
\]

If some member misses `U`, then `tau_U=infinity` and no allowed transversal
exists; equation (2.3) is asserted only in the feasible case.

In particular, put `tau=tau_C(I)=nu_C(I)`.  A minimum transversal avoiding
the forbidden set `C setminus U` exists if and only if

\[
 I\cap U\ne\varnothing\quad(I\in\mathcal I),
 \qquad \nu_U(\mathcal I)=\nu_C(\mathcal I).                  \tag{2.4}
\]

Thus (2.4) is an exact, greedily checkable criterion for an all-allowed
minimum transversal.

#### Proof

Cut the cyclic order at `c_0`.  Every member `I` is now an ordinary closed
interval in a linearly ordered set.  Delete the forbidden points and give
`U` its induced linear order.  If `I cap U` is nonempty, then it is still an
interval in this induced order: whenever allowed points `u<v<w` satisfy
`u,w in I`, convexity of `I` gives `v in I`.  Hence the family

\[
 \mathcal I|_U=\{I\cap U:I\in\mathcal I\}
\]

is an ordinary interval hypergraph.

For completeness, the earliest-right-end algorithm proves the interval
min--max theorem.  Choose an interval with smallest right endpoint `r`, put
`r` into the transversal, delete every interval containing `r`, and repeat.
The chosen trigger intervals are pairwise disjoint, while the selected
right endpoints hit every interval.  The packing and transversal therefore
have the same size, proving (2.3).

Apply this first with `U=C` and then with the prescribed allowed set.  If
every original interval meets `U`, every pairwise-disjoint family of
original intervals has pairwise-disjoint allowed traces.  Consequently
`nu_U>=nu_C`.  Equality is therefore equivalent to an allowed transversal
having the unrestricted minimum size.  This proves (2.4).  QED.

### Corollary 2.2 (the two-colour version)

Suppose

\[
 C=C_{AA}\mathbin{\dot\cup}C_{BB}\mathbin{\dot\cup}C_{AB}.
\]

There is a minimum interval transversal using no `AB` point if and only if
every interval meets `C_AA union C_BB` and the earliest-finish packing number
of the traces on `C_AA union C_BB` equals the unrestricted earliest-finish
packing number.

This criterion is dimension-free and makes no probabilistic or
equivariance assumption.

## 3. A local sufficient condition and colour counts

The exact test (2.4) is already linear-time after sorting endpoints.  The
following stronger condition can sometimes be proved directly from a
recursive construction.

Run earliest-finish greedy on the unrestricted linear intervals.  At step
`j`, let `I_j` be the trigger interval and let `B_j` be all intervals deleted
at that step.  Define the common core

\[
 K_j=\bigcap_{I\in\mathcal B_j}I.                              \tag{3.1}
\]

It is nonempty because it contains the selected right endpoint.

### Lemma 3.1 (greedy-block core criterion)

If `K_j cap U` is nonempty for every greedy block, then choosing any

\[
 u_j\in K_j\cap U                                                   \tag{3.2}
\]

gives an allowed minimum transversal.

If `U=U_A dotcup U_B`, let `a_0` be the number of blocks whose core meets
`U_A` but not `U_B`, let `b_0` be defined symmetrically, and let `f` be the
number of cores meeting both colours.  Then minimum transversals supplied by
(3.2) realize every colour split

\[
 (|T\cap U_A|,|T\cap U_B|)=(a_0+s,b_0+f-s),\qquad 0\le s\le f. \tag{3.3}
\]

#### Proof

Every interval belongs to one block and contains the chosen point of that
block, so (3.2) is a transversal.  Each chosen point lies in the trigger
interval `I_j`; the trigger intervals are pairwise disjoint.  Hence the
chosen points are distinct, and their number is the packing number.  The
colour choices in flexible cores are independent, proving (3.3).  QED.

Lemma 3.1 is only sufficient.  The exact criterion remains (2.4): an allowed
minimum transversal can exist even when a particular unrestricted greedy
blocking has a core with no allowed point.

## 4. Weighted and prescribed-colour formulations

After the cut and deletion of forbidden points, enumerate the allowed
points as `1,...,M`, and write every trace as `[l_i,r_i]`.

### Theorem 4.1 (weighted integral dual)

For nonnegative integral costs `w_p`, the program

\[
 \begin{aligned}
 \min &\ \sum_{p=1}^M w_p x_p\\
 \text{subject to }&\ \sum_{p=l_i}^{r_i}x_p\ge1 &&(i\in\mathcal I),\\
 &\ x_p\ge0
 \end{aligned}                                                    \tag{4.1}
\]

has an integral optimum.  Its value equals

\[
 \max\left\{\sum_i y_i:
 y_i\in\mathbb Z_{\ge0},\quad
 \sum_{i:p\in[l_i,r_i]}y_i\le w_p\ (1\le p\le M)\right\}.       \tag{4.2}
\]

#### Proof

The interval incidence matrix has consecutive ones in every row.  Its
transpose has consecutive ones in every column and is totally unimodular;
total unimodularity is preserved by transposition.  Thus the primal and
dual covering/packing polyhedra with integral right sides have integral
optima.  Linear-programming duality gives equality.  QED.

There is also an explicit dynamic program which handles exact colour counts
without appealing to total unimodularity.  Add sentinels `0` and `M+1` of
zero cost.  Put a directed arc `p -> q`, for `0<=p<q<=M+1`, exactly when no
trace interval is contained in the open integer gap

\[
 \{p+1,\ldots,q-1\}.                                             \tag{4.3}
\]

Give the arc the cost `w_q` when `q<=M` and zero otherwise.

### Lemma 4.2 (gap-DAG formulation)

Increasing paths from `0` to `M+1` are in bijection with transversals: the
internal vertices of the path are the chosen points.  Consequently a
shortest path gives (4.1).  If points have colours `AA` and `BB`, augmenting
the state by the two accumulated colour counts decides the existence of a
transversal with any prescribed pair `(a,b)`; restricting to `a+b=tau`
decides prescribed splits among minimum transversals.

#### Proof

A chosen set misses an interval if and only if that interval lies wholly
between two consecutive chosen points (sentinels included).  This is exactly
the forbidden-arc condition in (4.3).  Costs and colour counts add along the
path.  QED.

## 5. The two-shore residual factor lemma

Let `V=V_A dotcup V_B`, and let `F` be a simple spanning 2-factor on `V`.
Fix every cross edge

\[
 C=F\cap E(V_A,V_B).                                             \tag{5.1}
\]

Let `T_A subseteq F[V_A]` and `T_B subseteq F[V_B]` be deleted same-shore
edges.  For `sigma in {A,B}`, define the residual demand

\[
 b_\sigma(v)=d_{T_\sigma}(v),\qquad v\in V_\sigma.              \tag{5.2}
\]

Let `K_sigma` be a catalogue of admissible new same-shore edges, disjoint
from the retained old edges and from the deleted edges.  Decorate each edge
of `K_sigma` with the `q1` palette rows it supplies.  Let `P_sigma` be the
rows on shore `sigma` whose old providers have all been deleted.  This
definition includes only rows not already protected by a retained cross
edge.  Assume the remaining provider incidence is shore-separable: every
at-risk row is assigned to exactly one `P_sigma`, and all of its variable
providers lie in the corresponding `K_sigma`.

### Theorem 5.1 (fixed-cross two-shore decomposition)

There is a degree-two replacement preserving all fixed cross edges and all
old `q1` rows if, for each shore independently, there is a set
`J_sigma subseteq K_sigma` such that

\[
 d_{J_\sigma}(v)=b_\sigma(v)\quad(v\in V_\sigma),               \tag{5.3}
\]

and every row of `P_sigma` is supplied by at least one edge of `J_sigma`.
Indeed,

\[
 F'=(F\setminus(T_A\cup T_B))\cup J_A\cup J_B                  \tag{5.4}
\]

is then a spanning 2-factor with the required `q1` support.

Conversely, every replacement which keeps (5.1) fixed, retains every old
same-shore edge outside `T_A union T_B`, deletes exactly
`T_A union T_B`, and adds only catalogue edges decomposes in this way.
Thus, under this minimal-change convention, degree and `q1` feasibility are
exactly two independent coloured `b`-factor problems.

#### Proof

Deleting `T_sigma` lowers the degree of `v` by exactly (5.2); hence (5.3) is
necessary and sufficient to restore degree two.  Same-shore additions on
opposite shores have disjoint endpoint sets.  With the cross providers
fixed, the at-risk palette rows have the stipulated shore-separable
provider catalogues, so their coverage conditions also separate.  This
proves both directions.  QED.

Theorem 5.1 is the **minimal-change** form: every old same-shore edge outside
`T_A union T_B` is frozen, so `b_sigma=d_{T_sigma}` and the number of new
same-shore edges equals the number deleted.  There is also an exact
**from-scratch shore** form.  Freeze only the cross set `C`, put the retained
same-shore sets equal to the empty set, let `D_sigma` be any forbidden
same-shore edge set (in particular an interval transversal), and define

\[
 b_\sigma(v)=2-d_C(v).                                      \tag{5.4a}
\]

Remove `D_sigma` from the corresponding candidate catalogue.  Then a
degree-two carrier containing exactly the fixed cross edges and no edge of
`D_A union D_B` is equivalent, for degree and shore-separable `q1` support,
to a pair of independent coloured `b_sigma`-factors.  Indeed, the fixed
cross edges give `v` degree `d_C(v)` and no other incidence is retained, so
(5.4a) is its exact residual demand; the converse follows by restricting
any such carrier to each shore.  In this form `b_sigma` need not equal the
incidence of the interval cut.  The numerical `87/60` values count
forbidden transversal edges and do **not** count from-scratch replacement
edges.

This theorem deliberately says nothing about the number of components of
`F'`, the voltage of a quotient component, or residence motifs crossing a
new boundary.  Those are the precise recoupling gates.

### Lemma 5.2 (exact palette-bank reduction)

For one shore, a coloured `b`-factor `J subseteq K` exists if and only if
there is a palette-covering bank `R subseteq K` such that

\[
 d_R(v)\le b(v)\quad(v\in V)                                   \tag{5.5}
\]

and `K setminus R` has a factor of residual degree

\[
 b_R(v)=b(v)-d_R(v).                                            \tag{5.6}
\]

Here one edge of `R` may cover several lost palette rows.

#### Proof

The reverse implication is immediate by adjoining the residual factor to
`R`.  Conversely, from a coloured `b`-factor `J`, choose any subfamily
`R subseteq J` which still covers all required palette rows (for example an
inclusion-minimal one).  Then `J setminus R` has exactly the degrees (5.6).
QED.

Thus palette coverage is not being silently absorbed into an ordinary
degree theorem: the choice of `R` is the genuinely coloured part.  After it
is fixed, the remaining question is an uncoloured factor problem.

For a general loopless candidate graph, Tutte's `f`-factor theorem gives the
exact test.  With `f=b_R`, a residual factor exists if and only if, for every
two disjoint vertex sets `S,T`,

\[
 f(S)+\sum_{v\in T}\bigl(d_{K-R-S}(v)-f(v)\bigr)
 \ \ge\ q(S,T),                                                  \tag{5.7}
\]

where `q(S,T)` is the number of components `Q` of
`(K setminus R)-(S union T)` for which

\[
 f(Q)+e(Q,T)\quad\hbox{is odd}.                                 \tag{5.8}
\]

The bipartite Hall theorem below is a more transparent sufficient
specialization.  Merely cloning vertices of a nonbipartite quotient graph
does not justify Hall: the odd-component terms in (5.7) are real.

At quotient level a selected loop contributes degree two.  The exact safe
procedure is to choose a loop subset containing at most one loop at each
vertex, subtract two from the demand at each chosen loop endpoint (and
record its palette contribution), delete every remaining loop, and then
apply Lemma 5.2 or (5.7) to the resulting loopless graph.  This is exact:
degree at most two permits at most one selected loop at a vertex, and every
loop consumes both degree units.  Treating a quotient loop as a
unit-capacity ordinary edge would give a false degree ledger.  The physical
lift, used in Theorem 5.1, is loopless and needs no such convention.

### Lemma 5.3 (endpoint palette-accessibility clause)

For a shore demand `b`, let

\[
 K[b]=\{e\in K:d_{\{e\}}(v)\le b(v)
                 \text{ for every endpoint }v\}.              \tag{5.9}
\]

Thus a nonloop `uv` belongs to `K[b]` only when `b(u),b(v)>=1`, while a
loop at `v` requires `b(v)=2`.  If a coloured `b`-factor exists, then every
lost palette row `q` has an endpoint-accessible provider:

\[
 K[b]\cap\{e:q\in\lambda(e)\}\ne\varnothing.                  \tag{5.10}
\]

#### Proof

The selected factor edge which supplies `q` consumes its incidence at each
endpoint without exceeding `b`; it therefore belongs to `K[b]`.  QED.

In the minimal-change form, write `x_e=1` when an old same-shore edge is
deleted and put `a_v=1[d_D(v)>=1]`.  For a nonloop candidate provider
`e=uv`, introduce an accessibility indicator `z_e` with

\[
 z_e\le a_u,\qquad z_e\le a_v.                         \tag{5.11}
\]

If `P_0(q)` is the old provider bank of `q` and `P_1(q)` its off-seed
same-shore providers, the exact necessary cut-selection clause is

\[
 \sum_{p\in P_0(q)}(1-x_p)+
 \sum_{e\in P_1(q)}z_e\ge1.                            \tag{5.12}
\]

Equivalently: if the cut deletes every old provider of `q`, it must expose
both endpoints of at least one new provider.  Loop indicators use the
condition `d_D(v)=2`.  Clauses (5.11)--(5.12) are only the singleton rows of
the eventual coloured-factor problem; simultaneous endpoint congestion and
odd-set obstructions remain for Hall/Tutte.  Nevertheless they must be
imposed jointly with the interval-cut variables, because no later shore
factor can repair a row which fails (5.10).

## 6. A checkable Hall sufficient condition

The endpoint clause (5.10) is only singleton Hall.  The following strong
condition constructs the protected palette bank itself.

### Lemma 6.1 (palette-atom Hall)

Partition the lost palette rows into atoms, each containing at most one
lower and at most one upper row.  Let `W subseteq K[b]` be a candidate
reservoir satisfying

\[
                    d_W(v)\le b(v)\quad(v\in V).       \tag{6.1}
\]

Join an atom `A` to `e in W` when `e` supplies every row of `A`.  If

\[
 |N(\mathcal A)|\ge|\mathcal A|
 \quad\text{for every subfamily of atoms }\mathcal A,  \tag{6.2}
\]

then there is a palette-covering bank `R subseteq W` with `d_R<=b`.

#### Proof

Hall's theorem gives distinct representative edges for the atoms.  Their
set `R` covers every lost row.  Since `R subseteq W`, (6.1) gives the degree
bound.  QED.

Singleton atoms are always allowed; pairing one lower row with one upper row
records the useful fact that one edge may repair both.  Lemma 6.1 is
sufficient rather than necessary because the global reservoir bound (6.1)
may discard usable overlapping choices.  It upgrades endpoint accessibility
to a genuinely simultaneous palette test.

After such a bank is selected, the following supplies a usable, though not
necessary, certificate for the residual degrees.

### Theorem 6.2 (palette reservation plus capacitated Hall)

Fix a shore and suppress `sigma`.  Suppose there is a set `R subseteq K`
such that

1. `d_R(v)<=b(v)` for every vertex;
2. every lost palette row in `P` is supplied by `R`.

Put `b'(v)=b(v)-d_R(v)`.  Suppose `K setminus R` contains a bipartite
spanning subgraph `H` with parts `L,R_0` such that

\[
 b'(L)=b'(R_0)                                                   \tag{6.3}
\]

and, for all `X subseteq L` and `Y subseteq R_0`,

\[
 b'(X)\le e_H(X,R_0\setminus Y)+b'(Y).                          \tag{6.4}
\]

Equivalently, it is enough to check the one-set form

\[
 b'(X)\le
 \sum_{y\in R_0}\min\{b'(y),e_H(X,\{y\})\}
 \qquad(X\subseteq L).                                         \tag{6.5}
\]

Then `R` extends to a set `J` satisfying (5.3) and every palette requirement.

#### Proof

Build a network with arcs `s -> x` of capacity `b'(x)` for `x in L`, arcs
`x -> y` of capacity one for `xy in E(H)`, and arcs `y -> t` of capacity
`b'(y)` for `y in R_0`.  A cut with source side
`{s} union X union Y` has capacity

\[
 b'(L\setminus X)+e_H(X,R_0\setminus Y)+b'(Y).
\]

Condition (6.4) says that every cut has capacity at least `b'(L)`.  By
max-flow/min-cut and integrality, there is an integral flow of this value.
It saturates every vertex demand on both sides by (6.3), and its unit
middle arcs form a simple `b'`-factor.  Add it to the reserved set `R`.
For fixed `X`, minimizing the right side of (6.4) over `Y` independently at
each right vertex gives (6.5), proving the asserted equivalence.  QED.

For residual demands at most one, (6.4) reduces to the familiar matching
Hall conditions.  For demands two, the two-set form (6.4), rather than the
weaker inequality `b'(X)<=b'(N(X))`, is needed because candidate edges have
unit capacity.

Artificially replacing a nonbipartite edge by two directed copies does not
make Theorem 6.2 applicable: a flow can then select both orientations or
give the wrong total incidence at an original vertex.  One needs a genuine
bipartite residual subgraph, or else the Tutte test (5.7).

The companion note
`THREAD_A_TWO_SHORE_COLOURED_FFACTOR_LAMINAR_HALL_20260729.md` sharpens this
wrapper.  On a bipartite scaffold it proves the exact forced-bank Benders
cost

\[
 e_P(L\setminus X,Y)\le
 e(X,R\setminus Y)-b(X)+b(Y),                          \tag{6.6}
\]

and a laminar-matroid Rado--Hall theorem which selects paired lower/upper
providers while respecting every endpoint and Benders capacity.  That is
the strongest current dimension-uniform sufficient condition for the
palette bank; Theorem 6.2 then completes the residual factor.

## 7. Application boundary at `k=16`

The audited `k=16` data give a cyclic family of `226` residence motifs on an
`858`-edge quotient cycle.  Exactly `300` cycle positions are outside all
motifs, so Theorem 2.1 applies.  The certificate contains

* `147` pairwise edge-disjoint motifs;
* a `147`-edge transversal;
* a second `147`-edge transversal containing no cross edge, split as
  `87 AA + 60 BB`.

The packing and either transversal prove

\[
 \tau=\nu=147,
 \qquad
 \tau_{AA\cup BB}=147.                                         \tag{7.1}
\]

The new conceptual point is that the second equality is governed exactly by
the restricted-trace interval theorem (2.4); it is not an accidental
general hitting-set phenomenon.

After fixing all `AB` edges, deleting the indicated `87` and `60`
same-shore edges produces two independent demand vectors.  Theorem 5.1 says
that degree and current `q1` reconstruction may now be attempted by two
independent coloured residual factors.  It does **not** say that this
particular cut makes either coloured factor feasible.

### 7.1 The canonical `87/60` cut fails endpoint accessibility

The uncoloured degree equations for this fixed cut are feasible.  The
palette rows already fail the necessary singleton condition (5.10), however.
The exact zero-access rows are

\[
\begin{array}{c|c|l}
\text{shore}&\text{palette}&\text{colour labels}\ \hline
AA&\text{lower}&0{:}2765\\
BB&\text{lower}&1{:}845,\ 1{:}1433,\ 1{:}2347\\
BB&\text{upper}&1{:}703,\ 1{:}1751,\ 1{:}1963,\
                  1{:}3739,\ 1{:}6765.
\end{array}                                                   \tag{7.2}
\]

Thus four lost lower rows and five lost upper rows have no off-seed
same-shore provider whose two endpoints carry residual degree.  Lower-palette
completion alone and upper-palette completion alone are each infeasible,
even though degree completion alone is feasible.  This is a direct
structural no-go, not an odd-set or connectivity failure.

Consequently the `87/60` transversal certifies the coloured interval theorem
but is not a repair seed.  A candidate cut must be selected jointly with the
endpoint clauses (5.11)--(5.12) before the protected-bank and residual-factor
tests are run.

### 7.2 Every fixed-cross minimum cut is infeasible

The failure is not peculiar to the displayed `87/60` choice.  The `147`
packed motifs are pairwise edge-disjoint and have union size `476`.  Every
radius-`147` transversal chooses exactly one edge from each packed motif and
therefore lies in this union.  The joint model makes all those choices
simultaneously, while

* fixing all `80` old `AB` edge orbits and forbidding new `AB` edges;
* allowing all `23218` off-seed nonloop `AA/BB` replacement seams;
* hitting all `226` old residence motifs;
* balancing degree exactly at all `858` quotient vertices; and
* covering every lower and upper q1 row.

This relaxation is `INFEASIBLE`.  Connectivity, voltage, and newly created
residence motifs are not even reached.  Hence, in the loopless quotient-seam
model,

\[
 \boxed{\text{radius }147+\text{ fixed cross pattern}
        \quad\Longrightarrow\quad\text{no q1-complete degree-two rethread}.}
                                                               \tag{7.3}
\]

The minimum-distance route must therefore either alter the cross pattern or
use more than `147` old-edge deletions.  This finite no-go does not weaken
the dimension-uniform separation theorem: for any cut and frozen cross set,
degrees and q1 still reduce exactly to the two shore problems.  It shows that
the first viable cut cannot be chosen from the current fixed-cross
minimum-radius face.  After a viable shore pair is found, connectivity,
combined voltage, and newly created boundary motifs are precisely the joint
recoupling audits.

The exact finite sources are

```
scratch/k16_qfactor_q1_topresident_hamilton_residence_motifs_20260729.audit.json
scratch/k16_residence_motif_matching147_20260729.json
scratch/audit_k16_residence_motif_structure_20260729.py
scratch/k16_residence_fixed_cross_same_shore_transversal_barrier_20260729.json
scratch/k16_same_shore_radius147_noab_cegar_20260729.json
scratch/search_k16_same_shore_joint_cut_seam_cegar_20260729.py
```

The four JSONs listed above have respective SHA-256 values

```text
bf762af0339ec581d01e9c48991610425e51a864e065be23b8d23d21efbbf1f6
485283298cd4cf1db19bf45401dd08a8484cf11004755d9f88cab6c972122a6b
93936bcc90b3a627f8fea38d1038136c17278f63fdbb623f69ea8bd28703dcb2
9ebd21730c08d6ddb848012821dd7d91ff1d2fe141f089555bd9052dfcfd3a95.
```

The numerical certificate is input to Section 7; Theorems 2.1--6.2 are
dimension-uniform and independent of `k=16`.  The structural endpoint table
(7.2) is solver-free.  The global no-go (7.3) is a trusted exact CP-SAT
`INFEASIBLE` record (3.04 seconds, `160567` branches, `12640` conflicts);
the retained JSON does not contain a standalone proof log.
