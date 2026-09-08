# Balanced moving frames: an exact fractional all-depth orbit and the independent-mixing collision no-go

Date: 2026-07-26

Method: pure mathematics only.  No computation, search, solver, or web
input is used.

## 0. Outcome

Continue with

\[
 \Omega=[2m],\qquad W=\binom{2m}{m},\qquad
 N_q=\binom{2m}{m-q},\qquad H<m.                              \tag{0.1}
\]

The collective owner-frame theorem removed the \(H\)-collar charge from
cross-box transitions.  This note attacks its remaining collision energy

\[
 \Xi_H=\sum_{q=1}^H
 \left[
  \sum_T(\mu_q^-(T)-1)_+
 +\sum_U(\mu_q^+(U)-1)_+
 \right].                                                     \tag{0.2}
\]

There are three exact conclusions.

### No component-state obstruction

A maximal physical \(C_{2m}\)-strip is a cyclic coordinate order

\[
 z=(z_0,z_1,\ldots,z_{2m-1}),\qquad
 X_t=\{z_t,\ldots,z_{t+m-1}\}.                                 \tag{0.3}
\]

For every \(1\le q<m\), its lower and upper window maps are injective on
all \(2m\) phases.  Thus every single component has zero internal
collision energy at every controlled depth.

More strongly, take the complete coordinate-relabeling orbit of (0.3) and
allow every phase an independently chosen truncated radius \(\rho_t\).
There is an exact symmetric fractional distribution under which every
middle owner and every signed target at every \(q\le H\) has load one.
Therefore no point/profile/statewise linear functional separates the
balanced maximal-strip atlas from the all-depth target.

### Independent component mixing is linearly bad

Suppose component \(i\) exposes \(r_{i,q}\) distinct targets at depth \(q\),
the exact census is

\[
                         \sum_i r_{i,q}=N_q,                    \tag{0.4}
\]

and the components are conjugated independently and uniformly by
coordinate permutations.  Then the expected number \(M_q\) of missing
targets is exactly

\[
 \boxed{
 \mathbb E M_q
 =N_q\prod_i\left(1-\frac{r_{i,q}}{N_q}\right).}                \tag{0.5}
\]

For long physical components \(r_{i,q}\le2m\), so

\[
                         \mathbb E M_q=(e^{-1}+o(1))N_q.         \tag{0.6}
\]

Moreover \(M_q=(e^{-1}+o(1))N_q\) with probability \(1-o(1)\).
At

\[
                         q=A\sqrt m+O(1),\qquad A>0,             \tag{0.7}
\]

this is

\[
 \boxed{
 M_q=(e^{-1-A^2}+o(1))W=\Omega_A(W).}                           \tag{0.8}
\]

Hence independent random frames, independent component relabelings, and
diffuse product rounding cannot prove \(\Xi_H=o(W)\).  A single common
global relabeling is equally useless: it only permutes target names and
leaves \(\Xi_H\) unchanged.

### The exact remaining gate is correlated integral resolution

The maximal-strip orbit nevertheless has excellent pairwise geometry.
For one signed rank \(m-q\), \(q\ge1\), the normalized codegree of two
distinct targets in the cyclic-interval orbit is \(O(1/m)\).  At the middle
rank the only large codegree is the forced antipodal pair
\(\{X,X^c\}\); after contracting these pairs, the normalized codegrees are
again \(O(1/m)\).

This does not itself give an integral near-factor.  One augmented component
contains \(\Theta(m^{3/2})\) expected all-depth vertices when
\(\sqrt m\ll H=o(m)\), so a fixed-uniformity nibble theorem is inapplicable;
small normalized codegree alone is insufficient for growing-rank
hypergraphs.

The strongest non-PBBS fallback is therefore the following exact theorem:

> **Correlated maximal-strip orbit resolution.**  Select a correlated,
> owner-disjoint family of relabelled maximal strips and nested radius
> vectors so that the uncovered augmented vertices over all signed ranks
> \(q\le H\) have total size \(o(W)\).

Such a selection gives \(\Xi_H=o(W)\) and \(O(W/m)=o(W/H)\) components
for \(H=o(m)\).  The present note proves that the fractional point is exact,
that no statewise capacity obstruction exists, and that independent
rounding stays a linear distance from it.  It does not prove the correlated
integral resolution.

For the balanced recursion \(B_{2s}\times B_{2s}=B_{4s}\), put \(m=2s\).
All conclusions above then apply with \(W=\binom{4s}{2s}\).

## 1. Maximal strips have no internal collisions

Let \(z\) be a cyclic order of \(\Omega\), with indices modulo \(2m\), and
define \(X_t\) by (0.3).  The transition is

\[
                         X_{t+1}=X_t-z_t+z_{t+m}.                \tag{1.1}
\]

It is a physical maximal strip, and every proper window is signed safe.
Its depth-\(q\) targets are

\[
 \begin{aligned}
 D_q(t)&=\bigcap_{j=0}^qX_{t+j}
        =\{z_{t+q},\ldots,z_{t+m-1}\},\\
 E_q(t)&=\bigcup_{j=0}^qX_{t+j}
        =\{z_t,\ldots,z_{t+m+q-1}\}.
 \end{aligned}                                                 \tag{1.2}
\]

### Lemma 1.1 (proper cyclic intervals are distinct)

For a cyclic order on \(n\) distinct points and any
\(1\le k<n\), its \(n\) cyclic intervals of length \(k\) are distinct.

#### Proof

A nonempty proper cyclic interval is determined by its two boundary edges
in the cyclic order.  Two starts giving the same interval would give the
same entering boundary, hence the same start. \(\square\)

### Corollary 1.2 (zero diagonal collision)

For every \(1\le q<m\), both maps

\[
                         t\longmapsto D_q(t),\qquad
                         t\longmapsto E_q(t)                     \tag{1.3}
\]

are injective.  Thus a maximal strip contributes zero within-component
terms to \(\Xi_H\).

#### Proof

The sets in (1.2) are cyclic intervals of lengths \(m-q\) and \(m+q\),
both proper.  Apply Lemma 1.1. \(\square\)

Consequently a positive lower bound for \(\Xi_H\) cannot be statewise in
the sense of charging every long component.  Any obstruction must compare
different components or constrain their integral assembly.

## 2. Exact symmetric fractional all-depth cover

Put

\[
                         p_q=\frac{N_q}{W}\qquad(0\le q\le H),   \tag{2.1}
\]

where \(p_0=1\).  These numbers decrease with \(q\).  Let a truncated radius
\(\rho\in\{0,\ldots,H\}\) have distribution

\[
 \Pr(\rho\ge q)=p_q,\qquad
 \Pr(\rho=q)=p_q-p_{q+1},                                      \tag{2.2}
\]

with \(p_{H+1}=0\).

Choose a uniformly random oriented cyclic order \(z\) of \(\Omega\), and
independently assign the \(2m\) phases iid radii
\(\rho_0,\ldots,\rho_{2m-1}\) with law (2.2).  Form one augmented block
\({\cal B}(z,\rho)\) containing

1. all \(2m\) middle intervals \(X_t\);
2. \(D_q(t)\) whenever \(\rho_t\ge q\); and
3. \(E_q(t)\) whenever \(\rho_t\ge q\),

for every \(q\le H\).

By Corollary 1.2 this is a set, rather than a multiset, on every rank.

### Theorem 2.1 (exact orbit fractional point)

For every augmented vertex \(V\)—a middle owner or a signed target at any
depth \(q\le H\)—

\[
                         \Pr(V\in{\cal B}(z,\rho))
                         =\frac{2m}{W}.                          \tag{2.3}
\]

Consequently, multiplying the probability law of
\({\cal B}(z,\rho)\) by \(W/(2m)\) gives a fractional perfect matching of
the complete augmented owner-and-target hypergraph.

#### Proof

For a fixed middle owner \(X\), each of the \(2m\) cyclic \(m\)-intervals
is uniformly distributed over \(\binom{\Omega}{m}\), and by Lemma 1.1 at
most one can equal \(X\).  Therefore

\[
                         \Pr(X\in{\cal B})=\frac{2m}{W}.         \tag{2.4}
\]

Fix a lower target \(T\) of rank \(m-q\).  At one phase,
\(D_q(t)\) is uniform over its layer, and the independent eligibility
probability is \(p_q\).  Again the \(2m\) interval targets are distinct, so

\[
 \Pr(T\in{\cal B})
 =\frac{2m\,p_q}{N_q}
 =\frac{2m}{W}.                                                 \tag{2.5}
\]

The same calculation applies to an upper target.  This proves (2.3).
Scaling the block law by the reciprocal vertex load gives one unit at
every augmented vertex. \(\square\)

The theorem uses one common radius at both signs of a root, so lower and
upper nesting is coupled exactly.  It is not a product of separate
one-depth fractional points.

It also shows why a profile or marginal Hall obstruction cannot close this
route.  Every literal vertex has exactly the correct fractional load,
simultaneously at all depths.

There is a useful stronger symmetry.  Instead of choosing the \(2m\)
phase radii independently, choose one radius on each antipodal phase pair
\(\{t,t+m\}\), independently between pairs, and put

\[
                         \rho_{t+m}=\rho_t.                      \tag{2.6}
\]

Every phase still has marginal law (2.2), so Theorem 2.1 is unchanged.

### Corollary 2.2 (blockwise sign contraction)

Under (2.6),

\[
                         E_q(t+m)=D_q(t)^c                       \tag{2.7}
\]

whenever the phase is eligible.  Thus the upper target set of every block
is exactly the complement image of its lower target set.  Likewise
\(X_{t+m}=X_t^c\).

Consequently the augmented integral problem may contract middle complement
pairs and lower/upper target-complement pairs.  After this contraction,
exact lower coverage implies exact upper coverage component by component.

#### Proof

Using (1.2), the complement of
\[
D_q(t)=\{z_{t+q},\ldots,z_{t+m-1}\}
\]
is the cyclic interval
\[
\{z_{t+m},\ldots,z_{t+2m+q-1}\}=E_q(t+m).
\]
The eligibility equivalence is (2.6), and the middle identity follows from
(0.3). \(\square\)

## 3. The exact independent-mixing formula

Fix one signed depth \(q\) and let

\[
                         {\cal T}_q=\binom{\Omega}{m-q},
 \qquad |{\cal T}_q|=N_q.                                      \tag{3.1}
\]

For \(i=1,\ldots,c\), let \(S_i^0\subseteq{\cal T}_q\) be the distinct
depth-\(q\) targets exposed by an internally injective component template,
and put

\[
                         r_i=|S_i^0|.                            \tag{3.2}
\]

Choose independent uniform coordinate permutations \(\pi_i\), and set

\[
                         S_i=\pi_iS_i^0.                         \tag{3.3}
\]

The orbit need not be uniform over all \(r_i\)-subsets of
\({\cal T}_q\).  Only transitivity on individual targets is used.

### Theorem 3.1 (Poisson-one missing mass)

Assume

\[
                         \sum_i r_i=N_q.                         \tag{3.4}
\]

Then (0.5) holds.  If \(L=\max_i r_i=o(N_q)\), then

\[
                         \mathbb E M_q=(e^{-1}+O(L/N_q))N_q.     \tag{3.5}
\]

If in addition \(L=O(m)\), then for every fixed
\(\varepsilon>0\),

\[
 \Pr\left(|M_q-\mathbb EM_q|\ge\varepsilon N_q\right)
 \le2\exp\left(-\frac{\varepsilon^2N_q}{2L}\right).             \tag{3.6}
\]

#### Proof

Fix \(T\in{\cal T}_q\).  Coordinate transitivity and internal injectivity
give

\[
                         \Pr(T\in S_i)=\frac{r_i}{N_q}.          \tag{3.7}
\]

The choices \(\pi_i\) are independent, so

\[
 \Pr\left(T\notin\bigcup_iS_i\right)
 =\prod_i\left(1-\frac{r_i}{N_q}\right).                        \tag{3.8}
\]

Summing (3.8) over \(T\) proves (0.5).

Since

\[
 \sum_i r_i^2\le L\sum_i r_i=LN_q,                              \tag{3.9}
\]

the expansion \(\log(1-x)=-x+O(x^2)\), together with (3.4), gives

\[
 \sum_i\log\left(1-\frac{r_i}{N_q}\right)
 =-1+O(L/N_q),                                                 \tag{3.10}
\]

which proves (3.5).

Changing one permutation \(\pi_i\) changes the union size, and hence the
hole count, by at most \(2r_i\).  The bounded-difference inequality gives

\[
 \Pr(|M_q-\mathbb EM_q|\ge\varepsilon N_q)
 \le2\exp\left(
 -\frac{2\varepsilon^2N_q^2}{4\sum_i r_i^2}\right).
 \tag{3.11}
\]

Apply (3.9) to obtain (3.6). \(\square\)

For a physical component \(r_i\le|C_i|\le2m\), so the hypotheses are
automatic.  The result remains valid when the component templates, their
orientations, and their radius vectors are chosen adversarially before the
independent conjugations.

This is an optimistic target-only experiment: independently conjugated
components need not be owner-disjoint.  Conditioning on exact owner
factorhood can evade the conclusion only by introducing strong correlations
between the component conjugations.  Those correlations are precisely the
integral gate isolated in Section 8.

### Corollary 3.2 (Gaussian-depth linear obstruction)

If \(q=A\sqrt m+O(1)\), then

\[
                         \frac{N_q}{W}=e^{-A^2}+o(1).            \tag{3.12}
\]

Under independent component conjugation and the exact census,

\[
                         M_q=(e^{-1-A^2}+o(1))W                 \tag{3.13}
\]

with probability \(1-o(1)\).  Therefore \(\Xi_H=\Omega_A(W)\) whenever
this depth is controlled.

#### Proof

The adjacent-binomial product gives

\[
 \frac{N_q}{W}
 =\prod_{j=0}^{q-1}\frac{m-j}{m+j+1}
 =e^{-q^2/m+o(1)}.                                             \tag{3.14}
\]

Combine (3.5)--(3.6) with (3.14).  Missing targets equal repeat excess at
the exact census, so they are a summand of \(\Xi_H\). \(\square\)

The same calculation at \(q=1\) gives
\((e^{-1}+o(1))W\) missing first shadows.  Thus postponing correlation to
the Gaussian rows cannot repair an independently assembled first row.

## 4. Pair energy confirms the same obstruction

Define the cross-component pair collision energy

\[
                         P_q=\sum_{i<j}|S_i\cap S_j|.            \tag{4.1}
\]

### Proposition 4.1 (independent pair overlap)

Under the hypotheses of Theorem 3.1,

\[
 \mathbb EP_q
 =\frac1{N_q}\sum_{i<j}r_ir_j
 =\frac{N_q^2-\sum_i r_i^2}{2N_q}
 =\left(\frac12-o(1)\right)N_q.                                \tag{4.2}
\]

#### Proof

For a fixed target, the two independent membership probabilities are
\(r_i/N_q\) and \(r_j/N_q\).  Summing over targets gives
\(\mathbb E|S_i\cap S_j|=r_ir_j/N_q\).  Sum over pairs and use
(3.4) and (3.9). \(\square\)

Thus neither a second-moment argument nor an independent discrepancy
rounding begins near the integral floor.  The desired family must impose
negative correlations of linear total strength between different
components.

## 5. A common relabeling has zero effect

Let a completed component family have target multiplicities
\(\mu_q^\pm\), and apply one coordinate permutation \(\pi\) to every
component.  Then

\[
                         \mu_{q,\pi}^\pm(T)
                         =\mu_q^\pm(\pi^{-1}T).                  \tag{5.1}
\]

### Proposition 5.1 (global-orbit rigidity)

Every permutation-invariant collision functional, including \(\Xi_H\),
is unchanged by one common coordinate relabeling.

#### Proof

Equation (5.1) merely permutes the entries of every target histogram.
The summands \((x-1)_+\) are symmetric in those entries. \(\square\)

There is therefore an exact dichotomy:

* one common relabeling preserves the old collision energy exactly;
* independent relabelings drive the target occupancy to the
  Poisson-one regime and leave a linear number of holes.

The useful regime must be a deliberately correlated intermediate orbit
selection.

## 6. Same-rank codegrees of the maximal-strip orbit

The preceding no-go is not caused by large pairwise codegrees.  The
cyclic-interval orbit is locally sparse.

Fix

\[
                         n=2m,\qquad k=m-q,\qquad q\ge1.         \tag{6.1}
\]

Let \(I\) be any set of at most \(r\le2m\) eligible phases of one cyclic
order, and let \(S_I\) be its family of length-\(k\) intervals at those
phases.  Relabel the coordinates uniformly.

### Lemma 6.1 (conditional two-interval count)

For distinct \(k\)-sets \(T,T'\), put

\[
                         d=|T\setminus T'|=|T'\setminus T|.      \tag{6.2}
\]

Then

\[
 \Pr(T'\in S_I\mid T\in S_I)
 \le
 \begin{cases}
 \displaystyle
 \frac{2}{\binom{k}{d}\binom{n-k}{d}},&1\le d<k,\\[4mm]
 \displaystyle
 \frac{r}{\binom{n-k}{k}},&d=k.
 \end{cases}                                                   \tag{6.3}
\]

#### Proof

Condition on the unique eligible phase whose interval is \(T\).  If two
cyclic \(k\)-intervals overlap and differ in \(d<k\) points, their starts
have cyclic displacement \(d\) or \(-d\), giving at most two candidate
phases.  At one such displacement, the \(d\) departing members form a
uniform \(d\)-subset of \(T\), and the \(d\) entering members form an
independent uniform \(d\)-subset of its complement.  The probability of
the prescribed pair is the reciprocal product in (6.3).

If \(T,T'\) are disjoint, there are at most \(r\) candidate eligible
phases.  At each one the \(k\) coordinates occupying that interval form a
uniform \(k\)-subset of the \(n-k\) coordinates outside \(T\).  This gives
the second bound. \(\square\)

### Corollary 6.2 (small normalized codegree)

Uniformly for

\[
                         1\le q\le H=o(m),                       \tag{6.4}
\]

the normalized codegree of two distinct lower targets in the maximal-strip
orbit is

\[
                         O(1/m).                                \tag{6.5}
\]

The same holds for upper targets.

#### Proof

For \(1\le d<k\), the first line of (6.3) is maximized at \(d=1\), giving
\(2/[k(n-k)]=O(m^{-2})\).  For disjoint targets,

\[
 \binom{n-k}{k}
 =\binom{m+q}{2q}\ge\binom{m+1}{2},
\]

so the second line is \(O(m^{-1})\) because \(r\le2m\).
Complementation turns upper intervals of length \(m+q\) into lower
intervals of length \(m-q\). \(\square\)

At the middle rank \(q=0\), every maximal strip contains \(X\) together
with \(X^c\), so this antipodal pair has normalized codegree one.  It is
the physical chunk constraint, not an accidental collision.  Contracting
middle owners into complement pairs removes it; all other middle-pair
codegrees obey the overlapping case of Lemma 6.1.

## 7. Why the codegree estimate does not finish the proof

Under the fractional law of Section 2,

\[
 \mathbb E|{\cal B}(z,\rho)|
 =2m+4m\sum_{q=1}^Hp_q.                                      \tag{7.1}
\]

When \(\sqrt m\ll H=o(m)\), the Gaussian estimate gives

\[
                         \sum_{q=1}^Hp_q=\Theta(\sqrt m),        \tag{7.2}
\]

and hence

\[
                         \mathbb E|{\cal B}|=\Theta(m^{3/2}).    \tag{7.3}
\]

Thus the augmented hypergraph has growing rank.  The implication

\[
 \text{fractional perfect matching}
 +\text{normalized codegree }o(1)
 \Longrightarrow\text{integral near-perfect matching}          \tag{7.4}
\]

is false for growing-rank hypergraphs in general: finite projective planes
already have codegree/degree tending to zero while every two edges meet.
Accordingly a fixed-uniformity nibble theorem cannot be invoked here
without an additional interval-specific expansion or absorber theorem.

The antipodal owner quotient and the nested radius choices are also coupled:
one may not round the signed depth layers independently and then hope to
recover common components.

## 8. Exact correlated resolution gate

Let \({\cal H}_{m,H}^{\rm strip}\) be the augmented multiple-choice
hypergraph whose vertices are

\[
 \binom{\Omega}{m}
 \mathbin{\dot\cup}
 \bigcup_{q=1}^H
 \left(
 \binom{\Omega}{m-q}^-\mathbin{\dot\cup}
 \binom{\Omega}{m+q}^+
 \right),                                                     \tag{8.1}
\]

and whose edges are the blocks \({\cal B}(z,\rho)\).

Theorem 2.1 gives an exact fractional perfect matching in
\({\cal H}_{m,H}^{\rm strip}\).  An integral matching in this hypergraph is
an owner-disjoint family of maximal strips with no signed target collision
at any controlled depth.  If its uncovered augmented target mass is
\(o(W)\), and its selected edge types realize the prescribed rank
incidences with total \(o(W)\) error, then its complete collision/missing
ledger is \(o(W)\).  Since every component has \(2m\) owners, its component
count is at most

\[
                         \frac{W}{2m}+o(W/m)=o(W/H)              \tag{8.2}
\]

whenever \(H=o(m)\).

The exact unresolved theorem is not ordinary matching alone, because the
edge sizes vary with \(\rho\) and the desired selected family must have the
correct total incidence on every rank.  Equivalently one may split edge
types by their nested radius-count vector and seek a near-perfect
multi-type matching realizing the fractional mixture (2.2).

### Theorem 8.1 (audited dichotomy)

For the balanced moving-frame maximal-strip atlas, exactly one of the
following must supply the next advance.

1. A correlated multi-type matching/absorption theorem for
   \({\cal H}_{m,H}^{\rm strip}\) leaves \(o(W)\) augmented targets
   uncovered.  Then \(\Xi_H=o(W)\), the component toll is \(o(W)\), and
   the balanced-product fallback reaches the coefficient-one central gate.
2. There is an integral odd-set, residue, or interval-union cut separating
   the exact fractional point of Theorem 2.1 from every such near-matching
   by \(\Omega(W)\).

No statewise/profile cut can be such an obstruction: individual blocks are
internally injective and the symmetric fractional point loads every literal
vertex exactly.  The independent-mixing theorem shows, however, that a
proof must construct linear-strength negative correlation; random
componentwise conjugation remains \(\Omega(W)\) away from the target.

This is the precise surviving non-PBBS backup.
