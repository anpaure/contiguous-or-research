# The two-period centre character forces a sharp linear-size near-C atom

**Date:** 2026-08-14
**Status:** unconditional sharp algebraic obstruction and finite-design
reduction.  It applies to genuine positive trades, but does not assert that
the extremal centre profile has a cyclic-window realization.

## 1. Setup

Fix \(q\ge2\), a common \((c-1)\)-set \(C_0\), and reduced labels \(V\).
For \(z\in V\), a distance-one core is \(K_z=C_0\cup\{z\}\).  A rail
centred at \(z\), of period \(N\), has owners

\[
 C_0\cup\{z\}\cup I_i^q(\sigma),\qquad i\in\mathbb Z_N,
\]

where \(\sigma\) is a cyclic word of \(N\) distinct labels avoiding \(z\).
Use only the two shortest legal periods

\[
 n=2q+2,\qquad n+1=2q+3.                         \tag{1.1}
\]

Let \(\mathcal A^+,\mathcal A^-\) be simple collections of the same number of
such rails and suppose their complete named-owner vectors obey

\[
 \sum_{Q\in{\cal A}^+}f(Q)-
 \sum_{Q\in{\cal A}^-}f(Q)=e_H,                  \tag{1.2}
\]

where \(H=C_0\cup H_0\) and \(|H_0|=q+1\).

For \(z\in V\), let \(a_z\) be the positive-minus-negative number of
period-\(n\) rails centred at \(z\), and let \(b_z\) be the corresponding
number of period-\((n+1)\) rails.

## 2. Exact centre equations

### Lemma 2.1

Every trade (1.2) satisfies

\[
 \boxed{2a_z+3b_z\equiv \mathbf 1_{H_0}(z)\pmod q}  \tag{2.1}
\]

for every reduced label \(z\), and

\[
 \boxed{\sum_za_z=-1,\qquad\sum_zb_z=1.}         \tag{2.2}
\]

#### Proof

A period-\(N\) rail centred at \(z\) contains \(z\) in every one of its
\(N\) owners.  Every toggle label occurs in exactly \(q\) cyclic
\(q\)-windows.  Taking the reduced point degree at \(z\) modulo \(q\)
therefore gives

\[
 na_z+(n+1)b_z\equiv\mathbf 1_{H_0}(z)\pmod q.
\]

Since \(n\equiv2\) and \(n+1\equiv3\pmod q\), this is (2.1).

Equal rail counts give

\[
 \sum_z(a_z+b_z)=0.
\]

Taking total owner counts in (1.2) gives

\[
 n\sum_za_z+(n+1)\sum_zb_z=1.
\]

Subtracting \(n\) times the first equation yields \(\sum_zb_z=1\), and
then \(\sum_za_z=-1\). \(\square\)

This corrects a tempting but false simplification: for general \(q\), one
cannot discard the long-centre variable \(b_z\) and write
\(a_z\equiv-1\pmod q\).

## 3. Sharp minimum number of rails per shore

Put

\[
 s_q=
 \begin{cases}
 q,&2\le q\le4,\\
 \left\lfloor(4q+1)/3\right\rfloor,&q\ge5.
 \end{cases}                                      \tag{3.1}
\]

### Theorem 3.1 (sharp centre-character minimum)

Every trade (1.2) has at least \(s_q\) rails on each shore.  This bound is
sharp at the level of the integer centre equations (2.1)--(2.2), even when
arbitrarily many exterior labels \(z\notin H_0\) are allowed.

#### Proof: reduction to an \(\ell^1\) problem

The positive and negative masses of the net centre ledger represented by
\((a_z,b_z)\) are respectively

\[
 P=\sum_z(a_z^++b_z^+),\qquad
 N=\sum_z(a_z^-+b_z^-).
\]

Equations (2.2) imply \(P-N=\sum_z(a_z+b_z)=0\).  Hence

\[
 P=N=\frac12\sum_z(|a_z|+|b_z|).                 \tag{3.2}
\]

Each physical shore has size at least this common value.  Equality holds
if and only if no centre/period class occurs on both shores; cancelling
identical rails preserves the trade but need not remove all aggregate
cancellation between different cyclic orders in one class.

It remains to minimize the right side subject to (2.1)--(2.2).

For \(h\in\{0,1\}\), define the residue set

\[
 \Lambda_h(q)=\{(a,b)\in\mathbb Z^2:
                 2a+3b\equiv h\pmod q\}.         \tag{3.3}
\]

For every \(q\), the following supporting-plane inequality holds for all
\(h\in\{0,1\}\) and all \((a,b)\in\Lambda_h(q)\):

\[
 \gamma_qh+x_qa+y_qb\le |a|+|b|.                \tag{3.4}
\]

For \(q=2,3,4\), take respectively

\[
 (\gamma_q,x_q,y_q)=
 (1,-1,0),\quad(4/3,1/3,1),\quad(3/2,0,1/2).
                                                               \tag{3.5}
\]

For \(q\ge5\), take

\[
\begin{array}{c|ccc}
q\bmod3&\gamma_q&x_q&y_q\\ \hline
0&(8q-6)/(3q)&(12-q)/(3q)&(6-q)/q\\
1&(8q-8)/(3q)&(16-q)/(3q)&(8-q)/q\\
2&(8q-4)/(3q)&(8-q)/(3q)&(4-q)/q.
\end{array}                                                    \tag{3.6}
\]

Here is a uniform verification of (3.4), including the exterior residue
class.  First suppose `q>=5`, put

\[
                         2a+3b=h+qk,                \tag{3.4a}
\]

and set

\[
                         L(a,b)=3(|a|+|b|)+a+3b.    \tag{3.4b}
\]

After multiplying (3.4) by `3q` and substituting (3.4a), the three rows of
(3.6) reduce exactly to

\[
 L(a,b)\ge
 \begin{cases}
 6k+8h,&q\equiv0\pmod3,\\
 8k+8h,&q\equiv1\pmod3,\\
 4k+8h,&q\equiv2\pmod3.
 \end{cases}                                      \tag{3.4c}
\]

Write the coefficient of `k` in these three cases as `c=6,8,4`.  If
`a,b>=0`, then `L=2(h+qk)`.  If exactly one coordinate is negative and its
absolute value is `t`, then

\[
                         L=2(h+qk)+6t.              \tag{3.4d}
\]

In the nonnegative quadrant, `h=1` forces `k>=1` (the equation `2a+3b=1`
has no nonnegative solution), and (3.4c) follows because

\[
                         2q-c\ge6.                  \tag{3.4e}
\]

In a mixed quadrant with `k>=0`, the negative coordinate has `t>=1`, so
(3.4d) supplies the missing six.  For `h=0,k<0` or `h=1,k<=-2`, the right
side of (3.4c) is nonpositive and the claim is automatic.  At the only
remaining mixed boundary `h=1,k=-1`, the `c=8` row is again automatic.
For `c=6` or `c=4`, the required bound is respectively `L>=2` or `L>=4`.
If the negative coordinate is `b`, then `L=4a`.  The choice `a=0` would
give `q=3|b|+1`, contradicting `q\equiv0,2\pmod3`; hence `a>=1`.  If the
negative coordinate is `a`, then `L=2|a|+6b`; the only possibility below
four is `(|a|,b)=(1,0)`, which forces `q=3`.

If both coordinates are negative, then `L=2|a|`.  For `h=0` the right side
of (3.4c) is negative; for `h=1,k<=-2` it is nonpositive.  At the remaining
boundary `h=1,k=-1`, the `c=8` right side is zero, the `c=6` row requires
only `|a|>=1`, and the only exceptional-looking case is

\[
 q\equiv2\pmod3,qquad h=1,qquad k=-1.             \tag{3.4f}
\]

In that case `2|a|+3|b|=q-1`.  The choice `|a|=1` would give
`q-1\equiv2\pmod3`, contrary to `q\equiv2\pmod3`;
hence `|a|>=2` and `L>=4`, as required.  This proves (3.4c) in all four
orthants.

For `q=2`, (3.4) is

\[
                         h-a\le|a|+|b|.             \tag{3.4g}
\]

It is immediate for `h=0`; for `h=1`, the congruence forces `b` odd, which
settles the only cases `a<=0`.  For `q=3`, the required slack is

\[
          3|a|-a+3|b|-3b\ge4h.                    \tag{3.4h}
\]

When `h=1`, the congruence gives `a\equiv-1\pmod3`, and therefore
`3|a|-a>=4`; this proves (3.4h).  Finally, for `q=4` the slack is

\[
                         2|a|+2|b|-b\ge3h.          \tag{3.4i}
\]

For `h=1`, a negative `b` already contributes at least three.  If `b>=3`,
the claim is also immediate.  The cases `b=0` and `b=2` are impossible;
if `b=1`, the congruence forces `a` odd, supplying the remaining two beyond
the single `b` contribution.
This proves (3.4) for every `q>=2` and both `h=0,1`.  In particular,
arbitrary exterior `h=0` centres cannot improve the bound.

Sum (3.4) over \(q+1\) coordinates with \(h=1\) and all remaining
coordinates with \(h=0\).  Use (2.2) to get

\[
 \sum_z(|a_z|+|b_z|)
 \ge(q+1)\gamma_q-x_q+y_q=2s_q.                 \tag{3.7}
\]

Equation (3.2) proves the lower bound.

For sharpness, the following profiles use only the \(q+1\) labels of
\(H_0\), satisfy (2.1)--(2.2), and have \(\ell^1\)-norm \(2s_q\).
For \(q\ge5\), write \(q=3r,3r+1,3r+2\):

\[
\begin{array}{c|l}
q=3r&
2r\times(-1,1),\ r\times(2,-1),\ 1\times(-1,-(r-1))\\
q=3r+1&
(2r+1)\times(-1,1),\ r\times(2,-1),\ 1\times(0,-r)\\
q=3r+2&
(2r+1)\times(-1,1),\ (r+1)\times(2,-1),\
1\times(-2,-(r-1)).
\end{array}                                                    \tag{3.8}
\]

For the exceptional values \(q=2,3,4\), one may use

\[
\begin{array}{c|l}
2&2\times(0,1),\ 1\times(-1,-1),\\
3&3\times(-1,0),\ 1\times(2,1),\\
4&2\times(-1,1),\ 2\times(0,-1),\ 1\times(1,1).
\end{array}                                                    \tag{3.9}
\]

Direct summation verifies all assertions. \(\square\)

## 4. The exact next finite atom

The theorem identifies the smallest possible two-period reserve catalogue:
choose one of the extremal profiles (3.8)--(3.9), split every positive
entry into that many actual rails on the positive shore and every negative
entry into its absolute number on the negative shore, and seek cyclic
orders such that

\[
 \boxed{
 \mathcal D(\mathcal A^+)=
 \mathcal D(\mathcal A^-)\mathbin{\dot\cup}\{H\}.}  \tag{4.1}
\]

Both decks must be simple.  This is a finite \(q\)-dependent exact-cover
problem on centred cyclic \(q\)-window decks.  Any solution uses exactly
\(s_q=\Theta(q)\) rails per shore; no smaller atom using only periods
\(2q+2,2q+3\) exists, regardless of how many exterior centres are offered.

At \(q=3\), (3.9) gives the first unresolved primitive atom:

\[
 \begin{array}{c|c}
 \text{positive}&2\text{ period-8 rails at one }H_0\text{ centre}
                   +1\text{ period-9 rail there},\\
 \text{negative}&1\text{ period-8 rail at each of the other three }
                   H_0\text{ centres}.
 \end{array}                                                    \tag{4.2}
\]

Thus it is a three-by-three atom, not the previously tested five-by-six
puncture profile.

## 5. Factor and residence integration

A solution of (4.1) lifts to the original owner layer by adjoining the
common set \(C_0\); every nonoriginal core is exactly the distance-one
bridge \(C-a+z\).  Period legality is automatic from (1.1).

For use as a common reserve for a pre-existing macro, one still must choose
the reduced label embedding and cyclic orders so that the collateral deck
\(\mathcal D(\mathcal A^-)\) avoids both compulsory shores.  Translation or
orbit development of a local atom does not by itself solve that condition:
developing the distinguished owner also creates multiple translates of
\(H\), while (1.2) requires exactly one named owner.  Accordingly the
integration-safe next theorem must be a **rooted local design with a
forbidden-owner avoidance parameter**, not merely a global factor of all
reduced owners.

The centre character is compatible with global overlapping-core role flow:
it concerns only the local signed reserve, whereas the global role theorem
balances aggregate core/toggle degrees.  It does not solve the remaining
global cyclic-order equations, owner-factor residence, upper-ticket
preservation, or terminal opening.

## 6. Scope

This theorem is an obstruction and exact algebraic reduction.  The profiles
(3.8)--(3.9) are integer centre ledgers, not positive rail decompositions.
No signed lattice identity is claimed as a nonnegative common reserve.  The
open constructive row is precisely the simple cyclic-window realization
(4.1), first at the \(q=3\) three-by-three atom.
