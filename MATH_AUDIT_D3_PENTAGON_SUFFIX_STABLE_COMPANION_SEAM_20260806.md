# Independent audit of the suffix-stable `D_3` companion seam

**Date:** 2026-08-06  
**Method:** direct symbolic alignment; no computation or search  
**Status:** PASS for the corrected connected phase union; FAIL for the
withdrawn claim that both whole base companion graphs persist.

## 1. Base correction

The former positive `5--2` first row

\[
                         (3,1,5,2,6,\infty,4)        \tag{1.1}
\]

is neither a rotation nor a reversal of positive row 5

\[
                         (3,1,4,5,2,6,\infty).       \tag{1.2}
\]

It is invalid and must be deleted.  The four positive alignments

\[
                         1-4,\quad3-2,\quad4-3,\quad4-5 \tag{1.3}
\]

are literal companion normal forms and remain connected: they give
`1-4-3-2` with the branch `4-5`.  The displayed negative tree is also
literal.

## 2. Exact stable edges

Let `U` and `V` be the ordered fresh deletion and insertion banks.  Direct
rotation of the four relevant row pairs gives

\[
\begin{array}{c|c|c|c|c}
\text{phase/edge}&r_0&r_1&X&Y\\ \hline
-/12&(4,5,V,\infty,2,3,1,U,6)&
      (5,3,V,\infty,4,2,1,U,6)&(V,\infty)&(1,U,6)\\
-/54&(4,3,U,2,6,5,V,\infty,1)&
      (3,5,U,2,4,6,V,\infty,1)&(U,2)&(V,\infty,1)\\
+/14&(5,4,V,\infty,3,2,1,U,6)&
      (4,2,V,\infty,5,3,1,U,6)&(V,\infty)&(1,U,6)\\
+/32&(5,2,U,3,6,4,V,\infty,1)&
      (2,4,U,3,5,6,V,\infty,1)&(U,3)&(V,\infty,1).
\end{array}                                             \tag{2.1}
\]

Every row pair in (2.1) has the exact form

\[
             (a,b,X,c,d,Y),\qquad(b,d,X,a,c,Y).       \tag{2.2}
\]

Thus the suffix-stable phase matchings are

\[
                         M^- =\{12,54\},\qquad
                         M^+ =\{14,32\}.              \tag{2.3}
\]

Their union is the spanning path

\[
                         3-2-1-4-5.                   \tag{2.4}
\]

This independently verifies the corrected connected-union theorem.

## 3. Why `43` and `45` do not survive

In the displayed base alignment for `43`, row 4 places the two fresh-bank
cuts in the normal-form gaps `d|Y` and `a|b`, while row 3 places them in
`c|d` and `Y|a`.  Edge `45` has the same kind of mismatch.  Hence neither
tail merely enlarges the common `X,Y` blocks.

There is no alternative common-tail alignment.  All fresh labels must be
common positions of (2.2).  Aligning the two disjoint labelled banks fixes
the relative rotation of the old rows.  Under that rotation, rows `4,3`
agree positionwise only at `infinity`; rows `4,5` do likewise.  A native
pair needs three old common positions in addition to the fresh banks.  For
a one-step tail, a relative reflection cannot align both marked gaps
(positions `3` and `7` on the resulting 9-cycle); for a longer tail, the
ordered banks already force the orientation.  Thus `43,45` fail for every
nonempty common suffix.

## 4. All-k implication

The connected-union **topology** premise of the corrected phase-switched
companion theorem is now unconditional in every semilength.  This is a
real improvement over the four-row Tamari tensor, whose audited native
graph retains only one edge.

It is not yet the phase-switched group theorem.  The seam provides one
static inverse slot on each of four edges, in two slot classes separated
by the semilength.  It does not provide every diagonal element of
`A_(2r+1)` on an edge, and two fixed involutions alone generate only a
dihedral-type subgroup.  More importantly, applying a native inverse move
has nonzero q1/deeper current and is not proved to return to a reusable
complete guarded phase.

The exact remaining statement is therefore:

> **Guarded generator-complete seam lemma.**  Conjugate/regenerate the
> four stable inverse slots so that their based excursions provide a
> generator-complete diagonal row action, while absorbing every nested-
> rail current and retaining one marked generator plus the terminal common
> cap.

Until that lemma is proved, the anchored suffix lift closes companion
connectivity but not the all-k construction.
