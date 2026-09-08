# The asymmetric one-coordinate lift has a rank-shell obstruction

Date: 2026-07-25

## 0. Verdict

Let

\[
Q_R=[0,R]^3
\]

with the coordinatewise order and coordinatewise maximum.  Suppose a
universal word has the form

\[
U_R=P\,C\,S,
\qquad
C=U_{R-2}+(1,0,0).
\]

Then, for every \(R\ge 5\),

\[
\boxed{|P|+|S|\ge 5R-5.}
\]

In particular, the proposed outside ledger

\[
|P|+|S|=3R+e_R,
\qquad e_R=o(R),
\]

is impossible: necessarily

\[
\boxed{e_R\ge 2R-5.}
\]

The obstruction is not a support toll and does not assume that old selected
witnesses survive.  It uses only the contiguity and bounding box of the
retained core.  More generally, every recurrence retaining one contiguous
translate of an \((R-2)\)-cube has outside cost at least \(4R-O(1)\).

## 1. The outside-endpoint injection

### Lemma 1.1 (contiguous-core exterior-antichain injection)

Let \(W=P\,C\,S\) be a word over a finite product of chains.  Let \(B\) be
any subset closed under coordinatewise maximum (in particular, any
subbox), and assume every letter of the contiguous factor \(C\) belongs to
\(B\).  If \(\mathcal A\) is an antichain disjoint from \(B\), and every
member of \(\mathcal A\) is represented by a contiguous factor of \(W\),
then

\[
\boxed{|P|+|S|\ge |\mathcal A|.}
\]

#### Proof

Choose one witness \(I_T=[\ell_T,r_T]\) for each \(T\in\mathcal A\).
No \(I_T\) lies wholly in \(C\), because a coordinatewise maximum of
letters in the join-closed set \(B\) is again in \(B\), whereas
\(T\notin B\).

Define an outside endpoint \(\phi(T)\) as follows.

* If \(r_T\) lies in the suffix \(S\), put \(\phi(T)=r_T\).
* Otherwise \(r_T\) lies weakly before \(S\).  Since \(I_T\) is not wholly
  in \(C\), its left endpoint must lie in \(P\); put
  \(\phi(T)=\ell_T\).

The two cases are exhaustive even when a witness touches both outside
pieces.  Such a witness ends in \(S\) and is charged only to its right
endpoint.  Conversely, a witness which does not end in \(S\) and does not
start in \(P\) would have both endpoints in \(C\), contrary to
\(T\notin B\).  Hence all left charges lie in \(P\), all right charges lie
in \(S\), and the two image sets are physically disjoint.

Thus \(\phi(T)\) is always a position of \(P\cup S\).  If two distinct
targets were mapped to the same prefix position, their selected intervals
would have the same left endpoint and hence would be nested.  Their maxima
would be comparable.  The same holds for two targets mapped to the same
suffix position, using their common right endpoint.  A prefix position and
a suffix position are distinct.  Since two distinct members of an
antichain cannot be comparable, \(\phi\) is injective.  This proves the
claim. \(\square\)

The asymmetric recurrence is therefore governed by the width of the
complementary rank shell, not merely by the support of its zero face.

## 2. Exact rank-shell count for the proposed shift

The retained factor lies in the subbox

\[
B_R=(1,0,0)+[0,R-2]^3
=[1,R-1]\times[0,R-2]^2.
\]

Let

\[
\mathcal A_R
=\{(x,y,z)\in Q_R\setminus B_R:x+y+z=2R\}.
\]

This is an antichain.  We now count it exactly.

Complementing all three coordinates maps rank \(2R\) of \(Q_R\) to rank
\(R\).  At rank \(R\), the upper bounds are inactive, so

\[
\bigl|\{v\in Q_R:|v|=2R\}\bigr|
=\binom{R+2}{2}.
\]

A point of \(B_R\) has the form \((1+u,v,w)\), with
\(0\le u,v,w\le R-2\).  It has rank \(2R\) exactly when

\[
u+v+w=2R-1.
\]

Complementing inside \([0,R-2]^3\) changes this to rank

\[
3(R-2)-(2R-1)=R-5.
\]

For \(R\ge5\), the coordinate caps are again inactive at rank \(R-5\),
and hence

\[
\bigl|\{v\in B_R:|v|=2R\}\bigr|
=\binom{R-3}{2}.
\]

Therefore

\[
|\mathcal A_R|
=\binom{R+2}{2}-\binom{R-3}{2}
=5R-5.
\]

Lemma 1.1 gives

\[
|P|+|S|\ge5R-5,
\]

which proves the verdict.

## 3. Exact asymptotic consequence under iteration

If the same architecture is used at every scale, and \(N_R=|U_R|\), then

\[
N_R\ge N_{R-2}+5R-5
\qquad(R\ge5).
\]

For \(R=2s\ge6\), summing from scale \(6\) gives

\[
N_{2s}\ge N_4+\sum_{j=3}^s(10j-5)
=N_4+5s^2-20.
\]

For \(R=2s+1\ge5\), summing from scale \(5\) gives

\[
N_{2s+1}\ge N_3+\sum_{j=2}^s10j
=N_3+5s(s+1)-10.
\]

Since

\[
W_{2s}=3s^2+3s+1,
\qquad
W_{2s+1}=3(s+1)^2,
\]

this architecture obeys

\[
\liminf_{R\to\infty}\frac{N_R}{W_R}\ge\frac53
\]

and, more precisely,

\[
N_R-W_R\ge \frac12R^2-\frac32R+O(1).
\]

Thus the failure is quadratic after iteration, not a lower-order defect.

## 4. Every single translated core is excluded

The same injection completely classifies translations.  Let

\[
a=(a_1,a_2,a_3)\in\{0,1,2\}^3,
\qquad s=a_1+a_2+a_3,
\]

and suppose all letters of the contiguous core lie in

\[
B_{R,a}=a+[0,R-2]^3.
\]

Put \(d=|s-3|\).  For \(R\ge6\), Lemma 1.1 and one rank count give

\[
\boxed{
|P|+|S|
\ge (3+d)R-\frac{d(d+3)}2.
}
\]

Indeed, if \(s\le3\), use rank \(2R\).  The ambient count is
\(\binom{R+2}{2}\), while translation and complementation inside the
small cube give the core count

\[
\binom{R+s-4}{2}.
\]

Their difference is

\[
(6-s)R-\frac{(3-s)(6-s)}2
=(3+d)R-\frac{d(d+3)}2.
\]

If \(s\ge3\), use rank \(R\).  The ambient count is again
\(\binom{R+2}{2}\), while the core count is

\[
\binom{R-s+2}{2}.
\]

Their difference is

\[
sR+\frac{s(3-s)}2
=(3+d)R-\frac{d(d+3)}2.
\]

For \(s\ne3\), this is at least \(4R-2\).  If \(s=3\), then at least two
coordinates of \(a\) are positive, since each \(a_i\le2\).  Every core
letter is therefore positive in two fixed coordinates.  The exact
two-zero-face wedge bound gives

\[
|P|+|S|\ge4R-1.
\]

For completeness, the lower-bound mechanism for that wedge is short.  The
\(R\) pure pins on each of two axes and the \(R\) pure pins on the remaining
axis are forced.  For every fixed row on either of the first two axes,
designate the distinct remaining-coordinate providers in its \(R\)
witnesses.  If the minimum numbers of row roots on the two sides sum to at
least three, root counting already gives \(4R\).  Otherwise both minima are
one; for the two corresponding fixed roots, at most one provider can be
shared, because two shared providers would have to occur in opposite orders
when viewed from the two roots.  The two root-axis families plus the two
provider families then contain at least \(4R-1\) occurrences.  Deleting the
core and concatenating its core-free components preserves all these
zero-face witnesses, so the wedge bound applies to the outside word.

Consequently no recurrence retaining one contiguous translated copy of an
\((R-2)\)-cube can have the width increment \(3R+o(R)\).  The specific
one-coordinate shift is worse than the general minimum because its rank
center is displaced by two units from the ambient rank center, producing
the exact \(5R-5\) shell antichain.

For the low-total-shift cases relevant to the asymmetric lane, the
rank-\(2R\) ledger is especially transparent.  For \(s=0,1,2\), respectively,

\[
\begin{array}{c|c|c|c}
s&|B_{R,a}\cap\{|v|=2R\}|&
|(Q_R\setminus B_{R,a})\cap\{|v|=2R\}|&
\text{outside recurrence}\\ \hline
0&\binom{R-4}{2}&6R-9&N_R\ge N_{R-2}+6R-9\\[1mm]
1&\binom{R-3}{2}&5R-5&N_R\ge N_{R-2}+5R-5\\[1mm]
2&\binom{R-2}{2}&4R-2&N_R\ge N_{R-2}+4R-2.
\end{array}
\]

Using the exact width increment

\[
W_R-W_{R-2}=3R,
\]

and writing \(D_R=N_R-W_R\), these become the exact excess recurrences

\[
\begin{array}{c|c|c|c}
s&D_R-D_{R-2}\text{ is at least}&
N_R\text{ after iteration}&N_R-W_R\text{ after iteration}\\ \hline
0&3R-9&\frac64R^2+O(R)&\frac34R^2+O(R)\\[1mm]
1&2R-5&\frac54R^2+O(R)&\frac12R^2+O(R)\\[1mm]
2&R-2& R^2+O(R)&\frac14R^2+O(R).
\end{array}
\]

Equivalently, the corresponding limiting ratios to width are at least
\(2,5/3,4/3\).  Thus even the best one-positive-coordinate translation,
namely total shift \(s=2\), has a quadratic iterated excess.

## 5. The next exact statement

The single-factor recursive lane is exhausted.  A viable recurrence must
allow new shell letters to split the old letters into several physical
runs.  The exact next statement is the separator-safe two-shell splice:

\[
\boxed{
g_3(t+2)\le g_3(t)+3t+6+O(1),
}
\]

with the stronger literal requirement that, after deleting the two new
height levels, the remaining height-\(\le t\) runs collectively retain an
internal witness for every target of \(Q_t\).  This segmented-core condition
is essential.  It evades Lemma 1.1 because a boundary witness may then have
both endpoints among old letters while containing a new separator between
them.  Equivalently, one must now prove the separator-safe two-shell splice
from the equal-box structural report, or move to the three-shell/global
braid gates; another contiguous translated core cannot work.
