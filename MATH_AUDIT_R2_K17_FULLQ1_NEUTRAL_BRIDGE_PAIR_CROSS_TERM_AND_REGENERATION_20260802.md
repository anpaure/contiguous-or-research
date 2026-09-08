# R2 audit: K17 full-q1 neutral bridge, quadratic pair cross-term, and regeneration gate

**Date:** 2026-08-02  
**Status:** exact algebraic extraction from the independently replayed
`strict17 -> escape_s2_bridge -> escape_s2_quench` packet.  The displayed
packet is positive; uniform regeneration is stated only as a sufficient
hypothesis.  No resident, source, compiler, or word claim is made.

## 1. Frozen packet and literal scope

The predecessor is `fullq1_strict17.best.model` (also frozen as the
residence-2025 checkpoint):

```text
SHA-256 5499b2fb492a6307e531bf33f20341a3e1c89c44cd45e0ee88ae6a8556c5e4fa
```

The promoted packet consists of one neutral `C6` bridge followed by three
state-relative star-`C8` quenches:

| stage | row | kind | roots | old incidences | new incidences |
|---|---:|:---:|---|---|---|
| bridge | 2508 | C6 | `15672,15768,16152` | `25943,26169,26860` | `26167,26862,25944` |
| quench 1 | 2446 | C8 | `15129,16152,15130,47896` | `24702,26858,24713,87553` | `26857,24711,87554,24704` |
| quench 2 | 12688 | C8 | `104210,112386,104226,120578` | `186038,199229,186075,210811` | `199228,186074,210812,186039` |
| quench 3 | 2243 | C8 | `13625,13626,15672,79160` | `21223,25940,142666,21222` | `21214,21228,25947,142660` |

The three quench circuits are root-disjoint from one another.  The bridge
shares root `16152` with row 2446 and root `15672` with row 2243.  Hence the
complete packet has 13 distinct roots and toggles 15 distinct old plus 15
distinct new incidences.

The independent promoted-prefix replay is

```text
/home/amodo/or15/work/audit_k17_fullq1_floor_compounds_20260802/
  promoted_moves.tsv
SHA-256 8ae21b56cec03e04386b3c2f8aad441ec1421e5c9f3387d3da744a4aaf9d2488
```

It verifies at every displayed prefix: minimum ordinary non-`D` q1 provider
load at least one and opened rank-ten holes `[0,0]`.  Its verifier source has
SHA-256
`46e0ddaa3ccca27bc853d8ab27d9094614f900c81cf071cd09c0953978d8a22e`.
The final factor and its independent checkpoint are

```text
escape_s2_quench.best.model
  c8f961413aeea43cbad5036e801c08f854f84889eaef11c281aa83bea46c057d
checkpoint_fullq1_escape_res2018/independent.audit.json
  885f62c5b7689ada00970688a9771a5bcaa543657e3fae3d065aed3d1f41cb9d
```

The final replay has one connected normalized lollipop, all 16,261 guards,
full ordinary q1, opened q1 holes `[0,0]`, and literal opened residence
`2025 -> 2018` in the best orientation, in fact `2018` in both orientations.

## 2. The bridge is an exact palette-multiset permutation

Write an ordinary root state as the unordered pair of its two selected
rank-nine owners.  The bridge performs

```text
L=15672: {15674,15800} -> {15674,16184}
L=15768: {15770,16280} -> {15770,15800}
L=16152: {16154,16184} -> {16154,16280}.
```

The corresponding rank-ten colours are

```text
before: 15802,16282,16186
after:  16186,15802,16282.
```

Thus the bridge does not merely preserve colour support.  It exactly
permutes the colour multiset

\[
                    \{15802,16186,16282\}.             \tag{2.1}
\]

Every other ordinary root is unchanged, so every ordinary q1 multiplicity
is identical before and after the bridge.  The bridge is also a literal hard
face move and has reported ordinary residence delta zero.  This neutrality
does not imply that its pair-channel or topology state is unchanged.

## 3. Two-slot turnover at the repeated roots

At the two roots later revisited by the quench, the bridge changes one slot
and a quench changes the complementary slot:

```text
L=15672:
  base       {15674,15800}
  bridge     {15674,16184}
  final      {81208,16184}

L=16152:
  base       {16154,16184}
  bridge     {16154,16280}
  final      {16153,16280}.
```

Equivalently, the aggregate incidence current at either repeated root has
two `-1` and two `+1` entries while its row sum is zero.  Each constituent
circuit has zero owner boundary, so for the full signed current `z`

\[
 \sum_{T\supset L}z_{L,T}=0\quad(L\text{ every root}),
 \qquad
 \sum_{L\subset T}z_{L,T}=0\quad(T\text{ every owner}). \tag{3.1}
\]

This explains the census `13 roots / 15 old / 15 new`; root support is not
the number of toggled old incidences when a repeated root turns over both
slots.

## 4. Exact quadratic pair cross-term

At an ordinary root `L`, write the pair channel as

\[
                 p_{\{u,v\}}(y)=y_u y_v\qquad(u\ne v), \tag{4.1}
\]

where `u,v` abbreviate the two incidences `(L,u),(L,v)`.  Suppose the base
pair is `{a,b}`, the bridge switches `a -> a'`, and the quench switches the
complementary slot `b -> b'`.  Put

\[
 z_b=e_{a'}-e_a,\qquad z_q=e_{b'}-e_b.             \tag{4.2}
\]

For every unordered pair coordinate the exact identity is

\[
 p(y+z_b+z_q)-p(y)
 =\bigl[p(y+z_b)-p(y)\bigr]
 +\bigl[p(y+z_q)-p(y)\bigr]+C(z_b,z_q),           \tag{4.3}
\]

where

\[
 C_{\{u,v\}}(z_b,z_q)=z_b(u)z_q(v)+z_q(u)z_b(v). \tag{4.4}
\]

In basis-vector notation,

\[
\begin{aligned}
 \Delta p_b&=[a',b]-[a,b],\\
 \Delta p_q^{\rm base}&=[a,b']-[a,b],\\
 C&=[a',b']-[a',b]-[a,b']+[a,b],
\end{aligned}                                      \tag{4.5}
\]

and therefore

\[
             \boxed{\Delta p_{b+q}=[a',b']-[a,b].} \tag{4.6}
\]

The cross-term is nonzero at roots `15672` and `16152`.  Consequently,
adding independently computed base-local pair or colour deltas is unsound.
The final pair variables, guard literals, and q1 multiplicities must be
rebuilt from the materialized incidence state.  Root-disjointness of the
three quench rows does not remove this bridge--quench interaction.

## 5. Enabled schemas and topology

Let `Q(F)` be the complete declared circuit catalogue rebuilt from literal
factor `F`.  The bridge changes selected incidences and the quadratic pair
state at two later-revisited roots.  Therefore one must recompute
alternation, guards, and connectivity at the bridge endpoint; the safe
statement is

\[
 Q(F)\text{ and }Q(bF)\text{ need not be equal}.        \tag{5.1}
\]

A root catalogue is provably incomplete for the bridge endpoint precisely
when `Q(bF)\setminus Q(F)` is nonempty.  Merely observing that the bridge
changed an incidence shows the possibility, not the nonempty set
difference.

In this packet, rows 12688 and 2243 are disconnected when tested singly at
the post-bridge base.  This does not make the promoted ordered packet
invalid: the independent replay checks the order

```text
2446 -> 12688 -> 2243
```

and every resulting prefix is connected, guard-safe, and q1-full in both
openings.  Alternatively, the same three rows may be treated under the
weaker terminal-atomic contract, in which only the joint quench endpoint is
assigned topology and residence.  These two semantics are both sound but
must not be conflated.

## 6. Sufficient regenerative bridge criterion

Let `X` be a finite class of literal factors satisfying the declared hard
rows, and let `Phi:X -> Z_(>=0)` be the exact final score (here the selected
literal opened-residence policy).  Fix integers `ell,h,B >= 0` and
`epsilon >= 1`.  Define `RB(ell,h,B,epsilon)` to mean that for every
`F in X` with `Phi(F)>0` there exist

1. at most `ell` ordered bridge moves
   `F=H_0 -> H_1 -> ... -> H_m`, every `H_i in X`, with
   `Phi(H_i)<=Phi(F)+B`;
2. a quench regenerated from the literal state `H_m`, of terminal union
   support at most `h`, whose materialized endpoint `G` lies in `X`; and
3. the strict endpoint inequality

   \[
                         \Phi(G)\le\Phi(F)-\epsilon.     \tag{6.1}
   \]

The quench may be either an ordered strict-prefix packet, in which every
quench prefix lies in `X`, or a declared terminal-atomic batch, in which no
partial quench state is assigned a factor claim.

### Proposition 6.1 (regenerative descent)

If `RB(ell,h,B,epsilon)` holds, repeated certified packets reach `Phi=0`
after at most

\[
                         \left\lceil
                         \frac{\Phi(F_{start})}{\epsilon}
                         \right\rceil                 \tag{6.2}
\]

commits.  Every claimed intermediate factor remains in `X`.

#### Proof

Every committed endpoint belongs to `X`, so the hypothesis applies again
whenever its score is positive.  The nonnegative integer score decreases by
at least `epsilon` at every commit, proving (6.2).  Bridge prefixes are in
`X` by item 1; ordered quench prefixes are in `X` by their declared contract,
while terminal-atomic partial batches make no intermediate claim. \(\square\)

The current four-primitive packet proves one instance of the conclusion at
the strict17 factor, with endpoint decrease seven.  It does **not** prove
`RB` uniformly, does not prove that four primitives are minimal, and does
not imply residence zero.

## 7. Scope

This audit proves the exact palette permutation, repeated-root turnover,
quadratic pair interaction, and the logical form of a sufficient uniform
regeneration hypothesis.  It does not establish deeper ranks 11--17, source
antecedents, lower or terminal compiler, exterior opening windows,
regeneration, a universal word, or `nu(17)=24313`.
