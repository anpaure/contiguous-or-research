# Opposed hinges have sharp complementary-profile rings

## Status

This note solves the **local macroscopic profile-completion problem** for a
singleton-spine opposed hinge.  A bare opposed hinge cannot be balanced by a
constant endpoint gadget, but it does have an explicit literal cyclic
completion of the least possible period in the private-marker/common-core
class.  The completion is state-balanced, owner-once, Johnson-simple,
doubly `q1`-rainbow, and named-simple at every proper source width.

There is also a slightly longer antipodal completion in which every moving
coordinate has both owner-run and owner-gap exactly `d+1`.  Thus the
positional deficit of the large hinge layer is not an impossibility: it is
paid by a macroscopic complementary profile.  What is not proved here is a
partition of the full owner shore, or an exact global named-target factor.

## 1. Source-state balance and its positional projection

Put

\[
                            D=d+1.                         \tag{1.1}
\]

A two-owner depth-`d` macro is a word

\[
                   X=(B_0,B_1,\ldots,B_D).                 \tag{1.2}
\]

Its tail and head states are

\[
 P(X)=(B_0,\ldots,B_{D-2}),\qquad
 Q(X)=(B_2,\ldots,B_D).                                   \tag{1.3}
\]

For a finite multiset `M` of macros, exact state balance means

\[
                    \sum_{X\in M}[P(X)]
                      =\sum_{X\in M}[Q(X)]                \tag{1.4}
\]

in the free abelian group on literal `(D-1)`-states.

For any source-letter statistic `phi`, define

\[
 H_t^\phi(M)=\sum_{X\in M}\phi(B_t(X)).                    \tag{1.5}
\]

### Lemma 1.1 (two parity profiles)

Exact state balance implies

\[
                   H_t^\phi(M)=H_{t+2}^\phi(M)
                    \qquad(0\le t\le D-2)                 \tag{1.6}
\]

for every statistic `phi`.  Hence every additive source-position profile is
constant separately on the even and odd positions.

Conversely, exact state balance is equivalent to saying that the directed
multigraph with arcs `P(X)->Q(X)` is Eulerian.  Every connected Eulerian
component is a cyclic source word: there are literal letters

\[
                         L_0,\ldots,L_{2q-1}                \tag{1.7}
\]

such that its macros are the length-`(D+1)` factors beginning at the even
phases.

#### Proof

Project (1.4) onto coordinate `t` of the state and then apply `phi`.  The
tail coordinate is macro position `t`, while the head coordinate is macro
position `t+2`, proving (1.6).  The second assertion is the ordinary Euler
decomposition.  Along consecutive arcs, equality of head and tail states
identifies source positions after a shift by two, yielding (1.7).  Conversely
every cyclic source word is balanced under that shift.  \(\square\)

The rank obstruction for the one-spine portal bank is the instance of
(1.6) in which `phi(B)=1_{|B|=r-d}` and `t=1,3`.  The construction below
cancels it at the level of full literal states, not merely ranks.

## 2. The bare singleton-spine hinge

Let `K` be a set of size

\[
                           |K|=r-D.                         \tag{2.1}
\]

Choose pairwise distinct labels

\[
 a,b,x,m_2,\ldots,m_{D-1}                                 \tag{2.2}
\]

outside `K`, and optional endpoint subsets
`A_0,A_D\subseteq K`.  The word

\[
 (\{a\}\cup A_0, K\cup\{x\},
       \{m_2\},\ldots,\{m_{D-1}\},
       \{b\}\cup A_D)                                    \tag{2.3}
\]

has `D+1` letters.  It is exactly the opposed-hinge word with one large
layer `K+x` and `D-2=d-1` singleton layers.  Its two owner windows are

\[
 K\cup\{a,x,m_2,\ldots,m_{D-1}\},\qquad
 K\cup\{b,x,m_2,\ldots,m_{D-1}\}.                         \tag{2.4}
\]

The optional subsets do not change the owners.

## 3. Sharp short complementary completion

Let

\[
 L_0=\min\{L:L\text{ is even and }L\ge D+2\}
 =\begin{cases}
 D+2,&D\text{ even},\\
 D+3,&D\text{ odd}.
 \end{cases}                                               \tag{3.1}
\]

Choose distinct private labels `f_0,...,f_(L_0-1)` and identify

\[
 f_0=a,\quad f_1=x,\quad f_i=m_i\ (2\le i<D),\quad f_D=b.  \tag{3.2}
\]

Define a cyclic source word by

\[
 B_t=\{f_t\}\cup C_t,                                     \tag{3.3}
\]

where

\[
 C_0=A_0,\quad C_D=A_D,\quad C_1=C_{D+1}=K,\quad
 C_t=\varnothing\text{ otherwise}.                         \tag{3.4}
\]

### Theorem 3.1 (sharp complementary-profile ring)

Assume `D>=3` and `r>=D+1`, with enough ground labels for (3.2).  The
cyclic word (3.3) has all of the following properties.

1. Its macros beginning at the even phases form one exact state-balanced
   component of size `L_0/2`.
2. Its `L_0` length-`D` owner windows are distinct rank-`r` sets and form a
   simple Johnson cycle.
3. Its `L_0` immediate-lower roots and `L_0` immediate-upper colours are
   separately pairwise distinct.
4. The macro beginning at phase zero is exactly (2.3).
5. For every `1<=q<D`, all `L_0` cyclic width-`q` source unions are
   pairwise distinct.
6. Within the private-marker/common-core class (3.3), with `A_0=A_D=emptyset`,
   no shorter owner-once state component can contain the bare word (2.3).

#### Proof

The two full-core phases are `1` and `D+1`.  Their cyclic separation in one
direction is `D`; in the other it is `L_0-D`, equal to two or three.  Thus
every cyclic interval of `D` source phases contains at least one full-core
phase.  Its union is therefore

\[
                  K\cup\{f_t,f_{t+1},\ldots,f_{t+D-1}\}.  \tag{3.5}
\]

This has rank `(r-D)+D=r`.  Distinct proper cyclic `D`-intervals of the
private labels give distinct owners.  Shifting the window once deletes
`f_t` and inserts `f_(t+D)`, so consecutive owners are Johnson adjacent.

Since `L_0` is even, shifting macro starts by two visits exactly the
`L_0/2` even phases, and the two owner windows of those macros partition all
`L_0` owner starts.  Head-tail equality is literal under the shift, proving
state balance and owner-once use.

The lower root of a transition is `K` plus the cyclic `(D-1)`-interval of
private labels common to its two owners.  The upper colour is `K` plus the
cyclic `(D+1)`-interval.  Both lengths are strictly between zero and
`L_0`, so the private-label set recovers the start phase.  This proves the
two rainbow assertions.

Equations (3.2)--(3.4) make phases `0,...,D` exactly (2.3).  Finally, every
proper width-`q` union contains the private-label set

\[
                         \{f_t,\ldots,f_{t+q-1}\}.          \tag{3.6}
\]

Distinct cyclic `q`-intervals of distinct labels are distinct, irrespective
of their additional core part.  This proves item 5.

For sharpness, exact one-copy two-step balance has an even source period
`L>D`.  The locked word (2.3) occupies phases `0,...,D`.  If `L=D+1`, it
occupies the entire period.  With empty endpoint subsets, `K` then occurs
only at phase one.  The length-`D` owner window omitting phase one has rank
only `D<r`, contradiction.  Hence `L>=D+2`; parity forces `L>=L_0`.
\(\square\)

The theorem gives only two complementary templates, according to the
parity of `D`.  Its component size is asymptotic to `d/2`, matching the
general lower bound for distinct-owner two-step components.

### Corollary 3.2 (parity-free whole-ring completion)

If the packet interface accepts a whole cyclic source ring under the
one-source shift, rather than requiring a partition into disjoint
shift-two macros, take

\[
                              L=D+2.                         \tag{3.7}
\]

for both parities of `D`, with the same full-core phases `1,D+1`.  The
result is a literal owner-once ring satisfying items 2--5 of Theorem 3.1,
and `D+2` is the least possible period in the same bare private-marker
class.

#### Proof

The proof of Theorem 3.1 uses evenness only when decomposing the source
cycle into shift-two macros.  For `L=D+2`, the full-core phases have cyclic
gaps `D` and two, so every owner window still meets one.  The one-source
translation is itself a balanced cyclic chronology and uses every owner
start once.  The sharpness argument already gives `L>=D+2`.  \(\square\)

## 4. Exact two-sided-resident completion

The short ring has moving-coordinate zero gaps of only `L_0-D`, which is
two or three.  If both positive runs and zero gaps must have length at least
`D`, use an antipodal private-label ring instead.

Choose disjoint labels

\[
 u_0,\ldots,u_{D-1},v_0,\ldots,v_{D-1}                    \tag{4.1}
\]

outside `K`, with

\[
 u_0=a,\quad u_1=x,\quad u_i=m_i\ (2\le i<D),\quad v_0=b. \tag{4.2}
\]

On the cyclic period `2D`, put

\[
 \begin{aligned}
 B_0&=\{u_0\}\cup A_0,& B_D&=\{v_0\}\cup A_D,\\
 B_1&=K\cup\{u_1\},& B_{D+1}&=K\cup\{v_1\},\\
 B_i&=\{u_i\}\quad(2\le i<D),&
 B_{D+i}&=\{v_i\}\quad(2\le i<D).
 \end{aligned}                                             \tag{4.3}
\]

### Theorem 4.1 (antipodal perimeter completion)

The `D` even-start macros in (4.3) form one exact state-balanced component
with:

1. `2D` distinct rank-`r` owners forming the perimeter cycle of the paired
   transversal cube on pairs `{u_i,v_i}`;
2. distinct immediate-lower and immediate-upper colours;
3. the original opposed hinge at phase zero;
4. pairwise distinct source-union targets at every width `1<=q<D`; and
5. for every noncore coordinate, one owner-run and one owner-gap, both of
   length exactly `D`.

#### Proof

Every cyclic `D`-interval of a `2D`-cycle contains exactly one of the two
antipodal phases `i,D+i`, for every `i`.  It also contains exactly one of
the two full-core phases `1,D+1`.  Therefore its owner is

\[
              K\cup\{w_0,\ldots,w_{D-1}\},
              \qquad w_i\in\{u_i,v_i\},                   \tag{4.4}
\]

and has rank `r`.  Shifting once changes exactly the antipodal pair whose
phase leaves and enters.  The resulting `2D` owners traverse the two
oppositely oriented monotone geodesics between the all-`u` and all-`v`
transversals, hence form a simple perimeter cycle.

An immediate-lower root contains neither member of the unique changing
pair and one member of every other pair.  An immediate-upper colour
contains both members of the changing pair and one of every other pair.
These descriptions recover the transition and prove both palettes simple.

The even-start shift gives one component and uses all owners exactly once,
as in Theorem 3.1.  Phases `0,...,D` are (2.3).  At a proper source width
`q<D`, the noncore part is the set of the `q` distinct phase labels in that
cyclic interval; it recovers the start phase, proving named simplicity.

Finally a private coordinate occurs in one source phase.  Exactly the `D`
owner windows containing that phase contain the coordinate, while the
other `D` do not.  Core coordinates occur in every owner.  This proves the
residence statement.  \(\square\)

## 5. Exact profile ledger and scope

In the original hinge macro, macro position one carries the large letter
`K+x`, while the later internal positions are singletons.  In either
completion, the other macros are precisely the complementary positional
profiles forced by Lemma 1.1.  Thus the large-layer deficit is cancelled
without an external seasoning word and without sacrificing owners, `q1`,
or named simplicity.

The result is local.  It does **not** assert any of the following:

1. that the complete rank-`r` owner shore decomposes into these rings;
2. that the named targets emitted by different rings are disjoint or form
   the prescribed complete lower palette;
3. that the rational pull-clock densities round to integral ring profiles;
4. that the ring components fuse while retaining the same target table.

Consequently this theorem removes the local state-balance obstruction for
an opposed hinge, but it does not by itself prove `B(k)+O(1)`.  The next
global object is a matching/decomposition in the hypergraph of decorated
complementary-profile rings, with simultaneous owner and named-target
coordinates.
