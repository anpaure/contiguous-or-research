# Domino twins: the exact stopped factorial generator and the macroscopic-overlap gate

Date: 2026-07-27

## 0. Outcome

The time-zero factorial overlap hierarchy of the domino-twin catalogue is
not a hereditary statement.  This note identifies the exact dynamic
observable and its generator.

For a live entrance target \(X\), a live packet \(F\ni X\), and

\[
 w_p(F,G)=(|F\cap G|-1)_p,
\]

put

\[
 d=d_t(X),\qquad
 S_{p,t}(X,F)=\sum_{G\in L_t(X)}w_p(F,G),\qquad
 A_{p,t}(X,F)=\frac{S_{p,t}(X,F)}d.
\]

If a selected edge \(e\) is disjoint from \(F\), define

\[
 B_X(e)=|\{G\in L_t(X):G\cap e\ne\varnothing\}|,
\]

\[
 C_{p,X,F}(e)=
 \sum_{\substack{G\in L_t(X)\\G\cap e\ne\varnothing}}w_p(F,G).
\]

Then, up to the stopping time at which \(F\) dies,

\[
 \boxed{
 \Delta_e A_{p,t}(X,F)
 =\frac{A_{p,t}(X,F)B_X(e)-C_{p,X,F}(e)}{d-B_X(e)}.}
 \tag{0.1}
\]

Consequently, for predictable live-edge clock rates \(\nu_t(e)\),

\[
 \boxed{
 \mathcal G_tA_{p,t}(X,F)
 =\sum_{\substack{e\in\mathcal H_t\\e\cap F=\varnothing}}
 \nu_t(e)
 \frac{A_{p,t}(X,F)B_X(e)-C_{p,X,F}(e)}{d-B_X(e)}.}
 \tag{0.2}
\]

This has no deterministic sign.  It is positive precisely when the next
selected edge deletes a below-average portion of the factorial-overlap
mass in the link of \(X\).  The full-catalogue diameter proof gives no
pointwise control of this covariance in a residual link.

There is a second, genuinely new obstruction.  Every twin packet has
\(\Theta(n)\) distinct near-parallel twins sharing at least \(K-8\) of its
\(K=2n\) entrance resources.  Their contribution is invisible to every
fixed or logarithmic factorial moment, because their relative mass is
factorially small.  Under an independent survivor tilt to
\(z=m^{-1/2}\), however, the factor \(z^{-(K-9)}\) cancels that factorial
smallness.  Thus the proved static \(K_{2,\ell}\) hierarchy through
\(\ell=O(\log m)\) does **not** imply stopped regeneration.

The correct next input is a macroscopic-overlap quarantine, in addition
to the logarithmic ACLE hierarchy.  Section 5 gives an incidence-averaged
form sufficient for a near-factor argument.

## 1. Exact individual generator

Let \(L=L_t(X)\) be the current link.  If \(e\cap F=\varnothing\), then
\(X\notin e\), and selection of \(e\) replaces \(L\) by

\[
 L'=L\setminus\{G:G\cap e\ne\varnothing\}.
\]

Hence

\[
 d'=d-B_X(e),\qquad S'=S-C_{p,X,F}(e).
\]

Subtracting \(S/d\) from \(S'/d'\) proves (0.1), and summing it against
the live-edge clock rates proves (0.2).  If \(e\cap F\ne\varnothing\),
the monitor is stopped and contributes no further generator term.

Equivalently, for a deterministic comparison level \(b_p(t)\), the
unnormalized excess

\[
 M_{p,t}(X,F)=S_{p,t}(X,F)-b_p(t)d_t(X)
\]

has event increment

\[
 \Delta_eM_{p,t}=b_p(t)B_X(e)-C_{p,X,F}(e),              \tag{1.1}
\]

apart from the deterministic transport term \(-\dot b_p(t)d_t(X)\).
Formula (1.1) is the exact stopped compensator which a regeneration
argument must control.

## 2. Aggregate covariance form

There is a cleaner symmetric version.  Put

\[
 P=d(d-1),\qquad
 Z_{p,t}(X)=
 \sum_{\substack{F,G\in L_t(X)\\F\ne G}}w_p(F,G),
 \qquad \bar A_{p,t}(X)=\frac{Z_{p,t}(X)}P.
\]

For \(e\not\ni X\), let \(H_e=\{F\in L:F\cap e\ne\varnothing\}\) and
\(B=|H_e|\).  The number of killed ordered row pairs is

\[
 Q_e=P-(d-B)(d-B-1)=B(2d-B-1).                         \tag{2.1}
\]

Let

\[
 W_e=\sum_{\substack{F\in H_e,\ G\in L\\F\ne G}}w_p(F,G),
\qquad
 U_e=\sum_{\substack{F,G\in H_e\\F\ne G}}w_p(F,G).
\]

The killed factorial weight is \(C_e=2W_e-U_e\).  Therefore

\[
 \boxed{
 \Delta_e\bar A_{p,t}(X)
 =\frac{\bar A_{p,t}(X)Q_e-C_e}{P-Q_e},}                \tag{2.2}
\]

and its numerator decomposes exactly as

\[
 \boxed{
 \bar A Q_e-C_e
 =2\bigl(\bar A B(d-1)-W_e\bigr)
  +\bigl(U_e-\bar A B(B-1)\bigr).}                      \tag{2.3}
\]

The first bracket is the marginal row-hazard covariance.  The second is
the genuine common-column covariance.  The latter is represented by the
literal \(K_{2,j}\) extension tower.  Formula (2.3) explains both why the
static common-column moments are relevant and why they are not by
themselves hereditary: the residual process must also control their
covariance with the current link.

If the process is stopped whenever \(B_X(e)>\beta d_t(X)\), with
\(\beta<1/4\), then \(P-Q_e\ge(1-3\beta)P\).  Thus (2.3) gives a literal
positive-drift observable with no denominator ambiguity.

## 3. Deterministic heredity fails

The proof of the time-zero factorial theorem uses

\[
 \sum_{G\ni X}(|F\cap G|-1)_p
\]

over the complete link and bounds it by summing full-catalogue cluster
codegrees.  After an arbitrary edge restriction, the surviving link may
consist only of the largest values of \((|F\cap G|-1)_p\).  Therefore no
normalized version of the theorem is monotone under link restriction.

This already refutes a deterministic proof which simply reapplies the
diameter argument to every residual.  It does not by itself refute the
actual matching trajectory, because a matching residual is a special
vertex-induced restriction.  Equations (0.2) and (2.3) are the exact
additional trajectory information needed.

## 4. Near-parallel twins and the logarithmic-moment blind spot

Fix a labelled cyclic order \(P=(x_0,\ldots,x_{n-1})\).  Let \(s_i\)
swap the entries across one domino boundary, namely the adjacent positions
\((2i+1,2i+2)\), and put

\[
 F=Q(P),\qquad F_i=Q(P\circ s_i).
\]

### Lemma 4.1 (near-parallel twins)

For every \(i\),

\[
 |F\cap F_i|\ge K-8.                                    \tag{4.1}
\]

Moreover, for a fixed \(X\in F\), all but \(O(1)\) of the \(n/2\)
packets \(F_i\) contain \(X\).

#### Proof

Swapping two adjacent entries of a cyclic order changes exactly the two
length-\(R\) interval sets containing one swapped position but not the
other.  It leaves the other \(n-2\) interval sets unchanged.  After
conjugation by \(\tau\), the cross-boundary adjacent transposition becomes
a transposition of positions at cyclic distance three.  Such a
transposition changes exactly six length-\(R\) interval sets.  Comparing
the two components separately therefore gives at least
\((n-2)+(n-6)=K-8\) common targets, proving (4.1).  These packets are
distinct: a cross-boundary swap creates a boundary pattern which is not
obtained by independently swapping the fixed domino pairs.

A fixed ordinary interval is changed by at most two of the adjacent
cross-boundary swaps.  A fixed interval in the \(\tau\)-component is
changed by at most six of their distance-three conjugates.  Since the two
component traces are disjoint, every fixed target is therefore retained
by all but \(O(1)\) choices of \(i\).  \(\square\)

The use of cross-boundary swaps is essential.  Swapping a single fixed
domino pair actually preserves the whole twin support: it merely exchanges
two ordinary targets with their \(\tau\)-partners.  Thus the labelled
catalogue has at least \(2^{n/2}\), rather than merely polynomial, parallel
labels for one support.  Parallel labels must be collapsed in the simple
matching catalogue and must not be mistaken for distinct near-parallel
supports.

For completeness, the support multiplicity is only exponential in \(m\).
Writing \(R=2r+1\), every member of the position support is obtained from
\(r\) consecutive domino blocks by adjoining one element of one adjacent
boundary block.  A pair inside one domino occurs together in \(4r\)
members of the support.  This is the unique maximum pair-incidence value,
so the support recovers the domino partition.  Between two different
dominoes, the largest pair-incidence value is \(4r-2\), and it occurs
exactly for adjacent dominoes (the \(4r-4\) occurrences with both blocks
full, plus the two possible boundary-singleton occurrences).  Thus the
support also recovers the cyclic order of the blocks.  Its automorphism
group is therefore
contained in
\[
 (S_2)^m\rtimes D_m,
\]
and has size at most \(2^m(2m)\).  Hence collapsing parallel labels changes
\(\log D\) by only \(O(m)\), and the simple degree still satisfies
\[
 \log D=2m\log m-O(m).                                  \tag{4.1a}
\]

For a link pair put \(r(F,G)=|F\cap G|-1\), and define the independent
survivor overlap kernel

\[
 \Omega_{X,F}(z)=
 \frac1D\sum_{\substack{G\ni X\\G\ne F}}
 \bigl(z^{-r(F,G)}-1\bigr).                              \tag{4.2}
\]

Lemma 4.1 gives

\[
 \Omega_{X,F}(z)
 \ge\frac{n/2-O(1)}D\bigl(z^{-(K-9)}-1\bigr).           \tag{4.3}
\]

At \(z=m^{-1/2}\), \(K=4m\), and, in either the labelled or simple
normalization by (4.1a),

\[
 \log D=\log(2nR!(n-R)!)=2m\log m-2m+O(\sqrt m),
\]

so the right side of (4.3) is \(\exp[2m+O(\sqrt m)]\).
Thus product-style residual regeneration fails by an exponential margin.

On the other hand, for every \(p=O(\log m)\), the same near-parallel
pairs contribute only

\[
 \frac{O(n)K^p}{D}=\exp[-\Theta(m\log m)]                \tag{4.4}
\]

to the normalized factorial moment.  Hence all static logarithmic
diagrams may be correct while the deep survivor kernel is enormous.
This is a statewise explanation of why the static theorem cannot be
promoted to a stopped theorem by a formal moment argument.

More explicitly, the exact Newton expansion is

\[
 z^{-r}=
 \sum_{p=0}^{r}\frac{(r)_p}{p!}(z^{-1}-1)^p.             \tag{4.5}
\]

An epoch-restart proof based on the established moments would have to
truncate (4.5) at \(p=L=O(\log m)\) and declare the remainder negligible.
For the pairs in Lemma 4.1, \(r\ge K-9=\Theta(m)\), and that remainder is
\((1-o(1))z^{-r}\) at \(z=m^{-1/2}\).  Equation (4.3) shows that its
normalized contribution is exponentially large.  This is the first exact
inequality at which the logarithmic static hierarchy fails; no choice of
constants in \((Cp)^{Cp}m^{-2}\) repairs it.

## 5. An incidence-averaged quarantine sufficient condition

The following elementary reduction states what a positive dynamic theorem
may prove instead of pointwise heredity.

For a current center \(X\), call an incidence \((X,F)\) \(p\)-bad at
threshold \(b_p\) when

\[
 S_{p,t}(X,F)>b_p d_t(X).                                \tag{5.1}
\]

Then

\[
 \boxed{
 |\{F\in L_t(X):(X,F)\text{ is }p\text{-bad}\}|
 \le\frac{Z_{p,t}(X)}{b_p d_t(X)}.}                     \tag{5.2}
\]

Indeed, sum (5.1) over the bad rows and use the definition of \(Z_p\).
If all live degrees lie in \([d_*,Cd_*]\), summing (5.2) gives

\[
 \frac{\#\{p\text{-bad incidences}\}}
      {\#\{\text{live incidences}\}}
 \le
 \frac{C}{b_p}
 \frac{\sum_X Z_{p,t}(X)}{\sum_Xd_t(X)^2}.             \tag{5.3}
\]

Consequently a stopped maximal estimate of the form

\[
 \mathbb E\sup_{t\le\tau}
 \frac{\sum_XZ_{p,t}(X)}{\sum_Xd_t(X)^2}
 \le a_p                                                    \tag{5.4}
\]

allows analytical quarantine at any \(b_p\gg a_p\).  Deleting at the
end every selected packet carrying a bad incidence costs at most \(K\)
times the bad-incidence fraction.  Thus

\[
 \boxed{\frac{a_p}{b_p}=o(1/K)}                           \tag{5.5}
\]

is sufficient for an \(o(N)\) additional entrance leave.  A sharper
weighted version replaces counts in (5.3)--(5.5) by the actual selected
edge intensities and gives the same conclusion.

For the twin catalogue the time-zero value is

\[
 a_p\le(Cp)^{Cp}m^{-2}.
\]

Thus, absent the macroscopic-overlap effect, a threshold such as
\(b_p=m^{-1/2+o(1)}\) would leave ample room in (5.5).  Lemma 4.1 shows
why a proof of (5.4) must first quarantine or explicitly resolve
near-parallel packets: logarithmic factorial moments alone cannot do so.

## 6. Exact remaining theorem

A twin near-factor, and hence the desired linear repeat-excess
counterexample, follows from the following trajectory-specific statement:

1. the degree corridor survives to entrance leave \(o(N)\);
2. the marginal and common covariance sums in (2.3), stopped at
   \(B_X(e)\le\beta d_t(X)\), satisfy (5.4)--(5.5) through logarithmic
   factorial order; and
3. the macroscopic-overlap class from Lemma 4.1, and its finite-block
   generalizations, has incidence-weighted selected mass \(o(N/K)\).

The first two clauses are the local ACLE hierarchy.  The third is not
contained in it: it is an all-scale cluster quarantine.  This is now the
precise dynamic gate.  Classical Pippenger--Spencer, maximum codegree,
and the static \(K_{2,\ell}\) theorem do not supply it.
