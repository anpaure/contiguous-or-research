# A pair-quota-aware diamond near-factor

Date: 2026-07-27

## 0. Outcome

For prime (p=2r-1\), the Catalan excess design can be chosen so that the
prescribed q1 diamond catalogue admits a near-perfect matching which never
overuses any forced swap-pair quota.

The device is elementary: add a fifth vertex part containing one labelled
slot for every required use of each swap pair.  The resulting hypergraph is
5-uniform, asymptotically regular, and has maximum codegree (o(D)).  The
ordinary fixed-uniformity nibble then gives the desired quota-aware matching.

This removes the new second-order obstruction from the *near-factor* stage.
It does not supply exact cover-down: the leftover still has to be rearranged
into coherent cells before the ladder absorbers apply.

## 1. Forced swap quotas

Let (D\subseteq\binom{[p]}{r+1}) be a simple Catalan excess design and put

\[
w(A)=1+\mathbf1_D(A).
\]

The prescribed upper load vector forces the total number of transitions
whose swap pair is ({i,j}) to be

\[
h^*_{ij}=d_D(\{i,j\})-C_{r-1}.                     \tag{1.1}
\]

Assume (h^*_{ij}\ge0) for every pair.  Double counting gives

\[
\sum_{i<j}h^*_{ij}=W.                              \tag{1.2}
\]

Indeed, every selected diamond has exactly one swap pair, while the pair
identity in the prescribed-design audit gives (1.1).  Equivalently, using
(p=2r-1),

\[
\frac{W}{\binom p2}
=\frac{C_{r-1}}{r-1}=:H.                           \tag{1.3}
\]

For the random prime-orbit design, pair-degree concentration strengthens the
previous floor to

\[
h^*_{ij}=(1+o(1))H                                 \tag{1.4}
\]

uniformly over the (O(r^2)) pairs.  This follows from the same weighted
hypergeometric Bernstein estimate used for the pair floor: the mean is

\[
\mathbb E d_D(ij)=\frac r{r-1}C_{r-1},
\]

and both its upper and lower relative tails are exponentially smaller than
(r^{-2}).

## 2. The augmented five-partite hypergraph

Start with the four parts

\[
P_L,\quad P_U,\quad P_0,\quad P_1
\]

of the oriented-diamond hypergraph.  Add a fifth part

\[
P_Q=\{(\{i,j\},t):1\le t\le h^*_{ij}\}.
\tag{2.1}
\]

By (1.2), every part has size (W).

For every oriented diamond with lower set (X), upper slot ((A,s)),
middle clones ((Y,0),(Z,1)), and swap pair

\[
\{i,j\}=A\setminus X,
\]

insert one augmented edge for each quota slot
((\{i,j\},t)\).  A matching in this 5-graph projects to a diamond matching,
and it uses each swap pair at most (h^*_{ij}) times automatically.

## 3. Degree calculation

Put

\[
B=\binom{2r-3}{r-1},
\qquad
R=2B=Hr(r-1).                                      \tag{3.1}
\]

The identities (C_{r-1}=2B/r) and (1.3) give the second equality.

For a fixed quota slot of pair (ij),

\[
d_Q(ij,t)
=2\left(B+d_D(ij)\right)
=(1+o(1))R.                                        \tag{3.2}
\]

For a lower vertex (X),

\[
d_L(X)
=2\sum_{\{i,j\}\subseteq X^c}w(X+i+j)h^*_{ij}
=(1+o(1))R,                                        \tag{3.3}
\]

because there are \(\binom r2\) base terms, only \(O(r)\) doubled terms for
the quasirandom (D), and (1.4) holds uniformly.

For an upper slot ((A,s)),

\[
d_U(A,s)
=2\sum_{\{i,j\}\subseteq A}h^*_{ij}
=(1+o(1))R.                                        \tag{3.4}
\]

The ratio between the leading quantities in (3.4) and (3.1) is
((r+1)/(r-1)=1+O(1/r)).

Finally, for a middle clone ((Y,\epsilon)), exactly one orientation of the
diamond (Y-b\subset Y+a) uses that clone, so

\[
d_{M_\epsilon}(Y)
=\sum_{a\notin Y}\sum_{b\in Y}w(Y+a)h^*_{ab}
=(1+o(1))R.                                        \tag{3.5}
\]

Thus every vertex degree is ((1+o(1))R).

## 4. Codegrees

Two vertices in the same part have codegree zero.  Across distinct parts,
fixing the two vertices determines either

- the whole lower--upper interval, leaving at most (2h^*_{ij}=O(R/r^2))
  choices;
- one exchanged coordinate and at most (O(rH)=O(R/r)) choices; or
- a fixed quota slot, leaving only (O(r)) choices.

Consequently

\[
\Delta_2=O(R/r)=o(R).                              \tag{4.1}
\]

The estimates remain valid for the orbit design because (1.4) is uniform
and (w(A)\le2).

## 5. Quota-aware near-factor theorem

### Theorem 5.1

For prime (p=2r-1\to\infty), there is a simple Catalan excess design (D)
and a matching of prescribed diamonds which

1. covers all but (o(W)) vertices in each of the four original parts;
2. uses every upper slot and every middle/lower resource at most once; and
3. satisfies
   \[
   h^M_{ij}\le h^*_{ij}
   \]
   for every swap pair, leaving only (o(W)) unused quota slots in total.

### Proof

Choose (D) by the prime-orbit sampling theorem, adding the uniform pair
concentration (1.4).  Sections 3--4 show that the augmented hypergraph is
fixed-5-uniform, ((1+o(1))R)-regular, and has maximum pair codegree
(o(R)).  The fixed-uniformity near-perfect matching theorem therefore gives
a matching covering all but (o(W)) of its (5W) vertices.  Project away
the quota part.  Since each pair has exactly (h^*_{ij}) labelled slots,
the projected matching cannot overuse it, and the number of unused slots is
the uncovered part of (P_Q), namely (o(W)).  \(\square\)

### Theorem 5.2 (uniform early-stop margin)

The matching in Theorem 5.1 can be chosen so that, simultaneously for every
pair,

\[
h^M_{ij}\le \left(1-\frac1r\right)h^*_{ij},
\tag{5.1a}
\]

while it still covers \(W-o(W)\) vertices in each original part.

#### Proof

Start with the augmented near-perfect matching \(M_0\) from Theorem 5.1 and
retain each of its edges independently with probability

\[
\rho=1-\frac2r.
\]

For a fixed pair \(ij\), its retained usage is stochastically dominated by
\(\operatorname{Bin}(h^*_{ij},\rho)\).  Since

\[
\min_{i<j}h^*_{ij}=(1+o(1))H
\]

and \(H=C_{r-1}/(r-1)\) is exponential in \(r\), Chernoff's inequality gives

\[
\Pr\!\left[
h^M_{ij}>\left(1-\frac1r\right)h^*_{ij}
\right]
\le
\exp\{-\Omega(H/r^2)\}.
\]

A union bound over \(O(r^2)\) pairs tends to zero.  A second Chernoff bound
gives

\[
|M|\ge\left(1-\frac3r\right)|M_0|
=W-o(W)
\]

with probability tending to one.  Any retained subfamily is still a
matching, so one realization satisfies both conclusions.  \(\square\)

Thus the pair-defect of the leave has the coordinatewise margin

\[
\Delta_{ij}(\mathrm{leave})
=h^M_{ij}-h^*_{ij}
\le-\frac1r h^*_{ij}
=-(1+o(1))\frac{W}{2r^3}.
\tag{5.1b}
\]

## 6. Exact residual gate

For the projected matching (M), the pair-defect identity from the absorber
audit is

\[
\Delta_{ij}(\mathrm{leave})=h^M_{ij}-h^*_{ij}\le0.
\tag{6.1}
\]

Hence the quadratic mixed-cell obstruction cannot arise from aggregate pair
**overuse** in this near-factor.  What remains is a deterministic re-pairing
theorem in the full five-part geometry.

There is an important qualification.  A single nonedge coherent cell cannot
be absorbed independently while the labelled quota vertices are fixed.  An
absorber with (q) reservoir edges and (q+1) absorbing edges has net swap
inventory exactly one basis vector—the label of the newly supplied quota
slot.  By contrast, the coherent ladder's four-part swap difference is
spread over (2t+1) coordinate pairs and has both signs.  Its quota changes
must therefore cancel against those of other cells.

The corrected deterministic target is consequently one of the following:

1. partition the five-part leftover directly into legal augmented diamonds;
   or
2. partition it into batches of coherent/mixed cells whose **aggregate** swap
   difference equals their multiset of unused quota slots, and braid their
   ladder absorbers through a quota-exchange network.

Uncontrolled mixed cells can require (Theta(r^2)) reservoir edges each.
Thus the augmented nibble pays the exact aggregate second-order quotas but
does not yet prove a perfect matching.
