# RP_A at the Dyck quotient: reduced-period fibre elimination and the exact Pascal fan

Date: 2026-07-25

Method: pure mathematics only. No web search, finite search, solver, or
computation is used.

## 0. Verdict

Put

\[
 N=2r+1,\qquad B_r=\operatorname{Cat}_r,\qquad \tau=\phi^2
\]

for the normalized PBBS quotient on semilength-\(r\) Dyck roots. This note
proves two structural results about a zero-winding quotient interval of
step-two length at most \(H\).

First, short periods remain negligible even after one complete inverse
peak-deletion fibre is restored. If \(\partial\) is simultaneous peak
deletion and

\[
 \mathcal S_{r,H}^{(1)}
 =\{D\in\mathcal D_r:\operatorname{per}_\tau(\partial D)\le H\},
\]

then, whenever \(H\log r=o(r)\),

\[
 \boxed{
 |\mathcal S_{r,H}^{(1)}|
 \le \exp\!\left[-\left(
       \log {4\over\varphi^2}-o(1)\right)r\right]B_r,}
 \qquad
 \varphi={1+\sqrt5\over2}.
\]

In particular this is \(o(B_r/N)\) for
\(H=\lceil A\sqrt r\rceil\). Thus, after deleting a negligible number of
outer starts at the exact quotient packing scale, every first-pruned trace
of length at most \(H\) is nonwrapping. This is stronger than merely
deleting short parent quotient cycles.

Second, a genuine zero-winding return has an exact triangular descendant
structure. If its gap is

\[
 g=2h+1,\qquad h=\operatorname{ht}(D),
\]

and \(D^{(j)}=\partial^jD\), then, until the first path core, level \(j\)
contains the \(j+1\) exact consecutive returns

\[
 \boxed{
 I_{j,a}=[\,2a,\ g-2(j-a)\,],\qquad 0\le a\le j,}
\]

all of common gap \(g-2j\). The labels of these returns are consecutive
equality particles. Consequently the inverse expansion from level \(j\)
to level \(j-1\), when pulled back to one fixed phase, has at least \(j\)
distinct free child-slot variables fixed to prescribed nonnegative values.
For a fixed pruning-rank profile \((r_i)\), this gives the following exact
zero-value worst-case envelope for the profile-capacity factor:

\[
 \boxed{
 Q_k(\mathbf r)
 =\prod_{j=1}^k
   {\binom{r_{j-1}+r_{j+1}-j}{2r_j-j}
    \over
    \binom{r_{j-1}+r_{j+1}}{2r_j}}
 =\prod_{j=1}^k\prod_{i=0}^{j-1}
   {2r_j-i\over r_{j-1}+r_{j+1}-i}.}
\]

This is a real multilevel strengthening of the known one-slot Pascal
factor. It is also quantitatively critical. On the formal harmonic profile
\(r_j=R/(j+1)\), the large-\(R\), fixed-\(k\) limit is

\[
 \prod_{j=1}^k
 \left({j(j+2)\over(j+1)^2}\right)^j
 ={(k+2)^k\over(k+1)^{k+1}}
 \sim {e\over k}.
\]

The raw interval ledger contributes only another factor of order \(1/h\).
At \(h\asymp\sqrt r\), the two factors are therefore of the critical order
\(1/r\), not \(o(1/r)\). A further dynamic or aggregate gain is required
for \(\mathrm{RP}_A\).

There is also an exact obstruction to replacing this missing gain by a
period argument. The gap-seven family has

\[
 R_7(r)=2^{r-1}-r
\]

starts, and all but \(\exp(o(r))\) of them lie on \(\tau\)-cycles of period
greater than \(A\sqrt r\). A greedy selection gives
\(\Omega(2^r)\) edge-disjoint constant-gap intervals on long cycles. This
is globally negligible because \(2^r=o(B_r/N)\), but it disproves every
claim that a short zero-winding interval must come from a short quotient
period.

No proof or disproof of \(\mathrm{RP}_A\) follows. The precise surviving
class consists of long-period, nonwrapping Pascal fans in the Gaussian
rank tube. The remaining theorem must improve the critical harmonic
\(1/h\) fan-capacity factor by \(o(1)\), or prove additional clustering of
their length-\(h\) intervals.

## 1. Exact Dyck normalization and the orbit-sum identity

For a Dyck word \(D\in\mathcal D_r\), mark the first up-step which reaches
the global maximum and the first following return to height zero. Write

\[
 D=P1R0S.
\]

Put

\[
 \delta(D)=|P|+1,\qquad d(D)=|S|+1.
\]

The one- and two-step quotient maps are

\[
 \phi D=\overline R1\overline S0\overline P,
 \qquad
 \tau D=S1P0R.
\]

If \(E_j=\phi^jD\) and \(a_j=\delta(E_j)\), then the block lengths give

\[
 \boxed{d(E_j)=N-a_j-a_{j+1}.}                    \tag{1.1}
\]

Indeed, in the displayed factorization of \(E_j\), the three positive
quantities \(|P|+1\), \(|R|+1\), and \(|S|+1\) sum to \(N\), and the
first two are \(a_j,a_{j+1}\).

### Lemma 1.1 (exact orbit-sum form of zero winding)

A return after \(s\) step-two moves and one final odd move has zero winding
if and only if

\[
 \boxed{\sum_{j=0}^{2s}a_j=sN.}                  \tag{1.2}
\]

#### Proof

The even-time skew product changes the spatial root by \(-d\), and the
final odd move changes it by \(\delta(\tau^sD)=a_{2s}\). Zero winding is
therefore the integer equality

\[
 \sum_{q=0}^{s-1}d(E_{2q})=a_{2s}.
\]

Substitution of (1.1) gives

\[
 sN-\sum_{j=0}^{2s-1}a_j=a_{2s},
\]

which is (1.2). Every step is reversible. \(\square\)

The identity is exact but not by itself rare: it places a local orbit sum
at its natural central scale. The structural gain below comes from peak
deletion and endpoint anchoring.

## 2. Voltage-itinerary rigidity

### Lemma 2.1 (quotient cycles of bounded period)

At semilength \(d\), put \(N_d=2d+1\). The number of quotient states on
\(\phi\)-cycles of period at most \(Q\) is at most

\[
 \boxed{QN_d^Q.}                                  \tag{2.1}
\]

Consequently the number of states on \(\tau\)-cycles of period at most
\(H\) is at most

\[
 \boxed{2H N_d^{2H}.}                            \tag{2.2}
\]

#### Proof

Let \(D_0,\ldots,D_{q-1}\) be a quotient \(\phi\)-cycle and put
\(v_i=\delta(D_i)\). Normalize the first omitted physical label to zero.
The ordered cyclic voltage word determines the entire periodically
continued omitted-label word by

\[
 \lambda_0=0,\qquad
 \lambda_{t+1}=\lambda_t+v_{t\bmod q}\pmod{N_d}.
\]

Every ground coordinate occurs as an omitted coordinate in a lifted PBBS
component. At an edge omitting coordinate \(x\), that coordinate is absent
from both incident factor states. Until the next \(x\)-edge its membership
alternates at each transition. Consecutive \(x\)-gaps are odd, so the two
endpoint prescriptions agree. Applying this to every coordinate
reconstructs every factor state and hence \(D_0\). Thus an ordered
length-\(q\) voltage word determines at most one rooted quotient state.
There are fewer than \(N_d^q\) such words, and summing over \(q\le Q\)
proves (2.1).

If a \(\tau=\phi^2\) orbit has period \(p\), its containing \(\phi\)-orbit
has period \(p\) or \(2p\). Equation (2.2) follows from (2.1) with
\(Q=2H\). \(\square\)

## 3. One inverse fibre cannot amplify a short reduced period

Let \(\partial D\) be obtained by deleting every peak simultaneously. If

\[
 E=\partial D\in\mathcal D_d,\qquad k(E)=\operatorname{pk}(E),
\]

then the exact inverse-fibre size is

\[
 \boxed{
 F_r(E)=|\partial^{-1}(E)|
 =\binom{r+d-k(E)}{2d}.}                          \tag{3.1}
\]

For the empty core put \(F_r(\varnothing)=1\). The formula follows by
attaching one mandatory new leaf to each old leaf and distributing the
remaining new leaves among the \(2d+1\) ordered child slots.

### Lemma 3.1 (uniform Fibonacci cap on one inverse fibre)

For every core \(E\) of every rank \(0\le d<r\),

\[
 \boxed{F_r(E)\le F_{2r+1}<\varphi^{2r+1},}       \tag{3.2}
\]

where \(F_n\) is the Fibonacci sequence with \(F_0=0,F_1=1\).

#### Proof

For \(d>0\), (3.1) gives

\[
 F_r(E)\le\binom{r+d}{2d}.
\]

The tiling formula for Fibonacci numbers is

\[
 F_{2r+1}
 =\sum_{q=0}^r\binom{2r-q}{q}
 =\sum_{d=0}^r\binom{r+d}{2d},                    \tag{3.3}
\]

where the second equality uses \(d=r-q\). Every summand is nonnegative, so
each individual fibre is at most the sum. Binet's formula gives
\(F_n<\varphi^n\). \(\square\)

### Theorem 3.2 (first-pruned short-period fibre elimination)

Let \(H=H(r)\ge1\) satisfy \(H\log r=o(r)\). Then

\[
 \boxed{
 |\mathcal S_{r,H}^{(1)}|
 \le 1+2Hr(2r+1)^{2H}F_{2r+1}.}                  \tag{3.4}
\]

If

\[
 c_*:=\log {4\over\varphi^2}>0,
\]

then for every fixed \(0<c<c_*\), and all sufficiently large \(r\),

\[
 \boxed{
 |\mathcal S_{r,H}^{(1)}|
 \le e^{-cr}B_r.}                                \tag{3.5}
\]

#### Proof

At a fixed reduced rank \(d\ge1\), Lemma 2.1 gives at most

\[
 2H(2d+1)^{2H}
\]

cores of \(\tau\)-period at most \(H\). Each has at most \(F_{2r+1}\)
outer preimages by Lemma 3.1. Sum over \(1\le d<r\), bound
\(2d+1\le2r+1\), and add the unique empty-core preimage. This proves
(3.4).

The elementary Catalan lower bound

\[
 B_r={1\over r+1}\binom{2r}{r}
 \ge {4^r\over(r+1)(2r+1)}                       \tag{3.6}
\]

follows because the central binomial coefficient is the largest of the
\(2r+1\) coefficients of order \(2r\). Equations (3.2), (3.4), and
(3.6) yield

\[
 \log {|\mathcal S_{r,H}^{(1)}|\over B_r}
 \le
 -r\log {4\over\varphi^2}
 +2H\log(2r+1)+O(\log r).
\]

The last two terms are \(o(r)\), proving (3.5). \(\square\)

### Corollary 3.3 (first-pruned wrapping is negligible)

Fix \(A>0\) and put \(H=\lceil A\sqrt r\rceil\). Let \(\mathcal P\) be
any pairwise parent-quotient-edge-disjoint family of intervals of
step-two length at most \(H\). The number of intervals in \(\mathcal P\)
whose first-pruned trace makes a complete wrap around its reduced
\(\tau\)-cycle is

\[
 \boxed{o_A(B_r/N).}                              \tag{3.7}
\]

#### Proof

Peak deletion commutes with \(\tau\):

\[
 \partial\tau D=\tau\partial D.
\]

If a projected trace of length \(s\le H\) wraps its reduced cycle, that
cycle has period at most \(s\le H\). Its parent start therefore lies in
\(\mathcal S_{r,H}^{(1)}\). Distinct intervals in \(\mathcal P\) have
distinct parent starting edges. Theorem 3.2 bounds their number by
\(e^{-cr}B_r=o(B_r/N)\). \(\square\)

The corollary does not say that the parent interval itself lies on a short
cycle. The parent cycle can be long because the reduced short cycle may
act nontrivially on its inverse slot vector. This is exactly the
amplification excluded by (3.4).

## 4. Long quotient period does not exclude a short return

The exact gap-seven classification gives the cores

\[
 E_d=(10)^{d-2}1100,\qquad d\ge2,
\]

and the exact number of rank-\(r\) starts

\[
 \boxed{
 R_7(r)=\sum_{d\ge2}\binom r{2d-1}
 =2^{r-1}-r.}                                     \tag{4.1}
\]

Each such return has a quotient trace contained in five consecutive
step-two edges.

### Theorem 4.1 (long-period gap-seven obstruction)

Let \(H=H(r)\ge5\) with \(H\log r=o(r)\). At least

\[
 \boxed{
 2^{r-1}-r-2H(2r+1)^{2H}}                        \tag{4.2}
\]

gap-seven starts lie on \(\tau\)-cycles of period greater than \(H\).
They contain a pairwise quotient-edge-disjoint family of size at least

\[
 \boxed{
 {1\over9}\left(
 2^{r-1}-r-2H(2r+1)^{2H}
 \right).}                                        \tag{4.3}
\]

For \(H=\lceil A\sqrt r\rceil\), this is
\((1/18-o(1))2^r\), while still being \(o(B_r/N)\).

#### Proof

Lemma 2.1 bounds the total number of rank-\(r\) states on \(\tau\)-cycles
of period at most \(H\) by \(2H(2r+1)^{2H}\). Subtract this from (4.1)
to prove (4.2).

On a cycle of length greater than \(H\ge5\), a five-edge interval can
intersect only intervals whose starts lie at one of the four preceding,
its own, or the four following edge positions. Greedy selection therefore
retains at least one ninth of any set of starts, proving (4.3).

Finally, \(2^r=o(B_r/N)\) follows from
\(B_r/N=\Theta(4^r/r^{5/2})\). \(\square\)

Thus neither a bounded-period theorem nor the stronger first-pruned
period theorem can classify all short returns. Period eliminates an
amplification mechanism; it does not supply the required aggregate
Catalan saving.

## 5. The exact Pascal fan under repeated pruning

We use three established integral facts.

1. A genuine zero-winding return is an equality case of the height-gap
   theorem. If its step-two duration is \(h\), then

   \[
    h=\operatorname{ht}(D),\qquad
    g=2h+1,\qquad d(D)=1.                         \tag{5.1}
   \]

2. Simultaneous peak deletion lowers the height of a nonempty plane tree
   by exactly one, and PBBS preserves height along each quotient orbit.

3. If a consecutive return \([L,R]\) has gap below the current
   circumference, then in the once-pruned equality-particle PBBS it has a
   leader child beginning at \(L\), and a last immediate-predecessor child
   ending at \(R\). Both child gaps are odd and at most \(R-L-2\).

For completeness, the first assertion follows from the strict
first-passage variable. If

\[
 D_j=\tau^jD=P_j1R_j0S_j,\quad
 C_j=\sum_{q<j}d(D_q),\quad
 Y_j=\delta(D_j)-C_j,
\]

then

\[
 Y_{j+1}-Y_j=-d(\phi D_j)<0.
\]

At a zero-winding hit \(Y_h=0\), the literal recursion

\[
 P_h=S_{h-1}1S_{h-2}1\cdots S_1\,1\,S_0
\]

shows that \(P_h\) ends at height \(h-1\), so the endpoint root has height
\(h\). Height invariance gives (5.1), and the first-maximum condition
forces \(S_0=\varnothing\).

Put

\[
 D^{(j)}=\partial^jD,\qquad r_j={1\over2}|D^{(j)}|,
\]

and define the first path-core level

\[
 \ell=\min\{j:r_j=h-j\}.                           \tag{5.2}
\]

Rank is at least height, so \(\ell\) exists by level \(h\).

### Theorem 5.1 (tight-return Pascal fan)

Let \(D\) start a genuine zero-winding return with gap
\(g=2h+1<N\). For every

\[
 0\le j\le\ell,\qquad 0\le a\le j,
\]

the level-\(j\) PBBS contains the consecutive return

\[
 \boxed{
 I_{j,a}=[\,2a,\ g-2(j-a)\,].}                    \tag{5.3}
\]

Every interval in level \(j\) has exact gap

\[
 \boxed{g-2j=2(h-j)+1.}                           \tag{5.4}
\]

Moreover \(\ell\le h-1\), and

\[
 \boxed{D^{(\ell)}=1^{h-\ell}0^{h-\ell}.}        \tag{5.5}
\]

#### Proof

At level zero, (5.3) is the original return. Suppose the fan has been
constructed at level \(j<\ell\). Then

\[
 r_j>h-j,
\]

so the common parent gap \(2(h-j)+1\) is strictly below the level-\(j\)
circumference \(2r_j+1\). Apply the two-child return lemma to
\(I_{j,a}=[L,R]\). The leader child begins at \(L\), the last predecessor
child ends at \(R\), and both gaps are at most

\[
 2(h-j)+1-2=2(h-j-1)+1.                           \tag{5.6}
\]

Every level-\((j+1)\) root on the relevant orbit has height \(h-j-1\).
The height-gap theorem gives the reverse inequality in (5.6). Hence the
two children are exactly

\[
 [L,R-2]=I_{j+1,a},\qquad
 [L+2,R]=I_{j+1,a+1}.                             \tag{5.7}
\]

Interior children obtained from adjacent parents have the same endpoints;
a return interval determines its omitted coordinate at its endpoints, so
the two copies are the same labelled occurrence. This completes the
induction.

At level \(\ell\), rank equals height, so the plane tree is the unique path
of that rank, proving (5.5). If \(\ell=h\), then level \(h-1\) would have
rank greater than one and (5.3) would give a gap-three return below its
circumference. To see the contradiction directly, the unique height-one
rank-\(q\) word is \((10)^q\). It is \(\tau\)-fixed, with
\(d=2q-1=N_q-2\) and \(\delta=1\). Its displacement through one even move
and the following odd move is \(3\pmod {N_q}\), nonzero when \(q>1\).
Thus it has no gap-three return below its circumference. Hence
\(\ell\le h-1\). \(\square\)

The stopping mountain is itself \(\tau\)-fixed. Indeed, for
\(M_q=1^q0^q\), the canonical blocks are
\(P=1^{q-1}\), \(R=0^{q-1}\), \(S=\varnothing\), and hence

\[
 \tau M_q=1P0R=M_q.                               \tag{5.5a}
\]

Thus every genuine zero-winding start eventually projects to a
period-one core. Theorem 3.2 shows that this cannot happen after only one
pruning round at significant mass. The unresolved amplification occurs
over a growing tower of as many as \(\Theta(\sqrt r)\) rounds; the
fan-capacity ledger in Section 6 is the exact additional information
available along that tower.

### Corollary 5.2 (unit-sector middle core)

For every \(1\le k\le\ell\),

\[
 \boxed{
 d(\tau^aD^{(k)})=1
 \qquad(0\le a<k).}                               \tag{5.8}
\]

Consequently, with \(k=\lceil h/2\rceil\), every zero-winding start has
one of the following two forms.

* If \(\ell\le k\), a mountain core of rank
  \(h-\ell\ge\lfloor h/2\rfloor\) appears within \(k\) pruning rounds.

* If \(\ell>k\), put \(s=h-k\). The level-\(k\) return has gap
  \(2s+1<2r_k+1\), and

  \[
   d(D^{(k)}),d(\tau D^{(k)}),\ldots,
   d(\tau^{s-1}D^{(k)})=1.                        \tag{5.9}
  \]

  Hence

  \[
   \delta(\tau^sD^{(k)})=s,                       \tag{5.10}
  \]

  and the endpoint contour begins with \(1^s\).

#### Proof

Consider the level-\((k-1)\) fan interval beginning at time \(2a\).
Its leader equality particle is selected at time \(2a\). By (5.7), its
immediate predecessor starts the exact right child at time \(2a+2\).
Let \(\Delta\) be their spacing at time \(2a\). The two-child lemma says
that the predecessor supplies \(\Delta\) return intervals in the parent
window. Since its last such interval begins already at \(2a+2\), the
inequality \(\Delta>1\) would force another predecessor selection at
\(2a+1\). This would repeat the same omitted coordinate at consecutive
one-step times, a gap-one return, which is impossible. Hence \(\Delta=1\).
The even-time skew displacement from time \(2a\) to time \(2a+2\) is
therefore \(-1\). Since \(1\le d<2r_k+1\), the deficit is literally one.
This proves (5.8).

If \(\ell>k\), then \(s=h-k\le k\), so (5.8) covers every
deficit-carrying phase of the level-\(k\) return. Its cumulative deficit is
\(s\). The return is below the level-\(k\) circumference, so the return
congruence is the integer equality (5.10). A height-\(s\) Dyck word whose
first maximum is reached at step \(s\) must begin with \(s\) up-steps.
\(\square\)

The corollary is conditional on a genuine zero-winding start. The converse
statement \(d(D)=1\Rightarrow\) zero winding is false; see Section 8.

## 6. Distinct forced slots and the profile-capacity product

### Lemma 6.1 (consecutive fan labels)

At level \(j\), label the return \(I_{j,a}\) by its omitted equality
particle \(\alpha_{j,a}\). Then

\[
 \boxed{
 \alpha_{j,a+1}=\alpha_{j,a}-1
 \quad(0\le a<j),}                                \tag{6.1}
\]

with particle labels read in cyclic order.

#### Proof

The right child of \(I_{j-1,a}\) is labelled by the immediate predecessor
of its leader. By (5.7), it has the same endpoints as the left child of
\(I_{j-1,a+1}\). There is only one omitted coordinate at a fixed endpoint,
so these two labelled return occurrences coincide. Induction in \(a\)
gives (6.1). \(\square\)

### Theorem 6.2 (multislot inverse-fibre capacity)

Let \(D\) be as in Theorem 5.1 and let

\[
 1\le k\le\min(\ell,\lfloor h/2\rfloor).
\]

At inverse level \(j\), \(1\le j\le k\), the fan supplies \(j\) distinct
phase-local free child slots of occupancy zero. After transporting every
condition back to a single fixed phase of the inverse fibre, it fixes
\(j\) distinct free child-slot variables to prescribed nonnegative
integer values.

Fix a realizable rank profile

\[
 r_0,r_1,\ldots,r_{k+1}.
\]

For a fixed level-\(k\) bottom core, the number of compatible outer inverse
towers is at most the product of the unrestricted conditional fibre
capacities multiplied by

\[
 \boxed{
 Q_k(\mathbf r)
 =\prod_{j=1}^k
 {\binom{r_{j-1}+r_{j+1}-j}{2r_j-j}
  \over
  \binom{r_{j-1}+r_{j+1}}{2r_j}}.}                \tag{6.2}
\]

Equivalently,

\[
 \boxed{
 Q_k(\mathbf r)
 =\prod_{j=1}^k\prod_{i=0}^{j-1}
 {2r_j-i\over r_{j-1}+r_{j+1}-i}.}                \tag{6.3}
\]

#### Proof

The inverse expansion from \(D^{(j)}\) to \(D^{(j-1)}\) is a weak
composition of

\[
 y_j=r_{j-1}-2r_j+r_{j+1}                         \tag{6.4}
\]

free leaves into the \(2r_j+1\) ordered child slots of the core. The full
fibre therefore has size

\[
 \binom{y_j+2r_j}{2r_j}
 =\binom{r_{j-1}+r_{j+1}}{2r_j}.                  \tag{6.5}
\]

The \(j\) fan intervals at level \(j-1\) begin at the phases
\(0,1,\ldots,j-1\) of the step-two core orbit. For each such interval, the
exact right child starts two one-step updates later. In the proof of the
two-child lemma this says that the leader and its immediate predecessor
have spacing one: if their spacing were greater than one, the predecessor
would have an additional selection in the sole intermediate time and
would then repeat at consecutive times. The exact terminal-slot spacing
formula

\[
 \Delta=2z+1
\]

therefore forces the corresponding free inverse-slot variable \(z\) to
zero.

By Lemma 6.1, these are the consecutive labelled particle gaps

\[
 (\alpha,\alpha-1),
 (\alpha-1,\alpha-2),\ldots,
 (\alpha-j+1,\alpha-j).
\]

They are distinct. Indeed, for \(j\le k\le h/2\),

\[
 2r_j+1\ge2(h-j)+1>j.
\]

Equality-particle transport preserves the cyclic labels, but it need not
preserve the numerical gap. Write the initial labelled gap in the form

\[
 \Delta_i(0)=1+\varepsilon_i+2z_i,
\]

where \(z_i\) is its free weak-composition coordinate and the fixed
\(\varepsilon_i\) records the mandatory-core contribution. If \(n_i(t)\)
is the number of selections of particle \(i\) before time \(t\), then

\[
 \Delta_i(t)=\Delta_i(0)+n_i(t)-n_{i-1}(t).        \tag{6.6a}
\]

The selection counts and \(\varepsilon_i\) are determined by the reduced
core orbit, independently of the outer inverse occupancies. Thus a
phase-local equation \(\Delta_i(t)=1\) fixes \(z_i\) to one prescribed
integer. Actual existence of the outer fan guarantees that this integer is
nonnegative. Distinct gap labels fix distinct initial variables; no
assertion that all prescribed initial values are zero is needed.

If the prescribed values have total \(w\ge0\), deleting those boxes leaves
free mass \(y_j-w\). The number of possible vectors is therefore at most
its value at \(w=0\), namely

\[
 \binom{y_j+2r_j-j}{2r_j-j}
 =\binom{r_{j-1}+r_{j+1}-j}{2r_j-j}.              \tag{6.6}
\]

This is an upper bound because further dynamic fan constraints may remain.
Condition successively on the core already chosen at level \(j\). The
ratio (6.6)/(6.5) is uniform in that core once the rank triple is fixed,
so the conditional bounds multiply down the tower. This proves (6.2), and
cancellation of factorials gives (6.3). \(\square\)

### Proposition 6.3 (the harmonic worst-case envelope is critical)

For the formal harmonic rank profile

\[
 r_j={R\over j+1},
\]

the one-slot ratio at level \(j\) is

\[
 q_j={2r_j\over r_{j-1}+r_{j+1}}
 ={j(j+2)\over(j+1)^2}.
\]

For every fixed \(k\), along integer realizations with \(R\to\infty\), the
zero-value envelope in (6.3) satisfies

\[
 Q_k(\mathbf r)\longrightarrow
 \prod_{j=1}^kq_j^j
 ={(k+2)^k\over(k+1)^{k+1}}
 \sim {e\over k}.                                 \tag{6.7}
\]

#### Proof

For fixed \(j\), every \(i<j\) is negligible compared with the ranks as
\(R\to\infty\), so the level-\(j\) product in (6.3) tends to \(q_j^j\).
The telescoping identity is

\[
 \begin{aligned}
 \prod_{j=1}^k
 \left({j(j+2)\over(j+1)^2}\right)^j
 &=\prod_{j=1}^k
   \left({j\over j+1}\right)^j
   \left({j+2\over j+1}\right)^j\\
 &={(k+2)^k\over(k+1)^{k+1}}.
 \end{aligned}
\]

Finally,

\[
 \left(1+{1\over k+1}\right)^k\to e,
\]

which gives the asymptotic. Fixed finite harmonic rank strings have
integer plane-tree realizations after taking \(R\) divisible by the
required denominators. \(\square\)

This proposition is a no-go for a pointwise profile argument which expects
the triangular slot conditions alone to give \(o(1/k)\) uniformly. It is
not a counterexample to an aggregate theorem: the Catalan weight of rank
profiles, dynamic admissibility of the fan, and interval clustering could
still produce an additional vanishing factor.

## 7. Companion period/sector-mass theorem

The separately audited report
MATH_ATTACK_RPA_PERIODIC_SECTOR_MASS_NOGO_20260725.md proves two further
facts which compose with the results above.

1. The entire peak-defect-one sector is a rotation action on weak
   three-compositions. Its zero-winding returns occur only at step-two
   time two, and its exact quotient packing is \(r-2\) for \(r\ge3\).

2. If \(\mathcal Z_r(H,T)\) is the set of zero-winding pairs \((D,s)\)
   with \(1\le s\le H\) and

   \[
    \sum_{j<s}d(\tau^jD)=\delta(\tau^sD)\le T,
   \]

   then absolute constants \(c,C>0\) give

   \[
    |\mathcal Z_r(H,T)|
    \le CHT r^2 4^r
       \exp\!\left(-c\sqrt{r/T}\right).            \tag{7.1}
   \]

   Hence, for \(H\le r\) and
   \(T=o(r/\log^2r)\), this is \(o(B_r/N)\).

Choose arbitrary cutoffs

\[
 P_r=o(r/\log r),\qquad T_r=o(r/\log^2r).
\]

Together with Theorem 3.2, every possible obstruction to \(\mathrm{RP}_A\)
must therefore have all of the following properties after an
\(o(B_r/N)\) deletion:

\[
 \begin{gathered}
 \operatorname{per}_\tau(D)>P_r,\\
 \operatorname{per}_\tau(\partial D)>H,\\
 \sum_{j<s}d(\tau^jD)>T_r,
 \end{gathered}                                    \tag{7.2}
\]

and it carries the Pascal fan of Theorem 5.1. These conditions do not yet
force a contradiction.

## 8. Adversarial audit and exact implication boundary

### 8.1 The false primitive converse is excluded

It is true that every zero-winding start has \(d(D)=1\). The converse is
false. The exact counterexample is

\[
 D_0=1110011000,
\]

of semilength five and height three. Its quotient orbit is

\[
 \begin{aligned}
 D_1&=1110001100,\\
 D_2&=1100111000,\\
 D_3&=D_0,
 \end{aligned}
\]

with

\[
 (d(D_0),d(D_1),d(D_2))=(1,5,1),
 \qquad \delta(D_3)=3.
\]

Thus

\[
 1+5+1=7\ne3\pmod{11}.
\]

Any sector-shift proof claiming that the first deepest spine remains fixed
under \(\tau\) overlooks an off-spine forest which can be transported to
positive depth and become the first deepest forest. Theorems 5.1 and 6.2
start from a genuine zero-winding return and do not use this false
converse.

### 8.2 Quantifier audit

* The period bounds use \(H\log r=o(r)\). Fixed
  \(H=\lceil A\sqrt r\rceil\) satisfies this.

* Corollary 3.3 concerns wrapping of the first-pruned trace, not merely
  a short parent quotient cycle.

* The fan induction is legal only while
  \(r_j>h-j\), equivalently while its gap is strictly below the current
  circumference. The stopping core is exactly a mountain.

* The distinct-slot theorem is stated only for
  \(j\le h/2\), which guarantees that the consecutive particle gaps have
  not wrapped around the reduced particle circle.

* Equation (6.2) is a fibre-capacity upper bound. It does not assert that
  every weak composition satisfying the displayed prescribed-coordinate
  conditions realizes the required PBBS fan.

* The harmonic calculation is a fixed-\(k\), large-rank limiting profile
  and a sharp pointwise obstruction. It is not an asymptotic construction
  of Catalan many dynamically admissible zero-winding roots.

### 8.3 Exact remaining lemma

Let \(h\asymp\sqrt r\), and split genuine zero-winding starts by their
pruning-rank profiles and first mountain depth. A theorem proving
\(\mathrm{RP}_A\) by this route must supply at least one of the following.

1. An aggregate fan-capacity estimate which improves the harmonic
   profile factor in (6.2) from \(O(1/h)\) to \(o(1/h)\) after summing with
   exact Catalan/Pascal weights.

2. A clustering theorem showing that the edge-disjoint packing of
   height-\(h\) fans is \(o(1/h)\) of their already fan-weighted start
   mass.

3. A joint forward/dual dynamic code contributing an additional
   \(\omega(1)\) bits beyond the exact one-staircase deficit
   \(\log_2(h+1)\) and the raw interval factor \(h\).

Without one of these, the current ledger is exactly critical:

\[
 {1\over h}\times{1\over h}
 =\Theta(1/r),
\]

whereas the quotient form of \(\mathrm{RP}_A\) requires
\(o(B_r/N)\), and \(N=2r+1\); a fixed constant multiple of \(B_r/r\)
does not suffice.
