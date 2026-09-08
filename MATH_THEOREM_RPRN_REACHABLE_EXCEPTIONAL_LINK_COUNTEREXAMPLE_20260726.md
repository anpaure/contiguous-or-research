# A support-reachable residual defeating literal RPRN regeneration

Date: 2026-07-26

Scope: constant-one packing only.  This note uses the repaired promotion-ring
catalogue and its exact path influence estimate.  It concerns the trajectory
statement `RPRN(z)`, not another static codegree estimate.

## 0. Verdict

Let

\[
 W=\binom{2m}{m},\qquad N_H=\binom{2m}{m-H},\qquad
 M=m+H,
\]

where \(H\) is the packing-side height, and retain a repaired path of
length \(r=M-k\), with \(1\le k=o(m)\).  Write \(R\) and \(D=\rho R\) for
the root and owner degrees of the simple rooted catalogue.

There is a matching \(\mathcal M\) with

\[
 |\mathcal M|=o(N_H)                                             \tag{0.1}
\]

such that, after deleting its roots and owners, there is a family
\(\mathcal F'\) of surviving owners satisfying

\[
 |\mathcal F'|=o(W),\qquad
 d_{\rm res}(X)\le (1-c)D\quad(X\in\mathcal F')                  \tag{0.2}
\]

for an absolute constant \(c>0\), while

\[
 \bigl|\{A\text{ surviving}:\text{ some residual edge contains }
              A\text{ and an }X\in\mathcal F'\}\bigr|
       \ge(4/5-o(1))N_H.                                        \tag{0.3}
\]

At the same time, all but \(o(N_H)\) roots retain degree
\((1-o(1))R\), and all but \(o(W)\) owners retain degree
\((1-o(1))D\).  Thus the owners in \(\mathcal F'\) are genuinely
exceptional relative to the common residual scale, while their literal
surviving root--owner links meet a positive fraction of the root shore.
This contradicts the exceptional-link clause in the residual-link reading
of RPRN.

The residual is reachable in one marking round: mark exactly the edges of
\(\mathcal M\) and no others.  Since \(\mathcal M\) is a matching, every
marked edge is isolated and accepted.  This event has positive probability
for every fixed \(m\).

Consequently:

\[
 \boxed{\text{literal RPRN regeneration cannot hold for every
 support-reachable residual.}}                                  \tag{0.4}
\]

This does **not** refute a high-probability theorem for the unbiased
nibble.  It identifies the necessary extra content of that theorem: one
must prove that the unbiased trajectory avoids sparse root-covering owner
families; static path influence and absence of small odd meshes do not
imply that avoidance.

## 1. Inputs from the repaired catalogue

The argument uses only the following already proved facts.

1. Every repaired edge contains one root and \(r\) owners.  The degrees
   are

   \[
   d(A)=R,\qquad d(X)=D=\rho R,\qquad \rho=1-o(1).                \tag{1.1}
   \]

2. If \(X,Y\) are owners at Johnson distance one, then

   \[
   d(X,Y)=D\,{2(r-1)\over r m^2}.                                \tag{1.2}
   \]

3. For an owner \(X\notin e\), put

   \[
   a_X(e)=|\{f:X\in f,\ f\cap e\ne\varnothing\}|.
   \]

   The repaired-path estimate is

   \[
   a_X(e)\le {20+o(1)\over m^2}D.                               \tag{1.3}
   \]

4. A repaired path containing \(X\) contains at least one and at most two
   owners at Johnson distance one from \(X\).  The lower assertion uses
   only \(r\ge2\); the upper assertion is the path property.

For an owner \(X\), let

\[
 \Gamma(X)=\{Y:d_J(X,Y)=1\}.
\]

Then

\[
 |\Gamma(X)|=m^2.                                                \tag{1.4}
\]

The construction exploits the distinction between the two roles of
\(\Gamma(X)\).  It is only polynomially large, so a sparse matching can
delete a positive fraction of it.  Nevertheless every option through
\(X\) must pass through it.

## 2. A sparse root-covering family of owners

Put

\[
 Q=\binom MH,qquad L=m^2,qquad \alpha={L\over Q}.               \tag{2.1}
\]

At the packing-side height,

\[
 Q=\exp\!\bigl(\Theta(H\log(m/H))\bigr),
\]

and therefore

\[
 \alpha m^C=o(1)\quad\text{for every fixed }C.                  \tag{2.2}
\]

Choose every owner independently with probability \(\alpha\), obtaining
a preliminary family \(\mathcal F\).  A fixed root \(A\) is contained in
exactly \(Q\) owners, so

\[
 |\{X\in\mathcal F:A\subset X\}|\sim\operatorname {Bin}(Q,\alpha)
\]

has mean \(L=m^2\).  Chernoff's inequality and a union bound over
\(N_H\le4^m\) roots show that with probability \(1-o(1)\), simultaneously
for every root,

\[
 {L\over2}\le |\{X\in\mathcal F:A\subset X\}|\le2L.             \tag{2.3}
\]

Also

\[
 |\mathcal F|=(1+o(1))\alpha W=o(W).                             \tag{2.4}
\]

Fix a realization having (2.3)--(2.4), together with the scheduling
property proved next.

## 3. Sparse boundary-deletion lemma

### Lemma 3.1

There are an absolute \(\delta>0\), a subfamily
\(\mathcal F'\subseteq\mathcal F\), and a matching \(\mathcal M\) such
that

\[
 |\mathcal F\setminus\mathcal F'|=o(|\mathcal F|),               \tag{3.1}
\]

no edge of \(\mathcal M\) contains an owner of \(\mathcal F\), and, for
every \(X\in\mathcal F'\), the owner set covered by \(\mathcal M\)
contains at least \(\delta m^2\) distinct members of \(\Gamma(X)\).
In addition,

\[
 \sum_{e\in\mathcal M}a_X(e)\le(40\delta+o(1))D
 \qquad(X\in\mathcal F').                                      \tag{3.8}
\]

Moreover

\[
 |\mathcal M|\le 2\delta m^2|\mathcal F|
       =O(\alpha Wm^2)=o(N_H).                                   \tag{3.2}
\]

#### Proof

We give the averaging argument because this is the genuinely dynamic
step.  For a matching \(\mathcal Q\), define the fraction of the owner
link of \(Y\) blocked by \(\mathcal Q\) by

\[
 b_{\mathcal Q}(Y)
 =D^{-1}|\{f:Y\in f,\ f\cap V(\mathcal Q)\ne\varnothing\}|.
\]

If \(Y\notin V(\mathcal Q)\), then (counting conflicts with multiplicity)

\[
 b_{\mathcal Q}(Y)
 \le {1\over D}\sum_{e\in\mathcal Q}a_Y(e).                     \tag{3.3}
\]

For this counting paragraph only, extend the notation to \(Y\in e\) by
putting \(a_Y(e)=D\); this is exactly the number of edges through \(Y\)
which meet \(e\).  For a fixed catalogue edge \(e\), interchange the
order of counting.
Every edge \(f\) meeting \(e\) is counted once for each of its \(r\)
owners, while the number of such \(f\) is at most \(R+rD\).  Hence

\[
 {1\over W}\sum_Y {a_Y(e)\over D}
 \le {r(R+rD)\over WD}=O\!\left({m^2\over W}\right).            \tag{3.4}
\]

Consequently, as long as

\[
 |\mathcal Q|\le 2\delta\alpha Wm^2,
\]

the mean cross-cluster blocked fraction is

\[
 {1\over W}\sum_Y b_{\mathcal Q}(Y)
       =O(\alpha m^4)=o(1).                                     \tag{3.5}
\]

There is a second forbidden set: the owners of \(\mathcal F\) themselves
must survive.  For every \(Y\), an upper bound for the fraction of its
link meeting \(\mathcal F\) is

\[
 c_{\mathcal F}(Y)
 =\mathbf1_{\{Y\in\mathcal F\}}
  +{1\over D}\sum_{Z\in\mathcal F\setminus\{Y\}}d(Y,Z).
\]

Since every edge through \(Z\) contains \(r-1\) other owners,

\[
 \sum_Yd(Y,Z)=D(r-1).
\]

Therefore, for every fixed \(\mathcal F\),

\[
 {1\over W}\sum_Yc_{\mathcal F}(Y)
       ={|\mathcal F|\over W}r
       =(1+o(1))\alpha r=o(1).                                   \tag{3.6}
\]

We now run the Bernoulli choice of \(\mathcal F\) and the randomized
greedy schedule as one joint experiment.  Give all owners independent
continuous priorities, reveal membership in \(\mathcal F\) in priority
order, and process the selected owners in that order.  On reaching \(X\),
expose a random list of \(2\delta m^2\) distinct members of
\(\Gamma(X)\).  A listed owner
already covered by the current matching counts as a success.  Otherwise
try to choose an edge through it which avoids the current matching and all
of \(\mathcal F\).  Memberships needed to test a candidate edge are
revealed at that moment.  Cap the number of candidate tests at
\(K=C\log m\), where \(C\) is a sufficiently large absolute constant.
Every owner whose positive membership is revealed before its priority is
reached is put in an exposure-exception set and is not later processed as
a cluster centre.

There are at most

\[
 O(\alpha Wm^3\log m)=o(W)
\]

out-of-order membership queries.  Each newly queried membership is still
an independent Bernoulli variable of mean \(\alpha\).  Hence the expected
number of positive exposure exceptions is

\[
 O(\alpha^2Wm^3\log m)=o(\alpha W)=o(|\mathcal F|).
\]

Markov's inequality lets us discard all of them at a cost
\(o(|\mathcal F|)\).  After this deletion, the next processed selected
owner is fresh and uniform on the unexposed owner set; the latter omits
only \(o(W)\) vertices.  This is the filtration point needed below.

The targets in a random distance-one list have uniform owner marginal,
by transitivity of the Johnson graph.  Conditional on the exposed
data, the next processed owner is uniform on the unexposed owner set.
Thus (3.5) applies conditionally with an \(o(1)\) change.  The still-unexposed
memberships in \(\mathcal F\) remain independent Bernoulli variables, so
(3.6) also applies conditionally in expectation.  Summing the conditional
expectations and using Markov's inequality shows that only
\(o(|\mathcal F|m^2)\) listed targets have cross-cluster or
\(\mathcal F\)-blocked fraction larger than \(1/4\).  This conclusion
holds with probability \(1-o(1)\), and hence simultaneously with the
root-covering event (2.3).

It remains to control edges already chosen while processing the same
\(X\).  Before \(2\delta m^2\) successes have been sought, (1.3) gives,
for every uncovered target \(Y\),

\[
 {1\over D}\sum_{e\text{ chosen for }X}a_Y(e)
       \le (40+o(1))\delta.                                     \tag{3.7}
\]

Choose, for example, \(\delta=1/400\).  Then (3.7) is less than \(1/8\)
for all sufficiently large \(m\).  For every nonexceptional listed target,
at least \(1-1/4-1/4-1/8=3/8\) of its link is therefore still available.
The chance that all \(K=C\log m\) random candidate tests fail is
\((5/8)^K=m^{-\Omega(C)}\).  Taking \(C\) large makes the total number of
such failures \(o(|\mathcal F|m^2)\).  Summing these failures and the
exceptional targets, and applying Markov
once more over \(X\in\mathcal F\), all but \(o(|\mathcal F|)\) clusters
obtain at least \(\delta m^2\) distinct covered neighbours.  Call this
preliminary family \(\mathcal F_0\).  At most one new matching edge is
used for each success, proving the first inequality in (3.2).

It remains to retain a lower bound on the attacked centres themselves.
For \(X\in\mathcal F_0\), let \(\mathcal M_X\) be the edges chosen while
processing \(X\).  Since every candidate edge avoids \(\mathcal F\), it
avoids \(X\); hence (1.3) gives

\[
 \sum_{e\in\mathcal M_X}a_X(e)
 \le |\mathcal M_X|{20+o(1)\over m^2}D
 \le(40+o(1))\delta D.                                         \tag{3.9}
\]

The cross-cluster load is smaller.  Conditional on a chosen edge \(e\)
and on all earlier exposures, a fresh centre has uniform owner marginal
up to \(o(1)\).  By (3.4),

\[
 \mathbb E\!\left[
 \sum_{X\in\mathcal F_0}
  \sum_{e\in\mathcal M\setminus\mathcal M_X}a_X(e)\right]
 \le(1+o(1))\alpha|\mathcal M|\,r(R+rD).                        \tag{3.10}
\]

After division by \(|\mathcal F|D=(1+o(1))\alpha WD\), the right side
of (3.10) is

\[
 O\!\left({|\mathcal M|m^2\over W}\right)
 =O(\alpha m^4)=o(1).                                          \tag{3.11}
\]

Markov's inequality therefore permits deletion of another
\(o(|\mathcal F|)\) centres so that the cross-cluster sum is \(o(D)\)
at every remaining centre.  Let the remaining family be
\(\mathcal F'\).  Combining this conclusion with (3.9) proves (3.8).

Finally, by (2.2) and \(N_H=W/\lambda_H\) with
\(\lambda_H=\Theta(m)\),

\[
 {\alpha Wm^2\over N_H}=\alpha m^2\lambda_H=O(\alpha m^3)=o(1),
\]

which proves the last assertion of (3.2).  The randomized construction
has positive probability of satisfying all displayed estimates, so a
deterministic realization exists. \(\square\)

### Remark 3.2 (why the static \(m^{-2}\) estimate does not regenerate)

The same estimate (1.3) has opposite effects at two scales.  It makes a
cluster of fewer than \(m^2/40\) prescribed deletions schedulable, because
their total same-cluster obstruction is bounded away from one.  But a
positive fraction of the \(m^2\) distance-one boundary is already enough
to remove a positive fraction of an owner's whole link.  Thus
\(m^{-2}\) external influence is compatible with a sparse coordinated
attack on \(o(W)\) owners.

## 4. Constant link loss on every selected exceptional owner

Fix \(X\in\mathcal F'\), and let

\[
 T_X=\Gamma(X)\cap V(\mathcal M),\qquad |T_X|\ge\delta m^2.
\]

By (1.2),

\[
 \sum_{Y\in T_X}d(X,Y)
 =|T_X|D{2(r-1)\over rm^2}.                                     \tag{4.1}
\]

An edge through \(X\) contains at most two distance-one neighbours of
\(X\).  Hence every destroyed edge is counted at most twice in (4.1), and

\[
 |\{f:X\in f,\ f\cap T_X\ne\varnothing\}|
 \ge {1\over2}\sum_{Y\in T_X}d(X,Y)
 \ge \delta{r-1\over r}D.                                      \tag{4.2}
\]

No edge of \(\mathcal M\) contains \(X\), because \(\mathcal M\) avoids
\(\mathcal F\).  Thus \(X\) survives, while (4.2) gives

\[
 d_{\rm res}(X)\le
 \left(1-\delta{r-1\over r}\right)D
 \le(1-\delta/2)D                                               \tag{4.3}
\]

for all sufficiently large \(m\).  We may take \(c=\delta/2\) in (0.2).

The new estimate (3.8) gives the complementary inequality.  Every
catalogue edge through \(X\) which disappears meets at least one selected
edge, so the union bound in the other direction yields

\[
 D-d_{\rm res}(X)
 \le\sum_{e\in\mathcal M}a_X(e)
 \le(40\delta+o(1))D.
\]

Consequently

\[
 \boxed{(1-40\delta-o(1))D
 \le d_{\rm res}(X)
 \le(1-\delta/2)D\qquad(X\in\mathcal F').}                      \tag{4.4}
\]

Thus the attacked owners have a constant defect but are not annihilated.

## 5. The ambient residual is still regular at scale one

Put \(s=|\mathcal M|=o(N_H)\).  The selected edges use \(s\) roots and
\(rs\) owners.

For root degrees, the total loss over all unselected roots is at most
\(rsD\): each selected owner lies in \(D\) catalogue edges.  Therefore

\[
 {rsD\over N_HR}= {rs\rho\over N_H}
 =O\!\left({ms\over N_H}\right)
 =O(\alpha m^4)=o(1).                                           \tag{5.1}
\]

For owner degrees, use (3.4).  The total link loss over all owners is at
most

\[
 s\,r(R+rD),
\]

and hence its mean, normalized by \(D\), is

\[
 {sr(R+rD)\over WD}=O\!\left({sm^2\over W}\right)
 =O(\alpha m^4)=o(1).                                           \tag{5.2}
\]

Markov's inequality applied with any threshold tending to zero sufficiently
slowly now gives

\[
 d_{\rm res}(A)=(1-o(1))R
\]

for all but \(o(N_H)\) surviving roots, and

\[
 d_{\rm res}(X)=(1-o(1))D
\]

for all but \(o(W)\) surviving owners.  In particular the constant loss
in (4.3) cannot be hidden by redefining the common residual scale
\(R_t\) or \(\rho_tR_t\).

## 6. Static containment versus actual surviving pair-links

For a surviving root \(A\) and owner \(X\), write

\[
 \Lambda_{\rm res}(A,X)=
 \mathbf1_{\{\exists f\text{ residual}:A,X\in f\}}.              \tag{6.1}
\]

This is the literal root--owner link required by RPRN; it is stronger
than \(A\subset X\).

Every owner contains exactly \(\binom mH\) roots, and

\[
 W\binom mH=N_H\binom MH=N_HQ.                                  \tag{6.2}
\]

For every containment \(A\subset X\), the original pair degree is

\[
 K=d(A,X)={rR\over Q}={D\over\binom mH}.                         \tag{6.3}
\]

The residual edges through a fixed owner \(X\) are partitioned by their
root.  Each nonempty residual pair-link contributes at most its original
size \(K\).  Therefore (4.4) forces

\[
 |\{A:\Lambda_{\rm res}(A,X)=1\}|
 \ge {d_{\rm res}(X)\over K}
 \ge(1-40\delta-o(1))\binom mH
 \qquad(X\in\mathcal F').                                      \tag{6.4}
\]

Thus at most \((40\delta+o(1))\binom mH\) of the static containments
below any \(X\in\mathcal F'\) fail to be actual residual links.

We now sum these failures.  The discarded centres
\(\mathcal F\setminus\mathcal F'\) contribute

\[
 o(|\mathcal F|)\binom mH=o(N_HL),                              \tag{6.5}
\]

while the actual-link failures below \(\mathcal F'\) contribute at most

\[
 (40\delta+o(1))|\mathcal F|\binom mH
 =(40\delta+o(1))N_HL.                                         \tag{6.6}
\]

Every root has at least \(L/2\) containers in \(\mathcal F\).  Hence a
root with no actual residual link to \(\mathcal F'\) accounts for at
least \(L/2\) incidences in (6.5)--(6.6).  The number of such roots is at
most

\[
 (80\delta+o(1))N_H.                                           \tag{6.7}
\]

The matching itself deletes only \(o(N_H)\) roots.  Consequently

\[
 \boxed{
 |\{A\text{ surviving}:\exists X\in\mathcal F',
       \ \Lambda_{\rm res}(A,X)=1\}|
 \ge(1-80\delta-o(1))N_H.}                                     \tag{6.8}
\]

With \(\delta=1/400\), the right side is
\((4/5-o(1))N_H\).  This is a literal residual-link obstruction, not a
static-containment surrogate.

## 7. Reachability and the exact logical consequence

In one round of the marking rule, the event

\[
 \{\text{the marked edge set is exactly }\mathcal M\}
\]

has strictly positive probability.  Because \(\mathcal M\) is a matching,
all its edges are isolated among the marked edges and are accepted.  The
resulting residual is precisely the one above.  Its surviving root fraction
is

\[
 1-{s\over N_H}=1-o(1),                                         \tag{7.1}
\]

so it occurs before the stopping density \(z\) for every fixed \(z<1\).

This proves a statewise, support-reachable obstruction to hereditary
literal-link regeneration.  It does not say that the event has
nonvanishing probability under the unbiased nibble.  Accordingly the
conclusions are exactly:

* static codegrees, path influence, EKR, and small-mesh density do not
  imply literal-link regeneration after arbitrary support-reachable
  conditioning;
* a proof of typical `RPRN(z)` must include a trajectory statement ruling
  out sparse root-covering exceptional owner families;
* the minimal natural additional observable is the containment energy

  \[
  \mathcal E_t(\mathcal B)
   =\bigl|\{A:\exists X\in\mathcal B,\ A\subset X\}\bigr|
  \]

  for low-degree owner sets \(\mathcal B\), not merely their cardinality
  or the maximum path influence.

The obstruction is not an odd mesh and has no small matching-number
certificate.  Its mechanism is a sparse transversal of root containment
neighbourhoods followed by a coordinated deletion of distance-one
boundaries with a simultaneous lower bound on the attacked owner links.
This is why the two repaired static theorems do not see it.
