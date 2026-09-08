# Exact trace degrees for the affine parity-complete seed and its lifts

Date: 2026-07-26

Method: pure mathematics only.  No search, computation, Poisson surrogate,
or marginal-product assumption is used.

## 0. Verdict

For the affine double-factor \(Q_4\) seed, consider aligned physical
windows of length \(2d\), beginning at an even parity state and completing
\(d\) adjacent physical pairs.  There are

\[
                         2^{2\cdot4-1}=128           \tag{0.1}
\]

such starts.  The lower and upper trace maps have the same exact regular
fibre law:

\[
\boxed{
\begin{array}{c|c|c|c|c}
d&\text{fibre degree }\mu_d&
\text{distinct traces }R_d&
\sum_T\deg_d(T)^2&
\sum_T\deg_d(T)(\deg_d(T)-1)\\ \hline
0&1&128&128&0\\
1&1&128&128&0\\
2&2&64&256&128\\
3&8&16&1024&896\\
4&128&1&16384&16256
\end{array}}                                         \tag{0.2}
\]

Thus the nonconstant affine context does not reduce the
context-independent erased-parity multiplicity \(2^{d-1}\):

\[
 \mu_1=2^0,\qquad \mu_2=2^1,\qquad
 \mu_3=2^3>2^2,\qquad \mu_4=2^7>2^3.                \tag{0.3}
\]

The last two values are forced by the physical trace alphabet.  In an
arbitrary \(r\)-pair cell, an aligned \(d\)-pair trace has at most

\[
                         \binom rd4^{r-d}            \tag{0.4}
\]

values, while there are \(2^{2r-1}\) even starts.  Hence

\[
 \boxed{
 {1\over|\operatorname {im}\tau_d|}
 \sum_T\deg_d(T)
 \ge {2^{2d-1}\over\binom rd}.}                      \tag{0.5}
\]

For \(r=4,d=3,4\), the right side is respectively \(8,128\); the affine
seed attains equality.

The exact tensor law is multiplicative.  If \(k\) independent seed cells
are exposed at local completed-pair depths
\(\mathbf d=(d_1,\ldots,d_k)\), then every nonempty trace fibre has degree

\[
 \boxed{
 \mu_{\mathbf d}=\prod_{\ell=1}^k\mu_{d_\ell},}       \tag{0.6}
\]

and, with \(N=128^k\),

\[
\boxed{\begin{aligned}
 \#\text{ traces}&={N\over\mu_{\mathbf d}},\\
 \sum_T\deg(T)^s&=N\mu_{\mathbf d}^{\,s-1}\quad(s\ge1),\\
 \sum_T\deg(T)(\deg(T)-1)&=N(\mu_{\mathbf d}-1).
\end{aligned}}                                      \tag{0.7}
\]

In particular, every fully erased seed block contributes a factor \(128\)
to the candidate degree.  Pure tensoring makes the collision exponential.

For a general affine double factor on \(Q_r\), with

\[
                         y=Sp\oplus x,               \tag{0.8}
\]

the exact fibre over a completed support \(J\) is the fibre of the linear
observation map

\[
 (p,y)\longmapsto
 \bigl(p|_{J^c},(y\oplus Sp)|_{J^c}\bigr)            \tag{0.9}
\]

restricted to even \(p\) and the phase cell

\[
                         Y_{J,d}=\{y:J_d(y)=J\}.     \tag{0.10}
\]

If \(Y_{J,d}\) is an affine coset of a subspace \(H_{J,d}\), every
nonempty fibre has the exact degree

\[
\boxed{
 2^{\dim\mathcal K_{J,d}},\qquad
 \mathcal K_{J,d}=
 \left\{\begin{array}{l}
 (z,w): |z|\equiv0\pmod2,\ w\in H_{J,d},\\
 z|_{J^c}=0,\quad(w\oplus Sz)|_{J^c}=0
 \end{array}\right\}.}                              \tag{0.11}
\]

This is the complete rank criterion for affine context coding.

There is always an invisible parity subgroup

\[
 V_J=\{z:|z|\equiv0,\
          \operatorname {supp}z\subseteq J\cap S^{-1}J\}.       \tag{0.12}
\]

It acts by

\[
                         (p,x)\mapsto(p\oplus z,x\oplus Sz),    \tag{0.13}
\]

fixes \(y\), fixes the completed support, and fixes the physical trace.
Therefore every affine fibre is divisible by

\[
 \boxed{
 2^{\max\{|J\cap S^{-1}J|-1,0\}}.}                  \tag{0.14}
\]

For \(S=I\), this is exactly \(2^{d-1}\).  An affine context can reduce
that particular invariant only by moving a positive part of \(J\) outside
itself under \(S\).  The \(Q_4\) transposition \(S=(2\ 4)\) weakens the
universal subgroup bound on some supports, but its phase-cell kernel in
(0.11) restores the lost dimensions and gives (0.2).  Hence the present
seed does not reduce \(2^{d-1}\), while direct tensor powers and
trace-visible recursions retain and multiply all of their local seed
fibres.

Independent tensor cells impose separate local even-parity constraints.
Accordingly their exact invariant is the product (0.6), not the
single-global-parity expression \(2^{(\sum d_i)-1}\).

A genuinely new recursion can do better only if its context-dependent
completed support is itself recorded in the physical trace and separates
the erased parity assignments.  The exact recursive collision law is
nonnegative: if one old fibre \(F\) is partitioned by visible support
labels \(\sigma\), with cell sizes \(m_\sigma\), then

\[
\boxed{\begin{aligned}
 |F|&=\sum_\sigma m_\sigma,\\
 \sum_\sigma m_\sigma^2&=\text{second candidate moment},\\
 \sum_\sigma m_\sigma(m_\sigma-1)&=\text{ordered collision count}.
\end{aligned}}                                      \tag{0.15}
\]

Merely using a hidden context label does nothing: labels which are erased
by the physical trace are recombined by the sums in (0.15).  To split a
fibre of size \(M\) down to singletons requires at least \(M\) distinct
completed-support or boundary labels visible in the target.

## 1. Exact affine trace code

Let

\[
 E_r=\{p\in Q_r:|p|\equiv0\pmod2\}.
\]

Suppose \(G_0,G_1\) are neighbour permutations satisfying the same-vertex
direction relation

\[
                         \delta_1(y)=S\delta_0(y).    \tag{1.1}
\]

The affine complete-mapping construction defines

\[
 y=Sp\oplus x,\qquad
 d_p(x)=\delta_0(y),\qquad
 F_p(x)=x\oplus e_{d_p(x)}.                          \tag{1.2}
\]

Along one coarse path,

\[
                         y_t=G_0^t(y).               \tag{1.3}
\]

Thus the completed-pair support of an aligned \(d\)-step coarse window is

\[
 J_d(y)=
 \{\delta_0(y),\delta_0(G_0y),\ldots,
                      \delta_0(G_0^{d-1}y)\}.        \tag{1.4}
\]

On \(J=J_d(y)\), both physical coordinates of every pair vary, so the
lower trace is empty and the upper trace full.  On \(J^c\), the trace
records the local physical state, equivalently

\[
                         p|_{J^c},\qquad x|_{J^c}.   \tag{1.5}
\]

Consequently the aligned physical trace is exactly the code

\[
 \boxed{
 \mathcal C_d(p,x)=
 \bigl(J_d(y),p|_{J_d(y)^c},x|_{J_d(y)^c}\bigr).}    \tag{1.6}
\]

This is an equality of fibres, not merely a necessary invariant.
Both signs carry the same code: a completed pair is fixed to the empty
lower trace or the full upper trace, while an untouched pair records the
same constant physical state.  Hence the lower and upper fibre sizes are
identical without requiring a complement symmetry of the factor.

For a target code \((J,v,u)\), define

\[
\boxed{
 \deg_d(J,v,u)=
 \#\{(p,y)\in E_r\times Y_{J,d}:
       p|_{J^c}=v,\ (y\oplus Sp)|_{J^c}=u\}.}        \tag{1.7}
\]

Equations (1.7) and

\[
\boxed{\begin{aligned}
 M_1(d)&=\sum_{J,v,u}\deg_d(J,v,u)=2^{2r-1},\\
 M_2(d)&=\sum_{J,v,u}\deg_d(J,v,u)^2,\\
 \operatorname {Coll}(d)&=M_2(d)-M_1(d)
\end{aligned}}                                      \tag{1.8}
\]

are the exact candidate-degree and collision laws for every affine
double-factor seed.

### Proposition 1.1 (affine rank formula)

If \(Y_{J,d}=y_0+H_{J,d}\) is one affine coset, then every nonempty fibre
in (1.7) has size (0.11).

#### Proof

Two points \((p,y)\) and \((p',y')\) in the same fibre have differences

\[
                         z=p\oplus p',\qquad w=y\oplus y'.      \tag{1.9}
\]

Both parity contexts are even, so \(z\) is even.  Both phase points lie
in the same coset, so \(w\in H_{J,d}\).  Equality of the two visible
restrictions is exactly

\[
                         z|_{J^c}=0,\qquad
                         (w\oplus Sz)|_{J^c}=0.       \tag{1.10}
\]

Thus differences of points in one fibre form precisely
\(\mathcal K_{J,d}\).  Every element of that kernel translates one
solution to another, so every nonempty fibre is one kernel coset.
\(\square\)

If \(Y_{J,d}\) is a disjoint union of affine cosets, apply Proposition
1.1 to each coset and sum their degrees at every common output.  The
cross-coset contributions to \(M_2\) are nonnegative.

### Proposition 1.2 (invisible subgroup)

Every nonempty fibre in (1.7) contains the orbit (0.13) of \(V_J\), and
hence has the divisor (0.14).

#### Proof

For \(z\in V_J\), both \(z\) and \(Sz\) vanish on \(J^c\).  Therefore
(0.13) fixes the two visible restrictions in (1.6).  Moreover,

\[
 S(p\oplus z)\oplus(x\oplus Sz)=Sp\oplus x=y,        \tag{1.11}
\]

so it fixes the phase point and hence \(J_d(y)\).  The even-weight
subspace supported on a set of size \(t\) has dimension
\(\max\{t-1,0\}\). \(\square\)

## 2. The four affine phase cells of the \(Q_4\) seed

Use the common-phase braid rows

\[
\begin{array}{c|cccccccc}
j&0&1&2&3&4&5&6&7\\ \hline
a_j&0000&1000&1100&1110&1111&0111&0011&0001\\
b_j&0101&1101&1001&1011&1010&0010&0110&0100.
\end{array}                                         \tag{2.1}
\]

The unswitched direction word is \(1234\,1234\), and

\[
                         S=(2\ 4).                   \tag{2.2}
\]

For \(j\in\mathbb Z_4\), let \(Y_j\) contain the four vertices in phase
classes \(j\) and \(j+4\).  Put

\[
 H=\{(a,b,a,b):a,b\in\mathbb F_2\}.                 \tag{2.3}
\]

Directly from (2.1),

\[
\begin{aligned}
 Y_0&=H,\\
 Y_1&=1000+H,\\
 Y_2&=1100+H,\\
 Y_3&=1110+H.                                       \tag{2.4}
\end{aligned}
\]

Equivalently,

\[
\begin{array}{c|cccc}
j&0&1&2&3\\ \hline
y_1\oplus y_3&0&1&1&0\\
y_2\oplus y_4&0&0&1&1.
\end{array}                                         \tag{2.5}
\]

For \(1\le d\le3\), the unordered set of \(d\) consecutive directions in
\(1234\) identifies \(j\pmod4\).  Hence

\[
                         Y_{J,d}=Y_j=y_j+H.          \tag{2.6}
\]

For \(d=4\), \(J=[4]\) for every phase and

\[
                         Y_{[4],4}=Q_4.              \tag{2.7}
\]

## 3. Kernel calculation for \(d=1,2,3,4\)

Fix one support \(J\), put \(K=J^c\), and take a difference
\((z,w)\in\mathcal K_{J,d}\).  Since \(z|_K=0\), the vector \(z\) is an
even vector supported on \(J\).  Write

\[
                         w=(a,b,a,b)\in H            \tag{3.1}
\]

when \(d\le3\).

### Depth \(d=1\)

The only even vector supported on a singleton is zero.  The condition
\(w|_K=0\) on three coordinates then forces \(a=b=0\).  Thus

\[
                         \dim\mathcal K_{J,1}=0,
 \qquad\mu_1=1.                                     \tag{3.2}
\]

### Depth \(d=2\)

The four supports are

\[
                         12,\quad23,\quad34,\quad41. \tag{3.3}
\]

On each support, \(z\) is the one-dimensional even vector which is one
on both members of \(J\).  For example, when \(J=12\),

\[
 z=(t,t,0,0),\qquad
 w=(0,t,0,t).                                       \tag{3.4}
\]

The other three supports give the coordinate rotations of (3.4).
Therefore

\[
                         \dim\mathcal K_{J,2}=1,
 \qquad\mu_2=2.                                     \tag{3.5}
\]

### Depth \(d=3\)

The four supports are the complements of one coordinate.  The even
vectors supported on \(J\) form a two-dimensional space.  The single
visible coordinate imposes one equation on one of \(a,b\), leaving the
other free.  Hence

\[
                         \dim\mathcal K_{J,3}=3,
 \qquad\mu_3=8.                                     \tag{3.6}
\]

### Depth \(d=4\)

There is no visible coordinate.  The even parity context has dimension
three, and the phase point \(y\) is arbitrary in \(Q_4\), of dimension
four.  Thus

\[
                         \dim\mathcal K_{[4],4}=7,
 \qquad\mu_4=128.                                   \tag{3.7}
\]

For each \(d\), all nonempty fibres have the displayed common size.
Dividing the 128 starts by that size gives \(R_d\), and the moment
identities

\[
 M_2(d)=R_d\mu_d^2=128\mu_d,\qquad
 \operatorname {Coll}(d)=128(\mu_d-1)               \tag{3.8}
\]

prove the complete table (0.2).

This table is the exact aligned even-start sector.  Odd starts and
odd-length windows have the half-step boundary codes described by the
paired-order lift; they cannot remove any collision counted here.
Whenever their partial-pair rank pattern is distinct, their contributions
are disjoint and add to the full-factor collision moment.  Thus (0.2) is
also a literal lower bound for the complete physical factor, without
combining marginal estimates.

## 4. The physical trace-alphabet lower bound

An aligned trace records:

1. the completed support \(J\in\binom{[r]}d\);
2. one of four physical states on every untouched pair.

Thus the number of possible physical targets is at most (0.4).
Cauchy--Schwarz gives the stronger second-moment form

\[
\boxed{
 M_2(d)\ge
 {2^{4r-2}\over\binom rd4^{r-d}}.}                  \tag{4.1}
\]

Dividing by the first moment \(2^{2r-1}\) gives (0.5).  For the \(Q_4\)
seed:

\[
\begin{array}{c|cccc}
d&1&2&3&4\\ \hline
\binom4d4^{4-d}&256&96&16&1\\
128/(\binom4d4^{4-d})&1/2&4/3&8&128.
\end{array}                                         \tag{4.2}
\]

At \(d=3,4\), no context-dependent order on this physical alphabet can
improve the affine degrees \(8,128\).

## 5. Tensor candidate degrees and moments

Let \(\tau_\ell:\Omega_\ell\to\mathcal T_\ell\) be finite trace maps.
Their tensor trace is

\[
 \tau_1\otimes\cdots\otimes\tau_k:
 (\omega_1,\ldots,\omega_k)\longmapsto
 (\tau_1(\omega_1),\ldots,\tau_k(\omega_k)).         \tag{5.1}
\]

For a tensor target \(\mathbf T=(T_1,\ldots,T_k)\),

\[
 \boxed{
 \deg_{\otimes}(\mathbf T)=
 \prod_{\ell=1}^k\deg_\ell(T_\ell).}                \tag{5.2}
\]

Consequently, for every integer \(s\ge1\),

\[
 \boxed{
 \sum_{\mathbf T}\deg_{\otimes}(\mathbf T)^s
 =\prod_{\ell=1}^k\left(\sum_{T_\ell}
                              \deg_\ell(T_\ell)^s\right).}      \tag{5.3}
\]

Applying (5.2)--(5.3) to the regular seed maps in (0.2) proves
(0.6)--(0.7).

A recursive lift often exposes a sequence of full child cells and at
most two boundary child cells.  If \(f_j\) child cells are seen at local
depth \(j\), its unavoidable tensor factor is

\[
 \boxed{
 2^{\,f_2+3f_3+7f_4}.}                               \tag{5.4}
\]

This factor is present before any collision between different parent
contexts is counted.

## 6. Exact context gluing and recursive collisions

Tensor multiplicativity applies when the child target labels remain
visible.  A parent recursion may erase or identify some context labels.
The exact law then has no cancellation.

Let \(\Omega=\bigsqcup_c\Omega_c\), and let
\(\tau_c:\Omega_c\to\mathcal T\) be the trace map in context \(c\).
Put

\[
                         d_c(T)=|\tau_c^{-1}(T)|.    \tag{6.1}
\]

After forgetting the context label, the candidate degree is

\[
 \boxed{
                         d(T)=\sum_cd_c(T).}         \tag{6.2}
\]

Its second moment and ordered collision count are

\[
\boxed{\begin{aligned}
 \sum_Td(T)^2
 &=\sum_c\sum_Td_c(T)^2
   +\sum_{c\ne c'}\sum_Td_c(T)d_{c'}(T),\\
 \sum_Td(T)(d(T)-1)
 &=\sum_c\sum_Td_c(T)(d_c(T)-1)
   +\sum_{c\ne c'}\sum_Td_c(T)d_{c'}(T).
\end{aligned}}                                      \tag{6.3}
\]

Every cross-context term is nonnegative.  Context dependence reduces
collisions only when it changes a label which remains physically visible
in the final target.

More locally, let \(F\) be one old fibre and let the new visible schedule
label partition it as

\[
                         F=\bigsqcup_{\sigma\in\Sigma}F_\sigma,
 \qquad m_\sigma=|F_\sigma|.                         \tag{6.4}
\]

Then (0.15) is immediate.  In particular,

\[
\boxed{
 \sum_\sigma m_\sigma^2\ge {|F|^2\over|\Sigma|},
 \qquad
 \max_\sigma m_\sigma\ge
 \left\lceil{|F|\over|\Sigma|}\right\rceil.}         \tag{6.5}
\]

If the parent scheduling rule is a function only of the old visible
trace, it is constant on \(F\), so \(|\Sigma|=1\) and the entire old
fibre survives.  This proves:

### Theorem 6.1 (trace-visible return-free recursion no-go)

Consider a tensor or return-free recursive lift of the affine \(Q_4\)
seed in which parent stages add directions disjoint from those already
completed in a child, and each parent order is determined by already
visible child traces.  Then the lift retains the factor (5.4).  Forgetting
parent context labels can only increase the second moment through the
cross terms in (6.3).

To improve the degree, a recursion must read information which is
currently erased and convert it into a different completed support or
boundary label which the final physical target records.  Merely selecting
one of several orders by a hidden context does not split a physical trace
fibre.

## 7. Can affine context dependence reduce \(2^{d-1}\)?

The exact answer has three levels.

1. **Only potentially, and only through visible support motion.**
   Formula (0.14) replaces \(d\) by the self-overlap
   \(|J\cap S^{-1}J|\).  A permutation \(S\) which moves most of \(J\)
   outside \(J\) removes the corresponding universal invisible subgroup.
   This does not itself prove smaller fibres: the phase cells
   \(Y_{J,d}\) must also have enough rank to separate the remaining
   assignments.  Parity completeness alone supplies no such separation.

2. **For the affine \(Q_4\) seed, no.**  The exact kernel dimensions are
   \(0,1,3,7\), giving (0.2).  At \(d=3,4\), the physical trace alphabet
   proves that no alternative context rule can do better than \(8,128\)
   on average.

3. **For tensor and trace-visible return-free recursive lifts of this
   seed, no local fibre is reduced.**  Degrees and all moments multiply
   by (5.2)--(5.3), and hidden context gluing adds the nonnegative cross
   terms (6.3).  With separate child parity constraints the resulting
   invariant is the product of local degrees, as noted after (0.14).

Thus parity-complete ownership and nonconstant affine context are not
enough.  A successful recursion must be a literal erasure code: within
each old parity fibre it must produce sufficiently many distinct physical
completed supports.  Equations (0.11), (0.14), and (6.5) are the exact
rank, invariant, and expansion conditions that such a recursion must
beat.
