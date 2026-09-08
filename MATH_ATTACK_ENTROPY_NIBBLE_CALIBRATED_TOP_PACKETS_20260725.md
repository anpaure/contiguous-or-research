# Entropy and semi-random gates for calibrated top packets

Date: 2026-07-25

Method: pure mathematics only. No computation, solver, or web search is
used.

## 0. Outcome

Put

\[
 W=\binom{2m}{m},\qquad
 N=N_H=\binom{2m}{m-H},\qquad
 M=m+H,\qquad
 \rho={MN\over W}={M\over\lambda_H}=1-o(1),
\tag{0.1}
\]

where \(H\) is the least integer with \(\lambda_H=W/N_H\ge M\). Thus

\[
 H\sim\sqrt{m\log m},\qquad N=(1+o(1)){W\over m}.
\tag{0.2}
\]

There are three conclusions.

1. A one-shot symmetric Lovász-local-lemma selection of one independent cyclic order
   per top is outside the LLL range by a factor \(\Theta(M)\), already for
   middle-owner collisions. This is the probabilistic form of the
   critical-load obstruction: every owner has mean load \(1-o(1)\).

2. A sparse semi-random round is rigorous. If only a
   \(\Theta(1/M)\)-fraction of the tops is activated, random orders followed
   by deletion of colliding packets leave

   \[
   \Theta(N/M)=\Theta(W/m^2)
   \tag{0.3}
   \]

   pairwise owner-disjoint packets. More generally, if a packet must be
   disjoint in a family of nested claimed rows of average augmented size
   \(K\), activation at scale \(1/K\) gives \(\Theta(N/K)\) compatible
   packets in one round.

3. There is a natural column-preserving augmentation. Give the \(M\) cyclic
   starts one common priority order and, at depth \(q\), claim an initial
   priority segment of mean size

   \[
   b_q=\min\!\left(M,{\lambda_H\over\lambda_q}\right).
   \tag{0.4}
   \]

   The claimed start sets are nested in \(q\), every claimed target has
   degree \(1-o(1)\) after normalization, and the average augmented packet
   size is

   \[
   K=M+2\sum_{q=1}^{H-1}b_q+O(1)=\Theta(m^{3/2}).
   \tag{0.5}
   \]

   The maximum normalized pair codegree is still
   \((2+o(1))/m\), but the stronger packet--link overlap is only
   \(O(H/m)=O(\sqrt{\log m/m})\). This records the nested-column structure which a
   row-by-row encoding destroys.

What remains is a genuinely quantitative iterative-nibble theorem for this
specific column system. To prove coefficient one it must leave
\(o(W)\), not merely an \(o(1)\) fraction of the
\(\Theta(W\sqrt m)\) claimed band vertices. To leave a residual small enough
for the phase rectangles, it must leave only \(O(N)=O(W/m)\) excess
collisions. No currently audited growing-uniformity theorem supplies either
rate.

## 1. Exact one-top probabilities

Fix a middle owner \(X\). It is contained in

\[
 a=\binom mH
\tag{1.1}
\]

tops. If \(U\supset X\) and a cyclic order of \(U\) is uniform, then

\[
 p_0:=\Pr(X\text{ is an }m\text{-window})
 ={M\over\binom Mm}.
\tag{1.2}
\]

Indeed a packet has \(M\) of the \(\binom Mm\) possible owners in \(U\),
symmetrically. The identity

\[
 {\binom Mm\over\binom mH}=\lambda_H
\tag{1.3}
\]

therefore gives

\[
 ap_0={M\over\lambda_H}=\rho=1-o(1).
\tag{1.4}
\]

Thus independent one-order-per-top choices give an asymptotically Poisson
unit owner load; in particular their owner-hole density tends to \(e^{-1}\).

## 2. Why the direct LLL is supercritical

For distinct tops \(U,V\) containing \(X\), let

\[
 B(U,V;X)
\]

be the event that both selected packets contain \(X\). Then

\[
 \Pr B(U,V;X)=p_0^2.
\tag{2.1}
\]

An event involving \(U,V\) is dependent only on events involving one of
those two top variables. The number involving a fixed top is at most

\[
 \binom Mm\binom mH.
\tag{2.2}
\]

Consequently the symmetric LLL product has order

\[
 p_0^2\binom Mm\binom mH
 ={M^2\over\lambda_H}
 =(1+o(1))M.
\tag{2.3}
\]

It diverges rather than tending below \(1/e\). The corresponding uniform
cluster-expansion sum through one top has the same \(\Theta(M)\) scale.
Thus the standard symmetric or uniform-activity LLL does not certify a
collision-free full-density choice. This calculation does not rule out a
more structured asymmetric resampling argument.

If every top is independently activated with probability \(\alpha\), the
same product becomes \(\Theta(\alpha M)\). Thus the natural LLL/nibble
activation scale is

\[
 \boxed{\alpha=\Theta(1/M).}
\tag{2.4}
\]

## 3. A rigorous sparse-round lemma

The following alteration argument uses no black box.

### Lemma 3.1 (one owner-disjoint round)

Activate each top independently with probability

\[
 \alpha={\theta\over M},\qquad0<\theta<1,
\tag{3.1}
\]

and choose a uniform cyclic order on every activated top. There exists an
owner-disjoint subfamily of the activated packets of expected-order size

\[
 \boxed{
 \left(\theta-{\theta^2\over2}+o(1)\right){N\over M}.}
\tag{3.2}
\]

In particular, some outcome contains \(cN/M\) owner-disjoint packets for an
absolute \(c>0\).

#### Proof

Let \(A\) be the number of activated tops. Then

\[
 \mathbb EA=\alpha N={\theta N\over M}.
\tag{3.3}
\]

For an owner \(X\), every containing top selects \(X\) with probability

\[
 \alpha p_0={\theta\over\binom Mm}.
\]

If \(L_X\) is its selected load, then

\[
 \mathbb E\binom{L_X}{2}
 \le {1\over2}\left({\theta\over\lambda_H}\right)^2.
\tag{3.4}
\]

Let \(C\) be the number of unordered colliding packet pairs. Summing (3.4)
over owners may count one packet pair more than once, so it is an upper
bound:

\[
 \mathbb EC
 \le {W\theta^2\over2\lambda_H^2}
 =\left({\theta^2\over2}+o(1)\right){N\over M}.
\tag{3.5}
\]

Delete one packet for every edge of the collision graph. At most \(C\)
packets are deleted, and the survivors are owner-disjoint. Taking
expectations in \(A-C\) proves (3.2). \(\square\)

One round covers only a \(\Theta(1/M)\)-fraction of the available owners.
An owner near-transversal therefore needs \(\Theta(M)\) successful rounds,
with the packet degrees and codegrees remaining pseudorandom after every
deletion. Lemma 3.1 alone does not provide that preservation.

## 4. Entropy reserve and the row-independence barrier

The owner-only problem has enough raw entropy for a long nibble. A tag starts
with

\[
 D=(M-1)!
\]

orders. If a pseudorandom residual leaves an \(x\)-fraction of the owners
available and packet-owner constraints behaved independently, its surviving
tag degree would be

\[
 D_x\approx D x^M.
\tag{4.1}
\]

For \(x=m^{-c}\), Stirling gives

\[
 \log D_x=(1-c+o(1))m\log m.
\tag{4.2}
\]

Thus \(D_x\) is still exponentially large for every fixed \(c<1\). In
particular an owner residual \(x=1/\log m=o(1)\) is comfortably inside the
entropy range. The entropy calculation does not prove pseudorandomness, but
it shows that shortage of cyclic orders is not the scalar obstruction to
owner holes \(o(W)\).

The calculation reverses if all band rows are encoded as independent hard
vertices. The nested augmentation below has

\[
 K=\Theta(m^{3/2})
\tag{4.3}
\]

protected entries, while the number of order/priority decorations of one top
has logarithm only \(\Theta(m\log m)\). If every protected entry survived
independently with probability \(x<1\), the expected surviving tag degree
would have logarithm

\[
 \Theta(m\log m)+K\log x.
\tag{4.4}
\]

For a deleted fraction \(y=1-x=o(1)\), this becomes negative once

\[
 y\gg{\log m\over\sqrt m}.
\tag{4.5}
\]

Hence a product estimate over the \(K\) row vertices dies after a vanishing
amount of the desired construction. A valid iterative proof must exploit
that the \(K\) entries are \(M\) coherent nested columns and that packets
delete similarly coherent columns. This is an exact entropy reason not to
round or track the rows independently.

## 5. The general collision-mass formula

The same calculation identifies the correct activation scale when other
rank resources are protected.

Suppose one packet choice supplies \(k_i\) resources in layer \(i\), the
layer has \(V_i\) possible resources, and symmetry gives a fixed resource
full-selection load

\[
 \mu_i={Nk_i\over V_i}.
\tag{5.1}
\]

Let

\[
 K_{\rm eff}:=\sum_i k_i
 ={1\over N}\sum_iV_i\mu_i.
\tag{5.2}
\]

### Lemma 5.1 (one multirow round)

Activate a fraction \(\alpha\) of the tops and choose all packet decorations
independently and symmetrically. After deleting one packet from every pair
which collides in any protected layer, the expected surviving count is at
least

\[
 \boxed{
 \alpha N-{\alpha^2N K_{\rm eff}\over2}.}
\tag{5.3}
\]

Thus \(\alpha=\theta/K_{\rm eff}\) gives at least

\[
 \theta(1-\theta/2){N\over K_{\rm eff}}
\tag{5.4}
\]

compatible packets in some outcome.

#### Proof

For a target in layer \(i\), its active load has mean \(\alpha\mu_i\).
The sum of its expected load pairs is at most

\[
 {\alpha^2\over2}V_i\mu_i^2.
\tag{5.5}
\]

If the protected decoration has been normalized to \(\mu_i\le1\), then

\[
 V_i\mu_i^2\le V_i\mu_i=Nk_i.
\]

Sum over layers and delete one endpoint of every collision. This proves
(5.3). \(\square\)

For unthinned raw interval rows through depth \(Q\), formula (5.5) gives
the sharper activation condition

\[
 \alpha M\left(\rho+2\sum_{q=1}^Q\rho\lambda_q\right)=O(1).
\tag{5.6}
\]

This already shows why protecting \(Q\) rows independently is expensive:
the factor in parentheses grows at least linearly in \(Q\).

## 6. A nested-column claim system

The raw rows have different loads

\[
 \mu_q={MN\over N_q}=\rho\lambda_q.
\tag{6.1}
\]

When \(\mu_q>1\), it is wasteful to protect all \(M\) occurrences against
collisions. Instead claim only the number needed to give every target mean
claim load one.

Give the \(M\) starts of a cyclic packet one common random priority order.
For \(1\le q<H\), put

\[
 c_q={\lambda_H\over\lambda_q}={N_q\over N}
\tag{6.2}
\]

and choose a random integer \(b_q\in\{\lfloor c_q\rfloor,\lceil c_q\rceil\}\)
with mean \(\min(M,c_q)\). At depth \(q\), claim the first \(b_q\) starts in
the common priority order, on both the lower and upper sides. Couple the
rounding so that

\[
 b_1\ge b_2\ge\cdots\ge b_{H-1}.
\tag{6.3}
\]

At lower depth \(H\), claim one start. The upper depth-\(H\) target is the
top itself and is already represented by the tag.

This construction chooses complete nested columns: a start which remains
claimed at a deeper level retains all of its shallower claims. It does not
choose unrelated subsets in different ranks.

### Proposition 6.1 (normalized degrees)

Every owner has normalized degree \(\rho=1-o(1)\). Every claimed rank target
has normalized degree exactly one when \(c_q\le M\), and degree

\[
 \rho\lambda_q\in[\rho,1)
\tag{6.4}
\]

when the cap \(b_q=M\) is active. Hence every non-tag vertex degree is
\(1-O(H/m)\) times the common tag degree.

#### Proof

Before claiming, a target at depth \(q\) has load \(\mu_q=\rho\lambda_q\).
The mean claimed fraction is \(c_q/M\) when \(c_q\le M\), so its claimed
load is

\[
 \rho\lambda_q{c_q\over M}
 ={M\over\lambda_H}\lambda_q
   {\lambda_H\over M\lambda_q}=1.
\]

If \(c_q>M\), every occurrence is claimed and (6.4) applies. The cap
condition says \(\lambda_q<\lambda_H/M=1/\rho\), proving the displayed
range. \(\square\)

The total mean number of claims in either signed rank is exactly

\[
 N\,\mathbb E b_q=\min(T,N_q).
\tag{6.4a}
\]

Hence an unmatched claimed target is precisely one unit of excess beyond
the unavoidable floor \((N_q-T)_+\); no independent rowwise rounding is
hidden in the construction.

### Proposition 6.2 (average augmented size)

The mean number of protected vertices in one decorated packet is

\[
 K=M+2\sum_{q=1}^{H-1}\min(M,c_q)+O(1)
   =\Theta(m^{3/2}).
\tag{6.5}
\]

#### Proof

Uniformly through the calibrated window,

\[
 \lambda_q=\exp\!\left({q^2\over m}
       +O\!\left({q\over m}+{q^3\over m^2}\right)\right).
\tag{6.6}
\]

Also \(\lambda_H=(1+o(1))M\). Therefore

\[
 \sum_{q=1}^{H-1}\min(M,c_q)
 =(1+o(1))M\sum_{q\ge1}e^{-q^2/m}
 =\Theta(M\sqrt m).
\tag{6.7}
\]

Since \(M\sim m\), this is \(\Theta(m^{3/2})\). \(\square\)

## 7. Pair codegree versus nested link spread

The augmented hypergraph has a large-looking vertical pair codegree. If
\(S\subset X\), \(|S|=m-1\), then, conditioned on a packet containing the
owner \(X\), exactly two of the \(m\) facets of \(X\) occur in its
rank-\((m-1)\) interval row. Since \(b_1/M=1-o(1)\),

\[
 \boxed{
 {\deg(X,S)\over\deg(X)}
 ={2+o(1)\over m}.}
\tag{7.1}
\]

Thus the maximum relative pair codegree is \(\Theta(1/m)\), not
\(\Theta(1/m^2)\). Encoding the \(2H+1\) rows as unrelated vertices sees
only this obstruction.

The correlations are sparse along a packet. For a decorated packet \(e\)
and a protected target \(v\notin e\), define

\[
 \Lambda(e,v)
 ={1\over\deg(v)}
   \sum_{u\in e}\deg(u,v).
\tag{7.2}
\]

It is the union-bound probability that a random decorated packet through
\(v\) meets \(e\).

### Proposition 7.1 (column link-overlap bound)

Uniformly at the calibrated depth,

\[
 \boxed{\max_{e,\,v\notin e}\Lambda(e,v)
 =O(H/m)=O\!\left(\sqrt{\log m/m}\right).}
\tag{7.3}
\]

#### Proof

Fix one protected rank in \(e\). For equal ranks, the exact codegree formula
is at most \(2/[r(2m-r)]=O(m^{-2})\); summing over its at most \(M\)
intervals contributes \(O(1/m)\).

For different ranks, classify a second interval as nested or crossing
relative to \(v\); two band sets occurring in one \(M\)-top cannot be
disjoint once \(m>3H\). If the rank difference is \(d\), there are at
most \(d+1\) nested intervals in a fixed cyclic row and their individual
conditional probability, after also counting the containing-top choice, is

\[
 {d+1\over\binom{s}{d}},
\]

where \(s=m+O(H)\); for a superinterval the denominator is instead
\(\binom{2m-s}{d}\), with the same bound. Their total is \(O(1/m)\), with
the \(d=1\) term largest.

In the crossing case put
\(a=|v-T|>0\) and \(b=|T-v|>0\). Conditioning on \(v\) as an interval,
the two interval boundaries give

\[
 {\deg(v,T)\over\deg(v)}
 \le {2\over\binom{s}{a}\binom{2m-s}{b}}=O(m^{-2}).
\]

There are at most \(M\) intervals \(T\) in the fixed row, so all crossing
terms contribute \(O(1/m)\). Thus one unthinned rank of \(e\) contributes
\(O(1/m)\).

Claiming a subset of starts cannot increase this deterministic row bound.
There are at most \(2H+1\) protected rows, so summation gives

\[
 \Lambda(e,v)=O(H/m).
\]

At the calibrated height this is
\(O(\sqrt{\log m/m})=o(1)\). \(\square\)

Hence the nested system has no projective-plane-type link obstruction:
the link overlap tends to zero even though the maximum vertical codegree is
only \(O(1/m)\).

## 8. The exact iterative rate required

Lemma 5.1 applied to the nested augmentation has activation scale

\[
 \alpha=\Theta(1/K)=\Theta(m^{-3/2})
\tag{8.1}
\]

and selects \(\Theta(N/K)\) compatible packets in one sparse round. An ideal
degree-preserving nibble would therefore require

\[
 R_\varepsilon=\Theta\!\left(K\log{1\over\varepsilon}\right)
\tag{8.2}
\]

rounds to leave an \(\varepsilon\)-fraction of every normalized resource
class.

There are

\[
 V_{\rm aug}
 =W+2\sum_{q=1}^{H-1}N_q+O(N)
 =\Theta(W\sqrt m)
\tag{8.3}
\]

protected non-tag vertices. Therefore:

* coefficient one requires

  \[
  \varepsilon V_{\rm aug}=o(W),
  \qquad\text{i.e.}\qquad
  \boxed{\varepsilon=o(m^{-1/2});}
  \tag{8.4}
  \]

* a residual of order \(N=O(W/m)\), small enough for the phase rectangles,
  requires

  \[
  \varepsilon V_{\rm aug}=O(W/m),
  \qquad\text{i.e.}\qquad
  \boxed{\varepsilon=O(m^{-3/2}).}
  \tag{8.5}
  \]

The corresponding ideal round counts are \(K\log m\) in both cases, up to
constant factors.

This identifies the precise missing semi-random theorem:

> **Column-preserving calibrated nibble.** The decorated packet hypergraph
> of Section 6 has a matching which leaves \(o(W)\) protected mask vertices;
> preferably it leaves \(O(W/m)\).

The numerical inputs available for such a theorem are

\[
 K=\Theta(m^{3/2}),\qquad
 {\Delta_2\over D}=\Theta(1/m),\qquad
 \max\Lambda=O(H/m)=O(\sqrt{\log m/m}),\qquad
 \log D=\Theta(m\log m).
\tag{8.6}
\]

The first-round alteration is valid, and concentration is not the scalar
problem because \(D\) is factorially large. The unproved point is stability
of the nested link profiles for \(\Theta(K\log m)\) adaptive rounds.

## 9. Collision excess and the absorber interface

For a selected packet family \(\mathcal P\), define at depth \(q\)

\[
 E_q^\pm
 :=\min(T,N_q)-|\operatorname{supp}_q^\pm(\mathcal P)|.
\tag{9.1}
\]

This is the excess hole count beyond the unavoidable slot deficit:

\[
 N_q-|\operatorname{supp}_q^\pm|
 =(N_q-T)_++E_q^\pm.
\tag{9.2}
\]

The calibrated scalar estimate gives

\[
 \sum_{q=0}^H(N_q-T)_+=o(W).
\tag{9.3}
\]

Fix any absorber cutoff \(Q\le H-1\). The exact phase-absorber interface is

\[
 \boxed{
 \sum_{q=1}^Q(E_q^-+E_q^+)=O(N)=O(W/m),}
\tag{9.4}
\]

with the separate requirement that the claimed holes at \(q>Q\) total
\(o(W)\). The phase rectangles can
alter only \(O(N)\) desired rank incidences, while causing \(O(HN)=o(W)\)
collateral damage. They cannot repair an \(\omega(N)\) excess.

A generic owner-only matching is not enough: at any shallow rank with
\(\mu_q=\Theta(1)\), random-like interval loads leave a positive fraction of
the rank uncovered. Thus the entropy bias represented by the nested claims
must be present during owner matching; it cannot be postponed to an
independent vertical rounding.

## 10. Final status

### Proved

1. The direct LLL parameter is \(\Theta(M)\), so the one-shot LLL fails.
2. A sparse owner-only round selects \(\Theta(N/M)\) disjoint packets.
3. The general protected-layer alteration formula (5.3).
4. An exact nested-priority claim system with normalized degrees \(1-o(1)\).
5. Its augmented size \(K=\Theta(m^{3/2})\).
6. Its unavoidable vertical codegree \((2+o(1))/m\).
7. Its stronger packet--link overlap
   \(O(H/m)=O(\sqrt{\log m/m})\).
8. The explicit final errors \(o(m^{-1/2})\) for coefficient one and
   \(O(m^{-3/2})\) for rectangle-scale absorption.

### Open

1. Iterating the owner-only sparse round for \(\Theta(M)\) rounds while
   keeping the top and owner degrees balanced.
2. Iterating the nested-column round for \(\Theta(K\log m)\) rounds while
   retaining the link bound.
3. Obtaining the absorber-scale residual (9.4).
