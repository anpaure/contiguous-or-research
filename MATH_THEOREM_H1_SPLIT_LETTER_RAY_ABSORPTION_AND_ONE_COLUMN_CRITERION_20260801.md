# One split letter absorbs the complete rotating-hole damage ray: the exact one-column criterion

Date: 2026-08-01  
Lane: additive-constant regeneration / one-spare exchange  
Status: exact positive theorem and replay.  It uses a one-unit deadline staircase rather than a flat `D^h` antecedent.

## 0. Outcome

The linear `h-1` complete-damage family in
`MATH_THEOREM_H1_ROTATING_HOLE_COMPLETE_DAMAGE_LINEAR_NOGO_20260801.md`
is **exactly absorbed** by one added source letter.

The reference cell at the task position is

\[
                         X=\tau\cup\{\epsilon\}.            \tag{0.1}
\]

Replace this one letter by the consecutive block

\[
                         \{\epsilon\},\quad\tau.            \tag{0.2}
\]

Every old interval union survives by contracting the two-letter block back
to `X`; the new task `tau` occurs as a singleton; and the displaced old cell
plus all `h-1` lost ray targets are the `h` intervals beginning at the new
`{epsilon}` letter.

Thus the counterexample proves that **fixed-length cap replacement** can
have `Omega(h)` complete damage.  It does not create an additive-length
obstruction.  At length `B+1`, one split letter pays the whole ray exactly.

All old middle owners and all old upper witnesses are retained verbatim as
set values.  Owner intervals which cross the split use length `h+2`; the
others retain length `h+1`.  This is a one-unit deadline staircase, so the
construction lies outside a rigid flat-derivative ansatz but inside the
original OR-word problem.

## 1. Universal split-letter lemma

### Theorem 1.1 (block-contraction preservation)

Let

\[
                         A=(A_0,\ldots,A_{N-1})              \tag{1.1}
\]

be any nonzero set word.  Fix `r` and nonempty sets `Z,T` such that

\[
                              A_r=Z\cup T.                  \tag{1.2}
\]

Form the length-`N+1` word

\[
 \widetilde A=(A_0,\ldots,A_{r-1},Z,T,A_{r+1},\ldots,A_{N-1}).\tag{1.3}
\]

Then every interval union of `A` occurs in `A tilde`, and `T` occurs as the
singleton cell at the second new position.  More precisely, the map

\[
 [a,b]\longmapsto
 \begin{cases}
 [a,b],&b<r,\\
 [a+1,b+1],&a>r,\\
 [a,b+1],&a\le r\le b
 \end{cases}                                               \tag{1.4}
\]

is injective on physical cells and preserves their literal OR values.

#### Proof

Intervals avoiding `r` are merely shifted.  An interval containing `r`
has `A_r=Z union T` in the old word and contains both consecutive new
letters in its image, so its union is unchanged.  The cell containing only
`T` is new and realizes the task.  \(\square\)

No rank, adjacency, or probability hypothesis is used.  The theorem is the
literal reason an added letter can absorb many matched casualties: damage
counts reference **cells**, while the added block preserves all of them at
once.

### Corollary 1.3 (bounded dominating-letter reset)

Let `T_1,...,T_H` be nonempty tasks and suppose one reference source letter
`X` contains all of them.  Replace `X` by the consecutive block

\[
                         X,T_1,T_2,\ldots,T_H.              \tag{1.5}
\]

The block union is still `X`.  Therefore every old interval value survives,
every `T_i` is a singleton cell, and the word length rises by exactly `H`.
Named carrier and upper witnesses transport by contracting the whole block;
their deadlines rise by at most `H` exactly when they cross it.

More generally different tasks may use different dominating letters and be
split independently.  Thus a bounded-task regenerative theorem needs no
complete-damage estimate at all if it can plant the tasks below `O(1)` old
source letters in one reference cap state.

This is stronger than saying `T_i` lies in a carrier envelope.  The
dominating `X` must be an actual nonzero source letter in a reference word
which already realizes the old target bank.  Producing such letters is the
new positive host condition.

### Corollary 1.2 (carrier and witness preservation)

Suppose a named carrier or upper-witness bank in `A` is represented by
intervals `I_alpha`.  Replace every `I_alpha` by its image under (1.4).
Then the carrier values, their order, every coordinate residence record on
that value sequence, and every named upper target are unchanged.

If the old carrier used windows of length `h+1`, the new witnesses use
length `h+2` exactly for old windows containing `r`, and length `h+1`
otherwise.  Hence the only structural price is one deadline jump of size
one.

This corollary is invalid only for an architecture which insists that every
carrier owner remain in one flat derivative row.  The original interval-OR
problem has no such restriction.

## 2. Exact absorption of the rotating-hole family

Retain the notation of the complete-damage theorem.  The reference source
has

\[
 A_h^-=\tau\cup\{\epsilon\},\qquad
 \tau=K_0\cup\{q_h\},                                    \tag{2.1}
\]

whereas the fixed-length terminal plus state replaces this cell by `tau`.
The damaged targets are

\[
 S_j=K_0\cup\{\epsilon,q_h,q_{h+1},\ldots,q_{h+j}\},
             \qquad1\le j<h.                              \tag{2.2}
\]

Apply Theorem 1.1 with `Z={epsilon}` and `T=tau`.  In the split word,

\[
 \begin{aligned}
 [\epsilon,\tau]&=A_h^-=S_0,\\
 [\epsilon,\tau,A_{h+1}^+,\ldots,A_{h+j}^+]&=S_j
                       &&(1\le j<h).                       \tag{2.3}
 \end{aligned}
\]

Here `S_0` is the old singleton-cell value displaced when `tau` took its
position.  Therefore the one added letter repairs

\[
                    1+(h-1)=h                              \tag{2.4}
\]

old matching edges while keeping the new task.

The retained screen row

\[
 J=[h+1,2h-1],\qquad
 B=K_0\cup\{q_{h+1},\ldots,q_{2h-1}\}                     \tag{2.5}
\]

simply shifts one position to the right and remains exact.  Every other old
lower or upper interval is preserved by (1.4), whether or not it was named
in the damage proof.

### Theorem 2.1 (exact `B+1` seam finish for the ray family)

The length-`N+1` split word simultaneously has:

1. every interval-OR value of the reference word;
2. the new task `tau`;
3. the complete rotating-hole owner cycle in its old order;
4. every old upper witness and the old screen row; and
5. literal occurrences of all `h-1` formerly damaged targets.

Thus its terminal complete-damage charge relative to the reference matching
is zero after the physical cells are transported by (1.4).

#### Proof

Theorem 1.1 gives items 1--2 and transports every reference matching edge.
Corollary 1.2 gives items 3--4.  Equation (2.3) gives item 5.  \(\square\)

This says that the `h-1` damage and the `d-1` residual-address count agree
for a structural reason: the damaged family is one strict nested right ray.
There is no content or orientation obstruction in this example.

## 3. General nested-ray criterion

Let a prospective extra letter `Z` be inserted immediately before a task
letter `T` at a right-facing socket.  Let

\[
 P_j=\bigcup_{t=r}^{e_j}A_t,qquad
            r\le e_0<e_1<\cdots<e_s                  \tag{3.1}
\]

be selected prefix unions on the right.

### Theorem 3.1 (direct one-column ray criterion)

A target family `R_0,...,R_s` can occupy distinct right-fan addresses of
one added column, while every old interval is preserved by block
contraction, if and only if there are nonempty `Z,T`, an old letter `X`, and
endpoints as in (3.1) such that

\[
                  X=Z\cup T,qquad R_j=Z\cup P_j
                  \quad(0\le j\le s).                       \tag{3.2}
\]

For the consecutive full ray of depth `d`, take `e_j=r+j`; it fits the
`d-1` residual addresses exactly when its values are

\[
 Z\cup T,quad Z\cup T\cup A_{r+1},\quad\ldots,quad
 Z\cup T\cup A_{r+1}\cup\cdots\cup A_{r+d-2}.             \tag{3.3}
\]

The left-facing criterion is the reversal using suffix unions.

#### Proof

After inserting `Z` before `T`, every new interval beginning at `Z` and
ending at `e_j` has exactly the value `Z union P_j`.  Distinct endpoints
give distinct physical addresses.  Preservation by contracting the new
two-letter block to one old letter is equivalent to its union being the old
letter `X`, namely `X=Z union T`.  These conditions are also plainly
necessary for this direct right-fan realization.  Reversal proves the other
orientation.  \(\square\)

The criterion is **address-specific**.  A nested family of the correct
cardinality can still fail if no common `Z` makes its successive differences
appear in one physical prefix order, or if `Z union T` is not an available
old letter.  Such a family would need the nonlocal gammoid/exterior-ear
router.  Cardinality `d-1` alone is insufficient.

For bounded damage rather than exact direct service, (3.2) need hold for all
but `O(1)` targets; the exceptional identities become the next terminal
sidecar.

## 4. Audit

Run

```text
python3 scratch/audit_h1_split_letter_ray_absorption_20260801.py
```

For `2<=h<=30`, the replay:

* reconstructs the old and split source words;
* verifies that **every** old interval value survives;
* transports every rank-`m` rail owner with the exact `h+1/h+2` deadline
  staircase;
* verifies the task, screen row, displaced old cell, and all `h-1` ray
  targets; and
* checks literal length increase one.

Canonical audit payload SHA-256:

```text
82418a5180c88e704b78392f43a8aa96fcfb2d830cb99579a1ee1a024e3388b8
```
