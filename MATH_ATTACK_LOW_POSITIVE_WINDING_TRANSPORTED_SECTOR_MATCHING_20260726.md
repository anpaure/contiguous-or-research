# Low-positive-winding transported sectors at the ST scale

Date: 2026-07-26

Method: pure mathematics only.  No computation, finite search, solver, or
external input is used.

## 0. Verdict

Put

\[
 N=2r+1,\qquad B=\operatorname {Cat}_r,
 \qquad H=\lceil A\sqrt r\rceil .
\]

This note attacks the low-positive-winding half of \((ST_A)\) starting
from Theorems 5.1--5.2 of
`MATH_ATTACK_A_CP_RAINBOW_FAN_AGGREGATE_BOUNDARY_20260725.md`.
It does **not** prove the full transported-sector matching lemma, and it
does not construct an actual PBBS saturator.  It proves the following
genuine part of the lemma and isolates the exact remaining scale.

1. If one nonempty chronological cell is selected from every member of a
   quotient-edge-disjoint family and every selected cell has lag at most

   \[
     L=o\!\left(\sqrt{r/\log(r+2)}\right),
   \]

   then the family has size

   \[
     \boxed{o(B/\sqrt r).}
   \]

   The proof charges each interval to one actual intervening PBBS edge.
   Thus this is a transported-sector matching theorem, not a marginal
   estimate.

2. For bounded winding, after the already available small-carrier and
   near-total-carrier deletions, the selected cell can be taken to have
   length \(\gamma N\), where \(\gamma>0\) depends only on the fixed
   winding and carrier cutoffs.  Consequently the only unresolved cells
   have both linear length and lag within a polylogarithmic factor of the
   Gaussian scale.  For example, with

   \[
    L_*(r)=\left\lfloor
      {\sqrt{r/\log(r+2)}\over\log\log(r+3)}
      \right\rfloor,
   \]

   the residual satisfies

   \[
     \boxed{
       |E_j\cap O_k|\ge\gamma N,
       \qquad
       L_*(r)<k-j\le H.}
   \]

3. There is an exact coarea identity for the cell lag.  If \(j_I(x)\)
   and \(k_I(x)\) are the even and odd sector indices at a transported
   coordinate \(x\), then

   \[
    k_I(x)-j_I(x)
     =\sum_{t=1}^{s-1}
       \mathbf 1_{(-C_t,Y_t]}(x).
   \]

   Hence every selected cell of length \(L_I\) and lag \(\ell_I\)
   obeys the aggregate inequality

   \[
    \boxed{
    \sum_I L_I\ell_I
      \le \sum_{D\in\mathcal D_r}\delta(D)
      ={NB-\mathscr D_r\over2}.}
   \]

   At \(L_I=\Theta(N)\) and \(\ell_I=\Theta(\sqrt r)\), this gives
   only \(O(B/\sqrt r)\), with the correct critical coefficient scale.
   Thus the first transported coarea dual lands exactly at the order
   relevant to \((ST_A)\); it cannot prove the required little-oh.

No paired-matching \(C_6\) or \(C_8\) switch is used.  Such a switch is
legal here only if each replacement edge is still a literal edge
\(D\mapsto\phi\tau^\ell D\) in the same PBBS orbit block and carries the
actual interval \(E_j\cap O_k\).  The standard paired-matching switches do
not supply this chronology and therefore do not encode transported cells.

The exact residual is a large-lag correlation problem for the canonical
block rotation.  All presently known critical
saturation models fail simultaneous orbit realizability
\(D_{i+1}=\tau D_i\).  Therefore none is an actual PBBS saturator.

## 1. The two transported partitions

Let

\[
 D_i=\tau^iD_0,
 \quad a_i=\delta(D_i),
 \quad c_i=d(D_i),
 \quad \widehat c_i=d(\phi D_i).
\]

The exact block identities are

\[
 c_i=N-a_i-\delta(\phi D_i),
 \qquad
 a_{i+1}-a_i=c_i-\widehat c_i.
\]

Put

\[
 C_i=\sum_{u<i}c_u,
 \qquad
 Y_i=a_i-C_i.
\]

For a return of step-two duration \(s\) and winding \(w\ge1\),

\[
 C_s=a_s+wN,
 \qquad
 Y_s=-wN.
\]

The two ordered sector partitions are

\[
 E_j=(-C_{j+1},-C_j],
 \qquad
 O_k=(Y_{k+1},Y_k]
 \quad(0\le j,k<s).
\]

Their common range is

\[
 J_I=(-wN,0].
\]

Theorem 5.1 of the source note gives total common mass \(wN\), at most
\(2s-1\) nonempty cells, and therefore one cell of length at least

\[
 {wN\over2s-1}\ge {N\over2H-1}.
\]

The index order is one-sided.

### Lemma 1.1 (no negative lag)

If \(E_j\cap O_k\ne\varnothing\), then \(k\ge j\).

#### Proof

If \(k<j\), monotonicity of \(Y_i\) gives

\[
 Y_{k+1}\ge Y_j=a_j-C_j>-C_j.
\]

Thus every point of \(O_k\) lies strictly to the right of \(-C_j\),
whereas every point of \(E_j\) lies at or to its left.  The intervals are
disjoint. \(\square\)

The integer

\[
 \ell=k-j\ge0
\]

is called the lag of the cell.

## 2. Literal chronology of one positive-lag cell

Write the canonical factorization at phase \(i\) as

\[
 D_i=P_i1R_i0S_i.
\]

There is a canonical Dyck word \(T_i\) satisfying

\[
 S_i1P_i=P_{i+1}1\overline T_i,
 \qquad
 \widehat c_i=|T_i|+1.
\]

Iteration in the free word monoid gives, for \(j\le k\),

\[
 (S_k1)(S_{k-1}1)\cdots(S_j1)P_j
 =P_{k+1}(1\overline T_k)(1\overline T_{k-1})
       \cdots(1\overline T_j).
\]

After translation by \(C_j+\sum_{i=j}^kc_i\), the ledger interval
\(E_j\) is exactly the coordinate interval of \(S_j1\), while \(O_k\)
is exactly the coordinate interval of \(\overline T_k1\).  Therefore a
cell is a literal overlap of these two designated blocks.  This is the
chronology used below; no independent-sector or random matching model is
substituted for it.

## 3. A genuine growing-lag matching theorem

The next theorem is the proved part of the requested transported-sector
matching lemma.

### Theorem 3.1 (sub-Gaussian-lag transported matching)

Let \(L=L(r)\) satisfy

\[
 L=o\!\left(\sqrt{r/\log(r+2)}\right).
\]

Let \(\mathcal P_L\) be a pairwise quotient-edge-disjoint family of
genuine, nonwrapping PBBS return intervals.  Equip every interval with
one nonempty chronological cell of lag at most \(L\).  Then

\[
 \boxed{|\mathcal P_L|=o(B/\sqrt r).}
\]

#### Proof

The diagonal lag has the following direct charge.  If
\(D=P1R0S\), put \(U=P1R0\).  A nonempty diagonal cell forces

\[
 \operatorname {ht}(U)=\operatorname {ht}(S).
\]

Indeed, if \(\operatorname {ht}(S)<h=\operatorname {ht}(D)\), then in
\(\tau D=S1P0R\) the first visit to height \(h\) occurs after all of
\(S\), and hence \(a_1\ge |S|+1=c_0\), which makes the diagonal cell
empty.  The number of roots split into two Dyck paths of equal height is
\(O(B/r^{3/4})\), by the standard fixed-height collision convolution.

Now take a positive lag \(\ell\le L\), translate its left phase to zero,
and let \(h\) be the invariant orbit height.  The nested first-hit
calculation for the exact word recursion gives the following alternative:

\[
 \text{there is }i\in\{0,\ldots,\ell\}
 \text{ such that }
 \operatorname {ht}(S_i)\ge h-\ell+i.
 \tag{3.1}
\]

For completeness, if all inequalities in (3.1) failed, successively
factor the canonical prefix \(P_1\) at its first visits to
\(h-1,h-2,\ldots,h-\ell\).  The literal recursion then identifies the
terminal odd carrier with the last negative excursion.  In the single
root \(D_1\), nonempty overlap with \(S_01\) forces \(S_0\) to contain
the first visit to height \(h-\ell\), contradicting the failed
\(i=0\) inequality.  Thus (3.1) is a consequence of the actual PBBS
word, not of sector lengths.

This is the nested first-hit statement proved as Theorem 5.3 in
`MATH_ATTACK_Z16_POSITIVE_COMMON_EDGE_FIXED_CORE_OBSTRUCTION_20260725.md`;
the preceding paragraph records the mechanism needed here.

Put

\[
 U_i=P_i1R_i0.
\]

Then \(D_i=U_iS_i\), both factors are Dyck, and

\[
 \operatorname {ht}(U_i)=h,
 \qquad
 0\le h-\operatorname {ht}(S_i)\le\ell-i\le L.
\]

If \(h\le\ell\), the same conclusion with height difference at most
\(L\) already holds at \(i=0\).  Choose the least valid \(i\).  The
edge indexed by \(D_i\) is an actual edge of the parent return support.
Parent edge-disjointness therefore makes all charged roots distinct,
even when their lags and witness phases differ.

It remains to count roots \(D=UV\) for which the two Dyck factors have
height difference at most \(L\).  Lemma 5.5A of the same audited note
gives the adaptive collision bound
with \(q=L+1\), is

\[
 CB\left\{
 {q+1\over\eta r}
 +r^{-1/2}e^{-c/\sqrt\eta}
 +(1+R)^2e^{-cR}
 \right\},
 \tag{3.2}
\]

where

\[
 R={r\over q^2},
 \qquad
 \eta=\sqrt{q/\sqrt r}.
\]

The hypotheses of that bound hold eventually.  Divide (3.2) by
\(B/\sqrt r\).  With \(\delta=q/\sqrt r\), its three terms are at most

\[
 C\sqrt\delta,
 \qquad
 Ce^{-c\delta^{-1/4}},
 \qquad
 C\sqrt r(1+R)^2e^{-cR}.
\]

The first two vanish because \(\delta\to0\); the last vanishes because
the assumed range gives \(R/\log(r+2)\to\infty\).  Adding the diagonal
sector proves the theorem. \(\square\)

The proof uses a single internal support charge.  In particular there is
no union loss over \(\ell\) or over the witness phase \(i\).

## 4. Reduction of low winding to a linear rare--rare cell

Theorem 5.2 of the source note gives, for every edge-disjoint positive
family,

\[
 \sum_I w(I)=O(B/\sqrt r).
\]

Hence for every \(K_r\to\infty\),

\[
 \#\{I:w(I)\ge K_r\}=o(B/\sqrt r).
\]

Thus the range \(1\le w<\eta\sqrt r\) reduces to fixed bounded winding
in the usual order of limits: first prove a little-oh theorem for every
fixed \(K\), then let \(K\to\infty\).

Fix \(K\ge2\) and \(0<\varepsilon<1/16\), and put

\[
 T=\lfloor\varepsilon N\rfloor.
\]

The exact one-deficit convolution gives

\[
 \sum_{D:d(D)\le T}d(D)\le CB\sqrt{T+1}.
\]

Therefore all intervals for which at least one parity carries at least a
quarter of its common range on deficits at most \(T\) have total size

\[
 O(\sqrt\varepsilon\,B/\sqrt r).
\]

The near-total deficits \(d(D)>N-r/[\kappa(\log r)^2]\) also give
\(o(B/\sqrt r)\), by the early-first-maximum estimate and an injective
support-edge charge.

For every remaining interval with \(1\le w<K\), more than \(wN/2\) of
the common range lies in cells for which both carrier deficits exceed
\(\varepsilon N\).  Each parity has fewer than \(K/\varepsilon\) such
carrier indices, because each full deficit ledger is less than \(KN\).
The rare--rare part of the monotone cell path therefore has fewer than
\(2K/\varepsilon\) cells.  One of them has length greater than

\[
 \boxed{\gamma N,
 \qquad \gamma={\varepsilon\over4K}.}
\]

Set

\[
 L_*(r)=\left\lfloor
 {\sqrt{r/\log(r+2)}\over\log\log(r+3)}
 \right\rfloor.
\]

This satisfies the hypothesis of Theorem 3.1.  Combining that theorem
with the preceding reduction leaves only cells satisfying

\[
 \boxed{
 \begin{gathered}
  1\le w<K,
  \qquad |E_j\cap O_k|\ge\gamma N,\\
  \varepsilon N<d(D_j),d(\phi D_k)
       \le N-{r\over\kappa(\log r)^2},\\
  L_*(r)<k-j\le H.
 \end{gathered}}
 \tag{4.1}
\]

The \(O(\sqrt\varepsilon)\) term is removed only after the residual
fixed-\((K,\varepsilon)\) theorem is proved, by sending
\(\varepsilon\downarrow0\) and then \(K\to\infty\).

## 5. Exact transported-depth coarea identity

For one interval write

\[
 e_t=-C_t,
 \qquad o_t=Y_t=e_t+a_t.
\]

Away from partition boundaries, let \(j(x)\) and \(k(x)\) be the unique
indices such that

\[
 x\in E_{j(x)}\cap O_{k(x)}.
\]

### Theorem 5.1 (transported-depth coarea)

For every \(x\in J_I=(-wN,0]\) away from endpoints,

\[
 \boxed{
 k(x)-j(x)
  =\sum_{t=1}^{s-1}\mathbf1_{(e_t,o_t]}(x).}
 \tag{5.1}
\]

Consequently

\[
 \boxed{
 \int_{J_I}(k(x)-j(x))\,dx
  =\sum_{t=1}^{s-1}|(e_t,o_t]\cap J_I|
  \le\sum_{t=1}^{s-1}a_t.}
 \tag{5.2}
\]

#### Proof

Since \((e_t)\) is strictly decreasing, if \(x\in E_j\), exactly the
indices \(1,\ldots,j\) satisfy \(e_t\ge x\).  Similarly, if
\(x\in O_k\), exactly \(1,\ldots,k\) satisfy \(o_t\ge x\).  Hence

\[
 k-j=\sum_{t=1}^{s-1}
  \bigl(\mathbf1_{\{o_t\ge x\}}-
        \mathbf1_{\{e_t\ge x\}}\bigr).
\]

Because \(o_t=e_t+a_t>e_t\), each difference is precisely the indicator
of \((e_t,o_t]\).  This proves (5.1).  Integration and
\(|(e_t,o_t]|=a_t\) prove (5.2). \(\square\)

### Corollary 5.2 (aggregate coarea dual)

Let \(\mathcal P\) be edge-disjoint, and choose a cell of length \(L_I\)
and lag \(\ell_I\) from every interval.  Then

\[
 \boxed{
 \sum_{I\in\mathcal P}L_I\ell_I
  \le {NB-\mathscr D_r\over2},
 \qquad
 \mathscr D_r=\sum_Dd(D).}
 \tag{5.3}
\]

#### Proof

The function in (5.1) equals \(\ell_I\) throughout the selected cell,
so its integral is at least \(L_I\ell_I\).  Sum (5.2) over the family.
All roots \(D_t\) in the selected supports are distinct, giving

\[
 \sum_I\sum_{t=1}^{s(I)-1}a_t
 \le\sum_{D\in\mathcal D_r}\delta(D).
\]

Finally

\[
 \delta(D)+\delta(\phi D)=N-d(D).
\]

Since \(\phi\) permutes \(\mathcal D_r\), summing gives

\[
 2\sum_D\delta(D)=NB-\mathscr D_r.
\]

This proves (5.3). \(\square\)

For the residual (4.1), if in addition
\(\ell_I\ge\lambda\sqrt r\), then (5.3) yields only

\[
 |\mathcal P|\le {1+o(1)\over2\gamma\lambda}
                  {B\over\sqrt r}.
\]

This is exactly big-oh at the critical scale.  It is not a little-oh
estimate.  The identity therefore identifies the correct obstruction:
an actual saturator whose selected lags are \(\Theta(\sqrt r)\) would use
\(\Theta(B)\) distinct PBBS roots and a positive fraction of the
uncentered first-maximum mass
\(NB/2-\Theta(B\sqrt r)\).  The known first moment permits this.  For
lags only of order \(\sqrt{r/\log r}\), (5.3) is still weaker by a
factor of order \(\sqrt{\log r}\).

## 6. Why the bridge alone does not close the estimate

The literal word identity in Section 2 turns a cell into a common
substring of a Dyck suffix \(S_j\) and a complemented Dyck word
\(\overline T_k\).  This is a bridge constraint, not a new independent
Dyck excursion.

Indeed, for every balanced word \(Z\), if

\[
 p=-\min_t\sigma_Z(t),
 \qquad q=\max_t\sigma_Z(t),
\]

then

\[
 1^pZ0^p,
 \qquad
 1^q\overline Z0^q
\]

are Dyck words.  A positive fraction of the
\(\binom{2n}{n}=\Theta(4^n/\sqrt n)\) balanced words of length \(2n\)
have \(p,q=O(\sqrt n)\).  Thus even a linear synchronized overlap retains
the diagonal bridge-renewal mode.  Counting it as a fifth independent
Catalan strip would incorrectly gain a factor of order \(r\).

This bridge family is not an actual PBBS orbit family: it does not impose
all intermediate canonical factorizations.  Its role is narrower.  It
shows that cell length, two Dyck carrier conditions, and matching on the
two endpoints do not by themselves prove a vanishing factor.

## 7. Paired-matching switch audit

Define the transported-cell bipartite graph with left vertices
\(D\in\mathcal D_r\) and right vertices \(\phi E\), where a cell of lag
\(\ell\) can join only

\[
 \boxed{D\longmapsto\phi\tau^\ell D.}
 \tag{7.1}
\]

Moreover, (7.1) is only a candidate edge: it is legal only when the two
specific ledger intervals have nonempty physical intersection inside one
enclosing genuine return.

### Lemma 7.1 (orbit-block invariance of legal switches)

Every legal transported-cell edge joins one \(\tau\)-cycle \(C\) on the
left to the single cycle \(\phi C\) on the right.  Therefore an
alternating switch which replaces transported-cell edges must preserve
each ordered orbit block \((C,\phi C)\).  Inside such a block, every new
edge must still satisfy (7.1) for its new phase difference and must carry
the corresponding literal cell intersection.

#### Proof

The map \(\phi\) commutes with \(\tau\).  Hence
\(\phi\tau^\ell D\) belongs to \(\phi C\) whenever \(D\in C\).  A
replacement edge leaving this ordered pair of cycles cannot have the
form (7.1).  Preserving the cycle pair is necessary but not sufficient,
because the PBBS return and the interval intersection are additional
conditions. \(\square\)

The ordinary paired-matching \(C_6\) and \(C_8\) switches change a
matching through local Johnson incidences.  They neither preserve the
fixed PBBS successor permutation nor supply the intervals
\((E_j,O_k)\).  Consequently they cannot be imported into this proof as
transported-sector switches.  They would become relevant only after an
explicit encoding verifies both requirements in Lemma 7.1.  No such
encoding is presently available.

## 8. Exact remaining lemma and saturator status

For every fixed \(A,K,\varepsilon>0\), let
\(\mathcal R_{A,K,\varepsilon}(r)\) be the maximum size of a genuine
edge-disjoint PBBS family satisfying (4.1).  The remaining low-positive
theorem is exactly

\[
 \boxed{
 \mathcal R_{A,K,\varepsilon}(r)=o(B/\sqrt r).}
 \tag{8.1}
\]

If (8.1) holds for every fixed \(K,\varepsilon\), then the winding and
carrier reductions, in the order

\[
 r\to\infty,
 \qquad \varepsilon\downarrow0,
 \qquad K\to\infty,
\]

prove the whole low-positive-winding half of \((ST_A)\).  Theorem 5.2
then also disposes of the complementary large winding.

An actual PBBS saturator for the failure of (8.1) would have to provide
a sequence of genuine canonical orbits with

* \(\Theta(B/\sqrt r)\) pairwise support-disjoint returns;
* bounded winding and Gaussian height/duration;
* a linear interior--interior transported cell in every return;
* cell lag larger than every proved
  \(o(\sqrt{r/\log r})\) cutoff (and at most \(A\sqrt r\)); and
* simultaneous realization of every intervening identity
  \(D_{i+1}=\tau D_i\).

No known example has these properties.  The peak-defect-one positive
returns lie on quotient cycles of period at most three and have negligible
total mass.  The complete-colour and bridge-renewal saturation models
reach \(\Theta(B/\sqrt r)\) only after dropping simultaneous orbit
realizability.  They are therefore not PBBS saturators.

The honest conclusion is

\[
 \boxed{
 \begin{array}{ll}
 \text{sub-Gaussian transported lag:}&o(B/\sqrt r)\text{ proved},\\
 \text{large mesoscopic/Gaussian lag with linear cell:}&\text{open},\\
 \text{first coarea/Hall dual:}&\text{critical-order and insufficient},\\
 \text{actual PBBS saturator:}&\text{none identified},\\
 \text{generic paired }C_6/C_8\text{ switches:}&\text{not chronology-legal}.
 \end{array}}
\]
