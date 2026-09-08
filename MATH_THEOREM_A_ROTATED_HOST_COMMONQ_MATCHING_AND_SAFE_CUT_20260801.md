# Rotated endpoint hosts: exact common-Q rows, owner-collar exchange, and protected matching transport

Date: 2026-08-01  
Lane: A, additive-constant rotated host / common-Q  
Status: exact finite-dimensional equivalences, a sharp fixed-additive owner
obstruction to literal endpoint rotation, and a conditional laminar/convex
safe-cut theorem for a fresh simultaneous recompile.  This note does **not**
prove that the fresh rotated owner row exists in every Pascal child.

## 0. Result

Write a nonzero source word as

\[
                         W=P\,M\,Q=P\,R,
        \qquad R=M Q,
\]

and rotate the prefix to obtain

\[
                         W^\rho=M\,Q\,P=R\,P.              \tag{0.1}
\]

The prepared endpoint traces put consecutive letters `Z,T` at the new
`Q|P` seam.  This bypasses the absence of a native source envelope containing
`X=Z union T`, but only at the level of source positions.  There is no
automatic cap theorem and no automatic transport of a completed flat
carrier.

The exact conclusions are as follows.

1. If the owner row has window length `ell=h+1`, an interior rotation deletes
   the `h` old owner windows crossing `P|R` and creates the `h` new windows
   crossing `R|P` (when both blocks contain `h` positions on both sides of
   their seams).  A completed coefficient-one carrier rotates literally if
   and only if the lost and gained owner multisets agree.  Thus an arbitrary
   internal recut is not safe.  More sharply, in a length `B+C` flat word a
   fixed middle-owner transversal can avoid a cut only within `C` positions
   of an endpoint.  For the actual prepared endpoint blocks, literal rotation
   cannot even remain owner-complete once `d>=2C+4`: the new seam has at most
   two distinct owner values.
2. Treating `R P` instead as a new cap source gives an exact maximal-word
   test.  If the singleton seam rows are prescribed to be `Z` and `T`, then
   the maximal letters at those positions are forced to be exactly `Z` and
   `T`.  No cap containing `X=Z union T` is required.  Every mixed row through
   the seam must nevertheless pass the ordinary positive-cover equality.
3. A reference matching cell transports verbatim precisely when its interval
   avoids the old cut `P|R` (apart from the irrelevant whole-word interval).
   Crossing cells must be rematched or recompiled.  After a final literal
   word is fixed, distinct target masks never compete for one cell, so
   rematching is equivalent to the survival of one occurrence of each
   casualty mask.  Before the common-Q word is fixed, the residual assignment
   is a genuine Hall/common-Q problem.
4. There are two useful exact safe-cut criteria.  For named old witness banks,
   the forbidden-cut sets give an exact union test; if those sets are
   laminar, it reduces to the sum of their maximal members.  For a fixed cut
   with a private convex residual slot atlas, Hall is equivalent to checking
   only interval cuts.  If the slot neighborhoods are laminar, only the
   laminar neighborhood cuts remain.

Consequently the sound bridge is a simultaneous **MQP rethread/recompile**
theorem.  Rotating an already completed coefficient-one word is justified
only on the exceptional lost-equals-gained owner face.

## 1. Exact interval and owner-collar ledger

Let `P=(p_1,...,p_a)` and `R=(r_1,...,r_b)`, and put `N=a+b`.  Denote the old internal gap
`p_a|r_1` by `c`, and the new internal gap `r_b|p_1` by `c'`.

### Lemma 1.1 (proper interval transport)

Every proper old interval wholly contained in `P` or wholly contained in
`R` maps injectively to an interval of `R P`, with the same ordered letters
and the same OR.  An old proper interval crossing `c` maps to a cyclic arc
which crosses the two endpoints of the linear word `R P`, and hence is not a
linear interval there.

#### Proof

Rotation preserves the order inside each block.  A crossing old interval is
a suffix of `P` followed by a prefix of `R`; after rotation these pieces are
a suffix and a prefix of the complete linear word, respectively.  Their
union is a wrapping cyclic arc.  It is a linear interval only when it is the
whole word, excluded by properness.  Distinct within-block intervals retain
distinct endpoint pairs.  \(\square\)

For a word `A`, write `D^(ell-1) A` for its row of consecutive `ell`-letter
unions.

### Theorem 1.2 (flat owner-collar exchange)

Assume `a,b>=ell-1`.  Passing from `P R` to `R P` retains every `ell`-window
contained in one block, deletes exactly

\[
 L_c=\left\{
   \bigvee(p_{a-i+1},\ldots,p_a,r_1,\ldots,r_{\ell-i}):
                  1\le i<\ell\right\},                    \tag{1.1}
\]

and creates exactly

\[
 G_c=\left\{
   \bigvee(r_{b-i+1},\ldots,r_b,p_1,\ldots,p_{\ell-i}):
                  1\le i<\ell\right\}.                    \tag{1.2}
\]

Here the braces denote multisets.  Therefore

\[
       \operatorname{multi}D^{\ell-1}(P R)
       =\operatorname{multi}D^{\ell-1}(R P)
       \quad\Longleftrightarrow\quad L_c=G_c.              \tag{1.3}
\]

In particular, for owner length `ell=h+1`, an internal rotation exchanges
exactly `h` owner rows.  If the old row is coefficient-one, the rotated row
is coefficient-one with the same owner set only if every gained owner is one
of the lost owners, once each.

#### Proof

An `ell`-window either lies inside one block or crosses the unique internal
gap.  The within-block windows are identical in the two orders.  At `c`, a
crossing window is determined by the number `i` of its letters in `P`, giving
(1.1).  At `c'` the same count gives (1.2).  Subtracting the common
within-block multiset proves (1.3).  \(\square\)

If one block is shorter, use the two (generally different) index sets

\[
 \begin{aligned}
 I^-&=\{i:\max(1,\ell-b)\le i\le\min(\ell-1,a)\},\\
 I^+&=\{j:\max(1,\ell-a)\le j\le\min(\ell-1,b)\}.
 \end{aligned}                                             \tag{1.4a}
\]

Restrict (1.1) to `i in I^-` and (1.2) to `j in I^+`.  The two sets have
the same cardinality, namely

\[
 \min(a,N-\ell+1)-\max(1,a-\ell+2)+1,                     \tag{1.4}
\]

with a zero value understood when the upper endpoint is smaller.  The
multiset identity remains exact after these separate restrictions.

Theorem 1.2 is the basic transport obstruction.  Endpoint preparation does
not make (1.3) automatic.  Hence the positive construction below does not
rotate a completed flat owner word; it uses `R P` as the order of a new
simultaneous cap/owner compilation.

### Theorem 1.3 (fixed-owner safe cuts are endpoint-local at `B+C`)

Let the source length be

\[
                         N=\mathsf W+d+C,                  \tag{1.5}
\]

so there are `N-d=mathsf W+C` consecutive owner windows of length `d+1`.
Assume these windows cover `mathsf W` distinct middle owners, and choose one
window for each owner.  For the cut after source position `c`, the number of
owner windows which cross the cut is

\[
 \chi_d(c)=
 \max\!\left(0,
   \min(c,N-d)-\max(1,c-d+1)+1\right).                    \tag{1.6}
\]

If all chosen owner windows avoid the cut, then

\[
                              \chi_d(c)\le C.              \tag{1.7}
\]

In particular, when `N>=2d` and `d>C`, every such cut satisfies

\[
                         c\le C\quad\hbox{or}\quad N-c\le C. \tag{1.8}
\]

#### Proof

A length-`d+1` window with start `s` crosses the gap after `c` precisely when

\[
             \max(1,c-d+1)\le s\le\min(c,N-d),
\]

which gives (1.6).  Exactly `mathsf W` of the `mathsf W+C` windows were
chosen, so only `C` windows are unchosen.  If every chosen window avoids the
cut, every crossing window is unchosen, proving (1.7).  For `N>=2d`,
`chi_d(c)=min(d,c,N-c)`.  If `d>C` and both endpoint distances exceed `C`,
this minimum exceeds `C`, a contradiction.  \(\square\)

This theorem concerns transport of a fixed completed owner transversal.  It
does not prohibit changing the owner order and recompiling all central rows.

### Theorem 1.4 (prepared endpoint rotation has a fixed-additive owner no-go)

Let `d>=3`, let

\[
 \begin{aligned}
 P&=(T,f_{d-1},f_{d-2},\ldots,f_2),\\
 Q&=(f_{d-1},f_{d-2},\ldots,f_2,Z),                       \tag{1.9}
 \end{aligned}
\]

and suppose `|M|>=d` and the full word has length (1.5).  Assume every old
owner window is a middle-rank mask and the row covers all `mathsf W` middle
masks.  If the literal
rotation

\[
                           P M Q\longmapsto M Q P           \tag{1.10}
\]

is still owner-complete, then necessarily

\[
                                  d\le 2C+3.               \tag{1.11}
\]

Consequently, for fixed `C` and `d>=2C+4`, the endpoint wrap cannot be a
rotation of a completed `B+C` flat word.

#### Proof

Since `|P|=|Q|=d-1`, exactly `d-1` old owner windows cross `P|M` and are
deleted by (1.10).  If an owner value has load `l_U`, then

\[
                 \sum_U(l_U-1)=C.
\]

The number of window occurrences whose values are nonunique is therefore

\[
 \sum_{l_U\ge2}l_U
   =\sum_{l_U\ge2}(l_U-1)+\#\{U:l_U\ge2\}\le2C.           \tag{1.12}
\]

Thus at least `d-1-2C` deleted windows carried globally unique, pairwise
distinct owner masks.

There are `d-1` new owner windows crossing `Q|P`.  Of these, the `d-2`
windows which use at least two letters from each prepared side all have the
single value

\[
                    G=Z\cup T\cup\{f_2,\ldots,f_{d-1}\}.   \tag{1.13}
\]

Indeed the suffix of `Q` and prefix of `P` contain complementary portions
of the displayed filler list.  The sole remaining extreme window contains
all of `Q`, the first letter `T` of `P`, and one final letter of `M`; it has
at most one further value.  Hence the whole gained seam contains at most two
distinct owner masks.  Every globally unique deleted mask must be among
these gained masks if owner coverage is to survive.  Therefore

\[
                            d-1-2C\le2,
\]

which is (1.11).  \(\square\)

Unlike Theorem 1.3, this is a full owner-coverage obstruction, not merely a
no-go for transporting named occurrences.  It is still scoped to the
literal prepared-tail rotation; changing the source letters under rebuilt
owner caps is exactly the escape studied next.

## 2. Exact maximal-word test at the `Z,T` seam

Fix the rotated order `R P`.  Let `V` be its live source positions and let
`mathcal R` be every exact compiler, owner, protected-witness and mixed row
which the proposed plus state must realize.  A row `J` has live positions
`V_J subseteq V`, frozen exterior OR `E_J`, and required value `S_J`.  Let
`C_v` be the source cap at `v`.  Define

\[
 K_v=C_v\cap\bigcap_{J:\,v\in V_J}S_J.                    \tag{2.1}
\]

Let `z,t` denote the consecutive seam positions and include the singleton
rows

\[
                 (\{z\},\varnothing,Z),\qquad
                 (\{t\},\varnothing,T).                   \tag{2.2}
\]

Every frozen exterior letter is assumed nonempty and legal in its rebuilt
exogenous cap.  If that is not known, it must be moved into `V` and tested
by the same maximal-word equations; the frozen OR `E_J` by itself does not
certify cap legality.

### Theorem 2.1 (rotated-seam common-Q equivalence)

There is one nonzero capped word on `R P` realizing every row in
`mathcal R` if and only if

\[
 E_J\subseteq S_J,\qquad K_v\ne\varnothing,\qquad
 S_J=E_J\cup\bigcup_{v\in V_J}K_v                         \tag{2.3}
\]

for every row `J` and live position `v`.  Under the singleton rows (2.2),
the seam part of (2.3) is equivalently

\[
 \begin{aligned}
 Z&\subseteq C_z\cap\bigcap_{J:\,z\in V_J}S_J,\qquad K_z=Z,\\
 T&\subseteq C_t\cap\bigcap_{J:\,t\in V_J}S_J,\qquad K_t=T,
 \end{aligned}                                             \tag{2.4}
\]

together with the reconstruction equalities for all nonsingleton rows.
Every row containing both seam positions necessarily satisfies

\[
                         Z\cup T\subseteq S_J,              \tag{2.5}
\]

but there is no source cap for `X=Z union T` and none is needed.

#### Proof

The first assertion is the maximal-word positive-cover theorem: every
feasible letter is contained in (2.1), so (2.3) is necessary, while the word
`A_v=K_v` proves sufficiency.  The singleton row at `z` makes

\[
 K_z=C_z\cap Z\cap\bigcap_{J\ne\{z\}:z\in V_J}S_J.
\]

Its reconstruction equality is `K_z=Z`, which is equivalent to the first
line of (2.4).  The proof for `t` is identical.  Equation (2.5) follows
because both forced nonempty letters occur in the row.  \(\square\)

Thus the absence of `X` from every native maximal envelope is no longer the
relevant test.  It has been replaced by two separate cap containments and
all mixed-row reconstruction equalities.  This replacement is real but not
automatic.

### Corollary 2.2 (exact simultaneous owner/compiler recompile)

Let `mathcal O` be the `mathsf W+C` central cells of `R P`.  Choose a target
`O_J` for every `J in mathcal O` so that every middle owner occurs at least
once; equivalently, choose an injection of the `mathsf W` middle owners into
`mathcal O` and label the remaining `C` cells by allowed repeats.  Add all
rows `J mapsto O_J`, all seam-ray rows, and every selected protected/compiler
row to `mathcal R`.

Fix also an exogenous cap state `C^ext`; equivalently, quantify over a
declared finite menu of such states.  The owner rows contribute the owner
screen

\[
 C_v^{\rm own}=\bigcap_{J\in\mathcal O:\,v\in J}O_J,
 \qquad C_v=C_v^{\rm ext}\cap C_v^{\rm own},              \tag{2.6}
\]

where intersecting the owner targets directly in (2.1) is the same
operation.  For this fixed occurrence assignment and cap state, a
simultaneous fresh central owner row and common-Q compiler exists if and only
if (2.3) holds.  If either is not fixed, exact existence is the union of this
test over all owner injections, allowed repeat labels and allowed exogenous
cap states.

#### Proof

The central owner equations are rows of exactly the same Boolean-union form
as every compiler equation.  Theorem 2.1 is therefore necessary and
sufficient after they are included.  Quantifying over owner assignments is
the stated union.  \(\square\)

This is the noncircular replacement for literal transport.  The overlap of
the central windows is handled inside the intersections (2.1); rankwise or
marginal owner coverage alone does not imply (2.3).  The corollary certifies
the central OR row only.  Johnson adjacency, q1, residence, topology and
upper protection hold only when their own exact rows are also included.

### Minimal cap counterexample

Take `Z={a}`, `T={b}`, caps `C_z=Z`, `C_t=T`, and one additional row on
`{z,t}` with target `{a,b,c}` and empty exterior.  Both seam letters are
nonempty and cap-legal, and `Z union T` is contained in the row target, but
the maximal union is only `{a,b}`.  Hence (2.3) fails.  Separate seam caps,
or even (2.5), do not imply common-Q.

## 3. Protected matching transport

Let `M_0` be a literal reference matching from pairwise-distinct target
masks `S` to proper physical cells `I_S` of `P R`.  A cell is **stable** if
it avoids `c`; otherwise call its target a **casualty**.

### Theorem 3.1 (strong transport and literal rematching)

1. Every stable edge `S-I_S` transports injectively to a cell of `R P` with
   the same value.
2. The whole reference matching transports edge-for-edge if and only if all
   its cells are stable.
3. Suppose a final literal word on `R P` retains the transported stable
   cells.  Then all casualty targets can be rematched if and only if every
   casualty mask occurs in at least one allowed final cell.  Choices for
   different casualty masks are automatically cell-disjoint.

For occurrence-labelled multiplicity, first remove every reserved stable,
seam and task cell.  If `mu_res(S)` copies remain to be placed and
`Occ^free_(R P)(S)` is the bank of allowed unreserved occurrences, the last
condition becomes

\[
        |\operatorname{Occ}^{\rm free}_{R P}(S)|
                              \ge\mu_{\rm res}(S)           \tag{3.1}
\]

for every mask `S` separately.

#### Proof

Parts 1--2 are Lemma 1.1.  For part 3, necessity is immediate.  Conversely,
choose one occurrence for each casualty mask.  One physical cell has one
literal OR value, so occurrences selected for distinct masks cannot be the
same cell; they also cannot equal a stable cell carrying a different target
mask.  Repeated copies of one mask compete only with one another, giving
(3.1).  \(\square\)

Before a final word is fixed, a cap cell can have several possible target
assignments and the conclusion of part 3 is unavailable.  Those assignments
must be included in the simultaneous maximal-word system.  In particular,
to guarantee the stable part under Theorem 2.1, include every transported
stable cell as an exact row.  The maximal word then preserves it by (2.3).

### Minimal transport counterexample

Let `P=({a})`, `M=({b})`, and `Q=({c})`.  The old cell on the first two
positions has value `{a,b}` and crosses `P|M`.  After rotation the word is
`({b},{c},{a})`, whose interval deck does not contain `{a,b}`.  The new seam
letters `Z={c}`, `T={a}` are perfectly legal, but the protected target is
lost.  Local seam legality therefore does not transport an arbitrary old
matching.

## 4. Exact forbidden-cut and laminar criteria

Let `mathcal C` be a finite bank of allowed cut gaps in one fixed linear
chart.  For a protected target `S`, let `mathcal W_S` be its bank of named
proper old witness intervals.  For an interval `I`, let `g(I)` be its set of
internal gaps.  (A whole-word witness is never endangered and may simply be
removed from this test.)  Define

\[
                  F_S=\bigcap_{I\in\mathcal W_S}g(I).       \tag{4.1}
\]

Thus `c in F_S` exactly when every named witness of `S` crosses `c`.

### Theorem 4.1 (exact transport-safe cut)

A cut in `mathcal C` preserves at least one named old witness of every
protected target if and only if

\[
                   \mathcal C\not\subseteq\bigcup_S F_S.   \tag{4.2}
\]

If the nonempty sets `F_S cap mathcal C` form a laminar family, let
`mathcal F_max` be its inclusion-maximal members.  They are pairwise
disjoint, and (4.2) is equivalent to

\[
             \sum_{F\in\mathcal F_{\max}}|F|<|\mathcal C|. \tag{4.3}
\]

The same statement applies to the cells of a fixed reference matching by
taking one witness per target.

#### Proof

A target loses all named transported witnesses exactly on `F_S`; avoiding
their union is therefore necessary and sufficient.  In a laminar family,
distinct maximal members are disjoint and their union is the union of the
whole family, proving (4.3).  \(\square\)

This is a transport criterion, not a regeneration criterion.  A cut inside
`F_S` may still be usable if a new `Q|P` seam cell recreates `S`; that option
belongs to the residual completion theorem below.

In a fresh recompile, Theorem 4.1 selects only cut-avoiding **addresses**.
Their old values are not inherited after the source letters change.  Every
retained address/value equality must be inserted as a row of `mathcal R` and
must pass (2.3).

### Corollary 4.2 (convex safe-cut Helly certificate)

Suppose that for each protected target `S`, the set

\[
 C_S=\{c\in\mathcal C:\text{some named witness of }S\text{ avoids }c\}
                                                                  \tag{4.4}
\]

is a nonempty interval `[ell_S,r_S]` in one common linear order on the
candidate cuts.  Then a single cut transports a named witness for every
target if and only if

\[
                         \max_S\ell_S\le\min_S r_S.        \tag{4.5}
\]

In particular, pairwise intersection of the safe-cut intervals is already
sufficient.

#### Proof

A common safe cut is exactly a point of `intersection_S C_S`.  Finite
intervals on a line have nonempty intersection exactly under (4.5), and
pairwise intersection implies the same inequality.  \(\square\)

Neither laminarity of the old witness intervals nor convexity of one target's
safe-cut set is enough by itself; Theorem 4.1 or (4.5) must hold jointly.

## 5. Convex residual completion

Fix a cut and suppose a residual bank `D` of occurrence-labelled demands
must be assigned to an ordered bank of free cells

\[
                          f_1<\cdots<f_s.                   \tag{5.1}
\]

Assume each demand `u` has a nonempty interval of eligible cells

\[
                         N(u)=[\ell(u),r(u)].               \tag{5.2}
\]

Assume also the **private common-Q composition row**: each eligible option
has a certified local cap realization with a common outside word and common
boundary signature, different cell slots have disjoint live supports, every
mixed/global row is invariant under those common signatures, and choosing at
most one option per slot makes the complete local-plus-global maximal-word
systems compose.  This hypothesis is what separates an actual compiler
atlas from an abstract eligibility graph.

### Theorem 5.1 (convex safe-cut Hall criterion)

Under the private composition row, the residual demands admit a simultaneous
common-Q completion if and only if, for every interval of slots `[i,j]`,

\[
       \left|\{u\in D:N(u)\subseteq[i,j]\}\right|\le j-i+1. \tag{5.3}
\]

If the family of neighborhoods `N(u)` is laminar, it is enough to check

\[
       \left|\{u\in D:N(u)\subseteq J\}\right|\le |J|      \tag{5.4}
\]

only for distinct neighborhoods `J=N(u)`.

#### Proof

The private composition row reduces simultaneous feasibility to an ordinary
matching of demands to slots.  Necessity of (5.3) is Hall's inequality.
If Hall fails for a demand set `A`, the union of its interval neighborhoods
is a disjoint union of slot intervals `J_1,...,J_k`.  Since each `N(u)` is
itself an interval, it lies wholly in one component.  Partitioning `A`
accordingly, some component has more assigned demands than slots; all their
neighborhoods are contained in that `J_i`, violating (5.3).  Hence (5.3) is
sufficient.

If the neighborhoods are laminar, the maximal neighborhoods contained in a
violating interval are disjoint.  Their demand counts sum to more than their
total size, so one maximal neighborhood violates (5.4).  \(\square\)

Convexity without the private common-Q composition row is insufficient:
two individually legal target options may screen the same source position
to disjoint nonempty letters, emptying it when selected together.  The exact
global fallback is to append the selected assignment rows to `mathcal R` and
test (2.3).

The smallest such failure has three live positions in physical order
`q<p<r`, caps
`C_p={a,b}`, `C_q={a}`, `C_r={b}`, and two distinct physical slots supported
on `{p,q}` and `{p,r}`.  Assigning target `{a}` to the first slot alone is
feasible, as is assigning `{b}` to the second slot alone.  The two-slot Hall
graph has a perfect matching.  Joint selection, however, screens `p` by
`{a} cap {b}=emptyset`.  Thus even a disjoint *cell* assignment is not a
common-Q certificate when its live source supports overlap.

## 6. A sufficient simultaneous MQP theorem

### Corollary 6.1 (laminar/convex fresh-`MQP` bridge)

The rotated order gives a valid protected two-ray host if there is a cut, an
owner assignment and a residual assignment with all of the following
properties.

1. **Owner rethread:** the row system contains one prescribed occurrence of
   every middle owner and `C` explicitly labelled allowed repeat cells, as in
   Corollary 2.2.  Any q1, residence, topology or upper conditions required
   of this chronology are present as additional exact rows.
2. **Seam cap:** the system contains the singleton `Z,T` rows and both
   coatom ray chains.
3. **Protected bank:** every retained cut-avoiding address selected by
   Theorem 4.1 or Corollary 4.2 is inserted with its required target as an
   exact row.  Cut avoidance is not used to infer its value.
4. **Residual bank:** after reserving owner, seam, task and retained cells,
   every casualty is assigned to an allowed free cell.  This assignment is
   either literal in a fixed baseline word, or is chosen by the private
   convex/laminar atlas of Theorem 5.1.
5. **One final cap:** after the residual rows have been selected and added,
   the complete combined row family passes the maximal-word test (2.3).
   Under the private composition hypothesis in item 4, this last test is
   already part of that hypothesis; without privacy it must be run explicitly.

Then one nonzero source word in the order `M Q P` realizes the prepared
`Z,T` host and the complete protected lower assignment.  If the external
owner, q1, residence and upper rows were included in (2.3), they hold in the
same word.

#### Proof

Choose the residual matching first; Theorem 5.1 proves that choice exists on
the private convex/laminar face.  Form the complete row family containing
the owner, seam, protected and selected residual equalities.  Item 5 and
Theorem 2.1 then produce one word realizing all of them simultaneously.
Corollary 2.2 gives the owner row, while the singleton and ray rows give the
seam host.  No value is imported from the old word without appearing in the
final maximal-word system.  \(\square\)

For comparison, if the final source word is literally `rho(W)` and (1.3)
holds, then Lemma 1.1 and Theorem 4.1 do transport values directly.  This is
the exceptional literal-rotation face ruled out asymptotically for the
prepared tails by Theorem 1.4; it is not the fresh recompilation proof above.

## 7. Proved boundary

The endpoint wrap has removed the **native-X source-letter** obstruction.
It has not removed:

* the `h`-window owner-collar exchange (1.1)--(1.3);
* the endpoint-local fixed-owner cut bound (1.8), or the stronger prepared-
  tail owner no-go (1.11);
* mixed-row positive-cover failures at `Z,T`;
* a cut whose protected witness banks cover every allowed gap; or
* nonprivate cross-option common-Q conflicts.

Accordingly the next genuine construction theorem is not “rotate a completed
word.”  For fixed additive slack, Theorem 1.4 rules that route out for the
prepared tails once `d` grows.  The surviving statement is: use `M Q P` only
as a fresh cap order, choose the owner rethread and lower assignment jointly,
and enforce (2.3), (4.2) and the residual interval cuts (5.3).  The present
note gives exact finite certificates and a laminar/convex sufficient theorem,
but does not prove that this fresh all-`d` recompile exists.
