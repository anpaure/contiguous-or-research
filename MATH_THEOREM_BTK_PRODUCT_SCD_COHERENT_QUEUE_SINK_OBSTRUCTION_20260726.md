# The BTK product-SCD record cut is a coherent queue state and isolates a Gaussian band

Date: 2026-07-26

Method: pure mathematics only.  No computation, search, solver, or web
input is used.

## 0. Outcome

Let (A\mathbin{\dot\cup}B) have two halves of size (m), put

\[
                         W=\binom{2m}{m},            \tag{0.1}
\]

and form the rank-(m) product paths from the standard BTK symmetric-chain
decomposition on each half.  The endpoint record-tail theorem in
`MATH_OBSTRUCTION_BTK_PRODUCT_SCD_ENDPOINT_RECORD_TAIL_CUT_20260726.md`
is not merely an adversarial static cut.  Its forbidden set is generated
automatically by every legal traversal of the path itself.

More precisely, let (P) have length (h), traverse it from its low
endpoint to its high endpoint, and suppose

\[
                         5\le h,\qquad 2h+3\le H.    \tag{0.2}
\]

The live lower-safety queue at the high endpoint contains the complete
insertion alphabet (I_A(P)).  If (Q) has a Johnson-adjacent high
endpoint, then

\[
                         |I_A(P)\cap I_A(Q)|\ge h-4>0.            \tag{0.3}
\]

Traversing (Q) away from that high endpoint removes every coordinate in
(I_A(Q)).  A shared coordinate from (0.3) is therefore inserted on (P)
and removed at inclusive separation at most

\[
                         h+1+h(Q)\le2h+3\le H.       \tag{0.4}
\]

This is a literal positive residence, so the proposed concatenation is not
even lower (H)-safe.  The same argument at low endpoints uses the
(B)-alphabet.  Consequently every BTK product path satisfying (0.2) is
an isolated atomic component in every endpoint-splicing construction that
preserves the product paths as blocks.

For fixed (0<c_1<c_2<\infty), all lengths

\[
                  c_1\sqrt m\le h\le c_2\sqrt m      \tag{0.5}
\]

satisfy (0.2) when (H=\sqrt m\log\log m) and (m) is sufficiently
large.  The number of paths in this band is

\[
 \boxed{
 \left(\frac{2}{\sqrt\pi}
       (e^{-c_1^2}-e^{-c_2^2})+o(1)\right)
       \frac W{\sqrt m}.}                           \tag{0.6}
\]

Thus the coherent BTK endpoint route has

\[
                         \Omega(W/\sqrt m)           \tag{0.7}
\]

components.  This is not (o(W/H)) at the requested scale; it exceeds
(W/H=W/(\sqrt m\log\log m)) by a factor of order (\log\log m).

At a double-boundary endpoint there is an even smaller coherent
certificate.  The last three edges of (P) supply three (A)-labels and
three (B)-labels.  Those six labels are in the live two-sided queue, and
the three labels on the relevant side already meet the active alphabet of
every adjacent endpoint.  Hence the earlier ``(3+3)'' cut is also a
literal suffix of a legal path history, not an arbitrary forbidden state.

The result is a sharp no-go for the concrete BTK product-SCD endpoint
splicing route.  It does not exclude splitting the atomic paths internally
or replacing BTK by an SCD whose active alphabet changes macroscopically
under one Johnson move.

## 1. Exact queue decomposition at a block endpoint

Write a directed Johnson transition as

\[
                         X_{t+1}=X_t-a_t+b_t.        \tag{1.1}
\]

For lower (H)-safety, the state just before edge (t) is the ordered
queue of insertion labels on the preceding (H-1) edges.  Edge (1.1) is
legal exactly when (a_t) is absent from that queue.  For simultaneous
lower and upper safety, store both labels of each of the preceding
(H-1) edges; the (2H) labels in every (H)-edge window must be pairwise
distinct.

The following bookkeeping statement makes the reachability issue exact.

### Lemma 1.1 (block suffix decomposition)

Let a legal history arrive at an oriented block

\[
 P=(X_0,X_1,\ldots,X_h),\qquad
 X_j=X_{j-1}-a_j+b_j,                               \tag{1.2}
\]

and suppose (h\le H-1).  At (X_h), the lower queue is

\[
 Q^-_{\rm out}
 =\operatorname{suffix}_{H-1-h}(Q^-_{\rm in})
    \mathbin\Vert(b_1,\ldots,b_h),                  \tag{1.3}
\]

with the evident truncation if the incoming queue is shorter.  The
two-sided queue is

\[
 Q^{\pm}_{\rm out}
 =\operatorname{suffix}_{H-1-h}(Q^{\pm}_{\rm in})
    \mathbin\Vert((a_1,b_1),\ldots,(a_h,b_h)).       \tag{1.4}
\]

All labels displayed in the retained two-sided queue are distinct.
Consequently its support is the disjoint union of the retained incoming
history and the physical alphabet of (P).

#### Proof

Equations (1.3)--(1.4) are exactly the update rule ``append the new edge
and delete the edge of age (H)'', iterated (h) times.  The lower
legality test prevents a retained insertion label from being removed.  In
the two-sided case, repeating either label in the displayed (H-1) edges
would give a repeated physical coordinate in an (H)-edge window, contrary
to two-sided safety.  \(\square\)

Every longer concatenation has the same canonical decomposition: read
backward from the live endpoint until (H-1) edges have been collected.
The queue is made of a terminal part of the most recent product path, the
preceding seam, then terminal or complete parts of earlier product paths
and seams.  Under two-sided safety these pieces have disjoint physical
supports.  There is therefore no freedom to choose a queue independently
of the route which generated it.

For a product path traversed low to high, its edge word has the form

\[
                  d_1\to c_1,\ldots,d_h\to c_h,     \tag{1.5}
\]

where

\[
 \{c_1,\ldots,c_h\}=I_A(P),\qquad
 \{d_1,\ldots,d_h\}=I_B(P).                        \tag{1.6}
\]

All (2h) labels are distinct because the two halves are disjoint and a
saturated chain uses each increment once.  Lemma 1.1 gives

\[
 I_A(P)\subseteq\operatorname{supp}Q^-_{\rm out},qquad
 I_A(P)\mathbin{\dot\cup}I_B(P)
       \subseteq\operatorname{supp}Q^{\pm}_{\rm out}.            \tag{1.7}
\]

If (P) starts a component with empty memory, the inclusions in (1.7) are
equalities.  Thus both the one-alphabet and two-alphabet forbidden sets are
coherently reachable.  In fact they are forced terminal pieces of every
incoming history.

## 2. The endpoint overlap used by the queue

For completeness, recall the exact BTK fact.  Encode (X\cap A) by a
binary word (w), put

\[
 D_w(t)=\sum_{i\le t}(2w_i-1),                       \tag{2.1}
\]

and list the strict ascending record times of (D_w) as

\[
                         \tau_1<\cdots<\tau_M.       \tag{2.2}
\]

If (X) is a high endpoint whose product path has length

\[
                         h=2|X\cap A|-m,             \tag{2.3}
\]

then

\[
                         I_A(X)=\{\tau_{M-h+1},\ldots,\tau_M\}.  \tag{2.4}
\]

An exchange of one zero and one one changes the record-time set in at
most four places: the two height walks differ by (2) on one interval,
which can add at most two record levels inside the interval and suppress at
most two after it.  A one-bit change shifts one suffix by (2) and changes
at most two record times.

If (Y) is a Johnson neighbor which is also a product-path endpoint, its
(A)-rank differs from that of (X) by at most one.  For (h\ge5), both
are high endpoints and

\[
 h(Y)\in\{h-2,h,h+2\},qquad
 |I_A(X)\cap I_A(Y)|\ge h-4.                       \tag{2.5}
\]

At low endpoints, interchange (A) and (B): the (B)-part has rank
above (m/2), and

\[
 |I_B(X)\cap I_B(Y)|\ge h-4.                       \tag{2.6}
\]

These are deterministic statements for every Johnson neighbor, not
average-degree estimates.

## 3. Coherent sink theorem

### Theorem 3.1 (no legal high-to-high continuation)

Let (P) be a BTK product path of length (h\ge5), traversed from low to
high, and assume (2h+3\le H).  No Johnson seam from its high endpoint to
the high endpoint of another product path can be followed by a traversal
of that path while preserving lower (H)-safety.

#### Proof

Let (Q) be a path whose high endpoint (Y) is Johnson-adjacent to the
high endpoint (X) of (P).  By (2.5), choose

\[
                         z\in I_A(P)\cap I_A(Q).     \tag{3.1}
\]

The coordinate (z) is present in both (X) and (Y), so the Johnson
seam (X\to Y) does not toggle it.  It was inserted on one of the (h)
edges of (P).  Traversing (Q) away from its high endpoint reverses its
product orientation and therefore removes (z) on one of its (h(Q))
edges.

If the insertion is the first edge of (P) and the removal is the last
edge of the reversed (Q), their inclusive separation is

\[
                         h+1+h(Q).                  \tag{3.2}
\]

This is the largest possible separation.  Since adjacent high endpoint
ranks differ by at most one, (h(Q)\le h+2).  Hence (3.2) is at most
(2h+3\le H).  The insertion of (z) followed by its removal is a
positive residence within one protected window, contradicting lower
(H)-safety.  \(\square\)

### Corollary 3.2 (both endpoint orientations are sinks)

Under the hypotheses of Theorem 3.1, no low-to-low continuation is lower
(H)-safe either.  Consequently (P) cannot share an atomic endpoint-splice
component with any other product path.

#### Proof

Traverse (P) from high to low.  It inserts the alphabet (I_B(P)).
A neighboring path traversed away from its low endpoint removes its
(I_B)-alphabet.  Equation (2.6) and the same separation calculation give
a positive residence.

Any component containing two or more intact product paths has an internal
seam preceded by a complete traversal of one atomic path.  If an incident
high-to-high seam is oriented from (Q) into (P), use the same shared
coordinate (z): it is inserted on (Q) and removed on the reverse traversal
of (P), at the same bound (h(Q)+1+h\le2h+3).  Thus Theorem 3.1 blocks both
orientations of every high-end seam incident with (P), even when
(h(Q)=h-2<5).  The identical observation applies at low endpoints.  Hence
no internal seam incident with (P) is legal and no multi-block component
can contain it.  \(\square\)

This proves more than failure of a static robust-degree condition.  The
actual state produced by the only relevant incoming traversal is a sink in
the lower-safety automaton.

## 4. Exact Gaussian-band component count

An SCD of (2^{[m]}) has (\binom mr-\binom m{r-1}) chains of minimum
rank (r).  A product path has length (h=m-2r) precisely when the maximum
of the two half-chain minima is (r).  Therefore

\[
 P_h=\binom mr^2-\binom m{r-1}^2,\qquad r=(m-h)/2.  \tag{4.1}
\]

Uniformly for (h=x\sqrt m+O(1)), with (x) in a fixed compact subset of
((0,\infty)),

\[
 \frac{P_h}{W}
 =\left(\frac{8x e^{-x^2}}{\sqrt\pi}+o(1)\right)\frac1m.        \tag{4.2}
\]

Only lengths with the parity of (m) occur, so the mesh in (x) is
(2/\sqrt m).  Summing (4.2) over (0.5) gives

\[
\begin{aligned}
 \frac1W\sum_{\substack{c_1\sqrt m\le h\le c_2\sqrt m\\
                         h\equiv m\pmod2}}P_h
 &=\frac4{\sqrt{\pi m}}
     \int_{c_1}^{c_2}x e^{-x^2}\,dx+o(m^{-1/2})\\
 &=\left(\frac2{\sqrt\pi}
          (e^{-c_1^2}-e^{-c_2^2})+o(1)\right)m^{-1/2}.          \tag{4.3}
\end{aligned}
\]

This is (0.6).  If (H=\sqrt m\log\log m), then for fixed (c_2),

\[
                         2c_2\sqrt m+3\le H           \tag{4.4}
\]

for all sufficiently large (m).  Corollary 3.2 makes every path counted
in (4.3) an isolated atomic component, proving (0.7).

## 5. The coherent (3+3) certificate at a double boundary

Take half chains with the same minimum (a=b=r).  At the high endpoint,
the (A)-word is the top of its BTK chain.  Its final walk height (h) is
also its maximum, so

\[
                         I_A(P)=\mathcal R(X\cap A),qquad
                         |I_A(P)|=h.                 \tag{5.1}
\]

### Lemma 5.1 (two-loss boundary stability)

For every Johnson-adjacent high endpoint (Y),

\[
                         |I_A(P)\setminus I_A(Y)|\le2.           \tag{5.2}
\]

#### Proof

For an internal (B)-move the (A)-word is unchanged.  For a cross move
which adds an (A)-coordinate, its height walk is raised by two on a
suffix.  Every old record remains, the new final height is (h+2), and
the new maximum is exactly (h+2); hence (I_A(P)\subseteq I_A(Y)).

For a cross move which removes an (A)-coordinate, the walk is lowered by
two on a suffix.  Its new record set is a subset of the old one, and the
new active set has size (h-2).  Thus it omits exactly two old active
coordinates.

It remains to consider an internal (A)-exchange.  Let (R) and (R')
be the old and new record sets.  The interval perturbation proof gives

\[
                         |R'\setminus R|\le2.         \tag{5.3}
\]

Write (p=|R\setminus R'|), (q=|R'\setminus R|).  Since
(|R|=h), while the new walk still has final height (h), its maximum
and hence (|R'|) is at least (h).  Therefore (q\ge p).  The new
active set is the last (h) members of (R'), obtained by discarding
exactly (q-p) record times.  Even if all discarded times lie in
(R\cap R'), the number of old records absent from the new active set is
at most

\[
                         p+(q-p)=q\le2.              \tag{5.4}
\]

This proves (5.2).  \(\square\)

Let (S_A) be the three (A)-insertion labels and (S_B) the three
(B)-removal labels on the last three edges of the forward traversal.
Lemma 5.1 gives

\[
                         S_A\cap I_A(Y)\ne\varnothing             \tag{5.5}
\]

for every adjacent high endpoint (Y).  At the low endpoint the identical
argument on the (B)-word says that every three-set in (I_B(P)), including
this (S_B), meets every adjacent low-end active alphabet.

The six labels

\[
                         Z_6=S_A\mathbin{\dot\cup}S_B             \tag{5.6}
\]

are exactly the labels used by the last three edges of (P).  Hence, for
(H\ge4), they form a literal terminal suffix of the coherent two-sided
queue.  In the lower-only queue at the high endpoint, (S_A) itself is a
literal terminal insertion suffix.  This verifies the reachability of the
(3+3) certificate with no prescribed or artificial overlay.

If the path is traversed in reverse and the certificate is required as a
terminal suffix at the low endpoint, take instead the labels on the first
three forward edges, which are the last three reverse edges.  Thus each
orientation has its own literal (3+3) terminal suffix.

## 6. Proved boundary

The following statements are now exact.

1. The full BTK forbidden alphabet is forced into the live queue by a
   traversal of its own product path.
2. For (2h+3\le H), every endpoint overlap survives long enough to make
   the next product-path traversal residence-unsafe.
3. A fixed Gaussian band contributes (\Theta(W/\sqrt m)) isolated
   product paths.
4. At a double boundary, a coherently generated three-label suffix on the
   relevant side already certifies the obstruction; the complementing
   side gives the advertised (3+3) certificate.

Not proved, and not claimed, is an obstruction to an SCD with
macroscopically unstable endpoint alphabets, to internal cuts which break a
product path before its whole alphabet enters the queue, or to a global
construction which does not preserve the product-SCD paths as atomic
blocks.  Those are the exact remaining escape routes.
