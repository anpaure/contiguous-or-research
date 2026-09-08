# A unique alternating C8 fixes the contextual boundary and relays the hole to `R0`

**Date:** 2026-08-07  
**Method:** exact Johnson-detour normal form, touching-step phases, and q2
turn replay; no computation or search  
**Status:** unconditional local theorem after the direct `J` face.  The C8
is the unique simple length-eight incidence cycle effecting the named
boundary transfer.  It makes one contextual reverse hex literal, but the
three-face macro moves the q2 hole to `R0=1100111110` rather than closing it.

## 1. The one-bad-owner contextual hex

After the direct `J` face, consider the contextual base hex with owners

\[
 A=1100100110,\qquad B=1100010110,\qquad C=1100000111
\]

and colours

\[
 P=1100110110,\qquad N=1100010111,\qquad Q=1100100111.
\]

The reverse orientation requires selected incidences

\[
                         AQ,\qquad BP,\qquad CN.      \tag{1.1}
\]

The actual post-face state already has `BP` and `CN`, but has `AP` instead
of `AQ`.  Thus the complete six-cycle obstruction is the single transfer

\[
                         AP\longmapsto AQ.            \tag{1.2}
\]

No incidence hexagon effects (1.2): for the five possible core labels
`1,2,5,8,9`, the first auxiliary owner never supplies the required
addition ten with the core edge absent, or the second auxiliary owner fails
the complementary phase.

## 2. Exact C8 normal form

For two colours `P=A+6` and `Q=A+10`, every simple incidence C8 through
`AP,AQ` and avoiding `A` otherwise has the form

\[
 A-Q-B_1-R_1-B_2-R_2-B_3-P-A,                      \tag{2.1}
\]

where

\[
\begin{aligned}
B_1&=Q-s,&R_1&=Q-s+x,\\
B_2&=A-s+x,&R_2&=P-s+x,\\
B_3&=P-s,
\end{aligned}                                       \tag{2.2}
\]

with

\[
 s\in A=\{1,2,5,8,9\},\qquad
 x\in\{3,4,7\}.                                    \tag{2.3}
\]

For (2.1) to alternate in the required orientation, the selected edges are

\[
 QB_1,\qquad R_1B_2,\qquad R_2B_3,\qquad PA,        \tag{2.4}
\]

and the other four are unselected.  Equivalently:

1. `B_1` selects addition `s`;
2. `B_2` selects addition ten and not addition six;
3. `B_3` selects addition `x` and not addition `s`.

The exact touching-step test collapses the fifteen cases as follows.

\[
\begin{array}{c|c|c}
s&\text{surviving }x\text{ after }B_1,B_2&
 \text{surviving }x\text{ after }B_3\\ \hline
1&\varnothing&\varnothing\\
2&\varnothing&\varnothing\\
5&\varnothing&\varnothing\\
8&\varnothing&\varnothing\\
9&\{3,4\}&\{4\}.
\end{array}                                         \tag{2.5}
\]

Hence exactly one C8 alternates, namely `(s,x)=(9,4)`.

## 3. The literal C8

Its vertices are

\[
\begin{aligned}
A  &=1100100110,\\
Q  &=1100100111,\\
B_1&=1100100101,\\
R_1&=1101100101,\\
B_2&=1101100100,\\
R_2&=1101110100,\\
B_3&=1100110100,\\
P  &=1100110110.
\end{aligned}                                       \tag{3.1}
\]

The edge statuses in this order are

\[
                         0,1,0,1,0,1,0,1.            \tag{3.2}
\]

Here `B_1` is the centre of the direct `J` face and selects additions
`7,9`; `B_2` is a Dyck endpoint selecting addition ten; and `B_3` is a
Dyck endpoint selecting addition four.  These are precisely the three
selected conditions in (2.4).  Toggling the C8 performs (1.2), so the
contextual reverse hex becomes literally alternating.

## 4. Exact q2 current of the C8

Only `A` and `B_1` are internal lower owners.  Put

\[
\begin{aligned}
E_0&=1101110110,&W&=1101100111,\\
F_0&=1101101101,&J&=1100101111.
\end{aligned}
\]

At `A`, the untouched mate is addition four and the turn changes
`E_0 -> W`.  At `B_1`, the untouched mate is addition seven and the turn
changes `J -> F_0`.  Thus

\[
 \boxed{\partial_2 C_8=[W]+[F_0]-[E_0]-[J].}        \tag{4.1}
\]

## 5. The now-alternating reverse hex

After the C8, toggle the reverse contextual base hex on `A,B,C`.  Its
ownerwise turn changes are

\[
\begin{array}{c|c|c}
\text{owner}&\text{old}&\text{new}\\ \hline
A&W&E_0,\\
B&R_0=1100111110&U=1100011111,\\
C&V=1101010111&W.
\end{array}                                         \tag{5.1}
\]

Therefore

\[
 \partial_2 H_F^{-1}=[E_0]+[U]-[R_0]-[V].          \tag{5.2}
\]

The direct `J` face had current

\[
 \partial_2H_J=[J]+[V]-[U]-[W].                    \tag{5.3}
\]

Adding (4.1)--(5.3), every intermediate target cancels and gives

\[
 \boxed{
 \partial_2(H_J+C_8+H_F^{-1})=[F_0]-[R_0].}         \tag{5.4}
\]

The target `R_0` has the unique canonical inverse witness `(5,7)`, at the
owner `B`.  The reverse hex deletes that occurrence.  Hence (5.4) is an
exact one-unit relay, not a support-closed repair.

## 6. Suffix and topology scope

Every displayed q2 target ends at height four.  Appending a Dyck suffix
preserves all touching phases and inverse multiplicities, and suffix
projection separates distinct copies.  Thus the C8 and reverse-hex bank
tensors literally.

No claim is made here that the C8 and three incidence faces extend to the
particular published MNW spanning hypertree with the required component
action.  The exact next q2 target is

\[
                         \boxed{1100111110v}.         \tag{6.1}
\]

