# The decorated-two-factor configuration system and its exact relational induction

Date: 2026-07-31  
Status: exact all-dimension equivalence and exact accepting-root composition
theorem; explicit `m=4` accepting base; no all-dimension existence or
contiguous-OR theorem

## 0. Verdict

Hamiltonicity is not part of the weakest central Catalan trace target.  The
right integral object is a spanning Middle Levels `2`-factor, a residual
matching on its unmarked occurrences, and two globally exact turn-colour
transversals, with every factor cycle on the corrected forest side of the
binary trace law.

This note gives two exact formulations of that target.

1.  A local integral configuration system chooses the `2`-factor and the
    decoration simultaneously.  It is feasible if and only if a corrected
    decorated `2`-factor exists.
2.  On every normalized recursive decomposition, the relations of all
    feasible boundary configurations compose by natural join, literal trace
    concatenation, and existential projection.  The empty root relation is
    accepting if and only if the integral configuration system is feasible.

Thus an exact relational induction is available without a Hamilton cycle and
without retaining one decoration through every glue.  What remains open is
the substantive statement that an accepting root state exists for every
`m`.  The positive `ML(7)` incidence-hex repair supplies the `m=4` base and
also proves that separate turn surjections, or independently nonempty local
transparency/decorability predicates without one propagated common state, are
too weak.

## 1. Local configuration variables

Fix `m>=2`, put

\[
 \mathcal A=\binom{[2m-1]}{m-1},\qquad
 \mathcal B=\binom{[2m-1]}m,
\]

and let `G_m=ML(2m-1)` be their inclusion graph.  For a vertex `v`, let
`P(v)` be the set of unordered pairs of distinct edges incident with `v`.
If `p={vx,vy}` belongs to `P(v)`, define its turn colour by

\[
 \tau_v(p)=
 \begin{cases}
 x\cup y,&v\in\mathcal A,\\
 x\cap y,&v\in\mathcal B.
 \end{cases}                                         \tag{1.1}
\]

The two values have ranks `m+1` and `m-2`, respectively.

Use binary variables

\[
 z_{v,p},\quad w_{v,p},\quad y_e,\quad r_e.
\]

Here `z` chooses the two factor edges at an owner, `w` marks that owner by
its turn, `y` is the resulting factor edge set, and `r` is the residual
matching.  Put

\[
 \sum_{p\in P(v)}z_{v,p}=1                                      \tag{1.2}
\]

for every `v`.  For every edge `e=uv`, impose

\[
 y_e=\sum_{p\in P(u):e\in p}z_{u,p}
     =\sum_{p\in P(v):e\in p}z_{v,p}.                           \tag{1.3}
\]

The mark variables obey

\[
 0\le w_{v,p}\le z_{v,p},\qquad
 t_v:=\sum_{p\in P(v)}w_{v,p}\le1.                              \tag{1.4}
\]

The two palettes are exact:

\[
 \sum_{\substack{v\in\mathcal A, p\in P(v)\\
                  \tau_v(p)=U}}w_{v,p}=1
 \quad\left(U\in\binom{[2m-1]}{m+1}\right),                    \tag{1.5a}
\]

\[
 \sum_{\substack{v\in\mathcal B, p\in P(v)\\
                  \tau_v(p)=L}}w_{v,p}=1
 \quad\left(L\in\binom{[2m-1]}{m-2}\right).                    \tag{1.5b}
\]

Finally,

\[
 0\le r_e\le y_e,qquad
 t_v+\sum_{e\ni v}r_e=1
 \quad(v\in\mathcal A\cup\mathcal B).                          \tag{1.6}
\]

For a cycle `C` of the selected graph `(V,y)`, read the cyclic word
`chi_C=(t_v:v in C)`.  Call it **forest-safe** when either

* it is all zero; or
* it contains both symbols and either some zero-run has length different
  from two or some one-run has even length.

Equivalently, the forbidden cyclic traces are the all-one word and the
partial cycle face

\[
 \text{every positive zero-run has length two and every one-run is odd}.
                                                               \tag{1.7}
\]

Add the requirement

\[
                  \chi_C\text{ is forest-safe for every }C.    \tag{1.8}
\]

## 2. Exact equivalence

### Theorem 2.1 (integral decorated-factor equivalence)

The binary system (1.2)--(1.8) is feasible if and only if `ML(2m-1)` has a
componentwise decorated spanning `2`-factor whose diamond lift is a spanning
linear forest with exactly `Cat_m` path components.

#### Proof

Suppose first that (1.2)--(1.8) is feasible.  Equation (1.2) chooses two
incident edges at each owner, and (1.3) makes the choices agree at the two
ends of every edge.  Hence `F={e:y_e=1}` is a spanning `2`-factor.

If `t_v=1`, the unique nonzero `w_{v,p}` selects the turn determined by the
two neighbours of `v` in `F`.  Equations (1.5a)--(1.5b) select every upper
and lower turn colour exactly once.  If `t_v=0`, (1.6) gives exactly one
residual factor edge at `v`; if `t_v=1`, it gives none.  Because `r_e` is one
edge variable shared by its two endpoints, the residual edges match exactly
the unmarked occurrences.

On a marked factor cycle, each zero-block is therefore a path with a perfect
matching, so its order is even.  Since `F` is bipartite, consecutive marked
occurrences have opposite shores.  Thus the selected shore types alternate.
An entirely unmarked cycle receives one of its two alternating residual
phases.  We have obtained a componentwise Catalan decoration.

The component-local lift law is exact.  An all-zero trace gives disjoint
cross edges.  An all-one trace gives the two rail cycles.  For a partial
trace, a zero-run of length at least four breaks both rails; when every
zero-run has length two, a rail closes exactly when all intervening one-runs
are odd.  Consequently (1.8) is precisely the condition that no physical
cycle survives.  The perfect diamond matching has

\[
 \binom{2m}{m-1}
 =\binom{2m}m-\operatorname {Cat}_m
\]

edges on `binom(2m,m)` physical vertices, so the resulting linear forest has
exactly `Cat_m` components.

Conversely, take a corrected decorated factor.  Let `z` record the two
factor edges at each owner, let `y` be its edge set, and let `w` record its
selected turn occurrences.  On a marked component, alternation leaves even
unmarked paths and hence a unique residual matching; on an unmarked
component choose either alternating residual phase.  Record these edges by
`r`.  Then (1.2)--(1.6) hold.  The global turn bijections give (1.5), and
the linear-lift hypothesis is exactly (1.8).  ∎

### Corollary 2.2 (fixed-factor slice)

After `z,y` are fixed, (1.4)--(1.6) are precisely the perfect-matching
system of the turn-augmentation graph of that factor.  Equivalently, choose
an upper occurrence transversal `I`.  Its size is

\[
 |I|=\binom{2m-1}{m+1}=\binom{2m-1}{m-2},            \tag{2.1}
\]

which is both the number of cyclic `I`-gaps and the number of lower colours.
The fixed factor is decorable exactly when, for some `I`, the
occurrence-labelled gap--lower-colour graph has a perfect matching.  The
matched occurrence labels then determine (1.8); it is forest-safe decorable
exactly when some such perfect matching also passes that test.  Separate
upper and lower turn surjections do not imply this gap Hall condition.

## 3. A finite trace monoid

### Lemma 3.1

There is an absolute finite monoid `M_tr` which summarizes a finite binary
path word, composes under concatenation, and decides (1.8) when the two ends
are cyclically joined.

#### Proof

For a nonempty word record its first and last symbols, whether it is
homogeneous, whether both symbols have occurred, the first and last zero-run
lengths capped in `{1,2,3+}`, the first and last one-run parities, and one
breaker bit.  The breaker says that an already closed zero-run has length
different from two or an already closed one-run has even length.  Add one
empty state.

Concatenation has a finite exact case table.  When the two boundary symbols
agree, merge the two runs, using capped addition for zero-runs and addition
modulo two for one-runs.  The merged run is internal precisely when neither
input word is homogeneous; otherwise it remains the prefix or suffix (or
the whole word).  When the boundary symbols differ, the suffix run of the
left word is internal precisely when the left word is not homogeneous, and
the prefix run of the right word is internal precisely when the right word
is not homogeneous.  Every run which becomes internal updates the breaker.
The untouched outer run data are copied.  All these decisions and updates
are determined by the displayed finite summary.

Hence the summary of a concatenation depends only on the two input
summaries.  Since it is the exact summary of the literal concatenation, the
operation is associative.  Reversal swaps the prefix and suffix data and
leaves the breaker unchanged, giving the required anti-involution on
`M_tr`.

At cyclic closure, handle homogeneous words separately.  For a mixed word,
merge and test the suffix and prefix runs when their symbols agree; when the
symbols differ, close and test both without merging.  Accept exactly when a
bad maximal run has then set the breaker.  Thus all zero is accepted, all
one is rejected, and the mixed acceptance test is exactly (1.8).  ∎

## 4. Exact relational induction

A recursive decomposition is **normalized** when every local choice/use
atom is introduced at exactly one node, child interiors are disjoint, and:

1. every local pair choice `z_{v,p}` is processed together with its two edge
   incidences and its turn-colour resource before `v` is forgotten;
2. a palette colour remains exposed until every occurrence capable of using
   it has been processed; and
3. every selected local pair exports its two selected factor half-edges
   until the corresponding full edges are identified; the open selected
   half-edges of every partial component are exposed, and a component is
   forgotten only after it closes and passes the cyclic `M_tr` test.

Such a decomposition always exists for the finite instance; no bounded
adhesion is asserted.

At a node `x`, let `Sigma_x` be the relation of all boundary states realized
by integral choices in its processed subtree.  A state records:

* every exposed local-pair choice, the selected status of its open
  half-edges, and the common `(y_e,r_e)` values of every exposed full edge;
* the residual-matching degree and mark status at every exposed owner;
* the partial use degree in `{0,1}` of every exposed upper or lower colour;
* the pairing of exposed selected half-edges induced by the partial factor
  paths (a newly chosen owner is the one-vertex path between its two
  half-edges); and
* an oriented `M_tr` label on each such half-edge-to-half-edge path; reversing
  its orientation applies the reversal anti-involution.

Every factor cycle already closed in the subtree has passed (1.8).
Each owner bit `t_v` is written into exactly one path word, at the unique
node introducing its local-pair atom.  Full-edge identification concatenates
two disjoint owner words and never writes either endpoint again; this is the
endpoint convention used below.

### Theorem 4.1 (accepting-root composition)

For a normalized decomposition, the parent relation is obtained exactly by
the following operations:

1. choose one state from every child relation and local integral atoms at
   the parent;
2. natural-join equal decision variables, add the child and local
   owner/residual/palette degrees, and reject an inconsistent edge choice or
   any degree exceeding its capacity;
3. require each forgotten owner to satisfy (1.2), (1.4), and (1.6), each
   forgotten full edge to satisfy (1.3) and `r_e<=y_e`, and each forgotten
   colour to satisfy its row of (1.5);
4. identify the two selected half-edges of every processed full edge, splice
   the resulting factor paths, and multiply their `M_tr` labels in literal
   traversal order;
5. whenever a factor cycle closes, apply the cyclic test and reject it unless
   it is forest-safe; and
6. existentially project the child data not exposed at the parent.

The empty root relation contains an accepting state if and only if the
system (1.2)--(1.8) is feasible.

#### Proof

Restrict any global integral solution to the processed atoms of a node.
Edge consistency, degrees, palette uses, the residual matching, open-path
connectivity and the literal trace summaries give one state of `Sigma_x`.
Restriction commutes with Steps 1--6, so every global solution reaches an
accepting root state.

Conversely, join witnesses for the selected child states with the local
atoms.  Natural-join consistency makes decision variables identical on
overlaps, while addition of partial degrees counts every use exactly once.
The normalized forgetting rules certify every equation at the last node
where all its variables are visible.  Before identifications,
every chosen owner has exactly two selected half-edges.  After any subset of
full-edge identifications, each nonclosed partial component is therefore a
half-edge-to-half-edge path; its pairing and monoid product are exact.  Every
component is tested once, when its last two half-edges are identified and it
closes.  Induction up the decomposition yields an integral assignment
satisfying (1.2)--(1.8) at an accepting empty root.  ∎

If a boundary exposes `b` owner/edge objects and `c` palette colours, a
coarse state bound is

\[
 m^{O(b)}2^{O(b+c)}\operatorname {Bell}(2b)
       |M_{\rm tr}|^{O(b)}.                          \tag{4.1}
\]

This proves finite exact composition, not bounded width or root
nonemptiness.

### Corollary 4.2 (the exact induction gate)

The Decorated Middle Levels `2`-Factor Theorem follows from either of the
following genuinely substantive statements:

* a direct integral construction satisfying (1.2)--(1.8) for every `m`; or
* a normalized all-`m` recursion whose correlated relation `Sigma_root`
  contains an accepting state.

It is not enough to prove the two palettes separately, to keep only a
nonempty projection of each local relation, or to prove that every chosen
glue admits some decoration independently.

## 5. The positive `ML(7)` hex and the hierarchy

The authenticated `m=4` construction begins with the explicit gap-Hall
counterexample and applies one standard incidence-hex toggle.  The output is
a decorated Hamilton cycle, hence a one-component solution of
(1.2)--(1.8), whose diamond lift has `Cat_4=14` paths.

For a **fixed** decoration, a hex toggle preserves that decoration exactly
when:

1. the selected local turn-colour multisets agree separately on the two
   shores; and
2. the retained-fragment boundary mark types alternate after reconnection.

This is the diagonal part which retains the same selected owner set and
preserves its two local colour multisets.  The residual matching `r` may
change when the factor edges change, and even the indexed variable
`w_{v,p}` changes when the same selected owner acquires a new neighbour pair.
It is not the whole relation.  In the exact `ML(7)` census there are `31`
alternating hexes, `16` Hamilton outputs, `10` decorable outputs, but only
`6` outputs sharing a forest decoration with the input.  Thus the exact
logical hierarchy is

\[
 \begin{array}{c}
 \text{joint alternating SDR + transparent gluing tree}\\
 \Downarrow\\
 \text{decorated Hamilton cycle}\\
 \Downarrow\\
 \text{corrected decorated spanning `2`-factor}.
 \end{array}                                         \tag{5.1}
\]

The first line is a strong recursive certificate.  The last line is the
minimal central existential target.  Neither separate rainbows nor an
arbitrary upper SDR imply it, because the occurrence-labelled gap graph can
fail Hall.

Finally, any two spanning `2`-factors are connected through spanning
`2`-factors by toggling the closed alternating circuits in their symmetric
difference.  This removes component topology as an existential obstruction,
but it does not preserve a decoration at intermediate factors.  Theorem 4.1
correctly recomputes the correlated decoration state.

## 6. Scope

Theorems 2.1 and 4.1 prove an exact central reduction, not the all-`m`
existence theorem.  Even that existence theorem would prove only Catalan
Linear Matching.  Exact `nu(k)=B(k)` additionally requires one chronology
with residence, the deeper lower/upper shadow tower, protected
seams/voltage where used, and the integral compiler/common-`Q` state.

The fixed-rotation ECO component path and transparent private-collar lanes
remain useful ways to transport those stronger downstream states, but they
are not hypotheses of the minimal decorated-`2`-factor theorem.
