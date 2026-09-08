# Prime quotient fractional gate: exact two-loop mass with only polynomial deficiency

Date: 2026-07-26

## 0. Outcome

Let \(p=2m+1\) be prime, let \(Q=KG(p,m)/\mathbb Z_p\), and let

\[
        T={1\over p}{p\choose m}=C_m,\qquad
        D={m!(m+1)!\over2}.
\]

Let \(\mathscr Z\) be the hypergraph on \(V(Q)\) whose edges are the
vertex sets of simple zero-voltage quotient \(p\)-cycles.  These are
exactly the translation orbits of middle-transversal wreaths.

The exact fractional perfect-matching question remains unresolved.
However, the following unconditional statement is sharp enough to remove
every density-scale concern.

> **Theorem.**  Fix any two distinct AP loop vertices
> \(\ell_1,\ell_2\).  There are nonnegative cycle weights \(x_C\) and
> loop weights
>
> \[
>                 z_{\ell_1}=z_{\ell_2}=1
> \]
>
> such that every quotient vertex has total load at most one, the two
> selected loop vertices have load exactly one, and the total uncovered
> quotient mass is at most
>
> \[
>                 \boxed{p^2+p-2.}
> \tag{0.1}
> \]

Since \(T\) is exponential in \(p\), the relative deficiency is
\(e^{-\Theta(p)}\).  Thus:

* a fractional perfect matching is not obstructed at positive density;
* the exact Farkas question is an \(O(p^2)\)-mass absorption problem;
* translate-averaging becomes valid after the nontransversal rows are
  deleted, but it gives a nearfactor rather than an exact factor.

No argument below turns (0.1) into zero.  In particular, exact
fractional feasibility is not claimed.

## 1. Counting the nontransversal rows

Let \(\mathscr R\) be the set of geometric wreath rows, modulo rotation
and reversal.  Then

\[
       |\mathscr R|={(p-1)!\over2}=TD,
\tag{1.1}
\]

and every physical middle \(m\)-set lies in exactly \(D\) rows.

Call a row bad if two of its middle intervals lie in the same
translation necklace.  Let \(B_{\rm bad}\) be the number of bad rows.
For a fixed \(t\ne0\), count triples

\[
       (C,A,t),\qquad A,A+t\in C.
\]

If

\[
       d=|A\setminus(A+t)|,
\]

then the number of \(A\)'s with this value of \(d\) is

\[
       {p\over d}
       \binom{m-1}{d-1}\binom m{d-1},
\tag{1.2}
\]

while the number of rows through \(A,A+t\) is

\[
       D\,{2\over\binom md\binom{m+1}d}.
\tag{1.3}
\]

Consequently

\[
\begin{aligned}
 {1\over D}\sum_A
   \#\{C:A,A+t\in C\}
 &=\sum_{d=1}^m
   {p\over d}\binom{m-1}{d-1}\binom m{d-1}
   {2\over\binom md\binom{m+1}d}\\
 &=p.
\end{aligned}
\tag{1.4}
\]

Summing over the \(p-1\) nonzero translations gives

\[
                  \boxed{B_{\rm bad}\le p(p-1)D.}
\tag{1.5}
\]

The inequality rather than equality occurs because one bad row may
contain several collision triples.

Every good row has a free translation orbit of size \(p\), and that orbit
projects to one edge of \(\mathscr Z\).  Conversely every edge of
\(\mathscr Z\) arises this way.

## 2. The uniform good-cycle weighting

Give every edge of \(\mathscr Z\) weight

\[
                         x_C={1\over D}.
\tag{2.1}
\]

For a quotient vertex \(v\), choose one physical representative \(A\).
A good cycle through \(v\) has a unique translated row containing \(A\).
Therefore its load under (2.1) is

\[
                         \ell(v)={d_{\rm tr}(v)\over D}\le1,
\tag{2.2}
\]

where \(d_{\rm tr}(v)\) is the number of transversal rows containing
\(A\).

Summing degrees over quotient vertices counts every good cycle \(p\)
times, hence

\[
 \sum_{v\in V(Q)}d_{\rm tr}(v)
       =|\mathscr R|-B_{\rm bad}=TD-B_{\rm bad}.
\tag{2.3}
\]

It follows that the total uncovered quotient mass is exactly

\[
 \sum_v(1-\ell(v))
       ={B_{\rm bad}\over D}
       \le p(p-1).
\tag{2.4}
\]

This is a feasible fractional matching in the simple zero-voltage
cycle hypergraph.  It is important that only good rows appear.  Averaging
all row orbits would give exact loads but would also use multiset columns
coming from repeated quotient vertices, which are not selectable
zero-voltage cycles.

## 3. Installing exactly two loops

Fix two distinct AP loop vertices \(\ell_1,\ell_2\).  From the weighting
(2.1), delete every cycle meeting either selected vertex.  Then put unit
weight on the two loops.

The selected loop vertices now have load exactly one.  Every other
vertex has load at most its former load, hence at most one.  Thus the
result is a feasible fractional matching with exact loop mass two.

Let \(\mathscr S\) be the union of the deleted cycle sets.  Since the
total weight of cycles through either fixed vertex is at most one,

\[
                  \sum_{C\in\mathscr S}x_C\le2.
\tag{3.1}
\]

Every deleted cycle has \(p\) vertices, so deleting them removes at most
\(2p\) units of total vertex load.  Adding the two loops restores two
units.  Combining with (2.4), the final total deficiency is at most

\[
       {B_{\rm bad}\over D}+2p-2
       \le p(p-1)+2p-2
       =p^2+p-2.
\tag{3.2}
\]

This proves the theorem.

## 4. Consequence for the Farkas dual

The exact two-loop LP is

\[
\begin{aligned}
 \sum_{C\ni v}x_C+\sum_{L:v(L)=v}z_L&=1
                   &&(v\in V(Q)),\\
 \sum_Lz_L&=2,\\
 x_C,z_L&\ge0.
\end{aligned}
\tag{4.1}
\]

Its Farkas obstruction is a pair \((y,\alpha)\) such that

\[
 \sum_{v\in C}y_v\ge0\quad(C\in\mathscr Z),\qquad
 y_{v(L)}+\alpha\ge0\quad(L\in\mathscr L),
\tag{4.2}
\]

but

\[
                    \sum_vy_v+2\alpha<0.
\tag{4.3}
\]

The construction above shows that any such obstruction is invisible
outside a deficiency vector of total mass at most \(p^2+p-2\).  More
explicitly, if the dual is normalized by \(y_v\ge-1\), multiplying
(4.2) by the nearfactor weights gives

\[
             \sum_v y_v+2\alpha\ge-(p^2+p-2).
\tag{4.4}
\]

Thus no dual certificate can obtain a macroscopic negative margin.  This
does not rule out a zero-margin separating face, and precisely that
boundary phenomenon is the remaining issue.

## 5. Exact remaining lemma

To settle fractional feasibility it is enough to prove a fractional
absorber of polynomial size:

> Every feasible simple-cycle weighting with total deficiency
> \(O(p^2)\), and with two prescribed AP loops installed, can be altered
> within the simple zero-voltage catalogue so as to eliminate the
> deficiency.

Equivalently, one must show that the uniform demand vector with the two
loop coordinates removed lies in the cycle-incidence cone, not merely
within \(O(p^2)\) in \(\ell_1\)-distance from it.

Regular quotient-edge circulations do not prove this: their cycle
decompositions may have the wrong lengths or nonzero voltages.  Likewise,
the exact full-row average does not prove it, because its bad row-orbit
columns repeat quotient vertices.  The missing input is a genuinely
simple zero-voltage fractional absorber.
