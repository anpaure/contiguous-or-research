# Deterministic Stage B for rank-balanced partial blocks: the exact flow ceiling and a sharp pair-energy criterion

Date: 2026-07-26

Method: pure mathematics only.

## 0. Outcome

Let

\[
 W=\binom{2m}{m},\qquad N_q=\binom{2m}{m-q}
                  =\binom{2m}{m+q},\qquad \rho_q=N_q/W.
\]

Suppose that a selected family \(\mathcal F\) consists of disjoint cyclic
partial pair-flip blocks of length

\[
 R=2\ell,
\]

and that every cyclic window through depth \(H<\ell\) is geodesic.  Put

\[
 t=|\mathcal F|,\qquad A=Rt,\qquad L=W-A.
\]

Thus \(L\) is the middle leave.  At every depth and on either side, the
blocks supply exactly \(A\) shadow occurrences, with no repetition inside
one block.

This note proves five facts.

1.  After \(\mathcal F\) is fixed, physical Stage B is exactly a support
    problem.  A max-flow can assign existing targets to witnessing blocks,
    but it cannot create a target of occurrence zero.  With the full physical
    capacity \(R\) on every block, the exact flow deficiency is the missing
    target count.

2.  There is a sharp deterministic certificate for small missing count using
    only pairwise block overlaps.  If \(n(S)\) is the occurrence multiplicity
    and

    \[
       P=\sum_S\binom{n(S)}2,
    \]

    then the exact extremal relation between \(P\) and the number of occupied
    targets is obtained by balancing \(A\) balls among the occupied targets.
    A particularly convenient corollary is

    \[
      M\le {2(P-P_{\rm bal})\over a(a+1)},
      \qquad
      a=\left\lfloor {A\over N_q}\right\rfloor\ge1,
    \]

    where

    \[
       P_{\rm bal}=aA-\binom{a+1}{2}N_q.
    \]

    When \(A<N_q\), one instead has

    \[
       M\le N_q-A+P.
    \]

    These inequalities hold separately for every depth and both signs, so a
    weighted sum of the normalized excess pair energies gives a completely
    deterministic simultaneous Stage-B theorem.

3.  The middle leave has an exact, substantially sharper aggregate capacity
    cost than the crude bound \(2HL\):

    \[
       \Lambda_H(L)
       =2\sum_{q=1}^H\bigl(L-W(1-\rho_q)\bigr)_+.
    \]

    If \(\delta=L/W\to0\), \(m\delta\to\infty\), and the controlled band
    contains \((1+o(1))\sqrt{m\delta}\), then

    \[
       \Lambda_H(L)
       =\left({4\over3}+o(1)\right)
          W\sqrt m\,\delta^{3/2}.
    \]

    In particular

    \[
       L=o(Wm^{-1/3})
    \]

    makes the forced aggregate shadow leave \(o(W)\).  The exponent
    \(1/3\) is sharp for this capacity ledger.

4.  Exact rank-balanced first marginals do not imply any of these
    conclusions.  Uniformly relabelling one bad integral factor gives exact
    symmetric marginal \(A/N_q\) at every target while preserving every
    hole and every pair-overlap energy.  Therefore ordinary averaging of
    fractional degrees, or a flow run only after an arbitrary Stage-A
    factor has been fixed, cannot prove Stage B.

5.  Overlaying finitely many exact middle factors componentwise gives a
    second deterministic, non-nibble averaging theorem with the exact
    missing probability

    \[
      \prod_K\left(1-{h_K(S)\over k}\right).
    \]

    A matching lower bound shows that a fixed number of uniformly averaged
    overlays cannot repair a positive-density bad layer unless the inputs
    are already individually good there.  Thus the overlay theorem is a
    valid positive mechanism, but its required component exposure is new
    information not supplied by rank balance.

The genuine remaining gate is to construct a middle near-factor for which
the summed normalized excess pair energy below is \(o(W)\).  No
growing-uniformity nibble is needed *after* such a family is supplied, but
the present argument does not construct it.

## 1. Occurrence and collision ledgers

For \(\sigma\in\{-,+\}\), let

\[
 \mathcal V_q^- =\binom{[2m]}{m-q},\qquad
 \mathcal V_q^+ =\binom{[2m]}{m+q}.
\]

For a block \(B\in\mathcal F\), write

\[
 C_{q,\sigma}(B)\subseteq\mathcal V_q^\sigma
\]

for its cyclic depth-\(q\) colors.  Local geodesicity and the partial
pair-flip geometry give

\[
 |C_{q,\sigma}(B)|=R                                      \tag{1.1}
\]

for \(q<\ell\), with all these colors distinct inside \(B\).

Define

\[
 n_{q,\sigma}(S)
  =|\{B\in\mathcal F:S\in C_{q,\sigma}(B)\}|,
\]

\[
 M_{q,\sigma}=|\{S:n_{q,\sigma}(S)=0\}|,                 \tag{1.2}
\]

and

\[
 C_{q,\sigma}
   =\sum_S(n_{q,\sigma}(S)-1)_+ .                         \tag{1.3}
\]

Double counting gives

\[
 \sum_S n_{q,\sigma}(S)=A.                               \tag{1.4}
\]

Consequently the exact missing/collision identity is

\[
 \boxed{M_{q,\sigma}=N_q-A+C_{q,\sigma}.}                 \tag{1.5}
\]

Indeed the number of occupied targets is
\(A-C_{q,\sigma}\), and subtracting it from \(N_q\) proves
(1.5).

In particular every construction has the capacity lower bound

\[
 M_{q,\sigma}\ge (N_q-A)_+
   =\bigl(L-W(1-\rho_q)\bigr)_+.                          \tag{1.6}
\]

This lower bound is independent of the geometry of the blocks.

Define also the pair-overlap energy

\[
 P_{q,\sigma}
    =\sum_{S\in\mathcal V_q^\sigma}
       \binom{n_{q,\sigma}(S)}2.                          \tag{1.7}
\]

Because no block repeats one of its own depth-\(q\) colors,

\[
 \boxed{
 P_{q,\sigma}
   =\sum_{\{B,B'\}\in\binom{\mathcal F}2}
       |C_{q,\sigma}(B)\cap C_{q,\sigma}(B')|.}           \tag{1.8}
\]

Thus (1.7) is a genuinely quadratic statistic of the chosen blocks, but it
requires only pairwise overlap information.

## 2. Exact max-flow theorem and its ceiling

Fix one pair \((q,\sigma)\), and abbreviate its target layer by
\(\mathcal V\).  Give each block an integer service capacity

\[
 0\le c_B\le R.
\]

One asks to assign as many targets as possible to incident blocks, each
target at most once and block \(B\) at most \(c_B\) times.

### Theorem 2.1 (exact capacitated deficiency)

The minimum number of unassigned targets is

\[
 \boxed{
 \Delta(c)=
  \max_{X\subseteq\mathcal V}
  \left(
    |X|-\sum_{B:\,C_{q,\sigma}(B)\cap X\ne\varnothing}c_B
  \right)_+.}                                            \tag{2.1}
\]

#### Proof

Replace block \(B\) by \(c_B\) identical service clones, each adjacent to
all targets in \(C_{q,\sigma}(B)\).  A target assignment is a matching from
targets to these clones.  The deficiency form of Hall's theorem says that
the number of unmatched targets is the maximum of

\[
 |X|-|N(X)|
\]

over target subsets \(X\).  Here

\[
 |N(X)|=\sum_{B:C_{q,\sigma}(B)\cap X\ne\varnothing}c_B,
\]

which proves (2.1).  Equivalently, this is the integral max-flow theorem for
the network target--block with unit target capacities and block capacities
\(c_B\).  All capacities are integral.  \(\square\)

### Corollary 2.2 (full physical capacity)

For \(c_B=R\) for every block,

\[
 \boxed{\Delta(R)=M_{q,\sigma}.}                          \tag{2.2}
\]

#### Proof

No assignment can serve a target of occurrence zero.  Conversely, choose
one witnessing block for every target of positive occurrence.  A block
receives at most one assignment for each of its \(R\) distinct colors, hence
at most \(R\) assignments.  Thus all \(N_q-M_{q,\sigma}\) present targets
are simultaneously served.  \(\square\)

Corollary 2.2 is the exact limit of a deterministic flow argument after
Stage A.  The flow performs the assignment integrally, but its deficiency is
already the missing-color count.  It cannot reduce that count.

If artificial balanced capacities \(c_B\simeq R\rho_q\) are imposed, (2.1)
is a genuine extra Hall condition.  Such capacities may be convenient in a
one-stage decorated-hypergraph proof, but they are not a physical constraint
of the contiguous-OR problem.

## 3. Sharp support bound from pair energy

For integers \(A\ge1\) and \(1\le K\le A\), define

\[
 b=\left\lfloor {A\over K}\right\rfloor,
 \qquad r=A-bK,
\]

and

\[
 \Phi(A,K)
   =K\binom b2+br.                                       \tag{3.1}
\]

### Lemma 3.1 (balanced occupancy is extremal)

Among all positive integer vectors

\[
 x_1,\ldots,x_K\ge1,qquad \sum_{i=1}^Kx_i=A,
\]

the minimum of

\[
 \sum_{i=1}^K\binom{x_i}2
\]

is \(\Phi(A,K)\).  Equality holds exactly when all \(x_i\) belong to
\(\{b,b+1\}\), with precisely \(r\) entries equal to \(b+1\).

#### Proof

If \(x_i\ge x_j+2\), moving one unit from \(x_i\) to \(x_j\) changes the
sum by

\[
 - (x_i-1)+x_j<0.
\]

Repeated smoothing therefore reaches, and only stops at, a vector whose
coordinates differ by at most one.  Its value is (3.1).  \(\square\)

### Theorem 3.2 (exact variational inverse and sharp lower envelope)

Let \(N=N_q\), \(P=P_{q,\sigma}\), and define the exact integer inverse

\[
 K_{\rm ex}(A,N,P)=
 \min\left\{K:\begin{array}{l}
 1\le K\le\min(A,N),\ \text{and there are }x_1,\ldots,x_K\in\mathbb Z_{\ge1},\\
 \displaystyle\sum_i x_i=A,\qquad
 \displaystyle\sum_i\binom{x_i}{2}=P
 \end{array}\right\}.                               \tag{3.2a}
\]

The defining set is nonempty for the physical multiplicity vector.  Also
define the explicit lower-envelope inverse

\[
 K_\Phi(A,N,P)
  =\min\{K:1\le K\le\min(A,N),\ \Phi(A,K)\le P\}.    \tag{3.2b}
\]

Then

\[
 \boxed{
 M_{q,\sigma}\le N-K_{\rm ex}(A,N,P)
                 \le N-K_\Phi(A,N,P).}                 \tag{3.3}
\]

The first inequality is the exact sharp conclusion available from the three
integers \((A,N,P)\) alone: any vector in the defining set, placed on
exactly `K_ex` targets, attains equality.  The second is the useful closed
lower-envelope bound.  For every admissible `K`, equality
`P=Phi(A,K)` is attained by the balanced vector of Lemma 3.1, so no stronger
bound follows merely from the universal inequality `P>=Phi(A,K)` (or from
an upper bound on `P`).  For a prescribed exact `P`, discrete unattainable
energy gaps are retained by `K_ex` and may make the first inequality
strictly stronger than the second.

#### Proof

The actual number of occupied targets is

\[
 K=N-M_{q,\sigma}.
\]

Its positive multiplicity vector witnesses that `K` belongs to the defining
set for `K_ex`, so `K>=K_ex`; conversely a minimizing vector for `K_ex`
realizes equality at the level of scalar multiplicities.  This proves the
first inequality in (3.3).

Its positive multiplicities sum to \(A\), so Lemma 3.1 gives

\[
 P\ge\Phi(A,K).
\]

By definition of \(K_\Phi\), this forces \(K\ge K_\Phi\), proving the
second inequality.  Balanced multiplicities give the stated lower-envelope
extremizers.  \(\square\)

The exact variational inverse and even the explicit envelope inverse are
sometimes cumbersome.  The following linear corollary is better suited to
simultaneous averaging.

### Corollary 3.3 (normalized excess-energy bound)

Put

\[
 a=\left\lfloor {A\over N}\right\rfloor.
\]

If \(a=0\), then

\[
 \boxed{M_{q,\sigma}\le N-A+P_{q,\sigma}.}               \tag{3.4}
\]

If \(a\ge1\), put

\[
 P_{\rm bal}(A,N)
   =aA-\binom{a+1}{2}N.                                  \tag{3.5}
\]

Then

\[
 \boxed{
 M_{q,\sigma}
  \le {2\bigl(P_{q,\sigma}-P_{\rm bal}(A,N)\bigr)
           \over a(a+1)}.}                               \tag{3.6}
\]

#### Proof

If \(a=0\), identity (1.5) and

\[
 (n-1)_+\le\binom n2
\]

give (3.4).

Suppose \(a\ge1\).  For every integer \(n\),

\[
 (n-a)(n-a-1)\ge0,                                      \tag{3.7}
\]

with equality exactly for \(n\in\{a,a+1\}\).  Summing (3.7) over all
targets gives

\[
 \begin{aligned}
 \sum_S(n(S)-a)(n(S)-a-1)
   &=2P_{q,\sigma}-2aA+Na(a+1)\\
   &=2\bigl(P_{q,\sigma}-P_{\rm bal}(A,N)\bigr).
 \end{aligned}                                          \tag{3.8}
\]

Every missing target contributes exactly \(a(a+1)\) to the left side of
(3.8), and every other contribution is nonnegative.  This proves (3.6).
\(\square\)

Notice that (3.5) is the absolute minimum of \(P\) among all multiplicity
vectors of length \(N\) and total \(A\).  Indeed, if
\(A=aN+r\), then it equals

\[
 (N-r)\binom a2+r\binom{a+1}2.
\]

Thus (3.6) measures only collision energy above the unavoidable integral
floor; it does not charge the large forced multiplicity at deeper ranks.

### Theorem 3.4 (threshold robust-flow theorem)

Assume \(a=\lfloor A/N\rfloor\ge1\), and put

\[
 E=P_{q,\sigma}-P_{\rm bal}(A,N)\ge0.                   \tag{3.9}
\]

For any integer \(d\) with \(1\le d\le a\), delete the low-degree target
set

\[
 \mathcal Z_d=\{S:n_{q,\sigma}(S)<d\}.                  \tag{3.10}
\]

Then

\[
 \boxed{
 |\mathcal Z_d|
 \le {2E\over(a-d+1)(a-d+2)}.}                         \tag{3.11}
\]

Every target outside \(\mathcal Z_d\) can be assigned integrally to a
witnessing block so that no block receives more than

\[
 \boxed{c_d=\left\lceil {R\over d}\right\rceil}         \tag{3.12}
\]

assignments.

Thus \(d=1\) recovers full physical capacity and the hole bound (3.6), while
\(d=a\) gives a robust flow with capacity \(\lceil R/a\rceil\), after
deleting at most \(E\) low-degree targets.  Before the integer ceiling this
is within a factor

\[
 {A/N\over a}<1+{1\over a}
\]

of the forced average load \(N/t=R/(A/N)\).  The *integral* capacity
\(\lceil R/a\rceil\) is asymptotically equal to that forced average when
\(a\to\infty\) and, in addition, \(R/a\to\infty\) (equivalently here,
\(a=o(R)\)).  Without the latter condition the additive unit from the
ceiling need not be relatively negligible.

#### Proof

For \(n<d\), the smallest value of the polynomial in (3.7) occurs at
\(n=d-1\) and equals

\[
 (a-d+1)(a-d+2).
\]

Equation (3.8) therefore proves (3.11).

Now consider any family \(X\) of retained targets.  Every member has
incidence degree at least \(d\), so at least \(d|X|\) target--block
incidences leave \(X\).  Every neighboring block contains exactly \(R\)
depth-\(q\) colors and hence receives at most \(R\) of these incidences.
Therefore

\[
 |N(X)|\ge {d|X|\over R}.                               \tag{3.13}
\]

With \(c_d=\lceil R/d\rceil\),

\[
 c_d|N(X)|\ge |X|.
\]

The capacitated Hall criterion (2.1) now assigns every retained target with
block load at most \(c_d\).  \(\square\)

Theorem 3.4 is the strongest conclusion obtainable here by a plain
degree-averaging/Hall argument.  It is useful because it replaces every
exponential cut check by one quadratic energy bound.  It does not show that
the selected middle factor has small \(E\).

## 4. Simultaneous weighted deterministic theorem

Let \(w_{q,\sigma}\ge0\) be arbitrary deterministic weights.  Define

\[
 \mathfrak D_{q,\sigma}(\mathcal F)=
 \begin{cases}
 N_q-A+P_{q,\sigma},&A<N_q,\\[4pt]
 \displaystyle
 {2(P_{q,\sigma}-P_{\rm bal}(A,N_q))\over
   a_q(a_q+1)},&A\ge N_q,
 \end{cases}                                            \tag{4.1}
\]

where

\[
 a_q=\left\lfloor {A\over N_q}\right\rfloor.
\]

### Theorem 4.1 (weighted Stage-B certificate)

For every selected partial-block family,

\[
 \boxed{
 \sum_{q=1}^{H}\sum_{\sigma\in\{-,+\}}
 w_{q,\sigma}M_{q,\sigma}
 \le
 \sum_{q=1}^{H}\sum_{\sigma\in\{-,+\}}
 w_{q,\sigma}\mathfrak D_{q,\sigma}(\mathcal F).}       \tag{4.2}
\]

In particular, if the right side is \(o(W)\) for unit weights, all missing
central-band masks have total cardinality \(o(W)\).  Appending those masks
literally costs \(o(W)\).

#### Proof

Apply Corollary 3.3 separately to each depth and sign and sum.  Different
depths and the two signs consume no common physical capacity, so there is no
additional compatibility condition.  \(\square\)

### Corollary 4.2 (deterministic averaging)

Let \(\mu\) be any probability distribution on middle-disjoint
partial-block families having the same values of \(A,N_q\).  If

\[
 \sum_{q,\sigma}w_{q,\sigma}
 \mathbb E_\mu\mathfrak D_{q,\sigma}=o(W),               \tag{4.3}
\]

then at least one family in the support of \(\mu\) satisfies

\[
 \sum_{q,\sigma}w_{q,\sigma}M_{q,\sigma}=o(W).           \tag{4.4}
\]

Moreover, because (4.1) is affine in \(P_{q,\sigma}\) once \(A,N_q\) are
fixed, any sequential construction for which the conditional expectations
in (4.3) are available may be derandomized by choosing at every step an
option of no larger conditional expectation.

If the distribution is described by indicators \(X_B\) on an ambient block
pool, its required quadratic input is explicitly

\[
 \mathbb E P_{q,\sigma}
 =\sum_{\{B,B'\}}
   \Pr(X_B=X_{B'}=1)
   |C_{q,\sigma}(B)\cap C_{q,\sigma}(B')|.              \tag{4.5}
\]

Thus only pair-selection probabilities are needed to verify (4.3); no
high-order shadow-uniformity estimate is hidden in the averaging step.

#### Proof

Take expectations in (4.2).  Some outcome is no larger than the expectation.
The final assertion is the standard tower-property proof of the method of
conditional expectations.  \(\square\)

This is a genuine deterministic Stage-B route.  Its unproved input is not a
growing-uniformity matching theorem, but a distribution on already feasible
middle near-factors whose expected *excess pair overlap* satisfies (4.3).

## 5. Exact and asymptotic middle-leave rate

The capacity term in (1.6), summed over the two signs, is

\[
 \boxed{
 \Lambda_H(L)
   =2\sum_{q=1}^{H}\bigl(L-W(1-\rho_q)\bigr)_+.}         \tag{5.1}
\]

This is the exact minimum missing mass forced solely by having only
\(A=W-L\) window starts at every depth.  It is attained at the level of
unstructured multiplicity counts by using every occurrence on a different
target whenever \(A<N_q\).

The crude estimate

\[
 \Lambda_H(L)\le2HL                                    \tag{5.2}
\]

is often far from sharp.

### Lemma 5.1 (Gaussian leave law)

Let

\[
 \delta=L/W\to0.
\]

If \(m\delta\to\infty\) and

\[
 H/\sqrt{m\delta}\to\infty,
\]

then

\[
 \boxed{
 \Lambda_H(L)
  =\left({4\over3}+o(1)\right)
       W\sqrt m\,\delta^{3/2}.}                         \tag{5.3}
\]

If \(m\delta=O(1)\), then \(\Lambda_H(L)=O(W\delta)\).  Uniformly in both
regimes,

\[
 \Lambda_H(L)
   =O\!\left(W\delta+W\sqrt m\,\delta^{3/2}\right).      \tag{5.4}
\]

#### Proof

The exact product is

\[
 \rho_q=\prod_{j=0}^{q-1}{m-j\over m+j+1}.              \tag{5.5}
\]

First note the global one-sided estimate

\[
 \rho_q
 \le \exp\!\left(-\sum_{j=0}^{q-1}{2j+1\over m+j+1}\right)
 \le \exp\!\left(-{q^2\over m+q}\right).                \tag{5.6}
\]

Indeed \((m-j)/(m+j+1)=1-(2j+1)/(m+j+1)\le
\exp(-(2j+1)/(m+j+1))\).  Consequently, while
\(q^2/(m+q)\le1\),

\[
 1-\rho_q\ge {q^2\over2(m+q)}.                          \tag{5.7}
\]

For \(\delta=o(1)\), a positive summand in (5.1) must therefore have
\(q=O(\sqrt{m\delta})\).  This proves already that only \(O(1)\) summands
are positive when \(m\delta=O(1)\).

Uniformly for \(q=o(m^{2/3})\), Taylor expansion gives

\[
 -\log\rho_q
   ={q^2\over m}
    +O\!\left({q\over m}+{q^3\over m^2}\right).         \tag{5.8}
\]

On the relevant scale \(q=O(\sqrt{m\delta})=o(\sqrt m)\), and under
\(m\delta\to\infty\), the error in (5.8) is \(o(\delta)\).  Hence

\[
 1-\rho_q={q^2\over m}+o(\delta)                        \tag{5.9}
\]

uniformly on that scale.  The positive summands in (5.1) therefore end at

\[
 Q=(1+o(1))\sqrt{m\delta}.
\]

Using

\[
 \sum_{q=1}^{Q}q^2={Q^3\over3}+O(Q^2)
\]

in (5.1) gives

\[
 \begin{aligned}
 \Lambda_H(L)
 &=2W\sum_{q=1}^{Q}
       \left(\delta-{q^2\over m}+o(\delta)\right)\\
 &=2W\left(Q\delta-{Q^3\over3m}\right)
      +o(W\sqrt m\,\delta^{3/2})\\
 &=\left({4\over3}+o(1)\right)
      W\sqrt m\,\delta^{3/2}.
 \end{aligned}
\]

If \(m\delta=O(1)\), only \(O(1)\) summands can be positive, and each is at
most \(2W\delta\), giving \(O(W\delta)\).  In the unbounded regime,
(5.7) restricts all positive summands to
\(q=O(\sqrt{m\delta})\), and the same summation, with inequalities in place
of asymptotic equality, gives
\(O(W\sqrt m\,\delta^{3/2})\) even if \(H\) truncates the range.  This
proves (5.4).  \(\square\)

### Corollary 5.2 (sharp capacity threshold)

If

\[
 L=o(Wm^{-1/3}),                                        \tag{5.10}
\]

then

\[
 \Lambda_H(L)=o(W)                                     \tag{5.11}
\]

for every \(H\).  Conversely, if

\[
 L\sim cWm^{-1/3}\qquad(c>0)
\]

and \(H/m^{1/3}\to\infty\), then

\[
 \Lambda_H(L)\sim {4\over3}c^{3/2}W.                  \tag{5.12}
\]

#### Proof

Equation (5.11) follows from (5.4).  Equation (5.12) follows from (5.3).
\(\square\)

Thus \(o(W/H)\) is a convenient but unnecessarily strong leave hypothesis.
The exact condition is (5.1), and the band-independent power threshold is
\(o(Wm^{-1/3})\).

## 6. Why first-moment rank balance cannot prove Stage B

Let the full coordinate permutation group act on block families.  Fix one
integral family \(\mathcal F_0\), and choose a uniformly random coordinate
permutation \(g\).  For a fixed target \(S\in\mathcal V_q^\sigma\), target
transitivity and (1.4) give

\[
 \mathbb E_g n_{q,\sigma}^{g\mathcal F_0}(S)
   ={A\over N_q}.                                       \tag{6.1}
\]

Thus the orbit distribution is perfectly rank-balanced at the level of
every individual target.

On the other hand, relabelling only permutes the multiplicity vector.  Hence

\[
 M_{q,\sigma}(g\mathcal F_0)
   =M_{q,\sigma}(\mathcal F_0),\qquad
 P_{q,\sigma}(g\mathcal F_0)
   =P_{q,\sigma}(\mathcal F_0)                           \tag{6.2}
\]

for every \(g\).

### Proposition 6.1 (orbit-averaging obstruction)

No argument which uses only the exact first marginals (6.1) can bound the
missing count of an integral factor.  In particular, symmetrizing a bad
factor gives the exact fractional rank balance while every outcome retains
the same bad Hall cut and the same shadow deficit.

#### Proof

Equations (6.1)--(6.2) prove the claim.  If \(X\) is the set of missing
targets of \(\mathcal F_0\), then in the full-capacity network its
neighborhood is empty, so (2.1) has deficiency \(|X|\).  Relabelling merely
relabels this cut.  \(\square\)

The established native-fixed-pair partial-block factors provide a
Boolean-specific macroscopic instance of Proposition 6.1: at an appropriate
depth \(q=c\sqrt m\), every construction confined to that one coordinate
pairing has a positive-density target deficit, while its uniform relabelling
orbit has exact symmetric first marginals.  The orbit proposition itself
does not depend on that example.

## 7. Constant-one interface and precise proved boundary

The Stage-B contribution to a rank-balanced partial-block theorem can now be
stated without ambiguity.

Assume

\[
 H<\ell,\qquad H/\ell\to0,\qquad \ell=o(m),              \tag{7.1}
\]

and suppose a middle-disjoint block family has

\[
 \sum_{q=1}^{H}\sum_{\sigma\in\{-,+\}}
 \mathfrak D_{q,\sigma}(\mathcal F)=o(W).               \tag{7.2}
\]

Then Theorem 4.1 gives

\[
 \sum_{q=1}^{H}(M_{q,-}+M_{q,+})=o(W).                  \tag{7.3}
\]

No separate middle-leave hypothesis is needed here.  Indeed (1.6) at
\(q=1\) gives

\[
 L\le W-N_1+M_{1,-}={W\over m+1}+o(W)=o(W).             \tag{7.4}
\]

If one verifies (7.2) by separately bounding its forced-capacity and excess
pair-energy parts, Corollary 5.2 gives the convenient sharp sufficient
condition \(L=o(Wm^{-1/3})\) for the first part.  It is not an additional
hypothesis once the full condition (7.2) is known.

Copying the first \(H\) middle states of each cyclic block costs

\[
 Ht={H(W-L)\over2\ell}=o(W),                            \tag{7.5}
\]

and retains every cyclic shadow window through depth \(H\).  Applying the
endpoint-capped erosion compiler to the resulting paths may add one further
\(H\) entries per block.  Thus the complete copy-plus-endpoint overhead is
at most

\[
 2Ht={H(W-L)\over\ell}=o(W).                            \tag{7.6}
\]

The middle leave costs \(L=o(W)\), and the central-band shadow repairs cost
\(o(W)\) by (7.3).  Therefore, together with any independently proved
\(o(W)\) outer-tail word and the standard literal-OR transfer, these
hypotheses imply a word of length \(W+o(W)\).

What is proved here:

* the exact target-to-block max-flow and all its cuts;
* the fact that full physical capacity reduces its deficiency exactly to
  zero-occurrence targets;
* the sharp support-versus-pair-energy extremal theorem;
* the normalized weighted simultaneous Stage-B certificate;
* deterministic conditional-expectation rounding once a low-energy
  distribution of feasible Stage-A factors is available;
* exact component-overlay conditional expectation, together with its
  bounded-uniform-overlay lower bound;
* the exact middle-leave capacity sum and its sharp \(m^{-1/3}\) threshold;
* the orbit-averaging obstruction to every first-moment-only proof.

What is not proved:

* existence of a length-\(2\ell\) middle near-factor satisfying (7.3);
* a distribution on such near-factors with the low expected pair energy
  required by (4.3);
* an overlay system whose component products in (8.5) sum to `o(W)`;
* any implication from ordinary rank balance or ambient block codegrees to
  (7.3).

Accordingly, deterministic flow closes the assignment layer but not the
selection layer.  A positive Stage-B proof must control quadratic shadow
overlaps, full Hall cuts, or the zero-occurrence counts during the
construction of the middle near-factor itself.

## 8. A second non-nibble route: exact component-overlay averaging

There is one further deterministic averaging operation which preserves the
middle packing *exactly*.  It gives a useful positive theorem, but also a
sharp obstruction to proving Stage B from a bounded uniform overlay.

Let `k>=2`, and let `U` be a fixed set of middle masks.  For `1<=i<=k`, let
`F_i` be a partition of `U` into allowed locally geodesic blocks, all of
the same size `R`.  Form the `k`-partite incidence hypergraph whose vertices
are the labelled blocks `(i,B)`, and whose hyperedge indexed by `X in U` is

\[
 e_X=\{(i,B_i(X)):1\le i\le k\},                         \tag{8.1}
\]

where `B_i(X)` is the unique block of `F_i` containing `X`.  Let `K` range
over its connected components, and let `U_K` be the middle masks whose
hyperedges lie in `K`.

### Lemma 8.1 (exact component switch)

For every component `K` and every layer `i`, the blocks of `F_i` lying in
`K` partition exactly `U_K`.  Consequently, for an arbitrary map

\[
                         \phi:\{K\}\longrightarrow[k],  \tag{8.2}
\]

taking in component `K` all blocks from layer `phi(K)` produces another
partition `F_phi` of `U` into allowed locally geodesic `R`-blocks.  Moreover
every layer contributes exactly `|U_K|/R` blocks inside `K`; hence the total
block count and every uniform collar/seam charge are preserved exactly.

#### Proof

Every middle hyperedge in `K` meets one block vertex in each layer.  If a
block vertex lies in `K`, all of its incident middle hyperedges lie there as
well.  Thus the layer-`i` vertices in `K` partition precisely the common
edge-label set `U_K`.  Choosing one whole layer in each component therefore
preserves both coverage and disjointness.  Finally each chosen layer has
`|U_K|/R` blocks.  \(\square\)

Fix any collection `Sscr` of shadow targets, possibly simultaneously over
all depths and both signs.  For a target `S`, let

\[
 a_{K,i}(S)=\text{the number of occurrences of `S` among the layer-`i`
 blocks in `K`},
 \qquad
 h_K(S)=|\{i:a_{K,i}(S)>0\}|.                            \tag{8.3}
\]

### Theorem 8.2 (exact overlay missing formula)

Choose the values `phi(K)` independently and uniformly from `[k]`.  Then

\[
 \boxed{
 \Pr(S\text{ is missing from }F_\phi)
   =\prod_K\left(1-\frac{h_K(S)}k\right).}              \tag{8.4}
\]

Hence, for arbitrary nonnegative target weights `w_S`, some deterministic
integral component choice satisfies

\[
 \boxed{
 \sum_{S\in\mathscr S}w_S\mathbf1_{\{S\text{ missing}\}}
 \le
 \sum_{S\in\mathscr S}w_S
       \prod_K\left(1-\frac{h_K(S)}k\right).}           \tag{8.5}
\]

It can be found abstractly by fixing the components successively and always
choosing a value of no larger conditional expectation.

#### Proof

Component `K` fails to cover `S` precisely when `phi(K)` is one of its
`k-h_K(S)` zero-occurrence layers.  The choices are independent, proving
(8.4).  Sum (8.4) with weights and apply the tower property to obtain
(8.5).  Every intermediate and final choice is an integral exact middle
factor by Lemma 8.1.  \(\square\)

For `k=2`, if one component contains `S` on both sides, its missing
probability is zero.  Otherwise, if `d_S` is the number of components on
which `S` occurs on exactly one side, then (8.4) becomes the exact formula

\[
                         \Pr(S\text{ missing})=2^{-d_S}. \tag{8.6}
\]

Thus (8.5) is a genuine non-nibble sufficient condition for Stage B.  It
does not, however, follow from first marginals.  The following lower bound
locates the obstruction.

### Theorem 8.3 (bounded uniform-overlay obstruction)

Fix one target layer of size `N`.  Let `A_i` be the total number of its
occurrence slots in `F_i`.  Call a target **locked covered** if
`h_K(S)=k` for at least one component, let `G` be the number of such
targets, and put `E=N-G`.  If `E>0`, then the uniform overlay in Theorem
8.2 obeys

\[
 \boxed{
 \mathbb E M\ge
 E\,k^{-\frac{\sum_iA_i-kG}{(k-1)E}}.}                 \tag{8.7}
\]

If `E=0`, every target is covered for every component choice and there is
nothing to prove.  For `k=2` and `E>0`, put

\[
 T=A_1+A_2-2G,\qquad a=\lfloor T/E\rfloor,
 \qquad b=T-aE.
\]

Then the sharper integer bound is

\[
 \boxed{
 \mathbb E M\ge (E-b)2^{-a}+b2^{-(a+1)}.}              \tag{8.8}
\]

#### Proof

For every nonlocked target put `e_S=sum_K h_K(S)`.  Locked targets consume
at least `k` occurrence slots apiece, while each nonlocked positive
component-layer indicator consumes at least one slot.  Therefore

\[
             \sum_{S\text{ nonlocked}}e_S
             \le\sum_iA_i-kG.                          \tag{8.9}
\]

For `0<=h<=k-1`, concavity of `log(1-h/k)` above the chord joining its
values at `0` and `k-1` gives

\[
             1-\frac hk\ge k^{-h/(k-1)}.               \tag{8.10}
\]

Equations (8.4), (8.9), and Jensen's inequality for the convex decreasing
function `x mapsto k^{-x/(k-1)}` prove (8.7).  When `k=2`, a nonlocked
target has probability `2^{-d_S}` and `sum_S d_S<=T`.  The convex sequence
`2^{-d}` is minimized, for a fixed integer budget, by distributing the
budget as evenly as possible.  This is exactly (8.8).  \(\square\)

If `k` is fixed, `A_i<=W`, and `E>=epsilon W` in even one central-band
target layer, (8.7) gives

\[
 \mathbb E M\ge
 \epsilon W\,k^{-k/((k-1)\epsilon)}=\Omega_{k,\epsilon}(W). \tag{8.11}
\]

Also `G<=N-M_i` for every endpoint factor, because a locked target occurs
in every layer.  Therefore a bounded uniform component overlay can have
expected `o(W)` holes only if every input factor already has `o(W)` holes
in that layer.  The familiar one-giant-component case is the extreme:
the overlay only chooses one of its input factors.

This lower bound concerns the **uniform averaging certificate**.  A
specially correlated global solution of the component covering ILP could
beat its mean; (8.7) does not rule that out.  What it proves is that neither
rank-balanced first marginals nor a fixed number of uniform heat-bath
layers supplies the missing Stage-B estimate.  The exact positive input
needed by this route is the component product bound on the right of (8.5),
which is information strictly beyond rank balance.

Different middle leaves cause no logical problem.  Adjoin every uncovered
middle mask as a singleton atom in each input partition before forming
(8.1).  Component switching still partitions the whole middle layer into
`R`-blocks and literal singletons.  The number of `R`-blocks need no longer
be componentwise constant.  If `b(phi)` denotes that number, uniform
component choice gives the exact identity

\[
                    \mathbb E b(\phi)=\frac1k\sum_{i=1}^k|\mathcal F_i|.
                                                               \tag{8.12}
\]

Thus a seam price per selected `R`-block can be included in the same
conditional-expectation objective; in all cases `b(phi)<=W/R`.  The exact
baseline cancellation of literal singleton leaves from the sufficient
theorem is unchanged.
