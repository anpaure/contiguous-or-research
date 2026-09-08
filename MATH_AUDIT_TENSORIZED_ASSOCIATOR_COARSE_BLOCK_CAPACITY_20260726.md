# Coarse 8-block capacity audit for the tensorized pair-frame associator

Date: 2026-07-26

Method: pure mathematics only.

## 0. Outcome

Tensorize the 8-coordinate pair-frame associator over \(r\) disjoint
blocks. In every selected block the middle source belongs to the local
24-set frame

\[
 \mathcal V=
 \{X\cup Y:X\in\tbinom{\{a,b,c,d\}}2,
                 Y\in\{uw,ux,vw,vx\}\}.
\tag{0.1}
\]

There is an evident coarse invariant: if a rank-\((m-q)\) target is a
lower \(q\)-shadow of one of the packet cycles, then at least \(r-q\) of
the selected blocks are still literally in \(\mathcal V\). This invariant
does **not** create a positive-density target-capacity deficit when

\[
 q=\Theta(\sqrt m),\qquad q=o(r),\qquad r=o(m).
\tag{0.2}
\]

Indeed, a uniform rank-\((m-q)\) target has

\[
 \left(\frac3{128}+o(1)\right)m
\tag{0.3}
\]

\(\mathcal V\)-blocks on average, and

\[
 \frac{\#\{S\in\binom{[2m+1]}{m-q}:
              S\text{ has fewer than }r-q\ \mathcal V\text{-blocks}\}}
      {\binom{2m+1}{m-q}}
       \le e^{-\Omega(m)}.
\tag{0.4}
\]

The canonical convention which assigns a middle source to its first \(r\)
eligible blocks is also harmless at the coarse level. Except for an

\[
                         e^{-\Omega(r)}+e^{-\Omega(m)}
\tag{0.5}
\]

fraction of rank-\((m-q)\) targets, one can choose \(q\) early one-deletion
blocks and complete them to \(\mathcal V\), after which all \(q\) altered
blocks occur among the first \(r\) eligible blocks of the completed middle
source.

Thus no \(\Omega(W)\) obstruction is visible in the coarse 8-block weight
profile. The remaining gate is genuinely finer: the prescribed \(q\)
cube directions must occur as a legal length-\(q\) window in the chosen
Hamming cycle, and the resulting fine lower targets must have controlled
collisions across packets.

## 1. The exact block invariant

Put \(n=2m+1\). Partition \(8B\) of the \(2m\) paired coordinates into

\[
                         B=\lfloor m/4\rfloor
\tag{1.1}
\]

labelled 8-blocks. At most seven coordinates remain outside these blocks.
In each block use the labels \(a,b,c,d,u,v,w,x\) and the local frame
\(\mathcal V\) from (0.1).

Suppose a tensor packet has selected block set \(I\), \(|I|=r\). Each
selected block contributes a local \(Q_2\), so the product cell is a
\(Q_{2r}\). In an isometric \(C_{4r}\), every cyclic segment of \(q<2r\)
steps uses \(q\) distinct cube directions. Let \(d_i\) be the number of
these directions which lie in block \(i\in I\). Then

\[
 d_i\in\{0,1,2\},\qquad \sum_{i\in I}d_i=q.
\tag{1.2}
\]

If \(S\) is the corresponding lower target, its block weights satisfy

\[
 |S\cap B_i|=4-d_i.
\tag{1.3}
\]

More is true when \(d_i=0\): the block was not changed at all, so

\[
                         S\cap B_i\in\mathcal V.
\tag{1.4}
\]

Writing

\[
 Z(S)=\#\{i\le B:S\cap B_i\in\mathcal V\},
\tag{1.5}
\]

we obtain the exact necessary condition

\[
 \boxed{Z(S)\ge \#\{i\in I:d_i=0\}\ge r-q.}
\tag{1.6}
\]

If \(a_j=\#\{i:d_i=j\}\), then the full coarse ledger is

\[
 a_0+a_1+a_2=r,
 \qquad a_1+2a_2=q,
 \qquad (|S\cap B_i|)_{i\in I}
       =(4^{a_0},3^{a_1},2^{a_2}).
\tag{1.7}
\]

In particular the number of touched selected blocks lies between
\(\lceil q/2\rceil\) and \(q\). Condition (1.6), rather than an invariant
requiring all \(r\) blocks to retain weight four, is the correct coarse
restriction.

## 2. Exact conditioned-binomial calculation

Let \(S\) be uniform in \(\binom{[n]}k\), where \(k=m-q\), and put

\[
                         p=\frac{k}{n}.
\tag{2.1}
\]

Generate \(S\) instead by independent Bernoulli-\(p\) coordinates and then
condition on \(|S|=k\). Before conditioning, the block indicators in
(1.5) are independent, and

\[
 \begin{aligned}
 \pi_q
  &:=\Pr(S\cap B_i\in\mathcal V)\\
  &=24p^4(1-p)^4\\
  &=\frac3{32}
    \left(1-\frac{(2q+1)^2}{(2m+1)^2}\right)^4.
 \end{aligned}
\tag{2.2}
\]

Consequently, before conditioning,

\[
                         Z\sim\operatorname{Bin}(B,\pi_q).
\tag{2.3}
\]

For \(q=o(m)\),

\[
 \pi_q=\frac3{32}+o(1),
 \qquad
 \mathbb EZ=\left(\frac3{128}+o(1)\right)m.
\tag{2.4}
\]

Since \(p\) stays in a compact subinterval of \((0,1)\), Stirling's
formula gives an absolute constant \(c_0>0\) such that

\[
 \Pr\{\operatorname{Bin}(n,p)=k\}\ge \frac{c_0}{\sqrt n}.
\tag{2.5}
\]

For every event \(\mathcal A\), therefore,

\[
 \Pr(\mathcal A\mid |S|=k)
 \le c_0^{-1}\sqrt n\,\Pr(\mathcal A).
\tag{2.6}
\]

Assume \(r=o(m)\). Uniformly for \(q=o(m)\), eventually
\(r-q\le(\mathbb EZ)/2\). The multiplicative Chernoff bound and (2.6)
give

\[
 \begin{aligned}
 \Pr\{Z<r-q\mid |S|=k\}
 &\le c_0^{-1}\sqrt n
       \Pr\{Z<(\mathbb EZ)/2\}\\
 &\le c_0^{-1}\sqrt n\exp(-\mathbb EZ/8)\\
 &=e^{-\Omega(m)}.
 \end{aligned}
\tag{2.7}
\]

This proves (0.4). At \(q=c\sqrt m+O(1)\), the layer size
\(\binom n{m-q}\) is a constant-order multiple of
\(W=\binom nm\). Hence the absolute number of targets rejected by the
coarse invariant is \(e^{-\Omega(m)}W\), in particular \(o(W)\).

## 3. Even the exact local weight requests are abundant

The conclusion is not an artefact of discarding the \(d_i=1,2\) data in
(1.7). There are explicit allowable local targets of both weights.

For example, in the resolution-\(0\) square

\[
             (acuw,\ bcuw,\ bduw,\ aduw)
\tag{3.1}
\]

the one-direction lower face contains

\[
                         A_1=\{c,u,w\},
\tag{3.2}
\]

and a two-direction lower face contains

\[
                         A_2=\{u,w\}.
\tag{3.3}
\]

Under the Bernoulli-\(p\) model the probabilities of these two exact
labelled local patterns are

\[
 \pi_1=p^3(1-p)^5=\frac1{256}+o(1),
 \qquad
 \pi_2=p^2(1-p)^6=\frac1{256}+o(1).
\tag{3.4}
\]

Thus a uniform rank-\((m-q)\) target has \(\Theta(m)\) blocks of each
explicit allowable kind, except on an \(e^{-\Omega(m)}\) fraction of the
layer. In particular, for every prescribed

\[
 a_0+a_1+a_2=r,\qquad a_1+2a_2=q,\qquad
 a_0,a_1,a_2=o(m),
\tag{3.5}
\]

the inventory demanded by the coarse ledger (1.7) is present outside an
\(e^{-\Omega(m)}\) exceptional set. This is only a capacity statement;
it does not assert that an arbitrary choice of those blocks is a consecutive
window of one chosen Hamming cycle.

## 4. The canonical first-\(r\)-eligible convention

We now incorporate the proposed global packet partition: for every middle
source, use its first \(r\) blocks whose restrictions lie in \(\mathcal V\).
The prefix convention still does not cause a positive-density obstruction.

Assume

\[
                         q=o(r),\qquad r=o(m),
\tag{4.1}
\]

and let \(L=\lfloor r/4\rfloor\). In the first \(L\) blocks count exact
copies of \(A_1=\{c,u,w\}\). Before conditioning this is

\[
                         Z_1\sim\operatorname{Bin}(L,\pi_1).
\tag{4.2}
\]

Because \(\mathbb EZ_1=(1/1024+o(1))r\) and \(q=o(r)\), eventually
\(q\le(\mathbb EZ_1)/2\). Equations (2.5)--(2.6) and Chernoff give

\[
 \Pr\{Z_1<q\mid |S|=m-q\}
             \le e^{-\Omega(r)}
\tag{4.3}
\]

at the requested scale \(q=\Theta(\sqrt m)\), where the harmless
\(\sqrt m\) conditioning factor is absorbed by \(r\gg q\).

Take a target outside the exceptional events in (2.7) and (4.3). Choose
\(q\) prefix blocks of type \(A_1\), and in each add the coordinate \(a\).
This changes \(A_1\) to \(acuw\in\mathcal V\), uses exactly \(q\) new
coordinates, and therefore produces a middle set. Leave \(r-q\)
already-\(\mathcal V\) blocks untouched. The completed middle source has
at least \(r\) eligible blocks.

Every newly completed block lies among the first \(L<r\) physical blocks.
Even if every block in that prefix is eligible, fewer than \(r\) eligible
blocks precede its end. Consequently all \(q\) newly completed blocks are
among the source's first \(r\) eligible blocks. The canonical packet thus
contains all \(q\) altered blocks, and its remaining selected blocks are
filled by unchanged \(\mathcal V\)-blocks.

We have proved the quantitative coarse-completion bound

\[
 \frac{\#\{\text{rank-}(m-q)\text{ targets failing canonical coarse
 completion}\}}
      {\binom n{m-q}}
 \le e^{-\Omega(r)}+e^{-\Omega(m)}.
\tag{4.4}
\]

Again, (4.4) is deliberately called *coarse completion*. It supplies a
product cube containing a middle extension and the required \(q\) local
directions. It does not prove that a preselected \(C_{4r}\)-factor places
those directions consecutively, nor that different packets give distinct
lower targets.

## 5. The apparent three-deletion obstruction

One may object that a selected local \(Q_2\) supplies only two directions,
so no lower window can delete three coordinates from one active 8-block.
There are two separate answers.

### 5.1 Almost no target is forced to use three deletions in one block

Fix \(Q=o(r)\) with \(Q=O(\sqrt m\,\omega(m))\) and \(r/Q\to\infty\).
Call a rank-\((m-q)\) target *macro-forced-3* if it has no coarse
completion of the canonical kind in Section 4 using at most two additions
in every selected block.

The construction in Section 4 uses exactly one addition in each of \(q\)
distinct prefix blocks. Its proof is uniform for \(1\le q\le Q\): because
\(\mathbb EZ_1=\Theta(r)\) and \(Q=o(r)\), eventually
\(Q\le(\mathbb EZ_1)/2\). Hence there are constants \(c,c'>0\) such that

\[
 \#\{\text{macro-forced-3 targets at depth }q\}
 \le
 \left(e^{-cr}+e^{-c'm}\right)\binom n{m-q}
\tag{5.1}
\]

uniformly for \(q\le Q\). Since \(\binom n{m-q}\le W\),

\[
 \boxed{
 \sum_{q=1}^{Q}
 \#\{\text{macro-forced-3 targets at depth }q\}
 \le
 Q\left(e^{-cr}+e^{-c'm}\right)W=o(W).}
\tag{5.2}
\]

Without the first-\(r\) convention, the \(e^{-cr}\) term is absent: the
global inventory calculation in Section 3 gives \(Qe^{-\Omega(m)}W\).
Thus the restriction \(d_i\le2\) creates no aggregate capacity loss on the
Gaussian scale.

### 5.2 The local frame itself contains \(Q_3\)'s and a \(Q_4\)

More strongly, dimension two is not an invariant of \(\mathcal V\). An
isometric constant-weight cube is obtained from a fixed core by choosing
one endpoint from each of several disjoint coordinate pairs.

The following three \(Q_3\)'s partition \(\mathcal V\):

\[
\begin{array}{c|c|c|c}
\text{cell}&\text{fixed special point}&
 \text{active special pair}&\text{other active pairs}\\ \hline
A_1&a&bc&uv,\ wx\\
A_2&d&ab&uv,\ wx\\
A_3&c&bd&uv,\ wx .
\end{array}
\tag{5.3}
\]

Their special two-set supports are respectively

\[
 \{ab,ac\},\qquad \{ad,bd\},\qquad \{bc,cd\},
\tag{5.4}
\]

which partition \(\binom{\{a,b,c,d\}}2\); every cell uses all four
reservoir orientations. Thus each cell has \(2^3=8\) vertices and the
three cells partition all 24 vertices.

There is a second \(Q_3\)-partition:

\[
\begin{array}{c|c|c|c}
\text{cell}&\text{fixed special point}&
 \text{active special pair}&\text{other active pairs}\\ \hline
B_1&a&bd&uv,\ wx\\
B_2&c&ab&uv,\ wx\\
B_3&d&bc&uv,\ wx ,
\end{array}
\tag{5.5}
\]

with special supports

\[
 \{ab,ad\},\qquad \{ac,bc\},\qquad \{bd,cd\}.
\tag{5.6}
\]

The ownership overlap of (5.3) and (5.5) is connected. After suppressing
the four parallel reservoir phases, its edges are

\[
 A_1B_1\ (ab),\ A_1B_2\ (ac),\
 A_2B_1\ (ad),\ A_2B_3\ (bd),\
 A_3B_2\ (bc),\ A_3B_3\ (cd),
\tag{5.7}
\]

which form a 6-cycle. Consequently \(\mathcal V\) has an exact connected
three-\(Q_3\)-versus-three-\(Q_3\) cubical associator.

The original two resolutions contain dimension four as well. The four
parallel local squares \(Q_0\cup Y\), \(Y\in\mathcal Y\), are the slices
of the single \(Q_4=Q_0\square Q_R\). Therefore

\[
 \mathcal V
 =
 (Q_0\square Q_R)\ \dot\cup\
 (ab\cup Q_R)\ \dot\cup\ (cd\cup Q_R),
\tag{5.8}
\]

and analogously

\[
 \mathcal V
 =
 (Q_1\square Q_R)\ \dot\cup\
 (ac\cup Q_R)\ \dot\cup\ (bd\cup Q_R).
\tag{5.9}
\]

These are one-\(Q_4\)-plus-two-\(Q_2\) partitions.

Finally, four is the maximum local cube dimension. Along any cube edge,
one coordinate is exchanged for another. In order that both endpoints
remain in \(\mathcal V\), the exchanged coordinates must lie in the same
one of the three macro-classes

\[
 \{a,b,c,d\},\qquad\{u,v\},\qquad\{w,x\}.
\tag{5.10}
\]

The first class supplies at most two disjoint direction pairs and each of
the latter classes at most one. Hence \(d\le2+1+1=4\).

The \(Q_3\)-partition does not plug mechanically into the current uniform
Hamming \(C_{2h}\)-factor step: tensoring it \(r\) times gives dimension
\(3r\), which can never be a power of two, while the divisibility
\(2h\mid2^h\) forces \(h\) to be a power of two. Likewise (5.8)--(5.9)
have nonuniform cell dimensions. They nevertheless prove rigorously that
the two-direction restriction is architectural, not a local state-space
no-go.

There is also a direct divisibility repair if one is willing to enlarge
the macroblock by one spectator pair. Add coordinates \(y,z\) and require
exactly one of them. Then

\[
                    \widetilde{\mathcal V}
                    =\mathcal V\square Q_1
\tag{5.11}
\]

has 48 weight-5 states on ten coordinates. Tensoring every \(Q_3\) in
(5.3) or (5.5) with the \(yz\)-direction gives two partitions of
\(\widetilde{\mathcal V}\) into three \(Q_4\)'s. Their overlap remains
connected. Therefore \(r\) such 10-blocks give, in either resolution,

\[
              \widetilde{\mathcal V}^{\,r}
              =\dot\bigcup_{3^r\text{ cells}}Q_{4r}.
\tag{5.12}
\]

If \(r\) is a power of two, then \(h=4r\) is a power of two and the known
Hamming \(C_{2h}=C_{8r}\)-factor applies to every cell. Thus local
dimension at least three can be made fully compatible with the same
power-of-two cycle-factor mechanism. What is not audited here is whether
these new two resolutions have the desired signed fixed-pair shadow drift;
(5.11)--(5.12) settle only exact support, connectedness, dimension, and
divisibility.

## 6. Final audit verdict

The fixed 8-block decomposition leaves a visible invariant, but its
capacity scale is linear in \(m\): a typical target carries about
\(3m/128\) untouched frame blocks. The tensor construction asks for only
\(r-q=o(m)\) of them and only \(q=\Theta(\sqrt m)\) altered blocks. Both
inventories lie far below their typical linear supplies.

Therefore

\[
 \boxed{
 \text{the coarse 8-block weight invariant creates no }
 \Omega(W)\text{ deficit at }q=\Theta(\sqrt m).}
\tag{6.1}
\]

Any future no-go for the tensorized associator must use information finer
than block weights and local frame eligibility: direction-order rigidity,
cycle-factor incidence, ownership compatibility, or target collisions.
