# The K16 def4 reversal: exact physical-pin criterion and an all-P/Q capacity no-go

**Date:** 2026-07-31  
**Status:** proved for the authenticated monotone depth-three P/Q architecture; independently audited provenance and fixed-schedule pin criterion

## 1. Result

Consider

```text
scratch/k16_fourfilter_def4_reversal_targets_20260731.word
SHA-256 0a3a34c4f4c5e7e0fd474909a1010f2ca6d6df895bb869ac79cbacfbb757a08b.
```

It is byte-identical to the result of reversing zero-based target rows
`[2130,10447]` of

```text
scratch/k16_fourfilter_insert_aug_d2_1_targets_20260731.word
SHA-256 e483dae43cce3ca3e678958daab49f4237628f9b129df4f030fd83d83ffaa452.
```

The two old boundary colours `29cf,a98f` are replaced by `a9ce,a9cf`.
The resulting order is a permutation of all

\[
W={16\choose8}=12870
\]

rank-eight masks.  Its complete target-order upper audit has exactly the
three holes

\[
\mathtt{a9fe},\qquad \mathtt{b8ce},\qquad \mathtt{b8cf}.       \tag{1.1}
\]

The main conclusion is stronger than the previously frozen deficiency-four
audit of one maximum-area schedule.

### Theorem 1.1 (all-P/Q no-go from the `b8ce` pin)

There is no monotone K16 P/Q schedule for this target order having

1. three omitted physical starts and three omitted deadlines;
2. one representative interval \(I_i=[p_i,q_i]\) for every listed middle
   target, with \(0\le q_i-p_i\le3\);
3. a nonempty physical word realizing every middle target;
4. a literal physical interval realizing `b8ce`; and
5. literal occurrences of all \(26332\) nonempty lower masks.

This remains impossible if the `a9fe` and `b8cf` requirements are dropped.
Consequently no choice of lower-provider hosts, no Hall rematching, and no
simultaneous common cap can complete this target order inside the stated
P/Q architecture.

The proof has two parts.  First, every legal `b8ce` pin has length at most
seven.  Second, an exact pin-augmented event DAG over **all** P/Q schedules
shows that the maximum selected lower-prefix area is only \(25745\).  Even
granting the three omitted starts the optimistic credit \(3\) each gives

\[
25745+9=25754<26332.                                    \tag{1.2}
\]

The gap is exactly \(578\).

## 2. Exact one-pin criterion

Fix any middle schedule \((I_i,T_i)\), where \(|T_i|=8\), and define its
maximal envelope

\[
E_j=\bigcap_{i:j\in I_i}T_i.                            \tag{2.1}
\]

Assume the uncapped envelope is nonzero and realizes every middle row:

\[
E_j\ne\varnothing,qquad
\bigcup_{j\in I_i}E_j=T_i.                              \tag{2.2}
\]

For a row-bit pair \((i,x)\), put

\[
H_{i,x}=\{j\in I_i:x\in E_j\}.                         \tag{2.3}
\]

### Theorem 2.1 (individual physical upper pin, if and only if)

Let \(J\) be a nonempty physical interval and let \(U\) be any mask.  A
nonempty word \(A\), with \(A_j\subseteq E_j\), can preserve every middle
row and satisfy

\[
\bigcup_{j\in J}A_j=U                                  \tag{2.4}
\]

if and only if

\[
E_j\cap U\ne\varnothing\quad(j\in J),                 \tag{P0}
\]

\[
U\subseteq\bigcup_{j\in J}E_j,                         \tag{P1}
\]

and

\[
H_{i,x}\not\subseteq J
\quad\text{for every }i\text{ and }x\in T_i\setminus U.\tag{P2}
\]

#### Proof

Necessity is direct.  Equation (2.4) forces every \(A_j\), \(j\in J\), to
lie in \(U\), giving `P0--P1`.  If \(x\in T_i\setminus U\) and
\(H_{i,x}\subseteq J\), all maximal hosts of \(x\) in row \(i\) are capped
away, so row \(i\) cannot retain \(x\).

Conversely set

\[
A_j=\begin{cases}
E_j\cap U,&j\in J,\\
E_j,&j\notin J.
\end{cases}                                             \tag{2.5}
\]

Condition `P0` makes every letter nonempty, and `P1` makes the OR on \(J\)
equal to \(U\).  A bit of \(T_i\) lying in \(U\) survives wherever it did
before.  For a bit outside \(U\), `P2` leaves at least one host outside
\(J\).  Hence every middle OR remains \(T_i\).  \(\square\)

For an interval \(J=[a,b]\), `P2` is equivalent to saying that \(J\)
contains no forbidden segment

\[
[\min H_{i,x},\max H_{i,x}],\qquad x\in T_i\setminus U. \tag{2.6}
\]

This is the exact short-pin oracle.  It is not enough that the capped
envelopes merely have union \(U\).

## 3. A general compatible-run bound

Let \(h\) be the number of omitted starts, let every scheduled span have
length at most \(d\), and define

\[
\rho_T(U)=\max\{s:\ T_a,T_{a+1},\ldots,T_{a+s-1}\subseteq U\}. \tag{3.1}
\]

### Lemma 3.1 (every legal pin is short)

Every physical interval \(J\) realizing \(U\) while preserving the scheduled
middle rows satisfies

\[
|J|\le d+h+\rho_T(U).                                  \tag{3.2}
\]

#### Proof

Write \(J=[a,b]\).  Every selected start

\[
p_i\in[a,b-d]
\]

has \(q_i\le p_i+d\le b\), so \(I_i\subseteq J\).  At most \(h\) physical
starts in this interval are omitted.  Thus at least

\[
|J|-d-h                                                   \tag{3.3}
\]

consecutive scheduled rows have their whole representative intervals inside
\(J\).  Every letter of a literal \(U\)-pin lies in \(U\).  Therefore each
of those middle targets is a subset of \(U\), and (3.3) is at most
\(\rho_T(U)\).  Rearranging proves (3.2).  The inequality is automatic when
the left side of (3.3) is nonpositive.  \(\square\)

For `b8ce`, the authenticated order has exactly its nine rank-eight facets,
at zero-based rows

```text
2891  3797  4306  4999  6099  6173  12519  12834  12869
```

with values

```text
b0ce  b8ca  b8c6  a8ce  b84e  38ce  b88e  b8cc  98ce.
```

No two are consecutive.  Hence

\[
\rho_T(\mathtt{b8ce})=1.                               \tag{3.4}
\]

With \(d=h=3\), Lemma 3.1 gives

\[
|J|\le7.                                                \tag{3.5}
\]

Thus a search through length seven is complete for **every** possible
physical `b8ce` pin in this target order.

## 4. Exact pin-augmented event DAG

The recurrence scans physical positions \(j=0,\ldots,12872\).  Its state is

\[
(x_j,y_j,Q_j,\phi_j,R_j,\ell_j),                         \tag{4.1}
\]

where

- \(x_j,y_j\in\{0,1,2,3\}\) count used start and deadline holes;
- \(Q_j\) is the ordered queue of accumulated ORs for active middle rows;
- \(\phi_j\in\{\text{before},\text{inside},\text{after}\}\) is the pin
  phase;
- \(R_j\subseteq\mathtt{b8ce}\) is the accumulated pin OR while inside; and
- \(\ell_j\le7\) is the current pin length.

At each position the transition chooses independently whether the position
is a start hole and a deadline hole.  These choices determine the consecutive
active target block and hence its maximal envelope (2.1).  Outside the pin,
that envelope is OR-ed into every active accumulator.  Inside the pin, its
intersection with `b8ce` is used; a zero intersection is rejected.  A row
ending at the position is accepted only when its accumulator equals its
target exactly.  The pin can end only when its accumulated OR is `b8ce`.

Once the pin OR first reaches `b8ce`, ending it immediately is without loss:
uncapping later cells can only restore middle bits.  Consequently histories
with identical state (4.1) may be merged by retaining only the largest area

\[
A=\sum_i(q_i-p_i).                                      \tag{4.2}
\]

Future feasibility and future area depend only on (4.1), so this dominance
is exact.

### Theorem 4.1 (audited optimum)

The complete pin-augmented DAG has at most \(79\) states in any layer.  Its
maximum selected area is

\[
A_{\max}=25745.                                         \tag{4.3}
\]

One maximizing history is

\[
X=\{6099,12871,12872\},\qquad
Y=\{0,1,6096\},                                         \tag{4.4}
\]

with the exact `b8ce` pin

\[
J=[6099,6102].                                          \tag{4.5}
\]

Direct reconstruction of the maximal capped word gives zero empty cells,
zero middle failures, and pin OR exactly `b8ce`.  The exact omitted-start
credit of this representative is only \(6\), so it has \(25751\) candidate
lower cells.  The proof uses the more generous uniform credit \(9\) in
(1.2).

#### Completeness audit

The recurrence considers both start-hole choices, both deadline-hole choices,
and all three pin-phase choices at every physical position.  The active queue
is the actual capped row-OR queue, not the uncapped schedule queue.  Thus
every history accepted by the DAG reconstructs a physical capped word, and
Theorem 2.1 maps every possible physical pin to an accepted maximal capped
history.  Lemma 3.1 supplies the exact length-seven bound.  No target-order
interval assumption or fixed \(X,Y\) is used.

## 5. Lower-provider consequence

At a selected start \(p_i\), at most \(q_i-p_i\) proper prefixes can be
lower.  Each of the three omitted starts contributes at most three further
lower prefixes.  Hence every history in the complete DAG has at most

\[
A_{\max}+3\cdot3=25754                              \tag{5.1}
\]

physical lower cells.  The number of required nonempty lower masks is

\[
\Lambda=\sum_{s=1}^{7}{16\choose s}=26332.              \tag{5.2}
\]

Distinct masks require distinct literal intervals, so (5.1)--(5.2) prove
Theorem 1.1 before constructing an individual-pin graph.  In particular,
there cannot be a joint selection of lower provider hosts: the right side is
already \(578\) cells too small.

This strictly supersedes, for this target order, the fixed maximum-area
schedule audit

```text
X={10457,12871,12872}, Y={0,1,6101}, area=30098,
lower matching 26328/26332, deficiency 4,
zero-host targets {29cc,8000,898d}.
```

That schedule also has zero legal physical pins, and zero literal maximal-
envelope pins, for each target in (1.1).  The fixed-schedule pin obstruction
agrees independently with Theorem 2.1; it is no longer the decisive no-go.

## 6. Useful near-pins and the exact surviving route

The fixed maximum-area schedule contains two nested near-pin sockets for
`b8ce,b8cf`:

```text
outer b8cf [4558,4563], inner b8ce [4559,4563]: forced bit 0200;
outer b8cf [12834,12839], inner b8ce [12835,12839]: forced bit 0010.
```

After the indicated caps, both upper ORs are exact and no cell is zero.  In
the first socket, bit `0200` is lost from middle rows `4558..4561`; in the
second, bit `0010` is lost from rows `12835..12836`.  Each offending middle
interval lies wholly inside the outer pin, so Theorem 2.1 rejects both under
the displayed fixed schedule.

These are useful only after a target-order rethread or endpoint retiming.
Theorem 1.1 proves that no alternative P/Q retiming of the **same** target
order can combine even one exact `b8ce` pin with enough scalar lower cells.
The surviving route is therefore a new rank-eight chronology (or a genuinely
non-P/Q equality architecture), not another schedule or lower Hall solve for
SHA `0a3a34c4...`.

## 7. Frozen artifacts and scope

```text
scratch/audit_ad_k16_def4_b8ce_shortpin_capacity_20260731.py
scratch/ad_k16_def4_b8ce_all_schedule_shortpin_capacity_20260731.audit.json
```

The audit JSON has payload SHA-256

```text
b4d5a2936cb39eb1495f19dec8dc8ae8a09d5a4b42e52ffce67d26190af53417.
```

Independent fixed-schedule artifacts are

```text
scratch/ad_k16_fourfilter_def4_maxpq_upperpin_a9fe_20260731.audit.json
scratch/ad_k16_fourfilter_def4_maxpq_upperpin_b8ce_20260731.audit.json
scratch/ad_k16_fourfilter_def4_maxpq_upperpin_b8cf_20260731.audit.json.
```

The theorem is exact for all monotone depth-three P/Q schedules on the
authenticated target order.  It does not claim a global K16 lower bound, does
not exclude another target order, and does not exclude a representation that
falls outside the P/Q equality architecture.
