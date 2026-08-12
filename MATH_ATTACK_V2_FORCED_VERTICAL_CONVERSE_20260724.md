# Second-wave V: a partial converse to endpoint-throughput forced verticality

Date: 2026-07-24

## 1. Result and scope

This note proves a finite partial converse to the endpoint-throughput theorem.
The converse has two complementary forms.

1. **Flag-preserving form.**  Suffix flags at different endpoints of one
   literal word are not independent flags.  They are prefix flags of one
   canonical last-occurrence ordered-partition trajectory, and consecutive
   states are related by the exact arbitrary-mask move-to-front operation.
   If only `b` endpoints fail to be saturated on a prescribed rank band,
   then every represented band mask which is absent from the good-endpoint
   support can be assigned to one of those `b` endpoints.  All masks assigned
   to one endpoint form one nested partial flag.  Thus the residual repair is
   compressed into at most `b` vertical objects even when the sum of the
   rankwise defects is as large as the band width times `b`.

2. **Canonical-refactor form.**  On every consecutive run of lower-depth-
   `H` active endpoints, multi-coordinate changes of the middle prefix can be
   refined into Johnson changes.  After a proved loop-label scheduling step,
   and provided `m>=3H+1`, this refined chronology has a literal lower-band
   MTF realization of length

   \[
   K+E+H
   \]

   and a literal two-sided realization of length

   \[
   K+E+2H,
   \]

   where the two-sided form also assumes `k-m>=H`.  Here `K` is the number
   of original active states and

   \[
   E=\sum_i\bigl(|T_{i+1}\setminus T_i|-1\bigr)_+
   \]

   is the exact turnover-refinement excess.  Over `c` runs the corresponding
   lengths are `K+E+cH` and `K+E+2cH`.

The first form preserves the original deep supports but may require a
rank-`U` recency reset, as large as `U-1` entries beyond the first state, if a
bad gap is physically cut.  The second form has an `H`-scale reset but changes
the flags and therefore does not inherit the original lower/upper support
bounds.  This separation is essential.

All theorems below are finite.  No probabilistic, computational, or
asymptotic existence input is used.  The final Gaussian corollaries merely
specialize the finite inequalities.

The result is a structural converse for a word or an MTF trajectory already
in hand.  It does not construct an exact wreath factor, prove MWB, prove
labelled common-owner synchronization, or prove the coefficient-one OR
conjecture.  In particular, endpoint throughput by itself does not force
Gaussian-depth activity; activity through `H=Theta(sqrt(m))` is an additional
hypothesis here.

## 2. Canonical recency states

Let

\[
\mathcal A=(A_1,\ldots,A_n),\qquad
\varnothing\ne A_i\subseteq[k],
\]

be a literal OR word.  For `x in [k]` and `j>=1`, define its last occurrence
time

\[
\lambda_j(x)=\max\bigl(\{i\le j:x\in A_i\}\cup\{0\}\bigr).
\]

Group coordinates with equal positive last-occurrence time and list the
nonempty groups in decreasing order of that time.  Coordinates with
`lambda_j(x)=0`, if any, form one final unseen block.  The resulting ordered
partition is denoted by

\[
\Pi_j=(B_{j,1},B_{j,2},\ldots).
\]

For an ordered partition `Pi=(B_1,B_2,...)` and a nonempty mask `X`, write

\[
M_X(\Pi)=(X,B_1\setminus X,B_2\setminus X,\ldots),
\tag{2.1}
\]

with empty blocks deleted.

### Theorem 2.1 (exact recency/endpoint equivalence)

For every endpoint `j`:

1. the distinct suffix unions ending at `j` are exactly the prefix unions of
   `Pi_j` which stop before the unseen block;
2. one has the exact recurrence

   \[
   \boxed{\Pi_{j+1}=M_{A_{j+1}}(\Pi_j).}
   \tag{2.2}
   \]

Consequently, if the suffix-union chain at `j` contains one set of every
rank `L,L+1,...,U`, those sets are unique and form a saturated flag

\[
S_{j,L}\subset S_{j,L+1}\subset\cdots\subset S_{j,U},
\qquad |S_{j,r}|=r,
\tag{2.3}
\]

inside the single state `Pi_j`.  Flags at consecutive active endpoints are
therefore consecutive states of one genuine arbitrary-mask MTF trajectory.

#### Proof

For a suffix starting at `i`,

\[
\bigcup_{t=i}^j A_t
=\{x:\lambda_j(x)\ge i\}.
\]

As `i` moves left, these are precisely the unions of the first several
positive-last-occurrence blocks of `Pi_j`.  Conversely, if `t` is the
last-occurrence time of the last block in a prefix, the suffix beginning at
`t` has exactly that prefix union.  This proves the first assertion.

Appending `A_{j+1}` gives every coordinate of that mask the newest common
last-occurrence time and preserves the relative order of all other
last-occurrence blocks.  This is exactly (2.2).

All suffix unions at one endpoint form a chain.  Equal-cardinality members
of a chain are equal, so the member of each active rank is unique.  Between
two consecutive active ranks the ordered partition must add a block of size
one.  This proves (2.3).  ∎

Thus the weak correlated-flag converse is exact: **endpoint activity in a
literal word already is MTF correlation.**  What is not automatic is
distinct support, Johnson geometry, or a cheap restart after the inherited
recency state is discarded.

## 3. Good endpoints and vertically compressed residual repair

Fix integers

\[
1\le L\le U\le k.
\]

Call `j` **good** if its suffix chain is active at every rank from `L` through
`U`.  Let

\[
G=\{j:j\text{ is good}\},\qquad
B=[n]\setminus G,\qquad \beta=|B|.
\]

Suppose target families

\[
\mathcal F_r\subseteq\binom{[k]}r,
\qquad L\le r\le U,
\]

are represented by the word.  Put

\[
\mathcal C_r(G)=\{S_{j,r}:j\in G\}.
\]

### Theorem 3.1 (owner support and vertical residual compression)

For every `r in [L,U]`,

\[
\boxed{
|\mathcal F_r\setminus\mathcal C_r(G)|\le\beta.
}
\tag{3.1}
\]

More strongly, all masks in

\[
\bigsqcup_{r=L}^U
\bigl(\mathcal F_r\setminus\mathcal C_r(G)\bigr)
\]

can be assigned to at most `beta` bad endpoints so that the masks assigned to
each one endpoint form a nested partial flag of actual suffix unions at that
endpoint.

In particular, the residual masks across the entire band are carried by at
most `beta` literal endpoint chains, even though the scalar estimate obtained
by summing (3.1) is only

\[
\sum_{r=L}^U
|\mathcal F_r\setminus\mathcal C_r(G)|
\le \beta(U-L+1).
\tag{3.2}
\]

#### Proof

Take a target `S` which is absent from the good support at its rank.  Every
witness interval for `S` must end at a bad endpoint: if a witness ended at a
good endpoint `j`, the unique rank-`|S|` suffix union there would be `S`,
placing it in `C_|S|(G)`.

Choose one witnessing right endpoint for every residual target.  At a fixed
rank two distinct targets cannot be assigned to the same endpoint, because
the suffix unions at that endpoint form a chain and contain at most one
distinct set of a fixed cardinality.  Hence at most `beta` targets of any
one rank are residual, proving (3.1).

Across different ranks, every target assigned to the same endpoint is a
prefix union of that endpoint's single recency state.  The assigned targets
are therefore nested.  This proves the stronger partial-flag assertion and
(3.2).  ∎

### Corollary 3.2 (distinct good middle owners)

If `m in [L,U]` and every `m`-set is represented, then at least

\[
\boxed{\binom{k}{m}-\beta}
\tag{3.3}
\]

distinct middle masks have distinct good owner endpoints, each carrying a
saturated `[L,U]` flag.  All these owner flags occur on the one literal MTF
trajectory (2.2).

#### Proof

Apply (3.1) with `F_m=binom([k],m)`.  Distinct middle masks at good endpoints
automatically have distinct endpoints.  ∎

There is a second, genuinely physical correlation when activity is available
at both ends of selected middle witnesses.  Say a position is **left-good**
on `[L,m]` if the interval unions beginning there contain one set of every
rank `L,...,m`; right-good has the suffix meaning already used above.

### Theorem 3.3 (two-ended activity gives a touching biflag forest)

Let

\[
W=\binom{k}{m},\qquad n=W+d,
\]

and suppose the word represents every `m`-set.  Choose one witness interval
`I_T` for each middle set `T`.  Let `beta_L` and `beta_R` be the numbers of
positions which are not left-good and not right-good, respectively, on
`[L,m]`, where `1<=L<m`.

Then the selected middle masks support a directed linear forest with at
least

\[
\boxed{W-d-\beta_L-\beta_R}
\tag{3.4}
\]

edges (read as a vacuous lower bound if negative), and hence at most

\[
\boxed{d+\beta_L+\beta_R}
\tag{3.5}
\]

components.  Every forest edge has the form

\[
T^-\longrightarrow T^+
\]

at one physical junction `p`, where the selected witness of `T^-` ends at
`p`, the selected witness of `T^+` begins at `p`, and

\[
A_p\subseteq T^-\cap T^+,
\qquad |A_p|\le L.
\tag{3.6}
\]

The source carries a saturated right flag and the target a saturated left
flag, both literally based at the common entry `A_p`.

#### Proof

Selected intervals of distinct equal-rank masks cannot be nested: physical
containment would imply containment of their OR values, and equal
cardinality would then force the masks to be equal.  Their left endpoints
are therefore all distinct, as are their right endpoints.  If `E_L,E_R`
are the two endpoint sets, then

\[
|E_L\cap E_R|\ge2W-n=W-d.
\]

At a common endpoint `p`, let `I^-` be the selected interval ending there
and `I^+` the selected interval beginning there.  If exactly one were the
singleton `[p,p]`, its rank-`m` value `A_p` would be contained in the other
rank-`m` value, forcing equality and contradicting the one-witness-per-mask
selection.  Thus either both are the same singleton witness or both are
nonsingleton.

At a position which is good from either side down to rank `L<m`, the entry
`A_p` is contained in a rank-`L` interval union, so `|A_p|<=L`.  The common
singleton case, which would have `|A_p|=m`, is impossible.  Excluding the at
most `beta_L+beta_R` endpoints which are not good from both sides leaves at
least (3.4) nonsingleton junctions.

Direct an edge from the interval ending at a junction to the interval
beginning there.  Each selected interval has one left and one right endpoint,
so indegree and outdegree are at most one.  Along a directed path the
physical junction strictly increases, excluding cycles.  The graph is a
linear forest.  Its number of components is `W-|E|`, proving (3.5), and
(3.6) follows because the common physical entry belongs to both witness
unions.  The two endpoint flags are literal by definition.  ∎

The forest need not be a Johnson forest: (3.6) gives no lower bound on
`|A_p|`, so the two middle masks may exchange many coordinates.  Nor do its
possibly interlacing witness intervals immediately give a short
concatenation.  The theorem supplies a correlated biflag skeleton, not the
missing low-reset support theorem.

Theorem 3.1 is the promised nonsummable-defect repair statement.  It does not
say that the `beta` partial flags can be replaced by `beta` isolated literal
entries after the original chronology is destroyed.  It says that retaining
the bad endpoint states retains all those repairs with one physical endpoint
per vertical chain.

## 4. Exact bridge-versus-reset accounting

The original word itself realizes all good flags with length `n` and zero
reset.  A nontrivial question arises only when the relevant span is restarted
independently or bad gaps are cut.

### Lemma 4.1 (top-rank prefix equivalence)

Say two ordered partitions are **`U`-prefix equivalent** if they have the
same initial block string through a common prefix whose union has cardinality
at least `U`.  If `Pi` and `PiHat` are `U`-prefix equivalent, then for every
nonempty `X`,

\[
M_X(\Pi)\quad\text{and}\quad M_X(\widehat\Pi)
\]

are `U`-prefix equivalent.  Therefore every prefix set of rank at most `U`
which occurs in one updated state occurs with the same value in the other.

#### Proof

Let `C_1,...,C_t` be the common initial blocks and let their union be `C`,
with `|C|>=U`.  After the common update, both states begin with the same
nonempty blocks in

\[
X,\ C_1\setminus X,\ldots,C_t\setminus X.
\]

Their union is `X\cup C`, whose size is at least `U`.  Thus no prefix of
rank at most `U` can depend on a later, noncommon tail block.  ∎

### Lemma 4.2 (exact prefix reset)

Suppose

\[
\Pi=(B_1,\ldots,B_t,\ldots),
\qquad
|B_1\cup\cdots\cup B_t|=U.
\]

From an arbitrary inherited state, the `t` updates

\[
B_t,B_{t-1},\ldots,B_1
\tag{4.1}
\]

recreate exactly the first `t` blocks of `Pi`.  The tail need not be reset.

If `Pi` exposes every rank `L,...,U`, and the rank-`L` prefix has block depth
`h`, then

\[
\boxed{t=h+(U-L),}
\tag{4.2}
\]

and consequently

\[
1+(U-L)\le t\le U.
\tag{4.3}
\]

#### Proof

The masks in (4.1) are disjoint.  Reverse emission puts them at the front in
the order `B_1,...,B_t`, independently of the old tail.

After the rank-`L` prefix, saturation at consecutive ranks forces exactly
`U-L` further singleton blocks.  This gives (4.2).  The rank-`L` prefix is
nonempty, so `h>=1`; all blocks are nonempty and their union has size `U`, so
`t<=U`.  ∎

Decompose the good endpoint set into maximal physical runs

\[
[a_1,c_1],\ldots,[a_p,c_p],
\]

and for `i>=2` put

\[
\ell_i=a_i-c_{i-1}-1.
\]

Let `t_i` be the block depth of the rank-`U` prefix at the first state of run
`i`, and set

\[
e_i=t_i-1.
\]

Assume in the remainder of this section that `G` is nonempty, so `p>=1`.
If `G` is empty, the extraction statements are vacuous.

### Theorem 4.3 (sharp explicit bridge/reset ledger)

For each bad gap independently, either retain all its updates or cut before
the next good run and perform the prefix reset (4.1).  The resulting literal
word reproduces every original good flag and has length

\[
\boxed{
|G|+e_1+
\sum_{i=2}^p
\begin{cases}
\ell_i,&\text{if gap }i\text{ is bridged},\\
e_i,&\text{if gap }i\text{ is cut}.
\end{cases}}
\tag{4.4}
\]

In particular, choosing the cheaper policy at every gap gives

\[
\boxed{
L_{\rm hybrid}
=|G|+e_1+\sum_{i=2}^p\min\{\ell_i,e_i\}
\le n+U-1.
}
\tag{4.5}
\]

Cutting every bad gap gives a disjoint union of saturated original runs of
length

\[
\boxed{
L_{\rm cut}=|G|+\sum_{i=1}^p e_i
\le |G|+p(U-1),
\qquad p\le\beta+1.
}
\tag{4.6}
\]

#### Proof

Within one good run, after its first state has been reset, every later state
is obtained by replaying one original update.  Lemma 4.1 shows that the
rank-`U` prefix agreement, and hence every required rank at most `U`, survives
all those updates.

Between two runs, retaining a gap of `ell_i` bad endpoints uses `ell_i+1`
updates to reach the next good state.  One of these is the baseline entry for
that good state, so the excess is `ell_i`.  Cutting instead initializes the
next first state with `t_i` entries, an excess of `t_i-1=e_i`.  The first run
has the same reset excess `e_1`.  This proves (4.4).

By (4.3), `e_i<=U-1`.  The internal bad gaps contain at most `beta` endpoints,
so

\[
|G|+e_1+\sum_{i=2}^p\min\{\ell_i,e_i\}
\le |G|+(U-1)+\beta\le n+U-1.
\]

This proves (4.5); summing `e_i<=U-1` proves (4.6).  ∎

For the lower band `[m-H,m]`,

\[
t_i=h_i+H,
\qquad H+1\le t_i\le m,
\tag{4.7}
\]

while for the two-sided band `[m-H,m+H]`,

\[
t_i=h_i+2H,
\qquad 2H+1\le t_i\le m+H.
\tag{4.8}
\]

Thus an isolated flag can be initialized with `H+1` or `2H+1` entries by
coarsening its lower member into one block, but this coarser state need not
compose with the next prescribed update.  The inherited lower-head recency
depth `h_i` is real data, not an artifact of the proof.

## 5. Forced dwell and almost-Johnson motion

Now specialize to a middle prefix of rank `m` and assume every endpoint under
discussion is active at ranks

\[
m-H,m-H+1,\ldots,m,
\qquad 1\le H\le m-1.
\]

Write `T_j` for the rank-`m` prefix of `Pi_j`, and let `kappa_j` be its block
depth.

### Lemma 5.1 (forced coordinate dwell)

Suppose transition `a` refreshes a coordinate `x` into the first block, `x`
remains in the middle prefix, and transition `b` is the first later transition
after which `x` is outside the middle prefix.  If the state after transition
`b` is lower-`H` active, then

\[
\boxed{b-a\ge H+1.}
\tag{5.1}
\]

#### Proof

After the last refresh of `x`, its block is first.  Every later update not
containing `x` inserts at most one new block before its residual block.
Immediately before departure its residual block therefore has position at
most the elapsed number of transitions.

In the state after departure, the middle prefix contains at least one block
to reach rank `m-H` and then `H` singleton blocks to reach rank `m`.  Its
block depth is at least `H+1`.  The residual block containing `x` lies after
that prefix, hence at position at least `H+2` in the updated state, or at
least `H+1` in the old residual order.  This forces at least `H+1`
transitions since the last refresh, and a fortiori since transition `a`.  ∎

### Theorem 5.2 (block-depth potential)

If consecutive active states have distinct middle prefixes `T_j` and
`T_{j+1}`, then

\[
\boxed{\kappa_{j+1}\le\kappa_j.}
\tag{5.2}
\]

Equality in (5.2) forces `T_j` and `T_{j+1}` to be Johnson adjacent.  Hence
every distinct non-Johnson transition drops the middle block depth by at
least one.

A consecutive active run in which every consecutive pair of middle prefixes
is distinct therefore contains at most

\[
\boxed{m-H-1}
\tag{5.3}
\]

non-Johnson transitions.

#### Proof

Write

\[
\Pi_j=(B_1,B_2,\ldots),
\qquad P_q=B_1\cup\cdots\cup B_q,
\qquad T_j=P_p.
\]

Let the update be `X`.  Every prefix of the new state has the form

\[
X\cup P_q
\]

for the last old residual block used, with `q=0` allowed.  If the new
rank-`m` prefix is distinct from `T_j`, then `q<p`: for `q>=p` it contains
`P_p=T_j`, and equal cardinality would force equality.  Its new block depth
is at most

\[
1+q\le p=\kappa_j,
\]

proving (5.2).

Equality requires `q=p-1` and no empty residual among the first `p-1` old
blocks.  Activity at rank `m-1` forces the last middle block `B_p` to be a
singleton and `P_{p-1}` to have rank `m-1`.  The new middle prefix is
`P_{p-1}` plus exactly one new coordinate, so it differs from `T_j` by one
deletion and one insertion.  It is a Johnson neighbor.

Finally,

\[
H+1\le\kappa_j\le m.
\]

Every non-Johnson distinct transition decreases this integer by at least
one, proving (5.3).  ∎

If there are `c` maximal active runs and `r` consecutive equal-middle
transitions inside them, cutting at those `r` transitions produces `c+r`
distinct-transition segments.  Thus

\[
\#\{\text{distinct non-Johnson transitions}\}
\le(c+r)(m-H-1).
\tag{5.4}
\]

If all retained middle labels are globally distinct, cutting the repeats and
the non-Johnson transitions produces a Johnson linear forest with at most

\[
(c+r)(m-H)
\tag{5.5}
\]

components.  Without global distinctness, (5.5) is a path decomposition in
occurrence space, not a graph-theoretic forest on set labels.  If the
duplicate excess is `rho`, deleting all but one occurrence of each repeated
middle label increases the run count by at most `rho` and gives a genuine
forest with at most `(c+rho)(m-H)` components.

## 6. Turnover-refactored literal MTF core

The preceding theorem controls how often a distinct non-Johnson change can
occur, but not how many coordinates one such change turns over.  The next
theorem records the exact price of refining all such changes.

Let

\[
\Pi_0,\Pi_1,\ldots,\Pi_{K-1}
\]

be one consecutive lower-`H` active MTF run, with updates `X_i` and middle
prefixes `T_i`.  Put

\[
d_i=|T_{i+1}\setminus T_i|,
\qquad
E=\sum_{i=0}^{K-2}(d_i-1)_+.
\tag{6.1}
\]

### Theorem 6.1 (canonical turnover refactor)

Assume

\[
\boxed{m\ge3H+1.}
\tag{6.2}
\]

There is a refined Johnson/loop chronology containing

\[
T_0,T_1,\ldots,T_{K-1}
\]

in order and having exactly `K+E` middle-state occurrences.  It admits:

1. a literal lower-band MTF word exposing every rank `m-H,...,m` at every
   refined state, of exact length

   \[
   \boxed{K+E+H};
   \tag{6.3}
   \]

2. a literal two-sided MTF word exposing every rank `m-H,...,m+H` at every
   refined state, of exact length

   \[
   \boxed{K+E+2H}.
   \tag{6.4}
   \]

   This part also assumes `k-m>=H`, so the upper band and the `H` initial
   complementary markers exist.

For `c` disjoint active runs containing `K` original states in total, with
the sum of (6.1) denoted again by `E`, the lengths are

\[
\boxed{K+E+cH}
\qquad\text{and}\qquad
\boxed{K+E+2cH}.
\tag{6.5}
\]

The original endpoint flags need not be preserved.

#### Proof, Step 1: turnover identity

The new middle prefix has the form `X_i union P`, where `P` is an old
residual prefix.  Since the old middle set is itself a prefix of rank `m`,
`P` cannot pass beyond it.  Therefore

\[
\boxed{T_{i+1}\setminus T_i=X_i\setminus T_i.}
\tag{6.6}
\]

In particular the departure and arrival sets have the same size `d_i`.

#### Step 2: Johnson refinement and separation

If `d_i>0`, pair the members of

\[
T_i\setminus T_{i+1}
\quad\text{and}\quad
T_{i+1}\setminus T_i
\]

arbitrarily and perform the `d_i` exchanges successively.  If `d_i=0`, keep
one formal loop.  The number of refined edges is

\[
R=\sum_i\max\{1,d_i\}=(K-1)+E,
\]

so the refined chronology has `R+1=K+E` states.

If a coordinate inserted in original transition `a` has its first later
exit in original transition `b`, Lemma 5.1 gives `b-a>=H+1`.  Even if it is
inserted in the last refined edge of transition `a` and deleted in the first
refined edge of transition `b`, every intervening original transition
contributes at least one refined edge.  Its refined residence is still at
least `H+1`.  Hence no genuine inserted coordinate is deleted within the
next `H` refined edges.

#### Step 3: scheduling formal loops

Write a genuine refined edge as

\[
T_{j+1}=T_j-\{p_j\}+\{q_j\}.
\]

At a formal loop choose `p_j=q_j in T_j`.  Process loop positions from left
to right.  At loop `j` use the candidate set

\[
C_j=\bigcap_{s=\max(0,j-H)}^jT_s.
\tag{6.7}
\]

At most `H` Johnson changes occur in this window, so

\[
|C_j|\ge m-H.
\]

Exclude the preceding `H` chosen departure labels and the departure labels
of the next `H` genuine edges.  There are at most `2H` exclusions, and (6.2)
leaves an available coordinate.

A recent genuine entrant is automatically absent from `C_j`, because its
pre-entry middle state occurs in the intersection.  Future loops avoid the
current choice among their preceding labels.  Together with the genuine
residence bound, this proves that no inserted or formal-loop coordinate is
deleted within `H` refined edges.

It also proves the two properties needed below.  A genuine departure at
time `j+s`, `s<=H`, must already belong to `T_j`: otherwise it would have
entered during those `s` edges and then departed too soon.  A loop label at
time `j+s` belongs to `T_j` by its intersection rule.  Two genuine
departures within `H` edges cannot have the same label, because after the
first departure that coordinate would have to re-enter before the second;
the loop exclusions handle every case involving a loop.

Choose `H` further terminal **dummy departure labels** by the same rule.
They are labels only; they are not extra emitted states or updates.  We
obtain, for every actual refined transition `j`,

\[
p_j,p_{j+1},\ldots,p_{j+H}
\quad\text{distinct and contained in }T_j.
\tag{6.8}
\]

For the final state only the `H` dummy labels needed below are asserted.
Formally, while choosing them one may repeat the final middle state in the
intersection rule; these repetitions are scheduling devices and contribute
no word entries.

#### Step 4: canonical lower states

For every refined state define

\[
L_j=T_j\setminus\{p_j,p_{j+1},\ldots,p_{j+H-1}\}.
\tag{6.9}
\]

Then

\[
L_{j+1}
=(L_j\setminus\{p_{j+H}\})\cup\{q_j\}.
\tag{6.10}
\]

Use the leading ordered-partition state

\[
\widehat\Pi_j=
\bigl(
L_j,\{p_{j+H-1}\},\ldots,\{p_j\},\Theta_j
\bigr).
\tag{6.11}
\]

Here `Theta_0` may be any ordered partition of `T_0^c`; the recurrences below
then keep `Theta_j` an ordered partition of `T_j^c`.

For a genuine edge set

\[
\Theta_{j+1}=(\{p_j\},\Theta_j\setminus\{q_j\}),
\tag{6.12}
\]

whereas at a loop `p_j=q_j` set

\[
\Theta_{j+1}=\Theta_j.
\tag{6.13}
\]

Direct block subtraction using (6.10) gives

\[
\boxed{
\widehat\Pi_{j+1}=M_{L_{j+1}}(\widehat\Pi_j).
}
\tag{6.14}
\]

The loop recurrence (6.13) is necessary: on a loop `p_j` is refreshed into
the new lower core and never enters the complement tail.

Initialize (6.11) by emitting

\[
\{p_0\},\{p_1\},\ldots,\{p_{H-1}\},L_0.
\tag{6.15}
\]

These `H+1` entries create the desired leading blocks in reverse recency
order.  Each of the remaining `K+E-1` refined states costs one update
`L_{j+1}`.  The total is (6.3).

#### Step 5: two-sided states

Choose `H` distinct coordinates

\[
z_1,\ldots,z_H\in T_0^c.
\]

Before (6.15), emit

\[
\{z_H\},\ldots,\{z_1\}.
\tag{6.16}
\]

The initial state now has `H` leading complementary singleton blocks after
the middle prefix.  Under a genuine transition, (6.12) prepends the departed
`p_j`; if `q_j` removes one of the first `H` complementary singletons, the
new `p_j` replaces it.  If `q_j` lies later, there are `H+1` leading
singletons and the first `H` still expose the required ranks.  A loop leaves
the tail unchanged.  Hence every state exposes ranks through `m+H`.

The initialization uses `2H+1` entries and the later transitions use
`K+E-1`, proving (6.4).  Summing componentwise proves (6.5).  The residual
tail beyond rank `m+H` need not be emitted: it may remain arbitrarily
partitioned because every required prefix stops before it.  ∎

The `H+1` and `2H+1` initialization counts are sharp for a from-scratch or
uncontrolled-tail guarantee for this central band: one endpoint must expose
that many distinct consecutive-rank suffix unions.  They are not lower
bounds when a favorable inherited state is already present.

The audited adaptive-MTF length `K+2H+1` remains exact for its stronger
declared policy, which emits a final residual block and initializes the full
state.  Formula (6.4) initializes only the prefix through rank `m+H`; its
uncontrolled residual stays in the inherited or unseen tail.  Thus the net
per-component toll here is `2H`, not `2H+1`, without contradicting that
full-state ledger.

### Corollary 6.2 (finite activity-only turnover bound)

Let `c` be the number of maximal active runs and `r` the number of
consecutive equal-middle transitions inside them.  Then

\[
\boxed{
E\le(c+r)(m-H-1)^2.
}
\tag{6.17}
\]

#### Proof

At an active successor endpoint, the first update block lies inside the
rank-`m-H` prefix.  Thus

\[
d_i=|X_i\setminus T_i|\le |X_i|\le m-H.
\]

Only transitions with `d_i>=2` contribute to `E`; they are distinct
non-Johnson transitions and each contributes at most `m-H-1`.  Equation
(5.4) bounds their number by `(c+r)(m-H-1)`.  ∎

### Corollary 6.3 (near-width owner core with explicit defects)

Let the ground set have size `2m`, put

\[
W=\binom{2m}{m},
\]

and let a word of length

\[
n=W+d
\]

represent every middle set.  Suppose exactly `b` endpoints fail lower-`H`
activity, assume `b<W`, and assume `m>=3H+1`.  Then the good endpoints admit
a two-sided literal MTF core which:

1. contains at least `W-b` distinct original middle masks;
2. has length at most

\[
\boxed{
W+d-b
+(b+d+1)(m-H-1)^2
+2H(b+1).
}
\tag{6.18}
\]

The lower-only version replaces the last term by `H(b+1)`.

#### Proof

There are `K=n-b` good states and at most `c=b+1` good runs.  By Corollary
3.2 their middle support has size at least `W-b`.  Hence the duplicate
occurrence excess among good centers is at most

\[
(n-b)-(W-b)=d.
\]

In particular the number `r` of consecutive equal-center transitions is at
most `d`.  Apply (6.17) and then (6.5).  ∎

For any fixed `A>0` and

\[
H=\lfloor A\sqrt{2m}\rfloor
\]

(equivalently `H=Theta_A(sqrt(m))`), condition (6.2) holds for all sufficiently
large `m`.  If

\[
\boxed{m^2(b+d)=o(W),}
\tag{6.19}
\]

then (6.18) is `W+o(W)`.  This is a genuine coefficient-one **MTF core on
middle owners**, but not yet a coefficient-one central-band cover: its new
lower and upper flags may collide.

For the refactored two-sided core, let `\mathcal V_0` be its middle support
and `\mathcal V_q^-`, `\mathcal V_q^+` its distinct canonical depth-`q`
supports.  Literal
completion gives the exact sufficient ledger

\[
\begin{aligned}
L_{\rm band}\le{}&K+E+2cH+(W-|\mathcal V_0|)\\
&+\sum_{q=1}^H
\left[
N_q-|\mathcal V_q^-|
+N_q-|\mathcal V_q^+|
\right],
\end{aligned}
\tag{6.20}
\]

where

\[
N_q=\binom{2m}{m-q}.
\]

**UNPROVED SUPPORT STEP.**  Nothing in endpoint activity, (6.17), or the
turnover refinement proves that the last line of (6.20) is `o(W)`.  This is
the precise support geometry still missing from the canonical-refactor
route.

## 7. Gaussian specialization of the flag-preserving theorem

Let `k=2m`, `W=binom(2m,m)`, fix `A>0`, and take either

\[
[L,U]=[m-H,m]
\quad\text{or}\quad
[L,U]=[m-H,m+H],
\qquad H=\lfloor A\sqrt{k}\rfloor.
\]

Consider a sequence of words with

\[
n=(1+o(1))W
\]

which represent the prescribed central band, and suppose

\[
\beta=o(W)
\]

endpoints fail full activity on that band.  Then Theorems 2.1 and 3.1 give:

1. one literal MTF chronology of length `n=W+o(W)` carrying all good flags;
2. at least `W-o(W)` distinct middle owner masks on that chronology;
3. at most `beta=o(W)` vertically correlated bad-endpoint partial flags
   carrying every band target absent from the good support;
4. an independently restartable trimmed realization of the good flags of
   length at most

   \[
   n+U-1=W+o(W).
   \]

No hypothesis of the form

\[
\sum_{r=L}^U
|\mathcal F_r\setminus\mathcal C_r(G)|=o(W)
\]

is needed for the vertical compression statement.  If the bad endpoints are
discarded and the holes are instead appended rank by rank, the weaker scalar
bound `beta(U-L+1)` reappears.

This is the strongest converse proved here from the stated
premise: it constructs globally correlated flags and an exact vertical
repair geometry.  It remains conditional on Gaussian-depth activity.  The
audited endpoint-throughput estimate automatically gives almost-all endpoint
activity only when

\[
H\eta_m+H^3/m=o(1)
\]

for a word of length `(1+eta_m)W`; it does not reach `H=Theta(sqrt(m))`.

## 8. Sharp scope obstructions

### 8.1 Activity does not imply distinct middle support

Initialize a singleton recency state

\[
(\{x_1\},\{x_2\},\ldots,\{x_k\})
\]

and repeatedly update by `{x_1}`.  Every endpoint remains active at every
rank, but the state and every prefix value are constant.  Thus activity alone
does not imply even two distinct middle owners.

### 8.2 Activity does not imply Johnson adjacency

Start from the singleton order on `[2m]` with middle prefix

\[
T=\{1,\ldots,m\}.
\]

For any

\[
1\le t\le m-H,
\]

update by

\[
X=\{m+1,\ldots,m+t\}.
\]

Both the old and new states expose every rank from `m-H` through `m+H`, but
the new middle prefix is

\[
X\cup\{1,\ldots,m-t\},
\]

at Johnson distance `t` from `T`.  Thus a single fully active transition can
have turnover `m-H`, which is `Theta(m)` in the Gaussian regime.

### 8.3 A bad gap has no one-update shortcut in general

For singleton states,

\[
(1,2,3)
\xrightarrow{\{2\}}
(2,1,3)
\xrightarrow{\{3\}}
(3,2,1).
\]

No one mask sends `(1,2,3)` directly to `(3,2,1)`: the first block would
have to be `{3}`, after which the residual order is `(1,2)`, not `(2,1)`.
This is why (4.4) charges either the physical bridge or a reset.

### 8.4 Frozen updates can require a linear reset

Take the singleton state

\[
(1,2,\ldots,2m)
\]

and then update successively by

\[
\{m+1\},\{m+2\},\ldots,\{2m-H\}.
\]

At time `t` the middle prefix is

\[
T_t=\{m+1,\ldots,m+t\}
\cup\{1,\ldots,m-t\},
\]

and every state is active at every rank.  Any independent restart which
follows these same frozen updates and reproduces these middle prefixes must,
after the successive refreshed coordinates are removed from its inherited
blocks, realize the residual prefixes

\[
\{1,\ldots,r\}
\]

for every `H<=r<=m`.  These conditions force its initial relevant state to
have at least `m-H+1` blocks.  A fresh or uncontrolled-tail restart therefore
requires at least that many emitted reset entries; a favorable inherited
state may already contain some or all of them.  Here is the exact boundary
argument.  Put

\[
Q_t=\{m+1,\ldots,m+t\},\qquad R_t=\{1,\ldots,m-t\}.
\]

If `P_{a_t}` is the old block prefix used after the first `t` updates, then

\[
P_{a_t}\setminus Q_t=R_t.
\tag{8.1a}
\]

The prefix used at time `t-1` cannot contain the not-yet-updated coordinate
`m+t`, because the prescribed middle set at that time excludes it.  Hence
if `a_t>=a_{t-1}`, removing `Q_t` from `P_{a_t}` would still contain all of
`R_{t-1}`, contradicting (8.1a).  Therefore

\[
a_0>a_1>\cdots>a_{m-H}\ge1.
\]

The restart state has at least `m-H+1` relevant blocks.  Thus even singleton
updates and a Johnson middle chronology do not give
an `O(H)` reset when the updates are frozen.  The `H`-scale reset in Theorem
6.1 is obtained by replacing them with the canonical bulk updates
`L_{j+1}`.

### 8.5 Distinct owner flags alone do not control deep support

Fix `D\subseteq[2m]` with `|D|=H`.  For every middle set `S`, choose an
ordered deletion list of length `H` which includes all of `S\cap D` and then
uses fillers from `S\setminus D`.  Its depth-`H` lower member avoids `D`.
Choose an addition list of length `H` which includes all of `D\setminus S`
and then uses fillers outside `S\cup D`.  Its depth-`H` upper member contains
`D`.  If `s=|S\cap D|`, the two filler demands are `H-s` and `s`, while the
available pools have sizes `m-s` and `m-H+s`, respectively.  Thus `H<=m`
is exactly enough for both choices.

Each such two-sided flag is individually an honest ordered-partition state:
use the depth-`H` lower member as the first block, the deleted coordinates as
the next `H` singleton blocks in reverse order, the additions as the next
`H` singleton blocks, and an arbitrary residual tail.  Nevertheless each
signed depth-`H` support has size at most

\[
\binom{2m-H}{m-H},
\]

whereas the target layer has size

\[
N_H=\binom{2m}{m-H}.
\]

The ratio is

\[
\frac{\binom{2m-H}{m-H}}{N_H}
=\prod_{i=1}^H
\frac{m+i}{2m-H+i}
\le
\left(\frac12+\frac{H}{2m}\right)^H.
\tag{8.1}
\]

If `H/sqrt(m)->a>0`, then

\[
N_H/W\longrightarrow e^{-a^2},
\]

because

\[
\begin{aligned}
\log\frac{N_H}{W}
&=\sum_{i=0}^{H-1}
\left[
\log\left(1-\frac{i}{m}\right)
-\log\left(1+\frac{i+1}{m}\right)
\right]\\
&=-\frac{H^2}{m}+O\left(\frac{H^3}{m^2}\right).
\end{aligned}
\tag{8.2}
\]

while (8.1) tends to zero exponentially in `H`.  Thus either signed depth
can have

\[
(e^{-a^2}+o(1))W
\]

holes even though all `W` distinct middle centers own full individually
realizable flags.

This is an obstruction only after the common chronology is forgotten; it is
not asserted that the polarized states lie on one low-reset MTF tour.  It
pinpoints exactly why individual owner fibres are insufficient and why the
remaining support theorem must be jointly chronological.

## 9. Internally audited claims

The decisive steps were independently rederived adversarially.

1. **Recency extraction:** the suffix/prefix identity and the exact update
   (2.2) hold with tied last-occurrence blocks and an unseen tail.
2. **Prefix reset:** `U`-prefix equivalence is preserved even across inactive
   bridge states, because the common updated prefix has union `X\cup C` of
   size at least `U`.  Thus (4.4) does not hide a state-transversal
   assumption.
3. **Depth potential:** in the equality case of (5.2), rank-`m-1` activity
   really forces the last middle block to be a singleton.  The exact
   non-Johnson budget is `m-H-1`, not `m-H`.
4. **Turnover refactor:** the `H` right-boundary objects are dummy departure
   labels, not emitted loop states.  Counting them as states would falsely
   add `H` to (6.3)--(6.4).
5. **Loop recurrence:** the audited nonloop MTF recurrence does not by itself
   cover `p_j=q_j`; equation (6.13) is the required separate loop case.
6. **Initialization constants:** `H+1` and `2H+1` are sharp only for a fresh
   or uncontrolled-tail realization of the canonical prefix layout.  They
   are not claimed minimal from a favorable inherited state.
7. **Implication scope:** Theorem 3.1 preserves original supports, while
   Theorem 6.1 changes them.  Combining the first theorem's support bounds
   with the second theorem's reset bound would be invalid without a new
   support-preserving refactor lemma.

No unproved lemma is used in Theorems 2.1--6.3.  The only explicitly unproved
statement needed to turn the refactored core into a central-band universal
word is the support bound following (6.20).

## 10. Final theorem-level conclusion

The strongest valid partial converse is:

> **Partial converse.**
>
> Almost-all endpoint activity on a fixed band of an actual word already
> produces one globally correlated literal MTF flag trajectory.  Every band
> target absent from the good support is carried by one of the bad endpoint
> states, and all targets carried by the same bad state form one partial
> flag.  Thus the residual vertical-object count is the number of bad
> endpoints, not the sum of the rankwise defects.
>
> If the original updates are retained, the exact bridge/reset cost is
> (4.4).  If `m>=3H+1` and the updates may be canonically replaced, every
> lower-`H` active run has a literal lower core of length `K+E+H`.  When also
> `k-m>=H`, it has a literal two-sided core of length `K+E+2H`, with `E` the
> exact turnover excess.  Activity alone controls this excess only by (6.17)
> and does not control the new deep supports.

Therefore the endpoint-throughput geometry does force a genuine MTF core,
but in two noninterchangeable senses.  The remaining theorem is not local
verticality or reset legality.  It is a **support-preserving chronological
refactor**, or some alternative joint construction that simultaneously
retains Gaussian-depth support and attains the `H`-scale reset.
