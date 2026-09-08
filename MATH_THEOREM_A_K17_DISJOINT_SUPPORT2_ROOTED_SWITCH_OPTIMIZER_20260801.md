# `k=17`: exact disjoint support-two rooted-switch optimizer

Date: 2026-08-01  
Lane: A / rooted age-partition repair  
Status: unconditional finite formulation relative to any declared literal
flag menu, with complete support-two catalogues and independently replayed
finite incumbents; no upper constraints and no global feasibility verdict

## 0. Verdict

Fix an incumbent lower-palette-perfect rooted flag factor.  Every
palette-preserving move supported on at most two roots is exactly one of:

1. a unary replacement whose resource difference is zero; or
2. two replacements on distinct roots whose nonzero resource differences
   are opposite.

Therefore every root-disjoint family of such moves is a matching in a
labelled multigraph on the roots, with unary moves represented by private
leaf edges.  Conversely every such matching gives a literal
palette-perfect factor.  The option-only convex hull is the ordinary
general-graph matching polytope, including its odd-set inequalities.

The chronology objective is not additive over these options.  Its exact
linearization first reconstructs one final flag at every root and then
activates compatibility columns indexed by the complete ordered pair of
final endpoint flags.  This handles transitions whose two endpoints lie
in one support-two move, in two different selected moves, or in no move.
Legal quotient loops are retained.

The declared finite optimization first maximizes the exact packet-support
matching, then minimizes the exact numbers of zero-out and zero-in roots.
The next layer chooses one aligned owner state at every root and owner and
a perfect split-state transition matching.  A maximum-matching residual
cut is the exact Hall/Benders separator.  Thus even a packet-perfect root
graph can still have a genuinely nonlocal selected-state Hall obstruction.

Everything below concerns only lower palettes, literal depth-three
chronology, and the two incidence matchings.  It imposes no upper row,
subtour, voltage, opening, or compiler condition.

## 1. Resource differences and the complete option catalogue

Let \(V\) be the 1,430 rank-eight roots.  At \(q\in V\), let \(f_q^0\)
be the incumbent flag.  For a literal candidate flag \(f\) on \(q\), let

\[
 r(f)=e_q+e_{\operatorname{type}(f)}
      +e_{(|B(f)|,[B(f)])}
      +{\bf1}_{|A(f)|\ge2}e_{(|A(f)|,[A(f)])},       \tag{1.1}
\]

where \(A=C_0\) and \(B=C_0\cup C_1\).  Rank-one suffixes are slack and
have no resource coordinate.  Put

\[
                    \partial_q(f)=r(f)-r(f_q^0).     \tag{1.2}
\]

The root coordinate cancels in (1.2).  All rank-six targets use the same
resource coordinate, whether they occur as \(A\) or as \(B\).

Fix any declared finite literal menu \(\mathcal F_q\) at each root,
containing \(f_q^0\).  Taking the complete literal menu makes the result
exhaustive over all support-at-most-two moves.

### Definition 1.1 (canonical options)

A unary option is a pair

\[
                 o=(q;f),\qquad
 f\ne f_q^0,\qquad \partial_q(f)=0.                  \tag{1.3}
\]

A pair option is

\[
 o=(q,f;\,q',f'),\qquad q<q',                        \tag{1.4}
\]

where both replacements are nonincumbent and

\[
       \partial_q(f)=-\partial_{q'}(f')\ne0.         \tag{1.5}
\]

The ordering \(q<q'\) removes the orientation duplicate.  A pair with two
zero differences is omitted, because it is exactly two independent unary
options.  Identical final flags reached through distinct labelled options
remain distinct option columns.

### Theorem 1.2 (support-two iff)

A replacement supported on one or two distinct roots preserves every
root row, every type mass, and every tight lower target multiplicity if and
only if it is a unary option (1.3), a pair option (1.4)--(1.5), or the
identity.

#### Proof

For a one-root replacement, preservation is exactly
\(r(f)=r(f_q^0)\), which is (1.3).  For two roots, the total resource
change is

\[
                   \partial_q(f)+\partial_{q'}(f').
\]

It vanishes exactly under (1.5), unless both terms vanish separately, in
which case the change is the union of two unary moves.  The resource
coordinates in (1.1) are precisely all defining lower-palette and type
rows, so zero total difference is also sufficient.  \(\square\)

The catalogue is generated without SAT: bucket every nonincumbent literal
flag by \(\partial_q(f)\), output zero-bucket columns as unary options, and
join columns in opposite nonzero buckets on different roots.

## 2. Root-disjoint option master

Let \(\mathcal O\) be the option catalogue and \(S(o)\subseteq V\) its
support.  Use a binary variable \(x_o\) and impose

\[
                    \sum_{o:q\in S(o)}x_o\le1
                    \qquad(q\in V).                  \tag{2.1}
\]

The final flag at \(q\) is the replacement named by the unique selected
option incident with \(q\), or \(f_q^0\) if no option is incident.

### Theorem 2.1 (root-disjoint exactness)

The binary points of (2.1) are in bijection with all factors obtainable as
a root-disjoint family of support-at-most-two palette moves.  Every such
factor remains exactly lower-palette perfect.

#### Proof

By (2.1), different selected options have disjoint supports, so their
literal replacements compose without ambiguity.  Each option has zero
resource difference by Theorem 1.2; summing over selected options leaves
every resource row unchanged.  Conversely, decompose any declared
root-disjoint family into its unary and nonzero opposite-difference pair
moves.  These are catalogue options and satisfy (2.1).  \(\square\)

There is an exact matching interpretation.  Make an augmented multigraph
with vertex set

\[
             V\mathbin{\dot\cup}\{q^\star:q\in V\}.             \tag{2.2}
\]

Represent a pair option on \(q,q'\) by a labelled edge \(qq'\), and a
unary option at \(q\) by a labelled edge \(qq^\star\).  Then selected
root-disjoint options are exactly matchings of this multigraph.  Hence the
option-only convex hull is given by nonnegativity, the vertex-degree rows,
and Edmonds' odd-set inequalities.  Writing \(E(o)\) for the two augmented
endpoints of either kind of option, those inequalities are

\[
 \sum_{o:\,E(o)\subseteq U}x_o
 \le { |U|-1\over2}
 \qquad
 (U\subseteq V\mathbin{\dot\cup}V^\star,\ |U|\ {\rm odd}),     \tag{2.3}
\]

after unary options are viewed as their private-leaf edges.  Parallel
labelled edges cause no difficulty.  Thus option selection alone is an
integral general-graph matching problem; the degree relaxation by itself
need not be integral on an odd triangle.

## 3. Final-flag channel and exact nonadditivity

Let \(\widehat{\mathcal F}_q\) be the incumbent flag together with every
flag delivered at \(q\) by a catalogue option.  Introduce a binary
\(p_{qf}\) for \(f\in\widehat{\mathcal F}_q\).  Because options are
root-disjoint, the exact channel equations are

\[
 p_{qf_q^0}=1-\sum_{o:q\in S(o)}x_o,                 \tag{3.1}
\]

and, for \(f\ne f_q^0\),

\[
 p_{qf}=\sum_{\substack{o:q\in S(o)\\f_o(q)=f}}x_o. \tag{3.2}
\]

In particular,

\[
                    \sum_{f\in\widehat{\mathcal F}_q}p_{qf}=1.
                                                               \tag{3.3}
\]

For complete flag options \(f\) at \(q\) and \(g\) at \(q'\), retain every
literal phase-labelled state transition

\[
 a=(s,t,h,\delta),\quad
 s=(q,f,o,\sigma),\quad t=(q',g,o',\sigma').         \tag{3.4}
\]

Here \(s,t\) are complete aligned attachment states, \(h\) is the
old-root incidence, and \(\delta\) is its literal phase.  The catalogue
includes \(q=q'\), and even \(s=t\) with a nonzero physical phase change,
whenever the complete transition test admits that quotient loop.
Introduce an activation variable \(c_a\) and impose

\[
\begin{aligned}
 c_a&\le p_{qf},&
 c_a&\le p_{q'g},&
 c_a&\ge p_{qf}+p_{q'g}-1.
\end{aligned}                                                   \tag{3.5}
\]

Thus \(c_a=1\) exactly when both complete endpoint flags of that legal
transition are final.  For a self-loop with the same endpoint flag,
(3.5) reduces to \(c_a=p_{qf}\).

### Proposition 3.1 (why move deltas do not add)

The final transition catalogue cannot in general be obtained by adding
the transition deltas of the individually selected options.

#### Proof

For an aligned source state of \(f\) and target state of \(g\), literal
compatibility includes

\[
 \rho^\delta C_{i+1}(g)\subseteq C_i(f)
                 \qquad(0\le i<3).                  \tag{3.6}
\]

This is a predicate of the ordered pair \((f,g)\).  When both endpoint
rows change, (3.6) is evaluated on \((f',g')\), not on either one-sided
pair \((f',g)\) or \((f,g')\).  Hence a transition can be created only by
the joint change, or destroyed only by the joint change.  The same issue
occurs between roots belonging to two different selected pair options.
Equations (3.1)--(3.5) evaluate the complete final pair and therefore
retain exactly these cross terms.  \(\square\)

This is the essential fail-closed rule: precomputed one-move degree gains
may be used as heuristics, but never as the objective ledger of a
multi-option solution.

## 4. Exact packet matching and dead-root objectives, with loops

Let \(\mathcal E_{\rm root}\) be the ordered pairs
\((q,f;q',g)\) for which at least one complete literal transition column
in (3.4) exists.  Introduce a packet-matching variable
\(w_{q,f,q',g}\) for each such pair and impose

\[
 w_{q,f,q',g}\le p_{qf},\qquad
 w_{q,f,q',g}\le p_{q'g},                            \tag{4.1}
\]

\[
 \sum_{f,q',g}w_{q,f,q',g}\le1\quad(q\in V),\qquad
 \sum_{q,f,g}w_{q,f,q',g}\le1\quad(q'\in V).        \tag{4.2}
\]

For fixed final flags these are exactly the rows of a bipartite matching
in the packet/root transition graph.  Hence maximizing

\[
                         P=\sum w_{q,f,q',g}          \tag{4.3}
\]

gives the exact packet-support maximum matching, jointly over every
root-disjoint circuit packing.  A legal quotient loop is the ordinary
split edge from the left copy of \(q\) to its right copy and is retained.

Use binary dead indicators \(d_q^+,d_q^-\).  With the active complete
transition columns of (3.5), impose

\[
 d_q^+\ge1-\sum_{a:\operatorname{tailroot}(a)=q}c_a,
 \qquad
 d_q^-\ge1-\sum_{a:\operatorname{headroot}(a)=q}c_a. \tag{4.4}
\]

Minimization makes these the exact zero-out and zero-in indicators.
Every active quotient loop appears once in each corresponding sum and
therefore makes its root live on both sides, as it should.

The requested proof-safe objective is lexicographic optimization of

\[
 \left(
    -P,\quad
    D^+=\sum_qd_q^+,\quad
    D^-=\sum_qd_q^-,\quad
    R=\sum_o|S(o)|x_o,\quad
    M=\sum_ox_o
 \right).                                                       \tag{4.5}
\]

Changing the order of \(D^+\) and \(D^-\), or minimizing their sum first,
defines a different but still exact declared objective.  It must be
reported explicitly.

For the authenticated rooted table, every solution of the later full
owner/state transversal has the additional valid support cut

\[
                         \sum_o|S(o)|x_o\ge103.       \tag{4.6}
\]

Indeed, its owner-shore projection has 782 owner orbits with no incoming
transition, and the 102 largest changed-root incidence capacities total
only 779.  Every new transition into one of those owners touches a changed
incident root.  This is a necessary cut only; it does not assert that 103
changed roots suffice.

One may avoid the \(c_a\) variables in a compact implementation by using,
for every final flag \(f\),

\[
 d_q^+\ge
 p_{qf}-\sum_{(q',g)\in\Gamma^+(q,f)}p_{q'g},         \tag{4.7}
\]

and the analogous incoming inequality.  The neighbourhoods in (4.7)
include the root itself exactly when a legal loop exists.  Formulations
(3.5), (4.4), and (4.7) are equivalent for the dead-root objective.

## 5. Exact 1,430-state owner/root/`H` transversal

After the first objective, materialize all nine aligned owner states of
every final flag.  A state has the form

\[
                 s=(q,f,o,\sigma),                   \tag{5.1}
\]

where \(\rho^\sigma Q_q\subset T_o\), and it carries the whole rotated
four-cell partition.  Use \(z_s\in\{0,1\}\) and impose

\[
 z_s\le p_{qf},                                      \tag{5.2}
\]

\[
 \sum_{s:\operatorname{root}(s)=q}z_s=1
                 \quad(q\in V),\qquad
 \sum_{s:\operatorname{owner}(s)=o}z_s=1
                 \quad(o\in\mathcal N_9).            \tag{5.3}
\]

Retain every literal phase-labelled transition between complete states,
including legal state loops, and use a binary \(y_a\).  The exact rows are

\[
 \sum_{a:\operatorname{tail}(a)=s}y_a=z_s,\qquad
 \sum_{a:\operatorname{head}(a)=s}y_a=z_s,\qquad
 y_a\le c_a\quad(a\in\mathcal A).                    \tag{5.4}
\]

The endpoint equalities gate every selected transition automatically;
explicit inequalities \(y_a\le z_{\rm tail(a)},z_{\rm head(a)}\) are
redundant but useful defensive checks.

### Theorem 5.1 (transversal iff)

Equations (2.1), (3.1)--(3.5), and (5.2)--(5.4) are necessary and
sufficient for a lower-palette-perfect disjoint support-two repair whose
selected states form a literal depth-three quotient cycle cover, with one
incidence at every root and every owner for both \(D\) and \(H\).

#### Proof

Theorem 2.1 gives the lower-palette factor.  Equations (5.2)--(5.3) select
one aligned \(D\) incidence at every root and owner.  Equations (5.4)
select one outgoing and incoming literal transition at every selected
state, so their support is a directed cycle cover.

The outgoing transition at a root names one old-root \(H\) incidence.
There is one at every root by the first equality in (5.4).  The incoming
equality and the owner bijection in (5.3) give one such incidence at every
owner.  Hence \(H\) is perfect.  Conversely any declared repaired
transversal reads off exactly these variables.  Legal loops are ordinary
one-cycles in this equivalence.  \(\square\)

The theorem does not assert that the cycle cover is one quotient cycle or
that any lifted component has nonzero voltage.

## 6. Exact Hall/Benders separation

For fixed final flags and a fixed root/owner state transversal \(Z\), form
the split bipartite graph \(B_Z\) with a tail and head copy of each state.
A legal state loop is the ordinary split edge \(s_Ls_R\).  Define

\[
 \delta(Z)=\max_{X\subseteq Z}
            \bigl(|X|-|N^+_Z(X)|\bigr).              \tag{6.1}
\]

Then the largest transition matching has size \(1430-\delta(Z)\), and
(5.4) is feasible exactly when \(\delta(Z)=0\).

An integer Benders master may retain the option variables \(x\), final
flags \(p\), and the root/owner matching \(z\), while a bipartite
maximum-matching oracle handles (5.4).  If an incumbent returns a Hall
witness \(X\subseteq Z\), add

\[
 \sum_{t\in\Gamma^+(X)}z_t
 +|X|\sum_{s\in X}(1-z_s)\ge |X|.                   \tag{6.2}
\]

Here \(\Gamma^+(X)\) is the union of all complete state columns reachable
from \(X\) under the currently admitted support-two final-flag menu, and
contains a state itself when a legal loop supplies that neighbour.
If every state of \(X\) remains selected, (6.2) is exactly its Hall row.
If any tail in \(X\) changes, the second term deactivates this
incumbent-specific cut.  Repeated residual min-cut separation is complete.

The exact optimized deficiency of the declared support-two face is

\[
 \Delta_{\le2}^{\rm disj}
 =\min_{\substack{x\ {\rm satisfies}\ (2.1)\\
                  z\ {\rm satisfies}\ (5.2),(5.3)}}
       \max_{X\subseteq Z}
          \bigl(|X|-|N^+_{x,Z}(X)|\bigr).            \tag{6.3}
\]

A full owner/root/`H` transversal exists in this face if and only if
\(\Delta_{\le2}^{\rm disj}=0\).

The option matching polytope and each fixed-\(Z\) transition matching
polytope are separately integral.  Their correlation through final flag
pairs and Hall cuts is not thereby integral.  The exact algorithm is
therefore matching plus integer Benders, not one unqualified matching
theorem.

## 7. Quantifier and implementation audit

The complete proof-safe order is:

1. enumerate the literal flag menu and resource differences;
2. construct every unary and opposite-difference pair option;
3. choose a root-disjoint option matching;
4. reconstruct the complete final flag at every root;
5. rebuild all ordered final-flag and complete-state transitions, including
   loops;
6. maximize the exact packet matching, then optimize the dead-root vector;
7. choose the root/owner state matching and separate transition Hall cuts.

It is unsound to:

* add the root-arc gains of selected options;
* omit interactions between two roots changed by different options;
* discard loops merely because the earlier frozen catalogue had none;
* distinguish the same rank-six target according to its inner/outer role;
  or
* infer a 1,430-state transversal from zero dead roots.

This theorem is exact only for root-disjoint families of support-at-most-two
options from the declared literal menu.  Overlapping support-two circuits,
support-three or larger circuits, upper rows, connectivity, and all
compiler constraints remain outside its scope.

## 8. Complete `ad9e15...` catalogue and union calibration

For the authenticated certificate

```text
scratch/k17_rank8_rooted_static_age_flag_20260801.certificate.tsv
SHA256 ad9e15f724b5048c00cf43ae007d0e02c03c72204a5c169736461e946a166eab
```

the complete literal menu has exactly 1,904 options per root and hence
2,722,720 options.  The O3/H100 delta-bucket enumeration gives

```text
zero-delta options, incumbents included                  3,987
unary circuits                                           2,557
nonzero option records                                2,718,733
opposite nonzero delta-bucket pairs                       5,550
indecomposable support-two literal circuits             214,711
root pairs supporting such a circuit                     26,874
```

The unary circuits occur on 488 roots.  The 22 support-two circuits
changing root 0 reproduce the separately frozen local census.

As a necessary relaxation, allow each root to use every option appearing
in any unary or support-two circuit, independently of the required return
partner.  This permissive union has 54,537 options, 18,307 literal packet
edges, no zero-out or zero-in root, and packet-support matching 1,430
(legal loops included).  Thus the union gives no support-two ceiling: the
remaining obstruction, if any, is entirely the correlation imposed by
(2.1)--(3.3).

## 9. Independently replayed basins

The stronger portfolio seed

```text
scratch/threadA_k17_rooted_static_portfolio_28401_20260801/
  certificate_28401.tsv
SHA256 e973061f57d1e4c141dc42489da289a0b454d4b9fd27369d887561fdea29299e
```

has been replayed independently in O3 C++ on the H100 CPU.  It is exactly
lower/type perfect and has

```text
root turns / packet matching / zero-out / zero-in
  961 / 557 / 739 / 822
state arcs / zero-state-out / zero-state-in
  7688 / 7118 / 11963
```

with no quotient loop.  It strictly dominates the original `ad9e15...`
basin in the primary matching objective.  Catalogue counts cannot be
transported between the two certificates: every difference vector (1.2)
is incumbent-relative, so the complete shell and optimizer must be rebuilt
on this seed.  Its rebuilt shell contains 2,533 unary and 213,836
indecomposable support-two circuits.

The independently supplied shuffle seed

```text
scratch/k17_rank8_rooted_static_shuffle201_20260801.certificate.tsv
SHA256 d44b60611a3c9e4ba1533a774762fce825d327dcc7536cdcd9c10522404b1ad3
```

was separately replayed from the literal flag table.  It is also exactly
lower/type perfect and has

```text
root turns / packet matching / zero-out / zero-in
  970 / 556 / 723 / 826
state arcs / zero-state-out / zero-state-in
  7760 / 6997 / 11950
```

with no quotient loop.  Thus it starts one unit below `certificate_28401`
in the primary matching objective but in a different transition basin.  Its
complete rebuilt shell contains 2,541 unary and 213,714 indecomposable
support-two circuits.  These counts and the baseline transition statistics
were independently replayed; no catalogue was transported from another
incumbent.

## 10. Materialized root-disjoint incumbents

On `certificate_28401`, a deterministic construction sorted every circuit
by its exact one-move score

\[
 (\text{packet matching},-D^+,-D^-,\text{turns})
\]

and accepted a circuit only when it was root-disjoint from all earlier
choices and strictly improved the fully materialized current factor.  The
complete list was revisited until one full pass accepted nothing.  This is
a fixed-order greedy maximality statement, not the optimum of Sections
2--6.

The four passes, including the final empty pass, select 460 moves: 30
unary circuits and 430 support-two circuits, changing 890 roots.  Exact
static and transition replay gives

```text
                         baseline       final
packet matching             557           947
zero-out / zero-in       739 / 822     228 / 447
raw turns / root edges       961          1838
state arcs                   7688         14704
zero state out / in      7118/11963    2781/11168
```

There are no quotient loops, so loop-inclusive and nonloop packet matching
both equal 947.  An independent verifier reconstructs all type/target
loads, all phase-labelled transitions, the state arcs, and the maximum
matching from the materialized certificate.

This gives a 390-unit primary improvement over its own baseline and a
417-unit improvement over the old `ad9e15...` matching.

The same complete construction was then run on `shuffle201`.  Two
deterministic serial tie orders were retained because they expose the
nonconvex correlation rather than merely duplicating one answer.  Forward
serial order selects 454 moves on 870 roots and gives

```text
packet matching / zero-out / zero-in / turns
  951 / 228 / 444 / 1872.
```

Reverse serial order inside exact one-move score ties selects 449 moves
(42 unary and 407 support-two) on 856 roots and gives

```text
                         baseline       reverse final
packet matching             556              954
zero-out / zero-in       723 / 826        234 / 445
raw turns / root edges       970             1855
state arcs                   7760            14840
zero state out / in      6997/11950       2803/11140
```

Both factors pass independent complete resource and transition replay.
Under the declared lexicographic objective---packet matching first, then
dead roots---the reverse result is the authoritative incumbent because
`954 > 951`.  The forward result is better only for a zero-first objective.
The value 954 is not asserted to be the optimum of the exact master.

There is a second, distinct projection relevant to owner demand.  Project
the same phase-labelled state arcs onto their physical owner endpoints,
without requiring the root and owner matchings to choose the same state.
For the shuffle baseline this owner graph has

```text
edges / loops / maximum matching / zero-out / zero-in
  7694 / 1 / 722 / 3 / 708.
```

For the reverse incumbent it has

```text
edges / loops / maximum matching / zero-out / zero-in
  14643 / 0 / 1079 / 0 / 351.
```

Thus the same exact switch family improves owner-demand matching by 357,
eliminates every owner zero-out demand, and more than halves the zero-in
obstruction from 708 to 351.  This does **not** combine the packet matching 954 and the
owner matching 1079: the common 1,430-state owner/root/`H` transversal is
precisely the correlated Hall/Benders gate in Sections 4--6.

The reverse incumbent is therefore neither a full root-level carrier nor
an owner-exact carrier: 234 root zero-out, 445 root zero-in, and 351 owner
zero-in demands remain.  Since the permissive support-two union is
packet-perfect, these residuals do not prove a support-two ceiling.  The
exact unresolved gate is the correlated integer master of Sections 2--6,
or a move class allowing overlapping/iterated circuits or support at least
three.

## 11. Frozen finite artifacts

```text
scratch/audit_threadA_k17_ad9e_global_support2_delta_counts_20260801.cpp
  SHA256 c922ba37d5244fb3882a6d01aee70956069a2b8cb54b14d79a00ea4bea9bf35c

scratch/threadA_k17_global_support2_delta_counts_h100_20260801/
  global_support2_delta_counts.audit.json
  SHA256 2bab3453acb297a0fc209e536b338072e4f2711275f57ee220e2262743cf8798

scratch/audit_threadA_k17_ad9e_support2_option_union_ceiling_20260801.cpp
  SHA256 a3e555662cc6f5d407f855289c7311c779738dc8ce624f04bdb3669e4a729595

scratch/threadA_k17_rooted_static_portfolio_28401_20260801/
  certificate28401.audit.json
  SHA256 9521e7ced3778a23ef42251e6daea63727e5cdef3ecee80aca284f744bd59097

scratch/search_threadA_k17_rooted_global_support2_greedy_multipass_20260801.cpp
  SHA256 3c892952b68350c1fc0c2e1c3ae02e7f222c8b5e1d9467b864e969e87a3530fd

scratch/threadA_k17_rooted_global_support2_multipass_h100_20260801/
  cert28401_multipass.audit.json
  SHA256 641f60571e9c281d851b6448986df2a976fbb6309c146a231365ea49ca6bee31

  cert28401_multipass.candidate.tsv
  SHA256 0675b404b48b1082f2473be7da250bb428680b1004786e1e4a748d0d2df4c3a9

  cert28401_multipass.moves.tsv
  SHA256 8110e501f7cbb194aae00dc101fb5d286d549daeab9eb3ed8a5d09019bf9cde6

  greedy28401_multipass.independent.audit.json
  SHA256 3b560ed0046cab6f237762a4ca45403cc7a43f475ab3cc47ba26fbaa548157e0

scratch/search_threadA_k17_rooted_global_support2_greedy_multipass_reverse_ties_20260801.cpp
  SHA256 289151cfcda8a559f0900c03239042f6a6c53ac93a6a05066d5ecb49722abbdd

scratch/threadA_k17_rooted_global_support2_shuffle201_h100_20260801/
  shuffle201.baseline.audit.json
  SHA256 51d314f3a9f40ce8b6c1718b0a46bb041cd2bf648b30d85491a51b44d3d7902d

  shuffle201_reverse.audit.json
  SHA256 2e45e0893199ca046c8dd351a1572494ed26185e9641a50c1e83cbe90a1459b2

  shuffle201_reverse.candidate.tsv
  SHA256 e28a8ee5825564baf0d75720d8f3c1a53a911e9c53956aff49ed2460fd08c8dd

  shuffle201_reverse.moves.tsv
  SHA256 47b5017e4605d996657590a198fbf091b3090f5235cd75910f7b1e7cc4f4f7b3

  shuffle201_reverse.independent.audit.json
  SHA256 264ba804b98b96a216b9087a948f5e74c305f13f3be2d07270ccdd3d94e752a0

  reverse.owner.audit.json
  SHA256 b332ccc08662e3931d7e6afe59f945ce8e49df32f95311c7315b1b0c64b80e3d

scratch/threadA_k17_rooted_global_support2_shuffle201_h100_20260801/
  audit_threadA_k17_rooted_owner_shore_transition_support_20260801.cpp
  SHA256 f807917fef66518e6099b6e0787e747879aa84d76072754c8f21407ffdbeaaf9
```
