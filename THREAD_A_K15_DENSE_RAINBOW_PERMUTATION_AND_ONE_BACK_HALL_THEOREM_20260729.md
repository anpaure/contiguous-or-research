# Dense k15 chronology: rainbow permutations and the one-back Hall theorem

Date: 2026-07-29

Status: exact global characterization, positive conditional construction
theorem, and rigorous obstruction to the independent-row first-moment and
standard symmetric-LLL criteria.
This note
does not construct an eligible parent.  It proves that the surviving object
is a support-Theta(429) coloured permutation, not a bounded repair of the
saved `426+3` factor.  It also reduces a quota-first construction to a
335-arc rainbow path forest followed by a 94-vertex Hall/voltage connector.
An independent theorem-by-theorem counteraudit has been incorporated,
including the quotient-loop, short-orbit, support, and period-parity fixes.

The cited finite `fl` and fixed-cut `r99` obstructions concern other
restricted completion faces.  None is used as evidence for or against the
global permutation considered here.

## 1. Parameters and the consumer

Put

\[
k=15,\qquad r=8,\qquad
W=\binom{15}{8}=6435,\qquad N=W/15=429.
\tag{1.1}
\]

The cyclic action is free on ranks seven and eight, so both quotient shores
have 429 vertices.  Burnside's lemma gives exactly

\[
M_+=\left|\binom{[15]}9/C_{15}\right|
=\frac{\binom{15}9+2\binom53}{15}=335                 \tag{1.2}
\]

upper target orbits.  There are 333 free orbits and two orbits of size
five.

The consumer is already proved: by the two-parent flag-stabilizer theorem,
one lower-q1-exact, upper-complete, cyclically biresident Hamilton parent in
`J(15,8)` produces a valid one-rung `k=16` child after a suitable independent
relabeling of the second rail.  No separate endpoint-collision hypothesis
remains.

## 2. The fixed-first-matching permutation model

Let `B` be the phase-labelled quotient inclusion multigraph between rank
seven and rank eight.  Fix one perfect matching `P` in `B`; one alternating
half of the audited PBBS factor is an available choice.  For every lower
owner `R`, write

\[
X_R=P(R).
\tag{2.1}
\]

Delete the phase-labelled matching incidence `R X_R` from each row.  The
residual quotient multigraph is seven-regular on both shores.  Another
phase-labelled incidence from `R` to `Y` induces the directed owner arc

\[
a:X_R\longrightarrow Y.                               \tag{2.2}
\]

Parallel quotient incidences are retained: `Y` may equal `X_R` as an orbit
vertex even though the physical incidence differs.  Such an arc is a
quotient loop and cannot occur in the eventual 429-cycle.

It carries:

* lower colour `R`;
* upper colour \(\upsilon(a)=[X_R\cup Y]\);
* deletion and insertion ports
  \(\alpha(a)=X_R\setminus R\) and
  \(\beta(a)=Y\setminus R\), with their physical phase labels;
* quotient voltage \(\omega(a)\in\mathbb Z_{15}\).

When two ports on different arcs are compared, the later port is transported
back through the cumulative intervening voltage.  All equalities below use
that common physical frame.

### Theorem 2.1 (exact dense permutation equivalence)

Let `Q` be a second perfect matching disjoint from `P` and define

\[
\pi_Q(X_R)=Q(R).                                       \tag{2.3}
\]

Then `P union Q` contracts to an eligible equivariant Hamilton parent if and
only if all of the following hold.

1. \(\pi_Q\) is one 429-cycle.
2. Its total voltage
   \[
   v(Q)=\sum_{a\in Q}\omega(a)                         \tag{2.4}
   \]
   is a unit modulo 15.
3. Every one of the 335 actual upper orbits occurs among
   \(\upsilon(a)\), \(a\in Q\).
4. If \(a_i,a_{i+1},\ldots\) are the arcs in cyclic order, then for every
   \(i\) and \(t=1,2,3\),
   \[
   \beta(a_i)\ne\alpha(a_{i+t}),\qquad
   \alpha(a_i)\ne\beta(a_{i+t}),                       \tag{2.5}
   \]
   after phase transport.

#### Proof

Because `P` and `Q` are perfect matchings, every lower owner and every
middle orbit has degree two in their union.  Contracting each lower vertex
turns its two incidences into the Johnson edge

\[
X_R=(R+\alpha(a)),\qquad Q(R)=(R+\beta(a)).
\]

Thus the factor components are precisely the cycles of the permutation
\(\pi_Q\), and every lower colour occurs once.  A single quotient cycle
lifts to one physical Hamilton cycle exactly when its voltage is coprime to
15.  Condition 3 is literal upper-q1 completeness.

Along the oriented cycle, an insertion followed by the same deletion after
`t` further transitions creates a positive run of length at most three;
the reversed equality creates the corresponding zero run.  Therefore (2.5)
is exactly the six depth-three residence inequalities.  The multi-spiral
normal form then supplies both start and end residue transversals
automatically.  Every implication is reversible.  \(\square\)

Theorem 2.1 characterizes the fixed-\(P\) slice.  It does not assert that an
arbitrary eligible parent contains this particular PBBS matching.

### Proposition 2.2 (unrestricted voltage-arc system)

Let \(\mathcal J^\to\) contain every oriented, phase-labelled Johnson edge
orbit between the 429 middle orbits.  An arc carries lower colour
\(\lambda(a)\), upper colour \(\upsilon(a)\), voltage, and its two event
ports.  Without fixing \(P\), an eligible equivariant parent is exactly a
binary vector \(x\) satisfying

\[
x(\delta^+(T))=x(\delta^-(T))=1\quad(T\in\mathcal T),
\qquad
\sum_{\lambda(a)=R}x_a=1\quad(R\in\mathcal R),          \tag{2.5a}
\]

together with the subtour, upper-cover, transported residence-path, and
unit-voltage conditions of Corollary 2.3 below.

#### Proof

The first two equation families say precisely that the selected directed
edges form an oriented degree-two middle factor using every lower owner
once.  Subtour cuts make it one quotient cycle; unit voltage makes its lift
one physical cycle.  Upper colours and residence are literal arc/path
labels.  Conversely orient any eligible parent and read off its arcs.
\(\square\)

### Corollary 2.3 (exact fixed-\(P\) binary system)

Let `A` be the directed port multigraph in (2.2), and use variables
\(q_a\in\{0,1\}\).  The dense parent problem is exactly:

\[
\sum_{a\in\delta^+(X)}q_a=1,\qquad
\sum_{a\in\delta^-(X)}q_a=1                    \quad(X\in\mathcal T),
\tag{2.6}
\]

all proper directed subtour cuts,

\[
\sum_{\upsilon(a)=U}q_a\ge1                    \quad(U\in\mathcal U),
\tag{2.7}
\]

the unit congruence for (2.4), and, for every compatible directed path
\(a_0,\ldots,a_t\), \(1\le t\le3\),

\[
\sum_{j=0}^{t}q_{a_j}\le t                              \tag{2.8}
\]

whenever either transported equality in (2.5) fails.

Relative to any old second matching `Q_0`, the symmetric difference
\(Q\mathbin{\triangle}Q_0\) is automatically a balanced union of alternating
circuits in `B`.  Hence solving (2.6)--(2.8) directly chooses the desired
global circulation; no sequence of bounded trades is part of this model.
For the saved \(426+3\) factor, the preceding collar theorem supplies the
additional automatic novelty bound

\[
\sum_{a\in Q_0}(1-q_a)\ge83,                            \tag{2.8a}
\]

or at least 84 when the update is one connected primitive.  Thus this
particular repair really has linear-size support.

### Corollary 2.4 (relative sign and phase)

Let \(\pi_0\) be the saved \(426+3\) permutation and let \(\pi\) be any
eligible 429-cycle in the same voltage chart.  The update
\(\theta=\pi\pi_0^{-1}\) is odd.  If its nontrivial support has size \(s\)
and \(c\) cycles, then

\[
s-c\equiv1\pmod2.                                      \tag{2.9}
\]

The old component voltages add to \(11+4=0\pmod {15}\).  Hence the phase
change of an eligible replacement must lie in

\[
\mathbb Z_{15}^{\times}=\{1,2,4,7,8,11,13,14\}.         \tag{2.10}
\]

#### Proof

A permutation on 429 points with two cycles has sign
\((-1)^{429-2}=-1\), whereas a 429-cycle has sign
\((-1)^{429-1}=1\).  Thus \(\theta\) is odd, and its sign is also
\((-1)^{s-c}\).  Voltage additivity gives the second assertion. \(\square\)

## 3. There is no fractional literal-load obstruction

The following count is independent of the choice of `P`.

### Lemma 3.1 (nine candidates per literal upper target)

Every literal rank-nine set `U` has exactly nine candidate residual edges
whose Johnson union with `P` is `U`.

#### Proof

For each of the nine rank-eight facets `X` of `U`, let

\[
R=P^{-1}(X).
\]

Since `R` is a rank-seven subset of `X`, the difference `U minus R` has two
elements.  Besides `X`, there is a unique other rank-eight facet `Y` of `U`
containing `R`.  The residual edge `R Y` has union `X union Y=U`.
Distinct facets `X` have distinct preimages `R`, so the nine candidate rows
are distinct.  Conversely every provider of `U` arises this way.  \(\square\)

The residual physical inclusion graph is seven-regular.  Therefore the
uniform fractional perfect matching \(y_e=1/7\) gives every literal `U`
exact fractional provider load

\[
\sum_{e\text{ provides }U}y_e=\frac97.                 \tag{3.1}
\]

In the quotient, each of the 333 free upper orbits has nine candidate arc
orbits.  Each of the two size-five orbits has three candidate arc orbits,
each contributing multiplicity three to a literal target; its
multiplicity-weighted fractional load is again `9/7`.

The uniform point does **not** satisfy the stronger unweighted
orbit-provider row for a short orbit: its value there is only `3/7`.
Those two exceptional orbit quotas must be hardwired.  Thus there is no
fractional physical-load obstruction, and every ordinary upper orbit has
slack `2/7`; exact orbit ownership remains an integral coloured constraint.
Equivalently, for a short orbit the multiplicity-weighted row

\[
\sum_a m(a,U)q_a\ge1
\]

is integer-equivalent to cover but is a weaker fractional relaxation than
the unweighted row (2.7).

## 4. Why independent row randomness does not supply the upper quotas

Keep `P` fixed but temporarily ignore column degrees.  Independently in
each lower row choose one of its seven residual incidences uniformly.

### Proposition 4.1 (exact coupon obstruction)

For every literal upper target `U`,

\[
\Pr(U\text{ is missed})=\left(\frac67\right)^9.         \tag{4.1}
\]

Consequently

\[
\mathbb E H
=5005\left(\frac67\right)^9
>1249                                                   \tag{4.2}
\]

for the number `H` of missing upper targets.

#### Proof

Lemma 3.1 gives nine candidate incidences in nine distinct independently
sampled rows.  Each is chosen with probability `1/7`, proving (4.1), and
linearity gives (4.2).  \(\square\)

Each missing-target event depends on nine row variables.  A fixed row can
serve exactly seven upper targets, one for each residual incidence.  Hence
the variable-event dependency degree is at most

\[
9(7-1)=54.                                              \tag{4.3}
\]

The ordinary symmetric local-lemma expression is therefore

\[
e\left(\frac67\right)^9(54+1)>37,                       \tag{4.4}
\]

far outside its valid range.  More generally, at `n=2r-1` the analogous
product law has a constant missing probability tending to `e^{-1}`, while
the dependency degree is polynomial in `r`.  A dependency-graph variance
bound then gives a linear number of holes with high probability as
`r` grows.

This does not prove that a quota-conditioned LLL or another correlated law is
impossible.  It proves only that first moment and the ordinary symmetric
variable-LLL criterion fail for the natural independent-row law.  A
successful random proof must add hard quota conditioning or an equivalent
nonlocal resampling mechanism.

There is a second exact warning.  On an abstract `K_(2,2)`, colour the two
diagonal arcs `U` and the two off-diagonal arcs `V`.  Row and column sums one
together with both colour-cover inequalities force the fractional point
`1/2` on all four arcs, although either integral perfect matching misses one
colour.  Thus adding colour-cover rows destroys total unimodularity in the
smallest possible rectangle.  The Boolean inclusion graph has no `C4`, so
this is not itself a physical no-go; it proves that generic matching
integrality cannot settle (2.7).

## 5. The exact rainbow-Hall decomposition

Let `A` be any allowed residual support in the fixed-`P` graph.  It may
already incorporate phase, residence, order, or protected-provider
restrictions.

### Theorem 5.1 (upper-rainbow matching plus Hall)

There is a perfect matching `Q subset A` covering all 335 upper orbits if
and only if there is a partial matching `K subset A` such that:

1. `K` contains exactly one edge of every upper orbit;
2. its 335 tails are pairwise distinct on the outgoing shore and its 335
   heads are pairwise distinct on the incoming shore; cross-shore
   coincidences are allowed and expected; and
3. after deleting those tails and heads, the remaining `94 by 94` bipartite
   graph has a perfect matching.

#### Proof

Given `Q`, choose one of its provider edges for every upper orbit.  Distinct
selected matching edges have distinct tails and heads, and the unchosen
edges of `Q` complete the residual graph.  Conversely append any residual
perfect matching to `K`.  The union is a perfect matching and retains all
designated providers.  \(\square\)

Equivalently, condition 3 is the finite family of Hall inequalities

\[
|N_{A-K}(S)|\ge |S|                                    \tag{5.1}
\]

for all residual row sets `S`.  This is the exact boundary between the
nonintegral coloured selection and the totally unimodular completion.

The count `94` is sharp.  Every perfect matching has 429 arcs and upper
completeness consumes at least 335 distinct provider arcs.  Hence only 94
arcs may be colour repetitions.  In particular, if a set `D` of `s` old
rows is changed, the number of old upper colours losing every **old-bank**
provider before additions are installed is at least

\[
|Z(D)|\ge s-94.                                        \tag{5.2}
\]

Thus at least `s-94` additions must restore those old-bank losses; at most
94 additions are unconstrained colour repetitions.  Any dense replacement
is necessarily almost rainbow.

Indeed, if the old load of colour \(U\) is \(l_U\) and \(d_U\) of its
providers are deleted, then \(d_U\le l_U-1\) unless \(U\in Z(D)\), in which
case \(d_U=l_U=(l_U-1)+1\).  Summing and using
\(\sum_U(l_U-1)=429-335=94\) proves (5.2).

## 6. A quota-first path-forest construction theorem

The rainbow bank can also localize every residence test involving the
final completion.

### Theorem 6.1 (335 plus 94 global construction)

Suppose there is a partial matching `M` of 335 residual port edges with the
following properties.

1. It contains exactly one provider of every upper orbit.
2. Its directed owner arcs form an acyclic spanning path forest on the 429
   middle vertices.
3. Every path has at least three arcs.
4. Every residence comparison lying wholly inside a path satisfies (2.5).

Then the forest has exactly 94 path components.  For two components `C,D`,
put an arc `C to D` in the connector digraph `K_M` whenever the residual
port from the terminal vertex of `C` to the initial vertex of `D` exists and
all depth-three residence comparisons whose arc window crosses that
connector seam are safe.  This includes comparisons whose two endpoint arcs
are internal forest arcs but whose intervening window crosses the seam.

If `K_M` has a directed Hamilton cycle whose connector voltage plus the
fixed internal voltage is a unit modulo 15, then `M` together with those 94
connectors is an eligible Hamilton parent.

#### Proof

A path forest on 429 vertices with 335 arcs has `429-335=94` components.
Its terminal vertices are exactly its unused tails and its initial vertices
are exactly its unused heads, so a directed cycle through the 94 components
uses every residual row and column once.  It turns the forest into one
429-cycle.

There are at least three internal arcs between two consecutive connectors.
No comparison at distance one, two, or three can therefore contain two
connectors.  Internal comparisons are safe by hypothesis, and every
remaining comparison is one of the checked connector-collar comparisons in
`K_M`.  The rainbow bank already gives upper completeness, while the two
perfect matchings give exact lower ownership.  Unit total voltage makes the
physical lift Hamilton.  Apply Theorem 2.1.  \(\square\)

The length condition has genuine room:

\[
335-3\cdot94=53.                                       \tag{6.1}
\]

The old `426+3` collar certificate implies that a witness forest obtained by
repairing that factor must use at least 16 genuinely new upper-provider
orbits.  Theorem 6.1 permits this; it does not freeze the old provider bank.

### Corollary 6.2 (one-back Hall connector)

In Theorem 6.1, it is sufficient to choose:

* a total order of the 94 path components;
* one forced connector `b`;
* no self-connectors, and every allowed connector other than `b` strictly
  increasing in the chosen order, while `b` is strictly decreasing;
* for a connector `a:C to D`, its **effective voltage**
  \[
  \widehat\omega(a)=v_M(C)+\omega(a),
  \]
  where \(v_M(C)\) is the total internal voltage of the tail path;
* a unit \(u\in\mathbb Z_{15}\) and a potential
  \(h:V(K_M)\to\mathbb Z_{15}\) such that every allowed connector `a`
  obeys
  \[
  \widehat\omega(a)=h(\operatorname{head}a)-h(\operatorname{tail}a)
             +u\,1_{\{a=b\}};                          \tag{6.2}
  \]
* Hall's inequalities on the remaining `93 by 93` graph after fixing `b`
  and deleting its tail only on the outgoing shore and its head only on the
  incoming shore.

Indeed Hall supplies an integral residual matching.  Every cycle of its
component permutation needs a descending arc, but only the cycle containing
`b` has one.  Hence the permutation is a single cycle.  The potential terms
in (6.2) telescope and leave total internal-plus-connector voltage `u`.

This is a genuine flow theorem: after the discrete rainbow forest, order,
and phase potential have been selected, the remaining assertion is ordinary
bipartite Hall and therefore integral.

## 7. A dense scalar-entropy obstruction

The run-transversal equations have very regular biresident solutions, but
regularity alone collapses ownership.

Let `c` be the scalar word of a unit-voltage strict spiral and put

\[
\Delta_{15}(c)=\{p\in\mathbb Z_W:c_{p+15}\ne c_p\},
\qquad \delta=|\Delta_{15}(c)|.                         \tag{7.1}
\]

### Theorem 7.1 (period-defect lower bound)

If the induced middle trace contains all `W` middle sets distinctly, then

\[
\boxed{\delta\ge430.}                                  \tag{7.2}
\]

#### Proof

The reconstructed state is

\[
T_i=\{x\in\mathbb Z_{15}:c_{i-xN}=1\}.                 \tag{7.3}
\]

The equality `T_(i+15)=T_i` can fail only if

\[
i-xN\in\Delta_{15}(c)
\]

for some coordinate `x`.  Thus changes along the map `i to i+15` occur on
a set of at most `15 delta` directed edges.  Hamilton ownership makes
`T_(i+15)` different from `T_i` for every one of the `W` indices.  Hence

\[
W\le15\delta,
\]

so \(\delta\ge429\).  The shift preserves the number of ones, hence the
numbers of mismatches of types `1 to 0` and `0 to 1` are equal.  Thus
\(\delta\) is even and (7.2) follows.  More generally, the map `i to i+15`
has exactly 15 cycles on `Z_W`.  On a cycle with `b` marked change edges,
the state sequence has at most `max(1,b)` distinct values.  Summing over the
15 cycles also gives

\[
|\{T_i:i\in\mathbb Z_W\}|\le15+15\delta.               \tag{7.4}
\]

This secondary bound will be useful for the calibration below.  \(\square\)

For calibration, start with the three cycles of the successor
`x to x+15` on `Z_429`.  Swap the successors at tails `0,1`, and then at
tails `4,5`.  The first swap joins the residue-zero and residue-one cycles;
the second joins that cycle to the residue-two cycle.  The result is one
residue Hamilton cycle with step histogram

\[
14^2\,15^{425}\,16^2.                                  \tag{7.5}
\]

Taking every lifetime equal to eight gives zero-gap histogram

\[
6^2\,7^{425}\,8^2.                                     \tag{7.6}
\]

Thus both start/end transversals, unit voltage, and biresidence are exact.
The four non-fifteen spacings are the only phase-change boundaries, and
each contributes the two endpoints of the block \(1^8\); hence its scalar
word has exactly eight period defects.  Formula (7.4) bounds it by 135
middle states.  It cannot be a Hamilton parent.  This proves that a bounded
number of repairs to a flat run schedule is intrinsically insufficient:
an eligible strict spiral needs linear scalar entropy.

## 8. Exact upper-load density and the strengthened consumer

There is no scalar overload obstruction either; in fact an eligible parent
must have many duplicate-safe upper edges.

### Proposition 8.1 (upper excess ledger)

For any lower-q1-exact Hamilton cycle in `J(2r-1,r)`, every coordinate has
exactly `N=W/(2r-1)` one-runs and zero-runs.  If upper loads are `l_U` and
upper support is complete, put `e_U=l_U-1`.  Then

\[
\sum_Ue_U=\frac{2W}{r+1},\qquad
\sum_{U\ni x}e_U=2N\quad(x\in[2r-1]).                  \tag{8.1}
\]

If zero-residence is at least two, the provider edges of one `U` form a
matching on its `r+1` facets.  Hence

\[
l_U\le\left\lfloor\frac{r+1}{2}\right\rfloor.          \tag{8.2}
\]

#### Proof

A coordinate occurs in `rN` middle vertices.  The exact lower palette has
`(r-1)N` lower colours containing it.  Hence the number of `1 to 0`
transitions, and therefore the number of one-runs, is `N`; cyclicity gives
the same number of zero-runs.  Upper edge colours containing the coordinate
are the `rN` occupied states plus the `N` incoming boundary edges, namely
`(r+1)N`.  There are `(r-1)N` distinct upper targets containing it, which
proves the point equation in (8.1).  The total equation follows from
\(W-\binom{2r-1}{r+1}=2W/(r+1)\).

If two provider edges of `U` share a facet `X`, then at `X` the coordinate
missing from `X` but present in `U` has local trace `1,0,1`.  This is a
zero-run of length one.  Thus providers are a matching, proving (8.2).
\(\square\)

At `k=15`,

\[
\sum_Ue_U=1430,qquad e_U\le3.                          \tag{8.3}
\]

Therefore at least

\[
\left\lceil\frac{1430}{3}\right\rceil=477             \tag{8.4}
\]

upper colours are duplicated.  The number of edges whose upper colour has
another provider is at least

\[
1430+477=1907.                                         \tag{8.5}
\]

Substituting (8.5) in the two-parent flag-stabilizer theorem gives

\[
\mathbb E C_{\rm dup}
\ge\frac{4\cdot1907^2}{8\cdot6435}>282,                \tag{8.6}
\]

and after its exact `25/42` seam-safe factor,

\[
\mathbb E N_{\rm safe}>168.                            \tag{8.7}
\]

Thus any eligible parent yields, after some independent second-rail
relabeling, at least 169 safe oriented one-rung corners.

For either size-five upper orbit, one quotient provider supplies three
literal edges.  Bound (8.2) therefore forces exactly one provider orbit;
its two missing labels must lie in distinct residue classes modulo five.
Indeed, if its missing pair is \(\{a,b\}\), the three literal provider pairs
are
\[
\{a,b\},\quad\{a+5,b+5\},\quad\{a+10,b+10\}.
\]
They form a matching exactly when \(a\not\equiv b\pmod5\).  This is a hard
finite row in the rainbow model, not a density obstruction.

## 9. The exact remaining lemma

No scalar, voltage, run-mass, or multiplicity-weighted literal-load
obstruction has been found.  The two short-orbit provider rows remain hard
integral quotas.  Two rigorous no-go statements have been proved:

1. the natural independent-row law starts with a linear upper deficit and
   fails the ordinary symmetric-LLL criterion;
2. a low-period or bounded-defect run schedule cannot own the middle layer.

The minimum positive theorem still needed is:

> **Dense rainbow-forest lemma.**  For one PBBS first matching `P`, there is
> a 335-arc upper-rainbow, internally biresident partial matching whose
> directed arcs form 94 paths, each of length at least three, and whose
> residence-pruned endpoint connector graph has a unit-voltage Hamilton
> cycle.  Equivalently, it has a one-back support satisfying Corollary 6.2.

This statement is support-Theta(N), uses literal quotient ports, and includes
upper ownership before randomization.  Theorem 6.1 would turn it directly
into the eligible Hamilton parent consumed by the two-parent theorem.

The remaining difficulty is the joint construction of the 335-colour
extendible witness bank and the 94 connector chronology.  It is not a
bounded `426+3` repair, not a rankwise marginal problem, and not an ordinary
uncoloured matching flow.
