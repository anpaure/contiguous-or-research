# Monotone pivot insertion and one-letter repair of a nested damage ray

Date: 2026-08-01  
Status: exact general word lemma and exact application to the rotating-hole
linear-damage family.  This proves that the `h-1` local casualties from that
family are repaired by one extra letter.  It does not construct the global
Pascal child or prove `nu(k)<=B(k)+1`.

## 0. Outcome

One extra word position has a stronger role than appending one missing mask.
It can create an entire nested prefix/suffix chain without destroying any old
interval union.

Let

\[
                         A=(A_1,\ldots,A_N)
\]

be a nonzero set word, choose an interior cut `p`, and let

\[
                 \varnothing\ne X\subseteq A_p\cup A_{p+1}.       \tag{0.1}
\]

Insert `X` at the cut:

\[
             A^X=(A_1,\ldots,A_p,X,A_{p+1},\ldots,A_N).            \tag{0.2}
\]

Then every interval union of `A` remains an interval union of `A^X`.
The new intervals incident with the pivot include the two nested rays

\[
 \left(\bigcup_{t=i}^{p}A_t\right)\cup X,
 \qquad
 X\cup\left(\bigcup_{t=p+1}^{j}A_t\right),                        \tag{0.3}
\]

and their two-sided grid.

Applied to the actual rotating-hole complete-damage counterfamily, insert
the singleton `{epsilon}` immediately before the screened block.  Every old
target survives, while the `h-1` damaged targets become the new right-prefix
ray.  Every old middle owner also survives; exactly the owner witnesses
crossing the cut grow from length `h+1` to `h+2`.  Thus the linear local
damage is paid by a **one-unit deadline staircase**, not by `h-1` appended
masks.

## 1. General insertion theorem

### Theorem 1.1 (OR-monotone pivot insertion)

Under (0.1)--(0.2),

\[
       \{\operatorname{OR}_A(I):I\text{ an interval}\}
       \subseteq
       \{\operatorname{OR}_{A^X}(J):J\text{ an interval}\}.       \tag{1.1}
\]

More precisely, an old interval wholly on one side of the cut is copied
unchanged (with the right indices shifted by one).  An old interval `[i,j]`
with `i<=p<j` is represented by the corresponding interval `[i,j+1]` in
`A^X`, and its union is unchanged.

#### Proof

Only a crossing interval contains the new position.  Its old union contains
both `A_p` and `A_(p+1)`, hence contains their union and therefore contains
`X`.  Adding `X` changes nothing.  The two one-sided cases are literal
copies.  \(\square\)

### Corollary 1.2 (exact ray bank)

For every `i<=p` and `j>=p+1`, the new word contains the interval unions

\[
 L_i=\left(\bigcup_{t=i}^{p}A_t\right)\cup X,
 \quad
 R_j=X\cup\left(\bigcup_{t=p+1}^{j}A_t\right),
 \quad
 G_{i,j}=\left(\bigcup_{t=i}^{p}A_t\right)\cup X\cup
             \left(\bigcup_{t=p+1}^{j}A_t\right).                 \tag{1.2}
\]

Thus one pivot gives two nested rays and one Ferrers grid.  If `X subseteq
A_p`, the left ray is old and only the right ray can be genuinely new; the
dual statement holds when `X subseteq A_(p+1)`.

### Corollary 1.3 (deadline staircase)

Let `mathcal T` be any family of old targets with chosen witness intervals.
After pivot insertion, every noncrossing witness has its old length and every
crossing witness has length increased by exactly one.  In particular, a
rank-`r` owner family remains complete, although it need no longer occupy one
flat derivative row.

This is a purely physical statement and does not require Johnson adjacency,
residence, a cap, or a compiler normal form.

## 2. Exact repair of the rotating-hole damage family

Use the notation of
`MATH_THEOREM_H1_ROTATING_HOLE_COMPLETE_DAMAGE_LINEAR_NOGO_20260801.md`.
The final screened source is `A^+_0,...,A^+_(2h+2)`, and

\[
             \epsilon\in A^+_{h-1},\qquad
             \epsilon\notin A^+_h,\ldots,A^+_{2h-1}.              \tag{2.1}
\]

Insert

\[
                             X=\{\epsilon\}                       \tag{2.2}
\]

between positions `h-1` and `h`.  Condition (0.1) holds.

The formerly missing targets are

\[
 S_j=K_0\cup\{\epsilon,q_h,q_{h+1},\ldots,q_{h+j}\},
 \qquad 1\le j<h.                                                   \tag{2.3}
\]

In the inserted word, the interval beginning at the pivot and ending at the
shifted copy of old position `h+j` has union exactly `S_j`.  Hence all `h-1`
casualties are repaired simultaneously.

The singleton task `tau=K_0+q_h` remains at the shifted old position `h`, and
the retained screen row `B` remains on the shifted copy of `[h+1,2h-1]`.
By Theorem 1.1 every other old plus-state interval target survives.

Finally, every original length-`h+1` rotating-hole owner window survives.
Those not spanning the cut retain length `h+1`; those spanning the cut are
represented by the same old letters together with the pivot and have length
`h+2`.  Since the pivot is already contained in the old crossing union, the
owner set is unchanged.

### Theorem 2.1 (tight local B+1 compensation)

The `h-1` forced complete-damage casualties of the actual-rail counterfamily
are repaired by one nonempty inserted letter, with no loss of any old
interval-OR target and no loss of any middle owner.  The price is one physical
position and a one-unit deadline staircase.

The theorem is tight only for this local family.  It does not show that every
mixed-coatom damage set is one pivot ray, that a global length-`B(k)` terminal
word with this unique defect exists, or that the inserted chronology satisfies
all recursive sidecar requirements.

## 3. Relevance to the additive conjecture

At length `B(k)+1`, one new position supplies one cell in every short row.
Theorem 1.1 identifies the geometric object behind those cells: two nested
rays through one pivot.  This exactly matches the scale `d-1` in the
rotating-hole damage example and explains why its `Omega(d)` local matching
loss is not evidence against `B+1`.

A sufficient next theorem would show that the complete terminal damage of one
prepared mixed-coatom move is contained in the union of the two pivot rays
(1.2), with compatible pivot labels and a cap-feasible maximal word.  That is
strictly stronger than scalar slack and strictly weaker than requiring zero
damage at length `B(k)`.

