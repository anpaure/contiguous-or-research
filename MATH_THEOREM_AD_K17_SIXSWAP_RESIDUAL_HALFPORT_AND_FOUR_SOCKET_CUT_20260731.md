# K17 six-swap bank: exact residual halfports, a four-socket cut, and the common-cap interface

Date: 2026-07-31  
Lane: AD, odd-diamond nonflat braid  
Status: solver-free source-relative theorem and independently replayed finite
ledger; four compensated marked joins, residual connected `b`-flow, the
staircase, upper service, and the common cap remain open

## 0. Result and scope

The six occurrence swaps in

```text
scratch/k17_sixswap_macro_forest_20260731.flow.json
```

repair the whole-component residence failure.  The rebuilt macro forest has

```text
macro edges                                      1430
macro-forest components                          5005
marked components                                 106
marked closure macros                             154
marked owner tokens                              3815
strict marked-bank D2 runs below 3                   0
strict marked-bank D3 runs below 4                   0.
```

This does **not** make the marked path automatic.  Form every oriented
one-pure-`U` connector between two marked components and retain it only when
the complete 17-coordinate literal join creates no D2 or D3 residence debt.
There are 312 such oriented arcs, using 140 distinct pure-owner labels.  Their
component projection has five weak components of sizes

\[
                             99,2,2,2,1.                 \tag{0.1}
\]

Consequently every residence-clean Hamilton path on the 106 marked
components needs at least

\[
                                \boxed 4                 \tag{0.2}
\]

marked adjacencies outside this clean one-`U` catalogue.  A single packet may
realize more than one such adjacency, so (0.2) is a socket-**unit** floor,
not necessarily a four-packet floor.  The exceptional adjacencies may be
facet collars, longer nonflat sockets, or positive-debt pure-`U` joins with
literal compensation.

There is also an independent tail/head Hall witness.  After forgetting
orientation consistency and owner-label collisions, the projected bipartite
graph has matching number 103.  The exact deficient row is

\[
 S=\{48,54,74,76,79,92,97\},\qquad
 N(S)=\{16,32,53,85\}.                                \tag{0.3}
\]

Thus \(|S|-|N(S)|=3\).  A Hamilton path would give a matching of size 105,
so even this relaxation needs at least two new adjacencies.  The weak-
component argument (0.2) is stronger.

Conditional on finding a literal 105-connector marked path, the residual
resource ledger is exact and has no scalar deficit:

```text
unused pure-U owners                               4900
residual halfports                                 9800
residual port-demand profile             0^651 1^1768 2^4016
contracted forest components                       4900
complement components                              4899.
```

The residual completion is one cycle, with marked and complementary banks
contiguous, exactly when the pair-column degree equations and all contracted
component cuts in Theorem 4.1 below hold.  This is owner/lower-palette
closure only.  One common cap is a separate global target--cell condition;
it cannot be inferred from (0.1), the balanced halfport count, or ordinary
Hall.

Conditionally, if this factor is arranged in the proved two-bank `D2`
normal form, its (a=3920) owner tokens have scalar short-cell slack
(7401-a=3481).  Thus the repaired bank is on the feasible side of that
scalar inequality.  The literal `D2` row, envelope and common cap are not
thereby constructed.

## 1. Repaired port forest and marked connector language

Put

\[
 {cal T}=\binom{[15]}8,\qquad {cal U}=\binom{[15]}9.
\]

The repaired macro graph (F_0) is a linear forest on ({\cal T}).  Every
macro edge expands to one literal `A/X/Y` owner path.  Its degree profile on
all 6,435 port colours is

\[
            \deg_{F_0}:\qquad 0^{4016}1^{1978}2^{441}.      \tag{1.1}
\]

Hence its halfport demand is

\[
 \sum_{t\in{\cal T}}(2-\deg_{F_0}(t))
 =2\cdot4016+1978=10010=2|{\cal U}|.                \tag{1.2}
\]

Exactly 106 components meet the 108 forced nonflat macros.  Their closure
has 154 macros and 3,815 literal owners and is internally resident in both
relevant rows.

For an orientation (C^\epsilon) of a marked component, write

\[
 h(C^\epsilon),\ t(C^\epsilon)\in{\cal T}
\]

for its entry and exit ports and (W(C^\epsilon)) for its owner word.  A
**clean one-`U` arc**

\[
 C^\epsilon\xrightarrow{u}D^\delta                 \tag{1.3}
\]

exists when

\[
 u=t(C^\epsilon)\cup h(D^\delta),\quad |u|=9,       \tag{1.4}
\]

and the word

\[
 W(C^\epsilon),u,W(D^\delta)                        \tag{1.5}
\]

has no newly created strict D2 run below three and its adjacent-OR
derivative has no newly created strict D3 run below four.  Condition (1.4)
is exactly physical rank-eight incidence on both sides, not merely owner-
trace compatibility.

## 2. The four-socket cut

### Theorem 2.1 (clean-graph component floor)

In the authenticated repaired forest, the undirected projection of all
clean one-`U` arcs has five components, of sizes (99,2,2,2,1).  Therefore
every marked Hamilton path contains at least four consecutive-component
adjacencies outside the clean one-`U` catalogue.

#### Proof

The audit reconstructs both orientations of all 106 marked component words,
tests all endpoint pairs by (1.4)--(1.5), and obtains 312 directed arcs.
Ignoring orientation and direction cannot delete an available clean join,
so its five weak components are a relaxation of every clean marked path.

A linear path meeting all five weak components needs at least four edges
between distinct weak components.  None of those edges is in the clean
catalogue by definition.  Every added adjacency can reduce the number of
weak components by at most one, proving the lower bound. \(\square\)

The four small components, in local marked-component numbering, are

\[
 \{48\},\quad\{8,67\},\quad\{61,89\},\quad\{77,78\};       \tag{2.1}
\]

their global repaired-forest component IDs are respectively

\[
 \{1269\},\quad\{247,2107\},\quad
 \{1856,2820\},\quad\{2435,2440\}.                  \tag{2.2}
\]

The singleton component 48 has no clean incoming or outgoing arc in either
orientation.  The audit JSON records every endpoint port of (2.1).
This is the physical singleton with ports `(16638,22835)` and macro `[18]`;
another independently rebuilt component ordering calls it component 6 (and
the endpoint-gate audit calls it 77).  The masks, not the local index, are
the invariant identifier.

### Theorem 2.2 (projected Hall obstruction)

Let (B) be the bipartite graph with a tail copy and a head copy of each
marked component, and put (C_LC_R\in E(B)) when some clean oriented arc
goes from (C) to (D).  Then

\[
                         \nu(B)=103.                  \tag{2.3}
\]

Moreover (0.3) is a Hall witness of deficiency three.

#### Proof

The deterministic augmenting-path replay finds a matching of size 103.
Alternating reachability from its three unmatched left vertices returns
exactly the sets in (0.3); direct adjacency replay gives the displayed
neighbourhood.  Hence Hall gives the matching upper bound (106-3=103),
so the matching is maximum.

The 105 directed adjacencies of a Hamilton path use every component at most
once as tail and at most once as head, and hence form a size-105 matching in
this projection.  Equation (2.3) excludes such a clean path. \(\square\)

This proof deliberately ignores orientation consistency, repeated pure-
owner labels, common-cap guards and residual flow.  It is therefore a valid
early no-go, not an artefact of a stronger downstream model.

## 3. Exact conditional residual slot ledger

Suppose four or more compensated socket units enlarge the connector
catalogue and a literal marked Hamilton path (P) is found.  Require:

1. its 105 connectors use distinct members of ({\cal U});
2. every connector consumes the two exposed degree-one halfports of its
   consecutive components;
3. all expanded joins are D2/D3 resident; and
4. all incidence changes made by a nonstandard socket are included in the
   degree ledger rather than charged as free cuts.

For the ordinary endpoint-incidence case, installing (P) uses 210 of the
1,978 unit-demand ports.  It joins 106 old forest components by an acyclic
105-edge path.  Therefore

\[
\begin{aligned}
 |{\cal U}_{\rm res}|&=5005-105=4900,\\
 c(F_0\cup P)&=5005-105=4900,\\
 d_P(t)&=2-\deg_{F_0\cup P}(t),\\
 \#\{t:d_P(t)=0,1,2\}&=(651,1768,4016),\\
 \sum_t d_P(t)&=1768+2\cdot4016=9800
              =2|{\cal U}_{\rm res}|.               \tag{3.1}
\end{aligned}
\]

The marked bank itself has

\[
                         3815+105=3920               \tag{3.2}
\]

owner tokens.  The counts (3.1)--(3.2) are independent of the marked path
order.  If a compensated socket changes the endpoint incidence multiset,
then (3.1) must be recomputed from its signed port delta.  Its necessary
scalar conditions are

\[
           0\le d_P(t)\le2,\qquad
           \sum_t d_P(t)=2|{\cal U}_{\rm res}|.       \tag{3.3}
\]

They are not sufficient Hall conditions.

### Corollary 3.1 (one optional unmarked-component bridge)

Suppose the isolated physical singleton is routed through one formerly
unmarked macro component (R), and the augmented marked path therefore has
107 macro components.  Any Hamilton path on this augmented bank uses 106
distinct pure owners and 212 endpoint halfports.  If all four bridge
incidences and all remaining marked joins use distinct degree-one endpoint
halfports, then the exact residual ledger becomes

\[
\begin{aligned}
 |{\cal U}_{\rm res}|&=5005-106=4899,\\
 c(F_0\cup P)&=5005-106=4899,\\
 \#\{t:d_P(t)=0,1,2\}&=(653,1766,4016),\\
 \sum_t d_P(t)&=1766+2\cdot4016=9798=2\cdot4899.     \tag{3.4}
\end{aligned}
\]

If (R) contains (r_R) literal `A/X/Y` owner tokens, the marked owner
phase has exactly

\[
                         3815+r_R+106=3921+r_R        \tag{3.5}
\]

tokens.  Thus adding the optional component is again component/owner/
halfport neutral: relative to (3.1), one macro component and one pure owner
move from the residual bank into the marked bank.

In the exact two-bank `D2` short-cell ledger, this augmented owner count has
scalar slack

\[
                   7401-(3921+r_R)=3480-r_R.          \tag{3.6}
\]

Hence (r_R\le3480) is the exact scalar condition for this optional-
component move inside that normal form.  It is only a count condition; the
row inversion/envelope and common-cap equations remain separate.

There is no aggregate pure-owner or port deficit in (3.4).  This does not
prove conditioned Hall.  The two bridge labels must be distinct from one
another and from the other 104 marked connector labels; after all 106 are
fixed, equations (4.5)--(4.6) must be checked with exactly those labels and
ports removed.  In particular, an unused owner whose nine facets all have
zero residual demand would be an immediate singleton owner cut, while a
larger failed set gives the corresponding Benders min-cut.  No such
conditioned claim is possible from the optional component count alone.

## 4. Exact residual pair-column and connectivity criterion

Fix a literal marked path (P), including every compensated socket
incidence.  Split occurrence-labelled halfports when two units have the
same colour.  For each unused (u\in{\cal U}_{\rm res}), let

\[
 {\cal A}_u(P)=
 \{\{h,h'\}:h\ne h',\ \tau(h),\tau(h')\subset u\}      \tag{4.1}
\]

after deleting any pair forbidden by a declared local residence, provider,
or fixed-cap guard.  Let (gamma(h)) be the component of (F_0\cup P)
containing the halfport.

Introduce (z_{u,a}\in\{0,1\}) for (a\in{\cal A}_u(P)).

### Theorem 4.1 (residual connected `b`-flow, iff)

The marked path extends to a literal connected owner/lower-`q1` factor
using precisely the allowed columns if and only if

\[
 \sum_{a\in{\cal A}_u(P)}z_{u,a}=1
       \qquad(u\in{\cal U}_{\rm res}),                       \tag{4.2}
\]

\[
 \sum_{u,a\ni h}z_{u,a}=1
       \qquad(h\in H_P),                                      \tag{4.3}
\]

and, for every nonempty proper union (X) of components of (F_0\cup P),

\[
 \sum_{u,a:\,|\gamma(a)\cap\{X,X^c\}|=2}z_{u,a}\ge2.       \tag{4.4}
\]

Here the notation in (4.4) means that the two halfports of (a) lie on
opposite sides of the cut.  Equivalently one may write the sum over
(delta(X)).

#### Proof

Equation (4.2) uses every remaining owner exactly once, and (4.3) consumes
every residual halfport exactly once.  Thus after contracting each fixed
forest component, every vertex has degree two.  A finite two-regular
multigraph is connected exactly when every nontrivial component cut is
crossed.  Its cut sizes are even, so the exact positive cut condition is
(4.4).  Expanding every selected column gives the literal factor.

Conversely, a connected literal completion chooses one pair for each
remaining owner, consumes each halfport once, and crosses every nontrivial
cut at least twice.  It therefore satisfies (4.2)--(4.4). \(\square\)

If pair-specific guards are Cartesian, degree feasibility alone is the
integral source--owner--port--sink flow.  Its exact Hall form is

\[
 2|A|\le
 \sum_{t\in{\cal T}}
 \min\bigl(d_P(t),|N(t)\cap A|\bigr)
 \qquad(A\subseteq{\cal U}_{\rm res}).                \tag{4.5}
\]

Equivalently, for every (Q\subseteq{\cal T}),

\[
 \sum_{t\in Q}d_P(t)\le
 \sum_{u\in{\cal U}_{\rm res}}
 \min\bigl(2,|\{t\in Q:t\subset u\}|\bigr).          \tag{4.6}
\]

Equations (4.5)--(4.6) do not imply (4.4), and pair-specific guards need not
be Cartesian.

### Corollary 4.2 (two-bank contiguity)

When (4.2)--(4.4) hold, contract the marked path to one supervertex.  The
resulting connected degree-two quotient is one cycle.  Its marked
supervertex has exactly two incidences to the 4,899 complementary
components; deleting either one opens the cycle into a linear chronology
with the marked bank and the complementary bank each contiguous and exactly
one surviving bank interface.

This is the precise topology promised by the two-bank route.  Degree Hall
without (4.4) may leave several cycles and does not imply the corollary.

## 5. The exact D2 common-cap boundary state

In the intended two-bank normal form the physical word has length
\(L=W+3\) and its second derivative is a row

\[
                       Z=(Z_0,\ldots,Z_W).             \tag{5.0a}
\]

The exact D2 inversion envelope is

\[
 E_p=\bigcap_{i:\,p\in[i,i+2]}Z_i.                   \tag{5.0b}
\]

It gives a nonempty word with \(D^2E=Z\) exactly when every \(E_p\) is
nonempty and

\[
                    E_i\cup E_{i+1}\cup E_{i+2}=Z_i. \tag{5.0c}
\]

The two-bank zipper has the crucial short-cell property: every lower target
not already present as a direct rank-eight row of \(Z\) must use a singleton
or adjacent-pair physical cell.  Indeed, a length-three cell equals one
\(Z_i\), while every longer cell contains two adjacent \(Z\)-rows and has
rank at least nine.  Consequently, at a physical cut between positions
\(c-1\) and \(c\), the only residual cell crossing the cut is
\([c-1,c]\).

Suppose internal target--cell assignments have been chosen on the two banks,
and let their partial maximal caps near the cut be

\[
       A^-_{c-2},A^-_{c-1};\qquad A^+_c,A^+_{c+1}.    \tag{5.0d}
\]

The crossing state is one symbol

\[
 \xi_c=\bot\quad\hbox{or}\quad \xi_c=S,              \tag{5.0e}
\]

where \(\bot\) means that \([c-1,c]\) is unused and \(S\) is the unique
lower target assigned to it.  Put \(S=[17]\) when \(\xi_c=\bot\), and set

\[
 \widehat A_{c-1}=A^-_{c-1}\cap S,\qquad
 \widehat A_c=A^+_c\cap S.                            \tag{5.0f}
\]

### Proposition 5.1 (rank-three boundary composition, iff)

The two internal common-cap assignments and the crossing choice compose to
one common-cap word if and only if:

1. the crossing target and cell are unused internally and individually
   feasible;
2. both sets in (5.0f) are nonempty;
3. the only two D2 equations meeting both banks hold,
   \[
   A^-_{c-2}\cup\widehat A_{c-1}\cup\widehat A_c=Z_{c-2},
   \qquad
   \widehat A_{c-1}\cup\widehat A_c\cup A^+_{c+1}=Z_{c-1}; \tag{5.0g}
   \]
4. if \(\xi_c=S\ne\bot\), then
   \[
                     \widehat A_{c-1}\cup\widehat A_c=S. \tag{5.0h}
   \]

All internal middle, lower and protected-prepin equations remain part of the
two bank states.

#### Proof

Every singleton or pair cell lies wholly in one bank except the unique pair
\([c-1,c]\).  Thus (5.0e) is the complete crossing target--cell assignment,
and it changes only the two caps in (5.0f).  Every three-window lies wholly
in one bank except the windows starting at \(c-2\) and \(c-1\), giving
exactly (5.0g).  Equation (5.0h) is the sole crossing lower-target equation.
Nonemptiness and the internal equations are precisely the maximal-common-cap
equivalence.  Choosing the resulting maximal caps gives sufficiency; any
realizing word gives the same conditions by maximalization. \(\square\)

Hence the smallest direct Markov interface proved for this D2 normal form is
the four-letter halo (5.0d) plus the optional crossing-target label (5.0e).
The two port colours, run signature, or scalar slack alone are insufficient.

Globally, every position belongs to at most three residual cells (its
singleton and two adjacent pairs), and every D2 row has three hosts.  Thus
the complete common-cap obstruction clutter has rank at most three; bad
pairs and triples give an exact terminal formulation.  Rank three is sharp:
at one position with envelope \(\{1,2,3\}\), the three labels
\(\{2,3\},\{1,3\},\{1,2\}\) are pairwise compatible but jointly empty.

### 5.1 General-schedule formulation

For a schedule not separately reduced to the D2 short-cell atlas, the
following full crossing relation is the lossless fallback.

Theorems 2.1--4.1 concern owners and the lower-`q1` palette.  They do not
construct depth-zero letters.  Fix a final linear chronology, a
chain-aligned schedule (I_i), positional caps (Gamma_p), and an
injective lower-target assignment (M) to the complete physical lower-cell
atlas.  Its maximal common cap is

\[
 A_p(M)=\Gamma_p\cap
        \bigcap_{S:\,p\in M(S)}S.                    \tag{5.1}
\]

At the unique marked/complement bank cut (c), define the crossing state

\[
 \Xi_c(M)=
 \{(S,[a,b]):M(S)=[a,b],\ a<c\le b\}.                \tag{5.2}
\]

Together with the two internal assignments, (Xi_c(M)) is a lossless
composition state: for every position, the targets intersected in (5.1)
are exactly the internal targets covering that position plus the crossing
rows of (5.2) covering it.  Thus the global maximal cap and all middle,
protected, and selected-lower positive-supply equations can be reconstructed
exactly.

### Proposition 5.2 (general common-cap composition criterion)

For fixed chronology, schedule and caps, two bank assignments compose to
one common-cap word if and only if there is an injective crossing state
(Xi_c) such that the reconstructed (A(M)) is nonempty at every position
and satisfies

\[
 \bigcup_{p\in I_i}A_p(M)=T_i                         \tag{5.3}
\]

for every middle row and

\[
 \bigcup_{p\in M(S)}A_p(M)=S                         \tag{5.4}
\]

for every internal or crossing lower target, including protected pins.

#### Proof

Necessity follows from any realizing word by taking its witnessing
target--cell injection.  Formula (5.1) is coordinatewise maximal among all
words subordinate to the middle caps and the selected target cells.  The
partition into left-internal, right-internal and crossing cells is exact,
so (5.2) reconstructs (5.1).  Nonemptiness and (5.3)--(5.4) are therefore
the maximal-common-cap equivalence, and are sufficient by choosing the word
(A(M)). \(\square\)

The crossing state cannot in general be replaced by the two port colours,
the capped run signature, or a scalar cell count.  Lower witness intervals
may cross the bank cut with arbitrary span, and their labels cap every
position they cover.  The standard three-position fixture

\[
 \Gamma_0=\{a\},\quad\Gamma_1=\{b,c\},\quad
 \Gamma_2=\{d\},
\]

with crossing targets ({a,c}) on ([0,1]) and ({b,d}) on
([1,2]) has perfect marginal target--cell matching but makes the cap at
position 1 empty.  Endpoint and scalar ledgers do not see this failure.

Consequently the smallest **proved lossless** interface for a general
schedule is the exact crossing target--cell relation (5.2), or an
independently justified guarded subrelation which implies (5.3)--(5.4).
The D2 normal form above is the special case in which that relation has at
most the one adjacent-pair row (5.0e).

## 6. Proved boundary

The six swaps close the old internal residence obstruction.  They do not
close marked-path routing: four compensated adjacency units are still
necessary by Theorem 2.1.  If those units produce a literal 105-connector
path, the residual halfport ledger is perfectly balanced and Theorem 4.1 is
an exact completion test.  Balance is not a proof of its Hall or connectivity
rows.

There is likewise no scalar halfport obstruction and no reinstated
`107`-boundary tax.  Inside the conditional two-bank `D2` normal form the
base marked bank has exact positive scalar slack 3,481, while one optional
component has slack (3480-r_R).  No literal optimal-length `D2` row has
yet been constructed for this repaired carrier, so the condition is a
passed count row, not a passed schedule/envelope row.  Even a scalar-feasible
row would not imply Proposition 5.1.  Upper and deeper shadows remain
separate terminal rows.

## 7. Reproducibility

The lightweight audit is

```text
python3 scratch/audit_ad_k17_sixswap_residual_halfport_four_socket_20260731.py
python3 -m py_compile scratch/audit_ad_k17_sixswap_residual_halfport_four_socket_20260731.py
```

It performs no SAT, CP-SAT, exhaustive long search, or network solve.  It
replays all 312 local clean arcs, the weak components, the 106-by-106
bipartite matching and its Hall witness, and the exact port-demand counts.

```text
scratch/audit_ad_k17_sixswap_residual_halfport_four_socket_20260731.py
scratch/ad_k17_sixswap_residual_halfport_four_socket_20260731.audit.json
```

No `K17` word, improved numerical bound, residual `b`-flow, upper-complete
carrier, staircase, or common-cap compiler is claimed.
