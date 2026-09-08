# Coherent endpoint queues: fixed-colour dead ends and a polynomial mixed-SCD alphabet escape

Date: 2026-07-26

Method: pure mathematics only.  No computation, finite search, solver, or
web input is used.

## 0. Outcome

Let

\[
 H=\sqrt m\,\omega(m),\qquad \omega(m)\longrightarrow\infty,
 \qquad H=o(m).                                      \tag{0.1}
\]

The arbitrary-history countercuts in
`MATH_OBSTRUCTION_PRODUCT_SCD_ENDPOINT_ROBUST_DEGREE_ZERO_20260726.md`
and
`MATH_OBSTRUCTION_BTK_PRODUCT_SCD_ENDPOINT_RECORD_TAIL_CUT_20260726.md`
already close uniform robust degree.  This note does not repeat their
average-degree arguments.  It changes the quantifier to histories produced
by the route itself.

There are two exact conclusions.

### Fixed-colour coherent no-go

Let (P) be an intact BTK product diagonal of length (h\ge5), traversed
completely to an endpoint.  Its own direction word places every coordinate
of its (A)-record-tail alphabet into the live queue.  Every
Johnson-adjacent BTK product endpoint has an (A)-alphabet meeting this
one, and its length is (h-2,h), or (h+2).  Therefore

\[
 \boxed{2h+3\le H\quad\Longrightarrow\quad
 \text{there is no (H)-geodesic intact-path endpoint continuation}.}
                                                               \tag{0.2}
\]

This is a reachable-history obstruction; no adversarial padding is used.
The number (N_{\rm iso}) of isolated product paths satisfies

\[
 N_{\rm iso}\ge
 N\left[1-O(m^{-1})-
  \exp\!\left(-{(H-7)^2\over12m}\right)\right],
 \qquad
 N=\binom m{\lfloor m/2\rfloor}^{\!2}.              \tag{0.3}
\]

Hence (N_{\rm iso}=(1-o(1))N), and any route retaining complete paths
has

\[
 N_{\rm iso}
 =\left({2\over\sqrt\pi}+o(1)\right){W\over\sqrt m}
 \gg {W\over H}                                    \tag{0.4}
\]

components or requires that many bulk chronology changes.  Alternating
which half controls the next path, changing the status pairing, or changing
the checkerboard phase does not evade (0.2).

### Polynomial mixed-colour local escape

Assume additionally

\[
                         \omega=o(\log m),qquad
                         H\log m=o(m).               \tag{0.5}
\]

Fix constants (0<c<C<\infty).  There is a deterministic catalogue of

\[
                         J=m^4                       \tag{0.6}
\]

colours.  Each colour consists of independent coordinate conjugates of a
fixed SCD on (A) and (B), together with a cross-pairing
\(\phi:A\to B\).  For **every** endpoint state of radius

\[
                         c\sqrt m\le h\le C\sqrt m  \tag{0.7}
\]

and every physically typed live queue of length at most (H), at least

\[
                         m^{3-o(1)}                  \tag{0.8}

\]

catalogue colours contain a queue-legal status edge leading to a
double-boundary endpoint whose entire next product path avoids the live
queue.  This holds for either prescribed radius change (h\mapsto h+2) or
(h\mapsto h-2), and at either endpoint orientation.  Consequently the
controller may alternate the two signs and keep the generated radii in a
fixed Gaussian band.  Thus the catalogue supplies polynomially many
locally legal coloured continuations at every reachable bulk state.

The mixed-colour theorem is not an owner-disjoint factor.  Different
colours partition the same middle owners in different ways, and choosing a
colour separately at every state can reuse owners.  A global coloured
endpoint Hall/cycle theorem remains necessary.  What is proved is that the
record-tail dead end is a fixed-colour phenomenon, not an information or
local alphabet-capacity obstruction.

## 1. Coherent BTK record-tail dead ends

Use the standard BTK SCD on each half.  Let (P) be a product diagonal of
length (h\ge5), oriented from its low endpoint to its high endpoint (X).
Write

\[
                         I_A(X)                     \tag{1.1}
\]

for the set of (A)-coordinates inserted during this traversal.  It has
size (h).  The exact record-tail theorem in the second audited
countercut says that, for every Johnson-adjacent product-path endpoint
(Y),

\[
 h(Y)\in\{h-2,h,h+2\},qquad
 |I_A(X)\cap I_A(Y)|\ge h-4>0.                     \tag{1.2}
\]

### Theorem 1.1 (coherent natural-history dead end)

If (2h+3\le H), no Johnson seam from (X) to another product endpoint
can be followed by that endpoint's intact BTK product diagonal while
remaining (H)-geodesic.

#### Proof

All labels in (I_A(X)) were inserted during the last (h) transitions.
An adjacent endpoint (Y) is also a high endpoint: its (A)-rank differs
from that of (X) by at most one, and (h\ge5) keeps it strictly above
the centre.  Starting at (Y), its product path must be traversed toward
the low endpoint and therefore deletes every label in (I_A(Y)).

Choose (z\in I_A(X)\cap I_A(Y)), which exists by (1.2).  The insertion
of (z) on (P), the seam, and its deletion on the next path all lie in
a segment of length at most

\[
                         h+1+h(Y)\le2h+3\le H.       \tag{1.3}
\]

Thus one physical coordinate changes twice in an (H)-window.  Its
intersection and union have the wrong ranks, so the window is not a
literal geodesic flag. \(\square\)

Reverse-complement gives the low-endpoint form.  Notice that (1.2) uses
the complete (A)-segment of the adjacent path, whether that path is
controlled by its (A)-chain or its (B)-chain.  Hence alternating
control does not help.

### Corollary 1.2 (delay cost)

If a bridge of (g) transitions is inserted between the two intact paths,
then the same repetition remains inside one protected window whenever

\[
                         h+1+g+h(Y)\le H.            \tag{1.4}
\]

Therefore a nonproductive delay must have

\[
                         g>H-2h-3.                  \tag{1.5}
\]

For (h\le H/4), this is \(\Omega(H)\) per splice.  Such bridges can only
escape the toll if their middle owners are productively re-factorized, in
which case the construction is no longer intact endpoint stitching.

## 2. Exact census of coherently isolated paths

For an admissible length (h\equiv m\pmod2), put

\[
 P_h=\binom m{(m-h)/2}^{\!2}
       -\binom m{(m-h)/2-1}^{\!2}.                 \tag{2.1}
\]

This is the exact number of product paths of length (h), and

\[
                         \sum_hP_h=N.               \tag{2.2}
\]

The paths covered by Theorem 1.1 are

\[
 N_{\rm iso}
 =\sum_{\substack{h\equiv m\ (2)\\5\le h\le(H-3)/2}}P_h.    \tag{2.3}
\]

The finitely many shells (h<5) contain (O(N/m)) paths.  The upper
tail telescopes:

\[
 \sum_{h\ge h_0}P_h
 =\binom m{\lfloor(m-h_0)/2\rfloor}^{\!2}           \tag{2.4}
\]

up to the harmless parity rounding.  The elementary central binomial
ratio bound gives, uniformly for (h_0=o(m)),

\[
 {1\over N}\sum_{h\ge h_0}P_h
 \le\exp\!\left(-{(h_0-2)^2\over 3m}\right).       \tag{2.5}
\]

Taking (h_0=(H-3)/2) and weakening the constant proves (0.3).
Stirling's formula gives

\[
 N=\left({2\over\sqrt\pi}+o(1)\right){W\over\sqrt m},        \tag{2.6}
\]

which proves (0.4).

There is an owner-mass version as well.  Summation by parts gives

\[
 \sum_{h\ge h_0}(h+1)P_h
 =(h_0+1)\binom m{(m-h_0)/2}^{\!2}
   +2\sum_{r<(m-h_0)/2}\binom mr^2,                \tag{2.7}
\]

again with parity rounding.  Successive-ratio bounds imply

\[
 {1\over W}\sum_{h\ge h_0}(h+1)P_h
 \le C_0\left({h_0\over\sqrt m}+{\sqrt m\over h_0}\right)
       e^{-h_0^2/(3m)}.                             \tag{2.8}
\]

Thus the isolated shells also contain (W-o(W)) middle owners when
(H/\sqrt m\to\infty).

## 3. A general active-alphabet avalanche criterion

The coherent obstruction is not tied to record words once active-set
stability is stated explicitly.  For one half of an arbitrary SCD, let

\[
                         A_h(X)                     \tag{3.1}
\]

be the (h)-coordinate carrier used by the complete product diagonal
ending at (X).

### Theorem 3.1 (carrier-edit no-go)

Suppose every adjacent same-side product endpoint (Y) satisfies

\[
 h(Y)\in\{h(X)-2,h(X),h(X)+2\},qquad
 |A_h(X)\triangle A_{h(Y)}(Y)|\le D_m.             \tag{3.2}
\]

Then every intact path with

\[
                         D_m<h,qquad2h+3\le H       \tag{3.3}
\]

is isolated in the (H)-legal endpoint-continuation graph.

#### Proof

The first inequality in (3.3), together with (|A_h(X)|=h), forces
(A_h(X)\cap A_{h(Y)}(Y)\ne\varnothing).  Complete traversal changes a
shared coordinate once on each path, within at most (2h+3) transitions.
The proof of Theorem 1.1 applies verbatim. \(\square\)

If (D_m=o(\sqrt m)), the same binomial census gives

\[
 N_{\rm iso}\ge N\left[
  1-O(D_m^2/m)-
  \exp\!\left(-{(H-O(1))^2\over12m}\right)
                         \right].                  \tag{3.4}
\]

Thus a successful *single* SCD must exhibit an active-alphabet avalanche:
on a positive density of Gaussian-length endpoints, some one-Johnson-edge
(two-coordinate) endpoint move must replace \(\Theta(\sqrt m)\) carrier labels.

One checkable conditional class is the following.  In a balanced binary
SCD recursion of depth (L=\lceil\log_2m\rceil), assume an endpoint edit
creates at most (b) new carrier-membership discrepancies at each ancestor
interface, after inherited child discrepancies are passed upward.  Charge
each final discrepancy to the first interface where it appears.  Then

\[
 |A_h(X)\triangle A_{h'}(Y)|
 \le4\bigl(1+b\lceil\log_2m\rceil\bigr).           \tag{3.5}
\]

Consequently every recursion satisfying this explicit boundary-local
axiom is closed by Theorem 3.1.  Equation (3.5) is conditional on verifying
the axiom for the actual recursive rule; it must not be inferred merely
from the word “recursive.”

## 4. Uniform active alphabets under a random SCD conjugate

The avalanche criterion suggests changing the entire SCD colour at a
seam.  The following symmetry fact is the key.

Fix any SCD \({\cal D}\) of (2^{[m]}), and choose a uniformly random
coordinate permutation σ.  Use the conjugate SCD
σ\({\cal D}\).

### Lemma 4.1 (conditional uniform carrier)

Fix (k>m/2), put (r=m-k) and (h=k-r), and fix a (k)-set (S).
Then

\[
 \Pr(S\text{ is a chain top of minimum }r)
 ={\binom mr-\binom m{r-1}\over\binom mk}
 ={h+1\over k+1}.                                  \tag{4.1}
\]

Conditional on this event, the chain's (h)-coordinate active alphabet
is uniform on \(\binom Sh\).  Dually, for a fixed (r)-set (T),
conditional on (T) being a chain bottom of minimum (r), its active
alphabet is uniform on \(\binom{[m]\setminus T}h\).

#### Proof

Every SCD has exactly
(n_r=\binom mr-\binom m{r-1}) chains of minimum (r).  Under a random
coordinate conjugate, their tops are a uniform (n_r)-subset of the
rank-(k) layer in the marginal sense, proving the first equality.  The
second is elementary cancellation.

The conditional law is invariant under the full stabilizer of (S).
That stabilizer acts transitively on the (h)-subsets of (S), while the
active alphabet is an equivariant (h)-subset.  Hence its conditional law
is uniform.  The bottom statement is identical. \(\square\)

## 5. Polynomially many mixed-colour queue-safe continuations

A colour γ consists of three independent objects:

* a uniform coordinate conjugate \({\cal D}_{A,\gamma}\) on (A);
* a uniform coordinate conjugate \({\cal D}_{B,\gamma}\) on (B); and
* a uniform bijection \(\phi_\gamma:A\to B\), used as its status pairing.

Consider a high-endpoint state (X) with

\[
 |X\cap A|=k={m+h\over2},\qquad
 |X\cap B|=r={m-h\over2},                           \tag{5.1}
\]

where (0.7) holds.  Track four typed queues.  A (B\to A) seam may not
use any coordinate occurring in the recent (A)- or (B)-half history,
respectively.  Every product or status transition changes exactly one
coordinate in each half, so each half-history contains at most (H)
labels.  Excluding them leaves at least

\[
                         (r-H)^2\ge {m^2\over10}      \tag{5.2}
\]

physical (B\to A) Johnson neighbors for all large (m).

Fix one such neighbor

\[
                         Y=X+u-v,qquad
 u\in A\setminus X,\quad v\in X\cap B.             \tag{5.3}
\]

Put

\[
 r'=r-1,qquad k'=k+1,qquad h'=h+2.                \tag{5.4}
\]

Call (5.3) successful in colour γ if

1. \(\phi_\gamma(u)=v\), so the seam is one literal status-cube axis;
2. (Y\cap A) is a top of minimum (r') in
   \({\cal D}_{A,\gamma}\), and (Y\cap B) is a bottom of minimum
   (r') in \({\cal D}_{B,\gamma}\);
3. the two active alphabets of this double-boundary path avoid all recent
   labels in their respective halves and also avoid (u,v), respectively.

Condition 3 makes the seam followed by the whole high-to-low path a
literal queue-safe geodesic continuation.

Indeed, if the two selected half chains have common minimum (r'), their
rank-(m) product slice is the (h'+1)-vertex path

\[
 \bigl(C_{k'-t}\cup D_{r'+t}:0\le t\le h'\bigr).    \tag{5.4a}
\]

Its changed physical coordinates are exactly the two active carrier sets,
one coordinate in each half at every edge.  Condition 3 makes these
coordinates disjoint from the preceding live history and from the seam,
while a chain changes each of its own carrier coordinates once.  Hence no
coordinate changes twice in any resulting window of at most (H) edges;
every such Johnson subwalk is literal geodesic.

This is the high-endpoint, outward-radius case.  There are three companion
cases.  At a high endpoint an (A\to B) seam gives radius (h-2); at a low
endpoint an (A\to B) seam gives radius (h+2), and a (B\to A) seam gives
radius (h-2).  In each case the two candidate pools have size either (r)
or (k), the new two half-ranks are again complementary, and the required
events are respectively “top of the new minimum” and “bottom of the new
minimum.”  Thus the same proof applies after interchanging top/bottom and
the two halves.

For clarity, the other sign at a high endpoint is completely explicit:

\[
 Y=X-a+b,\quad a\in X\cap A,\quad b\in B\setminus X,\quad
 \phi_\gamma(a)=b,                                 \tag{5.4b}
\]

and

\[
 k_-=k-1,qquad r_-=r+1,qquad h_-=h-2.            \tag{5.4c}
\]

After the recent labels are excluded there are at least \((k-H)^2\)
candidates, and each of the two required boundary events has exact
probability

\[
                         {h-1\over k}.              \tag{5.4d}
\]

The low-endpoint formulas are obtained by swapping top with bottom and
(A) with (B).  These identities, rather than an appeal to average degree,
are what permit a prescribed inward step.

### Lemma 5.1 (one-colour success probability)

Uniformly over every state satisfying (0.7), every typed queue of length
at most (H), either endpoint orientation, and either prescribed sign
(\epsilon\in\{-1,+1\}), a random colour has at least one successful
continuation of new radius (h+2\epsilon) with probability

\[
                         p_m\ge m^{-1-o(1)}.          \tag{5.5}
\]

#### Proof

It suffices to prove the displayed high/outward case.  For a fixed
candidate (5.3), condition 1 has probability (1/m).  By
Lemma 4.1 and independence of the two half colours, condition 2 has
probability

\[
 p_{h'}^2,qquad
 p_{h'}={h'+1\over k'+1}={h+3\over k+2}
            \ge {c\over3\sqrt m}.                  \tag{5.6}
\]

Conditional on condition 2, the two active alphabets are independent
uniform (h')-subsets of sets of size (k').  Each relevant forbidden
queue has at most (H+1) labels.  Therefore condition 3 has probability
at least

\[
 \left({\binom{k'-H-1}{h'}\over\binom{k'}{h'}}\right)^2
 \ge\exp(-K_C\omega)                               \tag{5.7}
\]

for a constant (K_C) depending only on (C).  The last inequality
follows from

\[
 \prod_{j=0}^{h'-1}\left(1-{H+1\over k'-j}\right)
 \ge\exp\!\left(-{2(H+1)h'\over k'-h'}\right),     \tag{5.8}
\]

valid for all large (m).

There are at least (m^2/10) candidates.  If (Z_\gamma) is their
number of successes, (5.6)--(5.7) give

\[
                         \mathbb EZ_\gamma
 \ge c_0e^{-K_C\omega}.                             \tag{5.9}
\]

One perfect matching \(\phi_\gamma\) supplies at most (m) status axes,
so (Z_\gamma\le m).  Hence

\[
 \Pr(Z_\gamma>0)\ge{\mathbb EZ_\gamma\over m}
 \ge c_0m^{-1}e^{-K_C\omega}=m^{-1-o(1)},          \tag{5.10}
\]

where (0.5) is used in the final equality.

For the other three cases replace (h') by (h+2\epsilon).  For all large
(m), its boundary numerator is at least (c\sqrt m/2), its denominator is
at most (m+1), and both candidate pools still have size at least
(m/3).  Equations (5.7)--(5.10) therefore hold with altered constants
depending only on (c,C). \(\square\)

### Theorem 5.2 (uniform polynomial mixed-colour menu)

There is a deterministic catalogue of (J=m^4) colours such that every
state in (0.7), with every ordered typed history of length at most (H),
for each endpoint orientation and each prescribed sign, has successful
continuations in at least (m^{3-o(1)}) catalogue colours.

#### Proof

Sample the (J) colours independently.  For one fixed state, the success
indicators are independent and each has probability at least (p_m) from
Lemma 5.1.  Chernoff gives

\[
 \Pr\{\#\text{ successful colours}<Jp_m/2\}
 \le\exp(-Jp_m/8)=\exp(-m^{3-o(1)}).                \tag{5.11}
\]

There are fewer than (4^m) owners.  Even retaining the order and type of
every queue label, the number of histories is at most

\[
                         (4m)^{2H+2}.                \tag{5.12}
\]

Here a Johnson transition contributes at most two physical labels, and
the harmless factor (4) records half and insertion/deletion type.

By (0.5), the logarithm of the product of these two counts is (O(m)).
The union bound against (5.11) is therefore (o(1)).  Some deterministic
catalogue satisfies the conclusion simultaneously for all states.  It may
also be taken to have distinct colours: among (m^4) independent samples,
the probability that two cross-pairings coincide is at most
(m^8/m!)=o(1).
\(\square\)

The catalogue theorem therefore removes local dead ends along a coherently
generated route.  In particular, starting at a high endpoint of radius
(h_0) in (0.7), choose the outward sign, traverse the radius-(h_0+2) path,
then choose the inward sign at its low endpoint and traverse a
radius-(h_0) path.  Repeating this sign pattern keeps every radius in
(\{h_0,h_0+2\}) while maintaining the (H)-geodesic queue condition.
This is a walk in the coloured state graph, not yet an owner-disjoint
factor.

## 6. Exact boundary

Proved:

* Fixed-colour BTK intact endpoint fusion is coherently dead on
  (1-o(1)) of its path components; its own natural queue realizes the
  record-tail cut.
* Every single-SCD family with (o(\sqrt m)) endpoint carrier edit has the
  same obstruction.  Bounded-interface recursions are conditionally in
  this class via (3.5).
* A polynomial library of independently conjugated SCD colours and status
  pairings supplies polynomially many queue-safe coloured continuations at
  every central reachable state when \(\omega=o(\log m)\).

Not proved:

* one owner-disjoint choice of colours and paths;
* Hall expansion of the coloured continuation graph over arbitrary owner
  subsets;
* a bounded-component cycle factor rather than a walk in the lifted state
  graph;
* simultaneous lower/upper target support after colour changes; or
* a single structurally different SCD with the required
  \(\Omega(\sqrt m)\) active-alphabet avalanche.

Thus the coherent fixed-SCD lane is closed, while a precise mixed-colour
local escape survives.  The next theorem must be a coloured owner-disjoint
Hall/cycle selection; another fixed-colour endpoint-degree estimate cannot
cross the record-tail barrier.
