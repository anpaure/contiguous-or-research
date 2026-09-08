# Independent-style audit: four-slot Bellman efficiency normal forms

**Date:** 2026-08-04  
**Audited theorem:**
`MATH_THEOREM_FOUR_SLOT_BELLMAN_EFFICIENCY_NORMAL_FORMS_20260804.md`  
**Verdict:** **PASS** as an exact reduction.  Four-slot positivity is left
open.

## 1. Efficiency split

Internal superadditivity gives `x<=y/2`, so the maximal generator is among
sizes two, three, and four.  If size two is maximal, `T<=2y`, while the
table gives `T>=2y`; hence equality.  The parity exchanges in Theorem 1.1
are identical to the already audited two-coset exchanges.

The positive subcase `y>=A` compares the shifted negative tail at `r` with
the larger tail at `x`; all positive-period arguments are at least `A`, so
the inequality direction is correct.  The unresolved endpoint range is
exactly `A/2<=y<A`.

## 2. Three-slot-efficient recurrence

The definitions give

\[
 x\le u,quad 3u\le z,quad 3y\le2z,quad u+y\le z.
\]

They imply every inequality in (2.7).  Direct recurrence substitution
checks the exceptional entries

\[
 V_1=x,quad V_2=y,quad V_5=z+\max(y,u+x),
\]

and the eventual residue offsets `0,u,max(y,2u)`.  The effective table is
internally superadditive, and `2w<=z+u` makes its own residue-one offset
equal to `u`.

The comparison (2.8) lists all and only the three exceptional positions.
Its first two terms have no unconditional sign, while its last term is
nonpositive in the increasing tail, so no positivity claim is smuggled
into the reduction.  Also
`z>=3T/4` does not imply `z>=A`; the normalization warning is necessary.

## 3. Four-slot-efficient Apery form

Every reduced edge weight is nonpositive.  A repeated vertex in a residue
walk cuts out a closed segment of total capacity divisible by four and
nonpositive reduced weight, so removal preserves or improves the walk.
There is therefore a simple maximizer with at most three edges and capacity
at most nine.

Because the size-one generator has nonnegative value, an underfilled
integer configuration can be filled exactly without lowering value.
Padding a maximizing residue walk with zero-reduced-weight size-four edges
then gives the eventual formula.  The threshold is determined by the
chosen simple walk and is below ten, exactly as stated.

## 4. Scope

The note does not prove:

* positivity in the compact two-coset range (1.4);
* nonnegativity of the transient correction (2.8);
* positivity of the four-coset Apery prefix/tail;
* the universal Bellman inequality or an additive OR-word bound.

It isolates the first genuinely new finite obstruction after the complete
`n<=3` theorem.
