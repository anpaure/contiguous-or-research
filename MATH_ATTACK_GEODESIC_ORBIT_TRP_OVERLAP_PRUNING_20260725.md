# Geodesic-orbit pruning for short TRP chunks

Date: 2026-07-25

Method: pure mathematics only. No computation, solver, web search, or
fixed-rank matching theorem is used.

## 0. Outcome

Let \(H\) be the calibrated crossing height and \(Q=o(H)\) the truncated
rotor radius. Choose

\[
 \ell=\left\lfloor\sqrt{QH}\right\rfloor,
 \qquad g:=\ell-1.
\tag{0.1}
\]

Then

\[
 Q\ll\ell\ll H,\qquad \ell=o(m).
\tag{0.2}
\]

There are two complementary conclusions.

1. A nonempty fully coordinate-symmetric chunk catalogue cannot have a
   fixed owner-intersection cap. More precisely, if \(C<H\) is fixed and
   the catalogue is invariant under \(S_{2m}\), then it contains two chunks
   on distinct carrier tags sharing at least \(C+1\) owners. Thus canonical
   anchors cannot produce a symmetric \(O(1)\)-intersection code.

2. The stronger cap is unnecessary. Restrict every carrier to the orbit of
   monotone length-\(g\) Johnson geodesics

   \[
   X_t=C+\{a_{t+1},\ldots,a_g\}
          +\{b_1,\ldots,b_t\},
   \qquad 0\le t\le g.
   \tag{0.3}
   \]

   Every such owner chain is realized by a radius-\(Q\) rotor walk, is
   repetition-free, and the family is exactly coordinate-symmetric and
   owner-regular. If \(P\) is one such chunk and

   \[
   \Psi_j(P)
   ={1\over D_L}
     \sum_{F:\operatorname{tag}(F)\ne\operatorname{tag}(P)}
       \binom{|P\cap F|}{j},
   \tag{0.4}
   \]

   then, uniformly for \(2\le j\le\ell\),

   \[
   \boxed{
   \Psi_j(P)
   \le(2+o(1)){\ell\over\binom m{j-1}^{\,2}}.}
   \tag{0.5}
   \]

Consequently, for the weighted overlap series

\[
 \mathcal K_z(P)
 =\sum_{j=2}^{\ell}
   \Psi_j(P)\left({c\over z}\right)^{j-2},
\tag{0.6}
\]

one has, uniformly for \(1/\log m\le z\le1\),

\[
 \boxed{
 \mathcal K_z(P)\le(2+o(1)){\ell\over m^2}.}
\tag{0.7}
\]

Hence

\[
 \log\log m\,
 \sup_{z\ge1/\log m}\sup_P
 \ell\mathcal K_z(P)
 =O\left({\ell^2\log\log m\over m^2}\right)=o(1).
\tag{0.8}
\]

This proves the **initial static** weighted-overlap estimate proposed in
MATH_ATTACK_TRP_SHORT_CHUNK_NIBBLE_AUDIT_20260725.md. It does not prove
that the same normalized estimate holds in every adaptively generated
residual. The pruned tag degree also satisfies

\[
 D_L(\log m)^{-A\ell}\longrightarrow\infty
\tag{0.9}
\]

for every fixed \(A\). Thus scalar entropy is not the obstruction.
However, MATH_ATTACK_TRP_PHASE_CODE_WEIGHTED_NIBBLE_20260725.md shows that
static weighted links do not imply hereditary residual degree/link
control. Accordingly, the previously asserted implication to a matching is
retracted. What remains is only the conditional statement

\[
 [\hbox{hereditary residual propagation}]
 \Longrightarrow
 \begin{cases}
  o(W)&\hbox{owner leave},\\
  o(W/\ell)&\hbox{carrier-copy leave}.
 \end{cases}
\tag{0.10}
\]

The hereditary premise is unproved. The static owner hierarchy is closed;
the dynamic owner near-factor and the simultaneous flag-row gate remain
open. The exact residual-normalization gap and decoration rigidity are
recorded in
MATH_ATTACK_GEODESIC_ORBIT_DYNAMIC_AND_FLAG_AUDIT_20260725.md.

## 1. Why a symmetric constant-overlap code is impossible

Call a global catalogue coordinate-symmetric if applying any
\(\sigma\in S_{2m}\) to every coordinate sends catalogue chunks to
catalogue chunks, while preserving the labelled copy index of each carrier.

### Theorem 1.1 (fixed-cap symmetry obstruction)

Let \(C\) be a fixed nonnegative integer, and suppose \(\ell>C\). Every
nonempty coordinate-symmetric catalogue of radius-\(Q\) chunks contains
two chunks on distinct carrier tags with at least \(C+1\) common owners.

#### Proof

Take a catalogue chunk \(P\) on carrier \(U\), and take any \(C+1\)
consecutive owners

\[
 X_t,X_{t+1},\ldots,X_{t+C}.
\]

When \(C\le Q\), the rotor geodesic lemma gives

\[
 \left|\bigcup_{i=0}^{C}X_{t+i}\right|=m+C.
\tag{1.1}
\]

Write this union as \(A\). The carrier has

\[
 |U-A|=H-C.
\]

There are

\[
 \binom{m-C}{H-C}>1
\tag{1.2}
\]

size-\(M\) carriers containing \(A\). Choose one, \(V\ne U\). Since
\(U-A\) and \(V-A\) have the same size, there is a coordinate permutation
\(\sigma\) which fixes \(A\) pointwise and maps \(U\) to \(V\).

Coordinate symmetry puts \(\sigma P\) in the catalogue on the distinct
carrier \(V\). Since \(\sigma\) fixes every \(X_{t+i}\),

\[
 |P\cap\sigma P|\ge C+1.
\]

This proves the assertion for every fixed \(C\le Q\), hence for every
fixed \(C\) when \(m\) is large. \(\square\)

The theorem does not use degree or entropy. It rules out canonical-anchor
schemes which demand a deterministic \(O(1)\) intersection cap while
retaining full coordinate symmetry.

There is also an entropy warning without symmetry. Suppose a global
catalogue has pairwise owner intersection at most \(C\). Every
\(\ell\)-chunk contains \(\ell-C\) directed consecutive owner segments of
length \(C+1\), and no such segment can occur in two catalogue chunks.
The global Johnson graph has degree \(m^2\), so there are at most

\[
 W(m^2)^C
\tag{1.3}
\]

directed \(C\)-step owner segments. Since the number of carrier-copy tags
is \((1+o(1))W/\ell\), the average tag degree of a fixed-cap catalogue is
at most

\[
 (1+o(1)){\,\ell\over\ell-C}m^{2C}.
\tag{1.4}
\]

For fixed \(C\),

\[
 m^{2C}(\log m)^{-\ell}\longrightarrow0
\tag{1.5}
\]

because \(\ell\to\infty\). Thus even without symmetry, a fixed-cap code
does not retain the residual degree needed by an ordinary
rank-\(\ell\) product nibble down to density \(1/\log m\).

More generally, an intersection cap \(s=o(\ell)\) can retain such product
entropy only if

\[
 2s\log m\ge(1-o(1))\ell\log\log m,
\tag{1.6}
\]

or

\[
 s\ge\left({1\over2}-o(1)\right)
       {\ell\log\log m\over\log m}.
\tag{1.7}
\]

This explains why the weighted hierarchy, rather than a hard cap, is the
right target.

## 2. The monotone geodesic orbit

Fix a carrier \(U\in\binom{[2m]}M\). An oriented geodesic parameter is an
ordered partition

\[
 U=C\ \dot\cup\
   \{a_1,\ldots,a_g\}\ \dot\cup\
   \{b_1,\ldots,b_g\}\ \dot\cup R,
\tag{2.1}
\]

where the \(a\)'s and \(b\)'s are ordered and

\[
 |C|=m-g,\qquad |R|=H-g.
\]

It exposes the owner sequence (0.3). Consecutive owners differ by

\[
 X_{t+1}=X_t-a_{t+1}+b_{t+1},
\tag{2.2}
\]

and for all \(0\le s<t\le g\),

\[
 d_J(X_s,X_t)=t-s.
\tag{2.3}
\]

Thus the sequence is isometric and repetition-free.

The number of oriented parameters is

\[
 D_{\rm or}
 ={M!\over(m-g)!(H-g)!}
 =\binom Mm(m)_g(H)_g.
\tag{2.4}
\]

Reversing the sequence replaces the two ordered lists by

\[
 (a_1,\ldots,a_g;\ b_1,\ldots,b_g)
 \longmapsto
 (b_g,\ldots,b_1;\ a_g,\ldots,a_1)
\]

and gives the same unordered owner support. For \(g\ge2\), the induced
Johnson graph on the support is a path, so these are its only two oriented
presentations. The simple-support tag degree is therefore

\[
 \boxed{
 D_L={1\over2}\binom Mm(m)_g(H)_g.}
\tag{2.5}
\]

This is genuine support entropy, not parallel repetition.

## 3. Every geodesic support is a rotor chunk

### Proposition 3.1

If

\[
 Q\le g\le H-Q,
\tag{3.1}
\]

then every owner sequence (0.3) is exposed by a legitimate radius-\(Q\)
carrier-rotor walk.

#### Proof

At time zero put

\[
 z_Q=a_1,\quad z_{Q-1}=a_2,\quad\ldots,\quad z_1=a_Q.
\tag{3.2}
\]

The lower block is

\[
 L_0=C+\{a_{Q+1},\ldots,a_g\},
\tag{3.3}
\]

which has size \(m-Q\). Choose the \(Q\) upper queue entries from \(R\);
this is possible because \(g\le H-Q\). Put every \(b_i\), together with
the unused part of \(R\), in the tail block. Its size is \(H-Q\).

At transition \(t\), use arrival

\[
 y_t=b_{t+1}.
\]

For \(0\le t<g-Q\), choose

\[
 x_t=a_{t+Q+1}.
\tag{3.4}
\]

The element in (3.4) is still in the lower block. It enters queue position
one and reaches departure position \(Q\) exactly \(Q\) transitions later.
Thus the scheduled departures are

\[
 a_1,a_2,\ldots,a_g.
\]

During the last \(Q\) transitions choose any \(Q\) distinct elements of
\(C\) which have not previously been used as \(x_t\)'s. They remain in the
lower block until chosen, and their scheduled departures occur only after
the chunk ends. Such a choice exists because
\(|C|=m-g\gg Q\).

All arrivals \(b_i\) were initially in the tail, are distinct, and are
used only once. Hence every move is legal, and the owner recurrence is
exactly (2.2). \(\square\)

The choices of upper queue order are hidden decorations of the same owner
support. We work with the simple support catalogue (2.5); after a support
is selected, Proposition 3.1 supplies a literal rotor realization. Thus no
hidden-state multiplicity is used to inflate the matching degree.

## 4. Exact owner degrees

The family of geodesic supports is invariant under \(S_U\). Therefore a
fixed owner \(X\in\binom Um\) occurs in exactly

\[
 d_U(X)={\ell D_L\over\binom Mm}
\tag{4.1}
\]

supports on \(U\).

Introduce \(K=\lfloor M/\ell\rfloor\) labelled copies of every carrier and
use the same support orbit above every copy. A global owner belongs to
\(\binom mH\) carriers, so its degree is

\[
 D_R
 =K\binom mH\,{\ell D_L\over\binom Mm}
 =\rho_\ell D_L,
\tag{4.2}
\]

where

\[
 \rho_\ell={K\ell N_H\over W}
 =1-O((H+\ell)/m)=1-o(1).
\tag{4.3}
\]

Thus the tagged catalogue is exactly regular within each vertex type and
asymptotically regular across the two types.

## 5. Exact endpoint codegrees

Let \(X,Y\in\binom{[2m]}m\) have Johnson distance \(s\le g\). The number
of carriers containing both is

\[
 \kappa_s=\binom{m-s}{H-s},
\qquad
 {\kappa_s\over\kappa_0}
 ={\binom Hs\over\binom ms}
 ={(H)_s\over(m)_s}.
\tag{5.1}
\]

Inside one containing carrier, count oriented geodesics in which \(X,Y\)
occur \(s\) positions apart. There are two orientations and
\(\ell-s\) choices for the first position. The \(s\) exchanges between the
endpoints can be ordered in \((s!)^2\) ways. The other \(g-s\) departing
and arriving coordinates can be ordered in

\[
 (m-s)_{g-s}(H-s)_{g-s}
\]

ways. Hence the oriented count is

\[
 2(\ell-s)(s!)^2
 (m-s)_{g-s}(H-s)_{g-s}.
\tag{5.2}
\]

Quotienting by reversal divides both (5.2) and all one-owner degrees by
two, so relative codegrees are unchanged. Combining (4.1), (5.1), and
(5.2) gives the exact global identity

\[
 \boxed{
 {\deg(X,Y)\over\deg(X)}
 ={2(\ell-s)\over\ell}
   {1\over\binom ms^{\,2}}.}
\tag{5.3}
\]

In particular the maximum relative owner codegree is

\[
 {2+o(1)\over m^2}.
\tag{5.4}
\]

## 6. The full overlap hierarchy

Fix a geodesic chunk

\[
 P=(X_0,\ldots,X_g).
\]

For a set

\[
 \mathcal S=\{X_{i_1},\ldots,X_{i_j}\}\subseteq P,
\qquad i_1<\cdots<i_j,
\]

put

\[
 s=i_j-i_1.
\tag{6.1}
\]

Every geodesic chunk is isometric by (2.3). Therefore any other geodesic
chunk containing \(\mathcal S\) must place \(X_{i_1}\) and \(X_{i_j}\)
exactly \(s\) positions apart, in one of the two orientations. Its
codegree is consequently at most the endpoint codegree (5.3).

The number of \(j\)-subsets of the positions
\(\{0,\ldots,g\}\) having span \(s\) is

\[
 (\ell-s)\binom{s-1}{j-2}.
\tag{6.2}
\]

Since \(D_R=\rho_\ell D_L\le D_L\), summing over the \(j\)-subsets of
\(P\) gives

\[
 \boxed{
 \Psi_j(P)
 \le {2\over\ell}
 \sum_{s=j-1}^{g}
 {(\ell-s)^2\binom{s-1}{j-2}\over\binom ms^{\,2}}.}
\tag{6.3}
\]

This includes all tags; deleting the tag of \(P\) only decreases the sum.

### Proposition 6.1

If \(g=o(H)\), then uniformly for \(2\le j\le\ell\),

\[
 \Psi_j(P)
 \le(2+o(1)){\ell\over\binom m{j-1}^{\,2}}.
\tag{6.4}
\]

#### Proof

The first summand of (6.3), at \(s=j-1\), is at most

\[
 {2\ell\over\binom m{j-1}^{\,2}}.
\tag{6.5}
\]

The ratio of the \(s+1\) summand to the \(s\) summand is at most

\[
 {s\over s-j+2}
 \left({s+1\over m-s}\right)^2
 \le O(\ell^3/m^2).
\tag{6.6}
\]

For the choice (0.1),

\[
 {\ell^3\over m^2}
 =m^{-1/2+o(1)}=o(1).
\tag{6.7}
\]

Thus the sum is its first term times \(1+o(1)\), uniformly in \(j\).
Equations (6.5)--(6.7) prove (6.4). \(\square\)

This is the required exponential overlap hierarchy. It permits rare pairs
with \(\ell-O(1)\) common owners, but their normalized frequency carries
the factorial denominator \(\binom m{j-1}^{-2}\).

## 7. The weighted \(\mathcal K_z\) gate

Put

\[
 \eta={1\over\log m}.
\]

From (6.4), uniformly for \(\eta\le z\le1\),

\[
 \mathcal K_z(P)
 \le(2+o(1))\ell
 \sum_{t=1}^{g}
 { (c/z)^{t-1}\over\binom mt^{\,2}}.
\tag{7.1}
\]

The ratio of consecutive summands is

\[
 {c\over z}
 \left({t+1\over m-t}\right)^2
 \le
 c\log m\,{\ell^2\over(m-\ell)^2}
 =o(1),
\tag{7.2}
\]

because \(\ell\ll H\) and \(H^2=(1+o(1))m\log m\). Therefore the
\(t=1\) term dominates and

\[
 \boxed{
 \sup_{\eta\le z\le1}\sup_P\mathcal K_z(P)
 \le(2+o(1)){\ell\over m^2}.}
\tag{7.3}
\]

Multiplying by \(r=\ell+1\) and \(\log(1/\eta)=\log\log m\) gives

\[
 \log(1/\eta)\,r\sup\mathcal K_z
 =O\left({\ell^2\log\log m\over m^2}\right)
 =o(1).
\tag{7.4}
\]

This was the weighted series used in the earlier short-chunk draft. The
exact conflict-neighbourhood audit uses the stronger static series

\[
 \widehat{\mathcal K}_z(P)
 =\sum_{j=2}^{\ell}\Psi_j(P)(c/z)^j.
\tag{7.5}
\]

The same calculation still gives a favorable **initial** bound:

\[
 \sup_{\eta\le z\le1}\sup_P\widehat{\mathcal K}_z(P)
 =O\left({\ell(\log m)^2\over m^2}\right),
\tag{7.6}
\]

because its summands again have ratio \(o(1)\) and the \(j=2\) term
dominates. Hence

\[
 r\log\log m\sup\widehat{\mathcal K}_z
 =O\left({\ell^2(\log m)^2\log\log m\over m^2}\right)
 =o(1).
\tag{7.7}
\]

Equations (7.4) and (7.7) are static. Neither proves that the corresponding
normalized series remains small after adaptive bites.

## 8. Entropy after pruning

The simple-support tag degree is (2.5). Since \(g=o(H)\),

\[
 \begin{aligned}
 \log D_L
 &=\log\binom Mm+\log(m)_g+\log(H)_g+O(1)\\
 &=\log\binom Mm
   +g(\log m+\log H)+o(g\log m).
 \end{aligned}
\tag{8.1}
\]

In particular,

\[
 \log D_L\ge(3/2-o(1))g\log m.
\tag{8.2}
\]

For every fixed \(A\),

\[
 \begin{aligned}
 \log\left(D_L\eta^{A\ell}\right)
 &\ge(3/2-o(1))g\log m
      -A\ell\log\log m\\
 &\longrightarrow+\infty.
 \end{aligned}
\tag{8.3}
\]

Thus, at the scalar-count level, pruning to one geodesic orbit leaves
exponentially more than the nominal degree needed throughout the owner
nibble. This is not a residual concentration statement.

## 9. Conditional owner leave and literal ledger

The conditional bite-summation lemma gives the owner-leave estimate

\[
 {L_O\over W}
 =O\left(
 \eta+
 h\log(1/\eta)+
 \log(1/\eta)\,r\sup\widehat{\mathcal K}_z
 \right),
\tag{9.1}
\]

and

\[
 L_C\le L_O/\ell
\tag{9.2}
\]

for the unused carrier-copy tags **if**, in every current residual, degrees
remain flat and the residual analogue of the corrected
conflict-neighbourhood series (7.5)--(7.7) holds. Choose

\[
 h={1\over(\log\log m)^2}.
\]

Under that hereditary hypothesis, equations (7.7), (9.1), and (9.2) would
give

\[
 L_O=o(W),\qquad L_C=o(W/\ell).
\tag{9.3}
\]

Equation (8.3) verifies only scalar degree availability. It does not prove
the martingale concentration or residual link bounds. Therefore (9.3) is a
conditional target, not a proved near-factor.

Finally,

\[
 {Q\over\ell}W=o(W)
\tag{9.4}
\]

is the reset cost, and

\[
 {\ell\over m}W=o(W)
\tag{9.5}
\]

is the omitted-remainder cost. Conditional on (9.3), appending the
\(o(W)\) owner holes preserves the \(W+o(W)\) owner ledger.

## 10. What remains for coefficient one

The construction closes the **static** higher-owner-overlap census:

* a fixed overlap cap is impossible under coordinate symmetry;
* the geodesic orbit is a coordinate-symmetric, repetition-free,
  rotor-realizable pruning;
* its owner degrees are exactly regular;
* its entire overlap hierarchy is (6.4);
* its initial weighted \(\mathcal K_z\) series has the required scale; and
* its support entropy remains exponential.

The first remaining issue is hereditary propagation of degrees and
conflict-neighbourhood links through the wasteful nibble. Only after that
is proved does one obtain the owner near-factor (9.3).

The second issue is the flag decoration. The owner
support (0.3) has several hidden radius-\(Q\) rotor realizations. Selecting
one realization per matched support must preserve the calibrated lower and
upper flag rows with \(o(W)\) aggregate holes. The vertical
owner--facet codegree and the upper-star obstruction from the previous
audits are not changed by the present owner pruning.
