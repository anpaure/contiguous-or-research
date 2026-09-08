# Pair-radius nested bonus families and aligned Johnson endpoint rows

Date: 2026-07-26

Method: pure mathematics only.

## 0. Outcome

Fix a partition of the \(2m\) coordinates into \(m\) unordered pairs.
For a set \(T\), let

\[
                         d(T)=\#\{\text{pairs contained in }T\}.            \tag{0.1}
\]

The pair-radius filtration gives a positive answer to the proposed
joint-bonus-family strategy, in an approximate-quota range almost as large
as \(\sqrt m\).

For

\[
 H=o\!\left(\sqrt{m/\log m}\right),                \tag{0.2}
\]

there are nondecreasing integer thresholds \(r_1\le\cdots\le r_H\) such
that the lower bonus families

\[
 {\cal H}_q^-=\left\{T\in\binom{[2m]}{m-q}:d(T)\le r_q\right\}             \tag{0.3}
\]

have the balanced bonus sizes

\[
 s_q=W-N_q,\qquad N_q=\binom{2m}{m-q},              \tag{0.4}
\]

up to aggregate error \(o(W)\).  Define the upper families by complement,

\[
 {\cal H}_q^+=\{U:[2m]\setminus U\in{\cal H}_q^-\}.                       \tag{0.5}
\]

Then:

1. the lower families are closed under every one-step lower shadow and
   the upper families under every one-step upper shadow;
2. on every return-free endpoint suffix, their forbidden-row envelopes
   are nested in \(q\), as are their forbidden-column envelopes;
3. consequently the union over all \(q\le H\) costs only the terminal
   envelope, not a sum of \(H\) marginal costs;
4. on a uniform relative coordinate orbit of suffixes against the fixed
   pair frame (equivalently, a uniform relative pair frame against a fixed
   suffix),
   \[
    \mathbb E\left(\left|\bigcup_q{\cal R}_q\right|
                  +\left|\bigcup_q{\cal C}_q\right|\right)
    \le (2+o(1))H^2,                                \tag{0.6}
   \]
   improving the unrestricted \(\Theta(H^3)\) incidence moment;
5. all families are exactly point-regular, and the two signs lie on the
   same complementary rational point-margin line.  Rounding that line to
   one integer common run vector costs only an \(o(W)\) exceptional target
   ledger.

Thus, for every fixed \(c<1/2\), the construction gives

\[
                         H=m^c                     \tag{0.7}
\]

with \(m-o(m)\) simultaneous row and column slack on all but \(o(1)\) of
the relative-orbit shores.

There is a precise caveat.  Whenever \(r_{q+1}>r_q\), a target with

\[
                         r_q<d(T)\le r_{q+1}        \tag{0.8}
\]

can have its entire lower shadow inside \({\cal H}_{q+1}^-\); this is the
shadow-lock obstruction.  The aggregate density of all such transition
bands telescopes to

\[
                         O(H^2/m)=o(1).             \tag{0.9}
\]

Targets with too few singleton pairs form an exponentially small further
exception.  Therefore the locked targets may be charged to the allowed
\(o(W)\) target error.  Outside those exceptions every demanded target has
\(\Omega(m)\) unsaturated shadow exits, provided saturation is confined to
the nested bonus families.

The elementary additive-hash interval proposal does not have this
property.  Suffix-dependent translations destroy interval nesting unless
the intervals expand by every coordinate-label direction; the common
run-vector theorem does not control those partial sums.  Section 2 gives
the exact obstruction.

This note constructs compatible target-load profiles and proves the
endpoint-row theorem.  It does not construct the integral \(H\)-safe
Hamilton chronology realizing those profiles.

## 1. Endpoint traces and what nesting must mean

Let

\[
 P=(X_{-H+1},\ldots,X_0)                            \tag{1.1}
\]

be a return-free suffix and put \(X=X_0\).  Let
\(b_1,b_2,\ldots,b_{H-1}\) be its inserted coordinates, listed backwards
from the endpoint, and let \(a_1,a_2,\ldots,a_{H-1}\) be the corresponding
removed coordinates.  For an eligible next removal \(a\) and insertion
\(b\), the new signed targets are

\[
\begin{aligned}
 L_q(a)&=I_{q-1}-a,\\
 I_{q-1}&=X-\{b_1,\ldots,b_{q-1}\},                 \tag{1.2}\\
 U_q(b)&=J_{q-1}+b,\\
 J_{q-1}&=X\cup\{a_1,\ldots,a_{q-1}\}.             \tag{1.3}
\end{aligned}
\]

In particular,

\[
 L_{q+1}(a)=L_q(a)-b_q,\qquad
 U_{q+1}(b)=U_q(b)+a_q.                             \tag{1.4}
\]

Suppose bonus envelopes satisfy

\[
 \partial{\cal H}_q^-\subseteq{\cal H}_{q+1}^-,\qquad
 \nabla{\cal H}_q^+\subseteq{\cal H}_{q+1}^+.      \tag{1.5}
\]

Define their endpoint row and column envelopes by

\[
\begin{aligned}
 E_q^-(P)&=\{a:L_q(a)\in{\cal H}_q^-\},\\
 E_q^+(P)&=\{b:U_q(b)\in{\cal H}_q^+\}.            \tag{1.6}
\end{aligned}
\]

Equation (1.4) and (1.5) give the exact, pointwise nesting

\[
 E_1^-(P)\subseteq\cdots\subseteq E_H^-(P),\qquad
 E_1^+(P)\subseteq\cdots\subseteq E_H^+(P).        \tag{1.7}
\]

If every doubled target at depth \(q\) belongs to
\({\cal H}_q^\pm\), the actual forbidden sets satisfy

\[
 \boxed{
 \bigcup_{q\le H}{\cal R}_q(P)\subseteq E_H^-(P),\qquad
 \bigcup_{q\le H}{\cal C}_q(P)\subseteq E_H^+(P).}              \tag{1.8}
\]

This is the desired correlation.  It is a deterministic implication on
one suffix; no marginal densities are multiplied.

## 2. Why one additive interval hash does not give (1.5)

Let \(h:[2m]\to G\) label coordinates in an abelian group and extend it
additively to subsets.  Let

\[
 {\cal K}_q^- =\{T:h(T)\in A_q\}.                  \tag{2.1}
\]

At the endpoint suffix,

\[
 h(L_q(a))
 =h(X)-\sum_{i<q}h(b_i)-h(a).                      \tag{2.2}
\]

Put

\[
 c_q(P)=h(X)-\sum_{i<q}h(b_i).                     \tag{2.3}
\]

Then the forbidden coordinate labels at depth \(q\) form the translate

\[
                         c_q(P)-A_q.                \tag{2.4}
\]

Since \(c_{q+1}=c_q-h(b_q)\), universal nesting of these translates for
every return-free suffix requires

\[
                         A_q-h(v)\subseteq A_{q+1} \tag{2.5}
\]

for every label \(h(v)\) which may occur as the next insertion.

### Proposition 2.1 (additive expansion obstruction)

Let \(G=\mathbb Z_p\) with \(p\) prime, and let
\(S=h([2m])\).  If (2.5) holds through depth \(H\), then, before wraparound,

\[
                         |A_q|\ge |A_1|+(q-1)(|S|-1).             \tag{2.6}
\]

In particular, an injective or high-entropy coordinate hash forces the
bonus interval to occupy all of \(G\) after very few depths.  If
\(|S|=1\), the hash is constant on each rank and cannot resolve a
nontrivial bonus fraction.

#### Proof

Iterating (2.5) gives

\[
 A_q\supseteq A_1-(q-1)S.
\]

The Cauchy--Davenport inequality, applied repeatedly, gives

\[
 |A_1-(q-1)S|
 \ge\min\{p,|A_1|+(q-1)(|S|-1)\},
\]

which is (2.6). \(\square\)

For a single fixed suffix the translates in (2.4) may instead drift in
different directions and have nearly disjoint unions.  The common
coordinate-run vector fixes total point margins over the whole cycle, but
does not fix the ordered partial sums in (2.3).  Thus point-margin
compatibility alone does not repair the additive hash.

## 3. The pair-radius filtration

Fix pairs

\[
                         M_i=\{x_i,y_i\},\qquad 1\le i\le m.     \tag{3.1}
\]

For \(T\subseteq[2m]\), let \(d(T)\) be the number of pairs with two
members in \(T\), \(e(T)\) the number with no members in \(T\), and
\(s(T)\) the number with one member in \(T\).

If \(|T|=m-q\), then

\[
 e(T)-d(T)=q,\qquad s(T)=m-q-2d(T).                 \tag{3.2}
\]

Deleting one coordinate has the exact effect

\[
 d(T-v)=
 \begin{cases}
 d(T)-1,&v\text{ lies in a double pair of }T,\\
 d(T),&v\text{ lies in a singleton pair of }T.
 \end{cases}                                       \tag{3.3}
\]

Thus \(d\) never increases under deletion.  Consequently, for any
nondecreasing threshold sequence \(r_q\), the families (0.3) satisfy

\[
                         \partial{\cal H}_q^-
                         \subseteq{\cal H}_{q+1}^-.              \tag{3.4}
\]

Complementation turns (3.4) into the upper-shadow inclusion for (0.5).
Hence (1.7)--(1.8) hold for every return-free suffix.

This statistic is the radius from the transversal layer in the product
decomposition associated with the pair matching.  It is therefore an
SCD-radius filtration rather than an additive hash.

## 4. Exact radius distribution and monotone quantiles

Let \(D_q=d(T)\) for a uniform
\(T\in\binom{[2m]}{m-q}\).  Its exact mass function is

\[
 \mathbb P(D_q=d)
 ={A_{q,d}\over N_q},                               \tag{4.1}
\]

where

\[
 A_{q,d}
 ={m!\,2^{m-q-2d}\over
   d!\,(q+d)!\,(m-q-2d)!}.                         \tag{4.2}
\]

Indeed, choose the \(d\) double pairs, the \(q+d\) empty pairs, and one
of two coordinates from every remaining singleton pair.

Successive masses obey

\[
 {A_{q,d+1}\over A_{q,d}}
 ={(m-q-2d)(m-q-2d-1)
   \over4(d+1)(q+d+1)}.                             \tag{4.3}
\]

Thus the law is log-concave and has mode

\[
 d_q^*={m\over4}-{q\over2}+{q^2\over4m}+O(1).      \tag{4.4}
\]

Let

\[
 F_q(r)=\mathbb P(D_q\le r),\qquad
 \theta_q={W-N_q\over N_q}={W\over N_q}-1.         \tag{4.5}
\]

In the range (0.2), \(m^{-1}\le\theta_q=o(1)\) and

\[
                         \theta_q=(1+o(1)){q^2\over m}.          \tag{4.6}
\]

There is an exact deletion coupling.  Delete a uniformly chosen element
from a uniform \((m-q)\)-set.  The result is uniform at rank
\(m-q-1\), and (3.3) gives

\[
 F_{q+1}(r)
 =F_q(r)+\mathbb P(D_q=r+1){2(r+1)\over m-q}.       \tag{4.7}
\]

### Lemma 4.1 (monotone quota quantiles)

Assume (0.2).  There are nondecreasing integers
\(r_1\le\cdots\le r_H\) such that, uniformly for \(q\le H\),

\[
 0\le F_q(r_q)-\theta_q
 \le C\theta_q\sqrt{\log m\over m}.                \tag{4.8}
\]

Moreover, for every fixed integer \(t\ge0\) with \(q+t\le H\),

\[
 F_q(r_{q+t})
 =\theta_{q+t}
  +O_t\!\left(\theta_{q+t}\sqrt{\log m\over m}\right).         \tag{4.9}
\]

#### Proof

Take \(r_q\) to be the least integer with \(F_q(r_q)\ge\theta_q\).
We record the standard elementary estimate needed for this quantile.
From the ratio (4.3), summing logarithms outward from the mode (4.4)
shows that, whenever

\[
 m^{-1}\le F_q(r)\le o(1),
\]

one has

\[
 {\mathbb P(D_q=r)\over F_q(r)}
 \le C\sqrt{\log m\over m}.                        \tag{4.10}
\]

For completeness, the quantile in this probability range is at distance
\(O(\sqrt{m\log m})\) below the mode: multiplying the ratios in (4.3)
gives upper and lower bounds
\(\exp(-C_2t^2/m)\) and \(\exp(-c_2t^2/m)\) at distance \(t\); summing the
preceding masses gives a tail-to-boundary ratio
\(\Omega(\sqrt m/(1+t/\sqrt m))\).  This proves (4.10).  The overshoot of
the least quantile is at most its boundary atom, proving (4.8).

It remains to prove monotonicity.  The exact cap ratios satisfy

\[
 \theta_{q+1}-\theta_q
 =(1+\theta_q){2q+1\over m-q}.                      \tag{4.11}
\]

At \(r=r_q-1\), equations (4.7) and (4.10) show

\[
 F_{q+1}(r)
 \le\theta_q
   +C\theta_q\sqrt{\log m\over m}.
\]

The error divided by the increment in (4.11) is
\(O(q\sqrt{\log m/m})=o(1)\), uniformly under (0.2).  Hence
\(F_{q+1}(r_q-1)<\theta_{q+1}\) for all sufficiently large \(m\), so the
least \(\theta_{q+1}\)-quantile satisfies \(r_{q+1}\ge r_q\).

Finally iterate (4.7) a fixed number \(t\) of times.  Every added boundary
atom satisfies (4.10), and (4.8) at depth \(q+t\) then gives (4.9).
\(\square\)

The total cardinal error of the families (0.3) is therefore

\[
\begin{aligned}
 \sum_{q\le H}\bigl||{\cal H}_q^-|-s_q\bigr|
 &\le CW\sqrt{\log m\over m}\sum_{q\le H}\theta_q\\
 &\le CW{H^3\sqrt{\log m}\over m^{3/2}}
 =o(W),                                             \tag{4.12}
\end{aligned}
\]

and the same holds for the upper sign.

## 5. Exact union of forbidden rows and columns

Let \(\widetilde r_1\le\cdots\le\widetilde r_H=r_H\), put

\[
 \widetilde{\cal H}_q^-=
 \{T:d(T)\le\widetilde r_q\},
 \qquad
 \widetilde{\cal H}_q^+=
 \{U:[2m]\setminus U\in\widetilde{\cal H}_q^-\},   \tag{5.1}
\]

and suppose the actual doubled-target families satisfy

\[
                         D_q^\pm\subseteq\widetilde{\cal H}_q^\pm.         \tag{5.2}
\]

By (1.8), only the depth-\(H\) envelopes need be considered.  These are
the original quantile families because \(\widetilde r_H=r_H\).

Put \(I=I_{H-1}(P)\), so \(|I|=m-H+1\), and write \(d=d(I)\).  For an
eligible removal \(a\), (3.3) gives the exact trichotomy

\[
 |E_H^-(P)|=
 \begin{cases}
 |A(P)|,&d\le r_H,\\
 |A(P)\cap Q(I)|,&d=r_H+1,\\
 0,&d\ge r_H+2,
 \end{cases}                                       \tag{5.3}
\]

where \(Q(I)\) is the set of coordinates lying in double pairs of \(I\).
In particular,

\[
 |E_H^-(P)|\le
 \begin{cases}
 |A(P)|,&d\le r_H,\\
 2(r_H+1),&d=r_H+1,\\
 0,&d\ge r_H+2.
 \end{cases}                                       \tag{5.4}
\]

For the upper sign, take the complement of \(J_{H-1}(P)\).  Candidate
insertions become deletions from this complement, so the identical
trichotomy holds for \(E_H^+(P)\).

### Theorem 5.1 (quadratic correlated-row moment)

On a uniform coordinate orbit of return-free endpoint suffixes relative to
the fixed pair frame,

\[
\begin{aligned}
 \mathbb E\left|\bigcup_{q\le H}{\cal R}_q(P)\right|
 &\le(m-H+1){|{\cal H}_H^-|\over N_H},\\
 \mathbb E\left|\bigcup_{q\le H}{\cal C}_q(P)\right|
 &\le(m-H+1){|{\cal H}_H^+|\over N_H}.             \tag{5.5}
\end{aligned}
\]

Consequently,

\[
 \mathbb E\left(\left|\bigcup_q{\cal R}_q\right|
                 +\left|\bigcup_q{\cal C}_q\right|\right)
 \le(2+o(1))H^2.                                   \tag{5.6}
\]

Within the construction range (0.2), every \(\eta=\eta(m)\) satisfying
\(H^2/(\eta m)\to0\) has the following property: a \(1-o(1)\) fraction
of the orbit shores have at least

\[
                         (1-\eta)m-H+1              \tag{5.7}
\]

simultaneously available rows and columns.

#### Proof

The deterministic inclusions (1.8) reduce each union to its terminal
envelope.  For a uniform rank-\((m-H+1)\) parent \(I\), double counting
the deletion incidences into \({\cal H}_H^-\) gives

\[
 \mathbb E|E_H^-|
 =(m-H+1){|{\cal H}_H^-|\over N_H}.
\]

Restricting to eligible rows can only decrease the count.  The upper proof
is its complement.  Equations (4.6) and (4.8) give
\(|{\cal H}_H^\pm|/N_H=(1+o(1))H^2/m\), proving (5.6).  Apply Markov's
inequality to the one joint sum in (5.6), then use
\(|A(P)|,|B(P)|\ge m-H+1\). \(\square\)

Again, (5.6) is not a product of marginal estimates.  It follows from a
pointwise nesting of all depth constraints on the same endpoint matrix.

## 6. Exact point-margin compatibility

Let \(G\) be the wreath group generated by arbitrary permutations of the
\(m\) coordinate pairs and independent swaps inside the pairs.  It is
transitive on the \(2m\) coordinates and preserves \(d(T)\).  Hence every
family \({\cal H}_q^-\) is point-regular:

\[
 \#\{T\in{\cal H}_q^-:v\in T\}
 ={m-q\over2m}|{\cal H}_q^-|                       \tag{6.1}
\]

for every coordinate \(v\).  By complementation,

\[
 \#\{U\in{\cal H}_q^+:v\in U\}
 ={m+q\over2m}|{\cal H}_q^+|.                      \tag{6.2}
\]

If \(|{\cal H}_q^\pm|=s_q\), adding one bonus occurrence on every target
in these families to the all-one baseline gives

\[
\begin{aligned}
 \sum_{T\ni v}\mu_q^-(T)
 &={m-q\over2m}(N_q+s_q)
 ={W\over2}-q{W\over2m},\\
 \sum_{U\ni v}\mu_q^+(U)
 &={m+q\over2m}(N_q+s_q)
 ={W\over2}+q{W\over2m}.                           \tag{6.3}
\end{aligned}
\]

These are the common-run-vector identities on the symmetric rational line

\[
                         R_v={W\over2m}\qquad(v\in[2m]).        \tag{6.4}
\]

The quantity in (6.4) need not be integral.  Write

\[
 W=2mR_0+s,\qquad 0\le s<2m,                         \tag{6.5}
\]

and choose one common integer run vector with \(s\) entries \(R_0+1\)
and \(2m-s\) entries \(R_0\).  Replacing (6.4) by this vector changes the
required signed point margin of coordinate \(v\) by at most \(q\) at
depth \(q\).  The total arithmetic correction over all coordinates and
depths is polynomial in \(m,H\), hence \(o(W)\).  The quantile cardinal
error (4.12) is also \(o(W)\) in target occurrences.  Therefore there is
no asymptotic point-margin obstruction to this nested filtration.

This is a compatibility statement, not an integral realization theorem:
an exact nonnegative correction by physical Johnson windows is part of the
remaining chronology problem.  What is already exact is the complementary
relation between the two signs and the use of one common centered run line;
the depthwise high families have not been chosen independently.

## 7. Shadow lock and an approximate repair

The same nesting which aligns endpoint rows can lock a target.  If

\[
 T\notin{\cal H}_q^-,\qquad
 \partial T\subseteq{\cal H}_{q+1}^-,              \tag{7.1}
\]

then no appended occurrence of \(T\) is possible after all of
\({\cal H}_{q+1}^-\) has saturated.

By (3.3), condition (7.1) can occur only in the transition band

\[
 {\cal B}_q=\{T:r_q<d(T)\le r_{q+1}\},             \tag{7.2}
\]

apart from targets with no singleton pair.  Stochastic domination and
Lemma 4.1 give

\[
\begin{aligned}
 {|{\cal B}_q|\over N_q}
 &=F_q(r_{q+1})-F_q(r_q)\\
 &\le \theta_{q+1}-\theta_q
  +O\!\left(\theta_{q+1}\sqrt{\log m\over m}\right).           \tag{7.3}
\end{aligned}
\]

Therefore the bands telescope:

\[
 \sum_{q<H}|{\cal B}_q|
 \le W\theta_H
 +O\!\left(W{H^3\sqrt{\log m}\over m^{3/2}}\right)
 =o(W).                                             \tag{7.4}
\]

The sets with fewer than \(m/4\) singleton pairs have exponentially small
density.  This follows directly from (4.2)--(4.3), since the typical
singleton count is \(m/2+O(H)\), while \(s(T)<m/4\) places \(d(T)\) a
linear distance above the mode.

Consequently, outside an \(o(W)\) aggregate family, every nonbonus target
\(T\) has at least \(m/4\) singleton coordinates \(v\) for which

\[
                         T-v\notin{\cal H}_{q+1}^-.              \tag{7.5}
\]

The upper statement follows by complement.

There is a conserved approximate repair which also keeps every doubled
target inside a nested envelope.  Fix the look-ahead constant \(L=4\) and
put

\[
 \bar r_q=r_{\min\{q+L,H\}},\qquad
 \overline{\cal H}_q^-
 =\{T:d(T)\le\bar r_q\}.                            \tag{7.6}
\]

Use complements for the upper sign.  The thresholds \(\bar r_q\) are
still nondecreasing, and \(\bar r_H=r_H\).  Thus the deterministic union
bound (1.8) and the terminal moment (5.6) are unchanged.

Let

\[
 h_q=|\overline{\cal H}_q^-|,
 \qquad x_q=h_q-s_q.                                \tag{7.7}
\]

By the fixed-shift estimate (4.9), uniformly away from the last \(L\)
depths,

\[
 {x_q\over N_q}
 ={(q+4)^2-q^2\over m}(1+o(1))
 ={8q+16\over m}(1+o(1)).                          \tag{7.8}
\]

The targets outside the new envelope which can be locked by the next new
envelope lie in

\[
 \overline{\cal B}_q
 =\{T:\bar r_q<d(T)\le\bar r_{q+1}\}.              \tag{7.9}
\]

For \(q+L+1\le H\), again by (4.9),

\[
 {|\overline{\cal B}_q|\over N_q}
 ={2q+9\over m}(1+o(1)).                            \tag{7.10}
\]

For the last \(L\) depths this band is empty.  Hence (7.8) dominates
(7.10) for every \(q\ge1\) and all sufficiently large \(m\).  The
exponentially small family with fewer than \(m/4\) singleton pairs can be
included as well.  It follows that one may choose a hole family
\({\cal Z}_q^-\), disjoint from \(\overline{\cal H}_q^-\), such that

\[
 \overline{\cal B}_q\subseteq{\cal Z}_q^-,
 \qquad |{\cal Z}_q^-|=x_q+O(m),                   \tag{7.11}
\]

and \({\cal Z}_q^-\) also contains every low-singleton exception.

The \(O(m)\) rounding in (7.11) can be made point-regular before the last
exceptional orbit.  Indeed, the cyclic subgroup which rotates the \(m\)
pairs and globally swaps their two shores is transitive on all \(2m\)
coordinates and preserves every radius layer.  Taking complete orbits
changes a desired cardinality by at most \(2m\), while keeping every point
degree equal.

Define the formal lower load profile

\[
 \mu_q^-(T)=
 \begin{cases}
 2,&T\in\overline{\cal H}_q^-,\\
 0,&T\in{\cal Z}_q^-,\\
 1,&\text{otherwise},
 \end{cases}                                       \tag{7.12}
\]

and define the upper profile by complementation.  Ignoring the final
\(O(m)\) orbit rounding, (7.7) gives

\[
 \sum_T\mu_q^-(T)=N_q+h_q-x_q=N_q+s_q=W.           \tag{7.13}
\]

Thus the holes are exactly compensated by extra double loads, and every
double load lies in the nested envelope.  Both the doubled and hole
families are point-regular, so their point contributions cancel to the
same rational common-run line in Section 6.  The final orbit rounding over
all depths costs only \(O(mH)=o(W)\).

Finally, the fixed shifts telescope:

\[
 \sum_{q\le H}x_q
 =O(W\theta_H)
 +O\!\left(W{H^3\sqrt{\log m}\over m^{3/2}}\right)
 =O\!\left(W{H^2\over m}\right)+o(W)=o(W).          \tag{7.14}
\]

The \(L^1\) target error of (7.12) from a balanced one/two profile is at
most \(2\sum_qx_q+O(mH)=o(W)\).

For \(q<H\), every target which is neither a bonus nor a hole has more
than \(\bar r_{q+1}\) double pairs and at least \(m/4\) singleton pairs.
Deleting any of those singleton coordinates leaves the radius unchanged
and outside the next bonus envelope.  Hence it has at least \(m/4\)
literal shadow escapes.  This removes the shadow-lock obstruction for all
nonexceptional demanded targets of the approximate profile.

If exact coverage is demanded, the filtration alone still does not solve
the exceptional \(o(W)\) ledger; a relative seam orbit or a separate
fibrewise absorber is then necessary.

## 8. What is proved and what remains

The pair-radius construction proves the following deterministic target
design theorem.

> For \(H=o(\sqrt{m/\log m})\), there are jointly chosen lower and upper
> bonus envelopes with aggregate quota error \(o(W)\), compatibility with
> one common point-margin line up to an \(o(W)\) exceptional correction,
> and shadow nesting such that the union of
> all endpoint forbidden rows and columns has joint expectation
> \((2+o(1))H^2\).  All but \(o(W)\) potentially demanded targets have
> \(\Omega(m)\) one-step shadow escape.

This improves the generic correlated-row window from \(H=o(m^{1/3})\) to
every fixed power \(H=m^c\), \(c<1/2\), at the target-profile level.

The missing theorem is chronological: construct an integral \(H\)-safe
Johnson cycle factor whose doubled targets stay inside these envelopes,
whose exceptional loads have total \(o(W)\), and whose component count is
small enough for an \(o(W)\) seam merge.  Neither the nested filtration nor
the common run-vector identity alone supplies that owner permutation.
