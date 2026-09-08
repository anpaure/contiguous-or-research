# The global component-noise gate: exact slack decomposition and no-go theorem

## 1. Verdict

This note does not prove the corrected component-noise estimate

\[
R_H(F)\le 4(n-1)B_H+o(nW).
\tag{CN}
\]

It proves that, at a global minimizer, the left side minus the proposed
baseline has an exact decomposition into three nonnegative terms.  One of
those terms is already (4(n-1)) times the desired floor excess.  Thus
\((\mathrm{CN})\) is not an easier mixing reformulation of low floor energy:
it is a strictly stronger near-equality assertion which includes low floor
energy, almost-pure Johnson degree two, and an almost-flat switching cube.

The note also proves:

* componentwise equivariance and zero point margins;
* exact equality rigidity for every switching cube;
* targetwise disjointness of component wall crossings, separately for each
  transposition, at exact equality;
* the equitable-colouring arithmetic forced by spectral equality;
* an exact row self-energy expansion, showing the cancellation scale that
  any proof of \((\mathrm{CN})\) must achieve; and
* a formal connected-overlay countermodel showing that zero point margins,
  equivariance, connectivity, and global minimality alone cannot imply
  \((\mathrm{CN})\).

No search, numerical experiment, or external black box is used.

## 2. Setup

Put

\[
n=2m+1,\qquad W=\binom{n}{m},\qquad
N_q=\binom{n}{m-q},\qquad r_q=m-q.
\]

Let (F) be an exact middle wreath factor.  At depth (q), let

\[
\mu_q(S)=\#\{\text{pointed wreath starts exposing }S\},
\qquad
a_q=\frac{W}{N_q},
\]

and set

\[
f_q=\mu_q-a_q\mathbf 1.
\]

Write (a_q=c_q+\theta_q), where (c_q=\lfloor a_q\rfloor) and
(0\le\theta_q<1).  The unconstrained integer floor at this rank is

\[
V_q^{\min}=N_q\theta_q(1-\theta_q).
\]

For a height (H<m), define

\[
B_H=\sum_{q=1}^{H}\frac{V_q^{\min}}{c_q},
\qquad
Q_H(F)=\sum_{q=1}^{H}
\frac{\|f_q\|_2^2-V_q^{\min}}{c_q},
\]

and

\[
S_H(F)=\sum_{q=1}^{H}\frac{\|f_q\|_2^2}{c_q}
=B_H+Q_H(F).
\]

The exact integer-floor inequality is

\[
2\sum_{q=1}^{H}\frac{O_q(F)}{c_q}\le Q_H(F).
\tag{2.1}
\]

For an unordered coordinate transposition \(\tau\), overlay (F) and
\(\tau F\).  Let \(\mathcal C_\tau(F)\) be the overlap components and let
\(u_{q,C}\), (w_{q,C}\) be the two depth-(q) histograms in component
(C).  Put

\[
N_{\tau,H}(F)=\sum_{C\in\mathcal C_\tau(F)}
\sum_{q=1}^{H}\frac{\|u_{q,C}-w_{q,C}\|_2^2}{c_q},
\]

\[
A_{\tau,H}(F)=\sum_{q=1}^{H}
\frac{\|\mu_q-\tau\mu_q\|_2^2}{c_q},
\]

and

\[
R_H(F)=\sum_\tau N_{\tau,H}(F),
\qquad
D_H(F)=\sum_\tau A_{\tau,H}(F).
\tag{2.2}
\]

Thus (R_H) is the unscaled component-noise sum.  A fair side choice in
one component contributes one quarter of the corresponding squared norm
to the conditional variance.

## 3. Component equivariance and zero margins

### Proposition 3.1

For every transposition \(\tau=(x\ y)\) and every overlap component (C),
the right rows of (C) are precisely the \(\tau\)-images of its left rows.
Consequently

\[
\boxed{w_{q,C}=\tau u_{q,C}.}
\tag{3.1}
\]

Moreover, (w_{q,C}-u_{q,C}) has zero total mass and zero point margins at
every depth.

### Proof

Fix a wreath row (P).  Across its (n) cyclic middle intervals, the total
number of incidences with (x) and (y) is (2m=n-1).  Hence not every
middle interval contains exactly one of the two coordinates.  Some middle
interval contains both or neither, is fixed by \(\tau\), and gives an
overlap edge from (P) to \(\tau P\).  Thus these two rows lie in the same
component.

The two sides of a finite regular bipartite component have equal size.
The injective map (P\mapsto\tau P) from its left side to its right side is
therefore onto, proving (3.1).

If the component has (k) rows on either side, both histograms have mass
(nk).  In one cyclic row, every coordinate belongs to exactly (r_q) of
the cyclic (r_q)-intervals.  Both component histograms therefore have
point margin (r_qk) at every coordinate.  Their difference has zero total
and point margins. \(\square\)

In Johnson harmonic notation, every component difference, and also every
full centered profile (f_q), belongs to

\[
\bigoplus_{j\ge2}E_j.
\tag{3.2}
\]

## 4. Exact switching-cube barrier

For a fixed \(\tau\), abbreviate

\[
d_C=(w_{q,C}-u_{q,C})_{q\le H}
\]

in the weighted Hilbert direct sum.  Switching a set (I) of components
changes the centered profile to

\[
f_I=f+\sum_{C\in I}d_C.
\]

Let

\[
e_\tau(I)=\|f_I\|_H^2-\|f\|_H^2.
\]

Switching all components gives \(\tau F\), and coordinate relabelling
preserves the objective.  Hence

\[
e_\tau(\varnothing)=e_\tau(\mathcal C_\tau)=0.
\]

For a uniformly random subset (I), independent component signs give the
exact identity

\[
\boxed{
\mathbb E_I e_\tau(I)
=\frac14\bigl(N_{\tau,H}-A_{\tau,H}\bigr).
}
\tag{4.1}
\]

If (F) is a global minimizer of the (H)-window quadratic objective,
then (e_\tau(I)\ge0) for every (I).  Therefore

\[
N_{\tau,H}\ge A_{\tau,H}.
\tag{4.2}
\]

Equality in (4.2) is rigid: (4.1) is the mean of a nonnegative function,
so equality forces (e_\tau(I)=0) for every (I).  Expanding singleton
and two-component switches gives

\[
2\langle f,d_C\rangle_H+\|d_C\|_H^2=0,
\tag{4.3}
\]

\[
\langle d_C,d_{C'}\rangle_H=0
\qquad(C\ne C').
\tag{4.4}
\]

Conversely, (4.3)--(4.4) make the whole cube energy-constant.

In particular, a connected overlay has only its two relabelled endpoint
factors and automatically has (N_{\tau,H}=A_{\tau,H}).  Connectivity by
itself provides no descent.

## 5. The exact three-slack identity

Decompose

\[
f_q=\sum_{j=2}^{r_q}f_q^{(j)}
\]

into Johnson harmonics.  The Johnson Laplacian eigenvalue on (E_j) is
(j(n-j+1)), and

\[
\sum_\tau\|f_q-\tau f_q\|_2^2
=2\sum_{j\ge2}j(n-j+1)\|f_q^{(j)}\|_2^2.
\]

It follows that

\[
\boxed{
D_H-4(n-1)S_H
=2\sum_{q=1}^{H}\frac1{c_q}
\sum_{j=3}^{r_q}(j-2)(n-j-1)\|f_q^{(j)}\|_2^2.
}
\tag{5.1}
\]

Every term on the right is nonnegative.  Combining (4.2), (5.1), and
(S_H=B_H+Q_H) gives the central exact identity.

### Theorem 5.1 (three nonnegative slacks)

At every global minimizer,

\[
\boxed{
\begin{aligned}
R_H-4(n-1)B_H
={}&(R_H-D_H)\\
&+\bigl(D_H-4(n-1)(B_H+Q_H)\bigr)\\
&+4(n-1)Q_H.
\end{aligned}}
\tag{5.2}
\]

All three terms on the right are nonnegative.

Consequently, if

\[
R_H\le4(n-1)B_H+\varepsilon_m,
\qquad \varepsilon_m=o(nW),
\tag{5.3}
\]

then separately

\[
Q_H=o(W),
\tag{5.4}
\]

\[
R_H-D_H=o(nW),
\tag{5.5}
\]

and

\[
\sum_{q=1}^{H}\frac1{c_q}
\sum_{j=3}^{r_q}\|f_q^{(j)}\|_2^2=o(W).
\tag{5.6}
\]

For (5.6), use

\[
2(j-2)(n-j-1)\ge2(n-4)
\]

for every (j\ge3) in the relevant half of the Johnson scheme.

Thus (5.3) already contains the desired quadratic conclusion (5.4), and
also demands two extra near-equalities.  It is a stronger rigidity theorem,
not a simplification of the balancing problem.

The quadratic conclusion is itself strictly stronger than MWB's weighted
(L^1) overload condition at the level of load profiles.  Starting from a
balanced vector, lower (t) distinct coordinates by one and place all
(t) removed units on one coordinate.  Its balanced overload is (t),
whereas its floor-quadratic excess is of order (t^2).  Taking, for
example, (t=W^{3/4}) gives overload (o(W)) but quadratic excess much
larger than (W).  This is an abstract load-profile separation, not a claim
that every such vector is realized by a wreath factor.

There is a useful meta-consequence.  Consider a proposed estimate of the form

\[
R_H\le4(n-1)B_H+\gamma_m Q_H+o(nW)
\]

With no error information stronger than (o(nW)), a scale-robust way for
this estimate to force (Q_H=o(W)) through (5.2) is

\[
\gamma_m\le4(n-1)-\Omega(n).
\]

More generally, if

\[
\delta_m=4(n-1)-\gamma_m>0,
\]

then the required error scale is (o(\delta_m W)).  A proportional gap
\(\delta_m=\Omega(n)\) makes the stated (o(nW)) error sufficient.  Such
an estimate lies a linear-in-(nQ_H) amount below the universal
spectral contribution (4(n-1)Q_H); proving it already supplies the
missing balancing information.  An upper bound whose (Q_H)-coefficient
is at least (4(n-1)) gives no control of (Q_H).

## 6. Equality and arithmetic rigidity

Suppose the exact baseline equation
\(R_H=4(n-1)B_H\) holds at a global minimizer. Then:

1. (Q_H=0), so every rank load is floor-balanced;
2. every (f_q) lies in Johnson degree two; and
3. every transposition switching cube has constant energy.

The third assertion is stronger integrally than (4.4).  Fix a depth and a
target (S).  Every child is balanced, so

\[
\mu_q(S)+\sum_{C\in I}d_{q,C}(S)\in\{c_q,c_q+1\}
\]

for every subset (I).  If the parent value is (c_q), every nonzero
increment must be (+1) and at most one component can have such an
increment.  If the parent value is (c_q+1), every nonzero increment must
be (-1), again in at most one component.  Hence

\[
\boxed{
\#\{C:d_{q,C}(S)\ne0\}\le1.
}
\tag{6.1}
\]

For each fixed transposition separately, the component wall-crossing
supports are targetwise disjoint. No disjointness across different
transpositions is asserted.

There is also a rankwise arithmetic condition.  Write a balanced load as

\[
\mu_q=c_q+\mathbf1_{\mathcal B_q},
\qquad
\theta_q=\frac{|\mathcal B_q|}{N_q}.
\]

If its centered part lies in (E_2), then

\[
L_J(\mathbf1_{\mathcal B_q}-\theta_q)
=2(n-1)(\mathbf1_{\mathcal B_q}-\theta_q).
\]

Thus \(\mathcal B_q\) is an equitable two-colouring of
(J(n,r_q)):

\[
S\notin\mathcal B_q:quad
|N_J(S)\cap\mathcal B_q|=2(n-1)\theta_q,
\tag{6.2}
\]

\[
S\in\mathcal B_q:quad
|N_J(S)\setminus\mathcal B_q|=2(n-1)(1-\theta_q).
\tag{6.3}
\]

In particular (2(n-1)\theta_q) must be an integer.

At the first shadow, (r_1=m-1) and \(\theta_1=2/m\).  Equations
(6.2)--(6.3) require cross-degrees (8) and (4m-8).

At depth two, for (m\ge8), one has (c_2=1) and

\[
\theta_2=\frac{6(m+1)}{m(m-1)}.
\]

Hence spectral equality requires

\[
2(n-1)\theta_2
=24+\frac{48}{m-1}
\]

to be an integer.  In particular exact baseline equality is impossible at
depth two whenever (m-1\nmid48), including every (m\ge50).
This is only an exact-equality obstruction; by itself it gives no
macroscopic lower bound on the slack allowed in (5.3).

### Theorem 6.1 (first-shadow spectral equality is impossible)

For every (m\ge18), there is no balanced first-shadow load whose
centered indicator lies in (E_2).  Consequently exact equality in the
global baseline is impossible as soon as the first shadow is controlled.

### Proof

Suppose otherwise.  Put

\[
r=m-1,qquad k=r-1=m-2,
\]

and let \(\mathcal B\subseteq\binom{[n]}r\) be the bonus family.  By
(6.2)--(6.3), every nonbonus (r)-set has exactly (8) bonus Johnson
neighbours, while every bonus (r)-set has exactly (4m-8) nonbonus
neighbours.

For a (k)-set (T), let

\[
\kappa(T)=\#\{S\in\mathcal B:T\subset S,\ |S|=r\}.
\]

The full star over (T) has size

\[
n-k=m+3.
\]

If \(\kappa(T)<m+3\), choose a nonbonus extension (S\supset T).  Every
bonus extension of (T) is a bonus Johnson neighbour of (S), so

\[
\boxed{\kappa(T)\le8\quad\text{or}\quad\kappa(T)=m+3.}
\tag{6.4}
\]

Call (T) **full** in the second case, and write \(\mathcal T\) for the
family of full (k)-sets.

Fix (S\in\mathcal B).  Its bonus neighbours can be grouped according to
the deleted point.  Hence

\[
\sum_{\substack{T\subset S\\|T|=k}}(\kappa(T)-1)
=r(n-r)-(4m-8)=m^2-3m+6,
\]

or equivalently

\[
\sum_{\substack{T\subset S\\|T|=k}}\kappa(T)
=m^2-2m+5.
\tag{6.5}
\]

If all (r=m-1) facets were full, the sum would be

\[
r(m+3)=m^2+2m-3.
\]

Thus the total deficit from full-star size is exactly (4m-8).  By
(6.4), every nonfull facet contributes a deficit between (m-5) and
(m+3).  When (m\ge18), three such deficits cannot reach (4m-8),
while five already exceed it.  Therefore every bonus (S) has exactly
four nonfull facets and exactly

\[
\boxed{m-5}
\]

full facets.  (The four nonfull \(\kappa\)-values sum to (20).)

An (r)-set outside \(\mathcal B\) contains no full facet.  If (U) is
the up-incidence operator

\[
(Ug)(S)=\sum_{\substack{T\subset S\\|T|=k}}g(T),
\]

we have the exact Boolean identity

\[
\boxed{U\mathbf1_{\mathcal T}=(m-5)\mathbf1_{\mathcal B}.}
\tag{6.6}
\]

The operator (U) intertwines the Johnson harmonic decompositions and is
injective in this range.  For completeness,

\[
U^*U=(n-k)I+A_{J(n,k)},
\]

and its eigenvalue on (E_j) is

\[
(k+1-j)(n-k-j)>0
\qquad(0\le j\le k).
\]

Since \(\mathbf1_{\mathcal B}\in E_0\oplus E_2\), (6.6) implies

\[
\mathbf1_{\mathcal T}\in E_0\oplus E_2.
\tag{6.7}
\]

Now count the Johnson boundary of \(\mathcal T\) directly.  Fix
(T\in\mathcal T) and (z\notin T).  The extension (S=T\cup\{z\})
belongs to \(\mathcal B\).  Its four nonfull facets are precisely four
sets (T-\{x\}+\{z\}), and these are the four neighbours of (T) outside
\(\mathcal T\) associated with (z).  There are (m+3) choices of (z),
so every member of \(\mathcal T\) has exactly

\[
4(m+3)
\tag{6.8}
\]

Johnson neighbours outside \(\mathcal T\).

On the other hand, (6.7) says that the centered indicator of
\(\mathcal T\) is a degree-two Johnson eigenfunction.  If
\(\delta=|\mathcal T|/\binom nk>0\), its outside degree must therefore be

\[
2(n-1)(1-\delta)=4m(1-\delta)<4m,
\tag{6.9}
\]

contradicting (6.8).  This proves the theorem. \(\square\)

The contradiction is deliberately an exact-equality theorem.  At the
first shadow (V_1^{\min}=\Theta(W/m)), so the entire rank-one centered
mass is already (o(W)).  A robust version strong enough to contradict
the aggregate (o(nW)) allowance would require a genuinely quantitative
stability theorem and is not proved here.

The same argument gives a useful density exclusion beyond depth one.

### Theorem 6.2 (sparse Boolean (E_2) exclusion)

Let (2\le r\le m), put (s=n-r+1), and suppose that a nonempty proper
family \(\mathcal B\subseteq\binom{[n]}r\) has density \(\theta\), with

\[
\mathbf1_{\mathcal B}-\theta\mathbf1\in E_2.
\]

Set

\[
b=4m\theta,
\qquad
d=4m(1-\theta).
\]

These are necessarily integers.  If (r>4) and

\[
\boxed{
b<s,qquad 3s<d<5(s-b),
}
\tag{6.10}
\]

then no such family exists.

### Proof

For an ((r-1))-set (T), let \(\kappa(T)\) count its extensions in
\(\mathcal B\).  The star over (T) has size (s).  If it is not full,
choose an outside extension.  Its (\kappa(T)) bonus extensions are all
bonus Johnson neighbours, so

\[
\kappa(T)\le b.
\tag{6.11}
\]

For (S\in\mathcal B), the sum of the deficits (s-\kappa(T)) over its
nonfull facets is exactly its number (d) of neighbours outside
\(\mathcal B\).  Every such deficit lies in ([s-b,s]).  The inequalities
in (6.10) force the number of nonfull facets to be exactly four: three
deficits cannot sum to (d), and five already sum to more than (d).

Let \(\mathcal T\) be the family of full ((r-1))-facets.  Every member of
\(\mathcal B\) contains exactly (r-4) members of \(\mathcal T\), while
every set outside \(\mathcal B\) contains none.  Hence

\[
U\mathbf1_{\mathcal T}=(r-4)\mathbf1_{\mathcal B}.
\]

The up operator is injective below the middle and intertwines each Johnson
harmonic \(E_j\) with the corresponding \(E_j\) in the next rank, so
\(\mathbf1_{\mathcal T}\in E_0\oplus E_2\). Yet every
full facet has exactly four nonfull replacement facets for each of its
(s) extensions.  Its Johnson boundary degree in \(\mathcal T\) is
therefore (4s>4m).  A nonempty Boolean (E_0\oplus E_2) family has
inside-to-outside degree (4m(1-\delta)<4m), where \(\delta\) is its
density.  Contradiction. \(\square\)

For sequences \(r_m=m-O(\sqrt m)\) and \(\theta_m\to\theta_0\) with
\(0<\theta_0<1/16\), conditions (6.10) hold for all sufficiently large
\(m\). Applying the theorem to the complementary family gives the
corresponding open limiting exclusion for \(15/16<\theta_0<1\). On a
Gaussian window, a rigorous positive-density conclusion is obtained by
choosing a compact \(x=q/\sqrt m\) interval, away from the integer crossings
of \(e^{x^2}\), on which its fractional part stays in one of these open
density ranges. No endpoint claim at \(1/16\) or \(15/16\) is made.
Turning this exact exclusion into an (L^2)-stability theorem would be a
new and potentially decisive obstruction to (5.3); no such stability
estimate is claimed here.

## 7. Gaussian-window size of the baseline

Fix (A>0) and put (H=\lceil A\sqrt m\rceil).  Uniformly for
(q\le H),

\[
\frac{W}{N_q}=\exp\!\left(\frac{q^2}{m}+O_A(m^{-1/2})\right).
\]

Define for (t\ge1)

\[
\varphi(t)=
\frac{\{t\}(1-\{t\})}{\lfloor t\rfloor\,t},
\]

with value zero at integers.  The one-sided limits at every integer are
zero, so \(\varphi\) is continuous.  Since

\[
\frac{V_q^{\min}}{c_qW}
=\varphi\!\left(\frac{W}{N_q}\right),
\]

a Riemann-sum argument gives

\[
\boxed{
\frac{B_H}{W\sqrt m}
\longrightarrow
\kappa_A:=\int_0^A\varphi(e^{x^2})\,dx.
}
\tag{7.1}
\]

The integrand is positive away from a discrete set, so
\(\kappa_A>0\) for every (A>0).  Thus the forced baseline has order

\[
4(n-1)B_H=\Theta_A(nW\sqrt m),
\]

whereas (5.3) permits only (o(nW)) excess.  It asks for relative accuracy
\(o(m^{-1/2})\) at the aggregate Gaussian-window scale.  In view of
(5.4)--(5.6), almost all of this \(\Theta_A(W\sqrt m)\) centered mass must
sit in Johnson degree two.

This exposes a concrete stability problem which decides whether the
component-noise gate is merely difficult or actually false.  The following
statement would rule out (5.3), rather than prove it.

> **Sparse Boolean-(E_2) stability problem.**  Fix a compact interval
> (I\subset(0,1/16)).  For (r=m-O(\sqrt m)), prove that there is
> (\varepsilon_I>0) such that every Boolean family
> \(\mathcal B\subseteq\binom{[n]}r\) of density in (I) satisfies
> \[
> \|P_{E_1\oplus E_{\ge3}}
> (\mathbf1_{\mathcal B}-|\mathcal B|/N)\|_2^2
> \ge\varepsilon_I N.
> \tag{7.2}
> \]

Theorem 6.2 is the zero-error version of (7.2).  To see why the robust
version would refute (5.3), note first that for every integer load vector
there is a pointwise adjacent-integer vector (b\in\{c,c+1\}^N) with

\[
\|\mu-b\|_2^2\le
\sum_S(\mu(S)-c)(\mu(S)-c-1).
\]

After changing exactly the mass discrepancy of (b), one obtains a
balanced adjacent-integer vector (b'=c+\mathbf1_{\mathcal B}).  If

\[
\Delta=\left|\sum_S b(S)-W\right|,
\]

then Cauchy--Schwarz gives

\[
\Delta\le\sqrt N\,\|b-\mu\|_2\le\sqrt{NQ_q}.
\]

Since \(\|b-b'\|_2^2=\Delta\),

\[
\boxed{
\|\mu-b'\|_2^2
\le2Q_q+2\sqrt{NQ_q}.
}
\tag{7.3}
\]

Thus rank floor excess (Q_q=o(N)) implies squared adjustment distance
\(o(N)\).

Under (5.3), the sums of the floor excesses and of all (j\ge3) harmonic
masses are (o(W)) over \(\Theta(\sqrt m)\) ranks.  Since exact-factor
profiles have zero (E_1) part, for all but (o(\sqrt m)) relevant ranks
the associated Boolean bonus vector has

\[
\|P_{E_1\oplus E_{\ge3}}
(\mathbf1_{\mathcal B}-\theta)\|_2^2=o(N).
\]

The function \(\{e^{x^2}\}\) lies in any chosen subinterval of
((0,1/16)) on a positive-length set of (x)'s once the interval is chosen
inside its range on ([0,A]).  Thus (7.2) would contradict (5.3) on a
positive proportion of Gaussian depths.

No robust estimate (7.2) is proved here.  It is, however, a sharply isolated
finite-design/stability problem arising from the equality analysis, and it
shows that the corrected component-noise criterion may be stronger than the
factor fibre can satisfy.

## 8. Exact row self-energy and required cancellation

Let (h_{P,r}) be the indicator of the (n) cyclic (r)-intervals of one
wreath row (P).  If the transposed coordinates have shorter cyclic
distance \(\ell\in\{1,\ldots,m\}\), then

\[
\|\tau h_{P,r}-h_{P,r}\|_2^2
=4\min(r,\ell)-4\mathbf1_{\{\ell=r\}}.
\tag{8.1}
\]

An odd cycle has exactly (n) unordered coordinate pairs at each shorter
distance.  Therefore, for (2\le r\le m),

\[
\boxed{
\sum_\tau\|\tau h_{P,r}-h_{P,r}\|_2^2
=2n\bigl(r(n-r)-2\bigr).
}
\tag{8.2}
\]

To justify (8.1), exactly (2\min(r,\ell)) cyclic (r)-windows contain
one of the transposed coordinates but not the other.  Their images normally
leave the original cyclic-window family.  Precisely when \(\ell=r\), two
of those windows are exchanged with each other and remain in the family.
The squared distance of two indicator vectors is the size of their
symmetric difference, giving (8.1).  Summing over the (n) pairs at each
distance gives

\[
4n\left(\sum_{\ell=1}^{r}\ell+(m-r)r-1\right)
=2n(r(n-r)-2),
\]

which is (8.2).

There are (W/n) rows in (F).  Expanding component sums gives

\[
\boxed{
\begin{aligned}
R_q={}&2W\bigl(r_q(n-r_q)-2\bigr)\\
&+2\sum_\tau\sum_{C\in\mathcal C_\tau(F)}
\sum_{P<P'\in C}
\langle\tau h_{P,r_q}-h_{P,r_q},
       \tau h_{P',r_q}-h_{P',r_q}\rangle.
\end{aligned}}
\tag{8.3}
\]

The first line is the row-diagonal mass.  At the first shadow it is

\[
2W(m^2+m-4),
\tag{8.4}
\]

whereas the exact spectral floor at that rank is

\[
4(n-1)V_1^{\min}
=16W\frac{m-2}{m+2}.
\tag{8.5}
\]

Thus exact floor-scale noise requires cancellation of all but
(O(m^{-2})) of the row-diagonal mass.  Even the weaker allowed error
(o(nW)) requires cancellation of all but (o(m^{-1})) of it at the
first shadow.  Component sizes or connectivity alone do not give the sign
of the cross terms in (8.3).

## 9. A formal connected-overlay countermodel

The following construction is not an exact wreath factor.  It is an
axiomatic countermodel showing exactly which missing hypothesis must do
the work.

Fix one cyclic order (P), one rank (2\le r\le m), and let (h_{P,r})
be its (n)-window incidence vector.  Put

\[
T=\frac Wn\,h_{P,r}.
\]

Then (T) is an integer nonnegative vector of total mass (W), every
point has margin (rW/n), and (T) is a sum of (W/n) genuine cyclic-row
incidence vectors.  Consider the formal state space

\[
\mathfrak X=\{\sigma T:\sigma\in S_n\}.
\]

Every state has the same centered quadratic energy, so every state is a
global minimizer in \(\mathfrak X\).  For each transposition \(\tau\),
declare the overlap to have one connected component, with difference
\(\tau T-T\).  The switching cube then consists only of its two relabelled
endpoints.  Component equivariance, zero total and point margins,
connectivity, global minimality, and (N_\tau=A_\tau) all hold exactly.

Nevertheless

\[
\left\|T-\frac WN\mathbf1\right\|_2^2
=\frac{W^2}{n}\left(1-\frac nN\right),
\tag{9.1}
\]

which is exponentially larger than the integer floor (V^{\min}\le N/4)
in the central regime.  The component-noise upper bound fails enormously.

This does not disprove (5.3) for actual exact wreath factors.  It proves
that the ingredients used before exact middle ownership is invoked --
cyclic-row decomposition, zero point margins, equivariance, connected
overlays, and global minimality -- cannot imply it.  The missing theorem
must exploit the actual factor fibre and force the cancellations in (8.3).

## 10. Final mathematical status

The corrected gate is valid as a sufficient condition, but (5.2) shows it
is a three-part rigidity theorem:

\[
\boxed{
\begin{gathered}
\text{low integer-floor excess},\\
\text{negligible Johnson degrees }j\ge3,\\
\text{negligible aggregate switching barrier}.
\end{gathered}}
\]

It is strictly stronger than the quadratic conclusion and substantially
stronger than MWB's weighted \(L^1\) overload conclusion.  No estimate
derived only from zero point margins, component connectivity, or global
minimality can establish it.  A successful proof along this route needs a
new exact-factor cancellation theorem for the row cross terms in (8.3), or
a richer move system which crosses the connected-overlay energy barriers.
