# Reverse-time gap sections are not disjoint: two self-dual PBBS components

**Date:** 2026-08-05  
**Method:** direct expanded-mark reversal; no computation or search  
**Status:** unconditional obstruction.  It rules out using a reverse-time
gap section as a disjoint backup for the forward section.

## 0. Outcome

Let `mathcal S^+` be the forward gap-potential q1 section of the canonical
PBBS factor, and define `mathcal S^-` by applying the same construction to
the inverse chronology `g^(-1)`.

Both sections have the whole-fan property: the forward statement is the
whole-fan theorem, and the reverse statement follows by reversing every
owner path.  However, they cannot be made edge-disjoint.  There are two
independent obstructions.

1. Scalar:

   \[
    |\mathcal S^+|=|\mathcal S^-|=N_1
      ={m\over m+2}W,
   \]

   so

   \[
    |\mathcal S^+\cap\mathcal S^-|
      \ge2N_1-W={m-2\over m+2}W
   \]

   for `m>2`.

2. Literal: on both the all-unit component `(10)^m` and the
   single-soliton component `1^m0^m`, forward and reverse gap rules select
   the same undirected q1 occurrence at every phase.

Thus reverse time does not supply a section-free edge on the wholly
selected single-soliton component, and it does not create a second quiet
tail on either extreme component.

## 1. What time reversal does to the expanded word

For a rank-`(m-1)` q1 core, write `A` on the forward-unmatched marks and
`C` on the reverse-unmatched marks, expanding a shared coordinate as
`C,A`.  The inverse PBBS construction reads the physical circle backward
and interchanges the two kinds of marks.  Thus its expanded word is obtained
by:

1. reversing the cyclic order; and
2. replacing original `A` by inverse `C`, and original `C` by inverse `A`.

The inverse gap potential must be recomputed on this reversed/swapped word.
It is not, in general, the negative of the original `C`-gap potential.
Therefore the slogan “forward maximum becomes reverse minimum” is false.

## 2. The all-unit component

For one outgoing q1 core on the all-unit component, the forward expanded
order is

\[
 C_r,A_r,C_p,A_p,A_z,C_w.
 \tag{2.1}
\]

The forward `C`-gap counts are

\[
                         (1,2,0),
\]

so the unique forward maximum is `C_w`, with last preceding forward mark
`A_z`.  Hence `mathcal S^+` selects the remote edge

\[
                         K+w\;--\;K+z.
 \tag{2.2}
\]

Reverse (2.1) and swap the mark types.  Starting at inverse
`C_(A_r)`, the inverse expanded order has gap counts

\[
                         (2,0,1).
 \tag{2.3}
\]

Its unique maximum is inverse `C_(A_z)`, and the last inverse `A` before it
is the mark coming from original `C_w`.  The inverse rule therefore selects

\[
                         K+z\;--\;K+w,
\]

the same undirected edge (2.2).

The rooted all-unit update only rotates the physical word, so this equality
holds on every phase of the component.

## 3. The single-soliton component

Use the notation of the whole-fan audit.  For

\[
                         A=0_r1^m0^m,
\]

let `p` be the final up-step and `v_1,...,v_m` the down-steps.  For
`K=A-{p}`, and `m>=3`, the forward expanded cyclic order is

\[
 C_p,C_{v_1},C_{v_2},
 A_{v_{m-1}},A_{v_m},A_r.
 \tag{3.1}
\]

Its gap counts are `(0,0,3)`, so the forward rule uniquely selects

\[
                         K+p\;--\;K+r.
 \tag{3.2}
\]

After reversing and swapping, start at inverse `C_(A_r)`.  The three
inverse gap counts are again

\[
                         (0,0,3).
 \tag{3.3}
\]

The inverse maximum is `C_(A_r)`, preceded by the inverse `A` coming from
original `C_p`.  Thus the inverse section also selects (3.2), with the
opposite orientation.

At `m=2`, the shared coordinates retain the order `C,A`; direct reversal
of the six-symbol expanded word gives the same conclusion.  Root rotation
then proves

\[
 E(C_{single})\subseteq
 \mathcal S^+\cap\mathcal S^-.
 \tag{3.4}
\]

## 4. Consequence

A topology move which punctures a forward-selected single-soliton edge also
punctures the reverse whole-fan bank.  Hence the reverse section does not
solve the selected-component repair problem.

It can still supply alternative occurrences on cores where the two rules
differ, but any such use must be occurrence-specific.  There is no global
disjoint-backup theorem, and no maximum/minimum duality may be invoked
without an independent literal check.

