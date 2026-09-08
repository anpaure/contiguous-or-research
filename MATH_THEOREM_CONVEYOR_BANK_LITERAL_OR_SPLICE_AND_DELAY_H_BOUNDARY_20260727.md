# Literal OR splicing for a bank of three-top conveyors

## One reset per frame, common-state zero surgery, and the sharp delay-\(H\) boundary

Date: 2026-07-27

Scope: constant-one Gaussian-annulus program; pure mathematics only.
No computation, search, solver, or external theorem is used.

## 0. Verdict

Let a top-disjoint bank contain \(t\) literal three-top conveyor packets,
and let

\[
                         L=H+\delta-1,\qquad1\le\delta\le H  \tag{0.1}
\]

be the marked safe-port length.  Switching all packets changes exactly

\[
                         D=6Lt                              \tag{0.2}
\]

top-indexed ordered ports and preserves exactly the same \(3Mt\)
squarefree principal middle owners.

There is a direct word-level compiler for either shore with length

\[
 \boxed{
                         3Mt+6Ht\le3Mt+D.}                    \tag{0.3}
\]

Thus the total number of added symbols is at most the number of changed
ports; in particular it is

\[
                         O(t+D).                              \tag{0.4}
\]

The reason is exact and simple: the \(2H\)-symbol initialization of one
promotion frame simultaneously repairs every one of its \(2L\) changed
ports.  Paying a separate delay \(H\) at every changed port would count
the same queue memory repeatedly.

There is also a zero-addition substitution theorem.  The plus and minus
promotion cycles on any touched top have exactly \(M-4H\) identical full
useful states.  If an ambient word traverses the old frame as a closed
excursion based at one such common state, the new closed excursion has
the same endpoints and the same length, and can replace it without one
additional symbol.

On the negative side, no universal \(O(1)\) bridge exists between
arbitrary useful states.  The exact useful-prefix bridge distance can be
\(2H+1\).  Hence top-disjointness alone does not create constant-size
seams.  This delay does not obstruct (0.3), because it is paid once per
\(M\)-owner frame and is already bounded by the changed-port ledger.

The result resolves the word-interface cost **conditional on the
existence of the conveyor bank**.  It does not construct a
\(\Theta(W/M)\)-matching of packets, and it does not prove that the
resulting new annular flags cover every target.

## 1. Literal OR and last-occurrence states

A literal word is a sequence of nonempty masks

\[
                         Y_1,Y_2,\ldots,Y_s\subseteq[2m].      \tag{1.1}
\]

At an endpoint, partition coordinates by decreasing last occurrence.
This gives an ordered state

\[
                         \Sigma=(C_1,C_2,\ldots,C_r).          \tag{1.2}
\]

Appending a mask \(Y\) performs the move-to-front update

\[
 M_Y(\Sigma)=
 (Y,C_1\setminus Y,C_2\setminus Y,\ldots,C_r\setminus Y),     \tag{1.3}
\]

after empty blocks are deleted.  For every \(j\), the prefix union

\[
                         C_1\cup\cdots\cup C_j               \tag{1.4}
\]

is the OR of a literal suffix ending at that endpoint.  Conversely all
distinct suffix ORs ending there are these prefix unions.  They form one
nested chain, so at one endpoint there is at most one represented mask
of each rank.

This last observation is the exact seam ledger: an initialization symbol
creates one physical endpoint, not \(H\) different word positions.
Although that endpoint may expose one mask in every protected rank, it
contributes only one symbol to word length and at most one extra rank-
\(m\) occurrence.

## 2. One cyclic frame has a word of length \(M+2H\)

Put

\[
                         r=m-H,\qquad M=r+2H=m+H.             \tag{2.1}
\]

Fix a top \(U\) of size \(M\) and a cyclic order

\[
                         \pi=(a_i:i\in\mathbb Z_M).           \tag{2.2}
\]

For each phase \(i\), define the full useful state

\[
 \Omega_i=(L_i;z_{i,1},\ldots,z_{i,2H};R),                   \tag{2.3}
\]

where

\[
 \begin{aligned}
  L_i&=\{a_i,a_{i+1},\ldots,a_{i+r-1}\},\\
  z_{i,j}&=a_{i-j},\\
  R&=[2m]\setminus U.
 \end{aligned}                                                \tag{2.4}
\]

The displayed blocks partition \([2m]\).

### Lemma 2.1 (exact promotion update)

Appending the nonempty mask \(L_{i+1}\) to state \(\Omega_i\) produces
state \(\Omega_{i+1}\).

#### Proof

The two lower blocks satisfy

\[
 L_{i+1}=L_i-\{a_i\}+\{a_{i+r}\}.                            \tag{2.5}
\]

Because \(M=r+2H\), one has

\[
                         a_{i+r}=a_{i-2H}=z_{i,2H}.            \tag{2.6}
\]

Apply (1.3) with \(Y=L_{i+1}\).  The surviving part of \(L_i\) is the
singleton \(\{a_i\}\), followed by
\(z_{i,1},\ldots,z_{i,2H-1}\), while \(z_{i,2H}\) is absorbed into
\(Y\).  The residual block \(R\) is unchanged.  This is exactly
\(\Omega_{i+1}\). \(\square\)

The principal middle owner and its exact signed flags are

\[
 X_i=L_i\cup\{z_{i,1},\ldots,z_{i,H}\}
     =\{a_{i-H},\ldots,a_{i+r-1}\},                           \tag{2.7}
\]

\[
 D_{i,q}=L_i\cup\{z_{i,1},\ldots,z_{i,H-q}\}
     =\{a_{i-H+q},\ldots,a_{i+r-1}\},                        \tag{2.8}
\]

\[
 A_{i,q}=L_i\cup\{z_{i,1},\ldots,z_{i,H+q}\}
     =\{a_{i-H-q},\ldots,a_{i+r-1}\},                        \tag{2.9}
\]

for \(0\le q\le H\), with cyclic indices.  By (1.4), every set in
(2.7)--(2.9) is the OR of an actual suffix ending at the endpoint whose
state is \(\Omega_i\).

These formulas use the direct interval convention, which is the
convention in which the conveyor's complete middle window decks were
first compared.  No complement of an OR witness is being assumed.

### Theorem 2.2 (independent useful-prefix frame compiler)

The complete \(M\)-owner promotion frame \(\pi\) has a literal word of
length

\[
                             M+2H.                            \tag{2.10}
\]

It has exactly \(M\) designated principal endpoints, one for every
owner \(X_i\), and exactly \(2H\) nonprincipal initialization
endpoints.

#### Proof

To install the useful prefix of \(\Omega_0\) from an arbitrary incoming
state, append its useful blocks in reverse order:

\[
 \{z_{0,2H}\},\{z_{0,2H-1}\},\ldots,\{z_{0,1}\},L_0.      \tag{2.11}
\]

These are \(2H+1\) nonempty masks.  Repeated use of (1.3) shows that the
resulting state begins exactly with

\[
                         (L_0;z_{0,1},\ldots,z_{0,2H}).       \tag{2.12}
\]

The surviving old blocks, after \(U\) is deleted from them, form an
arbitrary ordered refinement of \(R\).  They need not coalesce.  This is
irrelevant: every protected prefix union ends before \(R\), and every
later update \(L_i\subseteq U\) leaves this residual refinement
unchanged.  Thus all later states have exactly the useful prefix in
(2.3), possibly followed by a refined residual tail.  Designate this
last initialization endpoint as the first principal endpoint.

Now append

\[
                         L_1,L_2,\ldots,L_{M-1}.              \tag{2.13}
\]

Lemma 2.1, applied to the useful prefix, visits the useful prefixes of
\(\Omega_1,\ldots,\Omega_{M-1}\), one endpoint per symbol.  The length is

\[
                         (2H+1)+(M-1)=M+2H.                  \tag{2.14}
\]

Equations (2.7)--(2.9) give the exact OR windows at every principal
endpoint. \(\square\)

The initialization is source-blind.  Therefore words of the form
(2.11)--(2.13) may be concatenated in an arbitrary order; each new
initialization overwrites precisely the useful prefix it needs and
leaves an irrelevant residual tail.

## 3. Exact compilation of a top-disjoint conveyor bank

Let \(\mathcal B\) be a bank of \(t\) top-disjoint three-top packets.
Assume their selected old shores occur in one middle-squarefree frame
table.  For every packet independently choose either its old or new
shore.  The squarefree packet theorem says that all choices have the
same principal middle-owner set, of size

\[
                             K=3Mt.                           \tag{3.1}
\]

There are \(3t\) selected cyclic frames.

### Theorem 3.1 (standalone bank word)

Every shore choice for \(\mathcal B\) has one literal OR word of length

\[
 \boxed{
                             K+6Ht.}                           \tag{3.2}
\]

The word has exactly \(K\) principal middle endpoints, squarefree and
independent of the shore choices.  At those endpoints it exposes exactly
the lower and upper interval flags of the chosen physical frames through
all depths \(q\le H\).

#### Proof

Apply Theorem 2.2 independently to the \(3t\) selected cyclic frames and
concatenate the resulting words in any order.  Their total length is

\[
                         3t(M+2H)=3Mt+6Ht.                   \tag{3.3}
\]

The independent initialization at the beginning of every frame makes
the incoming residual state irrelevant.  Hence every advertised state
and every OR window (2.7)--(2.9) occurs literally.

Within a packet, the old and new three-frame middle supports are equal
and squarefree.  Top-disjointness plus initial global squarefreeness make
the supports of different packets disjoint.  Thus all \(K\) designated
middle endpoints are distinct for every shore choice. \(\square\)

For a switched packet, the three companion frames are not discarded:
all three new minus cycles are the cycles compiled in Theorem 3.1.  Their
changed annular flags are precisely the conveyor derivative.  Thus no
companion collateral is hidden in a seam or appended as a separate
target list.

### Corollary 3.2 (changed ports pay the complete reset bill)

At protected depth \(\delta\), switching all \(t\) packets changes
\(D=6Lt\) ordered ports.  The nonprincipal word excess in (3.2) obeys

\[
                         E=6Ht\le6Lt=D.                        \tag{3.4}
\]

Consequently the bank has a word-level splice with

\[
                         E=O(t+D),                             \tag{3.5}
\]

with absolute constant one in front of \(D\).

If \(K=\Theta(W)\) and \(H=o(m)\), then

\[
                         E=\frac{2H}{M}K=o(W).                \tag{3.6}
\]

#### Proof

Equation (3.4) uses \(L=H+\delta-1\ge H\).  Equation (3.6) follows from
\(K=3Mt\). \(\square\)

The exact OR ledger at reset endpoints is benign for word length.  There
are exactly \(E\) nonprincipal endpoints.  Each has a nested chain of
suffix ORs and therefore contributes at most one extra occurrence at
any fixed rank.  Cross-seam suffixes are not uncounted objects: they end
at one of these same physical endpoints.  Duplicates may occur, but a
covering word does not pay a second symbol for each rank represented at
one endpoint.

## 4. Insertion into an ambient word

The standalone theorem also gives a literal surgery statement.

### Theorem 4.1 (reset-collared ambient insertion)

Let an ambient literal word be cut into a prefix and suffix, and insert a
bank of \(t\ge1\) conveyor packets between them.  There is an insertion
which

1. represents all \(K=3Mt\) selected bank owners and their chosen flags;
2. preserves every OR witness lying wholly in the old prefix or suffix;
3. uses at most \(K+6Ht\) inserted symbols if the suffix begins with an
   independent useful-prefix initialization; and
4. otherwise uses at most

   \[
                             K+6Ht+2H+1                       \tag{4.1}
   \]

   inserted symbols after reinstalling the first useful state required
   by the suffix.

In the latter case the excess over the \(K\) new principal owners is at
most

\[
                         6Ht+2H+1\le9Lt=\frac32D.             \tag{4.2}
\]

#### Proof

Append the standalone bank word from Theorem 3.1 after the prefix.  Its
first initialization is source-blind, so no entrance collar is needed.
All suffix OR witnesses lying wholly in the old prefix remain unchanged.

If the old suffix begins with an independent initialization, simple
concatenation restores its advertised first state.  Otherwise prepend to
the suffix the reverse-written useful prefix of that first state.  This
uses \(2H+1\) masks.  After it, the old suffix useful chronology and all
of its internal OR witnesses resume exactly; the residual tail may be
refined, but no protected flag reaches it.

Finally \(t\ge1\), \(L\ge H\), and
\(6Ht+2H+1\le9Ht\le9Lt=(3/2)D\). \(\square\)

The theorem does not promise preservation of OR witnesses which formerly
crossed the chosen cut.  Those witnesses can be quarantined at the cut;
there are only the physical endpoints charged in (4.1).  If a particular
compiler relies on essential cross-cut witnesses, their replacement is a
separate path-hitting condition, not an additional hidden symbol cost.

## 5. Common-state zero-addition surgery

The independent-reset bound is sufficient for \(o(W)\), but the
conveyor geometry gives a sharper substitution when the ambient
chronology has a suitable anchor.

Let \(\pi^+,\pi^-\) be the two cyclic orders on one touched top.  They
differ by swapping the labels in two placeholder positions whose two
open gaps are at least \(4H-2\).  Let \(\Omega_i^+,\Omega_i^-\) be their
promotion states from (2.3).

### Lemma 5.1 (exact common-state census)

The two promotion cycles have exactly

\[
                             M-4H                              \tag{5.1}
\]

common full useful states, with the same phase index.

#### Proof

At phase \(i\), the singleton collar of \(\Omega_i\) consists of the
\(2H\) positions immediately preceding the lower block.  A fixed
placeholder position belongs to this collar at exactly \(2H\) phases.
The two phase sets are disjoint because the two open placeholder gaps
are at least \(4H-2>2H-1\).  Hence exactly \(4H\) phases have one
placeholder in the singleton collar.

At every other phase both placeholder labels lie in the unordered lower
block \(L_i\).  Swapping their positions does not change that block, the
singleton list, or the residual block.  Therefore the full states agree
at exactly the remaining \(M-4H\) phases. \(\square\)

### Theorem 5.2 (zero-addition closed-excursion replacement)

Suppose an ambient bridge-one word reaches a common state \(\Omega\),
traverses the complete old promotion cycle as a closed \(M\)-update
excursion from \(\Omega\) back to \(\Omega\), and then continues.  The
old excursion may be replaced by the complete new promotion cycle with

1. exactly the same number \(M\) of symbols;
2. the identical incoming and outgoing last-occurrence state;
3. all \(M\) principal owners and all flags of the new frame; and
4. no changed OR witness outside the replaced excursion.

#### Proof

Choose \(\Omega\) from Lemma 5.1 and cut both directed promotion cycles
there.  Lemma 2.1 gives a closed sequence of \(M\) nonempty updates on
each cycle.  The initial and final state is literally \(\Omega\) on both
sides, so the old and new update blocks have equal length and identical
boundary states.  Substitution therefore leaves the complete prefix and
suffix last-occurrence histories unchanged.

The new closed excursion visits every new frame state; the repeated
return to \(\Omega\) is nonprincipal.  Equations (2.7)--(2.9) give all
advertised OR windows. \(\square\)

Applying Theorem 5.2 separately to all three frames of a packet tracks
the two companion transpositions exactly.  Thus, whenever the ambient
word already supplies three common-state closed excursions, a packet
switch has zero word-length toll.  Constructing such anchored excursions
globally is stronger than top-disjointness and is not assumed in
Theorem 3.1.

## 6. The sharp delay-\(H\) obstruction

The preceding common-state theorem cannot be extended to arbitrary
incoming and outgoing states.

A radius-\(H\) useful prefix has the form

\[
                         \Lambda=(B_1,B_2,\ldots,B_{2H+1}),   \tag{6.1}
\]

where \(|B_1|=m-H\) and \(B_2,\ldots,B_{2H+1}\) are singletons.  Put
\(U_j=B_1\cup\cdots\cup B_j\).  For a source state \(\Sigma\), let
\(t_*(\Sigma,\Lambda)\) be the least \(j\) such that, after deleting
\(U_j\) from every source block, the surviving state begins with
\(B_{j+1},\ldots,B_{2H+1}\).  The exact useful-prefix bridge theorem
gives

\[
             b(\Sigma,\Lambda)=\max\{1,t_*(\Sigma,\Lambda)\}. \tag{6.2}
\]

### Proposition 6.1 (maximum bridge distance is attained)

For every useful prefix \(\Lambda\), the one-block source state

\[
                         \Sigma=([2m])                          \tag{6.3}
\]

satisfies

\[
                         b(\Sigma,\Lambda)=2H+1.              \tag{6.4}
\]

#### Proof

For \(0\le j\le2H\), deleting \(U_j\) from \([2m]\) leaves one block.
At \(j=0\) it is not \(B_1\).  At \(1\le j\le2H\), it contains the
required singleton \(B_{j+1}\) together with additional coordinates,
so it does not begin with the required singleton-block suffix.  Hence no
\(j\le2H\) is admissible.  The empty target suffix makes
\(j=2H+1\) admissible, proving (6.4). \(\square\)

The one-block state is physical: append the nonempty mask \([2m]\) at
one word position.  Therefore no theorem based only on top-disjointness
or middle squarefreeness can promise an \(O(1)\) bridge from an arbitrary
ambient history.

This is the exact delay-\(H\) obstruction.  It costs \(\Theta(H)\) per
independently entered frame, not per changed port.  Theorem 3.1 amortizes
it over \(M\) owners and Corollary 3.2 charges it injectively to the
\(2L\ge2H\) changed ports of that frame.

## 7. Constant-one consequence and remaining gate

Suppose the conveyor-packet hypergraph has a matching of size

\[
                         t=\Theta(W/M)                         \tag{7.1}
\]

inside one middle-squarefree factor.  Then its packet owners have a
literal OR word whose excess is

\[
                         6Ht=O(HW/m)=o(W)                     \tag{7.2}
\]

for every Gaussian \(H=o(m)\).  All companion collateral is internal to
this word, and all selected lower and upper flags are actual suffix ORs.

Hence the interface problem for a top-disjoint bank is solved at the
coefficient-one scale.  The unresolved statements are now strictly
combinatorial:

1. construct the matching (7.1) with its prescribed \(\omega/\omega'\)
   companion templates inside one squarefree owner factor;
2. choose packet signs so the resulting annular flags have only \(o(W)\)
   aggregate holes; and
3. fuse the packet word with the rest of the owner factor, preserving any
   essential cross-cut path-hitting witnesses.

Item 3 has no raw reset-cost obstruction by Theorem 4.1; only the
identity of indispensable cross-cut witnesses remains to be audited.

## 8. Proved versus not proved

Proved here:

1. an explicit literal word of length \(3Mt+6Ht\) for any top-disjoint
   bank and any shore choices;
2. exact principal middle squarefreeness and exact companion inclusion;
3. the complete lower/upper OR-window formulas at every principal
   endpoint;
4. excess at most the \(6Lt\) changed-port count;
5. reset-collared insertion into an ambient word with excess at most
   \((3/2)D\);
6. \(M-4H\) common states per swapped frame and zero-addition closed-loop
   substitution; and
7. the sharp \(2H+1\) arbitrary-history bridge obstruction.

Not proved here:

1. existence of a critical-size conveyor matching;
2. all-depth annular coverage after signing the packets;
3. a global anchored-excursion schedule; or
4. coefficient one without those selection theorems.

## 9. Dependency ledger

The three-top packet, exact middle telescope, squarefreeness, and annular
derivative are in
`MATH_THEOREM_THREE_TOP_TWO_BASE_PROMOTION_CONVEYOR_20260726.md`.
The exact changed-port census and packet matching gate are in
`MATH_THEOREM_THREE_TOP_CONVEYOR_PORT_CATALYSIS_AND_CORE_REORDERING_20260727.md`.
The useful-prefix bridge metric and direct phase compiler are in
`MATH_ATTACK_ORIENTATION_CUBE_DIRECT_LITERALIZATION_INTERFACE_TOLL_20260725.md`.
The promotion-cycle state formulas are the calibrated top-fibre formulas
from
`MATH_ATTACK_CP_CALIBRATED_TOP_PACKET_NEAR_FACTOR_20260725.md`.
