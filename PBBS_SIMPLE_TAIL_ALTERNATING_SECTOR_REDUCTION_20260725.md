# PBBS simple-tail load is an alternating-sector count

Date: 2026-07-25

Pure mathematics only.

## 0. Outcome

Fix a middle set

\[
 T\in\binom{[2r+1]}r.
\]

For a simple PBBS return sector, the two nonfixed terms in the ambient
completion kernel are nonzero exactly when the half-open omitted-label word
has one of the two strictly alternating membership patterns

\[
 0,1,0,1,\ldots,0
 \quad\hbox{or}\quad
 1,0,1,0,\ldots,1
\]

relative to (T).  Along one step-two owner parity this is equivalently a
strictly monotone run of the intersection statistic (|A\cap T|).

Consequently the unresolved fractional completion inequality is exactly a
weighted enumeration of pairwise projected-edge-disjoint monotone PBBS
return sectors.  The weights are reciprocal binomial geodesic kernels.
This note proves that reduction and records two useful endpoint
interpretations.  It does not prove the required uniform bound.

## 1. Simple-return notation

Let a simple return have gap (2s+1), and write its omitted labels as

\[
 a_0,b_0,a_1,b_1,\ldots,a_{s-1},b_{s-1},a_s,a_0.
 \tag{1.1}
\]

The half-open labels in (1.1) are pairwise distinct.  Put

\[
 U=\{b_0,\ldots,b_{s-1}\},\qquad
 A=\{a_0,\ldots,a_s\},
 \tag{1.2}
\]

and put (q=r-s).  The simple-return normal form gives disjoint inactive
cores (K,K'), each of size (q), such that

\[
 A_{2h}=K\cup\{a_0,\ldots,a_{h-1}\}
              \cup\{b_h,\ldots,b_{s-1}\},
 \tag{1.3}
\]

\[
 A_{2h+1}=K'\cup\{b_0,\ldots,b_{h-1}\}
                \cup\{a_{h+1},\ldots,a_s\}.
 \tag{1.4}
\]

The completion-tail kernel from
`PBBS_SIMPLE_SECTOR_AMBIENT_COMPLETION_KERNEL_20260725.md` is

\[
 \begin{aligned}
 \pi_I(T)={}&
 \mathbf1_{\{T\cap(A\cup U)=U\}}
 \mathbf1_{\{1\le j\le q-1\}}
 {1\over\binom qj^2}\\
 &+\mathbf1_{\{T\cap(A\cup U)=A\}}
 {1\over\binom qj\binom q{j+1}},
 \end{aligned}
 \tag{1.5}
\]

where (j=|T\cap K|) in the first line and (j=|T\cap K'|) in the
second.

## 2. Exact alternating-label criterion

Write

\[
 \chi_T(x)=\mathbf1_{\{x\in T\}}.
\]

### Theorem 2.1 (tail compatibility is strict alternation)

For a simple sector (I):

1. the odd-tail term in (1.5) is nonzero exactly when
   
   \[
    \chi_T(a_0),\chi_T(b_0),\ldots,
    \chi_T(b_{s-1}),\chi_T(a_s)
    =0,1,0,1,\ldots,1,0;
    \tag{2.1}
   \]

2. the even-tail term in (1.5) is nonzero exactly when
   
   \[
    \chi_T(a_0),\chi_T(b_0),\ldots,
    \chi_T(b_{s-1}),\chi_T(a_s)
    =1,0,1,0,\ldots,0,1.
    \tag{2.2}
   \]

In the full return word (1.1), the final repeated (a_0) therefore makes
the last two membership bits equal.  Thus a compatible sector is a maximal
strictly alternating block terminated by a (00) or (11) return pair.

#### Proof

The condition (T\cap(A\cup U)=U) says precisely that every (b_h) lies
in (T) and every (a_h) lies outside (T), which is (2.1).  The
condition (T\cap(A\cup U)=A) gives the reverse pattern (2.2).  The final
claim uses the return identity (lambda_{2s+1}=a_0).  \(\square\)

The importance of Theorem 2.1 is that the condition involves the actual
PBBS omitted-label chronology.  It is not an arbitrary condition on two
abstract cores.

## 3. Exact monotone-run form

For (0\le h\le s), put

\[
 x_h=|A_{2h}\cap T|,
 \qquad
 y_h=|A_{2h+1}\cap T|.
 \tag{3.1}
\]

### Theorem 3.1 (two monotone owner arms)

In the odd-tail case, with (j=|K\cap T|),

\[
 \boxed{x_h=j+s-h,\qquad y_h=q-j+h.}
 \tag{3.2}
\]

Thus the even step-two arm is strictly decreasing and the odd arm is
strictly increasing.

In the even-tail case, with (j=|K'\cap T|),

\[
 \boxed{x_h=q-1-j+h,\qquad y_h=j+s-h.}
 \tag{3.3}
\]

Thus the even arm is strictly increasing and the odd arm is strictly
decreasing.

#### Proof

In the odd case, (T) contains every (b_t) and no (a_t).  Equation
(1.3) therefore gives

\[
 x_h=|K\cap T|+|\{b_h,\ldots,b_{s-1}\}|=j+s-h.
\]

Since (T) has size (r=s+q), its inactive contribution outside (K)
is (q-j), all lying in (K'), and (1.4) gives

\[
 y_h=q-j+h.
\]

The even case is identical with the roles reversed.  Here (T) contains
all (s+1) labels (a_t), no (b_t), and has (j) elements in (K'),
so its contribution in (K) is (q-1-j).  Substitution in
(1.3)--(1.4) gives (3.3).  \(\square\)

This also follows one edge at a time from

\[
 A_{t+2}=A_t-\{\lambda_{t+1}\}+\{\lambda_t\}.
\]

Every step of a compatible arm exchanges a (T)-label for a
(T^c)-label in the same direction.

## 4. Endpoint-geodesic interpretation of the odd kernel

Let

\[
 X=A_0=K\cup U,
 \qquad
 Y=A_{2s+1}=K'\cup U.
 \tag{4.1}
\]

Then

\[
 X\cap Y=U,qquad d_J(X,Y)=q,
 \tag{4.2}
\]

where (d_J) is Johnson distance.  In the odd-tail case,

\[
 U\subseteq T\subseteq X\cup Y,
 \tag{4.3}
\]

and

\[
 d_J(T,Y)=j,qquad d_J(T,X)=q-j.
 \tag{4.4}
\]

A uniform ambient completion chooses a uniform shortest Johnson geodesic
from (Y) to (X).  Its probability of passing through (T) is exactly

\[
 {1\over\binom qj^2}.
 \tag{4.5}
\]

Indeed, among the (q) labels of (K), the prescribed (j)-set
(T\cap K) must be chosen first, and among the (q) labels of (K'),
the prescribed (j)-set (K'\setminus T) must be removed first.

The even kernel has the analogous two-sided ordering description, with
unequal block sizes (j) and (j+1), which yields

\[
 {1\over\binom qj\binom q{j+1}}.
 \tag{4.6}
\]

## 5. A common-random-priority realization

Assign independent continuous random priorities to all physical labels.
For each sector, order (K) and (K') by restricting this one global
priority order.  Then:

* in the odd case, the event that the completed tail contains (T) is
  exactly
  
  \[
   T\cap K \prec K\setminus T,
   \qquad
   K'\setminus T \prec T\cap K';
   \tag{5.1}
  \]

* in the even case, it is exactly
  
  \[
   K\setminus T \prec T\cap K,
   \qquad
   T\cap K' \prec K'\setminus T.
   \tag{5.2}
  \]

Here (B\prec C) means that every priority in (B) is smaller than every
priority in (C).  The probabilities of (5.1)--(5.2) are precisely
(4.5)--(4.6).

This couples all completion kernels on one probability space.  Therefore
the desired tail-load bound would follow from an (O_A(1)) pointwise
multiplicity theorem for the compatible priority-separation events.
No such multiplicity theorem is proved here.

## 6. Exact alternating-sector count

For a projected-edge-disjoint simple-sector family \(\mathcal P\), let

\[
 N^-_{s,j}(T)
\]

be the number of its residence-((s+1)) sectors satisfying (2.1) and
(|K\cap T|=j).  Let

\[
 N^+_{s,j}(T)
\]

be the number satisfying (2.2) and (|K'\cap T|=j).  Then the exact
fractional tail load is

\[
 \boxed{
 \begin{aligned}
 \sum_{I\in\mathcal P}\pi_I(T)
 ={}&\sum_{s\le H-1}\sum_{j=1}^{r-s-1}
 {N^-_{s,j}(T)\over\binom{r-s}{j}^2}\\
 &+\sum_{s\le H-1}\sum_{j=0}^{r-s-1}
 {N^+_{s,j}(T)\over
   \binom{r-s}{j}\binom{r-s}{j+1}}.
 \end{aligned}}
 \tag{6.1}
\]

Hence the remaining theorem is the following concrete assertion.

> **Alternating-sector estimate.**  For every fixed (A), every
> projected-edge-disjoint family of simple PBBS returns with
> (s+1\le\lceil A\sqrt r\rceil), and every middle set (T), the
> right-hand side of (6.1) is (O_A(1)).

By the ambient-completion criterion, this estimate implies the
Catalan-order residence packing theorem and hence coefficient one.

## 7. Endpoint layers close the extreme terms

The fixed open endpoint throughput gives useful exact boundary checks.

For odd sectors, (Y=A_{2s+1}) has Johnson distance (j) from (T).
There are

\[
 \binom rj\binom{r+1}j
 \tag{7.1}
\]

possible endpoints (Y), and every endpoint lies in at most four fixed
open sectors.  Thus

\[
 N^-_{s,j}(T)
 \le4\binom rj\binom{r+1}j.
 \tag{7.2}
\]

For even sectors, (Y=A_{2s+1}=K'\cup U) satisfies

\[
 |T\cap Y|=j.
\]

In particular, at (j=0), (Y) is an (r)-subset of (T^c), of which
there are exactly (r+1).  Endpoint throughput applies across all sector
lengths at once, so

\[
 \sum_sN^+_{s,0}(T)\le4(r+1),
 \tag{7.3}
\]

and their total weighted contribution is at most

\[
 {4(r+1)\over r-H}=O_A(1)
 \tag{7.4}
\]

uniformly for (H\le A\sqrt r+1).  Similarly, all odd (j=1) terms
together are bounded by

\[
 {4r(r+1)\over(r-H)^2}=O_A(1).
 \tag{7.5}
\]

The symmetric endpoint terms admit the same bounds from the other fixed
endpoint: all even (j=q-1) terms have total (O_A(1)), as do all odd
(j=q-1) terms.  Thus the genuine difficulty lies in the interior values
of (j), not in the largest (1/q) and (1/q^2) kernel entries.

## 8. Why a generic monotone-path argument is insufficient

The number of rank-(r) vertices with (|Y\cap T|=j) is (7.1).  Around
the central values of (j), the ratio

\[
 {\binom rj\binom{r+1}j\over\binom{r-s}{j}^2}
 \tag{8.1}
\]

can be exponential in (s), of order (4^s).  Thus endpoint throughput,
layer sizes, or abstract edge-disjoint monotone paths do not prove (6.1).
The missing saving must use the PBBS first-return chronology: among the
abstract monotone sectors, only a very sparse subset can be consecutive
simple omitted-label returns.

This identifies the exact next target.  One needs an (O_A(1)) weighted
count of actual PBBS alternating return pairs, or a chronological
completion rule whose full-wreath loads are bounded.  An arbitrary
Johnson-path packing theorem is quantitatively off by the factor displayed
in (8.1).

## 9. The weaker linear-seam gate removes every sub-Gaussian endpoint strip

The linear-seam theorem does not require the (O_A(1)) bound proposed in
Section 6.  It is enough to prove

\[
 \sup_T\sum_{I\in\mathcal P}\pi_I(T)=o_A(\sqrt r),
 \tag{9.1}
\]

because the completion double count then gives

\[
 |\mathcal P|=o_A(B_r\sqrt r),
\]

which is exactly the physical form of the sufficient gate
((\mathrm{ST}_A)).

There is an unconditional reduction of (9.1) to the genuinely interior
mixtures.  Let (J=J(r)) satisfy

\[
 J\longrightarrow\infty,
 \qquad J=o(\sqrt r).
 \tag{9.2}
\]

### Theorem 9.1 (endpoint-strip load is little-oh critical)

Uniformly over every projected-edge-disjoint simple-sector family with
(s+1\le H\le A\sqrt r+1), and every (T), the total contribution to
(6.1) of

\[
 \min\{j,q-j\}\le J
\]

in the odd kernel and of

\[
 \min\{j,q-1-j\}\le J
\]

in the even kernel is

\[
 \boxed{O_A(J)=o_A(\sqrt r).}
 \tag{9.3}
\]

#### Proof

First consider the left odd strip.  For fixed (j), endpoint throughput
and (7.1) give, across every sector length simultaneously,

\[
 \sum_sN^-_{s,j}(T)
 \le4\binom rj\binom{r+1}j.
 \tag{9.4}
\]

Since (q=r-s\ge r-H), for (j\le J=o(\sqrt r)),

\[
 \begin{aligned}
 {\binom rj\binom{r+1}j\over\binom{r-H}j^2}
 &\le
 \exp\left(
 {jH\over r-H-j}
 +{j(H+1)\over r-H-j}
 \right)\\
 &=\exp(o_A(1)).
 \end{aligned}
 \tag{9.5}
\]

Summing (9.4) with the largest possible kernel over (j\le J) gives
(O_A(J)).

For the left even strip, the number of possible fixed endpoints with
(|T\cap Y|=j) is

\[
 \binom rj\binom{r+1}{j+1}.
\]

Hence endpoint throughput gives

\[
 \sum_sN^+_{s,j}(T)
 \le4\binom rj\binom{r+1}{j+1}.
 \tag{9.6}
\]

The analogue of (9.5) is

\[
 {\binom rj\binom{r+1}{j+1}
  \over
  \binom{r-H}j\binom{r-H}{j+1}}
 \le\exp(o_A(1)),
 \tag{9.7}
\]

uniformly for (j\le J).  Its sum is again (O_A(J)).

For the right strips use the other fixed endpoint.  In the odd case put
(d=q-j); that endpoint has Johnson distance (d) from (T), and the
kernel is (1/\binom qd^2).  In the even case put
(d=q-1-j); the other endpoint has intersection size (d) with (T),
and the kernel is

\[
 {1\over\binom qd\binom q{d+1}}.
\]

The same calculations (9.4)--(9.7), with (d) in place of (j), give
another (O_A(J)).  This proves (9.3).  \(\square\)

The estimate also has a useful two-parameter form.  If
\(J=\lfloor\varepsilon\sqrt r\rfloor\), the exponents in
(9.5) and (9.7) are \(O(A\varepsilon)\), and hence

\[
 \boxed{
 \limsup_{r\to\infty}
 {L_{\rm endpoint}(\varepsilon,A)\over\sqrt r}
 \le C\varepsilon e^{CA\varepsilon}.}
 \tag{9.8}
\]

Thus one may first take the rank limit and then let
\(\varepsilon\downarrow0\).  Any positive critical mass must remain in a
fixed genuinely mixed window

\[
 \varepsilon\sqrt r\le j,\qquad
 \varepsilon\sqrt r\le q-j
\]

(with \(q-1-j\) in the even case), for some fixed
\(\varepsilon>0\).

Thus a critical counterfamily, if one exists, must place essentially all
of its completion mass in sectors satisfying

\[
 j\to\infty,
 \qquad q-j\to\infty
\]

(and the analogous even inequalities).  Equivalently, neither inactive
core is allowed to be almost aligned with (T).  Only these genuinely
mixed, perfectly alternating PBBS sectors remain capable of saturating the
reciprocal-height trace scale.

## 10. Exact critical-saturation contrapositive

The preceding conclusion can be made quantitative without assuming any
pointwise completion estimate.

For a sector of residence (s+1), the completion has (N=2r+1) middle
vertices and its fixed open part has (2s+2) vertices.  Therefore

\[
 \sum_{T\in\binom{[N]}r}\pi_I(T)=N-(2s+2).
 \tag{10.1}
\]

If every sector has (s+1\le H\le A\sqrt r+1), then

\[
 \sum_T\sum_{I\in\mathcal P}\pi_I(T)
 \ge (N-2H)|\mathcal P|.
 \tag{10.2}
\]

Let (L_{\rm bulk}(T)) denote the part of (6.1) outside the endpoint
strips of Theorem 9.1.

### Corollary 10.1 (a critical family forces a bulk alternating witness)

If, along some sequence of ranks,

\[
 |\mathcal P|\ge cB_r\sqrt r
 \tag{10.3}
\]

for a fixed (c>0), then for every choice (J\to\infty),
(J=o(\sqrt r)), there is a middle set (T) for which

\[
 \boxed{L_{\rm bulk}(T)\ge(c-o_A(1))\sqrt r.}
 \tag{10.4}
\]

#### Proof

Since (W=NB_r), equations (10.2)--(10.3) imply that the average tail
load over (T) is at least

\[
 {N-2H\over W}|\mathcal P|
 \ge(c-o_A(1))\sqrt r.
\]

The endpoint-strip load is (O_A(J)=o_A(\sqrt r)) for every (T) by
Theorem 9.1.  Subtract it and take a maximizer of the remaining load.
\(\square\)

Thus failure of the sufficient packing gate has an exact witness: one
fixed middle set sees critical mass from actual simple PBBS first-return
sectors, every one of whose omitted labels alternates perfectly relative
to that set and whose two inactive cores are both genuinely mixed.  It is
enough for coefficient one to prove that no such bulk witness exists.

## 11. Every inactive core label gives an enclosing return pair

The return-pair chronology supplies one further exact structure.  Lift a
simple sector to indices

\[
 0,1,\ldots,2s+1,
\]

with (lambda_{2s+1}=lambda_0).  For an inactive label (zin K\cup
K'), let (p(z)<0<n(z)), with (n(z)>2s+1), be the consecutive
occurrences of (z) which bracket the sector.

### Lemma 11.1 (two enclosing residence decks)

1. If (z\in K), then (p(z)) is even and (n(z)) is odd.  Its
   projected return trace
   
   \[
    \{p(z)-1,p(z)+1,\ldots,n(z)\}
   \]
   contains the sector trace
   
   \[
    I=\{-1,1,\ldots,2s+1\}.
   \]

2. If (z\in K'), then (p(z)) is odd and (n(z)) is even.  Its
   projected return trace contains the translated sector trace
   
   \[
    I+1=\{0,2,\ldots,2s+2\}.
   \]

#### Proof

No inactive label occurs in the half-open active word, so its consecutive
bracketing occurrences lie strictly outside the sector.  On the even
step-two owner line, an occurrence at an even omitted-label index inserts
that label and an occurrence at an odd index removes it, by

\[
 A_{t+2}=A_t-\{\lambda_{t+1}\}+\{\lambda_t\}.
\]

Every label of (K) is present throughout the even arm (1.3).  Its last
bracketing occurrence must therefore be the even insertion and its next
one the odd removal.  This proves the parity assertion and the containment
of (I).  Every label of (K') is absent throughout the even arm and
present throughout the odd arm (1.4), giving the reversed parities and the
containment of (I+1).  \(\square\)

After the parity split used in the simple-return reduction, both the
sector traces (I) and their translates (I+1) are pairwise disjoint.
Thus every bulk alternating sector is simultaneously enclosed by (q)
same-parity and (q) opposite-parity genuine PBBS return pairs.  A future
proof may exploit the ordered endpoints of these (2q) enclosing pairs.
The unweighted incidence count alone gives no gain: each projected edge
already lies in (r+2) complete residence intervals, so summing only the
number of enclosures reproduces the existing critical edge ledger.

## 12. Exact enclosure-capacity ledger and its saturation boundary

The last observation admits a useful exact weighted form.  Work in one
PBBS quotient-height stratum (h), and lift its (b_{r,h}) quotient
edges through all (N) spatial phases.  Thus the physical edge volume of
the stratum is

\[
 E_h=N b_{r,h}.
 \tag{12.1}
\]

Use the complementary \(A\)-owner normalization, whose owners have rank
\(r\).  For every physical coordinate, its consecutive positive-residence
traces partition the edges on which that coordinate is present.  Summing
their lengths over all coordinates counts each Johnson edge exactly
\(r+1\) times: the \(r-1\) coordinates common to its endpoints contribute
internally, and the departing and arriving coordinates contribute at the
two boundaries.

Let (mathcal P_h) be a same-start-parity, projected-edge-disjoint family
of simple sectors in this height stratum.  Write (|I|) for the number of
projected edges in the sector trace and (q_I=r-s_I).

### Proposition 12.1 (core-enclosure capacity)

\[
 \boxed{
  \sum_{I\in\mathcal P_h}q_I|I|
  \le(r+1)E_h.}
 \tag{12.2}
\]

The translated-parity (K')-enclosures satisfy the identical inequality.

#### Proof

For every (z\in K_I), Lemma 11.1 puts the whole trace (I) inside one
positive-residence gap of (z) on the selected parity.  Fix one such gap
(J).  All selected traces contained in (J) are pairwise edge-disjoint,
so

\[
 \sum_{I\subseteq J}|I|\le|J|.
\]

Sum first over the residence gaps of one coordinate, then over all
coordinates.  The left side becomes
\(\sum_I|K_I||I|=\sum_Iq_I|I|\), while the right side is
\((r+1)E_h\).  The \(K'\) statement follows on the translated trace
parity.  \(\square\)

Since the height-gap theorem gives (|I|\ge h+2), and
(q_I\ge r-H), (12.2) implies

\[
 |\mathcal P_h|
 \le {r+1\over r-H}{E_h\over h+2}.
 \tag{12.3}
\]

Thus the core-enclosure ledger recovers the reciprocal-height trace bound
with asymptotic constant one.  More importantly, it identifies the exact
rigidity of a critical family.  Define, for every coordinate residence gap
(J),

\[
 \rho_J={1\over|J|}
 \sum_{I\in\mathcal P_h:I\subseteq J}|I|\le1.
 \tag{12.4}
\]

Then the slack in (12.2) is the residence-length-weighted sum of
(1-\rho_J), together with the harmless edge-normalization remainder.
Consequently, if a family asymptotically saturates (12.3), then for all but
an (o(1)) fraction of the residence-length measure seen by its inactive
cores, one has

\[
 \rho_J=1-o(1).
 \tag{12.5}
\]

In words: a counterfamily occupying a fixed positive proportion of the
critical trace capacity must occupy a fixed positive proportion of the
inactive-label residence-length measure on both translated parities.  A
family approaching the full upper constant must almost tile almost every
such enclosing gap.  Any theorem showing that the utilization factor tends
to zero for the genuinely mixed alternating sectors would give the missing
little-oh improvement over reciprocal-height capacity and hence
coefficient one.
