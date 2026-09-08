# Fifth-wave B: non-product packet fusion

## Exact type transport, literal sibling fusion, and a recursive-closure no-go

### 25 July 2026

## 0. Verdict

This route does **not** prove the contiguous-OR width conjecture. It does,
however, separate the surviving packet problem into a solved scalar part and
an unsolved labelled part.

1. There is no cone-mass, parent-count, or width-capacity obstruction to
   pairing the obstructed three-chain parents with nonobstructed parents.
   An explicit orthogonal reflection of the Rayleigh height cone has
   push-forward dominated by the available density on the strict triangle
   region, and it strictly increases continuous middle width. Consequently,
   all but \(o(W(3s))\) of the certified integer bad-parent endpoint demand
   can be assigned integrally to distinct, wider good parents.

2. That scalar pairing is not a literal packet construction. Every
   \(W(3s)+o(W(3s))\) word must realize a positive linear amount of
   cross-parent endpoint sharing. Such sharing can be saturated at adjacent
   ranks only by Boolean covers lying in one-factor fibres. In a near-sum-
   width two-parent fusion, a packet containing a dominant parent needs a
   matching of order its plateau deficit in the corresponding cross-parent
   comparability graph; the exact excess-dependent bound is (5.3).

3. There is a genuine exact fusion atom. Two recursive sibling parents can
   be covered at their two complete middle layers, together with the complete
   first upper layer of the shorter sibling, by a word of exactly the sum of
   their widths. The witnesses are explicit adjacent pairs. This proves
   that endpoint sharing is real and that a blanket “different parents must
   pay separately” principle is false.

4. The atom cannot be promoted by taking bounded, polynomial, or more
   generally \(\exp(o(\sqrt s))\)-sized **full recursive descendant closures**.
   A positive global-width fraction of such packets retains at least ten per
   cent excess even when all descendants in a packet are fused by one
   unrestricted word. Moreover a full recursive packet containing a deep
   obstructed descendant and any nonobstructed descendant has at least
   \(2^{0.4\sqrt s}/(3s+1)^3\) children.

Thus small full recursive closures are ruled out. Arbitrary non-full packets
(including bounded but remote packets), as well as full recursive closures
of mesoscopic exponential size, remain open. Any adjacent-rank endpoint
sharing they use must lie in labelled one-factor fibres; rank-skipping
sharing is the alternative quantified by Theorem 4.1. Either mechanism must
ultimately be sequenced in legal MTF state paths with only \(o(W(3s))\)
initialization and seam cost. The exact missing statement is isolated in
Section 9.

All lower bounds below permit foreign letters in the word and witnesses that
cross nominal packet boundaries unless a packet-confinement hypothesis is
explicitly stated.

## 1. Set-up and the exact cone resources

Write \(\mathcal B_s=2^{[s]}\), and fix an arbitrary symmetric-chain
decomposition (SCD) in each of three disjoint \(s\)-coordinate blocks. A
chain of edge-height \(h\) is identified with \([0,h]\). Three factor chains
of heights \(p,q,r\) determine the product box

\[
   B(p,q,r)=[0,p]\times[0,q]\times[0,r].
\]

All product boxes are centred at the same global rank. Hence their middle
layers partition a middle layer of \(\mathcal B_{3s}\), and

\[
   \sum_B w(B)=W(3s),
   \qquad W(t):=\binom{t}{\lfloor t/2\rfloor},                 \tag{1.1}
\]

where \(w(B)\) is the width of the box. We take \(s\) even when an exact
central rank is convenient; the asymptotic statements are unchanged along
odd \(s\), with the usual floor convention.

After sorting the heights, write \(p\le q\le r\). Call the box
**dominant** or **bad** when

\[
                 r>p+q.                                      \tag{1.2}
\]

Projection to the first two coordinates is injective on every antichain,
while every rank from \(p+q\) through \(r\) contains one point above each
\((i,j)\in[0,p]\times[0,q]\). Therefore

\[
   w(B)=(p+1)(q+1)\qquad(r\ge p+q).                           \tag{1.3}
\]

For a bad box put

\[
 d(B):=\left\lceil
        (p+1)(q+1)\frac{r-p-q}{r}
       \right\rceil,                                         \tag{1.4}
\]

and let

\[
 D_s:=\sum_{B\ {\rm bad}}d(B),\qquad
 W_s^{\rm bad}:=\sum_{B\ {\rm bad}}w(B),\qquad
 W_s^{\rm good}:=W(3s)-W_s^{\rm bad}.                        \tag{1.5}
\]

The quantity \(d(B)\) is an exact integer lower demand on the two endpoint
partitions, furnished by the flat-plateau lemma proved in Section 3; no
attainability assertion is intended.

### Lemma 1.1 (SCD height law)

If \(H_s\) is the height of a uniformly selected chain of an arbitrary SCD
of \(\mathcal B_s\), then its law is independent of the SCD and

\[
 \Pr(H_s\ge \epsilon_s+2j)
 =\frac{\binom{s}{\lfloor s/2\rfloor-j}}
        {\binom{s}{\lfloor s/2\rfloor}},                     \tag{1.6}
\]

where \(\epsilon_s\in\{0,1\}\) has the parity of \(s\). Moreover

\[
     \frac{H_s}{\sqrt s}\Longrightarrow Y,
     \qquad \Pr(Y\ge y)=e^{-y^2/2},                           \tag{1.7}
\]

and all fixed polynomial moments converge.

#### Proof

Exactly

\[
 \binom{s}{a}-\binom{s}{a-1}
\]

chains start at rank \(a\le s/2\): the first term counts the rank-\(a\)
points and the second counts chains already present at rank \(a-1\). Such a
chain has height \(s-2a\). Summing these differences gives (1.6).

For \(j=O(\sqrt s)\), the quotient in (1.6) is a product of factors
\((m-i+O(1))/(m+i+O(1))\), and logarithmic expansion gives

\[
 \log\frac{\binom{s}{\lfloor s/2\rfloor-j}}
              {\binom{s}{\lfloor s/2\rfloor}}
       =-\frac{2j^2}{s}+o(1).                                \tag{1.8}
\]

This proves (1.7). The same product and \(\log(1-u)\le-u\) give
\(\Pr(H_s\ge t\sqrt s)\le C e^{-ct^2}\), uniformly in \(s,t\); hence every
fixed polynomial is uniformly integrable. \(\square\)

Stirling's formula also gives

\[
 \frac{sW(s)^3}{W(3s)}\longrightarrow\frac{2\sqrt3}{\pi}.    \tag{1.9}
\]

Let \(A<B<C\) be the order statistics of three independent standard
Rayleigh variables, each of density \(x e^{-x^2/2}\).

### Theorem 1.2 (exact bad width and endpoint-demand masses)

As \(s\to\infty\),

\[
 \frac{W_s^{\rm bad}}{W(3s)}\longrightarrow
 \Omega:=\frac43-\frac{2\sqrt3}{\pi}<\frac12,                \tag{1.10}
\]

and

\[
 \frac{D_s}{W(3s)}\longrightarrow
 \Gamma:=\frac{2\sqrt3}{\pi}
 \mathbb E\!\left[
 AB\frac{C-A-B}{C}\mathbf1_{\{C>A+B\}}
 \right].                                                    \tag{1.11}
\]

In particular \(0<\Gamma<\Omega\), and

\[
 W_s^{\rm good}-D_s
 \ge
 \left(\frac{4\sqrt3}{\pi}-\frac53-o(1)\right)W(3s)>0.       \tag{1.12}
\]

#### Proof

The three chain choices are independent, Lemma 1.1 supplies their Rayleigh
limit, and (1.3), (1.9), and uniform integrability give

\[
 \frac{W_s^{\rm bad}}{W(3s)}
 \longrightarrow
 \frac{2\sqrt3}{\pi}
 \mathbb E[AB\mathbf1_{\{C>A+B\}}].                          \tag{1.13}
\]

For one choice of the largest Rayleigh variable, integration in that
variable and then the substitution \(y=tx\) give

\[
\begin{aligned}
 \mathbb E[AB\mathbf1_{\{C>A+B\}}]
 &=3\int_0^\infty\!\int_0^\infty
       x^2y^2e^{-(x^2+y^2+xy)}\,dx\,dy  \\
 &=3\int_0^\infty\frac{t^2}{(t^2+t+1)^3}\,dt
   =\frac{2\pi}{3\sqrt3}-1.                                \tag{1.14}
\end{aligned}
\]

Completing the square in the last elementary rational integral gives its
displayed value. Equations (1.13)--(1.14) prove (1.10).

The number of parent boxes is \(W(s)^3=O(W(3s)/s)\), so the total effect of
the ceilings in (1.4) is \(o(W(3s))\). Away from the null cone wall,

\[
 \frac{(p+1)(q+1)}s\frac{r-p-q}{r}
 \longrightarrow AB\frac{C-A-B}{C}.
\]

The Gaussian height tail from Lemma 1.1 again gives uniform integrability,
which proves (1.11). Its integrand is strictly between \(0\) and \(AB\) on
a positive-measure event, hence \(0<\Gamma<\Omega\).

Finally \(d(B)\le w(B)\) for every bad box. Thus

\[
 W_s^{\rm good}-D_s
 \ge W(3s)-2W_s^{\rm bad},                                   \tag{1.15}
\]

and (1.10) yields (1.12), since
\(1-2\Omega=4\sqrt3/\pi-5/3>0\). \(\square\)

The strict surplus (1.12) already rules out a mere scalar shortage. The
next theorem gives a geometric, typewise version.

## 2. An exact reflection transport from bad to good types

Work first in labelled continuous height space \(\mathbb R_{>0}^3\), with
Rayleigh product measure

\[
 d\mu(x,y,z)=xyz\,e^{-(x^2+y^2+z^2)/2}\,dx\,dy\,dz.           \tag{2.1}
\]

On the oriented bad cone \(c>a+b\), write \(c=a+b+3t\), \(t>0\), and set

\[
 R(a,b,c)=(a+2t,\ b+2t,\ a+b+t).                             \tag{2.2}
\]

This is orthogonal reflection across the plane \(c=a+b\). Use its two
coordinate permutations on the other oriented bad cones.

For a strict triangle \(x,y,z\), the continuous central-section width is

\[
 \omega(x,y,z)
 =\frac{2(xy+xz+yz)-(x^2+y^2+z^2)}4.                         \tag{2.3}
\]

For a dominant triple \((a,b,c)\) it is \(ab\).

### Theorem 2.1 (reflection domination and width gain)

The union of the three maps (2.2) sends the three bad cones into the strict
triangle region. For \(c=a+b+3t\),

\[
 \omega(R(a,b,c))
 =ab+2(a+b)t+\frac74t^2>ab.                                  \tag{2.4}
\]

Moreover, if \(\nu\) is the sum of the three push-forwards of \(\mu\)
restricted to the oriented bad cones, then

\[
                         \nu\le\mu                           \tag{2.5}
\]

as measures on the strict triangle region.

#### Proof

Reflection preserves Euclidean norm and has Jacobian one. Formula (2.2)
has three positive triangle slacks, and substitution in (2.3) gives (2.4).
It remains to compare the polynomial factors in (2.1), including all
possible preimages of one target.

For a target \(y=(y_1,y_2,y_3)\) in the strict triangle region, introduce
semiperimeter coordinates

\[
 u=\frac{y_2+y_3-y_1}{2},\quad
 v=\frac{y_1+y_3-y_2}{2},\quad
 w=\frac{y_1+y_2-y_3}{2}.                                    \tag{2.6}
\]

Thus \(u,v,w>0\),

\[
 y=(v+w,u+w,u+v),\qquad
 P:=y_1y_2y_3=(u+v)(u+w)(v+w).                               \tag{2.7}
\]

The preimage reflected through the face \(u=0\), when positive, has product

\[
 P_u=(v+w+4u/3)(v-u/3)(w-u/3),                               \tag{2.8}
\]

and it is eligible precisely when \(v,w>u/3\). Define \(P_v,P_w\) by
cyclic permutation. Since the exponential factor is unchanged, (2.5) is
equivalent to

\[
                    \sum_{i\ {\rm eligible}}P_i\le P.         \tag{2.9}
\]

Order \(u\le v\le w\). There are three cases.

* If \(v\ge3u\), only \(P_u\) is eligible. In the source variables, direct
  expansion gives

  \[
  P-P_u
  =2t((a+b)^2-ab)+6t^2(a+b)+4t^3>0.                          \tag{2.10}
  \]

* If \(v<3u\le w\), precisely \(P_u,P_v\) are eligible and expansion gives

  \[
  \begin{aligned}
  27(P-P_u-P_v)
  ={}&9w^2(u+v)+9w(u+v)^2+45uv(u+v)\\
     &-4(u^3+v^3)>0.                                         \tag{2.11}
  \end{aligned}
  \]

  Indeed, with \(r=v/u\in[1,3)\), the last two terms divided by \(u^3\)
  are \(45r(1+r)-4(1+r^3)>0\); its derivative is positive on
  \([1,3]\).

* If \(w<3u\), all three preimages are eligible and

  \[
  27(P-P_u-P_v-P_w)
   =-4\sum u^3+18\sum_{\rm sym}u^2v>0.                        \tag{2.12}
  \]

  If \(M=\max(u,v,w)\), each of the other two variables exceeds \(M/3\).
  The terms \(18M^2\) times their sum alone exceed \(12M^3\), whereas
  \(4\sum u^3\le12M^3\).

These cases prove (2.9), hence (2.5). \(\square\)

### Corollary 2.2 (integral parent-type pairing)

There are sets \(\mathscr D_s'\) of bad discrete parent boxes and injections

\[
      \Phi_s:\mathscr D_s'\longrightarrow
      \{\hbox{nonobstructed parent boxes}\}                   \tag{2.13}
\]

such that

\[
 \sum_{B\notin\mathscr D_s'}d(B)=o(W(3s)),\qquad
 w(\Phi_s(B))\ge w(B)\ge d(B).                               \tag{2.14}
\]

Consequently, all but \(o(W(3s))\) exact endpoint-demand units can be
assigned to distinct middle-width tokens in distinct good parents.

#### Proof

First remove a shrinking neighbourhood of the coordinate planes, the cone
wall, and infinity. The discarded \(AB\)-weighted Rayleigh mass tends to
zero by absolute continuity and the Gaussian tail; by Theorem 1.2 this
discards \(o(W(3s))\) discrete demand under a diagonal choice of the
neighbourhoods.

On each remaining compact set, (2.4) has a uniform positive width margin,
and (2.9) has a uniform density margin. Partition the **target** compact set
into finitely many sufficiently small cells \(C\), and partition each source
branch by the pieces \(R_i^{-1}(C)\). The measure domination (2.5), including
the sum over overlapping branches, says that every target cell has more
available good mass than the total mass of all its source pieces. The
empirical SCD-height measures converge on this finite family of cells and
pieces by Lemma 1.1. Thus, for all large \(s\), the number of good parent
boxes in each \(C\) exceeds the total number of bad boxes in all
\(R_i^{-1}(C)\). Pair them within \(C\). The elementary lattice slice
estimate

\[
 \frac1s w([0,\lfloor x\sqrt s\rfloor]
              \times[0,\lfloor y\sqrt s\rfloor]
              \times[0,\lfloor z\sqrt s\rfloor])
   =\omega(x,y,z)+O(s^{-1/2})                                \tag{2.15}
\]

is uniform on such a compact set: it follows by counting integer pairs in
the central planar slice, or directly from the three truncated triangular
sums. Therefore the uniform margin in (2.4) implies
\(w(\Phi_s(B))\ge w(B)\) for large \(s\).

A progressively finer finite partition, chosen slowly enough that the
finite-cell asymptotics have already stabilized, gives (2.13)--(2.14).
The ceiling contribution is \(O(W(s)^3)=o(W(3s))\). \(\square\)

Corollary 2.2 is deliberately only a type/count/width theorem. It says
nothing about comparability of the actual masks, compatible endpoint order,
or a common MTF trajectory.

## 3. The exact endpoint-sharing ledger

A word is a sequence \(x_1,\ldots,x_n\in\mathcal B_{3s}\). It covers a
target \(T\) if \(T=x_i\cup\cdots\cup x_j\) for some interval \([i,j]\).
Fix one witnessing interval for every selected target.

### Lemma 3.1 (flat-plateau endpoint lemma)

Let \(Q\) be a finite graded poset of cardinality \(B\) and height \(S\),
embedded rank-preservingly and saturatedly in a Boolean lattice: intrinsic
rank differs from Boolean cardinality by one fixed constant, and every
rank-one comparability is a Boolean cover. Let \(L>S\), and suppose
\(Q\times[0,L]\) is realized on disjoint coordinate sets. Every ambient
Boolean word covering all targets in its plateau ranks
\(S,S+1,\ldots,L\) has length, provided those plateau targets are nonempty,

\[
 n\ge B+\left\lceil\frac{B(L-S)}{2L}\right\rceil.             \tag{3.1}
\]

Foreign letters and witnesses leaving the subposet are allowed.

#### Proof

Put \(H=L-S\). Each plateau layer has exactly \(B\) targets, one above each
point of \(Q\). Partition the chosen witnesses by common left endpoint.
Each class is a strict inclusion chain, because intervals with a common left
endpoint are nested. If the partition has \(C=B+\delta\) classes, the sets
of classes meeting two consecutive plateau layers intersect in at least
\(2B-C=B-\delta\) classes. Across the \(H\) adjacent layer pairs, the
partition therefore contains at least

\[
                         H(B-\delta)                          \tag{3.2}
\]

Boolean covers between plateau targets.

Use the potential \(\phi(q,z)=\operatorname{rk}_Q(q)\), whose range is
\([0,S]\). The bottom and top plateau layers have the same
\(\phi\)-multiset. Exactly \(B\) partition classes meet each boundary, so
there are \(\delta\) internal class starts and \(\delta\) internal class ends.
Telescoping \(\phi\) along all classes shows that their total number of
transverse covers is at most \(S\delta\). Hence this endpoint partition
contains at least

\[
 H(B-\delta)-S\delta=HB-L\delta                              \tag{3.3}
\]

vertical covers.

Apply the same argument to right endpoints, with excesses
\(\delta_L,\delta_R\). The two partitions are orthogonal: a common left and
right endpoint determine one physical interval and one target. Thus no
vertical cover can occur in both partitions. Since there are exactly
\(BH\) vertical plateau covers,

\[
 2BH-L(\delta_L+\delta_R)\le BH,
 \qquad
 \delta_L+\delta_R\ge\frac{BH}{L}.                            \tag{3.4}
\]

Each partition has at most \(n\) classes, so
\(2(n-B)\ge\delta_L+\delta_R\). Taking the integer ceiling proves (3.1).
\(\square\)

For \(Q=[0,p]\times[0,q]\), \(B=(p+1)(q+1)\), \(S=p+q\), and \(L=r\),
(3.4) says that the two endpoint partitions of a bad box have at least
\(2w(B)+d(B)\) box-endpoint incidences.

Select now the complete plateau in every bad box and only the middle layer
in every good box. The selected middle targets over all boxes form one
global antichain of size \(W(3s)\). For physical position \(j\), let
\(\ell_j\) and \(r_j\) be the numbers of distinct boxes represented there as
a left or right endpoint, and put

\[
 \mathcal C_\partial
 :=\sum_j\bigl((\ell_j-1)_+ +(r_j-1)_+\bigr).                 \tag{3.5}
\]

### Theorem 3.2 (global endpoint-sharing necessity)

If a word of length \(W(3s)+E\) covers the selected targets, then

\[
                 \boxed{\mathcal C_\partial\ge D_s-2E.}       \tag{3.6}
\]

Consequently, if \(E=o(W(3s))\), then

\[
 \mathcal C_\partial\ge(\Gamma-o(1))W(3s).                  \tag{3.7}
\]

If sharing is confined within independently serviced packets of at most
\(K\ge2\) whole parent boxes and \(Q_\partial\) is the number of oriented
physical endpoints used by at least two boxes, then

\[
 Q_\partial\ge\frac{(D_s-2E)_+}{K-1}.                        \tag{3.8}
\]

In particular, \(o(s)\) average sharing surplus per parent forces
\(E\ge(\Gamma/2-o(1))W(3s)\).

#### Proof

Lemma 3.1 gives total endpoint-box incidence at least
\(2W(3s)+D_s\): bad boxes contribute \(2w(B)+d(B)\), and the selected
middle antichain in every good box contributes \(2w(B)\). On the other
hand,

\[
 \sum_j\ell_j\le W(3s)+E+\sum_j(\ell_j-1)_+,
\]

and similarly on the right. This proves (3.6), and (3.7) follows from
Theorem 1.2.

Within a \(K\)-parent packet, one oriented shared endpoint contributes at
most \(K-1\) to (3.5), proving (3.8). Finally the number of parent boxes is
\(W(s)^3\sim(2\sqrt3/(\pi s))W(3s)\). Thus \(o(s)\) average surplus per
parent is \(o(W(3s))\); (3.6) then gives the last assertion. \(\square\)

This theorem makes the role of good parents precise: they supply endpoint
capacity, never a negative local rebate.

## 4. A cross-box cover-transition dual

The preceding ledger does not yet force the shared targets to be adjacent
in rank. The following exact inequality measures the price of rank gaps.

Let a selected target family \(\mathcal T\) lie in an interval of \(R\)
consecutive ranks and be labelled by product boxes. For orientation
\(o\in\{L,R\}\), let

* \(P_o\) be the number of physical endpoints used;
* \(I_o\) be the number of endpoint-box incidences;
* \(S_o:=I_o-P_o\) be the sharing surplus; and
* \(X_o\) be the number of adjacent pairs in endpoint classes that are
  cross-box Boolean covers.

Let \(E_\times\) be the total number of permitted cross-box Boolean covers
inside \(\mathcal T\).

### Theorem 4.1 (cover-transition inequality)

For every fixed witness choice,

\[
 S_o\le X_o+RP_o-|\mathcal T|,                                \tag{4.1}
\]

and

\[
 S_L+S_R\le E_\times+2(Rn-|\mathcal T|).                     \tag{4.2}
\]

If local endpoint duals give

\[
 I_L+I_R\ge2W_0+\Gamma_0                                   \tag{4.3}
\]

and \(n=W_0+e\), then

\[
 \boxed{
 e\ge
 \frac{[\Gamma_0-E_\times-2(RW_0-|\mathcal T|)]_+}
      {2(R+1)}.}                                             \tag{4.4}
\]

#### Proof

At one endpoint, suppose \(k\) targets from \(d\) distinct box labels occur.
Ordered by rank they form a strict inclusion chain. At least \(d-1\) of
the consecutive transitions change labels. A label-changing transition is
either a Boolean cover, counted by \(X_o\), or skips at least one rank. The
skipped open rank intervals for consecutive transitions are disjoint, and
there are only \(R-k\) unused rank slots. Therefore

\[
                         d-1\le x+(R-k).                      \tag{4.5}
\]

Summing over endpoints gives (4.1).

A fixed cover cannot occur in both endpoint partitions: that would give its
two targets the same left and the same right endpoint, hence the same
witness interval. Thus \(X_L+X_R\le E_\times\). Since \(P_L,P_R\le n\),
summing (4.1) proves (4.2).

Finally \(I_o=P_o+S_o\le n+S_o\). Combine this with (4.2)--(4.3), substitute
\(n=W_0+e\), and rearrange to obtain (4.4). \(\square\)

### Lemma 4.2 (one-factor-fibre support)

If \(X\lessdot Y\) is a cross-box Boolean cover between two product-SCD
boxes, the two boxes have the same chain owner in two coordinate blocks and
differ only in the block containing the unique coordinate of \(Y\setminus
X\). In that block, the two factor masks form a cross-chain Boolean cover.
Conversely, every such one-block cross-chain cover, with fixed masks in the
other two factor chains, is a cross-box product cover.

#### Proof

The masks of \(X,Y\) agree in the two unchanged coordinate blocks, and the
SCD gives each mask a unique chain owner there. In the changed block their
masks differ by one coordinate. If their owner also agreed, all three
owners would agree and the product boxes would be identical. The converse
is immediate by adjoining the two fixed factor masks. \(\square\)

Thus every saturated unit in (4.2) lies in a one-factor fibre. In (4.4),
\(E_\times\) must count **all** cross-box covers permitted to the selected
targets; it may be restricted to within-packet covers only when witnesses
are genuinely packet-confined.

## 5. A two-parent comparability obstruction

The next result does not require adjacency in rank and applies before any
Safe-Pin or MTF-order constraint.

### Theorem 5.1 (matching forced by a dominant parent)

Let \(B=[0,p]\times[0,q]\times[0,r]\) be bad, with width
\(w=(p+1)(q+1)\), and put

\[
 D_B:=w\frac{r-p-q}{r}.                                      \tag{5.1}
\]

Let \(G\) be any distinct parent of width \(v\). Suppose one word of length

\[
                         n=w+v+e                              \tag{5.2}
\]

covers the full plateau of \(B\) and the middle layer of \(G\). Then, in
one of the two endpoint orientations, the cross-parent comparability graph
between those selected targets contains a matching of size at least

\[
 \boxed{
 \max\left\{0,\left\lceil\frac{D_B}{2}\right\rceil-e\right\}
 =\max\left\{0,\left\lceil\frac{D_B-2e}{2}\right\rceil\right\}.} \tag{5.3}
\]

#### Proof

For one orientation, the endpoint partition of the \(B\)-plateau has
\(w+\delta_o\) classes, exactly \(w\) of which meet the \(B\) middle layer.
All \(w+v\) middle targets of \(B\cup G\) lie at the same global rank, so
they are pairwise incomparable and have distinct physical endpoints. The
word has only \(e\) further positions. Hence at least
\((\delta_o-e)_+\) extra \(B\)-classes share their endpoints with distinct
\(G\)-middle targets. Targets sharing an endpoint are comparable, and
distinct classes and endpoints make these pairs a matching.

Lemma 3.1 gives
\(\delta_L+\delta_R\ge D_B\); since the left side is integral, one
orientation has \(\delta_o\ge\lceil D_B/2\rceil\). This proves (5.3).
\(\square\)

For heights of order \(\sqrt s\) and a fixed positive relative plateau gap,
(5.3) demands \(\Theta(s)\) distinct comparable pairs in a near-sum-width
two-parent fusion. Corollary 2.2 supplies enough *unlabelled* partner width,
but it does not supply this matching.

## 6. An explicit optimal recursive-sibling fusion atom

The matching obstruction is not universal. Here is an exact family in
which a recursive sibling pair shares witnesses at coefficient one.

Let \(u\) be a new coordinate. From a symmetric chain

\[
 A_a\subset A_{a+1}\subset\cdots\subset A_{s-1-a}
 \quad\hbox{in }\mathcal B_{s-1}
\]

the standard recursion produces the long and short siblings

\[
\begin{aligned}
 C&=(A_a,\ldots,A_{s-1-a},A_{s-1-a}\cup\{u\}),\\
 D&=(A_a\cup\{u\},\ldots,A_{s-2-a}\cup\{u\}).                \tag{6.1}
\end{aligned}
\]

Write their vertices as \(C_0,\ldots,C_c\) and
\(D_0,\ldots,D_{c-2}\), where \(c=s-2a\). Fix two other chains
\(P_0,\ldots,P_p\) and \(Q_0,\ldots,Q_q\), and assume

\[
                         c=p+q+2.                             \tag{6.2}
\]

Put \(w=(p+1)(q+1)\). For every \(0\le i\le p\), \(0\le j\le q\), set

\[
 z=c-1-i-j,\qquad
 X_{ij}=P_i\cup Q_j\cup C_z,\qquad
 Y_{ij}=P_i\cup Q_j\cup D_{z-1}.                             \tag{6.3}
\]

Here unions mean unions of masks on the three disjoint coordinate blocks.

### Theorem 6.1 (coefficient-one sibling atom)

The \(X_{ij}\) are exactly the complete middle layer of
\(P\times Q\times C\), and the \(Y_{ij}\) are exactly the complete middle
layer of \(P\times Q\times D\). Moreover

\[
 X_{ij}\cup Y_{ij}
 =P_i\cup Q_j\cup(A_{a+z}\cup\{u\}).                         \tag{6.4}
\]

For \((i,j)\ne(0,0)\), these unions are exactly all \(w-1\) targets in the
first layer above the middle of \(P\times Q\times D\). For \((i,j)=(0,0)\)
the union is the target \(P_0\cup Q_0\cup C_c\), one rank above the middle
of \(P\times Q\times C\).

Consequently, concatenating the \(w\) two-letter blocks

\[
                         (X_{ij},Y_{ij})                       \tag{6.5}
\]

in any order gives a literal word of length \(2w\) covering both complete
middle layers, the complete first upper layer of the short sibling box, and
one upper target of the long sibling box. This length is optimal for these
targets.

#### Proof

From (6.2), \(1\le z\le c-1\). The local index sum in the long box is

\[
                         i+j+z=c-1,                           \tag{6.6}
\]

its central rank; in the short box it is
\(i+j+(z-1)=c-2\), again its central rank. Varying \(i,j\) gives all \(w\)
points in each layer.

Since \(C_z=A_{a+z}\) for \(z\le c-1\) and
\(D_{z-1}=A_{a+z-1}\cup\{u\}\), nesting of the \(A\)-chain gives (6.4).
When \(i+j\ge1\), \(z\le c-2\), so the right side is
\(P_i\cup Q_j\cup D_z\). The equation \(i+j+z=c-1\) enumerates the whole
upper layer of the short box; the sole impossible pair there is
\((i,j)=(0,0)\), hence it has \(w-1\) points. For that remaining pair,
\(z=c-1\) and (6.4) is \(P_0\cup Q_0\cup C_c\).

Singleton intervals in (6.5) witness every \(X_{ij},Y_{ij}\), and each
adjacent two-letter interval witnesses their union (6.4). The \(2w\)
middle targets form a same-rank antichain, so no word covering them can have
fewer than \(2w\) distinct endpoints, and hence no fewer than \(2w\)
letters. \(\square\)

This is a genuine non-product packet fusion, but it does **not** cover the
entire plateau of the long sibling. It is a local atom, not a solution of
the global packet problem.

## 7. Full recursive closures cannot rescue the deep cone

The preceding atom suggests iterating recursive sibling diamonds. The
following theorem shows exactly where that natural amplification fails.

Start with an ancestor chain of height \(h\), expose \(d\) fresh Boolean
coordinates one at a time, and retain every descendant chain created by the
standard SCD recursion. The descendants form an SCD of
\([0,h]\times\mathcal B_d\), and every descendant height \(p\) satisfies

\[
                         |p-h|\le d,                           \tag{7.1}
\]

because each recursive split changes height by \(+1\) or \(-1\).

For three ancestor chains of heights \(h_1,h_2,h_3\), expose
\(d_1,d_2,d_3\) fresh coordinates and include **all** descendant Cartesian
boxes. Put \(D=d_1+d_2+d_3\). Their literal union is

\[
 \mathcal P\cong Q\times[0,h_3],                              \tag{7.2}
\]

where

\[
 Q=[0,h_1]\times\mathcal B_{d_1}
   \times[0,h_2]\times\mathcal B_{d_2}\times\mathcal B_{d_3},
\]

so

\[
 |Q|=(h_1+1)(h_2+1)2^D,\qquad
 \operatorname{ht}Q=h_1+h_2+D.                              \tag{7.3}
\]

### Theorem 7.1 (recursive-closure excess)

If \(h_3>h_1+h_2+D\) and \(h_1+h_2+D>0\), every word covering all nonempty
targets of \(\mathcal P\) satisfies

\[
 n(\mathcal P)\ge |Q|+
 \left\lceil
 \frac{|Q|(h_3-h_1-h_2-D)}{2h_3}
 \right\rceil.                                               \tag{7.4}
\]

This is excess over the **sum** of the descendant-box widths, not a sum of
separate descendant lower bounds:

\[
                \sum_{B\subset\mathcal P}w(B)=w(\mathcal P)=|Q|. \tag{7.5}
\]

#### Proof

Apply Lemma 3.1 to (7.2), with \(B=|Q|\), \(S=h_1+h_2+D\), and \(L=h_3\).
This proves (7.4), even when the witnesses freely cross descendant-box
boundaries.

Every recursive descendant chain is symmetric about the centre of its
ancestor product \([0,h_i]\times\mathcal B_{d_i}\). Therefore all
descendant triple boxes have the same centre. Their middle layers partition
the middle layer of \(\mathcal P\), whose plateau width is \(|Q|\). This
proves (7.5). \(\square\)

Let \(K\) be the number of descendant boxes. Since a graded poset of height
\(h+d\) has width at least its cardinality divided by \(h+d+1\),

\[
 w([0,h]\times\mathcal B_d)
 \ge\frac{(h+1)2^d}{h+d+1}
 \ge\frac{2^d}{d+1},                                        \tag{7.6a}
\]

where the second inequality is
\((h+1)(d+1)\ge h+d+1\). Therefore

\[
\begin{aligned}
 K&=\prod_{i=1}^3w([0,h_i]\times\mathcal B_{d_i})\\
  &\ge\prod_{i=1}^3\frac{2^{d_i}}{d_i+1}
   \ge\frac{2^D}{(D+1)^3}.                                  \tag{7.6}
\end{aligned}
\]

### Corollary 7.2 (positive-density no-go for small full closures)

Suppose the product boxes are partitioned into independently concatenated
full recursive closures and, writing \(K_{\mathcal P}\) for the number of
descendants in a closure,

\[
 \max_{\mathcal P\ {\rm meeting}\ (7.8)}
       \log K_{\mathcal P}=o(\sqrt s).                        \tag{7.6b}
\]

Then

\[
 \liminf_{s\to\infty}\frac{L}{W(3s)}
 \ge1+\frac{\sqrt3}{5\pi}
 \bigl(e^{-1/2}-e^{-121/200}\bigr)^2
 \bigl(e^{-9/2}-e^{-961/200}\bigr)>1.                        \tag{7.7}
\]

#### Proof

Consider oriented descendants whose heights satisfy

\[
 p,q\in[\sqrt s,1.1\sqrt s],\qquad
 r\in[3\sqrt s,3.1\sqrt s].                                 \tag{7.8}
\]

If such a descendant lies in a closure with recursion depths \(d_i\), then
(7.1) gives

\[
 h_3-h_1-h_2-D\ge r-p-q-2D.                                 \tag{7.9}
\]

Equations (7.6) and (7.6b) imply \(D=o(\sqrt s)\), uniformly for the
closures under consideration. For all large \(s\), take
\(D\le\sqrt s/40\). Then the right side of (7.9) is at least
\(0.75\sqrt s\), while \(h_3\le3.125\sqrt s\). The excess fraction in
(7.4) is therefore at least

\[
 \frac{0.75}{2(3.125)}=\frac3{25}>\frac1{10}.                \tag{7.10}
\]

Hence every closure meeting (7.8) costs at least \(1.1\) times the sum of
all its descendant widths.

By Lemma 1.1, the two low windows have chain probability

\[
 \kappa_L=e^{-1/2}-e^{-121/200},
\]

and the high window has probability

\[
 \kappa_H=e^{-9/2}-e^{-961/200}.
\]

On (7.8), \(w(B)=(p+1)(q+1)\ge s\). Equations (1.9) and the independent
height law show that these oriented boxes carry limiting width at least

\[
 \omega_*:=\frac{2\sqrt3}{\pi}\kappa_L^2\kappa_H>0.          \tag{7.11}
\]

The closures are disjoint. Summing their ten-per-cent excess over all
closures meeting (7.8), and using the trivial width lower bound on the
others, gives \(L/W(3s)\ge1+\omega_*/10-o(1)\), which is (7.7).
\(\square\)

### Corollary 7.3 (mixing threshold)

If a full recursive closure contains a descendant satisfying (7.8) and
also contains any nonobstructed descendant, then

\[
 D\ge0.4\sqrt s,\qquad
 K\ge\frac{2^{0.4\sqrt s}}{(3s+1)^3}.                        \tag{7.12}
\]

#### Proof

Let \((p',q',r')\) be a nonobstructed descendant in the same oriented
factors. Heights of two descendants of the same ancestor differ by at most
\(2d_i\). Thus

\[
 r-2d_3\le r'\le p'+q'\le p+q+2d_1+2d_2,
\]

and so \(2D\ge r-p-q\ge0.8\sqrt s\). Insert this in (7.6), using
\(D\le3s\), to obtain (7.12). \(\square\)

The full-closure hypothesis is essential. These results do not exclude a
sparse choice of descendants from many remote recursion families, nor one
global word crossing all such families.

## 8. Why heights alone cannot produce literal packets

The reflection theorem pairs height types. Literal MTF compatibility also
depends on the ordered coordinate increments of the factor chains. The
smallest exact example already occurs in \(\mathcal B_4\).

For a two-edge chain with consecutive increment coordinates \((e_1,e_2)\),
a one-letter update realizes cutoff \(1\) exactly when it contains \(e_1\)
and omits \(e_2\).

### Proposition 8.1 (same heights, opposite frontier compatibility)

There is an SCD of \(\mathcal B_4\) containing height-two chains with
increment sequences \((1,2)\) and \((2,3)\), and no one-letter update can
realize cutoff \(1\) on both. There is another SCD with height-two chains
of increment sequences \((1,2)\) and \((3,4)\), for which the update
\(\{1,3\}\) realizes cutoff \(1\) on both.

#### Proof

The first SCD is

\[
\begin{array}{l}
 \varnothing<1<14<134<1234,\\
 3<13<123,\qquad 4<24<234,\qquad 2<12<124,\\
 23,\qquad34.
\end{array}                                                   \tag{8.1}
\]

Its displayed height-two chains have increments \((1,2)\) and \((2,3)\).
The first demands \(1\in U,2\notin U\), while the second demands
\(2\in U,3\notin U\), a contradiction.

The second SCD is

\[
\begin{array}{l}
 \varnothing<1<12<123<1234,\\
 2<23<234,\qquad3<13<134,\qquad4<14<124,\\
 24,\qquad34.
\end{array}                                                   \tag{8.2}
\]

The chains \(2<23<234\) and \(4<14<124\) have increments \((3,4)\) and
\((1,2)\); \(U=\{1,3\}\) meets the required contain/omit conditions. Each
display lists \(1,4,6,4,1\) sets in ranks \(0,1,2,3,4\), so both are indeed
SCDs. \(\square\)

Fixing the same other two factor chains turns Proposition 8.1 into two
families of three-chain parents with identical height data but opposite
common-reset feasibility for this prescribed one-letter frontier pattern.
Thus the scalar reflection pairing cannot, by height data alone, certify
the simultaneous one-letter cutoffs needed by this particular fusion
architecture. The example does not rule out a height-guided existential
choice of different partners, a multi-letter packet, or another chronology.

## 9. The exact surviving MTF state-lift criterion

The scalar transport is complete, and Theorems 3.2, 4.1, and 5.1 show what
the reflected-pair architecture still lacks. To state that gate without
assuming a word in its own hypothesis, use the exact last-occurrence state
formalism.

An ordered partition of \([3s]\) is
\(\Pi=(B_1,\ldots,B_b)\), with nonempty disjoint blocks covering the ground
set. Put

\[
 \operatorname{Pref}(\Pi)
 =\{B_1,B_1\cup B_2,\ldots,B_1\cup\cdots\cup B_b\}.           \tag{9.1}
\]

For a nonempty mask \(X\), define

\[
 M_X(\Pi)=(X,B_1\setminus X,\ldots,B_b\setminus X),           \tag{9.2}
\]

deleting empty blocks. An MTF state path is a sequence
\(\Pi_1,\ldots,\Pi_T\) with
\(\Pi_{t+1}=M_{X_t}(\Pi_t)\) for nonempty updates \(X_t\).

### Lemma 9.1 (exact state paths imply a literal word)

Let \(\{\Pi_{j,1},\ldots,\Pi_{j,T_j}\}_{j=1}^J\) be finite MTF state paths,
and let \(b_j\) be the number of blocks of \(\Pi_{j,1}\). If

\[
 \bigcup_{j,t}\operatorname{Pref}(\Pi_{j,t})
 \supseteq\mathcal B_{3s}\setminus\{\varnothing\},            \tag{9.3}
\]

then there is a literal contiguous-OR word covering every nonempty target,
of length

\[
              \sum_jT_j+\sum_j(b_j-1).                       \tag{9.4}
\]

#### Proof

For path \(j\), initialize \(\Pi_{j,1}=(B_1,\ldots,B_{b_j})\) by writing

\[
                       B_{b_j},B_{b_j-1},\ldots,B_1,          \tag{9.5}
\]

then append its updates \(X_1,\ldots,X_{T_j-1}\). After (9.5), the
last-occurrence ordered partition is exactly \(\Pi_{j,1}\); after each
subsequent update it is the next state by (9.2). At the endpoint of a state,
its suffix ORs are exactly its prefix unions (9.1). Hence every target in
(9.3) has a contiguous witness lying wholly inside this path segment.
Concatenate the \(J\) segments. Their internal witnesses remain contiguous,
and the total length is
\(\sum_j(b_j+T_j-1)\), which is (9.4). \(\square\)

The exact unproved state target is now the following.

### Unproved Lemma 9.2 (reflected-pair MTF path cover)

For each \(s\), there exist choices of the three block SCDs, the resulting
product parents, and MTF state paths as in Lemma 9.1 such that

\[
 \sum_jT_j=W(3s)+o(W(3s)),\qquad
 \sum_j(b_j-1)=o(W(3s)),                                    \tag{9.6}
\]

and (9.3) holds. In addition, within the reflected-pair architecture one
asks for the following literal representation of all but \(o(W(3s))\) of
the lower demand (1.4). Regard the demand as labelled copies
\((B,k)\), \(1\le k\le d(B)\). Choose \(D_s-o(W(3s))\) of these copies and
inject them into pairwise distinct good-parent middle targets, using the
parent pairing of Corollary 2.2. For every chosen copy, name a state
\(\Pi_{j,t}\) containing both its assigned good target and a bad-parent
plateau target in \(\operatorname{Pref}(\Pi_{j,t})\); for fixed \(B\), the
named box-state incidences \((B,j,t)\) are distinct. Whenever the two named
prefixes are adjacent in rank, Lemma 4.2 requires their transition to be a
one-factor-fibre cross-chain cover. Rank-skipping sharing is instead subject
collectively to the unused-rank-slot term of Theorem 4.1.

The full prefix coverage (9.3) includes every target in exceptional boxes;
no inference is made that \(o(W)\) discarded endpoint demand would itself
be cheap to cover. Lemma 9.1 proves that (9.6) implies a word of length
\(W(3s)+o(W(3s))\), and hence the coefficient-one bound on the
three-block subsequence.

Lemma 9.2 is a sufficient architecture, not a necessary characterization
of every possible proof. It has two open gates:

* a labelled Hall/frontier construction producing enough comparable shared
  prefixes from the scalar reflection pairing; and
* a state-path construction with the exact initialization ledger (9.6).

Proposition 8.1 shows why height data alone do not certify the first gate for
the prescribed one-letter pattern. The second gate is not implied by an
incidence count. Extending the conclusion from dimensions \(3s\) to all
dimensions would additionally require balanced block sizes differing by at
most one, or a separate residue-class lift; no such lift is proved here.

## 10. Adversarial audit and exact scope

The strongest positive and negative claims were checked against the
following failure modes.

1. **Ordered versus labelled cones.** The factor \(3\) implicit in the
   ordered Rayleigh law is included in (1.14). The reflection proof works
   on all three labelled oriented cones and sums every eligible preimage in
   (2.9); it is not a one-preimage argument.

2. **Integer ceilings.** There are \(W(s)^3=O(W(3s)/s)\) parent boxes, so
   replacing the real endpoint demand by (1.4) costs \(o(W(3s))\). The
   pointwise inequality \(d(B)\le w(B)\) remains exact.

3. **Discretizing the reflection.** A fixed finite mesh gives only a fixed
   error. Corollary 2.2 uses a slowly refining diagonal mesh after removing
   axes, wall, and tails. The strict interior density and width margins are
   what permit integral pairing.

4. **What reflection does not prove.** It proves parent-type injection and
   token capacity only. It proves neither comparable masks nor endpoint
   chronology. Proposition 8.1 is an exact witness to this gap.

5. **Foreign witnesses.** Lemma 3.1 and Theorem 7.1 use only the selected
   targets and their physical endpoints. Letters may lie outside the local
   product, and intervals may cross child boundaries. Thus (7.4) is a true
   fused-packet lower bound.

6. **Cross-cover counting.** Theorem 4.1 permits rank gaps and charges them
   to unused rank slots. Its \(E_\times\) must include every cover actually
   allowed by the witness model. Restricting it to nominal packet edges
   without packet-confined witnesses would be invalid.

7. **Sibling atom scope.** The word (6.5) is optimal for its stated target
   family, but it covers only one upper target of the long sibling. It does
   not cancel the long sibling's full plateau deficit.

8. **Recursive no-go scope.** Corollaries 7.2--7.3 require full descendant
   closure and independent concatenation between closures. They do not
   exclude sparse cross-family selection or a single global word.

9. **No overclaim about the conjecture.** The results prove a stronger-than-
   separate-payment obstruction for a broad canonical packet class and one
   exact local rescue atom. They neither prove nor disprove the global
   contiguous-OR width conjecture.

The stable conclusion is therefore: the obstruction cone can be balanced
at the exact asymptotic resource level, but the reflected-pair architecture
still needs a genuinely labelled comparability-and-sequencing theorem.
Adjacent-rank sharing is confined to one-factor fibres, while rank-skipping
sharing incurs the exact gap ledger of Theorem 4.1. Small full recursive
closures fail; arbitrary non-full packets and large full closures remain
open. Signed mass and parent height type alone do not furnish the missing
literal witnesses.
