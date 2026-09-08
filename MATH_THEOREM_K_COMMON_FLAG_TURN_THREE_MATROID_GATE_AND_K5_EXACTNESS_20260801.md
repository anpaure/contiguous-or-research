# The common flag-turn gate is three-matroid intersection; the first literal case is integral

**Date:** 2026-08-01  
**Lane:** K, protected SCD / common integral chronology  
**Status:** unconditional exact formulation, a minimal abstract
fractional--integral obstruction, two exact tractable subclasses, and an
analytic solution of the complete `(k,m,d)=(5,2,2)` face.  This note does
not construct the all-dimensional common rounding.

## 0. Verdict

Fix one literal flag at every rank-`m` root, and suppose its marked suffixes
already have the required exact named-target multiplicities.  The remaining
owner-exact cycle-cover problem is exactly a common-base problem for three
matroids on the attachment columns:

1. the head-root partition matroid;
2. the owner partition matroid; and
3. the transversal matroid represented by the legal predecessor lists.

Thus the statewise Hall and owner-rainbow rows are one instance of
**three-matroid intersection**.  They are not ordinary matroid intersection.
The smallest generic fractional obstruction has two vertices on each shore
and four columns of weight `1/2`; disjoint copies have linear integral
deficiency.  Consequently fractional feasibility, by itself, gives no
bounded one-copy defect.

The minimal four-column obstruction cannot occur in the literal Boolean
turn geometry `o=p union q`.  At the first literal case,
`(k,m,d)=(5,2,2)`, something stronger happens: fractional owner exactness
forces the unique integral matching.  The `24` fractionally feasible flag
tables in the complete census are exactly the `24` labelled regular
tournaments on five vertices.

Two all-dimensional subclasses remain ordinary matching problems:

* a fixed bijective functional owner attachment; and
* a head-separable turn support
  `H={(p,q,o):pq in G, qo in J}`.

In the second subclass, even with fixed protected turns, exact completion is
equivalent to Hall in the two residual bipartite graphs `G` and `J`.

The result isolates the exact one-copy gap.  SCD/layered flow proves the
named-target projection, and the pull clock proves a correlated fractional
projection, but a positive theorem must force one of the tractable support
structures above or supply genuine three-matroid/odd-cycle absorption.

## 1. Attachment columns and the predecessor matroid

Let `P,Q,O` be copies of, respectively, the tail roots, head roots, and
rank-`(m+1)` owners; all three shores have size `N`.  Fix a complete rooted
flag table `F`, one flag at each root.  Let `A` be the set of aligned
attachment columns.  A column `a` records

\[
                 q(a)\in Q,\qquad o(a)\in O,
                 \qquad q(a)\subset o(a).                 \tag{1.1}
\]

Parallel physical or quotient-phase columns are retained.  Let

\[
 P_F(a)\subseteq P                                           \tag{1.2}
\]

be the set of tails whose fixed flag can literally precede the fixed flag
at `q(a)` using incoming owner `o(a)`.  These are precisely the predecessor
sets in the chronology-first owner/flag Hall theorem.

Define three matroids on ground set `A`.

* `M_Q` is the partition matroid with parts
  `A(q)={a:q(a)=q}`, each of capacity one.
* `M_O` is the partition matroid with parts
  `A(o)={a:o(a)=o}`, each of capacity one.
* `M_P` is the transversal matroid represented by the bipartite graph
  between `A` and `P`, with `a` adjacent to every `p in P_F(a)`.

### Theorem 1.1 (exact three-matroid common-base formulation)

The fixed flag table `F` has a literal owner-exact directed cycle cover if
and only if `M_Q,M_O,M_P` have a common base of size `N`.

#### Proof

Let `D` be such a common base.  Since `D` has size `N` and is independent
in `M_Q`, it contains exactly one column at every head.  Independence in
`M_O` similarly says that it contains exactly one column at every owner.
Independence in `M_P` supplies distinct representatives

\[
                         p(a)\in P_F(a)\qquad(a\in D).        \tag{1.3}
\]

There are `N` of them on an `N`-element tail shore, so every tail occurs
once.  The triples

\[
                         (p(a),q(a),o(a)),\qquad a\in D,      \tag{1.4}
\]

therefore use every tail, head, and owner exactly once, and every triple is
a literal turn by (1.2).  They form the desired directed permutation.

Conversely, from an owner-exact directed cycle cover take its attachment
column at every head.  The selected columns use every head and owner once,
and their distinct predecessor tails are an SDR.  They are a common base of
the three matroids.  `square`

The rank inequalities of `M_P` are exactly the weighted predecessor-Hall
cuts.  Indeed, for a vector `z` with `z(A)=N`, membership in the base
polytope of `M_P` is equivalently the existence of a fractional matching
from column mass `z_a` to unit tail demands.  Capacitated Hall gives

\[
 z(A_X)\ge |X|\quad(X\subseteq P),\qquad
 A_X=\{a:P_F(a)\cap X\ne\varnothing\}.                       \tag{1.5}
\]

Consequently the natural fractional common master is exactly

\[
             B(M_Q)\cap B(M_O)\cap B(M_P).                   \tag{1.6}
\]

The first two base polytopes impose an owner-attachment perfect matching;
the third imposes a predecessor SDR.

### Corollary 1.2 (Boolean core-flow refinement)

For literal all-high flags, the predecessor transversal is not an arbitrary
transversal matroid.  The overlap-core theorem compresses its uncoloured
matching as follows.  After assigning each head to a bottom core, every
rail/core node `v` has two sets of equal size:

\[
             Z_v=\{\hbox{exposed tail labels}\},\qquad
             P_v=\{\hbox{incoming addition labels}\}.       \tag{1.7}
\]

The local matching is any bijection

\[
                  \sigma_v:Z_v\longrightarrow P_v,
                  \qquad z\ne\sigma_v(z).                    \tag{1.8}
\]

Such a bijection always exists except for a one-by-one diagonal.  Hence,
after the flags are fixed, the uncoloured statewise Hall row is a network
flow and is integral.  The genuinely nonnetwork part of Theorem 1.1 is the
global demand that the owner labels

\[
                       w\cup A\cup\{z,\sigma_v(z)\}           \tag{1.9}
\]

be all distinct.  In other words, the three-matroid formulation is exact,
but Boolean geometry localizes its difficult row to a rainbow choice among
local derangements.  This agrees with
`MATH_THEOREM_K_OVERLAP_CORE_FLOW_AND_ROOT_COLOURED_CIRCULATION_GATE_20260801.md`.

### Corollary 1.3 (protected columns)

Let `S subseteq A` be a prescribed attachment set which is independent in
all three matroids.  A cycle cover containing those columns exists exactly
when the contractions

\[
                         M_Q/S,\quad M_O/S,\quad M_P/S       \tag{1.10}
\]

have a common base of size `N-|S|`.

If the actual predecessor turns, rather than only their attachment columns,
are prescribed, delete their used tail, head, and owner resources first and
apply Theorem 1.1 to the residual instance.  This distinction is necessary:
contraction in `M_P` preserves an SDR for the prescribed columns, not a
specified representative of each column.

## 2. Why ordinary matroid intersection stops

Even before owner colours are imposed, the edge sets of perfect matchings
are not the bases of a matroid on the edge ground set.  In `K_(2,2)` the
two perfect matchings are

\[
 B_0=\{e_{00},e_{11}\},\qquad
 B_1=\{e_{01},e_{10}\}.                                    \tag{2.1}
\]

For `e_(00) in B_0-B_1`, replacing it by either element of `B_1-B_0`
does not give a perfect matching.  The basis-exchange axiom fails.
Accordingly a statewise matching is already an intersection of its tail
and head partition matroids; owner-rainbow adds a third partition matroid.
The attachment formulation of Theorem 1.1 packages the predecessor
matching as a transversal matroid, but still leaves three matroids.

This does not rule out a problem-specific extended formulation.  It proves
that no argument which merely calls the three natural constraint families
one matroid intersection is valid.

## 3. The smallest generic fractional--integral obstruction

Take

\[
 P=\{p_0,p_1\},\quad Q=\{q_0,q_1\},\quad O=\{o_0,o_1\}.     \tag{3.1}
\]

Use four attachment columns

\[
\begin{array}{c|c|c}
a&q(a),o(a)&P_F(a)\\ \hline
a_{00}&q_0,o_0&\{p_0\}\\
a_{01}&q_0,o_1&\{p_1\}\\
a_{10}&q_1,o_0&\{p_1\}\\
a_{11}&q_1,o_1&\{p_0\}.
\end{array}                                                   \tag{3.2}
\]

### Proposition 3.1 (minimal half-integral obstruction)

The vector

\[
                             z_{a_{ij}}={1\over2}             \tag{3.3}
\]

lies in all three base polytopes in (1.6), but there is no common integral
base.

#### Proof

Every head and owner sees two half-columns, so the `M_Q` and `M_O` base
equations hold.  In the predecessor representation, `p_0` is adjacent to
`a_(00),a_(11)` and `p_1` to `a_(01),a_(10)`.  Giving each of the two
columns at a tail weight `1/2` is in the transversal base polytope.

There are only two head--owner perfect matchings.  The diagonal one selects
`a_(00),a_(11)`, both of which have the sole predecessor `p_0`.  The
off-diagonal one selects `a_(01),a_(10)`, both of which have the sole
predecessor `p_1`.  Neither is independent in `M_P`.  `square`

This is smallest in shore size: at `N=1` a feasible fractional point is the
single integral column.  At `N=2`, any nonintegral doubly stochastic
head--owner point uses the four-cycle support in (3.2), up to deleting
zero-weight columns and relabelling.  Thus (3.2) is the minimum natural
three-matroid witness.

Taking `t` disjoint copies gives fractional perfect value `2t` but integral
matching number only `t`.  Hence a theorem based only on fractional
feasibility of the unrestricted three-matroid system cannot imply an
`O(1)` one-copy defect.

### Proposition 3.2 (the minimum witness is not a literal Boolean turn)

The four atoms corresponding to (3.2) cannot all satisfy

\[
                         o=p\cup q,\qquad |p|=|q|=m,\quad
                         |o|=m+1.                              \tag{3.4}
\]

#### Proof

The four atoms would be

\[
 (p_0,q_0,o_0),\ (p_1,q_0,o_1),\
 (p_1,q_1,o_0),\ (p_0,q_1,o_1).                              \tag{3.5}
\]

Every one of the four rank-`m` roots `p_0,p_1,q_0,q_1` is contained in
both owners `o_0,o_1`.  If the owners are distinct, then
`|o_0 cap o_1|<=m`; hence every root in (3.5) must equal the same
rank-`m` intersection.  Its union with another root has rank `m`, contrary
to (3.4).  If the owners are equal, the owner shore is not exact.  Both
cases are impossible.  `square`

Thus the generic witness blocks a black-box three-matroid rounding theorem,
but it is not a Boolean no-go.  Literal Boolean geometry removes this first
obstruction.  It does not remove clean strong pentagons, so an all-rank
positive proof still needs Boolean-specific correlation or absorption.

## 4. Two exact tractable subclasses

The functional-attachment theorem is the first subclass.  If a bijection

\[
                         \theta:Q\longrightarrow O            \tag{4.1}
\]

is fixed and only columns with `o(a)=theta(q(a))` remain, the head and owner
partition rows coincide.  The problem is the ordinary predecessor matching
on `P,Q`; Hall is necessary and sufficient.

There is a second, slightly less rigid product subclass.

### Theorem 4.1 (head-separable two-Hall theorem)

Suppose the retained turn support has the exact product form

\[
 {\cal H}=\{(p,q,o):pq\in E(G),\ qo\in E(J)\},               \tag{4.2}
\]

where `G` is bipartite on `P,Q` and `J` is bipartite on `Q,O`.
Then `H` has a perfect turn matching if and only if both `G` and `J` have
perfect matchings.

More generally, let `T_0` be a matching of prescribed turn triples.  Delete
their used vertices from all three shores.  A perfect turn matching
containing `T_0` exists if and only if the two residual graphs `G'` and
`J'` have perfect matchings.

#### Proof

Projecting a perfect turn matching to `P-Q` and `Q-O` gives perfect
matchings in `G` and `J`, proving necessity.  Conversely choose perfect
matchings `M_G` and `M_J`.  At each `q`, let `p(q)q` be its edge in `M_G`
and `qo(q)` its edge in `M_J`.  By (4.2),

\[
                           (p(q),q,o(q))\in{\cal H}.          \tag{4.3}
\]

These triples use every vertex in every shore exactly once.  The protected
statement is the same proof after deleting the resources of `T_0`.
`square`

In attachment language, (4.2) says that the legal predecessor set of a
column depends only on its head:

\[
                            P_F(q,o)=P_F(q).                    \tag{4.4}
\]

This is stronger than rail balance and statewise Hall, but weaker than
fixing one owner at each head.  It is a concrete prospective invariant for
a robust-order atlas: expose an owner-independent predecessor bank at every
unprotected head, then solve two ordinary Hall systems.  Any bounded bank
of prepared turns is harmless provided the two residual Hall systems pass.

An owner-separable analogue holds when

\[
 {\cal H}=\{(p,q,o):po\in E(G_1),\ qo\in E(G_2)\};           \tag{4.5}
\]

choose perfect matchings from tails and heads into the common owner shore
and compose them through each owner.

Neither separability is automatic for literal flags.  The incoming owner
specifies the oldest exchanged coordinate and can change the predecessor
list.  The theorem is therefore a useful sufficient construction target,
not a restatement of the open problem.

### Proposition 4.2 (exact local absorber/Markov language)

Fix a successful uncoloured core-flow assignment.  At one rail/core node
`v=(w,A)`, let `Z_v,P_v` be the two equal label sets from (1.7).  If
`sigma` and `tau` are two legal local derangements, their symmetric
difference is a disjoint union of alternating even cycles in

\[
                    K_{Z_v,P_v}-\{z\beta:z=\beta\}.           \tag{4.6}
\]

Toggling one cycle

\[
 z_1\beta_1z_2\beta_2\cdots z_t\beta_tz_1                 \tag{4.7}
\]

changes the owner-count vector by

\[
 \Delta_v=
 \sum_{i=1}^t
   \left(
    e_{w\cup A\cup\{z_{i+1},\beta_i\}}
    -e_{w\cup A\cup\{z_i,\beta_i\}}
   \right),
 \qquad z_{t+1}=z_1.                                       \tag{4.8}
\]

Conversely every change between two legal local matchings is a sum of
vertex-disjoint moves (4.8).

#### Proof

The union of two perfect matchings in a bipartite graph is a disjoint union
of doubled common edges and alternating even cycles.  Delete the doubled
edges and toggle any remaining cycle.  Every toggled edge belongs to (4.6),
so the result remains a legal derangement.  The old edge at `beta_i` has
tail label `z_i`; the new edge has tail label `z_(i+1)`.  Substituting the
owner formula (1.9) gives (4.8).  Toggling all symmetric-difference cycles
turns `sigma` into `tau`.  `square`

For `t=2`, (4.8) is exactly a Johnson-square/Pluecker switch.  Longer
chordless cycles are the necessary moves when a diagonal deletion removes
the relevant square.  Thus a cubic/Pluecker absorber programme has a
complete local move language after the core flow is fixed.  Its remaining
global theorem is not move generation: it is selecting these signed
circuits so that every owner coordinate becomes one without creating a
new collision elsewhere.

## 5. Exact analytic solution at `(k,m,d)=(5,2,2)`

A depth-two flag on a two-set `{a,b}` deletes one endpoint.  Orient the edge
from the deleted endpoint to the retained endpoint.  Hence a complete flag
table is exactly a tournament `T` on five coordinates.

A legal turn is a directed two-edge path

\[
                            a\longrightarrow b\longrightarrow c,          \tag{5.1}
\]

and its owner colour is the triple `{a,b,c}`.  At coordinate `b`, the legal
state block is the complete bipartite graph

\[
       K_{\deg^-(b),\deg^+(b)}                                \tag{5.2}
\]

between the directed edges entering and leaving `b`.

### Lemma 5.1 (statewise Hall forces the regular tournament)

The flag table admits a fractional, or integral, root cycle cover only if

\[
                       \deg^-(b)=\deg^+(b)=2\qquad(b\in[5]). \tag{5.3}
\]

Conversely (5.3) makes the five state blocks copies of `K_(2,2)`.

#### Proof

A cycle cover uses every directed root edge once as an incoming tail and
once as an outgoing head.  In the block (5.2), equality of the two shore
loads is necessary even fractionally.  Since their sum is four, both are
two.  Conversely `K_(2,2)` has a perfect matching.  `square`

There is one regular tournament on five vertices up to relabelling.  Label
its vertices by `Z_5` and orient

\[
                    i\longrightarrow i+1,\ i+2.               \tag{5.4}
\]

At the block centred at `b`, order the in-neighbours as `b-1,b-2` and the
out-neighbours as `b+1,b+2`.  Every fractional perfect matching of this
`K_(2,2)` is

\[
 \begin{pmatrix}x_b&1-x_b\\1-x_b&x_b\end{pmatrix},
                              \qquad0\le x_b\le1.              \tag{5.5}
\]

### Theorem 5.2 (fractional owner exactness forces the integral diagonal)

Every fractional root/head/owner-perfect turn matching for a depth-two
flag table on five coordinates is integral.  More precisely, after the
regular labelling (5.4), the owner equations force

\[
                                x_b=1\qquad(b\in\mathbb Z_5). \tag{5.6}
\]

The resulting five diagonal state matchings use every rank-three owner
exactly once.

#### Proof

For each `b`, the triple

\[
                          A_b=\{b-1,b,b+1\}                    \tag{5.7}
\]

is transitive in the tournament.  Its unique directed two-edge path is

\[
                          b-1\longrightarrow b\longrightarrow b+1.       \tag{5.8}
\]

Consequently the total fractional load of owner `A_b` is exactly the
upper-left diagonal entry `x_b` in (5.5).  Owner exactness requires that
load to be one, proving (5.6).

The other selected diagonal turn at `b` has owner

\[
                          B_b=\{b-2,b,b+2\}.                    \tag{5.9}
\]

The five `A_b` are the five transitive triples, and the five `B_b` are the
five cyclic triples: their complements are respectively the five adjacent
pairs and the five distance-two pairs of `Z_5`.  Both families are
pairwise distinct.  Thus the forced diagonal selection uses all ten owners
once.  `square`

### Corollary 5.3 (analytic explanation of the complete census)

There are exactly

\[
                              {5!\over5}=24                    \tag{5.10}
\]

labelled regular tournaments on five vertices.  These are exactly the `24`
fractionally feasible flag tables in the complete `2^10` census, and all
are integrally feasible.  Hence the first literal common-turn face has no
fractional--integral gap.

The exact singleton marking is not an extra obstruction here: every
coordinate is the retained endpoint of two oriented roots, so one may mark
one of those occurrences.  Connectivity, later upper rows, and a terminal
compiler are outside this calibration.

The independent exhaustive audit agrees with the proof:

```text
all rooted flag tables          1024
singleton-supporting tables      704
fractionally feasible             24
integrally feasible               24
```

```text
scratch/search_d2_flag_fractional_integral_gap_exact_20260801.cpp
SHA256 3db240cbd10cfcba48ae12eed143d4443e542b7d1a05101d66e51b6ac9e1c063

scratch/d2_flag_fractional_integral_gap_20260801.audit.txt
SHA256 ae3339e2e2a06e59190be33d2e2bab8c93a05d3c7cb8f57ec7348eca8bffc8e7
```

The audit is corroboration; Theorem 5.2 gives the exact explanation.

## 6. Consequence for protected SCD/pull-clock rounding

The high-rank SCD selector is a layered matching/chain-flow construction.
Each adjacent-rank layer is integral, and their union is automatically a
chain forest.  That fact does not extend through chronology: after the
flags are frozen, Theorem 1.1 already leaves three matroids.  Thus adding
more layers to the SCD flow cannot by itself prove common integrality.

Likewise, the stationary pull clock gives a fractional correlated trace
circulation, but a fractional point in (1.6) has no generic bounded-defect
rounding by Proposition 3.1 and its disjoint unions.  The fact that the
minimum generic obstruction is non-Boolean is encouraging, but only a
Boolean-specific theorem can exploit it.

For `O(1)` prepared roots fixed to one robust order, the exact proof-safe
interfaces are now:

1. quarantine their marked suffixes by the protected SCD theorem;
2. prescribe resource-disjoint protected turns, not merely root flags;
3. expose either a functional attachment or a head/owner-separable residual
   support; and
4. check the corresponding residual Hall systems after deleting the
   prepared resources.

Without Step 3, the residual problem remains three-matroid intersection.
Fractional feasibility does not imply exactness or `O(1)` defect.

The remaining one-copy theorem may therefore be stated sharply:

> **Boolean common-rounding gate.**  Jointly choose the protected exact
> marked-chain flags and a positive literal turn support so that either
> (a) one owner/head relation becomes functional, (b) the support is
> head/owner-separable, or (c) every nonbalanced block admits a globally
> resource-disjoint portal/absorber system whose residual three-matroid
> intersection is integral.

This theorem concerns only exact lower flags and owner-exact cycle-cover
chronology.  Connectedness, voltage, residence, the arbitrary upper deck,
and the terminal compiler remain later independent rows.
