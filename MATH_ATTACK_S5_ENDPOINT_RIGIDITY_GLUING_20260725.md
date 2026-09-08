# Fifth-wave S: endpoint near-equality, rank ladders, and cross-parent gluing

Date: 2026-07-25

## 0. Verdict

This report goes beyond the leading three-box lower bound in two
directions.

First, the endpoint-potential proof has an exact nonnegative slack
decomposition.  It completely classifies formal equality and shows that
formal equality is impossible for every fixed band profile with a
positive quadratic certificate, including profiles on the width boundary
\(c=a+b\).  More quantitatively, if \(Q_t\) is the quadratic certificate
of the chosen band profile (in particular, it may be the optimized
certificate), then every literal word satisfies

\[
\boxed{
g_3(p_t,q_t,r_t)-(p_t+1)(q_t+1)
\ge Q_t+\Omega(t^{5/3})}                                   \tag{0.1}
\]

on every fixed plateau ray and every fixed band profile whose certificate
has a positive quadratic coefficient.  The
\(t^{5/3}\) term is subquadratic, so it does not change the sharp leading
functional from the third-wave report; it proves that its exact equality
geometry is empty.

Second, simultaneous near-equality across product parents has a genuine
global rigidity consequence.  Product-box bands arising from symmetric
shoulders are centered at the same Boolean middle rank.  At one physical
endpoint, targets from all parents form one global inclusion chain and
there is at most one target per global rank.  If the local layer slack is
small, then:

- endpoint degree greater than two costs one full common-band unit of
  slack per extra parent;
- a degree-two endpoint with zero layer slack must alternate the two
  parents at successive ranks; and
- the two parents must agree in two factor chains and differ in exactly
  one.  Their traces form a Boolean diamond ladder in that coordinate
  block.

Thus the only zero restricted-layer-slack cross-parent templates are
single-parent flags and two-parent parity ladders: three coordinate-block
orientations, with two parity phases when the parents are labelled.  Near
equality allows broken versions of these templates, with every break
charged at least once (and at most twice in the restricted two-parent
ledger).  The aggregate theorem controls the density of breaks among
endpoint--rank transitions; it does not say that all but \(o(W)\)
degree-two endpoints are completely break-free.

This rigidity is conditional on near-minimal aggregate endpoint incidence.
A near-width global word is not known to satisfy that condition.  Indeed,
arbitrarily long isolated symmetric diamond rails are explicit, but their
extension and dense packing inside one full factor SCD are not proved.
Independently, static high-degree double flags are constructible at the sharp
\(\Theta(W/\sqrt k)\)-portal scale and carry \(\Theta(W)\) useful
endpoint--box incidence.  They necessarily pay leading-order local layer
slack if extended to common full bands, and isolated realizations cost
\(\Theta(W)\) arm positions.  What remains open is middle-productive
dynamic fusion of the diffuse parity
ladders or of the high-slack global portals.

Finally, endpoint chains and their common cores are not sufficient for a
literal global word.  An exact coordinate-threshold safe-point theorem is
proved below; it isolates the additional interval-union consistency which
all parents must satisfy simultaneously.

No web search, finite search, or computational search was used.  The slack
identity, calculus scales, global rank-packing theorem, and double-flag
construction were independently audited.

## 1. Exact local slack identity

Let \(g_3(p,q,r)\) denote the least length of a word over nonzero
three-coordinate box letters whose contiguous coordinatewise maxima
contain every nonzero point of
\([0,p]\times[0,q]\times[0,r]\).

Let

\[
1\le p\le q,\qquad P=p+q,\qquad r\ge P,\qquad
W=(p+1)(q+1).
\]

Choose lower and upper shoulder depths \(u,v\), and retain the consecutive
rank band

\[
P-u,\ldots,r+v.
\]

Put

\[
H=r-P,\qquad J=H+u+v,\qquad \Lambda=J+P=r+u+v.             \tag{1.1}
\]

For completeness, let

\[
f_j=\#\{(x,y)\in[0,p]\times[0,q]:x+y=j\},
\]

\[
F_k=\sum_{j<k}f_j,\qquad
L_k=\sum_{j<k}j f_j,\qquad
G_k=\sum_{i=1}^{k}F_i,
\]

and

\[
\mathcal R_k=-3G_k+2(1-P)F_k+2L_k.                         \tag{1.2}
\]

The raw band numerator is

\[
\mathcal N=JW+\mathcal R_u+\mathcal R_v.                   \tag{1.3}
\]

The two boundary layer sizes, total target count, and vertical capacity
are

\[
M_-=W-F_u,\qquad M_+=W-F_v,                                \tag{1.4}
\]

\[
T=(J+1)W-G_u-G_v,\qquad
A_{\rm vert}=JW-G_u-G_v.                                   \tag{1.5}
\]

Let a literal universal word have length

\[
n=W+D.
\]

Choose one witness for every target in the band and form either the left-
or right-endpoint chain partition \(\mathcal C\).  Let \(C\) be its number
of nonempty chains.  Index the band layers by \(0,\ldots,J\).  For a chain
\(Q\), let

\[
S_Q\subseteq\{0,\ldots,J\}
\]

be its rank support.

### 1.1 The four one-partition slacks

Define the unused-endpoint slack

\[
\epsilon(\mathcal C)=n-C.                                  \tag{1.6}
\]

Define the layer slack

\[
\alpha(\mathcal C)
=
\sum_{i=0}^{J-1}
\#\{Q:i,i+1\notin S_Q\}.                                   \tag{1.7}
\]

Let consecutive selected targets \(X<Y\) in one chain be a gap pair when
their rank difference is at least two.  With

\[
\phi(x,y,z)=x+y,
\]

define the skipped-potential slack

\[
\kappa(\mathcal C)
=
\sum_{\text{gap pairs }X<Y}
\bigl(\phi(Y)-\phi(X)\bigr).                                \tag{1.8}
\]

Finally define the endpoint-corner slack

\[
\beta(\mathcal C)
=
\sum_{\substack{Q\\0\notin S_Q}}\phi(\min Q)
+
\sum_{\substack{Q\\J\notin S_Q}}
\bigl(P-\phi(\max Q)\bigr).                                \tag{1.9}
\]

All four quantities are nonnegative integers.

For the left and right partitions, let

\[
Z_{\mathcal L},Z_{\mathcal R}
\]

be their sets of vertical target-poset cover edges.  Orthogonality makes
these sets disjoint.  Define the unused vertical capacity

\[
\omega
=A_{\rm vert}-|Z_{\mathcal L}|-|Z_{\mathcal R}|
\ge0.                                                      \tag{1.10}
\]

### Theorem 1.1 — master slack identity

The exact identity is

\[
\boxed{
\begin{aligned}
2\Lambda D-\mathcal N
={}&
\Lambda\bigl(\epsilon(\mathcal L)+\epsilon(\mathcal R)\bigr)
+\alpha(\mathcal L)+\alpha(\mathcal R)\\
&+\kappa(\mathcal L)+\kappa(\mathcal R)
+\beta(\mathcal L)+\beta(\mathcal R)
+\omega .
\end{aligned}}                                             \tag{1.11}
\]

#### Proof

Let \(S_i\) be the set of chains meeting layer \(i\), whose size is the
layer size \(m_i\).  The exact number of adjacent-rank covers used by one
partition is

\[
\sum_{i=0}^{J-1}|S_i\cap S_{i+1}|.
\]

Since

\[
|S_i\cap S_{i+1}|
=m_i+m_{i+1}-C
  +\#\{Q:i,i+1\notin S_Q\},
\]

this cover count is exactly

\[
2T-M_--M_+-JC+\alpha(\mathcal C).                          \tag{1.12}
\]

Let \(\Phi(\mathcal C)\) be the total \(\phi\)-rise from the minimum to
the maximum of every chain.  The boundary-mass calculation from the sharp
dual gives

\[
\Delta_\phi=PF_u-L_u-L_v.
\]

There are \(C-M_+\) internal chain ends.  Direct telescoping gives the
identity

\[
\Delta_\phi+P(C-M_+)-\Phi(\mathcal C)
=\beta(\mathcal C).                                        \tag{1.13}
\]

Every adjacent horizontal cover contributes one unit of \(\phi\), every
adjacent vertical cover contributes zero, and all remaining \(\phi\)-rise
comes from the gap pairs.  Thus

\[
\Phi(\mathcal C)
=\#\{\text{horizontal covers used by }\mathcal C\}
 +\kappa(\mathcal C).                                      \tag{1.14}
\]

Subtracting horizontal covers from (1.12), and using
(1.13)--(1.14), gives the exact vertical count

\[
\begin{aligned}
|Z_{\mathcal C}|
={}&
2T-M_--M_+-\Delta_\phi+PM_+-\Lambda C\\
&+\alpha(\mathcal C)+\kappa(\mathcal C)+\beta(\mathcal C).
\end{aligned}                                              \tag{1.15}
\]

Sum (1.15) for the two endpoint partitions, insert

\[
C_{\mathcal L}+C_{\mathcal R}
=2n-\epsilon(\mathcal L)-\epsilon(\mathcal R),
\]

and use (1.10).  The constant term simplifies exactly to
\(\mathcal N\), proving (1.11). \(\square\)

### 1.2 Endpoint-incidence form

For cross-parent gluing, the word length should be eliminated.  Put

\[
e_\partial
=(C_{\mathcal L}-W)+(C_{\mathcal R}-W).
\]

Canceling the \(\epsilon\)-terms in (1.11) gives

\[
\boxed{
\Lambda e_\partial-\mathcal N
=
\sum_{\mathcal C=\mathcal L,\mathcal R}
\bigl(\alpha(\mathcal C)+\kappa(\mathcal C)+\beta(\mathcal C)\bigr)
+\omega.}                                                  \tag{1.16}
\]

This identity holds for witnesses cut from an arbitrary global word; no
local subword or local word length is required.

## 2. Equality and near equality inside one parent

### 2.1 Complete formal equality conditions

Equality in the unrounded word-length certificate means that every term
on the right of (1.11) is zero.  This is equivalent to all of the
following.

1. **Endpoint saturation.**

   \[
   C_{\mathcal L}=C_{\mathcal R}=n.
   \]

   Every physical position is used as a selected left endpoint and as a
   selected right endpoint.

2. **Rank domination.**  The complement of every chain support \(S_Q\)
   has no two consecutive ranks.  Equivalently, every chain meets at least
   one layer from every adjacent layer pair.

3. **Pure vertical gaps.**  Consecutive targets of one chain which skip a
   layer have the same \(x,y\).  Rank domination then forces every such
   rank gap to be exactly two.

4. **Corner endpoints.**  Every chain which starts internally begins at
   \(\phi=0\), and every chain which ends internally ends at \(\phi=P\).

5. **Exact vertical ownership.**  The two endpoint partitions divide all
   vertical band covers between them; none is unused.

These conditions are necessary and sufficient for the right side of
(1.11) to vanish.  They do not yet assert that a physical word realizing
the selected intervals exists.  There is also the arithmetic prerequisite

\[
2\Lambda\mid\mathcal N,                                  \tag{2.0}
\]

because formal equality has \(D=\mathcal N/(2\Lambda)\) and \(D\) is an
integer.  If one instead compares with the rounded bound
\(D\ge\lceil\mathcal N/(2\Lambda)\rceil\), a nonzero ceiling remainder is
itself positive slack and the five zero conditions cannot all hold.

### 2.2 Equality is empty on every positive ray

Rank domination forces an internally starting chain to start in the first
layer above the bottom: otherwise it misses both layers of the first
transition.  Corner equality then forces it to use the unique possible
target with \(\phi=0\) in that layer.  Hence there is at most one internal
start.  The top argument is complementary.  Since

\[
C_{\mathcal L}=n=W+D,
\]

while the boundary sizes are \(W-F_u,W-F_v\), zero slack requires

\[
\boxed{
D+F_u\le\mathbf 1_{H+u>0},
\qquad
D+F_v\le\mathbf 1_{H+v>0}.}                                \tag{2.1}
\]

In particular, \(D\le1\) and \(u,v\le1\).  A positive fixed-ray
certificate has \(D=\Theta(t^2)\), so equality is impossible.

In the remaining tiny finite cases, the two partitions still have to own
every vertical edge.  When both have the unique layer-one corner entrance,
the incoming vertical edge at that corner is used by neither, so even the
formal corner conditions do not automatically produce coupled equality.

### 2.3 Exact entrance-energy bound

For a chain beginning internally at relative layer \(i\), define its
start-corridor cost

\[
c_-=i-1+\phi(\min Q).
\]

For a chain ending internally at relative layer \(i\), define

\[
c_+=J-i-1+P-\phi(\max Q).
\]

The leading and trailing pairs of missed layers are disjoint, so

\[
\alpha(\mathcal C)+\beta(\mathcal C)
\ge
\sum_{\rm internal\ starts}c_-
+\sum_{\rm internal\ ends}c_+.                             \tag{2.2}
\]

For \(1\le K\le p+1\), at most

\[
\binom{K+2}{3}
\]

possible band targets have start-corridor cost below \(K\).  Indeed, put
\(d=i-1\).  The condition \(d+\phi<K\) lies in the untruncated triangular
corner, where there are \(\phi+1\) targets of potential \(\phi\), and

\[
\sum_{\phi=0}^{K-1}(K-\phi)(\phi+1)
=\binom{K+2}{3}.
\]

The same bound holds at the upper corner.  Define

\[
\Psi_p(N)
=
\max_{1\le K\le p+1}
K\left(N-\binom{K+2}{3}\right)_+.                          \tag{2.3}
\]

The internal-start targets are pairwise distinct, as are the
internal-end targets (a singleton chain may occur once in each list).
Therefore the two lists may be charged separately in (2.2), giving

\[
\boxed{
\alpha(\mathcal C)+\beta(\mathcal C)
\ge
\Psi_p(C-M_-)+\Psi_p(C-M_+).}                              \tag{2.4}
\]

There is a sharper exact order-statistic form.  Set \(\rho_3(0)=0\).  For
\(N\ge1\), let \(h=h(N)\) be the unique nonnegative integer satisfying

\[
\binom{h+2}{3}<N\le\binom{h+3}{3},                        \tag{2.4a}
\]

and put

\[
\rho_3(N)
=3\binom{h+2}{4}
 +h\left(N-\binom{h+2}{3}\right).                         \tag{2.4b}
\]

The number of ideal, untruncated corner targets of cost exactly \(j\) is
\(\binom{j+2}{2}\), and the actual truncated box has no more.  Filling
the lowest ideal cost shells first therefore gives the exact universal
order-statistic bound

\[
\boxed{
\alpha(\mathcal C)+\beta(\mathcal C)
\ge
\rho_3(C-M_-)+\rho_3(C-M_+).}                             \tag{2.4c}
\]

Here

\[
\sum_{j=0}^{h-1}j\binom{j+2}{2}
=3\binom{h+2}{4},
\]

which proves (2.4b) including its constant.  As \(N\to\infty\),

\[
\rho_3(N)
=\left(\frac34\,6^{1/3}+o(1)\right)N^{4/3}.               \tag{2.4d}
\]

For \(N=\Theta(t^2)\) and \(p=\Theta(t)\), choosing
\(K=\Theta(N^{1/3})\) gives

\[
\Psi_p(N)=\Omega(t^{8/3}).                                 \tag{2.5}
\]

### Theorem 2.1 — subleading separation from the sharp dual

Fix positive ratios, take any corresponding sufficiently large integer
ray sequence, and fix a band profile for which

\[
\Lambda=\Theta(t),\qquad
Q_t:=\frac{\mathcal N}{2\Lambda}\ge c_0t^2
\]

for some fixed \(c_0>0\) (and hence \(Q_t=\Theta(t^2)\)).  Choose a
fixed \(\lambda_+\) such that \(\Lambda\le\lambda_+t\) for all
sufficiently large \(t\), and set

\[
\gamma_3=\frac34\,6^{1/3},\qquad
K_0=\min\left\{
1,\frac{c_0}{4},
\frac{\gamma_3}{4\lambda_+}
\left(\frac{c_0}{2}\right)^{4/3}
\right\}.                                                 \tag{2.5a}
\]

Then, for all sufficiently large \(t\), every universal word satisfies

\[
\boxed{D\ge Q_t+K_0t^{5/3}.}                              \tag{2.6}
\]

#### Proof

The master identity first gives \(D\ge Q_t\).  If
\(D\ge Q_t+t^2\), then (2.6) is immediate because \(K_0\le1\).  It
remains to treat \(Q_t\le D<Q_t+t^2\), where
\(D=\Theta(t^2)\).

For either endpoint partition,

\[
C-M_-=D+F_u-\epsilon(\mathcal C).
\]

Here \(D+F_u=\Theta(t^2)\).  If
\(\epsilon(\mathcal C)\ge(D+F_u)/2\), the unused-endpoint term in
(1.11) gives

\[
D-Q_t\ge\frac{\epsilon(\mathcal C)}2
\ge\frac{c_0}{4}t^2
\ge K_0t^{5/3}.
\]

Otherwise

\[
C-M_-\ge\frac{D+F_u}{2}\ge\frac{c_0}{2}t^2.
\]

By (2.4c)--(2.4d), for all sufficiently large \(t\),

\[
\alpha(\mathcal C)+\beta(\mathcal C)
\ge
\frac{\gamma_3}{2}
\left(\frac{c_0}{2}\right)^{4/3}t^{8/3}.                 \tag{2.6a}
\]

Since

\[
2\Lambda(D-Q_t)=\text{total slack},
\]

equation (2.6a) and \(\Lambda\le\lambda_+t\) give

\[
D-Q_t
\ge
\frac{\gamma_3}{4\lambda_+}
\left(\frac{c_0}{2}\right)^{4/3}t^{5/3}
\ge K_0t^{5/3}.
\]

This proves (2.6). \(\square\)

The same proof works with the upper boundary if it is more convenient.
All constants may depend on the fixed ratios and band profile.

### Corollary 2.2 — local leading-order stability

Under the hypotheses of Theorem 2.1, suppose more generally that

\[
D-Q_t=o(t^2).                                             \tag{2.7}
\]

Then

\[
\epsilon(\mathcal L)+\epsilon(\mathcal R)=o(t^2),         \tag{2.8}
\]

and

\[
\sum_{\mathcal C=\mathcal L,\mathcal R}
(\alpha(\mathcal C)+\kappa(\mathcal C)+\beta(\mathcal C))
+\omega=o(t^3).                                           \tag{2.9}
\]

In particular, only \(o(t^3)\) chain--transition pairs miss both adjacent
layers, all but \(o(t^3)\) vertical covers are owned by one of the two
partitions, and the total transverse potential accumulated in skipped-rank
gaps is \(o(t^3)\).  Moreover, for every fixed \(\eta>0\), only
\(o(t^2)\) internal starts have

\[
i-1+\phi(\min Q)\ge\eta t,
\]

and only \(o(t^2)\) internal ends have the complementary corridor cost at
least \(\eta t\).

#### Proof

By (1.11), the total slack equals
\(2\Lambda(D-Q_t)=o(t^3)\).  Every summand is nonnegative, and
\(\Lambda=\Theta(t)\), giving (2.8)--(2.9).  The first three conclusions
are the definitions of \(\alpha,\omega,\kappa\).  The last follows from
(2.2) and Markov's inequality for the nonnegative corridor costs.
\(\square\)

This is stability only in aggregate.  Defects may concentrate on a small
set of chains, ranks, or columns, and the conclusion supplies neither a
physical endpoint alignment nor a realizing word.

## 3. Local anti-rigidity: equality data do not select a small family

The empty coupled equality geometry does not mean that the scalar
rank/potential data determine canonical endpoint patterns.  They do not.

Consider a flat band with only two plateau layers:

\[
H=1,\qquad u=v=0,\qquad
Q=[0,p]\times[0,q],\qquad
B=(p+1)(q+1).
\]

Fix any saturated monotone path

\[
\pi:\quad z_0=(0,0)<z_1<\cdots<z_P=(p,q)
\]

in \(Q\).  Make \(B+1\) abstract endpoint chains:

- one top-only chain at \(z_0\);
- one bottom-only chain at \(z_P\);
- for \(0\le i<P\), a chain pairing bottom \(z_i\) with top
  \(z_{i+1}\); and
- a vertical pair at every off-path base point.

This partitions both layers.  For this one endpoint partition,

\[
\alpha=\beta=\kappa=0.
\]

Every path has the same rank profile, corner endpoints, potential increase,
and number of vertical covers.  Nevertheless there are

\[
\boxed{\binom{p+q}{p}}
\]

such patterns.  Their only difference is the order of the \(x\)- and
\(y\)-increments.

Thus the endpoint-potential equality data leave exponentially many fixed
labelled local patterns and do not select a canonical pattern or a
polynomial-size list of such fixed patterns.  This does not rule out a
short parametrized schema such as ``choose an arbitrary monotone path.''

### Theorem 3.1 — exact two-layer path-cover rigidity

More generally, let one endpoint partition of the two-layer band have

\[
C=B+\delta,\qquad 0\le\delta\le B
\]

chains.  After identifying the two copies of \(Q\), its nonvertical
matched covers form \(\delta\) pairwise vertex-disjoint directed monotone
paths; every vertex outside those paths carries its vertical loop.
Conversely, every such path family gives an endpoint partition.

Let

\[
a_s=\#\{z\in Q:|z|=s\},\qquad 0\le s\le P.
\]

Then

\[
\boxed{
\beta
\ge
\sum_{s=0}^{P-1}
\bigl(\delta-\min\{\delta,a_s,a_{s+1}\}\bigr).}           \tag{3.1}
\]

For \(0\le\delta\le p+1\), this simplifies to the sharp inequality

\[
\boxed{\beta\ge\delta(\delta-1).}                         \tag{3.2}
\]

#### Proof

A chain has at most one point in each of the two layers.  Identifying the
layers turns every two-point chain into either a loop or a directed cover
of \(Q\).  Each vertex has indegree and outdegree at most one.  There are
exactly \(\delta\) unmatched points on each layer, so the nonloop
components are exactly \(\delta\) disjoint directed paths, with singleton
paths allowed.  Conversely, for each nontrivial path pair each vertex to
its successor, place a top-only chain at its first vertex and a bottom-only
chain at its last vertex, use two singleton chains for a singleton path,
and put a vertical pair at every off-path vertex.

If \(h\) is their total number of directed covers, the corner-slack
definition telescopes along the paths to

\[
\beta=P\delta-h.                                          \tag{3.3}
\]

At most one edge of each path crosses from base rank \(s\) to \(s+1\),
and vertex disjointness gives at most
\(\min\{\delta,a_s,a_{s+1}\}\) such edges.  Summing this bound in (3.3)
proves (3.1).  When \(\delta\le p+1\), the two triangular tails of the
rank sequence each contribute \(\delta(\delta-1)/2\), proving (3.2).

Sharpness is witnessed by the \(\delta\) disjoint paths

\[
(0,k)\longrightarrow(p-k,k)\longrightarrow(p-k,q),
\qquad 0\le k<\delta,                                     \tag{3.4}
\]

where each arrow denotes the saturated coordinate path.  The \(k\)-th
path has corner slack \(2k\), and their sum is
\(\delta(\delta-1)\). \(\square\)

In particular, the one-partition zero-slack patterns with \(\delta=1\)
are exactly the corner-to-corner monotone paths constructed above.  Thus
the exponential family is a complete two-layer one-sided equality
classification, not merely a collection of examples.

These are abstract one-partition patterns, not coupled literal words.  Two
\(\delta=1\) zero-slack partitions would also have to use disjoint vertical
edges.  Their two monotone-path supports would have to cover all \(B\) base
vertices, which two paths cannot do when

\[
B>2(P+1).
\]

This cleanly separates one-sided anti-rigidity from the coupled and
literal gluing problem.

## 4. Global near-equality forces low degree and broken parity ladders

Now let \(k=3s\) be even, put \(m=k/2\), and fix SCDs in the three coordinate blocks.
Their products partition the Boolean cube into product parents.

For each selected parent \(\mathcal B\), use a symmetric local shoulder
band.  Symmetry of the three factor chains translates this local band to a
global rank interval centered at \(m\).  Suppose all chosen bands contain
the common transition interval

\[
\mathcal I_0
=\{m-h_0,m-h_0+1,\ldots,m+h_0-1\},
\qquad L=2h_0.                                             \tag{4.1}
\]

For compact fixed-ratio parent windows, \(L=\Theta(\sqrt k)\).

Fix one endpoint side \(\sigma\in\{\mathcal L,\mathcal R\}\) and one
physical position \(j\).  Let \(S_{\mathcal B,j}^{\sigma}\) be the set of
global ranks at which the endpoint chain at \(j\) owns a selected target
of parent \(\mathcal B\).  Put

\[
a_{\mathcal B,j}^{\sigma}
=
\mathbf 1_{\{S_{\mathcal B,j}^{\sigma}\ne\varnothing\}}
\#\{r\in\mathcal I_0:
r,r+1\notin S_{\mathcal B,j}^{\sigma}\}.                   \tag{4.2}
\]

Thus an unrepresented parent has \(a_{\mathcal B,j}^{\sigma}=0\); the
quantity is defined only to charge an actual nonempty endpoint chain.

The sum over \(j\) of these restricted missing-pair counts is at most the
full local layer slack:

\[
\sum_j a_{\mathcal B,j}^{\sigma}
\le\alpha_\sigma(\mathcal B).                              \tag{4.3}
\]

Let

\[
d_j^\sigma
=\#\{\mathcal B:S_{\mathcal B,j}^{\sigma}\ne\varnothing\}. \tag{4.4}
\]

### Theorem 4.1 — cross-parent rank-packing inequality

For either endpoint side,

\[
\boxed{
L\sum_j(d_j^\sigma-2)_+
\le
\sum_{\mathcal B}\alpha_\sigma(\mathcal B).}               \tag{4.5}
\]

#### Proof

At a fixed endpoint, all represented Boolean targets form one strict
inclusion chain.  Hence at one global rank there is at most one target,
irrespective of its product parent.

Fix one transition \(r,r+1\in\mathcal I_0\), and consider only the
\(d_j^\sigma\) represented parents.  Such a parent avoids contributing to
\(a_{\mathcal B,j}^\sigma\) at this transition precisely when its chain
owns a target at rank \(r\) or \(r+1\).  There are only two available rank
slots, so at most two represented parents can avoid the missing-pair
charge.  Thus, for fixed \(j\),

\[
\sum_{\mathcal B}a_{\mathcal B,j}^\sigma
\ge L(d_j^\sigma-2)_+.
\]

Sum over \(j\) and use (4.3). \(\square\)

This theorem is independent of product-box adjacency, interval pins, and
the detailed potential ledger.  It uses only common centered ranks and the
one-target-per-rank endpoint rule.

### 4.1 Exact degree-two classification

Suppose \(d_j^\sigma=2\), with parents \(\mathcal B,\mathcal B'\), and

\[
a_{\mathcal B,j}^\sigma
=a_{\mathcal B',j}^\sigma=0.                               \tag{4.6}
\]

At every transition of \(\mathcal I_0\), each parent must occupy one of the
two ranks.  The two targets are distinct and one endpoint chain has at most
one target at a rank.  Therefore the parents alternate exactly:

\[
\boxed{
\mathcal B,\mathcal B',\mathcal B,\mathcal B',\ldots}
\quad\text{or}\quad
\boxed{
\mathcal B',\mathcal B,\mathcal B',\mathcal B,\ldots .}     \tag{4.7}
\]

More generally, let \(b_j^\sigma\) be the number of transitions of
\(\mathcal I_0\) on which at least one of the two parents misses both
endpoint ranks.  Deleting those transitions breaks the common interval
into at most \(b_j^\sigma+1\) pieces, and on every remaining piece the
same parity alternation holds; its phase may restart independently after
each deleted transition.  Moreover,

\[
b_j^\sigma
\le
a_{\mathcal B,j}^\sigma+a_{\mathcal B',j}^\sigma
\le2b_j^\sigma.                                          \tag{4.6a}
\]

Thus the restricted layer ledger charges the distinct ladder breaks,
within a factor of two.  The full \(\alpha\)-ledger can additionally
charge transitions outside \(\mathcal I_0\) and chains at other
endpoints.

Successive targets in (4.7) are comparable Boolean sets of consecutive
ranks, hence form Boolean covers.  A Boolean cover changes exactly one of
the three coordinate blocks.  The unchanged block components lie in the
same unique factor chains.  Since the two product parents are fixed and
distinct, they agree in two factor chains and differ in exactly one.
Every cover in the alternating segment changes that same coordinate block.

Consequently, inside the differing block, the two factor chains form the
two rails of a sequence of Boolean diamonds.  The other two block
components stay fixed.  Explicitly, two same-parent vertices two ranks
apart have the unique intermediate vertex belonging to their saturated
factor chain; the alternating other-parent vertex is the second
intermediate vertex between the same bottom and top, so the four vertices
form a Boolean diamond.  This literal diamond assertion needs two
consecutive transitions (\(L\ge2\)); for \(L=1\), (4.7) is merely the
single alternating cover.  Up to swapping the two parents, there are
exactly three coordinate orientations.  For labelled parents there are
three orientations and two parity phases.

This is the promised small structural rank-monotone template theorem:

\[
\boxed{
\text{zero restricted-layer-slack global sharing is either one-parent or a two-parent
parity ladder.}}                                           \tag{4.8}
\]

It is a global theorem.  Section 3 shows why no analogous finite
classification follows from the scalar local ledger alone.

### 4.2 Aggregate near-equality corollary

For parent \(\mathcal B\), put

\[
e_{\mathcal B}
=C_{\mathcal L}(\mathcal B)+C_{\mathcal R}(\mathcal B)
 -2W_{\mathcal B},
\]

and let \(\mathfrak S_{\mathcal B}\) be the right side of the
endpoint-incidence identity (1.16).  Then

\[
e_{\mathcal B}
=\frac{\mathcal N_{\mathcal B}}{\Lambda_{\mathcal B}}
 +\frac{\mathfrak S_{\mathcal B}}{\Lambda_{\mathcal B}}.   \tag{4.9}
\]

Assume a compact parent family for which

\[
c\sqrt k\le\Lambda_{\mathcal B}\le C\sqrt k,
\qquad
L\ge c\sqrt k,                                             \tag{4.10}
\]

with fixed positive constants, and suppose its aggregate endpoint
incidence is near the local minimum:

\[
\sum_{\mathcal B}
\left(
e_{\mathcal B}
-\frac{\mathcal N_{\mathcal B}}{\Lambda_{\mathcal B}}
\right)
=o(W_k),\qquad
W_k=\binom{k}{k/2}.                                        \tag{4.11}
\]

Equations (4.9)--(4.11) give

\[
\sum_{\mathcal B}\mathfrak S_{\mathcal B}
=o(W_k\sqrt k).
\]

Applying (4.5) on both endpoint sides yields

\[
\boxed{
\sum_j
\bigl((d_j^{\mathcal L}-2)_+
     +(d_j^{\mathcal R}-2)_+\bigr)
=o(W_k).}                                                  \tag{4.12}
\]

Since \(d\le3(d-2)\) for \(d\ge3\), only \(o(W_k)\)
endpoint--parent incidences occur at degree at least three.

For degree-two positions, sum (4.6a) and use
\(\sum_{\mathcal B}\alpha_\sigma(\mathcal B)\le
\sum_{\mathcal B}\mathfrak S_{\mathcal B}\).  On both endpoint sides,

\[
\boxed{
\sum_{\substack{j,\sigma\\d_j^\sigma=2}}b_j^\sigma
=o(W_k\sqrt k).}                                          \tag{4.13}
\]

Since \(L\ge c\sqrt k\), (4.13) implies the following exact quantified
near-template statement.  For every fixed \(\eta>0\), all but
\(o(W_k)\) degree-two endpoint positions satisfy

\[
b_j^\sigma\le\eta L.                                     \tag{4.14}
\]

Equivalently, by a diagonal choice there is a sequence
\(\eta_k\downarrow0\) for which all but \(o(W_k)\) such positions have at
most \(\eta_kL=o(L)\) breaks.  Between those breaks their parents
alternate exactly.

Consequently, if there are \(\Omega(W_k)\) degree-two sharing positions,
their total number of common-band transition cells is
\(\Omega(W_k\sqrt k)\), and those cells agree
with parity ladders outside an \(o(1)\) fraction.  This is a
rank-transition-density conclusion.  It permits, for example, one or a
few breaks at each of \(\Theta(W_k)\) endpoints and therefore does not
imply that all but \(o(W_k)\) endpoints are unbroken ladders.

The assumption (4.11) is essential.  A near-width global word may use far
more endpoint--parent incidence than the local minimum by concentrating it
at high-degree portals.  No implication from near global word length to
(4.11) is proved here.

## 5. Static templates: construction and obstruction

### 5.1 Exact isolated double flags

Let

\[
R_0\subsetneq R_1\subsetneq\cdots\subsetneq R_u,
\qquad
L_0\subsetneq L_1\subsetneq\cdots\subsetneq L_v
\]

be two strict Boolean chains.  Suppose there is a nonempty common core

\[
\varnothing\ne C\subseteq R_0\cap L_0.
\]

Emit the block

\[
\begin{aligned}
&
R_u\setminus R_{u-1},\ldots,R_1\setminus R_0,
R_0\setminus C,\ C,\\
&\hspace{3cm}
L_0\setminus C,
L_1\setminus L_0,\ldots,L_v\setminus L_{v-1},
\end{aligned}                                              \tag{5.1}
\]

omitting empty differences.

Every \(R_i\) is the union of one suffix ending at the central occurrence
of \(C\), and every \(L_i\) is the union of one prefix beginning there.
Conversely, at a position \(j\) of any nonzero word, every target whose
witness starts or ends at \(j\) contains the nonempty letter \(A_j\).
Thus two endpoint flags at one isolated center are realizable if and only
if they are strict chains with a nonempty common core.

In particular, every isolated parity-ladder flag has a literal
realization.  The difficulty is not one center but simultaneous fusion of
many centers.  This statement begins with the two rail chains already
present.  It does not prove that a prescribed long rail pair extends to a
full factor SCD, or that one full SCD contains a dense disjoint packing of
such pairs; those are separate SCD-extension questions.

### Theorem 5.2 — explicit isolated diamond rails; full-SCD completion open

The structural template itself exists at arbitrary length.  Fix
\(s\ge3\) and an ordering \(x_1,\ldots,x_s\).  For
\(1\le r\le s-1\), put

\[
A_r=\{x_1,\ldots,x_r\},\qquad
B_r=\{x_1,\ldots,x_{r-1},x_{r+1}\}.                       \tag{5.2a}
\]

Define two rails by

\[
C_r=
\begin{cases}
A_r,&r\ \text{odd},\\
B_r,&r\ \text{even},
\end{cases}
\qquad
D_r=
\begin{cases}
B_r,&r\ \text{odd},\\
A_r,&r\ \text{even}.
\end{cases}                                               \tag{5.2b}
\]

Then

\[
C_1\subsetneq\cdots\subsetneq C_{s-1},
\qquad
D_1\subsetneq\cdots\subsetneq D_{s-1}                    \tag{5.2c}
\]

are disjoint saturated symmetric chains of \(B_s\).  At each rank they
are the two distinct sets \(A_r,B_r\).  For \(1\le r\le s-2\),

\[
C_{r+1}\setminus C_r=
\begin{cases}
\{x_{r+2}\},&r\ \text{odd},\\
\{x_r\},&r\ \text{even},
\end{cases}
\qquad
D_{r+1}\setminus D_r=
\begin{cases}
\{x_r\},&r\ \text{odd},\\
\{x_{r+2}\},&r\ \text{even}.
\end{cases}                                               \tag{5.2e}
\]

Thus both chains are saturated; their endpoint ranks \(1,s-1\) sum to
\(s\), proving symmetry.
The prefix flag

\[
A_1\subsetneq A_2\subsetneq\cdots\subsetneq A_{s-1}       \tag{5.2d}
\]

alternates between the two rails.  For \(2\le r\le s-2\),
\(A_r\) and \(B_r\) are the two intermediate vertices of the Boolean
two-interval

\[
[A_{r-1},A_{r+1}],
\]

so the construction contains \(s-2\) alternating covers and \(s-3\)
overlapping internal diamonds. \(\square\)

This proves existence of arbitrarily long isolated symmetric rail pairs.
It does **not** prove that the complement of these two chains has an SCD.
Rank symmetry of that complement is only a necessary condition.  Nor may
one invoke a general extension lemma for disjoint symmetric chains: such a
lemma is false already in \(B_2\), where deleting the two singleton
symmetric chains leaves \(\varnothing\) and \([2]\), which cannot form one
saturated chain.  Thus embedding even one prescribed long rail pair in a
full SCD, and especially packing enough compatible rail pairs in one full
SCD, remains unproved here.

### 5.3 Static high-degree double portals exist

This subsection uses the global-portal theorem from
`GLOBAL_PORTAL_CONSTRUCTION_AFTER_DRAY_20260724.md`, with precisely the
scope certified in
`GLOBAL_PORTAL_CONSTRUCTION_AFTER_DRAY_AUDIT_20260725.md`.  That audited
theorem supplies, after a coordinate relabeling,
a family of

\[
\Theta_\varepsilon(W_k/\sqrt k)
\]

central global-SCD flags.  Each flag contains
\(\Theta(\sqrt k)\) selected targets in distinct product parents, and the
total selected endpoint--parent incidence is
\(\Omega(\varepsilon W_k)\).

These one-sided flags can be made two-sided without changing the scale.
Let \(B_D\) be the least selected target of flag \(D\), and let \(d_D\)
be its parent degree.  Since \(|B_D|\ge m-O(\sqrt k)\),

\[
\sum_{x\in[k]}\sum_{D:x\in B_D}d_D
=\sum_Dd_D|B_D|
\ge(m-O(\sqrt k))\sum_Dd_D.
\]

Some coordinate \(x\) therefore belongs to the minima of a subfamily
carrying a fixed positive fraction of the total incidence.  After the
standard high-degree thinning, pair these flags and apply (5.1) with
\(C=\{x\}\), putting one flag on the suffix side and the other on the
prefix side.

Starting with a smaller constant budget absorbs the one-center overhead.
The result is one literal nonzero word of length at most
\(\varepsilon W_k\), with

\[
\Theta_\varepsilon(W_k/\sqrt k)
\]

distinguished centers, left and right degree
\(\Theta(\sqrt k)\) at every center, and
\(\Omega(\varepsilon W_k)\) typed endpoint--parent incidence.

Thus static high-degree rank-monotone templates are not obstructed.
Theorem 4.1 shows what they sacrifice: if such a degree-\(\Theta(\sqrt k)\)
center were extended to the common full local bands and required to be
layer-near-equal in all of its parents, it would contribute
\(\Theta(k)\) layer slack.  The isolated static flag by itself is not a
full-band endpoint partition and carries no such intrinsic charge.  Summed over
\(\Theta(W_k/\sqrt k)\) centers, this is
\(\Theta(W_k\sqrt k)\), the full leading aggregate slack scale.

### 5.4 Isolated arms have linear cost

If \(d_R\) distinct designated targets end at one center, their starts are
distinct.  If \(d_L\) distinct designated targets start there, their ends
are distinct.  In an isolated double-flag block, the two position sets
meet only at the center.  Hence

\[
\boxed{
\text{isolated block length}\ge d_R+d_L-1.}                \tag{5.3}
\]

Therefore isolated templates carrying \(\Omega(W_k)\) useful incidence
consume \(\Omega(W_k)\) arm positions.  They cannot be appended as an
\(o(W_k)\) repair.  Their starts and ends must be fused into the already
necessary middle-owning trajectory.

## 6. Exact literal gluing criterion

Endpoint chains, parity ladders, orthogonality, and common cores are still
not sufficient for a global word.

Fix a family \(\mathcal I\) of physical intervals in
\(\{1,\ldots,n\}\).  For every \(I\in\mathcal I\), prescribe a target
vector \(T_I\) with nonnegative integral coordinates.  For a coordinate
\(c\) and threshold \(h\ge1\), define the forbidden set of positions

\[
F_{c,h}
=
\bigcup\{J\in\mathcal I:T_J(c)<h\}.                         \tag{6.1}
\]

### Theorem 6.1 — coordinate-threshold safe points

Allowing zero word letters, there exists a word

\[
A_1,\ldots,A_n
\]

such that

\[
\max_{t\in I}A_t=T_I
\quad\text{for every }I\in\mathcal I                       \tag{6.2}
\]

if and only if

\[
\boxed{
I\setminus F_{c,h}\ne\varnothing
\quad
\text{whenever }T_I(c)\ge h.}                              \tag{6.3}
\]

#### Proof

Necessity is immediate.  If \(T_I(c)\ge h\), some position of \(I\)
must carry coordinate value at least \(h\).  Such a position cannot lie
in an interval whose prescribed target has coordinate below \(h\).

Conversely, define

\[
A_t(c)=
\begin{cases}
\max\bigl(\{h:1\le h\le H_c,\ t\notin F_{c,h}\}\cup\{0\}\bigr),
 &t\in\displaystyle\bigcup_{I\in\mathcal I}I,\\
0,&t\notin\displaystyle\bigcup_{I\in\mathcal I}I,
\end{cases}                                                \tag{6.4}
\]

where \(H_c=\max_{I\in\mathcal I}T_I(c)\) (and \(H_c=0\) if
\(\mathcal I\) is empty).  This finite cutoff only handles positions
lying in no prescribed interval; for every position in a prescribed
interval, membership in \(F_{c,H_c+1}\) already bounds the unrestricted
maximum.  If \(T_I(c)=q\), condition
(6.3) gives a position of \(I\) with value at least \(h\) for every
\(h\le q\), and in particular gives maximum at least \(q\).  On the other
hand, \(I\subseteq F_{c,q+1}\), because \(I\) itself occurs in the union
defining that forbidden set.  Hence every position of \(I\) has value at
most \(q\).  This proves (6.2) coordinate by coordinate. \(\square\)

For a nonzero target family, zero positions may be deleted and all
intervals compressed; the retained positions of every interval remain
consecutive and its maximum is unchanged.  Endpoint classes may coalesce,
so this deletion should be performed only after the realization theorem is
applied.

### 6.1 Why local templates do not imply safe points

Represent every selected target by the edge

\[
\ell_T\longrightarrow r_T
\]

between its left and right endpoint classes.  A literal word forces:

- targets in every left class form an increasing inclusion chain;
- targets in every right class form an inclusion chain;
- the two partitions are orthogonal;
- nested physical intervals have nested targets; and
- the two flags at a physical position contain its common nonempty letter.

Even these properties do not imply (6.3).  For example, prescribe

\[
U_{12}=\{a,c\},\qquad
U_{23}=\{b,c\},\qquad
U_{13}=\{a,b,c,d\}
\]

on intervals \([1,2],[2,3],[1,3]\).  The two smaller labels are contained
in the large label and the local endpoint flags have a common core
\(\{c\}\).  Nevertheless every OR word would satisfy

\[
U_{13}=U_{12}\cup U_{23}=\{a,b,c\},
\]

contradicting the prescribed element \(d\).

Before safe points can even be tested, abstract local endpoint classes
must be aligned on one physical line so that every selected edge obeys

\[
\ell_T\le r_T.
\]

The endpoint dual supplies neither this common ordering nor the
coordinate-threshold pins.  Across product parents, all local systems must
share one alignment and one family of global letters.

## 7. Final construction/obstruction ledger

### Unconditional theorems proved

- the exact master slack identity (1.11);
- the endpoint-incidence identity (1.16);
- complete formal equality conditions;
- impossibility of equality for every fixed band profile with a positive
  quadratic certificate, including the width boundary;
- the entrance-energy bounds (2.4) and (2.4c), with exact shell constant
  (2.4d);
- the subleading separation \(Q_t+\Omega(t^{5/3})\);
- exponential one-partition anti-rigidity;
- the exact two-layer path-cover characterization and sharp bound
  \(\beta\ge\delta(\delta-1)\);
- the global rank-packing inequality (4.5);
- the degree-two parity-ladder classification;
- the conditional aggregate near-equality conclusions (4.12)--(4.13),
  with breaks controlled in endpoint--rank transition density;
- exact isolated double-flag realization;
- explicit arbitrarily long isolated symmetric diamond rails (5.2a)--(5.2e);
- existence of static high-degree double portals at the sharp endpoint
  scale, using the separately audited global-portal theorem;
- the isolated-arm lower bound (5.3); and
- the exact safe-point realization theorem (6.3).

### What is constructed

- Every individual degree-one or degree-two endpoint flag is literally
  realizable in isolation.  A prescribed left/right pair is realizable as
  an isolated double flag exactly when its two minima have a common
  nonempty subset.
- Arbitrarily long pairs of disjoint symmetric diamond rails are explicit
  as partial SCD data.
- Static high-degree double portals with \(\Theta(W_k)\) useful incidence
  exist in a word of constant-times-\(W_k\) length.

### What is obstructed

- Exact equality in the sharp local dual.
- Concentrating a simultaneously near-equal parent family at endpoints of
  degree greater than two.
- Isolated use of either the parity-ladder templates or the high-degree
  portals as an \(o(W_k)\) appendage.
- Any proposed global template that violates the safe-point criterion.

### Still unproved

For the low-slack parity-ladder route there are two distinct missing
statements: extend and pack the prescribed rail pairs in one full factor
SCD, and then fuse their physical flags.  The high-degree portal route
already has a full-SCD static construction and retains only the latter
dynamic gate.  In either case the decisive common-object problem is:

\[
\boxed{
\begin{gathered}
\textbf{UNPROVED:}\quad
\text{fuse a linear family of degree-two parity ladders, or the}\\
\text{high-slack global portals, into one middle-productive interval
system}\\
\text{with }o(W_k)\text{ connector cost and with all safe-point
constraints.}
\end{gathered}}                                            \tag{7.1}
\]

Equivalently, one must construct one legal last-occurrence/MTF trajectory
whose physical positions are already the \(W_k-o(W_k)\) middle owners and
whose interval graph realizes the required cross-parent flags.  A
canonical rotor walk is one sufficient subclass, but general legal MTF
updates are strictly broader.

No theorem here shows that a near-width global word must minimize the
aggregate local endpoint incidence, and no theorem here rules out
high-degree middle-productive fusion.  Therefore this fifth-wave result
does not prove or refute the global contiguous-OR conjecture.

## 8. Adversarial audit record

The decisive statements were reconstructed independently.  The audit
made the following checks and corrections.

1. The boundary-mass telescoping, every sign in (1.11), the triangular
   count \(\binom{K+2}{3}\), and the \(t^{5/3}\) division by
   \(\Lambda=\Theta(t)\) were checked independently.  The proof of
   Theorem 2.1 now uses the explicit half-threshold dichotomy for
   \(\epsilon\), rather than an informal ``positive fraction'' case.

2. The first invalid statement in the draft was the original definition
   of (4.2): without the activity indicator it charged an empty support
   by all \(L\) transitions and made (4.3) false.  Equation (4.2) now
   assigns zero to an unrepresented parent.  With that correction, the
   proof of (4.5) is exact.

3. Two independent checks recovered the degree-two alternation, the
   one-factor-chain localization, and the overlapping Boolean diamonds.
   They also identified the necessary scope correction: (4.11) controls
   total bad transition cells, not the number of endpoints having at
   least one break.  Equations (4.13)--(4.14) are the corrected sharp
   conclusion.

4. The isolated double-flag construction and weighted-coordinate pairing
   were checked independently.  The high-degree construction explicitly
   depends on the separately audited global-portal theorem, and its local
   layer-slack cost applies only after extension to the common full bands.

5. The safe-point theorem was checked coordinate by coordinate.  The
   draft maximum was unbounded at positions lying in no prescribed
   interval; (6.4) now sets those positions to zero and imposes the finite
   cutoff \(H_c\).

6. No audit established the implication from near global word length to
   (4.11), or from static flags to a common middle-productive MTF
   trajectory.  Both implications remain expressly unproved.

7. The explicit rail pair (5.2a)--(5.2e) was checked directly.  It is a
   pair of complete saturated symmetric chains, but no valid argument was
   found extending its complement to an SCD.  The report therefore does
   not promote isolated rails to a full-SCD or dense-packing theorem.

The precise conclusion is:

\[
\boxed{
\begin{gathered}
\text{local equality is empty and locally noncanonical;}\\
\text{conditional aggregate near-equality suppresses high degree and forces}\\
\text{piecewise degree-two parity ladders with charged breaks;}\\
\text{isolated rails and static portals exist, but full-SCD rail packing}\\
\text{and literal dynamic fusion remain the gates.}
\end{gathered}}
\]
