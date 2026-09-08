# Overlapping adjacent-priority atlas: exact legality, signed Gram, and the joined-target gate

Date: 2026-07-25

Method: pure mathematics only.  No computation, search, solver, or
long-running job is used.

## 0. Outcome

Put

\[
 n=2m+1,
 \qquad W=\binom{2m+1}{m},
\]

with \(m\ge3\).  Every multidepth identity below is asserted for
\(1\le H\le m-2\), so all upper cyclic windows used in lossless
packetization are proper.

Fix ordered disjoint coordinate pairs

\[
 P_1,P_2,\ldots ,P_m.
\]

Let \(\tau_j\) exchange \(P_j\) and \(P_{j+1}\) coordinatewise and
fix every other coordinate.  Choose one exact local factor \(F_1\) and
define the whole factor chain recursively by

\[
 \boxed{F_{j+1}=\tau_jF_j\qquad(1\le j<m).}
\tag{0.1}
\]

For the base priority \(P_1<\cdots<P_m\), let

\[
 \mathcal D_j=\left\{S\in\binom{[n]}{m-1}:
 S\cap P_h\ne\varnothing\ (h<j),\quad
 S\cap(P_j\cup P_{j+1})=\varnothing\right\}.
\tag{0.2}
\]

In every \(F_j\)-row, split its \(\mathcal D_j\)-starts into maximal
physical intervals.  A packet bit replaces, at every root in that
interval, the \(F_j\)-token by its \(F_{j+1}\)-token.

The first result is stronger than separate odd/even legality.

> **Overlapping-atlas theorem.**  Arbitrary packet choices may be made
> simultaneously for every \(j=1,\ldots ,m-1\), including neighboring
> blocks.  Every corner still saturates every lower target once and has
> distinct middle owners.

If \(r_j\) is the packet count of block \(j\) and
\(r=\sum_{j<m}r_j\), then

\[
 \boxed{
 r=O\!\left(\frac{W\log ^2m}{m}\right),
 \qquad
 J(M_\varepsilon)\le J(M_0)+2r
 =O\!\left(\frac{W\log ^2m}{m}\right).}
\tag{0.3}
\]

Thus for \(H=L\sqrt m\), fixed \(L\), every corner has

\[
 HJ(M_\varepsilon)=o(W).
\tag{0.4}
\]

Moreover, the initial factor may be relabelled before freezing the chain
so that simultaneously

\[
 \boxed{J(M_0)+r=O(W/m),
 \qquad J(M_\varepsilon)=O(W/m)\text{ for every corner}.}
\tag{0.4a}
\]

The complete upper-flag Gram matrix has an exact signed path form.  If
\(z_K\) is the load column of packet \(K\), then

\[
 \begin{array}{c|c}
 K,L\text{ in the same block}&\langle z_K,z_L\rangle_w\ge0,\\
 K,L\text{ in neighboring blocks}&\langle z_K,z_L\rangle_w\le0,\\
 \text{block distance at least two}&\langle z_K,z_L\rangle_w=0.
 \end{array}
\tag{0.5}
\]

Write

\[
 G_{\rm in}:=
 \sum_j\sum_{K<L\in\mathscr P_j}\langle z_K,z_L\rangle_w,
\tag{0.6}
\]

\[
 G_{\rm join}:=
 -\sum_{j=1}^{m-2}
   \sum_{\substack{K\in\mathscr P_j\\L\in\mathscr P_{j+1}}}
       \langle z_K,z_L\rangle_w.
\tag{0.7}
\]

Both quantities are nonnegative.  For independent fair packet bits and
the doubled factorial floor excess \(\mathcal Q_w\),

\[
 \boxed{
 \mathbb E\mathcal Q_w(M_\varepsilon)
 =\mathcal Q_w(M_0)-\frac12
       (G_{\rm in}+G_{\rm join}).}
\tag{0.8}
\]

There is also a deterministic joined-mode descent.  Switching every
packet in every block cancels each block's flat endpoint polynomial and
leaves only the negative neighboring-block terms:

\[
 \boxed{
 \mathcal Q_w(M_{\bf1})
 =\mathcal Q_w(M_0)-2G_{\rm join}.}
\tag{0.8a}
\]

Thus \(G_{\rm join}>0\) gives an explicit, rather than averaged, legal
energy decrease with the same run bound.

The within-block term is exactly the previously audited collision charge:

\[
 \frac12G_{\rm in}=\sum_{j=1}^{m-1}\mathcal C_j.
\tag{0.9}
\]

The second term is new.  It is a nonnegative joined-owner cross-Gram gap
created by overlapping the odd and even charts; it is strict exactly when
some neighboring packet columns meet in their common stratum.

At the first upper depth, every within-block charge vanishes.  The
nonzero switches of block \(j\) form a matching \(E_j\) from the
first-avoided target stratum \(j\) to stratum \(j+1\).  The union of all
\(E_j\) is a disjoint union of directed paths.  If

\[
 \mathfrak J_1
 =\sum_{j=1}^{m-2}
   |\operatorname{head}(E_j)\cap\operatorname{tail}(E_{j+1})|,
\tag{0.10}
\]

then

\[
 \boxed{G_{{\rm in},1}=0,
 \qquad G_{{\rm join},1}=w_1^+\mathfrak J_1.}
\tag{0.11}
\]

More sharply, selecting every first-upper switch gives the exact integral
identity

\[
 \boxed{Q_1(M_{\bf1})=Q_1(M_0)-2\mathfrak J_1.}
\tag{0.12}
\]

Thus overlapping charts can evade the single-block first-upper flatness
identity, and do so exactly when \(\mathfrak J_1>0\).

There is an exact support-level charged-coverage bound.  If \(e_j=|E_j|\)
and \(Z_{j+1}\) is the number of first-upper targets in stratum \(j+1\),
then

\[
 \boxed{
 \mathfrak J_1
 \ge\sum_{j=1}^{m-2}
       (e_j+e_{j+1}-Z_{j+1})_+.}
\tag{0.13}
\]

At all depths, if \(s^+_{j,q}\) and \(s^-_{j+1,q}\) are the two joined
support sizes in stratum \(j+1\), and \(Z_{j+1,q}\) is the size of that
whole target stratum, then

\[
 \boxed{
 G_{\rm join}\ge
 \sum_{j=1}^{m-2}\sum_{q=1}^H w_q^+
 (s^+_{j,q}+s^-_{j+1,q}-Z_{j+1,q})_+.}
\tag{0.13a}
\]

This lower bound is sharp from support sizes alone, but it is normally
zero in every fixed early stratum: one always has

\[
 e_j\le4\operatorname{Cat}_{m-1}=O(W/m),
\tag{0.14}
\]

whereas, for fixed \(s\),

\[
 Z_s=\left(\frac14\left(\frac34\right)^{s-1}+o(1)\right)W.
\tag{0.15}
\]

Consequently the atlas proves a nonincreasing overlapping-chart move,
strict when \(G_{\rm in}+G_{\rm join}>0\), but does not prove a uniform
contraction.  The exact missing estimate is

\[
 \boxed{
 \frac12(G_{\rm in}+G_{\rm join})
 \ge \eta\,\mathcal Q_w(M_0)-o(W)}
\tag{0.16}
\]

for some fixed \(\eta>0\), together with a recentering theorem which
supplies the same atlas after taking a mixed corner.  Under those two
statements, \(O(\log m)\) rounds give \(o(W)\) energy and add only
\(O(W\log ^3m/m)=o(W/H)\) runs.  Neither statement is proved here, so no
constant-one conclusion is claimed.

## 1. Token maps and the common factor chain

For a lower root \(S\) avoiding \(P_j\), let \(e_j(S)\) denote its
token in \(F_j\), and let \(f_j(S)\) be that token's predecessor middle
owner.  If \(S\in\mathcal D_j\), then \(\tau_jS=S\) pointwise, and
(0.1) gives

\[
 \boxed{
 e_{j+1}(S)=\tau_je_j(S),
 \qquad
 f_{j+1}(S)=\tau_jf_j(S).}
\tag{1.1}
\]

The families \(\mathcal D_j\) are pairwise disjoint.  Indeed, if
\(j<k\), every member of \(\mathcal D_j\) avoids \(P_j\), whereas
every member of \(\mathcal D_k\) meets \(P_j\).

For each \(S\in\mathcal D_j\), choose either \(e_j(S)\) or
\(e_{j+1}(S)\).  Packet choices are special cases in which this bit is
constant on a maximal physical interval.  We first prove legality for
arbitrary rootwise choices.

## 2. Simultaneous legality for all adjacent blocks

### Theorem 2.1 (full overlapping rootwise cube)

For the factor chain (0.1), every rootwise choice over all
\(\mathcal D_j\), \(1\le j<m\), together with the unchanged base
tokens, is a lower-saturating, middle-injective token matching.

### Proof

Lower saturation is immediate from the disjointness of the
\(\mathcal D_j\): every affected root receives exactly one of its two
tokens, and every other root retains its base token.

We prove middle injectivity.  Within one block, suppose

\[
 f_j(S)=f_{j+1}(T)=\tau_jf_j(T).
\tag{2.1}
\]

The common owner avoids both \(P_j\) and \(P_{j+1}\), hence is fixed by
\(\tau_j\).  Thus \(f_j(S)=f_j(T)\), and exactness of \(F_j\) gives
\(S=T\).  A corner chooses only one token at that root.  Same-phase
owners are distinct by the same injectivity.

Now take \(S\in\mathcal D_j\) and \(T\in\mathcal D_k\), with
\(j<k\).  If \(k\ge j+2\), an owner over \(S\) avoids at least one of
\(P_j,P_{j+1}\).  The root \(T\), and hence every owner over \(T\),
meets both.  Equality is impossible.

It remains to treat neighboring blocks, \(k=j+1\).  The root \(T\)
meets \(P_j\), so an owner \(f_j(S)\), which avoids \(P_j\), cannot
equal either owner over \(T\).  Suppose instead that \(S\) uses
\(f_{j+1}(S)\).  If \(T\) also uses \(f_{j+1}(T)\), injectivity inside
\(F_{j+1}\) excludes equality.  In the only remaining case, suppose

\[
 f_{j+1}(S)=f_{j+2}(T)
 =\tau_{j+1}f_{j+1}(T).
\tag{2.2}
\]

The common owner avoids both \(P_{j+1}\) and \(P_{j+2}\), so it is
fixed by \(\tau_{j+1}\).  Equation (2.2) reduces to
\(f_{j+1}(S)=f_{j+1}(T)\).  Injectivity again gives \(S=T\), contrary
to \(\mathcal D_j\cap\mathcal D_{j+1}=\varnothing\).

Finally consider an unchanged background root \(R\).  The old candidate
over \(S\in\mathcal D_j\) occurs with the background token over \(R\)
in the base matching.  The new candidate occurs with the same background
token in the coherent endpoint obtained by swapping only priority
positions \(j,j+1\); that endpoint changes precisely the roots in
\(\mathcal D_j\).  Both coherent matchings are middle-simple.  Thus no
changed candidate collides with the unchanged background.  All owner
pairs have now been exhausted.  \(\square\)

This theorem is the simultaneous odd/even legality statement.  It is not
an appeal to commuting priority permutations: neighboring transpositions
do not commute.  Legality follows instead from the common-base identities
(1.1) and the meet/avoid filtration.

## 3. Exact packet and run accounting

Let

\[
 R_m=\frac1{2m-1}\binom{2m-1}{m-1}
 =\operatorname{Cat}_{m-1}.
\tag{3.1}
\]

In one \(F_j\)-row, membership in \(\mathcal D_j\) is the conjunction
of \(j\) pair-meeting or pair-avoidance predicates.  One such predicate
has at most four cyclic boundary edges.  Hence it has at most \(2j\)
cyclic components.  Therefore

\[
 r_j\le\min\{2jR_m,|\mathcal D_j|\}.
\tag{3.2}
\]

The category-tail estimate

\[
 |\mathcal D_j|\le C\sqrt m\binom{2m-1}{m-1}(3/4)^{j-1}
\tag{3.3}
\]

and a split at \(20\log m\) give

\[
 \sum_{j=1}^{m-1}r_j
 =O(R_m\log ^2m)
 =O(W\log ^2m/m).
\tag{3.4}
\]

Switching one packet clears one interval in its old row and fills one
interval in its new row.  Each operation raises the cyclic one-run count
by at most one.  This remains true when the same factor participates in
the two neighboring blocks: applying the interval operations one at a
time gives the deterministic bound

\[
 J(M_\varepsilon)-J(M_0)\le2r.
\tag{3.5}
\]

There are at most four new raw \(0/1\) boundary edges per packet.  Since
the base first-avoided matching has

\[
 J(M_0)=O(W\log ^2m/m),
\tag{3.6}
\]

equations (3.4)--(3.6) prove (0.3)--(0.4).

If a packet has length less than \(\ell\), it contains fewer than
\(\ell\) affected roots.  Therefore all packets shorter than \(\ell\)
together contain fewer than \(\ell r\) roots.  At
\(\ell=H=L\sqrt m\), (3.4) gives

\[
 H r=O_L(W\log ^2m/\sqrt m)=o(W).
\tag{3.7}
\]

Thus all but \(o(W)\) affected roots which belong to packets lie in
packets of length at least \(H\).  This is an exact component-size
statement; no mean-length inference is being used.

There is also a jointly chosen chained family with no logarithmic loss.
Start from any abstract exact factor on \(2m-1\) points, give \(F_1\) a
uniform random relabelling on \([n]\setminus P_1\), and then impose the
recursion (0.1).  For every \(j\), the marginal law of \(F_j\) is a
uniform relabelling on \([n]\setminus P_j\); correlations between the
different factors do not affect expectations of the summed nonnegative
row counts.

Put

\[
 A_m=\binom{2m-1}{m-1},
 \qquad T=\binom{2m+1}{m-1},
\]

\[
 p_m=\frac{3m-2}{4m-2},
 \qquad
 \alpha_m=\frac{m}{2(2m-1)},
 \qquad
 p'_m=\frac{3(m-1)}{4m-6}\le\frac56
 \quad(m\ge6).
\tag{3.8}
\]

We record the elementary product bound used here.  If a uniform
\(k\)-subset of a finite ground set is tested against disjoint coordinate
pairs \(Q_1,\ldots,Q_s\), then

\[
 \Pr(X\cap Q_h\ne\varnothing\text{ for every }h\le s)
 \le\prod_{h=1}^s\Pr(X\cap Q_h\ne\varnothing).
\tag{3.8a}
\]

Indeed, let \(A\) be the union of the first \(s-1\) pairs and condition
on \(R=|X\cap A|\).  Given \(R=r\), the choices inside and outside
\(A\) are independent uniform subsets.  The conditional probability of
meeting every pair inside \(A\) is nondecreasing in \(r\): couple a
uniform \(r\)-subset to a uniform \((r+1)\)-subset by adjoining a
uniform missing point.  The conditional probability of meeting the last
pair is nonincreasing in \(r\), because the outside sample has size
\(k-r\).  Oppositely monotone functions of one random variable have
nonpositive covariance, so the last-pair event is negatively correlated
with the conjunction of the preceding events.  Induction proves (3.8a).

After conditioning a current root to avoid the successor pair, (3.8a)
applies on the remaining \(2m-3\) coordinates and gives the factor
\((p'_m)^s\) below.  Without that conditioning it gives \(p_m^s\).

The directed-boundary count for the first-avoided endpoint and for all
\(\mathcal D_j\)-carriers gives, respectively,

\[
 \mathbb EJ(M_0)
 \le\frac{T}{2m-1}
   +\frac{A_m}{m-1}\sum_{s\ge0}s p_m^s
 =O(W/m),
\tag{3.9}
\]

\[
 \mathbb Er
 \le\frac{T}{2m-1}
  +A_m\alpha_m\sum_{s\ge0}(p'_m)^s
       \left(\frac2m+\frac{s}{m-1}\right)
 =O(W/m).
\tag{3.10}
\]

For (3.9), a boundary at priority depth \(s\) requires the entering
coordinate to be the unique representative of one of the \(s\) earlier
pairs.  For (3.10), in addition, it may insert one of the two coordinates
of the avoided successor pair.  Exposing disjoint earlier pairs gives the
geometric factors \(p_m^s,(p'_m)^s\).  These are exactly the two displayed
possibilities, so (3.9)--(3.10) count every directed boundary.

Some one relabelling therefore satisfies

\[
 \boxed{J(M_0)+r=O(W/m).}
\tag{3.11}
\]

For that fixed recursively conjugate family, every full overlapping-atlas
corner has \(J=O(W/m)\).  The generic bound (0.3) remains the statement
for an already frozen arbitrary factor family.  The estimates were written
for \(m\ge6\); enlarging the absolute constant covers the finitely many
values \(3\le m<6\).

## 4. The signed tridiagonal Gram law

At signed depth \(q\), let \(L_q(S),U_q(S)\) be the old lower and upper
flags of a root in \(\mathcal D_j\).  Since every lower flag is a subset
of the pointwise fixed root \(S\),

\[
 L_q^{\rm new}(S)=L_q^{\rm old}(S).
\tag{4.1}
\]

For upper flags,

\[
 U_q^{\rm new}(S)=\tau_jU_q^{\rm old}(S).
\tag{4.2}
\]

An old upper flag avoids \(P_j\).  If it also avoids \(P_{j+1}\), its
innovation is zero.  Otherwise its innovation is

\[
 d_{j,S,q}={\bf e}_{\tau_jU_q(S)}-{\bf e}_{U_q(S)},
\tag{4.3}
\]

with negative support in first-avoided stratum \(j\) and positive support
in stratum \(j+1\).  A packet column is the sum of (4.3) over its roots.

Two packets in one block have nonnegative inner product: positive-negative
cross terms lie in disjoint strata, while equal-sign products are
nonnegative.  Packets in blocks whose indices differ by at least two have
disjoint stratum support.  For neighboring blocks \(j,j+1\), their only
common stratum is \(j+1\); the first packet is positive there and the
second is negative there.  Their inner product is therefore nonpositive.
This proves (0.5), depth by depth and hence for every finite nonnegative
weighted sum.

Let \(x\) be the base load and define

\[
 g_K=2\langle x,z_K\rangle_w+\|z_K\|_w^2.
\tag{4.4}
\]

Because every column has zero mass at every rank, the exact doubled
floor-energy polynomial is

\[
 \mathcal Q_w(I)-\mathcal Q_w(\varnothing)
 =\sum_{K\in I}g_K
  +2\sum_{K<L\in I}\langle z_K,z_L\rangle_w.
\tag{4.5}
\]

No floor term was omitted: the integral floor baseline is constant on
this mass fibre.

For one block \(j\), selecting all its packets is the coherent adjacent
priority swap.  Pair symmetry permutes the complete upper load in the
union of strata \(j,j+1\), fixes all lower loads, and preserves middle
simplicity.  Hence its floor energy is rankwise equal to the base energy,
and (4.5) gives

\[
 \sum_{K\in\mathscr P_j}g_K
 =-2\sum_{K<L\in\mathscr P_j}\langle z_K,z_L\rangle_w.
\tag{4.6}
\]

Sum (4.6) over all blocks.  Under independent fair packet bits, a linear
term is selected with probability \(1/2\) and a pair term with probability
\(1/4\).  Only same-block and neighboring-block pairs survive.  Therefore

\[
 \begin{aligned}
 \mathbb E[\mathcal Q_w(M_\varepsilon)-\mathcal Q_w(M_0)]
 &=-G_{\rm in}
   +\frac12G_{\rm in}
   -\frac12G_{\rm join}\\
 &=-\frac12(G_{\rm in}+G_{\rm join}),
 \end{aligned}
\tag{4.7}
\]

which proves (0.8).

If every packet is selected, (4.5) and (4.6) cancel the linear and
within-block terms block by block.  The remaining adjacent-block cross
sum is \(-2G_{\rm join}\).  Hence

\[
 \mathcal Q_w(M_{\bf1})-\mathcal Q_w(M_0)
 =-2G_{\rm join},
\tag{4.7a}
\]

proving (0.8a).

More generally, select every packet independently with a common bias
\(p\in[0,1]\).  The linear terms in (4.5) have expectation
\(-2pG_{\rm in}\), while the within and adjacent pair terms have
expectation \(2p^2(G_{\rm in}-G_{\rm join})\).  Therefore

\[
 \boxed{
 \mathbb E_p\mathcal Q_w(M_\varepsilon)
 =\mathcal Q_w(M_0)-D(p),
 \qquad
 D(p)=2p(1-p)G_{\rm in}+2p^2G_{\rm join}.}
\tag{4.7b}
\]

This contains fair rounding at \(p=1/2\) and the explicit all-on corner
at \(p=1\).  Maximizing the quadratic gives

\[
 \boxed{
 D_*:=\max_{0\le p\le1}D(p)=
 \begin{cases}
 \displaystyle\frac{G_{\rm in}^2}
 {2(G_{\rm in}-G_{\rm join})},
 &0\le G_{\rm join}\le G_{\rm in}/2,\\[8pt]
 2G_{\rm join},&G_{\rm join}\ge G_{\rm in}/2,
 \end{cases}}
\tag{4.7c}
\]

where the first line is used only when \(G_{\rm in}>0\).  In particular,
some legal integral corner descends by at least \(D_*\).

For \(S\in\mathcal D_j\), put

\[
 \mu_{j,q,U}
 =|\{S\in\mathcal D_j:U_q(S)=U\}|.
\]

The proper-window hypothesis \(H\le m-2\) ensures that equal targets from
distinct roots occur in distinct physical packets.  Within one block, the
equal-target calculation therefore gives

\[
 \sum_{K<L\in\mathscr P_j}\langle z_K,z_L\rangle_w
 =2\sum_{q=1}^Hw_q^+
   \sum_{U:\,U\cap P_{j+1}\ne\varnothing}
        \binom{\mu_{j,q,U}}2
 =2\mathcal C_j.
\tag{4.8}
\]

This proves (0.9).  The adjacent term has the equally explicit form

\[
 G_{\rm join}
 =\sum_{j=1}^{m-2}\sum_{q=1}^Hw_q^+
   \sum_T a^+_{j,q,T}a^-_{j+1,q,T},
\tag{4.9}
\]

where \(a^+_{j,q,T}\) is the number of block-\(j\) new flags equal to
the stratum-\((j+1)\) target \(T\), and \(a^-_{j+1,q,T}\) is the
number of block-\((j+1)\) old flags equal to \(T\).  Formula (4.9) is
the joined-owner cross-Gram charge; it is not an abstract Gram remainder.

Let

\[
 S^+_{j,q}=\{T:a^+_{j,q,T}>0\},
 \qquad
 S^-_{j+1,q}=\{T:a^-_{j+1,q,T}>0\},
\]

and put \(s^+_{j,q}=|S^+_{j,q}|\),
\(s^-_{j+1,q}=|S^-_{j+1,q}|\).  Every nonzero integral product in
(4.9) is at least one, and both supports lie in the same stratum of size
\(Z_{j+1,q}\).  Hence

\[
 \begin{aligned}
 \sum_Ta^+_{j,q,T}a^-_{j+1,q,T}
 &\ge |S^+_{j,q}\cap S^-_{j+1,q}|\\
 &\ge(s^+_{j,q}+s^-_{j+1,q}-Z_{j+1,q})_+.
 \end{aligned}
\tag{4.10}
\]

Summing (4.10) proves the full-window charged-coverage bound (0.13a).
The stratum size appearing there is explicitly

\[
 Z_{s,q}=
 \sum_{h=0}^{s-1}(-1)^h\binom{s-1}{h}
 \binom{2m-1-2h}{m+q},
\tag{4.11}
\]

with impossible binomial coefficients interpreted as zero.  This is
inclusion-exclusion over the earlier pairs missed by a rank-\((m+q)\)
target which already avoids \(P_s\).

## 5. Exact first-upper matching and path law

The autonomous token mass at this rank is

\[
 T=\binom{2m+1}{m-1}=\frac{m}{m+2}W<W,
\]

so its exact integral floor is \(c_1^+=0\) and

\[
 Q_1(x)=\sum_Ux_U(x_U-1).
\tag{5.0}
\]

No division by a zero floor is used below.

Fix one row

\[
 \pi=(x_0,\ldots ,x_{2m-2})
\]

of \(F_j\), and a token rooted at

\[
 S=I_\pi(i,m-1).
\]

Its first upper flag and its two adjacent middle windows are

\[
 U=I_\pi(i-1,m+1),
\tag{5.1}
\]

\[
 Y=I_\pi(i-1,m),
 \qquad X=I_\pi(i,m).
\tag{5.2}
\]

Writing

\[
 E(U,S)=U\setminus S
 =\{x_{i-1},x_{i+m-1}\},
\tag{5.3}
\]

we have

\[
 Y=U\setminus\{x_{i+m-1}\},
 \qquad
 X=U\setminus\{x_{i-1}\}.
\tag{5.4}
\]

Every rank-\(m\) target has one window occurrence in an exact local
factor.  Consecutive tokens in one row do of course share that one window,
so the following small adjacency check is necessary.  Suppose two token
starts \(i,k\) have the same first upper target \(U\) and their collars
share a point \(x\).  Then the facet \(U\setminus\{x\}\) is one of the
two windows at starts \(i-1,i\) and also one of the two windows at starts
\(k-1,k\).  Uniqueness of its window occurrence forces the two tokens to
lie in the same row and, unless \(i=k\), forces \(k=i-1\) or
\(k=i+1\).  But two consecutive length-\((m+1)\) windows in a cyclic
order of \(2m-1\) distinct coordinates are different (here \(m\ge3\)).
Thus distinct occurrences with the same \(U\) have disjoint two-point
collars.

Now take two changed roots in \(\mathcal D_j\) with the same nonfixed
first upper target \(U\).  Both roots avoid \(P_{j+1}\), whereas
\(U\) meets \(P_{j+1}\).  Therefore

\[
 \varnothing\ne U\cap P_{j+1}
 \subseteq E(U,S)\cap E(U,T),
\]

contradicting collar disjointness.  We have proved

\[
 \boxed{\mu_{j,1,U}\le1.}
\tag{5.5}
\]

Thus the nonzero first-upper switches of one block have distinct old
targets and distinct new targets.  Old targets lie in stratum \(j\), new
targets in stratum \(j+1\), so the switch columns form a matching

\[
 E_j:\quad U\longrightarrow\tau_jU.
\tag{5.6}
\]

Let \(x\) be the base first-upper load.  The coherent full block swap
permutes the complete stratum-\(j,j+1\) load by \(\tau_j\).  Because the
support pairs in (5.6) are disjoint, on every edge \(U\to V\) this vector
identity reads

\[
 x_U-1=x_V,
 \qquad x_V+1=x_U.
\tag{5.7}
\]

Moving the token along one edge therefore changes the doubled first-upper
floor energy by

\[
 2(x_V-x_U)+2=0.
\tag{5.8}
\]

This proves rootwise, and not merely average, first-upper flatness inside
one block.

Edges from nonneighboring blocks have disjoint strata.  At a target in
stratum \(j+1\), there is at most one incoming edge from \(E_j\) and at
most one outgoing edge from \(E_{j+1}\).  Hence

\[
 E_1\cup\cdots\cup E_{m-1}
\]

is a disjoint union of directed paths, with every edge increasing the
stratum index by one.  Two edge columns have nonzero inner product exactly
when the first edge ends where the second begins, and then their inner
product is \(-1\).  Consequently, for any selected edge set \(I\),

\[
 \boxed{
 Q_1(M_I)-Q_1(M_0)
 =-2\,|\{\text{two consecutive selected edges on one path}\}|.}
\tag{5.9}
\]

Packet choices merely require certain groups of edges to be selected
together, so (5.9) remains valid.  Taking all edges proves (0.12), and
summing the adjacent cross products proves (0.11).

## 6. Quantified joined coverage and its sharp limitation

Let \(\mathcal T_s\) be the rank-\((m+1)\) targets whose first avoided
pair is \(P_s\), and put \(Z_s=|\mathcal T_s|\).  The heads of \(E_j\)
and the tails of \(E_{j+1}\) are subsets of \(\mathcal T_{j+1}\), of
sizes \(e_j\) and \(e_{j+1}\), respectively.  Inclusion-exclusion gives

\[
 |\operatorname{head}(E_j)\cap\operatorname{tail}(E_{j+1})|
 \ge(e_j+e_{j+1}-Z_{j+1})_+.
\tag{6.1}
\]

Summing proves (0.13).  Equality can occur for arbitrary subsets of a
fixed universe, so no stronger estimate follows from the three support
sizes alone.

There is a factor-independent collar bound.  In one cyclic row, a fixed
coordinate occurs in the two-point collar (5.3) at exactly two starts.
The two coordinates of \(P_{j+1}\) therefore occur in at most four
collars.  Restricting to \(\mathcal D_j\) can only decrease the count, so

\[
 e_j\le4R_m.
\tag{6.2}
\]

Using

\[
 \frac{R_m}{W}
 =\frac{m(m+1)}{(2m-1)(2m)(2m+1)},
\tag{6.3}
\]

we obtain

\[
 e_j\le\left(\frac1{2m}+O(m^{-2})\right)W,
\tag{6.4}
\]

and

\[
 \mathfrak J_1
 \le4(m-2)R_m
 =\left(\frac12+O(m^{-1})\right)W.
\tag{6.5}
\]

The exact stratum count is

\[
 Z_s=
 \sum_{h=0}^{s-1}(-1)^h\binom{s-1}{h}
 \binom{2m-1-2h}{m+1}.
\tag{6.6}
\]

For fixed \(s\), dividing each term by \(W\) and using the fixed-codimension
binomial ratio gives

\[
 \frac{Z_s}{W}
 \longrightarrow
 \frac14\sum_{h=0}^{s-1}\binom{s-1}{h}(-1/4)^h
 =\frac14(3/4)^{s-1},
\tag{6.7}
\]

which proves (0.15).  Equations (6.4) and (6.7) show that the right side
of (6.1) is zero for every fixed \(j\) and all sufficiently large \(m\).
Thus the desired joined gap is an exact nonnegative quantity, but its
strict positivity or a quantitative lower bound cannot come from support
masses or row-boundary counts alone.
It must use a genuine incidence-alignment theorem between consecutive
pair collars in the common factor.

For comparison with the first local phase, let

\[
 A_m=\binom{2m-1}{m-1},
 \qquad B_m=\binom{2m-1}{m+1},
\]

and let \(h_1(F_1)\) be the number of missing length-\((m+1)\) interval
targets in \(F_1\).  The phase-one mass is \(A_m\), its support has size
\(B_m-h_1(F_1)\), and \(\binom r2\ge r-1\) for every positive integer
\(r\).  Hence the base first-upper doubled floor energy obeys

\[
 \boxed{
 Q_1(M_0)
 \ge2(A_m-B_m+h_1(F_1))
 =\frac{2W}{2m+1}+2h_1(F_1).}
\tag{6.8}
\]

Single parity layers leave all of (6.8) invariant.  The overlapping atlas
can reduce it only through the joined paths (5.9).  In particular, a
large local shadow hole is not burned by within-block interval curvature;
it must be transported through consecutive pair collars or excluded by an
independent near-rainbow factor theorem.

## 7. The exact conditional recurrence

Define the one-round charged curvature

\[
 \Gamma_w(M_0)=\frac12(G_{\rm in}+G_{\rm join}).
\tag{7.1}
\]

Optimizing the biased rounding identity (4.7b), put

\[
 \Gamma_w^\star(M_0)=D_*.
\tag{7.1a}
\]

Equation (4.7b) and the deterministic run bound imply the existence of a
literal integral corner satisfying

\[
 \boxed{
 \mathcal Q_w(M_1)\le\mathcal Q_w(M_0)-\Gamma_w^\star(M_0),
 \qquad
 J(M_1)\le J(M_0)+2r.}
\tag{7.2}
\]

The same corner creates at most \(4r\) new raw row-boundary edges and at
most \(2r\) new selected runs.  Thus, when \(r>0\), the exact guaranteed
descent per boundary and per run surcharge is

\[
 \boxed{
 \frac{\mathcal Q_w(M_0)-\mathcal Q_w(M_1)}
      {\#\text{ new raw boundary edges}}
 \ge\frac{\Gamma_w^\star(M_0)}{4r},
 \qquad
 \frac{\mathcal Q_w(M_0)-\mathcal Q_w(M_1)}
      {(J(M_1)-J(M_0))_+}
 \ge\frac{\Gamma_w^\star(M_0)}{2r}.}
\tag{7.2a}
\]

If one of the displayed denominators is zero, the corresponding ratio is
omitted.  Relative to the complete endpoint ledger, the numerator is
still \(\Gamma_w^\star(M_0)\) and the denominator is at most
\(2J(M_0)+4r=O(W\log ^2m/m)\), or \(O(W/m)\) for the jointly relabelled
chain (3.11).  Thus a round with \(\Gamma_w(M_0)=\Omega(W)\) descends by
\(\Omega(m/\log ^2m)\) per endpoint in the frozen-factor bound and by
\(\Omega(m)\) per endpoint in the jointly chosen chain.

Suppose, in addition to the proved atlas theorem, that every state reached
in this way admits a recentered chained-factor atlas with

\[
 \Gamma_w^\star(M)\ge\eta\mathcal Q_w(M)-\epsilon_mW,
 \qquad 0<\eta\le1,\quad 0\le\epsilon_m=o(1),
\tag{7.3}
\]

and with at most \(Cr\) new packets, where
\(r=O(W\log ^2m/m)\).  Choosing the decreasing corner at each round gives

\[
 \mathcal Q_w(M_{t+1})
 \le(1-\eta)\mathcal Q_w(M_t)+\epsilon_mW,
\tag{7.4}
\]

and hence, by induction,

\[
 \boxed{
 \mathcal Q_w(M_t)
 \le(1-\eta)^t\mathcal Q_w(M_0)
    +\frac{\epsilon_m}{\eta}W.}
\tag{7.5}
\]

If \(\mathcal Q_w(M_0)=O(W)\), choose any \(t=t(m)\to\infty\) with
\(t=O(\log m)\).  Then (7.5) is \(o(W)\), while the cumulative new-run
count is

\[
 O(tr)=O(W\log ^3m/m)=o(W/\sqrt m)=o(W/H).
\tag{7.6}
\]

Thus the exact run arithmetic supports a genuine iterative contraction;
the obstruction is not boundary accumulation.  The two unproved inputs
are precisely the charged-coverage inequality (7.3) and recentering after
a mixed all-adjacent corner.  Formula (4.9) identifies the incidence
quantity which a positive theorem must control, while (6.1)--(6.7) show
that marginal support sizes alone cannot control it.

## 8. Proved and conditional boundary

The following statements are proved here.

1. One recursively conjugate fixed factor family supports all adjacent
   interval charts simultaneously.
2. Arbitrary choices in overlapping odd and even blocks preserve lower
   saturation and distinct middle ownership.
3. Every corner has \(O(W\log ^2m/m)=o(W/H)\) runs at a fixed Gaussian
   window.
4. The full Gram matrix is signed tridiagonal, and independent full-atlas
   rounding has the exact floor descent (0.8).
5. Within-block first-upper curvature is identically zero, while adjacent
   blocks create the explicit nonnegative joined gap (0.10)--(0.12),
   strict exactly when \(\mathfrak J_1>0\).
6. The exact unconditional joined-coverage lower bound is (0.13); from
   support counts alone it is asymptotically zero in every fixed early
   stratum.

What is not proved is equally exact.  There is no bound of
\(G_{\rm in}+G_{\rm join}\) below by a fixed fraction of the surviving
floor energy.  Nor is a new chained-factor atlas constructed with the
same quantifiers around an arbitrary mixed corner.  Therefore (7.4) is a
conditional recurrence, not a constant-one theorem.
