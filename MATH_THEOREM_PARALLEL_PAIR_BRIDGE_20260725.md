# The parallel-pair involution bridge

Date: 2026-07-25

Method: pure mathematics only.

## 0. Setup

Put

\[
 n=2m+1,
 \qquad
 \sigma=(2\ 3)(4\ 5)\cdots(2m\ \ 2m+1).
 \tag{0.1}
\]

Thus (\sigma) fixes coordinate (1) and has cycle type (1\,2^m).
Write ({\cal I}_m) for its conjugacy class.  This note separates two
questions:

1. how strongly the class ({\cal I}_m) mixes every Johnson rank, and
   how many targets one member fixes;
2. whether the displayed recursion-aligned representative has a
   fragmented or low-conductance ownership overlay on the canonical MSW
   factor.

The first question has an exact favorable answer.  The second is the
remaining gate.

## 1. Exact Johnson spectrum

On the rank-(r) slice, write

\[
 V_r=U_0\oplus U_1\oplus\cdots\oplus U_s,
 \qquad s=\min(r,n-r),
 \tag{1.1}
\]

for the multiplicity-free Johnson decomposition, where (U_j) is the
Specht module of shape ((n-j,j)).  Let

\[
 K_{\rm pp}={1\over|{\cal I}_m|}
 \sum_{\pi\in{\cal I}_m}P_\pi.
 \tag{1.2}
\]

### Theorem 1.1 (exact parallel-pair spectrum)

For every (j\le s), the eigenvalue (\rho_j) of (K_{\rm pp}) on
(U_j) is

\[
 \boxed{
 \rho_{2a+1}=0,
 \qquad
 \rho_{2a}={\binom ma\over\binom{2m+1}{2a}}.}
 \tag{1.3}
\]

In particular

\[
 \boxed{
 0\le\rho_j\le{1\over n}\quad(j\ge1),}
 \tag{1.4}
\]

with equality only at (j=2).

#### Proof

For a permutation of cycle type (1\,2^m), the fixed-subset polynomial
is

\[
 (1+x)(1+x^2)^m.
 \tag{1.5}
\]

Let (F_j) be the number of fixed (j)-sets.  Then

\[
 F_{2a}=F_{2a+1}=\binom ma.
 \tag{1.6}
\]

The permutation module on (j)-sets is

\[
 M_j=U_0\oplus\cdots\oplus U_j.
 \tag{1.7}
\]

Consequently the character of (U_j) at this conjugacy class is

\[
 \chi_j=F_j-F_{j-1}.
 \tag{1.8}
\]

All odd numerators vanish.  For (j=2a),

\[
 \chi_{2a}=\binom ma-\binom m{a-1}.
 \tag{1.9}
\]

The dimension of (U_{2a}) is

\[
 d_{2a}=\binom{2m+1}{2a}-\binom{2m+1}{2a-1}.
 \tag{1.10}
\]

The two binomial differences in (1.9)--(1.10) have the same multiplicative
factor:

\[
 \begin{aligned}
 \binom ma-\binom m{a-1}
 &=\binom ma{m-2a+1\over m-a+1},\\
 \binom{2m+1}{2a}-\binom{2m+1}{2a-1}
 &=\binom{2m+1}{2a}{m-2a+1\over m-a+1}.
 \end{aligned}
 \tag{1.11}
\]

Their ratio proves (1.3).

It remains to bound the even ratios.  Put

\[
 R_a={\binom{2m+1}{2a}\over\binom ma}.
 \tag{1.12}
\]

Then (R_1=n), and

\[
 {R_{a+1}\over R_a}
 ={2(m-a)+1\over2a+1}\ge1
 \tag{1.13}
\]

through the relevant range (2a\le m).  Hence
(\rho_{2a}=R_a^{-1}\le1/n), proving (1.4). \(\square\)

## 2. Opportunity for one common involution

Let ({\cal Z}\subseteq\binom{[n]}r), and put

\[
 h=|{\cal Z}|,\qquad N=\binom nr,
 \qquad z=\mathbf1_{\cal Z}.
 \tag{2.1}
\]

For (\pi\in{\cal I}_m), let

\[
 A_\pi({\cal Z})
 =|\{R\in{\cal Z}:\pi R\notin{\cal Z}\}|.
 \tag{2.2}
\]

### Theorem 2.1 (near-complete class mixing)

\[
 \boxed{
 \mathbb E_{\pi\in{\cal I}_m}A_\pi({\cal Z})
 \ge\left(1-{1\over n}\right){h(N-h)\over N}.}
 \tag{2.3}
\]

For arbitrary nonnegative weights (w_q), one common involution
(\pi\in{\cal I}_m) therefore satisfies

\[
 \boxed{
 \sum_qw_qA_\pi({\cal Z}_q)
 \ge\left(1-{1\over n}\right)
 \sum_qw_q{h_q(N_q-h_q)\over N_q}.}
 \tag{2.4}
\]

#### Proof

Write

\[
 z={h\over N}\mathbf1+\sum_{j\ge1}z_j,
 \qquad z_j\in U_j.
 \tag{2.5}
\]

Since every member of ({\cal I}_m) is an involution,

\[
 \mathbb E_\pi A_\pi({\cal Z})
 =h-\langle z,K_{\rm pp}z\rangle
 =\sum_{j\ge1}(1-\rho_j)\|z_j\|_2^2.
 \tag{2.6}
\]

Equation (1.4) and

\[
 \sum_{j\ge1}\|z_j\|_2^2={h(N-h)\over N}
 \tag{2.7}
\]

give (2.3).  Sum the same expectation over depths to obtain (2.4).
\(\square\)

Thus the parallel-pair conjugacy class has essentially the full
uniform-permutation opportunity, while retaining an involutive two-shore
overlay.

## 3. Fixed target fraction

Every (\pi\in{\cal I}_m) has (m) two-cycles and one singleton.
A set is fixed exactly when it is a union of these coordinate orbits.
Therefore the number of fixed rank-(r) targets is

\[
 \boxed{
 F_{m,r}=
 \begin{cases}
 \binom m{r/2},&r\text{ even},\\[1mm]
 \binom m{(r-1)/2},&r\text{ odd}.
 \end{cases}}
 \tag{3.1}
\]

Equivalently,

\[
 F_{m,r}=[x^r](1+x)(1+x^2)^m.
 \tag{3.2}
\]

### Proposition 3.1 (exponentially small central fixed family)

Fix (A<\infty).  Uniformly for

\[
 r=m-q,\qquad0\le q\le A\sqrt m,
 \tag{3.3}
\]

one has

\[
 \boxed{
 {F_{m,r}\over\binom{2m+1}r}
 =2^{-m+O_A(1)}.}
 \tag{3.4}
\]

In particular the total number of targets fixed by one parallel-pair
involution over an (O(\sqrt m)) Gaussian window is (o(W)).

#### Proof

The central-binomial estimates, uniformly for (3.3), give

\[
 \binom m{\lfloor r/2\rfloor}
 =2^{m+O_A(1)}m^{-1/2},
 \qquad
 \binom{2m+1}r
 =2^{2m+O_A(1)}m^{-1/2}.
 \tag{3.5}
\]

Their ratio is (3.4).  Multiplication by (O(\sqrt m)) still leaves an
exponentially small fraction. \(\square\)

## 4. Immediate comparison with the two extreme bridges

* A coordinate transposition has only (\Theta(1/n)) coherent crossing
  gap and fixes asymptotically half of every central rank.
* A coordinate (n)-cycle has constant coherent gap and fixes no
  nontrivial target, but its ownership overlay may be connected.
* The parallel-pair class has coherent gap at least (1-1/n), fixes only
  a (2^{-m+O_A(1)}) fraction of a central rank, and remains involutive.

Thus, at the rank-function level, the parallel-pair bridge has almost all
the advantages of the long cycle and the exact two-shore symmetry of the
transposition bridge.  Any failure must occur in the ownership-component
restitution or conductance, not in continuous Johnson mixing or in a large
fixed-target family.

## 5. Canonical MSW scope already forced by reflection symmetry

The conjugacy class alone cannot be a universal pointwise descent theorem.
There is a recursion-aligned representative

\[
 \sigma_0(i)=n-i\quad(1\le i\le2m),
 \qquad \sigma_0(n)=n,
 \tag{5.1}
\]

of the same cycle type for which the exact MSW reflection identity gives

\[
 \boxed{\sigma_0F_m^{\rm MSW}=F_m^{\rm MSW}.}
 \tag{5.2}
\]

For this representative the comparison has no noncommon rows after
cancellation, so its intrinsic cell is a singleton and every component
gain is zero, even though the class-average coherent spectrum is almost
perfect.

The displayed adjacent representative (0.1) is conjugate to (\sigma_0),
but the conjugating permutation does not preserve the canonical MSW
factor.  Therefore (5.2) neither proves nor disproves fragmentation for
(0.1).  It does prove a necessary quantifier warning:

\[
 \boxed{
 \text{one must choose the involution adaptively from its conjugacy class;}
 \text{no prescribed (1\,2^m) bridge works for every exact factor.}}
 \tag{5.3}

The exact adjacent-pair overlay is analyzed next.

## 6. The recursion-native truncated matching

The coordinate matching appearing literally in the contextual MSW
selector hierarchy is

\[
 \sigma_{\rm tr}
 =(2\ 3)(4\ 5)\cdots(2m-2\ \ 2m-1),
 \tag{6.1}
\]

which fixes the three coordinates (1,2m,2m+1).  It has cycle type
(1^3,2^{m-1}).  Omitting the last pair therefore changes neither the
central fixed-target conclusion nor the exact-load coherent spectrum in
any material way.

### Theorem 6.1 (truncated spectrum)

The conjugacy-class average of type (1^3,2^{m-1}) has Johnson
eigenvalues

\[
 \boxed{
 \rho_{2a}={\binom ma\over\binom n{2a}},
 \qquad
 \rho_{2a+1}={2a+1\over m}\rho_{2a}.}
 \tag{6.2}
\]

Consequently

\[
 0\le\rho_j\le {1\over n}\quad(2\le j\le m-1),
 \qquad \rho_1={1\over m}.
 \tag{6.3}
\]

Every centered exact cyclic-load vector has zero Johnson degrees zero and
one, so on the actual load space the coherent ceiling is still (1/n).

#### Proof

The fixed-subset polynomial is

\[
 (1+x)^3(1+x^2)^{m-1}.
 \tag{6.4}
\]

The degree-(j) two-row character numerator is the coefficient of (x^j)
in

\[
 (1-x)(1+x)^3(1+x^2)^{m-1}
 =(1+2x-2x^3-x^4)(1+x^2)^{m-1}.
 \tag{6.5}
\]

For (j=2a) and (2a+1), respectively, these coefficients are

\[
 \binom{m-1}{a}-\binom{m-1}{a-2},
 \qquad
 2\left(\binom{m-1}{a}-\binom{m-1}{a-1}\right).
 \tag{6.6}
\]

Division by
(\binom nj-\binom n{j-1}) simplifies to (6.2).  The even ratios
decrease from (\rho_2=1/n), and the displayed odd factor is below one
for (3\le2a+1\le m-1), proving (6.3).

Finally, exact cyclic loads have constant point marginals:

\[
 \sum_{S\ni x}\mu_q(S)=(m-q){W\over n}
 \tag{6.7}
\]

for every coordinate (x).  Centering therefore removes (U_0\oplus
U_1). \(\square\)

### Proposition 6.2 (truncated fixed targets remain exponentially rare)

The exact number of fixed rank-(r) targets is

\[
 \boxed{
 F^{(3)}_{m,r}
 =[x^r](1+x)^3(1+x^2)^{m-1}
 =\sum_{b=0}^3\binom3b
   \binom{m-1}{(r-b)/2},}
 \tag{6.8}
\]

where a nonintegral or out-of-range lower index contributes zero.  Uniformly
for (r=m-q), (q\le A\sqrt m),

\[
 \boxed{
 {F^{(3)}_{m,r}\over\binom nr}=2^{-m+O_A(1)}.}
 \tag{6.9}
\]

#### Proof

Equation (6.8) is immediate from (6.4).  It is a sum of at most four
binomial coefficients of order (2^m/\sqrt m) in the stated window,
whereas the rank size is of order (4^m/\sqrt m), up to constants
depending only on (A). \(\square\)

Thus the final pair involving the omitted label is not needed to destroy
the fixed-target obstruction.  The truncated matching is the more natural
candidate for preserving the contextual MSW component geometry.

## 7. What the known recursion proves--and what it does not

For

\[
 \tau_s=(2s+2\ \ 2s+3),
 \qquad0\le s\le m-2,
 \tag{7.1}
\]

the canonical MSW overlay contains the genuine sealed size-two components

\[
 \{P1100R,\ P1010R\},
 \qquad P\in{\cal D}_s,quad
 R\in{\cal D}_{m-s-2}.
 \tag{7.2}
\]

The colours (\tau_s) are exactly the disjoint coordinate pairs in
(\sigma_{\rm tr}).  Moreover, by choosing one prefix (P_s=1^s0^s)
at each boundary (2\le s\le m-H-2), one obtains a row-disjoint family
of packets over a positive-density matching of coordinate colours.  The
number of reserved owner rows is (>B/128).

This proves **sequential selector-like fragmentation**: each (\tau_s)
can be used on its reserved packets, and those packet supports remain
fresh under the previously selected packet switches.

It does not prove fragmentation of the one endpoint overlay

\[
 F_m^{\rm MSW}quad\text{versus}\quad
 \sigma_{\rm tr}F_m^{\rm MSW}.
 \tag{7.3}
\]

The reason is exact and elementary.  A packet union (U_s) in (7.2)
satisfies

\[
 \tau_sU_s=U_s,
 \tag{7.4}
\]

but the other disjoint coordinate transpositions (\tau_t), (t\ne s),
need not preserve (U_s).  Therefore

\[
 \tau_sU_s=U_s
 \quad\not\Longrightarrow\quad
 \sigma_{\rm tr}U_s=U_s.
 \tag{7.5}
\]

Consequently none of the already proved size-two packets can be promoted,
without a new common-invariance theorem, to a component of the direct
parallel-pair overlay.

There is a useful exact cut inequality.  For any family (A) of MSW rows,
put (U=U(A)).  Since the (\tau_s) commute,

\[
 \boxed{
 |U\triangle\sigma_{\rm tr}U|
 \le\sum_{s=0}^{m-2}|U\triangle\tau_sU|.}
 \tag{7.6}
\]

#### Proof

Order the transpositions arbitrarily and telescope from (U) to
(\sigma_{\rm tr}U).  Symmetric-difference distance is invariant under
coordinate relabelling, and commutativity gives

\[
 |\tau_{<s}U\triangle\tau_s\tau_{<s}U|
 =|U\triangle\tau_sU|.
 \tag{7.7}
\]

The triangle inequality proves (7.6). \(\square\)

Thus a balanced row set which is simultaneously (o(W/m))-invariant
under the individual recursion colours would give a direct
(o(W))-boundary cut for the truncated product bridge.  No such common
row set is currently supplied by the contextual component hierarchy.

Conversely, (7.6) is only an upper bound.  Large individual colour
boundaries may cancel in the endpoint product, so failure of the common
small-boundary premise would not disprove a direct low-conductance cut.

The present rigorous conclusion is therefore:

\[
 \boxed{
 \begin{gathered}
 \text{omitting the last pair preserves constant-order exact-load mixing}\
 \text{and exponentially small fixed-target mass, while retaining a}\
 \text{positive-density sequential MSW packet matching;}\\
 \text{direct endpoint fragmentation or low conductance remains unproved.}
 \end{gathered}}
 \tag{7.8}
\]

## 8. Coherent mixing versus diagonal conductance

The favorable class spectrum creates an exact tension with the near-trade
route.  Fix any row family \(A\subseteq F\), put

\[
 U=U(A),\qquad \alpha={|U|\over W}={|A|\over B}.
 \tag{8.1}
\]

For an involution \(\pi\), the diagonal boundary is

\[
 \partial_\pi(A)=|U\triangle\pi U|
 =2|U\setminus\pi U|.
 \tag{8.2}
\]

Applying Theorem 2.1 on the middle rank gives:

### Proposition 8.1 (every predetermined balanced cut is generically large)

\[
 \boxed{
 \mathbb E_{\pi\in{\cal I}_m}\partial_\pi(A)
 \ge2\left(1-{1\over n}\right)
       \alpha(1-\alpha)W.}
 \tag{8.3}
\]

In particular, if \(\alpha\) stays in a compact subinterval of \((0,1)\),
the expected normalized diagonal conductance is bounded below by a positive
constant.

The same statement holds for the truncated class on exact-load vectors;
for an arbitrary set indicator its degree-one ceiling is \(1/m\), yielding

\[
 \mathbb E\partial_\pi(A)
 \ge2\left(1-{1\over m}\right)\alpha(1-\alpha)W.
 \tag{8.4}
\]

Thus one cannot preselect a recursion cut \(A\) and expect a generic
parallel-pair relabelling to have small middle cost.  Any useful
low-conductance cut must be chosen *after* the involution, from exceptional
ownership geometry (for example, as a union of many direct overlay
components).  Near-complete coherent mixing and generic low conductance
pull in opposite directions.

## 9. Small-component facts available without an enumeration

Identify the two shores of the direct \(F/\pi F\) overlay by the source
row in \(F\).  Its components are exactly the minimal row families
\(A\subseteq F\) for which

\[
 \pi U(A)=U(A).
 \tag{9.1}
\]

This follows immediately from the diagonal-cut identity

\[
 \partial_\pi(A)=|U(A)\triangle\pi U(A)|.
 \tag{9.2}
\]

A noncommon component cannot have one row on each shore: equality of the
two middle-wreath columns determines the same unoriented cyclic order, so
the rows would already have been common and cancelled.  Hence every
noncommon component has at least two old rows, and there are at most \(B/2\)
of them.

For the truncated type \(1^3\,2^{m-1}\), even an uncancelled row cannot be
stabilized by the coordinate involution.  The automorphism group of an odd
cyclic order is dihedral; its involutive reflections have cycle type
\(1\,2^m\), never \(1^3\,2^{m-1}\).  Thus all apparent one-row packets are
excluded before any shadow calculation.

For the full type \(1\,2^m\), stabilized rows are possible, but every such
row contains a fixed middle interval.  Therefore their number is at most

\[
 F_{m,m}=2^{m+O(\log m)},
 \tag{9.3}
\]

which is \(o(B)\).  This does not bound paired common rows
\(C,\pi C\in F\): the recursion reflection (5.1) shows that an entire factor
can be common in that paired sense.

These observations rule out a positive-density supply of trivial singleton
packets, but they do not distinguish the two possibilities that matter:

\[
 \boxed{
 \begin{array}{ll}
 \text{fragmented endpoint:}&\Theta(B)\text{ components of bounded or
 moderate size};\\
 \text{mixed endpoint:}&\text{one giant component carrying }B-o(B)\text{
 rows}.
 \end{array}}
 \tag{9.4}
\]

The contextual selector theorems prove the first behavior sequentially for
the individual colours.  They do not currently decide (9.4) for either
product representative (0.1) or (6.1).

## 10. Exact path-space ledger for the commuting factorization

Write

\[
 \sigma_t=\tau_t\tau_{t-1}\cdots\tau_1,
 \qquad \sigma_0=1,
 \tag{10.1}
\]

where the \(\tau_t\) are any ordering of the disjoint pairs in
\(\sigma_{\rm tr}\).  There are two mathematically different ways to use
this factorization.

### 10.1 Transporting one common row cut

Fix \(A\subseteq F\), put \(U=U_F(A)\), and define the row multisets

\[
 P_t=(F\setminus A)\sqcup\sigma_tA.
 \tag{10.2}
\]

Only \(P_0\) is assumed exact.  Every \(P_t\) nevertheless has \(B\) rows,
and the rows in the transported subfamily \(\sigma_tA\) have pairwise
disjoint middle supports.

Put

\[
 U_t=\sigma_tU,\qquad
 E_t=U_{t-1}\triangle U_t
     =\sigma_{t-1}(U\triangle\tau_tU).
 \tag{10.3}
\]

### Theorem 10.1 (transported-cut XOR ledger)

The final middle boundary satisfies the exact identities

\[
 \boxed{
 U\triangle\sigma_TU
 =E_1\triangle E_2\triangle\cdots\triangle E_T,}
 \tag{10.4}
\]

\[
 \boxed{
 \mathbf1_{\sigma_TU}-\mathbf1_U
 =\sum_{t=1}^T
   \left(\mathbf1_{U_t}-\mathbf1_{U_{t-1}}\right).}
 \tag{10.5}
\]

Consequently

\[
 \boxed{
 2M_0(P_T)
 =\left|\,\triangle_{t=1}^TE_t\,\right|
 \le\left|\bigcup_{t=1}^TE_t\right|
 =\sum_{t=1}^T|E_t^{\rm new}|,}
 \tag{10.6}
\]

where

\[
 E_t^{\rm new}=E_t\setminus\bigcup_{s<t}E_s.
 \tag{10.7}
\]

Thus only newly encountered boundary locations can contribute to the
final middle defect; every location crossed an even number of times
cancels exactly.

#### Proof

For any three sets \(X,Y,Z\),

\[
 X\triangle Z=(X\triangle Y)\triangle(Y\triangle Z).
 \tag{10.8}
\]

Iterating along \(U_0,U_1,\ldots,U_T\) proves (10.4).  The ordinary
indicator differences telescope, proving (10.5).  The final row multiset
has middle load

\[
 \mathbf1_{\Omega\setminus U}+\mathbf1_{\sigma_TU}
 =\mathbf1_\Omega+
  \mathbf1_{\sigma_TU}-\mathbf1_U.
 \tag{10.9}
\]

Its middle holes are therefore \(U\setminus\sigma_TU\), half the symmetric
difference.  Equation (10.6) follows from (10.4), because the symmetric
difference is contained in the ordinary union and the new pieces partition
that union. \(\square\)

The usual triangle bound

\[
 2M_0(P_T)\le\sum_t|E_t|
 =\sum_t|U\triangle\tau_tU|
 \tag{10.10}
\]

forgets all reuse.  Equation (10.6) is strictly stronger whenever the same
middle locations recur.  It is the exact cancellation mechanism needed if
the individual one-pair cuts are not summable.

At depth \(q\), let \(a_q^A\) be the cyclic-interval load vector contributed
by the rows of \(A\).  The same transported calculation gives the exact
linear flag ledger

\[
 \boxed{
 \mu_q(P_T)-\mu_q(F)
 =(\sigma_T-I)a_q^A
 =\sum_{t=1}^T
   \sigma_{t-1}(\tau_t-I)a_q^A.}
 \tag{10.11}
\]

Unlike the middle identity, (10.11) does not convert hole counts into an
XOR: holes are a nonlinear threshold of the final sum.  It does show that
all rankwise reuse and cancellation must be evaluated on the **final**
histogram, not by summing nominal one-pair repairs.

### 10.2 Varying cuts and exact component switches

Now let \(F_0=F\).  At stage \(t\), choose a current row family
\(A_t\subseteq F_{t-1}\) and put

\[
 F_t=(F_{t-1}\setminus A_t)\sqcup\tau_tA_t.
 \tag{10.12}
\]

As long as the selected current rows have disjoint middle supports, write
\[
 U_t=U_{F_{t-1}}(A_t),\qquad
 d_t=\mathbf1_{\tau_tU_t}-\mathbf1_{U_t}.
 \tag{10.13}
\]

Then the final middle load is

\[
 \lambda_T=\mathbf1+\sum_{t=1}^Td_t.
 \tag{10.14}
\]

Whenever every row removal is legal, \(\lambda_T\) is a nonnegative integer
vector of total mass \(W\), and hence

\[
 \boxed{
 M_0(F_T)={1\over2}\left\|\sum_{t=1}^Td_t\right\|_1.}
 \tag{10.15}
\]

Define the exact cancellation at stage \(t\) by

\[
 {\cal C}_t={1\over2}
 \left(
 \left\|\sum_{s<t}d_s\right\|_1+\|d_t\|_1
 -\left\|\sum_{s\le t}d_s\right\|_1
 \right)\ge0.
 \tag{10.16}
\]

Then

\[
 \boxed{
 M_0(F_T)
 ={1\over2}\sum_{t=1}^T\|d_t\|_1
 -\sum_{t=1}^T{\cal C}_t.}
 \tag{10.17}
\]

This is the exact multiround middle ledger: summing cut boundaries is
sufficient, but not necessary, because opposite signed incidence updates
may cancel.

If \(A_t\) is a union of complete current ownership components, then

\[
 \tau_tU_t=U_t,\qquad d_t=0.
 \tag{10.18}
\]

Every intermediate \(F_t\) is then an exact factor, and the middle cost is
identically zero rather than merely telescoping to zero.

### Corollary 10.2 (the certified MSW packet schedule composes exactly)

The row-disjoint contextual packets reserved over the distinct colours
\[
 \tau_s=(2s+2\ \ 2s+3),
 \qquad2\le s\le m-H-2,
 \tag{10.19}
\]
may be switched in increasing \(s\), one complete current component at a
time.  Every intermediate state and the final state are exact middle
wreath factors, and

\[
 \boxed{M_0(F_t)=0\quad\text{for every }t.}
 \tag{10.20}
\]

#### Proof

The contextual packet theorem gives pairwise row-disjoint invariant middle
supports, and proves that after switches on earlier packets the current side
of every later packet remains a complete freshly recomputed
\(\tau_s\)-component.  Apply (10.18) at every microstep. \(\square\)

This answers the middle-composition question positively.  It does **not**
identify the endpoint with the global relabelled factor
\(\sigma_{\rm tr}F\): different row lineages receive different subsets of
the commuting transpositions.  The aggregate energy release currently
proved for the certified schedule is only of order \(H B=o(W)\).  To finish coefficient
one, one still needs either:

1. substantially more shadow gain from the same zero-middle-cost exact
   path; or
2. a transported common cut for which the XOR boundary in (10.6) and the
   final multidepth histogram in (10.11) are both \(o(W)\).

## 11. Exact first-shadow ceiling of the certified packet path

The zero-middle-cost packet schedule cannot secretly contain a
coefficient-scale first-shadow correction.

Let

\[
 {\cal P}
 =\{(s,R):2\le s\le m-H-2,\ 
                 R\in{\cal D}_{m-s-2}\},
 \tag{11.1}
\]

and put

\[
 K=|{\cal P}|=\sum_{r=H}^{m-4}\operatorname{Cat}_r.
 \tag{11.2}
\]

For a packet \(p=(s,R)\), orient its legal switch and let
\(d_p^{(1)}\) be its rank-\((m-1)\) histogram displacement.  The exact
four-arm cancellation is

\[
\begin{aligned}
 d_p^{(1)}={}&
 e_{K_p\cup\{\beta_s,x_p\}}
 -e_{K_p\cup\{\gamma_s,x_p\}}\\
 &-e_{K_p\cup\{\beta_s,y_p\}}
 +e_{K_p\cup\{\gamma_s,y_p\}}.
\end{aligned}
 \tag{11.3}
\]

All four displayed targets are distinct.  Hence

\[
 \boxed{\|d_p^{(1)}\|_1=4,\qquad
        \sum_Sd_p^{(1)}(S)=0.}
 \tag{11.4}
\]

### Theorem 11.1 (no hidden linear first-shadow action)

Let \(F_\varepsilon,F_{\varepsilon'}\) be any two vertices of the
row-disjoint heterogeneous packet cube.  Then

\[
 \boxed{
 \|\mu_1(F_\varepsilon)-\mu_1(F_{\varepsilon'})\|_1
 \le4\,|\{p:\varepsilon_p\ne\varepsilon'_p\}|
 \le4K,}
 \tag{11.5}
\]

and

\[
 \boxed{
 |H_1(F_\varepsilon)-H_1(F_{\varepsilon'})|
 \le2K.}
 \tag{11.6}
\]

Moreover,

\[
 \boxed{
 {K\over B}\longrightarrow {1\over192},}
 \tag{11.7}
\]

so the entire scheduled cube has first-shadow diameter at most

\[
 \boxed{
 2K=\left({1\over96}+o(1)\right)B
 =O(W/m)=o(W).}
 \tag{11.8}
\]

#### Proof

The difference of two cube vertices is

\[
 \mu_1(F_\varepsilon)-\mu_1(F_{\varepsilon'})
 =\sum_{p:\varepsilon_p\ne\varepsilon'_p}\eta_p d_p^{(1)},
 \qquad\eta_p\in\{\pm1\}.
 \tag{11.9}
\]

The triangle inequality and (11.4) prove (11.5).  Both histograms have the
same total mass \(W\).  For two nonnegative integer load vectors of equal
mass, every repaired zero consumes at least one unit of positive
difference and every newly created zero consumes at least one unit of
negative difference.  The total positive and negative differences both
equal half the \(\ell_1\)-distance.  Hence

\[
 |H(\mu)-H(\nu)|\le{1\over2}\|\mu-\nu\|_1,
 \tag{11.10}
\]

which gives (11.6).

Finally, for every fixed \(j\),

\[
 {\operatorname{Cat}_{m-j}\over\operatorname{Cat}_m}
 \longrightarrow4^{-j}.
 \tag{11.11}
\]

Successive Catalan ratios give a uniform geometric majorant in the range
\(r\ge H\), and \(H\to\infty\).  Therefore

\[
 {K\over B}
 =\sum_{t=0}^{m-H-4}
   {\operatorname{Cat}_{m-4-t}\over\operatorname{Cat}_m}
 \longrightarrow
 \sum_{t\ge0}4^{-4-t}
 ={1\over192}.
 \tag{11.12}
\]

This proves (11.7)--(11.8). \(\square\)

### Corollary 11.2 (exact scalar \(g_p\) telescoping)

Order the packet switches arbitrarily along the exact path.  At the moment
packet \(p\) is switched, let

\[
 g_p=
 \#\{\text{old holes repaired by }p\}
 -\#\{\text{old covered targets opened by }p\}.
 \tag{11.13}
\]

Then

\[
 \boxed{
 g_p\in\{-2,-1,0,1,2\},\qquad
 \sum_{p\text{ switched}}g_p
 =H_1(F_{\rm start})-H_1(F_{\rm end}).}
 \tag{11.14}
\]

Consequently

\[
 \boxed{\left|\sum_pg_p\right|\le2K=O(W/m).}
 \tag{11.15}
\]

#### Proof

The square (11.3) has two increasing and two decreasing cells, so at most
two old holes can be repaired and at most two old singleton targets can be
destroyed.  This gives the five possible integer values.  The definition
of \(g_p\) is the negative one-step hole-count increment, so summing along
the path telescopes exactly.  Apply (11.6). \(\square\)

There is no uniform sign theorem for the \(g_p\)'s.  The canonical private
face of one native transposition contains packets with \(g_p=-1\), while
the antipodal face contains the reverse \(g_p=+1\).  Cross-packet shadow
overlap can change intermediate signs, but (11.14) shows that it cannot
amplify their final total beyond \(O(W/m)\).

Thus the proved \(H B\)-scale quadratic release of the scheduled path is
necessarily carried by depths \(q\ge2\) and by collision-energy changes,
not by an unrecorded \(\Omega(W)\) first-shadow repair.  A coefficient-one
argument still needs a new \(q=1\) mechanism outside this fixed packet
cube.

### Corollary 11.3 (the complete fixed contextual atlas is also \(q=1\)-small)

Across all native boundaries \(0\le s\le m-2\), the number of contextual
size-two packet occurrences is

\[
 \sum_{s=0}^{m-2}
 \operatorname{Cat}_s\operatorname{Cat}_{m-s-2}
 =\operatorname{Cat}_{m-1}.
 \tag{11.16}
\]

Therefore any formal sum which uses each fixed canonical contextual packet
at most once has total rank-\((m-1)\) action incidence at most

\[
 4\operatorname{Cat}_{m-1}
 =(1+o(1))B=O(W/m),
 \tag{11.17}
\]

and can change the number of first-shadow holes by at most

\[
 2\operatorname{Cat}_{m-1}
 =\left({1\over2}+o(1)\right)B=o(W).
 \tag{11.18}
\]

The packet occurrences for different \(s\) overlap in owner rows, so
(11.16) is not itself one legal simultaneous cube.  The conclusion is only
an action ceiling: even if all those fixed charts could be made compatible,
one use of each would still be first-shadow negligible.  Linear first-shadow
repair needs repeated creation of genuinely new packet charts, components
whose \(q=1\) action grows with their size, or a different global bridge.
