# Atomic lopsided compiler selection and the native PBBS multiplicity obstruction

Date: 2026-07-30  
Lane: R, pure-mathematics all-`k` compiler lane  
Status: unconditional abstract selector theorem and exact scoped PBBS
obstructions.  The residual PBBS expansion hypothesis is not proved.

## 0. Outcome

The uniform condition `M>=4` from handoff item 1969 cannot hold on the
native within-piece PBBS candidate atlas.  Rank-`(r-1)` facets already have
one cyclic interior source candidate each, and after residence-safe opening
into `b` paths at least

\[
                         \max\{0,W-(k-1)b\}           \tag{0.1}
\]

facet parts have at most three within-piece candidates.  With one cut per
PBBS component **if that opening were residence-safe**, this would leave at
least `W/k=Cat_m` such parts; raw PBBS short runs mean that hypothesis is
not currently available.  Moreover, singleton target multiplicity is
exactly a tight-return statistic not controlled after the residence cuts
by the PBBS all-depth support theorem.

The common all-arity inequality also fails on the full pruned atlas.  When
`c_0=r-2d-1>=1`, put

\[
                         Q=2^{r-2d-2}-1,
\]

and, for an arity `2<=j<=d+1`, assume `Q>=j-1`.  Then every singleton part
supports exact minimal conflict banks
`D_j>=|V_{\{x\}}|(Q)_(j-1)`.  At deadline depth `d=O(sqrt(k))`, this gives
`D_4>M^2/16` eventually whenever the minimum list size is positive.  Hence
higher conflicts do not reduce to pairs in this atlas.

The correct replacement is an atomic **lopsided** local lemma.  Conflict
events agreeing on a common target choice are nonneighbors; only events
prescribing different candidates in one part create lopsided pressure.
This permits singleton and unequal candidate lists after exact unit closure.

For a candidate `v`, let `A(v)` be the conflict edges which use an
alternative candidate in the target part of `v`.  Choose numbers `c_v>=1`
and `0<=y_E<1`.  If

\[
 p_E\le {y_E\over\prod_{v\in E}c_v}                 \tag{0.2}
\]

and

\[
 \boxed{
 \sum_{F\in A(v)}{y_F\over1-y_F}\le\log c_v
 \quad\hbox{for every positive-mass }v,}             \tag{0.3}
\]

then one exact compatible compiler selector exists.  This is a genuine
all-arity asymmetric Hall/LLL replacement for both uniform hypotheses; it
remains integral inside one physical chronology.

## 1. Atomic product spaces have a smaller lopsided graph

Let `(V_s)_(s in Q)` be finite target parts.  Independently choose one
random vertex `X_s in V_s` with distribution `pi_s`.  A transversal edge
`E` is an atomic bad event

\[
                         B_E=\{X_s=v_s:v_s\in E\},    \tag{1.1}
\]

of probability

\[
                         p_E=\prod_{v\in E}\pi(v).   \tag{1.2}
\]

Call two atomic events **assignment-incompatible** when they use different
vertices of some common target part.

### Lemma 1.1 (exact atomic negative-dependency graph)

After discarding zero-probability events, the graph joining precisely the
assignment-incompatible pairs is a negative-dependency graph for the
events `(B_E)`.

#### Proof

Fix one event `B_E`, which prescribes values on a set `S` of target parts,
and a family `J` of events compatible with it.  For `s in S`, put

\[
                         M_s=1_{\{X_s=v_s\}},         \tag{1.3}
\]

where `v_s` is the value prescribed by `E`.  After all variables outside
`S` are fixed, every event in `J` is the conjunction of an outside
condition and requirements `M_s=1` on some subset of `S`.  Therefore the
indicator that every event in `J` is avoided is coordinatewise
nonincreasing in the vector `(M_s)_(s in S)`.

Conditioning on `B_E` sets every `M_s` equal to one.  Unconditionally these
match indicators are independent Bernoulli variables.  Averaging first
over them and then over the outside variables gives

\[
 \Pr\left(\bigcap_{F\in J}\overline{B_F}\mid B_E\right)
 \le
 \Pr\left(\bigcap_{F\in J}\overline{B_F}\right).    \tag{1.4}
\]

Bayes' identity is exactly the negative-dependency inequality

\[
 \Pr\left(B_E\mid\bigcap_{F\in J}\overline{B_F}\right)
 \le\Pr(B_E).                                        \tag{1.5}
\]

Thus compatible atomic events are legitimate lopsided nonneighbors.  QED.

Notice the direction: two events requiring the **same** value of a shared
part are nonneighbors.  Avoiding such an event can only make the common
assignment less likely.  Two different assignments are mutually exclusive,
and avoiding one can increase the other; they must be neighbors.

## 2. Candidate-specific lopsided compiler theorem

For a vertex `v in V_s`, define

\[
 \mathcal A(v)=
 \{F:\text{the edge }F\text{ uses some }w\in V_s\setminus\{v\}\}.
                                                               \tag{2.1}
\]

### Theorem 2.1 (atomic lopsided product criterion)

Suppose numbers `c_v>=1` and `y_E in [0,1)` satisfy (0.2) and the product
conditions

\[
 \boxed{
 Q_v:=\prod_{F\in\mathcal A(v)}(1-y_F)\ge c_v^{-1}}
                                                               \tag{2.2}
\]

for every vertex of positive selection probability.  Then the hypergraph
has an independent full transversal.  The additive inequalities (0.3) are
sufficient for (2.2).

#### Proof

Let `Gamma_lop(E)` be the assignment-incompatible neighbors of `E`.  Every
such neighbor belongs to `A(v)` for at least one `v in E`.  Since all
factors lie in `(0,1]`, repeating a factor only decreases a product, and
hence

\[
 \prod_{F\in\Gamma_{\rm lop}(E)}(1-y_F)
 \ge\prod_{v\in E}Q_v
 \ge\prod_{v\in E}c_v^{-1}.                         \tag{2.3}
\]

Together with (0.2),

\[
 p_E\le y_E
       \prod_{F\in\Gamma_{\rm lop}(E)}(1-y_F).       \tag{2.4}
\]

Lemma 1.1 and the asymmetric lopsided local lemma now give positive
probability that no bad edge is selected.  That outcome is one deterministic
independent transversal.

Finally, `log(1-y)>=-y/(1-y)` gives

\[
 \log Q_v\ge-sum_{F\in\mathcal A(v)}{y_F\over1-y_F},
\]

so (0.3) implies (2.2).  QED.

The use of probability proves existence of one integral selector; it does
not average different physical words.

### Corollary 2.2 (uniform residual lists)

After removing unary edges, suppose every residual part has at least `M`
candidates and choose uniformly.  For a candidate `v`, let

\[
 \widetilde D_j(v)=
 |\{F\in\mathcal A(v):|F|=j\}|.                     \tag{2.5}
\]

For any `1<c<M`, an exact selector exists if

\[
 \boxed{
 \prod_{j\ge2}\left(1-(c/M)^j\right)^{\widetilde D_j(v)}
 \ge {1\over c}\quad\hbox{for every }v.}            \tag{2.6}
\]

At `c=sqrt(e)`, the elementary sufficient form is

\[
 \sum_{j\ge2}\widetilde D_j(v)
 { (\sqrt e/M)^j\over1-(\sqrt e/M)^j}
 \le {1\over2}.                                      \tag{2.7}
\]

If every residual edge has size two, it is enough that

\[
 \boxed{
 \widetilde D_2(v)\le {M^2-e\over2e}.}              \tag{2.8}
\]

The exact product threshold for a general fixed `c` is

\[
 \widetilde D_2(v)\le
 {\log c\over-\log(1-c^2/M^2)}.                     \tag{2.9}
\]

These are candidate-specific **alternative-choice** degrees, not the much
larger incident-part degrees `D_j` from item 1969.

## 3. Exact deterministic unit closure

Singleton parts should not be padded or omitted.  Condition on their sole
vertices.  When conditioning a part `V_s` to `v`, discard every edge which
uses an alternative `w in V_s minus {v}`, replace every edge which uses
`v` by `E minus {v}`, and leave edges disjoint from `V_s` unchanged.  An
edge which becomes empty certifies infeasibility.  A residual unary edge
`{v}` forbids `v`; delete that candidate and discard every edge containing
it.  If a part becomes empty, feasibility fails; if it becomes singleton,
condition on it and continue.

### Lemma 3.1 (unit closure is exact)

When this finite process stops without an empty edge or part, compatible
full selectors of the residual instance are in bijection with compatible
full selectors of the original instance extending the forced choices.

#### Proof

Conditioning a forced vertex turns an event containing that vertex into
the conjunction on the remaining vertices.  An event prescribing a
different value in the same part becomes impossible and is discarded.  An
empty conjunction is always bad, while a unary conjunction forbids its
sole value.  Deleting that value makes every event containing it impossible.
Thus candidate deletion and newly forced parts are logical equivalences at
each step.  Composing them proves the bijection.  QED.

Unique-candidate q1 parts consequently create no lopsided alternatives of
their own.  They may still anchor positive compiler rows, and residual
choices must preserve those rows; unit closure and Theorem 2.1 retain those
constraints exactly.

### Lemma 3.2 (the physical interval map is injective)

If `(S,I)` and `(R,I)` are candidates in distinct target parts with
`S!=R`, then they form a size-two conflict.  Consequently every compatible
compiler selector maps its target parts injectively to physical source
intervals.

#### Proof

After exchanging `S,R` if necessary, choose `x in S minus R`.  Since
`S subseteq P(I)`, the anchor row for `(S,I)` has a nonempty allowed set
`E_x cap I`.  The candidate `(R,I)` omits `x` and deletes every one of
those occurrences.  Thus the pair kills that positive row.  Neither
singleton is a conflict by the mandatory-core theorem, so the pair is
minimal.  QED.

In particular, conditioning a unique native facet candidate reserves its
length-`d` interval.  Every different-label candidate on that same interval
becomes unary-forbidden under the exact closure above.  The forced vertex
is therefore not an isolated harmless choice: it must be translated
through all incident pair edges before applying Theorem 2.1.  Exact unit
closure does precisely this.

## 4. Native PBBS q1 candidates are not fourfold

Let

\[
 k=2m+1,\qquad r=m+1,\qquad W={k\choose m},          \tag{4.1}
\]

and let `3<=d<r`.  Cut a q1-rainbow complement-projected PBBS factor into
`b` directed paths, each of length at least `d+1`, and assume each piece is
strictly depth-`d` resident.  Count only source intervals lying within one
piece; cross-seam intervals are explicitly outside this theorem.

On one path, use constant endpoint extension and put

\[
                         P_p=\bigcap_{j=p-d}^{p}T_j. \tag{4.2}
\]

For a non-ramp interval `I=[a,b]` of length `ell<=d`, coordinatewise
erosion--dilation gives

\[
 \boxed{
 P(I):=\bigcup_{p=a}^{b}P_p
      =\bigcap_{j=b-d}^{a}T_j,}                     \tag{4.3}
\]

and strict residence gives

\[
                         |P(I)|=r-d+\ell-1.          \tag{4.4}
\]

Indeed the displayed intersection crosses `d-ell+1` Johnson transitions;
their departure coordinates are distinct, since a repeated departure would
create a positive run of at most `d` states.

If `|S|=r-1` and `S subseteq P(I)`, equations (4.3)--(4.4) force

\[
                         \ell=d,\qquad P(I)=S.       \tag{4.5}
\]

The interval is the natural frame of one Johnson edge and

\[
                         S=T_{a-1}\cap T_a.          \tag{4.6}
\]

PBBS facet rainbowness makes this cyclic interior candidate unique.

There is no omitted mixed-ramp case.  With constant endpoint extension,
(4.3) holds globally.  If an interval begins on the left ramp but reaches
`b>=d` (and symmetrically at the right), its relevant owner indices are
genuine and the same rank calculation (4.4) applies.  A rank-`(r-1)`
target again forces `ell=d` and the natural edge facet.  Only intervals
wholly inside the clipped ramp, `b<d` on the left or its reversal on the
right, require the ramp calculation below.

### Theorem 4.1 (quantitative native-cut obstruction)

Let `L_(<=3)` be the number of rank-`(r-1)` targets with at most three
within-piece candidates.  Then

\[
 \boxed{L_{\le3}\ge\max\{0,W-(k-1)b\}.}             \tag{4.7}
\]

#### Proof

At a left endpoint write

\[
 \delta_j=T_{j-1}\setminus T_j\qquad(1\le j\le d).
\]

The ramp has

\[
 P_p=T_0\setminus\{\delta_1,\ldots,\delta_p\},
 \qquad F_p=\{\delta_{p+1}\}\quad(0\le p<d).       \tag{4.8}
\]

A direct sandwich check gives at most `j-1` left-ramp candidates for the
facet `T_0 minus {delta_j}` when `2<=j<=d`.  Thus every endpoint has two
distinct facets, omitting `delta_2` and `delta_3`, with respectively at most
one and two ramp candidates.  The right endpoint is symmetric.  At each of
the `2b` endpoints choose one of these two facets which is not the deleted
cut facet.

Let `n_S` count endpoint owners containing `S`, and let `U_0` count targets
contained in no endpoint owner.  Each deleted PBBS edge contributes one
distinct facet counted at both paired endpoints.  After removing these `b`
forced duplications, the remaining endpoint-incidence excess is

\[
 X=\sum_{S:n_S>0}
   (n_S-1-1_{\{S\text{ is a cut facet}\}})
  =kb-W+U_0.                                          \tag{4.9}
\]

Here `sum_S n_S=2rb=(k+1)b`.  Among the `2b` selected endpoint incidences,
a repeated selected target consumes an incidence unit of `X`; a selected
target with any additional endpoint socket also consumes one.  For a
non-cut target with multiplicity `n>=2`, at most `n<=2(n-1)` selected
incidences are charged to its `n-1` excess units.  A cut target is never
selected at its paired cut endpoints, so its selected incidences are at
most `n-2`, exactly its contribution to `X`.  Consequently at least

\[
                         \max\{0,2b-2X\}             \tag{4.10}
\]

selected incidences belong to distinct targets with no other endpoint
socket.  They have their unique interior candidate and at most two ramp
candidates.  The `U_0` targets likewise have only their unique interior
candidate.  Therefore

\[
 L_{\le3}\ge U_0+max\{0,2b-2(kb-W+U_0)\}
 \ge\max\{0,W-(k-1)b\},                              \tag{4.11}
\]

where the last scalar inequality follows by splitting at
`U_0=W-(k-1)b`.  QED.

Every projected PBBS component has at least `k` owners.  **If** one cut per
component produced pieces satisfying the residence and length hypotheses,
then `b=c<=W/k`, and hence

\[
 \boxed{L_{\le3}\ge W-(k-1)c\ge W/k=\operatorname{Cat}_m.}            \tag{4.12}
\]

The displayed one-cut corollary is conditional at the growing deadline.
The audited PBBS gap-five family gives positive runs of length three, so
cuts are compulsory, but no theorem says that all short runs in one
component share one cut edge.  The general `b`-cut theorem remains valid
for any actual residence-safe decomposition.  Thus, under the explicitly
conditional one-cut hypothesis, omitting only `O(k)` targets cannot make
`M>=4`.  In the general `b`-cut theorem, if `E` exceptions are allowed, a
necessary condition for fourfold native lists is

\[
                         b\ge{W-E\over k-1}.          \tag{4.13}
\]

Cross-seam candidates, stutters, and exterior-moving braids can evade this
scoped count; they must be proved rather than silently included.

## 5. Shallow flags freeze; deep flags need exterior sockets

Let `T` be any strict depth-`d`-resident Johnson path and `P` its maximal
erosion.  Suppose

\[
                         S=\bigcap_{i=a}^{b}T_i,
 \qquad q=b-a.                                         \tag{5.1}
\]

Assume that `S` is a strict lower target.  In particular the
envelope-exact case below has `q>=1`.

If `q<=d`, the source interval

\[
                         I=[b,a+d]                    \tag{5.2}
\]

has length `d-q+1` and satisfies

\[
                         P(I)=S.                      \tag{5.3}
\]

It is therefore an envelope-exact candidate.  Choosing it creates no
negative deletion relative to `P`, although its positive row must still be
protected from other choices.  PBBS all-depth support consequently supplies
a canonical partial selector through owner depth `d`, conditional on the
selected opening retaining those occurrences.

If `q>d`, put `K=[a+d,b]`.  No admissible candidate interval for `S` may
meet `K`.  For `p<b`, both `P_p` and `P_(p+1)` contain `S`, while strict
erosion gives a nonempty set

\[
                         P_p\setminus P_{p+1}
                         \subseteq F_p\setminus S.    \tag{5.4}
\]

At `p=b`, use the nonempty entering difference
`P_b minus P_(b-1)`.  It comes from the owner transition at `b-d-1`,
which lies inside `[a,b]`; that coordinate was absent from an owner
containing `S`, and hence belongs to `F_b minus S`.  Thus every `p in K`
has `F_p not subseteq S`, and the mandatory sandwich excludes it from a
candidate interval.

This proves a sharp scope correction: the audited PBBS load

\[
                         1\le\mu_q(S)
                         \le{2q+1\choose q}           \tag{5.5}
\]

counts owner-path flag starts, not source candidates.  At `q>d` the entire
interior of such a flag supplies zero compiler sockets; only exterior
intervals can serve it.

## 6. Exact singleton lists and an exponential higher-conflict bank

The failure of the old common profile is not confined to candidate
multiplicity.  On the full mandatory-core-pruned atlas its higher conflict
degrees are also too large.  This subsection is stated for an arbitrary
linear resident Johnson path; PBBS enters only in the interpretation after
the proof.

Let

\[
 T=(T_0,\ldots,T_{W-1}),\qquad |T_i|=r,
\]

be a strict depth-`d`-resident Johnson path, where `1<=d<r` and
`W>=d+2`.  Put `n=W+d`, use maximal erosion

\[
 P_p=\bigcap_{i=\max(0,p-d)}^{\min(p,W-1)}T_i
 \qquad(0\le p<n),                                  \tag{6.1}
\]

and use the mandatory cores `F_p` from Section 5.  For every nonempty
strict lower target `S`, let the **full pruned list** be

\[
 V_S=\{(S,I):1\le |I|\le d,\ I\text{ contiguous},\
                 F(I)\subseteq S\subseteq P(I)\}.   \tag{6.2}
\]

### Theorem 6.1 (exact singleton-list statistic)

For a coordinate `x`, let `a_x` be the number of internal maximal positive
`x`-runs in `T` having exactly `d+1` states.  Let `epsilon_L(x)=1` exactly
when the initial positive `x`-run exists and has length at most `d+1`, and
define `epsilon_R(x)` symmetrically.  Then

\[
 \boxed{|V_{\{x\}}|=a_x+\epsilon_L(x)+\epsilon_R(x).}                 \tag{6.3}
\]

#### Proof

An internal positive run `[a,b]` of `T` erodes to the `P`-run `[a+d,b]`.
An initial run `[0,b]` erodes to `[0,b]`, and a terminal run
`[a,W-1]` erodes to `[a+d,n-1]`.

If `({x},I)` is retained, every `p in I` has
`emptyset != F_p subseteq {x}`, so `F_p={x}`.  Adjacent positions cannot
both have singleton core `{x}`.  Indeed, `x` then lies in both erosion
states, while the two unequal consecutive erosion states have a second
coordinate at one of their two run boundaries.  Consecutive erosion states
are unequal: their ranks differ on a ramp, while equality in the flat
region would identify an entering and departing coordinate and create a
positive `T`-run of at most `d` states.  Hence `I={p}`.

In the flat interior, `F_p={x}` precisely when the eroded `x`-run is the
singleton `{p}`, equivalently when the original internal run has `d+1`
states.  On the left ramp this occurs once precisely when the initial run
has length at most `d+1`; the right ramp is symmetric.  These cases are
disjoint and prove (6.3).  QED.

For an unmodified cyclic complement-projected PBBS component, the internal
term in (6.3) is equivalently the number of exact omitted-label returns of
gap `2d+1` for `x`.  The audited PBBS all-depth flag load does not bound
this exact-gap survivor statistic.  Thus even the singleton target lists
require information absent from the support theorem.

### Theorem 6.2 (exact large minimal-conflict bank)

Fix `2<=j<=d+1`, put

\[
 c_0=r-2d-1,
 \qquad Q=2^{c_0-1}-1,                              \tag{6.4}
\]

and assume `c_0>=1` and `Q>=j-1`.  Let `D_j(V_S)` count size-`j` minimal
conflict edges incident with the target part `V_S` in the full atlas
(6.2).  Then every singleton target satisfies

\[
 \boxed{
 D_j(V_{\{x\}})\ge |V_{\{x\}}|(Q)_{j-1},}          \tag{6.5}
\]

where `(q)_t=q(q-1)...(q-t+1)` and `(q)_0=1`.

#### Proof

Fix `v=({x},{p}) in V_{\{x\}}`, so `F_p={x}`.  Extend from `p` in a
direction in which the adjacent erosion state omits `x`.  Take the
`d+1`-position source window

\[
                         K=[i,i+d]                  \tag{6.6}
\]

having `p` as its first or last position, and include one further erosion
position beyond the other end.  The ramp orientations and `W>=d+2` ensure
that this choice also exists when `p` is on a global ramp.  Let
`\widehat K` be
these `d+2` positions and set

\[
                         C=\bigcap_{q\in\widehat K}P_q.                \tag{6.7}
\]

Every erosion state has rank at least `r-d`, and an erosion transition
loses at most one old coordinate.  Consequently

\[
                         |C|\ge r-d-(d+1)=c_0.       \tag{6.8}
\]

The direction chosen at `p` makes `x notin C`.  Choose `y in C`.

Partition `K minus {p}` into `j-1` nonempty consecutive blocks
`J_1,...,J_(j-1)`.  Every coordinate of `C` is present at every block
position and at both neighboring positions used in its mandatory cores.
At the `p` end this follows from `F_p={x}` and `x notin C`; the one extra
position in `\widehat K` handles the opposite end.  Therefore

\[
                         C\cap F(J_h)=\varnothing.   \tag{6.9}
\]

Choose ordered, pairwise distinct, nonempty subsets
`Z_h subseteq C minus {y}` and define

\[
                         R_h=F(J_h)\cup Z_h.         \tag{6.10}
\]

Then `F(J_h) subseteq R_h subseteq P(J_h)`.  Moreover every `P_q` with
`q in K` is contained in the middle owner `T_i`; since `y` belongs to
`P(J_h)` but not to `R_h`, one has `0<|R_h|<r`.  Equation (6.9) gives
`R_h cap C=Z_h`, so the `R_h` are pairwise distinct.  They also differ
from `{x}`, because `Z_h` is nonempty and `x notin C`.  Hence

\[
                         w_h=(R_h,J_h)               \tag{6.11}
\]

are valid candidates in distinct target parts.

All labels in

\[
                         E=\{v,w_1,\ldots,w_{j-1}\} \tag{6.12}
\]

omit `y`, while their pairwise disjoint intervals partition `K`.  Thus
they delete every allowed occurrence of `y` in the central requirement
`(i,y)`, and `E` is incompatible.

It is inclusion-minimal.  A proper subfamily occupies at most `d` source
positions.  A central row which can be covered by negative candidates
cannot meet a finite erosion-run endpoint, since its mandatory core would
force that coordinate into the candidate label.  Its allowed set is
therefore the full untruncated `d+1` window, too large for that proper
subfamily.  No selected-target positive row is killed: all other selected
intervals are disjoint from its anchor interval, while the anchor itself
does not delete its positive coordinates.  Source nonemptiness is automatic
from the mandatory-core theorem.  So every proper subfamily is compatible.

There are at least `Q` nonempty subsets of `C minus {y}`.  Distinct ordered
choices give `(Q)_(j-1)` distinct edges containing `v`.  Edges obtained
from different vertices `v` of the singleton part are distinct because a
transversal conflict contains exactly one vertex of that part.  Summing
over `v` proves (6.5).  QED.

For the candidate-specific lopsided graph of Theorem 2.1, a fixed
`v in V_{\{x\}}` consequently has at least

\[
 (|V_{\{x\}}|-1)(Q)_{j-1}                          \tag{6.13}
\]

opposing size-`j` events, obtained by using an alternative singleton
candidate in its part.

### Corollary 6.3 (the common quadratic profile fails)

Let `M=min_S|V_S|>0`.  Since every singleton candidate is a one-position
interval,

\[
                         M\le |V_{\{x\}}|\le n.     \tag{6.14}
\]

For `d>=3`, if `Q>=3` and

\[
                         16(Q)_3>n,                 \tag{6.15}
\]

then

\[
                         D_4>M^2/16.                \tag{6.16}
\]

Indeed, (6.5) gives `D_4>=M(Q)_3`, and (6.14)--(6.15) give
`16(Q)_3>M`.  For odd `k`, `r=(k+1)/2`, and deadline
`d=O(sqrt(k))`, condition (6.15) holds for all sufficiently large `k`.
For example, if `e=r-2d-2` and `Q=2^e-1>=4`, then
`16(Q)_3>=2^(3e-2)`, while `n=W+d<2^(k+1)`; the sufficient inequality
`3e-2>k+1` is eventual.

This is an obstruction to the **full** pruned atlas, not to all sublists.
Deleting high-pressure candidates can evade it, at the price of proving
new multiplicity estimates.  Nor does (6.5) refute the size-sensitive
product criterion: a size-`j` event carries probability of order `M^-j`.
It does prove that the common all-arity bound `D_j<=M^2/16` cannot be the
unpruned all-`k` PBBS/Pascal argument.

### Proposition 6.4 (all-arity normalization of the stable-cube bank)

The same construction explains why the lopsided criterion is the relevant
replacement.  Fix one of the displayed conflict subbanks, sampling the
singleton part uniformly from `m_x>=2` candidates.  Suppose every
auxiliary candidate appearing in that bank has sampling probability at
most `1/M_0`, where `M_0>c>1` and `c^2<m_xM_0`.  Assign
`y_E=c^|E|p_E`.  For a fixed
singleton candidate `v`, the total opposing pressure contributed by this
entire subbank is at most

\[
 \boxed{
 \sum_{j=2}^{d+1}(m_x-1)(Q)_{j-1}
 {c^j/(m_xM_0^{j-1})
  \over1-c^j/(m_xM_0^{j-1})}.}                     \tag{6.17}
\]

If `alpha=Q/M_0` and `c alpha<1`, this is at most

\[
 {c^2\alpha
  \over(1-c\alpha)(1-c^2/(m_xM_0))}.               \tag{6.18}
\]

#### Proof

For each alternative singleton vertex there are exactly `(Q)_(j-1)`
edges in the fixed subbank.  Each such size-`j` event has probability at
most `1/(m_xM_0^(j-1))`; the function `y/(1-y)` is increasing.  This gives
(6.17).  Bound `(Q)_(j-1)<=Q^(j-1)`, use
`(m_x-1)/m_x<=1`, bound every denominator by
`1-c^2/(m_xM_0)`, and sum the resulting geometric series.  QED.

For example, at `c=sqrt(e)`, `m_x>=2`, `M_0>=4`, and `Q/M_0<=1/10`,
the right side of (6.18) is strictly below `1/2=log c`.  Thus the exact
exponential conflict bank disproves the crude unweighted `D_j` profile but
does **not** by itself disprove an all-arity lopsided proof.  What is needed
is a post-cut lower bound on the auxiliary list scale relative to the
stable cube `Q`, together with upper bounds for every other opposing
kernel.  Current PBBS support theorems provide neither bound.

### Proposition 6.5 (raw PBBS tight-port supply and exact cut loss)

Assume `2<=h=d(k)<m`, put `L=floor(h/2)` and `a=h-L`.  The audited PBBS
terminal-mountain theorem says that for every

\[
 X\in\mathcal D_{m-h},\qquad \operatorname{ht}(X)\le L,               \tag{6.19}
\]

the normalized root

\[
                         D=X1^h0^h                   \tag{6.20}
\]

has first omitted-label return gap exactly `2h+1`.  Rotation symmetry gives
the same raw number of tight ports for every physical label.  That number
is at least

\[
 C_{m-h,\le L}
 \ge {2\over L+2}\sin^2{\pi\over L+2}
       \left(4\cos^2{\pi\over L+2}\right)^{m-h}.    \tag{6.21}
\]

At the Boolean deadline `h=Theta(sqrt(m))`, its base-two logarithm is

\[
                         2m-2h-O(\log m),            \tag{6.22}
\]

whereas the stable-cube parameter in (6.4) is
`Q=2^(m-2h-1)-1`.  Raw PBBS therefore has vastly more tight returns than
the stable-cube scale.

For a cyclic binary coordinate trace, let `R` be a positive run of exactly
`h+1` owner states, with boundary edges `e_in,e_out`.  After deleting an
arbitrary edge set `C` into linear pieces, this run supplies a within-piece
singleton candidate if and only if not both boundary edges belong to `C`.
Consequently, if `G_(2h+1)(x)` is the raw tight-return count for label `x`
and `V_{\{x\}}` denotes its aggregate candidate list across all cut pieces,

\[
 |V_{\{x\}}|\ge G_{2h+1}(x)-B_x(C),                 \tag{6.23}
\]

where `B_x(C)` counts tight `x`-runs whose two boundary edges are cut, and

\[
                         \sum_xB_x(C)\le |C|.       \tag{6.24}
\]

Indeed, with no internal cut and neither boundary cut the run remains
internal.  An internal cut creates terminal/initial positive fragments of
length at most `h+1`.  The extreme fragment crossing a surviving original
boundary has exactly one retained finite `x`-boundary; the direct ramp
formula gives `F_p={x}` there, even if that cut piece is too short for
Theorem 6.1's global length hypothesis.  Thus at least one singleton
survives whenever at least one original boundary remains.  If both original
boundary edges are cut, every resulting fragment is a whole-piece `x`-run
with no retained finite `x`-boundary, and this original run contributes no
core.  Each
destroyed run consumes two boundary-edge incidences, while a deleted
Johnson edge supplies exactly two such incidences, proving (6.24).
Formula (6.21) is the first positive
eigenmode in the path-graph formula for height-bounded Dyck paths; all
terms are nonnegative at even walk length.

This still does not prove the required post-cut multiplicity.  The same
cut/rethreading must enforce depth-`h` residence and upper completeness,
and (6.24) is only aggregate, not per label.  New seams can also change
the trace rather than merely delete edges.  The sharp explicit PBBS gate
is therefore survival of these tight ports, together with auxiliary-list
and all-other-kernel bounds in the **same** resident chronology.

## 7. The surviving exact gate

The raw uniform profile `M>=4`, `D_j<=M^2/16` is therefore closed for the
native PBBS atlas.  The valid replacement is:

1. choose a residence-safe PBBS/Markov opening;
2. freeze envelope-exact shallow flags and perform exact deterministic unit
   closure, including the many singleton/low-list q1 parts;
3. construct exterior or cross-seam socket lists for the deep flags; and
4. verify the candidate-specific opposing-pressure inequalities (0.2)--
   (0.3) on the residual instance.

No current PBBS theorem supplies step 3 or the opposing-pressure bound in
step 4.  This is more precise than a generic missing Hall lemma: it identifies
the correct lopsided graph, the exact native-list failure, and the deep flag
region from which new candidates must come.

### Theorem 7.1 (exact conditional `B(k)+O(k)` interface)

For each `k`, let `d(k)` be the monotone-deadline depth for which the
fixed-middle source has length `B(k)`.  Suppose one has an upper-complete,
strict depth-`d(k)`-resident middle chronology in the fixed-middle
realization theorem.  Omit a family `O_k` of nonempty strict lower targets,
condition any compatible envelope-exact partial selector, and perform the
exact unit closure of Section 3 on all nonomitted parts.  If the closure
succeeds and the residual physical candidate lists admit probabilities and
parameters satisfying (0.2)--(0.3), then

\[
                         \nu(k)\le B(k)+|O_k|.       \tag{7.1}
\]

In particular, the same hypotheses with `|O_k|<=Ck` for an absolute `C`
give `nu(k)<=B(k)+Ck`; with `O_k=emptyset` they give equality.

#### Proof

Theorem 2.1 supplies one integral compatible residual selector.  Adjoin it
to the conditioned selector and invert maximal erosion inside this one
chronology.  The fixed-middle realization theorem gives a literal word of
length `B(k)` covering every middle/upper target and every nonomitted lower
target.  Append each member of `O_k` once as a literal nonempty letter.
Existing witnesses remain contiguous, and the appended singleton intervals
cover the omitted targets.  This proves (7.1).  QED.

The authenticated `k=11,13,15` flat compilers show that forced low-list
choices can coexist in particular finite chronologies; they do not imply
the all-dimensional inequalities.  The `k=16` length-`B(16)+1` word does
not name a flat PBBS candidate atlas and has no implication here.
