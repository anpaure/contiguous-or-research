# Truncated-\(Q\) rotor compilation of the multi-swap cube

Date: 2026-07-25

Method: pure mathematics only. No computation, search, solver, or web
input is used.

## 0. Verdict

Let

$$
M=m+H,\qquad
Q=o(H),\qquad H=o(m),\qquad \frac{Q^2}{M}\longrightarrow\infty,
\tag{0.1}
$$

and put

$$
L=\left\lfloor\frac{M}{Q}\right\rfloor.
\tag{0.2}
$$

Thus \(L=o(Q)\), \(LQ=(1+o(1))M\), and

$$
L^2=(1+o(1))\frac{M^2}{Q^2}=o(M).
\tag{0.3}
$$

Replacing the full radius-\(H\) state by the genuine radius-\(Q\)
carrier rotor changes the earlier conclusion, but it does not make the
entire static cube literal at coefficient one.

1. A code-separated vertex of the full \(L\times L\) independent port
   cube needs

   $$
   N\ge(4-o(1))M
   \tag{0.4}
   $$

   rotor-state occurrences whenever the total radius-\(Q\) initialization
   toll is \(o(M)\). This is a cache-restitution obstruction, not the old
   full-\(H\) queue obstruction.
2. A large cut-space subcube does compile literally. It has
   \(2L-1\) independent signs and \(L^2\) support-disjoint constituent
   rectangles. Every cut-space vertex is a union of \(O(1)\) truncated
   rotor paths, has \(M+O(Q)\) state occurrences, exact fixed middle-owner
   incidence, and \(O(Q)=o(M)\) initialization/fragmentation toll.
3. More generally, for every \(b=o(L)\), a fixed partition of the
   \(L\) port columns into \(b\) consecutive signature runs gives an
   exact affine \(Lb\)-bit rank-rectangle cube with literal length
   \(M+O(L+Qb)=M+o(M)\). Its full heat bath has exact variance
   \(2L^2=o(M)\).
4. A separate common-endpoint rotor braid compiles an entire
   \(\Theta(M^2/Q^2)\)-bit path cube on one length-\(M\) rotor path.
   Its bits are coherent one-edge sweeps through all \(2Q+1\) hard rows,
   not rank-isolated rectangles. A one-bit heat bath has variance one in
   every row and \(2Q+1\) in total, but contraction only
   \(\Theta(Q^2/M^2)\).
5. Fresh uniform resampling of the cut-space vertex is an exact
   mean-reversion kernel toward the cut-space barycenter. In the direct
   sum of all hard rows,

   $$
   \mathbb E\|Z\|_2^2=2L^2=o(M).
   \tag{0.5}
   $$

   After choosing one carrier among \(P\) carriers uniformly, its exact
   drift rate is \(1/P\).
6. These kernels mean-revert only their installed affine projections and
   toward its own barycenter. No theorem here proves that this barycenter
   is the globally balanced row vector or that the cut spaces span an
   arbitrary residual.
7. Stacking \(G\asymp Q^2/M\) disjoint batches restores
   \(\Theta(M)\) local directions, but then simultaneous unit-rate
   resampling has variance \(\Theta(M)\). Resampling one batch retains
   variance \(o(M)\) but loses the required mean-reversion rate by the
   factor \(G\).

Thus truncation produces a genuine bounded-total-variance literal kernel
on a nontrivial \(o(M)\)-capacity subspace. It does not by itself furnish
the coefficient-scale low-variance kernel.

## 1. The exact truncated carrier rotor

Fix a carrier \(U\), \(|U|=M\). A radius-\(Q\) quotient state is

$$
\omega=(K;z_1,\ldots,z_{2Q};R),
\tag{1.1}
$$

where

$$
|K|=m-Q,\qquad |R|=H-Q,
$$

and \(K,\{z_1\},\ldots,\{z_{2Q}\},R\) partition \(U\).
For \(x\in K\) and \(y\in R\), the exact induced rotor successor is

$$
\mathcal R_{x,y}(\omega)
=
(K-x+y;\ x,z_1,\ldots,z_{2Q-1};\ R-y+z_{2Q}).
\tag{1.2}
$$

The middle owner and its hard flags are

$$
X(\omega)=K+z_1+\cdots+z_Q,
\tag{1.3}
$$

$$
X^-_q(\omega)=K+z_1+\cdots+z_{Q-q},
\qquad
X^+_q(\omega)=K+z_1+\cdots+z_{Q+q}.
\tag{1.4}
$$

The deletion queue, written from its owner-exit end, is

$$
A(\omega)=(z_Q,z_{Q-1},\ldots,z_1).
\tag{1.5}
$$

The upper ordered cache is \((z_{Q+1},\ldots,z_{2Q})\). A label leaving
the deletion queue must traverse that entire upper cache before entering
\(R\). It can then be chosen into \(K\), chosen again into \(z_1\), and
shifted back through the deletion queue.

Every fixed cyclic order on \(U\) gives a directed trajectory of (1.2).
Consequently every cyclic phase interval used below is a literal
radius-\(Q\) rotor path. A path with \(s\) state endpoints compiles to a
word of length

$$
s+2Q+1.
\tag{1.6}
$$

## 2. Exact cache-restitution lower bound

Consider \(p\) disjoint marked label pairs. Suppose that at each marked
endpoint all their labels lie among the first \(R_0\) positions of the
deletion queue (1.5). The orientation signature is the vector in
\(\{0,1\}^p\) recording the order inside every pair.

### Lemma 2.1 (pair restitution)

Let two marked endpoint states on one rotor path have orientation
signatures at Hamming distance \(h>0\). If their rotor distance is \(d\),
then

$$
\boxed{
d\ge 2Q-R_0+2+h.}
\tag{2.1}
$$

#### Proof

The relative order of two labels in the ordered \(z\)-string is preserved
until at least one of them leaves that string. For every reversed marked
pair, choose one label which leaves and later re-enters. The chosen labels
are distinct because the marked pairs are disjoint.

Suppose a chosen label leaves the deletion queue through \(z_Q\) at
transition \(e\). It then needs \(Q\) shifts to traverse the upper cache
and enter \(R\). It needs one further transition to be chosen from \(R\)
into \(K\), another to be chosen from \(K\) into \(z_1\), and at least
\(Q-R_0\) further shifts to return to the first \(R_0\) deletion
positions. Hence

$$
e\le d-(2Q-R_0+2).
$$

Only one label leaves \(z_Q\) in one transition. The \(h\) chosen labels
therefore require \(h\) distinct exit transitions before that deadline,
which proves (2.1). \(\square\)

This proof already permits arbitrary choices of \(x\in K\) and \(y\in R\)
at every intervening rotor step. It uses the full hidden freedom of both
unordered reservoirs.

### Corollary 2.2 (many marked states)

Suppose \(k\) marked states, with pairwise signature distance at least
\(\delta\), are distributed among \(F\) rotor paths using \(N\) state
occurrences in total. Then

$$
\boxed{
N\ge F+(k-F)(2Q-R_0+2+\delta).}
\tag{2.2}
$$

#### Proof

Consecutive marked states on one path have the separation in Lemma 2.1.
A path containing \(s\ge1\) marked states therefore contains at least

$$
1+(s-1)(2Q-R_0+2+\delta)
$$

states. Sum over the \(F\) paths. \(\square\)

The minimum-distance form has the following sharper variation version.
If the marked signatures are ordered as
\(\sigma_{f,1},\ldots,\sigma_{f,k_f}\) along path \(f\), define

$$
\begin{aligned}
V_0
&=\#\{(f,r):\sigma_{f,r}\ne\sigma_{f,r+1}\},\\
\operatorname{TV}_H
&=
\sum_{\substack{f,r\\\sigma_{f,r}\ne\sigma_{f,r+1}}}
d_H(\sigma_{f,r},\sigma_{f,r+1}).
\end{aligned}
$$

Summing Lemma 2.1 without replacing the individual Hamming distances by
a minimum gives

$$
\boxed{
N\ge
F+(2Q-R_0+2)V_0+\operatorname{TV}_H.}
\tag{2.3}
$$

Thus rotor compilation is governed by two independent ledgers: one full
cache-restitution collar for every actual signature change, and one unit
of throughput for every reversed marked pair. This is the exact
bounded-variation form of the chronology obstruction.

## 3. A worst vertex of the full static cube

Use the square port cube with \(p=t=L\):

$$
a_i=4L+2i,\qquad
s_j=2j,\qquad
b_j=m+2j-1,
\qquad 0\le i,j<L.
\tag{3.1}
$$

The \(i\)-th row swap is at positions \(a_i,a_i+1\); the \(j\)-th
column swap is at positions \(b_j,b_j+1\). At port \(s_j\), define the
two positive states

$$
\mathcal F_j(x)
=
\{S_{s_j}(\alpha_x\pi),
  S_{s_j}(\alpha_{\bar x}\beta\pi)\},
\tag{3.2}
$$

where \(\alpha_x\) applies the row swaps selected by
\(x\in\{0,1\}^L\), \(\bar x=\mathbf1-x\), and \(\beta\) is the product
of all column swaps.

Toggling bit \(x_i\) at port \(j\) changes exactly one elementary
rectangle at lower depth

$$
q_{ij}=4L+2i-2j+1,
\tag{3.3}
$$

and no other central rank. Since

$$
2L+3\le q_{ij}\le6L-1\le Q
\tag{3.4}
$$

for large \(m\), these are genuine hard-window cells. Their supports are
pairwise disjoint. The middle-owner pair at port \(j\) is independent of
\(x\).

At every port, all marked row pairs lie in the first

$$
R_0=6L=o(Q)
\tag{3.5}
$$

deletion positions.

Choose \(L\) column signatures

$$
x^0,\bar x^0,\ldots,x^{L-1},\bar x^{L-1}
\tag{3.6}
$$

whose mutual Hamming distances are

$$
\delta=\left(\frac12-o(1)\right)L.
\tag{3.7}
$$

Such a family exists by the probabilistic method: choose \(L\) independent
fair words, include their complements, and apply a Chernoff bound and a
union bound over \(O(L^2)\) pairs.

### Theorem 3.1 (truncated-radius full-cube obstruction)

Any radius-\(Q\) rotor realization containing the \(2L\) marked states
specified by (3.6), using \(N\) states and \(F\) rotor paths, satisfies

$$
N\ge
F+(2L-F)
\left(2Q-6L+2+\left(\frac12-o(1)\right)L\right).
\tag{3.8}
$$

If its total initialization toll is \(o(M)\), then

$$
FQ=o(M),
\qquad\text{hence}\qquad F=o(L),
\tag{3.9}
$$

and therefore

$$
\boxed{N\ge(4-o(1))M.}
\tag{3.10}
$$

#### Proof

Equation (3.8) is Corollary 2.2 with \(k=2L\), (3.5), and (3.7).
Every rotor path initialization costs \(2Q+1\) extra word entries, so
an \(o(M)\) initialization ledger gives (3.9). Finally,

$$
LQ=(1+o(1))M,\qquad L=o(Q),
$$

and substitution in (3.8) proves (3.10). \(\square\)

Thus merely replacing \(H\) by \(Q\) does not compile a positive-rate
set of arbitrary static cube vertices. The upper cache and both hidden
reservoirs supply the restitution delay which the deletion-queue-only
bound misses.

### Corollary 3.2 (rectangular coefficient-scale no-go)

More generally, take \(p\) row bits and \(t\) ports in the rectangular
static construction, with

$$
pt\ge M,\qquad R_0=4t+2p\le Q.
$$

Choose the \(2t\) marked signatures to have minimum distance
\((1/2-o(1))p\). If the initialization toll is \(o(M)\), then
\(F=o(t)\), and Corollary 2.2 gives

$$
\begin{aligned}
N
&\ge(2-o(1))t\left(2Q-R_0+\frac p2\right)\\
&\ge(2-o(1))t\left(Q+\frac p2\right)\\
&\ge(5-o(1))pt
\ge(5-o(1))M.
\end{aligned}
\tag{3.11}
$$

The penultimate inequality uses \(p\le Q/2\), which follows from
\(R_0\le Q\). Thus optimizing the rectangular aspect ratio does not
remove the cache-restitution obstruction.

## 3A. A one-path rotor braid with trail directions

The static rectangle cube is too rigid, but the truncated rotor does
support a different full bit cube on one literal path.

Put \(n=2Q\), and choose

$$
\ell=
\left\lfloor
\frac{\sqrt{Q^2+2(M-1)}-Q}{2}
\right\rfloor.
\tag{RB.0}
$$

Then

$$
\ell(2Q+2\ell)\le M-1.
\tag{RB.1}
$$

We may take

$$
\ell=\left(\frac12-o(1)\right)\frac{M}{Q}.
\tag{RB.2}
$$

Starting from one common quotient state

$$
\omega=(K;z_1,\ldots,z_n;R),
$$

choose \(2\ell\) program labels in \(K\), grouped into disjoint pairs
\(\{a_i,b_i\}\), \(1\le i\le\ell\). During the next \(2\ell\) rotor
steps, insert the two labels of pair \(i\) consecutively, in order
\(a_i,b_i\) or \(b_i,a_i\) according to a bit \(\varepsilon_i\). At
these programming steps choose the same \(y\)-labels from \(R\) for every
bit vector.

After the programming steps, the unordered sets \(K,R\) are independent
of \(\varepsilon\), and the ordered \(z\)-strings differ only by the
orientations of \(\ell\) adjacent pairs among their first \(2\ell\)
positions. Continue for \(n=2Q\) steps with common choices of \(x\).
At any flush time at most one programmed adjacent pair straddles the
\(z_n/R\) boundary. Hence the \(R\)-sets of all variants differ, if at
all, only in which mate of that one pair they contain. Their intersection
has size at least \(|R|-1\), so a common \(y\) exists. All program labels
eventually leave the ordered string. Their unordered set in \(R\) is
independent of their exit order, and every variant coalesces to exactly
the same final quotient state.

The required common choices exist because

$$
m-Q\gg Q,\qquad H-Q\gg Q.
$$

Thus one block of \(2Q+2\ell\) transitions has common endpoints and
\(\ell\) independent program bits. Concatenate \(\ell\) such blocks and
fill the unused suffix by common rotor steps. Equation (RB.1) gives one
length-\(M\) rotor path for every matrix

$$
E\in\{0,1\}^{\ell\times\ell},
$$

with only one radius-\(Q\) initialization.

### Theorem 3A.1 (literal braid cube)

The preceding construction injects a
\(K_{\rm br}=\ell^2\)-bit Boolean cube into literal radius-\(Q\) rotor
paths, where

$$
K_{\rm br}
=\left(\frac14-o(1)\right)\frac{M^2}{Q^2}.
\tag{RB.3}
$$

Flipping one program bit changes one state flag successively at every
hard rank. Its path-load direction \(\eta\) satisfies

$$
\boxed{
\|\eta\|_2^2=2(2Q+1).}
\tag{RB.4}
$$

At each individual hard rank, \(\eta\) is one Johnson edge and has
squared norm two.

#### Proof

After the first label of a programmed pair is inserted, the two variants
differ only in the bottom prefix \(K\): adding the inserted singleton
makes the next prefix equal. After the second insertion, the variants
differ by one adjacent transposition in the \(z\)-string. Under every
common rotor step that adjacent transposition shifts one slot to the
right.

A prefix chain notices an adjacent transposition at exactly the one rank
whose boundary cuts the pair. Consequently the differing flag moves once
through the ranks

$$
m-Q,m-Q+1,\ldots,m+Q.
$$

When the first program label exits \(z_n\), only the top hard prefix
differs; after the second exits, the quotient states coalesce. Thus there
is exactly one two-target Johnson edge at every one of the \(2Q+1\)
hard ranks, proving (RB.4).

For several program pairs, a prefix boundary cuts at most one of the
disjoint adjacent pairs. The marked state after every programming stage
recovers all bits in that block, and common block endpoints make choices
in different blocks independent. This proves injectivity in literal path
space. \(\square\)

This is a complete one-path compilation, but it is not a compilation of
the static rank-isolated rectangles. A trail changes every hard row,
including the middle row, and generally has nonzero point margin in each
row.

Fix all other bits and let \(Y_0,Y_1\) be the two path loads obtained
from one braid bit. Fairly resampling that bit gives

$$
\mathbb E(Y'-Y\mid Y_\varepsilon,\text{ other bits})
=-\left(Y_\varepsilon-\frac{Y_0+Y_1}{2}\right),
\tag{RB.5}
$$

and

$$
\boxed{
\mathbb E\|Y'-Y\|_2^2=2Q+1.}
\tag{RB.6}
$$

The expected squared increment in each fixed row is exactly one. Thus the
braid supplies literal bounded-row-variance primitive exchanges. If one
braid coordinate is selected uniformly, each coordinate is updated only
at rate \(1/K_{\rm br}\).

The path-load map is not asserted to be affine: the cores of the Johnson
edges in one trail may depend on the other program bits, and trails from
different coordinates may interact after target labels are forgotten.
Accordingly, fresh full-cube resampling need not satisfy a global linear
mean-reversion identity and can have variance as large as order
\(K_{\rm br}Q=M^2/Q\gg M\). The exact claims are the literal path cube,
the one-bit trail formula, and the pair-local heat identities
(RB.5)--(RB.6).

## 3B. Exact bounded-run compilation of static rectangles

There is also a direct literal compilation of a much larger affine subset
of the original static rectangle cube.

Return to the square port construction (3.1)--(3.4), with \(p=t=L\).
The marked ports are the even phases

$$
s_j=2j,\qquad 0\le j<L,
$$

and their phase hull is

$$
J=\{0,1,\ldots,2L-2\}.
$$

Fix a partition of the \(L\) columns into \(b\) nonempty consecutive
runs. Assign one signature \(x^{(r)}\in\{0,1\}^L\) to each run.
Over the phase interval belonging to run \(r\), use the two fixed cyclic
order tracks

$$
\alpha_{x^{(r)}}\pi,
\qquad
\alpha_{\overline{x^{(r)}}}\beta\pi.
\tag{BR.1}
$$

Assign each odd phase at a run boundary to either adjacent run, and use
one base cyclic track on the complementary phase interval
\(\mathbb Z_M-J\).

### Theorem 3B.1 (bounded-run static cube)

For every fixed \(b\)-run partition, the construction above is an exact
affine \(Lb\)-bit subcube of the static rank-rectangle cube. It has

$$
N=M+2L-1
\tag{BR.2}
$$

state occurrences, \(2b+1\) radius-\(Q\) rotor-path pieces, and literal
word length

$$
\boxed{
M+2L-1+(2b+1)(2Q+1).}
\tag{BR.3}
$$

In particular,

$$
b=o(L)
\quad\Longrightarrow\quad
\text{literal length }M+o(M).
\tag{BR.4}
$$

All vertices have the same exact middle-owner incidence. Freshly and
independently resampling the \(Lb\) run bits gives exact mean reversion
toward the fixed-partition barycenter and

$$
\boxed{
\mathbb E\|Z\|_2^2=2L^2=o(M).}
\tag{BR.5}
$$

#### Proof

Every phase outside \(J\) uses the same base state. Every phase in \(J\)
uses two states, which gives (BR.2). Each run contributes two fixed cyclic
segments, and the complement contributes one, proving the component
count and (BR.3) by the truncated initialization formula (1.6).

At an even phase \(2j\), the right boundary of every lower flag is the
column cut \(b_j\). Toggling row bit \(i\) therefore gives exactly the
static elementary rectangle \(\rho_{ij}\) and no other central effect.
At an odd phase, no hard interval has both a row-swap cut and a
column-swap cut as its boundaries. A prefix notices at most one moved
pair, and the unordered two-track contribution in (BR.1) is independent
of the run signature. Thus every nonport contribution is a common
baseline, and the choice-dependent incidence consists precisely of the
static port rectangles.

For a fixed row \(i\) and run \(r\), toggling its run bit changes the
support-disjoint rectangles \(\rho_{ij}\) over all columns \(j\) in that
run. These \(Lb\) block directions have disjoint cell supports, so the
load map is affine and has dimension \(Lb\). The same argument at rank
\(m\) proves fixed middle incidence.

Under a fresh fair heat bath, each of the \(L^2\) constituent cells
changes diagonal with probability \(1/2\). Every cell rectangle has
squared norm four and the cell supports are disjoint. This proves the
exact drift to the partition barycenter and (BR.5). Finally,

$$
L=o(M),\qquad Qb=o(QL),\qquad QL=(1+o(1))M,
$$

so \(Qb=o(M)\) when \(b=o(L)\), proving (BR.4). \(\square\)

For example, \(b=\lfloor L/\log L\rfloor\) gives

$$
\frac{L^2}{\log L}
$$

independent rank-isolated directions with \(o(M)\) literal overhead.
This is much larger than the cut-space dimension \(2L-1\), although it
still has zero entropy rate inside the full \(L^2\)-bit cube.

Indeed the number of column sequences with at most \(b\) maximal
constant-signature runs is at most

$$
2^L
\sum_{r=1}^{b}
\binom{L-1}{r-1}(2^L-1)^{r-1}.
\tag{BR.6}
$$

Its base-two logarithm is \(O(Lb+b\log L)=o(L^2)\) when \(b=o(L)\).
Conversely a positive-entropy run family needs \(b=\Omega(L)\), for
which the initialization term \(Qb\) is \(\Omega(QL)=\Omega(M)\).
This is the sharp bounded-variation boundary for this fixed-track
compiler.

## 4. A literal cut-space subcube

The obstruction in Section 3 is not an obstruction to every large
subfamily. We now construct one which keeps the two strand signatures
fixed and varies only which side of the strand cut carries each swap.

Choose disjoint row-swap cuts

$$
c_i=6i,\qquad 0\le i<L,
$$

and column-swap cuts

$$
d_j=m+\lfloor Q/2\rfloor+6j,\qquad 0\le j<L.
\tag{4.1}
$$

For large \(m\), \(48L\le Q\). Hence every cross separation is

$$
d_j-c_i=m+q_{ij},
\qquad
\frac Q4\le q_{ij}\le\frac{3Q}{4}.
\tag{4.2}
$$

Let \(\sigma_i,\tau_j\) be these swaps and put

$$
\Gamma=\prod_i\sigma_i\prod_j\tau_j.
$$

For

$$
\chi=(r_0,\ldots,r_{L-1},s_0,\ldots,s_{L-1})
\in\{0,1\}^{2L},
$$

let

$$
\Delta_\chi
=\prod_i\sigma_i^{r_i}\prod_j\tau_j^{s_j}.
\tag{4.3}
$$

Let \(O\) contain every hard-window affected start of every one of the
\(2L\) swaps. The four affected-start clusters have total size

$$
|O|\le4Q+24L+O(1)=(4+o(1))Q.
\tag{4.4}
$$

Choose phase sets \(A,B\), each a union of \(O(1)\) cyclic intervals,
such that

$$
A\cup B=\mathbb Z_M,\qquad A\cap B=O.
\tag{4.5}
$$

Define

$$
\mathcal D_\chi
=
\Delta_\chi\pi|_A
\sqcup
\Gamma\Delta_\chi\pi|_B.
\tag{4.6}
$$

### Theorem 4.1 (literal cut-space compilation)

Every \(\mathcal D_\chi\) is a positive union of \(O(1)\)
radius-\(Q\) rotor paths. It has

$$
M+O(Q)
\tag{4.7}
$$

state occurrences and total initialization/fragmentation toll \(O(Q)\).
All \(\mathcal D_\chi\) have the same exact middle-owner incidence vector.

There are pairwise support-disjoint elementary rectangles
\(\rho_{ij}\), one at each hard rank \(m+q_{ij}\), such that

$$
I_{\rm hard}(\mathcal D_\chi)-I_{\rm hard}(\mathcal D_0)
=
\sum_{\substack{0\le i,j<L\\ r_i\oplus s_j=1}}
\rho_{ij}.
\tag{4.8}
$$

Thus the selectable cell patterns are exactly the cuts of
\(K_{L,L}\). They have \(2L-1\) independent signs and may contain
\(\Theta(L^2)\) cells.

#### Proof

At a phase outside \(O\), no hard-window interval notices any swap, so
the local contribution of (4.6) is independent of \(\chi\). At a phase
in \(O\), both tracks occur, and their local pair is

$$
\{\Delta_\chi\pi,\Gamma\Delta_\chi\pi\}.
$$

A positional interval notices at most its two boundary swap pairs.
If it notices zero or one, the unordered pair of outcomes is independent
of \(\chi\). If its boundaries are the row cut \(c_i\) and column cut
\(d_j\), the pair uses the even diagonal when \(r_i=s_j\) and the odd
diagonal when \(r_i\ne s_j\). Their difference is exactly
\(\rho_{ij}\). No two row cuts and no two column cuts have a hard-window
separation, so there are no other hard cells. This proves (4.8).

Endpoint-block parity, as in the ordinary adjacent-swap square, shows
that the supports of different \(\rho_{ij}\) are disjoint.
No exceptional length is \(m\), proving exact middle-owner equality.

Each fixed cyclic-order phase interval is a directed trajectory of the
truncated rotor (1.2). The bounded number of phase components therefore
gives \(O(1)\) literal rotor paths. Equations (4.4)--(4.7) and the
initialization cost (1.6) prove the two ledgers. \(\square\)

The configurations for \(\chi\) and \(1-\chi\) have the same hard cell
pattern, so the incidence family has exactly \(2^{2L-1}\) cut patterns.
This is exponentially large in \(L=M/Q\), but has zero entropy rate
relative to the full \(L^2\)-bit cube.

## 5. Exact mean reversion on the cut space

Write

$$
u_i=(-1)^{r_i},\qquad v_j=(-1)^{s_j}.
$$

After fixing the sign of each \(\rho_{ij}\), Theorem 4.1 can be written

$$
X(u,v)
=
\overline X+\frac12\sum_{i,j}u_iv_j\rho_{ij},
\tag{5.1}
$$

where \(\overline X\) is the uniform cut-space barycenter.

Choose \(u',v'\) independently and uniformly from
\(\{\pm1\}^L\), and replace \(X(u,v)\) by \(X(u',v')\).

### Theorem 5.1 (cut-space heat bath)

For every current cut-space vertex,

$$
\boxed{
\mathbb E(X'-X\mid X)=-(X-\overline X),}
\tag{5.2}
$$

and

$$
\boxed{
\mathbb E\|X'-X\|_2^2=2L^2=o(M).}
\tag{5.3}
$$

At each individual hard rank, the expected squared increment is at most
\(2L=O(M/Q)=o(M)\).

#### Proof

For every cell,

$$
\mathbb E(u'_iv'_j)=0,
$$

which proves (5.2). Also \(u'_iv'_j\) differs from the fixed sign
\(u_iv_j\) with probability \(1/2\). When it differs, its contribution
to \(X'-X\) is one full elementary rectangle \(\rho_{ij}\), whose squared
norm is four. Distinct cell supports are orthogonal. Therefore every one
of the \(L^2\) cells contributes expected squared norm two, proving
(5.3). At a fixed separation \(j-i\), at most \(L\) cells occur, which
gives the rowwise statement. \(\square\)

Now suppose \(P\) carriers each carry one installed cut-space deployment.
Let \(h\) be their total hard-row load and let

$$
\overline h_{\rm cut}=\sum_{U=1}^{P}\overline X_U.
$$

Choose one carrier uniformly and apply its heat bath. Then

$$
\boxed{
\mathbb E(Z\mid h)
=-\frac1P(h-\overline h_{\rm cut}),}
\tag{5.4}
$$

and

$$
\mathbb E\|Z\|_2^2\le2L^2=o(M).
\tag{5.5}
$$

Thus this is an exact simultaneous low-total-variance mean-reversion
kernel on the installed cut-space model, with rate \(1/P\).

The center in (5.4) is \(\overline h_{\rm cut}\), not automatically the
balanced scalar row vector. Relative to a desired balanced vector
\(\overline h\), the exact bias is

$$
e=\frac1P(\overline h_{\rm cut}-\overline h).
\tag{5.6}
$$

No bound sufficient for the global coefficient-one theorem is proved for
(5.6).

### Corollary 5.2 (exact conditional coefficient-one transfer)

Let \(P=N_H=(1+o(1))W/M\), and install one literal cut-space gadget in
every carrier, allowing different carriers to place their \(O(L)\)-depth
cell bands at different hard depths. Let \(b\) be the desired balanced
direct-sum hard-row vector. If

$$
\boxed{
\|\overline h_{\rm cut}-b\|_2^2=o(W),}
\tag{5.7}
$$

then dependent heat descent on the finite product of cut-space vertices
produces a literal configuration with total hard-row factorial energy
\(o(W)\).

More precisely, the exact drift/variance parameters are

$$
\kappa=\frac1P,\qquad
C_m=2L^2,\qquad
e=\frac1P(\overline h_{\rm cut}-b),
$$

so the terminal energy bound is

$$
\boxed{
\Psi_{\rm hard}
\le
PL^2+\frac12\|\overline h_{\rm cut}-b\|_2^2
=o(W).}
\tag{5.8}
$$

Indeed

$$
PL^2
=(1+o(1))W\frac{M}{Q^2}
=o(W).
$$

The literal gadget overhead over all carriers is

$$
O(QP)=O(WQ/M)=o(W).
$$

Thus (5.7), including the fixed middle and nonvariable row components,
is the exact missing barycenter theorem for this truncated cut-space
route.

## 6. Why the kernel does not yet have coefficient-scale capacity

One cut-space batch has

$$
K=L^2=(1+o(1))\frac{M^2}{Q^2}=o(M)
\tag{6.1}
$$

support-disjoint cells per carrier. Across
\(P\asymp W/M\) carriers, its total cell capacity is

$$
PK\asymp W\frac{M}{Q^2}=o(W).
\tag{6.2}
$$

This is potentially useful as a final \(o(W)\)-scale absorber, but it
cannot absorb a \(\Theta(W)\) residual.

The bounded-run compiler exhibits the same tradeoff without any
chronological loss. Its proof works for \(p\) row bits and \(t\) port
columns. Taking

$$
p=\lfloor Q/4\rfloor,\qquad
t=\left\lceil M/p\right\rceil,\qquad b=1
$$

gives \(pt=(1+o(1))M\) constituent cells on \(O(1)\) literal rotor
pieces with \(M+o(M)\) word length. Nevertheless its fresh heat bath has

$$
\mathbb E\|Z\|_2^2=2pt=(2+o(1))M.
\tag{6.2a}
$$

Thus low rotor variation does not imply low heat variance. The square
choice \(p=t=L=M/Q\) has variance \(2L^2=o(M)\) precisely because its
adjustable cell capacity is only \(L^2=o(M)\).

To restore \(\Theta(M)\) cell capacity per carrier, one needs

$$
G\asymp\frac{M}{L^2}\asymp\frac{Q^2}{M}
\tag{6.3}
$$

disjoint batches.

* Resampling all \(G\) batches gives rate \(1/P\), but variance

  $$
  2GL^2=\Theta(M),
  $$

  which is not \(o(M)\).
* Resampling one uniformly chosen batch retains variance \(2L^2=o(M)\),
  but a fixed cell is mean-reverted only at rate \(1/(PG)\), a factor
  \(G\) below the required \(1/P\).

This is the exact local fluctuation--dissipation barrier. More generally,
if \(K\) support-disjoint elementary rectangle bits are mean-reverted
toward fair means at coefficient rate \(\alpha\), then

$$
\boxed{
\mathbb E\|Z\|_2^2=2\alpha K.}
\tag{6.4}
$$

Indeed each bit changes with probability \(\alpha/2\), and each changed
rectangle has squared norm four.

Consequently any single-carrier kernel with \(K=\Theta(M)\) and
\(\alpha=\Theta(1)\) has variance \(\Theta(M)\), regardless of whether
its vertices are chronologically compilable. A coefficient-scale
low-variance theorem must either:

1. use negative covariance between different carriers so their rectangle
   increments cancel;
2. prove that an upstream construction leaves only an
   \(O(WM/Q^2)=o(W)\) residual lying in the installed cut spaces; or
3. construct a nonlocal kernel whose drift is not coordinatewise local
   cube mean reversion.

## 7. Proved boundary

The truncated-radius analysis gives the following exact division.

### Proved

1. The cache-restitution distance (2.1), including the upper cache and
   both hidden reservoirs.
2. The \((4-o(1))M\) worst-vertex lower bound for the full square port
   cube at \(L\asymp M/Q\).
3. A one-path common-endpoint rotor braid with
   \(\Theta(M^2/Q^2)\) independent trail bits and exact one-bit
   row variance.
4. For every \(b=o(L)\), an exact affine \(Lb\)-bit bounded-run
   rectangle cube with literal length \(M+o(M)\) and heat variance
   \(2L^2=o(M)\).
5. A literal \(K_{L,L}\) cut-space family with \(M+O(Q)\) states,
   \(O(Q)\) initialization toll, fixed middle incidence, and
   \(L^2\) constituent cells.
6. Exact cut-space mean reversion at rate one and variance
   \(2L^2=o(M)\).
7. The exact capacity--variance batching barrier.

### Not proved

1. That \(\overline h_{\rm cut}\) equals, or is sufficiently close to,
   the balanced hard-row vector.
2. That the installed cut spaces contain the actual residual produced by
   a carrier near-factor.
3. A multi-carrier negative-covariance coupling.
4. A coefficient-scale \(K=\Theta(M)\) kernel with total variance \(o(M)\).

Therefore the surviving coefficient-one statement is conditional and
precise:

$$
\boxed{
\text{the cut-space rotor kernel is physically and probabilistically
valid, but its span and barycenter are not yet globally sufficient.}}
$$
