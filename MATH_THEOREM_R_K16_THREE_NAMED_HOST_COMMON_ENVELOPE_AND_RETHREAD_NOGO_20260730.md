# K16 three named hosts: exact common-envelope gate and scoped rethread no-go

Date: 2026-07-30  
Lane: R  
Status: **proved exact physical-host theorem; complete no-go for the local twelve-label block atlas, tail-fixed standard 2/3-opt, and the fixed-three-plus-one 4-opt fibre; no unrestricted K16 no-go**

## 1. Result and scope

The three protected lower masks are

\[
 A=\mathtt{0x4c71},\qquad
 B=\mathtt{0x4879},\qquad
 C=\mathtt{0x4c39}.                                      \tag{1.1}
\]

Two authenticated upper-complete rank-eight chronologies were already known:

* `u0`, obtained by the standard pattern-4 rethread with cuts
  `(3278,6388,12826)`, has a unique physical host for each of `B,C` and no
  host for `A`;
* `u1`, obtained by the same pattern with cuts `(5725,6388,12826)`, has a
  unique physical host for `A` and no host for either `B,C`.

This note proves the exact simultaneous-host condition, audits the advertised
twelve parent-pair labels, and exhausts the next standard one-extra-cut fibre.
No zero-host-free chronology occurs in any of those families.  The smallest
obstruction is already a singleton Hall row: `{A}->empty` for `u0`, and
`{B}->empty` or `{C}->empty` for `u1` and every chronology-preserving member
of the twelve-label local atlas.

This does not exclude movable original cuts, terminal-flat cuts, five cuts,
nonstandard duplication, a different target chronology, or an arbitrary
length-12,873 K16 word.

## 2. Exact one-host criterion

Let

\[
 T_0,T_1,\ldots,T_{N-1}\in\binom{[16]}8                  \tag{2.1}
\]

be a fixed rank-eight chronology.  Suppose its forced first-delivery depths
are `d_i in {0,1,2,3}` and put

\[
 W_i=[i,i+d_i].                                           \tag{2.2}
\]

Define the maximal physical envelope at position `p` by

\[
 E_p=\bigcap_{i:p\in W_i}T_i.                             \tag{2.3}
\]

Assume throughout that

\[
 E_p\ne\varnothing\quad\hbox{for every }p,
 \qquad
 \bigcup_{p\in W_i}E_p=T_i\quad\hbox{for every }i.        \tag{2.4}
\]

Every lower interval beginning at `s` is a proper prefix

\[
 J=[s,s+\ell-1],\qquad 1\le\ell\le d_s,                  \tag{2.5}
\]

because the complete interval `W_s` already has rank eight and OR is
monotone.

For a middle incidence `(i,b)`, let

\[
 C_{i,b}=\{p\in W_i:b\in E_p\}.                           \tag{2.6}
\]

For a proper-prefix interval `J`, set

\[
 U_J=\bigcup_{p\in J}E_p,
 \qquad
 M_J=\{b:\ C_{i,b}\subseteq J\text{ for some }i\}.       \tag{2.7}
\]

### Theorem 2.1 (exact individual physical-host criterion)

A nonempty physical assignment `x_p subseteq E_p` can preserve every middle
row and realize a lower target `S` on `J` if and only if

\[
 S\subseteq U_J,\qquad M_J\subseteq S,
 \qquad E_p\cap S\ne\varnothing\quad(p\in J).             \tag{2.8}
\]

#### Proof

Necessity is immediate.  A bit requested by `S` must occur in `U_J`.  If an
outside bit `b notin S` has its complete middle carrier `C_(i,b)` inside `J`,
erasing `b` throughout `J` destroys middle row `i`.  Finally, every physical
cell must remain nonempty.

Conversely assign

\[
 x_p=E_p\cap S\quad(p\in J),\qquad x_p=E_p\quad(p\notin J). \tag{2.9}
\]

The third condition makes every edited cell nonempty, and the first gives
`OR_(p in J)x_p=S`.  A middle bit in `S` survives wherever its envelope
contains it.  A middle bit outside `S` could disappear only if its complete
carrier lay inside `J`, which the second condition excludes.  Hence every
middle row remains exact.  QED.

## 3. Exact simultaneous-host criterion

Individual host existence is not sufficient for several lower targets.  Let
one proper-prefix host `J_R` be chosen for every `R` in a finite protected
family `P`, and define the common core

\[
 K_p=E_p\cap\bigcap_{R\in\mathcal P:p\in J_R}R.            \tag{3.1}
\]

An empty intersection over protected rows is interpreted as `[16]`.

### Theorem 3.1 (common-envelope theorem)

There is one nonzero physical assignment which preserves every middle row
and simultaneously realizes every selected protected host if and only if

\[
 \begin{aligned}
 &K_p\ne\varnothing &&(0\le p<N),                         \tag{CE0}\\
 &\bigcup_{p\in W_i}K_p=T_i &&(0\le i<N),                 \tag{CEM}\\
 &\bigcup_{p\in J_R}K_p=R &&(R\in\mathcal P).             \tag{CEH}
 \end{aligned}
\]

When these conditions hold, the canonical physical assignment is `x_p=K_p`.

#### Proof

If `x` realizes the declared rows, then `x_p` is contained in every envelope
and every protected target whose host uses `p`; hence `x_p subseteq K_p`.
Nonemptiness and every requested bit therefore force (CE0)--(CEH).  Conversely
the assignment `x_p=K_p` is nonzero by (CE0), preserves all middle rows by
(CEM), and realizes the protected intervals by (CEH).  QED.

For a bit `b`, put

\[
 D_b=\bigcup_{R\in\mathcal P:b\notin R}J_R.               \tag{3.2}
\]

Then (CE0) says that each `E_p` contains some bit `b` with `p notin D_b`.
Conditions (CEM) and (CEH) say respectively that no middle carrier and no
requested host carrier is covered by `D_b`.  This is the exact physical
Hall/noncover form; it has no independent-rankwise relaxation.

### Corollary 3.2 (the special three-mask triangle)

Write

\[
 K=\mathtt{0x4831},\quad u=\mathtt{0x0040},\quad
 v=\mathtt{0x0008},\quad w=\mathtt{0x0400}.               \tag{3.3}
\]

Then

\[
 A=K\vee u\vee w,\quad B=K\vee u\vee v,\quad
 C=K\vee v\vee w,
 \qquad A\vee B\vee C=\mathtt{0x4c79}.                   \tag{3.4}
\]

Thus the only overlap cores are

\[
 A\cap B=\mathtt{0x4871},\quad
 A\cap C=\mathtt{0x4c31},\quad
 B\cap C=\mathtt{0x4839},\quad
 A\cap B\cap C=K.                                       \tag{3.5}
\]

After the three individual tests (2.8) pass, simultaneous compatibility is
equivalent to the following remaining checks:

1. every overlap cell meets the appropriate pair or triple core in (3.5);
2. the two special ears of each target survive outside the host of the target
   omitting that ear;
3. no middle carrier of a bit outside `0x4c79` is covered by
   `J_A union J_B union J_C`.

In particular, three individually admissible hosts whose position sets are
pairwise separated by distance at least four are jointly compatible.  A
middle carrier has diameter at most three, so it cannot meet two such hosts;
any combined carrier loss would already contradict one of the individual
mandatory-bit tests.

Separate individual host existence can fail to imply the common system.  For
example, at a cell in `J_A intersect J_B`, envelope `0x0408` meets `A` and
`B` separately but has empty intersection with `A intersect B`.

## 4. Frozen `u0` and `u1` host domains

Independent reconstruction gives the complete named-host domains:

| chronology | `0x4879` | `0x4c39` | `0x4c71` |
|---|---:|---:|---:|
| `u0` | `(9717,2)` | `(12164,2)` | empty |
| `u1` | empty | empty | `(3279,3)` |

Here `(s,l)` denotes `[s,s+l-1]`.  The complete proper-prefix cell counts are
29,065 for `u0` and 31,512 for `u1`.  Both chronologies are upper-complete and
their maximal envelopes reconstruct every middle row.  Neither reaches even
the individual-existence premise of Theorem 3.1.

## 5. Complete tail-fixed standard 2/3-opt census

The authenticated state-2 source has only the two rank-nine upper holes

\[
 \mathtt{0x4e79},\qquad\mathtt{0xc679}.                   \tag{5.1}
\]

Any new witness for a missing rank-nine target must cross a new join whose
rank-eight endpoints have that union.  This pins every relevant standard
2-opt and all but at most one cut of a genuine standard 3-opt.

The complete tail-fixed census has:

| gate | 2-opt | genuine 3-opt |
|---|---:|---:|
| candidate keys | 1 | 299 |
| exact terminal-flat profile | 1 | 278 |
| scalar capacity at least 26,332 | 1 | 267 |
| exact nonzero maximal-envelope carrier | 0 | 4 |
| upper-complete | 0 | 2 |

The two upper-complete survivors are exactly `u0` and `u1`, with named-host
vectors `(B,C,A)` equal to `110` and `001`.  Therefore no standard tail-fixed
2/3-opt chronology hosts all three masks.

## 6. The twelve-label parent-block atlas

The phrase “twelve parent-pair rethreads” needs a correction.  The exact
local object has only six physically distinct blocks: one length-three
`0x4c71` block from each K15 parent `X=0,...,5`.  Each embeds, in the displayed
orientation, into the unique `u1` host at start 3279:

| `X` | parent start | orientation | installed block |
|---:|---:|---|---|
| 0 | 6025 | forward | `0821,0050,4421` |
| 1 | 4559 | forward | `0c21,0410,4061` |
| 2 | 172 | reverse | `0c61,0030,4041` |
| 3 | 3281 | forward | `0c20,0070,4441` |
| 4 | 2302 | reverse | `0c61,0010,4421` |
| 5 | 598 | reverse | `0861,0030,4400` |

Pairing each `X` with either valid marked-parent label `Y in {1,5}` produces
twelve provenance labels, but `Y` is inert in this local operation.  These
are not twelve distinct rethreads and do not install either complete parent
body or a collar.

All six blocks preserve every middle row and every upper mask of `u1`, lose
no previously covered literal mask, and leave respectively

\[
 3985,3985,3986,3985,3986,3984                         \tag{6.1}
\]

lower masks absent from their maximal-envelope source.  The last block is
best by this raw count.  Nevertheless `0x4879` and `0x4c39` remain absent in
all six.  Since their proper-prefix neighbor sets are empty for the frozen
`u1` chronology, no physical assignment consistent with that chronology can
repair either target.  Hence each of the twelve labelled rows has the exact
singleton obstruction

\[
 \{\mathtt{0x4879}\}\longmapsto\varnothing                \tag{6.2}
\]

(and independently the analogous `0x4c39` obstruction).

This is a no-go for the local length-three block atlas, not for a
chronology-changing parent-pair construction.

## 7. Complete fixed-three-plus-one 4-opt fibre

Starting from `u1`, freeze its three cuts

\[
 5725,\quad6388,\quad12826,                              \tag{7.1}
\]

add one extra nonterminal cut in `[0,12868]`, and reconnect the resulting
three internal segments in every one of

\[
 3!2^3=48                                                \tag{7.2}
\]

orders and orientations.  Excluding the three already frozen choices leaves

\[
 (12869-3)48=617568                                      \tag{7.3}
\]

representations.  The exact census partitions them as follows:

```text
upper-join necessity reject       591,701
join prefilter pass                25,867
  G0/terminal-flat reject               6
  carrier/capacity reject          12,985
  exact carrier pass               12,876
    named B,C host reject          12,875
    named B,C host pass                 1
      arbitrary upper pass              1
```

The sole named-host and upper-complete survivor is

```text
extra cut       3278
sorted cuts     3278,5725,6388,12826
segment order   2,0,1
orientation     all forward
capacity        29065
flat starts     3322,12869,12871
```

Independent reconstruction shows that this chronology is byte-for-byte
`u0`.  Its sole zero-host target is `0x4c71`.  Therefore the complete
fixed-three-plus-one fibre has zero rows preserving all three masks.

The upper-join prefilter is necessary: the source lacks the two rank-nine
masks in (5.1), all old adjacencies remain internal to a rethreaded segment,
and a new rank-nine witness must cross a new adjacent join with that exact
endpoint union.  The subsequent tests are a fail-closed chain: literal G0 and
terminal flats, maximal-envelope reconstruction, the named `B,C` hosts, and
arbitrary upper coverage.  The sole row reaching the last gate then receives
the complete lower zero-host audit.

## 8. Audited boundary and next exact enlargement

Proved:

1. Theorems 2.1 and 3.1 are necessary and sufficient integral physical-word
   criteria.
2. `u0` and `u1` have the exact complementary host domains displayed above.
3. No chronology in the complete tail-fixed standard 2/3-opt catalogue hosts
   all three masks.
4. The twelve provenance labels are exactly six local `u1` blocks times two
   inert `Y` labels, and each retains two singleton Hall obstructions.
5. No chronology in the complete fixed-three-plus-one standard 4-opt fibre
   hosts all three masks.

Not proved:

1. infeasibility after moving one of the three frozen cuts;
2. infeasibility with a terminal-flat cut, five cuts, duplication, or a
   nonstandard segment braid;
3. infeasibility of the separate twelve-pair tri-window collar family from
   handoff item 2002a;
4. a full simultaneous COMP3 assignment even for a chronology with all three
   individual host domains nonempty;
5. an unrestricted K16 equality no-go.

The smallest faithful next family is a chronology-changing move which gives
nonempty domains for all three masks, followed first by the exact three-row
common-envelope test (CE0)--(CEH), and only then by the full lower compiler.

The global bracket remains

\[
 12873\le\nu(16)\le12874.
\]

## 9. Artifacts

```text
scratch/audit_r_k16_threehost_parent_rethread_catalogue_20260730.py
scratch/r_k16_threehost_parent_rethread_catalogue_20260730.audit.json

scratch/threadD_k16_state2_threehost_standard_3opt_census_20260730.cpp
scratch/threadD_k16_state2_fixed3plus1_4opt_lower_host_census_20260730.cpp

scratch/r_k16_state2_threehost_20260730/threehost.json
scratch/r_k16_state2_threehost_20260730/fixed4.json
scratch/audit_r_k16_state2_fixed4_threehost_nogo_20260730.py
scratch/r_k16_state2_threehost_20260730/independent.audit.json

MATH_AUDIT_R_K16_THREE_NAMED_HOST_COMMON_ENVELOPE_AND_RETHREAD_NOGO_20260730.md
```

The independent audit reconstructs the sole 4-opt survivor directly from the
source chronology, verifies that it equals `u0`, recomputes its upper cover,
maximal envelopes and complete named-host domains, and checks every census
partition identity.  It does not trust the production program's saved
envelope or host flags.
