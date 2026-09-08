# Lane L: provider-closure cuts and the canonical two-buffer deep-fibre no-go

Date: 2026-08-01
Status: exact signed-provider min--max identity, exact private-transfer
absorber min-cut, decomposition-independent canonical two-buffer type
obstruction, literal protected-q1 source-reassembly lower bound, and sharp
scope boundary.  The provider-private abstract lower bound is not asserted
for every Boolean incidence catalogue or for the full canonical Ferrers
inventory.

## 0. Outcome

The two adjacent aggregate buffer roles

\[
                       \ell_-=d-1,\qquad \ell_+=d+1
\]

do not force the bounded root boundary needed by the NRFC merge-tree
cocycle.

There are two independent reasons.

1. For a fixed literal provider ledger, terminal named-target debt has an
   exact closure-cut formula.  Low/high socket abundance does not imply any
   one of those cuts.  A private signed-payload spanning tree can pass all
   topology and buffer-resource rows while forcing one new hole per merge.
2. Even before named targets, there is an infinite family of balanced
   semigroup inventories satisfying the exact two-buffer rounding
   hypotheses whose deep positive-composition fibres have no outgoing edge
   on the degree-one, marginal-tight successor face.  (The raw compatibility
   graph may contain slack edges, but none can occur in a perfect successor
   assignment.)  In fact the tight face contains exponentially many forced
   raw-rotation necklaces.  Hence no literal NRFC merge tree exists on that
   inventory, regardless of owner and flag labelling.

There is also a literal Boolean calibration between these two extremes.
Disjoint-tag primitive `PH` modules pass the same scalar two-buffer test,
but every cyclic source reassembly loses at least `d-1` protected old q1
colours per module, apart from explicitly counted outside providers.  Thus
their merge-tree root boundary is `Omega(Cd)`, not `O(1)`.

Consequently an unconditional `O(1)`-debt absorber theorem cannot follow
from the two buffer coordinates plus signed bookkeeping alone.  A positive
theorem needs a new **off-fibre circuit supply** and a **provider-recycling
closure expansion** hypothesis.  The full canonical Ferrers inventory may
possess such extra packages; the no-go below does not rule that out.

## 1. Exact signed provider-closure cuts

Let `P` be a finite protected target palette.  A literal baseline state has
an occurrence-labelled provider multiset with load

\[
                              m_0(t)\in\mathbb Z_{\ge0}
                              \qquad(t\in P).
\]

For a serialized, statewise-valid packet of connector and absorber macros,
let `D_e(t)` and `A_e(t)` be the numbers of providers of `t` deleted and
added by macro `e` in the state in which it is applied.  Put

\[
                \Delta_e(t)=A_e(t)-D_e(t),\qquad
                m(t)=m_0(t)+\sum_e\Delta_e(t).                 \tag{1.1}
\]

All terminal loads are assumed nonnegative; this is automatic after literal
replay.  For `S subseteq P`, use the abbreviations

\[
 m(S)=\sum_{t\in S}m(t),\qquad \Delta_e(S)=\sum_{t\in S}\Delta_e(t).
\]

### Theorem 1.1 (exact provider-closure min--max)

The number of missing targets in the terminal state is exactly

\[
 \boxed{
 h(m)=\max_{S\subseteq P}
       \left(|S|-m_0(S)-\sum_e\Delta_e(S)\right).}             \tag{1.2}
\]

In particular, terminal debt at most `H` is equivalent to the complete cut
family

\[
       m_0(S)+\sum_e\Delta_e(S)\ge |S|-H
                       \qquad(S\subseteq P).                   \tag{1.3}
\]

If the baseline is exact, `m_0(t)=1` for every `t`, this becomes

\[
                  \sum_e\Delta_e(S)\ge-H
                       \qquad(S\subseteq P).                   \tag{1.4}
\]

#### Proof

For every target, the integer `1-m(t)` is positive precisely when `m(t)=0`,
and is then equal to one.  Therefore

\[
 \max_{S\subseteq P}\sum_{t\in S}(1-m(t))
   =\sum_{t\in P}(1-m(t))_+
   =|\{t:m(t)=0\}|.
\]

Substitution of (1.1) gives (1.2), and (1.3)--(1.4) are immediate.  QED.

The maximizing set is the literal set of terminal holes.  Thus (1.2) is
not a relaxation and does not confuse occurrence load with support.

### Corollary 1.2 (exact closure obstruction)

Fix a target set `S`.  Suppose the connector packet has signed loss

\[
                         \sum_e\Delta_e(S)=-q,
\]

and every available repair macro has nonpositive net gain on `S`.  From an
exact baseline every completion has at least `q` target holes.  More
generally, if a resource-feasible repair selection can add at most `g(S)`
net providers to `S`, then every completion has at least `q-g(S)` holes.

This is the precise meaning of a provider-closed target cut.  A target can
be deleted and recreated many times; only the signed net gain on `S`
matters.

### Corollary 1.3 (exact merge-tree boundary test)

Suppose a one-root component cocycle has

\[
 \sum_e\Delta_e=
       \pi(R)-\sum_{C\in L}\pi(C)+\sum_e\epsilon_e=:B.         \tag{1.5}
\]

From an exact baseline its terminal target debt is not merely bounded by a
norm of `B`; it is exactly

\[
                       h=\max_{S\subseteq P}(-B(S)).            \tag{1.6}
\]

Consequently a dimension-independent `O(1)` root boundary is equivalent to
the uniform target-cut condition

\[
                              B(S)\ge-O(1)
                                  \qquad(S\subseteq P).         \tag{1.7}
\]

The two scalar buffer coordinates place no restriction on (1.7).

#### Proof

Substitute (1.5) and `m_0(S)=|S|` into Theorem 1.1.  QED.

## 2. Exact optimization and why the buffers do not make it a flow

Let `Z` be the family of serial-safe component-spanning macro selections
obeying all low sockets, high sockets, other unit resources, and literal
owner/recurrence guards.  The exact optimum terminal debt is

\[
 H^*=\min_{z\in Z}\max_{S\subseteq P}
 \left(|S|-m_0(S)-\sum_e z_e\Delta_e(S)\right).                \tag{2.1}
\]

This is a theorem by (1.2), not an algorithmic claim.  In general `Z`
contains a graphic spanning row, two paired partition-resource rows, and
possibly further resources.  It is not an ordinary network-flow polytope.
The diagonal/off-diagonal `2x2` paired-socket obstruction already shows
that separately feasible low and high projections need not have a common
selection.

On the special face in which every repair atom transports one provider
along an arc, its low/high pair is a single functional private resource,
and there are no graphic choices left, (2.1) reduces to an ordinary
capacitated transshipment.  Then the usual source--sink min-cuts are exact.
This positive face is strictly stronger than possession of the two
aggregate buffer counts.

### Theorem 2.1 (exact private-transfer absorber cut)

Let `m` be the literal target load after the connector packet.  Put

\[
 D=\{t:m(t)=0\},\qquad s(t)=(m(t)-1)_+ .                       \tag{2.2}
\]

Suppose the repair atlas consists of serial-composable unit transports
`u->v`: one provider of `u` is deleted and one provider of `v` is added.
Give the transport arcs integral capacities `c(u,v)`.  Assume every arc's
low/high socket pair and every other physical resource are represented by
that same network capacity (in particular, there is no independent paired
socket conflict outside the network).

The exact optimum number of holes after repair is

\[
 \boxed{
 H^*=\max_{B\subseteq P}
   \left(|D\cap B|-\sum_{u\in B}s(u)
                   -c(P\setminus B,B)\right)_+.}               \tag{2.3}
\]

Equivalently, a repair leaving at most `H` missing targets exists if and
only if, for every `B subseteq P`,

\[
 |D\cap B|\le
       \sum_{u\in B}s(u)+c(P\setminus B,B)+H,                  \tag{2.4}
\]

where `c(P-B,B)` is the total capacity of repair arcs entering `B`.

#### Proof

Build a network with source `sigma`, sink `tau`, arcs

\[
 \sigma\to u\text{ of capacity }s(u),\qquad
 u\to v\text{ of capacity }c(u,v),\qquad
 v\to\tau\text{ of capacity }1\quad(v\in D).                 \tag{2.5}
\]

An integral flow of value `q` moves `q` surplus provider units to `q`
initial holes.  Conversely every serialized repair projects to such a
flow.  For the forward physical direction, decompose an integral flow into
source--sink paths and discard directed cycles.  Execute each path from its
surplus end toward its deficit end: every intermediate target first receives
the provider that it subsequently passes on.  The serial-composability and
private-capacity assumptions make these path executions legal in any order.
Thus at most `H` holes remain exactly when the maximum flow has value at
least `|D|-H`.

For a source-side cut `{sigma} union A`, put `B=P-A`.  Its capacity is

\[
 \sum_{u\in B}s(u)+c(A,B)+|D\cap A|.
\]

Requiring this to be at least `|D|-H` is precisely (2.4).  The deficit of
this cut from `|D|` is

\[
             |D\cap B|-\sum_{u\in B}s(u)-c(P\setminus B,B).
\]

Maximizing its positive part gives (2.3).  Max-flow/min-cut and integral
capacities complete the proof.  QED.

The theorem remains valid when a functional low or high socket is inserted
as a capacity-one intermediate network node.  It fails as a projection
when a repair choice simultaneously consumes independently shared low and
high sockets: that is a paired hyperedge, not a network arc.

### Proposition 2.2 (private paired-buffer boundary can be linear)

For every `C>=2` there is a serial-safe path merge tree on `C` components
with `C-1` pairwise-private low sockets, `C-1` pairwise-private high
sockets, and pairwise-private physical ports, such that the exact baseline
is complete and the terminal named-target debt is `C-1`.

#### Construction and proof

Let

\[
                         P=\{q,t_1,\ldots,t_{C-1}\}
\]

and give every target baseline load one.  The forced merge on path edge
`i` has its own low/high socket pair and signed provider payload

\[
                         \Delta_i={\bf1}_q-{\bf1}_{t_i}.        \tag{2.6}
\]

All topology and resource rows pass.  Taking
`S={t_1,...,t_(C-1)}` in (1.4) gives value `-(C-1)`, so Theorem 1.1 forces
`C-1` holes; direct summation gives the same result.  QED.

This is a literal signed-provider catalogue counterexample to an inference
from topology plus buffer abundance.  It is not claimed that every payload
in (2.6) is realized by a Boolean incidence circuit.  Its role is to prove
that a Boolean-specific provider-recycling theorem is logically necessary.

## 3. A decomposition-independent canonical two-buffer deep-fibre no-go

The preceding target counterexample is catalogue-level.  The next theorem
is stronger on chronology: it is an actual age-type obstruction for
**every canonical package decomposition of one aggregate vector**, and
therefore rules out every labelled NRFC lift of that vector within the
canonical uniform-rotor catalogue.

Fix

\[
                         d\ge4,\qquad r\ge2d+2,                 \tag{3.1}
\]

and put

\[
\begin{gathered}
 s=r-1-d,\qquad q_0=\binom{r-2}{d},\qquad
 p_0=\binom{r-2}{d-1},\\
 N=Q^\circ_{r,d},\qquad
 T=\left\lfloor{N\over s p_0}\right\rfloor+1.                \tag{3.2}
\end{gathered}
\]

Consider the aggregate vector

\[
 A_0=q_0T,\qquad A_{r-1}=p_0T,\qquad
 A_{d-1}=A_{d+1}=N,                                            \tag{3.3}
\]

with all other entries zero.  It is realized by `T` copies of
`g_(0,r-1)` and `N` copies of `g_(d-1,d+1)`.  The resource identity

\[
                         d q_0=s p_0                            \tag{3.4}
\]

shows that it is balanced, and its two canonical buffers meet the exact
threshold with equality.

The type conclusion is independent of the owner host.  Its literal NRFC
consequence applies for every `k>=r+1` for which the displayed occurrences
are proposed to receive rank-`r` owners.

Let

\[
 \mathcal U_2=\{c=(c_0,\ldots,c_d):c_i\ge2,\ \sum_i c_i=r\},   \tag{3.5}
\]

and write `kappa_2(r,d)` for its number of cyclic-rotation orbits.

### Lemma 3.1 (a core-free top package is forced)

Every decomposition of (3.3) into canonical uniform rotor packages and
canonical unit self-loops contains at least one copy of `g_(0,r-1)`.

#### Proof

Only low roles `0,d-1` and high roles `d+1,r-1` are present.  If no
`g_(0,r-1)` were used, every one of the `p_0T` top-role occurrences would
have to be supplied by `g_(d-1,r-1)`.  That package supplies one top
occurrence and consumes

\[
                         q_{d-1,r-1}=r-d-1=s
\]

low-buffer occurrences.  It would therefore require `s p_0T>N`, by the
definition of `T`, contradicting `A_(d-1)=N`.  QED.

### Theorem 3.2 (decomposition-independent deep-fibre cut)

Fix any canonical decomposition of (3.3), and let `z>=1` be its number of
core-free packages `g_(0,r-1)`.  In every legal successor perfect
assignment on the associated canonical type occurrences, an occurrence of
type `c in U_2` can map only to an occurrence of raw-rotation type

\[
                         R(c)=(c_d,c_0,c_1,\ldots,c_{d-1}).     \tag{3.6}
\]

Copies may permute among the `z` identical package occurrences.  However,
for every cyclic type orbit `O subseteq U_2`, all `z|O|` copies of its
types form a closed successor block.  Consequently every successor
assignment has at least `kappa_2(r,d)+1` components and no one-cycle NRFC
lift exists.

#### Proof

Besides `g_(0,r-1)`, the only possible nontrivial packages are

\[
 g_{0,d+1},\qquad g_{d-1,d+1},\qquad g_{d-1,r-1}.               \tag{3.7}
\]

Every package in (3.7), every core-free package, and every canonical unit
self-loop has equal total age marginals in coordinates `2,...,d`.
Therefore the complete occurrence inventory obeys

\[
                         M_i=M_{i+1}\qquad(2\le i<d).           \tag{3.8}
\]

Every selected legal edge has nonnegative coordinate slack.  Summing the
slack and using (3.8) forces termwise equality

\[
                         c'_{i+1}=c_i\qquad(2\le i<d).          \tag{3.9}
\]

Fix an internal word

\[
                         w=(c_2,\ldots,c_{d-1})                 \tag{3.10}
\]

all of whose entries are at least two.  The package `g_(0,d+1)` has the
all-one internal word with at most one entry changed to two; the other two
packages in (3.7) and all unit packages have the all-one internal word.
Because `d>=4`, the word (3.10) has at least two entries, so none of these
packages occurs on either shore of its block.  The block consists exactly
of `z` copies of the core-free bank.

Put `R_w=r-sum_j w_j`.  The core-free sources in one copy of the block are
parametrized by

\[
 P_w=\{(x_0,x_1)\in\mathbb Z_{>0}^2:x_0+x_1\le R_w-1\},       \tag{3.11}
\]

with terminal coordinate `R_w-x_0-x_1`.  Its targets are parametrized by
the identical set of pairs `(y_1,y_2)`.  After (3.9), edge legality is
exactly

\[
                              y_1\le x_0,\qquad y_2\le x_1.    \tag{3.12}
\]

Thus the source and target prefix multisets are both `z` copies of `P_w`.
Summing the two coordinatewise nonnegative slacks over any perfect matching
gives zero in each coordinate.  Hence `(y_1,y_2)=(x_0,x_1)` on every edge,
although the copy indices may be permuted.  Conservation of total age mass
then gives target fresh coordinate `c_d`, proving (3.6).

If every coordinate of `c` is at least two, the same statement applies
after every rotation.  Hence all copies of each raw type orbit form a
closed block.  At least one buffer occurrence lies outside these blocks,
so the full factor has at least one further component.  Finally, a literal
owner/flag successor cycle projects to a legal age-type successor
assignment, so labels cannot evade the cut.  QED.

### Corollary 3.3 (an exponential zero-capacity cut family on every
canonical decomposition)

In general

\[
 |\mathcal U_2|=\binom{r-d-2}{d},\qquad
 \kappa_2(r,d)\ge {1\over d+1}\binom{r-d-2}{d}.                \tag{3.13}
\]

At `r=3(d+1)` this is

\[
 \kappa_2(r,d)\ge {1\over d+1}\binom{2d+1}{d},                \tag{3.14}
\]

which grows exponentially in `d`.  After imposing the successor degree
rows and the marginal-tight block rows (3.8), every nonempty proper union
of these orbit blocks is a zero-capacity directed connectivity cut.  There
are at least

\[
                         2^{\kappa_2(r,d)}-2                    \tag{3.15}
\]

such proper union cuts within the closed bank, in every canonical
decomposition of the same aggregate vector (3.3).

#### Proof

Subtract two from every coordinate.  The residual is a weak composition of
`r-2(d+1)` into `d+1` parts, giving the first count in (3.13).  A cyclic
orbit has size at most `d+1`, giving the lower bound.  Theorem 3.2 gives the
cut claim.  QED.

The raw compatibility digraph can contain edges leaving these words.
Global marginal tightness first forces the block decomposition, and the
identical prefix multisets inside each deep block force all remaining slack
to zero.  Thus the family (3.3) passes the exact scalar two-buffer theorem
while failing component-spanning supply on the actual successor face by an
exponentially large margin, independently of its canonical package
decomposition.  No component potential or provider absorber can telescope
a merge tree that does not exist.

## 4. A literal Boolean protected-q1 bank forces linear root boundary

The deep-fibre theorem is type-level.  The following separate construction
is literal at the source-word, owner, and lower-q1 levels.  It permits an
arbitrary cyclic reassembly of all retained source occurrences, so its
negative conclusion is stronger than a no-go for one fixed connector
catalogue.

Fix

\[
 d\ge2,\qquad s\ge3,\qquad r=d+s,\qquad
 m=\left\lceil{d+2\over2}\right\rceil,\qquad L=2m>d+1.         \tag{4.1}
\]

Choose `C>=2`, a common set `G` of size `s-2`, a common point `b`, and
pairwise-disjoint tag sets

\[
                         Z_j=\{z_{j,t}:t\in\mathbb Z/L\mathbb Z\}
                         \qquad(1\le j\le C),                  \tag{4.2}
\]

all otherwise disjoint.  It suffices that

\[
                              k\ge s-1+CL.                     \tag{4.3}
\]

On module `j`, alternate the types `P,H` and use the cyclic source letters

\[
 S_{j,t}=\begin{cases}
   G\cup\{z_{j,t}\},&t\text{ a }P\text{ position},\\
   G\cup\{b,z_{j,t}\},&t\text{ an }H\text{ position}.
 \end{cases}                                                    \tag{4.4}
\]

There are no adjacent `P` positions.  The common-core construction gives a
literal owner-simple `L`-cycle realizing `m` copies of the primitive package
`g_(d-1,d+1)`.  Its owners and old lower-q1 colours are

\[
\begin{aligned}
 T_{j,t}&=G\cup\{b\}\cup
       \{z_{j,t-d},\ldots,z_{j,t}\},\\
 Q_{j,t}&=T_{j,t}\cap T_{j,t+1}
       =G\cup\{b\}\cup
       \{z_{j,t-d+1},\ldots,z_{j,t}\}.                         \tag{4.5}
\end{aligned}
\]

The `CL` colours `Q_(j,t)` are pairwise distinct and initially have load
one.  Under the primitive-package convention which marks every offered
rank, `Q_(j,t)` is exactly the rank-`(r-1)` marked prefix through age
`d-1`, hence a literal named NRFC target, as well as the adjacent-owner
intersection displayed in (4.5).

### Theorem 4.1 (protected source-reassembly q1 lower bound)

Consider any one-cycle literal rethread or reselection which uses every
source occurrence (4.4) exactly once.  More generally, relax every type,
owner-injectivity, and transition guard and permit an arbitrary cyclic
permutation of those `CL` sources.  Among the protected old colours
`{Q_(j,t)}`, pure retained-source windows can preserve at most

\[
                              C(L-d+1)                          \tag{4.6}
\]

colours.  Consequently at least

\[
                              C(d-1)                            \tag{4.7}
\]

protected colours are missing.

If the final factor has at most `B_out` selected provider incidences for old
`Q_(j,t)` colours which are not pure internal `d`-windows of the retained
source order, then the exact bound is

\[
                       \boxed{h\ge C(d-1)-B_{\rm out}.}         \tag{4.8}
\]

Here `B_out` is a literal provider-closure capacity.  It must not be
replaced by the number of sidecar states unless a separate theorem bounds
how many protected colours one sidecar state can provide.

#### Proof

Iterating the age recurrence makes every owner the union of `d+1`
consecutive source letters.  Hence an adjacent-owner intersection coming
from retained sources is the union of the intervening `d` letters.  An old
`Q_(j,t)` can occur only if those `d` consecutive positions all carry tags
from `Z_j` and their tag set is the corresponding old cyclic `d`-window.

Fix `j` and write the maximal runs of `Z_j` tags in the new cyclic order as
lengths `l_1,...,l_q`, with sum `L`.  Because `C>=2`, these are proper
linear runs.  The number of pure `d`-windows is

\[
                     \sum_i\max(0,l_i-d+1)\le L-d+1.           \tag{4.9}
\]

Indeed the sum is zero if every run is shorter than `d`; otherwise, if
`I={i:l_i>=d}`, it is at most
`L-|I|(d-1)<=L-d+1`.  Since `L>d+1`, distinct old cyclic `d`-windows have
distinct tag sets, so each pure window supplies at most one old colour.
Summing over the `C` modules proves (4.6)--(4.7).  Every outside provider
incidence supplies at most one protected colour, giving (4.8).  QED.

### Corollary 4.2 (unbounded merge-tree cocycle boundary)

The `C` modules realize `Cm` copies of the primitive package, so

\[
                         A_{d-1}=A_{d+1}=Cm.                   \tag{4.10}
\]

Choose `C` so that `Cm>=Q^circ_(r,d)`.  Then the exact balanced scalar
two-buffer hypotheses pass.  Nevertheless, if a proposed merge-tree
cocycle on the protected q1 bank has

\[
 \sum_e\Delta_e=\Pi+E,
 \qquad
 \Pi=\pi(R)-\sum_{L\text{ leaf}}\pi(L),
 \qquad E=\sum_e\epsilon_e,                                   \tag{4.11}
\]

then

\[
 \| (\Pi+E)_-\|_1\ge C(d-1)-B_{\rm out},                      \tag{4.12}
\]

and hence

\[
 \boxed{
 \|\Pi_-\|_1\ge
 C(d-1)-B_{\rm out}-\|E_-\|_1.}                              \tag{4.13}
\]

Thus bounded outside-provider capacity and bounded exceptional error force
an `Omega(Cd)` root-minus-leaf boundary.  At fixed `d`, taking
`k=s-1+CL` makes this `Omega(k)`.

#### Proof

The initial protected loads are exactly one, so Theorem 1.1 and (4.8) give
(4.12).  Subadditivity
`||(Pi+E)_-||_1<=||Pi_-||_1+||E_-||_1` gives (4.13).  QED.

This theorem is a literal protected **partial** NRFC/primitive-buffer bank.
It is not a full unguarded canonical-Ferrers owner factor.  A global
reselection may import many outside providers, and (4.8) records that
possibility exactly.  The disjoint-tag fixed modules also need not possess
cross-module transitions; the run argument deliberately grants the much
larger class of all cyclic source permutations.  Therefore the result is a
provider-boundary obstruction, not a claim that a nonvacuous fixed-state
merge tree exists and then fails.

## 5. What an actual positive theorem must add

The no-go identifies two distinct missing rows.

1. **Off-fibre supply.**  Added circuit packages must cross every closed
   deep-word orbit cut of Theorem 3.2.  The two buffer role counts contain
   no such information.
2. **Provider-recycling expansion.**  For the selected cross-fibre packet,
   every target set must satisfy (1.3) after the same jointly
   resource-feasible absorber selection.  Separate target cuts, separate
   low/high matchings, or bounded payload support per connector are not
   sufficient.

A source-private repair bank can close the second row after the first only
if it is prospectively planted with a common low/high pairing and literal
owner/recurrence guards.  Establishing that for the full canonical Ferrers
inventory would be a new Boolean-specific theorem.  It is not a consequence
of aggregate semigroup rounding or of the bounded-debt cocycle identity.

## 6. Scope

Theorem 1.1 is fully literal and applies to arbitrary named provider loads.
Theorem 3.2 is an unlabelled age-type occurrence theorem, but this makes its
negative implication stronger: every literal NRFC chronology projects to
the forbidden one-cycle assignment.

Theorem 3.2 concerns every canonical package decomposition of the explicit
aggregate vector (3.3).  It does **not** prove that the actual canonical
Ferrers inventory has the same closed fibres; other package types may enter
them and supply off-fibre circuits.  Likewise,
Proposition 2.2 does not assert that its private payloads occur in the
Boolean incidence atlas.  The exact proved conclusion is:

> canonical two-buffer abundance, even together with exact signed-provider
> accounting, is insufficient for an unconditional bounded-root NRFC
> merge-tree theorem.
