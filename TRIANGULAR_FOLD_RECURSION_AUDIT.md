# Audit of `TRIANGULAR_FOLD_RECURSION.md`

## 1. Verdict

The algebraic core is correct.

* The fold fibres in (2.1) are exact.
* The complete block lift covers every target with `u>=1,x>=1`, including
  the delicate folded-height case `x-1=0` and the boundary case `u-1=0`.
* A spanning lower word lifts to every upper triangular cell except `P_0`.
* The boundary scaffold covers exactly the advertised boundary regimes.
* The length identities (3.3) and (4.5) are correct.

The required correction is logical scope, not algebra.  Section 5 turns a
particular sufficient construction into an asserted equivalence.  Embedding
the displayed scaffold `B_R` into occurrences of a lifted word is a strong
sufficient route to a near-once recursion; it is not proved necessary for:

1. an arbitrary universal triangular word;
2. an arbitrary word obtained using the fold; or even
3. an arbitrary way of covering the boundary targets with the same lifted
   occurrences.

Likewise, an `Omega(R)` obstruction for that particular superposition would
be architecture-specific and would not imply `rho(R)=Omega(R^2)` for the
unrestricted triangular problem.

With those qualifications, the note contains a useful exact quotient/section
theorem and a valid explicit recursive construction.

## 2. Fibre audit

For an upper cell `(s,y)` with `s>=1`, the map is

\[
                 \phi_R(s,y)=(s-1,\max(y-1,0)).       \tag{2.1}
\]

Fix a lower cell `(a,b)`.

* If `(a,b)=P_0`, then `s=1`; triangularity forces `y=0`, giving only
  `P_1`.
* If `(a,b)=P_a` with `a>=1`, then `s=a+1` and
  `max(y-1,0)=0`, hence `y=0` or `1`.  These are exactly
  `P_(a+1)` and `(a+1,1)`.
* If `b>=1`, then necessarily `s=a+1,y=b+1`.  Since `b<a` in the lower
  triangle, `b+1<a+1`, so this is a legal and unique upper cell.

Thus

\[
\begin{aligned}
 \phi_R^{-1}(P_0)&=\{P_1\},\\
 \phi_R^{-1}(P_a)&=\{P_{a+1},(a+1,1)\}\quad(1\le a<R),\\
 \phi_R^{-1}(a,b)&=\{(a+1,b+1)\}\quad(b\ge1),
\end{aligned}                                         \tag{2.2}
\]

and these fibres partition `T_R\{P_0}`.  The statement that precisely the
nonzero lower peaks have two-element fibres is correct.

There is also a safe reverse statement, implicit but not stated formally in
the source:

### Proposition 1 (exact target quotient)

The parameter map

\[
 (u,r,x)\longmapsto(u-1,r-1,x-1)                     \tag{2.3}
\]

is a bijection from the strict upper target family `u>=1,x>=1` to the full
target family of `T_(R-1)`.  Folding a strict-target witness gives a witness
of its image.

Conversely, the full block lift is a section of this quotient.

If an upper word is universal, delete its `P_0` occurrences and fold every
remaining letter.  For each lower target, select the corresponding strict
upper target.  Its upper witness cannot contain `P_0` because its minimum
first coordinate is at least one; it consequently remains contiguous after
the deletion and folds to a lower witness.  Thus the folded word is lower
universal.  If the upper word spans `T_R`, the folded word spans
`T_(R-1)` as well.

This is the precise sense in which the strict-interior target family is
exactly self-similar.

## 3. Block-lift coverage audit

Let the requested upper target be

\[
 [u,r]\times[0,x],\qquad1\le u<r\le R,\quad1\le x<r.
                                                               \tag{3.1}
\]

Its folded parameters

\[
 u'=u-1,\qquad r'=r-1,\qquad x'=x-1                \tag{3.2}
\]

form a legal lower target: `0<=u'<r'<=R-1` and
`0<=x'<r'`.  Take a lower witness and, in the lifted word, take the complete
replacement blocks from the first witnessed lower occurrence through the
last.  No partial endpoint block is used.

### 3.1 First-coordinate extrema

Every preimage has first coordinate exactly one more than its lower image.
The lifted interval therefore has first-coordinate extrema `u,r`.

### 3.2 Minimum height

Every lower witness has minimum height zero, hence contains a lower peak.
The block of every lower peak contains a height-zero preimage:

* `P_0->[P_1]`; and
* `P_a->[P_(a+1),(a+1,1)]` for `a>=1`.

Thus the lifted minimum height is zero.  This also handles `u'=0`: a lower
witness may use `P_0`, whose singleton lift is still a genuine upper peak.

### 3.3 Positive folded height `x'>0`

Here `x=x'+1>=2`.  A lower cell of height `x'` has the unique preimage of
height `x`.  Every other positive-height singleton lifts by `+1`, and every
peak block has heights only zero and one.  Hence no lifted height exceeds
`x`, and the maximum is exactly `x`.

### 3.4 Zero folded height `x'=0`

This is the only delicate case.  Now the lower target has height zero, so
its witness consists entirely of peaks.  Since `u'<r'`, its maximum first
coordinate `r'` is positive; therefore it contains a nonzero peak.  The full
two-letter block of that peak contains a height-one preimage.  All lifted
blocks have height at most one.  The lifted extrema are consequently
exactly `0,1`, as required for the upper target `x=1`.

This confirms the proof in Theorem 2.  The order of the two letters inside a
peak block is irrelevant only because the selected lifted witness includes
the **complete** first and last blocks.  A later sparse or interleaved lift
cannot inherit this argument automatically.

## 4. Spanning audit

If the lower word contains every cell at least once, the union of the full
replacement blocks is the union of all fibres in (2.2), hence exactly

\[
                         \mathcal T_R\setminus\{P_0\}. \tag{4.1}
\]

The spanning assertion is therefore correct.  In particular, the lift
contains all cells of the scaffold except `P_0`:

* upper `P_1` comes from lower `P_0`;
* upper `P_s`, `s>=2`, comes from the block of lower `P_(s-1)`;
* `(2,1)` comes from that same lower `P_1` fibre; and
* `(s,s-1)`, `s>=3`, is the singleton preimage of
  `(s-1,s-2)`.

Thus inclusion (5.1) is exact under the explicitly stated spanning
hypothesis.

## 5. Boundary-scaffold audit

The scaffold

\[
 \mathcal B_R=
 P_R,P_{R-1},\ldots,P_0,
 (2,1),(3,2),\ldots,(R,R-1)                          \tag{5.1}
\]

has `(R+1)+(R-1)=2R` entries.

For `x=0`, the contiguous peak segment from `P_r` through `P_u` has exactly
first-coordinate extrema `u,r` and height zero.

For `u=0,x>=1`, take the interval from `P_r` through `P_0` and then through
`(x+1,x)`.  Its diagonal cells have first coordinates `2,...,x+1`.  Since
`x<r`,

\[
                         x+1\le r,                    \tag{5.2}
\]

so none contaminates the upper first-coordinate bound.  The peak segment
supplies first-coordinate minimum zero, maximum `r`, and height minimum
zero; the final diagonal cell supplies height maximum `x`.

The boundary proof is correct, including `x=1`; that case uses only the
single diagonal cell `(2,1)` and necessarily has `r>=2`.  The two regimes

\[
 (u=0\text{ or }x=0),\qquad(u>=1\text{ and }x>=1)     \tag{5.3}
\]

are disjoint and exhaustive.

Combining the scaffold with the lift also spans the full upper triangle:
the lift supplies (4.1), and the scaffold supplies the missing `P_0`.

## 6. Length and excess audit

Let the lower word have length `n`, and let `p_+(W)` count occurrences of
lower peaks `P_a` with `a>=1`.  Every such occurrence contributes one extra
letter under the full block lift, while every other occurrence contributes
one.  Hence

\[
                         |\mathcal L_R(W)|=n+p_+(W).   \tag{6.1}
\]

If

\[
                         n=|\mathcal T_{R-1}|+q,       \tag{6.2}
\]

then

\[
\begin{aligned}
 |\mathcal B_R\Vert\mathcal L_R(W)|-|\mathcal T_R|
 &=2R+|\mathcal T_{R-1}|+q+p_+(W)-|\mathcal T_R|\\
 &=q+R+p_+(W),                                        \tag{6.3}
\end{aligned}
\]

because `|T_R|-|T_(R-1)|=R`.  Formula (4.5) is correct.

When the lower word is a cell permutation, it contains exactly `R-1`
nonzero lower peaks.  The lift then contains every upper cell except `P_0`
exactly once, and literal concatenation adds one necessary `P_0` plus
`2R-1` repeated scaffold cells.  More generally, `2R-1` is the number of
scaffold **cell types** recopied across the concatenation; duplicates already
present in `W` and additional duplicated peak fibres are separately measured
by `q` and `p_+(W)-(R-1)`.

## 7. Scope corrections for the superposition claim

The following implications are proved:

1. `B_R || L_R(W)` is a universal spanning upper word.
2. The strict-interior target family is an exact fold quotient of the lower
   target family.
3. The displayed scaffold is one length-`2R` word covering every boundary
   target.
4. All scaffold cell types except `P_0` already occur somewhere in a full
   spanning lift.

They do **not** prove the following assertions currently suggested by the
words “exactly”, “equivalent”, and “if and only if” in Sections 1 and 5:

* Every near-once triangular word contains the scaffold `B_R` as a
  contiguous subword.
* Every near-once word is obtained by superposing `B_R` with a block lift.
* Even within a fold-based construction, the only economical way to cover
  boundary targets is to realize that exact scaffold order.
* A lower bound for this scaffold-embedding problem is a lower bound for the
  unrestricted triangular repetition number.

A boundary family can be represented by many different collections of
intervals; it need not contain the particular order (5.1).  Likewise, an
interior lift may choose different lower witnesses, split fibre elements,
or abandon literal block adjacency.  Once blocks are split, however, the
proof in Section 3 no longer certifies the lifted witnesses.  Their survival
becomes a coupled interval-selection and ordering problem, not merely an
independent binary choice at each peak occurrence.

### Safe conditional superposition statement

Fix a recursive construction architecture.  Suppose that at level `R` one
can start from a lower universal spanning word, place enough elements of its
fold fibres to preserve every strict-interior target, place every remaining
upper cell at least once, and cover all boundary targets, with at most
`delta_R` new repeated positions beyond those inherited from the lower
level.  Then

\[
                         q_R\le q_{R-1}+\delta_R.      \tag{7.1}
\]

If this is achieved with `delta_R=o(R)` uniformly as `R->infinity`, then

\[
                         q_R=o(R^2).                   \tag{7.2}
\]

Embedding the exact scaffold into a rearranged/sparsified lift is one
sufficient way to establish such a recurrence.  It is not known to be
necessary.

Conversely, proving that every realization **inside this specified
architecture** has `delta_R=Omega(R)` would show quadratic cumulative cost
for that architecture.  It would not, without an additional normal-form
theorem, prove a quadratic lower bound for arbitrary triangular words.

The phrase “two-choice interval-pinning problem” is therefore best read as
a proposed sufficient search model.  It is not yet an exact reduction:
height-one targets may draw their zero- and one-height providers from
different peak fibres, several lower witnesses may be available, and moving
unused preimages can contaminate or disconnect physical witness intervals.

## 8. Safe theorem ledger

The defensible result is:

> The strict-positive target family in dimension `R` is an exact fold
> quotient of the complete target family in dimension `R-1`.  Full fibre
> blocks give an explicit section.  A separate word of length `2R` covers
> the complementary boundary family, and literal concatenation has exact
> excess `q+R+p_+(W)`.

The open strengthening is:

> Can the fibre elements and boundary witnesses be globally ordered so that
> the two target families share their compulsory occurrences with
> `o(R)` new repetitions at level `R`?

This is a sharp and useful construction question.  It is not an equivalent
normal form for all universal triangular words unless an additional theorem
proves that equivalence.
