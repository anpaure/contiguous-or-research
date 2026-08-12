# Exact compatibility of two consecutive minimal common-history C6 packets

**Date:** 2026-08-05  
**Method:** literal overlap of two sliding source fragments; no computation
or search  
**Status:** unconditional pair criterion and positive literal PBBS
evaluation.  The canonical consecutive leaf-plucking packets have disjoint
shared-owner screens, so their two minimal depth-`d` histories coexist
whenever `r-4>=d-1`.

## 1. Two adjacent owner transitions

Let a depth-`d` source word contain two consecutive owner transitions at
indices zero and one.  A minimal common-history decoration of transition
zero has fragment

\[
 A_0,\ A_1,\ldots,A_d,\ A_{d+1},                  \tag{1.1}
\]

where `A_0,A_(d+1)` are its two-set screens and

\[
                         K_0=A_1\dot\cup\cdots\dot\cup A_d  \tag{1.2}
\]

is its rank-`(r-2)` clean core.

The adjacent packet has fragment

\[
 A_1,\ A_2,\ldots,A_{d+1},\ A_{d+2},              \tag{1.3}
\]

with two-set screens `A_1,A_(d+2)` and core

\[
                         K_1=A_2\dot\cup\cdots\dot\cup A_{d+1}. \tag{1.4}
\]

Let

\[
 S=A_1,qquad T=A_{d+1},qquad
 M=A_2\dot\cup\cdots\dot\cup A_d.                \tag{1.5}
\]

For `d=1`, interpret `M=emptyset` and the displayed empty partition
literally.

The screen `S` is prescribed as the second packet's left active pair and is
disjoint from its core `K_1`.  The screen `T` is prescribed as the first
packet's right active pair and is disjoint from `K_0`.

## 2. Pair criterion

### Theorem 2.1 (core exchange criterion)

The two prescribed minimal packet decorations coexist in one source word if
and only if

\[
 K_0\setminus K_1=S,
 \qquad
 K_1\setminus K_0=T,                               \tag{2.1}
\]

and the common intersection

\[
                         M=K_0\cap K_1             \tag{2.2}
\]

admits a partition into `d-1` nonempty source letters.

Equivalently:

1. `|K_0 triangle K_1|=4`, with two coordinates in each direction;
2. the two directed differences are exactly the prescribed shared-owner
   screen pairs; and
3. `|K_0 cap K_1|=r-4>=d-1` for `d>=2` (while `d=1` forces `r=4`).

#### Proof

If the source fragments coexist, (1.2)--(1.5) give

\[
                         K_0=S\dot\cup M,
 \qquad K_1=M\dot\cup T.                           \tag{2.3}
\]

Because `S` is a screen of the second packet, `S cap K_1=emptyset`; because
`T` is a screen of the first, `T cap K_0=emptyset`.  Equation (2.3) therefore
implies (2.1)--(2.2), and the middle source letters give the required
partition.

Conversely, partition `M` into `A_2,...,A_d`, put `A_1=S` and
`A_(d+1)=T`, and use the prescribed exterior screens at `A_0,A_(d+2)`.
Then (1.2) and (1.4) hold literally.  Each packet is a valid minimal
common-history fragment, and the two shared fragments agree at every
overlapping source position.  \(\square\)

### Corollary 2.2 (shared-owner screen form)

Let `V` be the rank-`r` owner shared by the two transitions, let `T` be the
first packet's right screen in `V`, and let `S` be the second packet's left
screen in `V`.  Since

\[
                         V=K_0\dot\cup T=K_1\dot\cup S,         \tag{2.4}
\]

the criterion is equivalent simply to

\[
                         S\cap T=emptyset                       \tag{2.5}
\]

plus partitionability of `V\setminus(S\cup T)` into `d-1` nonempty
letters.

#### Proof

From (2.4), `K_0=V\T` and `K_1=V\S`.  Hence

\[
 K_0\setminus K_1=S\setminus T,
 \qquad K_1\setminus K_0=T\setminus S.
\]

These equal the full two-set screens exactly when the screens are disjoint.
The common core is then `V\(S union T)`.  \(square\)

## 3. Literal PBBS sibling screens are disjoint

Take two consecutive cool-lex leaf-plucking packets `A,B`.  On their shared
child, the first uses role `E_2` with center shape `10F_A`, while the second
uses role `E_1` with center shape `F_B10`.  Both factor edges have the
orientation `P_i -> Q_i`.  Hence the first packet's right screen and the
second packet's left screen are

\[
 T=\{c_A,a_2^A\},
 \qquad
 S=\{a_1^B,a_2^B\}.                               \tag{3.1}
\]

The first changed edge is the second packet's incoming companion at the
shared owner.  Its q1 row is both

\[
                         O-c_A
 \quad\hbox{and}\quad
                         O-d_B,
\]

where `d_B` is packet `B`'s common companion deletion.  Thus

\[
                         c_A=d_B\in K_B,             \tag{3.2}
\]

and `c_A notin S`.  It remains to exclude `a_2^A` from `S`.

### Lemma 3.1 (rooted active-label exclusion)

For consecutive packet centers as above,

\[
                         a_2^A\notin\{a_1^B,a_2^B\}. \tag{3.3}
\]

#### Proof

Retain physical coordinate labels.  The first center has cyclic rooted word

\[
 X=0_{a_0^A}\,1_{a_1^A}0_{a_2^A}D,               \tag{3.4}
\]

where the displayed initial zero is the forward survivor and `D=F_A` is a
hook Dyck word of height `h>=3`.

Let `s` be the last up-step which reaches the rightmost height-`h` maximum
of `D`.  The PBBS formula

\[
                         f(Z)=Z^c\setminus\{r_+(Z)\} \tag{3.5}
\]

first gives

\[
 f(X)=0_{a_0^A}\,0_{a_1^A}1_{a_2^A}\,\overline D. \tag{3.6}
\]

In (3.6), the rightmost global height minimum occurs at the complemented
step `s`: minima of `bar D` are maxima of `D`, and `h>=3` makes this lower
than either initial prefix minimum.  The forward cycle lemma therefore gives

\[
                         r_+(f(X))=s.               \tag{3.7}
\]

Every coordinate except the two successive survivors is complemented twice.
Consequently

\[
 g(X)=f^2(X)
 =1_{a_0^A}1_{a_1^A}0_{a_2^A}D^{\downarrow s},    \tag{3.8}
\]

where `D^(downarrow s)` is obtained by changing the up-step `s` to zero.

The same state is packet `B`'s center of shape `F_B10`; with its physical
root labels it is

\[
 g(X)=0_{a_2^B}\,F_B\,1_{a_0^B}0_{a_1^B}.         \tag{3.9}
\]

In particular `a_1^B` is immediately followed cyclically by the zero root
`a_2^B`.

Let `u` be the first step of `D`.  It is an up-step.  Since `h>=3`, the
last up-step `s` reaching height `h` is not `u`; hence `u` remains a one in
(3.8).  The cyclic successor of `a_2^A` is exactly `u`.  Therefore
`a_2^A` cannot equal `a_1^B`, whose cyclic successor `a_2^B` is zero.

If `a_2^A=a_2^B`, cutting (3.8) after that coordinate would make the
purported Dyck word

\[
                         D^{\downarrow s},11.       \tag{3.10}
\]

But `D^(downarrow s)` has total height `-2`; its complete prefix in (3.10)
is negative before the final two ones.  It is not Dyck, contradicting that
`a_2^B` is the forward root in (3.9).  This excludes the second possibility
and proves (3.3).  \(\square\)

Combining (3.2)--(3.3) gives

\[
                         S\cap T=\varnothing.        \tag{3.11}
\]

### Corollary 3.2 (canonical adjacent sibling compatibility)

For `r-4>=d-1`, the two forced consecutive packet occurrences on every
internal cool-lex sibling child admit simultaneous minimal depth-`d`
common-history decorations.  Their shared middle history is any partition
of the rank-`(r-4)` set `O\setminus(S\cup T)` into `d-1` nonempty letters.

## 4. Consequence for a subcubic packet tree

The long-rail cardinality obstruction requires `d+1` consecutive packet
edges on one physical source component.  It does not apply merely because a
sibling path has many packets: before rethreading, each internal child
component of that path is shared by its two incident packets.

For such a child, Corollary 2.2 is the complete minimal-source test:

> the outgoing screen of the first literal PBBS packet and the incoming
> screen of the next must be disjoint inside their shared owner.

Lemma 3.1 proves that it does hold for the literal PBBS sibling overlap.
If the remaining packet shores and any third incidence at a subcubic node
are separated by the available rotations, all forced pairwise overlaps have
compatible minimal histories.  A global serial order and the already proved
directed q2-halo identity are still required to turn those local overlaps
into one final chronology.

## 5. Scope

The theorem closes the only **forced consecutive** source overlap in the
sibling formula `S -> gS -> g^2S`.  It does not prove simultaneous rotation
separation of every optional/third incidence at all subcubic nodes,
arbitrary upper safety, zero-gap residence, common-cap compatibility, or the
global contour order.
