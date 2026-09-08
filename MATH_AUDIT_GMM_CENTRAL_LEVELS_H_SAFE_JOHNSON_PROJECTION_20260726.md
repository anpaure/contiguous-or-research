# Gregor--Mička--Mütze central-level cycles: exact Johnson projection and the chronology obstruction

Date: 2026-07-26

Method: pure mathematics only. No computation, solver, search, or web
input is used.

## 0. Verdict

The Gregor--Mička--Mütze saturating-cycle theorem has one exact
constant-one consequence and no automatic all-depth consequence.

1. A cube cycle using exactly three consecutive levels and alternating
   through rank \(m\) projects canonically to a Johnson cycle on rank
   \(m\).
2. The projected Johnson word is two-sided \(H\)-safe if and only if the
   \(2H\) cube-edge labels in every corresponding window are pairwise
   distinct.
3. Under that condition, every depth-\(q\) intersection and union has the
   exact expected form

   \[
   L_i^q=X_i-\{a_i,\ldots,a_{i+q-1}\},
   \qquad
   U_i^q=X_i+\{b_i,\ldots,b_{i+q-1}\}.
   \tag{0.1}
   \]

   Hence the all-depth rainbow question becomes the injectivity/coverage
   of the maps in (0.1); saturation proves only one of the two
   \(q=1\) maps.
4. A cube cycle genuinely using levels at distance at least two from the
   projected rank has no direct short chronology-preserving \(H\)-safe
   Johnson projection.
   Between two consecutive rank-\(m\) visits, every projected Johnson edge
   must come from either a two-edge excursion or an excursion of at least
   \(2H\) cube edges.
5. The natural GMM Hamilton cycle that concatenates monotone
   Greene--Kleitman chains fails the required label separation.  For

   \[
   H=\left\lfloor\sqrt m\log\log m\right\rfloor
   \tag{0.2}
   \]

   in \(B_{2m}\), a coordinate repeats inside a \(2H\)-edge window at
   \((1-o(1))\binom{2m}{m}\) chain interfaces.

Thus the published central-levels construction supplies an exact
one-sided depth-one rainbow cycle, but neither an \(H\)-safe middle cycle
nor near-rainbow chronology at depths \(2,\ldots,H\).  A positive use
would require a new **label-separated three-level saturating cycle** or a
new synthetic-owner resolution for the long excursions.

## 1. Canonical projection of a three-level cube cycle

Let a simple cube cycle in levels \(m-1,m,m+1\) have cyclic form

\[
 X_0,Z_0,X_1,Z_1,\ldots,X_{\ell-1},Z_{\ell-1},X_0,
\tag{1.1}
\]

where every \(X_i\) has rank \(m\), and every \(Z_i\) has rank
\(m-1\) or \(m+1\).  Simplicity makes the \(X_i\)'s distinct.

There are unique distinct labels \(a_i,b_i\) such that

\[
                         X_{i+1}=X_i-a_i+b_i.
\tag{1.2}
\]

More precisely,

\[
 Z_i=
 \begin{cases}
 X_i-a_i=X_i\cap X_{i+1},&|Z_i|=m-1,\\[1mm]
 X_i+b_i=X_i\cup X_{i+1},&|Z_i|=m+1.
 \end{cases}
\tag{1.3}
\]

Consequently

\[
                         X_0X_1\cdots X_{\ell-1}X_0
\tag{1.4}
\]

is a simple cycle in \(J(n,m)\).  Its directed exchange word is exactly

\[
                         (a_0\to b_0),(a_1\to b_1),\ldots.
\tag{1.5}
\]

This is an equivalence: expanding any Johnson edge through either its
intersection or its union gives one of the two cube two-edge paths in
(1.3).

### Theorem 1.1 (exact chronology transfer)

The Johnson cycle (1.4) is two-sided safe through depth \(H\) if and only
if, for every \(H\) consecutive indices, the \(2H\) labels

\[
 a_i,b_i,a_{i+1},b_{i+1},\ldots,
 a_{i+H-1},b_{i+H-1}
\tag{1.6}
\]

are pairwise distinct.

Equivalently, the cube-edge label word of (1.1) has no repeated physical
coordinate in any \(2H\)-edge window whose endpoints are rank-\(m\)
vertices.

#### Proof

The two cube edges between \(X_i\) and \(X_{i+1}\) toggle precisely
\(a_i,b_i\), in one of the two orders in (1.3).  Thus an \(H\)-edge
window of the projected word contains exactly the labels in (1.6).
The two-sided residence criterion says that a Johnson word is safe through
depth \(H\) exactly when those labels are distinct. \(\square\)

### Theorem 1.2 (exact all-depth targets)

Under the hypotheses of Theorem 1.1, for every \(q\le H\),

\[
 \boxed{
 \bigcap_{j=0}^{q}X_{i+j}
 =X_i-\{a_i,\ldots,a_{i+q-1}\},}
\tag{1.7}
\]

\[
 \boxed{
 \bigcup_{j=0}^{q}X_{i+j}
 =X_i+\{b_i,\ldots,b_{i+q-1}\}.}
\tag{1.8}
\]

In particular their ranks are exactly \(m-q\) and \(m+q\).

#### Proof

Every departure label in the window belongs to \(X_i\), is removed once,
and is not reinserted in the window.  Every arrival label is absent from
\(X_i\), is inserted once, and is not removed.  All other coordinates
retain their initial membership.  Intersecting or uniting the states gives
(1.7)--(1.8). \(\square\)

Define the exact target images

\[
 \mathcal L_q(C)=
 \left\{X_i-\{a_i,\ldots,a_{i+q-1}\}:i\in\mathbb Z_\ell\right\},
\tag{1.9}
\]

\[
 \mathcal U_q(C)=
 \left\{X_i+\{b_i,\ldots,b_{i+q-1}\}:i\in\mathbb Z_\ell\right\}.
\tag{1.10}
\]

The lower and upper hole counts are therefore exactly

\[
 \binom n{m-q}-|\mathcal L_q(C)|,
 \qquad
 \binom n{m+q}-|\mathcal U_q(C)|.
\tag{1.11}
\]

No marginal statement about the vertices of the cube cycle can replace
these two image cardinalities.

## 2. What saturation proves

Simplicity of (1.1) gives:

* the lower colors \(X_i\cap X_{i+1}\) are distinct on those indices for
  which \(Z_i\) has rank \(m-1\);
* the upper colors \(X_i\cup X_{i+1}\) are distinct on those indices for
  which \(Z_i\) has rank \(m+1\).

If a two-level saturating cycle uses ranks \(m-1,m\) and saturates rank
\(m-1\), then

\[
 \mathcal L_1(C)=\binom{[n]}{m-1}
\tag{2.1}
\]

exactly.  Dually, saturation of ranks \(m,m+1\) gives

\[
 \mathcal U_1(C)=\binom{[n]}{m+1}.
\tag{2.2}
\]

These are the exact one-sided rainbow Johnson cycles already extracted
from the GMM theorem.

There are two strict limits.

First, an index routed through a lower intermediate exposes its lower
color but says nothing about whether the opposite upper color collides
with an earlier one; the upper statement is dual.  Second, for \(q\ge2\)
the targets in (1.7)--(1.8) are not vertices \(Z_i\) of the three-level
cycle.  They depend on \(q\) consecutive exchanges.  Hence saturation
contains no assertion about either image in (1.9)--(1.10) for
\(q\ge2\).

The exact missing strengthening is therefore simultaneous:

\[
 \begin{array}{ll}
 \text{chronology:}&
 \text{every \(2H\)-label window is repetition-free},\\[1mm]
 \text{lower images:}&
 |\mathcal L_q(C)|=\binom n{m-q}-o(W)
 \quad(1\le q\le H),\\[1mm]
 \text{upper images:}&
 |\mathcal U_q(C)|=\binom n{m+q}-o(W)
 \quad(1\le q\le H),
 \end{array}
\tag{2.3}
\]

with the appropriate aggregate \(L^1\) form when the target rank is
smaller than the owner cycle.  None of the three lines follows from the
other two.

## 3. Why additional levels do not project locally

Let \(C\) be any simple cube cycle, and retain its rank-\(m\) vertices in
cyclic order.  Consider a segment between consecutive retained vertices

\[
                         X=V_0,V_1,\ldots,V_s=Y
\tag{3.1}
\]

which has no internal rank-\(m\) vertex.  Since \(X,Y\) have the same
rank, \(s\) is even; write \(s=2d\).

Call a projection **chronology-preserving** when the cube excursion is the
literal physical expansion of the projected transition; in particular its
coordinate toggles remain in the all-depth word rather than being erased as
formal null moves.

### Theorem 3.1 (short-excursion dichotomy)

Assume \(2d<2H\).  Then one of the following holds.

1. Some coordinate label repeats on the segment, so the cube chronology
   cannot be the literal expansion of an \(H\)-safe projected Johnson
   word.
2. All \(2d\) labels are distinct, in which case

   \[
                         d_J(X,Y)=d.
\tag{3.2}
\]

   Hence \(X,Y\) are Johnson adjacent if and only if \(d=1\).

Consequently, if retaining the rank-\(m\) visits is to give a
chronology-preserving \(H\)-safe Johnson cycle, every gap is either a
two-edge excursion or has at least \(2H\) cube edges.

#### Proof

If a label repeats among fewer than \(2H\) consecutive cube edges, the
required distinct-label chronology fails.

Otherwise every toggled coordinate occurs exactly once.  Hence

\[
                         |X\triangle Y|=2d.
\]

Equal ranks imply that exactly \(d\) initial members were removed and
\(d\) initial nonmembers were inserted, so \(d_J(X,Y)=d\).  This is one
exactly when the segment has two edges. \(\square\)

Any excursion reaching rank \(m-2\) or \(m+2\) has at least four edges.
Thus a Hamilton or saturating cycle genuinely using five or more
consecutive levels cannot be chronology-preservingly projected to a
Johnson cycle merely by deleting the nonmiddle vertices, unless every
such deep excursion is a \(2H\)-scale expiration collar.

If internal repeated toggles are simply erased, a short deep excursion may
have Johnson-adjacent endpoints.  That is only a formal endpoint
compression: it discards the physical chronology and all band vertices on
the excursion.  The GMM theorem gives no assertion that the resulting net
exchange labels are \(H\)-separated, nor that the compressed middle owners
are distinct and spanning.

One can replace a repetition-free \(2d\)-edge excursion by a synthetic
Johnson geodesic of \(d\) edges, pairing its \(d\) removed labels with its
\(d\) inserted labels.  However, the intermediate middle owners are not
vertices certified by the GMM cycle.  The central-levels theorem supplies
no assertion that these synthetic owners are distinct globally, avoid the
already used owners, or make the target images (1.9)--(1.10) near-rainbow.
This is an exact ownership obstruction, not a missing routine projection.

## 4. The natural GMM Greene--Kleitman Hamilton cycle is not label-separated

The GMM full-cube Hamilton construction orders the Greene--Kleitman/BTK
symmetric chains and traverses every chain monotonically, joining
successive chains at alternating top or bottom endpoints.  We now audit
its physical edge-label word.

Let \(C,C'\) be successive nontrivial chains joined at their top
endpoints, and let their lengths be \(h,h'\).  Since their tops are cube
neighbors,

\[
                         |h-h'|=2.
\tag{4.1}
\]

The BTK top-containment law gives

\[
                         |U(C)\cap U(C')|
 \ge\min(h,h'),
\tag{4.2}
\]

where \(U(C)\) is the active coordinate alphabet of the chain.  At a
bottom join the complemented statement holds.

Choose a common active coordinate \(c\).  It is toggled once during the
monotone traversal of \(C\) and once during the traversal of \(C'\).
In the word

\[
 \underbrace{C}_{h\ {\rm edges}}\;
 \underbrace{\text{endpoint connector}}_{1\ {\rm edge}}\;
 \underbrace{C'}_{h'\ {\rm edges}},
\tag{4.3}
\]

the two occurrences have edge-index distance at most \(h+h'\).
Therefore every interface with

\[
                         1\le h,h'\le H-1
\tag{4.4}
\]

has a repeated coordinate inside a \(2H\)-edge window.

### Theorem 4.1 (asymptotically full interface failure)

Put \(n=2m\), \(W=\binom{2m}{m}\), and take \(H\) from (0.2).
Among the \(W\) Greene--Kleitman chain interfaces in the natural cyclic
GMM ordering, all but \(o(W)\) violate the \(2H\)-label separation needed
by Theorem 1.1.

#### Proof

The number of SCD chains of length at least \(L\) is exactly

\[
 \binom{n}{\left\lfloor(n-L)/2\right\rfloor}.
\tag{4.5}
\]

For \(L=H\), its ratio to \(W\) is

\[
 \exp\left[-\frac{H^2}{2n}
       +o\left(\frac{H^2}{n}\right)\right]
 =\exp[-\omega^2/4+o(\omega^2)]
 =o(1).
\tag{4.6}
\]

The number of chains of any fixed bounded length is \(O(W/m)=o(W)\).
Thus all but \(o(W)\) chains have lengths between a fixed positive
constant and \(H-1\).  Every exceptional chain is incident with at most
two cyclic chain interfaces, so all but \(o(W)\) interfaces satisfy
(4.4).  Equations (4.2)--(4.4) give a repeated label at each of them.
\(\square\)

Pairing consecutive cube edges therefore gives a walk in the halved cube
whose transition supports repeat within \(H\) steps at almost every chain
interface.  It is not \(H\)-safe.  Compressing every whole chain to one
central member removes precisely the chronological edge word on which the
GMM endpoint connectors act and does not turn this into a Johnson
projection.

## 5. Constant-one consequence

The useful GMM input is exactly the one-sided depth-one cycle:

\[
 \text{saturating two cube levels}
 \quad\Longrightarrow\quad
 \text{one rainbow Johnson shadow at \(q=1\)}.
\tag{5.1}
\]

The following implications are false without new hypotheses:

\[
 \begin{array}{c}
 \text{saturation of three or more levels}\\
 \Downarrow\ \text{not valid}\\
 \text{\(H\)-safe Johnson chronology},
 \end{array}
\qquad
 \begin{array}{c}
 \text{Hamiltonicity of a central band}\\
 \Downarrow\ \text{not valid}\\
 \text{near-rainbow images for all \(q\le H\)}.
 \end{array}
\tag{5.2}
\]

For exactly three levels, the precise positive gate is a saturating cycle
satisfying (1.6) and (2.3).  For wider bands, one additionally needs either

* a globally injective synthetic-middle resolution of every deep
  excursion, compatible across all depths; or
* \(2H\)-scale expiration excursions, whose physical toll must be charged.

These are new theorems, not consequences of the GMM central-levels
construction.  In particular, the construction does not bypass the
stateful all-depth chronology problem identified for product-SCD fusion.
