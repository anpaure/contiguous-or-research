# Rail-extended queues close the full owner/lower/upper system fractionally

**Date:** 2026-08-07  
**Method:** one cyclic sequence of unique toggle labels, read through a
longer owner window, plus a tiny full-ground rail reserve  
**Status:** unconditional local theorem and all-rank fractional
correlation theorem.  The same literal component family simultaneously
carries flat simple owners, exact monotone-rotor lower marginals, both
immediate palettes, residence, regeneration, and fractional coverage of
every upper rank.  Integral owner/target-once rounding, component fusion,
and the common compiler remain open.

## 1. One construction for all rail lengths

Fix trace depth \(d\ge2\), owner rank \(R\), and

\[
 0\le a\le d,
 \qquad p=d-a+1.
\tag{1.1}

Choose positive weights

\[
 h_0,\ldots,h_{p-1}\ge1,qquad H=\sum_i h_i\le R-a.
\tag{1.2}

Let \(L\ge2\) satisfy

\[
 Lp\ge2(d+2).
\tag{1.3}

On pairwise disjoint coordinate sets choose

\[
 |K|=R-a-H,qquad |P_i|=h_i-1,qquad
 X_i=\{x_{i,0},\ldots,x_{i,L-1}\}.
\tag{1.4}

The used universe has size

\[
 U=R-a+p(L-1).
\tag{1.5}

Define the period-\(Lp\) source word

\[
 \boxed{A_{up+i}=K\cup P_i\cup\{x_{i,u}\}}
 \qquad(u\in\mathbb Z_L,\ 0\le i<p).
\tag{1.6}

The cases have the following meanings:

* \(a=0\): an ordinary positive-composition rotor;
* \(1\le a<d\): a mixed rotor with a terminal \(1^a\) rail;
* \(a=d,p=1,h_0=1\): the pure saturated singleton rail.

Write \(Z_{t,j}=\bigcup_{v=0}^{j-1}A_{t-v}\).

## 2. Full interval spectrum

### Theorem 2.1 (unified rail queue)

The word (1.6) has the following exact properties.

1. Every owner \(Z_{t,d+1}\) has rank \(R\); the owners are distinct and
   form a simple Johnson cycle.
2. Both immediate owner palettes are simple and have ranks \(R-1\) and
   \(R+1\).
3. Every toggle coordinate has owner run \(d+1\) and owner gap
   \(Lp-(d+1)\ge d+3\).  All \(K\)- and \(P_i\)-coordinates are
   permanent in the owner row.
4. The age composition at endpoint \(up+i\) is

   \[
   \boxed{
   (R-a-H+h_i,h_{i-1},\ldots,h_{i-(p-1)},1^a).}
   \tag{2.1}
   \]

5. Every interval value \(Z_{t,j}\), \(1\le j<Lp\), determines
   \((t,j)\).  Hence the complete proper interval deck of the component is
   simple.
6. Its ranks are

   \[
   |Z_{t,j}|=R-a-H+\sum_{v=0}^{j-1}h_{i-v}
   \qquad(1\le j<p),
   \tag{2.2}
   \]

   and

   \[
   \boxed{|Z_{t,j}|=R-a-p+j}
   \qquad(p\le j\le Lp).
   \tag{2.3}
   \]

   In particular the upper interval ranks after the owner are precisely

   \[
   R+1,R+2,\ldots,U.
   \tag{2.4}
   \]

   Below rank \(U\), these give one distinct target value per endpoint.
   At rank \(U\), the interval is the full period and all endpoints give
   the same used-universe target, so there is one distinct rank-\(U\)
   target value per component.

7. The complete literal state regenerates after \(Lp\) positions.

#### Proof

The toggle labels

\[
 x_{0,0},x_{1,0},\ldots,x_{p-1,0},
 x_{0,1},\ldots,x_{p-1,L-1}
\tag{2.5}
\]

form one labelled cyclic order of length \(Lp\), and every source
position contains its unique corresponding toggle.  A source interval of
length below \(Lp\) therefore contains a unique proper cyclic interval of
toggle labels; that toggle interval alone recovers its start, end, and
length.

If \(j<p\), its active phases are distinct and (2.2) follows.  If
\(j\ge p\), every phase occurs, so the interval contains \(K\), all the
\(P_i\), and exactly \(j\) toggle labels.  Its rank is

\[
 (R-a-H)+(H-p)+j=R-a-p+j,
\]

proving (2.3) and interval simplicity.

At \(j=d+1=p+a\), equation (2.3) gives rank \(R\).  Advancing the window
deletes its first unique toggle and inserts the next unique toggle.  The
sets \(K,P_0,\ldots,P_{p-1}\) remain in both windows, so this is one
Johnson swap.  The owner row is simple by the toggle-interval decoder.

The intersection and union of consecutive owners consist of the same
permanent bank together with, respectively, \(d\) and \(d+2\)
consecutive toggle labels.  They therefore have ranks \(R-1,R+1\) and are
simple.  A toggle occurrence belongs to the next \(d+1\) owner windows
and no others in its period, proving residence.

The most recent \(p\) positions give the reduced positive-composition age
classes; each of the preceding \(a\) positions repeats its phase bank but
adds one old unique toggle.  This is (2.1).  Periodicity proves Item 7.
\(\square\)

This proof contains the binary-toggle and delayed-multistate constructions
as special cases, but also records their full upper interval spectra.

## 3. Maximal clocks miss fewer than \(d+1\) coordinates

Embed the component into a \(k\)-coordinate ground set.  For fixed
\((a,p)\), choose the maximal clock

\[
 L_{\max}=1+\left\lfloor\frac{k-R+a}{p}\right\rfloor.
\tag{3.1}

For all sufficiently large \(k\), it satisfies (1.3).  Put

\[
 r_a=(k-R+a)\bmod p.
\tag{3.2}

Then the used universe is exactly

\[
 \boxed{U=k-r_a,\qquad0\le r_a<p\le d+1.}
\tag{3.3}

Thus every maximal component covers every upper rank through at least
\(k-d\).

The pure rail \(a=d,p=1,h_0=1\) has \(r_a=0\), uses all \(k\)
coordinates, and has age profile

\[
 (R-d,1^d),
\tag{3.4}

the short-clock vertex \(v_d\).

## 4. An exponentially tiny full-ground reserve covers the top tail

Use the optimal Ferrers residual vector

\[
 q_s=\frac{{k\choose s}-b_s}{W},
 \qquad W={k\choose R},
 \qquad R=\left\lceil\frac k2\right\rceil.
\tag{4.1}

For all sufficiently large \(k\), the Ferrers correction is supported far
below ranks \(R-d-1,R-d\).  Put

\[
 \alpha_d=q_{R-d}-q_{R-d-1}
 =\frac{{k\choose R-d}-{k\choose R-d-1}}W.
\tag{4.2}

Then

\[
 \alpha_d=\Theta(d^{-1}),
\tag{4.3}

whereas

\[
 \delta:=\frac{{k\choose d}}W=e^{-\Theta(k)}.
\tag{4.4}

In particular \(0<\delta<\alpha_d\) for all sufficiently large \(k\).

Subtract \(\delta v_d\) and renormalize:

\[
 q'=\frac{q-\delta v_d}{1-\delta}.
\tag{4.5}

The inequality \(\delta\le\alpha_d\) preserves monotonicity at the only
new boundary, and all other defining inequalities of
\(\mathcal M_{R,d}\) are immediate.  Hence

\[
 q'\in\mathcal M_{R,d}.
\tag{4.6}

Realize the \(\delta v_d\) mass with full-ground pure rails, and realize
\((1-\delta)q'\) with maximal-clock queue components from Theorem 2.1.

## 5. Full fractional Shadow--Braid factor

### Theorem 5.1 (all-rank owner-correlated fractional factor)

For all sufficiently large \(k\), there is a symmetric fractional mixture
of literal rail-queue components such that, simultaneously:

1. every rank-\(R\) owner has load exactly one;
2. together with the Ferrers boundary, every strict-lower target has
   designated load exactly one;
3. every target of every rank \(R+1,\ldots,k\) has load at least one;
4. both selected immediate owner-palette rows have their exact uniform
   loads

   \[
   \frac W{\binom{k}{R-1}},
   \qquad
   \frac W{\binom{k}{R+1}};
   \tag{5.1}
   \]

5. every component is a simple Johnson owner cycle with two-sided owner
   residence and a simple proper interval deck.

#### Proof

The owner/lower assertions follow from the owner-simple monotone-rotor
theorem and symmetric coordinate averaging.  Give type \(c\), of endpoint
length \(N_c\), endpoint mass \(W\lambda_c\) and component mass
\(W\lambda_c/N_c\).  This gives total owner mass \(W\) and designated
marked rank-\(s\) mass \(Wq_s\), exactly complementary to the Ferrers
boundary.  Incidental unmarked physical lower cells are not included in
this designated-load equality.

Every maximal component has universe rank at least \(k-d\).  For

\[
 R+1\le u\le k-d-1,
\]

its rank-\(u\) interval is proper and supplies one distinct target value
per endpoint.  The total endpoint mass is \(W\), so every target at such a
rank has uniform load

\[
 \frac W{\binom{k}{u}}\ge1.
\tag{5.2}

The full-ground rail reserve has endpoint mass

\[
 \delta W={k\choose d}.
\]

For \(k-d\le u<k\), its rank-\(u\) intervals are proper and distinct over
the endpoints.  Hence every rank-\(u\) target has load

\[
 \frac{\binom{k}{d}}{\binom{k}{u}}
 =\frac{\binom{k}{d}}{\binom{k}{k-u}}\ge1.
\tag{5.3}
\]

At rank \(k\), all full-period intervals in one pure-rail component are
the same target \([k]\), so they must be counted once per component, not
once per endpoint.  The pure-rail period is

\[
 N_*=1+k-R+d.
\]

Its load on \([k]\) is therefore

\[
 \frac{\delta W}{N_*}
 =\frac{\binom{k}{d}}{1+k-R+d}\ge1
\tag{5.4}
\]

for all sufficiently large parameters.  This proves Item 3 without
counting the repeated full-period universe as distinct occurrences.

Every component has one lower and one upper immediate colour per owner,
and each selected local palette list is simple.  Symmetry therefore gives
(5.1).  Incidental nonselected or boundary cells are outside these palette
equalities.  Item 5 is Theorem 2.1. \(\square\)

## 6. Exact remaining theorem

This removes, in one correlated literal family, all of the following
fractional obstructions:

\[
 \boxed{
 \text{owner mass, triangular lower mass, all upper ranks, immediate
 palettes, owner residence, and local topology.}}
\]

It still does not prove \(\nu(k)\le B(k)+O(1)\).  The remaining step is
integral and occurrence-labelled:

> Round the rail-queue mixture so every named owner and designated lower
> target occurs once, fuse the resulting cycles without losing the upper
> interval witnesses, and retain one common compiler/Ferrers cap.

The construction shows that no scalar rank marginal, local history,
residence, immediate-palette, or arbitrary-upper marginal can separate the
desired object.  Any remaining obstruction lies in integral multi-resource
rounding, fusion, or the terminal common cap.
