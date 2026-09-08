# The protected 29-owner `k=17` object: exact source/deck integration and the terminal common-cap gate

**Date:** 2026-08-01  
**Lane:** AD / literal source integration  
**Status:** exact local source/deck theorem and exact audit of the frozen
rank-10-complete factor.  The six terminal lower pins are compatible with
the maximal caps.  The frozen factor is nevertheless not a global compiler
instance: its canonical packet source fails three left exterior caps, its
seven components are not joined, and thousands of internal short runs
remain.  No compiler SAT or UNSAT claim is made.

## 0. Exact outcome

The new protected host closes the owner, lower-`q1`, and upper-`q1` rows:

```text
owners                         24310 / 24310
rank-8 lower colours           24310 / 24310
rank-10 upper colours          19448 / 19448
protected packet/PX/PU owners       14+6+9=29
protected ML9 incidences                     52
components                  14305,8615,1362,18,4,3,3
```

The frozen factor is

```text
scratch/k17_reset_twin_ferrers_bank_ml9_factor_20260801.tsv
SHA-256 7c022f4050d6358bc5047532113814fdb46412db0018a0254cc82e056720d8df
```

and its independent replay is

```text
scratch/verify_k17_reset_twin_ferrers_bank_ml9_factor_20260801.out
SHA-256 d49405282c791e408a20e2ff378aa66317e61c567129f50dd5f2b64ebd8ad9df.
```

The literal source audit proves four further facts.

1. The displayed packet has cyclic maximal antecedent
   
   ```text
   2275,4323,8419,32995,32967,32911,32799,
   287,543,1055,16415,16443,16499,16611.
   ```
   Appending the first three letters gives all fourteen packet owners once.
   Its complete lost cyclic OR deck consists of the twelve twin-Ferrers
   targets, and the displayed `PX` and `PU` paths witness all twelve.

2. The six forced lower cells at the terminal triangle have values
   
   ```text
   2275,4323,8419,6371,12515,14563
   ```
   and addresses
   
   ```text
   [24310,24310], [24311,24311], [24312,24312],
   [24310,24311], [24311,24312], [24310,24312].
   ```
   They pass the exact maximal-cap and packet-owner reconstruction test.

3. In the actual 14,305-owner component, rotate and orient the component so
   that the displayed packet is terminal.  The protected blocks then occupy
   the exact owner slots
   
   ```text
   PU       12488..12496  (reverse orientation),
   PX       24108..24113  (forward orientation),
   packet   24296..24309  (forward orientation).
   ```
   All lie in the flat suffix after the deadline jump at `7401`.  Thus the
   old numerical address-capacity concern is gone.  The three paths need not
   be artificially concatenated: the residual factor already places them in
   one component with long intervening segments.

4. That same residual segment is not a legal canonical source collar.  At
   the first three packet-source positions, the chosen packet letters miss
   the actual maximal caps by masks `66,66,2`.  With the packet opening fixed
   and the other six components optimally opened, `5763` internal short runs
   remain, including `3058` length-two runs.  The optimistic union of the
   seven **cyclic** component decks still misses `1502,295,9` targets at
   ranks `11,12,13`.

Consequently the correct present compiler verdict is

```text
NOT_INSTANTIATED
```

not `SAT`, `UNSAT`, or a numerical Hall deficiency.

## 1. The cut convention and the one-step correction

Let `T_0,...,T_13` be the cyclic packet owners and put

\[
 A_i=\bigcap_{q=0}^{3}T_{i-q},                 \tag{1.1}
\]

with indices modulo fourteen.  Residence gives

\[
 T_i=A_i\cup A_{i+1}\cup A_{i+2}\cup A_{i+3}. \tag{1.2}
\]

Starting a linear source at `A_s` and appending its first three letters
produces the owner order

\[
 T_s,T_{s+1},\ldots,T_{s-1}.                   \tag{1.3}
\]

Therefore it opens owner edge

\[
                     e=s-1\pmod {14}.          \tag{1.4}
\]

This exposes a harmless but important bug in the old all-cut table.
`solve_cut(c)` deleted owner edge `c`, whereas `audit_restitution(c)` began
at source `A_c` and hence audited owner edge `c-1`.  Since all fourteen
owner-edge residual flows were feasible, the old global q1 conclusion is
unchanged.  A cut-specific source/bank/compiler composition must use (1.4).

The exact minimum-loss **source** cuts are

\[
                 s\in\{3,4,5,10,11,12\}.       \tag{1.5}
\]

Each has leave histogram

\[
 10^1,11^2,12^3,13^1,14^2,15^3.           \tag{1.6}
\]

The displayed named packet is the semantic image of raw source start
`s=11`, owner edge `e=10`.  A second packet automorphism represents the
same named object as raw source start `s=4`, owner edge `e=3`.  This is why
the fixed bank belongs to the structural `{4,11}` class; it is not a bank
for six unrelated fixed labelled cuts.

## 2. Exact packet source, all-width leave, and the six pins

Write the named packet owners as

\[
 Z=(47331,45287,41199,33023,33247,33695,34591,
 18207,17983,17535,16639,18683,22771,30947).    \tag{2.1}
\]

Its cyclic maximal erosion (1.1) is

\[
\begin{split}
 A=(2275,4323,8419,32995,32967,32911,32799,287,543,1055,\qquad\\
 16415,16443,16499,16611).                      \tag{2.2}
\end{split}
\]

Every `A_i` has rank six, and direct bitwise replay gives

\[
             Z_i=\bigcup_{q=0}^{3}A_{i+q}.      \tag{2.3}
\]

Use the owner-exact linear source

\[
 \widetilde A=(A_0,\ldots,A_{13},A_0,A_1,A_2). \tag{2.4}
\]

Enumerating every cyclic interval of `A` and every ordinary interval of
`widetilde A` gives the exact leave

\[
\begin{split}
 \mathcal F_X={}&\{63739,63731,63715,63735,63719,63727\},\\
 \mathcal F_U={}&\{65279,64767,63743,65023,63999,64511\}. \tag{2.5}
\end{split}
\]

No width is truncated in this comparison.  The literal owner-interval deck
of

```text
PX = 63630,63686,63714,63713,61681,57593
PU = 64259,63811,63587,61543,57455,49279,49405,50397,50845
```

contains every member of (2.5).  Thus the packet plus banks closes the
complete **internal packet** OR deck, not merely ranks ten through twelve.
This statement is conditional only on retaining each bank as a consecutive
owner interval inside a chain-aligned source chronology.

The last three source positions in (2.4) are `A_0,A_1,A_2`.  Their six
nonempty interval values are

\[
 A_0,A_1,A_2,A_0\cup A_1,A_1\cup A_2,A_0\cup A_1\cup A_2,
                                                               \tag{2.6}
\]

which are exactly the six masks in item 2 of Section 0.  All are nonzero
and distinct.  They are forced positional pins in any terminal realization
of this packet source.

## 3. The fixed bank is a one-opening object

Close the displayed packet path by its last-to-first edge.  Its lower and
upper colours are

\[
              14563,qquad63715.                \tag{3.1}
\]

The fixed `PX/PU` upper palette meets the closed packet upper palette in
exactly the singleton `{63715}`.  Therefore opening (3.1) produces the
claimed 26 distinct upper colours.  Opening any other packet edge retains
`63715` in both the packet and `PX`, giving only 25 distinct protected
upper colours.

Hence:

> **Fixed-bank cut lemma.**  The literal masks displayed above are valid
> only for their canonical packet opening.  A six-cut audit may transport
> them by a proved coordinate conjugacy, but may not reuse them unchanged
> at the other five openings.

Under coordinate conjugacy the `{4,11}` pair is covered.  A second bank
template is still required for the other structural cut orbit
`{3,5,10,12}` before a literal six-cut host comparison exists.

## 4. Exact particle placement in the frozen factor

The factor has seven cycles.  All 29 protected owners belong to the unique
14,305-owner cycle.  Orient that cycle so the displayed packet is read
forward, cut immediately after the packet, and rotate the resulting path so
the packet is terminal.  Put the other six component paths before it.  The
largest path then starts at global owner address

\[
                 24310-14305=10005.              \tag{4.1}
\]

Direct occurrence matching gives the three ranges stated in Section 0.
In particular each start is above `7401`, so the one-jump schedule assigns
the flat support

\[
                       I_i=[i,i+3]                \tag{4.2}
\]

to every protected owner.

This placement corrects the earlier provisional picture
`PX|PU|packet` in 29 consecutive slots.  No ordering or orientation of the
three naked paths has both joins Johnson-adjacent.  The minimum total number
of intermediate owners required by two Johnson geodesic joins is four.
The frozen residual factor supplies much longer connector segments, so this
naked-path obstruction is not an obstruction to the factor itself.

## 5. Maximal envelope and the exact left-collar cut

Let `b=24296` be the first packet owner address.  In the flat suffix, the
maximal cap at source position `p` is

\[
 E_p=\bigcap_{i:\ i\le p\le i+3}T_i.             \tag{5.1}
\]

For the seventeen packet source positions `b,...,b+16`, the exact audit is:

```text
local j        0      1      2      3..13 exact     14      15      16
chosen A_j   2275   4323   8419                    2275    4323    8419
max cap     47265  45217  41185                   18659   22755   30947
missing        66     66      2                        0       0       0
```

All internal positions `3..13` have cap exactly `A_j`.  The tail copies are
legal strict subsets of their caps.  Only the first three canonical packet
letters fail.

This has an exact three-owner formulation.  Let `R_{-3},R_{-2},R_{-1}` be
the three owners immediately before `Z_0`.  Then the canonical source
(2.4) is cap-admissible at its left boundary if and only if

\[
\begin{aligned}
 R_{-3}&\supseteq A_0,\\
 R_{-2}&\supseteq A_0\cup A_1,\\
 R_{-1}&\supseteq A_0\cup A_1\cup A_2.           \tag{5.2}
\end{aligned}
\]

Indeed source position `b+j`, for `j=0,1,2`, is contained in precisely
`3-j` predecessor supports and the first `j+1` packet supports.  The latter
already contain `A_j`; intersecting the predecessor supports gives (5.2).

The actual predecessor owners are

\[
                 47785,quad47793,quad47345.      \tag{5.3}
\]

Their deficits against the nested requirements in (5.2) are

\[
                         66,quad66,quad2,         \tag{5.4}
\]

respectively.  Thus this factor does **not** embed the canonical packet
source/deck certificate without a predecessor rethread.

There is a useful positive distinction.  The maximal caps (5.1) themselves
reconstruct all fourteen packet owners exactly.  Intersecting only the last
three caps with the singleton pins `A_0,A_1,A_2` still reconstructs all
fourteen owners, and the six terminal cells evaluate exactly to (2.6).
Therefore:

> **Terminal six-pin theorem.**  The six forced lower pins are jointly
> compatible with the current packet owner rows and terminal caps.  What
> fails is the stronger reuse of the complete canonical cyclic source at
> the packet's left boundary.

This is why the audit reports both `terminal_six_pin_caps_pass=true` and
`terminal_source_cap_failures=3`.

## 6. Residence and higher-shadow obstruction of the frozen factor

The seven cyclic components contain

\[
                 3073\text{ length-two runs},qquad
                 2710\text{ length-three runs}.  \tag{6.1}
\]

A cut before position `q` can make a cyclic run beginning at `i` and of
length `ell` boundary-clipped only when

\[
                   q\in\{i,i+1,\ldots,i+\ell\}.   \tag{6.2}
\]

Thus a per-component gain array gives the exact best opening calculation.
With the large component forced to the packet-terminal opening and each
other component independently optimized, at least

\[
        5763\text{ short runs remain, including }3058
        \text{ length-two runs}.                  \tag{6.3}
\]

These remaining runs are wholly internal to their opened component paths;
later inter-component joins cannot lengthen them.

For the stipulated one-jump schedule

\[
 G=(W,W,W),\qquad H=(0,0,7401),                  \tag{6.4}
\]

owner supports have length three before the jump and length four after it.
The residence-corridor criterion says that an internal run must have length
at least the active support length.  Hence an internal length-two run is
illegal on **both** sides of the jump.  Equation (6.3) therefore proves:

> **Frozen-factor source no-go.**  No ordering obtained merely by opening
> the seven frozen cycles, orienting them, and joining their endpoints can
> realize the one-jump depth-three source.  An internal factor rethread is
> mandatory.

This no-go is scoped to the frozen internal orders and schedule (6.4).  It
does not exclude a different factor or a more general staircase with
additional span-two territory.

The cyclic component interval decks give the optimistic pre-opening upper
holes

\[
             1502,quad295,quad9                 \tag{6.5}
\]

at ranks 11, 12, 13, with no holes from rank 14 onward.  Cross-component
intervals created by a future joining may fill some of (6.5), while cuts
may lose other witnesses.  Therefore (6.5) is an exact diagnostic, not an
immutable lower bound.  The future chronology must be audited from its
literal ordered owner word.

## 7. The six best cuts: exact current status

In the historical raw-coordinate convention, the terminal pins are:

| source `s` | owner edge `s-1` | singleton pins | pair/triple pins | status |
|---:|---:|---|---|---|
| 3 | 2 | 287,543,1055 | 799,1567,1823 | second bank template absent |
| 4 | 3 | 543,1055,2079 | 1567,3103,3615 | conjugate of fixed bank; global source not reached |
| 5 | 4 | 1055,2079,4127 | 3103,6175,7199 | second bank template absent |
| 10 | 9 | 4344,8440,16632 | 12536,24824,28920 | second bank template absent |
| 11 | 10 | 8440,16632,33016 | 24824,49400,57592 | semantic fixed bank; global source not reached |
| 12 | 11 | 16632,33016,504 | 49400,33272,49656 | second bank template absent |

The `s=11` row maps to the named six pins in (2.6).  All six rows have six
distinct nonzero masks and the same twelve-target leave histogram.  That
does **not** create six compiler instances.  A compiler instance needs a
cut-compatible protected bank, a joined row-exact chronology, and its full
cell atlas.  Only the `{4,11}` bank orbit is presently supplied, and its
frozen factor fails Section 6.

## 8. Exact terminal common-cap instance

This section freezes the model to run after the chronology gate is repaired.
Let a proposed linear chronology be `T_0,...,T_(W-1)`, with increasing
owner supports `I_i=[s_i,d_i]` in a length-`W+3` particle schedule.  Define

\[
 E_p=\bigcap_{i:p\in I_i}T_i.                    \tag{8.1}
\]

Fail immediately unless all `E_p` are nonempty and

\[
                    \bigcup_{p\in I_i}E_p=T_i    \tag{8.2}
\]

for every owner.  Install the six injective fixed pins `M_0` from (2.6) at
the six terminal cells.  Put

\[
 \bar E_p=E_p\cap\bigcap_{S:p\in M_0(S)}S.        \tag{8.3}
\]

Again fail unless all caps are nonempty and every owner row remains exact.
The terminal six-pin theorem proves these local checks for the packet rows;
the ambient rows still require the completed chronology.

Let `C(I)` be the exact lower-cell atlas: the physical intervals containing
no complete owner support.  A residual target `S` may use a cell `J` only if

\[
 \bar E_p\cap S\ne\varnothing\quad(p\in J),
 \qquad S\subseteq\bigcup_{p\in J}\bar E_p.       \tag{8.4}
\]

Choose an injective extension `M` of `M_0` assigning every strict-lower
target to one such cell, and define the maximal common word

\[
 Q_p=\bar E_p\cap\bigcap_{S:p\in M(S)}S.          \tag{8.5}
\]

The exact terminal master accepts if and only if

\[
\begin{aligned}
 Q_p&\ne\varnothing &&\text{for all }p,\\
 \bigcup_{p\in I_i}Q_p&=T_i &&\text{for all owners }i,\\
 \bigcup_{p\in M(S)}Q_p&=S &&\text{for every lower target }S.
                                                               \tag{8.6}
\end{aligned}
\]

Equations (8.1)--(8.6) are the precise fixed-cut terminal common-cap
instance.  Ordinary target-to-cell Hall is only its marginal relaxation.
Bad-set CEGAR may separate violations of (8.6), but it must not be invoked
before (8.1)--(8.3) and literal upper coverage pass.

For the frozen factor, (8.1)--(8.2) fail globally by Section 6, so the model
has no legitimate ambient input.  Reporting a common-cap deficiency would
therefore be unsound.

## 9. Sharp remaining joint gate

The next exact construction must do all of the following in one object:

1. preserve the 29 protected owners, their 26 lower and 26 upper q1
   colours, and the twelve bank witness intervals;
2. rethread the seven-component factor so the one-jump residence corridor
   is exact, in particular eliminating or boundary-routing every internal
   length-two run;
3. supply a predecessor collar satisfying (5.2), or replace the canonical
   packet source by a separately proved all-width source certificate;
4. join the seven components while retaining exact rank-8 and rank-10
   palettes;
5. cover every rank-11, rank-12, and rank-13 target after the actual cuts
   and joins; and
6. only then solve (8.1)--(8.6).

This is a joint rethread/source/compiler problem.  The central owner and
immediate-palette host is closed; neither a second residual q1 flow nor a
premature compiler Hall solve addresses the live obstruction.

## 10. Reproducible audit

The exact audit was compiled and run with `g++ -std=c++20 -O3 -DNDEBUG` on
the H100 CPU only.  Its frozen local artifacts are:

```text
scratch/audit_ad_k17_twin29_source_deck_terminal_gate_20260801.cpp
scratch/run.audit.json
scratch/run.bestcuts.tsv
scratch/run.terminal_caps.tsv
```

The audit reconstructs the old raw cycle instead of trusting the old cut
labels; independently rebuilds the named packet source; enumerates every
cyclic and linear packet interval; binds all 48,620 factor incidences;
locates all three protected paths; computes the maximal caps at the actual
particle positions; checks the six pins; and recomputes the short-run and
deep-hole ledgers.

Its verdict is

```text
PASS_AD_K17_TWIN29_SOURCE_DECK_TERMINAL_GATE
cap_failures=3 addresses=24108,12488,24296
remaining_short=5763 remaining_len2=3058
deep=1502,295,9 compiler=NOT_INSTANTIATED
```

The exact hashes are recorded after the independent audit below; any later
factor rethread requires a fresh source/cap replay.
