# Two consecutive rectangle sizes admit an exact capacity-feasible upper-current table

**Date:** 2026-08-07  
**Input:**
`MATH_THEOREM_MIXED_CORE_FORWARD_RECTANGLE_GLOBAL_UPPER_CURRENT_OBSTRUCTION_20260807.md`  
**Method:** explicit Diophantine decomposition of the center currents  
**Status:** theorem at the global incidence-table level.  It proves that
the fixed-size upper-current obstruction disappears already for two
consecutive sizes, including all global shore counts and the one-copy
owner-slot inequality.  It does not construct the rectangles geometrically
and does not cancel their proper-target currents.

## 1. Currents and incidence totals

Work in the complemented owner layer on

\[
                         n=2r-1.
\]

Assume both rectangle sizes are geometrically admissible, in particular

\[
                         D+1\le p,
 \qquad                  2(p+1)\le r+1.
\tag{1.0}
\]

A forward rectangle of size \(q\) has:

* \(q\) positive \(A\)-centres, each with current \(q+1\) and owner
  load \(q+1\);
* \(q+1\) negative \(B\)-centres, each with current \(-q\) and owner
  load \(q\).

For a fixed rank-\((r-2)\) centre \(G\), write

\[
 a_q(G),\qquad b_q(G)
\]

for the numbers of size-\(q\) positive and negative incidences at \(G\).
Its current and load are

\[
 u_G=\sum_q\bigl((q+1)a_q(G)-q b_q(G)\bigr),
\tag{1.1}
\]

\[
 \ell_G=\sum_q\bigl((q+1)a_q(G)+q b_q(G)\bigr).
\tag{1.2}
\]

An owner-disjoint geometric realization must satisfy

\[
                         \ell_G\le r+1.
\tag{1.3}
\]

The fixed-size theorem proves that, for \(2q(q+1)>r+1\), no nonzero
zero-current table exists using only size \(q\).  We now give an exact
table using sizes \(p\) and \(p+1\).

## 2. Two zero-current centre types

Put

\[
 c=\left\lfloor{p\over2}\right\rfloor,
 \qquad
 b=p+1-c.
\tag{2.1}
\]

Define two centre types.  Their coordinates are ordered as

\[
 (a_p,b_p,a_{p+1},b_{p+1}).
\]

The **cross type** is

\[
                         X=(1,0,0,1).
\tag{2.2}
\]

Its current is

\[
                         (p+1)-(p+1)=0
\]

and its owner load is

\[
                         \ell_X=2(p+1).
\tag{2.3}
\]

The **bulk type** is

\[
                         Y=(p-2c,b,c,0).
\tag{2.4}
\]

Its current is

\[
 \begin{aligned}
 u_Y
  &=(p+1)(p-2c)-pb+(p+2)c\\
  &=(p+1)(p-2c)-p(p+1-c)+(p+2)c\\
  &=0,
 \end{aligned}
\tag{2.5}
\]

and therefore its load is twice either shore mass:

\[
                         \ell_Y=2pb.
\tag{2.6}
\]

Explicitly,

\[
 \ell_Y=
 \begin{cases}
 p^2+2p,&p\text{ even},\\
 p^2+3p,&p\text{ odd}.
 \end{cases}
\tag{2.7}
\]

## 3. Exact global shore balance

Take formally

\[
 H_p=b=p+1-c
\tag{3.1}
\]

forward rectangles of size \(p\), and

\[
 H_{p+1}=c
\tag{3.2}
\]

forward rectangles of size \(p+1\).

Their required global incidence counts are

\[
 \begin{array}{c|cccc}
  &a_p&b_p&a_{p+1}&b_{p+1}\\ \hline
 \text{required}
  &pH_p&(p+1)H_p&(p+1)H_{p+1}&(p+2)H_{p+1}.
 \end{array}
\tag{3.3}

### Theorem 3.1 (exact consecutive-size current table)

The multiset consisting of

\[
                         p+1
\tag{3.4}

centres of type \(Y\) and

\[
                         c(p+2)
\tag{3.5}

centres of type \(X\) has exactly the incidence totals (3.3).  Every
centre has zero immediate-upper current.

#### Proof

For the negative size-\(p\) incidences, the \(Y\)-centres supply

\[
                         (p+1)b=(p+1)H_p.
\]

For the positive size-\((p+1)\) incidences, they supply

\[
                         (p+1)c=(p+1)H_{p+1}.
\]

The cross centres supply all

\[
                         c(p+2)=(p+2)H_{p+1}
\]

negative size-\((p+1)\) incidences.  Finally, the total positive
size-\(p\) supply is

\[
 \begin{aligned}
 &(p+1)(p-2c)+c(p+2)\\
 &\qquad=p(p+1-c)=pH_p.
 \end{aligned}
\]

Thus every entry of (3.3) is exact.  Equations (2.3) and (2.5) prove
pointwise zero current. \(\square\)

The table represents

\[
                         H_p+H_{p+1}=p+1
\tag{3.6}

formal forward component reductions.  There is no inverse trade and no
unbalanced boundary size.

## 4. The owner-slot bound is compatible

### Corollary 4.1 (one-copy capacity feasibility)

If

\[
                         2p\bigl(p+1-\lfloor p/2\rfloor\bigr)
                         \le r+1,
\tag{4.1}

then every centre of the table satisfies the necessary one-copy owner
bound \(\ell_G\le r+1\).

In the optimal triangular range, take any

\[
                         p=d+O(1).
\]

Since

\[
                         d^2\sim {\pi\over4}r,
\]

we have

\[
 \ell_Y=p^2+O(p)=\left({\pi\over4}+o(1)\right)r<r+1.
\tag{4.2}

Hence (4.1) holds for all sufficiently large parameters.  Meanwhile each
fixed size separately lies in the negative regime

\[
                         2p(p+1)>r+1.
\]

Thus mixing just two consecutive sizes changes the arithmetic answer:
the exact global incidence totals, pointwise upper-current equations, and
local owner-slot capacities are simultaneously compatible.

#### Proof

The larger load is \(\ell_Y=2pb\); equation (4.1) is exactly
\(\ell_Y\le r+1\).  Equation (4.2) follows from (2.7). \(\square\)

## 5. What the table does and does not prove

The theorem closes the **arithmetic** objection to a mixed-size escape.
It is stronger than observing one cancelling pair: it accounts exactly for
all four shore-incidence totals of a finite bank of forward rectangles.

It does not yet prove the existence of labelled rectangles realizing the
table.  Such a realization must simultaneously:

1. group the prescribed centre incidences into \(b\) complete
   \(K_{p,p+1}\) rectangles and \(c\) complete
   \(K_{p+1,p+2}\) rectangles;
2. assign different rank-\((r-1)\) owner supersets at every centre and
   globally avoid owner reuse;
3. cancel or transport the proper-target currents at all
   \(1\le q<D\); and
4. respect the literal cyclic orders and any protected external rows.

The theorem therefore supplies an exact target for the next construction:

> **Consecutive-size geometric circulation.**  Realize the \(X/Y\) table
> above by an owner-disjoint labelled rectangle bank, then solve its
> proper-target current.

The fixed-size no-go remains valid.  What is now proved is that its global
centre-count argument cannot be extended to two consecutive sizes: there
is an explicit capacity-feasible integral null current of that mixed-size
incidence system.
