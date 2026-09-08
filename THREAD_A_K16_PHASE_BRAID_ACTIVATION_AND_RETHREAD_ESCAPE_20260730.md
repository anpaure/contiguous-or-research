# The `k=16` phase braid: exact trace normal form and activation-capacity escape

Date: 2026-07-30

Status: theorem-level structural analysis.  This note treats the reported
top-bit trace as an input datum and proves what it does, and does not, imply.
It performs no search and makes no claim that the reported incumbent is a
universal word.

## 1. Frozen theorem boundary

Let `x` be the new coordinate and let

\[
 A=(A_1,\ldots,A_{6438})
\]

be the authenticated optimal `k=15` word.  The companion note

```text
THREAD_A_K16_TRIMMED_LIFT_THREE_DELETION_AND_BLOCK_FUSION_20260730.md
```

proves, with the first copy and central singleton fixed:

1. pure three-deletion is impossible;
2. one contiguous replacement block has old support `b>=3218`;
3. an arbitrary order-preserving mixed-tag tail rethread has support
   `s>=1610`, provided the old copy itself remains untagged;
4. a uniformly tagged tail cannot reach length `12873` even after a complete
   rewrite.

The hypothesis in item 3 is important: no letter of the old copy may gain
`x`.  The present note quantifies exactly how one such gain breaks the
rank-seven proof.

## 2. Exact binary normal form of the reported trace

The reported length-`12873` top-bit trace has:

* `6376` ones;
* `6497` zeroes;
* `121` runs;
* one zero-run of length `6436`;
* outside that run, `57` zero-runs of length one and two zero-runs of length
  two;
* one low-shore cell changed from zero to one before the long zero-run.

The zero count is exact:

\[
                  6436+57+2\cdot2=6497.               \tag{2.1}
\]

There are therefore `60` zero-runs.  Since the total number of runs is odd,
there are `61` one-runs and the trace starts and ends in one.  Under the
reported chronology, the gained low-shore tag is the first one-run and the
long zero-run is the second run.

### Proposition 2.1 (phase-braid normal form)

The trace is necessarily

\[
 1\,0^{6436}\,
 1^{h_1}0^{e_1}1^{h_2}\cdots0^{e_{59}}1^{h_{60}},     \tag{2.2}
\]

where

\[
 h_i\ge1,qquad \sum_{i=1}^{60}h_i=6375,              \tag{2.3}
\]

and the multiset of gap lengths is

\[
                       \{e_1,\ldots,e_{59}\}
                       =\{1^{57},2^2\}.                \tag{2.4}
\]

#### Proof

Equation (2.1) accounts for all zeroes and gives exactly sixty zero-runs.
Alternation and the total of 121 runs give sixty-one one-runs.  Removing the
initial gained singleton leaves sixty positive one-runs with total mass
`6376-1=6375`.  The fifty-nine intervening zero-runs have precisely the
reported multiset.  This is (2.2)--(2.4). \(\square\)

The mean length of the sixty terminal high packets is `6375/60=106.25`.
No individual lower bound on an `h_i` follows from the binary ledger alone.

### Comparator arithmetic

If exactly `61` comparator-high cells lose `x` and exactly one comparator-low
cell gains `x`, the comparator has

\[
                         6376+61-1=6436               \tag{2.5}
\]

tagged cells.  Thus the phrase “triple-deleted lift” in this comparison must
mean a deletion pattern with two deleted high cells and one deleted low cell.
An all-three-high deletion comparator has `6435` tags and would be off by one
against the other reported numbers.  This is only a bookkeeping distinction;
the comparator need not itself be universal.

## 3. Exact phase-braid algebra

Let `B=(B_1,...,B_m)` be a word of subsets of a `k`-point old ground set;
zero old projections are allowed.  For a binary trace
`epsilon=(epsilon_1,...,epsilon_m)`, put

\[
 W_i=B_i\cup\bigl(\{x\}\text{ if }\epsilon_i=1\bigr).
\]

For an interval `I`, write `b(I)=union_(i in I) B_i` and call `I` active
when it meets the support of `epsilon`.  For every old mask `S`, define

\[
 n_0(S)=|\{I:b(I)=S,\ I\text{ inactive}\}|,
 \qquad
 n_1(S)=|\{I:b(I)=S,\ I\text{ active}\}|.              \tag{3.1}
\]

### Theorem 3.1 (projection conservation and exact two-shore criterion)

The word `W` witnesses `S` exactly `n_0(S)` times and witnesses
`S union {x}` exactly `n_1(S)` times.  In particular,

\[
 n_0(S)+n_1(S)=
 \nu_B(S):=|\{I:b(I)=S\}|                               \tag{3.2}
\]

is independent of the tag trace.  Both shores of `S` are covered if and
only if

\[
                         n_0(S)>0<n_1(S).                \tag{3.3}
\]

Consequently `nu_B(S)>=2` is necessary, and a pure phase braid can never
repair a mask with `nu_B(S)=1`; it can only exchange which member of
`{S,S union {x}}` is missing.

Summing over projected masks gives the phase-independent hole floor

\[
          \sum_{S\ne\varnothing}\max\{0,,2-\nu_B(S)\}.       \tag{3.4}
\]

#### Proof

The OR of the lifted interval is `b(I)` when `I` is inactive and
`b(I) union {x}` when it is active.  This partitions, without changing, the
fixed family of intervals having old union `S`.  Equations (3.2)--(3.3)
follow. \(\square\)

### Lemma 3.2 (activation rectangles)

Suppose a formerly untagged position `p` is tagged.  Let `l<p<r` be the
nearest old tagged positions, using the two exterior boundaries when one is
absent.  Exactly the intervals

\[
                         l<i\le p\le j<r                 \tag{3.5}
\]

change from inactive to active.

More generally, if a set `F` of tagged positions is untagged, an interval
changes from active to inactive exactly when its old tag set is a nonempty
subset of `F`.  If `F=[u,v]` contains all old tags between the nearest
surviving tags `l` and `r`, this is the interval rectangle

\[
 l<i\le j<r,qquad [i,j]\cap[u,v]\ne\varnothing.         \tag{3.6}
\]

Every affected interval preserves its old projection and transfers one
witness between the two shores.  Hence, if `delta(S)` is the number of
active-to-inactive transfers of projection `S` minus the number of
inactive-to-active transfers, then

\[
             n'_0(S)=n_0(S)+\delta(S),\qquad
             n'_1(S)=n_1(S)-\delta(S).                  \tag{3.7}
\]

#### Proof

An interval changes activity precisely when its Boolean OR in the tag trace
changes.  For a single added tag, this means that it contains `p` but neither
neighboring old tag, which is (3.5).  For deleted tags, its old tag set must
be nonempty and all those tags must be deleted; the stated special case is
(3.6).  The old-coordinate OR is unchanged, so summing the transfers gives
(3.7). \(\square\)

### Corollary 3.3 (unique-witness phase-transfer law)

If `nu_B(S)=1` and its unique projected witness is `I`, then:

* moving `S union {x}` to `S` requires deleting every tag of `I`;
* moving `S` to `S union {x}` requires inserting at least one tag in `I`;
* either operation necessarily loses the formerly covered shore.

Thus a permanent repair of both shores requires a payload/chronology edit
which creates a second projected witness, not merely a phase edit.

### Lemma 3.4 (fixed-rank capacity of one gained tag)

Fix a gained position `p` with nonempty old core `B_p`.  Among old unions of
intervals containing `p`, at most

\[
                            r-|B_p|+1                   \tag{3.8}
\]

distinct rank-`r` sets occur.  The coarser bound is `r`; if `p` is an
endpoint, the bound improves to one.  For several gains, assigning each
newly active interval to its leftmost gain makes these bounds additive.

#### Proof

Every union has the form `P union B_p union Q`, with `P` in the suffix chain
left of `p` and `Q` in the prefix chain right of `p`.  Distinct rank-`r`
outputs form an antichain in the product of the two chains.  Order their
representatives with `P` increasing and `Q` decreasing.  The sets
`P union B_p` must increase strictly: equality at two consecutive terms
would make the corresponding outputs nested, hence equal at common rank.
For `t` outputs, the last therefore has size at least `|B_p|+t-1` and lies
inside a rank-`r` output.  This proves (3.8).  At an endpoint there is only
one chain, which meets a fixed rank in at most one distinct set. \(\square\)

## 4. The exact rank-seven boundary for the incumbent

The general antichain calculation is useful in the following form.  If a
tail of length `L` must provide `t` distinct masks of one fixed rank, then
one may choose their witness intervals as a containment antichain, and every
chosen interval has length at most `L-t+1`.

For the abstract architecture retaining the full old copy `A`, the central
singleton, and a tail of length `6434`, there are at most two external old
rank-seven states.  With `g` gained old-shore tags, Lemma 3.4 gives the
coarse comparator bounds

\[
 t\ge6433-7g,qquad \text{witness radius}\le2+7g.        \tag{4.1}
\]

This is a theorem about that fixed-`A` comparator.  It is not the exact
geometry of the reported incumbent.

### Theorem 4.1 (incumbent-specific four-window bound)

For `scratch/k16_12873_repaired_partial.word`, the singleton `{x}` is at
zero-based position `6437`; the post-singleton tail therefore has length
`6435`.  Outside that tail, an active old rank-seven interval has at most
three distinct projections:

1. at most one prefix state through the gained tag at position zero;
2. at most one central state from an empty pre-singleton suffix; and
3. the fixed terminal old-shore state `18033` from a nonempty suffix.

Thus at least `6435-3=6432` old rank-seven masks would have to be supplied
inside the tail in any complete word of this exact architecture, and their
witness radius is at most

\[
                         6435-6432+1=4.                 \tag{4.2}
\]

The exact replay is one unit short of this necessary count: the tail supplies
`6431` distinct active old rank-seven projections, all by intervals of length
at most three.  The three external states are

\[
                         10349,\quad18553,\quad18033,    \tag{4.3}
\]

and the sole absent old rank-seven projection is `20065`; its tagged target
is `32768+20065=52833`, one of the three authenticated holes.

#### Proof

An active interval before the singleton must contain the sole early tag at
position zero and hence is a prefix; a nested prefix chain has at most one
state at fixed rank.  A crossing interval with empty pre-singleton suffix is
again one prefix-chain state.  Every nonempty pre-singleton suffix contains
the rank-seven endpoint `18033`, so a rank-seven union containing it can only
equal it.  This proves the capacity three and (4.2).  The values in (4.3),
the `6431` tail count, the length-three bound, and the missing projection are
the frozen exact replay data. \(\square\)

The old `1/4` support proof used radius two: it could charge every required
rank-seven target to a singleton or adjacent pair.  The incumbent is outside
that theorem twice over: it has only `6437` pre-singleton cells and `6435`
tail cells, and its endpoint gain supplies a third external state.  The
resulting radius four admits the source word's overwhelmingly length-three
rank-seven catalogue.  This, rather than the mere number `59` of short zero
gaps, is why the protected-singleton/adjacent-pair charge no longer applies.

## 5. What the 59 internal zero portals do and do not prove

The binary trace has the exact normal form (2.2), but rank-seven saturation
does not force `60` high packets or `59` internal zero gaps.  Those gaps
decide which old-projection intervals are active and hence route witnesses
between the two shores according to Theorem 3.1.  They do not create new old
projections and they do not by themselves change the radius bound.

Consequently the strongest justified statement is:

> A fixed full-`A` shore with central singleton and a `6434`-cell mixed tail
> needs order-preserving rethread support at least `1610`.  The incumbent
> evades the hypothesis by changing the old-shore/singleton boundary; its
> exact rank-seven catalogue then operates at radius three within the
> radius-four allowance.

No theorem here says that one early gain is necessary, that `59` portals are
minimal, or that the 121-run trace follows from rank-seven coverage.  Any such
lower bound must use payload-specific two-shore multiplicities, other ranks,
or chronology constraints.

## 6. The adjacent two-down portal and the phase-pair transfer theorem

All positions in this section are zero based.  In the frozen incumbent,

\[
\begin{array}{c|cccc}
p&6435&6440&6441&12872\\ \hline
W_p&\mathtt{0600}&\mathtt{a069}&\mathtt{806d}&\mathtt{cc41}.
\end{array}                                                  \tag{6.1}
\]

The two adjacent edits

\[
 6440:\mathtt{a069}\mapsto\mathtt{2069},\qquad
 6441:\mathtt{806d}\mapsto\mathtt{006d}                   \tag{6.2}
\]

are pure high-to-low phase flips.  The old mask `10365=0x287d` has the
unique projected interval `[6439,6441]`, and its two tagged positions are
exactly `6440,6441`.  Corollary 3.3 therefore says that both flips are
necessary and sufficient to move this unique witness from tagged target
`43133=0xa87d` to untagged target `10365`.  The shorter interval
`[6439,6440]` simultaneously moves a tagged witness of `43129=0xa879` to an
already covered untagged projection.  Hence (6.2) fills the untagged original
hole `10365` and creates exactly the two immediate tagged debts

\[
                         43129,\quad43133.               \tag{6.3}
\]

The nearest surviving tags are at `6437` and `6442`.  Lemma 3.2 therefore
gives exactly seven transferred interval occurrences:

\[
\begin{array}{c|c}
\text{interval}&\text{old projection}\\ \hline
[6438,6440]&\mathtt{6879}\\
[6438,6441]&\mathtt{687d}\\
[6439,6440]&\mathtt{2879}\\
[6439,6441]&\mathtt{287d}\\
[6440,6440]&\mathtt{2069}\\
[6440,6441]&\mathtt{206d}\\
[6441,6441]&\mathtt{006d}.
\end{array}                                                 \tag{6.4}
\]

Clearing `6440` alone leaves `6441` in the unique `0x287d` interval;
clearing `6441` alone leaves `6440`.  Thus this service is genuinely
two-flip.

There are two authenticated ways to supply the other two original holes.

### The pure all-central braid

Add the phase flip

\[
                         6435:\mathtt{0600}\mapsto\mathtt{8600}. \tag{6.5}
\]

The unique old-projection witnesses

\[
 [6433,6435]\mapsto20065,\qquad
 [6432,6435]\mapsto20067                              \tag{6.6}
\]

become witnesses of `52833=0xce61` and `52835=0xce63`.  This fills all three
original holes.  Projection conservation prevents it from being a complete
repair: `nu_B(20065)=nu_B(20067)=1`, so the two old targets in (6.5) must be
lost.  The same activation rectangle also removes the last inactive witnesses
of `20081` and `20215`.  Together with (6.3), the exact six-mask debt is

\[
       \{20065,20067,20081,20215,43129,43133\}.          \tag{6.7}
\]

The complete relevant multiplicity transfer is

\[
\begin{array}{c|c}
S&(n_0(S),n_1(S))\text{ before}\longmapsto\text{after}\\ \hline
\mathtt{2879}&(1,1)\mapsto(2,0)\\
\mathtt{287d}&(0,1)\mapsto(1,0)\\
\mathtt{4e61}&(1,0)\mapsto(0,1)\\
\mathtt{4e63}&(1,0)\mapsto(0,1)\\
\mathtt{4e71}&(2,2)\mapsto(0,4)\\
\mathtt{4ef7}&(1,1)\mapsto(0,2).
\end{array}                                                \tag{6.8}
\]

### The remote payload braid

Instead of (6.4), make the payload edit

\[
                    12872:\mathtt{cc41}\mapsto\mathtt{ce41}. \tag{6.9}
\]

The terminal intervals `[12871,12872]` and `[12870,12872]` now witness
`52833` and `52835`.  Unlike (6.4), this is not a pure phase edit: it creates
second projected witnesses of `20065` and `20067`, so their old central
witnesses survive on the opposite shore.  It instead destroys the terminal
palette

\[
                         52321,52323,52327,52455.        \tag{6.10}
\]

Together with (6.3), its exact debt is

\[
       \{43129,43133,52321,52323,52327,52455\}.          \tag{6.11}
\]

### Theorem 6.1 (general phase-pair transfer)

For any fixed old payload word, a phase braid is exactly a signed transfer
of the projection histograms in (3.7).  In particular, if an uncovered shore
of `S` has a unique projected witness interval `I`, then changing its shore
requires toggling all old tags of `I` off, or at least one tag of `I` on,
according to direction; the opposite shore is necessarily lost.  A
simultaneous two-shore repair is possible only if the chronology already has
a second projected witness, or a payload edit creates one.

The adjacent pair (6.2) is the smallest instance of the first operation:
the unique interval for `10365` contains two tags, so no one of the two flips
can deactivate it.  The central edit (6.4) demonstrates the unavoidable-hole
transfer, whereas the remote edit (6.7) demonstrates the only general escape:
create a second projection occurrence and split the two occurrences between
the shores.

#### Proof

The first assertion is Theorem 3.1 and Lemma 3.2.  The unique-witness claim
is Corollary 3.3.  Equations (6.3), (6.7), and (6.11) follow by the displayed
literal windows and exact global multiplicity replay. \(\square\)

Thus a genuine completion theorem cannot be a tag-balancing theorem alone.
It must construct additional projected occurrences while keeping at least
one occurrence on each shore.  For the six-debt portals, that is the precise
remaining payload/chronology gate.

## 7. Frozen replay artifacts

```text
scratch/k16_12873_repaired_partial.word
  SHA-256 0a70a67eced48a82883a698c6fd25688a27c52faf19e3fa11bbbd9a78581bea6

scratch/audit_threadA_k16_phase_pair_transfer_20260730.py
  SHA-256 8b465ba7b5ff3f0e7117ccb26b529941732bd6d53883c2b86008bfc4df2f42c2

scratch/threadA_k16_phase_braid_activation_20260730.audit.json
  SHA-256 336de48b536e2cda18de6648e5d85ff935d74a393307e86cd902ac9fb7b4c90d
```

The script is an `O(nk)` contiguous-OR replay.  It verifies the trace normal
form, the exact rank-seven tail/exterior split, the source length-three
catalogue, both portal ledgers, and every displayed unique projected witness.
It performs no repair search.
