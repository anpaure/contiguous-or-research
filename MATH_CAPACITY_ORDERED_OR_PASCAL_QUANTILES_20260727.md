# Capacity-ordered OR--Pascal tableaux: the exact arithmetic

Date: 2026-07-27

## 1. Purpose

The finite exact words suggest that the rows below the central row of the
OR--Pascal tableau are ordered by rank.  The literal finite pattern

\[
D^0A:\ |S|\le r-d,\qquad D^jA:\ |S|=r-d+j
\]

cannot persist asymptotically: row zero has only \((1+o(1))W\) cells, while
the number of masks of ranks at most \(r-d\) is \(\Theta(\sqrt{k}W)\).

This note gives the corrected statement.  The capacities do not determine
one rank boundary.  They determine an exact **quantile polytope**, with the
usual rank-slack as its total amount of waste.  This distinction matters:
there is no further rank-count obstruction once a rank is allowed to split
at a row boundary.

## 2. Parameters and row capacities

Put

\[
r=\lceil k/2\rceil,\qquad W=\binom kr,\qquad
L=\sum_{s=1}^{r-1}\binom ks.
\]

Let \(d\) be least such that

\[
L\le S_d:=dW+\binom{d+1}{2},
\]

and put

\[
n=W+d=B(k),\qquad e=S_d-L.
\tag{2.1}
\]

The rows strictly below \(D^dA\) have capacities

\[
c_j=n-j=W+d-j\qquad(0\le j<d),
\tag{2.2}
\]

and indeed

\[
\sum_{j=0}^{d-1}c_j=S_d=L+e.
\tag{2.3}
\]

Minimality of \(d\) gives the useful sharp inequality

\[
0\le e<W+d=c_0,
\tag{2.4}
\]

because \(S_d-S_{d-1}=W+d\).

## 3. First-witness counts and the slack path

For a word \(A=(A_0,\ldots,A_{n-1})\), write

\[
X_{j,i}=A_i\cup\cdots\cup A_{i+j}.
\]

Suppose every nonempty mask of rank below \(r\) has a first witness in one
of the rows \(0,\ldots,d-1\).  Let

\[
u_j=\#\{S:1\le |S|<r,\ \min\{h:S=X_{h,i}\text{ for some }i\}=j\}.
\]

Then necessarily

\[
0\le u_j\le c_j,qquad \sum_{j=0}^{d-1}u_j=L.
\tag{3.1}
\]

Define the row waste and cumulative waste by

\[
\delta_j=c_j-u_j,\qquad Z_j=\sum_{h=0}^j\delta_h.
\]

Then

\[
\delta_j\ge0,qquad Z_{d-1}=e.
\tag{3.2}
\]

Thus the rank-slack \(e\) has a literal cell-by-cell meaning: it is exactly
the number of cells in the first \(d\) rows which are not first witnesses
for lower masks.  Such a cell may be a repeated lower mask or an early
central mask.  If no high mask occurs below the central row, these are the
only two possibilities.

Conversely, (3.1) is the complete *arithmetic* condition.  Given any
integers \(u_j\) satisfying (3.1), order the \(L\) lower masks by
nondecreasing rank and assign the first \(u_0\) to row zero, the next
\(u_1\) to row one, and so on.  This produces an abstract rank-monotone
first-witness schedule.  Whether it can be realized by the OR recurrence is
the geometric problem; rank counts add no further condition.

There is a useful geometric simplification once the central row is fixed.
For \(0\le j<d\) and \(0\le i<W\),

\[
X_{j,i}\subseteq X_{d,i}.
\tag{3.3}
\]

Hence if \(D^dA\) consists of rank-\(r\) sets, all \(dW\) cells in these
aligned columns automatically have rank at most \(r\).  The only cells
below the central row which can be prematurely upper are the right boundary
staircase

\[
W\le i<W+d-j,
\]

whose total size is exactly \(\binom{d+1}{2}\).  Thus the no-upper-waste
condition is a boundary condition, not a bulk condition.

## 4. The exact rank-quantile envelope

Put

\[
Q_j=\sum_{h=0}^jc_h,qquad U_j=\sum_{h=0}^ju_h.
\]

Then

\[
U_j=Q_j-Z_j
\]

and therefore every schedule satisfies the sharp prefix bounds

\[
\boxed{
Q_j-e\le U_j\le\min\{Q_j,L\}
}\qquad(0\le j<d).
\tag{4.1}
\]

Both envelopes are attainable abstractly.  The lower envelope is attained
by placing all waste in row zero:

\[
\delta_0=e,qquad \delta_j=0\ (j\ge1).
\tag{4.2}
\]

This is legal by (2.4).  It is the unique schedule which postpones every
prefix as far as all remaining capacities permit.  Equivalently, if
\(t=d-1-j\), then

\[
\boxed{
U_{d-1-t}=L-tW-\binom{t+1}{2}
}\qquad(0\le t<d).
\tag{4.3}
\]

The upper envelope is obtained by filling the early rows with new masks
until the lower ideal is exhausted and placing the waste after that point.

For the rank interpretation, let

\[
F_s=\sum_{a=1}^s\binom ka,\qquad F_0=0.
\]

For every \(U_j>0\), let

\[
b_j=\min\{s:F_s\ge U_j\},\qquad
\alpha_j=U_j-F_{b_j-1}.
\tag{4.4}
\]

Rank monotonicity says precisely that the masks completed by row \(j\)
are

* every mask of ranks below \(b_j\), and
* exactly \(\alpha_j\) of the \(\binom{k}{b_j}\) masks of rank \(b_j\).

Thus each row is a genuine binomial-rank quantile.  A row may contain a
suffix of the rank cut by its left boundary, some complete intervening
ranks, and a prefix of the rank cut by its right boundary.  In particular,
**at each row boundary at most one rank is split**.

The full parametrization is also exact.  Capacity-ordered schedules are in
bijection with integer slack paths

\[
Z_{-1}=0,\qquad 0\le Z_j-Z_{j-1}\le c_j,qquad Z_{d-1}=e,
\tag{4.5}
\]

via \(U_j=Q_j-Z_j\).  There is no distinguished quantile unless an extra
normalization is imposed.

### 4.1 Asymptotic location of the deferred quantiles

Formula (4.3) also explains exactly why the finite one-rank-per-row clock
eventually fails.  Let \(s_t\) be the rank cut determined by
\(U_{d-1-t}\), and write \(\Phi\) for the standard normal distribution
function.  Uniformly on fixed Gaussian scales, the binomial CLT gives

\[
s_t=\frac{k}{2}+\frac{\sqrt{k}}2\,
 \Phi^{-1}(p_t)+o(\sqrt{k}),
\tag{4.6}
\]

where, for \(t=O(\sqrt{k})\),

\[
p_t=
\begin{cases}
\displaystyle \frac12-t\sqrt{\frac{2}{\pi k}}+o(1),&k\text{ odd},\\[2mm]
\displaystyle \frac12-(t+\frac12)\sqrt{\frac{2}{\pi k}}+o(1),&k\text{ even}.
\end{cases}
\tag{4.7}
\]

For \(t=o(\sqrt{k})\), expansion of \(\Phi^{-1}\) at \(1/2\) gives a
rank displacement of approximately \(t\).  This is why the last few short
rows in the finite words look like one complete rank per row.

At the opposite end, \(t=d-1\), the leading half-cube mass has been almost
entirely subtracted.  Row zero contains only \(c_0-e\le W+d\) new masks.
When this quantity is of order \(W\), its terminal rank is therefore at
binomial tail probability \(\Theta(k^{-1/2})\), hence at distance

\[
\Theta(\sqrt{k\log k})
\]

below the middle.  Thus the first row must collect a long outer-tail block,
not all ranks through \(r-d\).  The quantile schedule interpolates between
this moderate-deviation tail and the nearly one-rank central rows.

## 5. The finite exact words inside the polytope

For the rank-exact representatives, the numbers of new lower masks in the
short rows are as follows.

| \(k\) | \(d\) | \((u_0,\ldots,u_{d-1})\) | \((\delta_0,\ldots,\delta_{d-1})\) |
|---:|---:|---:|---:|
| 6 | 1 | \((21)\) | \((0)\) |
| 7 | 2 | \((28,35)\) | \((9,1)\) |
| 8 | 2 | \((36,56)\) | \((36,15)\) |
| 9 | 2 | \((128,127)\) | \((0,0)\) |
| 10 | 2 | \((175,210)\) | \((79,43)\) |
| 11 (near) | 3 | \((231,330,462)\) | \((234,134,1)\) |
| 12 | 2 | \((793,792)\) | \((133,133)\) |

The waste vectors sum respectively to the exact arithmetic slack \(e\).
Except at \(k=9\), these examples choose interior points of the quantile
polytope which align row boundaries with complete binomial ranks.  They do
not choose the extremal schedule (4.3).  Consequently, (4.3) should be used
as an arithmetic normal form, not asserted as a property of the known
words.

## 6. Whole-rank bands really do have new obstructions

If ranks may split at row boundaries, (3.1)--(4.5) show that the sole
rank-count condition is \(S_d\ge L\), exactly the definition of \(d\).

If one strengthens the target by forbidding split ranks, a new arithmetic
obstruction appears.  A no-split boundary after row \(j\) must be a value
\(F_s\), and hence must satisfy

\[
Q_j-e\le F_s\le\min\{Q_j,L\}.
\tag{6.1}
\]

For several boundaries one must additionally have

\[
0\le F_{s_j}-F_{s_{j-1}}\le c_j.
\tag{6.2}
\]

The familiar first failure is \(k=9\), where \(e=0\) and row zero has
capacity \(128\), while

\[
F_2=45<128<F_3=129.
\]

Thus rank three is forced to split \(83+1\), exactly as in the stored
optimum.

The next useful warning is \(k=14\).  Here

\[
r=7,\quad W=3432,\quad d=2,\quad L=6475,\quad e=392,
\]

and the two capacities are \(3434,3433\).  The relevant cumulative counts
are

\[
F_4=1470,qquad F_5=3472,qquad F_6=6475.
\]

Every admissible boundary satisfies

\[
3042=L-3433\le U_0\le3434.
\]

There is no cumulative rank count in this interval.  Hence every
capacity-ordered schedule at \(k=14\) must split rank five.  More precisely,
row zero must receive between

\[
3042-1470=1572
\quad\hbox{and}\quad
3434-1470=1964
\]

of the \(2002\) rank-five masks.

Therefore a theorem phrased as "each short row is a union of complete
ranks" is false for arithmetic reasons.  The quantile formulation is not a
technical relaxation; it is the sharp one.

## 7. A correct structural target for \(\nu(k)=B(k)\)

Call a word \(A=(A_0,\ldots,A_{W+d-1})\) a **capacity-ordered optimal
tableau** if it has the following properties.

1. **Central factor:** \(D^dA\) is a permutation of
   \(\binom{[k]}r\).
2. **Lower completion:** every nonempty mask of rank below \(r\) has a
   first witness in a row \(j<d\).
3. **Capacity ordering:** if \(|S|<|T|<r\), then the first-witness depth of
   \(S\) is at most that of \(T\).  Equivalently, the lower first witnesses
   follow one of the quantile schedules (4.5).
4. **No premature upper masks:** every cell in a row \(j<d\) has rank at
   most \(r\).  Consequently the \(e\) non-first-witness cells are exactly
   repeated lower masks or early central masks.
5. **Upper completion:** the cells in rows \(j>d\) cover every mask of rank
   above \(r\).

### Capacity-ordered tableau theorem (sufficient target)

If a capacity-ordered optimal tableau exists for every \(k\), then

\[
\nu(k)=B(k)\qquad\hbox{for every }k.
\]

Indeed, properties 1, 2, and 5 cover all nonempty masks in a word of length
\(W+d=B(k)\), while the rank-slack lower bound gives the reverse inequality.

This is a substantive normal-form theorem, but one logical warning is
essential.  At present it is a **sufficient strengthening** of
\(\nu(k)=B(k)\), not a proved equivalent reformulation: no theorem says that
an arbitrary optimal word can be converted into one with a central
permutation and rank-monotone first witnesses.  Within the class of words
admitting that normalization, Sections 3--4 give the exact equivalence and
all arithmetic constraints.

If a literally equivalent statement is desired, one must drop the
normal-form clauses and merely ask for a length-\(B(k)\) OR--Pascal tableau
covering every mask; that is tautological and loses the structural content.

## 8. Conclusion

The corrected general picture is:

\[
\boxed{
\text{rank-slack }e
=\text{ total short-row waste},\qquad
\text{row boundaries }=\text{ binomial rank quantiles}.
}
\]

There is no new rank-count obstruction to the capacity-ordered theorem.
All remaining difficulty is OR--Pascal compatibility: realizing the chosen
quantile schedule simultaneously down the diagonals and across neighboring
columns, while completing the upper tower.  Whole-rank row formulations do
have genuine arithmetic obstructions and should be retired in favor of the
split-quantile statement.
