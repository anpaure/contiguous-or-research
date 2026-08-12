# Exact PBBS reciprocal-height trace and its stability defect

Date: 2026-07-26  
Method: pure mathematics only; no computation or search

## 0. Outcome

Put

\[
 N=2m+1,
 \qquad B_m=\operatorname {Cat}_m,
 \qquad H=\lceil A\sqrt m\rceil,
\]

where \(A>0\) is fixed. Delete the quotient \(\tau\)-cycles of length at
most \(H+1\), and let \(V_H\) be the remaining Dyck-root edge set. For a
root \(D\), write \(h(D)=\operatorname {ht}(D)\), and define the exact
long-cycle reciprocal trace

\[
 \mathcal T_{m,H}
 :=\sum_{\substack{D\in V_H\\h(D)\le H-1}}
       {1\over h(D)+2}.
 \tag{0.1}
\]

The existing quotient bound is correct, and in fact

\[
 \boxed{
 c_A{B_m\over\sqrt m}
 \le\mathcal T_{m,H}
 \le C{B_m\over\sqrt m}}
 \tag{0.2}
\]

for all sufficiently large \(m\), with \(c_A>0\) and an absolute upper
constant \(C\). Every quotient-edge-disjoint short-return packing obeys

\[
 \boxed{\overline\nu_H\le\mathcal T_{m,H}
 =O_A(B_m/\sqrt m).}
 \tag{0.3}
\]

The useful new audit statement is an exact complementary-slackness
identity. If \(x_I\) is any feasible fractional packing of eligible return
supports, \(s(I)\) is the step-two core duration, and \(h(I)\) is the
invariant height, then

\[
\boxed{
\begin{aligned}
 \mathcal T_{m,H}-\sum_Ix_I
 ={}&\sum_Ix_I\,{s(I)-h(I)\over h(I)+2}\\
 &+\sum_{D\in V_H\,:\,h(D)\le H-1}
 {1-\sum_{I\ni D}x_I\over h(D)+2}.
\end{aligned}}
\tag{0.4}
\]

Both terms are nonnegative. For an integral packing the second is exactly
the reciprocal mass of uncovered eligible quotient edges.

Iterated peak deletion resolves the first defect further. If
\(\partial^{h(I)-1}D=(10)^{p(I)}\), and
\(s_0(I),\ldots,s_{h(I)-1}(I)\) are the nested half-gaps, then

\[
 s(I)-h(I)
 =p(I)-1+\sum_{j=0}^{h(I)-2}
       \bigl(s_j(I)-s_{j+1}(I)-1\bigr).             \tag{0.5}
\]

Every term on the right is a nonnegative integer. Substitution in (0.4)
gives a complete quantitative stability ledger.

Thus equality in the trace bound requires simultaneously:

1. \(p(I)=1\) and every nested return gap drops by exactly two at every
   selected interval, equivalently \(s(I)=h(I)\);
2. every eligible long-cycle quotient edge has packing load exactly one.

For an integral packing, every retained \(\tau\)-cycle of height at most
\(H-1\) must consequently be tiled by height-equality supports of length
\(h+2\). Near equality forces the corresponding approximate tiling and
minimal-gap conditions quantitatively.

This is a stability saving, but not a little-oh theorem. Every zero-winding
return is a height-gap equality case. Moreover an additive slack
\(s-h=O(1)\) costs only \(O(m^{-1/2})\) per Gaussian interval, so even
\(\Theta(B_m/\sqrt m)\) such intervals pay only \(O(B_m/m)\), negligible
relative to the trace. The remaining task is therefore to exclude an
almost-tiling by equality or bounded-slack genuine PBBS returns; height
alone cannot do so.

## 1. Exact quotient support and the three identities before counting

Let a consecutive omitted-coordinate return have odd physical gap

\[
 g=2s+1.
\]

Under the insertion-edge convention its complete quotient support is

\[
 Q(D,s)=\{e_D,e_{\tau D},\ldots,e_{\tau^{s+1}D}\},
 \qquad |Q(D,s)|=s+2.                               \tag{1.1}
\]

The residence cutoff \(s+1\le H\) is exactly

\[
 1\le s\le H-1.                                    \tag{1.2}
\]

There are three inputs.

### 1.1 Height invariance

If \(D=P1Q\) at its first step reaching height \(h\), then

\[
 \phi(D)=\overline Q0\overline P
\]

also has height exactly \(h\). Indeed, \(\overline Q\) rises from zero
to \(h\) without leaving \([0,h]\); after the displayed zero, the word
\(\overline P\), read from height \(h-1\), stays in \([0,h-1]\) and
returns to zero. Hence

\[
 h(\phi D)=h(D),
 \qquad h(\tau D)=h(D).                            \tag{1.3}
\]

This is an equality, not an estimate. Every root in (1.1) has the same
height.

### 1.2 Height-gap inequality

The peak-deletion/equality-particle theorem gives

\[
 g\ge2h(D)+1,
 \qquad\text{equivalently}\qquad s\ge h(D).        \tag{1.4}
\]

Therefore every eligible return has

\[
 h(D)\le s\le H-1.                                 \tag{1.5}
\]

For fixed \(A\), one has \(2H-1<N\) for all sufficiently large \(m\), so
the full nested return-chain theorem applies without a wrapping exception.
After \(h-1\) simultaneous peak deletions the remaining height-one path is
\((10)^p\). The successive same-label return gaps
\(g_j=2s_j+1\) satisfy

\[
 s_{j+1}\le s_j-1,
 \qquad s_{h-1}=p.
\]

Telescoping gives (0.5). Consequently

\[
 s=h
 \quad\Longleftrightarrow\quad
 p=1\ \text{ and }\ s_j-s_{j+1}=1
 \text{ for every }j.                              \tag{1.6}
\]

This is the exact equality condition in (1.4). The audited zero-winding
word recursion implies \(s=h\), so zero winding lies wholly in this
equality class. The converse is not asserted.

### 1.3 Edge capacity

On the retained cycles, every support (1.1) is nonwrapping and has distinct
edges. For a feasible fractional packing define its edge load

\[
 \ell_D=\sum_{I\ni D}x_I\le1.                      \tag{1.7}
\]

Because of (1.3),

\[
 \sum_{D\in Q(I)}{1\over h(D)+2}
 ={s(I)+2\over h(I)+2}
 =1+{s(I)-h(I)\over h(I)+2}.                       \tag{1.8}
\]

This is the only place where the height-gap inequality enters the
reciprocal trace.

## 2. Exact complementary-slackness identity

Let

\[
 w_D={\mathbf1_{\{D\in V_H,\ h(D)\le H-1\}}\over h(D)+2}.
\]

Every eligible support lies in the positive-weight set. By finite double
counting,

\[
 \sum_Dw_D\ell_D
 =\sum_Ix_I{s(I)+2\over h(I)+2}.                   \tag{2.1}
\]

Subtract \(\sum_Ix_I\) and use (1.8):

\[
\begin{aligned}
 \mathcal T_{m,H}-\sum_Ix_I
 &=(\mathcal T_{m,H}-\sum_Dw_D\ell_D)
   +\sum_Ix_I{s(I)-h(I)\over h(I)+2}\\
 &=\sum_Dw_D(1-\ell_D)
   +\sum_Ix_I{s(I)-h(I)\over h(I)+2}.
\end{aligned}
\]

This proves (0.4). In particular, \(w\) is a feasible fractional dual,
and

\[
 \overline\nu_H\le p_H^*=d_H^*\le\mathcal T_{m,H}. \tag{2.2}
\]

For an integral packing \(\mathcal P\), (0.4)--(0.5) become

\[
\boxed{
\begin{aligned}
 \mathcal T_{m,H}-|\mathcal P|
 ={}&\sum_{I\in\mathcal P}{p(I)-1\over h(I)+2}\\
 &+\sum_{I\in\mathcal P}\sum_{j<h(I)-1}
 {s_j(I)-s_{j+1}(I)-1\over h(I)+2}\\
 &+\sum_{\substack{D\in V_H,\ h(D)\le H-1\\
                    D\notin\bigcup_{I\in\mathcal P}Q(I)}}
 {1\over h(D)+2}.
\end{aligned}}
\tag{2.3}
\]

Every displayed summand is nonnegative. This identity gives all equality
conditions claimed in Section 0. On one retained height-\(h\) cycle,
equality means a partition into supports of size \(h+2\); in particular,
the cycle length must be divisible by \(h+2\).

## 3. Exact Dyck trace and the \(B_m/\sqrt m\) scale

Let

\[
 b_{m,h}=\#\{D\in\mathcal D_m:h(D)=h\},
 \qquad
 M_{m,h}=\sum_{j\le h}b_{m,j}.
\]

Before short-cycle deletion the trace is

\[
 \mathcal T^{\rm all}_{m,H}
 =\sum_{h=1}^{H-1}{b_{m,h}\over h+2}.              \tag{3.1}
\]

Summation by parts gives the exact identity

\[
\boxed{
 \mathcal T^{\rm all}_{m,H}
 ={M_{m,H-1}\over H+1}
 +\sum_{h=1}^{H-2}
 {M_{m,h}\over(h+2)(h+3)}.}
\tag{3.2}
\]

The number of roots removed with short cycles satisfies

\[
 Z_H\le(2H+2)N^{2H+2}=\exp(o(m)).                  \tag{3.3}
\]

Since every reciprocal weight is at most \(1/3\),

\[
 0\le\mathcal T^{\rm all}_{m,H}-\mathcal T_{m,H}
 \le {Z_H\over3}
 =o_A(B_m/N).                                      \tag{3.4}
\]

Thus short-cycle deletion is negligible by an extra factor
\(m^{-1/2}\) compared with the critical trace.

The exact path-graph spectrum is

\[
 M_{m,h}
 ={2\over h+2}\sum_{j=1}^{h+1}
 \sin^2{\pi j\over h+2}
 \left(2\cos{\pi j\over h+2}\right)^{2m}.        \tag{3.5}
\]

For \(2\le h\le\sqrt m\), the sine bound and Gaussian cosine decay in
(3.5) give

\[
 M_{m,h}
 \le C{4^m\over h^3}
       \exp\!\left(-c{m\over h^2}\right).         \tag{3.6}
\]

Here is the complete scale calculation. In a dyadic band
\(u/2<h\le u\le\sqrt m\),

\[
 \sum_{u/2<h\le u}{b_{m,h}\over h+2}
 \le {2M_{m,u}\over u}
 \le C{4^m\over u^4}e^{-cm/u^2}.                 \tag{3.7}
\]

Since

\[
 B_m\asymp{4^m\over m^{3/2}},
\]

the ratio of (3.7) to \(B_m/\sqrt m\) is at most

\[
 Cx^4e^{-cx^2},
 \qquad x={\sqrt m\over u}.                       \tag{3.8}
\]

The dyadic sum \(x=1,2,4,\ldots\) converges. Heights
\(h\ge\sqrt m\) contribute at most

\[
 {1\over\sqrt m}\sum_hb_{m,h}\le{B_m\over\sqrt m}. \tag{3.9}
\]

Equations (3.7)--(3.9) prove the upper half of (0.2).

For sharpness, take

\[
 h_0=\left\lfloor{A\sqrt m\over2}\right\rfloor.
\]

The two extremal terms \(j=1,h_0+1\) in (3.5) are nonnegative and give

\[
 M_{m,h_0}
 \ge {4\over h_0+2}\sin^2{\pi\over h_0+2}
       \left(2\cos{\pi\over h_0+2}\right)^{2m}
 \ge c_AB_m.                                       \tag{3.10}
\]

All but \(Z_H=o(B_m/N)\) of these roots remain in \(V_H\), and each has
weight at least \(1/(H+1)\). Hence

\[
 \mathcal T_{m,H}\ge c_A{B_m\over\sqrt m}.        \tag{3.11}
\]

Thus the reciprocal-height trace itself has critical order; no sharpening
of the spectral estimate can turn (0.3) into little-oh.

The inequalities in this section have the following near-equality meaning.
The small-height spectral term is exponentially suppressed when
\(h=o(\sqrt m)\); critical trace mass lies at Gaussian heights. The crude
high-height step (3.9) is only a constant-scale estimate, but (3.10) proves
that a fixed Gaussian band already has positive Catalan mass. Therefore a
packing of critical trace order cannot be removed solely by declaring
Gaussian height atypical.

## 4. Quantitative stability consequences

Let

\[
 \Delta(\mathcal P)=\mathcal T_{m,H}-|\mathcal P|.
\]

Equation (2.3) immediately gives the following exact consequences.

### 4.1 Relative height-gap contraction

If every interval in \(\mathcal P\) satisfies

\[
 {s(I)-h(I)\over h(I)+2}\ge\eta,
\]

then

\[
 \boxed{|\mathcal P|\le{\mathcal T_{m,H}\over1+\eta}.} \tag{4.1}
\]

More generally, for every \(\eta>0\),

\[
 \boxed{
 \#\left\{I\in\mathcal P:
 {s(I)-h(I)\over h(I)+2}\ge\eta\right\}
 \le {\Delta(\mathcal P)\over\eta}.}              \tag{4.2}
\]

The same statements hold fractionally with cardinality replaced by total
\(x\)-mass.

### 4.2 Near-saturation rigidity

If

\[
 |\mathcal P|=\mathcal T_{m,H}-o(B_m/\sqrt m),      \tag{4.3}
\]

then

\[
 \sum_{I\in\mathcal P}(s(I)-h(I))=o_A(B_m),        \tag{4.4}
\]

and the number of uncovered eligible long-cycle roots is

\[
 o_A(B_m).                                         \tag{4.5}
\]

Indeed \(h+2\le H+1=O_A(\sqrt m)\), so multiplying each of the first and
last defects in (2.3) by at most \(H+1\) proves (4.4)--(4.5).

For every fixed \(\varepsilon>0\), (4.2) consequently gives

\[
 \#\{I:s(I)-h(I)\ge\varepsilon\sqrt m\}
 =o_A(B_m/\sqrt m).                                \tag{4.6}
\]

Using (0.5), equation (4.4) is equivalently

\[
 \sum_{I\in\mathcal P}
 \left[p(I)-1+\sum_{j<h(I)-1}
 (s_j(I)-s_{j+1}(I)-1)\right]
 =o_A(B_m).                                        \tag{4.7}
\]

Thus a trace near-saturator is an approximate tiling by returns whose
nested chronology is minimal on average.

### 4.3 Exact limitation of the saving

If every Gaussian-height interval merely has \(s-h\ge1\), its extra trace
cost is only \(\Theta_A(m^{-1/2})\). Even
\(\Theta_A(B_m/\sqrt m)\) such intervals contribute only

\[
 \Theta_A(B_m/m)=o_A(B_m/\sqrt m)                  \tag{4.8}
\]

to the stability defect. Hence excluding literal equality, or proving one
extra PBBS step, gives no leading-order contraction. A constant-factor
contraction requires \(s-h=\Omega_A(\sqrt m)\), and a little-oh estimate
from support/height ratio alone requires that ratio to diverge.

The known positive-winding critical formal family has \(s-h=1\), while
every genuine zero-winding return has \(s-h=0\). These are exactly the two
sectors invisible at leading order to (4.1).

## 5. Proved boundary

The audited \(O_A(B_m/\sqrt m)\) quotient bound is correct with all support
endpoints and floors included. Its complete chain of inequalities is:

1. height is exactly constant on a quotient cycle;
2. the height-gap theorem gives \(s\ge h\);
3. each return support contains exactly \(s+2\) quotient edges;
4. edge-capacity double counting gives the exact identity (0.4);
5. the Dyck path-graph spectrum and dyadic summation give (0.2);
6. short quotient cycles cost only \(o_A(B_m/N)\).

The quantitative stability advance is (2.3): it identifies every unit of
loss as nested height-gap slack or uncovered reciprocal edge mass. It also
shows exactly why this lane stops at critical big-oh. The unresolved family
consists of genuine PBBS returns with equality or bounded additive slack
whose supports almost tile the Gaussian-height quotient cycles. Excluding
that almost-tiling requires a chronology or cross-return collision theorem,
not a sharper marginal height estimate.
