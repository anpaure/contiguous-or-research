# Physical cyclic-strip ports: the exact spread-approximation failure

Date: 2026-07-26

Method: pure mathematics only.  No computation, solver, or web input is
used.

## 0. Outcome

Consider the exact target-regular physical port hypergraph
\(\mathcal H^\#\) from
`MATH_THEOREM_PHYSICAL_PORT_EKR_HIGH_COVER_REDUCTION_20260726.md`.  Write

\[
 D=D_1,
 \qquad
 \theta_a={D_1\over D_a}\quad(1\le a\le H),       \tag{0.1}
\]

so every signed rank-\(a\) target retains exactly a \(\theta_a\)-fraction
of its raw strip incidences.  Middle targets and first-shadow targets are
unthinned.

The ordinary spread-approximation route does **not** apply.  The failed
hypothesis is hereditary spread of target links.  More precisely, there
are nested target sets

\[
 \mathcal A_r\subset\mathcal A_{r+1},
 \qquad
 |\mathcal A_r|=r^2,
 \qquad
 |\mathcal A_{r+1}\setminus\mathcal A_r|=2r+1,     \tag{0.2}
\]

with

\[
 \boxed{
 {d^\#(\mathcal A_{r+1})\over d^\#(\mathcal A_r)}
 \ge {1-o(1)\over
  4(m-r+1)(m-2r+2)(m-2r+1)}
 =m^{-3-o(1)}.}                                    \tag{0.3}
\]

This holds for some such pair in **every** exact target-regular port
system whenever

\[
 \log m\ll r=o(m^{1/4}),
 \qquad r+1\le H.                                  \tag{0.4}
\]

Here \(d^\#(A)\) denotes the number of selected physical port edges
containing every target in \(A\).

A hereditary \(\kappa\)-spread link inequality would require

\[
 {d^\#(A\cup B)\over d^\#(A)}\le\kappa^{-|B|}.    \tag{0.5}
\]

Applying (0.5) to (0.2)--(0.3) gives

\[
 \boxed{
 \kappa\le m^{(3+o(1))/(2r+1)}=1+o(1).}           \tag{0.6}
\]

Thus the physical port system has no useful growing spread parameter; in
fact it has no spread parameter bounded away from one on all links.

The obstruction is the two-dimensional rank--phase geometry.  An
\(r\times r\) rectangle contains \(r^2\) literal targets, but it is
specified by only

\[
                         (r-1)+(2r-2)=3r-3          \tag{0.7}
\]

ordered boundary coordinates.  Growing the rectangle by one row and one
column adds \(2r+1\) targets but only one inside coordinate and two outside
coordinates.  The conditional degree therefore loses \(m^3\), not
\(m^{\Theta(r)}\).

This failure persists after extracting a rectangle as a spread-approximation
core: the next border again violates spread.  At the high-cover threshold
\(\tau_0\) isolated in the EKR reduction, one may choose

\[
 \log m\ll r\ll\min\{m^{1/4},\sqrt{\tau_0}\},      \tag{0.8}
\]

so both rectangle cores have size \(o(\tau_0)\).  Hence the usual claim
that core extraction terminates before consuming the cover budget is also
unavailable.

This is a method obstruction, not a physical fractional-colouring
counterexample.  It does not disprove

\[
 \chi_f'(\mathcal H^\#)=D+o(D/\sqrt m).            \tag{0.9}
\]

It proves that a black-box spread approximation on ordinary target
vertices cannot establish (0.9).  The surviving route would need an
entropy-dimensional spread theorem which charges a whole rectangle border
for its three new boundary coordinates while still enforcing collisions
at every individual target.  No such theorem is presently supplied.

## 1. The spread hypothesis being tested

For a target set \(A\), let

\[
 \mathcal L(A)=\{C:A\subseteq e_C^\#\},
 \qquad d^\#(A)=|\mathcal L(A)|.                   \tag{1.1}
\]

The hereditary form required in a spread approximation is that, after a
small core \(A\) has been extracted, the residual link satisfies

\[
 {d^\#(A\cup B)\over d^\#(A)}le\kappa^{-|B|}     \tag{1.2}
\]

for every feasible set of new target vertices \(B\).  Variants allow a
constant factor or bounded core multiplicity.  Neither changes the audit:
the exponent \(|B|=2r+1\) tends to infinity, whereas the physical cost in
(0.3) has exponent three.

There is already a constant-size closure.  If two adjacent middle owners
\(X,Y\) lie in one strip, then the unthinned targets

\[
                         X\cap Y,\qquad X\cup Y    \tag{1.3}
\]

are forced, so

\[
 d^\#(X,Y,X\cap Y,X\cup Y)=d^\#(X,Y).             \tag{1.4}
\]

One could absorb each such diamond into the core.  The rectangle theorem
below shows that this finite closure repair is insufficient: the
rank--phase dependency has unbounded size.

## 2. Shallow rank--phase rectangles

Fix a raw physical strip with core \(K\), \(|K|=m-h\), and cyclic active
order

\[
                         z_0,z_1,\ldots,z_{2h-1}.
\]

Take an oriented phase \(t\) and an integer \(r<h/3\).  With indices read
cyclically, define

\[
 T_{u,a}=K\cup I_z(t+u,h+a),
 \qquad 0\le u,a<r,                                \tag{2.1}
\]

and put

\[
                         \mathcal A_r(t)
                         =\{T_{u,a}:0\le u,a<r\}.  \tag{2.2}
\]

All these targets are distinct: different \(a\)'s have different ranks,
and at one rank the \(r<h\) consecutive cyclic intervals are distinct.
Thus \(|\mathcal A_r|=r^2\).

Let \(T=T_{0,0}\).  Write the active order relative to this middle phase
as an inside word and an outside word:

\[
 \alpha=(z_t,\ldots,z_{t+h-1})\subset T,
 \qquad
 \beta=(z_{t+h},\ldots,z_{t+2h-1})\subset[2m]\setminus T.        \tag{2.3}
\]

Then

\[
 T_{u,a}
 =T\setminus\{\alpha_0,\ldots,\alpha_{u-1}\}
   \cup\{\beta_0,\ldots,\beta_{u+a-1}\}.          \tag{2.4}
\]

Consequently the whole \(r^2\)-target rectangle is determined by the
ordered prefixes

\[
 \alpha_0,\ldots,\alpha_{r-2},
 \qquad
 \beta_0,\ldots,\beta_{2r-3}.                     \tag{2.5}
\]

This proves the entropy count (0.7).

### Lemma 2.1 (raw rectangle degree)

For a fixed oriented rectangle \(\mathcal A_r\), its raw physical-strip
degree satisfies

\[
 {d_{\rm raw}(\mathcal A_r)\over D_0}
 \asymp {1\over (m)_{r-1}(m)_{2r-2}},              \tag{2.6}
\]

up to the harmless factor two from reversal of the cyclic order.  In
particular,

\[
 {d_{\rm raw}(\mathcal A_r)\over D_0}
 =m^{-3r+3+o(r)}.                                  \tag{2.7}
\]

#### Proof

A strip through \(T\) is obtained, up to reversal, by choosing an ordered
\(h\)-tuple from \(T\) and an ordered \(h\)-tuple from its complement.
The degree is

\[
                         D_0={(m)_h^2\over2}.       \tag{2.8}
\]

For the rectangle in (2.2), (2.5) fixes the first \(r-1\) entries of the
inside word and the first \(2r-2\) entries of the outside word.  The
remaining entries have

\[
 (m-r+1)_{h-r+1}(m-2r+2)_{h-2r+2}                 \tag{2.9}
\]

ordered completions.  Divide (2.9), with the same reversal convention, by
(2.8), and use

\[
 (m)_h=(m)_{r-1}(m-r+1)_{h-r+1}
       =(m)_{2r-2}(m-2r+2)_{h-2r+2}.
\]

This gives (2.6), with absolute factors between the two possible cyclic
orientations; (2.7) follows from \(r=o(m)\). \(\square\)

### Lemma 2.2 (one-border extension count)

For an oriented \(\mathcal A_r\), the number of possible oriented
\((r+1)\times(r+1)\) rectangle extensions is at most

\[
 L_r=(m-r+1)(m-2r+2)(m-2r+1).                     \tag{2.10}
\]

Every raw completion of \(\mathcal A_r\) determines exactly one such
extension.

#### Proof

The larger rectangle fixes one further inside entry and two further
outside entries.  After (2.5), there are respectively

\[
 m-r+1,\qquad (m-2r+2)(m-2r+1)
\]

ordered choices.  Once those entries are fixed, (2.4) determines all
\(2r+1\) targets in the new row and column. \(\square\)

## 3. Exact target regularity cannot destroy all rectangles

For \(a\ge1\), exact target regularity gives the retained incidence
fraction

\[
 \theta_a={D_1\over D_a}.
\]

### Lemma 3.1 (shallow deletion mass)

Uniformly for \(1\le a=o(\sqrt m)\),

\[
                         1-\theta_a=O(a^2/m).       \tag{3.1}
\]

#### Proof

From the exact factorial formula,

\[
 {D_a\over D_1}
 ={(m+a)!(m-a)!\over(m+1)!(m-1)!}.
\]

Taking logarithms and expanding each factor \(\log(1+O(a/m))\) gives

\[
                         \log(D_a/D_1)=O(a^2/m).
\]

Since \(\theta_a=(D_a/D_1)^{-1}\le1\), (3.1) follows. \(\square\)

Let \(M=|\mathscr C_{m,h}|\) be the number of raw physical strips.  At
each fixed signed rank \(a\), every raw strip has exactly \(2h\) target
incidences.  Hence the total number of deleted rank-\(a\) incidences is

\[
                         2hM(1-\theta_a).           \tag{3.2}
\]

For a strip \(C\) and oriented phase \(t\), call \((C,t)\)
\(r\)-complete if every target of \(\mathcal A_r(C,t)\) is retained in
\(e_C^\#\).

### Theorem 3.2 (deterministic rectangle abundance)

If \(r=o(m^{1/4})\) and \(r\le H\), then

\[
 \boxed{
 |\{(C,t):(C,t)\text{ is }r\text{-complete}\}|
 \ge(1-O(r^4/m))\,2hM.}                            \tag{3.3}
\]

This holds for every port system with exact target degrees \(D_1\); no
independence or randomness is assumed.

#### Proof

A deleted incidence at phase \(u\) and rank \(a<r\) lies in exactly \(r\)
of the cyclic phase intervals of length \(r\), hence can spoil at most
\(r\) labelled rectangles \(\mathcal A_r(C,t)\) in its strip.  By the
union bound, (3.2), and Lemma 3.1, the number of spoiled pairs is at most

\[
 \begin{aligned}
 r\sum_{a=1}^{r-1}2hM(1-\theta_a)
 &\le O\left(r{r^3\over m}\right)2hM\\
 &=O(r^4/m)\,2hM.
 \end{aligned}
\]

Subtract from the \(2hM\) raw strip--phase pairs. \(\square\)

Thus independent targetwise thinning is not the source of the cluster.
There are too few shallow deleted incidences to hit all rank--phase
rectangles.

## 4. Hereditary spread fails after every rectangle core

### Lemma 4.1 (rectangle rigidity)

For \(3\le r<h/3\), a physical strip containing every target of a fixed
\(\mathcal A_r\) realizes its middle targets as one consecutive Johnson
path, in one of at most two orientations.  In either orientation its
\((r+1)\)-rectangle extension is determined by the three new boundary
coordinates of Lemma 2.2.

#### Proof

The rank-\(m\) members of \(\mathcal A_r\) are \(r\) consecutive middle
windows.  Their induced Johnson-adjacency graph is the path \(P_r\):
successive windows differ in one exchange and every non-successive pair
has Johnson distance at least two.  Any physical isometric cycle
containing these middle targets must therefore place them consecutively,
and the path has only its two orientations.  Formula (2.4) then places all
higher-rank targets and proves the last assertion. \(\square\)

### Theorem 4.2 (hereditary nonspread pair)

Under (0.4), every exact target-regular port system contains nested target
sets \(\mathcal A_r\subset\mathcal A_{r+1}\) satisfying (0.2)--(0.3).

#### Proof

Apply Theorem 3.2 at \(r\) and \(r+1\).  Since both exceptional fractions
are \(O(r^4/m)=o(1)\), a \((1-o(1))\)-fraction of the \(r\)-complete
strip--phase pairs are also \((r+1)\)-complete.

Group the complete pairs by their underlying, unoriented target set
\(\mathcal A_r\).  Lemma 4.1 says that every selected completion is
represented at most twice.  The preceding global estimate therefore
implies, by averaging, that some \(\mathcal A_r\) has at least a
\((1-o(1))/2\)-fraction of its selected completions extending to a
selected \(\mathcal A_{r+1}\).  Lemma 2.2 and the two orientations give
at most \(2L_r\) possible extensions, so one extension has

\[
 {d^\#(\mathcal A_{r+1})
  \over d^\#(\mathcal A_r)}
 \ge{1-o(1)\over4L_r}.                             \tag{4.1}
\]

This proves (0.3).  Finally, the new row and column contain
\((r+1)^2-r^2=2r+1\) targets. \(\square\)

### Corollary 4.3 (failure of ordinary spread)

If the link above \(\mathcal A_r\) is \(\kappa\)-spread in the ordinary
target-vertex sense, then (0.6) holds.

#### Proof

Put \(B=\mathcal A_{r+1}\setminus\mathcal A_r\) in (1.2).  Equations
(0.2)--(0.3) give

\[
 \kappa^{-(2r+1)}\ge m^{-3-o(1)}.
\]

Take \((2r+1)\)-st roots. \(\square\)

## 5. Why spread-core extraction does not repair the audit

A spread approximation normally extracts a small target core whenever a
link violates (1.2), and applies a spread theorem after the extraction
terminates.  Here the violations form the nested sequence

\[
 \mathcal A_3\subset\mathcal A_4\subset\cdots,
 \qquad |\mathcal A_r|=r^2.                        \tag{5.1}
\]

At every step, the next \(2r+1\) target vertices cost only three new
boundary coordinates.  Therefore no link on this sequence has a useful
ordinary spread parameter.

Let \(\tau_0\) be the lower cover scale of a putative distributed EKR
blocker.  In the default ports one has

\[
                         \tau_0=m^{1/3-o(1)},
\]

and at the optimized strip scale

\[
                         \tau_0={\sqrt m\over\operatorname{polylog}m}.
\]

In either case one may choose \(r\) satisfying (0.8).  Then

\[
                         |\mathcal A_{r+1}|=o(\tau_0),             \tag{5.2}
\]

so the approximation cannot declare the extracted core to be a target
cover, yet its residual link is still nonspread by Corollary 4.3.  This
is the exact termination hypothesis that fails.

The same conclusion holds after quotienting the forced diamonds (1.3).
The rectangle has \(\Theta(r^2)\) targets but only \(\Theta(r)\) diamonds
along its middle boundary, and its higher-rank interior remains
deterministically generated by the same boundary words.

## 6. Consequences for EKR and fractional colouring

The preceding note proved that literal linear spaces, bounded-overlap
families, and target-pair odd-set blow-ups are harmless.  Spread
approximation was a plausible way to handle the remaining distributed
nonlinear family.  Theorem 4.2 blocks that black-box step:

\[
 \boxed{
 \text{ordinary target cardinality is not the entropy dimension of a
 physical port link}.}                             \tag{6.1}
\]

This does not construct an intersecting family of size
\(\Omega(D/\sqrt m)\), nor a weight violating the matching dual.  The
rectangles are local link clusters; a global blocker would still have to
couple many such clusters while remaining pairwise intersecting or while
defeating every matching.

The exact weighted target therefore remains

\[
 \sum_Cy_C
 \le\left(D+o(D/\sqrt m)\right)
      \max_{M\text{ matching}}\sum_{C\in M}y_C.     \tag{6.2}
\]

What has failed is the proposed derivation of (6.2) from a standard
spread approximation.

## 7. The only plausible spread repair

For a rectangle border \(B_r=\mathcal A_{r+1}\setminus\mathcal A_r\),
define its boundary dimension by

\[
                         \partialdim(B_r)=3,         \tag{7.1}
\]

corresponding to the one new inside coordinate and two new outside
coordinates.  The physical link does satisfy the correctly scaled local
law

\[
 {d^\#(\mathcal A_r\cup B_r)\over d^\#(\mathcal A_r)}
 \asymp m^{-\partialdim(B_r)}.                      \tag{7.2}
\]

A useful replacement would have to prove a disjointness or matching
theorem from a submodular boundary-rank function \(\partialdim\), rather
than from ordinary target cardinality.  Two obstacles must be handled
explicitly:

1. collision is still at an individual target, so rectangle borders
   cannot simply be contracted to independent atoms; and
2. two different rectangles can share long target subrectangles while
   using different next boundary coordinates, so \(\partialdim\) is not
   additive on arbitrary unions.

Thus “quotient each rectangle” is not yet a proof.  The precise surviving
theorem would be a **submodular entropy-spread matching theorem** for the
rank--phase boundary matroid, together with a verification that its
weighted matching conclusion has the additive error \(o(D/\sqrt m)\).

## 8. Audited boundary

Proved:

1. exact shallow deletion mass \(1-\theta_a=O(a^2/m)\);
2. deterministic abundance of complete rank--phase rectangles in every
   exact target-regular port system;
3. the hereditary link ratio (0.3); and
4. failure of every ordinary \(\kappa\)-spread hypothesis with
   \(\kappa>1+o(1)\), even after sub-cover-size core extraction.

Not proved:

1. a distributed high-cover physical EKR family;
2. a physical fractional-colouring obstruction; or
3. a submodular entropy-spread replacement theorem.

Therefore spread approximation does not close the EKR/fractional-colouring
gate.  Its exact failed hypothesis is hereditary decay by the **number of
new target vertices**; physical links decay only by the number of new
boundary coordinates.
