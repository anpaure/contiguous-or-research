# Fractional realizability audit for the explicit \(k=11\) cap-two design

Date: 2026-07-27

## 0. Outcome

Let \({\cal D}_4\subseteq\binom{\mathbb Z_{11}}4\) be the twelve-orbit
design in `K11_EXPLICIT_CYCLIC_CAPTWO_EXCESS_DESIGN_20260727.md`, and let

\[
 {\cal E}_7=\{\mathbb Z_{11}\setminus R:R\in{\cal D}_4\}.
\]

There is an explicit, translation-equivariant **signed** solution of all
lower, middle, and prescribed upper equations.  It is obtained by a
three-component Johnson-harmonic lifting, whose coefficients are given
below.

The degree-two component of this signed solution is automatically
nonnegative after adding the uniform background.  Thus the point and pair
data cause no positivity problem.  The unresolved issue is positivity of
the degree-three and degree-four components.

The first higher subset-moment inequality is a triple inequality.  The
explicit design satisfies it with margin at least eight.  On the other hand,
the design has a five-set containing no selected four-block; this refutes a
particularly natural positive decomposition, but not general fractional
feasibility.

## 1. Johnson-edge formulation

Write

\[
 w(A)=1+\mathbf1_{{\cal E}_7}(A)
 \qquad(A\in\tbinom{[11]}7).
\]

A diamond \(X\subset A\), with \(|X|=5,|A|=7\), is the edge between the
two six-sets

\[
 Y=X+a,\qquad Z=X+b,qquad A=X+a+b.
\]

Thus fractional realizability is exactly a nonnegative weighting
\(x_{X,A}\) of the edges of \(J(11,6)\) such that

\[
\begin{aligned}
 \sum_{A\supset X}x_{X,A}&=1 &&(|X|=5),\\
 \sum_{X\subset Y\subset A}x_{X,A}&=2 &&(|Y|=6),\\
 \sum_{X\subset A}x_{X,A}&=w(A) &&(|A|=7).
\end{aligned}                                           \tag{1.1}
\]

The first and third sums are the weights of the lower and upper Johnson
cliques; the middle equation is weighted degree two.

The constant weighting

\[
 x^0_{X,A}=\frac1{15}                                  \tag{1.2}
\]

has lower sums one, middle sums two, and upper sums \(21/15=7/5\).
Put

\[
 g(A)=w(A)-\frac75=\mathbf1_{{\cal E}_7}(A)-\frac25.
\]

The size and point-degree identities for \({\cal E}_7\) give

\[
 \sum_Ag(A)=0,\qquad \sum_{A\ni i}g(A)=0.              \tag{1.3}
\]

Hence \(g\), as a function on the seven-slice, has only Johnson harmonic
degrees \(j=2,3,4\).

## 2. An explicit signed lift

Let \(\phi_j\) be harmonic on the \(j\)-sets and write its lift to level
\(s\) as

\[
 F_s^{(j)}(S)=\sum_{Q\in\binom Sj}\phi_j(Q).
\]

Decompose

\[
 g=F_7^{(2)}+F_7^{(3)}+F_7^{(4)}.
\]

For one diamond \(X\subset A\), with intermediate sets \(Y,Z\), define

\[
 \delta_j(X,A)=a_jF_7^{(j)}(A)+b_jF_5^{(j)}(X)
 +c_j\bigl(F_6^{(j)}(Y)+F_6^{(j)}(Z)\bigr),            \tag{2.1}
\]

where

\[
\begin{array}{c|ccc}
 j&a_j&b_j&c_j\\ \hline
 2&2/9&2/15&-1/6\\
 3&5/54&1/36&-5/108\\
 4&5/84&1/168&-5/336.
\end{array}                                            \tag{2.2}
\]

Then

\[
 \boxed{x_{X,A}=\frac1{15}+\delta_2(X,A)+\delta_3(X,A)+\delta_4(X,A)}
                                                               \tag{2.3}
\]

satisfies all equations (1.1), without yet asserting \(x\ge0\).

### Verification

For a pure degree-\(j\) lift, summing (2.1) over an upper clique, a lower
clique, and the edges incident with one middle vertex gives respectively

\[
\begin{aligned}
 21a+\binom{7-j}{2}b+6(7-j)c&=1,\\
 \binom{6-j}{2}a+15b+5(6-j)c&=0,\\
 6(5-j)a+5(6-j)b+\bigl(30+(6-j)(5-j)-j\bigr)c&=0.
\end{aligned}                                           \tag{2.4}
\]

The last line uses the Johnson eigenvalue
\((6-j)(5-j)-j\).  The three rows of (2.2) are the solutions of (2.4).
This proves (2.3).  Since harmonic decomposition commutes with translation,
the signed solution is translation-equivariant.

## 3. The pair component is safely positive

The pair degrees of \({\cal E}_7\) are \(50\) at cyclic distances
\(1,3,5\) and \(51\) at distances \(2,4\).  Therefore the degree-two
harmonic coefficient on a pair is

\[
 \phi_2(P)=
 \begin{cases}
 -2/105,&d(P)\in\{1,3,5\},\\
  1/35,&d(P)\in\{2,4\}.
 \end{cases}                                           \tag{3.1}
\]

Let \(H\) be the Cayley graph on \(\mathbb Z_{11}\) with differences
\(\pm2,\pm4\).  For a diamond \(A=X+a+b\), put

\[
 e_X=e_H(X),\quad
 u=|N_H(a)\cap X|,\quad v=|N_H(b)\cap X|,
 \quad s=\mathbf1_{ab\in E(H)}.
\]

Substitution in the \(j=2\) row of (2.2) gives the local formula

\[
 \boxed{\delta_2(X,A)=
 \frac{2e_X+5(u+v)+20s-36}{1890}.}                    \tag{3.2}
\]

All four statistics in the numerator are nonnegative, and hence

\[
 \delta_2(X,A)\ge-\frac{2}{105}.
\]

Consequently

\[
 \frac1{15}+\delta_2(X,A)\ge\frac1{21}>0.             \tag{3.3}
\]

Thus the complete point/pair correction has a uniform positive margin.
Any failure of the canonical lift (2.3) must come from degrees three or
four.

## 4. The first higher subset-moment cut

For a coordinate set \(Q\), let

\[
 N_Q=\sum_{\substack{X\subset A:\
                      A\setminus X\subseteq Q\subseteq A}}x_{X,A}.
\]

For one diamond, the quantity

\[
 \mathbf1_{Q\subset X}+\mathbf1_{Q\subset A}
 -\mathbf1_{Q\subset Y}-\mathbf1_{Q\subset Z}
\]

is one exactly when \(A\setminus X\subseteq Q\subseteq A\), and zero
otherwise.  Therefore every nonnegative solution of (1.1) must satisfy

\[
 N_Q=\binom{11-t}{5-t}+\binom{11-t}{7-t}
      +d_{{\cal E}_7}(Q)-2\binom{11-t}{6-t}\ge0,
 \qquad t=|Q|.                                        \tag{4.1}
\]

For \(t=1\), this is the point identity.  For \(t=2\), it is the known
pair floor

\[
 N_Q=d_{{\cal E}_7}(Q)-42.
\]

The first new member is

\[
 \boxed{N_Q=d_{{\cal E}_7}(Q)-14\ge0\qquad(|Q|=3).}   \tag{4.2}
\]

The explicit design clears it with room.  Inclusion-exclusion gives

\[
 d_{{\cal E}_7}(Q)
 =132-3\cdot48+\sum_{P\in\binom Q2}d_{{\cal D}_4}(P)
  -d_{{\cal D}_4}(Q).
\]

Every pair degree is at least fourteen, while a fixed triple lies in at
most eight four-sets.  Hence

\[
 d_{{\cal E}_7}(Q)\ge-12+3\cdot14-8=22,
 \qquad N_Q\ge8.                                      \tag{4.3}
\]

For \(t=4,5,6,7\), (4.1) becomes respectively

\[
 d_{{\cal E}_7}(Q),\quad 4+d_{{\cal E}_7}(Q),
 \quad3+d_{{\cal E}_7}(Q),\quad1+d_{{\cal E}_7}(Q),
\]

so no further single-subset moment obstruction occurs.

## 5. A natural positive splitting fails

The five-set

\[
 S=\{0,5,7,8,10\}
\]

has cyclic gap word \((5,2,1,2,1)\).  Deleting its five points gives the
four-gap words

\[
 (2,1,2,6),\ (7,1,2,1),\ (5,3,2,1),\
 (5,2,3,1),\ (5,2,1,3).                              \tag{5.1}
\]

None is a cyclic rotation of one of the twelve orbit representatives in
the explicit design.  Thus

\[
 \#\{R\in{\cal D}_4:R\subset S\}=0.                  \tag{5.2}
\]

Equivalently, the middle six-set \(Y=\mathbb Z_{11}\setminus S\) is
contained in no excess upper set.

This kills the following tempting construction.  Giving every diamond
weight \(1/21\) realizes upper load one everywhere and produces lower and
middle loads \(5/7\) and \(10/7\).  A nonnegative residual supported only
on \({\cal E}_7\) would have to supply lower load \(2/7\) and middle load
\(4/7\) everywhere, but at the above \(Y\) its middle load is forced to
zero.

This is **not** a Farkas refutation of (1.1): a general solution may
redistribute the unit load of the ordinary upper sets instead of fixing the
uniform \(1/21\) base.  It does show that point/pair balance does not support
the most direct positive superposition argument.

## 6. Remaining gate

The prescribed design has now passed:

1. all linear identities (via the explicit signed lift);
2. the pair-capacity inequalities;
3. every single-subset moment inequality, including the new triple cut.

What remains is genuinely cone-theoretic: prove that (2.3), or another
solution of the same affine system, is nonnegative.  For the canonical
solution this has been localized to the degree-three and degree-four
harmonic components of \(\mathbf1_{{\cal E}_7}\).  More complicated Farkas
cuts involving families of middle sets are not decided by the scalar
moments above.
