# Balanced growing products: collective owner-frame routing and the exact collision gate

Date: 2026-07-26

Method: pure mathematics only.  No computation, search, solver, or web
input is used.

## 0. Outcome

The balanced product route left open by the paired-SCD audit has an exact
collective moving-frame lift.  It does not require an independent collar at
each cross-box seam.

Let

\[
                 \Omega=[2m],\qquad |X_t|=m,
\]

and let

\[
                 X_{t+1}=X_t-a_t+b_t                         \tag{0.1}
\]

be a directed Johnson path or cycle which is simultaneously lower and upper
safe through depth \(H<m\).  At the root \(X_t\), take the balanced product
frame

\[
                 A_t=X_t^c,\qquad B_t=X_t.                    \tag{0.2}
\]

Then every rooted window through depth \(H\) is literally the central
segment of one boundary-peeling product chain in

\[
                         B_{A_t}\times B_{B_t}\cong B_m\times B_m. \tag{0.3}
\]

Its lower and upper members are exactly

\[
 \bigcap_{i=0}^qX_{t+i},\qquad \bigcup_{i=0}^qX_{t+i}.          \tag{0.4}
\]

The frames move by one exchange,

\[
 A_{t+1}=A_t-b_t+a_t,
 \qquad B_{t+1}=B_t-a_t+b_t,                                  \tag{0.5}
\]

and return with zero holonomy on a cycle.  Thus a long component supplies
one collective nested-flag routing; its internal product-frame changes cost
no resets.  The only component collar is the usual \(2H\) outer cyclic
collar.

The construction is not confined to (0.2).  At one root there are exactly

\[
                         \binom{2m-2H}{m-H}                    \tag{0.6}
\]

balanced frames which literalize the whole signed \(H\)-window.  Consecutive
compatible frames can be chosen to differ by at most one coordinate swap.
Hence no statewise coordinate projection is forced when \(H=o(m)\).

This closes the **local and chronological** part of the balanced-product
escape.  It does not by itself produce a common SCD.  Define the lower and
upper window multiplicities at depth \(q\) by

\[
 \mu_q^-(T)=\#\{t:\rho_t\ge q,
                    \bigcap_{i=0}^qX_{t+i}=T\},
 \qquad
 \mu_q^+(U)=\#\{t:\rho_t\ge q,
                    \bigcup_{i=0}^qX_{t+i}=U\}.               \tag{0.7}
\]

When the truncated-radius census is exact, the moving product chains form a
central-band SCD if and only if every multiplicity in (0.7) is at most one.
Equivalently, the exact remaining obstruction is the frame-independent
collision energy

\[
 \boxed{
 \Xi_H=\sum_{q=1}^H
  \left[
   \sum_T(\mu_q^-(T)-1)_+
  +\sum_U(\mu_q^+(U)-1)_+
  \right].}                                                   \tag{0.8}
\]

At each depth, repeat excess equals the number of missing targets.  Thus
\(\Xi_H=o(W)\), together with \(c=o(W/H)\) components and the usual
\(o(W)\) owner leave, is exactly the coefficient-one scale.

For the requested split

\[
                         B_{2s}\times B_{2s}=B_{4s},            \tag{0.9}
\]

put \(m=2s\).  The fixed-product audit's forced escapes
\(\Theta(W/s)\) and cross-box mass \(\Theta(W/\sqrt s)\) create no
separate collar term under (0.2)--(0.5).  They may all occur internally in
long components.  What remains is to arrange those components so that
\(\Xi_H=o(W)\).  Moving frames cannot change \(\Xi_H\), because they
certify the physical windows rather than changing their target sets.

Consequently there is no local statewise obstruction to the projection-free
balanced-product route.  There is, however, an exact global obstruction:
window collisions.  If the old product-SCD flags are frozen rather than
reassigned to (0.4), the earlier de Bruijn Euler and raw Hall cuts also
survive unchanged; a frame choice only decorates those old flag words.

## 1. Signed safety makes a window a fresh exchange word

For a \(q\)-edge window beginning at time \(t\), write

\[
 \mathbf a_{t,q}=(a_t,\ldots,a_{t+q-1}),\qquad
 \mathbf b_{t,q}=(b_t,\ldots,b_{t+q-1}).                       \tag{1.1}
\]

Recall that lower safety excludes an insertion followed by a removal of the
same coordinate in a controlled window, while upper safety excludes a
removal followed by a reinsertion.

### Lemma 1.1 (fresh-label normal form)

The word (0.1) is simultaneously lower and upper safe through depth \(H\)
if and only if, in every window of at most \(H\) edges, all displayed
removal and insertion labels are pairwise distinct.

In that case, for every \(q\le H\),

\[
 \{a_t,\ldots,a_{t+q-1}\}\subseteq X_t,
 \qquad
 \{b_t,\ldots,b_{t+q-1}\}\subseteq X_t^c,                    \tag{1.2}
\]

and

\[
 X_{t+j}
 =X_t-\{a_t,\ldots,a_{t+j-1}\}
       +\{b_t,\ldots,b_{t+j-1}\}.                             \tag{1.3}
\]

#### Proof

If an insertion label is later removed, lower safety fails; if a removal
label is later inserted, upper safety fails.  A repeated removal requires an
intervening reinsertion, and a repeated insertion requires an intervening
removal.  Thus signed safety implies pairwise distinctness of all labels in
the window.

Conversely, every failure of either signed safety is one of these four kinds
of repetition.  This proves the equivalence.

If a future removal label \(a_{t+i}\) were absent from \(X_t\), it would
have to be inserted between times \(t\) and \(t+i\), giving a forbidden
repetition.  The insertion statement is the complement.  Applying the fresh
exchanges successively proves (1.3). \(\square\)

It follows at once that

\[
 \begin{aligned}
 D_q(t)&:=\bigcap_{i=0}^qX_{t+i}
       =X_t-\{a_t,\ldots,a_{t+q-1}\},\\
 E_q(t)&:=\bigcup_{i=0}^qX_{t+i}
       =X_t+\{b_t,\ldots,b_{t+q-1}\}.
 \end{aligned}                                                 \tag{1.4}
\]

These are nested saturated flags of ranks \(m-q\) and \(m+q\).

## 2. Every safe state has a large balanced product atlas

Fix one root \(X=X_t\), and abbreviate

\[
 P=\{b_t,\ldots,b_{t+H-1}\},\qquad
 N=\{a_t,\ldots,a_{t+H-1}\}.                                  \tag{2.1}
\]

The sets \(P,N\) are disjoint and have order \(H\).

Call a balanced frame \(A\mathbin{\dot\cup}B=\Omega\),
\(|A|=|B|=m\), **compatible at \(t\)** when

\[
                         P\subseteq A,\qquad N\subseteq B.      \tag{2.2}
\]

### Theorem 2.1 (balanced product literalization)

Every compatible frame places the complete chain segment

\[
 D_H(t)\subset\cdots\subset D_1(t)\subset X_t
 \subset E_1(t)\subset\cdots\subset E_H(t)                    \tag{2.3}
\]

inside one chain of an ordinary boundary-peeling product SCD of
\(B_A\times B_B\).

The number of compatible frames is exactly (0.6).

#### Proof

Let

\[
                         r=|X_t\cap A|.                          \tag{2.4}
\]

Choose a maximal chain

\[
                         C_0\subset C_1\subset\cdots\subset C_m=A
\]

of \(B_A\) such that

\[
 C_r=X_t\cap A,\qquad
 C_{r+j}=C_r+\{b_t,\ldots,b_{t+j-1}\}\quad(1\le j\le H).      \tag{2.5}
\]

Choose a maximal chain

\[
                         F_0\subset F_1\subset\cdots\subset F_m=B
\]

of \(B_B\) such that

\[
 F_{m-r}=X_t\cap B,\qquad
 F_{m-r-j}=F_{m-r}-\{a_t,\ldots,a_{t+j-1}\}.                   \tag{2.6}
\]

The prescribed portions are nested, so both maximal chains exist: order
the displayed coordinates as required and order all unused coordinates
arbitrarily.  Each chosen maximal chain belongs to an SCD of its Boolean
factor: relabel any standard SCD so that its unique maximal chain has the
chosen coordinate order.

In the standard rectangular boundary peeling of
\(C\times F\), the path indexed by \(r\) is

\[
 (C_r,F_0),\ldots,(C_r,F_{m-r}),
 (C_{r+1},F_{m-r}),\ldots,(C_m,F_{m-r}).                        \tag{2.7}
\]

Equations (2.5)--(2.6) identify (2.3) with the central \(2H+1\)
members of (2.7).  This proves literalization.

After the forced memberships in (2.2), there remain \(2m-2H\) free
coordinates.  Exactly \(m-H\) of them must be put in \(A\), proving
(0.6). \(\square\)

### Corollary 2.2 (no local projection cut)

For \(H<m\), every coordinate outside \(P\cup N\) occurs on each shore
in some compatible frame.  Hence the intersection of all compatible
\(A\)-shores is exactly \(P\), and the intersection of all compatible
\(B\)-shores is exactly \(N\).

In particular, when \(H=o(m)\), no positive-density coordinate projection
is forced by one state and its complete signed collar.

#### Proof

The free-frame system is the complete uniform layer
\(\binom{\Omega\setminus(P\cup N)}{m-H}\).  Since
\(0<m-H<2m-2H\), every free coordinate is present in some choices and
absent in others. \(\square\)

This is different from complete status-cell recoupling.  Here a frame is a
literal certificate for one rooted product chain, not a partition of all
owners into complete cells which must be selected on overlap components.

## 3. Frames can move collectively with the component

Let \({\cal F}_t\) denote the compatible frame family at time \(t\).

### Lemma 3.1 (one-swap frame transport)

For every \(A_t\in{\cal F}_t\), there exists
\(A_{t+1}\in{\cal F}_{t+1}\) with

\[
                         |A_t\triangle A_{t+1}|\le2.             \tag{3.1}
\]

Thus successive balanced frames require at most one shore exchange.

#### Proof

On advancing one time step, the continuing \(H-1\) insertion labels are
already in \(A_t\), and the continuing \(H-1\) removal labels are already
outside it.  Only two new requirements appear:

\[
                         b_{t+H}\in A_{t+1},\qquad
                         a_{t+H}\notin A_{t+1}.                 \tag{3.2}
\]

If both are already satisfied, change nothing.  If both fail, swap
\(a_{t+H}\) out and \(b_{t+H}\) in.  If only the first fails, insert
\(b_{t+H}\) and remove any member not forced into the new frame.  If only
the second fails, remove \(a_{t+H}\) and insert any nonmember not forced
out.  Such a compensating coordinate exists because \(H<m\).  Every case
uses at most one swap. \(\square\)

The canonical choice is stronger.

### Theorem 3.2 (owner-complement frame trajectory)

Put

\[
                         A_t=X_t^c,\qquad B_t=X_t.               \tag{3.3}
\]

Then \((A_t,B_t)\) is compatible at every root, satisfies (0.5), and is
periodic whenever \((X_t)\) is periodic.  The product flags supplied by
Theorem 2.1 are exactly the physical flags (1.4) simultaneously at every
root and every depth \(q\le H\).

#### Proof

Compatibility is (1.2).  Complementing (0.1) gives the first identity in
(0.5), and the second is (0.1).  Periodicity is immediate.  Equations
(1.4) and Theorem 2.1 give the flag assertion. \(\square\)

There is no seam in this construction at which a fresh \(H\)-collar is
installed.  The collar state is transported by the actual exchange word,
and adjacent rooted product certificates overlap in \(H-1\) exchanges.

For a physical \(C_{2h}\)-strip, the canonical frame has a fixed included
core and fixed excluded core, both of size \(m-h\).  It is fully
projection-free precisely for a maximal \(C_{2m}\)-strip, and has only
\(o(m)\) fixed coordinates when \(h=m-o(m)\).  The larger atlas of
Theorem 2.1 can move the otherwise free coordinates as well.

## 4. The de Bruijn obstruction disappears under window reassignment

For a prescribed flag table, write the ordered lower deletion word at owner
\(X\) as

\[
                         d(X)=(d_1(X),\ldots,d_H(X)).             \tag{4.1}
\]

Every coherent cycle must satisfy

\[
 (d_2(X_t),\ldots,d_H(X_t))
 =(d_1(X_{t+1}),\ldots,d_{H-1}(X_{t+1})).                       \tag{4.2}
\]

Consequently the prefix/suffix Euler imbalance of the prescribed words is
a frame-independent lower bound on the discarded owner mass.  Choosing a
different balanced frame does not change (4.1).

Under the collective window assignment, however,

\[
                         d_j(X_t)=a_{t+j-1},                     \tag{4.3}
\]

so (4.2) is an identity.  The upper word satisfies the same identity with
\(b\) in place of \(a\).  Thus the moving-product construction removes the
statewise de Bruijn obstruction exactly, not just asymptotically.

This uses the freedom explicitly left open by the paired-SCD product audit:
retain the half-chain/radius census but globally reassign the middle-rooted
flags.  If the literal flags of the old fixed product SCD must be retained,
(4.1)--(4.2) remain an obstruction and Theorem 3.2 does not repair them.

## 5. Exact global compatibility is window injectivity

Let \({\cal C}\) be an owner-disjoint family of signed \(H\)-safe directed
cycles, and assign to every represented owner a truncated radius

\[
                         0\le\rho_t\le H.                        \tag{5.1}
\]

Assume also that the cycle owners, together with the declared radius-zero
singleton owners, partition the complete middle layer.

Assume the exact SCD census

\[
 \#\{t:\rho_t\ge q\}=N_q:=\binom{2m}{m-q}
                         \qquad(1\le q\le H).                   \tag{5.2}
\]

Owners of radius zero include the Catalan singleton leave.

### Theorem 5.1 (collective balanced-product SCD criterion)

The moving product chains

\[
 D_{\rho_t}(t)\subset\cdots\subset D_1(t)\subset X_t
 \subset E_1(t)\subset\cdots\subset E_{\rho_t}(t)              \tag{5.3}
\]

form a symmetric-chain decomposition of the complete central band through
depth \(H\) if and only if

\[
 \mu_q^-(T)\le1,\qquad \mu_q^+(U)\le1                          \tag{5.4}
\]

for every \(q\le H\) and every target of the corresponding rank.

#### Proof

Every chain in (5.3) is saturated and symmetric by (1.4), and Theorem 2.1
makes it a literal balanced-product chain at its root.  At lower depth
\(q\), the eligible roots number \(N_q\), exactly the number of
rank-\((m-q)\) targets.  Therefore injectivity of the lower window map is
equivalent to bijectivity.  The upper proof is identical.  Different ranks
cannot collide, and owner-disjointness handles the middle rank.  Hence
(5.4) is equivalent to an exact partition at every rank of the band.
\(\square\)

### Corollary 5.2 (exact repeat--hole identity)

Under (5.2), for each sign and depth,

\[
 \sum_T(1-\mu_q^-(T))_+
     =\sum_T(\mu_q^-(T)-1)_+,                                  \tag{5.5}
\]

and likewise on the upper side.  Consequently (0.8) is exactly the total
number of missing signed targets, not merely an upper bound for it.

#### Proof

Both the number of eligible roots and the number of targets are \(N_q\),
so

\[
                         \sum_T(\mu_q^-(T)-1)=0.
\]

Separating positive and negative parts gives (5.5). \(\square\)

Frame changes cannot alter (5.5): the multiplicities depend only on the
physical owner cycles and their radius labels.

## 6. The constant-one ledger

Let \(c=|{\cal C}|\).  With an approximate radius census and an owner leave,
count all omitted or incorrect window flags in \(B_{\rm flag}\).  The
whole-component compiler has the exact central bound

\[
                         W+2Hc+B_{\rm flag}.                     \tag{6.1}
\]

In the exact-census setting of Section 5 one may take

\[
                         B_{\rm flag}=\Xi_H.                     \tag{6.2}
\]

Thus the collective balanced-product route is coefficient-safe under

\[
                         c=o(W/H),\qquad \Xi_H=o(W),             \tag{6.3}
\]

together with the standard \(o(W)\) owner/radius leave.

The key accounting difference from independent collars is that there is no
term \(H P\), where \(P\) is the number of old product paths or cross-box
transitions.  All such transitions are internal to the moving-frame cycles;
only the final component count \(c\) appears.

For \(B_{2s}\times B_{2s}\), write

\[
                         W=\binom{4s}{2s}.                        \tag{6.4}
\]

The paired-SCD audit gives

\[
 \text{forced standard-product escapes}=\Theta(W/s),
 \qquad
 \text{necessary fixed-box crossings}=\Theta(W/\sqrt s).       \tag{6.5}
\]

Both are \(o(W)\).  Under Theorem 3.2 they cause no automatic flag charge.
If the pieces can be routed into physical components of order
\(\Theta(s)\), then

\[
                         c=O(W/s),\qquad 2Hc=O(HW/s)=o(W)        \tag{6.6}
\]

for every \(H=o(s)\).  Near-maximal components are also projection-free
apart from an \(o(s)\) coordinate fringe when their half-length satisfies
\(h=2s-o(s)\).

Equation (6.6) is a ledger theorem, not an existence proof for those
components.  Their exact existence problem is now cleanly separated from
the collar problem.

## 7. Antipodal chunk closure is still physical

The moving-frame theorem removes collars; it does not weaken the physical
cycle equation.  Suppose one component has length \(2h\).  Its exchange
word is physical exactly when, after a cyclic indexing,

\[
 a_0,\ldots,a_{2h-1}\text{ are distinct},
 \qquad b_t=a_{t+h}\quad(t\bmod 2h).                            \tag{7.1}
\]

### Proposition 7.1 (antipodal chunk condition)

Let an interval of a physical component have exchange word

\[
 (a_t\to b_t),\ldots,(a_{t+\ell-1}\to b_{t+\ell-1}).            \tag{7.2}
\]

The interval displaced by \(h\) has word

\[
 (b_t\to a_t),\ldots,
 (b_{t+\ell-1}\to a_{t+\ell-1}).                               \tag{7.3}
\]

For a maximal strip \(h=m\), its owner states additionally satisfy

\[
                         X_{t+m}=X_t^c.                          \tag{7.4}
\]

Hence a chunk decomposition whose cuts are invariant under the antipodal
shift must pair every oriented chunk with the shore-reversed word (7.3);
in the maximal case this is its literal complementary owner path.

#### Proof

Equation (7.3) follows twice from (7.1):
\[
 a_{t+h}=b_t,\qquad
 b_{t+h}=a_{t+2h}=a_t.
\]
For a maximal strip the active support is the whole ground set and
\[
 X_t=\{a_t,\ldots,a_{t+m-1}\},\qquad
 X_{t+m}=\{a_{t+m},\ldots,a_{t+2m-1}\}=X_t^c.
\]
This proves (7.4). \(\square\)

Thus a route assembled from old product-path chunks still needs an
antipodal chunk resolution.  An arbitrary fixed child SCD is not
chainwise complement-stable, so its unchanged product paths do not supply
this closure automatically.  One must cut the complement-asymmetric
internal edges, use paired child resolutions, or globally reassign the
chunks.  The present theorem proves that, once this physical resolution is
made, its many frame changes carry no additional \(H\)-scale toll.

## 8. The precise surviving routing gate

The balanced growing-product line therefore has the following status.

1. **No local statewise obstruction.**  Every signed-safe rooted window has
   exponentially many balanced \(B_m\times B_m\) literalizations.
2. **No frame-reset obstruction.**  Owner-complement frames give a cyclic
   one-swap trajectory and exact nested flags at all roots.
3. **No de Bruijn obstruction after flag reassignment.**  The deletion and
   insertion words shift identically along the component.
4. **No independent-collar tax.**  \(\Theta(W/\sqrt s)\) cross-box
   transitions may be internal, while the collar is only \(2Hc\).
5. **One global obstruction survives.**  The physical cycles and radius
   labels must satisfy \(\Xi_H=o(W)\); equivalently their eligible cyclic
   windows must be an almost-injective design simultaneously at every
   signed depth.

The exact next theorem is therefore an **antipodal chunk-routing and window
design theorem**: partition all but \(o(W)\) balanced-product path pieces
into \(o(W/H)\) signed-safe physical cycles, preferably near-maximal
\(C_{2m}\)-strips, assign the forced radius census, and prove (0.8).

If instead the old product-SCD flags are frozen, the correct next tests are
the frame-independent prefix/suffix Euler imbalance and the raw overlap
Hall deficiency.  Projection-free frame motion alone cannot repair either
one.  The two formulations must not be conflated: the positive theorem in
this note uses global flag reassignment, exactly the freedom left open by
the balanced paired-SCD audit.
