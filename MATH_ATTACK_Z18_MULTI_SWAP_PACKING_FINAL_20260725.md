# Multi-swap packing in one calibrated top: capacity and chronology

Date: 2026-07-25

Method: pure mathematics only. No computation, search, solver, or web
input is used.

## 0. Exact verdict

Let

$$
M=m+H,\qquad
\mathcal B_Q=\{m-Q,\ldots,m+Q\},
$$

and assume the calibrated asymptotic regime

$$
H=o(m),\qquad Q=o(H),\qquad \frac{Q}{\sqrt M}\longrightarrow\infty.
\tag{0.1}
$$

This includes

$$
H\asymp\sqrt{m\log m},\qquad
Q\asymp\sqrt{m\log\log m}.
$$

There are three different answers, depending on what “choices” means.

1. **Literal synchronized capacity: yes.** One complementary-segment
   diagonal with only $(2+o(1))Q$ duplicated phase occurrences carries
   $(1-o(1))M$ pairwise support-disjoint rank-isolating rectangle cells
   and hard-window $\ell _1$ effect $(4-o(1))M$. All cells switch
   together, subject to an exact cut-space parity law.
2. **Independent positive state capacity: yes.** A phase-varying port
   construction carries at least $M$ independently selectable,
   support-disjoint rectangle bits with only

   $$
   t=(4+o(1))\frac{M}{Q}=o(Q)
   $$

   duplicated owner phases. Its middle-owner multiset is independent of
   all bits.
3. **Uniform coefficient-one promotion-path realization: no for this
   port cube.** A worst cube vertex forces either

   $$
   F=\Theta(M/Q)
   $$

   promotion fragments at length $M+O(Q)$, or

   $$
   N=\Omega(MH/Q)=\omega(M)
   $$

   useful-state occurrences if only $O(1)$ paths are allowed. The exact
   inequality is

   $$
   N\ge F+(2t-F)(H-R+1),\qquad R\le Q.
   \tag{0.2}
   $$

The hidden unordered reserve is sufficient to splice the synchronized
bundle. It is not sufficient to reprogram the independent cube while its
selector labels occupy the ordered deletion queue. Thus owner capacity
and integrality are not the remaining obstruction; ordered-collar
chronology is.

## 1. Composite complementary-segment identity

Fix a top $U$, $|U|=M$, and a directed cyclic order $\pi$ of $U$. Index
positions and phase starts by $\mathbb Z_M$. A cut $c$ lies between
positions $c-1$ and $c$; let $\sigma_c$ interchange the entries in those
positions.

For a cyclic order $\rho$, let

$$
v_{s,u}(\rho)=e_{[u,u+s-1]_\rho}
$$

denote the basis vector of the length-$s$ positional interval beginning
at phase $u$, and write

$$
I_{s,A}(\rho)=\sum_{u\in A}v_{s,u}(\rho),\qquad
I_s(\rho)=I_{s,\mathbb Z_M}(\rho).
$$

### Lemma 1.1 (affected starts)

If $P$ is a product of adjacent position swaps at cuts $C$, then

$$
v_{s,u}(P\rho)=v_{s,u}(\rho)
$$

unless

$$
u\in\bigcup_{c\in C}\{c,c-s\}.
\tag{1.1}
$$

Therefore every first difference under $P$ throughout $\mathcal B_Q$ is
supported on

$$
E_Q(P)=
\bigcup_{c\in C}
\left(\{c\}\cup\{c-s:s\in\mathcal B_Q\}\right).
\tag{1.2}
$$

#### Proof

A positional interval notices the swap at cut $c$ exactly when one of its
two boundary cuts is $c$. Its start is then $c$ or $c-s$. Otherwise the
two swapped positions are both inside or both outside the interval, so
the interval's label set is unchanged. Apply this successively to all
constituent swaps. $\square$

### Theorem 1.2 (composite segment identity)

Let $P,R$ be products of swaps with disjoint moved-position supports.
Suppose phase sets $A,B$ satisfy

$$
A\cup B=\mathbb Z_M,\qquad E_Q(P)\subseteq A\cap B.
\tag{1.3}
$$

Define the positive segment systems

$$
\mathcal C^-=\pi|_A\sqcup PR\pi|_B,\qquad
\mathcal C^+=P\pi|_A\sqcup R\pi|_B.
\tag{1.4}
$$

Then, for every $s\in\mathcal B_Q$,

$$
\boxed{
I_s(\mathcal C^-)-I_s(\mathcal C^+)
=I_s(\pi)+I_s(PR\pi)-I_s(P\pi)-I_s(R\pi).}
\tag{1.5}
$$

#### Proof

At a phase in $A-B$, the local difference is
$v_{s,u}(\pi)-v_{s,u}(P\pi)$; at a phase in $B-A$, it is
$v_{s,u}(PR\pi)-v_{s,u}(R\pi)$. Both vanish by Lemma 1.1, because such a
phase is outside $E_Q(P)$. At a phase in $A\cap B$, all four terms occur.
The full mixed difference also vanishes outside $E_Q(P)$. Summing the
phasewise identity proves (1.5). $\square$

This is an integral identity between positive literal promotion segments.

## 2. A literal synchronized $\Theta(M)$-cell bundle

For sufficiently large $m$, (0.1) implies

$$
4H<m,\qquad 4Q<H,\qquad 48L\le Q,
\qquad L=\lfloor\sqrt M\rfloor.
\tag{2.1}
$$

Put $q_0=\lfloor Q/2\rfloor$ and choose cuts

$$
a_i=6i,\qquad
b_j=m+q_0+6j,\qquad 0\le i,j<L.
\tag{2.2}
$$

Let $\sigma_i$ and $\tau_j$ swap across $a_i$ and $b_j$, respectively,
and put

$$
P_i=\sigma_{i-1}\cdots\sigma_0,\qquad
R_j=\tau_{j-1}\cdots\tau_0,
$$

with $P_0=R_0=1$, $P=P_L$, and $R=R_L$. Spacing six makes all moved
pairs disjoint.

In the free integer module on cyclic orders,

$$
\begin{aligned}
Z
&=e_\pi+e_{PR\pi}-e_{P\pi}-e_{R\pi}\\
&=\sum_{i=0}^{L-1}\sum_{j=0}^{L-1}
\bigl(
e_{P_iR_j\pi}+e_{P_{i+1}R_{j+1}\pi}
-e_{P_{i+1}R_j\pi}-e_{P_iR_{j+1}\pi}
\bigr).
\end{aligned}
\tag{2.3}
$$

The equality is double telescoping. The $(i,j)$ summand is the elementary
adjacent-swap square for $\sigma_i,\tau_j$.

Its directed cut separation is

$$
r_{ij}=b_j-a_i=m+q_{ij},\qquad
q_{ij}=q_0+6(j-i).
\tag{2.4}
$$

Condition (2.1) gives

$$
\frac Q4\le q_{ij}\le\frac{3Q}{4}.
\tag{2.5}
$$

An adjacent-swap square is nonzero only at lengths

$$
r_{ij}\quad\text{and}\quad M-r_{ij}=H-q_{ij}.
\tag{2.6}
$$

Thus exactly the first exceptional length lies in $\mathcal B_Q$.

### Theorem 2.1 (noncancelling cell capacity)

The $L^2$ hard-window rectangle supports in (2.3) are pairwise disjoint.
Consequently

$$
\boxed{
\sum_{s\in\mathcal B_Q}\|I_s(Z)\|_1=4L^2=(4-o(1))M.}
\tag{2.7}
$$

#### Proof

Let $A_i$ be the two-label block at the $\sigma_i$ positions in $\pi$,
and $B_j$ the corresponding block at the $\tau_j$ positions. Every mask
in cell $(i,j)$ contains exactly one label from $A_i$, exactly one label
from $B_j$, and either zero or two labels from every other moved
two-block. This is because its two positional boundary cuts are precisely
$a_i,b_j$.

Therefore the parity vector of intersections with the moved two-blocks
identifies $(i,j)$. Two different cells cannot share a mask. Each cell
has four distinct masks with coefficients $+1,+1,-1,-1$, proving (2.7).
$\square$

The primary cuts $a_i$ occupy an interval of length at most $6L$.
Lemma 1.1 places $E_Q(P)$ in two cyclic intervals of total size at most

$$
D\le2Q+12L+4=(2+o(1))Q.
\tag{2.8}
$$

Choose complementary cyclic phase intervals $A,B$ whose union is the
phase circle and whose intersection contains $E_Q(P)$ with size $D$.
Theorem 1.2 gives literal systems (1.4), each with $M+D$ state
occurrences, and exact hard-window difference $I_s(Z)$.

No cell is exceptional at length $m$, so

$$
I_m(\mathcal C^-)=I_m(\mathcal C^+)
\tag{2.9}
$$

as an exact owner multiplicity vector. Each of $P,R$ contains $L$ swaps,
and one adjacent swap affects exactly two middle starts. Selecting one
occurrence over every phase shows that each sign retains at least
$M-4L$ distinct base owners. Its collision excess is at most

$$
D+4L=(2+o(1))Q.
\tag{2.10}
$$

### Hidden-interior splice

All moved positions lie in the short cyclic arc from the $b$-cluster,
through the cyclic wrap, to the $a$-cluster. Its length is at most

$$
h_*=H-q_0+6L+2<m-H.
\tag{2.11}
$$

At at least

$$
m-H-h_*+1
\tag{2.12}
$$

phases, the unordered reserve block of size $m-H$ contains this entire
arc. At each such phase, $\pi,P\pi,R\pi,PR\pi$ have the same ordered
deletion queue, the same ordered cache, and the same reserve set. Hence
they encode one identical useful state. These are exact reset-free common
ports. The segment endpoints may be cut at such a port, adding at most
one zero-difference overlap occurrence, so the number of path pieces is
$O(1)$ and is independent of $L^2$.

This proves literal aggregate $\Theta(M)$ capacity with only $O(Q)$
duplicated owner phases.

### Exact sign lock

This bundle has one synchronized diagonal bit, not $L^2$ independent
bits. If primary coordinate $i$ is traversed with sign
$u_i\in\{\pm1\}$ and secondary coordinate $j$ with sign
$v_j\in\{\pm1\}$, double telescoping gives cell coefficient

$$
c_{ij}=u_iv_j.
\tag{2.13}
$$

Hence every four-cycle obeys

$$
c_{ij}c_{i'j'}=c_{ij'}c_{i'j}.
\tag{2.14}
$$

The sign family has only $2L-1$ binary degrees of freedom. Hidden
splicing can choose the row and column signs before the swaps become
visible, but cannot invalidate (2.14), which holds already in the free
order module.

The $O(Q)$ truncation above is exact only on $\mathcal B_Q$. At depths
$Q<q\le H$, the usual single-swap truncation counterterms remain. This
bundle does not prove full-band isolation with $O(Q)$ overlap.

## 3. An exact independent positive port cube

The sign lock is specific to one composite four-frame diagonal. It is not
an owner-phase capacity obstruction.

Set

$$
p=\lfloor Q/4\rfloor,\qquad
t=\left\lceil\frac{M}{p}\right\rceil.
\tag{3.1}
$$

Because $Q^2/M\to\infty$, for all sufficiently large $m$,

$$
4t+2p\le Q.
\tag{3.2}
$$

Choose $p$ row swaps $\alpha_i$ at cuts after positions

$$
a_i=4t+2i,\qquad 0\le i<p,
\tag{3.3}
$$

and $t$ column swaps $\beta_j$ at cuts after

$$
b_j=m+2j-1,\qquad
s_j=2j,\qquad 0\le j<t.
\tag{3.4}
$$

Here $s_j$ is the $j$-th marked phase. All moved pairs are disjoint.
For $x\in\{0,1\}^p$, put

$$
\alpha_x=\prod_{i=0}^{p-1}\alpha_i^{x_i},\qquad
\bar x=\mathbf1-x,\qquad
\beta=\prod_{j=0}^{t-1}\beta_j.
\tag{3.5}
$$

Let $S_u(\rho)$ be the radius-$H$ useful state encoded by order $\rho$ at
phase $u$. At marked phase $s_j$, define the positive pair

$$
\mathcal F_j(x)=
\{S_{s_j}(\alpha_x\pi),\,
  S_{s_j}(\alpha_{\bar x}\beta\pi)\}.
\tag{3.6}
$$

For a bit matrix $E\in\{0,1\}^{p\times t}$, let $x^j$ be column $j$ and
define

$$
\mathcal F(E)=
\{S_u(\pi):u\notin\{s_0,\ldots,s_{t-1}\}\}
\sqcup
\mathop{\bigsqcup}_{j=0}^{t-1}\mathcal F_j(x^j).
\tag{3.7}
$$

### Theorem 3.1 (independent $pt$-bit state cube)

Every $\mathcal F(E)$ has exactly $M+t$ positive useful-state
occurrences. Its middle-owner multiset is independent of $E$ and contains
all $M$ base owners.

There are pairwise support-disjoint elementary rectangles
$\rho_{ij}$, each supported only at lower rank $m-q_{ij}$, where

$$
q_{ij}=a_i-s_j+1=4t+2i-2j+1,
\tag{3.8}
$$

and

$$
2t+3\le q_{ij}\le4t+2p-1\le Q,
\tag{3.9}
$$

such that

$$
\boxed{
I_{\rm cent}(\mathcal F(E))-I_{\rm cent}(\mathcal F(0))
=\sum_{i=0}^{p-1}\sum_{j=0}^{t-1}E_{ij}\rho_{ij}.}
\tag{3.10}
$$

Here $I_{\rm cent}$ includes every lower and upper central rank
$m\pm q$, $0\le q\le H$. In particular the identity has no leakage
outside the hard window.

Moreover,

$$
\sum_{\rm central\ ranks}
\|I_s(\mathcal F(E))-I_s(\mathcal F(E'))\|_1
=4\,d_{\rm Ham}(E,E').
\tag{3.11}
$$

Finally,

$$
pt\ge M,\qquad
t=(4+o(1))\frac{M}{Q}=o(Q).
\tag{3.12}
$$

Thus at least $M$ independently selectable rank rectangles are
superposed with only $o(Q)$ duplicated owner phases.

#### Proof

At phase $s_j$, the base middle owner is the positional interval

$$
X_j=[2j,m+2j-1].
$$

Every row pair lies wholly inside $X_j$. Among the column pairs, those
with index below $j$ lie wholly inside, those above $j$ lie wholly
outside, and only $\beta_j$ crosses the right boundary. Therefore
$\mathcal F_j(x)$ has owner multiset

$$
\{X_j,\beta_jX_j\},
\tag{3.13}
$$

independent of $x$. At unmarked phases the base state is unchanged.
Hence every $\mathcal F(E)$ contains all $M$ base owners and exactly one
additional occurrence at each of the $t$ marked phases.

Now toggle bit $x_i$ at port $j$, initially with $x_i=0$. Write

$$
G=\prod_{h\ne i}\alpha_h^{x_h},\qquad
K=\prod_{h\ne i}\alpha_h^{1-x_h}.
$$

The signed change of the two port states is

$$
e_{\alpha_iG\pi}+e_{K\beta\pi}
-e_{G\pi}-e_{\alpha_iK\beta\pi}.
\tag{3.14}
$$

The lower depth-$q$ flag at phase $s_j$ is the positional interval

$$
[s_j+q,s_j+m-1].
\tag{3.15}
$$

It notices $\alpha_i$ exactly when its left boundary is the
$\alpha_i$ cut, namely when $q=q_{ij}$. At this depth its right boundary
is the $\beta_j$ cut. Every other row pair and every other column pair is
wholly inside or wholly outside (3.15). Thus (3.14) is exactly the
elementary $\alpha_i$-by-$\beta_j$ rectangle at lower rank
$m-q_{ij}$.

At every other lower depth, $\alpha_i$ is invisible. Every upper flag and
the middle owner contain both positions of every row pair, so (3.14)
vanishes there as well. The rectangle is independent of the other bits,
and toggling entries one at a time proves (3.10).

Different $q_{ij}$ give different ranks. If
$q_{ij}=q_{i'j'}$, then $i'-i=j'-j=d$. Suppose $d>0$. Every mask in the
later cell $(i',j')$ contains both labels of the earlier right-boundary
block $\beta_j$, while every mask in cell $(i,j)$ contains exactly one.
Thus their supports are disjoint; $d<0$ is symmetric. This proves (3.11).

The inequalities in (3.9) follow directly from the extreme indices and
(3.2). Finally $pt\ge M$ by definition, while
$p=(1+o(1))Q/4$ gives (3.12). $\square$

Theorem 3.1 is a positive integral state theorem, but the states in
(3.7) have not yet been placed on few promotion paths. That distinction
is decisive.

## 4. Ordered-queue chronology obstruction

At every marked phase $s_j\le2t-2$, all row labels lie among the first

$$
R=4t+2p\le Q
\tag{4.1}
$$

entries of the ordered deletion queue. Their pair orientations record
signature $x^j$ in the first state of (3.6) and $\bar x^j$ in the second.
They are not in the unordered reserve at these phases.

One promotion step changes the deletion queue by

$$
(a_1,\ldots,a_H)\longmapsto(a_2,\ldots,a_H,z),
\tag{4.2}
$$

where $z$ is selected from the reserve. After
$d\le H-R$ transitions, the first $R$ entries of the new queue are
inherited, in their old relative order, from entries
$d+1,\ldots,d+R$ of the old queue. No appended label has reached that
prefix.

Choose columns $x^0,\ldots,x^{t-1}$ so that

$$
x^0,\bar x^0,\ldots,x^{t-1},\bar x^{t-1}
\tag{4.3}
$$

are pairwise distinct. This is possible for large $m$, because there are
$2^{p-1}$ complement classes and $t$ is only polynomial in $m$.

### Theorem 4.1 (exact fragmentation inequality)

Let a literal realization contain these $2t$ marked port states. Suppose
it uses $N$ useful-state occurrences and $F$ promotion paths containing
marked states. Put

$$
D=H-R+1.
\tag{4.4}
$$

Then

$$
\boxed{N\ge F+(2t-F)D.}
\tag{4.5}
$$

Consequently,

$$
N\le M+O(Q)
\quad\Longrightarrow\quad
F=(2-o(1))t=\Theta(M/Q),
\tag{4.6}
$$

whereas

$$
F=O(1)
\quad\Longrightarrow\quad
N=\Omega(tH)=\Omega(MH/Q)=\omega(M).
\tag{4.7}
$$

#### Proof

Suppose two marked states with different signatures occur on one
promotion path at distance $d<D$. Both states contain every row-pair
label in their first $R$ queue entries. By (4.2), the later prefix is
inherited from the earlier ordered queue, so the relative order inside
every row pair is unchanged. Their signatures must be equal, a
contradiction.

Hence consecutive marked states on one path are separated by at least
$D$ transitions. A path containing $k\ge1$ marked states has at least

$$
1+(k-1)D
$$

state occurrences. Summing over the $F$ paths and using
$\sum k=2t$ proves (4.5).

Solving for $F$ gives

$$
F\ge2t-\frac{N-2t}{D-1}.
\tag{4.8}
$$

Now $D=(1-o(1))H$ and

$$
\frac{M/H}{t}=(1+o(1))\frac{Q}{4H}=o(1).
$$

Substituting $N\le M+O(Q)$ proves (4.6). Equation (4.7) follows directly
from (4.5), since $tH=(4+o(1))MH/Q$ and $H/Q\to\infty$. $\square$

The obstruction already permits arbitrary choices of the promoted
reserve label between marked states. Hidden-interior permutation cannot
evade it, because the programmed labels are in the ordered queue, not the
reserve.

If one imports the established literal compiler ledger that an
independent path initialization costs $\Theta(H)$ entries, (4.6) gives
initialization cost

$$
\Theta(HM/Q)=\omega(M)
$$

per top. Without importing that compiler fact, the unconditional result
is exactly (4.5).

## 5. Sharp scope and coefficient-one ledger

The two positive theorems solve different parts of the problem.

| construction | independent bits | duplicate phases | path status |
|---|---:|---:|---|
| synchronized composite bundle | cut-space only; one dense switch has $(1-o(1))M$ cells | $(2+o(1))Q$ | $O(1)$ literal promotion pieces |
| independent port cube | $pt\ge M$ | $t=(4+o(1))M/Q=o(Q)$ | worst vertex needs $\Theta(M/Q)$ fragments or $\Omega(MH/Q)$ states |

For the synchronized construction, the leading $2Q$ overlap is sharp if
one fixed primary cut must support every hard-window secondary choice:
the forced affected starts are

$$
\{c\}\cup\{c-s:s\in\mathcal B_Q\},
$$

which has exactly $2Q+2$ phases. Omitting one of them misses the elementary
square obtained by putting the secondary cut at the other boundary of
that interval.

Across calibrated tops with

$$
MN_H=(1+o(1))W,
$$

the synchronized construction has global duplicate toll

$$
O(QN_H)=O(WQ/m)=o(W),
$$

bounded-path initialization toll

$$
O(HN_H)=O(WH/m)=o(W),
$$

and aggregate hard-window capacity $\Theta(MN_H)=\Theta(W)$. Its unresolved
gate is the cut-space sign restriction and the leakage beyond $Q$.

The independent cube has enough static directions and a fixed middle
histogram, but Theorem 4.1 makes the present promotion-only chronology
too expensive by the factor $H/Q\to\infty$. A coefficient-one completion
would therefore need a new literal seam that reprograms an ordered queue
signature without an $H$-step residence delay and without a fresh
initialization. Hidden permutation of the reserve alone cannot do this.

## 6. Internal audit

The decisive steps were independently checked.

1. Equation (2.3) is an identity in the free integer order module; no
   fractional or negative physical state is used.
2. Each synchronized cell has exceptional lengths exactly
   $r_{ij},M-r_{ij}$, and only $r_{ij}$ lies in $\mathcal B_Q$.
3. Endpoint-block parity proves disjoint support in Theorem 2.1, so the
   norm in (2.7) has no hidden cancellation.
4. The whole moved-position support, not just one swap, fits inside one
   reserve block at the common ports (2.12).
5. In the independent cube, every nonendpoint swap is wholly inside or
   outside the relevant lower interval; every upper interval contains
   both positions of every row swap.
6. Equal-depth port cells are separated by the earlier right-boundary
   block, which occurs once in one cell and twice in the other. Hence the
   cube image really has dimension $pt$.
7. The middle-owner multiset in (3.13) is exact and independent of all
   bits.
8. The fragmentation inequality uses only the exact queue recurrence
   (4.2). It already allows arbitrary reserve choices between ports.

Thus the precise proved boundary is:

$$
\boxed{\text{static multi-rectangle capacity is sufficient, but
promotion-path chronology is not.}}
$$
