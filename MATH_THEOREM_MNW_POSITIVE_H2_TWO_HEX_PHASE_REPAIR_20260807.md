# Positive H2 has an exact ordered two-hex phase repair

**Date:** 2026-08-07  
**Method:** exact touching-step replay; no computation or search  
**Status:** unconditional incidence-phase theorem after the repaired
positive-H1 prefix.  The two faces make positive H2 literally alternating.
Their complete q2 current is explicit but not yet support-closed.

## 1. The two H2 phase defects

The positive H2 owners are

```text
X1 =1011000101
X2 =1011000110
X3 =1011010100.
```

Before any H2 repair, their touching-step selected additions are

```text
X1 : {6,7}
X2 : {2,6}
X3 : {2}       (Dyck endpoint).
```

Positive H2 requires respectively

```text
X1 : old 9 selected, new 6 unselected
X2 : old 6 selected, new 10 unselected
X3 : old 10 selected, new 9 unselected.
```

Thus X2 is already correct, while X1 and X3 are not.

## 2. First face: move the endpoint phase

Put `K0=1011000100` and use active labels `6,2,10`.  The lower owners are

```text
K0+6  =1011010100 = X3,   selected {2}
K0+2  =1111000100,        selected {10}
K0+10 =1011000101 = X1,   selected {6,7}.
```

The six statuses alternate.  Toggling the face performs

```text
X3 : 2 -> 10,
K0+2 : 10 -> 6,
X1 : 6 -> 2  (retaining 7).
```

Only X1 is internal.  Hence its q2 current is

\[
 [1111001101]-[1011011101].                         \tag{2.1}
\]

## 3. Second face: finish X1

Now put `K1=1001000101` and use active labels `3,2,9`.  Its lower owners
and current pairs are

```text
K1+3 =1011000101 = X1, selected {2,7}
K1+2 =1101000101,      selected {7,9}
K1+9 =1001000111,      selected {3,5}.
```

This face is alternating and performs

```text
X1 : 2 -> 9  (retaining 7),
K1+2 : 9 -> 3 (retaining 7),
K1+9 : 3 -> 2 (retaining 5).
```

Its turn rows telescope to

\[
 [1011001111]+[1101100111]
 -[1101001111]-[1011100111].                        \tag{3.1}
\]

After the two faces the three H2 pairs are

```text
X1 : {7,9}
X2 : {2,6}
X3 : {10},
```

so positive H2 is literally alternating.

## 4. H2 and the combined current

With the contextual mates above, H2 has current

\[
 [1011011101]+[1111000111]
 -[1011001111]-[1111010110].                        \tag{4.1}
\]

Adding (2.1), (3.1), and (4.1) cancels both transfer intermediates and
gives the exact phase-packet current

\[
\boxed{
 [1111001101]+[1101100111]+[1111000111]
 -[1101001111]-[1011100111]-[1111010110].}          \tag{4.2}
\]

The two faces are the literal first two transport shells forced by the
positive-context endpoint mismatch: the first moves the exposed endpoint
ticket, and the second carries its displaced X1 ticket to the desired H2
edge.  Reversing their order fails because X1 does not yet select addition
two.

## 5. Exact negative multiplicities

The three negative targets in (4.2) have inverse lists

\[
\begin{array}{c|c|c}
\text{target}&\text{inverse pairs}&\text{load before the packet}\\ \hline
1101001111&(7,9)&1,\\
1011100111&(3,5),(6,7)&2,\\
1111010110&(2,6)&1.
\end{array}                                         \tag{5.1}
\]

The first and third occurrences are precisely the turns removed in
(4.2).  Neither target is changed by the preceding gamma--alpha, endpoint,
`H0`, repair-C8, safe-`L_0`, or `H1` currents.  Therefore the ordered
two-face H2 phase repair opens the two additional unit holes

\[
                         1101001111,\qquad1111010110. \tag{5.2}
\]

The middle negative retains its `(6,7)` provider.  Thus the phase packet is
not q2-support safe by itself.

## 6. Scope

Equation (4.2) is an exact signed q2 ledger and (5.2) is its exact support
defect.  Its interaction with the two residual repair-C8 holes must be
priced jointly.  Positive H3 also has a contextual phase mismatch and is
not asserted literal here.  Component action and q3+ remain open.
