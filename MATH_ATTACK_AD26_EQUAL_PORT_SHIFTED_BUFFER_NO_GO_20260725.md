# AD26: the equal-adjacent-port shifted-buffer telescope has an exact cap obstruction

Date: 2026-07-25

Method: pure mathematics only. No computation, finite search, solver, or web
input is used.

## 0. Exact outcome

Put

\[
 n=2Q.
\]

In the rectangular truncated static-cube compiler, fix a row pair \(i\)
and two adjacent ports \(j,j+1\), and impose one common bit

\[
 E_{ij}=E_{i,j+1}=e.
\tag{0.1}
\]

Let

\[
 q=q_{ij},\qquad r=Q-q.
\tag{0.2}
\]

Thus the active row pair starts at collar boundaries

\[
 r,\quad r+2,\quad r+2,\quad r+4
\tag{0.3}
\]

in the four source states

\[
 A_j,\quad C_j,\quad A_{j+1},\quad C_{j+1}.
\tag{0.4}
\]

Assume \(j\le t-3\), so that all four source routes occur. Couple the two
values of \(e\) by the slot-equivariant flush/reload rule: within each
route, the ordered buffer list is fixed under the active row
transposition. The lists used in different routes may otherwise be
arbitrary and may be correlated or shifted in any way.

Then the complete two-port physical incidence difference satisfies

\[
 \boxed{
 \|\Delta_h\|_2^2\ge 8
 \qquad(r+5\le h\le 2Q-1).}
\tag{0.5}
\]

Consequently

\[
 \boxed{
 \sum_{h=0}^{2Q}\|\Delta_h\|_2^2
 \ge 8(Q+q)-26.}
\tag{0.6}
\]

The high-prefix interval alone contributes \(8(Q+q-5)\).  The additional
fourteen units in (0.6) come from the same old-collar tag at the three
preceding ranks, including a two-unit half-trace at the first one.

The lower bound is sharp on every displayed rank. There is an exact legal
choice of the background column signatures and common buffers for which
the two phase-matched middle source traces cancel and

\[
 \|\Delta_h\|_2^2=8
 \qquad(r+5\le h\le2Q-1).
\tag{0.7}
\]

The two designated rectangles do survive:

\[
 \Delta J=\pm(\rho_{ij}+\rho_{i,j+1}),
 \qquad
 \|\Delta J\|_2^2=8.
\tag{0.8}
\]

Thus the proposal retains its marked drift but cannot have \(O(1)\) total
vertical connector variance. A fair common bit already has conditional
connector covariance trace at least

\[
 \boxed{2(Q+q)-\frac{13}{2}.}
\tag{0.9}
\]

The obstruction is not a failure to choose the buffers cleverly. It is a
buffer-independent cap flux: the initial source ribbon contains the last
old collar label, which every later source cap omits, while the final
source ribbon contains both labels of the next column pair, which every
earlier cap omits.

## 1. Exact scope and source-trace formula

The quotient state is

\[
 \omega=(A;z_1,\ldots,z_n;B),
\]

and its prefix flag is

\[
 F_h(\omega)=A\cup\{z_1,\ldots,z_h\},
 \qquad 0\le h\le n.
\tag{1.1}
\]

For distinct active labels \(u,v\) and a base \(D\) containing neither,
write

\[
 T_{uv}(D)=e_{D+u}-e_{D+v}.
\tag{1.2}
\]

Different bases give orthogonal vectors, and

\[
 \|T_{uv}(D)\|_2^2=2.
\tag{1.3}
\]

Suppose \(u,v\) occupy adjacent source-collar slots \(a,a+1\). Under a
slot-equivariant buffer coupling, toggling their order gives, after
aggregation over the source-flush part of one route,

\[
 D_h^{\rm src}
 =\varepsilon\bigl(T_{uv}(K_h)-T_{uv}(J_h)\bigr)
 \qquad(a+1\le h\le n-1),
\tag{1.4}
\]

where \(\varepsilon\in\{1,-1\}\) records the orientation. The exact
flush formulas give

\[
 K_h\ne J_h\qquad(a+1\le h\le n-1).
\tag{1.5}
\]

Hence

\[
 \boxed{\|D_h^{\rm src}\|_2^2=4.}
\tag{1.6}
\]

The target-reload difference of a pair at boundary \(a\) is supported
only on

\[
 0\le h\le a.
\tag{1.7}
\]

These statements allow arbitrary legal buffer lists in different routes.
Only the natural coherence needed to compare the two orientations of the
same route is imposed: its buffer slots do not change when \(u,v\) are
transposed.

### 1.1 Complete one-route ribbon identity

The high-rank formula above is only one part of the exact routed
transition.  The complete identity distinguishes the genuine ribbon
structure from the false assertion that there is just one ribbon.

Let the source core be \(D\), let the prescribed core--tail exchange be
\(\mathfrak a\in D\), \(\mathfrak b\in B\), and suppose

\[
 z_r=u,\qquad z_{r+1}=v.
\]

Put

\[
 s=n-r+1,\qquad
 P=\{z_1,\ldots,z_{r-1}\},\qquad
 T=\{z_{r+2},\ldots,z_n\}.
\tag{1.8}
\]

Choose the flush buffers \(x_1,\ldots,x_n,\mathfrak a\) as in the routing
theorem.  For a base \(C\) of size \(m-Q+h-1\), define

\[
 \partial_h(C)
 =e_{C+u}^{(m-Q+h)}-e_{C+v}^{(m-Q+h)}.
\tag{1.9}
\]

The ordinary source-boundary bases are

\[
 K_0=D+P,
\tag{1.10}
\]

and, for \(1\le \ell\le s-1\),

\[
 K_\ell
 =D+P+\{\mathfrak b\}
   +\{z_{n-\ell+2},\ldots,z_n\},
\tag{1.11}
\]

where the last suffix is empty when \(\ell=1\).  Let

\[
 q^*=(x_s,x_{s-1},\ldots,x_1,z_1,\ldots,z_{r-1}).
\]

The single recycle-state column has bases

\[
 G_h
 =D-\{x_1,\ldots,x_s\}+\{\mathfrak b\}+T
  +\operatorname{pref}_h(q^*),
 \qquad 0\le h\le n.
\tag{1.12}
\]

Finally, the target-reload bases are

\[
 H_h
 =D-\{\mathfrak a,x_{s+h},\ldots,x_n\}
   +\{\mathfrak b\}+P,
 \qquad 0\le h\le r,
\tag{1.13}
\]

with the displayed buffer suffix empty at \(h=r\).  The standard static
geometry is used here: all other disjoint adjacent swaps lie wholly on one
side of the active cut, so they do not change the sets \(P\) and \(T\).

Compare the route whose source pair is \(v,u\) and target pair is \(u,v\)
with the route whose source pair is \(u,v\) and target pair is \(v,u\).
Up to reversing the common overall sign, its complete aggregate incidence
difference is

\[
 \boxed{
 \Delta_{\rm route}
 =\sum_{h=0}^{n-1}\partial_h(G_h)
  +\sum_{h=0}^{r}\partial_h(H_h)
  -\sum_{\ell=0}^{s-2}\partial_{r+\ell}(K_\ell).}
\tag{1.14}
\]

The omitted top-rank terms cancel exactly because

\[
 K_{s-1}=G_n.
\tag{1.15}
\]

The two marked endpoints in (1.14) are

\[
 -\partial_r(K_0)+\partial_r(H_r)
 =-\partial_r(D+P)
  +\partial_r(D-\mathfrak a+\mathfrak b+P),
\tag{1.16}
\]

which is precisely the designated elementary rectangle.  Removing those
two endpoint occurrences leaves

\[
 \boxed{
 \Delta_{\rm conn}
 =\sum_{h=0}^{n-1}\partial_h(G_h)
  +\sum_{h=0}^{r-1}\partial_h(H_h)
  -\sum_{\ell=1}^{s-2}\partial_{r+\ell}(K_\ell).}
\tag{1.17}
\]

Thus the connector is the signed sum of three monotone strands:

* the recycle column \(G_h\), present for every \(0\le h<n\);
* the lower reload ribbon \(H_h\), present for \(0\le h<r\);
* the oppositely oriented upper source ribbon \(K_{h-r}\), present for
  \(r<h<n\).

It is not one vertical interval.  Under the routing theorem's distinct
buffers, the two edge supports at every rank where two strands coexist are
disjoint.  Every \(H_h\) omits \(\mathfrak a\), while \(G_h,K_\ell\)
contain it; at a common upper rank, \(z_{r+2}\) belongs to \(G_h\) but not
to \(K_{h-r}\).  Consequently

\[
 \boxed{
 \|\Delta_{\rm conn}\|_1
 =\|\Delta_{\rm conn}\|_2^2
 =4n-2=8Q-2.}
\tag{1.18}
\]

Rank by rank, there are two elementary edges for \(h<r\), one for \(h=r\),
two for \(r<h<n\), and none for \(h=n\).  Formula (1.18) is already
aggregated over time; it is not a count of unresolved time slices.

## 2. The four source traces of one paired bit

Toggle the common bit in (0.1), holding every other bit fixed. Before the
two paths coalesce at \(A_{j+2}\), its high-prefix dependence occurs in
exactly four source flushes:

\[
\begin{array}{c|c|c}
\text{source}&\text{active boundary}&\text{orientation sign}\\ \hline
A_j&r&+\\
C_j&r+2&-\\
A_{j+1}&r+2&+\\
C_{j+1}&r+4&-
\end{array}
\tag{2.1}
\]

The signs in the middle need not lead to cancellation, because the two
route templates and the other row orientations may differ. Denote the
four source differences by

\[
 D_h^0,D_h^1,D_h^2,D_h^3
\tag{2.2}
\]

in the order displayed in (2.1).

For

\[
 h\ge r+5,
\tag{2.3}
\]

all four traces are in the range (1.4). Thus

\[
 \|D_h^a\|_2^2=4
 \qquad(0\le a\le3).
\tag{2.4}
\]

No target-reload term occurs in this range. The largest target boundary is
\(r+4\), so (1.7) excludes it. The intermediate cyclic states can split
the active adjacent pair only at one of the moving boundaries

\[
 r+1,r+2,r+3,r+4,
\]

and therefore also contribute nothing to (2.3). Hence

\[
 \Delta_h=D_h^0+D_h^1+D_h^2+D_h^3
 \qquad(r+5\le h\le n-1).
\tag{2.5}
\]

## 3. The old far-collar separator

Use phase \(s=2j\) at \(A_j\), and let

\[
 w=z_{s,n}
\tag{3.1}
\]

be the last label of its ordered collar. This label is disjoint from the
active row pair because that pair lies in slots \(r,r+1\) with
\(r+1<Q<n\).

For the initial source \(A_j\), the ordinary flush base at
\(h=r+d\), \(d\ge1\), is

\[
 K_h=A+b+\{z_1,\ldots,z_{r-1}\}
       +\{z_{n-d+2},\ldots,z_n\}.
\tag{3.2}
\]

If \(h\ge r+5\), then the displayed suffix contains \(w=z_n\). The
special base contains the whole fixed suffix

\[
 \{z_{r+2},\ldots,z_n\},
\tag{3.3}
\]

and therefore also contains \(w\). It follows that

\[
 \boxed{\text{every mask in }\operatorname{supp}D_h^0
 \text{ contains }w.}
\tag{3.4}
\]

After the first two literal cyclic steps, \(w\) has dropped from the old
collar into the carrier tail. It is not in the new source core, not in the
new collar, and not the distinguished first tail input of any of the
three routes at phases \(s+2\) and \(s+4\). Every flush buffer is selected
from the source core. Consequently the complete extended cap available to
each of those three source traces omits \(w\). Thus

\[
 \boxed{\text{every mask in }
 \operatorname{supp}(D_h^1+D_h^2+D_h^3)
 \text{ omits }w.}
\tag{3.5}
\]

Equations (3.4)--(3.5) prove the orthogonality

\[
 D_h^0\perp D_h^1+D_h^2+D_h^3.
\tag{3.6}
\]

This is the requested exact \(w=z_n\) invariant. It is independent of all
choices and shifts of the buffer lists.

## 4. The future column-pair separator

Let

\[
 G=\{c_{j+2},d_{j+2}\}
\tag{4.1}
\]

be the two labels of the column exchange at port \(j+2\). In the route

\[
 C_{j+1}\longrightarrow A_{j+2},
\]

one member of \(G\) is in the source core and is the distinguished core
element eventually removed; the other member is the first tail input.
The distinguished core element cannot be one of the flush buffers.
Therefore both the ordinary and special bases of the source trace contain
both members of \(G\). Hence

\[
 \boxed{\text{every mask in }\operatorname{supp}D_h^3
 \text{ contains }G.}
\tag{4.2}
\]

At all earlier phases, the pair \(G\) lies wholly in the tail. It is not
in an earlier source collar or core, and the prescribed first tail inputs
there belong to the column pairs at ports \(j\) or \(j+1\), not \(j+2\).
Thus

\[
 \boxed{\text{every mask in }
 \operatorname{supp}(D_h^0+D_h^1+D_h^2)
 \text{ omits }G.}
\tag{4.3}
\]

In particular,

\[
 D_h^3\perp D_h^0+D_h^1+D_h^2.
\tag{4.4}
\]

Combining (3.6), (4.4), and (2.4) gives

\[
\begin{aligned}
 \|\Delta_h\|_2^2
 &=\|D_h^0\|_2^2+\|D_h^3\|_2^2
   +\|D_h^1+D_h^2\|_2^2\\
 &\ge4+4=8.
\end{aligned}
\tag{4.5}
\]

This proves (0.5).

There are exactly

\[
 (n-1)-(r+5)+1=n-r-5=Q+q-5
\tag{4.6}
\]

prefix ranks in the interval, proving the high-prefix contribution
\(8(Q+q-5)\). Since

\[
 q\ge2t+3,
\]

one may also record the uniform bound

\[
 \sum_h\|\Delta_h\|_2^2
 \ge8(Q+2t+3)-26
 =8Q+16t-2.
\tag{4.7}
\]

For completeness, the exact off-by-one at the beginning of the old-collar
trace gives a stronger total.  At \(h=r+1\), formula (3.2) has
\(d=1\), so its returned suffix is empty: \(K_{r+1}\) omits \(w\), while
\(J_{r+1}\) contains \(w\).  Every other occurrence affected by the paired
bit at this rank either precedes the split or belongs to a later cap and
omits \(w\).  The isolated \(T_{uv}(J_{r+1})\) half-trace therefore gives

\[
 \|\Delta_{r+1}\|_2^2\ge2.
\tag{4.8}
\]

For \(h=r+2,r+3,r+4\), both \(K_h\) and \(J_h\) of the initial source
contain \(w\), while every other affected occurrence omits it.  Hence

\[
 \|\Delta_h\|_2^2\ge4
 \qquad(r+2\le h\le r+4).
\tag{4.9}
\]

Adding (4.8), the three ranks in (4.9), and the \(Q+q-5\) ranks in
(0.5) gives

\[
 2+3\cdot4+8(Q+q-5)=8(Q+q)-26,
\tag{4.10}
\]

which is (0.6).  No assertion is made here about possible further positive
contributions at ranks \(h\le r\); (4.10) is the strongest lower bound
forced solely by the two cap tags.

## 5. A legal shifted-buffer coupling attains the lower bound

The middle traces in (2.1) really can be canceled. This verifies that the
constant eight in (0.5) is not an artifact of a poor coupling.

Let \(K\) be the source core of \(A_{j+1}\), and write the column pair at
that port as \(\{c,d\}\), with

\[
 C_j\text{ having source core }K-c+d.
\tag{5.1}
\]

Then the two phase-matched routes are

\[
 C_j\longrightarrow A_{j+1},
 \qquad
 A_{j+1}\longrightarrow B_{j+1}.
\tag{5.2}
\]

For the first route the distinguished exchange is \(d\) out and \(c\)
in; for the second it is \(c\) out and \(d\) in. Their extended source
caps agree exactly:

\[
 (K-c+d)+c=K+d.
\tag{5.3}
\]

Choose the same ordered list of \(n=2Q\) buffers from

\[
 K\setminus\{c\}.
\tag{5.4}
\]

This is legal for both routes: (5.4) is precisely the intersection of the
two allowable buffer reservoirs after their respective distinguished core
elements are excluded. The required size inequality is

\[
 |K|-1=m-Q-1\ge2Q,
\tag{5.5}
\]

or \(m\ge3Q+1\), which holds eventually in the calibrated regime
\(Q=o(m)\).

Let \(x^j,x^{j+1}\in\{0,1\}^p\) be the two column signatures. Choose

\[
 x^{j+1}=\mathbf1-x^j\oplus e_i,
\tag{5.6}
\]

where \(e_i\) is the \(i\)-th unit vector and \(\oplus\) is coordinatewise
addition modulo two. Thus

\[
 x_i^{j+1}=x_i^j,
 \qquad
 x_k^{j+1}=1-x_k^j\quad(k\ne i).
\tag{5.7}
\]

The collar of \(C_j\) has signature \(\mathbf1-x^j\), while that of
\(A_{j+1}\) has signature \(x^{j+1}\). Equations (5.6)--(5.7) show that
the collars agree in every row pair except \(i\), where they have opposite
orientation. Together with (5.3)--(5.4), the exact formulas for both
\(K_h\) and \(J_h\) agree in the two routes, while the active
transposition signs are opposite. Therefore

\[
 \boxed{D_h^1+D_h^2=0\quad\text{for every }h.}
\tag{5.8}
\]

In the high-prefix range (2.3), all other contributions vanish, so
(4.5) becomes equality. This proves (0.7).

The shifted schedule therefore solves the phase-matched middle coupling
perfectly. What it cannot change is either outer cap signature (3.4) or
(4.2).

## 6. The two marked rectangles and the exact bit count

The designated marked-state identity is

\[
 J(E)-J(0)=\sum_{a,b}E_{ab}\rho_{ab}.
\tag{6.1}
\]

The rectangles have pairwise disjoint supports and

\[
 \|\rho_{ab}\|_2^2=4.
\tag{6.2}
\]

Toggling the common bit (0.1) therefore gives (0.8). The two summands lie
at distinct lower depths

\[
 q_{ij}=q,
 \qquad
 q_{i,j+1}=q-2,
\tag{6.3}
\]

so neither can cancel the other.

If all ports are partitioned into disjoint adjacent pairs and one common
bit is assigned to each pair, the constrained marked cube has dimension

\[
 K_{\rm pair}=p\left\lfloor\frac t2\right\rfloor.
\tag{6.4}
\]

Using

\[
 pt=(1/16-o(1))M,
 \qquad t\longrightarrow\infty,
\]

gives

\[
 \boxed{K_{\rm pair}=(1/32-o(1))M.}
\tag{6.5}
\]

The interior pairs to which Theorem (0.5) applies number

\[
 p\left\lfloor\frac{t-1}{2}\right\rfloor
 =(1/32-o(1))M,
\tag{6.6}
\]

so discarding the possible terminal pair does not change the asymptotic
capacity or the obstruction.

For independent fair paired bits, the designated marked projection alone
has covariance trace

\[
 \frac14\sum_{i,s}
 \|\rho_{i,2s}+\rho_{i,2s+1}\|_2^2
 =2K_{\rm pair}
 =(1/16-o(1))M.
\tag{6.7}
\]

For one paired bit, condition on all other choices and let it be fair.
The two-valued variance identity and (0.6) give

\[
\begin{aligned}
 \sum_h\operatorname{tr}\operatorname{Cov}
   (I_h(e)\mid\text{all other data})
 &=\frac14\sum_h\|\Delta_h\|_2^2\\
 &\ge2(Q+q)-\frac{13}{2}.
\end{aligned}
\tag{6.8}
\]

Every term used in this lower bound is a connector source-flush term; no
marked endpoint is being charged. Thus the proposed local paired-bit
kernel has \(\Omega(Q)\), not \(O(1)\), total vertical connector variance.

Equation (6.8) is a conditional one-direction statement. One must not sum
it over all independent paired bits to claim an automatic
\(\Omega(K_{\rm pair}Q)\) covariance lower bound for an arbitrary
nonlinear simultaneous cube law: Boolean influences need not add as a
lower bound on total variance. The exact conclusion needed here is that
each proposed paired-bit physical direction already fails the desired
\(O(1)\) vertical ledger.

## 7. Simultaneous-row compatibility at the phase-matched seam

There is a second, independent incompatibility if one tries to use one
background schedule for many row directions at once.

At an internal phase define

\[
 D=\{k:x_k^{j+1}=x_k^j\},
 \qquad d=|D|.
\tag{7.1}
\]

For a row \(i\in D\), the \(C_j\) and \(A_{j+1}\) active orientations are
opposite, as required for cancellation. For every \(k\notin D\), their
other-row collar orientations agree. For every \(k\in D\setminus\{i\}\),
they differ by \(\alpha_k\).

As the ordinary or special prefix boundary passes that adjacent
\(k\)-pair, exactly one mask base is changed. The residual is the elementary
commutator rectangle

\[
 (I-\alpha_i)(I-\alpha_k)e_B,
\tag{7.2}
\]

whose four masks are distinct and whose squared norm is four. The ordered
row cuts imply that each \(k\ne i\) appears at exactly one prefix rank:
earlier row pairs occur in the ordinary moving suffix, and later row pairs
occur in the special moving prefix. Different \(k\)'s give distinct
supports. Therefore the exact phase-matched residual for direction \(i\)
has squared norm

\[
 4(d-1),
\tag{7.3}
\]

and the aggregate over the \(d\) separately usable row directions is

\[
 \boxed{4d(d-1).}
\tag{7.4}
\]

In particular, the exact cancellation (5.8) can hold for at most one row
direction in a single column transition. This is why (5.6) depends on the
designated row \(i\). A common shifted schedule cannot simultaneously
realize the best middle cancellation for the \(p\) row directions of the
full rectangle cube.

This simultaneous-row obstruction is not needed for (0.5): the outer-cap
lower bound already holds even for the one favored row whose middle traces
cancel perfectly.

## 8. Exact proved and conditional boundary

The following statements are proved.

1. Equal adjacent-port bits retain both marked rectangles and leave
   \((1/32-o(1))M\) independent marked directions under disjoint port
   pairing.
2. A legal shifted common-buffer schedule can cancel the two source traces
   on opposite sides of the shared phase exactly.
3. Regardless of every cross-route buffer shift, the initial and final
   source ribbons have orthogonal cap signatures. For every interior
   paired bit they force squared discrepancy at least eight at each of
   exactly \(Q+q-5\) high prefix ranks, and the old-collar half-trace
   sharpens the total certified discrepancy to \(8(Q+q)-26\).
4. The corresponding fair one-bit connector covariance is at least
   \(2(Q+q)-13/2\). Hence the proposed construction does not give
   \(O(1)\) total vertical variance.
5. One background column transition can give perfect phase-matched
   cancellation to at most one row direction; \(d\) simultaneous
   same-bit rows incur the exact separate-direction ledger \(4d(d-1)\).

### 8.1 What a common seed can and cannot change

The cap proof is pointwise in the common bit, so replacing independent
bits by one shared seed does not alter (0.5)--(0.6) for the proposed local
paired direction.  A scalar interval-discrepancy rule controls only how
many signed rank intervals are active.  The actual row vectors are
transposition edges \(T_{uv}(C)\), and different bases \(C\) are
orthogonal.  Cancellation therefore requires equality or a genuine cycle
among the labelled mask edges, not merely opposite interval signs.  The
old-collar and future-column tags prove that the needed labelled equality
is absent here.

There is also an exact retained-drift test which is independent of the
route formulas.  Let \(\rho_1,\ldots,\rho_k\) be support-disjoint marked
rectangles in one hard row, so

\[
 \langle\rho_a,\rho_b\rangle=0\ (a\ne b),
 \qquad \|\rho_a\|_2^2=4.
\]

For any common-seed physical row increment \(Z\), suppose its **complete**
conditional mean, connectors included, retains coefficients
\(\alpha_a\) in these modes:

\[
 \frac{\langle\mathbb E Z,\rho_a\rangle}{4}
 =-\alpha_a(E_a-\tfrac12).
\tag{8.1}
\]

Then Jensen and Bessel give

\[
 \boxed{\mathbb E\|Z\|_2^2\ge\sum_{a=1}^k\alpha_a^2.}
\tag{8.2}
\]

Indeed \(u_a=\rho_a/2\) are orthonormal and
\(|\langle\mathbb E Z,u_a\rangle|=\alpha_a\).  On each plateau row of the
rectangular cube one may take \(k=t\to\infty\).  Thus an \(O(1)\) row
second moment can retain only \(O(t^{-1/2})\) root-mean-square coefficient
across all \(t\) cell modes.  This does not exclude a load-adaptive kernel
which uses only a lower-dimensional direction at a time; it does exclude
the claim that interval correlation alone preserves order-one drift in
the whole marked row while making its physical variance \(O(1)\).

The following possibilities are not ruled out by this theorem.

1. The proof uses the coherent slot-equivariant compiler in which the
   buffer list of a fixed route is transported unchanged when its active
   collar pair is transposed. If the buffer template itself is allowed to
   change with the bit value, formula (1.4) no longer isolates a single
   transposition trace. Such a construction would be a new nonlinear
   compiler and would require a fresh literal-incidence audit.
2. A genuinely nonlocal multi-carrier signed identity could, in principle,
   supply another source ribbon with the same old- or future-cap signature
   and opposite sign. No such identity is furnished by adjacent cyclic
   advance or by shifting core buffers.
3. The theorem is a no-go for a local low-variance cube switch. It does not
   obstruct selecting whole connector braids positively in a global
   support-level near-factor argument.

Any successor to the paired-port idea must therefore transport the fallen
far-collar labels back into the later cap, or match the outer cap flux
nonlocally across carriers. A shift of the legal core-buffer schedule alone
cannot do either.

## 9. Independent audit

An independent proof audit checked the decisive support separation,
legality, constants, and scopes.

* It confirmed that the common buffer reservoir for the two phase-matched
  middle routes has exact size \(m-Q-1\), so the coupling in Section 5 is
  legal once \(m\ge3Q+1\).
* It confirmed both outer support tags: the initial high-rank trace contains
  the old last collar label \(w\), and the final trace contains both labels
  of \(\beta_{j+2}\), while all competing traces omit the corresponding
  tag.
* It confirmed the range \(r+5\le h\le2Q-1\), its exact cardinality
  \(Q+q-5\), the norm-squared lower bound eight, the fair-bit factor
  \(1/4\), and the interior capacity
  \(p\lfloor(t-1)/2\rfloor=(1/32-o(1))M\).
* The audit caught and corrected a potential off-by-one: at \(h=r+1\) the
  ordinary \(K\)-base does **not** yet contain \(w\); only the special
  \(J\)-base does. From \(h=r+2\) onward both contain it. This is exactly
  the distinction used in (4.8)--(4.10), and it does not affect the main
  high-rank theorem.
* It also confirmed the essential scope of the equality construction:
  when the entire adjacent columns satisfy \(x^{j+1}=x^j\) and \(p>1\),
  the middle traces do not cancel. They leave the exact separate-direction
  residue \(4(p-1)\) for each row. Equality in (0.7) is attainable only
  after favoring one designated row through (5.6), not simultaneously for
  the full \(p\)-row paired cube.

The audit therefore passes the universal lower bound and strengthens its
interpretation: the only equality coupling is lower-dimensional, whereas
the coefficient-scale all-row paired family has additional middle-seam
residue.
