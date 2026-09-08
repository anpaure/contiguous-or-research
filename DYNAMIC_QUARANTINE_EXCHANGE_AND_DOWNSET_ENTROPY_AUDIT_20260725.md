# Dynamic quarantine: exchange survival, exceptional colouring, and down-set entropy

Date: 2026-07-25

Method: pure mathematics only.

## 0. Outcome

Aggressive dynamic quarantine gives a genuine improvement over fixed
Bernoulli isolation.

1. Under three-antichain quarantine with
   \(\eta=m^{-12/5}\), all but a sufficiently sparse exceptional
   subhypergraph retain a \(1-o(1)\) fraction of their adjacent-switch
   neighbours.  After discarding \(o(W)\) exceptional target fibres, that
   exceptional subhypergraph can be greedily edge-coloured with \(o(D)\)
   colours.
2. The same conclusion is stronger under four-antichain quarantine.
3. Owner/priority feasibility being a down-set gives an exact entropy
   theorem: any feasible switch slice of relative density
   \(\rho=\exp(-o(f))\) retains \(1-o(1)\) of its aggregate lower switch
   squares.

These advances still do not prove the weighted matching cut.  Ambient
exchange degree does not imply exchange degree inside an arbitrary dual
weight support.  Moreover the down-set entropy theorem controls the total
number of squares, while the required pair-square kernel is a labelled
second moment.  The unsummed term is the collision multiplicity of
physical target-pair labels across different switch squares and different
slices.

## 1. Exchange-deficient schedules after quarantine

Fix one good tag fibre

\[
 \Omega\times Q_k,\qquad k=\Theta(m),
\]

and let \(A\) be the schedules surviving dynamic quarantine.  Suppose

\[
 |(\Omega\times Q_k)\setminus A|
 \le \eta|\Omega|2^k.
 \tag{1.1}
\]

Counting directed cube edges at their deleted endpoint gives

\[
 {1\over|A|}\sum_{x\in A}
 \#\{i:x\oplus e_i\notin A\}
 \le {k\eta\over1-\eta}.
 \tag{1.2}
\]

For \(a>0\), call \(x\) exchange-deficient if it has more than \(ak\)
missing switch neighbours.  Markov applied to (1.2) gives

\[
 \boxed{
 {|\{x\in A:x\text{ deficient}\}|\over|A|}
 \le {\eta\over a(1-\eta)}.}
 \tag{1.3}
\]

Write

\[
 \beta={\eta\over a(1-\eta)}.
 \tag{1.4}
\]

Thus every nondeficient schedule retains at least \((1-a)k\) legal switch
neighbours.

## 2. The deficient part costs only \(o(D)\) colours

The tag bound in (1.3) alone does not control concentration in target
stars.  The following second exceptional ledger is necessary.

### Theorem 2.1 (exceptional-subgraph colouring)

Suppose the full dynamically quarantined multicover has degree \(D\) in
every good tag fibre and edge size at most \(K+1\).  Let
\(\mathcal E_{\rm def}\) be a candidate family with at most \(\beta D\)
members in each tag.  For \(\tau>0\), declare a target exceptional when it
belongs to more than \(\tau D\) members of \(\mathcal E_{\rm def}\).
Then

\[
 \boxed{
 \#\{\text{exceptional targets}\}
 \le {K\beta T\over\tau}
 =O\left({Q\beta\over\tau}W\right).}
 \tag{2.1}
\]

After removing these target constraints, the deficient multihypergraph
has a proper edge colouring with at most

\[
 \boxed{
 1+(K+1)\max\{\beta,\tau\}D}
 \tag{2.2}
\]

colours.

#### Proof

The total number of deficient edge--target incidences is at most
\(K\beta DT\).  Every exceptional target accounts for more than
\(\tau D\) such incidences, proving (2.1).  On the remaining augmented
tag--target hypergraph, every tag degree is at most \(\beta D\) and every
target degree at most \(\tau D\).  Its line graph has maximum degree at
most

\[
 (K+1)\max\{\beta,\tau\}D.
\]

Greedy vertex colouring of that line graph proves (2.2). \(\square\)

For three-antichain quarantine take

\[
 \eta=m^{-12/5},\qquad
 a=m^{-2/5},\qquad
 \beta=m^{-2+o(1)},\qquad
 \tau=m^{-5/4}.
 \tag{2.3}
\]

Since \(K=m^{1+o(1)}\) and \(Q=m^{1/2+o(1)}\),

\[
 K\tau=m^{-1/4+o(1)}=o(1),
 \tag{2.4}
\]

and

\[
 {Q\beta\over\tau}=m^{-1/4+o(1)}=o(1).
 \tag{2.5}
\]

Hence the exchange-deficient candidates use only \(o(D)\) extra colours,
after charging \(o(W)\) exceptional target fibres, while every remaining
candidate retains at least

\[
 (1-m^{-2/5})k
\]

adjacent switch neighbours.

For four-antichain quarantine, the simpler choice

\[
 \eta=m^{-4},\qquad a=m^{-1},\qquad
 \beta=m^{-3+o(1)},\qquad \tau=m^{-3/2}
 \tag{2.6}
\]

gives \(K\tau=o(1)\) and \(Q\beta/\tau=o(1)\) with more room.

Thus dynamic quarantine really does isolate the final difficulty in an
exchange-rich core.

## 3. Why ambient exchange richness does not settle the weighted dual

The exact dual asks for

\[
 \nu_w\ge {w(E)\over(1+o(1))D}
 \tag{3.1}
\]

for every \(w\ge0\).  Equations (1.3)--(2.6) concern the unweighted
ambient catalogue.  An arbitrary weighting may place all its mass on a
set having no internal adjacent swaps.

The simplest example is a parity class in \(Q_k\): every ambient vertex
has all \(k\) switch neighbours, but every radius-one neighbour has
opposite parity and may have weight zero.  Radius-two switch squares
connect the parity class, so preserving squares is a real improvement.
Nevertheless a distance-three code has no other weighted point in its
radius-two ball and can have density of order \(1/k\).  With radius-three
control, a distance-four code gives the analogous obstruction.

This does not construct a geodesic matching counterexample.  It proves the
precise logical gap:

\[
 \boxed{\text{ambient switch survival}\not\Rightarrow
 \text{weighted augmenting-switch survival}.}
 \tag{3.2}
\]

To use the exchange-rich core in (3.1), one still needs a local-to-global
theorem saying that every high-weight restriction either

* contains enough weight-preserving switch squares/cubes to augment a
  matching, or
* is sufficiently code-sparse that Theorem 2.1, with a corresponding
  target-star ledger, colours it using \(o(D)\) colours.

No such weighted decomposition is presently proved.

There is some additional room under four-antichain quarantine.  The
target-fibre ledger only requires

\[
 \eta\gg Q\xi_4=m^{-9/2+o(1)}.
\]

Thus one may take, for example, \(\eta=m^{-22/5}\).  Then the fraction of
vertices whose complete radius-four ball is damaged is at most

\[
 \eta\sum_{j=0}^4\binom kj=m^{-2/5+o(1)}=o(1).
 \tag{3.3}
\]

A set with mutual distance at least five has density \(O(k^{-2})\) by
disjoint radius-two balls, and \(K/k^2=o(1)\).  This suggests a
radius-four weighted code/exchange decomposition, but arbitrary,
nonuniform weights and target-star concentration still have to be handled.
Equation (3.3) is therefore a concrete promising refinement, not a proof
of (3.1).

## 4. Exact entropy theorem for feasible down-sets

Let \(A\subseteq Q_f\) be a nonempty down-set, let \(X\) be uniform on
\(A\), and put

\[
 \rho={|A|\over2^f},\qquad
 b=\log_2{1\over\rho},\qquad
 \mu=\mathbb E|X|.
 \tag{4.1}
\]

### Theorem 4.1 (down-set square entropy)

\[
 \boxed{
 \mu\ge {f\over2}
 -\sqrt{{(\ln2)fb\over2}}.}
 \tag{4.2}
\]

Moreover the number of anchored lower switch squares, averaged per
feasible assignment, satisfies

\[
 \boxed{
 \mathbb E\binom{|X|}{2}
 \ge {\mu(\mu-1)\over2}.}
 \tag{4.3}
\]

Consequently, relative to the full-cube average
\(\binom f2/4=f(f-1)/8\),

\[
 \boxed{
 {\mathbb E\binom{|X|}{2}\over f(f-1)/8}
 \ge
 1-O\left(\sqrt{b/f}+1/f\right).}
 \tag{4.4}
\]

In particular, every down-set of density \(\exp(-o(f))\) retains
\(1-o(1)\) of its aggregate lower switch squares.

#### Proof

Downward closure gives \(\Pr(X_i=1)\le1/2\).  Entropy subadditivity and
concavity give

\[
 f-b=H(X)
 \le\sum_i h_2(\Pr(X_i=1))
 \le f h_2(\mu/f).
 \tag{4.5}
\]

For \(0\le u\le1/2\),

\[
 1-h_2(1/2-u)\ge {2u^2\over\ln2}.
 \tag{4.6}
\]

Substitute \(u=1/2-\mu/f\) into (4.5)--(4.6) to obtain (4.2).
Every pair of one-coordinate descents from \(x\in A\) spans a full lower
square in \(A\).  Thus the square count at \(x\) is
\(\binom{|x|}{2}\).  Convexity gives (4.3), and substitution of (4.2)
gives (4.4). \(\square\)

There is also a useful size-biased slice form.  Suppose owner conditioning
produces subcubes \(Q_{f_\omega}\), priority conditioning produces
down-sets \(A_\omega\), and

\[
 \sum_\omega |A_\omega|
 \ge z\sum_\omega2^{f_\omega}.
 \tag{4.7}
\]

For any \(L_0>1\), slices with relative density

\[
 {|A_\omega|\over2^{f_\omega}}<{z\over L_0}
\]

contain at most a \(1/L_0\) fraction of all feasible assignments.  Hence,
if \(z\ge1/\log m\), \(L_0=\log m\), and \(f_\omega=\Theta(m)\) outside a
negligible family, Theorem 4.1 gives \(1-o(1)\) aggregate square survival
on all but \(o(1)\) feasible mass.

The unproved hypotheses in this application are important: the current
residual theorem does not yet give (4.7) at every tag, nor does it show
that almost all size-biased owner subcubes have \(f_\omega=\Theta(m)\).

## 5. The exact unsummed pair-square term

Theorem 4.1 is a first-moment square statement.  The hereditary kernel
condition is a labelled second-moment statement.

For a feasible slice \(\omega\), let

\[
 N_\omega(x,y)
\]

be the number (or current priority weight) of its feasible assignments
whose relevant switch square carries the physical target-pair label
\((x,y)\).  Entropy controls an aggregate of the form

\[
 \sum_{\omega,x,y}N_\omega(x,y).
 \tag{5.1}
\]

The pair-square block instead contains

\[
 \boxed{
 \sum_{x,y}
 { \left(\sum_\omega N_\omega(x,y)\right)^2
  \over d_A(x)d_A(y)}.}
 \tag{5.2}
\]

Expanding the square in (5.2) exposes the unsummed cross-slice term

\[
 \boxed{
 \sum_{x,y}\sum_{\omega\ne\omega'}
 {N_\omega(x,y)N_{\omega'}(x,y)
  \over d_A(x)d_A(y)}.}
 \tag{5.3}
\]

Neither cube isoperimetry nor the down-set entropy bound controls (5.3).
Many entropy-rich slices may send their surviving squares to the same
small family of physical target pairs.  This is exactly the square-label
dispersal/four-walk term which appears as transfer energy in the propagation
audit.

Thus the entropy theorem proves:

\[
 \boxed{\text{dense feasible down-sets retain many switch squares},}
\]

but the remaining theorem is still:

\[
 \boxed{\text{those squares are dispersed over physical target-pair
 labels strongly enough to give the }z^{-2}\text{ block bound}.}
\]

This identifies a concrete unsummed term rather than an unspecified
failure of concentration.

