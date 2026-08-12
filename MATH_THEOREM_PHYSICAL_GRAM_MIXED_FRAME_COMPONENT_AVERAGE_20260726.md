# Physical Gram averaging for mixed frames and tensor packets

Date: 2026-07-26

Method: pure mathematics only. No computation, solver, web input, or
probabilistic black box is used.

## 0. Verdict

Fix a signed depth \(j=(q,\epsilon)\), a physical target layer
\(\mathcal T_j\) of size \(N_j\), and owner-disjoint physical
\(Q_s\)-cells. Put

\[
 p_{s,q}={2^q\over\binom sq},\qquad
 F_{s,q}=2^{s-q}\binom sq={2^s\over p_{s,q}}.          \tag{0.1}
\]

Thus one cell has exactly \(F_{s,q}\) candidate affine \(q\)-face
traces. Suppose a tensor packet contains \(L\) face-separated cells, so
its complete candidate family has size

\[
                         K_j=LF_{s,q}.                 \tag{0.2}
\]

Let there be \(P\) retained packets. Then

\[
 PL2^s=G,\qquad PK_j={G\over p_{s,q}}.                \tag{0.3}
\]

The path/cycle component polynomials have the exact physical average

\[
 \boxed{
 \mathbb E_{c'}\,
 |\mathcal A_j(c)\cap\mathcal A_j(c')|
 ={F_{s,q}^2\over N_j},}                              \tag{0.4}
\]

where \(c\) is fixed and \(c'\) is uniform in the full physical
coordinate orbit of an \(s\)-cell. The identity holds for both signs and
for literal masks, not tagged frame types.

Consequently, suppose every owner packet has a finite catalogue of states
which all preserve exactly the same packet owner support. Choose packet
states independently. If their aggregate one-target candidate marginal is
uniform, then

\[
 \boxed{\mathbb E V_j\le {G\over p_{s,q}}.}            \tag{0.5}
\]

No individual packet must be target-uniform. Finite averaging and Jensen
then give one deterministic exact-owner state choice for which

\[
 \sum_{q\le H,\,\epsilon=\pm}
 p_{s,q}\sqrt{N_jV_j}
 \le
 2W\sum_{q\le H}\sqrt{p_{s,q}}.                       \tag{0.6}
\]

Uniformly for \(H\le s/2\),

\[
 \boxed{
 \sum_{q\le H}\sqrt{p_{s,q}}
 =\sqrt{2\over s}+O(1/s).}                            \tag{0.7}
\]

Hence the ideal physical Gram total is

\[
 \boxed{
 \sum_jp_{s,q}\sqrt{N_jV_j}
 \le
 (2\sqrt2+o(1)){W\over\sqrt s}+O(W/s)=o(W)}           \tag{0.8}
\]

whenever \(s\to\infty\). The two signed depth-one rows give the leading
universal bound. All \(q\ge2\) rows together cost only \(O(W/s)\).

There is one decisive audit qualification. The current uniform
mixed-frame catalogue proves a pointwise size-biased one-owner/one-target
marginal. The block-capacity part of the \(Q_3\) tensor activity law has
total Gaussian-band forbidden-pattern error \(O(m^{-1/2})\). These close
that coefficient calculation, but do not prove pointwise symmetry among
all admissible activity patterns and do not yet produce owner-preserving
packet state catalogues whose choices may be made independently. A common
global coordinate permutation makes every one-target marginal uniform
while leaving Gram variance unchanged. Thus one-point frame averaging
alone does not prove (0.5).

The exact deterministic residual is the packet-pair correlation

\[
 R_j=\sum_{a\ne b}
 \left(
 |\mathcal B_{a,j}\cap\mathcal B_{b,j}|-{K_j^2\over N_j}
 \right),                                             \tag{0.9}
\]

where \(\mathcal B_{a,j}\) is packet \(a\)'s candidate family. One has

\[
 \boxed{
 V_j={G\over p_{s,q}}
       \left(1-{K_j\over N_j}\right)+R_j.}             \tag{0.10}
\]

If

\[
 \eta_j={N_j(R_j)_+\over P(P-1)K_j^2},                \tag{0.11}
\]

then

\[
 \boxed{
 p_{s,q}\sqrt{N_jV_j}
 \le\sqrt{p_{s,q}N_jG}+G\sqrt{\eta_j}.}               \tag{0.12}
\]

Therefore the exact remaining correlation theorem is

\[
                         \sum_j\sqrt{\eta_j}=o(1).     \tag{0.13}
\]

The convenient uniform sufficient estimate is
\(\eta_j=o(H^{-2})\). A row with \(\eta_j=\Theta(1)\) contributes
\(\Theta(W)\), overwhelming the harmless \(W/\sqrt s\) diagonal term.
Thus the component coefficients themselves have no coefficient-one
obstruction; the only possible dominant term is coherent cross-packet
frame activity.

## 1. The component polynomials explicitly

First take two active perfect matchings \(M_0,M_1\) on the same \(2s\)
coordinates. A lower candidate is a set \(A\) meeting every edge of both
matchings in at most one point. If \(z_i(A)\) is the number of empty
edges of \(M_i\), its contribution is

\[
                         x^{z_0(A)}y^{z_1(A)}.          \tag{1.1}
\]

The union \(M_0\cup M_1\) is a disjoint union of doubled edges and even
alternating cycles. If exterior cores or active supports differ, imposing
the pins and exclusions also produces alternating paths.

For a doubled edge the lower polynomial is

\[
                         D(x,y)=xy+2.                  \tag{1.2}
\]

For an alternating cycle on \(2\ell\) vertices, an admissible \(A\) is
an independent set. If \(|A|=k\), exactly \(\ell-k\) edges of each
colour are empty. Therefore

\[
 C_\ell(x,y)=
 \sum_{k=0}^{\ell}
 {2\ell\over2\ell-k}\binom{2\ell-k}{k}
 (xy)^{\ell-k}.                                       \tag{1.3}
\]

This includes \(C_1=xy+2\). For an alternating path whose edge colours
are \(t_1,\ldots,t_d\), with \(t_i\in\{x,y\}\), put

\[
 M(t)=\begin{pmatrix}t&1\\[1mm]1&0\end{pmatrix}.       \tag{1.4}
\]

Its unpinned polynomial is exactly

\[
 (1,1)M(t_1)\cdots M(t_d)\binom11.                    \tag{1.5}
\]

Pinned endpoints replace the all-one boundary vectors by the appropriate
coordinate vectors; internal pins split the path. Multiplying
(1.2)--(1.5) over components and extracting \([x^qy^q]\) gives the
physical intersection.

Upper traces have the same component polynomials. Complementing \(A\) on
the active support turns the condition “no full edge” into “no empty
edge” and converts full upper-edge counts to empty lower-edge counts.

## 2. Summing all alternating components

The component sum can be executed exactly before asymptotics. Fix
\(M_0\), and let

\[
 \mathcal A_q(M)=
 \left\{
 A\in\binom{[2s]}{s-q}:|A\cap e|\le1\quad(e\in M)
 \right\}.                                            \tag{2.1}
\]

Every such family has size

\[
                         F_{s,q}=2^{s-q}\binom sq.     \tag{2.2}
\]

Fix \(A\in\mathcal A_q(M_0)\). A second perfect matching \(M\) contains
no edge internal to \(A\) in exactly

\[
 { (s+q)!\over(2q)!}(2q-1)!!
 ={(s+q)!\over 2^q q!}                                \tag{2.3}
\]

ways: inject the \(s-q\) points of \(A\) into distinct complement
points, and match the remaining \(2q\) complement points. Since there are

\[
                         (2s-1)!!={(2s)!\over2^ss!}   \tag{2.4}
\]

perfect matchings, the exact probability is

\[
 {2^{s-q}s!(s+q)!\over q!(2s)!}
 ={F_{s,q}\over\binom{2s}{s-q}}.                      \tag{2.5}
\]

Summing first over \(A\) proves

\[
 \boxed{
 {1\over(2s-1)!!}\sum_M
 [x^qy^q]\prod_{Q\in\operatorname{comp}(M_0\cup M)}P_Q(x,y)
 ={F_{s,q}^2\over\binom{2s}{s-q}}.}                   \tag{2.6}
\]

Thus the complete distribution of alternating cycle lengths collapses to
one hypergeometric coefficient.

For cells with different cores and supports, alternating paths occur. Let
\(\mathfrak C_s\) be the full coordinate orbit of a physical \(s\)-cell.
It is transitive on each target layer, so for fixed \(T\),

\[
 \Pr_{c'\in\mathfrak C_s}\{T\in\mathcal A_j(c')\}
 ={F_{s,q}\over N_j}.                                  \tag{2.7}
\]

Summing over the \(F_{s,q}\) targets in a fixed cell proves (0.4).
Equivalently, averaging all path matrices, cycle polynomials, and pin
patterns gives exactly \(F_{s,q}^2/N_j\).

## 3. Tensor face separation changes cells into packet coins

Let packet \(a\) contain \(L\) product cells. Local \(Q_2/Q_3\) face
separation makes their candidate families disjoint at every certified
signed depth. Define

\[
 \mathcal B_{a,j}=
 \mathop{\dot\bigcup}_{c\subset a}\mathcal A_j(c),
 \qquad |\mathcal B_{a,j}|=K_j=LF_{s,q}.              \tag{3.1}
\]

Then

\[
                         d_j(T)=\sum_{a=1}^P
 {\bf1}_{\{T\in\mathcal B_{a,j}\}}.                   \tag{3.2}
\]

For a deterministic atlas, expansion of the square gives

\[
\begin{aligned}
 V_j
 &=PK_j+\sum_{a\ne b}
       |\mathcal B_{a,j}\cap\mathcal B_{b,j}|
       -{(PK_j)^2\over N_j}\\
 &=PK_j\left(1-{K_j\over N_j}\right)+R_j.
                                                               \tag{3.3}
\end{aligned}
\]

Using \(PK_j=G/p_{s,q}\) proves (0.10). All same-packet
off-diagonal terms vanish before averaging.

Now let packet \(a\) choose a random owner-preserving state,
independently over \(a\), and write

\[
 \pi_{a,T}=\Pr\{T\in\mathcal B_{a,j}\},\qquad
 e_T=\sum_a\pi_{a,T}-{PK_j\over N_j}.                 \tag{3.4}
\]

Since every packet state has exactly \(K_j\) candidates,

\[
\begin{aligned}
 \mathbb EV_j
 &=\sum_a\left(K_j-\sum_T\pi_{a,T}^2\right)
       +\sum_Te_T^2\\
 &\le PK_j\left(1-{K_j\over N_j}\right)+\|e\|_2^2\\
 &\le {G\over p_{s,q}}+\|e\|_2^2.                    \tag{3.5}
\end{aligned}
\]

The first inequality is Cauchy--Schwarz:
\(\sum_T\pi_{a,T}^2\ge K_j^2/N_j\). Exact aggregate marginal balance
\(e=0\) therefore proves (0.5), even when each packet reaches only a tiny
part of the target layer.

If

\[
 |e_T|\le\delta_j{PK_j\over N_j}
 \qquad(T\in\mathcal T_j),                             \tag{3.6}
\]

then Jensen and (3.5) give

\[
 \boxed{
 \mathbb E\left[p_{s,q}\sqrt{N_jV_j}\right]
 \le\sqrt{p_{s,q}N_jG}+\delta_jG.}                    \tag{3.7}
\]

Finite averaging supplies one deterministic exact-owner choice with total
Gram cost at most

\[
 \sum_j\sqrt{p_{s,q}N_jG}+G\sum_j\delta_j.            \tag{3.8}
\]

No concentration result is used: the minimum of finitely many outcomes is
at most their mean.

## 4. Mixed-frame first moment and tensor activity

This section records exactly what the size-biased frame identity proves.
Fix a lower target \(T\) of frame type \(f\). It has

\[
 d^{\rm tar}_{f,q}=2^q\binom{f+q}{q}                  \tag{4.1}
\]

compatible middle extensions in that frame. A compatible source has

\[
                         k_f=m-2f                     \tag{4.2}
\]

split pairs. Under the ideal uniform \(s\)-activity law, a prescribed
set of \(q\) compatible deletion pairs is active with probability

\[
                         \beta_{f,q}
 ={\,\binom sq\,\over\binom{k_f}q}.                    \tag{4.3}
\]

Every candidate face contains \(2^q\) middle owners. If an owner uses
each allowed catalogue frame with weight \(1/a_X\), and

\[
 S_{T,q}=\sum_{j:f_j(T)\in\mathcal B}\lambda_{f_j(T),q},
                                                               \tag{4.4}
\]

then its expected candidate degree obeys the exact bounds

\[
 {\binom sq\over2^q(1+\varepsilon)\alpha}S_{T,q}
 \le\mu_q(T)\le
 {\binom sq\over2^q(1-\varepsilon)\alpha}S_{T,q}.       \tag{4.5}
\]

where

\[
 \lambda_{f,q}
 ={2^q\binom{f+q}{q}\over\binom{m-2f}{q}}.            \tag{4.6}
\]

The uniform mixed-frame catalogue gives

\[
 S_{T,q}
 =(1+O(\varepsilon)){\alpha\over\rho_q},
 \qquad \rho_q={N_q\over W}.                          \tag{4.7}
\]

Substitution into (4.5) yields the pointwise physical first moment

\[
 \boxed{
 \mu_q(T)=
 (1+O(\varepsilon))
 {\binom sq\over2^q\rho_q}.}                          \tag{4.8}
\]

The main term is exactly \((W/N_q)/p_{s,q}\), the required mean candidate
degree. Size bias and uniform activity cancel all pair-type dependence.

For a block law symmetric on its admissible \(q\)-sets, let
\(\gamma_q\) be the excluded fraction. Then (4.8) has relative error
\(O(\varepsilon+\gamma_q)\). If ideal deletion directions are grouped
into bounded four-direction blocks, a \(Q_2\) law first excludes a triple,
whereas a \(Q_3\) law first excludes four directions. The exact
hypergeometric union bound

\[
 B\sum_{t=d+1}^4\binom4t
 {\binom{m-4}{q-t}\over\binom mq},
 \qquad B=\Theta(m),                                   \tag{4.9}
\]

gives

\[
 \gamma_q^{(2)}=O(q^3/m^2),\qquad
 \gamma_q^{(3)}=O(q^4/m^3).                           \tag{4.10}
\]

Therefore, for fixed \(A\),

\[
 \sum_{q\le A\sqrt m}\gamma_q^{(3)}
 =O(m^{-1/2})=o(1),                                   \tag{4.11}
\]

while

\[
 \sum_{q\le A\sqrt m}\gamma_q^{(2)}=O_A(1),           \tag{4.12}
\]

and the known triple-occupancy coefficient is positive. Thus the
\(Q_3\) block-capacity loss has the correct coefficient scale for (3.8),
provided the mixed catalogue also makes the admissible activity patterns
pointwise symmetric. The pure \(Q_2\) activity error does not itself imply
\(o(W)\).

Equations (4.8)--(4.11) close the marginal coefficient calculation. They
do not assert that the weights \(1/a_X\) and ideal activity are realized
by complete owner-preserving packet states.

## 5. The binomial coefficient sum

Put

\[
                         a_q=\sqrt{2^q\over\binom sq}. \tag{5.1}
\]

Then

\[
 a_1=\sqrt{2/s},\qquad
 a_2=\sqrt{8\over s(s-1)}=O(1/s),                     \tag{5.2}
\]

and

\[
 {a_{q+1}\over a_q}
 =\sqrt{2(q+1)\over s-q}.                             \tag{5.3}
\]

For \(2\le q+1\le s/4\), this ratio is at most
\(\sqrt{2/3}+o(1)\). Hence

\[
                         \sum_{2\le q\le s/4}a_q=O(1/s).          \tag{5.4}
\]

For \(s/4\le q\le s/2\), monotonicity of binomial coefficients and
Stirling's formula give

\[
 a_q\le
 {2^{s/4}\over\sqrt{\binom{s}{\lfloor s/4\rfloor}}}
 \le \exp(-cs)                                        \tag{5.5}
\]

for an absolute \(c>0\), up to an irrelevant polynomial factor. This
proves (0.7).

Since \(N_j\le W\) and \(G\le W\), (3.8), (0.7), and the two signs give

\[
 \sum_jp_{s,q}\sqrt{N_jV_j}
 \le(2\sqrt2+o(1)){W\over\sqrt s}+O(W/s)
       +G\sum_j\delta_j.                              \tag{5.6}
\]

Conditional on that pointwise activity symmetry, with

\[
 \delta_j=O(m^{-3})+O(q^4/m^3),\qquad H\le A\sqrt m,  \tag{5.7}
\]

the last term is \(O(W/\sqrt m)=o(W)\).

## 6. Why one-point averaging is not the missing theorem

Take any deterministic exact-owner atlas and apply one uniformly random
ambient coordinate permutation to all packets. Every target in a fixed
rank has the correct one-target marginal. The mixed-frame and activity
averages are perfectly flat. But the candidate degree vector is only
permuted, so

\[
                         V_j(g\mathscr C)=V_j(\mathscr C)           \tag{6.1}
\]

for every permutation \(g\). No Gram energy is removed.

This distinguishes two operations.

1. A common global frame shuffle gives transitive one-point marginals but
   preserves every packet-pair correlation.
2. Independent packet shuffles give (3.5), but are legal only when every
   shuffled state has exactly the same packet middle-owner support.

The polynomial mixed-pair catalogue currently supplies the first kind of
fractional symmetry. The tensor associator supplies owner-preserving local
shore states, but those states are not known to realize the size-biased
full-frame marginal (4.8). Combining both properties is the missing exact
lemma.

Equivalently, in deterministic language the remaining task is (0.13), or
the stronger uniform estimate

\[
 \sum_{a\ne b}
 \left(
 |\mathcal B_{a,j}\cap\mathcal B_{b,j}|-{K_j^2\over N_j}
 \right)
 =o\left({G^2\over p_{s,q}^2N_jH^2}\right).           \tag{6.2}
\]

Every intersection in (6.2) is given by the path/cycle polynomials of
Section 1.

## 7. Exact successor lemma

The physical Gram route is reduced to the following owner-level statement.

> **Owner-preserving mixed-frame activity lemma.** Partition
> \(W-o(W)\) middle owners into tensor packets. For every packet construct
> a finite catalogue of complete face-separated \(Q_s\)-cell resolutions,
> all with exactly the same middle support. Choose packet states
> independently. For both signs and every \(q\le A\sqrt m\), their
> aggregate candidate marginal must obey
> \[
> \left|
> \sum_a\pi_{a,T}-{G\over p_{s,q}N_j}
> \right|
> \le\delta_j{G\over p_{s,q}N_j}
> \qquad(T\in\mathcal T_j),
> \]
> with \(\sum_j\delta_j=o(1)\).

If this lemma holds, (3.7), finite averaging, and (5.6) prove the desired
physical Gram estimate with no further coefficient loss. The exact scale
is

\[
 \boxed{
 \text{diagonal cost }\sim2\sqrt2\,W/\sqrt s;\qquad
 \text{all remaining danger }=G\sum_j\sqrt{\eta_j}.}
\]
