# Algebraic consecutive-face designs for the constant-one lane

Date: 2026-07-26

Method: pure mathematics only.

## 0. Verdict

There is no local counting obstruction to an algebraic consecutive-face
design at the required depth. In fact, the local Boolean-cube problem is
already solved more strongly than a Hamming-code construction could solve
it: a recursive nonlinear cycle factor of \(Q_\ell\) has coordinate
residence \(\ell\) and is simultaneously lower- and upper-shadow injective
for every \(q\leq \ell/2\).

The obstruction is at the outer assignment.

* If all Boolean fibers use one fixed coordinate pairing, an exact pair-type
  capacity identity forces a macroscopic shadow defect. No choice of cyclic
  orders, orthogonal arrays, or \(q\)-designs inside those fibers can change
  this identity.
* Mixing coordinate pairings removes the numerical type obstruction and
  gives a balanced fractional reservoir. But fibers belonging to different
  pairings overlap in their middle owners. Choosing one resolution class per
  fiber is then not a collection of independent choices; it is an integral
  owner-packing problem.
* A one-factorization by affine translations is too weak even as an outer
  matching design. A codimension-one affine subspace gives an exact
  two-point type distribution concentrated at the two extreme pair types.

The weakest useful explicit object is therefore a **mixed-frame resolvable
consecutive-face design**: an integral owner-disjoint selection of isometric
cycles, with the Catalan radius census, for which the simultaneous lower and
upper shadow maps have total collision excess \(o(W)\). This property
directly implies the constant-one theorem. It implies literal MWB only if
the selected cycles are additionally realized as one exact odd middle
wreath factor; arbitrary cube cycles do not provide that interface.

All elementary parameter counts for such a design pass at

\[
 H\asymp \sqrt{m\log m},\qquad H\ll \ell\ll m.
\]

Hamming coset tilings fail at \(H>\log_2(2\ell)\). Binary orthogonal arrays,
permutation \(q\)-designs, and perfect-matching designs are large enough by
counting, but none of their standard definitions includes the needed
integral owner equation.

## 1. The normalization: once for an SCD, balanced multiplicity for MWB

Put

\[
 W=\binom{2m}{m},\qquad N_q=\binom{2m}{m-q},\qquad
 \rho_q=\frac{N_q}{W}.
\tag{1.1}
\]

For \(q=o(m^{2/3})\), direct expansion of the product for \(\rho_q\) gives

\[
 \log\rho_q
 =\sum_{j=0}^{q-1}\log\frac{m-j}{m+j+1}
 =-\frac{q^2}{m}
  +O\!\left(\frac{q}{m}+\frac{q^3}{m^2}\right).
\tag{1.2}
\]

There are two different incidence problems.

### 1.1 Radius-thinned SCD incidence

Give every middle owner \(X\) a radius \(d(X)\). The symmetric-chain census
is

\[
 \#\{X:d(X)=d\}=N_d-N_{d+1},
\tag{1.3}
\]

with the last class truncated at \(H\). Hence the depth-\(q\) certified
domain

\[
 \mathcal D_q=\{X:d(X)\geq q\}
\]

has exactly \(N_q\) members. Its target layer also has \(N_q\) members.
Thus the correct ideal is one occurrence per target.

### 1.2 Unthinned wreath incidence

For the odd MWB lane, write

\[
 W_{\rm o}=\binom{2m+1}{m},\qquad
 N_{q,{\rm o}}=\binom{2m+1}{m-q},\qquad
 \rho_{q,{\rm o}}=\frac{N_{q,{\rm o}}}{W_{\rm o}}.
\]

In an exact odd middle wreath factor, every one of the \(W_{\rm o}\) middle
owners has a lower interval at every depth. The average depth-\(q\) load is

\[
 \bar c_q=\frac{W_{\rm o}}{N_{q,{\rm o}}}
 =\rho_{q,{\rm o}}^{-1},
\tag{1.4}
\]

not one. At \(H=\sqrt{m\log m}\), the odd analogue of the product
expansion (1.2) gives

\[
 \rho_{H,{\rm o}}=m^{-1+o(1)},\qquad
 \bar c_H=m^{1+o(1)}.
\tag{1.5}
\]

Consequently a literal “nearly once at every depth” assertion cannot be an
MWB assertion at growing Gaussian depth. It is either a radius-thinned SCD
assertion, or it must be replaced by near floor/ceiling balance around
\(W_{\rm o}/N_{q,{\rm o}}\).

## 2. Exact consecutive-face maps

Fix a coordinate perfect matching of the \(2m\) ground points. Once the
full, empty, and split pairs have been fixed, the orientations of the \(s\)
split pairs form \(Q_s=\mathbb F_2^s\).

Let \(F\) be a neighbor permutation whose cycles are isometric pair-flip
cycles. Write \(\rho(X)\) for the direction toggled from \(X\) to \(F(X)\),
and put

\[
 D_q^+(X)=
 \{\rho(X),\rho(FX),\ldots,\rho(F^{q-1}X)\}.
\tag{2.1}
\]

For a geodesic \(q\)-window these are \(q\) distinct directions. Its lower
shadow is completely encoded by

\[
 \Sigma_q^+(X)
 =\bigl(D_q^+(X),X|_{[s]\setminus D_q^+(X)}\bigr):
\tag{2.2}
\]

the pairs in \(D_q^+(X)\) are made empty, and all other split orientations
are retained. Using \(F^{-1}\) gives the upper-shadow encoding
\(\Sigma_q^-(X)\), with the deleted pairs made full.

The tuple in (2.2) is only a coordinate description of an actual subset of
the \(2m\)-point ground set. In a mixed-frame family, \(\Sigma_q^\pm\) below
always means that physical subset after forgetting the pair-frame tag.
Retaining the tag would make equal shadows coming from different frames look
different and would erase exactly the cross-frame collisions that must be
controlled.

For a certified domain \(\mathcal D_q\), define the collision excesses

\[
 \kappa_q^\pm
 =|\mathcal D_q|-|\Sigma_q^\pm(\mathcal D_q)|.
\tag{2.3}
\]

When \(|\mathcal D_q|=N_q\), this is also the number of missing targets in
the corresponding rank.

## 3. The weakest direct sufficient design property

The following property isolates exactly what an algebraic construction has
to supply.

### Definition 3.1 (mixed-frame resolvable consecutive-face design)

An \({\rm MRCF}(m,H,\ell;E)\) consists of isometric cycles selected from
possibly different coordinate-pair frames, satisfying:

1. their middle-owner supports are disjoint and cover all but \(E\) middle
   owners;
2. every selected cycle has length at least \(2\ell\), transition residence
   at least \(\ell\), and is radius-pure;
3. after an \(E\)-sized completion, the radius classes have the census
   (1.3) through \(H\);
4. the forward and reverse maps (2.2) satisfy

   \[
    HE+\sum_{q=1}^H(\kappa_q^++\kappa_q^-)=o(W).
   \tag{3.1}
   \]

Complement closure permits the last requirement to be stated on lower
shadows alone: if complement followed by cycle reversal carries the chosen
family to itself, then \(\kappa_q^+=\kappa_q^-\).

### Theorem 3.2 (MRCF implies coefficient one)

Suppose

\[
 H/\sqrt m\longrightarrow\infty,\qquad H=o(m),\qquad
 H/\ell\longrightarrow0,
\tag{3.2}
\]

and an \({\rm MRCF}(m,H,\ell;E)\) exists. Then the central Boolean band has
a literal rotor/SCD word of length \(W+o(W)\), and the audited outer-tail
construction gives

\[
 \nu(k)=(1+o(1))\binom{k}{\lfloor k/2\rfloor}.
\tag{3.3}
\]

#### Proof

At depth \(q\), the completed Catalan census gives \(N_q\) certified starts
and there are \(N_q\) targets. Before completion the lower and upper rows
need at most \(E+\kappa_q^+\) and \(E+\kappa_q^-\) literal repairs. Their
aggregate is \(o(W)\) by (3.1). This is the origin of the term \(HE\).

Cutting a cycle into a path destroys only \(O(H)\) boundary windows. There
are \(O(W/\ell)\) cycles, so all cycle cuts cost

\[
 O(HW/\ell)=o(W).
\]

The resulting chain flags form a near wreath-resolved SCD of the central
band. The tail outside \(H\gg\sqrt m\) costs \(o(W)\), proving (3.3).
\(\square\)

This is a direct even-lattice route. It must not be relabelled as MWB.

### 3.3 The corresponding property for literal MWB

Suppose instead that the selected algebraic cycles have been spliced into
one exact odd middle wreath factor. Let \(\mu_q(S)\) be the lower load of an
\((m-q)\)-set, let
\(c_q=\lfloor W_{\rm o}/N_{q,{\rm o}}\rfloor\), and let \(b_q(S)\) take the
values \(c_q,c_q+1\) with total \(W_{\rm o}\). The explicit sufficient
discrepancy condition is

\[
 \sum_{q\leq H}\frac1{2c_q}
 \|\mu_q-b_q\|_1=o(W_{\rm o}).
\tag{3.4}
\]

Indeed, equality of the two totals gives

\[
 \frac12\|\mu_q-b_q\|_1
 =\sum_S(\mu_q(S)-b_q(S))_+,
\]

so (3.4) is exactly a balanced-overload certificate for MWB. Arbitrary
isometric cube cycles do not themselves furnish the required exact odd
wreath factor, which is why Theorem 3.2 is the valid unconditional
interface for MRCF.

## 4. The local direction count

The elementary local lower bound is exponential, but it is far below the
number of available cube cycles.

### Lemma 4.1 (direction-catalog bound)

Let \(M\) starts in \(Q_s\) use only \(K_q\) distinct \(q\)-direction sets.
Then

\[
 |\Sigma_q^+(M)|\leq K_q2^{s-q}.
\tag{4.1}
\]

In particular, if \(M=(1-o(1))2^s\) and the collision excess is \(o(2^s)\),
then

\[
 K_q\geq(1-o(1))2^q.
\tag{4.2}
\]

If every cyclic order contributes at most \(\ell\) consecutive
\(q\)-direction sets, the number \(T\) of order templates must satisfy

\[
 T\geq(1-o(1))\frac{2^q}{\ell}.
\tag{4.3}
\]

#### Proof

For a fixed direction set \(D\), (2.2) has only \(2^{s-q}\) possible
outside orientations. Summing over \(D\) proves (4.1), and (4.2)--(4.3)
follow. \(\square\)

A polynomial library is therefore impossible at Gaussian \(q\). This is a
template-count obstruction, not a cube-size obstruction. A factor of
\(Q_s\) into \(2\ell\)-cycles has \(2^s/(2\ell)\) cycles. The inequality

\[
 \frac{2^q}{\ell}\leq\frac{2^s}{2\ell}
\]

already holds for every \(q\leq s-1\).

## 5. Hamming and affine coset tilings: an exact logarithmic ceiling

Consider a translate tiling of \(Q_\ell\) by one \(2\ell\)-cycle \(P\) and a
linear translation code \(K\leq\mathbb F_2^\ell\). Since \(P\) is a coset
transversal,

\[
 [\mathbb F_2^\ell:K]=2\ell.
\tag{5.1}
\]

Thus, writing \(r=\operatorname{codim}K\),

\[
 r=\log_2(2\ell).
\tag{5.2}
\]

Let \(A\) be a parity-check matrix for \(K\). If a permitted consecutive
direction set \(D\) has dependent columns in \(A_D\), then a nonzero
\(k\in K\) is supported inside \(D\). Two translates separated by \(k\)
then have the same outside orientation on that face, producing a shadow
collision. Hence face simplicity through depth \(H\) requires every
permitted \(H\)-block of columns to be independent. In particular,

\[
 \boxed{H\leq r=\log_2(2\ell).}
\tag{5.3}
\]

This is also the Singleton obstruction \(d(K)\leq r+1\) if one asks for all
\(H\)-faces. Hamming, BCH, or other linear codes cannot evade (5.3) while
one \(2\ell\)-cycle remains a complete syndrome transversal. Affine shifts
change coset representatives but not \(K\), \(A\), or the rank bound.

One can increase the syndrome dimension and place many cycles in each
resolution class. That leaves the one-transversal construction, however,
and returns to the integral resolution-class assignment in Definition 3.1.

## 6. A nonlinear inner factor already reaches linear depth

For powers of two \(\ell\), define \(F_\ell:Q_\ell\to Q_\ell\) recursively.
Let \(F_1\) toggle its only bit. If \(\ell=2a\) and
\(x=(u,v)\in Q_a\times Q_a\), set

\[
 F_{2a}(u,v)=
 \begin{cases}
  (F_a(u),v),&|u|+|v|\equiv0\pmod2,\\
  (u,F_a(v)),&|u|+|v|\equiv1\pmod2.
 \end{cases}
\tag{6.1}
\]

Every cycle has length \(2\ell\), and its transition word is \(\pi\pi\)
for a permutation \(\pi\) of the \(\ell\) directions. Moreover both maps
\(\Sigma_q^+\) and \(\Sigma_q^-\) are injective on all of \(Q_\ell\) for

\[
 q\leq \ell/2.
\tag{6.2}
\]

The proof is an induction. Two consecutive moves alternate between the
halves and

\[
 F_{2a}^{2t}(u,v)=(F_a^t(u),F_a^t(v)).
\]

For an even window \(q=2t\), its labelled shadow splits into the two
depth-\(t\) labelled shadows in the halves. For \(q=2t+1\), the cardinalities
of the two deleted direction sets reveal which half moved first, after which
the data split into depths \(t+1\) and \(t\). The reverse recursion is
identical. This proves injectivity through \(a=\ell/2\).

If \(s>\ell\), choose \(\ell\) active directions, apply \(F_\ell\) on them,
and retain the other \(s-\ell\) orientations as passive labels. This gives
the same two-sided injectivity on all of \(Q_s\). Thus the local
simultaneous-\(q\) problem is not the missing theorem.

## 7. Orthogonal arrays and \(q\)-designs: feasible but stronger than needed

### 7.1 Binary orthogonal arrays

An \({\rm OA}(N,s,2,H)\) has \(N\geq2^H\), since its projection on any \(H\)
columns must contain all \(2^H\) binary words.

This scale is feasible. Choose \(s\) random columns in \(\mathbb F_2^r\).
For a fixed \(H\)-set, the probability of linear dependence is at most
\((2^H-1)2^{-r}\). A union bound shows that columns exist with every
\(H\)-set independent once

\[
 r\geq H+\log_2\binom{s}{H}+O(1).
\tag{7.1}
\]

The \(2^r\) linear evaluations of these columns form an orthogonal array of
strength \(H\). If \(s=\Theta(m)\) and
\(H=\Theta(\sqrt{m\log m})\), then

\[
 r=O\!\left(H\log\frac{s}{H}\right)=o(s),
\tag{7.2}
\]

so \(N=2^{o(s)}\), well below the \(2^{s+o(s)}\) local state supply.

But an OA balances binary labels on prescribed coordinate sets. It does
not make those sets consecutive in a cycle order, and it says nothing about
collisions between physical targets belonging to different fibers. In
particular, an OA on frame-tagged shadows does not imply an OA after the
tags are forgotten.

### 7.2 Consecutive-block \(q\)-designs

Let \(T\) cyclic orders on active subsets of \([s]\) be used, each supplying
at most \(\ell\) consecutive \(q\)-sets. If every \(q\)-subset is to occur
\(\lambda_q\) times, the incidence count is

\[
 T\ell=\lambda_q\binom{s}{q}.
\tag{7.3}
\]

Thus a full unordered \(q\)-design needs at least
\(\binom{s}{q}/\ell\) orders. If ordered \(q\)-tuples are prescribed, the
corresponding lower bound is \((s)_q/\ell\). Both are far stronger than the
minimal injectivity demand \(2^q/\ell\) from (4.3).

Even these stronger counts are feasible at the target parameters:

\[
 \log\binom{s}{H}=H\log\frac{es}{H}+O(\log s)=o(s),
 \qquad
 \log(s)_H=H\log s+o(H\log s)=o(s).
\tag{7.4}
\]

Thus the number \(2^s/(2\ell)\) of available cycles is not a barrier to an
unordered or ordered near-design. Exact simultaneous designs also face
the divisibilities in (7.3); an \(o(W)\)-defect theorem may discard these
remainders. The decisive omission is again the global owner equation.

## 8. The fixed-pair type obstruction survives every inner design

Fix one coordinate perfect matching. A middle source type has \(f\) full,
\(f\) empty, and \(s=m-2f\) split pairs. The number of middle starts of
this type is

\[
 V_f=\frac{m!}{f!f!(m-2f)!}2^{m-2f}.
\tag{8.1}
\]

A lower rank-\(m-q\) target of type \(f\) has \(f\) full, \(f+q\) empty,
and \(m-2f-q\) split pairs. Their number is

\[
 T_{f,q}=
 \frac{m!}{f!(f+q)!(m-2f-q)!}2^{m-2f-q}.
\tag{8.2}
\]

Every depth-\(q\) start of source type \(f\) lands in target type \(f\).
Therefore every fixed-frame factor misses at least

\[
 \sum_f(T_{f,q}-V_f)_+
\tag{8.3}
\]

targets, independently of all direction orders. The exact ratio is

\[
 \frac{V_f}{T_{f,q}}
 =\lambda_{f,q}
 =\frac{2^q(f+q)_{\underline q}}{(m-2f)_{\underline q}}.
\tag{8.4}
\]

For orientation, write \(f=m/4+x\sqrt m\) and \(q=c\sqrt m\), with
\(c=o(m^{1/6})\). Uniformly on bounded \(x/c\),

\[
 \log\lambda_{f,q}=8cx+3c^2+o(1+c^2).
\tag{8.5}
\]

The middle-source type law is centered at \(x=0+o(1)\), while the target
type law is centered at \(x=-c/2+o(1)\). Stirling expansion of the exact
factorial laws (8.1)--(8.2) gives, uniformly for \(x=O(c)\), the respective
Gaussian exponents

\[
 -8x^2+o(c^2),
 \qquad
 -8(x+c/2)^2+o(c^2).
\tag{8.6}
\]

The capacity threshold in (8.5) is \(x=-3c/8+o(c)\), strictly between the
two centers. The target mass above this threshold is
\(\exp(-c^2/8+o(c^2))\). Below the threshold, use
\(\pi_q(f)\lambda_{f,q}=\rho_q^{-1}\pi_0(f)\): the source tail has mass
\(\exp(-9c^2/8+o(c^2))\), and \(\rho_q^{-1}=\exp(c^2+o(c^2))\).
Consequently the total coverable fraction in (8.3) is
\(\exp(-c^2/8+o(c^2))\), which tends to zero when \(c\to\infty\). For a
sufficiently large fixed \(c\), it is bounded away from one.

Hence a fixed coordinate pairing fails precisely in the range needed for
the outer tail. A \(q\)-design of direction sets cannot change
(8.1)--(8.4).

## 9. Affine-shift matchings have an exact subspace obstruction

Let the \(2m=2^t\) ground points be \(V=\mathbb F_2^t\). The translation
matchings

\[
 \mathcal P_a=\{\{x,x+a\}:x\in V\}/2,
 \qquad a\in V\setminus\{0\},
\tag{9.1}
\]

form a one-factorization. They are perfectly edge-balanced, but not
pair-type balanced.

Let \(S_0\leq V\) be a codimension-one subspace, and first take the middle
owner \(S_0\), of size \(m\).

* If \(a\in S_0\setminus\{0\}\), every matching edge stays within \(S_0\)
  or within its complement. Thus \(f=m/2\) and \(s=0\).
* If \(a\notin S_0\), every matching edge crosses the cut
  \(S_0,V\setminus S_0\). Thus \(f=0\) and \(s=m\).

The random-perfect-matching type is instead concentrated at \(f=m/4\).
Thus affine directions reproduce the first edge marginal while missing the
entire relevant type profile.

The obstruction persists at a lower target. Delete any \(q\)-set
\(R\subset S_0\) and put \(S=S_0\setminus R\). For
\(a\in S_0\setminus\{0\}\), at least \(m/2-q\) matching edges lie completely
in \(S\), so its candidate source dimension satisfies

\[
 s=m-2f\leq2q.
\tag{9.2}
\]

For \(a\notin S_0\), one has \(f=0\) and \(s=m\). If \(\ell>2q\), roughly
half the affine matching frames do not even contain an \(\ell\)-dimensional
source cube for \(S\), while the other half have the opposite extreme type.
Phase shifts and affine relabelings preserve this dichotomy. Therefore the
translation one-factorization is not a viable outer design uniformly over
targets.

## 10. What strength an outer matching design would need

A natural stronger object is a \(t\)-design of perfect matchings: a multiset
\(\mathscr P\) in which every partial matching of \(j\leq t\) disjoint edges
is contained in the same number of members. The elementary incidence lower
bound at strength \(t\) is

\[
 |\mathscr P|\binom mt
 \geq
 \frac{(2m)!}{(2m-2t)!2^t t!},
\]

or

\[
 |\mathscr P|
 \geq
 \frac{(2m)!(m-t)!}{(2m-2t)!2^tm!}
 =(2m)^t\exp\!\left(O(t^2/m)\right).
\tag{10.1}
\]

For \(t=H=\Theta(\sqrt{m\log m})\), the logarithm of (10.1) is
\(o(m)\). It is far below the logarithm \(\Theta(m\log m)\) of the number
of all perfect matchings. Counting therefore permits such a design.

Uniformity on \(t\)-edge partial matchings controls the first \(t\) falling-
factorial moments of the internal-pair count \(f\). It does not, by itself,
give the exact weighted identity needed by (8.4), because
\(\lambda_{f,q}\) is rational in \(f\) and the construction also discards
small source dimensions. The weakest outer condition is instead the direct
weighted type balance

\[
 \frac1{|\mathscr P|}
 \sum_{\mathcal P\in\mathscr P}
 \rho_q\lambda_{f_{\mathcal P}(S),q}
 \mathbf1_{\{m-2f_{\mathcal P}(S)\geq\ell\}}
 =1+o(1)
\tag{10.2}
\]

uniformly in every target \(S\) and every \(q\leq H\), together with the
analogous middle-owner equation. The full symmetric-group orbit satisfies
the untruncated version exactly in expectation, and a polynomial sampled
reservoir can satisfy (10.2) approximately. This is a fractional statement,
not the owner-disjoint integral selection in Definition 3.1.

## 11. Parameter feasibility at the calibrated depth

Take

\[
 H=\sqrt{m\log m},\qquad
 \ell\asymp\sqrt m\,\log m,
\tag{11.1}
\]

rounding \(\ell\) to a power of two. Then

\[
 H/\ell\asymp(\log m)^{-1/2}\to0,
 \qquad \ell=o(m),
 \qquad H<\ell/2
\tag{11.2}
\]

for all large \(m\). Typical fixed-pair orientation dimensions satisfy
\(s=\Theta(m)\), so the \(s<\ell\) strata have negligible mass.

At these parameters:

* cycle cutting costs \(O(HW/\ell)=o(W)\);
* the nonlinear factor in Section 6 gives exact local two-sided shadow
  injectivity through \(H\);
* the necessary template count \(2^H/\ell\) is exponentially smaller than
  the available \(2^s/(2\ell)\) cycles;
* even a full consecutive-block \(H\)-design has subexponential-in-\(s\)
  counting demand by (7.4);
* a binary OA of strength \(H\), or a perfect-matching design of strength
  \(H\), also has subexponential counting demand.

Thus no entropy, direction-supply, reset, or elementary design-size
inequality rules out the proposed route.

## 12. Exact remaining algebraic theorem

Let a **packet** consist of one isometric cycle, its coordinate-pair frame,
its radius label, and all consecutive lower and upper shadows through that
radius. Write

\[
 B_{X,P}=\mathbf1_{\{P\text{ owns }X\}},\qquad
 A_{q,S,P}^{\pm}
 =\#\{\text{certified starts of }P\text{ with physical shadow }S\}.
\tag{12.1}
\]

The algebraic assignment variables are \(z_P\in\{0,1\}\). After allowing an
exceptional owner set of size \(E=o(W/H)\), the exact owner equations are

\[
 \sum_P B_{X,P}z_P=1.
\tag{12.2}
\]

Together with the radius census, the weakest row equation needed by the
direct route is

\[
 \sum_{q\leq H}\left[
 \sum_{S\in\binom{[2m]}{m-q}}
 \left|\sum_P A_{q,S,P}^{+}z_P-1\right|
 +
 \sum_{S\in\binom{[2m]}{m+q}}
 \left|\sum_P A_{q,S,P}^{-}z_P-1\right|
 \right]=o(W).
\tag{12.3}
\]

Because the certified source and target totals agree, (12.3) is equivalent,
up to the \(HE\) exception allowance, to (3.1). For literal odd MWB, replace
the right-hand ideal \(1\) by a floor/ceiling vector
\(\beta_q(S)\in\{c_q,c_q+1\}\), omit the upper row, and weight the
depth-\(q\) \(L^1\) term by \(1/(2c_q)\), as in (3.4).

The desired algebraic theorem is:

> From a mixed family of pair frames satisfying (10.2), select packets so
> that every middle owner is used once, up to \(o(W/H)\) exceptions; the
> radius census is (1.3); and (3.1) holds.

This is the weakest explicit design property that implies coefficient one
within the cube-fiber lane. It is simultaneously an owner resolution and a
multi-rank shadow resolution. An OA addresses label marginals, a
\(q\)-design addresses direction-set marginals, and a perfect-matching
design addresses outer pair-type marginals. None of them alone enforces the
common integral packet selection.

The hidden dichotomy is exact:

1. with one fixed pair frame, the Boolean fibers are disjoint and the owner
   equation is automatic, but (8.3) is fatal;
2. with mixed pair frames, (8.3) can be balanced fractionally, but the fibers
   overlap and the owner equation becomes the unresolved integral packing
   theorem.

Accordingly, algebraic local resolution classes are viable ingredients, and
the nonlinear recursion already supplies the strongest needed inner one.
The constant-one lane now requires an algebraic **resolvable mixed-frame
packing**, not a stronger Hamming code or a larger orthogonal array.
