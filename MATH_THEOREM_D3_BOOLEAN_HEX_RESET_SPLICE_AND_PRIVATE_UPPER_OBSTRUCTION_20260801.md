# The depth-three Boolean-hex reset splice and its private upper obstruction

Date: 2026-08-01

Status: exact symbolic support-three lift through the central, suffix, rail,
topology and representative-rainbow rows; exact comparison with the frozen
support-three commutator shell; and a sharp private-context obstruction to
automatic arbitrary-width OR transparency.  A universally transparent
two-reset-block support-three splice is not obtained.

## 0. Verdict

The ternary Boolean hexagon has a lossless depth-three flag lift.  In its
clean common-state form it:

1. preserves lower colours, owners, typed tails and typed heads;
2. preserves both suffix-target multisets;
3. preserves the complete positional rail histograms;
4. is an alternating `C_6` between two rainbow matchings in one state graph;
5. in gain mode replaces two old edges by three and can join two opened
   paths into one.

The flag change is an indispensable cubic on a structural-zero `C_6`; it
cannot be factored through a legal support-two intermediate.  It is
therefore outside the class `C_ov(F)` exhaustively enumerated in
`MATH_THEOREM_A_K17_2E919_CRITICAL_SHORE_SUPPORT3_COMMUTATOR_ESCAPE_20260801.md`.

Two obstructions remain.

* In the displayed forward orientation, all three tail flags delete the
  same coordinate `u` first.  A simple rolling-reset ring contains `u` only
  once, so it can host at most one such native tail flag, irrespective of
  the second state.  Thus every forward-oriented native lift needs three
  reset rings, not two.  Reversing all six directed atoms changes the typed
  tail shore and is not ruled out by this argument.
* At the root chronology level a natural two-open-ring gain embedding exists,
  but its support-three braid changes the arbitrary-width upper deck.  A
  private boundary gives an explicit old-only target.  Thus four-resource,
  suffix and rail neutrality do not imply zero exterior product-grid
  current.

The remaining positive target is either a non-common-state two-ring lift
whose signed upper currents cancel in a prepared host, or a paired
support-six construction using two opposite hex currents.

## 1. The Boolean hexagon

Let `S` have rank `m-2`, and choose four distinct labels

\[
                         a,b,c,u\notin S.             \tag{1.1}
\]

Define rank-`m` roots

\[
 \begin{array}{lll}
 A=S+a+u,&B=S+a+c,&C=S+c+u,\\
 D=S+b+c,&E=S+b+u,&F=S+a+b.
 \end{array}                                         \tag{1.2}
\]

The old and new ordered edges are

\[
 \begin{aligned}
 O&=\{A\to B,\ C\to D,\ E\to F\},\\
 N&=\{A\to F,\ C\to B,\ E\to D\}.                 \tag{1.3}
 \end{aligned}
\]

Their lower/owner pairs are exactly the ternary Boolean-hex identity:

\[
 \begin{array}{c|ccc}
 O&(S+a,S+a+c+u)&(S+c,S+b+c+u)&(S+b,S+a+b+u)\\
 N&(S+a,S+a+b+u)&(S+c,S+a+c+u)&(S+b,S+b+c+u).
 \end{array}                                         \tag{1.4}
\]

Thus the lower and owner multisets agree, while the tail and head sets in
both phases are respectively `{A,C,E}` and `{B,D,F}`.

## 2. Exact common-state flag lift

Choose any

\[
                         w\in S.                     \tag{2.1}
\]

Use the following old flags:

\[
 \begin{array}{c|cccccc}
 q&A&C&E&B&D&F\\ \hline
 f_q^-&(u,w)&(u,w)&(u,w)&(w,a)&(w,c)&(w,b),
 \end{array}                                         \tag{2.2}
\]

and new flags

\[
 \begin{array}{c|cccccc}
 q&A&C&E&B&D&F\\ \hline
 f_q^+&(u,w)&(u,w)&(u,w)&(w,c)&(w,b)&(w,a).
 \end{array}                                         \tag{2.3}
\]

An ordered pair denotes `(z_1,z_2)`.

### Theorem 2.1 (lossless `d=3` hex lift)

Every edge in (1.3) is a literal legal turn under its corresponding flag
phase.  Passing from (2.2) to (2.3) preserves:

1. the multiset of first deletion labels;
2. the multiset of second deletion labels;
3. the rank-`(m-1)` suffix-target multiset; and
4. the rank-`(m-2)` suffix-target multiset.

Hence the Boolean hex is simultaneously resource-zero, target-zero and
rail-flux-zero at depth three.

#### Proof

For `A -> B`, the leaving coordinate is `u`, the common state is `w`, and
the appended second deletion at `B` is `a`, which lies in

\[
                         A-\{u,w\}=(S-w)+a.
\]

The other five turns follow by the cyclic replacements
`a -> c -> b -> a`.

The tail flags are unchanged.  On the heads, both phases use first deletion
`w`, while the second deletions are the same multiset `{a,b,c}`.
Rank-`(m-1)` head suffixes are root-minus-`w` and therefore rootwise fixed.
The old rank-`(m-2)` head suffixes are

\[
                         (S-w)+c, (S-w)+b, (S-w)+a,
\]

and the new suffixes cyclically permute these three sets.  Tail suffixes are
unchanged. `square`

The packet need not itself be a balanced standalone flag table; its exact
claim is that the phase change has zero rail and target current inside an
already balanced ambient table.

## 3. It is an indispensable cubic, not an overlapping binary commutator

Only the three head flags change.  At rank `m-2`, their signed deltas are

\[
 \begin{aligned}
 \delta_B&=e_{(S-w)+a}-e_{(S-w)+c},\\
 \delta_D&=e_{(S-w)+c}-e_{(S-w)+b},\\
 \delta_F&=e_{(S-w)+b}-e_{(S-w)+a}.
 \end{aligned}                                         \tag{3.1}
\]

They are nonzero and sum to zero.  The legal option graph is

\[
 B:\{a,c\},\qquad D:\{b,c\},\qquad F:\{a,b\},       \tag{3.2}
\]

which is the chordless bipartite `C_6=K_(3,3)-I`.

### Theorem 3.1 (structural-zero separation from `C_ov`)

The cubic change (3.1) is primitive and has no legal support-two
factorization.  In particular it does not belong to the overlapping
support-two commutator class `C_ov(F)`.

#### Proof

A support-two factorization would require a nontrivial `2 x 2` square in
(3.2), so that two roots could swap their assigned suffix values.  Every two
rows in (3.2) have only one common value; the fourth corner of such a square
is a structural zero.  Equivalently, the toric ideal of this six-cycle is
generated by the displayed cubic. `square`

The frozen `k=17` commutator census proves that many members of `C_ov(F)`
raise the common matching by one.  Theorem 3.1 is complementary: the Boolean
hex gives a uniform symbolic primitive triple in the shell explicitly
excluded from that census.  Whether a translated copy crosses its particular
critical DM shore is a separate host-selection question.

## 4. Exact representative-rainbow action

All six edges lie in the state graph `G_w`.  The two phases are the two
perfect matchings of its alternating six-cycle.  Their three owner colours
are the same sets in (1.4).

Delete the old edge `E -> F`, writing

\[
                         O^-=\{A\to B,C\to D\}.       \tag{4.1}
\]

The four resources of the missing atom are

\[
 (S+b, S+a+b+u, E, F).                            \tag{4.2}
\]

### Theorem 4.1 (one-unit rainbow augment)

If a residual owner-coloured state matching contains `O^-` and the lower
colour, owner colour, tail and head in (4.2) are free, replacing `O^-` by
`N` raises its size by one and preserves injectivity in all four resources.

Thus the packet is a literal three-edge augmenting ear for the complementary
rainbow `G_0` gate isolated by the bidirectional-reset theorem.

There is an important projection distinction.  Put

\[
 o_1=S+a+c+u,\quad o_2=S+b+c+u,\quad o_3=S+a+b+u.
\]

For the **complete** phase toggle,

\[
 \alpha(O)=\{(B,o_1),(D,o_2),(F,o_3)\}=\alpha(N),
\]

where `alpha` is the head--owner attachment projection.  Thus `O <-> N`
has zero attachment action and cannot close the opened reset's attachment
path.  The gain mode `O^- -> N` augments only because it adds the entire
missing atom `(E,F,o_3,S+b)`; its two sides have different cardinalities.
It is not by itself a phase-balanced compatible three-return lift.  This
scope is developed in
`MATH_THEOREM_PIVOT_CORRIDOR_HEX_RESET_COMPOSITION_GATE_20260801.md`.

#### Proof

The resource identity (1.4) says precisely

\[
                         res(N)=res(O^-)\mathbin{\dot\cup}res(E\to F).
\]

Every new edge is in `G_w` by Theorem 2.1. `square`

## 5. Topological gain mode

Suppose the old edges `A -> B` and `C -> D` lie on two directed paths.  Cut
them, and suppose `E` is the free tail endpoint of the first path while `F`
is the free head endpoint of the second.  Write the four resulting fragments
as

\[
 H_1\Longrightarrow A,\quad B\Longrightarrow E,
 \quad F\Longrightarrow C,\quad D\Longrightarrow T_2.       \tag{5.1}
\]

Then the new edges give the single path

\[
 H_1\Longrightarrow A\to F\Longrightarrow C\to B
 \Longrightarrow E\to D\Longrightarrow T_2.        \tag{5.2}
\]

So support three is centrally and topologically sufficient to join two
opened path components.  This is the gain-ear form of the Boolean hex, not
a two-edge component switch.

## 6. Why the forward-oriented lift cannot live in only two simple reset rings

In every legal flag lift of the forward-oriented atoms (1.3), the three
tail flags at `A,C,E` all have first deletion coordinate `u`, because

\[
 A-B=C-D=E-F=\{u\}
\]

on the directed tail side.  In the common-state lift (2.2), they even begin
with the same ordered rail word

\[
                         (u,w).                      \tag{6.1}
\]

A simple rolling-reset ring is induced by one cyclic order of distinct
private coordinates.  The coordinate `u` occurs only once in that order,
so the native tail flag beginning with `u` occurs at most once.  This is
stronger than merely observing that a fixed ordered pair occurs once.

### Proposition 6.1 (forward three-return obstruction)

No flag lift of the forward-oriented Boolean hex (1.3) can plant all three
tail flags natively in only two simple rolling-reset rings.  Each ring can
contain at most one native flag whose first deletion is `u`, whereas the
three tails `A,C,E` all require one.  Hence at least three rings are needed.

The general flag-signature census in Section 8 does find non-common-state
neutral lifts, but their forward tails still share first deletion `u`, so
they do not evade this pigeonhole obstruction.  Reversing every atom swaps
the typed tail/head shores: the reversed tails `B,D,F` leave by the three
distinct labels `c,b,a`.  Proposition 6.1 does **not** rule out that reversed
orientation or a more general host which is not a pair of simple reset
rings.

## 7. A central two-ring embedding and the upper-deck failure

There is nevertheless a literal two-ring embedding of the six **roots** and
the gain-ear topology.  Put

\[
                         S=K+\{w\},\qquad |K|=m-3,    \tag{7.1}
\]

and choose six further private labels `p_1,p_2,p_3,q_1,q_2,q_3`.  Use the
two cyclic private orders

\[
 \begin{aligned}
 P&=(b,u,w,a,c,p_1,p_2,p_3),\\
 Q&=(u,c,w,b,a,q_1,q_2,q_3).                        \tag{7.2}
 \end{aligned}
\]

Their length-three root windows contain

\[
 E,A,B\quad\hbox{at starts }0,1,2\text{ of }P,
 \qquad
 C,D,F\quad\hbox{at starts }0,1,2\text{ of }Q.      \tag{7.3}
\]

Open `P` at `E -> A` and `Q` at `D -> F`.  The old internal edges are
`A -> B` and `C -> D`, with `E` a free tail and `F` a free head.  Thus the
central gain braid (5.2) is physically available.

The native reset flags at all six roots cannot realize any forward-oriented
hex lift by Proposition 6.1.  More decisively, even if one
forgets that flag mismatch and compares the direct-seam root chronology
with the Boolean-hex braid, their arbitrary-width union decks differ.

For pairwise private `p_i,q_i`, the direct chronology has the interval of
three roots ending immediately before and after the direct `E -> F` seam
whose union, after suppressing `K`, is

\[
                         \{p_3,b,u,w,a\}.             \tag{7.4}
\]

The braided chronology replaces the corresponding boundary by `E -> D`;
its private distinguished value is

\[
                         \{p_3,b,u,w,c\}.             \tag{7.5}
\]

Because `p_3` occurs only in the first ring's private boundary collar, no
other interval in the braided chronology recreates (7.4).

### Theorem 7.1 (private-context support-three no-go)

The two-ring Boolean-hex gain braid is not context-independently
arbitrary-width upper transparent.  There are private reset collars for
which it loses (7.4) and creates (7.5), despite preserving all four central
resources.

Consequently no theorem using only the Boolean-hex resource identity,
suffix rows and rail histograms can certify a universal one-hex word splice.
An ambient duplicate witness or an opposite signed boundary current is
necessary.

## 8. Exact computational replays

The general flag-signature census enumerates every legal old and new
three-edge hex lift for core sizes `2,...,6`.  It finds many non-common-state
neutral signatures.  They remain subject to the forward first-deletion
obstruction, but they show that common-state equality is not forced by the
suffix/rail equations themselves.  The old/new common-signature counts are

\[
                         18,78,236,570,1182.          \tag{8.1}
\]

The direct-versus-braided root-deck replay for (7.2) reports

```text
D3_RESET_HEX_UPPER_DECK direct_distinct=99 braid_distinct=99
oldonly_mult=34 newonly_mult=34 l1=68 exact=0
old_witness value=151 interval=6,8
```

The bitmask `151` is exactly (7.4) under the audit's label map.

These are finite confirmations of the symbolic identities and the displayed
private counterexample.  They do not exhaust non-common-state hosts or
paired-hex constructions.

## 9. Sharpened remaining packet

The minimum central/rainbow/topological support is three, and its exact
packet is now known.  The full-word target is stricter:

> Find two native reset paths supporting a **reversed-orientation** or other
> tail-diverse Boolean hex for which the old/new suffix inventories agree
> and the signed prefix/suffix product-grid current is zero; or pair two
> hexes with opposite currents while keeping their six owner colours
> distinct and their residual rainbow augmentations compatible.

The first alternative would be the true minimum support-three splice.  The
private-context theorem proves that it cannot follow from local central
algebra alone.  The second has support six but matches the exact
mirror-current mechanism of the bidirectional phase theorem.
