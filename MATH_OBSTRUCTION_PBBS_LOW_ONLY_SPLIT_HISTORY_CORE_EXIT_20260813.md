# Splitting only the low PBBS spine does not evade source-history holonomy

**Date:** 2026-08-13  
**Status:** unconditional source-letter no-go for the proposed hybrid which
uses the same ordered history on both halves of every split macro, replaces
the consecutive low role-zero edges beginning at height `4`, and then
returns to the direct height spine.  The obstruction occurs already at the
fourth junction, before the earlier `d+1`-junction holonomy bound.

## 1. Consecutive core exchange

For the PBBS height core

\[
 H_h=\{0\}\cup\{h+2,\ldots,2h\}
       \cup\{2h+4,2h+6,\ldots,2r\},
\tag{1.1}
\]

put

\[
 X_{h+1}=H_h\setminus H_{h+1}=\{h+2,2h+4\},
 \qquad
 Y_h=H_{h+1}\setminus H_h=\{2h+1,2h+2\}.
\tag{1.2}
\]

Let

\[
 \mathcal C_h=(C_{h,1},\ldots,C_{h,d})
\tag{1.3}
\]

be the ordered history used on both halves of the split macro at height
`h`.  Literal overlap of the terminal half-block at height `h` with the
initial half-block at height `h+1` forces

\[
 C_{h,1}=X_{h+1},
 \qquad
 \mathcal C_{h+1}
   =(C_{h,2},\ldots,C_{h,d},Y_h).
\tag{1.4}
\]

The recurrence is equality of source letters, not merely equality of their
unions.

## 2. A copied block exits the future core

Starting with the split macro at height `4`, recurrence `(1.4)` appends the
literal block

\[
                         Y_4=\{9,10\}
\tag{2.1}
\]

to `\mathcal C_5`.  Every subsequent junction shifts this block one queue
position to the left.  If the split chain reaches the macro at height `8`,
then `Y_4` is still one of the displayed history letters of
`\mathcal C_8`.

But direct substitution in `(1.1)` gives

\[
 H_8=\{0\}\cup\{10,11,\ldots,16\}
          \cup\{20,22,\ldots,2r\},
\tag{2.2}
\]

and therefore

\[
                         9\notin H_8,
 \qquad                  Y_4\not\subseteq H_8.
\tag{2.3}
\]

Every source history letter in the split half-block at height `8` is
contained in every owner window of that half-block and hence must be a
subset of its common core `H_8`.  Equations `(2.1)--(2.3)` contradict this
necessary condition.

The same argument is uniform.  A block `Y_j={2j+1,2j+2}` appended at the
`j`-th junction is not contained in `H_{2j}`, because `2j+1` lies below the
first interval element `2j+2` of `H_{2j}`.  Thus a same-history split chain
cannot carry that block through the macro at height `2j`.

### Theorem 2.1 (four-junction core-exit no-go)

No depth-`d` source chronology can contain the same-history split macros
at all heights

\[
                         4,5,6,7,8.
\tag{2.4}
\]

Equivalently, beginning with height `4`, the proposed hybrid cannot pass
four consecutive junctions and then enter the height-`8` macro.  In
particular, replacing all direct edges `e_h` for `4<=h<=d` fails for every
`d>=8`.

This obstruction is independent of the number `d` of queue letters.  It
therefore precedes the more general `d+1`-junction holonomy equation.

## 3. Why a high-spine terminal partition cannot repair it

Choosing a maximal antecedent history at the first retained direct high
edge and shifting that history backwards still has to satisfy the literal
recurrence `(1.4)` at every preceding split junction.  Hence the backward
history necessarily contains the same copied `Y_4` block, while the
forward recurrence still requires that block to occur inside `H_8`.
Terminal freedom changes neither `(1.4)` nor `(2.3)`.

There is also an owner-run interpretation.  The coordinate `9=2\cdot4+1`
is inserted by `e_4` and deleted by `e_8`.  A copied source letter
containing `9` cannot remain a history letter through the height-`8`
interface, where the common owner intersection no longer contains it.
This is exactly the core-exit witnessed in `(2.3)`.

## 4. Exact surviving scope

The result does not invalidate the local palette split, nor does it rule
out a genuine history-changing detour at every macro.  It rules out the
specific shortcut

\[
 \boxed{
  \text{split only }4\le h\le d
  +\text{ same input/output history per macro}
  +\text{ terminal high-spine backshift}.}
\]

Two possible escapes remain:

1. introduce a real source-history reset which removes an old appended
   block before it exits the next common core; or
2. transport only the selected lower-compiler occurrences on protected
   auxiliary providers, freeing the palette path from complete old-context
   transport.

Neither escape follows from the local split theorem alone.
