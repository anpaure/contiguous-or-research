# K16 waste three: the three-hole core staircase and the exact physical-overlap gate

**Date:** 2026-07-30  
**Status:** unconditional normal form for a hypothetical length-12,873 word;
no existence or no-go conclusion

## 1. Verdict

Assume, only for this note, that a universal K16 word of length

\[
  L=W+3=12873,
  \qquad W=\binom{16}{8}=12870
\]

exists.  The ghost-exclusion theorem in
`MATH_AUDIT_K16_MIDDLE_CHAIN_WASTE_PHASE_DUAL_20260730.md` implies that its
forward and reverse first-middle inventories are ghost-free.

That already forces an exact, architecture-independent physical normal form.
There are three omitted left endpoints `X`, three omitted right deadlines
`Y`, and an order-preserving family of `W` endpoint-essential intervals

\[
  I_i=[p_i,q_i],\qquad 0\le q_i-p_i\le3,
\]

whose OR labels are every rank-eight set exactly once.  Here `p_i` is the
`i`th position outside `X`, and `q_i` is the `i`th position outside `Y`.
The two defect triples obey a prefix-Dyck condition and the exact area law

\[
  \sum_i(q_i-p_i)=\sum_{x\in X}x-\sum_{y\in Y}y.
\]

Lower universality forces this area to be at least `26323`.  In particular,
among the canonical middle witnesses there must be at least

```text
11,437 intervals of length at least 2,
 6,572 intervals of length at least 3,
   583 intervals of length exactly 4 or more (here exactly 4).
```

The middle labels must also pass an exact overlap-envelope test: at every
physical position, their common intersection is nonempty, and the union of
these common intersections over each `I_i` must recover its label.

This is the genuinely physical successor to the scalar waste ledger.  It
does not force a fourth waste unit.  A completion still has to place letters
inside these common envelopes so that all lower masks occur in lengths at
most three and every upper mask occurs somewhere.  Conversely, satisfying
that coupled envelope/compiler problem would be a constructive escape to
length 12,873.

No doubled parent, marked run, two-rail decomposition, flat carrier, or
Johnson adjacency is assumed.

## 2. Canonical core intervals

For a nonzero word `A=(A_0,...,A_(L-1))`, write

\[
 U(p,q)=\bigcup_{j=p}^q A_j.
\]

For each left endpoint `p`, stop at the first `q` for which `|U(p,q)|>=8`.
If the rank is exactly eight, `p` delivers `T=U(p,q)` at deadline `q`.

In a universal length-12,873 word, every rank-eight target is delivered.  By
the global ghost-exclusion theorem, all delivery occurrences of a fixed
target have one common deadline.  For each target `T`, choose the largest
left endpoint in that deadline group and call the resulting interval

\[
 I_T=[p_T,q_T].
\]

### Theorem 2.1 (three-hole endpoint-essential core)

The selected intervals have the following properties.

1. The `p_T` are pairwise distinct, and the `q_T` are pairwise distinct.
2. If `p_T<p_R`, then `q_T<q_R`.
3. Every interval has length at most four: `0<=q_T-p_T<=3`.
4. Both endpoints are essential:

   \[
   |U(p_T+1,q_T)|<8,
   \qquad |U(p_T,q_T-1)|<8,
   \]

   whenever the displayed shorter interval is nonempty.
5. The labels `U(I_T)` are the complete rank-eight layer, once each.

Consequently, if

\[
 P=\{p_T\},\quad Q=\{q_T\},\quad
 X=[0,L-1]\setminus P,\quad Y=[0,L-1]\setminus Q,
\]

then `|X|=|Y|=3`.  Writing

\[
 P=\{p_1<\cdots<p_W\},
 \qquad Q=\{q_1<\cdots<q_W\},
\]

pairs `I_i=[p_i,q_i]` with one permutation of all rank-eight labels.

**Proof.**  One left endpoint delivers at most one target.  If two distinct
targets had one right deadline, their intervals would be nested and their
equal-rank OR labels would be equal.  This proves distinctness on both
shores.

If `p_T<p_R` but `q_R<q_T`, then `I_R` is contained in `I_T`; again the two
rank-eight labels would be equal.  Equality of right endpoints was already
excluded, proving strict order preservation.

The monotone-deadline depth lemma bounds every initial lower column by
`L-W=3`, proving the length claim.  Removing the right endpoint leaves a
proper prefix of a first delivery, hence rank below eight.  If removing the
left endpoint still gave `T`, the new left endpoint would first deliver `T`
at this deadline or at an earlier one.  The former contradicts maximality of
`p_T`; the latter is a ghost.  Both are impossible.  Universal coverage
supplies every target.  Finally `L-W=3` gives the two complement sizes.  QED.

Reversing the word yields the same core intervals: the left-essential
condition says that scanning backward from `q_T` first reaches rank eight at
`p_T`.

## 3. Defect path and exact area ledger

For `0<=t<L`, put

\[
 h(t)=|Y\cap[0,t]|-|X\cap[0,t]|.
\]

### Lemma 3.1 (prefix-Dyck condition)

For every `t`,

\[
 0\le h(t)\le3,
 \qquad h(L-1)=0.
\]

**Proof.**  Since `q_i>=p_i`, the number of selected right endpoints at or
before `t` cannot exceed the number of selected left endpoints there:

\[
 (t+1)-|Y\cap[0,t]|
 \le (t+1)-|X\cap[0,t]|.
\]

This is `h(t)>=0`.  Both defect sets have size three, giving the upper bound
and final equality.  QED.

Thus the six endpoint defects form a height-at-most-three Dyck/Motzkin path;
coincident left/right defects are neutral steps.

### Lemma 3.2 (core area identity)

Let `s_i=q_i-p_i`.  Then

\[
 \boxed{
   \sum_{i=1}^W s_i
    =\sum_{x\in X}x-\sum_{y\in Y}y
    =\sum_{t=0}^{L-1}h(t).
 }                                                   \tag{3.1}
\]

**Proof.**  Since `P,Q` are complements of `X,Y` in the same physical
index set,

\[
 \sum_iq_i-\sum_ip_i
 =\left(\sum_{j=0}^{L-1}j-\sum_{y\in Y}y\right)
  -\left(\sum_{j=0}^{L-1}j-\sum_{x\in X}x\right).
\]

This is the first equality.  Summing the prefix contributions of each defect
gives the second.  QED.

Now let `f_p` be the number of initial interval cells in column `p` whose OR
rank is below eight.  On a selected core endpoint, `f_(p_i)=s_i`.  Put

\[
 U_X=\sum_{x\in X} f_x.
\]

Every lower target occurs among these cells, and no column has more than
three of them.  If `R_<` is the repeated-lower occurrence excess, then

\[
 \boxed{
  \Lambda+R_<
   =\sum_pf_p
   =\left(\sum_{x\in X}x-\sum_{y\in Y}y\right)+U_X,
 }                                                   \tag{3.2}
\]

where

\[
 \Lambda=\sum_{j=1}^7\binom{16}{j}=26332,
 \qquad
 0\le U_X\le\sum_{x\in X}\min(3,L-x)\le9.
\]

In particular,

\[
 \boxed{
  \sum_{x\in X}x-\sum_{y\in Y}y\ge26323.
 }                                                   \tag{3.3}
\]

Equation (3.2), rather than a flat-row hypothesis, is the exact way in which
the lower compiler forces the three endpoint defects to stay separated for
positive density.

## 4. Rankwise width moments

For `a=1,2,3`, let

\[
 C_a=|\{i:s_i\ge a\}|.
\]

Then the core area is `C_1+C_2+C_3`.

### Theorem 4.1 (mandatory long-core counts)

Every hypothetical universal length-12,873 word satisfies

\[
 \boxed{
 C_1\ge11437,
 \qquad C_2\ge6572,
 \qquad C_3\ge583.
 }                                                   \tag{4.1}
\]

More sharply,

\[
 C_1+C_2\ge19442,
 \qquad C_1+C_2+C_3\ge26323.                         \tag{4.2}
\]

**Proof.**  The `11440=\binom{16}{7}` rank-seven targets require at least that
many columns with one or more lower cells.  A nested column contains at most
one distinct rank-seven target.  The three unselected endpoints contribute
at most three such columns, so `C_1>=11437`.

The rank-six and rank-seven layers contain `8008+11440=19448` targets.  A
column contributes at most `min(f_p,2)` distinct targets from these two ranks.
The three unselected endpoints contribute at most six, while the selected
cores contribute `C_1+C_2`.  This proves the first inequality in (4.2), and
`C_2>=19442-W=6572`.

Equation (3.3) is the second inequality in (4.2).  Since `C_1,C_2<=W`, it
gives

\[
 C_3\ge26323-2W=583.
\]

QED.

Thus a candidate cannot hide all depth-three behavior in a bounded seam:
at least 583 canonical middle intervals must have full length four.  This is
still far below the 6,432 full-length middle intervals of upper12874, so it
does not by itself create a contradiction.

## 5. Exact common-intersection overlap test

Let `T_i` be the label of `I_i`.  Define the maximal old-coordinate envelope
at each position by

\[
 K_j=\bigcap_{i:j\in I_i}T_i,
\]

using `[16]` if no selected core contains `j`.

### Theorem 5.1 (core-envelope criterion)

Every physical realization of the selected core intervals satisfies

\[
 A_j\subseteq K_j,
 \qquad K_j\ne\varnothing,
 \qquad
 \bigcup_{j\in I_i}K_j=T_i\quad\text{for every }i.   \tag{5.1}
\]

Conversely, if the last two conditions in (5.1) hold for a proposed labelled
core system, assigning `A_j=K_j` realizes every displayed middle interval
with its prescribed OR label.

**Proof.**  A letter used by several selected witnesses must lie in all of
their labels, giving `A_j\subseteq K_j`; nonzeroness gives the second
condition.  For one core `I_i`, every `K_j` in it is a subset of `T_i`, while
the actual letters satisfy

\[
 T_i=\bigcup_{j\in I_i}A_j
     \subseteq\bigcup_{j\in I_i}K_j\subseteq T_i.
\]

This proves equality.  The converse is immediate from the same equality.
QED.

The converse realizes the selected middle labels only.  It need not retain
their first-delivery status, cover the lower or upper layers, or keep an
uncovered physical position from creating a jump.  Those are separate
compiler constraints.

## 6. Immediate-lower targets force a near-rainbow Johnson path

The core order is much more structured than an arbitrary permutation of the
middle layer.

### Theorem 6.1 (all but six rank-seven targets are consecutive intersections)

For at least

\[
 \binom{16}{7}-6=11434
\]

distinct rank-seven sets `S`, there is an index `i` such that

\[
 S=T_{i-1}\cap T_i,
 \qquad |T_{i-1}\triangle T_i|=2.             \tag{6.1}
\]

Thus at least 11,434 of the 12,869 consecutive core transitions are Johnson
edges, and their rank-seven intersection labels are distinct.  At most 1,435
transitions remain unrestricted by this statement.

**Proof.**  Choose one physical witness `J_S=[a,b]` for each rank-seven
target.  A fixed left endpoint can witness at most one distinct rank-seven
target, because equal-rank labels in one increasing OR chain are equal.  The
same holds for a fixed right endpoint after reversal.  Charge a witness with
`a in X` to `a`; among the rest, charge one with `b in Y` to `b`.  At most
`|X|+|Y|=6` targets are charged.  Every other witness has

\[
 a=p_i,\qquad b=q_j
\]

for canonical core indices `i,j`.  Since `U(a,b)` has rank seven, the core
starting at `a` ends strictly after `b`, while the core ending at `b` starts
strictly before `a`; hence `j<i` and both `T_j,T_i` contain `S`.

Suppose `j<k<i`.  Endpoint order gives

\[
 p_k<a\le b<q_k,
\]

so `J_S` lies strictly inside `I_k`.  Since `T_k` has rank eight, write
`T_k=S union {x}`.  Left-end essentiality forces `x` to occur only in the
letter at `p_k`; otherwise deleting that endpoint would leave rank eight.
Right-end essentiality simultaneously forces `x` to occur only at `q_k`.
The two positions are distinct, a contradiction.  Therefore `j=i-1`.

The two distinct rank-eight labels `T_(i-1),T_i` both contain `S`, so their
intersection has rank exactly seven and equals `S`.  Distinct `S` give
distinct edge labels.  QED.

This theorem derives a near-`q1` Johnson carrier from universality and the
three-hole core; it does not assume one.  The six possible exceptions are
literal endpoint-defect charges, not an asymptotic error term.  A fourth-waste
proof would now have to couple this near-rainbow path to rank six and below,
or to upper completion.  The edge count by itself is feasible and gives no
contradiction.

## 7. The remaining physical gate

The prior independent-column relaxation supplies a nested chain cover of all
lower and middle targets with scalar waste three.  Theorem 5.1 explains
exactly why that relaxation is not yet physical: independently chosen chains
need not fit inside the common envelopes `K_j` created by one ordered middle
deck.

A length-12,873 construction would follow from one joint object consisting
of:

1. defect triples `X,Y` satisfying the prefix and area constraints;
2. a permutation `T_1,...,T_W` of all rank-eight sets satisfying the
   endpoint-essential interval equations and the common-envelope test;
3. nonempty choices `A_j\subseteq K_j` whose length-one, -two, and -three ORs
   contain all 26,332 lower masks; and
4. witnesses for every upper mask without changing the core equations.

A fourth-waste theorem must prove that no such joint object exists.  The
strict doubled-overlap bridge obstruction proves this only in one two-block
subclass.  The abstract matching countermodel proves that layer counts and
within-column containment alone cannot do it.  The literal middle-only word
proves that the overlap envelope and all middle labels alone cannot do it.

The exact unresolved coupling is therefore

\[
  \text{three-hole core overlap}
  +\text{ lower length-3 universality}
  +\text{ upper completion}.
\]

No claim here changes

\[
  12873\le\nu(16)\le12874.
\]

## 8. Exact audit and calibration

The solver-free checker reconstructs first-delivery columns, selects the
canonical cores, verifies endpoint injection/order, the defect-prefix and
area identities, every lower occurrence, both endpoint-essential tests, and
the common-intersection envelope equations.

On upper12874 it obtains

```text
X = [6433,12827,12870,12872]
Y = [0,2,3,12829]
span histogram = 0^1 1^2 2^6435 3^6432
core area = 32168
unselected lower depth = 8
lower occurrences = 32176 = 26332 + 5844.
rank-seven consecutive intersections = 11437; endpoint-charged = 3.
```

On the authenticated item-1995 length-12,873 H1 source it obtains

```text
middle targets = 12869 (one hole)
X = [6433,12826,12869,12872]
Y = [0,2,3,12828]
span histogram = 1^3 2^6434 3^6432
core area = 32167
unselected lower depth = 8
lower occurrences = 32175 = 26332 + 5843.
rank-seven consecutive intersections = 11437; endpoint-charged = 3.
```

The latter is not the hypothetical theorem case because its missing middle
target gives four rather than three endpoint holes.  It does show that all
lower masks and all overlap-envelope equations can coexist with this area;
the remaining defect is genuinely in middle ownership.

Artifacts:

```text
scratch/audit_k16_three_hole_core_overlap_gate_20260730.py
SHA-256 c5f228d21158d8a8a2db593585b19ee376876fa8c4a9d87979adbbe49f98be45

scratch/k16_three_hole_core_overlap_gate_20260730.audit.json
SHA-256 cc9646b723cfed49b9d0219551d16e0160ae9f07a6bbed39b89626795c0b2e18
payload 0aab187af8b429097234d3e14de1965545c6f9a1b6a25abaf5202e139c4b94f8
```

Re-execution reproduces the JSON byte for byte.
