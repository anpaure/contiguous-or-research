# Audit of the reachable exceptional-link construction

Date: 2026-07-26

Audited file:
MATH_THEOREM_RPRN_REACHABLE_EXCEPTIONAL_LINK_COUNTEREXAMPLE_20260726.md.

## 0. Verdict

The parameter calculation and static construction are correct.  The
matching is a matching in the **actual repaired promotion-ring
hypergraph**, not in an abstract analogue, and marking exactly its edges
makes the resulting state support-reachable.

The original draft nevertheless did not prove a literal counterexample to
**RPRN(z)** under the natural meaning of a *residual root link*.  It proved
that the exceptional owners cover almost every root in the static
containment graph

\[
 A\sim X\quad\Longleftrightarrow\quad A\subset X,
\]

but not that a surviving catalogue edge contains both \(A\) and \(X\).
Deleting the matching can in principle erase an entire root--owner
pair-link even when both vertices survive.  The theorem file has therefore
been corrected to claim only the static-containment obstruction and to
isolate the extra residual-link estimate.

There were also two small errors and one filtration gap in Lemma 3.1.
They have been repaired without changing any parameter scale.

Finally, positive support probability for each fixed \(m\) refutes only an
**every-reachable-state** hereditary statement.  It does not refute a
with-high-probability assertion for the unbiased nibble.

## 1. Parameters and static counts: verified

Put

\[
 Q=\binom{M}{H},\qquad \alpha={m^2\over Q}.
\]

A root \(A\) has exactly \(Q\) containing middle owners, so the Bernoulli
family has mean root incidence \(\alpha Q=m^2\).  Since

\[
 \log Q=\Theta\!\bigl(H\log(m/H)\bigr)
\]

at the packing height, \(\alpha m^C=o(1)\) for every fixed \(C\).
Chernoff plus \(N_H\le4^m\) therefore gives simultaneously

\[
 {m^2\over2}\le d_{\mathcal F}(A)\le2m^2
\]

for every root, and
\(|\mathcal F|=(1+o(1))\alpha W=o(W)\).

The repaired-catalogue identities are normalized correctly:

\[
 d(A)=R,\qquad d(X)=D=\rho R,
\]

and for \(d_J(X,Y)=1\),

\[
 d(X,Y)=D{2(r-1)\over r m^2}.
\]

Every repaired path through \(X\) has one or two distance-one neighbours
of \(X\).  Hence covering \(\delta m^2\) distinct members of
\(\Gamma(X)\) destroys at least

\[
 {1\over2}\delta m^2D{2(r-1)\over rm^2}
 =\delta {r-1\over r}D
\]

edges through \(X\).  The constant-degree loss in Section 4 is correct.

The matching-size calculation is also correct:

\[
 |\mathcal M|=O(\alpha Wm^2),\qquad
 {|\mathcal M|\over N_H}=O(\alpha m^3)=o(1).
\]

The ambient average-loss estimates have the correct normalization:

\[
 {r|\mathcal M|D\over N_HR}=O(\alpha m^4)=o(1),
 \qquad
 {|\mathcal M|r(R+rD)\over WD}=O(\alpha m^4)=o(1).
\]

Consequently all but \(o(N_H)\) roots and \(o(W)\) owners have degree
\((1-o(1))\) of their original degree.

Finally,

\[
 W\binom mH=N_HQ
\]

and \(|\mathcal F\setminus\mathcal F'|=o(|\mathcal F|)\) imply that the
static containment neighbourhood of \(\mathcal F'\) contains
\((1-o(1))N_H\) roots.  Equations (6.1)--(6.3) are correct as static
containment statements.

## 2. Repairs to the scheduling lemma

### 2.1 The diagonal member of \(\mathcal F\)

The quantity

\[
 D^{-1}\sum_{Z\in\mathcal F}d(Y,Z)
\]

is an upper bound for the fraction of the link of \(Y\) meeting
\(\mathcal F\) only when \(Y\notin\mathcal F\).  The corrected quantity is

\[
 \widetilde c_{\mathcal F}(Y)
 =\mathbf1_{\{Y\in\mathcal F\}}
  +{1\over D}\sum_{Z\in\mathcal F\setminus\{Y\}}d(Y,Z).
\]

Its mean is

\[
 {1\over W}\sum_Y\widetilde c_{\mathcal F}(Y)
 ={r|\mathcal F|\over W}=(1+o(1))\alpha r=o(1),
\]

so the correction is asymptotically free.

### 2.2 Available fraction

Two forbidden fractions of at most \(1/4\) and the same-cluster fraction
of at most \(1/8\) leave at least \(3/8\), not “more than half”, of the
link available.  This still gives a bounded expected number of trials.

### 2.3 Adaptive revelations

Candidate tests reveal memberships of future owners in \(\mathcal F\).
The repaired proof caps the tests at \(C\log m\), discards selected owners
whose membership was revealed before their priority was reached, and
processes only fresh selected owners.

There are

\[
 O(\alpha Wm^3\log m)=o(W)
\]

out-of-order membership queries.  The expected number of queried positives
is

\[
 O(\alpha^2Wm^3\log m)
 =o(\alpha W)=o(|\mathcal F|),
\]

because \(\alpha m^C=o(1)\) for every fixed \(C\).  Markov's inequality
allows all these positives to be discarded.  The remaining processed
owner is fresh and uniform relative to the filtration.  A good listed
target has at least a \(3/8\) available fraction, and \(C\log m\) failed
tests have probability \((5/8)^{C\log m}=m^{-\Omega(C)}\).  This makes the
number of capped failures \(o(|\mathcal F|m^2)\), completing the scheduler
at the stated scale.

## 3. Exact missing residual-link estimate

For \(A\subset X\), the original root--owner pair degree is

\[
 K=d(A,X)={rR\over Q}.
\]

If Lemma 3.1 could additionally give, for all but
\(o(|\mathcal F|)\) targeted owners,

\[
 c_0D\le d_{\rm res}(X)\le(1-c_1)D                \tag{3.1}
\]

with fixed \(c_0,c_1>0\), then the literal residual-link obstruction
would follow.  The edges through \(X\) are partitioned by their root, and
each root contributes at most \(K\) edges.  Thus \(X\) would occur in at
least

\[
 {c_0D\over K}
 =c_0{Q\over\lambda_H}
 =c_0\binom mH
\]

surviving root links.  Every root has at most \(2m^2\) containers in
\(\mathcal F\).  Hence the union of the surviving root links meeting the
exceptional owners would have size at least

\[
 {c_0|\mathcal F'|\binom mH\over2m^2}
 =(c_0/2-o(1))N_H.
\]

This is \(\Omega(N_H)\), already enough to contradict an \(o(N_H)\)
exceptional-link clause; the stronger \(1-o(1)\) conclusion is
unnecessary.

The source proof establishes the upper inequality in (3.1), but not the
lower one.  It is plausible to add it by bounding final cross-cluster
influence on the random family: edges assigned to \(X\) cost at most
\(40\delta D\), while fresh Bernoulli membership should make the influence
from other clusters \(o(D)\) for all but \(o(|\mathcal F|)\) owners.
That extra filtration calculation is not presently proved.

## 4. Logical scope

After the scheduling repairs, the construction is an actual matching of
the repaired owner catalogue.  The event that exactly its edges are marked
has positive probability for each finite \(m\), so the state is genuinely
support-reachable.

This proves that static degrees, codegrees, path influence and small-mesh
information cannot imply a deterministic theorem covering **every** state
in the support of the nibble.  It does not contradict a statement asserted
with probability \(1-o(1)\), because the prescribed marking event may have
probability tending to zero arbitrarily fast.

Under the static-containment reading of “meet a root link”, the corrected
file gives the statewise counterexample.  Under the literal residual-link
reading, it becomes a complete counterexample only after (3.1) is proved.
Until then its exact status is: a genuine support-reachable
static-containment obstruction plus a well-specified residual-link gate,
not a completed refutation of **RPRN(z)**.
