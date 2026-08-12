# Odd APH after reserving the fixed collar: the exact imbalance-three resource theorem

**Date:** 2026-08-06  
**Method:** a transition-matching argument in a punctured linear word; no
computation or search  
**Status:** unconditional resource theorem.  This repairs item 2 of the
minimal package in
`MATH_AUDIT_ODD_APH_TEMPORARY_CART_DICHOTOMY_20260806.md`.  It is only a
resource statement; it does not by itself supply an occurrence-labelled
moving head.

## 1. The correctly punctured word

Write

\[
 A=00,\qquad B=20,\qquad C=22.
\]

Start with a balanced connector word, so that the total numbers of `A` and
`C` agree.  Remove the protected first connector and the two named source
blocks of the fixed collar.  The remaining linear work word \(w\) has

\[
             |w|=m-3,
       \qquad |\#A(w)-\#C(w)|\le 3.                 \tag{1.1}
\]

The second inequality is sharp: three removed blocks may all have the same
extreme sign.

An **ordinary atom** is either a transition interval

\[
                  A B^s C\quad\hbox{or}\quad C B^s A
                                                        \tag{1.2}
\]

or an adjacent neutral pair `BB`.  Delete the `B`'s and call the resulting
binary linear word \(\bar w\).

## 2. One atom is unavoidable at length eight

### Theorem 2.1 (reserved-collar one-atom theorem)

If \(w\) satisfies (1.1) and \(|w|\ge8\), then \(w\) contains an ordinary
atom.

#### Proof

If \(\bar w\) has a transition, the corresponding two consecutive extreme
letters, together with the intervening `B`-run, give (1.2).  Suppose it has
no transition.  Then all extreme letters have one sign.  By (1.1) there are
at most three of them.

If `BB` does not occur, every linear `B`-run has length at most one.  At most
four such runs surround at most three extreme letters, so

\[
                         |w|\le3+4=7.
\]

This contradicts \(|w|\ge8\).  Hence `BB` occurs.  \(\square\)

For the odd parameterization \(k=2m-1\), this starts at \(m=11\), hence at
\(k=21\).  Unlike the old length-ten claim, this threshold is computed
*after* the first connector and both collar blocks have been reserved.

## 3. The full two-atom/compound dichotomy survives at length fourteen

### Theorem 3.1 (imbalance-three dichotomy)

Let \(w\) satisfy (1.1) and \(|w|\ge14\).  Then at least one of the following
holds.

1. The word contains two block-disjoint ordinary atoms.
2. Four consecutive vertices of \(\bar w\) have type `AACC` or `CCAA`, and
   the physical interval from the first to the fourth has length at most
   nine.

#### Proof

Consider the transition edges of the binary path \(\bar w\).  If their
matching number is at least two, two matched edges give two block-disjoint
transition atoms.  Assume henceforth that the matching number is at most
one.  A path with this property has at most two transition edges.

**No transition.**  All extremes have one sign, so there are at most three.
If there are not two disjoint `BB` pairs, then across the at most four
`B`-runs

\[
                  \sum_G\lfloor |G|/2\rfloor\le1.
\]

At most one run has length two or three and all others have length at most
one.  Thus there are at most six `B`'s and \(|w|\le9\), a contradiction.

**Two transitions.**  Since the two transition edges must meet, the middle
extreme run has length one.  Up to exchanging `A,C`,

\[
                         \bar w=A^p C A^q.
\]

By (1.1), \(p+q-1\le3\), so \(|\bar w|\le5\).  Any adjacent `BB` pair is
disjoint from at least one of the two transition atoms: if it lies on one
side of the singleton `C`, use the transition on the other side.  Therefore
the failure of outcome 1 implies that every `B`-run has length at most one.
There are at most six such runs, and hence \(|w|\le11\), again a
contradiction.

**One transition.**  Up to exchanging the letters,

\[
                         \bar w=A^pC^q.              \tag{3.1}
\]

If \(p,q\ge2\), take the last two `A`'s and the first two `C`'s.  Let
\(g_1,g_2,g_3\) be the three intervening `B`-run lengths.  If \(g_1\ge2\)
or \(g_3\ge2\), a `BB` pair there is disjoint from the transition atom.  If
\(g_2\ge4\), that middle run contains two disjoint `BB` atoms.  Otherwise

\[
                         g_1\le1,\qquad g_2\le3,
                         \qquad g_3\le1,
\]

and the selected `AACC` interval has length at most

\[
                              4+1+3+1=9.
\]

This is outcome 2.

It remains that \(\min(p,q)=1\).  By (1.1), the other multiplicity is at
most four, so \(|\bar w|\le5\).  A `BB` pair outside the unique transition
gap is disjoint from the transition atom.  Four `B`'s in the transition gap
contain two disjoint `BB` pairs.  Thus, if outcome 1 fails, the transition
gap has length at most three and each of the at most five other `B`-runs has
length at most one.  Consequently

\[
                          |w|\le5+3+5=13,
\]

contrary to the hypothesis.  This exhausts all cases.  \(\square\)

## 4. Exact consequence and scope

For \(k=2m-1\), Theorem 3.1 starts at \(m=17\), hence \(k=33\).  Theorem
2.1 is enough for any bootstrap using one anchored mobile head and already
starts at \(k=21\).  The stronger dichotomy is retained because a future
two-head construction may use it.

The theorem corrects only the resource arithmetic.  In particular it does
not assert that:

* two selected atom paths are occurrence-disjoint;
* the bounded `AACC/CCAA` construction has an early orientation record; or
* a cart can cross a protected `H`, `H|M`, or `M|H` island.

Those are separate literal-path questions.
