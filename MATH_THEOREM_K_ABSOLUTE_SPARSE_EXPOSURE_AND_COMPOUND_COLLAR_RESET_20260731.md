# Absolute sparse exposure: sharp compound-collar count and guarded reset

Date: 2026-07-31  
Lane: K, bounded-defect/common-cap compiler  
Status: sharp conditional theorem and explicit counterexamples.  The
uniform Boolean/Pascal lift supplying its hypotheses remains open.

## 0. Verdict

The proposed compound-collar argument has a valid bounded-state conclusion,
but one coefficient-four inference is false without an additional row.

Let `Phi` be the carried defect potential.  Suppose a same-parity lift has

\[
                         s\le a\Phi+s_0                         \tag{0.1}
\]

changed physical seams.  Passive two-coordinate inheritance creates at
most four named descendants of each live source.  Grouping every
`O(d)`-wide seam collar into one exact compound task gives

\[
              \boxed{H\le(4+a)\Phi+b} ,                         \tag{0.2}
\]

where `H` is the number of packet lists seen by the simultaneous selector
and `b` is absolute.  This bound is sharp when the inherited tasks, seam
tasks, and boundary tasks are disjoint.  Grouping removes the factor `d`;
it does not remove the seam task.

The stronger selector bound

\[
                         H\le4\Phi+b_0                           \tag{0.3}
\]

requires one further **absorption row**: all but `O(1)` seam collars must be
compiled inside already counted inherited/boundary packet lists.  Merely
saying that every collar is repaired exactly does not prove (0.3) at the
selection stage.  Exact closure can make the seam task disappear from the
*exported child state* after selection; that is a distinct statement.

On a bounded sublevel `Phi<=E`, either (0.2) or (0.3) makes `H` absolute.
If every whole-packet list has quadratic supply, source-fixed resources are
strongly private, and every nonfixed physical/witness/topology/cap token has
`O(m)` load in each other list, deterministic greedy selection succeeds
because `d=o(m)`.  This is a greedy theorem for a constant **number of
lists**.  It does not justify pruning each list to constant size.

There are four exact obstructions which any all-dimensional construction
must avoid.

1. Compiler Hall defect alone cannot bound seams: arbitrarily many private
   perfect components have zero Hall defect but require arbitrarily many
   joins.
2. Current-depth residence alone cannot bound seams: the odd-diamond lift
   shortens every coordinate run by one, so separated minimum-run packets
   create independent compensation tasks.
3. Distinct anchor names do not imply compatibility: fixed source tokens or
   one common cap-one vertex can couple all lists.
4. The canonical absent-key PBBS collar has only `m` safe choices for one
   active departure key and none for two distinct keys.  Its bare `m^2`
   parameterization is not a quadratic compound list.

The weakest live theorem is therefore a bounded-sublevel protected lift
with seam charging, compound-task absorption or the coefficient `(4+a)`,
key-preloaded packet supply, a fixed topology skeleton, and complete
common-guard linkage tickets.

## 1. Seam charging

Let `D(g)` be a bank of named repair tokens in a parent state `g`, with

\[
                              |D(g)|\le\Phi(g).                    \tag{1.1}
\]

The tokens must include every obstruction which can force a physical
change: compiler sources, protected-witness debt, minimum-run compensation,
and component/connector debt not already installed in the baseline.

Let `J` be the changed physical seam set and write

\[
                      J=J_{\rm str}\sqcup J_{\rm ch}.              \tag{1.2}
\]

A seam-charging certificate of width `(a,s_0)` is a map

\[
                    \chi:J_{\rm ch}\longrightarrow D(g)           \tag{1.3}
\]

such that

\[
 |J_{\rm str}|\le s_0,
 \qquad |\chi^{-1}(z)|\le a\quad(z\in D(g)).                       \tag{1.4}
\]

### Lemma 1.1 (absolute seam bound)

A seam-charging certificate gives

\[
                            |J|\le a\Phi(g)+s_0.                    \tag{1.5}
\]

#### Proof

Sum (1.4) over `D(g)` and use (1.1):

\[
 |J|\le s_0+\sum_{z\in D(g)}|\chi^{-1}(z)|
     \le s_0+a|D(g)|\le s_0+a\Phi(g).
\]

\(\square\)

This is a construction certificate, not a consequence of locality.  In
particular, a path-forest baseline must charge its uninstalled connectors,
and a flat odd-diamond lift must charge every minimum-run packet which lacks
one extra unit of parent margin.

## 2. The sharp compound-task count

Let `P` be the passive descendant task bank, `Sigma` the bank of seam
collars, and `E` the other exceptional/boundary tasks.  Assume

\[
 |P|\le4\Phi+b_p,
 \qquad |\Sigma|\le s\le a\Phi+s_0,
 \qquad |E|\le b_e.                                      \tag{2.1}
\]

One member of `Sigma` contains the complete signed old/new collar of one
seam: every residence wall, every protected shadow occurrence, every
erosion/compiler row, its boundary state, and its complete cap/topology
ticket.  There may be `Theta(d^2)` labelled rows inside the task; it is one
selection variable only when one packet certifies all of them together.

### Theorem 2.1 (sharp selector exposure)

Without further overlap information, the selector task bank `T` satisfies

\[
        |T|\le |P|+|\Sigma|+|E|
             \le(4+a)\Phi+(b_p+s_0+b_e).                         \tag{2.2}
\]

No smaller coefficient follows from (2.1).

#### Proof

The upper bound is the union bound.  For sharpness, take the three task
families pairwise disjoint and take equality in every row of (2.1).  Every
seam still contributes one compound choice even though its `O(d)` local
rows have been bundled.  Hence the coefficient `4+a` is attained.  
\(\square\)

Define a seam collar to be **absorbed** when its entire signed state and
repair choice are included in one already counted list in `P union E`.
Let `Sigma_new` be the unabsorbed seam tasks.

### Corollary 2.2 (coefficient-four absorption criterion)

If

\[
                            |\Sigma_{\rm new}|\le b_s              \tag{2.3}
\]

for an absolute `b_s`, then

\[
                         |T|\le4\Phi+b_p+b_e+b_s.                  \tag{2.4}
\]

Conversely, when the three task families carry distinct compulsory
resources, (2.4) implies that all but `O(1)` seam tasks were absorbed or
charged into the definition of `Phi`.

Exact collar repair can also give a postselection export bound.  If every
selected seam packet closes all its rows and exports no child source, then
the *carried child source bank* has size at most `4Phi+O(1)`.  This does not
alter the preselection count (2.2); it is the regenerative row needed after
the simultaneous packet choice has already been made.

## 3. Whole-packet greedy theorem

Fix one literal common guard `Q` and one prescribed topology skeleton.  For
each task `t` let `P_t` be its list of whole packets.  A packet contains its
literal physical replacement, all protected witness occurrences, its
residence and boundary certificate, and complete directed cap/linkage and
topology tickets.

Assume:

1. every packet has the typed boundary relation prescribed by the fixed
   skeleton;
2. source-fixed resources are **strongly private**: every resource fixed in
   all packets of one list is absent from every packet in every other list;
3. a packet uses at most `r_j(d)` nonfixed resources of type `j`, and one
   such resource occurs in at most `kappa_j m` packets of any one other
   list; and
4. pairwise resource-disjoint complete tickets compose literally under the
   fixed skeleton and guard.

Put

\[
                         K(d)=\sum_j\kappa_j r_j(d).                 \tag{3.1}
\]

Suppose every list has

\[
                         |P_t|\ge L:=m^2-gmd.                       \tag{3.2}
\]

### Theorem 3.1 (bounded-bank deterministic reset)

If `H=|T|` and

\[
                         L>(H-1)mK(d),                              \tag{3.3}
\]

then one can choose one mutually compatible packet from every list.

#### Proof

Fix a packet already selected from one list.  By the union bound over its
typed nonfixed resources, it excludes at most

\[
                       \sum_j r_j(d)\kappa_jm=mK(d)
\]

packets from any one later list.  After at most `H-1` earlier choices,
fewer than `(H-1)mK(d)` candidates are excluded.  Inequality (3.3) leaves a
packet.  Induction gives a transversal, and hypothesis 4 turns it into a
literal global replacement.  
\(\square\)

If `Phi<=E`, Theorem 2.1 gives the absolute bound

\[
                  H\le H_E:=(4+a)E+b_p+s_0+b_e.                    \tag{3.4}
\]

If `r_j(d)=O(d)` and `d=o(m)`, then `K(d)=O(d)` and (3.3) holds for all
sufficiently large `m`.  Under the absorption criterion, replace `H_E` by
`4E+O(1)`.

This is the precise sense in which constant-list greedy suffices: there are
only constantly many lists on the bounded sublevel.  It is not a theorem
that each list can be pruned to `O(1)` candidates.  Such a pruning would
need a post-pruning exclusion bound `K=O(1)`.

## 4. Exact weighted-C6 interpretation

For a native resource `x` in a restricted buffered-C6 atlas, let
`N_0^x,N_1^x,N_2^x` count the other assigned anchors at which `x` is,
respectively, source-fixed, one-free, or zero-free.  The exact external
load is

\[
                    m^2N_0^x+mN_1^x+N_2^x.                         \tag{4.1}
\]

Strong source privacy makes `N_0^x=0`.  If a native token occurs in at most
one nonfixed role at each of the other `H-1` anchors, then

\[
                    mN_1^x+N_2^x\le m(H-1).                        \tag{4.2}
\]

Thus a packet with `R(d)` native nonfixed tokens excludes at most
`R(d)m(H-1)` candidates from one other list.  More generally, (3.1) records
the precise typed congestion constants.

Distinct anchor identities are weaker than strong privacy.  The two
incidences

\[
                       (C,C+a),\qquad(C,C+b)                        \tag{4.3}
\]

are distinct but share the source-fixed token `C`; their mutual load is
quadratic.  The same audit must be made separately for witness, topology,
and complete cap-path tokens.  Local C6 geometry alone does not control
those tickets.

## 5. Common-guard contraction constants

Let the precompiler source bank obey

\[
                              |U|\le\lambda\Phi+b,                  \tag{5.1}
\]

where `lambda=4+a` under the sharp unabsorbed count and `lambda=4` under
the absorption/export row.  In one fixed common-guard alternating network,
assume

\[
                       r(A)\ge\eta|A|-\gamma
                       \qquad(A\subseteq U).                        \tag{5.2}
\]

Suppose each unmatched source contributes at most weight `w` to the next
potential and all other fresh debt is at most `c`.

### Theorem 5.1 (explicit regenerative inequality)

The next defect satisfies

\[
                     \Phi'\le\rho\Phi+\beta,                       \tag{5.3}
\]

with

\[
 \boxed{
   \rho=w(1-\eta)\lambda,
   \qquad
   \beta=w\bigl((1-\eta)b+\gamma\bigr)+c.}                         \tag{5.4}
\]

#### Proof

Apply (5.2) to `U`.  At most

\[
 |U|-r(U)\le(1-\eta)|U|+\gamma
\]

sources remain.  Multiply by `w`, add `c`, and use (5.1).  
\(\square\)

Strict contraction requires

\[
                         w(1-\eta)\lambda<1.                        \tag{5.5}
\]

For unit weights this is `eta>3/4` only on the genuine coefficient-four
face.  Without absorption it is

\[
                         \eta>1-{1\over4+a}.                        \tag{5.6}
\]

Selecting complete mutually disjoint path tickets gives `eta=1,gamma=0`
and hence an exact reset of the declared compiler sources.

## 6. Exact counterexamples

### Proposition 6.1 (component debt)

For every `N`, there is an abstract sidecar with `N` resource-private path
fragments, zero compiler Hall defect, and at least `N-1` required physical
joins under interior-preserving linearization.

#### Proof

Give each fragment a private perfect guarded compiler.  Contract every
fragment interior.  A single chronology induces a connected graph on the
`N` contracted vertices and therefore uses at least `N-1` cross-fragment
edges.  
\(\square\)

So (0.1) fails when `Phi` omits component debt.  A fixed skeleton is also
necessary: on three fragments, the individually legal private connectors
`12,23,31` are pairwise forests but jointly form a cycle.

### Proposition 6.2 (residence compensation debt)

A parent coordinate trace

\[
                             0\,1^{d+1}\,0                         \tag{6.1}
\]

is clean at parent threshold `d+1`, while its odd-diamond intersection
trace has a run of length `d` and fails the child threshold.  `N`
collar-separated copies require `N` independent compensations unless the
parent exports one additional unit of run margin.

#### Proof

The odd-diamond trace is the product of adjacent parent bits.  Eroding
`1^{d+1}` by one adjacency leaves `1^d`.  A local collar which meets only
one of `N` separated occurrences cannot repair any other occurrence.  
\(\square\)

Thus current-depth residence defect can be zero while the next lift creates
unbounded repair demand.  `Phi` must charge a minimum-run hitting bank or
the state must export the extra unit of margin.

### Proposition 6.3 (cap bottleneck)

Two tasks may have distinct private physical anchors and arbitrarily many
local packet choices, yet no compatible pair of complete tickets.

#### Proof

Force every allowed path ticket for both tasks through one unit-capacity
vertex `z`, and make every other token private.  Each task separately links,
but the two-source strict-gammoid rank is one.  
\(\square\)

Consequently anchor privacy must be paired with all-set Rado/gammoid cuts or
with explicit complete path tickets having dispersed private ranges.

### Proposition 6.4 (canonical absent-key collar)

Let a service endpoint be `u` and let active nested rays have distinct
departure-key set `K` disjoint from `u`.  In the canonical menu

\[
                     v_{b,c}=u-\{b\}+\{c\},
                     \qquad |B|=|C|=m,                             \tag{6.2}
\]

assume a ray is restored exactly when its key belongs to `v_(b,c)`.  One
pair repairs the whole collar if and only if

\[
                               K\subseteq\{c\}.                     \tag{6.3}
\]

Hence one active key leaves exactly `m` safe pairs, and two distinct active
keys leave none.

#### Proof

Every key is absent from `u`, while (6.2) inserts only `c`.  Thus a key lies
in `v_(b,c)` exactly when it equals `c`; impose this simultaneously for all
keys.  
\(\square\)

The favorable polarity is exact as well.  If a noncanonical rail begins at
`u^+` with `K subseteq u^+`, a key is lost only when `b in K`.  For
`|K|=O(d)`, at most `O(md)` pairs are bad, leaving `m^2-O(md)`.  Constructing
such a preloaded rail while preserving every other ticket is part of the
missing theorem.

## 7. Weakest sufficient all-dimensional statement

The bounded-defect route needs the following correlated construction only
on one invariant bounded sublevel, not on every abstract state.

> **Protected compound-collar lift.**  There are absolute `E,a,s_0,b` and a
> finite authenticated base such that every selected state with `Phi<=E`
> has a same-parity successor satisfying:
>
> 1. all topology, minimum-run, protected-shadow, and compiler repair tokens
>    are charged in `Phi`, and the lift has `s<=aPhi+s_0` literal seams;
> 2. passive descendants and whole seam collars form at most
>    `(4+a)Phi+b` tasks, or at most `4Phi+b` tasks under an explicit
>    absorption map;
> 3. every task has a key-preloaded/noncanonical whole-packet list obeying
>    (3.2), strong source privacy, and the typed `O(m)` load bound for all
>    physical, witness, topology, and complete common-cap tickets;
> 4. the chosen packets pass literal replay and all protected rows and
>    regenerate a state with `Phi'<=E`.

Theorems 2.1 and 3.1 then give a literal simultaneous repair for all large
dimensions; Theorem 5.1 supplies the quantitative compiler transition; the
finite base handles the remaining dimensions.  Combined with the existing
terminal bounded-defect physicalization theorem, this would imply
`nu(k)<=B(k)+O(1)`.

No present PBBS/Pascal theorem supplies the absorption map or, on the
unabsorbed face, the full key-preloaded compound lists and dispersed cap
tickets.  Therefore this note proves the exact conditional implication and
the sharp counterexamples, not an unconditional additive-constant upper
bound.

## 8. Audit boundary

The decisive counting correction is independent of Boolean geometry:
three disjoint families attaining (2.1) force coefficient `4+a`.  The
greedy proof uses only the per-other-list exclusion row and the fixed
topology/common-guard composition hypothesis.  The contraction formula is
the exact strict-gammoid rank inequality applied to the whole exposed bank.

The external mathematical inputs are:

* the exact seam-window/collar partition;
* the weighted buffered-C6 multiplicity identity;
* the minimal common-guard linkage theorem; and
* the odd-diamond residence-tax identity.

The remaining construction hypotheses are listed explicitly in Section 7;
none is inferred from scalar seam count or local circuit abundance.

The corrected arithmetic and scope have a separate light replay:

* `scratch/audit_k_absolute_sparse_exposure_compound_collar_20260731.py`,
  SHA `f5d4cf50c75b365c678de56f64ac2d24a03955be805571a47470fb6351c070d4`;
* `scratch/k_absolute_sparse_exposure_compound_collar_20260731.audit.json`,
  SHA `a19f798ee3c11ed524bba0a93514db72e71bc2a4d65e415772c2be39c49f0325`,
  payload `94e3b47b14b709c2fb5ca49fc9c5fde3ec818953e6368f0de59811b3f996050f`.

The replay checks the sharp disjoint-family count, the absorbed count,
sampled contraction thresholds, the absent-key collar multiplicities, and
finite greedy thresholds.  It does not search for or certify the missing
Boolean/Pascal packet atlas.
