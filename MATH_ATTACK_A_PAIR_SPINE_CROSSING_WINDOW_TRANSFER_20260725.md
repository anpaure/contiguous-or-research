# Pair-spine crossing-window transfer: the global corridor gate is exactly local

Date: 2026-07-25

Method: pure mathematics only.  No search, computation, or finite case
analysis is used.

## 0. Outcome

Put

\[
 n=2m+1,\qquad L=2m-1,\qquad W=\binom{n}{m}.
\]

For an exact central wreath factor \(F\) on \(L\) coordinates, let
\(\mathcal I_r(F)\) be the family of \(r\)-sets that occur as cyclic
intervals in its rows, and put

\[
 g_q(F)=\binom{L}{m+q}-|\mathcal I_{m+q}(F)|
 \qquad(0\le q\le m-1).
\tag{0.1}
\]

Thus \(g_0(F)=0\).  The main result is the following transfer theorem.

> **Pair-spine transfer theorem.**  Let \(H=o(m^{2/3})\).  From one exact
> factor \(F\), independently relabelled on the pair-deleted coordinate
> sets, one can form the first-avoided-pair physical spine with
> \(J=O(W/m)\) selected runs and
> \[
> \sum_{q=1}^{H}(\widehat M_q^-+\widehat M_q^+)
> \le
> C\sum_{q=1}^{H}g_q(F)
> +O\left(W\left({H\over m}+{H^3\over m^2}\right)\right)+o(W).
> \tag{0.2}
> \]

Here \(\widehat M_q^\pm\) are the actual missing targets from the union of
the complete physical Pascal corridors of the selected owners.  The
constant \(C\) is absolute.  In particular, if

\[
 \sum_{q=1}^{H}g_q(F)=o(W),
\tag{0.3}
\]

then the expanded-collar construction has

\[
 \sum_{q=1}^{H}(\widehat M_q^-+\widehat M_q^+)=o(W).
\tag{0.4}
\]

The range includes

\[
 H=\sqrt m\,\omega(m),\qquad
 \omega(m)\longrightarrow\infty,qquad
 \omega(m)=o(m^{1/6}),
\tag{0.5}
\]

and hence includes the useful choice
\(H=(1+o(1))\sqrt{m\log\log m}\).

The new ingredient is deterministic.  If a supported upper interval of
first-avoided category \(j\) contains no selected owner, then either one
earlier pair occurs only at its terminal coordinate, or two distinct
earlier pairs are confined to the two opposite crossing strips.  Random
relabeling is used only to average these explicit certificates, after
which one deterministic family of exact relabelled factors is fixed.

There is also an exact converse.  The targets avoiding the first pair can
only be supplied by phase one, and their upper corridor support is exactly
the interval support of the phase-one factor.  Therefore

\[
 \widehat M_q^+\ge g_q(F_1)\quad(1\le q\le H).
\tag{0.6}
\]

Consequently, in the range \(H=o(m^{2/3})\), existence of a
pair-omission spine satisfying (0.4) is equivalent to existence of one
exact local factor satisfying (0.3).  The pair spine, its physical
selection rule, and all category crossings add only \(o(W)\); they do not
remove the exact local shallow-shadow gate.

## 1. The physical spine and local defects

Partition \(2m\) coordinates into ordered disjoint pairs

\[
 P_1,\ldots,P_m
\]

and leave one coordinate unpaired.  Put

\[
 Q_j=[n]\setminus P_j.
\]

For a set \(A\) which avoids at least one pair, define

\[
 \kappa(A)=\min\{j:A\cap P_j=\varnothing\}.
\tag{1.1}
\]

On each \(Q_j\), take a relabelled copy \(F_j\) of \(F\).  In a row
\(\pi\) of \(F_j\), write

\[
 S_i=I_\pi(i,m-1),\qquad X_i=I_\pi(i,m).
\]

Select the start \(i\) exactly when \(\kappa(S_i)=j\).  These selected
\((m-1)\)-sets cover their rank exactly once and the selected owners are
distinct.  For a selected owner \(X_i\), its full lower and upper
depth-\(q\) corridors are

\[
 I_\pi(i+a,m-q)\quad(0\le a\le q),
 \qquad
 I_\pi(i-b,m+q)\quad(0\le b\le q).
\tag{1.2}
\]

Let \(\widehat{\mathcal C}_q^-\) and
\(\widehat{\mathcal C}_q^+\) be the unions of the actual targets in
(1.2), and define

\[
 \widehat M_q^-=\binom n{m-q}-|\widehat{\mathcal C}_q^-|,
 \qquad
 \widehat M_q^+=\binom n{m+q}-|\widehat{\mathcal C}_q^+|.
\tag{1.3}
\]

Complementation inside a cyclic row on \(L\) coordinates sends an
interval of length \(m-q\) to one of length

\[
 L-(m-q)=m+q-1.
\]

It follows that the local lower defect at depth \(q\) is exactly

\[
 \binom L{m-q}-|\mathcal I_{m-q}(F)|=g_{q-1}(F).
\tag{1.4}
\]

Thus the one sequence \(g_0,g_1,\ldots\) controls both signed local
supports.

## 2. The deterministic crossing-window certificate

The following is the promised charged crossing lemma.

### Lemma 2.1 (two-end crossing certificate)

Let \(U\) be an \((m+q)\)-set of finite category
\(j=\kappa(U)\), where \(1\le q\le m-1\).  Suppose that in a row of
\(F_j\),

\[
 U=I_\pi(s,m+q).
\]

Linearly index the positions of this occurrence by
\(0,1,\ldots,m+q-1\), and put \(e=m+q-1\).  Consider the two contained
\((m-1)\)-windows

\[
 S_L=[0,m-2],\qquad S_R=[q,m+q-2].
\tag{2.1}
\]

If neither corresponding owner start is selected in phase \(j\), then
one of the following holds.

1. For some \(a<j\),
   \[
   U\cap P_a=\{e\}.
   \tag{2.2}
   \]
2. There are distinct \(a,b<j\) such that
   \[
   \varnothing\ne U\cap P_a
      \subseteq [m-1,m+q-1],
   \tag{2.3}
   \]
   and
   \[
   \varnothing\ne U\cap P_b
      \subseteq [0,q-1]\cup\{e\}.
   \tag{2.4}
   \]

If either \(S_L\) or \(S_R\) is selected, then \(U\) belongs to the
full upper corridor of that selected owner.

#### Proof

The set \(U\) avoids \(P_j\) and meets every \(P_h\), \(h<j\).  If
\(S_L\) is not selected, it must miss some earlier pair \(P_a\).  Hence
the nonempty set \(U\cap P_a\) is contained in

\[
 U\setminus S_L=[m-1,m+q-1].
\]

Likewise, failure of \(S_R\) gives an earlier pair \(P_b\) for which

\[
 \varnothing\ne U\cap P_b
 \subseteq U\setminus S_R=[0,q-1]\cup\{e\}.
\]

If \(a\ne b\), this is (2.3)--(2.4).  If \(a=b\), then

\[
 U\cap P_a\subseteq
 [m-1,m+q-1]\cap([0,q-1]\cup\{e\})=\{e\},
\]

because \(q\le m-1\).  Nonemptiness gives (2.2).

The owner beginning with \(S_L\) has \(U\) as its right-extended
depth-\(q\) interval; the owner beginning with \(S_R\) has \(U\) as its
left-extended depth-\(q\) interval.  Therefore selection of either start
puts \(U\) in the corresponding full corridor. \(\square\)

The certificate has a useful uniform probability bound.

### Lemma 2.2 (crossing charge under a uniform interval order)

Fix an \((m+q)\)-set \(U\) of category \(j\), put \(r=j-1\) and
\(k=m+q\), and place the elements of \(U\) in a uniformly random linear
order.  The probability that the certificate of Lemma 2.1 occurs is at
most

\[
 {r\over k}+16r(r-1){(q+1)^2\over k^2}.
\tag{2.5}
\]

#### Proof

For a fixed earlier pair \(P_a\), (2.2) is possible only when
\(|U\cap P_a|=1\), and its sole element must occupy the specified
terminal position.  Its probability is then exactly \(1/k\).  A union
bound gives the first term.

For fixed distinct \(a,b\), the two nonempty, disjoint sets
\(U\cap P_a\) and \(U\cap P_b\) have total size at least two.  Expose
their positions without replacement.  Each must fall in a prescribed set
of \(q+1\) positions.  Since \(q=o(m)\) in every later application, for
all sufficiently large \(m\) one has \(2(q+1)\le k\); sequential exposure
then bounds this probability by

\[
 16{(q+1)^2\over k^2}.
\]

There are \(r(r-1)\) ordered choices of \((a,b)\), proving (2.5).
\(\square\)

The constant 16 is deliberately inessential.  The important point is
that two distinct crossing pairs cost \(O(q^2/m^2)\), not \(O(q/m)\).
The only first-order exception is the single terminal representative
(2.2), which costs \(O(1/m)\) independently of \(q\).

## 3. Category moments

We use the following elementary consequence of fixed-size sampling.

### Lemma 3.1 (geometric category moments)

Uniformly for \(q=o(m)\), if \(U\) ranges over the \((m+q)\)-sets of
finite category and \(r(U)=\kappa(U)-1\), then for every fixed
\(a\ge0\),

\[
 \sum_U r(U)^a=O_a\left(\binom n{m+q}\right).
\tag{3.1}
\]

#### Proof

For a uniform \(k\)-set, the probability of meeting each of \(r\)
specified disjoint pairs is at most

\[
 p_{n,k}^{,r},\qquad
 p_{n,k}=1-{(n-k)(n-k-1)\over n(n-1)}.
\tag{3.2}
\]

This follows by exposing the pair blocks successively: conditional on the
number of sampled points already spent in previous blocks, success on the
old blocks is increasing in that number whereas success on a fresh block
is decreasing, so the two events are negatively correlated.  For
\(k=m+q\) and \(q=o(m)\), one has \(p_{n,k}\le\rho<1\) for an absolute
\(\rho\), once \(m\) is large.

The family of category \(j=r+1\) is contained in the family meeting the
first \(r\) pairs.  Hence its size is at most
\(\binom nk\rho^r\).  Summing \(r^a\rho^r\) proves (3.1). \(\square\)

The sets meeting every pair are exponentially negligible throughout any
sublinear window.

### Lemma 3.2 (infinite-category tail)

If \(H=o(m)\), then

\[
 \sum_{q=1}^H
 |\{U\in\tbinom{[n]}{m+q}:U\cap P_j\ne\varnothing\ 
       \text{for every }j\}|=o(W).
\tag{3.3}
\]

#### Proof

Choose one contained representative from each pair, in at most \(2^m\)
ways, and then choose the remaining \(q\) elements from the other
\(m+1\) coordinates.  Thus the summand is at most

\[
 2^m\binom{m+1}{q}.
\]

For \(H=o(m)\),

\[
 \sum_{q\le H}\binom{m+1}{q}=\exp(o(m)).
\]

On the other hand the largest-binomial-coefficient bound gives
\(W\ge2^{2m}/(m+1)\).  The ratio of the displayed sum to \(W\) is
\(2^{-m+o(m)}\), proving (3.3). \(\square\)

## 4. Transfer of local support to the physical spine

### Theorem 4.1 (quantitative pair-spine transfer)

Let \(H=o(m)\), and let \(F\) be any exact central wreath factor on
\(L=2m-1\) coordinates.  Independently relabel \(F\) uniformly onto
each \(Q_j\), and form the first-avoided-pair spine.  Then

\[
 \mathbb E\sum_{q=1}^{H}
 (\widehat M_q^-+\widehat M_q^+)
 \le
 C\sum_{q=1}^{H}g_q(F)
 +C W\left({H\over m}+{H^3\over m^2}\right)+o(W),
\tag{4.1}
\]

where the final \(o(W)\) is the infinite-category contribution.  The
constant \(C\) is absolute.

#### Proof: lower targets

Fix \(T\in\binom{[n]}{m-q}\).  Since \(|T|<m\), it avoids at least one
pair, so \(j=\kappa(T)\) is finite.  Then \(T\subseteq Q_j\) and it
meets every earlier pair.

If \(T\) occurs as a length-\((m-q)\) interval in \(F_j\), take the
same-start length-\((m-1)\) interval \(S\).  It contains \(T\), avoids
\(P_j\), and meets every earlier pair.  Hence \(\kappa(S)=j\), its start
is selected, and \(T\) lies in that owner's lower corridor.  Therefore
\(T\) can be missing only if it is absent from the local interval support
of \(F_j\).

Under a uniform relabeling, that probability is

\[
 {g_{q-1}(F)\over\binom L{m-q}}
\]

by (1.4).  Summing over \(T\), and using

\[
 {\binom n{m-q}\over\binom{n-2}{m-q}}=O(1)
\tag{4.2}
\]

uniformly for \(q=o(m)\), gives

\[
 \mathbb E\widehat M_q^-=O(g_{q-1}(F)).
\tag{4.3}
\]

#### Proof: upper targets

Fix a finite-category \(U\in\binom{[n]}{m+q}\), let
\(j=\kappa(U)\), \(r=j-1\), and \(k=m+q\).  Its probability of being
absent from the local interval support of \(F_j\) is

\[
 {g_q(F)\over\binom L{m+q}}.
\tag{4.4}
\]

Conditional on its preimage being a supported local target, fix one
distinguished pointed occurrence of that preimage.  Conditional on the
preimage, the relabeling restricted to it is a uniform bijection onto
\(U\).  Thus its order in the distinguished occurrence is uniformly
random.  Lemmas 2.1--2.2 show that, apart from (4.4), its failure
probability is at most

\[
 {r\over k}+16r(r-1){(q+1)^2\over k^2}.
\tag{4.5}
\]

Summing (4.4) over targets costs \(O(g_q(F))\), because

\[
 {\binom n{m+q}\over\binom{n-2}{m+q}}=O(1)
\tag{4.6}
\]

uniformly for \(q=o(m)\).  Lemma 3.1, with \(a=1,2\), bounds the sum of
(4.5) by

\[
 O\left(\binom n{m+q}
   \left({1\over m}+{(q+1)^2\over m^2}\right)\right)
 =O\left(W\left({1\over m}+{(q+1)^2\over m^2}\right)\right).
\tag{4.7}
\]

The infinite-category targets contribute \(o(W)\) after summing all
depths by Lemma 3.2.  Finally, summing (4.3) and (4.7) over
\(1\le q\le H\), using \(g_0=0\), proves (4.1). \(\square\)

### Corollary 4.2 (simultaneous sharp run count)

If \(H=o(m^{2/3})\) and \(F=F_m\) satisfies (0.3), then there are
deterministic relabelings for which simultaneously

\[
 J=O(W/m)
\tag{4.8}
\]

and (0.4) holds.

#### Proof

The boundary calculation for the first-avoided selection words gives
\(\mathbb EJ=O(W/m)\) under exactly these independent uniform
relabelings.  Theorem 4.1 gives

\[
 \mathbb E\sum_{q\le H}(\widehat M_q^-+\widehat M_q^+)=o(W).
\]

Let the latter expectation be \(\varepsilon_mW\), where
\(\varepsilon_m\to0\).  Markov's inequality makes the corridor sum at
most \(\sqrt{\varepsilon_m}W=o(W)\) outside an event of probability
\(\sqrt{\varepsilon_m}\).  A fixed sufficiently large constant multiple
of \(W/m\) bounds \(J\) outside an event of probability less than
\(1/2\).  For large \(m\), the two good events intersect.  Fix any
relabeling in their intersection. \(\square\)

Combining Corollary 4.2 with the expanded-collar theorem gives a literal
word of length

\[
 N_1+3HJ+O(1)=W+o(W)
\]

which covers the entire signed band except \(o(W)\) targets; those targets
may be appended literally.  Taking
\(H=\lceil\alpha\sqrt{m\log m}\rceil\) with fixed
\(\alpha>1/\sqrt2\) also makes the factor-independent outer binomial tails
\(o(W)\).  Thus (0.3) at that depth is sufficient for coefficient one.

## 5. Exact necessity and equivalence

### Theorem 5.1 (phase-one local shadow is the exact residual gate)

For every first-avoided-pair spine, with arbitrary exact local factors
\(F_j\),

\[
 \widehat M_q^+\ge g_q(F_1)
 \qquad(1\le q\le m-1).
\tag{5.1}
\]

More precisely, among the rank-\((m+q)\) targets contained in \(Q_1\),
the covered targets are exactly \(\mathcal I_{m+q}(F_1)\).

#### Proof

Every start in phase one is selected, because there are no earlier pairs.
Hence every supported length-\((m+q)\) interval of \(F_1\) contains a
selected same-row middle owner and lies in its full corridor.

Conversely, every upper target in a phase-one corridor is a cyclic
length-\((m+q)\) interval of \(F_1\).  A selected owner from a later
phase meets \(P_1\), because its selected \((m-1)\)-facet meets every
earlier pair.  Every upper target in its corridor therefore also meets
\(P_1\).  Such a target cannot fill a hole contained in \(Q_1\).  This
proves the exact assertion and (5.1). \(\square\)

### Corollary 5.2 (equivalence for the pair-spine architecture)

Let \(H=o(m^{2/3})\).  The following are equivalent.

1. There are exact factors and a first-avoided-pair expanded-collar spine
   for which
   \[
   \sum_{q=1}^H(\widehat M_q^-+\widehat M_q^+)=o(W).
   \]
2. There is one exact central wreath factor \(F\) on \(2m-1\)
   coordinates for which
   \[
   \sum_{q=1}^H g_q(F)=o(W).
   \]

#### Proof

Statement 1 implies Statement 2 by taking \(F=F_1\) in Theorem 5.1.
Statement 2 implies Statement 1 by Corollary 4.2. \(\square\)

Thus the deterministic crossing-window problem created by pair omission
is solved quantitatively: its total charge is

\[
 O\left(W\left({H\over m}+{H^3\over m^2}\right)\right)=o(W)
\]

in the stated range.  The smallest unproved statement is no longer a
global pair-category transport lemma.  It is exactly the local integral
factor theorem (0.3).

## 6. Adversarial audit

1. **The two endpoint windows really correspond to selected owners.**
   Both have length \(m-1\), both lie in \(Q_j\), and meeting all earlier
   pairs makes their first avoided pair exactly \(P_j\).  Their associated
   length-\(m\) windows are contained in \(U\), so \(U\) is one of the
   legal upper corridor intervals in (1.2).
2. **The same-pair case was not charged quadratically.**  The two excluded
   boundary strips intersect in the single terminal position.  This is why
   (2.5) contains the separate \(r/k\) term.
3. **Support and order were not assumed independent.**  Conditional on a
   supported preimage target, one fixed pointed occurrence is chosen.
   The coordinate bijection restricted to that preimage remains uniform,
   which is all Lemma 2.2 uses.
4. **Lower targets need no crossing argument.**  Their same-start
   \((m-1)\)-window contains the target, so it automatically meets every
   pair met by the target.
5. **Infinite category was not silently assigned a phase.**  It is paid
   separately in Lemma 3.2, at exponentially small total cost.
6. **The signed local defects have the correct one-step shift.**  Lower
   depth \(q\) is complementary inside \(2m-1\) coordinates to upper
   local depth \(q-1\), giving (1.4); \(g_0=0\) is exact middle
   factorization.
7. **The result is deterministic.**  Randomness selects relabelings only.
   Corollary 4.2 fixes one integral family of exact factors and one literal
   physical spine.
8. **No constant-one claim is hidden.**  The local theorem (0.3) remains
   unproved.  Theorem 5.1 shows that no crossing charge involving later
   pair phases can remove it within the first-avoided architecture.
