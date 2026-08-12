# Every endpoint-critical physical Bellman row is an odd tropical convolution of the head

**Date:** 2026-08-12
**Method:** pure mathematics; greedy literal grouping, generalized inverses,
and Stieltjes integration
**Status:** unconditional.  The complete physical endpoint-critical
Bellman functional, including every finite-availability shoulder, is reduced
exactly to one integer head staircase and its odd tropical convolutions.
Every row-\(q\) first hit has a literal certificate using at most
\(2q+1\) displayed denominations.  Positivity of the resulting one-profile
functional is not proved.

## 1. Setting

Let \(n\ge2\), and let

\[
 0=v_0\le v_1\le\cdots\le v_n=1,
 \qquad v_{i+j}\ge v_i+v_j\quad(i+j\le n),
 \qquad v_j\le {j\over n}.
\tag{1.1}
\]

Let \(L\) be the literal max-plus Bellman closure of the displayed
denominations.  For \(q\ge0\) and \(0\le r\le n\), put

\[
 P_q(r)=L(qn+r)-q.
\tag{1.2}
\]

Then

\[
 P_q(0)=0,qquad P_q(n)=1,qquad
 0\le P_q(r)\le {r\over n}.
\tag{1.3}
\]

In particular \(P_0(r)=v_r\), while \(P_1(r)\) is the first physical
carry row from the two-block covariance reduction.

## 2. Greedy grouping

### Theorem 2.1 (odd-degree literal row theorem)

Let \(q\ge0\) and \(qn\le m\le(q+1)n\).  Then

\[
\boxed{
 L(m)=
 \max_{\substack{1\le t\le2q+1\\
                   a_1,\ldots,a_t\in\{0,\ldots,n\}\\
                   a_1+\cdots+a_t=m}}
       \sum_{i=1}^t v_{a_i}.}
\tag{2.1}
\]

Zero parts may be used to pad every list to length exactly \(2q+1\).

#### Proof

First suppose \(m<(q+1)n\).  Take any literal partition of \(m\), order
its parts arbitrarily, and greedily form maximal consecutive blocks whose
total sizes do not exceed \(n\).  Let their totals be
\(a_1,\ldots,a_t\).

If \(t\ge2q+2\), pair the first \(2q+2\) blocks consecutively.  Maximality
of every odd block says

\[
 a_{2j-1}+a_{2j}>n\qquad(1\le j\le q+1).
\]

Their combined total would exceed \((q+1)n\), a contradiction.  Hence
\(t\le2q+1\).  Internal superadditivity collapses each block to its one
displayed total without decreasing reward.  Thus every literal partition
is bounded by one of the expressions on the right of (2.1).  The converse
is immediate because every displayed expression is itself a literal
partition.

If \(m=(q+1)n\), density gives \(L(m)\le q+1\), while \(q+1\) endpoint
parts attain equality.  Their number is at most \(2q+1\) (also for
\(q=0\)), so (2.1) holds at the endpoint as well. \(\square\)

In reduced-cost coordinates

\[
 e_j={j\over n}-v_j,
 \qquad
 \delta(m)={m\over n}-L(m),
\tag{2.2}
\]

Theorem 2.1 is the exact finite min-plus identity

\[
\boxed{
 \delta(m)=
 \min_{\substack{t\le2q+1\\a_1+\cdots+a_t=m}}
       \sum_{i=1}^t e_{a_i}
 \qquad(qn\le m\le(q+1)n).}
\tag{2.3}
\]

Unlike a stabilized Apéry formula, (2.3) retains the ordinary total-size
constraint and therefore the complete physical availability shoulder.

## 3. Odd tropical inverse hierarchy

Define

\[
 C_q(z)=\min\{0\le r\le n:P_q(r)\ge z\},
 \qquad U_q(z)=C_q(z)-nz
 \quad(0\le z\le1).
\tag{3.1}
\]

Thus \(C_0,U_0\) are the inverse and discrepancy of the displayed head.

### Theorem 3.1 (exact odd tropical convolution)

For every \(q\ge0\) and \(0<z<1\),

\[
\boxed{
 qn+C_q(z)=
 \min_{\substack{x_1,\ldots,x_{2q+1}\in[0,1]\\
                  x_1+\cdots+x_{2q+1}\ge q+z}}
       \sum_{i=1}^{2q+1}C_0(x_i).}
\tag{3.2}
\]

Equivalently,

\[
\boxed{
 U_q(z)=
 \min_{\sum x_i\ge q+z}
 \left\{
   \sum_{i=1}^{2q+1}U_0(x_i)
   +n\left(\sum_{i=1}^{2q+1}x_i-q-z\right)
 \right\}.}
\tag{3.3}
\]

#### Proof

Let \(C(t)=\min\{m:L(m)\ge t\}\).  Density gives \(C(q+z)>qn\).
Using \(q\) endpoint parts together with a head witness for \(z\) gives

\[
 C(q+z)\le qn+C_0(z)\le(q+1)n.
\tag{3.4}
\]

Every tuple in (3.2) supplies a literal partition whose reward is at least
\(q+z\), and hence its total index is at least \(C(q+z)\).  Conversely,
Theorem 2.1 collapses a maximizing partition at the first hitting index to
at most \(2q+1\) displayed parts.  At the endpoint \((q+1)n\), use
\(q+1\) endpoint parts and pad by zeros.  Taking their displayed rewards as
the \(x_i\)'s gives the reverse inequality.  Finally

\[
 C(q+z)=qn+C_q(z)
\]

by (1.2).  Substituting \(C_0(x)=nx+U_0(x)\) proves (3.3). \(\square\)

Two useful pointwise consequences are

\[
\boxed{
 U_q(z)\le U_0(z),
 \qquad
 U_q(z)\le(2q+1)
 U_0\!\left({q+z\over2q+1}\right).}
\tag{3.5}
\]

The first uses \(q\) entries equal to one, one entry equal to \(z\), and
zeros elsewhere.  The second uses equal entries.  The full unequal minimum
in (3.3) is stronger than either estimate.

### Corollary 3.2 (rowwise integer saturation)

Every level-\((q+z)\) first hitting event has a literal certificate using
at most \(2q+1\) head denominations.  Hence each fixed physical Bellman row
lies in a bounded-degree integer semigroup of the literal head signatures,
not merely in its rational cone.  For \(q=1\), this is the degree-three
first-row saturation theorem.

The degree grows linearly with \(q\), but the analytic weight of row \(q\)
decays Gaussianly.  This statement remains one-dimensional: it does not
imply occurrence-labelled packet semigroup normality.

## 4. Exact one-profile formula for the complete physical functional

Put

\[
 a={\pi\over4},\qquad f(x)=e^{-ax^2},
\]

\[
 B(y)=f(1-y)+f(1+y),
 \qquad
 \phi_q(y)=f(q+1+y)\quad(q\ge1).
\tag{4.1}
\]

For the normalized Rayleigh kernel \(\kappa(y)=K(Ay)\), the complete
physical Bellman functional is

\[
 \Phi(v)=
 n-\sum_{r<n}B(v_r)
 -\sum_{q\ge1}\sum_{r<n}\phi_q(P_q(r)).
\tag{4.2}
\]

### Theorem 4.1 (exact all-row odd-tropical covariance)

One has

\[
\boxed{
 \Phi(v)=
 \int_0^1U_0(z)B'(z)\,dz
 +\sum_{q\ge1}\int_0^1U_q(z)\phi_q'(z)\,dz,}
\tag{4.3}
\]

where every \(U_q\) is the explicit odd tropical convolution (3.3) of
the single integer staircase \(U_0\).

#### Proof

Stieltjes integration for each phase list gives

\[
 \int_0^1U_0B'=n\int_0^1B-\sum_{r<n}B(v_r)
\tag{4.4}
\]

and

\[
 \int_0^1U_q\phi_q'
 =n\int_0^1\phi_q-\sum_{r<n}\phi_q(P_q(r)).
\tag{4.5}
\]

The Gaussian series and its derivative converge uniformly on
\([0,1]\), while \(0\le U_q\le n\), so termwise summation is justified.
Finally

\[
 \sum_{q\ge1}\phi_q(y)=\sum_{\ell\ge2}f(\ell+y)=H_2(y),
 \qquad
 \int_0^1(B+H_2)=1.
\tag{4.6}
\]

The constant terms in (4.4)--(4.5) therefore sum to \(n\), giving exactly
(4.2). \(\square\)

### Theorem 4.2 (complete-functional late saturation)

Let \(\theta\in(0,1)\) be the unique interior zero of \(B'\), equivalently
the normalized location of the compact Rayleigh minimum.  The functional
\(\Phi\) attains a minimum on the compact polytope (1.1).  At every
minimizer, if \(0<j<n\) and \(v_j>\theta\), then

\[
\boxed{
 v_j=v_{j-1}
 \quad\hbox{or}\quad
 v_j=v_i+v_{j-i}\text{ for some }1\le i<j.}
\tag{4.7}
\]

#### Proof

The Gaussian tails make (4.2) uniformly convergent over the compact table
polytope; each finite Bellman value is a maximum of finitely many linear
forms.  Hence \(\Phi\) is continuous and attains a minimum.

If neither equality in (4.7) holds, lower \(v_j\) slightly.  Monotonicity,
density, and all superadditivity inequalities remain valid.  Every Bellman
value \(L(m)\) weakly decreases.  On the outer branch the kernel \(\kappa\)
is strictly increasing, so every tail contribution weakly decreases.  On
the head compact branch, \(v_j>\theta\) also lies on the strictly increasing
side of \(\kappa=1-B\), so its own contribution strictly decreases.  The
complete functional therefore strictly decreases, a contradiction.
\(\square\)

Thus even a counterexample to the full physical endpoint inequality may be
chosen with a literal additive staircase throughout its post-minimum head.

There is also an exact occupation constraint on every early phase which is
not blocked by a table face.  For \(m\ge0\), let \(\operatorname{Opt}(m)\)
be the finite set of literal partitions attaining \(L(m)\), and define

\[
 M_j(m)=\max_{x\in\operatorname{Opt}(m)}x_j.
\tag{4.8}
\]

### Theorem 4.3 (early-phase occupation compensation)

Let \(v\) minimize \(\Phi\), and suppose \(0<j<n\),
\(0<v_j<\theta\), and all three kinds of upward table constraint have
positive slack:

\[
 v_j<v_{j+1},\qquad v_j<{j\over n},qquad
 v_{j+i}>v_j+v_i\quad(1\le i\le n-j).
\tag{4.9}
\]

Then

\[
\boxed{
 \sum_{m\ge n}\kappa'(L(m))M_j(m)
 \ge-\kappa'(v_j)>0.}
\tag{4.10}
\]

Thus every unblocked early phase in a minimizer must be used, with the
displayed quantitative Gaussian occupation, by literal optimal tail
partitions.

#### Proof

Under (4.9), increasing only \(v_j\) by a sufficiently small positive
amount remains inside the table polytope.  The one-sided directional
derivative of the finite maximum defining \(L(m)\) is

\[
 D^+L(m)=M_j(m).
\tag{4.11}
\]

For \(m<n\), internal superadditivity keeps \(L(m)=v_m\).  The strict
outgoing inequalities in (4.9) imply that only the head term \(m=j\) has
nonzero derivative.  At every \(m\ge n\), the kernel is on its increasing
outer branch.  Therefore

\[
 D^+\Phi
 =\kappa'(v_j)+
   \sum_{m\ge n}\kappa'(L(m))M_j(m).
\tag{4.12}
\]

The series is absolutely convergent: \(M_j(m)\le m/j\), while endpoint
parts give \(L(m)\ge\lfloor m/n\rfloor\), and the outer derivative decays
Gaussianly.  Minimality gives \(D^+\Phi\ge0\), proving (4.10). \(\square\)

Equation (4.10) is the literal Bellman version of the surviving covariance:
negative compact drift must be paid by integer occupation of optimal tail
paths.  It is stronger than a sublevel-count inequality and exposes the
precise integer statistic which a packet rounding would have to retain.

## 5. Consequence and remaining gate

The complete endpoint-critical analytic problem is now a one-profile
inequality:

\[
\boxed{
 \int_0^1U_0B'
 +\sum_{q\ge1}\int_0^1
       (\mathcal T_{q,n}U_0)\phi_q'\ge0,}
\tag{5.1}
\]

where \(\mathcal T_{q,n}\) is the literal odd tropical operator in (3.3).
This identity retains every finite shoulder automatically; no formal
period, conductor, or residue-only relaxation occurs.

It strictly strengthens the first-row lower bound: rather than replacing
all later phases by the first carry row, it records the exact physical
phase at every Gaussian tail level.  It also explains the relevant lattice
boundary.  Scalar Bellman rows are integrally generated at bounded degree,
so any remaining congruence obstruction in the OR-word construction must
couple named owners, sockets, trace states, or common-cap resources.

Neither (5.1) nor protected occurrence-labelled integral rail normality is
proved here.  The analytic sign and multidimensional packet saturation
remain separate gates.
