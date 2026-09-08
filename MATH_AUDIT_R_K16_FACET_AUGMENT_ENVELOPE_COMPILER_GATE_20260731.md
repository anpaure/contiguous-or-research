# The K16 facet-augment carrier: immutable-ghost audit and exact rethread/compiler gate

**Date:** 2026-07-31  
**Status:** exact solver-free theorem; current order `COMPILER-DEAD`, alternating-path family `LIVE-RETHREAD`

## 1. Authoritative object and verdict

This note concerns the current rank-eight target order

```text
scratch/k16_facet_augmented_middle_targets_20260731.word
SHA-256 9712d02ebfb97c4a773caa90c0933eea78f30834162c462f4dd50692186b6550
```

obtained from the authenticated length-12,873 one-hole source by two
four-step facet augmenting paths (eight deleted and eight inserted edges).
The independent facet audit proves:

1. the order contains each of the `12,870` rank-eight masks exactly once;
2. it is one connected path;
3. its complete rank-nine edge-colour multiset is identical to the source;
4. its only missing upper carrier-interval target is
   `0x6f79`, of rank eleven; and
5. it has `1,430` internal coordinate runs of length below four.

The exact classification, after the complete three-hole schedule DP, is

```text
CURRENT TARGET ORDER: COMPILER-DEAD
ALTERNATING-PATH / FACET-AUGMENT FAMILY: LIVE-RETHREAD
```

for the following precise reason.  Middle ownership is perfect, so the
immutable-ghost count is zero.  But neither canonical fixed-envelope lift is
a physical antecedent:

* the flat depth-three maximal envelope fails `3,489` middle rows;
* the much stronger lift obtained by transplanting the source word's exact
  delivery slots fails only **six** middle rows, each by one bit.

The six-row result alone suggested a deadline/start rethread.  The complete
three-start-hole/three-deadline-hole DP closes that possibility for this
**fixed target order**: among every envelope-realizable schedule its maximum
representative lower-prefix area is only `16,876`, versus `26,332` required.
Even crediting all three omitted starts with three lower prefixes each gives
only `16,885`.  Thus no compiler can realize this order.  What remains live
is choosing a different pair of colour-preserving augmenting paths, or an
additional carrier rethread, and then applying the exact upper/compiler gate
below to the new order.

The obsolete two-hole `{0xae6d,0xef79}` snapshot is not used anywhere in
this note.

## 2. Immutable ghosts vanish exactly

Let (T=(T_0,\ldots,T_{W-1})), where (W={16\choose8}=12870), denote the
current target order.

### Proposition 2.1 (squarefree carrier has no intrinsic ghost)

The carrier itself has no repeated target, so its immutable-ghost count is
zero.  In a physical schedule using exactly one delivery occurrence for each
listed row, both repeat counts (F) and (G) are zero.

### Proof

The target file is a permutation of the complete rank-eight layer.  Hence no
listed target occurs twice, either at the same deadline or at different
deadlines.
\(\square\)

This is stronger than testing the locations of two particular immutable
witnesses: there is no repeated middle target in the carrier.  A physical
word can still create an additional **flat** occurrence of one target at its
existing deadline; that is not an immutable ghost.  Conversely, the global
K16 equality theorem independently forces (G=0) for every universal
length-12,873 word.  None of these statements implies that a compatible
schedule exists.

## 3. Exact generalized-envelope theorem

The following is the required source-independent finite gate.

Let the physical positions be (0,\ldots,L-1).  A scheduled middle row is a
triple

\[
 (I_i,T_i),\qquad I_i=[s_i,e_i],\qquad |T_i|=8.
\]

Define its maximal envelope by

\[
 P_p=\bigcap_{i:p\in I_i}T_i,                         \tag{3.1}
\]

where an uncovered position has (P_p=[16]).

### Theorem 3.1 (base envelope, necessary and sufficient)

There is a nonzero physical word (A_0,\ldots,A_{L-1}) satisfying

\[
 \bigcup_{p\in I_i}A_p=T_i\quad\hbox{for every }i       \tag{3.2}
\]

if and only if

\[
 P_p\ne\varnothing\quad(0\le p<L),                    \tag{ENV0}
\]

and

\[
 \bigcup_{p\in I_i}P_p=T_i\quad\hbox{for every }i.     \tag{ENV1}
\]

### Proof

Every solution has (A_p\subseteq P_p), because (A_p) is contained in
every scheduled target whose interval covers (p).  Thus `ENV0--ENV1` are
necessary.  Conversely (A_p=P_p) satisfies every row equation and is
nonzero.  \(\square\)

There is therefore no integrality or Boolean-SAT ambiguity at the bare
envelope stage.

## 4. Exact simultaneous upper-pin and compiler theorem

For any family of additional desired interval cells

\[
 \mathcal Q=\{(J_a,U_a):J_a=[u_a,v_a]\},               \tag{4.1}
\]

define the jointly capped envelope

\[
 P_p^{\mathcal Q}
 =P_p\cap\bigcap_{a:p\in J_a}U_a.                      \tag{4.2}
\]

### Theorem 4.1 (maximal capped-envelope criterion)

There is a nonzero word satisfying every scheduled middle row and every pin

\[
 \bigcup_{p\in J_a}A_p=U_a                              \tag{4.3}
\]

if and only if

\[
 P_p^{\mathcal Q}\ne\varnothing\quad(0\le p<L),        \tag{CAP0}
\]

\[
 \bigcup_{p\in I_i}P_p^{\mathcal Q}=T_i\quad\forall i, \tag{CAP1}
\]

and

\[
 \bigcup_{p\in J_a}P_p^{\mathcal Q}=U_a\quad\forall a.\tag{CAP2}
\]

### Proof

Every solution lies inside (4.2), giving necessity.  Under `CAP0--CAP2`, the
coordinatewise maximal choice (A_p=P_p^{\mathcal Q}) is itself a solution.
\(\square\)

This criterion handles overlapping upper and lower witnesses, repeated use
of one physical position, and all common-bit correlations.  Testing pins one
at a time is weaker and is not an exact compiler test.

## 5. The exact K16 equality gate for this carrier

Set (L=W+3=12873).  By the global equality and ghost theorem, a universal
length-(L) realization whose distinct middle-target groups occur in this
order has a representative interval for each target satisfying:

1. (W) distinct starts (s_0<\cdots<s_{W-1}) among the (L) physical
   starts;
2. strictly increasing deadlines (e_i), since all (T_i) are distinct;
3. (0\le e_i-s_i\le3); and
4. `ENV0--ENV1` for (I_i=[s_i,e_i]).

The remaining three starts need not all be stalls or jumps: a physical word
may use part of its waste budget on flat repeats.  They need not be classified
in advance, because the interval equations below already construct a
universal word and the global equality theorem then controls its inventory.

Call these conditions `SCH+ENV`.

If, in addition,

\[
 s_{i+1}\le e_i+1\quad(0\le i<W-1),                   \tag{CHAIN}
\]

then the union of any consecutive block of scheduled intervals is the
physical interval ([s_a,e_b]).  Hence every upper carrier-interval target
is automatically a literal physical interval target.  The audited carrier
has exactly one exception:

\[
 U_*=0x6f79.                                           \tag{UP*}
\]

Thus its exact upper completion consists of choosing one physical interval
(J_*) and adding the single pin ((J_*,U_*)) to Theorem 4.1.

Finally let

\[
 \mathcal L=\{S\subseteq[16]:1\le |S|\le7\},
 \qquad |\mathcal L|=26332.
\]

For each (S\in\mathcal L), choose a physical interval (J_S) of length at
most three.  This restriction is exact at equality: before the first
rank-eight deadline, every proper-prefix witness has at most three letters.
Apply Theorem 4.1 to

\[
 \mathcal Q={(J_*,U_*)\}\cup
              \{(J_S,S):S\in\mathcal L\}.              \tag{5.1}
\]

### Corollary 5.1 (exact finite rethread/compiler gate)

Within the ordered-deck, chained-witness equality architecture, a universal
length-12,873 word exists if and only if there are representative intervals
(I_i), one interval (J_*), and lower intervals (J_S) satisfying
`SCH+ENV`, `CHAIN`, and `CAP0--CAP2` for (5.1).

This is a host-choice/interval problem, not a cell-bit SAT problem: once the
intervals are selected, the unique maximal admissible solution is (4.2).
The corollary is an exact gate, not a claim that it is feasible.

For the present target SHA, Section 6.3 proves that the gate fails already at
the lower interval-count projection, before choosing the `0x6f79` pin or any
lower host assignment.

## 6. Two canonical fixed-envelope audits

### 6.1 Flat depth three

Taking (I_i=[i,i+3]) gives:

```text
empty maximal envelopes                 0
failed middle rows                   3489
missing row-bit incidences           4284
envelope ranks      3^1 4^4 5^12858 6^7 7^1 8^2
```

Equivalently, the `1,430` short internal coordinate runs violate the exact
residence criterion.  The fact that every envelope cell is nonzero does not
repair the failed row unions.  Moreover, flat upper/lower separation says
that `0x6f79` has no physical provider, because it has no consecutive
carrier-interval provider.  Flat `COMP_3` is therefore exactly impossible.

### 6.2 Transplanted source delivery slots

The authenticated source word has exact first-middle delivery slots with

```text
unused starts              6432, 12869, 12871
depth histogram            0^1 1^2 2^6436 3^6431
total proper-prefix mass   32167
adjacent interval-chain breaks  0
```

Transplanting the new target order into these slots gives no empty maximal
envelopes and envelope ranks

```text
5^6425 6^6442 7^3 8^3.
```

It fails exactly six row equations:

| row | interval | target | maximal replay | missing bit |
|---:|:---:|:---:|:---:|:---:|
| 3287 | 3287..3290 | `4ae9` | `4ae1` | `0008` |
| 3288 | 3288..3291 | `6a69` | `6a61` | `0008` |
| 3289 | 3289..3292 | `6a71` | `6a61` | `0010` |
| 5189 | 5189..5192 | `263d` | `262d` | `0010` |
| 5190 | 5190..5193 | `263e` | `262e` | `0010` |
| 6077 | 6077..6080 | `2e69` | `2c69` | `0200` |

For a row (i) and required bit (x\in T_i), define its physical host set

\[
 H(i,x)=I_i\setminus
 \bigcup_{j:x\notin T_j}I_j.                           \tag{6.1}
\]

The six table entries are exactly the six empty host obligations
(H(i,x)=\varnothing).  Hence any successful rethread must change the
start/deadline overlap pattern enough to make all six host sets nonempty.
No choice of compiler letters inside the fixed envelopes can do so.

The old physical word had five witnesses for `0x6f79`, all concentrated in
the collar

```text
[6385,6391], [6385,6392], [6385,6393],
[6386,6393], [6387,6393].
```

The new carrier order destroys that carrier interval.  Before the complete
DP no-go, a rethread of this order would therefore have had to score both
the six empty middle-bit hosts and a new `0x6f79` capped-envelope pin.  For a
different augmenting-path order, the analogous envelope-host and complete
upper-spectrum scores must again be imposed jointly.

### 6.3 Complete three-hole schedule DP: fixed-order death

The preceding transplanted schedule is not the final obstruction.  Let

```text
P = the three omitted physical starts,
Q = the three omitted physical deadlines.
```

Pair the (i)-th retained start with the (i)-th retained deadline and
assign the (i)-th target in the fixed order.  This is the general monotone
representative schedule at excess three: distinct target groups have
strictly increasing deadlines, and every such schedule is specified by
((P,Q)).

For fixed ((P,Q)), Theorem 3.1 tests realizability by the maximal envelope.
The complete streaming DP retains the active row-OR queue and, for identical
states, the largest area

\[
 A(P,Q)=\sum_i(e_i-s_i)=\sum_{p\in P}p-\sum_{q\in Q}q. \tag{6.2}
\]

It has at most sixteen live states.  Its exact optimum is

```text
maximum representative lower area   16876
maximizing start holes               3290, 12871, 12872
maximizing deadline holes            0, 6078, 6079
required lower targets               26332
```

The area counts every proper-prefix interval at the (W) representative
middle starts.  Each of the other three physical starts has at most three
lower prefixes by the global depth-three equality bound, whether it becomes
a stall, jump, or flat occurrence.  Therefore every universal word with this
fixed distinct-target order would satisfy

\[
 26332\le 16876+3\cdot3=16885,                       \tag{6.3}
\]

which is false.

### Theorem 6.1 (fixed-order compiler no-go)

No universal K16 word of length 12,873 can have the distinct middle-target
deadline groups in the order of target SHA `9712d02e...`, regardless of the
three start holes, three deadline holes, maximal-envelope choice, upper pin,
or lower compiler assignment.

This theorem does not exclude another one of the colour-preserving
augmenting-path orders.  In particular, the alternating-path mechanism stays
live while this particular target sequence is retired.

## 7. Scope and remaining obligation

Proved:

* immutable ghosts are exactly zero;
* both named fixed envelopes fail, with exact counts;
* the transplanted schedule is only six one-bit obligations from `ENV1`;
* nevertheless, the complete schedule DP proves the fixed order
  compiler-dead by the robust `16885<26332` lower-capacity inequality;
* the sole carrier-level upper obligation of this now-retired order is
  `0x6f79`; and
* Theorem 4.1 and Corollary 5.1 are necessary and sufficient in their stated
  ordered-deck/chained schedule scope.

Not proved:

* an alternative augmenting-path/rethread order passing the area gate;
* upper completeness or an exact residual upper pin for that new order;
* the `26,332`-target lower compiler for that new order; or
* a literal universal K16 word of length 12,873.

The current order is dead.  The non-collar architecture remains genuinely
live only at the level of its colour-preserving alternating-path family,
which must emit a different target order and then pass the coupled
upper/lower maximal-envelope solve.

## 8. Independent lightweight audit

```text
scratch/audit_r_k16_facet_augment_envelope_gate_20260731.py
scratch/r_k16_facet_augment_envelope_gate_20260731.audit.json
scratch/audit_three_hole_middle_schedule_dp_20260731.py
scratch/k16_facet_augmented_three_hole_schedule_dp_20260731.audit.json
```

The checker pins the target SHA, reconstructs both maximal envelopes, replays
every scheduled row, recomputes the complete upper carrier spectrum, and
enumerates the old literal `0x6f79` witnesses.  It performs no search.

```text
combined checker SHA-256
  e255f0cf65c3950bc29a669b888ecb57e1a65c8fd2c7effaf7b42cdf22669a5f
audit JSON SHA-256
  433205bbd13ab307928492be4d4bdcbe2df4300208b43a562bc87ba082d18ce1
audit payload SHA-256
  4339d92afd3ef0c8054b37d9dc991f22ea774b20b42354a1bcedf8fd486f2d3c
three-hole DP checker SHA-256
  0f98adae54686b773d449a3def482a099fab1b939aa623244b220f6b64d6bbc2
three-hole DP JSON SHA-256
  3c14c4a6a8250fccef56d82fc1ca446bbec4e7317f348bea140c59334c8116b5
three-hole DP payload SHA-256
  9a3102873bc4f06bc0b84f5a60469fd79147d6ad88a351b53b7c1319e52ec6fc
```
