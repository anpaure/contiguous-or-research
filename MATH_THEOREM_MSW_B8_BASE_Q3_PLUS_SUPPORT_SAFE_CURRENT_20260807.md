# The four-hex B8 macro is support-safe at every unmarked width q >= 3

**Date:** 2026-08-07  
**Method:** symbolic MSW flip recursion and exact path tracing; no
computation or search  
**Status:** unconditional finite base theorem for the z-free semilength-four
factor.  The q3 and q4 signed currents are nonzero, but every negative
retains literal multiplicity.  Widths at least five create only additional
rank-seven/full-set witnesses.  Marked closure-seam windows are outside
this theorem.

## 1. The six changed canonical paths

Use the six roots from the four-hex topology theorem:

```text
A=11110000  B=11010100  C=11011000
D=11010010  E=11100010  F=10110010.
```

Write `R0,R1,R2,R3` for the four rank-five colours on canonical path R.
The MSW recursion

\[
 \pi(1u0v)=(d,d-\pi(\mu u),1,d+\pi(v))             \tag{1.1}
\]

gives the following flip permutations:

\[
\begin{array}{c|c}
A&(8,2,6,4,5,3,7,1)\\
B&(8,6,7,4,5,2,3,1)\\
C&(8,4,6,5,7,2,3,1)\\
D&(6,4,5,2,3,1,8,7)\\
E&(6,2,4,3,5,1,8,7)\\
F&(2,1,6,4,5,3,8,7).
\end{array}                                         \tag{1.2}
\]

Tracing the twelve final incidence exchanges of H0--H3 gives exactly the
six z-free paths

\[
\begin{array}{c|l}
A_0-D_r&A0,A1,A2,C1,B0,B1,C2,D1,D2,D3\\
C_0-B_r&C0,B2,B3\\
C_r-A_r&C3,A3\\
D_0-F_r&F0,F1,F2,F3\\
F_0-E_0&E1,E0\\
E_r-B_0&E3,E2,D0.
\end{array}                                         \tag{1.3}
\]

The entries in the right column are colour sequences.  Their lengths are

\[
                         10,3,2,4,2,3,              \tag{1.4}
\]

and sum to the original 24 colours.

## 2. Exact q3 current on the changed paths

For a rank-five colour Y, use its three-element complement.  A q3 window
has complement equal to the intersection of the complements of its three
consecutive colours.

Before the macro, the two q3 windows on each of A--F omit respectively

\[
\begin{array}{c|c}
A&(7,2)\\ B&(3,6)\\ C&(3,4)\\
D&(8,4)\\ E&(8,2)\\ F&(8,1).
\end{array}                                         \tag{2.1}
\]

After the macro, the long path in (1.3) gives

```text
7, 7, 7, 3, {3,5}, 3, 4, 4,
```

where `{3,5}` denotes a rank-six value whose complement is the displayed
two-set.  The paths `C0-Br`, `D0-Fr`, and `Er-B0` give respectively

```text
6 ; 8,1 ; 3,
```

and the two length-two paths give no q3 window.

Consequently the complete signed current of the changed bank is

\[
\boxed{
\begin{aligned}
 \delta_3^B={}&2[11111101]+[11011111]+[11010111]\\
              &-2[10111111]-2[11111110].
\end{aligned}}                                      \tag{2.2}
\]

The rank-seven masks in (2.2) omit coordinates `7,3,2,8`, respectively;
`11010111` is the rank-six value with complement `{3,5}`.

## 3. Global multiplicities prove q3 support safety

The eight unchanged Dyck roots have q3 omitted-coordinate pairs

\[
\begin{array}{c|c}
11101000&(7,2)\\
11100100&(5,6)\\
11001100&(7,2)\\
11001010&(8,2)\\
10111000&(7,1)\\
10110100&(5,1)\\
10101100&(7,1)\\
10101010&(8,1).
\end{array}                                         \tag{3.1}
\]

Adding (2.1) and (3.1), the canonical multiplicities of the eight
rank-seven targets, indexed by their omitted coordinate, are

\[
                         (5,5,2,2,2,2,5,5).         \tag{3.2}
\]

After (2.2) they are

\[
                         (5,3,3,2,2,2,7,3).         \tag{3.3}
\]

Every rank-seven target therefore remains represented.  In particular the
two negative multiplicities in (2.2) fall only from five to three.

## 4. q4 and all later widths

Every canonical path has four colours and its unique q4 window is the full
eight-set.  Thus the canonical full-set multiplicity is 14.

On the long new path, the seven q4 windows have complement intersections

```text
{7}, {7}, empty, {3}, {3}, empty, {4}.
```

The length-four path `D0-Fr` supplies one further empty intersection.  The
other four paths are too short.  Hence after the macro:

* the full eight-set still has multiplicity three;
* two extra rank-seven windows omit 7;
* two omit 3; and
* one omits 4.

Equivalently the q4 current is

\[
 2[11111101]+2[11011111]+[11101111]
 -11[11111111].                                     \tag{4.1}
\]

It is not zero, but its only negative is the full set, whose multiplicity
remains three.

At q5, the long path gives

```text
omit 7, full, full, omit 3, full, full.
```

There were no canonical z-free q5 windows, so these are gains only.  Every
q-window on the long path is the full set for q at least six.  Therefore no
q >= 5 target can be lost.

### Theorem 4.1

The B8 four-hex macro preserves the complete z-free upper support at every
width q >= 3.  Its wider currents are not transparent as signed multisets,
but every negative term has a literal surviving occurrence.

## 5. Dyck suffixing and the annulus consequence

Appending a Dyck suffix adds the same fixed up-set to every colour in a
base path and preserves the path order.  Restriction to base coordinates
therefore leaves every complement intersection above unchanged.  The
multiplicity tables (3.2)--(3.3) and the full-set counts tensor exactly in
each suffix fibre.

Combined with the full-annulus endpoint-coboundary theorem, this proves:

> Every chronology-faithful `01 -> 10` carry of the B8 packet is q3+-
> support-safe on the complete z-free suffix bank.  No audit of the
> individual transport faces at q3+ is required.

The current is transported rather than annihilated, but the base spare
occurrences transport with it.

## 6. Scope

This theorem closes the finite unmarked/z-free q3+ gate.  It does not prove
that one MNW hypertree contains the turn-, chronology-, and socket-faithful
annulus, nor does it audit windows crossing the lifted z-closure or other
marked chronology seams.  Those require the static host theorem and its
marked socket ledger.
