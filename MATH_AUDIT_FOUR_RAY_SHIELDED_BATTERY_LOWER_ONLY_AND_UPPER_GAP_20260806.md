# Independent audit of the four-ray shielded battery

**Date:** 2026-08-06  
**Method:** literal interval classification and rank audit  
**Verdict:** PASS for the sign, shield argument, cross-port isolation, and
`4m+1` position count.  FAIL for the original inference that lower-current
cancellation automatically cancels the native upper current.  The source
theorem has been corrected to the exact lower-only scope.

## 1. Literal one-port classification

In a port

\[
                         H,\{p\},\{z_1\},\ldots,\{z_t\},H,
                         \qquad H=\{a,d\},             \tag{1.1}
\]

an interval not containing the pivot is fixed.  An interval containing a
shield is also fixed, since the shield already contains both possible
pivot values.  Every changed interval therefore starts at the pivot and
ends at one of the `t+1` positions before the right shield.  This proves
the one-sided prefix current with no omitted two-sided interval.

When ports share consecutive shields, an interval meeting two ports
contains their common shield and is fixed.  Hence there is no hidden
cross-port current.

## 2. Sign audit

In `B_0 -> B_1`, the `Y^+,X^+` pivots change `d -> a`, while the
`Y^-,X^-` pivots change `a -> d`.  Their sum is

\[
\begin{aligned}
 &[Y_j^++a]-[Y_j^++d]+[X_j^++a]-[X_j^++d]\\
 &\quad+[Y_j^-+d]-[Y_j^-+a]+[X_j^-+d]-[X_j^-+a],
\end{aligned}                                           \tag{2.1}
\]

which is exactly `-D_j(X,Y;a,d)`.  Thus the sign in the corrected lower
theorem is right.

## 3. Rank boundary and the failed complement inference

Every changed interval in one port consists of one pivot and at most

\[
                         p=m-2
\tag{3.1}
\]

distinct chain letters.  Its rank is therefore at most `m-1`.  The same
linear battery has **zero** changed interval current in ranks `m` and
above.

By contrast, the upper current of the native cyclic wreath move is obtained
by complementing the lower basis sets inside the full `(2m+1)`-coordinate
ground.  That complementation is an algebraic correspondence within the
native cyclic row.  It does not create complementary occurrences in the
separate linear battery word.  Therefore

\[
 \boxed{
  \text{battery lower current}=-D
  \quad\not\Longrightarrow\quad
  \text{battery upper current}=-\overline D.}
\tag{3.2}
\]

The uncorrected statement that complementation alone closes the upper
current was an overclaim.

## 4. Position count

Each of the four chains has length `p`; there are four pivot positions and
five shields after adjacent shields are shared.  Hence the standalone
length is

\[
                         4p+4+5
                           =4(m-2)+9
                           =4m+1.                     \tag{4.1}
\]

This count is exact.

## 5. Minimal all-width repair hypothesis

Either of the following additional statements would promote the lower
battery to a complete all-width absorber.

1. **Dual battery.**  A protected second gadget has zero lower current and
   upper current `-overline(D)`, with every interval meeting both gadgets
   fixed.
2. **Complement-paired cyclic embedding.**  The four ports lie in a cyclic
   owner system with a literal occurrence bijection carrying every signed
   lower ray occurrence `S` to one upper occurrence `Omega-S`, preserving
   its coefficient and address.

Under either hypothesis the lower and upper ledgers cancel separately.
Neither hypothesis is supplied by the present linear word, so upper-dual
realization remains a genuine host gate.
