# K17: a two-gap obstruction for the parent cycle and the exact common-cap gate

Date: 2026-07-31  
Status: exact scoped theorems; no global `K17` obstruction and no `K17` word

## 0. Result and scope

Let

```text
scratch/k17_parent_induced_macro_port_cycle_20260731.cycle
```

be the authenticated cyclic order on all

\[
W={17\choose9}=24310
\]

rank-nine owners.  Its SHA-256 is

```text
39cc3abe6a8991dc101a585123989deab863030060c00d3e0a2a60cd73252de6.
```

It is a Johnson Hamilton cycle and its rank-eight edge intersections are
all distinct.  Thus middle ownership and lower `q1` are already exact.

This note proves a new obstruction one layer downstream.

> **Fixed-order two-gap theorem.** Every cyclic opening of this particular
> owner order fails the row-exact/scalar gate for every monotone depth-three
> arbitrary-start/deadline staircase of optimal length.  The exact
> all-opening census gives
> \[
> G_2\le422,
> \qquad
> \operatorname {Loss}\ge47776>7401=\Delta_{17}.
> \]
> A shorter, correlation-free proof uses only the cyclic order of the
> length-two run starts and gives
> \[
> G_2\le588,
> \qquad
> \operatorname {Loss}\ge47444>7401.
> \]

Consequently the displayed order cannot be completed by changing only the
three omitted starts and three deadlines.  Lower-Hall or common-cap solving
on that fixed order is premature: scalar row recovery has already failed.

This theorem is narrower than, and logically separate from, the fixed-macro
residence obstruction:

1. `605` length-three runs are wholly internal to the fixed `1430` macros,
   so macro permutation, macro reversal, and port-flow recompletion cannot
   make that object family *flat* depth-three resident;
2. for every one-occurrence-per-rank-six transversal of the same `K15`
   parent, `165` forbidden `0 111 0` clauses are empty, exactly eleven per
   old coordinate; the exact correlated optimum is stronger, namely `180`
   surviving short runs, attained as twelve per old coordinate, so
   occurrence selection alone cannot rescue the flat branch;
3. the present two-gap theorem closes all monotone arbitrary-start
   staircases only for the one authenticated final cyclic order.

The live exits are therefore a different parent chronology or internal
forest, a rethreaded chronology whose short-run geometry is genuinely
different, or a physical compiler outside this monotone staircase class.
No statement here obstructs an optimal `K17` word.  The upper-shadow defects
of the current order also remain separate.

The second contribution is an exact fixed-fibre lower-compiler theorem.  It
states the necessary-and-sufficient target--interval matching plus
common-cap conflict cuts for any future chronology and schedule.  It also
gives a guarded Hall condition which is genuinely constructive.  The
current cycle never reaches that gate because of the scalar obstruction.

## 1. The arbitrary-start staircase

Fix a linear opening

\[
T=(T_0,T_1,\ldots,T_{W-1})
\]

of a cyclic rank-nine owner order.  For depth `d=3`, an arbitrary-start
schedule is encoded by

\[
0\le\alpha _1\le\alpha _2\le\alpha _3\le W,
\qquad
0\le\tau _1\le\tau _2\le\tau _3\le W.
\tag{1.1}
\]

As in the exact arbitrary-start staircase theorem, put

\[
g_i=|\{j:\alpha_j\le i\}|,
\qquad
h_i=|\{j:\tau_j\le i\}|.
\tag{1.2}
\]

The selected physical interval for row `i` begins at `i+g_i` and ends at
`i+h_i`.  Row legality is `tau_j <= alpha_j`, and the exact scalar loss is

\[
\operatorname {Loss}(\alpha,\tau)
=\sum_{j=1}^3\tau_j+
 \sum_{j=1}^3(W-\alpha_j)+
 |\{(j,t):\alpha_j<\tau_t\}|.
\tag{1.3}
\]

At `k=17`, optimal-length scalar capacity is exactly

\[
\operatorname {Loss}(\alpha,\tau)\le\Delta_{17}=7401.
\tag{1.4}
\]

The last term of (1.3) is nonnegative.  This elementary fact is important:
it lets the length-two runs alone give a large lower bound, without solving
the complete adjusted-frontier problem.

## 2. The two-gap inequality

For a fixed linear opening, let a length-two positive coordinate run have
owner positions `[s,s+1]`.  Define

\[
R_2(x)=\max\bigl(\{s:s+3\le x\text{ and }[s,s+1]
 \text{ is an interior length-two run}\}\cup\{0\}\bigr)
\tag{2.1}
\]

and

\[
G_2(T)=\max_{0\le x\le W}\bigl(x-R_2(x)\bigr).
\tag{2.2}
\]

Thus `G_2` is the longest clean threshold gap available before the latest
length-two obstruction.  It includes the activation delay: a run starting
at `s` enters the depth-two frontier when `x=s+3`.

### Theorem 2.1 (two-gap loss bound)

Every row-exact depth-three arbitrary-start schedule on `T` satisfies

\[
\boxed{
\operatorname {Loss}(\alpha,\tau)\ge 2W-2G_2(T).}
\tag{2.3}
\]

This assertion does not require the absence of length-one runs.  Such runs
can only impose additional constraints.

#### Proof

Consider a length-two run starting at `s`.  Its following absent row is at
`s+2`.

If `s+3 <= alpha_1`, then no start threshold has activated by `s+2`, so

\[
g_{s+2}=0.
\]

Its adjusted length is therefore two, and exact row recovery forces

\[
\tau_2\ge R_2(\alpha_1).
\tag{2.4}
\]

If `s+3 <= alpha_2`, at most the first start threshold has activated by
`s+2`, so `g_{s+2} <= 1`.  The adjusted length is at most three, and exact
row recovery forces

\[
\tau_3\ge R_2(\alpha_2).
\tag{2.5}
\]

Discard from (1.3) the nonnegative terms `tau_1`, `W-alpha_3`, and the cross
term.  Equations (2.4)--(2.5) give

\[
\begin{aligned}
\operatorname {Loss}(\alpha,\tau)
&\ge R_2(\alpha_1)+R_2(\alpha_2)
 +(W-\alpha_1)+(W-\alpha_2)\\
&=2W-
  \bigl(\alpha_1-R_2(\alpha_1)\bigr)-
  \bigl(\alpha_2-R_2(\alpha_2)\bigr)\\
&\ge2W-2G_2(T).
\end{aligned}
\]

This proves (2.3).  \(\square\)

### Corollary 2.2 (necessary clean gap)

At `k=17`, scalar feasibility requires

\[
G_2(T)\ge
\left\lceil\frac{2W-\Delta_{17}}2\right\rceil
=20610.
\tag{2.6}
\]

More precisely, the two credits
\(\alpha_j-R_2(\alpha_j)\), `j=1,2`, must have sum at least `41219`.
Consequently at least one is at least `20610`, and neither can be below
`16909` because the other is at most `W=24310`.  This is a structural
requirement, not a count of short runs.

## 3. A cyclic opening bound

List the cyclic length-two run-start occurrences, with multiplicity, as

\[
s_0\le s_1\le\cdots\le s_{N-1}<W,
\]

and extend by `s_(i+N)=s_i+W`.  Put

\[
D_j=\max_i(s_{i+j}-s_i).
\tag{3.1}
\]

### Lemma 3.1 (few deleted starts)

If the cycle has `N>r` length-two run-start occurrences and opening it
makes at most `r` of them into boundary runs, then

\[
G_2(T)\le D_{r+1}+2.
\tag{3.2}
\]

#### Proof

After deleting at most `r` cyclic start occurrences, two consecutive
surviving occurrences were separated by at most `r` deleted occurrences in
the original cyclic list.  Their cyclic displacement is therefore at most
`D_(r+1)`.  The initial and terminal pieces of the opened line are each
contained in one such cyclic surviving gap.  The activation delay in (2.1)
adds two, proving (3.2).  Multiplicity causes no problem: coincident starts
are separate occurrences and can only reduce a displacement.  \(\square\)

### 3.2 Literal K17 values

The authenticated cycle has

\[
N_2=1063,
\qquad
N_3=1829
\tag{3.3}
\]

cyclic coordinate runs of lengths two and three.  A single cut makes at
most two length-two runs boundary; it makes at most three short runs of
either length boundary.  The literal cyclic displacement values are

\[
D_1=420,
\qquad
D_3=586,
\qquad
D_4=617.
\tag{3.4}
\]

Using the actual length-two deletion bound `r=2`, Lemma 3.1 gives

\[
G_2(T)\le D_3+2=588
\]

for every cyclic opening.  Therefore Theorem 2.1 yields the entirely
solver-free bound

\[
\operatorname {Loss}\ge
2(24310)-2(588)=47444>7401.
\tag{3.5}
\]

Even the deliberately weaker rule “delete any three length-two starts”
would give `G_2 <= D_4+2=619` and

\[
\operatorname {Loss}\ge47382>7401.
\]

The exact correlated all-opening audit uses the actual three-edge support
of each length-two run.  It gives

\[
\max_{\text{cyclic openings}}G_2=422,
\tag{3.6}
\]

attained by `23889` of the `24310` cuts.  Hence the sharper audited lower
bound is

\[
\boxed{\operatorname {Loss}\ge47776>7401.}
\tag{3.7}
\]

No chain-alignment, envelope, pin, Hall, common-cap, or upper-shadow
condition is used in (3.5) or (3.7).

### Corollary 3.3 (clustering target for a rethread)

Suppose a cyclic chronology has an opening which deletes at most `r`
length-two starts and supports an optimal depth-three staircase.  By (2.6),
two consecutive surviving cyclic starts must be separated by at least

\[
20610-2=20608.
\]

Thus all but at most `r` length-two run-start occurrences lie in the
complementary cyclic arc of length at most

\[
24310-20608=3702.
\tag{3.8}
\]

For the authenticated order, the deletion-two displacement is only `586`.
This is the quantitative redesign target: a useful rethread must create a
macroscopic clean arc, not merely lower the total number of short runs.

## 4. The stronger flat obstruction for the fixed parent

The preceding theorem concerns one final chronology and a nonflat schedule.
The updated fixed-parent theorem closes a different, larger flat branch.

### 4.1 The dimension-uniform residence tax

The reason is dimension-uniform.  On any parent Johnson component put

\[
C_i=T_i\cap T_{i+1}.
\tag{4.1}
\]

For every nonconstant coordinate, a positive cyclic run of length
`ell >= 2` in `T` becomes a run of length exactly `ell-1` in `C`: the
entering parent edge does not yet contain the coordinate in its
intersection, while all later edges in the run do.  A singleton run
disappears, while an all-one constant coordinate is the exceptional cyclic
case and does not shorten.  The lower-q1-bijective parent class relevant
here has no singleton or all-one case.  Thus an odd diamond child compiled
at depth `d` cannot merely inherit parent minimum run `d+1`.  It needs
either

\[
\text{parent minimum run at least }d+2,
\tag{4.2}
\]

or an explicit cut/facet/nonflat actuator hitting every parent run of
length exactly `d+1`.

This is the **one-unit residence tax**.  A recursively useful state must
export either one extra residence unit or a certified compensation set.  A
resident factor with no such extra state is not regenerative.

### 4.2 The forced K15 packets

Let \(C_i=T_i\cap T_{i+1}\) be the rank-seven trace on the old `K15`
parent.
An `A`-shore internal short run is a pattern

\[
x\notin C_{i-1},
\qquad
x\in C_i\cap C_{i+1}\cap C_{i+2},
\qquad
x\notin C_{i+3}.
\tag{4.3}
\]

It survives precisely when the four corresponding rank-six physical edges
are retained.  Choosing one physical occurrence of every rank-six colour
therefore gives an exact one-hot CNF: each pattern contributes a negative
clause forbidding simultaneous retention of its four edges.

The authenticated parent has `1425` length-four runs, exactly `95` per old
coordinate.  By the residence-tax identity these become the `1425`
patterns (4.3).  In `165` patterns the four colours each have a unique
physical occurrence.  All four edges are forced, so the corresponding
forbidden clause is empty.  There are exactly eleven empty clauses for each
of the fifteen old coordinates.

The companion CNF has

```text
variables                         2805
clauses                           4285
forbidden clause sizes 0..4       165,420,510,270,60
empty clauses per old coordinate  11
```

Thus no rank-six occurrence transversal of this parent produces a flat
depth-three-resident child.  This conclusion is solver-free: a single empty
clause is already a contradiction, and there are `165` of them.

The exact finite optimum is stronger:

\[
\boxed{\min_{\text{occurrence transversals}}
       \#\{\text{internal A-shore short runs}\}=180.}
\tag{4.4}
\]

An authenticated transversal attains exactly twelve runs per old
coordinate and its literal expansion reconstructs all `1430` macros.  For
the lower bound, the `bound179` CNF asks whether at most fourteen
non-forced patterns can survive in addition to the `165` forced patterns.
Its DRAT proof is independently verified with a `5531`-clause core and
`99145` resolution steps.  Hence (4.4) is an exact certificate, not a
heuristic optimizer value.

The difference between `165` and `180` is an integral-correlation debt.
Each coordinate separately has only the eleven forced packets, but the one
shared occurrence transversal cannot attain those fifteen coordinatewise
minima simultaneously.  The symmetric witness pays one additional packet
on every coordinate.

### 4.3 The same occurrence variables carry upper-provider debt

Occurrence selection is not a residence-only preprocessing step.  For a
rank-six fibre `Z`, let `u_Z` be the number of its physical occurrences
whose parent upper union is uniquely provided by that edge.  Since the
transversal retains exactly one occurrence in each fibre, the exact minimum
number of deleted upper-unique provider edges is

\[
\boxed{\sum_Z(u_Z-1)^+.}
\tag{4.5}
\]

The lower bound is fibrewise: at most one of the `u_Z` unique providers can
survive.  It is attained by retaining one such provider whenever `u_Z>0`.
This debt counts destroyed internal witnesses; a macro port may later
recreate their colours, so it is not by itself a child upper-hole lower
bound.

For the current parent the profile is

\[
u_Z:0^{1835}1^{2685}2^{465}3^{20},
\qquad
\sum_Z(u_Z-1)^+=505.
\tag{4.6}
\]

The authenticated octahedral `r2` parent improves this to

\[
0^{1735}1^{2865}2^{405},
\qquad
\text{unique-provider debt }405,
\tag{4.7}
\]

and also improves the **separate marginal** internal residence optimum from
`180` to `150`.  No assertion is made that one occurrence transversal
attains both marginal optima `405` and `150`.  These improvements do not
finish the child, but they prove the correct order of quantifiers: choose
the occurrence transversal jointly against the residence hyperclauses and
upper-provider rewards, and only then solve the macro endpoint/port flow.

The statement does **not** rule out a different parent chronology, a
different internal forest construction, or a nonflat compiler.  It also
does not extend the chronology-specific values (3.3)--(3.7) to arbitrary
macro permutations.

## 5. Exact lower-compiler criterion after a chronology is changed

The fixed order fails before this section is needed.  We nevertheless state
the exact gate for a future rethread, because the displayed `1623/1013`
`q2/q3` hole counts are not themselves compiler holes.

Fix:

1. a chronology `T=(T_i)`;
2. legal physical row intervals `I_i` supplied by a chosen schedule;
3. a maximal nonempty envelope
   \[
   E_p=\bigcap_{i:p\in I_i}T_i;
   \tag{5.1}
   \]
4. an injective bank `M_0` of already protected target occurrences, if any.

At a position covered by no middle interval, the empty intersection in
(5.1) is, by convention, the full coordinate set.

Absorb the protected bank by putting

\[
\bar E_p=E_p\cap
\bigcap_{S:p\in M_0(S)}S.
\tag{5.2}
\]

Before proceeding, verify that every `bar E_p` is nonempty, every middle row
is still exact, and every protected target is still exact.  Remove the
protected targets and their used cells.  Candidate incidences must then be
rebuilt from `bar E`, not inherited from the uncapped envelope.

Let

\[
\mathcal L^-=\bigsqcup_{q=1}^{8}{[17]\choose 9-q}
\tag{5.3}
\]

be the nonempty lower target family.  In particular, `q2` and `q3` are the
rank-seven and rank-six parts.  The physical lower-cell atlas consists of
the nonempty physical intervals `J` which do not contain a whole middle row
interval.  A residual pair `(S,J)` is individually feasible exactly when

\[
\bar E_p\cap S\ne\varnothing\quad(p\in J),
\qquad
S\subseteq\bigcup_{p\in J}\bar E_p.
\tag{5.4}
\]

The first condition permits a nonempty letter at every position of `J`; the
second supplies every required bit of `S`.

Choose an injective residual assignment `M`, one feasible cell `M(S)` for
each unpinned lower target.  Its maximal common cap is

\[
Q_p(M)=\bar E_p\cap
\bigcap_{S:p\in M(S)}S.
\tag{5.5}
\]

### Theorem 5.1 (maximal-cap equivalence)

The assignment `M` is realized by one nonempty physical word if and only if

\[
\begin{array}{ll}
\text{(P)}&Q_p(M)\ne\varnothing\quad\text{for every }p;\\[2mm]
\text{(R)}&\displaystyle\bigcup_{p\in I_i}Q_p(M)=T_i
             \quad\text{for every middle row }i;\\[3mm]
\text{(L)}&\displaystyle\bigcup_{p\in M(S)}Q_p(M)=S
             \quad\text{for every residual lower target }S;
\\[3mm]
\text{(M0)}&\displaystyle\bigcup_{p\in M_0(S)}Q_p(M)=S
             \quad\text{for every protected target }S.
\end{array}
\tag{5.6}
\]

When these conditions hold, `Q(M)` itself is the coordinatewise maximal
realizing word.  The preliminary protected-target check under `bar E` is
necessary but does not replace (M0): later residual caps can still delete a
protected witness.

#### Proof

Any realizing word `A` is contained in every active middle row, every
protected target whose cell contains `p`, and every residual target whose
selected cell contains `p`.  Hence \(A_p\subseteq Q_p(M)\) pointwise.
Maximalizing from `A` to `Q(M)` cannot remove a required bit.  Conversely,
the definitions (5.2) and (5.5) forbid every bit outside an active middle,
protected, or selected lower target, while (P), (R), and (L) assert
nonemptiness and the residual positive-supply equations.  Condition (M0)
does the same for every protected target.
Thus `Q(M)` is a realization.  \(\square\)

There are no missing “forbidden-bit” clauses: containment in (5.5) enforces
them automatically.  The genuine difficulty is simultaneous positive
supply after many selected cells cap the same positions.

## 6. Hall plus the exact common-cap conflict clutter

Make every feasible incidence `e=(S,J)` a vertex, partitioned by its target
`S`.  A matching must choose one vertex from every target part and use each
physical interval at most once.  Ordinary Hall is necessary but is not the
common-cap theorem.

Define the following inclusion-minimal bad sets, always discarding sets
which already choose two incidences from one target part.

1. **Cell collision:** two incidences use the same interval.
2. **Empty position:** all chosen intervals contain `p` and
   \[
   \bar E_p\cap\bigcap_{e=(S,J)\in F}S=\varnothing.
   \tag{6.1}
   \]
3. **Middle-bit blocker:** for `b in T_i`, the selected incidences omitting
   `b` cover every host
   \[
   H_{i,b}=\{p\in I_i:b\in\bar E_p\}.
   \tag{6.2}
   \]
4. **Protected-bit blocker:** the analogous minimal cover of the host set
   of one protected target bit.
5. **Selected-lower-bit blocker:** an anchor `e_0=(S,J)`, a bit `b in S`,
   and a minimal family of other selected incidences omitting `b` whose
   cells cover
   \[
   H_{e_0,b}=\{p\in J:b\in\bar E_p\}.
   \tag{6.3}
   \]

### Theorem 6.1 (conflict-transversal equivalence)

A one-incidence-per-target selection is a common-cap compiler if and only if
it contains none of the five bad-set types above.

#### Proof

A cell collision is exactly failure of injectivity.  Equation (6.1) is
exactly failure of (P).  A bit survives at `p` precisely when every selected
target whose cell contains `p` contains that bit.  Therefore (6.2) is
exactly failure of one middle-row bit in (R), and (6.3) is exactly failure
of one selected-target bit in (L); the protected case is identical.  Every
failure contains an inclusion-minimal failure.  The converse follows by
reading the same statements backwards and applying Theorem 5.1.  \(\square\)

For a general arbitrary-start atlas, put `c_p` for the number of distinct
candidate cells through position `p`.  Minimality gives the exact safe
bounds

```text
cell collision             2
empty position             at most min(|bar E_p|,c_p), hence at most 17 globally
middle-bit blocker          at most |I_i|, hence at most 4
protected-bit blocker       at most |M_0(S)|
selected-lower-bit blocker  at most 1+|J|
```

At a position covered by at least one rank-nine middle row, the empty-set
bound improves from `17` to `9`.  The global value `17` is needed because
the empty-row intersection convention in (5.1) gives the full ground set at
an uncovered position.

If one has separately restricted to a cell-injective bounded-cell subatlas
in which every residual and protected cell has length at most three, these
specialize to `min(|bar E_p|,6)`, `4`, `3`, and `4`: there are only
`6=3*4/2` length-at-most-three cells through one position.  The complete
arbitrary-start atlas can contain longer omitted-start cells, so this
depth-only table is not automatic.  Even on the bounded-cell face, bounded
rank does not imply bounded dependency; no generic LLL or
total-unimodularity conclusion follows.

Equivalently, with binary selectors `y_e`, impose

\[
\sum_{e\in D_S}y_e=1,
\qquad
\sum_{e:\operatorname{cell}(e)=J}y_e\le1,
\tag{6.4}
\]

and, for every bad set `F`,

\[
\sum_{e\in F}y_e\le |F|-1.
\tag{6.5}
\]

The integral system (6.4)--(6.5) is feasible if and only if the fixed
chronology and schedule admit a common-cap lower compiler.  It is a finite,
proof-producing separation theorem: form the maximal cap of a tentative
matching, shrink any failed position or bit supply to a minimal blocker,
add (6.5), and repeat.

Marginal Hall alone can fail even in a two-target restricted instance.  On
three positions take

\[
\bar E_0=\{a\},\qquad
\bar E_1=\{b,c\},\qquad
\bar E_2=\{d\},
\]

with targets `A={a,c}` and `B={b,d}`.  Their unique feasible cells are
`[0,1]` and `[1,2]`, so the candidate graph has a perfect matching.  At the
overlap position, however,

\[
\bar E_1\cap A\cap B=\varnothing.
\]

Thus the matching violates an empty-position conflict.

## 7. A constructive guarded-Hall theorem

The exact conflict cuts are the fallback.  The following stronger local
hypothesis reduces the compiler to ordinary Hall and is a useful target for
a Pascal or PBBS construction.

Choose a subgraph `G` of the feasible target--cell graph and choose:

1. a guard bit `a_p in bar E_p` at every position;
2. for every middle requirement `(i,b)`, one host
   `r(i,b) in H_(i,b)`;
3. for every protected-target bit, one protected host;
4. for every incidence `e=(S,J) in G` and every `b in S`, one host
   `g(e,b) in J` with `b in bar E_(g(e,b))`.

Assume the following closure rules.

- Every incidence `(S,J) in G` contains `a_p` whenever `p in J`.
- If an incidence cell covers a chosen middle or protected host for bit
  `b`, its target label contains `b`.
- If `e` and `f` are pairwise matching-compatible--their target parts and
  cells are distinct--and the cell of `f` covers `g(e,b)`, then the target
  label of `f` contains `b`.

### Theorem 7.1 (guarded Hall lift)

Every target-saturating matching in `G` is a common-cap compiler.  Hence it
is sufficient that

\[
|N_G(X)|\ge|X|
\quad\text{for every residual target set }X.
\tag{7.1}
\]

#### Proof

The first closure rule leaves `a_p` in every maximal cap, proving (P).  The
second protects one literal host for every middle and prepin bit, proving
(R) and the protected equations.  For a selected incidence `e` and bit
`b`, the third rule says that every co-selected interval covering its chosen
host `g(e,b)` also contains `b`; the anchor `e` contains `b` by definition.
Thus `b` survives at that host, proving (L).  Theorem 5.1 applies.  Hall's
theorem supplies a target-saturating matching under (7.1).  \(\square\)

This is deliberately sufficient, not necessary.  It exposes a concrete
constructive goal: orient enough physical positions and witnesses so that
all cap conflicts disappear before applying Hall.

## 8. Consequences for the authenticated K17 carrier

The displayed lower-window diagnostics are

```text
rank-seven q2 holes  1623
rank-six q3 holes    1013
```

but these are not yet literal word holes.  In a future schedule they are
residual targets in the single family (5.3).  They must be matched together
with every other lower rank; separate rankwise Hall tests are insufficient.
A currently present trace occurrence may be pinned only after its physical
interval survives the chosen schedule and passes (5.4).  Pinning all
inherited occurrences is optional and can destroy a feasible common cap.

For the current chronology, Theorem 2.1 stops the construction earlier:
there is no row-exact scalar-feasible monotone depth-three schedule for any
opening.  Therefore no marginal-Hall, conflict-cut, or common-cap search on
this fixed order **within the monotone arbitrary-start staircase fibre** can
yield an optimal word.  A more general nonflat physical compiler is not
excluded.

The upper rank-ten holes of the current order split by tag

\[
\texttt{none}/Y/X/XY=618/623/650/0.
\]

The fixed object family has enough scalar port opportunities for those
rows, but this proves neither a coupled upper cover nor a compatible lower
compiler.  The split is chronology-specific except for the separately
audited interior opportunity banks.  The same order still has upper holes
`910/128/3` at ranks eleven through thirteen, so solving the port-turn row
alone would not establish all-depth upper service.

## 9. Exact next gate

A viable rethread must export more than a component graph.  Each oriented
macro or fragment must carry:

1. either a one-unit residence margin or an explicit compensation set for
   every minimum parent run consumed by the next diamond step;
2. the occurrence-fibre choice together with its upper-unique provider
   rewards and macro endpoint demands;
3. its internal run offsets and boundary bit traces, evaluated by the exact
   safe-corridor inequality;
4. its lower-q1 seam colour and upper turn labels;
5. all protected deeper upper witnesses;
6. its surviving physical lower cells and pins; and
7. its boundary relation for the maximal common cap.

For a completed chronology `T`, the first test is the exact functional

\[
\mathsf R_3^*(T)=
\min_{\alpha}
\operatorname {Loss}\bigl(\alpha,\rho^\alpha\bigr),
\tag{9.1}
\]

with legality and chain alignment.  The two-gap theorem supplies the cheap
necessary cut

\[
G_2(T)\ge20610.
\tag{9.2}
\]

Only after (9.1) passes should the upper port-turn cover and the exact
common-cap system (6.4)--(6.5), or the guarded Hall theorem, be invoked.

The `605` and `165` flat obstructions do not determine (9.1), while the
fixed-order two-gap obstruction says nothing about another macro order.
This is the precise proved/conditional boundary.

## 10. Reproducibility and provenance

The new light audit is

```text
python3 scratch/audit_k17_parent_cycle_nonflat_schedule_gap_20260731.py \
  > scratch/k17_parent_cycle_nonflat_schedule_gap_20260731.audit.json
```

and emits the frozen payload

```text
scratch/k17_parent_cycle_nonflat_schedule_gap_20260731.audit.json
```

It reconstructs all coordinate runs from the literal cycle, checks the
`1063/1829` profile, computes `D_1,D_3,D_4`, exhausts all cyclic openings,
and records both the robust and exact bounds.  It performs no SAT or
candidate search; the deterministic all-opening census is exhaustive.

The strengthened fixed-parent flat obstruction is in

```text
MATH_THEOREM_ODD_DIAMOND_RESIDENCE_TAX_20260731.md
MATH_THEOREM_ODD_DIAMOND_OCCURRENCE_COHERENCE_20260731.md
MATH_THEOREM_K17_FIXED_MACRO_RESIDENCE_OBSTRUCTION_20260731.md
scratch/k17_macro_residence_20260731.cnf
scratch/k17_macro_residence_20260731.map.json
scratch/k17_macro_residence_optimal_20260731.json
scratch/k17_macro_residence_optimal_20260731.verify.json
scratch/k17_macro_residence_bound179_20260731.cnf
scratch/k17_macro_residence_bound179_20260731.drat
scratch/k17_macro_residence_bound179_20260731.dratcheck.txt
```

The map binds all occurrence variables and all `1425` forbidden patterns;
the CNF contains the `165` literal empty clauses.  The older audit JSON
`scratch/k17_fixed_macro_residence_obstruction_20260731.audit.json` audits
the `605` fixed-macro statement only, not the later all-transversal
strengthening.

The two-gap proof and the common-cap equivalence were independently
adversarially audited.  The audits confirmed the numerical thresholds and
the scope separation: fixed chronology, fixed macro family, and fixed
parent occurrence transversals are three different quantifier classes.
