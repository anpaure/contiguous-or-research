# A transversal retained-axis selector and the remaining compiler Hall gate

Date: 2026-07-26

Method: pure mathematics only.  No computation, solver, or web input is
used.

## 0. Outcome

Let \(C\cong Q_S\) be a product status cell in the rank-twisted
macroblock construction.  The parallel split used in the original owner
theorem chooses one fixed \(r\)-set of axes in \(C\).  That freedom admits
the localized-carrier counterexample: almost every packet can be placed
inside one ground carrier of size \(\Theta(r)\), producing a lower and
upper Gaussian Hall ratio \(\exp[-\Theta(q^2/r)]=o(1)\).

This note gives an exact owner-preserving selector which removes that
counterexample.

Partition the \(S\) orientation axes into \(r\) large groups.  In each
group install a direction-spread perfect matching of its orientation
cube.  A packet is the Cartesian product of one matching edge from every
group.  Thus every packet is a physical \(Q_r\), but its active support
contains one direction from each group and varies with the owner
cylinder.  The packets partition \(Q_S\) exactly.

The local matchings can be chosen so that every payload direction in a
group is used with frequency \(1+o(1)\) times uniform.  Consequently:

1. the packet supports form an asymptotically exact transversal block
   design;
2. distinct packet faces inside one cell are literal-target distinct;
3. affine compiler conjugates can be batched integrally, separately
   inside every support class, with error \(2^{-\Omega(S)}\); and
4. for every set \(E\) of physical cell axes, the fraction of actual
   signed depth-\(q\) compiler occurrences whose whole direction support
   lies in \(E\) is at most

   \[
       \boxed{\nu_{C,q}(E)
       \le(1+o(1))
          \left({|E\cap P_C|\over |P_C|}\right)^q,}               \tag{0.1}
   \]

   where \(P_C\) is the payload-axis set and
   \(|P_C|=S-o(S)\).  The same estimate holds for both signs.

In particular, if \(|E|=\Theta(r)\), \(S=\Theta(m)\), and
\(q=A\sqrt m\), then

\[
                 \nu_{C,q}(E)
        \le \exp[-\Omega(q\log(m/r))]=o(1).                       \tag{0.2}
\]

Thus no fixed localized \(E\) contains a positive fraction of the
selected compiler occurrences, let alone the \(1-o(1)\) fraction used in
the old Hall cut.  The \(\exp[-\Theta(q^2/r)]\) obstruction is not
unavoidable.

The selector also retains the allocation score reservoir.  Under

\[
              r\gg qd^2,\qquad d\asymp\log m,                     \tag{0.3}
\]

which holds for \(r=m^{3/5+o(1)}\), every bounded joint lower/upper score
class occurs on \(\Theta(r/d)\gg q\) retained axes of almost every
selected packet.  Hence the selected-axis graph has the same
positive-density Gaussian profile Hall expansion as the maximal graph,
now simultaneously for the two signs.

This still does not prove arbitrary raw Hall or coefficient one.  The
exact selected-axis graph and the packet-configuration dual are stated
below.  An arbitrary maximal raw injection cannot be lifted: the
requirements assigned to the \(2^r\) owners of one packet may have union
larger than \(r\).  A coherent selected-axis injection must be constructed
directly.  After that, one compiler conjugate still couples all starts in
one packet.  The remaining theorem is the literal, block-labelled
configuration inequality (9.4), not another anti-localization estimate.

## 1. A direction-spread perfect matching

The elementary gadget is a perfect matching of \(Q_L\) whose edge
directions are nearly uniform.

### Lemma 1.1 (selector-hash matching)

Let \(L\to\infty\), choose

\[
                         t=\lceil3\log_2m\rceil<L,                \tag{1.1}
\]

and split the coordinate set as

\[
                         G=B\mathbin{\dot\cup}P,
 \qquad |B|=t,\quad |P|=v=L-t.                                  \tag{1.2}
\]

There is a perfect matching \(\mathcal M_G\) of \(Q_G\) using only
directions in \(P\), such that a uniform matching edge has direction
\(i\in P\) with probability

\[
                         p_i={1+\theta_i\over v},
 \qquad |\theta_i|\le {v\over2^t}=O(m^{-2}).                     \tag{1.3}
\]

#### Proof

Choose a map

\[
                         \iota:Q_B\longrightarrow P              \tag{1.4}
\]

whose fibre sizes differ by at most one.  In the branch \(x|_B=z\),
pair every word with the word obtained by flipping coordinate
\(\iota(z)\).  Because \(\iota(z)\notin B\), this flip remains inside the
same branch.  Inside a branch it is the parallel perfect matching in
direction \(\iota(z)\), and the branches partition \(Q_G\).  Hence their
union is a perfect matching.

The number of matching edges in direction \(i\) is

\[
                         |\iota^{-1}(i)|\,2^{v-1}.                \tag{1.5}
\]

Division by the total \(2^{L-1}\) edges gives
\(p_i=|\iota^{-1}(i)|/2^t\).  Since
\[
 \left||\iota^{-1}(i)|-{2^t\over v}\right|\le1,
\]
(1.3) follows. \(\square\)

The \(t\) coordinates in \(B\) are local selectors for this one matching
gadget.  They are not global selector coordinates for the whole
\(Q_S\)-cell, and the choices made in different groups are independent.
Their total number will be \(rt=o(S)\).

### Remark 1.2 (selector-free power-of-two gadget)

When \(L=2^a\), \(a\ge2\), the local selector coordinates can be removed.
Index the \(L\) cube coordinates by \(V=\mathbb F_2^a\).  Choose an
invertible linear map \(M:V\to V\) for which \(I+M\) is invertible.  For
an even word \(x\in Q_L\), put

\[
 \sigma(x)=\sum_{u\in V}x_u u,\qquad
 d(x)=(I+M)\sigma(x),\qquad
 f(x)=x\oplus e_{d(x)}.                                         \tag{1.6}
\]

If \(f(x)=f(y)\), then with \(a=d(x),b=d(y)\),
\[
 x\oplus y=e_a\oplus e_b.
\]
Taking syndromes and using
\(a\oplus b=(I+M)(\sigma(x)\oplus\sigma(y))\) gives
\(M(a\oplus b)=0\), hence \(a=b\) and \(x=y\).  Thus \(f\) is a
bijection from the even to the odd shore.  The syndrome map on the even
shore is onto \(V\), so every direction is used exactly
\(2^{L-1}/L\) times.  This is an exact balanced perfect matching.

## 2. Exact transversal \(Q_r\)-tiling

Call a product cell dimension-typical when \(S\ge m/3\).  The total
middle-owner mass in cells which are not dimension-typical is \(o(W/H)\):
for each fixed local-rank vector the split count has the binomial
\(\operatorname{Bin}(m-O(d),1/2)\) census, its lower tail is
\(\exp[-\Omega(m)]\), and the number of rank vectors and residual states
is \(2^{o(m)}\).  On these exceptional cells retain any legal parallel
\(Q_r\)-split.  They do not affect an \(o(W)\) Hall ledger.

On every dimension-typical cell assume

\[
                         r=o(S),\qquad {S\over r}\gg\log m.       \tag{2.1}
\]

Partition the \(S\) axes into labelled groups

\[
                         G_1\dot\cup\cdots\dot\cup G_r,          \tag{2.2}
\]

with sizes differing by at most one.  In every \(G_h\), apply Lemma 1.1,
using selector set \(B_h\), payload \(P_h\), and matching
\(\mathcal M_h\).  Put

\[
                         B_C=\bigdotcup_hB_h,\qquad
                         P_C=\bigdotcup_hP_h.                    \tag{2.3}
\]

Then

\[
                         |B_C|=rt=o(S),\qquad |P_C|=S-o(S).      \tag{2.4}
\]

For a tuple of matching edges

\[
                         e=(e_1,\ldots,e_r),
 \qquad e_h\in\mathcal M_h,                                     \tag{2.5}
\]

define

\[
                         Q(e)=e_1\times\cdots\times e_r
                                  \cong Q_r.                     \tag{2.6}
\]

### Theorem 2.1 (transversal owner factor)

The cubes \(Q(e)\) in (2.6) partition \(Q_S\) exactly.  Every packet has
one active physical axis in every group \(G_h\), and no axis in \(B_C\)
is active.

#### Proof

Every \(\mathcal M_h\) partitions \(Q_{G_h}\) into edges.  Cartesian
products of parts of \(r\) partitions form a partition of their Cartesian
product
\[
                         Q_S=\prod_{h=1}^rQ_{G_h}.
\]
Every product contains two choices in each group and hence is a physical
\(Q_r\). \(\square\)

This construction applies independently in every retained rank-twisted
product cell.  It changes neither its owner set nor the already proved
low-dimension leave.  Together with the arbitrary split on the
dimension-exceptional cells, it is an exact partition of every owner
covered by the original theorem.  The grouping and the maps \(\iota_h\)
may depend on the cell's fixed rank/status tag.

## 3. The exact support design

For a packet \(Q(e)\), let

\[
                         R(e)=\{\operatorname{dir}(e_h):h\le r\}. \tag{3.1}
\]

It is a transversal: \(|R(e)\cap P_h|=1\) for every \(h\).  For
\(i\in P_h\), let \(p_{h,i}\) be its direction frequency in
\(\mathcal M_h\).  The product construction gives the exact support law

\[
 \Pr\{R(e)=\{i_1,\ldots,i_r\}\}
                         =\prod_{h=1}^rp_{h,i_h}.                 \tag{3.2}
\]

In particular the group directions are independent, and by (1.3) each
is \(1+O(m^{-2})\) times uniform.  Since \(r=o(m)\), every support tuple
has probability

\[
                  (1+o(1))\prod_h|P_h|^{-1}.                    \tag{3.3}
\]

There is also an exact face-recovery property.

### Lemma 3.1 (within-cell face recovery)

Let \(F\) be any abstract face of a packet \(Q(e)\).  From \(F\), viewed
as a face of \(Q_S\), one recovers the unique tuple \(e\) and hence the
unique packet containing it.

#### Proof

In group \(G_h\), either the packet direction is used by \(F\), in which
case the local face is the entire matching edge \(e_h\), or it is unused,
in which case the local face is one endpoint of \(e_h\).  A matching edge
is recovered from either the edge itself or either endpoint, because
\(\mathcal M_h\) is a perfect matching.  Do this independently in all
groups. \(\square\)

Consequently, if the compiler in each packet is trace-injective, all
lower depth-\(q\) targets emitted by one product cell are distinct.
The same holds above.  This removes within-cell target collisions without
requiring parallel packets or a common global selector cylinder.

## 4. Integral compiler batching

Let

\[
                         \Gamma_r=\mathbb F_2^r\rtimes S_r       \tag{4.1}
\]

be the affine conjugate catalogue of a fixed valid two-sided compiler on
\(Q_r\).  For a physical support tuple \(R\), the number of packets with
that support is

\[
                         N_R=\prod_{h=1}^r
               \bigl(|\iota_h^{-1}(i_h)|\,2^{|P_h|-1}\bigr).     \tag{4.2}
\]

Uniformly in \(R\),

\[
 \log_2N_R
 =S-r-r\log_2(S/r)+o(S)=\Omega(S),                              \tag{4.3}
\]

whereas

\[
                         \log_2|\Gamma_r|=O(r\log r)=o(S).       \tag{4.4}
\]

Assign the labels of \(\Gamma_r\) as evenly as possible among the packets
of every fixed support \(R\).  The exceptional fraction in one support
class is at most

\[
                         {|\Gamma_r|\over N_R}
                              =2^{-\Omega(S)}.                   \tag{4.5}
\]

This assignment is integral and uses one complete compiler in every
packet.  It changes no owner.

The affine-conjugate face census implies that, averaged over one complete
batch, the \(q\)-direction set at a uniform start is uniform on
\(\binom{[r]}q\), for each sign.  The one label is common through every
protected depth; only its marginals are being counted here.

## 5. Weighted direction law and anti-localization

For a transversal direction set

\[
                         D=\{i_h:h\in H\},\qquad
                         H\in\binom{[r]}q,\quad i_h\in P_h,       \tag{5.1}
\]

put

\[
                         \pi_q(D)
 ={1\over\binom rq}\prod_{h\in H}p_{h,i_h}.                      \tag{5.2}
\]

Put \(\pi_q(D)=0\) for a nontransversal \(D\).  Equations (3.2), the
compiler batch, and (4.5) prove:

### Theorem 5.1 (integral weighted support design)

For every nonnegative weight \(w\) on physical \(q\)-direction sets, the
normalized weight of the actual depth-\(q\) occurrences emitted by the
cell is

\[
 \boxed{
 {1\over2^S}\sum_{\text{cell occurrences}}w(D)
   =(1+o(1))\sum_D\pi_q(D)w(D),}                                \tag{5.3}
\]

uniformly for both signs.  The error is \(2^{-\Omega(S)}\) for a fixed
depth and support class, and the same integral compiler labels work at
all protected depths.

Now fix \(E\subseteq P_C\) and put

\[
                         \beta_h=\sum_{i\in E\cap P_h}p_{h,i}.   \tag{5.4}
\]

Taking \(w(D)=\mathbf1_{\{D\subseteq E\}}\) gives

\[
 \nu_{C,q}(E)
 =(1+o(1)){e_q(\beta_1,\ldots,\beta_r)\over\binom rq}.           \tag{5.5}
\]

Maclaurin's inequality yields

\[
 {e_q(\boldsymbol\beta)\over\binom rq}
 \le\left({1\over r}\sum_h\beta_h\right)^q.                      \tag{5.6}
\]

The groups have asymptotically equal payload sizes and (1.3) gives

\[
 {1\over r}\sum_h\beta_h
       \le(1+o(1)){|E|\over|P_C|}.                               \tag{5.7}
\]

Equations (5.5)--(5.7) prove (0.1).

The packet-support version is even stronger:

\[
 \Pr\{R(e)\subseteq E\}
                         =\prod_h\beta_h
 \le\left((1+o(1)){|E|\over|P_C|}\right)^r.                      \tag{5.8}
\]

Thus the construction rules out the hypothesis used by the old
localized-axis Hall cut.  It also rules out a subtler strategy in which
most packet supports are global but most chronological \(q\)-windows are
confined to one small carrier.

If \(E_0\) is a set of ground coordinates, apply (5.5) to the cell axes
whose two physical endpoints lie in \(E_0\).  Since the intrinsic split
axes are coordinate-disjoint, their number is at most \(|E_0|/2\).
Hence a ground carrier of size \(\Theta(r)\) also satisfies (0.2).

Summing over all dimension-typical cells and inserting the
\(o(W/H)\)-mass exceptional cells gives the global estimate

\[
 {1\over W_0}\#\{\text{signed occurrences supported in }E_0\}
 \le o(1)+(1+o(1))
       \left({|E_0|\over c m}\right)^q,                           \tag{5.9}
\]

for an absolute \(c>0\).  Thus (5.9) is \(o(1)\) uniformly for every
fixed carrier \(|E_0|=O(r)\).  This is the exact negation of the
concentration premise in the localized-axis counterexample.

## 6. The selected-axis compatibility graph

Fix a sign and depth.  Let \(\mathcal X\) be the retained middle owners
and \(\mathcal T_q^\epsilon\) the corresponding target layer.  Every
owner \(X\) lies in a unique transversal packet \(P(X)\), with active
set \(R(X)\).

Define the selected-axis graph \(\mathcal G_{q,\mathrm{sel}}^\epsilon\)
by

\[
 T\sim_{\rm sel}X
 \quad\Longleftrightarrow\quad
 T\sim_{\rm max}X
 \quad\hbox{and}\quad
 D(T,X)\subseteq R(X),                                           \tag{6.1}
\]

where \(D(T,X)\) is the exact set of touched intrinsic split axes.  On the
lower shore \(T=X\setminus\{\hbox{the occupied endpoints of }D\}\);
above, \(U\) adds the absent endpoints of the same axes.

Every retained owner has exact selected-axis degree

\[
                         d_{\rm sel}(X)=\binom rq                 \tag{6.2}
\]

on each sign.  For an indicator \(y=\mathbf1_{\mathcal A}\), the support
function \(\sum_X\max_{T\sim_{\rm sel}X}y(T)\) is exactly
\(|N_{\rm sel}(\mathcal A)|\).  Thus the desired weighted Hall inequality
is

\[
 \boxed{
                         \sum_Ty(T)
       \le\sum_X\max_{T\sim_{\rm sel}X}y(T)
       \quad\hbox{for every }y\ge0.}                             \tag{6.3}
\]

Indicator weights in (6.3) are exactly Hall.  Equation (0.1) proves
(6.3) for the old exterior-cylinder potentials only after quotienting by
the cell direction law; it does not prove (6.3) for an arbitrary
block-labelled target weight.

## 7. Survival of the Gaussian score reservoir

Use independent local-rank permutations as in the allocation-overlap
construction.  For a typical owner, attach to every intrinsic split axis
the joint one-hit edit score

\[
                         \mathbf R(e)=(R^-(e),R^+(e)),            \tag{7.1}
\]

where the two coordinates are the exact lower look-ahead and upper
look-behind corrections.  Conditional on central half-ranks, this is the
joint difference of three independent hypergeometric counts.  Its
covariance matrix is nonsingular and of order \(d\).  Every fixed bounded
lattice cell therefore has probability

\[
                         \Theta(d^{-1}).                         \tag{7.2}
\]

Choose the group partitions and the balanced maps \(\iota_h\) randomly,
independently of the rank permutations, and then fix a good realization.
For a uniform owner, the selected direction in every group is
\(1+o(1)\) times a uniform payload direction.  Standard
exponential-moment bounds for sampling without replacement give, for
every bounded joint score cell,

\[
                  \#\{e\in R(X):\mathbf R(e)\text{ in the cell}\}
                         =\Theta(r/d)                             \tag{7.3}
\]

for all but \(o(W)\) owners, simultaneously for the finitely many cells
needed below.  A Fubini--Markov argument fixes the cell designs
deterministically.

Under (0.3), even the crude lower bound
\(\Theta(r/d^2)\) on the number of distinct supplying macroblocks is much
larger than \(q\).  The same is true after splitting by occupied endpoint
side.  A random group partition in fact has only \(o(r/d)\) collision
losses in each fixed score reservoir.

### Theorem 7.1 (paired profile reachability after selection)

For all but \(o(W)\) owners, and for every bounded feasible pair
\((z_-,z_+)\) of lower and upper Gaussian carrier values, there is a
\(q\)-subset \(D\subseteq R(X)\), using distinct macroblocks, for which
the paired targets satisfy

\[
                         Z^-(T_D)=z_-+o(1),\qquad
                         Z^+(U_D)=z_++o(1).                       \tag{7.4}
\]

The numbers of touched \(A\)- and \(C\)-side endpoints can be prescribed
as well.

#### Proof

The exact carrier-edit identities give

\[
 \begin{aligned}
 Z^-(T_D)&=L^-(X)+{4\over\sqrt m}\sum_{e\in D}R^-(e)+o(1),\\
 Z^+(U_D)&=L^+(X)+{4\over\sqrt m}\sum_{e\in D}R^+(e)+o(1).
 \end{aligned}                                                   \tag{7.5}
\]

The desired average joint score is the bounded vector

\[
 {1\over4A}\bigl(z_--L^-(X),z_+-L^+(X)\bigr).                   \tag{7.6}
\]

Choose three or four bounded lattice cells whose convex hull contains
(7.6), and take the required integral mixture of \(q\) axes from the
reservoirs (7.3).  Rounding changes the average by \(O(1/q)\); the local
centering offsets are \(o(1)\).  Since each reservoir has
 \(\Theta(r/d)\) axes and no macroblock supplies more than \(O(d)\)
of them, the axes can be chosen in distinct macroblocks.  Insert the
result in (7.5). \(\square\)

This proves that the selected-axis operation does not reintroduce the
fixed-allocation Gaussian profile deficit.  Combining Theorem 7.1 with
the ordinary half-profile flow gives, for either sign, the same
\(e^{A^2}-o(1)\) weighted Hall expansion for weights constant on the safe
empirical half-rank/carrier profiles.  With the common block-imbalance
tag retained, Theorem 7.1 also supplies joint reachability of every
feasible signed profile pair.  The full additive paired-weight inequality
is still the compiler dual in Section 9.  None of these statements is
(6.3) for arbitrary literal weights.

### Corollary 7.2 (selected-axis profile Hall)

Let \(y^\epsilon\ge0\) be constant on the safe empirical
half-rank/carrier cells, including the residual tag.  Separately for
\(\epsilon=-,+\),

\[
 \boxed{
 \sum_{T\in\mathcal T_q^\epsilon}y^\epsilon(T)
 \le\bigl(e^{-A^2}+o(1)\bigr)
 \sum_{X\in\mathcal X}
 \max_{\substack{D\subseteq R(X)\\|D|=q}}
 y^\epsilon(T_D^\epsilon).}                                    \tag{7.7}
\]

The coefficient is strictly below one for fixed \(A>0\).  Theorem 7.1
also says that any *feasible* pair of signed carrier cells with the common
block-imbalance tag can be reached using the same \(D\).  Equation (7.7)
does not assert the full joint additive-weight dual, because separately
maximizing lower and upper profiles may request incompatible imbalance
tags.  That coupling is retained explicitly in (9.4).

## 8. Why a maximal raw injection does not automatically lift

Suppose a maximal-graph injection assigns to each target \(T\) a distinct
source \(X(T)\) and touched set \(D(T)\).  A packet \(P\) can retain all
of these assigned incidences only if

\[
                         \left|\bigcup_{X(T)\in P}D(T)\right|
                              \le r.                              \tag{8.1}
\]

Condition (8.1) is necessary before chronology is considered.  It is not
a consequence of injectivity.

Indeed, after any packet tiling is fixed, choose
\(k=\lfloor r/q\rfloor+1\) owners of one packet and give them pairwise
disjoint legal touched \(q\)-sets in the ambient product cell.  Their
sources are distinct and their assigned targets can be chosen distinct,
so this is a valid fragment of a maximal raw injection.  But the union
of the requirements has size \(kq>r\), and that fixed packet cannot retain
the fragment.  This obstructs lifting an arbitrary already chosen
injection through a packet grouping; it is not a no-go against choosing a
new coherent injection together with the tiling.

Thus the logical bridge

\[
                         \text{maximal raw injection}
 \Longrightarrow\text{selected-axis injection}                  \tag{8.2}
\]

is false without a coherence theorem.  The transversal construction
supplies a favorable selected graph in which a new injection may exist;
it cannot repair an arbitrary injection already chosen.

## 9. Compiler configurations and the exact remaining dual

For every transversal packet \(P\) and legal affine compiler conjugate
\(g\), define the paired configuration

\[
 \mathcal A_{P,g,q}
 =\{(T^-_{P,g,q}(x),T^+_{P,g,q}(x)):x\in P\}.                   \tag{9.1}
\]

Trace recovery makes each signed projection injective.  Lemma 3.1 makes
the projections from different packets of one product cell disjoint.

Choosing one compiler in every packet means

\[
                         x_{P,g}\in\{0,1\},\qquad
                         \sum_gx_{P,g}=1.                         \tag{9.2}
\]

For one depth, literal signed loads are

\[
 L_q^\epsilon(T)=\sum_{P,g,x}
 x_{P,g}\mathbf1_{\{T^\epsilon_{P,g,q}(x)=T\}}.                 \tag{9.3}
\]

The fractional cover condition has the exact weighted Hall dual: for
every real signed target weight pair \(\lambda^-,\lambda^+\),

\[
 \boxed{
 \sum_P\min_g\sum_{x\in P}
 \bigl(\lambda^-(T^-_{P,g,q}(x))
       +\lambda^+(T^+_{P,g,q}(x))\bigr)
 \le h_{\mathcal B_q}(\lambda^-,\lambda^+),}                    \tag{9.4}
\]

where \(h_{\mathcal B_q}\) is the support function of the two translated
quota hypersimplices.  Explicitly, for either sign,

\[
 h_{\mathcal B_q^\epsilon}(\lambda)
 =h_q\sum_T\lambda(T)
   +\sum_{\text{\(R_q\) largest }\lambda(T)}\lambda(T),          \tag{9.5}
\]

with
\[
 h_q=\left\lfloor{W_0\over N_q}\right\rfloor,\qquad
 R_q=W_0-h_qN_q.
\]

The same \(g\) occurs in the two signed terms in (9.4).  At several
depths, all their weights are inserted inside the same minimum.

The integral compiler batching of Section 4 proves the direction-weight
identities (5.3) and eliminates every exterior-cylinder dual whose
deficit mechanism is confinement of almost all \(q\)-supports to one
localized \(E\).  It does not prove (9.4) for an arbitrary literal
target array, because a target
decodes its unique packet face and different product cells can still
collide.  Nor does fractional feasibility imply the integral
multiple-choice system (9.2).

## 10. Certified boundary

Proved:

1. an exact, nonparallel, owner-preserving \(Q_r\)-tiling of every good
   product cell;
2. asymptotically uniform transversal packet supports;
3. within-cell literal trace recovery;
4. an integral compiler deployment satisfying the weighted direction
   design at both signs and every protected depth;
5. the sharp anti-localization bound (0.1);
6. survival of the joint lower/upper Gaussian score reservoir; and
7. selected-axis Hall expansion for admissible Gaussian profile weights.

Not proved:

1. (6.3) for arbitrary block-labelled target weights;
2. an arbitrary raw selected-axis injection;
3. the literal compiler configuration inequality (9.4); or
4. integral all-target quota balancing.

Accordingly, the localized-\(E\) obstruction is removed while preserving
the exact owner tiling.  The remaining constant-one gate is a
block-labelled selected-axis/configuration Hall theorem, not axis
dispersion.

## 11. Subsequent cross-profile and packet-union audit

`MATH_THEOREM_OVERLAP_COMPRESSION_CROSS_PROFILE_AND_PACKET_UNION_CUT_20260726.md`
tests the proposed combination with the overlap-stratum compression
theorem.  It proves two sharp qualifications.

First, even exact Hall on whole profiles together with expansion by an
arbitrarily large factor \(K\) for every raw subfamily inside each profile
does not imply raw Hall: an explicit construction has a raw neighborhood
ratio exactly \(1/2\).  Thus the missing statement is cross-profile source
overlap control, not another within-profile compression.

Second, a probabilistic face construction gives a near-spanning injective
raw assignment for which every coordinate \(Q_R\)-packetization retains at
most

\[
                 (2+o(1)){\binom Rq\over\binom Sq}=o(1)
\]

of the assigned incidences.  Hence the maximal raw injection cannot be
chosen first and made coherent afterward.  This strengthens Section 8
from a finite fragment to a near-spanning simultaneous obstruction.  It
is allocation/cell-labelled, so a literal construction may still escape
by quotienting alternative cell labels and rerouting before Hall.  The
cross-parent \(Q_{R+1}\)-slab trades in the subsequent CPCR synthesis are
exactly such a possible re-atlasing operation and lie outside the
frozen-parent hypothesis of the cut.  Once a matching is built directly
in the fixed selected-axis graph, the union condition is automatic.
Condition (9.4) is then only an intermediate one-depth configuration
dual.  The authoritative common all-depth target is CPCR in
MATH_EXACT_REMAINING_CROSS_PARENT_COMPILER_RESOLUTION_20260726.md.
Neither the cut nor CPCR reopens common-order syndrome or within-packet
injectivity.
