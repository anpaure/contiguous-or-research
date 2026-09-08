# Private low-collar blocks forbid bounded-top self-recharging reroot amplification

Date: 2026-07-27

Method: pure mathematics only. No computation, finite search, solver, or
web input is used.

## 0. Verdict

Put

\[
 n=2m,\qquad M=m+H,\qquad d=m-3H+1,
\tag{0.1}
\]

and assume

\[
 H\ge3,\qquad d\ge2H+1.
\tag{0.2}
\]

These inequalities hold in the hypotheses of the audited three-top and
unshifted four-top local recharge theorems.

Fix a family \(\mathcal S\) of \(s\) physical rank-\(M\) tops and
allow one selected consecutive retained path on each top.  Suppose every
allowed transition is aggregate-neutral in the physical retained decks
at omitted lengths \(h=1,2\).  This is a strictly weaker hypothesis than
full collar neutrality.  It is satisfied by:

1. the three-top collar-neutral re-root packet;
2. the unshifted four-top full-trace recharge;
3. their inverses and arbitrary compositions; and
4. the two-top boundary rectangle, since \(H\ge3\) and its only
   nonzero aggregate row is the middle row \(h=H\).

For every fixed focal top \(U\in\mathcal S\), the entire state-graph
component contains at most

\[
             \boxed{F(s)=2^{4s-3}(4s-3)!}                  \tag{0.3}
\]

different first-\(d\) focal words, hence at most that many protected
boundary prefixes.  In particular it contains at most \(F(s)\)
different complete first-two boundary-swap derivative vectors through
all protected lengths \(0\le h\le2H\).

Consequently:

\[
\boxed{
\begin{gathered}
\text{No fixed five-top, or any fixed bounded-top, exact
self-recharging packet}\\
\text{can yield }\Theta(m)\text{ effective focal directions in this
retained-deck interface.}
\end{gathered}}
\tag{0.4}
\]

For five tops the explicit bound is

\[
                         F(5)=2^{17}17!,                    \tag{0.5}
\]

independent of \(m\).  More generally, \(t\) distinct directions force

\[
                         t\le F(s),                         \tag{0.6}
\]

and therefore

\[
                         s\log(s+1)=\Omega(\log t).         \tag{0.7}
\]

Thus \(t=\Theta(m)\) requires at least

\[
                         s=\Omega\!\left(
                         {\log m\over\log\log m}\right).   \tag{0.8}
\]

The obstruction is statewise.  Helpers may be left in different valid
source states, may exchange their roles, and may follow a periodic
cycle.  Exact restoration is not assumed.  The invariant is the private
rank-\((M-1)\) and rank-\((M-2)\) target ledger: after at most
\(2(s-1)\) nonprivate labels are deleted, the focal retained word splits
into a bounded collection of labelled path blocks which no legal move
can cut or merge.

The immediate three-top reuse is not overlooked.  Its target shore is
the inverse packet's source shore, so the same three tops give a genuine
period-two self-recharge.  It merely alternates between two focal states
and has zero amplification.  The theorem proves that adding a fifth, or
any bounded number of, physical tops cannot turn this local alternation
into linear direction rank.

No coefficient-one conclusion is claimed.  Rather, even if every
candidate packet were granted literal owner installability, bounded-top
self-recharge would still fail at the lower collar ledger.

## 1. The retained-deck interface

For a top \(U\) and an injective cyclic word

\[
                         p=(p_1,\ldots,p_M),                 \tag{1.1}
\]

normalize the consecutive retained phase starts as \(1,\ldots,d\).
For \(0\le h\le2H\), put

\[
 \mathcal D_h(U,p)=
 \sum_{j=1}^{d}
 e_{U\setminus\{p_j,p_{j+1},\ldots,p_{j+h-1}\}},         \tag{1.2}
\]

with the deleted interval empty at \(h=0\).  No wrap occurs in the
prefixes used below because of (0.2).

At the two lowest positive lengths, complementation identifies
\(\mathcal D_1,\mathcal D_2\) with

\[
 L(p)=\{p_1,\ldots,p_d\},                                  \tag{1.3}
\]

and the edge set

\[
 E(p)=\bigl\{\{p_j,p_{j+1}\}:1\le j\le d\bigr\}.          \tag{1.4}
\]

Thus \(E(p)\) is the labelled simple path

\[
                         p_1-p_2-\cdots-p_{d+1}.            \tag{1.5}
\]

A transition \({\bf p}\to{\bf q}\) on \(\mathcal S\) is
**low-collar neutral** if

\[
 \sum_{U\in\mathcal S}\mathcal D_h(U,q_U)
 =
 \sum_{U\in\mathcal S}\mathcal D_h(U,p_U)
 \qquad(h=1,2).                                             \tag{1.6}
\]

Every full \(0\le h\le2H\) collar-neutral packet is low-collar
neutral.  Notice that (1.6) permits arbitrary middle action when
\(H\ge3\), so it also permits all useful boundary rectangles.

Let \(B\) interchange the first two letters of \(p\).  For \(h\ge2\),
only the phase-two interval changes, and hence

\[
\begin{aligned}
 \partial_hB(p)
 &:={\cal D}_h(U,Bp)-{\cal D}_h(U,p)\\
 &=e_{U\setminus\{p_1,p_3,\ldots,p_{h+1}\}}
   -e_{U\setminus\{p_2,p_3,\ldots,p_{h+1}\}}.
                                                               \tag{1.7}
\end{aligned}
\]

At \(h=0,1\) the derivative is zero.  Therefore the complete protected
boundary derivative

\[
                 \partial B(p)=(\partial_hB(p))_{0\le h\le2H}
                                                               \tag{1.8}
\]

is determined by

\[
                         (p_1,\ldots,p_{2H+1}).              \tag{1.9}
\]

The middle hypersimplex direction is its \(h=H\) coordinate.

## 2. What the existing three- and four-top packets actually recycle

### 2.1 The three-top packet has an exact period-two inverse

Use the notation of the three-top theorem.  Its source is

\[
 \bigl(
 \omega^+(x,y),\ \eta^+(x,a),\ \eta^+(a,y)
 \bigr).                                                     \tag{2.1}
\]

Because \(\theta^-(u,v)=\theta^+(v,u)\), its target is

\[
 \bigl(
 \omega^+(y,x),\ \eta^+(a,x),\ \eta^+(y,a)
 \bigr).                                                     \tag{2.2}
\]

After interchanging the two helper roles, (2.2) is exactly the source
of the inverse triangle with \((x,y)\) replaced by \((y,x)\).  Hence
the same three physical tops can be used forever in the alternating
sequence

\[
                         \mathcal O\leftrightarrow\mathcal N. 
                                                               \tag{2.3}
\]

This is a literal self-recharge, but its focal word has only the two
states displayed in the source theorem.  The theorem does not certify a
second forward triangle on (2.2) with a new remote focal label.

The individual helpers in (2.1) are not neutral.  Their derivatives
telescope only in the three-top sum; suppressing the depth and retained-
phase superscripts, at every protected length one has

\[
 d_\eta(x,a)+d_\eta(a,y)=d_\eta(x,y)=-d_\omega(x,y).        \tag{2.4}
\]

Thus treating either helper as a freely restored catalyst would be
incorrect.

### 2.2 The four-top recharge is open, not already periodic

The unshifted four-top theorem gives, for arbitrary focal word \(p_0\),
three helper words and the simultaneous transition

\[
                         p_i\longmapsto rp_i
                         \qquad(0\le i<4),                  \tag{2.5}
\]

where \(r\) is one-step left re-rooting and

\[
 \sum_{i=0}^3
 \bigl(\mathcal D_h(U_i,rp_i)-\mathcal D_h(U_i,p_i)\bigr)=0
 \qquad(0\le h\le2H).                                      \tag{2.6}
\]

All four words change.  The theorem constructs a new set of compatible
helper words for each prescribed current focal word; it does not prove
that \((rp_i)_{i<4}\) is again the source shore of the same four-top
cycle.  Indeed its second entrance facets use the first labels of the
two long collar blocks rather than the four original Johnson seam
labels.  At that second \(h=1\) step the eight signed facets are
\(U_i\setminus\{\alpha\}\) and \(U_i\setminus\{\beta\}\), where
\(\alpha,\beta\) are the first labels of the two disjoint collar blocks.
They are pairwise distinct across the four original tops, so the
original carrier square supplies no cancellation.

There is also an implication-scope issue in the shifted four-top report:
aggregate trace equality and one word per top do not by themselves prove
that the four middle decks are squarefree.  The no-go below grants the
word/deck transition anyway, so it does not depend on this missing
coefficient-one audit.

The local failures in Sections 2.1--2.2 motivate a fifth top, but they do
not by themselves classify all possible fifth-top packets.  The next
sections give the invariant which does.

## 3. Strict helper restoration already has zero focal boundary holonomy

We first separate exact restoration from the weaker valid-source
condition.

### Lemma 3.1 (two decks reconstruct the oriented retained path)

The pair \((\mathcal D_1(U,p),\mathcal D_2(U,p))\) determines the
ordered word

\[
                         p_1,p_2,\ldots,p_{d+1}              \tag{3.1}
\]

exactly.

#### Proof

After complementation, \(\mathcal D_2\) gives the simple path (1.5).
The vertex set of this path is \(L(p)\cup\{p_{d+1}\}\), while
\(\mathcal D_1\) gives exactly \(L(p)\).  Hence \(p_{d+1}\) is the
unique path vertex absent from \(L(p)\).  Starting at that endpoint and
following the path backwards recovers

\[
                         p_{d+1},p_d,\ldots,p_1.
\]

This fixes the orientation and proves the lemma. \(\square\)

### Corollary 3.2 (strict self-recharge has zero focal boundary holonomy)

Let one low-collar-neutral macro touch one focal top and any number of
helpers.  If every helper returns with its original
\(\mathcal D_1,\mathcal D_2\) decks, then the focal word through
position \(d+1\) is unchanged.  In particular its boundary direction is
unchanged.

#### Proof

Subtract the identical helper endpoints from (1.6).  The two focal
decks are individually equal, and Lemma 3.1 applies. \(\square\)

The same argument applies over a whole period.  If helpers move through
different valid sources but eventually return to their initial physical
decks, the focal prefix also returns at that period.  Thus a periodic
macro cannot accumulate nonzero focal low-collar or boundary-state
holonomy.  This statement alone does not exclude unrelated higher-deck
endpoint action.  A literal full-state circuit is, of course, null in
every endpoint deck.  The macro might still visit many transient focal
directions inside one period; bounded support for those transients is
the remaining issue.

## 4. Private low-collar coordinates

Fix \(U\in\mathcal S\).  Define its exceptional label set

\[
 Z_U=
 \bigcup_{\substack{V\in\mathcal S\setminus\{U\}\\
                    1\le |U\setminus V|\le2}}
                    (U\setminus V),                         \tag{4.1}
\]

and put

\[
                         \ell_U=|Z_U|,\qquad Q_U=U\setminus Z_U.
                                                               \tag{4.2}
\]

Every other top contributes at most two labels, so

\[
                         \boxed{\ell_U\le2(s-1).}           \tag{4.3}
\]

### Lemma 4.1 (private facets)

If \(x\in Q_U\), the rank-\((M-1)\) target \(U\setminus\{x\}\)
occurs in a deck on no other top in \(\mathcal S\).

#### Proof

If

\[
                         U\setminus\{x\}=V\setminus\{y\}
                                                               \tag{4.4}
\]

for \(V\ne U\), then \(|U\setminus V|=1\) and
\(U\setminus V=\{x\}\).  Definition (4.1) would give \(x\in Z_U\),
a contradiction. \(\square\)

### Lemma 4.2 (private pairs)

If \(x,y\in Q_U\) are distinct, the rank-\((M-2)\) target
\(U\setminus\{x,y\}\) occurs in a deck on no other top in
\(\mathcal S\).

#### Proof

Suppose

\[
 U\setminus\{x,y\}=V\setminus\{z,w\},\qquad V\ne U.       \tag{4.5}
\]

Then

\[
                         \varnothing\ne U\setminus V
                         \subseteq\{x,y\},                 \tag{4.6}
\]

so \(1\le|U\setminus V|\le2\).  Every member of \(U\setminus V\)
belongs to \(Z_U\) by (4.1), contradicting \(x,y\in Q_U\).
\(\square\)

Let \(p^0\) be the initial word at \(U\), and put

\[
                         K_U=L(p^0)\cap Q_U.                \tag{4.7}
\]

By Lemma 4.1 and aggregate \(\mathcal D_1\)-neutrality, every reachable
state \(p\) satisfies

\[
                         L(p)\cap Q_U=K_U.                  \tag{4.8}
\]

By Lemma 4.2 and aggregate \(\mathcal D_2\)-neutrality, for every
pair \(x,y\in K_U\),

\[
 \{x,y\}\in E(p)\quad\Longleftrightarrow\quad
 \{x,y\}\in E(p^0).                                       \tag{4.9}
\]

Both presence and absence are frozen.  These are coordinatewise
identities; no cancellation on a helper top is available for them.

## 5. The private-block normal form

Delete the \(Z_U\)-labels from the initial first-\(d\) word

\[
                         p^0_1,p^0_2,\ldots,p^0_d.          \tag{5.1}
\]

The remaining \(K_U\)-labels form labelled consecutive path blocks

\[
                         P_1,\ldots,P_c,                    \tag{5.2}
\]

including singleton blocks.  Since deleting one label can increase the
number of runs by at most one,

\[
                         c\le\ell_U+1.                      \tag{5.3}
\]

### Lemma 5.1 (private blocks cannot split or merge)

In every reachable first-\(d\) word:

1. every block \(P_i\) occurs contiguously;
2. it occurs in one of its two orientations;
3. no two distinct blocks are adjacent; and
4. every label outside the blocks belongs to \(Z_U\).

#### Proof

Item 4 is (4.8).  The internal edges of each \(P_i\) are precisely
private \(Q_UQ_U\)-edges present in (4.9).  Splitting the block would
delete one such edge.  Because the block is a simple labelled path, any
contiguous traversal of all its edges has one of the two orientations.

Joining two blocks directly would create a new \(Q_UQ_U\)-edge, whose
absence is also frozen by (4.9).  Equivalently, an extra connector
cannot enter an internal block vertex: that vertex already has its two
private path edges, while the full retained adjacency graph has maximum
degree two. \(\square\)

Put

\[
                         b=d-|K_U|.                         \tag{5.4}
\]

Every later first-\(d\) word contains all \(K_U\)-labels and exactly
\(b\) labels from \(Z_U\).  Hence

\[
                         b\le\ell_U.                        \tag{5.5}
\]

Choose those exceptional labels, orient the \(c\) fixed blocks, and
order the \(c+b\) objects.  Lemma 5.1 gives

\[
\begin{aligned}
 \#\{\text{reachable first-}d\text{ words at }U\}
 &\le {\ell_U\choose b}\,2^c(c+b)!\\
 &\le 2^{2\ell_U+1}(2\ell_U+1)!\\
 &\le 2^{4s-3}(4s-3)!.
                                                               \tag{5.6}
\end{aligned}
\]

A label outside \(K_U\cup Z_U\) may vary at the terminal position
\(p_{d+1}\).  It cannot enter positions \(1,\ldots,d\) by (4.8).
Since \(d\ge2H+1\), that terminal freedom does not affect (1.9) and
therefore cannot change any protected boundary direction.

This proves (0.3).

## 6. Consequences for periodic and valid-source recharge

### Theorem 6.1 (bounded-top self-recharge ceiling)

Let a chronology use a fixed family \(\mathcal S\) of \(s\) physical
tops, one retained path per top, and let every step satisfy (1.6).
Helpers may end a step in any valid source states for the next step.
Then a fixed focal top supports at most \(F(s)\) distinct complete
boundary derivative vectors (1.8), and their linear span has dimension
at most \(F(s)\).

#### Proof

Every state in the chronology lies in the same private-coordinate fibre
(4.8)--(4.9).  Equation (5.6) bounds its first \(d\) words, while
(0.2) and (1.7)--(1.9) make the complete boundary derivative a function
of that word.  A span has dimension no larger than the number of its
generators. \(\square\)

For \(s=5\), Theorem 6.1 gives (0.5).  For arbitrary \(s\), put
\(k=4s-3\).  Since

\[
                         F(s)=2^kk!\le(2k)^k,               \tag{6.1}
\]

one has

\[
                         \log t\le k\log(2k).               \tag{6.2}
\]

This proves (0.7)--(0.8).

### Corollary 6.2 (periodicity does not help)

Suppose the helpers follow a periodic valid-source schedule.  If at one
period, or at some finite multiple of it, the actual helper
\(\mathcal D_1,\mathcal D_2\) tuple returns, Corollary 3.2 forces the
focal prefix to return as well.  A mere finite-order permutation of role
names need not return the physical decks because internal state
monodromy may remain; no return conclusion follows in that case.

In either interpretation, all transient focal directions obey the
ceiling \(F(s)\) by Theorem 6.1.  A literal period repeats old
directions, while a role-only schedule remains in the same bounded
private-block state fibre.
If the focal role itself rotates among the \(s\) physical tops, the
total number of directions across all possible focal identities is at
most \(sF(s)\), still independent of \(m\) for bounded \(s\).

Thus there is no periodic five-top construction with \(\Theta(m)\)
effective directions, even though the elementary three-top inverse
cycle is a valid period-two self-recharger.

## 7. Exact implication boundary and source audit

The following are proved.

1. Exact restoration of the helpers forces zero focal low-collar
   holonomy.
2. Merely leaving helpers in other valid source states does not evade
   the private facet/pair invariants.
3. A fixed \(s\)-top support has at most \(F(s)\) focal boundary-prefix
   states and directions.
4. Five tops have the explicit \(m\)-independent ceiling
   \(2^{17}17!\).
5. Linear direction rank requires
   \(s=\Omega(\log m/\log\log m)\) in this interface.

The first exact failure of a proposed bounded self-recharger is not a
high-depth collar term.  It occurs already at \(h=1,2\): a new focal
chart must either move a private label across the retained boundary or
break/create a private adjacency, leaving an uncancelled literal target.

The scope qualifications are essential.

1. There is one selected consecutive linear path per physical top and
   one fixed union \(\mathcal S\) of physical tops.
2. The transitions obey the unshifted retained-deck identities (1.6).
   This is the interface proved in
   `MATH_THEOREM_THREE_TOP_COLLAR_NEUTRAL_REROOTING_AND_LINEAR_RECHARGE_20260727.md`
   and
   `MATH_THEOREM_L_COLLAR_NEUTRAL_REROOTING_AND_LINEAR_LOCAL_REUSE_20260727.md`.
3. The alternate shifted traces \(\mathcal T_r\) in
   `MATH_THEOREM_FOUR_TOP_REROOT_COLLAR_CYCLE_AND_BOUNDED_SUPPORT_GATE_20260727.md`
   do not, by themselves, imply the anchored \(\mathcal D_1,\mathcal D_2\)
   identities used here.  A genuinely new primitive preserving only
   that shifted interface is outside this theorem.
4. Multiple simultaneous rows on one physical top, nonconsecutive
   retained decks, or a packet whose cancellation exists only after a
   tag-dependent thinning are outside the theorem.
5. For a tagged lift of the full unshifted identities, tags and owner
   constraints can only restrict the reachable word states further.
6. The state-graph ceiling applies at every harvested packet boundary
   for which (1.6) holds.  It does not count transient directions inside
   a larger atomic macro that is allowed to leave the
   \(\mathcal D_1,\mathcal D_2\) fibre before returning.  Every move in
   the cited three-top/four-top/rectangle library is itself neutral at
   these two rows, so their chronological closure is covered.

Finally, the four-top word/deck theorem does not itself establish
squarefree middle ownership of every four-row shore.  The present result
is conditional only on the word/deck transition and hence remains valid
even if one grants that missing literal installation step.

No construction with growing support is supplied here, and no
coefficient-one theorem follows.  What is closed is the requested
five-top/bounded-top self-recharging architecture in the audited
unshifted local library.

## Independent audit

Three independent proof audits checked the source/target orientations
of the three-top packet, the open four-top source issue, privacy of the
rank-\((M-1)\) and rank-\((M-2)\) coordinates, the terminal-position
caveat, the block count, and the shifted-trace implication boundary.
The corrections from those audits are incorporated above.
